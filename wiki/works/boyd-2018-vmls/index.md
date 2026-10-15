---
id: boyd-2018-vmls/index
work: boyd-2018-vmls
type: work-map
units: [boyd-2018-vmls/ch01-vectors, boyd-2018-vmls/ch02-linear, boyd-2018-vmls/ch03-norm, boyd-2018-vmls/ch04-clustering, boyd-2018-vmls/ch05-linear, boyd-2018-vmls/ch06-matrices, boyd-2018-vmls/ch07-matrix, boyd-2018-vmls/ch08-linear, boyd-2018-vmls/ch09-linear, boyd-2018-vmls/ch10-matrix, boyd-2018-vmls/ch11-matrix, boyd-2018-vmls/ch12-least, boyd-2018-vmls/ch13-least, boyd-2018-vmls/ch14-least, boyd-2018-vmls/ch15-multi, boyd-2018-vmls/ch16-constrained, boyd-2018-vmls/ch17-constrained, boyd-2018-vmls/ch18-nonlinear, boyd-2018-vmls/ch19-constrained, boyd-2018-vmls/app-appendices]
---

# Boyd, S., & Vandenberghe, L. (2018). *Introduction to Applied Linear Algebra: Vectors, Matrices, and Least Squares*. Cambridge University Press. https://doi.org/10.1017/9781108583664

## In one paragraph
The book starts with vectors and matrices and builds a large part of data work from them. Vector operations give norms, distances, angles and correlation. These lead to clustering with k-means. Matrices represent linear functions, and matrix multiplication composes them. Independence, QR factorization and inverses lead to the main tool: least squares. Least squares fits data, classifies, trades off several objectives (regularization) and handles exact linear constraints. It also covers portfolios, control and state estimation. The last chapters extend the idea to nonlinear problems by repeatedly solving linear least squares problems. The work matters because it shows how far plain linear algebra goes in applications, while keeping track of the computational cost of each method.

