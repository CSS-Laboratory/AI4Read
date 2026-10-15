---
id: masked-language-modeling
type: concept
fields: [llm]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [devlin-2019-bert/main, prince-2023-udl/ch09-regularization, prince-2023-udl/ch12-transformers]
raw_ids: [masked language modeling]
canon_spine: llm
generated_by: build_kg.py
---

# masked-language-modeling

## Canon spine entry

- **masked language modeling** (llm): predicting randomly hidden tokens from both sides of the context (UG)

## Definitions in the sources

### llm

- [[devlin-2019-bert/main]] (p. 4174): randomly mask 15% of WordPiece tokens and predict them from both sides; only masked positions are predicted [as `masked language modeling`]
- [[prince-2023-udl/ch09-regularization]] (p. 152): here: masking words and predicting them as a generative self-supervised task
- [[prince-2023-udl/ch12-transformers]] (p. 220): BERT pre-training: predict randomly masked tokens from both sides [as `masked language modeling`]

## Candidate bridges

- [structural-analogy] Masked-word prediction (9.3.7) ↔ llm: masked language modeling as pretraining before fine-tuning. — from [[prince-2023-udl/ch09-regularization]] (llm → llm)
