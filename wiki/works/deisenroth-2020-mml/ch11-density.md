---
id: deisenroth-2020-mml/ch11-density
work: deisenroth-2020-mml
unit: "11 Density Estimation with Gaussian Mixture Models"
pages: 348–369
fields: [linear-algebra]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 2
pipeline_version: 0.1
---
# Density Estimation with Gaussian Mixture Models

## L0 — One line
A Gaussian mixture model is fitted by maximum likelihood with the EM algorithm, which alternates computing soft cluster assignments (responsibilities) with responsibility-weighted updates of means, covariances and weights.

## L1 — The gist (≤ 120 words)
A single Gaussian can be a poor model for clustered data. The chapter asks how to fit a mixture of K Gaussians to data by maximum likelihood. No closed-form solution exists, because the update for each parameter depends on responsibilities, which in turn depend on all parameters. The authors derive update formulas for means, covariances and weights, and alternate them with recomputing the responsibilities: this is the EM algorithm. A latent-variable view (a hidden variable says which component made each point) then explains responsibilities as posterior probabilities and gives a principled derivation of EM. Each EM step raises the log-likelihood, but EM may reach only a local optimum.

**Prerequisites:** Gaussian density; likelihood and log-likelihood; partial derivatives and the chain rule; matrix-derivative identities (determinant, quadratic form); Lagrange multipliers; Bayes' theorem; one-hot vectors.

## L2 — Key ideas
- A mixture model is a convex combination of simple densities (non-negative weights that sum to 1). It allows several clusters (multimodal densities), whereas a single Gaussian would approximate the data of Figure 11.1 poorly (p. 349).
- The GMM log-likelihood has a sum inside the log. So setting the gradient to zero gives no closed-form maximum likelihood solution (pp. 351–352).
- The responsibility $r_{nk}$ is a normalized "soft assignment" of data point $n$ to component $k$. All update formulas are written in terms of it (pp. 352–353).
- With responsibilities held fixed, the stationarity conditions (gradient set to zero) give weighted means, weighted covariances ($\Sigma_k$ is a weighted sum of outer products) and weights $N_k/N$ (pp. 353–359).
- EM alternates an E-step (compute $r_{nk}$) and an M-step (update $\mu_k,\Sigma_k,\pi_k$). In the running example the log-likelihood rises from −28.3 to −14.4 after one cycle (pp. 360–361).
- The latent-variable view uses a one-hot indicator $z$ (a vector with a single 1 and zeros elsewhere, saying which component made the point). Marginalizing $z$ recovers the GMM, and $p(z_k=1\mid x_n)=r_{nk}$ (pp. 364–367).
- EM increases the log-likelihood but gives no guarantee of reaching the maximum likelihood solution. Different initializations can reduce the risk of a bad local optimum (p. 367).
- Maximum likelihood for GMMs can overfit (a component collapsing on one point), and it gives only a point estimate. K-means is the "hard assignment" relative of the GMM (p. 368).

## L3 — Walkthrough

### Introduction (pp. 348–349)
- Density estimation is introduced as a third pillar of machine learning, after regression and dimensionality reduction. The data are represented compactly by a density from a parametric family, such as a Gaussian or Beta (p. 348).
- The Gaussian, and the other distributions met so far, have limited modeling capability. A Gaussian would approximate the density behind Figure 11.1 poorly (p. 349).
- **Mixture model** (convex combination of $K$ base densities; $\pi_k$ are the *mixture weights*) (p. 349):
$$p(\boldsymbol x)=\sum_{k=1}^K \pi_k p_k(\boldsymbol x)\tag{11.1}$$
$$0\le\pi_k\le1,\quad \sum_{k=1}^K\pi_k=1\tag{11.2}$$
- Mixtures are more expressive than their base distributions because they allow *multimodal* representations, i.e. several clusters (p. 349).
- For GMMs there is no closed-form maximum likelihood solution. Instead we get dependent simultaneous equations that can only be solved iteratively (p. 349).

### 11.1 Gaussian Mixture Model (pp. 349–350)
$$p(\boldsymbol x\mid\boldsymbol\theta)=\sum_{k=1}^K\pi_k\,\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)\tag{11.3}$$
$$0\le\pi_k\le1,\quad\sum_{k=1}^K\pi_k=1\tag{11.4}$$
with $\boldsymbol\theta:=\{\boldsymbol\mu_k,\boldsymbol\Sigma_k,\pi_k: k=1,\dots,K\}$. For $K=1$ a single Gaussian is recovered (p. 349).

Figure 11.2 example (p. 350):
$$p(x\mid\boldsymbol\theta)=0.5\,\mathcal N(x\mid-2,\tfrac12)+0.2\,\mathcal N(x\mid1,2)+0.3\,\mathcal N(x\mid4,1)\tag{11.5}$$

