# -*- coding: utf-8 -*-
"""Maintainer-only. Verifies the package and builds the fallback zip.

Run from anywhere:  python build_package.py

This script is NOT part of the plugin and never reaches a user. A marketplace
install copies only the plugin directory, and this file sits outside it. The
plugin itself is markdown and needs no build step; this exists to catch the
packaging mistakes that are invisible until somebody else tries to install.

Why a script rather than a one-line Compress-Archive: Windows PowerShell writes
backslash separators into zip entry names, which is out of spec and fails to
extract correctly on macOS and Linux.
"""
import json
import os
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PLUGIN_DIRNAME = "advisory-board"
PLUGIN = os.path.join(HERE, PLUGIN_DIRNAME)
OUT = os.path.join(HERE, PLUGIN_DIRNAME + ".zip")

SKIP_DIRS = {"__pycache__", ".git", ".pytest_cache"}
SKIP_EXTS = {".pyc", ".pyo"}

# Terms that must never reach a public file, one per line, read from a local
# file that is not committed. The list itself would be the leak if it were
# published here, so it lives outside the repo's tracked content. Absent file
# means the check is skipped with a printed notice rather than silently passing.
LEAKTERMS = os.path.join(HERE, ".leakterms")


def fail(msg):
    sys.exit("FAIL: " + msg)


def check_licenses():
    root_lic = os.path.join(HERE, "LICENSE")
    plugin_lic = os.path.join(PLUGIN, "LICENSE")
    if not os.path.isfile(root_lic):
        fail("no LICENSE at repo root; GitHub needs one there to detect the licence")
    if not os.path.isfile(plugin_lic):
        fail("no LICENSE in %s; a marketplace install copies only the plugin dir" % PLUGIN_DIRNAME)
    if open(root_lic, "rb").read() != open(plugin_lic, "rb").read():
        fail("the two LICENSE copies disagree; make them byte-identical")
    print("ok   LICENSE present in both places and byte-identical")


def check_manifests():
    mkt_path = os.path.join(HERE, ".claude-plugin", "marketplace.json")
    plg_path = os.path.join(PLUGIN, ".claude-plugin", "plugin.json")
    for p in (mkt_path, plg_path):
        if not os.path.isfile(p):
            fail("missing manifest: %s" % p)
    try:
        mkt = json.load(open(mkt_path, encoding="utf-8"))
        plg = json.load(open(plg_path, encoding="utf-8"))
    except ValueError as exc:
        fail("a manifest does not parse as JSON: %s" % exc)

    entries = mkt.get("plugins") or []
    if len(entries) != 1:
        fail("marketplace.json should list exactly one plugin, found %d" % len(entries))
    entry = entries[0]

    if entry.get("name") != plg.get("name"):
        fail("plugin name disagrees between the two manifests: %r vs %r"
             % (entry.get("name"), plg.get("name")))
    if entry.get("version") != plg.get("version"):
        fail("version disagrees between the two manifests: %r vs %r"
             % (entry.get("version"), plg.get("version")))

    src = (entry.get("source") or "").lstrip("./")
    if src != PLUGIN_DIRNAME:
        fail("marketplace source %r does not point at the plugin dir %r" % (src, PLUGIN_DIRNAME))

    # Both manifests, not just the marketplace one. A marketplace install copies
    # only the plugin dir, so the plugin manifest is the one a user ends up with.
    for label, block in (("marketplace", entry.get("author") or {}),
                         ("plugin", plg.get("author") or {})):
        if "linkedin.com" not in (block.get("url") or ""):
            fail("the %s author entry is missing the LinkedIn URL" % label)
    print("ok   both manifests parse, agree on name and version, and carry the author link")


def check_no_leaks():
    # Fail closed. A missing list used to print SKIP and still exit green, which
    # meant any other clone got an "all checks passed" with no leak check run at
    # all. A gate that defaults to pass is the failure it exists to prevent.
    if not os.path.isfile(LEAKTERMS):
        if "--no-leak-check" in sys.argv:
            print("SKIP leak check waived by --no-leak-check")
            return
        fail("no .leakterms file next to this script, so the leak check cannot run.\n"
             "      Create it with one term per line, or pass --no-leak-check if you\n"
             "      genuinely do not have the list. It is gitignored on purpose.")
    terms = [t.strip().lower() for t in open(LEAKTERMS, encoding="utf-8")
             if t.strip() and not t.startswith("#")]
    if not terms:
        fail(".leakterms exists but is empty")
    hits = []
    for dirpath, dirnames, filenames in os.walk(HERE):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            if os.path.abspath(full) == os.path.abspath(LEAKTERMS):
                continue
            if os.path.splitext(fn)[1] in SKIP_EXTS or fn.endswith(".zip"):
                continue
            try:
                body = open(full, encoding="utf-8", errors="ignore").read().lower()
            except OSError:
                continue
            for term in terms:
                if term in body:
                    hits.append((os.path.relpath(full, HERE), term))
    if hits:
        for rel, term in hits:
            print("LEAK %s -> %r" % (rel, term))
        fail("%d internal name(s) found in public files" % len(hits))
    print("ok   no internal names found in any public file")


def check_no_em_dashes():
    hits = []
    for dirpath, dirnames, filenames in os.walk(HERE):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if not (fn.endswith(".md") or fn.endswith(".json")):
                continue
            full = os.path.join(dirpath, fn)
            body = open(full, encoding="utf-8", errors="ignore").read()
            if "—" in body:
                hits.append(os.path.relpath(full, HERE))
    if hits:
        for rel in hits:
            print("EM-DASH %s" % rel)
        fail("em-dashes found in public copy")
    print("ok   no em-dashes in any public copy")


def check_no_unfilled_slots():
    """The master prompt is allowed to carry {{SLOTS}}. Nothing else is."""
    voices = os.path.join(PLUGIN, "skills", PLUGIN_DIRNAME, "references", "the-five-voices.md")
    if not os.path.isfile(voices):
        fail("the master prompt file is missing: %s" % voices)
    body = open(voices, encoding="utf-8").read()
    for slot in ("{{BOARD_NAME}}", "{{THE_DECISION}}", "{{MODE}}"):
        if slot not in body:
            fail("the master prompt is missing the %s slot" % slot)
    print("ok   the master prompt exists and carries its named slots")


def build_zip():
    if os.path.exists(OUT):
        os.remove(OUT)
    written = []
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        for dirpath, dirnames, filenames in os.walk(PLUGIN):
            dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
            for fn in sorted(filenames):
                if os.path.splitext(fn)[1] in SKIP_EXTS:
                    continue
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, PLUGIN).replace(os.sep, "/")
                z.write(full, PLUGIN_DIRNAME + "/" + rel)
                written.append(rel)
    with zipfile.ZipFile(OUT) as z:
        assert not [n for n in z.namelist() if "\\" in n], "backslash entry names"
        assert z.testzip() is None, "zip failed integrity check"
    print("ok   built %s (%.1f KB, %d files)"
          % (os.path.basename(OUT), os.path.getsize(OUT) / 1024.0, len(written)))
    for rel in written:
        print("       " + rel)


def main():
    if not os.path.isdir(PLUGIN):
        fail("no plugin directory at %s" % PLUGIN)
    check_licenses()
    check_manifests()
    check_no_leaks()
    check_no_em_dashes()
    check_no_unfilled_slots()
    build_zip()
    print("\nall checks passed")


if __name__ == "__main__":
    main()
