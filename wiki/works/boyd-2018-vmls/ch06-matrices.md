---
id: boyd-2018-vmls/ch06-matrices
work: boyd-2018-vmls
unit: Chapter 6 — Matrices
pages: 107-127
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Matrices

## L0 — One line
A matrix is a rectangular table of numbers that can be read by rows or by columns, and the product $y = Ax$ is both a set of row inner products and a linear combination of the columns of $A$.

## L1 — The gist (≤ 120 words)
This chapter introduces matrices as tables of numbers: notation, block structure, special shapes (zero, identity, sparse, diagonal, triangular, symmetric), and basic operations (transpose, addition, scalar multiplication, a norm). It then turns to matrix-vector multiplication. The product $y = Ax$ can be read row by row, as inner products, or column by column, as a linear combination of the columns of $A$. Many practical computations are of this form: portfolio returns, polynomial evaluation at many points, document scoring, audio mixing. The chapter also counts the cost of these operations (memory and flops), showing that sparsity cuts cost. The text points ahead to later uses (§7.3, §10.1).

**Prerequisites:** vectors, inner product, vector norm, linear independence and basis; the idea of a flop count; summation notation.

## L2 — Key ideas (5–10 bullets)
- A matrix is a two-index table. Its columns and rows are vectors, and block notation (concatenating and stacking) lets us write a matrix as its columns or its rows. (pp. 107–110)
- Matrices represent data: images, time series, price tables, contingency tables, collections of feature vectors, and relations or directed graphs via the adjacency matrix. (pp. 110–112)
- Special structures matter: identity ($Ix = x$), diagonal, triangular, symmetric and sparse matrices. Sparsity means few nonzeros and brings efficient storage and computation. (pp. 113–116, 119, 123)
- Transpose swaps rows and columns; addition and scalar multiplication work entry by entry (scalar multiplication is defined as for vectors). The norm (6.3) is the root of the sum of squared entries, equal to the vector norm of the entries listed as one long vector; in contexts where other matrix norms are used, it is called the Frobenius norm. (pp. 115–118)
- $y=Ax$ has a row view ($y_i = b_i^T x$) and a column view ($y = x_1a_1+\dots+x_na_n$). Linear dependence, independence and basis expansion can be stated with $Ax$. (pp. 118–121)
- Many operations are matrix-vector products with special matrices: difference, running sum, Vandermonde, weighted scores, mixes. The entry $A_{ij}$ says how much $y_i$ depends on $x_j$. (pp. 119–122)
- Cost: a dense product takes about $2mn$ flops; a sparse one takes between $\mathbf{nnz}(A)$ and $2\,\mathbf{nnz}(A)$. Transposition costs zero flops. (pp. 122–123)

## L3 — Walkthrough

### 6.1 Matrices (pp. 107–112)

**Definition and notation.** A matrix is a rectangular array of numbers in brackets or parentheses. Its *size* is rows × columns; an $m\times n$ matrix has $m$ rows and $n$ columns (p. 107). The entry in row $i$, column $j$ is $A_{ij}$ (or $A_{i,j}$). Row indices run top to bottom, column indices left to right (p. 107). For the $3\times 4$ example matrix $B$ with rows $(0,1,-2.3,0.1)$, $(1.3,4,-0.1,0)$, $(4.1,-1,0,1.7)$: $B_{13}=-2.3$, $B_{32}=-1$ (p. 107). Two matrices are equal if they have the same size and all corresponding entries are equal. Entries are real unless stated otherwise; $\mathbf R^{m\times n}$ is the set of real $m\times n$ matrices (pp. 107–108).

**Indexing in software.** Mathematical notation starts at 1. Lower-level languages typically start at 0; higher-level matrix languages usually start at 1 (p. 108).

**Shapes.** A *square* matrix has equal numbers of rows and columns; $n\times n$ has *order* $n$. A *tall* matrix has $m>n$; a *wide* matrix has $n>m$ (p. 108).

