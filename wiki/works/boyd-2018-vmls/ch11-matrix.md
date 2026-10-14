---
id: boyd-2018-vmls/ch11-matrix
work: boyd-2018-vmls
unit: Chapter 11 — Matrix inverses
pages: 199-221
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Matrix inverses

## L0 — One line
A matrix has a left inverse exactly when its columns are independent and a right inverse exactly when its rows are independent; for square matrices both coincide with the inverse $A^{-1}$, which solves $Ax=b$ and can be computed by QR factorization and back substitution.

## L1 — The gist (≤ 120 words)
Scalars have one inverse; matrices need left inverses ($XA=I$) and right inverses ($AX=I$). The chapter links them to independence of columns or rows and to the shape of the matrix. A left inverse gives the unique solution of an over-determined system, if a solution exists. A right inverse gives a solution of an under-determined system. A square matrix with either kind has a unique, two-sided inverse. QR factorization reduces solving $Ax=b$ to one costly factorization followed by cheap steps (a matrix–vector product and a triangular solve). The chapter counts flops, shows examples (interpolation, chemical balancing, heat flow), and introduces the pseudo-inverse $(A^TA)^{-1}A^T$.

**Prerequisites:** matrix multiplication and transpose; linear independence; basis; QR factorization and orthogonal matrices; flop counts; Gram matrix $A^TA$.

## L2 — Key ideas
- A left inverse ($XA=I$) forces independent columns, so only square or tall matrices can have one; the chapter proves the converse in §11.5. A left inverse gives the unique solution of $Ax=b$ when a solution exists, and a test for whether one exists (p. 200).
- A right inverse ($AX=I$) is the transpose-mirror of this. It requires independent rows, so only square or wide matrices have one. It gives a solution $x=Bb$ for every $b$ (p. 201).
- If a matrix has both a left and a right inverse, they are equal and unique; this is $A^{-1}$ (p. 202). For square matrices the text says six conditions are equivalent (it lists five), e.g. independent columns, independent rows, a left inverse, a right inverse (p. 203).
- Inverse rules: $(A^T)^{-1}=(A^{-1})^T$, $(AB)^{-1}=B^{-1}A^{-1}$. The dual basis (rows of $A^{-1}$) gives basis coefficients as $\beta=A^{-1}x$ (p. 205).
- Triangular matrices with nonzero diagonal are invertible. Back substitution solves $Rx=b$ in $n^2$ flops (pp. 206–207).
- Solving $Ax=b$ via QR costs about $2n^3$ flops. The factorization can be reused for many right-hand sides. Forming $A^{-1}$ explicitly costs about $3n^3$, so solving $Ax=b$ via $A^{-1}$ is usually not the method of choice (pp. 208–210).
- The pseudo-inverse $A^\dagger=(A^TA)^{-1}A^T$ is a left inverse of a matrix with independent columns. $A^T(AA^T)^{-1}$ is a right inverse when the rows are independent. Both equal $A^{-1}$ for square invertible $A$ (pp. 214–215).

## L3 — Walkthrough

### 11.1 Left and right inverses (pp. 199–202)

**Left inverse.** $X$ is a left inverse of $A$ if $XA=I$. For $A$ of size $m\times n$, $X$ is $n\times m$. $A$ is *left-invertible* if one exists (p. 199).

Examples (p. 199–200):
- A nonzero $1\times1$ matrix has exactly one left inverse (its scalar inverse).
- A nonzero $n$-vector $a$ (as $n\times1$) has the left inverse $x=(1/a_i)e_i^T$ for any $i$ with $a_i\ne0$.
- $A=\begin{bmatrix}-3&-4\\4&6\\1&1\end{bmatrix}$ has two different left inverses
$$B=\tfrac19\begin{bmatrix}-11&-10&16\\7&8&-11\end{bmatrix},\qquad C=\tfrac12\begin{bmatrix}0&-1&6\\0&1&-4\end{bmatrix},$$
checked by $BA=CA=I$. If a matrix has more than one left inverse, it has infinitely many (exercise 11.1).
- If $A$ has orthonormal columns, $A^TA=I$, so $A^T$ is a left inverse.

