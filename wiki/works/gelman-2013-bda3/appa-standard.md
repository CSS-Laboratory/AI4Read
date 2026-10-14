---
id: gelman-2013-bda3/appa-standard
work: gelman-2013-bda3
unit: "Appendix A — Standard probability distributions"
pages: 577–586
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Appendix A — Standard probability distributions

## L0 — One line
Realistic distributions for complicated multivariate models can typically be built from a set of simple standard distributions, whose densities, moments, closure properties and simulation recipes are collected here.

## L1 — The gist (≤ 120 words)
This appendix is a reference. It lists the continuous and discrete distributions used as building blocks for hierarchical and mixture models. For most it gives notation, density, mean, variance (or standard deviation) and mode, and for many it states which parameter ranges make the density or integral finite. Many distributions are linked by special-case, addition or mixture relations, for example chi-square as a gamma and negative binomial as a Gamma–Poisson mixture. Simulation recipes are given for many of them, built from uniform, normal, chi-square or gamma draws. This matters because the authors say realistic models can typically be built from these simple pieces, and that it can be valuable to understand where simulated draws come from. The multivariate normal conditioning formulas (A.1)–(A.2) and the beta moment-matching formula (A.3) are the only numbered equations.

**Prerequisites:** density, mean, variance, mode; matrices (Cholesky factor, inverse, trace, determinant); conditional and marginal distributions; the gamma function.

## L2 — Key ideas
- Simulation starts from pseudorandom draws from U(0,1). A sequence can look uniform in one dimension while $m$-tuples are not randomly scattered in $m$ dimensions (p. 577).
- Location–scale draws: $\theta=a+(b-a)u$ gives U(a,b); $\theta=\mu+\sigma z$ gives N(μ,σ²); $\mu+Az$ with $AA^T=\Sigma$ gives the multivariate normal (pp. 577, 582).
- The normal has addition and mixture properties, useful for hierarchical normal models. The multivariate normal is closed under marginals, linear maps and conditioning, with explicit formulas (A.1)–(A.2) (pp. 577, 582).
- Gamma, inverse-gamma, χ², inverse-χ², exponential, Wishart and inverse-Wishart form linked families. Several are conjugate priors for normal or Poisson parameters (pp. 583–584).
- The t distribution can be interpreted as a normal mixture with inverse-gamma variances. It is simulated as $\mu+\sigma z\sqrt{\nu/x}$ and can replace the normal in robust analysis (p. 584).
- Beta and Dirichlet are conjugate priors for binomial and multinomial probabilities. They can be simulated from gamma or χ² draws, and beta parameters can be matched to moments by (A.3) (pp. 584–585).
- Discrete distributions have addition properties (Poisson, binomial) and mixture definitions. Negative binomial is Gamma–Poisson and beta-binomial is Beta–binomial, which also give simulation algorithms (pp. 585–586).

## L3 — Walkthrough

### Introduction (p. 577)
- Tables A.1 and A.2 give notation, density, parameter meaning, mean, mode and standard deviation. The random variable is called θ in the printed pages (ω in the text layer). The exceptions are $W$ for the Wishart and inverse-Wishart, and Σ for the LKJ correlation matrix (p. 577).
- Realistic distributions for hierarchical and mixture models can typically be built from these simple ones. The authors use preprogrammed generators (e.g. in R) but say it is valuable to understand where the numbers come from (p. 577).

### A.1 Continuous distributions

**Uniform (p. 577).**
- It represents a variable known to lie in an interval and equally likely anywhere in it. A noninformative form arises as $a\to-\infty$, $b\to\infty$.
- If $u\sim U(0,1)$, then $\theta=a+(b-a)u\sim U(a,b)$.
- Table (p. 579): density $1/(\beta-\alpha)$ on $[\alpha,\beta]$; mean $(\alpha+\beta)/2$; variance $(\beta-\alpha)^2/12$; no mode.

