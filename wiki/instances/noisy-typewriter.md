---
id: noisy-typewriter
type: instance
fields: [information-theory]
n_sources: 4
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, mackay-2003-information/ch09-communication, stone-2022-information/ch04-noisy]
generated_by: build_kg.py
---

# noisy-typewriter

## Descriptions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p1]] (pp. 185–186): $C=\log13$
- [[cover-2006-elements/ch08-channel-p2]] (p. 208): alternate-letter code with 13 codewords achieves $\log13$ and satisfies the equality conditions
- [[mackay-2003-information/ch09-communication]] (pp. 148, 152): C = log₂9 reached with a length-1 code on every third letter
- [[stone-2022-information/ch04-noisy]] (pp. 108–110): non-confusable subset gives error-free 3.17 bits/s

## Candidate bridges

- [structural-analogy] Disjoint output triplets in the noisy typewriter ↔ coding theory: non-overlapping decoding regions for codewords — one input per region lets lookup decoding work. — from [[stone-2022-information/ch04-noisy]] (information-theory → information-theory)
