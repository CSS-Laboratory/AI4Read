---
id: minimum-description-length
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch07-kolmogorov, cover-2006-elements/ch11-maximum, mackay-2003-information/ch28-model]
aliases: [mdl, minimum-description-length-mdl]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# minimum-description-length

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `mdl` — 1 digest(s)
- `minimum-description-length-mdl` — 1 digest(s)

## Canon spine entry

- **Minimum Description Length (MDL)** (information-theory): pick the model that minimizes the bits for model plus data; formalized Occam's razor (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch07-kolmogorov]] (p. 182): mentioned in Historical Notes as "close in spirit" to the Kolmogorov sufficient statistic
- [[cover-2006-elements/ch11-maximum]] (p. 276): choosing $p$ by a two-stage description length [alias `mdl`]
- [[mackay-2003-information/ch28-model]] (p. 352): prefer the model giving the shortest total message; $L=-\log_2P$, so MDL maps onto Bayesian comparison [alias `minimum-description-length-mdl`; work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] Ockham factor / marginal likelihood ↔ information-theory: Minimum Description Length — model complexity is charged against fit, as bits for the model plus bits for the data. — from [[jaynes-2003-probability/ch20-model]] (bayesian → information-theory)
- [structural-analogy] Map equation ↔ information-theory: Minimum Description Length — pick the model giving the shortest total code (the paper cites refs 14–16 for the equivalence between community finding and coding; ref. 15 is titled "Advances in minimum description length"). — from [[rosvall-2008-maps/main-p1]] (information-theory → information-theory)
- [structural-analogy] shortest program for an object ↔ information-theory: Minimum Description Length — both equate good description with short description — from [[stone-2022-information/ch03-source]] (information-theory → information-theory)
