---
id: weakly-informative-prior
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch05-hierarchical, gelman-2013-bda3/ch16-generalized, mcelreath-2020-rethinking/ch08-markov]
generated_by: build_kg.py
---

# weakly-informative-prior

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch02-single]] (pp. 51, 55): proper prior intentionally weaker than real knowledge, to regularize [new]
- [[gelman-2013-bda3/ch05-hierarchical]] (p. 132): a proper prior that only mildly constrains the posterior, not meant as real prior knowledge [new]
- [[gelman-2013-bda3/ch16-generalized]] (pp. 412, 416): default prior (Cauchy on standardized inputs) giving minimal information that constrains coefficients away from unrealistic extremes [new]
- [[mcelreath-2020-rethinking/ch08-markov]] (pp. 259–260): prior that gives a gentle nudge away from absurd values; in the examples it cured wild chains, though the likelihood washed it out [new]

## Instances that use it

- [[three-schools-half-cauchy]] — weakly informative prior needed for $J=3$ — from [[gelman-2013-bda3/ch05-hierarchical]]

## Candidate bridges

- [metaphor] Weakly informative prior as "regularization" ↔ penalized estimation: shared intent of keeping estimates in a sensible range. — from [[gelman-2013-bda3/ch02-single]] (bayesian → other)