*Intuition note:* A GMM draws several bumps and adds them with weights that sum to 1. Each bump can sit on a different cluster, so the total density can have several peaks.

### 11.2 Parameter Learning via Maximum Likelihood (pp. 350–352)
- Data $\mathcal X=\{\boldsymbol x_1,\dots,\boldsymbol x_N\}$ are drawn i.i.d. from an unknown $p(\boldsymbol x)$. The aim is to approximate it by a GMM with $K$ components (p. 350).
- **Example 11.1 (running example).** Data $\mathcal X=\{-3,-2.5,-1,0,2,4,5\}$ ($N=7$), $K=3$. Initial components (p. 351):
$$p_1=\mathcal N(x\mid-4,1),\quad p_2=\mathcal N(x\mid0,0.2),\quad p_3=\mathcal N(x\mid8,3)\tag{11.6–11.8}$$
 with $\pi_1=\pi_2=\pi_3=\tfrac13$ (second argument of $\mathcal N$ is the variance).
- Likelihood and log-likelihood (p. 351):
$$p(\mathcal X\mid\boldsymbol\theta)=\prod_{n=1}^N p(\boldsymbol x_n\mid\boldsymbol\theta),\quad p(\boldsymbol x_n\mid\boldsymbol\theta)=\sum_{k=1}^K\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)\tag{11.9}$$
$$\log p(\mathcal X\mid\boldsymbol\theta)=\sum_{n=1}^N\log\sum_{k=1}^K\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)=:\mathcal L\tag{11.10}$$
- The usual route (gradient $=0$, solve) gives no closed form here. The key idea is to update one parameter at a time while keeping the others fixed (p. 351).
- *Remark (single Gaussian).* The sum over $k$ vanishes, so the log acts on the Gaussian directly (p. 351), where $D$ is the data dimension:
$$\log\mathcal N(\boldsymbol x\mid\boldsymbol\mu,\boldsymbol\Sigma)=-\tfrac D2\log(2\pi)-\tfrac12\log\det\boldsymbol\Sigma-\tfrac12(\boldsymbol x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\boldsymbol x-\boldsymbol\mu)\tag{11.11}$$
 This gives closed-form estimates. In (11.10) the log cannot be moved into the sum over $k$, so no simple closed form results (pp. 351–352).
- **Necessary conditions** (a local optimum must have vanishing gradient) (p. 352):
$$\frac{\partial\mathcal L}{\partial\boldsymbol\mu_k}=\mathbf 0^\top\iff\sum_n\frac{\partial\log p(\boldsymbol x_n\mid\boldsymbol\theta)}{\partial\boldsymbol\mu_k}=\mathbf 0^\top\tag{11.12}$$
 and the analogous (11.13) for $\boldsymbol\Sigma_k$ and (11.14) for $\pi_k$.
- All three need the chain-rule form
$$\frac{\partial\log p(\boldsymbol x_n\mid\boldsymbol\theta)}{\partial\boldsymbol\theta}=\frac1{p(\boldsymbol x_n\mid\boldsymbol\theta)}\frac{\partial p(\boldsymbol x_n\mid\boldsymbol\theta)}{\partial\boldsymbol\theta}\tag{11.15}$$
$$\frac1{p(\boldsymbol x_n\mid\boldsymbol\theta)}=\frac1{\sum_{j=1}^K\pi_j\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}\tag{11.16}$$

#### 11.2.1 Responsibilities (pp. 352–353)
$$r_{nk}:=\frac{\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\sum_{j=1}^K\pi_j\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}\tag{11.17}$$
- $r_{nk}$ is the *responsibility* of component $k$ for point $n$. It is proportional to $\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ (11.18). The component has high responsibility when the point could plausibly be a sample from it (p. 352).
- $\boldsymbol r_n=[r_{n1},\dots,r_{nK}]^\top\in\mathbb R^K$ is a normalized probability vector: $\sum_k r_{nk}=1$, $r_{nk}\ge0$. It is a "soft assignment" of $\boldsymbol x_n$. A margin note says $\boldsymbol r_n$ follows a Boltzmann/Gibbs distribution (pp. 352–353).
- The author states that $r_{nk}$ represents the probability that $\boldsymbol x_n$ was generated by component $k$ (p. 353). This is justified in 11.4.3.
- **Example 11.2.** For the running example, $R=[r_{nk}]\in\mathbb R^{N\times K}$ (rows are points, columns are components) (p. 353):

| $n$ | $k=1$ | $k=2$ | $k=3$ |
|---|---|---|---|
| 1 | 1.0 | 0.0 | 0.0 |
| 2 | 1.0 | 0.0 | 0.0 |
| 3 | 0.057 | 0.943 | 0.0 |
| 4 | 0.001 | 0.999 | 0.0 |
| 5 | 0.0 | 0.066 | 0.934 |
| 6 | 0.0 | 0.0 | 1.0 |
| 7 | 0.0 | 0.0 | 1.0 |

 Row sums are 1. Column sums $N_k$ (total responsibility) are $N_1=2.058$, $N_2=2.008$, $N_3=2.934$ (p. 353).
