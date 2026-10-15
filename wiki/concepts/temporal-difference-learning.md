---
id: temporal-difference-learning
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 15
n_works: 2
tiers: [core]
grounding: digests
sources: [recht-2019-tour/main, sutton-2018-rl/ch01-introduction, sutton-2018-rl/ch06-temporal, sutton-2018-rl/ch07-n, sutton-2018-rl/ch08-planning, sutton-2018-rl/ch09-policy-p1, sutton-2018-rl/ch09-policy-p2, sutton-2018-rl/ch10-policy, sutton-2018-rl/ch11-off, sutton-2018-rl/ch12-eligibility, sutton-2018-rl/ch13-policy, sutton-2018-rl/ch14-psychology, sutton-2018-rl/ch15-neuroscience-p1, sutton-2018-rl/ch15-neuroscience-p2, sutton-2018-rl/ch16-applications]
aliases: [temporal-difference-learning-reward-prediction-error]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# temporal-difference-learning

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `temporal-difference-learning-reward-prediction-error` — 8 digest(s)

## Canon spine entry

- **temporal-difference learning / reward prediction error** (control-theory): learn values from the gap between predicted and received reward plus next-step value (UG)

## Definitions in the sources

### control-theory

- [[recht-2019-tour/main]] (p. 7): value-function methods derived from the value-centred view; named but not derived here [alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch01-introduction]] (p. 10): updates driven by the difference between estimates at successive times
- [[sutton-2018-rl/ch06-temporal]] (p. 120–121): update a value estimate toward $R_{t+1}+\gamma V(S_{t+1})$; the bracket is the TD error $\delta_t$
- [[sutton-2018-rl/ch07-n]] (p. 142): update an earlier estimate toward a later one; here the gap spans n steps
- [[sutton-2018-rl/ch08-planning]] (p. 161): the Q-learning step used for both learning and planning [as `temporal-difference learning / reward prediction error`; alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch09-policy-p1]] (p. 203): here used as the semi-gradient TD(0) update with target $R+\gamma\hat v(S',\mathbf w)$ [as `temporal-difference-learning / reward prediction error`; alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch09-policy-p2]] (p. 236): here, $n$-step semi-gradient TD with function approximation
- [[sutton-2018-rl/ch10-policy]] (p. 250): here the differential TD error (10.11) [as `temporal-difference learning / reward prediction error`; alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch11-off]] (p. 258): bootstrapped value learning from the TD error
- [[sutton-2018-rl/ch12-eligibility]] (p. 293): learning values from the one-step TD error $\delta_t$; traces spread this error over recent states
- [[sutton-2018-rl/ch13-policy]] (p. 331): δ is the quantity $R+\gamma\hat v(S',w)-\hat v(S,w)$ from the pseudocode (p. 332), used by the critic (paired with semi-gradient TD(0)) [as `temporal-difference learning / reward prediction error`; alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch14-psychology]] (pp. 348, 350, 375): here $\delta_t$ acts as a conditioned/primary reinforcement signal and as "surprise" [as `temporal-difference-learning / reward prediction error`; alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch15-neuroscience-p1]] (pp. 380–381): here, the TD error $\delta_{t-1}=R_t+\gamma V(S_t)-V(S_{t-1})$, a special RPE comparing old and new long-term reward expectations [alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch15-neuroscience-p2]] (p. 398): δ is the TD error, here the dopamine-like reinforcement signal sent to both actor and critic [alias `temporal-difference-learning-reward-prediction-error`]
- [[sutton-2018-rl/ch16-applications]] (p. 424): update value estimates toward the next prediction plus reward; used by TD-Gammon, Samuel, Watson, DQN

## Candidate bridges

- [structural-analogy] SARSA update (3.27) ↔ temporal-difference learning: parameter moves along a gradient times the Q prediction error — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [metaphor] On-line Bayesian learning ↔ control-theory: temporal-difference learning — both update beliefs from each new observation. — from [[sarkka-2023-bayesianfiltering/ch03-batch]] (control-theory → control-theory)
