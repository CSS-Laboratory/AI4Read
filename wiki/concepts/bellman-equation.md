---
id: bellman-equation
type: concept
fields: [control-theory, bayesian]
n_sources: 5
tiers: [reference, core, deep]
grounding: digests
sources: [bellman-1957-dp/ch10-x, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch02-approximation-p7, murphy-2023-pml2/ch34-decision, ng-2000-irl/main]
generated_by: build_kg.py
---

# bellman-equation

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch10-x]] (p. 296): here the functional equation $f=\max_G\min_{G'}\iint[R+h\,f(T,T')]$
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 90): here: for the infinite-horizon form of a finite-horizon problem it coincides with the finite-horizon DP algorithm
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (p. 327): here, the minimax Bellman operator $T$, neither convex nor concave in $J$
- [[ng-2000-irl/main]] (p. 2): Theorems 1–2: value equations (1)–(2) and the optimality test (3)

### bayesian

- [[murphy-2023-pml2/ch34-decision]] (p. 1132): recursive characterisation of $V_*$, $Q_*$ [new]

## Candidate bridges

- [same-math] $f_N(x)=\max_y[\dots+f_{N-1}(\dots)]$ ↔ control-theory: Bellman equation for a finite-horizon value function — the recursion has the same form. — from [[bellman-1957-dp/ch01-i-p1]] (control-theory → control-theory)
- [structural-analogy] Expected-value recursion of §25 ↔ MDP: finite-horizon Bellman equation with two random outcomes. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → other)
- [same-math] Theorem 1's contraction argument, $u_{N+1}\le q\,u_N$ ↔ control-theory: value iteration for discounted Bellman equations — the survival probability $p_i<1$ plays the role of a discount factor. — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [structural-analogy] stochastic recurrence (5.2) ↔ MDP Bellman equation: expected next-stage value under a transition kernel $dG_q$ (p. 85) — from [[bellman-1957-dp/ch03-iii]] (control-theory → other)
- [structural-analogy] Equation (2.3) as the limit of a Bellman recursion ↔ control-theory: Hamilton–Jacobi–Bellman equation — Bellman himself compares his intermediate approach to the heat equation versus Chapman–Kolmogorov (p. 224). — from [[bellman-1957-dp/ch08-viii]] (control-theory → control-theory)
- [same-math] §6 equation $0=\max_v[F+Gf_c-f_T]$ ↔ control-theory: Hamilton–Jacobi–Bellman equation for finite-horizon optimal control — same PDE (canon link; name not used in this unit) — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] Max-Min functional equation ↔ control-theory: Bellman equation of a one-person problem — replacing $\max$ by $\max\min$ keeps the "payoff plus value of next state" form. — from [[bellman-1957-dp/ch10-x]] (control-theory → control-theory)
- [same-math] Principle of optimality / $J_k^*$ recursion ↔ control-theory Bellman equation / value function: this unit gives the finite-horizon deterministic case — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → control-theory)
- [structural-analogy] One lookahead step as a Newton step on Bellman's equation ↔ numerical analysis: Newton's method for fixed-point equations (announced p. 55; details not in this unit). — from [[bertsekas-2026-rlcourse/ch01-exact-p2]] (control-theory → other)
- [structural-analogy] MPC "apply the first control, then replan" ↔ rollout/approximation in value space: both are one Newton step on the Bellman equation (pp. 119–122). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → other)
- [structural-analogy] Rollout or lookahead with $\tilde J$ as one Newton step ↔ Newton's method for fixed-point equations — the page states the Newton-step view for Bellman's equation. — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (control-theory → unspecified)
- [structural-analogy] rollout or one-step lookahead as a Newton step ↔ optimization: Newton iteration on the Bellman equation (pp. 378, 386) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → other)
- [structural-analogy] value function and HJB ↔ reinforcement learning: Bellman equation — the continuous-time, deterministic analogue of the recursion (5.4) — from [[liberzon-2012-calculus/ch05-hamilton]] (control-theory → control-theory)
- [structural-analogy] Value function ↔ control theory: the optimal return function of the Bellman equation (p. 14); the chapter treats optimal control as work in RL (p. 15) — from [[sutton-2018-rl/ch01-introduction]] (control-theory → control-theory)
- [structural-analogy] Bellman optimality equation (3.19) ↔ control theory: Hamilton–Jacobi–Bellman equation — the text calls the HJB equation the continuous-time, continuous-state counterpart (p. 71). — from [[sutton-2018-rl/ch03-finite]] (control-theory → control-theory)
- [same-math] Bellman equation (3.14) for $v_\pi$ ↔ linear algebra: a linear system of equations in $n$ unknowns — Example 3.5 says $v_\pi$ was computed by solving such a system (p. 60). — from [[sutton-2018-rl/ch03-finite]] (control-theory → linear-algebra)
- [structural-analogy] Q-learning's max backup ↔ Bellman equation / value iteration — a sampled version of the optimality backup. — from [[sutton-2018-rl/ch06-temporal]] (control-theory → unspecified)
