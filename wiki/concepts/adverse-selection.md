---
id: adverse-selection
type: concept
fields: [decision-game-theory, economics-finance, political-science]
fields_strong: [decision-game-theory, economics-finance, political-science]
n_sources: 8
n_works: 6
tiers: [core, deep]
grounding: digests
sources: [akerlof-1970-lemons/main, clark-2017-principles/ch12-parliamentary-p3, dixit-2008-art-strategy/ch08-interpreting, dixit-2008-art-strategy/ch13-incentives, myerson-2008-mechanism/main, osborne-2004-introduction/ch09-bayesian, stiglitz-2002-paradigm/main-p1, stiglitz-2002-paradigm/main-p2]
raw_ids: [adverse selection]
canon_spine: [economics-finance]
generated_by: build_kg.py
---

# adverse-selection

## Canon spine entry

- **adverse selection** (economics-finance): hidden quality leads the worst types to dominate the market, which can unravel it (UG)

## Definitions in the sources

### decision-game-theory

- [[dixit-2008-art-strategy/ch08-interpreting]] (p. 232): a deal selectively attracts the worst types (insurance, lemons) [new]
- [[dixit-2008-art-strategy/ch13-incentives]] (p. 357): a hidden innate characteristic rather than a deliberate choice; the chapter says moral hazard is not this problem [new]
- [[myerson-2008-mechanism/main]] (p. 322): problem of eliciting honest reports of hidden information [new]
- [[osborne-2004-introduction/ch09-bayesian]] (p. 281): named in Exercise 280.4; not developed in the text [new]

### economics-finance

- [[akerlof-1970-lemons/main]] (pp. 490, 493): at a given price, the sellers who stay in the market are those with the worst quality, so average quality falls as price falls and the market can unravel
- [[stiglitz-2002-paradigm/main-p1]] (pp. 475, 492): willingness to trade at a price conveys hidden quality, and price changes alter who trades [as `adverse selection`]
- [[stiglitz-2002-paradigm/main-p2]] (p. 498): Stiglitz says the 1976 analysis reinforced earlier results that such markets do not function well [as `adverse selection`]

### political-science

- [[clark-2017-principles/ch12-parliamentary-p3]] (p. 517): agent's type is hidden from the principal [new]

## Instances that use it

- [[akerlof-lemons]] — adverse selection collapses the market for peaches — from [[dixit-2008-art-strategy/ch08-interpreting]]
- [[bilateral-trade-adverse-selection]] — seller value 0/80, buyer value 100/20. Split-the-difference fails; best symmetric plan $y=20$, $q=5/6$ — from [[myerson-2008-mechanism/main]]

## Candidate bridges

- [same-math] Akerlof's adverse selection and Spence-style signaling ↔ decision-game-theory: Bayesian games with incomplete information — the seller's type (quality) is private, and the buyer's belief must match the distribution of types who choose to trade. — from [[akerlof-1970-lemons/main]] (economics-finance → decision-game-theory)
- [structural-analogy] Moral hazard/adverse selection in delegation ↔ information problems elsewhere (insurance, labour markets): the unit itself borrows its examples from insurance and hiring. — from [[clark-2017-principles/ch12-parliamentary-p3]] (political-science → economics-finance)
- [structural-analogy] Adverse selection in insurance and used cars ↔ selection bias in data: the sample that accepts an offer is not representative of the population. — from [[dixit-2008-art-strategy/ch08-interpreting]] (decision-game-theory → bayesian)
- [structural-analogy] unraveling of disclosure ↔ adverse selection/lemons: both are processes in which one group's exit or disclosure changes the pool that remains. — from [[stiglitz-2002-paradigm/main-p1]] (economics-finance → economics-finance)
