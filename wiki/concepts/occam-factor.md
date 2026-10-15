---
id: occam-factor
type: concept
fields: [bayesian, information-theory]
fields_strong: [bayesian, information-theory]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [jaynes-2003-probability/ch20-model, mackay-2003-information/ch28-model]
aliases: [ockham-factor]
generated_by: build_kg.py
---

# occam-factor

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `ockham-factor` — 1 digest(s)

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/ch20-model]] (pp. 604, 610): $W=\int d\theta\,(L/L_{\max})\,p(\theta|MI)\le1$ [alias `ockham-factor`; new; work fields: bayesian, information-theory]

### information-theory

- [[mackay-2003-information/ch28-model]] (pp. 349–350): the factor below one multiplying the best-fit likelihood. In 1-D with a uniform prior it is $\sigma_{w|D}/\sigma_w$; in $K$ dimensions $P(\mathbf{w}_{MP}\mid H)\det^{-1/2}(\mathbf{A}/2\pi)$ [new; work fields: information-theory, bayesian]

## Candidate bridges

- [structural-analogy] Ockham factor / marginal likelihood ↔ information-theory: Minimum Description Length — model complexity is charged against fit, as bits for the model plus bits for the data. — from [[jaynes-2003-probability/ch20-model]] (bayesian → information-theory)
- [structural-analogy] Occam factor in (24.13) ↔ bayesian: the volume factor from integrating out a fitted parameter, as in model comparison (Chapter 28, mentioned p. 322). — from [[mackay-2003-information/ch24-exact]] (information-theory → bayesian)
- [structural-analogy] log Occam factor as information gained about parameters ↔ information-theory: reduction of uncertainty (entropy) from data — the source describes the log as "information gained" (p. 349) — from [[mackay-2003-information/ch28-model]] (information-theory → information-theory)
