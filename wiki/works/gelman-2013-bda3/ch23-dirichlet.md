---
id: gelman-2013-bda3/ch23-dirichlet
work: gelman-2013-bda3
unit: "23 Dirichlet process models"
pages: 545–574
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Dirichlet process models (BDA3, Chapter 23)

## L0 — One line
A Dirichlet process is a prior on an unknown distribution; used as the prior of a mixing distribution, it gives a mixture model whose number of clusters is not fixed in advance but grows with the data.

## L1 — The gist (≤ 120 words)
How can Bayes place a prior on an unknown distribution, and use it to build mixture models with unlimited components? The chapter starts from a Bayesian histogram, defines the Dirichlet process (DP) through Dirichlet-distributed bin probabilities, and gives its stick-breaking form. Because DP draws are discrete, the DP is used as prior for a mixing distribution (DP mixture), fitted by Gibbs samplers that let the number of clusters grow with the data. The chapter then extends this to nonparametric residuals, functional data, groups of distributions (dependent, hierarchical, nested DPs, convex mixtures) and density regression. It matters because it relaxes parametric assumptions without fixing the number of components.

**Prerequisites:** Dirichlet, beta, gamma and normal distributions; conjugate updating; Gibbs sampling; finite mixture models (BDA Ch. 22); hierarchical models; basic regression.

## L2 — Key ideas (5–10 bullets)
- **Bayesian histogram.** With fixed bins and a Dirichlet prior on bin probabilities, the posterior is Dirichlet with the bin counts added. This is easy but sensitive to the number and location of knots (pp. 545–546).
- **Dirichlet process (DP).** Demanding a Dirichlet prior on bin probabilities for every partition defines a prior on the whole distribution $P$, written $P\sim\mathrm{DP}(\alpha P_0)$. It has mean $P_0$, a variance controlled by $\alpha$, and a conjugate posterior (pp. 546–547).
- **Discreteness and stick-breaking.** DP draws are discrete, written as infinite weighted sums of point masses with stick-breaking weights. So the DP is not appropriate as a direct prior for the data distribution, particularly for continuous data (pp. 548–549).
- **DP mixtures.** Putting the DP on a mixing measure gives an infinite mixture. Marginalising $P$ gives the Pólya urn / Chinese restaurant rule, in which the number of clusters depends on $n$, with new clusters added as data arrive (pp. 549–550).
- **Computation.** A marginal Gibbs sampler and a truncated blocked Gibbs sampler give posterior draws of clusters, weights and densities, and the number of clusters comes out automatically. The marginal likelihood penalises needless clusters, and $P_0$'s scale matters (pp. 550–554).
- **Beyond density estimation.** DPs can model error distributions, group-varying coefficients and subject-specific functions, with clusters of subjects or curves (pp. 557–560).
- **Dependent distributions.** Dependent DPs (fixed-$\pi$), hierarchical DPs (shared atoms, varying weights), nested DPs (clusters of whole distributions) and convex mixtures borrow strength across groups (pp. 561–568).
- **Density regression.** Predictor-dependent stick-breaking (kernel, probit) lets the whole conditional density $p(y\mid x)$ change with $x$ (pp. 568–571).

## L3 — Walkthrough

### 23.1 Bayesian histograms (pp. 545–546)
Setting: $y_i \overset{iid}{\sim} f$, and we want a Bayes estimate of the density $f$. The bins are given by prespecified knots $\xi_0<\xi_1<\dots<\xi_k$ with all $y_i\in[\xi_0,\xi_k]$ (p. 545).

Histogram-like density model, with $\pi=(\pi_1,\dots,\pi_k)$ an unknown probability vector (p. 545):
$$f(y)=\sum_{h=1}^{k}1_{\xi_{h-1}<y\le\xi_h}\,\frac{\pi_h}{\xi_h-\xi_{h-1}},\quad y\in\mathbb R .$$
Dirichlet prior (p. 545):
$$p(\pi\mid a)=\frac{\Gamma\!\left(\sum_{h=1}^k a_h\right)}{\prod_{h=1}^k\Gamma(a_h)}\prod_{h=1}^k \pi_h^{a_h-1}.$$
Write $a=\alpha\pi_0$, where $\pi_0=E(\pi\mid a)=\left(\frac{a_1}{\sum_h a_h},\dots,\frac{a_k}{\sum_h a_h}\right)$ is the prior mean. The scale $\alpha$ is often interpreted as a prior sample size (p. 545).

(added step) The likelihood contributes the factor $\pi_h/(\xi_h-\xi_{h-1})$ for each $y_i$ in bin $h$. The bin width does not depend on $\pi$, so the posterior is
$$p(\pi\mid y)\propto\prod_{h=1}^k\pi_h^{a_h+n_h-1}\;\overset{\mathcal D}{=}\;\mathrm{Dirichlet}(a_1+n_1,\dots,a_k+n_k),$$
with $n_h=\sum_i 1_{\xi_{h-1}<y_i\le\xi_h}$ the count in bin $h$ (pp. 545–546).

*Illustration.* Data: $n=100$ draws from $f(y)=0.75\,\mathrm{Beta}(y\mid1,5)+0.25\,\mathrm{Beta}(y\mid20,2)$. The support is $[0,1]$ with 10 equally spaced knots. The author says the estimator does "an adequate job" but is sensitive to the number and location of knots (p. 546).

*Pros and cons (author).* Conjugacy gives an analytic posterior. Prior information can be included, and interval estimates are easy. Putting a prior on the knots with reversible-jump MCMC is computationally demanding, and averaging over random knots still tends to produce artifactual bumps. The Dirichlet prior does not smooth across adjacent bins (p. 546).

**Intuition note.** The posterior just adds the bin counts to the prior pseudo-counts, so each bin probability is a compromise between prior guess and data. The weakness is that the answer depends on how you cut the axis into bins.

### 23.2 Dirichlet process prior distributions (pp. 546–549)

**Definition and basic properties.** Motivation: bypass explicit bins, which also explode in number in multivariate settings (p. 546). Let $P$ be an unknown random probability measure (RPM) on $(\Omega,\mathcal B)$. For a partition $B_1,\dots,B_k$ of $\Omega$, the bin probabilities are $P(B_h)=\int_{B_h}f(y)\,dy$, and they are random variables (p. 546). A natural prior is
$$(P(B_1),\dots,P(B_k))\sim\mathrm{Dirichlet}\big(\alpha P_0(B_1),\dots,\alpha P_0(B_k)\big),\tag{23.1}$$
where $P_0$ is a base measure (initial guess at $P$) and $\alpha$ is a concentration parameter controlling shrinkage of $P$ toward $P_0$ (p. 546).

For a fixed partition, (23.1) says nothing about how mass is spread inside a bin, so it does not fully specify a prior on $P$. The idea is to assume (23.1) for all partitions and all $k$ (p. 546). For this to be coherent, a random measure with these properties must exist. The text says existence can be shown by verifying certain consistency conditions, and the resulting $P$ is a Dirichlet process, $P\sim\mathrm{DP}(\alpha P_0)$. Here $\alpha>0$ is a precision parameter, and $P_0$ is commonly a parametric model such as a Gaussian (p. 547).

