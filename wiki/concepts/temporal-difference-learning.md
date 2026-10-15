---
id: temporal-difference-learning
type: concept
fields: [control-theory]
n_sources: 7
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch06-temporal, sutton-2018-rl/ch07-n, sutton-2018-rl/ch09-policy-p2, sutton-2018-rl/ch11-off, sutton-2018-rl/ch12-eligibility, sutton-2018-rl/ch16-applications]
generated_by: build_kg.py
---

# temporal-difference-learning

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch01-introduction]] (p. 10): updates driven by the difference between estimates at successive times
- [[sutton-2018-rl/ch06-temporal]] (p. 120–121): update a value estimate toward $R_{t+1}+\gamma V(S_{t+1})$; the bracket is the TD error $\delta_t$
- [[sutton-2018-rl/ch07-n]] (p. 142): update an earlier estimate toward a later one; here the gap spans n steps
- [[sutton-2018-rl/ch09-policy-p2]] (p. 236): here, $n$-step semi-gradient TD with function approximation
- [[sutton-2018-rl/ch11-off]] (p. 258): bootstrapped value learning from the TD error
- [[sutton-2018-rl/ch12-eligibility]] (p. 293): learning values from the one-step TD error $\delta_t$; traces spread this error over recent states
- [[sutton-2018-rl/ch16-applications]] (p. 424): update value estimates toward the next prediction plus reward; used by TD-Gammon, Samuel, Watson, DQN

## Candidate bridges

- [structural-analogy] SARSA update (3.27) ↔ temporal-difference learning: parameter moves along a gradient times the Q prediction error — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → other)
- [metaphor] On-line Bayesian learning ↔ control-theory: temporal-difference learning — both update beliefs from each new observation. — from [[sarkka-2023-bayesianfiltering/ch03-batch]] (control-theory → control-theory)
