---
id: missing-data-mechanism
type: concept
fields: [bayesian]
fields_strong: [bayesian]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [gelman-2013-bda3/ch18-models, murphy-2023-pml2/ch03-statistics-p3]
aliases: [missing-data-mechanisms]
generated_by: build_kg.py
---

# missing-data-mechanism

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `missing-data-mechanisms` — 1 digest(s)

## Definitions in the sources

### bayesian

- [[gelman-2013-bda3/ch18-models]] (p. 450): the conditional law $p(I|y,\phi)$ of the inclusion indicator given the complete data [new]
- [[murphy-2023-pml2/ch03-statistics-p3]] (p. 141): MCAR, MAR, MNAR, defined via $p(\mathbf R_n|\mathbf X_n)$ [alias `missing-data-mechanisms`; new]

## Candidate bridges

- [structural-analogy] Ignorability (MAR + distinct parameters) ↔ causal inference: ignorable assignment given covariates / unconfoundedness — the text treats assignment as a missing-data mechanism. — from [[gelman-2013-bda3/ch08-modeling]] (bayesian → bayesian)
- [structural-analogy] MAR (assignment depends only on observed $L$) ↔ bayesian: ignorable missing-data mechanism, so inference can ignore the assignment model — the text defines MAR and links it to conditional randomization (p. 18). — from [[hernan-2020-whatif/ch02-randomized]] (bayesian → bayesian)
