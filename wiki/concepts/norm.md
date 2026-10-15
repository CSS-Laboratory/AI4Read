---
id: norm
type: concept
fields: [linear-algebra]
n_sources: 22
tiers: [core, deep]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p1, axler-2024-ladr/ch07-operators-p2, boyd-2018-vmls/ch03-norm, boyd-2018-vmls/ch04-clustering, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch07-matrix, bryan-2006-eigenvector/main, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch10-dimensionality, deisenroth-2020-mml/ch12-classification, eckart-1936-lowrank/main, mikolov-2013-regularities/main, spielman-2025-sagt/ch08-eigenvalues, spielman-2025-sagt/ch14-approximating, spielman-2025-sagt/ch23-spectral, spielman-2025-sagt/ch27-properties, spielman-2025-sagt/ch31-psrgs, spielman-2025-sagt/ch32-sparsification, strang-2023-introduction/ch01-vectors, strang-2023-introduction/ch07-singular, strang-2023-introduction/ch09-linear]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# norm

## Canon spine entry

- **norm** (linear-algebra): a size of a vector or matrix (ℓ2, ℓ1, Frobenius, spectral) (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p1]] (p. 186): here $\|v\|=\sqrt{\langle v,v\rangle}$, the norm induced by an inner product
- [[axler-2024-ladr/ch07-operators-p2]] (p. 258): the quantity preserved by isometries
- [[boyd-2018-vmls/ch03-norm]] (pp. 45–46): Euclidean norm √(xᵀx); four properties; the only norm used in the book
- [[boyd-2018-vmls/ch04-clustering]] (p. 72): Euclidean length; distances $\|x_i-z_j\|$ drive all steps
- [[boyd-2018-vmls/ch06-matrices]] (p. 117): here the matrix (Frobenius) norm (6.3): root of the sum of squared entries
- [[boyd-2018-vmls/ch07-matrix]] (p. 135): squared norm $\|\cdot\|^2$ used in the Dirichlet energy
- [[bryan-2006-eigenvector/main]] (p. 8): the 1-norm $\|v\|_1=\sum|v_i|$
- [[deisenroth-2020-mml/ch03-analytic]] (p. 71): function giving a vector's length; homogeneous, triangle inequality, positive definite
- [[deisenroth-2020-mml/ch04-matrix-p2]] (p. 131): here the spectral norm $\|A\|_2=\max_x\|Ax\|_2/\|x\|_2=\sigma_1$
- [[deisenroth-2020-mml/ch10-dimensionality]] (pp. 327, 334): spectral norm in (10.50); squared Euclidean norm in the error
- [[deisenroth-2020-mml/ch12-classification]] (p. 375, 377): the Euclidean norm $\|\boldsymbol w\|$; the margin equals $1/\|\boldsymbol w\|$ under the scaling of 12.2.2
- [[eckart-1936-lowrank/main]] (p. 212): "length" $l=(\alpha,\alpha)^{1/2}$ of a matrix; distance is the length of the difference
- [[mikolov-2013-regularities/main]] (p. 748): vectors are normalized to unit norm before computing $y$
- [[spielman-2025-sagt/ch08-eigenvalues]] (p. 71): spectral norm $\|R\|=\max_x|x^TRx/x^Tx|$
- [[spielman-2025-sagt/ch14-approximating]] (p. 129): here the matrix norm $\|x\|_A=\sqrt{x^TAx}=\|A^{1/2}x\|$ for PSD $A$
- [[spielman-2025-sagt/ch23-spectral]] (p. 191): spectral norm $\|R\|$ (largest $|$eigenvalue$|$ of symmetric $R$) measures noise size
- [[spielman-2025-sagt/ch27-properties]] (p. 220): operator norm = largest singular value
- [[spielman-2025-sagt/ch31-psrgs]] (p. 254): here the operator (2-norm) $\max_v\|Mv\|/\|v\|$
- [[spielman-2025-sagt/ch32-sparsification]] (p. 259): the matrix norm bound $\|X_i\|\le R$ controls the Chernoff bound
- [[strang-2023-introduction/ch01-vectors]] (p. 9): length ‖v‖ = √(v·v)
- [[strang-2023-introduction/ch07-singular]] (p. 302): spectral $\|A\|_2=\sigma_1$, Frobenius $\sqrt{\sum\sigma_i^2}$, nuclear $\sum\sigma_i$
- [[strang-2023-introduction/ch09-linear]] (p. 355–356): ℓ¹, ℓ², ℓ^∞, ℓᵖ (p ≥ 1); the "ℓ⁰ norm" counts nonzeros and is not a norm

