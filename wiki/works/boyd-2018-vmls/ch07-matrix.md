---
id: boyd-2018-vmls/ch07-matrix
work: boyd-2018-vmls
unit: Chapter 7 — Matrix examples
pages: 129-146
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
# Matrix examples (Boyd & Vandenberghe, ch. 7)

## L0 — One line
Many useful operations (rotating, picking entries, differencing along graph edges, convolving signals) are just matrix–vector products with a special, easily described matrix.

## L1 — The gist (≤ 120 words)
Which special matrices keep appearing in applications, and what does multiplying by each one mean? The chapter shows four families. Geometric matrices (scaling, rotation, reflection, projection) act on points. Selector and permutation matrices copy or reorder entries. The incidence matrix of a directed graph turns edge flows into net node flows, and its transpose turns node potentials into edge differences; this gives the Dirichlet energy, a roughness measure. Convolution, which is polynomial multiplication, is a product with a Toeplitz matrix (constant along each diagonal) and models smoothing, filtering and channels. For convolution, the special structure even allows a much faster algorithm than the naive one.

**Prerequisites:** matrix–vector product; unit vectors $e_i$; transpose; norm $\|x\|^2=\sum x_i^2$; sparse matrix; polynomial multiplication; flop (arithmetic operation) counting.

## L2 — Key ideas (5–10 bullets)
- To find the matrix of a geometric transformation, apply it to each unit vector $e_i$; the results are the columns (p. 130).
- A selector matrix has a transposed unit vector in each row, so $Ax$ copies chosen entries of $x$. Identity, reverser, slicing, down-sampling and cropping are selectors; a permutation matrix is a selector whose transpose is also a selector (pp. 131–132).
- For a directed graph with incidence matrix $A$ and edge-flow vector $x$, $Ax$ is the vector of net flows into the nodes. $Ax=0$ is flow conservation (such an $x$ is called a circulation), and $Ax+s=0$ includes source flows (pp. 133–134).
- $A^Tv$ gives potential differences across edges; $\mathcal D(v)=\|A^Tv\|^2$ is the Dirichlet energy, a roughness measure of node values (p. 135).
- Convolution $c=a*b$ is the coefficient list of the product of polynomials. It is symmetric and associative, and equals $T(b)a=T(a)b$ with a Toeplitz matrix (entries constant along each diagonal) (pp. 136–138).
- Moving averages, first differences, audio filters, channels and input–output systems are all convolutions (pp. 138, 140).
- Naive convolution costs about $2mn$ flops; an algorithm based on the fast Fourier transform (FFT) needs about $5(m+n)\log_2(m+n)$ flops and no extra memory (p. 140).
- 2-D convolution $A\star B$ models image blurring and image differencing, with the same symmetry and associativity (pp. 140–142).

## L3 — Walkthrough

### 7.1 Geometric transformations (pp. 129–131)
Position vectors in 2-D or 3-D are mapped to points by $y=Ax$ with $A$ of size $2\times2$ or $3\times3$. The author works mostly in 2-D (p. 129).

- **Scaling:** $y=ax$, i.e. $A=aI$. It stretches by $|a|$, shrinks if $|a|<1$, and flips direction if $a<0$ (p. 129).
- **Dilation:** $y=Dx$, $D=\mathbf{diag}(d_1,d_2)$. It stretches by different factors along the two axes (shrinks if $|d_i|<1$, flips if $d_i<0$) (p. 129).
- **Rotation** by $\theta$ radians counterclockwise (p. 129):
$$y=\begin{bmatrix}\cos\theta&-\sin\theta\\ \sin\theta&\cos\theta\end{bmatrix}x.\tag{7.1}$$
- **Reflection** through the line through the origin inclined $\theta$ to the horizontal (p. 129):
$$y=\begin{bmatrix}\cos 2\theta&\sin 2\theta\\ \sin 2\theta&-\cos 2\theta\end{bmatrix}x.$$
- **Projection onto a line** through the origin inclined $\theta$. The projection of $x$ onto a set is the point of the set closest to $x$ (p. 130):
$$y=\begin{bmatrix}\tfrac12(1+\cos 2\theta)&\tfrac12\sin 2\theta\\ \tfrac12\sin 2\theta&\tfrac12(1-\cos 2\theta)\end{bmatrix}x.$$
- Figure 7.1 illustrates a dilation $\mathbf{diag}(2,2/3)$, a rotation by $\pi/6$, and a reflection through a line at angle $\pi/4$ (p. 130).

