---
id: deisenroth-2020-mml/index
work: deisenroth-2020-mml
type: work-map
units: [deisenroth-2020-mml/ch01-introduction, deisenroth-2020-mml/ch02-linear-p1, deisenroth-2020-mml/ch02-linear-p2, deisenroth-2020-mml/ch03-analytic, deisenroth-2020-mml/ch04-matrix-p1, deisenroth-2020-mml/ch04-matrix-p2, deisenroth-2020-mml/ch05-vector, deisenroth-2020-mml/ch06-probability-p1, deisenroth-2020-mml/ch06-probability-p2, deisenroth-2020-mml/ch07-continuous, deisenroth-2020-mml/ch08-when, deisenroth-2020-mml/ch09-linear, deisenroth-2020-mml/ch10-dimensionality, deisenroth-2020-mml/ch11-density, deisenroth-2020-mml/ch12-classification]
---

# Deisenroth, M. P., Faisal, A. A., & Ong, C. S. (2020). *Mathematics for Machine Learning*. Cambridge University Press. https://doi.org/10.1017/9781108679930

## In one paragraph
The book argues that machine learning rests on three things: data (treated as vectors), a model, and learning by optimizing the model's parameters. Part I builds the mathematics for these: linear algebra, analytic geometry, matrix decompositions, vector calculus, probability and optimization. Part II uses it on four problems: linear regression, dimensionality reduction with PCA, density estimation with Gaussian mixtures, and classification with SVMs. Inner products, projections and decompositions explain why the methods work. For example, maximum likelihood in regression is an orthogonal projection, and PCA is a projection onto the top eigenvectors of the covariance matrix. The aim is to help readers build, debug and understand the limits of ML methods. The book is modular, so it can be read bottom-up or top-down.

## The path through the work
- [[deisenroth-2020-mml/ch01-introduction]] — Machine learning rests on three things (data, a model, learning), and this book first builds the mathematics for them (Part I) and then applies it to four core problems (Part II).
- [[deisenroth-2020-mml/ch02-linear-p1]] — Anything that can be added and scaled is a vector, and a linear system Ax = b is solved by Gaussian elimination, which brings the system to a simple form from which one particular solution plus all solutions of Ax = 0 can be found.
- [[deisenroth-2020-mml/ch02-linear-p2]] — A basis gives every vector unique coordinates, so a linear map between finite-dimensional spaces becomes a matrix, and changing bases changes that matrix by $\tilde A=T^{-1}AS$.
- [[deisenroth-2020-mml/ch03-analytic]] — An inner product on a vector space defines lengths, distances, angles and orthogonality, and orthogonal projection onto a subspace (via the normal equation) is a central application built on them.
- [[deisenroth-2020-mml/ch04-matrix-p1]] — A square matrix can be summarised by its determinant, trace and eigenvalues (det = product, trace = sum of eigenvalues), and it can be factored into simpler matrices, e.g. $A=LL^\top$ (Cholesky, for symmetric positive definite $A$) or $A=PDP^{-1}$ (eigendecomposition, when the eigenvectors form a basis).
- [[deisenroth-2020-mml/ch04-matrix-p2]] — Every real matrix factors as $A=U\Sigma V^\top$ (rotate, scale, rotate), and writing it as a sum of rank-1 pieces and cutting the sum after $k$ terms gives the best rank-$k$ approximation in the spectral norm.
- [[deisenroth-2020-mml/ch05-vector]] — Gradients, Jacobians and Hessians collect partial derivatives into arrays whose shapes make the multivariate chain rule a plain matrix product. This lets backpropagation compute gradients efficiently and lets Taylor expansions approximate functions locally.
- [[deisenroth-2020-mml/ch06-probability-p1]] — Probability is a mathematical structure (probability space → random variable → distribution) obeying two rules, the sum rule and the product rule; Bayes' theorem follows from the product rule, and summary statistics and independence describe and compare distributions.
- [[deisenroth-2020-mml/ch06-probability-p2]] — Gaussians stay Gaussian under marginalizing, conditioning, summing independent variables and linear maps; exponential families have conjugate priors, so Bayesian updating stays inside the family; and change of variables (with a Jacobian determinant) gives the density of a differentiable invertible transform.
- [[deisenroth-2020-mml/ch07-continuous]] — Training a model often means minimising a differentiable objective by following negative gradients (gradient descent), and for constrained convex problems Lagrange duality and the convex conjugate give a second, dual way to solve the same problem.
- [[deisenroth-2020-mml/ch08-when]] — A machine learning model is fitted to data by empirical risk minimization, maximum likelihood or MAP point estimates, or by full Bayesian inference, and its quality is judged on unseen data, using cross-validation or model evidence.
- [[deisenroth-2020-mml/ch09-linear]] — Linear regression with Gaussian noise is least squares seen as maximum likelihood, and adding a Gaussian prior gives regularization (MAP, which maximizes the posterior over the parameters) and then a full Bayesian treatment, all in closed form; geometrically, maximum likelihood is an orthogonal projection.
- [[deisenroth-2020-mml/ch10-dimensionality]] — PCA compresses data by projecting it onto the eigenvectors of the data covariance matrix with the largest eigenvalues, and the variance lost (the average squared reconstruction error) equals the sum of the discarded eigenvalues.
- [[deisenroth-2020-mml/ch11-density]] — A Gaussian mixture model is fitted by maximum likelihood with the EM algorithm, which alternates computing soft cluster assignments (responsibilities) with responsibility-weighted updates of means, covariances and weights.
- [[deisenroth-2020-mml/ch12-classification]] — A support vector machine picks the separating hyperplane with the largest margin, its soft margin version is equivalent to regularized hinge-loss minimization, and its dual form uses only inner products between examples, so kernels give nonlinear classifiers.

