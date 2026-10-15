---
id: probability-distribution
type: concept
fields: [decision-game-theory, information-theory]
n_sources: 2
tiers: [core]
grounding: digests
sources: [osborne-2004-introduction/ch17-mathematics, stone-2022-information/ch02-entropy]
generated_by: build_kg.py
---

# probability-distribution

## Definitions in the sources

### decision-game-theory

- [[osborne-2004-introduction/ch17-mathematics]] (pp. 449–450): assignment of probabilities to events; each in $[0,1]$, total 1 [new]

### information-theory

- [[stone-2022-information/ch02-entropy]] (p. 22, p. 27): probabilities of all values of a variable; sums to 1 [new]

## Instances that use it

- [[gaussian-mixture-density-estimation]] — a probability distribution describing the data, fitted iteratively — from [[deisenroth-2020-mml/ch01-introduction]]

## Candidate bridges

- [structural-analogy] Soft alignment replacing hard word alignment ↔ the paper's discussion of statistical MT: a probability distribution over alignments instead of a single choice. — from [[bahdanau-2015-attention/main]] (llm → other)
- [structural-analogy] fractional threat probability $\pi$ ↔ mixed strategy: both are probability distributions over actions, but here the odds are meant to be learned by the other player. — from [[schelling-1960-conflict/ch07-randomization]] (decision-game-theory → other)
