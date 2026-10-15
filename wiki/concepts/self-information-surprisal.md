---
id: self-information-surprisal
type: concept
fields: [information-theory]
n_sources: 16
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch02-entropy, cover-2006-elements/ch03-asymptotic, gibson-2019-efficiency/main, mackay-2003-information/ch02-probability, mackay-2003-information/ch04-source, mackay-2003-information/ch05-symbol, mackay-2003-information/ch06-stream, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch39-single, polyanskiy-2025-information/ch02-entropy, stone-2022-information/appa-glossary, stone-2022-information/appb-mathematical, stone-2022-information/appd-probability, stone-2022-information/ch01-information, stone-2022-information/ch02-entropy, stone-2022-information/ch03-source]
raw_ids: [self-information / surprisal]
canon_spine: information-theory
generated_by: build_kg.py
---

# self-information-surprisal

## Canon spine entry

- **self-information / surprisal** (information-theory): −log p(x): how surprising one outcome is, so rare events carry more bits (HS)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (p. 20): here "self-information" means $I(X;X)=H(X)$, the entropy of a variable; the text does not use the per-outcome $-\log p(x)$ sense
- [[cover-2006-elements/ch03-asymptotic]] (p. 51): −log p(x), used in "almost all events are almost equally surprising"
- [[gibson-2019-efficiency/main]] (p. 4): $h(x)=\log_k 1/p(x)$; approximates the shortest code length for $x$
- [[mackay-2003-information/ch02-probability]] (p. 32): $h(x)=\log_2 1/P(x)$, "Shannon information content", in bits
- [[mackay-2003-information/ch04-source]] (p. 67): Shannon information content h(x)=log₂(1/p); additive for independent outcomes [as `self-information / surprisal`]
- [[mackay-2003-information/ch05-symbol]] (p. 97): Shannon information content $\log_2(1/p_i)$ equals the optimal codelength
- [[mackay-2003-information/ch06-stream]] (p. 115): $h(\mathbf x\mid\mathcal H)=\log 1/P(\mathbf x\mid\mathcal H)$, the ideal message length, which arithmetic coding matches within 2 bits
- [[mackay-2003-information/ch18-crosswords]] (p. 264): $h(x)=\log 1/P(x)$ (18.13); the author equates it with surprise value and log evidence [as `self-information / surprisal`]
- [[mackay-2003-information/ch39-single]] (p. 475): each term of $G$ is the information content of one outcome [as `self-information / surprisal`]
- [[polyanskiy-2025-information/ch02-entropy]] (p. 8): the random variable $\log 1/P_X(X)$ whose mean is $H(X)$ [new]
- [[stone-2022-information/appa-glossary]] (p. 243): $h(x)=\log(1/p(x))$
- [[stone-2022-information/appb-mathematical]] (p. 248): here $h(x)=\log(1/p(x))$, "Shannon information, uncertainty, or surprise"
- [[stone-2022-information/appd-probability]] (p. 258): $h(x)=\log(1/p(x))$, called Shannon information here [as `self-information / surprisal`]
- [[stone-2022-information/ch01-information]] (p. 8): only hinted at here: a predictable answer gives no information (p. 8); the formal quantity comes later [as `self-information / surprisal`]
- [[stone-2022-information/ch02-entropy]] (p. 32): $h(x)=-\log_2p(x)$ bits; surprise of one outcome
- [[stone-2022-information/ch03-source]] (p. 55): $h=\log(1/p)$, listed per symbol in Table 3.2
