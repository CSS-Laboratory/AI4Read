---
id: plant
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 5
n_works: 3
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch11-requisite, ashby-1956-cybernetics/ch12-error, astrom-2021-feedbacksystems/ch01-introduction, astrom-2021-feedbacksystems/ch02-feedback, sutton-2018-rl/ch03-finite]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# plant

## Canon spine entry

- **plant** (control-theory): the system being controlled, as distinct from the controller (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch11-requisite]] (p. 209): roughly T, the given table of the external world (Ashby's own term is "Table")
- [[ashby-1956-cybernetics/ch12-error]] (p. 220): T, the given environment plus parts of the organism taken as given
- [[astrom-2021-feedbacksystems/ch01-introduction]] (pp. 1-4, 1-6): here the "process" $P$ or "system" being controlled; in Fig. 1.4 it includes sensors and actuators
- [[astrom-2021-feedbacksystems/ch02-feedback]] (p. 2-2): the "process" $P$ being controlled
- [[sutton-2018-rl/ch03-finite]] (p. 48, fn. 1): engineers' term for what the book calls the environment

## Instances that use it

- [[cruise-control]] — first-order nonlinear plant with PI feedback; hill response — from [[astrom-2021-feedbacksystems/ch04-examples]]
- [[scrapping-half-redundant-plant]] — scrapping part of redundant plant may raise marginal user cost and price immediately — from [[keynes-1936-general/ch06-definition]]
- [[power-plant-oscillation]] — construction delays cause swings between over- and undercapacity — from [[meadows-2008-thinking/ch06-leverage]]
- [[mendel-pea-plants]] — tall/dwarf crosses and the 25% result — from [[mitchell-2009-guidedtour/ch05-evolution]]
- [[plant-stomata-network]] — hypothesized natural decentralized computation, maybe with 2D particles — from [[mitchell-2009-guidedtour/ch11-computing]]
- [[galapagos-darwin]] — islands with the same geology, height and climate differ radically in their plants and animals; Darwin says the nature of the other inhabitants is at least as important, and generally far more important, than physical conditions; used to illustrate that others' behavior shapes one's environment — from [[stiglitz-2002-paradigm/main-p3]]

## Candidate bridges

- [metaphor] Pole/zero cancellation as "designing the controller around the process" ↔ engineering co-design of plant and controller (p. 14-2). — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → unspecified)
- [structural-analogy] Mixture of experts with gating ↔ control-theory: multiple-model adaptive control — switch among controllers when the plant changes — from [[bertsekas-2026-rlcourse/ch03-learning-p5]] (control-theory → control-theory)
- [structural-analogy] Weak or slow balancing loop in the fishery ↔ a controller too slow relative to plant growth: the loop must act before the threshold is crossed (p. 72). — from [[meadows-2008-thinking/ch02-brief]] (control-theory → control-theory)
- [structural-analogy] Pirsig's idea that a factory's rationality, not the factory itself, determines what gets rebuilt ↔ control-theory: a plant's behavior is set by its control law, not by which physical components implement it; swapping components without changing the rule leaves the steady behavior unchanged. — from [[meadows-2008-thinking/ch02-note]] (control-theory → control-theory)
- [structural-analogy] Shifting the burden ↔ control theory: a controller that masks an error lets the plant's own regulation weaken, raising the required control effort. — from [[meadows-2008-thinking/ch05-system]] (control-theory → control-theory)
- [structural-analogy] $\mathbf F$, $\mathbf L$, spectral density $\mathbf Q^{\rm c}$ ↔ control-theory: continuous-time state-space matrices with white-noise disturbance — same symbols as a linear plant model driven by noise. — from [[sarkka-2023-bayesianfiltering/ch01-symbols]] (control-theory → control-theory)
- [structural-analogy] Same test problem under many estimators ↔ control-theory: one plant tested with several observers. — from [[sarkka-2023-bayesianfiltering/ch20-list]] (control-theory → control-theory)
- [structural-analogy] agent / environment / action ↔ control theory: controller / controlled system (plant) / control signal — the book says it uses the first names in place of the second (p. 48). — from [[sutton-2018-rl/ch03-finite]] (control-theory → control-theory)
- [structural-analogy] ε-greedy exploration ↔ control theory: probing or dither signals added to excite a plant for identification — only an analogy, not in the text — from [[sutton-2018-rl/ch05-monte]] (control-theory → control-theory)
- [structural-analogy] Policymakers as the plant, the public as the sensor and comparator ↔ closed-loop control — the author notes policymakers may not follow the signal (p. 998). — from [[wlezien-1995-thermostat/main]] (control-theory → unspecified)
