---
name: post03-verify-3
stage: S5, round 3 (final)
checker: independent fact-checker (fresh agent; did not write the post or any earlier report)
date: 2026-10-25
checked: src/content.html (text, 8 widget configs, 3 fold-outs, recall, sources), audio-script.md (12 chapters), english/english.json (28 items and the loop)
evidence: source-brief.verified.md; sources/*.txt (line numbers = file lines) and mackay-2003-mac.txt; Nanda HTML for section mapping; notebook/results.md (authority for notebook claims) and the saved cells of both .ipynb; check.mjs (default state and all presets)
independence: self-review.md and numbers.md not read; response-2.md read only after the own pass
---

# S5 verify, round 3: post 03

`C:` = line of `src/content.html`, `A:` = line of `audio-script.md`, `E:` = item in `english/english.json`. Source lines are lines of the saved `.txt` files.

## Critical

None.

## Major

None.

## Minor

### V3-01 · minor · Lens 1: TCAV is listed as an intervention
- **Where.** C:403: "Testing use takes interventions, which this post does not run. Nanda’s glossary lists some: ablation …, activation patching …, and TCAV, which compares a probe-like direction with the direction that … would most raise an output". A:149 says the same.
- **Source.** Nanda L1598 (§ Non-MI Techniques, TCAV): "looks at the derivative of the model’s output (the zebra log prob) with respect to that layer’s activation". L1442: activation patching "uses a causal intervention". L1361: an ablation "deletes one activation".
- **Problem.** Ablation and patching are interventions. TCAV is not: it compares the probe-like vector with a gradient and changes nothing in the run. The wording makes TCAV "one of" the interventions. The TCAV clause itself is accurate, and "intuitively" keeps Nanda's hedge. This is a new gloss (WRITING §9), not a wrong quote.
- **Fix.** "Nanda’s glossary lists interventions such as ablation … and activation patching …, and a gradient-based test, TCAV, which compares …"; the same in A:149.

### V3-02 · minor · fold-out: "the rewriting … that TransformerLens normally applies"
- **Where.** C:166 (`#box-numbers`): "*Raw weights* means the published weights, without the rewriting of the weights that TransformerLens normally applies."
- **Evidence.** results.md L1 and T6: in TransformerLens 4.x "the default loader does *not* rewrite weights; only `enable_compatibility_mode()` does"; L3: the older `HookedTransformer.from_pretrained` processed by default. The post's reference run uses 4.3.0 (C:531), and C:459 correctly says "In its compatibility mode".
- **Problem.** For the version cited, "normally" is wrong: by default the weights are raw. The definition of "raw weights" is right; only the adverb is off, and the fold-out is not part of the argument.
- **Fix.** "… without the rewriting of the weights that TransformerLens applies in its compatibility mode (and its older loader applied by default)."

### V3-03 · minor · scope trap: "none of the three says anything about … post-training"
- **Where.** C:200 (trap box, `#bets`): "none of the three says anything about Qwen3, Llama 3, Gemma 3 or Mistral, base versus instruct models, post-training or steering". A:83 the same.
- **Evidence.** Nanda L905: "Fine-tuning: Taking a pretrained model, and training it on a more specific task." L908: RLHF "is a special form of fine-tuning large, pre-trained language models." The post itself cites these lines in `#work` (C:501). Brief trap 1 limits the gap to "post-training effects on representations".
- **Problem.** As worded, the sources say nothing at all about post-training; Nanda does define two post-training procedures. The post corrects this in section 11, so the reader is not misled for long, but the two sentences disagree.
- **Fix.** "… base versus instruct models, what post-training changes inside a model, or steering …"; the same in A:83.

## Round-2 findings: resolved / not resolved

Checked against the current files, not against response-2.md. Every audio line that response-2 quotes was found verbatim in audio-script.md.

| Round-2 ID | Status | Evidence in the current files |
|---|---|---|
| V2-01 (major) | resolved | E loop and the "firm ground" item: "concepts are directions in a language model’s stream". |
| V2-02 | resolved | C:197 and C:224 quote L587 with "the apparent universality of some low-level vision features"; A:81 the same. |
| V2-03 | resolved (moot) | Cars-and-dogs sentence gone ("co-occur": 0 hits in page and audio). |
| V2-04 | resolved | C:218: "the test itself is future work" carries "Olah 2020, § Circuit 2". |
| V2-05 | resolved | C:134 "the account Elhage and colleagues give, which says: “We also ignore layer normalization.”" (L142); A:50 the same. |
| V2-06 | resolved | C:134 "then applies a learned scale and shift. Before that last step …"; A:50 the same. |
| V2-07 | resolved | C:71 cites § Transformer Components, Positional information (L671); C:137 cites § Transformer Basics (L601) for the first clause and § Decoder-only (L831) for the second. |
| V2-08 | resolved | A:58 "a TransformerLens comparison made with raw weights"; page row C:171 "(raw weights)", 7.8e−7 = row 23. |
| V2-09 | resolved | A:83 "They promise a forthcoming paper on larger ones, which is not among our sources." (L102). |
| V2-10 | resolved | A:164 "it could be that the input state was zero, one or one, zero" (p. 237). |
| V2-11 | resolved | A:98 "write of hints, which they word with may" ("only of hints": 0 hits). |
| V2-12 | resolved | A:52 "no single hidden state of a sentence … That is ours." |
| V2-13 | resolved | "four times" sentence gone from the audio (0 hits). |
| V2-14 | resolved | A:25 options 1-4 equal C:50. |
| V2-15 | resolved | E loop "the division inside the norm in front of it". |
| V2-16 | resolved | E "affect vs effect": "unless it is at right angles to u" in sentence, wrong and right lines. |
| V2-17 | resolved | E "to bear out": "for entries 0 to 11". |
| V2B-01 (major) | resolved | The false absence claim is gone (C:403, A:149); the three techniques are named and cited correctly (L1361-1375, L1442, L1593-1598). New, smaller gloss issue: V3-01. |
| V2B-02 | resolved | C:155 and A:54: output named `hidden_states`; no claim about the library's wording. |
| V2B-03 | resolved | C:71 "position list included"; C:174 entry 0 = table row plus position list (0.0), table row alone 3.63 (rows 36-37); C:392 and A:138 the same. |
| V2B-04 | resolved | As V2-07(a). |
| V2B-05 | resolved | As V2-02. |
| V2B-06 | resolved (moot) | Paragraph deleted ("bottleneck": 0 hits). |
| V2B-07 | resolved | C:355 and A:127 quote L245 "always slightly privileged", with floating point, Adam and "spectrum"; C:406 and A:155 "a habit, not a law (ours)". |
| V2B-08 | resolved | C:211 "gives an intuition (ours: an argument, not a measurement)" and L200 "an extremely natural way to represent things". |
| V2B-09 | resolved | As V2-04. |
| V2B-10 | resolved | C:413 and A:158 "binary multiple access channel, whose output is the sum of two inputs" (caption 15.3b); "adder": 0 hits. |
| V2B-11 | resolved | (a) C:134 "GPT-2 uses this version" cites Notebook 02 (row 35); "close variants" gone; RMS norm moved to C:176 with HF modeling_qwen3.py 49, 62-63 (L14). (b) C:498 and A:201 conditional, "(ours)". |
| V2B-12 | resolved | C:459 (3) and A:179; notebook 01 cell [10] computes max(min urgent − max calm, min calm − max urgent), which is 0 at 0° (results.md "W9 margin"). |
| V2B-13 | resolved | As V2-11. |
| V2B-14 | resolved | As V2-10. |
| V2B-15 | resolved | As V2-08. |
| V2B-16 | resolved | As V2-13. |
| V2B-17 | resolved | A:25, A:29, A:33 equal the page options; A:52 as V2-12. |

Summary: 34 of 34 round-2 findings resolved (2 moot by deletion: V2-03, V2B-06). Both round-2 majors are resolved.

**Audio fixes claimed in response-2, checked in audio-script.md:** V2-02 (A:81), V2-05 and V2-06 (A:50), V2-08 (A:58), V2-09 (A:83), V2-10 (A:164), V2-11 (A:98), V2-12 (A:52), V2-13 (deleted), V2-14 and V2B-17 (A:25, A:29, A:33), V2B-01 (A:149), V2B-02 (A:54), V2B-03 (A:38, A:138), V2B-07 (A:127, A:155), V2B-10 (A:158), V2B-11(b) (A:201), V2B-12 (A:179), critic M2 lens contrast (A:170), M3 (A:77), m6 (A:109), m8 (A:92, A:166), m11 (A:12), m12 (a) A:125, (b) A:69, (d) A:123. All present, word for word.

## Brief note, unit 12 (writer's "UNVERIFIED" note)

Checked against nanda-2022-glossary.txt L1355-1475 and L1584-1600, plus a grep of the whole file for "TCAV", "concept activation", "probe", "ablat" and "patch". **Verdict: rewritten as [S3-verified] with corrections**, not struck. What was right: the line ranges for ablation (L1361-1375) and TCAV (L1593-1598), the TCAV description (a probe-like vector compared with the derivative of an output; zebra example), "TCAV appears only at L1593-1598", and "none is applied to a probe direction in a language model". Corrected: (1) "use-tests" is our label, now marked so; (2) TCAV is gradient-based, not an intervention, now stated, with a rule not to list it as one (this is V3-01 in the post); (3) the patching entry is L1442-1456, not just L1442, and ablation also appears outside its entry (L985, L1302-1304, L1432, L1521). Each claim in the new note carries a short verbatim quote with its line. This is the only edit made outside `review/`.

## Checked and found correct

- **Quotes.** Every curly-quoted string in content.html (outside widget configs) and in english.json matched by script against the four saved `.txt` files (NFKC, quote-normalised, letters and digits only). All source quotes are verbatim; the only non-matches are our own labels, the prompt and scare words. The ellipsis in the Olah L242 quote (C:208) skips only a parenthesis and keeps "have led us to believe". Referents checked by hand: Olah L232 (understandable features), L587 (apparent universality of low-level vision features), L320 (curve circuit, § Argument 5), L669 ("adjacent layers"); Nanda L1365 ("This" = zero ablation), L287 (opens "Intuitively"), L245 (caveat and "spectrum"), L1598 ("intuitively represents"). No quote is cut before its turn. No hidden Olah line is used.
- **Section labels.** Olah and Elhage labels mapped to the `##` headings of each `.txt`; Nanda labels mapped to the HTML `<h3>` sections. All hold. Elhage cites stay inside Introduction (L98, L102), Model Simplifications (L142), High-Level Architecture (L148), Communication Channel (L155, L158) and Residual Stream Bandwidth (L168, L172).
- **Writer-must-not-use list, items 1-15.** None used. No firmness upgrade: Olah's claims stay "deliberately speculative"; L259 is quoted whole; L280 keeps "almost"; L1587 keeps "likely"; L172 keeps "hints" and "may"; no privileged basis is "assert[ed], for their idealised linear stream".
- **Absence claims re-grepped.** "hidden state", "hidden_state", "steer", "refusal" and "trust" (as a behaviour): 0 hits in the three web sources. "Post-training": see V3-03.
- **Toy numbers, recomputed.** Running sum (3,1), (2,2), (5,0), (4,2); shares 5, 0, 1, −1 and the r = (0,1) case 2, −1, 1, −2; the folded answer r = (2,−1); unit-length check u = (0.6, 0.8), score 3, foot (1.8, 2.4), residual (3.2, −2.4), dot 0; margins −4, −2.828, 0, 2, 2.828; blind scores 2.828, 4.243, 5.657; push (−2,2): u·v = 2.828, calm −1.414 → 1.414, urgent 1.414 → 4.243; push (2,2): 0; E4 −1.414 and 2; rotation shares unchanged, rotated writers (−2,1), (1,2), (−1,−1), (2,3); norm table 3/6, (1,−1), sd 1/2, −1, 8/16; logit-lens rows and the flip from token 2 to token 1; three-feature reads, (0.5, 0.5, 0.5) silent; M(1,0) = (2,1), M(1,1) = (3,3), M(1,−1) = (1,−1); "four writes" in the English pattern item.
- **check.mjs.** 8/8 configs OK; every preset of `probe-push`, `rotate`, `read-split` and `three-features` run with `--values`; readouts equal the text and captions.
- **Notebook claims.** Every number is in results.md: 768, 12 blocks, 2,048; 0.0, 1.03e−6, 6.2e−6, 7.8e−7, epsilon 1.19e−7; index convention 0.0, 3.63, 0.986; tiny models about 10⁻⁷, Gemma 3 9.7 vs 0.0; 7.211561 and 13 shares; steering residual 0 for five α; cosine 0.1318 vs 1.0935; norms 5.3 and 472.4; logit lens 0.0 and 834.6, ranks of " it" 0, 1, 0, 0, 0 after blocks 8-12, and 12 without the norm; compatibility mode = HF stream minus its mean coordinate; HF and TransformerLens line numbers (L2, L12, L14, L15, L17-L19). Trained Qwen3, Llama, Gemma and Mistral are reported as not run everywhere.
- **Steering, scope, standalone, Discipline.** No sentence claims a behavioural effect of steering; the notebook result is called arithmetic. Elhage stays within Kunhao's scope. No other post is cited or relied on. No Discipline data, models or results.
- **MacKay.** Exercise 15.18, p. 237: quotes verbatim; "no noise" and "cannot hear the output" kept; no capacity claim; link labelled a structural analogy (ours), with the disanalogies.
- **Audio.** 12 chapter ids match the 12 `data-ch` sections in order; numbers and formulas equal the page; the "AI4Read from CSS Lab" intro is present. Apart from V3-01 and V3-03, which the audio shares with the page, differences are cuts or paraphrase.
- **English pack.** All 28 item sentences and the loop restate the post at its own firmness; scoped wording kept ("in a language model’s stream", "for entries 0 to 11", "which we did not run", "with the hooks placed correctly"). Levels not checked (not a fact-check task).
- **Sources list.** Olah authors, 2020, DOI 10.23915/distill.00024.001; Elhage first authors and "Dec 22, 2021"; MacKay pages; HF and TransformerLens file lists agree with results.md.

## Counts

- Critical: 0
- Major: 0
- Minor: 3 (V3-01 to V3-03)
- Round 2: 34 of 34 resolved (2 moot by deletion), 0 not resolved.
