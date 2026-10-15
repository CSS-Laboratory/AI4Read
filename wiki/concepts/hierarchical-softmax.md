---
id: hierarchical-softmax
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 2
n_works: 2
tiers: [deep]
grounding: digests
sources: [mikolov-2013-compositionality/main, mikolov-2013-efficient/main]
generated_by: build_kg.py
---

# hierarchical-softmax

## Definitions in the sources

### llm

- [[mikolov-2013-compositionality/main]] (p. 3): binary-tree factorization of softmax, about $\log_2 W$ nodes per prediction; Huffman tree here [new]
- [[mikolov-2013-efficient/main]] (p. 3): softmax over a Huffman binary tree; about $\log_2(\text{Unigram perplexity}(V))$ outputs evaluated [new]

## Candidate bridges

- [structural-analogy] Hierarchical softmax over a Huffman tree ↔ information theory: short codes for frequent items reduce average work — from [[mikolov-2013-efficient/main]] (llm → information-theory)
