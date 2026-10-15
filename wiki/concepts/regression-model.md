---
id: regression-model
type: concept
fields: [linear-algebra]
n_sources: 2
tiers: [core]
grounding: digests
sources: [boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch13-least]
generated_by: build_kg.py
---

# regression-model

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch02-linear]] (p. 38): affine prediction $\hat y=x^T\beta+v$ from a feature vector [new]
- [[boyd-2018-vmls/ch13-least]] (p. 257): ŷ = xᵀβ + v, a special case with A = [**1** Xᵀ] [new]

## Instances that use it

- [[x-x2-regression-model]] — density $x^n/\epsilon$ model; estimates of $x^2$ from $x$ and vice versa sharpen as $n$ grows — from [[jaynes-1957-information/main]]
- [[kempthorne-folks-regression]] — 16 regression models for one inference problem — from [[jaynes-2003-probability/ch17-principles-p2]]

## Candidate bridges

- [structural-analogy] Interaction on additive scale ↔ regression models: a product term in a linear model measures departure from additive effects. The source does not state this; it is our proposal. — from [[hernan-2020-whatif/ch05-interaction]] (bayesian → other)
