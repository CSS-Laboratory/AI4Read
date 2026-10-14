---
id: murphy-2023-pml2/ch18-gaussian-p2
work: murphy-2023-pml2
unit: "18 Gaussian processes (part 2/2)"
pages: 704-733
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 19
pipeline_version: 0.1
---
# Gaussian processes, part 2: non-Gaussian likelihoods (end), scaling, kernel learning, GPs and DNNs, forecasting

## L0 — One line
Exact GP inference costs $O(N^3)$, but inducing points, variational bounds, matrix-vector methods and state-space forms scale it up, while the kernel itself can be learned from data (by marginal likelihood, search, spectral mixtures, deep features) and relates to infinitely wide neural networks.

## L1 — The gist (≤ 120 words)
This part asks how to use GPs when data are large, the likelihood is non-Gaussian, or the right kernel is unknown. Scaling methods approximate the prior (Nyström, SOR/DTC/FITC), approximate the posterior variationally (SVGP), or avoid Cholesky by fast matrix-vector products (CG, KISS-GP), or use a state-space form for 1-d inputs. Kernel learning uses the marginal likelihood (a point estimate, or a posterior over hyperparameters), additive or compositional kernels, spectral mixtures and deep kernels. Infinitely wide one-hidden-layer networks give GP kernels (NN-GP), and training dynamics give the NTK. A forecasting example (Mauna Loa) closes the chapter.

**Prerequisites:** Gaussian conditioning; GP regression and the Gram matrix; Cholesky cost; KL divergence and ELBO; matrix inversion lemma; basic MCMC and neural-net notation.

## L2 — Key ideas
- Poisson GP: $f=\log r\sim\mathrm{GP}$ regularises noisy small counts by sharing information between neighbouring cells (p. 704).
- Subset-of-data and the Nyström approximation $K\approx K_{\cdot Z}K_{ZZ}^{-1}K_{Z\cdot}$ cut cost: subset-of-data to $O(M^3)$, Nyström to $O(M^3+NM^2)$, which is linear in $N$ (pp. 705–707).
- Inducing-point methods differ in which conditional is made deterministic or factorised (SOR, DTC, FITC). SOR is degenerate and can underestimate variance; FITC avoids some of this (pp. 708–710).
- SVGP keeps the model but approximates the posterior with $q(f_Z)$. Inducing points are then variational parameters, and the collapsed bound has an extra trace term that prevents overfitting (pp. 710–713).
- Matrix-vector (Krylov/CG/Lanczos) methods can exploit kernel structure when present and parallelise easily on GPUs; KISS and SKIP impose structure to make the matrix-vector products fast. Exact GPs on a data subset can beat approximate GPs on full data (pp. 714–716).
- The log marginal likelihood trades data fit against complexity, is non-convex, and its point estimate can be overconfident. A posterior over hyperparameters can help overcome this overconfidence (pp. 717–720).
- Kernel learning is the GP form of representation learning: additive kernels, BIC-guided compositional search, spectral mixture kernels and deep kernels (pp. 717, 721–728).
- An infinitely wide one-hidden-layer MLP with Gaussian priors is a GP (NN-GP). The NTK describes training dynamics (pp. 729–731).

## L3 — Walkthrough

### 18.4.3 (end) Poisson regression with a GP (pp. 704–705)
- Fig. 18.10 compares posterior predictive distributions for GP Poisson regression from MCMC and from SVI (p. 704). The variational GP posterior $p(f\mid X,y)$ is Gaussian, with a point estimate for the kernel parameters (p. 704).
- **Disease mapping.** Data: heart attacks in Finland, 1996–2000, in $20\text{km}\times20\text{km}$ cells. Likelihood $y_n\sim\mathrm{Poi}(e_nr_n)$, with $e_n$ the known expected deaths and $r_n$ the relative risk to infer. Counts are small, so the prior is $f\triangleq\log r\sim\mathrm{GP}(0,\mathcal K)$ with a Matérn $\nu=3/2$ kernel, length scale and magnitude estimated from data (p. 704).
- Fig. 18.11 (Laplace approximation, 911 data points): posterior mean relative risk is higher in eastern Finland, consistent with other studies. Posterior variance is higher in the north, where fewer people live (pp. 704–705).

### 18.4.4 Other likelihoods (p. 704)
Many others are possible. A Student-$t$ likelihood gives robust regression. A general variational method for non-conjugate likelihoods is in [WSS21].

### 18.5 Scaling GP inference (pp. 704–705)
Cholesky of the $N\times N$ Gram matrix costs $O(N^3)$. Table 18.3 gives costs for the log marginal likelihood ($M$ inducing points, $B$ minibatch size, $D$ input dimension, $C$ CG iterations, $L$ Lanczos iterations):

| Method | Cost |
|---|---|
| Cholesky | $O(N^3)$ |
| Conj. grad. | $O(CN^2)$ |
| Inducing | $O(NM^2+M^3+DNM)$ |
| Variational | $O(NM^2+M^3+DNM)$ |
| SVGP | $O(BM^2+M^3+DNM)$ |
| KISS-GP | $O(CN+CDM^D\log M)$ |
| SKIP | $O(DLN+DLM\log M+L^3N\log D+CL^2N)$ |

### 18.5.1 Subset of data (pp. 705–706)
- Keep $M$ examples, so exact inference costs $O(M^3)$ (p. 705). Choices: random subset, clustering, or coreset methods that provably find an information-preserving subset (pp. 705–706).
- **18.5.1.1 Informative vector machine.** Clustering and coresets ignore the labels $y_i$. The IVM greedily adds the labelled example that maximally reduces posterior entropy of $f_j$: $\Delta_j=\mathbb H(p(f_j))-\mathbb H(p^{\rm new}(f_j))$ (p. 706). With $p(f_j)=\mathcal N(\mu_j,v_j)$ and $p(f_j\mid y_j)\propto p(f_j)\mathcal N(y_j\mid f_j,\sigma^2)=\mathcal N(\mu_j^{\rm new},v_j^{\rm new})$:
$$ (v_j^{\rm new})^{-1}=v_j^{-1}+\sigma^{-2},\qquad \mathbb H(\mathcal N(\mu,v))=\tfrac12\log(2\pi e v)\Rightarrow \Delta_j=\tfrac12\log(1+v_j/\sigma^2).$$
(added step: $\Delta_j=\tfrac12\log(v_j/v_j^{\rm new})$.) $\Delta_j$ is monotonic in $v_j$, so pick the site with the largest variance (p. 706). Entropy is submodular, so submodular optimisation can improve on the IVM [Kra+08] (p. 706).
- **18.5.1.2 Discussion.** The weakness is that ignored data can reduce accuracy and increase uncertainty. Other methods compress the data instead (p. 706).

*Intuition note.* Throwing data away is cheap but wasteful. Choosing the point where the model is most uncertain is a greedy way to lose as little as possible.