**Univariate normal (p. 577).**
- Sample averages are approximately normal by the central limit theorem. A flat form arises as the variance $\to\infty$ (as printed). The density is always finite. The integral is finite as long as σ is finite. σ = 0 is a point mass.
- Draw: if $z$ is standard normal, then $\theta=\mu+\sigma z\sim N(\mu,\sigma^2)$.
- **Addition property.** If $\theta_1\sim N(\mu_1,\sigma_1^2)$ and $\theta_2\sim N(\mu_2,\sigma_2^2)$ are independent, then $\theta_1+\theta_2\sim N(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.
- **Mixture property.** If $\theta_1|\theta_2\sim N(\theta_2,\sigma_1^2)$ and $\theta_2\sim N(\mu_2,\sigma_2^2)$, then $\theta_1\sim N(\mu_2,\sigma_1^2+\sigma_2^2)$. This is useful for hierarchical normal models.
- Table (p. 579): density $\frac{1}{\sqrt{2\pi}\sigma}\exp\!\big(-\frac{1}{2\sigma^2}(\theta-\mu)^2\big)$; mean = mode = μ; variance σ².

*Intuition note.* Adding independent normals adds means and variances. Putting a normal prior on the centre of a normal gives a wider normal: the two sources of uncertainty add.

**Lognormal (p. 582).**
- If $\theta>0$ and $\log\theta\sim N(\mu,\sigma^2)$, θ is lognormal. The Jacobian of the log transformation gives the density, mean, variance and mode below.
- The geometric mean and geometric standard deviation are $e^{\mu}$ and $e^{\sigma}$.
- Table (p. 579): $p(\theta)=(\sqrt{2\pi}\sigma\theta)^{-1}\exp\!\big(-\frac{1}{2\sigma^2}(\log\theta-\mu)^2\big)$; mean $\exp(\mu+\tfrac12\sigma^2)$; variance $\exp(2\mu+\sigma^2)(\exp(\sigma^2)-1)$; mode $\exp(\mu-\sigma^2)$.

**Multivariate normal (p. 582).**
- The density is always finite. The integral is finite as long as $\det(\Sigma^{-1})>0$. A noninformative form arises as $\det(\Sigma^{-1})\to0$, but this limit is not uniquely defined.
- **Draw.** Take the Cholesky factor $A$, lower-triangular with $AA^T=\Sigma$. If $z=(z_1,\dots,z_d)$ are independent standard normals, then $\theta=\mu+Az$ is a draw from N(μ,Σ).
- Marginals of any subset of components are normal. Any linear transformation is normal, with dimension equal to the rank of the transformation. The conditional distribution constrained to a linear subspace is normal.
- **Addition.** For independent $\theta_1\sim N(\mu_1,\Sigma_1)$ and $\theta_2\sim N(\mu_2,\Sigma_2)$ of the same dimension: $\theta_1+\theta_2\sim N(\mu_1+\mu_2,\Sigma_1+\Sigma_2)$.
- **Conditioning.** Partition $\theta=(U,V)$. Then $p(U|V)$ is multivariate normal with
$$E(U|V)=E(U)+\mathrm{cov}(U,V)\,\mathrm{var}(V)^{-1}(V-E(V)),$$
$$\mathrm{var}(U|V)=\mathrm{var}(U)-\mathrm{cov}(U,V)\,\mathrm{var}(V)^{-1}\mathrm{cov}(V,U),\tag{A.1}$$
where $\mathrm{cov}(V,U)$ is a rectangular submatrix of Σ and $\mathrm{cov}(U,V)=\mathrm{cov}(V,U)^T$.
- With the matrix of conditional coefficients $C=I-[\mathrm{diag}(\Sigma^{-1})]^{-1}\Sigma^{-1}$,
$$(\theta_i\mid\theta_j,\ \text{all } j\ne i)\sim N\Big(\mu_i+\sum_{j\ne i}c_{ij}(\theta_j-\mu_j),\ [(\Sigma^{-1})_{ii}]^{-1}\Big).\tag{A.2}$$
- **Hierarchical form (generalized mixture property).** If $U|V\sim N(XV,\Sigma_{U|V})$ and $V\sim N(\mu_V,\Sigma_V)$, then the joint is
$$\theta=\begin{pmatrix}U\\V\end{pmatrix}\sim N\!\left(\begin{pmatrix}X\mu_V\\ \mu_V\end{pmatrix},\begin{pmatrix}X\Sigma_VX^T+\Sigma_{U|V} & X\Sigma_V\\ \Sigma_VX^T & \Sigma_V\end{pmatrix}\right).$$
- The weighted sum of squares $SS=(\theta-\mu)^T\Sigma^{-1}(\theta-\mu)$ has a $\chi^2_d$ distribution. For any $A$ with $AA^T=\Sigma$, the conditional distribution of $A^{-1}(\theta-\mu)$ given $SS$ is uniform on a $(d-1)$-dimensional sphere.
- Table (p. 579): density $(2\pi)^{-d/2}|\Sigma|^{-1/2}\exp(-\tfrac12(\theta-\mu)^T\Sigma^{-1}(\theta-\mu))$; mean = mode = μ; variance Σ.
- Shapes (our added note): $\mu$ is $d\times1$; $\Sigma$, $A$ are $d\times d$; $z$ is $d\times1$.

*Intuition note.* Marginals, linear maps and conditionals of a multivariate normal are again normal, and (A.1)–(A.2) give their means and variances by matrix algebra. In (A.1) the conditional mean is linear in $V$, and the conditional variance is $\mathrm{var}(U)$ minus a correction term.

**Gamma (p. 583).**
- It is the conjugate prior for the inverse of the normal variance and for the Poisson mean. The integral is finite if α > 0; the density is finite if α ≥ 1.
- Many packages draw gamma variables directly. Otherwise they can be built from uniform draws, and the best method depends on α.
- **Addition.** If $\theta_1\sim\text{Gamma}(\alpha_1,\beta)$ and $\theta_2\sim\text{Gamma}(\alpha_2,\beta)$ are independent with the same β, then $\theta_1+\theta_2\sim\text{Gamma}(\alpha_1+\alpha_2,\beta)$.
- The log of a gamma variable is approximately normal. The one-third power gives an even better normal approximation.
- Table (p. 579): density $\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{\alpha-1}e^{-\beta\theta}$; mean α/β; variance α/β²; mode $(\alpha-1)/\beta$ for α ≥ 1.

**Inverse-gamma (p. 583).** If $\theta^{-1}$ is Gamma(α,β), then θ is inverse-gamma. The density is always finite and the integral is finite if α > 0. It is the conjugate prior for the normal variance. A noninformative form arises as α, β → 0. Table (p. 579): density $\frac{\beta^\alpha}{\Gamma(\alpha)}\theta^{-(\alpha+1)}e^{-\beta/\theta}$; mean $\beta/(\alpha-1)$ for α > 1; variance $\beta^2/((\alpha-1)^2(\alpha-2))$ for α > 2; mode $\beta/(\alpha+1)$.

**Chi-square (p. 583).** It is Gamma with α = ν/2, β = ½. The addition property holds because the inverse scale is fixed: $\chi^2_{\nu_1}+\chi^2_{\nu_2}\sim\chi^2_{\nu_1+\nu_2}$ for independent variables. Table (p. 579): mean ν; variance 2ν; mode ν − 2 for ν ≥ 2.

**Inverse chi-square and scaled version (p. 583).**
- Inv-χ² is Inv-gamma with α = ν/2, β = ½. The scaled Inv-χ²(ν,s²) is useful for variance parameters in normal models.
- **Draw:** take $X\sim\chi^2_\nu$ and set $\theta=\nu s^2/X$.
- Table (p. 579): the scaled version equals Inv-gamma(α = ν/2, β = νs²/2), with mean $\frac{\nu}{\nu-2}s^2$, variance $\frac{2\nu^2}{(\nu-2)^2(\nu-4)}s^4$, and mode $\frac{\nu}{\nu+2}s^2$. The unscaled Inv-χ²_ν has mean $1/(\nu-2)$ (ν > 2), variance $2/((\nu-2)^2(\nu-4))$ (ν > 4), and mode $1/(\nu+2)$.

**Exponential (p. 583).** It is the waiting time for the next event in a Poisson process and equals Gamma(α = 1, β). **Draw:** if $U\sim U(0,1)$, then $-\log(U)/\beta$ is Expon(β). Table (p. 579): density $\beta e^{-\beta\theta}$; mean 1/β; variance 1/β²; mode 0.

**Laplace (p. 579).** Density $\frac{1}{2\sigma}\exp(-|\theta-\mu|/\sigma)$; mean = mode = μ; variance $2\sigma^2$.

**Weibull (p. 583).**
- If θ > 0 and $(\theta/\beta)^\alpha\sim\text{Expon}(1)$, θ is Weibull with shape α > 0 and scale β > 0. It is often used for failure times in reliability analysis.
- The Jacobian gives density $\frac{\alpha}{\beta^\alpha}\theta^{\alpha-1}\exp(-(\theta/\beta)^\alpha)$; mean $\beta\Gamma(1+\tfrac1\alpha)$; variance $\beta^2[\Gamma(1+\tfrac2\alpha)-(\Gamma(1+\tfrac1\alpha))^2]$; mode $\beta(1-\tfrac1\alpha)^{1/\alpha}$.

*Intuition note.* Several named distributions are special cases of the gamma. Chi-square is the gamma with α = ν/2, β = ½ and exponential is the gamma with α = 1. Inverse-χ² is a special case of the inverse-gamma, which is the distribution of θ when θ⁻¹ is gamma. The addition property for fixed β explains why summing independent chi-squares just adds degrees of freedom.

**Wishart (p. 584).**
- It is the conjugate prior for the inverse covariance matrix of a multivariate normal and a multivariate generalization of the gamma. The integral is finite if ν ≥ k; the density is finite if ν ≥ k + 1. A noninformative form arises as ν → 0. The sample covariance matrix of i.i.d. multivariate normal data is Wishart.
- **Draw:** simulate $\alpha_1,\dots,\alpha_\nu$ independently from a $k$-dimensional N(0,S) and set $\theta=\sum_{i=1}^\nu\alpha_i\alpha_i^T$. This works only for a proper distribution, ν ≥ k.
- Table (p. 579): $p(W)\propto|S|^{-\nu/2}|W|^{(\nu-k-1)/2}\exp(-\tfrac12\mathrm{tr}(S^{-1}W))$ for positive definite $W$, with normalising constant $\big(2^{\nu k/2}\pi^{k(k-1)/4}\prod_{i=1}^k\Gamma(\tfrac{\nu+1-i}{2})\big)^{-1}$; $E(W)=\nu S$.

**Inverse-Wishart (p. 584).** If $W^{-1}\sim\text{Wishart}_\nu(S)$, then $W$ is inverse-Wishart. It is the conjugate prior for the multivariate normal covariance matrix. The density and the integral are always finite. A degenerate form occurs when ν < k. Table (p. 579): $p(W)\propto|S|^{\nu/2}|W|^{-(\nu+k+1)/2}\exp(-\tfrac12\mathrm{tr}(SW^{-1}))$, with the same normalising constant as the Wishart; $E(W)=(\nu-k-1)^{-1}S$.

**LKJ correlation (p. 584).**
- (Lewandowski, Kurowicka and Joe, 2009.) It is a distribution over correlation matrices: positive-definite symmetric matrices with unit diagonal. $\text{LkjCorr}(\Sigma|\eta)\propto\det(\Sigma)^{\eta-1}$, with η > 0.
- η can be interpreted like the shape of a symmetric beta. If η = 1, the density is uniform over correlation matrices of a given order. If η > 1, the mode is the identity, and the distribution concentrates around it as η grows. For 0 < η < 1, the density has a trough at the identity.
- Table (p. 579), as printed: $p(\Sigma)=\det(\Sigma)^{\eta-1}\times 2^{\sum_{i=1}^k(2\eta-2+k-i)(k-i)}\times\prod_{i=1}^k\big(\mathrm{B}(\tfrac{i+1}{2},\tfrac{i+1}{2})\big)^k$; $E(\Sigma)=I_k$.

**t (p. 584).**
- It is the marginal posterior for a normal mean with unknown variance and conjugate prior. It can be interpreted as a mixture of normals with a common mean and inverse-gamma variances. It is also the ratio of a normal to the square root of an independent gamma variable.
- **Draw:** take $z$ standard normal and $x\sim\chi^2_\nu$; set $\theta=\mu+\sigma z\sqrt{\nu/x}$.
- The density is always finite. The integral is finite if ν > 0 and σ is finite. As ν → ∞ it approaches N(μ,σ²). ν = 1 is the Cauchy. It can replace a normal in a robust analysis.
- **Multivariate:** draw $z\sim N(0,I)$ and $x\sim\chi^2_\nu$, then $\mu+Az\sqrt{\nu/x}$ with $AA^T=\Sigma$.
- Table (p. 581): density $\frac{\Gamma((\nu+1)/2)}{\Gamma(\nu/2)\sqrt{\nu\pi}\sigma}\big(1+\frac1\nu(\frac{\theta-\mu}{\sigma})^2\big)^{-(\nu+1)/2}$; mean μ for ν > 1; variance $\frac{\nu}{\nu-2}\sigma^2$ for ν > 2; mode μ. The multivariate t has the same moments with Σ in place of σ² (p. 581).

**Beta (pp. 584–585).**
- It is the conjugate prior for the binomial probability. The density is finite if α, β ≥ 1 and the integral is finite if α, β > 0. α = β = 1 gives the uniform. α = β = 0.5 and α = β = 0 are sometimes used as noninformative densities.
- **Draw:** simulate $x_\alpha\sim\chi^2_{2\alpha}$ and $x_\beta\sim\chi^2_{2\beta}$, then $\theta=x_\alpha/(x_\alpha+x_\beta)$.
- **Method of moments** for quick parameter estimates:
$$\alpha+\beta=\frac{E(\theta)(1-E(\theta))}{\mathrm{var}(\theta)}-1,\qquad \alpha=(\alpha+\beta)E(\theta),\quad \beta=(\alpha+\beta)(1-E(\theta)).\tag{A.3}$$
- The $k$th order statistic of $n$ independent U(0,1) variables is Beta(k, n − k + 1).
- Table (p. 581): density $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\theta^{\alpha-1}(1-\theta)^{\beta-1}$; mean $\frac{\alpha}{\alpha+\beta}$; variance $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$; mode $\frac{\alpha-1}{\alpha+\beta-2}$.

**Dirichlet (p. 585).**
- It is the conjugate prior for multinomial parameters and a multivariate generalization of the beta. The integral is finite if all α's are positive; the density is finite if all are ≥ 1.
- The marginal of $\theta_j$ is Beta(α_j, α₀ − α_j). A subvector's marginal is Dirichlet, e.g. $(\theta_i,\theta_j,1-\theta_i-\theta_j)\sim\text{Dirichlet}(\alpha_i,\alpha_j,\alpha_0-\alpha_i-\alpha_j)$. The conditional of a subvector given the rest is Dirichlet under $\sum_j\theta_j=1$.
- **Fast sampling:** draw $x_j$ from independent gammas with shapes $\alpha_j$ and a common scale, and set $\theta_j=x_j/\sum_i x_i$.
- **Slower sampling:** $\theta_1\sim\text{Beta}(\alpha_1,\sum_{i\ge2}\alpha_i)$. For $j=2,\dots,k-1$, draw $\phi_j\sim\text{Beta}(\alpha_j,\sum_{i>j}\alpha_i)$ and set $\theta_j=(1-\sum_{i<j}\theta_i)\phi_j$. Finally $\theta_k=1-\sum_{i<k}\theta_i$.
- Table (p. 581): $E(\theta_j)=\alpha_j/\alpha_0$; $\mathrm{var}(\theta_j)=\frac{\alpha_j(\alpha_0-\alpha_j)}{\alpha_0^2(\alpha_0+1)}$; $\mathrm{cov}(\theta_i,\theta_j)=-\frac{\alpha_i\alpha_j}{\alpha_0^2(\alpha_0+1)}$; mode $\frac{\alpha_j-1}{\alpha_0-k}$.

**Constrained distributions (p. 585).** N⁺ denotes the normal constrained to be positive (truncated normal). The half-t is the right half of the t.

**Logistic and log-logistic (pp. 580–581).** Logistic: density $\frac{\exp(-(\theta-\mu)/\sigma)}{\sigma(1+\exp(-(\theta-\mu)/\sigma))^2}$; mean = mode = μ; variance $\sigma^2\pi^2/3$. Log-logistic (scale α, shape β): density $\frac{(\beta/\alpha)(\theta/\alpha)^{\beta-1}}{(1+(\theta/\alpha)^\beta)^2}$; mode $\alpha\big(\frac{\beta-1}{\beta+1}\big)^{1/\beta}$ for β > 1; variance as printed $\alpha^2\frac{2\pi/\beta}{\sin(2\pi/\beta)}$ for β > 2 (not checked). No prose text is given for these two.

### A.2 Discrete distributions

**Poisson (p. 585).** It represents counts, such as arrivals in a fixed period. Addition: $\text{Poisson}(\lambda_1)+\text{Poisson}(\lambda_2)\sim\text{Poisson}(\lambda_1+\lambda_2)$ for independent variables. Simulation of most discrete distributions can be cumbersome. Table lookup can invert the CDF. Table (p. 581): $p(\theta)=\frac{1}{\theta!}\lambda^\theta e^{-\lambda}$; mean = variance = λ; mode $\lfloor\lambda\rfloor$.

**Binomial (pp. 585–586).** It counts successes in $n$ i.i.d. Bernoulli trials with success probability $p$. For large $n$ it is approximately normal. Addition: $\text{Bin}(n_1,p)+\text{Bin}(n_2,p)\sim\text{Bin}(n_1+n_2,p)$. For small $n$, simulate by drawing $n$ uniforms and counting those ≤ $p$. $n=1$ is the Bernoulli. Table (p. 581): mean $np$; variance $np(1-p)$; mode $\lfloor(n+1)p\rfloor$.

**Multinomial (p. 586).** It generalizes the binomial. The marginal of a single $\theta_i$ is binomial. The conditional of a subvector is multinomial, with $n$ reduced by the fixed components and probabilities rescaled to sum to one. **Simulation:** $\theta_1\sim\text{Bin}(n,p_1)$. For $j=2,\dots,k-1$, $\theta_j\sim\text{Bin}\big(n-\sum_{i<j}\theta_i,\ p_j/\sum_{i\ge j}p_i\big)$. Then $\theta_k=n-\sum_{i<k}\theta_i$. Convention: Bin(0,p) is identically zero. Table (p. 581): $E(\theta_j)=np_j$; $\mathrm{var}=np_j(1-p_j)$; $\mathrm{cov}(\theta_i,\theta_j)=-np_ip_j$.

**Negative binomial (p. 586).**
- It is the marginal distribution of a Poisson variable whose rate has a Gamma(α,β) prior. It is a robust alternative to the Poisson: same sample space, one extra parameter.
- **Draw:** $\lambda\sim\text{Gamma}(\alpha,\beta)$, then $\theta\sim\text{Poisson}(\lambda)$.
- As α → ∞ with α/β → constant, it approaches Poisson(α/β). With $p=\beta/(\beta+1)$, θ is the number of Bernoulli failures before α successes, success probability $p$.
- Table (p. 581): $p(\theta)=\binom{\theta+\alpha-1}{\alpha-1}\big(\frac{\beta}{\beta+1}\big)^\alpha\big(\frac{1}{\beta+1}\big)^\theta$; mean α/β; variance $\frac{\alpha}{\beta^2}(\beta+1)$.

**Beta-binomial (p. 586).** It is the marginal of a binomial whose success probability has a Beta(α,β) prior. It is a robust alternative to the binomial. **Draw:** $\phi\sim\text{Beta}(\alpha,\beta)$, then $\theta\sim\text{Bin}(n,\phi)$. Table (p. 581): mean $n\frac{\alpha}{\alpha+\beta}$; variance $n\frac{\alpha\beta(\alpha+\beta+n)}{(\alpha+\beta)^2(\alpha+\beta+1)}$.

*Intuition note.* Both extra distributions come from letting a parameter vary: a random rate or probability gives a marginal count law with one more parameter, which the authors suggest as a robust alternative to the plain Poisson or binomial (p. 586). The same mixture definition gives the simulation recipe: draw the parameter first, then the data.

### A.3 Bibliographic note (p. 586)
Software packages contain simulation routines. Gentle (2003) discusses simulation of all of these in detail, except LKJ; Ripley (1987) is a general simulation text; Johnson and Kotz (1972) give details such as characteristic functions; Press et al. (1986) has Fortran and C code for uniform, normal, gamma, Poisson and binomial (p. 586).

## Toy example (ours, not from the text)
Goal: simulate a Dirichlet(2,1,1) draw and an Expon(2) draw, then check them against the appendix rules.
1. Exponential: take β = 2 and $U=0.25$. Then $-\log(U)/\beta=\ln 4/2=1.3863/2=0.6931$.
2. A second draw with $U=0.5$ gives $\ln 2/2=0.6931/2=0.3466$.
3. Both are Expon(2) = Gamma(1,2). By the gamma addition property, their sum $0.6931+0.3466=1.0397$ is a draw from Gamma(2,2), whose mean is α/β = 2/2 = 1.
4. Dirichlet: suppose gamma draws (common scale) with shapes (2,1,1) came out as $x=(1.2,0.6,0.2)$. The sum is 2.0. So $\theta=(1.2/2.0,\ 0.6/2.0,\ 0.2/2.0)=(0.6,0.3,0.1)$, which sums to 1.
5. Check against the table: the marginal of $\theta_1$ is Beta(α₁, α₀ − α₁) = Beta(2,2), with mean $2/4=0.5$. The Dirichlet mean is $\alpha_1/\alpha_0=2/4=0.5$, which agrees.

## Concepts
- [[standard-distributions]] (new) — the catalogue of named distributions used as building blocks for hierarchical and mixture models (p. 577)
- [[conjugate-prior]] — gamma for the inverse normal variance and Poisson mean; inverse-gamma for the normal variance; Wishart for the inverse covariance matrix; inverse-Wishart for the covariance matrix; beta for the binomial; Dirichlet for the multinomial (pp. 583–585)
- [[hierarchical-model]] — the normal mixture property (and its multivariate form) gives the marginal law of a normal with a normally distributed mean (pp. 577, 582)
- [[distribution-addition-property]] (new) — sums of independent variables stay in the family, with parameters adding, under the stated conditions (e.g. same β for gamma) (pp. 577, 583, 585)
- [[cholesky-sampling]] (new) — draw $\mu+Az$ with $AA^T=\Sigma$ to get a multivariate normal (p. 582)
- [[mixture-simulation]] (new) — simulate a marginal by drawing the parameter first, then the data (p. 586)
- [[normal-conditioning-formulas]] (new) — $E(U|V)$ and $\mathrm{var}(U|V)$ in (A.1), and the full conditional in (A.2) (p. 582)
- [[method-of-moments-beta]] (new) — match a beta's mean and variance via (A.3) (p. 585)
- [[improper-noninformative-limits]] (new) — flat or noninformative forms as limits (σ → ∞, α, β → 0, ν → 0), with conditions for finite density or integral (pp. 577, 583, 584)

## Canonical instances
- [[gamma-poisson-negative-binomial]] — a gamma-distributed Poisson rate gives a negative binomial count (p. 586)
- [[beta-binomial-mixture]] — a beta-distributed success probability gives a beta-binomial count (p. 586)
- [[normal-normal-hierarchy]] — $\theta_1|\theta_2\sim N(\theta_2,\sigma_1^2)$, $\theta_2\sim N(\mu_2,\sigma_2^2)$ gives $\theta_1\sim N(\mu_2,\sigma_1^2+\sigma_2^2)$ (p. 577)
- [[t-as-normal-scale-mixture]] — t can be interpreted as a normal mixture with inverse-gamma variances (p. 584)

## Bridges (candidates)
- [same-math] Normal mixture property ↔ bayesian: the marginal law of data under a normal prior on the mean, with variances adding — the same variance-addition calculation.
- [same-math] Gamma-to-Dirichlet sampling ↔ bayesian: normalised independent gammas as Dirichlet, as beta is the two-component case.
- [structural-analogy] Negative binomial / beta-binomial as overdispersed versions of Poisson / binomial ↔ bayesian: hierarchical models, where letting a parameter vary across units widens the marginal distribution.
- [structural-analogy] Heavy-tailed t as a robust replacement for the normal ↔ bayesian: scale-mixture representations of outlier-robust likelihoods.

## Questions this raises
- Why does a gamma mixing distribution on a Poisson rate give exactly a negative binomial? (The text states it but does not derive it.)
- How do the normalising constants and sampling recipes for LKJ and Wishart work in practice for large $k$?
- When should one choose a half-t or LKJ prior over the conjugate gamma or inverse-Wishart priors for scale and covariance parameters?
- Which noninformative limits (σ → ∞, α, β → 0, ν → 0) give proper posteriors?

## Reading notes
- Printed page = pdf page − 10 (pdf 587 = printed 577).
- The text layer replaces θ with ω and "~" with "→". It also garbles the tables, subscripts and minus signs. The page images show θ and ∼; I used the images, and θ throughout.
- The log-logistic mean (p. 581) is printed as $1/(1+(x/\alpha)^{-\beta})$ (the symbol inside looks like $x$ or θ). It contains a variable, so I did not copy it as a mean. I also did not check the log-logistic variance as printed.
- The LKJ density constant on p. 579 is copied as printed. I did not verify it. The Beta-function arguments printed there contain no η.
- Typo on p. 584: "for with the parameter η required to be positive". The Wishart simulation uses $\alpha_i$ for normal vectors, which clashes with the gamma shape α.
- The Dirichlet fast method (p. 585) says "common scale and shape parameters α₁,…,α_k". I read this as common scale and shape parameters $\alpha_j$.
- The Weibull mode formula is printed without a stated parameter range.
- The normal section says the variance "σ → ∞" for the flat limit (as printed; σ is the scale elsewhere).
- The unit has no exercises.
