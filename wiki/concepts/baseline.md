---
id: baseline
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [bertsekas-2026-rlcourse/ch03-learning-p2, sutton-2018-rl/ch13-policy]
generated_by: build_kg.py
---

# baseline

## Definitions in the sources

### control-theory

- [[bertsekas-2026-rlcourse/ch03-learning-p2]] (p. 396): a subtracted constant or state-dependent term that reduces the range of the target [new]
- [[sutton-2018-rl/ch13-policy]] (p. 329): an $a$-independent $b(s)$ subtracted from the return: same expected update, different variance [new]

## Instances that use it

- [[la-airport-temperature-ar]] — AR(8) RMS 1.01°F vs baselines 3.05, 1.16, 1.73 (p. 259); time-based validation 1.03/0.98 — from [[boyd-2018-vmls/ch13-least]]
- [[dependency-length-37-languages]] — dependency length below random baselines — from [[gibson-2019-efficiency/main]]
- [[minimal-pairs-clustering]] — the four lexicons tested (Dutch, English, French, German) have more minimal pairs than phonotactic baselines — from [[gibson-2019-efficiency/main]]
- [[flan-t0-baseline-tuning]] — baselines tuned by RM score, with Figure 13 — from [[ouyang-2022-instructgpt/main-p2]]
- [[daniel-diet-experiment]] — prospective controlled trial; confounding by baseline health — from [[pearl-2018-bookofwhy/ch04-confounding]]
- [[gsm8k]] — the arithmetic benchmark with the lowest baseline here. PaLM 540B reaches 56.9% with chain of thought, against 17.9% standard — from [[wei-2022-cot/main-p1]]
- [[central-america-baseline-case]] — medium-intensity, low-familiarity benchmark for the typology — from [[zaller-1992-massopinion/ch08-tests]]

## Candidate bridges

- [metaphor] advantage updating, baselines ↔ control theory: removing the operating-point offset to work with deviations — from [[bertsekas-2026-rlcourse/ch03-learning-p2]] (control-theory → control-theory)
- [structural-analogy] $T_{PF}$ versus $T$ and eq. (15) ↔ confounding versus selection bias: the braces term in (15) is the baseline difference between groups. — from [[holland-1986-statistics/main]] (bayesian → bayesian)
- [metaphor] Control group ↔ mechanism design: comparing against a baseline to isolate an effect — only a loose likeness. — from [[kahneman-2011-thinking/ch17-regression]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Experts doing worse than equal-probability guessing ↔ forecast scoring against a naive benchmark: skill is judged relative to a trivial baseline. — from [[kahneman-2011-thinking/ch20-illusion]] (decision-game-theory → other:forecast-scoring-against-a)
- [structural-analogy] Baseline prediction plus adjustment ↔ Bayesian updating: the class base rate is the prior and case information updates it. — from [[kahneman-2011-thinking/ch23-outside]] (decision-game-theory → bayesian)
- [structural-analogy] Reference-dependent perception (loudness, gray patches) ↔ gains/losses relative to a reference point in choice — context sets the baseline for judgment. — from [[kahneman-2011-thinking/ch25-bernoulli]] (decision-game-theory → unspecified)
- [structural-analogy] Control variate/baseline ↔ Monte Carlo variance reduction in estimating expectations (p. 275) — from [[murphy-2023-pml2/ch06-optimization-p1]] (bayesian → unspecified)
- [structural-analogy] Control variate with $c^*$ ↔ regression: $c^*=-\mathrm{Cov}/\mathbb V$ is a regression slope on the baseline. — from [[murphy-2023-pml2/ch11-monte]] (bayesian → other:statistics)
- [structural-analogy] $E$ and $C$ as normalized forms of $P(e,h)-P(e)$ ↔ statistics: likelihood against a baseline. Both compare how well a hypothesis predicts the data with how well the data are predicted anyway. — from [[popper-1959-logic/appix-untitled]] (analytic-philosophy → other:statistics)
- [metaphor] "test the simple EKF first as a baseline" ↔ control practice of testing simple (e.g. PID) control before complex designs — from [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (control-theory → unspecified)
- [structural-analogy] Gradient bandit with baseline ↔ stochastic approximation: noisy-gradient ascent with variance reduction. — from [[sutton-2018-rl/ch02-multi]] (control-theory → other:optimization)
- [metaphor] baseline subtraction ↔ statistics: variance reduction by subtracting something with zero mean effect. — from [[sutton-2018-rl/ch13-policy]] (control-theory → other:statistics)
