---
id: principle-of-optimality
type: concept
fields: [control-theory, decision-game-theory]
fields_strong: [control-theory, decision-game-theory]
n_sources: 18
n_works: 5
tiers: [core, deep, reference]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch01-i-p2, bellman-1957-dp/ch01-i-p3, bellman-1957-dp/ch02-ii, bellman-1957-dp/ch03-iii, bellman-1957-dp/ch04-iv, bellman-1957-dp/ch06-vi, bellman-1957-dp/ch08-viii, bellman-1957-dp/ch09-ix, bellman-1957-dp/ch10-x, bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch02-approximation-p6, liberzon-2012-calculus/ch01-introduction, liberzon-2012-calculus/ch04-maximum-p1, liberzon-2012-calculus/ch05-hamilton, osborne-2004-introduction/ch05-extensive, recht-2019-tour/main]
raw_ids: [principle of optimality]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# principle-of-optimality

## Canon spine entry

- **principle of optimality** (control-theory): the tail of an optimal plan is optimal for the state it starts from (UG)

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p1]] (p. 8): the "key observation": after any first choice the remainder must be used optimally; the name itself is not used in these pages
- [[bellman-1957-dp/ch01-i-p2]] (pp. 24, 31, 32, 39): the same recursion form $f_{N+1}=\max_y[\text{return}+f_N(\text{remaining})]$ is reused in the variants, introduced with "as before" or "arguing as in the preceding pages"; the principle itself is not named in these pages
- [[bellman-1957-dp/ch01-i-p3]]: used implicitly in each recurrence (first decision plus optimal remainder); not stated in this unit (canon link; not stated in this unit) [weak: not really used in this unit]
- [[bellman-1957-dp/ch02-ii]] (p. 63): after any first choice, the continuation over the remaining stages must be optimal
- [[bellman-1957-dp/ch03-iii]] (p. 83): an optimal policy's remaining decisions are optimal for the state produced by the first decision
- [[bellman-1957-dp/ch04-iv]]: is only implicit (the equations come from Ch. III).
- [[bellman-1957-dp/ch06-vi]] (p. 192): the continuation of an optimal policy over $[S,T]$ is optimal from $c(S)$ [as `principle of optimality`]
- [[bellman-1957-dp/ch08-viii]] (p. 231): the continuation of an optimal policy is optimal, used in §11
- [[bellman-1957-dp/ch09-ix]] (p. 247): whatever the first decisions, the remaining path must be optimal for the state reached; applied to extremals as continuous policies
- [[bellman-1957-dp/ch10-x]] (pp. 291–292): extended to games: the one-step Max-Min plus the next-state value yields the value of the $N$-stage game, proved via a one-person comparison
- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (p. 14): the tail of an optimal control sequence is optimal for the tail subproblem
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 30; the principle itself is only named on p. 28): the stochastic DP recursion (1.15) uses tail subproblems to reduce multistage minimization to single-stage minimizations
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 319): used to justify the minimax DP algorithm [as `principle of optimality`]
- [[liberzon-2012-calculus/ch01-introduction]] (p. 3): "dynamic programming" is named as the other development, not explained here
- [[liberzon-2012-calculus/ch04-maximum-p1]] (p. 86): a final portion of an optimal trajectory is optimal for its own starting point
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 128): the tail of an optimal plan is optimal from the state where it starts; here stated as (5.4) [as `principle of optimality`]
- [[recht-2019-tour/main]] (p. 6): the tail of an optimal policy is optimal from its starting state

### decision-game-theory

- [[osborne-2004-introduction/ch05-extensive]] (p. 165): a plan optimal at the start, given the others' strategies, is never wanted to be changed after play begins, as long as the others stick to their strategies; the author names it from dynamic programming [new]

## Candidate bridges

- [structural-analogy] Backpropagation ↔ principle of optimality / dynamic programming: the author says they are closely related. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → control-theory)
- [same-math] Principle of optimality / $J_k^*$ recursion ↔ control-theory Bellman equation / value function: this unit gives the finite-horizon deterministic case — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → control-theory)
- [structural-analogy] Euler–Lagrange equation from small bumps; Lemma 2.1 ↔ principle of optimality: every piece of an optimal path is optimal (p. 31) — from [[liberzon-2012-calculus/ch02-calculus]] (control-theory → control-theory)
- [structural-analogy] Principle of optimality (Fig. 4.2) ↔ dynamic programming: the tail of an optimal plan is optimal. — from [[liberzon-2012-calculus/ch04-maximum-p1]] (control-theory → control-theory)
- [structural-analogy] Principle of Optimality / SPE ↔ dynamic programming: the text states the link (p. 165). A plan optimal now stays optimal after any reached history, as in dynamic programming. — from [[osborne-2004-introduction/ch05-extensive]] (decision-game-theory → control-theory)
- [structural-analogy] Viterbi forward value $V_k$ ↔ control-theory: dynamic-programming value function and the principle of optimality. The backward argmax resembles reading off an optimal policy. — from [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (control-theory → control-theory)
- [structural-analogy] Viterbi algorithm (12.9) ↔ control theory: principle of optimality — both build a best path recursively. — from [[sarkka-2023-bayesianfiltering/ch21-list]] (control-theory → control-theory)
