---
id: autoregressive-model
type: concept
fields: [bayesian, control-theory]
n_sources: 2
tiers: [deep, reference]
grounding: digests
sources: [murphy-2023-pml2/ch22-autoregressive, sarkka-2023-bayesianfiltering/ch05-modeling]
generated_by: build_kg.py
---

# autoregressive-model

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch22-autoregressive]] (p. 821): model $p(x_{1:T})=\prod_t p(x_t|x_{1:t-1})$ with a restricted form for each conditional [new]

### control-theory

- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (p. 86): $y_k$ as weighted past values plus noise; weights as state [new]

## Instances that use it

- [[gpt-3-175b]] — the 175B autoregressive model; 96 layers, $d_{\text{model}} = 12288$, trained on 300B tokens — from [[brown-2020-gpt3/main-p1]]

## Candidate bridges

- [same-math] Autoregressive model as one-layer flow with inverse conditional cdfs ↔ sampling: inverse-transform sampling applied conditional by conditional (p. 842). — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other)
- [structural-analogy] Decision transformer (return-conditioned action prediction) ↔ llm: decoder-only autoregressive models with conditioning tokens. — from [[prince-2023-udl/ch19-reinforcement]] (llm → llm)
