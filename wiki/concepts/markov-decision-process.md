---
id: markov-decision-process
type: concept
fields: [control-theory, bayesian, llm]
n_sources: 17
tiers: [core, reference, deep]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p2, bellman-1957-dp/ch01-i-p3, bellman-1957-dp/ch03-iii, bellman-1957-dp/ch11-xi, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch02-approximation-p6, murphy-2023-pml2/ch34-decision, murphy-2023-pml2/ch35-reinforcement, ng-2000-irl/main, prince-2023-udl/ch19-reinforcement, recht-2019-tour/main, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch03-finite, sutton-2018-rl/ch04-dynamic, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch16-applications]
raw_ids: [Markov decision process, markov decision process]
canon_spine: control-theory
generated_by: build_kg.py
---

# markov-decision-process

## Canon spine entry

- **Markov decision process** (control-theory): states, actions, transition probabilities and rewards: the formal RL problem (UG)

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p2]] (p. 39): only anticipated: expected-value criterion lets future decisions be based solely on the present state
- [[bellman-1957-dp/ch01-i-p3]]: the stochastic allocation process, with state $x$, allocation $y$ and random next state (canon link; the term is not used in this unit)
- [[bellman-1957-dp/ch03-iii]] (pp. 85–86): the stochastic formulation with $dG_q(p,z)$ and expected return has this shape; Bellman does not use the term
- [[bellman-1957-dp/ch11-xi]] (pp. 318–319): here: states with transition probabilities $a_{ij}(q)$, $q$ chosen at each stage to maximize the probability of $S_1$ [as `markov decision process`]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 28): finite-state stochastic problem; the author uses the system-equation form, equivalent to transition probabilities
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. 134): notation for finite-state MDPs, $p_{ij}(u)$ vs $p(s'\mid s,a)$ [as `Markov decision process`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 309): the term underlying POMDP (partially observed Markovian decision problem); not discussed on its own in this unit [as `Markov decision process`]
- [[ng-2000-irl/main]] (p. 1): tuple $(S,A,\{P_{sa}\},\gamma,R)$ as defined here
- [[recht-2019-tour/main]] (pp. 10, 22): mentioned here only via partially observed MDPs
- [[sutton-2018-rl/ch01-introduction]] (pp. 2, 13): formal framework of states, actions and rewards for agent–environment interaction; formal definition in Chapter 3
- [[sutton-2018-rl/ch03-finite]] (p. 48): formal problem: states, actions, rewards, with dynamics $p$ depending only on the previous state and action
- [[sutton-2018-rl/ch04-dynamic]] (p. 73): finite MDP with known $p(s',r|s,a)$; the setting of all DP here
- [[sutton-2018-rl/ch10-policy]] (p. 249): continuing MDP with stationary distribution $\mu_\pi$ [as `Markov decision process`]
- [[sutton-2018-rl/ch16-applications]] (pp. 433, 451, 453): formulation used for DRAM scheduling, ad recommendation and soaring

### bayesian

- [[murphy-2023-pml2/ch34-decision]] (p. 1128): $\langle\mathcal S,\mathcal A,p,R,p_0\rangle$ with state changing under actions [new]
- [[murphy-2023-pml2/ch35-reinforcement]] (p. 1145): trajectory model factored into one-step transition and reward models; planning if known, RL if not [new]

### llm

- [[prince-2023-udl/ch19-reinforcement]] (pp. 375, 378): states, actions, transition and reward distributions; Markov means the next state depends on the current state and action only [new]
