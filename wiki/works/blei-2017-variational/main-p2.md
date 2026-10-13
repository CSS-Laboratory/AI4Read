---
id: blei-2017-variational/main-p2
work: blei-2017-variational
unit: paper (part 2/2) — end of Section 4, Section 5 (Discussion), Appendices A–C
pages: 22–41
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Blei, Kucukelbir & McAuliffe (2017), Variational Inference — part 2: applications, theory, extensions, appendices

## L0 — One line
Variational inference (VI) turns posterior computation into optimization. It is already used widely, has only partial theory, has been extended beyond conditional conjugacy (including by Monte Carlo gradients), and the appendices give a CAVI derivation for ARD regression, a Gaussian mixture specification with Stan code, and CAVI updates for LDA.

## L1 — The gist (≤ 120 words)
This part closes the review of variational inference (VI), which approximates a posterior by optimizing within a simple family. It shows topic modelling of 1.8M New York Times articles made possible by stochastic VI. It then surveys applications, summarizes consistency results that each cover one model and one approximation family, covers models without conditional conjugacy (including "black box" Monte Carlo-gradient methods), and lists open problems: other divergences, richer families, VI with MCMC, and statistical properties. Three appendices give explicit coordinate-ascent updates for Bayesian linear regression with automatic relevance determination and for latent Dirichlet allocation, and specify a Gaussian mixture of image histograms with Stan code.

**Prerequisites:** KL divergence and the ELBO; mean-field family and coordinate-ascent VI (CAVI); exponential families, conjugacy and complete conditionals; Gaussian/Gamma/Dirichlet distributions; digamma function Ψ.

## L2 — Key ideas (5–10 bullets)
- Stochastic VI (SVI) scales mean-field VI to millions of documents. Topics were inferred from 1.8M New York Times articles, an analysis the authors say would not have been possible without SVI (p. 22). Algorithm 3 is SVI for conditionally conjugate models (p. 23).
- VI is used across computational biology, vision and robotics, neuroscience, language and speech, and other fields. The authors say this list is not exhaustive (pp. 23–24).
- Theory is thin. The known results treat VI posterior means (or variational-EM estimates) as point estimates and check frequentist asymptotics. Each concerns one model and one variational family. Mostly they find consistency, but the variational covariance can be "too small" (pp. 24–25).
- Models whose complete conditionals are not exponential-family (e.g., Bayesian logistic regression) break the standard ELBO expectations and coordinate updates (p. 25). Remedies are tailored bounds, delta/Laplace methods, message passing, and Monte Carlo gradients of the ELBO (pp. 25–26).
- Open problems: other divergences (α-divergences, expectation propagation), richer families than mean-field (which can underestimate posterior variances), combining VI with MCMC, and understanding VI as an estimator (p. 26).
- Appendix A derives CAVI for Bayesian linear regression with an ARD prior. The optimal factors are normal-gamma for $(\beta,\tau)$ and Gamma for each relevance variable $\alpha_d$ (pp. 27–28).
- Appendix B specifies a diagonal-covariance Gaussian mixture, with hyperparameter values and Stan code that marginalizes the discrete assignments (pp. 29–30).
- Appendix C gives LDA's generative process and its CAVI updates, Equations (59)–(61), and Algorithm 4 (pp. 31–32).

## L3 — Walkthrough

### End of Section 4: topic modelling at scale (p. 22)
- Motivation: get a handle on massive document collections. Early algorithms were CAVI (Blei et al., 2003) and handled thousands or tens of thousands of documents (p. 22).
- With SVI, topic models scale to millions of documents. Figure 7 shows 15 topics inferred with latent Dirichlet allocation (LDA) from 1.8M New York Times articles. Each topic is shown as a list of words. Topic 1 has game, season, team, coach…; topic 10 has government, war, military, iraq… (p. 22).
- The authors state this analysis would not have been possible without SVI. Appendix C presents the CAVI algorithm; the SVI details are in Hoffman et al. (2013) (p. 22).