- Every update below depends on $r_{nk}$, which depends on all parameters. Hence closed-form maximum likelihood is impossible. The plan is to update parameters for given responsibilities, one at a time, then recompute responsibilities. The author says iterating "will eventually converge to a local optimum" (p. 353); 11.4.5 adds a caveat.

#### 11.2.2 Updating the Means (pp. 353–355)
**Theorem 11.1.**
$$\boldsymbol\mu_k^{\text{new}}=\frac{\sum_{n=1}^Nr_{nk}\boldsymbol x_n}{\sum_{n=1}^Nr_{nk}}\tag{11.20}$$
*Proof* (p. 354). Only component $k$ depends on $\boldsymbol\mu_k$:
$$\frac{\partial p(\boldsymbol x_n\mid\boldsymbol\theta)}{\partial\boldsymbol\mu_k}=\sum_{j}\pi_j\frac{\partial\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}{\partial\boldsymbol\mu_k}=\pi_k\frac{\partial\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\partial\boldsymbol\mu_k}\tag{11.21a}$$
$$=\pi_k(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1}\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)\tag{11.21b}$$
Insert into (11.15) with (11.16):
$$\frac{\partial\mathcal L}{\partial\boldsymbol\mu_k}=\sum_n\frac1{p(\boldsymbol x_n\mid\boldsymbol\theta)}\frac{\partial p(\boldsymbol x_n\mid\boldsymbol\theta)}{\partial\boldsymbol\mu_k}\tag{11.22a}$$
$$=\sum_n(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1}\underbrace{\frac{\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\sum_j\pi_j\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}}_{=r_{nk}}\tag{11.22b}$$
$$=\sum_{n=1}^Nr_{nk}(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1}\tag{11.22c}$$
Setting this to $\mathbf 0^\top$ and solving for $\boldsymbol\mu_k^{\text{new}}$:
$$\sum_nr_{nk}\boldsymbol x_n=\sum_nr_{nk}\boldsymbol\mu_k^{\text{new}}\iff\boldsymbol\mu_k^{\text{new}}=\frac{\sum_nr_{nk}\boldsymbol x_n}{\sum_nr_{nk}}=\frac1{N_k}\sum_nr_{nk}\boldsymbol x_n\tag{11.23}$$
with the *total responsibility*
$$N_k:=\sum_{n=1}^Nr_{nk}\tag{11.24}$$
- *Remark:* the update depends on all means, covariances and weights through $r_{nk}$, so no closed form for all $\boldsymbol\mu_k$ at once (p. 354).
- Interpretation: an importance-weighted Monte Carlo estimate of the mean, with weights $r_{nk}$. The mean is pulled toward $\boldsymbol x_n$ with strength $r_{nk}$ (Figure 11.4) (pp. 354–355). Equivalently, the expected value of the data under the probability vector $\boldsymbol r_k:=[r_{1k},\dots,r_{Nk}]^\top/N_k\in\mathbb R^N$ (11.25), written $\boldsymbol\mu_k\leftarrow\mathbb E_{\boldsymbol r_k}[\mathcal X]$ (11.26) (p. 355).
- **Example 11.3.** $\mu_1:-4\to-2.7$; $\mu_2:0\to-0.4$; $\mu_3:8\to3.7$ (11.27–11.29). Components 1 and 3 move toward the data; component 2 changes less (p. 355).

*Intuition note:* The new mean of component $k$ is the average of all data points, where each point counts as much as the component is "responsible" for it. Points that the component explains well pull hardest.

