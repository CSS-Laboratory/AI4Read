---
id: ip-weighting
type: concept
fields: [bayesian]
n_sources: 4
tiers: [core]
grounding: digests
sources: [hernan-2020-whatif/ch02-randomized, hernan-2020-whatif/ch08-selection, hernan-2020-whatif/ch12-ip, hernan-2020-whatif/ch13-standardization]
generated_by: build_kg.py
---

# ip-weighting

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch02-randomized]] (pp. 22–23): weight $W^A=1/f[A\mid L]$ to build a pseudo-population with $L\perp A$ [new]
- [[hernan-2020-whatif/ch08-selection]] (p. 117): weight each selected person by $1/\Pr[C=0|L,A]$ so she stands for similar unselected people [new]
- [[hernan-2020-whatif/ch12-ip]] (p. 164–165): weight each person by 1/(probability of the treatment received given $L$) to create a pseudo-population where $A\perp L$ [new]
- [[hernan-2020-whatif/ch13-standardization]] (p. 175): pseudo-population method needing a model for treatment (and censoring) given $L$ [new]

## Instances that use it

- [[wasabi-trial]] — worked IP-weighting example, risk ratio 0.89 versus 1 — from [[hernan-2020-whatif/ch08-selection]]
- [[smoking-cessation-weight-gain]] — NHEFS example: IP weighting and standardization both give 3.5 kg — from [[hernan-2020-whatif/ch13-standardization]]
- [[sequentially-randomized-experiment-table-21-1]] — two-time-point dataset where g-formula, IP weighting and g-estimation all give 60 for both strategies — from [[hernan-2020-whatif/ch21-g]]

## Candidate bridges

- [structural-analogy] IP weighting by $1/\Pr[C=0|L,A]$ ↔ Monte Carlo: reweighting samples by inverse probability to mimic another distribution. — from [[hernan-2020-whatif/ch08-selection]] (bayesian → other)
- [structural-analogy] cloning + censoring + IP weighting ↔ survey sampling / missing data: reweighting retained cases to represent those lost to informative selection. — from [[hernan-2020-whatif/ch22-target]] (bayesian → other)
