---
id: bayesian-model-averaging
type: concept
fields: [bayesian]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [mcgrayne-2011-theory/ch17-rosetta, murphy-2023-pml2/ch17-bayesian]
generated_by: build_kg.py
---

# bayesian-model-averaging

## Definitions in the sources

### bayesian

- [[mcgrayne-2011-theory/ch17-rosetta]] (p. 244): when two models that are not highly correlated are combined smartly, the result often beats either alone, per Volinsky [new]
- [[murphy-2023-pml2/ch17-bayesian]] (p. 647): predict by averaging $p(y|x,\theta)$ over the posterior, Eq. (17.1) [new]

## Candidate bridges

- [structural-analogy] Spike-and-slab inclusion indicators ↔ Bayesian model averaging over regressors: each γ indexes a model. — from [[gelman-2013-bda3/ch20-basis]] (bayesian → bayesian)
- [structural-analogy] Mixture code with $\log K$-bit header and incompleteness ↔ Bayesian: model averaging over $K$ models with a uniform prior. The source only points to bits-back coding (p. 108), so the link is ours. — from [[mackay-2003-information/ch05-symbol]] (information-theory → bayesian)
- [structural-analogy] dropout ensemble ↔ Bayesian model averaging (Monte Carlo dropout, Ch. 17): both average over many networks; the chapter only points forward — from [[murphy-2023-pml2/ch16-deep]] (bayesian → bayesian)
