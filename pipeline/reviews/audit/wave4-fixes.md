# Wave 4 audit fixes (2026-10-14)

Sources: `wiki/works/<work>/<unit>.md`, checked against `/home/claude/audit/w4/<work>__<unit>.pdf`. I checked the text layer for every fix. I also checked the page images for Sutton p. 236; McElreath p. 186; Strogatz pp. 218–219; Shannon pp. 54, 58, 60; Schelling pp. 218, 232; and Zaller pp. 154–155.
The edits are minimal and nothing was cut. Every edited digest now has `audited: 2026-10-14` and `audit_fixes: <n>` in its frontmatter. Undefined-term majors were fixed with inline definitions of 15 words or fewer at first use.

## Math audit (wave4-math.md)

### Sutton & Barto ch. 9 pt 2: 11 fixes
| ID | Status | Note |
|---|---|---|
| S1 | fixed | L2: "nonparametric; the local-learning ones the authors focus on avoid exponential memory" (p. 231) |
| S2 | fixed | "can produce good results" (p. 225) |
| S3 | fixed | "helps make responses spatially invariant" (p. 228) |
| S4 | fixed | Inline definitions added for (2.7) conditions, GPI, VE, Monte Carlo and bootstrapping |
| S5 | fixed | p. 236 image reads $n=\infty$ and $n=1$; L3 states it; Reading note rewritten |
| S6 | fixed | "if we fully care, it might be one" (p. 234) |
| S7 | fixed | "sometimes desirable, but problematic" (p. 229) |
| S8 | fixed | Ex. 9.6 pointer now gives the $\mathbf x^\top\mathbf x=\mathbb E[\mathbf x^\top\mathbf x]$ condition |
| S9 | fixed | "complex functions needed for many AI tasks" (p. 224) |
| S10 | fixed | Forgetting is now one of the "many ways" researchers developed, not a requirement (p. 232) |
| S11 | fixed | L0: "Beyond basic linear semi-gradient SGD ... a step-size rule of thumb" |

### McElreath ch. 6 pt 2: 10 fixes
| ID | Status | Note |
|---|---|---|
| M1 | fixed | L2 and `[[aic]]`: "flat priors (or priors overwhelmed by the likelihood)" (p. 189) |
| M2 | fixed | L2: "widened the 89% interval of the averaged predictions μ, which then includes a slope of zero" (p. 204) |
| M3 | fixed | "as long as it is not too strong" added in L2 and L3 (p. 194) |
| M4 | fixed | Definitions added for OLS, posterior predictive checks, small-world, masking, MAP, percentile interval and counterfactual predictions |
| M5 | fixed | "WAIC and similar metrics will be fooled" (p. 204) |
| M6 | fixed | BIC box: "of a linear model"; "not in general the same" (p. 192) |
| M7 | fixed | "The priors do help" restored (p. 187) |
| M8 | fixed | Removed the `\tag{p. 192}` page-number tag; the page ref is now in the text |
| M9 | not fixed | Getting under the 10-quote limit means rewording several passages. That is not a one-line fix, and the brief says not to shorten. |
| M10 | fixed | Added the "be wary not to overgeneralize" caveat (p. 196) |
| M-cat | fixed (digest side) | Reading notes now say the pages are from the **1st edition**. No edition statement is printed on them; the evidence is the running header and the `map`/`map2stan`/`ensemble`/DIC material (p. 186 image checked). The catalog and work-id re-id are pipeline actions and were not touched. |

### Strogatz ch. 7 pt 2: 6 fixes
| ID | Status | Note |
|---|---|---|
| T1 | fixed | Definitions added for Fourier series, conservative system, nonlinear center, method of averaging, asymptotic approximation, Liapunov function, Dulac's criterion, cycle graph, heteroclinic cycle and Liénard system. The heteroclinic-cycle and cycle-graph definitions follow Ex. 7.3.11–7.3.12. |
| T2 | fixed | Equation (8) added from the p. 218 image |
| T3 | fixed | Added "convergent" and "works well on certain classes of problems (Ex. 7.3.9)"; L0 now says "breaks down at long times" |
| T4 | fixed | L2: "a trajectory started near the origin" |
| T5 | fixed | "≲" changed to "≪" (p. 219 image) |
| T6 | fixed | 7.6.1 added to the exercise list |

