---
id: deisenroth-2020-mml/ch02-linear-p1
work: deisenroth-2020-mml
unit: "2 Linear Algebra (part 1/2): chapter intro, 2.1 Systems of Linear Equations, 2.2 Matrices, 2.3 Solving Systems of Linear Equations, 2.4 Vector Spaces, 2.5 Linear Independence (to the start of Example 2.15)"
pages: 17-43
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Linear Algebra, part 1: equations, matrices, vector spaces, linear independence

## L0 — One line
Anything that can be added and scaled is a vector, and a linear system Ax = b is solved by Gaussian elimination, which brings the system to a simple form from which one particular solution plus all solutions of Ax = 0 can be found.

## L1 — The gist (≤ 120 words)
The unit asks what vectors and matrices are and how to solve linear systems systematically. Vectors are any objects that can be added and scaled. A system can be written as Ax = b. Gaussian elimination (swapping, scaling and adding equations until the system is simple) brings it to a form from which one finds one particular solution (any single solution) and then adds all solutions of Ax = 0. The same elimination gives matrix inverses and tests linear independence. The unit then defines groups, vector spaces and subspaces, and linear (in)dependence. This matters because later chapters on regression and dimensionality reduction rest on these ideas.

**Prerequisites:** high-school algebra (solving simultaneous equations); sets and the ∀/∃ notation; the idea of a row and a column of numbers.

## L2 — Key ideas
- A vector is any object that can be added and scaled with the result of the same kind. Geometric vectors, polynomials, audio signals and elements of Rⁿ all qualify; the book works mostly in Rⁿ (pp. 17–18).
- A system of linear equations has no solution, exactly one, or infinitely many. It can be written compactly as Ax = b, where Ax is a linear combination of the columns of A (pp. 21, 26).
- Matrix multiplication needs matching "neighbouring" dimensions and is not commutative (AB ≠ BA in general). Inverses exist only for some square matrices (pp. 22–25).
- General solution of Ax = b = particular solution + all solutions of Ax = 0. Neither the general nor the particular solution is unique (p. 28).
- Gaussian elimination uses three elementary row operations (swap rows, scale a row, add rows) to reach (reduced) row-echelon form, a staircase shape. It also gives the inverse via [A|I] ⇝ [I|A⁻¹] and the null-space solutions (the solutions of Ax = 0) via the "minus-1 trick" (pp. 29–33).
- For huge systems, elimination is impractical because its cost grows cubically. Iterative schemes x⁽ᵏ⁺¹⁾ = Cx⁽ᵏ⁾ + d are used instead (p. 35).
- Groups and vector spaces are defined by axioms. A subspace (a subset that is itself a vector space) needs 0, closure under addition and closure under scaling (adding or scaling members stays inside the set) (pp. 36–39).
- Vectors are linearly independent iff only the trivial combination gives 0. In row-echelon form (a staircase of leading nonzero entries called pivots), this holds iff every column is a pivot column, i.e. contains a pivot (pp. 40–42).

## L3 — Walkthrough

### Chapter introduction (pp. 17–19)
- Algebra means a set of objects plus rules to manipulate them. Linear algebra studies vectors and rules for manipulating them (p. 17).
- **Definition used:** vectors are special objects that can be added together and multiplied by scalars (plain real numbers) to give another object of the same kind. Any object with these two properties can be considered a vector (p. 17).
- The author's examples (pp. 17–18):
  1. Geometric vectors (directed segments); sums and scalar multiples are again geometric vectors.
  2. Polynomials; these are abstract, unlike geometric vectors.
  3. Audio signals (series of numbers).
  4. Elements of Rⁿ (n-tuples of reals), e.g. $\boldsymbol a=[1,2,3]^\top\in\mathbb R^3$ (2.1). Addition is componentwise. Rⁿ loosely corresponds to arrays on a computer.
- The book focuses on finite-dimensional vector spaces. In that case there is a 1:1 correspondence between any kind of vector and Rⁿ (p. 18).
- "Closure" is the question: what set of objects can result from my operations? Starting from a few vectors and adding and scaling them leads to a vector space (Section 2.4) (p. 18).
- Figure 2.2 is a mind map of the chapter. Chapters 3, 5, 9, 10 and 12 use these ideas: geometry (Ch. 3), vector calculus (Ch. 5), least-squares regression (Ch. 9), PCA via projections (Ch. 10) (pp. 18–19).

### 2.1 Systems of Linear Equations (pp. 19–22)
- **Example 2.1 (production plan).** Products $N_1,\dots,N_n$ need resources $R_1,\dots,R_m$. Unit of $N_j$ needs $a_{ij}$ units of $R_i$. We want $x_j$ units of each product so that $b_i$ units of each resource are available and (ideally) none are left over. Resource $R_i$ use is $a_{i1}x_1+\dots+a_{in}x_n$ (2.2), so the plan must satisfy
$$a_{11}x_1+\dots+a_{1n}x_n=b_1,\ \ \dots,\ \ a_{m1}x_1+\dots+a_{mn}x_n=b_m \tag{2.3}$$
  with $a_{ij},b_i\in\mathbb R$ (pp. 19–20).
- Terms: (2.3) is a *system of linear equations*; $x_1..x_n$ are the *unknowns*; each n-tuple in Rⁿ satisfying (2.3) is a *solution* (p. 20).
- **Example 2.2** (three 3×3 systems, p. 20):
  - (2.4) has no solution: (1)+(2) gives $2x_1+3x_3=5$, contradicting (3) $2x_1+3x_3=1$.
  - (2.5) has the unique solution (1,1,1). From (1) and (3), $x_1=1$. From (1)+(2), $2x_1+3x_3=5$, so $x_3=1$. Then (3) gives $x_2=1$.
  - (2.6) has (1)+(2)=(3), so (3) is redundant. Then $2x_1=5-3x_3$ and $2x_2=1+x_3$. With free variable $x_3=a$, every triple $(\tfrac52-\tfrac32a,\ \tfrac12+\tfrac12a,\ a)$, $a\in\mathbb R$, is a solution (2.7). There are infinitely many.
