---
id: boyd-2018-vmls/ch08-linear
work: boyd-2018-vmls
unit: Chapter 8 — Linear equations
pages: 147–162
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 4
pipeline_version: 0.1
---
# Linear equations

## L0 — One line
Every linear function of vectors is a matrix–vector product $f(x)=Ax$, and such functions serve as models (affine, Taylor, regression), while systems of linear equations $Ax=b$ cover interpolation, chemical balancing, diffusion and input–output.

## L1 — The gist (≤ 120 words)
This chapter asks what a vector-valued linear function is and where such functions and linear equations appear. A function $f:\mathbf R^n\to\mathbf R^m$ is linear exactly when it satisfies superposition, and then it equals $x\mapsto Ax$ for one unique matrix. Adding a constant vector gives affine functions. Linear and affine functions serve as models and approximations (elasticity, Taylor approximation, regression). A system of linear equations is written $Ax=b$. It can have no, one, or many solutions. Applications are polynomial interpolation, balancing chemical reactions, diffusion systems and Leontief's economic model. Chapter 11 will address how to decide whether such a system has a solution and how to find one.

**Prerequisites:** matrix–vector product; unit vectors; partial derivatives; incidence matrix (§7.3); Vandermonde matrix (6.7).

## L2 — Key ideas
- A function satisfying superposition $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$ is linear. Every such $f$ equals $Ax$ for exactly one matrix $A$, and every $Ax$ is linear (p. 148).
- The columns of $A$ are $f(e_1),\dots,f(e_n)$, so evaluating $f$ at the unit vectors determines $f$ completely (p. 148).
- Affine means $Ax+b$. It is equivalent to superposition for coefficients with $\alpha+\beta=1$. $A$ and $b$ are unique and come from $f(0), f(e_k)$ (pp. 149–150).
- Abs value and sort fail superposition, so they are not linear (p. 149).
- Linear/affine models approximate real relations: elasticity, structural deformation, first-order Taylor approximation with the Jacobian, regression predictions (pp. 150–152).
- A system of $m$ equations in $n$ unknowns is $Ax=b$. It is over-determined if $m>n$, under-determined if $m<n$, square if $m=n$ (p. 153).
- Solving $Ax=b$ means finding coefficients that write $b$ as a linear combination of the columns of $A$ (p. 154).
- Interpolation, chemical balancing, diffusion (with the incidence matrix) and the Leontief model $(I-A)x=d$ are all linear systems (pp. 154–158).

## L3 — Walkthrough

### 8.1 Linear and affine functions
**Vector-valued functions.** $f:\mathbf R^n\to\mathbf R^m$ maps an $n$-vector $x$ to the $m$-vector $f(x)=(f_1(x),\dots,f_m(x))$. Each component $f_i$ is a scalar-valued function of $x$ (p. 147).

**Matrix-vector product function.** For an $m\times n$ matrix $A$, $f(x)=Ax$ defines $f:\mathbf R^n\to\mathbf R^m$. The inner product function $a^Tx$ is the case $m=1$ (p. 147).

**Superposition.** $f(x)=Ax$ is linear, i.e. it satisfies
$$f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)\tag{8.1}$$
for all $n$-vectors $x,y$ and all scalars $\alpha,\beta$. The author notes that the symbols are overloaded. On the left, $\alpha x+\beta y$ is an $n$-vector sum and $f(\cdot)$ is an $m$-vector. On the right, scalar multiples and sum are of $m$-vectors (p. 147). Verification (p. 148):
$$f(\alpha x+\beta y)=A(\alpha x+\beta y)=A(\alpha x)+A(\beta y)=\alpha(Ax)+\beta(Ay)=\alpha f(x)+\beta f(y).$$