**Vectors as matrices.** An $n$-vector is treated as an $n\times 1$ matrix (a *column vector*). A $1\times n$ matrix is a *row vector* ($n$-row-vector). A $1\times1$ matrix is the same as a scalar (p. 108). Many authors (including the book) tend to use capital letters for matrices and lower-case letters for vectors, but this is not standardized; the reader must infer from context (p. 108).

**Columns and rows.** For an $m\times n$ matrix $A$, the columns are the $m$-vectors $a_j = (A_{1j},\dots,A_{mj})$, $j=1,\dots,n$, and the rows are the $n$-row-vectors $b_i = [A_{i1}\ \cdots\ A_{in}]$, $i=1,\dots,m$ (p. 108). Example: $\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$ has first row $[1\ 2\ 3]$ and second column $(2,5)$ (p. 109).

**Block matrices.** A block matrix has matrices as entries, e.g. $A=\begin{bmatrix}B&C\\D&E\end{bmatrix}$; the entries are *blocks* or *submatrices*. Blocks must fit together: blocks in the same block row have the same height, and blocks in the same block column have the same width. Blocks side by side are *concatenated*; blocks above each other are *stacked* (p. 109). Example (6.1): with $B=[0\ 2\ 3]$, $C=[-1]$, $D=\begin{bmatrix}2&2&1\\1&3&5\end{bmatrix}$, $E=\begin{bmatrix}4\\4\end{bmatrix}$,
$$A=\begin{bmatrix}0&2&3&-1\\2&2&1&4\\1&3&5&4\end{bmatrix}.\tag{6.1}$$
Colon notation: for $1\le p\le q\le m$ and $1\le r\le s\le n$, $A_{p:q,r:s}$ is the submatrix of rows $p$ through $q$ and columns $r$ through $s$. Its size is $(q-p+1)\times(s-r+1)$ (pp. 109–110). For (6.1), $A_{2:3,3:4}=\begin{bmatrix}1&4\\5&4\end{bmatrix}$ (p. 110).

**Column and row representation.** $A=[a_1\ a_2\ \cdots\ a_n]$ (columns concatenated). Also $A$ is the stack of its rows $b_1,\dots,b_m$ (p. 110).

*Intuition note.* A matrix can be read as a table, as a row of column vectors, or as a column of row vectors. Block notation writes the same matrix in each of these three forms (p. 110).

**Examples (table interpretation, pp. 110–111).** A vector depends on one index, a matrix on two.
- *Images:* an $M\times N$ black-and-white image; row $i$ is vertical position, column $j$ horizontal position, entry is pixel value.
- *Rainfall:* $m\times n$ matrix, $m$ locations, $n$ days. $A_{42}$ is rainfall at location 4 on day 2; column $j$ is all locations on day $j$; row $i$ is the time series at location $i$.
- *Asset returns:* $T\times n$ matrix $R$, $R_{ij}$ the return of asset $j$ in period $i$. $R_{12,7}=-0.03$ means asset 7 lost 3% in period 12. Table 6.1 (daily returns of AAPL, GOOG, MMM, AMZN on March 1–3, 2016) has $n=4$, $T=3$:
$$R=\begin{bmatrix}0.00219&0.00006&-0.00113&0.00202\\0.00744&-0.00894&-0.00019&-0.00468\\0.01488&-0.00215&0.00433&-0.00407\end{bmatrix}.$$
- *Prices from multiple suppliers:* $P_{ij}$ is the price supplier $i$ charges for good $j$.
- *Contingency table:* $A_{ij}$ counts objects with first attribute $i$ and second attribute $j$. Example: a $4\times 50$ matrix, year of study by state.
- *Customer purchase history:* $n\times N$ matrix $P$; $P_{ij}$ is the dollar value (or quantity) of product $i$ bought by customer $j$.

**Collection of vectors.** If $x_1,\dots,x_N$ are $n$-vectors of features, then $X=[x_1\ \cdots\ x_N]$ is the $n\times N$ *data (feature) matrix*. $X_{ij}$ is the value of feature $i$ for example $j$. A $3\times M$ matrix can hold $M$ points in 3-D space (pp. 111–112).