## Instances that use it

- [[us-senate-reciprocity]] — norm of reciprocity; turnover down from about 40% to about 20% — from [[axelrod-1984-cooperation/ch01-problemof]]
- [[us-congress-reciprocity]] — norm of reciprocity emerged from early treachery — from [[axelrod-1984-cooperation/ch09-robustness]]
- [[norm-example-7-90]] — norms: $\|I\|=1$; all-ones matrix has norm $n$; the $1/(j^2+k)$ matrix has $\|T\|\approx0.8$ and $\|T^{-1}\|\approx10^6$ — from [[axler-2024-ladr/ch07-operators-p3]]
- [[gradient-of-squared-norm-of-vector-function]] — $\nabla h(z)=2Df(z)^Tf(z)$ — from [[boyd-2018-vmls/app-appendices]]
- [[least-norm-force-sequence]] — least norm $0.0121$ vs bang-bang $2$ — from [[boyd-2018-vmls/ch16-constrained]]
- [[kuwait-sabah-succession]] — a norm of alternating succession between two branches — from [[clark-2017-principles/ch10-varieties-p2]]
- [[manhattan-vs-euclidean-norm]] — $\ell_1$ and $\ell_2$ unit sets differ; $\ell_1$ has no inner product — from [[deisenroth-2020-mml/ch03-analytic]]
- [[matza-delinquent-boys]] — status pressure produces bandwagon against held norms — from [[granovetter-1978-threshold/main]]
- [[wincing-soup-eater]] — norm theory: later events recruit the first one — from [[kahneman-2011-thinking/ch06-norms]]
- [[dolphins-vs-farmworkers]] — category norms plus intensity matching, then reversal in joint evaluation — from [[kahneman-2011-thinking/ch33-reversals]]
- [[hawthorne-studies]] — test-room group raised output whatever the conditions; a natural group set an output norm that depressed it — from [[katz-1955-personalinfluence/ch02-played]]
- [[sherif-autokinetic-experiment]] — private estimates converge into a group norm that persists afterwards — from [[katz-1955-personalinfluence/ch04-norms]]
- [[rwanda-radio-soap-opera]] — field experiment shifting norms and behavior, not beliefs — from [[lewandowsky-2012-misinformation/main]]
- [[nowak-may-spatial-pd]] — lattice players; cooperators can persist without norms — from [[mitchell-2009-guidedtour/ch14-prospects]]
- [[axelrod-norms-metanorms]] — metanorms sustained cooperation in the original model — from [[mitchell-2009-guidedtour/ch14-prospects]]
- [[gaussian-norm-concentration]] — PAC-Bayes proof of $\|X\|\le\sqrt{\mathrm{tr}\Sigma}+\sqrt{2\|\Sigma\|_{op}\ln\frac1\delta}$ — from [[polyanskiy-2025-information/ch05-variational]]
- [[lipschitz-density-class]] — $\log N=\Theta(1/\epsilon)$, sharp sup-norm constant $LA/\epsilon$ — from [[polyanskiy-2025-information/ch30-metric]]
- [[trivial-lqr-random-search-variance]] — $R(u)=\|u\|^2$ with Gaussian sampling shows dimension scaling of the gradient norm — from [[recht-2019-tour/main]]
- [[korean-villages-family-planning]] — same-trait women, villages with 57% vs 26% adoption; village norms — from [[rogers-2003-diffusion/ch01-elements-p2]]
- [[us-smoking-cessation]] — discontinuance driven by norms, media and regulation — from [[rogers-2003-diffusion/ch05-innovation-p2]]
- [[sherif-norm-experiments]] — subjects create norms, and joint norms influence each other — from [[schelling-1960-conflict/ch06-game]]
- [[path-on-3-vertices-norm]] — an asymmetric walk matrix with norm $\sqrt2>1$ — from [[spielman-2025-sagt/ch31-psrgs]]
- [[kadison-singer-problem]] — essentially equivalent to dropping scale factors for equal-norm vectors — from [[spielman-2025-sagt/ch33-linear]]
- [[home-equity-norm-erosion]] — mortgage pay-off norm fades; equity funds consumption — from [[thaler-2015-misbehaving/ch09-buckets]]
- [[hmrc-tax-letter-experiment]] — all social-norm letters helped; the best one raised payment within 23 days by over 5 percentage points — from [[thaler-2015-misbehaving/ch33-nudging]]

