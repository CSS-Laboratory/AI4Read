---
id: gain-scheduling
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch13-robust, bertsekas-2026-rlcourse/ch01-exact-p5]
raw_ids: [gain scheduling]
generated_by: build_kg.py
---

# gain-scheduling

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-28): feedback gains $K(x_d)$ varying with the operating point (p. 8-28) (new) [as `gain scheduling`]
- [[astrom-2021-feedbacksystems/ch13-robust]] (p. 13-27): switching controllers by a measured variable correlated with parameters [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p5]] (p. footnote, p. 111): precompute a controller per known parameter value and switch [as `gain scheduling`; new]

## Candidate bridges

- [structural-analogy] Linearize-at-the-estimate loop ↔ gain scheduling/extended observers in nonlinear control: the linearization point is itself estimated. — from [[sarkka-2023-bayesianfiltering/ch10-posterior]] (control-theory → control-theory)
