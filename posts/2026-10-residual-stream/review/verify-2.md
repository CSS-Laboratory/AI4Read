---
name: post03-verify-2
stage: S5, round 2
checker: independent fact-checker (fresh agent; did not write the post or the round-1 reports)
date: 2026-10-25
checked: src/content.html (text, 8 widget configs, 3 fold-outs, recall, sources), audio-script.md, english/english.json
evidence: source-brief.verified.md (units 1-15, writer-must-not-use list); sources/*.txt (line numbers = file lines, as in the brief); sources/mackay-2003-mac.txt; Olah HTML with comments stripped (hidden-line check); notebook/results.md (authority for every notebook claim) plus spot checks of the saved .ipynb outputs; check.mjs (default state and every preset)
independence: self-review.md and numbers.md not read; response-1.md read only after the own pass
---

# S5 verify, round 2: post 03

Severity follows rubric §A. `C:` = line of `src/content.html`, `A:` = line of `audio-script.md`, `E:` = item in `english/english.json`. Source lines are lines of the saved `.txt` files.

## Critical

None.

## Major

### V2-01 · major · English loop: "evidence the sources do not supply" drops the scope (language-model stream)
- **Where.** E: loop text: "The claim that concepts are directions hinges on evidence the sources do not supply, so we are on firmer ground with the arithmetic than with the interpretation."
- **Evidence.** Olah L242: "thousands of hours of studying individual neurons have led us to believe the typical case is that neurons … are understandable"; L273: "Curve detecting neurons can be found in every non-trivial vision model we’ve carefully examined"; seven arguments for curve detectors (L293 ff.). Nanda L259: "a decent amount of empirical evidence that this is mostly true of Inceptionv1". The post itself is scoped: C:190 "For the stream of a language model, none of the three sources tests whether concepts are directions"; C:395 "For the trained language models people use now, the three sources give no test".
- **Problem.** As written, the sentence says the sources give no evidence at all. They do, for vision networks. Same kind of error as round-1 V1-01 (scope dropped, so the claim becomes false), and it makes Olah look as though he offered none (balance rule). WRITING §8 applies §9 to the pack.
- **Fix.** "The claim that concepts are directions in a language model's stream hinges on evidence the sources do not supply …"

## Minor

### V2-02 · minor · universality: the referent of "the exception or the rule" is widened
- **Where.** C:198: "further work will be needed” to tell whether it “is the exception or the rule”". Here "it" reads as "the universality hypothesis". A:85 stops at "further work will be needed." and drops the object.
- **Evidence.** Olah L587: "further work will be needed to understand if the apparent universality of some low-level vision features is the exception or the rule". The fold-out (C:225) is closer ("the apparent universality") but also drops "of some low-level vision features".
- **Fix.** "… to tell whether “the apparent universality of some low-level vision features is the exception or the rule”", on the page, in the fold-out, and in the audio.

### V2-03 · minor · cars and dogs: the belief and the condition are attached to the wrong clause (new text from the V1B-m7 fix)
- **Where.** C:417 and A:168: "Olah and colleagues say they believe that cars and dogs can share a neuron “As long as cars and dogs don’t co-occur”".
- **Evidence.** Olah L510: "We believe superposition allows the model to use fewer neurons, conserving them for more important tasks. As long as cars and dogs don’t co-occur, the model can accurately retrieve the dog feature in a later layer". The sharing itself is observed (L506: "the model had a “pure neuron” and then mixed it up with other features"). "Believe" governs the fewer-neurons sentence; the condition governs accurate retrieval in a later layer, not sharing.
- **Fix.** "Olah and colleagues observe car and dog features sharing neurons, believe this lets the model use fewer neurons, and add that “As long as cars and dogs don’t co-occur”, the dog feature can still be retrieved in a later layer."

### V2-04 · minor · fold-out: "the test itself is future work" cited to the wrong section
- **Where.** C:219, `#box-firmness`, "Proposes and plans": "…edit the weights”; the test itself is future work" with one cite, § Interpretability as a Natural Science.
- **Evidence.** L633 (Natural Science) gives the standard only. The plan is L490, § Circuit 2: "we plan to return to it in a future article … including testing our theory of the circuit by editing the weights". The main text (C:194) cites § Circuit 2 correctly.
- **Fix.** Add the cite "Olah 2020, § Circuit 2" after "future work".

### V2-05 · minor · Elhage: the analysis ignores layer norm, not the models
- **Where.** C:135: "It is exact in Elhage and colleagues’ toy models, which “ignore layer normalization”". A:50 the same.
- **Evidence.** Elhage L142 (§ Model Simplifications): "We also ignore layer normalization." It is a simplification of the analysis. Elhage L1015 (appendix, cited here only as evidence): "Our transformer models apply layer normalization every time they read off from the residual stream." The brief (unit 9, tensions) records the same point.
- **Fix.** "It is exact in Elhage and colleagues’ analysis, which “ignore[s] layer normalization”", or "… in their simplified account, which ignores layer normalization".

### V2-06 · minor · new norm definition: "always ends up the same overall size" and "This is GPT-2's version" omit the learned scale and shift
- **Where.** C:135 (new in revision): "It subtracts the average … and divides by … the standard deviation, so the list always ends up the same overall size … This is GPT-2’s version". A:50.
- **Evidence.** Nanda L686-693: four steps, the last two "scale" and "translate (adds on a learned bias vector)"; L700: "2*d_model learned parameters per LayerNorm layer". The fold-out (C:362-363) gives the four steps and sets scale and translate "at identity" for the toy. GPT-2's ln_1/ln_2/ln_f have these learned parameters, so the output size is not fixed.
- **Fix.** "… so, before a learned scale and shift, the list always has the same overall size … GPT-2's version adds that learned scale and shift (fold-out in section 6)."

### V2-07 · minor · two clauses in section 3 are cited to a section that does not contain them
- **Where.** (a) C:71: "GPT-2 also adds a learned list for the token’s position" cited § Transformer Basics. (b) C:138: "Only attention carries information between positions, and in a decoder-only model … only from earlier ones" cited only § Decoder-only.
- **Evidence.** (a) Transformer Basics L586 says "plus the positional embedding" but not "learned"; "learned, absolute positional embeddings" is L671, § Transformer Components. (b) "Attention layers are the only layers that can move information between token positions" is L601, § Transformer Basics; L831 (Decoder-only) supports only the "earlier ones" half.
- **Fix.** (a) Cite "Nanda 2022, § Transformer Components, Positional information". (b) Add "Nanda 2022, § Transformer Basics" after the first clause.

### V2-08 · minor · audio: TransformerLens "raw weights" still missing (V1B-m18 left in the audio)
- **Where.** A:56: "The TransformerLens stream agreed with the Hugging Face list within seven point eight times ten to the minus seven, relative." A:183 later says TransformerLens in compatibility mode gives "the Hugging Face stream minus its mean coordinate".
- **Evidence.** results.md row 23 (raw, 7.8e−7) versus row 26 (processed, 2.5e−2 to 4.3e−2). The page row now says "TransformerLens (raw weights)" (C:161).
- **Fix.** "The TransformerLens stream, with raw weights, agreed …".

### V2-09 · minor · audio: Elhage scope sentence still ends before the turn (V1-07 left in the audio)
- **Where.** A:87: "Elhage and colleagues study attention-only transformers of two layers or fewer, and do not apply their insights to larger models there."
- **Evidence.** Elhage L102 continues "but in a forthcoming paper, we will show that … continues to be at least partially relevant for much larger and more realistic models". The page (C:201) now adds "(they promise a forthcoming paper, not among our sources)".
- **Fix.** Add "They promise a forthcoming paper on larger models, which is not among our sources."

### V2-10 · minor · audio: MacKay line unchanged, although response-1 says it was changed (V1B-m14)
- **Where.** A:170: "If the output is one, the input state was zero, one or one, zero".
- **Evidence.** MacKay p. 237: "it could be that the input state was (0, 1) or (1, 0)". response-1 (V1B-m14): "Audio MacKay line says “it could be that the input state was …”"; the script does not.
- **Fix.** "If the output is one, it could be that the input state was zero, one or one, zero …". (The disjunction is not wrong; the fix is for wording fidelity and to make the response true.)

### V2-11 · minor · audio: "write only of hints" kept, although response-1 says "only" was removed (V1B-m5)
- **Where.** A:102: "Elhage and colleagues write only of hints". The page (C:269) now reads "write of hints".
- **Evidence.** Elhage L172 (hedged throughout: "hints", "may", "may indicate"). I judge "only of hints" accurate for deletion itself, but the page and the audio now differ and the response misreports the change.
- **Fix.** Match the page: "Elhage and colleagues write of hints …".

### V2-12 · minor · audio: "no hidden state of a sentence" loses its label and its qualifier
- **Where.** A:52: "So there is no hidden state of a sentence."
- **Evidence.** The page (C:153): "So there is no “hidden state of a sentence”; a summary of a sentence is a further step that someone must choose (ours)." Nanda L598-601 support one stream per position; no source says anything about sentence summaries (brief unit 10, trap).
- **Fix.** "So there is no single hidden state of a sentence. A summary of a sentence is a further step someone must choose; that is ours."

### V2-13 · minor · audio carries a source claim that the page does not
- **Where.** A:168: "Elhage and colleagues note that a single MLP layer typically has four times more neurons than the residual stream has dimensions."
- **Evidence.** The statement is verbatim-faithful (Elhage L170, in scope, § Subspaces and Residual Stream Bandwidth), but it is not on the page, so no on-page citation backs it and the render test (rubric C) cannot pair it with the text.
- **Fix.** Add it to the `#lens-info` paragraph with "Elhage 2021, § Residual Stream Bandwidth", or drop it from the audio.

### V2-14 · minor · audio: quiz option for question 1 differs from the page and names the answer
- **Where.** A:25: "Option two: a running total, the word's starting list plus every addition made so far." The page (C:50) reads "The word’s starting list plus every addition made so far"; the revealed answer is headed "A running total" (C:173).
- **Evidence.** WRITING §5 (the right option must not be the longest or most specific). Not a source error; a page/audio mismatch.
- **Fix.** Drop "a running total," from the audio option.

### V2-15 · minor · English loop: "the norm … is the part that is not linear"
- **Where.** E: loop: "a read is then a dot product with that sum, and the norm in front of it is the part that is not linear."
- **Evidence.** Nanda L702: "the “divide by the standard deviation” step is non-linear (but the other 3 are linear)". The pack's own item for "to a first approximation" and the post (C:274) say "the division inside the norm".
- **Fix.** "… and the division inside the norm in front of it is the part that is not linear."

### V2-16 · minor · English fix item "affect vs effect": the example is false for a sideways push
- **Where.** E: "affect vs effect": "Adding a vector affects every score; the effect is the same shift, u dot v, for each point."
- **Evidence.** The post (C:331): a push at right angles to u "has u·v = 0: every point moves and no score moves".
- **Fix.** "Adding a vector along u affects every score; the effect is the same shift, u dot v, for each point." Change the "wrong" and "right" lines to match.

### V2-17 · minor · English "to bear out": the identity is stated without its index limit
- **Where.** E: "to bear out": "The notebook bears out the identity in GPT-2 small: the writes add up to the stream within rounding error."
- **Evidence.** C:165 and C:170: equal "for entries 0 to 11"; the last entry is final-normed (results.md rows 42, 44-45). Round-1 V1-15 was the same omission in the term box.
- **Fix.** "The notebook bears out the identity in GPT-2 small for entries 0 to 11: …".

## Round-1 findings: resolved / not resolved

Checked against the current files, not against response-1.md.

| Round-1 ID | Status | Note |
|---|---|---|
| V1-01 | resolved | C:395 and A:146 scoped to "trained language models people use now", with the Elhage two-layer mention. |
| V1-02 | resolved | C:394, C:497, A:144, A:203, E "rest on the assumption": "each model's own dot products"; cross-model dot product excluded (C:497). |
| V1-03 | resolved | C:264 and A:100: "agree to all printed digits … 0.0 in this run", no reason claimed. |
| V1-04 | resolved | Recall 8 replaced by the margin card (C:517, A:242). |
| V1-05 | resolved | C:194: three worked circuits named. |
| V1-06 | resolved | No "but" join; L587 quoted through its turn. New referent issue: V2-02. |
| V1-07 | partly | Page resolved (C:201). Audio not: V2-09. |
| V1-08 | resolved | C:356 cites Nanda for "acts on each coordinate independently"; activation function glossed. |
| V1-09 | resolved | C:501 § Training. |
| V1-10 | resolved | C:156 "The Hugging Face library". |
| V1-11 | resolved | "Independent record" gone; 6.2e−6 row in the table (C:162). |
| V1-12 | resolved | C:459 "far larger after two or more blocks … but 417.4 after 12". |
| V1-13 | resolved | C:376 "normally applies". |
| V1-14 | resolved | C:405, A:155 "will try to pull apart". |
| V1-15 | resolved | C:170 "for entries 0 to 11". |
| V1-16 | resolved | C:395 "vision networks, mostly InceptionV1". |
| V1-17 | resolved | Cites added (C:218-219). Second half of the "Proposes" bullet still needs § Circuit 2: V2-04. |
| V1-18 | resolved | Elhage URL (C:528); "Notebook 01, reference run" on 1.09e−6 (C:459). |
| V1-19 | resolved | A:10 "GPT-2 small"; A:12 label kept; Inceptionv1 line no longer in the audio. |
| V1-20 | resolved | Item sentence now hedges the norm, not the sum. Loop wording: V2-15. |
| V1-21 | resolved | Loop "may not simply carry over … which we did not run"; "with the hooks placed correctly". |
| V1B-M1 | resolved | As V1-05; short answer "vision networks". |
| V1B-M2 | resolved | As V1-06 (page and audio). |
| V1B-M3 | resolved | As V1-01. |
| V1B-m1 | resolved | C:185, A:71 "features connect through weights into circuits". |
| V1B-m2 | resolved | C:217 condition added. |
| V1B-m3 | resolved | C:211 "Hedges". |
| V1B-m4 | resolved | C:190, C:210 referent quoted. |
| V1B-m5 | partly | Page resolved (C:269). Audio keeps "only" (A:102), contrary to response-1: V2-11. |
| V1B-m6 | resolved | As V1-14. |
| V1B-m7 | partly | "Believe" added as asked, but the new wording attaches the belief and the condition to the wrong clause: V2-03. |
| V1B-m8 | resolved | As V1-13. |
| V1B-m9 | resolved | C:201 Nanda continuation added; "probably false" left out (optional). |
| V1B-m10 | resolved | C:325 "In Nanda’s description you train a linear map …". |
| V1B-m11 | resolved | As V1-08. |
| V1B-m12 | resolved | C:208 § Example 1: Curve Detectors; C:501 § Training. |
| V1B-m13 | resolved | Line removed from the audio. |
| V1B-m14 | not resolved | A:170 unchanged, though response-1 says it was changed: V2-10. |
| V1B-m15 | resolved | As V1-02. |
| V1B-m16 | resolved | C:268 "net +2" (recomputed: a₂+f₂ = (2, 0)). |
| V1B-m17 | resolved | C:159-162 table carries 6.2e−6 and names "after 12 blocks". |
| V1B-m18 | partly | Page resolved (C:161). Audio not: V2-08. |
| V1B-m19 | resolved | C:165 GPT-2 exact; tiny models "to about 10⁻⁷". |
| V1B-m20 | resolved | As V1-12. |
| V1B-m21 | resolved | bars max 15 (preset "along a₂" peaks at 13); note explains empty negative bars. |
| V1B-m22 | resolved | As V1-04. |

Summary: 41 resolved, 4 partly (V1-07, V1B-m5, V1B-m7, V1B-m18; leftovers in V2-03, V2-08, V2-09, V2-11), 1 not resolved (V1B-m14 → V2-10). All four round-1 majors and all three V1B majors are resolved.

## Checked and found correct

- **Quotes.** Every curly-quoted string in content.html (about 120) was matched by script against the saved `.txt` files, whitespace- and quote-normalised, then letters-and-digits only. All source quotes are verbatim (the only non-matches are our own labels, scare words and the prompt). The ellipsis in "thousands of hours … are understandable" (C:209) skips only a parenthesis of L242 and keeps "have led us to believe". No quote comes from the hidden Olah lines (L490 and L273 confirmed visible after stripping HTML comments). Section labels re-mapped to the `##` headings of each `.txt`: all right except V2-04 and V2-07.
- **Writer-must-not-use list, items 1-15.** None used. No firmness upgrade: no privileged basis is "assert[ed], for their idealised linear stream" (C:356, C:394); Nanda's interference line keeps "as an intuition"; "almost" kept; L242 keeps "led us to believe".
- **Elhage scope.** Every Elhage cite is in High-Level Architecture, Communication Channel (incl. the L158 norm footnote), Subspaces and Residual Stream Bandwidth (L168-172, incl. virtual weights at L170), or the limit statements L98, L102, L142. Circuits appear only as the bare mention "two layers or less which have only attention blocks" (C:194, C:201, C:395).
- **Steering.** No sentence claims a behavioural effect (C:333, C:394, C:497, A:125, A:144). "Steering" and "activation addition" confirmed absent from all three sources.
- **Standalone, Discipline.** No other post is named or relied on (the new recall card 8 is on this post's toy). No Discipline data, models or results.
- **New revision text.** Matrix-vector step: M(1,0) = (2,1), M(1,1) = (3,3), M(1,−1) = (1,−1), each output entry a row dotted with the vector (C:488, A:194). Probe-push explanation: Pythagoras length √2 = 1.414; u = (−0.707, 0.707); the perpendicular-foot reading of a unit-length score; the margin's sign rule; u·v = 2.828 for v = (−2, 2) and 0 for v = (2, 2); calm −1.414 → 1.414, urgent 1.414 → 4.243; every calm point lands on an urgent start point. Rotation read (−2,1)·(0,5) = 5. Norm toy: (4,2) and (8,4) → (1,−1), r·LN = −1, r·x = 8 and 16. Reorder explanation (about seven digits; float32 epsilon 1.19e−7).
- **Toy numbers, rerun in Python.** Running sum (3,1), (2,2), (5,0), (4,2); shares 5, 0, 1, −1 and edge case 2, −1, 1, −2 (total 0); margins −4, −2.828, 0, 2, 2.828 at 0°, 45°, 90°, 120°, 135° (135° is the maximum over 0-180°); blind-probe scores 2.828, 4.243, 5.657; E1-E5 solutions; logit-lens toy rows; three-feature reads (1, −0.5, −0.5; all on and all at 0.5 give silence; features 1 and 2 give 0.5, 0.5, −1).
- **check.mjs.** 8/8 configs OK in the default state; every preset run with `--values` (best, blind, push along, push sideways, 120°, 90°; rotations 45°, 90°, 180°; three-feature presets; r = (0,1)) matches the text and captions.
- **Notebook claims against results.md.** 768/12 and 2,048 (row 35 config, cell [13]); 0.0, 1.03e−6, 7.8e−7, 6.2e−6 (rows 6, 7, 23, 43); index convention and last entry 0.0 / 0.986 (rows 41, 44-45, L12); tiny-model 10⁻⁷ (row 62); Gemma 3 9.7 vs 0.0 (rows 58-60); 7.211561 and 13 shares (row 49); steering residual 0 for five α (row 50); cosine 0.1318 vs 1.0935 (row 53); norms 5.3 / 472.4, BOS 3155.5 / 417.4 (rows 9-10); logit lens 0.0 / 834.6, ranks of " it" (rows 13-14, 17, 20); compatibility mode 1.09e−6 (row 27); HF and TL line numbers (L2, L12, L14-L19); environment in Sources. Nothing goes beyond results.md; trained Qwen3, Llama, Gemma and Mistral are reported as not run everywhere.
- **MacKay.** Exercise 15.18, p. 237; quotes verbatim; set up as an exercise; "no noise" and "cannot hear the output" kept; link labelled a structural analogy (ours), with the disanalogies.
- **Audio.** 12 chapter ids match the 12 `data-ch` sections in order; numbers equal the page. Differences other than V2-08 to V2-14 are paraphrase or cuts.
- **English pack.** Apart from V2-01 and V2-15 to V2-17, the sentences restate the post (pin down, face value, case in point, hold up, rest on, at pains to, fall out of, matter of convention, firm ground, lockstep, hinge on, tantamount to, the four patterns, the other three fixes, both tips).

## Counts

- Critical: 0
- Major: 1 (V2-01)
- Minor: 16 (V2-02 to V2-17)
