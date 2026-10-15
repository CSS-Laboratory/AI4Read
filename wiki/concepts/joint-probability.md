---
id: joint-probability
type: concept
fields: [information-theory, linear-algebra]
fields_strong: [information-theory, linear-algebra]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [pierce-1980-introduction/app-mathematical, strang-2023-introduction/ch10-learning]
generated_by: build_kg.py
---

# joint-probability

## Definitions in the sources

### information-theory

- [[pierce-1980-introduction/app-mathematical]] (p. 281): p(x,y), the probability of x and y occurring together [new]

### linear-algebra

- [[strang-2023-introduction/ch10-learning]] (pp. 393–394): p_ij, probability of the pair (xᵢ,yⱼ); marginals are row/column sums [new]

## Instances that use it

- [[weatherperson-example]] — hit rate vs cost vs joint probability as accuracy targets — from [[mcelreath-2020-rethinking/ch06-overfitting-p1]]
- [[send-w-receive-b]] — p(W,B) as a joint probability of sending and receiving letters — from [[pierce-1980-introduction/app-mathematical]]
- [[dice-pair]] — joint probability $1/36$; outcome vs outcome value — from [[stone-2022-information/appa-glossary]]
- [[biased-coin-pairs]] — 100 pairs of flips with $p(h)=0.9$ show that independent joint probabilities multiply — from [[stone-2022-information/appf-rules]]
- [[joint-probability-tensor]] — $p_{ijk}$ for age, height, weight — from [[strang-2023-introduction/app1-ranks]]

## Candidate bridges

- [same-math] Bayes' Rule in the poker example ↔ probability/statistics: posterior = joint probability ÷ marginal — the same formula applied to a bid. — from [[dixit-2008-art-strategy/ch08-interpreting]] (decision-game-theory → other:statistics)
- [structural-analogy] evidence as a product of on-line predictions (28.18) ↔ information-theory: chain rule for entropy and cumulative log-loss — a joint probability factorizes step by step — from [[mackay-2003-information/ch28-model]] (information-theory → information-theory)
