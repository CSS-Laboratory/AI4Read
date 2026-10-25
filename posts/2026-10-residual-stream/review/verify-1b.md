# verify-1b: S5 round 1, second fact-checker, post 03 (residual stream)

Checked: `src/content.html` (text, 7 widget configs, 3 fold-outs) and `audio-script.md`.
Evidence used: `source-brief.verified.md` (units 1-15 and the writer-must-not-use list), `sources/*.txt` and the MacKay PDF extract, `notebook/results.md`, the saved outputs of both `.ipynb`, and `node site/ai4read/components/check.mjs` (7/7 widget configs OK).
Not read: `self-review.md`, `numbers.md`.
Line numbers: `C:` = `src/content.html`, `A:` = `audio-script.md`, `Olah/Elhage/Nanda L` = line in the saved `.txt`.

## Counts

| Critical | Major | Minor |
|---|---|---|
| 0 | 3 | 22 |

---

## Major

### V1B-M1 · "The evidence is two circuits in a vision network" is wrong
- **Location:** C:182 (Bet 2); A:75; also C:372 / A:132 "their evidence is a vision network".
- **Post text:** "The evidence is two circuits in a vision network, and the test they propose ... is a plan".
- **Source:** Olah has three titled circuit sections: `## Circuit 1: Curve Detectors` (L413), `## Circuit 2: Oriented Dog Head Detection` (L457), `## Circuit 3: Cars in Superposition` (L492). Beside them stand `Argument 7: Handwritten Circuits` (L327, "hand setting all weights to reimplement curve detection ... significantly mimic the original curve detectors") and `Circuit Motifs` (L512). The post itself cites Circuit 3 at C:394. Claim 3 uses several vision architectures (AlexNet, InceptionV1, InceptionV3, residual nets, L549), not one network.
- **Why it matters:** The miscount understates Olah's evidence in the place where the post sorts the claims by firmness (balance rule, both directions). The "is a plan" sentence also applies the Circuit 2 plan (L490) to "the test" in general, while Argument 7 reports a weight-based reimplementation.
- **Fix:** Write "the worked evidence is three circuits in a vision network (curve detectors, a dog-head detector, cars and dogs sharing neurons), plus a hand-built reimplementation of the curve detectors". Keep: "the weight-editing test is planned (L490), not reported". Change "a vision network" to "vision networks" in the short answer.

### V1B-M2 · Quote cut before the turn, and two passages joined by "but" (house rule, WRITING §9)
- **Location:** C:186 (Bet 3); A:77.
- **Post text:** "The authors suspect it is “likely true”, but “the only evidence we can offer today is anecdotal”."
- **Source:** Two different passages. Olah L587: "These results have led us to suspect that the universality hypothesis is **likely true, but further work will be needed to understand if the apparent universality of some low-level vision features is the exception or the rule**." Olah L547 (about 40 lines earlier): "Unfortunately, the only evidence we can offer today is anecdotal".
- **Problem:** The L587 quote stops just before its own qualifier ("but further work ... the exception or the rule"). The L547 line is then attached with the post's "but" and in reverse order. S2 already warned: "quote both parts together or neither: the second part is the turn" (unit 3).
- **Fix:** "Their evidence is, in their words, “only ... anecdotal” (L547), from “a couple low-level features” seen in several vision models. It led them “to suspect that the universality hypothesis is likely true, but further work will be needed to understand if the apparent universality of some low-level vision features is the exception or the rule”." Make the same change in the audio.

### V1B-M3 · Short answer (c): "For language models the three sources give no test" is too broad
- **Location:** C:372 (and A:132); compare C:182.
- **Post text:** "For language models the three sources give no test, so we hold all three as bets."
- **Source:** Elhage's paper is a circuit analysis of attention-only language models with one and two layers. It includes a test of a mechanistic theory (`## Checking the Mechanistic Theory`, L512; `## Induction Heads`, L472). C:182 itself says Elhage limits "their circuit results" to such models.
- **Problem:** Bet 2 (circuits) therefore has some test in small language models. The true narrower claim is that no source tests any of the three bets in a trained language model of the size people use now. For bet 1 the post's own sentence at C:179 is already correctly narrow ("whether concepts are directions" in the stream).
- **Fix:** "For the trained models people use today, the three sources give no test. Elhage and colleagues' circuit results are for attention-only transformers of two layers or fewer, and none of them tests concepts as directions."

---

## Minor

### Quotes, attribution and firmness