## Big ideas across units
- **Orthogonal projection as the engine of fitting.** Projection onto a subspace is derived in ch03 (normal equation, least squares). In ch09 it becomes maximum likelihood for regression, and in ch10 it gives the projection view of PCA. ch12 lists it among its prerequisites. Units: ch03-analytic, ch09-linear, ch10-dimensionality, ch12-classification.
- **Bases, coordinates and change of basis.** A basis gives coordinates, linear maps become matrices, and a basis change can diagonalize a matrix. The same idea reappears in eigendecomposition and in the SVD, which changes basis in the domain and the codomain. Units: ch02-linear-p2, ch04-matrix-p1, ch04-matrix-p2.
- **Decompose a matrix, then truncate it.** Cholesky, eigendecomposition and SVD make determinants, powers and approximations cheap. Eckart–Young says truncating the SVD gives the best low-rank approximation. PCA uses exactly this, through the covariance eigendecomposition or the SVD of the data. Units: ch04-matrix-p1, ch04-matrix-p2, ch10-dimensionality.
- **Inner products as geometry, including for random variables.** The inner product gives lengths, angles and orthogonality (ch03). Zero-mean random variables have covariance as inner product and correlation as cosine (ch06-p1). SVM margins and kernels use inner products between examples (ch12). Units: ch03-analytic, ch06-probability-p1, ch12-classification.
- **Gaussians are closed under linear operations.** Marginals, conditionals, products and linear maps stay Gaussian with matrix formulas for the parameters. This makes Bayesian linear regression and probabilistic PCA solvable in closed form. Units: ch06-probability-p1, ch06-probability-p2, ch09-linear, ch10-dimensionality.
- **From maximum likelihood to MAP to full Bayes.** ch08 sets out the estimation options; a Gaussian prior acts as a regularizer; conjugate priors keep updates simple. ch09 works this out for regression. ch11 notes that ML for GMMs can overfit and gives only a point estimate. Units: ch06-probability-p2, ch08-when, ch09-linear, ch11-density.
- **Optimizing objectives with gradients and duality.** Gradients, Jacobians and backpropagation (ch05) feed gradient descent and SGD (ch07). Lagrange multipliers and duality appear in PCA's variance derivation, the GMM weight updates, and the SVM dual. Units: ch05-vector, ch07-continuous, ch10-dimensionality, ch11-density, ch12-classification.
- **Latent variables and generalization.** Hidden variables explain responsibilities in GMMs and the codes in probabilistic PCA. Overfitting and regularization recur from ch01 through regression and SVMs. Units: ch08-when, ch10-dimensionality, ch11-density, ch01-introduction, ch09-linear, ch12-classification.

