---
id: self-information
type: concept
fields: [information-theory, bayesian, llm, theory-of-mind]
fields_strong: [information-theory, bayesian, llm, theory-of-mind]
n_sources: 19
n_works: 7
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch02-entropy, cover-2006-elements/ch03-asymptotic, frank-2012-rsa/main, gibson-2019-efficiency/main, mackay-2003-information/ch02-probability, mackay-2003-information/ch04-source, mackay-2003-information/ch05-symbol, mackay-2003-information/ch06-stream, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch20-example, mackay-2003-information/ch39-single, polyanskiy-2025-information/ch02-entropy, shannon-1948-mathematical/main-p1, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appd-probability, stone-2022-information/ch01-information, stone-2022-information/ch02-entropy, stone-2022-information/ch03-source]
aliases: [self-information-surprisal, surprisal]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# self-information

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `self-information-surprisal` — 16 digest(s)
- `surprisal` — 1 digest(s)

## Canon spine entry

- **self-information / surprisal** (information-theory): −log p(x): how surprising one outcome is, so rare events carry more bits (HS)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (p. 20): here "self-information" means $I(X;X)=H(X)$, the entropy of a variable; the text does not use the per-outcome $-\log p(x)$ sense [alias `self-information-surprisal`]
- [[cover-2006-elements/ch03-asymptotic]] (p. 51): −log p(x), used in "almost all events are almost equally surprising" [alias `self-information-surprisal`]
- [[gibson-2019-efficiency/main]] (p. 4): $h(x)=\log_k 1/p(x)$; approximates the shortest code length for $x$ [alias `self-information-surprisal`]
- [[mackay-2003-information/ch02-probability]] (p. 32): $h(x)=\log_2 1/P(x)$, "Shannon information content", in bits [alias `self-information-surprisal`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch04-source]] (p. 67): Shannon information content h(x)=log₂(1/p); additive for independent outcomes [as `self-information / surprisal`; alias `self-information-surprisal`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch05-symbol]] (p. 97): Shannon information content $\log_2(1/p_i)$ equals the optimal codelength [alias `self-information-surprisal`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch06-stream]] (p. 115): $h(\mathbf x\mid\mathcal H)=\log 1/P(\mathbf x\mid\mathcal H)$, the ideal message length, which arithmetic coding matches within 2 bits [alias `self-information-surprisal`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch18-crosswords]] (p. 264): $h(x)=\log 1/P(x)$ (18.13); the author equates it with surprise value and log evidence [as `self-information / surprisal`; alias `self-information-surprisal`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch20-example]] (p. 284): here only the objective $\log 1/P(\{x\})$ appears [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch39-single]] (p. 475): each term of $G$ is the information content of one outcome [as `self-information / surprisal`; alias `self-information-surprisal`; work fields: information-theory, bayesian, llm]
- [[polyanskiy-2025-information/ch02-entropy]] (p. 8): the random variable $\log 1/P_X(X)$ whose mean is $H(X)$ [alias `self-information-surprisal`; new]
- [[shannon-1948-mathematical/main-p1]] (p. 13): used implicitly as $\log 1/p$ of a long message, with $\frac{\log1/p}N\doteq H$
- [[stone-2022-information/appa-glossary]] (p. 243): $h(x)=\log(1/p(x))$ [alias `self-information-surprisal`]
- [[stone-2022-information/appb-mathematical]] (p. 248): here $h(x)=\log(1/p(x))$, "Shannon information, uncertainty, or surprise" [alias `self-information-surprisal`]
- [[stone-2022-information/appd-probability]] (p. 258): $h(x)=\log(1/p(x))$, called Shannon information here [as `self-information / surprisal`; alias `self-information-surprisal`]
- [[stone-2022-information/ch01-information]] (p. 8): only hinted at here: a predictable answer gives no information (p. 8); the formal quantity comes later [as `self-information / surprisal`; alias `self-information-surprisal`]
- [[stone-2022-information/ch02-entropy]] (p. 32): $h(x)=-\log_2p(x)$ bits; surprise of one outcome [alias `self-information-surprisal`]
- [[stone-2022-information/ch03-source]] (p. 55): $h=\log(1/p)$, listed per symbol in Table 3.2 [alias `self-information-surprisal`]

### theory-of-mind

- [[frank-2012-rsa/main]] (p. 10): $-\log p(x)$, how much information is gained by observing $x$; the measure of informativeness [alias `surprisal`; new]

## Candidate bridges

- [structural-analogy] Zipf's frequency–length law ↔ information theory: code length $\approx$ surprisal in optimal codes — both give short codes to likely messages, with probability taken in context. — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [same-math] Surprisal, entropy, conditional entropy, mutual information in Box 2 ↔ information theory: the standard definitions (I)–(V). — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [structural-analogy] multiplicative $w$ (2.26) ↔ information-theory: surprisal $-\log p$ is additive for independent events. Taking $\log w$ turns the product rule into addition, but this unit does not make that move. — from [[jaynes-2003-probability/ch02-quantitative]] (bayesian → information-theory)
- [same-math] Evidence in db (log-likelihood ratio) ↔ information-theory: difference of surprisals $-\log P(D|\overline H)+\log P(D|H)$ (change of base and factor 10) — the same quantity. — from [[jaynes-2003-probability/ch04-elementary]] (bayesian → information-theory)
- [structural-analogy] log ab = log a + log b ↔ information-theory: surprisal of independent events adds — logs turn product into sum. — from [[pierce-1980-introduction/app-mathematical]] (information-theory → information-theory)
- [structural-analogy] normal approximation $nH+\sqrt{nV}Q^{-1}(\epsilon)$ ↔ statistics: central limit theorem for the sum of surprisals. — from [[polyanskiy-2025-information/ch13-fixed]] (information-theory → other:statistics)
- [same-math] log turns products into sums ↔ information theory: surprisal of independent events adds, because $\log$ of a product of probabilities is a sum of logs. This is a candidate only; the unit itself does not state it. — from [[stone-2022-information/appb-mathematical]] (information-theory → information-theory)
- [structural-analogy] Entropy as average surprisal ↔ statistics: sample mean converging to the expected value $E[\cdot]$ — Eq. 2.74 is a sample mean of $-\log p$, and Eq. 2.58 is its expectation. — from [[stone-2022-information/ch02-entropy]] (information-theory → other:statistics)
