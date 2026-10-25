---
name: writing-principles
description: How AI4Read posts are written. Read before drafting or revising any post. Claude updates it whenever a review round or a note from Kunhao shows a missing rule (add the rule, the note or finding that caused it, and the date); Kunhao asked for this on 2026-10-18.
version: 0.9 (2026-10-25)
---

# AI4Read writing principles

The charter (§5–7) fixes the post template, style and audio. This file says *how to explain*. It grows from Kunhao's review notes: every rule cites the note that produced it, so we can see why it exists and change it when it stops helping.

## 0. Every post stands alone
- A reader may open any post first. **Never cite or rely on another post** (“as in post 01”, “remember the village”). Re-introduce every toy world, term and result the post needs, from scratch. Spaced review still happens: recall questions and English expressions may repeat earlier material, without saying so. (Note, 2026-10-18.)
- A person's idea can be the **starting hint**, but the post is about the **question**, not about the person. Keep the account of what someone said short in the main text, and put the full list of their lines in a fold-out. (Note on post 02: “the introduction focused a little too much on what Harari said … it is an idea, a hint for us to explore”, 2026-10-18.)
- **Answer the question where the reader looks.** Give a one-line preview after the hook. Open the synthesis with a boxed **Short answer**, with one paragraph for each part of the question. Define any key term from the question at first use. (Post 02 critic round 1, 2026-10-17.)
- **Pin down the question's threshold words.** Words like *fully*, *without any*, *possible* or *society* decide the answer. Say which sense the post tests (post 02: intervention at run time vs at design time; capable vs stable vs accepted), define the key noun (“society”), and carry the same senses through to the short answer. (Post 02 v2 critic round 1, 2026-10-18.)
- **The short answer gives a verdict.** Do not hand the question back to a source (“the question behind Harari's …”). State our verdict, label it ours, and say what evidence would change it. Give each part of the question an argument, not only a status report; if one part has only one channel (e.g. impact = correlated failure), say who gains and who bears as well. (Post 02 v2 critic round 1.)
- **Recall tests only this post.** A recall or exercise question may use only what this post itself teaches and cites; a question that needs an outside idea (post 03 draft: an attention √d_k card) is a hidden cross-reference. (Post 03 S5 round 1.)
- **One point, one ladder.** If several toys teach the same idea, keep the clearest in the main text and move the others to fold-outs; spend the words on the parts of the question that carry its meaning. (Post 02 v2: four ladders all taught “sameness makes failure joint”.)

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
- **A quoted formula still needs its climb.** If the source gives a result without derivation, derive a small case ourselves (labelled ours, with its assumption stated) or say plainly that we quote it; never let “as given by” replace the ladder. (Post 02 v2: Haldane and May's \(N^N\varepsilon^N/N!\), derived for two banks.)
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
- Guess-first options: the right answer must not be the longest, most hedged or most specific option. Make the distractors serious and similar in length. (Post 02 v2 critic.)
- Every **mechanism** (an architecture, a procedure, an experiment's setup) gets a picture: an inline SVG diagram or a small interactive. Words alone are not enough for “the hidden layer was removed” or “the object is *on* the box instead of *in* it”. (Notes on Step 4, Step 5, prediction 3, 2026-10-15.)
- Interactives must let the reader **change one thing and see the effect** (a slider, a tap on a word). Label invented numbers as “toy numbers”.
- Diagrams follow the theme tokens and are readable at 375 px. A diagram revealed in steps shows later steps faded from the start (`"preview": true`), so the frame is never mostly blank on a phone.
- A paragraph carries **at most about five numbers**. A worked example with more numbers goes in a small table. (Post 02 critic rounds 2–3.)

- **Checks must work on the page.** Any check the reader is invited to do (“add the shares: you get 5”) must come out with the numbers actually shown in the same passage, the widget and the exercise; use one vector throughout. (Post 03 S5 round 1: the rotation passage read x₂ but gave the shares of (5, 0), so the reader's check gave 8.)
- **Define at first use, in the main text.** If a term (*norm*) is used before the fold-out that explains it, give a one-line definition in the text at first use; the fold-out keeps the details. (Post 03 S5 round 1.)

## 6. Formulas
- Show the formula the reader will meet in the field (e.g. the machine-learning cross-entropy $H(p,q)=-\sum_x p(x)\log q(x)$), even when the source writes it differently, and connect the two. (Note on cross-entropy, 2026-10-15.)
- Derivations that a reader can do in five minutes become **exercises** with a hint and a folded solution, not finished text.
- Every number in a formula example is checked by running code.

## 7. Big claims need “what it means”
- After any headline result (a scaling law, a theorem, a test score), answer three questions in plain words: **what was measured, on what, and what it lets you predict** — then what it does *not* show. (Note on Step 8, 2026-10-15.)

- **Measured numbers carry their frame.** For every number from code we ran, say what was run (model, library and version, precision, device), what a *relative* error is relative to, and what was not run. A check that repeats the model's own computation (bit-exact additivity inside one library) is a consistency check, not evidence; say so and lean on the independent comparison. (Post 03 S5: a relative error was described against the stream when the code divided by the block's writes; the notebook's own docstring was wrong.)

## 8. English study packs (separate from the post)
- **The blog contains no English-learning section** and no English audio chapter. Kunhao publishes the posts without it (note, 2026-10-25). Each post's English material is a separate **pack** for Margin, written in `posts/<slug>/english/english.json` and built with `python3 scripts/english_pack.py posts/<slug>` (pack JSON plus a readable `.md`). The loop paragraph is recorded with `scripts/tts_english_loop.py <slug>` and tagged “AI4Read from CSS Lab”.
- **C1 and C2 only.** Every expression, pattern, fix and the loop paragraph carries a level, and the builder refuses anything else. Levels are our estimate in the style of the English Vocabulary Profile; an independent reviewer checks them.
- Contents: about 15–18 expressions from the post's ideas, 4 sentence patterns (cleft, inversion, concession, nominalisation, calibrated reporting verbs), 4 fixes of the kind advanced writers still make (comprise of, stacked hedges, dangling modifiers, imply/infer, respectively), 2 practice tips, and one loop paragraph of about 150 words that uses 8–11 of the expressions.
- Every example sentence uses an idea from the same post and must not misreport a source (the fact-check rules of §9 apply). Keep an item's headword unchanged when it is reused, so its `externalId` and Margin review history survive; you may repeat 2–3 expressions from earlier packs for spaced review.
- The post's own prose stays plain (§1): the C1–C2 level is for the study pack, not for the explanations.

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
- **Purpose is not effect.** “A rule triggered in order to prevent a cascade” states a purpose; never report it as “the rule prevented a cascade”, even attributed. (Post 02 v2 round 1, major.)
- **A quote must be about the thing it supports.** Check the referent of “it” or “this” in the source: a line about a contrived example (the “factoring derivative”) does not support a claim about realistic products. (Post 02 v2 round 1, major.)
- **One source per cited sentence.** A remedy from one talk and a doubt from a book extract three months later get two citations and two sentences, never one. Attribute surveys to whoever ran them (“a Mercer survey reproduced by the IMF”). (Post 02 v2 round 1.)
- **New glosses are new claims.** A parenthetical added to explain a term (“liquidity shocks (banks unable to borrow)”) must be checked against the source page like any quote; in post 02 v2 such glosses caused new errors in rounds 2 and 3.
- **Search before saying “never”.** Before writing that an author never discusses X, search the whole text (Searle mentions computers on pp. 14, 34, 56, 140–141); state the narrower true claim instead.
- **"None of the sources" is a claim about every source.** Search all of them before writing it, and prefer the narrow true statement (“Elhage reports circuits only in attention-only models of at most two layers”). In post 03 this error recurred three times (tests for language models, tests of whether a direction is used, post-training). (Post 03 S5 rounds 1–3.)
- **Commented-out text is not published text.** When a web page is saved as text, HTML comments must be stripped; a quote from inside `<!-- -->` is a quote the author never published. (Post 03 S2, critical.)
- **Keep the source's population and scope.** “Participants in the IMF's outreach” are not “firms” or “the market”; “more frequently” is not “mostly”; a survey of one market is not all markets.

## 10. Change log
- 0.1 (2026-10-15): charter style guide only.
- 0.3 (2026-10-16): §8 English section with a B2 → C1 toolkit.
- 0.2 (2026-10-16): §2 ladder, §3 term boxes, §4 explanations in text, §5 illustrations for mechanisms, §6 field formulas + exercises, §7 “what it means”. From Kunhao's first review of post 01.
- 0.4 (2026-10-17): §8b audio files carry the source mark “AI4Read from CSS Lab”.
- 0.5 (2026-10-18): §0 standalone posts, the question over the person, the short answer; §2 toys point the same way as the source; §5 diagram preview and the five-number rule; §8a one length counter; §9 balance (four groups of firmness), quote boundaries, whole-source reading. From Kunhao's note on post 02 and the post 02 review rounds.
- 0.6 (2026-10-18): §0 threshold words, verdict in the short answer, one point one ladder; §2 quoted formulas still climb; §5 guess options; §9 purpose ≠ effect, quote referent, one source per cited sentence. From the post 02 v2 S5 round 1.
- 0.7 (2026-10-18): §9 new glosses are new claims, search before saying “never”, keep the source's population and scope. From post 02 v2 S5 rounds 2–3.
- 0.8 (2026-10-25): §8 the English material leaves the post and becomes a separate C1–C2 pack for Margin. From Kunhao's note on posts 01 and 02.
- 0.9 (2026-10-25): §0 recall tests only this post; §2 checks must work on the page, define at first use in the main text; §7 measured numbers carry their frame; §9 "none of the sources" needs a search of all, commented-out HTML is not published text. From the post 03 S2–S5 rounds.
