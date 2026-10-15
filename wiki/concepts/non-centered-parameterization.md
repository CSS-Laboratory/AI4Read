---
id: non-centered-parameterization
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 5
n_works: 3
tiers: [reference, core]
grounding: digests
sources: [gelman-2013-bda3/appc-computation, mcelreath-2020-rethinking/ch13-adventures, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch12-markov-p2, murphy-2023-pml2/ch15-generalized]
generated_by: build_kg.py
---

# non-centered-parameterization

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/appc-computation]] (pp. 592, 607): θ = μ + τη with η ~ N(0,1); this is "better behaved" for HMC [new]
- [[mcelreath-2020-rethinking/ch13-adventures]] (pp. 408–409): move means, standard deviations and (via Cholesky) correlations out of the prior into the linear model, leaving standardized z-scores [new]
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 113): $\theta_j=\mu+\tau\eta_j$ to avoid the funnel [new]
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 532): sample standardized $z$ and set $x=z\exp(\nu)$ [new]
- [[murphy-2023-pml2/ch15-generalized]] (p. 629): $\beta_j=\mu_\beta+\tilde\beta_j\sigma_\beta$ to avoid Neal's funnel [new]

## Instances that use it

- [[eight-schools]] — hierarchical Gaussian, funnel and non-centered parameterization — from [[murphy-2023-pml2/ch03-statistics-p2]]

## Candidate bridges

- [structural-analogy] Non-centered parameterization ↔ variational inference: reparameterizing a random variable as a deterministic transform of fixed noise (canon link; not stated in this unit). — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → bayesian)
