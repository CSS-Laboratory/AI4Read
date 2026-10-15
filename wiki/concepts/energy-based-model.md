---
id: energy-based-model
type: concept
fields: [bayesian, llm]
n_sources: 3
tiers: [reference, deep]
grounding: digests
sources: [bengio-2003-nplm/main, murphy-2023-pml2/ch04-graphical-p2, murphy-2023-pml2/ch24-energy]
generated_by: build_kg.py
---

# energy-based-model

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p2]] (p. 166): $p\propto\exp(-\mathcal E)$ with low energy meaning high probability; the Gibbs distribution [new]
- [[murphy-2023-pml2/ch24-energy]] (p. 849): density $\propto\exp(-E_\theta(x))$ with arbitrary energy function [new]

### llm

- [[bengio-2003-nplm/main]] (p. 1150): the variant scoring a word subsequence with energy $E$, normalized by a softmax over the last word [new]