#### 11.2.3 Updating the Covariances (pp. 356–358)
**Theorem 11.2.**
$$\boldsymbol\Sigma_k^{\text{new}}=\frac1{N_k}\sum_{n=1}^Nr_{nk}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\tag{11.30}$$
Shapes: $\boldsymbol x_n,\boldsymbol\mu_k\in\mathbb R^D$; each term $(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\in\mathbb R^{D\times D}$ is an outer product; $r_{nk},N_k$ are scalars.

*Proof* (pp. 356–357). Start from
$$\frac{\partial\mathcal L}{\partial\boldsymbol\Sigma_k}=\sum_n\frac1{p(\boldsymbol x_n\mid\boldsymbol\theta)}\frac{\partial p(\boldsymbol x_n\mid\boldsymbol\theta)}{\partial\boldsymbol\Sigma_k}\tag{11.31}$$
Write the Gaussian explicitly and drop all terms except the $k$th:
$$\frac{\partial p}{\partial\boldsymbol\Sigma_k}=\frac{\partial}{\partial\boldsymbol\Sigma_k}\Big(\pi_k(2\pi)^{-D/2}\det(\boldsymbol\Sigma_k)^{-1/2}\exp\big(-\tfrac12(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1}(\boldsymbol x_n-\boldsymbol\mu_k)\big)\Big)\tag{11.32a,b}$$
By the product rule:
$$=\pi_k(2\pi)^{-D/2}\Big[\frac{\partial}{\partial\boldsymbol\Sigma_k}\det(\boldsymbol\Sigma_k)^{-1/2}\exp(\cdots)+\det(\boldsymbol\Sigma_k)^{-1/2}\frac{\partial}{\partial\boldsymbol\Sigma_k}\exp(\cdots)\Big]\tag{11.32c}$$
Identities used (book's (5.101) and (5.103)):
$$\frac{\partial}{\partial\boldsymbol\Sigma_k}\det(\boldsymbol\Sigma_k)^{-1/2}=-\tfrac12\det(\boldsymbol\Sigma_k)^{-1/2}\boldsymbol\Sigma_k^{-1}\tag{11.33}$$
$$\frac{\partial}{\partial\boldsymbol\Sigma_k}(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1}(\boldsymbol x_n-\boldsymbol\mu_k)=-\boldsymbol\Sigma_k^{-1}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1}\tag{11.34}$$
After rearranging (the author's words):
$$\frac{\partial p(\boldsymbol x_n\mid\boldsymbol\theta)}{\partial\boldsymbol\Sigma_k}=\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)\cdot\big[-\tfrac12(\boldsymbol\Sigma_k^{-1}-\boldsymbol\Sigma_k^{-1}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1})\big]\tag{11.35}$$
Putting it together, with $r_{nk}$ appearing:
$$\frac{\partial\mathcal L}{\partial\boldsymbol\Sigma_k}=\sum_nr_{nk}\cdot\big[-\tfrac12(\boldsymbol\Sigma_k^{-1}-\boldsymbol\Sigma_k^{-1}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\boldsymbol\Sigma_k^{-1})\big]\tag{11.36a–c}$$
$$=-\tfrac12\boldsymbol\Sigma_k^{-1}\underbrace{\sum_nr_{nk}}_{=N_k}+\tfrac12\boldsymbol\Sigma_k^{-1}\Big(\sum_nr_{nk}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\Big)\boldsymbol\Sigma_k^{-1}\tag{11.36d}$$
Setting this to $\mathbf 0$ gives the necessary condition
$$N_k\boldsymbol\Sigma_k^{-1}=\boldsymbol\Sigma_k^{-1}\Big(\sum_nr_{nk}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\Big)\boldsymbol\Sigma_k^{-1}\tag{11.37a}$$
$$\iff N_k\boldsymbol I=\Big(\sum_nr_{nk}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top\Big)\boldsymbol\Sigma_k^{-1}\tag{11.37b}$$
Solving for $\boldsymbol\Sigma_k$ gives (11.38), identical to (11.30). $\square$

*Skip path:* carry forward (11.30) only.

- Interpretation: an importance-weighted expected value of the squared centered data $\tilde{\mathcal X}_k:=\{\boldsymbol x_1-\boldsymbol\mu_k,\dots,\boldsymbol x_N-\boldsymbol\mu_k\}$ (p. 357), i.e. a Monte Carlo estimate of a weighted covariance with weights $r_{nk}$. It again depends on all parameters through $r_{nk}$, which prohibits a closed form (p. 358).
- **Example 11.4.** $\sigma_1^2:1\to0.14$; $\sigma_2^2:0.2\to0.44$; $\sigma_3^2:3\to1.53$ (11.39–11.41). Variances of components 1 and 3 shrink significantly; that of component 2 increases slightly (pp. 357–358).

*Intuition note:* This is the usual covariance formula (average of outer products of deviations), except that each data point is weighted by its responsibility for component $k$.

#### 11.2.4 Updating the Mixture Weights (pp. 358–360)
**Theorem 11.3.**
$$\pi_k^{\text{new}}=\frac{N_k}{N},\quad k=1,\dots,K\tag{11.42}$$
*Proof* (pp. 358–359). The constraint $\sum_k\pi_k=1$ is handled with a Lagrange multiplier $\lambda$ (Section 7.2). Lagrangian:
$$\mathfrak L=\mathcal L+\lambda\Big(\sum_k\pi_k-1\Big)=\sum_n\log\sum_k\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)+\lambda\Big(\sum_k\pi_k-1\Big)\tag{11.43}$$
Derivatives:
$$\frac{\partial\mathfrak L}{\partial\pi_k}=\sum_n\frac{\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\sum_j\pi_j\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}+\lambda=\frac1{\pi_k}\underbrace{\sum_n\frac{\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\sum_j\pi_j\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}}_{=N_k}+\lambda=\frac{N_k}{\pi_k}+\lambda\tag{11.44}$$
$$\frac{\partial\mathfrak L}{\partial\lambda}=\sum_k\pi_k-1\tag{11.45}$$
Setting both to 0 (necessary condition):
$$\pi_k=-\frac{N_k}{\lambda}\tag{11.46}$$
$$1=\sum_k\pi_k\tag{11.47}$$
Insert (11.46) in (11.47), using $\sum_kN_k=N$:
$$\sum_k\pi_k=1\iff-\sum_k\frac{N_k}{\lambda}=1\iff-\frac N\lambda=1\iff\lambda=-N\tag{11.48}$$
Substituting $\lambda=-N$ in (11.46) gives $\pi_k^{\text{new}}=N_k/N$ (11.49). $\square$

