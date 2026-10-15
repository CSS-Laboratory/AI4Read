---
id: leapfrog-integrator
type: concept
fields: [bayesian, information-theory]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch12-computationally, mackay-2003-information/ch30-efficient, murphy-2023-pml2/ch12-markov-p1]
generated_by: build_kg.py
---

# leapfrog-integrator

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch12-computationally]] (p. 301): discrete half-step/full-step update of $\phi$ and $\theta$ approximating Hamiltonian dynamics [new]
- [[murphy-2023-pml2/ch12-markov-p1]] (p. 519): symmetric half-full-half integrator for Hamilton's equations [new]

### information-theory

- [[mackay-2003-information/ch30-efficient]] (p. 388): half-step, full-step, half-step scheme to simulate Hamiltonian dynamics [new]

## Instances that use it

- [[leapfrog-integrator]] — three-line half-step/full-step algorithm — from [[betancourt-2017-hmc/main-p2]]
