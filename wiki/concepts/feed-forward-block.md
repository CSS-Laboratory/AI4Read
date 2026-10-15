---
id: feed-forward-block
type: concept
fields: [llm]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [geva-2021-ffn/main, kaplan-2020-scaling/main]
generated_by: build_kg.py
---

# feed-forward-block

## Definitions in the sources

### llm

- [[geva-2021-ffn/main]] (p. 5485): per-token two-layer network $f(xK^\top)V$; here read as a key-value memory
- [[kaplan-2020-scaling/main]] (p. 6): $d_{\rm ff}$ intermediate layer, counted in N

## Candidate bridges

- [structural-analogy] Hidden-layer ReLU network ↔ llm: the per-token feed-forward block of a Transformer — same layer shape (linear, nonlinearity, linear), but the book here covers only the shallow case. — from [[prince-2023-udl/ch03-shallow]] (llm → llm)
