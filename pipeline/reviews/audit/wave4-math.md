# Independent audit, wave 4: math and formal digests (Sutton & Barto ch. 9 pt 2, McElreath ch. 6 pt 2, Strogatz ch. 7 pt 2, Shannon 1951, Xie et al. 2022)

Auditor: Claude Opus 5.5. I did not write these digests. Date: 2026-10-14.
Pipeline under audit: Claude Sonnet 5.5, digest prompt v2.2 + verifier v2.2, all five `verified: repaired`. **In this wave the length target was lowered.**
Ground truth: the page images of the five extracts in `/home/claude/audit/w4/`. I read every page: 21 + 23 + 27 + 15 + 28 (Xie pp. 13–15 are references and were skipped).
Recomputation: inline Python (scipy). It re-ran every toy example and every "(added step)", plus these source numbers:
- McElreath: −2(12.34189 − 4.860017) = −14.9637; P(N(6.7, 7.26) < 0) = 0.178.
- Shannon: Σ.1/n cutoff and Σ p log p for the Zipf estimate; 4.5/5.5 = .818.
- Xie: 56% gap closure, (70.7 − 69.8)/(71.4 − 69.8) = 0.5625.
- Strogatz: the sign of (37) re-derived from (35)–(36); identity (38); (42) from (40); (55) solved in closed form.

Targets come from `pipeline/state/units.jsonl`.

Severity scale (as briefed; same as waves 2–3):
- **Critical:** a wrong equation, number or statement; a strengthened or weakened claim, including a dropped condition; a claim not in the source.
- **Major:** a wrong page ref; a missing key result; a dropped hedge; 3 or more undefined terms.
- **Minor:** notation, format, length, small coverage gaps.

"Low impact" marks an error that is real but unlikely to mislead a later post, usually because L3 states the point correctly.

## Summary

| Digest | Checks (approx.) | Critical | Major | Minor | Coverage of L3 | Toy / added steps | Length (digest; source / target; ×target) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Sutton & Barto ch. 9 pt 2 (pp. 222–242) | ~75 (9.19–9.26, LSTD box line by line, Ex. 9.4 numbers, Figs 9.14/9.15 numbers, ~45 claims incl. bibliography) | 1 | 3 | 7 | complete (all of §9.5.5-end to §9.12, Ex. 9.5–9.8, bibliography) | all correct | 4,513; 10,141 / 4,259 (1.06×) | good after 1 fix |
| McElreath ch. 6 pt 2 (pp. 186–207) | ~95 (all formulas, Fig. 6.10 gaps, `compare` table 28 cells, `coeftab` 16 cells, R outputs, ~40 claims) | 2 | 2 (+1 catalog) | 6 | complete (§6.3–6.7 and every box) | all correct | 4,791; 11,115 / 4,668 (1.03×) | good after 2 fixes |
| Strogatz ch. 7 pt 2 (pp. 217–243) | ~90 (eqs (1)–(57) symbol by symbol, sign of (37) re-derived, (54) averages, every exercise number/page cited) | 0 | 1 | 5 | complete (all of §7.6; exercises listed) | all correct | 3,145; 10,920 / 4,586 (**0.69×**) | very good |
| Shannon 1951 (pp. 50–64) | ~80 (eqs (1)–(21), Table I row 1, bounds table 32 values, reverse table 18 values, Fig. 3, Zipf numbers) | 1 | 2 | 4 | complete (§§1–6) | all correct | 4,454; 6,375 / 2,678 (**1.66×**) | good; too long |
| Xie et al. 2022 (pp. 1–31) | ~110 (eqs (1)–(118), A1–A5, Thms 1–3, Lemmas 1–2, Props 1–2, Fig. 6 table, Table 1, appendix settings) | 0 | 2 | 4 | complete (§§1–6, App. A–F) | all correct | 4,627; 13,937 / 5,854 (0.79×) | very good |

**Totals:** 4 critical, 10 major (plus 1 catalog major not charged to a digest), 26 minor across 5 units.

**Estimate of surviving errors per unit:**
- **Critical:** 0.8. All four are low impact, and in every case L3 is correct.
- **Major:** 2.0. If the glossary item is excluded, 1.0.
- **Minor:** 5.2.

