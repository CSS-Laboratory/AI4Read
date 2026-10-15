---
id: value-iteration
type: concept
fields: [control-theory]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, sutton-2018-rl/ch04-dynamic]
generated_by: build_kg.py
---

# value-iteration

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 46): algorithm (1.31), starting from $J_0\equiv0$ or another $J_0$ [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 61): repeatedly minimizing stage cost plus $J_k$; for LQ, $K_{k+1}=F(K_k)$ [new]
- [[sutton-2018-rl/ch04-dynamic]] (p. 83): update (4.10): Bellman optimality as an assignment; evaluation cut to one sweep [new]

## Instances that use it

- [[gamblers-problem]] — value iteration on an episodic MDP; $v$ is the probability of winning; optimal policy not unique — from [[sutton-2018-rl/ch04-dynamic]]

## Candidate bridges

- [structural-analogy] $f_{N+1}(x)=\max_y\int[u+f_N(v)]dG$ ↔ reinforcement learning: finite-horizon value iteration with transition kernel $dG$ — same expected-reward-plus-next-value structure. — from [[bellman-1957-dp/ch01-i-p3]] (control-theory → control-theory)
- [same-math] Theorem 1's contraction argument, $u_{N+1}\le q\,u_N$ ↔ control-theory: value iteration for discounted Bellman equations — the survival probability $p_i<1$ plays the role of a discount factor. — from [[bellman-1957-dp/ch02-ii]] (control-theory → control-theory)
- [structural-analogy] Procedure B, $f_{N+1}=\max_q f_N(T_q\cdot)$ ↔ control theory / RL: value iteration — both iterate the max operator from an initial guess (p. 89) — from [[bellman-1957-dp/ch03-iii]] (control-theory → control-theory)
- [same-math] Type Two equation with constant $h=\beta$ and sup over actions ↔ control-theory: value iteration for a discounted decision process; the argument is a sup-norm contraction by factor $\beta$. — from [[bellman-1957-dp/ch04-iv]] (control-theory → control-theory)
- [same-math] $f_{n+1}(x)=\min_z T(z,x,f_n)$ iterated from $f_0$ ↔ control-theory: value iteration for a discounted MDP with a continuous state — the same successive-approximation scheme. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
- [structural-analogy] shrinking transformation and $\sum w(k^nc)<\infty$ ↔ control-theory: discounting that makes value iteration converge — both make late stages matter less. — from [[bellman-1957-dp/ch10-x]] (control-theory → control-theory)
- [same-math] Value iteration (1.31) ↔ finite-horizon backward DP recursion with time reversed (footnote, p. 46). — from [[bertsekas-2026-rlcourse/ch01-exact-p2]] (control-theory → unspecified)
- [structural-analogy] Recursion (1.95) for the largest invariant set ↔ value iteration: the author says it resembles value iteration (p. 127). — from [[bertsekas-2026-rlcourse/ch01-exact-p5]] (control-theory → other)
- [structural-analogy] Value iteration's Bellman backup ↔ optimal control: backward recursion on the value function, where the max over actions is the optimizing step. — from [[sutton-2018-rl/ch04-dynamic]] (control-theory → control-theory)
- [structural-analogy] Q-learning's max backup ↔ Bellman equation / value iteration — a sampled version of the optimality backup. — from [[sutton-2018-rl/ch06-temporal]] (control-theory → unspecified)
- [same-math] RTDP and other asynchronous updates (4.10) ↔ dynamic programming: Gauss–Seidel / asynchronous value iteration. — from [[sutton-2018-rl/ch08-planning]] (control-theory → control-theory)
