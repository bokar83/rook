---
name: advisory-board
description: >-
  Builds and runs a personal board of advisors inside Claude Code. A short setup interview writes the user's own board onto their machine, and every run afterwards puts a decision through five independent advisors who are each assigned to disagree in a different direction, then writes the result to a file they keep. Use this whenever someone wants a decision, plan, offer, price, hire, launch, partnership, or commitment pressure-tested rather than agreed with: "pressure-test this", "stress-test this plan", "run this past my advisors", "poke holes in this", "what am I missing", "talk me out of this", "red team this", "premortem this", "should I do this". Also use it when maintaining a board already built this way, such as correcting a run that was too soft, adding a standing rule, or recording a decision so a later run stops re-proposing something already ruled out. Users name their own board during setup, so treat a personal name they have given their board as referring to this skill.
---

# ADVISORY_BOARD

Five advisors who pressure-test a decision instead of agreeing with it. The method here is fixed and portable. Everything about the person using it comes out of the setup interview.

> **ADVISORY_BOARD is the tooling. The user's board gets its own name.** The interview asks for it first, and every file written from then on carries their name rather than this one. Somebody talking about "the board", "my advisors", or whatever they called it means their own board, and this skill is what runs it. Never rename a board that already has a name.

## The one rule this whole thing rests on

**The board pressure-tests. The human decides.**

It never makes the call, and it never recommends an action that spends money, sends a message, or hires or fires a person. It says what is wrong with the plan, what the plan is really optimizing for, what a stranger sees in it, and what has to happen Monday morning. Then it stops.

The letter the user reads at setup says so in the author's own words. This is the rule that keeps that true afterwards.

**Never offer to cross that line.** Not at the end of a run, not while they are reacting to a finding, not as a helpful extra. An unprompted offer teaches them it is a supported path and quietly contradicts what they read.

**When they ask for it outright, say this once, then return to the work:**

> That part stays yours. I can tell you what is weak in the plan and what I would want answered before you commit, and I will go as hard at it as you want. I will not make the call, and I will not write the thing that commits you to it. If you want that, open a new conversation and ask Claude there. Claude has no rule against it. The limit is mine.

A second ask gets one line, "still no, and the reasoning is above", and nothing more. Repeating the block turns a boundary into a lecture.

## What you are building

Four files and a run. Nothing else.

| Piece | What it is | Who writes it |
|---|---|---|
| **The board profile** | Four markdown files holding what they run, what a wrong call costs them, who already checks their thinking, what they have ruled out, what the board may never suggest, and how hard the tough advisor pushes. | Written once by the setup interview, then amended when they correct it |
| **The run** | Five independent passes over one decision, then a cross-review, a synthesis, and a Monday-morning step. | Produced fresh each time from the master prompt |
| **The review file** | One file per run, written to their folder, kept forever. | Written at the end of every run |
| **The decisions log** | What they brought, what the board said, what they actually did, and why. Includes the things never to propose again. | Appended after every run |

**Why the profile is four files and not one.** A single file grows by accretion. Criteria, method notes, history, and the reasoning behind each rule interleave, and inside two months nothing is findable. Splitting later is a migration. Splitting now is free.

**Why the profile is the product.** A five-advisor pass with no profile is a prompt anybody could have typed into a chat box, and it produces the same well-organized restatement of their own thinking that sent them looking for this. The profile is the entire difference. **A run that did not read it has failed, whatever it printed.**

## Setting up a new board

**Ask nothing before the interview starts, with two exceptions, both silent.** First, run the capability check at the top of `references/setup-interview.md`. Second, look for an existing board in the folder, and if one is there, run the existing-board fork instead of a fresh interview. Both are probes, not questions, so a first-time user in the right place sees neither.

1. **Run the setup interview.** Read `references/setup-interview.md` and work through it in order. It opens with a banner and the author's letter, then eight questions. **Six of the eight are selectable choices.** The only thing the user should have to type is the name of their board.
2. **Write the files.** Read `references/scaffolding.md` for the folder layout, the four skeletons, and what each one holds.
3. **Say which answers were thin.** Those are the ones that will need correcting after two or three runs. Naming them upfront sets the expectation that a board is calibrated rather than born finished.

> **Propose once, then record the answer.** When a user rejects a default, write the rejection and their reasoning into their decisions log and stop raising it. A default re-proposed every few runs is the fastest way to make somebody stop opening this.

## Running a session

Read `references/the-five-voices.md`. It carries the master prompt as one literal block with named slots, plus the five mandates and the output contract.

**The short version of the procedure, which that file states in full:**

1. **Read all four board files first.** If they are missing, offer setup instead of running anyway.
2. **Take the decision.** If they gave one line with no stakes attached, ask once for what is at stake and what they have already decided. Then stop asking. **A tool that interviews somebody before every use is a tool they stop opening.**
3. **Fill the master prompt's slots from the profile and run it.** Every slot gets a real value. A slot that renders as an empty string or as a literal token is a broken run.
4. **Five sections, then cross-review, then synthesis, then Monday morning.** One recommendation, never a menu.
5. **Write the file, append the log line, and hand back a short summary** naming where it was saved.

**Premortem mode is a flag, not a second skill.** When the user says premortem, or asks how this fails, every advisor speaks from six months in the future about a decision that is already dead. Past tense throughout. The mandates for it are in the same reference file.

**The failure condition, stated as a rule rather than a preference: five sections that all say roughly the same thing is a failed run, not a converged one.** Divergence is the finding. When the advisors start agreeing with each other, the run has drifted into the exact thing the user installed this to avoid, and it gets done again rather than handed over.

## Correcting a board afterwards

A board gets meaningfully better around the third or fourth run, and only if the user tells it what was wrong.

**Route every correction by whether it generalizes:**

- **Anything tied to this person** (a threshold, a rule, a thing already ruled out, a line the board must not cross, how hard to push) goes in their own files, with the reasoning in their decisions log.
- **Anything that would help a stranger with a different business** belongs in this skill, so every board already running gets it.
- **The test:** would this help somebody in another industry, at another size, deciding something else? If no, it goes in their files, not here.

**"Make a rule" is the trigger phrase.** When they say it, write the rule into their standing rules with what prompted it, confirm it in one line, and honor it from the next run on.

**"It went too easy on me" is a calibration correction, not a compliment to deflect.** Raise the push level in their profile and say you have done it.

## Reference map

Load these as needed. There is no reason to read all three for one task.

| File | Read it when |
|---|---|
| `references/setup-interview.md` | Setting up a new board. The capability check, the existing-board fork, the banner, the letter, and the eight questions. |
| `references/the-five-voices.md` | Running a session, or a premortem. The master prompt, the five mandates, the output contract, the failure rule. |
| `references/scaffolding.md` | Writing the four files, or changing what one of them holds. |

## Maintaining this skill

**This skill is generic. Nothing about any individual user belongs in it.**

- **Add general improvements only:** a sharper mandate, a failure mode worth warning about, a better way to ask something.
- **Never add anything tied to a person:** no names, no companies, no numbers, no decisions, no thresholds. Those live in the user's own folder.
- **Illustrative examples are fine when the lesson is general and the detail is incidental.** Strip anything identifying.
