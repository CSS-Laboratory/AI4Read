---
id: transformation
type: concept
fields: [analytic-philosophy, control-theory]
fields_strong: [analytic-philosophy, control-theory]
n_sources: 2
n_works: 2
tiers: [core]
grounding: digests
sources: [ashby-1956-cybernetics/ch02-change, lycan-2019-language/ch09-truth]
generated_by: build_kg.py
---

# transformation

## Definitions in the sources

### analytic-philosophy

- [[lycan-2019-language/ch09-truth]] (p. 121): Chomskyan rule turning one phrase marker into another [new]

### control-theory

- [[ashby-1956-cybernetics/ch02-change]] (p. 10): a set of transitions on a set of operands, defined by what each becomes, not why [new]

## Instances that use it

- [[alphabet-shift-code]] — the letter-to-next-letter transformation: closed, with its square — from [[ashby-1956-cybernetics/ch02-change]]
- [[sunshine-transformations]] — pale skin, cold soil and photographic plate under one operator — from [[ashby-1956-cybernetics/ch02-change]]
- [[clock-transformation]] — $n'=n+k$; the operator is vague but the transformation is well defined — from [[ashby-1956-cybernetics/ch03-determinate]]
- [[two-coin-vector]] — the transformations $N$ and $M$ on four vector states — from [[ashby-1956-cybernetics/ch03-determinate]]
- [[nonclosed-transformation-example]] — $T^6(a)$ undefined — from [[ashby-1956-cybernetics/ch03-determinate]]
- [[coin-walk-x-plus-a]] — simplest stochastic transformation, with its set of trajectories — from [[ashby-1956-cybernetics/ch09-incessant]]
- [[unbounded-allocation-process]] — state $(x,z)$, decision $y$, transformation $ay+b(x-y)$ — from [[bellman-1957-dp/ch03-iii]]
- [[skinner-chomsky-switch]] — shift of worlds as repair/transformation of reality — from [[carey-1989-cultural/ch01-cultural]]
- [[eight-schools-hmc]] — HMC tuning on the educational-testing model, with a log τ transformation — from [[gelman-2013-bda3/ch12-computationally]]
- [[add-1-add-3-task]] — paced digit transformation that drives effort to its limit — from [[kahneman-2011-thinking/ch02-attention]]
- [[house-transformations]] — AH draws images of a house under 2×2 matrices — from [[strang-2023-introduction/ch08-linear]]

## Candidate bridges

- [structural-analogy] Repeated transformation and trajectory on the kinematic graph ↔ control-theory: state evolution of a discrete-time system, with the initial state set and then left to run without input (the text calls the correspondence "analogous"). — from [[ashby-1956-cybernetics/ch02-change]] (control-theory → control-theory)
- [same-math] Kinematic graph of a single-valued transformation ↔ graph theory: the directed graph of a function on a finite set, where each point has one outgoing arrow. — from [[ashby-1956-cybernetics/ch02-change]] (control-theory → other:graph-theory)
- [structural-analogy] shrinking transformation and $\sum w(k^nc)<\infty$ ↔ control-theory: discounting that makes value iteration converge — both make late stages matter less. — from [[bellman-1957-dp/ch10-x]] (control-theory → control-theory)
- [same-math] Mass matrix $M^{-1}$ = target covariance ↔ bayesian: preconditioning/reparameterization of $q$ by $\sqrt M q$ (the unit gives the transformation). — from [[betancourt-2017-hmc/main-p2]] (bayesian → bayesian)
- [structural-analogy] Determining $f$ from $f(e_i)$ ↔ matrix as transformation: columns of $A$ are the images of the basis vectors (the scalar case is a single row). — from [[boyd-2018-vmls/ch02-linear]] (linear-algebra → linear-algebra)
- [same-math] linear function determined by $f(e_k)$ ↔ linear-algebra: matrix as transformation (columns are images of basis vectors) — same statement. — from [[boyd-2018-vmls/ch08-linear]] (linear-algebra → linear-algebra)
- [same-math] Inverse-CDF sampling (D.3) ↔ simulation of any 1-D random variable — the same transformation. — from [[clauset-2009-powerlaw/main-p2]] (complex-systems → unspecified)
- [same-math] Cholesky sampling of a Gaussian with covariance $\Sigma=LL^\top$ ↔ probability (Chapter 6): linear transformation of random variables (as sketched on p. 115). — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → other:probability)
- [same-math] Weighted regression with $\Sigma_{ii}=\sigma^2/w_i$ ↔ generalized least squares: $\Sigma_y^{-1/2}$ transformation gives (14.12)–(14.13). — from [[gelman-2013-bda3/ch14-introduction]] (bayesian → linear-algebra)
- [same-math] logit scale $u=\log[p/(1-p)]$ (A.3) ↔ bayesian: log-odds — the same transformation, under which the sum rule becomes $u(A)+u(\bar A)=0$. — from [[jaynes-2003-probability/appa-other]] (bayesian → bayesian)
- [structural-analogy] MPG vs gallons-per-mile ↔ nonlinear transformations: the reciprocal scale changes which differences look large (12→14 mpg saves more than 30→40). — from [[kahneman-2011-thinking/ch34-frames]] (decision-game-theory → other:nonlinear-transformations)
- [structural-analogy] Individual liquidity vs community illiquidity ↔ maturity/liquidity transformation: short claims on long assets work until everyone withdraws. — from [[keynes-1936-general/ch12-state]] (economics-finance → economics-finance)
- [metaphor] ICA as information maximization ↔ information-theory: choosing a transformation to maximize output information — from [[mackay-2003-information/ch34-independent]] (information-theory → information-theory)
- [structural-analogy] Logit and log links ↔ transformations in regression more generally: mapping a bounded parameter onto the whole real line. — from [[mcelreath-2020-rethinking/ch09-big]] (bayesian → other:statistics)
- [same-math] Flow density via change of variables ↔ probability: transformation of random variables — the same formula with the Jacobian determinant. — from [[murphy-2023-pml2/ch23-normalizing]] (bayesian → other:probability)
- [structural-analogy] Ordinal payoffs (any increasing transformation) ↔ order-invariant statistics, e.g. rank-based methods — only order matters. — from [[osborne-2004-introduction/ch01-introduction]] (decision-game-theory → unspecified)
- [structural-analogy] Transformation costs rising with number of decision makers and inclusive aggregation rules (pp. 198, 201) ↔ political-science: veto player — more required consenters make change harder. — from [[ostrom-1990-commons/ch06-framework]] (political-science → political-science)
- [structural-analogy] MI's invariance under invertible transformations ↔ statistics: association measures such as correlation, which the author says lack this claim (p. 151). — from [[stone-2022-information/ch06-mutual]] (information-theory → other:statistics)
- [same-math] cdf encoder $g^*(s)=\int p_s$ giving uniform output ↔ statistics: probability integral transform / histogram equalisation — the same transformation of a variable into a uniform one. — from [[stone-2022-information/ch11-information]] (information-theory → other:statistics)
- [metaphor] "leaky bucket" account ↔ economics-finance: maturity/liquidity transformation — both involve money more or less accessible than it appears. — from [[thaler-2015-misbehaving/ch09-buckets]] (economics-finance → economics-finance)
