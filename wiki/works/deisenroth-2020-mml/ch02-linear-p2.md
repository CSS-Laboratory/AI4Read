---
id: deisenroth-2020-mml/ch02-linear-p2
work: deisenroth-2020-mml
unit: "2 Linear Algebra (part 2/2): §2.6 Basis and Rank, §2.7 Linear Mappings, §2.8 Affine Spaces, §2.9 Further Reading, Exercises 2.1–2.20"
pages: 44–69
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Linear Algebra, part 2: Basis, Rank, Linear Mappings, Affine Spaces

## L0 — One line
A basis gives every vector unique coordinates, so a linear map between finite-dimensional spaces becomes a matrix, and changing bases changes that matrix by $\tilde A=T^{-1}AS$.

## L1 — The gist (≤ 120 words)
This part asks how vector spaces can be described with a minimal set of vectors, and how maps between them can be written as matrices. A basis is a minimal spanning set (equivalently, a maximal independent set); its size is the dimension. A linear map gets a transformation matrix once ordered bases are fixed, and a basis change replaces $A$ by $T^{-1}AS$. The kernel and image of a map are linked by the rank–nullity theorem. Finally, shifting subspaces away from the origin gives affine subspaces and affine maps. The text says these ideas are used later: basis change for diagonal forms (Chapter 4) and data compression (Chapter 10), and projections for regression and PCA (Chapters 3, 9, 10).

**Prerequisites:** linear combinations, linear independence, Gaussian elimination and row-echelon form, pivot columns, matrix–vector multiplication, regular (invertible) matrices.

## L2 — Key ideas
- A basis of $V$ can be defined four equivalent ways: basis, minimal generating set, maximal independent set, or a set giving unique linear combinations. All bases of $V$ have the same size, the dimension (pp. 45–46).
- To find a basis of a span, put the vectors in the columns of a matrix, row-reduce, and keep the vectors in the pivot columns (p. 46).
- Rank is the number of independent columns, which equals the number of independent rows. It decides whether a square matrix is invertible (iff $\mathrm{rk}(A)=n$), whether $Ax=b$ is solvable (iff $\mathrm{rk}(A)=\mathrm{rk}(A|b)$), and gives the dimension $n-\mathrm{rk}(A)$ of the solution space of $Ax=0$ (p. 47).
- Finite-dimensional spaces are isomorphic (linked by a linear bijection) iff their dimensions are equal. So any $n$-dimensional space is isomorphic to $\mathbb R^n$ (pp. 49–50).
- Given ordered bases $B$, $C$ (bases whose vectors are listed in a fixed order), a linear map has a transformation matrix whose $j$-th column holds the $C$-coordinates of $\Phi(b_j)$. It satisfies $\hat y=A_\Phi\hat x$ (pp. 51–52).
- Basis change: $\tilde A_\Phi=T^{-1}A_\Phi S$. A good basis can make the matrix diagonal (pp. 53–54).
- The kernel (what is sent to 0) and the image (what is reached) obey $\dim\ker\Phi+\dim\mathrm{Im}\,\Phi=\dim V$ (p. 60).
- Affine subspaces are $x_0+U$. Affine maps are a linear map plus a translation. Solution sets of $Ax=b$ are either empty or affine subspaces (pp. 61–63).

## L3 — Walkthrough

### End of the preceding example (continued from the earlier part)
The page starts mid-example. The fragment says some vectors are linearly independent. It then gives the coefficient matrix (2.75) $$A=\begin{bmatrix}1&-4&2&17\\-2&-2&3&-10\\1&0&-1&11\\-1&4&-3&1\end{bmatrix}$$ and its reduced row-echelon form (2.76) (p. 44):
$$\begin{bmatrix}1&0&0&-7\\0&1&0&-15\\0&0&1&-18\\0&0&0&0\end{bmatrix}.$$
The last column is not a pivot column, and $x_4=-7x_1-15x_2-18x_3$. So $x_1,\dots,x_4$ are linearly dependent (p. 44).

### 2.6 Basis and Rank
**2.6.1 Generating set and basis.**
- **Definition 2.13.** A set $\mathcal A=\{x_1,\dots,x_k\}\subseteq V$ is a *generating set* of $V$ if every $v\in V$ is a linear combination of its vectors. The *span* of $\mathcal A$ is the set of all linear combinations of vectors in $\mathcal A$. We write $V=\mathrm{span}[\mathcal A]$ if $\mathcal A$ spans $V$ (p. 44).
- **Definition 2.14.** A generating set is *minimal* if no smaller subset $\tilde{\mathcal A}\subsetneq\mathcal A$ spans $V$. Every linearly independent generating set of $V$ is minimal and is called a *basis* (p. 44).
- For $\mathcal B\subseteq V$, $\mathcal B\neq\emptyset$, these statements are equivalent (p. 45):
  1. $\mathcal B$ is a basis of $V$.
  2. $\mathcal B$ is a minimal generating set.
  3. $\mathcal B$ is a maximal linearly independent set, i.e. adding any vector makes it dependent.
  4. Every $x\in V$ is a linear combination of $\mathcal B$, and uniquely: from $x=\sum_{i=1}^k\lambda_i b_i=\sum_{i=1}^k\psi_i b_i$ it follows that $\lambda_i=\psi_i$ (2.77).
