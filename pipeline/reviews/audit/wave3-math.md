# Independent audit, wave 3: math and formal digests (MacKay ITILA ch. 4, Shannon 1948 part 1, Frank & Goodman 2012, Hernán & Robins ch. 7, Magnus et al. forall x ch. 22)

Auditor: Claude Opus 5.5. I did not write these digests. Date: 2026-10-14.
Pipeline under audit: Claude Sonnet 5.5, digest prompt v2.2 + verifier v2.2. All five digests are `verified: repaired`.
Ground truth: the page images of the five extracts in `/home/claude/audit/w3/`. I read every page: 24 + 28 + 10 + 18 + 7. I zoomed to 200 dpi on Hernán p. 97 to confirm the "it it" misprint.
Recomputation: inline Python (scipy). It re-ran every toy example and every "(added step)", plus these source numbers:
- the telegraph capacity 0.539;
- the equivocations .081 and .469;
- the Fig. 12b/12c capacities;
- the Fig. 11 capacity, by brute-force maximisation at p = 0.9 and 0.7;
- the MacKay h/H₂ table and the submarine terms;
- the Frank posteriors and the Hernán crude and standardized risks.

Page offsets and targets were checked against `pipeline/units.csv` and `pipeline/state/units.jsonl`.

Severity scale (as briefed; same as wave 2):
- **Critical:** a wrong equation, number or statement; a strengthened or weakened claim, including a dropped condition; a claim not in the source.
- **Major:** a wrong page ref; a missing key result; a dropped hedge; 3 or more undefined terms.
- **Minor:** notation, format, length, small coverage gaps.

"Low impact" marks an error that is real but unlikely to mislead a later post.

## Summary

