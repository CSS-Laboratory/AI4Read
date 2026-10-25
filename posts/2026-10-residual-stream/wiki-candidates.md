---
id: 2026-10-residual-stream/wiki-candidates
type: wiki-candidates
date: 2026-10-25
status: candidates only (Kunhao's spec: "Wiki: candidate nodes and bridges"); nothing is written to wiki/ until he approves
---

# Post 03 · candidate wiki nodes and bridges

**New nodes** (after just-in-time digests of the three sources): `hidden-state`, `logit-lens`, `linear-probe`, `unembedding`, `direction`, `steering-vector`, `activation-space`. **Updates:** `residual-stream` (add Elhage 2021 and Nanda 2022 grounding; the node is grounded only in `geva-2021-ffn/main` and `kaplan-2020-scaling/main`); `privileged-basis`; `circuit` and `superposition` each need an interpretability sense apart from the electrical and the linearity/coding senses; `feature-steering` has no digest.

**Bridges, all marked `candidate`:**
- residual-stream sum ↔ `vector`, `linear-combination` [same-math]
- read ↔ `dot-inner-product`, `projection` [same-math] (pin the sense: score vs closest point)
- write ↔ vector addition [same-math]
- steering ↔ `affine-function` [same-math]
- no privileged basis ↔ `change-of-basis` [same-math]
- W9-B (read split) ↔ weighted edge in `circuit` [structural-analogy]
- stream ↔ `multiple-access-channel` [structural-analogy] (now sourced: brief unit 15, MacKay 2003 p. 237)
- "bus"/"bandwidth" ↔ Shannon–Weaver channel [metaphor]
- probe vs steer ↔ `do-operator` [structural-analogy]
- Elhage (study the writes, not the stream) versus Nanda (the stream is the central object) [contradicts, a difference of method, not of fact]
- `special-case-of`: probe ⊂ linear read; `historical-influence`: none claimed.

**Also for the graph (decided by Kunhao, 2026-10-25):** reading-path item 1b, an eigen-decomposition post between *The lens* and *Directions* (`canon/interpretability.md`).