**Left-invertibility ⟹ independent columns.** Suppose $C$ is a left inverse and $Ax=0$. Then $0=C(Ax)=(CA)x=Ix=x$. So the only combination of the columns giving 0 is the trivial one (p. 200). The text says the converse is proved later (it is, in §11.5). So "a matrix has a left inverse iff its columns are linearly independent" (p. 200).

**Dimensions.** A wide matrix ($m<n$) has dependent columns by the independence-dimension inequality, so it is not left-invertible. Only square or tall matrices can be (p. 200).

**Solving with a left inverse.** If $Ax=b$ and $CA=I$, then $Cb=C(Ax)=(CA)x=x$. Since the columns are independent, this solution is unique (p. 200). If no solution exists, $x=Cb$ cannot satisfy $Ax=b$. So we test whether $A(Cb)=b$: if yes, $Cb$ is the solution; if no, there is no solution (p. 200).

**Right inverse.** $X$ with $AX=I$; it has the same dimensions as $A^T$ (p. 201).

**Transposes.** If $B$ is a right inverse of $A$, then $B^TA^T=(AB)^T=I$, so $B^T$ is a left inverse of $A^T$. If $C$ is a left inverse of $A$, then $C^T$ is a right inverse of $A^T$ (p. 201). Hence:
- a matrix is right-invertible iff its rows are linearly independent;
- a tall matrix cannot have a right inverse; only square or wide matrices can (p. 201).

**Solving with a right inverse.** If $A$ has right inverse $B$, then for *any* $b$, $x=Bb$ satisfies $Ax=A(Bb)=(AB)b=Ib=b$. Other solutions may exist (p. 201).

Examples with the $3\times2$ matrix $A$ above (pp. 201–202):
- $Ax=(1,-2,0)$ has the unique solution $x=(1,-1)=B(1,-2,0)=C(1,-2,0)$.
- $Ax=(1,-1,0)$ has no solution, because $x=C(1,-1,0)=(1/2,-1/2)$ does not satisfy it.
- $A^Ty=(1,2)$ has the different solutions $B^T(1,2)=(1/3,2/3,-2/3)$ and $C^T(1,2)=(0,1/2,-1)$.

**Products.** If $A$, $D$ have right inverses $B$, $E$, then $EB$ is a right inverse of $AD$: $(AD)(EB)=A(DE)B=A(IB)=AB=I$. If $A$, $D$ have left inverses $C$, $F$, then $FC$ is a left inverse of $AD$: $(FC)(AD)=F(CA)D=FD=I$ (p. 202).

*Intuition note.* A left inverse "undoes" $A$, which is only possible if $A$ loses no information, i.e. its columns are independent. A right inverse says every right-hand side can be reached, so the rows must be independent.

### 11.2 Inverse (pp. 202–206)

**Uniqueness.** Let $AX=I$ and $YA=I$. Then $X=(YA)X=Y(AX)=Y$. So any left inverse equals any right inverse. If $A$ has both, each is unique. This common matrix is $A^{-1}$; $A$ is *invertible* (nonsingular). A square matrix that is not invertible is *singular* (p. 202).

**Dimensions.** Invertible matrices must be square (tall: no right inverse; wide: no left inverse). $AA^{-1}=A^{-1}A=I$ and $(A^{-1})^{-1}=A$ (p. 202).

**Solving square systems.** If $A$ is invertible, $x=A^{-1}b$ \tag{11.1} is a solution, because $A^{-1}$ is a right inverse. It is the only solution, because $A^{-1}$ is a left inverse. So the solution is a linear function of $b$ (p. 203).

