---
id: binary-symmetric-channel
type: instance
fields: [information-theory, bayesian]
n_sources: 10
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch01-introduction, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, mackay-2003-information/ch08-dependent, mackay-2003-information/ch09-communication, mackay-2003-information/ch10-noisy, mackay-2003-information/ch14-very, pierce-1980-introduction/ch08-noisy, polyanskiy-2025-information/ch04-mutual, stone-2022-information/appa-glossary]
canon_instance: [binary-symmetric-channel-with-repetition-vs-hamming-74-codes]
canon_match_rule: same-work-tokens
generated_by: build_kg.py
---

# binary-symmetric-channel

## Canon entry

- **Binary symmetric channel with repetition vs. Hamming (7,4) codes** (information-theory): shows the trade-off between rate and reliability that the coding theorem says can be beaten — mackay-2003-information

## Descriptions in the sources

### information-theory

- [[cover-2006-elements/ch01-introduction]] (p. 8): $C=1+p\log p+(1-p)\log(1-p)$
- [[cover-2006-elements/ch08-channel-p1]] (p. 187): $C=1-H(p)$
- [[cover-2006-elements/ch08-channel-p2]] (pp. 209): zero-error capacity 0; repetition code has rate $\to0$
- [[mackay-2003-information/ch08-dependent]] (pp. 141, 144): input $x$, noise $y$, output $z$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch09-communication]] (pp. 148, 151): flips each bit with prob. f; C = 1 − H₂(f), 0.39 bits at f = 0.15 [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch10-noisy]] (pp. 163, 168): jointly-typical example ($N=100$, noise 0.2); code reversed as lossy compressor [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch14-very]] (p. 230): flips each bit with probability $f$; the channel analysed [new; work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch08-noisy]] (pp. 158–159): capacity $1+p\log p+(1-p)\log(1-p)$; .53 at 1/10 errors and .92 at 1/100
- [[polyanskiy-2025-information/ch04-mutual]] (p. 50): $I=\log2-h(\delta)$
- [[stone-2022-information/appa-glossary]] (p. 241): symmetric flip probability $P$

## Candidate bridges

- [structural-analogy] Min–sum (Viterbi) most-probable path ↔ bayesian: MAP estimate versus full posterior — path cost is a negative log-likelihood under the binary symmetric channel. — from [[mackay-2003-information/ch48-convolutional]] (information-theory → bayesian)