### 5 Discussion (pp. 22–23)
Recap in the authors' words:
- VI approximates $p(\mathbf z\mid\mathbf x)$. It posits a family $\mathcal Q$ and finds the member $q^*(\cdot)$ closest in KL divergence. The complexity of the optimization is governed by the complexity of the family (p. 22).
- The mean-field family is fully factorized. It suits coordinate ascent, which iteratively optimizes each factor. This is closely connected to the classical Gibbs sampler (p. 22).
- Examples shown earlier: Bayesian mixture of Gaussians, exponential families with conditional conjugacy, and SVI for massive data (pp. 22–23).

**Algorithm 3 (SVI for conditionally conjugate models)** (p. 23)
- Input: model $p(\mathbf x,\mathbf z)$, data $\mathbf x$, step sizes $\epsilon_t$. Output: global variational densities $q_\lambda(\beta)$. Initialize $\lambda_0$.
- Repeat forever:
  1. Pick $t\sim\mathrm{Unif}(1,\dots,n)$.
  2. Optimize its local variational parameters: $\varphi_t^*=\mathbb E_\lambda[\eta(\beta,x_t)]$.
  3. Compute the coordinate update as though $x_t$ were repeated $n$ times:
$$\hat\lambda=\alpha+n\,\mathbb E_{\varphi_t^*}[f(z_t,x_t)]$$
  4. Update the global parameter: $\lambda_t=(1-\epsilon_t)\lambda_t+\epsilon_t\hat\lambda_t$.

*Intuition note.* One random data point is treated as if the whole dataset consisted of $n$ copies of it. That gives a noisy "ideal" global parameter $\hat\lambda$. The step size $\epsilon_t$ moves the current $\lambda$ a fraction of the way toward it.

### 5.1 Applications (pp. 23–24)
The authors focus on mean-field and structured VI based on KL, and say the list is not exhaustive (p. 23).
- **Computational biology:** genome-wide association, regulatory networks, motif detection, phylogenetic HMMs, population genetics, gene expression (p. 23).
- **Vision and robotics:** VI has been important since its inception. Examples include image manifolds, video layers, video models, denoising, tracking, place recognition and mapping, segmentation with Bayesian nonparametrics, and joint segmentation, clustering and annotation (p. 23).
- **Neuroscience:** autoregressive processes, multi-subject hierarchical models, spatial models, brain–computer interfaces, factor models. A software toolbox exists (pp. 23–24).
- **Language and speech:** parsing, grammar induction, streaming text, topic models, HMM tagging; coupled HMMs and switching dynamical systems for speech (p. 24).
- **Other:** marketing, control and reinforcement learning, network analysis, astrophysics, social sciences. General VI algorithms exist for shrinkage, time-series, robust, and Gaussian process models (p. 24).

### 5.2 Theory (pp. 24–25)
- The authors say researchers have not developed much theory. One of their purposes in writing the paper is to catalyze such research (p. 24).
- All results below are of one type. They treat VI posterior means (or M-step estimates from variational EM) as point estimates and check the usual frequentist asymptotics. Sometimes these are not enjoyed. Each result concerns one model and one family of approximations (p. 24).
- **You et al. (2014):** Bayesian linear model with a normal prior on coefficients and an inverse-gamma prior on the response variance. Under standard regularity conditions, the mean-field variational posterior means are frequentist-consistent. Ormerod et al. (2014) find similar consistency with a spike-and-slab prior (p. 24).
- **Hall et al. (2011a,b):** Poisson mixed-effects model with one predictor and a random intercept, Gaussian variational approximation, variational EM. They prove consistency at the parametric rate and asymptotic normality with asymptotically valid standard errors (p. 24).
- **Celisse et al. (2012), Bickel et al. (2013):** stochastic blockmodels. They show asymptotic normality of mean-field estimates. They highlight computational advantages and theoretical guarantees over maximum likelihood for dense, sparse and restricted variants (pp. 24–25).
- **Westling & McCormick (2015):** consistency via M-estimation, for models with posterior support in real coordinate space and an automated Gaussian-VI technique. They derive an asymptotic covariance estimator and show robustness to misspecification (p. 25).
- **Wang & Titterington (2006):** Bayesian Gaussian mixtures with conjugate priors, mean-field, variational posterior mean. They confirm that CAVI converges to a local optimum and that the VI estimator is consistent. The VI estimate and the MLE approach each other at rate $\mathcal O(1/n)$. **Wang & Titterington (2005):** the asymptotic variational posterior covariance is "too small". It differs from the MLE covariance (inverse Fisher information) by a positive-definite matrix (p. 25).