**Relations and graphs.** A relation $\mathcal R$ on $\{1,\dots,n\}$ is a set of ordered pairs. It is drawn as a directed graph with an edge from $j$ to $i$ for each $(i,j)\in\mathcal R$. The *adjacency matrix* has $A_{ij}=1$ if $(i,j)\in\mathcal R$ and $0$ otherwise (some authors use the reverse convention) (p. 112). Example (6.2): $\mathcal R=\{(1,2),(1,3),(2,1),(2,4),(3,4),(4,1)\}$ gives
$$A=\begin{bmatrix}0&1&1&0\\1&0&0&1\\0&0&0&1\\1&0&0&0\end{bmatrix}$$
(figure 6.1 shows the graph) (p. 112).

### 6.2 Zero and identity matrices (pp. 113–115)

**Zero matrix.** All entries zero; usually written $0$, with size read from context (p. 113).

**Identity matrix.** Always square, with
$$I_{ij}=\begin{cases}1 & i=j\\ 0 & i\ne j\end{cases},\qquad i,j=1,\dots,n.$$
Its columns are the unit vectors: $I=[e_1\ e_2\ \cdots\ e_n]$ (p. 113). Sizes are usually inferred. Example: for $A=\begin{bmatrix}1&2&3\\4&5&6\end{bmatrix}$, the block matrix $\begin{bmatrix}I&A\\0&I\end{bmatrix}$ must have a $2\times2$ identity top left, a $3\times3$ identity bottom right, and a $3\times2$ zero block bottom left. It is the $5\times5$ matrix with rows $(1,0,1,2,3)$, $(0,1,4,5,6)$, $(0,0,1,0,0)$, $(0,0,0,1,0)$, $(0,0,0,0,1)$ (p. 113).

**Sparse matrices.** $A$ is sparse if many entries are zero. Its *sparsity pattern* is the set of $(i,j)$ with $A_{ij}\ne0$. $\mathbf{nnz}(A)$ is the number of nonzeros, so $\mathbf{nnz}(A)\le mn$. The *density* is $\mathbf{nnz}(A)/(mn)\le 1$; in applications it is typically small, e.g. $10^{-2}$ or $10^{-4}$ (p. 114). There is no precise cutoff. The author cites Wilkinson: "A matrix is sparse if it has enough zero entries that it pays to take advantage of them." (p. 114). The $n\times n$ identity has density $1/n$; the zero matrix is the sparsest possible. A typical customer purchase history matrix is sparse, since each customer has likely only purchased a small fraction of the products (p. 114).

**Diagonal matrices.** A square $A$ is diagonal if $A_{ij}=0$ for $i\ne j$; diagonal entries may themselves be zero. Notation: $\mathbf{diag}(a_1,\dots,a_n)$ has $A_{ii}=a_i$; also $I=\mathbf{diag}(\mathbf 1)$ (p. 114).

**Triangular matrices.** Upper triangular: $A_{ij}=0$ for $i>j$. Lower triangular: $A_{ij}=0$ for $i<j$. A diagonal matrix is both (p. 114). A triangular $n\times n$ matrix has up to $n(n+1)/2$ nonzeros, so density is around 50%. Triangular matrices are generally not called sparse, but their pattern will matter later (p. 115).

### 6.3 Transpose, addition, and norm (pp. 115–118)

#### 6.3.1 Matrix transpose
For $A\in\mathbf R^{m\times n}$, the transpose $A^T$ is the $n\times m$ matrix with $(A^T)_{ij}=A_{ji}$; rows and columns swap. Example: $\begin{bmatrix}0&4\\7&0\\3&1\end{bmatrix}^T=\begin{bmatrix}0&7&3\\4&0&1\end{bmatrix}$. Transposing twice returns $A$: $(A^T)^T=A$ (p. 115).

