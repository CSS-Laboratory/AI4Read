---
id: frequency-response
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 3
n_works: 1
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch03-system-p2, astrom-2021-feedbacksystems/ch06-linear]
generated_by: build_kg.py
---

# frequency-response

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-5): outputs for a step input / for sinusoidal inputs of different frequencies [new]
- [[astrom-2021-feedbacksystems/ch03-system-p2]] (p. 3-22): steady-state gain $g(\omega)$ and phase $\varphi(\omega)$ of the output to a sinusoidal input; amplitude-independent for linear systems [new]
- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-23): $G(i\omega)=C(i\omega I-A)^{-1}B+D$; gain $|G|$ and phase $\arg G$ for sinusoidal input [new]

## Instances that use it

- [[spring-mass-system]] — Lyapunov analysis, frequency response, step-response identification, scaling — from [[astrom-2021-feedbacksystems/ch03-system-p2]]
- [[active-band-pass-filter]] — op amp circuit with a band-pass frequency response — from [[astrom-2021-feedbacksystems/ch06-linear]]