*Intuition note.* VI point estimates can behave like standard estimators (consistent, asymptotically normal) in specific models. For Gaussian mixtures, Wang and Titterington show the asymptotic variational covariance is too small. These results cover single models, not a general theory.

### 5.3 Beyond conditional conjugacy (pp. 25–26)
- The paper focused on models whose complete conditional is in the exponential family. Many models lack this property (p. 25).
- Example, Bayesian logistic regression (p. 25):
$$\beta_k\sim\mathcal N(0,1),\qquad y_i\mid x_i,\beta\sim\mathrm{Bern}(\sigma(\beta^\top x_i)),$$
  with $\sigma$ the logistic function. The posterior is not in an exponential family. So the expectations in the first term of the ELBO (Eq. 13) and the coordinate update (Eq. 18) cannot be computed (p. 25).
- Model-specific fixes (p. 25):
  - Jaakkola & Jordan (1997, 2000): a variational bound tailored to logistic regression.
  - Blei & Lafferty (2007) adapted it to nonconjugate topic models, and others improved it.
  - Braun & McAuliffe (2010): a delta method for the discrete choice model.
  - Wand et al. (2011): auxiliary variables, quadrature and mixture approximations.
- General recipes (p. 25):
  - Wang & Blei (2013): Laplace approximations and the delta method.
  - Knowles & Minka (2011): the Jaakkola–Jordan bound inside message passing, later simplified by Wand (2014).
  - Tan & Nott: message passing for generalized linear mixed models, combined with SVI.
  - Rohde & Wand (2015): unified these developments.
- Monte Carlo (MC) gradients (pp. 25–26): write the ELBO gradient as an expectation, estimate it by MC, and run stochastic optimization with repeated MC gradients. This appeared independently in several papers (Ji et al.; Nott et al.; Paisley et al.; Wingate & Weber). The newest "black box" methods avoid model-specific derivations. Kucukelbir et al. (2016) apply the ideas to any model written in Stan. The authors call this a step towards a derivation-free, easy-to-use VI algorithm (p. 26).

*Intuition note.* When the exact coordinate update has no closed form, one can still follow a noisy but usable estimate of the ELBO's gradient. The newest "black box" methods use this to avoid model-specific derivations.

### 5.4 Open problems (p. 26)
- **Other objectives.** The paper optimized $\mathrm{KL}(q(z)\|p(z\mid x))$. Promising: other measures such as α-divergences. Expectation propagation is inspired by KL "in the other direction", between $p(z\mid x)$ and $q(z)$. Others use bounds tighter than the ELBO. Alternatives may be hard to optimize, but may give better approximations.
- **Richer families.** Mean-field makes strong independence assumptions. They help scalable optimization but limit expressiveness, and can exacerbate local optima and underestimation of posterior variance (see Figure 1). The goal is better approximations with efficient optimization. Existing directions: structured VI, Gaussian families with non-diagonal covariance, post-processing mean-field parameters to correct variances (Giordano et al.), and embedding mean-field parameters in a hierarchical model (Ranganath et al.).
- **VI and MCMC.** The interface is relatively unexplored. Examples: fitted variational distributions as part of a Metropolis–Hastings proposal; MCMC to approximate coordinate updates; a variational approximation to the MCMC chain that trades accuracy for speed. A principled analysis of when to use or combine them would have theoretical and practical impact.
- **Statistical properties.** They are not yet well understood, especially compared with MCMC. The open problem is to understand VI as an estimator and its statistical profile relative to the exact posterior.

