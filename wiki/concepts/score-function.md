---
id: score-function
type: concept
fields: [information-theory]
n_sources: 2
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch12-information-p3, polyanskiy-2025-information/ch03-divergence]
raw_ids: [score function]
generated_by: build_kg.py
---

# score-function

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch12-information-p3]] (p. 327): $\partial_\theta\ln f(X;\theta)$; has mean zero [new]
- [[polyanskiy-2025-information/ch03-divergence]] (p. 39): $V=\nabla_\theta\ln p_\theta(X)$, mean zero under regularity [as `score function`; new]

## Candidate bridges

- [same-math] likelihood-ratio gradient (3.47) ↔ statistics: score-function estimator, since $E\{\nabla\log p\}=0$ is the same identity. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other)
- [same-math] Evolution-strategies gradient (6.190) ↔ machine learning: score-function (REINFORCE) estimator, cited as Section 6.3.4. — from [[murphy-2023-pml2/ch06-optimization-p2]] (bayesian → other)
- [structural-analogy] Score-function estimator for text GANs ↔ REINFORCE-style gradient estimators for discrete variables, also relevant to GAIL (p. 923). — from [[murphy-2023-pml2/ch26-generative]] (bayesian → unspecified)
