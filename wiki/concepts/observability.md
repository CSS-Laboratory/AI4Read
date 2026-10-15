---
id: observability
type: concept
fields: [control-theory, bayesian, communication-theory]
fields_strong: [control-theory, bayesian, communication-theory]
n_sources: 10
n_works: 6
tiers: [core, deep]
grounding: digests
sources: [ashby-1956-cybernetics/ch06-black, astrom-2021-feedbacksystems/ch03-system-p1, astrom-2021-feedbacksystems/ch08-output, astrom-2021-feedbacksystems/ch09-transfer-p1, astrom-2021-feedbacksystems/ch09-transfer-p2, astrom-2021-feedbacksystems/ch15-architecture-p2, liberzon-2012-calculus/ch06-linear, rogers-2003-diffusion/ch06-attributes-p2, sarkka-2023-bayesianfiltering/ch17-epilogue, welch-2004-kalmanintro/main]
canon_spine: [control-theory]
generated_by: build_kg.py
---

# observability

## Canon spine entry

- **observability** (control-theory): whether outputs reveal the entire internal state (UG)

## Definitions in the sources

### control-theory

- [[ashby-1956-cybernetics/ch06-black]] (p. 114): Ashby's partial observability: only some variables visible; here an observer-relative idea
- [[astrom-2021-feedbacksystems/ch03-system-p1]] (p. 3-6): whether $y$ contains enough information to reconstruct the state; only named
- [[astrom-2021-feedbacksystems/ch08-output]] (p. 8-2, 8-3): the state can be determined from $y,u$ on $[0,T]$ for every $T>0$; for linear systems, $W_o$ has full row rank (p. 8-2, 8-3) (new)
- [[astrom-2021-feedbacksystems/ch09-transfer-p1]] (p. 9-13): with reachability determines the part $\Sigma_{ro}$ that $G$ represents
- [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (p. 9-27): lost under pole/zero cancellation
- [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (p. 15-28): here: the cancelled mode $I_1-I_2$ is neither reachable from the forces nor observable from $v$
- [[liberzon-2012-calculus/ch06-linear]] (p. 157): of $(A,C)$ with $Q=C^TC$; gives stability and $P>0$
- [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (p. 353): whether the state can be determined from measurements; mentioned as omitted [work fields: control-theory, bayesian]
- [[welch-2004-kalmanintro/main]] (p. 11): if over all measurements there is not a one-to-one mapping between measurement and state via $h$, the filter will quickly diverge ("as you might expect") and the process is "unobservable"

### communication-theory

- [[rogers-2003-diffusion/ch06-attributes-p2]] (pdf 330): visibility of results to others [new]

## Instances that use it

- [[calculator-tape-memory]] — memory as relation to observability — from [[ashby-1956-cybernetics/ch06-black]]
- [[dog-memory]] — memory as relation to observability — from [[ashby-1956-cybernetics/ch06-black]]
- [[observability-ladder]] — tree, telescope, microscope, X-ray, MRI, electron microscope as a continuum — from [[godfreysmith-2003-theory/ch12-scientific]]
- [[n-trak-soil-test]] — failure explained by low relative advantage, incompatibility and low observability — from [[rogers-2003-diffusion/ch06-attributes-p1]]

## Candidate bridges

- [structural-analogy] "Memory is a hypothesis forced by limited observation" (p. 172) ↔ control-theory: observability, where hidden state is inferred from a sequence of outputs. Ashby himself links this to S.6/21. — from [[ashby-1956-cybernetics/ch09-incessant]] (control-theory → control-theory)
- [structural-analogy] Hidden cancelled mode ↔ observability/reachability: an unobservable or unreachable mode does not show in the transfer function. — from [[astrom-2021-feedbacksystems/ch09-transfer-p2]] (control-theory → control-theory)
- [metaphor] Blind men touching parts ↔ control-theory: observability — partial measurements may not reveal the whole internal state. — from [[meadows-2008-thinking/ch00-introduction]] (control-theory → control-theory)
- [structural-analogy] observability/controllability omitted here ↔ control-theory observability/controllability: same questions, asked for estimation — from [[sarkka-2023-bayesianfiltering/ch17-epilogue]] (control-theory → control-theory)
- [structural-analogy] BE unlearnable from feature vectors ↔ control-theory/observability: different internal systems giving identical outputs cannot be told apart from data — from [[sutton-2018-rl/ch11-off]] (control-theory → control-theory)
- [structural-analogy] Stacking the four latest frames to handle states not fully observable from one image ↔ control-theory: observability and state estimation — use history to recover hidden state (p. 438). — from [[sutton-2018-rl/ch16-applications]] (control-theory → control-theory)
