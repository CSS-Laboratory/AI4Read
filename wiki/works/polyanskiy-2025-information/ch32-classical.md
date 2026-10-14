---
id: polyanskiy-2025-information/ch32-classical
work: polyanskiy-2025-information
unit: "Chapter 29 (unit id ch32-classical) — Classical large-sample asymptotics"
pages: 575-584
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
# Classical large-sample asymptotics

## L0 — One line
For smooth parametric models in fixed dimension, the minimax squared error is asymptotically $\frac{1+o(1)}{n}\sup_\theta \mathrm{Tr}\,J_F^{-1}(\theta)$, under suitable conditions, where the lower bound comes from the Bayesian Cramér–Rao bound (motivated by data processing for $\chi^2$-divergence) and the maximum likelihood estimator (MLE) heuristically matches it.

## L1 — The gist (≤ 120 words)
How well can any estimator of $\theta$ do from $n$ iid samples when the model is smooth and the dimension is fixed? The chapter answers with a sharp constant: the minimax squared error is $\frac{1+o(1)}{n}\sup_\theta\mathrm{Tr}\,J_F^{-1}(\theta)$. The lower bound comes from comparing the model with a shifted copy. Data processing for $\chi^2$-divergence gives the Hammersley–Chapman–Robbins (HCR) and Cramér–Rao bounds and, with a prior, motivates the Bayesian Cramér–Rao (BCR) bound, which is later proved directly. The MLE matches the bound heuristically. Applications: discrete distributions and entropy. The chapter warns that one must be careful extending these results to high dimension, especially when bias becomes the dominating factor.

**Prerequisites:** $\chi^2$-divergence and its data-processing/variational form; Fisher information and its additivity; Bayes vs. minimax risk; Cauchy–Schwarz; CLT and law of large numbers; Taylor expansion.

## L2 — Key ideas
- Main result (29.1): minimax risk $\approx \frac1n\sup_\theta \mathrm{Tr}J_F^{-1}(\theta)$ under suitable conditions; the sole asymptotics is $n\to\infty$ (p. 575).
- HCR bound: data processing plus the variational form of $\chi^2$ lower-bounds variance. Its small-shift limit gives Cramér–Rao for unbiased estimators (pp. 576–577).
- Bayesian version: shift the prior by $\delta$ and compare joint laws. This gives a bound valid for all estimators, with the prior's Fisher information $J(\pi)$ added to the data's (pp. 577–578).
- BCR (Theorems 29.2, 29.3) has a direct Cauchy–Schwarz proof. Among compactly supported densities, a squared-cosine density is known to minimize the Fisher information $J$ (pp. 578–580).
- Theorem 29.4 uses BCR with a shrinking box prior ($\delta=n^{-1/4}$) to obtain the minimax lower bound. The same argument gives a bound for smooth functionals (pp. 580–581).
- The MLE is heuristically asymptotically efficient, via a local quadratic expansion of the log-likelihood. It can fail to exist, be inconsistent, or miss the rate in high dimension (pp. 581–583).
- Applications: fixed-$k$ distribution estimation has minimax risk $\frac1n(\frac{k-1}{k}+o(1))$, and entropy estimation has minimax risk $\frac1n(\max_P V(P)+o(1))$. For large alphabets, bias can dominate (pp. 583–584).

## L3 — Walkthrough

**Setup (p. 575).** Data $X_1,\dots,X_n\overset{iid}{\sim}P_\theta$, $\Theta\subset\mathbb R^d$ open, quadratic risk. Claim, under suitable conditions:
$$\inf_{\hat\theta}\sup_{\theta\in\Theta}\mathbb E_\theta\|\hat\theta-\theta\|_2^2=\frac{1+o(1)}{n}\sup_{\theta\in\Theta}\mathrm{Tr}\,J_F^{-1}(\theta).\tag{29.1}$$

### 29.1 Lower bounds from data processing (p. 575)
Method: compare the true model with a perturbed one. Relate the estimator to an $f$-divergence by data processing and the variational representation.

