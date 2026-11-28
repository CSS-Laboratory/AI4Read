---
name: post04-self-review
description: Writer self-review of the S4 draft of post 04 ("How much is a surprise worth?") against rubric v1.1, with the places a fact-checker is most likely to object, deviations from the outline, and what was not run.
---
# Self-review, S4 draft (2026-11-28)

**Length.** Main text 7,459 words by `python3 scripts/wordcount.py posts/2026-12-surprise/src/content.html` (cap 7,500). Fold-outs hold about 1,030 words in 7 boxes. The first full draft was about 10,000 words; the cuts are listed under "Deviations from the outline".

**Checks run.**
- `check.mjs`: 8 of 8 widget configs OK (the `switch` is skipped by the checker).
- `build-post.mjs --public --owner`: 0 math errors, 0 unmapped cites, no missing source entries, no owner-reference error (118 cites).
- `test.mjs --inline`: PASS (0 console errors, no overflow at 390 px, readouts reproducible, interactions work). The `switch` with two nested `diagram` widgets was also opened by hand in Chromium at 390 px: both panels draw, the second panel shows after the tap, and the page is 390 px wide. The fallback of two stacked diagrams was not needed.
- Layer 2 grep: no hit for bit, entropy, probability, code, model, encode, decode, log, surprisal, formula, symbol, equation, in the text or in the diagram labels; no symbol, abbreviation or digit-with-operator formula.
- A quote script compared all 139 quoted strings with `sources/*.txt` after normalising quotation marks, dashes and hyphenation. 119 match, and the flagged ones are our own labels, read-aloud lines and the answer options, plus eight source quotes that the script cannot match for layout reasons (two-column Gibson pages, OCR in Pierce, a quotation mark nested inside Mills' quote); those were verified by the S2 and S2b fact-checkers on the page images and are quoted exactly as the brief prints them. No quotation is longer than 25 words.
- Notebook: executed top to bottom with nbclient (Python 3.12.12, numpy 2.5.5, matplotlib 3.11.2, seed 20261207); 18 code cells (8 of them empty "your attempt" stubs), 0 errors; every number is in `notebook/results.md` with its cell and frame.

## Scores (1-5), by section and criterion
Criterion 1 accuracy and hedges; 2 Four Layers and ladder; 3 clarity and English; 4 insight and connections (layer 4); 5 illustrations; 6 concision; 7 CSS imagination. A dash means the criterion does not apply to that section.

| Section | 1 | 2 | 3 | 4 | 5 | 6 | 7 | Note |
|---|---|---|---|---|---|---|---|---|
| hook (layer 1) | 4 | 5 | 4 | - | 4 | 4 | - | No logarithm, bit, entropy or probability; "model" appears once and is defined in the same sentence. Old practice from Pierce only; Nyquist, Hartley and Morse are "as Pierce reports". G1 has no figure; the submarine figure is in step 5. |
| cafe (layer 2) | 5 | 5 | 5 | - | 5 | 4 | - | Grep clean. Ten numbered parts; the two-script switch widget; two check-yourself questions. |
| village, surprisal, entropy | 4 | 5 | 4 | - | 5 | 4 | - | Each concept has instance, question, words, numbers, formula, check, limits. Every equation (E1 to E5, E9) has an "In the café" line. Dense where citations sit inside sentences. |
| weighing, submarine | 4 | 5 | 4 | - | 5 | 4 | - | Ex. 4.9 answer labelled ours (MacKay prints none). Table rounds where MacKay truncates and says so. |
| roles | 4 | 4 | 4 | - | 4 | 4 | - | The 1951 roles use the corrected reading; the toy predictor is ours. The Figure 2 detail was cut for length, so the diagram widget carries only the café roles. |
| nothalves | 4 | 4 | 4 | - | 3 | 5 | - | The bound is quoted from Cover and Thomas, not derived: our small case is in a fold-out. No widget for the bound (the notebook has it). Caps criterion 2 at 4 for this concept. |
| answer, lenses | 4 | 5 | 4 | 4 | 4 | 4 | - | Five lenses with link type, adds, does-not-explain, and a "how they differ" line. Lens 3 stays thin because Weaver is unseen. Lens detail partly moved to a fold-out. |
| fails | 4 | 5 | 4 | 5 | 5 | 4 | - | Six boundaries, each tied to a layer-3 assumption, each with "the café breaks"; W7 widget; the estimation table is from the notebook. |
| imagination (layer 5) | 4 | - | 4 | - | - | 4 | 4 | Four moves as reasoning on whose model prices a surprise; two open questions with data and method, labelled ours. Only 4: every claim about society is our conjecture or hypothetical (Mills' numbers are his own illustration), and the sourced anchor is one sentence of Pierce. |
| turn, recall | 4 | 4 | 5 | - | 4 | 4 | - | Transfer challenge with hint and folded solution; eight recall cards using only this post. |

**Post score per criterion (the minimum over sections).** 1: 4. 2: 4 (the bound in step 7). 3: 4. 4: 4. 5: 4 (the bound has no widget; the 3 above is for that one section, whose mechanism is a short quoted result). 6: 4. 7: 4.

## The five places a fact-checker is most likely to object
1. **Layer 5, Move 1: our test for "issue" and the reading of Mills.** The "test" (if changing the ranking changes what many readers miss at once, it is an issue) is ours and is labelled "Our case (ours)", but it follows Mills' phrases "unlike even widespread trouble" and "a crisis in institutional arrangements" (pp. 8-9, quoted across a page break). A reviewer may say we put our test next to his quotes too closely. The paraphrase "a quality of mind that shows how a life and its time fit together" stands for his "interplay of man and society, of biography and history" (p. 4) and may be judged loose. Mills' unemployment numbers are labelled hypothetical, and no rate is stated (brief unit 18).
2. **Lens 2 (Gibson et al. 2019).** The sentence "Since language processing effort is associated with predictability [104,105]" (p. 11) is quoted with its hedge, and the references are named Hale (2001) and Levy (2008) from the reference list on p. 18 (titles only, unseen). Gibson's abstract sentence ("show how a pervasive pressure ...") sits in a fold-out next to the p. 14-15 limits. Pre-proof pages, not the published pagination (stated in Sources).
3. **Step 4, the 6 against 6 answer (MacKay Exercise 4.9).** "0 bits about which ball, 1 bit about ball and direction" is ours; MacKay prints no solution. It was checked by hand and by the notebook (0.000 and 1.000), but the claim "after left heavier every ball is still possible" is a reading of the problem, not a source statement. Also the page for "3^2 = 9, 3^3 = 27" is p. 68 (checked against the page footers of the text copy).
4. **Step 6, Shannon 1951.** The roles follow the S2-corrected unit 14 (the guesser has not seen the passage; Fig. 2: original text plus predictor is the encoding side). The Figure 2 sentence was cut for length, so the roles claim rests on "the reduced text can be considered to be an encoded form of the original" (p. 55) and on the p. 54 quote. The toy predictor (ranked list, "2 1 3") is ours. The 69 and 77 per cent figures are not used.
5. **Editions and bibliography.** Cover and Thomas pages are from the 1991 first edition; Pierce pages are from the 1961 first edition (a library scan; the provenance decision from S2 is still open, see `requests.md`); Gibson pages are pre-proof; Mills pages are the 2000 Oxford printing; the Sources entries for Gibson (vol. 23, pp. 389-407) and Shannon 1951 (vol. 30, pp. 50-64) carry volume and page data that are not in the brief. Also a likely query: "Hartley, in 1928" and the sender's-side wording are paraphrases of Pierce pp. 39-40 and Shannon p. 1, since Hartley's own paper is unseen.

Also worth a second look: the claim "Shannon's 1948 paper uses neither word for one outcome (our search of the whole text)" rests on the S2 search; and "a share of 0.3 would cost 1.74" is our log, not a source figure.

## Deviations from the outline
- **Length cuts to reach 7,459 words.** Pierce's "ten versus a million" sentence (unit 22) was dropped from layer 1; the "four times" trap box moved into the Nyquist fold-out; the Wenglish, Nyquist, 0.7-village, Shannon-properties, names, Mills-on-counting and lens-limits material sits in fold-outs; two check-yourself blocks (surprisal of snow, "why is EQ exactly H") were cut as duplicates of the text just above them; the estimation table is kept but the notebook's sample-text number was dropped from the page.
- **Layer 3 is seven sections, not one**, so that each step is its own audio chapter and can be looped. Section ids: village (with step 1), surprisal, entropy, weighing, submarine, roles, nothalves. Layer 4 is three sections: answer (with 4a), lenses (4b), fails (4c). The audio script has 15 chapters with the same ids.
- **E9 (script average) moved into step 3** so that the widget's "script" line and the 2.25 are defined where the reader meets them. E6 stays in step 7.
- **W3 (the surprisal curve) sits in step 2**, after the check that uses MacKay's table.
- **Collaboration tie** uses no named index ("Shannon diversity index" is not in the brief): the same sum applies to shares of topics or ties, labelled a connection.
- **Mills.** All four moves are used, with Mills' own terms and pages from units 16-21; the "balance" lines (ch. 3, p. 73) are in a fold-out with the p. 215 order-of-work sentence.
- **No `english/english.json`**, as instructed; the audio script has no English-pack material.

## What was not run or not checked
- No audio was recorded (Kunhao reviews first).
- No language model, no real corpus. The notebook's sample text is a paragraph we wrote.
- The estimation table is from one seeded run of 2,000 repeats per n; the standard errors are in `results.md` (0.0071, 0.0037, 0.0019, 0.0006).
- The Chinese text and audio script were not produced at this stage.
