---
id: prince-2023-udl/ch22-mathematics
work: prince-2023-udl
unit: Appendix B — Mathematics (unit id "ch22")
pages: 440–448
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Appendix B: Mathematics (functions, matrices, matrix calculus)

## L0 — One line
This appendix is a reference sheet of the function, linear-algebra and matrix-derivative tools that the deep-learning text relies on.

## L1 — The gist (≤ 120 words)
The appendix collects background mathematics for the main text. It covers kinds of function mappings, Lipschitz constants, convexity, special functions, binomial coefficients and autocorrelation. It then covers vectors, matrices and tensors: norms, products, inverses, subspaces, singular values and eigenvalues, determinant and trace. It also covers special matrices (diagonal, triangular, orthogonal, permutation), linear equations in matrix form, and matrix calculus. Several sections show how a matrix scales vectors, and how special matrices can make some computations cheaper.

**Prerequisites:** high-school algebra, summation notation, the idea of a derivative, a first look at vectors and matrices.

## L2 — Key ideas
- Functions can be injective (one-to-one), surjective (every target element is reached) or bijective (both). A diffeomorphism is a bijection that is differentiable in both directions (p. 440).
- A Lipschitz constant β bounds how fast a function can change. It combines under composition (≤ β₁β₂) and addition (≤ β₁+β₂) (p. 440).
- Gradient descent is guaranteed to find the global minimum of a function that is convex and defined on a convex region (p. 441).
- Special functions used later: exp, log, the gamma function (which extends the factorial), the Dirac delta (a unit-area spike at zero with a key integral property, B.3), and Stirling's approximation of the factorial (p. 441).
- Matrix facts with shapes: transpose reverses products, and products need matching inner dimensions (pp. 443–444).
- A 2×2 matrix maps the unit circle to an ellipse. The radii of the ellipse's axes correspond to the magnitudes of the matrix's singular values. The spectral norm (the largest absolute eigenvalue) tells us about the Lipschitz constant (p. 445).
- Determinant and trace summarise the eigenvalues (product and sum) and obey simple rules (p. 446).
- Diagonal, triangular, orthogonal and permutation matrices can make inverses and determinants cheaper to compute (pp. 446–447).
- Matrix calculus: for y = Ax, ∂y/∂x = Aᵀ, using the Jacobian shape D_x × D_y (the matrix whose (i, j) entry is ∂y_j/∂x_i) (p. 448).

## L3 — Walkthrough

### B.1 Functions
- Injection: one-to-one, with possibly unreached elements in the target. Surjection: every target element is reached, possibly many-to-one. Bijection: both. Diffeomorphism: a bijection whose forward and reverse maps are differentiable (p. 440).

**B.1.1 Lipschitz constant.** f is Lipschitz continuous if for all z₁, z₂:
$$\|f[z_1]-f[z_2]\|\le \beta\|z_1-z_2\|. \tag{B.1}$$
- β is the Lipschitz constant, the maximum gradient (how fast f can change) for the chosen distance (p. 440).
- If β < 1 the function is a contraction mapping, and Banach's theorem gives the inverse for any point (p. 440).
- Composition has constant ≤ β₁β₂. Addition has constant ≤ β₁+β₂ (p. 440).
- For f[z] = Az + b with Euclidean distance, the constant is the maximum eigenvalue of A (p. 440).

*Intuition note:* β says "output distance can grow at most β times input distance". Stacking functions multiplies these limits.

**B.1.2 Convexity.** A function is convex if a line between any two points on it lies above it. It is concave if the line lies below. By definition, convex (concave) functions have at most one minimum (maximum) (p. 441).
- A region of $\mathbb{R}^D$ is convex if a line between two boundary points does not meet the boundary elsewhere (p. 441).
- Gradient descent is guaranteed to find the global minimum of any function that is convex and defined on a convex region (p. 441).

**B.1.3 Special functions** (p. 441).
- exp: maps ℝ to non-negative numbers, y = eˣ.
- log: the inverse of exp. All logarithms in the book are natural (base e).
- Gamma function:
$$\Gamma[x]=\int_0^\infty t^{x-1}e^{-t}\,dt, \tag{B.2}$$
 which extends the factorial: Γ[x] = (x−1)! for x ∈ {1, 2, …}.