- **Example 2.16** (p. 45):
  - The canonical basis of $\mathbb R^3$ is $e_1,e_2,e_3$ (2.78).
  - Other bases of $\mathbb R^3$ are $\mathcal B_1=\{[1,0,0]^\top,[1,1,0]^\top,[1,1,1]^\top\}$ and $\mathcal B_2=\{[0.5,0.8,0.4]^\top,[1.8,0.3,0.3]^\top,[-2.2,-1.3,3.5]^\top\}$ (2.79).
  - The set $\mathcal A=\{[1,2,3,4]^\top,[2,-1,0,2]^\top,[1,1,0,-4]^\top\}$ (2.80) is linearly independent but not a generating set of $\mathbb R^4$. For instance, $[1,0,0,0]^\top$ is not a combination of its elements.
- **Remark** (p. 45): every vector space has a basis. There is no unique basis, but all bases have the same number of elements.
- **Dimension.** We consider only finite-dimensional spaces. $\dim(V)$ is the number of basis vectors. For a subspace $U\subseteq V$: $\dim U\le\dim V$, with equality iff $U=V$ (pp. 45–46). The dimension is not necessarily the number of entries of a vector: $\mathrm{span}[[0,1]^\top]$ is one-dimensional, although its basis vector has two entries (p. 46).
- **Finding a basis of $U=\mathrm{span}[x_1,\dots,x_m]\subseteq\mathbb R^n$** (p. 46):
  1. Write the spanning vectors as columns of $A$.
  2. Compute the row-echelon form.
  3. The spanning vectors in the pivot columns form a basis of $U$.
- **Example 2.17** (pp. 46–47). In $\mathbb R^5$:
$$x_1=\begin{bmatrix}1\\2\\-1\\-1\\-1\end{bmatrix},\;x_2=\begin{bmatrix}2\\-1\\1\\2\\-2\end{bmatrix},\;x_3=\begin{bmatrix}3\\-4\\3\\5\\-3\end{bmatrix},\;x_4=\begin{bmatrix}-1\\8\\-5\\-6\\1\end{bmatrix}.$$
  Solving $\sum\lambda_i x_i=0$ (2.82) means row-reducing $[x_1,x_2,x_3,x_4]$ (2.83). The row-echelon form has rows $[1,2,3,-1]$, $[0,1,2,-2]$, $[0,0,0,1]$, and two zero rows. The pivots are in columns 1, 2, 4, so $\{x_1,x_2,x_4\}$ is a basis of $U$ (p. 47).

*Intuition note.* A basis is a spanning set with nothing wasted. Drop any vector and you lose some of the space. Add any vector and you create a redundancy. In the row-echelon form, the pivot columns pick out a basis from the spanning vectors.

**2.6.2 Rank.** The number of linearly independent columns of $A\in\mathbb R^{m\times n}$ equals the number of independent rows. It is the *rank*, $\mathrm{rk}(A)$ (p. 47). Properties listed by the author (p. 47):
- $\mathrm{rk}(A)=\mathrm{rk}(A^\top)$.
- The columns span a subspace of $\mathbb R^m$ of dimension $\mathrm{rk}(A)$ (later called image or range). Pivot columns give a basis.
- The rows span a subspace of $\mathbb R^n$ of dimension $\mathrm{rk}(A)$. Eliminate on $A^\top$ to get a basis.
- For $A\in\mathbb R^{n\times n}$: $A$ is regular (invertible) iff $\mathrm{rk}(A)=n$.
- $Ax=b$ is solvable iff $\mathrm{rk}(A)=\mathrm{rk}(A|b)$, where $A|b$ is the augmented system.
- The solutions of $Ax=0$ form a subspace of dimension $n-\mathrm{rk}(A)$ (later the kernel or null space).
- $A\in\mathbb R^{m\times n}$ has *full rank* if $\mathrm{rk}(A)=\min(m,n)$. Otherwise it is *rank deficient*.

**Example 2.18** (pp. 47–48):
- $A=\begin{bmatrix}1&0&1\\0&1&1\\0&0&0\end{bmatrix}$ has two independent rows/columns, so $\mathrm{rk}(A)=2$.
- $A=\begin{bmatrix}1&2&1\\-2&-3&1\\3&5&0\end{bmatrix}$ reduces to $\begin{bmatrix}1&2&1\\0&1&3\\0&0&0\end{bmatrix}$ (2.84), so $\mathrm{rk}(A)=2$.

### 2.7 Linear Mappings
A map $\Phi:V\to W$ between real vector spaces preserves structure if $\Phi(x+y)=\Phi(x)+\Phi(y)$ (2.85) and $\Phi(\lambda x)=\lambda\Phi(x)$ (2.86) (p. 48).
- **Definition 2.15.** $\Phi$ is a *linear mapping* (vector space homomorphism, linear transformation) if
$$\forall x,y\in V\;\forall\lambda,\psi\in\mathbb R:\;\Phi(\lambda x+\psi y)=\lambda\Phi(x)+\psi\Phi(y).\tag{2.87}$$
  Linear mappings can be represented as matrices. One must keep in mind whether a matrix represents a mapping or a collection of vectors (p. 48).
