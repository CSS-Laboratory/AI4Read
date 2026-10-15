---
id: probability-integral-transform
type: concept
fields: [bayesian, linear-algebra]
fields_strong: [bayesian, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p2, murphy-2023-pml2/ch02-probability-p3]
generated_by: build_kg.py
---

# probability-integral-transform

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch02-probability-p3]] (p. 45): $P_X(X)\sim\mathrm{Unif}(0,1)$; basis of KS test and inverse-cdf sampling [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p2]] (p. 216): $F_X(X)$ is uniform [new]

## Candidate bridges

- [structural-analogy] Encoding with the cdf to get a uniform output ↔ statistics: probability integral transform — same change-of-variables idea. — from [[stone-2022-information/ch07-channel]] (information-theory → other:statistics)
- [same-math] cdf encoder $g^*(s)=\int p_s$ giving uniform output ↔ statistics: probability integral transform / histogram equalisation — the same transformation of a variable into a uniform one. — from [[stone-2022-information/ch11-information]] (information-theory → other:statistics)
