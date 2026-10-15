---
id: effective-sample-size
type: concept
fields: [bayesian, control-theory]
n_sources: 6
tiers: [core, deep, reference]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch10-introduction, gelman-2013-bda3/ch11-basics, murphy-2023-pml2/ch13-sequential, sarkka-2023-bayesianfiltering/ch11-particle]
generated_by: build_kg.py
---

# effective-sample-size

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (p. 11): $N/(1+2\sum\rho_l)$; exact-sample equivalent of a chain [new]
- [[gelman-2013-bda3/appc-computation]] (pp. 594, 598): n_eff: crude measure of effective sample size; itself a random variable [new]
- [[gelman-2013-bda3/ch10-introduction]] (p. 266): $S_{\rm eff}=1/\sum\tilde w^2$ for normalized importance weights; rough guide (p. 266) (new)
- [[gelman-2013-bda3/ch11-basics]] (pp. 286–287): n_eff = mn/(1 + 2Σρ_t), the equivalent number of independent draws for estimating the posterior mean [new]
- [[murphy-2023-pml2/ch13-sequential]] (p. 553): $1/\sum W^2$; used to trigger resampling (p. 553); differs from the MCMC ESS [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch11-particle]] (p. 240): $1/\sum w^2$, used to trigger adaptive resampling [new]

## Candidate bridges

- [structural-analogy] n_eff for MCMC ↔ survey sampling: effective sample size under dependence, like cluster sampling (our link; the text compares only the var⁺ estimator to cluster sampling, p. 284). — from [[gelman-2013-bda3/ch11-basics]] (bayesian → other)
- [metaphor] "Premature optimization" in software engineering ↔ running MCMC to large effective sample size for an untested model — compute is wasted if bugs appear early (p. 14). — from [[gelman-2020-workflow/main-p1]] (bayesian → unspecified)
