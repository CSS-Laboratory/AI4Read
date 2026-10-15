---
id: do-calculus
type: concept
fields: [bayesian]
n_sources: 3
tiers: [core, deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch36-causality-p2, pearl-2009-causality/main, pearl-2018-bookofwhy/ch07-beyond]
generated_by: build_kg.py
---

# do-calculus

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch36-causality-p2]] (p. 1228): three rewrite rules converting do-expressions to observational ones given a graph [new]
- [[pearl-2009-causality/main]] (p. 422): three rules turning expressions with *do* into other expressions, licensed by graph conditions [new]
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 215–218): Three rewrite rules for eliminating do from expressions. Rules 1–3 can be proven from the arrow-deleting definition of do (pdf 216); Pearl proposed them in 1994, and Huang–Valtorta and Shpitser proved them complete [new]

## Instances that use it

- [[wermuth-cox-sequential]] — Time-varying treatment solved with the do-calculus — from [[pearl-2018-bookofwhy/ch07-beyond]]

## Candidate bridges

- [structural-analogy] Do-calculus proof as symbol manipulation ↔ Bayesian inference: both turn one kind of probability into another by licensed rewrites (conditioning, Bayes' theorem) — different rules, same "format change" spirit. — from [[pearl-2018-bookofwhy/ch07-beyond]] (bayesian → bayesian)
