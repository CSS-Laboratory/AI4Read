---
id: certainty-equivalence
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 7
n_works: 3
tiers: [reference, core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch15-architecture-p2, bertsekas-2026-rlcourse/ch01-exact-p2, bertsekas-2026-rlcourse/ch01-exact-p3, bertsekas-2026-rlcourse/ch01-exact-p5, bertsekas-2026-rlcourse/ch02-approximation-p4, bertsekas-2026-rlcourse/ch02-approximation-p5, sutton-2018-rl/ch06-temporal]
raw_ids: [certainty equivalence]
generated_by: build_kg.py
---

# certainty-equivalence

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-30): treat estimated parameters as true in design [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p2]] (p. 35): two meanings: the LQ property that the policy ignores noise variance (p. 33); an approximation that replaces random quantities by typical values [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 70): a simplification of later lookahead steps; discussed later in the book [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. 128): replace future uncertain quantities by fixed values, keep current-stage randomness [as `certainty equivalence`; new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p4]] (p. 262): replacing random disturbances by nominal values, here only after the first lookahead stage [new]
- [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (p. 282): fix future disturbances at nominal values and optimize deterministically [new]
- [[sutton-2018-rl/ch06-temporal]] (p. 128): value function exactly correct for the maximum-likelihood model; batch TD(0) converges to it [new]

## Candidate bridges

- [structural-analogy] Certainty equivalence in the LQ example ↔ control-theory: separation of estimation and control under Gaussian noise — in both, noise does not change the control law (not stated in this unit). — from [[bertsekas-2026-rlcourse/ch01-exact-p2]] (control-theory → control-theory)
- [metaphor] Averaging out uncontrollable components ↔ certainty-equivalence or expected-value reductions. — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → unspecified)
- [structural-analogy] Belief-averaged Q-factors, with a fixed policy for each fixed $\theta^i$ ↔ certainty equivalence / indirect adaptive control — the unknown parameter is treated as known and the results are averaged (p. 312–314). — from [[bertsekas-2026-rlcourse/ch02-approximation-p6]] (control-theory → unspecified)
- [structural-analogy] Nominal-opponent reduction ↔ certainty equivalence: fix a point guess of the uncertain element, solve the resulting deterministic problem (pp. 323, 328). — from [[bertsekas-2026-rlcourse/ch02-approximation-p7]] (control-theory → control-theory)
- [metaphor] Certainty equivalence in batch TD ↔ adaptive control: certainty-equivalence design — the text says the term comes from there (p. 139). — from [[sutton-2018-rl/ch06-temporal]] (control-theory → control-theory)
