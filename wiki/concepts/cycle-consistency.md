---
id: cycle-consistency
type: concept
fields: [bayesian, llm]
n_sources: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch26-generative, prince-2023-udl/ch15-generative]
generated_by: build_kg.py
---

# cycle-consistency

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch26-generative]] (p. 920): require $F(G(x))=x$, $G(F(y))=y$ for unpaired translation [new]

### llm

- [[prince-2023-udl/ch15-generative]] (p. 296): translate there and back should recover the input [new]
