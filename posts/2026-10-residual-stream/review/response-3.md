---
name: post03-response-3
stage: S5 round 3, narrow fix pass (writer, after the meta-manager step-in)
date: 2026-10-25
inputs: review/verify-3.md, review/verify-3b.md, review/critic-3.md, notebook/results.md (correction note)
scope: only the findings listed below. source-brief.verified.md, the notebooks and results.md were not touched.
C = src/content.html, A = audio-script.md (line numbers before the edits).
---

# Response to round 3

Main text: 7,295 words (cap 7,500; was 7,142). Build: 0 unmapped, 0 missing, 0 math errors. check.mjs 8/8. test.mjs PASS. Playwright at 375 px: scrollWidth = 375.

## Major

### V3B-01 · fixed
The 6.2e−6 is relative to the norm of the block's own two writes. Stream-relative the same differences are about 4e−8 to 7e−7 (results.md correction note).
- C:156 (section 3): "relative to the size of the block's own two writes at that position. Measured against the stream instead, the same differences are about 4e−8 to 7e−7", with the Notebook 02 cite.
- C:166 (fold-out): *Relative* now reads "the difference divided by the size of the second thing in the comparison: the stream in rows 2 and 4, the block's two writes in row 3, and the table row in the 3.63 below".
- C:170 (table row 3): "6.2e−6 relative to the two writes (4e−8 to 7e−7 relative to the stream)".
- C:174: "the table row alone differs by 3.63, relative to the size of the table rows".
- C:510 (recall card 1): "differed from the block's two writes by at most 6.2e−6, relative to the size of those writes (rounding)".
- Audio A:56: "relative to the size of the block's own two writes at that position. Measured against the stream instead, the same differences are about four times ten to the minus eight up to seven times ten to the minus seven."
- Audio A:212: "by at most six point two times ten to the minus six, relative to the size of those writes, which is rounding."
- numbers.md updated (denominators; stream-relative row).

## Minors from verify-3 and verify-3b

| ID | Fix | Where | New audio line |
|---|---|---|---|
| V3-01 = V3B-06 | TCAV is no longer an intervention: "Testing use takes further tests… Nanda's glossary lists interventions such as ablation … and activation patching …, and a gradient-based test, TCAV, which compares…" | C:403 | A:149: "Testing use takes further tests, which this post does not run. Nanda's glossary lists interventions such as ablation, which means deleting a part, and activation patching, which swaps in the activation from another input; and a gradient-based test, TCAV, which compares a probe-like direction with the direction that, intuitively, would most raise an output." |
| V3-02 = V3B-08 | "…without the rewriting of the weights that TransformerLens applies in its compatibility mode (and its older loader applied by default)" | C:166 | none (fold-out only) |
| V3-03 | Scope stated precisely: "…or Mistral AI's models, base versus instruct models, what post-training changes inside a model, or steering" | C:200 | A:83: "none of the three says anything about Qwen3, Llama three, Gemma three or Mistral AI's models, base versus instruct models, what post-training changes inside a model, or steering, and none tests concepts as directions in a language model's stream." |
| V3B-10 | "Mistral AI's models" (same edit as V3-03) | C:200 | A:83, as above |
| V3B-02 | Two cites: the quote now cites "§ Interpretability as a Natural Science"; "the test itself is future work" keeps "§ Circuit 2" | C:218 | none (fold-out) |
| V3B-03 | "Elhage and colleagues say they generally think of it as “a communication channel”" | C:162 | none (audio has no such sentence) |
| V3B-04 | "would not be completely fatal" | C:516 (recall card 7) | A:234: "Which of Olah's three claims would not be completely fatal to circuits research if false?"; A:85: "The third is the only one not completely fatal if false." |
| V3B-05 | "Concedes, of the curve circuit:" | C:219 | none (fold-out) |
| V3B-07 | "For GPT-2, in its compatibility mode, TransformerLens gives the Hugging Face stream minus its mean coordinate" | C:459 | A:179: "For GPT-2, in its compatibility mode, TransformerLens gives the Hugging Face stream minus its mean coordinate." |
| V3B-09 | "every attention and MLP part of the model changes it by adding to it" | C:72 | A:40: "…every attention and MLP part of the model changes it by adding to it." |
| V3B-11 | ReLU glossed: "(a curve applied to each number on its own; the ReLU turns every negative number into 0)" | C:355 | A:127: "A ReLU turns every negative number into zero, one number at a time." |
| V3B-12 | Audio "attention two"; "and tiny random models" restored | none on the page (C:90 and C:122 already say "attention 2") | A:46: "The second number of the last write, plus two, undoes the minus two that attention two wrote."; A:138: "In code and tiny random models, Gemma 3 norms each sub-layer's output before adding it." |

## Critic minors

