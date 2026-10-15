---
id: kelly-criterion
type: concept
fields: [information-theory, bayesian, decision-game-theory, economics-finance]
fields_strong: [information-theory, bayesian, decision-game-theory, economics-finance]
n_sources: 8
n_works: 5
tiers: [core, deep]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch06-gambling, cover-2006-elements/ch07-kolmogorov, cover-2006-elements/ch15-information, jaynes-2003-probability/ch13-decision, kelly-1956-information/main, mackay-2003-information/ch36-decision, pierce-1980-introduction/ch14-back]
aliases: [doubling-rate, kelly-criterion-doubling-rate, kelly-criterion-log-optimal-growth]
canon_spine: [economics-finance, information-theory]
generated_by: build_kg.py
---

# kelly-criterion

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `doubling-rate` — 1 digest(s)
- `kelly-criterion-doubling-rate` — 5 digest(s)
- `kelly-criterion-log-optimal-growth` — 0 digest(s)

## Canon spine entry

- **Kelly criterion / doubling rate** (information-theory): betting fractions that maximize the long-run growth rate of wealth; side information raises growth by its mutual information (UG)

## Canon spine entry

- **Kelly criterion / log-optimal growth** (economics-finance): bet fractions that maximize the long-run growth rate of wealth (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 9): $W$ in (1.7), the maximal asymptotic growth exponent of wealth [as `Kelly criterion / doubling rate`; alias `kelly-criterion-doubling-rate`]
- [[cover-2006-elements/ch06-gambling]] (p. 126–128): doubling rate $W=E\log S$; proportional betting maximises it under the stated conditions [alias `kelly-criterion-doubling-rate`]
- [[cover-2006-elements/ch07-kolmogorov]] (p. 166–167): universal gambling bets $2^{-K(x)}$ on string x; $\log S(x)+K(x)\ge l(x)$ [alias `kelly-criterion-doubling-rate`]
- [[cover-2006-elements/ch15-information]] (p. 461): $W(\mathbf b,F)=E\log\mathbf b^t\mathbf X$, the almost-sure exponential growth rate of reinvested wealth [alias `doubling-rate`; new]
- [[mackay-2003-information/ch36-decision]] (p. 456): Cover's aim of maximizing $\mathbb E[\log m(T)]$; the author does not name it so [work fields: information-theory, bayesian, decision-game-theory]
- [[pierce-1980-introduction/ch14-back]] (pp. 270–271): with inside information at fair odds, capital grows by $2^{NR}$; maximum growth rate equals the information rate [alias `kelly-criterion-doubling-rate`]

### bayesian

- [[jaynes-2003-probability/ch13-decision]] (p. 402): maximise expected log fortune; Exercise 13.1 asks to show the best growth rate is H₀ − H [alias `kelly-criterion-doubling-rate`; work fields: bayesian, information-theory]

### economics-finance

- [[kelly-1956-information/main]] (pp. 919, 925): bet fractions chosen to maximize the exponential growth rate $G$, equivalently the expected log of capital [work fields: economics-finance, information-theory]

## Candidate bridges

- [structural-analogy] doubling rate $W$ ↔ entropy rate: the authors call $W$ a "dual" of the entropy rate (p. 4) — from [[cover-2006-elements/ch01-introduction]] (information-theory → information-theory)
- [same-math] Doubling rate with side information, $\Delta W=I(X;Y)$ ↔ Kelly criterion: side information raises growth by its mutual information — same quantity. — from [[cover-2006-elements/ch06-gambling]] (information-theory → information-theory)
- [structural-analogy] Doubling-rate loss $\le D(f\|g)$ ↔ cross-entropy/KL in model fitting: Thm 15.4.1 bounds the growth-rate cost of acting on model $g$ by a KL divergence (p. 467). — from [[cover-2006-elements/ch15-information]] (information-theory → information-theory)
- [same-math] expected log fortune with tips ↔ information-theory: Kelly criterion — the growth-rate limit H₀ − H is the log-wealth/entropy link in the canon list. — from [[jaynes-2003-probability/ch13-decision]] (bayesian → information-theory)
- [same-math] Cover's aim, maximizing $\mathbb E\log m(T)$ ↔ information-theory: Kelly criterion / doubling rate — the same objective and bets proportional to $p$. — from [[mackay-2003-information/ch36-decision]] (information-theory → information-theory)
- [structural-analogy] one-molecule engine's bit-for-work trade ↔ Kelly criterion: side information has a measurable, bounded value (it raises growth by its mutual information). — from [[pierce-1980-introduction/ch10-information]] (information-theory → information-theory)
- [same-math] Kelly's $2^{NR}$ growth ↔ finance/gambling: the Kelly criterion and doubling rate — the same quantity is the growth rate of wealth. — from [[pierce-1980-introduction/ch14-back]] (information-theory → economics-finance)
- [structural-analogy] genome gaining bits from selection ↔ Kelly criterion/doubling rate — both treat growth as information gained about an environment (the source does not make this link). — from [[stone-2022-information/ch11-information]] (information-theory → unspecified)