- **Definition 2.16.** $\Phi:V\to W$ (arbitrary sets) is *injective* if $\Phi(x)=\Phi(y)\Rightarrow x=y$. It is *surjective* if $\Phi(V)=W$, and *bijective* if both (p. 48).
- A surjective $\Phi$ reaches every element of $W$. A bijective $\Phi$ can be undone by a map $\Psi=\Phi^{-1}$ with $\Psi\circ\Phi(x)=x$ (p. 49).
- Special linear maps (p. 49):
  - isomorphism: linear and bijective;
  - endomorphism: $V\to V$ linear;
  - automorphism: $V\to V$ linear and bijective;
  - $\mathrm{id}_V:x\mapsto x$ is the identity automorphism.
- **Example 2.19** (p. 49). $\Phi:\mathbb R^2\to\mathbb C$, $\Phi(x)=x_1+ix_2$ is a homomorphism. Additivity and scaling are checked in (2.88). The author shows linearity only, not bijectivity. The text says this justifies representing complex numbers as tuples in $\mathbb R^2$ (p. 49).
- **Theorem 2.17** (Axler 2015, Thm 3.59). Finite-dimensional vector spaces $V$, $W$ are isomorphic iff $\dim V=\dim W$ (p. 49). Hence $\mathbb R^{m\times n}$ and $\mathbb R^{mn}$ can be treated as the same space, since both have dimension $mn$ (p. 49).
- **Remark** (pp. 49–50):
  - $\Psi\circ\Phi$ of linear maps is linear.
  - The inverse of an isomorphism is an isomorphism.
  - $\Phi+\Psi$ and $\lambda\Phi$ are linear if $\Phi,\Psi:V\to W$ are linear.

*Intuition note.* Linear maps are the functions that respect adding and scaling. Spaces of equal dimension can be converted into each other without loss, so only the dimension matters.

**2.7.1 Matrix representation of linear mappings.**
- An *ordered basis* is an $n$-tuple $B=(b_1,\dots,b_n)$ (2.89). Notation: $B=(\cdot)$ is ordered, $\mathcal B=\{\cdot\}$ is unordered, and $\boldsymbol B=[b_1,\dots,b_n]$ is a matrix with these columns (p. 50).
- **Definition 2.18 (coordinates).** For $x\in V$ there is a unique $x=\alpha_1b_1+\dots+\alpha_nb_n$ (2.90). The $\alpha_i$ are the coordinates of $x$ w.r.t. $B$. The vector $\boldsymbol\alpha=[\alpha_1,\dots,\alpha_n]^\top\in\mathbb R^n$ (2.91) is the coordinate vector (p. 50).
- A basis defines a coordinate system, and the same vector has different coordinates in different bases. In Figure 2.8 the vector has coordinates $[2,2]^\top$ in $(e_1,e_2)$ and $[1.09,0.72]^\top$ in $(b_1,b_2)$ (p. 51).
- **Example 2.20** (p. 51). $x=[2,3]^\top=2e_1+3e_2$. With $b_1=[1,-1]^\top$, $b_2=[1,1]^\top$ the coordinates are $\tfrac12[-1,5]^\top$, i.e. $x=-\tfrac12b_1+\tfrac52b_2$.
- **Remark** (p. 51). The map $\Phi:\mathbb R^n\to V$ with $\Phi(e_i)=b_i$ is linear, and an isomorphism by Theorem 2.17.
- **Definition 2.19 (transformation matrix).** Let $B=(b_1,\dots,b_n)$ be an ordered basis of $V$, $C=(c_1,\dots,c_m)$ one of $W$, and $\Phi:V\to W$ linear. For $j=1,\dots,n$,
$$\Phi(b_j)=\alpha_{1j}c_1+\dots+\alpha_{mj}c_m=\sum_{i=1}^m\alpha_{ij}c_i\tag{2.92}$$
  is the unique $C$-representation of $\Phi(b_j)$. The $m\times n$ matrix with $A_\Phi(i,j)=\alpha_{ij}$ (2.93) is the transformation matrix of $\Phi$ w.r.t. $B$, $C$. Its $j$-th column is the $C$-coordinate vector of $\Phi(b_j)$ (p. 51).
- If $\hat x$ are the $B$-coordinates of $x$ and $\hat y$ the $C$-coordinates of $y=\Phi(x)$, then
$$\hat y=A_\Phi\hat x.\tag{2.94}$$
  The matrix maps coordinates in $V$ to coordinates in $W$ (p. 52).