**29.1.1 HCR bound.**
**Theorem 29.1.** For any estimator $\hat\theta$ (p. 576):
$$R_\theta(\hat\theta)=\mathbb E_\theta[(\hat\theta-\theta)^2]\ge \mathrm{Var}_\theta(\hat\theta)\ge\sup_{\theta'\ne\theta}\frac{(\mathbb E_\theta[\hat\theta]-\mathbb E_{\theta'}[\hat\theta])^2}{\chi^2(P_{\theta'}\|P_\theta)}.\tag{29.2}$$
Proof: write $P_X=P_\theta$, $Q_X=P_{\theta'}$ (p. 576). Then
$$\chi^2(P_X\|Q_X)\ge\chi^2(P_{\hat\theta}\|Q_{\hat\theta})\ge\frac{(\mathbb E_\theta[\hat\theta]-\mathbb E_{\theta'}[\hat\theta])^2}{\mathrm{Var}_\theta(\hat\theta)}.\tag{29.3}$$
The first step is data processing (Thm 7.4). The second is the variational form (7.91) of $\chi^2$.

For unbiased $\hat\theta$ ($\mathbb E_\theta\hat\theta=\theta$ for all $\theta$): $\mathrm{Var}_\theta(\hat\theta)\ge\sup_{\theta'\neq\theta}(\theta-\theta')^2/\chi^2(P_{\theta'}\|P_\theta)$. Take $\theta'\to\theta$ and use the Fisher expansion of $\chi^2$ (Thm 7.22). Under its regularity conditions this gives Cramér–Rao (p. 576):
$$\mathrm{Var}_\theta(\hat\theta)\ge 1/J_F(\theta).\tag{29.4}$$
Multivariate case (unbiased, $\mathrm{Cov}_\theta(\hat\theta)\succ0$, p. 576): apply Thm 29.1 to $\langle a,\hat\theta\rangle$ to get $\chi^2(P_\theta\|P_{\theta'})\ge\langle a,\theta-\theta'\rangle^2/(a^\top\mathrm{Cov}_\theta(\hat\theta)a)$. Optimizing over $a$, using $\sup_{x\ne0}\langle x,y\rangle^2/x^\top\Sigma x=y^\top\Sigma^{-1}y$ attained at $x=\Sigma^{-1}y$, gives $\chi^2(P_\theta\|P_{\theta'})\ge(\theta-\theta')^\top\mathrm{Cov}_\theta(\hat\theta)^{-1}(\theta-\theta')$. With $\chi^2(P_\theta\|P_{\theta'})=(\theta-\theta')^\top J_F(\theta)(\theta-\theta')(1+o(1))$:
$$\mathrm{Cov}_\theta(\hat\theta)\succeq J_F^{-1}(\theta).\tag{29.5}$$
For $n$ iid samples the Fisher information is $nJ_F(\theta)$ (additivity, (2.36)). So unbiased estimators satisfy $\mathbb E_\theta\|\hat\theta-\theta\|^2\ge\frac1n\mathrm{Tr}J_F^{-1}(\theta)$ (p. 577). This is close to (29.1) except for the unbiasedness restriction.

*Intuition note:* If two parameters give nearly identical data laws (small $\chi^2$), no estimator can separate them well. Fisher information measures this local indistinguishability, so $1/J_F$ is the variance floor for unbiased estimators.

**29.1.2 Bayesian CR and HCR (p. 577).** Unbiasedness is not required in the minimax setting; trading bias for variance is often wise. Fix a prior $\pi$ and the chain $\theta\to X\to\hat\theta$. Two joint laws of $(\theta,X)$:
- $Q$: $\theta\sim\pi$, $X\sim P_\theta$.
- $P$: $\theta\sim T_\delta\pi$ (the prior shifted by $\delta$, $T_\delta\pi(A)=\pi(A-\delta)$), $X\sim P_{\theta-\delta}$.

Data processing and the variational form give
$$\chi^2(P_{\theta X}\|Q_{\theta X})\ge\chi^2(P_{\theta\hat\theta}\|Q_{\theta\hat\theta})\ge\chi^2(P_{\theta-\hat\theta}\|Q_{\theta-\hat\theta})\ge\frac{(\mathbb E_P[\theta-\hat\theta]-\mathbb E_Q[\theta-\hat\theta])^2}{\mathrm{Var}_Q(\hat\theta-\theta)}.$$
By design $P_X=Q_X$, so $\mathbb E_P\hat\theta=\mathbb E_Q\hat\theta$, while $\mathbb E_P\theta=\mathbb E_Q\theta+\delta$. The numerator is therefore $\delta^2$. Also $\mathbb E_\pi[(\hat\theta-\theta)^2]\ge\mathrm{Var}_Q(\hat\theta-\theta)$. Hence the Bayes risk (and, by Thm 28.1, the minimax risk) satisfies the Bayesian HCR bound
$$R^*_\pi\triangleq\inf_{\hat\theta}\mathbb E_\pi[(\hat\theta-\theta)^2]\ge\sup_{\delta\ne0}\frac{\delta^2}{\chi^2(P_{X\theta}\|Q_{X\theta})}.\tag{29.6}$$
Chain rule: $\chi^2(P_{X\theta}\|Q_{X\theta})=\chi^2(P_\theta\|Q_\theta)+\mathbb E_Q\big[\chi^2(P_{X|\theta}\|Q_{X|\theta})(dP_\theta/dQ_\theta)^2\big]$ (p. 577). Under the regularity conditions of Thm 7.22 (p. 578): $\chi^2(P_\theta\|Q_\theta)=(J(\pi)+o(1))\delta^2$, with $J(\pi)=\int\pi'^2/\pi$ the Fisher information of the prior; and $\chi^2(P_{X|\theta}\|Q_{X|\theta})=[J_F(\theta)+o(1)]\delta^2$. This yields
$$R^*_\pi\ge\frac{1}{J(\pi)+\mathbb E_{\theta\sim\pi}[J_F(\theta)]}.\tag{29.7}$$
*(added step: dP_θ/dQ_θ → 1 as δ→0, so the two terms add to $(J(\pi)+\mathbb E J_F+o(1))\delta^2$; the text does not spell this out.)*

**Example 29.1 (Gaussian location, p. 578).** $X^n\overset{iid}\sim\mathcal N(\theta,1)$, prior $\theta\sim\mathcal N(0,s)$. By sufficiency of $\bar X$ and the chain rule, with $Q_\theta=\mathcal N(0,s)$, $Q_{\bar X|\theta}=\mathcal N(\theta,1/n)$, $P_\theta=\mathcal N(\delta,s)$, $P_{\bar X|\theta}=\mathcal N(\theta-\delta,1/n)$:
$$\chi^2=e^{\delta^2/s}-1+e^{\delta^2/s}(e^{n\delta^2}-1)=e^{\delta^2(n+1/s)}-1.$$
Then $R^*_\pi\ge\sup_{\delta\neq0}\frac{\delta^2}{e^{\delta^2(n+1/s)}-1}=\lim_{\delta\to0}(\cdot)=\frac{s}{sn+1}$. The text says this matches the Bayes risk of Example 28.1, so both bounds are exact here.

### 29.2 BCR bounds and extensions (p. 578)
**Theorem 29.2 (BCR).** Let $\pi$ be a differentiable prior density on $[\theta_0,\theta_1]$ with $\pi(\theta_0)=\pi(\theta_1)=0$ and
$$J(\pi)\triangleq\int_{\theta_0}^{\theta_1}\frac{\pi'(\theta)^2}{\pi(\theta)}d\theta<\infty.\tag{29.8}$$
Let $p_\theta(x)$ be differentiable in $\theta$ for $\mu$-a.e. $x$, with $\int\mu(dx)\,\partial_\theta p_\theta(x)=0$ for $\pi$-a.e. $\theta$ (29.9). Then
$$R^*_\pi\ge\frac1{\mathbb E_{\theta\sim\pi}[J_F(\theta)]+J(\pi)}.\tag{29.10}$$
Proof (p. 579): $\hat\theta$ may be taken deterministic (Remark 28.3). For each $x$, integration by parts gives $\int d\theta\,(\hat\theta(x)-\theta)\partial_\theta(p_\theta(x)\pi(\theta))=\int p_\theta(x)\pi(\theta)d\theta$. Integrating over $\mu(dx)$ gives $\mathbb E[(\hat\theta-\theta)V(\theta,X)]=1$, where $V=\partial_\theta\log p_\theta(x)+\partial_\theta\log\pi(\theta)$. Cauchy–Schwarz gives $\mathbb E[(\hat\theta-\theta)^2]\,\mathbb E[V^2]\ge1$. By (29.9), $\mathbb E[V^2]=\mathbb E[J_F(\theta)]+J(\pi)$.

**Theorem 29.3 (multivariate BCR).** Product prior $\pi=\prod_i\pi_i$ on a box, each $\pi_i$ differentiable and vanishing on the boundary; $\int\mu(dx)\nabla_\theta p_\theta(x)=0$ (29.11). Then
$$R^*_\pi\ge\mathrm{Tr}\big((\mathbb E_{\theta\sim\pi}[J_F(\theta)]+J(\pi))^{-1}\big),\tag{29.12}$$
with $J(\pi)=\mathrm{diag}(J(\pi_1),\dots,J(\pi_d))$ (pp. 579–580). Proof: integration by parts in $\theta_i$ gives $\mathbb E[(\hat\theta_k-\theta_k)\langle u,\nabla\log(p_\theta\pi)\rangle]=\langle u,e_k\rangle$. Cauchy–Schwarz and optimizing over $u$ give $\mathbb E(\hat\theta_k-\theta_k)^2\ge\sup_u\langle u,e_k\rangle^2/u^\top\Sigma u=\Sigma^{-1}_{kk}$, with $\Sigma=\mathbb E_\pi[J_F]+J(\pi)$. Sum over $k$.

Remarks (p. 580):
- A uniform prior gives a similar bound, the Chernoff–Rubin–Stein inequality (Ex. VI.4), which also suffices for the minimax lower bound.
- To make the bound strong, choose a prior with minimum Fisher information. On compact support the minimizer is $g(u)=\cos^2(\pi u/2)$ on $[-1,1]$, with $\min_g J(g)=\pi^2$ (29.13).
- Functional version, under the same condition as Thm 29.3, for smooth $T:\mathbb R^d\to\mathbb R^s$ with $s\times d$ Jacobian $\nabla T$:
$$\inf_{\hat T}\mathbb E_\pi\|\hat T(X)-T(\theta)\|^2\ge\mathrm{Tr}\big(\mathbb E[\nabla T](\mathbb E[J_F]+J(\pi))^{-1}\mathbb E[\nabla T]^\top\big).\tag{29.14}$$

**Theorem 29.4.** If $\theta\mapsto J_F(\theta)$ is continuous, then as $n\to\infty$, $R^*_n\triangleq\inf_{\hat\theta}\sup_\theta\mathbb E_\theta\|\hat\theta-\theta\|^2\ge\frac{1+o(1)}{n}\sup_\theta\mathrm{Tr}J_F^{-1}(\theta)$ (29.15).
Proof (pp. 580–581): fix $\theta$. For small $\delta$ the box $\theta+[-\delta,\delta]^d\subset\Theta$. Let $\pi_i(\cdot)=\frac1\delta g(\cdot/\delta)$, a rescaled $g$ of (29.13) centred at the fixed $\theta$. Then $J(\pi_i)=\pi^2/\delta^2$ (scaling rule (2.35)) and $J(\pi)=\frac{\pi^2}{\delta^2}I_d$. Continuity of $J_F$ implies (29.11) (cited from [68]). Minimax $\ge$ Bayes risk, and Fisher information is additive, so
$$R^*_n\ge\frac1n\mathrm{Tr}\Big(\big(\mathbb E_{\theta\sim\pi}[J_F(\theta)]+\tfrac{\pi^2}{n\delta^2}I_d\big)^{-1}\Big).$$
Choose $\delta=n^{-1/4}$. *(added step: then $\pi^2/(n\delta^2)=\pi^2n^{-1/2}\to0$ and $\delta\to0$.)* Continuity of $J_F$ then gives the claim. The same argument with (29.14) gives, for functionals (p. 581):
$$\inf_{\hat T}\sup_\theta\mathbb E_\theta\|\hat T-T(\theta)\|^2\ge\frac{1+o(1)}{n}\sup_\theta\mathrm{Tr}\big(\nabla T J_F^{-1}\nabla T^\top\big).\tag{29.16}$$

*Intuition note:* A prior on a tiny box makes the problem "local" while still allowing biased estimators. The prior's own information $\pi^2/\delta^2$ is small compared with the data's $n$ because $\delta$ shrinks slowly.

### 29.3 MLE and asymptotic efficiency (p. 581)
Estimators attaining the information bound are called asymptotically efficient. The text gives only a sketch; rigorous versions need long lists of conditions, even longer for uniformity in $\theta$.

MLE: $\hat\theta_{\rm MLE}\in\arg\max_\theta L_\theta(X^n)$, with $L_\theta=\sum_i\log p_\theta(X_i)$ (29.17). For discrete $P_\theta$, $\hat\theta_{\rm MLE}\in\arg\min_\theta D(\hat P_n\|P_\theta)$, a KL projection of the empirical distribution (reverse of the information projection of Sec. 15.3).

*Consistency intuition (p. 582):* if the model is identifiable, then for $\theta\neq\theta_0$, $\mathbb E_{\theta_0}[L_\theta-L_{\theta_0}]=-nD(P_{\theta_0}\|P_\theta)<0$. This iid sum is therefore negative with high probability for large $n$. Consistency follows under regularity conditions, including Wald's integrability condition.

*Normality (p. 582):* with score $V=\nabla_\theta\log p_\theta(x)$ and $H=\nabla^2_\theta\log p_\theta(x)$, Taylor expansion gives
$$L_\theta=L_{\theta_0}+(\theta-\theta_0)^\top\sum_iV(\theta_0,X_i)+\tfrac12(\theta-\theta_0)^\top\Big(\sum_iH(\theta_0,X_i)\Big)(\theta-\theta_0)+o(n(\theta-\theta_0)^2).\tag{29.18}$$
Under regularity, $\mathbb E V=0$ and $\mathbb E[VV^\top]=-\mathbb E[H]=J_F(\theta_0)$. By the CLT and weak law, $\frac1{\sqrt n}\sum V\xrightarrow{d}\mathcal N(0,J_F(\theta_0))$ and $\frac1n\sum H\xrightarrow{\mathbb P}-J_F(\theta_0)$. So
$$L_\theta\approx L_{\theta_0}+\langle\sqrt{nJ_F(\theta_0)}Z,\theta-\theta_0\rangle-\tfrac n2(\theta-\theta_0)^\top J_F(\theta_0)(\theta-\theta_0),\quad Z\sim\mathcal N(0,I_d).$$
Maximizing gives $\hat\theta_{\rm MLE}\approx\theta_0+\frac1{\sqrt n}J_F(\theta_0)^{-1/2}Z$. Hence $\mathbb E\|\hat\theta_{\rm MLE}-\theta_0\|^2\le\frac1n(\mathrm{Tr}J_F^{-1}+o(1))$. By the delta method, $\mathbb E\|T(\hat\theta_{\rm MLE})-T(\theta_0)\|^2\le\frac1n(\mathrm{Tr}(\nabla TJ_F^{-1}\nabla T^\top)+o(1))$. These match (29.15) and (29.16). The derivation is heuristic and needs extra assumptions (e.g. Cramér's condition). Uniformity in $\theta$ needs stronger ones; the general theory is due to Hájek and Le Cam (p. 582).

Limitations (p. 583):
- The MLE may not exist. For a two-component Gaussian mixture with unknown means and variances, set $\mu_1=X_1$, $\sigma_1\to0$; the likelihood is unbounded.
- The MLE may be inconsistent, even in one-dimensional families (examples cited).
- In high dimensions the MLE may miss the minimax rate (Ex. VI.15).

### 29.4 Discrete distributions and entropy (pp. 583–584)
Setting: $X_i\overset{iid}\sim P\in\mathcal P_k=\mathcal P([k])$, fixed $k$.

**Theorem 29.5.** $R^*_{\rm sq}(k,n)\triangleq\inf_{\hat P}\sup_P\mathbb E\|\hat P-P\|_2^2=\frac1n\big(\frac{k-1}{k}+o(1)\big)$.
Proof: parametrize $\theta=(P_1,\dots,P_{k-1})$, $P=T(\theta)$ affine, $\nabla T=\begin{bmatrix}I_{k-1}\\-\mathbf 1^\top\end{bmatrix}$. By (2.37)–(2.38), $J_F^{-1}=\mathrm{diag}(\theta)-\theta\theta^\top$ and
$$\nabla TJ_F^{-1}\nabla T^\top=\begin{bmatrix}\mathrm{diag}(\theta)-\theta\theta^\top&-P_k\theta\\-P_k\theta^\top&P_k(1-P_k)\end{bmatrix}.$$
Its trace is $\sum_iP_i(1-P_i)=1-\sum_iP_i^2$, maximal ($1-1/k$) at the uniform distribution. Then (29.16) gives the lower bound. Upper bound: the MLE is the empirical distribution (Ex. VI.8), with $n\hat P_i\sim\mathrm{Bin}(n,P_i)$. So $\mathbb E\|\hat P-P\|^2=\frac1n\sum P_i(1-P_i)\le\frac1n(1-\frac1k)$.

Remarks (p. 584):
- Exactly, for all $k,n$: $R^*_{\rm sq}=\frac{1-1/k}{(1+\sqrt n)^2}$ (Ex. VI.7h), via a Dirichlet prior and the additively smoothed empirical distribution.
- $R^*_{\rm sq}$ does not grow with $k$; the text says squared loss is too weak for probability vectors. For $f$-divergence losses the rates do depend on $k$. For KL risk: $\Theta(k/n)$ for $k\le n$ and $\Theta(\log\frac kn)$ for $k\gg n$ (Ex. VI.8, VI.10). This agrees with the rule of thumb that consistent estimation needs $n$ to grow faster than the dimension.

**Theorem 29.6 (entropy).** For fixed $k$, $R^*_{\rm ent}(k,n)=\inf_{\hat H}\sup_P\mathbb E[(\hat H-H(P))^2]=\frac1n(\max_PV(P)+o(1))$, where $H(P)=\mathbb E\log\frac1{P(X)}$ and $V(P)=\mathrm{Var}\log\frac1{P(X)}$ is the varentropy. It follows from (29.16) and the analysis of the empirical-entropy MLE.

Large alphabets (p. 584): $\max_PV(P)\asymp\log^2k$, which suggests that $R^*_{\rm ent}$ may satisfy $R^*_{\rm ent}\asymp\log^2k/n$ even when $k$ grows with $n$ (footnote: $\max_PV(P)\le\log^2k$ for $k\ge3$ is cited from [334]; for the lower bound the footnote suggests $P=(\frac12,\frac1{2(k-1)},\dots,\frac1{2(k-1)})$). This holds only for sufficiently small alphabets. The empirical entropy has bias of order $k/n$ (Lemma 13.2). Polynomial approximation reduces the bias to $\frac{k}{n\log k}$. Consistent estimation is possible if and only if $n\gg k/\log k$, and then $R^*_{\rm ent}\asymp(\frac{k}{n\log k})^2+\frac{\log^2k}{n}$. Lesson: be careful extending classical results to high dimension, especially when bias dominates.

## Toy example (ours)
Bernoulli($p$), one parameter ($d=1$). Fisher information per sample: $J_F(p)=\frac1{p(1-p)}$.
- At $p=\tfrac12$: $J_F=1/(0.5\cdot0.5)=4$. For $n=100$ the bound is $\frac1{nJ_F}=\frac1{400}=0.0025$.
- The sample mean is unbiased with variance $p(1-p)/n=0.25/100=0.0025$. It meets the bound exactly.
- Worst case: $J_F^{-1}(p)=p(1-p)$ is largest at $p=\tfrac12$ (0.25). At $p=0.1$ it is $0.09$. So (29.1) predicts minimax risk $\approx\frac{0.25}{n}$.
- Check against Thm 29.5 with $k=2$: the loss counts both coordinates, so $\|\hat P-P\|^2=2(\hat p-p)^2$, with risk $2\times0.0025=0.005=\frac1n(1-\frac12)$. ✓.

## Concepts
- [[fisher-information]] — curvature of log-likelihood; sets the $1/(nJ_F)$ variance floor for unbiased estimators (and the asymptotic minimax constant), with matrix form $J_F^{-1}$ (p. 575; local $\chi^2$ expansion p. 576).
- [[f-divergence]] — here mainly $\chi^2$, used with data processing and its variational form to bound variance (p. 576).
- [[data-processing-inequality]] — processing $X$ into $\hat\theta$ cannot raise $\chi^2$ divergence; the engine of the HCR/CR derivations and the heuristic route to BCR (pp. 576–577).
- [[relative-entropy-kl-divergence]] — gives the intuition for MLE consistency ($-nD<0$) and the KL-projection view of the MLE (pp. 581–582).
- [[minimax-risk]] (new) — $\inf_{\hat\theta}\sup_\theta$ of expected loss; bounded below by the Bayes risk for any prior (pp. 575, 577).
- [[cramer-rao-bound]] (new) — $\mathrm{Var}\ge1/J_F$ for unbiased estimators; derived as the small-shift limit of HCR (p. 576).
- [[bayesian-cramer-rao-van-trees]] (new) — $R^*_\pi\ge1/(\mathbb E J_F+J(\pi))$ for all estimators under regularity conditions; includes the prior's Fisher information (pp. 577–579).
- [[maximum-likelihood-estimator]] (new) — maximizer of total log-likelihood; asymptotically efficient under conditions (p. 581).
- [[varentropy]] (new) — variance of $\log(1/P(X))$; controls entropy-estimation risk (p. 584).

## Canonical instances
- [[gaussian-location-model]] — Bayes risk $s/(sn+1)$, exactly met by Bayesian HCR/CR bounds (p. 578).
- [[discrete-distribution-estimation]] — asymptotic minimax squared error $\frac1n\frac{k-1}k$ for fixed $k$, with the worst case at uniform $P$ (p. 583).
- [[entropy-estimation]] — fixed-$k$ rate $\max V/n$; breakdown through bias for large $k$ (p. 584).
- [[gaussian-mixture-mle-nonexistence]] — likelihood unbounded as $\sigma_1\to0$ with $\mu_1=X_1$ (p. 583).

## Bridges (candidates)
- [same-math] MLE as $\arg\min_\theta D(\hat P_n\|P_\theta)$ ↔ ML training: minimizing cross-entropy loss on data (discrete case, p. 581).
- [same-math] Local $\chi^2$/KL expansion with Fisher information ↔ information geometry: Fisher–Rao metric as local divergence curvature.
- [structural-analogy] Data-processing proof of estimation bounds ↔ Fano/converse arguments in channel coding: both bound error through a divergence or mutual-information inequality.

## Questions this raises
- When do the regularity conditions (e.g. (29.11), Wald, Cramér) fail, and what happens to the bound?
- How does the asymptotic constant $\mathrm{Tr}J_F^{-1}$ change with the loss, e.g. KL instead of squared error?
- Where exactly does the fixed-$d$ theory break down as $k/n$ grows, and how does bias enter the rate?
- Is the squared-cosine prior optimal beyond this proof technique?

## Exercises worth doing
Difficulty labels are our guesses; the exercise statements are not on these pages.
- Ex. VI.7 (p. 575) — minimax risk for a Bernoulli model; recommended reading before the chapter — difficulty: medium.
- Ex. VI.5 (p. 576) — Hellinger-based version of HCR that also implies CR — difficulty: medium.
- Ex. VI.4 (p. 580) — Chernoff–Rubin–Stein inequality for the uniform prior — difficulty: medium.
- Ex. VI.8 (p. 583) — MLE equals empirical distribution; $f$-divergence minimax rates — difficulty: medium.
- Ex. VI.15 (p. 583) — MLE failing to achieve the minimax rate in high dimension — difficulty: hard.

## Reading notes
- The unit is headed "29 Classical large-sample asymptotics" (printed p. 575); the unit id says ch32. Printed = pdf − 25.
- In the proof of Thm 29.1 (p. 576), $P_X=P_\theta$, $Q_X=P_{\theta'}$ is written with $\mathrm{Var}_\theta$ in the denominator, while the statement has $\chi^2(P_{\theta'}\|P_\theta)$. The argument order of $\chi^2$ seems reversed in the proof; the multivariate remark has the same order. This does not matter in the $\theta'\to\theta$ limit.
- In the proof of Thm 29.4, the printed $\pi_i(\theta_i)=\frac1\delta g(\frac{\theta-\theta_i}{\delta})$ mixes the symbols $\theta$ and $\theta_i$. I read it as a prior centred at the fixed $\theta$.
- The MLE risk is written with "≤" on p. 582, as printed.
- Text layer was usable; math was checked against the page images. For the $\max V\asymp\log^2k$ claim, the footnote (p. 584) cites the upper bound and only names a candidate distribution for the lower bound; no full proof is given.