### Appendix A: Bayesian linear regression with automatic relevance determination (ARD) (pp. 27–28)
**Setup.** $\mathbf y\in\mathbb R^n$, $\mathbf x\in\mathbb R^{n\times D}$ with rows $x_i\in\mathbb R^D$, coefficients $\beta\in\mathbb R^D$. ARD gives each coefficient its own latent precision-scaling $\alpha_d$. The hyper-prior encourages small values of $\alpha$, which selects relevant coefficients (p. 27). Gaussians use the precision parameterization.
$$p(\mathbf y\mid\beta,\tau;\mathbf x)=\prod_{i=1}^n\mathcal N(y_i\mid\beta^\top x_i,\tau)$$
$$p(\beta,\tau\mid\alpha)=\mathcal N(\beta\mid 0,\tau\,\mathrm{diag}(\alpha))\,\mathrm{Gam}(\tau\mid a_0,b_0),\qquad p(\alpha)=\prod_{d=1}^D\mathrm{Gam}(\alpha_d\mid c_0,d_0)$$
$a_0,b_0,c_0,d_0$ are fixed. The posterior $p(\beta,\tau,\alpha\mid\mathbf y;\mathbf x)$ has no closed form. Without $\alpha$, the normal-gamma is conjugate to the normal likelihood with unknown mean and precision (p. 27).

**Variational family:** $q(\beta,\tau,\alpha)=q(\beta,\tau)\,q(\alpha)$, with $\beta,\tau$ in one factor (p. 27).

**Factor $q(\beta,\tau)$** from Eq. (18) (p. 27):
$$\begin{aligned}\log q(\beta,\tau)&=\log p(\mathbf y\mid\beta,\tau;\mathbf x)+\mathbb E_\alpha[\log p(\beta,\tau\mid\alpha)]+\text{const.}\\&=\Big(\tfrac D2+a_0-1+\tfrac n2\Big)\log\tau-\tfrac\tau2\Big(\beta^\top\big(\mathbb E_\alpha[\mathrm{diag}\,\alpha]+\textstyle\sum_i x_ix_i^\top\big)\beta+\sum_i y_i^2-2\beta^\top\sum_i x_iy_i+2b_0\Big)+\text{const.}\\&=\log\mathcal N(\beta\mid\beta_*,\tau V_*^{-1})+\log\mathrm{Gam}(\tau\mid a_*,b_*).\end{aligned}$$
(Added step: the $D/2$ in the $\log\tau$ coefficient is the normalizing power of $\tau$ in the $D$-dimensional normal factor, so only $a_0+n/2$ remains in $a_*$.) Parameters (p. 28):
$$V_*^{-1}=\mathbb E_\alpha[\mathrm{diag}\,\alpha]+\sum_i x_ix_i^\top,\quad \beta_*=V_*\sum_i x_iy_i,\quad a_*=a_0+\tfrac n2,\quad b_*=b_0+\tfrac12\Big(\sum_i y_i^2-\beta_*^\top V_*^{-1}\beta_*\Big).$$
Shapes: $V_*^{-1}$ is $D\times D$, $\beta_*\in\mathbb R^D$.

