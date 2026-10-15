---
id: value-function
type: concept
fields: [control-theory, economics-finance]
fields_strong: [control-theory, economics-finance]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [thaler-2015-misbehaving/ch04-value, todorov-2002-ofc/main]
generated_by: build_kg.py
---

# value-function

## Definitions in the sources

### control-theory

- [[todorov-2002-ofc/main]] (p. 4): $v^*(t,x)$, the optimal cost-to-go; it determines $\pi^*$

### economics-finance

- [[thaler-2015-misbehaving/ch04-value]] (pdf 41–42): S-shaped curve over gains and losses from a reference point [new]

## Instances that use it

- [[nondifferentiable-value-function]] — $\dot x=xu$, cost $x(t_1)$, $V$ not $\mathcal C^1$ at 0 — from [[liberzon-2012-calculus/ch05-hamilton]]
- [[pole-balancing-feature-interaction]] — why angle and angular velocity need interaction features in a linear value function — from [[sutton-2018-rl/ch09-policy-p1]]

## Candidate bridges

- [same-math] $f_N(x)=\max_y[\dots+f_{N-1}(\dots)]$ ↔ control-theory: Bellman equation for a finite-horizon value function — the recursion has the same form. — from [[bellman-1957-dp/ch01-i-p1]] (control-theory → control-theory)
- [structural-analogy] Quadratic closed forms of §17 ↔ LQR: value function quadratic in the state — here only on a restricted interval with constraint $0\le y\le x$. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → control-theory)
- [same-math] Principle of optimality / $J_k^*$ recursion ↔ control-theory Bellman equation / value function: this unit gives the finite-horizon deterministic case — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → control-theory)
- [structural-analogy] Aggregation interpolation $\tilde J=\Phi r$ ↔ control-theory: linearization or gridding of a nonlinear value function — both replace a large problem by a small one and map back — from [[bertsekas-2026-rlcourse/ch03-learning-p5]] (control-theory → control-theory)
- [structural-analogy] value function and HJB ↔ reinforcement learning: Bellman equation — the continuous-time, deterministic analogue of the recursion (5.4) — from [[liberzon-2012-calculus/ch05-hamilton]] (control-theory → control-theory)
- [structural-analogy] Viterbi forward value $V_k$ ↔ control-theory: dynamic-programming value function and the principle of optimality. The backward argmax resembles reading off an optimal policy. — from [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (control-theory → control-theory)
- [structural-analogy] Value function ↔ control theory: the optimal return function of the Bellman equation (p. 14); the chapter treats optimal control as work in RL (p. 15) — from [[sutton-2018-rl/ch01-introduction]] (control-theory → control-theory)
- [structural-analogy] greedy action choice from $q_*$ ↔ optimal control: one-step lookahead on a value function — the text frames $q_*$ as caching one-step searches (p. 65). — from [[sutton-2018-rl/ch03-finite]] (control-theory → control-theory)
- [structural-analogy] Value iteration's Bellman backup ↔ optimal control: backward recursion on the value function, where the max over actions is the optimizing step. — from [[sutton-2018-rl/ch04-dynamic]] (control-theory → control-theory)