**Converse.** If $f$ maps $n$-vectors to $m$-vectors and satisfies (8.1), then there is an $m\times n$ matrix $A$ with $f(x)=Ax$ for all $x$. The proof follows §2.1 by showing
$$f(x)=x_1f(e_1)+x_2f(e_2)+\cdots+x_nf(e_n),\tag{8.2}$$
where $e_k$ is the $k$th unit vector. The right side is $Ax$ with $A=[\,f(e_1)\ f(e_2)\ \cdots\ f(e_n)\,]$ (shape $m\times n$). So a linear $f$ is completely characterized by its values at $e_1,\dots,e_n$. The matrix is unique: exactly one $A$ gives $f(x)=Ax$ for all $x$ (p. 148).

*Intuition note.* To know a linear function, you only need to know what it does to the $n$ unit vectors. Every other input is a weighted mix of those, and the output is the same weighted mix of the outputs.

**Examples of linear functions** (all $\mathbf R^n\to\mathbf R^n$; pp. 148–149):
- Negation $f(x)=-x$: $A=-I$.
- Reversal $f(x)=(x_n,\dots,x_1)$: $A$ is the identity with its columns in reverse order (the reverser matrix of §7.2).
- Running sum $f(x)=(x_1,\,x_1+x_2,\dots,x_1+\cdots+x_n)$: $A_{ij}=1$ if $i\ge j$, else $0$ (running sum matrix of (6.6)).
- De-meaning $f(x)=x-\mathbf{avg}(x)\mathbf 1$: $A$ has diagonal entries $1-1/n$ and all off-diagonal entries $-1/n$.

**Examples that are not linear** (superposition counterexamples, p. 149):
- Absolute value $f(x)=(|x_1|,\dots,|x_n|)$. With $n=1$, $x=1$, $y=0$, $\alpha=-1$, $\beta=0$: $f(\alpha x+\beta y)=1\ne\alpha f(x)+\beta f(y)=-1$.
- Sort (decreasing order); linear only when $n=1$. With $n=2$, $x=(1,0)$, $y=(0,1)$, $\alpha=\beta=1$: $f(\alpha x+\beta y)=(1,1)\ne\alpha f(x)+\beta f(y)=(2,0)$.

**Affine functions.** $f:\mathbf R^n\to\mathbf R^m$ is affine if $f(x)=Ax+b$, with $A$ an $m\times n$ matrix and $b$ an $m$-vector. It can be shown that $f$ is affine if and only if $f(\alpha x+\beta y)=\alpha f(x)+\beta f(y)$ for all $x,y$ and all scalars with $\alpha+\beta=1$. So superposition holds for affine combinations; for linear functions it holds for any linear combination (pp. 149–150).

$A$ and $b$ are unique, and are obtained by evaluating $f$ at $0,e_1,\dots,e_n$:
$$A=[\,f(e_1)-f(0)\ \ f(e_2)-f(0)\ \cdots\ f(e_n)-f(0)\,],\qquad b=f(0).$$
Affine functions are often called linear, though they are linear only when $b=0$ (p. 150).

*Intuition note.* An affine function is a linear one shifted by a fixed vector. Evaluating at $0$ finds the shift. Subtracting it from the other values leaves the linear part.

### 8.2 Linear function models
Many relations in natural science, engineering and social science can be approximated as linear or affine. The linear function is then called a *model* or *approximation*, to stress that it is not exact (p. 150).

- **Price elasticity of demand.** $\delta^{\text{price}}_i=(p_i^{\text{new}}-p_i)/p_i$ and $\delta^{\text{dem}}_i=(d_i^{\text{new}}-d_i)/d_i$ are fractional changes. The linear model is $\delta^{\text{dem}}=E^{\text{d}}\delta^{\text{price}}$, with $E^{\text{d}}$ the $n\times n$ demand elasticity matrix. If $E^{\text{d}}_{11}=-0.4$ and $E^{\text{d}}_{21}=0.2$, a 1% rise in price 1 (other prices fixed) lowers demand 1 by 0.4% and raises demand 2 by 0.2%. Good 2 is then a partial substitute for good 1 (p. 150).
- **Elastic deformation.** For a loading $f$ ($n$-vector of forces) and displacements $d$ ($m$-vector), small displacements are well approximated by $d=Cf$. $C$ is the $m\times n$ compliance matrix, with entries in m/N (p. 150).

