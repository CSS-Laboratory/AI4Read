---
id: hamiltonian-monte-carlo-hmc-nuts
type: concept
fields: [bayesian, information-theory]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [gelman-2020-workflow/main-p1, mackay-2003-information/ch30-efficient, mcelreath-2020-rethinking/ch08-markov, murphy-2023-pml2/ch12-markov-p2]
canon_spine: bayesian
generated_by: build_kg.py
---

# hamiltonian-monte-carlo-hmc-nuts

## Canon spine entry

- **Hamiltonian Monte Carlo (HMC/NUTS)** (bayesian): uses gradients and simulated physics to make long, efficient moves through the typical set (grad)

## Definitions in the sources

### bayesian

- [[gelman-2020-workflow/main-p1]] (p. 13): a generalisation of Metropolis that uses gradients to move efficiently in continuous spaces
- [[mcelreath-2020-rethinking/ch08-markov]] (pp. 246–247): simulates a frictionless particle on the log-posterior; needs continuous parameters and tuning
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 524): here: needs discrete variables marginalized and unconstrained continuous ones

### information-theory

- [[mackay-2003-information/ch30-efficient]] (pp. 387–389): Metropolis method using gradient dynamics with momentum variables $\mathbf p$; original name "hybrid Monte Carlo"
