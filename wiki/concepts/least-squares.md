---
id: least-squares
type: concept
fields: [linear-algebra]
n_sources: 17
tiers: [core]
grounding: digests
sources: [axler-2024-ladr/ch06-inner-p2, boyd-2018-vmls/app-appendices, boyd-2018-vmls/ch12-least, boyd-2018-vmls/ch13-least, boyd-2018-vmls/ch14-least, boyd-2018-vmls/ch15-multi, boyd-2018-vmls/ch16-constrained, boyd-2018-vmls/ch17-constrained, boyd-2018-vmls/ch18-nonlinear, boyd-2018-vmls/ch19-constrained, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch05-vector, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, eckart-1936-lowrank/main, strang-2023-introduction/ch04-orthogonality-p1, strang-2023-introduction/ch04-orthogonality-p2]
raw_ids: [least squares]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# least-squares

## Canon spine entry

- **least squares** (linear-algebra): solving an overdetermined Ax ≈ b by projecting b onto the column space (normal equations AᵀAx = Aᵀb) (UG)

## Definitions in the sources

### linear-algebra

- [[axler-2024-ladr/ch06-inner-p2]] (pp. 217, 222): only the minimization-in-norm idea appears (6.61, 6.70, sine approximation); normal equations are not stated here
- [[boyd-2018-vmls/app-appendices]] (p. 442): cost $2mn^2$ flops [as `least squares`]
- [[boyd-2018-vmls/ch12-least]] (p. 225): choose $x$ to minimize $\|Ax-b\|^2$ for tall $A$; the solution need not satisfy $Ax=b$
- [[boyd-2018-vmls/ch13-least]] (p. 247): choose θ to minimize ‖Aθ − yᵈ‖², here with A built from basis functions [as `least squares`]
- [[boyd-2018-vmls/ch14-least]] (p. 288): here the fitting engine behind every classifier in the chapter
- [[boyd-2018-vmls/ch15-multi]] (p. 310): reused; the stacked problem is solved by $(\tilde A^T\tilde A)^{-1}\tilde A^T\tilde b$, via QR
- [[boyd-2018-vmls/ch16-constrained]] (p. 340, 345): the unconstrained special case, with normal equations (12.4) [as `least squares`]
- [[boyd-2018-vmls/ch17-constrained]] (p. 360, 367, 373): minimize $\|Ax-b\|^2$; here it is the base of every application
- [[boyd-2018-vmls/ch18-nonlinear]] (p. 382): the linear special case, solved at each Gauss–Newton/LM step
- [[boyd-2018-vmls/ch19-constrained]] (pp. 421, 423): the stacked residuals (19.6), (19.10) are ordinary nonlinear least squares problems
- [[deisenroth-2020-mml/ch03-analytic]] (p. 88): approximate solution of unsolvable $Ax=b$ by projecting $b$ onto the column space [as `least squares`]
- [[deisenroth-2020-mml/ch05-vector]] (p. 154): squared-error loss $\|\mathbf y-\boldsymbol\Phi\boldsymbol\theta\|^2$, with gradient $-2\mathbf e^\top\boldsymbol\Phi$ [as `least squares`]
- [[deisenroth-2020-mml/ch08-when]] (p. 261): minimize (1/N)‖y − Xθ‖² (8.9); closed form via normal equations in Ch. 9
- [[deisenroth-2020-mml/ch09-linear]] (pp. 294, 296): minimizing $\|y-\Phi\theta\|^2$. Here it is the ML solution (9.12c)/(9.19), found by solving a linear system [as `least squares`]
- [[eckart-1936-lowrank/main]] (p. 212): approximation criterion with all elements equally weighted
- [[strang-2023-introduction/ch04-orthogonality-p1]] (pp. 163–164): x̂ minimizing ‖Ax − b‖² when Ax = b is unsolvable
- [[strang-2023-introduction/ch04-orthogonality-p2]] (pp. 179, 183): $\hat x=Q^{\mathsf T}b$ for $Q$; $R\hat x=Q^{\mathsf T}b$ for $A=QR$

## Instances that use it