### 18.5.2 Nyström approximation (pp. 706–707)
- Suppose a rank-$M$ form $K_{X,X}\approx U\Lambda U^{\mathsf T}$ (18.106), with $\Lambda$ the $M$ leading eigenvalues and $U$ the $N\times M$ eigenvectors. Then, as printed (p. 706; see Reading notes):
$$K_\sigma^{-1}=(K_{X,X}+\sigma^2I_N)^{-1}\approx\sigma^{-2}I_N+\sigma^{-2}U(\sigma^2\Lambda^{-1}+U^{\mathsf T}U)^{-1}U^{\mathsf T}\tag{18.107}$$
$$|K_\sigma|\approx|\Lambda|\,|\sigma^2\Lambda^{-1}+U^{\mathsf T}U|\tag{18.108}$$
Both take $O(NM^2)$. A full eigendecomposition is $O(N^3)$, so it does not help (p. 706).
- Instead pick a subset $Z$ of $M<N$ points, ordered first, and partition
$$K_{X,X}=\begin{pmatrix}K_{Z,Z}&K_{Z,\tilde X}\\K_{\tilde X,Z}&K_{\tilde X,\tilde X}\end{pmatrix},\quad \tilde X=X-Z\tag{18.109}$$
Eigendecompose $K_{Z,Z}$ (eigenpairs $\lambda_i,u_i$). Scale so that $\|\tilde u_i\|\approx1$ (p. 707):
$$\tilde\lambda_i\triangleq\tfrac NM\lambda_i\ (18.110),\qquad \tilde u_i\triangleq\sqrt{\tfrac MN}\tfrac1{\lambda_i}K_{\tilde X,Z}u_i\ (18.111)$$
$$K_{X,X}\approx\sum_{i=1}^M\tilde\lambda_i\tilde u_i\tilde u_i^{\mathsf T}\tag{18.112}$$
$$=\sum_i\tfrac NM\lambda_i\sqrt{\tfrac MN}\tfrac1{\lambda_i}K_{\tilde X,Z}u_i\ \sqrt{\tfrac MN}\tfrac1{\lambda_i}u_i^{\mathsf T}K_{\tilde X,Z}^{\mathsf T}\tag{18.113}$$
$$=K_{\tilde X,Z}\Big(\sum_i\tfrac1{\lambda_i}u_iu_i^{\mathsf T}\Big)K_{\tilde X,Z}^{\mathsf T}\tag{18.114}$$
$$=K_{\tilde X,Z}K_{Z,Z}^{-1}K_{\tilde X,Z}^{\mathsf T}\tag{18.115}$$
This is the **Nyström approximation**. Define $Q_{A,B}\triangleq K_{A,Z}K_{Z,Z}^{-1}K_{Z,B}$ (18.116); the approximate Gram matrix is $Q_{X,X}$, and $K_\sigma$ is replaced by $\hat Q_{X,X}=Q_{X,X}+\sigma^2I_N$. The eigendecomposition costs $O(M^3)$ and $\hat Q^{-1}_{X,X}$ costs $O(NM^2)$, so the cost is linear in $N$ (p. 707).
- Caution: approximating only $\hat K_{X,X}$ in $\mu_{*|X}$ (18.52) and $\Sigma_{*|X}$ (18.53), while leaving other kernel evaluations exact, is inconsistent and can give negative predictive variance. One solution is to use the same $Q$ everywhere (p. 707).

*Intuition note.* A few chosen points summarise the whole Gram matrix as a low-rank matrix. The approximation is exact on rows and columns of $Z$ and uses a "bridge" through $Z$ elsewhere.

### 18.5.3 Inducing point methods (pp. 707–711)
- **Setup.** Inducing points $Z$ (pseudoinputs) are like a learned summary of the training data that we can condition on. Function values $f_Z$ (often $u$) are unknown. The exact joint prior is
$$p(f_X,f_*)=\int p(f_*,f_X\mid f_Z)p(f_Z)\,df_Z=\mathcal N\Big(0,\begin{pmatrix}K_{X,X}&K_{X,*}\\K_{*,X}&K_{*,*}\end{pmatrix}\Big)\tag{18.117}$$
(p. 707).
- **Key assumption.** $f_Z$ acts as a sufficient statistic: $f_*\perp f_X\mid f_Z$, so
$$p(f_*,f_X,f_Z)=p(f_*|f_X,f_Z)p(f_X|f_Z)p(f_Z)\approx p(f_*|f_Z)p(f_X|f_Z)p(f_Z)\tag{18.118}$$
(p. 708; Fig. 18.12). The method is often called a "sparse GP" (p. 708). The conditionals are
$$p(f_X|f_Z)=\mathcal N(f_X\mid K_{X,Z}K_{Z,Z}^{-1}f_Z,\ K_{X,X}-Q_{X,X})\tag{18.119}$$
$$p(f_*|f_Z)=\mathcal N(f_*\mid K_{*,Z}K_{Z,Z}^{-1}f_Z,\ K_{*,*}-Q_{*,*})\tag{18.120}$$
They can be seen as exact inference on noise-free observations $f_Z$. Speed-ups come from further approximating $\tilde Q_{X,X}=K_{X,X}-Q_{X,X}$ and $\tilde Q_{*,*}=K_{*,*}-Q_{*,*}$ (p. 708).
- All variants below cost $O(M^3+NM^2)$ to train, then $O(M)$ per test case for the mean and $O(M^2)$ for the variance. Exact inference costs $O(N^3)$ for training, $O(N)$ and $O(N^2)$ for testing (p. 708).

**18.5.3.1 SOR/DIC.** Set $\tilde Q_{X,X}=0$ and $\tilde Q_{*,*}=0$ (deterministic conditionals). Prior: $q_{\rm SOR}(f_X,f_*)=\mathcal N(0,\begin{pmatrix}Q_{X,X}&Q_{X,*}\\Q_{*,X}&Q_{*,*}\end{pmatrix})$ (18.121). With $\hat Q_{X,X}=Q_{X,X}+\sigma^2I_N$ and $\Sigma=(\sigma^{-2}K_{Z,X}K_{X,Z}+K_{Z,Z})^{-1}$ (p. 709):
$$q_{\rm SOR}(f_*|y)=\mathcal N(f_*\mid Q_{*,X}\hat Q_{X,X}^{-1}y,\ Q_{*,*}-Q_{*,X}\hat Q_{X,X}^{-1}Q_{X,*})\tag{18.122}$$
$$=\mathcal N(f_*\mid\sigma^{-2}K_{*,Z}\Sigma K_{Z,X}y,\ K_{*,Z}\Sigma K_{Z,*})\tag{18.123}$$
This is GP inference with kernel $\mathcal K_{\rm SOR}(x_i,x_j)=\mathcal K(x_i,Z)K_{Z,Z}^{-1}\mathcal K(Z,x_j)$ (18.124). That kernel matrix has rank $M$, so the GP is degenerate. It is near 0 when $x_i$ or $x_j$ is far from one of the chosen points $Z$, which can underestimate predictive variance (p. 709).

**18.5.3.2 DTC.** Assume only $\tilde Q_{X,X}=0$ and keep $\tilde Q_{*,*}=K_{*,*}-Q_{*,*}$ exact. Prior $q_{\rm dtc}=\mathcal N(0,\begin{pmatrix}Q_{X,X}&Q_{X,*}\\Q_{*,X}&K_{*,*}\end{pmatrix})$ (18.125). Predictive:
$$q_{\rm dtc}(f_*|y)=\mathcal N(f_*\mid Q_{*,X}\hat Q_{X,X}^{-1}y,\ K_{*,*}-Q_{*,X}\hat Q_{X,X}^{-1}Q_{X,*})\tag{18.126}$$
$$=\mathcal N(f_*\mid\sigma^{-2}K_{*,Z}\Sigma K_{Z,X}y,\ K_{*,*}-Q_{*,*}+K_{*,Z}\Sigma K_{Z,*})\tag{18.127}$$
The mean equals SOR's. The variance is larger, due to the uncertainty of $f_*$ given $f_Z$ (p. 709).