- Interpretation: $\pi_k$ is the share of total responsibility held by component $k$. Since $N=\sum_kN_k$, the data count is the total responsibility of all components, so $\pi_k$ is the relative importance of component $k$ (p. 359).
- *Remark:* $N_k=\sum_nr_{nk}$, so (11.42) also depends on all parameters via $r_{nk}$ (p. 359; the text's index $i$ in $\sum_{i=1}^N$ is a misprint for $n$).
- **Example 11.5.** $\pi_1:\tfrac13\to0.29$; $\pi_2:\tfrac13\to0.29$; $\pi_3:\tfrac13\to0.42$. After one full update of means, variances, weights, the log-likelihood rose from $-28.3$ (initialization) to $-14.4$ (p. 360).

*Intuition note:* A component's weight becomes the fraction of the data it is responsible for. In the example, $N_3/N=2.934/7\approx0.42$ (added check).

### 11.3 EM Algorithm (pp. 360–363)
- (11.20), (11.30), (11.42) are not closed-form, because $r_{nk}$ depends on the parameters. They do suggest an iterative scheme. The *EM algorithm* was proposed by Dempster et al. (1977). It is a general iterative scheme for learning parameters (maximum likelihood or MAP) in mixture models and, more generally, in latent-variable models (pp. 360–361).
- **E-step:** evaluate the responsibilities $r_{nk}$ (posterior probability of point $n$ belonging to component $k$). **M-step:** use them to re-estimate $\boldsymbol\mu_k,\boldsymbol\Sigma_k,\pi_k$ (p. 361).
- Every step increases the log-likelihood (Neal and Hinton, 1999). Convergence can be checked via the log-likelihood or the parameters (p. 361).
- **GMM-EM** (p. 361):
 1. Initialize $\boldsymbol\mu_k,\boldsymbol\Sigma_k,\pi_k$.
 2. E-step: $r_{nk}=\dfrac{\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\sum_j\pi_j\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}$ (11.53).
 3. M-step: $\boldsymbol\mu_k=\frac1{N_k}\sum_nr_{nk}\boldsymbol x_n$ (11.54); $\boldsymbol\Sigma_k=\frac1{N_k}\sum_nr_{nk}(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top$ (11.55); $\pi_k=N_k/N$ (11.56). A margin note says the means from (11.54) are then used in (11.55).
- **Example 11.6.** On the running example, EM converges after five iterations (Fig. 11.8) to
$$p(x)=0.29\,\mathcal N(x\mid-2.75,0.06)+0.28\,\mathcal N(x\mid-0.50,0.25)+0.43\,\mathcal N(x\mid3.64,1.63)\tag{11.57}$$
 (p. 362).
- On the 2-D data of Figure 11.1 with $K=3$, Figure 11.9 shows EM from initialization through iterations 1, 10 and 62; the negative log-likelihood falls steeply early and then flattens (p. 362). Figure 11.10 colors points by final responsibilities. One component clearly owns the left cluster. On the overlapping right side some points have responsibilities around 0.5 for two components, so they cannot be uniquely assigned (p. 363).

*Intuition note:* EM is "guess assignments, then refit, repeat". The guesses are soft (probabilities), so no point is forced into one cluster.

### 11.4 Latent-Variable Perspective (pp. 363–367)
The GMM is viewed as a *discrete* latent-variable model, whose latent variable takes finitely many values. In PCA the latent variables were continuous. Advantages: (i) it justifies earlier ad hoc decisions, (ii) responsibilities become posterior probabilities, (iii) EM can be derived in a principled way (p. 363).

#### 11.4.1 Generative Process and Probabilistic Model (pp. 363–365)
- Assume a point is generated by exactly one component. A binary indicator $z_k\in\{0,1\}$ says whether component $k$ generated it:
$$p(\boldsymbol x\mid z_k=1)=\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)\tag{11.58}$$
- $\boldsymbol z=[z_1,\dots,z_K]^\top\in\mathbb R^K$ has $K-1$ zeros and exactly one 1 (e.g. $[0,1,0]^\top$ selects component 2). So $\sum_kz_k=1$: a *one-hot* (1-of-K) encoding. This distribution is sometimes called "multinoulli" (p. 364).
- Since $\boldsymbol z$ is unknown, put a prior on it:
$$p(\boldsymbol z)=\boldsymbol\pi=[\pi_1,\dots,\pi_K]^\top,\quad\sum_k\pi_k=1\tag{11.59}$$
$$\pi_k=p(z_k=1)\tag{11.60}$$
- *Remark (sampling).* Sample $\boldsymbol z^{(i)}\sim p(\boldsymbol z)$, then $\boldsymbol x^{(i)}\sim p(\boldsymbol x\mid z^{(i)}=1)$. Discarding the $\boldsymbol z$ samples leaves valid GMM samples. Sampling a variable given samples of its parents in the graphical model (Fig. 11.11) is *ancestral sampling* (p. 364).
- Joint distribution:
$$p(\boldsymbol x,z_k=1)=p(\boldsymbol x\mid z_k=1)p(z_k=1)=\pi_k\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)\tag{11.61}$$
$$p(\boldsymbol x,\boldsymbol z)=\big[\pi_1\mathcal N(\boldsymbol x\mid\boldsymbol\mu_1,\boldsymbol\Sigma_1),\dots,\pi_K\mathcal N(\boldsymbol x\mid\boldsymbol\mu_K,\boldsymbol\Sigma_K)\big]^\top\tag{11.62}$$
 This fully specifies the model (p. 365).

