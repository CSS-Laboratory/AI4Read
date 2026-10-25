---
name: critic-3
post: 2026-10-residual-stream
stage: S5 round 3 (final round; pedagogy critic, blind to self-review.md)
date: 2026-10-25
read: src/content.html (wordcount.py: 7,142 main words, cap 7,500), index.html at 390 px and 375 px (Playwright: mouse drag, CDP touch drag and keyboard on probe-push; every preset and slider of all eight widgets), audio-script.md; context from topic-card.md (Decisions), kunhao-input.md, learner/state.md. critic-2.md and response-2.md read only after my own pass. self-review.md not read.
---

# Critic round 3: post 03, "What Is a Hidden State?"

**Verdict: 0 critical, 0 major, 14 minor. Criteria 2 to 6 are all at 4 or above, so the pedagogy gate is met.** Criterion 1 belongs to the fact-checkers. All 3 round-2 majors and 15 of the 16 round-2 minors are resolved. The other round-2 minor is host chrome (m16, the Notes chip). Two minors (handle hit area, and the length of the audio chapters) are carried over. Two things I would fix before release, because each takes one sentence: the dot-product reason in the rotation passage (m1) and the 375 px horizontal scroll (m6). Neither lowers a score.

Checks run: 0 console errors at 390 px and 375 px. At 390 px `scrollWidth` is 390. **At 375 px it is 387** (m6). Every readout I opened equals the text:
- probe-push, drag to 135°: calm −1.41 ×3, urgent +1.41 ×3, margin 2.828.
- probe-push, then dragging the push ring to (−2, 2): calm 1.41, urgent 4.24, u·v 2.828, margin 2.828.
- Presets: axis only −4.000; blind probe scores 2.83, 4.24, 5.66 with margin −2.828; "push along" as above; "push sideways" gives u·v 0.000 and margin 2.828. Dragging the probe to 90° gives margin 0.000, and the arrow key moves φ to 91°.
- CDP touch drag of the probe works at 375 px.
- read-split: r = (1, 2) gives shares 5, 0, 1, −1 and total 5. r = (0, 1) gives 0 (shares 2, −1, 1, −2). The "along a₂" preset gives 15 = 15. r = (2, −1) gives embedding share 0, the folded answer. Negative bars now grow to the left.
- rotate: 90° gives stream (0, 5), r (−2, 1), shares 5, 0, 1, −1, and the shares stay put at 0°, 45° and 180°.
- three-features: "all three" gives stream (0, 0), reads 0, 0, 0; "feature 1 only" gives reads 1, −0.5, −0.5.
- stepper rows start hidden and the last note carries the sum (4, 2).

I re-did by hand the margin table, the logit-lens table, the norm table, E1 to E5, the open-question matrix and the (0.6, 0.8) perpendicular check. All are correct.

## 1. Post-level scores (minimum over sections)

| # | Criterion | Score | Reason |
|---|---|---|---|
| 1 | Factual accuracy and hedges | not scored here | Fact-checkers' gate. Hedges and "ours" labels are visible throughout; the toy numbers all match. |
| 2 | Ladder for a high-school reader | **4** | Full ladders: sum ("(1, 2) + (2, −1) = (3, 1)", the rule read aloud, the x₂ check), read ("1·5 + 2·0 = 5", then the four shares add to 5), direction (three tries by hand, "u = (0.6, 0.8) … 1.92 − 1.92 = 0"), steering ("s(x+v) = s(x) + u·v" with 2.828 and the margin check) and the superposition toy ("0 − ½(1 + 0) = −0.5"). Small gaps: m1 (rotation reason), m3 (attention), m10 (identity test). |
| 3 | Clarity and English | **4** | Short, one-idea sentences in the ladders, and terms are defined at first use. Two dense paragraphs need a reread: the norm paragraph in section 3 (m2) and the privileged-basis paragraph in section 6 (m5). |
| 4 | Insight and connections | **5** | Both lenses state a link type, what they add, what they do not explain and a 3C tie. Lens 1 is "same-math … Only this bookkeeping is the same mathematics". Lens 2 is "structural analogy … metaphor … No theorem or number transfers" and states where the analogy breaks. "Across the two lenses" now says what each cannot do. No reference to another post. |
| 5 | Illustrations and interactives | **4** | All calculation mechanisms have a working widget with an edge-case preset (blind probe, push sideways, r = (0, 1), all three on). The norm and the logit lens are fold-out tables only, which is allowed for minor mechanisms. Cosmetic defects: m7 (bus arrow), m14. |
| 6 | Concision | **4** | 7,142 words, 358 under the cap; round-2 repeats mostly gone. About 10% still repeats (m8). |

