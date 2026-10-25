---
name: critic-2
post: 2026-10-residual-stream
stage: S5 round 2 (pedagogy critic, blind to self-review.md)
date: 2026-10-25
read: src/content.html (wordcount.py: 7,498 main words, cap 7,500), index.html at 390 px and 375 px (Playwright; mouse, CDP touch and keyboard on probe-push; every widget and preset opened), audio-script.md; context from topic-card.md (Decisions), kunhao-input.md, outline.md, learner/state.md. critic-1.md and response-1.md read only after my own pass.
---

# Critic round 2: post 03, "What Is a Hidden State?"

**Verdict: the gate is not met, but it is close.** There are 0 critical and 3 major findings (M1 to M3), and 14 minor ones. Criteria 3 (clarity) and 6 (concision) are at 3 at post level; criteria 2, 4 and 5 are at 4. Round 1 is largely resolved: of the 27 round-1 critic findings, 23 are resolved, 2 are partly resolved (M3, m13), 1 is not resolved (m4) and 1 is template chrome (m17); two of the four audio notes are also still open. The post is much better where it was weak (the direction ladder, the rotation example, the open question, the hook, the guess-first options). What still holds it back is one empirical block in section 3, the density of section 4, and a total length that sits exactly on the cap (7,498 of 7,500 words) with the same point repeated several times. Two of the three majors are cuts, so the fixes give room instead of costing it.

Checks run: 0 console errors; no horizontal scroll at 390 px or 375 px (scrollWidth equals the viewport; no widget or table overflows); every widget readout I opened equals the text (probe-push presets: 0° margin −4.000, 45° −2.828, 135° 2.828, "push along" scores 1.41 and 4.24 with u·v 2.828, "push sideways" u·v 0.000; read-split r=(1,2) shares 5, 0, 1, −1 and r=(0,1) shares 2, −1, 1, −2; rotate at 90° gives stream (0, 5), r (−2, 1), shares 5, 0, 1, −1; three-features all-on gives stream (0, 0)). I re-did the margin table (0°, 45°, 90°, 120°, 135°) and the 140° case by hand: all correct, and 135° is the maximum. Fact-checking is not my gate.

## 1. Post-level scores (minimum over sections)

