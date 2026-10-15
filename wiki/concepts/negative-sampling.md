---
id: negative-sampling
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 1
n_works: 1
tiers: [deep]
grounding: digests
sources: [mikolov-2013-compositionality/main]
raw_ids: [negative sampling]
canon_spine: [llm]
generated_by: build_kg.py
---

# negative-sampling

## Canon spine entry

- **negative sampling** (llm): train by telling true context pairs apart from random noise pairs, instead of a full softmax (grad)

## Definitions in the sources

### llm

- [[mikolov-2013-compositionality/main]] (pp. 3–4): eq. 4: logistic regression separating true context from $k$ noise words; uses samples only [as `negative sampling`]

## Candidate bridges

- [structural-analogy] Negative sampling ↔ llm/contrastive training: separate a true pair from random pairs by a logistic-style loss. — from [[mikolov-2013-compositionality/main]] (llm → llm)