- Dirac delta δ[z]: total area one, all at z = 0. A dataset of N points can be seen as a sum of N deltas at the points, each scaled by 1/N. Key property:
$$\int f[\mathbf x]\,\delta[\mathbf x-\mathbf x_0]\,d\mathbf x=f[\mathbf x_0]. \tag{B.3}$$

**B.1.4 Stirling's formula** (p. 441) approximates the factorial (and hence the gamma function). The caption of figure B.2 says Stir[x] is defined for every real value (p. 442):
$$x!\approx\sqrt{2\pi x}\left(\frac{x}{e}\right)^{x}. \tag{B.4}$$

### B.2 Binomial coefficients
$\binom{n}{k}$ ("n choose k") is the number of ways to pick an unordered subset of k items from n, without replacement (p. 442):
$$\binom nk=\frac{n!}{k!\,(n-k)!}. \tag{B.5}$$

**B.2.1 Autocorrelation.** For continuous f, with τ the time lag (pp. 442–443):
$$r[\tau]=\int_{-\infty}^{\infty} f[t+\tau]\,f[t]\,dt. \tag{B.6}$$
- It is sometimes normalised by r[0], so that r[0] = 1.
- A slowly and predictably changing function has an autocorrelation that falls slowly with lag. A fast, unpredictable one falls quickly to zero (p. 443).

### B.3 Vectors, matrices, tensors
- A vector $\mathbf x\in\mathbb R^D$ is a column of D numbers. A matrix $\mathbf Y\in\mathbb R^{D_1\times D_2}$ has D₁ rows and D₂ columns. A tensor is an N-dimensional array. Deep-learning APIs store all three as "tensors" (p. 443).

**B.3.1 Transpose.** $\mathbf A^T\in\mathbb R^{D_2\times D_1}$ reflects A about the diagonal. Also (p. 443):
$$(\mathbf{AB})^T=\mathbf B^T\mathbf A^T. \tag{B.7}$$

**B.3.2 Norms.** For real p > 1 (p. 443):
$$\|\mathbf z\|_p=\Big(\sum_{d=1}^{D}|z_d|^p\Big)^{1/p}. \tag{B.8}$$
- p = 2 is the Euclidean norm (the length), the usual case in deep learning. p = ∞ gives the largest absolute entry (p. 443).
- Frobenius norm of a matrix (p. 444):
$$\|\mathbf Z\|_F=\Big(\sum_{i=1}^{I}\sum_{j=1}^{J}|z_{ij}|^2\Big)^{1/2}. \tag{B.9}$$

**B.3.3 Matrix product.** For $\mathbf A\in\mathbb R^{D_1\times D_2}$, $\mathbf B\in\mathbb R^{D_2\times D_3}$, $\mathbf C=\mathbf{AB}\in\mathbb R^{D_1\times D_3}$ (p. 444):
$$C_{ij}=\sum_{d=1}^{D_2}A_{id}B_{dj}. \tag{B.10}$$

**B.3.4 Dot product** (p. 444):
$$\mathbf a^T\mathbf b=\mathbf b^T\mathbf a=\sum_{d=1}^D a_db_d, \tag{B.11}$$
$$\mathbf a^T\mathbf b=\|\mathbf a\|\|\mathbf b\|\cos[\theta]. \tag{B.12}$$
The text says it "can be shown" that (B.12) holds, with θ the angle between the vectors, and gives no proof.

**B.3.5 Inverse.** A square A may have an inverse with $\mathbf A^{-1}\mathbf A=\mathbf{AA}^{-1}=\mathbf I$. Without one, it is singular (p. 444).
- For square invertible A, B (p. 444):
$$(\mathbf{AB})^{-1}=\mathbf B^{-1}\mathbf A^{-1}. \tag{B.13}$$
- Inverting a D×D matrix generally costs $\mathcal O[D^3]$. It is cheaper for diagonal, orthogonal and triangular matrices (p. 444).

**B.3.6 Subspaces.**
- If A has fewer columns than rows (D₂ < D₁, "portrait"), Ax reaches only the linear subspace spanned by A's columns, the column space (pp. 444–445).
- For a landscape matrix, the x with Ax = 0 form the nullspace (p. 445).

