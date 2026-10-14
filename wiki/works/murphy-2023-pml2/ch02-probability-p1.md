---
id: murphy-2023-pml2/ch02-probability-p1
work: murphy-2023-pml2
unit: "1 Introduction; 2 Probability (part 1/3): 2.1 Introduction, 2.2 Some common probability distributions (up to 2.2.5.7)"
pages: 1-21
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
# Introduction; Probability basics and common distributions

## L0 — One line
The book adopts model-based learning of the data-generating process, with Bayesian inference as one way to formalise it, and Chapter 2 starts from the probability axioms and Bayes' rule and then catalogues the distributions used as building blocks.

## L1 — The gist (≤ 120 words)
Chapter 1 asks what many feel current "function-fitting" machine learning lacks. Its answer is a model-based approach: learn parsimonious models of the data-generating process (the process that produces the data); one way to formalise this is Bayesian inference on probabilistic models. This aims at robust and efficient systems. Chapter 2 gives the background. It defines probability spaces, random variables, the Kolmogorov axioms, conditional probability and Bayes' rule. It then lists common distributions: discrete, on the real line, on positive reals, on [0,1], and multivariate. For most it gives the density, parameters, and some moments and relations, such as special cases and heavy tails. These distributions are used in various kinds of models.

**Prerequisites:** sets and basic integrals; sums and products; matrices, trace and determinant (only for 2.2.5.4–2.2.5.6); the gamma function.

## L2 — Key ideas (5–10 bullets)
- The chapter opens with Tenenbaum's quote that intelligence is about modeling the world, not just pattern recognition. The book adopts a model-based approach, with Bayesian inference on probabilistic models as one way to formalise it, aimed at robustness and data efficiency (pp. 1–2).
- A probability space $(\Omega,\mathcal F,\mathbb P)$ plus random variables gives probability mass functions (pmfs) for discrete variables and densities (pdfs) and cumulative distribution functions (cdfs) for continuous ones; an uncountable $\Omega$ needs a Borel σ-field, a family of events built from intervals (pp. 5–6).
- Three Kolmogorov axioms generate the complement and addition rules. Cox's theorem is cited as their deeper justification (p. 7).
- Independence is defined by a product rule; the law of total probability and Bayes' rule are derived from the definition of conditional probability. Bayes' rule names prior, likelihood, posterior and marginal likelihood (pp. 7–8).
- Discrete families (binomial, categorical, multinomial, Poisson, negative binomial) are related. The Poisson is a limit of the negative binomial, which allows variance different from the mean (pp. 9–10).
- The Gaussian is sensitive to outliers; the Student, Cauchy and Laplace are described as heavy-tailed. Kurtosis (a fourth-moment measure of tail weight) separates super-Gaussian (e.g. Laplace) from sub-Gaussian distributions (pp. 10–13).
- Gamma-family distributions (exponential, chi-squared, inverse gamma) and the Pareto power law cover positive quantities. Beta covers [0,1] (pp. 14–17).
- Multivariate distributions (Student, von Mises–Fisher, matrix normal, Wishart, inverse Wishart, Dirichlet) are also covered; several generalise earlier ones (Student, gamma, inverse gamma, beta). The Dirichlet scale $\alpha_0$ controls peakedness, and the Dirichlet is useful for distinguishing aleatoric (data) from epistemic uncertainty (pp. 17–21).

## L3 — Walkthrough

### 1 Introduction (pp. 1–2)
- **Motivation.** Much of current ML approximates functions $f:\mathcal X\to\mathcal Y$, often by deep learning. Pearl called this "glorified curve fitting"; the author says this is a little unfair in high dimensions, but, as many feel, it points at what is lacking: too much focus on predicting observable patterns, too little on the latent structure behind them (p. 1).
- **Why "deep understanding".** It is needed for science and for applications such as healthcare, and for robust and efficient systems. *Robust* = works under unexpected shifts of the data distribution. *Efficient* = data-efficient (learns from little data); computational efficiency is secondary (p. 1).
- **Approach.** Learn parsimonious representations of the data-generating process (DGP). This resembles the scientific method. One way to formalise it is Bayesian inference on probabilistic models, citing [Jay03; Box80; GS13] (p. 1).
- **Footnote 1.** In deep learning, "inference" means applying a function to inputs. In Bayesian inference it means inverting a function, from observed outputs back to possible hidden causes. This is closer to what deep learning calls "training" (pp. 1–2).
- **Book layout.**
  - Part I: background, which can be skipped by readers who know it.
  - Part II: inference algorithms.
  - Part III: prediction models $p(y|x)$, assuming one right answer.
  - Part IV: generation models $p(x)$ or $p(x|c)$, where several outputs may be valid.
  - Part V: latent variable models $p(z,x)=p(z)p(x|z)$, whose goal is $p(z|x)$.
  - Part VI: decisions under uncertainty, then causality (p. 2).

