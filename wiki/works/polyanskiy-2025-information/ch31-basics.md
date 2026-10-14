---
id: polyanskiy-2025-information/ch31-basics
work: polyanskiy-2025-information
unit: "Chapter 28 (printed numbering): Basics of statistical decision theory"
pages: 558-574
fields: [information-theory]
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
# Basics of statistical decision theory

## L0 — One line
Statistical estimation is a game against Nature. The minimax (worst-case) risk is at least the largest Bayes (average-case) risk, with equality under mild conditions. The author says essentially all lower-bound techniques in this book boil down to this, and it gives the exact minimax risk of the unconstrained Gaussian location model.

## L1 — The gist (≤ 120 words)
How do we measure the best possible performance of an estimator? The chapter defines risk, Bayes risk (average over a prior) and minimax risk (worst case over parameters). Theorem 28.1 shows minimax ≥ worst-case Bayes risk, so lower bounds come from a well-chosen prior. Minimax theorems give equality in broad cases, via convex duality. The Gaussian location model is the running example. Its exact minimax risk is $d\sigma^2/n$ for quadratic loss. Anderson's lemma extends the exact answer to bowl-shaped losses (convex, symmetric sublevel sets). Tensorization (independent coordinates) and sample complexity show how risk scales with dimension and sample size, and that this scaling depends on the loss.

**Prerequisites:** expectation and Jensen's inequality; Gaussian conditioning; convexity and Lagrange duality; min–max inequality; basic measure theory (densities, Fatou's lemma).

## L2 — Key ideas (5–10 bullets)
- An estimator's risk $R_\theta$ depends on the unknown $\theta$. Comparing estimators needs a scalar summary: worst case (minimax) or average (Bayes). Both views are valid (p. 561).
- Bayes estimators can always be taken deterministic. Minimax estimators sometimes must randomize (pp. 562, 564).
- Theorem 28.1: $R^*\ge R^*_{\rm Bayes}=\sup_\pi R^*_\pi$. The author says all lower-bound techniques in this book essentially boil down to evaluating a Bayes risk under a sagaciously chosen prior (pp. 563–564).
- Minimax and worst-case Bayes risk are primal and dual values of a convex program. The gap can be strict (Example 28.3). It closes for finite $\Theta$ with finite $\mathcal X$ or with a loss bounded below (pp. 565–567).
- Gaussian location model (GLM: observe $\theta$ plus Gaussian noise; here $\theta\in\mathbb R^d$ unconstrained) with quadratic loss: $R^*=d\sigma^2$ via the Bayes risk with prior $\mathcal N(0,s)$ and $s\to\infty$. The maximum-likelihood estimator ($\hat\theta=X$) and, for $d\ge 3$, the James–Stein shrinkage estimator are both minimax (p. 564).
- With $n$ i.i.d. samples, the GLM minimax risk is $d\sigma^2/n$. How sample complexity scales with $d$ depends on the loss (p. 568).
- Tensor products of experiments (independent coordinates, loss summed over coordinates): $\sum_i R^*_{\rm Bayes}(\mathcal P_i)\le R^*(\mathcal P)\le\sum_i R^*(\mathcal P_i)$. The right inequality can be strict (p. 569–570).
- Anderson's lemma (via log-concavity): the conditional mean is Bayes-optimal for every bowl-shaped loss (one whose sublevel sets are convex and symmetric) under a Gaussian prior. Hence exact GLM minimax risk $\mathbb E\rho(Z/\sqrt n)$ (pp. 571–574).

## L3 — Walkthrough

### 28.1 Basic setting
- A *statistical experiment* is a family $\mathcal P=\{P_\theta:\theta\in\Theta\}$ on a common measurable space \tag{28.1} (p. 558).
- Game: Nature picks $\theta$ and draws $X\sim P_\theta$. The statistician wants to estimate $T(\theta)$, where $T:\Theta\to\mathcal Y$ is the *estimand* (e.g. $\mathbb 1\{\theta>0\}$ or $\|\theta\|$) (p. 558).
- An *estimator* is $\hat T:\mathcal X\to\hat{\mathcal Y}$. The action space $\hat{\mathcal Y}$ need not equal $\mathcal Y$. It may be randomized, i.e. a Markov kernel $P_{\hat T|X}$, written $\hat T(X,U)$ with $U$ uniform on $[0,1]$ independent of $X$ (pp. 558–559).
- Loss $\ell:\mathcal Y\times\hat{\mathcal Y}\to\mathbb R$. Since it is a loss, converses are lower bounds and achievability results are upper bounds. The risk of $\hat T$ at $\theta$ is
$$R_\theta(\hat T)=\mathbb E_\theta[\ell(T,\hat T)]=\int P_\theta(dx)P_{\hat T|X}(d\hat t|x)\,\ell(T(\theta),\hat t)\tag{28.2}$$
(p. 559).
- Remark 28.1: testing and inference are special cases. For composite-vs-composite testing, take $T(\theta)=0$ on $\Theta_0$ and $1$ on $\Theta_1$, $\hat T\in\{0,1\}$, and zero-one loss. Then the risk is the error probability. For confidence sets use $\ell(\theta,\hat T)=\mathbb 1\{\theta\notin\hat T\}+\lambda\,\mathrm{length}(\hat T)$ (p. 559).
- Remark 28.2: reasons to allow randomization. Under the minimax criterion deterministic estimators can be suboptimal. Under the Bayes criterion deterministic ones lose no generality. The space of kernels is convex (the convex hull of deterministic ones), which minimax theorems need (p. 560).
- If $\hat T\mapsto\ell(T,\hat T)$ is convex, randomization does not help. Replace $\hat T$ by $\mathbb E[\hat T|X]$. By Jensen, $R_\theta(\hat T)\ge\mathbb E_\theta\ell(T,\mathbb E[\hat T|X])$ at every $\theta$ (p. 560).

