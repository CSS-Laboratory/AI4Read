---
id: skip-gram-cbow
type: concept
fields: [llm]
n_sources: 2
tiers: [deep]
grounding: digests
sources: [mikolov-2013-compositionality/main, mikolov-2013-efficient/main]
raw_ids: [skip-gram / CBOW]
canon_spine: llm
generated_by: build_kg.py
---

# skip-gram-cbow

## Canon spine entry

- **skip-gram / CBOW** (llm): word2vec objectives: predict context from a word, or a word from its context (UG)

## Definitions in the sources

### llm

- [[mikolov-2013-compositionality/main]] (pp. 2, 8): Skip-gram predicts the surrounding words from the center word; the paper's techniques also apply to CBOW [as `skip-gram / CBOW`]
- [[mikolov-2013-efficient/main]] (pp. 4–5): CBOW: predict middle word from averaged window (4 history + 4 future); Skip-gram: predict surrounding words from the current word; no hidden layer
