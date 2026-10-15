---
id: residual-stream
type: concept
fields: [llm]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [geva-2021-ffn/main, kaplan-2020-scaling/main]
canon_spine: llm
generated_by: build_kg.py
---

# residual-stream

## Canon spine entry

- **residual stream** (llm): the running vector sum that every layer reads from and writes to; the "communication bus" of a Transformer (grad)

## Definitions in the sources

### llm

- [[geva-2021-ffn/main]] (p. 5490): the vector $r^\ell$ carried between layers, with $o^\ell=y^\ell+r^\ell$
- [[kaplan-2020-scaling/main]] (p. 6): $d_{\rm model}$ is the dimension of the residual stream

## Candidate bridges

- [structural-analogy] Residual $r^\ell$ read out through $E$ and refined layer by layer ↔ residual stream as shared bus (canon link; not stated in this unit). — from [[geva-2021-ffn/main]] (llm → unspecified)
- [metaphor] memory stream ↔ residual stream: both are running records read from and written to by components. (The first is text and the second a vector.) — from [[park-2023-agents/main]] (llm → other)
- [structural-analogy] additive layer update $\mathbf h+\mathbf f[\mathbf h]$ ↔ llm: the residual stream that every Transformer layer reads from and writes to — the same additive pattern, but the unit never mentions Transformers' internals. — from [[prince-2023-udl/ch11-residual]] (llm → llm)
- [metaphor] Decoder f[z,ϕ] mapping a low-dimensional z to data ↔ llm (residual stream): a compressed internal code that generates outputs. — from [[prince-2023-udl/ch17-variational]] (llm → llm)