**Invertibility conditions (square $A$).** Suppose $A$ is $n\times n$ and left-invertible. Its columns are independent, hence form a basis. So each unit vector can be written $e_i=Ab_i$. With $B=[\,b_1\ \cdots\ b_n\,]$,
$$AB=[\,Ab_1\ \cdots\ Ab_n\,]=[\,e_1\ \cdots\ e_n\,]=I,$$
so $B$ is a right inverse (p. 203). Thus for square $A$:
left-invertible ⟹ independent columns ⟹ right-invertible.
Applying this to $A^T$: right-invertible ⟹ independent rows ⟹ left-invertible. All six conditions are equivalent: invertible, independent columns, independent rows, has a left inverse, has a right inverse (p. 203; the source lists five bullets and says "six" conditions).

**Examples (p. 204).**
- $I^{-1}=I$.
- A diagonal matrix is invertible iff all diagonal entries are nonzero; then $\mathbf{diag}(A_{11},\dots,A_{nn})^{-1}=\mathbf{diag}(A_{11}^{-1},\dots,A_{nn}^{-1})$.
- $A=\begin{bmatrix}1&-2&3\\0&2&2\\-3&-4&-4\end{bmatrix}$ has $A^{-1}=\tfrac1{30}\begin{bmatrix}0&-20&-10\\-6&5&-2\\6&10&2\end{bmatrix}$ (checked by $AA^{-1}=I$).
- A $2\times2$ matrix is invertible iff $A_{11}A_{22}\ne A_{12}A_{21}$, with
$$A^{-1}=\frac{1}{A_{11}A_{22}-A_{12}A_{21}}\begin{bmatrix}A_{22}&-A_{12}\\-A_{21}&A_{11}\end{bmatrix}.$$
Formulas for larger sizes grow in complexity and are not very useful in most applications.
- A square matrix with orthonormal columns (orthogonal) has $A^{-1}=A^T$.

**Transpose and product (p. 205).** If $A$ is invertible, so is $A^T$, and $(A^T)^{-1}=(A^{-1})^T=:A^{-T}$. If $A$, $B$ are invertible and the same size, $AB$ is invertible and
$$(AB)^{-1}=B^{-1}A^{-1}.\tag{11.2}$$

**Dual basis (p. 205).** Let $A=[\,a_1\ \cdots\ a_n\,]$ be invertible with $B=A^{-1}$ having rows $b_1^T,\dots,b_n^T$. The $a_i$ form a basis; the $b_i$ also form a basis (rows of $B$ are independent), called the *dual basis*. For any $x$, from $AB=I$:
$$x=ABx=[\,a_1\ \cdots\ a_n\,]\begin{bmatrix}b_1^T\\\vdots\\b_n^T\end{bmatrix}x=(b_1^Tx)a_1+\cdots+(b_n^Tx)a_n.$$
By independence of the $a_i$, the coefficients in $x=\beta_1a_1+\cdots+\beta_na_n$ are $\beta_i=b_i^Tx$; in matrix form $\beta=Bx=A^{-1}x$.
Numerical example: $a_1=(1,1)$, $a_2=(1,-1)$; dual basis $b_1^T=[\,1/2\ \ 1/2\,]$, $b_2^T=[\,1/2\ \ -1/2\,]$. For $x=(-5,1)$: $x=(-2)a_1+(-3)a_2$.

*Intuition note.* Row $i$ of $A^{-1}$ is a "detector" for the $i$-th basis vector: its inner product with $x$ reads off how much of $a_i$ is in $x$.

**Negative powers (p. 206).** For invertible $A$ and positive integer $k$, repeated use of (11.2) gives $(A^k)^{-1}=(A^{-1})^k=:A^{-k}$. With $A^0=I$, $A^{k+l}=A^kA^l$ holds for all integers $k,l$.

**Triangular matrices (p. 206).** Let $L$ be $n\times n$, lower triangular, with nonzero diagonal. Write $Lx=0$ row by row: $L_{11}x_1=0$ gives $x_1=0$; then $L_{22}x_2=0$ gives $x_2=0$; and so on. So $x=0$, the columns are independent, and $L$ is invertible. For upper triangular $R$ with nonzero diagonal: $L=R^T$ is lower triangular with the same diagonal, and $(L^T)^{-1}=(L^{-1})^T$.

