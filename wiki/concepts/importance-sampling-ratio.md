---
id: importance-sampling-ratio
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch07-n, sutton-2018-rl/ch11-off, sutton-2018-rl/ch12-eligibility]
generated_by: build_kg.py
---

# importance-sampling-ratio

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch07-n]] (p. 148): product of $\pi/b$ over the actions taken; reweights off-policy data [new]
- [[sutton-2018-rl/ch11-off]] (pp. 257, 258): $\rho_t=\pi(A_t|S_t)/b(A_t|S_t)$, correcting the update target; raises variance [new]
- [[sutton-2018-rl/ch12-eligibility]] (p. 309): $\rho_t=\pi(A_t|S_t)/b(A_t|S_t)$, entering traces and returns [new]
