# Independent audit: math-heavy digests (Jaynes ch. 2, MacKay ch. 2, Vaswani 2017)

Auditor: Claude Opus 5.5 (did not write these digests). Date: 2026-10-13.
Ground truth: page images of `/home/claude/audit/{jaynes-ch02,mackay-ch02,vaswani}.pdf`, read in full (all 27 + 25 + 15 pages), plus `pdftotext` for string checks.
Recomputation: every worked number and toy example re-run in Python (script results summarised in each section).

Severity scale (as briefed): **critical** = wrong equation, number or statement, or a claim not in the source; **major** = wrong page ref, missing key step or result, dropped hedge; **minor** = notation or format.

## Summary

| Digest | Checks | Correct | Minor | Major | Critical | Toy example | Verdict |
|---|---|---|---|---|---|---|---|
| Jaynes ch. 2 | ~140 (104 numbered eqs, ~36 claims and refs) | ~131 | 6 | 2 | 1 | all correct | good after 3 fixes |
| MacKay ch. 2 | ~160 (≈105 numbered eqs, ~30 numbers, ~25 claims) | ~156 | 3 | 1 (systemic: every page ref) | 0 | all correct | good after page remap |
| Vaswani 2017 | ~200 (eqs, 4 tables cell by cell, ~30 hyperparameters, ~25 claims) | ~197 | 3 | 0 | 0 | all correct | good |

Overall, faithfulness is high. Equations, numbered references and table cells are almost all exact. The surviving errors are mostly in **L2 compressions** and in **"(added step)" glosses**, where the verifier seems to check less carefully than it checks L3 equations against the page. The biggest usability problems are not errors but spec gaps: undefined technical terms (Vaswani, Jaynes), full worked solutions that give away the recommended exercises (MacKay), and pdf-number page refs (MacKay).

---

## 1. Jaynes 2003, ch. 2 "The quantitative rules" (printed pp. 24–50)

### A. Math and faithfulness
I checked every displayed equation (2.1)–(2.107) symbol by symbol against the page images: subscripts, conditioning bars, negation bars, exponents ($w^r$, $[w(z)]^{r^2}$), domains ($0\le S(y)\le x$, $0<m<\infty$) and equation numbers. All numbered equations are correct. This includes the overline-heavy ones that the text layer drops: (2.38)–(2.43), (2.59), (2.65), (2.70), (2.76). I also confirmed the digest's own claims about source misprints with `pdftotext`. The missing ")" in (2.49) is real. "(2.25) becomes a functional equation" on p. 31 is a genuine misprint for (2.40). The unbalanced parenthesis in Ex. 2.2 is real.