### 28.2 Gaussian location model (GLM)
- Every model can be written parametrically (take $\theta$ to be the distribution). A model is *parametric* if $\theta$ lives in finite-dimensional space, *nonparametric* if infinite-dimensional (p. 560).
- GLM: $\mathcal P=\{\mathcal N(\theta,\sigma^2I_d):\theta\in\Theta\subset\mathbb R^d\}$, i.e. $X=\theta+Z$, $Z\sim\mathcal N(0,\sigma^2I_d)$. This is the Gaussian channel of Example 3.3 and is the running example (p. 560).
- $\Theta$ encodes prior knowledge. Examples: $\mathbb R^d$; $\ell_p$-balls; $k$-sparse vectors ($\|\theta\|_0\le k$); low-rank matrices. A smaller $\Theta$ always lowers the worst-case risk, but not necessarily the computational cost (pp. 560–561).
- Typical loss: $\|\theta-\hat\theta\|_p^\alpha$; $p=\alpha=2$ is quadratic loss. Estimators: MLE $\hat\theta_{\rm ML}=X$ \tag{28.3} and James–Stein
$$\hat\theta_{\rm JS}=\Big(1-\frac{(d-2)\sigma^2}{\|X\|_2^2}\Big)X\tag{28.4}$$
(p. 561).
- Other targets: functionals $T(\theta)$ (e.g. $\|\theta\|_p$, $\max_i\theta_i$) and testing, e.g. $H_0:\theta=0$ vs $H_1:\|\theta\|\ge\epsilon$ (p. 561).

### 28.3 Bayes risk, minimax risk, minimax theorem
Setup (p. 561): Figure 28.1 shows three risk curves. $\hat\theta_1$ is pointwise better than $\hat\theta_2$ (so $\hat\theta_2$ is *inadmissible*). $\hat\theta_3$ has a higher peak but a smaller area than $\hat\theta_1$. Peak = worst case (minimax); area = average (Bayes). Both views are meaningful. From here $T(\theta)=\theta$.

**28.3.1 Bayes risk.**
- For a prior $\pi$ on $\Theta$: $R_\pi(\hat\theta)=\mathbb E_{\theta\sim\pi}[R_\theta(\hat\theta)]=\mathbb E_{\theta,X}[\ell(\theta,\hat\theta)]$ \tag{28.5}. The Bayes risk is $R^*_\pi=\inf_{\hat\theta}R_\pi(\hat\theta)$. A Bayes estimator attains it (p. 562).
- Remark 28.3: a Bayes estimator can always be deterministic, for any loss. For $\hat\theta(X,U)$,
$$R_\pi(\hat\theta)=\mathbb E_U[R_\pi(\hat\theta(\cdot,U))]\ge\inf_uR_\pi(\hat\theta(\cdot,u)).$$
Equivalently, $R_\pi$ is affine in the kernel, so its minimum is at extreme points, which are deterministic rules (p. 562).
- Quadratic loss: the Bayes estimator is $\mathbb E[\theta|X]$ and the Bayes risk is the MMSE, $R^*_\pi=\mathbb E\|\theta-\mathbb E[\theta|X]\|_2^2=\mathbb E[\mathrm{Tr}\,\mathrm{Cov}(\theta|X)]$ (p. 562).
- Example 28.1 (Gaussian prior, scalar). $X=\theta+Z$, $Z\sim\mathcal N(0,\sigma^2)$, $\theta\sim\mathcal N(0,s)$. The posterior is $\mathcal N\big(\frac{s}{s+\sigma^2}x,\frac{s\sigma^2}{s+\sigma^2}\big)$, the Bayes estimator is $\frac{s}{s+\sigma^2}X$, and
$$R^*_\pi=\frac{s\sigma^2}{s+\sigma^2}.\tag{28.6}$$
In $d$ dimensions with $\theta\sim\mathcal N(0,sI_d)$: $R^*_\pi=\frac{s\sigma^2}{s+\sigma^2}d$ \tag{28.7} (p. 563).

