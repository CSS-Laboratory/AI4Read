---
id: centering
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [mcelreath-2020-rethinking/ch04-linear-p2, mcelreath-2020-rethinking/ch07-interactions]
generated_by: build_kg.py
---

# centering

## Definitions in the sources

### bayesian

- [[mcelreath-2020-rethinking/ch04-linear-p2]] (pp. 99–100): subtracting the mean of a predictor; makes α the expected outcome at the average predictor and decorrelates α and β here [new]
- [[mcelreath-2020-rethinking/ch07-interactions]] (pp. 225–226, 230): subtracting the mean so zero marks a typical case; gives the intercept and main effects clearer meanings and eases fitting [new]

## Instances that use it

- [[minnesota-radon]] — hierarchical regression over 85 counties; Neal's funnel and non-centering — from [[murphy-2023-pml2/ch15-generalized]]

## Candidate bridges

- [structural-analogy] Centering $z=y-y(j)\mathbf 1$ ↔ choosing a weighted median; the shift changes only the denominator. — from [[spielman-2025-sagt/ch21-cheeger]] (linear-algebra → unspecified)
