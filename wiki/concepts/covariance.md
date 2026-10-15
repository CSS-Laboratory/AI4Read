---
id: covariance
type: concept
fields: [control-theory, economics-finance]
n_sources: 2
tiers: [core, deep]
grounding: digests
sources: [markowitz-1952-portfolio/main, sarkka-2023-bayesianfiltering/ch01-symbols]
generated_by: build_kg.py
---

# covariance

## Definitions in the sources

### control-theory

- [[sarkka-2023-bayesianfiltering/ch01-symbols]] (p. xv): $\mathrm{Cov}[\mathbf x]=\mathrm E[(\mathbf x-\mathrm E\mathbf x)(\mathbf x-\mathrm E\mathbf x)^{\mathsf T}]$ [new]

### economics-finance

- [[markowitz-1952-portfolio/main]] (p. 80): $\sigma_{ij}=\rho_{ij}\sigma_i\sigma_j$, how two returns move together [new]

## Instances that use it

- [[mean-field-2d-gaussian]] — mean-field fit to a correlated 2-D Gaussian: same mean, decoupled covariance, underestimated marginal variance — from [[blei-2017-variational/main-p1]]
- [[x-and-x-squared-uncorrelated]] — zero covariance without independence — from [[deisenroth-2020-mml/ch06-probability-p1]]
- [[linear-map-of-standard-gaussian]] — Example 6.17: density of $Y=AX$, covariance $AA^\top$ — from [[deisenroth-2020-mml/ch06-probability-p2]]
- [[normal-unknown-mean-variance-approx]] — normal approximation for $(\mu,\log\sigma)$ with diagonal covariance $\mathrm{diag}(\hat\sigma^2/n,1/(2n))$ — from [[gelman-2013-bda3/ch04-asymptotics]]
- [[rbf-infinite-limit-to-gaussian-kernel]] — infinitely many radial basis functions give a Gaussian covariance — from [[mackay-2003-information/ch45-gaussian]]
- [[oceanic-tools-gaussian-process]] — tool counts with geographic-distance covariance — from [[mcelreath-2020-rethinking/ch13-adventures]]
- [[ar1-precision-vs-covariance]] — tridiagonal precision, dense covariance — from [[murphy-2023-pml2/ch04-graphical-p2]]
- [[sparse-graph-portfolio]] — sparse stock-covariance graph used in trading [CW07] — from [[murphy-2023-pml2/ch30-graph]]
- [[normal-family-fisher]] — Fisher matrices of $N(\mu,\sigma)$ in two parameterizations, covariance (81)–(87) — from [[nielsen-2020-elementary/main-p1]]
- [[cramer-rao-simulation]] — MLE covariances versus Fisher ellipses, Fig. 8 — from [[nielsen-2020-elementary/main-p1]]
- [[zero-covariance-not-independent]] — uniform on unit circle: covariance zero, yet dependent — from [[prince-2023-udl/ch23-probability]]
- [[bivariate-normal-covariance-types]] — spherical, diagonal and full covariance shapes — from [[prince-2023-udl/ch23-probability]]
- [[coordinated-turn-model]] — polar and Cartesian versions; closed-form mean, intractable covariance — from [[sarkka-2023-bayesianfiltering/ch04-discretization]]
- [[age-height-covariance-example]] — six children; $S=\begin{bmatrix}20&25\\25&40\end{bmatrix}$, $u_1\approx(0.6,0.8)$ — from [[strang-2023-introduction/ch07-singular]]
- [[glued-coins]] — perfectly correlated coins with a singular covariance matrix — from [[strang-2023-introduction/ch10-learning]]

## Candidate bridges

