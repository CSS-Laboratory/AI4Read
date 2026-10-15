---
id: variety
type: concept
fields: [control-theory, information-theory]
fields_strong: [control-theory, information-theory]
n_sources: 10
n_works: 1
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch04-machine, ashby-1956-cybernetics/ch06-black, ashby-1956-cybernetics/ch07-quantity, ashby-1956-cybernetics/ch08-transmission, ashby-1956-cybernetics/ch09-incessant, ashby-1956-cybernetics/ch10-regulation, ashby-1956-cybernetics/ch11-requisite, ashby-1956-cybernetics/ch12-error, ashby-1956-cybernetics/ch13-regulating, ashby-1956-cybernetics/ch14-amplifying]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# variety

## Canon spine entry

- **variety** (control-theory): the number of distinguishable states a system can take (HS)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch04-machine]] (p. 57): the arrow in a diagram of immediate effects means variety in A shows as variety in B
- [[ashby-1956-cybernetics/ch06-black]]: not used in this unit. [weak: not really used in this unit]
- [[ashby-1956-cybernetics/ch07-quantity]] (pp. 124, 126): number of distinguishable elements of a set, or its log base 2 in bits; relative to the observer [work fields: control-theory, information-theory]
- [[ashby-1956-cybernetics/ch08-transmission]] (p. 142, 152): the diversity of a set of possibilities (from Ch. 7), here measured logarithmically; it needs reference to a set and cannot exist in one transducer at one moment [work fields: control-theory, information-theory]
- [[ashby-1956-cybernetics/ch09-incessant]] (pp. 174–175): in this chapter measured per step by entropy; maximal ($\log n$) when probabilities are equal [work fields: control-theory, information-theory]
- [[ashby-1956-cybernetics/ch10-regulation]] (p. 199): (developed in Part II; not defined on these pages) here, η has less variety than the set of all possible values of E [weak: not really used in this unit]
- [[ashby-1956-cybernetics/ch11-requisite]] (pp. 205–207): number of distinct elements in a set; used for outcomes and moves, measured as a count or logarithmically
- [[ashby-1956-cybernetics/ch12-error]] (p. 220): F must block the flow of variety from D to E
- [[ashby-1956-cybernetics/ch13-regulating]] (p. 250): number of distinguishable states or elements of a set; in vectors, $k$ within the class and at most $k^n$ for $n$ components
- [[ashby-1956-cybernetics/ch14-amplifying]] (p. 269): the number of possible states, here counted in bits; e.g. $2^{36500}$

## Instances that use it

- [[two-arm-semaphore]] — variety is 36, not 64, for a distant observer — from [[ashby-1956-cybernetics/ch07-quantity]]
- [[coin-spin-sequence-1024]] — ten two-valued components give variety 1024 — from [[ashby-1956-cybernetics/ch08-transmission]]
- [[table-11-5-1]] — no repeats in columns; variety at least 9/3 — from [[ashby-1956-cybernetics/ch11-requisite]]
- [[coin-spun-six-times]] — basic variety 2, vector variety 64 — from [[ashby-1956-cybernetics/ch13-regulating]]
- [[variety-of-opinion-and-monetary-control]] — control by money supply is more precarious where everyone tends to hold the same opinion at once (the United States, compared with England) — from [[keynes-1936-general/ch13-general]]
- [[colombian-coffee-varieties]] — adopters' income rose more and credit barriers blocked small farmers — from [[rogers-2003-diffusion/ch11-consequences-p2]]

## Candidate bridges

- [structural-analogy] constraint as reduction of variety ↔ information theory: redundancy (Ashby links them himself, p. 130) — from [[ashby-1956-cybernetics/ch07-quantity]] (control-theory → information-theory)
- [structural-analogy] decay of variety under a single-valued map ↔ dynamical systems: trajectories merging into attractors or basins — from [[ashby-1956-cybernetics/ch07-quantity]] (control-theory → complex-systems)
- [structural-analogy] one-one coding preserves variety ↔ information theory: lossless encoding preserves the number of distinguishable messages — both rest on decodability — from [[ashby-1956-cybernetics/ch08-transmission]] (control-theory → information-theory)
- [metaphor] variety cannot exist in one transducer, only across a set of them ↔ statistics: a distribution describes a population, not an individual draw — from [[ashby-1956-cybernetics/ch08-transmission]] (control-theory → other:statistics)
- [structural-analogy] Capacity must at least match source entropy rate (p. 183) ↔ control-theory: law of requisite variety (canon link; not stated in this unit). — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [structural-analogy] regulator blocks variety from D to E ↔ control-theory: disturbance rejection (the output barely reflects the disturbance) — both describe a good controller leaving the output unaffected. — from [[ashby-1956-cybernetics/ch10-regulation]] (control-theory → control-theory)
- [structural-analogy] Law of requisite variety ↔ control-theory: a controller needs enough distinct responses to cover the distinct disturbances it must absorb — echoes "only variety in the regulator can absorb variety". — from [[ashby-1956-cybernetics/ch11-requisite]] (control-theory → control-theory)
- [structural-analogy] Variety of opinion stabilises, unanimity makes mass movement ↔ agent-based modeling: diversity of agents damps aggregate swings. — from [[keynes-1936-general/ch13-general]] (economics-finance → complex-systems)
- [metaphor] Self-organization and diversity as raw material ↔ control theory: variety in the regulator (requisite variety) — both stress variety, but the text does not make this link. — from [[meadows-2008-thinking/ch06-leverage]] (control-theory → control-theory)
- [structural-analogy] Pierce's "language that the listener knows" ↔ uniform information density / efficient communication: an audience can take in only a small variety rate, so signals are paced and predictable. — from [[pierce-1980-introduction/ch13-information]] (information-theory → communication-theory)
- [structural-analogy] Classifier-free guidance ↔ GAN truncation: both trade variety for typicality (the text says "somewhat analogous", p. 367). — from [[prince-2023-udl/ch18-diffusion]] (llm → other:gan-truncation)
- [structural-analogy] redundant dimension as a "noise buffer" ↔ requisite variety: spare dimensions give the regulator room to absorb disturbance — only a loose parallel — from [[todorov-2002-ofc/main]] (control-theory → other:requisite-variety)
