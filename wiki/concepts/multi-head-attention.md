---
id: multi-head-attention
type: concept
fields: [llm]
fields_strong: [llm]
n_sources: 2
n_works: 2
tiers: [core, reference]
grounding: digests
sources: [prince-2023-udl/ch12-transformers, vaswani-2017-transformer/main]
raw_ids: [multi-head attention]
canon_spine: [llm]
generated_by: build_kg.py
---

# multi-head-attention

## Canon spine entry

- **multi-head attention** (llm): several attention operations in parallel subspaces, concatenated (grad)

## Definitions in the sources

### llm

- [[prince-2023-udl/ch12-transformers]] (p. 214): $H$ parallel attention heads with separate parameters, concatenated and mixed by $\boldsymbol\Omega_c$ [as `multi-head attention`]
- [[vaswani-2017-transformer/main]] (p. 4): $h$ parallel attentions on learned projections, concatenated and projected