**28.3.2 Minimax risk.**
- A criticism of Bayes is the arbitrary prior. The frequentist alternative: $R^*=\inf_{\hat\theta}\sup_{\theta\in\Theta}R_\theta(\hat\theta)$ \tag{28.8}. An estimator attaining it is minimax (p. 563).
- Finding $R^*$ needs an upper bound (an estimator with $R_\theta\le R^*+\epsilon$ for all $\theta$) and a lower bound (for any estimator some $\theta$ has $R_\theta\ge R^*-\epsilon$). Often only a *minimax rate* $\Psi$ is sought: $c\Psi\le R^*\le C\Psi$ for universal constants, written $R^*\asymp\Psi$ \tag{28.9} (p. 563).
- **Theorem 28.1.** $R^*\ge R^*_{\rm Bayes}\triangleq\sup_{\pi\in\mathcal P(\Theta)}R^*_\pi$ \tag{28.10}. A prior attaining the supremum is *least favorable* (p. 564).
  - Proof 1 ("max ≥ mean"): $R_\pi(\hat\theta)=\mathbb E_{\theta\sim\pi}R_\theta(\hat\theta)\le\sup_\theta R_\theta(\hat\theta)$. Take $\inf_{\hat\theta}$.
  - Proof 2 ("min max ≥ max min"): $R^*=\inf_{\hat\theta}\sup_\theta R_\theta=\inf_{\hat\theta}\sup_\pi R_\pi\ge\sup_\pi\inf_{\hat\theta}R_\pi=\sup_\pi R^*_\pi$, using $\min_x\max_yf\ge\max_y\min_xf$ (p. 564).
- *Intuition note.* Nature can pick a random $\theta$ instead of the worst one, and an average never beats the maximum. So any prior gives a valid lower bound on the worst-case risk.
- Remark 28.4: minimax may need randomization. With $\theta\in\{0,1\}$, no data, and zero-one loss, the minimax risk is $\tfrac12$, achieved by guessing $\mathrm{Ber}(\tfrac12)$ but by no deterministic guess (p. 564).
- Example 28.2 (GLM, quadratic loss, $\Theta=\mathbb R^d$): $R^*=\inf_{\hat\theta}\sup_\theta\mathbb E_\theta\|\hat\theta(X)-\theta\|_2^2=d\sigma^2$ \tag{28.11}. By scaling take $\sigma=1$. Upper bound: $\hat\theta_{\rm ML}=X$ has $R_\theta=d$ for all $\theta$. Lower bound: with $\theta\sim\mathcal N(0,s)$, (28.6) gives $R^*\ge R^*_\pi=\frac{sd}{s+1}$. Sending $s\to\infty$ gives $R^*\ge d$ (p. 564).
- Remark 28.5: minimax estimators need not be unique. For $d\ge3$ the James–Stein risk is smaller than the MLE's everywhere (Figure 28.2), so it is also minimax. A continuum of minimax estimators exists (cited, [276, Thm 5.5]) (p. 564).
- Example 28.3 (strict gap). $\theta,\hat\theta\in\mathbb N$, $\ell=\mathbb 1\{\hat\theta<\theta\}$, no data. For any $\hat\theta$, $R_\theta=\mathbb P(\hat\theta<\theta)$, so $R^*\ge\lim_{\theta\to\infty}\mathbb P(\hat\theta<\theta)=1$, which is achievable. For any prior, $R_\pi(\hat\theta)=\mathbb P(\hat\theta<\theta)\to0$ as $\hat\theta\to\infty$, so $R^*_\pi=0$. Hence $R^*=1>R^*_{\rm Bayes}=0$ (p. 565).
- Exercise remark: the minimax quadratic risk of $X\sim\mathcal N(\theta,1)$ with $\theta\ge0$ equals the unconstrained value, even though $X_+=\max(X,0)$ is pointwise better. The gain vanishes asymptotically in the worst case (p. 565).

**28.3.3 Duality.**
- $R^*$ is the primal value of a convex program; $R^*_{\rm Bayes}$ is its dual. So (28.10) is weak duality, and strong duality means the minimax theorem holds (p. 565).
- For finite $\Theta$: $R^*=\min_{P_{\hat\theta|X}}\max_\theta\mathbb E_\theta[\ell(\theta,\hat\theta)]$ \tag{28.12}. This is convex because $P_{\hat\theta|X}\mapsto\mathbb E_\theta\ell$ is affine and a pointwise supremum of affine functions is convex. Augmented form:
$$R^*=\min_{P_{\hat\theta|X},t}\ t\quad\text{s.t. }\mathbb E_\theta[\ell(\theta,\hat\theta)]\le t\ \ \forall\theta\in\Theta.\tag{28.13}$$
- With multipliers $\pi_\theta\ge0$, the Lagrangian is
$$L=t+\sum_\theta\pi_\theta(\mathbb E_\theta\ell-t)=\Big(1-\sum_\theta\pi_\theta\Big)t+\sum_\theta\pi_\theta\mathbb E_\theta\ell.$$
$R^*\ge\min_{t,P}L$. Unless $\sum\pi_\theta=1$, $\min_tL=-\infty$. So $\pi$ is a probability measure, and the dual is $\max_{\pi}\min_{P}R_\pi(\hat\theta)=\max_\pi R^*_\pi$ (p. 566).
- Primal variables are (randomized) estimators; dual variables are priors. The author notes this view can be operationalized: dualizing Le Cam's two-point bound leads to optimal minimax upper bounds in some problems ([238, 346]; Exercise VI.17) (p. 566).
- *Intuition note.* The statistician picks a strategy (estimator), Nature picks a mixed strategy (prior). Weak duality says the statistician's guaranteed loss is at least Nature's guaranteed gain. Strong duality says the two meet.

