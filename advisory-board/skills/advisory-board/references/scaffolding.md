# File Scaffolding

What gets written to the user's own computer at setup, what each file holds, and where every answer lands.

**Write these only after the interview is finished.** Nothing here is created early, and nothing is created for a user who stopped partway.

---

## The folder

Everything lives in one folder in the working directory. Default it to `Board/` and do not ask them to choose a location. A user who wants it somewhere else will say so.

```
Board/
  Board_Profile.md          who they are and what this board is calibrated to
  How_It_Runs.md            the method in effect, and only their deviations from it
  Decisions_Log.md          what they brought, what came back, what they did
  Standing_Rules.md         rules learned after setup
  Reviews/
    2026-09-04-pricing.md   one file per run, kept forever
```

**Four files, not one.** A single file grows by accretion: context, method, history, and the reasoning behind each rule interleave until nothing is findable. Splitting now is free. Splitting in two months is a migration.

**`{{BOARD_NAME}}` is whatever they answered to question 1** and it goes in the header of every file. **`{{TODAY}}` is today's date, `YYYY-MM-DD`.**

---

## Read contracts

What a run reads, and what it costs. Keep these true as the files grow.

| File | Read when | Note |
|---|---|---|
| `Board_Profile.md` | **Every run, in full.** It fills the master prompt's slots. | Keep it short enough to stay readable in full forever. If it passes roughly 200 lines, something belongs in `Standing_Rules.md` instead. |
| `Standing_Rules.md` | **Every run, in full.** | Append-only, one rule per line. |
| `Decisions_Log.md` | **Every run, the do-not-re-propose table only.** | The history table can grow without limit because no run reads it. Read the whole file only when the user asks about their own history. |
| `How_It_Runs.md` | **Only when the user asks how it works, or wants to change it.** | It records deviations. It never copies the method in. |

---

## `Board_Profile.md`

Every field maps to one interview answer. **A field with no answer is written as `not set` and never guessed.**

```markdown
# {{BOARD_NAME}}

Set up {{TODAY}}. This is the file the board reads before every session. Everything
here came from the setup conversation. To change any of it, just say so.

## What they run
{{Q2 answer, or their typed answer word for word}}

## The kinds of calls this board is for
{{Q3 answers, comma separated}}

## What a wrong call costs
{{Q4 answers, comma separated}}

## Who already checks their thinking
{{Q5 answer}}

## Never suggest
{{Q7 answers, one per line. If they chose None, write: Nothing is off the table.}}

## How hard the tough one pushes
{{Q8 answer}}

## Built with
A board of advisors for Claude Code by Boubacar Barry.
https://linkedin.com/in/boubacarbarry
MIT licensed.
```

- **The typed answer wins.** Where a user used the free-text box on a picker question, write their words, not the option they also touched, and not your summary of them. **Their sentence goes in the slot at run time exactly as they wrote it.**
- **The "Built with" block is written once, here, at setup, and nowhere else.** It is not printed at the start of a run, not repeated in a review file, and not spoken in a summary. It sits in a file they will rarely open, which is the correct amount of credit.

---

## `How_It_Runs.md`

**This file cites the method. It never copies it in.** A copy drifts from the original and then the board is running two versions of itself.

```markdown
# How {{BOARD_NAME}} Runs

Set up {{TODAY}}.

## The method
Five advisors, each with one job, working independently. One looks only for what
will fail. One ignores the question as asked and names what is actually being
decided. One looks for the bigger version. One reads it cold, from outside the
industry. One asks what happens Monday morning. Then a cross-review, a synthesis
with one recommendation, and one next step.

The full method lives in the skill, and it is the same for everybody. This file
records only what is different here.

## In effect for this board
- The tough one pushes at: {{Q8 answer}}
- Never suggests: {{Q7 answers}}
- Premortem is available any time. Say premortem and every advisor speaks from six
  months in the future about a decision that already failed.

## Deviations from the standard method
None yet.

## What a failed run looks like
Five sections that agree with each other. If a session comes back and every part
of it says roughly the same thing, say so and it gets run again.
```

---

## `Decisions_Log.md`

**Two tables. Only the second one is read by a run.**

```markdown
# {{BOARD_NAME}} Decisions Log

## History

| Date | What was decided | What came back | What they actually did | Why |
|---|---|---|---|---|

## Do not re-propose

Things already looked at and ruled out. The board does not raise these again.

| Ruled out | When | Why |
|---|---|---|
{{Q6 answer, one row per item, dated {{TODAY}}. If they skipped it, leave the
table empty with no placeholder row.}}
```

- **Append a history row after every run.** Fill the date, the decision, and the recommendation. **Leave "what they actually did" and "why" blank.** They get filled when the user says what they did, and never guessed.
- **Add a do-not-re-propose row whenever they rule something out**, in a run or in passing. Ask nothing. Record it and mention it in one line.
- **This is the file that makes a board better than a chat.** A chat forgets that they killed the partnership idea in March. This does not.

---

## `Standing_Rules.md`

```markdown
# {{BOARD_NAME}} Standing Rules

Rules learned after setup. To add one, say "make a rule".

| Rule | Added | What prompted it |
|---|---|---|
```

**"Make a rule" is the trigger phrase**, and it is the last thing said at the end of setup. When they use it: write the rule in their words, date it, note what prompted it, confirm in one line, and honor it from the next run on. **Never argue with a rule.** If it conflicts with an earlier one, say which two conflict and ask which wins.

---

## `Reviews/<date>-<slug>.md`

One file per run. **Never overwritten, never deleted.** If a file with that name already exists, append `-2` rather than replacing it.

```markdown
# {{TODAY}}: {{the decision in one line}}

Mode: standard
Board: {{BOARD_NAME}}

{{the full seven-section output, exactly as produced, nothing trimmed}}
```

**The full output goes in the file. The conversation gets four lines.** That split is the point: a pressure test they can reopen at six the next morning, forward to a partner, or reread after sleeping on it is worth ten times one that scrolled past in a chat window.

---

## After writing the files

**Say in one or two plain lines what you saved.** It holds what they told you, it is on their own computer and nowhere else, and they never need to open it. **Do not list file names, do not say "profile" or "scaffolding", and do not show them the folder.** The way they change anything is to say so.
