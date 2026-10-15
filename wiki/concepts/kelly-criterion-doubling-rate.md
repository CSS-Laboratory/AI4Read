---
id: kelly-criterion-doubling-rate
type: concept
fields: [information-theory]
n_sources: 5
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch06-gambling, cover-2006-elements/ch07-kolmogorov, jaynes-2003-probability/ch13-decision, pierce-1980-introduction/ch14-back]
raw_ids: [Kelly criterion / doubling rate]
canon_spine: information-theory
generated_by: build_kg.py
---

# kelly-criterion-doubling-rate

## Canon spine entry

- **Kelly criterion / doubling rate** (information-theory): betting fractions that maximize the long-run growth rate of wealth; side information raises growth by its mutual information (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 9): $W$ in (1.7), the maximal asymptotic growth exponent of wealth [as `Kelly criterion / doubling rate`]
- [[cover-2006-elements/ch06-gambling]] (p. 126–128): doubling rate $W=E\log S$; proportional betting maximises it under the stated conditions
- [[cover-2006-elements/ch07-kolmogorov]] (p. 166–167): universal gambling bets $2^{-K(x)}$ on string x; $\log S(x)+K(x)\ge l(x)$
- [[jaynes-2003-probability/ch13-decision]] (p. 402): maximise expected log fortune; Exercise 13.1 asks to show the best growth rate is H₀ − H
- [[pierce-1980-introduction/ch14-back]] (pp. 270–271): with inside information at fair odds, capital grows by $2^{NR}$; maximum growth rate equals the information rate

## Candidate bridges

- [same-math] Cover's aim, maximizing $\mathbb E\log m(T)$ ↔ information-theory: Kelly criterion / doubling rate — the same objective and bets proportional to $p$. — from [[mackay-2003-information/ch36-decision]] (information-theory → information-theory)
- [structural-analogy] genome gaining bits from selection ↔ Kelly criterion/doubling rate — both treat growth as information gained about an environment (the source does not make this link). — from [[stone-2022-information/ch11-information]] (information-theory → unspecified)