**28.3.4 Minimax theorem.**
- The author recalls Chapter 5: capacity satisfies a min–max = max–min identity with a saddle point (p. 566).
- A general result ([404, Thm 46.6], cited, not proved) gives $R^*=R^*_{\rm Bayes}$ if: the experiment is dominated ($P_\theta\ll\nu$ for all $\theta$); the action space is locally compact with a countable base; and the loss is level-compact (bounded below, compact sublevel sets $\{\hat\theta:\ell(\theta,\hat\theta)\le a\}$). The author says this covers virtually all problems encountered in practice (p. 566).
- **Theorem 28.2.** $R^*=R^*_{\rm Bayes}$ if (i) $\Theta$ and $\mathcal X$ are finite, or (ii) $\Theta$ is finite and $\inf_{\theta,\hat\theta}\ell>-\infty$ (p. 567).
  - Case (i): strong duality for finite-dimensional linear programming.
  - Case (ii): if $R^*=\infty$, take the uniform prior. Some $\theta$ has $R_\theta=\infty$, so $R_\pi\ge R_\theta/|\Theta|=\infty$. If $R^*<\infty$, then $R^*\in\mathbb R$. Define the risk vector $R(\hat\theta)=(R_\theta(\hat\theta))_\theta$, with $R_\pi=\langle R(\hat\theta),\pi\rangle$. Let $S=\{R(\hat\theta):\hat\theta\text{ randomized}\}$ and $T=\{t\in\mathbb R^\Theta:t_\theta<R^*\ \forall\theta\}$. Both are convex ("why?" is left to the reader), and $S\cap T=\emptyset$. Separation gives $\pi\ne0$, $c$ with $\inf_S\langle\pi,s\rangle\ge c\ge\sup_T\langle\pi,t\rangle$. $\pi$ must be componentwise positive (else the sup over $T$ is $\infty$), so normalize it to a prior. Then $R^*_{\rm Bayes}\ge R^*_\pi=\inf_S\langle\pi,s\rangle\ge\sup_T\langle\pi,t\rangle\ge R^*$ (p. 567).

### 28.4 Multiple observations and sample complexity
- Independent sampling model: $\mathcal P_n=\{P_\theta^{\otimes n}:\theta\in\Theta\}$ \tag{28.14}. Minimax risk $R^*_n(\Theta)=\inf_{\hat\theta}\sup_\theta\mathbb E_\theta[\ell(\theta,\hat\theta)]$ \tag{28.15}. It is non-increasing in $n$ (extra data can be discarded). Typically it vanishes as $n\to\infty$ for fixed $\Theta\subset\mathbb R^d$ (p. 567).
- Sample complexity: $n^*(\epsilon)\triangleq\min\{n\in\mathbb N:R^*_n(\Theta)\le\epsilon\}$ \tag{28.16}. In classical large-sample asymptotics (Chapter 29) the quadratic risk is usually $\Theta(1/n)$ (the "parametric rate"). This book focuses on non-asymptotic dependence on dimension (p. 568).
- GLM with $n$ samples: $R^*_n=\frac{d\sigma^2}{n}$ \tag{28.17}. The sample mean $\bar X\sim\mathcal N(\theta,\frac{\sigma^2}{n}I_d)$ is sufficient, so this reduces to (28.11). Thus $n^*(\epsilon)=\lceil d\sigma^2/\epsilon\rceil$, linear in $d$ ("counting degrees of freedom") (p. 568).
- Linear scaling is not universal. For $\theta\in\mathbb R^{d\times d}$ and small constant $\epsilon$ (p. 568):
  - squared Frobenius loss: $R^*_n=d^2/n$, so $n^*=\Theta(d^2)$;
  - squared operator-norm loss: $R^*_n\asymp d/n$, so $n^*=\Theta(d)$ (Example 28.4);
  - estimating only $\theta_{\max}$: $n^*(\epsilon)=\Theta(\sqrt{\log d})$ as printed (Exercise VI.14). The last two scale sublinearly in the dimension.

