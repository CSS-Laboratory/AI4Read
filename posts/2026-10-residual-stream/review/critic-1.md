---
name: critic-1
post: 2026-10-residual-stream
stage: S5 round 1 (pedagogy critic, blind to self-review.md)
date: 2026-10-25
read: src/content.html (7,358 main words), built index.html at 390 px (Playwright, touch and mouse), audio-script.md; context from topic-card.md, kunhao-input.md, outline.md
---

# Critic round 1: post 03, "What Is a Hidden State?"

**Verdict: the gate is not met.** There are 0 critical and 9 major findings (M1-M9). Criteria 2, 3, 5 and 6 are at 3 at post level. The post is strong where it is concrete: the add-by-hand opening, the stepper, the read-split table, the probe widget and the exercises. It is weak where it turns abstract or empirical: the bets section, the "is the hidden state the stream?" block, and the undefined "norm". These can be fixed in one round without a rewrite.

## 1. Post-level scores (minimum over sections)

| # | Criterion | Score | Reason in one line |
|---|---|---|---|
| 1 | Factual accuracy and hedges | not my gate (fact-checker); provisional 4 | Hedges are kept and "ours" is used well. I re-did the toy arithmetic by hand and in the widgets: every toy number, the logit-lens table, the norm table and all five exercise solutions match. Two items for the checker: the recall card on attention (M8) has no source, and "analogous can only mean … rotation" (m9) is overreach. |
| 2 | Ladder for a high-school reader | **3** | §3 and §5 climb fully. §4 starts at abstract claims with no instance. §6 packs five new ideas into one paragraph. The reorder check skips a step (floating point). The open question needs matrix multiplication that is never taught. |
| 3 | Clarity and English | **3** | "Norm" is used in five places before it is defined, and the definition sits in a fold-out. Relative error, logits and "final norm" are never glossed. Several paragraphs have more than 5 numbers or 100+ words. |
| 4 | Insight and connections | **4** | Both lenses give a link type, what they add and what they do not explain. Lens 2 adds a question Lens 1 cannot. Lens 1 is mostly a recap. The 3C ties are good. No cross-post reference was found. |
| 5 | Illustrations and interactives | **3** | The stepper, bus diagram, read-split and probe-push work at 390 px with 0 console errors. The rotate and three-features widgets have no picture, and the rotate widget mismatches the text (M4). The probe-push widget has defects (§4). Bets have no figure. |
| 6 | Concision | **3** | At 7,358 words the post is under the cap but near it. About 15% can go: the empirical block in §3, quote-stacking in §4 that the fold-out repeats, and a recap-style Lens 1. |

## 2. Section scores (criteria 2-6)

| Section | C2 | C3 | C4 | C5 | C6 | Note |
|---|---|---|---|---|---|---|
| hook | 4 | 4 | 4 | n/a | 4 | Opening sentence is good; the "configuration file / notebooks" sentence is the first place a high-school reader gets lost (see §3 below). |
| guess | n/a | 4 | n/a | n/a | 4 | Good questions. Q1 is spoiled by the hook (M5). |
| sum (§3) | 4 | 3 | 4 | 4 | 3 | Best ladder in the post, then a dense empirical block (M1, M6). |
| bets (§4) | 3 | 3 | 4 | 3 | 3 | Abstract first, quote-heavy (M3). |
| rw (§5) | 4 | 4 | 4 | 4 | 4 | Complete ladder. The widget challenge is stale (m1). |
| dir (§6) | 3 | 3 | 4 | 4 | 4 | Overloaded paragraph, unmotivated unit length, rotation mismatch (M2, M4, M9). |
| answer | 4 | 3 | 4 | n/a | 4 | The (a) paragraph is dense (m11). |
| lens-linalg | 4 | 4 | 4 | n/a | 3 | Mostly recap. |
| lens-info | 4 | 4 | 4 | 3 | 4 | Good toy, but no picture and a stale challenge (m1, m5). |
| turn | 3 | 4 | 4 | n/a | 4 | Exercises are good. The open question skips a step (M7). |
| work | 4 | 4 | 4 | n/a | 4 | Honest; "Collaboration: no link" is fine. |
| recall | 3 | 3 | n/a | n/a | 4 | Card 8 is undefined jargon (M8). |