**Factor $q(\alpha)=\prod_d q(\alpha_d)$** from Eq. (18) (p. 28):
$$\log q(\alpha_d)=\mathbb E_{\beta,\tau}[\log p(\beta,\tau\mid\alpha_d)]+\log p(\alpha_d)+\text{const.}=\Big(c_0-1+\tfrac D2\Big)\log\alpha_d-\alpha_d\Big(d_0+\tfrac12\mathbb E_{\beta,\tau}[\tau\beta_d^2]\Big)+\text{const.}=\log\mathrm{Gam}(\alpha_d\mid c_*,d_{*d})$$
(printed as shown; see Reading notes on $D/2$). Parameters:
$$c_*=c_0+\tfrac12,\qquad d_{*d}=d_0+\tfrac12\mathbb E_{\beta,\tau}[\tau\beta_d^2].$$

**Needed expectations** (p. 28), with $[\cdot]_d$ the $d$th diagonal entry:
$$\mathbb E_\alpha[\mathrm{diag}\,\alpha]=c_*\,\mathrm{diag}\,1/d_*,\qquad \mathbb E_{\beta,\tau}[\tau\beta_d^2]=\beta_{*d}^2\,a_*/b_*+[V_*]_d.$$
CAVI iterates $a_*,b_*,c_*,d_*,V_*^{-1},\beta_*$. These quantities also define the ELBO; Drugowitsch (2013) gives the algebra (p. 28).

*Intuition note.* The coefficient factor depends on $\alpha$ only through $\mathbb E_\alpha[\mathrm{diag}\,\alpha]$, and each $d_{*d}$ depends on $\beta$ only through $\mathbb E[\tau\beta_d^2]$. Each factor is updated using the other's expectations, which is the usual CAVI alternation.

### Appendix B: Gaussian mixture model of image histograms (pp. 29–30)
**Shapes** (p. 29): $n$ observations $\mathbf x\in\mathbb R^{n\times D}$; $K$ components; assignments $\mathbf z\in\mathbb R^{n\times K}$ (each $z_i$ a $K$-indicator vector); mixing vector $\pi$ in the $K$-simplex; means $\mu\in\mathbb R^{K\times D}$; precisions $\tau\in\mathbb R^{K\times D}$, each $\tau_k\in\mathbb R^D_{>0}$.

Joint density (p. 29):
$$p(\mathbf x,\mathbf z,\pi,\mu,\tau)=p(\mathbf x\mid\mathbf z,\mu,\tau)\,p(\mathbf z\mid\pi)\,p(\pi)\,p(\mu\mid\tau)\,p(\tau).$$
Components (precision parameterization):
$$p(\mathbf x\mid\mathbf z,\mu,\tau)=\prod_{i=1}^n\prod_{k=1}^K\Big(\prod_{d=1}^D\mathcal N(x_{id}\mid\mu_{kd},\tau_{kd})\Big)^{z_{ik}},\qquad p(\mathbf z\mid\pi)=\prod_{i=1}^n\prod_{k=1}^K\pi_k^{z_{ik}},$$
$$p(\pi)=\mathrm{Dir}(\pi\mid a_0)=C(a_0)\prod_{k=1}^K\pi_k^{a_0-1},$$
$$p(\mu\mid\tau)p(\tau)=\prod_{k=1}^K\prod_{d=1}^D\mathcal N(\mu_{kd}\mid m_0,b_0\tau_{kd})\,\mathrm{Gam}(\tau_{kd}\mid\alpha_0,\beta_0).$$
Hyperparameters: $a_0=1/K$, $m_0=0.0$, $b_0=1.0$, $\alpha_0=1.0$, $\beta_0=1.0$. Bishop (2006, Ch. 10.2) derives CAVI for this model. Figure 8 gives Stan code. Stan does not support discrete latent variables, so the code marginalizes over assignments (p. 29).

Figure 8 (p. 30): parameters are `theta` (simplex of mixing proportions), `mu[K]`, and `sigma[K]` (commented "standard deviations"). The model block puts `dirichlet(alpha0_vec)` on `theta`, `normal(0, 1/sigma[k])` on `mu[k]` and `inv_gamma(1,1)` on `sigma[k]`. For each data point it accumulates `ps[k] = log(theta[k]) + normal_log(x[n], mu[k], sigma[k])` and adds `log_sum_exp(ps)` to the log probability. That log-sum-exp is the marginalization over $z$.