**Inverse via QR (p. 206).** If $A$ is square and invertible, its columns are independent, so $A=QR$ with $Q$ orthogonal and $R$ upper triangular with positive diagonal. Hence
$$A^{-1}=(QR)^{-1}=R^{-1}Q^{-1}=R^{-1}Q^T.\tag{11.3}$$

### 11.3 Solving linear equations (pp. 207–210)

**Back substitution (Algorithm 11.1).** $R$ is $n\times n$ upper triangular with nonzero diagonal; solve $Rx=b$. The last equation gives $x_n=b_n/R_{nn}$. Substituting upward, $x_{n-1}=(b_{n-1}-R_{n-1,n}x_n)/R_{n-1,n-1}$. In general, for $i=n,\dots,1$:
$$x_i=(b_i-R_{i,i+1}x_{i+1}-\cdots-R_{i,n}x_n)/R_{ii}.$$
It computes $x=R^{-1}b$ and cannot fail, since the divisions are by nonzero diagonal entries. *Forward substitution* does the analogous thing for lower triangular matrices, finding $x_1$ first (p. 207).

**Complexity (pp. 207–208).** Step $k$ costs $k-1$ multiplies, $k-1$ subtractions and 1 division: $2k-1$ flops. Total $1+3+5+\cdots+(2n-1)=n^2$ flops. For even $n$, pair first with last, second with second-to-last, etc.: each pair sums to $2n$, with $n/2$ pairs, giving $(n/2)(2n)=n^2$ (an odd $n$ works similarly).

**Solving via QR (Algorithm 11.2).** From (11.3), $x=A^{-1}b=R^{-1}Q^Tb$ \tag{11.4}. Steps: (1) compute $A=QR$; (2) compute $Q^Tb$; (3) solve $Rx=Q^Tb$ by back substitution. Costs: $2n^3$ (QR, §5.4), $2n^2$, $n^2$. Total $2n^3+3n^2\approx2n^3$, so the order is $n^3$. The QR step dominates (p. 208).

**Factor-solve methods.** A factor-solve scheme has a *factor* step (write the coefficient matrix as a product of special matrices) and a *solve* step (solve equations involving the factors). The solve step is cheaper, often negligible; here $n^3$ vs $n^2$ (p. 208).

**Multiple right-hand sides (pp. 208–209).** To solve $Ax_i=b_i$, $i=1,\dots,k$, write $AX=B$ with $X=A^{-1}B$. Running Algorithm 11.2 $k$ times costs $2kn^3$. Instead, reuse the factorization ("factorization caching") and repeat only steps 2–3. Cost: $2n^3+3kn^2$, about $2n^3$ if $k\ll n$. So many systems with the same $A$ cost essentially the same as one.

