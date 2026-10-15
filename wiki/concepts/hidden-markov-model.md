---
id: hidden-markov-model
type: concept
fields: [bayesian, control-theory, information-theory, llm]
fields_strong: [bayesian, control-theory, information-theory, llm]
n_sources: 8
n_works: 5
tiers: [deep, reference, core]
grounding: digests
sources: [cover-2006-elements/ch04-entropy, murphy-2023-pml2/ch09-message, murphy-2023-pml2/ch29-state-p1, polyanskiy-2025-information/ch07-tensorization, sarkka-2023-bayesianfiltering/ch05-modeling, sarkka-2023-bayesianfiltering/ch06-bayesian, sarkka-2023-bayesianfiltering/ch12-bayesian, xie-2022-icl/main]
generated_by: build_kg.py
---

# hidden-markov-model

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch05-modeling]] (p. 87): finite-state chain with matrices $\boldsymbol\Pi$ and $\mathbf{O}$ [new; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch06-bayesian]] (p. 103): discrete-state Markov model with measurements; filtered by (6.43) [new; work fields: control-theory, bayesian]
- [[sarkka-2023-bayesianfiltering/ch12-bayesian]] (p. 261): finite states and measurements with matrices $\boldsymbol\Pi$ and $\mathbf O$ [new; work fields: control-theory, bayesian]

### bayesian

- [[murphy-2023-pml2/ch09-message]] (p. 402): chain model with discrete latent states and per-state observation distributions, eq. (9.1) (p. 402) (new)
- [[murphy-2023-pml2/ch29-state-p1]] (p. 980): SSM with discrete $z_t\in\{1..K\}$, parameters $\pi$, $A$ and an observation model [new; work fields: bayesian, control-theory]

### information-theory

- [[cover-2006-elements/ch04-entropy]] (p. 69): here, $Y_i=\phi(X_i)$ for a Markov chain $X$; bounded entropy rate [new]
- [[polyanskiy-2025-information/ch07-tensorization]] (p. 110): Markov state process observed through a memoryless emission channel [new]

### llm

- [[xie-2022-icl/main]] (p. 3): sequence model with hidden states $h_t$ that emit observed tokens; the pretraining document model [new]
