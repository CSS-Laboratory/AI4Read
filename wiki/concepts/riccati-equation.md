---
id: riccati-equation
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, bellman-1957-dp/ch11-xi, bertsekas-2026-rlcourse/ch01-exact-p3, recht-2019-tour/main]
raw_ids: [Riccati equation]
generated_by: build_kg.py
---

# riccati-equation

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-28): differential (7.31) and algebraic (7.33) equations that give $S$ and $K=Q_u^{-1}B^TS$ [new]
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-20): equation (8.30)/(8.31) for the error covariance; dual to the LQR one (p. 8-20) (new) [as `Riccati equation`]
- [[bellman-1957-dp/ch11-xi]] (pp. 325–326): $v'+v^2+pv+q=0$, written as a minimum over linear equations [new]
- [[bertsekas-2026-rlcourse/ch01-exact-p3]] (p. 59): scalar equation $K=F(K)$, $F(K)=\frac{a^2rK}{r+b^2K}+q$; $F$ is the Riccati operator [new]
- [[recht-2019-tour/main]] (p. 12): equation (4.2) whose stabilising solution $M$ gives $K$ [new]

## Candidate bridges

- [same-math] Kalman–Bucy Riccati equation ↔ LQR Riccati equation: equivalences (8.32) map one into the other (p. 8-20). — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → control-theory)
- [structural-analogy] Riccati equation as $\min_w$ of linear equations (§8) ↔ LQR: a Riccati equation arising from minimizing over linear feedback-like choices. — from [[bellman-1957-dp/ch11-xi]] (control-theory → control-theory)
- [same-math] Lookahead from $\tilde K$ ↔ numerical analysis: one Newton iteration on the scalar Riccati equation — shown algebraically in Ex. 1.7. — from [[bertsekas-2026-rlcourse/ch01-exact-p6]] (control-theory → other:numerical-analysis)
- [structural-analogy] Riccati equation (2.64) and its matrix form ↔ control theory: LQR Riccati equation (the author says matrix Riccati equations play a central role in Chapter 6, p. 54) — from [[liberzon-2012-calculus/ch02-calculus]] (control-theory → control-theory)