Consequences stated by the author (p. 547), for all $B\in\mathcal B$:
$$P(B)\sim\mathrm{Beta}\big(\alpha P_0(B),\,\alpha(1-P_0(B))\big),\quad E(P(B))=P_0(B),\quad \mathrm{var}(P(B))=\frac{P_0(B)(1-P_0(B))}{1+\alpha}.$$
The prior is centred on $P_0$, and $\alpha$ controls the variance. It can also be shown that the support of the DP contains all probability measures whose support lies in the support of $P_0$ (p. 547).

**Conjugacy.** Let $y_i\overset{iid}{\sim}P$ and $P\sim\mathrm{DP}(\alpha P_0)$. By finite Dirichlet conjugacy, for any partition (p. 547),
$$(P(B_1),\dots,P(B_k))\mid y\sim\mathrm{Dirichlet}\Big(\alpha P_0(B_1)+\sum_{i=1}^n1_{y_i\in B_1},\dots\Big),$$
and therefore
$$P\mid y_1,\dots,y_n\sim\mathrm{DP}\Big(\alpha P_0+\sum_i\delta_{y_i}\Big).$$
The updated precision is $\alpha+n$, so $\alpha$ is in some sense a prior sample size. The posterior mean is (p. 547)
$$E(P(B)\mid y^n)=\Big(\frac{\alpha}{\alpha+n}\Big)P_0(B)+\Big(\frac{n}{\alpha+n}\Big)\sum_{i=1}^n\frac1n\delta_{y_i}(B).\tag{23.2}$$
So the Bayes estimator under squared error loss is the empirical measure shrunk toward the base measure. As $n$ grows, the estimate converges to the empirical distribution function (p. 547).

**Bayesian bootstrap.** As $\alpha\to0$ (a "noninformative" prior in some sense), $P\mid y^n\sim\mathrm{DP}(\sum_{i=1}^n\delta_{y_i})$. This is the Bayesian bootstrap. Its draws are discrete distributions on the observed points with Dirichlet-distributed weights. Compared with the classical bootstrap, it smooths the weights (p. 548).

**Drawbacks (author).** (i) (23.2) is not smooth: ideally one would allow smooth deviations from $P_0$, which would make $P(B_1)$ and $P(B_2)$ dependent for adjacent bins. Instead the DP induces *negative* correlation between $P(B_1)$ and $P(B_2)$ for any two disjoint sets, regardless of distance. (ii) Realisations are discrete: $P$ is atomic and has no continuous density on the real line (p. 548).

**Intuition note.** Updating a DP works like updating Dirichlet bin probabilities, except that the "bins" are arbitrary. The new data points become point masses added to the prior mass $\alpha P_0$. The price is that a DP draw is a spiky discrete distribution.

**Stick-breaking construction.** The definition is indirect, so the author gives a direct representation (p. 548):
$$P(\cdot)=\sum_{h=1}^\infty\pi_h\delta_{\theta_h}(\cdot),\quad \pi_h=V_h\prod_{l<h}(1-V_l),\quad V_h\sim\mathrm{Beta}(1,\alpha),\quad\theta_h\sim P_0.\tag{23.3}$$
Atoms $\theta_h$ are drawn independently from $P_0$. The weights come from a stick-breaking process, which makes the weights sum to 1. Procedure: take a unit stick and break off $V_1\sim\mathrm{Beta}(1,\alpha)$ as $\pi_1$ for atom $\theta_1$. Break off a proportion $V_2$ of the remaining $1-V_1$ as $\pi_2=V_2(1-V_1)$, and so on. Since $E(V_h)=1/(1+\alpha)$, values of $\alpha$ near zero put high weight on the first atoms (pp. 548–549).

Figure 23.1 shows draws for $P_0=N(0,1)$ and $\alpha=0.5,1,5,10$ (p. 549). The author concludes that the DP is not appropriate as a direct prior for the data distribution, especially for continuous data. Each new subject would need a new atom, which requires large $\alpha$, so each atom has weight near zero and ties are unlikely. As $\alpha\to\infty$, $y_i\sim P_0$, so for large $\alpha$ and no ties the DP effectively models the data as drawn from the parametric base (p. 549).

**Intuition note.** A DP draw is a countable set of spikes. Small $\alpha$ puts almost all mass on a few spikes. Large $\alpha$ spreads mass over many tiny spikes that look like $P_0$.

### 23.3 Dirichlet process mixtures (pp. 549–557)

**Specification and Pólya urns.** The DP is better used as a prior for an unknown mixing measure (p. 549). The kernel mixture is
$$f(y\mid P)=\int\mathcal K(y\mid\theta)\,dP(\theta),\tag{23.4}$$
with $\mathcal K(\cdot\mid\theta)$ a kernel whose $\theta$ includes location and possibly scale. If $P$ is discrete with $k$ atoms, this is a finite mixture (Chapter 22). A DP prior on $P$ gives the DP mixture (DPM) (pp. 549–550):
$$f(y)=\sum_{h=1}^\infty\pi_h\mathcal K(y\mid\theta_h^*),\quad\pi\sim\mathrm{stick}(\alpha),\ \theta_h^*\sim P_0.\tag{23.5}$$
Infinitely many components exist, but not infinitely many are occupied by the sample: new components are introduced as subjects are added. Equivalent hierarchical form: $y_i\sim\mathcal K(\theta_i)$, $\theta_i\sim P$, $P\sim\mathrm{DP}(\alpha P_0)$ (p. 550).

Posterior computation looks problematic because $P$ has infinitely many parameters and joint conjugacy is lost. The way around it is to marginalise out $P$, which gives the Pólya urn predictive rule (p. 550):
$$p(\theta_i\mid\theta_1,\dots,\theta_{i-1})\sim\Big(\frac{\alpha}{\alpha+i-1}\Big)P_0(\theta_i)+\sum_{j=1}^{i-1}\Big(\frac1{\alpha+i-1}\Big)\delta_{\theta_j}.\tag{23.6}$$

*Chinese restaurant metaphor* (p. 550). The first customer sits at a table with dish $\theta_1$. The second sits at the first table with probability $\frac1{1+\alpha}$ or at a new table with probability $\frac\alpha{1+\alpha}$. In general the $i$th customer joins an occupied table with probability proportional to its number $c_j$ of customers, or a new table with probability proportional to $\alpha$ (see Reading notes on the printed denominator). Tables are clusters, and the rate at which new clusters are added is proportional to $\alpha\log n$ asymptotically. The number of clusters therefore depends probabilistically on $n$, unlike a finite mixture where $k$ does not depend on $n$. The author likens this to the good practice of manually adding components until the data fit (p. 550).

