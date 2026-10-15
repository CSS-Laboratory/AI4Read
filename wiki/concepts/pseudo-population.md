---
id: pseudo-population
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch08-selection, hernan-2020-whatif/ch12-ip]
generated_by: build_kg.py
---

# pseudo-population

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch02-randomized]] (p. 22): hypothetical population where each person appears under each treatment [new]
- [[hernan-2020-whatif/ch08-selection]] (p. 118): reweighted copy of the population in which nobody is censored [new]
- [[hernan-2020-whatif/ch12-ip]] (p. 164–165): the weighted copy of the data in which treatment no longer depends on $L$; association is causation there if conditional exchangeability holds [new]

## Candidate bridges

- [structural-analogy] Stabilized weights with mean 1 ↔ normalizing constant: dividing by $\mathrm E[g(A)I/f]$ keeps pseudo-population size fixed, like normalizing weights. — from [[hernan-2020-whatif/ch12-ip]] (bayesian → other:normalizing-constant)