**Row vectors.** Transposition turns rows into columns and back, so a row vector can be written $a^T$. The $m$ rows of $A$ can be written $\tilde a_1^T,\dots,\tilde a_m^T$. Concepts for column vectors are extended to row vectors via their transposes: "the rows of $A$ are linearly independent" means the columns of $A^T$ are; "the rows are orthonormal" means the columns of $A^T$ are; "clustering the rows of $X$" means clustering the columns of $X^T$ (p. 115).

**Block transpose.** $\begin{bmatrix}A&B\\C&D\end{bmatrix}^T=\begin{bmatrix}A^T&C^T\\B^T&D^T\end{bmatrix}$: transpose the block layout and each block (p. 115).

**Document-term matrix.** For $N$ documents and a dictionary of $n$ words, $A$ is $N\times n$, with $A_{ij}$ the number of times word $j$ appears in document $i$. Rows are the word-count vectors $a_i^T$; column $j$ gives the count of word $j$ over the corpus (p. 116).

**Data matrix, two conventions.** A collection of $N$ $n$-vectors can be an $n\times N$ matrix (vectors as columns) or its transpose, an $N\times n$ matrix $X$ with $i$th row $x_i^T$. Context (e.g. dimensions) usually shows which is meant (p. 116).

**Symmetric matrix.** Square $A$ is symmetric if $A=A^T$, i.e. $A_{ij}=A_{ji}$ for all $i,j$. An adjacency matrix is symmetric when the relation is: whenever $(i,j)\in\mathcal R$, also $(j,i)\in\mathcal R$. Example: the friend relation (the "social network graph") (p. 116).

#### 6.3.2 Matrix addition
Same-size matrices add entry by entry; subtraction is similar. Example: $\begin{bmatrix}0&4\\7&0\\3&1\end{bmatrix}+\begin{bmatrix}1&2\\2&3\\0&4\end{bmatrix}=\begin{bmatrix}1&6\\9&3\\3&5\end{bmatrix}$, and $\begin{bmatrix}1&6\\9&3\end{bmatrix}-I=\begin{bmatrix}0&6\\9&2\end{bmatrix}$ (here $I$ must be $2\times2$) (p. 116). For same-size $A,B,C$ (p. 117):
- $A+B=B+A$ (commutativity);
- $(A+B)+C=A+(B+C)$ (associativity);
- $A+0=0+A=A$;
- $(A+B)^T=A^T+B^T$.

#### 6.3.3 Scalar-matrix multiplication
Multiply every entry by the scalar. Example: $(-2)\begin{bmatrix}1&6\\9&3\\6&0\end{bmatrix}=\begin{bmatrix}-2&-12\\-18&-6\\-12&0\end{bmatrix}$. The scalar may be on the right; $0A=0$. Properties: $(\beta A)^T=\beta(A^T)$, $(\beta+\gamma)A=\beta A+\gamma A$, $(\beta\gamma)A=\beta(\gamma A)$. In these, the same symbols mean different operations (scalar vs matrix addition or multiplication). Scalar-matrix multiplication takes precedence over addition (p. 117).

#### 6.3.4 Matrix norm
$$\|A\|=\sqrt{\sum_{i=1}^m\sum_{j=1}^n A_{ij}^2}.\tag{6.3}$$
For a vector ($n=1$) it agrees with the vector norm. It equals the norm of the $mn$-vector formed from the entries in any order. The RMS value of the entries, $\|A\|/\sqrt{mn}$, gives the typical entry size independent of dimensions (p. 118).

Norm properties (p. 118): $\|A\|\ge0$; $\|A\|=0$ only if $A=0$ (definiteness); $\|\gamma A\|=|\gamma|\,\|A\|$ (nonnegative homogeneity); and the triangle inequality $\|A+B\|\le\|A\|+\|B\|$. Distance between matrices is $\|A-B\|$. The book uses only (6.3), which elsewhere is called the Frobenius norm and written $\|A\|_F$ (p. 118). Two further properties (p. 118):
$$\|A\|=\|A^T\|,\qquad \|A\|^2=\|a_1\|^2+\cdots+\|a_n\|^2,$$
where $a_j$ are the columns of $A$. The squared norm of a matrix is the sum of the squared norms of its columns.

