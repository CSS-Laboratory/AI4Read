---
id: topic-model-lda
type: concept
fields: [political-science]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch01-introduction]
generated_by: build_kg.py
---

# topic-model-lda

## Definitions in the sources

### political-science

- [[grimmer-2013-textasdata/main]] (p. 18): documents are mixtures of topics, topics are word distributions; mixed-membership structure [new]
- [[grimmer-2022-textasdata/ch01-introduction]] (p. 27): a statistical model that finds topics and each document's proportion in each topic [new]

## Instances that use it

- [[nyt-topic-model]] — LDA on 1.8M New York Times articles via SVI — from [[blei-2017-variational/main-p2]]

## Candidate bridges

- [structural-analogy] Latent document-level concept ↔ topic models (LDA): the paper itself notes this shared latent-variable structure (p. 2), but uses no explicit inference algorithm. — from [[xie-2022-icl/main]] (llm → other)
