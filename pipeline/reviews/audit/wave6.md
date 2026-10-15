# Independent audit, wave 6: Murphy ch. 15, Polyanskiy & Wu ch. 17 ("ch19"), Jaynes ch. 12, Lorenz 1963, Bayes 1763

Auditor: Claude Opus 5.5. I did not write these digests. Date: 2026-10-15.
Pipeline under audit: Claude Sonnet 5.5, digest prompt v2.2 + verifier v2.2. All five digests are `verified: repaired`.
Ground truth: the page images of the five extracts in `/home/claude/audit/w6/`. I read every page: 40 + 8 + 25 + 12 + 16 = 101.
Zoomed re-renders (250 dpi) were used for: Lorenz p. 140 ("τ₂ = τ₁ + 0.7"), Jaynes p. 375 (12.7) and p. 390 (12.58), Bayes p. 20 (Prop. 8 wording, also checked in the text layer).

Recomputation (python3 / by hand):
- Polyanskiy toy: P[Bin(3,0.1) ≥ 2] = 0.028; h(0.1) = 0.469, C = 0.531, bound 1/0.9 = 1.111. Added step $d(p\|q)\ge -h(p)+p\log\frac1q$ is true. Monotonicity of $h(p)/(1-p)$: derivative numerator $=-\log p>0$.
- Lorenz: $r_c = 10(10+8/3+3)/(10-8/3-1) = 470/19 = 24.74$; $\sqrt{b(r-1)}=\sqrt{72}=6\sqrt2$; $e^{-(41/3)(0.7)} = 7.0\times10^{-5}$ (38); toy tent-map table (gap 0.01 → 0.32, cycle 4/5, 2/5).
- Bayes: added step of Prop. 3 ($N/a=b/P$); Prop. 4 algebra ($x-y=P$, $y:x=N-b:N \Rightarrow x:P=N:b$); toy areas 1/3, 1/3, 1/3 and 7/24 ÷ 1/3 = 7/8.
- Jaynes: (12.48) from the Jacobian $d\theta'/d\theta=a/(1-\theta+a\theta)^2$; (12.49) by differentiating at a = 1; added step to (12.68) and $\int_{\sqrt3/2}^1 x/\sqrt{1-x^2}\,dx=1/2$; (12.13) sign; toy (ln 2 both units; ⟨θ⟩ = 3/4, σ² = 0.0375; θ′ = 0.75).
- Murphy: Table 15.1 total 4526; norms √10, √20, √34, √58; ridge factor-of-2 note; (15.87) swap note; (15.81) vs (15.60); added step to (15.116); toy (gradient (−1, 1), H = [[5, 2.5], [2.5, 2.5]], H⁻¹, Newton step (−0.8, 1.2), MLE (−0.847, 1.253)).

Targets from `pipeline/state/units.jsonl`.

Severity scale (as briefed):
- **Critical:** wrong equation/number/statement; strengthened or weakened claim (including a dropped condition); claim not in source; misattributed voice.
- **Major:** wrong page ref; missing key result; dropped hedge; ≥ 3 undefined terms (glossary).
- **Minor:** notation, format, length, small coverage gaps, small ref slips.

"Low impact" = real, but L2/L3 state the point correctly, so a later post is unlikely to copy it.

## Summary (counts before fixes)