- **Example 2.21** (p. 52). With $\Phi(b_1)=c_1-c_2+3c_3-c_4$, $\Phi(b_2)=2c_1+c_2+7c_3+2c_4$, $\Phi(b_3)=3c_2+c_3+4c_4$ (2.95), the transformation matrix is
$$A_\Phi=\begin{bmatrix}1&2&0\\-1&1&3\\3&7&1\\-1&2&4\end{bmatrix}\tag{2.96}$$
  Its columns are the coordinate vectors of $\Phi(b_j)$ w.r.t. $C$.
- **Example 2.22** (pp. 52–53). Three maps of 400 points arranged in a square in $\mathbb R^2$ (2.97):
  - $A_1=\begin{bmatrix}\cos\frac\pi4&-\sin\frac\pi4\\\sin\frac\pi4&\cos\frac\pi4\end{bmatrix}$ rotates the square (by $45^\circ$ per Figure 2.10(b)).
  - $A_2=\mathrm{diag}(2,1)$ stretches each $x_1$-coordinate by 2.
  - $A_3=\frac12\begin{bmatrix}3&-1\\1&-1\end{bmatrix}$ combines a reflection, a rotation and a stretch.

*Intuition note.* The $j$-th column of a transformation matrix records where the $j$-th input basis vector goes, written in output-basis coordinates. Once the bases are fixed, applying the map is just matrix–vector multiplication on coordinates.

**2.7.2 Basis change.** Take ordered bases $B,\tilde B$ of $V$ (2.98) and $C,\tilde C$ of $W$ (2.99). Let $A_\Phi\in\mathbb R^{m\times n}$ be the matrix w.r.t. $B,C$ and $\tilde A_\Phi\in\mathbb R^{m\times n}$ w.r.t. $\tilde B,\tilde C$ (p. 53). The change of basis amounts to different coordinate representations of the identity map. A new basis can give a particularly simple matrix (p. 53).

**Example 2.23** (pp. 53–54). $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$ (2.100) w.r.t. the canonical basis. With the new basis $B=([1,1]^\top,[1,-1]^\top)$ (2.101) the matrix becomes the diagonal $\tilde A=\begin{bmatrix}3&0\\0&1\end{bmatrix}$ (2.102), "easier to work with".

**Theorem 2.20 (Basis change).** Let $\Phi:V\to W$ be linear, $B,\tilde B$ bases of $V$ (2.103), $C,\tilde C$ bases of $W$ (2.104), and $A_\Phi$ the matrix w.r.t. $B,C$. Then the matrix w.r.t. $\tilde B,\tilde C$ is
$$\tilde A_\Phi=T^{-1}A_\Phi S.\tag{2.105}$$
Here $S\in\mathbb R^{n\times n}$ is the matrix of $\mathrm{id}_V$ mapping $\tilde B$-coordinates to $B$-coordinates. $T\in\mathbb R^{m\times m}$ is the matrix of $\mathrm{id}_W$ mapping $\tilde C$-coordinates to $C$-coordinates (p. 54). Shapes: $A_\Phi,\tilde A_\Phi$ are $m\times n$; $S$ is $n\times n$; $T$ is $m\times m$.

*Proof* (pp. 54–55):
1. Write the new basis vectors in terms of the old ones:
$$\tilde b_j=\sum_{i=1}^n s_{ij}b_i,\quad j=1,\dots,n\tag{2.106}$$
$$\tilde c_k=\sum_{l=1}^m t_{lk}c_l,\quad k=1,\dots,m\tag{2.107}$$
2. Then $S=((s_{ij}))$ has as $j$-th column the $B$-coordinates of $\tilde b_j$. $T=((t_{lk}))$ has as $k$-th column the $C$-coordinates of $\tilde c_k$. Both are regular (p. 55).
3. Compute $\Phi(\tilde b_j)$ in two ways. First, using $\tilde A_\Phi$ (entries $\tilde a_{kj}$), then (2.107), then swapping the order of summation:
$$\Phi(\tilde b_j)=\sum_{k=1}^m\tilde a_{kj}\tilde c_k\overset{(2.107)}{=}\sum_{k=1}^m\tilde a_{kj}\sum_{l=1}^mt_{lk}c_l=\sum_{l=1}^m\Big(\sum_{k=1}^mt_{lk}\tilde a_{kj}\Big)c_l\tag{2.108}$$
4. Second, using (2.106) and linearity of $\Phi$ (entries $a_{li}$ of $A_\Phi$):
$$\Phi(\tilde b_j)\overset{(2.106)}{=}\Phi\Big(\sum_{i=1}^ns_{ij}b_i\Big)=\sum_{i=1}^ns_{ij}\Phi(b_i)=\sum_{i=1}^ns_{ij}\sum_{l=1}^ma_{li}c_l\tag{2.109a}$$
$$=\sum_{l=1}^m\Big(\sum_{i=1}^na_{li}s_{ij}\Big)c_l,\quad j=1,\dots,n\tag{2.109b}$$
5. Comparing coefficients of $c_l$ in (2.108) and (2.109b), for all $j,l$:
$$\sum_{k=1}^mt_{lk}\tilde a_{kj}=\sum_{i=1}^na_{li}s_{ij}\tag{2.110}$$
   so $T\tilde A_\Phi=A_\Phi S\in\mathbb R^{m\times n}$ (2.111) and $\tilde A_\Phi=T^{-1}A_\Phi S$ (2.112). ∎

