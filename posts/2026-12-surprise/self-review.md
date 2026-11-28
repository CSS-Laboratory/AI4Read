---
name: post04-self-review
description: Writer self-review of the S5-to-S4 revision (round 2) of post 04 ("How much is a surprise worth?") against rubric v1.1, with the places a fact-checker is most likely to object, deviations, and what was not run.
---
# Self-review, S4 revision after S5 round 2 (28 November 2026)

**Length.** Main text **7,044 words** by `python3 scripts/wordcount.py posts/2026-12-surprise/src/content.html` (cap 7,500; round 1 was 6,844). We did **not** reach the ideal of "below 6,844 even with the cardlab step". Step 6 grew from 389 to about 650 words (the instance with the widget, three worked days, the rule with its citations and conditions, E9 and its check); the other sections shrank by about 190 words (hook 350 to 304, lenses 569 to 508, layer 5 795 to 680, recall 286 to 314 after two new cards). Fold-outs hold about 1,805 words (the Nyquist box gained the independence quote). The trims left are small ones in many places and would risk the ladders the critic asked for, so we stopped.

**What changed (the big moves).**
1. **Step 6 is a ladder you can do.** The `cardlab` widget lets the reader join groups, press “Join the two rarest”, and read ticket length and worth for the village day (1.750 = H), the 0.7 day (1.500 against H 1.357) and the equal day (2.000 = H); a bad chain card on the village day gives 2.625. The rule is credited to Huffman with Cover & Thomas and MacKay pages and the conditions of brief unit 24, including the top-down trap (2.53 against 1.97). Then E9 and a check on the three days. Notebook exercise 7 and recall card 8 agree.
2. **Ticket length and worth are two things.** Layer 2's parts list names both; step 2 defines the worth (E2) and says it equals the ticket length only for shares 1/2, 1/4, 1/8, …; the café lines of steps 2, 3, 4 and 6 are rewritten. This cleared the false E2 café line and the submarine “cost” slips.
3. **The majors on sources.** Lens 4 no longer turns MacKay's single-experiment remark into a search rule; “uniquely decipherable” keeps its own gloss, separate from the prefix property; Mills' “cannot very well be defined” is back and the collapse sentence is tied to his unemployment example; the audio recap of the imagination no longer says “only when”.
4. **Lighter hook, fewer lenses.** Layer 1's Nyquist and Hartley paragraph is down by a third and defines nothing new; the old communication-theory lens is folded into step 5; the layer-5 caveat moved to Sources; the 30-million extreme now opens layer 5.
5. **Minors.** Predict-first exercise in step 3 is new (shares reversed, answer 2.625 and 1.750); the forecaster slider has min and step 0.005; `weigh-lab` bars max 1 and “remain on average”; “ergodic” glossed; Gibson file called an article-in-press proof; tags no longer include Bayesian & causal inference; notebook reordered and fixed.

**Checks run.**
- `check.mjs`: 9 of 9 widget configs OK (the `switch` is skipped by the checker and covered by `test.mjs`). `card-lab` values: village day 1.750, bad chain 2.625, 0.7 day 1.500 with H 1.357, equal day 2.000; `village-lab` reversed script 2.625.
- `build-post.mjs --public --owner`: 0 math errors, 0 unmapped cites (121 cites), no missing source entries, no owner-reference error.
- `test.mjs --inline`: PASS (0 console errors, no overflow at 390 px, readouts equal the Node computation, including `card-lab`; the tap-to-join and the “join the two rarest” interactions work).
- Forecaster slider: loaded the real `widgets.js` in headless Chromium; the slider reads 0.125 and the readout 3.00, 1.00, gap 2.00.
- Layer 2 grep: no whole-word hit for bit, entropy, probability, code, model, encode, decode, log, logarithm, surprisal, formula, symbol, equation, information in the café section; no symbol or abbreviation. The new parts-list lines use “ticket’s length” and “order’s worth” only.
- Notebook: rebuilt in the new order, executed top to bottom with nbclient (Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2, seed 20261207), 0 errors; `results.md` regenerated from this run only. Numbers equal the earlier runs except the 1,050 random share vectors of exercise 7 (seed offset +7; gap range now 0.0033 to 0.8361; the page states no range).
- Audio: every quote in `response-2.md` was matched by script against `audio-script.md`.

## Scores (1-5), by section and criterion
Criterion 1 accuracy and hedges; 2 Four Layers and ladder; 3 clarity and English; 4 insight and connections (layer 4); 5 illustrations; 6 concision; 7 CSS imagination. A dash means the criterion does not apply.

