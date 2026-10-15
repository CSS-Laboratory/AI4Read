---
id: block-coding
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 2
n_works: 1
tiers: [core]
grounding: digests
sources: [pierce-1980-introduction/ch04-encoding, pierce-1980-introduction/ch05-entropy]
generated_by: build_kg.py
---

# block-coding

## Definitions in the sources

### information-theory

- [[pierce-1980-introduction/ch04-encoding]] (pp. 74–75, 77): encoding groups of 2, 3 or more characters together to reduce wasted patterns [new]
- [[pierce-1980-introduction/ch05-entropy]] (pp. 90, 96–97): coding long blocks as single symbols to approach entropy [new]

## Instances that use it

- [[repeat-three-source]] — random digit repeated three times; entropy ⅓ bit per character, so mechanical block coding is unnecessary — from [[pierce-1980-introduction/ch07-efficient]]

## Candidate bridges

- [structural-analogy] Block coding saving ↔ information-theory: typical set / source coding theorem — long blocks let the code use only the likely sequences. — from [[pierce-1980-introduction/ch04-encoding]] (information-theory → information-theory)
- [structural-analogy] Block coding with noise-like waveforms ↔ information-theory: source–channel coding theorems, where long blocks are needed to approach limits. — from [[pierce-1980-introduction/ch09-many]] (information-theory → information-theory)
