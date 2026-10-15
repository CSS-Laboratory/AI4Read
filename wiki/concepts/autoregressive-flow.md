---
id: autoregressive-flow
type: concept
fields: [bayesian, llm]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch23-normalizing, prince-2023-udl/ch16-normalizing]
generated_by: build_kg.py
---

# autoregressive-flow

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch23-normalizing]] (p. 837): $x_i=h(u_i;\Theta_i(x_{1:i-1}))$; triangular Jacobian; sequential $f$, parallel $f^{-1}$ [new]

### llm

- [[prince-2023-udl/ch16-normalizing]] (p. 313): output $d$ depends on inputs $1{:}d$; fast in one direction, sequential in the other [new]

## Instances that use it

- [[parallel-wavenet-style-distillation]] — teacher–student training of an inverse autoregressive flow — from [[prince-2023-udl/ch16-normalizing]]

## Candidate bridges

- [structural-analogy] Masked autoregressive flow ↔ llm: causal masking in self-attention, which prunes dependence on later positions (p. 314) — from [[prince-2023-udl/ch16-normalizing]] (llm → llm)