Gate: no criterion below 4, 0 major, 0 critical. This is the pedagogy side only.

## 2. Section scores (criteria 2 to 6)

| Section | C2 | C3 | C4 | C5 | C6 | Note |
|---|---|---|---|---|---|---|
| hook | 4 | 4 | 4 | n/a | 4 | Clear. No pointer to the short answer (m11). |
| guess | n/a | 4 | n/a | n/a | 4 | Options are similar in length. The right answer is never the longest. |
| sum (§3) | 4 | 4 | 4 | 4 | 4 | Best ladder in the post. The empirical block is now three paragraphs plus a fold-out. m2, m3, m10, m15. |
| bets (§4) | 4 | 4 | 4 | n/a | 4 | Each bet starts with an instance. InceptionV1 is glossed once, and "neuron" is glossed in place. Still attribution-heavy (734 words), but each quote carries a hedge. |
| rw (§5) | 5 | 4 | 4 | 4 | 4 | Complete ladder with a check and an edge case. |
| dir (§6) | 4 | 4 | 4 | 4 | 4 | m1, m5, m13. |
| answer | 4 | 4 | 4 | n/a | 4 | Verdicts are labelled ours. It leaves out the read/write result (m4). |
| lens-linalg | 4 | 4 | 5 | n/a | 4 | "Seeing is not doing" and the cosine counter-example are real additions. |
| lens-info | 5 | 4 | 5 | 4 | 4 | Derivation, check, folded answer and the analogy-breaks paragraph. 626 words, but it earns them. |
| turn | 4 | 4 | 4 | n/a | 4 | Exercises are checkable by hand. The open question gives the rule first. |
| work | 4 | 4 | 4 | n/a | 4 | The assumption is labelled untested. |
| recall | 4 | 4 | n/a | n/a | 4 | |

## 3. First sentence where a high-school reader gets lost

Section 3, the "sum is bookkeeping" paragraph: "Before that last step the list always has the same overall size: (4, 2) becomes (1, −1), and so does (8, 4)." The reader has just met a four-step recipe in words ("subtracts the average … divides by … the standard deviation … then applies a learned scale and shift"). They get an end result for two vectors with none of the intermediate numbers. They cannot check it without computing a standard deviation, and the table that does so sits in a fold-out in section 6. "Overall size" is also loose: (1, −1) does not have size 1. Everything before this sentence climbs smoothly. (Round 2 named the identity block; that is fixed.)

## 4. Widgets: can the reader do the mechanism, does the edge case teach, does the prose quote the readout?