| Section | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Note |
|---|---|---|---|---|---|---|---|---|
| hook (layer 1) | 4 | 4 | 4 | - | 4 | 4 | - | One short history paragraph; options of g1 all have a reason. |
| cafe (layer 2) | 5 | 5 | 5 | - | 5 | 4 | - | Grep clean. Ticket length and worth named as two things. |
| village, surprisal | 4 | 5 | 4 | - | 4 | 4 | - | Worth defined in E2; reason for “a log turns a product into a sum”. |
| entropy | 4 | 4 | 4 | - | 4 | 4 | - | New predict-first on reversed shares; E5 no longer gives away the answer. |
| submarine | 4 | 5 | 4 | - | 5 | 4 | - | Café line now true for any order of questions (ours). |
| roles | 4 | 5 | 4 | - | 4 | 4 | - | Shannon mapping now here, not in a lens. |
| nothalves | 4 | 4 | 4 | - | 5 | 3 | - | A real instance, widget, rule with sources, E9, check. Long (about 650 words). |
| answer, lenses | 4 | 4 | 4 | 4 | 4 | 4 | - | Four lenses and a comparison line; (a) split into three paragraphs. |
| fails | 4 | 5 | 4 | 5 | 5 | 4 | - | Seven boundaries; ergodic glossed. |
| imagination (layer 5) | 4 | - | 4 | - | - | 4 | 4 | Three moves as reasoning; comparison inside research question 2. |
| turn, recall | 4 | 4 | 4 | - | 4 | 4 | - | Notebook reordered; recall cards 7 and 8 new. |

**Post score per criterion (the minimum over sections).** 1: 4. 2: 4. 3: 4. 4: 4. 5: 4. 6: 3 (step 6 and the total length; the main text is 200 words over round 1). 7: 4.

## The five places a fact-checker is most likely to object
1. **Step 6, “among scripts in which no string is the start of another”.** Cover's Theorem 5.8.1 (p. 101) says Huffman coding beats “any other code”; the brief (unit 24, condition 3) says the proof compares instantaneous (prefix) codes. We state the narrower, safe condition, and it is also true of every card the widget builds. “Prove” is Cover's own word for the theorem; we say we do not reproduce the proof.
2. **Step 6, non-uniqueness and ties.** “Swapping yes and no on a question gives another [best card]” is Cover p. 97 (“inverting all the bits”), cited as pp. 96–97; “which 0.1 word gets 2 is a tie; any choice costs the same” is ours (Cover p. 96; MacKay p. 99 say ties may be broken any way). The widget's own tickets are 1, 3, 3, 2 for rain, sun, wind, snow; the text does not say which word gets 2.
3. **The worth/ticket identities (ours).** “A ticket’s length can equal the worth only for shares 1/2, 1/4, 1/8, …” and “for any one customer, the worths of her answers add up to the worth of her drink, whatever order the card asks in” are our arithmetic (the chain rule); both are labelled ours. The second is shown on the page only for the grid (E8) and stated for any card.
4. **Layer 5, Move 2 and Move 3.** “cannot very well be defined” within everyday surroundings is a paraphrase of “cannot very well be defined in terms of the immediate and everyday environments of ordinary men”; the quotation marks cover only “cannot very well be defined”. Gibson's sentence is now paraphrased as “language processing effort is associated with how predictable an element is in context”; the source says “Since language processing effort is associated with predictability”, about elements that make nouns more predictable.
5. **Lens 4, “step 6’s rule is [the fastest]”.** MacKay p. 100 and Cover p. 97 give the trap; Cover p. 101 gives the optimality of the join rule. The sentence joins three citations for one claim (“the even split is not always fastest; the join rule is”).

Also worth a second look: the “ergodic” gloss is ours (not from Pierce p. 59, whose page numbering differs between the 1961 and the Dover edition); “His ‘information’ means, in our reading, facts” rests on Mills p. 5 (“this Age of Fact, information often dominates their attention”).

## Deviations from the outline
- **Lenses are four** (statistical mechanics, psycholinguistics, Bayesian probability, search); the communication-theory lens became part of step 5.
- **Boundaries are seven** (boundary 6 split into “fixed script and whole questions” and “no noise”).
- **Layer 5 has three moves in the text**; comparison is named inside research question 2 (Mills p. 215, “comparable cases”).
- **Step 6 uses weather words** in the `cardlab` table (the village), not drinks; the first preset is called “village day”.
- **Notebook exercise numbers changed** (see `review/response-2.md`); the page cites exercises 6 and 7.
- `outline.md` was not updated; it is an S3 document.

## What was not run or not checked
- No audio was recorded (Kunhao reviews first). The audio script is about 8,150 words including headings, about 55 minutes: longer than round 1 (7,560) because step 6 is now spoken as a ladder.
- No language model, no real corpus. The notebook's sample text is a paragraph we wrote.
- Python versions other than 3.12.12 were not tried.
- The Chinese text and audio script were not produced at this stage.
