---
id: multistep-lookahead
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch02-approximation-p1]
generated_by: build_kg.py
---

# multistep-lookahead

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 50): $\ell$-step minimization, apply only the first control; may allow a less accurate $\tilde J$ [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 68): $\ell$-step lookahead: $\ell-1$ VI steps improve the Newton starting point $F^{\ell-1}(\tilde K)$ [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p1]] (p. 177): $\ell$-step deterministic DP with terminal approximation $\tilde J_{k+\ell}$ [new]

## Instances that use it

- [[alphazero-td-gammon]] — mentioned as examples of off-line training yielding a cost approximation (TD-Gammon) or both cost and policy (AlphaZero); long multistep lookahead critical for AlphaZero chess — from [[bertsekas-2026-rlcourse/ch01-exact-p2]]
