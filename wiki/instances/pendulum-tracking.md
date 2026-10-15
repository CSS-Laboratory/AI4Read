---
id: pendulum-tracking
type: instance
fields: [control-theory]
n_sources: 6
tiers: [deep]
grounding: digests
sources: [sarkka-2023-bayesianfiltering/ch07-extended, sarkka-2023-bayesianfiltering/ch08-general, sarkka-2023-bayesianfiltering/ch10-posterior, sarkka-2023-bayesianfiltering/ch13-extended, sarkka-2023-bayesianfiltering/ch14-general, sarkka-2023-bayesianfiltering/ch15-particle]
generated_by: build_kg.py
---

# pendulum-tracking

## Descriptions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 117, 124): EKF/IEKF track pendulum angle from $\sin(x_1)$ measurements; RMSE 0.17
- [[sarkka-2023-bayesianfiltering/ch08-general]] (pp. 141, 149, 160, 165): RMSE: EKF/IEKF 0.17, GHKF 0.10, CKF 0.11, UKF 0.10, UKF5 0.10
- [[sarkka-2023-bayesianfiltering/ch10-posterior]] (pp. 219–220): IPLF RMSE 0.14 vs EKF/IEKF 0.17
- [[sarkka-2023-bayesianfiltering/ch13-extended]] (p. 269, 275): RMSE 0.17 (EKF) → 0.06 (ERTSS) → 0.03 (IERTSS)
- [[sarkka-2023-bayesianfiltering/ch14-general]] (pp. 281, 304): Example 7.6 reused to compare filters and smoothers (RMSE 0.10, 0.06, 0.03, 0.04)
- [[sarkka-2023-bayesianfiltering/ch15-particle]] (p. 311): BS-PS RMSE 0.04, about the same as Gaussian smoothers; no real benefit from particles