#### 11.4.2 Likelihood (pp. 365–366)
Marginalize out the latent variable (summing over the $K$ one-hot configurations, e.g. (11.64) for $K=3$):
$$p(\boldsymbol x\mid\boldsymbol\theta)=\sum_{\boldsymbol z}p(\boldsymbol x\mid\boldsymbol\theta,\boldsymbol z)p(\boldsymbol z\mid\boldsymbol\theta)=\sum_{k=1}^Kp(\boldsymbol x\mid\boldsymbol\theta,z_k=1)p(z_k=1\mid\boldsymbol\theta)=\sum_{k=1}^K\pi_k\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)\tag{11.63–11.66}$$
This is the GMM (11.3). For a dataset, $p(\mathcal X\mid\boldsymbol\theta)=\prod_n\sum_k\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$ (11.67), exactly (11.9). So the latent-variable model is an equivalent way of thinking about a GMM (p. 366).

#### 11.4.3 Posterior Distribution (p. 366)
By Bayes' theorem, $p(z_k=1\mid\boldsymbol x)=\dfrac{p(z_k=1)p(\boldsymbol x\mid z_k=1)}{p(\boldsymbol x)}$ (11.68), which equals
$$\frac{p(z_k=1)p(\boldsymbol x\mid z_k=1)}{\sum_jp(z_j=1)p(\boldsymbol x\mid z_j=1)}=\frac{\pi_k\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\sum_j\pi_j\mathcal N(\boldsymbol x\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}\tag{11.69}$$
The author identifies this as the responsibility of component $k$ for $\boldsymbol x$.

#### 11.4.4 Extension to a Full Dataset (pp. 366–367)
- Each $\boldsymbol x_n$ has its own latent $\boldsymbol z_n=[z_{n1},\dots,z_{nK}]^\top\in\mathbb R^K$ (11.70). All share the prior $\boldsymbol\pi$ (plate notation, Fig. 11.12). The conditional factorizes: $p(\boldsymbol x_1,\dots,\boldsymbol x_N\mid\boldsymbol z_1,\dots,\boldsymbol z_N)=\prod_np(\boldsymbol x_n\mid\boldsymbol z_n)$ (11.71).
- Same reasoning gives $p(z_{nk}=1\mid\boldsymbol x_n)=\dfrac{\pi_k\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)}{\sum_j\pi_j\mathcal N(\boldsymbol x_n\mid\boldsymbol\mu_j,\boldsymbol\Sigma_j)}=r_{nk}$ (11.72). Responsibilities now have a mathematically justified interpretation as posterior probabilities (p. 367).

*Intuition note:* "Which component made this point?" is a hidden choice. Bayes' theorem turns our prior beliefs ($\pi_k$) and the fit of each component into a probability for that choice, and this probability is exactly $r_{nk}$.

#### 11.4.5 EM Algorithm Revisited (p. 367)
- Given current parameters $\boldsymbol\theta^{(t)}$, the E-step computes the expected log-likelihood
$$Q(\boldsymbol\theta\mid\boldsymbol\theta^{(t)})=\mathbb E_{\boldsymbol z\mid\boldsymbol x,\boldsymbol\theta^{(t)}}[\log p(\boldsymbol x,\boldsymbol z\mid\boldsymbol\theta)]=\int\log p(\boldsymbol x,\boldsymbol z\mid\boldsymbol\theta)\,p(\boldsymbol z\mid\boldsymbol x,\boldsymbol\theta^{(t)})\,\mathrm d\boldsymbol z\tag{11.73}$$
 taken under the posterior of the latent variables. The M-step picks $\boldsymbol\theta^{(t+1)}$ by maximizing (11.73b).
