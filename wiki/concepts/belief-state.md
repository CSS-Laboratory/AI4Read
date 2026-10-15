---
id: belief-state
type: concept
fields: [control-theory]
n_sources: 4
tiers: [reference, core]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch02-approximation-p6, sutton-2018-rl/ch17-frontiers]
raw_ids: [belief state]
generated_by: build_kg.py
---

# belief-state

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (pp. 81, 98): $b_k$, the distribution of $x_k$ given all observations and controls up to $k$; serves as state in an exact DP [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. 117): pair $(x_k,b_k)$ of observed state and posterior over $\theta$ [as `belief state`; new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 303, 310): the posterior over the hidden quantity, alone in BO and paired with $x_k$ in adaptive control [new]
- [[sutton-2018-rl/ch17-frontiers]] (p. 467): POMDP distribution over latent states given history, updated by Bayes' rule (17.9–17.10) [new]

## Instances that use it

- [[bidirectional-parking]] — belief-state DP with time-varying free probabilities — from [[bertsekas-2026-rlcourse/ch01-exact-p4]]
- [[pomdp-belief-state]] — the belief vector as a Markov state — from [[sutton-2018-rl/ch17-frontiers]]

## Candidate bridges

- [structural-analogy] Type Three problem with $p$ a probability vector over states ↔ belief-state formulation of decisions under partial observation: "observe the true state" resets the belief to a vertex. — from [[bellman-1957-dp/ch04-iv]] (control-theory → other)
- [structural-analogy] Belief state $b_k$ with update $F_k$ ↔ control-theory state estimation: Kalman filter output used as the state of a perfect-information problem (the text names Kalman filtering as one choice of $F_k$). — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → control-theory)
- [structural-analogy] Belief state $(x_k,b_k)$ ↔ Kalman filter state estimate: both summarize the information history in a recursively updated quantity (pp. 117, 131). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → other)
- [structural-analogy] notional world as the set of worlds consistent with a description ↔ belief-state models: an agent's belief as a set of possible world-states consistent with its evidence. — from [[dennett-1987-intentional-stance/ch05-beyond-p1]] (theory-of-mind → other)
- [structural-analogy] notional world as the world an agent takes itself to be in ↔ theory-of-mind/POMDP: an agent's belief state about the world — both describe an agent by what it takes the world to be like. — from [[dennett-1987-intentional-stance/ch05-beyond-p2]] (theory-of-mind → theory-of-mind)
- [structural-analogy] Belief-state MDP in bandits ↔ sequential updating: today's posterior is tomorrow's prior, now used as the decision state. — from [[murphy-2023-pml2/ch34-decision]] (bayesian → other)
- [structural-analogy] Bayes-adaptive MDP belief state ↔ bayesian: sequential updating, with the posterior predictive as transition model (p. 1149). — from [[murphy-2023-pml2/ch35-reinforcement]] (bayesian → bayesian)
- [structural-analogy] Child's two models (own knowledge vs protagonist's belief) ↔ POMDP / BToM: agent's belief state kept distinct from the world state — both separate what is true from what the agent represents. — from [[wimmer-1983-beliefs-about-beliefs/main]] (theory-of-mind → other)
