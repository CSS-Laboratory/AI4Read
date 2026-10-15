---
id: principle-of-indifference
type: concept
fields: [bayesian, information-theory]
n_sources: 10
tiers: [core, reference, deep]
grounding: digests
sources: [griffiths-2006-optimal/main, jaynes-2003-probability/ch02-quantitative, jaynes-2003-probability/ch06-elementary-p1, jaynes-2003-probability/ch08-sufficiency, jaynes-2003-probability/ch10-physics, mcelreath-2020-rethinking/ch02-small, mcgrayne-2011-theory/ch01-causes, mcgrayne-2011-theory/ch02-man, mcgrayne-2011-theory/ch03-many, mcgrayne-2011-theory/ch10-46]
raw_ids: [Principle of indifference]
generated_by: build_kg.py
---

# principle-of-indifference

## Definitions in the sources

### bayesian

- [[griffiths-2006-optimal/main]] (p. 770): related only loosely: the fixed uninformative prior $1/t_{total}$ is an alternative the data are inconsistent with
- [[mcelreath-2020-rethinking/ch02-small]] (p. 26): with no reason to prefer a conjecture, weigh all equally; the author notes that "ignorance" is a complicated notion
- [[mcgrayne-2011-theory/ch01-causes]] (p. 9): equal probabilities when nothing distinguishes cases; "law of insufficient reason"
- [[mcgrayne-2011-theory/ch02-man]] (p. 25): equal prior probabilities as a provisional starting point
- [[mcgrayne-2011-theory/ch03-many]] (p. 38): equal odds for causes; Bertrand allows it only for truly equal or unknown cases
- [[mcgrayne-2011-theory/ch10-46]] (p. 134): equal priors; Fisher says not knowing is not equal probabilities

### information-theory

- [[jaynes-2003-probability/ch02-quantitative]] (pp. 38–40): $P(A_i|B)=1/n$ when $B$ is indifferent among $n$ exclusive, exhaustive propositions, derived from permutation symmetry plus desideratum (IIIc). Jaynes calls it the first "baby" group-invariance argument
- [[jaynes-2003-probability/ch06-elementary-p1]] (p. 152): the uniform prior (6.14) as the "seemingly as ignorant as possible" state
- [[jaynes-2003-probability/ch08-sufficiency]] (pp. 261–262): Savage's objection via fine-grained propositions [as `Principle of indifference`]
- [[jaynes-2003-probability/ch10-physics]] (p. 331): here, Jaynes says the compulsion toward a uniform assignment comes from positive knowledge of symmetry, not merely from equal ignorance

## Candidate bridges

- [structural-analogy] Scholium (no reason to prefer a count) ↔ principle of indifference: a symmetry argument fixes the uniform prior. — from [[bayes-1763-essay/main]] (bayesian → other)
- [structural-analogy] Desideratum (IIIc), equivalent knowledge gives equal plausibilities ↔ bayesian: principle of indifference/maximum entropy — from [[jaynes-2003-probability/ch01-plausible]] (information-theory → bayesian)
- [structural-analogy] Principle of indifference (uniform $1/n$) ↔ maximum entropy: the uniform distribution is the most uncommitted one when only normalization is known (canon link; not stated in this unit). — from [[jaynes-2003-probability/ch02-quantitative]] (information-theory → other)
- [structural-analogy] Fundamental domain of a symmetry group fixing the prior ↔ bayesian: Principle of indifference / maximum entropy — symmetry as the formal basis for uninformative priors. — from [[jaynes-2003-probability/ch10-physics]] (information-theory → bayesian)
- [same-math] Maxent model with $\exp(\boldsymbol\theta^\top\boldsymbol\phi)$ ↔ principle of indifference / maximum entropy: least-committal distribution matching feature expectations (p. 174–175). — from [[murphy-2023-pml2/ch04-graphical-p2]] (bayesian → other)
