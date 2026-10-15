---
id: disturbance-and-noise
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 20
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch05-stability, ashby-1956-cybernetics/ch10-regulation, ashby-1956-cybernetics/ch11-requisite, ashby-1956-cybernetics/ch12-error, ashby-1956-cybernetics/ch13-regulating, ashby-1956-cybernetics/ch14-amplifying, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch04-examples, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch12-frequency, maxwell-1868-governors/main, sarkka-2023-bayesianfiltering/ch01-are, sarkka-2023-bayesianfiltering/ch01-symbols, sarkka-2023-bayesianfiltering/ch04-discretization, sarkka-2023-bayesianfiltering/ch05-modeling, sarkka-2023-bayesianfiltering/ch07-extended, welch-2004-kalmanintro/main]
raw_ids: [disturbance and noise]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# disturbance-and-noise

## Canon spine entry

- **disturbance and noise** (control-theory): unwanted inputs to the plant, and errors in the measurements (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch05-stability]] (p. 77): a transformation $D$ that moves the system from one state to another
- [[ashby-1956-cybernetics/ch10-regulation]] (p. 198): D, the source of disturbances and dangers from the outside world [as `disturbance and noise`]
- [[ashby-1956-cybernetics/ch11-requisite]] (pp. 209, 216): D, "that which disturbs"; noise in T can be absorbed into D [as `disturbance and noise`]
- [[ashby-1956-cybernetics/ch12-error]] (p. 219): D, which threatens to drive E out of η [as `disturbance and noise`]
- [[ashby-1956-cybernetics/ch13-regulating]] (p. 246): here: D, the source of disturbances, against T, the system yielding the outcome. In very large systems the boundary between them may be drawn in several equally good ways [as `disturbance and noise`]
- [[ashby-1956-cybernetics/ch14-amplifying]] (p. 269): here: the Grand Disturbance (S.13/8), whose variety in the water-bath example is $2^{36500}$; its definition is in an earlier chapter [as `disturbance and noise`]
- [[astrom-2021-feedbacksystems/ch01-introduction]] (pp. 1-4, 1-6): external perturbations $v$ on the process and noise in sensing and actuation [as `disturbance and noise`]
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-2): load disturbance $v$ entering at the process input
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-6): disturbances modeled as deterministic signals (steps, sinusoids) or, more realistically, as random signals
- [[astrom-2021-feedbacksystems/ch04-examples]] (p. 4-3): road slope as $F_d$
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-26): constant disturbances are rejected by integral action
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-18, 9-19): load disturbance $v$ and measurement noise $w$ as inputs to $e$
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-2): load disturbance $v$ at the process input, measurement noise $w$ at the output
- [[maxwell-1868-governors/main]] (p. 270): variations of driving power $P$ or resistance $R$ [as `disturbance and noise`]
- [[sarkka-2023-bayesianfiltering/ch01-are]] (p. 1): here process noise (uncertainty in the dynamics) and measurement noise [as `disturbance and noise`; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (pp. xxiv, xxvi): process noise $\mathbf q_k$, measurement noise $\mathbf r_k$, white noise $\mathbf w(t)$ [work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch04-discretization]] (p. 46): here, process noise as continuous-time white noise $\mathbf w(t)$ with spectral density $\mathbf Q^c$ [work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (p. 74): measurement noise $\mathbf{r}_k$, Gaussian or heavy-tailed, additive or not [work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch07-extended]] (p. 113, 115): Gaussian process and measurement noise, additive or non-additive [as `disturbance and noise`; work fields: control-theory, bayesian]
- [[welch-2004-kalmanintro/main]] (p. 2): process noise $w\sim N(0,Q)$ and measurement noise $v\sim N(0,R)$
