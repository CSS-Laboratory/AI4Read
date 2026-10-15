---
id: symmetric-channel
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p1, mackay-2003-information/ch10-noisy]
generated_by: build_kg.py
---

# symmetric-channel

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p1]] (p. 190): rows are permutations of each other and columns too; weakly symmetric: every row a permutation of every other row, and equal column sums; capacity $\log|\mathcal Y|-H(\text{row})$ [new]
- [[mackay-2003-information/ch10-noisy]] (p. 170): Gallager's partition-into-permutation-matrices definition; Ex. 10.10 asks to prove that the uniform input is optimal (p. 171) [new; work fields: information-theory, bayesian]

## Instances that use it

- [[binary-symmetric-channel]] — $C=1+p\log p+(1-p)\log(1-p)$ — from [[cover-2006-elements/ch01-introduction]]
- [[binary-symmetric-channel]] — $C=1-H(p)$ — from [[cover-2006-elements/ch08-channel-p1]]
- [[weakly-symmetric-channel-example]] — matrix (8.24) — from [[cover-2006-elements/ch08-channel-p1]]
- [[binary-symmetric-channel]] — zero-error capacity 0; repetition code has rate $\to0$ — from [[cover-2006-elements/ch08-channel-p2]]
- [[binary-symmetric-channel]] — input $x$, noise $y$, output $z$ — from [[mackay-2003-information/ch08-dependent]]
- [[binary-symmetric-channel]] — flips each bit with prob. f; C = 1 − H₂(f), 0.39 bits at f = 0.15 — from [[mackay-2003-information/ch09-communication]]
- [[binary-symmetric-channel]] — jointly-typical example ($N=100$, noise 0.2); code reversed as lossy compressor — from [[mackay-2003-information/ch10-noisy]]
- [[binary-symmetric-channel]] — flips each bit with probability $f$; the channel analysed — from [[mackay-2003-information/ch14-very]]
- [[two-bsc-broadcast]] — two binary symmetric channels with a shared input, $f_A=0.01$, $f_B=0.1$ — from [[mackay-2003-information/ch15-further]]
- [[3-1-repetition-style-code-decoder]] — exercise: optimal decoder for a (3,1) code on a binary symmetric channel as a neuron — from [[mackay-2003-information/ch39-single]]
- [[binary-symmetric-channel]] — capacity $1+p\log p+(1-p)\log(1-p)$; .53 at 1/10 errors and .92 at 1/100 — from [[pierce-1980-introduction/ch08-noisy]]
- [[binary-symmetric-channel]] — $I=\log2-h(\delta)$ — from [[polyanskiy-2025-information/ch04-mutual]]
- [[binary-symmetric-channel]] — symmetric flip probability $P$ — from [[stone-2022-information/appa-glossary]]

## Candidate bridges

- [structural-analogy] Min–sum (Viterbi) most-probable path ↔ bayesian: MAP estimate versus full posterior — path cost is a negative log-likelihood under the binary symmetric channel. — from [[mackay-2003-information/ch48-convolutional]] (information-theory → bayesian)