| # | Criterion | Score | Reason |
|---|---|---|---|
| 1 | Factual accuracy and hedges | not my gate; provisional 4 | Hedges and "ours" labels are kept throughout; toy numbers all match. One hedge missing: m13 (Nanda's "the standard basis is always slightly privileged" is in the saved source and not in the post, while the post tells the reader "never read dimension 17 as a feature"). |
| 2 | Ladder for a high-school reader | **4** | Full ladders for the sum ("(1, 2) + (2, −1) = (3, 1)", then the formula, then "x₂ = (4, 2)" check), the read ("1·5 + 2·0 = 5", direct read equals the sum of shares), the probe, steering and rotation. Small gaps: the unit-length claim is asserted, not checked (m6); the identity test is dense (M1). |
| 3 | Clarity and English | **3** | The identity block in section 3 needs rereading ("TransformerLens (raw weights) against the Hugging Face list" is never introduced), section 4 stacks quotes and undefined names ("InceptionV1", "curve detectors, dog heads, cars in superposition"), "norm" has two meanings, and "virtual weights" is undefined in Lens 1. |
| 4 | Insight and connections | **4** | Both lenses state a link type, what they add, what they do not explain, and a 3C tie (Computation); no reference to another post. Lens 2 adds a question Lens 1 cannot ("d dimensions, many messages"). Lens 1 spends a third of its words on a method difference that is not about the lens (m7), and the two lenses are never compared with each other. |
| 5 | Illustrations and interactives | **4** | Every mechanism that is a calculation has a working widget with an edge-case preset and readouts that match the text. Defects: negative bars unreadable in read-split although the component now supports `signed` (m1); probe and push handles coincide in the "push along" preset (m2); bus labels overlap arrows (m3); rotate does not draw the four writers its note mentions (m4). |
| 6 | Concision | **3** | At the cap (7,498). About 15% can go without loss: the empirical block, a method paragraph, quote stacks, and a refrain ("none of the three sources …", "use each model's own dot products") that appears 6 to 9 times. The word count rose from 7,358 to 7,498 in the revision. |

Release gate: criteria 3 and 6 are below 4, so the post does not pass yet. To reach 4 on both, do the three changes in section 7; they cut about 800 words net.

## 2. Section scores (criteria 2 to 6)

| Section | C2 | C3 | C4 | C5 | C6 | Note |
|---|---|---|---|---|---|---|
| hook | 4 | 4 | 4 | n/a | 4 | Good now; "Copy the list at one layer. You can train …; compare …; or add …" mixes a set-up sentence with the three things (m11). |
| guess | n/a | 4 | n/a | n/a | 4 | Options are similar in length; the right answer is never the longest. g3's right option is the shortest and the only unqualified one (m9). |
| sum (§3) | 4 | 3 | 4 | 4 | 3 | Best ladder in the post, then a 650-word empirical block (M1). 1,498 words, 20% over plan. |
| bets (§4) | 4 | 3 | 4 | n/a | 3 | Each bet now starts with an instance. Still 773 words, mostly attribution, with undefined names (M3). |
| rw (§5) | 5 | 4 | 4 | 4 | 4 | Complete ladder with check and edge case. Bars hide negatives (m1); challenge has no answer (m8). |
| dir (§6) | 4 | 4 | 4 | 4 | 4 | The round-1 overload is fixed. Handle overlap (m2); unit-length check (m6). |
| answer | 4 | 4 | 4 | n/a | 4 | Verdicts are labelled ours with what would change them. |
| lens-linalg | 4 | 3 | 4 | n/a | 3 | "virtual weights", "bottleneck" and "our reads sit on Nanda's side" are unexplained (m7). |
| lens-info | 4 | 4 | 5 | 4 | 3 | Strong lens and toy; 647 words against a 380 plan. |
| turn | 4 | 4 | 4 | n/a | 4 | Exercises and open question are now checkable by hand. "What to look for" has 6 numbers and a flag name in small print. |
| work | 4 | 4 | 4 | n/a | 4 | Honest; the assumption is labelled untested. |
| recall | 4 | 4 | n/a | n/a | 4 | Good. |

## 3. First sentence where a high-school reader gets lost

Section 3, "Is the hidden state the stream?": "We ran this in the two notebooks that come with this post: GPT-2 small (12 blocks), the prompt “The cat sat on the mat because”, 32-bit numbers, CPU." The reader meets "32-bit numbers" and "CPU" with no gloss, and then a table row "TransformerLens (raw weights) against the Hugging Face list". Neither tool has been introduced; "raw weights" is not explained. Everything before this sentence climbs smoothly. (Round 1 named the hook; that is fixed.)

## 4. Widgets: can the reader do the mechanism, does the edge case teach, does the prose quote the readout?

| Widget | Verdict |
|---|---|
| `sum-table` (stepper) | Yes. Rows start hidden, so the reader adds by hand first. Last note names the cancellation. Minor: the caption under the table shows the final answer "x₂ = … = (4, 2)" from the first screen, which spoils the check (m14). |
| `bus` (diagram, 6 steps, preview) | Yes. The running total shows in the stream column. At 390 px the edge labels "(1, 2)", "+(3, −2)" and "+(−1, 2)" are crossed by arrow lines (m3). |
| `positions` (diagram) | Yes, static and clear. |
| `read-split` (lab) | The mechanism can be done; the edge case r = (0, 1) is correct. The bars for −1 and −2 render as a hairline, so the cancellation cannot be seen, and the note says "shows as an empty bar" (m1). |
| `probe-push` (vec2d) | Works with mouse, touch and keyboard (arrow keys; sliders stay in sync; 0 errors; touch-action is none on handles, so the page does not scroll during a drag). Drag of the push ring from the origin works. The edge cases teach: 45° blind probe, push sideways (every point moves, no score moves), push along (scores move, margin stays 2.828). Defects: m2 (handle overlap). Hit area: the handle is 46 SVG units, which is 42 CSS px at 390 px; a grab 20 px from the centre works, 24 px misses. Acceptable, borderline against the 44 px guideline. |
| `rotate` (vec2d) | One vector throughout; the readout agrees with the text at 0° and 90°. The note says every vector turns "and the four writers", but only the stream and r are drawn (m4). |
| `three-arrows` (diagram) | Shows the three directions; the arrows to g₂ and g₃ look shorter than the one to g₁, while the label says "Equal lengths" (m5). |
| `three-features` (lab) | Numbers right; the edge case (all on equals none) teaches. The note shows a raw "g_j" instead of a subscript (m5). |

Prose and readouts: every number I compared matches. The edge-case captions are correct.

## 5. Lens sections

- **Lens 1 (same-math).** Link type stated; adds "exactness for the bookkeeping, and three habits"; does-not-explain stated (why concepts would be directions, anything nonlinear, whether a probe's direction is used); 3C tie present; stands alone. "Seeing is not doing" and the cosine counter-example are real additions. The paragraph "The sources differ in method" does not belong to the lens and uses an undefined term (m7).
- **Lens 2 (structural analogy, metaphor).** Link types stated and honest ("No theorem or number transfers"); adds the question of limits and a silence case; says where the analogy breaks (MacKay's users cannot hear the output); 3C tie present. It reads as the strongest lens. Its source paragraph (Elhage, Nanda, Olah, in one block) is long.
- **Across lenses.** Nothing says why these two lenses and not others, or what Lens 2 shows that Lens 1 cannot beyond "the question of limits". A two-sentence contrast would take criterion 4 to 5 (see M2, fix 5).

## 6. Findings

Severity: **Major** = holds a criterion below 4 and needs more than a sentence to fix. **Minor** = fix in a sentence or a config edit.

### Major

**M1. The identity block in section 3 is a results report inside a primer. (C3, C6, WRITING §5 "about five numbers", §1)**
- Location: #sum, from "Is the hidden state the stream?" to "What we did not run": 5 paragraphs, one 4-row table, about 650 words, more than 25 numbers.
- Problems:
  - Undefined names and settings: "TransformerLens (raw weights)", "32-bit numbers, CPU", "tiny random Qwen3 and Gemma 3" (random how, and why), "consecutive Hugging Face entries subtracted".
  - The table does not say which row answers the headline question. Rows 1 and 2 compare the writes with "the stream after k blocks", which is a hooked stream, not "the list the library returns"; only rows 3 and 4 involve the library list. The reader cannot tell what "the stream" in the first column is.
  - The paragraph "The index convention matters" carries about 7 numbers (0 to 11, 0.0, 10⁻⁷, 0.986, 0.0) and three model names.
- Fix (net about −400 words):
  1. Keep in the main text: the procedure (copy the list; add the starting list and the writes; compare), a one-line verdict for GPT-2 small (equal up to rounding, last entry normed), the rounding explanation (it is clear and good), and the sentence "we ran no trained Qwen3, Llama, Gemma or Mistral model; Gemma 3 norms each sub-layer's output before adding it".
  2. Move the 4-row table, the index-convention paragraph and the tiny-model details into a fold-out "Look inside: the numbers behind the check", beside the existing code fold-out (merge the two).
  3. In the fold-out table, rename the first column so each row says what is compared with what, and mark the row that is the identity test (row 3).
  4. Gloss once: "32-bit numbers keep about seven digits".

**M2. Concision: the post is at the cap, and the same points repeat. (C6)**
- Location: whole post; 7,498 of 7,500 words. Plan sizes against actual: sum 1,250 vs 1,498; lens-info 380 vs 647; turn 420 vs 679; dir 900 vs 1,168.
- Repeats: "none of the three sources says/tests X" (hook, bets ×3, trap, answer ×2, dir, lens-linalg, work ×2); "compare by each model's own dot products, not coordinates" (dir ×2, answer, work, recall); "ours / not a result about real models" after almost every toy.
- Fix (about −400 words, in addition to M1):
  1. Lens 1: delete the paragraph "The sources differ in method" (about 90 words), see m7.
  2. Lens 2: cut the Olah "cars and dogs" sentence and shorten the Nanda sentence to its "almost" clause (about −80).
  3. Turn: shorten "What to look for" to two items without the 3155.5 and 417.4 figures (about −60).
  4. Bets: see M3.
  5. State "none of the three sources …" once in the trap box and once in the short answer; delete it from the other places.
  6. Add two sentences that compare the lenses (what Lens 1 cannot say that Lens 2 can, and the reverse), paid for by the cuts. This lifts criterion 4.

**M3. Section 4 is still quote-dense and uses undefined names. (C3, C6)**
- Location: #bets, Bet 1 and Bet 2 paragraphs; 773 words (round-1 target 450).
- Problems: "InceptionV1", "curve detectors, dog heads, cars in superposition" and "attention blocks" are named without explanation; "a linear combination of neurons in a layer" is quoted before "neuron" is defined (it is defined in section 5); the Bet 2 paragraph holds five citations in about 150 words; "cars in superposition" uses a word that Lens 2 defines.
- Fix:
  1. Replace the three circuit names with "three small circuits found by hand in an image-recognition network".
  2. Replace "InceptionV1" by "an image-recognition network" in the main text (keep the name in the trap box and fold-out).
  3. After the Olah quote, add "(a neuron is one small unit of a network, as section 5 will show)", or drop "neurons" from the quote and paraphrase.
  4. Keep, for each bet, one instance, the claim, one hedge and the "what the post does about it" line. Move the other quotes to the existing firmness fold-out. Target about 500 words.

### Minor

**m1. read-split: negative bars are unreadable, and `signed` should be used.** Location: `cfg-read-split`, `bars`. The component now supports `"signed": true` (negative values grow left from the centre line). I tested it on a copy: with `"max":15,"fmt":"d","signed":true` the shares 2, −1, 1, −2 of the r = (0, 1) preset show two bars to the right and two to the left, which is exactly the cancellation the caption describes. Fix: add `"signed":true` to `bars` (keep `max` 15 so the slider extremes, up to ±15, are not clipped; 9 would clip a₂ at r = (3, −3)), and change the note from "A negative share shows as an empty bar; read its number" to "Negative shares grow to the left." No centre line is drawn; that is acceptable.

**m2. probe-push: the two handles coincide in the "push along" preset.** Location: `cfg-vec2d`, `vectors[0].scale = 3` and preset "push along" (φ = 135°, v = (−2, 2)). The probe arrow tip is at 3 units and the push tip at 2.83 units on the same line, 4 px apart on screen. A grab at the centre moves the push (it is drawn last); the probe can only be grabbed on a thin crescent. The reader's natural next step after pressing "push along" is to turn the probe, and cannot. Fix: draw u with `"scale":4` and change `x` to `{"min":-5,"max":8}` so the tip at φ = 180° is inside the view; the tips are then 45 px apart in this preset. Update the caption ("four times longer"). Alternatively, ask for the component to draw the last-dragged handle on top.

**m3. Bus diagram: edge labels are crossed by arrows at 390 px.** Location: `cfg-bus` edges `w0`, `w3`, `w4`. Fix: use `dx`/`dy` on those three edges to move the labels next to the arrow start, or drop the labels (the step text and the stream column already carry the numbers).

**m4. rotate: the writers are not drawn.** Location: `cfg-rotate` note "and the four writers". Only the stream and r are drawn, so the reader cannot see the writers turn with them. Fix: add four faint vectors (`cls` c0) for the writers with the same rotation formulas, or change the note to "the reader r = (1, 2) and the stream (5, 0)". The second is free.

**m5. three-arrows and three-features: small drawing and text slips.** `cfg-three-arrows` caption says "Equal lengths" but the arrows to g₂ and g₃ are drawn shorter than to g₁ (boxes at different distances); move g₂ and g₃ to the same distance from (0, 0) as g₁ (for example x = 131 and y offsets chosen so all three are 102 px away). `cfg-three-features` note shows "g_j" with a raw underscore; write "gⱼ" or "g, j".

**m6. The unit-length claim has no worked check.** Location: #dir, "Why length 1? … (textbook geometry, ours)". The reader is told that the score is the distance to the foot of the perpendicular but sees no number. Add (about 35 words): "Check: u = (0.6, 0.8) and x = (5, 0). Score 3. The foot is 3·u = (1.8, 2.4), and x − foot = (3.2, −2.4) has dot product 1.92 − 1.92 = 0 with u, so the dotted line is perpendicular." (All numbers verified by hand.)

**m7. Lens 1: "The sources differ in method" is off-topic and cryptic.** Uses "virtual weights" and "bottleneck", neither defined; ends "our reads sit on Nanda's side", which says nothing to the reader. Fix: delete the paragraph (and the matching audio paragraph).

**m8. Two challenges have no answer anywhere.** #rw "can you find a reader that cannot hear the embedding (1, 2)?" and #lens-info "find a setting that looks exactly like silence". The reader cannot check. Fix: add a one-line folded hint to each: r = (2, −1) or (−2, 1); strengths (0.5, 0.5, 0.5).

**m9. Guess g3: the right option is the shortest and the only one without a qualifier.** "By the same amount for every point" against three longer, qualified distractors. Fix: lengthen to "By the same amount, whichever point it is" or shorten the others to match.

**m10. Terms used before or twice.** `<dfn>blocks</dfn>` appears twice (in g1 and in #sum; round-1 m13 claimed it removed); "neuron" is used in section 4 before its section 5 gloss (see M3); "cosine similarity" is used in Lens 1 without a definition (a clause, "dot product divided by the two lengths", would do). The round-1 response said "Length is defined as the norm in #sum"; the text does not do that.

**m11. "Norm" has two meanings.** Section 3 defines the norm as a normalisation step; section 10 says "the stream's length (its norm) grows with depth" and "the median … is 5.3 before block 1 and 472.4 after twelve", in the same paragraph block as "the final norm plus the unembedding". A reader will not know which is meant. Fix: in section 10 write "the stream's length" without "(its norm)", and in the notebook sentence "plots the stream's length by depth". Also hook sentence: split "Copy the list at one layer." into its own setup sentence ("Say you copy the list at one layer. People then do three things with it: …").

**m12. Audio: three items from round 1 or new.** (a) "In symbols, R r dot R x equals r dot x" is ambiguous aloud (round-1 audio note not applied); say "the turned r dotted with the turned x equals r dotted with x". (b) In #bets the six points are spoken as "three calm, three, one; four, two; five, three, and three urgent, one, three; …", where "three" is both a count and a coordinate; say "three calm points: the point three-one, the point four-two, the point five-three; and three urgent points: one-three, two-four, three-five". (c) The fold-out "Look inside: what the code says about four model families" is not mentioned in the #sum chapter (the other four fold-outs are); with M1 the merged fold-out should be mentioned. Also "Prediction three" is spoken as one sentence while the page reveal gives the reason; add "Each score moves by u dot v, whatever the point."

**m13. Hedge missing on "no privileged basis".** Location: #dir, "So never read “dimension 17” as a feature" (also the work card and recall). Elhage's claim is for an idealised linear stream; the saved Nanda page says "the standard basis is always slightly privileged. Floating point representations and Adam inherently privilege the standard basis" (line 245 of the saved text). Fix: "…never read 'dimension 17' as a feature on that ground alone (Nanda adds that the standard basis is always slightly privileged, so this is a habit, not a law)" and list this in Lens 1's does-not-explain. For the fact-checker.

**m14. stepper caption gives the answer first.** `cfg-sum-table` caption "x₂ = x₀ + a₁ + f₁ + a₂ + f₂ = (4, 2)" is visible before the first tap, so the "add by hand first" check is spoiled. Fix: move the caption text into the last row's note (it is already there in part) and leave the caption empty.

**m15. Hit area is 42 px, not 46, at phone width.** The handle radius is 23 SVG units and the figure is scaled to 91% at 390 px, so the circle is 42 CSS px; a grab 24 px off-centre misses. Acceptable, and a big gain on round 1 (about 28 px). If the component can scale the handle with the figure, use radius 26.

**m16. Notes chip.** No control is blocked. The chip covers the end of captions and a readout line at some scroll positions only; it is template chrome.

## 7. The three changes that would raise the post most

1. **Slim section 3's identity block (M1, m11).** Keep procedure, verdict, rounding and the "not run" sentence in the main text; move the table, index convention and tiny-model details to one fold-out; name TransformerLens and Hugging Face in one clause each. This lifts C3 and C6 and saves about 400 words.
2. **Make section 4 and Lens 1 plain and short (M3, m7, M2 items 1 to 5).** Image-recognition network instead of InceptionV1 and the circuit names; keep one instance, one claim, one hedge per bet; delete the Lens 1 method paragraph; say "none of the three sources …" twice instead of nine times. This lifts C3 and C6 and saves about 400 more words.
3. **Fix the widgets and the one-line items (m1 to m6, m8 to m11, m14).** Turn on `signed` for read-split; draw u at scale 4; move the three bus labels; align the three arrows; one unit-length check; two folded answers. These are config and sentence edits; with the savings above they fit under the cap.

Expected result: C3 4, C6 4, C4 5 with the lens contrast, C5 4 to 5. Re-run `check.mjs` and `test.mjs` after the widget edits, and re-check quote boundaries in anything moved to a fold-out. Update the audio chapters for M1, M3, m7 and m12 together with the text.

## 8. Round-1 critic findings: resolved or not

| ID | Round-1 finding | Status | Evidence in round 2 |
|---|---|---|---|
| M1 | "Norm" used before it is defined | Resolved | Defined in #sum at first use with the (4, 2) and (8, 4) toy. New homonym with "length (its norm)" in section 10: m11. |
| M2 | §6 score paragraph overloaded | Resolved | Split into cloud, length and unit vector, score, margin, angle form; widget task precedes the table. Residual: m6. |
| M3 | Bets abstract and attribution-heavy | Partly | Each bet now starts with an instance (resolved). Words rose to 773 from 809 target 450; undefined names remain: new M3. |
| M4 | Rotation example mixed two vectors | Resolved | One stream (5, 0) → (0, 5), r → (−2, 1); readout, prose and E5 agree. |
| M5 | Guess Q1 pre-answered; option lengths | Resolved | Hook asks the questions only; bank picture moved after the guess; right options not longest. Residual: m9. |
| M6 | Reorder check skipped a step | Resolved | Rounding and "relative" explained in plain words. |
| M7 | Open question needed matrix product | Resolved | Rows-as-readers rule and three worked images. |
| M8 | Recall card on attention scaling | Resolved | Replaced by a card on the margin; no outside terms in recall. |
| M9 | probe-push: margin sign, steering purpose, v invisible, no scores at feet | Resolved (iv and v accepted) | Sign explained in text, widget caption and recall; v = (−2, 2) used; presets show push along and sideways. The push arrow still starts at length 0, with a note that says so (acceptable); scores are in the readout, not at the feet (acceptable). |
| m1 | Challenges answered on screen | Resolved | Both challenges now ask for something not shown. New: no answers given (m8). |
| m2 | Table before widget | Resolved | Task precedes the table. |
| m3 | Colour collision | Resolved | Dark ink for u, green for v. |
| m4 | Bars hide negatives | **Not resolved** | Round-1 response called it a component limit. The component now has `signed`; read-split does not use it, and the note still says "empty bar": m1. |
| m5 | rotate and three-features had no picture | Resolved | rotate is a vec2d; `three-arrows` added. Residual: m4, m5. |
| m6 | Bus diagram did not show running value | Resolved | Running total in the stream column. Residual label overlap: m3. |
| m7 | Wide table scrolled at 390 px | Resolved | Two columns; no overflow at 390 or 375 px. |
| m8 | Cloud table did not list points | Resolved | Points listed as pairs. |
| m9 | Bet 3 overreach ("can only mean") | Resolved | Now "a fair comparison must not depend on coordinates (ours)". |
| m10 | Hook did not name "hidden state" | Resolved | "Libraries call this list a hidden state" in paragraph 1. |
| m11 | Short answer (a) dense | Resolved | Error figures removed from the verdict. |
| m12 | "13 shares" unexplained | Resolved | Explained as embedding plus 12 writes. |
| m13 | Duplicate dfn, undefined small terms | Partly | Standard deviation, logit lens, log_softmax, RLHF glossed; `blocks` still defined twice; neuron before gloss; cosine similarity undefined: m10. |
| m14 | "Linear" uses without instances | Resolved | Each of the three uses carries an instance. |
| m15 | E3 workload, terse solutions | Resolved | Hint added; solutions show the dot products. |
| m16 | `keypoint` box | Resolved | Gone. |
| m17 | Notes chip covers captions | Not applicable | Template chrome; no control is blocked (m16). |
| m18 | Handle hit area | Resolved (borderline) | 46 SVG units, 42 CSS px at 390 px; see m15. |
| Audio | "R r dot R x" ambiguous | **Not resolved** | Still in #dir: m12 (a). |
| Audio | Error figures spoken in #answer | Resolved | Removed. |
| Audio | #sum and #bets long for looping | Not resolved | Still long; shorten with M1 and M3. |
| Audio | Recall item 8 (attention) | Resolved | Card replaced. |
