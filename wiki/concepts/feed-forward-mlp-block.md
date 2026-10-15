---
id: feed-forward-mlp-block
type: concept
fields: [llm, control-theory]
fields_strong: [llm, control-theory]
n_sources: 6
n_works: 5
tiers: [core, reference, deep]
grounding: digests
sources: [geva-2021-ffn/main, kaplan-2020-scaling/main, prince-2023-udl/ch03-shallow, prince-2023-udl/ch04-deep, sutton-2018-rl/ch09-policy-p2, vaswani-2017-transformer/main]
aliases: [feed-forward-block, feedforward-ann]
raw_ids: [feed-forward (MLP) block]
canon_spine: [llm]
generated_by: build_kg.py
---

# feed-forward-mlp-block

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `feed-forward-block` — 2 digest(s)
- `feedforward-ann` — 1 digest(s)

## Canon spine entry

- **feed-forward (MLP) block** (llm): the per-token two-layer network inside each Transformer layer; arguably a key-value memory (grad)

## Definitions in the sources

### llm

- [[geva-2021-ffn/main]] (p. 5485): per-token two-layer network $f(xK^\top)V$; here read as a key-value memory [alias `feed-forward-block`]
- [[kaplan-2020-scaling/main]] (p. 6): $d_{\rm ff}$ intermediate layer, counted in N [alias `feed-forward-block`]
- [[prince-2023-udl/ch03-shallow]] (p. 35): here the whole MLP: at least one hidden layer; the book's term is feed-forward when connections are acyclic
- [[prince-2023-udl/ch04-deep]] (p. 49): here, the fully connected layer stack of eq. 4.15 [as `feed-forward (MLP) block`]
- [[vaswani-2017-transformer/main]] (p. 5): per-position two-layer ReLU network, $d_{ff}=2048$

### control-theory

- [[sutton-2018-rl/ch09-policy-p2]] (p. 223): loop-free network of weighted units with activation functions [alias `feedforward-ann`; new]

## Candidate bridges

- [structural-analogy] Hidden-layer ReLU network ↔ llm: the per-token feed-forward block of a Transformer — same layer shape (linear, nonlinearity, linear), but the book here covers only the shallow case. — from [[prince-2023-udl/ch03-shallow]] (llm → llm)
- [same-math] $\mathbf h_{k+1}=\mathbf a[\boldsymbol\beta_k+\boldsymbol\Omega_k\mathbf h_k]$ ↔ llm: the per-token feed-forward (MLP) block of a Transformer, which has the same linear-then-activation form (canon link; not stated in this unit). — from [[prince-2023-udl/ch04-deep]] (llm → llm)
- [same-math] 1×1 convolution with activation (same fully connected map at every position) ↔ llm: the per-token feed-forward (MLP) block of a Transformer — both apply one shared network independently at each position. — from [[prince-2023-udl/ch10-convolutional]] (llm → llm)