- General fact: a real-valued system has either no, exactly one, or infinitely many solutions (p. 21). Linear regression (Ch. 9) handles a version of Example 2.1 when the system cannot be solved (p. 21).
- **Geometric remark (p. 21).** With two unknowns each equation is a line, and the solution set is the intersection of the lines. It is a line (same line), a point, or empty (parallel lines). Example (2.8): $4x_1+4x_2=5$, $2x_1-4x_2=1$ has the single solution $(1,\tfrac14)$ (Figure 2.3). With three unknowns each equation is a plane, and the intersection can be a plane, a line, a point or empty.
- Compact form: collect the coefficients into column vectors (2.9), then into a matrix: $\boldsymbol A\boldsymbol x=\boldsymbol b$ as in (2.10) (pp. 21–22).

*Intuition note.* Each equation is a constraint. The solution set is what survives all constraints at once, so it can be empty, a single point, or a whole line, plane or larger set.

### 2.2 Matrices (pp. 22–26)
**Definition 2.1 (Matrix).** For $m,n\in\mathbb N$, a real (m,n) matrix is an $m\cdot n$-tuple $a_{ij}$ arranged in m rows and n columns (2.11). By convention (1,n)-matrices are *rows* and (m,1)-matrices are *columns*; these are row/column vectors (p. 22). $\mathbb R^{m\times n}$ is the set of all such matrices. A matrix can be re-shaped into a vector in $\mathbb R^{mn}$ by stacking its columns (Figure 2.4) (p. 22).

**2.2.1 Addition and multiplication.**
- Sum: elementwise, $\boldsymbol A+\boldsymbol B\in\mathbb R^{m\times n}$ for same-size matrices (2.12) (p. 22).
- Product: for $\boldsymbol A\in\mathbb R^{m\times n}$, $\boldsymbol B\in\mathbb R^{n\times k}$, $\boldsymbol C=\boldsymbol A\boldsymbol B\in\mathbb R^{m\times k}$ with
$$c_{ij}=\sum_{l=1}^{n}a_{il}b_{lj},\quad i=1..m,\ j=1..k \tag{2.13}$$
  Row i of A times column j of B, summed. This is the dot product of that row and column (p. 23).
- **Remark (p. 23).** Neighbouring dimensions must match: $\underbrace{A}_{n\times k}\underbrace{B}_{k\times m}=\underbrace{C}_{n\times m}$ (2.14). BA is then undefined if $m\ne n$. Matrix multiplication is *not* elementwise ($c_{ij}\neq a_{ij}b_{ij}$); elementwise multiplication is the Hadamard product.
- **Example 2.3** (p. 23): $\boldsymbol A=\begin{bmatrix}1&2&3\\3&2&1\end{bmatrix}$, $\boldsymbol B=\begin{bmatrix}0&2\\1&-1\\0&1\end{bmatrix}$ give
$$\boldsymbol A\boldsymbol B=\begin{bmatrix}2&3\\2&5\end{bmatrix}\in\mathbb R^{2\times2}\ (2.15),\qquad \boldsymbol B\boldsymbol A=\begin{bmatrix}6&4&2\\-2&0&2\\3&2&1\end{bmatrix}\in\mathbb R^{3\times3}\ (2.16).$$
  So $\boldsymbol A\boldsymbol B\ne\boldsymbol B\boldsymbol A$: multiplication is not commutative (p. 23).
- **Definition 2.2.** The identity matrix $\boldsymbol I_n\in\mathbb R^{n\times n}$ has 1 on the diagonal and 0 elsewhere (2.17) (p. 23).
- Properties (p. 24): associativity $(\boldsymbol A\boldsymbol B)\boldsymbol C=\boldsymbol A(\boldsymbol B\boldsymbol C)$ (2.18); distributivity $(\boldsymbol A+\boldsymbol B)\boldsymbol C=\boldsymbol A\boldsymbol C+\boldsymbol B\boldsymbol C$ (2.19a) and $\boldsymbol A(\boldsymbol C+\boldsymbol D)=\boldsymbol A\boldsymbol C+\boldsymbol A\boldsymbol D$ (2.19b); $\boldsymbol I_m\boldsymbol A=\boldsymbol A\boldsymbol I_n=\boldsymbol A$ (2.20), with $\boldsymbol I_m\ne\boldsymbol I_n$ for $m\neq n$.

