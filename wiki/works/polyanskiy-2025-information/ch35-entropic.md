---
id: polyanskiy-2025-information/ch35-entropic
work: polyanskiy-2025-information
unit: "Chapter 32. Entropic bounds for statistical estimation"
pages: 602-625
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# Entropic bounds for statistical estimation

## L0 — One line
For KL, squared Hellinger and squared total-variation loss, the minimax estimation risk is bounded, up to constants, by $\inf_{\epsilon>0}\{\epsilon^2+\frac1n\log N(\epsilon)\}$, where $N$ is the covering number of the model under the matching distance.

## L1 — The gist (≤ 120 words)
Can the minimax risk of estimating a distribution from n i.i.d. samples be bounded by the metric entropy of the model class? Yes, for three losses: KL (Yang–Barron, via the capacity of the channel from parameter to data), squared Hellinger (Le Cam–Birgé, via pairwise tests) and squared total variation (Yatracos, via minimum distance over a finite family of sets). All three bounds have the form $\inf_\epsilon\{\epsilon^2+\frac1n\log N(\epsilon)\}$, up to constants. For smooth densities on the unit cube this yields optimal rates for L2, TV and Hellinger loss, and a rate for KL with a logarithmic gap. The source notes that these entropic bounds are not attained by computationally efficient estimators (p. 624).

**Prerequisites:** KL divergence, mutual information and capacity, chain rule; Fano's inequality; covering and packing numbers (metric entropy); Hellinger and total-variation distance; convexity and Jensen's inequality.

## L2 — Key ideas
- Three upper bounds (KL, $H^2$, $\mathrm{TV}^2$) share one form with different metric entropies. Machine-learning density estimators are not known to be optimal over reasonable classes; metric-entropy methods can give fundamental limits for such classes (p. 602).
- Yang–Barron: $R^*_{\rm KL}(n)\le C_{n+1}/(n+1)$ and $\sum_{t=0}^n R^*_{\rm KL}(t)\ge C_{n+1}$, where $C_n$ is the capacity of the channel $\theta\mapsto X^n$. For a general channel, the capacity equals $\inf_\epsilon\{\epsilon^2+\log N_{\rm KL}(\epsilon)\}$ over KL covers of its family of output laws (Thm 32.4). For $C_n$ this gives $C_n\le\inf_\epsilon\{n\epsilon^2+\log N_{\rm KL}(\mathcal P,\epsilon)\}$ (pp. 603–604, 608–609).
- For a prior $\pi$, the Bayes KL risk is $I(\theta;X_{n+1}|X^n)$. This decreases in $n$, which turns a cumulative bound into a one-step bound (pp. 605–606).
- Capacity is bounded below by Hellinger packing numbers (Thm 32.5). With a finite Rényi radius (the smallest worst-case Rényi divergence from the model to one reference law) it is bounded above by Hellinger covering numbers (Thm 32.6). The source calls these tight up to log factors under mild conditions (pp. 609–610).
- Online-to-batch: $nR^*_n\le C_n\le\sum_t R^*_t$ for general losses. So $R^*_n\approx C_n/n$ within constant or polylog factors for most cases of interest (p. 611).
- Le Cam–Birgé: tests between convex Hellinger balls have error $e^{-\frac n2H^2}$. They give a proper estimator (one lying in the model class) with $H^2$ risk $\lesssim\epsilon_n^2$. Local entropy (covering numbers of small Hellinger balls by balls of half the radius) removes the log factor. This gives the rate $d/n$ when the doubling dimension (the $d$ with $\log N_{\rm loc}\le d\log\frac1\epsilon$) is at most $d$ (pp. 613–617).
- Under regularity (finite Rényi radius, large local packing number), a Fano argument gives a lower bound that matches the local-entropy upper bound up to logarithmic factors when $\log N_{\rm loc}\asymp\log M_{\rm loc}$, as in all instances known to the authors. If $H^2\asymp D$, the local-entropy rate is exact (pp. 618–620).
- Yatracos: replacing TV by a distance over finitely many sets $A_{ij}$ built from a TV-cover gives a proper minimum-distance estimator with $\mathrm{TV}^2$ risk $\lesssim\epsilon^2+\frac1n\log N$ (pp. 620–621).
- On Hölder densities, the L2 and TV rates are $n^{-2\beta/(2\beta+d)}$ and $n^{-\beta/(2\beta+d)}$, and the $H^2$ rate is $n^{-\beta/(\beta+d)}$. The KL rate is known up to a $(\log n)^{d/(\beta+d)}$ gap (pp. 622–625).

## L3 — Walkthrough

### Introduction (pp. 602–603)
Setting: observe $X_1,\dots,X_n$ i.i.d. from $P_\theta$, $\theta\in\Theta$; produce an estimate $\hat P$ of $P_\theta$. $N(\mathcal P,\epsilon)$ is the metric entropy (covering number: fewest balls of radius $\epsilon$ that cover the class) of $\mathcal P=\{P_\theta\}$ (p. 602). Claimed bounds (the symbol $\lesssim$ is not defined here; I read it as "up to a constant factor"):

$$\inf_{\hat P}\sup_\theta \mathbb E_\theta[D(P_\theta\|\hat P)]\lesssim\inf_{\epsilon>0}\Big\{\epsilon^2+\tfrac1n\log N_{\rm KL}(\mathcal P,\epsilon)\Big\}\tag{32.1}$$
$$\inf_{\hat P}\sup_\theta \mathbb E_\theta[H^2(P_\theta,\hat P)]\lesssim\inf_{\epsilon>0}\Big\{\epsilon^2+\tfrac1n\log N_{H}(\mathcal P,\epsilon)\Big\}\tag{32.2}$$
$$\inf_{\hat P}\sup_\theta \mathbb E_\theta[\mathrm{TV}^2(P_\theta\|\hat P)]\lesssim\inf_{\epsilon>0}\Big\{\epsilon^2+\tfrac1n\log N_{\rm TV}(\mathcal P,\epsilon)\Big\}\tag{32.3}$$

They are due to Yang–Barron, Le Cam–Birgé and Yatracos, obtained by completely different means (p. 602). They achieve minimax rates for density estimation under smoothness constraints. Machine-learning density estimators are not known to be optimal over any reasonable classes (p. 602). MLE and other M-estimators need bracketing entropy and are not covered (pp. 602–603).

### 32.1 Yang–Barron's construction (pp. 603–611)
Loss: $D(P_\theta\|\hat P)$, with $\hat P=\hat P(\cdot|X^n)$ a distribution. The loss is asymmetric. The reversed loss $D(\hat P\|P)$ is typically infinite in nonparametric settings (p. 603, fn. 1). Improper estimates (outside $\mathcal P$) are allowed. Minimax KL risk:
$$R^*_{\rm KL}(n)\triangleq\inf_{\hat P}\sup_\theta\mathbb E_\theta D(P_\theta\|\hat P).\tag{32.4}$$
For losses with an approximate triangle inequality, an improper estimate can be projected onto the model with risk inflated by at most a constant factor (p. 603, fn. 2).

**Theorem 32.1.** Let $C_n=\sup_\pi I(\theta;X^n)$ (32.5), the capacity of $\theta\mapsto X^n\sim P_\theta^{\otimes n}$. Let
$$N_{\rm KL}(\mathcal P,\epsilon)\triangleq\min\{N:\exists Q_1,\dots,Q_N\ \forall\theta\,\exists i:\ D(P_\theta\|Q_i)\le\epsilon^2\}\tag{32.6}$$
Then
$$R^*_{\rm KL}(n)\le\frac{C_{n+1}}{n+1}\tag{32.7}$$ $$\le\inf_{\epsilon>0}\Big\{\epsilon^2+\tfrac1{n+1}\log N_{\rm KL}(\mathcal P,\epsilon)\Big\}\tag{32.8}$$
and conversely $\sum_{t=0}^nR^*_{\rm KL}(t)\ge C_{n+1}$ (32.9) (pp. 603–604).

$C_n$ is the redundancy (13.10) governing minimax regret in universal compression. In general it is difficult to compute exactly, even for Bernoulli. Metric entropy gives usable bounds (p. 604).

