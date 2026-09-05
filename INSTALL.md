# Installing Rook

Two ways in. Use the first one. The second is a backup for the day the first one does not cooperate (Anthropic has changed plugin marketplace behavior before without warning, so this guide keeps a working fallback at the bottom on purpose).

This repository is private. You need GitHub access to `bokar83/rook` before either method below will work.

## Method 1: Claude Plugin Marketplace (use this first)

1. Open the Claude desktop app. First time using Claude Code? In a chat, type *"Help me set up Claude Code"* and follow the prompts.
2. Click **Customize** in the left sidebar, then the **Plugins** tab.
3. In the top right, click **Add**, then **Add marketplace**.
4. Type `bokar83/rook` into the box, then click the **rook** suggestion that appears underneath it. Do not press Enter. That box is a repository picker, not a plain text field, so the name has to be picked before anything happens.
5. Click **Sync**.
6. **Rook** appears in the list. Click **Install**.
7. Start a **new conversation in Claude Code**. It will not appear in one that is already open.
8. Say: *"Help me set up my board of advisors."*

Nothing happening? Close Claude, open it again, and repeat step 7.

To update later: open the same Plugins screen and click **Sync**.

### Terminal version of Method 1

Open a terminal, run `claude`, then:

```
/plugin marketplace add bokar83/rook
```

```
/plugin install rook@rook
```

`rook@rook` is correct: the plugin's name, then the marketplace it came from. If the install summary says `Run /reload-plugins to activate`, run that.

## Method 2: Direct from GitHub (backup, if Method 1 does not show Rook)

Skip straight here if the marketplace step above will not sync, will not list the plugin, or the Install button does nothing after two tries.

1. Go to `https://github.com/bokar83/rook` (sign in first, the repo is private).
2. Get a local copy, either way works:
   - **Clone:** `git clone git@github.com:bokar83/rook.git` (or the HTTPS URL if you have not set up an SSH key with GitHub)
   - **Download ZIP:** click the green **Code** button, then **Download ZIP**, then extract it
3. Note the path to the `rook` folder inside what you just cloned or extracted: that is the plugin itself, not the whole repo. For example: `C:\Users\<you>\Downloads\rook\rook` on Windows, or `~/Downloads/rook/rook` on Mac.
4. Open a terminal and run Claude Code pointed straight at that folder:

```bash
claude --plugin-dir "/path/to/rook/rook"
```

5. In that session, say: *"Help me set up my board of advisors."*

`--plugin-dir` loads the plugin for that session directly off your disk, no marketplace sync involved. It is the same folder Method 1 would have installed, just pointed at by hand. Run the same command again (with the same path) any time you want to use it; there is nothing else to install or configure.

## After either method

Say what you are deciding. That is the whole interface. If a session goes too easy on you, say so: it changes.

See [README.md](README.md) for what it does, what it will not do, and what it touches on your machine.