**8.2.1 Taylor approximation.** Let $f:\mathbf R^n\to\mathbf R^m$ be differentiable (has partial derivatives) and $z$ an $n$-vector. The first-order Taylor approximation near $z$ is, for $i=1,\dots,m$,
$$\hat f(x)_i=f_i(z)+\frac{\partial f_i}{\partial x_1}(z)(x_1-z_1)+\cdots+\frac{\partial f_i}{\partial x_n}(z)(x_n-z_n)=f_i(z)+\nabla f_i(z)^T(x-z).$$
In compact form,
$$\hat f(x)=f(z)+Df(z)(x-z),\tag{8.3}$$
where the $m\times n$ Jacobian $Df(z)$ has entries $Df(z)_{ij}=\frac{\partial f_i}{\partial x_j}(z)$. Its rows are $\nabla f_i(z)^T$. For $x$ near $z$, $\hat f(x)$ is a very good approximation of $f(x)$. $\hat f$ is an affine function of $x$ (often called a "linear approximation", though in general not linear). It is sometimes written $\hat f(x;z)$ to show the base point (p. 151).

*Intuition note.* Near a point $z$, a smooth function looks like an affine one. The Jacobian holds the slopes of each output with respect to each input.

**8.2.2 Regression model.** Recall $\hat y=x^T\beta+v$ (8.4), with feature $n$-vector $x$, weights $\beta$, offset $v$. For $N$ examples, $\hat y^{(i)}=(x^{(i)})^T\beta+v$. With responses $y^{(i)}$, the residuals are $r^{(i)}=y^{(i)}-\hat y^{(i)}$ (some authors use the opposite sign) (pp. 151–152).

Form the $n\times N$ feature matrix $X$ with columns $x^{(i)}$. Let $y^{\text{d}}$ (actual responses), $\hat y^{\text{d}}$ (predictions), $r^{\text{d}}$ (residuals) be $N$-vectors. Then (p. 152)
$$\hat y^{\text{d}}=X^T\beta+v\mathbf 1,\qquad r^{\text{d}}=y^{\text{d}}-\hat y^{\text{d}}=y^{\text{d}}-X^T\beta-v\mathbf 1.$$
To absorb the offset, add a first feature equal to one:
$$\hat y^{\text{d}}=\begin{bmatrix}\mathbf 1^T\\X\end{bmatrix}^T\begin{bmatrix}v\\\beta\end{bmatrix}=\tilde X^T\tilde\beta,$$
with new feature matrix $\tilde X$ (a new first row of ones; shape $(n+1)\times N$, added step) and $\tilde\beta=(v,\beta)$. This is often written without tildes as $\hat y^{\text{d}}=X^T\beta$. Conclusion: the prediction vector is a linear function of the parameters $(v,\beta)$, and the residual vector is an affine function of them (p. 152).

### 8.3 Systems of linear equations
$m$ linear equations in $n$ unknowns $x_1,\dots,x_n$ have the form $A_{i1}x_1+\cdots+A_{in}x_n=b_i$, $i=1,\dots,m$. The $A_{ij}$ are the *coefficients*, the $b_i$ the *right-hand sides*. In matrix form
$$Ax=b.\tag{8.5}$$
$A$ ($m\times n$) is the coefficient matrix, $b$ the right-hand side. An $n$-vector $x$ is a *solution* if $Ax=b$. A system can have no solutions, one solution, or multiple solutions (pp. 152–153).

