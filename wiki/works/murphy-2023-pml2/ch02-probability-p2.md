---
id: murphy-2023-pml2/ch02-probability-p2
work: murphy-2023-pml2
unit: "2 Probability (part 2/3): Gaussian joint distributions (2.3) and the exponential family (2.4, up to Eq. 2.255)"
pages: 22-43
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 10
pipeline_version: 0.1
---
# Gaussian joint distributions and the exponential family

## L0 — One line
Gaussians are closed under marginalizing, conditioning and Bayesian updating, and they belong to the exponential family, whose log partition function generates the cumulants (first the mean and covariance) of the sufficient statistics.

## L1 — The gist (≤ 120 words)
This part asks how to compute with a multivariate normal (MVN) and the exponential family. For an MVN, marginals, conditionals and Bayes' rule have closed forms, in moment or information form. A Gaussian prior with a linear Gaussian likelihood gives a Gaussian posterior. The exponential family writes a density as $h(x)\exp[\eta^\top\mathcal T(x)-A(\eta)]$. Here $\mathcal T$ are the sufficient statistics (data features) and $A$ is the log normalizer; its derivatives give the mean and covariance of $\mathcal T(x)$. The MLE matches expected to empirical sufficient statistics. The part ends mid-derivation of the maximum-entropy view of this family. The author says it is at the core of GLMs and variational inference, and that every member has a conjugate prior (p. 33–34).

**Prerequisites:** matrix algebra (block matrices, inverse, determinant); multivariate Gaussian density; expectation, variance, covariance; partial derivatives and gradients; Lagrange multipliers.

