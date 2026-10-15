---
id: meta-learning
type: concept
fields: [llm, theory-of-mind]
fields_strong: [llm, theory-of-mind]
n_sources: 2
n_works: 2
tiers: [core, deep]
grounding: digests
sources: [brown-2020-gpt3/main-p1, rabinowitz-2018-machine-tom/main]
generated_by: build_kg.py
---

# meta-learning

## Definitions in the sources

### llm

- [[brown-2020-gpt3/main-p1]] (p. 3–4, fn. 1): here: the model acquires broad skills in the outer loop (SGD pre-training) and uses them to adapt or recognize a task in the inner loop [new]

### theory-of-mind

- [[rabinowitz-2018-machine-tom/main]] (pdf 2): learning across many agents so inference on a new agent is fast and sample-efficient [new]

## Candidate bridges

- [structural-analogy] Inner loop (in-context learning) / outer loop (SGD) ↔ ML: meta-learning, learning to learn across a distribution of tasks — the authors say the structure is the same, while staying agnostic on mechanism (p. 4, fn. 1) — from [[brown-2020-gpt3/main-p1]] (llm → llm)
- [structural-analogy] Inner loop (prompt) / outer loop (pretraining) ↔ meta-learning (RL2, MAML): adaptation happens through activations versus through weight updates. — from [[brown-2020-gpt3/main-p2]] (llm → other:meta-learning-rl2-maml)
- [structural-analogy] Hierarchical Bayesian DG and meta-learning models (Figs. 19.13, 19.15) ↔ Hierarchical models / partial pooling: task parameters drawn from a shared population level. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → bayesian)
