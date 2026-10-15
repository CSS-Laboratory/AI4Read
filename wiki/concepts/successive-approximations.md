---
id: successive-approximations
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 6
n_works: 1
tiers: [core]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch02-ii, bellman-1957-dp/ch04-iv, bellman-1957-dp/ch05-v, bellman-1957-dp/ch10-x, bellman-1957-dp/ch11-xi]
aliases: [successive-approximation]
generated_by: build_kg.py
---

# successive-approximations

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `successive-approximation` — 2 digest(s)

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p1]] (p. 14, 16): iterate $f_{N+1}=\max_yT(f_N,y)$; converges under Theorem 1's conditions [new]
- [[bellman-1957-dp/ch02-ii]] (p. 65): $f_N\to f$ by geometric shrinkage of differences, factor $q=\max|p_i|<1$ [new]
- [[bellman-1957-dp/ch04-iv]] (p. 116): Picard iteration $f_{n+1}=\operatorname{Sup}_q[g+h f_n(T)]$ used to prove existence and uniqueness [new]
- [[bellman-1957-dp/ch05-v]] (pp. 152, 174): define $f_0$ and iterate $f_{n+1}=\min T(\cdot,f_n)$; here used to prove positivity, monotonicity and convexity [new]
- [[bellman-1957-dp/ch10-x]] (pp. 297, 300): $f_{n+1}=\max\min T(f_n)$; converges to the unique solution [alias `successive-approximation`; new]
- [[bellman-1957-dp/ch11-xi]] (pp. 321–323): iterates (5.3) converging by factorial bounds [alias `successive-approximation`; new]

## Candidate bridges

- [same-math] $f_{n+1}(x)=\min_z T(z,x,f_n)$ iterated from $f_0$ ↔ control-theory: value iteration for a discounted MDP with a continuous state — the same successive-approximation scheme. — from [[bellman-1957-dp/ch05-v]] (control-theory → control-theory)
