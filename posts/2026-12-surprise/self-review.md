---
name: post04-self-review
description: Writer self-review of the S5-to-S4 revision (round 1) of post 04 ("How much is a surprise worth?") against rubric v1.1, with the places a fact-checker is most likely to object, deviations from the outline, and what was not run.
---
# Self-review, S4 revision after S5 round 1 (28 November 2026)

**Length.** Main text 6,844 words by `python3 scripts/wordcount.py posts/2026-12-surprise/src/content.html` (cap 7,500; it was 7,459). Fold-outs hold about 1,740 words in 10 boxes: the weighing (about 500 words, with its widget), the twin game and the grouping rule moved there. The critic suggested 6,200–6,800 words; we are 44 words above that range because we added about 300 words that the reviews asked for (the repaired café, the E5 and E8 steps, a guess about a village the reader has not seen, the live-versus-fixed boundary, the roles check, the submarine slider).

**What changed (the three big moves).**
1. **The café has a hatch.** The customer fills in a paper ticket against a card on the wall; the barista in the back room has never seen the customer and holds the same card. Now the shared script is necessary (without it, "no, no, yes" means nothing), the customer encodes and the barista decodes, and no one asks anything live. Step 5 is rebuilt on it; Shannon's twin game is a fold-out; boundary 6 says where the café breaks (a real barista can ask live and adapt; a transmitter cannot hear the receiver).
2. **Gibson's scope.** Nowhere does the post say or imply that reading effort follows surprisal. Gibson's sentence is quoted as a premise, "language processing effort is associated with predictability", with the hedge, with the note that his word is predictability and that the two cited studies are unseen. Hale (2001) and Levy (2008) are no longer named in the text.
3. **Cuts and steps.** The weighing (step 4), the twin game, the binary-digit recipe for the rats, the 64-object paragraph, Move 4 of layer 5 (folded into research question 2) and several source-process asides left the main text. E5 became a laddered fold-out, E8 got its factors named, g2 became a question not answered earlier, and the surprisal plot lost its undefined second curve.

**Checks run.**
- `check.mjs`: 8 of 8 widget configs OK (the `switch` is skipped by the checker and is covered by `test.mjs`).
- `build-post.mjs --public --owner`: 0 math errors, 0 unmapped cites, no missing source entries, no owner-reference error (112 cites).
- `test.mjs --inline`: PASS (0 console errors, no overflow at 390 px, readouts equal the Node computation, interactions work). The weighing widget now sits inside a closed fold-out, and still passes.
- Layer 2 grep: no whole-word hit for bit, entropy, probability, code, model, encode, decode, log, surprisal, formula, symbol, equation, information in the café section (text, diagram labels, check-yourself); no symbol or abbreviation.
- Notebook: rebuilt in the new order, executed top to bottom with nbclient (Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2, seed 20261207), 0 errors; all numbers equal the first run; `results.md` was generated from the new run only.

## Scores (1-5), by section and criterion
Criterion 1 accuracy and hedges; 2 Four Layers and ladder; 3 clarity and English; 4 insight and connections (layer 4); 5 illustrations; 6 concision; 7 CSS imagination. A dash means the criterion does not apply.

| Section | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Note |
|---|---|---|---|---|---|---|---|---|
| hook (layer 1) | 4 | 4 | 4 | - | 4 | 4 | - | Opens with the pain; no term box, no new concept. "Worth" is defined in one clause inside the guess. The history is two sentences. |
| cafe (layer 2) | 5 | 5 | 5 | - | 5 | 4 | - | The hatch makes the script necessary. Grep clean. Parts named in words. Two check-yourself questions; the 2.25 is computed in the answer, without a forward pointer. |
| village, surprisal | 4 | 5 | 4 | - | 4 | 4 | - | Term box moved here. Binary recipe gone. E1 states the power-of-two condition. The plot has one curve and the sure-thing edge case. |
| entropy | 4 | 4 | 4 | - | 5 | 4 | - | E5 is a short fold-out ladder (grouping rule). Bars show share times surprisal, so a share of 0 shows 0 correctly. Widget has a 0.7 preset. |
| submarine | 4 | 5 | 4 | - | 5 | 4 | - | E8's two kinds of factor are named; the slider lets the reader choose when the hit comes. |
| roles | 4 | 5 | 4 | - | 4 | 4 | - | Built on the ticket café: customer encodes, barista decodes. Twin game is a fold-out. |
| nothalves | 4 | 4 | 4 | - | 3 | 4 | - | The bound is quoted, not derived (said so). The 0.7 village is worked in the text, with the join rule labelled ours. Section's mechanism has no widget of its own, but the village widget has the 0.7 preset. |
| answer, lenses | 4 | 5 | 4 | 4 | 4 | 4 | - | Link types limited to same-math, structural analogy; lens 2 has a concrete example and the scope note. |
| fails | 4 | 5 | 4 | 5 | 5 | 4 | - | Six boundaries; boundary 6 adds live asking versus a fixed script. |
| imagination (layer 5) | 4 | - | 4 | - | - | 4 | 4 | Three moves as reasoning, the scale move now has a mechanism (correlated surprise); research question 1 says how a post-level number is made. |
| turn, recall | 4 | 4 | 5 | - | 4 | 4 | - | Notebook reordered; eight recall cards; the Gibson card is scoped. |

