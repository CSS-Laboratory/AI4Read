---
id: redundancy
type: concept
fields: [information-theory, bayesian, control-theory]
fields_strong: [information-theory, bayesian, control-theory]
n_sources: 29
n_works: 10
tiers: [core, deep, reference]
grounding: digests
sources: [ashby-1956-cybernetics/ch07-quantity, ashby-1956-cybernetics/ch09-incessant, cover-2006-elements/ch08-channel-p1, cover-2006-elements/ch08-channel-p2, gibson-2019-efficiency/main, mackay-2003-information/ch01-introduction, mackay-2003-information/ch02-probability, mackay-2003-information/ch04-source, mackay-2003-information/ch06-stream, mackay-2003-information/ch15-further, mackay-2003-information/ch17-communication, mackay-2003-information/ch18-crosswords, mackay-2003-information/ch19-have, pierce-1980-introduction/ch02-origins, pierce-1980-introduction/ch04-encoding, pierce-1980-introduction/ch07-efficient, pierce-1980-introduction/ch08-noisy, pierce-1980-introduction/ch12-information, pierce-1980-introduction/ch13-information, polyanskiy-2025-information/ch15-universal, shannon-1948-mathematical/main-p1, shannon-1951-prediction/main, stone-2022-information/appa-glossary, stone-2022-information/ch01-information, stone-2022-information/ch02-entropy, stone-2022-information/ch03-source, stone-2022-information/ch04-noisy, stone-2022-information/ch11-information, todorov-2002-ofc/main]
canon_spine: [communication-theory]
generated_by: build_kg.py
---

# redundancy

## Canon spine entry

- **Redundancy** (communication-theory): predictable structure in messages that guards against noise (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p1]] (p. 184): added in a controlled way during transmission to fight errors
- [[cover-2006-elements/ch08-channel-p2]] (p. 216): added deliberately by coding so loss can be repaired (p. 209); source redundancy may suit the channel
- [[gibson-2019-efficiency/main]] (p. 11): extra marking (e.g. gender) that may act like parity bits against noise
- [[mackay-2003-information/ch01-introduction]] (p. 4): extra bits added by the encoder, which the decoder uses to infer both message and noise [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch02-probability]] (p. 33): $1-H(X)/\log|\mathcal A_X|$, as defined here; not used later in the book [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch04-source]] (p. 73): structure making a file compressible, e.g. unused ASCII bit, unequal letter frequencies [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch06-stream]] (p. 110): English has redundancy in character frequencies, letter pairs and word predictability [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch15-further]] (p. 236): extra digits needed for detection vs correction [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch17-communication]] (p. 249): C₁'s forced 0 is redundant and can be removed [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch18-crosswords]] (p. 260): here: why crosswords constrain a language. No redundancy means any grid is valid, and high redundancy makes crosswords hard [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch19-have]] (p. 269): the selection signal's bits are redundant because similar unfit individuals fail for similar reasons [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch02-origins]] (p. 39): Nyquist's sense: a signal component that conveys no intelligence because it is predictable at the receiver
- [[pierce-1980-introduction/ch04-encoding]] (p. 75): not named in this unit. The word-versus-letter comparison (p. 75) concerns restricting codes to sequences that actually occur. [weak: not really used in this unit]
- [[pierce-1980-introduction/ch07-efficient]] (pp. 143–144): the clues messages give the recipient; it lets errors be survived or detected; removing it saves digits but makes errors dangerous
- [[pierce-1980-introduction/ch08-noisy]] (p. 164): here: added deliberately, in the right form, to permit correction
- [[pierce-1980-introduction/ch12-information]]: not named in this unit; not listed here. [weak: not really used in this unit]
- [[pierce-1980-introduction/ch13-information]] (p. 251–252): repetition and rule-governed structure that make the next event partly expected
- [[polyanskiy-2025-information/ch15-universal]] (pp. 248, 251, 263): used with the meanings of the canon list
- [[shannon-1948-mathematical/main-p1]] (p. 14): $1-$relative entropy; for English about 50% (considering structure up to about eight letters)
- [[shannon-1951-prediction/main]] (p. 50): constraint imposed on text by statistical structure; estimated at about 50% (≤ 8 letters) and roughly 75% (long range)
- [[stone-2022-information/appa-glossary]] (p. 245): a value obtainable from other values
- [[stone-2022-information/ch01-information]] (p. 15): dependence between neighbouring data values (e.g. similar pixels) that allows compression
- [[stone-2022-information/ch02-entropy]] (p. 28): natural redundancy can be removed by compression; redundancy may be added against noise
- [[stone-2022-information/ch03-source]] (p. 48): author's usage: predictable symbols or unequal frequencies make the information rate fall below capacity
- [[stone-2022-information/ch04-noisy]] (p. 104): here it is compressible, but also protects against noise
- [[stone-2022-information/ch11-information]] (p. 218, 220): spatial and temporal similarity in images, removed to compress; small redundancy re-added for error protection

