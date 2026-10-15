---
id: metropolis-hastings
type: concept
fields: [bayesian, information-theory, control-theory]
n_sources: 23
tiers: [core, deep, reference]
grounding: digests
sources: [betancourt-2017-hmc/main-p1, betancourt-2017-hmc/main-p2, betancourt-2017-hmc/main-p3, gelman-2013-bda3/appc-computation, gelman-2013-bda3/ch11-basics, gelman-2013-bda3/ch12-computationally, gelman-2013-bda3/ch16-generalized, gelman-2013-bda3/ch17-models, gelman-2013-bda3/ch19-parametric, mackay-2003-information/ch29-monte, mackay-2003-information/ch30-efficient, mackay-2003-information/ch31-ising, mackay-2003-information/ch32-exact, mackay-2003-information/ch41-learning, mcelreath-2020-rethinking/ch08-markov, mcgrayne-2011-theory/ch16-eureka, murphy-2023-pml2/ch06-optimization-p2, murphy-2023-pml2/ch07-inference, murphy-2023-pml2/ch12-markov-p1, murphy-2023-pml2/ch12-markov-p2, murphy-2023-pml2/ch13-sequential, robert-2011-mcmc/main, sarkka-2023-bayesianfiltering/ch16-parameter]
raw_ids: [Metropolis–Hastings]
canon_spine: bayesian
generated_by: build_kg.py
---

# metropolis-hastings

## Canon spine entry

- **Metropolis–Hastings** (bayesian): propose a move and accept it with a probability ratio that keeps the target distribution invariant (grad)

## Definitions in the sources

### bayesian

- [[betancourt-2017-hmc/main-p1]] (p. 15): proposal plus accept/reject correction with the ratio above
- [[betancourt-2017-hmc/main-p2]] (p. 38): used here to correct integrator error, with a reversible proposal
- [[betancourt-2017-hmc/main-p3]] (p. 41): correction used in the simple static scheme; target acceptance 0.6–0.8
- [[gelman-2013-bda3/appc-computation]] (pp. 600–601): Metropolis step for 1/ν with a normal jump; about 44% acceptance is optimal for one parameter
- [[gelman-2013-bda3/ch11-basics]] (pp. 278–280): propose from J_t, accept with min(r,1); r uses (11.1) for symmetric J and (11.2) otherwise
- [[gelman-2013-bda3/ch12-computationally]] (p. 295): propose and accept/reject; many possible jumping rules $J_t$
- [[gelman-2013-bda3/ch16-generalized]] (p. 424): Metropolis runs for the meta-analysis
- [[gelman-2013-bda3/ch17-models]] (p. 440): Gibbs with mixture variables; Metropolis step for $\nu$
- [[gelman-2013-bda3/ch19-parametric]] (p. 482): normal proposal, acceptance rate about 0.23, one person at a time
- [[mcelreath-2020-rethinking/ch08-markov]] (pp. 243–245): propose a move; accept with probability from the target ratio. Plain Metropolis needs symmetric proposals; Hastings allows asymmetric ones
- [[mcgrayne-2011-theory/ch16-eureka]] (p. 223): algorithm from Metropolis (1953), generalized by Hastings (1970); gives estimates, not exact answers
- [[murphy-2023-pml2/ch06-optimization-p2]] (p. 307): simulated annealing uses a variant to sample $\exp(-\mathcal E)$ [as `Metropolis–Hastings`]
- [[murphy-2023-pml2/ch07-inference]] (pp. 354–355): accept moves using the unnormalised ratio (7.35)
- [[murphy-2023-pml2/ch12-markov-p1]] (pp. 500–501): propose from $q$, accept with $\min(1,\alpha)$; normalizer cancels
- [[murphy-2023-pml2/ch12-markov-p2]] (p. 536, 541): basis of RJMCMC and simulated annealing acceptance rules
- [[murphy-2023-pml2/ch13-sequential]] (pp. 565–566): used as SMC moves; HMC alone gets stuck on the bimodal example
- [[robert-2011-mcmc/main]] (p. 3): propose a move, accept with probability (1) or the generic $\alpha_{ij}$; Hastings (1970) generalised the rule

### information-theory

- [[mackay-2003-information/ch29-monte]] (p. 365–366): propose from Q(x'; x), accept with min(1, a), a from (29.31); a rejection repeats the state
- [[mackay-2003-information/ch30-efficient]] (pp. 389, 396): accept/reject rule used to correct inexact dynamics and in crossover moves
- [[mackay-2003-information/ch31-ising]] (p. 402): flip spin, accept with (31.20)
- [[mackay-2003-information/ch32-exact]] (p. 413): the 21-state Metropolis chain is the toy chain used throughout
- [[mackay-2003-information/ch41-learning]] (p. 496): accept/reject sampler used for the weights

### control-theory

- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (pp. 324–326): MCMC using only energy differences; adaptive (RAM) and Hamiltonian variants [new]

## Candidate bridges

- [same-math] Acceptance $\min(1,e^{-\Delta H})$ ↔ bayesian: Metropolis–Hastings ratio with a symmetric deterministic proposal. — from [[betancourt-2017-hmc/main-p2]] (bayesian → bayesian)
- [same-math] Gibbs step ↔ Metropolis-Hastings step: with proposal equal to the full conditional, r ≡ 1, as shown on p. 281. — from [[gelman-2013-bda3/ch11-basics]] (bayesian → other)
- [same-math] Gibbs/Metropolis–Hastings sampling ↔ the field's MCMC concepts: same algorithms as the Bayesian posterior-sampling toolkit. — from [[mcgrayne-2011-theory/ch16-eureka]] (bayesian → other)
- [structural-analogy] Simulated annealing ↔ MCMC: Metropolis–Hastings sampling from $\exp(-\mathcal E)$ with decreasing entropy. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → other)
- [same-math] Metropolis–Hastings acceptance ↔ Markov-chain reversibility: acceptance probability makes $\pi$ invariant (detailed balance). — from [[robert-2011-mcmc/main]] (bayesian → other)