**Finding the matrix.** The $i$th column is the result of applying the transformation to $e_i$. Example: clockwise rotation by $90^\circ$ sends $e_1=(1,0)\mapsto(0,-1)$ and $e_2=(0,1)\mapsto(1,0)$, so $A=\begin{bmatrix}0&1\\-1&0\end{bmatrix}$ (p. 130).

**Change of coordinates.** Earth-fixed axes point East, North, up. Body-fixed axes (origin at the aircraft's center of gravity) point forward, left, up. The two descriptions of one location are related by $x^{\rm earth}=p+Qx^{\rm body}$, where $p$ is the aircraft center in earth coordinates and $Q$ is $3\times3$ (p. 130). The $i$th column of $Q$ gives the earth coordinates of the aircraft's $i$th axis. For level flight heading due South, $Q=\begin{bmatrix}0&1&0\\-1&0&0\\0&0&1\end{bmatrix}$ (pp. 130–131).

*Intuition note.* A linear map is fixed by what it does to the unit vectors, so writing its matrix is just recording those images as columns. The coordinate change is a matrix product plus a shift $p$.

### 7.2 Selectors (pp. 131–132)
An $m\times n$ **selector matrix** has rows $e_{k_1}^T,\dots,e_{k_m}^T$ with each $k_i\in\{1,\dots,n\}$. Then $y=Ax=(x_{k_1},\dots,x_{k_m})$: entry $k_i$ of $x$ is copied to entry $i$ of $y$ (p. 131).

- Special cases: the identity; the **reverser** (rows $e_n^T,\dots,e_1^T$), giving $Ax=(x_n,\dots,x_1)$; the **$r{:}s$ slicing matrix** $A=[\,0_{m\times(r-1)}\;\;I_{m\times m}\;\;0_{m\times(n-s)}\,]$ with $m=s-r+1$, giving $Ax=x_{r:s}$ (p. 131).
- **Down-sampling** by 2 (n even): the $(n/2)\times n$ matrix with rows $e_1^T,e_3^T,e_5^T,\dots,e_{n-1}^T$ gives $y=(x_1,x_3,\dots,x_{n-1})$. For a time series sampled hourly, $y$ is sampled every 2 hours (p. 131).
- **Image cropping.** An $M\times N$ image is an $MN$-vector. The upper-left $(M/2)\times(N/2)$ crop is $y=Ax$, with $A$ an $(MN/4)\times MN$ selector. Row $i$ is $e_{k_i}^T$, where $k_i$ is the index in $x$ of the pixel that becomes the $i$th pixel of $y$ (p. 132).
- **Permutation matrix** ($n\times n$): each column is a unit vector and each row is a transposed unit vector, so $A$ and $A^T$ are both selectors. Exactly one entry in each row and each column is one. Then $y_i=x_{\pi_i}$, where $\pi$ uses each of $1,\dots,n$ exactly once. Example: $\pi=(3,1,2)$ gives $A=\begin{bmatrix}0&0&1\\1&0&0\\0&1&0\end{bmatrix}$ and $Ax=(x_3,x_1,x_2)$ (p. 132).

*Intuition note.* A selector does no arithmetic, only copying. A permutation matrix reorders entries without losing any.

### 7.3 Incidence matrix (pp. 132–136)
A **directed graph** has vertices $1,\dots,n$ and directed edges $1,\dots,m$; each edge goes from one node into another (Figure 7.2, p. 132). Its $n\times m$ **incidence matrix** is (p. 133)
$$A_{ij}=\begin{cases}1&\text{edge }j\text{ points to node }i\\-1&\text{edge }j\text{ points from node }i\\0&\text{otherwise.}\end{cases}$$

- It is sparse: each column has exactly two nonzeros (one $1$, one $-1$). Column $j$ identifies the two nodes joined by edge $j$. Row $i$ shows which edges touch node $i$ and whether they point in or out (p. 133).
- For Figure 7.2 (edges 1: 1→2, 2: 1→4, 3: 2→3, 4: 3→1, 5: 3→4) (pp. 132–133):
$$A=\begin{bmatrix}-1&-1&0&1&0\\1&0&-1&0&0\\0&0&1&-1&-1\\0&1&0&0&1\end{bmatrix}.$$
- It is closely related to, but not the same as, the adjacency matrix (described on p. 112 of the book, outside this unit). The adjacency matrix does not explicitly label edges, and self-edges cannot be represented by an incidence matrix (p. 133).

#### 7.3.1 Networks (pp. 133–136)
In a network, a quantity (electricity, water, heat, traffic) flows along edges. For $x\in\mathbf R^m$, $x_j$ is the flow along edge $j$; positive means in the direction of the edge, negative means opposite. Edge direction only fixes which direction counts as positive (p. 133).

**Flow conservation.** $y=Ax$ is the vector of net flows into nodes: $y_i$ = total inflow minus total outflow at node $i$, the *flow surplus*. If $Ax=0$, flow is conserved and $x$ is a **circulation** (p. 133). Example: $x=(1,-1,1,0,1)$ gives $Ax=0$. It is a unit clockwise flow on outer edges 1, 3, 5, 2 and zero on diagonal edge 4 (p. 134).

**Sources.** Exogenous flows $s\in\mathbf R^n$ enter or leave at nodes (Figure 7.3). $s_i>0$ is a source; $s_i<0$ is a sink. $Ax+s=0$ means flow is conserved at every node, counting these flows (p. 134). In an approximate lossless power-grid model, $x$ is power on lines, $s_i>0$ a generator, $s_i<0$ a load, and $s_i=0$ a substation (p. 134).

Example: $s=(1,0,-1,0)$ (one unit in at node 1, out at node 3). The flow $x=(0.6,0.3,0.6,-0.1,-0.3)$ satisfies $Ax+s=0$. The unit entering node 1 splits into 0.6 up edge 1, 0.3 right edge 2, and 0.1 along edge 4. (added step: edge 4 points from node 3 to node 1, so $x_4=-0.1$ is flow from 1 to 3.) The 0.6 passes through node 2 onto edge 3, and the 0.3 passes through node 4 up edge 5 (added step: $x_5=-0.3$ means flow opposite to the edge direction 3→4). Node 3 receives the excess unit, which leaves as the external sink (pp. 134–135).

*Intuition note.* Each column of $A$ takes one unit out of one node and puts it into another. So $Ax$ adds up what each edge delivers and removes at each node.

**Node potentials.** For $v\in\mathbf R^n$ ($v_i$ the potential at node $i$), $u=A^Tv$ gives edge differences: $u_j=v_l-v_k$ for edge $j$ from node $k$ to node $l$ (p. 135).

**Dirichlet energy.** Also called the Laplacian quadratic form of the graph (p. 135):
$$\mathcal D(v)=\|A^Tv\|^2=\sum_{\text{edges }(k,l)}(v_l-v_k)^2.$$
It is small when connected nodes have similar potentials, so it measures roughness (non-smoothness) of node values on the graph. The author says it will arise again as a roughness measure in later applications (p. 135).

Examples on the Figure 7.2 graph (p. 135):
- $v=(1,-1,2,-1)$: $A^Tv=(-2,-2,3,-1,-3)$, so $\mathcal D(v)=4+4+9+1+9=27$.
- $v=(1,2,2,1)$: $A^Tv=(1,0,0,-1,-1)$, so $\mathcal D(v)=3$.

**Chain graph** (Figure 7.4: $n$ vertices, $n-1$ edges, $i\to i+1$). Its $n\times(n-1)$ incidence matrix is the transpose of the difference matrix $D$ of (6.5), so (p. 136)
$$\mathcal D(v)=\|Dv\|^2=(v_2-v_1)^2+\cdots+(v_n-v_{n-1})^2.$$
For a time series $v$ this is a non-smoothness measure. Figure 7.5: two vectors of length 100, a smooth one with $\mathcal D(a)=1.14$ and a noisy one with $\mathcal D(b)=8.99$ (p. 136).

*Intuition note.* $A^T$ turns "values at nodes" into "differences along edges". Squaring and summing those differences scores how much the values jump between neighbours.

### 7.4 Convolution (pp. 136–143)
For an $n$-vector $a$ and an $m$-vector $b$, the convolution $c=a*b$ is an $(n+m-1)$-vector (p. 136):
$$c_k=\sum_{i+j=k+1}a_ib_j,\quad k=1,\dots,n+m-1,\tag{7.2}$$
summing over $i\in\{1..n\}$, $j\in\{1..m\}$ with $i+j=k+1$. For $n=4,m=3$ (p. 137): $c_1=a_1b_1$; $c_2=a_1b_2+a_2b_1$; $c_3=a_1b_3+a_2b_2+a_3b_1$; $c_4=a_2b_3+a_3b_2+a_4b_1$; $c_5=a_3b_3+a_4b_2$; $c_6=a_4b_3$. For $n=m=1$ it is ordinary multiplication; if $n=1$ or $m=1$ it is scalar–vector multiplication (p. 137).

Numerical example: $(1,0,-1)*(2,1,-1)=(2,1,-3,-1,1)$, with entries $(1)(2)=2$; $(1)(1)+(0)(2)=1$; $(1)(-1)+(0)(1)+(-1)(2)=-3$; $(0)(-1)+(-1)(1)=-1$; $(-1)(-1)=1$ (p. 137).

**Polynomial multiplication.** Let $p(x)=a_1+a_2x+\dots+a_nx^{n-1}$ and $q(x)=b_1+\dots+b_mx^{m-1}$. Then $p(x)q(x)=c_1+c_2x+\dots+c_{n+m-1}x^{n+m-2}$ with $c=a*b$. Proof: expand the $mn$ terms $a_ib_jx^{i+j-2}$. Those multiplying $x^{k-1}$ satisfy $i+j-2=k-1$, i.e. $i+j=k+1$. So the coefficient of $x^{k-1}$ is $\sum_{i+j=k+1}a_ib_j=c_k$ (p. 137).

**Properties.** Convolution is symmetric ($a*b=b*a$) and associative ($(a*b)*c=a*(b*c)$). Also, $a*b=0$ implies $a=0$ or $b=0$. The author says these follow from the polynomial property and can also be shown directly. Symmetry: $p(x)q(x)=q(x)p(x)$, so the coefficient vectors $a*b$ and $b*a$ coincide (p. 137).

**Matrix form.** $a*b=T(b)a=T(a)b$, where $T(b)$ is $(n+m-1)\times n$ (p. 138):
$$T(b)_{ij}=\begin{cases}b_{i-j+1}&1\le i-j+1\le m\\0&\text{otherwise.}\end{cases}\tag{7.3}$$
For $n=4,m=3$, $T(b)$ has first column $(b_1,b_2,b_3,0,0,0)^T$, and each later column is the previous one shifted down by one row; $T(a)$ is $6\times3$ with first column $(a_1,a_2,a_3,a_4,0,0)^T$ and shifted copies (p. 138). These are **Toeplitz matrices**: entries are constant along each diagonal ($i-j$ constant). Columns are shifted copies of the vector, padded with zeros (p. 138).

**Variations.** Other definitions exist: infinite two-sided sequences; or dropping the top and bottom rows of $T(a)$ that do not contain all of $a$'s coefficients. The book uses (7.2) throughout (p. 138).

**Examples (p. 138).**
- *Smoothing:* $a=(1/3,1/3,1/3)$, $y=a*x$ has length $n+2$; for $i=3,\dots,n$, $y_i$ is the average of $x_i,x_{i-1},x_{i-2}$ (3-period moving average; Figure 7.6, p. 139).
- *First differences:* $a=(1,-1)$ gives $y=(x_1,x_2-x_1,\dots,x_n-x_{n-1},-x_n)$ (first and last entries are differences if $x_0=x_{n+1}=0$).
- *Audio filtering:* $y=a*x$, with $a$ typically shorter than about 0.1 s of real time. Depending on $a$, frequencies are enhanced or suppressed, like tone controls.
- *Communication channel:* a common model is $y=c*u$, with $c$ the channel impulse response.

**Input–output system.** $y=h*u$, with $u$ an $m$-vector input, $h$ the $n$-vector system impulse response, $y$ of length $m+n-1$. Entries (with $u_k=0$ for $k\le0$ or $k>m$) (p. 140):
$$y_i=\sum_{j=1}^nu_{i-j+1}h_j.$$
So $y_i$ is a linear combination of the current input and the past $n-1$ inputs, with coefficients $h_1,\dots,h_n$. For example, $h_3$ is the factor by which the input at any time affects the output 2 steps later. Illustration: $u_t$ is heater power, $y_t$ the temperature rise (p. 140).

**Complexity.** The naive method (or $T(a)b$, using the zeros) takes about $2mn$ flops. Forming $T$ needs storage of $mn$ numbers although the data are only $m+n$ numbers. A fast convolution algorithm (based on the FFT, beyond the book's scope) needs about $5(m+n)\log_2(m+n)$ flops and no extra memory beyond the $m+n$ numbers (p. 140).

*Intuition note.* Convolution is "multiply two polynomials" or "slide a short pattern along a signal and take weighted sums". The Toeplitz matrix is that sliding written as a matrix.

#### 7.4.1 2-D convolution (pp. 140–143)
For $A$ ($m\times n$) and $B$ ($p\times q$), the convolution is the $(m+p-1)\times(n+q-1)$ matrix (p. 140)
$$C_{rs}=\sum_{i+k=r+1,\;j+l=s+1}A_{ij}B_{kl},$$
with out-of-range entries taken as zero. The notation is $C=A\star B$ (not $A*B$). As in 1-D, $A\star B=B\star A$ and $(A\star B)\star C=A\star(B\star C)$ (p. 141).

**Image blurring.** For an $m\times n$ image $X$, $Y=X\star B$ blurs it using point spread function (PSF) $B$. In vector form $y=T(B)x$, with $T(B)$ of size $(m+p-1)(n+q-1)\times mn$ (p. 141).
- With $B=\begin{bmatrix}1/4&1/4\\1/4&1/4\end{bmatrix}$ (7.4), each pixel of $Y$ is the average of a $2\times2$ block of $X$. The $8\times9$ example image $X$ in (7.5) has a ring of 1s with a black "Π" of 0s (Figure 7.7). $X\star B$ is $9\times10$ with a border of $1/4$ and $1/2$ values and interior values such as $3/4$, $1/4$, $1$ (p. 141).
- With $D^{\rm hor}=[\,1\;\;-1\,]$: $Y_{ij}=X_{ij}-X_{i,j-1}$ (horizontal first differences), with $Y_{i1}=X_{i1}$ and $X_{i,n+1}=-X_{in}$. With $D^{\rm ver}=\begin{bmatrix}1\\-1\end{bmatrix}$: $Y_{ij}=X_{ij}-X_{i-1,j}$ (vertical differences). The book prints both results for $X$ (p. 142). In the printed $X\star D^{\rm hor}$, the first column is all 1s and the last column all $-1$s.
- Figure 7.8: a $512\times512$ image convolved with an $8\times8$ matrix with all entries $1/64$ gives a $519\times519$ image (pp. 142–143).

## Toy example (ours, not from the text)
Take $a=(1,1)$ (polynomial $1+x$) and $b=(1,2)$ (polynomial $1+2x$), so $n=m=2$ and $c$ has length 3.

By (7.2): $c_1=a_1b_1=1$; $c_2=a_1b_2+a_2b_1=2+1=3$; $c_3=a_2b_2=2$. So $a*b=(1,3,2)$.

Check by polynomials: $(1+x)(1+2x)=1+2x+x+2x^2=1+3x+2x^2$, coefficients $(1,3,2)$. ✓.

Check by Toeplitz: $T(b)$ is $3\times2$ with entries $b_{i-j+1}$: $T(b)=\begin{bmatrix}1&0\\2&1\\0&2\end{bmatrix}$. Then $T(b)a=(1\cdot1+0\cdot1,\;2\cdot1+1\cdot1,\;0\cdot1+2\cdot1)=(1,3,2)$ ✓. Also $T(a)=\begin{bmatrix}1&0\\1&1\\0&1\end{bmatrix}$ and $T(a)b=(1,\;1\cdot1+1\cdot2,\;2)=(1,3,2)$ ✓. All three views agree.

## Concepts
- [[matrix as transformation]] — the $i$th column of the matrix is the image of $e_i$; used to build rotation, reflection, etc. (p. 130)
- [[linear map / transformation]] — scaling, dilation, rotation, reflection and projection written as $y=Ax$ (p. 129)
- [[projection]] — closest point of a set (here a line through the origin) to $x$, written as a matrix (p. 130)
- [[change of basis]] — here a change of coordinates $x^{\rm earth}=p+Qx^{\rm body}$, which includes a shift $p$ (p. 130)
- [[selector-matrix]] (new) — each row is a transposed unit vector, so $Ax$ copies chosen entries (p. 131)
- [[permutation-matrix]] (new) — square matrix such that both $A$ and $A^T$ are selectors; reorders entries (p. 132)
- [[incidence matrix]] — $n\times m$ matrix of a directed graph, $\pm1$ entries per edge; flows to net node flows (p. 133)
- [[adjacency matrix]] — related but different from incidence; does not explicitly label edges (p. 133)
- [[flow-conservation]] (new) — $Ax=0$, or $Ax+s=0$ with sources; $x$ with $Ax=0$ is a circulation (pp. 133–134)
- [[dirichlet-energy]] (new; the author also calls it the Laplacian quadratic form, cf. [[graph Laplacian]]) — $\|A^Tv\|^2=\sum(v_l-v_k)^2$, roughness of node values (p. 135)
- [[convolution]] (new) — $c_k=\sum_{i+j=k+1}a_ib_j$; coefficients of a polynomial product (p. 136)
- [[toeplitz-matrix]] (new) — entries constant along diagonals; $T(a)$ has shifted copies of $a$ as columns (p. 138)
- [[point-spread-function]] (new) — the matrix $B$ in the 2-D convolution $X\star B$ that blurs or differences an image (p. 141)
- [[norm]] — squared norm $\|\cdot\|^2$ used in the Dirichlet energy (p. 135)

## Canonical instances
- [[rotation-90-clockwise]] — matrix found by rotating $e_1,e_2$ (p. 130)
- [[aircraft-body-to-earth-coordinates]] — $x^{\rm earth}=p+Qx^{\rm body}$ (p. 130)
- [[image-cropping-selector]] — cropping as an $(MN/4)\times MN$ selector (p. 132)
- [[figure-7-2-graph]] — 4 nodes, 5 edges; its incidence matrix, circulation and source-flow examples (pp. 132–135)
- [[power-grid-flow-model]] — generators, loads, substations as $s_i>0,<0,=0$ (p. 134)
- [[chain-graph-roughness]] — $\mathcal D(v)=\|Dv\|^2$ for time series (p. 136)
- [[polynomial-multiplication-as-convolution]] — $c=a*b$ gives the product's coefficients (p. 137)
- [[moving-average-smoothing]] — $a=(1/3,1/3,1/3)$ (p. 138)
- [[heater-temperature-impulse-response]] — input–output system $y=h*u$ (p. 140)
- [[image-blur-8x9]] — $X\star B$ with a $2\times2$ averaging PSF (p. 141)

## Bridges (candidates)
- [same-math] Dirichlet energy $\|A^Tv\|^2$ ↔ graph Laplacian: the unit itself calls it the Laplacian quadratic form of the graph.
- [same-math] Convolution of coefficient vectors ↔ polynomial multiplication (shown on p. 137).
- [structural-analogy] Toeplitz matrix $T(a)$ ↔ shift-invariant (time-invariant) linear systems: each column is the previous one shifted.
- [structural-analogy] Flow conservation $Ax+s=0$ ↔ column sums of $A$ being zero (hint of ex. 7.8): conserved quantity in a network.
- [structural-analogy] Incidence matrix of a chain graph ↔ difference matrix $D$ ↔ first-order differences as convolution with $(1,-1)$.
- [metaphor] Dirichlet energy as roughness ↔ smoothing penalties in regularised estimation (later chapters, not in this unit).

## Questions this raises
- Which standard transformations do the other properties of rotation/reflection matrices (length preservation, inverse) hold for? The unit only gives formulas.
- Why does $a*b=0$ force $a=0$ or $b=0$, and why does it matter for undoing a convolution (equalization, ex. 7.15)?
- How does the FFT-based algorithm achieve $O((m+n)\log(m+n))$ cost?
- How does the Dirichlet energy of a social-network potential behave (ex. 7.9)?

## Exercises worth doing
- Ex. 7.1 (p. 144) — build the projection matrix onto the line through $(1,3)$; practises the formula of 7.1 or the column method — difficulty: easy
- Ex. 7.4 (p. 144) — averaging down-sampling and linear-interpolation up-conversion as matrices — difficulty: medium
- Ex. 7.6 (p. 144) — rows of an incidence matrix are linearly dependent (hint: sum the rows) — difficulty: easy
- Ex. 7.8 (p. 144) — flow conservation forces $\mathbf 1^Ts=0$ (hint: columns of $A$ sum to zero) — difficulty: easy
- Ex. 7.13 (p. 145) — sum of coefficients of $a*b$ equals the product of the sums (hint: $\mathbf 1^Ta=p(1)$) — difficulty: medium
- Ex. 7.15 (p. 146) — channel equalization $h*c\approx e_1$ and a numerical experiment — difficulty: medium

## Reading notes
- Printed page = pdf page − 10 (pdf 139 = printed 129).
- For Figure 7.8 (p. 143) only the caption is used here; the image content is not described. The caption gives the sizes $512\times512$ → $519\times519$ and credits NASA.
- Text-layer matrices were garbled; all matrices here were checked against the page images.
- The unit uses calligraphic $\mathcal D(v)$ for Dirichlet energy and plain $D$ for the difference matrix; do not confuse them. The dilation matrix $D$ on p. 129 is another use of the same letter.
- The text says the chain graph's incidence matrix is the transpose of the difference matrix of (6.5) on p. 119 of another chapter; that matrix is not shown here.
- The numerical convolution example $(1,0,-1)*(2,1,-1)$ on p. 137 is reproduced as printed; I found no misprints in this unit.
