---
id: dimension
type: concept
fields: [linear-algebra]
fields_strong: [linear-algebra]
n_sources: 10
n_works: 5
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch02-finite, axler-2024-ladr/ch03-linear-p1, axler-2024-ladr/ch03-linear-p2, axler-2024-ladr/ch04-polynomials, boyd-2018-vmls/ch05-linear, bryan-2006-eigenvector/main, deisenroth-2020-mml/ch02-linear-p2, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch03-four-p2, strang-2023-introduction/ch03-four-p3]
canon_spine: [linear-algebra]
generated_by: build_kg.py
---

# dimension

## Canon spine entry

- **dimension** (linear-algebra): the number of vectors in any basis; degrees of freedom (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch02-finite]] (p. 44): the length of any basis; well defined by 2.34
- [[axler-2024-ladr/ch03-linear-p1]] (p. 54, 62–63): used throughout the proofs
- [[axler-2024-ladr/ch03-linear-p2]] (p. 86): the single number that decides whether two finite-dimensional spaces over F are isomorphic
- [[axler-2024-ladr/ch04-polynomials]] (p. 123): dim 𝒫_n(F) = n + 1
- [[boyd-2018-vmls/ch05-linear]] (p. 91): only hinted: the independence-dimension inequality ($k\le n$); no general definition given
- [[bryan-2006-eigenvector/main]] (p. 4): $\dim V_1\ge r$ for $r$ disconnected subwebs
- [[deisenroth-2020-mml/ch02-linear-p2]] (pp. 45–46): number of basis vectors. Not necessarily the number of entries in a vector
- [[strang-2023-introduction/ch01-vectors]] (p. 33): only previewed here: the r columns of C are a basis, dimension r; defined in Section 3.4
- [[strang-2023-introduction/ch03-four-p2]] (p. 120): number of vectors in every basis
- [[strang-2023-introduction/ch03-four-p3]] (p. 129): number of vectors in any basis of a subspace

## Instances that use it

