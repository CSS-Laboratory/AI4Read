---
id: empirical-bayes
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 6
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch05-hierarchical, mcgrayne-2011-theory/app-appendixes, mcgrayne-2011-theory/ch10-46, mcgrayne-2011-theory/ch13-cold, mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch03-statistics-p3]
generated_by: build_kg.py
---

# empirical-bayes

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch05-hierarchical]] (p. 104): estimating prior parameters from the data by a point estimate; viewed as approximating full hierarchical Bayes [new]
- [[mcgrayne-2011-theory/app-appendixes]] (p. 254): using earlier studies to inform one's priors [new]
- [[mcgrayne-2011-theory/ch10-46]] (p. 134): estimate priors from relative frequencies, then apply Bayes' rule [new]
- [[mcgrayne-2011-theory/ch13-cold]] (p. 168): prior built from past data, e.g. earlier election results (Fienberg's description of NBC polling) [new]
- [[mcgrayne-2011-theory/ch17-rosetta]] (pp. 243–244): initial priors estimated from frequencies, as in the Netflix winner [new]
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 114): estimate hyperparameters from data (by maximizing marginal likelihood), then condition on them; approximation to full hierarchical Bayes [new]

## Candidate bridges

- [structural-analogy] Empirical Bayes as keeping the prior from carrying extra information ↔ hierarchical models: priors learned from data. — from [[efron-1986-bayesian/main]] (bayesian → bayesian)
