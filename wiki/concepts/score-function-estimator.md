---
id: score-function-estimator
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 1
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch10-variational-p1]
generated_by: build_kg.py
---

# score-function-estimator

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 274): $\mathbb E[\tilde{\mathcal L}\nabla_\theta\log q_\theta]$, via the log-derivative trick; also REINFORCE [new]
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 454): REINFORCE gradient of an expectation, for blackbox VI [new]

## Candidate bridges

- [same-math] likelihood-ratio gradient (3.47) ↔ statistics: score-function estimator, since $E\{\nabla\log p\}=0$ is the same identity. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other:statistics)
- [structural-analogy] Score-function estimator for text GANs ↔ REINFORCE-style gradient estimators for discrete variables, also relevant to GAIL (p. 923). — from [[murphy-2023-pml2/ch26-generative]] (bayesian → unspecified)