*Intuition note.* The matrix norm ignores the table shape and measures the total size of all entries. Matrix distance $\|A-B\|$ is then the ordinary vector distance of the flattened tables.

### 6.4 Matrix-vector multiplication (pp. 118–122)

**Definition.** For $A\in\mathbf R^{m\times n}$ and an $n$-vector $x$, $y=Ax$ is the $m$-vector
$$y_i=\sum_{k=1}^nA_{ik}x_k=A_{i1}x_1+\cdots+A_{in}x_n,\quad i=1,\dots,m.\tag{6.4}$$
Example: $\begin{bmatrix}0&2&-1\\-2&1&1\end{bmatrix}\begin{bmatrix}2\\1\\-1\end{bmatrix}=\begin{bmatrix}(0)(2)+(2)(1)+(-1)(-1)\\(-2)(2)+(1)(1)+(1)(-1)\end{bmatrix}=\begin{bmatrix}3\\-4\end{bmatrix}$ (p. 118).

**Row and column interpretations (p. 119).**
- Row view: $y_i=b_i^Tx$, the inner product of $x$ with row $i$.
- Column view: $y=x_1a_1+x_2a_2+\cdots+x_na_n$. So $Ax$ is a linear combination of the columns of $A$, with the entries of $x$ as coefficients.

*Intuition note.* The row view computes one output at a time. The column view builds the whole output at once by mixing the columns.

**General examples (p. 119).** $A$ is $m\times n$, $x$ an $n$-vector.
- $0x=0$; $Ix=x$.
- *Picking out:* $Ae_j=a_j$ (column $j$). $A^Te_i$ is row $i$ of $A$, transposed.
- *Sums and averages:* $A\mathbf 1$ is the sum of the columns (its $i$th entry is the sum of row $i$); $A(\mathbf 1/n)$ is the average of the columns; $A^T\mathbf 1$ has $j$th entry equal to the sum of column $j$.
- *Difference matrix* (6.5): the $(n-1)\times n$ matrix $D$ with $-1$ on the diagonal, $+1$ just above it, zeros elsewhere (rows $(-1,1,0,\dots,0)$, $(0,-1,1,0,\dots)$, …, $(0,\dots,0,-1,1)$). Then $Dx=(x_2-x_1,\ x_3-x_2,\ \dots,\ x_n-x_{n-1})$.
- *Running sum matrix* (6.6) (p. 120): the $n\times n$ lower-triangular matrix $S$ with ones on and below the diagonal. Then $(Sx)_i=x_1+\cdots+x_i$.

**Application examples (pp. 120–121).**
- *Scores:* with feature matrix $X$ ($n\times N$, columns $x_i$) and weight vector $w$, scores $s_i=x_i^Tw$ give $s=X^Tw$.
- *Portfolio return time series:* $R$ is $T\times n$, $w$ the (constant) weights; $Rw$ is the $T$-vector of portfolio returns. Negative entries of $w$ are short positions. With $R$ from table 6.1 and $w=(0.4,0.3,-0.2,0.5)$, $Rw=(0.00213,-0.00201,0.00241)$ (p. 120).
- *Polynomial evaluation:* with $p(t)=c_1+c_2t+\cdots+c_nt^{n-1}$ and points $t_1,\dots,t_m$, $y_i=p(t_i)$ gives $y=Ac$ with
$$A=\begin{bmatrix}1&t_1&\cdots&t_1^{n-2}&t_1^{n-1}\\1&t_2&\cdots&t_2^{n-2}&t_2^{n-1}\\\vdots&\vdots&&\vdots&\vdots\\1&t_m&\cdots&t_m^{n-2}&t_m^{n-1}\end{bmatrix},\tag{6.7}$$
called a *Vandermonde matrix* (p. 121).
- *Total price:* with price matrix $P$ ($m\times n$) and quantity vector $q$ (a basket of goods), $c=Pq$ is the total cost at each of the $m$ suppliers.
- *Document scoring:* with $A$ the $N\times n$ document-term matrix and word weights $w$, $s=Aw$ scores the documents. A search engine might choose $w$ from the query so scores predict relevance.
- *Audio mixing:* the $k$ columns of $A$ are tracks of length $T$; $b=Aw$ is the mix with track weights $w$.