### 28.5 Tensor product of experiments
- Given experiments $\mathcal P_i=\{P_{\theta_i}:\theta_i\in\Theta_i\}$ with losses $\ell_i$, $i\in[d]$, the tensor product has $P_\theta=\prod_iP_{\theta_i}$ on $\Theta=\prod_i\Theta_i$ and separable loss $\ell(\theta,\hat\theta)=\sum_i\ell_i(\theta_i,\hat\theta_i)$. The $X_i$ are independent but not identically distributed (pp. 568–569).
- **Theorem 28.3.**
$$\sum_{i=1}^d R^*_{\rm Bayes}(\mathcal P_i)\le R^*(\mathcal P)\le\sum_{i=1}^dR^*(\mathcal P_i)\tag{28.18}$$
If the minimax theorem holds for each $\mathcal P_i$, it holds for the product and $R^*(\mathcal P)=\sum_iR^*(\mathcal P_i)$ \tag{28.19} (p. 569).
  - Right inequality: estimate each $\theta_i$ from $X_i$ alone.
  - Left inequality: take a product prior $\pi=\prod\pi_i$. Any randomized $\hat\theta_i(X,U_i)$ can be rewritten $\hat\theta_i(X_i,\tilde U_i)$ with $\tilde U_i=(X_{\setminus i},U_i)\perp X_i$. So it is a randomized estimator based on $X_i$ alone, and $R_{\pi_i}(\hat\theta_i)\ge R^*_{\pi_i}$. Sum over $i$ and take suprema over $\pi_i$.
- Example: the $d$-dimensional unconstrained GLM with quadratic loss is the $d$-fold product of the scalar GLM. Minimax holds for the GLM, so risks add to $\sigma^2d$, as in Example 28.2 (p. 569).
- In general the right inequality can be strict. This is surprising, since $X_i$ carries information only about $\theta_i$. **Remark 28.6** (counterexample): $X=\theta Z$, $\theta\in\mathbb N$, $Z\sim\mathrm{Ber}(\tfrac12)$, loss $\mathbb 1\{\hat\theta<\theta\}$ (the larger guess wins).
  - One copy: $R^*=\mathbb P[Z=0]=\tfrac12$. When $Z=0$ all information is erased, so $R_\theta\ge\mathbb P[\hat\theta<\theta,Z=0]=\tfrac12\mathbb P[\hat\theta<\theta|X=0]$. Sending $\theta\to\infty$ gives $\sup_\theta R_\theta\ge\tfrac12$, achieved by $\hat\theta=X$. The minimax theorem fails here, as in Example 28.3.
  - Two copies, loss $\mathbb 1\{\hat\theta_1<\theta_1\}+\mathbb 1\{\hat\theta_2<\theta_2\}$: use $\hat\theta_1=\hat\theta_2=X_1\vee X_2$ if $X_1>0$ or $X_2>0$, else $1$. Averaging over $Z_1,Z_2$, $\mathbb E\,\ell\le\frac14(\mathbb 1\{\theta_1<\theta_2\}+\mathbb 1\{\theta_2<\theta_1\}+1)\le\frac34<1=\tfrac12+\tfrac12$ (pp. 569–570).
- *Intuition note.* Here the two coordinates share a useful hint: the larger observed value is a good guess for both. Estimating each coordinate separately throws that away. In this example (where the minimax theorem fails), independent data do not make the estimation problems decouple.
- **Theorem 28.4.** For $X_1,\dots,X_n\overset{\rm iid}\sim\mathcal N(\theta,I_d)$ and $1\le q<\infty$:
$$\inf_{\hat\theta}\sup_{\theta\in\mathbb R^d}\mathbb E_\theta\|\theta-\hat\theta\|_q^q=\frac{\mathbb E\|Z\|_q^q}{n^{q/2}},\quad Z\sim\mathcal N(0,I_d)$$
(p. 570).
  - Proof: the loss $\sum_i|\theta_i-\hat\theta_i|^q$ is separable, so by Theorem 28.3 take $d=1$. Upper bound: the sample mean $\sim\mathcal N(\theta,\frac1n)$, which is sufficient. Lower bound: prior $\mathcal N(0,s)$ gives posterior $\mathcal N\big(\mathbb E[\theta|X],\frac{s}{1+sn}\big)$. By Lemma 28.5 the conditional mean is Bayes-optimal, so $R^*_\pi=\big(\frac{s}{1+sn}\big)^{q/2}\mathbb E|Z|^q$. Send $s\to\infty$.
  - **Lemma 28.5.** For $Z\sim\mathcal N(0,1)$, $\min_y\mathbb E|y+Z|^q=\mathbb E|Z|^q$. Proof: $\mathbb E|y+Z|^q=\int_0^\infty\mathbb P[|y+Z|^q>c]dc\ge\int_0^\infty\mathbb P[|Z|^q>c]dc$, because $\mathbb P[|y+Z|\le a]\le\mathbb P[|Z|\le a]$ by symmetry and unimodality of the normal density (p. 570).