### Appendix C: Latent Dirichlet allocation (pp. 31–32)
**Model** (p. 31). LDA is a conditionally conjugate mixed-membership topic model. A topic is a distribution over the vocabulary. $K$ topics, vocabulary size $V$. Generative process:
1. For $k=1..K$: $\beta_k\sim\mathrm{Dir}_V(\eta)$.
2. For $d=1..D$: $\theta_d\sim\mathrm{Dir}_K(\alpha)$; for $n=1..N$: $z_{dn}\sim\mathrm{Mult}(\theta_d)$, then $w_{dn}\sim\mathrm{Mult}(\beta_{z_{dn}})$.

Here $\eta\in\mathbb R_{>0}$ is a fixed symmetric-Dirichlet parameter and $\alpha\in\mathbb R^K_{>0}$ is fixed. $z_{dn}$ is a $K$-vector with $z_{dn}^k=1$ if word $n$ of document $d$ is assigned to topic $k$. $w_{dn}$ is a $V$-vector with $w_{dn}^v=1$ if that word is vocabulary term $v$.

The posterior $p(\beta,\theta,\mathbf z\mid w)$ is not available in closed form. $\mathbf z$ and $\theta$ are conjugate, but introducing $\beta$ makes the posterior analytically intractable (p. 31).

**Mean-field family** (p. 31):
$$q(\beta,\theta,\mathbf z)=\prod_{k=1}^K q(\beta_k;\lambda_k)\prod_{d=1}^D\Big(q(\theta_d;\gamma_d)\prod_{n=1}^N q(z_{dn};\phi_{dn})\Big).$$
Because LDA is conditionally conjugate, each factor's family is read off its complete conditional (Section 4.2) (p. 31).

**Complete conditionals** (pp. 31–32):
$$p(z_{dn}=k\mid\theta_d,\beta,w_{dn})\propto\exp\big(\log\theta_{dk}+\log\beta_{k,w_{dn}}\big)\ \text{(multinomial; } q \text{ has parameters }\phi_{dn})$$
$$p(\theta_d\mid\mathbf z_d)=\mathrm{Dir}_K\Big(\alpha+\sum_{n=1}^N z_{dn}\Big)\ (q:\ \gamma_d),\qquad p(\beta_k\mid\mathbf z,w)=\mathrm{Dir}_V\Big(\eta+\sum_{d=1}^D\sum_{n=1}^N z_{dn}^k w_{dn}\Big)\ (q:\ \lambda_k).$$
In words, the $v$th Dirichlet parameter of topic $k$ is $\eta$ plus the number of times term $v$ was assigned to topic $k$ (p. 32).

**CAVI updates**, a direct application of Eq. (47) to these conditionals (p. 32). Iterate for each word in each document until convergence:
$$\phi_{dn}^k\propto\exp\big(\mathbb E[\log\theta_{dk}]+\mathbb E[\log\beta_{k,w_{dn}}]\big)\propto\exp\Big(\Psi(\gamma_{dk})+\Psi(\lambda_{k,w_{dn}})-\Psi\Big(\sum_v\lambda_{kv}\Big)\Big)\tag{59}$$
$$\gamma_d=\alpha+\sum_{n=1}^N\phi_{dn}\tag{60}$$
(Added step: $\mathbb E[\log\theta_{dk}]=\Psi(\gamma_{dk})-\Psi(\sum_j\gamma_{dj})$; the subtracted term does not depend on $k$, so it vanishes in $\propto$.) Then the topic update, which depends only on $\phi_{dn}$:
$$\lambda_k=\eta+\sum_{d=1}^D\sum_{n=1}^N\phi_{dn}^k\,w_{dn}\tag{61}$$
**Algorithm 4 (CAVI for LDA)** (p. 32): initialize $\lambda,\gamma$ randomly. While the ELBO has not converged: repeat (for each document and word, update $\phi,\gamma$ by (59), (60)) until $\phi,\gamma$ converge; then update $\lambda$ by (61). The ELBO algebra is in Hoffman et al. (2013).