- **V1B-m1 · "behaviours are circuits" put into Olah's mouth.** C:174 / A:69: the three parts include "behaviours are circuits", then "Olah and colleagues ... offered them as three claims". Olah's claim 2 is "Features are connected by weights, forming circuits" (L204). The nearest line about behaviours is hedged (L636, "it seems like ... could be broken down"). Brief note 10 flagged this. Fix: write "features are connected by weights, forming circuits".
- **V1B-m2 · Dropped condition on "read algorithms off the weights".** C:203. The fold-out lists "You can literally read meaningful algorithms off of the weights." under "Asserts". The source (L409) puts "seem to be" before it and "Once you understand what features they're connecting together" in front of it. Fix: add "(once the features are understood)".
- **V1B-m3 · "Concedes" for lines that are not concessions.** C:199. "if true, they could form the basis of a new “zoomed in” field" (L223) is a hedged hope, not a concession. Fix: use "Hedges" or "Supposes".
- **V1B-m4 · Referent of "this".** C:179. "The community is divided on whether this is true" (L232) is about "neural networks consist of meaningful, understandable features", not about the neuron sentence of L242 that precedes it in the post. The two passages are joined by "and concede". Fix: quote the L232 sentence with its referent, or write "on whether networks have understandable features".
- **V1B-m5 · "only a hint" is lower than Elhage's strongest line.** C:255 / A:94. Elhage L168: "Once added, information persists in a subspace unless another layer actively deletes it". Elhage L172 also gives the weight evidence: "very negative cosine similarity between their input and output weights". L745 credits "evidence of neurons performing memory management". Fix: delete "only", or add that L172 gives weight-level signs and that Elhage still words it as "hints" and "may".
- **V1B-m6 · "will try" dropped.** C:382 / A:141. "Elhage and colleagues pull apart the streams of communication “in terms of virtual weights...”". The source (L170) says "This is a major reason why we will try to pull apart ...". Fix: "say they will try to pull apart".
- **V1B-m7 · Hedge "we believe" dropped.** C:394 / A:152. "Olah and colleagues say that cars and dogs can share a neuron “As long as cars and dogs don't co-occur”". Source L510: "We believe superposition allows the model to use fewer neurons ... As long as ...". Fix: "believe".
- **V1B-m8 · "normally" dropped from the logit-lens procedure.** C:353. "it applies “the final layer norm, and unembed, and log_softmax”". Nanda L1425: "we **normally** apply the final layer norm, and unembed, and log_softmax, rather than linearizing anything". Fix: "normally applies".
- **V1B-m9 · Nanda scope sentence is one-sided.** C:189 / A:79. "mostly a description of how GPT-2 works" (L569) is followed by "there are many variants, but they're all essentially the same thing, even GPT-3, Gopher, Chinchilla and PaLM". Fix: add that clause so that Nanda's strongest scope claim is shown beside the hedge. Likewise, Nanda L156-159 calls the bolder universality "(and IMO probably false)", and the post leaves it out (optional, balance).
- **V1B-m10 · "defines a probe as" quotes a fragment of the procedure.** C:305 / A:109. The second quotation ("giving a 1D linear map (a probe), corresponding to a direction ... which likely corresponds to that feature", Nanda L1587) is the result of training in the description of probing. Fix: "describes the result of probing as".
- **V1B-m11 · Wrong source for a statement about ReLU.** C:333. "the MLP's curve acts on each coordinate separately <Elhage 2021, § Activation Properties>". Elhage (L850) says that a privileged basis comes from "a sparse activation function such as ReLU" and that MLP activations have one. "acts on each coordinate independently" is Nanda (§ Representations of Features). Fix: cite Elhage L850 for "privileged" and Nanda for the coordinate-wise statement.
- **V1B-m12 · Wrong or loose section labels.** (a) C:197 cites § Claim 1: Features for "Curve detecting neurons ..." (L273), which is under `Example 1: Curve Detectors`. (b) C:466 cites Nanda § General for fine-tuning and RLHF (L905, L908), which are under `## Training`. (c) C:229 and C:382 are fine; the Nanda "central object" quote at L1408 is under DLA as cited. Fix: correct (a) and (b).
- **V1B-m13 · Audio paraphrase drops "mostly true of".** A:73: "a decent amount of empirical evidence for Inceptionv1, but it seems at best only slightly true for transformers". Nanda L259: "evidence that this is **mostly true of** Inceptionv1". Writer-must-not-use item 4 asks for both halves. Fix: "evidence that it is mostly true of Inceptionv1".
- **V1B-m14 · Audio MacKay line is flatter than the source.** A:153 says "the input state was zero, one or one, zero" and drops "it could be that". Fix: "the input state could have been".
- **V1B-m15 · "Compare lists from two models by dot products" is ambiguous (our reasoning).** C:371, C:462 (A:130). The rotation argument covers dot products among the vectors of one model after rotating them all together. A dot product between a vector of model A and one of model B is not invariant when only one model's basis changes. Fix: "compare the dot products among the lists of each model (their Gram matrices), not the coordinates".

