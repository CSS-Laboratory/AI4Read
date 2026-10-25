---
name: post03-verify-3c
stage: S5, round 3, targeted re-check after the meta-manager step-in and the writer's fix pass (response-3.md)
checker: independent fact-checker (fresh agent; did not write the post or any earlier report)
date: 2026-10-25
scope: the diff 0de295e..HEAD in posts/2026-10-residual-stream (src/content.html, audio-script.md, cite-map.tsv), the denominator commit 5af4e65 (results.md correction note, notebook 02 `err` docstring), and every finding of verify-3.md and verify-3b.md
evidence: notebook/02_bus_my_model.ipynb cells [2], [7], [9], [10] (code and saved outputs); notebook/01_bus_gpt2.ipynb cells [2], [6], [7], [11]; notebook/results.md; a fresh rerun of the identity test on the cached GPT-2 (HF_HUB_OFFLINE=1, float32, CPU, eager); sources/*.txt; source-brief.verified.md; check.mjs
not read: self-review.md, numbers.md
line refs: C = src/content.html line, A = audio-script.md line (current files)
---

# S5 verify, round 3c: post 03

## Counts

| Critical | Major | Minor |
|---|---|---|
| 0 | 0 | 2 |

**Gate verdict (facts): PASS. 0 critical, 0 major.**

## 1. The open major, V3B-01: resolved

**The code.** In notebook 02, cell [2], `err(a, b)` returns `max over positions of ‖a − b‖ / ‖b‖`. The docstring now reads "relative to the norm of the second argument b (the reference)", which is correct. Cell [9] computes `d_hs_diff_vs_writes = err(hs[L+1] - hs[L], a + m)[1]`, so the reference is the block's two writes `a + m`. The saved output gives a max of 6.219e−06 over blocks 0..10 (0-based), with the largest value at index 8. The 3.63 is `err(hs0, E.weight[ids])` in cell [7], so its reference is the table rows. The 0.986 is `err(hs[-1], last_out)` in cell [10], so its reference is the raw stream. The notebook 01 rows the fold-out cites (1.03e−6 in cell [7], 7.8e−7 in cell [11]) use a stream-valued reference: the reordered sum and the HF entry. Notebook 01's docstring ("the stream's norm") is therefore right for its own calls.

**Rerun** (GPT-2, same prompt, 7 tokens, my own hooks). Per block 1..11, max over positions:

| Reference | Range over blocks | Max |
|---|---|---|
| the two writes | 6.4e−8 to 6.22e−6 | 6.219e−6 (block 9) |
| stream after the block | 3.9e−8 to 6.4e−8 | 6.37e−8 |
| stream before the block | 4.4e−8 to 6.9e−7 | 6.95e−7 (block 1) |

Also: 3.6304 against the table rows (0.975 against `hs[0]`), and 0.9858 for the last entry against the raw stream. Every saved number is reproduced.

**Where V3B-01 appeared, now:**

| Place | Current text | Verdict |
|---|---|---|
| C:156 | "at most 6.2e−6, relative to the size of the block’s own two writes at that position. Measured against the stream instead, the same differences are about 4e−8 to 7e−7" | correct. The range matches the stream before the block (4.4e−8 to 6.9e−7); the values against the stream after the block (≤ 6.4e−8) fall inside it. "about" fits. |
| C:166 | "*Relative* means the difference divided by the size of the second thing in the comparison: the stream in rows 2 and 4, the block’s two writes in row 3, and the table row in the 3.63 below" | correct for every row (row 2's reference is the reordered sum, which is a stream value). The general rule also covers 0.986 and 9.7. |
| C:170 | "6.2e−6 relative to the two writes (4e−8 to 7e−7 relative to the stream)" | correct |
| C:174 | "the table row alone differs by 3.63, relative to the size of the table rows" | correct (rerun 3.6304) |
| C:511 | "relative to the size of those writes" | denominator correct; wording slip, see V3C-01 |
| A:56 | page wording, spoken | matches C:156 |
| A:212 | "relative to the size of those writes" | denominator correct; see V3C-01 |
| C:393, A:138 | no 6.2e−6 any more (grep) | n/a |

"relative to the size of the stream" now has 0 hits in the page and the audio. results.md row 43 and its correction note agree with the code.

## 2. Findings

### V3C-01 · minor · Recall card 1: "Neighbouring entries differed from the block’s two writes"
- **Where.** C:511: "Neighbouring entries differed from the block’s two writes by at most 6.2e−6, relative to the size of those writes (rounding)." A:212 still says "differed by the block's two writes by at most …".
- **Evidence.** Cell [9] compares the *difference* `hs[L+1] − hs[L]` with `a + m`. It does not compare the entries themselves.
- **Problem.** Read literally, the new "from" says that each entry is close to the writes. That is false, because an entry is a whole stream. The audio keeps the older "by", so the page and the audio no longer match on this line. The number and the denominator are right.
- **Fix.** In both the page and the audio: "The difference of neighbouring entries matched the block’s two writes to within 6.2e−6, relative to the size of those writes (rounding)."

### V3C-02 · minor · New ReLU gloss implies that the activation is a ReLU
- **Where.** C:356: "after the activation function (a curve applied to each number on its own; the ReLU turns every negative number into 0)". A:127: "A ReLU turns every negative number into zero, one number at a time."
- **Evidence.** Nanda L240: "an elementwise non-linearity, like ReLU or GELU". results.md (notebook 01, cell [4]): GPT-2 small uses `gelu_new`.
- **Problem.** This is a new gloss, and so a new claim (WRITING §9). "The ReLU" with the definite article reads as if it names *the* activation function. In GPT-2 small, the post's own model, the activation is GELU. The gloss is also only half a definition, because a ReLU also leaves positive numbers unchanged. The audio's "A ReLU" is fine apart from that half.
- **Fix.** "…on its own; one common choice, the ReLU, turns every negative number into 0 and keeps positive numbers as they are)". In the audio, add "and keeps positive numbers as they are".

## 3. Round-3 findings: resolved / not resolved

Checked against the current files, not against response-3.md.

| ID | Sev. | Status | Evidence |
|---|---|---|---|
| V3B-01 | major | resolved | §1 above (C:156, 166, 170, 174, 511; A:56, 212) |
| V3-01 = V3B-06 | minor | resolved | C:404 and A:149: "Testing use takes further tests … lists interventions such as ablation … and activation patching …, and a gradient-based test, TCAV". Nanda L1598 (derivative): gradient-based is correct. |
| V3-02 = V3B-08 | minor | resolved | C:166: "applies in its compatibility mode (and its older loader applied by default)". results.md L1–L3 and T6. |
| V3-03 | minor | resolved | C:200 and A:83: "what post-training changes inside a model". Nanda L905–908 define fine-tuning and RLHF but say nothing about their effect inside a model. |
| V3B-02 | minor | resolved | C:218: the quote cites "§ Interpretability as a Natural Science" (Olah L633, under the heading at L606). "the test itself is future work" keeps "§ Circuit 2" (L490, under L457). cite-map.tsv has the added row. |
| V3B-03 | minor | resolved | C:162: "say they generally think of it as “a communication channel”" (Elhage L155, verbatim) |
| V3B-04 | minor | resolved | C:517, A:85, A:234: "completely fatal" (Olah L602). "not fatal" / "would not be fatal": 0 hits. |
| V3B-05 | minor | resolved | C:219 "Concedes, of the curve circuit:" (Olah L320, § Argument 5, "the circuit constructing the curve detectors") |
| V3B-07 | minor | resolved | C:460 and A:179: "For GPT-2, in its compatibility mode …" (results.md row 27; L6) |
| V3B-09 | minor | resolved | C:72 and A:40: "every attention and MLP part of the model" |
| V3B-10 | minor | resolved | C:200 and A:83: "Mistral AI’s models". The only "Mistral" in the sources is Nanda L1676 (the training library). |
| V3B-11 | minor | resolved | ReLU glossed at C:356 and A:127. The new gloss is not quite right, though: V3C-02. |
| V3B-12 | minor | resolved | A:46 "that attention two wrote" (page C:90 and C:122 say "attention 2"). A:138 "In code and tiny random models" = C:393. |

13 of 13 round-3 findings are resolved (counting duplicates once: V3-01 = V3B-06, V3-02 = V3B-08). The round-3 major is resolved.

## 4. Changed text: checked and found correct

- **Norm worked example** (C:134, A:50). (4, 2): mean 3, centred (1, −1), population SD 1, result (1, −1). (8, 4): mean 6, centred (2, −2), SD 2, result (1, −1). "A list and its double give the same result" holds before the scale and shift (up to the norm's epsilon). "GPT-2 uses this version" is backed by results.md row 35 (LayerNorm). The page and the audio match.
- **Rotation check** (C:338, A:125). \((-r_2)(-x_2)+r_1x_1=r\cdot x\). Correct, and the page and the audio match.
- **Privileged basis definition** (C:355, A:127). Matches Nanda L234: "the coordinates in that basis have some meaning, that coordinates in an arbitrary basis do not have".
- **Probe** (C:324). "a layer’s output" fits Nanda L1587 ("on a specific activation (eg the output of layer 5)"). "likely" is kept.
- **Short answer (b)** (C:394, A:140). The new reads/writes sentence restates sections 3 and 5 at the same firmness, inside "our reading". The page and the audio match.
- **Scope trap** (C:200, A:83). "steer": 0 hits in the three web sources, so "(the word does not occur)" still holds. "Mistral AI": 0 hits.
- **Cite label** "Nanda 2022, § Positional information" (C:71) still names the right entry.
- **check.mjs**: 8/8 widget configs OK. No widget config changed in the diff.
- **Text against audio** for every changed passage: A:40, 46, 50, 56, 83, 85, 125, 127, 138, 140, 149, 179, 212 and 234 against C:72, 90/122, 134, 156, 200, 197, 338, 355–356, 393, 394, 404, 460, 511 and 517. All match in substance. The one mismatch is the wording of recall card 1 (V3C-01).
- **Notebook docstring.** The notebook 02 `err` docstring is corrected (commit 5af4e65). No number changed.

## Polish-pass check (diff 364524c..HEAD, content.html and audio-script.md)

Scope: every changed or new sentence in the page and audio, against source-brief.verified.md, sources/*.txt and notebook/results.md. Line numbers are as of HEAD (C = src/content.html, A = audio-script.md).

### Findings

| ID | Sev. | Location | Evidence | Fix |
|---|---|---|---|---|
| P-01 | minor | C:461 "(it rewrites the weights when it loads them)"; A:180 "which rewrites the weights when it loads them" | Compatibility mode does not act at load time. results.md L1: "`boot_transformers` returns **raw HF weights by default** ... `enable_compatibility_mode()` gives HookedTransformer-equivalent numerics"; T6: "the default loader does *not* rewrite weights; only `enable_compatibility_mode()` does". Load-time processing was the older `HookedTransformer` loader (L3), which C:167 already says correctly. The gloss came from critic-3c n5's suggested wording. | "(it rewrites the weights after they are loaded)" on the page; "which rewrites the weights after they are loaded" in the audio. |
| P-02 | minor | A:128 | The audio says "in the standard basis a ReLU acts on each coordinate independently" and only then "One common choice, the ReLU, ...", so the term is used before it is glossed, and "one common choice" no longer follows "activation function". It also drops the page's gloss of the activation function ("a curve applied to each number on its own", C:357). Same meaning as the page; order and one gloss differ. | Audio: "after the activation function, a curve applied to each number on its own. One common choice, the ReLU, turns every negative number into zero and keeps positive numbers as they are. In the standard basis a ReLU acts on each coordinate independently." |
| P-03 | minor | numbers.md row "Stream-relative range 4e-8 to 7e-7 \| section 3" (ledger, not published) | The polish pass cut this range from section 3 (C:157, A:57). It now appears only in the fold-out table, C:171. | Change the location to "fold-out `box-numbers`, table row 3". |

### Checked and found correct

- **n1, attention and MLP glosses** (C:72, A:40). "Brings in information from other positions" is supported by Nanda L601 ("the only layers that can move information between token positions"), L712 and L743. "A small network" is supported by L405 ("the classic neural network architecture"). "12 blocks" is still in this sentence.
- **n2, norm example** (C:135, A:50–51). Recomputed: (4, 2) has mean 3 and population SD 1, giving (1, −1). (8, 4) has mean 6 and SD 2, giving (2, −2)/2 = (1, −1). This matches numbers.md (norm toy) and brief unit 9. The page and the audio match.
- **n3, identity paragraph** (C:157, A:57). The cut leaves 6.2e−6 and its denominator (the block's two writes) unchanged, as in results.md rows 43 and 62. The stream-relative range survives at C:171. No remaining sentence refers to the cut one ("against the stream" and "same differences": 0 hits in either file). "Twelve blocks" is still at C:72 and A:40.
- **n4, "Relative" note** (C:167). "In the index note below, the table rows (3.63)" matches C:175 and results.md row 36 ("relative to the norm of the reference, here the table rows").
- **n5, the rest of the sentence** (C:461). The cite (transformer_bridge.py 548–560) and the "minus its mean coordinate" claim are unchanged and supported by results.md L2, row 27 and L7. Only the gloss is wrong (P-01).
- **n6, TCAV** (C:405, A:150). "It also lists TCAV" is right: it is an entry under Nanda § Non-MI Techniques (L1530, L1593). "Gradient-based test and not an intervention" is supported by L1597: the method takes the derivative and its cosine with the CAV, and no activation is changed. This is our label for the method, and the source's mechanism supports it. "Intuitively" (L1597) is kept. "Nanda also cautions" fixes the referent of "He", and "arguably" (L1365) is kept.
- **V3C-01, recall card 1** (C:512, A:213). "Differed by the block's two writes, up to an error of at most 6.2e−6, relative to the size of those writes" uses the right denominator (row 43). Resolved.
- **V3C-02, ReLU gloss** (C:357). "One common choice" no longer implies that GPT-2 uses a ReLU (GPT-2 applies a GELU, Nanda L732). The ReLU definition is common knowledge and correct. The quote "in the standard basis a ReLU acts on each coordinate independently" is unchanged. Resolved on the page; the audio order is P-02.
- **Hedges and numbers.** No hedge or number changed meaning. "Assert" (Elhage), "intuitively", "arguably" and "slightly privileged" are all intact.
- **Text against audio.** Every changed passage matches in substance. Exceptions: P-02 (order and one gloss) and the shared P-01 wording.
- **check.mjs** `posts/2026-10-residual-stream/src/content.html`: 8/8 widget configs OK.

Counts: 0 critical, 0 major, 3 minor (P-01, P-02, P-03).

**Verdict: 0 critical and 0 major. The polish pass passes. P-01 and P-02 are one-line fixes, recommended before release.**
