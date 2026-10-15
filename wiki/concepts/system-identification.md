---
id: system-identification
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 3
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p2, recht-2019-tour/main, welch-2004-kalmanintro/main]
generated_by: build_kg.py
---

# system-identification

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p2]] (p. 3-28): subfield on experimental determination of models [new]
- [[recht-2019-tour/main]] (p. 5): the control community's name for estimating dynamical systems; inputs must excite the system [new]
- [[welch-2004-kalmanintro/main]] (p. 6): off-line tuning of $Q$ and $R$, often with another Kalman filter [new]

## Candidate bridges

- [structural-analogy] "$n+1$ measurements fix an affine function" ↔ system identification / calibration of a sensor from reference inputs. — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → unspecified)
- [structural-analogy] Direct vs indirect RL; model-learning = "system identification" (p. 192) ↔ adaptive control: direct vs indirect adaptive control. — from [[sutton-2018-rl/ch08-planning]] (control-theory → control-theory)
- [structural-analogy] Tolman's S–S and SA–S′ expectancies ↔ control engineering: system identification — the text says it is "much like" learning a model from labeled examples. — from [[sutton-2018-rl/ch14-psychology]] (control-theory → control-theory)