**Equations.** Every displayed equation I checked matches the image, symbol by symbol. The digests caught, and correctly flagged, four source problems:
- Strogatz (37)/(39): a sign misprint. I re-derived it. Substituting (36) into (35) gives the opposite overall sign. Conditions (40)–(41) are unaffected, as the digest says.
- Strogatz (49): the stray $\cos(t+\phi)$.
- Strogatz p. 227: the missing ¼.
- Shannon (18): the missing minus sign.

The digests also correctly flagged:
- Xie's unproved step (76) "≥ 1/c₄";
- the "<" in (93);
- the cubic term absorbed in (109);
- the `L_CE` missing its sum over y.

**Toy examples and added steps.** All five toy examples and every "(added step)" recompute exactly. These are:
- the LSTD inverse updates;
- the WAIC/lppd/variance arithmetic and the Akaike weights;
- the damped-oscillator averaging;
- the rank-frequency bounds 1.151 ≤ F ≤ 1.485;
- the concept-posterior 0.833 and the $1.5\cdot0.8^k$ threshold;
- the Ex. 9.4 emphasis sequence;
- Shannon's Fig. 3 rectangle masses;
- Xie's E.1 "θ ∈ B ⇒ KL sum ≤ ε".

**Coverage.** No key result is missing from any digest. The lower target did **not** cost content:
- **Strogatz (0.69× target)** keeps every numbered equation (1)–(57) except the trivial substitution (8). It keeps all four examples, the averaged-equation table and the validity rule. It reached its target by listing the 14 pages of exercises instead of summarising them.
- **Xie (0.79×)** keeps every theorem, lemma, proposition and appendix step.
- **Shannon** went the other way. At 1.66× target and 70% of its source's length, it breaks the 1.3× cap.

**Pattern.** As in waves 2–3, every critical item is a dropped or added condition in a summary-level line (L0, L2 or Concepts), and the L3 statement is correct. There are three such cases:
- Sutton L2: memory-based methods called "local".
- McElreath L2 and Concepts: "AIC needs flat priors".
- Shannon L0: bounds from human guesses.

The fourth critical item is a misdescribed interval in McElreath L2. The glossary rule ("≥ 3 undefined terms") failed in 4 of 5 digests. **This is the fifth wave in a row.**

**Verdict: OK to continue the batch.**
- Fix the 4 critical items and the 6 non-glossary majors listed in the fix list at the end.
- **Pipeline issues:**
  - (a) The `mcelreath-2020-rethinking` source PDF is the **1st edition** (2015) of the book, not the 2nd (2020). The catalog and work id say 2nd edition (§1.3).
  - (b) For Shannon, only 9 of 15 page images were sent to the digester. Its Reading notes say so and it "reconstructed" (10), (14), (15), which are printed legibly. The reconstructions happen to be right.
  - (c) The length cap is not enforced after the verifier repair. Shannon is 1.66×.

---

## 1. Sutton & Barto 2018, ch. 9 "On-policy Prediction with Approximation", part 2 (printed pp. 222–242)

