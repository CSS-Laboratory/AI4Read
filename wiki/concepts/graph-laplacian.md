---
id: graph-laplacian
type: concept
fields: [linear-algebra, control-theory]
n_sources: 33
tiers: [deep, core]
grounding: digests
sources: [astrom-2021-feedbacksystems/ch03-system-p2, boyd-2018-vmls/ch07-matrix, boyd-2018-vmls/ch15-multi, spielman-2025-sagt/ch01-introduction, spielman-2025-sagt/ch03-laplacian, spielman-2025-sagt/ch04-adjacency, spielman-2025-sagt/ch05-fundamental, spielman-2025-sagt/ch06-comparing, spielman-2025-sagt/ch07-cayley, spielman-2025-sagt/ch10-random, spielman-2025-sagt/ch11-walks, spielman-2025-sagt/ch12-effective, spielman-2025-sagt/ch13-random, spielman-2025-sagt/ch14-approximating, spielman-2025-sagt/ch17-monotonicity, spielman-2025-sagt/ch19-independent, spielman-2025-sagt/ch20-graph, spielman-2025-sagt/ch21-cheeger, spielman-2025-sagt/ch22-local, spielman-2025-sagt/ch24-nodal, spielman-2025-sagt/ch25-second, spielman-2025-sagt/ch26-planar, spielman-2025-sagt/ch27-properties, spielman-2025-sagt/ch29-expander, spielman-2025-sagt/ch30-simple, spielman-2025-sagt/ch32-sparsification, spielman-2025-sagt/ch33-linear, spielman-2025-sagt/ch34-iterative, spielman-2025-sagt/ch35-conjugate, spielman-2025-sagt/ch36-preconditioning, spielman-2025-sagt/ch37-augmented, spielman-2025-sagt/ch38-fast, vonluxburg-2007-spectralclustering/main]
raw_ids: [graph Laplacian]
canon_spine: linear-algebra
generated_by: build_kg.py
---

# graph-laplacian

## Canon spine entry

- **graph Laplacian** (linear-algebra): L = D − A = BᵀB; its quadratic form Σ(xᵢ − xⱼ)² measures how "unsmooth" a signal is on a network (grad)

## Definitions in the sources

### linear-algebra

- [[boyd-2018-vmls/ch07-matrix]] (p. 135): $\|A^Tv\|^2=\sum(v_l-v_k)^2$, roughness of node values [as `graph Laplacian`]
- [[boyd-2018-vmls/ch15-multi]] (p. 317): canon link: Dirichlet energy $\|A^Tx\|^2$ for an incidence matrix, used as "Laplacian regularization"
- [[spielman-2025-sagt/ch01-introduction]] (p. 5): $L_G=D_G-M_G$; its quadratic form is $\sum w_{a,b}(x(a)-x(b))^2$
- [[spielman-2025-sagt/ch03-laplacian]] (p. 29): $L_G=D_G-A_G=\sum w_{a,b}(\delta_a-\delta_b)(\delta_a-\delta_b)^T$, defined to realize (3.1) [as `graph Laplacian`]
- [[spielman-2025-sagt/ch04-adjacency]] (p. 35): compared; $L=dI-M$ for regular graphs
- [[spielman-2025-sagt/ch05-fundamental]]: the matrix whose action is (Lψ)(a) = Σ_{b∼a}(ψ(a) − ψ(b)) (formula (3.4), used on p. 45 and, with weights, p. 47) [as `graph Laplacian`]
- [[spielman-2025-sagt/ch06-comparing]] (p. 54): $x^TL_Gx=\sum w_{u,v}(x(u)-x(v))^2$
- [[spielman-2025-sagt/ch07-cayley]] (p. 63): L=D−A; here L² is expanded in {L,J,I}
- [[spielman-2025-sagt/ch10-random]] (p. 98): L; ν₂ and λ₂ related by Lemma 10.5.1
- [[spielman-2025-sagt/ch11-walks]] (pp. 104, 109): $L=D-M=U^TWU$; its rows encode harmonic equations
- [[spielman-2025-sagt/ch12-effective]] (p. 115): here also an operator from voltages to external currents [as `graph Laplacian`]
- [[spielman-2025-sagt/ch13-random]] (p. 125): $L_G=U^TWU=B^TB$
- [[spielman-2025-sagt/ch14-approximating]] (p. 131): $L=U^TWU$, with $U$ the signed edge–vertex matrix and $W$ the edge weights [as `graph Laplacian`]
- [[spielman-2025-sagt/ch17-monotonicity]] (p. 149): $L$ with $Lv=i_{ext}$ giving voltages
- [[spielman-2025-sagt/ch19-independent]] (p. 164): Laplacian matrix $L$ with eigenvalues $0=\lambda_1\le\dots\le\lambda_n$
- [[spielman-2025-sagt/ch20-graph]] (p. 172): $x^TLx$ sums squared differences over edges (p. 172); $L=D-A$ is the standard definition, not restated on these pages
- [[spielman-2025-sagt/ch21-cheeger]] (p. 177): $z^TLz$ as the numerator of the Rayleigh quotient
- [[spielman-2025-sagt/ch22-local]] (p. 185): $L$, and normalized $N=D^{-1/2}LD^{-1/2}$
- [[spielman-2025-sagt/ch24-nodal]] (p. 200): here also with negative edge weights; $x^TMx=\sum w_{uv}(x(u)-x(v))^2$
- [[spielman-2025-sagt/ch25-second]] (p. 204): the Laplacian matrix of a graph (not defined on these pages); λ₂ is its second-smallest eigenvalue
- [[spielman-2025-sagt/ch26-planar]] (p. 211): here $L$ of a weighted graph; the base of a generalized Laplacian [as `graph Laplacian`]
- [[spielman-2025-sagt/ch27-properties]] (p. 220): $L_G$; eigenvalues $\lambda_i=d-\mu_i$ for d-regular graphs [as `graph Laplacian`]
- [[spielman-2025-sagt/ch29-expander]] (p. 236): its spectrum defines "$\epsilon$-approximates $\frac dnK_{n,n}$"
- [[spielman-2025-sagt/ch30-simple]] (p. 246): L=D−A=UᵀU
- [[spielman-2025-sagt/ch32-sparsification]] (p. 259): $L_G=\sum w_{a,b}L_{a,b}$, sum of weighted elementary edge Laplacians
- [[spielman-2025-sagt/ch33-linear]] (p. 264): $L_G=\sum w_{a,b}L_{(a,b)}$, whose normalised form is $\Pi$
- [[spielman-2025-sagt/ch34-iterative]] (p. 279): singular; solve orthogonal to the all-1s vector, so $\lambda_2$ plays the role of $\lambda_1$ [as `graph Laplacian`]
- [[spielman-2025-sagt/ch35-conjugate]] (p. 285): $L$; it sends constant vectors to zero, so it has no inverse
- [[spielman-2025-sagt/ch36-preconditioning]] (p. 291): $L_G=\sum w_{uv}(\chi_u-\chi_v)(\chi_u-\chi_v)^T$
- [[spielman-2025-sagt/ch37-augmented]] (p. 295): $L_G$; the matrix of the systems being solved
- [[spielman-2025-sagt/ch38-fast]] (p. 301): $L$ in $M=L+X$ [as `graph Laplacian`]
- [[vonluxburg-2007-spectralclustering/main]] (pp. 4–5): $L=D-W$; $f'Lf=\tfrac12\sum w_{ij}(f_i-f_j)^2$; author also uses the normalized $L_{\rm sym},L_{\rm rw}$