**18.5.3.3 FITC.** Assume $q(f_X|f_Z)$ fully factorises:
$$q(f_X|f_Z)=\prod_{n=1}^Np(f_n|f_Z)=\mathcal N(f_X\mid K_{X,Z}K_{Z,Z}^{-1}f_Z,\ \mathrm{diag}(K_{X,X}-Q_{X,X}))\tag{18.128}$$
It throws away less uncertainty than SOR and DTC because it makes no deterministic assumption linking $f_X$ and $f_Z$ (p. 709). Joint prior:
$$q_{\rm fitc}=\mathcal N\Big(0,\begin{pmatrix}Q_{X,X}-\mathrm{diag}(Q_{X,X}-K_{X,X})&Q_{X,*}\\Q_{*,X}&K_{*,*}\end{pmatrix}\Big)\tag{18.129}$$
For a single test case, with $\Lambda\triangleq\mathrm{diag}(K_{X,X}-Q_{X,X}+\sigma^2I_N)$ and $\Sigma\triangleq(K_{Z,Z}+K_{Z,X}\Lambda^{-1}K_{X,Z})^{-1}$ (p. 710):
$$q_{\rm fitc}(f_*|y)=\mathcal N(f_*\mid k_{*,Z}\Sigma K_{Z,X}\Lambda^{-1}y,\ k_{**}-q_{**}+k_{*,Z}\Sigma k_{Z,*})\tag{18.130}$$
Batches of test cases assumed conditionally independent give FIC. The cost equals SOR/DTC, and FITC avoids some pathologies of a degenerate kernel. It is equivalent to exact GP inference with the non-degenerate kernel: $\mathcal K_{\rm fic}(x_i,x_j)=\mathcal K(x_i,x_j)$ if $i=j$, and $\mathcal K_{\rm SOR}(x_i,x_j)$ if $i\ne j$ (18.131) (p. 710).

**18.5.3.4 Learning the inducing points.** Treat $Z$ like kernel hyperparameters and maximise
$$\log q(y|X,Z)=\log\!\iint p(y|f_X)q(f_X|X,f_Z)p(f_Z|Z)\,df_Z\,df\tag{18.132}$$
$$=\log\!\int p(y|f_X)q(f_X|X,Z)\,df_X\tag{18.133}$$
$$=-\tfrac12\log|Q_{X,X}+\Lambda|-\tfrac12y^{\mathsf T}(Q_{X,X}+\Lambda)^{-1}y-\tfrac n2\log(2\pi)\tag{18.134}$$
with $\Lambda_{\rm SOR}=\Lambda_{\rm dtc}=\sigma^2I_N$ and $\Lambda_{\rm fitc}=\mathrm{diag}(K_{X,X}-Q_{X,X})+\sigma^2I_N$ (p. 710). If inputs are in $\mathbb R^d$, optimise $Z\in\mathbb R^{Md}$ by gradients. For structured inputs (strings, graphs) choose $Z$ from the training set, use the mechanism in [Cao+15], or use discrete optimisation such as simulated annealing [For+18a] (Fig. 18.13, DNA sequences of length 4) (pp. 710–711).

*Intuition note.* These methods all assume that $f_Z$ explains the dependence between data and test points. They differ in how much leftover noise they keep. SOR keeps none, DTC keeps it only at test points, and FITC keeps the diagonal at training points (and, as in DTC, the full $K_{*,*}$ at test points).

### 18.5.4 Sparse variational methods: SVGP/VFE (pp. 710–714)
- **Idea.** Unlike 18.5.3, the model is unchanged and the *posterior* is approximated by variational inference. Inducing points $Z$ and variables $f_Z$ are variational parameters, not model parameters, which avoids the risk of overfitting. Posterior quality consistently improves as $m$ grows, eventually recovering exact inference, whereas in the classical inducing-point method larger $m$ does not always help [BWR16] (p. 711).
- Take a finite input set split into training $X$, inducing $Z$ and the rest $X_*$; $f=[f_X,f_Z,f_*]$ with $p(f)=\mathcal N(m(\mathcal X),\mathcal K(\mathcal X,\mathcal X))$. Assume $q(f)=p(f_*,f_X|f_Z)\,q(f_Z)$, with the first factor exact from the GP prior and $q(f_Z)$ learned by minimising $\mathcal K(q)=D_{\rm KL}(q(f)\,\|\,p(f|y))$. Intuitively $q(f_Z)$ is a "bottleneck" that "absorbs" all the observations (p. 711). (Footnote 2: this KL equals $D_{\rm KL}(q(f_X,f_Z)\|p(f_X,f_Z|y))$.)
- **Derivation** (p. 712). Use $p(f_*,f_X,f_Z|y)=p(f_*|f_X,f_Z)p(f_X|f_Z)p(f_Z)p(y|f_X)/p(y)$; the factors $p(f_*|f_X,f_Z)p(f_X|f_Z)$ cancel:
$$\mathcal K(q)=\int q(f_*,f_X,f_Z)\log\frac{q(f_*,f_X,f_Z)}{p(f_*,f_X,f_Z|y)}\,df_*df_Xdf_Z\tag{18.135–18.136}$$
$$=\int p(f_*,f_X|f_Z)q(f_Z)\log\frac{q(f_Z)p(y)}{p(f_Z)p(y|f_X)}\tag{18.137–18.138}$$
$$=\int q(f_Z)\log\frac{q(f_Z)}{p(f_Z)}df_Z-\int p(f_X|f_Z)q(f_Z)\log p(y|f_X)\,df_Xdf_Z+C\tag{18.139}$$
$$=D_{\rm KL}(q(f_Z)\|p(f_Z))-\mathbb E_{q(f_X)}[\log p(y|f_X)]+C,\quad C=\log p(y)\tag{18.140}$$
Equivalently, an ELBO to maximise:
$$\log p(y)=\mathcal K(q)+\mathbb E_{q(f_X)}[\log p(y|f_X)]-D_{\rm KL}(q(f_Z)\|p(f_Z))\tag{18.141}$$
$$\ge\mathbb E_{q(f_X)}[\log p(y|f_X)]-D_{\rm KL}(q(f_Z)\|p(f_Z))\triangleq\mathcal L(q)\tag{18.142}$$
- **Gaussian $q(f_Z)=\mathcal N(m,S)$**, with $p(f_Z)=\mathcal N(0,\mathcal K(Z,Z))$. The KL term is closed form via Eq. (5.77). The induced posterior at training points is
$$q(f_X|m,S)=\int p(f_X|f_Z,X,Z)q(f_Z|m,S)df_Z=\mathcal N(\tilde\mu,\tilde\Sigma)\tag{18.143}$$
$$\tilde\mu_i=m(x_i)+\alpha(x_i)^{\mathsf T}(m-m(Z))\tag{18.144}$$
$$\tilde\Sigma_{ij}=\mathcal K(x_i,x_j)-\alpha(x_i)^{\mathsf T}(\mathcal K(Z,Z)-S)\alpha(x_j)\tag{18.145}$$
$$\alpha(x_i)=\mathcal K(Z,Z)^{-1}\mathcal K(Z,x_i)\tag{18.146}$$
and $\mathbb E_{q(f_X)}[\log p(y|f_X)]=\sum_n\mathbb E_{q(f_n)}[\log p(y_n|f_n)]$ with $q(f_n)=\mathcal N(\tilde\mu_n,\tilde\Sigma_{nn})$ (18.147) (p. 712).