**Examples** (p. 153):
- $x_1+x_2=1,\ x_1=-1,\ x_1-x_2=0$: $A=\begin{bmatrix}1&1\\1&0\\1&-1\end{bmatrix}$, $b=(1,-1,0)$. No solutions.
- $x_1+x_2=1,\ x_2+x_3=2$: $A=\begin{bmatrix}1&1&0\\0&1&1\end{bmatrix}$, $b=(1,2)$. Multiple solutions, including $(1,0,2)$ and $(0,1,1)$.

**Over-/under-determined.** The system is *over-determined* if $m>n$ (tall $A$, more equations than unknowns), *under-determined* if $m<n$ (wide $A$), *square* if $m=n$. $Ax=0$ is *homogeneous*, and $x=0$ always solves it. Chapter 11 will say how to decide whether a solution exists and how to find one (p. 153).

#### 8.3.1 Examples
**Coefficients of linear combinations.** With columns $a_1,\dots,a_n$ of $A$, $Ax=b$ reads $x_1a_1+\cdots+x_na_n=b$. Solving $Ax=b$ is the same as finding coefficients that express $b$ as a linear combination of the columns (p. 154).

**Polynomial interpolation.** To find a polynomial $p$ of degree at most $n-1$ with $p(t_i)=y_i$ for $m$ points, write $Ac=y$. $A$ is the Vandermonde matrix (6.7) and $c$ the $n$-vector of coefficients (p. 154).

**Balancing chemical reactions.** A reaction is $a_1R_1+\cdots+a_pR_p\to b_1P_1+\cdots+b_qP_q$, with positive numbers $a_j,b_j$ that can be scaled arbitrarily. By convention they are integers with least common divisor one. Atoms of each type (and charge, if any) must balance. Electrolysis: $2\mathrm H_2\mathrm O\to2\mathrm H_2+\mathrm O_2$, equivalently $3\mathrm H_2\mathrm O\to3\mathrm H_2+(3/2)\mathrm O_2$ (p. 154).

Let $m$ be the number of atom types. Define the $m\times p$ matrix $R_{ij}=$ number of atoms of type $i$ in $R_j$ (column $j$ is the formula of $R_j$), and the $m\times q$ matrix $P$ likewise. With $a\in\mathbf R^p$, $b\in\mathbf R^q$, $Ra$ and $Pb$ count atoms of each type on each side. Balance is $Ra=Pb$, i.e.
$$\begin{bmatrix}R&-P\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}=0,$$
$m$ homogeneous equations. Since $a=0,b=0$ solves this, a nonzero solution is wanted. Fixing $a_1=1$ (which may make others fractional) gives
$$\begin{bmatrix}R&-P\\e_1^T&0\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}=e_{m+1},$$
$m+1$ equations in $p+q$ variables. Solving this is *balancing* the reaction (p. 155).

Water: $p=1$, $q=2$, $m=2$, $R=\begin{bmatrix}2\\1\end{bmatrix}$, $P=\begin{bmatrix}2&0\\0&2\end{bmatrix}$:
$$\begin{bmatrix}2&-2&0\\1&0&-2\\1&0&0\end{bmatrix}\begin{bmatrix}a_1\\b_1\\b_2\end{bmatrix}=\begin{bmatrix}0\\0\\1\end{bmatrix},$$
with solution $(1,1,1/2)$. Multiplying by 2 gives the reaction above (p. 155).

**Diffusion systems.** Take a directed graph with $n$ nodes and $m$ edges (§6.1). Edge $j$ carries a scalar flow $f_j$; positive means flow along the edge direction, negative the opposite. Node $i$ has an exogenous source flow $s_i$ ($s_i>0$ injects, $s_i<0$ removes). Flows may be heat (Watts), current (Amps), or mass (pp. 155–156).

