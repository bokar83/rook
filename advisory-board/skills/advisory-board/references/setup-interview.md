# The Setup Interview

**Run this before creating any files.** It opens with a banner and a short letter, then eight questions. The whole thing takes about five minutes.

**The bar for this interview, and it is a hard one: the user finishes it by clicking, and the only thing they type is the name of their board.** Six of the eight questions are selectable choices. If you find yourself asking a ninth question, or turning a picker into a conversation, you have broken the thing that makes this worth opening twice.

---

## How to run this

- **Ask with the interactive picker wherever the answer is a small, discrete set.** `AskUserQuestion` renders selectable options: up to four questions per call, two to four options each. **Typing is the fallback, never the default.** A blank page produces vague answers, vague answers produce a generic board, and a generic board is the exact thing the user installed this to get away from.
- **Every question carries a free-text escape.** `AskUserQuestion` supplies an "Other" box automatically. Say so in the question text where it matters, so nobody feels boxed in. **A typed answer is written into the profile word for word and outranks the picked option on every later run.** Never paraphrase it into a category.
- **Put the recommended option first and mark it "(Recommended)"** where a recommendation is honest. Some questions carry none, and those are marked below.
- **Any multi-select where "none" is a real answer carries an explicit "None" option, first in the list**, because an empty multi-select cannot be submitted.
- **Two picker calls of four questions each.** Questions 2 to 5 in the first call, 6 to 8 plus nothing else in the second. Question 1 is asked on its own, first, because it changes what everything after it is called.
- **`Say:` blocks are the words to use, close to verbatim. Trim to fit, never expand. A blockquote without `Say:` is a note to you and is never spoken.**
- **Say it in plain language.** Nothing you say out loud carries a file path, a flag, a setting name, or a system word like "profile", "rubric", "slot", "on disk", or "artifact". Name each thing by what it does for them. These notes are technical. What you say is not.
- **The author's letter is the one fully verbatim block.** Do not paraphrase it, extend it, or add a line after it. It is signed by a person.
- **No em-dashes, in anything you say or write.** Use a full stop, a comma, or a colon instead. This covers every spoken line, every file, and every summary, and it gets missed on the first pass unless you check for it deliberately.
- **Never celebrate.** Somebody opening this is usually about to make a hard call and may already be worried about it. Warm and matter-of-fact, never upbeat about the situation.
- **Announce nothing you will ask later.** Naming a setting before its question reads as a decision already made.

---

## Before anything: can this actually run here?

**Silent. A capability check, not a question.** This needs a place that can save files onto the user's own computer. Some surfaces answer the first question convincingly and save nothing, which means a user can finish the whole interview, believe they have a board, and have nothing at all. **Check before the banner, never after**, so nobody reads the letter and then gets turned away.

| Check | How | What it proves |
|---|---|---|
| **Write a file** | Write and delete a scratch file in the working folder | Their board has somewhere to live. This is the whole product. |
| **Read it back** | Read the scratch file before deleting it | A write that cannot be read back is not a save |

**Both pass: say nothing at all.** Go to the existing-board check, then the banner. A user in the right place never learns this happened.

**Either fails: stop.** Do not run the interview, do not print the banner, do not answer a decision question instead.

**Say:**

> Before we start: I cannot set up your board from here. I need to be over in Code, which is the part of Claude where I can save your board onto your own computer.
>
> It is still Claude, and it still works by chatting, so nothing changes for you except where we are talking.
>
> 1. Look down the left-hand side of this app for **Code**, and click it.
> 2. Start a new conversation there.
> 3. Say "help me set up my board of advisors" and I will pick up right here.

- **Then stop and wait.** Do not offer a reduced version, and do not offer to pressure-test one decision "in the meantime". A board built in a conversation that cannot save anything is gone the moment that conversation closes, and the user will believe it was kept.
- **Never name the failing check.** "I cannot write a file" means nothing to them. "I cannot save your board onto your computer" does.
- **Never say terminal, command line, CLI, or install.** Assume the person reading this has never opened a terminal. The Code tab is a chat box, and it is the only route to offer. `claude.com/claude-code` is the durable fallback if the menu wording has moved.

---

## Before you start: is there already a board here?

**Look for an existing board before the banner, in this order:** `Board/` in the working directory, then the working directory itself, then any single subdirectory containing `Board_Profile.md`. Any of `Board_Profile.md`, `How_It_Runs.md`, `Decisions_Log.md`, or `Standing_Rules.md` counts as a hit. **All three coming up empty means a first run: go straight to the banner and skip this section entirely.**

Only when one exists, stop and ask, because a fresh interview written over a live board destroys every correction they have made since setup.

**Picker,** single-select, header `Existing board`. **Say:**

> It looks like you already have a board set up in this folder. What would you like to do?

| Option | Description |
|---|---|
| **Update the one I have** (Recommended) | Keep it and just take your change. I skip the setup. |
| **Archive it and start fresh** | I move the old one into a dated folder, then set up a brand new board from scratch |
| **Set up a second board** | Leave the current one alone and build a new one in its own folder |

