---
id: markov-chain-monte-carlo
type: concept
fields: [bayesian, information-theory]
n_sources: 12
tiers: [core, reference, deep]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, gelman-2013-bda3/ch10-introduction, gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch21-gaussian, gelman-2020-workflow/main-p3, mackay-2003-information/ch32-exact, mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch12-multilevel, mcgrayne-2011-theory/ch16-eureka, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch12-markov-p1, murphy-2023-pml2/ch25-diffusion]
generated_by: build_kg.py
---

# markov-chain-monte-carlo

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (pp. 9–10): a chain whose transition preserves the target; its history estimates expectations
- [[gelman-2013-bda3/ch10-introduction]] (pp. 262, 269): mentioned only as the engines of Bugs and Stan, developed in later chapters
- [[gelman-2013-bda3/ch12-computationally]] (p. 293): random walk whose long-run distribution is the posterior; this chapter is about making it efficient
- [[gelman-2013-bda3/ch21-gaussian]] (pp. 505, 510): slice sampler, elliptic slice, scaled MH, scaled HMC/NUTS for GPs
- [[gelman-2020-workflow/main-p3]] (pp. 60, 62): chains may not forget starting points in finite time, so starts are a tuning choice
- [[mcelreath-2020-rethinking/ch02-small]] (p. 44–45): conditioning engine that draws samples from the posterior instead of computing it directly
- [[mcelreath-2020-rethinking/ch12-multilevel]] (p. 360): used here because MAP cannot average over the second level
- [[mcgrayne-2011-theory/ch16-eureka]] (p. 221): replace integration by long chains of simple draws, each depending on the previous value
- [[murphy-2023-pml2/ch07-inference]] (pp. 354–355): random walk whose visit frequencies are proportional to the posterior probability if the proposal is chosen carefully
- [[murphy-2023-pml2/ch12-markov-p1]] (p. 499): random walk whose stationary distribution is the target; correlated samples
- [[murphy-2023-pml2/ch25-diffusion]] (p. 874): Langevin sampling is mentioned as a score-based sampler

### information-theory

- [[mackay-2003-information/ch32-exact]] (p. 413): Markov-chain sampler that can be guaranteed to produce samples from the target asymptotically. Run too short, it samples $P^{(T)}$, not $P$

## Candidate bridges

- [same-math] Gibbs and Metropolis acceptance logic here ↔ Markov chain Monte Carlo (canon): the same algorithms, in code form. — from [[gelman-2013-bda3/appc-computation]] (bayesian → other)