| Digest | Checks (approx.) | Critical | Major | Minor | Coverage | Toy / added steps | Length (body words; source / target; ×target) | Verdict |
|---|---|---|---|---|---|---|---|---|
| Murphy ch. 15 (pp. 591–629) | ~120 (every display (15.1)–(15.190) symbol by symbol; all numbers in 15.2.4, 15.3.5, 15.3.9, 15.5.2; 12 reading notes; Concepts/Instances) | 0 | 1 (glossary) | 5 | complete (15.1–15.5.2.2) | all correct | 5,761; 16,718 / 6,000 (0.96×) | very good |
| Polyanskiy & Wu ch. 17 (pp. 342–349) | ~40 (Defs 17.1–17.2, (17.1)–(17.6), Thm 17.3 and every proof step, all BSC numbers, history paragraph, Remarks) | 1 (low impact) | 1 (glossary) | 6 | complete; small gaps | all correct | 1,910; 3,150 / 1,323 (**1.44×**) | good; fix (17.2) condition |
| Jaynes ch. 12 (pp. 372–396) | ~85 ((12.1)–(12.68) symbol by symbol, 8 printed misprints re-checked, all voice tags, every hedge in 12.4.4–12.5, toy) | 1 (low impact) | 4 (1 glossary) | 4 | complete | all correct | 3,842; 11,602 / 4,873 (0.79×) | good; L0/L1 overstate |
| Lorenz 1963 (pp. 130–141) | ~75 ((1)–(38) symbol by symbol on the scan, every numerical claim in §7, all definitions/theorems of §3, all conclusion claims, misprint) | 1 (low impact) | 2 (1 glossary) | 9 | complete; small gaps | all correct | 4,078; 5,400 / 2,268 (**1.80×**) | good; too long |
| Bayes 1763 (pp. 8–23) | ~60 (every proposition, corollary and proof step; Defs 1–7; Postulates, Lemmas; voice of every Price/Bayes/footnote passage; misprints) | 1 (low impact) | 2 (1 glossary) | 8 | complete; small gaps | all correct | 3,802; 7,969 / 3,347 (1.14×) | good; voice slips |

**Totals:** 4 critical (all low impact, all at summary or L2 level, or a dropped condition), 10 major (5 of them glossary), 32 minor across 5 units.

