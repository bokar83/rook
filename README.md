# Rook

Five advisors who pressure-test a decision instead of agreeing with it.

You set it up once, in about five minutes, mostly by clicking. It saves your own board onto your own computer. After that, whenever you have a call that is hard to undo, you tell it what you are deciding and five advisors go at it separately. One of them only looks for what will fail. One ignores the question you asked and tells you what you are actually deciding. One looks for the bigger version you cannot see from inside it. One reads it cold, from outside your industry. One asks what happens Monday morning.

You get one recommendation, not a menu. Keep, change, or kill. It is saved to a file you can reopen at six the next morning.

**It never makes the call for you. That part stays yours.**

Free, MIT licensed, and it runs entirely on your own machine.

## Install

**You need the [Claude](https://claude.com) desktop app.** It is free to download.

1. Open Claude. **First time using Claude Code?** In a chat, type *"Help me set up Claude Code"* and follow the prompts.
2. Click **Customize** in the left sidebar, then the **Plugins** tab. Plugins are free add-ons for Claude.
3. In the top right, click **Add**, then **Add marketplace**.
4. In the box, type `bokar83/rook`, then click **Sync**. Do not press Enter, and ignore any repository suggestions that pop up.
5. **Rook** appears in the list. Click **Install**.
6. Start a **new conversation in Claude Code**. It will not appear in one that is already open.
7. Say: *"Help me set up my board of advisors."* Or type **`/rook`**, which does the same thing.

**Nothing happening?** Close Claude, open it again, and try step 6.

**To update later:** open the same Plugins screen and click **Sync**.

> **Do not type `/plugin` commands into the Claude app's chat box.** Those only work in a terminal, and the steps above need no terminal at all.

<details>
<summary><b>Using the Claude Code terminal instead</b></summary>

Open a terminal, run `claude`, then type:

```
/plugin marketplace add bokar83/rook
```

```
/plugin install rook@rook
```

`rook@rook` is correct: the plugin's name, then the marketplace it came from. If the install summary says `Run /reload-plugins to activate`, run that.

To try it for one session without installing anything:

```bash
claude --plugin-dir /path/to/rook
```

</details>

## Using it

Say what you are deciding. That is the whole interface.

You can also call it directly. Type **`/council`** or **`/rook`** in any conversation and it opens, whether or not you word anything the way it expects. Both do exactly the same thing, so use whichever you remember. Put the decision on the same line if you have one ready:

```
/council should I take the smaller contract to keep the month full
```

On its own, `/rook` sets your board up if you do not have one yet, and asks what you are deciding if you do.

> *"I want to raise my rates by 40% and I am about to tell three clients."*
>
> *"Should I take on a co-founder for this, or hire?"*
>
> *"Pressure-test this launch plan before I commit the money."*

If you would rather see how it goes wrong than whether to do it, say **premortem**. Every advisor then speaks from six months in the future about a decision that already failed, and works backwards from what killed it.

If a session goes too easy on you, say so. That is a setting, and it changes.

## What it will not do

- **It will not make the decision.** It tells you what is wrong, what you are really optimizing for, and what has to be true. You decide.
- **It will not tell you to spend money, send a message, hire somebody, or fire somebody.** That is a line it does not cross, on purpose.
- **It will not agree with you to be pleasant.** If five advisors come back saying the same thing, that is a failed session, not a good sign, and it will run again.
- **It will not suggest anything you told it not to.** At setup you name your own off-limits list, and it is honored absolutely.

## What it touches

Your own computer, and nothing else.

- It writes your board and every session to a folder on your machine. That is the only thing it saves.
- **There is no account, no sign-up, no email, no server, and nothing sent anywhere.** No part of this reports back to me. Nothing about you, your board, or anything you decide ever leaves your machine.
- **The one thing I can see is what GitHub shows any repository owner**, which is a count of how many people cloned or looked at the page, plus the names of anyone who stars it. That is the platform, not this tool. It tells me nothing about who you are or what you brought to your board.
- It reads nothing outside the folder it writes to.
- **Every saved session ends with an invisible version tag**, written as an empty HTML comment on the last line. It records which version of this tool wrote the file, it renders as nothing, and it never leaves your machine. Delete it if you like. Nothing breaks.
- It needs no API key. It runs on the Claude subscription you already have.

## Author

Built by Boubacar Barry. I help companies put AI to work without the confusion and the overwhelm. This one came out of ten years in global HR leadership for a Fortune 100 company, watching decisions get made in rooms where nobody was paid to disagree with them.

If it catches something before it costs you, send me a note: [linkedin.com/in/boubacarbarry](https://linkedin.com/in/boubacarbarry)

## Licence

MIT. Use it, change it, fork it, ship your own version of it. See [LICENSE](LICENSE).