| Digest | Checks (approx.) | Critical | Major | Minor | Toy / added steps | Length (words: digest; source / target) | Verdict |
|---|---|---|---|---|---|---|---|
| MacKay ITILA ch. 4 (pp. 66–89) | ~100 (eqs 4.1–4.55, Fig. 4.1 table, Ex. 4.6/4.7, Thm 4.1 proof both parts, submarine terms, 6 exercises, all solutions) | 1 | 3 | 5 | toy correct except one phrase (K6); added step correct | 4,978; ~12,100 / 6,000 (0.83×) | good after 1 fix |
| Shannon 1948, part 1 (pp. 1–28) | ~110 (every displayed equation pp. 1–28, Thms 1–12, the p. 6 tables, Examples 1–2, Figs 11–12, §17 code, App. 1) | 0 | 2 | 7 | all correct | 6,939; ~15,950 / 6,000 (1.16×) | very good |
| Frank & Goodman 2012 (pp. 1–10) | ~40 (Eqs 1–2, S1–S4, all statistics, N's, context types, ~25 claims) | 0 | 2 | 6 | all correct | 2,217; ~2,150 / 1,200 (**1.85×**) | good; too long |
| Hernán & Robins ch. 7 (pp. 91–108) | ~70 (all formulas incl. TP 7.3/7.4 proof steps, FP 7.1–7.4, Figs 7.1–7.15 read from images, ~40 claims) | 1 | 1 | 5 | all correct | 4,975; ~10,800 / 5,997 (0.83×) | very good after 1 fix |
| Magnus et al. ch. 22 (pp. 182–188) | ~35 (Tables 22.1–22.2 cell by cell, all definitions, footnote, 24 exercises, misprints) | 0 | 0 | 6 | correct | 1,863; ~1,980 / 1,200 (**1.55×**) | good; too long |

**Totals:** 2 critical, 8 major, 29 minor across 5 units.

**Estimate of surviving errors per unit:**
- **Critical:** about 0.4. Wave 2 had 1.0; wave 1 had 0.5.
- **Major:** about 1.6. If the "3 or more undefined terms" item is excluded, about 0.8 (3 of 5 digests).
- **Minor:** about 5.8.

**Every equation is faithful.** I checked every numbered and displayed equation symbol by symbol against the images. All of them match, including Shannon's §16 inverse-matrix system, MacKay (4.33)–(4.39), Frank S4 and Hernán's front-door proof. Two flagged notation choices are correct:
- Frank writes $r_s\to r_S$ and flags the change.
- MacKay omits the misprinted 0.0430 in (4.11) and flags it.

**Every toy example and "(added step)" recomputes correctly**, with one loose phrase in the MacKay toy (K6).

**Both critical errors are dropped conditions in L0 or L2. In both cases L3 is correct.** This is the same pattern as wave 2. In addition, three of the four non-glossary majors are dropped hedges ("might", "tend to") or dropped conditions.

**Verdict: OK to continue the batch.** Fix the 2 critical items and the 4 non-glossary majors listed at the end. Act on two process issues:
- **Length control fails on short units.** Frank is 1.85× its target and longer than its source; Magnus is 1.55×. The 1,200-word floor makes the target exceed the source's own length for both. The 1.3× check therefore leaves the summary nearly as long as what it summarises.
- **The glossary rule is still not enforced.** This is the fourth wave in a row.

---

## 1. MacKay 2003, *Information Theory, Inference, and Learning Algorithms*, ch. 4 "The Source Coding Theorem" (printed pp. 66–89)

### A. Math and faithfulness
I checked the following against the images:
- **Equations:** (4.1)–(4.55), symbol by symbol.
- **Tables and figures:** the Fig. 4.1 table (h, H₂ recomputed); Table 4.5; the Fig. 4.10 range (−37.3 to −65.9, −15.2, −332.1, H = 46.9).
- **Submarine:** (4.8)–(4.14) (log₂ 64/63 = 0.0227, 63/62 = 0.0230, 17/16 = 0.0874/5).
- **Wenglish:** 2¹⁵, 26⁵ ≃ 1.2×10⁷, 32/2048/2/128.
- **Examples:** Example 4.6 (15/16, δ = 1/16 → 2 bits) and Example 4.7.
- **Theorem 4.1 and its proof:** both parts, including β = ε and β = ε/2, and N₀ via σ²/(ε²N₀) ≤ δ.
- **Exercises and solutions:** the exercise list 4.9–4.20; the solutions to 4.2, 4.4, 4.5, 4.8, 4.13, 4.15, 4.17, 4.18 and 4.20.

All copied equations are exact. The reading notes on (4.11) "0.0430", the Fig. 4.14 caption (p₁ = 0.4, N = 100) and the 2Nβ vs $2^{\alpha\sqrt N}$ caveat are all real.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| K1 | L0 | "For N i.i.d. symbols … the number of bits needed … with any fixed error probability δ (0 < δ < 1) is close to NH, because almost all probability lies in a typical set of about 2^{NH} strings." The condition **"for N large / N > N₀"** is dropped. The chapter stresses the opposite for small N: "$H_\delta(X^N)$ depends strongly on the value of δ" (p. 76, Figs 4.6–4.8). The digest's own toy shows N = 2 giving 1, 0.79, 0.5, 0 against H = 0.469. L1, L2 and L3 all keep "large N". | pp. 76, 78 | **critical** (dropped condition in L0) |
| K2 | L3 §4.1, weighing problem, last bullet (and L2 bullet 2) | L3 says "The author's conclusion: the outcome of a random experiment **is guaranteed** to be most informative if its distribution is uniform." The source says "Thus **we might conclude**:", so the hedge is dropped. L2 bullet 2 turns "at each step of an optimal procedure" into the general "Informative experiments have outcomes as close to equiprobable as possible". | p. 70 | **major** (dropped hedge; low impact) |
| K3 | Questions, bullet 1 (also the §4.1 intuition note: "left to be explored later") | "The author promises to explore this but the question is **not answered in these pages**." On p. 68 the author says "We'll explore this question in detail **shortly**", and the chapter does: "the submarine example makes quite a convincing case for the claim that the Shannon information content is a sensible measure" (p. 72); "The preceding examples justify the idea…" (p. 73). The digest's own L3 reports both. So this is a false statement about what the source does. | pp. 68, 72, 73 | **major** (wrong characterization of the source, outside the summaries) |
| K4 | Whole digest (usefulness) | These terms are used without a gloss: convolution, Fourier transform, biexponential, central-limit theorem (Ex. 4.18); canonical ensemble, $k_B$, Gibbs entropy (Ex. 4.17); moment-generating function (named only); pigeon-hole principle; ASCII. The Prerequisites line covers none of them. | pp. 73, 86–88 | **major** (≥3 undefined terms) |
| K5 | L3 §4.8, Ex. 4.17 and Ex. 4.18 | Both are listed under "Exercises worth doing", but L3 reproduces their full worked solutions (Z = π, the convolution giving a width-2 Cauchy, the mean of N samples, the Fourier route; the microcanonical ↔ typical-set argument). Prompt rule 7 says "give only the final result". | pp. 87–88 | minor (spec) |
| K6 | Toy example, last sentence | "r ≈ 10 ± 3 holds **almost all** the probability." For Bin(100, 0.1), P(7 ≤ r ≤ 13) = 0.76 (±2 sd gives 0.97). This is our own numeric claim and it is overstated. | recomputed | minor (toy wording) |
| K7 | Concepts: `[[source coding theorem]]`, `[[typical set / AEP]]` | The canon defines these as **lossless** compression and "**roughly equiprobable**" sequences. MacKay's Thm 4.1 is **lossy** (failure probability δ), and he warns that equipartition holds "only in a weak sense". The concept lines do not flag the difference, as rule 10 requires. | pp. 74, 84 | minor |
| K8 | L2 bullet 3 | "In sixty-three and in submarine, the total information gained is log₂ of the number of hypotheses, however the outcomes unfold." This drops "**If we assume that all values of x are equally likely**" (sixty-three). | p. 70 | minor |
| K9 | L3 coverage | Omitted: the Wenglish/English point that a rare initial letter (z, "xyl…") identifies the word sooner than a common one ("pro…") (p. 73); the reduced-ASCII example that drops 17 rare characters (p. 75); and the remark that lossy compression is satisfactory for images (p. 74). | pp. 73–75 | minor |

Observation (not counted): Ex. 4.17's solution prints "fixing ln 1/P(x) to within $\epsilon k_BT$". By (4.50) this should be $\epsilon/k_BT$. The digest copies it faithfully and does not flag it.

### B. Toy example and added steps
- **Toy (N = 2, p₁ = 0.1):**
  - H = 0.469 ✓;
  - string probabilities 0.81, 0.09, 0.09, 0.01 ✓;
  - all four δ bands and the per-flip values 1, 0.792, 0.5, 0 ✓;
  - r = 10 at N = 100 gives log₂P = −46.9 = −N·H₂(0.1) ✓;
  - all-zeros −15.2, so P ≈ 2.7×10⁻⁵ ✓.

  It illustrates the main result (no flatness at small N). See K6 for the one loose phrase.
- **Added step (4.32):** combining $\bar x=\bar h$ and $\sigma_x^2=\sigma_h^2/N$ with (4.31) ✓.

### C. Coverage
- §§4.1–4.8 are in order, and all numbered equations are present.
- Weighing tree (Fig. 4.2): only the first weighing is transcribed, as disclosed.
- Exercises worth doing: 4.1, 4.9, 4.13, 4.15, 4.17 and 4.18. Numbers, pages and difficulties match the [rating] marks.

### D. Usefulness
- Glosses for i.i.d., Chebyshev, the weak law and Cauchy are good.
- Intuition notes are faithful, except the §4.1 note (K3).
- Length 0.83× target.

---

## 2. Shannon 1948, "A Mathematical Theory of Communication", part 1 (printed pp. 1–28)

### A. Math and faithfulness
I checked the following against the images:
- **Displayed equations:** every one on pp. 1–28, including:
  - the telegraph difference equation and determinant (expanded by hand to the μ-polynomial);
  - the p. 6 relations and all three p. 6 tables;
  - Theorems 1–12 (wording and conditions: "$q\neq0,1$", "$H\le C$", "$H>C$");
  - both proofs of Theorem 9, including $[(1-\delta)\frac TN+\delta\frac{T_1}N]^{-1}$;
  - Theorem 10 and its chain of inequalities;
  - the random-coding bound and its limit $1-2^{-T\eta}$;
  - §15 (U, both partials, P, Q, C);
  - §16 (the Lagrange equations, the inverse-matrix solution, $C=\log m+\sum p_i\log p_i$, Fig. 12a–c);
  - §17 ($\frac17[7+\frac88\log\frac18]=\frac47$, parity checks);
  - Appendix 1.
- **Recomputed:**
  - C = 0.5389 ✓;
  - $H_y(x)$ = .0808 ✓;
  - Fig. 12b = 0.0817 = $\log_2(2^{5/3}/3)$ ✓;
  - Fig. 12c = 0.1258 ✓;
  - Fig. 11 brute-force maximum = $\log\frac{\beta+2}\beta$ with $\beta=2^\alpha$, at p = 0.9 and 0.7 ✓;
  - the p. 6 digram table is consistent with $p(i)p_i(j)$ ✓.

All equations are exact. Voice handling is excellent: "Shannon says … in no way necessary", "alleged", "it appears", "probably". The reading notes on μ vs δ (p. 16) and $e^\alpha$ vs base 2 (p. 25) are real.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| S1 | L2 bullet 2; L3 Introduction, reason 1 | "Engineering quantities **grow linearly** with the log of the number of possibilities" / "**vary linearly**". The source says parameters of engineering importance "**tend to** vary linearly". The hedge is dropped in both L2 and L3. | p. 1 | **major** (dropped hedge; low impact) |
| S2 | Whole digest (usefulness) | These terms are used without a gloss: finite differences / linear difference equations (§1, App. 1), stationary / equilibrium conditions, ensemble average (§5), chance variable, Boltzmann's H theorem (§6), binary expansion (§9). The Prerequisites line covers none of them. | pp. 3, 10, 11, 17, 28 | **major** (≥3 undefined terms) |
| S3 | L3 §14, first bullet | "following it gives **no** practical code". The source says it is "**generally** impractical". | p. 24 | minor (slight strengthening) |
| S4 | L3 §14, second bullet | "Source redundancy left in the channel helps combat noise". This drops "**will usually help if it is utilized at the receiving point**". It also writes "a telegraph channel could save about 50%"; the source says a "**noiseless** telegraph channel". | p. 24 | minor |
| S5 | L3 §10, second bullet | "Good codes need long delay." This drops "**In general**, ideal or nearly ideal encoding requires a long delay". | p. 18 | minor |
| S6 | L3 §7, Theorem 4 | "For most purposes **there are** about $2^{HN}$ sequences". The source says "it is possible for most purposes to **treat** the long sequences **as though** there were just $2^{HN}$ of them". L2 and the intuition note phrase it correctly. | p. 14 | minor |
| S7 | L3 §5, mixed sources | "If (1) fails, the source is mixed". This drops Shannon's added assumption: "We will assume that the second condition is also satisfied for each subgraph." | p. 9 | minor (dropped condition in L3; low impact) |
| S8 | L3 §17 | "This corrects all errors and transmits at rate C (p. 28)". That claim is on p. 27. The source's "although somewhat unrealistic" is also omitted. | p. 27 | minor |
| S9 | Concepts | `[[huffman-arithmetic-coding]]`, `[[typical-set-aep]]` and `[[maximum-entropy-principle]]` name concepts that the paper does not name, but lack "(canon link; not stated in this unit)". The Huffman label is misleading for a Shannon–Fano-type code. | p. 17 | minor |

Observation (not counted): Example 2 (p. 19) prints "All numbers up to 16 are represented as usual; 16 is represented by … 17 = 10001". This is internally inconsistent, since 16 = 10000 already contains the special sequence. The digest copies it without a flag.

### B. Toy example and added steps
- **Toy:**
  - H = 1.5 ✓;
  - second-proof code: $P_s$ = 0, ½, ¾; $m_s$ = 1, 2, 2; codewords 0 / 10 / 11; average 1.5 ✓;
  - $3^{10}=2^{15.85}$ vs $2^{15}$ ✓;
  - BSC(0.1): $H_y(x)$ = 0.469, R = C = 0.531 ✓.

  It illustrates the main results: entropy, coding, and noisy capacity.
- **Added step 1 (§15):** $\beta=2^\alpha$ in base 2 ✓ (derived with base-2 derivatives).
- **Added step 2 (§15):** $H-H_y=-\log Q-\alpha=\log\frac{\beta+2}\beta$ ✓.

### C. Coverage
- Introduction, §§1–17, Appendix 1 and the start of Appendix 2 are all covered in order.
- The Fig. 9 description and the remark "at most a fraction √ε" are kept.
- Small omissions: "All the examples … above are ergodic" (p. 9), and "this redundancy … probably not a bad approximation to the ideal" (p. 24).
- There are no exercises, and the section is correctly omitted.

### D. Usefulness
- One intuition note per major result; all are faithful.
- Strong reading notes, including the scope of part 1.
- Length 1.16×, which is fine for the density.

---

## 3. Frank & Goodman 2012, "Predicting pragmatic reasoning in language games" (pdf pp. 1–10: main text, figure, Science SOM)

### A. Math and faithfulness
I checked the following against the images:
- **Equations:** Eq. (1); Eq. (2) with the definitions of $|w|$ and $W$; S1 (printed $r_s$); S2; $I_p(x)=-\log p(x)$; $I=-I_{\tilde w_C}(r_S)$; S3; S4, including the denominator index set.
- **Statistics:** r = .98, p < .001; r = .19, p = .40; r = .99, p < .0001; r = .87, p < .0001.
- **Sample sizes:** N = 745 / 206 / 276 / 263, and N = 20 / 24 (Fig. 1C).
- **Design:** the seven context types; "Fifty random trials … 6 unique numerical conditions".

All exact. The voice and hedges are kept: "perhaps because", "may lead", "Listeners may then use". The intuition note "the paper does not report a test of informativeness alone" is a model of restraint.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| F1 | L2 bullet 3 | "Speakers are modelled as rational … **With cost held constant**, this gives the 'size principle' … in proportion to 1/(number of objects)". S4 and Eq. 2 also need **α = 1**: S1 is $\propto e^{\alpha U}$, which gives $|w|^{-\alpha}$ in general. The bullet also needs the literal-listener definition of informativeness (S3). L2 bullet 6 and L3 state α = 1, which mitigates this. | pp. 9–10 (SOM pp. 2–3) | **major** (dropped condition in summary, partly restored in the next bullet) |
| F2 | Whole digest (usefulness) | These terms are used without a gloss: Luce choice rule, Bayesian decision theory, Boolean function, manipulation check, signalling games, referring-expression generation. The Prerequisites line covers none of them. | pp. 3, 9 | **major** (≥3 undefined terms) |
| F3 | Length | The digest has 2,217 words. The target is 1,200 (**1.85×**) and the source has ~2,150 words, so the digest is **longer than the paper plus SOM**. The prompt's 1.3× ceiling was not enforced. | — | minor (format; but see the verdict) |
| F4 | Page refs / Reading notes | The SOM is cited as pp. 9–10, but the images print "2" and "3" (pdf 8 prints "1"; the figure page has no number). The note "Printed page = pdf page for all pages" is contradicted by the images. The convention is disclosed, so a reader can map it. | pdf 8–10 | minor |
| F5 | Concepts | `[[Boltzmann (softmax) rationality]]` and `[[literal listener / pragmatic speaker / pragmatic listener]]` use terms the paper never uses (it says "Luce choice rule" and "literal interpretation"). They lack the "(canon link; not stated in this unit)" tag that the RSA line correctly has. | pp. 9–10 | minor |
| F6 | Toy example | "With a uniform prior, the normaliser is ⅓ + ½ = 5/6". In Eq. 1 the normaliser is $\sum P(w\mid r')P(r')$ = (⅓)(⅓ + ½) = 5/18. The posteriors 0.4 / 0.6 are right, because the prior cancels. | recomputed | minor |
| F7 | L2 bullet 6 | It cites "(pp. 9–10)" for "parameter-free", which is stated on p. 1 (the abstract). "So no parameter is fitted" is the digest's inference from α = 1 and constant D. | p. 1 | minor |
| F8 | L3 coverage | Omitted: "We posted a total of 900 individual trials" and the reposting rule (SOM p. 2); the Fig. 1B legend (points are mean bets per term or object per context type; the red line is the best linear fit; the bars are 95% CIs, p. 6). | pp. 6, 9 | minor |

### B. Toy example and added step
- **Toy:**
  - $P(\text{blue}\mid1)$ = ⅓, $P(\text{blue}\mid2)$ = ½, $P(\text{blue}\mid3)$ = 0 ✓;
  - uniform-prior posterior 0.4 / 0.6 / 0 ✓;
  - salience prior (0.6, 0.2, 0.2) gives ⅔ / ⅓ / 0 ✓.

  It illustrates the main idea (informativeness × salience), with a reversal.
- **Added step (S4 → Eq. 2):** $e^{-(-\log x)}=x$, and a constant D cancels ✓ (valid with α = 1, as stated).

### C. Coverage
- Introduction, model, experiment, Methods and the SOM derivation are covered in order.
- The p. 7 figure image was not provided to the pipeline, and the reading note says so. The pipeline should check why the image was not sent.

### D. Usefulness
- Faithful and careful, with good intuition notes.
- The main defect is length: L3 almost restates the paper.

---

## 4. Hernán & Robins, *Causal Inference: What If* (online revision 2026-08-19), ch. 7 "Confounding" (printed pp. 91–108)

### A. Math and faithfulness
I checked the following against the images:
- **Formulas:** the standardization formula; the backdoor criterion and Technical Point 7.1 (sufficiency without faithfulness; the converse under FFRCISTG; NPSEM-IE counterexample A→L, A→Y); the four Fine Point 7.2 identifying formulas.
- **Fine Point 7.1:** 0.6 → 0.7; the sign rule and its "may fail" caveat.
- **Technical Point 7.2:** both replacement conditions.
- **Technical Point 7.3:** the equi-confounding assumption and the DiD formula.
- **Technical Point 7.4:** the front-door formula and all four proof steps.
- **Figures:** every DAG structure (Figs 7.1–7.15) read from the images, including Fig. 7.7 (A→L←U→Y) and Fig. 7.11 (A→L→Y, U→A, U→L).
- **Misprint:** "because it it arises" (p. 97), confirmed at 200 dpi.

All formulas are exact. The hedges are mostly kept: "may be confounded", "quite generally", "under some weak conditions", "may result", "a matter of taste". The NPSEM-IE/FFRCISTG voice is handled well.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| H1 | L2 bullet 4 | "**Confounding is absolute, 'confounder' is relative.**" This drops the source's condition: "**Given a causal DAG**, confounding is an absolute concept whereas confounder is a relative one". Without it the bullet also contradicts p. 98, where under the alternative definition "the existence of confounding depends on the method of analysis". L3 and the Concepts line keep the condition. | pp. 98, 100 | **critical** (dropped condition in summary; low impact) |
| H2 | Prerequisites / whole digest | The prerequisites "gloss" faithfulness and FFRCISTG only as "assumptions about the causal model", which is not a definition. Also unglossed: NPSEM-IE and "cross-world independencies" (TP 7.1), noncollapsible effect measures (p. 100), nondifferential misclassification (FP 7.3), pseudo-population. | pp. 94, 100, 103 | **major** (≥3 undefined terms) |
| H3 | L3 TP 7.3 | "It is restrictive". The source says "a **somewhat** restrictive approach". | p. 106 | minor (slight strengthening) |
| H4 | L0 | Two sentences; the spec asks for one. | — | minor (format) |
| H5 | L2 bullet 3 | It cites "(p. 97)" for Figures 7.4 **and 7.7**. Fig. 7.7 and its discussion are on p. 99. | p. 99 | minor |
| H6 | L3 FP 7.3 and TP 7.2 (coverage) | Omitted: "if L were perfectly correlated with U then it would make no difference whether one conditions on L or on U" (p. 100); "The variables in $U_1$ may be associated with … $U_2$. $U_1$ can always be chosen to be the largest subset of U that is unassociated with treatment" (p. 101); and the EEG aside on measuring the natural value of treatment (p. 102). | pp. 100–102 | minor |
| H7 | L3 FP 7.3 | Fig. 7.8 is described as "$L\leftarrow U\to A$, $U\to Y$". The image also has **A→Y**. | p. 99 | minor |

### B. Toy example
- **Toy (null effect, binary L):**
  - Pr[A = 1] = 0.5; Pr[L = 1 | A] = 0.8 / 0.2 ✓;
  - crude risks 0.52 / 0.28, RR = 1.857 ✓;
  - standardized risks 0.4 / 0.4, causal RR = 1 ✓.

  It illustrates the main result: confounding through a backdoor path, removed by adjusting for a sufficient set.
- There are no added steps.

### C. Coverage
- §§7.1–7.6, FP 7.1–7.4 and TP 7.1–7.4 are all covered. The boxes are placed near their first use and their page refs are given.
- There are no exercises, and the section is correctly omitted.
- The reading notes are accurate (offset pdf − 9; p. 108 blank; revision warning).

### D. Usefulness
- The table of examples in §7.1 and the step-numbered front-door proof are excellent.
- Intuition notes are faithful.
- Length 0.83×.

---

## 5. Magnus, Button et al., *forall x: Calgary* (2025), ch. 22 "Soundness and completeness" (printed pp. 182–188)

### A. Faithfulness
I checked the following against the images:
- **Table 22.1:** all 7 rows × 2 definitions (p. 184, rotated).
- **Table 22.2:** all 6 rows × 2 columns.
- **Definitions:** inconsistent sentence; proof-theoretic contingency; inconsistent / consistent set; provably valid; footnote 1 ("A ⊢ ⊥ iff ¬A is a theorem").
- **Soundness and completeness:** the definitions; "generally harder"; "not the case for all proof systems or all formal languages".
- **The method-choice argument:** contingency and non-equivalence.
- **Exercises:** all 24 (A.1–12, B.1–12), and the six picks with their pages.
- **Misprints:** all four (B.12 parentheses, "can chose", the missing full stop, "Not only could show"), all real.
- **Offset:** printed = pdf − 10 ✓.

There are no faithfulness errors. Hedges ("practical", "generally harder", "simply isn't possible" for proofs) and the voice are kept.

**Surviving errors**

| # | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| G1 | Length | The digest has 1,863 words. The target is 1,200 (**1.55×**), which is 0.94× the source. For a 7-page chapter whose last 2½ pages are exercises, the digest nearly restates it. | — | minor (format) |
| G2 | L2 bullets 2–3 | Two bullets make the same point (contingency and consistency are defined negatively; no finite derivation test). | p. 183 | minor |
| G3 | Intuition note after Table 22.2 | "A single success settles a positive claim … A truth-table line can also be one." This is the digest's own generalization, and it is imprecise. Contingency needs **two** lines. Inconsistency ("consistency absent") is settled by a derivation. | p. 187 | minor |
| G4 | Undefined terms | "TFL" is never expanded. "Entailed / entailment" (soundness sketch) and "main connective" (Table 22.1) are unglossed. The Prerequisites line covers the rest (valuations, ⊢, ⊨, ⊥), so this falls just below the major threshold. | pp. 184–185 | minor |
| G5 | L1 | "Chapter 20 used ⊢ for derivations and ⊨ for truth tables." The source says that ch. 20 "started using the single turnstile the same way we used the double turnstile". ⊨ predates ch. 20. | p. 182 | minor |
| G6 | L3 coverage | Omitted: "We have also already given proof-theoretic definitions for theorems and pairs of interderivable sentences" (p. 183), and the gloss "everything that we can prove using derivations could also be proven using truth tables" (p. 185). | pp. 183, 185 | minor |

Observation (not counted): L1 says "Full proofs are beyond the book". The source says this too (p. 185), yet it also points to ch. 48 for the soundness proof "worked out". This is a source-side tension, and the digest does not flag it. The last reading note ("written loosely for a single premise") is editorial, not a source error.

### B. Toy example
- P∧Q vs Q∧P: columns T, F, F, F both ✓; interderivable ✓.
- P∧Q vs P∨Q differ at (T, F) ✓.

The toy illustrates the main result (verdicts agree) and Table 22.2.

### C–D. Coverage and usefulness
- Complete and in order.
- The exercise picks are well chosen (A.2, A.5, A.8, A.9, A.12, B.7).
- The concept line for `[[validity / soundness]]` correctly flags the difference from the canon's meaning (sound proof system vs sound argument).

---

## Fixes to apply (critical first)

1. **K1 (MacKay L0):** insert "for large N". For example: "For a long string of N i.i.d. symbols (N large), the number of bits … is close to NH …".
2. **H1 (Hernán L2 bullet 4):** "**Given a causal DAG**, confounding is absolute and 'confounder' is relative."
3. **K2 (MacKay):** restore "we might conclude". In L2 bullet 2, say "at each step of an optimal weighing procedure".
4. **K3 (MacKay):** delete "the question is not answered in these pages". Replace it with: "The author answers informally through the examples (pp. 72–73). What would a formal justification look like?"
5. **S1 (Shannon):** restore "tend to vary linearly" in L2 bullet 2 and in L3.
6. **F1 (Frank L2 bullet 3):** "With constant cost and α = 1, this gives …".
7. **Length:** trim Frank to ≤ 1,560 words and Magnus to ≤ 1,560 words. Cut restated prose in L3, not the math.
8. **K5:** reduce the Ex. 4.17 and 4.18 solutions in L3 to their final results.
9. **Glossary:** K4, S2, F2, H2 (and G4): add ≤ 15-word glosses at first use, or extend the Prerequisites lines.

## Improvements to the pipeline (up to 3)

1. **Add a "conditions" diff for L0–L2.** This repeats the wave-2 recommendation 1, which has not yet taken effect. For each L0/L1/L2 sentence, the verifier should extract from the cited L3 passage:
   - quantifier conditions ("for large N", "given a causal DAG", "α = 1");
   - hedges ("might", "tend to", "generally", "somewhat", "in general").

   It should then fail the sentence if any of them is missing. Every critical error and four of the eight majors in this wave are of this kind.
2. **Enforce the length ceiling against the source, not only the target.** For short units the 1,200-word floor gives a target near or above the source length (Frank: target 1,200 for a 2,150-word source). Two changes:
   - make the ceiling min(1.3 × target, 0.6 × source words);
   - make a breach a hard repair trigger, not a pass.
3. **Run a meta-claim and exercise-solution lint.**
   - Any sentence that says what the source does not do ("not answered", "not proved here", "only mentioned") must quote the page that shows the absence (K3).
   - Any exercise listed under "Exercises worth doing" must not have more than one sentence of solution in L3 (K5).
