---
id: encoder-only-decoder-only
type: concept
fields: [llm]
n_sources: 4
tiers: [core, reference]
grounding: digests
sources: [brown-2020-gpt3/main-p2, devlin-2019-bert/main, kaplan-2020-scaling/main, prince-2023-udl/ch12-transformers]
raw_ids: [encoder-only / decoder-only]
canon_spine: llm
generated_by: build_kg.py
---

# encoder-only-decoder-only

## Canon spine entry

- **encoder-only / decoder-only** (llm): BERT-style bidirectional models versus GPT-style left-to-right generators (UG)

## Definitions in the sources

### llm

- [[brown-2020-gpt3/main-p2]] (p. 33): the authors' contrast of autoregressive with bidirectional architectures and their effect on comparison/re-reading tasks [as `encoder-only / decoder-only`]
- [[devlin-2019-bert/main]] (p. 4173–4174, footnote 4): BERT is a bidirectional Transformer "encoder"; the left-context-only version is called a "decoder" [as `encoder-only / decoder-only`]
- [[kaplan-2020-scaling/main]] (p. 6): models here are mainly decoder-only Transformers
- [[prince-2023-udl/ch12-transformers]] (pp. 218–219): encoder builds representations (BERT); decoder predicts the next token (GPT3) [as `encoder-only / decoder-only`]
