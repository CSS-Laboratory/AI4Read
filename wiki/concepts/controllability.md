---
id: controllability
type: concept
fields: [control-theory]
n_sources: 5
tiers: [core, deep]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch15-architecture-p2, liberzon-2012-calculus/ch04-maximum-p2, sarkka-2023-bayesianfiltering/ch17-epilogue]
generated_by: build_kg.py
---

# controllability

## Definitions in the sources

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-6): here called *reachability*: can possible states be reached by choosing $u$; only named, treated in Chs. 7 and 8
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-13): here called reachability; its rank test appears in Example 9.7
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-28): here: the cancelled mode $I_1-I_2$ is neither reachable from the forces nor observable from $v$
- [[liberzon-2012-calculus/ch04-maximum-p2]] (pp. 111, 118): here: some control achieves the transfer (existence) and $(A,b_i)$ controllable (normality)
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 353): mentioned together with observability as omitted

## Candidate bridges

- [structural-analogy] Lie bracket as non-commutativity of flows ↔ controllability theory: brackets generate new reachable directions. — from [[liberzon-2012-calculus/ch04-maximum-p2]] (control-theory → control-theory)
- [structural-analogy] observability/controllability omitted here ↔ control-theory observability/controllability: same questions, asked for estimation — from [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (control-theory → control-theory)
