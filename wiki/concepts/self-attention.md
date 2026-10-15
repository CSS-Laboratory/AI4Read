---
id: self-attention
type: concept
fields: [llm]
n_sources: 6
tiers: [reference, core, deep]
grounding: digests
sources: [devlin-2019-bert/main, piantadosi-2022-meaning/main, prince-2023-udl/ch12-transformers, prince-2023-udl/ch13-graph, prince-2023-udl/ch18-diffusion, vaswani-2017-transformer/main]
canon_spine: llm
generated_by: build_kg.py
---

# self-attention

## Canon spine entry

- **self-attention** (llm): attention where queries, keys and values all come from the same sequence (UG)

## Definitions in the sources

### llm

- [[devlin-2019-bert/main]] (p. 4175): used to encode a concatenated text pair, effectively including bidirectional cross attention between the sentences
- [[piantadosi-2022-meaning/main]] (pdf 5): mentioned as the repeated analysis of current and past inputs, which may support implicit planning
- [[prince-2023-udl/ch12-transformers]] (p. 208): attention where queries, keys and values all come from the same inputs; each output is an attention-weighted sum of shared linear values (p. 208) (reuse spine "self-attention")
- [[prince-2023-udl/ch13-graph]] (p. 260): transformer analogue; in graph attention keys, queries and values are identical
- [[prince-2023-udl/ch18-diffusion]] (p. 365): used periodically inside the diffusion U-Net
- [[vaswani-2017-transformer/main]] (pp. 2, 5): queries, keys and values all come from the same sequence

## Candidate bridges

- [structural-analogy] self-attention as content-dependent routing ↔ convolution: both share parameters across positions, but attention weights depend on the inputs — from [[prince-2023-udl/ch12-transformers]] (llm → other)
- [structural-analogy] Graph attention ↔ transformer self-attention: both give softmax-weighted sums of transformed inputs. The graph version masks to the adjacency pattern. — from [[prince-2023-udl/ch13-graph]] (llm → llm)
- [structural-analogy] Masked autoregressive flow ↔ llm: causal masking in self-attention, which prunes dependence on later positions (p. 314) — from [[prince-2023-udl/ch16-normalizing]] (llm → llm)
