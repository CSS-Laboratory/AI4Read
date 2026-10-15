---
id: q-factor
type: concept
fields: [control-theory]
n_sources: 6
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p1, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch02-approximation-p1, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p5, bertsekas-2026-rlcourse/ch03-learning-p2]
generated_by: build_kg.py
---

# q-factor

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p1]] (p. 22): $g_k(x_k,u_k)+J^*_{k+1}(f_k(x_k,u_k))$; also "action value" or "Q-value" [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 33): expression minimized in the DP equation; $J=\min_uQ$ [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 174): $\tilde Q_k(x_k,u_k)=g_k+\tilde J_{k+1}(f_k)$; its minimization gives the one-step lookahead control [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 257): expected stage cost plus base-policy cost-to-go for a state–control pair [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (pp. 269, 272): cost of applying a control now and then following a given policy; here estimated by sampling [new]
- [[bertsekas-2026-rlcourse/ch03-learning-p2]] (p. 382): expected stage cost plus optimal (or base-policy) cost-to-go after a given first control [new]

## Candidate bridges

- [same-math] Gram–Schmidt (6.32) ↔ linear-algebra: QR factorization — orthonormalising the columns of an independent list gives the $Q$ factor (the text itself does not state QR). — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Belief-averaged Q-factors, with a fixed policy for each fixed $\theta^i$ ↔ certainty equivalence / indirect adaptive control — the unknown parameter is treated as known and the results are averaged (p. 312–314). — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → unspecified)
