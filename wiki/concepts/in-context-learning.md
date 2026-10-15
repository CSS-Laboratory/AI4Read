---
id: in-context-learning
type: concept
fields: [llm, bayesian]
fields_strong: [llm, bayesian]
n_sources: 5
n_works: 4
tiers: [core, reference]
grounding: digests
sources: [brown-2020-gpt3/main-p1, brown-2020-gpt3/main-p2, murphy-2023-pml2/ch22-autoregressive, wei-2022-cot/main-p1, xie-2022-icl/main]
raw_ids: [in-context learning]
canon_spine: [llm]
generated_by: build_kg.py
---

# in-context-learning

## Canon spine entry

- **in-context learning** (llm): task learning from the prompt alone, with no weight updates (UG)

## Definitions in the sources

### llm

- [[brown-2020-gpt3/main-p1]] (p. 3–4): inner loop of meta-learning: the task is conditioned on in the forward pass, via an instruction and/or demonstrations, with no weight updates
- [[brown-2020-gpt3/main-p2]] (p. 40): learning a task from prompt examples without weight updates; structurally like RL2's inner loop, with LM pre-training as the outer loop [as `in-context learning`]
- [[wei-2022-cot/main-p1]] (p. 2): a model performs a task from prompt examples alone, with no finetuning
- [[xie-2022-icl/main]] (p. 1–3): the LM does a task by conditioning on a prompt of input-output examples, with no weight updates; here, implicit Bayesian inference of a shared latent concept

### bayesian

- [[murphy-2023-pml2/ch22-autoregressive]] (p. 825): prompt holds input-output examples plus a test input; model generates the output [new; work fields: bayesian, llm]

## Instances that use it

- [[gpt-3]] — 175B-parameter decoder-only transformer, in-context learning — from [[murphy-2023-pml2/ch22-autoregressive]]

## Candidate bridges

- [structural-analogy] Inner loop (in-context learning) / outer loop (SGD) ↔ ML: meta-learning, learning to learn across a distribution of tasks — the authors say the structure is the same, while staying agnostic on mechanism (p. 4, fn. 1) — from [[brown-2020-gpt3/main-p1]] (llm → llm)