I also checked the added derivation steps by hand. The glosses for (2.18), (2.20)/(2.21), (2.46) and (2.53) are correct. For (2.53), substituting $S(y)/x=1-e^{-(q+\alpha)}$ and $S(x)/y=1-e^{-q}$ gives $x e^{-J(q+\alpha)}=y e^{-J(q)}$, and so (2.53). The gloss for (2.57) is also correct: raising (2.56) to the power $m=1/b$ and rearranging gives $S^{m-1}dS+x^{m-1}dx=0$. I numerically confirmed that $S(x)=(1-x^m)^{1/m}$ satisfies the scaling equation (2.45) for $m=3$.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| J1 | L2, bullet "Sum rule from negation" | Says "The product rule must give the same value for $A\bar B$ and $B\bar A$." This is false: $w(A\bar B\mid C)\neq w(B\bar A\mid C)$ in general. Commutativity requires $w(AB\mid C)$, computed through (2.39), to be the same when $A$ and $B$ are swapped (2.40). The terms $A\bar B$ and $B\bar A$ only appear inside $S[\cdot]$. An L2-only reader learns a wrong identity. | p. 31 (2.40) | **critical** |
| J2 | L2, bullet "Comments" | "Gödel's theorem does not block this theory." Jaynes explicitly hedges. He writes "We are not prepared to answer this fully" (p. 45) and calls the consistency question "an open question" (p. 47). The L3 text keeps the hedge; L2 drops it. | pp. 45, 47 | major |
| J3 | L3, added step after (2.52) | "$S(x)S'[S(x)]/x=S(x)/(xS'(x))=e^{-\alpha}$ with the sign absorbed." Since $S'<0$, the quantity equals $-e^{-\alpha}$. Numerically, at $x=0.7$, $m=3$: $S/(xS')=-1.915$ while $e^{-\alpha}=+1.915$. The final (2.51) is right, but the stated equality is false, and a reader checking it will get stuck. | p. 32 | major |
| J4 | Reading notes, 4th bullet | Says that "C implies A" on p. 29 "should read C implies $\bar A$", and that "the same slip appears at (2.34)". The printed page already has the bar (p. 29, line after (2.33)), so this is only text-layer loss, not a source slip. It is also one sentence, not two. | p. 29 image | minor |
| J5 | L3 §2.6.2, Gödel bullets | Fisher (1956) is attached after (2.103). In the source, Fisher's remark refers to the earlier argument ("deducibility of T cannot prove consistency"). The hedge "We do not suppose that any logician would accept Fisher's simple argument as a proof of the full Gödel theorem" is dropped. | p. 46 | minor |
| J6 | L3 §2.2 Completeness | "Exercise 2.1 asks for a formula for $p(C\mid A+B)$." The source asks *whether* one exists ("If so, derive it; if not, explain why"). The Exercises section words it correctly. | p. 34 | minor |
| J7 | L3 after (2.39) | Verifier residue: "This equation is correct as printed. Its middle term follows from…" This is pipeline chatter inside the walkthrough. | — | minor |
| J8 | L2 "rules are complete" | $P(A+B\mid C)=P(A)+P(B)-P(AB)$ drops the conditioning $\mid C$. | p. 34 (2.66) | minor |
| J9 | L2 "Comments" | "Venn diagrams and Kolmogorov's axioms are special cases." Jaynes says (2.104) justifies the Venn diagram "in one special case". He says Kolmogorov's four axioms are all *derived* here, not that they are a special case. | pp. 49–50 | minor |

All other page references in L1–L3, Concepts and Instances are correct. I spot-checked 30, including 2.4 (p. 37–42), the policeman's syllogism (pp. 36–37), the Bernoulli urn (pp. 42–43), Ex. 2.3 (p. 43), the finite-sets policy (pp. 43–44) and Sam's thermometer (p. 49).

### B. Toy example (recomputed)
- $S(0.6)=0.8$ and $S(0.8)=0.6$ for $m=2$; $0.36+0.64=1$. ✓
- Die: $3/6+3/6-2/6=4/6$. ✓
- Weak syllogism: $P(A\mid BC)=0.4$, $P(B\mid\bar AC)=0.375$ computed both ways. ✓
- Indifference with $n=3$. ✓

The choice is excellent: part 1 shows concretely why $m$ is irrelevant.