*Finite-dimensional models* (p. 604). Take $\Theta\subset\mathbb R^d$ compact and $D(P_\theta\|P_{\theta'})\asymp\|\theta-\theta'\|^2$ (e.g. $\mathcal N(\theta,I_d)$, where $D=\frac12\|\theta-\theta'\|_2^2$). Then $N_{\rm KL}(\mathcal P,\epsilon)\lesssim(1/\epsilon)^d$ and
$$C_n\lesssim\inf_\epsilon\{n\epsilon^2+d\log\tfrac1\epsilon\}\asymp d\log n,\tag{32.10}$$
consistent with the typical $C_n=\frac d2\log n+o(\log n)$. Hence $R^*_{\rm KL}(n)\lesssim\frac{d\log n}{n}$, suboptimal only by a log factor against the parametric rate $d/n$.

*Infinite-dimensional models* (pp. 604–605). $N_{\rm KL}(\epsilon)$ typically grows super-polynomially in $1/\epsilon$, so $C_n$ grows super-logarithmically. Whenever $C_n=n^\alpha\mathrm{polylog}(n)$ with $\alpha>0$ (polylog between $(\log n)^{c_0}$ and $(\log n)^{c_1}$), Theorem 32.1 shows
$$R^*_{\rm KL}(n)=n^{\alpha-1}\mathrm{polylog}(n),\tag{32.11}$$
which follows from combining (32.7) and (32.8); the source points to (32.27) for details.

> **Intuition note.** The risk of predicting one new sample is at most the average information the data carry about $\theta$, per sample. Capacity can be bounded by how many KL-balls are needed to cover the model.

#### 32.1.1 Bayes risk as conditional mutual information and capacity bound (pp. 605–608)
Bayesian setting: $\theta\sim\pi$, $X^n$ i.i.d. $P_\theta$. An estimator is a conditional distribution $Q_{X_{n+1}|X^n}$ that predicts an unseen $X_{n+1}\sim P_\theta$, independent of $X^n$ given $\theta$ (p. 605).

**Lemma 32.2.** For a prior $\pi$, the Bayes risk is
$$R^*_{\rm KL,Bayes}(\pi)\triangleq\inf_{\hat P}\int\pi(d\theta)P_\theta^{\otimes n}(dx^n)D(P_\theta\|\hat P(\cdot|x^n))=I(\theta;X_{n+1}|X^n).$$
The minimizer is the predictive density estimator $\hat P_{\rm Bayes}(\cdot|x^n)=P_{X_{n+1}|X^n=x^n}$, with density
$$\hat p_{\rm Bayes}(x_{n+1}|x^n)=\frac{\int\pi(d\theta)\prod_{i=1}^{n+1}p_\theta(x_i)}{\int\pi(d\theta)\prod_{i=1}^{n}p_\theta(x_i)}.\tag{32.12}$$
*Proof* (p. 605–606):
$$\inf_Q\mathbb E_{\theta,X^n}D(P_\theta\|Q_{X_{n+1}|X^n})=\inf_Q D(P_{X_{n+1}|\theta}\|Q_{X_{n+1}|X^n}|P_{\theta,X^n})=\mathbb E_{X^n}\Big[\inf_Q D(P_{X_{n+1}|\theta}\|Q_{X_{n+1}|X^n}|P_{\theta|X^n})\Big]$$
$$\overset{(a)}=\mathbb E_{X^n}\big[D(P_{X_{n+1}|\theta}\|P_{X_{n+1}|X^n}|P_{\theta|X^n})\big]=D(P_{X_{n+1}|\theta}\|P_{X_{n+1}|X^n}|P_{\theta,X^n})\overset{(b)}=I(\theta;X_{n+1}|X^n).$$
(a) is the variational representation of mutual information (Thm 4.1, Cor 4.2). (b) is the definition of conditional mutual information, using the Markov chain $X^n\to\theta\to X_{n+1}$, so $P_{X_{n+1}|\theta,X^n}=P_{X_{n+1}|\theta}$.

The quantity $I(\theta;X_{n+1}|X^n)$ is the information one extra observation gives about $\theta$ after $n$ observations (p. 606).

**Lemma 32.3 (diminishing marginal utility).** $n\mapsto I(\theta;X_{n+1}|X^n)$ is decreasing, and
$$I(\theta;X_{n+1}|X^n)\le\tfrac1{n+1}I(\theta;X^{n+1}).\tag{32.13}$$
*Proof* (p. 606). By the chain rule $I(\theta;X^{n+1})=\sum_{i=1}^{n+1}I(\theta;X_i|X^{i-1})$, so (32.13) follows from monotonicity. For monotonicity, use the sampling channel $\theta\to X\sim P_\theta$. Write $I(\pi)$ for its mutual information under input law $\pi$; $I(\pi)$ is concave in $\pi$ (Thm 5.3). Then
$$I(\theta;X_{n+1}|X^n)=\mathbb E_{X^n}[I(P_{\theta|X^n})]\le\mathbb E_{X^{n-1}}[I(P_{\theta|X^{n-1}})]=I(\theta;X_n|X^{n-1}),$$
by Jensen, since $P_{\theta|X^{n-1}}$ is a mixture of $P_{\theta|X^n}$.

*Converse (32.9)* (p. 606). Fix a prior $\pi$. Minimax risk dominates Bayes risk (Thm 28.1), so by Lemma 32.2 $\sum_{t=0}^nR^*_{\rm KL}(t)\ge\sum_{t=0}^nI(\theta;X_{t+1}|X^t)=I(\theta;X^{n+1})$. Optimizing over $\pi$ gives $C_{n+1}$.

*Upper bound via the minimax theorem* (p. 606). If the minimax theorem holds for (32.4), $R^*_{\rm KL}(n)=\sup_\pi I(\theta;X_{n+1}|X^n)$, so Lemma 32.3 gives (32.7).

*Direct proof without the minimax theorem* (pp. 606–607), after Yang–Barron: use Bayes-type estimators but analyse them in the worst case. Fix an arbitrary joint law $Q_{X^{n+1}}=\prod_{i=1}^{n+1}Q_{X_i|X^{i-1}}$, an auxiliary object only (see Reading notes on the printed index range and input size). Each conditional $Q_{X_i|X^{i-1}}$ is an estimator. Their Cesàro mean on the full sample is
$$\hat P(\cdot|X^n)\triangleq\frac1{n+1}\sum_{i=1}^{n+1}Q_{X_i|X^{i-1}}.\tag{32.14}$$
Fix $\theta$, with $X^{n+1}\sim P_\theta^{\otimes(n+1)}$. Then
$$\mathbb E_\theta D(P_\theta\|\hat P(\cdot|X^n))\overset{(a)}\le\frac1{n+1}\sum_{i=1}^{n+1}D(P_\theta\|Q_{X_i|X^{i-1}}|P_{X^{i-1}})\overset{(b)}=\frac1{n+1}D(P_\theta^{\otimes(n+1)}\|Q_{X^{n+1}}).$$
(a) is convexity of KL (Thm 5.1). (b) is the chain rule for KL (Thm 2.16(c)). Taking sup over $\theta$ and optimizing $Q$:
$$R^*_{\rm KL}(n)\le\frac1{n+1}\inf_{Q_{X^{n+1}}}\sup_\theta D(P_\theta^{\otimes(n+1)}\|Q_{X^{n+1}})=\frac{C_{n+1}}{n+1}.$$
The last identity is Kemperman's Theorem 5.9, which also says the optimal $Q_{X^{n+1}}$ exists and is uniquely the capacity-achieving output distribution $P^*_{X^{n+1}}$. So the bound is attained by
$$\hat P^*(\cdot|X^n)=\frac1{n+1}\sum_{i=1}^{n+1}P^*_{X_i|X^{i-1}},\tag{32.15}$$
which is in general improper. If a capacity-achieving input $\pi^*$ exists, $P^*_{X^{n+1}}=\int\pi^*(d\theta)P_\theta^{\otimes(n+1)}$, and $\hat P^*$ is the average of the Bayes estimators (32.12) under $\pi^*$ for sample sizes $0,\dots,n$ (p. 607).

*Route to (32.8)* (pp. 607–608). It suffices to take an $\epsilon$-KL cover $Q_1,\dots,Q_N$, $N=N_{\rm KL}(\mathcal P,\epsilon)$, a uniform prior, and $Q_{X^{n+1}}=\frac1N\sum_jQ_j^{\otimes(n+1)}$ (original construction of [464]). The estimator is then a convex combination $\hat P=\sum_jw_jQ_j$ with data-driven weights
$$w_j=\frac1{n+1}\sum_{i=1}^{n+1}\frac{\prod_{t=1}^{i-1}Q_j(X_t)}{\sum_{j'=1}^N\prod_{t=1}^{i-1}Q_{j'}(X_t)}.$$
It is improper except in the extraordinary case that $\mathcal P$ is convex and the centers lie in $\mathcal P$.

#### 32.1.2 Capacity upper bound via KL covering numbers (pp. 608–609)
**Theorem 32.4.** Let $\mathcal Q=\{P_{B|A=a}:a\in\mathcal A\}$ and $C=\sup_{P_A}I(A;B)$. Then
$$C=\inf_{\epsilon>0}\{\epsilon^2+\log N_{\rm KL}(\mathcal Q,\epsilon)\}.\tag{32.16}$$
*Proof.* Upper bound: take an $\epsilon$-KL cover $Q_1,\dots,Q_N$ with $i(a)$ such that $D(P_{B|A=a}\|Q_{i(a)})\le\epsilon^2$. For any $P_A$:
$$I(A;B)=I(A,i(A);B)=I(i(A);B)+I(A;B|i(A))\le H(i(A))+I(A;B|i(A))\le\log N+\epsilon^2.$$
The last step holds because $i(A)$ takes at most $N$ values and, by Thm 4.1, $I(A;B|i(A))$ is at most the average divergence of $P_{B|A}$ from $Q_{i(A)}$, which is $\le\epsilon^2$.
Lower bound: if $C=\infty$, the upper bound forces $N_{\rm KL}(\mathcal Q,\epsilon)=\infty$ for every $\epsilon$, so equality holds. If $C<\infty$, Thm 5.9 says $C$ is the KL radius of $\mathcal Q$: some $P^*_B$ has $D(P_{B|A=a}\|P_B^*)\le C$ for all $a$. So $N_{\rm KL}(\mathcal Q,\sqrt{C+\delta})=1$ for any $\delta>0$. (added step: then $\inf_\epsilon\{\epsilon^2+\log N_{\rm KL}\}\le C+\delta$; let $\delta\to0$.)

*Specialization* (p. 608–609). Take $A=\theta$, $B=X^n$, $\mathcal P_n=\{P_\theta^{\otimes n}\}$. Tensorization gives $D(P_\theta^{\otimes n}\|P_{\theta'}^{\otimes n})=nD(P_\theta\|P_{\theta'})$ (Thm 2.16(d)), so $N_{\rm KL}(\mathcal P_n,\epsilon)\le N_{\rm KL}(\mathcal P,\epsilon/\sqrt n)$. Hence
$$C_n\le\inf_{\epsilon>0}\{n\epsilon^2+\log N_{\rm KL}(\mathcal P,\epsilon)\}.\tag{32.17}$$
(added step: substitute $\epsilon\to\epsilon/\sqrt n$ in (32.16).) With $n+1$ in place of $n$ and division by $n+1$, this proves (32.8) and Theorem 32.1 (p. 609).

> **Intuition note.** The capacity is the best trade-off between two costs. One is the $\epsilon^2$ of describing each parameter by its nearest center. The other is the $\log N$ bits needed to say which center.

#### 32.1.3 Bounding capacity and KL covering number using Hellinger entropy (pp. 609–610)
KL covering numbers are inconvenient because KL is not a metric, so Chapter 27 tools do not apply. The source gives bounds via Hellinger entropy, tight up to logarithmic factors under mild conditions (p. 609).

**Theorem 32.5.** Let $M_H(\epsilon)$ be the Hellinger packing number of $\mathcal P$ (cf. (27.2)). Then
$$C_n\ge\min\Big(\tfrac{\log e}2n\epsilon^2,\ \log M_H(\epsilon)\Big)-\log2.\tag{32.18}$$
*Proof idea* (p. 609): take a packing $\theta_1,\dots,\theta_M$ with $H^2(Q_i,Q_j)\ge\epsilon^2$, $Q_i\equiv P_{\theta_i}$. Pairwise tests have error $e^{-n\epsilon^2/2}$ (Thm 7.8, Thm 32.8). If $Me^{-n\epsilon^2/2}<\frac12$, the union bound distinguishes all $M$ hypotheses with error $<\frac12$, and Fano gives $I(\theta;X^n)\gtrsim\log M$.
*Sharper constants* (pp. 609–610), via Ex. I.58 with $\lambda=\frac12$: for $i\ne j$,
$$D_{1/2}(Q_i,Q_j)=-2\log(1-\tfrac12H^2(Q_i,Q_j))\ge H^2(Q_i,Q_j)\log e\ge\epsilon^2\log e.$$
By tensorization of Rényi divergence (7.79), $D_{1/2}(Q_i^{\otimes n},Q_j^{\otimes n})=nD_{1/2}(Q_i,Q_j)$. Ex. I.58 then gives, with $\theta\sim\mathrm{Unif}(\theta_1,\dots,\theta_M)$:
$$I(\theta;X^n)\ge-\sum_{i=1}^M\frac1M\log\Big(\sum_{j=1}^M\frac1M\exp\{-\tfrac n2D_{1/2}(Q_i,Q_j)\}\Big)\overset{(a)}\ge-\sum_i\frac1M\log\Big(\frac{M-1}Me^{-\frac{n\epsilon^2}2}+\frac1M\Big)\ge-\log\Big(e^{-\frac{n\epsilon^2}2}+\frac1M\Big).$$
In (a), all pairwise terms are $\ge n\epsilon^2$ except $i=j$. Since $\frac1A+\frac1B\le\frac2{\min(A,B)}$, the result follows (added step: take $A=e^{n\epsilon^2/2}$, $B=M$).

From $D\ge H^2$ (7.33), a different (weaker) lower bound on the KL risk also follows from Section 32.2.4 (p. 610).

*Converse direction* (p. 610). Always $N_{\rm KL}(\mathcal P,\epsilon)\ge N_H(\epsilon)$ (32.19). If $\mathcal P$ has a finite Rényi radius, (32.19) and the capacity bound of Theorem 32.5 are tight up to logarithmic factors. Smooth densities have a finite $\chi^2$-radius (center: the uniform distribution); this is used in §32.4.

**Theorem 32.6.** Suppose $R_\lambda(\mathcal P)\triangleq\inf_U\sup_{P\in\mathcal P}D_\lambda(P\|U)<\infty$ for some $\lambda>1$ (32.20); here $D_\lambda$ is the Rényi divergence of order $\lambda$ (Def. 7.24, not reproduced in this unit). Then there exist $\epsilon_0,c$, depending only on $\lambda$ and $R_\lambda$, such that for all $\epsilon\le\epsilon_0$
$$N_{\rm KL}\Big(\mathcal P,c\epsilon\sqrt{\log\tfrac1\epsilon}\Big)\le N_H(\epsilon)\tag{32.21}$$
and consequently
$$C_n\le\inf_{\epsilon\le\epsilon_0}\Big\{cn\epsilon^2\log\tfrac1\epsilon+\log N_H(\epsilon)\Big\}.\tag{32.22}$$
*Proof.* Take an $\epsilon$-Hellinger cover $Q_1,\dots,Q_M$. Fix $U$ and set $P_i=\epsilon^2U+(1-\epsilon^2)Q_i$. Ex. I.59 gives
$$D(P\|P_i)\le24\epsilon^2\Big(\tfrac{2\lambda}{\lambda-1}\log\tfrac1\epsilon+D_\lambda(P\|U)\Big).$$
Optimizing $U$ toward (32.20) gives (32.21); (32.22) follows by applying (32.21) to (32.17).

#### 32.1.4 Cumulative versus individual risks (pp. 610–612)
The Yang–Barron method has two ideas: relate the one-step risk $R^*_{\rm KL}(n)$ to a cumulative risk $C_n$, and note that this cumulative risk equals a capacity, which is bounded via covering numbers. The second is special to KL (log-loss); the first is generic (p. 611).

**Proposition 32.7 (online-to-batch).** For a loss $\ell$ and class $\Pi$, define (for KL loss $C_n$ and $R_n^*$ coincide with AvgReg$^*_n$ and BatchReg$^*_n$ of (13.34), (13.35); p. 611, fn. 4)
$$C_n=\inf_{\{\hat P_t\}}\sup_{P\in\Pi}\mathbb E\Big[\sum_{t=1}^n\ell(P,\hat P_t(X^{t-1}))\Big],\tag{32.23}$$
$$R^*_n=\inf_{\hat P}\sup_{P\in\Pi}\mathbb E\big[\ell(P,\hat P(X^{n-1}))\big],\tag{32.24}$$
over measurable, possibly randomized, estimators, with $X_i$ i.i.d. $P$. Then
$$nR^*_n\le C_n\le C_{n-1}+R^*_n\le\sum_{t=1}^nR^*_t.\tag{32.25}$$
So if $R^*_n\asymp\frac1n\sum_{t=0}^{n-1}R^*_t$, then $C_n\asymp nR^*_n$. Conversely, if $n^{\alpha_-}\lesssim C_n\lesssim n^{\alpha_+}$ for all $n$ and some $\alpha_+\ge\alpha_->0$, then
$$n^{(\alpha_--1)\frac{\alpha_+}{\alpha_-}}\lesssim R^*_n\lesssim n^{\alpha_+-1}.\tag{32.26}$$
Remark 32.1: $R^*_n\approx\frac1nC_n$ within constant or polylogarithmic factors, for most cases of interest (p. 611).

*Proof* (pp. 611–612). First inequality: from predictors $\{\hat P_t\}$ for $C_n$, build a randomized predictor for $R_n^*$ that equals each $\hat P_t(X^{t-1})$ with equal probability. Second: interchange $\sup_P$ and $\sum_t$:
$$\sup_P\mathbb E\sum_{t=1}^n\ell(P,\hat P_t)\le\sup_P\mathbb E\sum_{t=1}^{n-1}\ell(P,\hat P_t)+\sup_P\mathbb E\,\ell(P,\hat P_n(X^{n-1})).$$
That is, use the $C_{n-1}$-optimal online learner for the first $n-1$ rounds and the $R_n^*$-optimal batch learner for the last. Third: induction and $C_1=R_1^*$. For (32.26): the upper bound follows from (32.25). For the lower bound, $R^*_n$ is non-increasing, so for $n<m$
$$C_m\le\sum_{t=0}^{m-1}R^*_t\le\sum_{t=0}^{n-1}\frac{C_t}t+(m-n)R^*_n.\tag{32.27}$$
Setting $m=an^{\alpha_+/\alpha_-}$ with a suitable constant $a$ yields the lower bound.

> **Intuition note.** Summing the one-step errors of a learner that predicts sample after sample gives a cumulative error. Because one-step error cannot rise with more data, the cumulative error sits between $n$ times the last one-step error and the sum of all one-step errors.

### 32.2 Pairwise comparison à la Le Cam–Birgé (pp. 612–620)
Question: can tests yield an estimator and a minimax upper bound in terms of metric entropy? For Hellinger loss, yes, with Hellinger (not KL) entropy. Idea: fix an $\epsilon$-cover $\{P_1,\dots,P_N\}$; test which ball $P$ belongs to, via composite tests $P\in B(P_i,\epsilon)$ vs $P\in B(P_j,\epsilon)$ (p. 612).

#### 32.2.1 Composite hypothesis testing and Hellinger distance (pp. 612–613)
For classes $\mathcal P,\mathcal Q$ (not necessarily convex) and a test $\phi\in\{0,1\}$, the minimax theorem gives
$$\min_\phi\Big\{\sup_{P\in\mathcal P}P(\phi=1)+\sup_{Q\in\mathcal Q}Q(\phi=0)\Big\}=1-\mathrm{TV}(\mathrm{co}(\mathcal P^{\otimes n}),\mathrm{co}(\mathcal Q^{\otimes n})),\tag{32.28}$$
where $\mathcal P^{\otimes n}=\{P^{\otimes n}\}$ and co is the convex hull (all mixtures). The optimal test is the likelihood ratio of the closest pair of worst-case mixtures (if it does not exist, use an infimizing sequence). This is unwieldy. For TV-balls around $P_0,Q_0$, Huber showed the optimal test is $\phi=\mathbb 1\{\sum_i\min(c',\max(c'',\log\frac{dP_0}{dQ_0}(X_i)))>t\}$. Few other explicit cases are known (p. 613).

**Theorem 32.8 (Le Cam).**
$$\min_\phi\Big\{\sup_{P\in\mathcal P}P(\phi=1)+\sup_{Q\in\mathcal Q}Q(\phi=0)\Big\}\le e^{-\frac n2H^2(\mathrm{co}(\mathcal P),\mathrm{co}(\mathcal Q))}.\tag{32.29}$$
*Proof* (p. 613). The special case of Prop. 7.25 reads $1-\frac12H^2(\mathrm{co}(\bigotimes_iP_i),\mathrm{co}(\bigotimes_iQ_i))\le\prod_i(1-\frac12H^2(\mathrm{co}(P_i),\mathrm{co}(Q_i)))$ (32.30). Then from (32.28):
$$1-\mathrm{TV}(\mathrm{co}(\mathcal P^{\otimes n}),\mathrm{co}(\mathcal Q^{\otimes n}))\overset{(a)}\le1-\tfrac12H^2(\mathrm{co}(\mathcal P^{\otimes n}),\mathrm{co}(\mathcal Q^{\otimes n}))\overset{(b)}\le\big(1-\tfrac12H^2(\mathrm{co}(\mathcal P),\mathrm{co}(\mathcal Q))\big)^n\le e^{-\frac n2H^2(\mathrm{co}(\mathcal P),\mathrm{co}(\mathcal Q))}.$$
(a) is (7.22); (b) is (32.30). The last step is $1-x\le e^{-x}$ (added step).

Remark 32.2: for Hellinger balls of radius $r$ around $P_0,Q_0$ with $H(P_0,Q_0)>2.01r$, Birgé built an explicit test $\phi=\mathbb 1\{\sum_i\log\frac{\alpha+\beta\psi(X_i)}{\beta+\alpha\psi(X_i)}>t\}$ with error $e^{-\Omega(nr^2)}$, where $\psi=\sqrt{dP_0/dQ_0}$ and $\alpha,\beta>0$ depend only on $H(P_0,Q_0)$ (p. 613).
Remark 32.3: Theorem 32.8 can be very loose. For $\mathcal P=\{\mathrm{Ber}(1/2)\}$ and $\mathcal Q=\{\mathrm{Ber}(0),\mathrm{Ber}(1)\}$, $\mathrm{co}(\mathcal P)\subset\mathrm{co}(\mathcal Q)$, so the bound is trivial. Yet a test that declares $\mathcal Q$ when all samples are equal (see Reading notes) has exponentially small error (p. 613).

#### 32.2.2 Hellinger guarantee for the pairwise comparison estimator (pp. 614–615)
Loss $\ell(P,\hat P)=H^2(P,\hat P)$; $\mathcal P$ need not be convex (p. 614).

**Theorem 32.9 (Le Cam–Birgé).** Let $\epsilon_n$ satisfy $n\epsilon_n^2\ge\log N_H(\mathcal P,\epsilon_n)\vee1$. Then there is an estimator $\hat P=\hat P(X_1,\dots,X_n)\in\mathcal P$ (proper) with, for any $t\ge1$,
$$\sup_{P\in\mathcal P}\mathbb P[H(P,\hat P)>4t\epsilon_n]\lesssim e^{-t^2}\tag{32.31}$$
and consequently
$$\sup_{P\in\mathcal P}\mathbb E_P[H^2(P,\hat P)]\lesssim\epsilon_n^2.\tag{32.32}$$
*Proof* (pp. 614–615). It suffices to prove (32.31). Let $\epsilon=\epsilon_n$, $N=N_H(\mathcal P,\epsilon_n)$. Take a maximal $\epsilon$-packing $P_1,\dots,P_N$, which is also an $\epsilon$-cover (Thm 27.2): $H(P_i,P_j)\ge\epsilon$ for $i\ne j$, and every $P$ has some $H(P,P_i)\le\epsilon$. Hellinger balls $B(P,\epsilon)=\{Q:H(P,Q)\le\epsilon\}$ are convex, because $H^2$ is convex as an f-divergence (Thm 7.5), whereas $H$ itself is not (7.6): $H^2(\bar\alpha P'+\alpha P'',P)\le\bar\alpha H^2(P',P)+\alpha H^2(P'',P)\le\epsilon^2$.
Test $H_i:P\in B(P_i,\epsilon)$ vs $H_j:P\in B(P_j,\epsilon)$ for $H(P_i,P_j)\ge\delta=4\epsilon$. Both balls are convex, so Theorem 32.8 gives tests $\psi_{ij}$ with $\psi_{ij}=1-\psi_{ji}$ and
$$\sup_{P\in B(P_i,\epsilon)}\mathbb P(\psi_{ij}=1)\le e^{-\frac n8H(P_i,P_j)^2}.\tag{32.33}$$
This uses the triangle inequality: for $P\in B(P_i,\epsilon)$, $Q\in B(P_j,\epsilon)$, $H(P,Q)\ge H(P_i,P_j)-2\epsilon\ge H(P_i,P_j)/2\ge2\epsilon$. (added step: $\frac n2(H(P_i,P_j)/2)^2=\frac n8H(P_i,P_j)^2$.)
Define $T_i\triangleq\max_{j}H^2(P_i,P_j)$ over $j$ with $\psi_{ij}=1$ and $H(P_i,P_j)>\delta$ (and $0$ if no such $j$). The estimator is
$$\hat P=P_{i^*},\quad i^*\in\arg\min_{i\in[N]}T_i.\tag{32.34}$$
(As printed $T_i$ uses $H^2$ but is then used as a distance; see Reading notes.) Assume $P\in B(P_1,\epsilon)$. Typically $T_1=0$ and $T_j\ge\delta^2$ for all $j$ with $H(P_1,P_j)\ge\delta$. For any pair with $H(P_i,P_j)\ge\delta$, $\max\{T_i,T_j\}\ge H(P_i,P_j)$. Hence
$$H(\hat P,P_1)\mathbb 1\{H(\hat P,P_1)\ge\delta\}\le\max\{T_{i^*},T_1\}\mathbb 1\{\max\{T_{i^*},T_1\}\ge\delta\}=T_1\mathbb 1\{T_1\ge\delta\},$$
the last equality because $i^*$ is a global minimizer. So for $t\ge1$:
$$\mathbb P[H(\hat P,P_1)\ge t\delta]\le\mathbb P[T_1\ge t\delta]\le N(\epsilon)e^{-2n\epsilon^2t^2}\lesssim e^{-t^2}.\tag{32.35, 32.36}$$
(32.35) follows from (32.33); (32.36) uses $n\epsilon^2\ge1$ and $N\le e^{n\epsilon^2}$.

> **Intuition note.** Pick the cover center that no other far-away center can beat in a pairwise test. Because tests between balls are cheap ($e^{-nH^2/8}$) and there are only $N\le e^{n\epsilon^2}$ centers, a union bound shows the true ball wins.

#### 32.2.3 Refinement using local entropy (pp. 616–618)
For $d$-dimensional parametric families $\log N_H(\epsilon)\asymp d\log\frac1\epsilon$. For $n\gtrsim d$, Theorem 32.9 gives $\epsilon_n^2\asymp\frac dn\log\frac nd$, short of the parametric rate $d/n$. Local Hellinger entropy fixes this:
$$N_{\rm loc}(\mathcal P,\epsilon)\triangleq\sup_{P\in\mathcal P}\sup_{\eta\ge\epsilon}N_H(B(P,\eta)\cap\mathcal P,\eta/2).\tag{32.37}$$
**Theorem 32.10.** If $n\epsilon_n^2\ge\log N_{\rm loc}(\mathcal P,\epsilon_n)\vee1$ (32.38), there is a proper estimator with, for $t\ge2$, $\sup_P\mathbb P[H(P,\hat P)>4t\epsilon_n]\le e^{-t^2}$ (32.39), hence $\sup_P\mathbb E_P[H^2(P,\hat P)]\lesssim\epsilon_n^2$ (32.40).

Remark 32.4 (doubling dimension): if $\log N_{\rm loc}(\mathcal P,\epsilon)\le d\log\frac1\epsilon$ for all sufficiently small $\epsilon$ (true for finite-dimensional models with Hellinger comparable to a norm, by the volume argument, Thm 27.3), the doubling dimension (Le Cam dimension) of $\mathcal P$ is at most $d$. The name reflects covering balls by balls of half the radius. Theorem 32.10 then gives the parametric rate $O(d/n)$, so doubling dimension acts as the effective dimension (p. 616).

**Lemma 32.11.** For $P\in\mathcal P$, $\eta\ge\epsilon$, $k\in\mathbb Z_+$: $N_H(B(P,2^k\eta)\cap\mathcal P,\eta/2)\le N_{\rm loc}(\mathcal P,\epsilon)^k$ (32.41). *Proof:* induction on $k$; the base case is claimed to follow from (32.37). For the step, cover $B(P,2^k\eta)\cap\mathcal P$ by $2^{k-1}\eta$-balls, then each by $\eta/2$-balls; the count is at most $N_H(B(P,2^k\eta)\cap\mathcal P,2^{k-1}\eta)\cdot\sup_{P'}N_H(B(P',2^{k-1}\eta)\cap\mathcal P,\eta/2)\le N_{\rm loc}\cdot N_{\rm loc}^{k-1}$ (p. 616).

*Proof of Theorem 32.10* (p. 617). Use the same estimator (32.34) and improve (32.35). Let $A_k=\{P:2^k\delta\le H(P_1,P)<2^{k+1}\delta\}$, $G_k=\{P_1,\dots,P_N\}\cap A_k$, $\delta=4\epsilon$. For $t\ge2$ let $\ell=\lfloor\log_2t\rfloor$, so $2^\ell\le t<2^{\ell+1}$:
$$\mathbb P[T_1\ge t\delta]\le\sum_{k\ge\ell}\mathbb P[2^k\delta\le T_1<2^{k+1}\delta]\overset{(a)}\le\sum_{k\ge\ell}|G_k|e^{-\frac n8(2^k\delta)^2}\overset{(b)}\le\sum_{k\ge\ell}N_{\rm loc}(\epsilon)^{k+3}e^{-2n\epsilon^24^k}\overset{(c)}\lesssim e^{-4^\ell}\le e^{-t^2}.$$
(a) uses (32.33); (c) uses $\log N_{\rm loc}\le n\epsilon^2$ and $k\ge\ell\ge\log_2t\ge1$. (b): as $\{P_i\}$ is an $\epsilon$-packing, $|G_k|\le M(A_k,\epsilon)\le N(A_k,\epsilon/2)\le N(B(P_1,2^{k+1}\delta)\cap\mathcal P,\epsilon/2)\le N_{\rm loc}(\epsilon)^{k+3}$, by Thm 27.2 and Lemma 32.11.

**Corollary 32.12.** Let $\Theta\subset\mathbb R^d$, with $\mathcal P$ totally bounded in Hellinger distance. Suppose a norm and constants $t_0,c,C$ satisfy, for $\|\theta_0-\theta_1\|\le t_0$,
$$c\|\theta_0-\theta_1\|\le H(P_{\theta_0},P_{\theta_1})\le C\|\theta_0-\theta_1\|.\tag{32.42}$$
Then some estimator $\hat\theta$ has $\sup_\theta\mathbb E_\theta H^2(P_\theta,P_{\hat\theta})\lesssim d/n$.
*Proof* (pp. 617–618): bound $N_{\rm loc}$. For $\eta>t_0$, $N_H(B(P_{\theta_0},\eta)\cap\mathcal P,\eta/2)\le N_H(\mathcal P,t_0)\lesssim1$. For $\epsilon\le\eta\le t_0$,
$$N_H(B(P_{\theta_0},\eta)\cap\mathcal P,\eta/2)\overset{(a)}\le N_{\|\cdot\|}(B_{\|\cdot\|}(\theta_0,\eta/c),\tfrac\eta{2C})\overset{(b)}\le\frac{\mathrm{vol}(B_{\|\cdot\|}(\theta_0,\eta/c+\eta/(2C)))}{\mathrm{vol}(B_{\|\cdot\|}(\theta_0,\eta/(2C)))}=\Big(1+\frac{2C}c\Big)^d.$$
(a) uses (32.42); (b) uses Thm 27.3. So $\log N_{\rm loc}\lesssim d$; apply Theorem 32.10.

> **Intuition note.** Counting only the balls needed to cover small neighbourhoods, instead of the whole class, removes the extra $\log(n/d)$. In a locally norm-like model that local count is a constant to the power $d$.

#### 32.2.4 Lower bound using local Hellinger packing (pp. 618–620)
Local packing number: $M_{\rm loc}(\epsilon)=\max\{M:\exists R,P_1,\dots,P_M\in\mathcal P:H(P_i,R)\le\epsilon,\ H(P_i,P_j)\ge\epsilon/2\ \forall i\ne j\}$.
**Lemma 32.13** (any metric): $\frac{M(\epsilon/2)}{M(\epsilon)}\le M_{\rm loc}(\epsilon)\le M(\epsilon)$. *Proof:* the upper bound is obvious. Take a maximal $\epsilon$-packing $P_1,\dots,P_M$ ($M=M(\epsilon)$) and a maximal $\epsilon/2$-packing $Q_1,\dots,Q_{M'}$ ($M'=M(\epsilon/2)$). Partition $E=\{P_j\}$ into Voronoi cells $E_i$ around the $Q_i$. Then $\max|E_i|\ge M/M'$, and each $E_i\subset B(Q_i,\epsilon)$ since $E$ is also an $\epsilon$-cover (p. 618). Local and global packing numbers behave similarly when growth is super-polynomial in $1/\epsilon$. Since $M_{\rm loc}$ has no sup over scale $\eta\ge\epsilon$, one cannot generally conclude $N_{\rm loc}\ge M_{\rm loc}$. In all instances known to the authors $\log N_{\rm loc}\asymp\log M_{\rm loc}$ (p. 618).

**Theorem 32.14.** Suppose $R_\lambda(\mathcal P)<\infty$ for some $\lambda>1$. There are $c=c(\lambda)$ and $\epsilon_0(\lambda)$ such that if $\epsilon<\epsilon_0$ and
$$c(\lambda)n\epsilon^2\Big(\log\tfrac1{\epsilon^2}+R_\lambda(\mathcal P)\Big)+2\log2<\log M_{\rm loc}(\epsilon),\tag{32.43}$$
then any estimator has $\sup_P\mathbb E_P[H^2(P,\hat P)]\ge\epsilon^2/32$.
*Proof* (p. 619). Take an $\epsilon/2$-packing $P_1,\dots,P_M$ inside a Hellinger ball $B(R,\epsilon)$, $M=M_{\rm loc}$; let $\theta\sim\mathrm{Unif}([M])$. Fano (Thm 31.3) gives
$$\sup_P\mathbb E[H^2(P,\hat P)]\ge\Big(\frac\epsilon4\Big)^2\Big(1-\frac{I(\theta;X^n)+\log2}{\log M}\Big).$$
It remains to show $\frac{I(\theta;X^n)+\log2}{\log M}\le\frac12$ (32.44). For arbitrary $U$ let $Q=\epsilon^2U+(1-\epsilon^2)R$. Ex. I.59 gives, for $\epsilon<2^{-\frac{5\lambda}{2(\lambda-1)}}\triangleq\epsilon_0$,
$$D(P_i\|Q)\le8(H^2(P_i,R)+2\epsilon^2)\Big(\tfrac\lambda{\lambda-1}\log\tfrac1{\epsilon^2}+D_\lambda(P_i\|U)\Big).$$
With $H^2(P_i,R)\le\epsilon^2$ and $U$ the $D_\lambda$-center, $\inf_U\max_iD(P_i\|Q)\le24\epsilon^2(\frac\lambda{\lambda-1}\log\frac1{\epsilon^2}+R_\lambda)\le\frac{c(\lambda)}2\epsilon^2(\log\frac1{\epsilon^2}+R_\lambda)$. By Thm 4.1, $I(\theta;X^n)\le\max_iD(P_i^{\otimes n}\|Q^{\otimes n})\le\frac{nc(\lambda)}2\epsilon^2(\log\frac1{\epsilon^2}+R_\lambda)$. With (32.43) this gives (32.44). (added step: (32.43) makes this $I<\frac12\log M-\log 2$.)

**Corollary 32.15.** If $H^2(P,P')\asymp D(P\|P')$ for all $P,P'\in\mathcal P$, then $\inf_{\hat P}\sup_P\mathbb E_P[H^2(P,\hat P)]\asymp\epsilon_n^2$, with $\epsilon_n$ from (32.38). *Proof:* KL neighbourhoods coincide with Hellinger balls up to constants, so the lower bound follows from Fano (Thm 31.3) applied to a Hellinger ball of radius $O(\epsilon_n)$ (p. 620). Such models include GLM and Gaussian mixtures with bounded centers in arbitrary dimensions [232] (p. 619).

### 32.3 Yatracos' class and minimum distance estimator (pp. 620–622)
**Theorem 32.16 (Yatracos).** There is a universal constant $C$ such that for $X_i$ i.i.d. $P\in\mathcal P$ and any $\epsilon>0$ there exists a proper estimator $\hat P\in\mathcal P$ with
$$\sup_{P\in\mathcal P}\mathbb E_P[\mathrm{TV}(\hat P,P)^2]\le C\Big(\epsilon^2+\tfrac1n\log N(\mathcal P,\mathrm{TV},\epsilon)\Big).\tag{32.45}$$
*Idea* (p. 620). Projecting the empirical distribution $\hat P_n=\frac1n\sum\delta_{X_i}$ onto $\mathcal P$ in TV is degenerate when $\mathcal P$ has densities, because $\hat P_n$ is discrete and TV is too strong. Replace TV by a proxy inspecting only a finite family $\mathcal A\subset\mathcal E$ of sets:
$$\mathrm{dist}(P,Q)\triangleq\sup_{A\in\mathcal A}|P(A)-Q(A)|\tag{32.46}$$
($\mathcal A=\mathcal E$ gives TV). It satisfies the triangle inequality. The minimizer
$$\tilde P\triangleq\arg\min_{P\in\mathcal P}\mathrm{dist}(P,\hat P_n)\tag{32.47}$$
satisfies
$$\mathrm{dist}(\tilde P,P)\le\mathrm{dist}(\tilde P,\hat P_n)+\mathrm{dist}(P,\hat P_n)\le2\,\mathrm{dist}(P,\hat P_n).\tag{32.48}$$
The binomial tail bound and a union bound give, for an absolute constant $C_0$ (p. 621),
$$\mathbb E[\mathrm{dist}(P,\hat P_n)^2]\le\frac{C_0\log|\mathcal A|}n.\tag{32.49}$$
*Choice of $\mathcal A$* (p. 621). Take a TV $\epsilon$-cover $\{Q_1,\dots,Q_N\}$ of $\mathcal P$ and
$$A_{ij}\triangleq\Big\{x:\frac{dQ_i}{d(Q_i+Q_j)}(x)\ge\frac{dQ_j}{d(Q_i+Q_j)}(x)\Big\},\qquad\mathcal A\triangleq\{A_{ij}:i\ne j\in[N]\}\ \text{(Yatracos class)}.\tag{32.50}$$
Then
$$\mathrm{dist}(P,Q)\le\mathrm{TV}(P,Q)\le\mathrm{dist}(P,Q)+4\epsilon,\quad\forall P,Q\in\mathcal P.\tag{32.51}$$
Only the upper bound needs proof. Pick $i,j$ with $\mathrm{TV}(P,Q_i)\le\epsilon$, $\mathrm{TV}(Q,Q_j)\le\epsilon$. By the key observation $\mathrm{dist}(Q_i,Q_j)=\mathrm{TV}(Q_i,Q_j)$:
$$\mathrm{TV}(P,Q)\le\mathrm{TV}(P,Q_i)+\mathrm{TV}(Q_i,Q_j)+\mathrm{TV}(Q_j,Q)\le2\epsilon+\mathrm{dist}(Q_i,Q_j)\le2\epsilon+\mathrm{dist}(Q_i,P)+\mathrm{dist}(P,Q)+\mathrm{dist}(Q,Q_j)\le4\epsilon+\mathrm{dist}(P,Q).$$
*Conclusion.* By (32.51) and (32.48), $\mathrm{TV}(\tilde P,P)\le\mathrm{dist}(P,\tilde P)+4\epsilon\le2\,\mathrm{dist}(P,\hat P_n)+4\epsilon$. Squaring and taking expectations with (32.49):
$$\mathbb E[\mathrm{TV}(\tilde P,P)^2]\le32\epsilon^2+8\mathbb E[\mathrm{dist}(P,\hat P_n)^2]\le32\epsilon^2+\frac{8C_0\log|N|}n.$$
(As printed with $\log|N|$; since $|\mathcal A|\le N(N-1)$, $\log|\mathcal A|\le2\log N$, a factor absorbed into constants. added step.) Choosing the optimal TV cover gives (32.45).

> **Intuition note.** The Yatracos sets are built from the cover centers and can be compared with the data cheaply, since there are finitely many. For cover centers, $\mathrm{dist}=\mathrm{TV}$, and on the whole model $\mathrm{dist}\le\mathrm{TV}\le\mathrm{dist}+4\epsilon$. So minimizing $\mathrm{dist}$ to the empirical distribution controls TV up to $O(\epsilon)$.

**Remark 32.5 (robust version)** (pp. 621–622). The scheme also works when $P\notin\mathcal P$ but is close. With $Q^*=\arg\min_{Q\in\{Q_i\}}\mathrm{TV}(P,Q)$, and using $\mathrm{dist}\le\mathrm{TV}$: $\mathrm{dist}(Q^*,\hat P_n)\le\mathrm{TV}(P,Q^*)+\mathrm{dist}(P,\hat P_n)$. Then, as printed,
$$\mathrm{TV}(\tilde P,P)\le\mathrm{TV}(\tilde P,Q^*)+\mathrm{TV}(Q^*,P)=\mathrm{dist}(\tilde P,Q^*)+\mathrm{TV}(Q^*,P)\le\dots\le2\,\mathrm{dist}(P,\hat P_n)+3\,\mathrm{TV}(P,Q^*),$$
and $3\mathrm{TV}(P,Q^*)\le3\epsilon+3\min_{P'\in\mathcal P}\mathrm{TV}(P,P')$. The multiplier 3 is, surprisingly, not improvable if the estimator must be proper (cf. [70]).

### 32.4 Density estimation over Hölder classes (pp. 622–625)
Let $\mathcal F\equiv\mathcal F_\beta(1,1)$ be the $\beta$-smooth densities on $[0,1]^d$ (following Thm 27.14); the parameter is the density $f$ itself. Quadratic risk: $\|f-\hat f\|_2^2=\int_0^1(f-\hat f)^2$ (p. 622).

**Theorem 32.17.**
$$R^*_{L_2}(n;\mathcal F)\triangleq\inf_{\hat f}\sup_{f\in\mathcal F}\mathbb E\|f-\hat f\|_2^2\asymp n^{-\frac{2\beta}{2\beta+d}}.\tag{32.52}$$
Plan: the upper bound uses Theorem 32.1 and the lower bound uses Fano (Thm 31.3), with a reduction from L2 to KL (p. 622).

**Lemma 32.18.** Let $\mathcal F'=\{f\in\mathcal F:f\ge\frac12\}$. Then $R^*_{L_2}(n;\mathcal F')\le R^*_{L_2}(n;\mathcal F)\le4R^*_{L_2}(n;\mathcal F')$. *Proof:* the left side holds as $\mathcal F'\subset\mathcal F$. For the right side, given $X_i\sim f$, draw $U_i$ uniform on $[0,1]^d$ and set $Z_i=U_i$ w.p. $\frac12$, $Z_i=X_i$ w.p. $\frac12$. Then $Z_i\sim g=\frac12(1+f)\in\mathcal F'$. Take a minimax $\hat g$ for $\mathcal F'$ and $\hat f=2\hat g-1$. Then $\|f-\hat f\|_2^2=4\|g-\hat g\|_2^2$ (p. 622).

Every $\beta$-smooth density is bounded above by an absolute constant, so on $\mathcal F'$: $D(f\|g)\asymp\|f-g\|_2^2$ (32.53) (p. 623).
**Lemma 32.19.** If $f=\frac{dP}{d\mu}$, $g=\frac{dQ}{d\mu}$ are both bounded above by $C$ and below by $c$ (absolute constants; see Reading notes), then
$$\frac1{4C}\int d\mu(f-g)^2\le H^2(P,Q)\le D(P\|Q)\le\chi^2(P\|Q)\le\frac1c\int d\mu(f-g)^2.$$
*Proof.* Upper: by (7.34), $D\le\chi^2=\int\frac{(f-g)^2}g\le\frac1c\int(f-g)^2$. Lower: by (7.33), $D\ge H^2=\int\frac{(f-g)^2}{(\sqrt f+\sqrt g)^2}\ge\frac1{4C}\int(f-g)^2$ (added step: $(\sqrt f+\sqrt g)^2\le4C$) (p. 623).

*Proof of Theorem 32.17* (pp. 623–624). By Lemma 32.18 consider $\mathcal F'$. Upper bound:
$$R^*_{L_2}(n;\mathcal F')\overset{(a)}\asymp R^*_{\rm KL}(n;\mathcal F')\overset{(b)}\lesssim\inf_\epsilon\Big\{\epsilon^2+\tfrac1n\log N_{\rm KL}(\mathcal F',\epsilon)\Big\}\overset{(c)}\asymp\inf_\epsilon\Big\{\epsilon^2+\tfrac1n\log N(\mathcal F',\|\cdot\|_2,\epsilon)\Big\}\overset{(d)}\asymp\inf_\epsilon\Big\{\epsilon^2+\tfrac1{n\epsilon^{d/\beta}}\Big\}\asymp n^{-\frac{2\beta}{2\beta+d}}.$$
(a),(c) use (32.53); (b) is Thm 32.1; (d) uses the metric entropy of the Lipschitz class (Thm 27.14), noting that $\mathcal F'$ has at most the entropy of $\mathcal F$. (added step: equating $\epsilon^2=\frac1{n\epsilon^{d/\beta}}$ gives $\epsilon=n^{-\beta/(2\beta+d)}$.)
Lower bound: $\log N(\mathcal F,\|\cdot\|_2,\epsilon)\asymp\log M(\mathcal F,\|\cdot\|_2,\epsilon)\asymp\epsilon^{-d/\beta}$ (Thms 27.14, 27.2). Take an $\epsilon$-packing $f_1,\dots,f_M$ in $\mathcal F$, $M\ge\exp(C\epsilon^{-d/\beta})$; then $g_i=(f_i+1)/2$ is an $\frac\epsilon2$-packing in $\mathcal F'$. Fano gives
$$R^*_{L_2}(n;\mathcal F')\gtrsim\epsilon^2\Big(1-\frac{C_n'}{\log M}\Big),\tag{32.54}$$
with $C_n'$ the capacity (KL radius) from $f\in\mathcal F'$ to $X^n$. By (32.17) and Lemma 32.19, $C_n'\le\inf_\epsilon(n\epsilon^2+\log N_{\rm KL}(\mathcal F',\epsilon))\asymp\inf_\epsilon(n\epsilon^2+\log N(\mathcal F',\|\cdot\|_2,\epsilon))\lesssim\inf_\epsilon(n\epsilon^2+\epsilon^{-d/\beta})\asymp n^{d/(2\beta+d)}$. With $\epsilon=cn^{-\beta/(2\beta+d)}$, $c$ small, $C_n'\le\frac12\log M$, so $R^*_{L_2}(n;\mathcal F')\gtrsim\epsilon^2\asymp n^{-2\beta/(2\beta+d)}$.

**Remark 32.6** (p. 624). The capacity can also be bounded below via Thm 32.5: $C_n'\gtrsim\min\{n\epsilon^2,\log M(\mathcal F',H,\epsilon)\}-2\asymp\min\{n\epsilon^2,\epsilon^{-d/\beta}\}-2\asymp n^{d/(2\beta+d)}$, for the same $\epsilon$. So $C_n'\asymp n^{d/(2\beta+d)}$, and online-to-batch (32.26) (or (32.7) with (32.9)) gives $R^*_{\rm KL}(n;\mathcal F')\asymp C_n'/n\asymp n^{-2\beta/(2\beta+d)}$.

**Remark 32.7** (p. 624). The entropic bound (32.1) is rate-optimal but not attained by a computationally efficient estimator; the same criticism applies to (32.2), (32.3). For squared loss, the kernel density estimator (KDE) convolves $\hat P_n$ with a kernel chosen according to smoothness. For Lipschitz densities a box kernel $K(\cdot)=\frac1{2h}\mathbb 1\{|\cdot|\le h\}$ with $h=n^{-1/3}$ attains the rate of Thm 32.17 (cf. [424]). L2 dominates the classical literature because its quadratic form allows bias–variance decomposition, but L2 distance between densities has no clear operational meaning.

*Other losses* (pp. 624–625):
$$R^*_{\rm TV}(n;\mathcal F)\asymp n^{-\frac\beta{2\beta+d}},\tag{32.55}$$
$$R^*_{H^2}(n;\mathcal F)\asymp n^{-\frac\beta{\beta+d}},\tag{32.56}$$
$$n^{-\frac\beta{\beta+d}}\lesssim R^*_{\rm KL}(n;\mathcal F)\lesssim n^{-\frac\beta{\beta+d}}(\log n)^{\frac d{\beta+d}}.\tag{32.57}$$
- *TV.* The upper bound follows from the L2 rates and $\|f-\hat f\|_1\le\|f-\hat f\|_2$ (Cauchy–Schwarz), or from Yatracos' estimator. The lower bound is the same Fano argument, since L1 entropy behaves the same (Thm 27.14).
- *Hellinger.* For L2/L1 the rate comes from the subclass $\mathcal F'$, on which $L_p\asymp H\asymp$ KL. It was surprising when Birgé [54] found the Hellinger rate on the full $\mathcal F$ to be different. The generic inequality $\frac{H^2}2\le\mathrm{TV}\le H$ (7.22) gives neither bound. What works is comparing entropy numbers via the first inequality:
$$\log N(\mathcal F,H,\epsilon)\le\log N(\mathcal F,\mathrm{TV},\epsilon^2/2)\lesssim\epsilon^{-2d/\beta}.\tag{32.58}$$
With Thm 32.9 this proves the upper bound in (32.56). (Fn. 7: the rate equals the L2 rate with $\beta\to\beta/2$. For $\beta\le1$, $\sqrt f$ is $\beta/2$-Hölder, explaining this. The interpretation fails in general; Glaeser constructs an infinitely differentiable $f$ with $\sqrt f$ having arbitrarily large second derivatives.)
 Lower bound (pp. 625): fix small $\epsilon$ and $\mathcal F'=\{f\in\mathcal F:f\ge\epsilon\}$. By the argument of Lemma 32.13 there exist $f_0,\dots,f_M\in\mathcal F$ with $\|f_i-f_j\|_2\ge c_0\epsilon$, $\|f_i-f_0\|_\infty\le\epsilon$, and $M\ge M(\mathcal F,\|\cdot\|_2,c_0\epsilon)/M(\mathcal F,\|\cdot\|_\infty,\epsilon)\ge\exp(c_1\epsilon^{-d/\beta})$. With $h_i=f_i-f_0$, define $f_i(x)=\epsilon+h_i(2x)$ on $[0,\frac12]^d$, extended smoothly to a valid density in $\mathcal F'$. Then $H^2(f_i,f_j)\ge\int_{[0,1/2]^d}\frac{(f_i-f_j)^2}{(\sqrt{f_i}+\sqrt{f_j})^2}\ge c_2\epsilon$, a Hellinger $\Omega(\sqrt\epsilon)$-packing (this also shows (32.58) is tight). For $f,g\in\mathcal F'$, $D\le\chi^2\le\|f-g\|_2^2/\epsilon$, so $N_{\rm KL}(\mathcal F',\delta^2/\epsilon)\le N(\mathcal F',\|\cdot\|_2,\delta)$ and $C_n'\lesssim\inf_\delta(n\delta^2/\epsilon+\delta^{-d/\beta})\asymp(n/\epsilon)^{d/(2\beta+d)}$. Fano as in (32.54) gives an $\Omega(\epsilon)$ lower bound on $H^2$ if $\log M\ge2C_n'$, achieved by $\epsilon=c_3n^{-\beta/(\beta+d)}$. (added check: then $\epsilon^{-d/\beta}$ and $(n/\epsilon)^{d/(2\beta+d)}$ both scale as $n^{d/(\beta+d)}$.)
- *KL.* The lower bound in (32.57) follows from (32.56), since $D\ge H^2$. For the upper bound, (32.7) gives $R^*_{\rm KL}(n;\mathcal F)\le C_{n+1}/(n+1)$. Thm 32.6 bounds $C_n$ via Hellinger entropy: using (32.58) with (32.22), $C_n\le\inf_\epsilon(n\epsilon^2\log\frac1\epsilon+\epsilon^{-2d/\beta})\asymp(n\log n)^{d/(d+\beta)}$. This capacity bound is tight up to logs: $\log M(\mathcal F,H,\epsilon)\gtrsim\epsilon^{-2d/\beta}$ and Thm 32.5 give $C_n\gtrsim n^{d/(d+\beta)}$ (fn. 8). To the best of the authors' knowledge, resolving the logarithmic gap in (32.57) remains open.

> **Intuition note.** Smooth densities are the test case for all three methods. The L2/TV rates are set by $\epsilon^{-d/\beta}$ entropy on the lower-bounded subclass, whereas Hellinger sees entropy $\epsilon^{-2d/\beta}$ on the full class. The Hellinger rate matches the L2 rate with $\beta$ replaced by $\beta/2$. The source explains this through $\sqrt f$ being $\beta/2$-Hölder, but only for $\beta\le1$ (p. 625, fn. 7).

## Toy example (ours; not from the text)
Model $\mathcal P=\{P_a,P_b\}$ with $P_a=\mathrm{Ber}(1/4)$, $P_b=\mathrm{Ber}(3/4)$. All logs are base 2 (bits). Covering with $\epsilon=0$ takes $N=2$ centers, so by (32.8) $R^*_{\rm KL}(n)\le\frac{\log2}{n+1}=\frac1{n+1}$ bit.

Take $n=1$, $Q_{X^2}=\frac12P_a^{\otimes2}+\frac12P_b^{\otimes2}$, and true $\theta=P_b$ (the case $P_a$ is symmetric).
- $Q_{X_1}$: mean $\frac12\cdot\frac14+\frac12\cdot\frac34=\frac12$, so $\mathrm{Ber}(1/2)$.
- $Q_{X_2|X_1=1}$: posterior weights $\propto(\frac14,\frac34)$, so $P(X_2=1)=\frac14\cdot\frac14+\frac34\cdot\frac34=\frac58$.
- $Q_{X_2|X_1=0}$: weights $\propto(\frac34,\frac14)$, so $P(X_2=1)=\frac34\cdot\frac14+\frac14\cdot\frac34=\frac38$.

Estimator (32.14): $\hat P=\mathrm{Ber}(q)$ with $q=\frac12(\frac12+\frac58)=\frac9{16}$ if $X_1=1$ (probability $\frac34$) and $q=\frac12(\frac12+\frac38)=\frac7{16}$ if $X_1=0$ (probability $\frac14$).

Risk, with $D(\mathrm{Ber}(\frac34)\|\mathrm{Ber}(q))=\frac34\log\frac{3/4}q+\frac14\log\frac{1/4}{1-q}$:
- $q=\frac9{16}$: $\frac34\log\frac43+\frac14\log\frac47=0.75(0.41504)+0.25(-0.80735)=0.31128-0.20184=0.10944$.
- $q=\frac7{16}$: $\frac34\log\frac{12}7+\frac14\log\frac49=0.75(0.77761)+0.25(-1.16993)=0.58321-0.29248=0.29073$.
- Risk $=0.75(0.10944)+0.25(0.29073)=0.08208+0.07268=0.15476$ bits.

Check of step (a), the average of per-step divergences:
- $i=1$: $D(\mathrm{Ber}(\frac34)\|\mathrm{Ber}(\frac12))=1-h(\frac34)=1-0.81128=0.18872$.
- $i=2$: $0.75\,D(\frac34\|\frac58)+0.25\,D(\frac34\|\frac38)=0.75(0.05103)+0.25(0.41952)=0.14315$.
- Average: $\frac12(0.18872+0.14315)=0.16594$.

So $0.15476\le0.16594\le0.5=\frac{\log2}{2}$: convexity gives the first inequality, and $Q\ge\frac12P_\theta^{\otimes2}$ gives the last. The factor $\log N=\log 2$ is exactly the cost of not knowing which of the two centers is true.

## Concepts
- [[channel-capacity]] — here $C_n=\sup_\pi I(\theta;X^n)$, the capacity of $\theta\mapsto X^n$; for a general channel the capacity equals $\inf_\epsilon\{\epsilon^2+\log N_{\rm KL}(\epsilon)\}$ (Thm 32.4); for $C_n$ it is bounded by $\inf_\epsilon\{n\epsilon^2+\log N_{\rm KL}(\mathcal P,\epsilon)\}$ (pp. 603, 608–609)
- [[mutual-information]] — the Bayes KL risk is the conditional mutual information $I(\theta;X_{n+1}|X^n)$ (p. 605)
- [[relative-entropy-kl-divergence]] — loss $D(P_\theta\|\hat P)$; asymmetric, and the reverse loss is typically infinite nonparametrically (p. 603)
- [[f-divergence]] — squared Hellinger is an f-divergence, hence convex, so Hellinger balls are convex (p. 614)
- [[fanos-inequality]] — used for the minimax lower bounds in this chapter (Thm 32.14, Cor 32.15, §32.4), in the form of Thm 31.3 (pp. 619, 620, 623)
- [[universal-coding]] — $C_n$ is the redundancy (13.10) governing minimax regret in universal compression (p. 604)
- [[minimax-risk]] (new) — $\inf_{\hat P}\sup_\theta\mathbb E_\theta\,\mathrm{loss}$; here $R^*_{\rm KL}(n)$ (p. 603)
- [[metric-entropy-covering-number]] (new) — fewest balls of radius $\epsilon$ covering the model; used under KL, Hellinger, TV and L2 (pp. 602, 603)
- [[proper-vs-improper-estimator]] (new) — proper estimators lie in the model class; Yang–Barron's are generally improper, Le Cam–Birgé's and Yatracos' are proper (pp. 603, 607, 614, 620)
- [[predictive-density-estimator]] (new) — Bayes estimator $P_{X_{n+1}|X^n}$ for KL loss (p. 605)
- [[online-to-batch-conversion]] (new) — $nR^*_n\le C_n\le\sum_tR_t^*$ relating cumulative and one-step minimax risks (p. 611)
- [[local-entropy-doubling-dimension]] (new) — $N_{\rm loc}$ covers Hellinger balls by half-radius balls; $\log N_{\rm loc}\le d\log\frac1\epsilon$ means doubling dimension at most $d$ (p. 616)
- [[yatracos-class]] (new) — sets $A_{ij}$ where $Q_i$'s density exceeds $Q_j$'s; define a pseudo-distance with $\mathrm{dist}\le\mathrm{TV}\le\mathrm{dist}+4\epsilon$ on the model (p. 621)
- [[renyi-radius]] (new) — $R_\lambda(\mathcal P)=\inf_U\sup_PD_\lambda(P\|U)$; finiteness for some $\lambda>1$ links KL and Hellinger entropy (p. 610)

## Canonical instances
- [[gaussian-location-model]] — $P_\theta=\mathcal N(\theta,I_d)$, $D=\frac12\|\theta-\theta'\|_2^2$; fits the finite-dimensional bound $R^*_{\rm KL}\lesssim\frac{d\log n}n$ (p. 604)
- [[bernoulli-family]] — even here, exact $C_n$ is in general difficult to compute (p. 604)
- [[ber-half-vs-ber-0-1]] — $\{\mathrm{Ber}(1/2)\}$ vs $\{\mathrm{Ber}(0),\mathrm{Ber}(1)\}$: Theorem 32.8 is very loose (p. 613)
- [[holder-smooth-densities]] — $\mathcal F_\beta(1,1)$ on $[0,1]^d$; rates (32.52), (32.55)–(32.57) (pp. 622–625)
- [[kernel-density-estimator]] — box kernel with $h=n^{-1/3}$ attains the L2 rate for Lipschitz densities (p. 624)
- [[gaussian-mixture-bounded-centers]] — a model with $H^2\asymp D$, where the local-entropy rate is exact (p. 619)

## Bridges (candidates)
- [same-math] $C_n$ as capacity of $\theta\mapsto X^n$ ↔ information-theory: redundancy and minimax regret of universal compression — the source states they are the same quantity (p. 604).
- [structural-analogy] Online-to-batch conversion ($nR_n^*\le C_n\le\sum R_t^*$) ↔ machine learning: relation between online regret and batch generalization — the same cumulative-versus-last-step logic.
- [structural-analogy] Yatracos class (comparing hypotheses only on finitely many sets) ↔ statistical learning: restricting to a low-complexity family to control uniform deviations — the text says the key is to inspect only a "low-complexity" family of sets.
- [structural-analogy] Capacity $\approx\inf_\epsilon\{\epsilon^2+\log N\}$ ↔ model selection / description length: trade-off between a quantization error and the bits naming the cell.

## Questions this raises
- When is $\log N_{\rm loc}\asymp\log M_{\rm loc}$ guaranteed rather than observed in known instances (p. 618)?
- Can the $(\log n)^{d/(\beta+d)}$ gap for KL risk on Hölder densities be closed (p. 625)?
- Which computationally efficient estimators attain the entropic rates for Hellinger and TV loss, as KDE does for L2 (p. 624)?
- How do these bounds change under misspecification beyond the factor-3 TV result (pp. 621–622)?

## Reading notes
- Page offset: printed = pdf − 25 (pdf 627 = printed 602). The chapter is printed as Chapter 32; sections are numbered 32.x.
- The symbols $\lesssim,\gtrsim,\asymp$ are not defined on these pages; I read them as "up to constant factors". The text layer was garbled for symbols such as $\asymp$; I used the images.
- The exercises cited (Ex. I.58, I.59, III.31) are not printed in this unit, so no exercises section is given.
- Factorization of $Q_{X^{n+1}}$ on p. 606: the image shows the product up to $n-1$. By (32.14) the index should run to $n+1$. The text also says $Q_{X_i|X^{i-1}}$ takes "the sample $X^i$ of size $i$" as input; I use $X^{i-1}$, as in (32.14).
- Remark 32.3 prints "all 0's or all 0's"; I read it as all samples equal (all 0's or all 1's).
- In the proof of Thm 32.9, $T_i$ is defined with $H^2$ but later compared with $H(P_i,P_j)$ and $t\delta$. I report both as printed; $H$ may have been intended in the definition.
- Lemma 32.11 as printed: the base case $k=0$ would give bound $N_{\rm loc}^0=1$, while (32.37) gives only $\le N_{\rm loc}$. I report the lemma as printed.
- Proof of Thm 32.10: the last step $e^{-4^\ell}\le e^{-t^2}$ goes the wrong way as printed (since $4^\ell\le t^2$).
- (32.27) and the sentence after (32.25) print sums starting at $t=0$, where $C_t/t$ and $R_0^*$ are not defined in these pages. In the proof of (32.51) the printed text has $\mathrm{TV}(P,P_i)\le\epsilon$ where $Q_i$ is meant.
- Lemma 32.19 reads "upper and lower bounded by absolute constants $c$ and $C$ respectively". The proof needs $c\le f,g\le C$ for both densities, which I use.
- Remark 32.4 contains an index-tag artifact ("Le Cam dimension|see doubling dimension") and Lemma 32.11 prints "$k\ge\mathbb Z_+$"; I read it as $k\in\mathbb Z_+$.
