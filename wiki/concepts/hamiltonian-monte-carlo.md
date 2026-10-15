---
id: hamiltonian-monte-carlo
type: concept
fields: [bayesian, information-theory, llm]
fields_strong: [bayesian, information-theory, llm]
n_sources: 21
n_works: 7
tiers: [core, reference, deep]
grounding: digests
sources: [betancourt-2017-hmc/main-p2, betancourt-2017-hmc/main-p3, blei-2017-variational/main-p1, gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch10-introduction, gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch15-hierarchical, gelman-2020-workflow/main-p1, mackay-2003-information/ch30-efficient, mackay-2003-information/ch41-learning, mcelreath-2020-rethinking/ch08-markov, mcelreath-2020-rethinking/ch10-counting, mcelreath-2020-rethinking/ch12-multilevel, mcelreath-2020-rethinking/ch14-missing, murphy-2023-pml2/ch03-statistics-p2, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch12-markov-p1, murphy-2023-pml2/ch12-markov-p2, murphy-2023-pml2/ch13-sequential, murphy-2023-pml2/ch17-bayesian, murphy-2023-pml2/ch18-gaussian-p2]
aliases: [hamiltonian-monte-carlo-hmc-nuts, hamiltonian-monte-carlo-nuts]
raw_ids: [Hamiltonian Monte Carlo]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# hamiltonian-monte-carlo

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `hamiltonian-monte-carlo-hmc-nuts` — 4 digest(s)
- `hamiltonian-monte-carlo-nuts` — 1 digest(s)

## Canon spine entry

- **Hamiltonian Monte Carlo (HMC/NUTS)** (bayesian): uses gradients and simulated physics to make long, efficient moves through the typical set (grad)

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p2]] (p. 26): MCMC that lifts $q$ to phase space, runs Hamiltonian trajectories, and projects back (p. 26). Canon id: Hamiltonian Monte Carlo (HMC/NUTS).
- [[betancourt-2017-hmc/main-p3]] (pp. 41, 47): HMC/NUTS: MCMC that follows Hamiltonian trajectories, then corrects with weighted state sampling
- [[blei-2017-variational/main-p1]] (p. 16): an MCMC method that uses gradients of the log density; the Stan sampler (legend: NUTS, the No-U-Turn Sampler, a self-tuning HMC variant) used as the comparison baseline in Figure 6
- [[gelman-2013-bda3/appc-computation]] (pp. 603–607): MCMC with gradient-based leapfrog trajectories; coded by hand in C.4 and used in Stan via NUTS
- [[gelman-2013-bda3/ch10-introduction]] (pp. 262, 269): mentioned only as the engines of Bugs and Stan, developed in later chapters
- [[gelman-2013-bda3/ch12-computationally]] (pp. 300–302): Metropolis on $(\theta,\phi)$ with leapfrog trajectories using $\nabla\log p$; "hybrid Monte Carlo"
- [[gelman-2013-bda3/ch15-hierarchical]] (p. 392, 394): preferred sampler here; parameterization $\theta_j=\mu+\tau\eta_j$ helps
- [[gelman-2020-workflow/main-p1]] (p. 13): a generalisation of Metropolis that uses gradients to move efficiently in continuous spaces [alias `hamiltonian-monte-carlo-hmc-nuts`]
- [[mcelreath-2020-rethinking/ch08-markov]] (pp. 246–247): simulates a frictionless particle on the log-posterior; needs continuous parameters and tuning [alias `hamiltonian-monte-carlo-hmc-nuts`]
- [[mcelreath-2020-rethinking/ch10-counting]] (p. 320): handles correlated posteriors but is less efficient with them [as `Hamiltonian Monte Carlo`]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (p. 376): said to handle tens of thousands of varying effects [alias `hamiltonian-monte-carlo-nuts`]
- [[mcelreath-2020-rethinking/ch14-missing]] (p. 428): `adapt_delta` is raised from 0.8 to 0.95; without that, a few (harmless here) divergent iterations appear
- [[murphy-2023-pml2/ch03-statistics-p2]] (p. 109): gradient-based MCMC used for hierarchical posteriors, on transformed unconstrained parameters
- [[murphy-2023-pml2/ch07-inference]] (p. 355): gradient-guided proposals
- [[murphy-2023-pml2/ch12-markov-p1]] (pp. 517–520): momentum auxiliary variable; leapfrog trajectory plus MH correction
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 524): here: needs discrete variables marginalized and unconstrained continuous ones [alias `hamiltonian-monte-carlo-hmc-nuts`]
- [[murphy-2023-pml2/ch13-sequential]] (pp. 565–566): used as SMC moves; HMC alone gets stuck on the bimodal example
- [[murphy-2023-pml2/ch17-bayesian]] (p. 655): HMC, "generally considered the gold standard" for BNN posteriors; needs the full data at each step [work fields: bayesian, llm]
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 720): one option for sampling kernel hyperparameters

### information-theory

- [[mackay-2003-information/ch30-efficient]] (pp. 387–389): Metropolis method using gradient dynamics with momentum variables $\mathbf p$; original name "hybrid Monte Carlo" [alias `hamiltonian-monte-carlo-hmc-nuts`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch41-learning]] (p. 500): many gradient steps per proposal; less random-walk behaviour [work fields: information-theory, bayesian, llm]
