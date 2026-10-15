---
id: delay
type: concept
fields: [control-theory]
n_sources: 6
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch08-transmission, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch12-frequency, meadows-2008-thinking/ch01-basics, meadows-2008-thinking/ch02-brief]
generated_by: build_kg.py
---

# delay

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch08-transmission]] (p. 156): here a device repeating its input one step later (p. 147–148). Also the slow transfer of variety when part of the sender acts only through intermediate parts (p. 156); compare the canon's "delay (dead time)"
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-9): neglected small time delays are an example of uncertainty that can matter in control
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-11): $y(t)=u(t-\tau)$, $G=e^{-s\tau}$
- [[astrom-2021-feedbacksystems/ch12-frequency]] (p. 12-20): time delays limit feedforward inversion and loop shaping
- [[meadows-2008-thinking/ch01-basics]] (p. 23): here used loosely: slowly changing stocks act as delays, lags and buffers. This is wider than the canon's sense of a lag between an action and its effect
- [[meadows-2008-thinking/ch02-brief]] (pp. 39, 52–54): perception, response, delivery and other delays; the author says a delay in a balancing loop makes oscillation likely

## Instances that use it

- [[time-delay-system]] — non-rational $e^{-s\tau}$ — from [[astrom-2021-feedbacksystems/ch09-transfer-p1]]
- [[atomic-force-microscope]] — fitted high-order transfer function with delay — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]]
- [[pupillary-light-reflex]] — third-order lag plus 0.2 s delay — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]]
- [[dc-motor-with-sensing-delay]] — delay turns a stable proportional loop into an oscillating, then unstable one — from [[astrom-2021-feedbacksystems/ch10-frequency]]
- [[supply-chain-delay]] — rollout with continuous controls, delays and on-line replanning — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[nyse-telephone-1894]] — thirty-second delay used to keep a knowledge advantage — from [[carey-1989-cultural/ch08-technology]]
- [[belgium-2010-formation-delay]] — over 500 days to form a government — from [[clark-2017-principles/ch12-parliamentary-p2]]
- [[czech-2006-formation-delay]] — seven months under a caretaker government — from [[clark-2017-principles/ch12-parliamentary-p2]]
- [[belgium-government-formation-2007-2011]] — eleven parties, an eight-month delay in 2007, and 540 days after 2010 — from [[clark-2017-principles/ch16-consequences-p1]]
- [[mischel-delay-experiment]] — four-year-olds' waiting goes with later control and intelligence scores — from [[kahneman-2011-thinking/ch03-lazy]]
- [[car-dealer-inventory]] — balancing loop with perception, response, delivery delays — from [[meadows-2008-thinking/app-untitled]]
- [[shower-delay]] — long pipe causes hot/cold oscillation — from [[meadows-2008-thinking/ch02-brief]]
- [[commodity-price-cycles]] — gestation/maturation delays give 4-, 7-, 11-year cycles — from [[meadows-2008-thinking/ch04-systems]]
- [[power-plant-oscillation]] — construction delays cause swings between over- and undercapacity — from [[meadows-2008-thinking/ch06-leverage]]
- [[gps-ekf]] — position from satellite signal delays via an EKF — from [[sarkka-2023-bayesianfiltering/ch01-are]]
- [[marshmallow-delay-choice]] — present bias, 2 p.m. tomorrow vs 2:15 p.m. — from [[thaler-2015-misbehaving/ch31-save]]

## Candidate bridges

- [structural-analogy] delayed transfer when part of T acts only through intermediates ↔ control theory: transport delay or lag from chains of components — from [[ashby-1956-cybernetics/ch08-transmission]] (control-theory → control-theory)
- [metaphor] Rush-hour effect in queues ↔ delay (dead time): slow recovery after a short overload resembles slow response, though the mechanism here is saturated service rate. — from [[astrom-2021-feedbacksystems/ch03-system-p2]] (control-theory → other)
- [metaphor] Delay-induced oscillation in a loop ↔ time-lagged feedback in other fields (e.g. congestion in networks): the same "returns in phase with gain ≥1" mechanism. — from [[astrom-2021-feedbacksystems/ch10-frequency]] (control-theory → control-theory)
- [structural-analogy] RHP pole needs high bandwidth, RHP zero needs low bandwidth ↔ balancing a stick: the shorter the stick the faster the reaction needed, and delay limits it (the unit compares the X-29 dynamics to an inverted pendulum and treats the cart–pendulum balance system in Ex. 14.7). — from [[astrom-2021-feedbacksystems/ch14-fundamental]] (control-theory → other)
- [structural-analogy] Trading control-space size for state-space size (Fig. 2.9.1) ↔ DP: state augmentation (also used for delays, p. 277). — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]] (control-theory → other)
- [structural-analogy] delay in a balancing loop causes oscillation ↔ control theory: delay as a cause of overshoot and oscillation. — from [[meadows-2008-thinking/app-untitled]] (control-theory → control-theory)
- [structural-analogy] Delay in a balancing loop leading to oscillation ↔ feedback with dead time: loop gain times delay limits stability; acting faster (higher gain) worsened oscillation (p. 56). — from [[meadows-2008-thinking/ch02-brief]] (control-theory → control-theory)
- [structural-analogy] Delay in feedback loop ↔ control-theory: dead time causing overshoot and oscillation — Meadows says delays always cause overshoot and oscillation; in control theory dead time is a main cause. — from [[meadows-2008-thinking/ch04-systems]] (control-theory → control-theory)
- [metaphor] Foresight under long delays ↔ control-theory: feedforward or predictive control — acting before the problem is obvious. — from [[meadows-2008-thinking/ch04-systems]] (control-theory → control-theory)
- [structural-analogy] Delays cause overshoot and oscillation ↔ control theory: delay in a feedback loop reduces stability margin — the text states the effect only in words. — from [[meadows-2008-thinking/ch06-leverage]] (control-theory → control-theory)
- [structural-analogy] Dartmouth central thermostat (p. 179) ↔ control-theory: delay in a loop causing overshoot and oscillation. — from [[meadows-2008-thinking/ch07-living]] (control-theory → control-theory)
- [structural-analogy] Hold-out and credible threats in small-group bargaining ↔ bargaining model of war: costly delay and credibility of threats. — from [[olson-1965-collectiveaction/app-untitled]] (political-science → other)
- [structural-analogy] Text as a low-dimensional projection of thought ↔ dynamical systems: Packard/Takens delay-embedding reconstruction — both recover hidden structure from a limited view; the paper itself says "analogy". — from [[piantadosi-2022-meaning/main]] (llm → complex-systems)
- [structural-analogy] Prediction step $\mathbf P^-=\mathbf A\mathbf P\mathbf A^T+\mathbf Q$ ↔ control-theory: delay/disturbance makes uncertainty grow between measurements. — from [[sarkka-2023-bayesianfiltering/ch03-batch]] (control-theory → control-theory)
- [structural-analogy] Hidden common cause with delays (Fig. 9.3) ↔ causal inference: confounding — both produce an apparent link that is not a direct effect. — from [[stone-2022-information/ch09-transfer]] (information-theory → bayesian)
- [structural-analogy] backward-view credit assignment (TD error shouted back to prior states) ↔ control-theory: delay (dead time) — spreading a late signal back over earlier causes compensates for lag between action and effect. — from [[sutton-2018-rl/ch12-eligibility]] (control-theory → control-theory)
- [structural-analogy] CSC representation ↔ engineering: tapped delay line — each time since onset has its own feature. — from [[sutton-2018-rl/ch14-psychology]] (control-theory → other)
