---
id: markov-chain-monte-carlo
type: concept
fields: [bayesian, information-theory, llm]
fields_strong: [bayesian, information-theory, llm]
n_sources: 26
n_works: 9
tiers: [core, reference, deep]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, blei-2017-variational/main-p1, gelman-2013-bda3/ch10-introduction, gelman-2013-bda3/ch11-basics, gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch13-modal, gelman-2013-bda3/ch21-gaussian, gelman-2020-workflow/main-p1, gelman-2020-workflow/main-p3, mackay-2003-information/ch29-monte, mackay-2003-information/ch30-efficient, mackay-2003-information/ch32-exact, mackay-2003-information/ch44-supervised, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch03-sampling, mcelreath-2020-rethinking/ch08-markov, mcelreath-2020-rethinking/ch12-multilevel, mcgrayne-2011-theory/ch16-eureka, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch12-markov-p1, murphy-2023-pml2/ch12-markov-p2, murphy-2023-pml2/ch18-gaussian-p2, murphy-2023-pml2/ch24-energy, murphy-2023-pml2/ch25-diffusion, robert-2011-mcmc/main]
aliases: [markov-chain-monte-carlo-mcmc, mcmc]
canon_spine: [bayesian]
generated_by: build_kg.py
---

# markov-chain-monte-carlo

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `markov-chain-monte-carlo-mcmc` — 10 digest(s)
- `mcmc` — 4 digest(s)

## Canon spine entry

- **Markov chain Monte Carlo (MCMC)** (bayesian): constructing a random walk whose long-run distribution is the posterior, so its states are posterior samples (grad)

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (pp. 9–10): a chain whose transition preserves the target; its history estimates expectations
- [[blei-2017-variational/main-p1]] (pp. 2–3): the baseline: sample an ergodic chain with the posterior as stationary law; asymptotically exact but heavier [alias `markov-chain-monte-carlo-mcmc`]
- [[gelman-2013-bda3/ch10-introduction]] (pp. 262, 269): mentioned only as the engines of Bugs and Stan, developed in later chapters
- [[gelman-2013-bda3/ch11-basics]] (pp. 275–276): Markov chain Monte Carlo: sequential draws whose distribution converges to p(θ|y); the Markov property helps prove this but is not the key [alias `mcmc`]
- [[gelman-2013-bda3/ch12-computationally]] (p. 293): random walk whose long-run distribution is the posterior; this chapter is about making it efficient
- [[gelman-2013-bda3/ch13-modal]] (pp. 311, 330): approximations serve as starting points and comparison points for Markov chain simulation [alias `mcmc`]
- [[gelman-2013-bda3/ch21-gaussian]] (pp. 505, 510): slice sampler, elliptic slice, scaled MH, scaled HMC/NUTS for GPs
- [[gelman-2020-workflow/main-p1]] (p. 14): approximation whose theoretical error goes to zero with more draws; here mostly HMC [alias `markov-chain-monte-carlo-mcmc`]
- [[gelman-2020-workflow/main-p3]] (pp. 60, 62): chains may not forget starting points in finite time, so starts are a tuning choice
- [[mcelreath-2020-rethinking/ch02-small]] (p. 44–45): conditioning engine that draws samples from the posterior instead of computing it directly
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 51): a family of methods; some of the most capable posterior-computation methods produce only samples, and many of these are MCMC variants, used from Chapter 8 [alias `markov-chain-monte-carlo-mcmc`]
- [[mcelreath-2020-rethinking/ch08-markov]] (p. 241, 245): a random walk whose long-run visits follow the posterior, so its states are posterior samples [alias `markov-chain-monte-carlo-mcmc`]
- [[mcelreath-2020-rethinking/ch12-multilevel]] (p. 360): used here because MAP cannot average over the second level
- [[mcgrayne-2011-theory/ch16-eureka]] (p. 221): replace integration by long chains of simple draws, each depending on the previous value
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 51): only mentioned as an application of stationary distributions [alias `markov-chain-monte-carlo-mcmc`]
- [[murphy-2023-pml2/ch07-inference]] (pp. 354–355): random walk whose visit frequencies are proportional to the posterior probability if the proposal is chosen carefully
- [[murphy-2023-pml2/ch12-markov-p1]] (p. 499): random walk whose stationary distribution is the target; correlated samples
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 524): here with focus on when its samples are valid [alias `markov-chain-monte-carlo-mcmc`]
- [[murphy-2023-pml2/ch18-gaussian-p2]] (p. 720): slice sampling, HMC and SMC are named options for kernel-parameter inference [alias `mcmc`]
- [[murphy-2023-pml2/ch24-energy]] (p. 852): sampling the EBM inside the training loop (p. 852) (reuse: Markov chain Monte Carlo) [alias `mcmc`; work fields: bayesian, llm]
- [[murphy-2023-pml2/ch25-diffusion]] (p. 874): Langevin sampling is mentioned as a score-based sampler [work fields: bayesian, llm]
- [[robert-2011-mcmc/main]] (p. 2): building a Markov chain whose stationary law is the target, to approximate integrals; traced here to 1953 [alias `markov-chain-monte-carlo-mcmc`]

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 366): generate dependent states from a chain whose long-run distribution is P [alias `markov-chain-monte-carlo-mcmc`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch30-efficient]] (p. 387): chains whose long-run distribution is the target; here the aim is fewer steps per independent sample [alias `markov-chain-monte-carlo-mcmc`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch32-exact]] (p. 413): Markov-chain sampler that can be guaranteed to produce samples from the target asymptotically. Run too short, it samples $P^{(T)}$, not $P$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch44-supervised]] (p. 531): Monte Carlo sampling named as one implementation [as `Markov chain Monte Carlo (MCMC)`; alias `markov-chain-monte-carlo-mcmc`; work fields: information-theory, bayesian, llm]

## Candidate bridges

- [same-math] Gibbs and Metropolis acceptance logic here ↔ Markov chain Monte Carlo (canon): the same algorithms, in code form. — from [[gelman-2013-bda3/appc-computation]] (bayesian → bayesian)