**Backslash notation.** In some software, `A\b` means $A^{-1}b$ and `A\B` means $A^{-1}B$, implemented by factoring once. The book does not use it (p. 209). (The book's own text prints the cached step with indices "$\hat x_k=R^{-1}Q^Tb_k$ for $l=1,\dots,k$"; see Reading notes.)

**Computing the inverse (Algorithm 11.3).** From $A^{-1}=R^{-1}Q^T$, set $B=A^{-1}$ so $RB=Q^T$. By columns, $Rb_i=\tilde q_i$, $i=1,\dots,n$, where $\tilde q_i$ is column $i$ of $Q^T$. Solve each by back substitution. Cost: $2n^3$ (QR) plus $n\cdot n^2=n^3$, about $3n^3$ flops (p. 209). Solving $Ax=b$ by first forming $A^{-1}$ and then $A^{-1}b$ costs more ($3n^3$ vs $2n^3$), so Algorithm 11.2 is the usual choice. The inverse appears in many formulas but is computed far less often (pp. 209–210).

**Sparse equations (p. 210).** If the coefficient matrix is sparse, use Algorithm 11.2 with a sparse-aware QR variant. Cost depends in a complicated way on the sparsity pattern. Typically, memory is a modest multiple of $\mathbf{nnz}(A)+n$ (much less than $n^2+n$), and the flop count is closer in order to $\mathbf{nnz}(A)$ than to $n^3$.

### 11.4 Examples (pp. 210–214)

**Polynomial interpolation (pp. 210–211).** The cubic $p(x)=c_1+c_2x+c_3x^2+c_4x^3$ must satisfy $p(-1.1)=b_1$, $p(-0.4)=b_2$, $p(0.2)=b_3$, $p(0.8)=b_4$. This is $Ac=b$ with the Vandermonde matrix $A$ whose rows are $(1,t,t^2,t^3)$ for $t=-1.1,-0.4,0.2,0.8$. The unique solution is $c=A^{-1}b$, with (4 decimals)
$$A^{-1}=\begin{bmatrix}-0.0370&0.3492&0.7521&-0.0643\\0.1388&-1.8651&1.6239&0.1023\\0.3470&0.1984&-1.4957&0.9503\\-0.5784&1.9841&-2.1368&0.7310\end{bmatrix}.$$
- Columns of $A^{-1}$ give coefficients of polynomials equal to 1 at one of the points and 0 at the other three. For example $A^{-1}e_1$ is 1 at $-1.1$ and 0 at $-0.4,0.2,0.8$. These are the *Lagrange polynomials* for the points (figure 11.2).
- Row $i$ shows how $b_1,\dots,b_4$ map into coefficient $c_i$. For instance $c_1$ is not very sensitive to $b_1$ since $(A^{-1})_{11}$ is small. Each increase of one in $b_4$ raises $c_3$ by about 0.95.

**Balancing a chemical reaction (pp. 211–213).** $a_1\mathrm{Cr_2O_7^{2-}}+a_2\mathrm{Fe^{2+}}+a_3\mathrm{H^+}\to b_1\mathrm{Cr^{3+}}+b_2\mathrm{Fe^{3+}}+b_3\mathrm{H_2O}$. There are 4 atoms (Cr, O, Fe, H) plus charge to balance, giving 5 rows. The reactant and product matrices are
$$R=\begin{bmatrix}2&0&0\\7&0&0\\0&1&0\\0&0&1\\-2&2&1\end{bmatrix},\quad P=\begin{bmatrix}1&0&0\\0&0&1\\0&1&0\\0&0&2\\3&3&0\end{bmatrix}.$$
Imposing $a_1=1$ adds one equation, giving a square system of 6 equations:
$$\begin{bmatrix}2&0&0&-1&0&0\\7&0&0&0&0&-1\\0&1&0&0&-1&0\\0&0&1&0&0&-2\\-2&2&1&-3&-3&0\\1&0&0&0&0&0\end{bmatrix}\begin{bmatrix}a_1\\a_2\\a_3\\b_1\\b_2\\b_3\end{bmatrix}=\begin{bmatrix}0\\0\\0\\0\\0\\1\end{bmatrix}.$$
Solution: $a=(1,6,14)$, $b=(2,6,7)$. (Setting $a_1=1$ could have given fractions, but here it did not.) Balanced: $\mathrm{Cr_2O_7^{2-}}+6\mathrm{Fe^{2+}}+14\mathrm{H^+}\to2\mathrm{Cr^{3+}}+6\mathrm{Fe^{3+}}+7\mathrm{H_2O}$.

**Heat diffusion (pp. 213–214).** This builds on the diffusion system of page 155, which is not included here. Let $\mathcal P$ be the set of nodes with fixed potential: $e_i=e_i^{\rm fix}$ for $i\in\mathcal P$, and source $s_i=0$ for $i\notin\mathcal P$. In matrix form $Bs+Ce=d$, with $n\times n$ diagonal $B_{ii}=0$ ($i\in\mathcal P$), $1$ ($i\notin\mathcal P$); $C_{ii}=1$ ($i\in\mathcal P$), $0$ otherwise; $d_i=e_i^{\rm fix}$ ($i\in\mathcal P$), $0$ otherwise. Assembling with flow conservation and edge flow gives $m+2n$ equations in $(f,s,e)$:
$$\begin{bmatrix}A&I&0\\R&0&A^T\\0&B&C\end{bmatrix}\begin{bmatrix}f\\s\\e\end{bmatrix}=\begin{bmatrix}0\\0\\d\end{bmatrix}.$$
Here $A$ is the graph's incidence matrix and $R$ the resistance matrix (page 155, not included). If the coefficient matrix is invertible, the solution is that inverse times $(0,0,d)$. Figure 11.3: a $100\times100$ grid (10000 nodes), equal edge resistances, top and bottom rows at temperature 0, three rectilinear node sets at 1, all other nodes with zero source.

### 11.5 Pseudo-inverse (pp. 214–216)

**Independent columns ⟺ invertible Gram matrix.** An $m\times n$ matrix $A$ has independent columns iff the $n\times n$ Gram matrix $A^TA$ is invertible (p. 214).
- (⟹) Let $(A^TA)x=0$. Then $0=x^TA^TAx=\|Ax\|^2$, so $Ax=0$, so $x=0$ by independence. Hence $A^TA$ is invertible.
- (⟸, shown as its contrapositive) If the columns are dependent, there is $x\ne0$ with $Ax=0$; then $(A^TA)x=0$, so $A^TA$ is singular.

**Pseudo-inverse, tall or square.** If $A$ has independent columns, $(A^TA)^{-1}A^T$ is a left inverse: $\big((A^TA)^{-1}A^T\big)A=(A^TA)^{-1}(A^TA)=I$. This proves the converse promised in §11.1. It is the pseudo-inverse (Moore–Penrose inverse):
$$A^\dagger=(A^TA)^{-1}A^T.\tag{11.5}$$
For square invertible $A$: $A^\dagger=A^{-1}A^{-T}A^T=A^{-1}$. This computation does not make sense when $A$ is not square (pp. 214–215).

**Square or wide.** Transposing: a square or wide $A$ has a right inverse iff its rows are independent. One right inverse is
$$A^T(AA^T)^{-1},\tag{11.6}$$
also called $A^\dagger$ ($AA^T$ is invertible iff the rows are independent). For square $A$ both formulas reduce to $A^{-1}$: $A^T(AA^T)^{-1}=A^TA^{-T}A^{-1}=A^{-1}$ (p. 215).

**Other cases.** $A^\dagger$ is defined for any matrix (tall with dependent columns, wide with dependent rows, singular square), but there it is not a left inverse, right inverse, or inverse respectively. Its meaning there is deferred to exercise 15.11 (p. 215).

**Via QR (pp. 215–216).** If $A$ is left-invertible, $A=QR$ and $A^TA=R^TQ^TQR=R^TR$, so
$$A^\dagger=(R^TR)^{-1}(QR)^T=R^{-1}R^{-T}R^TQ^T=R^{-1}Q^T.$$
Compute it by QR, then back substitution on the columns of $Q^T$ (the same as Algorithm 11.3 when $A$ is square). Cost: $2n^2m$ (QR) $+\,mn^2$ ($m$ back substitutions) $=3mn^2$ flops. If $A$ is right-invertible, use $A^T=QR$: $AA^T=R^TR$ and $A^\dagger=A^T(AA^T)^{-1}=QR(R^TR)^{-1}=QRR^{-1}R^{-T}=QR^{-T}$. Compute via $(A^T)^\dagger=(A^\dagger)^T$.

**Solving systems (p. 216).** If the columns of $A$ are independent and $Ax=b$ (over-determined) has a solution, then $x=A^\dagger b$ is it. If the rows are independent, $Ax=b$ has a solution for every $b$, and $x=A^\dagger b$ is one.

**Numerical example (p. 216).** $A=\begin{bmatrix}-3&-4\\4&6\\1&1\end{bmatrix}$ has $Q=\begin{bmatrix}-0.5883&0.4576\\0.7845&0.5230\\0.1961&-0.7191\end{bmatrix}$, $R=\begin{bmatrix}5.0990&7.2563\\0&0.5883\end{bmatrix}$ and
$$A^\dagger=R^{-1}Q^T=\begin{bmatrix}-1.2222&-1.1111&1.7778\\0.7778&0.8889&-1.2222\end{bmatrix}.$$
For $b=(1,-2,0)$: $x=A^\dagger b=(1,-1)$, and $Ax=b$ holds, so it is the unique solution.

*Intuition note.* $A^\dagger$ is one particular left (or right) inverse, chosen by a formula, so it is the same matrix whichever independent-column system you apply it to. $A^TA$ being invertible is what makes the formula work.

## Toy example (ours, not from the text)
Let $A=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix}$ (tall, columns independent).
1. $A^TA=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, determinant $4-1=3$, so by the $2\times2$ formula $(A^TA)^{-1}=\tfrac13\begin{bmatrix}2&-1\\-1&2\end{bmatrix}$.
2. $A^\dagger=(A^TA)^{-1}A^T=\tfrac13\begin{bmatrix}2&-1\\-1&2\end{bmatrix}\begin{bmatrix}1&0&1\\0&1&1\end{bmatrix}=\tfrac13\begin{bmatrix}2&-1&1\\-1&2&1\end{bmatrix}$.
3. Check $A^\dagger A$: row 1 $(2,-1,1)$ with columns $(1,0,1)$ and $(0,1,1)$ gives $3$ and $0$; row 2 $(-1,2,1)$ gives $0$ and $3$. So $A^\dagger A=\tfrac13\cdot3I=I$.
4. $b=(1,2,3)$: $x=A^\dagger b=\tfrac13(2-2+3,\,-1+4+3)=(1,2)$. $Ax=(1,2,3)=b$, so this is the unique solution.
5. $b=(1,2,4)$: $x=\tfrac13(4,7)=(4/3,7/3)$. $Ax=(4/3,7/3,11/3)\ne b$, so no solution exists.
6. Back substitution: $R=\begin{bmatrix}2&1\\0&3\end{bmatrix}$, $b=(5,6)$. $x_2=6/3=2$; $x_1=(5-1\cdot2)/2=3/2$.

