---
name: writing-principles
description: How AI4Read posts are written. Read before drafting or revising any post; update after every review round (add the rule, the note that caused it, and the date).
version: 0.3 (2026-10-16)
---

# AI4Read writing principles

The charter (§5–7) fixes the post template, style and audio. This file says *how to explain*. It grows from Kunhao's review notes: every rule cites the note that produced it, so we can see why it exists and change it when it stops helping.

## 1. The reader
- Write for a **curious high-school student who will not accept hand-waving**. Kunhao is a professor, but in every field outside his own he wants the explanation a strong 17-year-old could follow, without missing any step a graduate would need.
- Simple words, **complete content**. Simplify the language, never the substance: no skipped steps, no dropped conditions, no "it can be shown".

## 2. The ladder for every new idea
Every new concept or important question climbs the same ladder, in this order:
1. **A concrete instance first**: a story, a puzzle or a small case with real numbers (the guessing game, 32 cups of water, a four-word weather report).
2. **What happens in the instance**, step by step, in plain words.
3. **The general pattern**: what stays the same if we change the numbers.
4. **The formula**, introduced as a short name for the pattern, with every symbol read aloud in words.
5. **A check**: plug the instance back into the formula and get the same number.
6. **Where it breaks or what it does not say**: limits, conditions, hedges from the source.
Do not start a concept at step 4. (Note: “imagine you are explaining it to high school students … use instances or illustrations … as ladders”, 2026-10-16.)

## 3. Terms
- Every citation links to its source entry (hover or tap shows the full reference with a Copy button). (Note, 2026-10-16.)
- Define every technical term **at first use, in the sentence where it appears**, with an everyday comparison (held-out data = exam questions that were not in the homework).
- If a term needs more than one sentence, give it a **term box** (`.term`): name, plain definition, one example, why it matters here. (Note on “held-out”, 2026-10-15.)
- Never use a term in a formula or figure before it is defined in the text (fact-check minor 22, 2026-10-15).

## 4. Explanations live in the main text
- An explanation the argument needs goes **into the paragraph itself**, not into a side box. Boxes are only for (a) term definitions, (b) traps (naming conflicts, version conflicts), (c) answers to the guess-first questions, (d) exercises, (e) optional **deep-dive fold-outs** ("Look inside: …") that go one level deeper while the main text still stands alone; a deep dive uses one notation, worked toy numbers and a small diagram, and the audio only mentions that it exists. (Note on Step 5 attention, 2026-10-16.) (Note: “Instead of adding a WHO DOES WHAT inbox … integrate the explanation into the text”, 2026-10-15.)
- When an idea has roles (who sends, who receives, who encodes, who decodes), **name the roles explicitly** and walk one tiny example through them. (Comment on Shannon's twin, 2026-10-15.)

## 5. Illustrations
- Every **mechanism** (an architecture, a procedure, an experiment's setup) gets a picture: an inline SVG diagram or a small interactive. Words alone are not enough for “the hidden layer was removed” or “the object is *on* the box instead of *in* it”. (Notes on Step 4, Step 5, prediction 3, 2026-10-15.)
- Interactives must let the reader **change one thing and see the effect** (a slider, a tap on a word). Label invented numbers as “toy numbers”.
- Diagrams follow the theme tokens and are readable at 375 px.

## 6. Formulas
- Show the formula the reader will meet in the field (e.g. the machine-learning cross-entropy $H(p,q)=-\sum_x p(x)\log q(x)$), even when the source writes it differently, and connect the two. (Note on cross-entropy, 2026-10-15.)
- Derivations that a reader can do in five minutes become **exercises** with a hint and a folded solution, not finished text.
- Every number in a formula example is checked by running code.

## 7. Big claims need “what it means”
- After any headline result (a scaling law, a theorem, a test score), answer three questions in plain words: **what was measured, on what, and what it lets you predict** — then what it does *not* show. (Note on Step 8, 2026-10-15.)

## 8. The English section
- Two layers: (a) 8–10 phrases from the post's own topic (B2–C1), (b) a **B2 → C1 toolkit**: native expressions for discussing evidence (hedging, concession, emphasis), one or two sentence patterns, small error fixes typical for Chinese/Japanese speakers, and a short practice routine. Every example sentence uses an idea from the same post. (Request, 2026-10-16.)
- Rotate the toolkit: each post adds new expressions and repeats 2–3 from earlier posts for spaced review.

## 8b. Audio
- Every audio file names its source as **“AI4Read from CSS Lab”**: spoken in the first chapter (“Welcome to AI4Read from CSS Lab.”) and written into each MP3's metadata (artist, album artist, publisher, copyright, comment with the post link; album = post title; title and track = chapter). `scripts/tts_post.py` tags automatically through `scripts/tag_audio.py`. (Request, 2026-10-17.)

## 9. Sources and honesty (from the charter, kept here so it is never forgotten)
- Every claim is checked against the cited page by an independent reviewer before publishing; digests are maps, not truth.
- Keep the authors' hedges (may, suggest, appears). Our own examples and reasoning are labelled “ours”.
- When an error is found in a post, fix the digest and the source brief too.

## 10. Change log
- 0.1 (2026-10-15): charter style guide only.
- 0.3 (2026-10-16): §8 English section with a B2 → C1 toolkit.
- 0.2 (2026-10-16): §2 ladder, §3 term boxes, §4 explanations in text, §5 illustrations for mechanisms, §6 field formulas + exercises, §7 “what it means”. From Kunhao's first review of post 01.
- 0.4 (2026-10-17): §8b audio files carry the source mark “AI4Read from CSS Lab”.