Figure 2.11 shows this as a composition (p. 56):
$$\Phi_{\tilde C\tilde B}=\Xi_{\tilde CC}\circ\Phi_{CB}\circ\Psi_{B\tilde B}=\Xi_{C\tilde C}^{-1}\circ\Phi_{CB}\circ\Psi_{B\tilde B}\tag{2.114}$$
Concretely, $\Psi_{B\tilde B}=\mathrm{id}_V$ and $\Xi_{C\tilde C}=\mathrm{id}_W$. These are identity maps expressed in different bases (p. 56). Matrices: $S\leftrightarrow\Psi_{B\tilde B}$, $T\leftrightarrow\Xi_{C\tilde C}$, and for a composition $A_{\Psi\circ\Phi}=A_\Psi A_\Phi$ (p. 56). In terms of bases: $\tilde B\to\tilde C=\tilde B\to B\to C\to\tilde C$ (2.115), so $\tilde A_\Phi=T^{-1}A_\Phi S$ (2.116). It is executed right to left: $x\mapsto Sx\mapsto A_\Phi(Sx)\mapsto T^{-1}(A_\Phi(Sx))=\tilde A_\Phi x$ (p. 57).

- **Definition 2.21 (equivalence).** $A,\tilde A\in\mathbb R^{m\times n}$ are *equivalent* if there are regular $S\in\mathbb R^{n\times n}$, $T\in\mathbb R^{m\times m}$ with $\tilde A=T^{-1}AS$ (p. 56).
- **Definition 2.22 (similarity).** $A,\tilde A\in\mathbb R^{n\times n}$ are *similar* if there is a regular $S$ with $\tilde A=S^{-1}AS$ (p. 56).
- **Remark** (p. 56). Similar matrices are always equivalent. Equivalent matrices are not necessarily similar.

*Intuition note.* The map itself does not change when you change bases. Only the numbers describing it change. $S$ translates new-input coordinates into old ones, $A_\Phi$ acts, and $T^{-1}$ translates old-output coordinates into new ones.

**Example 2.24** (pp. 57–58). $\Phi:\mathbb R^3\to\mathbb R^4$ has matrix $A_\Phi$ as in (2.117) (same entries as (2.96)) w.r.t. the standard bases (2.118). New bases (2.119): $\tilde B=([1,1,0]^\top,[0,1,1]^\top,[1,0,1]^\top)$ and $\tilde C=([1,1,0,0]^\top,[1,0,1,0]^\top,[0,1,1,0]^\top,[1,0,0,1]^\top)$. The columns of $S$ and $T$ are these vectors, because $B$ and $C$ are standard bases (2.120). Then
$$\tilde A_\Phi=T^{-1}A_\Phi S=\frac12\begin{bmatrix}1&1&-1&-1\\1&-1&1&-1\\-1&1&1&1\\0&0&0&2\end{bmatrix}\begin{bmatrix}3&2&1\\0&4&2\\10&8&4\\1&6&3\end{bmatrix}=\begin{bmatrix}-4&-4&-2\\6&0&0\\4&8&4\\1&6&3\end{bmatrix}\tag{2.121}$$
The author says later chapters use basis change to get diagonal forms (Chapter 4) and to compress data (Chapter 10) (p. 58).

**2.7.3 Image and kernel.**
- **Definition 2.23.** For $\Phi:V\to W$:
$$\ker(\Phi):=\Phi^{-1}(0_W)=\{v\in V:\Phi(v)=0_W\}\tag{2.122}$$
$$\mathrm{Im}(\Phi):=\Phi(V)=\{w\in W\mid\exists v\in V:\Phi(v)=w\}\tag{2.123}$$
  $V$ is the domain and $W$ the codomain (p. 58).
- **Remark** (pp. 58–59):
  - $\Phi(0_V)=0_W$, so the kernel is never empty.
  - $\mathrm{Im}(\Phi)\subseteq W$ and $\ker(\Phi)\subseteq V$ are subspaces.
  - $\Phi$ is injective iff $\ker(\Phi)=\{0\}$.
- **Remark (null space and column space)** for $\Phi:\mathbb R^n\to\mathbb R^m$, $x\mapsto Ax$, $A=[a_1,\dots,a_n]$ (p. 59):
$$\mathrm{Im}(\Phi)=\Big\{\sum_{i=1}^nx_ia_i:x_i\in\mathbb R\Big\}=\mathrm{span}[a_1,\dots,a_n]\subseteq\mathbb R^m\tag{2.124}$$
  This is the column space, and $\mathrm{rk}(A)=\dim\mathrm{Im}(\Phi)$. The kernel is the general solution of $Ax=0$ and is a subspace of $\mathbb R^n$. It captures relationships among the columns.
