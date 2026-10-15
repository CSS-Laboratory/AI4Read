---
id: temporal-difference-learning-reward-prediction-error
type: concept
fields: [control-theory]
n_sources: 8
tiers: [core]
grounding: digests
sources: [recht-2019-tour/main, sutton-2018-rl/ch08-planning, sutton-2018-rl/ch09-policy-p1, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch13-policy, sutton-2018-rl/ch14-psychology, sutton-2018-rl/ch15-neuroscience-p1, sutton-2018-rl/ch15-neuroscience-p2]
raw_ids: [temporal-difference learning / reward prediction error, temporal-difference-learning / reward prediction error]
canon_spine: control-theory
generated_by: build_kg.py
---

# temporal-difference-learning-reward-prediction-error

## Canon spine entry

- **temporal-difference learning / reward prediction error** (control-theory): learn values from the gap between predicted and received reward plus next-step value (UG)

## Definitions in the sources

### control-theory

- [[recht-2019-tour/main]] (p. 7): value-function methods derived from the value-centred view; named but not derived here
- [[sutton-2018-rl/ch08-planning]] (p. 161): the Q-learning step used for both learning and planning [as `temporal-difference learning / reward prediction error`]
- [[sutton-2018-rl/ch09-policy-p1]] (p. 203): here used as the semi-gradient TD(0) update with target $R+\gamma\hat v(S',\mathbf w)$ [as `temporal-difference-learning / reward prediction error`]
- [[sutton-2018-rl/ch10-policy]] (p. 250): here the differential TD error (10.11) [as `temporal-difference learning / reward prediction error`]
- [[sutton-2018-rl/ch13-policy]] (p. 331): δ is the quantity $R+\gamma\hat v(S',w)-\hat v(S,w)$ from the pseudocode (p. 332), used by the critic (paired with semi-gradient TD(0)) [as `temporal-difference learning / reward prediction error`]
- [[sutton-2018-rl/ch14-psychology]] (pp. 348, 350, 375): here $\delta_t$ acts as a conditioned/primary reinforcement signal and as "surprise" [as `temporal-difference-learning / reward prediction error`]
- [[sutton-2018-rl/ch15-neuroscience-p1]] (pp. 380–381): here, the TD error $\delta_{t-1}=R_t+\gamma V(S_t)-V(S_{t-1})$, a special RPE comparing old and new long-term reward expectations
- [[sutton-2018-rl/ch15-neuroscience-p2]] (p. 398): δ is the TD error, here the dopamine-like reinforcement signal sent to both actor and critic
