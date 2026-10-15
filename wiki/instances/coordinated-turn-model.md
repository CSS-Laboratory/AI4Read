---
id: coordinated-turn-model
type: instance
fields: [control-theory]
n_sources: 7
tiers: [deep]
grounding: digests
sources: [sarkka-2023-bayesianfiltering/ch01-symbols, sarkka-2023-bayesianfiltering/ch04-discretization, sarkka-2023-bayesianfiltering/ch08-general, sarkka-2023-bayesianfiltering/ch10-posterior, sarkka-2023-bayesianfiltering/ch13-extended, sarkka-2023-bayesianfiltering/ch14-general, sarkka-2023-bayesianfiltering/ch20-list]
generated_by: build_kg.py
---

# coordinated-turn-model

## Descriptions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (p. xxviii): abbreviation CT, next to CV and CA
- [[sarkka-2023-bayesianfiltering/ch04-discretization]] (pp. 55–62): polar and Cartesian versions; closed-form mean, intractable covariance
- [[sarkka-2023-bayesianfiltering/ch08-general]] (pp. 142, 149, 160, 165): RMSE 0.30 for CKF, UKF, UKF5 (and GHKF in Ex. 8.14/8.20, but 0.030 in Ex. 8.9); the GHKF result is called practically the same as the EKF
- [[sarkka-2023-bayesianfiltering/ch10-posterior]] (p. 220): IPLF helps only at start-up
- [[sarkka-2023-bayesianfiltering/ch13-extended]] (p. 269, 276): ERTSS 0.016 vs EKF 0.31; IERTSS 0.015 vs ERTSS 0.017 on an inaccurate initial guess
- [[sarkka-2023-bayesianfiltering/ch14-general]] (pp. 290, 304): Tracking with RMSEs 0.016 (non-iterated) and 0.015 (iterated)
- [[sarkka-2023-bayesianfiltering/ch20-list]] (pp. 393–395): second recurring test problem
