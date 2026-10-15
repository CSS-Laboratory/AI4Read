---
id: parameter-expansion
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch15-hierarchical]
generated_by: build_kg.py
---

# parameter-expansion

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/appc-computation]] (pp. 601–602): extra parameters α, γ with θ = μ + αγ, τ_θ = |α|τ, used for the normal model (pp. 598–599) and, for the t model, to make the computations more efficient [new]
- [[gelman-2013-bda3/ch12-computationally]] (p. 294): adding an unidentified parameter (e.g., $\alpha$) to break dependence and speed Gibbs [new]
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 393, 396): multiplicative auxiliary parameters that decouple coefficients from their variance, avoiding stickiness near $\sigma=0$ [new]

## Instances that use it

- [[t-model-as-normal-mixture]] — t likelihood written with auxiliary variances $V_i$; Gibbs steps, then parameter expansion with $\alpha$ — from [[gelman-2013-bda3/ch12-computationally]]

## Candidate bridges

- [structural-analogy] Parameter expansion (extra unidentified scale) ↔ hierarchical models: the chapter points to Section 15.5 for the hierarchical use. — from [[gelman-2013-bda3/ch12-computationally]] (bayesian → bayesian)
