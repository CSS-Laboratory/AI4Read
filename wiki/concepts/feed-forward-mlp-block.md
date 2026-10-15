---
id: feed-forward-mlp-block
type: concept
fields: [llm]
n_sources: 3
tiers: [reference, core]
grounding: digests
sources: [prince-2023-udl/ch03-shallow, prince-2023-udl/ch04-deep, vaswani-2017-transformer/main]
raw_ids: [feed-forward (MLP) block]
canon_spine: llm
generated_by: build_kg.py
---

# feed-forward-mlp-block

## Canon spine entry

- **feed-forward (MLP) block** (llm): the per-token two-layer network inside each Transformer layer; arguably a key-value memory (grad)

## Definitions in the sources

### llm

- [[prince-2023-udl/ch03-shallow]] (p. 35): here the whole MLP: at least one hidden layer; the book's term is feed-forward when connections are acyclic
- [[prince-2023-udl/ch04-deep]] (p. 49): here, the fully connected layer stack of eq. 4.15 [as `feed-forward (MLP) block`]
- [[vaswani-2017-transformer/main]] (p. 5): per-position two-layer ReLU network, $d_{ff}=2048$

## Candidate bridges

- [same-math] $\mathbf h_{k+1}=\mathbf a[\boldsymbol\beta_k+\boldsymbol\Omega_k\mathbf h_k]$ ↔ llm: the per-token feed-forward (MLP) block of a Transformer, which has the same linear-then-activation form (canon link; not stated in this unit). — from [[prince-2023-udl/ch04-deep]] (llm → llm)
- [same-math] 1×1 convolution with activation (same fully connected map at every position) ↔ llm: the per-token feed-forward (MLP) block of a Transformer — both apply one shared network independently at each position. — from [[prince-2023-udl/ch10-convolutional]] (llm → llm)
