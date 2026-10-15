---
id: error-correcting-code
type: concept
fields: [information-theory, bayesian]
fields_strong: [information-theory, bayesian]
n_sources: 20
n_works: 7
tiers: [core, reference]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p2, gibson-2019-efficiency/main, mackay-2003-information/ch01-introduction, mackay-2003-information/ch11-error, mackay-2003-information/ch12-hash, mackay-2003-information/ch13-binary, mackay-2003-information/ch14-very, mackay-2003-information/ch15-further, mackay-2003-information/ch25-exact, mackay-2003-information/ch47-low, mackay-2003-information/ch48-convolutional, mackay-2003-information/ch49-repeat, mackay-2003-information/ch50-digital, pierce-1980-introduction/ch08-noisy, pierce-1980-introduction/ch14-back, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch20-random, shannon-1948-mathematical/main-p1, stone-2022-information/ch04-noisy, stone-2022-information/ch11-information]
raw_ids: [error-correcting code]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# error-correcting-code

## Canon spine entry

- **error-correcting code** (information-theory): adding structured redundancy so errors can be detected and corrected (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p2]] (p. 209): added structured redundancy; parity-check and Hamming codes
- [[gibson-2019-efficiency/main]] (p. 11): only the analogy to parity bits is made
- [[mackay-2003-information/ch01-introduction]] (p. 4): encoder/decoder pair that adds structured redundancy to detect and correct errors [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch11-error]] (p. 183): redundancy added to detect and correct errors; classified here as very good, good, bad, practical [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch12-hash]] (p. 203): adds redundancy to correct errors; needs far more check bits than a hash used for detection [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch13-binary]] (p. 212): used as in the canon; here for the BSC with $C=1-H_2(f)$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch14-very]] (p. 229): linear code defined by parity-check matrix $\mathbf H$, $\mathbf{Ht}=0$ [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch15-further]] (pp. 236, 239): includes the $(8,5)$ code hint and the detect/correct contrast of Ex. 15.16 [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch25-exact]] (pp. 324–325): a linear (N, K) code with $2^K$ codewords [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch47-low]] (p. 557): structured redundancy letting errors be corrected; here, a linear block code given by parity checks [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch48-convolutional]] (p. 581): the codes discussed here are convolutional and turbo codes, which have sparse (low-density, or generalized) parity-check matrices [as `error-correcting code`; work fields: information-theory, bayesian]
- [[mackay-2003-information/ch49-repeat]] (p. 582): structured redundancy to correct errors; here the RA code and relatives [work fields: information-theory, bayesian]
- [[mackay-2003-information/ch50-digital]] (pp. 589–590): here Reed–Solomon block codes versus fountain codes for erasures [work fields: information-theory, bayesian]
- [[pierce-1980-introduction/ch08-noisy]] (pp. 159–162): code with check digits or large distances between code blocks
- [[pierce-1980-introduction/ch14-back]] (p. 276): codes that correct $A$ errors in $B$ digits; no systematic way to find best ones yet
- [[polyanskiy-2025-information/ch19-error]] (p. 342): an M-code (f,g) built so decoding recovers W with small error
- [[polyanskiy-2025-information/ch20-random]] (pp. 350, 357): an $(M,\epsilon)$-code: codebook plus decoder with error at most $\epsilon$; "max" versions bound the worst message
- [[shannon-1948-mathematical/main-p1]] (p. 28): the 7-symbol Hamming example
- [[stone-2022-information/ch04-noisy]] (p. 102): redundancy (e.g. parity digits) that allows errors to be detected or corrected
- [[stone-2022-information/ch11-information]] (p. 218, 220): a small amount of redundancy added to compressed TV data

## Instances that use it

- [[compact-disc-error-correction]] — real application of error-correcting codes — from [[cover-2006-elements/ch01-introduction]]
- [[error-correcting-code-as-latent-variable-model]] — source bits are latent; $\mathbf G$ normally known in advance — from [[mackay-2003-information/ch34-independent]]

## Candidate bridges

- [structural-analogy] Redundant gender marking ↔ error-correcting codes: parity bits add redundancy for robustness to noise. — from [[gibson-2019-efficiency/main]] (information-theory → information-theory)
- [same-math] min–sum on a graph ↔ information-theory: decoding of error-correcting codes — the text says Chapter 25 uses min–sum for decoding. — from [[mackay-2003-information/ch16-message]] (information-theory → information-theory)
- [metaphor] encoder of a vector quantizer ↔ decoding of an error-correcting code (noted in passing, p. 285) — from [[mackay-2003-information/ch20-example]] (information-theory → unspecified)
- [structural-analogy] Redundancy removed means errors become false messages ↔ error-correcting codes: structured redundancy is added back (Pierce only says the next chapter treats noise). — from [[pierce-1980-introduction/ch07-efficient]] (information-theory → information-theory)
- [structural-analogy] linear compression $w=Hx$ with a decoder choosing the likeliest $x$ ↔ coding theory: syndrome decoding of linear error-correcting codes — the text says efficient decoders of such codes can make the decompressor practical (p. 218). — from [[polyanskiy-2025-information/ch13-fixed]] (information-theory → information-theory)
