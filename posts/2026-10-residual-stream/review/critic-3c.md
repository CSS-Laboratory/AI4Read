---
name: critic-3c
post: 2026-10-residual-stream
stage: S5 round 3, targeted re-check after the writer's fix pass (response-3.md)
date: 2026-10-25
read: git diff 0de295ee..HEAD of src/content.html and audio-script.md, each changed passage in its section; response-3.md; critic-3.md; learner/state.md. self-review.md not read.
---

# Critic 3c: targeted re-check of post 03

**Verdict: 0 critical, 0 major, 6 new minor. m1, m2, m4, m5 and m6 are resolved. No score changes.**

Render check (Playwright, index.html, strict CSP):

| Width | `scrollWidth` | Console errors |
|---|---|---|
| 375 px | **375** (was 387) | 0 |
| 390 px | 390 | 0 |

The only elements wider than the viewport are MathJax nodes inside their `.mjx` scroll containers.

## 1. Critic-3 findings: resolved or not

| ID | Status | Evidence |
|---|---|---|
| m1 (rotation reason) | Resolved | After the formula comes "Check for 90°: Rr=(−r₂,r₁) and Rx=(−x₂,x₁), so (Rr)·(Rx)=(−r₂)(−x₂)+r₁x₁=r·x". It is a correct step-5 check, using only the dot-product rule the reader already has. The audio reads it in words. The "so" after "lengths and angles did not" still leans on an unstated fact, but the check and the widget now carry it. |
| m2 (norm paragraph) | Resolved | Both toy lists are worked: "(4, 2) has average 3 … centred as (1, −1); its standard deviation is 1 …", and "(8, 4) has average 6, centred (2, −2), standard deviation 2". I recomputed both: correct. "Same overall size" is now "a list and its double give the same result". The two pointers are merged into one sentence. This costs some phone density (n2). |
| m4 (short answer) | Resolved | Part (b) opens with "A part reads the list by dot products, which split into one share per writer (a writer at right angles to the reader goes unheard), and writes by adding, so writes can cancel." This is the section 5 result, in plain words. |
| m5 (privileged basis) | Resolved | The paragraph is split (259 px and 403 px at 390 px; it was about 576 px). The plain definition "A basis is privileged if its single coordinates, such as 'dimension 17', mean something on their own" is added. ReLU is glossed in place. The probe definition now says "a layer's output". Adam is named as "the Adam training method", which is enough for a caveat. |
| m6 (375 px scroll) | Resolved | Cite shortened to "Nanda 2022, § Positional information"; scrollWidth 375 (above). |

## 2. Changed passages: ladder, term order, phone reading

| Passage (line in content.html) | Ladder (§2) | Term order (§3) | Phone |
|---|---|---|---|
| Embedding and stream paragraphs (71-72) | n/a | "attention and MLP part" is new here (n1) | fine |
| Norm paragraph (134) | Improved: claim, then two worked instances | "centred" is used after "subtracts the average", which explains it | 634 px at 375 px, now the densest paragraph (n2) |
| Identity result (156) | OK | "relative to the size of the block's own two writes" reads as plain English | 7 numbers and two denominators (n3) |
| Fold-out notes and table (166-174) | n/a (fold-out) | "Relative" is defined, but the sentence is garbled (n4) | OK |
| Scope sentence (200) | n/a | Mistral AI's models and the other named families are fine | long but a single list |
| Olah quotes (218-219) | n/a (fold-out) | none | fine |
| Probe definition (324) | OK | "output" replaces "activations" | fine |
| Rotation (338) | Complete: instance, formula, 90° check, principle, widget | R is introduced by the line before it | fine |
| Basis paragraphs (355) | Definition first, then the MLP contrast | ReLU, activation function and Adam all glossed | OK |
| Short answer (b) (394) | n/a | uses only terms from sections 5 and 6 | about 120 words, one idea per sentence |
| Seeing is not doing (404) | OK | "ablation" and "activation patching" glossed in parentheses | 547 px at 375 px; the TCAV sentence is long (n6) |
| "What to look for" (460) | n/a | "compatibility mode" is not explained in the main text (n5) | fine |
| Recall cards (511, 517) | n/a | consistent with the text | fine |