## L2 — Key ideas
- The high-dimensional $\mathcal N(\mathbf 0,\mathbf I_D)$ puts most samples in a thin shell of radius about $\sigma\sqrt D$, not near the mode (p. 23).
- MVN marginals just read off sub-blocks of $\boldsymbol\mu,\boldsymbol\Sigma$. Conditionals have a mean linear in the observed block and a covariance that does not depend on it (p. 24).
- Moment form makes marginalization easy; information form (precision $\boldsymbol\Lambda$, $\boldsymbol\eta=\boldsymbol\Lambda\boldsymbol\mu$) makes conditioning easy (p. 25).
- In a linear Gaussian system, the posterior is Gaussian (Bayes' rule for Gaussians). Its mean is the prior mean plus a gain matrix $\mathbf K$ (the Kalman gain) times the surprise $\mathbf y-\mathbf m$, and $p(\mathbf y)$ gives the marginal likelihood (p. 29).
- Gaussian potentials in canonical form $(g,\mathbf h,\mathbf K)$ multiply by adding parameters. This allows a general inference calculus and the product-of-Gaussians rule (p. 31–33).
- The exponential family is defined by $h$, $\mathcal T$, $A$. Bernoulli, categorical and Gaussian fit. Student and uniform do not (p. 34–39).
- $\nabla A=\mathbb E[\mathcal T]$ and $\nabla^2A=\mathrm{Cov}[\mathcal T]$, which equals the Fisher information. The log-likelihood is concave and the MLE is moment matching (p. 39–42).
- Minimizing KL to a prior $q$ under feature-expectation constraints gives an exponential-family form (derivation begins on p. 43).

## L3 — Walkthrough

### End of 2.2: Dirichlet samples (Fig. 2.7, p. 22)
Samples from a 5-dimensional symmetric Dirichlet with $\boldsymbol\alpha=(0.1,\dots,0.1)$ are very sparse, with many 0s. With $\boldsymbol\alpha=(1,\dots,1)$ they are more uniform and dense (p. 22).

### 2.3 Gaussian joint distributions (p. 22)
The MVN is the most widely used joint distribution for continuous variables. It is mathematically convenient and often reasonable. The Gaussian has maximum entropy subject to specified first and second moments (Section 2.4.7, not yet reached in this part) (p. 22).

**2.3.1.1 Definition.** The MVN density is
$$\mathcal N(\mathbf x|\boldsymbol\mu,\boldsymbol\Sigma)\triangleq\frac{1}{(2\pi)^{D/2}|\boldsymbol\Sigma|^{1/2}}\exp\Big[-\tfrac12(\mathbf x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf x-\boldsymbol\mu)\Big]\tag{2.71}$$
with $\boldsymbol\mu=\mathbb E[\mathbf x]\in\mathbb R^D$ and $\boldsymbol\Sigma=\mathrm{Cov}[\mathbf x]$ ($D\times D$). The quadratic form is the squared Mahalanobis distance:
$$d_{\boldsymbol\Sigma}(\mathbf x,\boldsymbol\mu)^2=(\mathbf x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf x-\boldsymbol\mu)\tag{2.72}$$
In 2d, $\boldsymbol\Sigma=\begin{pmatrix}\sigma_1^2&\sigma_{12}^2\\\sigma_{21}^2&\sigma_2^2\end{pmatrix}=\begin{pmatrix}\sigma_1^2&\rho\sigma_1\sigma_2\\\rho\sigma_1\sigma_2&\sigma_2^2\end{pmatrix}$ (2.73), with $\rho\triangleq\sigma_{12}^2/(\sigma_1\sigma_2)$ (p. 22–23). Covariance types (Fig. 2.8, p. 23):
- A full matrix has $D(D+1)/2$ parameters and elliptical contours.
- A diagonal matrix has $D$ parameters and axis-aligned ellipses.
- A spherical (isotropic) matrix $\sigma^2\mathbf I_D$ has one parameter and circular contours.

**2.3.1.2 Gaussian shells (p. 23–24).** For $\mathbf x\sim\mathcal N(\mathbf 0,\mathbf I_D)$ the mode is at the origin. Yet in high dimensions the typical set is a thin annulus at distance $r=\sigma\sqrt D$ with thickness $O(\sigma D^{1/4})$. The density decays like $e^{-r^2/2}$ but the volume of a sphere grows like $r^D$. Mass is density times volume, so most points sit where the two balance ("Gaussian soap bubble"). For $d^2=\sum_i x_i^2$ with $x_i\sim\mathcal N(0,1)$ the text states $\mathbb E[d^2]=D$ and $\mathbb V[d^2]=D$, so
$$\lim_{D\to\infty}\frac{\mathrm{std}[d^2]}{\mathbb E[d^2]}=\lim_{D\to\infty}\frac{\sqrt D}{D}=0\tag{2.74}$$
Hence $d^2$ concentrates around $D$ and the expected distance around $\sqrt D$ (p. 24). For images sampled from $\mathcal N(\boldsymbol\mu,\sigma^2\mathbf I)$ with $\boldsymbol\mu$ the all-gray image, samples close to all-gray are extremely unlikely (p. 24).

*Intuition note.* Density is highest at the centre, but there is far more room farther out. In high dimensions, "typical" points are therefore all about the same distance from the centre.

**2.3.1.3 Marginals and conditionals (p. 24).** Partition $\boldsymbol\mu=(\boldsymbol\mu_1;\boldsymbol\mu_2)$ and $\boldsymbol\Sigma=\begin{pmatrix}\boldsymbol\Sigma_{11}&\boldsymbol\Sigma_{12}\\\boldsymbol\Sigma_{21}&\boldsymbol\Sigma_{22}\end{pmatrix}$ (2.75). Then
$$p(\mathbf x_1)=\mathcal N(\mathbf x_1|\boldsymbol\mu_1,\boldsymbol\Sigma_{11}),\quad p(\mathbf x_2)=\mathcal N(\mathbf x_2|\boldsymbol\mu_2,\boldsymbol\Sigma_{22})\tag{2.76–2.77}$$
$$p(\mathbf x_1|\mathbf x_2)=\mathcal N\big(\mathbf x_1|\boldsymbol\mu_1+\boldsymbol\Sigma_{12}\boldsymbol\Sigma_{22}^{-1}(\mathbf x_2-\boldsymbol\mu_2),\ \boldsymbol\Sigma_{11}-\boldsymbol\Sigma_{12}\boldsymbol\Sigma_{22}^{-1}\boldsymbol\Sigma_{21}\big)\tag{2.78}$$
$$p(\mathbf x_2|\mathbf x_1)=\mathcal N\big(\mathbf x_2|\boldsymbol\mu_2+\boldsymbol\Sigma_{21}\boldsymbol\Sigma_{11}^{-1}(\mathbf x_1-\boldsymbol\mu_1),\ \boldsymbol\Sigma_{22}-\boldsymbol\Sigma_{21}\boldsymbol\Sigma_{11}^{-1}\boldsymbol\Sigma_{12}\big)\tag{2.79}$$
The conditional mean is linear in $\mathbf x_2$, but the conditional covariance is independent of $\mathbf x_2$; the author calls this a peculiar property of Gaussians (p. 24).

**2.3.1.4 Information (canonical) form (p. 25).** Define the precision matrix and precision-weighted mean (the canonical or natural parameters):
$$\boldsymbol\Lambda\triangleq\boldsymbol\Sigma^{-1},\quad\boldsymbol\eta\triangleq\boldsymbol\Sigma^{-1}\boldsymbol\mu\tag{2.80}$$
$$\boldsymbol\mu=\boldsymbol\Lambda^{-1}\boldsymbol\eta,\quad\boldsymbol\Sigma=\boldsymbol\Lambda^{-1}\tag{2.81}$$
$$\mathcal N_c(\mathbf x|\boldsymbol\eta,\boldsymbol\Lambda)\triangleq c\exp\big(\mathbf x^\top\boldsymbol\eta-\tfrac12\mathbf x^\top\boldsymbol\Lambda\mathbf x\big),\quad c\triangleq\frac{\exp(-\frac12\boldsymbol\eta^\top\boldsymbol\Lambda^{-1}\boldsymbol\eta)}{(2\pi)^{D/2}\sqrt{\det(\boldsymbol\Lambda^{-1})}}\tag{2.82–2.83}$$
Marginals and conditionals in this form:
$$p(\mathbf x_1)=\mathcal N_c(\mathbf x_1|\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\boldsymbol\Lambda_{22}^{-1}\boldsymbol\eta_2,\ \boldsymbol\Lambda_{11}-\boldsymbol\Lambda_{12}\boldsymbol\Lambda_{22}^{-1}\boldsymbol\Lambda_{21})\tag{2.84}$$
$$p(\mathbf x_2)=\mathcal N_c(\mathbf x_2|\boldsymbol\eta_2-\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\eta_1,\ \boldsymbol\Lambda_{22}-\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\Lambda_{12})\tag{2.85}$$
$$p(\mathbf x_1|\mathbf x_2)=\mathcal N_c(\mathbf x_1|\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\mathbf x_2,\ \boldsymbol\Lambda_{11}),\quad p(\mathbf x_2|\mathbf x_1)=\mathcal N_c(\mathbf x_2|\boldsymbol\eta_2-\boldsymbol\Lambda_{21}\mathbf x_1,\ \boldsymbol\Lambda_{22})\tag{2.86–2.87}$$
So marginalization is easier in moment form and conditioning is easier in information form (p. 25).

**2.3.1.5 Derivation, moment form (p. 25–27).** The inverse of a partitioned matrix $\mathbf M=\begin{pmatrix}\mathbf E&\mathbf F\\\mathbf G&\mathbf H\end{pmatrix}$ (2.88), assuming $\mathbf E,\mathbf H$ invertible, is
$$\mathbf M^{-1}=\begin{pmatrix}(\mathbf M/\mathbf H)^{-1}&-(\mathbf M/\mathbf H)^{-1}\mathbf F\mathbf H^{-1}\\-\mathbf H^{-1}\mathbf G(\mathbf M/\mathbf H)^{-1}&\mathbf H^{-1}+\mathbf H^{-1}\mathbf G(\mathbf M/\mathbf H)^{-1}\mathbf F\mathbf H^{-1}\end{pmatrix}\tag{2.89}$$
$$=\begin{pmatrix}\mathbf E^{-1}+\mathbf E^{-1}\mathbf F(\mathbf M/\mathbf E)^{-1}\mathbf G\mathbf E^{-1}&-\mathbf E^{-1}\mathbf F(\mathbf M/\mathbf E)^{-1}\\-(\mathbf M/\mathbf E)^{-1}\mathbf G\mathbf E^{-1}&(\mathbf M/\mathbf E)^{-1}\end{pmatrix}\tag{2.90}$$
with Schur complements $\mathbf M/\mathbf H\triangleq\mathbf E-\mathbf F\mathbf H^{-1}\mathbf G$ (2.91) and $\mathbf M/\mathbf E\triangleq\mathbf H-\mathbf G\mathbf E^{-1}\mathbf F$ (2.92). The author cites [Mur22] for the proof. The author also gets the matrix inversion lemma (Sherman–Morrison–Woodbury) from the above; equating the top-left blocks of (2.89) and (2.90) shows it (added step):
$$(\mathbf M/\mathbf H)^{-1}=(\mathbf E-\mathbf F\mathbf H^{-1}\mathbf G)^{-1}=\mathbf E^{-1}+\mathbf E^{-1}\mathbf F(\mathbf H-\mathbf G\mathbf E^{-1}\mathbf F)^{-1}\mathbf G\mathbf E^{-1}\tag{2.93}$$
To derive conditioning, factor $p(\mathbf x_1,\mathbf x_2)=p(\mathbf x_1|\mathbf x_2)p(\mathbf x_2)$. Start from
$$p(\mathbf x_1,\mathbf x_2)\propto\exp\Big\{-\tfrac12\begin{pmatrix}\mathbf x_1-\boldsymbol\mu_1\\\mathbf x_2-\boldsymbol\mu_2\end{pmatrix}^{\!\top}\begin{pmatrix}\boldsymbol\Sigma_{11}&\boldsymbol\Sigma_{12}\\\boldsymbol\Sigma_{21}&\boldsymbol\Sigma_{22}\end{pmatrix}^{-1}\begin{pmatrix}\mathbf x_1-\boldsymbol\mu_1\\\mathbf x_2-\boldsymbol\mu_2\end{pmatrix}\Big\}\tag{2.94}$$
Applying the block-inverse formula splits the exponent into three matrix factors (2.95–2.96): $\begin{pmatrix}\mathbf I&\mathbf 0\\-\boldsymbol\Sigma_{22}^{-1}\boldsymbol\Sigma_{21}&\mathbf I\end{pmatrix}$, then $\mathrm{diag}\big((\boldsymbol\Sigma/\boldsymbol\Sigma_{22})^{-1},\boldsymbol\Sigma_{22}^{-1}\big)$, then $\begin{pmatrix}\mathbf I&-\boldsymbol\Sigma_{12}\boldsymbol\Sigma_{22}^{-1}\\\mathbf 0&\mathbf I\end{pmatrix}$. Multiplying out:
$$=\exp\{-\tfrac12(\mathbf x_1-\boldsymbol\mu_1-\boldsymbol\Sigma_{12}\boldsymbol\Sigma_{22}^{-1}(\mathbf x_2-\boldsymbol\mu_2))^\top(\boldsymbol\Sigma/\boldsymbol\Sigma_{22})^{-1}(\cdots)\}\times\exp\{-\tfrac12(\mathbf x_2-\boldsymbol\mu_2)^\top\boldsymbol\Sigma_{22}^{-1}(\mathbf x_2-\boldsymbol\mu_2)\}\tag{2.97–2.98}$$
This has the form exp(quadratic in $\mathbf x_1,\mathbf x_2$) × exp(quadratic in $\mathbf x_2$) (2.99). Hence $p(\mathbf x_1,\mathbf x_2)=p(\mathbf x_1|\mathbf x_2)p(\mathbf x_2)=\mathcal N(\mathbf x_1|\boldsymbol\mu_{1|2},\boldsymbol\Sigma_{1|2})\mathcal N(\mathbf x_2|\boldsymbol\mu_2,\boldsymbol\Sigma_{22})$ (2.100–2.101), with
$$\boldsymbol\mu_{1|2}=\boldsymbol\mu_1+\boldsymbol\Sigma_{12}\boldsymbol\Sigma_{22}^{-1}(\mathbf x_2-\boldsymbol\mu_2),\quad\boldsymbol\Sigma_{1|2}=\boldsymbol\Sigma/\boldsymbol\Sigma_{22}\triangleq\boldsymbol\Sigma_{11}-\boldsymbol\Sigma_{12}\boldsymbol\Sigma_{22}^{-1}\boldsymbol\Sigma_{21}\tag{2.102–2.103}$$
(p. 26–27).

**2.3.1.6 Derivation, information form (p. 27–28).** Partition $\boldsymbol\eta=(\boldsymbol\eta_1;\boldsymbol\eta_2)$ and $\boldsymbol\Lambda$ into blocks (2.104). The joint log probability is
$$\ln p(\mathbf x_1,\mathbf x_2)=-\tfrac12\mathbf x_1^\top\boldsymbol\Lambda_{11}\mathbf x_1-\tfrac12\mathbf x_2^\top\boldsymbol\Lambda_{22}\mathbf x_2-\tfrac12\mathbf x_1^\top\boldsymbol\Lambda_{12}\mathbf x_2-\tfrac12\mathbf x_2^\top\boldsymbol\Lambda_{21}\mathbf x_1+\mathbf x_1^\top\boldsymbol\eta_1+\mathbf x_2^\top\boldsymbol\eta_2+\text{const}\tag{2.105–2.106}$$
*Conditional.* Fix $\mathbf x_2$. The terms quadratic in $\mathbf x_1$ give $\boldsymbol\Lambda^c_{1|2}=\boldsymbol\Lambda_{11}$ (2.107). The linear terms are $-\frac12\mathbf x_1^\top\boldsymbol\Lambda_{12}\mathbf x_2-\frac12\mathbf x_2^\top\boldsymbol\Lambda_{21}\mathbf x_1+\mathbf x_1^\top\boldsymbol\eta_1=\mathbf x_1^\top(\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\mathbf x_2)$, using $\boldsymbol\Lambda_{21}^\top=\boldsymbol\Lambda_{12}$ (2.108). So $\boldsymbol\eta^c_{1|2}=\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\mathbf x_2$ (2.109).

*Marginal.* $p(\mathbf x_2)=\int p(\mathbf x_1,\mathbf x_2)d\mathbf x_1$ (2.110–2.111). Collecting the $\mathbf x_1$ terms:
$$p(\mathbf x_2)\propto\exp\{-\tfrac12\mathbf x_2^\top\boldsymbol\Lambda_{22}\mathbf x_2+\mathbf x_2^\top\boldsymbol\eta_2\}\int\exp\{-\tfrac12\mathbf x_1^\top\boldsymbol\Lambda_{11}\mathbf x_1+\mathbf x_1^\top(\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\mathbf x_2)\}d\mathbf x_1\tag{2.112}$$
The integral is the normalizing constant of a Gaussian with precision $\boldsymbol\Lambda_{11}$ and precision-weighted mean $\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\mathbf x_2$, i.e. the reciprocal of (2.83). Substituting:
$$p(\mathbf x_2)\propto\exp\{-\tfrac12\mathbf x_2^\top\boldsymbol\Lambda_{22}\mathbf x_2+\mathbf x_2^\top\boldsymbol\eta_2\}\exp\{\tfrac12(\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\mathbf x_2)^\top\boldsymbol\Lambda_{11}^{-1}(\boldsymbol\eta_1-\boldsymbol\Lambda_{12}\mathbf x_2)\}\tag{2.113}$$
$$\propto\exp\{-\tfrac12\mathbf x_2^\top\boldsymbol\Lambda_{22}\mathbf x_2+\mathbf x_2^\top\boldsymbol\eta_2+\tfrac12\mathbf x_2^\top\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\Lambda_{12}\mathbf x_2-\mathbf x_2^\top\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\eta_1\}\tag{2.114}$$
$$=\exp\{-\tfrac12\mathbf x_2^\top(\boldsymbol\Lambda_{22}-\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\Lambda_{12})\mathbf x_2+\mathbf x_2^\top(\boldsymbol\eta_2-\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\eta_1)\}\tag{2.115}$$
Reading off quadratic and linear terms gives $\boldsymbol\Lambda^m_{22}=\boldsymbol\Lambda_{22}-\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\Lambda_{12}$ (2.116) and $\boldsymbol\eta^m_2=\boldsymbol\eta_2-\boldsymbol\Lambda_{21}\boldsymbol\Lambda_{11}^{-1}\boldsymbol\eta_1$ (2.117) (p. 28).

*Intuition note.* In information form the exponent is "quadratic plus linear". Fixing $\mathbf x_2$ only changes the linear term, so conditioning keeps the precision $\boldsymbol\Lambda_{11}$ and shifts $\boldsymbol\eta_1$. Marginalizing in information form needs a Schur-complement-type subtraction (2.116), whereas in moment form one just reads off blocks (2.76); the author concludes marginalization is easier in moment form.

### 2.3.2 Linear Gaussian systems (p. 28–30)
Let $\mathbf y\in\mathbb R^D$, $\mathbf z\in\mathbb R^L$, $\mathbf W$ of size $D\times L$:
$$p(\mathbf z)=\mathcal N(\mathbf z|\breve{\boldsymbol\mu},\breve{\boldsymbol\Sigma}),\quad p(\mathbf y|\mathbf z)=\mathcal N(\mathbf y|\mathbf W\mathbf z+\mathbf b,\boldsymbol\Omega)\tag{2.118–2.119}$$
**2.3.2.1 Joint.** $p(\mathbf z,\mathbf y)$ is a $(D+L)$-dimensional Gaussian (obtained by moment matching), with
$$\tilde{\boldsymbol\mu}=\begin{pmatrix}\breve{\boldsymbol\mu}\\\mathbf m\end{pmatrix}=\begin{pmatrix}\breve{\boldsymbol\mu}\\\mathbf W\breve{\boldsymbol\mu}+\mathbf b\end{pmatrix},\quad\tilde{\boldsymbol\Sigma}=\begin{pmatrix}\breve{\boldsymbol\Sigma}&\mathbf C^\top\\\mathbf C&\mathbf S\end{pmatrix}=\begin{pmatrix}\breve{\boldsymbol\Sigma}&\breve{\boldsymbol\Sigma}\mathbf W^\top\\\mathbf W\breve{\boldsymbol\Sigma}&\mathbf W\breve{\boldsymbol\Sigma}\mathbf W^\top+\boldsymbol\Omega\end{pmatrix}\tag{2.120a–c}$$
**2.3.2.2 Posterior (Bayes' rule for Gaussians).** Conditioning with (2.78) gives $p(\mathbf z|\mathbf y)=\mathcal N(\mathbf z|\widehat{\boldsymbol\mu},\widehat{\boldsymbol\Sigma})$ with
$$\widehat{\boldsymbol\mu}=\breve{\boldsymbol\mu}+\breve{\boldsymbol\Sigma}\mathbf W^\top(\boldsymbol\Omega+\mathbf W\breve{\boldsymbol\Sigma}\mathbf W^\top)^{-1}(\mathbf y-(\mathbf W\breve{\boldsymbol\mu}+\mathbf b))\tag{2.121b}$$
$$\widehat{\boldsymbol\Sigma}=\breve{\boldsymbol\Sigma}-\breve{\boldsymbol\Sigma}\mathbf W^\top(\boldsymbol\Omega+\mathbf W\breve{\boldsymbol\Sigma}\mathbf W^\top)^{-1}\mathbf W\breve{\boldsymbol\Sigma}\tag{2.121c}$$
A Gaussian prior with a Gaussian likelihood gives a Gaussian posterior, so the Gaussian prior is conjugate for the Gaussian likelihood (p. 29). With $\mathbf S,\mathbf C,\mathbf m$ as in (2.120) and the Kalman gain $\mathbf K=\mathbf C\mathbf S^{-1}$ (2.122):
$$\widehat{\boldsymbol\mu}=\breve{\boldsymbol\mu}+\mathbf K(\mathbf y-\mathbf m),\quad\widehat{\boldsymbol\Sigma}=\breve{\boldsymbol\Sigma}-\mathbf K\mathbf C^\top\tag{2.123–2.124}$$
Since $\mathbf K\mathbf S\mathbf K^\top=\mathbf C\mathbf S^{-1}\mathbf S\mathbf S^{-\top}\mathbf C^\top=\mathbf C\mathbf S^{-1}\mathbf C^\top=\mathbf K\mathbf C^\top$ (2.125), also $\widehat{\boldsymbol\Sigma}=\breve{\boldsymbol\Sigma}-\mathbf K\mathbf S\mathbf K^\top$ (2.126). Using (2.93), an equivalent form costs $O(L^3)$ instead of $O(D^3)$:
$$\widehat{\boldsymbol\Sigma}=(\breve{\boldsymbol\Sigma}^{-1}+\mathbf W^\top\boldsymbol\Omega^{-1}\mathbf W)^{-1},\quad\widehat{\boldsymbol\mu}=\widehat{\boldsymbol\Sigma}[\mathbf W^\top\boldsymbol\Omega^{-1}(\mathbf y-\mathbf b)+\breve{\boldsymbol\Sigma}^{-1}\breve{\boldsymbol\mu}]\tag{2.127–2.128}$$
The posterior's normalizing constant is the marginal of $\mathbf y$ at the observed value:
$$p(\mathbf y)=\int\mathcal N(\mathbf z|\breve{\boldsymbol\mu},\breve{\boldsymbol\Sigma})\mathcal N(\mathbf y|\mathbf W\mathbf z+\mathbf b,\boldsymbol\Omega)d\mathbf z=\mathcal N(\mathbf y|\mathbf W\breve{\boldsymbol\mu}+\mathbf b,\boldsymbol\Omega+\mathbf W\breve{\boldsymbol\Sigma}\mathbf W^\top)=\mathcal N(\mathbf y|\mathbf m,\mathbf S)\tag{2.129}$$
This gives the log marginal likelihood (p. 29).

*Intuition note.* The gain $\mathbf K$ says how much of the surprise $\mathbf y-\mathbf m$ to move the mean by. In the precision form (2.127), prior precision and data precision simply add.

**2.3.2.3 Sensor fusion (p. 30).** Take unknown $\mathbf z\sim\mathcal N(\boldsymbol\mu_z,\boldsymbol\Sigma_z)$ with two noisy measurements $\mathbf x\sim\mathcal N(\mathbf z,\boldsymbol\Sigma_x)$, $\mathbf y\sim\mathcal N(\mathbf z,\boldsymbol\Sigma_y)$, with $\boldsymbol\theta=(\boldsymbol\Sigma_x,\boldsymbol\Sigma_y)$ known. Stack $\mathbf v=(\mathbf x,\mathbf y)$. Then $p(\mathbf v|\mathbf z)=\mathcal N(\mathbf v|\mathbf W\mathbf z,\boldsymbol\Sigma_v)$ with $\mathbf W=[\mathbf I;\mathbf I]$ and $\boldsymbol\Sigma_v=[\boldsymbol\Sigma_x,\mathbf 0;\mathbf 0,\boldsymbol\Sigma_y]$. Apply Bayes' rule for Gaussians. Fig. 2.10 uses observations $\mathbf x=(0,-1)$ and $\mathbf y=(1,0)$:
- (a) $\boldsymbol\Sigma_x=\boldsymbol\Sigma_y=0.01\mathbf I_2$: the posterior mean is halfway between $\mathbf x$ and $\mathbf y$.
- (b) $\boldsymbol\Sigma_x=0.05\mathbf I_2$, $\boldsymbol\Sigma_y=0.01\mathbf I_2$: the mean is closer to $\mathbf y$.
- (c) $\boldsymbol\Sigma_x=0.01\begin{pmatrix}10&1\\1&1\end{pmatrix}$, $\boldsymbol\Sigma_y=0.01\begin{pmatrix}1&1\\1&10\end{pmatrix}$ (2.130): sensor 1 is more reliable vertically and sensor 2 horizontally. The mean is vertically closer to $\mathbf x$ and horizontally closer to $\mathbf y$.

### 2.3.3 A general calculus for linear Gaussian systems (p. 30–33)
Joint distributions are represented as potential functions in information form. Rules for marginalizing, multiplying, dividing and conditioning can then be used inside belief propagation or the junction tree algorithm (p. 30).

**2.3.3.1 Parameterizations (p. 31).** Moment form is $\phi(\mathbf x;p,\boldsymbol\mu,\boldsymbol\Sigma)=p\exp(-\frac12(\mathbf x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf x-\boldsymbol\mu))$ with $p=(2\pi)^{-n/2}|\boldsymbol\Sigma|^{-1/2}$ (2.131). Canonical form:
$$\phi(\mathbf x;g,\mathbf h,\mathbf K)=\exp\big(g+\mathbf x^\top\mathbf h-\tfrac12\mathbf x^\top\mathbf K\mathbf x\big)\tag{2.132}$$
$$\mathbf K=\boldsymbol\Sigma^{-1},\quad\mathbf h=\boldsymbol\Sigma^{-1}\boldsymbol\mu,\quad g=\log p-\tfrac12\boldsymbol\mu^\top\mathbf K\boldsymbol\mu\tag{2.133–2.135}$$
Potentials need not be normalizable. The constants $p$ or $g$ are kept so that the likelihood of the evidence can be computed (p. 31).

**2.3.3.2 Multiplication, division (p. 31).** After extending both potentials to the same domain by adding zeros,
$$(g_1,\mathbf h_1,\mathbf K_1)*(g_2,\mathbf h_2,\mathbf K_2)=(g_1+g_2,\mathbf h_1+\mathbf h_2,\mathbf K_1+\mathbf K_2)\tag{2.136}$$
and division subtracts componentwise (2.137).

**2.3.3.3 Marginalization (p. 31–32).** For $\mathbf x=(\mathbf x_1;\mathbf x_2)$ with dimensions $n_1,n_2$, and $\mathbf h,\mathbf K$ partitioned as in (2.138),
$$\int_{\mathbf x_1}\phi(\mathbf x_1,\mathbf x_2;g,\mathbf h,\mathbf K)=\phi(\mathbf x_2;\hat g,\hat{\mathbf h},\hat{\mathbf K})\tag{2.139}$$
$$\hat g=g+\tfrac12\big(n_1\log(2\pi)-\log|\mathbf K_{11}|+\mathbf h_1^\top\mathbf K_{11}^{-1}\mathbf h_1\big),\ \hat{\mathbf h}=\mathbf h_2-\mathbf K_{21}\mathbf K_{11}^{-1}\mathbf h_1,\ \hat{\mathbf K}=\mathbf K_{22}-\mathbf K_{21}\mathbf K_{11}^{-1}\mathbf K_{12}\tag{2.140–2.142}$$
**2.3.3.4 Conditioning on evidence (p. 32).** Observing $\mathbf y$ in a potential over $(\mathbf x,\mathbf y)$ gives a reduced potential:
$$\phi^*(\mathbf x)=\exp\Big[\big(g+\mathbf h_Y^\top\mathbf y-\tfrac12\mathbf y^\top\mathbf K_{YY}\mathbf y\big)+\mathbf x^\top(\mathbf h_X-\mathbf K_{XY}\mathbf y)-\tfrac12\mathbf x^\top\mathbf K_{XX}\mathbf x\Big]\tag{2.143–2.144}$$
**2.3.3.5 Linear-Gaussian CPD as a potential (p. 32–33).** A node with $p(\mathbf x|\mathbf u)=c\exp[-\frac12(\mathbf x-\boldsymbol\mu-\mathbf B^\top\mathbf u)^\top\boldsymbol\Sigma^{-1}(\mathbf x-\boldsymbol\mu-\mathbf B^\top\mathbf u)]$, $c=(2\pi)^{-n/2}|\boldsymbol\Sigma|^{-1/2}$ (2.145–2.147), has canonical parameters
$$g=-\tfrac12\boldsymbol\mu^\top\boldsymbol\Sigma^{-1}\boldsymbol\mu-\tfrac n2\log(2\pi)-\tfrac12\log|\boldsymbol\Sigma|,\ \mathbf h=\begin{pmatrix}\boldsymbol\Sigma^{-1}\boldsymbol\mu\\-\mathbf B\boldsymbol\Sigma^{-1}\boldsymbol\mu\end{pmatrix},\ \mathbf K=\begin{pmatrix}\boldsymbol\Sigma^{-1}&-\boldsymbol\Sigma^{-1}\mathbf B^\top\\-\mathbf B\boldsymbol\Sigma^{-1}&\mathbf B\boldsymbol\Sigma^{-1}\mathbf B^\top\end{pmatrix}=\begin{pmatrix}\mathbf I\\-\mathbf B\end{pmatrix}\boldsymbol\Sigma^{-1}\begin{pmatrix}\mathbf I&-\mathbf B\end{pmatrix}\tag{2.148–2.150}$$
For scalar $x$ ($\Sigma^{-1}=1/\sigma^2$, $\mathbf B=\mathbf b$, $n=1$): $g=-\mu^2/(2\sigma^2)-\frac12\log(2\pi\sigma^2)$, $\mathbf h=\frac{\mu}{\sigma^2}\binom{1}{-\mathbf b}$ (2.151–2.152), and $\mathbf K$ as printed in (2.153) (see Reading notes) (p. 33).

**2.3.3.6 Product of Gaussians (p. 33).**
$$\mathcal N(\mathbf x|\boldsymbol\mu_1,\boldsymbol\Sigma_1)\times\mathcal N(\mathbf x|\boldsymbol\mu_2,\boldsymbol\Sigma_2)\propto\mathcal N(\mathbf x|\boldsymbol\mu_3,\boldsymbol\Sigma_3)\tag{2.154}$$
$$\boldsymbol\Sigma_3=(\boldsymbol\Sigma_1^{-1}+\boldsymbol\Sigma_2^{-1})^{-1},\quad\boldsymbol\mu_3=\boldsymbol\Sigma_3(\boldsymbol\Sigma_1^{-1}\boldsymbol\mu_1+\boldsymbol\Sigma_2^{-1}\boldsymbol\mu_2)\tag{2.155–2.156}$$
Precisions add, and the mean is a precision-weighted combination of the means. A one-inversion form is $\boldsymbol\Sigma_3=\boldsymbol\Sigma_1(\boldsymbol\Sigma_1+\boldsymbol\Sigma_2)^{-1}\boldsymbol\Sigma_2$, $\boldsymbol\mu_3=\boldsymbol\Sigma_2(\boldsymbol\Sigma_1+\boldsymbol\Sigma_2)^{-1}\boldsymbol\mu_1+\boldsymbol\Sigma_1(\boldsymbol\Sigma_1+\boldsymbol\Sigma_2)^{-1}\boldsymbol\mu_2$ (2.157–2.158). In the scalar case:
$$\mathcal N(x|\mu_1,\sigma_1^2)\mathcal N(x|\mu_2,\sigma_2^2)\propto\mathcal N\Big(x\Big|\frac{\mu_1\sigma_2^2+\mu_2\sigma_1^2}{\sigma_1^2+\sigma_2^2},\frac{\sigma_1^2\sigma_2^2}{\sigma_1^2+\sigma_2^2}\Big)\tag{2.159}$$

### 2.4 The exponential family (p. 33–34)
The author gives these reasons for its importance:
- It is the unique family with maximum entropy subject to user-chosen constraints (Section 2.4.7).
- It is at the core of GLMs and of variational inference.
- Under certain regularity conditions it is the only family with finite-sized sufficient statistics (Section 2.4.5).
- All members have a conjugate prior (p. 33–34).

**2.4.1 Definition (p. 34).** For $\boldsymbol\eta\in\mathbb R^K$ and fixed support in $\mathcal X^D\subseteq\mathbb R^D$:
$$p(\mathbf x|\boldsymbol\eta)\triangleq\frac{1}{Z(\boldsymbol\eta)}h(\mathbf x)\exp[\boldsymbol\eta^\top\mathcal T(\mathbf x)]=h(\mathbf x)\exp[\boldsymbol\eta^\top\mathcal T(\mathbf x)-A(\boldsymbol\eta)]\tag{2.160}$$
Here $h$ is the base measure, $\mathcal T(\mathbf x)\in\mathbb R^K$ the sufficient statistics, $\boldsymbol\eta$ the natural (canonical) parameters, $Z$ the partition function and $A=\log Z$ the log partition function. The author says Section 2.4.3 shows that $A$ is convex on $\Omega\triangleq\{\boldsymbol\eta:A(\boldsymbol\eta)<\infty\}$ (p. 34). The family is *minimal* if no $\boldsymbol\eta\neq\mathbf 0$ has $\boldsymbol\eta^\top\mathcal T(\mathbf x)=0$. Multinomial parameters with a sum-to-one constraint can violate this, but can be reparameterized with $K-1$ parameters. With $\boldsymbol\eta=f(\boldsymbol\phi)$:
$$p(\mathbf x|\boldsymbol\phi)=h(\mathbf x)\exp[f(\boldsymbol\phi)^\top\mathcal T(\mathbf x)-A(f(\boldsymbol\phi))]\tag{2.161}$$
This is a *curved* exponential family if $f$ is nonlinear. It is in canonical form if $\boldsymbol\eta=\boldsymbol\phi$. It is a natural exponential family (NEF) if also $\mathcal T(\mathbf x)=\mathbf x$, giving $h(\mathbf x)\exp[\boldsymbol\eta^\top\mathbf x-A(\boldsymbol\eta)]$ (2.162). The moment parameters are $\mathbf m=\mathbb E[\mathcal T(\mathbf x)]$ (2.163) (p. 34).

**2.4.2 Examples (p. 35–39).**
- *Bernoulli.* $\mathrm{Ber}(x|\mu)=\mu^x(1-\mu)^{1-x}=\exp[\mathcal T(x)^\top\boldsymbol\eta]$ with $\mathcal T=[\mathbb I(x=1),\mathbb I(x=0)]$ and $\boldsymbol\eta=[\log\mu,\log(1-\mu)]$ (2.164–2.166). This is over-complete: $\mathbf 1^\top\mathcal T(x)=1$ (2.167), so $\boldsymbol\eta$ is not uniquely identifiable. The minimal form (2.168) is $\exp[x\log\frac{\mu}{1-\mu}+\log(1-\mu)]$, with $\eta=\log\frac{\mu}{1-\mu}$, $\mathcal T(x)=x$, $A(\eta)=-\log(1-\mu)=\log(1+e^\eta)$, $h=1$ (2.169–2.172). Then $\mu=\sigma(\eta)=1/(1+e^{-\eta})$ (2.173) (p. 35).
- *Categorical.* With $x_k=\mathbb I(x=k)$ and $\mu_K=1-\sum_{k<K}\mu_k$, the product $\prod_k\mu_k^{x_k}$ is rewritten step by step (2.174–2.177) as $\exp[\sum_{k=1}^{K-1}x_k\log(\mu_k/\mu_K)+\log\mu_K]$. So $\eta_k=\log(\mu_k/\mu_K)$, $A(\boldsymbol\eta)=-\log\mu_K$, $\mathcal T=[\mathbb I(x=1),\dots,\mathbb I(x=K-1)]$, $h=1$ (2.178–2.182). Inverting gives $\mu_k=e^{\eta_k}/(1+\sum_{j<K}e^{\eta_j})$ (2.183). Defining $\eta_K=0$, $\boldsymbol\mu=\mathrm{softmax}(\boldsymbol\eta)$ (2.184). Then $\mu_K=1/(1+\sum_{k<K}e^{\eta_k})$ (2.185) and $A(\boldsymbol\eta)=\log\sum_{k=1}^Ke^{\eta_k}$ (2.186) (p. 36).
- *Univariate Gaussian.* Starting from (2.187–2.188): $\boldsymbol\eta=(\mu/\sigma^2,\,-1/(2\sigma^2))$, $\mathcal T(x)=(x,x^2)$, $A(\boldsymbol\eta)=\frac{\mu^2}{2\sigma^2}+\log\sigma=\frac{-\eta_1^2}{4\eta_2}-\frac12\log(-2\eta_2)$, $h(x)=1/\sqrt{2\pi}$ (2.189–2.192). The moment parameters are $\mathbf m=[\mu,\mu^2+\sigma^2]$ (2.193) (p. 37).
- *Fixed variance $\sigma^2=1$.* This is a NEF with $\eta=\mu$, $\mathcal T=x$, $A=\mu^2/2$, $h(x)=\frac{1}{\sqrt{2\pi}}e^{-x^2/2}=\mathcal N(x|0,1)$ (2.194–2.197). Here the base measure is not constant (p. 37).
- *MVN.* Canonical parameters $\boldsymbol\Lambda=\boldsymbol\Sigma^{-1}$, $\boldsymbol\xi=\boldsymbol\Sigma^{-1}\boldsymbol\mu$ (2.201–2.204), the same information form as (2.80–2.83). Rewriting (2.205–2.209) gives $h(\mathbf x)=(2\pi)^{-D/2}$, $\boldsymbol\eta=[\boldsymbol\xi;-\frac12\mathrm{vec}(\boldsymbol\Lambda)]$, $\mathcal T(\mathbf x)=[\mathbf x;\mathrm{vec}(\mathbf x\mathbf x^\top)]$, $A(\boldsymbol\eta)=-\frac12\log|\boldsymbol\Lambda|+\frac12\boldsymbol\xi^\top\boldsymbol\Lambda^{-1}\boldsymbol\xi$ (2.210–2.213). Moments: $\mathbf m=[\boldsymbol\mu;\boldsymbol\mu\boldsymbol\mu^\top+\boldsymbol\Sigma]$ (2.214). This is not minimal, since $\boldsymbol\Lambda$ is symmetric (p. 38–39).
- *Non-examples (p. 39).* The Student distribution does not have the required form. The uniform $\mathrm{Unif}(\theta_1,\theta_2)$ looks like it fits ($h=1$, $\mathcal T=0$, $Z=\theta_2-\theta_1$), but its support depends on $\boldsymbol\theta$, which violates an assumption of the family.

**2.4.3 Log partition function is the cumulant generating function (p. 39–40).** Cumulants 1 and 2 are the mean and variance. The claim is
$$\nabla_{\boldsymbol\eta}A(\boldsymbol\eta)=\mathbb E[\mathcal T(\mathbf x)],\quad\nabla^2_{\boldsymbol\eta}A(\boldsymbol\eta)=\mathrm{Cov}[\mathcal T(\mathbf x)]\tag{2.216–2.217}$$
*Mean (1d).*
$$\frac{dA}{d\eta}=\frac{d}{d\eta}\log\int\exp(\eta\mathcal T(x))h(x)dx=\frac{\int\mathcal T(x)\exp(\eta\mathcal T(x))h(x)dx}{\exp(A(\eta))}=\int\mathcal T(x)\exp(\eta\mathcal T(x)-A(\eta))h(x)dx=\mathbb E[\mathcal T(x)]\tag{2.218–2.222}$$
Bernoulli check: $A=\log(1+e^\eta)$ gives $dA/d\eta=e^\eta/(1+e^\eta)=\sigma(\eta)=\mu$ (2.223).
*Variance (1d).* Differentiating (2.221) once more, the product rule gives $\mathcal T(x)\exp(\eta\mathcal T-A)h\,(\mathcal T(x)-A'(\eta))$, so
$$\frac{d^2A}{d\eta^2}=\int\mathcal T(x)p(x)(\mathcal T(x)-A'(\eta))dx=\mathbb E[\mathcal T^2]-A'(\eta)\,\mathbb E[\mathcal T]=\mathbb E[\mathcal T^2]-\mathbb E[\mathcal T]^2=\mathbb V[\mathcal T(x)]\tag{2.224–2.228}$$
using $A'=\mathbb E[\mathcal T]$. Bernoulli check: $\frac{d^2A}{d\eta^2}=(1+e^{-\eta})^{-2}e^{-\eta}=\mu(1-\mu)$ (2.229–2.230) (p. 40).

**2.4.3.3 Fisher information (p. 41).** Under regularity conditions (shown in Section 3.3.4), $\mathbf F(\boldsymbol\eta)=\mathbb E[\nabla\log p\,\nabla\log p^\top]=-\mathbb E[\nabla^2\log p]$ (2.231). For the exponential family, $\mathbf F(\boldsymbol\eta)=-\mathbb E[\nabla^2_{\boldsymbol\eta}(\boldsymbol\eta^\top\mathcal T-A)]=\nabla^2A=\mathrm{Cov}[\mathcal T(\mathbf x)]$ (2.232).

*Intuition note.* $A$ is the log of the normalizer. Differentiating it brings down $\mathcal T$ inside the integral, so slopes of $A$ are averages of $\mathcal T$ and its curvature is their spread. This spread is also how sharply the log-likelihood bends.

**2.4.4 Natural vs moment parameters (p. 41).** $\Omega\triangleq\{\boldsymbol\eta:Z(\boldsymbol\eta)<\infty\}$ (2.233). The family is *regular* if $\Omega$ is open. $\Omega$ is convex and $A$ is convex on it. The valid moment parameters are $\mathcal M=\{\mathbf m:\mathbb E_p[\mathcal T]=\mathbf m\text{ for some }p\}$ (2.235), and $\mathbf m=\nabla_{\boldsymbol\eta}A(\boldsymbol\eta)$ (2.234, 2.236). If the family is minimal, $\boldsymbol\eta=\nabla_{\mathbf m}A^*(\mathbf m)$ (2.237), where $A^*$ is the convex conjugate $A^*(\mathbf m)\triangleq\sup_{\boldsymbol\eta\in\Omega}\boldsymbol\mu^\top\boldsymbol\eta-A(\boldsymbol\eta)$ (2.238). So $(\nabla A,\nabla A^*)$ converts between $\boldsymbol\eta$ and $\mathbf m$. Bregman divergences of $A$ and $A^*$ are noted for later (2.239–2.240) (Section 5.1.10 is not in this part).

**2.4.5 MLE (p. 42).** For $N$ data points, $p(\mathcal D|\boldsymbol\eta)=[\prod_nh(\mathbf x_n)]\exp(\boldsymbol\eta^\top[\sum_n\mathcal T(\mathbf x_n)]-NA(\boldsymbol\eta))\propto\exp[\boldsymbol\eta^\top\mathcal T(\mathcal D)-NA(\boldsymbol\eta)]$ (2.242), where $\mathcal T(\mathcal D)=[\sum_n\mathcal T_1(\mathbf x_n),\dots,\sum_n\mathcal T_K(\mathbf x_n)]$ (2.243). For the Bernoulli, $\mathcal T(\mathcal D)=[\sum_n\mathbb I(x_n=1)]$. For the univariate Gaussian, $\mathcal T(\mathcal D)=[\sum_nx_n,\sum_nx_n^2]$. The Pitman–Koopman–Darmois theorem states that, under certain regularity conditions, the exponential family is the only family with finite sufficient statistics (size independent of dataset size), so $p(\mathcal D|\boldsymbol\eta)=p(\mathcal T(\mathcal D)|\boldsymbol\eta)$ (2.244). The log-likelihood is $\boldsymbol\eta^\top\mathcal T(\mathcal D)-NA(\boldsymbol\eta)+\text{const}$ (2.245). It is concave (linear term plus $-A$ concave), "and hence has a unique global maximum" (p. 42). The gradient is
$$\nabla_{\boldsymbol\eta}\log p(\mathcal D|\boldsymbol\eta)=\mathcal T(\mathcal D)-N\,\mathbb E[\mathcal T(\mathbf x)]\tag{2.246}$$
(single case: $\mathcal T(\mathbf x)-\mathbb E[\mathcal T(\mathbf x)]$, 2.247). Setting it to zero gives *moment matching*:
$$\mathbb E[\mathcal T(\mathbf x)]=\frac1N\sum_{n=1}^N\mathcal T(\mathbf x_n)\tag{2.248}$$
For the Bernoulli this reads $\mu=\frac1N\sum_n\mathbb I(x_n=1)$ (2.249).

**2.4.6 Exponential dispersion family (p. 43).** For a scalar, $p(x|\eta,\sigma^2)=h(x,\sigma^2)\exp[(\eta x-A(\eta))/\sigma^2]$ (2.250). $\sigma^2$ is the dispersion parameter. For fixed $\sigma^2$ this is a NEF. It is needed for GLMs (Section 15.1).

**2.4.7 Maximum-entropy derivation (begins, p. 43).** Suppose only feature expectations are known: $\int d\mathbf x\,p(\mathbf x)f_k(\mathbf x)=F_k$ (2.251), with prior belief $q(\mathbf x)$. "Fewest assumptions" is formalized as the distribution closest to $q$ in KL divergence satisfying the constraints. With a uniform prior this equals maximizing entropy (a maximum entropy model). The Lagrangian, with $\sum_xp=1$, $p\ge0$ and the constraints, is
$$J(p,\boldsymbol\lambda)=-\sum_xp(x)\log\frac{p(x)}{q(x)}+\lambda_0\Big(1-\sum_xp(x)\Big)+\sum_k\lambda_k\Big(F_k-\sum_xp(x)f_k(x)\Big)\tag{2.252}$$
Treating $p$ as a vector (discrete $x$): $\partial J/\partial p_c=-1-\log\frac{p(x=c)}{q(x=c)}-\lambda_0-\sum_k\lambda_kf_k(x=c)$ (2.253). Setting it to 0 gives
$$p(\mathbf x)=\frac{q(\mathbf x)}{Z}\exp\Big(-\sum_k\lambda_kf_k(\mathbf x)\Big),\quad Z\triangleq e^{1+\lambda_0}\tag{2.254}$$
The sum-to-one constraint gives $1=\frac1Z\sum_xq(x)\exp(-\sum_k\lambda_kf_k(x))$ (2.255). The text of this unit stops here.

## Toy example (ours, not from the text)
**Gaussian update.** Take scalar $z\sim\mathcal N(0,4)$, so $\breve\mu=0$, $\breve\Sigma=4$. Let $y|z\sim\mathcal N(z,1)$, so $W=1$, $b=0$, $\Omega=1$. Observe $y=5$.
- $S=W\breve\Sigma W+\Omega=4+1=5$ and $C=\breve\Sigma W=4$, so $K=C/S=0.8$ (2.122).
- $m=W\breve\mu+b=0$, so $\hat\mu=0+0.8\,(5-0)=4$ (2.123).
- $\hat\Sigma=4-KC=4-0.8\times4=0.8$ (2.124).
- Check with the precision form (2.127–2.128): $\hat\Sigma=(1/4+1\cdot1\cdot1)^{-1}=0.8$ and $\hat\mu=0.8\,[1\cdot1\cdot5+0.25\cdot0]=4$. ✓
- The marginal is $p(y)=\mathcal N(y|0,5)$ (2.129).

**Bernoulli cumulants.** For $\mu=0.75$: $\eta=\log(0.75/0.25)=\log3$ and $A=\log(1+3)=\log4$. $A'=3/4=\mu$ (2.223). $A''=\sigma(\eta)(1-\sigma(\eta))=0.75\times0.25=3/16$, the Bernoulli variance (2.230).

## Concepts
- [[multivariate-normal]] — joint Gaussian density (2.71), defined by mean vector and covariance matrix (new) (p. 22)
- [[mahalanobis-distance]] — $(\mathbf x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\mathbf x-\boldsymbol\mu)$, the quadratic form inside the Gaussian (new) (p. 22)
- [[typical-set]] — here, the thin shell of radius about $\sigma\sqrt D$ holding most Gaussian mass (p. 23)
- [[information-form]] — Gaussian parameterized by precision $\boldsymbol\Lambda$ and precision-weighted mean (new) (p. 25)
- [[schur-complement]] — $\mathbf M/\mathbf H=\mathbf E-\mathbf F\mathbf H^{-1}\mathbf G$, appears in block inverses and conditional covariances (new) (p. 26)
- [[linear-gaussian-system]] — Gaussian $p(\mathbf z)$ with $p(\mathbf y|\mathbf z)=\mathcal N(\mathbf W\mathbf z+\mathbf b,\boldsymbol\Omega)$ (new) (p. 28)
- [[conjugate-prior]] — Gaussian prior with Gaussian likelihood gives a Gaussian posterior (p. 29)
- [[marginal-likelihood]] — $p(\mathbf y)=\mathcal N(\mathbf y|\mathbf m,\mathbf S)$, the posterior's normalizing constant (p. 29)
- [[kalman-gain]] — $\mathbf K=\mathbf C\mathbf S^{-1}$, which scales the correction to the mean (new) (p. 29)
- [[sensor-fusion]] — combining several noisy measurements of one quantity by Bayes' rule for Gaussians (new) (p. 30)
- [[exponential-family]] — densities $h(\mathbf x)\exp[\boldsymbol\eta^\top\mathcal T(\mathbf x)-A(\boldsymbol\eta)]$ (new) (p. 34)
- [[log-partition-function]] — $A(\boldsymbol\eta)=\log Z(\boldsymbol\eta)$; its derivatives give moments of $\mathcal T$ (new) (p. 34, 39)
- [[moment-matching]] — at the MLE, model expectation of $\mathcal T$ equals the empirical average (new) (p. 42)
- [[fisher-information]] — equals $\nabla^2A=\mathrm{Cov}[\mathcal T]$ in this family (new) (p. 41)
- [[maximum-entropy]] — closest distribution to prior $q$ in KL under feature-expectation constraints; with a uniform prior this is maximizing entropy (p. 43)
- [[kl-divergence]] — closeness measure used in the max-entropy derivation (p. 43)

## Canonical instances
- [[gaussian-soap-bubble]] — high-dimensional Gaussian samples lie in a thin shell (p. 23)
- [[sensor-fusion-2d]] — two sensors with different noise matrices, with the posterior mean shifting toward the more reliable one (p. 30)
- [[bernoulli-as-exponential-family]] — logit natural parameter, sigmoid mean, $A=\log(1+e^\eta)$ (p. 35)
- [[categorical-softmax]] — softmax from the exponential-family form of the categorical (p. 36)
- [[uniform-non-example]] — parameter-dependent support excludes it from the family (p. 39)

## Bridges (candidates)
- [structural-analogy] Kalman gain update (2.123–2.124) ↔ filtering: the text says the gain's name comes from the Kalman filter (Section 8.2.2)
- [same-math] Bernoulli/categorical mean from natural parameters (2.173, 2.184) ↔ machine learning: logistic and softmax functions
- [structural-analogy] Precision-weighted combination of means (2.156) ↔ cue combination: weighting each source by its reliability
- [structural-analogy] Partition function $Z$, $A=\log Z$ ↔ statistical physics: normalizers of exponentially weighted distributions (the text only uses the name)

## Questions this raises
- How does the Gaussian shell phenomenon affect sampling and inference in high dimensions (Section 5.2.3 on typical sets)?
- What do the exponential-family conjugate priors look like (Section 3.4), and why does every member have one?
- Does the max-entropy derivation, once finished, produce $\lambda_k$ equal to natural parameters, and what are the Gaussian constraints?
- When would the $O(L^3)$ posterior form (2.127–2.128) be preferred over the Kalman-gain form?

## Reading notes
- This part starts at p. 22 with Fig. 2.7 (end of the Dirichlet discussion) and ends at p. 43 mid-derivation of Section 2.4.7, at Eq. (2.255). Printed page = pdf − 34.
- **Cross-reference:** 2.3.1.5 says it derives "(2.77) and (2.78)". The marginals are (2.76)–(2.77); only the conditional and $p(\mathbf x_2)$ appear in the derivation. 2.3.1.6 says it derives (2.85) and (2.86), which matches.
- **Eq. (2.153):** the page prints $\mathbf K=\frac1\sigma(\cdots)$, while the text says $\Sigma^{-1}=1/\sigma^2$, which would suggest $1/\sigma^2$.
- **Variance of $d^2$:** p. 23 states $\mathbb V[d^2]=\sum_i\mathbb V[x_i^2]=D$. For a standard normal, $\mathbb V[x_i^2]$ is 2, so $\mathbb V[d^2]$ would be $2D$ (my check, not in the source). The limit in (2.74) is still 0.
- **Eqs. (2.238)–(2.241):** (2.238) uses $\boldsymbol\mu^\top\boldsymbol\eta$ for the conjugate, where $\mathbf m$ is meant. (2.240) prints $A$ where $A^*$ is meant for $B_{A^*}$. (2.241) has a number but no content. p. 34 says Section 2.4.3 shows that $A$ is convex, but Section 2.4.3 (p. 39–40) derives only the mean and variance formulas and does not state convexity explicitly.
- Text-layer symbols were garbled in places (breve/hat marks). I checked them against the page images.
