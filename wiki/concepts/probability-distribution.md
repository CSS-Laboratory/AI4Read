---
id: probability-distribution
type: concept
fields: [decision-game-theory, information-theory, linear-algebra]
fields_strong: [decision-game-theory, information-theory, linear-algebra]
n_sources: 3
n_works: 3
tiers: [core]
grounding: digests
sources: [deisenroth-2020-mml/ch06-probability-p1, osborne-2004-introduction/ch17-mathematics, stone-2022-information/ch02-entropy]
aliases: [probability-distribution-law]
generated_by: build_kg.py
---

# probability-distribution

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `probability-distribution-law` — 1 digest(s)

## Definitions in the sources

### decision-game-theory

- [[osborne-2004-introduction/ch17-mathematics]] (pp. 449–450): assignment of probabilities to events; each in $[0,1]$, total 1 [new]

### information-theory

- [[stone-2022-information/ch02-entropy]] (p. 22, p. 27): probabilities of all values of a variable; sums to 1 [new]

### linear-algebra

- [[deisenroth-2020-mml/ch06-probability-p1]] (p. 177, p. 183): $P_X=P\circ X^{-1}$; also loosely used for pmf/pdf/cdf [alias `probability-distribution-law`; new]

## Instances that use it

- [[gaussian-mixture-density-estimation]] — a probability distribution describing the data, fitted iteratively — from [[deisenroth-2020-mml/ch01-introduction]]

## Candidate bridges

- [structural-analogy] Soft alignment replacing hard word alignment ↔ the paper's discussion of statistical MT: a probability distribution over alignments instead of a single choice. — from [[bahdanau-2015-attention/main]] (llm → other:statistics)
- [structural-analogy] fractional threat probability $\pi$ ↔ mixed strategy: both are probability distributions over actions, but here the odds are meant to be learned by the other player. — from [[schelling-1960-conflict/ch07-randomization]] (decision-game-theory → decision-game-theory)