## How to read it
- **Order.** Part I chapters mostly build on each other, and Part II chapters can be read in any order (ch01). The book can be read bottom-up or top-down.
- **Linear algebra to PCA path.** The catalog focus is ch02, ch03 (projections and rotations), ch04 (eigen/SVD/approximation), 9.4 (maximum likelihood as projection) and ch10. These are the essential units for that path: ch02-linear-p1, ch02-linear-p2, ch03-analytic, ch04-matrix-p1, ch04-matrix-p2, ch10-dimensionality, and the projection section of ch09-linear.
- **Dependencies stated in the units.**
  - ch03 needs basis, independence and null space (ch02).
  - ch04-p2 needs the eigenvalues and spectral theorem from ch04-p1.
  - ch10 needs orthogonal projection, SVD and Eckart–Young, covariance, Lagrange multipliers (ch07) and Gaussian conditioning (only for the probabilistic §10.7).
  - ch09 needs matrix calculus, Gaussians, Bayes' theorem and projection.
  - ch07 needs ch05 (gradients, Hessians) and ch06 (expectation).
  - ch08 needs Bayes, Gaussians and conjugate priors.
  - ch11 and ch12 need Lagrange multipliers; ch12 also needs inner products, norms and projection.
- **Can wait on a first pass (for the linear algebra → PCA goal).** The units outside the catalog focus are ch05, ch06-p2, ch07, ch08, ch11 and ch12. Only the pieces they feed into ch09 and ch10 are needed: Lagrange multipliers, Gaussian closure and covariance. The ch04 phylogeny discussion and the rest of ch06 can be revisited later. This is a suggestion from the catalog focus and the stated prerequisites, not a claim made by the book.

## Concepts introduced
Where a concept appears under several spellings, one id is kept at its first appearance.

**ch01-introduction**
- [[machine-learning-three-components]], [[vector]], [[predictor]], [[training]], [[generalization]], [[utility-function]], [[four-pillars-of-ml]], [[gradient]]

**ch02-linear-p1**
- [[linear-combination]], [[linear-independence]], [[inverse-matrix]], [[pseudoinverse]], [[null-space]], [[basis]], [[krylov-subspace-methods]], [[system-of-linear-equations]], [[matrix-multiplication]], [[transpose]], [[gaussian-elimination]], [[row-echelon-form]], [[particular-and-general-solution]], [[minus-1-trick]], [[group]], [[vector-space]], [[vector-subspace]]

**ch02-linear-p2**
- [[span]], [[generating-set]], [[dimension]], [[rank]], [[linear-map]], [[isomorphism]], [[coordinate-vector]], [[matrix-as-transformation]], [[matrix-multiplication-as-composition]], [[change-of-basis]], [[matrix-equivalence-and-similarity]], [[column-space]], [[rank-nullity]], [[affine-subspace]], [[affine-mapping]]

**ch03-analytic**
- [[norm]], [[dot-inner-product]], [[inner-product-space]], [[positive-semidefinite-matrix]], [[metric-distance]], [[cauchy-schwarz-inequality]], [[cosine-similarity]], [[orthogonality]], [[orthonormal-basis-orthogonal-matrix]], [[orthogonal-complement]], [[projection]], [[least-squares]], [[gram-schmidt-and-qr]], [[rotation-matrix-givens]]

