---
id: nielsen-2020-elementary/main-p2
work: nielsen-2020-elementary
unit: "paper (part 2/2): Eqs. 133–136, §3.13, §4 Applications, §5 Conclusion, Appendices A–B, Notations"
pages: 28–56
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Dually flat spaces, KL as Bregman divergence, and applications of information geometry (Nielsen 2020, part 2)

## L0 — One line
A convex potential $F$ and its conjugate $F^*$ make a dually flat space whose canonical divergence is a Bregman divergence. The KL divergence arises this way from exponential families (reverse KL) and mixture families (forward KL). The same structure gives geometric descriptions of natural gradient, mirror descent and (within an exponential family) Chernoff information.

## L1 — The gist (≤ 120 words)
This part finishes the survey of information geometry. It asks how dually flat structure (a convex potential F and its Legendre conjugate F*) connects to familiar statistical divergences and to practical algorithms. Answer: for exponential families the log-normalizer yields the reverse KL as a Bregman divergence; for mixture families the negative entropy yields the forward KL. Applications follow: in a dually flat space natural gradient equals ordinary gradient in dual coordinates, Bregman mirror descent is natural gradient in the dual space, within an exponential family the Chernoff information is a Bregman divergence, and mixtures can be clustered with Monte Carlo generators. Appendices give f-divergence estimation and the Gaussian family formulas.

**Prerequisites:** convex functions and the Legendre–Fenchel conjugate; gradients and Jacobians; exponential families and KL divergence; Fisher information; basic Riemannian ideas (metric tensor, connection) from part 1.

## L2 — Key ideas (5–10 bullets)
- Given a strictly convex smooth potential $F$, its Legendre–Fenchel conjugate $F^*$ (dual coordinates $\eta=\nabla F(\theta)$) gives the Hessian metrics $\nabla^2F(\theta)$, $\nabla^2F^*(\eta)$ and a pair of dual connections with $\Gamma(\theta)=0$, $\Gamma^*(\eta)=0$, i.e. a dually flat structure. Conversely, two dually flat connections determine canonical potentials $F,F^*$ (p. 28).
- Using the log-normalizer $\log\int\exp(\theta^\top t(x))\,d\mu$ of an exponential family as $F$, the Bregman divergence $B_F(\theta:\theta')=F(\theta)-F(\theta')-\langle\theta-\theta',\nabla F(\theta')\rangle$ (the canonical divergence) is the reverse KL ($D_{\mathrm{KL}^*}[p_{\theta_1}:p_{\theta_2}]=D_{\mathrm{KL}}[p_{\theta_2}:p_{\theta_1}]$). With negative Shannon entropy of a mixture family as $F$, it is the forward KL (pp. 29–31).
- Natural gradient $g^{-1}\nabla L$ ($g$ the Riemannian metric, $\nabla L$ the ordinary gradient of the loss) is invariant under reparameterization and approximates Riemannian gradient descent. In a dually flat space it equals the ordinary gradient in dual coordinates (Properties 5, 7; pp. 34–35).
- Bregman mirror descent on $(M,\nabla^2F(\theta))$ is natural gradient descent on the dual Hessian manifold; the step is taken in the dual (mirror) space (Property 6; p. 35).
- For two members of one exponential family, the Chernoff information $C=-\log\min_\alpha\int p_1^\alpha p_2^{1-\alpha}$ (the quantity tied to the best exponent of a two-hypothesis test) equals a Bregman divergence at the optimal exponent. Geometrically, the optimal point is where the e-geodesic (the exponential-family arc between the two distributions) meets the m-bisector (a set given by a linear equation in $\eta$, Eq. 199) (Thm 10; p. 37).
- The KL between mixtures with prescribed components is a Bregman divergence, but its generator (negative entropy) is in general not available in closed form (except, e.g., for components with pairwise disjoint supports). A Monte Carlo generator $\tilde F_S$ (a sampled approximation of $F$) gives tractable dually flat spaces for Bregman $k$-means (p. 39).
- Distances and divergences relate subtly: squared Riemannian distances are divergences, powers of divergences may or may not be metrics, and Fisher–Rao and Wasserstein geometries of location-scale families differ (pp. 40–41).
- Appendix A repairs the possibly negative Monte Carlo KL estimator by using the "extended" $f$-divergence. Appendix B lists all coordinate systems and the KL for the multivariate Gaussian (pp. 44–47).

## L3 — Walkthrough

### End of the preceding section — $\rho,\tau$-metric (Eqs. 133–136, p. 28)
The unit begins with equations for the $(\rho,\tau)$ metric (as printed; their setup is not on these pages):

$$ {}^{\rho,\tau}g_{ij}(\theta)=\int(\partial_i\rho(p_\theta(x)))(\partial_j\tau(p_\theta(x)))\,d\nu(x) \tag{133}$$
$$=\int\rho'(p_\theta)\tau'(p_\theta)(\partial_ip_\theta)(\partial_jp_\theta)\,d\nu \tag{134}$$
$$=\int f''(\rho(p_\theta))(\partial_i\rho(p_\theta))(\partial_j\rho(p_\theta))\,d\nu \tag{135}$$
$$=\int (f^*)''(\tau(p_\theta))(\partial_i\tau(p_\theta))(\partial_j\tau(p_\theta))\,d\nu \tag{136}$$
(p. 28).

### 3.13 Dually flat spaces and canonical Bregman divergences (pp. 28–31)
**Setting.** From a strictly convex smooth $F$ one builds a Hessian structure with metric $\nabla^2F(\theta)$. The conjugate $F^*(\eta)$ gives the dual Hessian metric $\nabla^2F^*(\eta)$. The dual connections have Christoffel symbols $\Gamma(\theta)=0$ and $\Gamma^*(\eta)=0$, so they are flat (p. 28). Conversely, it "can be proved [8]" that two dually flat connections let one reconstruct canonical potentials with $\eta=\nabla F(\theta)$, $\theta=\nabla F^*(\eta)$. The canonical divergence $A_{F,F^*}$ gives the dual Bregman divergences $B_F$, $B_{F^*}$ (p. 28).

