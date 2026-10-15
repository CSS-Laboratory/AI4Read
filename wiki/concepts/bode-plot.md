---
id: bode-plot
type: concept
fields: [control-theory]
n_sources: 4
tiers: [core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch06-linear, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch10-frequency, astrom-2021-feedbacksystems/ch12-frequency]
raw_ids: [Bode plot]
canon_spine: control-theory
generated_by: build_kg.py
---

# bode-plot

## Canon spine entry

- **Bode plot** (control-theory): gain and phase of a system plotted against frequency (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch06-linear]] (p. 6-23): gain and phase of $G(i\omega)$ plotted against $\omega$
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-29): gain on log/log and phase on log/linear scales against frequency; factor contributions add [as `Bode plot`]
- [[astrom-2021-feedbacksystems/ch10-frequency]] (p. 10-7, 10-16): gain and phase against frequency; used to sketch Nyquist curves and read margins
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-13): gain and phase vs frequency, used to read $S$, $T$, $L$ and compensators

## Instances that use it

- [[smith-predictor-example-15-8]] — $P_0=1/(s+1)$, PI controller, $L=8$, Bode plot of $C_{\rm pred}$ — from [[astrom-2021-feedbacksystems/ch15-architecture-p1]]

## Candidate bridges

- [structural-analogy] Bode plot as filter view of a system ↔ signal processing: low-/band-/high-pass filters — the same frequency-selective picture. — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (control-theory → other)
- [structural-analogy] Fourier cosine features with per-feature step sizes ↔ control-theory: frequency-domain view (Bode plots) — both organize behavior by frequency. — from [[sutton-2018-rl/ch09-policy-p1]] (control-theory → control-theory)
