---
id: causal-masking
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 4
n_works: 3
tiers: [core, reference]
grounding: digests
sources: [devlin-2019-bert/main, prince-2023-udl/ch12-transformers, prince-2023-udl/ch16-normalizing, vaswani-2017-transformer/main]
raw_ids: [causal masking]
canon_spine: [llm]
generated_by: build_kg.py
---

# causal-masking

## Canon spine entry

- **causal masking** (llm): preventing each position from attending to future tokens, so the model is autoregressive (UG)

## Definitions in the sources

### llm

- [[devlin-2019-bert/main]] (p. 4173): GPT's constrained self-attention, where each token attends only to its left; BERT lacks it [as `causal masking`]
- [[prince-2023-udl/ch12-transformers]] (p. 223): "masked self-attention": dot products to answer and right context set to $-\infty$ before softmax [as `causal masking`]
- [[prince-2023-udl/ch16-normalizing]] (pp. 313–314): masking in masked autoregressive flows is likened to masked self-attention [as `causal masking`]
- [[vaswani-2017-transformer/main]] (p. 5): setting illegal softmax inputs to $-\infty$ so position $i$ sees only earlier outputs

## Candidate bridges

- [structural-analogy] Masked autoregressive flow ↔ llm: causal masking in self-attention, which prunes dependence on later positions (p. 314) — from [[prince-2023-udl/ch16-normalizing]] (llm → llm)
