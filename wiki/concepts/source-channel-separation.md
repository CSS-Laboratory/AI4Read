---
id: source-channel-separation
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 5
n_works: 2
tiers: [reference, core]
grounding: digests
sources: [cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch14-network-p4, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch26-rate, polyanskiy-2025-information/ch29-evaluating]
raw_ids: [source–channel separation]
canon_spine: [information-theory]
generated_by: build_kg.py
---

# source-channel-separation

## Canon spine entry

- **source–channel separation** (information-theory): compression and transmission can be designed separately without loss, under standard conditions (grad)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch08-channel-p2]] (pp. 215, 218): two-stage design (compress, then channel-code) loses nothing for the single-user case proved here
- [[cover-2006-elements/ch14-network-p4]] (pp. 448–449): holds for one user. For a MAC it is sufficient to combine Slepian–Wolf and MAC capacity, but not necessary
- [[polyanskiy-2025-information/ch21-channel]] (p. 392): vanishing error is possible if $R<C/H$ and not if $R>C/H$ (the boundary $R=C/H$ is left open); achieved by compress-then-code [as `source–channel separation`]
- [[polyanskiy-2025-information/ch26-rate]] (p. 476): optimal lossy compressor plus optimal error-correcting code gives an optimal end-to-end scheme
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 516): compress, then channel-code; optimal for lossy JSCC under Assumption 26.1

## Candidate bridges

- [structural-analogy] Source–channel separation ↔ rational inattention: both treat information-rate limits as the binding constraint on what can be passed along. — from [[cover-2006-elements/ch08-channel-p2]] (information-theory → information-theory)
- [metaphor] Concatenation as a super-channel ↔ information-theory: source–channel separation — build blocks separately and chain them. — from [[mackay-2003-information/ch11-error]] (information-theory → information-theory)