### Numbers and notebook claims

- **V1B-m16 · "the +3 remains" is wrong.** C:254. "The second number of a2 was -2 and that of f2 is +2; they sum to zero, so the -2 is no longer visible, while the +3 remains." In the first place a2 has 3 and f2 has -1, so the block's net first number is 2 (a2+f2 = (2,0); recomputed). Fix: "while the first numbers 3 and -1 leave a net +2".
- **V1B-m17 · "largest relative differences" is selective.** C:370 (A:128), repeated by the table at C:153-157. Notebook 02 (saved output, `d_hs_diff_vs_writes`, results.md row 43) shows `hs[l+1]-hs[l]` against the writes at max rel **6.2e-06** for l = 0..10, larger than 7.8e-7 and 1.03e-6. The 1.03e-6 reorder test is also on the stream after 12 blocks (k = 12), outside "k = 0 to 11". Fix: add the 6.2e-6 line to the table, or write "relative differences between 5e-7 and 6.2e-6".
- **V1B-m18 · Condition dropped in the table row.** C:156. "TransformerLens's stream against the Hugging Face list ... 7.8e-7" is for the raw (unprocessed) bridge (results.md rows 23, 26). With `enable_compatibility_mode` the difference is 2.5e-2 to 4.3e-2 (row 26). C:424 (3) gives the compat result, but without saying that the two TL numbers differ. Fix: write "raw-weight TransformerLens stream" in the row.
- **V1B-m19 · "exactly the input of block l" in every model is shown only for GPT-2.** C:159. Saved outputs print `b_hs_l_vs_block_in = 0.0` only for GPT-2 small (cell 18 output). For the tiny Qwen3 and Gemma 3 the saved table shows the indirect row (1.1e-7 and 8.6e-8) only. Fix: "in GPT-2 small exactly; in the tiny models to within 1e-7". Related: the term box at C:164 says the test "lets us treat the last two as equal in GPT-2 small" without the last-entry exception (C:159 gives it).
- **V1B-m20 · "far larger: 10.3".** C:424. Position 0 at depth 0 has norm 10.3 against a median of 5.3 (ratio 1.94, results.md row 11); it becomes "far larger" only from block 2 on. Fix: "far larger from the third block on: ..., 3155.5 after 11 blocks".
- **V1B-m21 · Widget scale hides numbers.** C:238-246 (`read-split`). `bars.max` is 9 and the component clamps at 0-100% (`widgets.js` `barsHTML`). The preset "along a₂" (r = (3,-2)) gives the share 13, and r = (3,-3) gives 15, so both bars stop at full width. Negative shares (attention 2 = -1 in the default preset) show as empty bars, though the number is printed. Fix: set `max` to 15 and say in the note that negative shares show as an empty bar.

### Citation gap

- **V1B-m22 · Recall card 8 is uncited and from nowhere in the post.** C:482 / A:`recall` Q8. "Large scores push the softmax into regions with tiny gradients, the authors suspect" has no source ("the authors" are not named, Vaswani et al. 2017 is not in Sources), and nothing in the post teaches scaled dot-product attention. The card is also not marked ↻, though cards that repeat are meant to be. The content matches what I recall of Vaswani et al. (variance d_k, "We suspect ...") but that is outside this post's evidence. Fix: cite the paper in Sources and in the card, or replace the card with one on this post.

---

## Text against audio

- **Chapters.** The 12 audio chapter ids (hook, guess, sum, bets, rw, dir, answer, lens-linalg, lens-info, turn, work, recall) match the 12 `data-ch` sections in order. "Sources" has no chapter, as expected. The chapter titles in the audio shorten some h2 titles (e.g. "Three bets"), which is fine.
- **No additions found.** I read the audio against the text chapter by chapter. Everything it says is in the text, with these differences, all paraphrase or cuts: the "Welcome to AI4Read from CSS Lab. This is post three" intro (required, and not a cross-reference); recaps that restate the section; "Qwen3 one point seven billion" for "Qwen3-1.7B-Base". The fold-outs are only mentioned (as WRITING §4 allows).
- **Carried-over faults:** V1B-M1 (A:75), V1B-M2 (A:77), V1B-M3 (A:132), V1B-m1 (A:69), V1B-m5 (A:94), V1B-m6 (A:141), V1B-m7 (A:152), V1B-m8 (not mentioned in audio), V1B-m10 (A:109), V1B-m13 (A:73), V1B-m14 (A:153), V1B-m22 (A:recall Q8).
- **Numbers in the audio** (margins at 0, 45, 90, 120, 135 degrees; 5.3 / 58 / 472 norms; 7.211561; 0.1318; 1.0935; 1.03e-6; 7.8e-7; 768; 2048; "thirteen shares") all equal the text and the notebooks.