**2.2.2 Inverse and transpose.**
- **Definition 2.3 (Inverse).** For square $\boldsymbol A\in\mathbb R^{n\times n}$, a matrix $\boldsymbol B$ with $\boldsymbol A\boldsymbol B=\boldsymbol I_n=\boldsymbol B\boldsymbol A$ is the inverse $\boldsymbol A^{-1}$. If it exists, $\boldsymbol A$ is regular/invertible/nonsingular; otherwise singular/noninvertible. When the inverse exists it is unique (p. 24).
- **2×2 remark (pp. 24–25).** For $\boldsymbol A=\begin{bmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{bmatrix}$ (2.21) and $\boldsymbol A'=\begin{bmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{bmatrix}$ (2.22):
$$\boldsymbol A\boldsymbol A'=(a_{11}a_{22}-a_{12}a_{21})\boldsymbol I \tag{2.23}$$
$$\boldsymbol A^{-1}=\frac{1}{a_{11}a_{22}-a_{12}a_{21}}\begin{bmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{bmatrix}\quad\text{if and only if } a_{11}a_{22}-a_{12}a_{21}\ne0 \tag{2.24}$$
  This quantity is the determinant (Section 4.1); in general the determinant can be used to check invertibility (p. 25).
- **Example 2.4 (p. 25):** $\boldsymbol A=\begin{bmatrix}1&2&1\\4&4&5\\6&7&7\end{bmatrix}$ and $\boldsymbol B=\begin{bmatrix}-7&-7&6\\2&1&-1\\4&5&-4\end{bmatrix}$ satisfy $\boldsymbol A\boldsymbol B=\boldsymbol I=\boldsymbol B\boldsymbol A$.
- **Definition 2.4 (Transpose).** For $\boldsymbol A\in\mathbb R^{m\times n}$, $\boldsymbol B=\boldsymbol A^\top\in\mathbb R^{n\times m}$ with $b_{ij}=a_{ji}$ (columns of A become rows) (p. 25).
- Properties (p. 25): $\boldsymbol A\boldsymbol A^{-1}=\boldsymbol I=\boldsymbol A^{-1}\boldsymbol A$ (2.26); $(\boldsymbol A\boldsymbol B)^{-1}=\boldsymbol B^{-1}\boldsymbol A^{-1}$ (2.27); $(\boldsymbol A+\boldsymbol B)^{-1}\ne\boldsymbol A^{-1}+\boldsymbol B^{-1}$ in general (2.28), with scalar case $\frac1{2+4}=\frac16\ne\frac12+\frac14$; $(\boldsymbol A^\top)^\top=\boldsymbol A$ (2.29); $(\boldsymbol A\boldsymbol B)^\top=\boldsymbol B^\top\boldsymbol A^\top$ (2.30); $(\boldsymbol A+\boldsymbol B)^\top=\boldsymbol A^\top+\boldsymbol B^\top$ (2.31).
- **Definition 2.5.** $\boldsymbol A\in\mathbb R^{n\times n}$ is symmetric if $\boldsymbol A=\boldsymbol A^\top$. Only square matrices can be symmetric. If $\boldsymbol A$ is invertible, so is $\boldsymbol A^\top$, and $(\boldsymbol A^{-1})^\top=(\boldsymbol A^\top)^{-1}=:\boldsymbol A^{-\top}$ (p. 25).
- **Remark (p. 25).** A sum of symmetric matrices is always symmetric. Their product is always defined but generally not symmetric: $\begin{bmatrix}1&0\\0&0\end{bmatrix}\begin{bmatrix}1&1\\1&1\end{bmatrix}=\begin{bmatrix}1&1\\0&0\end{bmatrix}$ (2.32).

**2.2.3 Multiplication by a scalar (pp. 25–26).** $\lambda\boldsymbol A=\boldsymbol K$ with $K_{ij}=\lambda a_{ij}$. Scalars can be moved around: $(\lambda\psi)\boldsymbol C=\lambda(\psi\boldsymbol C)$, $\lambda(\boldsymbol B\boldsymbol C)=(\lambda\boldsymbol B)\boldsymbol C=\boldsymbol B(\lambda\boldsymbol C)=(\boldsymbol B\boldsymbol C)\lambda$, and $(\lambda\boldsymbol C)^\top=\lambda\boldsymbol C^\top$ since $\lambda=\lambda^\top$. Distributivity: $(\lambda+\psi)\boldsymbol C=\lambda\boldsymbol C+\psi\boldsymbol C$ and $\lambda(\boldsymbol B+\boldsymbol C)=\lambda\boldsymbol B+\lambda\boldsymbol C$. **Example 2.5** checks the first for $\boldsymbol C=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ (2.33–2.34).

**2.2.4 Compact representation (p. 26).** The system $2x_1+3x_2+5x_3=1$, $4x_1-2x_2-7x_3=8$, $9x_1+5x_2-3x_3=2$ (2.35) becomes $\begin{bmatrix}2&3&5\\4&-2&-7\\9&5&-3\end{bmatrix}\boldsymbol x=\begin{bmatrix}1\\8\\2\end{bmatrix}$ (2.36). Here $x_1$ scales column 1, $x_2$ column 2, $x_3$ column 3. In general $\boldsymbol A\boldsymbol x=\boldsymbol b$, and $\boldsymbol A\boldsymbol x$ is a (linear) combination of the columns of $\boldsymbol A$ (p. 26).

*Intuition note.* Writing Ax = b says "find the weights x that mix the columns of A to make b". The matrix is just a tidy container for the column vectors.

### 2.3 Solving Systems of Linear Equations (pp. 27–35)
Setting: $\boldsymbol A\boldsymbol x=\boldsymbol b$ with known constants $a_{ij},b_i$ and unknowns $x_j$ (2.37) (p. 27).

**2.3.1 Particular and general solution (pp. 27–28).**
- Example (2.38): $\begin{bmatrix}1&0&8&-4\\0&1&2&12\end{bmatrix}\boldsymbol x=\begin{bmatrix}42\\8\end{bmatrix}$. Two equations, four unknowns, so in general we expect infinitely many solutions (p. 27).
- Write $\boldsymbol c_i$ for column i. Since $\boldsymbol b=42\boldsymbol c_1+8\boldsymbol c_2$ (2.39), $[42,8,0,0]^\top$ is a *particular (special) solution* (p. 27).
- To find the other solutions, generate **0** non-trivially from the columns. Because $\begin{bmatrix}8\\2\end{bmatrix}=8\boldsymbol c_1+2\boldsymbol c_2$ (2.40), we have $\boldsymbol 0=8\boldsymbol c_1+2\boldsymbol c_2-\boldsymbol c_3+0\boldsymbol c_4$, so $(8,2,-1,0)$ solves $\boldsymbol A\boldsymbol x=\boldsymbol 0$, as does any multiple $\lambda_1$ of it (2.41). Likewise $-4\boldsymbol c_1+12\boldsymbol c_2-\boldsymbol c_4=\boldsymbol 0$ gives $\lambda_2(-4,12,0,-1)$ (2.42) (p. 28).
- **General solution** (2.43):
$$\Big\{\boldsymbol x\in\mathbb R^4:\ \boldsymbol x=\begin{bmatrix}42\\8\\0\\0\end{bmatrix}+\lambda_1\begin{bmatrix}8\\2\\-1\\0\end{bmatrix}+\lambda_2\begin{bmatrix}-4\\12\\0\\-1\end{bmatrix},\ \lambda_1,\lambda_2\in\mathbb R\Big\}$$
- **Three-step approach (remark, p. 28):** (1) find a particular solution of $\boldsymbol A\boldsymbol x=\boldsymbol b$; (2) find all solutions of $\boldsymbol A\boldsymbol x=\boldsymbol 0$; (3) combine them. Neither the general nor the particular solution is unique.
- This system was easy because of its special form. Gaussian elimination transforms any system into such a form by elementary transformations (p. 28).

*Intuition note.* Adding any solution of Ax = 0 to a solution of Ax = b gives another solution of Ax = b, because the added part contributes nothing. That is why the answer is "one solution plus a family of null-solutions".

**2.3.2 Elementary transformations (pp. 28–33).**
- Three operations keep the solution set the same (pp. 28–29): exchange two equations (rows); multiply a row by a constant $\lambda\in\mathbb R\setminus\{0\}$; add two rows.
- **Example 2.6 (pp. 29–30).** Find all solutions for $a\in\mathbb R$ of (2.44):
  $-2x_1+4x_2-2x_3-x_4+4x_5=-3$; $4x_1-8x_2+3x_3-3x_4+x_5=2$; $x_1-2x_2+x_3-x_4+x_5=0$; $x_1-2x_2-3x_4+4x_5=a$.
  - Build the *augmented matrix* $[\boldsymbol A\,|\,\boldsymbol b]$. Swap rows 1 and 3.
  - Subtract $4R_1$ from $R_2$, add $2R_1$ to $R_3$, subtract $R_1$ from $R_4$. This gives rows $(1,-2,1,-1,1|0)$, $(0,0,-1,1,-3|2)$, $(0,0,0,-3,6|-3)$, $(0,0,-1,-2,3|a)$.
  - Replace $R_4$ by $R_4-R_2-R_3$, giving $(0,0,0,0,0|a+1)$. Multiply $R_2$ by $-1$ and $R_3$ by $-\tfrac13$.
  - The result is the *row-echelon form* (REF) (2.45): $x_1-2x_2+x_3-x_4+x_5=0$; $x_3-x_4+3x_5=-2$; $x_4-2x_5=1$; $0=a+1$.
  - Only for $a=-1$ can the system be solved.
  - Particular solution: $[2,0,-1,1,0]^\top$ (2.46).
  - General solution (2.47): $\boldsymbol x=[2,0,-1,1,0]^\top+\lambda_1[2,1,0,0,0]^\top+\lambda_2[2,0,-1,2,1]^\top$, $\lambda_1,\lambda_2\in\mathbb R$.
- **Remark (pivots, p. 30).** The leading coefficient (first nonzero entry from the left) of a row is its *pivot*. It lies strictly to the right of the pivot above, giving a "staircase".
- **Definition 2.6 (REF, p. 30).** A matrix is in row-echelon form if (i) all-zero rows are at the bottom, and (ii) among nonzero rows, each pivot is strictly to the right of the pivot above. Some other texts require pivot = 1.
- **Basic/free variables (p. 30).** Variables at pivot columns are *basic*, the rest *free*. In (2.45), $x_1,x_3,x_4$ are basic and $x_2,x_5$ free.
- **Obtaining a particular solution (p. 31).** Write $\boldsymbol b=\sum_{i=1}^{P}\lambda_i\boldsymbol p_i$ with $\boldsymbol p_i$ the pivot columns. Solve for the $\lambda_i$ starting from the rightmost pivot column. Non-pivot variables are set to 0. For Example 2.6, (2.48) is $\lambda_1[1,0,0,0]^\top+\lambda_2[1,1,0,0]^\top+\lambda_3[-1,-1,1,0]^\top=[0,-2,1,0]^\top$, so $\lambda_3=1,\lambda_2=-1,\lambda_1=2$ and $\boldsymbol x=[2,0,-1,1,0]^\top$.
- **Reduced row-echelon form (RREF)** (remark, p. 31): REF, every pivot is 1, and each pivot is the only nonzero entry in its column. **Gaussian elimination** is the algorithm that uses elementary transformations to bring a system into RREF.
- **Example 2.7 (pp. 31–32).** $\boldsymbol A=\begin{bmatrix}1&3&0&0&3\\0&0&1&0&9\\0&0&0&1&-4\end{bmatrix}$ (2.49) is in RREF. To solve $\boldsymbol A\boldsymbol x=\boldsymbol 0$, express each non-pivot column via pivot columns on its left.
  - Column 2 = 3 × column 1, so subtract column 2 from 3 × column 1 to get **0**.
  - Column 5 = 3 × col 1 + 9 × col 3 + (−4) × col 4, giving $(3,0,9,-4,-1)$.
  - All solutions of $\boldsymbol A\boldsymbol x=\boldsymbol 0$: $\lambda_1[3,-1,0,0,0]^\top+\lambda_2[3,0,9,-4,-1]^\top$ (2.50).

**2.3.3 The minus-1 trick (pp. 32–33).**
- Purpose: read off solutions of homogeneous $\boldsymbol A\boldsymbol x=\boldsymbol 0$, $\boldsymbol A\in\mathbb R^{k\times n}$ (p. 32).
- Assume $\boldsymbol A$ is in RREF with no zero rows (2.51). The pivot columns $j_1..j_k$ are the unit vectors $\boldsymbol e_1..\boldsymbol e_k\in\mathbb R^k$. Extend to an $n\times n$ matrix $\tilde{\boldsymbol A}$ by inserting $n-k$ rows $[0\cdots0\ -1\ 0\cdots0]$ (2.52) at the places where pivots on the diagonal are missing, so the diagonal holds 1 or −1.
- The columns of $\tilde{\boldsymbol A}$ that contain −1 on the diagonal are solutions of $\boldsymbol A\boldsymbol x=\boldsymbol 0$. More precisely, they form a basis (Section 2.6.1) of the solution space, later called the kernel or null space (p. 33).
- **Example 2.8 (p. 33).** For (2.53) (= the matrix (2.49)), the 5×5 matrix is (2.54) with extra rows $(0,-1,0,0,0)$ and $(0,0,0,0,-1)$. Its −1 columns give (2.55), identical to (2.50).

*Intuition note.* Each −1 cancels exactly one free variable's column against the pivot columns. So each −1 column is one "free direction" of the solution set.

**Calculating the inverse (p. 33).** To find $\boldsymbol A^{-1}$, solve $\boldsymbol A\boldsymbol X=\boldsymbol I_n$ for $\boldsymbol X=[\boldsymbol x_1|\cdots|\boldsymbol x_n]$. In augmented notation
$$[\boldsymbol A\,|\,\boldsymbol I_n]\ \rightsquigarrow\cdots\rightsquigarrow\ [\boldsymbol I_n\,|\,\boldsymbol A^{-1}] \tag{2.56}$$
So finding an inverse is equivalent to solving linear systems.

**Example 2.9 (p. 34).** For $\boldsymbol A=\begin{bmatrix}1&0&2&0\\1&1&0&0\\1&2&0&1\\1&1&1&1\end{bmatrix}$ (2.57), elimination yields RREF with right-hand block
$$\boldsymbol A^{-1}=\begin{bmatrix}-1&2&-2&2\\1&-1&2&-2\\1&-1&1&-1\\-1&0&-1&2\end{bmatrix}\tag{2.58}$$
The author says to check this by confirming $\boldsymbol A\boldsymbol A^{-1}=\boldsymbol I_4$.

**2.3.4 Algorithms for solving Ax = b (pp. 34–35).**
- Assume a solution exists. If none exists, approximate solutions are needed (not covered here; linear regression, Ch. 9) (p. 34).
- If $\boldsymbol A$ is square and invertible, $\boldsymbol x=\boldsymbol A^{-1}\boldsymbol b$ (often not applicable). Otherwise, under the mild assumption that $\boldsymbol A$ has linearly independent columns:
$$\boldsymbol A\boldsymbol x=\boldsymbol b\iff\boldsymbol A^\top\boldsymbol A\boldsymbol x=\boldsymbol A^\top\boldsymbol b\iff\boldsymbol x=(\boldsymbol A^\top\boldsymbol A)^{-1}\boldsymbol A^\top\boldsymbol b\tag{2.59}$$
  $(\boldsymbol A^\top\boldsymbol A)^{-1}\boldsymbol A^\top$ is the *Moore–Penrose pseudo-inverse*. The author says the resulting solution also corresponds to the minimum-norm least-squares solution (pp. 34–35).
- Drawbacks: many computations (matrix–matrix product, inverse of $\boldsymbol A^\top\boldsymbol A$). For numerical precision, computing an inverse or pseudo-inverse is generally not recommended (p. 35).
- Gaussian elimination is used for determinants (Section 4.1), checking linear independence (Section 2.5), inverses (Section 2.2.2), rank (Section 2.6.2) and bases (Section 2.6.1). It is practical for thousands of variables but impractical for millions, since the operation count scales cubically in the number of equations (p. 35).
- In practice, large systems are solved indirectly by stationary iterative methods (Richardson, Jacobi, Gauß–Seidel, successive over-relaxation) or Krylov subspace methods (conjugate gradients, generalized minimal residual, biconjugate gradients) (p. 35).
- Key idea of iterative methods: with $\boldsymbol x^*$ a solution, set up
$$\boldsymbol x^{(k+1)}=\boldsymbol C\boldsymbol x^{(k)}+\boldsymbol d\tag{2.60}$$
  for suitable $\boldsymbol C,\boldsymbol d$, so that the residual error $\|\boldsymbol x^{(k+1)}-\boldsymbol x^*\|$ shrinks each iteration and converges to $\boldsymbol x^*$. Norms are introduced in Section 3.1 (p. 35).

### 2.4 Vector Spaces (pp. 35–40)
Plan: formalize "objects that can be added and scaled", starting with groups (p. 35).

**2.4.1 Groups (pp. 36–37).**
- **Definition 2.7 (Group).** A set $\mathcal G$ with an operation $\otimes:\mathcal G\times\mathcal G\to\mathcal G$ is a group $G=(\mathcal G,\otimes)$ if: (1) closure: $x\otimes y\in\mathcal G$; (2) associativity: $(x\otimes y)\otimes z=x\otimes(y\otimes z)$; (3) neutral element $e$: $x\otimes e=x=e\otimes x$; (4) inverse: for each $x$ some $y$ with $x\otimes y=e=y\otimes x$ (written $x^{-1}$). The quantifiers differ: closure holds for all $x,y$; associativity for all $x,y,z$; one neutral element $e$ must work for every $x$ ($\exists e\,\forall x$); each $x$ has its own inverse $y$ ($\forall x\,\exists y$) (p. 36).
- **Remark.** The inverse is defined with respect to ⊗ and does not necessarily mean $1/x$ (p. 36).
- If also $x\otimes y=y\otimes x$ for all $x,y$, the group is **Abelian** (commutative) (p. 36).
- **Example 2.10 (p. 36–37).**
  - $(\mathbb Z,+)$ is an Abelian group.
  - $(\mathbb N_0,+)$ is not a group (0 is neutral, but inverses are missing).
  - $(\mathbb Z,\cdot)$ is not a group (inverses missing for $z\ne\pm1$).
  - $(\mathbb R,\cdot)$ is not a group (0 has no inverse), but $(\mathbb R\setminus\{0\},\cdot)$ is Abelian.
  - $(\mathbb R^n,+)$, $(\mathbb Z^n,+)$ with componentwise addition (2.61) are Abelian. The inverse of $(x_1..x_n)$ is $(-x_1..-x_n)$ and $e=(0..0)$.
  - $(\mathbb R^{m\times n},+)$ is Abelian.
  - $(\mathbb R^{n\times n},\cdot)$: closure and associativity follow from the definition of the product, $\boldsymbol I_n$ is neutral, and inverses exist exactly when $\boldsymbol A$ is regular. In exactly that case it is a group, called the general linear group (the author's wording; Definition 2.8 below states it as the set of regular matrices) (p. 37).
- **Definition 2.8 (General linear group).** The set of regular (invertible) matrices in $\mathbb R^{n\times n}$ is a group under matrix multiplication, called $GL(n,\mathbb R)$. It is not Abelian because matrix multiplication is not commutative (p. 37).

**2.4.2 Vector spaces (pp. 37–38).**
- Groups have an *inner operation* ($\mathcal G\times\mathcal G\to\mathcal G$). A vector space adds an *outer operation* (scalar × vector). These have nothing to do with inner/outer products (p. 37).
- **Definition 2.9 (Vector space).** A real vector space $V=(\mathcal V,+,\cdot)$ is a set $\mathcal V$ with $+:\mathcal V\times\mathcal V\to\mathcal V$ (2.62) and $\cdot:\mathbb R\times\mathcal V\to\mathcal V$ (2.63), such that (p. 37):
  1. $(\mathcal V,+)$ is an Abelian group.
  2. Distributivity: $\lambda\cdot(\boldsymbol x+\boldsymbol y)=\lambda\cdot\boldsymbol x+\lambda\cdot\boldsymbol y$ and $(\lambda+\psi)\cdot\boldsymbol x=\lambda\cdot\boldsymbol x+\psi\cdot\boldsymbol x$.
  3. Associativity (outer): $\lambda\cdot(\psi\cdot\boldsymbol x)=(\lambda\psi)\cdot\boldsymbol x$.
  4. Neutral element for the outer operation: $1\cdot\boldsymbol x=\boldsymbol x$.
  Elements of $\mathcal V$ are vectors; the neutral element of $(\mathcal V,+)$ is the zero vector $\boldsymbol 0$; elements of $\mathbb R$ are scalars. A scalar product is something different (Section 3.2).
- **Remark (p. 37–38).** "Vector multiplication" $\boldsymbol a\boldsymbol b$ is not defined. Elementwise "array multiplication" exists in programming languages but makes mathematically limited sense. Treating vectors as n×1 matrices, only two products are defined: $\boldsymbol a\boldsymbol b^\top\in\mathbb R^{n\times n}$ (outer product) and $\boldsymbol a^\top\boldsymbol b\in\mathbb R$ (inner/scalar/dot product).
- **Example 2.11 (p. 38).** Vector spaces: $\mathbb R^n$ (componentwise addition and scaling); $\mathbb R^{m\times n}$ (elementwise addition, scaling as in Section 2.2; equivalent to $\mathbb R^{mn}$); $\mathbb C$ with standard complex addition.
- **Remark (p. 38).** $\mathbb R^n$, $\mathbb R^{n\times1}$, $\mathbb R^{1\times n}$ differ only in how vectors are written. The book does not distinguish $\mathbb R^n$ and $\mathbb R^{n\times1}$ (column vectors, 2.64), but does distinguish row vectors $\mathbb R^{1\times n}$, to avoid confusion with matrix multiplication. By default $\boldsymbol x$ is a column and $\boldsymbol x^\top$ a row.

**2.4.3 Vector subspaces (p. 39–40).**
- Intuition: sets inside a vector space so that vector-space operations on their elements never leave them, i.e. they are "closed". Vector subspaces are used for dimensionality reduction in Ch. 10 (p. 39).
- **Definition 2.10.** For a vector space $V=(\mathcal V,+,\cdot)$ and $\mathcal U\subseteq\mathcal V$, $\mathcal U\ne\emptyset$, $U=(\mathcal U,+,\cdot)$ is a (vector/linear) subspace if $U$ is itself a vector space with the operations restricted to $\mathcal U$ (p. 39).
- $U$ inherits the Abelian-group, distributivity, associativity and neutral-element properties from $V$. What still must be shown (p. 39): (1) $\mathcal U\ne\emptyset$, in particular $\boldsymbol 0\in\mathcal U$; (2) closure under the outer operation ($\lambda\boldsymbol x\in\mathcal U$) and under the inner operation ($\boldsymbol x+\boldsymbol y\in\mathcal U$).
- **Example 2.12 (p. 39).**
  - The trivial subspaces of any $V$ are $V$ and $\{\boldsymbol 0\}$.
  - In Figure 2.6 only D is a subspace of $\mathbb R^2$. A and C violate closure; B does not contain $\boldsymbol 0$.
  - The solution set of a homogeneous system $\boldsymbol A\boldsymbol x=\boldsymbol 0$ with n unknowns is a subspace of $\mathbb R^n$.
  - The solution set of an inhomogeneous system $\boldsymbol A\boldsymbol x=\boldsymbol b$, $\boldsymbol b\ne\boldsymbol 0$, is not a subspace.
  - The intersection of arbitrarily many subspaces is a subspace.
- **Remark (p. 40).** Every subspace of $(\mathbb R^n,+,\cdot)$ is the solution space of some homogeneous system $\boldsymbol A\boldsymbol x=\boldsymbol 0$.

*Intuition note.* A subspace is a flat set through the origin: adding or stretching its members keeps you inside. Solutions of Ax = 0 qualify. Solutions of Ax = b with b ≠ 0 do not, because they miss the origin.

### 2.5 Linear Independence (pp. 40–43)
- Motivation: it is possible to find a set of vectors with which every vector of the space can be represented by adding and scaling; this set is called a *basis* (Section 2.6.1, not covered in this unit). Linear combinations and independence come first (p. 40).
- **Definition 2.11 (Linear combination).** For $\boldsymbol x_1..\boldsymbol x_k\in V$, every $\boldsymbol v=\lambda_1\boldsymbol x_1+\dots+\lambda_k\boldsymbol x_k=\sum_{i=1}^k\lambda_i\boldsymbol x_i\in V$ with $\lambda_i\in\mathbb R$ is a linear combination (2.65). **0** can always be written as the *trivial* combination $\sum 0\cdot\boldsymbol x_i$; the interest is in non-trivial ones with not all $\lambda_i=0$ (p. 40).
- **Definition 2.12 (Linear (in)dependence).** If a non-trivial combination gives $\boldsymbol 0=\sum\lambda_i\boldsymbol x_i$ with at least one $\lambda_i\ne0$, the vectors are linearly dependent. If only the trivial solution $\lambda_1=\dots=\lambda_k=0$ exists, they are linearly independent (p. 40). Intuitively: independent vectors have no redundancy; removing any one loses something.
- **Example 2.13 (pp. 40–41; Figure 2.7).** In the plane of geography (ignoring altitude and the Earth's curvature): from Nairobi, "506 km Northwest" (to Kampala) then "374 km Southwest" reaches Kigali. These two vectors are linearly independent. The extra statement "751 km West" is a linear combination of them, so the three vectors are linearly dependent. Equivalently, 751 km West and 374 km Southwest can be combined to give 506 km Northwest.
- **Remark: useful properties (pp. 41–42).**
  - k vectors are either linearly dependent or independent; there is no third option.
  - If at least one vector is **0**, they are dependent. The same holds if two vectors are identical.
  - For nonzero vectors $\boldsymbol x_1..\boldsymbol x_k$, $k\ge2$: dependent if and only if at least one is a linear combination of the others. In particular, if $\boldsymbol x_i=\lambda\boldsymbol x_j$ the set is dependent.
  - Practical test: write the vectors as columns of $\boldsymbol A$ and do Gaussian elimination to row-echelon form (RREF unnecessary). Pivot columns indicate vectors that are linearly independent of the vectors on their left (order matters). Non-pivot columns are linear combinations of the pivot columns on their left. E.g. the REF $\begin{bmatrix}1&3&0\\0&0&2\end{bmatrix}$ (2.66) has pivot columns 1 and 3; column 2 is 3 × column 1.
  - All column vectors are linearly independent if and only if all columns are pivot columns. With at least one non-pivot column, they are dependent.
- **Example 2.14 (p. 42).** In $\mathbb R^4$: $\boldsymbol x_1=[1,2,-3,4]^\top$, $\boldsymbol x_2=[1,1,0,2]^\top$, $\boldsymbol x_3=[-1,-2,1,1]^\top$ (2.67). Solving $\lambda_1\boldsymbol x_1+\lambda_2\boldsymbol x_2+\lambda_3\boldsymbol x_3=\boldsymbol 0$ (2.68), elimination gives rows $(1,1,-1)$, $(0,1,0)$, $(0,0,1)$, $(0,0,0)$ (2.69). Every column is a pivot column, so only $\lambda_1=\lambda_2=\lambda_3=0$ works and the vectors are linearly independent.
- **Remark (p. 43).** Let $\boldsymbol b_1..\boldsymbol b_k$ be linearly independent and $\boldsymbol x_j=\sum_{i=1}^k\lambda_{ij}\boldsymbol b_i$, $j=1..m$ (2.70). With $\boldsymbol B=[\boldsymbol b_1,\dots,\boldsymbol b_k]$ and $\boldsymbol\lambda_j=[\lambda_{1j},\dots,\lambda_{kj}]^\top$ we get $\boldsymbol x_j=\boldsymbol B\boldsymbol\lambda_j$ (2.71). Then
$$\sum_{j=1}^m\psi_j\boldsymbol x_j=\sum_{j=1}^m\psi_j\boldsymbol B\boldsymbol\lambda_j=\boldsymbol B\sum_{j=1}^m\psi_j\boldsymbol\lambda_j\tag{2.72}$$
  Hence $\{\boldsymbol x_1..\boldsymbol x_m\}$ are linearly independent if and only if $\{\boldsymbol\lambda_1..\boldsymbol\lambda_m\}$ are.
- **Remark (p. 43).** m linear combinations of k vectors are linearly dependent if $m>k$.
- **Example 2.15 (p. 43, begins).** For independent $\boldsymbol b_1..\boldsymbol b_4\in\mathbb R^n$ and $\boldsymbol x_1..\boldsymbol x_4$ defined in (2.73), the question is whether the coefficient columns (2.74) are independent. The unit ends here, before the example is resolved.

*Intuition note.* "Independent" means no vector can be built from the others. In elimination, a non-pivot column is exactly such a redundant column, built from earlier pivot columns.

## Toy example (ours, not from the text)
Solve $\boldsymbol A\boldsymbol x=\boldsymbol b$ with $\boldsymbol A=\begin{bmatrix}1&0&2\\0&1&-1\end{bmatrix}$, $\boldsymbol b=\begin{bmatrix}3\\1\end{bmatrix}$. $\boldsymbol A$ is already in RREF: pivot columns 1 and 2, so $x_3$ is free.
1. **Particular solution:** $\boldsymbol b=3\boldsymbol c_1+1\boldsymbol c_2$, so $\boldsymbol x_p=(3,1,0)$.
2. **Null solutions:** column 3 is $2\boldsymbol c_1-1\boldsymbol c_2$, so $2\boldsymbol c_1-\boldsymbol c_2-\boldsymbol c_3=\boldsymbol 0$ and $\boldsymbol n=(2,-1,-1)$. Check: $\boldsymbol A\boldsymbol n=(2+0-2,\ 0-1+1)=(0,0)$.
3. **Minus-1 trick:** insert the row $(0,0,-1)$ to get $\tilde{\boldsymbol A}=\begin{bmatrix}1&0&2\\0&1&-1\\0&0&-1\end{bmatrix}$. Its column 3 is $(2,-1,-1)$, the same $\boldsymbol n$.
4. **General solution:** $\boldsymbol x=(3,1,0)+\lambda(2,-1,-1)$. For $\lambda=1$: $\boldsymbol x=(5,0,-1)$, and $\boldsymbol A\boldsymbol x=(5-2,\ 0+1)=(3,1)$ ✓.
5. **Independence link:** column 3 is a non-pivot column, so the three columns of $\boldsymbol A$ are linearly dependent.

## Concepts
- [[vector]] — any object that can be added and scaled with a result of the same kind; the book mostly uses elements of Rⁿ (p. 17)
- [[linear combination]] — $\sum\lambda_i\boldsymbol x_i$; Ax is a linear combination of the columns of A (pp. 26, 40)
- [[linear independence]] — only the trivial combination gives 0; tested by pivot columns in REF (pp. 40–42)
- [[inverse matrix]] — B with AB = I = BA; unique if it exists; 2×2 formula valid iff $a_{11}a_{22}-a_{12}a_{21}\ne0$; found by $[A|I]\rightsquigarrow[I|A^{-1}]$ (pp. 24, 33)
- [[pseudoinverse]] — here $(A^\top A)^{-1}A^\top$ for A with independent columns; gives the minimum-norm least-squares solution (pp. 34–35)
- [[null space (kernel)]] — solution space of Ax = 0; named only as a forward reference, basis read by the minus-1 trick (p. 33)
- [[basis]] — only previewed: a set of vectors that can represent every vector of the space (p. 40)
- [[Krylov subspace methods]] — iterative solvers for large systems, named (conjugate gradients, etc.) (p. 35)
- [[system-of-linear-equations]] (new) — $a_{i1}x_1+\dots+a_{in}x_n=b_i$, written $Ax=b$ (pp. 20, 22)
- [[matrix-multiplication]] (new) — $c_{ij}=\sum_l a_{il}b_{lj}$; needs matching inner dimensions; not commutative (pp. 22–23)
- [[transpose]] (new) — $b_{ij}=a_{ji}$; $(AB)^\top=B^\top A^\top$ (p. 25)
- [[gaussian-elimination]] (new) — elementary row operations bringing a system to RREF (pp. 29, 31)
- [[row-echelon-form]] (new) — zero rows at the bottom, pivots strictly staircase to the right; RREF adds pivot = 1 and zeros above and below pivots (pp. 30–31)
- [[particular-and-general-solution]] (new) — general = particular + all solutions of Ax = 0 (p. 28)
- [[minus-1-trick]] (new) — pad RREF with −1 rows to read off the solutions of Ax = 0 (pp. 32–33)
- [[group]] (new) — set with an operation satisfying closure, associativity, neutral element, inverses; Abelian if commutative (p. 36)
- [[vector-space]] (new) — Abelian group (V, +) plus scalar multiplication with distributivity, associativity and 1·x = x (p. 37)
- [[vector-subspace]] (new) — nonempty subset (containing 0) closed under addition and scaling (p. 39)

## Canonical instances
- [[production-plan-example]] — resource-use problem that leads to a linear system (p. 19)
- [[nairobi-kigali-example]] — geographic example of linearly dependent vectors in the plane (pp. 40–41)
- [[general-linear-group]] — invertible n×n matrices form a non-Abelian group under multiplication (p. 37)
- [[gaussian-elimination-inverse-example]] — 4×4 inverse found via $[A|I]$ (p. 34)
- [[non-subspace-gallery]] — Figure 2.6, four subsets of R², of which only D is a subspace (p. 39)

## Bridges (candidates)
- [structural-analogy] pivot columns in REF ↔ linear-algebra: rank — the unit uses pivots to test independence; the rank link is only forward-referenced here (p. 35).
- [same-math] $x=(A^\top A)^{-1}A^\top b$ ↔ least squares: normal equations $A^\top Ax=A^\top b$ — same equation, which the unit equates with the minimum-norm least-squares solution.
- [structural-analogy] iteration $x^{(k+1)}=Cx^{(k)}+d$ ↔ power iteration: repeated application of a matrix — both repeat a matrix map until convergence, though the update rules differ.
- [structural-analogy] "closure under operations" for subspaces ↔ group closure: both ask whether operations stay inside the set.

## Questions this raises
- When does Gaussian elimination give no solution, exactly one, or infinitely many, in terms of pivot columns? (The examples hint at it: the row $0=a+1$, free variables.)
- Why is computing $A^{-1}$ discouraged numerically (p. 35), and what do iterative methods gain?
- How do the number of pivots and the number of free variables relate to the dimension of the solution space (basis, rank; Sections 2.6.1–2.6.2)?
- Why does a subspace of Rⁿ always arise as the solution set of some Ax = 0 (remark, p. 40)?

## Reading notes
- This is part 1 of Chapter 2. It starts at the chapter opening (printed p. 17, pdf 23) and ends at the bottom of printed p. 43 (pdf 49), in the middle of Example 2.15. The unit metadata says the split is at a section boundary, but on these pages the text breaks inside Example 2.15 of Section 2.5; the rest of Section 2.5 and the later sections (e.g. 2.6 and 2.7, which the text refers to) are not covered.
- Page offset: printed = pdf − 6. All page labels carried printed numbers.
- No page image was supplied for pdf 41 (printed 35); that page was checked from the text layer only, where nothing was garbled.
- The text layers of the equation pages were garbled in places (matrices, Example 2.6 row operations). I checked all matrices and row operations against the page images and re-verified the arithmetic of Examples 2.2, 2.6, 2.7, 2.9 and the matrix products in Example 2.3.
- The unit contains no end-of-chapter exercises, so there is no Exercises section. Most margin notes in the source (links to video courses, Python `einsum`, definition of the main diagonal) were not digested; the notes on the pivot = 1 convention (p. 30) and the scalar case of (2.28) (p. 25) were used.
