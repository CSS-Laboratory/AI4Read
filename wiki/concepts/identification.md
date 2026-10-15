---
id: identification
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch02-randomized, murphy-2023-pml2/ch36-causality-p1]
generated_by: build_kg.py
---

# identification

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch02-randomized]] (p. 20): a counterfactual quantity expressible via the observed-data distribution [new]
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1191): an estimand is identified if the assumptions leave a unique value compatible with observed data [new]

## Instances that use it

- [[american-voter-party-id]] — party identification is fundamental to vote choice and shapes issue positions — from [[achen-2016-realists/ch08-very]]
- [[spring-mass-system]] — Lyapunov analysis, frequency response, step-response identification, scaling — from [[astrom-2021-feedbacksystems/ch03-system-p2]]
- [[poland-menu-of-parties]] — parties sorting people by degree of identification with the regime — from [[clark-2017-principles/ch10-varieties-p1]]
- [[feynman-layman]] — reference without unique identification — from [[kripke-1980-naming/ch02-lecture]]
- [[uranium-fission-identification]] — late recognition, partly because chemical tests were chosen by expectation — from [[kuhn-1962-structure/ch06-anomaly]]
- [[bonaparte-dna-mh17]] — pedigree network for victim identification — from [[pearl-2018-bookofwhy/ch03-evidence]]
- [[angelo-and-isabella]] — identification lets a threat become profitable — from [[schelling-1960-conflict/ch05-enforcement-p1]]
- [[motorist-bribe-cards]] — contingent identification of an enforcible promise — from [[schelling-1960-conflict/ch05-enforcement-p1]]

## Candidate bridges

- [structural-analogy] Skipping tally ↔ political science: Fiorina's running-tally party identification — both are accumulations of retrospection, but with different weights by year. — from [[achen-2016-realists/ch07-chicken]] (political-science → political-science)
- [structural-analogy] "$n+1$ measurements fix an affine function" ↔ system identification / calibration of a sensor from reference inputs. — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → unspecified)
- [metaphor] Bounds from partial identification ↔ Bayesian credible intervals: both express an honest range, but the bounds carry no probability. — from [[hernan-2020-whatif/ch16-instrumental]] (bayesian → bayesian)
- [same-math] $H^c=-\int p\log(p/m)$ ↔ information-theory: negative KL divergence $-D(p\|m)$ — same functional form; this identification is ours, not stated in the unit. — from [[jaynes-2003-probability/ch12-ignorance]] (bayesian → information-theory)
- [structural-analogy] Self-designated opinion leaders ↔ two-step flow: the identification step that later work relies on (canon link; not stated in this unit). — from [[katz-1955-personalinfluence/ch02-technique]] (communication-theory → communication-theory)
- [structural-analogy] Black box / input–output pairs (Boulding) ↔ control-theory: black-box identification — behavior-level models fail when structure changes, like fitted input–output models. — from [[meadows-2008-thinking/ch04-systems]] (control-theory → control-theory)
- [same-math] Viterbi algorithm ↔ HMM MAP smoothing — the text states this identification (p. 6). — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → unspecified)
- [structural-analogy] EM (E-step: smooth; M-step: re-fit) ↔ control-theory: alternating state estimation and model identification. — from [[sarkka-2023-bayesianfiltering/ch16-parameter]] (control-theory → control-theory)
- [structural-analogy] Identification and contingent identification ↔ signaling and Bayesian types: revealing a private type can be costly or conditional. — from [[schelling-1960-conflict/ch05-enforcement-p1]] (decision-game-theory → decision-game-theory)
- [same-math] Spring energy $\mathcal E(x)$ ↔ Laplacian quadratic form: (11.4) is a sum over edges of $w_{a,b}(x(a)-x(b))^2$ (the identification with $x^TLx$ is not stated in this unit). — from [[spielman-2025-sagt/ch11-walks]] (linear-algebra → other:laplacian-quadratic-form)
- [structural-analogy] Exploration vs exploitation ↔ control theory: identification (estimation) vs control, "dual control" — the text names this correspondence (p. 44). — from [[sutton-2018-rl/ch02-multi]] (control-theory → control-theory)
- [structural-analogy] ε-greedy exploration ↔ control theory: probing or dither signals added to excite a plant for identification — only an analogy, not in the text — from [[sutton-2018-rl/ch05-monte]] (control-theory → control-theory)
- [structural-analogy] Direct vs indirect RL; model-learning = "system identification" (p. 192) ↔ adaptive control: direct vs indirect adaptive control. — from [[sutton-2018-rl/ch08-planning]] (control-theory → control-theory)
- [structural-analogy] Tolman's S–S and SA–S′ expectancies ↔ control engineering: system identification — the text says it is "much like" learning a model from labeled examples. — from [[sutton-2018-rl/ch14-psychology]] (control-theory → control-theory)