## 3. First sentence where a high-school reader gets lost

Hook: "…and Qwen3-1.7B-Base, whose configuration file we read for the notebooks, has 2,048." This is the first sentence. The reader does not know what a "configuration file" is, what "the notebooks" are (they are introduced in the last hook paragraph), or what the model name means. The comparison "768 vs 2,048" adds nothing for them.

The first *conceptual* gap is in §3: "first an attention part, then an MLP part (short for multi-layer perceptron, a small network)". Neither is explained beyond "the part that can bring in information from other positions". This is acceptable for a post about the stream, but the post should say once, in plain words, "treat these as two black boxes, each computes one vector from the stream". Currently "computes a vector" is the only hint.

## 4. Findings

### Major

**M1. "Norm" is used before it is defined, and its definition lives in a fold-out. (WRITING §3, §4)**
- Location: #sum "the library overwrites it with the model's final output, which has been through the final norm"; "In Gemma 3 … norms each sub-layer's output before adding it"; "In Qwen3 the norm sits in front of each sub-layer". Also #rw "a real model puts a norm in front of every read … The fold-out at the end of section 6 shows what a norm does", #answer "final-normed", and #turn "The final norm plus the unembedding".
- Problem: the key result of the identity test, that the last entry is an exception and that Gemma differs, rests on a word the main text never explains. §4 says explanations the argument needs go in the main text, and "Look inside" must leave the main text standing alone.
- Fix:
  1. At first use in #sum, add 3 short sentences to the paragraph. For example: "A **norm** is a rescaling step. It takes a list, subtracts the average of its numbers and divides by their spread (the standard deviation), so that the list always has the same size. The toy list (4, 2) becomes (1, −1), and so does (8, 4)." That is the 2-line core of the fold-out table.
  2. Keep the full table in the fold-out.
  3. Replace "The fold-out … shows what a norm does" with a pointer to the main-text definition.

**M2. §6 "A score along a direction" crams five new ideas into one 102-word paragraph, and two steps are missing. (WRITING §2, §5)**
- Location: "Now turn a reading arrow instead of using the axes. A direction is an arrow … length 1 … (−1,1) has length √2 … Divide by it … The score … The margin …".
- Problems:
  - (a) There are about 20 numbers and 6 new items: direction, unit length, Pythagoras, normalising, score, margin.
  - (b) The reason for unit length is never given. It is: "so a score is the distance along the arrow, and scores from different arrows are comparable".
  - (c) The geometric meaning of a score is absent from the text, although the widget draws dotted perpendiculars and foot-points. Say: "the dotted line drops each point onto the arrow; the score is how far along the arrow the foot lies, with sign."
  - (d) "(cos φ, sin φ)" assumes the unit-circle definition. Add one line: "cos φ and sin φ are the horizontal and vertical positions of the point at angle φ on a circle of radius 1."
  - (e) "Score" is defined twice with `<dfn>` (in §5 and §6).
- Fix: split into three short paragraphs.
  1. Why one coordinate fails (the cloud, listed as points).
  2. Direction and unit length, with the shadow reading.
  3. Score and margin, with the (4,2) check.
  Put one sentence on "fitted" in the probe definition. Then give the widget before the margin table (see m2).

**M3. §4 "Three bets" starts from abstract claims and is almost entirely attribution. (WRITING §2 step 1, §0 "the question over the person")**
- Location: the whole of #bets, for example "Bet 1 · … A feature is a property of the input … By 'direction' … 'a linear combination of neurons in a layer' …", and Bet 2's 188-word paragraph.
- Problems:
  - The reader meets "feature", "direction", "linear combination of neurons", "circuit", "computational subgraph" and "universality" before they have seen one direction or one dot product. They are told "Section 6 makes this exact". That sends the reader elsewhere for the instance.
  - "Universality" and "analogous features" are never given an instance.
  - About 700 of the 809 words are who said what, and the fold-out repeats the same quotes. Several quotes appear three times (main text, trap box, fold-out).
