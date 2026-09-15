---
name: council
description: Put a decision through your board of advisors, or set the board up if you do not have one yet. Five advisors pressure-test it instead of agreeing with it.
argument-hint: [the decision you are weighing, or leave empty]
---

Use the Rook skill and follow it from the top, including its routing step. It is at `${CLAUDE_PLUGIN_ROOT}/skills/rook/SKILL.md`, and its reference files are in `${CLAUDE_PLUGIN_ROOT}/skills/rook/references/`. **Never search the filesystem for them.** A `find` or `glob` rooted at `/` or at the home directory scans a stranger's whole disk to locate a file whose path you were already given.

The user typed a command rather than a sentence, so treat this as a deliberate request for the board and never answer the decision directly.

What they brought: $ARGUMENTS

If that is empty, they opened the board without saying what for. Look for an existing board first, silently, exactly as the skill says. If one exists, ask in a single sentence what they are deciding, then stop and wait. If none exists, start the setup interview.
