---
id: sum-product-algorithm
type: concept
fields: [information-theory, bayesian]
n_sources: 6
tiers: [core, reference]
grounding: digests
sources: [mackay-2003-information/ch16-message, mackay-2003-information/ch25-exact, mackay-2003-information/ch26-exact, mackay-2003-information/ch47-low, mackay-2003-information/ch49-repeat, murphy-2023-pml2/ch09-message]
generated_by: build_kg.py
---

# sum-product-algorithm

## Definitions in the sources

### information-theory

- [[mackay-2003-information/ch16-message]] (p. 245): nodes sum incoming messages; used here to count paths, a weighted sum with weights 1 [new]
- [[mackay-2003-information/ch25-exact]] (pp. 329–330): min–sum with (sum, product): forward–backward, BCJR, belief propagation [new]
- [[mackay-2003-information/ch26-exact]] (p. 336): message rules (26.11, 26.12); exact marginals on tree-like graphs [new]
- [[mackay-2003-information/ch47-low]] (p. 560): message passing of $q$ and $r$ on the bipartite graph, equal to belief propagation; exact if the graph has no cycles [new]
- [[mackay-2003-information/ch49-repeat]] (p. 583): message passing on the factor graph; the accumulator part runs forward–backward [new]

### bayesian

- [[murphy-2023-pml2/ch09-message]] (pp. 414–415): tree BP: upward collect, downward distribute, eqs. (9.58)–(9.62) (pp. 414–415) (new)