## The path through the work
- [[boyd-2018-vmls/ch01-vectors]] — A vector is an ordered list of numbers, and four operations (addition, scaling, linear combination, inner product) already turn lists of numbers into a working language for positions, portfolios, images, text and cash flows, at a cost of order n flops (floating point operations) per operation.
- [[boyd-2018-vmls/ch02-linear]] — A scalar-valued function of a vector is linear exactly when it is an inner product with one fixed vector, and affine functions (linear plus a constant) are the form taken by first-order Taylor approximations and regression models.
- [[boyd-2018-vmls/ch03-norm]] — The Euclidean norm measures the size of a vector, and from it come distance, standard deviation, angle and correlation, with the Cauchy–Schwarz inequality keeping the correlation between −1 and 1.
- [[boyd-2018-vmls/ch04-clustering]] — Clustering splits $N$ vectors into $k$ groups by minimising the mean squared distance to group representatives, and the k-means algorithm does this heuristically by alternating "assign to nearest representative" and "replace each representative by its group mean".
- [[boyd-2018-vmls/ch05-linear]] — A list of vectors is linearly independent when only the all-zero coefficients combine them to zero; this makes coefficients unique, caps the list size at $n$ for $n$-vectors, and the Gram–Schmidt algorithm tests it.
- [[boyd-2018-vmls/ch06-matrices]] — A matrix is a rectangular table of numbers that can be read by rows or by columns, and the product $y = Ax$ is both a set of row inner products and a linear combination of the columns of $A$.
- [[boyd-2018-vmls/ch07-matrix]] — Many useful operations (rotating, picking entries, differencing along graph edges, convolving signals) are just matrix–vector products with a special, easily described matrix.
- [[boyd-2018-vmls/ch08-linear]] — Every linear function of vectors is a matrix–vector product $f(x)=Ax$, and such functions serve as models (affine, Taylor, regression), while systems of linear equations $Ax=b$ cover interpolation, chemical balancing, diffusion and input–output.
- [[boyd-2018-vmls/ch09-linear]] — A system whose next state is a matrix times its current state (plus optional input and offset) can be simulated by repeated matrix–vector multiplication, and many real processes can be described this way, at least approximately.
- [[boyd-2018-vmls/ch10-matrix]] — Multiplying matrices means composing linear functions (do B, then A), and this one operation unifies inner and outer products, Gram matrices, powers, path counting, dynamics and QR factorization.
- [[boyd-2018-vmls/ch11-matrix]] — A matrix has a left inverse exactly when its columns are independent and a right inverse exactly when its rows are independent; for square matrices both coincide with the inverse $A^{-1}$, which solves $Ax=b$ and can be computed by QR factorization and back substitution.
- [[boyd-2018-vmls/ch12-least]] — When $Ax=b$ has no solution because $A$ is tall, minimizing $\|Ax-b\|^2$ gives a unique best compromise $\hat x=(A^TA)^{-1}A^Tb=A^\dagger b$, provided the columns of $A$ are linearly independent; the optimal residual is orthogonal to the columns of $A$.
- [[boyd-2018-vmls/ch13-least]] — Fitting a model that is linear in its parameters to data is a least squares problem θ̂ = A†yᵈ, and what matters is how well the fitted model predicts new data, which is judged by validation on held-out data rather than by training error alone.
- [[boyd-2018-vmls/ch14-least]] — Fit the ±1 labels by ordinary least squares, then predict the sign of the fitted value; for K classes, fit one such model per class and pick the largest fitted value.
- [[boyd-2018-vmls/ch15-multi]] — To make several squared-norm objectives small at once, minimize their weighted sum, which is an ordinary least squares problem on a stacked matrix. Adding secondary terms such as $\lambda\|x\|^2$ is sometimes called regularization.
- [[boyd-2018-vmls/ch16-constrained]] — Minimizing $\|Ax-b\|^2$ subject to linear equality constraints $Cx=d$ reduces to one square linear system (the KKT equations), whose coefficient matrix is invertible exactly when $C$ has independent rows and $\begin{bmatrix}A\\C\end{bmatrix}$ has independent columns.
- [[boyd-2018-vmls/ch17-constrained]] — Portfolio selection, optimal control and state estimation can each be written as a linearly constrained least squares problem; in control and estimation this is done by stacking the states and inputs (or noises) into one big vector.
- [[boyd-2018-vmls/ch18-nonlinear]] — To solve f(x)=0 or minimize ‖f(x)‖² for a non-affine f, repeatedly replace f by its affine approximation at the current point and solve a linear least squares problem, with a penalty on step length (Levenberg–Marquardt) to keep the approximation trustworthy.
- [[boyd-2018-vmls/ch19-constrained]] — Equality-constrained nonlinear least squares can be attacked heuristically by solving a sequence of ordinary nonlinear least squares problems with Levenberg–Marquardt, and the augmented Lagrangian method does this more reliably than the plain penalty method.
- [[boyd-2018-vmls/app-appendices]] — The appendices give the book's notation, the flop counts of its algorithms, the small calculus toolkit (gradient, Jacobian, Taylor approximation, KKT conditions) behind nonlinear least squares, and pointers to further study.