By exchangeability (p. 550):
$$\theta_i\mid\theta_{-i}\sim\Big(\frac\alpha{\alpha+n-1}\Big)P_0(\theta_i)+\sum_{h=1}^{k^{(-i)}}\Big(\frac{n_h^{(-i)}}{\alpha+n-1}\Big)\delta_{\theta_h^{*(-i)}},\tag{23.7}$$
where $\theta_h^*$ are the $k^{(-i)}$ unique values of $\theta^{(-i)}$ and $n_h^{(-i)}=\sum_{j\ne i}1_{\theta_j=\theta_h^*}$.

**Intuition note.** The rule says "join an existing cluster in proportion to its size, or start a new one with weight $\alpha$". Big clusters attract more members, and $\alpha$ sets how readily new clusters appear.

**Marginal Gibbs sampler (p. 551).** If $P_0$ is conjugate to $\mathcal K$ (e.g. normal kernel with $\theta=(\mu,\phi)$ mean and precision, normal-gamma $P_0$), the full conditional of $\theta_i$ has the form (23.7) with updated weights and updated $P_0$. Updating the $\theta_i$ one at a time tends to mix poorly. The alternative separates allocation and cluster parameters. Let $\theta^*=(\theta_1^*,\dots,\theta_k^*)$ be the unique values and $S_i=c$ if $\theta_i=\theta_c^*$. Alternate:

1. Sample $S_i$ from the multinomial
$$\Pr(S_i=c\mid-)\propto\begin{cases}n_c^{(-i)}\mathcal K(y_i\mid\theta_c^*),&c=1,\dots,k^{(-i)}\\ \alpha\int\mathcal K(y_i\mid\theta)\,dP_0(\theta),&c=k^{(-i)}+1.\end{cases}$$
The last case is a singleton cluster.
2. Sample each unique value from $p(\theta_c^*\mid-)\propto P_0(\theta_c^*)\prod_{i:S_i=c}\mathcal K(y_i\mid\theta_c^*)$. This is the ordinary parametric posterior for the subjects in cluster $c$.

With conjugate $P_0$, the integral in step 1 is analytic and step 2 has the form of $P_0$ with updated parameters. For a Gaussian kernel with normal-inverse-gamma $P_0$ it is the same form as in the finite mixture case of Chapter 22. Non-conjugate modifications exist (p. 551).

*Role of $\alpha$ and $P_0$ (p. 551).* The new-cluster probability is proportional to $\alpha$ times the marginal likelihood of $y_i$ under $P_0$. If $\alpha$ is near zero, or that marginal likelihood is small relative to the likelihoods under occupied clusters, $y_i$ tends to join an existing cluster. As $\alpha\to0$ one gets the parametric model with a common $\theta$. In practice $\alpha=1$ is often set to favour allocation to few clusters, or a gamma hyperprior is used with an extra MCMC step.

The author warns that a naive high-variance $P_0$ is not "ignorance" (similarly to Section 7.4). It lowers the marginal likelihood for new clusters, so it effectively places a heavy penalty on new clusters. As the variance of $P_0\to\infty$, the posterior behaves as if there were one common $\theta$ (pp. 551–552). Recommendation: an informative $P_0$ placing high probability on clusters near the support of the data, helped by standardising the data (p. 552).

Differences from the finite-mixture sampler: the weights $\pi$ are marginalised out and the number of clusters varies across draws. The posterior of $k$ is obtained automatically, with no need for reversible jump MCMC. Predictive density for $y_{n+1}$, averaged over posterior draws (p. 552):
$$p(y)=\sum_{c=1}^k\Big(\frac{n_c}{n+\alpha}\Big)\mathcal K(y\mid\theta_c^*)+\Big(\frac\alpha{n+\alpha}\Big)\int\mathcal K(y\mid\theta)\,dP_0(\theta).$$
The finite mixture sampler of Chapter 22 approximates the DPM if the component parameters are iid from $P_0$ and $\pi\sim\mathrm{Dirichlet}(\frac\alpha k,\dots,\frac\alpha k)$. The approximation improves with $k$, and $k=25$ or $50$ "can work well" as a conservative bound (p. 552).

**Blocked Gibbs sampler (pp. 552–553).** Marginalising $P$ gives up inference on $P$; avoiding marginalisation opens the door to generalisations of DPMs where marginalisation is not analytically possible. Instead truncate (23.5): the stick-breaking weights are stochastically decreasing, so $\sum_{h>N}\pi_h$ is near zero for large $N$. Setting $V_N=1$ gives $\pi_h=0$ for $h>N$. Default $N=25$ or $50$; the author reports rarely needing more than 10 or 15 clusters to fit the density. It is unclear whether this or the finite Dirichlet approximation is more efficient, though exchangeability of components in the latter helps mixing (p. 552). Steps:

1. $\Pr(S_i=c\mid-)=\dfrac{\pi_c\mathcal K(y_i\mid\theta_c^*)}{\sum_{c'=1}^N\pi_{c'}\mathcal K(y_i\mid\theta_{c'}^*)}$, $c=1,\dots,N$.
2. For $c=1,\dots,N-1$: $V_c\sim\mathrm{Beta}\big(1+n_c,\ \alpha+\sum_{c'=c+1}^Nn_{c'}\big)$.
3. Update $\theta_c^*$ as in the finite mixture model; unoccupied clusters ($n_c=0$) are drawn from $P_0$ (p. 553).

To estimate the density, evaluate $f(y)=\sum_{c=1}^N\pi_c\mathcal K(y\mid\theta_c^*)$ at each iteration on a dense grid (e.g. 100 equally spaced values from min minus a buffer to max plus a buffer). Monitor $S_{\max}=\max(S_1,\dots,S_n)$ and increase $N$ if it is near $N$. Monitor convergence on the sampled $f(y)$, not on component parameters, since label ambiguity often causes poor mixing of the component parameters, which may not affect the induced density. Slow mixing from multimodal posteriors over clusterings can be partly addressed by label-switching moves and split-merge algorithms (p. 553).

**Hyperprior for $\alpha$ (pp. 553–554).** Fixing $\alpha=1$ means two randomly selected individuals have a 50–50 chance of sharing a cluster in the prior. Alternatively, $\alpha\sim\mathrm{Gamma}(a_\alpha,b_\alpha)$ is conditionally conjugate in the blocked sampler:
$$\alpha\mid-\sim\mathrm{Gamma}\Big(a_\alpha+N-1,\ b_\alpha-\sum_{h=1}^{N-1}\log(1-V_h)\Big).$$
The author's experience is that data are informative about $\alpha$, with a high-variance prior often giving a concentrated posterior. This does not contradict maximum-likelihood overfitting, because the Bayesian approach favours a high *marginal* likelihood. Many clusters enlarge the space integrated over, which gives "an intrinsic penalty" favouring few clusters actually needed, with no tendency to overfit (pp. 553–554).

**Choice of $P_0$ (p. 554).** $P_0$ induces the prior for cluster locations. If its variance is too high, the marginal-likelihood penalty for separate clusters is large and the model overly favours a single cluster. The variance of $P_0$ is meaningful only relative to the data scale, so standardise $y$ and centre $P_0$ at zero with near-unit variance. Otherwise changing units (e.g. inches to miles) can give completely different results.

**Intuition note.** More clusters give a better fit but spread the prior mass thinner, so the marginal likelihood falls unless the extra clusters are needed. That is why the data can inform $\alpha$ without overfitting. Too-wide $P_0$ makes new clusters look implausible.

**Example: toxicology application (pp. 554–557).** Data: number of implantations $y_i$ in pregnant mice, ethylene glycol, dose groups 0, 750, 1500, 3000 mg/kg/day, with sizes 25, 24, 23, 23. The control group is underdispersed, with mean 12.5 and variance 6.8 (p. 554).

*(a) DP directly on the data distribution*, $P_0=\mathrm{Poisson}(\bar y)$, $\alpha=1$ or $5$. No MCMC is needed:
$$\Pr(y=j\mid y_1,\dots,y_n)=\Big(\frac\alpha{\alpha+n}\Big)P_0(j)+\Big(\frac1{\alpha+n}\Big)\sum_{i=1}^n1_{y_i=j}.$$
This is a weighted average of prior and empirical proportions. With a subsample of size 10, the posterior mean looks like the base measure with high peaks at the observed $y$. As $n$ grows the empirical pmf increasingly dominates. The lack of smoothing is "unappealing" (p. 554–555, Figs 23.2–23.3).

*(b) DPM of Poissons* (23.8): $y_i\sim\mathrm{Poisson}(\theta_i)$, $\theta_i\sim P$, $P\sim\mathrm{DP}(\alpha P_0)$, $P_0=\mathrm{Gamma}(a,b)$. The blocked Gibbs steps are (pp. 555–556): (1) $S_i$ multinomial with $\pi_c\,\mathrm{Poisson}(y_i\mid\theta_c^*)$ normalised; (2) $V_c\sim\mathrm{Beta}(1+n_c,\alpha+\sum_{c'>c}n_{c'})$; (3) $\theta_h^*\sim\mathrm{Gamma}(a+\sum_{i:S_i=h}y_i,\ b+n_h)$. Here $n_c=\sum_i1_{S_i=c}$, and $N=n$ is a conservative truncation. Problem: the Poisson kernel forces mean = variance, so mixing can only increase the variance relative to the mean. It suits only overdispersed counts and fits these data poorly, with variance substantially larger than the empirical one (p. 556).

*(c) DPM of rounded Gaussians* (23.9):
$$y_i=h(y_i^*),\ y_i^*\sim N(\mu_i,\tau_i^{-1}),\ (\mu_i,\tau_i)\sim P,\ P\sim\mathrm{DP}(\alpha P_0).$$
Here $h(y^*)=j$ if $y^*\in(a_j,a_{j+1}]$ for $j=0,1,2,\dots$, with $a_0=-\infty$, $a_j=j-1$ for $j\ge1$. The base measure is $P_0(\mu,\tau)=N(\mu\mid\mu_0,\kappa\tau^{-1})\mathrm{Gamma}(\tau\mid a_\tau,b_\tau)$. Blocked Gibbs (p. 556):

1. $\Pr(S_i=c\mid-)=\dfrac{\pi_c\,p(y_i\mid\mu_c^*,\tau_c^*)}{\sum_{c'}\pi_{c'}p(y_i\mid\mu_{c'}^*,\tau_{c'}^*)}$, with $p(y_i\mid\mu,\tau)=\Phi(a_{j+1}\mid\mu,\tau)-\Phi(a_j\mid\mu,\tau)$ for $y_i=j$. Here $\Phi(z\mid\mu,\tau)$ is the normal cdf with location $\mu$ and precision $\tau$.
2. $V_h\sim\mathrm{Beta}(1+n_c,\alpha+\sum_{c'=c+1}^Nn_{c'})$.
3. $u_i\sim U\big(\Phi(a_{y_i}\mid\mu^*_{S_i},\tau^*_{S_i}),\Phi(a_{y_i+1}\mid\mu^*_{S_i},\tau^*_{S_i})\big)$, $y_i^*=\Phi^{-1}(u_i\mid\mu^*_{S_i},\tau^*_{S_i})$.
4. $(\mu_c^*,\tau_c^*)\sim N(\mu_c^*\mid\hat\mu_c,\hat\kappa_c\tau_c^{-1})\mathrm{Gamma}(\tau_c\mid\hat a_{\tau_c},\hat b_{\tau_c})$ with $\hat a_{\tau_c}=a_\tau+\frac{n_c}2$, $\hat b_{\tau_c}=b_\tau+\frac12\big(\sum_{i:S_i=c}(y_i^*-\bar y_c^*)^2+\frac{n_c}{1+\kappa n_c}(\bar y_c^*-\mu_0)^2\big)$, $\hat\kappa_c=(\kappa^{-1}+n_c)^{-1}$, $\hat\mu_c=\hat\kappa_c(\kappa^{-1}\mu_0+n_c\bar y_c^*)$. (Index and square as corrected; see Reading notes.)

Essentially, only step 3, imputing the latent $y_i^*$, is new. For continuous data observed directly as $y_i^*$, step 3 is not needed (p. 557). The rounded-Gaussian DPM gave "an excellent fit": empirical cdfs lay inside pointwise 95% credible intervals. Posterior probability of a negative average change across percentiles relative to control: 0.72 (750), 0.99 (1500), 0.94 (3000 mg/kg). The author reads this as substantial evidence of a stochastic decrease in implants in the two higher dose groups (p. 557).

### 23.4 Beyond density estimation (pp. 557–560)
The real attraction of DPMs is relaxing parametric assumptions in hierarchical models (p. 557).

**Nonparametric residual distributions.** Linear regression $y_i=X_i\beta+\epsilon_i$, $\epsilon_i\sim f$ (23.10) (p. 557). The $t_\nu$ error is a scale mixture of normals: $\epsilon_i\sim N(0,\phi_i^{-1}\sigma^2)$, $\phi_i\sim\mathrm{Gamma}(\frac\nu2,\frac\nu2)$. Replace this by a DP scale mixture: $\epsilon_i\sim N(0,\phi_i^{-1})$, $\phi_i\sim P$, $P\sim\mathrm{DP}(\alpha P_0)$, $P_0=\mathrm{Gamma}(\frac\nu2,\frac\nu2)$. This is centred on a $t$ distribution, but $f$ is still unimodal and symmetric about zero. To remove those restrictions, use a location mixture: $\epsilon_i\sim N(\mu_i,\tau^{-1})$, $\mu_i\sim P$, $P\sim\mathrm{DP}(\alpha P_0)$, $\tau\sim\mathrm{Gamma}(a_\tau,b_\tau)$, $P_0=N(0,\tau^{-1})$, with no intercept in $X_i\beta$. Computation: add steps for $\beta$ and replace $y_i$ by $y_i-X_i\beta$ (p. 557).

**Parameters varying by group.** One-factor ANOVA (23.11): $y_{ij}=\mu_i+\epsilon_{ij}$, $\mu_i\sim f$, $\epsilon_{ij}\sim g$. Parametric: $f=N(\mu,\psi^{-1})$, $g=N(0,\sigma^2)$. Nonparametric: $\mu_i\sim P$, $P\sim\mathrm{DP}(\alpha P_0)$ (23.12), with $g=N(0,\sigma^2)$. This induces a latent class model (23.13): $\mu_i=\mu^*_{S_i}$, $\Pr(S_i=h)=\pi_h$ with stick-breaking $\pi_h$. Different subjects can have identical parameter values, but posterior means of $\mu_i$ still differ across subjects because the clustering is soft (p. 558).

Identifiability and interpretation (p. 558): if $n_i=1$ for all subjects, the data cannot separate between-subject from within-subject variation. Under normal $g$, $P$ still absorbs lack of fit of the normal residual. For general $n_i\ge1$, $P$ has a dual role (lack of fit of residuals and systematic subject variability), and the latter dominates with many observations per subject. To remove the confounding one can also model $g$ by a DPM of Gaussians, but then accurate estimation may need many items and many observations per item. Restricting the mean to zero is hard in nonparametric Bayes models. The suggested remedy is to run the MCMC for an overparameterised model without mean restrictions and post-process to get the overall mean and mean-centred quantities.

**Functional data analysis (pp. 559–560).** Observations $y_{ij}\sim N(f_i(t_{ij}),\sigma^2)$ (23.14), with basis expansion $f_i(t)=\sum_{h=1}^H\theta_{ih}b_h(t)$ and subject-specific coefficients $\theta_i=(\theta_{i1},\dots,\theta_{iH})$. A common dictionary of bases gives a backbone for borrowing information, and zero or near-zero coefficients allow subject-specific selection (p. 559).

Parametric option: $\theta_i\sim P=N_H(\theta,\Omega)$, giving a population mean curve $\bar f(t)=b(t)\theta$. Problems the author lists: $\Omega$ has many parameters; there is no subject-specific basis selection (a prior on $\Omega$ with near-zero diagonals would drop a basis for all subjects); normality cannot accommodate subpopulations or outlying functions (p. 559).

DP option: $\theta_i\sim P$, $P\sim\mathrm{DP}(\alpha P_0)$ gives functional clustering, $f_i(t)=f^*_{S_i}(t)$, $f^*_c(t)=b(t)\theta^*_c$, $\Pr(S_i=c)=\pi_c$, $\theta_c^*\sim P_0$. A suitable $P_0$ allows cluster-specific basis selection (p. 559). Two good choices:

- **Variable-selection base.** $P_0=\bigotimes_{h=1}^HP_{0h}$ with $P_{0h}(\cdot)=\pi_{0h}\delta_0(\cdot)+(1-\pi_{0h})N(\cdot\mid0,\psi_h^{-1})$, possibly $\psi_h\sim\mathrm{Gamma}(\frac\nu2,\frac\nu2)$ for a heavy-tailed $t$ prior and $\pi_{0h}\sim\mathrm{Beta}(a,b)$. A subset of each $\theta_c^*$ is exactly zero, varying across clusters. The Gibbs sampler is a minor modification of the earlier ones, with each $\theta^*_{ch}$ drawn from a point-mass-plus-normal mixture. The one-at-a-time updates are computationally heavy and mix slowly (p. 560).
- **Heavy-tailed shrinkage base.** $\theta_{ch}^*\sim N(0,\psi_{ch}^{-1})$, $\psi_{ch}\sim\mathrm{Gamma}(\frac\nu2,\frac\nu2)$ with small $\nu$; $\nu=1$ gives a Cauchy marginal prior. Whole vectors $\theta_c^*$ can then be updated in one block from multivariate normal full conditionals, which speeds mixing substantially. No coefficient is exactly zero, but small ones effectively exclude their basis functions, and "in practice it is impossible to distinguish" small nonzero from zero coefficients (p. 560).

### 23.5 Hierarchical dependence (pp. 560–568)
Independent DPs for several unknown distributions (as in the toxicology analysis) have clear limits, so priors favouring dependence are appealing (p. 560).

**Example: genotoxicity (comet assay), motivation (pp. 560–562).** $y_i$ = DNA damage in cell $i$; $x_i\in\{1,\dots,T\}$ = dose group (hydrogen peroxide). In Figure 23.4, lower quantiles of the response density barely change with dose while higher quantiles increase dramatically. The author describes this as a natural consequence of variability among experimental units in sensitivity, and says differential quantile changes are common in other applications (p. 561). The standard parametric model (23.15), $y_i\sim N(\mu+\sum_{j=2}^T1_{x_i=j}\beta_j,\sigma^2)$, "falls short" by assuming normality within groups and only mean shifts (p. 562).

**Dependent Dirichlet processes (DDP) (p. 562).** Separate DPMs per group, $f_j(y)=\int N(y\mid\mu,\phi^{-1})dP_j(\mu,\phi)$, $P_j\sim\mathrm{DP}(\alpha_jP_{0j})$, raise the question of how to borrow information. A DDP prior for $\{P_1,\dots,P_T\}$ is defined by the property that each marginal is a DP: $P_j\sim\mathrm{DP}(\alpha_jP_{0j})$. Stick-breaking form: $P_j=\sum_h\pi_{jh}\delta_{\theta^*_{jh}}$, $\pi\sim Q$, $\theta_h^*\sim P_0$, with $Q,P_0$ chosen so that marginally $\pi_j\sim\mathrm{stick}(\alpha_j)$ and $\theta_{jh}^*\overset{iid}{\sim}P_{0j}$. Defining a suitable $Q$ is complicated, so most literature uses **fixed-$\pi$ DDPs**: $P_j=\sum_h\pi_h\delta_{\theta^*_{jh}}$, $\pi\sim\mathrm{stick}(\alpha)$, $\theta_h^*\sim P_0$. Weights are shared and only atoms vary across groups, with dependence controlled by $P_0$ (p. 562).

Comet assay model: $f_j(y)=\sum_h\pi_hN(y\mid\mu^*_{jh},\phi_h^{-1})$, $\pi\sim\mathrm{stick}(\alpha)$, $\phi_h\sim\mathrm{Gamma}(a,b)$. Draw $\mu^*_{1h}$ from a Gaussian and then set
$$\mu^*_{j+1,h}-\mu^*_{jh}=\beta_{jh}\sim\pi_0\delta_0+(1-\pi_0)N(0,c).\tag{23.16}$$
The shift between adjacent dose groups is zero with probability $\pi_0$. Replacing the normal by a normal truncated below at zero enforces a non-decreasing stochastic order. Larger $\pi_0$ favours identical kernels and effective pooling, which improves efficiency and is of interest for testing near-equalities. A heavy-tailed mixture prior for $\beta_{jh}$ is an alternative (p. 563).

Blocked Gibbs (with $y_i\sim N(\mu_i,\phi_i^{-1})$) (p. 563): (1) $\Pr(S_i=h\mid-)=\pi_hN(y_i\mid\mu^*_{x_ih},\phi_h^{*-1})/\sum_{l=1}^N\pi_lN(y_i\mid\mu^*_{x_il},\phi_l^{*-1})$, with $S_i=h$ meaning $\mu_i=\mu^*_{x_ih}$, $\phi_i=\phi_h^*$; (2) update stick-breaking weights from beta full conditionals as before; (3) update $\phi_h^*$ from gamma full conditionals; (4) update $\mu^*_{1h}$ from its Gaussian conditional and $\beta_{jh}$ from its point-mass-plus-Gaussian conditional. The author leaves the conditionals in 3–4 as an algebraic exercise.

**Example: genotoxicity (continued) (pp. 563–564).** Cells exposed to 0, 5, 20, 50 or 100 µmol $\mathrm{H_2O_2}$, with repair time 0, 60 or 90 min. This gives $K=15$ groups, and $n=1400$ cells: 100 per group except groups 9 and 13, which had 50. The response is the Olive tail moment. Damage should rise with dose at zero repair and fall stochastically with repair time (a graph of order restrictions, Fig. 23.5). The model is a restricted DDP: each group's density is a DP location mixture of Gaussians, parameterised via adjacent-group differences with the prior of (23.16) restricted to obey the ordering. Let $d_k$ be the total weight on clusters that differ between the two groups linked by edge $k$; a small $d_k$ means similar densities. Results reported (p. 564):

- Strong evidence of damage increases among the 0, 5 and 20 µmol groups at 0 min; evidence for further increases at higher doses is less clear.
- No evidence of change among groups 1, 6 and 11 (no damage to repair there).
- Clear decreases in each exposed group after 60 min; an extra 30 min did not significantly alter the distribution.

The author reports that simulation studies suggest low type I error and high power even in small samples. The approach "borrows strength adaptively": groups supported as similar are effectively pooled, which "dramatically reduces mean square error" (p. 564).

**Hierarchical Dirichlet processes (HDP) (pp. 564–566).** $P_j\sim\mathrm{DP}(\alpha P_0)$, $P_0\sim\mathrm{DP}(\beta P_{00})$, written $P\sim\mathrm{HDP}(\alpha,\beta,P_{00})$. Because DP draws are discrete, $P_j=\sum_h\pi_{jh}\delta_{\theta_h^*}$ and $P_0=\sum_h\lambda_h\delta_{\theta_h^*}$ with $\theta_h^*\sim P_{00}$. So all groups share identical atoms and differ in weights, the opposite of the fixed-$\pi$ DDP (p. 565). With $f_j(y)=\int N(y\mid\mu,\phi^{-1})dP_j$, there is a global dictionary of normal kernels $N(\mu_h^*,\phi_h^{*-1})$, a central density $f_0$ with weights $\lambda$, and group densities with weights $\pi_j$ drawn from a stick-breaking process centred on $\lambda$. The hyperparameter $\alpha$ controls variability of weights across groups. As $\alpha\to0$, group densities are single Gaussians, with clusters of groups sharing mean and precision. As $\alpha\to\infty$, $f_j\equiv f_0$ (pooling) (pp. 565–566).

Hospital example: $y_{ij}$ is quality of care for hospital $j$ in state $i$, with an HDP location-mixture prior on state densities. This induces $y_{ij}\sim N(\mu^*_{S_{ij}},\phi^{*-1}_{S_{ij}})$, $\Pr(S_{ij}=h)=\pi_{jh}$ (as printed), $(\mu_h^*,\phi_h^{*-1})\sim P_{00}$. Hospitals within a state are more likely to share a cluster, but clusters can also be shared across states (soft probabilistic clustering). Since $\alpha$ controls within-group dependence in clustering and $\beta$ the total number of clusters, both should get hyperpriors, e.g. $\alpha\sim\mathrm{Gamma}(1,1)$ independently of $\beta\sim\mathrm{Gamma}(1,1)$ (p. 566).

**Nested Dirichlet processes (NDP) (pp. 566–567).** The goal is to cluster *groups* with identical distributions (e.g. dose groups or states), which gives posterior probabilities for equalities between groups. The NDP is
$$P_j\sim P,\quad P\sim\mathrm{DP}(\alpha P_0),\quad P_0\equiv\mathrm{DP}(\beta P_{00}).\tag{23.17}$$
The base is a DP itself, not a realisation of a DP as in the HDP. Stick-breaking form:
$$P_j\sim P=\sum_h\pi_h\delta_{P_h^*},\quad\pi\sim\mathrm{stick}(\alpha),\quad P_h^*\sim\mathrm{DP}(\beta P_{00}).\tag{23.18}$$
The atoms are whole random measures drawn iid from a DP. By the Pólya urn, $\Pr(P_j=P_{j'})=\frac1{1+\alpha}$. Groups in different clusters have distinct atoms drawn independently from $P_{00}$. In the HDP, by contrast, $\Pr(P_j=P_{j'})=0$ (p. 567). For NDP mixtures $f_j(y)=\int N(y\mid\mu,\phi^{-1})dP_j$, $\Pr(f_j=f_{j'})=\frac1{1+\alpha}$. A hyperprior $\alpha\sim\mathrm{Gamma}(a,b)$ can be elicited to give desired values for $\Pr(H_{0jj'})$ and $\Pr(H_0)$. The data tend to inform more strongly as $T$ increases, a "blessing of dimensionality". Putting a DP on $P_{00}$ combines NDP and HDP (shared global atoms with varying weights); the author says this was implemented successfully in machine learning (p. 567).

**Convex mixtures (pp. 567–568).** HDP and NDP are DDPs (DP marginals), but one can also use priors without DP marginals. Setting: longitudinal studies at centres $c$, $y_{cij}\sim N(x_{cij}\beta_{ci}+\epsilon_{cij},\sigma^2)$. Parametric multilevel: $\beta_{ci}=\alpha_c+\psi_{ci}$ with Gaussian terms (p. 567). Semiparametric: $\beta_{ci}\sim P_c$, $\{P_c\}\sim\Pi$, with
$$P_c=\pi G_0+(1-\pi)G_c,\quad G_c\sim\mathrm{DP}(\alpha G_0),\quad\pi\sim\mathrm{Beta}(a,b).\tag{23.19}$$
A higher weight $\pi$ on the global $G_0$ makes groups more similar. Unlike the HDP, there are separate global and group-specific atoms. Subjects on global atoms can cluster across centres, and those on centre-specific atoms only within their centre. Computation: introduce a binary indicator $z_{ci}=1$ for allocation to the global component. After imputing the indicators, DP algorithms apply directly. $P_c$ is marginally not a DP, so $\Pi$ is not a DDP. Convex combinations are used because the result is guaranteed to be a probability measure (p. 568).

For ordered dose groups, a first-order autoregressive model favours dependence of $P_t$ and $P_{t+1}$ over $P_t$ and $P_{t+2}$:
$$P_t=(1-\pi)P_{t-1}+\pi G_t,\quad P_0=G_0,\quad G_t\sim\mathrm{DP}(\alpha P_0).\tag{23.20}$$
This is a random walk in the space of measures, with $\pi$ controlling dependence (possibly depending on $t$). In time series, a disadvantage is that atoms can only be added and never disappear, though early ones get decreasing weight. Drawing $P_0$ from an HDP reuses the same atoms; the author says this was successful for music data (p. 568).

**Intuition note.** DDP: same clusters' weights, shifted locations. HDP: same atoms, different weights. NDP: groups are either identical (same cluster of distributions) or entirely different. Convex mixtures blend a shared and a private distribution. Each answers "how much should groups look alike?" differently.

### 23.6 Density regression (pp. 568–571)
Now there is an uncountable collection $P_{\mathcal X}=\{P_x,x\in\mathcal X\}$, $\mathcal X\subset\mathbb R^p$, indexed by predictors, so the whole conditional density $p(y\mid x)$ can change flexibly (p. 568). A widely used approach, the hierarchical mixture-of-experts, is
$$p(y\mid x)=\sum_{h=1}^H\pi_h(x)N(y\mid x\beta_h,\tau_h^{-1}),\tag{23.21}$$
a mixture of normal linear regressions with predictor-varying weights (for finite $H$, a probabilistic tree or a logistic regression can give $\pi_h(x)$) (p. 569).

**Dependent stick-breaking processes (pp. 569–570).** Nonparametric version: $p(y\mid x)=\int N(y\mid x\beta,\tau^{-1})dP_x(\beta,\tau)$, $P_{\mathcal X}\sim\Pi_{\mathcal X}$, ideally centred on a reasonable parametric model. Predictor-dependent stick-breaking: $P_x=\sum_h\pi_h(x)\delta_{\theta_h^*(x)}$, $\pi_h(x)=V_h(x)\prod_{l<h}(1-V_l(x))$. For simplicity take global atoms $\theta^*_h=(\beta_h^*,\tau_h^*)$, giving infinitely many experts with a prior under which $\pi_h(x)$ decreases rapidly in $h$. If $V_h\sim Q$ iid with $V_h(x)\sim\mathrm{Beta}(1,\alpha)$ marginally for all $x$, the result is a DDP mixture of linear regressions (order-based DDP, local DP are examples). The author notes advantages in not restricting to DDPs.

*Kernel stick-breaking process* (p. 569):
$$V_h(x)=K_{\psi_h}(x,\Gamma_h)V_h,\quad\psi_h\sim H,\ \Gamma_h\sim G,\ V_h\sim\mathrm{Beta}(1,\alpha),$$
with $K_\psi(\cdot,\Gamma)$ a kernel bounded by one, equal to 1 at $x=\Gamma_h$, where $V_h(x)=V_h$. The author says this prior performs well and has been shown to give large support and posterior consistency for conditional densities. Weights $\pi_h(x)$ tend to be larger when $x$ is near $\Gamma_h$, especially for small $h$; bandwidths control spatial variability. When kernels become flat ($K\approx1$ everywhere), the DP stick-breaking process is a limiting case (p. 570).

*Probit stick-breaking process (PSBP)* (p. 570):
$$\pi_h(x)=V_h(x)\prod_{l<h}(1-V_l(x)),\quad V_h(x)=\Phi(\alpha_h+\mu_h(x)),\quad\alpha_h\sim N(\mu,1),$$
with $\Phi$ the standard normal cdf and $\mu_h:\mathcal X\to\mathbb R$ an arbitrary regression model. Without predictors, $V_h=\Phi(\alpha_h)$. For $\mu=0$, $V_h\sim\mathrm{Beta}(1,1)$, so the PSBP with $\mu=0$ equals a DP with precision 1. The hyperparameter $\mu$ plays the role of $\alpha$: for large $\mu$, $V_h\approx1$ and the first component gets large weight, as with $\alpha\approx0$. A logistic transform gives a logistic stick-breaking process. Posterior computation for the kernel version tends to be straightforward and efficient, but the PSBP has some computational advantages (p. 570).

**Example: glucose tolerance (pp. 570–571).** $n=868$ patients. $y$ = 2-hour plasma glucose (GT; <140 normal, [140,200] prediabetes, >200 diabetes); predictors: log insulin sensitivity ($x_1$, IS), age, waist-to-hip ratio, BMI, diastolic and systolic blood pressure. Figure 23.7: right-skewed glucose with a shape that changes with IS. Because linear or nonlinear mean or median regression is "not supported", a Bayesian density regression allows predictors to drop out and to act locally. Marginal posterior probabilities for the six predictors: 1.0, 1.0, 0.03, 0.02, 0.03, 0.03, so IS and age matter and the rest can be discarded. Figure 23.8 shows the glucose density has a heavy right tail for low IS that disappears as IS increases. The tail gets heavier with age, especially for low IS (p. 571).

### 23.7–23.8 Bibliographic note and exercises (pp. 571–573)
The note cites overviews, asymptotics, computation, applications and many alternative priors (Pólya trees; normalised random measures); it attributes the Bayesian bootstrap to Rubin (1981b) and the DDP to MacEachern (1999), and lists kernel, probit and logistic stick-breaking and convex-combination priors (pp. 571–573). Exercises: simulate from a three-component normal mixture, compare a non-Bayesian density estimate, the finite Dirichlet approximation ($k=20$) and the blocked sampler ($N=20$); then study the effect of larger $\alpha$, a gamma hyperprior, and a much larger variance of $P_0$ (p. 573).

## Toy example (ours, not from the text)
**Posterior mean of a DP (23.2).** Let $\alpha=2$ and $P_0=N(0,1)$. Observe $y=(1.0,\ 1.0,\ 2.0)$, so $n=3$ and $\alpha+n=5$.
- $B=(-\infty,0]$: $P_0(B)=0.5$, no data in $B$. $E(P(B)\mid y)=\frac25(0.5)+\frac35(0)=0.2+0=0.2$.
- $B=\{1\}$: $P_0(B)=0$, and 2 of 3 points equal 1, so $\frac35\cdot\frac23=0.4$.
The data point at 1.0 gets mass 0.4, which is much more than any single prior bin.

**Chinese-restaurant probabilities (23.6).** Let $\alpha=1$. Customer 2 joins customer 1's table with probability $\frac1{1+\alpha}=\frac12$. Given both are at one table, customer 3 joins it with probability $\frac2{\alpha+2}=\frac23$ and opens a new table with $\frac\alpha{\alpha+2}=\frac13$. Probability of the partition $\{1,2\},\{3\}$: $\frac12\times\frac13=\frac16$.

**Stick-breaking (23.3).** Suppose $V_1=0.4$, $V_2=0.5$, $V_3=0.3$. Then $\pi_1=0.4$; $\pi_2=0.5\times0.6=0.3$; $\pi_3=0.3\times(0.6)(0.5)=0.09$. The leftover stick is $0.6\times0.5\times0.7=0.21$, and $0.4+0.3+0.09+0.21=1$, as the construction requires.

## Concepts
- [[dirichlet-process]] (new) — random probability measure $P\sim\mathrm{DP}(\alpha P_0)$ whose bin probabilities on every finite partition are Dirichlet$(\alpha P_0(B_h))$ (p. 547)
- [[stick-breaking-construction]] (new) — $P=\sum\pi_h\delta_{\theta_h}$ with $\pi_h=V_h\prod_{l<h}(1-V_l)$, $V_h\sim\mathrm{Beta}(1,\alpha)$ (p. 548)
- [[polya-urn-crp]] (new) — predictive rule after marginalising $P$; Chinese restaurant metaphor (p. 550)
- [[dirichlet-process-mixture]] (new) — kernel mixture whose mixing measure has a DP prior; infinite mixture with data-driven occupied clusters (p. 549–550)
- [[bayesian-bootstrap]] (new) — limit $\alpha\to0$ of the DP posterior, $\mathrm{DP}(\sum\delta_{y_i})$ (p. 548)
- [[blocked-gibbs-sampler]] (new) — truncated stick-breaking Gibbs sampler with $V_N=1$ (p. 552)
- [[dependent-dirichlet-process]] (new) — collection of RPMs each marginally a DP; fixed-$\pi$ version shares weights (p. 562)
- [[hierarchical-dirichlet-process]] (new) — $P_j\sim\mathrm{DP}(\alpha P_0)$, $P_0\sim\mathrm{DP}(\beta P_{00})$; shared atoms, varying weights (p. 565)
- [[nested-dirichlet-process]] (new) — DP whose atoms are DP random measures; clusters whole distributions (p. 566)
- [[kernel-probit-stick-breaking]] (new) — predictor-dependent stick-breaking for density regression (pp. 569–570)
- [[conjugate-prior]] — Dirichlet/DP conjugacy gives posterior $\mathrm{DP}(\alpha P_0+\sum\delta_{y_i})$ (p. 547)
- [[gibbs-sampling]] — used for allocations, weights and cluster parameters (p. 551)
- [[marginal-likelihood]] — controls new-cluster probability and acts as complexity penalty (pp. 551, 553)
- [[bayesian-occams-razor]] — author's explanation of why no overfitting in clustering via $\alpha$ (pp. 553–554)
- [[exchangeability]] — used to derive the full conditional prior (23.7) (p. 550)
- [[hierarchical-multilevel-model]] — DP/DPM priors on group-varying parameters (p. 558)

## Canonical instances
- [[bayes-histogram-beta-mixture]] — simulated $n=100$ from 0.75 Beta(1,5)+0.25 Beta(20,2), 10 knots (p. 546)
- [[mouse-implantation-toxicology]] — counts per dose group; DP vs DPM of Poissons vs rounded Gaussians (pp. 554–557)
- [[comet-assay-genotoxicity]] — DNA damage densities; restricted DDP over 15 dose × repair groups (pp. 560–565)
- [[hospital-quality-hdp]] — hospitals in states, hierarchical clustering (p. 566)
- [[glucose-tolerance-density-regression]] — PSBP density regression, $n=868$ (pp. 570–572)

## Bridges (candidates)
- [same-math] DP posterior $\mathrm{DP}(\alpha P_0+\sum\delta_{y_i})$ on a finite partition ↔ Bayesian: Dirichlet–multinomial conjugate updating — bin pseudo-counts $\alpha P_0(B)$ plus observed counts.
- [structural-analogy] Posterior mean (23.2), weight $\alpha/(\alpha+n)$ on $P_0$ ↔ partial pooling/shrinkage: estimate pulled to a prior guess with strength decreasing in $n$.
- [structural-analogy] Marginal-likelihood penalty on extra clusters ↔ Bayesian Occam's razor: more parameters spread mass thinner.
- [structural-analogy] HDP shared atoms with varying weights ↔ hierarchical models: groups borrow strength from a common parent.
- [metaphor] Random walk in the space of measures (23.20) ↔ Gaussian random walk: dependence between neighbouring groups.

## Questions this raises
- How do the posterior of the number of clusters and $\alpha$ behave when the true density is not a finite mixture?
- How should a base measure $P_0$ be chosen when the data cannot be standardised sensibly (e.g. for several scales)?
- How does a restricted DDP compare with a classical test for ordered group differences in practice?
- When is a DP-based dependent prior preferable to non-DDP priors such as kernel or probit stick-breaking?

## Exercises worth doing
- Ex. 1 (p. 573) — fit the finite-Dirichlet and truncated stick-breaking DPM to simulated mixture data and compare with `density()`; builds familiarity with the samplers — difficulty: medium
- Ex. 2 (p. 573) — repeat with larger $\alpha$, a gamma hyperprior on $\alpha$, and much higher variance of $P_0$; shows how $\alpha$ and $P_0$ drive clustering — difficulty: medium

## Reading notes
- Page offset: printed = pdf − 10. Printed p. 574 (pdf 584) is blank except for the standard non-commercial-use banner.
- The text layer garbles Greek symbols (θ appears as ω, ∼ as →, ℜ as ∈, "→" for minus in subscripts). I used the page images: the atoms are $\theta$ throughout.
- Page 550: the printed CRP probability reads $c_j/(n-i+\alpha)$ and $\alpha/(n-i+\alpha)$. The denominator $\alpha+i-1$ follows from (23.6) (the image shows $n-i+\alpha$, apparently a misprint). I used (23.6).
- Page 556, rounded-Gaussian step 4: the first term in $\hat b_{\tau_c}$ appears printed without a square, and $n_h$ appears where $n_c$ is meant. I wrote the squared version with $n_c$ as the evident intent, since the formula is a sum of squared deviations.
- Page 553: the printed estimator reads $\sum_{c=1}^N\pi_hK(y\mid\theta_c^*)$ (index $h$ for $c$). Page 555 (Poisson step 1) similarly mixes $h$ and $c$. Page 566: $\Pr(S_{ij}=h)=\pi_{jh}$ as printed (the index $i$ for state does not appear on $\pi$).
- Page 563: the continuation says "described in the previous chapter" for blocked Gibbs steps, though they appear in the earlier sections of this chapter. Page 563 also refers to "page 560" for the genotoxicity example.
- Figure 23.5 caption mentions $H_{1k}$ and the text mentions $H_{0k}$; edge probabilities are in the figure and not all reproduced here.
- Exercise 1(c), as printed: "$a=\frac\alpha k$, $\alpha=1$, ... $\kappa=\alpha_\tau=b_\tau=\alpha=1$" (α is listed twice).
- Chapter heading on p. 545 gives only the introductory sentence; no solutions are printed for the exercises.
