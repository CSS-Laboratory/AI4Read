---
id: heavy-tailed-prior
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch17-models, murphy-2023-pml2/ch03-statistics-p2]
generated_by: build_kg.py
---

# heavy-tailed-prior

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch17-models]] (p. 436): long-tailed (t, Cauchy, mixture) exchangeable population model; an extreme observation is shrunk somewhat but proportionally much less than the others are shrunk toward each other [new]
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 100): e.g. Cauchy; heavy tails tend to make results more data-sensitive (in Berger's example, Cauchy gives about 4.6 vs 3.43 for the Gaussian prior) [new]

## Candidate bridges

- [structural-analogy] Heavy-tailed prior on group effects ↔ Hierarchical models: tail shape of the population distribution sets how strongly extreme groups are shrunk — from [[gelman-2013-bda3/ch17-models]] (bayesian → bayesian)