**Inner product as a special case.** For $n$-vectors $a,b$, treat $a$ as $n\times1$, transpose to a $1\times n$ matrix, and multiply by $b$. The $1$-vector $a^Tb$ is regarded as a scalar, so the inner product is a special case of matrix-vector multiplication (p. 121).

**Linear dependence (p. 121).** The columns of $A$ are linearly dependent if $Ax=0$ for some $x\ne0$. They are linearly independent if $Ax=0$ implies $x=0$.

**Expansion in a basis (p. 121).** If the columns of $A$ are a basis (so $A$ is square with linearly independent columns $a_1,\dots,a_n$), then for any $n$-vector $b$ there is a unique $x$ with $Ax=b$. This $x$ holds the coefficients of $b$ in the basis $a_1,\dots,a_n$.

**Properties (pp. 121–122).** For $A$ and $B$ $m\times n$, $u,v$ $n$-vectors, $\alpha$ a scalar:
$$A(u+v)=Au+Av,\qquad (A+B)u=Au+Bu,\qquad (\alpha A)u=\alpha(Au)=A(\alpha u).$$
Matrix-vector multiplication takes precedence over addition. The two sides of each equation use different operations: on the left of the first, $u+v$ is formed first (vectors in $\mathbf R^n$), then multiplied; on the right, two products are formed, then added ($m$-vectors) (p. 122).

*Intuition note.* These rules say that $x\mapsto Ax$ respects adding and scaling inputs. The text only states the equations here; it does not name this property.

**Input-output interpretation (p. 122).** Read $y=Ax$ as input $x$, output $y$. $A_{ij}$ is the factor by which $y_i$ depends on $x_j$. Conclusions the author draws:
- If $A_{23}$ is positive and large, $y_2$ depends strongly on $x_3$ and increases as $x_3$ increases.
- If $A_{32}$ is much larger than the other entries in row 3, then $y_3$ depends much more on $x_2$ than on the other inputs.
- If $A$ is square and lower triangular, $y_i$ depends only on $x_1,\dots,x_i$.

### 6.5 Complexity (pp. 122–123)

(Our gloss: a flop is a floating-point operation, the unit of arithmetic cost. These pages use the term without defining it.)

**Storage.** An $m\times n$ matrix is usually represented as an array of floating-point numbers needing $8mn$ bytes. Some software systems store only the upper triangle of a symmetric matrix, which reduces memory by around a factor of two. A sparse matrix stores each nonzero's row index, column index and value; with 4-byte indices (allowing $m,n$ up to about 4.3 billion) this takes around $16\,\mathbf{nnz}(A)$ bytes (pp. 122–123).

**Addition, scalar multiplication, transpose (p. 123).**
- Adding two $m\times n$ matrices, or scaling one, takes $mn$ flops.
- If $A$ is sparse, scaling takes $\mathbf{nnz}(A)$ flops.
- If at least one of $A,B$ is sparse, $A+B$ takes at most $\min\{\mathbf{nnz}(A),\mathbf{nnz}(B)\}$ flops.
- Transposition takes zero flops, since entries are only copied (copying time is not counted).

**Matrix-vector product (p. 123).** For dense $A$ ($m\times n$) the cost is $m(2n-1)$ flops, simplified to $2mn$. Reason: there are $m$ outputs, each an inner product of a row with $x$, costing $2n-1$ flops. For sparse $A$: $\mathbf{nnz}(A)$ multiplies and at most $\mathbf{nnz}(A)$ additions, so between $\mathbf{nnz}(A)$ and $2\,\mathbf{nnz}(A)$ flops. For a diagonal $n\times n$ $A$: $n$ multiplies, no additions, total $n=\mathbf{nnz}(A)$ flops.

