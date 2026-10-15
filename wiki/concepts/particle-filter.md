---
id: particle-filter
type: concept
fields: [control-theory, bayesian]
n_sources: 5
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch13-sequential, sarkka-2023-bayesianfiltering/ch11-particle, sarkka-2023-bayesianfiltering/ch17-epilogue, sarkka-2023-bayesianfiltering/ch20-list, sarkka-2023-bayesianfiltering/ch21-list]
generated_by: build_kg.py
---

# particle-filter

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch11-particle]] (pp. 239–240): SIR: SIS plus (adaptive) resampling [new]
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 350): Monte Carlo filter for models outside the Gaussian framework; the bootstrap filter is the easiest [new]
- [[sarkka-2023-bayesianfiltering/ch20-list]] (p. 394): named in 11.10, 11.11; no definition here [new]
- [[sarkka-2023-bayesianfiltering/ch21-list]] (p. 398–399): Ch. 11 entries [new]

### bayesian

- [[murphy-2023-pml2/ch13-sequential]] (p. 543): SMC where each marginal $\pi_t(z_t)$ matters, e.g. filtering in SSMs [new]

## Instances that use it

- [[inverse-chi-squared-measurement-noise]] — Rao–Blackwellized particle filter with Student's t predictive — from [[sarkka-2023-bayesianfiltering/ch16-parameter]]

## Candidate bridges

- [structural-analogy] Particle filter weight degeneracy ↔ importance sampling in high dimension: both have weights concentrating on one draw. — from [[robert-2011-mcmc/main]] (bayesian → other)
- [structural-analogy] particle filter ↔ observer / state estimator: a model run forward and corrected by measurements, here for non-linear and non-Gaussian systems. — from [[sarkka-2023-bayesianfiltering/ch11-particle]] (control-theory → other)
