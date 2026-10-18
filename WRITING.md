---
name: writing-principles
description: How AI4Read posts are written. Read before drafting or revising any post. Claude updates it whenever a review round or a note from Kunhao shows a missing rule (add the rule, the note or finding that caused it, and the date); Kunhao asked for this on 2026-10-18.
version: 0.5 (2026-10-18)
---

# AI4Read writing principles

The charter (§5–7) fixes the post template, style and audio. This file says *how to explain*. It grows from Kunhao's review notes: every rule cites the note that produced it, so we can see why it exists and change it when it stops helping.

## 0. Every post stands alone
- A reader may open any post first. **Never cite or rely on another post** (“as in post 01”, “remember the village”). Re-introduce every toy world, term and result the post needs, from scratch. Spaced review still happens: recall questions and English expressions may repeat earlier material, without saying so. (Note, 2026-10-18.)
- A person's idea can be the **starting hint**, but the post is about the **question**, not about the person. Keep the account of what someone said short in the main text, and put the full list of their lines in a fold-out. (Note on post 02: “the introduction focused a little too much on what Harari said … it is an idea, a hint for us to explore”, 2026-10-18.)
- **Answer the question where the reader looks.** Give a one-line preview after the hook. Open the synthesis with a boxed **Short answer**, with one paragraph for each part of the question. Define any key term from the question at first use. (Post 02 critic round 1, 2026-10-17.)

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
Do not start a concept at step 4.
- A toy that illustrates a source's mechanism must **move in the same direction as the source's result**, not only have correct arithmetic. (Post 02, round 3: the first junk-placement toy showed concentration *raising* value, the opposite of Arora et al.) (Note: “imagine you are explaining it to high school students … use instances or illustrations … as ladders”, 2026-10-16.)

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
- Diagrams follow the theme tokens and are readable at 375 px. A diagram revealed in steps shows later steps faded from the start (`"preview": true`), so the frame is never mostly blank on a phone.
- A paragraph carries **at most about five numbers**. A worked example with more numbers goes in a small table. (Post 02 critic rounds 2–3.)

## 6. Formulas
- Show the formula the reader will meet in the field (e.g. the machine-learning cross-entropy $H(p,q)=-\sum_x p(x)\log q(x)$), even when the source writes it differently, and connect the two. (Note on cross-entropy, 2026-10-15.)
- Derivations that a reader can do in five minutes become **exercises** with a hint and a folded solution, not finished text.
- Every number in a formula example is checked by running code.

## 7. Big claims need “what it means”
- After any headline result (a scaling law, a theorem, a test score), answer three questions in plain words: **what was measured, on what, and what it lets you predict** — then what it does *not* show. (Note on Step 8, 2026-10-15.)

## 8. The English section
- Two layers: (a) 8–10 phrases from the post's own topic (B2–C1), (b) a **B2 → C1 toolkit**: native expressions for discussing evidence (hedging, concession, emphasis), one or two sentence patterns, small error fixes typical for Chinese/Japanese speakers, and a short practice routine. Every example sentence uses an idea from the same post. (Request, 2026-10-16.)
- Rotate the toolkit: each post adds new expressions and repeats 2–3 from earlier posts for spaced review (without naming the earlier post).

## 8a. Length
- Main text ≤ **7,500 words**, measured with `python3 scripts/wordcount.py posts/<slug>/src/content.html`. Fold-outs, Sources, English and contents are not counted. Clarity beats brevity: a definition the reader needs is never cut. (Post 02, 2026-10-17.)

## 8b. Audio
- Every audio file names its source as **“AI4Read from CSS Lab”**: spoken in the first chapter (“Welcome to AI4Read from CSS Lab.”) and written into each MP3's metadata (artist, album artist, publisher, copyright, comment with the post link; album = post title; title and track = chapter). `scripts/tts_post.py` tags automatically through `scripts/tag_audio.py`. (Request, 2026-10-17.)

## 9. Sources and honesty (from the charter, kept here so it is never forgotten)
- Every claim is checked against the cited page by an independent reviewer before publishing; digests are maps, not truth.
- Keep the authors' hedges (may, suggest, appears). Our own examples and reasoning are labelled “ours”.
- When an error is found in a post, fix the digest and the source brief too.
- **Represent a person at full strength, in both directions.** Quote their strongest unhedged statement on the topic next to their hedged scenarios. Sort their lines by firmness and use the matching reporting verb: *asserts* (no hedge), *predicts* (a forecast with no hedge), *imagines / supposes / asks* (hedged), *concedes / proposes* (their own limits and remedies). (Post 02: the first brief kept only Harari's hedged scenarios and left out “anything made of words will be taken over by AI”; later rounds swung the other way. 2026-10-17.)
- **Never cut a quote before the turn.** Do not end a quotation just before a sentence in the same passage that reverses or qualifies it (“Unfortunately, humanity has never been united”). Never join two separate passages with “since” or “but”. (Post 02, S5 rounds 1 and 3.)
- Read the **whole** talk or essay for a person's claim, not only the passage someone else quoted. Check quotes from audio with a strong transcription model, not only a fast one. (Post 02: “we'll need”, not “we need”.)

## 10. Change log
- 0.1 (2026-10-15): charter style guide only.
- 0.3 (2026-10-16): §8 English section with a B2 → C1 toolkit.
- 0.2 (2026-10-16): §2 ladder, §3 term boxes, §4 explanations in text, §5 illustrations for mechanisms, §6 field formulas + exercises, §7 “what it means”. From Kunhao's first review of post 01.
- 0.4 (2026-10-17): §8b audio files carry the source mark “AI4Read from CSS Lab”.
- 0.5 (2026-10-18): §0 standalone posts, the question over the person, the short answer; §2 toys point the same way as the source; §5 diagram preview and the five-number rule; §8a one length counter; §9 balance (four groups of firmness), quote boundaries, whole-source reading. From Kunhao's note on post 02 and the post 02 review rounds.
