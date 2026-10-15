---
id: simulated-annealing
type: concept
fields: [bayesian, information-theory]
n_sources: 3
tiers: [core, deep, reference]
grounding: digests
sources: [mackay-2003-information/ch30-efficient, murphy-2023-pml2/ch12-markov-p2, robert-2011-mcmc/main]
generated_by: build_kg.py
---

# simulated-annealing

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch12-markov-p2]] (p. 540): MH with $p_T=\exp(-\mathcal E/T)$ and falling $T$ [new]
- [[robert-2011-mcmc/main]] (p. 3): Metropolis with changing $T$ ("cooling schedule") for optimisation [new]

### information-theory

- [[mackay-2003-information/ch30-efficient]] (p. 392): sample $P_T\propto e^{-E/T}$ with $T$ lowered to 1 (or 0 for optimization) [new]

## Instances that use it

- [[peaks-function-annealing]] — 2-d peaky target for simulated annealing — from [[murphy-2023-pml2/ch12-markov-p2]]

## Candidate bridges

- [structural-analogy] Simulated annealing temperature $T$ ↔ physics: Gibbs distribution at temperature $T$ — $e^{-E/T}$ flattens energy barriers. — from [[mackay-2003-information/ch30-efficient]] (information-theory → other)
- [structural-analogy] Simulated annealing ↔ MCMC: Metropolis–Hastings sampling from $\exp(-\mathcal E)$ with decreasing entropy. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → other)
- [metaphor] Simulated annealing temperature ↔ statistical physics: heating and slowly cooling a solid to a minimum-energy state. — from [[murphy-2023-pml2/ch12-markov-p2]] (bayesian → complex-systems)
- [structural-analogy] Learning rate schedule ↔ simulated annealing: large random moves early, small later — from [[prince-2023-udl/ch06-fitting]] (llm → other)
- [structural-analogy] Simulated annealing (varying $T$ in (1)) ↔ optimisation: random search with decreasing randomness; also SAEM, which reduces simulation noise toward EM. — from [[robert-2011-mcmc/main]] (bayesian → other)