## Concepts
- [[inverse matrix]] — a matrix $A^{-1}$ with $AA^{-1}=A^{-1}A=I$; exists only for square matrices, and then left, right and two-sided invertibility coincide (pp. 202–203)
- [[left-inverse]] (new) — $X$ with $XA=I$; exists iff columns are independent; not unique in general (pp. 199–200)
- [[right-inverse]] (new) — $X$ with $AX=I$; exists iff rows are independent (p. 201)
- [[singular-matrix]] (new) — a square matrix that is not invertible (p. 202)
- [[linear independence]] — here linked to inverses: independent columns ⟺ left-invertible, independent rows ⟺ right-invertible (pp. 200–201)
- [[basis]] — used for the dual basis: rows of $A^{-1}$ give coefficients $\beta=A^{-1}x$ (p. 205)
- [[dual-basis]] (new) — rows of $B=A^{-1}$, as vectors $b_i$, paired with the columns $a_i$ of $A$ (p. 205)
- [[orthonormal basis / orthogonal matrix]] — a square matrix with orthonormal columns has $A^{-1}=A^T$ (p. 204)
- [[Gram–Schmidt and QR]] — $A^{-1}=R^{-1}Q^T$, used to solve systems and compute inverses (pp. 206, 208–209)
- [[back-substitution]] (new) — solves upper triangular $Rx=b$ from $x_n$ up to $x_1$ in $n^2$ flops (p. 207)
- [[factor-solve-method]] (new) — factor $A$ once (costly), then solve with the factors (cheap); allows reuse for many right-hand sides (p. 208)
- [[gram-matrix]] (new) — $A^TA$; invertible iff the columns of $A$ are independent (p. 214)
- [[pseudoinverse]] — here $A^\dagger=(A^TA)^{-1}A^T$ for independent columns, $A^T(AA^T)^{-1}$ for independent rows; equals $A^{-1}$ if square invertible. The text defines it for any matrix but only for these cases as a one-sided inverse (pp. 214–215)
- [[lagrange-polynomials]] (new) — columns of the inverse of the Vandermonde matrix; each is 1 at one point and 0 at the others (p. 211)

