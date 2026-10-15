---
id: region-of-stability
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p6]
generated_by: build_kg.py
---

# region-of-stability

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 69): set of $K\ge0$ with $|a+bL_K|<1$; also Newton's region of convergence [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 162): set of cost approximations whose $\ell$-step lookahead policy is stable; usually grows with $\ell$ [new]

## Candidate bridges

- [structural-analogy] region of stability = region of convergence of Newton's method ↔ dynamical systems: basin of attraction of a fixed point. — from [[bertsekas-2026-rlcourse/ch01-exact-p3]] (control-theory → complex-systems)
- [metaphor] Region of stability ↔ control-theory stability margin: longer lookahead generally enlarges the set of cost estimates that give a stable policy (Ex. 1.9). — from [[bertsekas-2026-rlcourse/ch01-exact-p6]] (control-theory → control-theory)
