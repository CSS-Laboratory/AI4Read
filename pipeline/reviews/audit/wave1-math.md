# Independent audit, wave 1: math and formal digests (Axler ch. 5 p1, Cover & Thomas ch. 8 p1, Blei et al. 2017 p1, Ashby ch. 11)

Auditor: Claude Opus 5.5 (I did not write these digests). Date: 2026-10-14.
Pipeline under audit: Claude Sonnet 5.5, digest prompt v2.1 + independent verifier v2.1. All four digests are `verified: repaired`.
Ground truth: the page images of the four extracts in `/home/claude/audit/w1/`. I read every page (22 + 20 + 21 + 9 spread images). I zoomed in on the doubtful spots (Ashby pp. 208, 217) at 250 dpi.
Recomputation: `scratchpad/recompute.py` re-runs every worked number, toy example and "(added step)" (results are given per digest).
Page offsets were checked against `pipeline/units.csv`.

Severity scale (as briefed): **critical** = wrong equation, number or statement; a strengthened or weakened claim (incl. a dropped condition); a claim not in the source. **major** = wrong page ref; missing key result or step; dropped hedge; 3 or more undefined terms. **minor** = notation, format, small coverage gaps.

## Summary

| Digest | Checks | Correct | Minor | Major | Critical | Toy / added steps | Length (words; source / target) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Axler ch. 5 p1 (pp. 132–153) | ~80 (34 numbered items 5.1–5.34, 6 examples, every proof step, 6 exercises, L0–L2, notes) | ~75 | 5 | 0 | 0 | all correct | 3,947; 7,924 / ~4,360 | excellent |
| Cover & Thomas ch. 8 p1 (pp. 183–202) | ~85 (eqs 8.1–8.81, ~25 claims, refs) | ~79 | 5 | 1 | 0 | all correct | 3,368; 5,371 / ~2,950 | good after 1 fix |
| Blei et al. 2017 p1 (pp. 1–21) | ~95 (eqs 1–58, Alg. 1–2, ~35 claims and refs) | ~91 | 3 | 1 | 0 | all correct | 5,147; 10,138 / ~5,580 | good; needs term glosses |
| Ashby ch. 11 (pp. 202–218) | ~70 (3 tables cell by cell, 11/8–11/9 formulas, ~40 claims, 6 exercises) | ~64 | 2 | 2 | 2 (both low-impact) | all correct | 4,159; 6,587 / ~3,620 | good after 4 fixes |

**Estimate of errors that survive verification:** about 0.5 critical, 1 major and 4 minor per unit. The 2 critical errors (both in Ashby) are in illustrative examples, not in the law or its derivations. Every numbered equation in all four digests matches the page image symbol by symbol. The only exceptions are two equations that one digest omits (Cover 8.67–8.68) and the Ashby misprints, which the digest copies or corrects and flags. Most surviving errors fall into three groups:

1. **Things copied from the text layer without checking the image.** Ashby's "±10°" became "+10°". Cover's (8.66)–(8.68) were declared "only partly legible", but they are fully legible.
2. **Page refs on two-page spreads.** In Ashby, a passage on p. 212 is cited as p. 213.
3. **Dropped conditions and hedges in small examples.** Examples: Ashby's photographer, and "essentially independent".

The toy examples are all correct, well chosen and illustrate the main result.

**Verdict: OK to continue the batch.** Two cheap guards would remove most of the residue (see Improvements): an image re-check for ±, ≤/≥ and "unreadable" claims, and correct printed-page labels for spreads.

---

## 1. Axler 2024, *Linear Algebra Done Right*, ch. 5 part 1 (printed pp. 132–153)

### A. Math and faithfulness
I checked the following against the images, step by step:
- Definitions 5.1, 5.2, 5.5, 5.8, 5.13, 5.14, 5.16, 5.21, 5.24.
- Results 5.7, 5.11, 5.12, 5.17, 5.18, 5.19, 5.22, 5.27, 5.29, 5.31, 5.32, 5.33, 5.34 and every proof step the digest gives. This includes the induction in 5.22 (5.23, $q\in\mathcal P_m$, $\dim\operatorname{range}q(T)\le\dim V-m$, $s$ with $\deg s\le\dim V-m$), the completed square in 5.33 and the parity argument in 5.34.
- Examples 5.3, 5.4, 5.6, 5.9 (5.10), 5.15, 5.20, 5.26, 5.28.
- The 99.8% / 99.999% figures and the "millions of random matrices" margin note.
- The exercise counts (5A: 43, 5B: 29).
- The page offset (pdf 146 = p. 132, so printed = pdf − 14; correct per `units.csv`).
- The "≈ 100√2" header on p. 141 (real: the printed page shows it).