## Canonical instances
- [[three-by-two-example-matrix]] — $A=\begin{bmatrix}-3&-4\\4&6\\1&1\end{bmatrix}$ with two left inverses $B$, $C$; reused for QR and pseudo-inverse (pp. 199–201, 216)
- [[polynomial-interpolation]] — cubic through four points solved by $c=A^{-1}b$; Lagrange polynomials (pp. 210–211)
- [[balancing-chemical-reactions]] — dichromate–iron reaction solved as a $6\times6$ system (pp. 211–213)
- [[heat-diffusion-grid]] — $100\times100$ grid temperature problem as a $(m+2n)$-equation system (pp. 213–214)

## Bridges (candidates)
- [structural-analogy] left/right inverse ↔ solving over-/under-determined systems: left inverse = unique solution if one exists; right inverse = existence for every $b$ — mirrors injective vs surjective maps (not stated in this unit)
- [same-math] pseudo-inverse $(A^TA)^{-1}A^T$ ↔ least squares: the normal-equations matrix (canon: least squares; the text defers the interpretation to later chapters)
- [metaphor] factor-solve with caching ↔ numerical stability / conditioning: factor once, reuse; sensitivity of $A^{-1}b$ appears in exercise 11.26
- [same-math] dual basis coefficients $\beta=A^{-1}x$ ↔ change of basis: $A^{-1}$ converts standard coordinates into coordinates in the basis of columns of $A$
- [structural-analogy] diffusion on a grid (heat) ↔ graph Laplacian (canon): incidence matrix $A$ and a resistance matrix $R$ appear in the system

