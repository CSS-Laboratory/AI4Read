---
id: semi-gradient-methods
type: concept
fields: [control-theory]
fields_strong: [control-theory]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [sutton-2018-rl/ch09-policy-p1, sutton-2018-rl/ch11-off]
aliases: [semi-gradient-method]
generated_by: build_kg.py
---

# semi-gradient-methods

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `semi-gradient-method` — 1 digest(s)

## Definitions in the sources

### control-theory

- [[sutton-2018-rl/ch09-policy-p1]] (p. 202): bootstrapping updates that ignore the weights' effect on the target, so are not true gradient descent [new]
- [[sutton-2018-rl/ch11-off]] (pp. 258, 270): update with the gradient of the estimate only, ignoring the bootstrapped target's dependence on $\mathbf w$; not true SGD [alias `semi-gradient-method`; new]