- [[example-r2-vs-c-dimension]] — $\mathbf R^2$ has dimension 2 over $\mathbf R$ but $\mathbf C$ has dimension 1 over $\mathbf C$ — from [[axler-2024-ladr/ch02-finite]]
- [[two-stage-stochastic-programming]] — DP over scenarios equals a nonlinear program of dimension $d(1+m)$ — from [[bertsekas-2026-rlcourse/ch02-approximation-p5]]
- [[rwm-high-dimension-failure]] — large proposals rejected, small proposals slow — from [[betancourt-2017-hmc/main-p1]]
- [[flatland-two-dimensions]] — von Neumann's and Conway's two-dimensional universal machines show that fewer dimensions cost speed, not possibility — from [[dennett-1987-intentional-stance/ch09-fast]]
- [[antipodal-pair]] — two features in one dimension with $D=½$ — from [[elhage-2022-superposition/main-p1]]
- [[sphere-shell-high-dimension]] — volume concentrates near the surface — from [[mackay-2003-information/ch02-probability]]
- [[gaussian-thin-shell]] — in $N$ dimensions, shell radius $\sqrt N\sigma$ and thickness $\sigma/\sqrt2$ — from [[mackay-2003-information/ch06-stream]]
- [[koch-curve]] — fractal built by a rule; dimension about 1.26 — from [[mitchell-2009-guidedtour/ch07-defining]]
- [[koch-curve]] — fractal dimension 1.26 from $3^d=4$ — from [[mitchell-2009-guidedtour/ch17-mystery]]
- [[gaussian-rejection-dimension-curse]] — acceptance $1/C=(\sigma_p/\sigma_q)^D$ — from [[murphy-2023-pml2/ch11-monte]]
- [[mfa-ard-dimension-recovery]] — ARD recovers six subspaces of dimension 1,2,2,3,4,7 as sample size grows — from [[murphy-2023-pml2/ch28-latent-p1]]
- [[curve-dimensions]] — circle 3, parabola 4, ellipse 5, with reductions by points — from [[popper-1959-logic/ch06-degrees]]
- [[total-correlation-vae-chairs]] — latent dimensions for rotation, size, legs — from [[prince-2023-udl/ch17-variational]]
- [[trivial-lqr-random-search-variance]] — $R(u)=\|u\|^2$ with Gaussian sampling shows dimension scaling of the gradient norm — from [[recht-2019-tour/main]]
- [[divide-the-dollars]] — a three-player division needs two dimensions — from [[shepsle-2010-analyzing/ch05-spatial-p1]]
- [[figure-515-dimension-by-dimension-median]] — outcome $(x_c^1, x_a^2)$ — from [[shepsle-2010-analyzing/ch05-spatial-p2]]
- [[matrix-space-2x2]] — 2 by 2 matrices form a space of dimension 4 — from [[strang-2023-introduction/ch03-four-p2]]
- [[solution-space-y-double-prime-minus-y]] — basis $\sin x,\cos x$; dimension 2 — from [[strang-2023-introduction/ch03-four-p2]]
- [[incidence-matrix-5-edges-4-nodes]] — Figure 3.4 graph; dimensions 1, 3, 3, 2; loops and trees — from [[strang-2023-introduction/ch03-four-p3]]
- [[middle-thirds-cantor-set]] — measure zero, uncountable, dimension $\ln2/\ln3$ — from [[strogatz-2024-nonlinear/ch11-fractals]]
- [[von-koch-curve]] — infinite length, similarity dimension $\ln4/\ln3$ — from [[strogatz-2024-nonlinear/ch11-fractals]]
- [[even-fifths-cantor-set]] — dimension $\ln3/\ln5$ — from [[strogatz-2024-nonlinear/ch11-fractals]]
- [[random-square-removal-fractal]] — not self-similar; box dimension $\ln8/\ln3$ — from [[strogatz-2024-nonlinear/ch11-fractals]]
- [[lorenz-attractor]] — correlation dimension about 2.05 — from [[strogatz-2024-nonlinear/ch11-fractals]]
- [[tile-coding-98-tilings]] — Exercise 9.5 setup, 98 tilings in 7 dimensions — from [[sutton-2018-rl/ch09-policy-p2]]
- [[schematic-cube-and-step]] — aspects alternating in three dimensions; disruption of a demonstration — from [[wittgenstein-1953-investigations/ch09-ppf]]

## Candidate bridges

