---
id: detailed-balance
type: concept
fields: [bayesian, information-theory]
n_sources: 5
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch12-computationally, mackay-2003-information/ch29-monte, mackay-2003-information/ch30-efficient, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch12-markov-p1]
generated_by: build_kg.py
---

# detailed-balance

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch12-computationally]] (p. 304): flow of probability from A to B equals that from B to A; used to prove the target is stationary [new]
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 55): $\pi_iA_{ij}=\pi_jA_{ji}$; sufficient, not necessary, for stationarity of regular chains [new]
- [[murphy-2023-pml2/ch12-markov-p1]] (p. 501): $p(x'|x)p^*(x)=p(x|x')p^*(x')$; implies $p^*$ is stationary [new]

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 374): T(a;b)P(b) = T(b;a)P(a); implies invariance; defines reversible chains [new]
- [[mackay-2003-information/ch30-efficient]] (p. 391): reversibility condition; each coordinate update has it, the fixed-order sweep does not [new]

## Instances that use it

- [[three-state-chain-fig-2-18a]] — stationary $\boldsymbol\pi=[0.4,0.4,0.2]$; has stationarity without detailed balance — from [[murphy-2023-pml2/ch02-probability-p3]]

## Candidate bridges

- [same-math] Metropolis–Hastings acceptance ↔ Markov-chain reversibility: acceptance probability makes $\pi$ invariant (detailed balance). — from [[robert-2011-mcmc/main]] (bayesian → other)