### 2.1 Introduction (pp. 5–8)
**2.1.1 Probability space (p. 5).** A triple $(\Omega,\mathcal F,\mathbb P)$. $\Omega$ is the sample space (possible outcomes). $\mathcal F$ is the event space (the set of events; for countable $\Omega$, all subsets). $\mathbb P:\mathcal F\to[0,1]$ is the probability measure, subject to the consistency requirements of 2.1.4.

**2.1.2 Discrete random variables (pp. 5–6).**
- Example, 3-sided die: $\Omega=\{A,B,C\}$, with $\mathbb P[\{A\}]=2/6$, $\mathbb P[\{B\}]=1/6$, $\mathbb P[\{C\}]=3/6$. Then $\mathbb P[\{A,B\}]=2/6+1/6=1/2$ (p. 5).
- A random variable (rv) is a function $X:\Omega\to\mathbb R$. For the die, $X(A)=1,X(B)=2,X(C)=3$ (p. 5).
- Two fair coin flips: $X$ = number of heads, so $X(HH)=2$, $X(HT)=X(TH)=1$, $X(TT)=0$ (p. 5).
- State space $\mathcal X=X(\Omega)$. The pmf is
$$p_X(a)=\mathbb P[X=a]=\mathbb P[X^{-1}(a)],\tag{2.1}$$
where $X^{-1}(a)=\{\omega\in\Omega\mid X(\omega)=a\}$ is the pre-image. For the two-coin example: $p_X(0)=1/4$, $p_X(1)=2/4$, $p_X(2)=1/4$ (p. 6).

