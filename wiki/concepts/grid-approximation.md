---
id: grid-approximation
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 7
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch02-single, gelman-2013-bda3/ch03-introduction, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch03-sampling, mcelreath-2020-rethinking/ch04-linear-p1, murphy-2023-pml2/ch07-inference]
generated_by: build_kg.py
---

# grid-approximation

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/appc-computation]] (p. 597): discretise τ, normalise on the log scale, and sample from the grid [new]
- [[gelman-2013-bda3/ch02-single]] (pp. 38–39): evaluate the unnormalized posterior on a grid and normalize [new]
- [[gelman-2013-bda3/ch03-introduction]] (p. 76): discrete approximation of the posterior on a grid, sampled via marginal-then-conditional draws with jitter [new]
- [[mcelreath-2020-rethinking/ch02-small]] (p. 39): posterior computed on a finite grid of parameter values: prior × likelihood, then standardise [new]
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 52): posterior computed on a grid of parameter values, then normalized [new]
- [[mcelreath-2020-rethinking/ch04-linear-p1]] (p. 83): compute the posterior on a grid of parameter pairs; brute force, rarely practical [new]
- [[murphy-2023-pml2/ch07-inference]] (p. 351): discretise parameter space, normalise numerically [new]

## Instances that use it

- [[coarse-grid-approximation]] — representative states on a coarse grid with proximity-based $\phi_{jy}$ — from [[bertsekas-2026-rlcourse/ch03-learning-p5]]

## Candidate bridges

- [same-math] Grid approximation ↔ numerical integration: evaluating a function at grid points and normalising by the sum approximates the integral in $\Pr(w)$ (not stated in this unit). — from [[mcelreath-2020-rethinking/ch02-small]] (bayesian → other:numerical-integration)