**ch04-matrix-p1**
- [[determinant]], [[trace]], [[laplace-expansion]], [[triangular-matrix]], [[characteristic-polynomial]], [[eigenvector-eigenvalue]], [[eigenspace-and-spectrum]], [[algebraic-geometric-multiplicity]], [[defective-matrix]], [[spectral-theorem]], [[cholesky-decomposition]], [[diagonalization]], [[adjacency-matrix]], [[markov-stochastic-matrix]]

**ch04-matrix-p2**
- [[singular-value-decomposition]], [[eckart-young-theorem]], [[rank-one-matrix-outer-product]], [[low-rank-approximation]], [[full-vs-reduced-vs-truncated-svd]], [[singular-value-equation]], [[matrix-phylogeny]], [[principal-component-analysis]]

**ch05-vector**
- No concept links listed.

**ch06-probability-p1**
- [[probability-space]], [[random-variable]], [[probability-distribution-law]], [[pmf-pdf-cdf]], [[sum-rule-marginalization]], [[product-rule]], [[bayes-theorem]], [[expected-value]], [[mean-median-mode]], [[covariance-matrix]], [[correlation]], [[empirical-mean-covariance]], [[raw-score-variance]], [[statistical-independence]], [[conditional-independence]], [[iid]]

**ch06-probability-p2**
- [[multivariate-gaussian]], [[gaussian-conditioning]], [[gaussian-product]], [[mixture-of-gaussians]], [[law-of-total-variance]], [[cholesky-sampling]], [[conjugate-prior]], [[beta-distribution]], [[bernoulli-binomial]], [[sufficient-statistic]], [[exponential-family]], [[log-partition-function]], [[sigmoid]], [[change-of-variables]], [[probability-integral-transform]]

**ch07-continuous**
- [[gradient-descent]], [[step-size]], [[momentum]], [[stochastic-gradient-descent]], [[condition-number]], [[preconditioner]], [[lagrangian-and-multipliers]], [[lagrangian-duality]], [[weak-strong-duality]], [[minimax-inequality]], [[convex-set-function]], [[linear-and-quadratic-program]], [[convex-conjugate]]

**ch08-when**
- [[model]], [[feature-map]], [[empirical-risk-minimization]], [[loss-function]], [[expected-risk]], [[overfitting]], [[underfitting]], [[regularization]], [[cross-validation]], [[nested-cross-validation]], [[maximum-likelihood-estimation]], [[maximum-a-posteriori-estimation]], [[bayesian-inference]], [[latent-variable-model]], [[directed-graphical-model]], [[d-separation]], [[model-evidence]], [[bayes-factor]], [[information-criteria]]

**ch09-linear**
- [[linear-regression]], [[likelihood]], [[feature-matrix-design-matrix]], [[rmse]], [[lasso]], [[bayesian-linear-regression]], [[posterior-predictive]], [[marginal-likelihood]], [[completing-the-square]], [[generalized-linear-model]], [[gaussian-process]]

**ch10-dimensionality**
- [[power-iteration]], [[maximum-variance-view-of-pca]], [[reconstruction-error]], [[principal-subspace]], [[standardization]], [[n-much-less-than-d-covariance-trick]], [[linear-auto-encoder]], [[probabilistic-pca]], [[latent-variable]]

**ch11-density**
- [[gaussian-mixture-model]], [[mixture-model]], [[responsibility]], [[em-algorithm]], [[one-hot-encoding]], [[ancestral-sampling]], [[lagrange-multiplier]], [[kernel-density-estimation]], [[k-means]]

**ch12-classification**
- [[hyperplane]], [[margin]], [[hard-margin-svm]], [[soft-margin-svm]], [[slack-variable]], [[hinge-loss]], [[zero-one-loss]], [[representer-theorem]], [[support-vector]], [[convex-hull]], [[kernel-trick]], [[gram-matrix]], [[quadratic-programming]], [[subgradient]]
