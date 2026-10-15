---
id: data-processing-inequality
type: concept
fields: [information-theory, bayesian]
n_sources: 30
tiers: [reference, core]
grounding: digests
sources: [cover-2006-elements/ch02-entropy, cover-2006-elements/ch08-channel-p2, cover-2006-elements/ch12-information-p2, cover-2006-elements/ch14-network-p2, cover-2006-elements/ch14-network-p3, mackay-2003-information/ch08-dependent, mackay-2003-information/ch10-noisy, murphy-2023-pml2/ch05-information-p1, murphy-2023-pml2/ch05-information-p2, polyanskiy-2025-information/ch01-introduction, polyanskiy-2025-information/ch03-divergence, polyanskiy-2025-information/ch04-mutual, polyanskiy-2025-information/ch05-variational, polyanskiy-2025-information/ch06-extremization, polyanskiy-2025-information/ch08-f-p1, polyanskiy-2025-information/ch10-random, polyanskiy-2025-information/ch16-neyman, polyanskiy-2025-information/ch17-information, polyanskiy-2025-information/ch18-hypothesis, polyanskiy-2025-information/ch19-error, polyanskiy-2025-information/ch21-channel, polyanskiy-2025-information/ch23-capacity, polyanskiy-2025-information/ch24-strong, polyanskiy-2025-information/ch25-channel, polyanskiy-2025-information/ch29-evaluating, polyanskiy-2025-information/ch32-classical, polyanskiy-2025-information/ch33-mutual, polyanskiy-2025-information/ch36-strong-p1, polyanskiy-2025-information/ch36-strong-p2, shannon-1948-mathematical/main-p2]
raw_ids: [data processing inequality]
canon_spine: information-theory
generated_by: build_kg.py
---

# data-processing-inequality

## Canon spine entry

- **data processing inequality** (information-theory): no processing of Y can increase its information about X (UG)

## Definitions in the sources

### information-theory