**Estimate of surviving errors per unit (before this audit's fixes):**
- **Critical:** 0.8. All four are low impact; in each case L3 (or L2) states the point correctly.
- **Major:** 2.0; 1.0 if the glossary items are excluded.
- **Minor:** 6.4.

**Equations.** Every displayed equation matches the page image, symbol by symbol, in all five digests. The digests correctly flagged and handled these source problems (all confirmed against the images):
- Murphy: ridge factor ½ in (15.51); swapped π/1−π in (15.87); reversed σ² = ∞ / σ² = 0 statement in 15.3.5; (15.81)/(15.82) vs (15.60)/(15.71); matrix sizes in (15.113); Σ₀ in (15.110); "γ ∝ γ"; Fig. 15.5 variance/std labels; iris text vs caption; Φ(μ_i) in (15.175); "f(η_n) > 0".
- Jaynes: sign of (12.13); b₂ for b₁ in (12.31); "ν′ = ax + b" on p. 381; "1 − θ − aθ" in (12.48); (12.37) not the Poisson formula; "αR" in (12.58); "(12.50)" for the group on p. 396; Harr/Kendell.
- Lorenz: "τ₂ = τ₁ + 0.7" on p. 140.
- Bayes: "as A B, and B b" (Prop. 8); "fghimb" without k (Prop. 9); italic o read as 0; bar notation.

One printed misprint was **missed** (Jaynes (12.7), see J3).

**Toy examples and added steps.** All recompute exactly (see list above).

**Pattern.** Same as waves 2–5:
- Every critical item is a summary-level or L2 line that is stronger than L3, or a theorem with a dropped condition.
- The glossary rule ("≥ 3 undefined terms") failed in **all five** digests. This is the seventh wave in a row.
- The length cap was not enforced after repair: Lorenz 1.80× (76% of the source's length), Polyanskiy 1.44×.
- New this wave: two **voice** slips in Bayes (an unsigned footnote attributed to Bayes; Price's De Moivre framing given to Bayes in L1), and **soft hedges** ("it appears", "seem", "we suggest", "perhaps") dropped in Jaynes and Bayes.

**Verdict: OK to continue the batch** after the fixes below. The verifier should (1) check every L0/L1 sentence for dropped conditions, (2) tag every footnote's voice in historical texts, (3) enforce the glossary rule mechanically.

---

## 1. Murphy, *Probabilistic Machine Learning: Advanced Topics*, ch. 15 "Generalized linear models" (printed pp. 591–629; p. 630 blank)

### A. What I checked
- 15.1: (15.1)–(15.38), including the binomial and Poisson derivations, ZIP (15.24), canonical/probit/cloglog links (15.25)–(15.32), Hessian and convexity claim with its "assuming f(η_n) > 0".
- 15.1.4: package names, HMC/VB statements.
- 15.2.1–15.2.3: (15.39)–(15.82), every breve/hat; Jeffreys emulation; frequentist equivalence (15.76)–(15.77); g-prior footnote.
- 15.2.4: 178 ± 40, N(0,10), 272 cm, LN(0,1), Unif(0,50), Expon(λ), E[β₂|D] ≈ 0.08.
- 15.2.5–15.2.8: (15.86)–(15.104), [EY09]/[SPZ09], [WW12]/[WRN10]/[WN07]/[HXW17] claims, ARD 2-example argument.
- 15.2.9: (15.105)–(15.127) and the added completing-the-square step.
- 15.3: (15.128)–(15.152), logit adjustment and its added step, ω = 10 / 1.5, Ber(0.8) experiment, 1/√D, four separating lines and norms, Laplace shape description, probit approximation, iris HMC claims, LDA remark.
- 15.3.9: Table 15.1 total, both models, all six intervals, 14%, departments, DAG and collider caveat.
- 15.4: (15.164)–(15.184), λ = √(π/8), EM explanation, truncated-Gaussian sampler, ordinal thresholds.
- 15.5: (15.185)–(15.190), radon numbers (85 counties, 2–80 measurements, −0.6, RMSE 0.13/0.08, [0, 0.1]).

### B. Surviving errors
| ID | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| M1 | throughout | Glossary: HMC, Student $\mathcal T$, matrix normal / inverse Wishart, ELBO, empirical Bayes, Gaussian scale mixture, variational Bayes used without definition. | Spec rule 8. | major (glossary) |
| M2 | Concepts, credible-interval | Cites p. 602; the 95% credible interval is in the Fig. 15.1 caption on p. 601. | p. 601. | minor |
| M3 | L3 15.2.4, (15.85) | Drops "of the standardized features". | p. 603. | minor |
| M4 | L3 15.5.2.2 | Omits why excluding [0, 0.1] matters: "In cases where a covariate has no useful predictive role, we would like to be able to induce sparsity". | p. 629. | minor |
| M5 | Intuition note 15.5.2 | Cites p. 629 for "some counties have very few datapoints", which is on p. 627. | p. 627. | minor |
| M6 | L3 15.2.9 | Copies $\nu_0>N_x-1$ without noting that an inverse Wishart over $N_y\times N_y$ matrices would need $N_y-1$; the digest flags all other misprints in this section. | p. 609. | minor |

---

## 2. Polyanskiy & Wu, *Information Theory*, ch. 17 "Error correcting codes" (unit id ch19; printed pp. 342–349)

### A. What I checked
Defs 17.1–17.2 and footnote 1; (17.1) with both joint-distribution formulas; P_e ≤ P_e,max and the linear-code remark; all four fundamental limits; Example 17.1; uncoded P_e; repetition constraints, ℓ = 21, k = 47; Reed–Muller definition, d_min, [64,7,32], 6·10⁻⁶, 16 blocks, 10⁻⁴, 112 bits; (17.2) with its conditions; C ≈ ½; 500 bits; (17.3); 20%; 60 years, turbo, LDPC, 80–90%, polar codes; 2⁴⁰⁰ / 10¹⁸ s / 2⁶⁰; (17.4)–(17.6); randomized-encoder argument; P_e,max and the Neyman–Pearson vertex condition; Thm 17.3 and all six proof steps; Remark 17.2; Concepts; toy; Reading notes.

### B. Surviving errors
| ID | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| P1 | L3 17.2 "Shannon" bullet; Concepts noisy-channel-coding-theorem | (17.2) is stated without its condition "over memoryless channel $P_{Y^n\mid X^n}=(P_{Y\mid X})^n$". Dropped condition = stronger claim. | p. 345: "tells us that over memoryless channel … the fundamental limit satisfies". | critical (low impact: the running example is the BSC, which is memoryless) |
| P2 | throughout | Glossary: MAP/ML, Voronoi cell, Neyman–Pearson region, d_min, union bound, o(n), Type-I/II error (α, β) undefined. | Spec rule 8. | major (glossary) |
| P3 | L3 Remark 17.2 | "improve the bound" drops "significantly". | p. 349. | minor |
| P4 | L3 history | "reach 80–90%" for "typically approach 80…90%". | p. 346. | minor |
| P5 | L3 17.2 | Coverage: omits that computing M* exactly is impossible even for small n, and that existence (bounds) ≠ implementable f, g ("a different story"). | p. 346. | minor |
| P6 | L3 Remark 17.1 | Drops "if f (the encoder) is deterministic with codewords". (L2 keeps it.) | p. 347. | minor |
| P7 | Questions | "Why does the 1/(1−ε) factor make this converse 'weak'…" presupposes an explanation the text defers to Section 22.1. | p. 349. | minor |
| P8 | whole digest | Length 1.44× target. | units.jsonl. | minor |

Not counted: the Reading-notes offset "printed = pdf − 25" refers to the full book PDF and cannot be checked from the extract.

---

## 3. Jaynes, *Probability Theory: The Logic of Science*, ch. 12 "Ignorance priors and transformation groups" (printed pp. 372–396)

### A. What I checked
- 12.1: subjective-Bayesian description (voice), (A)–(C), "fully half", zero analogy, triangle reply, other tools.
- 12.2: "honest", inventory example, "may prove to be the final solution".
- 12.3: (12.1)–(12.15) and the logic around (12.1); Bayes / Jeffreys / mollusk / Haar / Wigner–Weyl paragraphs.
- 12.4.1: (12.16)–(12.36), Problems A/B, group laws, both representations, "which group?", the invitation.
- 12.4.2: (12.37)–(12.40).
- 12.4.3: (12.41)–(12.53), chemical example, population construction, q-values, r = n − r = 1, r = 0 or n.
- 12.4.4: problem statement, ten authors, Poincaré, viewpoint, (12.54)–(12.68), elimination of B and C, singularity, uniqueness, frequency correspondence, experiment.
- 12.5: Maxwell, poker, dilemma, problems vs events, Betelgeuse, reverbalization, Jeffreys reinterpretation (μ = θ − θ⁻¹), non-normalizability, pre-prior.
- Every printed misprint the digest lists.

### B. Surviving errors
| ID | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| J1 | L0 | "A prior for complete ignorance **is fixed** by naming the transformations…". Jaynes: the group "imposes definite restrictions on the form of the solution, and in many cases fully determines it"; combining the two equations "leads in most cases to a functional equation which imposes some restriction". Strengthened. | pp. 382, 389, 395. | critical (low impact; L2 bullet 4 is correct) |
| J2 | L1 | "Location and scale give the Jeffreys prior dσ/σ" drops the condition that this holds for group (12.18); Jaynes's central point in 12.4.1 is that location-and-scale ignorance alone is not enough ((12.30) gives 1/σ²). | p. 381. | major (dropped condition at summary level; L2 bullet 3 states it) |
| J3 | L3 12.3, (12.7) | The image prints (12.7) without the minus sign; the digest copies it silently, though it flags 8 other misprints. As printed, "subtract log n" does not lead to (12.8). | p. 375 (re-rendered at 250 dpi). | major (unflagged misprint in a derivation chain) |
| J4 | L3 frequency correspondence | "Jaynes says this contradicts von Mises" drops "seem to be in direct contradiction" and "It appears to us". | p. 393. | major (dropped hedge) |
| J5 | throughout | Glossary: Abelian, faithful representation, partition function, de Finetti's coherence, "orthodox", confidence interval, chi-squared, rule of succession undefined. | Spec rule 8. | major (glossary) |
| J6 | L3 12.3 first sentence; Concepts differential-entropy | "(12.1) is not derived and is not invariant …, **so** it is not the right measure" / "rejected as non-invariant". Jaynes explicitly sets the non-invariance aside: "We do not refer here to the well-known fact that … lacks invariance …, for (12.1) is not the result of any derivation". | p. 375. | minor (logic link) |
| J7 | L3 12.3, 12.4.3, 12.5 | Soft hedges dropped: "in the cases of interest" (limit (12.8)); "does not seem to correspond well" (Jeffreys/Carnap); "It thus appears that the Bayes–Laplace choice will be the appropriate prior"; "Thus it appears that…" (dilemma); "We suggest that…" (reverbalization). L3 voice tags keep these as Jaynes's views. | pp. 375, 383, 385, 395. | minor |
| J8 | L3 12.4.4 | Omits Jaynes's concessions: the conventional reading "clearly represents one valid way…", "it would perhaps be overstating the case…"; "experimental results will no doubt be more convincing if reported by others". | pp. 388, 394. | minor |
| J9 | L3 (12.61) | Range conditions $0<a\le1,\ 0\le r\le R$ dropped. | p. 390. | minor |

Not counted: Reading-notes offset "printed = pdf − 30" refers to the full book PDF.

---

## 4. Lorenz 1963, "Deterministic Nonperiodic Flow" (J. Atmos. Sci. 20, printed pp. 130–141; scan)

### A. What I checked
Abstract; §1 (rotating basin, forecaster, linear vs nonlinear); §2 (1)–(7), ellipsoid E, trapping; §3 all definitions, both theorems, the noncentral case and "to the writer", the p. 133 predictability implication, summary; §4 (8)–(16), convexity argument, finite-precision remark; §5 (17)–(27), all parameter definitions; §6 (28)–(34), r = 1, σ < b + 1 case; §7 σ, a², b, 470/19, r = 28, (6√2, 6√2, 27), Δτ, LGP-30, (0,1,0), ×10 printing, steps 35/50/60/85/150/1650, Figs. 1–5, 385, 483, (35)–(36), all three classes and the example sequences, 398 … 419, iterations 5340/4881/3625/3926, Λ, (37)–(38), the misprint; §8 every claim including the caveat, analogues, "a few days or a few centuries".

### B. Surviving errors
| ID | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| Lz1 | L2 bullet 1 | "in linear systems constant forcing ultimately gives constant response" drops "dissipative" (false for conservative linear systems). | p. 131: "in dissipative systems governed by finite sets of linear equations". | critical (low impact; L3 §1 correct) |
| Lz2 | L1 | "He argues that such systems have bounded solutions" generalizes to all forced dissipative ODE systems. Lorenz: systems "typified by" (4) are bounded; such a system "often has the property". | pp. 131–132, 140. | major (dropped hedge/condition) |
| Lz3 | §1, §5–§7 | Glossary: g, α, ν, κ, a; Rayleigh number (never named as such in L3); stream function; advection; the Jacobian $\partial(\cdot,\cdot)/\partial(x,z)$; measure zero. | Spec rule 8; p. 134 defines g, α, ν, κ. | major (glossary) |
| Lz4 | L2 bullet 5 | "three steady states" without "when r > 1". | p. 135. | minor |
| Lz5 | L2 bullet 6 | "settles onto a pair of nearly merging surfaces" drops "within the limits of accuracy of the printed values" and "appear to". | p. 138. | minor |
| Lz6 | L3 §5 | Equations (19)–(20) and the free-boundary condition omitted ("fields of the form (19)–(20)" with no formula). | p. 134. | minor |
| Lz7 | L3 §3; intuition note | Omits "an acceptable prediction of an instantaneous state in the distant future may well be impossible" (p. 133). Intuition note says a stable central trajectory "would repeat"; the theorem gives quasi-periodic, not periodic. | p. 133. | minor |
| Lz8 | L3 §7 | Omits the step motivating M_n (extent beyond the critical distance seems to fix the next spiral and number of circuits) and the "holes near C and C′". | p. 138. | minor |
| Lz9 | Canonical instances, atmospheric-predictability | "the case that very-long-range forecasting is impossible…" drops "when our results … are applied to the atmosphere". | p. 141. | minor |
| Lz10 | Concepts, attractor | Lorenz does not use "attractor"; no "(canon link; not stated in this unit)" flag, unlike the chaos and bifurcation lines. | whole paper. | minor |
| Lz11 | L3 §7 first-return map | Omits the limit on the empirical scheme's accuracy (exactness of Figs. 2, 4 and of observed initial values). | p. 139. | minor |
| Lz12 | whole digest | Length 1.80× target (76% of the source). | units.jsonl. | minor |

---

## 5. Bayes 1763, "An Essay towards solving a Problem in the Doctrine of Chances" (reprint pp. 8–23)

### A. What I checked
Price's letter (every paragraph, including the De Moivre footnote and the final-causes passage); the Problem; Defs 1–7; Props 1–7 with every corollary and both footnotes; the definition of trials; Postulates 1–2; Lemmas 1–2 (both cases); Prop. 8 statement, demonstration and corollary; Prop. 9 and corollary; scholium and its footnote; voice of each passage; misprints; toy; Concepts.

### B. Surviving errors
| ID | Location | Problem | Evidence | Severity |
|---|---|---|---|---|
| B1 | L1 first sentence | "Bayes asks the inverse of De Moivre's problem." Bayes never mentions De Moivre in these pages; the framing is Price's ("I know of no person who has shewn how to deduce the solution of the converse problem"). | pp. 9–10, 12. | critical (misattributed voice; low impact, L2 bullet 1 attributes it to Price) |
| B2 | L3 scholium, footnote | "Footnote: Bayes says it will be proved presently, in art. 4…". The footnote is unsigned; Price says he wrote short notes (p. 10), and the p. 16 footnote refers to "Mr. Bayes" in the third person. | pp. 10, 16, 23. | major (voice unclear stated as Bayes) |
| B3 | throughout | Glossary: *componendo inversè*, commensurable, ordinate, fluxions undefined. | Spec rule 8. | major (glossary) |
| B4 | L0 | "he argues that the model fits events about which nothing is known" drops "seems to appear"; also "the model" for "the rule". | pp. 22–23. | minor |
| B5 | L3 Price's letter | "(pp. 8–9)" for a passage wholly on p. 8. | p. 8. | minor |
| B6 | L3 Price's letter | "might not be looked upon" drops "perhaps". | p. 9. | minor |
| B7 | L3 Prop. 8 demonstration | Contradiction step cited "(pp. 21–22)"; it is on p. 21. | p. 21. | minor |
| B8 | L3 Lemma 1 | Incommensurable case drops that p, t lie on fb (needed for "if it lies between p and t it must lie between f and b"). | p. 19. | minor |
| B9 | L3 Price's letter | Coverage: omits Price's stated purpose (fixed laws, intelligent cause, argument from final causes for the Deity; the converse problem "more directly applicable to this purpose"). | p. 10. | minor |
| B10 | Reading notes | "(metadata: pp. 370–418)" is not visible in these pages (rule 14). | pp. 8–23. | minor |
| B11 | L3 Prop. 5 footnote (p. 15) | Unsigned footnote given without a voice tag (same issue as B2, lower stakes). | p. 15. | minor |

---

## Fixes (2026-10-15)

Every fix was re-verified against the page image before editing. Edits are minimal; nothing was cut. Every digest got longer (Murphy 5,761 → 5,885 body words; Polyanskiy 1,910 → 2,073; Jaynes 3,842 → 4,097; Lorenz 4,078 → 4,346; Bayes 3,802 → 3,908). L1 word counts after fixes: 101, 118, 117, 118, 110 (all ≤ 120). Every edited digest now has `audited: 2026-10-15` and `audit_fixes: <n>`. Glossary fixes are inline definitions of ≤ 15 words at first use in L3. No quotations were added (two that I first added were turned into paraphrase to respect the 10-quote cap).

### Murphy ch. 15: 6 fixes
| ID | Status | Note |
|---|---|---|
| M1 | fixed | Defined HMC, variational Bayes (15.1.4), Student $\mathcal T$ (15.63), Gaussian scale mixture (15.91), empirical Bayes (15.2.8), matrix normal / inverse Wishart (15.2.9), ELBO (15.3.8). |
| M2 | fixed | p. 602 → p. 601. |
| M3 | fixed | "A quadratic expansion of the standardized features". |
| M4 | fixed | Added the sparsity motivation (p. 629). |
| M5 | fixed | Ref → (pp. 627, 629). |
| M6 | fixed | Reading note: $\nu_0>N_x-1$ as printed; $N_y-1$ expected (my check). |

### Polyanskiy & Wu ch. 17: 7 fixes
| ID | Status | Note |
|---|---|---|
| P1 | fixed | "over a memoryless channel $P_{Y^n\mid X^n}=(P_{Y\mid X})^n$ of blocklength n" in L3 and in Concepts. |
| P2 | fixed | Defined o(n), d_min and $[n,k,d_{\min}]$, union bound, MAP, ML, Voronoi cell, Type-I/II error, Neyman–Pearson region. |
| P3 | fixed | "can improve the bound significantly". |
| P4 | fixed | "typically approach 80–90%". |
| P5 | fixed | Added the M* computation remark and existence vs implementation (paraphrased). |
| P6 | fixed | "and a deterministic encoder with codewords $\{c_i\}$". |
| P7 | fixed | Question reworded to follow the text (Section 22.1). |
| P8 | not fixed | Length; the brief says not to shorten. |

### Jaynes ch. 12: 9 fixes
| ID | Status | Note |
|---|---|---|
| J1 | fixed | L0: "is restricted, and in many cases fully determined, by…" (p. 395). |
| J2 | fixed | L1: "Location and scale under the shift-and-rescale group give the Jeffreys prior dσ/σ; another group gives 1/σ²" (L1 now 117 words). |
| J3 | fixed | (12.7) kept as printed, with "(as printed, without a leading minus sign; see Reading notes)" and a Reading-notes bullet giving the corrected limit. |
| J4 | fixed | "He says these conclusions seem to be in direct contradiction to von Mises; it appears to him that…". |
| J5 | fixed | Defined orthodox, de Finetti's coherence, partition function / Lagrange multipliers, Abelian (+ "direct product of two one-parameter groups"), faithful representation, rule of succession, confidence interval, chi-squared. |
| J6 | fixed | First sentence of 12.3 now follows Jaynes's logic; Concepts line corrected. |
| J7 | fixed | Restored "in the cases of interest", "does not seem to correspond well", "It thus appears to be the appropriate prior", "it appears that", "He suggests that". |
| J8 | fixed | Added the p. 388 concession and the p. 394 "more convincing if reported by others" (paraphrased). |
| J9 | fixed | Added $0<a\le1,\ 0\le r\le R$ to (12.61). |

### Lorenz 1963: 11 fixes
| ID | Status | Note |
|---|---|---|
| Lz1 | fixed | "in dissipative linear systems". |
| Lz2 | fixed | L1: "A typical forced dissipative form has bounded solutions; for bounded systems, nonperiodic solutions are ordinarily unstable." (118 words) |
| Lz3 | fixed | Defined advection, stream function, g, α, ν, κ, the Jacobian term, a, Rayleigh number, measure zero. |
| Lz4 | fixed | "three steady states when r > 1". |
| Lz5 | fixed | "Within the accuracy of the printed values, it lies on a pair of surfaces that appear to merge." |
| Lz6 | fixed | Added (19), (20) and the free-boundary condition. |
| Lz7 | fixed | Added the p. 133 implication; intuition note now says "would be quasi-periodic". |
| Lz8 | fixed | Added the critical-distance → next spiral → circuits step and the holes near C, C′. |
| Lz9 | fixed | Instance now conditional ("if the results apply to the (ostensibly nonperiodic) atmosphere"). |
| Lz10 | fixed | "Lorenz does not use the word 'attractor' (canon link; not stated in this unit)". |
| Lz11 | fixed | Added the accuracy limit of the empirical scheme. |
| Lz12 | not fixed | Length (now 1.92×); the brief says not to shorten. Recommend a separate trim pass. |

### Bayes 1763: 11 fixes
| ID | Status | Note |
|---|---|---|
| B1 | fixed | L1: "Price presents Bayes's problem as the converse of De Moivre's." |
| B2 | fixed | "Footnote (voice unclear; Price says he added short notes, p. 10): it will be proved presently…". |
| B3 | fixed | Defined *componendo inversè*, commensurable, ordinate, fluxions. |
| B4 | fixed | L0: "he gives a reason why the rule seems to fit…". |
| B5 | fixed | p. 8. |
| B6 | fixed | "might not perhaps be looked upon". |
| B7 | fixed | p. 21. |
| B8 | fixed | "choose points p, t on fb with Bp, pt, tA commensurable". |
| B9 | fixed | Added Price's final-causes purpose (p. 10), in Price's voice. |
| B10 | fixed | "The essay continues beyond these pages: …" (no unsourced page range). |
| B11 | fixed | p. 15 footnote tagged "voice unclear". |

**Fix totals:** 44 fixed, 2 not fixed (both length: Polyanskiy, Lorenz). All 4 critical and all 10 major items are fixed.
