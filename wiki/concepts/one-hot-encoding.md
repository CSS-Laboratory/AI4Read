---
id: one-hot-encoding
type: concept
fields: [linear-algebra, political-science, llm]
fields_strong: [linear-algebra, political-science, llm]
n_sources: 5
n_works: 4
tiers: [core, deep]
grounding: digests
sources: [boyd-2018-vmls/ch13-least, deisenroth-2020-mml/ch11-density, grimmer-2022-textasdata/ch06-multinomial, grimmer-2022-textasdata/ch08-distributed, mikolov-2013-regularities/main]
generated_by: build_kg.py
---

# one-hot-encoding

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch13-least]] (p. 270): l−1 Boolean features for an l-valued categorical [new]
- [[deisenroth-2020-mml/ch11-density]] (p. 364): vector with a single 1 and $K-1$ zeros, selecting a component [new]
- [[mikolov-2013-regularities/main]] (p. 747): "1-of-N coding" of the input word [new; work fields: linear-algebra, llm]

### political-science

- [[grimmer-2022-textasdata/ch06-multinomial]] (p. 114): length-$J$ vector with a single 1 marking the word; "dummy variable" [new]
- [[grimmer-2022-textasdata/ch08-distributed]] (pp. 140, 143): length-$J$ vector with a single 1. Distinct words have inner product 0 [new]

## Candidate bridges

- [same-math] one-hot encoding of categoricals ↔ statistics: dummy (indicator) variables in a regression — the same columns of 0/1 indicators. — from [[boyd-2018-vmls/ch13-least]] (linear-algebra → other:statistics)