- Fix:
  1. Give each bet one 2-sentence concrete instance in our own words, using the toy that follows. Bet 1: "In the calm/urgent cloud of section 6, 'calm vs urgent' will turn out to be the arrow (−1, 1): that is what 'a concept is a direction' would look like." Bet 2: "Think of the table of who-hears-whom in section 5 as one tiny circuit." Bet 3: "Imagine the same toy with every axis turned (section 6)."
  2. Cut the main text of each bet to claim, one hedge, and the "what the post does about it" line. Move the other quotes to the existing firmness fold-out.
  3. Alternatively, move §4 after §6 so that each bet is "cashed in" where the toy has just been seen. The current "Cashing in bet 1/2/3" lines already sit there.
- Target: about 450 words.

**M4. The rotation example mixes two different vectors, so the reader's own check fails. (§6 "Turn everything", widget `rotate`, E5)**
- Location: "The stream x₂=(4,2) becomes (−2,4), and r=(1,2) becomes (−2,1). … the four shares of section 5 are 5, 0, 1 and −1 before and after."
- Problem: the shares of §5 are for the read of the stream after attention 2, (5,0), not x₂. A careful reader computes (−2,1)·(−2,4)=8 and sees 8≠5. The widget has the same mismatch: it displays x₂ but the shares are for (5,0). The widget also never shows r's new coordinates (the text promises (−2,1)). The E5 solution repeats the problem ("x₂→(−2,4); the shares are still 5, 0, 1, −1").
- Fix: show the stream that is actually read, y=(5,0)→(0,5) at 90°, and its read r·y=5. Or switch the whole example to x₂ and give its shares, which are 1·4+2·2=8 as the sum of x₀…f₂ shares (5, 0, 1, −1, 3 for f₂, with total 8). Show r's rotated coordinates in the readout. Update E5 to match.

**M5. Guess-first Q1 is answered in the hook before the reader guesses, and the right options break the §5 rule. (WRITING §5, §0)**
- Location: the hook's `keypoint`: "The list is a running sum of what the earlier parts of the model wrote." Also g1 option 2 (73 characters, the longest and the most specific), and g2 option 3 (the longest).
- Problem: after the hook, g1 is a lookup, not a prediction. The keypoint also states "Reading it … is a dot product. Pushing it is adding a vector", which pre-answers g3's topic. The right option of g1 is the longest and most specific, which is exactly what §5 forbids.
- Fix:
  1. Rewrite the keypoint as a question-only preview: "Three questions drive the post: what the list is, what a part of the model can read from it, and what happens to a probe's score if every list is pushed by the same vector."
  2. Move the bank-balance picture after the guess (it also gives away g1).
  3. Equalise option lengths: g1 B, "The word's starting list plus every addition made so far"; g1 A and C lengthened to match. For g2 shorten C to "Only the sum, (0, 0)" and lengthen A, B and D.

**M6. The reorder check skips a step and appears to contradict the toy. (WRITING §2 step 6, §1)**
- Location: #sum "The same writes added in another order, against the stream after 12 blocks | 4.27e−4 absolute; 1.03e−6 relative" and "A relative difference near 10⁻⁶ is what 32-bit rounding gives (machine epsilon 1.19e−7)".
- Problem:
  - Two paragraphs earlier the reader was told "adding in the other order gives (3, 1) again". Now another order gives a different number, with no explanation. A high-school reader concludes that addition is not commutative.
  - "Relative" is never defined. "Machine epsilon" is jargon.
  - The paragraph after the table carries about 18 numbers (check: the "What we did not run" paragraph has 139 words and 18 numbers).
- Fix: add 2 sentences. "A computer keeps about 7 digits per number, so it rounds after every addition. Adding in a different order rounds at different places, so the last digits can differ, although the exact sums are equal. *Relative difference* means the difference divided by the size of the stream, here about one part in a million." Move the Qwen/Llama/Gemma code details (the 139-word paragraph) to a fold-out; keep the three-line "what we did not run".

