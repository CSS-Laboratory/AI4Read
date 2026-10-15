---
id: mcar
type: concept
fields: [bayesian]
n_sources: 2
tiers: [core]
grounding: digests
sources: [gelman-2013-bda3/ch18-models, mcelreath-2020-rethinking/ch14-missing]
generated_by: build_kg.py
---

# mcar

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch18-models]] (p. 450): missingness independent of $y$ altogether, $p(I|\phi)$; rarely plausible [new]
- [[mcelreath-2020-rethinking/ch14-missing]] (p. 432): missing completely at random: missingness unrelated to the missing values or to any other values [new]

## Instances that use it

- [[age-income-missingness]] — three missingness cases (MCAR; MAR but not observed at random, ignorable if parameters are distinct; nonignorable) in a bivariate normal — from [[gelman-2013-bda3/ch18-models]]

## Candidate bridges

- [structural-analogy] MCAR ↔ ignorability: both say the mechanism deciding what is seen is unrelated to the unseen values. — from [[mcelreath-2020-rethinking/ch14-missing]] (bayesian → other)
- [structural-analogy] MCAR/MAR/MNAR ↔ causal inference: ignorability of the assignment mechanism — from [[murphy-2023-pml2/ch03-statistics-p3]] (bayesian → bayesian)