- **Update:** do not run the interview. Take the amendment, write it to the right file, confirm in one line, stop.
- **Archive and start fresh:** move the existing files into `Archived_Board_{{DATE}}/` inside the folder, say out loud that it is moved, then run the interview from the banner. **Build only from this interview's answers. Do not read the archived files and do not carry anything remembered from an earlier conversation into the new ones. A blank slate is the point.**
- **Second board:** leave the existing files untouched and run the interview into a new folder they name.

---

## The banner

**Print the three boot lines with a short beat between each, then the banner. No input, no question.**

```
> waking up ..................... ok
> seating five advisors ......... ok
> removing the one who agrees .... ok
```

```
══════════════════════════════════════════════════════════════════════

 █████╗  ██████╗  ██╗   ██╗ ██╗ ███████╗  ██████╗  ██████╗  ██╗   ██╗
██╔══██╗ ██╔══██╗ ██║   ██║ ██║ ██╔════╝ ██╔═══██╗ ██╔══██╗ ╚██╗ ██╔╝
███████║ ██║  ██║ ██║   ██║ ██║ ███████╗ ██║   ██║ ██████╔╝  ╚████╔╝ 
██╔══██║ ██║  ██║ ╚██╗ ██╔╝ ██║ ╚════██║ ██║   ██║ ██╔══██╗   ╚██╔╝  
██║  ██║ ██████╔╝  ╚████╔╝  ██║ ███████║ ╚██████╔╝ ██║  ██║    ██║   
╚═╝  ╚═╝ ╚═════╝    ╚═══╝   ╚═╝ ╚══════╝  ╚═════╝  ╚═╝  ╚═╝    ╚═╝   

         ██████╗   ██████╗   █████╗  ██████╗  ██████╗ 
         ██╔══██╗ ██╔═══██╗ ██╔══██╗ ██╔══██╗ ██╔══██╗
         ██████╔╝ ██║   ██║ ███████║ ██████╔╝ ██║  ██║
         ██╔══██╗ ██║   ██║ ██╔══██║ ██╔══██╗ ██║  ██║
         ██████╔╝ ╚██████╔╝ ██║  ██║ ██║  ██║ ██████╔╝
         ╚═════╝   ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═════╝ 

              Five advisors. None of them agree with you.

══════════════════════════════════════════════════════════════════════
```

> **Terminal text only.** No image, no spinner, no real animation. The beat between the boot lines is the whole effect and it is enough.

## The letter

**Lead with the title line, then say the letter word for word. It is the only verbatim block in this file. Do not add a line after it.**

**A Note From The Author**

> I built this because of the meetings.
>
> Ten years in global HR leadership for a Fortune 100 company, and I watched the same thing happen in room after room: a decision got made and nobody there was paid to disagree with it. The plan got nodded at. Everyone went back to work. Six months later we found out what we had all assumed.
>
> So this is the room I wish I had. Five advisors, each with one job, and none of those jobs is agreeing with you. You tell it what you are deciding. It tells you what is wrong with it, what you are optimizing for that you did not choose on purpose, how it reads to somebody outside your industry, and what has to happen Monday morning.
>
> It will not make the call for you. That part stays yours.
>
> If it catches something before it costs you, send me a note on LinkedIn. That is the only thing I want back.
>
> Boubacar
> linkedin.com/in/boubacarbarry

> **Once, at setup, and nowhere else.** Never at the start of a run, never in a review file, never in a summary. A credit that reappears every time stops being a signature and becomes an advertisement, which damages the thing it is there to build.

## How this works

**Say:**

> Here is what happens. I ask you eight quick questions, most of them just pick-one or pick-any, and I save the answers as your board. After that, any time you are deciding something hard, you tell me what it is and five advisors go at it separately. One of them only looks for what will fail. One ignores your question and tells you what you are actually deciding. One looks for the bigger version you are not seeing. One reads it cold, from outside your world. One asks what happens Monday morning.
>
> Then you get one recommendation, not a menu, and I save the whole thing where you can go back to it.

---

## The eight questions

### 1. What do you want to call it?

**Free text. Asked on its own, first. The one deliberate exception to the picker rule, because a name cannot be enumerated.**

**Say:**

> First, what do you want to call your board? Some people name it after the room they wish they had, some after a person who used to tell them the truth, some just call it The Board. Anything you like.

**From here on, use that name in every file you write, and in the short summary at the end of every run. It is theirs, not mine.** If they say they do not care, propose "The Board" and move on. Do not push.

---

### 2 to 5: one picker call, four questions

> **Batch these four in a single `AskUserQuestion` call.** They are the context every advisor reads on every run.

**`What you run`,** single-select. **Say:**

> What are you building or running?