- [structural-analogy] five representatives chosen by stepwise regression ↔ statistics: feature selection to reduce dimension — a few predictors summarize many opponents. — from [[axelrod-1984-cooperation/appa-tournament]] (decision-game-theory → other:statistics)
- [metaphor] Gaussian elimination ↔ dimension counting — the author offers the abstract proof as a cleaner alternative to elimination (p. 65). — from [[axler-2024-ladr/ch03-linear-p1]] (linear-algebra → unspecified)
- [same-math] 3.78 dim range T = column rank ↔ linear-algebra spine: rank as dimension of column space — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] 3.70 (dimension classifies vector spaces) ↔ other fields: classification of structures up to isomorphism by one invariant; the author notes this is hard for groups or topological spaces (p. 86) — from [[axler-2024-ladr/ch03-linear-p2]] (linear-algebra → other:other-fields)
- [same-math] Eq. (35) with no mutation ↔ evolutionary game theory/ecology: replicator equations, said in the text to be equivalent to Lotka–Volterra in $M-1$ dimensions. — from [[castellano-2009-socialdynamics/main-p2]] (complex-systems → decision-game-theory)
- [structural-analogy] Weights $w_i$ over considerations ↔ spatial model of voting: voter salience on policy dimensions (p. 105 cites Enelow & Hinich) — both let importance vary across dimensions. — from [[chong-2007-framing/main]] (political-science → political-science)
- [same-math] Median voter theorem (committee voting) ↔ political-science canon, spatial model of voting: Box 11.1 uses the same single-peaked, one-dimension logic for party convergence. — from [[clark-2017-principles/ch11-problems-p1]] (political-science → political-science)
- [structural-analogy] majoritarian vs consensus visions ↔ political-science: Lijphart-style two-dimensional classification of democracies — the chapter adopts his executive-parties and federal-unitary dimensions. — from [[clark-2017-principles/ch16-consequences-p1]] (political-science → political-science)
- [structural-analogy] Constraint matrix suitable for factor analysis ↔ psychometrics/latent-variable modelling: an organizing dimension shows up as shared correlation — the author himself links the two (p. 32) — from [[converse-1964-beliefsystems/ch02-sections]] (political-science → other:statistics)
- [structural-analogy] channel codewords ↔ sphere packing in high dimension (p. 9) — from [[cover-2006-elements/ch01-introduction]] (information-theory → unspecified)
- [structural-analogy] Chain rule as product of Jacobians ↔ matrix multiplication as composition: neighbouring dimensions must match (p. 148). — from [[deisenroth-2020-mml/ch05-vector]] (linear-algebra → linear-algebra)
- [structural-analogy] Dual SVM in $N$ variables from inner products only ↔ PCA/dual view (Ch. 10, mentioned on p. 383) — both work with data via the table of inner products, not the feature dimension. — from [[deisenroth-2020-mml/ch12-classification]] (linear-algebra → unspecified)
- [structural-analogy] Antipodal two-feature code in one dimension ↔ sparse recovery: a sparse input is recovered after a nonlinear filter. — from [[elhage-2022-superposition/main-p1]] (llm → other:sparse-recovery)
- [structural-analogy] Pairwise comparisons recovering a latent dimension ↔ psychometric scaling (Thurstone, p. 314). — from [[grimmer-2022-textasdata/ch18-coding]] (political-science → unspecified)
- [metaphor] Discovering latent treatments ↔ political-science measurement: first discover the dimensions, then test their effects (pp. 439, 443). — from [[grimmer-2022-textasdata/ch26-text]] (political-science → political-science)
- [structural-analogy] Credible interval vs confidence interval in Fine Point 11.2 ↔ bayesian: credible intervals (probability as degree of belief) vs confidence intervals (probability as frequency). The definitions of probability differ, and coverage can differ in high dimensions. — from [[hernan-2020-whatif/ch11-model]] (bayesian → bayesian)
- [metaphor] Mental shotgun ↔ interference effects in cognitive tasks: an irrelevant dimension slows a main task. — from [[kahneman-2011-thinking/ch08-judgments]] (decision-game-theory → other:interference-effects-in-cognitive)
- [structural-analogy] Sphere overlap "not disastrous" in high dimensions ↔ typical set: probability sits in tiny-volume regions, not where volume intuition suggests. — from [[mackay-2003-information/ch13-binary]] (information-theory → information-theory)
- [structural-analogy] counting labellings realizable by a model class (VC dimension) ↔ bayesian: how many datasets a model can fit, as in the marginal likelihood — both measure the flexibility of a model class. — from [[mackay-2003-information/ch40-capacity]] (information-theory → bayesian)
- [structural-analogy] Pooling across intercepts and slopes via correlation ↔ regression toward the mean in two dimensions — from [[mcelreath-2020-rethinking/ch13-adventures]] (bayesian → unspecified)
- [same-math] Fractal dimension $x^d=N$ ↔ power laws (ch. 15): the same power-law relation, with the dimension as exponent (p. 137). — from [[mitchell-2009-guidedtour/ch17-mystery]] (complex-systems → complex-systems)
- [structural-analogy] Adversarial examples via $\|\delta\|\approx\sigma\sqrt d$ ↔ Typical set: in high dimensions mass sits in a thin shell far from the center, so ordinary and worst-case distances differ greatly. — from [[murphy-2023-pml2/ch19-beyond]] (bayesian → information-theory)
- [structural-analogy] dimension $d(a)$ and simplicity $1/d(a)$ ↔ statistics/model selection: number of free parameters as complexity — both tie complexity to the amount of data needed to refute. — from [[popper-1959-logic/appii-following]] (analytic-philosophy → other:statistics)
- [structural-analogy] Dimension $d$ of a theory = number of parameters ↔ statistics: model complexity and the number of free parameters (the text does not mention statistics) — both count a model's freedom. — from [[popper-1959-logic/appviii-untitled]] (analytic-philosophy → other:statistics)
- [structural-analogy] Dimension of a curve set equals number of free parameters ↔ statistics/modelling: model complexity as number of parameters; fewer free parameters means more ways the data can contradict the model. — from [[popper-1959-logic/ch06-degrees]] (analytic-philosophy → other:statistics)
- [structural-analogy] curse of dimensionality (sparse data in 40-D) ↔ nearest-neighbour and density estimation: distances lose contrast in high dimensions (note 5, p. 135). — from [[prince-2023-udl/ch08-measuring]] (llm → other:nearest-neighbour-and-density)
- [metaphor] Disentangled latent dimensions (topic, tense) ↔ llm: feature steering — directions in a representation that change one property. — from [[prince-2023-udl/ch14-unsupervised]] (llm → llm)
- [structural-analogy] Particle filter weight degeneracy ↔ importance sampling in high dimension: both have weights concentrating on one draw. — from [[robert-2011-mcmc/main]] (bayesian → other:importance-sampling-in-high)
- [metaphor] rationality as a bundle of attributes ↔ bounded rationality: departures from rationality have many dimensions, not one scale. — from [[schelling-1960-conflict/ch01-retarded]] (decision-game-theory → decision-game-theory)
- [same-math] Factor analysis of 18 ratings ↔ statistics: dimension reduction of correlated variables. — from [[slovic-1987-perception/main]] (communication-theory → other:statistics)
- [same-math] Counting dimension of $\{y:My=0\}$ ≥ unknowns − constraints ↔ rank–nullity (over $\mathbb F_2$ here). — from [[spielman-2025-sagt/ch29-expander]] (linear-algebra → unspecified)
- [structural-analogy] Voiculescu's theorem (infinite dimension, equality) ↔ free probability: the finite inequality mirrors the limiting additive convolution (p. 348). — from [[spielman-2025-sagt/ch43-ramanujan]] (linear-algebra → other:probability)
- [structural-analogy] Fourier series as least squares in infinite dimensions (p. 170) ↔ analysis: expansion in orthogonal functions — from [[strang-2023-introduction/ch04-orthogonality-p1]] (linear-algebra → other:mathematics)
- [structural-analogy] Eckart–Young truncation ↔ latent-factor / dimension-reduction models for survey or ratings matrices: keep few strong components, treat the rest as noise. — from [[strang-2023-introduction/ch07-singular]] (linear-algebra → linear-algebra)
- [same-math] $f'(x^*)$ stability test ↔ complex-systems: Jacobian eigenvalue test in higher dimensions — for $n=1$ the Jacobian is the single number $f'(x^*)$. — from [[strogatz-2024-nonlinear/ch02-flows]] (complex-systems → complex-systems)
- [structural-analogy] redundant dimension as a "noise buffer" ↔ requisite variety: spare dimensions give the regulator room to absorb disturbance — only a loose parallel — from [[todorov-2002-ofc/main]] (control-theory → other:requisite-variety)
- [structural-analogy] Sinusoids of geometric wavelengths for position ↔ Fourier features: each dimension is a sinusoid of a different frequency. — from [[vaswani-2017-transformer/main]] (llm → other:signal-processing)
- [metaphor] finding a concept's place "in another dimension" via application (§165) ↔ mathematics: imaginary numbers in the real continuum. — from [[wittgenstein-1953-investigations/ch09-ppf]] (analytic-philosophy → other:mathematics)
- [metaphor] Values/ideology dimensionality ↔ intelligence dimensions: author's own analogy of correlated but distinct dimensions (pp. 26–27). — from [[zaller-1992-massopinion/ch02-information]] (political-science → other:intelligence-dimensions)
