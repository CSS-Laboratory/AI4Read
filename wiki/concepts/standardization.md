---
id: standardization
type: concept
fields: [bayesian, linear-algebra, llm]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [boyd-2018-vmls/ch03-norm, deisenroth-2020-mml/ch10-dimensionality, hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch13-standardization, mcelreath-2020-rethinking/ch04-linear-p2, prince-2023-udl/ch23-probability]
generated_by: build_kg.py
---

# standardization

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch02-randomized]] (p. 20): $\sum_l\Pr[Y=1\mid L=l,A=a]\Pr[L=l]$; the population is the standard [new]
- [[hernan-2020-whatif/ch13-standardization]] (p. 176): weighted average of stratum-specific outcome means, with weights equal to the distribution of $L$; estimates $E[Y^a]$ under identifiability conditions [new]
- [[mcelreath-2020-rethinking/ch04-linear-p2]] (p. 111): centering then dividing by SD; one unit = one SD; avoids numerical glitches with powers [new]

### linear-algebra

- [[boyd-2018-vmls/ch03-norm]] (p. 56): z = (x − avg(x)1)/std(x); mean 0, std 1; z-scores [new]
- [[deisenroth-2020-mml/ch10-dimensionality]] (p. 336): subtract the mean and divide by the standard deviation per dimension [new]

### llm

- [[prince-2023-udl/ch23-probability]] (p. 456): shift and scale to mean 0, variance 1 [new]

## Instances that use it

- [[smoking-cessation-weight-gain]] — NHEFS example: IP weighting and standardization both give 3.5 kg — from [[hernan-2020-whatif/ch13-standardization]]
- [[table-2-2-standardization]] — 20-person example, three-block recipe gives 0.5 and 0.5 — from [[hernan-2020-whatif/ch13-standardization]]

## Candidate bridges

- [structural-analogy] Standardization $\sum_l P(Y\mid L,a)P(L)$ ↔ bayesian: marginalising over a nuisance variable, as in a posterior predictive average — both average a conditional distribution over another variable's distribution. — from [[hernan-2020-whatif/ch02-randomized]] (bayesian → bayesian)
- [structural-analogy] Standardization $\sum_l \mathrm{E}[Y|A,L=l]\Pr[L=l]$ ↔ Bayesian inference: marginalizing a nuisance variable by averaging over its distribution. — from [[hernan-2020-whatif/ch07-confounding]] (bayesian → bayesian)
- [same-math] mediation formula as a g-formula ↔ potential outcomes: a standardization (mixing over $\Pr[M|A=0]$) of a conditional mean. — from [[hernan-2020-whatif/ch23-causal]] (bayesian → other)
- [structural-analogy] Indexing each variable to the group mean = 100 ↔ standardization (z-scores): both make different scales comparable around a centre, but here there is no division by spread, so the math differs. — from [[katz-1955-personalinfluence/appa-choice]] (communication-theory → other)
- [structural-analogy] Adjustment formula (4.16) and weights $P(z\mid x')$ in (4.21) ↔ marginalization over a confounder with different weights (standardization versus within-group weighting). — from [[pearl-2016-primer/ch04-counterfactuals]] (bayesian → unspecified)
- [same-math] Back-door formula (Eq. 7.2) ↔ standardization over covariate strata in potential-outcomes adjustment: a weighted average of stratum-specific conditional probabilities by the covariate distribution. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → other)
- [structural-analogy] Standardization $z=(x-\mu)/\sigma$ ↔ normalization layers in neural networks. — from [[prince-2023-udl/ch23-probability]] (llm → unspecified)