### 28.6 Log-concavity, Anderson's lemma, exact minimax risk in GLM
- Theorem 28.4 relies on separable losses. For non-separable losses, tensorization would force risk linear in $d$, which is not always the case (p. 571).
- **Definition 28.6.** $\rho:\mathbb R^d\to\mathbb R_+$ is *bowl-shaped* if each sublevel set $K_c=\{x:\rho(x)\le c\}$ is convex and symmetric ($K_c=-K_c$) (p. 571).
- **Theorem 28.7.** In the GLM with $n$ observations, loss $\ell(\theta,\hat\theta)=\rho(\theta-\hat\theta)$ with $\rho$ bowl-shaped and lower-semicontinuous:
$$R^*=\inf_{\hat\theta}\sup_\theta\mathbb E_\theta[\rho(\theta-\hat\theta)]=\mathbb E\,\rho\Big(\frac{Z}{\sqrt n}\Big),\quad Z\sim\mathcal N(0,I_d).$$
The sample mean $\bar X$ attains the upper bound (p. 571).
- **Corollary 28.8.** For $\rho=\|\cdot\|^q$ with any norm and $q>0$: $R^*=\mathbb E\|Z\|^q/n^{q/2}$ \tag{28.20} (p. 571).
- Example 28.4 (p. 571): for $\rho=\|\cdot\|_2^2$, $R^*=d/n$. For $\rho=\|\cdot\|_\infty$, $\mathbb E\|Z\|_\infty\asymp\sqrt{\log d}$ (Lemma 27.10), so $R^*\asymp\sqrt{\log d/n}$. For matrices with operator norm, $\mathbb E\|Z\|_{\rm op}\asymp\sqrt d$ (Exercise V.29), so $R^*\asymp\sqrt{d/n}$. For Frobenius norm, $R^*\asymp d/\sqrt n$. For $q=2$: $n^*(\epsilon)=\lceil\mathbb E[\|Z\|^2]/\epsilon\rceil$. So the "sample complexity ∝ number of parameters" rule of thumb need not hold (pp. 571–572).
- High-probability version: $\rho=\mathbb 1\{\|\theta-\hat\theta\|>\epsilon\}$ is bowl-shaped and lower semicontinuous, giving $R^*=\mathbb P[\|Z\|\ge\epsilon\sqrt n]$. This is stronger, since $\bar X$ is optimal for all $\epsilon$ simultaneously; integrating over $\epsilon$ recovers (28.20) (p. 572).
- **Proof of Theorem 28.7 (lower bound only; upper bound stated, not proved).** With $\pi=\mathcal N(0,sI_d)$, shapes $\theta,X\in\mathbb R^d$:
$$R^*\ge R^*_\pi=\inf_{\hat\theta}\mathbb E_\pi\rho(\theta-\hat\theta)=\mathbb E\Big[\inf_{\hat\theta}\mathbb E[\rho(\theta-\hat\theta)|X]\Big]\overset{(a)}=\mathbb E\big[\mathbb E[\rho(\theta-\mathbb E[\theta|X])|X]\big]\overset{(b)}=\mathbb E\,\rho\Big(\sqrt{\tfrac{s}{1+sn}}Z\Big).$$
(a) is Lemma 28.9. (b) holds because $\theta-\mathbb E[\theta|X]\sim\mathcal N(0,\frac{s}{1+sn}I_d)$. Then, by lower semicontinuity and Fatou's lemma, $R^*\ge\lim_{s\to\infty}\mathbb E\rho\big(\sqrt{\tfrac{s}{1+sn}}Z\big)\ge\mathbb E\rho(Z/\sqrt n)$ (p. 572).
- **Lemma 28.9 (Anderson).** For $X\sim\mathcal N(0,\Sigma)$, $\Sigma\succ0$, and $\rho$ bowl-shaped: $\min_{y}\mathbb E\rho(y+X)=\mathbb E\rho(X)$ (p. 572).
- **Lemma 28.10.** For symmetric convex $K$ and $X\sim\mathcal N(0,\Sigma)$: $\max_y\mathbb P(X+y\in K)=\mathbb P(X\in K)$ (p. 572).
- Proof of 28.9 from 28.10: $K_c$ is convex and symmetric. Then
$$\mathbb E\rho(y+X)=\int_0^\infty(1-\mathbb P(y+X\in K_c))dc\ \ge\ \int_0^\infty(1-\mathbb P(X\in K_c))dc=\int_0^\infty\mathbb P(\rho(X)\ge c)dc=\mathbb E\rho(X)$$
(pp. 572–573). The first equality uses $\mathbb P(\rho>c)=1-\mathbb P(y+X\in K_c)$.
- **Definition 28.11.** A measure $\mu$ on $\mathbb R^d$ is *log-concave* if $\mu(\lambda A+(1-\lambda)B)\ge\mu(A)^\lambda\mu(B)^{1-\lambda}$ for all measurable $A,B$ and $\lambda\in[0,1]$ (p. 573).
- **Theorem 28.12 (Prékopa; cited).** A measure with a Lebesgue density $f$ is log-concave iff $f$ is log-concave (p. 573).
- Example 28.5 (p. 573): Lebesgue measure ($f\equiv1$) gives $\mathrm{vol}(\lambda A+(1-\lambda)B)\ge\mathrm{vol}(A)^\lambda\mathrm{vol}(B)^{1-\lambda}$ \tag{28.21}, which implies Brunn–Minkowski, $\mathrm{vol}(A+B)^{1/d}\ge\mathrm{vol}(A)^{1/d}+\mathrm{vol}(B)^{1/d}$ \tag{28.22}. (Footnote: apply (28.21) to unit-volume rescalings $A'=\mathrm{vol}(A)^{-1/d}A$, $B'=\mathrm{vol}(B)^{-1/d}B$ with $\lambda=\mathrm{vol}(A)^{1/d}/(\mathrm{vol}(A)^{1/d}+\mathrm{vol}(B)^{1/d})$.) The Gaussian $\mathcal N(0,\Sigma)$ is log-concave since $\log f$ is concave in $x$.
- **Proof of Lemma 28.10** (pp. 573–574). $\mathbb P[X\in K]\overset{(a)}=\mathbb P[X\in\tfrac12(K+y)+\tfrac12(K-y)]\overset{(b)}\ge\sqrt{\mathbb P[X\in K-y]\,\mathbb P[X\in K+y]}\overset{(c)}=\mathbb P[X+y\in K]$. (a): $\tfrac12K+\tfrac12K=K$ since $K$ is convex. (b): log-concavity with $\lambda=\tfrac12$, $A=K-y$, $B=K+y$. (c): $\mathbb P[X\in K+y]=\mathbb P[X\in-K-y]=\mathbb P[X+y\in K]$, since $X$ and $K$ are symmetric. (added step) $\mathbb P[X\in K-y]=\mathbb P[X+y\in K]=\mathbb P[X\in K+y]$, so the square root in (b) equals $\mathbb P[X+y\in K]$.
- *Intuition note.* A symmetric bell-shaped noise cloud puts most mass on a symmetric convex set when the set is centred at the origin. Shifting the set off-centre can only lose probability. So the best guess under a Gaussian posterior is its centre, whatever bowl-shaped loss is used.