**Mahalanobis case.** The only symmetric Bregman divergences are squared Mahalanobis distances $M_Q^2$ (p. 28), with
$$M_Q(\theta,\theta')=\sqrt{(\theta'-\theta)^\top Q(\theta'-\theta)}.\tag{137}$$
For $Q=LL^\top\succ0$ (Cholesky), with $\Delta\theta=\theta'-\theta$, $M_Q$ is Euclidean distance after an affine map:
$$M_Q^2=\Delta\theta^\top Q\Delta\theta=\Delta\theta^\top LL^\top\Delta\theta=M_I^2(L^\top\theta,L^\top\theta')=\|L^\top\theta-L^\top\theta'\|^2.\tag{138–140}$$
$M_Q^2$ violates the triangle inequality, but $M_Q$ is a metric (p. 28). Conversion between two Mahalanobis distances, with $Q_i=L_i^\top L_i$:
$$M_Q(\theta_1,\theta_2)=M_I(L^\top\theta_1,L^\top\theta_2)\iff M_I(\theta_1,\theta_2)=M_Q((L^\top)^{-1}\theta_1,(L^\top)^{-1}\theta_2),\tag{141}$$
$$M_{Q_1}(\theta_1,\theta_2)=M_I(L_1^\top\theta_1,L_1^\top\theta_2)=M_{Q_2}\big((L_2^\top)^{-1}L_1^\top\theta_1,(L_2^\top)^{-1}L_1^\top\theta_2\big).\tag{142–143}$$
Also $M_Q^2=B_F$ for $F(\theta)=\tfrac12\theta^\top Q\theta$, with $F^*(\eta)=\tfrac12\eta^\top Q^{-1}\eta$ and the dual identity
$$M_Q^2(\theta_1,\theta_2)=M^2_{Q^{-1}}(\eta_1,\eta_2).\tag{144}$$

**Integral-based generators.** When $F$ is built from an integral, the Bregman divergence can be read as a statistical distance (p. 29).

*(a) Exponential family* $\mathcal E=\{p_\theta=\exp(\theta^\top t(x)-F(\theta))\}$, order $D$, dominating measure $\mu$:
$$F(\theta)=\log\int\exp(\theta^\top t(x))\,d\mu,\qquad F^*(\eta)=-h(p_\theta)=\int p\log p\,d\mu,\tag{145–147}$$
where $h$ is Shannon entropy (p. 29). Inner product: $\eta_2(i)=E_{p_{\theta_2}}[t_i]$, and $\sum_i\theta_1(i)t_i(x)=\log p_{\theta_1}(x)+F(\theta_1)$. By linearity of expectation,
$$\theta_1^\top\eta_2=E_{p_{\theta_2}}[\log p_{\theta_1}+F(\theta_1)]=F(\theta_1)+E_{p_{\theta_2}}[\log p_{\theta_1}].\tag{148}$$
Then
$$B_{F,\mathcal E}[p_{\theta_1}:p_{\theta_2}]=F(\theta_1)+F^*(\eta_2)-\theta_1^\top\eta_2\tag{149}$$
$$=F(\theta_1)-h(p_{\theta_2})-E_{p_{\theta_2}}[\log p_{\theta_1}]-F(\theta_1)\tag{150}$$
$$=E_{p_{\theta_2}}\Big[\log\frac{p_{\theta_2}}{p_{\theta_1}}\Big]=:D_{\mathrm{KL}^*}[p_{\theta_1}:p_{\theta_2}].\tag{151}$$
Relaxing to arbitrary densities gives the reverse KL, $D_{\mathrm{KL}^*}[p_1:p_2]=E_{p_2}[\log (p_2/p_1)]=D_{\mathrm{KL}}[p_2:p_1]$ (152–153). The dual divergence $D^*[p_1:p_2]:=D[p_2:p_1]$ then returns $D_{\mathrm{KL}}[p_1:p_2]=E_{p_1}[\log(p_1/p_2)]$ (154). Summary: $D_{\mathrm{KL}}[p_{\theta_1}:p_{\theta_2}]=B_F(\theta_2:\theta_1)=A_{F,F^*}(\theta_2:\eta_1)$. The author notes this identity is easy to check directly and that here he "took the opposite direction", constructing KL from $B_F$ (p. 30).
Side remarks (p. 30): with a carrier term $k(x)$, $F^*(\eta)=-h(p_\theta)+E_{p_\theta}[k(x)]$. Because a Bregman generator is defined up to an affine term, $F(\theta)=-\log p_\theta(\omega)$ can replace the integral-based generator, which gives formulas that avoid the log-normalizer.

*Intuition note.* The log-normalizer's Bregman divergence compares two distributions of the family by an expectation under one of them. That expectation is exactly KL, with the arguments swapped.

*(b) Mixture family* $\mathcal M=\{m_\theta=\sum_{i=1}^D\theta_ip_i+(1-\sum_i\theta_i)p_0\}$, with $p_0,\dots,p_D$ linearly independent densities (155). Generator $F(\theta)=-h(m_\theta)=\int m_\theta\log m_\theta\,d\mu$ (156). Then
$$\eta_i=[\nabla F(\theta)]_i=\int(p_i-p_0)\log m_\theta\,d\mu,\qquad F^*(\eta)=-\int p_0\log m_\theta\,d\mu=h^\times(p_0:m_\theta),\tag{157–158}$$
the cross-entropy of $p_0$ relative to $m_\theta$ (p. 30). Expanding $\theta_1^\top\eta_2$ (159–160) and substituting,
$$B_{F,\mathcal M}[m_{\theta_1}:m_{\theta_2}]=-h(m_{\theta_1})-\int\Big((1-\textstyle\sum_i\theta_1(i))p_0+\sum_i\theta_1(i)p_i\Big)\log m_{\theta_2}\,d\mu\tag{161–163}$$
$$=-h(m_{\theta_1})-\int m_{\theta_1}\log m_{\theta_2}\,d\mu=\int m_{\theta_1}\log\frac{m_{\theta_1}}{m_{\theta_2}}\,d\mu=D_{\mathrm{KL}}[m_{\theta_1}:m_{\theta_2}]\tag{164–166}$$
(p. 31). So $D_{\mathrm{KL}}[m_{\theta_1}:m_{\theta_2}]=B_F(\theta_1:\theta_2)$: the forward KL. The entropy of a mixture is in general not closed-form (log-of-sum term), except for components with pairwise disjoint supports (including Dirac mixtures, i.e. categorical distributions) (p. 31).

**Cones.** Dually flat spaces can be built from any strictly convex $C^3$ $F$. Vinberg and Koszul [120] gave such a generator for homogeneous cones: for a cone $\mathcal C$, the dual cone is $\mathcal C^*=\{\omega\in V^*:\forall v\in\mathcal C,\omega(v)\ge0\}$ (167). The characteristic function is $\chi_{\mathcal C}(\theta)=\int_{\mathcal C^*}\exp(-\omega(\theta))\,d\omega$ (168). The function $\log\chi_{\mathcal C}$ is a Bregman generator inducing a Hessian structure and a dually flat space (p. 31). Fig. 10 (p. 32) is a diagram of how the main information manifolds relate.

### 4 Applications — overview (p. 31)
The author lists uses in statistics (asymptotic inference, EM and em, ARMA), machine learning (RBMs, natural gradient), signal processing (PCA, ICA, NMF), mathematical programming (barrier functions of interior-point methods) and game theory (score functions). He then describes a few.

### 4.1 Natural gradient in Riemannian space (pp. 33–36)
**4.1.1 Vanilla gradient descent.** To minimize $L_\theta(\theta)$ on $\Theta\subset\mathbb R^D$:
$$\mathrm{GD}:\ \theta_{t+1}=\theta_t-\alpha_t\nabla_\theta L_\theta(\theta_t),\tag{169}$$
with step size $\alpha_t>0$. After a differentiable bijective reparameterization $\eta=\eta(\theta)$ with $L_\eta(\eta):=L_\theta(\theta(\eta))$ (171), the rule becomes $\eta_{t+1}=\eta_t-\alpha_t\nabla_\eta L_\eta(\eta_t)$ (170). In general the two sequences differ and may reach different stationary points, since usually $\eta(\theta)\ne\theta$. Example: minimizing a temperature function in Celsius may give a different result than in Fahrenheit. GD is therefore "extrinsic": it ignores the geometry of $\Theta$ (p. 33). The natural gradient chooses the steepest direction intrinsically, with respect to a Riemannian metric on the parameter manifold (p. 33).

**4.1.2 Natural gradient and Riemannian gradient.** On a Riemannian space $(M,g)$ the Riemannian gradient uses the exponential map: $p_{t+1}=\exp_{p_t}(-\alpha_t\nabla_ML(p_t))$ (172), where $\nabla_ML(p):=\nabla_v\big(L(\exp_p(v))\big)|_{v=0}$ (173) and $\nabla_vL(p)=\lim_{h\to0}\frac{L(p+hv)-L(p)}{h}$ (174) (p. 33). The exponential map is often computationally intractable (it needs second-order differential equations), so one uses a retraction $R$: $\theta_{t+1}=R_{\theta_t}(-\alpha_t\nabla_\theta L_\theta(\theta_t))$ (175). The retraction $R_p(v)=p+v$ (a first-order Taylor approximation of $\exp$) gives natural gradient descent:
$$\mathrm{NG}:\ \theta_{t+1}=\theta_t-\alpha_tg_\theta^{-1}(\theta_t)\nabla_\theta L_\theta(\theta_t),\tag{176}$$
$${}^{\rm NG}\nabla L_\theta(\theta):=g_\theta^{-1}(\theta)\nabla_\theta L_\theta(\theta),\qquad\theta_{t+1}=\theta_t-\alpha_t{}^{\rm NG}\nabla L_\theta(\theta_t).\tag{177–178}$$
(added step) Shapes: $\theta,\nabla L\in\mathbb R^D$, $g_\theta\in\mathbb R^{D\times D}$. The natural gradient is a contravariant vector; the ordinary gradient is covariant. Raising an index uses $v^i=\sum_jg^{ij}v_j$ (p. 34). The natural gradient is invariant under invertible smooth reparameterization. However, the descent does not guarantee $\theta_t\in\Theta$ when $\Theta\ne\mathbb R^D$ (p. 34).
**Property 5 ([21]).** Natural gradient descent approximates intrinsic Riemannian gradient descent with a contravariant gradient induced by $g$, and the natural gradient is invariant to coordinate transformations (p. 34).

**4.1.3 Dually flat spaces: mirror descent and ordinary gradient.** On a dually flat space, $\frac{\nabla+\nabla^*}{2}={}^{LC}\nabla$. Global coordinates satisfy $\theta(\eta)=\nabla F^*(\eta)$ and $\eta(\theta)=\nabla F(\theta)$, with metrics $g_\theta=\nabla^2F(\theta)$ and $g^*_\eta=\nabla^2F^*(\eta)$. Crouzeix's identity gives $g_\theta(\theta)g_\eta(\eta)=I$ ($D\times D$) (p. 34). A proximal gradient scheme with proximity function $\Phi$:
$$\mathrm{PGD}:\ \theta_{t+1}=\arg\min_{\theta\in\Theta}\Big\{\langle\theta,\nabla L_\theta(\theta_t)\rangle+\frac1{\alpha_t}\Phi(\theta,\theta_t)\Big\}.\tag{179}$$
With $\Phi=\tfrac12\|\theta-\theta_t\|^2$ it is ordinary GD (p. 34). With $\Phi=B_F$ it is mirror descent:
$$\mathrm{MD}:\ \theta_{t+1}=\arg\min_{\theta\in\Theta}\Big\{\langle\theta,\nabla L(\theta_t)\rangle+\frac1{\alpha_t}B_F(\theta:\theta_t)\Big\}.\tag{180}$$
**Property 6 ([112]).** Bregman mirror descent on the Hessian manifold $(M,g=\nabla^2F(\theta))$ is equivalent to natural gradient descent on the dual Hessian manifold $(M,g^*=\nabla^2F^*(\eta))$ (p. 35). The resulting update is
$$\eta_{t+1}=\eta_t-\alpha_t(g^*_\eta)^{-1}(\eta_t)\nabla_\eta L_\eta(\eta_t),\qquad g^*_\eta=\nabla^2F^*(\eta)=(\nabla^2_\theta F(\theta))^{-1}.\tag{181–182}$$
It is called mirror descent because the step is made in the dual space $H=\{\nabla F(\theta)\}$. This fixes the covariant/contravariant mismatch of subtracting a covariant vector from a contravariant one in Eq. 169 (p. 35).

**Property 7 ([137]).** In a dually flat space induced by $F$, ${}^{\rm NG}\nabla L_\theta(\theta)=\nabla_\eta L_\eta(\eta)$, with $\eta=\nabla_\theta F(\theta)$ and $L_\eta(\eta)=L_\theta(\theta(\eta))$.
*Proof* (p. 35). $g_\theta=\nabla^2F(\theta)=\nabla_\theta\nabla_\theta F=\nabla_\theta\eta$ (the Jacobian, $D\times D$). The chain rule gives
$$\nabla_\theta L_\theta(\theta)=(\nabla_\theta\eta)(\nabla_\eta L_\eta(\eta)).\tag{183}$$
Hence ${}^{\rm NG}\nabla L_\theta=g_\theta^{-1}\nabla_\theta L_\theta=(\nabla_\theta\eta)^{-1}(\nabla_\theta\eta)\nabla_\eta L_\eta=\nabla_\eta L_\eta$ (184–186). ∎ So natural gradient descent on $L_\theta$ is ordinary gradient descent on the dually parameterized loss.

*Intuition note.* In a dually flat space, the metric is just the Jacobian between the two coordinate systems. The natural gradient therefore undoes the change of coordinates, and plain gradient descent in the dual coordinates is already "natural".

**4.1.4 Natural Evolution Strategies (NES).** To minimize a black-box $f(x)$, $x\in\mathbb X\subset\mathbb R^d$, Berny [18] relaxes the problem to $\min_{\lambda\in\Lambda}E_{p_\lambda}[f(x)]$ (187), with $J(\lambda)=E_{p_\lambda}[f]$. This is useful when $\mathbb X$ is discrete: combinatorial optimization becomes continuous optimization (pp. 35–36). The search gradient is estimated by the log-likelihood trick, with $x_1,\dots,x_n\sim p_\lambda$:
$$\widetilde\nabla J(\lambda)=\frac1n\sum_if(x_i)\nabla\log p_\lambda(x_i)\approx\nabla J(\lambda).\tag{188}$$
The Fisher information matrix is approximated by the empirical FIM
$$\tilde I(\lambda)=\frac1n\sum_i\nabla_\lambda l_\lambda(x_i)(\nabla_\lambda l_\lambda(x_i))^\top\approx I(\lambda),\quad l_\lambda=\log p_\lambda.\tag{189}$$
$\tilde I$ may be degenerate and may not respect the structure of the true FIM. Example: for $N(\mu,\sigma^2)$, $\nabla_\mu l=\frac{x-\mu}{\sigma^2}$ and $\nabla_{\sigma^2}l=\frac{(x-\mu)^2}{2\sigma^4}-\frac1{2\sigma^2}$. The expected FIM is $\mathrm{diag}(\frac1{\sigma^2},\frac1{2\sigma^4})$, but off-diagonal entries of $\tilde I$ are close to but usually non-zero. One may therefore sample until off-diagonal entries are below a prescribed $\epsilon>0$. For multivariate normals: $\nabla_\mu l=\Sigma^{-1}(x-\mu)$, $\nabla_\Sigma l=\tfrac12(\nabla_\mu l\,\nabla_\mu l^\top-\Sigma^{-1})$ (p. 36).

### 4.2 Illustrating applications of dually flat manifolds (p. 36)
For a general divergence neither $(\mathcal E,D)$ nor $(\mathcal M,D)$ is dually flat. With $D=\mathrm{KL}$ one gets dually flat spaces where primal and dual geodesics are straight lines in the global affine coordinates (p. 36).

### 4.3 Hypothesis testing in $(\mathcal E,\mathrm{KL}^*)$ (pp. 36–38)
**Problem.** Classify iid observations $X_{1:n}$ as drawn from $P_0\sim p_0$ or $P_1\sim p_1$. Fig. 11 shows the unavoidable error of any decision rule; the MAP rule picks the class with maximum likelihood (p. 36). Assume both lie in one exponential family $\mathcal E$ with the dually flat structure $(\mathcal E,{}_{\mathcal E}g,{}_{\mathcal E}\nabla^e,{}_{\mathcal E}\nabla^m)$. The expected $\alpha$-geometry of $\mathcal E$ with cumulant function $F$ is
$$g_{ij}=\partial_i\partial_jF(\theta),\qquad\Gamma^\alpha_{ij,k}=\frac{1-\alpha}2\partial_i\partial_j\partial_kF(\theta).\tag{190–191}$$
For $\alpha=1$, $\Gamma^1_{ij,k}=0$, so $\nabla^1$ is flat, and by the fundamental theorem so is $\nabla^{-1}$ (p. 37). The $\pm1$ structure equals the divergence structure of reverse KL: $(\mathcal E,{}_{\mathcal E}g,{}_{\mathcal E}\nabla^e,{}_{\mathcal E}\nabla^m)\equiv(\mathcal E,\mathrm{KL}^*)$ (192), and
$$\mathrm{KL}^*[P_{\theta'}:P_\theta]=\mathrm{KL}[P_\theta:P_{\theta'}]=B_F(\theta':\theta).\tag{193}$$
**Chernoff information.** The best exponent error $\alpha^*$ of the MAP rule is found, in the author's words, by minimizing the Bhattacharyya distance to get the Chernoff information; in Eq. 194 the minimization over $\alpha$ acts on the integral inside the log:
$$C[P_1,P_2]=-\log\min_{\alpha\in(0,1)}\int p_1^\alpha p_2^{1-\alpha}\,d\mu\ \ge0.\tag{194}$$
On $\mathcal E$ the Bhattacharyya distance $B_\alpha[p_1:p_2]=-\log\int p_1^\alpha p_2^{1-\alpha}d\mu$ (195) is a skew Jensen (Burbea–Rao) divergence:
$$J_F^\alpha(\theta_1:\theta_2)=\alpha F(\theta_1)+(1-\alpha)F(\theta_2)-F(\theta_1+(1-\alpha)\theta_2).\tag{196}$$
(Printed this way; see Reading notes.)
**Theorem 10 (Chernoff information, [73]).** For two distributions in the same exponential family,
$$C[P_{\theta_1}:P_{\theta_2}]=B(\theta_1:\theta_{12}^{\alpha^*})=B(\theta_2:\theta_{12}^{\alpha^*}),\tag{197}$$
where $\theta_{12}^\alpha=(1-\alpha)\theta_1+\alpha\theta_2$ and $\alpha^*$ is the best exponent (p. 37). Geometrically,
$$P^*=P_{\theta_{12}^*}=G_e(P_1,P_2)\cap\mathrm{Bi}_m(P_1,P_2),\tag{198}$$
where $G_e$ is the exponential geodesic and $\mathrm{Bi}_m$ the m-bisector
$$\mathrm{Bi}_m(P_1,P_2)=\{P:F(\theta_1)-F(\theta_2)+\eta(P)^\top(\theta_2-\theta_1)=0\}.\tag{199}$$
Fig. 12 shows the e-geodesic crossing the m-bisector at $P_{\theta^*_{12}}$ (pp. 37–38). For $n$ distributions $P_1,\dots,P_n\in\mathcal E$ (reference [72]), one checks the exponential arcs between natural neighbours (sharing Voronoi subfaces) of a Bregman Voronoi diagram (Fig. 13; pp. 37–38).

*Intuition note.* The Chernoff information is the "Bregman distance" from each hypothesis to a single point on the exponential arc between them (Eq. 197). That point lies on the m-bisector, which is given by a linear equation in $\eta$ (Eq. 199), so it is found by intersecting a curve and a hyperplane-like set.

### 4.4 Clustering mixtures in $(\mathcal M,\mathrm{KL})$ (pp. 39–40)
Given $k$ prescribed densities $p_0,\dots,p_{k-1}$ with the same support, the mixture family of order $D=k-1$ is
$$\mathcal M=\Big\{m(x;\theta)=\sum_{i=1}^{k-1}\theta_ip_i+\Big(1-\sum_i\theta_i\Big)p_0:\ \theta_i>0,\ \sum_i\theta_i<1\Big\}.\tag{200}$$
Fig. 14 shows $D=2$ mixtures of Laplacian, Gaussian and Cauchy components; with Gaussian components one gets a $w$-GMM. The manifold $(\mathcal M,{}_{\mathcal M}g,{}_{\mathcal M}\nabla^m,{}_{\mathcal M}\nabla^e)$ is dually flat and equivalent to $(\mathcal M_\Theta,\mathrm{KL})$:
$$\mathrm{KL}[m_{\theta_1}:m_{\theta_2}]=B_F(\theta_1:\theta_2),\quad F(\theta)=-h(m_\theta).\tag{201}$$
$F$ is the negative differential entropy of a mixture and has no closed form [95]. The author replaces it by Monte Carlo generators $\tilde F_S$ (for an iid sample $S$). Nested samples $S_1\subset\dots\subset S_m$ give tractable dually flat manifolds with $\lim_{m\to\infty}(\mathcal M,\tilde F_{S_m})=(\mathcal M,F)$, where convergence is with respect to the canonical Bregman divergence. For a given $S$, all computations in $(\mathcal M,\tilde F_S)$ are consistent [93]. Bregman $k$-means can then cluster $w$-GMMs (Fig. 15, $k=2$) (p. 39). The author recaps the two applications: $(\mathcal E,\mathrm{KL}^*)$ and $(\mathcal M,\mathrm{KL})$. Two further dually flat structures on the simplex $\Delta_D$ are in Amari's book [8]: conformal deformation of $\alpha$-geometry and $\chi$-escort geometry (p. 40).

### 5.1 Summary (pp. 40–41)
The information manifold $(M,g,\nabla,\nabla^*)$ is a pair of conjugate connections coupled with $g$, giving metric-preserving dual parallel transport. The pipeline to a one-parameter family is
$$(M,g,\nabla,\nabla^*)\Rightarrow(M,g,C)\Rightarrow(M,g,\alpha C)\Rightarrow(M,g,\nabla^{-\alpha},\nabla^{\alpha}),\ \forall\alpha\in\mathbb R.\tag{202}$$
The author emphasizes the dualistic, non-Riemannian view derived from any divergence, not tied to statistics (e.g. mathematical programming). Remarks (pp. 40–41):
- For any symmetric divergence (e.g. a symmetrized $f$-divergence such as squared Hellinger), the induced conjugate connections coincide with Levi-Civita. Yet the Fisher–Rao distance does not coincide with the squared Hellinger divergence.
- A Riemannian metric distance is never a divergence (rooted distance functions are not smooth at the extremities). A squared Riemannian distance is always a divergence.
- Powering a divergence, $D^\delta$ with $\delta>0$, may yield a metric (e.g. the square root of Jensen–Shannon) but need not; the powered Jeffreys divergence $J^\delta$ is never a metric ([127], p. 889 of that reference).
- Optimal transport between two members of one elliptically-contoured family has the same distance formula even though their KL divergences differ [40]. The Fisher–Rao manifold of location-scale families is hyperbolic; the Wasserstein manifold of location-scale families has positive curvature [40,125].
- Similarity and dissimilarity convert by $S=\exp(-D)\in(0,1]$, $D=-\log S\in[0,\infty)$ (203–204). If $D$ satisfies the additive triangle inequality, $S(p,q)S(q,r)\le S(p,r)$. A metric transform $T$ makes $T(D)$ a metric when $D$ is. The map $T(u)=\frac{u}{1+u}$ bounds an unbounded metric (printed as $T(u)=\frac1{1+u}$ followed by $\frac{D}{1+D}$; see Reading notes). $u\mapsto u^2$ is not a metric transform (squared Euclidean is not a metric).

### 5.2 Historical review (pp. 41–42)
- Hotelling [53] first considered, in the late 1920s, the Fisher information matrix as a Riemannian metric on a parametric family. His notes for a 1929 meeting were read by a colleague. He mentioned that location-scale families give Riemannian manifolds of constant non-positive curvature (p. 41).
- Rao [111] (1945) independently studied this modelling (it also contains the Cramér–Rao bound and Rao–Blackwellization). Jeffreys [55] proposed the normalized volume element as an invariant prior. The early papers did not justify using the Fisher matrix as metric, beyond its being positive definite for regular identifiable models (p. 41).
- Chentsov, in the 1960s, studied statistical decision rules with induced $\alpha$-geometries and dually flat manifolds. The Fisher metric is the unique metric (up to scale) giving invariance under Markov morphisms (pp. 41–42).
- Amari [4,5] developed the dual nature and coined "information geometry" in 1985. He was influenced by Efron's statistical curvature [41] (p. 42). Dual transport compatible with the metric is due to Norden [100] and Sen [116–118]; dual connections were also studied in affine differential geometry [99] (p. 42).

Table of structures (p. 42): $(M,g)$ Riemannian; $(\mathcal P,{}_{\mathcal P}g)$ Fisher–Riemannian; $(\mathcal P,{}_{\mathcal P}g,{}_{\mathcal P}^e\nabla^\alpha)$ Chentsov; $(M,g,\nabla,\nabla^*)$ Amari's dualistic manifold; $(M,g,C)$ Lauritzen's statistical manifold; $(M,{}^Dg,{}^D\nabla,{}^{D^*}\nabla)$ Eguchi's conjugate connection manifold induced by $D$; $(M,{}^Fg,{}^FC)$ the dually flat manifold induced by $F$.

### 5.3 Perspectives (pp. 42–44)
The author recommends [25,8] (and [48] for infinite-dimensional models). He did not report coefficients for common parametric models; information geometry also covers non-parametric and quantum settings. An information manifold $(M,D)$ can be built from any divergence. Beyond the Bregman/Csiszár/Jensen classes (which overlap), there are conformal and projective divergences; Fig. 16 shows the relationships (p. 42–43). Acknowledgments follow (p. 44).

### Appendix A — Monte Carlo estimation of $f$-divergences (pp. 44–45)
For a convex generator $f$, strictly convex at 1 with $f(1)=0$:
$$I_f(P:Q)=\int p\,f\!\Big(\frac qp\Big)d\mu,\tag{205}$$
with conventions $0f(0/0)=0$, $f(0)=\lim_{u\to0^+}f(u)$, $0f(a/0)=a\lim_{u\to\infty}f(u)/u$ (206). For $f(u)=-\log u$ this is $D_{\mathrm{KL}}(p:q)=\int p\log\frac pq\,d\mu$ (207). Monte Carlo with proposal $r$, $x_i\sim r$:
$$\widehat{\mathrm{KL}}_n=\frac1n\sum_i\frac{p(x_i)}{r(x_i)}\log\frac{p(x_i)}{q(x_i)}\tag{208}$$
With $r=p$: $\widehat{\mathrm{KL}}_n=\frac1n\sum_i\log\frac{p(x_i)}{q(x_i)}$ (209). It is consistent under mild conditions but may be negative, because $\sum_ip(x_i)\ne1$ and $\sum_iq(x_i)\ne1$ (p. 44).

**Definition 7 (extended $f$-divergence).**
$$I_f^e(p:q)=\int p\Big(f\Big(\frac qp\Big)-f'(1)\Big(\frac qp-1\Big)\Big)d\mu.\tag{210}$$
Derivation (p. 45). The scalar Bregman divergence $B_f(a:b)=f(a)-f(b)-(a-b)f'(b)\ge0$ (211). Setting $a=q/p$, $b=1$ and using $f(1)=0$:
$$f\Big(\frac qp\Big)-\Big(\frac qp-1\Big)f'(1)\ge0.\tag{212}$$
So $I_f^e(p:q)=\int p\,B_f(\tfrac qp:1)\,d\mu\ge0$ (213–214). The estimator with $x_i\sim p$ is
$$\hat I_{f,n}=\frac1n\sum_i\Big[f\Big(\frac{q(x_i)}{p(x_i)}\Big)-f'(1)\Big(\frac{q(x_i)}{p(x_i)}-1\Big)\Big]\ge0.\tag{215}$$
(The text says "importance sampling … with respect to $r$" but samples from $p$; see Reading notes.) For KL:
$$\widehat{\mathrm{KL}}_n=\frac1n\sum_i\Big(\log\frac{p(x_i)}{q(x_i)}+\frac{q(x_i)}{p(x_i)}-1\Big)\ge0,\tag{216}$$
since $D_{\mathrm{KL}^e}(p:q)=\int(p\log\frac pq+q-p)\,d\mu$ (217). Eq. 216 is a sum of scalar Itakura–Saito divergences, $D_{\rm IS}(a:b)=D_{\rm IS}(\tfrac ab:1)=\frac ab-\log\frac ab-1\ge0$ (218), a Bregman divergence for $f(u)=-\log u$. The extended divergence is itself an $f$-divergence for $f_e(u)=f(u)-f'(1)(u-1)$ (219), which satisfies $f_e(1)=0$ and $f_e'(1)=0$; for KL, $f^e_{\rm KL}(u)=-\log u+u-1$. Strict convexity at 1 suffices; non-smooth $f$ use $B_f(x:y)=\max_{g(y)\in\partial f(y)}\{f(x)-f(y)-(x-y)g(y)\}$ (220). Since $I_{\lambda f}=\lambda I_f$, one may impose $f''(1)=1$, giving a standard $f$-divergence with $I_f(p_\theta:p_{\theta+d\theta})=d\theta^\top I(\theta)d\theta$ as printed (p. 45).

### Appendix B — Multivariate Gaussian family (pp. 46–47)
Parameter $\lambda=(\lambda_v,\lambda_M)=(\mu,\Sigma)$, density
$$p_\lambda(x)=\frac{1}{(2\pi)^{d/2}\sqrt{|\lambda_M|}}\exp\Big(-\tfrac12(x-\lambda_v)^\top\lambda_M^{-1}(x-\lambda_v)\Big).\tag{221}$$
Compound inner product $\langle\theta,\theta'\rangle=\theta_v^\top\theta_v'+\mathrm{tr}(\theta_M'^\top\theta_M)$ (222). Canonical form $p_\theta=\exp(\langle t(x),\theta\rangle-F_\theta(\theta))$ (223), with sufficient statistic $t(x)=(x,-xx^\top)$ (225) and natural parameter (224) $\theta=(\Sigma^{-1}\mu,\,\cdot\,\Sigma^{-1})$ (the matrix part is printed as $-\tfrac12\Sigma^{-1}$ in Eq. 224 but $+\tfrac12\Sigma^{-1}$ in Eq. 230; see Reading notes). Log-normalizer:
$$F_\theta(\theta)=\tfrac12\big(d\log\pi-\log|\theta_M|+\tfrac12\theta_v^\top\theta_M^{-1}\theta_v\big),\tag{226}$$
$$F_\lambda(\lambda)=\tfrac12\big(\mu^\top\Sigma^{-1}\mu+\log|\Sigma|+d\log2\pi\big).\tag{227–228}$$
Moment parameters $\eta=E[t(x)]=\nabla F(\theta)$ (229). Conversions (230–232):
- $\theta_v=\Sigma^{-1}\mu$, $\theta_M=\tfrac12\Sigma^{-1}$; inverse $\lambda_v=\tfrac12\theta_M^{-1}\theta_v=\mu$, $\lambda_M=\tfrac12\theta_M^{-1}=\Sigma$.
- $\eta_v=\tfrac12\theta_M^{-1}\theta_v$, $\eta_M=-\tfrac12\theta_M^{-1}-\tfrac14(\theta_M^{-1}\theta_v)(\theta_M^{-1}\theta_v)^\top$; inverse $\theta_v=-(\eta_M+\eta_v\eta_v^\top)^{-1}\eta_v$, $\theta_M=-\tfrac12(\eta_M+\eta_v\eta_v^\top)^{-1}$.
- $\eta_v=\mu$, $\eta_M=-\Sigma-\mu\mu^\top$; inverse $\lambda_M=-\eta_M-\eta_v\eta_v^\top=\Sigma$.

Conjugate:
$$F^*_\eta(\eta)=-\tfrac12\big(\log(1+\eta_v^\top\eta_M^{-1}\eta_v)+\log|-\eta_M|+d(1+\log2\pi)\big),\quad\theta=\nabla F^*(\eta).\tag{233}$$
Fenchel–Young equality: $F_\theta(\theta)+F^*_\eta(\eta)-\langle\theta,\eta\rangle=0$ (234). KL between Gaussians, $\Delta_\mu=\mu_2-\mu_1$:
$$\mathrm{KL}(p_{(\mu_1,\Sigma_1)}:p_{(\mu_2,\Sigma_2)})=\tfrac12\Big\{\mathrm{tr}(\Sigma_2^{-1}\Sigma_1)+\Delta_\mu^\top\Sigma_2^{-1}\Delta_\mu+\log\frac{|\Sigma_2|}{|\Sigma_1|}-d\Big\}.\tag{235}$$
It is 0 when the two are equal ($\Delta_\mu=0$, $\mathrm{tr}(I)=d$). For $\Sigma_1=\Sigma_2=\Sigma$ it is $\tfrac12\Delta_\mu^\top\Sigma^{-1}\Delta_\mu=\tfrac12D^2_{\Sigma^{-1}}(\mu_1,\mu_2)$, half the squared Mahalanobis distance for the precision matrix (236–237). In general
$$\mathrm{KL}(p_{(\mu_1,\Sigma_1)}:p_{(\mu_2,\Sigma_2)})=B_F(\theta_2:\theta_1)=B_{F^*}(\eta_1:\eta_2),\tag{238}$$
with $B_F(\theta:\theta')=F(\theta)-F(\theta')-\langle\theta-\theta',\nabla F(\theta')\rangle$ (239) and canonical divergence $A_F(\theta_1:\eta_2)=F(\theta_1)+F^*(\eta_2)-\langle\theta_1,\eta_2\rangle=A_{F^*}(\eta_2:\theta_1)$ (240); $B_F(\theta_1:\theta_2)=A_F(\theta_1:\eta_2)$ (p. 47).

### Notations (pp. 47–49)
A glossary of symbols (Csiszár, Bregman, canonical divergences; Bhattacharyya, Jensen/Burbea–Rao, Chernoff; basis and tensor notation; $\nabla$- and $\nabla^*$-projections; $C$; $\mathcal E,\mathcal M,\Delta_D$; expected exponential/mixture connections, skewness tensor $C_{ijk}=E[\partial_il\partial_jl\partial_kl]$). Pages 49–56 are references.

## Toy example (ours)
Take the Poisson-type potential $F(\theta)=e^\theta$ (1-D). Then $\eta=F'(\theta)=e^\theta$ and $g_\theta=F''(\theta)=e^\theta$. Let the loss be $L_\theta(\theta)=(e^\theta-2)^2$, so $L_\eta(\eta)=(\eta-2)^2$.
- At $\theta=0$ ($\eta=1$): $\nabla_\theta L=2(e^0-2)e^0=-2$; $g=1$; natural gradient $=g^{-1}\nabla_\theta L=-2$. Dual side: $\nabla_\eta L_\eta=2(1-2)=-2$. Equal.
- At $\theta=\ln3$ ($\eta=3$): $\nabla_\theta L=2(3-2)\cdot3=6$; $g=3$; natural gradient $=6/3=2$. Dual side: $\nabla_\eta L_\eta=2(3-2)=2$. Equal, as Property 7 says.
- Bregman divergence from $F$: $B_F(\theta_2:\theta_1)=e^{\theta_2}-e^{\theta_1}-(\theta_2-\theta_1)e^{\theta_1}$. For $\theta_1=0$, $\theta_2=1$: $e-1-1=e-2\approx0.718$. In mean terms ($\lambda=e^\theta$: $\lambda_1=1$, $\lambda_2=e$), the standard Poisson relative-entropy formula $\lambda_1\log(\lambda_1/\lambda_2)+\lambda_2-\lambda_1=-1+e-1=e-2$. This matches the principle of §3.13 ($\mathrm{KL}[p_{\theta_1}:p_{\theta_2}]=B_F(\theta_2:\theta_1)$).

## Concepts
- [[relative-entropy-kl-divergence]] — in this unit: $D_{\mathrm{KL}}[p_1:p_2]=E_{p_1}\log(p_1/p_2)$; equals a Bregman divergence on exponential (reverse order) and mixture (same order) families (pp. 29–31).
- [[bregman-divergence]] (new) — $B_F(\theta:\theta')=F(\theta)-F(\theta')-\langle\theta-\theta',\nabla F(\theta')\rangle$ for convex $F$; squared Mahalanobis is the symmetric case (pp. 28, 47).
- [[legendre-fenchel-conjugate]] (new) — $F^*$ with $\eta=\nabla F(\theta)$, $\theta=\nabla F^*(\eta)$; Fenchel–Young equality $F+F^*-\langle\theta,\eta\rangle=0$ at dual points (pp. 28, 47).
- [[dually-flat-space]] (new) — manifold with two flat dual connections, global coordinates $\theta,\eta$, Hessian metrics $\nabla^2F$, $\nabla^2F^*$ (pp. 28, 34).
- [[natural-gradient]] (new) — $g^{-1}\nabla L$; coordinate-invariant steepest-descent direction; equals ordinary gradient in dual coordinates when dually flat (pp. 34–35).
- [[mirror-descent]] (new) — gradient step with proximity term $B_F$; equals natural gradient in the dual space (p. 35).
- [[chernoff-information]] (new) — $-\log\min_\alpha\int p_1^\alpha p_2^{1-\alpha}$; obtained by optimizing the exponent $\alpha$ in MAP testing (optimum $\alpha^*$); a Bregman divergence within an exponential family (p. 37).
- [[exponential-family-gibbs]] — $p_\theta=\exp(\theta^\top t-F(\theta))$, log-normalizer $F$ as Bregman generator (p. 29).
- [[mixture-family]] (new) — convex combinations of prescribed densities; generator $-h(m_\theta)$ (p. 30).
- [[f-divergence]] — $I_f(p:q)=\int pf(q/p)$; extended version $I_f^e$ subtracts a linear term to keep sample estimates non-negative (pp. 44–45).
- [[fisher-information]] — the metric used for Riemannian modelling; empirical FIM from scores in NES (pp. 36, 41).
- [[fisher-rao-information-geometry]] — Hotelling/Rao Riemannian modelling and Amari's dualistic extension (pp. 40–42).
- [[differential-entropy]] — $h(p)=-\int p\log p$; negative entropy of a mixture is not closed-form (pp. 29, 31, 39).
- [[cross-entropy]] — appears as the dual potential $F^*(\eta)=h^\times(p_0:m_\theta)$ for mixtures (p. 30).

## Canonical instances
- [[kl-as-bregman-exponential-family]] — reverse KL from the log-normalizer (p. 29).
- [[kl-as-bregman-mixture-family]] — forward KL from negative entropy (p. 31).
- [[multivariate-gaussian-family]] — $\lambda,\theta,\eta$ coordinates, $F$, $F^*$, KL as Bregman (pp. 46–47).
- [[natural-evolution-strategies]] — search gradient, empirical FIM, relaxation to $\min E_{p_\lambda}[f]$ (pp. 35–36).
- [[chernoff-geometry-e-geodesic-m-bisector]] — best exponent at the e-geodesic ∩ m-bisector (p. 37).
- [[w-gmm-bregman-kmeans]] — Monte Carlo generator, clustering of Gaussian mixtures (p. 39).
- [[hotelling-rao-fisher-metric]] — historical origin of Riemannian statistical geometry (p. 41).

## Bridges (candidates)
- [same-math] Natural gradient with Fisher metric ↔ machine learning: the natural-gradient update $\theta-\alpha g^{-1}\nabla L$ used in NES — the same formula, with $g$ the (empirical) FIM (pp. 34, 36).
- [same-math] KL between exponential-family members = Bregman divergence of the log-normalizer ↔ information theory: coding-cost excess (relative entropy) — same quantity (p. 29).
- [same-math] Chernoff information ↔ hypothesis testing/large deviations: the best error exponent of the MAP rule (p. 37).
- [structural-analogy] Mirror descent in the dual space ↔ optimization: gradient step in coordinates where the loss gradient has the right (covariant) type (p. 35).
- [structural-analogy] Similarity–dissimilarity map $S=e^{-D}$ ↔ probability/likelihood: additive triangle inequality becomes multiplicative (p. 41).
- [metaphor] Bregman Voronoi diagram of hypotheses ↔ decision regions in multiple hypothesis testing (p. 37).

## Questions this raises
- When is the empirical FIM in NES close enough to the true FIM that the natural-gradient direction is reliable?
- How accurate is the Monte Carlo generator $\tilde F_S$ for a given sample size, and how does it affect cluster quality?
- For which divergences $D$ is $D^\delta$ a metric, and can this be used to build metric geometry from divergences?
- Why do the Fisher–Rao and Wasserstein geometries of location-scale families have opposite curvature signs, and what does that mean for choosing between them?

## Reading notes
- This unit is part 2 of 2. It starts at Eq. 133 (p. 28), just before §3.13 (the section containing Eq. 133 is not shown on these pages) and ends at the references (p. 56). Printed page = pdf page (offset 0).
- Misprints and inconsistencies seen on the page images:
  - Eq. 196 and the notations table (p. 48) print $F(\theta_1+(1-\alpha)\theta_2)$; the argument looks like it should be $\alpha\theta_1+(1-\alpha)\theta_2$.
  - Eq. 197 gives $\theta_{12}^\alpha=(1-\alpha)\theta_1+\alpha\theta_2$, while Eq. 194 puts the exponent $\alpha$ on $p_1$.
  - Text before Eq. 144 prints "$\eta=Q^{-1}\theta$ and $\eta=Q\theta$"; for $F=\frac12\theta^\top Q\theta$ the consistent one is $\eta=Q\theta$.
  - Property 6 writes $\nabla^2F(\eta)$ for $g^*$ (should be $F^*$); $\theta(\eta)=\nabla F^*(\theta)$ after Eq. 182 should read $\nabla F^*(\eta)$.
  - Eq. 224 prints the matrix natural parameter as $-\frac12\Sigma^{-1}$, but Eqs. 225, 226, 228 and 230 are consistent only with $+\frac12\Sigma^{-1}$ (I used the latter).
  - Eq. 215 is described as importance sampling "with respect to $r$" yet uses $x_i\sim p$.
  - $T(u)=\frac1{1+u}$ on p. 41 is followed by the formula $\frac{D}{1+D}$, so $T(u)=\frac{u}{1+u}$ is presumably meant.
  - The $f$-divergence local expansion $d\theta^\top I(\theta)d\theta$ (p. 45) is printed without a ½ factor; check against part 1.
  - Eq. 191 and the notations table (p. 49) use different sign conventions for $\alpha$.
  - $Q$ is $LL^\top$ in Eqs. 137–140 but $L^\top L$ in the proof of Eqs. 141–143, which still use $L^\top\theta$; the two conventions are not reconciled (p. 28).
  - $h(p)=-\int p\log p$ on p. 29, but $h(p)=\int p\log p$ (called negative entropy) on p. 39.
  - By Eq. 218, a summand of Eq. 216 equals $D_{\mathrm{IS}}(q(x_i):p(x_i))$, not $D_{\mathrm{IS}}(p(x_i):q(x_i))$ as written (p. 45).
  - Several sentences are incomplete (p. 33 first paragraph; "$p_{\theta_1}$ and $p_{\theta_1}$" on p. 29–30).
- Figures 10–16 are diagrams; Fig. 10 is rotated. The reference list (pp. 49–56) is not digested.