- **Example 2.25** (pp. 59–60). $\Phi:\mathbb R^4\to\mathbb R^2$, $x\mapsto\begin{bmatrix}1&2&-1&0\\1&0&0&1\end{bmatrix}x=[x_1+2x_2-x_3,\;x_1+x_4]^\top$ (2.125).
  - $\mathrm{Im}(\Phi)=\mathrm{span}[[1,1]^\top,[2,0]^\top,[-1,0]^\top,[0,1]^\top]$ (2.126).
  - Gaussian elimination gives $\begin{bmatrix}1&0&0&1\\0&1&-\frac12&-\frac12\end{bmatrix}$ (2.127). Pivot columns are 1 and 2.
  - Non-pivot columns: $a_3=-\tfrac12a_2$, so $0=a_3+\tfrac12a_2$. Also $a_4=a_1-\tfrac12a_2$, so $0=a_1-\tfrac12a_2-a_4$.
  - $\ker(\Phi)=\mathrm{span}\big[[0,\tfrac12,1,0]^\top,[-1,\tfrac12,0,1]^\top\big]$ (2.128).
- **Theorem 2.24 (Rank–Nullity; "fundamental theorem of linear mappings").** For $\Phi:V\to W$ linear,
$$\dim(\ker\Phi)+\dim(\mathrm{Im}\,\Phi)=\dim V.\tag{2.129}$$
  Direct consequences (p. 60):
  - If $\dim\mathrm{Im}\,\Phi<\dim V$, the kernel is non-trivial, so $\dim\ker\Phi\ge1$.
  - Then $A_\Phi x=0$ has infinitely many solutions.
  - If $\dim V=\dim W$: $\Phi$ injective $\iff$ surjective $\iff$ bijective.

*Intuition note.* The input dimensions either survive into the image or are crushed into the kernel. In Example 2.25, the 4 input dimensions split into 2 (image) plus 2 (kernel).

### 2.8 Affine Spaces
Affine spaces are offset from the origin and so are not vector subspaces. The author remarks that machine-learning texts sometimes call affine objects "linear" (p. 61).

**2.8.1 Affine subspaces.**
- **Definition 2.25.** For $x_0\in V$ and a subspace $U\subseteq V$,
$$L=x_0+U:=\{x_0+u:u\in U\}=\{v\in V\mid\exists u\in U:v=x_0+u\}\tag{2.130}$$
  is an *affine subspace* (linear manifold). $U$ is the *direction (space)* and $x_0$ the *support point*. Chapter 12 calls such a subspace a *hyperplane* (p. 61).
- If $x_0\notin U$, then $0\notin L$, so $L$ is not a vector subspace. Examples: points, lines and planes in $\mathbb R^3$ that need not pass through the origin (p. 61).
- **Remark** (p. 61). For $L=x_0+U$ and $\tilde L=\tilde x_0+\tilde U$: $L\subseteq\tilde L$ iff $U\subseteq\tilde U$ and $x_0-\tilde x_0\in\tilde U$.
- **Parametric equation.** If $L=x_0+U$ is $k$-dimensional and $(b_1,\dots,b_k)$ is an ordered basis of $U$, every $x\in L$ is uniquely
$$x=x_0+\lambda_1b_1+\dots+\lambda_kb_k,\quad\lambda_i\in\mathbb R\tag{2.131}$$
  (p. 61).
- **Example 2.26** (p. 62), in $\mathbb R^n$:
  - A line is a 1-dimensional affine subspace: $y=x_0+\lambda b_1$ (Figure 2.13).
  - A plane is a 2-dimensional one: $y=x_0+\lambda_1b_1+\lambda_2b_2$, with $b_1,b_2$ linearly independent.
  - A hyperplane is an $(n-1)$-dimensional one: $y=x_0+\sum_{i=1}^{n-1}\lambda_ib_i$. In $\mathbb R^2$ a line is a hyperplane. In $\mathbb R^3$ a plane is a hyperplane.
- **Remark (inhomogeneous systems)** (p. 62):
  - For $A\in\mathbb R^{m\times n}$, the solution of $A\lambda=x$ is either empty or an affine subspace of $\mathbb R^n$ of dimension $n-\mathrm{rk}(A)$.
  - Every $k$-dimensional affine subspace of $\mathbb R^n$ is the solution of some $Ax=b$ with $\mathrm{rk}(A)=n-k$.
  - Homogeneous solution sets are a special case with $x_0=0$.
  - The remark also states, without further conditions, that the solution of $\lambda_1b_1+\dots+\lambda_nb_n=x$ with $(\lambda_1,\dots,\lambda_n)\ne0$ is a hyperplane in $\mathbb R^n$.

**2.8.2 Affine mappings.**
- **Definition 2.26.** For a linear $\Phi:V\to W$ and $a\in W$, the map $\phi:x\mapsto a+\Phi(x)$ (2.132–2.133) is an *affine mapping*. $a$ is its *translation vector* (p. 63).
- Properties (p. 63):
  - Every affine $\phi$ is $\tau\circ\Phi$ (a linear map followed by a translation $\tau$ in $W$), with $\Phi$ and $\tau$ uniquely determined.
  - A composition of affine maps is affine.
  - If $\phi$ is bijective, it keeps the geometric structure invariant and preserves dimension and parallelism.

