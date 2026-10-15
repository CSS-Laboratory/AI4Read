---
id: back-door-front-door-criterion
type: concept
fields: [bayesian]
n_sources: 11
tiers: [core, reference]
grounding: digests
sources: [hernan-2020-whatif/ch19-time, hernan-2020-whatif/ch21-g, hernan-2020-whatif/ch23-causal, murphy-2023-pml2/ch36-causality-p1, murphy-2023-pml2/ch36-causality-p2, pearl-2016-primer/ch03-effects, pearl-2016-primer/ch04-counterfactuals, pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch08-counterfactuals]
raw_ids: [Back-door / front-door criterion]
canon_spine: bayesian
generated_by: build_kg.py
---

# back-door-front-door-criterion

## Canon spine entry

- **Back-door / front-door criterion** (bayesian): graphical conditions telling which variables to adjust for to identify a causal effect (grad)

## Definitions in the sources

### bayesian

- [[hernan-2020-whatif/ch19-time]] (p. 261): used in the generalized backdoor criterion and SWIG checks
- [[hernan-2020-whatif/ch21-g]] (p. 300): front door formula as a reduction of the big g-formula
- [[hernan-2020-whatif/ch23-causal]] (p. 331): the front-door formula is re-derived via a deterministic copy of $L$ [as `Back-door / front-door criterion`]
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1198): backdoor adjustment as the family of estimation strategies here; details deferred to Section 36.8
- [[murphy-2023-pml2/ch36-causality-p2]] (pp. 1230–1231): graphical conditions for adjustment sets or mediators
- [[pearl-2016-primer/ch03-effects]] (p. front door, p. 69): graph conditions for choosing an adjustment set (backdoor, p. 61) or identifying through a mediator
- [[pearl-2016-primer/ch04-counterfactuals]] (p. 102): graphical conditions that make $Y_x$ independent of $X$ given $Z$ and identify effects
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 149–150): block every back-door path (paths starting with an arrow into X) without adjusting for descendants of X
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 193–194): no back-door path means no adjustment is needed; conditioning wrongly can violate the criterion
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 207–209): Back-door: adjust for a set blocking all back-door paths. Front-door: use a shielded mediator when the confounder is unmeasured
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 257): diagram test for ignorability: $Z$ blocks back-door paths and has no descendant of $X$

## Candidate bridges

- [same-math] front-door formula in Technical Point 23.3 ↔ Back-door / front-door criterion: the same formula under an expanded graph. — from [[hernan-2020-whatif/ch23-causal]] (bayesian → other)