- An EM iteration does increase the log-likelihood, but there is no guarantee that EM converges to the maximum likelihood solution. It may reach a local maximum. Several runs with different initializations can reduce the risk of a bad local optimum (p. 367).

### 11.5 Further Reading (pp. 368–369)
- A GMM is a *generative model*: sample an index $k$ from $[\pi_1,\dots,\pi_K]^\top$, then $\boldsymbol x\sim\mathcal N(\boldsymbol\mu_k,\boldsymbol\Sigma_k)$. Figure 11.1 was generated this way (p. 368).
- $K$ was assumed known. Nested cross-validation (Section 8.6.1) could be used to find good models (p. 368).
- **K-means:** if the GMM means are treated as cluster centers and the covariances ignored (or set to $\boldsymbol I$), one arrives at K-means. K-means makes a "hard" assignment, a GMM a "soft" one via responsibilities (p. 368).
- EM can be used for parameter learning in general latent-variable models, e.g. nonlinear state-space models and reinforcement learning (p. 368).
- **Standard criticisms of maximum likelihood** (p. 368):
 - Severe overfitting is possible: if a component's mean equals a data point and its covariance tends to $\mathbf 0$, the likelihood approaches infinity.
 - Only a point estimate is obtained, with no sign of uncertainty. A Bayesian approach would place a prior on the parameters, giving a posterior and the model evidence (marginal likelihood) for comparison, so the number of components could be chosen in a principled way. Closed-form inference is not possible because there is no conjugate prior for this model. Approximations such as variational inference can be used.
- **Other density estimators** (p. 369): *Histograms* (Pearson, 1895) bin the data space and count points per bin. Bin size is a critical hyperparameter (bad choice means overfitting or underfitting) and can be set by cross-validation (Section 8.2.4). *Kernel density estimation* (Rosenblatt 1956; Parzen 1962), for i.i.d. samples:
$$p(\boldsymbol x)=\frac1{Nh}\sum_{n=1}^Nk\Big(\frac{\boldsymbol x-\boldsymbol x_n}{h}\Big)\tag{11.74}$$
 where $k$ is a kernel (a nonnegative function integrating to 1) and $h>0$ is a bandwidth, similar in role to bin size. One kernel is placed on every data point. Uniform and Gaussian kernels are common. A suitable kernel guarantees a smooth estimate. Figure 11.13 compares histogram and KDE on 250 data points.

## Toy example (ours, not from the text)
One E-step and one M-step in 1-D with $K=2$. Data $\{0,1,2\}$. Initial: $\mu_1=0,\ \mu_2=2$, both variances 1, $\pi_1=\pi_2=\tfrac12$.

**E-step.** Weights and variances are equal, so the constants cancel and $r_{n1}=\dfrac{e^{-(x-0)^2/2}}{e^{-(x-0)^2/2}+e^{-(x-2)^2/2}}$.
- $x=0$: $e^{0}=1$, $e^{-2}=0.1353$, so $r_{11}=1/1.1353=0.8808$, $r_{12}=0.1192$.
- $x=1$: both exponents are $e^{-1/2}$, so $r_{21}=r_{22}=0.5$.
- $x=2$: by symmetry $r_{31}=0.1192$, $r_{32}=0.8808$.

**M-step.** $N_1=0.8808+0.5+0.1192=1.5$ and $N_2=0.1192+0.5+0.8808=1.5$.
- $\mu_1=(0.8808\cdot0+0.5\cdot1+0.1192\cdot2)/1.5=0.7384/1.5=0.4923$; $\mu_2=(0.1192\cdot0+0.5\cdot1+0.8808\cdot2)/1.5=2.2616/1.5=1.5077$.
- $\sigma_1^2=\frac1{1.5}\big[0.8808(0-0.4923)^2+0.5(1-0.4923)^2+0.1192(2-0.4923)^2\big]=\frac1{1.5}[0.2134+0.1289+0.2710]=0.6133/1.5=0.409$. By symmetry $\sigma_2^2=0.409$.
- $\pi_1=\pi_2=1.5/3=0.5$.

The means move toward each other (0→0.49, 2→1.51) because the middle point is shared. The variances shrink from 1 to about 0.41 because each component now explains only its nearer points.

