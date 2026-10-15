---
id: metric-entropy
type: concept
fields: [information-theory]
fields_strong: [information-theory]
n_sources: 3
n_works: 1
tiers: [reference]
grounding: digests
sources: [polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch26-rate, polyanskiy-2025-information/ch30-metric]
generated_by: build_kg.py
---

# metric-entropy

## Definitions in the sources

### information-theory

- [[polyanskiy-2025-information/ch01-introduction]] (pp. xviii, xix, xxii): Kolmogorov's notion, used in learning and in statistical upper bounds [new]
- [[polyanskiy-2025-information/ch26-rate]] (p. 476): Kolmogorov's non-probabilistic quantization theory for sets in metric spaces [new]
- [[polyanskiy-2025-information/ch30-metric]] (p. 523): log N or log M; called ε-capacity and ε-entropy in Kolmogorov–Tikhomirov [new]

## Instances that use it

- [[hilbert-13th-problem]] — resolved using metric entropy — from [[polyanskiy-2025-information/ch01-introduction]]

## Candidate bridges

- [structural-analogy] metric entropy ↔ statistical learning: entropic upper and lower bounds for estimation — the text says metric entropy has far-reaching consequences for statistical learning, e.g. entropic bounds for estimation (p. 476) — from [[polyanskiy-2025-information/ch26-rate]] (information-theory → llm)
- [structural-analogy] rate-distortion for the worst-case distribution ↔ minimax thinking: metric entropy as the hardest-distribution case (p. 476) — from [[polyanskiy-2025-information/ch26-rate]] (information-theory → other:minimax-thinking)
- [structural-analogy] Metric entropy $\log N(\epsilon)$ ↔ rate–distortion: Thm 27.16 compares worst-case rate–distortion at distortion cε (plus $\log2$, factor $1/(1-2c)$) with $\log N$; it is a comparison, not an equality. — from [[polyanskiy-2025-information/ch30-metric]] (information-theory → information-theory)
- [structural-analogy] Volume bound for metric entropy ↔ SLB for rate-distortion (Remark 30.2) — from [[polyanskiy-2025-information/ch33-mutual]] (information-theory → unspecified)