### C. Coverage
Nearly complete: every section, every numbered equation, all three exercises (numbers and pages correct: 2.1 p. 34, 2.2 p. 34, 2.3 p. 43), and all examples (eyes, policeman, urn, penguins, raindrops, two witnesses). Small gaps:
- Desideratum (IIIb) is cited but never stated. (IIIc) is glossed.
- The remark that $S=S^{-1}$, hence $u=S(v)$ (the $A$/$\bar A$ symmetry, p. 31), is omitted.
- Footnote 1 (implication vs. logical deducibility, p. 45) is omitted, though it is what makes (2.102) meaningful.
- The 2.6 opening (two chapters to return to Laplace's (2.99)) is omitted. Trivial.

### D. Usefulness for a B2 / high-school-start reader
- At 4,170 words, L3 is a near-complete equation-by-equation transcription. That is excellent as a reading companion beside the book, but it is not a learnable ladder for someone starting at high-school level. The Cox derivation (2.14)–(2.27) needs partial derivatives and the idea of a functional equation. The sum-rule derivation (2.48)–(2.57) needs asymptotics and $O(\cdot)$ notation. Neither is introduced. There is no "skip path" telling the reader that the result matters more than the proof.
- Intuition notes for the product rule, sum rule, weak syllogism and indifference are short and correct. A note is missing for the hardest step: why the $S(1-\delta)$ asymptotics fix $S$.
- Undefined terms include functional equation, monotonic, Boolean algebra, basic conjunction, asymptotic, measure theory, group invariance and noninformative prior.
- Metadata: `fields: [information-theory]` comes from `units.csv`, but the catalog lists Jaynes under **bayesian**. As a result, spine concepts that already exist ("Cox's theorem", "Probability as extended logic", "Principle of indifference / maximum entropy", the instance "Jaynes's reasoning robot") are proposed as `(new)`.

---

## 2. MacKay 2003, ch. 2 "Probability, Entropy, and Inference" (printed pp. 22–46)

### A. Math and faithfulness
I checked every reproduced equation (2.1)–(2.113), including the solution equations (2.57)–(2.113), all numbers in Fig. 2.1 and Table 2.9 that the digest quotes, the Fig. 2.6 posterior table, the Ex. 2.20 table, and Box 2.4. **I found no equation or number error.** Difficult transcriptions are exact: (2.44), (2.62) with its λ values, (2.67), (2.89), (2.92)–(2.93), and (2.108)–(2.113) with the 2/6 case weights. The reading notes are accurate:
- The vowel sum is 0.311 exact versus 0.31 printed.
- No solutions are given for 2.8, 2.27, 2.30–2.33, 2.36 and 2.37.
- Shannon (1950) is described as making "numerical errors".

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| K1 | All page refs (~110) and frontmatter | Every reference uses pdf numbers of the full-book file (pdf 34–58) instead of the **printed** pages 22–46 that the spec requires. The printed numbers are clearly visible on every page image, with a constant offset of 12. Root cause: `units.csv` has `printed_pages` blank for this unit, so the "(pdf N)" fallback was used. The digest itself noticed the offset in its Reading notes but did not convert. Every reference is internally consistent, so a mechanical −12 remap fixes all of them. | every page; e.g. Jo's test is printed p. 25, cited "pdf 37" | **major** (systemic) |
| K2 | L2 last bullet | "This foreshadows typicality": an interpretation, not in this chapter's text, placed in a page-grounded L2 bullet. It is fine as a bridge, which the digest also has. | p. 37 | minor |
| K3 | L3 §2.8 Ex. 2.16 | Omits part (a)'s second question (the distribution of the absolute difference). | p. 36 | minor |
| K4 | Frontmatter `pages:` | Free-text sentence instead of a range, which will break any parser expecting `22-46`. | — | minor |

### B. Worked numbers and toy example (recomputed)
- Jo's test: 0.1610 → 0.16 ✓.
- Evidence $P(n_B=3\mid N=10)=0.0827$ → 0.083 ✓. The posterior table matches to 2 significant figures ✓. The prediction is 0.33304 → 0.333 ✓.
- Ex. 2.4/2.5: means 1 and 80, variances 0.8 and 64, sds 0.894 and 8 ✓. $P(z<1)=0.4096$ ✓; only $n_B=1$ gives $z<1$ ✓.
- Entropy of English letters: 4.109 ✓. $h(z)$ printed 10.4, recomputed 10.48 (a source rounding, faithfully copied).
- Ex. 2.13: $\log_2 3+\tfrac13\log_2 1050=4.930$ vs $\log_2 30=4.907$ ✓ (≃).
- Ex. 2.20 table ✓ (0.0199, 0.0956, 0.99996; 0.75, 0.999).
- Ex. 2.16: variance 35/12, 3500/12 = 291.7 ✓; the 6,6,6,0,0,0 die gives a uniform sum over 1–12 ✓.
- Ex. 2.21: 3 ✓.
- Zipf: $\sum p_n=1.000004$, $H=9.716$ → 9.7 ✓.
- Ex. 2.35: $P(r_1>6)=0.335$, $P(r_{tot}>6)=0.670$, mean $r_{tot}=11$ ✓.
- R3: the sum-rule expression equals $f^3+3f^2(1-f)$ (0.028 at $f=0.1$) ✓.
- Toy example: $H=1.75$ by both routes ✓. $D_{KL}(P\|Q)=0.2075$, $D_{KL}(Q\|P)=0.1887$ ✓.

### C. Coverage
Every section 2.1–2.10, all examples (2.1, 2.3, 2.6, 2.7, 2.9–2.13, 2.15) and every exercise 2.2–2.39 appear. The exercise numbers and pages in "Exercises worth doing" are correct relative to the pdf numbering (printed: 2.8 p. 30, 2.14 p. 35, 2.20 p. 37, 2.26 p. 37, 2.35 p. 38, 2.38 p. 39). The difficulty labels agree with MacKay's [2]/[3] ratings. Only trivia are missing: the White Knight remark, the notation note on |·|, the pointer to §8.1, and Fig. 2.5.

### D. Usefulness
- At 5,090 words, about 35% of L3 is a transcription of §2.10 Solutions. This **gives away the answers to the exercises the digest itself recommends** (2.14, 2.20, 2.26, 2.35, 2.38 are all solved in full in L3). The spec says "Do not solve them here" for the Exercises section, and the spirit of the spec applies to L3 as well.
- The intuition notes (base rate, marginalise rather than pick the best, entropy as average surprise, group plus within-group decomposition, Jensen) are good and correctly placed.
- The math ladder is the most followable of the three, because MacKay himself builds it gently. A few terms are undefined: binomial distribution, chi-squared, central-limit theorem, Lagrange multiplier, binary symmetric channel and R3.
- Metadata: as with Jaynes, the field is `information-theory` only, while the work is also in the **bayesian** catalog. Spine items such as "Bayes' theorem", "Likelihood", "Prior", "Posterior", "Marginal likelihood (evidence)", "Base-rate neglect" (which is exactly Jo's test), "Posterior predictive distribution" (the 0.333 prediction), "Typical set" and "KL divergence" were not linked, or were proposed as new.

---

## 3. Vaswani et al. 2017, "Attention Is All You Need" (arXiv v7, pp. 1–15)

### A. Math and faithfulness
I checked:
- Eq. 1, 2 and 3; the MultiHead and head$_i$ formulas; the shapes of $W^Q,W^K,W^V,W^O$; both PE formulas and the wavelength range; LayerNorm(x+Sublayer(x)); footnote 4; the separable-convolution cost.
- **every cell** of Table 1 (12 cells), of the reproduced rows of Table 2 (BLEU and FLOPs), of Table 3 (all 21 rows × PPL, BLEU and params), and of Table 4 (12 rows).
- all hyperparameters: $N=6$, 512, 2048, $h=8$, 64, Adam 0.9/0.98/$10^{-9}$, warmup 4000, $P_{drop}$ 0.1, $\epsilon_{ls}$ 0.1, 4.5M/37K, 36M/32K, 25K tokens, 0.4 s/100K/12 h, 1.0 s/300K/3.5 d, 5/20 checkpoints, beam 4, α 0.6, +50, TFLOPS 2.8/3.7/6.0/9.5, and for parsing 4 layers, 1024, 40K, 17M, 16K/32K, +300, beam 21, α 0.3.

**All correct.** The added steps are correct: the rotation argument for $PE_{pos+k}$, and the scaled score variance of 1. The reading notes about the source are verified: "41.0" in the text vs 41.8 in the table and abstract; [3] vs [31] cited for BPE; the misspellings "el al." and "BerkleyParser"; "three types of regularization" with only two headings.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| V1 | Reading notes, parsing "inconsistency" | Lists Dyer et al. (91.7, WSJ only) as an inconsistency with "better than all … except the Recurrent Neural Network Grammar". But Dyer et al. 2016 [8] *is* the RNNG (refs p. 11), so it is the stated exception. Only Luong et al. (93.0) is a genuine inconsistency. | pp. 10–11 | minor |
| V2 | Intuition note after Table 3 | "Dropout is the one regularizer whose removal clearly hurts (24.6 vs 25.8 BLEU)." Removing label smoothing also lowers BLEU (25.3 vs 25.8), though it improves PPL. The claim is overstated. | p. 9 Table 3 (D) | minor |
| V3 | Appendix, Figure 3 | "attend from 'making' to the distant word 'difficult'". The caption says "a distant dependency of the verb 'making', completing the phrase 'making…more difficult'", and the image shows heads on both "more" and "difficult". | p. 13 | minor |

### B. Toy example (recomputed)
- Scores 4, 2, −1 → 2, 1, −0.5; softmax 0.6897/0.2537/0.0566; output (0.7463, 0.3103) ✓.
- Unscaled weights: 0.8756/0.1185/0.0059 ✓. Masked weights: 0.7311/0.2689 ✓.
- LR: $512^{-0.5}=0.04419$; peak $6.99\times10^{-4}$; step 1000 gives $1.75\times10^{-4}$ ✓.

This is the best toy example of the three: it covers scaling, saturation and masking in one calculation.

### C. Coverage
All sections 1–7 and the appendix figures are covered, and no exercises exist (correctly omitted). Gaps:
- Table 2's Deep-Att + PosUnk rows are dropped. They are labelled "selected rows", which is acceptable.
- Figure 2 (block diagram including "Mask (opt.)") is not described.
- "Hyperparameters chosen on the development set" (p. 8) is omitted.
- No tensor-shape walk-through ($Q\in\mathbb R^{n\times d_k}$, $QK^T\in\mathbb R^{n\times n}$). This is the single most useful missing step, because it is where the $O(n^2d)$ in Table 1 comes from.

### D. Usefulness
- At 4,850 words for a 10-page paper, it is long, mostly because Tables 3 and 4 are reproduced in full. That is useful as a reference but heavy for a learner.
- **Spec violation: technical terms are not defined at first use.** Softmax, layer normalization, residual connection, ReLU, BLEU, perplexity, beam search, byte-pair/word-piece encoding, dropout, label smoothing, Adam, FLOPs and F1 are undefined. Only "transduction" and "anaphora resolution" are defined. For a B2 reader starting at high-school level this is the main barrier.
- The intuition notes (soft lookup, quadratic price for parallelism, residual refinement, attention maps are qualitative only) are good.

---

## Cross-cutting findings
1. **L2 is where errors survive.** Two of the three highest-severity Jaynes errors are L2 paraphrases (J1, J2). The L3 equations are almost perfect. The verifier appears to check equations against images, but not compressed prose against the L3 or the source.
2. **"(added step)" text is not verified as mathematics.** J3 is a sign error in an added gloss.
3. **Reading-note "source errors" are sometimes not errors** (J4, V1). Claims about misprints need the same image check as equations.
4. **Page-number fallback is too eager** (K1). Printed numbers were visible in the images, with a fixed offset.
5. **Field and spine linking**: multi-catalog works get one field, so existing spine concepts are re-proposed as `(new)`.

## Prompt and pipeline improvements (concrete)
1. **Add an L0–L2 claim audit to the verifier prompt.** "For each sentence in L0–L2, find the supporting L3 passage and source page. Flag any (a) equality, inequality or implication not stated in the source, (b) dropped hedge ('we suspect', 'not prepared to answer', 'open question', 'may'), or (c) interpretation without a marker. Rewrite or delete the sentence." This would have caught J1, J2 and K2.
2. **Verify added steps numerically.** "Every `(added step)` must be a literally true equation. The verifier substitutes one concrete numeric case (or uses python/sympy if available) and reports the check. Do not use wording like 'with the sign absorbed'; write the exact sign." This catches J3.
3. **Use the printed-page rule before the pdf fallback.** In `pages.py` and `units.csv`, infer the printed offset from running headers in the text or images whenever PDF labels are missing (MacKay: printed = pdf − 12). Add to the prompt: "If printed page numbers are visible in the page images and differ from the pdf numbers by a constant offset, cite printed numbers and state the offset once in Reading notes. Use `(pdf N)` only when no printed number is visible."
4. **Add a term-definition pass with a prerequisites line.** "Before finishing, list every technical term used in L1–L3. Each must have a ≤ 15-word plain definition at first use (or a `[[concept]]` link whose definition is in Concepts). Add one line `Prerequisites:` naming the math the L3 assumes (e.g. partial derivatives, $O(\cdot)$ notation, matrix shapes), and for derivations longer than 10 steps add a one-line 'skip path' saying which result to carry forward." This fixes the Vaswani and Jaynes usability gaps. For papers with matrices, add: "include the tensor shapes of the main computation."
5. **Use spoiler-safe solutions and full field context.** "When the source prints solutions, give only the final result in L3, and put derivations in a collapsible `<details>` block. Never print full solutions to exercises listed in 'Exercises worth doing'." In the planner, pass every catalog field a work belongs to (e.g. `[bayesian, information-theory]`) and all matching concept spines, and instruct: "prefer an existing spine concept over `(new)`; name the spine entry you matched." Also: strip verifier residue lines, and require misprint claims to cite the image check ("image shows …").

## Verdict
**Acceptable as a knowledge-base foundation, after a short repair pass.** Fix J1–J3 in Jaynes, remap MacKay page refs (−12) and fix its `pages:` field, and correct the V1 note. With these fixes the three digests are reliable sources for later posts on equations, numbers and tables. The remaining weaknesses concern teaching, not truth: undefined terms, no prerequisites or skip path for long derivations, and exercise spoilers in MacKay. Fix these in the prompt before the full batch, because a learner starting at high-school level needs them.
