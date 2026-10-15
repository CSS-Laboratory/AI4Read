---
id: scaled-dot-product-attention
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [prince-2023-udl/ch12-transformers, vaswani-2017-transformer/main]
raw_ids: [scaled dot-product attention]
generated_by: build_kg.py
---

# scaled-dot-product-attention

## Definitions in the sources

### llm

- [[prince-2023-udl/ch12-transformers]] (p. 214): dot products divided by $\sqrt{D_q}$ to avoid softmax saturation [as `scaled dot-product attention`; new]
- [[vaswani-2017-transformer/main]] (p. 4): $\mathrm{softmax}(QK^T/\sqrt{d_k})V$ [new]