- **m1 (done).** C:338 starts with "Check for 90°: \(Rr=(-r_2,r_1)\) and \(Rx=(-x_2,x_1)\), so \((Rr)\cdot(Rx)=(-r_2)(-x_2)+r_1x_1=r\cdot x\)." Audio A:125: "Check for ninety degrees: the turned r is minus r two, r one, and the turned x is minus x two, x one. Their dot product is minus r two times minus x two, plus r one times x one, which is r one x one plus r two x two, the original."
- **m2 (done).** C:134: the two toy lists are worked step by step ("The list (4, 2) has average 3, so it is centred as (1, −1); its standard deviation is 1 …"), "same overall size" is replaced by "a list and its double give the same result", and the two fold-out pointers are merged into one sentence. Audio A:50: "Before that last step, a list and its double give the same result. The list four, two has average three, so it is centred as one, minus one; its standard deviation is one; the result is one, minus one. The list eight, four has average six, centred two, minus two, standard deviation two, so the result is again one, minus one. GPT-2 uses this version. Two fold-outs give more: a code reading at the end of this section and a norm table in section six."
- **m4 (done).** Short answer (b), C:392, begins: "A part reads the list by dot products, which split into one share per writer (a writer at right angles to the reader goes unheard), and writes by adding, so writes can cancel." Audio A:140: "A part reads the list by dot products, which split into one share per writer, and a writer at right angles to the reader goes unheard. It writes by adding, so writes can cancel."
- **m5 (done).** C:355 is split into two paragraphs. A plain definition is added: "A basis is privileged if its single coordinates, such as “dimension 17”, mean something on their own." In the probe definition (C:324) "a layer’s activations" became "a layer’s output". Audio A:127: "A basis is privileged if its single coordinates, such as dimension seventeen, mean something on their own."
- **m6 (done).** The no-wrap cite in section 3 (C:71) now reads "Nanda 2022, § Positional information". Playwright at 375 px: scrollWidth 375 (was 387). It still maps to the Nanda entry (0 unmapped).

## Not done (as instructed or out of scope)
- Host-chrome items (m14 handle size, m16).
- Other critic minors (m3, m7, m8, m9, m10, m11, m13, m14, m15): the brief for this pass listed only m1, m2, m4, m5 and m6.
- The notebook docstring for `err` (V3B-01, "fix the notebook docstring too"): not touched, per the limits. results.md's correction note says the maintainer corrected it.
- The loose "moves every score in lockstep" wording in the English loop (V3B "not counted"): not touched.

## Checks
- `node site/ai4read/build-post.mjs posts/2026-10-residual-stream`: 0 unmapped, 0 missing, math errors 0.
- `check.mjs`: 8/8 widget configs OK.
- `test.mjs --inline`: PASS, 0 console errors, no overflow at 390 px, readouts reproducible.
- Playwright at 375 px: scrollWidth = 375.
- Wordcount: 7,295 main words.


## Polish pass (minor findings of verify-3c and critic-3c)

Only the listed passages changed. Every number, hedge and cite is as before; "12 blocks" and the stream-relative range were dropped from the identity paragraph because the same facts stand in section 3 and in the fold-out table.

| ID | New text (page) | New audio line |
|---|---|---|
| V3C-01 | C:511: "Neighbouring entries differed by the block’s two writes, up to an error of at most 6.2e−6, relative to the size of those writes (rounding)." | A:212: "Neighbouring entries differed by the block's two writes, up to an error of at most six point two times ten to the minus six, relative to the size of those writes, which is rounding." |
| V3C-02 | C:356: "(a curve applied to each number on its own; one common choice, the ReLU, turns every negative number into 0 and keeps positive numbers as they are)" | A:127: "One common choice, the ReLU, turns every negative number into zero and keeps positive numbers as they are, one number at a time." |
| n1 | C:72: "every attention part (it brings in information from other positions) and every MLP part (a small network) changes it by adding to it." | A:40: "...every attention part, which brings in information from other positions, and every MLP part, a small network, changes it by adding to it." |
| n2 | C:134 split in two. First: the norm in one sentence chain. Second: "Before that last step, a list and its double give the same result. The list (4, 2) has average 3 and standard deviation 1: centred it is (1, −1), and dividing by 1 changes nothing. The list (8, 4) has average 6 and standard deviation 2: centred it is (2, −2), and dividing by 2 gives (1, −1) again. GPT-2 uses this version." | A:50, same two paragraphs: "...The list four, two has average three and standard deviation one: centred it is one, minus one, and dividing by one changes nothing. The list eight, four has average six and standard deviation two: centred it is two, minus two, and dividing by two gives one, minus one again." |
| n3 | C:156: "We ran this on GPT-2 small with the sentence ... Over the first eleven blocks they differed by at most 6.2e−6, relative to the size of the block’s own two writes at that position." The sentence with 4e−8 to 7e−7 is cut; it remains in the fold-out table (C:170). | A:56: same cut ("...at that position. That is rounding."); "with twelve blocks" removed. |
| n4 | C:166: "...the block’s two writes in row 3, and, in the index note below, the table rows (3.63);" | none (fold-out only) |
| n5 | C:460: "For GPT-2, in its compatibility mode (it rewrites the weights when it loads them), TransformerLens gives the Hugging Face stream minus its mean coordinate" | A:179: "For GPT-2, in its compatibility mode, which rewrites the weights when it loads them, TransformerLens gives the Hugging Face stream minus its mean coordinate." |
| n6 | C:405 split: "...activation patching (swapping in the activation from another input) [cite]. It also lists TCAV, a gradient-based test and not an intervention: it compares a probe-like direction with the direction that, intuitively, would most raise an output (its example is a zebra in an image) [cite]. Nanda also cautions that zero ablation ..." | A:149: "...activation patching, which swaps in the activation from another input. It also lists TCAV, a gradient-based test and not an intervention: it compares a probe-like direction with the direction that, intuitively, would most raise an output. Its example is a zebra in an image. Nanda also cautions that zero ablation..." |

Checks after the pass: build-post 0 unmapped, 0 missing, math errors 0; check.mjs 8/8 widget configs OK; test.mjs --inline PASS; main text 7,317 words (cap 7,500).
