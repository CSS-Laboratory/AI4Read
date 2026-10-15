---
id: controllability
type: concept
fields: [control-theory, bayesian]
fields_strong: [control-theory, bayesian]
n_sources: 9
n_works: 3
tiers: [core, deep]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch07-state, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch14-fundamental, astrom-2021-feedbacksystems/ch15-architecture-p2, liberzon-2012-calculus/ch04-maximum-p2, liberzon-2012-calculus/ch06-linear, sarkka-2023-bayesianfiltering/ch17-epilogue]
aliases: [controllability-reachability]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# controllability

## Aliases

Variant ids merged into this page (curated in `wiki/kg/aliases.json`):

- `controllability-reachability` — 4 digest(s)

## Canon spine entry

- **controllability (reachability)** (control-theory): whether inputs can drive the system to any state (UG)

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-6): here called *reachability*: can possible states be reached by choosing $u$; only named, treated in Chs. 7 and 8
- [[astrom-2021-feedbacksystems/ch07-state]] (p. 7-33): any state reachable from any state in finite time; tested by rank of $W_r$ (Def. 7.1, Thm 7.1; pp. 7-2, 7-4). Author prefers "reachability" to "controllability" [alias `controllability-reachability`]
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-13): here called reachability; its rank test appears in Example 9.7
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-27): lost under pole/zero cancellation [as `controllability (reachability)`; alias `controllability-reachability`]
- [[astrom-2021-feedbacksystems/ch14-fundamental]] (p. 14-2): needed for arbitrary state-feedback eigenvalues [as `controllability (reachability)`; alias `controllability-reachability`]
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-28): here: the cancelled mode $I_1-I_2$ is neither reachable from the forces nor observable from $v$
- [[liberzon-2012-calculus/ch04-maximum-p2]] (pp. 111, 118): here: some control achieves the transfer (existence) and $(A,b_i)$ controllable (normality)
- [[liberzon-2012-calculus/ch06-linear]] (p. 154): used to bound the infinite-horizon cost, so $P$ exists [alias `controllability-reachability`]
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 353): mentioned together with observability as omitted [work fields: control-theory, bayesian]

## Candidate bridges

- [structural-analogy] Lie bracket as non-commutativity of flows ↔ controllability theory: brackets generate new reachable directions. — from [[liberzon-2012-calculus/ch04-maximum-p2]] (control-theory → control-theory)
- [structural-analogy] observability/controllability omitted here ↔ control-theory observability/controllability: same questions, asked for estimation — from [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (control-theory → control-theory)
