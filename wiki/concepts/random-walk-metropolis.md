---
id: random-walk-metropolis
type: concept
fields: [bayesian]
n_sources: 2
tiers: [deep, reference]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, murphy-2023-pml2/ch12-markov-p1]
generated_by: build_kg.py
---

# random-walk-metropolis

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (pp. 15–16): Metropolis–Hastings with a Gaussian proposal; scales poorly with dimension [new]
- [[murphy-2023-pml2/ch12-markov-p1]] (p. 503): MH with $\mathcal N(x,\tau^2\mathbf I)$ proposal; $\tau$ sets mixing [new]

## Instances that use it

- [[random-walk-metropolis]] — non-gradient method with a smaller geometrically ergodic class than HMC — from [[betancourt-2017-hmc/main-p3]]
- [[correlated-bivariate-gaussian-rho-0998]] — benchmark target ($\rho=0.998$): HMC is compared with random-walk Metropolis (Fig. 30.2) and overrelaxation with Gibbs sampling (Fig. 30.3) — from [[mackay-2003-information/ch30-efficient]]
