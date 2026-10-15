---
id: latent-dirichlet-allocation
type: concept
fields: [political-science, bayesian]
fields_strong: [political-science, bayesian]
n_sources: 4
n_works: 3
tiers: [core, deep]
grounding: digests
sources: [blei-2017-variational/main-p2, grimmer-2013-textasdata/main, grimmer-2022-textasdata/ch01-introduction, grimmer-2022-textasdata/ch13-topic]
aliases: [topic-model-lda]
generated_by: build_kg.py
---

# latent-dirichlet-allocation

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `topic-model-lda` — 2 digest(s)

## Definitions in the sources

### political-science

- [[grimmer-2013-textasdata/main]] (p. 18): documents are mixtures of topics, topics are word distributions; mixed-membership structure [alias `topic-model-lda`; new]
- [[grimmer-2022-textasdata/ch01-introduction]] (p. 27): a statistical model that finds topics and each document's proportion in each topic [alias `topic-model-lda`; new]
- [[grimmer-2022-textasdata/ch13-topic]] (p. 237): Bayesian generative topic model: Dirichlet-distributed topic weights $\pi_i$ and topic-word distributions $\mu_k$; each token gets its own topic [new]

### bayesian

- [[blei-2017-variational/main-p2]] (p. 31): topic model with Dirichlet topic proportions and topics over a vocabulary [new]

## Candidate bridges

- [structural-analogy] Latent document-level concept ↔ topic models (LDA): the paper itself notes this shared latent-variable structure (p. 2), but uses no explicit inference algorithm. — from [[xie-2022-icl/main]] (llm → other:topic-models-lda)