- [[cover-2006-elements/ch02-entropy]] (p. 32): $X\to Y\to Z\Rightarrow I(X;Y)\ge I(X;Z)$
- [[cover-2006-elements/ch08-channel-p2]] (pp. 204, 218): used for $W\to X^n\to Y^n$ and $V^n\to X^n\to Y^n\to\hat V^n$
- [[cover-2006-elements/ch12-information-p2]] (p. 300): quantising a distribution cannot increase relative entropy
- [[cover-2006-elements/ch14-network-p2]] (p. 400): step (b) of the converse
- [[cover-2006-elements/ch14-network-p3]] (p. 424): gives $I(U;Y_1)\ge I(U;Y_2)$ for degraded channels
- [[mackay-2003-information/ch08-dependent]] (pp. 141, 144): on a Markov chain $w\to d\to r$, $I(W;R)\le I(W;D)$
- [[mackay-2003-information/ch10-noisy]] (p. 168): $I(s;\hat s)\le I(\mathbf x;\mathbf y)\le NC$ along $s\to\mathbf x\to\mathbf y\to\hat s$
- [[polyanskiy-2025-information/ch01-introduction]] (pp. xix, xxii): used for estimation lower bounds (Ch. 29); strong version in Ch. 33
- [[polyanskiy-2025-information/ch03-divergence]] (p. 35): same channel applied to $P_X,Q_X$ cannot increase $D$; equality iff $D(P_{X|Y}\|Q_{X|Y}|P_Y)=0$ [as `data processing inequality`]
- [[polyanskiy-2025-information/ch04-mutual]] (p. 52): $I(X;Z)\le I(X;Y)$ for X→Y→Z; equality iff X→Z→Y [as `data processing inequality`]
- [[polyanskiy-2025-information/ch05-variational]] (p. 71): used to show partition divergences lower-bound D
- [[polyanskiy-2025-information/ch06-extremization]] (p. 91): used to prove convexity of $D$
- [[polyanskiy-2025-information/ch08-f-p1]] (p. 120): passing both laws through one channel cannot increase any $D_f$
- [[polyanskiy-2025-information/ch10-random]] (p. 167): used for the converse, since extractors are deterministic functions
- [[polyanskiy-2025-information/ch16-neyman]] (p. 282): gives the weak converse $d(\alpha\|\beta)\le D(P\|Q)$ [as `data processing inequality`]
- [[polyanskiy-2025-information/ch17-information]] (p. 300): used to lower-bound P[Eₙ] via binary divergence
- [[polyanskiy-2025-information/ch18-hypothesis]] (p. 323, 326): used in the SPRT converse and for F_I(t) ≤ t
- [[polyanskiy-2025-information/ch19-error]] (p. 348): used for divergence in the converse proof
- [[polyanskiy-2025-information/ch21-channel]] (p. 393): used for $I(S^k;\hat S^k)\le I(X^n;Y^n)$ [as `data processing inequality`]
- [[polyanskiy-2025-information/ch23-capacity]] (pp. 411, 415): used for divergence and mutual information in the converses
- [[polyanskiy-2025-information/ch24-strong]] (p. 426): used in the weak converse; contrasted with the hypothesis-testing approach
- [[polyanskiy-2025-information/ch25-channel]] (pp. 446–447): applied to (23.3), (23.4) and to divergences
- [[polyanskiy-2025-information/ch29-evaluating]] (p. 516): step (b) in the JSCC converse
- [[polyanskiy-2025-information/ch32-classical]] (pp. 576–577): processing $X$ into $\hat\theta$ cannot raise $\chi^2$ divergence; the engine of the HCR/CR derivations and the heuristic route to BCR
- [[polyanskiy-2025-information/ch33-mutual]] (p. 585): applied to $\theta\to X\to\hat\theta$ [as `data processing inequality`]
- [[polyanskiy-2025-information/ch36-strong-p1]] (p. 626): $I(U;Y)\le I(U;X)$ along Markov chains; the SDPI strengthens it
- [[polyanskiy-2025-information/ch36-strong-p2]] (pp. 654, 658): used for $\eta^{(p)}\le1$ and (33.32)
- [[shannon-1948-mathematical/main-p2]] (p. 54): $R(x,v)\le R(x,y)$ for any operation on $y$

### bayesian

- [[murphy-2023-pml2/ch05-information-p1]] (p. 229): a channel cannot increase KL between two distributions [new]
- [[murphy-2023-pml2/ch05-information-p2]] (p. 239): post-processing along a Markov chain $X\to Y\to Z$ cannot increase MI about $X$ [new]

## Candidate bridges

- [same-math] Sufficient statistic ↔ statistics: equality condition of the data processing inequality $I(\theta;T(X))=I(\theta;X)$ is the sufficiency condition (p. 37). — from [[cover-2006-elements/ch02-entropy]] (information-theory → other)
- [metaphor] Systematic error not shrinking with repetition ↔ information-theory: Data processing inequality — more copies of corrupted data add no new information. — from [[jaynes-2003-probability/ch10-physics]] (information-theory → information-theory)
- [structural-analogy] 10-year averaging as irreversible information loss ↔ information-theory: data-processing inequality — canon link; not stated in this unit. — from [[jaynes-2003-probability/ch17-principles-p1]] (information-theory → information-theory)
- [structural-analogy] Data-processing inequality ↔ bayesian: posterior inference from a statistic $r(d)$ cannot be more informative about $w$ than from full data $d$ — same Markov structure. — from [[mackay-2003-information/ch08-dependent]] (information-theory → bayesian)
- [structural-analogy] Information monotonicity under coarse-graining ↔ information-theory: data processing inequality — both say processing cannot raise divergence, but the source treats only bin merging — from [[nielsen-2020-elementary/main-p1]] (information-theory → information-theory)
- [same-math] Appendix 7: $R(x,v)\le R(x,y)$ ↔ data processing inequality. — from [[shannon-1948-mathematical/main-p2]] (information-theory → unspecified)
