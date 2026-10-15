---
id: n-step-return
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch07-n, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch12-eligibility]
generated_by: build_kg.py
---

# n-step-return

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch07-n]] (p. 143): n discounted real rewards plus $\gamma^n$ times a value estimate at step n [new]
- [[sutton-2018-rl/ch10-policy]] (p. 247): return with $n$ real rewards, then a bootstrapped $\hat q$ term (10.4) [new]
- [[sutton-2018-rl/ch12-eligibility]] (p. 288): sum of n discounted rewards plus a bootstrapped value at step n [new]

## Candidate bridges

- [structural-analogy] n-step return with bootstrapped tail ↔ model predictive control: a finite lookahead horizon plus an estimate of the remaining cost — both truncate the future and replace the tail by a value estimate. — from [[sutton-2018-rl/ch07-n]] (control-theory → control-theory)
