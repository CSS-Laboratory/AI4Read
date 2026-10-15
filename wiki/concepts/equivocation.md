---
id: equivocation
type: concept
fields: [information-theory, control-theory]
fields_strong: [information-theory, control-theory]
n_sources: 7
n_works: 4
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch09-incessant, pierce-1980-introduction/ch08-noisy, shannon-1948-mathematical/main-p1, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/ch04-noisy, stone-2022-information/ch08-rate]
generated_by: build_kg.py
---

# equivocation

## Definitions in the sources

### information-theory

- [[pierce-1980-introduction/ch08-noisy]] (p. 154): $H_y(x)$, the recipient's remaining uncertainty about what was sent; the information lost [new]
- [[shannon-1948-mathematical/main-p1]] (p. 20): $H_y(x)$: average ambiguity of the received signal about what was sent [new]
- [[stone-2022-information/appa-glossary]] (p. 243): $H(X|Y)$, uncertainty about the channel input given the output [new]
- [[stone-2022-information/appb-mathematical]] (p. 248): $E=H(X|Y)$ [new]
- [[stone-2022-information/ch04-noisy]] (p. 105): Shannon's name for $H(X|Y)$ [new]
- [[stone-2022-information/ch08-rate]] (p. 174): $H(X|\hat X)$, uncertainty about input given distorted output [new]

### control-theory

- [[ashby-1956-cybernetics/ch09-incessant]] (pp. 188–189): $H_1 - H_2$ in Shannon's example; the measure of information destroyed by noise [new; work fields: control-theory, information-theory]

## Instances that use it

- [[sent-received-0-1-equivocation]] — 1% errors give equivocation 0.081 bit, 0.919 bit gets through — from [[ashby-1956-cybernetics/ch09-incessant]]

## Candidate bridges

- [same-math] equivocation and rate (8.6–8.10) ↔ information-theory: conditional entropy and mutual information identities — same quantities under other names. — from [[pierce-1980-introduction/ch08-noisy]] (information-theory → information-theory)
- [structural-analogy] equivocation falling with cipher length ↔ conditional entropy in statistics — uncertainty shrinks as more data arrives. — from [[pierce-1980-introduction/ch14-back]] (information-theory → unspecified)