## Standalone

No reference to another post in the text or the audio: searched for "post 0", "earlier/previous/last post", "as before", "remember", "village", "Harari" and the like (only "earlier" as an ordinary word). "post three" in the audio intro names this post. Every toy (calm/urgent cloud, three-feature plane, norm table, M matrix) is re-introduced inside the post. Spaced-review card 8 (V1B-m22) repeats earlier material without naming it, as WRITING §0 allows; the problem is only its missing source.

---

## Checked and found correct

**Quotes (machine-matched).** Every curly-quoted string in `content.html` was matched by script against the four saved `.txt` sources after whitespace, quote and dash normalisation. All 120+ quotes are verbatim; the unmatched strings were scare words, our own coined labels (e.g. "first plus first, second plus second", "like an edge weight") and the prompt text. The nested-quote cases (Nanda L1096 "What token is this"; Elhage L172 "memory management"; Olah L223 "zoomed in") were read in context. Section headings were mapped to line spans by script. All cited sections hold except V1B-m12. MacKay: Exercise 15.18 is PDF p. 249 = printed p. 237, Figure 15.3 is p. 238; the three quotes are verbatim; the "cannot hear the output" tension is stated correctly.

**Reporting verbs checked and right.** Olah: claims "offered ... deliberately speculative"; "believe", "concede" (community divided), "suspect ... likely true", "imagines" (periodic table), "plans" (L490), "supposes" (L636-637); Elhage "assert" for no privileged basis (L158, idealised stream); Nanda "backs with an intuition", "writes ... a decent amount of empirical evidence ... at best only slightly true" (neuron version, with "mostly true of Inceptionv1"), "an argument, not a measurement" ("almost"), "as an intuition" (bottleneck interference; "a pretty open question" refers to whether the neuron case is harder in practice). The Olah text hidden in HTML comments (brief unit 1: L147-148, L249-254, L265, L267, L287, L455, L658) is not used. None of the writer-must-not-use items 1-15 occurs except the half-quote in the audio (V1B-m13). "Steering", "activation addition", "hidden state" and the model families are correctly reported as absent from all three sources (re-grep: 0 hits).

**Toy numbers recomputed in Python (all match the post):** the stepper rows (1,2) -> (3,1) -> (2,2) -> (5,0) -> (4,2); the shares 5, 0, 1, -1 (sum 5, direct 5) and the r = (0,1) edge case (2, -1, 1, -2; total 0); E1-E5 solutions; calm/urgent scores and margins at 0, 45, 90, 120, 135 degrees (-4, -2.828, 0, 2.000, 2.828); u = (-0.707, 0.707) and scores -1.414 / +1.414; push by 2u moving scores by 2 (-1.414 -> 0.586, 1.414 -> 3.414); the sideways push u.v = 0; the 90-degree rotation (x2 -> (-2,4), r -> (-2,1), shares unchanged); the norm table (mean 3 / 6, sd 1 / 2, normalised (1,-1) both, r.norm = -1, r.stream = 8 / 16); the logit-lens toy rows (1.000, 1.232, -2.232 / 2.000, 0.732, -2.732 / 4.000, -0.268, -3.732); the three-feature toy (1, -0.5, -0.5 and the all-on silence); M(1,0) = (2,1), M(1,1) = (3,3), M(1,-1) = (1,-1). The widget checker prints the same values for the default state of all 7 widgets.

**Notebook numbers matched to saved outputs and results.md:** 0.0 for in-order sums; 4.27e-4 abs / 1.03e-6 rel (reordered); 4.88e-4 / 7.8e-7 (raw TL vs HF, k = 0-11); 1.09e-6 (processed TL vs HF minus mean); 0.986 and 0.0 (HF last entry vs raw and normed block output); 834.6 (no-norm lens) and 0.0 (with norm); lens ranks of " it" (2025, 1, 2, 3, 4, 2, 2, 1, 0, 1, 0, 0, 0) and the rank-12 no-norm value; norms 5.3 / 58.0 / 472.4, BOS 10.3 / 3155.5 / 417.4; 7.211561 twice (13 shares); steering residual 0 for alpha = 0.5, 1, 2, 5, -3; cosine 0.1318 against 1.0935; Gemma 3 relative error 9.7 and 0.0; epsilon 1.19e-7 (printed 1.192e-07; numpy 1.1920929e-07); GPT-2 numbers 768 / 12 blocks (Nanda L611-625); Qwen3 hidden size 2048; versions and line numbers in the Sources list (L12, L15, L17-L19, L2).

**Not checked (out of the task):** the S5 pedagogy and English-level criteria, `cite-map.tsv` completeness, word count, and the HF/TransformerLens line numbers against a fresh install (taken from results.md, whose rows I matched to the saved outputs).