## Toy example (ours, not from the text)
Scalar GLM, $d=1$, $\sigma^2=1$, one observation, quadratic loss. The MLE $X$ has risk $R_\theta=1$ for every $\theta$.

Bayes risk under prior $\mathcal N(0,s)$, from (28.6): $R^*_\pi=\frac{s}{s+1}$.
- $s=1$: $1/2$.
- $s=3$: $3/4=0.75$.
- $s=9$: $9/10=0.9$.
- $s=99$: $99/100=0.99$.

Each value is $\le1$, as Theorem 28.1 requires, since $R^*\le\sup_\theta R_\theta(X)=1$. The values approach $1$ as $s\to\infty$, so $R^*=1$ and $X$ is minimax.

Randomization (Remark 28.4 style): $\theta\in\{0,1\}$, no data, zero-one loss. Deterministic guess $0$ has $(R_0,R_1)=(0,1)$; guess $1$ has $(1,0)$. Guessing $0$ or $1$ with prob. $\tfrac12$ each gives $(\tfrac12,\tfrac12)$. So the worst-case risk drops from $1$ to $\tfrac12$. For a prior $(p,1-p)$ the Bayes risk is $\min(p,1-p)\le\tfrac12$, with maximum $\tfrac12$ at $p=\tfrac12$. So $R^*=R^*_{\rm Bayes}=\tfrac12$, as Theorem 28.2 (finite case) predicts.

## Concepts
- [[statistical-experiment]] (new) — family $\{P_\theta:\theta\in\Theta\}$; Nature picks $\theta$, statistician sees $X\sim P_\theta$ (p. 558)
- [[risk-function]] (new) — $R_\theta(\hat T)=\mathbb E_\theta\ell(T,\hat T)$, expected loss at fixed $\theta$ (p. 559)
- [[randomized-estimator]] (new) — estimator as Markov kernel $P_{\hat T|X}$; sometimes needed for minimax, never needed for Bayes (pp. 558, 560, 562, 564)
- [[bayes-risk]] (new) — $R^*_\pi=\inf_{\hat\theta}R_\pi(\hat\theta)$, average-case limit under prior $\pi$ (p. 562)
- [[minimax-risk]] (new) — $\inf_{\hat\theta}\sup_\theta R_\theta(\hat\theta)$, worst-case limit (p. 563)
- [[least-favorable-prior]] (new) — a prior attaining $\sup_\pi R^*_\pi$ (p. 564)
- [[minimax-theorem]] (new) — conditions under which $R^*=R^*_{\rm Bayes}$; strong duality of a convex program (pp. 565–567)
- [[gaussian-location-model]] (new) — $X=\theta+Z$, $Z\sim\mathcal N(0,\sigma^2I_d)$; the Gaussian channel viewed as estimation (p. 560)
- [[sample-complexity]] (new) — $n^*(\epsilon)=\min\{n:R^*_n\le\epsilon\}$ (p. 568)
- [[tensorization-of-experiments]] (new) — product experiments with separable loss; minimax risk between sum of Bayes and sum of minimax risks (p. 569)
- [[bowl-shaped-loss]] (new) — loss whose sublevel sets are convex and symmetric (p. 571)
- [[anderson-lemma]] (new) — under Gaussian noise, shifting cannot lower expected bowl-shaped loss (p. 572)
- [[log-concave-measure]] (new) — $\mu(\lambda A+(1-\lambda)B)\ge\mu(A)^\lambda\mu(B)^{1-\lambda}$ (p. 573)
- [[noisy-channel]] — the GLM corresponds to the Gaussian channel (p. 560)