### control-theory

- [[ashby-1956-cybernetics/ch07-quantity]] (p. 130): the name used in Shannon's work for constraints [new; work fields: control-theory, information-theory]
- [[ashby-1956-cybernetics/ch09-incessant]] (pp. 181–182): the set of vectors uses fewer combinations than independent components would allow, so components can be dropped without loss of variety; relative to a specified set [new; work fields: control-theory, information-theory]
- [[todorov-2002-ofc/main]] (p. 4): states with equal cost-to-go $v^*$ are task-equivalent, so $\Delta v^*=0$ means a redundant deviation [new]

## Instances that use it

- [[traffic-lights-entropy-and-redundancy]] — entropy 1.63 bits (pp. 174–175); redundancy in two different sets of vectors — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[guessing-game]] — a human predicting English text characters shows redundancy and motivates model-based compression — from [[mackay-2003-information/ch06-stream]]
- [[vowel-and-x-replacement]] — text surviving errors because of redundancy — from [[pierce-1980-introduction/ch07-efficient]]
- [[bernoulli-class-redundancy]] — Bernoulli class: $\mathcal R_n^*=\frac12\log n+O(1)$, KT and Laplace rules — from [[polyanskiy-2025-information/ch15-universal]]
- [[crossword-redundancy]] — if constraints are chaotic and random, large 2D puzzles are just possible at 50% redundancy and 3D puzzles should be possible at 33% — from [[shannon-1948-mathematical/main-p1]]
- [[array-description-64-to-35]] — redundancy gives a 35-symbol description of 64 symbols — from [[simon-1962-architecture/main]]

## Candidate bridges

- [structural-analogy] constraint as reduction of variety ↔ information theory: redundancy (Ashby links them himself, p. 130) — from [[ashby-1956-cybernetics/ch07-quantity]] (control-theory → information-theory)
- [metaphor] Black's "excess gain thrown away by feedback" ↔ error-correcting redundancy: spend gain to buy insensitivity. — from [[astrom-2021-feedbacksystems/ch13-robust]] (control-theory → other:error-correcting-redundancy)
- [structural-analogy] Redundant gender marking ↔ error-correcting codes: parity bits add redundancy for robustness to noise. — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [metaphor] Adding structured redundancy so noise can be undone ↔ bayesian: priors that let an inference "correct" noisy data. — from [[mackay-2003-information/ch09-communication]] (information-theory → bayesian)
- [structural-analogy] Word-level code reserving patterns only for real words ↔ information-theory: redundancy — a restricted set of sequences leaves room to compress. — from [[pierce-1980-introduction/ch04-encoding]] (information-theory → information-theory)
- [structural-analogy] Redundancy removed means errors become false messages ↔ error-correcting codes: structured redundancy is added back (Pierce only says the next chapter treats noise). — from [[pierce-1980-introduction/ch07-efficient]] (information-theory → information-theory)
- [same-math] $C_n$ as capacity of $\theta\mapsto X^n$ ↔ information-theory: redundancy and minimax regret of universal compression — the source states they are the same quantity (p. 604). — from [[polyanskiy-2025-information/ch35-entropic]] (information-theory → information-theory)
- [structural-analogy] constraints on a language remove garbles in a message ↔ information theory: redundancy that lets a receiver correct errors — Schelling's own comparison (p. 338) is an analogy, not the same math. — from [[schelling-1960-conflict/appc-re-p1]] (decision-game-theory → information-theory)