- [metaphor] $\|Tv\|=\|T^*v\|$ for normal $T$ ↔ covariance/Gram matrices $X^{\mathrm t}X$ vs $XX^{\mathrm t}$ sharing structure (canon link; not stated in this unit). — from [[axler-2024-ladr/ch07-operators-p1]] (linear-algebra → unspecified)
- [same-math] trace $=$ sum of eigenvalues with multiplicity (8.52) ↔ linear-algebra: total variance in PCA equals the sum of covariance eigenvalues (covariance is symmetric, so it is a special case). — from [[axler-2024-ladr/ch08-operators]] (linear-algebra → linear-algebra)
- [structural-analogy] Universal property of $\otimes$ ↔ "bilinear in two arguments equals linear on a product space", the pattern behind covariance-style bilinear forms on data. — from [[axler-2024-ladr/ch09-multilinear-p2]] (linear-algebra → unspecified)
- [same-math] Mass matrix $M^{-1}$ = target covariance ↔ bayesian: preconditioning/reparameterization of $q$ by $\sqrt M q$ (the unit gives the transformation). — from [[betancourt-2017-hmc/main-p2]] (bayesian → bayesian)
- [same-math] Covariance-like Gram matrix $\tilde A^T\tilde A/n$ (exercise 10.16) ↔ statistics: covariance matrix of de-meaned data. — from [[boyd-2018-vmls/ch10-matrix]] (linear-algebra → other)
- [same-math] Hadamard's inequality ↔ linear algebra: $|K|\le\prod K_{ii}$ for covariance matrices, from $h(X_1..X_n)\le\sum h(X_i)$ (p. 233). — from [[cover-2006-elements/ch09-differential]] (information-theory → linear-algebra)
- [same-math] Cholesky sampling of a Gaussian with covariance $\Sigma=LL^\top$ ↔ probability (Chapter 6): linear transformation of random variables (as sketched on p. 115). — from [[deisenroth-2020-mml/ch04-matrix-p1]] (linear-algebra → other)
- [structural-analogy] $A^\top A$ and its eigenvectors ↔ statistics: the covariance-matrix route to principal components. The unit only says the SVD plays a key role in PCA. — from [[deisenroth-2020-mml/ch04-matrix-p2]] (linear-algebra → other)
- [same-math] covariance matrix symmetric PSD (p. 190) ↔ linear-algebra: spectral theorem — real symmetric PSD matrices have orthonormal eigenbases and nonnegative eigenvalues. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [same-math] $\boldsymbol A\boldsymbol\Sigma\boldsymbol A^\top$ (6.51) ↔ linear-algebra: how a linear map transforms a quadratic form / covariance of linearly mapped data. — from [[deisenroth-2020-mml/ch06-probability-p1]] (linear-algebra → linear-algebra)
- [same-math] Gaussian conditioning (6.66)–(6.67) ↔ linear-algebra: least squares/projection, where the conditional mean is a linear regression of $x$ on $y$ with the Schur complement as residual covariance — the formulas are the same block-matrix algebra (the text itself does not state this link). — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [same-math] $y=Ax$ gives covariance $A\Sigma A^\top$ ↔ linear-algebra: congruence/quadratic form $A\Sigma A^\top$ of a positive semi-definite matrix. — from [[deisenroth-2020-mml/ch06-probability-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] PPCA covariance $BB^\top+\sigma^2I$ ↔ social-science latent factor models: a few shared factors plus noise explain the correlations among many observed variables. — from [[deisenroth-2020-mml/ch10-dimensionality]] (linear-algebra → other)
- [structural-analogy] Weighted covariance update (11.30) ↔ PCA/covariance matrix: the same average of outer products of centered data, but with responsibility weights. — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → linear-algebra)
- [structural-analogy] GMM-EM ↔ K-means: with covariances ignored, soft assignment becomes hard assignment (stated on p. 368). — from [[deisenroth-2020-mml/ch11-density]] (linear-algebra → other)
- [same-math] Squared multipliers = characteristic values of $\alpha\alpha'$ ↔ covariance eigenvalues: PCA variances are eigenvalues of $XX'$ (canon link; not stated in this unit). — from [[eckart-1936-lowrank/main]] (linear-algebra → linear-algebra)
- [same-math] Market-model slope $\beta_j$ and eq. (16) ↔ CAPM: if the covariance and variance in (16) are constant over time, $\beta_j(\Phi_t)$ corresponds to the slope $\beta_j$ in (12), whose least-squares estimate is the sample covariance over the sample variance (p. 403). — from [[fama-1970-efficient/main]] (economics-finance → other)
- [same-math] GP posterior mean/covariance ↔ multivariate normal conditioning (BDA §3.5): the formulas on p. 503 are Gaussian conditioning. — from [[gelman-2013-bda3/ch21-gaussian]] (bayesian → other)
- [structural-analogy] k-means as limit of a Gaussian mixture as covariances → 0 ↔ statistics: hard-EM as limit of soft-EM — the chapter states the limiting relation (p. 222). — from [[grimmer-2022-textasdata/ch12-clustering]] (political-science → other)
- [same-math] Exercise 7.4's weights (7.39)–(7.40) ↔ statistics: minimum-variance linear combination under a known covariance matrix (p. 215) — from [[jaynes-2003-probability/ch07-central-p1]] (information-theory → other)
- [same-math] $\log Z$ derivatives give means and covariances (11.60, 11.73) ↔ exponential-family theory: log-partition function as cumulant generating function — the same identities — from [[jaynes-2003-probability/ch11-discrete]] (information-theory → other)
- [same-math] Logistic output of a neuron ↔ Bayesian: posterior $P(s=1|\mathbf y)$ with Gaussian likelihoods and a shared covariance matrix (eqs. 39.8–39.9, section 11.2) — the formulas coincide. — from [[mackay-2003-information/ch39-single]] (information-theory → bayesian)
- [structural-analogy] GP covariance function ↔ kernel methods: the kernel in SVMs, which MacKay says is another name for it (p. 548). — from [[mackay-2003-information/ch45-gaussian]] (information-theory → other)
- [structural-analogy] Gaussian-process kernel (covariance falls with distance) ↔ spatial statistics: spatial autocorrelation — covariance as a function of separation — from [[mcelreath-2020-rethinking/ch13-adventures]] (bayesian → other)
- [same-math] Spectral-density formula for the information rate ↔ signal processing: log-determinant of Toeplitz covariances and Szegő's theorem. — from [[polyanskiy-2025-information/ch07-tensorization]] (information-theory → other)
- [structural-analogy] Lyapunov ODE (4.53) for $\mathbf P(t)$ ↔ control-theory: covariance propagation in the continuous-discrete extended Kalman filter (the text notes the same approximation is used there, p. 59). — from [[sarkka-2023-bayesianfiltering/ch04-discretization]] (control-theory → control-theory)
- [structural-analogy] EKF ↔ observer (state estimator): a model run in parallel, corrected by gain times innovation, with the gain from the covariance. — from [[sarkka-2023-bayesianfiltering/ch07-extended]] (control-theory → other)
- [structural-analogy] Moment matching to an assumed density ↔ approximate inference: fitting a Gaussian to match mean and covariance of an intractable posterior. — from [[sarkka-2023-bayesianfiltering/ch08-general]] (control-theory → other)
- [same-math] SL/SLR coefficients $\mathbf A=\mathbf C^{\mathsf T}\mathbf P^{-1}$ ↔ statistics: best linear (least-squares) predictor and its residual covariance — same formulas as linear regression, taken with respect to a Gaussian input. — from [[sarkka-2023-bayesianfiltering/ch09-gaussian]] (control-theory → other)
- [same-math] Kalman innovations $v_k,S_k$ in the energy (16.38) ↔ control-theory: Kalman filter innovation and its covariance — same quantities, here used to score θ. — from [[sarkka-2023-bayesianfiltering/ch16-parameter]] (control-theory → control-theory)
- [structural-analogy] $\partial P/\partial t=A_xP+PA_x^\top+LQ^cL^\top$ ↔ control-theory: Lyapunov-type covariance propagation — same shape, different setting. — from [[sarkka-2023-bayesianfiltering/ch19-56ptappendixadditional]] (control-theory → control-theory)
- [structural-analogy] $\psi_2,\psi_3$ as coordinates ↔ PCA: low-dimensional coordinates from eigenvectors, though PCA uses a covariance matrix. — from [[spielman-2025-sagt/ch01-introduction]] (linear-algebra → linear-algebra)
- [same-math] Rayleigh quotient maximization ↔ PCA: choosing the direction of maximal variance of a covariance matrix. — from [[spielman-2025-sagt/ch02-eigenvalues]] (linear-algebra → linear-algebra)
- [structural-analogy] Decoupling by A-orthogonality ↔ PCA: diagonalizing a covariance matrix — a good basis removes cross terms. — from [[spielman-2025-sagt/ch35-conjugate]] (linear-algebra → linear-algebra)
- [same-math] normal equations AᵀAx̂ = Aᵀb ↔ statistics/regression: ordinary least squares estimator (Problems 13–14 on p. 173–174 call x̂ unbiased and give its covariance σ²(AᵀA)⁻¹) — from [[strang-2023-introduction/ch04-orthogonality-p1]] (linear-algebra → other)
- [same-math] Spectral theorem S = QΛQᵀ ↔ PCA: eigen-decomposition of a covariance matrix gives orthogonal principal directions. — from [[strang-2023-introduction/ch06-eigenvalues-p2]] (linear-algebra → linear-algebra)
- [structural-analogy] Cholesky S = AᵀA ↔ statistics: factoring a covariance matrix into a triangular factor (not in this unit). — from [[strang-2023-introduction/ch06-eigenvalues-p2]] (linear-algebra → other)
- [same-math] PCA via SVD of centred $A$ ↔ eigendecomposition of covariance $S=AA^T/(n-1)$: $u_i$ and $\sigma_i^2$ are eigenvectors and eigenvalues of $AA^T$. — from [[strang-2023-introduction/ch07-singular]] (linear-algebra → linear-algebra)
- [structural-analogy] LSTD / Sherman–Morrison update ↔ control theory: recursive least squares and covariance-style updates — both maintain a matrix inverse recursively as data arrive. — from [[sutton-2018-rl/ch09-policy-p2]] (control-theory → control-theory)
- [structural-analogy] Narrow framing across projects ↔ diversification & covariance: pooling independent positive-value bets cuts the chance of a net loss. — from [[thaler-2015-misbehaving/ch20-narrow]] (economics-finance → other)
- [metaphor] Diversification cancelling independent moves ↔ portfolio theory: covariance, not individual volatility, drives portfolio risk. — from [[thaler-2015-misbehaving/ch23-reaction]] (economics-finance → other)
