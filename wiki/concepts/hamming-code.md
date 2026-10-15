---
id: hamming-code
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 3
n_works: 2
tiers: [core]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p2, mackay-2003-information/ch01-introduction, mackay-2003-information/ch13-binary]
generated_by: build_kg.py
---

# hamming-code

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p2]] (p. 211): linear code from parity-check matrix with all non-zero columns; $n=2^l-1$, $k=2^l-l-1$, $d=3$; corrects one error [new]
- [[mackay-2003-information/ch01-introduction]] (p. 9): the (7,4) linear block code with three parity checks that corrects any single flip [new; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch13-binary]] (p. 210): single-error-correcting code whose $\mathbf H$ columns are all nonzero $M$-bit vectors, $N=2^M-1$ [new; work fields: information-theory, bayesian]

## Instances that use it

- [[hamming-code-7-4]] — p_B ≃ 21f², p_b ≃ 9f², rate 4/7 — from [[mackay-2003-information/ch01-introduction]]
- [[raid-hamming-erasure]] — RAID as a (7,4) Hamming code over an erasure channel — from [[mackay-2003-information/ch11-error]]
- [[concatenated-hamming-codes]] — bad distance yet good code family; rate 0.093 at $f=0.0588$ — from [[mackay-2003-information/ch13-binary]]
- [[ebert-hat-puzzle]] — optimal strategy uses a Hamming code — from [[mackay-2003-information/ch13-binary]]
- [[hamming-code-7-4-3]] — $[7,4,3]_2$ linear code with explicit $G,H$, corrects 1 bit error — from [[polyanskiy-2025-information/ch20-random]]

## Candidate bridges

- [same-math] Hat-puzzle strategy ↔ coding: Hamming-code decoding (win prob. $N/(N+1)$) — the strategy literally uses the code's decoder (p. 227). — from [[mackay-2003-information/ch13-binary]] (information-theory → information-theory)