**B.3.7 Eigenspectrum.**
- A 2×2 matrix maps the unit circle to an ellipse (figure B.3, with A = [[2, −1],[3.1, 1.5]]). The axis radii are the magnitudes of the singular values λ₁, λ₂ (p. 445).
- In D dimensions a spheroid maps to an ellipsoid with D principal axes. For symmetric square matrices the eigenvalues equal the singular values (p. 445).
- The spectral norm is the largest absolute eigenvalue. It is the largest change in magnitude for a unit-length vector and so tells us about the Lipschitz constant (p. 445).
- The set of eigenvalues is sometimes called the eigenspectrum. It tells us about the scaling applied by the matrix across all directions, and can be summarised by the determinant and trace (p. 445).

*Intuition note:* A matrix stretches space by different amounts in different directions. The largest stretch is the most it can magnify any vector.

**B.3.8 Determinant and trace.**
- The determinant |A| = det[A] is the product of the eigenvalues. It relates to the average scaling. Small |det| tends to shrink vector norms, large |det| to enlarge them. If A is singular, det = 0 and at least one direction maps to the origin (pp. 445–446).
$$|\mathbf A^T|=|\mathbf A|,\quad |\mathbf{AB}|=|\mathbf A||\mathbf B|,\quad |\mathbf A^{-1}|=1/|\mathbf A|. \tag{B.14}$$
- The trace is the sum of the diagonal entries, or equally the sum of the eigenvalues (p. 446):
$$\mathrm{trace}[\mathbf A^T]=\mathrm{trace}[\mathbf A],\ \mathrm{trace}[\mathbf{AB}]=\mathrm{trace}[\mathbf{BA}],\ \mathrm{trace}[\mathbf A+\mathbf B]=\mathrm{trace}[\mathbf A]+\mathrm{trace}[\mathbf B],\ \mathrm{trace}[\mathbf{ABC}]=\mathrm{trace}[\mathbf{BCA}]=\mathrm{trace}[\mathbf{CAB}]. \tag{B.15}$$
 Only cyclic permutations are safe: in general trace[ABC] ≠ trace[BAC] (p. 446).

### B.4 Special matrices
Inverse and determinant cost $\mathcal O[D^3]$ in general. Special structure can make them cheaper (p. 446).
- **B.4.1 Diagonal:** if all diagonal entries are non-zero, the inverse is diagonal with entries 1/d_ii. The determinant is the product of the diagonal. The identity has inverse I and determinant 1 (p. 446).
- **B.4.2 Triangular** (lower: non-zeros on or below the diagonal; upper: on or above): inverted in $\mathcal O[D^2]$; the determinant is the product of the diagonal (pp. 446–447).
- **B.4.3 Orthogonal:** rotations and reflections. All eigenvalues have magnitude one, the determinant is ±1, and $\mathbf A^{-1}=\mathbf A^T$ (p. 447).
- **B.4.4 Permutation:** exactly one non-zero entry in each row and column, and every such entry is 1. It is a special case of an orthogonal matrix, so the inverse is the transpose and det = ±1 (p. 447):
$$\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix}\begin{bmatrix}a\\b\\c\end{bmatrix}=\begin{bmatrix}b\\c\\a\end{bmatrix}. \tag{B.16}$$
- **B.4.5 Linear algebra:** linear functions have the form $f[z_1,\dots,z_D]=\phi_1z_1+\dots+\phi_Dz_D$ (B.17). Adding a constant φ₀ makes it technically affine. The book calls this "linear" anyway (p. 447).
- **B.4.6 Matrix form:** three linear functions (B.18), $y_i=\phi_{i0}+\sum_{j}\phi_{ij}z_j$, are written as $\mathbf y=\boldsymbol\phi_0+\boldsymbol\Phi\mathbf z$ (B.19) (pp. 447–448).

### B.5 Matrix calculus (p. 448)
The three derivative forms are:
- y ∈ ℝ, x ∈ ℝ^D: ∂y/∂x is a D-vector with entries ∂y/∂x_i.
- y ∈ ℝ^{D_y}, x ∈ ℝ^{D_x}: ∂y/∂x is a D_x × D_y matrix with (i, j) entry ∂y_j/∂x_i. This is the Jacobian.
- y ∈ ℝ^{D_y}, X ∈ ℝ^{D₁×D₂}: ∂y/∂X is a 3D tensor with entries ∂y_i/∂x_jk.