**18.5.4.1 Gaussian likelihood** (pp. 712–713). With $m(x)=0$ and noise precision $\beta$:
$$\mathbb E_{q(f_n)}\log\mathcal N(y_n|f_n,\beta^{-1})=\log\mathcal N(y_n|k_n^{\mathsf T}K_{Z,Z}^{-1}m,\beta^{-1})-\tfrac12\beta\tilde k_{nn}-\tfrac12\mathrm{tr}(S\Lambda_n)\tag{18.148}$$
where $\tilde k_{nn}=k_{nn}-k_n^{\mathsf T}K_{Z,Z}^{-1}k_n$, $k_n$ is the $n$th column of $K_{Z,X}$ and $\Lambda_n=\beta K_{Z,Z}^{-1}k_nk_n^{\mathsf T}K_{Z,Z}^{-1}$. The ELBO is
$$\mathcal L(q)=\log\mathcal N(y|K_{X,Z}K_{Z,Z}^{-1}m,\beta^{-1}I_N)-\tfrac12\beta\,\mathrm{tr}(K_{X,Z}K_{Z,Z}^{-1}SK_{Z,Z}^{-1}K_{Z,X})\tag{18.149}$$
$$\quad-\tfrac12\beta\,\mathrm{tr}(K_{X,X}-Q_{X,X})-D_{\rm KL}(q(f_Z)\|p(f_Z))\tag{18.150}$$
For gradients use [OA09]:
$$\tfrac{\partial}{\partial\mu}\mathbb E_{\mathcal N(x|\mu,\sigma^2)}[h(x)]=\mathbb E\big[\tfrac{\partial}{\partial x}h(x)\big]\ (18.151),\qquad \tfrac{\partial}{\partial\sigma^2}\mathbb E[h(x)]=\tfrac12\mathbb E\big[\tfrac{\partial^2}{\partial x^2}h(x)\big]\ (18.152)$$
with $h(x)=\log p(y_n|f_n)$. Then
$$\nabla_m\mathcal L=\beta K_{Z,Z}^{-1}K_{Z,X}y-\Lambda m\ (18.153),\qquad \nabla_S\mathcal L=\tfrac12S^{-1}-\tfrac12\Lambda\ (18.154)$$
Setting them to zero gives the optimum
$$S=\Lambda^{-1}\ (18.155),\quad \Lambda=\beta K_{Z,Z}^{-1}K_{Z,X}K_{X,Z}K_{Z,Z}^{-1}+K_{Z,Z}^{-1}\ (18.156),\quad m=\beta\Lambda^{-1}K_{Z,Z}^{-1}K_{Z,X}y\ (18.157)$$
This is **sparse GP regression (SGPR)** [Tit09]. The "collapsed" lower bound (with $f_Z$ marginalised out) is
$$\log p(y)\ge\log\mathcal N(y|0,K_{X,Z}K_{Z,Z}^{-1}K_{Z,X}+\beta^{-1}I)-\tfrac12\beta\,\mathrm{tr}(K_{X,X}-Q_{X,X})\tag{18.158}$$
If $Z=X$ the bound is tight: $\log p(y)=\log\mathcal N(y|0,K_{X,X}+\beta^{-1}I)$. Eq. (18.158) is almost the DTC marginal likelihood (18.134) except for the trace term, which prevents overfitting because $f_Z$ is variational rather than a prior (model) parameter (p. 713).

**18.5.4.2 Non-Gaussian likelihood** (p. 713). Define $h(f_n)=\log p(y_n|f_n)$ and use Monte Carlo on (18.151)–(18.152). For binary classification, Table 18.2 gives the derivatives. Numerical integration (Section 8.5.1.4) is an alternative.

**18.5.4.3 Minibatch SVI** (p. 714). The batch solution costs $O(M^3+NM^2)$, which may still be too slow if $N$ is large, unless $M$ is small, which compromises accuracy. Since (18.147) is a sum over $N$ terms, use stochastic optimisation [HFL13]:
$$\mathcal L(q)=\Big[\tfrac NB\sum_{b=1}^B\tfrac1{|\mathcal B_b|}\sum_{n\in\mathcal B_b}\mathbb E_{q(f_n)}[\log p(y_n|f_n)]\Big]-D_{\rm KL}(q(f_Z)\|p(f_Z))\tag{18.159}$$
($\mathcal B_b$ is the $b$th batch, $B$ the number of batches.) With a Gaussian likelihood the model is in the exponential family, so natural gradients with respect to the canonical parameters of $q(f_Z)$ can be computed efficiently and converge much faster (p. 714).

*Intuition note.* Inducing points are not part of the model; they are the shape of the approximate posterior. The text says that as the number of inducing points grows the posterior quality consistently improves, eventually recovering exact inference, and that the trace term in the collapsed bound is what prevents overfitting (pp. 711, 713).

