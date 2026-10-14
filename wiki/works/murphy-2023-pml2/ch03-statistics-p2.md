---
id: murphy-2023-pml2/ch03-statistics-p2
work: murphy-2023-pml2
unit: "3 Statistics (part 2/3): §3.4 conjugate priors, §3.5 noninformative priors, §3.6 hierarchical priors (start)"
pages: 83-113
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Conjugate, noninformative and hierarchical priors (Murphy, Ch. 3, part 2)

## L0 — One line
When the prior is conjugate to the likelihood, Bayesian updating is just adding data statistics to prior "virtual" counts; where that fails, one uses default, robust or hierarchical priors, and hierarchical models make groups share strength through shrinkage.

## L1 — The gist (≤ 120 words)
How can we compute posteriors in closed form, and how should we choose priors when we know little? Murphy derives conjugate updates for categorical, Gaussian (scalar and multivariate) and general exponential-family models. He then covers priors beyond conjugacy: mixtures, heavy-tailed priors, and priors for variances and covariances. Next come noninformative priors: maximum entropy, Jeffreys, invariant and reference priors. Finally, hierarchical models learn the prior's hyperparameters from many related groups. Small groups are then pulled toward the population mean (shrinkage). Examples are the rats tumour data and the eight schools data. This matters because conjugate updates are building blocks for harder models, and priors on variances help determine how much regularization a model has.

**Prerequisites:** Bayes' rule; exponential family and sufficient statistics; Gaussian, Beta, Dirichlet densities; Fisher information; matrix trace and determinant; change of variables.

## L2 — Key ideas (5–10 bullets)
- A prior family is conjugate if the posterior stays in the same family; for exponential families the update is closed-form: add $s(\mathcal D)$ and $N$ to prior statistics (pp. 83–84, 97).
- Dirichlet–categorical: posterior parameters equal prior pseudo-counts plus observed counts (p. 84).
- Gaussian models (known variance): posterior precision is prior precision plus data precision, and the posterior mean is a convex combination of prior mean and sample mean. This is shrinkage (pp. 85–86).
- Unknown mean and variance use the NIX (normal-inverse-chi-squared, scalar) or NIW (normal-inverse-Wishart, matrix) conjugate prior. The marginal posterior of the mean is Student-$t$, and with the default (Jeffreys-type) prior the approximate 95% credible interval is $\bar y \pm 2s/\sqrt N$ (pp. 88–95).
- Beyond conjugacy: mixtures of conjugate priors stay conjugate, heavy-tailed priors tend to be more sensitive to the data, and for variances and covariances the text discusses half-distributions bounded below by 0 and the LKJ correlation prior, because improper or heavy-tailed choices can cause problems (pp. 99–102).
- "Noninformative" priors always encode something. Maximum entropy, Jeffreys (built from Fisher information; parameterization-invariant), translation/scale-invariant and reference priors (maximizing expected KL between posterior and prior) are different default choices (pp. 102–107).
- Hierarchical models treat group parameters as draws from a population distribution. Small groups borrow statistical strength, with the amount of shrinkage inferred from data (pp. 108–112).
- In the eight-schools model, $\tau^2$ and the $\theta_j$ depend tightly on each other (a funnel shape), which makes inference hard for many algorithms; a standard fix is the non-centered parameterization $\theta_j=\mu+\tau\eta_j$ (p. 113).

## L3 — Walkthrough

### Opening (end of preceding section, p. 83)
The unit starts inside a quoted passage; it is a quoted earlier author, whose name these pages do not give. It says everyone used to be Bayesian, that modern statisticians (following Savage and de Finetti) argue for Bayes, yet 20th-century statistics was mainly non-Bayesian; Lindley (1975) predicts change (p. 83).

**Murphy's comments:**
- Computation, once a barrier, is less of an issue (p. 83).
- The Bayesian approach is only as correct as its modelling assumptions, so check sensitivity to prior and likelihood, e.g. by Bayesian model checking (Sec. 3.9.1) (p. 83).
- **Rubin (quoted):** be Bayesian in principle and calibrated to the real world in practice; avoid models contradicted by data (p. 83).
- Practitioners often use "cookie cutter" tests ($t$, $\chi^2$). Simple Bayesian alternatives exist (Sec. 3.10), and empirical Bayes can give data-conditional methods with good frequentist properties (p. 83).

### 3.4 Conjugate priors
**Definition.** A prior $p(\theta)\in\mathcal F$ is conjugate to $p(\mathcal D|\theta)$ if $p(\theta|\mathcal D)\in\mathcal F$, i.e. $\mathcal F$ is closed under Bayesian updating. If $\mathcal F$ is an exponential family, computations are closed-form. In harder settings these results can be tractable subroutines (pp. 83–84).

**3.4.1** The beta–binomial model is in Sec. 3.2.1 (p. 84).

**3.4.2 Multinomial model.** Categorical likelihood, with $N_c=\sum_n \mathbb I(y_n=c)$ and $C$ categories:
$$p(\mathcal D|\boldsymbol\theta)=\prod_{n=1}^N\prod_{c=1}^C\theta_c^{\mathbb I(y_n=c)}=\prod_{c=1}^C\theta_c^{N_c}\tag{3.89}$$
The multinomial $\mathbf y\sim\mathcal M(N,\boldsymbol\theta)$ ($y_c=N_c$) has
$$p(\mathbf y|N,\boldsymbol\theta)=\binom{N}{N_1\ldots N_C}\prod_{c}\theta_c^{N_c}\tag{3.90}$$
The two likelihoods differ only by a scaling factor; the text uses the categorical one (p. 84).

The conjugate prior is $\mathrm{Dir}(\boldsymbol\theta|\breve{\boldsymbol\alpha})$, where $\breve{\boldsymbol\alpha}$ is a vector of prior pseudo-counts. For the symmetric choice $\breve\alpha_k=\breve\alpha/K$: $\mathbb E[\theta_k]=1/K$ and $\mathbb V[\theta_k]=\frac{K-1}{K^2(\breve\alpha+1)}$. A larger prior sample size $\breve\alpha$ means smaller prior variance, i.e. a stronger prior (p. 84).