## Concepts
- [[gaussian-mixture-model]] (new) — density $\sum_k\pi_k\mathcal N(\boldsymbol x\mid\boldsymbol\mu_k,\boldsymbol\Sigma_k)$, a convex combination of Gaussians; $K=1$ is a single Gaussian (p. 349)
- [[mixture-model]] (new) — convex combination of base densities with mixture weights $\pi_k$ (p. 349)
- [[maximum-likelihood-estimation]] (new) — choose $\boldsymbol\theta$ to maximize $\log p(\mathcal X\mid\boldsymbol\theta)$. For GMMs there is no closed form (p. 351)
- [[responsibility]] (new) — $r_{nk}=\pi_k\mathcal N(\boldsymbol x_n\mid\cdot)/\sum_j\pi_j\mathcal N(\boldsymbol x_n\mid\cdot)$; soft assignment, later the posterior $p(z_{nk}=1\mid\boldsymbol x_n)$ (pp. 352, 367)
- [[em-algorithm]] (new) — alternate E-step (responsibilities) and M-step (parameter updates); raises log-likelihood, may reach a local optimum (pp. 360–361, 367)
- [[latent-variable-model]] (new) — model with unobserved variable $\boldsymbol z$; here discrete and one-hot, marginalized to give the likelihood (pp. 363–365)
- [[one-hot-encoding]] (new) — vector with a single 1 and $K-1$ zeros, selecting a component (p. 364)
- [[ancestral-sampling]] (new) — sample $\boldsymbol z\sim p(\boldsymbol z)$ first, then $\boldsymbol x\mid\boldsymbol z$ (p. 364)
- [[lagrange-multiplier]] (new) — enforces $\sum\pi_k=1$ when maximizing over the weights (pp. 358–359)
- [[kernel-density-estimation]] (new) — nonparametric density with a kernel on every data point, bandwidth $h$ (p. 369)
- [[k-means]] (new) — hard-assignment relative of GMM-EM (p. 368)
- [[rank-one-matrix-outer-product]] — each term $(\boldsymbol x_n-\boldsymbol\mu_k)(\boldsymbol x_n-\boldsymbol\mu_k)^\top$ in the covariance update is a $D\times D$ outer product (p. 356)

## Canonical instances
- [[gmm-running-example-1d]] (new) — 7 points, $K=3$; responsibility table, one update cycle (−28.3→−14.4), final fit after 5 EM iterations (pp. 351–362)
- [[gmm-2d-clusters-example]] (new) — Figure 11.1 data fitted with $K=3$; EM takes 62 iterations; ambiguous points with responsibility near 0.5 (pp. 362–363)

## Bridges (candidates)
- [structural-analogy] Weighted covariance update (11.30) ↔ PCA/covariance matrix: the same average of outer products of centered data, but with responsibility weights.
- [structural-analogy] Responsibilities $r_n$ as a normalized probability vector (margin note: Boltzmann/Gibbs) ↔ softmax: normalizing positive scores into a distribution.
- [structural-analogy] GMM-EM ↔ K-means: with covariances ignored, soft assignment becomes hard assignment (stated on p. 368).
- [metaphor] E-step/M-step alternation ↔ coordinate-wise optimization: update one block of parameters while holding the others fixed.
- [structural-analogy] Lagrangian for $\sum\pi_k=1$ ↔ constrained optimization (Section 7.2): the multiplier turns a constrained problem into stationarity equations.

## Questions this raises
- Why does each EM step increase the log-likelihood? The unit only cites Neal and Hinton (1999).
- How do initialization choices (means, covariances) change which local optimum EM reaches?
- What stops a component from collapsing on a single point (covariance → 0, likelihood → ∞), and what would a prior change?
- How could the number of components $K$ be chosen in practice: nested cross-validation or model evidence?

## Reading notes
- Page offset: printed = pdf − 6 (pdf 354 = printed 348). Page labels give printed numbers, which are used throughout.
- The text layer was usable. Equations were checked against the page images. The text layer for (11.44b), (11.49) and Example 11.2 was garbled but readable in the images.
- Possible inconsistency: the Figure 11.8 caption says the GMM is "from Figure 11.2", while the text (p. 362) says the example is "from Figure 11.3". The data and values (11.57) belong to the running example of Figure 11.3.
- After (11.38) the text says "$\boldsymbol r_k$ is the probability vector defined in (11.25)", but (11.38) contains no vector $\boldsymbol r_k$; the formula uses the scalars $r_{nk}$.
- In the remark on p. 359 the sum is written $\sum_{i=1}^N r_{nk}$, with index $i$ where $n$ is meant. In the sampling remark on p. 364, "component $i$" is selected while the text otherwise uses $k$.
- Page 353 says iterating responsibilities and updates "will eventually converge to a local optimum". Page 367 says EM gives no guarantee of reaching the maximum likelihood solution and may reach a local maximum. Both are reported as stated.
- The unit contains no exercises. The running header carries "Draft (2024-01-15)" on some pages and "©2024 … Published by Cambridge University Press (2020)" on others.