- [[incremental-gradient-region-of-confusion]] — scalar least squares example showing fast far-field progress, oscillation inside $R$ — from [[bertsekas-2026-rlcourse/ch03-learning-p1]]
- [[boolean-least-squares]] — a constrained nonlinear least squares special case whose brute force method is not practical for $n$ larger than about 30 — from [[boyd-2018-vmls/app-appendices]]
- [[constrained-nonlinear-least-squares-kkt]] — KKT system $2Df^Tf+Dg^T\hat z=0$, $g=0$ — from [[boyd-2018-vmls/app-appendices]]
- [[mnist-digits]] — 60000-image digit data; Boolean and 10-class least squares classifiers — from [[boyd-2018-vmls/ch14-least]]
- [[location-from-ranges]] — least squares on range residuals; one of three LM starts ends at a non-optimal point — from [[boyd-2018-vmls/ch18-nonlinear]]
- [[least-squares-gradient]] — $\partial L/\partial\boldsymbol\theta=-2\mathbf e^\top\boldsymbol\Phi$ for the linear model — from [[deisenroth-2020-mml/ch05-vector]]
- [[least-squares-via-gd]] — Example 7.2: solving $Ax=b$ by minimising $\|Ax-b\|^2$ — from [[deisenroth-2020-mml/ch07-continuous]]
- [[gaussian-likelihood-linear-regression]] — Gaussian noise gives least squares (Ex. 8.4–8.5) — from [[deisenroth-2020-mml/ch08-when]]
- [[em-student-regression]] — scale-mixture latent variables turn robust regression into weighted least squares — from [[murphy-2023-pml2/ch06-optimization-p2]]
- [[recursive-least-squares]] — Kalman filter with latent state = regression weights — from [[murphy-2023-pml2/ch08-gaussian-p1]]
- [[1d-linear-regression]] — the line $y=\phi_0+\phi_1x$ fitted by least squares — from [[prince-2023-udl/ch02-supervised]]
- [[least-squares-regression-as-gaussian-mle]] — least squares follows from normal distribution with predicted mean and independence — from [[prince-2023-udl/ch05-loss]]
- [[kaczmarz-random-row]] — SGD for least squares via row projections; fast start, oscillating finish — from [[strang-2023-introduction/ch09-linear]]
- [[tsitsiklis-van-roy-counterexample]] — least-squares fit at each DP step still diverges if $\gamma>5/(6-4\varepsilon)$ — from [[sutton-2018-rl/ch11-off]]

## Candidate bridges