*Conservation:* at each node the total flow entering from adjacent edges and the source is zero. For node 1 in figure 8.1 (edges 1, 2 enter, edge 3 leaves):
$$f_1+f_2-f_3+s_1=0.$$
At all nodes:
$$Af+s=0,\tag{8.6}$$
with $A$ ($n\times m$) the incidence matrix of §7.3. This is Kirchhoff's current law in circuits, and conservation of mass for mass flows (p. 156).

Each node $i$ has a potential $e_i$ (temperature, voltage, or concentration). Here $e$ is the potential vector, not a unit vector (p. 156). The flow on an edge is proportional to the potential difference: $r_jf_j=e_k-e_l$ for edge $j$ from node $k$ to node $l$, where $r_j$ (typically positive) is the resistance. Example: $r_8f_8=e_2-e_3$ (p. 157). Compactly,
$$Rf=-A^Te,\tag{8.7}$$
with $R=\mathbf{diag}(r)$ ($m\times m$). The whole model is
$$\begin{bmatrix}A&I&0\\R&0&A^T\end{bmatrix}\begin{bmatrix}f\\s\\e\end{bmatrix}=0,$$
block shapes $[n\times m,\ n\times n,\ n\times n;\ m\times m,\ m\times n,\ m\times n]$ (shapes added). It is $n+m$ homogeneous equations in $m+2n$ variables. It is under-determined, and more equations can be added by specifying some entries of $f,s,e$ (p. 157).

*Intuition note.* Two laws give the whole model. What flows into a node must balance the source (conservation). Flow along an edge is driven by the potential difference across it (resistance law).

**Leontief input–output model.** An economy has $n$ sectors. $x_i$ is the activity level (total output, in a common unit such as dollars) of sector $i$. $d_i$ is consumer demand for sector $i$. Producing $x_j$ in sector $j$ requires $A_{ij}x_j$ of sector $i$'s output; $A_{ii}\ne0$ is allowed. $A$ is the input–output matrix, and $Ax$ gives the outputs needed to support production $x$ (this sounds circular, but isn't) (p. 157). Total production must equal demand plus what production requires:
$$x=Ax+d,\qquad\text{so}\qquad (I-A)x=d,$$
$n$ equations in $n$ unknowns, to find the output levels that support a given $d$. It was developed by Leontief in the late 1940s and earned him the 1973 Nobel Prize in economics (p. 158).

## Toy example (ours)
Suppose an unknown function $g:\mathbf R^2\to\mathbf R^2$ is known to be affine, with $g(0)=(1,1)$, $g(e_1)=(3,2)$, $g(e_2)=(1,4)$.
- $b=g(0)=(1,1)$.
- Columns of $A$: $g(e_1)-g(0)=(2,1)$ and $g(e_2)-g(0)=(0,3)$, so $A=\begin{bmatrix}2&0\\1&3\end{bmatrix}$.
- Check at $x=(4,-1)$: $Ax+b=(2\cdot4+0,\ 1\cdot4+3\cdot(-1))+(1,1)=(8,1)+(1,1)=(9,2)$. Cross-check (added step): $g(x)=g(0)+x_1\,(g(e_1)-g(0))+x_2\,(g(e_2)-g(0))=(1,1)+4(2,1)-1(0,3)=(1,1)+(8,4)-(0,3)=(9,2)$. ✓.
- Now solve $Ax=(8,1)$ as "coefficients of columns": $x_1(2,1)+x_2(0,3)=(8,1)$. First entry: $2x_1=8$, so $x_1=4$. Second: $4+3x_2=1$, so $x_2=-1$. So $x=(4,-1)$.

