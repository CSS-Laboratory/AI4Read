---
id: berkeley-admissions
type: instance
fields: [bayesian]
n_sources: 2
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch15-generalized, pearl-2009-causality/main]
canon_instance: [simpsons-paradox-and-berkeley-admissions]
canon_match_rule: confirmed
generated_by: build_kg.py
---

# berkeley-admissions

## Canon entry

- **Simpson's paradox and Berkeley admissions** (bayesian): a treatment or admission pattern reverses when stratified; the causal graph decides which table is right — pearl-2016-primer (§1.2)

## Descriptions in the sources

### bayesian

- [[murphy-2023-pml2/ch15-generalized]] (pp. 618–620): gender-only model suggests bias; department conditioning makes the apparent bias disappear ("it seems", p. 620); hidden confounder caveat [new]
- [[pearl-2009-causality/main]] (p. 426): Simpson's paradox with competitive departments

## Candidate bridges

- [structural-analogy] Berkeley admissions ↔ Simpson's paradox / collider bias: the aggregate rate and the within-department rates disagree, and conditioning on $D$ is valid only if no hidden confounder exists. — from [[murphy-2023-pml2/ch15-generalized]] (bayesian → bayesian)