## Questions this raises
- What does $A^\dagger b$ mean when the over-determined system $Ax=b$ has no solution? (The text treats only the case where a solution exists, p. 216; it defers $A^\dagger$ for dependent columns or rows to exercise 15.11, p. 215.)
- How sensitive is $x=A^{-1}b$ to small changes in $b$ or $A$? (Exercise 11.26 introduces ill-conditioning.)
- How much faster can sparse or structured systems be solved, e.g. the $10000$-node grid?
- What is the pseudo-inverse of a matrix whose columns are dependent (exercise 15.11)?

## Exercises worth doing
- Ex. 11.1 (p. 217) — affine combinations of left inverses give infinitely many left inverses — difficulty: easy
- Ex. 11.3 (p. 217) — matrix cancellation $AX=AY\Rightarrow X=Y$ holds exactly when $A$ is left-invertible — difficulty: medium
- Ex. 11.7 (p. 218) — the inverse of an upper triangular matrix is upper triangular, via back substitution — difficulty: medium
- Ex. 11.17 (p. 220) — nilpotent $A$: is $(I-A)^{-1}=I+A+\cdots+A^{k-1}$? — difficulty: medium
- Ex. 11.26 (p. 221) — sensitivity of $A^{-1}b$ to a perturbation of one entry of $b$ — difficulty: medium
- Ex. 11.28 (p. 221) — solving $Az=d$ with $d=\alpha b+\beta c$ in linear-in-$n$ time — difficulty: medium

## Reading notes
- Printed page = pdf page − 10 (pdf 209 = printed 199). The pdf page 232 is blank.
- Misprint on p. 209: the multiple-right-hand-side sentence reads "$\hat x_k=R^{-1}Q^Tb_k$ for $l=1,\dots,k$"; the indices should match (the image shows $k$ on the left side and $l$ in the range).
- On p. 203 the text says "all six of these conditions are equivalent" but the final summary list shows five bullets; the page does not say which condition is the sixth.
- The heat-diffusion section refers to equations on page 155 (flow conservation, edge flow), which is not in this unit; they are read here only from the block matrix.
- Text-layer equations were checked against the images; no unreadable equations.
