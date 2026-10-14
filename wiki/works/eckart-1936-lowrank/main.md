---
id: eckart-1936-lowrank/main
work: eckart-1936-lowrank
unit: paper
pages: 211-218
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# The Approximation of One Matrix by Another of Lower Rank (Eckart & Young, 1936)

## L0 — One line
The best rank-$r$ least-squares approximation of a matrix is found by writing it in canonic form (diagonal multipliers between two orthogonal matrices) and keeping only the $r$ largest multipliers.

## L1 — The gist (≤ 120 words)
Factor theory assumes that an $n\times N$ score matrix can be approximated by a matrix of lower rank $r$. The paper asks which rank-$r$ matrix is closest to a given matrix, when closeness is the sum of squared element differences. The answer: write $\alpha=u'\lambda U$ with orthogonal $u,U$ and non-negative diagonal $\lambda$. Keep the $r$ largest diagonal entries and set the rest to zero. The squared error is then the sum of the squares of the discarded entries. The solution is unique unless $\lambda_r=\lambda_{r+1}$. The best rank-$r$ approximation $\beta$ also gives, through $\beta\beta'$ and $\beta'\beta$, the best rank-$r$ approximations to the two correlation matrices. In modern terms this is truncated-SVD low-rank approximation (canon link; the paper itself does not use that name).