All are correct. The voice handling is good: the rhetorical question on p. 134 is tagged and answered with the text's own forward references.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| A1 | L3, Theorems 5.31 and 5.32 | The hypothesis "Suppose $V$ is finite-dimensional" is dropped from both statements. It is implicit, because the minimal polynomial is defined only in finite dimension, but the source states it. | p. 148 (5.31), p. 149 (5.32) | minor |
| A2 | L3, Example 5.28 | "no zero … can be expressed with rational numbers, roots and the usual arithmetic". The source says "roots **of rational numbers**". | p. 147 | minor |
| A3 | Exercises worth doing, Ex. 5A.13 and 5B.8 | 5A.13 says "with transformed eigenvectors", which gives away the answer to part (b). 5B.8 restates the book's printed hint ("degree ≤ 2, not $x^{180}+1$"). The book prints this hint, but repeating it removes the exercise's point. | pp. 140, 151 | minor |
| A4 | Questions | Q1 ("When does an operator have a basis of eigenvectors?") cites the chapter-intro promise of a basis with "almost half" zero entries (p. 132), which is a different property. Q3 drops "dimension at least two" from Ex. 5B.29. | pp. 132, 153 | minor |
| A5 | L3 after 5.19 and 5.34 | Two pointers are omitted: the comment after Ex. 16 explains why the fundamental theorem of algebra is tied to 5.19, and Ex. 8B.23 / 9C.10 give alternative proofs of 5.34. | pp. 143, 150 | minor (coverage) |

### B. Toy example and added steps (Python)
- 5.6: $T(3,1,-1)=(18,6,-6)$ ✓.
- 5.9: eigenvalues of the rotation over $\mathbf C$ are $\pm i$, and the eigenvector $(1,-i)$ for $i$ checks ✓.
- 5.26: solving (5.25) with $v=e_1$ gives $c=(3,-6,0,0,0)$, and $p(T)=0$ ✓.
- 5.28: the roots of $z^5-6z+3$ and the eigenvalues of $\mathcal M(T)$ are both $-1.67,\,0.51,\,1.40,\,-0.12\pm1.59i$ ✓.
- Toy example: $A=\begin{pmatrix}0&-2\\1&3\end{pmatrix}$. Then $A^2-3A+2I=0$, the eigenvalues are 1 and 2, $A(-2,1)=(-2,1)$, $A(-1,1)=(-2,2)$, and $\det=2$ ✓. The toy illustrates the main result (eigenvalues = zeros of the minimal polynomial) and uses the 5.25 method.
- There are no "(added step)" items.

### C. Coverage
All of §§5A–5B is covered in order, including every theorem, example and exercise-set summary. The six "Exercises worth doing" have correct numbers and pages and give no solutions (but see A3).

### D. Usefulness
The Prerequisites line is accurate. There is an intuition note after each major result, and they are good. No derivation exceeds ~10 steps, so no skip path is needed. The length (3,947 words) is under the target. This is the best of the four, and it can serve as a template for UG math chapters.

---

## 2. Cover & Thomas 1991, *Elements of Information Theory*, ch. 8 part 1 (printed pp. 183–202; scanned)

