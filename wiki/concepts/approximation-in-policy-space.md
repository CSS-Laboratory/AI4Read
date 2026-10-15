---
id: approximation-in-policy-space
type: concept
fields: [control-theory]
n_sources: 7
tiers: [core, reference]
grounding: digests
sources: [bellman-1957-dp/ch01-i-p1, bellman-1957-dp/ch01-i-p2, bellman-1957-dp/ch02-ii, bellman-1957-dp/ch09-ix, bellman-1957-dp/ch11-xi, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch03-learning-p3]
generated_by: build_kg.py
---

# approximation-in-policy-space

## Definitions in the sources

### control-theory

- [[bellman-1957-dp/ch01-i-p1]] (pp. 17–18): improve a policy guess iteratively; return functions rise monotonically [new]
- [[bellman-1957-dp/ch01-i-p2]] (p. 29): fit simple returns and use the resulting policy as a guide [new]
- [[bellman-1957-dp/ch02-ii]] (p. 65): start from a fixed policy such as $A^\infty$ to get monotone convergence when $p_i\ge0$
- [[bellman-1957-dp/ch09-ix]] (pp. 271–272): iterate on the policy $v$ instead of on $f$; gives monotone $f_n$ [new]
- [[bellman-1957-dp/ch11-xi]] (pp. 326–328): improve $q_n$ against $u_{n-1}$; monotone convergence [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 38): choose a policy from a parametric class $\tilde\mu(x,r)$ by off-line training [new]
- [[bertsekas-2026-rlcourse/ch03-learning-p3]] (p. 400): fit a parametric policy family to state-control samples [new]

## Candidate bridges

- [structural-analogy] Approximation in policy space ↔ policy improvement in reinforcement learning: improve a policy by one-step maximisation against its own return function. — from [[bellman-1957-dp/ch01-i-p1]] (control-theory → control-theory)
- [structural-analogy] approximation in policy space (§9) ↔ control-theory canon "policy": improve the policy against the current value, with monotone convergence — resembles policy iteration, but the text does not say so. — from [[bellman-1957-dp/ch11-xi]] (control-theory → control-theory)