### control-theory

- [[astrom-2021-feedbacksystems/ch03-system-p2]] (p. 3-39): $L=D-A$; drives the consensus update [new]

## Instances that use it

- [[two-vertex-graph-laplacian]] — $L_{G_{1,2}}=\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$ derived from $(x(1)-x(2))^2$ — from [[spielman-2025-sagt/ch03-laplacian]]
- [[path-graph-laplacian]] — locality of $L$ forces degree of order $n$ — from [[spielman-2025-sagt/ch34-iterative]]
- [[complete-graph-laplacian]] — $\Pi=\frac1nL_{K_n}$ — from [[spielman-2025-sagt/ch35-conjugate]]

## Candidate bridges

- [same-math] Dirichlet energy $\|A^Tv\|^2$ ↔ graph Laplacian: the unit itself calls it the Laplacian quadratic form of the graph. — from [[boyd-2018-vmls/ch07-matrix]] (linear-algebra → other)
- [structural-analogy] diffusion on a grid (heat) ↔ graph Laplacian (canon): incidence matrix $A$ and a resistance matrix $R$ appear in the system — from [[boyd-2018-vmls/ch11-matrix]] (linear-algebra → other)
- [same-math] Dirichlet energy $\|A^Tx\|^2$ (incidence matrix) ↔ linear-algebra canon: graph Laplacian quadratic form $\sum(x_i-x_j)^2$ — both are $x^T(AA^T)x$ for the incidence matrix $A$. — from [[boyd-2018-vmls/ch15-multi]] (linear-algebra → linear-algebra)
- [same-math] Harmonic condition at non-boundary vertices ↔ graph Laplacian: weighted-Laplacian equation $(Lz)(a)=0$ off the boundary — the averaging condition is the same linear equation. — from [[spielman-2025-sagt/ch15-tutte]] (linear-algebra → other)
- [same-math] Linear case $\Phi=\tfrac12v^2/r$ ↔ graph Laplacian: quadratic form $\sum(x(a)-x(b))^2$ (the source calls it the Lecture 13 energy). — from [[spielman-2025-sagt/ch18-dynamic]] (linear-algebra → other)
- [structural-analogy] replace a clique by a sparse expander ↔ spectral sparsification: both approximate a dense graph's Laplacian by a sparse one — from [[spielman-2025-sagt/ch30-simple]] (linear-algebra → linear-algebra)
- [structural-analogy] Kirchhoff's law $A^{\mathsf T}y=0$ ↔ graph Laplacian and network flow: nullspace of the incidence transpose. — from [[strang-2023-introduction/ch04-orthogonality-p2]] (linear-algebra → other)
- [same-math] Matrix in the heat-equation example (Figure 6.8) ↔ graph Laplacian: A = [−1 1 0; 1 −2 1; 0 1 −1] is minus the Laplacian of a 3-node path graph, so du/dt = Au smooths a signal on a network. — from [[strang-2023-introduction/ch06-eigenvalues-p3]] (linear-algebra → other)