**Post score per criterion (the minimum over sections).** 1: 4. 2: 4. 3: 4. 4: 4. 5: 4 (the 3 for step 6 is a short quoted result; the village widget with the 0.7 preset covers its numbers). 6: 4. 7: 4.

## The five places a fact-checker is most likely to object
1. **Step 6: "repeatedly join the two rarest outcomes" is ours, not from the sources.** It is the Huffman rule; the notebook runs it and the bound holds on 1,050 random share vectors, but no brief unit states it. The page labels it "ours and not from our sources" (see `requests.md` item 5).
2. **Lens 2 and the Gibson sentence.** The post says the sentence is a premise in an argument about grammatical gender (p. 11), that the two cited studies are unseen, and that his word is predictability. A reviewer may still read our "Surprisal is built from a share" in the link line as asserting a tie between predictability and surprisal; the page says the sentence does not claim it.
3. **The café's "stops at the first yes" and "fixed in advance".** The card is a decision tree written down before the day, so each next question depends on the earlier answers. Boundary 6 says so, and says a real barista can adapt live; a reviewer may ask whether "a transmitter that sends a ticket cannot hear the receiver" is a claim about Shannon's diagram (it is our gloss, marked ours).
4. **Layer 5, Move 1.** The test for an issue is ours, labelled so; the Mills quotes are cut at the sentence ends, with "The very structure of opportunities has collapsed" added on p. 9. The link from Pierce p. 267 (art) to model-priced surprisal is labelled our metaphor.
5. **Editions and bibliography.** Cover and Thomas pages are the 1991 first edition; Pierce pages the 1961 first edition (provenance decision still open, `requests.md`); Gibson pages are those of a corrected proof, and the volume and page range were dropped because our copy says "Vol. xx"; Mills pages are the 2000 Oxford printing.

Also worth a second look: "a share of 0.3 would cost 1.74" and "powers of one half cost whole numbers" are our arithmetic; the 12 : 12 : 0 split is our count; the weighing check "never balance" cites MacKay p. 68.

## Deviations from the outline
- **Step numbering.** The weighing is no longer a step, so layer 3 has six steps (equal chances, surprisal, entropy, submarine, roles, not halves); audio chapters: hook, cafe, village, surprisal, entropy, submarine, roles, nothalves, answer, lenses, fails, imagination, turn, recall.
- **Layer 5 has three moves in the text** (trouble and issue; extremes and scale; another discipline's eyes). Move 4, comparison, is named in research question 2.
- **The guess g2 sits in step 6**, about a village the reader has not seen (0.7, 0.1, 0.1, 0.1); the other two guesses are as before. g1 says "(answered in step 4)".
- **The step 2 plot lost its second curve**; the two-outcome curve is not shown anywhere in the post.
- **The stepper table of the submarine became a slider** (`lab`), the same numbers as rows.
- Outline.md was not updated for the new step numbering; it is an S3 document.

## What was not run or not checked
- No audio was recorded (Kunhao reviews first). The audio script is about 7,500 words including headings (the first draft was about 8,400), roughly 45 minutes: shorter than before, longer than the critic's 35–40.
- No language model, no real corpus. The notebook's sample text is a paragraph we wrote.
- Python versions other than 3.12.12 were not tried.
- The Chinese text and audio script were not produced at this stage.
