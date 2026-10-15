---
id: bellman-equation-value-function
type: concept
fields: [control-theory]
n_sources: 29
tiers: [core, reference, deep]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch01-i-p2, bellman-1957-dp/ch01-i-p3, bellman-1957-dp/ch02-ii, bellman-1957-dp/ch03-iii, bellman-1957-dp/ch04-iv, bellman-1957-dp/ch05-v, bellman-1957-dp/ch06-vi, bellman-1957-dp/ch08-viii, bellman-1957-dp/ch09-ix, bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch01-exact-p6, bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p6, bertsekas-2026-rlcourse/ch03-learning-p5, liberzon-2012-calculus/ch05-hamilton, liberzon-2012-calculus/ch06-linear, recht-2019-tour/main, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch03-finite, sutton-2018-rl/ch04-dynamic, sutton-2018-rl/ch05-monte, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch11-off, sutton-2018-rl/ch17-frontiers]
raw_ids: [Bellman equation / value function]
canon_spine: control-theory
generated_by: build_kg.py
---

# bellman-equation-value-function

## Canon spine entry

- **Bellman equation / value function** (control-theory): the value of a state equals the best immediate payoff plus the value of where you land (UG)

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p1]] (p. 8): $f_N(x)=\max_y[g(y)+h(x-y)+f_{N-1}(ay+b(x-y))]$, with $f$ the maximal return
- [[bellman-1957-dp/ch01-i-p2]] (pp. 31, 39): $f_{k,N}(x)$ (or $f_N(x)$ in the one-resource process) is the optimal $N$-stage return from quantity $x$
- [[bellman-1957-dp/ch01-i-p3]] (p. 40; the definition of $f_N$ is given earlier in the chapter, not on these pages): $f_N(x)$ is the best achievable return with $N$ stages and quantity $x$
- [[bellman-1957-dp/ch02-ii]] (p. 63): $f(x,y)$ is the optimal expected return, satisfying a one-function max equation
- [[bellman-1957-dp/ch03-iii]] (pp. 84–85): $f_N(p)=\max_q f_{N-1}(T_q(p))$; here the "return function" over states and stage counts
- [[bellman-1957-dp/ch04-iv]] (p. 116): the functional equation $f(p)=\operatorname{Sup}_q[g+h f(T(p,q))]$ whose solution is the optimal return; (1.1)
- [[bellman-1957-dp/ch05-v]] (pp. 155–156): $f_n(x)$ or $f(x)$ = optimal expected (discounted) cost from stock $x$, defined by a min over the order-up-to level $y$
- [[bellman-1957-dp/ch06-vi]] (pp. 188, 192): $f(c,T)$ obeys $f(c,S+T)=\max f(c(S),T)$ and its discrete analogue (2) [as `Bellman equation / value function`]
- [[bellman-1957-dp/ch08-viii]] (p. 223): the functional equation (5.1 of Chapter II) for the optimal expected return $f(x,y)$; its small-$\delta$ limit is (2.3)
- [[bellman-1957-dp/ch09-ix]] (p. 249): $f(c)$ (or $f(c,T)$) = optimal value as a function of state; satisfies (9)/(4) of §3/§6
- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (pp. 18–19): here the deterministic finite-horizon DP equation (1.5); $J_k^*$ is the optimal cost-to-go (called value function in maximization problems)
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (pp. 30, 46–47): $J^*$ solves (1.33); $J_k^*$ is the cost-to-go; $J_\mu$ solves (1.34)
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (pp. 58–59): fixed-point equation for the cost; here restricted to $J=Kx^2$ it becomes $K=F(K)$
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (pp. 119, 122): MPC and rollout are Newton steps for solving it [as `Bellman equation / value function`]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 162): for Ex. 1.9, $J^*(1)=\min\{1,\epsilon+J^*(1)\}$ [as `Bellman equation / value function`]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 167–168): here the deterministic DP recursion (2.3)–(2.4), where $J_k^*$ is the optimal cost-to-go of the tail subproblem
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 259): DP equations (2.70)–(2.71) for the stopping problem
- [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (p. 320): minimax form (2.114) with max over $w$ [as `Bellman equation / value function`]
- [[bertsekas-2026-rlcourse/ch03-learning-p5]] (p. 441): the aggregate problem satisfies (3.84)–(3.88); the unit's $\tilde J$ approximates $J^*$ [as `Bellman equation / value function`]
- [[liberzon-2012-calculus/ch05-hamilton]] (p. 127): $V(t,x)=\inf_u J(t,x,u)$, the optimal cost-to-go; infimum allowed, no existence assumed [as `Bellman equation / value function`]
- [[liberzon-2012-calculus/ch06-linear]] (p. 150): $V=x^TP(t)x$ is the optimal cost-to-go and solves HJB
- [[recht-2019-tour/main]] (pp. 6–7): recursion (3.3) for the Q-function; $V(x)=\max_u\mathcal Q(x,u)$
- [[sutton-2018-rl/ch01-introduction]] (p. 14): value of a state = expected total future reward from it; estimated, not given (p. 6); Bellman equation as the dynamic-programming functional equation
- [[sutton-2018-rl/ch03-finite]] (pp. 58–59): value functions $v_\pi$, $q_\pi$ are expected returns and satisfy recursive relationships, written out in (3.14) for $v_\pi$
- [[sutton-2018-rl/ch04-dynamic]] (pp. 73–74): equations (4.1)–(4.4) relating a state's value to its successors; DP turns them into updates
- [[sutton-2018-rl/ch05-monte]] (p. 102): used in the ε-soft optimality proof via an altered environment [as `Bellman equation / value function`]
- [[sutton-2018-rl/ch10-policy]] (p. 250): differential Bellman equations without $\gamma$ [as `Bellman equation / value function`]
- [[sutton-2018-rl/ch11-off]] (pp. 268–269): $v_\pi=B_\pi v_\pi$; the Bellman operator's only fixed point is $v_\pi$
- [[sutton-2018-rl/ch17-frontiers]] (p. 461–463): used throughout, extended to options and GVFs [as `Bellman equation / value function`]

## Candidate bridges

- [same-math] Principle of optimality / $J_k^*$ recursion ↔ control-theory Bellman equation / value function: this unit gives the finite-horizon deterministic case — from [[bertsekas-2026-rlcourse/ch01-exact-p1]] (control-theory → control-theory)