No WRITING §2 ladder was broken. No change uses a term in a formula before its definition. The audio lines match the page; I read the new audio lines for the norm, the identity result, the rotation check, the basis, short answer (b), TCAV and "What to look for", and they read aloud well.

## 3. New findings (all minor; none blocks the gate)

**n1. "Attention and MLP" appear before they are defined. (C2/C3, section 3, line 72)**
- Text: "every attention and MLP part of the model changes it by adding to it". The `<dfn>` for both is four paragraphs later. critic-3 m3 already noted that attention is thinly defined; this edit puts the undefined words earlier.
- Fix: write "every part of the model (the attention and MLP parts, defined below)", or go back to "every part".

**n2. The norm paragraph is now the densest on the page. (C3, section 3, line 134)**
- It is about 190 words and 634 px tall at 375 px, with three cites. The ladder is right; the packaging is not.
- Fix: split after "…a learned scale and shift." The second paragraph begins "Before that last step, a list and its double give the same result."

**n3. The identity paragraph carries seven numbers and two denominators. (C2/C3, line 156)**
- Numbers: 12, 32, seven digits, eleven, 6.2e−6, 4e−8, 7e−7. WRITING §5 allows about five.
- Fix: keep 6.2e−6 with its denominator in the paragraph, and leave the stream-relative range "4e−8 to 7e−7" in the fold-out table row (it is already there).

**n4. The "Relative" definition in the fold-out is garbled. (C3, line 166)**
- Text: "…and the table row in the 3.63 below". The "3.63" is two paragraphs down and is not introduced.
- Fix: "…and, in the index note below, the table rows (3.63)".

**n5. "Compatibility mode" is never explained where it is used. (C3, line 460)**
- Only the fold-out says "rewriting of the weights that TransformerLens applies in its compatibility mode".
- Fix: "For GPT-2, TransformerLens rewrites the weights when it loads them (its compatibility mode); the stream it returns is then the Hugging Face stream minus its mean coordinate."

**n6. The TCAV sentence is long. (C3, line 404; audio 149)**
- About 50 words, with "gradient-based" left undefined. On the audio, "He cautions" can be read as the TCAV author rather than Nanda.
- Fix: split after "TCAV". Say "…which compares a probe-like direction with the direction that would most raise an output", and write "Nanda also cautions".

**Carried (not touched, as instructed; all minor):** m3 (attention gloss), m7 (bus arrow), m8 (repeats, about 100 words), m9 (long audio chapters), m10 (identity test equivalence), m11 (hook pointer), m13 (two meanings of "direction"), m14 (cosmetics, host handle size), m15 (separate toy). Length is now 7,295 words (cap 7,500), 153 more than in critic-3; about 10% still repeats.

## 4. Re-scores (only criteria the changes touch)

| # | Criterion | critic-3 | Now | Reason |
|---|---|---|---|---|
| 2 | Ladder | 4 | **4** | m1 and m2 are closed with worked checks. m3 and m10 stay open, and n1 adds a small term-order gap. |
| 3 | Clarity and English | 4 | **4** | The basis paragraph (the m5 case) is fixed. The norm and TCAV paragraphs are denser (n2, n6), but each is one or two dense paragraphs in a section, which fits a 4. |
| 4 | Insight and connections | 5 | **5** | The changes to lens-linalg and short answer (b) keep "adds / does not explain" and add the read/write result. |
| 5 | Illustrations | 4 | **4** | No widget changed. m7 stays open. The 375 px overflow is fixed. |
| 6 | Concision | 4 | **4** | +153 words, mostly checks and clarifications. No new repeats. |

Criterion 1 belongs to the fact-checkers.

## 5. Gate verdict (pedagogy)

**PASS: 0 critical, 0 major, and every criterion at 4 or above (C2 4, C3 4, C4 5, C5 4, C6 4).**
