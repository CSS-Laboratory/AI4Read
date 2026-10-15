---
id: autoregressive-model
type: concept
fields: [bayesian, control-theory, linear-algebra, llm]
fields_strong: [bayesian, control-theory, linear-algebra, llm]
n_sources: 3
n_works: 3
tiers: [core, deep, reference]
grounding: digests
sources: [boyd-2018-vmls/ch13-least, murphy-2023-pml2/ch22-autoregressive, sarkka-2023-bayesianfiltering/ch05-modeling]
aliases: [auto-regressive-model]
generated_by: build_kg.py
---

# autoregressive-model

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `auto-regressive-model` — 1 digest(s)

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch22-autoregressive]] (p. 821): model $p(x_{1:T})=\prod_t p(x_t|x_{1:t-1})$ with a restricted form for each conditional [new; work fields: bayesian, llm]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (p. 86): $y_k$ as weighted past values plus noise; weights as state [new; work fields: control-theory, bayesian]

### linear-algebra

- [[boyd-2018-vmls/ch13-least]] (p. 259): predict z_{t+1} linearly from the previous M values [alias `auto-regressive-model`; new]

## Instances that use it

- [[gpt-3-175b]] — the 175B autoregressive model; 96 layers, $d_{\text{model}} = 12288$, trained on 300B tokens — from [[brown-2020-gpt3/main-p1]]

## Candidate bridges

- [same-math] Autoregressive model as one-layer flow with inverse conditional cdfs ↔ sampling: inverse-transform sampling applied conditional by conditional (p. 842). — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other:statistics)
- [structural-analogy] Decision transformer (return-conditioned action prediction) ↔ llm: decoder-only autoregressive models with conditioning tokens. — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)
