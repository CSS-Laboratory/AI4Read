---
id: positional-encoding
type: concept
fields: [llm]
n_sources: 3
tiers: [core, reference]
grounding: digests
sources: [devlin-2019-bert/main, prince-2023-udl/ch12-transformers, vaswani-2017-transformer/main]
raw_ids: [positional encoding]
canon_spine: llm
generated_by: build_kg.py
---

# positional-encoding

## Canon spine entry

- **positional encoding** (llm): injecting word-order information into an otherwise order-blind attention model (grad)

## Definitions in the sources

### llm

- [[devlin-2019-bert/main]] (p. 4174, 4183): here, learned position embeddings summed into the input; longer 512-length training teaches them [as `positional encoding`]
- [[prince-2023-udl/ch12-transformers]] (pp. 213–214): matrix $\boldsymbol\Pi$ (absolute) or per-offset parameters $\pi_{a,b}$ (relative) that add order information to an order-blind mechanism [as `positional encoding`]
- [[vaswani-2017-transformer/main]] (p. 6): sinusoidal vectors added to embeddings to inject order

## Candidate bridges

- [structural-analogy] Weight sharing across positions (translation equivariance) ↔ llm: sharing Transformer layer weights across token positions, with order information supplied separately (positional encoding) — different symmetry, similar economy. — from [[prince-2023-udl/ch10-convolutional]] (llm → llm)
- [structural-analogy] Fully connected net "has no notion of nearby" (p. 161) ↔ llm: attention without positional encoding is order-blind. — from [[prince-2023-udl/ch10-convolutional]] (llm → llm)
- [structural-analogy] Sinusoidal time embedding added to channels ↔ LLM: positional encoding injected into an otherwise position-blind network (figure caption cites a sinusoidal embedding, p. 365). — from [[prince-2023-udl/ch18-diffusion]] (llm → llm)
