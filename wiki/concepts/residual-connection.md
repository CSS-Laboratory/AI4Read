---
id: residual-connection
type: concept
fields: [llm, bayesian]
fields_strong: [llm, bayesian]
n_sources: 2
n_works: 2
tiers: [reference]
grounding: digests
sources: [murphy-2023-pml2/ch16-deep, prince-2023-udl/ch11-residual]
generated_by: build_kg.py
---

# residual-connection

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch16-deep]] (p. 635): skip connection $\boldsymbol y=\varphi(\mathrm{conv}(\boldsymbol x))+\boldsymbol x$; layer learns an offset [new; work fields: bayesian, llm]

### llm

- [[prince-2023-udl/ch11-residual]] (p. 189): add a layer's input back to its output, $\mathbf h+\mathbf f[\mathbf h]$; the layer learns an additive change [new]
