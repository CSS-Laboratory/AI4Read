---
id: dynamic-programming
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 3
n_works: 3
tiers: [core, deep, reference]
grounding: digests
sources: [liberzon-2012-calculus/ch05-hamilton, murphy-2023-pml2/ch09-message, sutton-2018-rl/ch01-introduction]
generated_by: build_kg.py
---

# dynamic-programming

## Definitions in the sources

### control-theory

- [[liberzon-2012-calculus/ch05-hamilton]] (p. 127): solving a family of problems backward via the value function [new]
- [[sutton-2018-rl/ch01-introduction]] (pp. 14–15): optimal-control solution methods based on the Bellman equation; almost all conventional methods require complete knowledge of the system [new]

### bayesian

- [[murphy-2023-pml2/ch09-message]] (pp. 401, 434): solve subproblems and combine; here, caching messages for reuse (pp. 401, 434) (new)

## Candidate bridges

- [structural-analogy] Backpropagation ↔ principle of optimality / dynamic programming: the author says they are closely related. — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → control-theory)
- [metaphor] Ex. 78 (order of activities does not matter) ↔ computer science: reordering subproblems in dynamic programming without changing the optimum. — from [[bellman-1957-dp/ch01-i-p3]] (control-theory → other:computer-science)
- [structural-analogy] Principle of optimality (Fig. 4.2) ↔ dynamic programming: the tail of an optimal plan is optimal. — from [[liberzon-2012-calculus/ch04-maximum-p1]] (control-theory → control-theory)
- [structural-analogy] Switching curve Γ as a state-feedback policy ↔ dynamic programming: optimal policy as a function of state. — from [[liberzon-2012-calculus/ch04-maximum-p2]] (control-theory → control-theory)
- [structural-analogy] Principle of Optimality / SPE ↔ dynamic programming: the text states the link (p. 165). A plan optimal now stays optimal after any reached history, as in dynamic programming. — from [[osborne-2004-introduction/ch05-extensive]] (decision-game-theory → control-theory)
- [metaphor] Binary-agenda backward induction ↔ dynamic programming: solving from the last stage backward. — from [[osborne-2004-introduction/ch07-extensive]] (decision-game-theory → control-theory)
- [structural-analogy] one-deviation property ↔ dynamic programming: checking single-step deviations in every state — proposal only; the unit does not mention dynamic programming. — from [[osborne-2004-introduction/ch14-repeated]] (decision-game-theory → control-theory)
- [structural-analogy] Backpropagation's reuse of partial products ↔ dynamic programming: sharing sub-results across overlapping computations. — from [[prince-2023-udl/ch07-gradients]] (llm → control-theory)
- [structural-analogy] Viterbi forward value $V_k$ ↔ control-theory: dynamic-programming value function and the principle of optimality. The backward argmax resembles reading off an optimal policy. — from [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (control-theory → control-theory)
- [structural-analogy] RTS backward recursion ↔ control: the backward pass of dynamic programming/Bellman recursion — both run backward from the final time $T$ using a one-step relation. — from [[sarkka-2023-bayesianfiltering/ch14-general]] (control-theory → control-theory)
- [structural-analogy] Backward induction on a game tree ↔ dynamic programming: choose by working back from the final stage. — from [[shepsle-2010-analyzing/ch06-strategic]] (political-science → control-theory)
- [same-math] RTDP and other asynchronous updates (4.10) ↔ dynamic programming: Gauss–Seidel / asynchronous value iteration. — from [[sutton-2018-rl/ch08-planning]] (control-theory → control-theory)
- [same-math] $v^*$ and $\pi^*=-Z^{-1}B^Tv_x^*$ ↔ control-theory: dynamic programming and the HJB equation — the same optimal-control machinery (pp. 4, 9) — from [[todorov-2002-ofc/main]] (control-theory → control-theory)