Posterior:
$$p(\boldsymbol\theta|\mathcal D)\propto\Big[\prod_k\theta_k^{N_k}\Big]\Big[\prod_k\theta_k^{\breve\alpha_k-1}\Big]\propto\mathrm{Dir}(\boldsymbol\theta|\breve\alpha_1+N_1,\dots,\breve\alpha_K+N_K)=\mathrm{Dir}(\boldsymbol\theta|\widehat{\boldsymbol\alpha})\tag{3.91–3.92}$$
with $\widehat\alpha_k=\breve\alpha_k+N_k$: add empirical counts to prior counts. Posterior mode:
$$\hat\theta_k=\frac{\widehat\alpha_k-1}{\sum_{k'}\widehat\alpha_{k'}-1}=\frac{N_k+\breve\alpha_k-1}{\sum_{k'}N_{k'}+\breve\alpha_{k'}-1}\tag{3.93}$$
Setting $\breve\alpha_k=1$ gives the MLE; $\breve\alpha_k=2$ gives the add-one smoothing estimate (p. 85). (added step: with $\breve\alpha_k=2$, (3.93) reads $(N_k+1)/(N+K)$.)

Marginal likelihood, with $B(\boldsymbol\alpha)=\prod_k\Gamma(\alpha_k)/\Gamma(\sum_k\alpha_k)$:
$$p(\mathcal D)=\frac{B(\mathbf N+\boldsymbol\alpha)}{B(\boldsymbol\alpha)}\tag{3.94–3.95}$$
$$p(\mathcal D)=\frac{\Gamma(\sum_k\alpha_k)}{\Gamma(N+\sum_k\alpha_k)}\prod_k\frac{\Gamma(N_k+\alpha_k)}{\Gamma(\alpha_k)}\tag{3.96}$$
(p. 85).

*Intuition note.* A Dirichlet prior is like having already seen $\breve\alpha_k$ virtual observations of category $k$. Updating means counting real ones on top. The marginal likelihood is a ratio of normalizers.

**3.4.3 Univariate Gaussian.** Three steps: $\mu$ alone, $\sigma^2$ alone, both (p. 85).

*3.4.3.1 $\mu$ given $\sigma^2$.* Likelihood $p(\mathcal D|\mu)\propto\exp\!\big(-\frac1{2\sigma^2}\sum_n(y_n-\mu)^2\big)$ (3.97). The conjugate prior is Gaussian $\mathcal N(\mu|\breve m,\breve\tau^2)$. By Bayes' rule for Gaussians (Eq. 2.121c):
$$p(\mu|\mathcal D,\sigma^2)=\mathcal N(\mu|\widehat m,\widehat\tau^2)\tag{3.98}$$
$$\widehat\tau^2=\frac1{\frac N{\sigma^2}+\frac1{\breve\tau^2}}=\frac{\sigma^2\breve\tau^2}{N\breve\tau^2+\sigma^2}\tag{3.99}$$
$$\widehat m=\widehat\tau^2\Big(\frac{\breve m}{\breve\tau^2}+\frac{N\bar y}{\sigma^2}\Big)=\frac{\sigma^2}{N\breve\tau^2+\sigma^2}\breve m+\frac{N\breve\tau^2}{N\breve\tau^2+\sigma^2}\bar y\tag{3.100}$$
with $\bar y=\frac1N\sum_n y_n$ (p. 85).

In precisions ($\lambda=1/\sigma^2$, $\breve\lambda=1/\breve\tau^2$):
$$p(\mu|\mathcal D,\lambda)=\mathcal N(\mu|\widehat m,\widehat\lambda^{-1}),\quad\widehat\lambda=\breve\lambda+N\lambda,\quad\widehat m=\frac{N\lambda\bar y+\breve\lambda\breve m}{\widehat\lambda}=\frac{N\lambda}{N\lambda+\breve\lambda}\bar y+\frac{\breve\lambda}{N\lambda+\breve\lambda}\breve m\tag{3.101–3.103}$$
The posterior precision is the prior precision plus $N$ units of measurement precision. The posterior mean is a convex combination of $\bar y$ and $\breve m$. A weak prior ($\breve\lambda$ small relative to $\lambda$) puts more weight on the data, a strong prior more on the prior (Fig. 3.5: prior variance 1 vs 5). $N$ measurements of precision $\lambda$ act like one measurement $\bar y$ of precision $N\lambda$ (p. 86).

For $N=1$, with $w=\breve\lambda/\widehat\lambda$:
$$\widehat m=\frac{\breve\lambda}{\widehat\lambda}\breve m+\frac\lambda{\widehat\lambda}y=\breve m+\frac\lambda{\widehat\lambda}(y-\breve m)=y-\frac{\breve\lambda}{\widehat\lambda}(y-\breve m)\tag{3.104–3.106}$$
$$\widehat m=y-w(y-\breve m)=(1-w)y+w\breve m\tag{3.107}$$
The third form (3.106), the data adjusted towards the prior mean, is called a **shrinkage** estimate. For a Gaussian the posterior mean equals the mode, so these formulas give MAP estimates (p. 86).

*3.4.3.2 $\sigma^2$ given $\mu$.* Likelihood $p(\mathcal D|\sigma^2)\propto(\sigma^2)^{-N/2}\exp\!\big(-\frac1{2\sigma^2}\sum_n(y_n-\mu)^2\big)$ (3.108); the $(\sigma^2)^{-N/2}$ factor cannot be ignored. Conjugate prior: inverse gamma,
$$\mathrm{IG}(\sigma^2|\breve a,\breve b)=\frac{\breve b^{\breve a}}{\Gamma(\breve a)}(\sigma^2)^{-(\breve a+1)}\exp(-\breve b/\sigma^2)\tag{3.109}$$
Posterior:
$$p(\sigma^2|\mu,\mathcal D)=\mathrm{IG}(\sigma^2|\widehat a,\widehat b),\quad\widehat a=\breve a+N/2,\quad\widehat b=\breve b+\tfrac12\sum_n(y_n-\mu)^2\tag{3.110–3.112}$$
(Fig. 3.6: from a flat start with true $\sigma^2=10$, the posterior concentrates near 10 as $N$ goes from 2 to 100.) (p. 87)

Because prior strength sits in both $\breve a$ and $\breve b$, the literature often uses the scaled inverse chi-squared:
$$\chi^{-2}(\sigma^2|\breve\nu,\breve\tau^2)=\mathrm{IG}\!\Big(\sigma^2\Big|\frac{\breve\nu}2,\frac{\breve\nu\breve\tau^2}2\Big)\propto(\sigma^2)^{-\breve\nu/2-1}\exp\!\Big(-\frac{\breve\nu\breve\tau^2}{2\sigma^2}\Big)\tag{3.113}$$
$\breve\nu$ (degrees of freedom) is the prior strength; $\breve\tau^2$ encodes the prior mean (pp. 87–88). Posterior:
$$p(\sigma^2|\mathcal D,\mu)=\chi^{-2}(\sigma^2|\widehat\nu,\widehat\tau^2),\quad\widehat\nu=\breve\nu+N,\quad\widehat\tau^2=\frac{\breve\nu\breve\tau^2+\sum_n(y_n-\mu)^2}{\widehat\nu}\tag{3.114–3.116}$$
The posterior sum of squares $\widehat\nu\widehat\tau^2$ equals the prior sum of squares plus the data sum of squares (p. 88).

*3.4.3.3 $\mu$ and $\sigma^2$, conjugate prior.* Normal-inverse-gamma:
$$\mathrm{NIG}(\mu,\sigma^2|\breve m,\breve\kappa,\breve a,\breve b)\triangleq\mathcal N(\mu|\breve m,\sigma^2/\breve\kappa)\,\mathrm{IG}(\sigma^2|\breve a,\breve b)\tag{3.117}$$
Common reparameterization, normal-inverse-chi-squared (NIX):
$$\mathrm{NI}\chi^2(\mu,\sigma^2|\breve m,\breve\kappa,\breve\nu,\breve\tau^2)\triangleq\mathcal N(\mu|\breve m,\sigma^2/\breve\kappa)\,\chi^{-2}(\sigma^2|\breve\nu,\breve\tau^2)\tag{3.118}$$
$$\propto\Big(\frac1{\sigma^2}\Big)^{(\breve\nu+3)/2}\exp\!\Big(-\frac{\breve\nu\breve\tau^2+\breve\kappa(\mu-\breve m)^2}{2\sigma^2}\Big)\tag{3.119}$$
Along $\mu$ it looks Gaussian, along $\sigma^2$ like $\chi^{-2}$, with "squashed egg" contours (Fig. 3.7). The $\mu$-contours are more peaked for small $\sigma^2$: low-variance data pin down the mean better (p. 88). Posterior:
$$p(\mu,\sigma^2|\mathcal D)=\mathrm{NI}\chi^2(\mu,\sigma^2|\widehat m,\widehat\kappa,\widehat\nu,\widehat\tau^2)\tag{3.120}$$
$$\widehat m=\frac{\breve\kappa\breve m+N\bar y}{\widehat\kappa},\ \ \widehat\kappa=\breve\kappa+N,\ \ \widehat\nu=\breve\nu+N,\ \ \widehat\nu\widehat\tau^2=\breve\nu\breve\tau^2+\sum_n(y_n-\bar y)^2+\frac{N\breve\kappa}{\breve\kappa+N}(\breve m-\bar y)^2\tag{3.121–3.124}$$
The text says this follows from Sec. 3.4.4.3. The sum of squares gains a term for the mismatch between prior mean and sample mean (p. 88). Marginals:
$$p(\sigma^2|\mathcal D)=\chi^{-2}(\sigma^2|\widehat\nu,\widehat\tau^2),\ \ \mathbb E[\sigma^2|\mathcal D]=\tfrac{\widehat\nu}{\widehat\nu-2}\widehat\tau^2\tag{3.125}$$
$$p(\mu|\mathcal D)=\mathcal T(\mu|\widehat m,\widehat\tau^2/\widehat\kappa,\widehat\nu),\ \ \mathbb E[\mu|\mathcal D]=\widehat m\tag{3.126}$$
The Student form arises because a Student is a scaled mixture of Gaussians (p. 89).

*3.4.3.4 Uninformative prior.* The Jeffreys prior for a location-scale pair is $p(\mu,\sigma^2)\propto p(\mu)p(\sigma^2)\propto\sigma^{-2}$ (3.127; derived in Sec. 3.5.2.3). It can be simulated by $\mathrm{NI}\chi^2(\breve m=0,\breve\kappa=0,\breve\nu=-1,\breve\tau^2=0)$ (3.128). The posterior is
$$\mathrm{NI}\chi^2(\widehat m=\bar y,\widehat\kappa=N,\widehat\nu=N-1,\widehat\tau^2=s^2)\tag{3.129}$$
with $s^2\triangleq\frac1{N-1}\sum_n(y_n-\bar y)^2=\frac N{N-1}\hat\sigma^2_{\rm mle}$ (3.130; $s$ is the sample standard deviation) (pp. 89–90). Then
$$p(\mu|\mathcal D)=\mathcal T(\mu|\bar y,s^2/N,N-1)\tag{3.131}$$
$$\mathbb V[\mu|\mathcal D]=\frac{\widehat\nu}{\widehat\nu-2}\widehat\tau^2=\frac{N-1}{N-3}\frac{s^2}N\to\frac{s^2}N\tag{3.132}$$
$$\mathrm{se}(\mu)\triangleq\sqrt{\mathbb V[\mu|\mathcal D]}\approx s/\sqrt N\tag{3.133}$$
The approximate 95% credible interval is $I_{.95}(\mu|\mathcal D)=\bar y\pm2s/\sqrt N$ (3.134) (p. 90).

*Intuition note.* Both prior and data contribute "strength" (counts) and "sums of squares". Strengths add, sums of squares add (plus a term for the mismatch between prior mean and sample mean), and means average with weights proportional to strength. With the default prior the posterior gives, approximately, the standard error $s/\sqrt N$ and interval $\bar y\pm2s/\sqrt N$, now read as posterior statements.

**3.4.4 Multivariate Gaussian** ($D$-dim data; $\mathbf Y$ is $N\times D$; $\boldsymbol\Sigma,\boldsymbol\Psi$ are $D\times D$) (p. 90).

*3.4.4.1 $\boldsymbol\mu$ given $\boldsymbol\Sigma$.* Likelihood $p(\mathcal D|\boldsymbol\mu)=\mathcal N(\bar{\mathbf y}|\boldsymbol\mu,\frac1N\boldsymbol\Sigma)$ (3.135). Prior $\mathcal N(\boldsymbol\mu|\breve{\mathbf m},\breve{\mathbf V})$ gives
$$p(\boldsymbol\mu|\mathcal D,\boldsymbol\Sigma)=\mathcal N(\boldsymbol\mu|\widehat{\mathbf m},\widehat{\mathbf V}),\ \ \widehat{\mathbf V}^{-1}=\breve{\mathbf V}^{-1}+N\boldsymbol\Sigma^{-1},\ \ \widehat{\mathbf m}=\widehat{\mathbf V}(\boldsymbol\Sigma^{-1}(N\bar{\mathbf y})+\breve{\mathbf V}^{-1}\breve{\mathbf m})\tag{3.136–3.138}$$
(Fig. 3.8: 2-d example with 10 points) (pp. 90–91).

*3.4.4.2 $\boldsymbol\Sigma$ given $\boldsymbol\mu$.* With scatter matrix $\mathbf S_\mu\triangleq\sum_n(\mathbf y_n-\boldsymbol\mu)(\mathbf y_n-\boldsymbol\mu)^{\mathsf T}$ (3.140), the likelihood is
$$p(\mathcal D|\boldsymbol\mu,\boldsymbol\Sigma)\propto|\boldsymbol\Sigma|^{-N/2}\exp\!\big(-\tfrac12\mathrm{tr}(\mathbf S_\mu\boldsymbol\Sigma^{-1})\big)\tag{3.139}$$
The conjugate prior is inverse Wishart (a distribution over positive definite matrices):
$$\mathrm{IW}(\boldsymbol\Sigma|\breve{\boldsymbol\Psi}^{-1},\breve\nu)\propto|\boldsymbol\Sigma|^{-(\breve\nu+D+1)/2}\exp\!\big(-\tfrac12\mathrm{tr}(\breve{\boldsymbol\Psi}\boldsymbol\Sigma^{-1})\big)\tag{3.141}$$
Here $\breve\nu>D-1$ and $\breve{\boldsymbol\Psi}$ is symmetric positive definite (pd); $\breve{\boldsymbol\Psi}$ plays the role of a prior scatter matrix, and $N_0\triangleq\breve\nu+D+1$ acts like a prior sample size (p. 91). Multiplying likelihood and prior:
$$p(\boldsymbol\Sigma|\mathcal D,\boldsymbol\mu)\propto|\boldsymbol\Sigma|^{-\frac{N+\breve\nu+D+1}2}\exp\!\big(-\tfrac12\mathrm{tr}[\boldsymbol\Sigma^{-1}(\mathbf S_\mu+\breve{\boldsymbol\Psi})]\big)=\mathrm{IW}(\boldsymbol\Sigma|\widehat{\boldsymbol\Psi}^{-1},\widehat\nu)\tag{3.142–3.144}$$
$$\widehat\nu=\breve\nu+N,\quad\widehat{\boldsymbol\Psi}=\breve{\boldsymbol\Psi}+\mathbf S_\mu\tag{3.145–3.146}$$
(p. 92).

*3.4.4.3 $\boldsymbol\mu$ and $\boldsymbol\Sigma$.* Likelihood (3.147) with the identity
$$\sum_n(\mathbf y_n-\boldsymbol\mu)^{\mathsf T}\boldsymbol\Sigma^{-1}(\mathbf y_n-\boldsymbol\mu)=\mathrm{tr}(\boldsymbol\Sigma^{-1}\mathbf S)+N(\bar{\mathbf y}-\boldsymbol\mu)^{\mathsf T}\boldsymbol\Sigma^{-1}(\bar{\mathbf y}-\boldsymbol\mu)\tag{3.148}$$
where $\mathbf S\triangleq\sum_n(\mathbf y_n-\bar{\mathbf y})(\mathbf y_n-\bar{\mathbf y})^{\mathsf T}=\mathbf Y^{\mathsf T}\mathbf C_N\mathbf Y$ (3.149) and the centering matrix is $\mathbf C_N\triangleq\mathbf I_N-\frac1N\mathbf 1_N\mathbf 1_N^{\mathsf T}$ ($N\times N$) (3.150). Hence
$$p(\mathcal D|\boldsymbol\mu,\boldsymbol\Sigma)\propto|\boldsymbol\Sigma|^{-N/2}\exp\!\big(-\tfrac N2(\boldsymbol\mu-\bar{\mathbf y})^{\mathsf T}\boldsymbol\Sigma^{-1}(\boldsymbol\mu-\bar{\mathbf y})\big)\exp\!\big(-\tfrac12\mathrm{tr}(\mathbf S\boldsymbol\Sigma^{-1})\big)\tag{3.151}$$
(p. 92).

*Prior.* The factored prior $\mathcal N(\boldsymbol\mu|\breve{\mathbf m},\breve{\mathbf V})\mathrm{IW}(\boldsymbol\Sigma|\breve{\boldsymbol\Psi}^{-1},\breve\nu)$ (3.152) is not conjugate, because $\boldsymbol\mu$ and $\boldsymbol\Sigma$ appear together in the first exponent of (3.151). It is "conditionally conjugate", since $p(\boldsymbol\mu|\boldsymbol\Sigma)$ and $p(\boldsymbol\Sigma|\boldsymbol\mu)$ are each conjugate (footnote 4: explaining away, Fig. 3.9a) (p. 93). A fully conjugate prior makes $\boldsymbol\mu$ depend on $\boldsymbol\Sigma$, the normal-inverse-Wishart:
$$\mathrm{NIW}(\boldsymbol\mu,\boldsymbol\Sigma|\breve{\mathbf m},\breve\kappa,\breve\nu,\breve{\boldsymbol\Psi})\triangleq\mathcal N(\boldsymbol\mu|\breve{\mathbf m},\tfrac1{\breve\kappa}\boldsymbol\Sigma)\times\mathrm{IW}(\boldsymbol\Sigma|\breve{\boldsymbol\Psi}^{-1},\breve\nu)\tag{3.153}$$
$$=\frac1{Z_{\rm NIW}}|\boldsymbol\Sigma|^{-\frac12}\exp\!\big(-\tfrac{\breve\kappa}2(\boldsymbol\mu-\breve{\mathbf m})^{\mathsf T}\boldsymbol\Sigma^{-1}(\boldsymbol\mu-\breve{\mathbf m})\big)\times|\boldsymbol\Sigma|^{-\frac{\breve\nu+D+1}2}\exp\!\big(-\tfrac12\mathrm{tr}(\breve{\boldsymbol\Psi}\boldsymbol\Sigma^{-1})\big)\tag{3.154}$$
$$Z_{\rm NIW}\triangleq2^{\breve\nu D/2}\Gamma_D(\breve\nu/2)(2\pi/\breve\kappa)^{D/2}|\breve{\boldsymbol\Psi}|^{\breve\nu/2}\tag{3.155}$$
$\breve{\mathbf m}$ is the prior mean of $\boldsymbol\mu$ with strength $\breve\kappa$; $\breve{\boldsymbol\Psi}$ is proportional to the prior mean of $\boldsymbol\Sigma$ with strength $\breve\nu$. Footnote 5: uncertainty in the mean is proportional to the covariance, since widely spread data make the mean hard to pin down (p. 93).

*Posterior derivation.* Rewrite $\mathbf S=\mathbf Y^{\mathsf T}\mathbf Y-N\bar{\mathbf y}\bar{\mathbf y}^{\mathsf T}$ (3.156), with $\mathbf Y^{\mathsf T}\mathbf Y=\sum_n\mathbf y_n\mathbf y_n^{\mathsf T}$ the sum-of-squares matrix. Multiply (3.151) by (3.154):
$$p(\boldsymbol\mu,\boldsymbol\Sigma|\mathcal D)\propto|\boldsymbol\Sigma|^{-\frac{N+\breve\nu+D+2}2}\exp\!\big(-\tfrac12\mathrm{tr}(\boldsymbol\Sigma^{-1}\mathbf M)\big)\tag{3.157–3.159}$$
$$\mathbf M\triangleq N(\boldsymbol\mu-\bar{\mathbf y})(\boldsymbol\mu-\bar{\mathbf y})^{\mathsf T}+\breve\kappa(\boldsymbol\mu-\breve{\mathbf m})(\boldsymbol\mu-\breve{\mathbf m})^{\mathsf T}+\mathbf S+\breve{\boldsymbol\Psi}\tag{3.160}$$
$$=(\breve\kappa+N)\boldsymbol\mu\boldsymbol\mu^{\mathsf T}-\boldsymbol\mu(\breve\kappa\breve{\mathbf m}+N\bar{\mathbf y})^{\mathsf T}-(\breve\kappa\breve{\mathbf m}+N\bar{\mathbf y})\boldsymbol\mu^{\mathsf T}+\breve\kappa\breve{\mathbf m}\breve{\mathbf m}^{\mathsf T}+\mathbf Y^{\mathsf T}\mathbf Y+\breve{\boldsymbol\Psi}\tag{3.161}$$
Complete the square on the first three terms:
$$(\breve\kappa+N)\Big(\boldsymbol\mu-\tfrac{\breve\kappa\breve{\mathbf m}+N\bar{\mathbf y}}{\breve\kappa+N}\Big)\Big(\boldsymbol\mu-\tfrac{\breve\kappa\breve{\mathbf m}+N\bar{\mathbf y}}{\breve\kappa+N}\Big)^{\mathsf T}-\frac{(\breve\kappa\breve{\mathbf m}+N\bar{\mathbf y})(\breve\kappa\breve{\mathbf m}+N\bar{\mathbf y})^{\mathsf T}}{\breve\kappa+N}=\widehat\kappa(\boldsymbol\mu-\widehat{\mathbf m})(\boldsymbol\mu-\widehat{\mathbf m})^{\mathsf T}-\widehat\kappa\widehat{\mathbf m}\widehat{\mathbf m}^{\mathsf T}\tag{3.162–3.165}$$
Hence the posterior is NIW: $p(\boldsymbol\mu,\boldsymbol\Sigma|\mathcal D)\propto|\boldsymbol\Sigma|^{\ldots}\exp(-\frac12\mathrm{tr}[\boldsymbol\Sigma^{-1}(\widehat\kappa(\boldsymbol\mu-\widehat{\mathbf m})(\boldsymbol\mu-\widehat{\mathbf m})^{\mathsf T}+\widehat{\boldsymbol\Psi})])=\mathrm{NIW}(\boldsymbol\mu,\boldsymbol\Sigma|\widehat{\mathbf m},\widehat\kappa,\widehat\nu,\widehat{\boldsymbol\Psi})$ (3.166–3.167). The $\boldsymbol\Sigma$-exponent is printed without a minus sign (see Reading notes) (p. 94). The parameters are
$$\widehat{\mathbf m}=\frac{\breve\kappa\breve{\mathbf m}+N\bar{\mathbf y}}{\widehat\kappa}=\frac{\breve\kappa}{\breve\kappa+N}\breve{\mathbf m}+\frac N{\breve\kappa+N}\bar{\mathbf y},\ \ \widehat\kappa=\breve\kappa+N,\ \ \widehat\nu=\breve\nu+N\tag{3.168–3.170}$$
$$\widehat{\boldsymbol\Psi}=\breve{\boldsymbol\Psi}+\mathbf S+\frac{\breve\kappa N}{\breve\kappa+N}(\bar{\mathbf y}-\breve{\mathbf m})(\bar{\mathbf y}-\breve{\mathbf m})^{\mathsf T}=\breve{\boldsymbol\Psi}+\mathbf Y^{\mathsf T}\mathbf Y+\breve\kappa\breve{\mathbf m}\breve{\mathbf m}^{\mathsf T}-\widehat\kappa\widehat{\mathbf m}\widehat{\mathbf m}^{\mathsf T}\tag{3.171–3.172}$$
The posterior mean is a convex combination of prior mean and MLE. The scatter matrix gets a virtual extra term from uncertainty in the mean, and $\widehat\kappa,\widehat\nu$ are each incremented by $N$ (p. 95).

*Skip path:* carry forward (3.168)–(3.171).

*Marginals and mode.* The joint is $\mathcal N(\boldsymbol\mu|\widehat{\mathbf m},\frac1{\widehat\kappa}\boldsymbol\Sigma)\mathrm{IW}(\boldsymbol\Sigma|\widehat{\boldsymbol\Psi}^{-1},\widehat\nu)$ (3.173). Marginals:
$$p(\boldsymbol\Sigma|\mathcal D)=\mathrm{IW}(\boldsymbol\Sigma|\widehat{\boldsymbol\Psi}^{-1},\widehat\nu)\tag{3.174}$$
$$p(\boldsymbol\mu|\mathcal D)=\mathcal T\!\Big(\boldsymbol\mu\Big|\widehat{\boldsymbol\mu},\frac{\widehat{\boldsymbol\Psi}}{\widehat\kappa\widehat\nu'},\widehat\nu'\Big),\ \ \widehat\nu'\triangleq\widehat\nu-D+1\tag{3.175}$$
This is an infinite mixture of Gaussians, one per $\boldsymbol\Sigma$ drawn from the IW, and it has heavier tails than one Gaussian (p. 95). For the MAP, $\boldsymbol\mu$ appears only in $\mathcal N(\boldsymbol\mu|\widehat{\boldsymbol\mu},\widehat\kappa^{-1}\boldsymbol\Sigma)$, whose mode is its mean for any $\boldsymbol\Sigma$. Plugging in $\boldsymbol\mu=\widehat{\boldsymbol\mu}$:
$$-2\log p(\widehat{\boldsymbol\mu},\boldsymbol\Sigma|\mathbf Y)=(\widehat\nu+D+2)\log|\boldsymbol\Sigma|+\mathrm{tr}(\widehat{\boldsymbol\Psi}\boldsymbol\Sigma^{-1})+c\tag{3.177}$$
The derivative is $(\widehat\nu+D+2)\boldsymbol\Sigma^{-1}-\boldsymbol\Sigma^{-1}\widehat{\boldsymbol\Psi}\boldsymbol\Sigma^{-1}$ (3.178; printed as the derivative of $\log p$, see Reading notes). Setting it to 0 gives $(\widehat\nu+D+2)^{-1}\widehat{\boldsymbol\Psi}$, which is positive definite, hence the MAP (p. 96):
$$\hat{\boldsymbol\mu}=\frac{\breve\kappa\breve{\boldsymbol\mu}+N\bar{\mathbf y}}{\breve\kappa+N},\qquad\hat{\boldsymbol\Sigma}=\frac1{\widehat\nu+D+2}\widehat{\boldsymbol\Psi}\tag{3.179–3.180}$$

*Posterior predictive.* If $\mathbf y\sim\mathcal N(\boldsymbol\mu,\boldsymbol\Sigma)$ and $(\boldsymbol\mu,\boldsymbol\Sigma|\mathcal D)\sim\mathrm{NIW}(\widehat{\mathbf m},\widehat\kappa,\widehat\nu,\widehat{\boldsymbol\Psi})$, then for one new vector
$$p(\mathbf y|\mathcal D)=\int\mathcal N(\mathbf y|\boldsymbol\mu,\boldsymbol\Sigma)\mathrm{NIW}(\cdots)\,d\boldsymbol\mu\,d\boldsymbol\Sigma=\mathcal T\!\Big(\mathbf y\Big|\widehat{\mathbf m},\frac{\widehat{\boldsymbol\Psi}(\widehat\kappa+1)}{\widehat\kappa\widehat\nu'},\widehat\nu'\Big)\tag{3.181–3.182}$$
with $\widehat\nu'=\widehat\nu-D+1$ (p. 96).

**3.4.5 Exponential family.** Closed-form conjugate analysis needs fixed-size sufficient statistics, $p(\mathcal D|\boldsymbol\theta)=p(\mathbf s(\mathcal D)|\boldsymbol\theta)$. This suggests the exponential family is the only family with conjugate priors, a result proved in [DY79]. Footnote 6 gives an exception: $\mathrm{Unif}(0,\theta)$ has finite sufficient statistics $(N,m=\max_ix_i)$; its conjugate prior is Pareto, with posterior $\mathrm{Pareto}(\max(\theta_0,m),\kappa+N)$ (p. 96).

Likelihood: $p(\mathcal D|\boldsymbol\eta)=h(\mathcal D)\exp(\boldsymbol\eta^{\mathsf T}\mathbf s(\mathcal D)-NA(\boldsymbol\eta))$, $\mathbf s(\mathcal D)=\sum_n\mathbf s(\mathbf x_n)$, $h(\mathcal D)=\prod_nh(\mathbf x_n)$ (3.183). Prior mirrors it:
$$p(\boldsymbol\eta|\breve{\boldsymbol\tau},\breve\nu)=\frac1{Z(\breve{\boldsymbol\tau},\breve\nu)}\exp(\breve{\boldsymbol\tau}^{\mathsf T}\boldsymbol\eta-\breve\nu A(\boldsymbol\eta))\tag{3.184}$$
$\breve\nu$ is the prior strength, $\breve{\boldsymbol\tau}/\breve\nu$ the prior mean, and $\breve{\boldsymbol\tau}$ can come from virtual samples (p. 97). Posterior:
$$p(\boldsymbol\eta|\mathcal D)=\frac{h(\mathcal D)}{Z(\breve{\boldsymbol\tau},\breve\nu)p(\mathcal D)}\exp\!\big((\breve{\boldsymbol\tau}+\mathbf s(\mathcal D))^{\mathsf T}\boldsymbol\eta-(\breve\nu+N)A(\boldsymbol\eta)\big)=\frac1{Z(\widehat{\boldsymbol\tau},\widehat\nu)}\exp(\widehat{\boldsymbol\tau}^{\mathsf T}\boldsymbol\eta-\widehat\nu A(\boldsymbol\eta))\tag{3.185–3.187}$$
$$\widehat{\boldsymbol\tau}=\breve{\boldsymbol\tau}+\mathbf s(\mathcal D),\ \ \widehat\nu=\breve\nu+N,\ \ Z(\widehat{\boldsymbol\tau},\widehat\nu)=\frac{Z(\breve{\boldsymbol\tau},\breve\nu)}{h(\mathcal D)}p(\mathcal D)\tag{3.188–3.190}$$
Posterior mean, as printed (with $\lambda=\breve\nu/(\breve\nu+N)$):
$$\mathbb E[\boldsymbol\eta|\mathcal D]=\frac{\widehat{\boldsymbol\tau}}{\widehat\nu}=\frac{\breve{\boldsymbol\tau}+\mathbf s(\mathcal D)}{\breve\nu+N}=\frac{\breve\nu}{\breve\nu+N}\frac{\breve{\boldsymbol\tau}}{\breve\nu}+\frac N{\breve\nu+N}\frac{\mathbf s(\mathcal D)}N=\lambda\mathbb E[\boldsymbol\eta]+(1-\lambda)\hat{\boldsymbol\eta}_{\rm mle}\tag{3.191–3.192}$$
(p. 97). Marginal likelihood from (3.190):
$$p(\mathcal D)=\frac{Z(\widehat{\boldsymbol\tau},\widehat\nu)h(\mathcal D)}{Z(\breve{\boldsymbol\tau},\breve\nu)}\tag{3.193}$$
(p. 97). Posterior predictive for $\mathcal D'=(\tilde{\mathbf x}_1,\dots,\tilde{\mathbf x}_{N'})$:
$$p(\mathcal D'|\mathcal D)=\int p(\mathcal D'|\boldsymbol\eta)p(\boldsymbol\eta|\mathcal D)d\boldsymbol\eta=h(\mathcal D')\frac{Z(\breve{\boldsymbol\tau}+\mathbf s(\mathcal D)+\mathbf s(\mathcal D'),\breve\nu+N+N')}{Z(\breve{\boldsymbol\tau}+\mathbf s(\mathcal D),\breve\nu+N)}\tag{3.194–3.196}$$
(p. 98).

*Example: Bernoulli (3.4.5.6).* Likelihood $(1-\theta)^N\exp(\log\frac\theta{1-\theta}\sum x_n)$ (3.197). The conjugate prior is $\propto(1-\theta)^{\nu_0}\exp(\log\frac\theta{1-\theta}\,\tau_0)=\theta^{\tau_0}(1-\theta)^{\nu_0-\tau_0}$ (3.198–3.199). With $\alpha=\tau_0+1$, $\beta=\nu_0-\tau_0+1$ this is a Beta. Posterior with $s=\sum_i\mathbb I(x_i=1)$: $p(\theta|\mathcal D)\propto\theta^{\tau_0+s}(1-\theta)^{\nu_0-\tau_0+n-s}=\theta^{\tau_n}(1-\theta)^{\nu_n-\tau_n}$ (3.200–3.201). Predictive probability of a future sequence with $s'$ heads in $m$ tosses, using the posterior $\mathrm{Beta}(\alpha_n,\beta_n)$:
$$p(\mathcal D'|\mathcal D)=\frac{\Gamma(\alpha_n+\beta_n)}{\Gamma(\alpha_n)\Gamma(\beta_n)}\frac{\Gamma(\alpha_{n+m})\Gamma(\beta_{n+m})}{\Gamma(\alpha_{n+m}+\beta_{n+m})}\tag{3.202–3.204}$$
$$\alpha_{n+m}=\alpha_n+s'=\alpha+s+s',\quad\beta_{n+m}=\beta_n+(m-s')=\beta+(n-s)+(m-s')\tag{3.205–3.206}$$
(p. 98).

*Intuition note.* For the exponential family the recipe is: prior statistics $+$ data statistics, and prior sample size $+$ $N$. The Beta–Bernoulli case is rederived in this notation just above; the earlier Dirichlet and Gaussian updates have the same add-to-prior form.

**3.4.6 Beyond conjugate priors.** Conjugate priors are easy to interpret (virtual data) and compute with. But most models have no exponential-family conjugate prior, and conjugacy may be too limiting. Inference with non-conjugate priors is deferred to Sec. 7.1 (p. 99).

*3.4.6.1 Mixtures of conjugate priors.* A mixture of conjugate priors is still conjugate. A casino coin may be fair or head-biased, which a single Beta cannot express. Example prior:
$$p(\theta)=0.5\,\mathrm{Beta}(\theta|20,20)+0.5\,\mathrm{Beta}(\theta|30,10)\tag{3.207}$$
With a latent indicator $h$: $p(\theta)=\sum_kp(h=k)p(\theta|h=k)$ (3.208). The posterior is $p(\theta|\mathcal D)=\sum_kp(h=k|\mathcal D)p(\theta|\mathcal D,h=k)$ (3.209), with weights
$$p(h=k|\mathcal D)=\frac{p(h=k)p(\mathcal D|h=k)}{\sum_{k'}p(h=k')p(\mathcal D|h=k')}\tag{3.210}$$
where $p(\mathcal D|h=k)$ is component $k$'s marginal likelihood. With $N_1=20$ heads and $N_0=10$ tails (using Eq. 3.31):
$$p(\theta|\mathcal D)=0.346\,\mathrm{Beta}(\theta|40,30)+0.654\,\mathrm{Beta}(\theta|50,20)\tag{3.211}$$
(Fig. 3.10). Then $\Pr(\theta>0.5|\mathcal D)=\sum_k\Pr(\theta>0.5|\mathcal D,h=k)p(h=k|\mathcal D)=0.9604$ (3.212); a single Beta(20,20) prior gives 0.8858. A prior "suspicious" of bias is confirmed faster (pp. 99–100).

*3.4.6.2 Robust (heavy-tailed) priors.* **Sensitivity (robustness) analysis** assesses the influence of the prior on the posterior. Example from [Ber85a]: $x\sim\mathcal N(\theta,1)$, $x=5$. The MLE and the posterior mean under a uniform prior are both 5. Now suppose the prior median is 0, with 25% probability in each of $(-\infty,-1),(-1,0),(0,1),(1,\infty)$, and the prior is smooth and unimodal. A Gaussian prior "$\mathcal N(\theta|0,2.19^2)$" satisfies these constraints, but its posterior mean is 3.43, "doesn't seem very satisfactory". A Cauchy prior $\mathcal T_1(\theta|0,1)$ with the same information gives a posterior mean of about 4.6 (numerical integration). In general, heavy-tailed priors tend to give results more sensitive to the data, which is usually desired. They are usually not conjugate but can be approximated by (possibly infinite) mixtures of conjugate priors. A Student (Cauchy is a special case) is an infinite mixture of Gaussians with gamma mixing weights (Sec. 28.2.3), a hierarchical prior (p. 100).

*3.4.6.3 Priors for scalar variances.* Variance priors play an important role in determining how much regularization a model exhibits. In linear regression $\mathcal N(y|\mathbf w^{\mathsf T}\mathbf x,\sigma^2)$ with prior $\mathcal N(\mathbf w|\mathbf 0,\tau^2\mathbf I)$, $\tau^2$ relative to $\sigma^2$ plays a role similar to the strength of $\ell_2$ regularization in ridge regression (p. 101).
- The uninformative prior $\mathrm{IG}(\sigma^2|0,0)$ is improper (does not integrate to 1). That is fine if the posterior is proper, which holds for noise variance with $N\ge2$ observables.
- The posterior is not proper, even as $N\to\infty$, if the prior is used for the variance of unobservable regression weights ([Gel06; PS12]; Sec. 3.6).
- The weakly informative proper prior $\mathrm{IG}(\epsilon,\epsilon)$ for small $\epsilon$ does not work well.
- Recommended instead: uniform, exponential, half-normal, half-Student-$t$ or half-Cauchy, bounded below by 0 with 1–2 hyperparameters ("half" = folded onto the positive axis) (p. 101).

*3.4.6.4 Priors for covariance matrices.*
- The inverse Wishart is conjugate but hard to set uninformatively. One approach [HW13] is a scale mixture of inverse Wisharts with inverse-gamma scales. Parameters can be chosen so that correlations have uniform $(-1,1)$ marginals and standard deviations are half-Student.
- The Wishart has heavy tails, which can hurt sampling. A common alternative factors
$$\boldsymbol\Sigma=\mathrm{diag}(\boldsymbol\sigma)\mathbf R\,\mathrm{diag}(\boldsymbol\sigma)\tag{3.213}$$
For $D=2$, $\boldsymbol\Sigma=\begin{pmatrix}\sigma_1^2&\rho\sigma_1\sigma_2\\\rho\sigma_1\sigma_2&\sigma_2^2\end{pmatrix}$ (3.214).
- Factored prior on the standard deviations: $p(\boldsymbol\sigma)=\prod_d\mathrm{Expon}(\sigma_d|1)$ (3.215).
- For the correlation matrix, the LKJ distribution is common: $\mathrm{LKJ}(\mathbf R|\eta)\propto|\mathbf R|^{\eta-1}$ (3.216), with one free parameter. $\eta=1$ is uniform; $\eta=2$ is "weakly regularizing", encouraging correlations near 0 (Fig. 3.11).
- In practice $\mathbf R=\mathbf L\mathbf L^{\mathsf T}$ with $\mathbf L$ an unconstrained lower triangular matrix, and the prior is written $\mathrm{LKJchol}(\mathbf L|\eta)\propto|\mathbf L|^{-\eta-1}$ (3.217) (pp. 101–102).

### 3.5 Noninformative priors
These are meant to "let the data speak for itself", but there is no unique way to define them and all encode some knowledge. So the terms diffuse, minimally informative or default prior are better (p. 102).

**3.5.1 Maximum entropy priors.** A maximum-entropy prior makes the least commitment to any value. This formalizes Laplace's principle of insufficient reason (if no reason prefers one prior, pick a flat one). For a Bernoulli rate the maxent prior is uniform, $\mathrm{Beta}(1,1)$. A *maxent prior with constraints* maximizes entropy subject to $\mathbb E[f_k(\theta)]=F_k$; such distributions must belong to the exponential family (Sec. 2.4.7) (p. 103). Example: $\theta\in\{1,\dots,10\}$, prior mean 1.5:
$$\sum_cc\,p_c=1.5,\ \ \sum_cp_c=1\tag{3.218–3.219}$$
(3.219 is printed as "min $\mathbb H(\mathbf p)$"; see Reading notes.) The solution is the decaying curve of Fig. 3.12. With the constraint $\Pr(\theta\in\{3,4\})=0.8$ (3.220), the solution is the inverted U, flat in as many places as possible (p. 103).

**3.5.2 Jeffreys priors.** Goal: a prior invariant to invertible reparameterization $\phi=f(\theta)$, so the posterior does not depend on parameterization. Example: Alice uses the rate $\theta$; Bob uses the odds $\phi=\theta/(1-\theta)$ and converts Alice's prior by change of variables. Converting Bob's posterior back should give Alice's result. The Jeffreys prior achieves this: $p(\theta)\propto\sqrt{F(\theta)}$ in 1-d, and $p(\boldsymbol\theta)\propto\sqrt{\det\mathbf F(\boldsymbol\theta)}$ in several dimensions ($F$ = Fisher information) (p. 103). Proof in 1-d, starting from $p_\theta\propto\sqrt{F(\theta)}$:
$$p_\phi(\phi)=p_\theta(\theta)\Big|\frac{d\theta}{d\phi}\Big|\propto\sqrt{F(\theta)\Big(\frac{d\theta}{d\phi}\Big)^2}=\sqrt{\mathbb E\Big[\Big(\frac{d\log p(x|\theta)}{d\theta}\Big)^2\Big]\Big(\frac{d\theta}{d\phi}\Big)^2}\tag{3.221–3.222}$$
$$=\sqrt{\mathbb E\Big[\Big(\frac{d\log p(x|\theta)}{d\theta}\frac{d\theta}{d\phi}\Big)^2\Big]}=\sqrt{\mathbb E\Big[\Big(\frac{d\log p(x|\phi)}{d\phi}\Big)^2\Big]}=\sqrt{F(\phi)}\tag{3.223–3.224}$$
(p. 104).

*Intuition note.* The Fisher information transforms with the squared Jacobian, so its square root picks up exactly one factor $|d\theta/d\phi|$, the same factor by which a density changes under a change of variables (3.221–3.224). So "square root of information" gives the same prior whichever way you parameterize.

*3.5.2.1 Binomial.* In the rate parameterization, using Eq. 3.57: $p(\theta)\propto\theta^{-1/2}(1-\theta)^{-1/2}\propto\mathrm{Beta}(\theta|\tfrac12,\tfrac12)$ (3.225). In odds form $\theta=\phi/(\phi+1)$ the likelihood is $p(x|\phi)\propto\phi^x(\phi+1)^{-n}$ (3.226). The log likelihood is $\ell=x\log\phi-n\log(\phi+1)$ (printed "$n\log\phi+1$", 3.227). Derivatives:
$$\frac{d\ell}{d\phi}=\frac x\phi-\frac n{\phi+1},\qquad\frac{d^2\ell}{d\phi^2}=-\frac x{\phi^2}+\frac n{(\phi+1)^2}\tag{3.228–3.229}$$
With $\mathbb E[x]=n\theta=n\frac\phi{\phi+1}$:
$$F(\phi)=-\mathbb E\Big[\frac{d^2\ell}{d\phi^2}\Big]=\frac n{\phi(\phi+1)}-\frac n{(\phi+1)^2}=\frac{n(\phi+1)-n\phi}{\phi(\phi+1)^2}=\frac n{\phi(\phi+1)^2}\tag{3.230–3.231}$$
so $p_\phi(\phi)\propto\phi^{-0.5}(1+\phi)^{-1}$ (3.232) (Fig. 3.13) (pp. 104–105).

*3.5.2.2 Multinomial.* For $K$ states the Jeffreys prior is $\mathrm{Dir}(\boldsymbol\theta|\tfrac12,\dots,\tfrac12)$ (3.233), different from $\mathrm{Dir}(\tfrac1K,\dots,\tfrac1K)$ or $\mathrm{Dir}(1,\dots,1)$ (p. 105).

*3.5.2.3 Gaussian mean and variance.* For $\boldsymbol\theta=(\mu,\sigma)$ the Fisher matrix is printed as $\mathrm{diag}(1/\sigma^2,\,1/(2\sigma^4))$ (3.234), so $\sqrt{\det}=1/(\sqrt2\sigma^3)$. The "standard" Jeffreys prior is instead the product of independent priors, $p(\mu,\sigma^2)\propto p(\mu)p(\sigma^2)\propto1/\sigma^2$ (3.235). It is emulated by the NIX prior with $\breve\kappa=0,\breve\nu=-1,\breve\sigma^2=0$ (3.236), so the results of Sec. 3.4.3.3 can be reused (p. 106).

**3.5.3 Invariant priors.** Knowledge of invariances can be encoded in a prior. A *location-scale family*: if $x$ is in the family, so is $y=a+bx$ (p. 106).
- *Translation-invariant:* the mass of $[A,B]$ equals that of $[A-c,B-c]$ (3.237). $p(\mu)\propto1$ achieves this (3.238), since $\int_{A-c}^{B-c}1\,d\mu=B-A=\int_A^B1\,d\mu$ (3.239). It equals the Jeffreys prior for a Gaussian mean with fixed variance, since $F(\mu)=1/\sigma^2\propto1$ (p. 106).
- *Scale-invariant:* the mass of $[A,B]$ equals that of $[A/c,B/c]$, $c>0$ (3.240). $p(\sigma)\propto1/\sigma$ achieves this (3.241), since $\int_{A/c}^{B/c}\frac{d\sigma}\sigma=\log(B/c)-\log(A/c)=\log B-\log A$ (3.242). It equals the Jeffreys prior for fixed mean and unknown scale, since $F(\sigma)=2/\sigma^2$ (p. 107).
- *Learning invariant priors:* analytically in some cases ([Rob07]); when intractable, perhaps by solving a variational optimization problem ([NS18]) (p. 107).

**3.5.4 Reference priors.** A reference prior is "maximally far from all possible posteriors, when averaged over datasets": it maximizes the expected KL divergence between posterior and prior,
$$p^*(\boldsymbol\theta)=\arg\max_{p(\boldsymbol\theta)}\int_{\mathcal D}p(\mathcal D)D_{\rm KL}\big(p(\boldsymbol\theta|\mathcal D)\,\|\,p(\boldsymbol\theta)\big)d\mathcal D,\ \ p(\mathcal D)=\int p(\mathcal D|\boldsymbol\theta)p(\boldsymbol\theta)d\boldsymbol\theta\tag{3.243}$$
This equals maximizing the mutual information $\mathbb I(\boldsymbol\theta,\mathcal D)$. Using $\frac{p(\boldsymbol\theta|\mathcal D)}{p(\boldsymbol\theta)}=\frac{p(\mathcal D|\boldsymbol\theta)}{p(\mathcal D)}$:
$$\int p(\mathcal D)\!\int p(\boldsymbol\theta|\mathcal D)\log\frac{p(\boldsymbol\theta|\mathcal D)}{p(\boldsymbol\theta)}=\int p(\boldsymbol\theta)\!\int p(\mathcal D|\boldsymbol\theta)\log\frac{p(\mathcal D|\boldsymbol\theta)}{p(\mathcal D)}=\mathbb E_{\boldsymbol\theta}[D_{\rm KL}(p(\mathcal D|\boldsymbol\theta)\|p(\mathcal D))]\tag{3.244}$$
In 1-d the reference prior is equivalent to the Jeffreys prior. In higher dimensions one can compute it one parameter at a time via the chain rule, which can be intractable; [NS17] gives a variational approximation (p. 107).

### 3.6 Hierarchical priors
Prior parameters are **hyperparameters** $\boldsymbol\xi$. If unknown, give them a prior: a hierarchical (multi-level) model, $\boldsymbol\xi\to\boldsymbol\theta\to\mathcal D$, with $p(\boldsymbol\xi,\boldsymbol\theta,\mathcal D)=p(\boldsymbol\xi)p(\boldsymbol\theta|\boldsymbol\xi)p(\mathcal D|\boldsymbol\theta)$ (3.245). The prior on $\boldsymbol\xi$ is assumed fixed (e.g. minimally informative). The hope is to learn $\boldsymbol\xi$ by treating the parameters as datapoints (p. 108).

It is useful with $J>1$ related datasets $\mathcal D_j$ with parameters $\boldsymbol\theta_j$. Separate inference is poor for small $\mathcal D_j$; pooling everything cannot model subpopulations. A hierarchical model lets groups with much data help groups with little ("borrow statistical strength"), sharing information through the hidden parent $\boldsymbol\xi$ (Fig. 3.14). Two predictive distributions follow (p. 108):
$$p(y_j|\mathcal D)=\int p(y_j|\boldsymbol\theta_j)p(\boldsymbol\theta_j|\mathcal D)d\boldsymbol\theta_j\ \text{(existing group)}\tag{3.246}$$
$$p(y_*|\mathcal D)=\int p(y_*|\theta_*)p(\theta_*|\boldsymbol\xi)p(\boldsymbol\xi|\mathcal D)d\theta_*d\boldsymbol\xi\ \text{(new, exchangeable group)}\tag{3.247}$$

**3.6.1 Hierarchical binomial.** $y_j\sim\mathrm{Bin}(N_j,\theta_j)$, $j=1{:}J$ (disease prevalence). Separate MLEs are unreliable for small groups (e.g. $y_j=0\Rightarrow\hat\theta_j=0$). *Parameter tying* (all $\theta_j$ equal) gives the pooled MLE $\hat\theta_{\rm pooled}=\sum_jy_j/\sum_jN_j$, a strong assumption. The compromise is $\theta_j\sim\mathrm{Beta}(a,b)$, $\boldsymbol\xi=(a,b)$ (pp. 108–109):
$$p(\mathcal D,\boldsymbol\theta,\boldsymbol\xi)=p(\boldsymbol\xi)\Big[\prod_j\mathrm{Beta}(\theta_j|\boldsymbol\xi)\Big]\Big[\prod_j\mathrm{Bin}(y_j|N_j,\theta_j)\Big],\quad p(a,b)\propto(a+b)^{-5/2}\tag{3.248–3.249}$$
(prior following [Gel+14a]; Fig. 3.14 shows the graphical model) (p. 109).

*3.6.1.1 Posterior inference.* Hamiltonian Monte Carlo (HMC, Sec. 12.5) is an MCMC method using the gradient of the log joint. It samples an unconstrained space, $\boldsymbol\omega=(\tilde{\boldsymbol\theta},\tilde{\boldsymbol\xi})\in\mathbb R^D$:
$$\log p(\mathcal D,\boldsymbol\omega)=\log p(\mathcal D|\boldsymbol\theta)+\log p(\boldsymbol\theta|\boldsymbol\xi)+\log p(\boldsymbol\xi)+\sum_{j=1}^J\log|\mathrm{Jac}(\sigma)(\tilde\theta_j)|+\sum_{i=1}^2\log|\mathrm{Jac}(\sigma_+)(\tilde\xi_i)|\tag{3.250–3.251}$$
with $\theta_j=\sigma(\tilde\theta_j)$ (sigmoid) and $\xi_i=\sigma_+(\tilde\xi_i)$ (softplus); Jacobian terms account for the transforms. Autodiff supplies $\nabla_{\boldsymbol\omega}\log p$. HMC returns correlated samples, which are back-transformed. Posteriors of quantities $f(\boldsymbol\theta)$ are estimated by Monte Carlo (pp. 109–110).

*3.6.1.2 Rats dataset.* Rats developing a tumour in a clinical trial (details in [Gel+14a]). Some groups have $\hat\theta_j=0$, well below the pooled MLE. Posterior means $\mathbb E[\theta_j|\mathcal D]$ move low-count groups up toward the population mean $\mathbb E[a/(a+b)|\mathcal D]$ and high-count groups down toward it. The groups regularize each other; this is **shrinkage**, with strength controlled by the prior on $(a,b)$, inferred from data (Fig. 3.15a). Fig. 3.15b is a forest plot of 95% credible intervals, usable to judge whether a group differs from a target value (pp. 110–111).

*Intuition note.* Treating group rates as draws from one population lets the data decide how alike the groups are. Little data in a group means the estimate leans on the population; much data means it stands on its own.

**3.6.2 Hierarchical Gaussian.** $y_{ij}\sim\mathcal N(\theta_j,\sigma^2)$ with shared fixed $\sigma^2$. $N_j$ observations act like one mean $y_j=\frac1{N_j}\sum_iy_{ij}$ with variance $\sigma_j^2=\sigma^2/N_j$ (known). Model: $\theta_j\sim\mathcal N(\mu,\tau^2)$,
$$p(\mu,\tau^2,\boldsymbol\theta_{1:J}|\mathcal D)\propto p(\mu)p(\tau^2)\prod_j\mathcal N(\theta_j|\mu,\tau^2)\mathcal N(y_j|\theta_j,\sigma_j^2)\tag{3.252}$$
(Fig. 3.19a) (p. 111).

*3.6.2.1 Eight schools.* Effect of a coaching programme on SAT scores ([Gel+14a, Sec 5.5]); each school is summarized by mean $\bar y_{\cdot j}$ and standard deviation $\sigma_j$ (Fig. 3.16a). The pooled estimate is precision-weighted:
$$\bar y_{\cdot\cdot}=\frac{\sum_j\frac1{\sigma_j^2}\bar y_{\cdot j}}{\sum_j\frac1{\sigma_j^2}}\tag{3.253}$$
School 0 has an unusually large improvement (28 points) compared to the overall mean, suggesting that estimating $\theta_0$ from $\mathcal D_0$ alone might be unreliable (p. 112). HMC gives marginal posteriors $p(\theta_j|\mathcal D)$ (Fig. 3.16b), shrunk toward the global mean $\bar\mu=\mathbb E[\mu|\mathcal D]$, close to $\bar y_{\cdot\cdot}$. Fixing hyperparameters at posterior means, $p(\mu,\tau^2|\mathcal D)=\delta(\mu-\bar\mu)\delta(\tau^2-\bar\tau^2)$ (3.254), gives $p(\theta_j|\mathcal D)\approx p(\theta_j|\mathcal D_j,\bar\mu,\bar\tau^2)$ (3.255) via Sec. 3.4.3.1. Then
$$\mathbb E[\theta_j|\mathcal D,\bar\mu,\bar\tau^2]=w_j\bar\mu+(1-w_j)\hat\theta_j,\quad w_j=\frac{\sigma_j^2}{\sigma_j^2+\tau^2}\tag{3.256–3.257}$$
with $\hat\theta_j=y_j$ (the printed 3.257 has $\tau^2$, not $\bar\tau^2$). There is more shrinkage for groups with lower measurement precision (e.g. smaller samples) and when $\tau^2$ is smaller. $\tau^2$ is unknown; Fig. 3.17 shows its posterior (mean of $\tau$ 3.6; 95% HPD interval from 0.00051 to 9.9) (p. 112).

*3.6.2.2 Non-centered parameterization (part ends mid-section).* Posterior inference is hard for many algorithms because $\tau^2$ and the $\theta_j$ depend tightly on each other, giving a *funnel* (Fig. 3.18). With local moves, small $\tau^2$ (strong shrinkage) is reachable only if all $\theta_j$ are near $\mu$, which may need all groups to move together. A standard fix is
$$\theta_j=\mu+\tau\eta_j,\qquad\eta_j\sim\mathcal N(0,1)\tag{3.258–3.259}$$
(Fig. 3.19b) (p. 113). The text breaks off at "By writing $\theta_j$ as a deterministic function of…".

## Toy example (ours, not from the text)
**A. Gaussian update (3.99–3.103).** Known $\sigma^2=1$ ($\lambda=1$). Prior $\mathcal N(0,4)$: $\breve m=0$, $\breve\lambda=1/4=0.25$. Data: $N=4$, $\bar y=2$.
- Posterior precision: $\widehat\lambda=0.25+4\cdot1=4.25$, so $\widehat\tau^2=1/4.25=4/17\approx0.235$.
- Mean: $\widehat m=(4\cdot1\cdot2+0.25\cdot0)/4.25=8/4.25=32/17\approx1.882$.
- Check with (3.100): weights are $\sigma^2/(N\breve\tau^2+\sigma^2)=1/17$ on the prior mean and $16/17$ on $\bar y$, giving $\frac1{17}\cdot0+\frac{16}{17}\cdot2=32/17$ ✓.

**B. Shrinkage (3.256–3.257).** Take hyperparameters fixed at $\bar\mu=0$, $\tau^2=1$, and two groups with the same observed mean $y_j=2$ but $\sigma_1^2=1$, $\sigma_2^2=4$.
- Group 1: $w=1/(1+1)=0.5$, so $\mathbb E[\theta_1]=0.5\cdot0+0.5\cdot2=1$.
- Group 2: $w=4/(4+1)=0.8$, so $\mathbb E[\theta_2]=0.8\cdot0+0.2\cdot2=0.4$.
- The noisier group is shrunk more.

## Concepts
- [[conjugate-prior]] — prior family whose posterior stays in the family; closed-form update for exponential families (p. 83)
- [[prior-distribution]] — here often expressed as virtual data (pseudo-counts $\breve\alpha$, strengths $\breve\kappa,\breve\nu$) (pp. 84, 97)
- [[posterior-distribution]] — obtained by adding data statistics to prior parameters in conjugate models (p. 84)
- [[marginal-likelihood]] — ratio of normalizers, e.g. $B(\mathbf N+\boldsymbol\alpha)/B(\boldsymbol\alpha)$, and $Z(\widehat{\boldsymbol\tau},\widehat\nu)h(\mathcal D)/Z(\breve{\boldsymbol\tau},\breve\nu)$ (pp. 85, 97)
- [[posterior-predictive-distribution]] — integrates out parameters; Student-$t$ for the NIW model (p. 96)
- [[credible-interval]] — e.g. $\bar y\pm2s/\sqrt N$ under the Jeffreys prior (p. 90)
- [[principle-of-indifference-maximum-entropy]] — maxent prior as formalization of Laplace's insufficient reason (p. 103)
- [[kl-divergence]] — the reference prior maximizes expected KL between posterior and prior (p. 107)
- [[hierarchical-multilevel-model]] — hyperparameters $\boldsymbol\xi$ with their own prior; $\boldsymbol\xi\to\boldsymbol\theta\to\mathcal D$ (p. 108)
- [[partial-pooling-shrinkage]] — group estimates pulled to the population mean; weight $w_j=\sigma_j^2/(\sigma_j^2+\tau^2)$ (pp. 110, 112)
- [[hamiltonian-monte-carlo]] — gradient-based MCMC used for hierarchical posteriors, on transformed unconstrained parameters (p. 109)
- [[monte-carlo-integration]] — posterior of $f(\boldsymbol\theta)$ estimated from samples (p. 110)
- [[exchangeability]] — a new group "exchangeable with" existing groups gets predictive (3.247) (p. 108)
- [[normal-inverse-chi-squared-prior]] (new) — NIX conjugate prior for Gaussian mean and variance (p. 88)
- [[normal-inverse-wishart-prior]] (new) — NIW conjugate prior for multivariate Gaussian (p. 93)
- [[mixture-of-conjugate-priors]] (new) — mixture prior stays conjugate; posterior weights $\propto$ prior weight $\times$ component marginal likelihood (p. 99)
- [[heavy-tailed-prior]] (new) — e.g. Cauchy; heavy tails tend to make results more data-sensitive (in Berger's example, Cauchy gives about 4.6 vs 3.43 for the Gaussian prior) (p. 100)
- [[jeffreys-prior]] (new) — $\propto\sqrt{\det\mathbf F}$; invariant to reparameterization (p. 103)
- [[invariant-prior]] (new) — translation-invariant $p(\mu)\propto1$, scale-invariant $p(\sigma)\propto1/\sigma$ (pp. 106–107)
- [[reference-prior]] (new) — maximizes expected KL (mutual information) between prior and posterior; Jeffreys in 1-d (p. 107)
- [[lkj-prior]] (new) — prior $\propto|\mathbf R|^{\eta-1}$ on correlation matrices (p. 102)
- [[non-centered-parameterization]] (new) — $\theta_j=\mu+\tau\eta_j$ to avoid the funnel (p. 113)
- [[sensitivity-analysis]] (new) — assessing the influence of the prior on the posterior (p. 100)

## Canonical instances
- [[dirichlet-categorical-model]] — counts added to pseudo-counts; add-one smoothing as a MAP case (pp. 84–85)
- [[casino-coin-mixture-prior]] — $0.5\,\mathrm{Beta}(20,20)+0.5\,\mathrm{Beta}(30,10)$ to $0.346\,\mathrm{Beta}(40,30)+0.654\,\mathrm{Beta}(50,20)$; $\Pr(\theta>0.5|\mathcal D)=0.9604$ (pp. 99–100)
- [[berger-heavy-tail-example]] — $x=5$: Gaussian prior posterior mean 3.43 vs Cauchy about 4.6 (p. 100)
- [[alice-bob-odds-parameterization]] — Jeffreys prior invariance for the binomial (rate vs odds) (pp. 103–105)
- [[rats-tumor-dataset]] — hierarchical binomial, shrinkage of low-count groups (p. 110)
- [[eight-schools]] — hierarchical Gaussian, funnel and non-centered parameterization (pp. 111–113)

## Bridges (candidates)
- [structural-analogy] Posterior mean as convex combination of prior mean and MLE ↔ ridge regression: $\tau^2$ vs $\sigma^2$ plays the role of the $\ell_2$ penalty (p. 101) — same shrinkage mechanism in a different guise.
- [same-math] Student-$t$ as a scale mixture of Gaussians ↔ heavy-tailed robust priors: marginal over unknown variance gives the $t$ (pp. 89, 100).
- [structural-analogy] Hierarchical "borrowing strength" ↔ multi-task / transfer learning: groups share information via a common parent (p. 108).
- [same-math] Reference-prior objective (mutual information $\mathbb I(\theta,\mathcal D)$) ↔ information theory: expected KL between posterior and prior (p. 107).

## Questions this raises
- Why does the Jeffreys prior for a Gaussian depend on whether $(\mu,\sigma)$ are treated jointly or as independent (pp. 106)?
- How does one choose among half-Cauchy, half-normal and exponential priors for a group-level $\tau$, and how sensitive is eight-schools shrinkage to that choice?
- When does the non-centered parameterization stop helping, e.g. with abundant data per group?
- What does the reference prior look like in several dimensions, and when is the one-parameter-at-a-time scheme tractable (p. 107)?

## Reading notes
- **Scope:** pdf 117–147 = printed 83–113 (printed = pdf − 34). The part starts inside a block quote at the end of the preceding section (heading not on these pages), then §3.4 begins mid-page 83. It ends mid-sentence on p. 113 inside §3.6.2.2 ("By writing θ_j as a deterministic function of…"). §§3.7 onward are not covered.
- **Misprints/inconsistencies in the source (images checked):**
  - (3.121) uses $\bar x$ where $\bar y$ is meant; p. 86 uses $\bar x$ for $\bar y$. (3.175) and (3.179) use $\widehat{\boldsymbol\mu}$/$\breve{\boldsymbol\mu}$ for $\widehat{\mathbf m}$/$\breve{\mathbf m}$.
  - (3.166) prints $|\boldsymbol\Sigma|^{(\widehat\nu+D+2)/2}$ without a minus sign; from (3.159) it should be $-(\widehat\nu+D+2)/2$.
  - (3.178) is written as the derivative of $\log p$, but the printed right side is the derivative of the expression in (3.177), i.e. of $-2\log p$. This does not change where it is zero.
  - (3.203) uses $t'$ (undefined; $s'$ is meant); (3.197) uses $N$ for the sample size while (3.200)–(3.206) use $n$, and the sum index in the text above (3.202) also reuses $n$.
  - (3.219) is printed "min $\mathbb H(\mathbf p)$" although a maximum-entropy problem is meant.
  - (3.227) is printed "$n\log\phi+1$"; (3.228) shows $n\log(\phi+1)$ was meant. The Fisher "matrix" in (3.230) is a scalar. In Fig. 3.13 Bob's axis is labelled κ, not φ.
  - The Berger example is printed as $\mathcal N(\theta|0,2.19^2)$. By Eq. (3.100) with $N=1$, $\sigma^2=1$ (our check), variance 2.19 gives $5\cdot2.19/3.19\approx3.43$, the printed result, whereas $2.19^2$ would give about 4.14. So "$2.19^2$" appears to be a misprint for variance 2.19.
  - (3.234) gives $F_{\sigma\sigma}=1/(2\sigma^4)$ for $\theta=(\mu,\sigma)$, while p. 107 uses $F(\sigma)=2/\sigma^2$; not resolved here.
  - p. 111 writes $y_j\sim\mathcal N(\theta,\sigma_j^2)$ (θ_j intended). (3.257) uses $\tau^2$ where $\bar\tau^2$ is meant.
- The eq. (3.191) mean is printed as $\mathbb E[\boldsymbol\eta|\mathcal D]$ with $\mathbf s(\mathcal D)/N$ called "the MLE"; reproduced as printed.
- Figures are described only from the plots shown; no exercises in these pages.