*Intuition note.* Each word softly votes for topics, weighted by how much its document likes the topic and how much the topic likes the word. The document's topic parameters are its prior plus the summed votes (60). Each topic's word parameters are its prior plus the votes pooled over all documents (61).

### References (pp. 33–41)
Bibliography only; not digested.

## Toy example (ours, not from the text)
Illustrates SVI's update (Algorithm 3) on the simplest conjugate case: a global parameter, no local variables.

Model: $\beta\sim\mathrm{Beta}(1,1)$ and $x_i\mid\beta\sim\mathrm{Bern}(\beta)$. The data are $n=4$ points $(1,0,1,1)$. The global parameter is $\lambda=(a,b)$, the Beta shape parameters. The coordinate update "as though $x_t$ were repeated $n$ times" gives $\hat\lambda=(1+n x_t,\ 1+n(1-x_t))$.

- Exact posterior (all data): $(1+3,\ 1+1)=(4,2)$.
- Possible $\hat\lambda$: for $x_t=1$, $(1+4,1+0)=(5,1)$; for $x_t=0$, $(1,5)$.
- Average over uniform $t$ (three 1s, one 0): $\big((5+1+5+5)/4,\ (1+5+1+1)/4\big)=(4,2)$. This equals the exact posterior, so $\hat\lambda$ is unbiased for it.
- Run with $\lambda_0=(1,1)$. Step 1: $t$ has $x=1$, $\epsilon=0.5$: $\lambda=0.5(1,1)+0.5(5,1)=(3,1)$. Step 2: $x=0$, $\epsilon=0.5$: $0.5(3,1)+0.5(1,5)=(2,3)$. Step 3: $x=1$, $\epsilon=0.25$: $0.75(2,3)+0.25(5,1)=(1.5+1.25,\ 2.25+0.25)=(2.75,\ 2.5)$.
- With shrinking $\epsilon_t$ the iterates average out the noise around the exact target $(4,2)$.

## Concepts
- [[variational-inference-elbo]] — approximate $p(z\mid x)$ by optimizing a family member to be KL-closest; the ELBO is the objective (p. 22)
- [[kl-divergence]] — the objective here is $\mathrm{KL}(q(z)\|p(z\mid x))$; EP uses the reverse direction (pp. 22, 26)
- [[mean-field-family]] (new) — fully factorized variational densities over latent variables (p. 22)
- [[coordinate-ascent-vi]] (new) — CAVI: iteratively optimize each factor given the others, linked to the Gibbs sampler (p. 22)
- [[gibbs-sampling]] — classical sampler that CAVI is closely connected to (p. 22)
- [[stochastic-variational-inference]] (new) — SVI: per-data-point noisy coordinate updates with step size $\epsilon_t$ for global parameters (p. 23)
- [[conditional-conjugacy]] (new) — complete conditionals are in the exponential family, so factors are read off directly (pp. 25, 31)
- [[conjugate-prior]] — e.g., normal-gamma conjugate to a normal likelihood with unknown mean and precision (p. 27)
- [[black-box-vi]] (new) — Monte Carlo ELBO-gradient methods needing no model-specific derivations (p. 26)
- [[automatic-relevance-determination]] (new) — a separate latent precision per regression coefficient shrinks irrelevant coefficients (p. 27)
- [[latent-dirichlet-allocation]] (new) — topic model with Dirichlet topic proportions and topics over a vocabulary (p. 31)
- [[gaussian-mixture-model]] (new) — diagonal-covariance mixture with Dirichlet, normal-gamma priors (p. 29)
- [[variance-underestimation-mean-field]] (new) — mean-field can underestimate posterior variances; the variational covariance is "too small" in the mixture analysis (pp. 25–26)
- [[hierarchical-model]] — ARD and LDA both place priors on parameters of lower-level distributions (pp. 27, 31)
- [[posterior-distribution]] — the target of approximation; closed form unavailable in ARD, GMM, LDA (pp. 27, 31)