| Widget | Verdict |
|---|---|
| `sum-table` (stepper) | Yes. The "stream" cells are hidden until Next, so the reader adds by hand first. No caption spoils the answer. |
| `bus` (diagram, 6 steps, preview) | Yes. Running totals show in the stream column and the labels no longer cross arrows. Caveat in m7: the "looks" arrow leaves next to the (2, 2) chip while step 6 says it reads (4, 2). The faded later totals are visible from step 1 (acceptable, since the stepper is the add-by-hand task). |
| `positions` | Yes. Static, clear. |
| `read-split` (lab) | Yes. Signed bars now show the cancellation at r = (0, 1). The caption's "2, −1, 1, −2 … total 0" matches. The folded answer r = (2, −1) is confirmed (embedding share 0). |
| `probe-push` (vec2d) | Works with mouse, CDP touch (at 375 px) and arrow keys, with sliders in sync. Dragging the push ring from the origin works. The edge cases teach: blind probe (margin −2.828, all scores shared), push sideways (every point moves, no score moves), push along (scores move, margin stays 2.828). In "push along" the two arrow tips are about 46 px apart, so both are grabbable. The handle is 42 CSS px at 390 px (borderline, host CSS; carried). |
| `rotate` (vec2d) | Yes. Readout, prose and E5 agree. The note says the writers are "not drawn", which is honest. The "stream" label overlaps the axis tick labels at 180° (m14). |
| `three-arrows` | Three equal arrows, 120° apart, as the caption says. |
| `three-features` | Numbers right. The edge case (all three on equals silence) teaches, and the folded answer (0.5, 0.5, 0.5) is reachable with the 0.5 slider step. |

Prose and readouts: every number I compared matches. Edge-case captions are correct.

## 5. Lens sections

