---
id: stationary-distribution
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 3
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch04-entropy, gelman-2013-bda3/ch11-basics, murphy-2023-pml2/ch02-probability-p3]
generated_by: build_kg.py
---

# stationary-distribution

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch11-basics]] (pp. 275, 279): a distribution unchanged by a chain step; the posterior must be the unique one [new]
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 52): $\boldsymbol\pi=\boldsymbol\pi\mathbf A$; the long-run distribution when it exists [new]

### information-theory

- [[cover-2006-elements/ch04-entropy]] (p. 61): state distribution unchanged by one step; with it as initial law the chain is stationary [new]

## Instances that use it

- [[reducible-four-state-chain-fig-2-18b]] — absorbing state, two stationary distributions, transient state 3 — from [[murphy-2023-pml2/ch02-probability-p3]]
- [[integer-random-walk]] — irreducible but non-recurrent for $p\ne0.5$; recurrent but no stationary distribution at $p=0.5$ — from [[murphy-2023-pml2/ch02-probability-p3]]

## Candidate bridges

- [same-math] Column-stochastic $A$, eigenvalue 1 ↔ Markov chains: stationary distribution — the paper mentions Markov chains and gives the surfer reading (p. 1, 3, 10) — from [[bryan-2006-eigenvector/main]] (linear-algebra → other:probability)
- [structural-analogy] Monotone fall of $D(\mu_n\|\mu)$ under a Markov transition ↔ convergence of Markov-chain simulation toward its stationary distribution: both are about a distribution approaching a fixed point. — from [[cover-2006-elements/ch02-entropy]] (information-theory → other:convergence-of-markov-chain)
- [same-math] Invariant distribution as principal right-eigenvector of $\mathbf{Q}$ ↔ bayesian: MCMC stationary distribution — the same linear-algebra fact about Markov chains. — from [[mackay-2003-information/ch51-appendices]] (information-theory → bayesian)
- [same-math] stationary distribution of a chain ↔ Bayesian: MCMC — the target posterior is made the stationary distribution of a chain (the unit only says MCMC is an application, p. 51). — from [[murphy-2023-pml2/ch02-probability-p3]] (bayesian → bayesian)
- [same-math] stationary distribution $\mu_\pi$ in (10.8) ↔ Markov chains: a fixed point of the transition operator. — from [[sutton-2018-rl/ch10-policy]] (control-theory → other:probability)
- [structural-analogy] $P=D^{-1}W$ and stationary $\pi$ ↔ PageRank / Markov steady state: a similar random-walk transition matrix and stationary distribution. — from [[vonluxburg-2007-spectralclustering/main]] (linear-algebra → other:pagerank-markov-steady-state)
