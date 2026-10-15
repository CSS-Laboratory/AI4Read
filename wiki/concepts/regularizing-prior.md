---
id: regularizing-prior
type: concept
fields: [bayesian]
n_sources: 3
tiers: [core]
grounding: digests
sources: [mcelreath-2020-rethinking/ch02-small, mcelreath-2020-rethinking/ch06-overfitting-p1, mcelreath-2020-rethinking/ch06-overfitting-p2]
generated_by: build_kg.py
---

# regularizing-prior

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch02-small]] (p. 35): prior that gently nudges inference and tends to guard against inferring strong associations; penalised likelihood is a mathematically equivalent approach [new]
- [[mcelreath-2020-rethinking/ch06-overfitting-p1]] (p. 166): prior telling the model not to get too excited by data; "penalized likelihood" elsewhere [new]
- [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (p. 186): a skeptical prior, usually on slopes, that slows learning from the sample to reduce overfitting; too strong causes underfitting [new]

## Candidate bridges

- [structural-analogy] Mixture-of-Gaussians resolution as an ill-posed inverse problem ↔ Bayesian: hierarchical models and regularizing priors — prior information selects among many consistent decompositions. — from [[jaynes-2003-probability/ch07-central-p2]] (information-theory → bayesian)