## Canonical instances
- [[blind-guess-randomization]] — $\theta\in\{0,1\}$, no data: minimax risk $\tfrac12$ needs a randomized guess (p. 564)
- [[blind-guess-larger-number]] — $\ell=\mathbb 1\{\hat\theta<\theta\}$ on $\mathbb N$: $R^*=1>R^*_{\rm Bayes}=0$ (p. 565)
- [[glm-minimax-quadratic]] — $R^*=d\sigma^2$ (single sample), $d\sigma^2/n$ (n samples) (pp. 564, 568)
- [[james-stein-estimator]] — for $d\ge3$ its risk is below the MLE's everywhere, yet both are minimax (p. 564)
- [[erased-observation-tensorization]] — $X=\theta Z$: product minimax risk strictly below the sum (pp. 569–570)

## Bridges (candidates)
- [structural-analogy] Primal–dual (minimax = worst-case Bayes) ↔ capacity: $C=\min_{P_X}\max_{Q_Y}=\max_{Q_Y}\min_{P_X}D(P_{Y|X}\|Q_Y|P_X)$ with saddle point — the text recalls it as an example of a similar minimax theorem (p. 566).
- [structural-analogy] Bayes risk with Gaussian prior and $s\to\infty$ ↔ I-MMSE: Bayes risk under quadratic loss is the MMSE (p. 562).
- [structural-analogy] Randomized estimators as Markov kernels ↔ channels and rate–distortion: action space $\hat{\mathcal Y}$ vs $\mathcal Y$ (p. 558).
- [metaphor] Least-favorable prior ↔ capacity-achieving input distribution: the adversary's best mixed strategy.

## Questions this raises
- When the minimax theorem fails (Example 28.3), how large can the gap $R^*-R^*_{\rm Bayes}$ be, and what extra structure repairs it?
- For constrained $\Theta$ (sparse, low-rank), which priors are least favorable, and how do lower bounds from them match upper bounds?
- Why is the rate $d/n$ for quadratic loss but $\sqrt{\log d/n}$ for $\ell_\infty$ loss? What does this say about which parameters matter?
- Can the dual (prior-side) view be turned into constructive upper bounds, as Le Cam duality is said to do (p. 566)?

## Exercises worth doing
The unit prints no numbered exercises. It points to these (statements are in later chapters, not here):
- Exercise VI.17 (p. 566) — dualizing Le Cam's two-point bound to get minimax upper bounds — difficulty: hard
- Exercise VI.14 (p. 568) — sample complexity of estimating $\theta_{\max}$ — difficulty: medium
- Exercise V.29 (p. 571) — $\mathbb E\|Z\|_{\rm op}\asymp\sqrt d$, used in Example 28.4 — difficulty: medium
- In-text prompts: show the minimax risk with $\theta\ge0$ equals the unconstrained value (p. 565); show $S$ and $T$ are convex (p. 567) — difficulty: medium / easy

## Reading notes
- Printed = pdf − 25. The unit is labelled "ch31" in the metadata, but the printed chapter number is 28 (sections 28.1–28.6).
- Chapter intro lists sections 28.1, 28.3, 28.4, 28.5, 28.2, 28.6 and skips 28.2 in its first mention. This is harmless.
- Misprints visible in the images:
  - Example 28.1 multivariate case: "$Z\sim\mathcal N(0,I_d)$" but the formula uses $\sigma^2$ (should be $\mathcal N(0,\sigma^2I_d)$).
  - Example 28.2: "$\inf_{\theta\in\mathbb R^d}$" should be $\inf_{\hat\theta}$.
  - Section 28.4: data "$X_i\sim\mathcal N(0,\sigma^2I_d)$", and Theorem 28.7: "$X_i\sim\mathcal N(0,I_d)$"; the mean should be $\theta$.
  - Lemma 28.10: "$K\in\mathbb R^d$" should be $K\subset\mathbb R^d$.
  - Remark 28.6, two copies: the page prints $\frac14(\mathbb 1\{\theta_1<\theta_2\}+\mathbb 1\{\theta_2<\theta_1\}+1)\le\frac34$. The last term appears undercounted: when $Z_1=Z_2=0$ the guess $1$ can lose up to $2$, which would give $+2$ and exactly $\frac34$.
  - After Theorem 28.3 the text says "the right inequality of (28.19)"; this evidently means (28.18).
  - Section 28.3.2 says the Bayes risk "is always lower" than the minimax risk; the theorem gives "$\le$".
  - Proof of Lemma 28.10 step (c): the text equates $\mathbb P[X\in K+y]$ with $\mathbb P[X+y\in K]$; the intermediate step $\mathbb P[X\in K-y]=\mathbb P[X\in K+y]$ is left implicit (I added it in the walkthrough).
- The $n^*(\epsilon)=\Theta(\sqrt{\log d})$ claim for $\theta_{\max}$ is as printed (p. 568); its proof is in an exercise not shown.
- Lemma 27.10, Exercise V.29, and the cited theorems (Prékopa, [404, Thm 46.6], Le Cam) are not proved in these pages.