### A. Math and faithfulness
I checked every displayed equation from (8.1) to (8.81) against the scan. This covers the BSC chain (8.2)–(8.7), the BEC chain (8.8)–(8.16) including the order of arguments in (8.12), the symmetric channel (8.17)–(8.25), the definitions (8.26)–(8.34), the joint AEP (8.35)–(8.60), and the achievability proof (8.61)–(8.81). All copied equations are exact. These are also correct:
- the edition note (1991 1st ed., ISBN 0-471-06259-6, printed on p. 183);
- the offset (printed = pdf − 22, per `units.csv`);
- the observation that p. 194's "next section" promise is fulfilled in §8.7 step 3 (p. 202);
- the Fig. 8.3 probabilities.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| C1 | L3 §8.7 "Detailed calculation", and Reading notes bullet 4 | (8.66)–(8.68) are collapsed to one line with "equation text only partly legible in the image". Reading notes repeat "only partly legible". The scan is fully legible: (8.67) $=\sum_{\mathscr C}P(\mathscr C)\frac{1}{2^{nR}}\sum_{w}\lambda_w(\mathscr C)$ and (8.68) $=\frac{1}{2^{nR}}\sum_{w}\sum_{\mathscr C}P(\mathscr C)\lambda_w(\mathscr C)$. These two steps (expand $P_e^{(n)}$, then swap the sums) are what make the symmetry argument in (8.69)–(8.71) work. The result is a missing derivation step plus a false reading note. | p. 200 | **major** |
| C2 | L2, bullet 3 | "$I(X;Y)$ is concave in $p(x)$, so capacity is a finite maximum and a local maximum is global." Concavity gives only "local = global". The source derives finiteness from properties 2–3 ($C\le\log\lvert\mathcal X\rvert$, $C\le\log\lvert\mathcal Y\rvert$). L3 has it right. | p. 191 | minor |
| C3 | L3 §8.6, after (8.60) | "The step uses $I(X;Y)=H(X)+H(Y)-H(X,Y)$." This is not in the source and is not marked "(added step)". It is true. | p. 197 | minor |
| C4 | Concepts, `[[symmetric-channel]]` | "weakly symmetric: equal column sums". This drops "every row is a permutation of every other row", which L3 states correctly. | p. 190 | minor |
| C5 | L2 bullet 7; §8.1.4; §8.7 intro | Garbled verifier residue "(the codebook is the set of codewords)" in L2. Omitted: "Later we show that we can still use such a channel … at a non-zero rate with arbitrarily small probability of error" (p. 186), and the 8.7 framing ("perhaps the basic theorem", Shannon 1948, "not made rigorous until much later") (p. 198). | pp. 186, 198 | minor |

### B. Toy example and added steps (Python)
- $H(0.1)=0.46900$, $C=0.53100$, and the MI of the BSC under uniform input is 0.53100 ✓.
- (8.23): $\log 3-H(0.5,0.3,0.2)=0.09949$, which equals the MI under uniform input and the grid maximum ✓.
- (8.24): the column sums are all 2/3, and $C=\log3-H(\tfrac13,\tfrac16,\tfrac12)=0.12581$ equals the grid maximum ✓.
- (8.12) identity checked at two $(\alpha,\pi)$ pairs ✓. BEC with $\alpha=0.3$: grid maximum 0.700 at $\pi=0.5$ ✓.
- Added step $H(Y|X)=H(\alpha)$ ✓. Added step (8.78)→(8.79) via $2^{nR}-1\le2^{nR}$ ✓, checked numerically.
- Toy union-bound exponent $40-53.1+300\epsilon$ ✓.

### C. Coverage
§§8.1–8.7 are covered up to the cut-off. No exercises fall in these pages, so the section is correctly omitted.

### D. Usefulness
The Prerequisites line is fine. Two derivations exceed 10 steps but have **no "Skip path"**: the joint-AEP proof (8.42–8.60, about 19 steps) and achievability (8.61–8.81). Prompt rule 8 requires one. The heuristic intuition notes (packing, 2^{nI} candidates) are good. The length is 3,368 words against a target of about 2,950 (+14%), which is acceptable for dense math.

---

## 3. Blei, Kucukelbir & McAuliffe 2017, "Variational Inference: A Review for Statisticians", part 1 (pp. 1–21, arXiv v9)

### A. Math and faithfulness
I checked every equation (1)–(58) and Algorithms 1–2 against the images: indices, $\mathbf m_{-k}$/$\mathbf s^2_{-k}$, $\varphi_i^*$, transposes, and the $[\alpha_1+\dots,\ \alpha_2+n]^\top$ structure in (44), (48), (55), (57). All are exact. The following are also correct:
- the reported claims (VI vs. MCMC guidance, history, the model-selection quote, EM relation, footnotes 1–5, practicalities, the imageCLEF set-up of 192 × 3 = 576 dimensions, 30 clusters and two sets of 10,000 images, "orders of magnitude faster", "less than a minute");
- the Reading note on Fig. 6 (legend "NUTS (Hoffman et al. 2013)" vs. text "Hoffman and Gelman 2014"), which is real.