### A. What I checked
- **Equations against the images:** (9.19)–(9.26) and the TD fixed point $\mathbf A,\mathbf b$. Sherman–Morrison (9.22), including the denominator $1+(\mathbf x_{t-1}-\gamma\mathbf x_t)^\top\widehat{\mathbf A}^{-1}_{t-1}\mathbf x_{t-1}$. The LSTD box line by line ($\mathbf v\leftarrow\widehat{\mathbf A^{-1}}^\top(\mathbf x-\gamma\mathbf x')$, etc.).
- **Numbers:** Ex. 9.5 (7 × 8 = 56, C(7,2) = 21, 98 tilings); Fig. 9.14 (4 in / 2 out / 2 hidden); Fig. 9.15 (6 maps 28×28, 5×5 fields, overlap 4, 25 weights, 2×2 subsampling → 6 maps 14×14); Ex. 9.4 ($\mathbf w_\infty$ = (3.5, 1.5), (4, 2)).
- **Claims and bibliography:** about 45 claims, with modal strength checked; bibliography attributions (Widrow & Hoff 1960, Sutton 1988, Dayan 1992, Tsitsiklis & Van Roy 1997, Konidaris 2011, Hinton 1984, Albus 1971/81, Broomhead & Lowe 1988, Bradtke & Barto, Sherman & Morrison 1949, Atkeson et al. 1997, Bentley 1975, Aizerman et al. 1964, Samuel 1959/67, Holland 1986).
- **Recomputation:**
  - The (added step) $M_0..M_3 = 1,0,1,0$ is correct (n = 2, γ = 1).
  - Toy: $\widehat A^{-1}$ = 10 → 0.909 → 0.476, w = 0.909, 0.952, $t/(t+0.1)$. All correct.
- **Format:** L1 has 100 words; L2 has 7 bullets. Offset printed = pdf − 22 is correct.

### B. Coverage
| Source item | In L3? |
|---|---|
| §9.5.5 end (RBF smoothness, RBF networks) | yes |
| §9.6 step-size, (9.19), Ex. 9.5–9.6 | yes (the tabular α = 1/10 → 10 experiences numbers are dropped; minor) |
| §9.7 ANN structure, UAT, deep hierarchy, backprop, overfitting, dropout, DBN, batch norm, residual, convnets (Figs 9.14–9.15) | yes |
| §9.8 TD fixed point, (9.20)–(9.22), cost, box, ε/forgetting caveats | yes |
| §9.9 parametric vs memory-based, NN / weighted avg / LWR, curse of dimensionality, k-d trees | yes |
| §9.10 kernel, (9.23), RBF kernel vs RBF net, (9.24), kernel trick | yes |
| §9.11 interest, emphasis, (9.25)–(9.26), MC case, Ex. 9.4 | yes |
| §9.12 summary incl. convergence-bound statement | yes |
| Ex. 9.7–9.8, Bibliographical remarks | yes (compressed) |

### C. Findings

**S1. Critical (low impact). L2 bullet 5 (line 32): memory-based methods called "local".**
- **Problem:** The bullet says memory-based methods "are nonparametric and local".
- **Evidence:** p. 231 says there are "many different memory-based methods"; "Here, we focus on local-learning methods". The unit's own kernel regression (§9.10, p. 232) is memory-based but averages over "*all* examples stored in memory".
- **Consequence:** The bullet turns a subclass property into a property of the class. L3 (line 121) is correct.
- **Fix:** "...are nonparametric; the local-learning ones avoid exponential memory..."

**S2. Major (low impact, dropped hedge). L3 §9.7, line 69: "It works well for shallow nets (1–2 hidden layers)".**
- **Evidence:** p. 225: "The backpropagation algorithm *can produce* good results for shallow networks having 1 or 2 hidden layers".

**S3. Major (low impact, dropped hedge). L3 §9.7, line 81: "This makes responses spatially invariant".**
- **Evidence:** p. 228: subsampling layers "reduce the network's sensitivity ... that is, they *help make* the network's responses spatially invariant".

**S4. Major (glossary). Several technical terms are used without a definition at first use or in Concepts:**
- **GPI** (line 114);
- **VE / VE(9.1)** (line 150; only "ranks approximations" on line 166);
- **bootstrap / bootstrapping** (lines 160, 169);
- **Monte Carlo / gradient MC** (lines 157, 159);
- **stochastic-approximation conditions (2.7)** (line 44).

**S5. Minor. Reading notes line 237 and L3 line 167: the n = ∞ / n = 1 values.**
- **Problem:** The reading note says it "cannot confirm from the text layer which value goes with which method". As a result, L3 omits "n = ∞ and n = 1 respectively".
- **Evidence:** The p. 236 image plainly reads "when n=∞ and n=1 respectively". The prompt forbids treating an equation as unreadable because the text layer is garbled.

**S6. Minor. Line 150: "one means full care".**
- **Evidence:** p. 234: "if we fully care, it *might* be one".

**S7. Minor. Line 114: half of the source's evaluation is dropped.**
- **Evidence:** p. 229: "This is sometimes desirable, but it is problematic...". The digest keeps only "problematic".

**S8. Minor. Line 55: the Ex. 9.6 pointer drops a condition.**
- **Problem:** It omits the condition $\mathbf x(S_t)^\top\mathbf x(S_t)=\mathbb E[\mathbf x^\top\mathbf x]$. The full condition is given in "Exercises worth doing" (line 230).

**S9. Minor. Line 63: "complex AI functions" for "the complex functions needed for many AI tasks" (p. 224).**
- **Problem:** "many" is dropped.

**S10. Minor. Line 127: forgetting methods presented as a requirement.**
- **Problem:** The digest says locally weighted regression "needs ... methods for forgetting entries".
- **Evidence:** p. 232 lists forgetting among the "many ways" researchers developed. It is not a requirement.

**S11. Minor. L0 (line 20): contradictory wording.**
- **Problem:** "Beyond hand-set linear SGD, ... can use step-size rules of thumb". The step-size rule of thumb *is* a hand-setting rule (§9.6 "Selecting Step-Size Parameters Manually").

---

## 2. McElreath, *Statistical Rethinking*, ch. 6 "Overfitting, Regularization, and Information Criteria", part 2 (printed pp. 186–207)

### A. What I checked
- **Formulas:** the example model (p. 186); AIC; the three AIC conditions; DIC and $p_D$; lppd, $V(y_i)$, $p_{\rm WAIC}$, WAIC; the Akaike-weight formula. All match the images.
- **Figures:** Fig. 6.10 gaps (2, 4.1, 5.3, 7.6, 9.7 / 1.9, 4.1, 4.9, 7.1, 8.5) and Fig. 6.8/6.9 priors.
- **R output:** cars output 421.0367 and 14.42941; `WAIC(m6.14)` (−14.96375, 12.34189, 4.860017, 7.582438).
- **Tables:** the `compare` table (all 28 cells) and `coeftab` (all 16 cells, nobs = 17); 17 rows × 9 columns.
- **Simulation and practice:** 0.1773; counterfactual grid 0.5–0.8 × 30, mass 4.5; Tippecanoe facts; 6H split (272 rows each), polynomial M1–M6, Normal(0, 5) priors.
- **Recomputation:**
  - The added check −2(12.34 − 4.86) = −14.96 is correct.
  - Toy: lppd −2.1203, V = 0.3087/0.6764, $p_{\rm WAIC}$ 0.9851, WAIC 6.21, weights .731/.269. All correct.
- **Reading notes:** the "only 12 cases" inconsistency (17 rows) and the 2$p_{\rm WAIC}$ reading are both correct.
- **Format:** L1 has 100 words; L2 has 8 bullets. Offset pdf − 14 is correct.

### B. Coverage
| Source item | In L3? |
|---|---|
| §6.3 regularizing priors, model, Figs 6.8–6.9, N = 20 / 100, tuning, cross-validation; boxes on multilevel and ridge | yes |
| §6.4 Fig. 6.10, AIC + 3 conditions, DIC/WAIC intro; consistency box | yes |
| §6.4.1 DIC; §6.4.2 WAIC, time-series caveat, BIC box, WAIC-calculation box | yes |
| §6.4.3 Fig. 6.11, complementarity; diverse-frameworks box incl. uniformitarian/town example | yes |
| §6.5 selection vs comparison vs averaging | yes |
| §6.5.1 data, same-observations rule, m6.11–6.14, log σ trick, `compare`, plot, Akaike weights + interpretation, 0.1773, conclusions/masking; significance and metaphor boxes | yes |
| §6.5.1.2 `coeftab`, Fig. 6.12, dotchart box | yes |
| §6.5.2 ensemble procedure, Fig. 6.13, "always conservative"; Tippecanoe box | yes |
| §6.6 summary, §6.7 practice | yes |

### C. Findings

**M1. Critical (low impact, dropped alternative condition). L2 bullet 3 (line 30) and Concepts `[[aic]]` (line 196).**
- **Problem:** "AIC needs flat priors ..." and "reliable only with flat priors". The digest drops the alternative "or overwhelmed by the likelihood". This makes the requirement stricter than the source's.
- **Evidence:** p. 189 condition (1): "The priors are flat or overwhelmed by the likelihood." L3 (line 66) has it right.

**M2. Critical (low impact, wrong statement). L2 bullet 7 (line 34): "widened the interval for the neocortex slope".**
- **Problem:** The interval that widened is the 89% interval of the averaged prediction μ across neocortex values. No slope parameter's interval is computed. Saying a slope interval widened contradicts the point made in the same bullet, that averaging is over predictions, not parameters.
- **Evidence:** p. 204: "model averaging the predictions has a noticeable impact on the intervals of μ. The shaded interval includes a slope of zero." L3 (line 166) is correct.

**M3. Major (dropped condition, mitigated). L3 line 103 and L2 bullet 8 (line 35): "Regularization reduces overfitting within a model".**
- **Evidence:** p. 194: "Regularization, *as long as it's not too strong*, reduces overfitting for any particular model." The caveat does survive elsewhere (L2 bullet 1, §6.3), so impact is limited.

**M4. Major (glossary). Several terms are used without a definition:**
- **MAP** (lines 146, 155);
- **OLS** (line 56);
- **posterior predictive checks** (lines 32, 110);
- **masking effect** (lines 140, 155);
- **counterfactual predictions** (line 165);
- **percentile interval** (line 155);
- **small-world analysis** (line 139).

**M5. Minor. Line 168: "WAIC can be fooled".**
- **Evidence:** p. 204: "WAIC and similar metrics *will* be fooled". The sentence sits inside a conditional ("if we try enough combinations"), so impact is small.

**M6. Minor. Line 92: BIC box drops "of a linear model".**
- **Evidence:** p. 192: "BIC is related to the logarithm of the average likelihood of a linear model". The digest also drops "in general" from "the exact penalty is not in general the same".

**M7. Minor. Line 53 (N = 100): "The priors do help" is dropped.**
- **Evidence:** p. 187.

**M8. Minor. Line 89: a page number used as an equation tag.**
- **Problem:** `\tag{p. 192}` uses a page number as an equation tag. The author has no equation numbers here.

**M9. Minor. Too many direct quotations.**
- **Problem:** There are about 12 verbatim source quotations, against the 10-quote limit (rule 13).

**M10. Minor. §6.5 drops a caveat.**
- **Evidence:** p. 196: "be wary not to overgeneralize the example that follows".

**M-cat. Major (catalog/provenance; not charged to the digest). The source PDF is the 1st edition.**
- **Problem:** The work id `mcelreath-2020-rethinking` and `canon/bayesian.md` cite the **2nd edition (2020)**, whose focus chapters are Ch. 7 "Ulysses' Compass" etc. The extracted chapter is the **1st edition's** ch. 6:
  - the running header "6. OVERFITTING, REGULARIZATION, AND INFORMATION CRITERIA";
  - `map`/`map2stan`;
  - DIC/AIC and `compare` columns dWAIC/weight;
  - `ensemble`.
- **Note:** The audit brief also describes this unit as "2nd ed., ch. 7".
- **Consequence:** Every digest from this PDF will be filed under the wrong edition, and its chapter numbers will not match the canon's focus list.
- **Fix:** Replace the PDF, or re-id the work as the 1st edition (2015/2016) and note it in the canon.

---

## 3. Strogatz, *Nonlinear Dynamics and Chaos*, ch. 7 "Limit Cycles", part 2 (printed pp. 217–243)

### A. What I checked
- **Equations against the images:** (1)–(7), (9)–(57), symbol by symbol.
- **Re-derivations:**
  - (27) from (25)–(26).
  - (37): the source sign is reversed. The digest's misprint note is correct, and I confirmed that (39) follows from the printed (37).
  - (38): $\sin\theta\cos^2\theta=\tfrac14(\sin\theta+\sin3\theta)$.
  - (42) from (40).
  - (55), which solves $r'=\tfrac12r-\tfrac18r^3$, r(0) = 1.
  - (54) averages and $\langle\cos^2\sin^4\rangle=1/16$.
- **Exercise list:** every exercise number and page in the list and in "Exercises worth doing" (7.3.9 p. 235, 7.6.2 p. 238, 7.6.12 p. 239, 7.6.14/7.6.17 p. 240, 7.6.19 p. 241).
- **Reading-note misprints:** (49) $\cos(t+\phi)$; ¼ missing on p. 227; 7.6.25(c) $\sin(t+\theta)$. All three are confirmed in the images.
- **Recomputation (toy):** $r=r_0e^{-T/2}$; 0.607, 0.368; roots $(-\varepsilon\pm i\sqrt{4-\varepsilon^2})/2$; regular series 1 − εt/2 = 0 at t = 20. All correct.
- **Format:** L1 has 108 words; L2 has 8 bullets. Offset pdf − 15 is correct.

### B. Coverage
| Source item | In L3? |
|---|---|
| end of §7.5 (sequential vs concurrent time scales) | yes |
| §7.6 setting (1)–(3), Fig. 7.6.1 | yes |
| Regular perturbation theory (4)–(17), Fig. 7.6.2, two failures | yes ((8) omitted, minor) |
| Two-timing (18)–(22), height analogy | yes |
| Ex. 7.6.1 (23)–(33), Fig. 7.6.3, super-slow time | yes |
| Ex. 7.6.2 van der Pol (34)–(44) | yes |
| Averaged equations (45)–(54) + derived averages | yes |
| Ex. 7.6.3 transient (55)–(56), Fig. 7.6.4 | yes |
| Ex. 7.6.4 Duffing (57), hardening/softening, conservative/center | yes |
| Validity of two-timing (rule of thumb, references) | yes |
| Exercises 7.1–7.6 (pp. 230–243) | listed by topic (appropriate) |

**Length check (0.69× target).** All key results survive. The savings came from listing the exercises.

### C. Findings

**T1. Major (glossary). Several terms are used without a definition:**
- **conservative system** and **nonlinear center** (line 279);
- **method of averaging** and **asymptotic approximation** (line 283);
- **Liapunov function, Dulac's criterion, cycle graph, Liénard system, heteroclinic cycle** (exercise list, line 286);
- **Fourier series** (line 224; listed in Prerequisites only as "averages of periodic functions").

**T2. Minor. Line 68: equation (8) is skipped.**
- **Problem:** The substitution step (8) is skipped ("Substituting (4) into (5) and grouping powers gives (9)"). Rule 6 says to never skip an author's step. It is trivial here.

**T3. Minor. Line 96 and L0 (line 20): two qualifications are dropped.**
- **Evidence:** p. 219 says (17) "is the beginning of a *convergent* series expansion" for the true solution. p. 218 says regular perturbation theory "works well on certain classes of problems (for instance, Exercise 7.3.9)".
- **Consequence:** Without these, L0's "a plain power series in ε breaks down" reads more generally than the source. The source's point is a breakdown at long times for this problem class.

**T4. Minor. L2 bullet 1 (line 28): one trajectory reported as many.**
- **Problem:** The digest says "trajectories spiral slowly out". Fig. 7.6.1 shows one computed trajectory from an initial condition near the origin.

**T5. Minor. Lines 29 and 96: "≲" is used for the source's "≪" (t ≪ O(1/ε)).**

**T6. Minor. Line 287: Exercise 7.6.1 is not in the 7.6 exercise list.**
- **Note:** It is cited earlier, at line 96.

---

## 4. Shannon 1951, "Prediction and Entropy of Printed English" (BSTJ, printed pp. 50–64)

### A. What I checked
- **Equations:** (1)–(7), (10)–(18), (20)–(21) against the images, including (10), (14) and (15). The digester did not have these images and "reconstructed" these equations from the prose. **All three reconstructions match the print exactly.**
- **The trigram correction formula.**
- **Tables:**
  - the 26/27-letter table;
  - Table I first-guess row (18.2 … 80, 16 values);
  - the reverse-prediction table (18 values);
  - the bounds table (32 values: 4.03 … 1.3 / 3.19 … .6).
- **Numbers:** Exp. 1 (89/129 = 69%) and Exp. 2 (79 + 8 + 3 + 2 + 2 + 8 = 102); Fig. 3 rectangle masses (.40 + .30 + .10 + .20 = 1, the digest's added check is correct); the smoothing of column 4 (47, 18, 14, 21 spread over rows 4–20).
- **Reading notes:**
  - "column 1" on p. 57 should be column 2. Confirmed.
  - (18) lacks a minus sign. Confirmed.
  - There is no (19). Confirmed.
  - Offset pdf + 49. Correct.
- **Recomputation (toy):** −Σq log q = 1.485, lower bound 1.151, flat case = 1. All correct.
- **Format:** L1 has exactly 120 words; L2 has 8 bullets.

**Auditor observation (not a digest error).** Shannon's own Zipf arithmetic does not reproduce:
- $\sum_{n\le N}.1/n$ reaches 1 at N ≈ 12,367, not 8,727;
- −Σ p log₂ p up to 8,727 gives 9.14 bits per word, not 11.82.

The digest correctly reports the printed values. A Reading-notes line saying so would help later posts.

### B. Coverage
| Source item | In L3? |
|---|---|
| §1 entropy/redundancy, 2.3 bits / 50%, ~1 bit / 75% | yes |
| §2 (1)–(7), trigram correction, Zipf (6)–(7), F_word table, .818 | yes |
| §3 Exp. 1 (8), twin argument, Fig. 2, Exp. 2 (9), reduced text; Exp. 3 Table I; reverse prediction | yes |
| §4 ideal predictor (10), (11) + proof (12), equality conditions, (13) limits, transducer properties, (14)–(15), majorization (16) | yes |
| §5 bounds (17), upper-bound proof, lower bound (18), rectangular decomposition (Fig. 3), proof, monotonicity (20)–(21) | yes |
| §6 smoothing, bounds table, caveats, Fig. 4 | yes |

### C. Findings

**H1. Critical (low impact, dropped condition). L0 (line 20): the ideal-predictor condition is dropped.**
- **Problem:** "...he proves bounds that turn the frequencies of the guess numbers into bounds on the N-gram entropy." The lower bound is proved only for the frequencies of an **ideal** predictor. The guess numbers in L0's own first clause come from people.
- **Evidence:** p. 64: "the lower bound was proved only for the ideal predictor, while the frequencies used here are from human prediction". L1, L2 and L3 all keep the condition.
- **Fix:** "...proves bounds that turn an ideal predictor's guess-number frequencies into bounds..."

**H2. Major (wrong definition in a helper line). Prerequisites (line 25): "concave functions (second derivative > 0 means the curve bends upward)".**
- **Problem:** In modern usage, f″ > 0 defines a **convex** function. Shannon's term (p. 64) is "concave *upward*". As written, the line teaches the wrong sign convention for "concave". L3 (line 173) correctly says "concave upward".

**H3. Major (low impact, dropped hedge). L3 line 93: "In general" is dropped.**
- **Problem:** The digest says "Good prediction does not require more than N preceding letters".
- **Evidence:** p. 55: "*In general*, good prediction does not require knowledge of more than N preceding letters".

**H4. Minor (length). 4,454 words is 1.66× the 2,678 target and 70% of the source's length.**
- **Problem:** This is over the 1.3× cap of rule 12. The repair pass grew rather than trimmed. The state log shows 4,448 words at acceptance.

**H5. Minor. Line 115: (10) is labelled "(added step: ... reconstructed from the prose)".**
- **Problem:** (10) is the author's printed equation (p. 58). The same applies to (14) and (15) on p. 60, which are called "reconstructed". The content is right; the provenance label is wrong. **Root cause (pipeline):** page images for pdf 1, 5, 7, 9, 11, 15 were not sent (Reading notes, line 232).

**H6. Minor. L2 bullet 4 (line 31): "69–77% ... on the first try" is stated without its scope.**
- **Problem:** The range applies to Experiments 1–2 only. In Experiment 3 the first-guess rate runs from 18% to 80% depending on N.

**H7. Minor. Line 85: "The earlier estimate of 2.3" drops "for F₈".**

---

## 5. Xie, Raghunathan, Liang & Ma 2022, "An Explanation of In-context Learning as Implicit Bayesian Inference" (arXiv v6, pp. 1–31)

### A. What I checked
- **Main-text equations and statements:** (1)–(18) against the images; A1–A5 condition by condition ($c_1..c_8$, Δ/4, θ* ∈ Θ); the definitions in (12)–(13); Condition 1; Theorems 1–3 with their exact hypotheses ($k\ge2$, the minimizer assumption, $g$ on [0, 1)).
- **Appendix:** (19)–(24); Props 1–2 incl. $c_7=(c_6)^kc_5^2$; Lemma 1 (31)–(47) incl. matrix shapes; App. D (48)–(94) incl. Δ′ < Δ/2, ε < (Δ/2 − Δ′)p(θ*), (69), (77)–(80), (84)–(88), (93); App. E (95)–(116).
- **Experimental settings:** temperatures 0.1/10/0.01, 0.1T + 0.9I, 10 × 10 memory matrix, 1000 × 10240 / 100 × 1024 tokens, n and k grids, 2500 prompts; GPT-2 settings (4/12/16 layers, 12 heads, 768, dropout 0.1, context 1024, AdamW, batch 8, 5 epochs, 8e-4); LSTM (6 layers, 768, dropout 0.2, 10 epochs).
- **Results:** the Fig. 6 table (60.2 ± 5.7, 81.2, 84.7, 95.8 ± 1.11, losses 1.33/1.50/1.35, 28M); Table 1 (69.8/70.7/69.6/71.4) and the 56% gap.
- **Reading notes:**
  - Fig. 6 at vocab 150 (98.4 vs 98.1): correct.
  - "Table 6": correct.
  - "the sum can must be": correct.
  - [0, 1] vs [0, 1): correct.
- **Recomputation:**
  - The (added step) in Lemma 1 (vector shapes) is correct.
  - The (added step) in E.1 (θ ∈ B ⇒ KL sum ≤ ε) is correct.
  - Toy: posterior 8/9, p(A) = 0.833; 1.2/0.96/0.768; 0.446 > 0.405. All correct.
- **Format:** L1 has 110 words; L2 has 8 bullets. Offset printed = pdf.

### B. Coverage
| Source item | In L3? |
|---|---|
| Abstract/§1 incl. (1), BvM challenge, claims, open questions | yes |
| §2 pretraining (2), prompt (3), mismatch, predictor (4), $f_n$, $L_{0\text{-}1}$; §2.1 A1–A5 | yes |
| §3.1 (5)–(7); §3.2 (8)–(11); §3.3.1 (12)–(15), Thm 1; §3.3.2 Thms 2–3 (16)–(18) | yes |
| §4 GINC, main result, ablations, unseen concepts, size/architecture, order sensitivity, zero-shot > few-shot | yes |
| §5 related work (BvM, topic models, mismatch, meta-learning, small scale); §6 | yes |
| App. A, B (Props 1–2), C (Lemma 1), D (Thm 1 proof), E (Lemma 2, E.1, E.2), F.1–F.5 | yes |

### C. Findings

**X1. Major (glossary). Several terms are used without a definition:**
- **MLE** (line 45);
- **dominated convergence** (lines 75, 184);
- **EM, MCMC** (line 128);
- **AdamW, dropout** (line 211);
- **LAMBADA** (lines 35, 215);
- **0-1 risk / multiclass logistic risk** (only symbolically defined).

**X2. Major (low impact, overstated Concepts line). `[[latent-concept]]` (line 232) "...and determines the task (pp. 2–3)".**
- **Evidence:** p. 26: "The prompt start distribution *and* the concept *together* determine the in-context task." The cited pages 2–3 do not say that the concept alone determines the task.

**X3. Minor. Line 124: "recovers" for "*can* recover with more examples" (p. 11).**

**X4. Minor. L0 (line 20), L1, L2 bullet 3: the framework assumptions are not mentioned.**
- **Problem:** These name only the distinguishability condition. Theorem 1 also assumes A1–A5 ("Assume the assumptions in Section 2.1 hold", p. 7). The abstract does the same, so impact is minimal.

**X5. Minor. Line 193 merges two steps.**
- **Problem:** (110) and (111) are merged under the label "(110–112)". The intermediate $O(\|\theta-\theta^*\|^3)$ line is not shown.

**X6. Minor. Line 122: the exception to "Accuracy rises ... 4 to 12 to 16 layers" is not in L3.**
- **Problem:** The vocab-150 exception (98.4 → 98.1) appears only in the Reading notes.

---

## Fix list (critical + non-glossary major)

| # | Digest / location | Change |
|---|---|---|
| S1 | Sutton L2 bullet 5 | "They are nonparametric; local-learning variants avoid exponential memory..." (kernel regression uses all examples) |
| S2 | Sutton L3 l. 69 | "It can produce good results for shallow nets..." |
| S3 | Sutton L3 l. 81 | "This helps make responses spatially invariant" |
| M1 | McElreath L2 bullet 3 + `[[aic]]` | "flat priors (or priors overwhelmed by the likelihood)" |
| M2 | McElreath L2 bullet 7 | "...widened the 89% interval of the averaged predictions μ, which then admits a zero slope" |
| M3 | McElreath L3 l. 103 / L2 bullet 8 | add "as long as it is not too strong" |
| H1 | Shannon L0 | "...an ideal predictor's guess-number frequencies..." |
| H2 | Shannon Prerequisites | "convex ('concave upward') functions: f″ > 0" |
| H3 | Shannon L3 l. 93 | restore "In general" |
| X2 | Xie Concepts `[[latent-concept]]` | "together with the prompt start distribution, determines the task (p. 26)" |

Also correct S5 (state n = ∞ / n = 1 from the image) and H5 (relabel (10), (14), (15) as the author's equations). Trim Shannon toward ≤ 3,500 words.

**Pipeline actions:**
1. Resolve the McElreath edition mismatch (M-cat) before any further McElreath units are digested.
2. Send all page images for short papers. Shannon was sent 9 of 15.
3. Enforce the 1.3× length cap after the verifier repair, not only before it.
4. Make the verifier check the glossary rule. It failed in 4 of 5 digests again.
