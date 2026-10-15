---
id: wordscores
type: concept
fields: [political-science]
fields_strong: [political-science]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch16-word]
generated_by: build_kg.py
---

# wordscores

## Definitions in the sources

### political-science

- [[grimmer-2013-textasdata/main]] (p. 26): supervised scaling via reference-text word scores [new]
- [[grimmer-2022-textasdata/ch16-word]] (p. 290): word scores derived from reference texts at extremes, then used to scale test texts [new]

## Instances that use it

- [[wordscores-senators-example]] — hypothetical illustration: scaling US senators using all speeches of a very liberal and a very conservative senator as reference texts — from [[grimmer-2022-textasdata/ch16-word]]

## Candidate bridges

- [structural-analogy] Validating on fresh data ↔ train/test split in machine learning: Wordscores' "virgin" texts are explicitly called the test set (p. 291). — from [[grimmer-2022-textasdata/ch16-word]] (political-science → llm)
- [structural-analogy] Wordscores' dependence on reference texts ↔ confounding of the measured trait with author style in any measure trained on few exemplars. — from [[grimmer-2022-textasdata/ch16-word]] (political-science → unspecified)