*Intuition note.* An affine map is a linear map followed by a shift. When the map is bijective, it preserves dimension and parallelism.

### 2.9 Further Reading
The author lists textbooks on linear algebra and on numerical methods for solving linear systems (this chapter covered only Gaussian elimination). The authors say Chapter 3 will introduce the inner product, norm, angles, lengths, distances and orthogonal projections. Projections are key to linear regression and PCA (Chapters 9 and 10) (p. 63).

## Toy example (ours, not from the text)
Let $\Phi:\mathbb R^2\to\mathbb R^2$ swap coordinates: $A=\begin{bmatrix}0&1\\1&0\end{bmatrix}$ in the standard basis. Take the new basis $\tilde B=\tilde C=([1,1]^\top,[1,-1]^\top)$.
- $S=T=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$. Its inverse is $S^{-1}=\tfrac12\begin{bmatrix}1&1\\1&-1\end{bmatrix}$. Check: $\tfrac12\begin{bmatrix}1+1&1-1\\1-1&1+1\end{bmatrix}=I$.
- $AS=\begin{bmatrix}0\cdot1+1\cdot1&0\cdot1+1\cdot(-1)\\1\cdot1+0&1\cdot1+0\end{bmatrix}=\begin{bmatrix}1&-1\\1&1\end{bmatrix}$.
- $\tilde A=S^{-1}AS=\tfrac12\begin{bmatrix}1\cdot1+1\cdot1&1\cdot(-1)+1\cdot1\\1\cdot1-1\cdot1&1\cdot(-1)-1\cdot1\end{bmatrix}=\tfrac12\begin{bmatrix}2&0\\0&-2\end{bmatrix}=\begin{bmatrix}1&0\\0&-1\end{bmatrix}$.
- Coordinate check with $x=[3,1]^\top$. Solve $\alpha_1+\alpha_2=3$, $\alpha_1-\alpha_2=1$, giving $\hat x=[2,1]^\top$.
  - Then $\tilde A\hat x=[2,-1]^\top$ stands for $2[1,1]^\top-1[1,-1]^\top=[1,3]^\top$.
  - Directly, $Ax=[1,3]^\top$. The two agree.
- So in this basis the map keeps the first basis vector and flips the second, and the matrix is diagonal.

## Concepts
- [[span]] — set of all linear combinations of a set of vectors; $V=\mathrm{span}[\mathcal A]$ if it spans $V$ (p. 44)
- [[generating-set]] (new) — a set of vectors whose combinations give every vector of $V$ (p. 44)
- [[basis]] — a linearly independent generating set. Equivalently a minimal generating set, a maximal independent set, or a set giving unique combinations (pp. 44–45)
- [[dimension]] — number of basis vectors. Not necessarily the number of entries in a vector (pp. 45–46)
- [[linear-independence]] — used here via pivot columns of the row-echelon form (pp. 44, 47)
- [[rank]] — number of independent columns, equal to the number of independent rows; $\mathrm{rk}(A)=\mathrm{rk}(A^\top)$ (p. 47)
- [[linear-map]] — $\Phi(\lambda x+\psi y)=\lambda\Phi(x)+\psi\Phi(y)$ (p. 48)
- [[isomorphism]] (new) — a linear bijection. Finite-dimensional spaces are isomorphic iff their dimensions are equal (p. 49)
- [[coordinate-vector]] (new) — the unique coefficients of $x$ w.r.t. an ordered basis (p. 50)
- [[matrix-as-transformation]] — here the transformation matrix: columns are $C$-coordinates of $\Phi(b_j)$ (p. 51)
- [[matrix-multiplication-as-composition]] — $A_{\Psi\circ\Phi}=A_\Psi A_\Phi$ (p. 56)
- [[change-of-basis]] — $\tilde A_\Phi=T^{-1}A_\Phi S$ (Theorem 2.20) (p. 54)
- [[matrix-equivalence-and-similarity]] (new) — $\tilde A=T^{-1}AS$ (equivalent) and $\tilde A=S^{-1}AS$ (similar) (p. 56)
- [[null-space]] — kernel $\{v:\Phi(v)=0\}$; solutions of $Ax=0$ (pp. 58–59)
- [[column-space]] — image of $x\mapsto Ax$; span of the columns (p. 59)
- [[rank-nullity]] — $\dim\ker\Phi+\dim\mathrm{Im}\,\Phi=\dim V$ (p. 60)
- [[inverse-matrix]] — appears as regular matrix ($\mathrm{rk}=n$) and as $\Phi^{-1}$ of a bijection (pp. 47, 49)
- [[affine-subspace]] (new) — $x_0+U$ with support point $x_0$ and direction space $U$ (p. 61)
- [[affine-mapping]] (new) — $x\mapsto a+\Phi(x)$ (p. 63)