### 18.5.5 Kernel matrix multiplies (pp. 714–716)
- Krylov subspace methods use only matrix-vector multiplication (MVM), which makes it easier to exploit kernel structure when present and, even without structure, parallelises easily on GPUs, unlike largely sequential Cholesky (p. 714).
- **18.5.5.1 CG and Lanczos.** Solve $K_\sigma\alpha=y$ by conjugate gradients. Let $\tau(K_\sigma)$ be the cost of one MVM; for dense $n\times n$, $\tau=n^2$. $C$ iterations cost $O(C\tau(K_\sigma))$. With $C=n$ and $\tau=n^2$ the solution is exact in $O(n^3)$, but often fewer iterations suffice, depending on the condition number of $K_\sigma$. The log determinant uses stochastic Lanczos quadrature, $O(L\tau(K_\sigma))$ for $L$ iterations (p. 714).
- **BBMM** [Gar+18a] is a batch CG parallelised on GPUs. With 8 GPUs [Wan+19a] did *exact* GP regression for $N\sim10^4$ points in seconds, $10^5$ in minutes, $10^6$ in hours (p. 715). Fig. 18.14: exact inference on a subset can often outperform approximate inference on the full data, and exact-GP performance keeps improving with data. Standard scalable approximations typically replace the kernel with one corresponding to a parametric model, whereas BBMM preserves the non-parametric representation, which can grow capacity with data (p. 715).
- **18.5.5.2 Compact support.** If $\mathcal K(x,x')=0$ for $\|x-x'\|>\epsilon$, then $K_\sigma$ is sparse and $\tau=O(N)$ (p. 715).
- **18.5.5.3 KISS.** SKI [WN15] interpolates inducing-point values: $K_{X,X}\approx W_XK_{Z,Z}W_X^{\mathsf T}$ (18.160), with $W_X$ sparse. With cubic interpolation each row has 4 nonzeros, so an MVM costs $O(N+M^2)$ (p. 716). SKI generalises all inducing-point methods: $W=K_{X,Z}K_{Z,Z}^{-1}$ recovers SOR. In 1d, a regular grid makes $K_{Z,Z}$ Toeplitz. In higher dimensions a grid makes it a Kronecker product of Toeplitz matrices, giving MVM in $O(N+M\log M)$ time and $O(N+M)$ space; this is **KISS-GP** (p. 716). KISS can take exponential time in $D$ because of the multidimensional lattice. **SKIP** [Gar+18b] writes many kernels (including ARD) as products of 1d kernels, $\mathcal K=\prod_d\mathcal K^d$, giving $O(DL(N+M\log M)+L^3N\log D+CL^2N)$; typical $L\sim10^1$, $C\sim10^2$ (p. 716).
- **18.5.5.4 Tensor train.** In the Gaussian VFE, represent $S$ with Kronecker structure and $m$ with a tensor-train decomposition combined with SKI. The resulting TT-GP can scale to billions of inducing points [INK18] (p. 716).

### 18.5.6 Converting a GP to an SSM (pp. 716–717)
For many stationary 1d kernels, the GP is a linear time-invariant SDE (the condition is that the spectral density is a rational function; this includes Matérn but not the SE kernel, which can be approximated) (fn. 3). The SDE converts to a linear-Gaussian state space model [HS10]. Example: the exponential kernel $\mathcal K(t,t')=\frac q{2\lambda}\exp(-\lambda|t-t'|)$ (Matérn $\nu=1/2$) corresponds to the Ornstein–Uhlenbeck process $\frac{dx}{dt}=-\lambda x+w(t)$ with white noise of spectral density $q$ (p. 716). Higher-order Matérn kernels need several latent states; higher-dimensional inputs need more to keep the Markov property (pp. 716–717). Kalman smoothing then gives exact inference in $O(N)$ time, or $\log N$ on highly parallel hardware (p. 717).

### 18.6 Learning the kernel (p. 717)
MacKay asked: "How can Gaussian processes replace neural networks? Have we thrown the baby out with the bathwater?" (p. 717). MacKay noted that neural nets can discover rich representations through adaptive hidden basis functions, while GPs with standard kernels such as the RBF are essentially just smoothing devices. The text adds that generalisation hinges on the kernel. Learning the kernel is how GPs do representation learning, and is often crucial for extrapolation (p. 717).

### 18.6.1 Empirical Bayes for kernel parameters (pp. 717–719)
- The noisy RBF kernel is
$$\mathcal K_y(x_p,x_q)=\sigma_f^2\exp\!\big(-\tfrac1{2\ell^2}(x_p-x_q)^2\big)+\sigma_y^2\delta_{pq}\tag{18.161}$$
$\ell$ = horizontal scale, $\sigma_f^2$ = vertical scale, $\sigma_y^2$ = noise variance (p. 717). Fig. 18.15: 20 noisy points sampled with $(\ell,\sigma_f,\sigma_y)=(1,1,0.1)$. Predictions with the same values fit well; with $\ell=3$ (and $\sigma_f=1.16,\sigma_y=0.89$ in the figure) the function is smoother, "arguably underfitting" (pp. 717–718).
- Grid search with validation loss (as for SVMs) is slow. Instead maximise the marginal likelihood $p(y|X,\theta)=\int p(y|f,X)p(f|X,\theta)df$ (18.162). Since $p(f|X)=\mathcal N(0,K)$ and $p(y|f)=\prod_n\mathcal N(y_n|f_n,\sigma_y^2)$:
$$\log p(y|X,\theta)=\log\mathcal N(y|0,K_\sigma)=-\tfrac12y^{\mathsf T}K_\sigma^{-1}y-\tfrac12\log|K_\sigma|-\tfrac N2\log(2\pi)\tag{18.163}$$
First term: data fit; second: model complexity; third: constant. For a 1d SE kernel with $\sigma_y^2$ fixed: short length scales fit well (small $y^{\mathsf T}K_\sigma^{-1}y$) but $K$ is almost diagonal, so $\log|K_\sigma|$ is large. Long length scales fit poorly, but $K$ is almost all 1's, so $\log|K_\sigma|$ is small (p. 718).
- Gradients (p. 718), with $\alpha=K_\sigma^{-1}y$:
$$\tfrac{\partial}{\partial\theta_j}\log p=\tfrac12y^{\mathsf T}K_\sigma^{-1}\tfrac{\partial K_\sigma}{\partial\theta_j}K_\sigma^{-1}y-\tfrac12\mathrm{tr}\big(K_\sigma^{-1}\tfrac{\partial K_\sigma}{\partial\theta_j}\big)\tag{18.164}$$
$$=\tfrac12\mathrm{tr}\big((\alpha\alpha^{\mathsf T}-K_\sigma^{-1})\tfrac{\partial K_\sigma}{\partial\theta_j}\big)\tag{18.165}$$
$K_\sigma^{-1}$ costs $O(N^3)$, then $O(N^2)$ per hyperparameter. For constraints such as $\sigma_y^2\ge0$, use $\theta=\log\sigma_y^2$ and the chain rule. The objective is not convex, so multiple restarts may be needed (p. 719).
- **18.6.1.1 Example (Fig. 18.16).** SE kernel, $\sigma_f^2=1$, 7 data points. Two local optima: low-noise, short length scale $(\ell,\sigma_n^2)\approx(1,0.2)$ (wiggly) and high-noise, long length scale $\approx(10,0.8)$ (smooth). With 7 points there is not enough evidence to decide confidently, although the complex model's marginal likelihood is about 60% higher; more data would favour it even more. Where $\sigma_y^2\approx1$ the likelihood is insensitive to $\ell$ (all data explained as noise). Where $\ell\approx0.5$ it is insensitive to the noise (data interpolated). A good optimiser would choose neither region (p. 719).

*Intuition note.* The marginal likelihood is a built-in Occam's razor: wiggly kernels fit the data but pay in $\log|K_\sigma|$, smooth ones pay in the fit term. The surface can still have several local optima.

### 18.6.2 Bayesian inference for kernel parameters (pp. 720–721)
- With few data points, a point estimate can be poor; e.g. if all observed values are similar, we may estimate $\hat\sigma\approx0$, which gives overly confident predictions (p. 720; fn. 5 notes a conjugate prior on $\sigma^2$ gives a more robust Student GP).
- For small $\dim\theta$, use a grid around the MAP $\hat\theta$:
$$p(f|\mathcal D)=\sum_{s=1}^Sp(f|\mathcal D,\theta_s)p(\theta_s|\mathcal D)w_s\tag{18.166}$$
In higher dimensions, a **central composite design** puts points at the mode and $\pm1$ sd along each dimension, $2|\theta|+1$ points (Fig. 18.17). Monte Carlo options: slice sampling [MA10], HMC [Hen+15], SMC [BBV11a] (p. 720).
- Fig. 18.18 fits $\mathcal K(r)=\sigma_1^2\mathcal K_{\rm SE}(r;\tau)\mathcal K_{\rm cos}(r;\rho_1)+\sigma_2^s\mathcal K_{32}(r;\rho_2)$ (18.167) by empirical Bayes and by HMC. Averaging over HMC samples captures more uncertainty than the plug-in estimate (pp. 720–721).

### 18.6.3 Additive kernels (pp. 721–722)
- $\mathcal K=\sum_{b=1}^Bw_b\mathcal K_b$ (18.168). Optimising $w_b>0$ by structural risk minimisation is multiple kernel learning (p. 721).
- **Hierarchical kernel learning:** base kernels depend on variable subsets with a hierarchical inclusion property (including $k_{123}$ requires $k_{12},k_{13},k_{23}$; Fig. 18.19). A good subset is found by convex optimisation [Bac09] but needs cross-validation for the weights; a more efficient empirical Bayes approach is in [DNR11] (p. 721).
- First-order additive kernels $\mathcal K=\sum_d\mathcal K_d(x_d,x'_d)$ (18.169) give $f(x)=f_1(x_1)+\dots+f_D(x_D)$ (18.170), a generalized additive model (GAM). Fig. 18.20 (concrete strength, 8 inputs): $\sigma_d^2$ for the coarse and fine inputs are set to zero, indicating no impact on the response (pp. 721–722).
- [DBW20]: $\mathcal K=\sum_bw_b\mathcal K_b(P_bx,P_bx')$ (18.171) can match or exceed kernels on the original space, even with 1-d, unlearned projections, promising for KISS and active learning (p. 722). OAK [LBH22] imposes orthogonality on the additive functions, giving an identifiable low-dimensional representation and improved performance (p. 722).

### 18.6.4 Automatic search for compositional kernels (pp. 722–725)
Based on [Duv+13]: start from a simple kernel (e.g. white noise) and replace it by alternatives (SE, RQ, ...), a sum $k\to k+k'$, or a product $k\to k\times k'$ (Fig. 18.21). Score each candidate with
$$\mathrm{BIC}(m)=\log p(\mathcal D|m)-\tfrac12|m|\log N$$
(fit minus complexity penalty; $|m|$ = number of parameters) (p. 724). This resembles what a human expert does: residual structure suggests a move; a global assumption such as linearity found to be only local suggests multiplying by an SE kernel (p. 724). Fig. 18.22 (airline passengers, depth-10 search) gives four additive components: a linear trend; an approximately periodic function with period 1.0 years and linearly increasing amplitude; a smooth function; and uncorrelated noise with linearly increasing standard deviation. A natural-language summary can be generated automatically [Llo+14] (pp. 724–725). [Sun+18] built a DNN whose hidden units are sums and products of elementary kernels, trained differentiably and so much faster (p. 725).

### 18.6.5 Spectral mixture kernels (pp. 725–726)
- Any stationary kernel has a dual form, its spectral density (Fourier transform). The RBF kernel gives a Gaussian density at the origin, Matérn a Student density. Standard multiple kernel learning with RBF/Matérn sums therefore amounts to density estimation with a scale mixture of Gaussians or Students at the origin, which is inflexible (p. 725).
- A scale-location mixture of Gaussians can model any density to arbitrary precision. Its inverse Fourier transform gives the spectral mixture kernel [WA13], for 1d inputs:
$$\mathcal K(x,x')=\sum_iw_i\cos\big((x-x')2\pi\mu_i\big)\exp\big(-2\pi^2(x-x')^2v_i\big)\tag{18.172}$$
Weights, means and variances can be learned by empirical Bayes or fully Bayesian inference (Fig. 18.23) (p. 725).
- Fig. 18.24: with learned spectral mixture kernels the GP extrapolates CO$_2$ and airline data automatically; the figure also shows Matérn, RQ, periodic and SE kernels for comparison. The text says expressive kernels plus scalable inference that preserves non-parametric structure (Kronecker, KISS-GP, CG) are needed for good extrapolation (p. 726).

### 18.6.6 Deep kernel learning (pp. 726–728)
- Deep RBF kernel: $\mathcal K_\theta(x,x')=\exp\!\big[-\tfrac1{2\sigma^2}\|h^L_\theta(x)-h^L_\theta(x')\|^2\big]$ (18.173), with $h^L_\theta$ the layer-$L$ outputs of a DNN; learn $\theta$ by marginal likelihood. The network can be pre-trained, learned jointly with the base kernel, or pre-trained then fine-tuned. It is a "last-layer" Bayesian model. The base kernel often provides a good measure of distance in feature space, encouraging high uncertainty far from the data (Fig. 18.25; p. 727).
- Fig. 18.26: on a discontinuous function, a GP with Matérn 3/2 predicts poorly out of sample, while the same GP after a learned 2-layer MLP (15 and 10 hidden units) works much better (pp. 727–728).
- Fig. 18.27 (Olivetti faces mapped to orientation angle): learned deep kernels (spectral-mixture and RBF base) show a pronounced diagonal band for data sorted by angle; a standard RBF kernel's matrix is diffuse. RBF essentially uses Euclidean distance, so highly non-Euclidean metric learning is needed (p. 728).
- [ORW21] show that DKL by marginal likelihood can overfit worse than standard DNN learning, and propose a fully Bayesian version using SGLD for DNN weights and GP hyperparameters (p. 728).

### 18.7 GPs and DNNs (p. 728)
Roadmap: NN-GP kernels from infinitely wide nets are fixed (no representation learning) but interesting, e.g. for non-stationary covariance. Then SGD training and the NTK, then deep GPs (p. 728).

### 18.7.1 NN-GP (pp. 729–730)
- One-hidden-layer MLP with Gaussian priors on all parameters converges, as width $\to\infty$, to a GP (first shown in [Nea96; Wil98]; extended to deep MLPs, CNNs and general DNNs) (p. 729). Model:
$$f_k(x)=b_k+\sum_{j=1}^Hv_{jk}h_j(x),\quad h_j(x)=\varphi(u_{0j}+x^{\mathsf T}u_j)\tag{18.174}$$
$$b_k\sim\mathcal N(0,\sigma_b),\ v_{jk}\sim\mathcal N(0,\sigma_v),\ u_{0j}\sim\mathcal N(0,\sigma_0),\ u_j\sim\mathcal N(0,\Sigma)\tag{18.175}$$
- Mean: $\mathbb E_\theta[f_k(x)]=\mathbb E[b_k]+\sum_j\mathbb E[v_{jk}]\mathbb E_u[h_j(x)]=0$ (18.176). Covariance (using $\mathbb E[u^2]=\sigma^2$ for $u\sim\mathcal N(0,\sigma^2)$):
$$\mathbb E_\theta[f_k(x)f_k(x')]=\sigma_b^2+\sum_{j}\mathbb E[v_{jk}^2]\mathbb E_u[h_j(x)h_j(x')]=\sigma_b^2+\sigma_v^2H\,\mathbb E_u[h_j(x)h_j(x')]\tag{18.177–18.178}$$
- As $H\to\infty$, scale $\sigma_v^2=\omega/H$. The output is an infinite sum of random variables, so by the central limit theorem it converges to a Gaussian:
$$\mathbb E[f_k(x)]=0,\quad\mathbb V[f_k(x)]=\sigma_b^2+\omega\mathbb E_u[h(x)^2]\tag{18.179}$$
and for any $N\ge2$ inputs the joint converges to a multivariate Gaussian with covariance
$$\mathbb E[f_k(x)f_k(x')]=\sigma_b^2+\omega\mathbb E_u[h(x)h(x')]\triangleq\mathcal K(x,x')\tag{18.180}$$
- Kernel computation: with $\tilde x=(1,x)$, $\tilde u=(u_0,u)$, $\tilde\Sigma=\mathrm{diag}(\sigma_0^2,\Sigma)$ (18.182),
$$C(x,x')=\mathbb E_u[h(u_0+u^{\mathsf T}x)h(u_0+u^{\mathsf T}x')]=\int h(\tilde u^{\mathsf T}\tilde x)h(\tilde u^{\mathsf T}\tilde x')\mathcal N(\tilde u|0,\tilde\Sigma)d\tilde u\tag{18.181, 18.183}$$
Closed forms exist for some activations (Table 18.4: erf, step, ReLU, from [Wil98; CS09]). Step: $C=\pi-\theta(\tilde x,\tilde x')$. ReLU: $C=\frac{f_2}{\pi}\sin\theta+\frac{\pi-\theta}{\pi}\tilde x^{\mathsf T}\tilde\Sigma\tilde x'$, with $f_2=\|\tilde\Sigma^{1/2}\tilde x\|\,\|\tilde\Sigma^{1/2}\tilde x'\|$, $f_3=\sqrt{(\tilde x^{\mathsf T}\tilde\Sigma\tilde x)((\tilde x')^{\mathsf T}\tilde\Sigma\tilde x')}$ and $\theta=\arccos f_3$, as printed (see Reading notes). E.g. for erf, $C=\frac2\pi\arcsin(f_1(\tilde x,\tilde x'))$ with $f_1=\frac{2\tilde x^{\mathsf T}\tilde\Sigma\tilde x'}{\sqrt{(1+2\tilde x^{\mathsf T}\tilde\Sigma\tilde x)(1+2\tilde x'^{\mathsf T}\tilde\Sigma\tilde x')}}$ (p. 730). The "neural net kernel" is non-stationary; its sample paths are nearly discontinuous and tend to constants for large positive or negative inputs (Fig. 18.28) (p. 730).

*Intuition note.* Many small independent random hidden-unit contributions add up to a Gaussian. The covariance between two inputs is the average product of their hidden features over the random weights.

### 18.7.2 Neural tangent kernel (p. 731)
- Can a kernel be derived from a DNN while or after it is trained? Let $f\in\mathbb R^{N}$ be predictions, $\nabla_f\mathcal L$ the $N\times1$ loss gradient, $\theta\in\mathbb R^P$ the parameters, $\nabla_\theta f$ the $P\times N$ matrix of partials. Continuous-time gradient descent with learning rate $\eta$:
$$\partial_t\theta_t=-\eta\nabla_\theta\mathcal L(f_t)=-\eta\nabla_\theta f_t\cdot\nabla_f\mathcal L(f_t)\tag{18.184}$$
$$\partial_tf_t=\nabla_\theta f_t^{\mathsf T}\partial_t\theta_t=-\eta\nabla_\theta f_t^{\mathsf T}\nabla_\theta f_t\cdot\nabla_f\mathcal L(f_t)=-\eta\mathcal T_t\cdot\nabla_f\mathcal L(f_t)\tag{18.185}$$
$$\mathcal T_t(x,x')\triangleq\nabla_\theta f_t(x)\cdot\nabla_\theta f_t(x')=\sum_{p=1}^P\frac{\partial f(x;\theta)}{\partial\theta_p}\Big|_{\theta_t}\frac{\partial f(x';\theta)}{\partial\theta_p}\Big|_{\theta_t}\tag{18.186}$$
($\mathcal T_t$ is $N\times N$.) For infinitesimal $\eta$ and widths $\to\infty$, $\mathcal T$ converges to a constant matrix, the **NTK** [JGH18]: $\mathcal T(x,x')\triangleq\nabla_\theta f(x;\theta_\infty)\cdot\nabla_\theta f(x';\theta_\infty)$ (18.187).
- The NTK results assume parameters barely change from initialisation (so a linear approximation is valid). Predictions can still change and reach zero training error because the final layer can use the random features, as in kernel regression. This "lazy training" is not representative of DNN behaviour in practice, where parameters often change a lot. A different parameterisation gives feature learning in the infinite-width limit [YH21] (p. 731).

### 18.7.3 Deep GPs (pp. 731–732)
A DGP of $L$ layers is
$$\mathrm{DGP}(x)=f_L\circ\dots\circ f_1(x),\quad f_i=[f_i^{(1)},\dots,f_i^{(H_i)}],\ f_i^{(j)}\sim\mathrm{GP}(0,\mathcal K_i)\tag{18.188}$$
Hidden nodes are hidden functions (p. 731). A single-layer GP with a non-degenerate kernel can model any function given enough data, but in practice is limited by the kernel. A GP on top of a DNN is in theory still just a GP, while a composition of GPs is strictly more general. Inference is complicated, so details are deferred to Supplementary Section 18.1 (p. 732).

### 18.8 GPs for time-series forecasting (p. 732)
Model $f(t)$ with a GP prior and forecast. Naively $O(T^3)$; for certain stationary kernels, a state-space reformulation plus Kalman smoother gives $O(T)$. This is exact for Matérn and approximate for RBF kernels; a parallel prefix scan gives $\log T$ on GPUs (p. 732).

### 18.8.1 Example: Mauna Loa (pp. 732–733)
Data: CO$_2$ with a year-long (quasi-)periodic signal on a long-term trend (Fig. 18.29). Following [RW06], $\mathcal K(r)=\mathcal K_1+\mathcal K_2+\mathcal K_3+\mathcal K_4$ (18.189), with $\mathcal K_i(t,t')=\mathcal K_i(t-t')$ (p. 733):
- Trend (SE): $\mathcal K_1=\theta_0^2\exp(-r^2/2\theta_1^2)$ (18.190).
- Seasonal (periodic × SE decay, period $\theta_4=1$ year): $\mathcal K_2=\theta_2^2\exp\!\big(-\tfrac{r^2}{2\theta_3^2}-\theta_5\sin^2(\tfrac{\pi r}{\theta_4})\big)$ (18.191).
- Medium-term irregularities (rational quadratic): $\mathcal K_3=\theta_6^2\big[1+\tfrac{r^2}{2\theta_7^2\theta_8}\big]^{-\theta_8}$ (18.192).
- Correlated noise (SE): $\mathcal K_4=\theta_9^2\exp(-r^2/2\theta_{10}^2)$ (18.193). Independent noise goes into the likelihood's observation noise. The combination of $\mathcal K_1$ and $\mathcal K_4$ is non-identifiable, which does not affect predictions.

Fit by maximising the marginal likelihood over $\theta$ (18.6.1); forecast in Fig. 18.29(b) (p. 733).

## Toy example (ours, not from the text)
Nyström/SOR/FITC with $N=3$, $M=1$. Let $Z$ be the first point and take the Gram matrix
$$K=\begin{pmatrix}1&0.5&0.25\\0.5&1&0.5\\0.25&0.5&1\end{pmatrix}.$$
Here $K_{Z,Z}=1$ and $K_{\cdot,Z}=(1,0.5,0.25)^{\mathsf T}$. Then $Q=K_{\cdot,Z}K_{Z,Z}^{-1}K_{Z,\cdot}=$ the outer product
$$Q=\begin{pmatrix}1&0.5&0.25\\0.5&0.25&0.125\\0.25&0.125&0.0625\end{pmatrix}.$$
It has rank 1 and equals $K$ in row and column 1. The residual is
$$K-Q=\begin{pmatrix}0&0&0\\0&0.75&0.375\\0&0.375&0.9375\end{pmatrix}.$$
(Check, lower block: determinant $0.75\cdot0.9375-0.375^2=0.703125-0.140625=0.5625>0$.)

- SOR uses $Q$: the prior variances of points 2 and 3 shrink to $0.25$ and $0.0625$ (from 1). A test point with $k(x_*,z)=0.01$ has SOR prior variance $0.01^2=0.0001$ against $1$ under the true kernel (assuming $K_{*,*}=1$), so SOR is overconfident far from $Z$ (cf. p. 709).
- FITC (18.129) uses $Q+\mathrm{diag}(K-Q)$, with $\mathrm{diag}(K-Q)=(0,0.75,0.9375)$. This restores the diagonal to $1$ and keeps off-diagonals of $Q$:
$$\begin{pmatrix}1&0.5&0.25\\0.5&1&0.125\\0.25&0.125&1\end{pmatrix}.$$
It has full rank (the Schur complement of the first entry is $\mathrm{diag}(0.75,0.9375)>0$), so it is non-degenerate.

## Concepts
- [[marginal-likelihood-evidence]] — $p(y|X,\theta)$ with latent $f$ integrated out; used to learn kernel hyperparameters and inducing points (pp. 710, 718)
- [[bayesian-occam-razor]] — in (18.163) the $\log|K_\sigma|$ term penalises complex kernels while the quadratic form measures fit (p. 718)
- [[variational-inference-elbo]] — SVGP maximises $\mathbb E_{q(f_X)}[\log p(y|f_X)]-D_{\rm KL}(q(f_Z)\|p(f_Z))$ (p. 712)
- [[kl-divergence]] — the objective $D_{\rm KL}(q(f)\|p(f|y))$ minimised in VFE (p. 711)
- [[posterior-predictive-distribution]] — GP predictions, optionally averaged over kernel-parameter posterior (18.166) (p. 720)
- [[hamiltonian-monte-carlo]] — one option for sampling kernel hyperparameters (p. 720)
- [[mcmc]] — slice sampling, HMC and SMC are named options for kernel-parameter inference (p. 720)
- [[empirical-bayes-kernel-learning]] (new) — maximise the marginal likelihood over kernel hyperparameters instead of grid search (p. 718)
- [[nystrom-approximation]] (new) — $K\approx K_{X,Z}K_{Z,Z}^{-1}K_{Z,X}$ from $M$ chosen points (p. 707)
- [[inducing-points-sparse-gp]] (new) — $f_Z$ as sufficient statistic: SOR/DIC, DTC, FITC (pp. 707–710)
- [[sparse-variational-gp]] (new) — SVGP/VFE: exact conditional, learned $q(f_Z)$; inducing points are variational parameters (p. 711)
- [[krylov-mvm-inference]] (new) — CG and Lanczos use only matrix-vector products; basis of BBMM, KISS-GP, SKIP (p. 714)
- [[gp-state-space-form]] (new) — stationary 1d GP as LTI SDE and linear-Gaussian SSM, $O(N)$ Kalman smoothing (p. 716)
- [[compositional-kernel-search]] (new) — BIC-guided search over sums and products of base kernels (p. 724)
- [[spectral-mixture-kernel]] (new) — kernel from a Gaussian-mixture spectral density, (18.172) (p. 725)
- [[deep-kernel-learning]] (new) — base kernel applied to learned DNN features (p. 726)
- [[nn-gp-kernel]] (new) — GP limit of an infinitely wide MLP with Gaussian priors (p. 729)
- [[neural-tangent-kernel]] (new) — constant kernel $\nabla_\theta f\cdot\nabla_\theta f$ in the infinite-width, small-learning-rate limit (p. 731)
- [[deep-gp]] (new) — composition of GP layers (p. 731)

## Canonical instances
- [[finland-heart-attack-disease-mapping]] (new) — Poisson GP, $y_n\sim\mathrm{Poi}(e_nr_n)$, $\log r\sim$ GP, Laplace approximation (p. 704)
- [[mauna-loa-co2-forecasting]] (new) — sum of SE, periodic×SE, RQ and SE kernels (pp. 732–733)
- [[airline-passengers-kernel-search]] (new) — compositional search (p. 724) and spectral mixture extrapolation (p. 726)
- [[olivetti-faces-deep-kernel]] (new) — deep kernel finds diagonal band by orientation (p. 728)
- [[marglik-local-minima-1d]] (new) — two local optima in the marginal likelihood (p. 719)

## Bridges (candidates)
- [same-math] SVGP ELBO (18.142) ↔ bayesian: ELBO = expected log-likelihood minus KL from approximate posterior to prior, here with $q(f)=p(f_*,f_X|f_Z)q(f_Z)$.
- [same-math] GP with Matérn kernel ↔ state-space models: for the kernels where the SDE conversion is exact, a 1d GP is a linear-Gaussian SSM and Kalman smoothing gives the same posterior.
- [structural-analogy] $f_Z$ as sufficient statistic, $f_*\perp f_X|f_Z$ ↔ graphical models: a hub variable that screens off training from test.
- [structural-analogy] Marginal likelihood fit-vs-complexity (18.163) and BIC kernel search ↔ model comparison: both penalise complexity.
- [structural-analogy] Lazy training in the NTK regime ↔ kernel regression: the text says the last layer uses random features as in kernel regression.
- [metaphor] Kernel learning ↔ neural representation learning: the author calls kernel learning "analogous to training a neural network" (p. 717).

## Questions this raises
- When does the $O(N)$ SSM route fail, and how do the extra latent states grow for higher-dimensional inputs?
- How should one choose $M$ in SVGP, and how does the Fig. 18.14 result (exact subset beating approximate full data) depend on data and kernel?
- Does a fully Bayesian treatment of kernel hyperparameters or DNN weights avoid the overfitting [ORW21] found for DKL, and at what cost?
- If NN-GP and NTK are fixed kernels, what exactly do finite networks gain from feature learning?

## Reading notes
- **Part boundaries.** This unit starts in the middle of the section before 18.4.4 (the end of the Poisson-regression example, Fig. 18.10, printed p. 704; the heading 18.4.3 itself is not on these pages) and ends with 18.8.1 (printed p. 733). The final page (pdf 768, printed 734) is blank. Printed = pdf − 34.
- **Possible sign misprint.** Eq. (18.107) is printed with "+" in front of the second term $\sigma^{-2}U(\ldots)^{-1}U^{\mathsf T}$. My own check with the Woodbury identity gives a "−" there. I copied the page as printed.
- **Possible missing factor.** Eq. (18.108) as printed has no $\sigma^{2(N-M)}$ factor. My own check with the Sylvester determinant lemma suggests the exact identity has one.
- **Symbol reuse.** $\Lambda$ is used for eigenvalues (18.106), for the FITC/log-likelihood matrix (18.130, 18.134), for $\Lambda_n$ in (18.148) and for the optimum (18.156).
- **Caption mismatch.** The Fig. 18.16 caption uses $\sigma_n^2$ where the text uses $\sigma_y^2$.
- **DTC variance.** The text justifies the larger DTC variance by saying $K_{*,*}-Q_{*,*}$ is "positive definite" (p. 709); L3 gives only the conclusion.
- **Table 18.4.** The text layer of the caption is garbled; the entries were transcribed from the image. As printed, $f_2$ and $f_3$ are algebraically the same quantity, so $\theta=\arccos f_3$ looks like a printing slip (my own check; I copied it as printed).
- **Text-layer problems.** Eq. (18.137) has cancellation strikes in the image. The text layer was garbled there, but the image is clear.
- **Cross-references.** Several equations and sections referred to are outside this part (e.g. 18.52, 18.53, Table 18.2, Supplementary 18.1, 18.2).
