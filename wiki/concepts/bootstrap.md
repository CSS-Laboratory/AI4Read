---
id: bootstrap
type: concept
fields: [bayesian]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch13-standardization, murphy-2023-pml2/ch03-statistics-p1]
generated_by: build_kg.py
---

# bootstrap

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch13-standardization]] (p. 180): resample the study population with replacement and use the spread of estimates as standard error [new]
- [[murphy-2023-pml2/ch03-statistics-p1]] (p. 74): Monte Carlo approximation of the sampling distribution; parametric or non-parametric [new]

## Instances that use it

- [[heart-attack-decision-tree]] — apparent 96.7% versus bootstrap about 70%; the likelihood is unaffected by how the tree was built — from [[efron-1986-bayesian/main]]
- [[bootstrap-vs-posterior-bernoulli]] — Fig. 3.4 with Ber(0.7) data — from [[murphy-2023-pml2/ch03-statistics-p1]]
- [[spiral-tracking-2d]] — nonlinear 2d tracking filtered by a bootstrap filter — from [[murphy-2023-pml2/ch13-sequential]]
- [[neural-decoding-poisson]] — guided vs bootstrap filter, ESS — from [[murphy-2023-pml2/ch13-sequential]]
- [[pendulum-tracking-bootstrap-pf]] — bootstrap PF with 10,000 particles, RMSE 0.10, approximately the same as the best Gaussian filters — from [[sarkka-2023-bayesianfiltering/ch11-particle]]
- [[bootstrap-filter]] — entry 11.9 — from [[sarkka-2023-bayesianfiltering/ch21-list]]

## Candidate bridges

- [structural-analogy] Monte Carlo $p$-value with refitting ↔ parametric bootstrap: simulate from the fitted model, repeat the same fit on each simulation — from [[clauset-2009-powerlaw/main-p1]] (complex-systems → other)
- [structural-analogy] Efron's tree: apparent vs bootstrap success rate ↔ machine learning: training error vs held-out error — both correct optimism from fitting and testing on the same data. — from [[efron-1986-bayesian/main]] (bayesian → other)
- [structural-analogy] posterior predictive p-value ↔ frequentist parametric-bootstrap goodness-of-fit: both simulate replicates from the fitted model, but the Bayesian one averages over the posterior and the bootstrap plugs in a point estimate (pp. 12, 15) — from [[gelman-2013-philosophy/main]] (bayesian → other)
- [structural-analogy] Bootstrap standard errors ↔ Bayesian posterior sampling: both use many simulated draws to describe uncertainty, though they target different things. — from [[hernan-2020-whatif/ch13-standardization]] (bayesian → bayesian)
- [structural-analogy] Bootstrap distribution ↔ Bayesian posterior sampling: both give a cloud of parameter values, from refitting vs from conditioning (p. 75). — from [[murphy-2023-pml2/ch03-statistics-p1]] (bayesian → bayesian)
- [metaphor] choosing λ between MC and TD ↔ control-theory: trade-off between trusting a model prediction (bootstrap) and measured outcomes (Kalman-gain-like weighting). — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → control-theory)
