---
id: markov-chain-monte-carlo-mcmc
type: concept
fields: [bayesian, information-theory]
n_sources: 10
tiers: [core, reference, deep]
grounding: digests
sources: [blei-2017-variational/main-p1, gelman-2020-workflow/main-p1, mackay-2003-information/ch29-monte, mackay-2003-information/ch30-efficient, mackay-2003-information/ch44-supervised, mcelreath-2020-rethinking/ch03-sampling, mcelreath-2020-rethinking/ch08-markov, murphy-2023-pml2/ch02-probability-p3, murphy-2023-pml2/ch12-markov-p2, robert-2011-mcmc/main]
raw_ids: [Markov chain Monte Carlo (MCMC)]
canon_spine: bayesian
generated_by: build_kg.py
---

# markov-chain-monte-carlo-mcmc

## Canon spine entry

- **Markov chain Monte Carlo (MCMC)** (bayesian): constructing a random walk whose long-run distribution is the posterior, so its states are posterior samples (grad)

## Definitions in the sources

### bayesian

- [[blei-2017-variational/main-p1]] (pp. 2–3): the baseline: sample an ergodic chain with the posterior as stationary law; asymptotically exact but heavier
- [[gelman-2020-workflow/main-p1]] (p. 14): approximation whose theoretical error goes to zero with more draws; here mostly HMC
- [[mcelreath-2020-rethinking/ch03-sampling]] (p. 51): a family of methods; some of the most capable posterior-computation methods produce only samples, and many of these are MCMC variants, used from Chapter 8
- [[mcelreath-2020-rethinking/ch08-markov]] (p. 241, 245): a random walk whose long-run visits follow the posterior, so its states are posterior samples
- [[murphy-2023-pml2/ch02-probability-p3]] (p. 51): only mentioned as an application of stationary distributions
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 524): here with focus on when its samples are valid
- [[robert-2011-mcmc/main]] (p. 2): building a Markov chain whose stationary law is the target, to approximate integrals; traced here to 1953

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 366): generate dependent states from a chain whose long-run distribution is P
- [[mackay-2003-information/ch30-efficient]] (p. 387): chains whose long-run distribution is the target; here the aim is fewer steps per independent sample
- [[mackay-2003-information/ch44-supervised]] (p. 531): Monte Carlo sampling named as one implementation [as `Markov chain Monte Carlo (MCMC)`]