**2.1.3 Continuous random variables (p. 6).**
- Take $\Omega\subseteq\mathbb R$ and $X(\omega)=\omega$. The example is a duration with $\Omega=\{t:0\le t\le T_{\max}\}$.
- An uncountable $\Omega$ cannot have its subsets enumerated, so one uses a σ-field $\mathcal F$: (1) $\emptyset,\Omega\in\mathcal F$; (2) closed under complement; (3) closed under countable unions and intersections. The Borel σ-field $\mathcal B$ is the σ-field generated by intervals $(-\infty,b]$. It contains the sets
$$(a,b),[a,b],(a,b],[a,b),\{b\},\ -\infty\le a\le b\le\infty.\tag{2.2}$$
- The measure is defined through a pdf $p_X(x)\ge0$:
$$\mathbb P([a,b])=\int_E d\mathbb P=\int_a^b p(x)\,dx\tag{2.3}$$
- The cdf is
$$P_X(x)\triangleq\mathbb P[X\le x]=\int_{-\infty}^x p_X(x')dx'\tag{2.4}$$
$$\mathbb P([a,b])=p(a\le X\le b)=P_X(b)-P_X(a)\tag{2.5}$$
- "Probability distribution" may mean the pdf, the cdf or the measure. The definitions extend to $\Omega\subseteq\mathbb R^n$ and to richer spaces such as functions (p. 7).

**2.1.4 Probability axioms (p. 7).** The Kolmogorov axioms:
- Non-negativity: $\mathbb P[E]\ge0$.
- Normalization: $\mathbb P[\Omega]=1$.
- Additivity: for pairwise disjoint $E_i$,
$$\mathbb P[\cup_{i=1}^\infty E_i]=\sum_{i=1}^\infty\mathbb P[E_i]\tag{2.6}$$
- Finite case: $\mathbb P[E_1\cup E_2]=\mathbb P[E_1]+\mathbb P[E_2]$ (2.7) for disjoint sets.
- Complement rule: $\mathbb P[E^c]=1-\mathbb P[E]$ (2.8). Proof: $1=\mathbb P[\Omega]=\mathbb P[E\cup E^c]=\mathbb P[E]+\mathbb P[E^c]$.
- Also $\mathbb P[E]\le1$ (by contradiction) and $\mathbb P[\emptyset]=0$ (the complement rule with $E=\Omega$).
- Addition rule, valid for any pair of events, disjoint or not:
$$\mathbb P[E_1\cup E_2]=\mathbb P[E_1]+\mathbb P[E_2]-\mathbb P[E_1\cap E_2]\tag{2.9}$$
- Footnote 1: these laws can be shown to follow from more basic assumptions about reasoning under uncertainty, a result known as Cox's theorem.

*Intuition note.* Probability is a non-negative weight on events that sums to 1 over everything and adds over non-overlapping events. The complement and addition rules follow from these three.

**2.1.5 Conditional probability (pp. 7–8).**
- If $\mathbb P[E_2]\ne0$:
$$\mathbb P[E_1|E_2]\triangleq\frac{\mathbb P[E_1\cap E_2]}{\mathbb P[E_2]}\tag{2.10}$$
- Multiplication rule: $\mathbb P[E_1\cap E_2]=\mathbb P[E_1|E_2]\mathbb P[E_2]=\mathbb P[E_2|E_1]\mathbb P[E_1]$ (2.11).
- Independence: $\mathbb P[E_1\cap E_2]=\mathbb P[E_1]\mathbb P[E_2]$ (2.12). If both probabilities are $>0$, this is equivalent to $\mathbb P[E_1|E_2]=\mathbb P[E_1]$, or equivalently $\mathbb P[E_2|E_1]=\mathbb P[E_2]$.
- Conditional independence given $E_3$: $\mathbb P[E_1\cap E_2|E_3]=\mathbb P[E_1|E_3]\mathbb P[E_2|E_3]$ (2.13).
- Law of total probability: if $\{A_1,\dots,A_n\}$ partitions $\Omega$, then for any event $B\subseteq\Omega$
$$\mathbb P[B]=\sum_{i=1}^n\mathbb P[B|A_i]\mathbb P[A_i]\tag{2.14}$$

**2.1.6 Bayes' rule (p. 8).** For $\mathbb P[E_1]>0$ and $\mathbb P[E_2]>0$:
$$\mathbb P[E_1|E_2]=\frac{\mathbb P[E_2|E_1]\mathbb P[E_1]}{\mathbb P[E_2]}\tag{2.15}$$
For discrete $X$ with $K$ states, using total probability:
$$p(X=k|E)=\frac{p(E|X=k)p(X=k)}{p(E)}=\frac{p(E|X=k)p(X=k)}{\sum_{k'=1}^K p(E|X=k')p(X=k')}\tag{2.16}$$
- $p(X=k)$ is the prior, $p(E|X=k)$ the likelihood, $p(X=k|E)$ the posterior, and $p(E)$ a normalization constant called the marginal likelihood.
- Continuous case: the same with $p(E)=\int p(E|X=x')p(X=x')dx'$ (2.17).

*Intuition note.* Bayes' rule just rewrites the multiplication rule (2.11) so that the cause-given-evidence probability is computed from the evidence-given-cause probability. The denominator makes the posteriors add to 1.

### 2.2 Some common probability distributions (pp. 8–21)
The author summarises commonly used distributions; Supplementary Chapter 2 has more (p. 8).

**2.2.1 Discrete distributions (pp. 9–10).**
- Binomial, $x\in\{0,\dots,N\}$:
$$\mathrm{Bin}(x|N,\mu)\triangleq\binom Nx\mu^x(1-\mu)^{N-x}\tag{2.18}$$
with $\binom Nk=\frac{N!}{(N-k)!k!}$. For $N=1$ it reduces to Bernoulli: $\mathrm{Ber}(x|\mu)=1-\mu$ if $x=0$, $\mu$ if $x=1$ (2.19), with $\mu=\mathbb E[x]=p(x=1)$ (p. 9).
- Categorical, $x\in\{1..K\}$: $\mathrm{Cat}(x|\boldsymbol\theta)\triangleq\prod_k\theta_k^{\mathbb I(x=k)}$ (2.20). With one-hot $\boldsymbol x$: $\prod_k\theta_k^{x_k}$ (2.21). If $x_k$ counts value $k$ in $N=\sum_k x_k$ trials we get the multinomial
$$\mathcal M(\boldsymbol x|N,\boldsymbol\theta)\triangleq\binom N{x_1\dots x_K}\prod_{k=1}^K\theta_k^{x_k}\tag{2.22}$$
$$\binom N{k_1\dots k_m}\triangleq\frac{N!}{k_1!\cdots k_m!}\tag{2.23}$$
- Poisson, $\lambda>0$: $\mathrm{Poi}(x|\lambda)=e^{-\lambda}\lambda^x/x!$ (2.24). $\lambda$ is both mean and variance (p. 10).
- Negative binomial (p. 10). Urn with $N$ balls, $R$ red, $B$ blue.
  - Sampling with replacement $n$ times: the number of blue balls is $\mathrm{Bin}(n,p)$ with $p=B/N$.
  - Instead, keep drawing until $r$ failures (red). Then the number of successes (blue) $X\sim\mathrm{NegBinom}(r,p)$:
$$\mathrm{NegBinom}(x|r,p)\triangleq\binom{x+r-1}x(1-p)^rp^x\tag{2.25}$$
  - For real $r$, replace the coefficient by $\frac{\Gamma(x+r)}{x!\Gamma(r)}$.
  - Moments: $\mathbb E[x]=\frac{pr}{1-p}$, $\mathbb V[x]=\frac{pr}{(1-p)^2}$ (2.26).
  - Two parameters let mean and variance be set separately, so it is useful for "contagious" (positively correlated) events, whose variance is larger than if the occurrences were independent.
  - $\mathrm{Poi}(\lambda)=\lim_{r\to\infty}\mathrm{NegBinom}(r,\frac\lambda{1+\lambda})$. The case $r=1$ is the geometric distribution.

**2.2.2 Continuous distributions on $\mathbb R$ (pp. 10–13).**
- Gaussian: $\mathcal N(x|\mu,\sigma^2)\triangleq\frac1{\sqrt{2\pi\sigma^2}}e^{-\frac1{2\sigma^2}(x-\mu)^2}$ (2.27). $\mu$ is mean and mode; $\sigma^2$ is variance; precision is $\lambda=1/\sigma^2$. Its cdf is $\Phi(x;\mu,\sigma^2)=\int_{-\infty}^x\mathcal N(z|\mu,\sigma^2)dz$ (2.28); $\Phi(x)$ for the standard normal (p. 11).
- Half-normal: $Y=|X|$ with $X\sim\mathcal N(0,\sigma^2)$ has pdf $\mathcal N_+(y|\sigma)\triangleq2\mathcal N(y|0,\sigma^2)=\frac{\sqrt2}{\sigma\sqrt\pi}\exp(-\frac{y^2}{2\sigma^2})$, $y\ge0$ (2.29). It is the Gaussian "folded over" (p. 11).
- Student t. The Gaussian is sensitive to outliers because density decays exponentially in squared distance; the Student is more robust (pp. 11–12):
$$\mathcal T_\nu(x|\mu,\sigma^2)=\frac1Z\Big[1+\frac1\nu\Big(\frac{x-\mu}\sigma\Big)^2\Big]^{-(\frac{\nu+1}2)}\tag{2.30}$$
$$Z=\frac{\sqrt{\nu\pi\sigma^2}\,\Gamma(\frac\nu2)}{\Gamma(\frac{\nu+1}2)}=\sqrt\nu\,\sigma B(\tfrac12,\tfrac\nu2)\tag{2.31}$$
  - $\sigma$ is a scale parameter, not the standard deviation. $\nu$ (degrees of freedom) is better thought of as "degree of normality", since large $\nu$ makes it act Gaussian.
  - $\Gamma(a)\triangleq\int_0^\infty x^{a-1}e^{-x}dx$ (2.32); $B(a,b)\triangleq\frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$ (2.33).
- Cauchy ($\nu=1$): $\mathcal C(x|\mu,\gamma)=\frac1Z[1+(\frac{x-\mu}\gamma)^2]^{-1}$ (2.34), $Z=\gamma\pi$. Its tails are so heavy that the integral defining the mean does not converge. Half Cauchy: $\mathcal C_+(x|\gamma)\triangleq\frac2{\pi\gamma}[1+(\frac x\gamma)^2]^{-1}$ (2.35) (p. 12).
- Laplace (double-sided exponential), heavy-tailed: $\mathrm{Laplace}(x|\mu,b)\triangleq\frac1{2b}\exp(-\frac{|x-\mu|}b)$ (2.36), $\mu$ location, $b>0$ scale (p. 12).
- Figure 2.1 (p. 11): the Student is not log-concave for any parameter value, unlike the Laplace; both are unimodal. The Student's mean and variance are undefined when $\nu=1$.
- Kurtosis (p. 13):
$$\mathrm{kurt}(z)\triangleq\frac{\mu_4}{\sigma^4}=\frac{\mathbb E[(Z-\mu)^4]}{(\mathbb E[(Z-\mu)^2])^2}\tag{2.37}$$
  - The standard Gaussian has kurtosis 3; excess kurtosis = kurtosis − 3.
  - Super-Gaussian (leptokurtic), e.g. Laplace: positive excess kurtosis, heavier tails.
  - Sub-Gaussian (platykurtic), e.g. uniform: negative excess kurtosis, lighter tails (Fig. 2.2).

*Intuition note.* The Gaussian's density decays exponentially in the squared distance from the centre, so it is sensitive to outliers. The Student, Cauchy and Laplace are described as heavy-tailed, and the text calls the Student the more robust choice.

**2.2.3 Continuous distributions on $\mathbb R^+$ (pp. 14–17).**
- Gamma, shape $a>0$, rate $b>0$: $\mathrm{Ga}(x|a,b)\triangleq\frac{b^a}{\Gamma(a)}x^{a-1}e^{-xb}$ (2.38). Scale form with $s=1/b$: $\frac1{s^a\Gamma(a)}x^{a-1}e^{-x/s}$ (2.39). In Fig. 2.3a, if $a\le1$ the mode is at 0 (p. 14).
- Exponential: $\mathrm{Expon}(x|\lambda)\triangleq\mathrm{Ga}(x|1,\lambda)$ (2.40). It describes times between events in a Poisson process (constant average rate $\lambda$) (p. 14).
- Chi-squared: $\chi^2_\nu(x)\triangleq\mathrm{Ga}(x|\frac\nu2,\frac12)$ (2.41). If $Z_i\sim\mathcal N(0,1)$ and $S=\sum_{i=1}^\nu Z_i^2$, then $S\sim\chi^2_\nu$. Hence $X\sim\mathcal N(0,\sigma^2)\Rightarrow X^2\sim\sigma^2\chi^2_1$. With $\mathbb E[\chi_1^2]=1$, $\mathbb V[\chi_1^2]=2$:
$$\mathbb E[X^2]=\sigma^2,\ \mathbb V[X^2]=2\sigma^4\tag{2.42}$$
- Inverse gamma: $Y=1/X$, $X\sim\mathrm{Ga}(a,b)$:
$$\mathrm{IG}(x|a,b)\triangleq\frac{b^a}{\Gamma(a)}x^{-(a+1)}e^{-b/x}\tag{2.43}$$
  The mean exists only if $a>1$; the variance only if $a>2$ (p. 15).
- Scaled inverse chi-squared: $\chi^{-2}(x|\nu,\sigma^2)=\mathrm{IG}(x|\frac\nu2,\frac{\nu\sigma^2}2)$ (2.44) $=\frac1{\Gamma(\nu/2)}(\frac{\nu\sigma^2}2)^{\nu/2}x^{-\frac\nu2-1}\exp(-\frac{\nu\sigma^2}{2x})$ (2.45). The regular inverse chi-squared is the case $\nu\sigma^2=1$, i.e. $\mathrm{IG}(\frac\nu2,\frac12)$ (p. 15).
- Pareto (p. 15):
$$\mathrm{Pareto}(x|m,\kappa)=\kappa m^\kappa\frac1{x^{\kappa+1}}\mathbb I(x\ge m)\tag{2.46}$$
  - Support starts at $m$, then the density decays rapidly. On a log–log plot, $\log p(x)=-a\log x+\log c$ with $a=\kappa+1$, $c=\kappa m^\kappa$ (Fig. 2.4).
  - For $m=0$ the form is $p(x)=\kappa x^{-a}$, a power law. For $a=1$, $p(x)\propto1/x$, called a $1/f$ function if $x$ is a frequency.
  - It models heavy-tailed quantities (mostly small values, a few very large). [ACL16] argue that mixing many latent factors naturally produces heavy tails.
- Wealth (p. 16). Named after Vilfredo Pareto, who created it to model wealth. $\kappa$ is the Pareto index. $\kappa=1.16$ gives the 80-20 rule: 80% of wealth held by 20% of the population. Footnote 2: real wealth is even more skewed (as of 2014, 80 billionaires held as much as 3.5 billion people).
- Zipf's law (pp. 16–17). The most frequent word occurs about twice as often as the second, which occurs twice as often as the fourth, etc. This is a Pareto form
$$p(x=r)\propto\kappa r^{-a}\tag{2.47}$$
with $r$ the frequency rank; $a=1$ gives Zipf's law. Footnote 3: $p(x=2)=\kappa2^{-1}=2\kappa4^{-1}=2p(x=4)$. So log-frequency versus log-rank is a line of slope $-1$ (Fig. 2.5). Footnote 4: the first 10 words are removed from the plot because they fit less well.

**2.2.4 Beta (on $[0,1]$) (p. 17).**
$$\mathrm{Beta}(x|a,b)=\frac1{B(a,b)}x^{a-1}(1-x)^{b-1}\tag{2.48}$$
Need $a,b>0$ so that $B(a,b)$ exists (integrability). $a=b=1$ gives the uniform. Both $<1$ gives a bimodal shape with spikes at 0 and 1; both $>1$ gives a unimodal shape (Fig. 2.3b).

**2.2.5 Multivariate continuous distributions (pp. 17–21).**
- Multivariate normal: by far the most used; the whole of Section 2.3 is devoted to it (p. 17).
- Multivariate Student, $D$ dimensions, scale matrix $\boldsymbol\Sigma$:
$$\mathcal T_\nu(\boldsymbol x|\boldsymbol\mu,\boldsymbol\Sigma)=\frac1Z\Big[1+\frac1\nu(\boldsymbol x-\boldsymbol\mu)^\top\boldsymbol\Sigma^{-1}(\boldsymbol x-\boldsymbol\mu)\Big]^{-(\frac{\nu+D}2)}\tag{2.49}$$
$$Z=\frac{\Gamma(\nu/2)}{\Gamma(\nu/2+D/2)}\frac{\nu^{D/2}\pi^{D/2}}{|\boldsymbol\Sigma|^{-1/2}}\tag{2.50}$$
  Fatter tails than a Gaussian; smaller $\nu$ means fatter; $\nu\to\infty$ tends to a Gaussian. $\text{mean}=\boldsymbol\mu$, $\text{mode}=\boldsymbol\mu$, $\text{cov}=\frac\nu{\nu-2}\boldsymbol\Sigma$ (2.51). The mean is well defined only if $\nu>1$, the covariance only if $\nu>2$ (p. 18).
- von Mises–Fisher (circular normal), for data on the unit sphere (e.g. $\ell_2$-normalized vectors):
$$\mathrm{vMF}(\boldsymbol x|\boldsymbol\mu,\kappa)\triangleq\frac1Z\exp(\kappa\boldsymbol\mu^\top\boldsymbol x),\quad Z=\frac{(2\pi)^{D/2}I_{D/2-1}(\kappa)}{\kappa^{D/2-1}}\tag{2.52–2.53}$$
  Here $\|\boldsymbol\mu\|=1$; $\kappa\ge0$ is the concentration (analogous to $1/\sigma$); $I_r$ is the modified Bessel function of the first kind. It is like a spherical Gaussian using cosine distance. It can be used in mixture models for clustering; the author says that for $\kappa\to0$ this reduces to spherical K-means. For $D=2$ the von Mises: $\frac1Z\exp(\kappa\cos(x-\mu))$, $Z=2\pi I_0(\kappa)$ (2.54–2.55) (p. 18).
- Matrix normal, $\mathbf X\in\mathbb R^{n\times p}$, $\mathbf M\in\mathbb R^{n\times p}$, $\mathbf U\in\mathcal S_{++}^{n\times n}$ (row covariance), $\mathbf V\in\mathcal S_{++}^{p\times p}$ (column precision):
$$\mathcal{MN}(\mathbf X|\mathbf M,\mathbf U,\mathbf V)\triangleq\frac{|\mathbf V|^{n/2}}{2\pi^{np/2}|\mathbf U|^{p/2}}\exp\Big\{-\frac12\mathrm{tr}\big[(\mathbf X-\mathbf M)^\top\mathbf U^{-1}(\mathbf X-\mathbf M)\mathbf V\big]\Big\}\tag{2.56}$$
$$\mathrm{vec}(\mathbf X)\sim\mathcal N(\mathrm{vec}(\mathbf M),\mathbf V^{-1}\otimes\mathbf U)\tag{2.57}$$
  An equivalent version (2.58) uses the column covariance $\tilde{\mathbf V}=\mathbf V^{-1}$. The author adopts (2.56) because it gives a neat posterior update, as precision matrices do for the multivariate normal with conjugate prior (pp. 18–19).
- Wishart: the generalisation of the gamma to positive definite matrices, used mostly to model uncertainty when estimating covariance matrices (p. 19).
$$\mathrm{Wi}(\boldsymbol\Sigma|\mathbf S,\nu)\triangleq\frac1Z|\boldsymbol\Sigma|^{(\nu-D-1)/2}\exp\Big(-\frac12\mathrm{tr}(\mathbf S^{-1}\boldsymbol\Sigma)\Big)\tag{2.59}$$
$$Z\triangleq|\mathbf S|^{-\nu/2}2^{\nu D/2}\Gamma_D(\nu/2)\tag{2.60}$$
  - $\nu$ is the degrees of freedom and $\mathbf S$ the scale matrix. The pdf is well defined only if $\nu>D-1$.
  - $\text{mean}=\nu\mathbf S$, $\text{mode}=(\nu-D-1)\mathbf S$ (2.61); the mode exists only if $\nu>D+1$.
  - For $D=1$: $\mathrm{Wi}(\lambda|s^{-1},\nu)=\mathrm{Ga}(\lambda|\frac\nu2,\frac1{2s})$ (2.62). The text says $s=2$ gives chi-squared (see Reading notes).
  - If $\boldsymbol x_n\sim\mathcal N(\mathbf 0,\boldsymbol\Sigma)$, then the scatter matrix $\mathbf S=\sum_{n=1}^N\boldsymbol x_n\boldsymbol x_n^\top\sim\mathrm{Wi}(\boldsymbol\Sigma,N)$.
- Inverse Wishart: if $\boldsymbol\Sigma^{-1}\sim\mathrm{Wi}(\mathbf S^{-1},\nu)$ then $\boldsymbol\Sigma\sim\mathrm{IW}(\mathbf S,\nu)$, defined for $\nu>D-1$, $\mathbf S\succ0$ (p. 19):
$$\mathrm{IW}(\boldsymbol\Sigma|\mathbf S^{-1},\nu)=\frac1Z|\boldsymbol\Sigma|^{-(\nu+D+1)/2}\exp\Big(-\frac12\mathrm{tr}(\mathbf S\boldsymbol\Sigma^{-1})\Big),\quad Z_{IW}=|\mathbf S|^{\nu/2}2^{\nu D/2}\Gamma_D(\nu/2)\tag{2.63–2.64}$$
  $\text{mean}=\frac{\mathbf S}{\nu-D-1}$, $\text{mode}=\frac{\mathbf S}{\nu+D+1}$ (2.65). For $D=1$: $\mathrm{IW}(\sigma^2|s^{-1},\nu)=\mathrm{IG}(\sigma^2|\nu/2,s/2)$ (2.66); $s=1$ gives the inverse chi-squared (p. 20).
- Dirichlet: a multivariate generalisation of the beta, supported on the probability simplex (p. 20)
$$S_K=\{\boldsymbol x:0\le x_k\le1,\ \textstyle\sum_k x_k=1\}\tag{2.67}$$
$$\mathrm{Dir}(\boldsymbol x|\boldsymbol\alpha)\triangleq\frac1{B(\boldsymbol\alpha)}\prod_{k=1}^Kx_k^{\alpha_k-1}\mathbb I(\boldsymbol x\in S_K),\quad B(\boldsymbol\alpha)\triangleq\frac{\prod_k\Gamma(\alpha_k)}{\Gamma(\sum_k\alpha_k)}\tag{2.68–2.69}$$
  - With $\alpha_0=\sum_k\alpha_k$: $\alpha_0$ controls peakedness, the $\alpha_k$ control where the peak is. For $K=3$: Dir(1,1,1) is uniform; Dir(2,2,2) is broad around (1/3,1/3,1/3); Dir(20,20,20) is narrow there; Dir(3,3,20) is asymmetric, with more density near one corner. If all $\alpha_k<1$ there are spikes at the corners, and samples are sparse (Figs. 2.6, 2.7).
  - Properties:
$$\mathbb E[x_k]=\frac{\alpha_k}{\alpha_0},\ \mathrm{mode}[x_k]=\frac{\alpha_k-1}{\alpha_0-K},\ \mathbb V[x_k]=\frac{\alpha_k(\alpha_0-\alpha_k)}{\alpha_0^2(\alpha_0+1)}\tag{2.70}$$
  - Symmetric prior $\alpha_k=\alpha/K$: $\mathbb E[x_k]=1/K$, $\mathbb V[x_k]=\frac{K-1}{K^2(\alpha+1)}$. Larger $\alpha$ means higher precision.
  - Aleatoric versus epistemic uncertainty (p. 21), for a 3-sided die. If we know all outcomes are equally likely, we can use a peaky symmetric Dir(20,20,20); the text says this reflects that we are sure the outcomes will be unpredictable. If we are unsure (it could be biased), we can use a flat Dir(1,1,1), which allows a wide range of outcome distributions.
  - Making the Dirichlet depend on inputs gives a "prior network" encoding $p(\boldsymbol\pi|\boldsymbol x)$ rather than a label $p(y|\boldsymbol x)$.

*Intuition note.* A Dirichlet is a distribution over probability vectors. A peaky symmetric Dirichlet such as Dir(20,20,20) reflects being sure the outcomes will be unpredictable; a flat one such as Dir(1,1,1) allows a wide range of outcome distributions (it could be a biased die). The text says this makes the Dirichlet useful for distinguishing aleatoric (data) from epistemic uncertainty.

## Toy example (ours, not from the text)
Use the text's 3-sided die with $\mathbb P(A,B,C)=(2/6,1/6,3/6)$ as "die 1". Let "die 2" be fair: $(1/3,1/3,1/3)$. Pick a die with prior probability 0.5 each, roll once, and observe $C$.
- Likelihoods: $p(C|\text{die 1})=3/6=0.5$; $p(C|\text{die 2})=1/3\approx0.3333$.
- Marginal likelihood by total probability (2.14): $p(C)=0.5\cdot0.5+0.5\cdot\frac13=0.25+0.16667=0.41667=5/12$.
- Bayes (2.16): $p(\text{die 1}|C)=0.25/0.41667=0.6$; $p(\text{die 2}|C)=0.16667/0.41667=0.4$.
- Check: $0.6+0.4=1$. Seeing $C$ moves belief from 0.5 to 0.6 toward the die that favours $C$.

## Concepts
- [[bayes-theorem]] — rule (2.15) obtained from the definition of conditional probability, for events with positive probability (p. 8)
- [[prior-distribution]] — $p(X=k)$ in (2.16), probability before seeing evidence $E$ (p. 8)
- [[likelihood]] — $p(E|X=k)$, probability of the evidence given each state (p. 8)
- [[posterior-distribution]] — $p(X=k|E)$, state probabilities after conditioning on $E$ (p. 8)
- [[marginal-likelihood]] — $p(E)$, the normalization constant in Bayes' rule (p. 8)
- [[cox-theorem]] — footnote claim that the axioms follow from basic assumptions about reasoning under uncertainty (p. 7)
- [[probability-space]] (new) — triple $(\Omega,\mathcal F,\mathbb P)$ (p. 5)
- [[random-variable-pmf-pdf-cdf]] (new) — rv as function $\Omega\to\mathbb R$; pmf (2.1), pdf (2.3), cdf (2.4) (pp. 5–6)
- [[kolmogorov-axioms]] (new) — non-negativity, normalization, countable additivity (p. 7)
- [[conditional-independence]] (new) — factorization given a third event (2.13) (p. 8)
- [[heavy-tailed-distribution]] (new) — density decays slowly; Student, Cauchy, Laplace, Pareto (pp. 11–15)
- [[kurtosis]] (new) — $\mu_4/\sigma^4$; Gaussian = 3 (p. 13)
- [[power-law-pareto]] (new) — $p(x)\propto x^{-a}$; log–log straight line (p. 15)
- [[dirichlet-distribution]] (new) — distribution on the probability simplex; $\alpha_0$ sets peakedness (p. 20)
- [[wishart-distribution]] (new) — gamma generalised to positive definite matrices (p. 19)
- [[aleatoric-vs-epistemic-uncertainty]] (new) — aleatoric (data) uncertainty versus epistemic uncertainty; the Dirichlet is said to help distinguish them (p. 21)
- [[data-generating-process]] (new) — the underlying process whose parsimonious model the book seeks (p. 1)

## Canonical instances
- [[three-sided-die]] — running example for sample space, events, measure, and Dirichlet priors (pp. 5, 21)
- [[two-coin-flips]] — rv "number of heads" and its pmf (pp. 5–6)
- [[zipf-law]] — word frequency vs rank is a Pareto/power law with $a=1$ (pp. 16–17)
- [[eighty-twenty-rule]] — Pareto index $\kappa=1.16$ (p. 16)
- [[urn-model]] — sampling balls gives binomial and negative binomial (p. 10)

## Bridges (candidates)
- [same-math] Dirichlet prior over die probabilities ↔ Bayesian inference: Dirichlet-multinomial conjugate prior — the text treats Dir as the multivariate beta; conjugacy itself is not stated here
- [structural-analogy] Student t with large $\nu$ → Gaussian ↔ robust statistics: heavy-tailed likelihoods reduce outlier influence
- [structural-analogy] Pareto/Zipf power law ↔ computational social science: heavy-tailed wealth and word-use distributions
- [structural-analogy] Aleatoric vs epistemic uncertainty ↔ hierarchical models: a flat versus peaky prior over the outcome distribution

## Questions this raises
- Why does the Gaussian remain the default despite its outlier sensitivity? What does the Student gain and lose?
- How do the Dirichlet and Wishart priors turn into posteriors when combined with multinomial and Gaussian data (promised in later sections)?
- If real wealth is more skewed than the 80-20 value of $\kappa$, what Pareto index fits it, and are such tails truly power laws?
- What is the exact content of Cox's theorem, so that the axioms are justified rather than assumed?

## Reading notes
- This is part 1 of 3 of Chapter 2. It includes Chapter 1 "Introduction" (printed pp. 1–2) and starts at Ch. 2 §2.1 (p. 5). It ends at the end of §2.2.5.7 (Dirichlet) on printed p. 21; §2.3 (multivariate normal) is not covered. Printed = pdf − 34. Pages 3–4 are the Part I title and a blank page.
- The footer reads "Online version. December 10, 2025".
- Apparent misprints in the pages: p. 5 "$E\subseteq\mathcal F$" (an event is an element of $\mathcal F$); p. 6 "identify function" (identity); p. 14 "the rate $a$ and the scale $s=1/b$" (should be shape $a$); p. 9 binomial coefficient written with $k$ though (2.18) uses $x$.
- Eq. (2.62): the text says $s=2$ gives chi-squared, but with the printed rate $1/(2s)$ the chi-squared rate $1/2$ needs $s=1$. The page image shows exactly this.
- (2.54) labels the von Mises density "vMF". I describe the figures (Figs. 2.4–2.7) from their captions. Fig. 2.7 is cited on p. 20 but is not on these pages.
- Eqs. (2.56) prefix reads $2\pi^{np/2}$ in the image; I copied as printed.