### Shannon 1951: 6 fixes
| ID | Status | Note |
|---|---|---|
| H1 | fixed | L0: "an ideal predictor's guess-number frequencies" |
| H2 | fixed | Prerequisites: convex ("concave upward"), f″ > 0 |
| H3 | fixed | "In general" restored (p. 55) |
| H4 | not fixed | Length (1.66× target). The brief says not to shorten digests. The H5 relabelling removed about 70 words as a side effect. |
| H5 | fixed | (10), (14) and (15) are relabelled as the author's printed equations and checked against the p. 58 and p. 60 images. Reading notes corrected. |
| H6 | fixed | L2: "In Experiments 1–2" |
| H7 | fixed | "2.3 for $F_8$" (p. 54 image) |

### Xie et al. 2022: 5 fixes
| ID | Status | Note |
|---|---|---|
| X1 | fixed | Definitions added for MLE, dominated convergence, EM, MCMC, AdamW, dropout, LAMBADA, 0-1 risk and multiclass logistic risk |
| X2 | fixed | `[[latent-concept]]`: "together with the prompt start distribution it determines the in-context task (pp. 2–3, 26)" |
| X3 | fixed | "can recover with more examples" (p. 11) |
| X4 | fixed | L0, L1 and L2 now name the §2.1 assumptions. L1 is 114 words. |
| X5 | not fixed | Showing the intermediate $O(\|\theta-\theta^*\|^3)$ step means rewriting a derivation. That is not a one-line wording fix. |
| X6 | fixed | The vocab-150 exception (98.4 vs 98.1) is now in L3 |

## Argumentative audit (wave4-argumentative.md)

### Schelling ch. 8: 13 fixes
| ID | Status | Note |
|---|---|---|
| S-M1 | fixed | "not altogether under the threatener's control (p. 218; the book prints 'threateneds')". Misprint added to Reading notes (p. 218 image). |
| S-M2 | fixed | L2: "as long as we are not trying to keep him guessing about our own motivation" |
| S-M3 | fixed | "some of the most momentous decisions of government ... somewhat inadvertently" (p. 235) |
| S-M4 | fixed | Added the two-sided calibration ("small enough ... large enough", p. 232 image). "May work if" restored to "an important reason why ... might be effective". |
| S-m1 | fixed | L1: "even if we do not consciously use it ... misjudge our own tactics". L1 is 120 words. |
| S-m2 | fixed | L2: "calls the small-probability threat" |
| S-m3 | fixed | "If a mechanism like this exists, this threat could be most credible" |
| S-m4 | fixed | "may turn out to be a contest of nerves" |
| S-m5 | fixed | "not an unusually cynical view"; "manifestly somewhat beyond" |
| S-m6 | fixed | Deter = "keeping him from starting something"; compel = "do, or cease doing, something" |
| S-m7 | not fixed | Coverage: seven omitted examples. Adding them is not a one-line fix. |
| S-m8 | fixed | Extrication sentence moved before "One does not expect a government…" |
| S-m9 | fixed (partly) | Glosses added for massive retaliation, graduated reprisal and satellites, using the source's own wording. Quemoy is left unglossed because the source does not describe it. |
| S-m10 | fixed | First-person note replaced with the p. 218 misprint note |

### Zaller ch. 8: 9 fixes
| ID | Status | Note |
|---|---|---|
| Z-M1 | fixed | Bold lead: "**Age need not mean resistance.**" (p. 180) |
| Z-m1 | fixed | "Older Republicans"; "presumably" restored |
| Z-m2 | fixed | "six panels of change curves, cells A–F" |
| Z-m3 | fixed | "partisan-resistance evidence helpful but not clinching" |
| Z-m4 | fixed | Meta sentence removed. Eq. 7.5 confirmed against the p. 154 image, and the Reading note now says so. |
| Z-m5 | fixed | Fn. 6 described as a condition |
| Z-m6 | fixed | Reading note added on the p. 155 "higher" vs fn. 5 inconsistency (image checked) |
| Z-m7 | fixed | Small-N caveat added (p. 175) |
| Z-m8 | fixed | L1: "no one piece of it conclusive" |
| Z-m9 | not fixed | Coverage and verbatim spans across several pages. Not a one-line fix. |