- [same-math] Recursive least squares (15.19) ↔ Kalman filter: the author states RLS is a special case of the Kalman filter (§8.2). — from [[astrom-2021-feedbacksystems/ch15-architecture-p2]] (control-theory → other)
- [structural-analogy] (range T)⁰ = null T′ ↔ least squares: the left null space is orthogonal to the column space (the two are the same relation without an inner product). — from [[axler-2024-ladr/ch03-linear-p3]] (linear-algebra → other)
- [same-math] Minimizing $\|v-u\|$ over $u\in U$ via $P_U$ ↔ statistics: least-squares fit — the same projection onto a subspace (normal equations are not in this unit). — from [[axler-2024-ladr/ch06-inner-p2]] (linear-algebra → other)
- [same-math] Linear least squares fit (3.7) ↔ statistics: ordinary least squares normal equations $\sum\phi\phi'\,r=\sum\phi\beta$. — from [[bertsekas-2026-rlcourse/ch03-learning-p1]] (control-theory → other)
- [same-math] condition $2Df(\hat x)^Tf(\hat x)=0$ ↔ least squares normal equations — the condition reduces to $A^T(Ax-b)=0$ when $f(x)=Ax-b$, since then $Df=A$ (our step; the text does not state this). — from [[boyd-2018-vmls/app-appendices]] (linear-algebra → unspecified)
- [structural-analogy] KKT conditions ↔ the KKT linear system of constrained least squares — in the linear case, $\nabla h+Dg^T\hat z=0$ and $g=0$ become linear equations (this unit does not state it). — from [[boyd-2018-vmls/app-appendices]] (linear-algebra → unspecified)
- [structural-analogy] k-means centroid update (mean minimises sum of squared distances) ↔ least squares: both minimise a sum of squared distances, and the mean is the best single constant fit (exercise 4.1 shows the minimiser). — from [[boyd-2018-vmls/ch04-clustering]] (linear-algebra → other)
- [same-math] pseudo-inverse $(A^TA)^{-1}A^T$ ↔ least squares: the normal-equations matrix (canon: least squares; the text defers the interpretation to later chapters) — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → other)
- [same-math] Matrix least squares $\hat X=A^\dagger B$ ↔ regression with several response variables: the same independent column-wise fits. — from [[boyd-2018-vmls/ch12-least]] (linear-algebra → other)
- [same-math] Matrix least squares for the $K$ coefficient vectors ↔ linear-algebra: least squares with a matrix right-hand side (the text points to p. 233) — same $X$, many right-hand sides. — from [[boyd-2018-vmls/ch14-least]] (linear-algebra → linear-algebra)
- [structural-analogy] control/estimation duality ↔ optimization: both are the same stacked constrained least squares, with inputs chosen (control) or inputs unknown (estimation) — the text itself calls this duality (p. 373). — from [[boyd-2018-vmls/ch17-constrained]] (linear-algebra → other)
- [same-math] LM step as regularized least squares ↔ linear-algebra: ridge/Tikhonov-type regularized least squares — each step solves $\min\|Ax-b\|^2+\lambda\|x-x^{(k)}\|^2$ literally. — from [[boyd-2018-vmls/ch18-nonlinear]] (linear-algebra → linear-algebra)
- [structural-analogy] Newton/Gauss–Newton iteration ↔ linear-algebra: repeated linearization — nonlinear problem solved as a sequence of linear least squares problems. — from [[boyd-2018-vmls/ch18-nonlinear]] (linear-algebra → linear-algebra)
- [structural-analogy] penalty method with growing $\mu$ ↔ regularization/bi-objective least squares: the weighted trade-off $\|f\|^2+\mu\|g\|^2$ (ch. 16 bi-objective view, mentioned on p. 421) — from [[boyd-2018-vmls/ch19-constrained]] (linear-algebra → other)
- [structural-analogy] inner step (19.10) ↔ ordinary stacked least squares: minimize $\|r(x)\|^2$ for the stacked residual — from [[boyd-2018-vmls/ch19-constrained]] (linear-algebra → other)
- [same-math] $x=(A^\top A)^{-1}A^\top b$ ↔ least squares: normal equations $A^\top Ax=A^\top b$ — same equation, which the unit equates with the minimum-norm least-squares solution. — from [[deisenroth-2020-mml/ch02-linear-p1]] (linear-algebra → other)
- [same-math] Normal equation $B^\top B\lambda=B^\top x$ ↔ linear regression (Ch. 9, as stated in the unit): the least-squares fit is a projection of the target onto the column space (p. 88). — from [[deisenroth-2020-mml/ch03-analytic]] (linear-algebra → other)
- [same-math] Gaussian conditioning (6.66)–(6.67) ↔ linear-algebra: least squares/projection, where the conditional mean is a linear regression of $x$ on $y$ with the Schur complement as residual covariance — the formulas are the same block-matrix algebra (the text itself does not state this link). — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Pseudo-inverse step (6.90) ↔ linear-algebra: least-squares normal equations $A^\top Ax=A^\top y$ — the same expression, used here to invert a Gaussian mean map. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] Least-squares ERM (8.9) ↔ linear-algebra: least squares by projecting y onto the column space of X (the book defers the closed form to Sec. 9.2 (p. 261); the projection reading is from the field list, not this unit). — from [[deisenroth-2020-mml/ch08-when]] (linear-algebra → linear-algebra)
- [same-math] ML normal equations $\Phi^\top\Phi\theta=\Phi^\top y$ ↔ linear algebra: least-squares solution of an overdetermined $A x\approx b$ — identical equations. — from [[deisenroth-2020-mml/ch09-linear]] (linear-algebra → linear-algebra)
- [same-math] MAP with Gaussian prior ↔ regularized (ridge) least squares: $(\Phi^\top\Phi+\lambda I)^{-1}\Phi^\top y$ with $\lambda=\sigma^2/b^2$. — from [[deisenroth-2020-mml/ch09-linear]] (linear-algebra → other)
- [same-math] Market-model slope $\beta_j$ and eq. (16) ↔ CAPM: if the covariance and variance in (16) are constant over time, $\beta_j(\Phi_t)$ corresponds to the slope $\beta_j$ in (12), whose least-squares estimate is the sample covariance over the sample variance (p. 403). — from [[fama-1970-efficient/main]] (economics-finance → other)
- [same-math] Ridge/least-squares-with-prior-as-extra-rows ↔ Bayesian conjugate updating: a normal prior on β is exactly extra rows $(I_k, \beta_0)$ in a weighted regression (14.24) — same algebra, different language. — from [[gelman-2013-bda3/ch14-introduction]] (bayesian → bayesian)
- [same-math] Weighted regression with $\Sigma_{ii}=\sigma^2/w_i$ ↔ generalized least squares: $\Sigma_y^{-1/2}$ transformation gives (14.12)–(14.13). — from [[gelman-2013-bda3/ch14-introduction]] (bayesian → other)
- [same-math] Normal prior as extra "observation" rows ↔ weighted least squares on stacked data — (15.3) is literally one weighted regression. — from [[gelman-2013-bda3/ch15-hierarchical]] (bayesian → unspecified)
- [same-math] pseudodata weighted regression (16.4) ↔ optimization: Newton/Fisher-scoring step (iteratively reweighted least squares) — the text says iterating equals Newton's method on the log posterior (p. 411) — from [[gelman-2013-bda3/ch16-generalized]] (bayesian → other)
- [same-math] adding $J$ prior rows to the regression (16.7) ↔ ridge-type penalized regression: normal prior as data augmentation — same weighted least-squares algebra — from [[gelman-2013-bda3/ch16-generalized]] (bayesian → other)
- [same-math] Lasso/ridge penalties ↔ Regression: regularized least squares — the same loss plus penalty form (Table 19.1). — from [[grimmer-2022-textasdata/ch19-classifying]] (political-science → other)
- [same-math] Weighted least squares $\hat x=(\tilde AWA)^{-1}\tilde AWy$ ↔ bayesian: posterior mean in a Gaussian linear model with flat prior — same formula (p. 596) — from [[jaynes-2003-probability/ch19-physical]] (information-theory → bayesian)
- [structural-analogy] Orthogonal-projection estimate ↔ statistics: least-squares regression as projection onto a span — both minimize squared error by making the residual orthogonal to the regressors. — from [[kalman-1960-filtering/main]] (control-theory → other)
- [structural-analogy] Quadratic cost gives linear law ↔ statistics: Gauss's least squares (footnote 1, p. 147). — from [[liberzon-2012-calculus/ch06-linear]] (control-theory → other)
- [same-math] $\mathbf f_{\rm MP}$ with Gaussian prior ↔ ridge regression: $\mathbf R^{\rm T}\mathbf R+\lambda\mathbf C$ regularizes least squares. — from [[mackay-2003-information/ch46-deconvolution]] (information-theory → other)
- [same-math] design matrix, $\mathbf m=\mathbf X\mathbf b$ and least-squares formula (p. 124) ↔ linear algebra / OLS: same matrix form. — from [[mcelreath-2020-rethinking/ch05-multivariate-p1]] (bayesian → linear-algebra)
- [structural-analogy] Regularizing Gaussian prior / ridge regression ↔ frequentist statistics: penalized least squares with penalty $\lambda$ — the author says both views exist (p. 188). — from [[mcelreath-2020-rethinking/ch06-overfitting-p2]] (bayesian → other)
- [same-math] SLR (8.165) ↔ least-squares regression: the same MSE objective, averaged over a Gaussian input. — from [[murphy-2023-pml2/ch08-gaussian-p2]] (bayesian → other)
- [same-math] EKF on a linear model = recursive least squares ↔ Kalman filtering: the text itself says the KF applied to linear regression is recursive least squares (p. 673). — from [[murphy-2023-pml2/ch17-bayesian]] (bayesian → other)
- [structural-analogy] Prior as regularisation ↔ penalised least squares (suggested by p. 18 and Ex. 2.4(d)). — from [[sarkka-2023-bayesianfiltering/ch02-bayesian]] (control-theory → unspecified)
- [same-math] IEKF update ↔ optimisation: Gauss–Newton for a nonlinear least-squares/MAP cost (the text states this equivalence, p. 121–122). — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → other)
- [same-math] SL/SLR coefficients $\mathbf A=\mathbf C^{\mathsf T}\mathbf P^{-1}$ ↔ statistics: best linear (least-squares) predictor and its residual covariance — same formulas as linear regression, taken with respect to a Gaussian input. — from [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (control-theory → other)
- [same-math] IERTSS iteration ↔ nonlinear least squares: Gauss–Newton on the cost (13.17), solved by Kalman filter and smoother. — from [[sarkka-2023-bayesianfiltering/ch13-extended]] (control-theory → other)
- [structural-analogy] σ_max/σ_min ↔ statistics: near-singular design matrices make least-squares estimates unstable. — from [[strang-2023-introduction/app1-ranks]] (linear-algebra → other)
- [same-math] normal equations AᵀAx̂ = Aᵀb ↔ statistics/regression: ordinary least squares estimator (Problems 13–14 on p. 173–174 call x̂ unbiased and give its covariance σ²(AᵀA)⁻¹) — from [[strang-2023-introduction/ch04-orthogonality-p1]] (linear-algebra → other)
- [structural-analogy] Fourier series as least squares in infinite dimensions (p. 170) ↔ analysis: expansion in orthogonal functions — from [[strang-2023-introduction/ch04-orthogonality-p1]] (linear-algebra → other)
- [same-math] $A=QR$ and $R\hat x=Q^{\mathsf T}b$ ↔ numerical linear algebra: QR-based least squares avoiding $A^{\mathsf T}A$ — same factorization, used for solving. — from [[strang-2023-introduction/ch04-orthogonality-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] LSTD / Sherman–Morrison update ↔ control theory: recursive least squares and covariance-style updates — both maintain a matrix inverse recursively as data arrive. — from [[sutton-2018-rl/ch09-policy-p2]] (control-theory → control-theory)