*Intuition note.* Cost is governed by how many nonzero entries must be touched. A sparse $A$ costs in proportion to its nonzeros, not to $mn$.

### Exercises (pp. 124–127)
The unit lists exercises 6.1–6.22 on notation, block shapes, adjacency matrices, applied models (currency, bank balance, marketing, resources), skew-symmetric matrices, polynomial differentiation, norm inequalities, Vandermonde independence, and flop counts. No solutions are printed in these pages.

## Toy example (ours, not from the text)
Let $A=\begin{bmatrix}1&0\\2&1\\0&3\end{bmatrix}$ ($3\times2$, tall) and $x=(2,-1)$.

- **Row view** ($y_i=b_i^Tx$): $y_1=1\cdot2+0\cdot(-1)=2$; $y_2=2\cdot2+1\cdot(-1)=3$; $y_3=0\cdot2+3\cdot(-1)=-3$. So $y=(2,3,-3)$.
- **Column view** ($y=x_1a_1+x_2a_2$) with $a_1=(1,2,0)$, $a_2=(0,1,3)$: $2(1,2,0)+(-1)(0,1,3)=(2,4,0)+(0,-1,-3)=(2,3,-3)$. Same result.
- **Picking a column:** $Ae_2=(0,1,3)=a_2$.
- **Transpose:** $A^T=\begin{bmatrix}1&2&0\\0&1&3\end{bmatrix}$ ($2\times3$).
- **Norm (6.3):** $\|A\|^2=1+0+4+1+0+9=15$. Column check: $\|a_1\|^2=1+4+0=5$, $\|a_2\|^2=0+1+9=10$, and $5+10=15$.
- **Flops:** dense cost is about $2mn=12$ flops. Here $\mathbf{nnz}(A)=4$, so a sparse method needs between 4 and 8 flops.

## Concepts
- [[matrix]] (new) — rectangular array of numbers with two indices; size $m\times n$ (p. 107)
- [[matrix-vector-multiplication]] (new) — $y=Ax$ with $y_i=\sum_kA_{ik}x_k$; row inner products or column combination (p. 118)
- [[linear combination]] — $Ax=x_1a_1+\dots+x_na_n$, a combination of the columns of $A$ with coefficients $x$ (p. 119)
- [[linear independence]] — columns of $A$ independent if $Ax=0$ implies $x=0$ (p. 121)
- [[basis]] — square $A$ with independent columns; each $b$ has a unique $x$ with $Ax=b$ (p. 121)
- [[dot (inner) product]] — $a^Tb$ is a special case of matrix-vector multiplication (p. 121)
- [[block-matrix]] (new) — matrix whose entries are matrices; blocks must fit in height and width (p. 109)
- [[matrix-transpose]] (new) — $(A^T)_{ij}=A_{ji}$; $(A^T)^T=A$, $(A+B)^T=A^T+B^T$ (p. 115)
- [[symmetric-matrix]] (new) — square $A$ with $A=A^T$ (p. 116)
- [[sparse-matrix]] (new) — few nonzeros; $\mathbf{nnz}(A)$, density $\mathbf{nnz}(A)/(mn)$, no precise cutoff (p. 114)
- [[diagonal-triangular-matrix]] (new) — zero off the diagonal / zero above or below it (p. 114)
- [[identity matrix]] — $I_{ij}=1$ if $i=j$, else 0; $Ix=x$; columns are unit vectors (p. 113)
- [[norm]] — here the matrix (Frobenius) norm (6.3): root of the sum of squared entries (p. 117)
- [[adjacency matrix]] — $A_{ij}=1$ if $(i,j)\in\mathcal R$, else 0; the reverse convention also exists (p. 112)
- [[difference-and-running-sum-matrices]] (new) — $D$ takes consecutive differences; $S$ takes running sums (pp. 119–120)
- [[vandermonde-matrix]] (new) — $A$ in (6.7); $Ac$ evaluates a polynomial at many points (p. 121)
- [[flop-count-matrix-ops]] (new) — dense $Ax$ costs about $2mn$ flops; sparse costs between $\mathbf{nnz}(A)$ and $2\,\mathbf{nnz}(A)$ (p. 123)

