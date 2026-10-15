---
id: entropy-hx
type: concept
fields: [information-theory]
n_sources: 15
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch02-entropy, cover-2006-elements/ch03-asymptotic, cover-2006-elements/ch16-inequalities, jaynes-1957-information/main, jaynes-2003-probability/ch13-decision, jaynes-2003-probability/ch14-simple, mackay-2003-information/ch04-source, mackay-2003-information/ch14-very, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch30-efficient, polyanskiy-2025-information/ch12-variable, stone-2022-information/appd-probability, stone-2022-information/appf-rules, stone-2022-information/ch03-source]
raw_ids: [entropy H(X), entropy-H(X), entropy-HX]
canon_spine: information-theory
generated_by: build_kg.py
---

# entropy-hx

## Canon spine entry

- **entropy H(X)** (information-theory): average surprisal; the irreducible uncertainty of a source in bits per symbol (HS)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 5): $-\sum p(x)\log_2 p(x)$; average bits needed to describe $X$ [as `entropy H(X)`]
- [[cover-2006-elements/ch02-entropy]] (pp. 13–14, 27): $H(X)=-\sum p\log p=E\log\frac1{p(X)}$; depends only on probabilities; $0\le H\le\log|\mathcal X|$ [as `entropy-HX`]
- [[cover-2006-elements/ch03-asymptotic]] (p. 51): H(X) = −E log p(X), the limit of sample entropy
- [[cover-2006-elements/ch16-inequalities]] (p. 483): $-\sum p\log p$, bounded by $\log|\mathcal X|$ [as `entropy-H(X)`]
- [[jaynes-1957-information/main]] (p. 622): $-K\sum p_i\ln p_i$, read as the amount of uncertainty in a distribution
- [[jaynes-2003-probability/ch13-decision]] (p. 403): the pay-off ceiling B[log n − H]
- [[jaynes-2003-probability/ch14-simple]] (pp. 429–430): used as expected entropy $\overline H_D(Y)$; extra conditioning never raises it on average [as `entropy H(X)`]
- [[mackay-2003-information/ch04-source]] (p. 67, p. 70): Σ p_i log₂(1/p_i), the average Shannon information content; maximal for the uniform distribution [as `entropy H(X)`]
- [[mackay-2003-information/ch14-very]] (p. 230): here $H(X)=H_2(f)$ is the noise entropy per bit
- [[mackay-2003-information/ch18-crosswords]] (pp. 261, 264): average information content (18.14); for Wenglish, $H_W=\log_2W/(L+1)$ per character, spaces included [as `entropy H(X)`]
- [[mackay-2003-information/ch30-efficient]] (p. 394): $H_2(f)$ caps information per Metropolis step
- [[polyanskiy-2025-information/ch12-variable]] (p. 199): average of $\log_2 1/P_X(X)$; the benchmark for mean code length [as `entropy H(X)`]
- [[stone-2022-information/appd-probability]] (p. 258): expected Shannon information, $\sum p\log(1/p)$ [as `entropy H(X)`]
- [[stone-2022-information/appf-rules]] (p. 265): $\sum p\log(1/p)$, or its integral form [as `entropy H(X)`]
- [[stone-2022-information/ch03-source]] (pp. 52, 57–58): average information per symbol, $\sum p\log(1/p)$; used as the lower limit for average codeword length [as `entropy-H(X)`]
