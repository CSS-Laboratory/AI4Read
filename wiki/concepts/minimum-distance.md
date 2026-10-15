---
id: minimum-distance
type: concept
fields: [information-theory, bayesian, linear-algebra]
fields_strong: [information-theory, bayesian, linear-algebra]
n_sources: 3
n_works: 3
tiers: [core, deep]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p2, mackay-2003-information/ch13-binary, spielman-2025-sagt/ch28-brief]
generated_by: build_kg.py
---

# minimum-distance

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p2]] (p. 211): least number of places two codewords differ; equals minimum weight for a linear code [new]
- [[mackay-2003-information/ch13-binary]] (p. 206): smallest separation between two codewords; a code corrects $\lfloor(d-1)/2\rfloor$ errors [new; work fields: information-theory, bayesian]

### linear-algebra

- [[spielman-2025-sagt/ch28-brief]] (pp. 231–232): smallest distance between distinct codewords; for linear codes, the smallest nonzero weight [new]

## Instances that use it

- [[hamming-7-4-code]] — 16 codewords, minimum distance 3, single-error correction using $H\mathbf r$ — from [[cover-2006-elements/ch08-channel-p2]]
- [[berlekamps-bats]] — picture of when minimum distance matters — from [[mackay-2003-information/ch13-binary]]
- [[hamming-voronoi-decoding]] — minimum-distance decoding on the BSC — from [[polyanskiy-2025-information/ch19-error]]