## Concepts
- [[linear-map-transformation]] — a function satisfying superposition (8.1); always of the form $x\mapsto Ax$ (pp. 147–148)
- [[matrix-as-transformation]] — columns of $A$ are $f(e_1),\dots,f(e_n)$ (p. 148)
- [[linear-combination]] — $Ax=b$ asks for coefficients expressing $b$ via the columns of $A$ (p. 154)
- [[superposition]] (new) — property (8.1); for affine functions it holds when $\alpha+\beta=1$ (pp. 147, 150)
- [[affine-function]] (new) — $f(x)=Ax+b$, with unique $A,b$; linear only if $b=0$ (pp. 149–150)
- [[taylor-approximation-jacobian]] (new) — $\hat f(x)=f(z)+Df(z)(x-z)$; an affine approximation (p. 151)
- [[system-of-linear-equations]] (new) — $Ax=b$; may have no, one, or many solutions (p. 153)
- [[overdetermined-underdetermined]] (new) — $m>n$ / $m<n$ equations vs unknowns; square if equal (p. 153)
- [[incidence-matrix]] — here used for flow conservation $Af+s=0$ (p. 156)

## Canonical instances
- [[polynomial-interpolation]] — $Ac=y$ with a Vandermonde matrix (p. 154)
- [[chemical-reaction-balancing]] — homogeneous system $[R\ -P]\,(a,b)=0$ plus normalisation $a_1=1$ (pp. 154–155)
- [[diffusion-system]] — conservation $Af+s=0$ and edge law $Rf=-A^Te$ (pp. 155–157)
- [[leontief-input-output]] — $(I-A)x=d$ (pp. 157–158)
- [[price-elasticity-model]] — $\delta^{\text{dem}}=E^{\text{d}}\delta^{\text{price}}$ (p. 150)
- [[regression-as-linear-in-parameters]] — predictions linear, residuals affine in $(v,\beta)$ (p. 152)

## Bridges (candidates)
- [same-math] linear function determined by $f(e_k)$ ↔ linear-algebra: matrix as transformation (columns are images of basis vectors) — same statement.
- [same-math] diffusion system with incidence matrix $A$ ↔ network analysis: flow conservation on a graph uses the incidence matrix — the same $A$ as in §7.3.
- [structural-analogy] Leontief balance $x=Ax+d$ ↔ network analysis: walks and influence propagation through a matrix — flows along weighted links.
- [structural-analogy] regression with features $X$ ↔ social-science modelling: a model linear in parameters, so fitting becomes a linear-algebra problem.

## Questions this raises
- When does $Ax=b$ have no, exactly one, or many solutions? (Chapter 11 is promised on p. 153.)
- Is the Leontief system $(I-A)x=d$ always solvable? Can the solution have negative outputs? (The text only says it is $n$ equations in $n$ unknowns.)
- How good is a Taylor approximation, and how far from $z$ can $x$ be before it fails? (The text says only "near" $z$.)
- If a balancing system has many solutions, which one is the "right" reaction?

## Exercises worth doing
- Ex. 8.2 (p. 159) — averages commute with affine maps; uses the $\alpha+\beta=1$ idea — easy
- Ex. 8.3 (p. 159) — write the cross product as a matrix times $x$ — easy
- Ex. 8.7 (p. 160) — turn value and derivative conditions into $Ac=b$ and classify the system — medium
- Ex. 8.11 (p. 160) — turn range measurements into linear equations by squaring and subtracting — medium
- Ex. 8.14 (p. 161) — affine combinations of solutions of $Ax=b$ are solutions — easy
- Ex. 8.16 (p. 162) — bilinear interpolation as a $4\times4$ system — medium

## Reading notes
- Printed page = pdf − 10 (pdf 157–172 ↔ printed 147–162). Printed numbers are visible and were used.
- The text layer garbles matrices (reversal, running sum, de-meaning, balancing equations, block system); these were checked against the page images.
- The unit covers §§8.1–8.3 (with 8.2.1, 8.2.2, 8.3.1) and Exercises 8.1–8.16. No solutions are printed in these pages.
- The text refers to earlier and later material not included here (§2.1, §2.2, §6.1, (6.6), (6.7), §7.2, §7.3, §C.1, chapter 11, the example on p. 120).
- Page 158 ends the main text (about three-quarters empty); the exercises start on p. 159.
