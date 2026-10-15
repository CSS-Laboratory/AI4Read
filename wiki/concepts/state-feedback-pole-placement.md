---
id: state-feedback-pole-placement
type: concept
fields: [control-theory]
n_sources: 4
tiers: [core, deep]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch14-fundamental, liberzon-2012-calculus/ch06-linear]
raw_ids: [state feedback / pole placement]
canon_spine: control-theory
generated_by: build_kg.py
---

# state-feedback-pole-placement

## Canon spine entry

- **state feedback / pole placement** (control-theory): u = −Kx chosen to put the closed-loop eigenvalues where you want them (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch07-state]] (pp. 7-10, 7-11, 7-15): law $u=-Kx+k_fr$ chosen to give the closed loop a desired characteristic polynomial
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-12): here applied to $\hat x$: $u=-K\hat x+k_fr$ [as `state feedback / pole placement`]
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-20, 14-25): choosing closed-loop poles; this unit adds rules for choosing them robustly [as `state feedback / pole placement`]
- [[liberzon-2012-calculus/ch06-linear]] (p. 147): here the linear feedback $u=-R^{-1}B^TPx$ is derived from the necessary conditions, with $P$ given by (6.10) or the RDE (6.14)

## Candidate bridges

- [same-math] Observer design by eigenvalue assignment ↔ state feedback pole placement (ch. 7): the same problem with $A,B,K$ replaced by $A^T,C^T,L^T$ (p. 8-7). — from [[astrom-2021-feedbacksystems/ch08-output]] (control-theory → control-theory)