## Canonical instances
- [[example-dependent-columns-rref]] (new) — a pivot-free last column shows $x_4=-7x_1-15x_2-18x_3$ (p. 44)
- [[example-basis-from-pivot-columns]] (new) — Example 2.17: $\{x_1,x_2,x_4\}$ is a basis of $U\subseteq\mathbb R^5$ (pp. 46–47)
- [[example-complex-numbers-as-R2]] (new) — Example 2.19: $\Phi(x)=x_1+ix_2$ is linear (p. 49)
- [[example-coordinates-in-two-bases]] (new) — Example 2.20: the vector with standard coordinates $[2,3]^\top$ has coordinates $\tfrac12[-1,5]^\top$ in basis $([1,-1]^\top,[1,1]^\top)$ (p. 51)
- [[example-rotation-stretch-reflection]] (new) — Example 2.22: matrices $A_1,A_2,A_3$ transform a square of points (pp. 52–53)
- [[example-diagonalising-basis-change]] (new) — Example 2.23: $\begin{bmatrix}2&1\\1&2\end{bmatrix}\to\mathrm{diag}(3,1)$ (pp. 53–54)
- [[example-basis-change-R3-R4]] (new) — Example 2.24: $\tilde A_\Phi=T^{-1}A_\Phi S$ computed (pp. 57–58)
- [[example-kernel-image-R4-R2]] (new) — Example 2.25: image and 2-dimensional kernel of a map $\mathbb R^4\to\mathbb R^2$ (pp. 59–60)
- [[example-lines-planes-hyperplanes]] (new) — Example 2.26: affine subspaces by parametric equation (pp. 61–62)

## Bridges (candidates)
- [same-math] Basis change $T^{-1}AS$ ↔ linear-algebra: diagonalisation $A=X\Lambda X^{-1}$ — the diagonal case $\tilde A=\mathrm{diag}$ of Example 2.23 is this with a well-chosen $S$ (the author defers this to Chapter 4).
- [same-math] Rank–nullity ↔ the earlier solution-set count: $Ax=0$ has an $(n-\mathrm{rk}A)$-dimensional solution space — the same statement for $\Phi:x\mapsto Ax$.
- [structural-analogy] Affine subspace $x_0+U$ ↔ data analysis: mean-centred data plus a subspace (PCA, Chapter 10; the link is not discussed in these pages) — an offset plus a linear directions space.
- [metaphor] Coordinates in a basis ↔ choice of feature representation in machine learning — the same object, different numbers.

## Questions this raises
- Why is the column rank always equal to the row rank? The text states it without proof.
- Is there a best choice of basis (diagonal $\tilde A$) for an endomorphism? The text says Chapter 4 addresses this.
- How do lengths and angles enter once a basis is chosen? The text points to the inner product in Chapter 3.
- When is a bijective affine map between spaces more than preserving dimension and parallelism?

## Exercises worth doing
- Ex. 2.9 (p. 66) — decide which sets are subspaces of $\mathbb R^3$ (closure, 0 in the set) — difficulty: easy
- Ex. 2.10 (p. 66) — test linear independence of vector sets via row-echelon form — difficulty: easy
- Ex. 2.14 (p. 67) — dimensions, bases and a basis of $U_1\cap U_2$ for column spaces — difficulty: medium
- Ex. 2.17 (p. 68) — transformation matrix, rank, kernel and image of a map $\mathbb R^3\to\mathbb R^4$, with rank–nullity check — difficulty: medium
- Ex. 2.19 (p. 68) — kernel/image of an endomorphism, then basis change to a new basis — difficulty: medium
- Ex. 2.20 (p. 69) — chain of basis changes between $B,B'$ and $C,C'$ checking $A'=\ldots$ against direct coordinates — difficulty: hard

## Reading notes
- **Part boundaries.** The unit starts mid-example on printed p. 44, just before the §2.6 heading; the example's number is not visible on these pages. The first sentence is cut off. The vectors named in that fragment are not visible here. The unit ends with Exercise 2.20 on p. 69. The split is at a section boundary.
- **Page offset:** printed = pdf − 6.
- **Edition facts as printed:** footer "Draft (2024-01-15) of 'Mathematics for Machine Learning'. Feedback: https://mml-book.com." and "©2024 M. P. Deisenroth, A. A. Faisal, C. S. Ong. Published by Cambridge University Press (2020)."
- **Exercises 2.1–2.8** (pp. 64–66) cover groups and modular arithmetic, matrix products, linear systems, the equation $Ax=12x$ (Ex. 2.7), and inverses. They are listed in the source here but not digested.
- **Text-layer garbling.** The extracted text was garbled in several equation and matrix displays. I checked them against the page images, including (2.76), (2.121), and the matrices in Example 2.17.
- **Terse statement.** The remark on p. 62 says the solution of $\lambda_1b_1+\dots+\lambda_nb_n=x$ with $(\lambda_1,\dots,\lambda_n)\ne0$ is a hyperplane. It is stated without further conditions, and I reproduced it as printed.
- **Typography.** Def. 2.22 has no closing period. The text of Def. 2.23 reads "We also call V and W also …".
- **Figure values.** The text on p. 51 gives the coordinates of the vector of Figure 2.8 with respect to $(b_1,b_2)$ as $[1.09,0.72]^\top$.