**M7. The open question needs matrix multiplication, which the post never teaches. (WRITING §1, topic-card "hand-computable"; Kunhao's request for a bridge to eigen-decomposition)**
- Location: #turn "a block acts on the stream as M=((2,1),(1,2)). It turns (1,0) into (2,1)… sends (1,1) to (3,3)".
- Problem: "M acts on a vector" is not defined. The reader cannot check one of the three claimed images. This is the exit ramp to post 04, so it must be checkable.
- Fix: add one sentence that uses what they now know: "To apply M to a vector, let each row of M be a reader: the first number of the answer is row 1 dotted with the vector, the second is row 2 dotted with it. So M(1,1) = (2·1+1·1, 1·1+2·1) = (3,3)." This also links reads (dot products) to maps, which is the natural step into eigen-decomposition. Optionally add a hand exercise: compute M(1,0) and M(0,1) and find a vector M only stretches.

**M8. Recall card 8 asks about attention scaling, which the post never mentions. (WRITING §0 stands alone, §3 terms)**
- Location: #recall "In attention, why divide the scores by √d_k? … q and k … softmax … tiny gradients, the authors suspect."
- Problem: q, k, d_k, softmax and gradients are undefined. "The authors" is unnamed. There is no source entry and no ↻ mark, although the intro says only ↻ cards come back. The audio repeats it.
- Fix: either drop the card, or give it the ↻ mark and write it self-contained, with the term defined in the card, a named source and a Sources entry. As written it cannot be answered from the post. The fact-checker should see this too.

**M9. Probe-push widget: the probe half teaches well, but the margin is misleading in text and widget, and the push half shows no purpose. (WRITING §5, rubric 5)**
- What I tested: mouse and touch drag (CDP touch events) of both arrows. The sliders stay in sync (best-probe preset gives sliders 135, 135, 0; after a touch drag of v they read 135, 136, 0.6). The presets work. The readout numbers equal the text: margin −4.000 (0°), −2.828 (45°), 2.828 (135°) and u·v=0.600 after the drag. There were 0 console errors and the page did not scroll sideways. A touch on a handle does not scroll the page (touch-action none).
- What teaches: finding the best angle, the blind probe (feet coincide on the dashed line), and "push sideways" (points move, scores do not).
- Defects:
  - (i) **Margin sign.** The margin is −4.000 at 0° and 0.000 at 90°, although in both cases the groups "touch at 3". The negative sign means "the groups are in the wrong order", which the text never says. The text table of margins reads as a list of "how good" values. Add: "A negative margin means the groups overlap, or sit in the wrong order along the arrow."
  - (ii) **Steering has no purpose on screen.** There is no threshold line, and the readout does not show that a push leaves the margin unchanged (2.828 at any push). The text uses v=2u, which moves calm scores from −1.414 to 0.586. Use v=(−2,2) instead (as E4 does): every calm point lands exactly on an urgent point, so "steer calm into urgent" is visible and the scores move by u·v=2.828. State that the margin does not change: a push moves both groups together.
  - (iii) **Colour collision** (m3).
  - (iv) **v is invisible at first.** At α=0 the red arrow has zero length, and its handle is a dashed ring on the origin that the user must guess is draggable. Start with α=1.
  - (v) The score values are not written at the feet on the dashed line, so the reader cannot see which dot is which score without the 4-line readout.
- Fix: items (i) and (ii) are the changes that matter. (iii) to (v) are in minor findings.

### Minor

**m1. Two widget challenges are already answered on screen.** #rw: "Can you find a reader that cannot hear attention 1?" The default r=(1,2) already shows 0 for attention 1, and the text had just computed it. Ask for a different reader ("Find a reader, other than (1,2) and its multiples, that cannot hear the embedding": r=(2,−1) works, since (1,2)·(2,−1)=0). #lens-info: "Find a setting that looks exactly like silence" is answered two sentences earlier ("Write all three: the stream is (0, 0)"). Ask instead: "Find a different setting, not (1,1,1), that is silent" (answer: 0.5, 0.5, 0.5, or all zero), or "How many settings are silent?"

**m2. Widget before answer.** In §6 the margin table (all five values) comes before the widget, so the widget confirms rather than lets the reader find. Pose "find the best angle" first, then give the table.

**m3. Colour collision in the probe widget.** The probe arrow and the calm points are both blue, and the push arrow and the urgent points are both red. A reader assumes blue arrow = calm. Change the arrow colours (for example dark ink for u and green or orange for v) or mark the groups by shape.

**m4. Bars hide negative values.** In `read-split` the bars for −1 and −2 appear as a thin sliver. The edge case (r=(0,1): 2, −1, 1, −2) should visibly cancel. Use a centre-zero bar or show a sign colour.

**m5. Two widgets have no picture.** `rotate` shows only numbers; the lengths-and-angles-unchanged argument needs arrows. `three-features` shows only a table; the three arrows at 0°, 120° and 240° summing to zero is the whole point. Request a `vec2d` view for both (WIDGET-REQUEST), or a static diagram for three-features.

**m6. Bus diagram: the stream box does not show the running value.** The value is only in the step text and the arrow labels overlap the arrows ("(1, 2)", "+(−1, 2)" in preview). Put the current sum inside the Stream box.

**m7. A wide table scrolls at 390 px.** The margin table in §6 (6 columns) has `scrollWidth` 385 in a 358 px container. Transpose it into rows ("φ | margin") or two short lines. Three display formulas also scroll inside `.mjx`, which is allowed.

**m8. The cloud table does not list points.** "calm | 3, 4, 5 | 1, 2, 3" makes the reader pair the numbers. List the six points as (3,1), (4,2), (5,3) and (1,3), (2,4), (3,5).

**m9. Bet 3's cash-in overreaches.** "'analogous' can only mean 'the same up to a rotation'". Other invertible linear maps and permutations also preserve structure. Write "at least up to a rotation, never the same coordinates" and keep the "ours" label.

**m10. The hook does not name the title's key term.** "Hidden state" first appears in §3 "Is the hidden state the stream?". WRITING §0 says to define a key term from the question at first use. Add "People call this list a hidden state" in the first paragraph. The hook also lacks the reader's own act ("I pull a vector from layer 20") that Kunhao asked for. One sentence would do.

**m11. Short answer (a) is dense.** 126 words, with 7.8e−7 and 1.03e−6 in the verdict. The verdict itself (running sum, up to rounding, last entry the exception) fits in 2 sentences. Move the error figures to §3 only.

**m12. "13 shares" is unexplained.** #rw "the sum of its 13 shares" (after 6 blocks: the embedding plus 12 writes). Say so.

**m13. Duplicate `<dfn>`s and undefined small terms.** `score` and `blocks` are defined twice. "Logits", "log_softmax", "rank 0", "standard deviation", "post-training", "RLHF" and "fine-tuning" are used without a gloss. Neuron is used in §5 before the reader knows what a neuron is (only a "unit of a layer" in §4). Add 3-word glosses.

**m14. "Linear" has three uses (§5)** is stated without an instance. A one-line example of each (sum: (4,2)=sum; read: split into shares; concept: bet) would climb it.

**m15. E3 workload and terse solutions.** E3 asks for 18 dot products with √2. The hint should say: "all three points of a group give the same score on (−1,1)/√2, so compute one point per group". Solutions give results only; add one line of working to E2, E3 and E4 (the dot product written out).

**m16. The `keypoint` box in the hook is not one of the allowed boxes** (term, trap, answer, exercise, fold-out). It duplicates the argument. With M5 it becomes the question list; keep it as plain text.

**m17. Site chrome.** The floating "Notes" chip covers the right end of captions and the last readout lines at 390 px (seen on probe-push, read-split and the dir paragraph). This is the host page, not the post, but check the `--site` build. I could not run the strict-CSP render test on the standalone `index.html` (inline scripts are refused by design) and `site/ai4read/dist` has no copy of post 03 yet, so the 0-console-error result above is from the standalone page only.

**m18. Hands-on difficulty of the handle.** The drag ring is about 30 px across, below the 44 px touch target. It worked in my touch test, but a larger invisible hit area is safer on a phone.

## 5. Checks requested in the role prompt

**Widgets: can the reader do the mechanism, does the edge case teach, are readouts quoted correctly?**
- `sum-table` (stepper): yes. The rows start blank so the reader adds by hand first. The last note (cancellation) is the edge case. Numbers match the text.
- `bus` (diagram): yes, 6 steps. Minor: m6.
- `positions` (diagram): static, readable, fits at 390 px.
- `read-split` (lab): the mechanism can be done; the edge case (0,1) is right, but the bars hide the cancellation (m4) and the challenge is stale (m1).
- `probe-push` (vec2d): see M9. It teaches the probe, and half teaches the push.
- `rotate` (lab): M4 and m5. The edge-case caption is correct but the displayed vector is the wrong one.
- `three-features` (lab): numbers right (reads 1.000, −0.500, −0.500; all-three gives 0). No picture (m5); stale challenge (m1). Superposition is defined in the same section but the toy is never called an instance of it. Say: "This toy is superposition in the sense above: three features in two dimensions."
- Prose vs readout: every number I compared matches (margins at 0°, 45°, 90°, 120°, 135°; scores 2.828, 4.243, 5.657; 0.586 and 3.414 after the v=2u push; norm table; logit-lens table).

**Lens sections.**
- Lens 1 states the link type (same-math), what it adds, what it does not explain, and the 3C tie. It is largely a recap of §3-6. Its new content is "seeing is not doing", the difference of method between sources, and the cosine counter-example. Cut the recap and keep these three.
- Lens 2 states two link types (structural analogy, metaphor), what it adds (the question of limits and a case that looks like silence) and where the analogy breaks (MacKay's users cannot hear the output; no rate or capacity transfers). Each lens shows something the other does not: exact bookkeeping versus a counting question with interference. The information-theory link is thin (no entropy or capacity appears), and the post says so. That is honest and fine.

**Hook and guess-first.** The hook is clear but has no puzzle with tension and no layer-20 moment; the bank picture is good but placed late. Guess-first questions are conceptually good. They are weakened by M5.

**Exercises.** All five are hand-computable and the hints and folded solutions are present. I recomputed all five and the solutions are right. The set is calculation only. Add one "why" prompt to E2 (done: "why") and E4 (done); fine. See m15.

**Open question.** It leads cleanly to eigen-decomposition (the toy has two stretched directions, by 3 and by 1), and it ties to "no privileged basis". It is not checkable by hand until M7 is fixed.

**Phone readability.** No horizontal page scroll at 390 px; body text is 18 px. One table scrolls (m7). Dense paragraphs: #sum "What we did not run" (139 words, 18 numbers), #dir "Now turn a reading arrow" (102 words, about 20 numbers), #rw "With r=(1,2) the shares are …" (about 12 numbers), #turn "What to look for" (141 words, 23 numbers). The citation tags make several paragraphs hard to scan; this is acceptable.

**Main text holds the explanations.** Exceptions: the norm (M1) and the `keypoint` box (m16). Boxes are otherwise used as allowed.

**Jargon before definition.** Norm (M1), relative difference (M6), q/k/softmax (M8), logits, neuron, and direction/circuit/universality in §4 (M3).

**Stands alone.** No reference to another post, strand or earlier toy was found. The eyebrow "Post 03" is only a label. Recall card 8 is the one item that relies on outside knowledge (M8).

**Audio script.** Chapter IDs match the page sections one to one. The speaker names the source ("Welcome to AI4Read from CSS Lab"), formulas are spoken in words, and widgets are described. Issues:
- "R r dot R x equals r dot x" is ambiguous aloud; say "capital R applied to r, dotted with capital R applied to x".
- The #answer chapter recites 7.8e−7 and 1.03e−6 as speech; drop them.
- The #sum and #bets chapters are long for looping; the bets chapter is mostly quotation (cut with M3).
- Recall item 8 repeats M8.
- Update the audio together with any text change in M2, M4 and M5.

## 6. The three changes that would raise the post most

1. **Make §3 and §5 stand on their own: define "norm" in the main text with the (4,2)→(1,−1) toy, explain why a reorder changes the last digits and what "relative" means, and move the Qwen/Llama/Gemma code details to a fold-out (M1, M6, m12, m13).** This lifts criteria 2 and 3 and cuts about 250 words.
2. **Rebuild the §6 direction ladder and fix the widgets: three short paragraphs with the shadow reading, unit-length reason and trig line; margin sign; use v=(−2,2) so steering is visible; fix the rotation mismatch; change colours and the stale challenges (M2, M4, M9, m1-m5).** This lifts criteria 2, 3 and 5.
3. **Give §4 an instance for each bet and cut the quote-stacking, then fix the guess-first spoiler and the open question (M3, M5, M7, M8).** This lifts criteria 2 and 6 and removes the last standalone gap.

Expected result after these: criteria 2-6 at 4 or above, if no new errors are introduced. Rerun the numbers in `check.mjs` after the widget changes, and re-check the quote boundaries in any text that is moved.
