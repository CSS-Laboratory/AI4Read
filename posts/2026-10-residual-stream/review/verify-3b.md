---
name: post03-verify-3b
stage: S5, round 3 (final), second fact-checker
checker: independent fact-checker (fresh agent; did not write the post; worked in parallel with the other round-3 checker)
date: 2026-10-25
checked: src/content.html (text, 8 widget configs, 3 fold-outs, recall, sources) and audio-script.md
evidence: source-brief.verified.md (the UNVERIFIED unit-12 note was re-checked against the source, not counted as evidence); sources/*.txt incl. mackay-2003-mac.txt; notebook/results.md; saved cell outputs of notebook/01 and 02 (.ipynb); the notebook code; installed transformers 5.19.0 source; a rerun of the GPT-2 additivity test (cached gpt2, offline); check.mjs (default state and 14 presets)
not read: self-review.md, numbers.md
line refs: C = src/content.html line; A = audio-script.md line; "Olah/Elhage/Nanda L" = line of the saved .txt
---

# S5 verify, round 3 (second checker): post 03

## Counts

| Critical | Major | Minor |
|---|---|---|
| 0 | 1 | 11 |

Round 2: of the 34 findings in verify-2 and verify-2b, 30 are resolved, 2 are moot (sentence deleted) and 2 are partly resolved (V2-04 and V2B-09, the same finding seen by both checkers; the fix put a wrong cite on the quote, see V3B-02). All three round-2 majors (V2-01, V2B-01 and the English loop) are resolved.

---

## Major

### V3B-01 · major · The headline "6.2e-6" is not "relative to the size of the stream"; the denominator is the block's own writes
- **Where.** C:156 "they differed by at most 6.2e−6, relative to the size of the stream"; C:166 "*Relative* means the difference divided by the size of the stream"; C:170 (identity-test row, "6.2e−6 relative"); C:174 ("the table row alone differs by 3.63 relative"); C:510 (recall card 1); A:56 ("relative to the size of the stream"). The same number is in C:394 and A:212 without the denominator.
- **Evidence.** Notebook 02 cell [9] computes `err(hs[L+1] - hs[L], a + m)`, and `err(a, b)` divides by `‖b‖`. So b is the sum of the block's two writes `a + m`, not the stream. The `err` docstring says "relative to the stream's norm", which is wrong for this call. I reran the test on the cached GPT-2 (same prompt, float32, CPU, eager):
  - 6.22e-06 against the writes (block 9, as in results.md row 43);
  - against the stream after the block, 4e-08 to 6e-08 for blocks 1 to 11, and at most 6.95e-07 against the stream before the block (block 1, where the stream is still small);
  - the 3.63 is `‖hs[0] − wte(ids)‖ / ‖wte(ids)‖`, i.e. relative to the table rows. Against `hs[0]` itself it is 0.975.
  Rows 1, 2 and 4 of the table (1.03e-6, 7.8e-7, 0.986) do divide by the stream, so the fold-out mixes two denominators under one definition.
- **Problem.** The statistic the post builds its identity claim on is described with a wrong denominator in five places. The conclusion ("that is rounding") is safe, and the error is conservative (the agreement against the stream is 10 to 100 times tighter), but the sentence as written is false, and a reader who recomputes it from the stream gets a different number.
- **Fix.** C:156 and A:56: "…by at most 6.2e−6, relative to the size of the block's own two writes at that position." C:166: define *relative* per row ("divided by the size of the second thing in the comparison"), or add "(for the identity-test row: the block's two writes; for the 3.63 row: the table row)". Optionally add the stream-relative figure from a rerun of the notebook cell. Fix the notebook docstring too.

---

## Minor

### Citations and attribution
- **V3B-02 · The L633 quote is now cited to the wrong section (V2-04 / V2B-09 fix applied as a swap).** C:218 (`box-firmness`, "Proposes and plans"): the quote "if you understand a circuit, you should be able to predict what will change if you edit the weights" is Olah L633, § Interpretability as a Natural Science. Only "the test itself is future work" is § Circuit 2 (L490). The line now carries the single cite "Olah 2020, § Circuit 2". Fix: two cites, one after the quote (Natural Science) and one after "future work" (Circuit 2).
- **V3B-03 · "call it 'a communication channel'" drops "generally think of".** C:162 (trap box): "Elhage and colleagues call it “a communication channel”". Elhage L155: "We generally think of the residual stream as a communication channel, since it doesn't do any processing itself". Fix: "Elhage and colleagues say they generally think of it as “a communication channel”".
- **V3B-04 · "would not be fatal" drops "completely".** C:516 (recall card 7: "would not be fatal to circuits research if false") and A:85 / A:236 ("not fatal if false"). Olah L602: "it wouldn't be completely fatal to circuits research if this claim turned out to be false". The main text (C:197) quotes it right. Fix: "would not be completely fatal" in the card and the two audio lines.
- **V3B-05 · A circuit concession loses its scope.** C:219 (`box-firmness`, Claim 2, "Concedes"): "although there are many smaller weights we don’t understand the role of". Olah L320 is about the curve-detector circuit ("We also don't see anything suggestive of a second alternative cause of firing, although there are many smaller weights we don't understand the role of"). Cited correctly as § Claim 1, Argument 5, but the bullet reads as a general concession about circuits. Fix: "Concedes, of the curve circuit: …".
- **V3B-06 · TCAV is not an intervention.** C:403: "Testing use takes interventions, which this post does not run. Nanda’s glossary lists some: ablation … and activation patching …, and TCAV". Nanda L1593-1598: TCAV trains a probe-like Concept Activation Vector and compares it with the derivative of the output (a gradient, no intervention). Ablation (L1361) and patching (L1442) are interventions. Fix: "Testing use takes tests of this kind, which this post does not run" (A:149 likewise), or "…lists some interventions (ablation, activation patching) and one gradient-based test, TCAV, …". The UNVERIFIED unit-12 note itself is correct: I re-read L1361-1375, L1442, L1593-1598; none is applied to a probe direction in a language model.

### Scope and wording
- **V3B-07 · "TransformerLens gives the Hugging Face stream minus its mean coordinate" is a GPT-2 result stated generally.** C:459, item (2). results.md row 27 is GPT-2 (a LayerNorm model); library fact L6 says that for RMSNorm models (Qwen3, Llama) writing weights are not centred, so the statement would be wrong there. Fix: "For GPT-2, in its compatibility mode, TransformerLens gives …".
- **V3B-08 · "that TransformerLens normally applies" conflicts with the pinned version.** C:166: *Raw weights* means "the published weights, without the rewriting of the weights that TransformerLens normally applies". results.md T6 and L1/L2: in TransformerLens 4.3.0 (the version cited in Sources) the default loader does not rewrite weights; only `enable_compatibility_mode()` does. Fix: "…without the rewriting that TransformerLens's compatibility mode applies".
- **V3B-09 · "every part of the model changes it by adding to it".** C:72. The unembedding and the norms only read the stream, and the post says so itself (diagram step 6). Fix: "every attention and MLP part changes it by adding to it".
- **V3B-10 · The absence claim about "Mistral" meets one hit.** C:200 and A:83: "none of the three says anything about … Mistral". Nanda L1676: "Trained during the development of their Mistral library" (the Stanford training library, not Mistral AI's models). The claim about the models is true. Fix: "Mistral models" (or "Mistral AI's models").
- **V3B-11 · ReLU is used before it is defined.** C:355: "in the standard basis a ReLU acts on each coordinate independently" (quote) after "an activation function (a curve applied to each number on its own)". "ReLU" is never glossed (WRITING §3). Fix: "a ReLU (an activation function that turns every negative number into 0)".

### Text against audio
- **V3B-12 · Audio ambiguity.** A:46: "undoes the minus two that attention wrote". The page (C:90, C:122) says "that attention 2 wrote"; attention 1 wrote −1 in the second place, so the audio is ambiguous. Fix: "that attention two wrote". Also A:138 drops "and tiny random models" from "in code and tiny random models, Gemma 3 norms each sub-layer’s output" (C:392); the claim is still true, but the page's evidence base is narrower than the audio's.

(V3B-12 counts as one finding. Total minor: V3B-02 to V3B-12 = 11.)

---

## Round-2 findings: resolved or not

Checked against the current files, not against response-2.md.

| ID | Status | Evidence |
|---|---|---|
| V2-01 (major) | Resolved | english.json loop: "The claim that concepts are directions in a language model’s stream hinges on evidence the sources do not supply"; the "firm ground" item is scoped the same way. |
| V2-02 | Resolved | C:197 and C:225: "further work will be needed” to understand if “the apparent universality of some low-level vision features is the exception or the rule”"; A:81 has the full object. |
| V2-03 | Moot | The cars-and-dogs sentence is gone from C and A (grep: 0 hits). |
| V2-04 | Partly | "Circuit 2" cite is on the line, but the quote is now under the wrong section: V3B-02. |
| V2-05 | Resolved | C:134, A:50 "the account Elhage and colleagues give, which says: “We also ignore layer normalization.”" |
| V2-06 | Resolved | C:134 and A:50 add the learned scale and shift; "before that last step the list always has the same overall size". |
| V2-07 | Resolved | C:71 cites § Transformer Components, Positional information (Nanda L671); C:137 cites § Transformer Basics (L601) and § Decoder-only (L831). |
| V2-08 | Resolved | A:58 names "a TransformerLens comparison made with raw weights"; C:171 "(raw weights)". |
| V2-09 | Resolved | A:83 "They promise a forthcoming paper on larger ones, which is not among our sources." |
| V2-10 | Resolved | A:164 "it could be that the input state was zero, one or one, zero". |
| V2-11 | Resolved | A:98 "write of hints, which they word with may". |
| V2-12 | Resolved | A:52 "no single hidden state of a sentence … That is ours." |
| V2-13 | Resolved | No "four times" sentence in the audio (grep: 0 hits). |
| V2-14 | Resolved | A:25 "Option two: the word's starting list plus every addition made so far." |
| V2-15 | Resolved | english.json loop: "the division inside the norm in front of it is the part that is not linear". |
| V2-16 | Resolved | "affect vs effect": "…unless it is at right angles to u". |
| V2-17 | Resolved | "to bear out": "…for entries 0 to 11". |
| V2B-01 (major) | Resolved | C:403 and A:149 list ablation, activation patching and TCAV from Nanda and no longer say the sources do not address use. One wording leftover (TCAV is not an intervention): V3B-06. |
| V2B-02 | Resolved | C:155 "returns the list after each block as hidden_states. None of the three sources uses the phrase “hidden state”" (grep 0 hits in all four .txt). |
| V2B-03 | Resolved | C:71 "starting list, position list included"; C:174 table row alone 3.63 (see V3B-01 on the denominator); C:392 "the token’s table row plus its position list". |
| V2B-04 | Resolved | As V2-07. |
| V2B-05 | Resolved | As V2-02. |
| V2B-06 | Moot | The "major reason" paragraph is gone (grep: 0 hits). |
| V2B-07 | Resolved | C:355 and C:406: Nanda's "always slightly privileged" and "spectrum". |
| V2B-08 | Resolved | C:211: "gives an intuition (ours: an argument, not a measurement)" and "an extremely natural way to represent things" (Nanda L200). |
| V2B-09 | Partly | As V2-04 / V3B-02. |
| V2B-10 | Resolved | "adder" gone (grep: 0 hits); C:413 "MacKay’s binary multiple access channel, whose output is the sum of two inputs (the link is ours)". |
| V2B-11 | Resolved | C:134 "GPT-2 uses this version" cites Notebook 02 (row 35); C:498 "(ours)". |
| V2B-12 | Resolved | C:459 (3) states the better-of-two-orientations margin. Notebook unchanged. |
| V2B-13 | Resolved | As V2-11. |
| V2B-14 | Resolved | As V2-10. |
| V2B-15 | Resolved | As V2-08. |
| V2B-16 | Resolved | As V2-13. |
| V2B-17 | Resolved | A:25, A:29, A:33 follow the page options; A:52 as V2-12. |

---

## Checked and found correct

- **Quotations.** All 121 curly-quoted strings in content.html outside the widget configs were extracted by script and matched against the four .txt files (NFKC, case-folded, letters and digits only, split at ellipses). Every source quote matches; the 13 non-matches are our own labels ("first plus first, second plus second", "like an edge weight", "dimension 17", "push along", etc.). None is over 25 words. None comes from the hidden Olah lines (L147-148, L249-254, L265, L267, L287, L455, L658) or Elhage L303. Each cite was mapped to the `##` heading of its quote line by script; all agree except V3B-02 (and the short forms "§ Post-LayerNorm", "§ Logit lens", "§ Ablation", which name an entry, not a section; harmless).
- **Referents and turns.** Olah L232 (understandable features), L242 ("have led us to believe" kept; the ellipsis skips only a parenthesis), L259 (both halves of the sentence), L587 (through its turn, with its object), L604 ("could imagine"), L490 (a plan). Elhage L142, L155, L158 (idealised stream; "up to a constant scalar"), L172 ("hints", "may"). Nanda L200 (intuition and "extremely natural"), L1365, L287 ("Intuitively"), L1587 ("likely"), L1425-1428.
- **Reporting verbs.** asserts, believe, concede, suspect, imagine, plan, suppose, propose, argues, describes, defines: each follows the source's firmness. Nanda's unhedged lines (L135, L1096) are quoted next to his hypothesis wording and flagged as unhedged. Olah's strongest unhedged lines (claim boxes, L273, L634) sit next to "deliberately speculative", "divided", "anecdotal". The Elhage sum is quoted flat and the cancellation line keeps "hints … may".
- **Absence claims re-grepped over the three sources plus MacKay.** "steer", "hidden state", "hidden_state", "post-training", "instruct", "Qwen", "Llama", "Gemma", "refusal", "activation addition": 0 hits. "fine-tun" and "RLHF" only in Nanda's training entries (L478, L905-908, L1727); nothing on their effect inside a model. "Mistral": V3B-10.
- **Toy numbers, recomputed in Python.** Running sum (3,1), (2,2), (5,0), (4,2); shares 5, 0, 1, −1 (sum 5 = direct); the r = (0,1) edge case 2, −1, 1, −2; "along a₂" r = (3,−2) gives 15 (widest share at r = (3,−3) is 15, so `bars.max` = 15 holds); the answer r = (2,−1) is silent for the embedding; margins −4.000, −2.828, 0.000, 2.000, 2.828 at 0°, 45°, 90°, 120°, 135° (135° is the maximum over 0° to 180°); u = (−0.707, 0.707) and ±1.414; blind-probe scores 2.828, 4.243, 5.657; the perpendicular-foot check (score 3, foot (1.8, 2.4), (3.2, −2.4), dot 0); push v = (−2, 2) moving every score by 2.828 and calm landing on the urgent start points; sideways push 0; the 90° rotation ((5,0)→(0,5), r→(−2,1), shares unchanged, writers (−2,1), (1,2), (−1,−1), (2,3)); the norm table (means 3 and 6, SD 1 and 2, both (1,−1), r· = −1, r·stream 8 and 16); the logit-lens toy rows and the flip from token 2 to token 1 after block 1; the three-feature reads (1, −0.5, −0.5; all three on and (0.5, 0.5, 0.5) give silence; features 1 and 2 give 0.5, 0.5, −1); E1 to E5 solutions; M(1,0) = (2,1), M(1,1) = (3,3), M(1,−1) = (1,−1); the `three-arrows` node coordinates (95 units, 0°/120°/240°).
- **check.mjs.** 8/8 configs parse. Default readouts match the text (shares 5, 0, 1, −1; margin −4.000 at 0°; rotation 5, 0, 1, −1; reads 1, −0.5, −0.5). I also ran 14 presets or edge states with `--values` (probe 0°, 45°, 90°, 120°, 135°, 180°, push along, push sideways; rotations 45° and 90°; read-split (0,1), (3,−2), (2,−1); three-features all on and features 1 and 2): all match the text and captions.
- **Notebook numbers** against results.md and the saved cell outputs: 768 and 12 blocks; 2,048 (Qwen3 config, cell [13], config only); 0.0 for the in-order sums (rows 2-8); 1.03e-6 and epsilon 1.19e-7 (row 7; output 1.027e-06); 7.8e-7 (row 23); 6.2e-6 (row 43; output 6.219e-06; the denominator is V3B-01); 0.0 and 0.986 for the last entry (rows 44-45); 3.63 and 0.0 for entry 0 (rows 36-37); tiny Qwen3 1.1e-7 and Gemma 3 8.6e-8 (row 62); Gemma 3 guessed hooks 9.7 and norm hooks 0.0 (rows 58-60); 7.211561 twice and 13 shares (row 49); steering residual 0 for α = 0.5, 1, 2, 5, −3 (row 50); cosine 0.1318 and 1.0935 (row 53); 834.6 and the ranks of " it" (rows 14, 17, 20: rank 0 after 8, 1 after 9, 0 after 10 to 12; 12 without the norm); norms 5.3 and 472.4, BOS ratio 0.88 after 12 (rows 9-11); 1.09e-6 (row 27). I reran the GPT-2 additivity test myself: per-block numbers equal the saved output.
- **Library lines** in transformers 5.19.0 (output_capturing 243-246; Qwen3 49, 62-63, 296-314; Gemma 3 105-116, 397-416, 485; Llama 294-312; Mistral 220-238) were read and match the claims.
- **MacKay.** Exercise 15.18, p. 237: "two sets of inputs and one output", "arithmetic sum of the two inputs, that's 0, 1 or 2", "There is no noise", "it could be that the input state was (0, 1) or (1, 0)", "cannot hear the output of the channel" are verbatim; the figure caption (p. 238) gives "binary multiple access channel … output equal to the sum of two inputs". No rate or capacity claim; the link is labelled a structural analogy (ours) with its disanalogies.
- **Text against audio.** The 12 chapter ids match the 12 `data-ch` sections in order. Numbers, formulas, the margin table, the norm and notebook figures in the audio equal the page. Fold-outs are only mentioned. "Welcome to AI4Read from CSS Lab" is in chapter 1. Every passage changed in round 2 was compared line by line (hook, guess, sum, bets, rw, dir, answer, both lenses, turn, work, recall); the differences are V3B-01 (audio side), V3B-04 (audio side) and V3B-12.
- **Stands alone.** No reference to another post, series, person's earlier work or earlier session (searched "post 0/N", "previous/earlier/last post", "as before", "remember", "village", "Harari", "series", "Discipline"). "Post 03" and "post three" name this post; "Questions marked ↻ will come back in later posts" names none. Every toy (running sum, calm/urgent cloud, three features, M matrix) is re-introduced inside the post. Section cross-references (sections 3, 4, 5, 6, 8) point to the right sections.
- **Steering and fine-tuning.** No sentence claims that adding a vector changes behaviour, or that fine-tuning or RLHF changes the stream; both are stated as absent from the sources. The notebook steering result is called arithmetic.
- **Not checked.** Pedagogy and English-level criteria, cite-map completeness, the word count, and english.json beyond the round-2 items and the loop paragraph. One loose wording there, not counted: the loop says a steering push "moves every score in lockstep", which is true for a push along u but not for the sideways push the post itself describes (the "affect vs effect" item already has the qualifier).