**Prerequisites:** matrix transpose and product; orthogonal matrices ($uu'=1$); rank; diagonal matrices; symmetric and skew-symmetric matrices; minimising a function by setting its variation to zero.

## L2 — Key ideas (5–10 bullets)
- The scalar product $(\alpha,\beta)=\sum\alpha_{ij}\beta_{ij}$ defines length and distance between matrices. "Closest" then means least squares with equal weight on every element (pp. 211–212).
- Theorem I (stated, not proved): every real matrix has a canonic resolution $\alpha=u'\lambda U$, with orthogonal $u,U$ and $\lambda$ diagonal with no negative entries (p. 213).
- The multipliers and $u$ can be computed from the symmetric matrix $\alpha\alpha'$, whose characteristic values are the squares of the multipliers (p. 213).
- A minimum of the distance forces $\alpha\beta'$ and $\beta'\alpha$ to be symmetric. Theorem II then lets $\alpha$ and $\beta$ be diagonalised by the same $u,U$ (p. 215).
- The problem reduces to $\sum_i(\lambda_i-\mu_i)^2$ with only $r$ nonzero $\mu_i$. The authors give the solution as keeping the $r$ largest $\lambda_i$ and zeroing the rest, calling it "obvious" without proof (pp. 215–216).
- The minimum squared error is $\sum_{i=r+1}^{R}\lambda_i^2$. The smallest upper bound for the error is $l(1-r/R)^{1/2}$ (p. 216).
- The best rank-$r$ approximation to the score matrix also yields the best rank-$r$ approximations to $\alpha\alpha'$ and $\alpha'\alpha$ (p. 216).
- The authors ask whether the canonic components in $\beta$ may be interpreted as factors; they call this a hypothetical interpretation, and the multipliers do not match factor theory's accepted postulates. They discuss a two-group scenario that would lead one to accept the reading, then reject the simple variance reading as untenable (pp. 216–218).

## L3 — Walkthrough

### Introduction (pp. 211–212)
- **Setting.** $N$ individuals take $n$ tests, giving an $n\times N$ score matrix $\alpha$. Factor theory postulates that $\alpha$ is adequately approximated by a matrix $\beta$ of rank $r$, with $r$ below the smaller of $n$ and $N$ (p. 211).
- **Problem.** Find the rank-$r$ matrix $\beta$ that most closely approximates a given $\alpha$ of higher rank $R$. The authors say the solution is simple in theory, but the numerical work in applications may be prohibitive (p. 211).
- **Scalar product** of two $n\times N$ matrices:
$$(\alpha,\beta)=\sum_{i=1}^{n}\sum_{j=1}^{N}\alpha_{ij}\beta_{ij}\tag{1}$$
It has the usual properties (pp. 211–212):
$$(\alpha,\beta)=(\beta,\alpha)\tag{2}$$
$$(\alpha\pm\beta,\gamma)=(\alpha,\gamma)\pm(\beta,\gamma)\tag{3}$$
$$(x\alpha,\beta)=x(\alpha,\beta)\ \ (x\text{ a number})\tag{4}$$
$$(\alpha,\alpha)>0\ \text{ if }\alpha\neq0\tag{5}$$
- **Length and distance.** The length $l$ of $\alpha$ is defined by $l^2=(\alpha,\alpha)$. Frobenius called $l^2$ the "span". The length of $\alpha-\beta$ is the distance from $\alpha$ to $\beta$ (p. 212).
- **Precise problem.** Find the rank-$r$ matrix $\beta$ such that no other rank-$r$ matrix is closer to $\alpha$. This is a least-squares solution with every element weighted equally (p. 212).

### Preliminary theorems and remarks (pp. 212–214)
- **Notation.** Lowercase $a,b,u$ are $n\times n$. Capitals $A,B,U$ are $N\times N$. Greek $\alpha,\beta$ are $n\times N$. The transpose of $\alpha$ is $\alpha'$ (p. 212).
- **Identities.** The paper states these as holding (p. 212):
$$(\alpha,\beta)=(\alpha',\beta')\tag{6}$$
$$(a\alpha,\beta)=(\alpha,a'\beta)=(\alpha,\beta\alpha')\tag{7}$$
(Here, as printed, the last term of (7) is $(\alpha,\beta\alpha')$; the image shows $\alpha$ where $A$ would be expected, so I report it as printed.)
$$(\alpha A,\beta)=(\alpha,\beta A')=(A,\alpha'\beta)\tag{8}$$
- **Orthogonal invariance.** From (7) and (8): if $u,U$ are orthogonal ($uu'=u'u=1_n$, $UU'=U'U=1_N$), then
$$(u\alpha U',u\beta U')=(\alpha,\beta)\tag{9}$$
- **Proposition.** If $(a,b)=0$ for all symmetric (skew-symmetric) $b$, then $a$ is skew-symmetric (symmetric) (p. 212).
- **Theorem I** (generalising a known theorem on square matrices; not proved here, p. 212). For any real matrix $\alpha$, orthogonal $u$ and $U$ exist such that $\lambda=u\alpha U'$ is a real diagonal matrix with no negative elements (p. 213).
  - A diagonal matrix, square or rectangular, has $\lambda_{ij}=0$ unless $i=j$. If it is rectangular, some rows or columns are entirely zero (p. 213).
  - Equivalent form, the **canonic resolution**:
$$\alpha=u'\lambda U\tag{10}$$
  - If $n<N$, $\lambda$ has $N-n$ zero columns, so $\alpha$ depends only on the first $n$ rows of $U$ (p. 213).
  - Let $v$ be the diagonal $n\times n$ matrix of the first $n$ columns of $\lambda$. Let $\omega$ be the $n\times N$ matrix of the first $n$ rows of $U$. Then
$$\alpha=u'v\omega\tag{10.1}$$
  - Shapes: $u',v:n\times n$; $\omega:n\times N$. Also $\omega\omega'=1_n$ but $\omega'\omega\neq1_N$. The authors prefer (10.1) for numerical work and (10) for formal manipulation (p. 213).
- **Computing $u$ and $\lambda$.** Put $a=\alpha\alpha'$ ($n\times n$), which is closely related to the matrix of correlation coefficients of the tests (p. 213):
$$a=\alpha\alpha'=u'\lambda\lambda'u=u'v^2u$$
  - Since $\lambda\lambda'=v^2$ is diagonal, $u$ is one of the orthogonal matrices that diagonalise $a$. Its rows are unit vectors along the principal axes of $a$. The squares of the diagonal elements of $v$ are the characteristic values of $a$, which therefore cannot be negative (p. 213).
  - If no characteristic value is zero, $v$ has an inverse and $\omega=v^{-1}u\alpha$. The other rows of $U$ are not needed but could be found (pp. 213–214).
- **Names (p. 214).**
  - The diagonal elements of $\lambda$ are Sylvester's "canonical multipliers" of $\alpha$.
  - For a correlational matrix, multipliers and characteristic values are identical.
  - For a symmetric matrix they may differ in sign.
  - For a general square matrix there is no simple relation.
  - For a rectangular matrix, characteristic values are not defined.
  - The correlational matrices are Sylvester's "false squares" of $\alpha$.
  - $A=\alpha'\alpha$ relates to the correlations of individuals just as $a$ relates to those of tests. The authors say the two are mathematically fully symmetric.
  - One multiplier together with one row of $u$ and one row of $U$ ($n+N+1$ numbers) is a **canonic component** of $\alpha$.
- **Theorem II** (stated, not proved). If $\alpha\beta'$ and $\beta'\alpha$ are both symmetric, then, and only then, orthogonal $u,U$ exist such that $\lambda=u\alpha U'$ and $\mu=u\beta U'$ are both real diagonal matrices. One of the two (in general not both) can additionally be made non-negative. It generalises the result that two symmetric matrices have coinciding principal axes iff $ab=ba$ (p. 214).

*Intuition note.* Every rectangular matrix can be turned into a diagonal one by a rotation (or reflection) of the rows' space and another of the columns' space. The diagonal entries say how strongly each pair of directions is used. Squaring them gives the characteristic values of $\alpha\alpha'$.

### Solution of the problem (pp. 214–216)
- **Objective.** Let $x$ be the distance between $\alpha$ and $\beta$:
$$x^2=(\alpha,\alpha)-2(\alpha,\beta)+(\beta,\beta)\tag{11}$$
$x$ is to be minimised over $\beta$. The elements of $\beta$ are not independent because of the rank condition (p. 214).
- **Canonic form of $\beta$.** Write $\beta=u'\mu U$ (12), with $\mu$ diagonal and $u,U$ orthogonal. Then $\beta$ has rank $r$ iff just $r$ diagonal elements of $\mu$ are nonzero, and these are independent. The entries of $u,U$ are not independent, because the matrices must be orthogonal (p. 215).
- **Variation of $u$.** The authors cite a proposition (Courant–Hilbert): if an orthogonal $u$ gets infinitesimal increments, then
$$\delta u=us\tag{13}$$
with $s$ skew-symmetric, infinitesimal, otherwise arbitrary (p. 215).
- **Stationarity.** By (12) and (9), $x^2=(\alpha,\alpha)-2(\alpha,u'\mu U)+(\mu,\mu)$ (14). At a minimum, $\delta x^2=0$ under $\delta u$ (p. 215). The author writes:
$$0=(\alpha,-su'\mu U)=-(\alpha,s\beta)=-(\alpha\beta',s)\tag{15}$$
  - $s$ is an arbitrary skew-symmetric matrix, so by the Proposition $\alpha\beta'$ must be symmetric.
  - Varying $U$ in the same way shows that $\beta'\alpha$ must also be symmetric.
  - Theorem II then gives orthogonal $u,U$ such that (12) and $\alpha=u'\lambda U$ (12.1) both hold ($\lambda$ = diagonal matrix of multipliers of $\alpha$) (p. 215).
- **Reduced problem.** By (9),
$$x^2=(\lambda-\mu,\lambda-\mu)=\sum_i(\lambda_i-\mu_i)^2\tag{11.1}$$
Minimise this with exactly $r$ of the $\mu_i$ nonzero (pp. 215–216).
- **Result.** Order the multipliers $\lambda_1\ge\lambda_2\ge\lambda_3\ge\cdots$. The author calls the following an "obvious solution" and gives no proof of the minimum (p. 216):
$$\mu_i=\lambda_i\ (i\le r);\qquad \mu_i=0\ (i>r)\tag{17}$$
It is the only solution unless $\lambda_r=\lambda_{r+1}$ (p. 216).
- **Procedure** (p. 216). (1) Write $\alpha$ in canonic form (12.1). (2) Replace all but $r$ of the diagonal elements of $\lambda$ by zeros, starting from the smallest. (3) The result is $\mu$, and $\beta$ is given by (12). The solution is unique unless $\lambda_r=\lambda_{r+1}$.
- **Minimum error.** With $R$ the rank of $\alpha$:
$$x^2=\sum_{i=r+1}^{R}\lambda_i^2$$
- **Upper bound.** If $l$ is the length of $\alpha$, the smallest upper bound for $x$ is $l(1-r/R)^{1/2}$. It can be used to judge approximations obtained by other methods (p. 216). *(added step: $\sum_i\lambda_i^2=l^2$, and the $R-r$ smallest of $R$ non-negative numbers hold at most the fraction $(R-r)/R$ of their sum.)*
- **Correlation matrices.** If $\beta$ is the best rank-$r$ approximation to $\alpha$, then $b=\beta\beta'$ (and $B=\beta'\beta$) is also the best rank-$r$ approximation to $a=\alpha\alpha'$ (and $A=\alpha'\alpha$). So correlation matrices computed from the best approximate score matrix are the best approximations to those computed from the original. The authors say this needs proof, which "is readily supplied" from the results above (p. 216); they do not write it out.

*Intuition note.* After rotating to the canonic form, the error is just the sum of squared gaps between diagonal entries. The cheapest way to zero out all but $r$ entries is to drop the smallest. What remains is a matrix built from the $r$ strongest components.

### Hypothetical interpretation of the canonic components of $\beta$ (pp. 216–218)
- **Question.** Can the canonic components that enter $\beta$ be read as the independent factors behind individual differences in performance? Index tests by $p=1..n$, individuals by $i=1..N$, components by $\rho,\sigma=1..r$ (those with nonzero multiplier). Component $\rho$ consists of $u_{\rho p}$, $\lambda_\rho>0$, $U_{\rho i}$ (pp. 216–217).
- **Relations** (p. 217):
$$\sum_p u_{\rho p}u_{\sigma p}=\delta_{\rho\sigma};\qquad \sum_i U_{\rho i}U_{\sigma i}=\delta_{\rho\sigma}\tag{18}$$
$$\beta_{pi}=\sum_\rho u_{\rho p}\,\lambda_\rho\,U_{\rho i}\tag{19}$$
- **Suggested reading.** If these numbers have empirical meaning, then $N^{1/2}U_{\rho i}$ is the standard score of individual $i$ for the ability to exercise factor $\rho$. And $n^{1/2}u_{\rho p}$ is the standard score of test $p$ for its demand for that factor. The multipliers in (19) do not match the accepted postulates of factor theory, so their interpretation is "not immediate" (p. 217).
- **Test by splitting.** Two sets of individuals ($N_{\rm I}$ and $N_{\rm II}$) take the same $n$ tests. This gives $n\times N_{\rm I}$ and $n\times N_{\rm II}$ matrices $\alpha_{\rm I},\alpha_{\rm II}$, and $\alpha$ is their adjoined combination (p. 217).
  - If $\alpha_{\rm I}$, $\alpha_{\rm II}$ can be approximated by $\beta_{\rm I},\beta_{\rm II}$ with the same $u$-matrix (within reasonable error), the interpretation would be appropriate. The $u$-matrix from $\alpha$ is then the same too.
  - A footnote gives a sufficient condition for equal $u$: $a_{\rm I}a_{\rm II}$ symmetric, where $a_{\rm I}=\alpha_{\rm I}\alpha_{\rm I}'$, etc. It can be applied even when $u_{\rm I},u_{\rm II}$ are unknown.
  - The multipliers and the $U$'s from the three matrices are not identical. With $i$ running from 1 to $N_{\rm I}+N_{\rm II}$, the authors say it "can be shown" that (p. 217):
$$\lambda_\rho^2=\lambda_{\rho,{\rm I}}^2+\lambda_{\rho,{\rm II}}^2\tag{20}$$
$$\lambda_\rho U_{\rho i}=\lambda_{\rho,{\rm I}}U_{\rho i,{\rm I}}\ (i\le N_{\rm I});\qquad =\lambda_{\rho,{\rm II}}U_{\rho i,{\rm II}}\ (i>N_{\rm I})\tag{21}$$
- **Assessment.** These are the relations expected if $\lambda_{\rho,{\rm I}}^2/N_{\rm I}$ and $\lambda_{\rho,{\rm II}}^2/N_{\rm II}$ were the variances of the two sets. The authors reject this as untenable, because individuals and tests enter the calculation symmetrically (pp. 217–218).
  - They suggest instead that $\lambda_{\rho,{\rm I}}^2/(nN_{\rm I})$ may be the product of the variance of the set of individuals and the variance of the set of tests (p. 218).
  - They note an implicit assumption: scores are measured from one fiducial zero common to all sets, not from the sets' own averages (p. 218).

## Toy example (ours, not from the text)
Take $n=N=2$ and $\alpha=\begin{pmatrix}3&1\\1&3\end{pmatrix}$, so $R=2$, $r=1$.
- $\alpha\alpha'=\begin{pmatrix}10&6\\6&10\end{pmatrix}$ has characteristic values $16$ (axis $(1,1)/\sqrt2$) and $4$ (axis $(1,-1)/\sqrt2$). So the multipliers are $\lambda_1=4$, $\lambda_2=2$.
- Check with $u=U=\tfrac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$: $u\alpha=\tfrac1{\sqrt2}\begin{pmatrix}4&4\\2&-2\end{pmatrix}$, and $u\alpha U'=\tfrac12\begin{pmatrix}8&0\\0&4\end{pmatrix}=\begin{pmatrix}4&0\\0&2\end{pmatrix}$.
- Keep $\mu=\mathrm{diag}(4,0)$. Then $\beta=u'\mu U=4\cdot\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}=\begin{pmatrix}2&2\\2&2\end{pmatrix}$.
- Error: $x^2=1+1+1+1=4=\lambda_2^2$. Also $l^2=9+1+1+9=20=16+4$, and the bound is $l(1-\tfrac12)^{1/2}=\sqrt{10}\approx3.16\ge x=2$.
- A competitor, $\begin{pmatrix}3&0\\0&0\end{pmatrix}$ (rank 1), has $x^2=0+1+1+9=11>4$.
- Correlation matrices: $\beta\beta'=\begin{pmatrix}8&8\\8&8\end{pmatrix}=16\cdot\tfrac12\begin{pmatrix}1&1\\1&1\end{pmatrix}$, which is the rank-1 truncation of $\alpha\alpha'$ (its characteristic value 16 kept, 4 dropped).

## Concepts
- [[singular-value-decomposition]] — the paper's "canonic resolution" $\alpha=u'\lambda U$; the multipliers are what the canon calls singular values (canon link; not stated in this unit) (p. 213)
- [[eckart-young-theorem]] — keeping the $r$ largest multipliers gives the closest rank-$r$ matrix in least-squares distance (p. 216)
- [[rank]] — number of nonzero diagonal entries in the canonic form (p. 215)
- [[orthonormal-basis-orthogonal-matrix]] — $u,U$ with $uu'=1$; they leave the scalar product unchanged (p. 212)
- [[norm]] — "length" $l=(\alpha,\alpha)^{1/2}$ of a matrix; distance is the length of the difference (p. 212)
- [[matrix-scalar-product]] (new) — $(\alpha,\beta)=\sum\alpha_{ij}\beta_{ij}$ (p. 211)
- [[canonic-multiplier]] (new) — a diagonal entry of $\lambda$, Sylvester's name (p. 214)
- [[covariance-matrix]] — the paper's "correlational matrices" $\alpha\alpha'$ and $\alpha'\alpha$, whose characteristic values are squared multipliers (pp. 213–214)
- [[spectral-theorem]] — Theorem II generalises the commuting-symmetric-matrices result; $u$ comes from diagonalising the symmetric $\alpha\alpha'$ (pp. 213–214)
- [[least-squares]] — approximation criterion with all elements equally weighted (p. 212)

## Canonical instances
- [[factor-theory-score-matrix]] — an $n\times N$ matrix of $n$ tests by $N$ individuals, approximated by lower rank (p. 211)
- [[two-group-split-test]] — splitting individuals into two sets, a scenario used to discuss the factor reading of the multipliers (p. 217)

## Bridges (candidates)
- [same-math] Eckart–Young best rank-$r$ approximation ↔ principal component analysis: truncated canonic form of the data matrix, keep largest components — same decomposition and truncation.
- [same-math] Squared multipliers = characteristic values of $\alpha\alpha'$ ↔ covariance eigenvalues: PCA variances are eigenvalues of $XX'$ (canon link; not stated in this unit).
- [structural-analogy] Error $=\sum_{i>r}\lambda_i^2$ ↔ explained-variance ratios: the fraction of squared length discarded.
- [metaphor] Canonic components as latent "factors" ↔ latent-variable models in social science.

## Questions this raises
- Why is dropping the smallest $\lambda_i$ the minimiser of $\sum(\lambda_i-\mu_i)^2$ with only $r$ nonzero? The authors call it "obvious".
- What changes if the elements are not weighted equally? The paper treats only equal weights.
- Why can the multipliers not simply be read as variances? What exactly does the symmetry of tests and individuals forbid?
- How is the non-uniqueness at $\lambda_r=\lambda_{r+1}$ resolved in practice?

## Reading notes
- The provided pdf pages 1–8 carry printed page numbers 211–218; all citations use the printed numbers. The running header is "PSYCHOMETRIKA"; the title page gives Vol. 1, No. 3, September 1936.
- The text layer is heavily garbled in equations. All equations here were checked against the page images.
- The printing is hard to distinguish between $\rho$ (component index) and $p$ (test index) in Eqs. (18)–(21). I used $\rho$ for components and $p$ for tests.
- No Eq. (16) appears: the numbering jumps from (11.1) to (17).
- Theorems I and II are stated without proof, referring to Courant–Hilbert and MacDuffee (p. 212). The proof of the $\sum(\lambda_i-\mu_i)^2$ minimum, the proof that $\beta\beta'$ is best for $\alpha\alpha'$, and the derivations of (20)–(21) are not given.
- (10.1) is discussed for $n<N$; the case $n>N$ is not treated. The paper never uses the words "singular value" or "SVD".
- Pages 211–218 contain no exercises.
