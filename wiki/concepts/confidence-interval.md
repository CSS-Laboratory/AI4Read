---
id: confidence-interval
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch10-random, mackay-2003-information/ch37-bayesian, murphy-2023-pml2/ch03-statistics-p1]
generated_by: build_kg.py
---

# confidence-interval

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch10-random]] (pp. 138–139): interval whose level is coverage frequency over repeated samples; Wald form $\hat\theta\pm1.96\,\widehat{se}$ [new]
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 80): interval with (3.81) coverage over repeated datasets, not a probability for θ given D [new]

### information-theory

- [[mackay-2003-information/ch37-bayesian]] (p. 464): an interval computed from data. Its level is the fraction of repeated experiments in which it contains the true θ, for every θ [new; work fields: information-theory, bayesian]

## Instances that use it

- [[integer-theta-confidence-interval]] — a 75% interval with posterior probability 50% or 100% — from [[mackay-2003-information/ch37-bayesian]]
- [[dow-jones-confidence-intervals]] — overly tight subjective distributions — from [[tversky-1974-heuristics/main]]

## Candidate bridges

- [structural-analogy] Wald confidence interval (coverage over repeated samples) ↔ Bayesian: credible interval (probability statement given data and prior) — same-looking intervals with different meanings, as the chapter itself notes (p. 139). — from [[hernan-2020-whatif/ch10-random]] (bayesian → bayesian)
- [structural-analogy] Credible interval vs confidence interval in Fine Point 11.2 ↔ bayesian: credible intervals (probability as degree of belief) vs confidence intervals (probability as frequency). The definitions of probability differ, and coverage can differ in high dimensions. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [metaphor] Confidence intervals working until stretched ↔ bayesian: acceptable only where they agree with Bayesian intervals (p. 674). — from [[jaynes-2003-probability/appb-mathematical]] (bayesian → bayesian)
- [structural-analogy] Overly narrow confidence intervals ↔ machine-learning model calibration: stated confidence exceeds hit rate. — from [[kahneman-2011-thinking/appa-judgment]] (decision-game-theory → other:machine-learning-model-calibration)
- [structural-analogy] Confidence-interval "surprises" ↔ statistics: checking interval coverage against its nominal 80% level. — from [[kahneman-2011-thinking/ch24-engine]] (decision-game-theory → other:statistics)
- [structural-analogy] Confidence interval ↔ bayesian: credible interval — both give an interval, but one has coverage over repeated data and the other has posterior probability for this data set. — from [[mackay-2003-information/ch37-bayesian]] (information-theory → bayesian)