Examples:
$$y=ax\ \to\ \frac{\partial y}{\partial x}=a, \tag{B.20}$$
$$\mathbf y=\mathbf A\mathbf x\ \to\ \frac{\partial \mathbf y}{\partial \mathbf x}=\mathbf A^T. \tag{B.21}$$

*Intuition note:* Vector derivatives look like scalar ones, but the transpose appears because the Jacobian is indexed input-first, so its (i, j) entry is ∂y_j/∂x_i = A_ji (added step).

## Toy example (ours, not from the text)
Take $\mathbf A=\begin{bmatrix}1&2\\0&3\end{bmatrix}$, so $y_1=x_1+2x_2$ and $y_2=3x_2$.
- Triangular: det = 1·3 = 3. Trace = 1+3 = 4.
- Inverse: $\mathbf A^{-1}=\begin{bmatrix}1&-2/3\\0&1/3\end{bmatrix}$. Check: row 1 × columns = (1·1+2·0, 1·(−2/3)+2·(1/3)) = (1, 0). Row 2 gives (0, 3·1/3) = (0, 1). So $\mathbf{AA}^{-1}=\mathbf I$. Also |A⁻¹| = 1·(1/3) = 1/3 = 1/|A| (B.14).
- Jacobian (B.21): entry (i, j) = ∂y_j/∂x_i. So (1,1)=1, (1,2)=∂y₂/∂x₁=0, (2,1)=∂y₁/∂x₂=2, (2,2)=3. This gives $\begin{bmatrix}1&0\\2&3\end{bmatrix}=\mathbf A^T$.
- (added step) The characteristic polynomial is (1−λ)(3−λ), so the eigenvalues are 1 and 3. Their product is 3 = det and their sum is 4 = trace, matching B.3.8.

## Concepts
- [[lipschitz-constant]] (new) — bound β on how much a function can stretch distances (p. 440)
- [[convexity]] (new) — a function whose chords lie above it; convex on a convex region gives guaranteed global minimum by gradient descent (p. 441)
- [[dirac-delta]] (new) — unit-area spike at zero; key integral property (B.3) (p. 441)
- [[stirling-approximation]] (new) — approximation of x!, defined for every real x (pp. 441–442)
- [[matrix-norm-and-spectrum]] (new) — Euclidean, Frobenius norms; singular values, eigenvalues, spectral norm (pp. 443–445)
- [[determinant-trace]] (new) — product and sum of eigenvalues (pp. 445–446)
- [[orthogonal-matrix]] (new) — rotation/reflection with A⁻¹ = Aᵀ (p. 447)
- [[jacobian]] (new) — D_x × D_y matrix of ∂y_j/∂x_i (p. 448)

## Canonical instances
- [[dataset-as-delta-mixture]] (new) — a dataset of N points viewed as N deltas weighted 1/N (p. 441)
- [[permutation-matrix-example]] (new) — the 3×3 matrix sending (a,b,c) to (b,c,a) (p. 447)

## Bridges (candidates)
- [same-math] Jacobian ∂y/∂x = Aᵀ for y = Ax ↔ backpropagation through a linear layer: the same transpose-of-weights rule.
- [structural-analogy] Spectral norm bounding Lipschitz behaviour ↔ stability of repeated layer products in deep networks: large stretch compounds across layers.
- [structural-analogy] Dataset as sum of delta functions ↔ empirical distribution in statistics.

## Questions this raises
- B.1.1 says the Lipschitz constant of a linear map is the "maximum eigenvalue". How does this match the "largest absolute eigenvalue" of B.3.7 for matrices that are not symmetric?
- Why does gradient descent lose its global-minimum guarantee when the function is not convex?
- How do the O[D³] and O[D²] inversion costs change what is practical for large D?
- Why is the cyclic property of the trace enough for derivations that rearrange matrix products?

## Reading notes
- Printed page = pdf − 14 (pdf 454 = p. 440).
- The text layer flattens several displayed equations and matrices (e.g. B.8, B.16, B.19); all equations were checked against the page images.
- B.1.1 says "maximum eigenvalue" while B.3.7 says "largest absolute eigenvalue". Both are kept as printed.
- B.3.2 requires p > 1 but then also mentions p = ∞.
- B.4.5: the book calls affine functions "linear" by convention.
- These pages contain no exercises. Figures B.1–B.3 are described through their captions (for B.3, also the matrix printed in the figure).
