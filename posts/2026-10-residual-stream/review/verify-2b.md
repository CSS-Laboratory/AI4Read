---
name: post03-verify-2b
stage: S5, round 2, second fact-checker
checker: independent fact-checker (fresh agent; did not write the post; worked in parallel with the other round-2 checker)
date: 2026-10-25
checked: src/content.html (text, 8 widget configs, 3 fold-outs, recall, sources) and audio-script.md
evidence: source-brief.verified.md (units 1-15 and the must-not-use list); sources/*.txt and mackay-2003-mac.txt; notebook/results.md; saved outputs of notebook/01_bus_gpt2.ipynb and 02_bus_my_model.ipynb; check.mjs; the installed transformers 5.19.0 source; review/verify-1.md and verify-1b.md
not read before the pass ended: self-review.md, numbers.md, response-1.md (read last, only to compare its claims with the files)
line refs: C = src/content.html line; A = audio-script.md line; "Olah/Elhage/Nanda L" = line of the saved .txt
---

# S5 verify, round 2 (second checker): post 03

## Counts

| Critical | Major | Minor |
|---|---|---|
| 0 | 1 | 16 |

Round 1: of the 46 findings in verify-1 and verify-1b, 42 are resolved or moot, 3 are partly resolved (V1-10, V1B-m5, V1B-m18) and 1 is not resolved (V1B-m14). Response-1 says V1B-m14 was changed in the audio; the file does not show it.

---

## Major

### V2B-01 · major · Lens 1: "none of the three sources addresses it directly" is false, and the next sentence cites a source that does
- **Where.** C:404 (`#lens-linalg`): "A high probe score shows that information is present along a direction, not that later parts of the model use it; that needs tests this post does not run, and none of the three sources addresses it directly." A:151 says the same.
- **Source.** Nanda § Non-MI Techniques, TCAV, L1593-1598: "A technique to measure how important a concept is for a model output on a specific input". It "first defines a Concept Activation Vector, essentially a probe", then takes the derivative of the output with respect to the layer's activation and compares it with the probe direction. Nanda also lists activation patching (L1442), ablation (L1361-1375) and causal tracing (L1458), all of which test whether a part is used. Brief unit 12 lists TCAV (L1593-1598) in its "Where" line, but its claim that use "is not addressed here" is itself too broad.
- **Problem.** An absence claim about the sources ("never" in WRITING §9: search first) that a grep disproves. The post contradicts itself: it quotes Nanda's ablation caution in the very next sentence. TCAV is the glossary's own method for asking whether a model uses a probe-like direction.
- **Fix.** "…that needs tests this post does not run. Nanda's glossary lists such tests (activation patching, ablation, and TCAV, which scores how much a probe-like direction matters for an output) but does not apply them to a probe's direction in a language model." Make the same change in A:151.

---

## Minor

### Sources and attribution

- **V2B-02 · "The Hugging Face library does not say 'residual stream'" is false as worded.** C:156. In the installed transformers 5.19.0, 17 files use the phrase, for example `models/hyperclovax/configuration_hyperclovax.py:39` ("Scaling factor applied to each sub-layer output before adding to the residual stream") and `models/gemma4/configuration_gemma4.py:95`. None is in GPT-2, Qwen3, Gemma 3, Llama or Mistral. Round 1 (V1-10) asked for the narrower "Hugging Face transformers does not say…". The narrowing is still an unchecked absence claim. Fix: "The Hugging Face output is named `hidden_states`, not 'residual stream'". A:54 says "does not say residual stream" too.
- **V2B-03 · "entry 0 is the embedding" is not what the notebook measured in GPT-2.** C:165 (and C:394, A:60): "entry 0 is the embedding". C:71 defines the embedding as the lookup-table row and then says GPT-2 "also adds a learned list for the token's position". Notebook 02 (results.md rows 36-37, cell [7]): `hidden_states[0]` against `wte(ids)` has relative error 3.63 (no match), and against `wte(ids)+wpe(positions)` it is 0.0. A reader who checks entry 0 against the lookup table finds a mismatch. Fix: C:165 "entry 0 is the embedding plus, in GPT-2, the position list". C:71 should say the position list is added to the starting list. Keep it in the short answer: "the embedding (and, in GPT-2, the position list)".
- **V2B-04 · Wrong section for GPT-2's learned position list.** C:71: "GPT-2 also adds a learned list for the token's position <Nanda 2022, § Transformer Basics>". Nanda L586 (Transformer Basics) says only "embedded tokens plus the positional embedding". "GPT-2 does with learned, absolute positional embeddings" is L671, § Transformer Components, Positional information. Fix: cite "§ Transformer Components, Positional information/embedding".
- **V2B-05 · Main text loses the referent of "is the exception or the rule".** C:198: "'suspect that the universality hypothesis is likely true, but further work will be needed' to tell whether it 'is the exception or the rule'". Olah L587: "…to understand if the apparent universality of some low-level vision features is the exception or the rule". "It" reads as the hypothesis, which the authors suspect is likely true; the source's open question is about the apparent universality of some low-level vision features. The fold-out (C:225) has it right. Fix: copy the fold-out wording into C:198.
- **V2B-06 · "because the stream is a bottleneck" turns "a major reason" into the reason.** C:405 (A:150). Elhage L170: "This is a major reason why we will try to pull apart the different streams of communication … in terms of virtual weights". Fix: "…partly because the stream is a bottleneck".
- **V2B-07 · Nanda's own caveat on privileged bases is missing.** C:339, C:356, C:402. The post quotes Nanda L243 and L234 for rotation invariance and says "never read 'dimension 17' as a feature". Nanda L245: "privileged/non-privileged bases is a somewhat leaky abstraction, and the standard basis is always slightly privileged. Floating point representations and Adam inherently privilege the standard basis … I mostly think of it as a spectrum". The brief (unit 8 traps) asks the post to note it. The post does restrict Elhage's claim to "their idealised linear stream", which helps. Fix: one clause in C:356, for example "Nanda adds that in practice the standard basis is 'always slightly privileged' (floating point, Adam), so he treats it as a spectrum".
- **V2B-08 · "an intuition, not evidence" is our reading, and the strongest half of the line is left out.** C:212: "Nanda, on 'features as directions': an intuition, not evidence: 'the main thing a model is capable of doing is linear algebra'". Nanda L200 calls it "the intuition behind this" and goes on: "features as directions is an extremely natural way to represent things" (brief unit 12, S2 balance addition). "Not evidence" is the brief's classification; it is not Nanda's. Fix: "Nanda, on 'features as directions', gives an intuition (ours: not a measurement): 'the main thing …', and concludes it is 'an extremely natural way to represent things'".
- **V2B-09 · "the test itself is future work" sits under the wrong citation.** C:219 (fold-out, "Proposes and plans"): the L633 quote and the sentence "the test itself is future work" are both cited to § Interpretability as a Natural Science. The plan to test by editing weights is Olah L490 (§ Circuit 2), which C:194 cites correctly. Fix: add "<Olah 2020, § Circuit 2>" after "future work".
- **V2B-10 · "MacKay's adder channel": MacKay never says "adder".** C:415 and C:451. Grep of mackay-2003-mac.txt for "adder": 0 hits. MacKay writes "a binary multiple access channel with output equal to the sum of two inputs". The name is ours and unlabelled. Fix: "MacKay's binary sum channel (our name)", or quote the caption.
- **V2B-11 · Two unsourced, unlabelled sentences.** (a) C:135: "This is GPT-2's version; other models use close variants." No cite. Notebook 02 (results.md row 35) shows GPT-2's `LayerNorm`; the Qwen3 and Gemma code is read in `box-code`. (b) C:498: "In the algebra, a prime or a frame added to a model is one more write along a direction." This is a statement of what a prime is, and no source supports it. The next sentence says "candidate", which helps. Fix: (a) cite "Notebook 02, reference run" and "HF modeling_qwen3.py, lines 49, 62-63" or write "(ours)". (b) "If a prime or a frame were added as a vector, it would be one more write along a direction (ours)".

### Notebook

- **V2B-12 · Notebook 01 prints a different margin from the post.** The W9 cell (cell [10], results.md row 21) prints "W9-C phi= 0: … margin 0.000" and "margin by phi: {0: 0.0, 45: -2.828, 90: 0.0, …}". The post (C:293, C:318) defines margin as lowest urgent minus highest calm and gives −4.000 at 0°. results.md ("W9 margin") says the notebook uses max(min urgent − max calm, min calm − max urgent) and "the post should state that definition". The post states its own definition, but a reader who runs notebook 01 sees 0.000 where the page says −4.000 and may think one is wrong. Fix: one sentence in `#turn` ("notebook 01's margin takes the better of the two orientations, so it prints 0.000 at 0°") or align the notebook's cell.

### Text against audio

- **V2B-13 · Audio keeps "write only of hints".** A:102 "Elhage and colleagues write only of hints". The page (C:269) says "write of hints"; response-1 says "only" was removed (V1B-m5). Elhage L172 also gives weight-level signs ("very negative cosine similarity between their input and output weights, which may indicate deleting information") and L168 asserts, with no hedge, "Once added, information persists in a subspace unless another layer actively deletes it". Fix: "…write of hints, which they word with 'may'".
- **V2B-14 · Audio MacKay line is flatter than the page; response-1 says it was changed.** A:170: "If the output is one, the input state was zero, one or one, zero". Page (C:418): "it could be that the input state was (0, 1) or (1, 0)". Response-1, V1B-m14: "Audio MacKay line says 'it could be that…'". Grep of the audio for "it could be that": 0 hits. Fix: "if the output is one, it could be that the input state was zero, one or one, zero".
- **V2B-15 · Audio drops "(raw weights)".** A:56: "The TransformerLens stream agreed with the Hugging Face list within seven point eight times ten to the minus seven". The page row (C:161) names the condition: raw weights. With TransformerLens's default processing (`enable_compatibility_mode`) the same comparison differs by 2.5e-2 to 4.3e-2 (results.md row 26). Fix: "The raw-weights TransformerLens stream agreed …".
- **V2B-16 · Audio adds a source fact that is not on the page.** A:168 (`lens-info`): "Elhage and colleagues note that a single MLP layer typically has four times more neurons than the residual stream has dimensions." The fact is Elhage L170 and correct, but it has no counterpart in C:417 and no citation. Fix: delete it from the audio, or add it to C:417 with the cite "Elhage 2021, § Residual Stream Bandwidth".
- **V2B-17 · Audio guess-first options differ from the page and give away the answer.** A:25: "Option two: a running total, the word's starting list plus every addition made so far." The page option (C:50) has no label "a running total", which is the answer's name in the reveal (C:173). A:29 Q2 option 4 "because the first write is kept for good" against the page's "kept and the second ignored". A:52 "So there is no hidden state of a sentence." drops the page's "(ours)" and the clause that a summary is a further step someone must choose. Fix: use the page wording for the options, and add "That is our point, not a source's." after A:52.

---

## Round-1 findings: resolved or not

| ID | Status | Evidence |
|---|---|---|
| V1-01 | Resolved | C:395 now says "for the trained language models people use now" and names Elhage's circuits in attention-only models; C:194 agrees. |
| V1-02 | Resolved | C:394, C:497, C:356-358, A:144, A:work and recall card 6 all say "each model's own dot products"; C:497 adds that a cross-model dot product is not protected. |
| V1-03 | Resolved | C:264 and A:100: "agree to all printed digits … 0.0 in this run" (results.md row 49), no invented reason. |
| V1-04 | Resolved | Recall card 8 is now on the margin sign (C:517); no attention or √d_k content. |
| V1-05 | Resolved | C:194, A:81 "three … in vision networks (curve detectors, dog heads, cars in superposition)" (Olah L413, L457, L492). |
| V1-06 | Resolved (see V2B-05, minor) | C:198 and C:225 give L587 through its turn and L547 separately. |
| V1-07 | Resolved | C:201 carries the Elhage "forthcoming paper" clause and Nanda's "all essentially the same thing, even GPT-3, …". |
| V1-08 | Resolved | C:356 cites Nanda § Representations of Features for the ReLU sentence (L240). |
| V1-09 | Resolved | C:501 cites § Training (L905, L908). |
| V1-10 | Partly | Narrowed to "The Hugging Face library", but still false as worded: V2B-02. |
| V1-11 | Resolved | "independent record" is gone; the 6.2e-6 row is in the table (C:162). |
| V1-12 | Resolved | C:459 and A:34: far larger after two or more blocks, 417.4 after 12 (results.md rows 10-11). |
| V1-13 | Resolved | C:376 "it normally applies" (Nanda L1425). |
| V1-14 | Resolved (see V2B-06, minor) | C:405 "say they will try to pull apart … rather than studying it directly". |
| V1-15 | Resolved | C:170 "for entries 0 to 11 in GPT-2 small"; C:173 states the last entry is normed. |
| V1-16 | Resolved | C:395 "vision networks, mostly InceptionV1". |
| V1-17 | Resolved | C:218 and C:219 carry the cite (but see V2B-09). |
| V1-18 | Resolved | Elhage URL in C:528; C:459 cites Notebook 01 for 1.09e-6. |
| V1-19 | Resolved | A:10 "GPT-2 small", A:12 "our summary of common practice"; the Nanda "mostly true" sentence is no longer in the audio. |
| V1-20 | Resolved | english.json l. 31 and loop l. 257 now use "first approximation" for a read, with the norm as the non-linear part (spot-checked; English pack not otherwise in this pass). |
| V1-21 | Resolved | Loop l. 257 "may not simply carry over to a trained Qwen3 or Llama, which we did not run"; l. 203 "with the hooks placed correctly". |
| V1B-M1 | Resolved | As V1-05; C:395 "vision networks". |
| V1B-M2 | Resolved | As V1-06, text and audio (A:85). |
| V1B-M3 | Resolved | As V1-01. |
| V1B-m1 | Resolved | C:185 "features connect through weights into circuits". |
| V1B-m2 | Resolved | C:217 "(They put this after understanding the features a circuit connects.)". |
| V1B-m3 | Resolved | C:211 headed "Hedges". |
| V1B-m4 | Resolved | C:190 and C:210 quote L232 with its referent. |
| V1B-m5 | Partly | Page fixed (C:269); audio still says "only of hints" (A:102): V2B-13. |
| V1B-m6 | Resolved | C:405 and A:150 "say they will try to pull apart". |
| V1B-m7 | Resolved | C:417 and A:168 "say they believe". |
| V1B-m8 | Resolved | As V1-13. |
| V1B-m9 | Resolved | C:201 adds the "all essentially the same thing" clause. The optional "(and IMO probably false)" is left out; acceptable. |
| V1B-m10 | Resolved | C:325 "In Nanda's description you train a linear map … giving a 1D linear map (a probe)". |
| V1B-m11 | Resolved | As V1-08. |
| V1B-m12 | Resolved | C:208 cites § Example 1: Curve Detectors (L273); C:501 cites § Training. |
| V1B-m13 | Resolved (moot) | The Nanda neuron-version sentence is not in the audio any more. |
| V1B-m14 | Not resolved | A:170 still lacks "it could be that"; response-1 says it was changed: V2B-14. |
| V1B-m15 | Resolved | As V1-02. |
| V1B-m16 | Resolved | C:268 "the first numbers, 3 and −1, leave a net +2" (a2+f2 = (2,0), recomputed). |
| V1B-m17 | Resolved | The table has the 6.2e-6 row and names the depth of the reorder row (C:158-163). |
| V1B-m18 | Partly | Page row says "(raw weights)" (C:161); audio does not: V2B-15. |
| V1B-m19 | Resolved | C:165 "In GPT-2 small exactly (0.0); in the tiny random Qwen3 and Gemma 3 … about 10⁻⁷, except at the last step" (results.md row 62). |
| V1B-m20 | Resolved | As V1-12. |
| V1B-m21 | Resolved | `read-split` `bars.max` is 15 and the note says negative shares show as an empty bar. The widest share, r = (3, −3) on a₂, is 15, so no bar saturates. |
| V1B-m22 | Resolved | As V1-04. |

---

## Checked and found correct

- **Quotations.** Every curly-quoted string in content.html outside the widget configs (about 120) was extracted by script and matched against the four saved .txt files (case-folded, letters and digits only; split at ellipses). All source quotes were found. The unmatched strings are our own labels ("first plus first, second plus second", "like an edge weight", "push along", "dimension 17"). None is over 25 words. None comes from the hidden Olah lines (L147-148, L249-254, L265, L267, L287, L455, L658) or hidden Elhage L303. Each cited section was mapped to the `##` heading of the quote's line by script. Every one holds except V2B-04 and the cite placement in V2B-09. The labels "Introduction" (Elhage L98) and "§ Residual Stream Bandwidth" are short forms of real headings.
- **Referents and turns.** Olah L232 "this" (understandable features), L242 with "have led us to believe", L259 "this" (features as neurons; both halves kept), L223 (a hope, not a concession), L510 condition, Nanda L1365 (zero ablation), L287 ("as an intuition"), Elhage L158 (idealised), L170 ("hypothetical" 50-layer example not used as a measurement). No quote is cut before its turn; the L172 quote ends before "clearing residual stream dimensions …", which only elaborates.
- **Reporting verbs.** offered, believe, concede (L232), suspect (L587), imagine (L604), plan (L490), suppose (L636-637), propose (L633), assert (Elhage L158), argues (Nanda L280, "almost" kept), describes (Nanda L1587, "likely" kept), defines (superposition, RLHF). The sort in `box-firmness` follows the brief's firmness groups.
- **Must-not-use list.** Items 1-15 checked: none used. In particular L259 is quoted whole; no skip-connection tension; no L216; no "not necessarily a unit vector"; the unit-vector convention is labelled "our convention; the sources give none"; steering, activation addition and hidden state are reported as absent (grep over the three .txt files: 0 hits); no Shannon comparison; "like an edge weight (ours)", not an Olah edge. Elhage citations stay inside the allowed sections.
- **Balance.** Olah's strongest unhedged lines (claim boxes, L273, L634) sit next to "deliberately speculative", "divided", "anecdotal". Nanda's flat lines (L135, L1096) are quoted next to his hypothesis wording. Elhage's flat sum and the hedged "hints" are both present (V2B-13 and V2B-07 note small gaps).
- **MacKay.** Exercise 15.18, p. 237: "with two sets of inputs and one output", "equal to the arithmetic sum of the two inputs, that's 0, 1 or 2", "it could be that the input state was (0, 1) or (1, 0)", "cannot hear the output of the channel" are verbatim; "no noise" kept; the disanalogies are stated; no capacity claim; the link is labelled "structural analogy (ours)".
- **Toy numbers, recomputed in Python.** The running sum (1,2)→(3,1)→(2,2)→(5,0)→(4,2); shares 5, 0, 1, −1 (sum 5, direct 5); the r = (0,1) edge case 2, −1, 1, −2; the "along a₂" preset 15; the cloud, u = (−0.707, 0.707), ±1.414; margins −4.000, −2.828, 0.000, 2.000, 2.828 at 0°, 45°, 90°, 120°, 135° under the post's definition; the blind-probe scores 2.828, 4.243, 5.657; push v = (−2, 2) moving scores by 2.828 (−1.414→1.414, 1.414→4.243); the sideways push 0; the 90° rotation ((5,0)→(0,5), r→(−2,1), writers (−2,1), (1,2), (−1,−1), (2,3), shares unchanged) and the 45° and 180° presets; the norm table (mean 3 and 6, sd 1 and 2, both (1,−1), r· = −1, r·stream 8 and 16); the logit-lens toy rows (1.000, 1.232, −2.232 / 2.000, 0.732, −2.732 / 4.000, −0.268, −3.732) and the flip from token 2 to token 1 after block 1; the three-feature reads (1, −0.5, −0.5; all three on gives 0; (0.5, 0.5, 0.5) also gives silence, so the "find another silent setting" challenge has an answer); E1-E5 solutions; M(1,0) = (2,1), M(1,1) = (3,3), M(1,−1) = (1,−1); the rotation formulas in the `rotate` config.
- **check.mjs.** 8/8 widget configs parse; default readouts (shares 5, 0, 1, −1; margin −4.000 at 0°; rotate 5, 0, 1, −1; three-features 1, −0.5, −0.5) match the text.
- **Notebook numbers** against results.md and the saved cell outputs: 768, 12 blocks, 2,048 (Qwen3 config); 0.0 for the in-order sums and the explanation (rows 2-8); 1.03e-6 and epsilon 1.19e-7 (row 7; output 1.027e-06, 1.192e-07); 7.8e-7 (row 23); 6.2e-6 (row 43; output 6.219e-06); 0.0 and 0.986 for the last entry (rows 44-45); tiny Qwen3 1.1e-7 and Gemma 3 8.6e-8 (row 62); Gemma 3 hooks 9.7 and 0.0 (rows 58-60); 7.211561 twice and 13 shares (row 49); steering residual 0 for α = 0.5, 1, 2, 5, −3 (row 50); cosine 0.1318 and 1.0935 (row 53); 834.6, ranks 2025 … 0 and 12 (rows 14, 17, 20); norms 5.3, 472.4, 10.3, 3155.5, 417.4 and ratios 11.03 (rows 9-11); 1.09e-6 (row 27); environment versions. Library line numbers (HF output_capturing 243-246, Qwen3 49, 62-63, 296-314, Gemma 3 105-116, 397-416, 485, Llama 294-312, Mistral 220-238) were read in the installed transformers 5.19.0 and match.
- **Text against audio.** The 12 audio chapters match the 12 `data-ch` sections in order. Numbers, formulas, the margin table, norms and notebook figures in the audio equal the page. Fold-outs are only mentioned. The "Welcome to AI4Read from CSS Lab" intro is present. Differences are listed in V2B-13 to V2B-17.
- **Standalone.** No reference to another post, series or person's earlier work in the text or audio (searched: "post 0/N", "previous/earlier/last post", "as before", "remember", "village", "Harari", "series"). "Post 03" and "post three" name this post. "Questions marked ↻ will come back in later posts" names none. Every toy (calm/urgent cloud, writers, three features, M matrix) is re-introduced inside the post.
- **Steering and fine-tuning.** No sentence claims that adding a vector changes behaviour, or that fine-tuning or RLHF change the stream; both are stated as absent from the sources. The notebook result is called arithmetic.
- **Not checked.** The pedagogy and English-level criteria, cite-map completeness, the word count, and english.json beyond the V1-20 and V1-21 spot-check.