## Big ideas across units
- **Linear functions are matrices.** Superposition characterizes linear functions. A linear scalar function is an inner product, a vector-valued one is $Ax$, and the columns are the function's values at the unit vectors. Matrix products compose these functions. Units: ch02, ch06, ch07, ch08, ch10.
- **Distance and geometry drive data methods.** The norm gives distance, angle and correlation. These in turn give nearest neighbours and k-means, and the residual norm that least squares minimizes. Units: ch03, ch04, ch12.
- **Independence, orthogonality and QR are the engine.** Independence gives unique coefficients and bases. Gram–Schmidt becomes the QR factorization. QR supports inverses, least squares, constrained least squares and the Levenberg–Marquardt steps. Units: ch05, ch10, ch11, ch12, ch16, ch18.
- **Least squares is the central tool.** The normal equations and pseudo-inverse solve tall systems. Data fitting, classification, multi-objective, constrained and nonlinear problems each reduce to it or extend it. Units: ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19.
- **Generalization and validation.** Training error alone misleads. Held-out data, cross-validation and back-testing are used to choose models, features and weights such as $\lambda$. Units: ch13, ch14, ch15, ch17.
- **Trade-offs and regularization.** Weighted sums of objectives give Pareto optimal points and trade-off curves. Secondary terms act as regularization (Tikhonov, ridge). Constraints are the "infinite weight" case. Units: ch15, ch16, ch17.
- **Linear approximation of nonlinear things.** Affine functions approximate differentiable ones through the Taylor approximation and the Jacobian. Nonlinear least squares repeats this at each step. Units: ch02, ch08, ch18, ch19, app-appendices.
- **Dynamics and stacking.** A state recursion $x_{t+1}=Ax_t+\dots$ is iterated matrix multiplication, and powers of $A$ propagate it. Stacking the states and inputs turns control and estimation into constrained least squares. Units: ch09, ch10, ch17, ch19.
- **Cost counted in flops, and sparsity helps.** Every method comes with a flop count, and sparse structure reduces it. Units: ch01, ch03, ch06, ch10, ch11, ch12, ch16, ch17, app-appendices.

## How to read it
- **Essential.** The catalog's focus list names ch03, ch04, ch07, ch09, ch12, ch13, ch14 and ch15. Several of these depend on units outside the list: ch12 needs ch05, ch10 and ch11 (independence, QR, pseudo-inverse), and ch09 needs the matrix basics of ch06.
- **Foundations.** ch01 and ch02 need no matrices. ch03 needs only vectors, and ch04 needs ch03. ch05 leads into ch06 and ch10, then ch11, then ch12.
- **Dependencies in the least squares sequence.** ch13 needs ch12 and ch03 (RMS, correlation). ch14 builds on ch13. ch15 builds on ch12. ch16 builds on ch12, and ch17 builds on ch16 and ch9.
- **Nonlinear part.** ch18 uses ch12 and ch15, plus the Jacobian and Taylor material from ch08 and appendix C. ch19 needs ch18 and the Lagrange multiplier ideas (ch16, appendix C.3).
- **Can be skipped on a first pass.** ch08, ch16–ch19 and the appendices are outside the focus list. The appendices are best used as a reference when needed: for notation, flop counts, and the calculus behind ch18–ch19. ch19 is the most specialized unit, since it depends on both ch16 and ch18.

## Concepts introduced
Near-duplicate ids that appear in several units are merged and listed under the first unit.

**ch01:** [[vector]], [[linear combination]], [[dot (inner) product]] (also written [[dot-inner-product]]), [[affine-convex-combination]], [[standard-unit-vector]], [[sparse-vector]], [[block-vector]], [[flop-count-complexity]] (also [[flop-count]], new in ch03), [[orthogonality]]

**ch02:** [[linear-map-transformation]], [[superposition]], [[affine-function]], [[affine-combination]], [[taylor-approximation-first-order]], [[gradient]], [[regression-model]], [[linear-independence]], [[basis]]

**ch03:** [[norm]], [[cosine-similarity]], [[root-mean-square]], [[euclidean-distance]], [[triangle-inequality]], [[cauchy-schwarz-inequality]], [[chebyshev-inequality]], [[standard-deviation]], [[standardization]], [[correlation-coefficient]], [[nearest-neighbor]]

**ch04:** [[clustering]], [[cluster-assignment-vector]], [[group-representative-centroid]], [[clustering-objective-jclust]], [[k-means-algorithm]], [[heuristic-algorithm]], [[imputation-missing-entries]]

**ch05:** [[dimension]], [[independence-dimension-inequality]], [[orthonormal basis / orthogonal matrix]], [[orthonormal-expansion-formula]], [[Gram–Schmidt and QR]] (also [[gram-schmidt-qr]], [[gram-schmidt-and-qr]]), [[net-present-value]]

**ch06:** [[matrix]], [[matrix-vector-multiplication]], [[block-matrix]], [[matrix-transpose]], [[symmetric-matrix]], [[sparse-matrix]], [[diagonal-triangular-matrix]], [[identity matrix]], [[adjacency matrix]], [[difference-and-running-sum-matrices]], [[vandermonde-matrix]], [[flop-count-matrix-ops]]

