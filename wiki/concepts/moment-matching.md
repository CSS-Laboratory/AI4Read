---
id: moment-matching
type: concept
fields: [bayesian, control-theory]
n_sources: 4
tiers: [reference, deep]
grounding: digests
sources: [murphy-2023-pml2/ch02-probability-p2, murphy-2023-pml2/ch04-graphical-p2, murphy-2023-pml2/ch26-generative, sarkka-2023-bayesianfiltering/ch08-general]
generated_by: build_kg.py
---

# moment-matching

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch02-probability-p2]] (p. 42): at the MLE, model expectation of $\mathcal T$ equals the empirical average (new)
- [[murphy-2023-pml2/ch04-graphical-p2]] (p. 184): MLE condition: data feature expectation equals model feature expectation [new]
- [[murphy-2023-pml2/ch26-generative]] (p. 902): match expectations of test statistics $s$ (26.40) [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch08-general]] (p. 131): approximating a distribution by a Gaussian with its true mean and covariance, computed via integrals [new]

## Candidate bridges

- [structural-analogy] Cavity/tilted distribution and moment matching ↔ Gibbs-style "all others fixed" updates — each step updates one piece in the context of the rest. — from [[gelman-2013-bda3/ch13-modal]] (bayesian → unspecified)
- [same-math] Boltzmann-machine learning gradient (data minus model moments) ↔ information-theory: maximum-entropy / exponential-family fitting, where parameters are tuned until model expectations match data expectations — same moment-matching condition. — from [[mackay-2003-information/ch43-boltzmann]] (information-theory → information-theory)
- [same-math] Moment matching of a Gaussian mixture (8.204) ↔ law of total variance (8.183): both are $E[\mathrm{Cov}]+\mathrm{Cov}[E]$. — from [[murphy-2023-pml2/ch08-gaussian-p2]] (bayesian → other)
- [same-math] Blackbox shift estimation $\mu=Cq$ ↔ linear inverse problems / moment matching: observed prediction rates are a known linear mixture of the unknown label prior. The author calls it moment matching (p. 750). — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → other)
- [structural-analogy] Moment matching to an assumed density ↔ approximate inference: fitting a Gaussian to match mean and covariance of an intractable posterior. — from [[sarkka-2023-bayesianfiltering/ch08-general]] (control-theory → other)
