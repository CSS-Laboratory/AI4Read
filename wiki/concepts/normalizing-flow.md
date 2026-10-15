---
id: normalizing-flow
type: concept
fields: [bayesian, llm]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch23-normalizing, prince-2023-udl/ch16-normalizing]
generated_by: build_kg.py
---

# normalizing-flow

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch23-normalizing]] (p. 829): density model $x=f(u)$ with simple base $p(u)$ and invertible $f$; sampling and exact likelihood [new]

### llm

- [[prince-2023-udl/ch16-normalizing]] (p. 304): generative model: base density pushed through an invertible network; exact likelihood plus sampling [new]

## Candidate bridges

- [same-math] Probability-flow ODE with exact likelihood ↔ normalizing flows: neural ODE / continuous normalizing flow. — from [[murphy-2023-pml2/ch25-diffusion]] (bayesian → other)