**ch07:** [[matrix as transformation]] (also [[matrix-as-transformation]]), [[linear map / transformation]], [[projection]], [[change of basis]], [[selector-matrix]], [[permutation-matrix]], [[incidence matrix]] (also [[incidence-matrix]]), [[flow-conservation]], [[dirichlet-energy]], [[graph Laplacian]] (also [[graph-laplacian]]), [[convolution]], [[toeplitz-matrix]], [[point-spread-function]]

**ch08:** [[taylor-approximation-jacobian]], [[system-of-linear-equations]], [[overdetermined-underdetermined]]

**ch09:** [[linear dynamical system]], [[state / trajectory]], [[time-invariant system]], [[input, offset]], [[Markov model / K-Markov (auto-regressive) model]], [[simulation]], [[Euler method / discretization]], [[matrix multiplication as composition]]

**ch10:** [[matrix-multiplication-definition]], [[non-commutativity-of-matrix-product]], [[block-matrix-multiplication]], [[rank-one matrix / outer product]], [[gram-matrix]], [[flop-count-matrix-product]], [[matrix-power]], [[chain-rule-derivative-matrix]], [[state-feedback-closed-loop]]

**ch11:** [[inverse matrix]], [[left-inverse]], [[right-inverse]], [[singular-matrix]], [[dual-basis]], [[back-substitution]], [[factor-solve-method]], [[pseudoinverse]], [[lagrange-polynomials]]

**ch12:** [[least-squares]] (also [[least squares]]), [[residual]], [[normal-equations]], [[orthogonality-principle]], [[matrix-least-squares]]

**ch13:** [[basis-function-feature-map]], [[linear-in-parameters-model]], [[residual-rms-error]], [[auto-regressive-model]], [[log-transform-relative-error]], [[generalization]], [[out-of-sample-validation]], [[overfitting]], [[cross-validation]], [[look-ahead-leakage]], [[feature-engineering]], [[one-hot-encoding]], [[generalized-additive-model]]

**ch14:** [[boolean-classifier]], [[confusion-matrix]], [[classification-metrics]], [[least-squares-classifier]], [[decision-threshold]], [[roc-curve]], [[one-versus-others-classifier]]

**ch15:** [[multi-objective-least-squares]], [[weighted-sum-objective]], [[stacked-least-squares]], [[pareto-optimality]] (also [[pareto-optimal]], ch17), [[optimal-trade-off-curve]], [[regularization]], [[tikhonov-regularization]], [[ridge-regression]], [[regularization-path]], [[first-difference-matrix]], [[gram-caching]], [[kernel-trick]], [[big-times-small-squared]]

**ch16:** [[constrained-least-squares]], [[feasible-point]], [[lagrange-multipliers]] (also [[lagrange-multiplier]], ch19), [[kkt-equations]], [[kkt-matrix-invertibility]], [[least-norm-problem]]

**ch17:** [[portfolio-optimization]], [[leverage-portfolio]], [[two-fund-theorem]], [[back-testing-validation]], [[linear-quadratic-control]], [[state-feedback-control]], [[state-estimation]], [[stacking-block-matrices]], [[sparse-structure-cost]]

**ch18:** [[nonlinear-least-squares]], [[jacobian-matrix]], [[optimality-condition-nls]], [[gauss-newton-algorithm]], [[newton-algorithm]], [[levenberg-marquardt]] (also [[levenberg-marquardt-algorithm]], ch19), [[trust-parameter]], [[warm-start]], [[sigmoid-function]], [[loss-function]], [[orthogonal-distance-regression]]

**ch19:** [[constrained-nonlinear-least-squares]], [[optimality-condition-constrained]], [[penalty-method]], [[augmented-lagrangian-method]], [[nonlinear-control]]

**app-appendices:** [[jacobian-derivative-matrix]], [[taylor-approximation]], [[chain-rule]], [[gradient-condition-for-minimization]], [[kkt-conditions]], [[boolean-least-squares]]