| Option | Description |
|---|---|
| **Solo consulting or services** | You sell your own time and expertise |
| **A small team or agency** | A handful of people, client work or your own product |
| **A product or software business** | You are building something people buy or subscribe to |
| **A team inside a bigger company** | You run something, but not the whole thing |
| **Something I am starting right now** | Early, pre-revenue, still deciding the shape of it |

*(The automatic "Other" box takes anything that does not fit. Write it in word for word.)*

**`Kind of calls`,** multi-select. **Say:**

> What kind of decisions do you want it for? Pick any.

| Option | Description |
|---|---|
| **Everything, do not narrow it** (Recommended) | Bring it whatever is hard that week |
| **Money and pricing** | What to charge, what to spend, what to stop spending |
| **People and hiring** | Who to bring on, who to let go, how to structure a team |
| **Product and what to build** | What to build, what to kill, what to say no to |
| **Commitments and partnerships** | Contracts, partners, co-founders, anything hard to get out of |

**`What it costs`,** multi-select. **Say:**

> When you get one of these wrong, what does it actually cost you? Pick any.

| Option | Description |
|---|---|
| **Money I cannot get back** | Real spend, and no way to unwind it |
| **Months I cannot get back** | Time is the expensive part, not the cash |
| **A relationship that matters** | A partner, a client, a friend, somebody on the team |
| **How people see me** | Reputation, credibility, being taken seriously next time |
| **All of it. This one is big.** | Bet the business |

> **This sets the pressure.** A reversible call and a bet-the-business call must not come back with the same intensity. Write the picked items into the profile as written and let the master prompt read them.

**`Who checks you`,** single-select. **Say:**

> Who is already checking your thinking before you commit?

| Option | Description |
|---|---|
| **Nobody. That is why I am here.** | No real check exists today |
| **A partner or co-founder** | Somebody with skin in it who will push back |
| **A board or investors** | A formal check, on their own schedule |
| **A mentor or a coach** | Somebody outside it who knows you |
| **My team, but they work for me** | People who could push back and mostly do not |

> **This changes volume, not content.** "Nobody" means the board is the only check they have and it says the uncomfortable thing plainly rather than gently. "A partner or co-founder" means it can assume some pushback already happened and go looking for what both of them are missing together.

---

### 6 to 8: one picker call, plus one optional free-text

**`Never suggest`,** multi-select, **"None" first. Say:**

> Anything the board should never suggest to you? Pick any, or None.

| Option | Description |
|---|---|
| **None. Nothing is off the table.** | Say anything |
| **Never suggest raising money** | Outside money is not a route I want |
| **Never suggest firing anyone** | Do not solve it with headcount |
| **Never suggest taking on debt** | Borrowing is not on the table |
| **Never suggest walking away from a commitment** | I keep what I said I would do |

> **This is their veto list and it is honored absolutely.** A run that proposes something on it has failed, no matter how good the reasoning was.

**`How hard`,** single-select. **Say:**

> How hard should the tough one push?

| Option | Description |
|---|---|
| **Standard. Push me, but stay useful.** (Recommended) | Direct, specific, no softening, still something you can act on |
| **Turn it up. I want the hardest version.** | Blunt. Assume the plan is wrong and go find where |
| **Ease off. I am early and I need momentum.** | Still honest about the risk, but it leads with what is workable |

> **This is a calibration, and it makes the hard pass something they chose rather than something that happened to them.** "Ease off" never becomes flattery. It changes the order and the tone, never the finding. Say that plainly if they ask.

**Then, question 6, asked as plain text because it genuinely cannot be enumerated. Offer the skip in the same breath. Say:**

> Last one, and you can skip it. Is there anything you have already looked at and ruled out? A direction you killed, an option people keep suggesting that is not happening. If there is nothing yet, just say so.

> **Write whatever they say into the do-not-re-propose list word for word, along with today's date.** This is the single question that stops the board wasting a whole section telling them to do the thing they killed in March. **If they skip it, leave the list empty and move on. Never push a second time.**

---

## After the interview

Work through these in order. Keep every spoken line plain.

1. **Write the four files** per `references/scaffolding.md`, using their chosen name throughout.

2. **Say in one or two lines what you saved and whether they have to touch it.** It holds what they told you, and it is saved on their own computer and nowhere else. **They never need to open it.** The way they change anything later is to say so, and you edit it. Do not list file names or folders.

3. **Say plainly which answers were thin.** Any question they answered with a single word, skipped, or picked the broadest option on. **Say:**

   > Two things worth knowing. Your answers on {the thin ones} are pretty broad, so the first couple of runs will be more general than they will be later. Tell me when a run misses and I will fix it. Most boards get properly useful around the third one.

4. **Tell them how to start, in one line, and then stop talking. Say:**

   > That is it. Whenever you have something hard to decide, just tell me what it is. If you want to know how it fails instead, say premortem.

5. **Do not run a session unprompted.** They set this up, which is not the same as having a decision ready right now. **Never end setup by asking what they want to pressure-test.** If they bring one, run it.
