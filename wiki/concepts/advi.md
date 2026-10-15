---
id: advi
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch10-variational-p1]
generated_by: build_kg.py
---

# advi

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch07-inference]] (p. 354): VI after mapping to unconstrained space, with automatic differentiation [new]
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 452): Gaussian VI on parameters transformed to $\mathbb R^D$ by a bijection [new]

## Instances that use it

- [[beta-bernoulli-10-heads-1-tail]] — running example used for grid, Laplace, ADVI and HMC — from [[murphy-2023-pml2/ch07-inference]]
- [[advi-beta-binomial]] — Gaussian in logit-like space approximates a skewed Beta posterior — from [[murphy-2023-pml2/ch10-variational-p1]]
- [[advi-gmm-old-faithful]] — K=10 mixture, Bayesian fit prefers 2 components, MAP shows no sparsity — from [[murphy-2023-pml2/ch10-variational-p1]]
