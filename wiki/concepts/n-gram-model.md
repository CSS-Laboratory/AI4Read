---
id: n-gram-model
type: concept
fields: [llm, bayesian]
n_sources: 4
tiers: [deep, reference]
grounding: digests
sources: [bengio-2003-nplm/main, mahowald-2024-dissociating/main, mikolov-2013-efficient/main, murphy-2023-pml2/ch02-probability-p3]
raw_ids: [n-gram model]
canon_spine: llm
generated_by: build_kg.py
---

# n-gram-model

## Canon spine entry

- **n-gram model** (llm): an LM that conditions only on the previous n−1 tokens, estimated by counting (UG)

## Definitions in the sources

### llm

- [[bengio-2003-nplm/main]] (p. 1138): table of next-word probabilities given the last $n-1$ words; back-off and interpolation handle unseen contexts [as `n-gram model`]
- [[mahowald-2024-dissociating/main]] (p. 5, 7): a model storing frequencies of short word strings; cannot track agreement at arbitrary distance
- [[mikolov-2013-efficient/main]] (p. 1): simple model that can be trained on virtually all available data, trillions of words

### bayesian

- [[murphy-2023-pml2/ch02-probability-p3]] (pp. 49, 51): Markov model of order $n-1$ (memory $m=n-1$ in 2.6.2), or order $n$ as named in 2.6.1.3 [new]