## Canonical instances
- [[nyt-topic-model]] — LDA on 1.8M New York Times articles via SVI (p. 22)
- [[bayesian-logistic-regression-nonconjugate]] — simple model whose posterior is not exponential-family (p. 25)
- [[ard-linear-regression]] — CAVI with normal-gamma and Gamma factors (pp. 27–28)
- [[gmm-image-histograms]] — diagonal Gaussian mixture and its Stan code (pp. 29–30)
- [[lda-cavi]] — CAVI updates (59)–(61) and Algorithm 4 (pp. 31–32)

## Bridges (candidates)
- [structural-analogy] CAVI ↔ Gibbs sampling: both update one block at a time given the others, but CAVI optimizes expected log complete-conditionals (p. 22).
- [structural-analogy] LDA complete-conditional updates ↔ conjugate Bayesian updating: the Dirichlet update $\alpha+\text{counts}$ is the usual conjugate update, with expected (soft) counts $\phi$ (pp. 31–32).
- [structural-analogy] Black-box MC-gradient VI ↔ Monte Carlo integration: the ELBO gradient is written as an expectation and estimated by sampling (pp. 25–26).
- [metaphor] Variational family choice ↔ Bayesian workflow: model expansion trades richer approximations against optimization ease (p. 26).

## Questions this raises
- When does the variational mean stay consistent while the variational covariance stays too small, and can a correction (e.g., post-processing) restore valid uncertainty (pp. 25–26)?
- What would a general theory look like, not tied to one model and one family (p. 24)?
- Which gradient estimators make black-box VI reliable, and how do they compare with exact coordinate updates in conditionally conjugate models (pp. 25–26)?
- When should VI and MCMC be combined, and how can accuracy–speed trade-offs be analyzed in principle (p. 26)?

## Reading notes
- This unit is part 2 of 2. It starts at printed p. 22 (Figure 7 and the end of Section 4) and ends at p. 41 (end of the reference list). It is split at a section boundary. Printed page = pdf page.
- Equations (13), (18), (47) and Sections 3, 4.2, Figure 1 are cited on these pages, but their content is not shown here.
- Apparent misprints in the page images:
  - Algorithm 3 prints the last update as $\lambda_t=(1-\epsilon_t)\lambda_t+\epsilon_t\hat\lambda_t$ with the same index on both $\lambda$'s (p. 23).
  - In Appendix A the $\log q(\alpha_d)$ line shows $D/2$ in the $\log\alpha_d$ coefficient, while the stated result is $c_*=c_0+\tfrac12$ (p. 28). I judge $\tfrac12$ is intended, since the stated $c_*$ requires it; I copied the source line as printed.
  - Appendix B's likelihood exponent prints $z_{nk}$, while $p(\mathbf z\mid\pi)$ uses $z_{ik}$ (p. 29).
  - Appendix C says "the variational approximation to the topic proportions is a $V$-dimensional Dirichlet with parameters $\lambda_k$"; context shows this refers to the topics $\beta_k$ (p. 32).
- Appendix B text puts Gamma priors on precisions $\tau$. The Stan code (Figure 8) uses standard deviations `sigma` with an `inv_gamma(1,1)` prior and `normal(0, 1/sigma)` for `mu`. The pages do not explain the correspondence.
- Appendix text reuses $\beta$ for regression coefficients (A) and for LDA topics (C), and $\alpha$ for different objects in A (relevance variables), B ($\alpha_0$, a Gamma shape) and C (Dirichlet parameter).
