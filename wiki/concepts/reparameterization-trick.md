---
id: reparameterization-trick
type: concept
fields: [bayesian, llm]
n_sources: 3
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch06-optimization-p1, murphy-2023-pml2/ch10-variational-p1, prince-2023-udl/ch17-variational]
generated_by: build_kg.py
---

# reparameterization-trick

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch06-optimization-p1]] (p. 275): write $z=g(\theta,\epsilon)$ with $\epsilon$ independent of $\theta$; pathwise gradient [new]
- [[murphy-2023-pml2/ch10-variational-p1]] (p. 447): write z = g(ϕ,x,ε) so gradients flow through z [new]

### llm

- [[prince-2023-udl/ch17-variational]] (p. 339): z* = μ + Σ^{1/2}ε*, moving the randomness outside the differentiated path [new]