- **Lens 1 (same-math).** Link type stated. "Adds: exactness for the bookkeeping, and three habits". "Does not explain: why concepts would be directions at all (bet 1), anything nonlinear …, whether a probe's direction is used". The 3C tie is present, and it stands alone. The limit is honestly narrowed ("no privileged basis is a habit, not a law (ours)").
- **Lens 2 (structural analogy, metaphor).** Link types stated. It says what it adds (the question of limits and a silence case), where the analogy breaks (MacKay's users cannot hear the output) and what is not claimed ("we do not claim that it is a multiple-access channel").
- **Across the lenses.** One short paragraph; it answers round-2 M2 item 6.

## 6. Findings (all minor; none blocks the gate)

**m1. The rotation reason uses a fact the post never states. (C2, §6 "Turn everything")**
- Text: "Every coordinate changed, but lengths and angles did not, so no dot product changed."
- Problem: the dot product has so far been "first times first plus second times second". "Depends only on the two lengths and the angle between them" is not stated anywhere. The 90° instance and the widget do show the equality, so the reader is not misled, only left with an unexplained "so". I considered this a major candidate. I kept it minor because the instance is fully computed and the widget shows the shares staying put at every angle.
- Fix (about 20 words): after the formula, add "Check for 90°: (−r₂)(−x₂) + r₁x₁ = r₁x₁ + r₂x₂." Or state once, "a dot product equals the two lengths times the cosine of the angle between them". Recommended before release.

**m2. The norm paragraph gives results without steps, and has two forward pointers. (C3, §3)**
- Text: "(4, 2) becomes (1, −1), and so does (8, 4). GPT-2 uses this version …; the code-reading fold-out at the end of this section shows a variant. A fold-out in section 6 gives the details."
- Fix: write "(4, 2): mean 3, centred (1, −1), standard deviation 1, so (1, −1); (8, 4): mean 6, centred (2, −2), standard deviation 2, so (1, −1)" (about 20 words). Say "same size" as "the same list". Merge the two pointers into one: "Two fold-outs give the table and a code reading."

**m3. "Attention" is marked as a definition but never defined at that point. (C2, §3)**
- Text: `<dfn>attention</dfn> part, then an <dfn>MLP</dfn> part`. MLP gets "a small network"; attention gets nothing. Its job (the only part that moves information between positions) appears three paragraphs later. The hook also says "at one layer" before "block" is introduced.
- Fix: add "attention (the part that lets one word's stream look at the streams of earlier words; see 'One stream per position')". In the hook, say "at one depth".

**m4. The short answer does not answer the hook's second question. (WRITING §0)**
- Hook questions: what is the list? what can a part read and write? what does a push do to a probe score?
- Short answer (a)(b)(c): the list; probe and steering and comparing; firmness. The result of section 5 (a read splits into one share per writer, a writer at right angles goes unheard, writes add and can cancel) is not in it.
- Fix: one sentence in (b): "A part reads by dot products, which split into one share per writer (a writer at right angles to the reader goes unheard), and writes by adding, so writes can cancel."

**m5. The privileged-basis paragraph is the densest in the post. (C3, §6)**
- Text: it is about 190 words and about 576 px tall at 390 px, with five citations. "A privileged basis is a meaningful basis" is circular for a high-school reader. "ReLU", "activations" (in the probe definition) and "Adam" are glossed only in passing or not at all.
- Fix: split into two paragraphs. Add a plain definition: "A basis is privileged if the individual coordinates, such as 'dimension 17', mean something on their own." Leave "ReLU" and "Adam" in the parenthesis only, and write "a layer's output" for "a layer's activations" outside the quote.

**m6. Horizontal scroll at 375 px. (render, charter §6)**
- At 375 px `scrollWidth` is 387. The cause is a no-wrap citation chip in §3 paragraph 1: "Nanda 2022, § Transformer Components, Positional information" (right edge at 383 px). The 390 px test passes, but the charter says every figure must be readable at 375 px.
- Fix: shorten the cite text to "Nanda 2022, § Positional information" (and check `cite-map.tsv`), or allow wrapping on `.cite`.

**m7. Bus diagram: the "looks" arrow starts at the wrong chip. (C5)**
- The dashed arrow leaves the stream column beside the (2, 2) chip, while step 6 says the unembedding reads (4, 2).
- Fix: move the Unembed node to y = 294, level with the (4, 2) chip, or start the edge at the bottom of the column.

**m8. About 10% still repeats. (C6)**
- Repeats:
  - "A probe score shows information is present, not that the model uses it": §6, Lens 1, §11 (and the short answer implies it).
  - "Compare through each model's own dot products": §6, short answer, §11, recall.
  - "Nothing here shows / says …": §6 twice, Lens 2, §11.
- Fix: keep the §6 and short-answer statements; replace the §11 cards' sentences with a pointer ("see section 8"). This saves about 100 words and is not required.

**m9. Audio: two chapters are long for looping.**
- `dir` is 1,209 words (about 8 min) and `sum` is 1,145. All chapter IDs match the page (hook, guess, sum, bets, rw, dir, answer, lens-linalg, lens-info, turn, work, recall), and every chapter ends with a recap.
- Fix: if the player supports sub-chapters, split `dir` at "Steering is a translation" and `sum` at "Is the hidden state the stream?". Otherwise accept.

**m10. The identity test is described one way and run another. (C2, §3)**
- The text says "record every write … and add them to the starting list. If the sum equals the copied list …", then reports differences of neighbouring entries against each block's two writes.
- These are equivalent (the differences add up to the total), but the step is not said.
- Fix: add "(the differences add up, block by block, to the whole sum)".

**m11. No pointer from the hook to the short answer. (WRITING §0)**
- The one-line preview is held back because of the guess-first design, which is defensible.
- Fix: end the hook with "The short answer is in section 7; guess first."

**m12. The audio "Prediction" lines are fine; no change.** (Recorded because round 2 raised them: "turned r dotted with the turned x" and "three calm points …" are now clear.)

**m13. "Direction" is used with two meanings. (C2, §4 to §6)**
- §4 says "the concept would be a direction, the arrow (−1, 1)". §6 says "a direction here is an arrow … with length 1 (our convention)", and (−1, 1) has length √2.
- Fix: in §4 add "(length √2; section 6 shrinks it to length 1)".

**m14. Cosmetic widget points. (C5)**
- The "stream" label overlaps axis tick labels in `rotate` at 180°. Move the label above the arrow.
- The probe-push handle is 42 CSS px at 390 px (carried from round 2, host CSS).

**m15. Two hypothetical numbers sit near the toy. (C2, nit)**
- "Block 3 writes (−2, −2) into (2, 2)" (guess 2) uses a third block and a stream value that equal the toy's x₁ but are not in it.
- Fix: add "(a separate toy)" in the question, or accept.

## 7. The three changes that would raise the post most

1. **Close the two one-sentence gaps (m1, m4).** Add the 90° check (or the cosine statement) under "(Rr)·(Rx) = r·x", and put the read/write result into short answer (b).
2. **Make the norm paragraph checkable and the basis paragraph plain (m2, m5).** Show the mean and standard deviation for the two toy vectors, merge the two fold-out pointers, split the basis paragraph and define "privileged" in one plain line.
3. **Fix the 375 px overflow and the bus arrow (m6, m7), and define attention in place (m3).** These are a cite string, a node position and one clause.

Expected result: C2 stays at 4 or goes to 5, and C3 goes to 5 in the two weakest sections. None of these is needed to pass.

## 8. Round-2 critic findings: resolved or not

| ID | Round-2 finding | Status | Evidence in round 3 |
|---|---|---|---|
| M1 | Identity block is a results report inside a primer | Resolved | Three paragraphs (about 245 words) in §3: procedure, one number (6.2e−6, with the rounding explanation), and what was not run. Table, index convention and tiny models are in the `box-numbers` fold-out. Float32, Hugging Face and TransformerLens are glossed. New small point: m10. |
| M2 | At the cap; same points repeat | Resolved | 7,142 words. Lens 1 method paragraph and Lens 2 cars-and-dogs sentence are gone. "Across the two lenses" added. Residual repeats are m8 (about 10%). |
| M3 | Section 4 quote-dense, undefined names | Resolved | 734 words. InceptionV1 appears once, in the trap box, glossed. Circuit names are gone. "Neuron" is glossed in place. One instance, claim and hedge per bet; other quotes are in the fold-out. |
| m1 | read-split negative bars unreadable | Resolved | `signed` is on; at r = (0, 1) and r = (2, −1) negative bars grow left. The note is rewritten. |
| m2 | probe-push handles coincide in "push along" | Resolved | Probe arrow drawn five times longer. Tips about 46 px apart; both grabbable. |
| m3 | Bus labels crossed by arrows | Resolved | Vectors sit inside the writer boxes; edge labels are gone. Screenshot clean. Residual: m7. |
| m4 | rotate note mentions writers that are not drawn | Resolved | Note now says "they are not drawn, but the shares below are computed from them". |
| m5 | three-arrows lengths and "g_j" | Resolved | Three equal arrows; the note uses "Feature j". |
| m6 | Unit-length claim had no check | Resolved | The (0.6, 0.8) check is in §6 and verified by hand. |
| m7 | Lens 1 method paragraph | Resolved | Deleted in page and audio. |
| m8 | Two challenges had no answer | Resolved | Folded "Answer" under each; both verified. |
| m9 | Guess 3 right option shortest | Resolved | "By the same amount, whichever point it is". Options are similar in length. |
| m10 | Terms used before or twice | Resolved | `blocks` is a `<dfn>` once. "Neuron" and "cosine similarity" are glossed. Residual: attention (m3), activations (m5). |
| m11 | "Norm" has two meanings; hook sentence | Resolved | "(its norm)" is gone from §10 and the audio; "length" is used. The hook sentence is split. |
| m12 | Audio: R r dot R x; six points; fold-out mention; Prediction 3 | Resolved | Page and audio agree (checked lines for each). |
| m13 | Hedge missing on "no privileged basis" | Resolved | Nanda's "always slightly privileged" caveat is in §6 and in Lens 1's "does not explain". |
| m14 | Stepper caption gave the answer | Resolved | No caption; the sum sits in the last note. |
| m15 | Hit area 42 px | Not changed (host CSS) | Carried (m14 here). Accepted in round 2. |
| m16 | Notes chip | Not applicable | Host chrome; blocks no control. |
| Audio | Round 1: #sum and #bets long to loop | Partly | #bets is shorter (725 words); #sum 1,145 and #dir 1,209 are still long. See m9. |
