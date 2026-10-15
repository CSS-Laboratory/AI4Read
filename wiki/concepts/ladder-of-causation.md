---
id: ladder-of-causation
type: concept
fields: [bayesian]
n_sources: 13
tiers: [core, reference]
grounding: digests
sources: [murphy-2023-pml2/ch04-graphical-p3, murphy-2023-pml2/ch36-causality-p1, pearl-2018-bookofwhy/ch00-introduction, pearl-2018-bookofwhy/ch01-ladder, pearl-2018-bookofwhy/ch02-buccaneers, pearl-2018-bookofwhy/ch03-evidence, pearl-2018-bookofwhy/ch04-confounding, pearl-2018-bookofwhy/ch06-paradoxes, pearl-2018-bookofwhy/ch07-beyond, pearl-2018-bookofwhy/ch08-counterfactuals, pearl-2018-bookofwhy/ch09-mediation-p1, pearl-2018-bookofwhy/ch09-mediation-p2, pearl-2018-bookofwhy/ch10-big]
raw_ids: [Ladder of causation]
canon_spine: bayesian
generated_by: build_kg.py
---

# ladder-of-causation

## Canon spine entry

- **Ladder of causation** (bayesian): association, intervention and counterfactual reasoning as strictly increasing levels of causal knowledge (HS)

## Definitions in the sources

### bayesian

- [[murphy-2023-pml2/ch04-graphical-p3]] (p. 216): association, intervention, counterfactuals
- [[murphy-2023-pml2/ch36-causality-p1]] (p. 1192): observational, interventional, counterfactual queries, each needing more assumptions
- [[pearl-2018-bookofwhy/ch00-introduction]] (pdf 23): observation, intervention, counterfactuals as steps; only named here, developed in Ch. 1
- [[pearl-2018-bookofwhy/ch01-ladder]] (pdf 34): three rungs: association, intervention, counterfactuals, ordered by the queries each can answer
- [[pearl-2018-bookofwhy/ch02-buccaneers]] (pdf 70, 77): Pearson's world has only rung one; Wright's bridge connects rungs one and two
- [[pearl-2018-bookofwhy/ch03-evidence]] (pdf 126): Bayesian networks answer rung one only. Causal diagrams reach rungs two and three
- [[pearl-2018-bookofwhy/ch04-confounding]] (pdf 134, 146): confounding sits on rung two; counterfactuals on rung three
- [[pearl-2018-bookofwhy/ch06-paradoxes]] (pdf 177): association and causation sit on different rungs, which is where Pearl says the tension behind these paradoxes starts
- [[pearl-2018-bookofwhy/ch07-beyond]] (pdf 213, 228): Eliminating do-expressions moves a query from rung one (seeing) to rung two (doing)
- [[pearl-2018-bookofwhy/ch08-counterfactuals]] (pdf 243, 261): Hume's second definition and PN/PS sit on rung three; hindsight separates it from rung two
- [[pearl-2018-bookofwhy/ch09-mediation-p1]] (pdf 275, 292): indirect effects need rung three [as `Ladder of causation`]
- [[pearl-2018-bookofwhy/ch09-mediation-p2]] (pdf 302–303): Pearl contrasts rung-one (observational) data with rung-three (counterfactual) assumptions
- [[pearl-2018-bookofwhy/ch10-big]] (pdf 325, 331): the hierarchy of levels of causal reasoning (this unit names rung one and mentions three levels); Pearl says deep learning cannot go beyond rung one

## Candidate bridges

- [structural-analogy] Logical vs. causal dependence (3.40) ↔ bayesian: association vs. intervention in the ladder of causation / do-operator — conditioning on information is not the same as physical intervention. — from [[jaynes-2003-probability/ch03-elementary]] (information-theory → bayesian)