Voice tagging is good ("as the authors tell it", "authors' guidance").

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| B1 | L3 §1, §2.4, §3.4, §4.3 | For a high-school-level reader, these terms are used with no gloss: "ergodic Markov chain" and "stationary distribution" (§1), "Markov blanket" (§2.4), "Hamiltonian Monte Carlo"/NUTS (§1, §3.4, and Concepts without a definition), "held-out log predictive" (§2.5, §3.4), and "symmetrized KL" (§4.3). That makes 3 or more undefined terms. | pp. 2, 10, 11, 16, 20 | **major** (usefulness) |
| B2 | L3 §1 | The authors' general hedge is omitted: VI "has been studied less rigorously than MCMC, and its statistical properties are less well understood" (p. 2; abstract: "not yet well understood", p. 1). The narrower hedge "relative accuracy … is still unknown" is kept. | pp. 1–2 | minor |
| B3 | L3 §3.4 | "elbows … at about iterations 20, 28, 35 and 50". These are the snapshot panels of Fig. 3, not elbow locations. The ELBO curve is already flat at iteration 50. The Reading note discloses the source of the numbers, but the sentence still asserts them as elbows. | p. 15 (Fig. 3) | minor |
| B4 | L3 §2.3 first bullet | Eq. (15) is on p. 7, but the bullet ends "(p. 8)". The section header (pp. 7–9) covers it. | p. 7 | minor |

### B. Toy example and added steps (Python)
- Part A: evidence 0.5. ELBO −0.9163, KL 0.2231, sum −0.6931 = ln 0.5 ✓. Tight at $q$ = posterior ✓.
- Part B: both exponents equal −1.6094, and KL(product‖joint) = 0.2231 ✓. I also checked that the symmetric point is the unique CAVI fixed point from any start (0.01, 0.3, 0.9, 0.99 → 0.5), so the toy is not showing an unlucky local optimum.
- Added step for (34): natural-parameter matching. I verified numerically that the mean and variance of $\exp\{(\sum\varphi x)\mu-(1/2\sigma^2+\sum\varphi/2)\mu^2\}$ equal (34) ✓.
- Added step (53)→(54) ✓. Added step $\mathbb E_t[\hat g]=g$ ✓, checked numerically.
- Added step on the shapes ($\varphi$ is $n\times K$) ✓.

### C. Coverage
§§1–4.3 are covered in order, up to the topic-model paragraph on p. 21. Algorithm 3, §5 and the appendices are correctly noted as out of unit. There are no exercises.

### D. Usefulness
There is a skip path for §3.2 ✓, and the intuition notes are clear. The Prerequisites line lists KL and exponential families. For an HS-start reader it should also list "Markov chains (only for §1 context)". The length is 5,147 words against a target of about 5,580 ✓. The main gap is B1.

---

## 4. Ashby 1956, *An Introduction to Cybernetics*, ch. 11 "Requisite Variety" (printed pp. 202–218; 9 two-page spreads)

### A. Math and faithfulness
I checked the following:
- Tables 11/3/1, 11/4/1 and 11/5/1, cell by cell.
- The strategy $1\to\gamma,2\to\alpha,3\to\beta,\dots,9\to\alpha$ and its outcomes $k,k,k,\dots,l$.
- The proof steps in 11/5 and the $r/c$ statement.
- 11/6–11/7 and $V_O\ge V_D-V_R$.
- 11/8: $H_R(E)\ge H_R(D)$, the identity, and the substitution chain.
- 11/9, as printed: $V_O\ge V_D-\log k-\log V_R$; $H(D)-K-H(R)$.
- 11/10–11/21 claim by claim.
- The six exercises.
- The spread offset (pdf 108 = pp. 202–203 … pdf 116 = p. 218).

