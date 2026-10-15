---
id: central-limit-theorem
type: concept
fields: [bayesian, information-theory, linear-algebra]
fields_strong: [bayesian, information-theory, linear-algebra]
n_sources: 5
n_works: 4
tiers: [core]
grounding: digests
sources: [jaynes-2003-probability/ch07-central-p1, jaynes-2003-probability/ch07-central-p2, mcgrayne-2011-theory/ch02-man, stone-2022-information/appf-rules, strang-2023-introduction/ch10-learning]
generated_by: build_kg.py
---

# central-limit-theorem

## Definitions in the sources

### bayesian

- [[jaynes-2003-probability/ch07-central-p1]] (p. 199): sums of many small contributions approach the Gaussian; here only cited and described, not proved [new; work fields: bayesian, information-theory]
- [[jaynes-2003-probability/ch07-central-p2]] (p. 222): sums of many independent terms tend to a Gaussian. Here the editor shows how it follows from cumulants [new; work fields: bayesian, information-theory]
- [[mcgrayne-2011-theory/ch02-man]] (p. 30): with some exceptions, any average of a large number of similar terms has a normal, bell-shaped distribution [new]

### information-theory

- [[stone-2022-information/appf-rules]] (p. 264): sample means from almost any distribution become increasingly Gaussian as $n$ grows [new]

### linear-algebra

- [[strang-2023-introduction/ch10-learning]] (p. 390): averages of many samples approach a normal distribution [new]

## Candidate bridges

- [structural-analogy] Posterior asymptotic normality ↔ the central limit theorem: the author compares only the generality of conditions, saying that like the CLT the result holds far beyond iid data (p. 590). — from [[gelman-2013-bda3/appb-outline]] (bayesian → other:the-central-limit-theorem)
- [structural-analogy] Gaussian by addition ↔ probability theory: the central limit theorem (not named in this unit); same qualitative statement, but the unit gives only simulations and a cancellation argument, not a theorem. — from [[mcelreath-2020-rethinking/ch04-linear-p1]] (bayesian → other:probability)
- [same-math] Galton board as a sum of coin flips ↔ central limit theorem: the text itself says the board is a demonstration of Laplace's theorem (pdf 59). — from [[pearl-2018-bookofwhy/ch02-buccaneers]] (bayesian → bayesian)
- [structural-analogy] normal approximation $nH+\sqrt{nV}Q^{-1}(\epsilon)$ ↔ statistics: central limit theorem for the sum of surprisals. — from [[polyanskiy-2025-information/ch13-fixed]] (information-theory → other:statistics)
