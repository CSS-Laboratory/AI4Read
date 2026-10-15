---
id: inverse-cdf-sampling
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch01-probability, murphy-2023-pml2/ch11-monte]
generated_by: build_kg.py
---

# inverse-cdf-sampling

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch01-probability]] (p. 23): draw $U\sim$ Uniform(0,1) and return $F^{-1}(U)$ [new]
- [[murphy-2023-pml2/ch11-monte]] (p. 486): sample $u\sim U(0,1)$, return $F^{-1}(u)$ [new]

## Candidate bridges

- [same-math] Inverse-CDF sampling (D.3) ↔ simulation of any 1-D random variable — the same transformation. — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → unspecified)
- [structural-analogy] Latent-variable regression via $y=F_0^{-1}(u)$ ↔ inverse-CDF sampling (p. 515). — from [[gelman-2013-bda3/ch21-gaussian]] (bayesian → unspecified)
- [same-math] Arithmetic decoding as sampling ↔ simulation/statistics: inverse-CDF sampling from a cumulative-probability partition of [0,1) — random point plus cumulative intervals $[Q,R)$ yields a sample (p. 118). — from [[mackay-2003-information/ch06-stream]] (information-theory → other:statistics)
- [structural-analogy] inverse-cdf sampling via PIT ↔ Monte Carlo integration — turning uniform draws into draws from a target. — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → unspecified)
