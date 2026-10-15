---
id: bellman-equation
type: concept
fields: [control-theory, bayesian, decision-game-theory, llm]
fields_strong: [control-theory, bayesian, decision-game-theory, llm]
n_sources: 35
n_works: 8
tiers: [core, reference, deep]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch01-i-p2, bellman-1957-dp/ch01-i-p3, bellman-1957-dp/ch02-ii, bellman-1957-dp/ch03-iii, bellman-1957-dp/ch04-iv, bellman-1957-dp/ch05-v, bellman-1957-dp/ch06-vi, bellman-1957-dp/ch08-viii, bellman-1957-dp/ch09-ix, bellman-1957-dp/ch10-x, bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p4, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p6, bertsekas-2026-rlcourse/ch02-approximation-p7, bertsekas-2026-rlcourse/ch03-learning-p5, liberzon-2012-calculus/ch05-hamilton, liberzon-2012-calculus/ch06-linear, murphy-2023-pml2/ch34-decision, ng-2000-irl/main, prince-2023-udl/ch19-reinforcement, recht-2019-tour/main, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch03-finite, sutton-2018-rl/ch04-dynamic, sutton-2018-rl/ch05-monte, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch11-off, sutton-2018-rl/ch17-frontiers]
aliases: [bellman-equation-value-function, bellman-equations]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# bellman-equation

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `bellman-equation-value-function` — 29 digest(s)
- `bellman-equations` — 1 digest(s)

## Canon spine entry

