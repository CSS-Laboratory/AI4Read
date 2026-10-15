---
id: straight-through-estimator
type: concept
fields: [bayesian]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch21-variational]
generated_by: build_kg.py
---

# straight-through-estimator

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 279): use $g(x)=x$ (or hard tanh) as backward pass for a threshold [new]
- [[murphy-2023-pml2/ch21-variational]] (p. 815): copy decoder-input gradients to the encoder output, bypassing quantization [new]
