---
id: nielsen-2020-elementary/main-p1
work: nielsen-2020-elementary
unit: paper (part 1/2) — §§1–3 up to eq. (132) in §3.12
pages: 1–27
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# An elementary introduction to information geometry (part 1: §§1–3)

## L0 — One line
Information geometry treats a family of probability models as a curved space (a manifold) with a metric and two coupled "dual" connections, built from a divergence or from exponential/mixture families.

## L1 — The gist (≤ 120 words)
How can families of probability models be studied with differential geometry? The survey builds a manifold (a space that locally looks like $\mathbb R^D$) carrying a metric (local lengths and angles) and two coupled connections (rules that transport vectors and define "straight" curves). Such pairs arise from a divergence (a possibly asymmetric dissimilarity) or from exponential and mixture families; convex potentials give dually flat spaces. Statistical invariance is discussed: the Fisher metric is stated to be the unique invariant metric (up to scale) under Markov embeddings (embeddings of a simplex of distributions into a larger one), and f-divergences the only invariant separable divergences. Proofs are omitted (abstract). This part ends mid-§3.12.

**Prerequisites:** partial derivatives; matrices, inverses, Jacobians; convex functions; expectation and covariance; Gaussian density; KL divergence; vector spaces (linear independence, basis).

## L2 — Key ideas
- **Two independent structures.** A manifold carries a metric $g$ (lengths, angles in each tangent plane) and an affine connection $\nabla$ (compares vectors at nearby points; gives parallel transport, geodesics, curvature, torsion) (p. 3).
- **Riemannian geometry is a special case.** The metric alone fixes one connection that is torsion-free (symmetric: $\Gamma^k_{ij}=\Gamma^k_{ji}$, p. 8) and metric-compatible (parallel transport keeps lengths and angles, p. 9), the Levi-Civita connection (Theorem 1, p. 10). A Riemannian manifold is the self-dual case $\nabla=\nabla^*={}^{LC}\nabla$ (p. 10).
- **Conjugate connections.** $\nabla^*$ is conjugate to $\nabla$ w.r.t. $g$ when $X\langle Y,Z\rangle=\langle\nabla_XY,Z\rangle+\langle Y,\nabla^*_XZ\rangle$ for all vector fields, identity (35). Each $\nabla$ has a unique conjugate, and $(\nabla+\nabla^*)/2$ is Levi-Civita (pp. 11–12). The cubic tensor $C$ (the difference $\Gamma-\Gamma^*$ of the two connections' Christoffel symbols, eq. (42)) then yields a one-parameter family of $\alpha$-connections (pp. 12–13).
- **Dual curvature.** If a torsion-free $\nabla$ has constant curvature $\kappa$, its torsion-free conjugate $\nabla^*$ has the same constant curvature (Theorem 3). Corollary 2 states that $\nabla$ is flat iff $\nabla^*$ is flat (p. 13).
- **Sources of conjugate pairs.** A divergence induces $(g,\nabla,\nabla^*)$ (Theorem 4, p. 14). A Bregman divergence $B_F(\theta:\theta')=F(\theta)-F(\theta')-(\theta-\theta')^\top\nabla F(\theta')$ of a strictly convex potential $F$ gives a dually flat manifold (both connections flat) with Legendre dual coordinates ($\theta$ and $\eta=\nabla F(\theta)$) and dual Pythagorean identities (pp. 14–16).
- **Parametric families.** The Fisher information matrix ($E[\partial_il\,\partial_jl]$, $l$ the log-likelihood) gives the metric. The exponential and mixture connections are dual, and for exponential and mixture families they are flat (pp. 18–22).
- **Statistical invariance.** The Fisher metric is the unique metric invariant under Markov embeddings, up to scale (Theorem 8). f-divergences are the only invariant separable divergences when $D>1$ (p. 23).
- **Fisher–Rao distance.** It is the geodesic distance of $(\mathcal P,{}_{\mathcal P}g)$, the Riemannian structure from the Fisher metric (pp. 25–26). The Fisher matrix does not depend on the $\alpha$-representation of the densities (p. 27).

## L3 — Walkthrough

### 1 Introduction (pp. 1–3)
**1.1 Overview (pp. 1–2).** Information theory studies communication of messages over noisy channels. By analogy, the author defines "information sciences" as the fields studying "communication" between noisy data and families of models given as prior knowledge (p. 1). Information geometry (IG) is defined by Amari as "a method of exploring the world of information by means of modern geometry" (p. 1). A narrower definition is the geometry of decision making. Model fitting counts as choosing a parameter from a parametric family $M=\{m_\theta\}$ (Fig. 1). This follows Wald, who treated statistical problems as decision problems (pp. 1–2). Dissimilarities measure goodness-of-fit (likelihood, classifier losses, objectives) and also the discrepancy between models (p. 2).
Why geometry? It studies invariance of figures in a coordinate-free way, and equivariance. Examples: the centroid of a triangle satisfies $c(A.T)=A.c(T)$ for affine $A$. The MLE is equivariant under a monotonic reparameterization $g$: the MLE of $g(\theta)$ is $g(\hat\theta)$ (p. 2).

**1.2 Outline (pp. 2–3).** §2 reviews differential geometry and the Levi-Civita theorem. §3 gives dualistic structures, from divergences and from parametric families. §3 also treats invariance, stating that the Fisher metric is the unique invariant metric up to scale and that f-divergences are the unique separable invariant divergences (p. 2). Part 3 of the survey (§4: natural gradient, Chernoff information, mixture clustering), §5 and the appendices belong to the next part (p. 3).

### 2 Basics of differential geometry (pp. 3–10)
**2.1 Overview (pp. 3–4).** A smooth $D$-dimensional manifold $M$ is a topological space that locally behaves like $\mathbb R^D$. Objects on $M$ are coordinate-free but can be computed in a chart $(\mathcal U_i,x_i)$ of an atlas (p. 3). In IG one usually uses a single chart covering the manifold (p. 3). At each point $p$ the tangent plane $T_p$ best linearizes $M$. Two independent structures can be put on $M$: a metric tensor $g$ and an affine connection $\nabla$ (p. 3). $g$ makes each $T_p$ an inner-product space. $\nabla$ defines the covariant derivative $\nabla_XY$, parallel transport, $\nabla$-geodesics (autoparallel curves, generalizing straight lines), and curvature and torsion (pp. 3–4).

**2.2 Metric tensor fields (pp. 4–5).** The tangent bundle is
$$TM:=\cup_pT_p=\{(p,v),\ p\in M,\ v\in T_p\},\tag{1}$$
of dimension $2D$ (p. 4). A tangent vector acts as a directional derivative. A vector field is a smooth cross-section of $TM$ (p. 4). In a chart, $X=\sum_iX^ie_i$ (Einstein summation) with natural basis $e_i=\partial_i$. Components $X^i$ are contravariant. The reciprocal basis $e^{*i}=\partial^i$ gives covariant components (p. 4). For any vector $v$ (pp. 4–5):
$$v^i=\langle v,e^{*i}\rangle \tag{2}$$
$$v_i=\langle v,e_i\rangle \tag{3}$$
The metric and dual metric are
$$g_{ij}:=\langle e_i,e_j\rangle \tag{4}$$
$$g^{*ij}:=\langle e^{*i},e^{*j}\rangle \tag{5}$$
and $g=\sum g_{ij}\,\mathrm dx^i\otimes \mathrm dx^j$ (6) is a 2-covariant tensor field (p. 4). With $G=[g_{ij}]$ and $G^*=[g^{*ij}]$ (both $D\times D$) one has $G^*=G^{-1}$ (p. 5), and
$$e^{*i}=\sum_j g^{*ij}e_j \tag{7}$$
$$e_i=\sum_j g_{ij}e^{*j} \tag{8}$$
$g$ is a smooth symmetric positive-definite bilinear form; $u\perp v$ iff $\langle u,v\rangle=0$; $\|u\|=\sqrt{\langle u,u\rangle}$ (p. 5). With column vectors,
$$g(u,v)=(u)_B^\top G_{x(p)}(v)_B=(u)_{B^*}^\top G^{-1}_{x(p)}(v)_{B^*},\tag{9}$$
since $G\,G^*=I$. So each $T_p$ carries the Mahalanobis distance
$$M_G(u,v)=\|u-v\|_G=\sqrt{\sum_{i,j}G_{ij}(u^i-v^i)(u^j-v^j)}.\tag{10}$$
The inner product is a scalar: $\langle u,v\rangle=\sum u^iv_i=\sum u_iv^i$ (11). A metric $g'$ is conformal to $g$ if both give the same angles:
$$\frac{g'_p(u,v)}{\sqrt{g'_p(u,u)}\sqrt{g'_p(v,v)}}=\frac{g_p(u,v)}{\sqrt{g_p(u,u)}\sqrt{g_p(v,v)}}.\tag{12}$$
The Poincaré disk model is conformal; the Klein disk model is not, except at the origin (p. 6).
*Intuition note.* The metric is a position-dependent ruler: a matrix $G$ at each point that turns two tangent vectors into a number. The reciprocal basis lets you read vector components by taking inner products.

**2.3 Affine connections (pp. 6–8).** An affine connection $\nabla$ is a differential operator giving a covariant derivative, parallel transport and geodesics, and it fully characterizes curvature and torsion (p. 6).
*2.3.1 Covariant derivative.* $\nabla:\mathfrak X(M)\times\mathfrak X(M)\to\mathfrak X(M)$ (13), written $\nabla_XY$. Prescribing $D^3$ smooth Christoffel symbols of the second kind $\Gamma^k_{ij}$ defines a unique connection:
$$\nabla_{\partial_i}\partial_j=\Gamma^k_{ij}\partial_k \tag{14}$$
$$(\nabla_XY)^k=X^i(\nabla_iY)^k=X^i\Big(\frac{\partial Y^k}{\partial x^i}+\Gamma^k_{ij}Y^j\Big)\tag{15}$$
The Christoffel symbols are not tensors, since they do not follow tensor transformation rules (p. 6).
*2.3.2 Parallel transport.* The manifold is not embedded in a Euclidean space, so vectors in different tangent planes cannot be added without a connection. $\nabla$ relates infinitesimally close tangent planes, so one can slide $v\in T_p$ along a smooth curve $c$ ($c(0)=p$, $c(1)=q$) to $v_q\in T_q$ (p. 7, Fig. 3):
$$\forall v\in T_p,\ \forall t\in[0,1],\quad v_{c(t)}=\prod_{c(0)\to c(t)}^{\nabla}v\in T_{c(t)}.\tag{16}$$
*2.3.3 Geodesics.* $\nabla$-geodesics are autoparallel curves, whose velocity stays parallel to itself (p. 7):
$$\nabla_{\dot\gamma}\dot\gamma=0.\tag{17}$$
In coordinates this is a system of second-order ODEs (the source prints it without the indices on $\dot\gamma$; I add them):
$$\ddot\gamma^k(t)+\Gamma^k_{ij}\dot\gamma^i(t)\dot\gamma^j(t)=0,\quad \gamma^l(t)=x^l\circ\gamma(t) \tag{18}$$
$$\Gamma^k_{ij}=\Gamma_{ij,l}\,g^{lk} \tag{19a}$$
$$\Gamma_{ij,k}=g_{lk}\Gamma^l_{ij} \tag{19b}$$
($\Gamma_{ij,l}$ are the symbols of the first kind; (19) is printed as one equation, p. 7). Geodesics are 1D autoparallel submanifolds. $\nabla$-hyperplanes are autoparallel submanifolds of dimension $D-1$. The geodesic equation can be posed as an initial value problem ($\gamma(0)=p$, $\dot\gamma(0)=v$) or a boundary value problem ($\gamma(0)=p$, $\gamma(1)=q$) (p. 7).
*2.3.4 Curvature and torsion.* The connection defines a curvature tensor $R$, a $(1,3)$-tensor with components $R^i_{jkl}$ (p. 7). The coordinate-free formula is
$$R(X,Y)Z:=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z \tag{20}$$
with Lie bracket $[X,Y](f)=X(Y(f))-Y(X(f))$. (Page 7 prints "$\nabla_X\nabla_YX$" for the first term; I write the evidently intended $Z$.) In coordinates $R(\partial_j,\partial_k)\partial_i=R^l_{jki}\partial_l$ (21). Informally, curvature measures the non-commutativity of covariant derivatives. For the Levi-Civita connection it is the Riemann–Christoffel tensor (p. 8).
A manifold is $\nabla$-flat when $R=0$. This holds in particular if some coordinate system makes all $\Gamma^k_{ij}=0$. That vanishing is coordinate-dependent: it happens in rectangular but not polar coordinates of the plane (p. 8, fn. 5). A connection is torsion-free iff it is symmetric:
$$\nabla_XY-\nabla_YX=[X,Y],\quad\text{i.e. }\Gamma^k_{ij}=\Gamma^k_{ji}\tag{22}$$
The torsion tensor, a $(1,2)$-tensor, is
$$T(X,Y):=\nabla_XY-\nabla_YX-[X,Y].\tag{23}$$
For a torsion-free connection the Bianchi identities hold:
$$R(X,Y)Z+R(Z,X)Y+R(Y,Z)X=0 \tag{24}$$
$$(\nabla_VR)(X,Y)Z+(\nabla_XR)(Y,V)Z+(\nabla_YR)(V,X)Z=0 \tag{25}$$
Parallel transport is in general path-dependent. The angle defect of a vector transported round an infinitesimal loop is related to curvature. For a flat connection, parallel transport does not depend on the path (p. 8). Fig. 4 contrasts the sphere (curved) and the cylinder (flat). Footnote 6 notes that Gaussian curvature is the product of the minimal and maximal sectional curvatures; for a cylinder $\kappa_{\min}=0$, so it is 0 (p. 8). The text says an affine connection is a torsion-free linear connection (p. 8). Fig. 5 summarizes concepts induced by $\nabla$ and $g$ (p. 9).

**2.4 Fundamental theorem of Riemannian geometry (pp. 9–10).** $\nabla$ is metric-compatible with $g$ if, for all vector fields,
$$X\langle Y,Z\rangle=\langle\nabla_XY,Z\rangle+\langle Y,\nabla_XZ\rangle \tag{26}$$
(equivalently (27) with $g$; in coordinates)
$$\partial_kg_{ij}=\langle\nabla_{\partial_k}\partial_i,\partial_j\rangle+\langle\partial_i,\nabla_{\partial_k}\partial_j\rangle.\tag{28}$$
Then parallel transport preserves the metric, hence lengths, angles and orthogonality (p. 9):
$$\langle u,v\rangle_{c(0)}=\Big\langle\prod_{c(0)\to c(t)}^{\nabla}u,\prod_{c(0)\to c(t)}^{\nabla}v\Big\rangle_{c(t)}\quad\forall t.\tag{29}$$
**Theorem 1.** There exists a unique torsion-free affine connection compatible with the metric, the Levi-Civita connection ${}^{LC}\nabla$ (p. 10). Its Christoffel symbols are
$${}^{LC}\Gamma^k_{ij}=\tfrac12g^{kl}(\partial_ig_{jl}+\partial_jg_{il}-\partial_lg_{ij})\tag{30}$$
(the source prints the first term as $\partial_ig_{il}$, apparently a misprint). The Koszul formula (31) gives the coordinate-free version:
$$2g(\nabla_XY,Z)=X(g(Y,Z))+Y(g(X,Z))-Z(g(X,Y))+g([X,Y],Z)-g([X,Z],Y)-g([Y,Z],X).$$
Metric-compatible connections with torsion exist (e.g. the flat Weitzenböck connection). The metric determines the local structure but not the global topology: a cone and a cylinder have locally the same flat metric (p. 10).
*Intuition note.* The metric alone is enough to select one connection without torsion that keeps lengths and angles under transport. So in Riemannian geometry the metric alone gives the connection (§2.4).

**2.5 Preview: IG versus Riemannian geometry (p. 10).** IG uses a pair of conjugate connections $\nabla,\nabla^*$ (often but not necessarily torsion-free) coupled to $g$. Their dual transports preserve the metric:
$$\langle u,v\rangle_{c(0)}=\Big\langle\prod^{\nabla}_{c(0)\to c(t)}u,\prod^{\nabla^*}_{c(0)\to c(t)}v\Big\rangle_{c(t)}.\tag{32}$$
A Riemannian manifold $(M,g)$ is the self-dual case $\nabla=\nabla^*={}^{LC}\nabla$. But the information-geometric structure for a self-dual Levi-Civita pair does not induce a distance, whereas $(M,g)$ gives the geodesic length distance (p. 10):
$$D_\rho(p,q)=\int_0^1\|\gamma'(t)\|_{\gamma(t)}\mathrm dt=\int_0^1\sqrt{g_{\gamma(t)}(\dot\gamma,\dot\gamma)}\,\mathrm dt \tag{33}$$
$$=\int_0^1\sqrt{\dot\gamma(t)^\top g_{\gamma(t)}\dot\gamma(t)}\,\mathrm dt \tag{34}$$
It is also the shortest path length, $\inf_\gamma\int_0^1\|\gamma'\|\,\mathrm dt$. Usually it has no closed form (p. 10).

### 3 Information manifolds (pp. 10–27)
**3.1 Overview (pp. 10–11).** Roadmap: conjugate connection manifolds (CCMs, §3.2), statistical manifolds (§3.3), $\alpha$-families (§3.4), the fundamental theorem (§3.5), divergences (§3.6), Bregman/dually flat (§3.7), expected manifolds from parametric families (§3.9), invariance (§3.10), Fisher–Rao (§3.11). These structures are not tied to a distance a priori; they need a pair $(\nabla,\nabla^*)$ coupled to $g$ (p. 11).

**3.2 Conjugate connection manifolds (pp. 11–12).**
**Definition 1.** $\nabla^*$ is conjugate to $\nabla$ w.r.t. $g$ iff, for all smooth vector fields,
$$X\langle Y,Z\rangle=\langle\nabla_XY,Z\rangle+\langle Y,\nabla^*_XZ\rangle.\tag{35}$$
It is also written with $g$ (36) and pointwise (37). Conjugation is an involution: $(\nabla^*)^*=\nabla$ (p. 11). **Definition 2:** a CCM is $(M,g,\nabla,\nabla^*)$ with $\nabla,\nabla^*$ conjugate w.r.t. $g$ (p. 11). Dual parallel transport preserves the metric (38), and Property 1 states (39) as an if-and-only-if condition for the pair (p. 12):
$$\forall t,\ \Big\langle\prod^{\nabla}_{c(0)\to c(t)}u,\prod^{\nabla^*}_{c(0)\to c(t)}v\Big\rangle_{c(t)}=\langle u,v\rangle_{c(0)}.\tag{39}$$
**Property 2:** given $\nabla$ on $(M,g)$, there is a unique conjugate $\nabla^*$. The mean connection
$$\bar\nabla=\frac{\nabla+\nabla^*}{2}\tag{40}$$
coincides with Levi-Civita:
$$\bar\nabla={}^{LC}\nabla \tag{41}$$
(Property 3: $\bar\nabla$ is self-conjugate) (p. 12).

**3.3 Statistical manifolds (p. 12).** Lauritzen's structure is purely geometric, though a statistical model can always be found for it (cited). Define the totally symmetric cubic Amari–Chentsov tensor
$$C_{ijk}:=\Gamma^k_{ij}-\Gamma^{*k}_{ij},\tag{42}$$
$$C(X,Y,Z):=\langle\nabla_XY-\nabla^*_XY,Z\rangle \tag{43}$$
$$C_{ijk}=\langle\nabla_{\partial_i}\partial_j-\nabla^*_{\partial_i}\partial_j,\partial_k\rangle .\tag{44}$$
**Definition 3.** A statistical manifold is $(M,g,C)$ with $C$ totally symmetric cubic (p. 12).

**3.4 The $\alpha$-family (p. 13).** Since $\alpha C$ is also totally symmetric, a 1-parameter family $\{\nabla^\alpha\}$ exists with $\nabla^0=\bar\nabla={}^{LC}\nabla$, $\nabla^1=\nabla$, $\nabla^{-1}=\nabla^*$. As printed:
$$\Gamma^\alpha_{ij,k}=\Gamma^0_{ij,k}-\tfrac\alpha2C_{ij,k}\tag{45}$$
$$\Gamma^{-\alpha}_{ij,k}=\Gamma^0_{ij,k}+\tfrac\alpha2C_{ij,k}\tag{46}$$
$$g(\nabla^\alpha_XY,Z)=g({}^{LC}\nabla_XY,Z)+\tfrac\alpha2C(X,Y,Z)\tag{47}$$
(the signs of (45) and (47) differ as printed; see Reading notes).
**Theorem 2.** For any $\alpha\in\mathbb R$, $(M,g,\nabla^{-\alpha},\nabla^\alpha=(\nabla^{-\alpha})^*)$ is a CCM. Also, directly from a conjugate pair:
$$\Gamma^\alpha_{ij,k}=\frac{1+\alpha}2\Gamma_{ij,k}+\frac{1-\alpha}2\Gamma^*_{ij,k}.\tag{48}$$

**3.5 Fundamental theorem of IG (p. 13).**
**Theorem 3 (dually constant curvature).** If a torsion-free affine connection $\nabla$ has constant curvature $\kappa$, then its conjugate torsion-free connection $\nabla^*$ necessarily has the same constant curvature $\kappa$ (proof cited: [25], Prop. 8.1.4). A statistical manifold is $\alpha$-flat if its $\alpha$-connection is flat; it "can be shown" that $R^\alpha=-R^{-\alpha}$. **Corollary 1:** $(M,g,\nabla^{-\alpha},\nabla^\alpha)$ is $\nabla^\alpha$-flat iff it is $\nabla^{-\alpha}$-flat. **Corollary 2:** for $\alpha=\pm1$, $\nabla$-flat iff $\nabla^*$-flat.
**Definition 4.** $(M,g,\nabla)$ has constant curvature $\kappa$ when $R^\nabla(X,Y)Z=\kappa\{g(Y,Z)X-g(X,Z)Y\}$ for all fields. It "can be proved" that
$$g\big(R^{(\alpha)}(X,Y)Z,W\big)+g\big(Z,R^{(-\alpha)}(X,Y)W\big)=0.\tag{49}$$
Hence $g(R^{\nabla^*}(X,Y)Z,W)=-g(Z,R^{\nabla}(X,Y)W)$. The author remarks that constant curvature is interesting computationally because dual geodesics then have simple closed forms (p. 13).
*Intuition note.* Curvature of $\nabla$ and of its dual are tied together. For a torsion-free $\nabla$ with constant curvature, its torsion-free conjugate has the same constant (Theorem 3), and (Corollary 2) $\nabla$ is flat iff $\nabla^*$ is flat.

**3.6 Conjugate connections from divergences (p. 14).** Notation: $\partial_{i,\cdot}$ differentiates in the first argument, $\partial_{\cdot,j}$ in the second; e.g. $\partial_{ij,k}=\partial^2_{x^ix^j}\partial_{y^k}$.
**Definition 5.** A divergence $D:M\times M\to[0,\infty)$ w.r.t. a chart $\Theta\subset\mathbb R^D$ is a $C^3$ function such that: (1) $D(\theta:\theta')\ge0$, with equality iff $\theta=\theta'$; (2) $\partial_{i,\cdot}D|_{\theta=\theta'}=\partial_{\cdot,j}D|_{\theta=\theta'}=0$; (3) $-\partial_{\cdot,i}\partial_{\cdot,j}D|_{\theta=\theta'}$ is positive-definite. The dual (reverse) divergence is
$$D^*(\theta:\theta'):=D(\theta':\theta),\tag{50}$$
an involution. The Euclidean distance is a metric but not a divergence. The squared Euclidean distance is a non-metric symmetric divergence. The Riemannian distance $D_\rho$ is never a divergence (p. 14).
**Theorem 4 (Eguchi).** $(M,{}^Dg,{}^D\nabla,{}^{D^*}\nabla)$ is an information manifold with
$${}^Dg:=-\partial_{i,j}D(\theta:\theta')|_{\theta=\theta'}={}^{D^*}g \tag{51}$$
$${}^D\Gamma_{ijk}:=-\partial_{ij,k}D(\theta:\theta')|_{\theta=\theta'}\tag{52}$$
$${}^{D^*}\Gamma_{ijk}:=-\partial_{k,ij}D(\theta:\theta')|_{\theta=\theta'}\tag{53}$$
The statistical manifold is $(M,{}^Dg,{}^DC)$ with
$${}^DC_{ijk}={}^{D^*}\Gamma_{ijk}-{}^D\Gamma_{ijk}.\tag{54}$$
A family $(M,{}^Dg,{}^D\nabla^{-\alpha},({}^D\nabla^{-\alpha})^*={}^D\nabla^\alpha)$ follows (55), and ${}^D\nabla^*={}^{D^*}\nabla$ (56) (p. 14).

**3.7 Dually flat manifolds (Bregman geometry) (pp. 14–17).** Take a strictly convex smooth potential $F(\theta)$ on an open convex $\Theta$. Its Bregman divergence is
$$B_F(\theta:\theta')=F(\theta)-F(\theta')-(\theta-\theta')^\top\nabla F(\theta').\tag{57}$$
The induced structure is
$${}^Fg:={}^{B_F}g=-[\partial_i\partial_jB_F(\theta:\theta')|_{\theta'=\theta}]=\nabla^2F(\theta) \tag{58}$$
$${}^F\Gamma:={}^{B_F}\Gamma_{ij,k}(\theta)=0 \tag{59}$$
$${}^FC_{ijk}:={}^{B_F}C_{ijk}=\partial_i\partial_j\partial_kF(\theta)\tag{60}$$
So the manifold is ${}^F\nabla$-flat. $^{LC}\nabla$ comes from ${}^Fg$ (usually not flat), and $({}^F\nabla)^*={}^F\nabla^1$ (p. 15). The Legendre–Fenchel transform gives the dual potential
$$F^*(\eta):=\sup_{\theta\in\Theta}\{\theta^\top\eta-F(\theta)\}.\tag{61}$$
**Theorem 5 (Fenchel–Moreau).** If $F$ is lower semicontinuous and convex, then $(F^*)^*=F$.
There are two global dual affine coordinate systems $\eta=\nabla F(\theta)$ and $\theta=\nabla F^*(\eta)$, so a single chart covers the manifold. The author concludes that natural parameters of an exponential family cannot live in, e.g., a spherical space (p. 15). The Crouzeix identity ($D\times D$ Hessians) is
$$\nabla^2F(\theta)\,\nabla^2F^*(\eta)=I.\tag{62}$$
It shows that $\{\partial_i\}$ and $\{\partial^j\}$ are primal and reciprocal bases. The canonical divergence (Young–Fenchel) is
$$B_F(\theta:\theta')=A_{F,F^*}(\theta:\eta')=F(\theta)+F^*(\eta')-\theta^\top\eta'=A_{F^*,F}(\eta':\theta).\tag{63}$$
The dual Bregman divergence gives
$${}^Fg^{ij}(\eta)=\partial^i\partial^jF^*(\eta),\quad\partial^l:=\tfrac{\partial}{\partial\eta_l}\tag{64}$$
$${}^F\Gamma^{*ijk}(\eta)=0,\quad {}^FC^{ijk}=\partial^i\partial^j\partial^kF^*(\eta)\tag{65}$$
So the manifold is both ${}^F\nabla$-flat and ${}^F\nabla^*$-flat: a dually flat manifold (DFM), with dual atlases in $\theta$ and $\eta$. Two points can be joined by a $\theta$-straight $\nabla$-geodesic or an $\eta$-straight $\nabla^*$-geodesic; there are $2^3=8$ types of geodesic triangles. Primal transport leaves contravariant components unchanged; dual transport leaves covariant components unchanged; both are path-independent (pp. 15–16).
*Intuition note.* A strictly convex function $F$ gives two coordinate systems, $\theta$ and $\eta=\nabla F(\theta)$. Straight lines are straight in one system for $\nabla$ and in the other for $\nabla^*$. Both connections are flat.

**Theorem 6 (dual Pythagorean identities, Fig. 6).** Two curves are orthogonal where $g(\dot\gamma_1,\dot\gamma_2)=0$ (p. 16). Then
$$\gamma^*(P,Q)\perp\gamma(Q,R)\iff(\eta(P)-\eta(Q))^\top(\theta(Q)-\theta(R))=0$$
$$\gamma(P,Q)\perp\gamma^*(Q,R)\iff(\theta(P)-\theta(Q))^\top(\eta(Q)-\eta(R))=0$$
The figure pairs these with $D(P:R)=D(P:Q)+D(Q:R)$ and the dual version for $D^*$. A submanifold $S$ is $\nabla$-flat ($\nabla^*$-flat) iff it is an affine subspace in $\theta$-($\eta$-)coordinates.
**Theorem 7 (uniqueness of projections).** The $\nabla$-projection $P_S=\arg\min_{Q\in S}D(\theta(P):\theta(Q))$ (66) is unique if $S$ is $\nabla^*$-flat. The dual $\nabla^*$-projection $P^*_S=\arg\min_{Q\in S}D(\theta(Q):\theta(P))$ (67) is unique "if $M\subseteq S$ is $\nabla$-flat", as printed (p. 16). For subsets, $D(S:S')=\min_{s\in S,s'\in S'}D(s:s')$ (68). It can be computed by alternating projections when $S$ is $\nabla$-flat and $S'$ is $\nabla^*$-flat. Kurose's Pythagorean theorem extends this to dually constant curvature (pp. 16–17).
**Bregman balls (p. 17).** $\mathrm{Ball}_F(C:r)=\{P:F(\theta(P))+F^*(\eta(C))-\langle\theta(P),\eta(C)\rangle\le r\}$ (69). Lift $\theta$ to $\hat\theta=(\theta,F(\theta))$. The lifted sphere lies on the hyperplane
$$H_{\hat\sigma}:\theta_{D+1}=\langle\theta-\theta(C),\eta(C)\rangle+F(\theta(C))+r.\tag{70}$$
A point is in the ball iff its lift lies in the halfspace $H^-_{\hat\sigma}$ containing $\hat\theta(C)$. Consequences: the intersection of $k$ Bregman balls is a $(D-k)$-dimensional Bregman ball. A Bregman sphere is determined by $D+1$ points in general position. Membership is tested by the sign of a $(D+2)\times(D+2)$ determinant (71), with sign $-1$ inside, $0$ on the sphere, $+1$ outside (72):
$$\mathrm{InBregmanBall}_F(P_1,\dots,P_{D+1};P):=\operatorname{sign}\begin{vmatrix}1&\cdots&1&1\\\theta(P_1)&\cdots&\theta(P_{D+1})&\theta(P)\\F(\theta(P_1))&\cdots&F(\theta(P_{D+1}))&F(\theta(P))\end{vmatrix}\tag{71}$$
The dual ball is $\mathrm{Ball}^*_F(C:r)=\{P:F(\theta(C))+F^*(\eta(P))-\langle\theta(C),\eta(P)\rangle\le r\}=\mathrm{Ball}_{F^*}(C:r)$ (73). **Property 4 (Bregman 4-parameter identity).** For any four points:
$$B_F(\theta(P_1):\theta(Q_1))+B_F(\theta(P_2):\theta(Q_2))-B_F(\theta(P_1):\theta(Q_2))-B_F(\theta(P_2):\theta(Q_1))-(\theta(P_2)-\theta(P_1))^\top(\eta(Q_1)-\eta(Q_2))=0.\tag{74}$$
Summary: a dually flat space needs a convex generator. It can be studied as a Hessian manifold, and also built on homogeneous cones; Fig. 7 lists generators (exponential family cumulant, mixture family negentropy, cone characteristic function) (pp. 17–18).

**3.8 Hessian $\alpha$-geometry (p. 18).**
$${}^Fg_{ij}(\theta)=\partial_i\partial_jF(\theta),\quad{}^Fg^{ij}(\eta)=\partial^i\partial^jF(\eta)\tag{75}$$
$${}^F\Gamma^\alpha_{ijk}(\theta)=\tfrac{1-\alpha}2\partial_i\partial_j\partial_kF(\theta)\tag{76a}$$
$${}^{F}\Gamma^{\alpha*}_{ijk}(\eta)={}^{F^*}\Gamma^\alpha_{ijk}(\eta)=\tfrac{1+\alpha}2\partial^i\partial^j\partial^kF^*(\eta)\tag{76b}$$
(printed as one equation (76); note that (75) prints $F$ in its second formula where $F^*$ is evidently meant). For $\alpha=\pm1$ it is dually flat (p. 18).

**3.9 Expected $\alpha$-manifolds of parametric families (pp. 18–22).** A regular parametric family $\mathcal P=\{p_\theta(x)\}_{\theta\in\Theta}$ (77), $\Theta$ open, has order $D=\dim\Theta$. Likelihood $L(\theta;x)=p_\theta(x)$, log-likelihood $l(\theta;x)=\log p_\theta(x)$ (78), score vector $s_\theta=\nabla_\theta l=(\partial_il)_i$ (79). The Fisher information matrix ($D\times D$) is
$${}_{\mathcal P}I(\theta):=E_\theta[\partial_il\,\partial_jl]_{ij}\succeq0\tag{80}$$
($\succeq$ the Löwner order; for regular models it is positive definite, $\succ0$) (p. 18). It is invariant under reparameterization of the sample space and covariant under reparameterization of $\Theta$. With $\bar p(x;\eta)=p(\theta(\eta);x)$ and Jacobian $J_{ij}=\partial\theta_i/\partial\eta_j$:
$$\bar I(\eta)=\Big[\frac{\partial\theta_i}{\partial\eta_j}\Big]^\top I(\theta(\eta))\Big[\frac{\partial\theta_i}{\partial\eta_j}\Big]\tag{81}$$
(p. 19).
**Example 1 (univariate normals).** $\mathcal N=\{p(x;\mu,\sigma)=\frac1{\sqrt{2\pi}\sigma}\exp(-\frac{(x-\mu)^2}{2\sigma^2})\}$ (82), with $\lambda=(\mu,\sigma)$ and $\lambda'=(\mu,\sigma^2)$ (p. 19). The Fisher matrices are
$$I_\lambda(\lambda)=\begin{bmatrix}1/\lambda_2^2&0\\0&2/\lambda_2^2\end{bmatrix}=\begin{bmatrix}1/\sigma^2&0\\0&2/\sigma^2\end{bmatrix}\tag{83}$$
$$I_{\lambda'}(\lambda')=\begin{bmatrix}1/\lambda_2&0\\0&1/(2\lambda_2^2)\end{bmatrix}=\begin{bmatrix}1/\sigma^2&0\\0&1/(2\sigma^4)\end{bmatrix}\tag{84}$$
(the $\lambda_2$ in (84) is the second coordinate of $\lambda'$). Covariance reads $I_{\lambda'}(\lambda')=J_{\lambda,\lambda'}^\top I_\lambda(\lambda(\lambda'))J_{\lambda,\lambda'}$ (85), with $J_{\lambda',\lambda}=\mathrm{diag}(1,2\sigma)$ (86). The check printed is
$$I_\lambda(\lambda)=\begin{bmatrix}1&0\\0&2\sigma\end{bmatrix}\begin{bmatrix}1/\sigma^2&0\\0&1/(2\sigma^4)\end{bmatrix}\begin{bmatrix}1&0\\0&2\sigma\end{bmatrix}=\begin{bmatrix}1/\sigma^2&0\\0&2/\sigma^2\end{bmatrix}\tag{87}$$
(added step: $(2\sigma)^2/(2\sigma^4)=2/\sigma^2$). The line elements are invariant: $\mathrm ds_\lambda=\mathrm ds_{\lambda'}$. If $g=J^\top J$ in some coordinates, the metric is Euclidean. The author cites that a dually flat space with a separable potential is Euclidean (p. 19).
**Cramér–Rao.** For an unbiased estimator,
$$\mathrm{Var}_\theta[\hat\theta_n(X)]\succeq\frac1n\,{}_{\mathcal P}I^{-1}(\theta).\tag{88}$$
Fig. 8 compares Fisher ellipses (red) with sample covariances of MLEs (black) over 200 runs of 100 iid samples at grid points. The Fisher ellipses are axis-parallel because the Fisher matrix is diagonal ($\mu$, $\sigma$ orthogonal). This is no longer true for the MLE sample covariances, whose centres deviate from the grid points (pp. 19–21).
**Example 2 (exponential family).**
$$\mathcal E=\Big\{p_\theta(x)=\exp\Big(\sum_{i=1}^Dt_i(x)\theta_i-F(\theta)+k(x)\Big):\theta\in\Theta\Big\}\tag{89}$$
with sufficient statistics $t(x)$, carrier measure $k$, and strictly convex cumulant function $F$ (log-normalizer). Then
$${}_{\mathcal E}I(\theta)=\mathrm{Cov}_{X\sim p_\theta}[t(x)]=\nabla^2F(\theta)=(\nabla^2F^*(\eta))^{-1}\succ0.\tag{90}$$
For $N(\mu,\Sigma)$ the Fisher matrix is block-diagonal (so $\mu$ and $\Sigma$ are orthogonal), with $\mu$-block $\sigma^{ij}$ and $\Sigma$-block (a $d\times d\times d\times d$ tensor) $\sigma^{il}\sigma^{jk}+\sigma^{ik}\sigma^{jl}$ (91). For $d=1$ it gives
$$I(\mu,\Sigma)=\begin{bmatrix}1/\sigma^2&0\\0&1/(2\sigma^4)\end{bmatrix}\tag{92}$$
(p. 21; see Reading notes on (91)–(92)).
**Example 3 (mixture family).**
$$\mathcal M=\Big\{p_\theta(x)=\sum_{i=1}^D\theta_iF_i(x)+C(x):\theta\in\Theta\Big\}\tag{93}$$
with $F_i$ linearly independent on a common support, $\int F_i\,\mathrm d\mu=0$, $\int C\,\mathrm d\mu=1$. Then
$${}_{\mathcal M}I(\theta)=E_{X\sim p_\theta}\Big[\frac{F_iF_j}{p_\theta^2}\Big]=\int_{\mathcal X}\frac{F_iF_j}{p_\theta}\mathrm d\mu\succ0.\tag{94}$$
Gaussian mixtures with prescribed components form a mixture family. The probability simplex can be modelled as either an exponential or a mixture family (pp. 21–22).
**Expected geometry (p. 22).** The Fisher metric is
$${}_{\mathcal P}g(u,v):=(u)_\theta^\top{}_{\mathcal P}I(\theta)(v)_\theta\tag{95}$$
The exponential and mixture connections have coefficients
$${}^e_{\mathcal P}\nabla:=E_\theta[(\partial_i\partial_jl)(\partial_kl)]\tag{96}$$
$${}^m_{\mathcal P}\nabla:=E_\theta[(\partial_i\partial_jl+\partial_il\,\partial_jl)(\partial_kl)]\tag{97}$$
The skewness (Amari–Chentsov) tensor is
$$C_{ijk}:=E_\theta[\partial_il\,\partial_jl\,\partial_kl].\tag{98}$$
The expected $\alpha$-manifolds are $\{(\mathcal P,{}_{\mathcal P}g,{}_{\mathcal P}\nabla^{-\alpha},{}_{\mathcal P}\nabla^{+\alpha})\}_{\alpha\in\mathbb R}$ (99), with
$${}_{\mathcal P}\Gamma^\alpha_{ij,k}(\theta):=E_\theta[\partial_i\partial_jl\,\partial_kl]+\tfrac{1-\alpha}2C_{ijk}(\theta)\tag{100}$$
$$=E_\theta\Big[\Big(\partial_i\partial_jl+\tfrac{1-\alpha}2\partial_il\,\partial_jl\Big)(\partial_kl)\Big]\tag{101}$$
The Levi-Civita connection is the mean:
$${}_{\mathcal P}\bar\nabla=\frac{{}_{\mathcal P}\nabla^{-\alpha}+{}_{\mathcal P}\nabla^\alpha}2={}^{LC}_{\mathcal P}\nabla:={}^{LC}\nabla({}_{\mathcal P}g)\tag{102}$$
The curvature tensor is
$${}_{\mathcal P}R^\alpha_{ijkl}=\partial_i\Gamma^\alpha_{jk,l}-\partial_j\Gamma^\alpha_{ik,l}+g^{rs}\big(\Gamma^\alpha_{ik,r}\Gamma^\alpha_{js,l}-\Gamma^\alpha_{jk,r}\Gamma^\alpha_{is,l}\big)\tag{103}$$
with $R^\alpha_{ijkl}=-R^{-\alpha}_{ijlk}$. The connections are coupled with the metric: $\partial_ig_{jk}=\Gamma^\alpha_{ij,k}+\Gamma^{-\alpha}_{ik,j}$. For exponential and mixture families with the dual exponential/mixture connections, all coefficients vanish, so the manifolds are dually flat (Bregman geometry):
$${}^e_{\mathcal M}\Gamma={}^m_{\mathcal M}\Gamma={}^e_{\mathcal E}\Gamma={}^m_{\mathcal E}\Gamma=0.\tag{104}$$
*Intuition note.* Fisher information is the expected product of score components, $E[\partial_il\,\partial_jl]$. For an exponential family it equals the Hessian of the log-normalizer, which is exactly the Bregman metric of §3.7. Hence the exponential-family manifold is a dually flat space.

**3.10 Criteria for statistical invariance (pp. 22–25).** Question: which metrics, connections and divergences make sense in statistics (p. 22)? Informally, an invariant metric preserves the inner product under Markov embeddings, i.e. embeddings of $\Delta_D$ into $\Delta_{D'}$ with $D'>D$ (p. 23).
**Theorem 8.** The Fisher information metric is the unique invariant metric tensor under Markov embeddings, up to a scaling constant (cited [26, 129]).
A discrete divergence has **information monotonicity** iff, for every coarse-grained partition $\mathcal A=\{A_i\}_{i=1}^E$ of $[D]$ with $E\le D$ and $\theta^i_{\mathcal A}=\sum_{j\in A_i}\theta^j$,
$$D(\theta_{\mathcal A}:\theta'_{\mathcal A})\le D(\theta:\theta')\tag{105}$$
(Fig. 9: merging bins). A divergence is separable if it is a sum of scalar divergences:
$$D(\theta_1:\theta_2):=\sum_id(\theta_1^i:\theta_2^i).\tag{106}$$
The squared Euclidean distance is separable; the Euclidean distance is not (square root). For $D>1$, the only invariant and separable (decomposable) divergences are the f-divergences, for convex generator $f$ (p. 23):
$$I_f(\theta:\theta')=\sum_{i=1}^D\theta_if\Big(\frac{\theta'_i}{\theta_i}\Big)\ge f(1),\quad f(1)=0.\tag{107}$$
"Standard" f-divergences have $f'(1)=0$ and $f''(u)=1$ as printed (scale fixed); $f_\lambda(u)=f(u)+\lambda(u-1)$ gives the same $I_f$. They are invariant under one-to-one (sufficient statistic) transformations $y=t(x)$:
$$I_f[p(x;\theta):p(x;\theta')]=\int_{\mathcal X}p(x;\theta)f\Big(\frac{p(x;\theta')}{p(x;\theta)}\Big)\mathrm d\mu(x)=I_f[q(y;\theta):q(y;\theta')].$$
(p. 23). Reference duality: $I_{f^*}[p:p']=I_f[p':p]=I_{f^\diamond}[p:p']$ (108), with $f^\diamond(u):=uf(1/u)$ (109) (p. 24). Examples (p. 24): $\alpha$-divergences
$$I_\alpha[p:q]=\frac4{1-\alpha^2}\Big(1-\int p^{\frac{1-\alpha}2}q^{\frac{1+\alpha}2}\mathrm d\mu\Big),\quad f(u)=\tfrac4{1-\alpha^2}(1-u^{\frac{1+\alpha}2})\tag{110}$$
include KL when $\alpha\to1$, with $f(u)=-\log u$ and $\mathrm{KL}[p:q]=\int p\log\frac pq\,\mathrm d\mu$ (111). They also include reverse KL when $\alpha\to-1$, with $f(u)=u\log u$ (112), and the squared Hellinger divergence ($\alpha=0$)
$$H^2[p:q]=\int(\sqrt p-\sqrt q)^2\mathrm d\mu\tag{113}$$
with $f(u)=(\sqrt u-1)^2$. Others are Pearson/Neyman $\chi^2$, Jensen–Shannon
$$\mathrm{JS}[p:q]=\tfrac12\int\Big(p\log\frac{2p}{p+q}+q\log\frac{2q}{p+q}\Big)\mathrm d\mu\tag{114}$$
and total variation
$$\mathrm{TV}[p:q]=\tfrac12\int|p-q|\,\mathrm d\mu\tag{115}$$
with $f(u)=\tfrac12|u-1|$. TV is the only metric f-divergence. By Csiszár's theorem, for $|\alpha|<1$ the $\alpha$-topology equals the TV topology; otherwise it is stronger (p. 24).
**Theorem 9.** f-divergences are invariant under diffeomorphisms $m$ of the sample space: if $Y_i=m(X_i)\sim q_i$ and $X_i\sim p_i$, then $I_f[q_1:q_2]=I_f[p_1:p_2]$ (p. 25).
**Example 4.** $X\sim\mathrm{Exponential}(\lambda)\iff Y=\sqrt X\sim\mathrm{Rayleigh}(\sigma=1/\sqrt{2\lambda})$, with $p_\lambda(x)=\lambda e^{-\lambda x}$ and $q_\sigma(x)=\frac x{\sigma^2}\exp(-\frac{x^2}{2\sigma^2})$ on $[0,\infty)$. By Theorem 9 and the Rayleigh KL, the exponential KL is
$$D_{KL}[p_{\lambda_1}:p_{\lambda_2}]=\log\frac{\lambda_1}{\lambda_2}+\frac{\lambda_2}{\lambda_1}-1.$$
(The printed intermediate lines have slips; see Reading notes.) (p. 25)
**Link to Fisher metric.** Invariant standard f-divergences are related infinitesimally to the Fisher metric:
$$I_f[p(x;\theta):p(x;\theta+\mathrm d\theta)]=\int p\,f\Big(\frac{p(x;\theta+\mathrm d\theta)}{p(x;\theta)}\Big)\mathrm d\mu\overset{\Sigma}=\tfrac12\,{}^Fg_{ij}(\theta)\mathrm d\theta^i\mathrm d\theta^j\tag{116–117}$$
A statistical divergence defines the parameter divergence ${}_{\mathcal P}D(\theta:\theta'):=D[p(x;\theta):p(x;\theta')]$ (118). For $D=I_f$, the induced $\pm1$ connections are exactly the expected $\pm\alpha$-connections with
$$\alpha=2f'''(1)+3\tag{119}$$
So the invariant connections that coincide with those of invariant divergences are the expected $\alpha$-connections. Their curvature depends on both $\alpha$ and the model (p. 25).

**3.11 Fisher–Rao expected Riemannian manifolds (p. 26).** Historically, a first modelling used the Fisher matrix as Riemannian metric:
$${}_{\mathcal P}I(\theta):=E_{p_\theta}[\partial_il\,\partial_jl]\tag{120}$$
which, under regularity conditions, equals
$${}_{\mathcal P}I(\theta)=-E_{p_\theta}[\partial_i\partial_jl].\tag{121}$$
The Fisher–Rao distance is the geodesic distance, with $\gamma(0)=\theta_1$, $\gamma(1)=\theta_2$:
$$D_\rho(p_{\theta_1},p_{\theta_2})=\int_0^1\sqrt{\dot\gamma(t)^\top g_{\gamma(t)}\dot\gamma(t)}\,\mathrm dt\tag{122}$$
It is also $\inf_\gamma$ of the path length. **Definition 6:** the Fisher–Rao distance is the geodesic metric distance of $(\mathcal P,{}_{\mathcal P}g)$. Examples: categorical distributions give spherical geometry; bivariate location-scale families give hyperbolic geometry; location families give Euclidean geometry. Line element $\mathrm ds^2=g_{ij}\mathrm dx^i\mathrm dx^j$. The structure was proposed by Hotelling (handwritten note of 1929) and independently by Rao (1945); Jeffreys (1946) proposed the volume element as an invariant prior. $(\mathcal P,{}_{\mathcal P}g)$ coincides with the self-dual CCM induced by a symmetric f-divergence such as squared Hellinger. The exponential map $\exp_p(v)$ maps $v\in T_p$ back to $M$ when well-defined and parameterizes geodesics $t\mapsto\exp_p(tv)$ (p. 26).

**3.12 Monotone $\alpha$-embeddings and gauge freedom (pp. 26–27; unit ends mid-section).** An equivalent expression of the Fisher matrix, said to be well-suited to prove that it is positive semi-definite, is
$$I_{ij}(\theta):=4\int\partial_i\sqrt{p(x;\theta)}\,\partial_j\sqrt{p(x;\theta)}\,\mathrm d\mu(x).\tag{123}$$
Define the $\alpha$-representation $l^\alpha(x;\theta):=k_\alpha(p(x;\theta))$ with
$$k_\alpha(u)=\begin{cases}\frac2{1-\alpha}u^{\frac{1-\alpha}2}&\alpha\ne1\\\log u&\alpha=1\end{cases}\tag{124}$$
and the $\alpha$-FIM
$$I^\alpha_{ij}(\theta):=\int\partial_il^\alpha(x;\theta)\,\partial_jl^{-\alpha}(x;\theta)\,\mathrm d\mu(x),\tag{125}$$
which expands as printed to
$$I^\alpha_{ij}=\begin{cases}\frac1{1-\alpha^2}\int\partial_ip^{\frac{1-\alpha}2}\partial_jp^{\frac{1+\alpha}2}\mathrm d\mu&\alpha\ne\pm1\\\int\partial_i\log p\,\partial_jp\,\mathrm d\mu&\alpha\in\{-1,1\}\end{cases}\tag{126}$$
The 1-representation is the e- (logarithmic) representation, the $-1$-representation the m- (mixture), the 0-representation the square-root representation. The $\alpha$-scores $\{\partial_il^\alpha\}$ are tangent basis vectors; "thus the FIM is $\alpha$-independent" (p. 27). Under mild conditions
$$I^\alpha_{ij}=-\frac2{1+\alpha}\int p^{\frac{1+\alpha}2}\partial_i\partial_jl^\alpha\,\mathrm d\mu\tag{127}$$
$$\partial_i\partial_jl^\alpha=p^{\frac{1-\alpha}2}\Big(\partial_i\partial_jl+\tfrac{1-\alpha}2\partial_il\,\partial_jl\Big)\tag{128}$$
$$I^\alpha_{ij}=-\frac2{1+\alpha}\Big(-I_{ij}+\tfrac{1-\alpha}2I_{ij}\Big)=I_{ij}\tag{129}$$
(added step: $\int p^{\frac{1+\alpha}2}p^{\frac{1-\alpha}2}\partial_i\partial_jl\,\mathrm d\mu=E[\partial_i\partial_jl]=-I_{ij}$ and $\int p\,\partial_il\,\partial_jl\,\mathrm d\mu=I_{ij}$). For $\alpha=1$: $I^1_{ij}=-E[\nabla^2\log p(x;\theta)]$ (130). For an exponential family with cumulant $F$: $I(\theta)=\nabla^2F(\theta)$ (131). Zhang's "representation/reference biduality" was confounded in $\alpha$-geometry. Gauge freedom is studied via $(\rho,\tau)$-monotone embeddings: $\rho,\tau$ strictly increasing, $f$ strictly convex with $f'(\rho(u))=\tau(u)$, the set of such functions forming a group under composition. The $(\rho,\tau)$-metric ${}^{\rho,\tau}g(\theta)=[{}^{\rho,\tau}g_{ij}(\theta)]_{ij}$ derives from
$$D_{\rho,\tau}(p:q)=\int\big(f(\rho(p(x)))+f^*(\tau(q(x)))-\rho(p(x))\tau(q(x))\big)\mathrm d\nu(x).\tag{132}$$
The page ends here (p. 27).

## Toy example (ours, not from the text)
**Setting:** the Bregman divergence (57) and the dual Pythagorean identity (Theorem 6).

*Asymmetry.* Take $F(\theta)=\log(1+e^\theta)$, so $F'(\theta)=\eta=e^\theta/(1+e^\theta)$. Let $\theta=0$ and $\theta'=\ln3$. Then $F(0)=\ln2=0.6931$, $F(\ln3)=\ln4=1.3863$, $\eta(0)=1/2$, $\eta'=3/4$.
- $B_F(0:\ln3)=\ln2-\ln4-(0-\ln3)(3/4)=-0.6931+0.8240=0.1308$.
- $B_F(\ln3:0)=\ln4-\ln2-(\ln3-0)(1/2)=0.6931-0.5493=0.1438$.

The two differ, so $B_F$ is not symmetric. Check with (63): $F^*(3/4)=\theta'\eta'-F(\theta')=0.8240-1.3863=-0.5623$, and $F(0)+F^*(3/4)-0\cdot\tfrac34=0.6931-0.5623=0.1308$ ✓.

*Pythagoras.* Take $F(\theta)=\tfrac12\theta^\top A\theta$ with $A=\begin{bmatrix}2&1\\1&1\end{bmatrix}$. Then $\eta=A\theta$ and $B_F(\theta:\theta')=\tfrac12(\theta-\theta')^\top A(\theta-\theta')$. Let $\theta_Q=(0,0)$, $\theta_P=(1,0)$, $\theta_R=(1,-2)$.
- Orthogonality in (Theorem 6): $(\theta_P-\theta_Q)^\top A(\theta_Q-\theta_R)=(2,1)\cdot(-1,2)=-2+2=0$ ✓.
- $B(P{:}Q)=\tfrac12(1,0)A(1,0)^\top=\tfrac12\cdot2=1$.
- $B(Q{:}R)$: $A\theta_R=(0,-1)$, $\theta_R\cdot(0,-1)=2$, so $B=1$.
- $B(P{:}R)$: $\theta_P-\theta_R=(0,2)$, $A(0,2)=(2,2)$, dot $=4$, so $B=2=1+1$ ✓.

## Concepts
- [[metric-tensor]] (new) — smooth symmetric positive-definite bilinear form on tangent planes; $G^*=G^{-1}$ (pp. 4–5)
- [[affine-connection]] (new) — operator giving covariant derivative, parallel transport, geodesics; set by Christoffel symbols (p. 6)
- [[curvature-torsion]] (new) — $R$ measures non-commuting derivatives; torsion-free iff symmetric $\Gamma$ (pp. 7–8)
- [[levi-civita-connection]] (new) — unique torsion-free metric-compatible connection (Theorem 1, p. 10)
- [[conjugate-connections]] (new) — $\nabla,\nabla^*$ satisfying (35); dual transport preserves $g$ (p. 11)
- [[statistical-manifold]] (new) — $(M,g,C)$ with totally symmetric cubic tensor $C$ (p. 12)
- [[alpha-connection]] (new) — one-parameter family from $C$ or from a conjugate pair (pp. 12–13)
- [[divergence-parameter]] (new) — $C^3$ possibly asymmetric dissimilarity with Def. 5 properties (p. 14)
- [[bregman-divergence]] (new) — $B_F$ of a strictly convex potential, eq. (57) (p. 14)
- [[dually-flat-manifold]] (new) — both $\nabla$ and $\nabla^*$ flat, dual affine coordinates $\theta,\eta$ (p. 15)
- [[legendre-fenchel-transform]] (new) — $F^*(\eta)=\sup_\theta\{\theta^\top\eta-F(\theta)\}$ (p. 15)
- [[mixture-family]] (new) — densities linear in $\theta$, eq. (93) (p. 21)
- [[information-monotonicity]] (new) — divergence does not increase under coarse-graining (p. 23)
- [[markov-embedding]] (new) — embedding of $\Delta_D$ in $\Delta_{D'}$; invariance criterion for metrics (p. 23)
- [[f-divergence]] — $I_f=\sum\theta_if(\theta'_i/\theta_i)$; invariant and separable (pp. 23–24)
- [[relative-entropy-kl-divergence]] — the $\alpha\to1$ member of the $\alpha$-divergences (p. 24)
- [[fisher-information]] — $E[\partial_il\,\partial_jl]$, equal to $-E[\partial_i\partial_jl]$ under regularity (pp. 18, 26)
- [[fisher-rao-metric-information-geometry]] — Fisher metric and its geodesic distance (p. 26)
- [[exponential-family]] — canonical density (89), Fisher matrix $=\nabla^2F$; dually flat with mixture connection (pp. 21–22)

## Canonical instances
- [[normal-family-fisher]] — Fisher matrices of $N(\mu,\sigma)$ in two parameterizations, covariance (81)–(87) (p. 19)
- [[cramer-rao-simulation]] — MLE covariances versus Fisher ellipses, Fig. 8 (pp. 19–21)
- [[exponential-rayleigh-kl]] — KL invariant under $x\mapsto\sqrt x$ (p. 25)
- [[categorical-sphere]] — Fisher–Rao geometry of categorical distributions is spherical (p. 26)
- [[coarse-graining-simplex]] — merging bins illustrates monotonicity, Fig. 9 (p. 23)
- [[sphere-cylinder-transport]] — parallel transport on curved vs flat surfaces, Fig. 4 (p. 8)

## Bridges (candidates)
- [same-math] $\alpha\to1$ member of the $\alpha$-divergences ↔ information-theory: relative entropy / KL divergence — eq. (111) is the KL integral
- [same-math] Fisher information of an exponential family $=\nabla^2F=\mathrm{Cov}[t]$ ↔ information-theory: exponential family / Gibbs distribution — $F$ is the log-normalizer
- [same-math] $I_f$ at nearby parameters $\approx\tfrac12g_{ij}\mathrm d\theta^i\mathrm d\theta^j$ ↔ information-theory: Fisher information as local second-order form of KL — eq. (116–117)
- [structural-analogy] Information monotonicity under coarse-graining ↔ information-theory: data processing inequality — both say processing cannot raise divergence, but the source treats only bin merging
- [structural-analogy] Dual Pythagorean identity (Theorem 6) ↔ information-theory: Pythagorean-type identities for projections — same shape (projection as divergence minimization, Thm 7), not derived here
- [metaphor] Wald's "inference as decision" (§1.1) ↔ information-theory: rate–distortion, choosing a representation under a dissimilarity

## Questions this raises
- Which models are dually flat only because the exponential/mixture connections are chosen, and what is lost for $\alpha\ne\pm1$ (curvature depends on $\alpha$ and on the model, p. 25)?
- Why do conjugate-connection structures carry no distance a priori (pp. 10–11), and what replaces the geodesic distance in applications?
- What does the missing proof of Theorem 8 rely on, and is invariance under Markov embeddings really the same demand as information monotonicity?
- How does the (ρ,τ) gauge freedom at the end of §3.12 change the metric, and what does it give beyond the $\alpha$-representations?

## Reading notes
- Printed page numbers equal pdf numbers (offset 0). Unit starts at §1 (p. 1) and ends at p. 27, mid-§3.12 right after eq. (132). §3.12's remainder, §4, §5, appendices and the notation summary (p. 47) belong to part 2.
- The text layer is badly garbled on equations; I used the images.
- Misprints or oddities seen on the pages: (30) prints $\partial_ig_{il}$ where $\partial_ig_{jl}$ is evidently meant (corrected above). (18) prints $\ddot\gamma+\Gamma^k_{ij}\dot\gamma\dot\gamma$ without indices. (20) prints $\nabla_X\nabla_YX$ for $\nabla_X\nabla_YZ$.
- Sign inconsistency: (45) uses $-\tfrac\alpha2C$ while (47) uses $+\tfrac\alpha2C$. With $C=\Gamma-\Gamma^*$ from (42) and $\nabla^1=\nabla$, (47) agrees with (48) and (45) does not.
- Theorem 7, second part: printed condition "$M\subseteq S$ is $\nabla$-flat"; probably $S\subseteq M$ is meant. I did not change the statement.
- (91) at $d=1$ gives $2/\sigma^4$ for the $\Sigma$-entry, which does not match $1/(2\sigma^4)$ in (92). A normalizing factor seems to be missing; I did not resolve it.
- (126): the integrand with prefactor $\frac1{1-\alpha^2}$ equals $\tfrac14$ of the Fisher integrand (computed as $\partial_ip^{a}\partial_jp^{b}=ab\,\partial_ip\,\partial_jp/p$ with $ab=(1-\alpha^2)/4$); a prefactor $\frac4{1-\alpha^2}$ would match (123).
- Example 4: the printed first line $\log(\lambda_2^2/\lambda_1^2)$ and the "$-1/\lambda_2$" in the second line do not follow from $\sigma^2=1/(2\lambda)$. The final result $\log(\lambda_1/\lambda_2)+\lambda_2/\lambda_1-1$ is the correct KL between exponentials. A consistent chain (added step): $\log\frac{\sigma_2^2}{\sigma_1^2}=\log\frac{\lambda_1}{\lambda_2}$ and $\frac{\sigma_1^2-\sigma_2^2}{\sigma_2^2}=\frac{\lambda_2}{\lambda_1}-1$.
- (106) prints $d(\theta_1^i:\theta_2^j)$; I wrote $\theta_2^i$. In (107) the text prints "$f''(u)=1$" (presumably at $u=1$).
- The text says "an affine connection is a torsion-free linear connection" (p. 8), but p. 10 allows pairs "often but not necessarily torsion-free".
- The p. 19 text (not the Fig. 8 caption, which reads "black") prints "back ellipses" (for "black"). Minor typos: p. 17 has an unclosed parenthesis at "Cauchy manifolds [79],"; p. 11 reads ("on submanifold a").