- **Bellman equation / value function** (control-theory): the value of a state equals the best immediate payoff plus the value of where you land (UG)

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p1]] (p. 8): $f_N(x)=\max_y[g(y)+h(x-y)+f_{N-1}(ay+b(x-y))]$, with $f$ the maximal return [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch01-i-p2]] (pp. 31, 39): $f_{k,N}(x)$ (or $f_N(x)$ in the one-resource process) is the optimal $N$-stage return from quantity $x$ [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch01-i-p3]] (p. 40; the definition of $f_N$ is given earlier in the chapter, not on these pages): $f_N(x)$ is the best achievable return with $N$ stages and quantity $x$ [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch02-ii]] (p. 63): $f(x,y)$ is the optimal expected return, satisfying a one-function max equation [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch03-iii]] (pp. 84–85): $f_N(p)=\max_q f_{N-1}(T_q(p))$; here the "return function" over states and stage counts [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch04-iv]] (p. 116): the functional equation $f(p)=\operatorname{Sup}_q[g+h f(T(p,q))]$ whose solution is the optimal return; (1.1) [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch05-v]] (pp. 155–156): $f_n(x)$ or $f(x)$ = optimal expected (discounted) cost from stock $x$, defined by a min over the order-up-to level $y$ [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch06-vi]] (pp. 188, 192): $f(c,T)$ obeys $f(c,S+T)=\max f(c(S),T)$ and its discrete analogue (2) [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch08-viii]] (p. 223): the functional equation (5.1 of Chapter II) for the optimal expected return $f(x,y)$; its small-$\delta$ limit is (2.3) [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch09-ix]] (p. 249): $f(c)$ (or $f(c,T)$) = optimal value as a function of state; satisfies (9)/(4) of §3/§6 [alias `bellman-equation-value-function`]
- [[bellman-1957-dp/ch10-x]] (p. 296): here the functional equation $f=\max_G\min_{G'}\iint[R+h\,f(T,T')]$
- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (pp. 18–19): here the deterministic finite-horizon DP equation (1.5); $J_k^*$ is the optimal cost-to-go (called value function in maximization problems) [alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (pp. 30, 46–47): $J^*$ solves (1.33); $J_k^*$ is the cost-to-go; $J_\mu$ solves (1.34) [alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (pp. 58–59): fixed-point equation for the cost; here restricted to $J=Kx^2$ it becomes $K=F(K)$ [alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 90): here: for the infinite-horizon form of a finite-horizon problem it coincides with the finite-horizon DP algorithm
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 119, 122): MPC and rollout are Newton steps for solving it [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 162): for Ex. 1.9, $J^*(1)=\min\{1,\epsilon+J^*(1)\}$ [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 167–168): here the deterministic DP recursion (2.3)–(2.4), where $J_k^*$ is the optimal cost-to-go of the tail subproblem [alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 259): DP equations (2.70)–(2.71) for the stopping problem [alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 320): minimax form (2.114) with max over $w$ [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (p. 327): here, the minimax Bellman operator $T$, neither convex nor concave in $J$
- [[bertsekas-2026-rlcourse/ch03-learning-p5]] (p. 441): the aggregate problem satisfies (3.84)–(3.88); the unit's $\tilde J$ approximates $J^*$ [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 127): $V(t,x)=\inf_u J(t,x,u)$, the optimal cost-to-go; infimum allowed, no existence assumed [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[liberzon-2012-calculus/ch06-linear]] (p. 150): $V=x^TP(t)x$ is the optimal cost-to-go and solves HJB [alias `bellman-equation-value-function`]
- [[ng-2000-irl/main]] (p. 2): Theorems 1–2: value equations (1)–(2) and the optimality test (3)
- [[recht-2019-tour/main]] (pp. 6–7): recursion (3.3) for the Q-function; $V(x)=\max_u\mathcal Q(x,u)$ [alias `bellman-equation-value-function`]
- [[sutton-2018-rl/ch01-introduction]] (p. 14): value of a state = expected total future reward from it; estimated, not given (p. 6); Bellman equation as the dynamic-programming functional equation [alias `bellman-equation-value-function`]
- [[sutton-2018-rl/ch03-finite]] (pp. 58–59): value functions $v_\pi$, $q_\pi$ are expected returns and satisfy recursive relationships, written out in (3.14) for $v_\pi$ [alias `bellman-equation-value-function`]
- [[sutton-2018-rl/ch04-dynamic]] (pp. 73–74): equations (4.1)–(4.4) relating a state's value to its successors; DP turns them into updates [alias `bellman-equation-value-function`]
- [[sutton-2018-rl/ch05-monte]] (p. 102): used in the ε-soft optimality proof via an altered environment [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[sutton-2018-rl/ch10-policy]] (p. 250): differential Bellman equations without $\gamma$ [as `Bellman equation / value function`; alias `bellman-equation-value-function`]
- [[sutton-2018-rl/ch11-off]] (pp. 268–269): $v_\pi=B_\pi v_\pi$; the Bellman operator's only fixed point is $v_\pi$ [alias `bellman-equation-value-function`]
- [[sutton-2018-rl/ch17-frontiers]] (p. 461–463): used throughout, extended to options and GVFs [as `Bellman equation / value function`; alias `bellman-equation-value-function`]

### bayesian

- [[murphy-2023-pml2/ch34-decision]] (p. 1132): recursive characterisation of $V_*$, $Q_*$ [new; work fields: bayesian, decision-game-theory]

### llm

- [[prince-2023-udl/ch19-reinforcement]] (pp. 380–382): self-consistency relations linking values at $t$ and $t+1$ [alias `bellman-equations`; new]

## Candidate bridges

- [same-math] $f_N(x)=\max_y[\dots+f_{N-1}(\dots)]$ ↔ control-theory: Bellman equation for a finite-horizon value function — the recursion has the same form. — from [[bellman-1957-dp/ch01-i-p1]] (control-theory → control-theory)
- [structural-analogy] Expected-value recursion of §25 ↔ MDP: finite-horizon Bellman equation with two random outcomes. — from [[bellman-1957-dp/ch01-i-p2]] (control-theory → control-theory)
- [same-math] Theorem 1's contraction argument, $u_{N+1}\le q\,u_N$ ↔ control-theory: value iteration for discounted Bellman equations — the survival probability $p_i<1$ plays the role of a discount factor. — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [structural-analogy] stochastic recurrence (5.2) ↔ MDP Bellman equation: expected next-stage value under a transition kernel $dG_q$ (p. 85) — from [[bellman-1957-dp/ch03-iii]] (control-theory → control-theory)
- [structural-analogy] Equation (2.3) as the limit of a Bellman recursion ↔ control-theory: Hamilton–Jacobi–Bellman equation — Bellman himself compares his intermediate approach to the heat equation versus Chapman–Kolmogorov (p. 224). — from [[bellman-1957-dp/ch08-viii]] (control-theory → control-theory)
- [same-math] §6 equation $0=\max_v[F+Gf_c-f_T]$ ↔ control-theory: Hamilton–Jacobi–Bellman equation for finite-horizon optimal control — same PDE (canon link; name not used in this unit) — from [[bellman-1957-dp/ch09-ix]] (control-theory → control-theory)
- [structural-analogy] Max-Min functional equation ↔ control-theory: Bellman equation of a one-person problem — replacing $\max$ by $\max\min$ keeps the "payoff plus value of next state" form. — from [[bellman-1957-dp/ch10-x]] (control-theory → control-theory)
- [same-math] Principle of optimality / $J_k^*$ recursion ↔ control-theory Bellman equation / value function: this unit gives the finite-horizon deterministic case — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → control-theory)
- [structural-analogy] One lookahead step as a Newton step on Bellman's equation ↔ numerical analysis: Newton's method for fixed-point equations (announced p. 55; details not in this unit). — from [[bertsekas-2026-rlcourse/ch01-exact-p2]] (control-theory → other:numerical-analysis)
- [structural-analogy] MPC "apply the first control, then replan" ↔ rollout/approximation in value space: both are one Newton step on the Bellman equation (pp. 119–122). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → other:rollout-approximation-in-value)
- [structural-analogy] Rollout or lookahead with $\tilde J$ as one Newton step ↔ Newton's method for fixed-point equations — the page states the Newton-step view for Bellman's equation. — from [[bertsekas-2026-rlcourse/ch02-approximation-p3]] (control-theory → unspecified)
- [structural-analogy] rollout or one-step lookahead as a Newton step ↔ optimization: Newton iteration on the Bellman equation (pp. 378, 386) — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → other:optimization)
- [structural-analogy] value function and HJB ↔ reinforcement learning: Bellman equation — the continuous-time, deterministic analogue of the recursion (5.4) — from [[liberzon-2012-calculus/ch05-hamilton]] (control-theory → control-theory)
- [structural-analogy] Value function ↔ control theory: the optimal return function of the Bellman equation (p. 14); the chapter treats optimal control as work in RL (p. 15) — from [[sutton-2018-rl/ch01-introduction]] (control-theory → control-theory)
- [structural-analogy] Bellman optimality equation (3.19) ↔ control theory: Hamilton–Jacobi–Bellman equation — the text calls the HJB equation the continuous-time, continuous-state counterpart (p. 71). — from [[sutton-2018-rl/ch03-finite]] (control-theory → control-theory)
- [same-math] Bellman equation (3.14) for $v_\pi$ ↔ linear algebra: a linear system of equations in $n$ unknowns — Example 3.5 says $v_\pi$ was computed by solving such a system (p. 60). — from [[sutton-2018-rl/ch03-finite]] (control-theory → linear-algebra)
- [structural-analogy] Q-learning's max backup ↔ Bellman equation / value iteration — a sampled version of the optimality backup. — from [[sutton-2018-rl/ch06-temporal]] (control-theory → unspecified)
