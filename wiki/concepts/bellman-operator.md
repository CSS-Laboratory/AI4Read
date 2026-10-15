---
id: bellman-operator
type: concept
fields: [control-theory]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p6]
generated_by: build_kg.py
---

# bellman-operator

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. footnote, p. 59): maps $J$ to the right side of Bellman's equation; Riccati operator is its restriction to quadratics [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p6]] (p. 143): abstract DP operator encoding a model; its monotonicity and contraction determine results [new]

## Candidate bridges

- [same-math] Max-norm contraction of $H$ ↔ standard Bellman-operator contraction in discounted DP — the same argument ($\alpha$-discounting plus averaging by probabilities) — from [[bertsekas-2026-rlcourse/ch03-learning-p5]] (control-theory → unspecified)
- [structural-analogy] Projected Bellman operator iteration ↔ control-theory/state-space: projection to representable subspace then dynamics step, fixed point as equilibrium — from [[sutton-2018-rl/ch11-off]] (control-theory → control-theory)