The misprint notes are **verified real** at 250 dpi: p. 208 prints "so $H(D)+H_D(R)\le H(R)+H_R(E)$" and "i.e. $H(E)\ge H(D)+H_D(E)-H(R)$"; Ex. 11/14/1 prints "Table 31/3/1". The digest's corrected final inequality, $H(E)\ge H(D)+H_D(R)-H(R)$, is mathematically right and is flagged. The voice handling is good: Hitler's control is tagged as common opinion, and the Sommerhoff mapping is hedged with "if I am not misinterpreting him".

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| S1 | L3 §11/13, "Value of the law"; Canonical instance `[[press-photographer]]` | "A photographer with twenty distinct subjects needs at least twenty camera settings." This drops the condition "**if all the negatives are to be brought to a uniform density and sharpness**". Without it, the claim is false. | pp. 212–213 | **critical** (dropped condition; low impact) |
| S2 | L3 §11/20 | "(ii) return within a minute if displaced by **+10°**". The image prints **±10°** (an underlined plus, which the text layer reads as "+"). | p. 217 | **critical** (wrong symbol; low impact) |
| S3 | L2 bullet 7; L3 §11/13 "Ashby's answer: variety arrives in two forms (p. 213)" and both sub-bullets | The natural-selection point, the two forms of variety, and "disturbance reaching the gene-pattern can be diminished only by the amount of information so transmitted" are all on **p. 212** (left half of spread pdf 113), not p. 213. | p. 212 | **major** (page ref) |
| S4 | L3 §11/11, "Time steps of any machine behind T are independent of the discrete steps" | The hedge is dropped: the source says "**essentially** independent". | p. 210 | major (dropped hedge; low impact) |
| S5 | Reading notes, OCR bullet | "'η' read as '17'" is called a text-layer OCR error. The page image itself prints "acceptable set 17" (p. 209), so it is a misprint in this typesetting. | p. 209 | minor |
| S6 | Concepts | `[[law of requisite variety]]` and `[[disturbance and noise]]` contain spaces, so they are not slug ids. | — | minor (format) |

### B. Toy example (Python)
- The table for $E=(D+R)\bmod 4$ is correct, and both columns are repeat-free ✓.
- Brute force over all $2^4$ strategies gives a minimum variety of 2, which equals $r/c=4/2$ ✓. The strategy giving $\{2,0\}$ ✓.
- The disjointness argument against variety 1 ✓.
- Source tables:
  - 11/3/1: R can force each of a, b, c ✓.
  - 11/4/1: R can force a, cannot force b or c, can force d (consistent with Ex. 1) ✓. The α column gives {a, b, d} (11/9) ✓.
  - 11/5/1: all columns are repeat-free. The brute-force minimum variety over $3^9$ strategies is 5 ≥ 9/3 ✓.

### C. Coverage
All of 11/1–11/21 is covered in order. Minor gap: 11/5 drops "Ex. 11/4/3 showed" as the reason for excluding columns with repeats (p. 204). The exercise numbers and pages are correct and no solutions are given.

### D. Usefulness
Level HS and the Prerequisites line are appropriate. The intuition notes are good: the 11/5 note gives a cleaner counting argument that is still faithful. The length is 4,159 words, which is **63% of the source** and +15% over the target. For a prose chapter, this nearly paraphrases every paragraph (11/15–11/21 could be halved). The page labels arrived as "?" (`units.csv` has no printed pages for Ashby), and the digest recovered them correctly from the spreads. But the spread layout is the likely cause of S3.

---

## Improvements (up to 3)

1. **Image re-check list for the verifier.** The verifier should re-crop the page image and re-read each of these, instead of trusting the text layer:
   - every ±, ≤/≥, minus sign and subscript in L3;
   - every claim that something is "unreadable", "partly legible" or a "misprint".

   It should reject "partly legible" unless the legible part is transcribed. This would have caught C1 and S2.
2. **Pre-split two-page spreads and fill `printed_pages`.** For spread scans, split each spread into half-images labelled with their own printed page (prompt rule 5 already assumes this). The verifier should also check the page ref of every L2 bullet whose content sits near a spread or page boundary. This would have caught S3, and it matters because several remaining books in the batch are spread scans.
3. **Lint in `checks.py`.** Add three checks:
   - (a) If L3 has more than ~10 consecutive display equations under one heading and no "Skip path", warn (Cover).
   - (b) Any sentence matching `\b(uses|step uses|follows from)\b` that is not in the source and has no "(added step)" tag should be flagged for review (C3).
   - (c) The digest must have a glossary-coverage pass that lists technical terms at their first use without a ≤15-word gloss or a `[[concept]]` link (B1).

   For dropped conditions in worked examples (S1), add each example's "if …" clause to the verifier's mandatory items.