## Candidate bridges

- [metaphor] Ratchet effect ↔ social norms: once reciprocity is established it does not slide back. — from [[axelrod-1984-cooperation/ch09-robustness]] (decision-game-theory → other)
- [same-math] 7.92 ↔ Eckart–Young theorem (spectral-norm version) — same statement: truncated SVD is the best rank-$k$ approximation, error $s_{k+1}$. — from [[axler-2024-ladr/ch07-operators-p3]] (linear-algebra → unspecified)
- [same-math] Type Two equation with constant $h=\beta$ and sup over actions ↔ control-theory: value iteration for a discounted decision process; the argument is a sup-norm contraction by factor $\beta$. — from [[bellman-1957-dp/ch04-iv]] (control-theory → control-theory)
- [structural-analogy] FIM scaling ↔ Newton's method: both rescale the gradient by curvature, in different norms. — from [[bertsekas-2026-rlcourse/ch03-learning-p4]] (control-theory → other)
- [same-math] Max-norm contraction of $H$ ↔ standard Bellman-operator contraction in discounted DP — the same argument ($\alpha$-discounting plus averaging by probabilities) — from [[bertsekas-2026-rlcourse/ch03-learning-p5]] (control-theory → unspecified)
- [same-math] $a^Ta=\sum a_i^2$ ↔ norm: squared Euclidean length of a vector (the norm is not defined in this unit). — from [[boyd-2018-vmls/ch01-vectors]] (linear-algebra → other)
- [metaphor] Choice of units changing which houses are "close" ↔ feature scaling in nearest-neighbour methods (the chapter itself proposes weighted norms in ex. 3.28). — from [[boyd-2018-vmls/ch03-norm]] (linear-algebra → unspecified)
- [same-math] Least norm solution $C^T(CC^T)^{-1}d$ ↔ linear-algebra: pseudo-inverse of a wide full-row-rank matrix — the chapter states they are the same matrix. — from [[boyd-2018-vmls/ch16-constrained]] (linear-algebra → linear-algebra)
- [metaphor] Popper's "recklessly critical quest" ↔ the unit's culture of science: willingness to be wrong as a norm. — from [[clark-2017-principles/ch02-science]] (political-science → other)
- [structural-analogy] W/S as loyalty norm ↔ exit/voice/loyalty: a credible exit threat weakens loyalty, as the text itself notes (n. 32) — from [[clark-2017-principles/ch10-varieties-p3]] (political-science → other)
- [same-math] $x=(A^\top A)^{-1}A^\top b$ ↔ least squares: normal equations $A^\top Ax=A^\top b$ — same equation, which the unit equates with the minimum-norm least-squares solution. — from [[deisenroth-2020-mml/ch02-linear-p1]] (linear-algebra → other)
- [structural-analogy] Authors' evolutionary account of fairness norms ↔ evolution: group-level selection of cooperative norms. The authors call it speculation. — from [[dixit-2008-art-strategy/ch02-games]] (decision-game-theory → other)
- [same-math] Linear-model interference $\sum_{i\ne j}|W_i\cdot W_j|^2$ ↔ compressed sensing: coherence $\max_{i\ne j}|W_i\cdot W_j|$ — the $L^2$ and $L^\infty$ norms of the same off-diagonal vector. — from [[elhage-2022-superposition/main-p1]] (llm → other)
- [metaphor] Category norms with typical value and range ↔ descriptive statistics: a summary by a central value and a spread (the text gives no numbers). — from [[kahneman-2011-thinking/ch06-norms]] (decision-game-theory → other)
- [metaphor] Wiring a new norm to a shared value (p. 79) ↔ framing: both change the frame in which behaviour is seen. Framing is not stated in this unit (canon link). — from [[katz-1955-personalinfluence/ch05-role]] (communication-theory → communication-theory)
- [metaphor] "Closeness depends on the norm" ↔ robustness: which perturbations count as small depends on the chosen measure (not stated in this unit) — from [[liberzon-2012-calculus/ch01-introduction]] (control-theory → other)
- [structural-analogy] ∨I allowing odd disjunctions ↔ analytic-philosophy: conversational implicature — the text says such inferences may "violate implicit conversational norms" yet are logically fine (p. 132). — from [[magnus-2025-forallx/ch17-basic]] (analytic-philosophy → analytic-philosophy)
- [metaphor] Ritschl's "communal spirit" ↔ Ostrom's local norms: both stress non-market motives, but Olson here treats them as metaphysical (canon link; not stated in this unit) — from [[olson-1965-collectiveaction/ch04-orthodox]] (political-science → other)
- [structural-analogy] Multiple equilibria and focal points ↔ social conventions and norm selection: an outside cue picks among self-sustaining regularities. — from [[osborne-2004-introduction/ch02-nash-p1]] (decision-game-theory → political-science)
- [metaphor] Grokking as weight norm falling into the Goldilocks zone ↔ llm: delayed generalization during long pretraining — from [[prince-2023-udl/ch20-does]] (llm → llm)
- [structural-analogy] Double descent via weight norm ↔ classical bias/variance trade-off — from [[prince-2023-udl/ch20-does]] (llm → unspecified)
- [structural-analogy] Spectral norm bounding Lipschitz behaviour ↔ stability of repeated layer products in deep networks: large stretch compounds across layers. — from [[prince-2023-udl/ch22-mathematics]] (llm → other)
- [structural-analogy] Opinion leaders as central, norm-conforming nodes ↔ network analysis: high-centrality nodes relaying influence. — from [[rogers-2003-diffusion/ch01-elements-p2]] (communication-theory → complex-systems)
- [structural-analogy] Minimum norm brain imaging ↔ Gaussian process regression — the text says the Bayesian reading is equivalent to statistical inversion/GP regression (p. 5). — from [[sarkka-2023-bayesianfiltering/ch01-are]] (control-theory → unspecified)
- [structural-analogy] Joint norm formation under indeterminacy (Sherif) ↔ decision-game-theory: convention — a regularity that settles in to solve a recurring coordination problem. — from [[schelling-1960-conflict/ch06-game]] (decision-game-theory → decision-game-theory)
- [structural-analogy] Wage-cut anger ↔ incomplete contracts and fairness norms: unspecified fairness expectations constrain what firms can do. — from [[shiller-2019-narrative/ch17-boycotts]] (economics-finance → other)
- [same-math] Theorem 2.3.2 ↔ SVD: $\sigma_1=\max u^TAv$ is the spectral norm of $A$. — from [[spielman-2025-sagt/ch02-eigenvalues]] (linear-algebra → other)
- [structural-analogy] Richardson convergence ↔ random walks on graphs: both are analysed through powers of a matrix with norm below 1 (the author notes the analogy to Chapter 10, p. 273) — from [[spielman-2025-sagt/ch34-iterative]] (linear-algebra → other)
- [structural-analogy] Double descent's minimum-norm solution ↔ linear algebra: pseudoinverse solution of underdetermined Ax = b — the unit's setting is nonlinear and it does not mention the pseudoinverse — from [[strang-2023-introduction/ch10-learning]] (linear-algebra → linear-algebra)
- [metaphor] Costly punishment and the nailed-down box ↔ incomplete contracts — norms and safeguards fill gaps that formal enforcement leaves. — from [[thaler-2015-misbehaving/ch15-fairness]] (economics-finance → unspecified)
- [metaphor] Social-norm message ↔ conditional cooperators: Thaler's footnote links the idea to conditional cooperators, ch. 15 (p. 288, fn). — from [[thaler-2015-misbehaving/ch33-nudging]] (economics-finance → other)
