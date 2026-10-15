---
id: transfer-entropy
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 5
n_works: 1
tiers: [core]
grounding: digests
sources: [stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appf-rules, stone-2022-information/ch08-rate, stone-2022-information/ch09-transfer]
raw_ids: [transfer entropy]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# transfer-entropy

## Canon spine entry

- **transfer entropy** (information-theory): directed, time-lagged information flow from one process to another (grad)

## Definitions in the sources

### information-theory

- [[stone-2022-information/appa-glossary]] (p. 246): extra information from past of $X$ about $y_t$ beyond $y_{\text{past}}$
- [[stone-2022-information/appb-mathematical]] (p. 249): information past $X$ gives about current $Y$ beyond what past $Y$ gives
- [[stone-2022-information/appf-rules]] (p. 266): H.24 [as `transfer entropy`]
- [[stone-2022-information/ch08-rate]] (p. 194): information measure used for bacteria in Sec. 8.8 [as `transfer entropy`]
- [[stone-2022-information/ch09-transfer]] (p. 196): $I(y_t;x_{\text{past}}|y_{\text{past}})$: extra information $x$'s past gives about $y_t$ beyond $y$'s past

## Candidate bridges

- [structural-analogy] directed information $\vec I(X^n;Y^n)$ ↔ information-theory: transfer entropy — both are sums of conditional mutual informations measuring causally directed flow, though the conditioning sets differ. — from [[polyanskiy-2025-information/ch25-channel]] (information-theory → information-theory)
- [same-math] Transfer entropy for Gaussian variables ↔ econometrics: Granger causality — the author states the two are equivalent in the Gaussian case (p. 201). — from [[stone-2022-information/ch09-transfer]] (information-theory → economics-finance)
