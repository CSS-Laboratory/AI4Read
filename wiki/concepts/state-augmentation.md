---
id: state-augmentation
type: concept
fields: [control-theory]
n_sources: 3
tiers: [deep, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch01-exact-p4, sarkka-2023-bayesianfiltering/ch05-modeling, sarkka-2023-bayesianfiltering/ch16-parameter]
generated_by: build_kg.py
---

# state-augmentation

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch01-exact-p4]] (p. 91): enlarging the state to include past states and controls, forecasts and the like, to fit the standard format [new]
- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (p. 85): adding unknown parameters or bias to the state [new]
- [[sarkka-2023-bayesianfiltering/ch16-parameter]] (p. 330): treat θ as a constant extra state; fragile with approximate filters [new]

## Instances that use it

- [[noisy-sinusoidal-disturbance]] — disturbance modeled by a noise-driven oscillator and state augmentation — from [[astrom-2021-feedbacksystems/ch08-output]]

## Candidate bridges

- [structural-analogy] Re-coding to Markov form ↔ control-theory: state augmentation, adding past values to the state so the dynamics become first-order. — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [structural-analogy] State augmentation with $x_{k-1},u_{k-1}$ ↔ state-space modeling: higher-order recursions rewritten as first-order systems. — from [[bertsekas-2026-rlcourse/ch01-exact-p4]] (control-theory → other)
- [structural-analogy] Trading control-space size for state-space size (Fig. 2.9.1) ↔ DP: state augmentation (also used for delays, p. 277). — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (control-theory → other)
- [structural-analogy] State augmentation (θ as constant state) ↔ control-theory: joint state and parameter estimation in adaptive estimation — both turn unknown parameters into states to be estimated online. — from [[sarkka-2023-bayesianfiltering/ch16-parameter]] (control-theory → control-theory)