## Canonical instances
- [[image-as-matrix]] — pixel grid as an $M\times N$ matrix (p. 110)
- [[asset-return-matrix]] — $T\times n$ returns, table 6.1; $Rw$ gives portfolio returns (pp. 110–111, 120)
- [[document-term-matrix]] — word counts; $Aw$ scores documents (pp. 116, 121)
- [[directed-graph-adjacency]] — relation (6.2) and figure 6.1 (p. 112)
- [[contingency-table]] — counts by two attributes, e.g. year of study × state (p. 111)
- [[polynomial-evaluation-vandermonde]] — $y=Ac$ with matrix (6.7) (pp. 120–121)
- [[audio-mixing]] — $b=Aw$ mixes $k$ tracks (p. 121)

## Bridges (candidates)
- [structural-analogy] Document scoring $s=Aw$ ↔ regression/text mining: a linear score on a count vector, computed row by row as inner products.
- [same-math] Adjacency matrix $A_{ij}$ ↔ network analysis: the graph as a table of 0/1 ties, where $A=A^T$ means an undirected network.
- [structural-analogy] Difference matrix $D$ and running sum $S$ ↔ time-series analysis: differencing and cumulating series (the text does not say they are inverses).
- [same-math] Portfolio return $Rw$ ↔ finance: weighted sum of asset return series.
- [structural-analogy] Sparse storage ($16\,\mathbf{nnz}$ bytes) ↔ large social-network data: cost scales with ties, not with all possible pairs.

## Questions this raises
- If $y=Ax$ is "mix the columns", which questions about $A$ (which $y$ can be reached, which $x$ give $y=0$) follow from independence of its columns?
- How does matrix-matrix multiplication extend the column and row readings of $Ax$ (the text promises a later use of $I$ in §10.1)?
- Which other norms of a matrix exist (p. 118 says they are beyond this book), and when would they replace the Frobenius norm?
- How does sparsity change the choice of algorithm for a very large adjacency matrix?

## Exercises worth doing
- Ex. 6.4 (p. 124) — row and column sums of an adjacency matrix via $A\mathbf 1$ and $A^T\mathbf 1$ — difficulty: easy
- Ex. 6.8 (p. 125) — cash-flow-to-balance matrix; building a matrix from a recursion — difficulty: medium
- Ex. 6.12 (p. 126) — skew-symmetric matrices and orthogonality of $Ax$ and $x$ — difficulty: medium
- Ex. 6.14 (p. 126) — $\|Ax\|\le\|A\|\|x\|$ via row inner products and Cauchy–Schwarz — difficulty: medium
- Ex. 6.18 (p. 127) — independent columns of a Vandermonde matrix — difficulty: hard
- Ex. 6.22 (p. 127) — flop counts of $(A+B)(x+y)$ computed two ways — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 10 (pdf 117–137 carry printed 107–127). The last pdf page (138) is blank, so the chapter's exercises end on printed p. 127.
- The text layer garbles matrices. All matrices, (6.5)–(6.7) and exercise matrices were checked against the page images.
- Likely misprint, p. 121: the document-scoring bullet reads "$w$ in an $n$-vector"; it should read "is".
- The unit refers back to the norm properties on p. 46 and forward to §7.3 and §10.1; the exercise hints use Cauchy–Schwarz, and flop counts are used without definition. None of these is covered in these pages.
- The portfolio product $Rw=(0.00213,-0.00201,0.00241)$ was recomputed from table 6.1 and agrees to the printed precision.
- Exercise solutions are not printed here.
