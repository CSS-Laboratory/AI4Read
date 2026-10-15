---
id: credible-interval
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 15
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch01-probability, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch04-asymptotics, gelman-2013-bda3/ch10-introduction, hernan-2020-whatif/ch10-random, hernan-2020-whatif/ch11-model, mcelreath-2020-rethinking/ch03-sampling, mcelreath-2020-rethinking/ch04-linear-p1, mcelreath-2020-rethinking/ch04-linear-p2, mcelreath-2020-rethinking/ch05-multivariate-p1, mcelreath-2020-rethinking/ch05-multivariate-p2, murphy-2023-pml2/ch03-statistics-p1, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch03-statistics-p3, murphy-2023-pml2/ch15-generalized]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# credible-interval

## Canon spine entry

- **Credible interval** (bayesian): an interval containing the parameter with a stated posterior probability, unlike a confidence interval's long-run coverage (UG)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (pp. 3, 24): the authors' term is Bayesian (probability) or posterior interval, e.g. central 95% from the 2.5% and 97.5% quantiles of draws
- [[gelman-2013-bda3/ch02-single]] (p. 33): here the central posterior interval, with α/2 posterior probability in each tail
- [[gelman-2013-bda3/ch04-asymptotics]] (p. 91): central posterior interval; asymptotically has the matching confidence coverage
- [[gelman-2013-bda3/ch10-introduction]] (p. 267): 50% and 95% posterior intervals read from the 25/75 and 2.5/97.5 percentiles of draws
- [[hernan-2020-whatif/ch10-random]] (p. 150): mentioned as an interval with "95% probability the estimand is in it" for a Bayesian (p. 139); highest posterior density intervals in Technical Point 10.7
- [[hernan-2020-whatif/ch11-model]] (p. 159): Bayesian interval with stated posterior probability of containing the estimand
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 54): posterior interval of defined mass; the author notes that "confidence interval" may be used interchangeably
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (pp. 85, 87): HPDI and percentile intervals computed from samples (here 89%)
- [[mcelreath-2020-rethinking/ch04-linear-p2]] (pp. 104, 107): here HPDI and PI of posterior samples; the author sometimes uses "confidence interval" for the same shaded bands
- [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (pp. 122, 125; "confidence" wording also pp. 132, 139): here an 89% percentile interval (5.5%–94.5%), sometimes called "confidence interval" in the text
- [[mcelreath-2020-rethinking/ch05-multivariate-p2]] (p. 154): percentile intervals (PI) from sampled posteriors, e.g. for the male mean
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 67): contiguous region with posterior mass 1−α; central or HPD
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 90): e.g. $\bar y\pm2s/\sqrt N$ under the Jeffreys prior
- [[murphy-2023-pml2/ch03-statistics-p3]] (pp. 133–134): $(P^{-1}(\alpha/2),P^{-1}(1-\alpha/2))$ from the posterior cdf; equals the confidence interval in the t-test case with noninformative prior
- [[murphy-2023-pml2/ch15-generalized]] (pp. 601, 619): 89%/95% intervals for weights and differences

## Candidate bridges

- [structural-analogy] Wald confidence interval (coverage over repeated samples) ↔ Bayesian: credible interval (probability statement given data and prior) — same-looking intervals with different meanings, as the chapter itself notes (p. 139). — from [[hernan-2020-whatif/ch10-random]] (bayesian → bayesian)
- [structural-analogy] Credible interval vs confidence interval in Fine Point 11.2 ↔ bayesian: credible intervals (probability as degree of belief) vs confidence intervals (probability as frequency). The definitions of probability differ, and coverage can differ in high dimensions. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [metaphor] Bounds from partial identification ↔ Bayesian credible intervals: both express an honest range, but the bounds carry no probability. — from [[hernan-2020-whatif/ch16-instrumental]] (bayesian → bayesian)
- [structural-analogy] Confidence interval ↔ bayesian: credible interval — both give an interval, but one has coverage over repeated data and the other has posterior probability for this data set. — from [[mackay-2003-information/ch37-bayesian]] (information-theory → bayesian)
- [structural-analogy] Optimism in the face of uncertainty ($\hat\mu+c\hat\sigma$) ↔ credible intervals: the bonus is a scaled posterior sd, i.e. an upper bound on the interval. — from [[murphy-2023-pml2/ch34-decision]] (bayesian → bayesian)