### Quine 1951: 12 fixes
| ID | Status | Note |
|---|---|---|
| Q-M1 | fixed | L2: "If Quine's view is right ... given drastic enough adjustments elsewhere" (p. 40) |
| Q-M2 | fixed | Concepts line rewritten to match p. 30 |
| Q-M3 | fixed | Definitions added for Platonic ideas, definiendum, definiens, sense-datum, truth functions, quantification, contextually definable singular terms, biconditional and incomplete symbols |
| Q-m1 | fixed | L1: "long left Carnap's philosophy, but a subtler form survives". L1 is 118 words. |
| Q-m2 | fixed | "Not flatly circular, but something like it" is now tied to the interchangeability argument (p. 29); the conventional-notation exception is in L2 |
| Q-m3 | fixed (wording) | "felt to have a sharper empirical reference than highly theoretical statements". The hallucination example was not added because it is coverage. |
| Q-m4 | fixed | L3 now says "fell short ... not merely through sketchiness but in principle" (p. 37) |
| Q-m5 | fixed | "our statements about the external world"; credit to Carnap's *Aufbau* added |
| Q-m6 | fixed | "Under this view" added in L2 and L3 |
| Q-m7 | fixed | "(canon link; not stated in this unit)" added to three Concepts lines |
| Q-m8 | not fixed | Coverage: five omitted lines. Not a one-line fix. |
| Q-m9 | fixed | Unquoted verbatim span reworded in my own words |
| Q-m10 | fixed | "printed = pdf + 18" |

### Pearl ch. 6: 7 fixes
| ID | Status | Note |
|---|---|---|
| PE-M1 | fixed | Definitions added for belief propagation, explain-away effect, do-operator, M-bias and direct effect. "Bayesian network" does not appear in the digest. |
| PE-m1 | fixed | L3 Opening: "Like optical illusions, they also reveal how the brain works" |
| PE-m2 | fixed | "to some extent, ongoing"; the "refused to believe ... 1979" point added |
| PE-m3 | fixed | "when properly interpreted ... causal, not classical, logic" |
| PE-m4 | fixed | L2: "In his examples" |
| PE-m5 | not fixed | Coverage: four omitted points. Not a one-line fix. |
| PE-m6 | fixed | Unquoted 17-word span reworded |
| PE-m7 | fixed | First person removed from Reading notes |

### Rogers ch. 6 pt 1: 11 fixes
| ID | Status | Note |
|---|---|---|
| R-M1 | fixed | Solar rebates: "became too costly and were halted once 5 or 10 percent"; the 20% hypothetical and the pump-priming rationale restored (pdf 306–307) |
| R-M2 | fixed | Miracle rice condition restored (pdf 310) |
| R-M3 | fixed | Definitions added for individual-optional, awareness-knowledge, side-dressing, anhydrous ammonia, rationality (objective vs subjective), pump-priming and cue-to-action |
| R-m1 | fixed | L2 b1 now also cites pdf 297 and 309 |
| R-m2 | fixed | "lead to adoption by people different from those who would otherwise adopt" |
| R-m3 | fixed | "implies that one role"; "sometimes bought when ... cannot be justified"; "major problem in some fields" |
| R-m4 | fixed | "may affect the rate"; "often involves serious ethical issues" |
| R-m5 | fixed | "imbalance may be disappearing" added |
| R-m6 | not fixed | Coverage: five omitted points. Not a one-line fix. |
| R-m7 | fixed | `[[adopter-categories]]` now gives the definition as used, then the finding |
| R-m8 | not fixed | The toy example is stipulated and already labelled "illustrative only". Redesigning it is not a wording fix. |
| R-m9 | fixed | First person removed. The lakh error is stated as a source error (a lakh is 100,000). |
| R-m10 | fixed | Loaf-of-bread reason added (pdf 311) |

## Disagreements with the audit
None. Every item listed as not fixed was skipped for scope (coverage, length or restructuring), not because I think the finding is wrong.
