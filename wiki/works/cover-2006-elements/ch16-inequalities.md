---
id: cover-2006-elements/ch16-inequalities
work: cover-2006-elements
unit: "16 Inequalities in Information Theory"
pages: 482-509
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Inequalities in Information Theory (Chapter 16)

## L0 — One line
Convexity and non-negative relative entropy generate a web of inequalities for entropy, Fisher information, volumes and determinants. Because Gaussian entropy is a log-determinant, information inequalities become matrix inequalities.

## L1 — The gist (≤ 120 words)
The chapter collects the inequalities used throughout the book and adds new ones. It starts from convexity and the non-negativity of relative entropy. It proves monotone inequalities for the entropy of subsets of variables. It links differential entropy to Fisher information (de Bruijn's identity) and derives the entropy power inequality. One common proof also gives the Brunn–Minkowski inequality on volumes of set sums. Gaussian entropy is a log-determinant, so information inequalities become determinant inequalities (Hadamard, Szász, Minkowski, Bergström). The chapter also draws parallels with inequalities in matrix theory and probability theory.

**Prerequisites:** convex/concave functions; entropy, relative entropy, mutual information; multivariate normal and covariance matrices; determinants and principal submatrices; basic calculus (integration by parts).

## L2 — Key ideas (5–10 bullets)
- Many of the basic inequalities of information theory follow directly from convexity (the author's wording). 16.1 restates the information inequality $D\ge 0$, conditioning reduces entropy and the chain-rule bound, with their equality conditions. (pp. 482–485)
- For differential entropy, the normal maximises $h$ for a given covariance: $h(\mathbf X)\le\frac12\log(2\pi e)^n|K|$. This is the bridge to matrix results. (p. 488)
- Entropy per element of a random $k$-subset decreases with $k$ (Han); conditional entropy per element increases with $k$. Both follow from the chain rule. (pp. 491–493)
- de Bruijn: adding Gaussian noise of variance $t$ changes $h$ at rate $\frac12 J$. This gives a proof route to the entropy power inequality. (pp. 494–497)
- The entropy power inequality and Brunn–Minkowski are special cases ($r\to1$, $r\to0$) of one Rényi-entropy inequality derived from Young's inequality. (pp. 497–501)
- Applying entropy inequalities to Gaussians yields Ky Fan, Hadamard, Szász, Minkowski, Toeplitz and Bergström determinant inequalities. (pp. 501–508)
- Fano's inequality and $\mathcal L_1$-type bounds relate error probability, entropy and distance between distributions. (pp. 488–489)

## L3 — Walkthrough

### 16.1 Basic inequalities of information theory
Definition (convex function): $f(\lambda x_1+(1-\lambda)x_2)\le \lambda f(x_1)+(1-\lambda)f(x_2)$ for all $0\le\lambda\le1$ \tag{16.1}. (p. 482)

- Jensen (Thm 16.1.1): if $f$ is convex, $f(EX)\le Ef(X)$ \tag{16.2}. (p. 482)
- Lemma 16.1.1: $\log x$ is concave and $x\log x$ is convex on $0\le x<\infty$. (p. 483)
- Log sum inequality (Thm 16.1.2): for positive $a_i,b_i$,
$$\sum_{i=1}^n a_i\log\frac{a_i}{b_i}\ \ge\ \Big(\sum a_i\Big)\log\frac{\sum a_i}{\sum b_i}\tag{16.3}$$
with equality iff $a_i/b_i$ is constant. (p. 483)
- Entropy $H(X)=-\sum p(x)\log p(x)$ \tag{16.4}; bound $0\le H(X)\le\log|\mathcal X|$ \tag{16.5}. (p. 483)
- Conditioning reduces entropy: $H(X|Y)\le H(X)$, equality iff $X,Y$ independent \tag{16.6}. (p. 483)
- Chain rule: $H(X_1,\dots,X_n)=\sum H(X_i|X_{i-1},\dots,X_1)\le\sum H(X_i)$, equality iff independent \tag{16.7}. $H(\mathbf p)$ is concave in $\mathbf p$ (Thm 16.1.6). (p. 483)
- Relative entropy $D(p\|q)=\sum p(x)\log\frac{p(x)}{q(x)}$ \tag{16.8}. Mutual information $I(X;Y)=\sum\sum p(x,y)\log\frac{p(x,y)}{p(x)p(y)}=D(p(x,y)\|p(x)p(y))$ \tag{16.9}. (p. 484)
- Information inequality (Thm 16.1.7): $D(\mathbf p\|\mathbf q)\ge0$, equality iff $p=q$ everywhere \tag{16.10}. The author says it can prove many other inequalities in the chapter. Corollary: $I(X;Y)\ge0$, equality iff independent \tag{16.11}. $D(p\|q)$ is convex in the pair $(p,q)$ (Thm 16.1.8). (p. 484)
- Thm 16.1.9: $I(X;Y)=H(X)-H(X|Y)$ \tag{16.12}; $=H(Y)-H(Y|X)$ \tag{16.13}; $=H(X)+H(Y)-H(X,Y)$ \tag{16.14}; $I(X;X)=H(X)$ \tag{16.15}. (p. 484)
- Markov chains (Thm 16.1.10): $D(\mu_n\|\mu_n')$ decreases with time; $D(\mu_n\|\mu)$ to the stationary distribution decreases; $H(X_n)$ increases if the stationary distribution is uniform; $H(X_n|X_1)$ increases for a stationary chain. (pp. 484–485)
- Thm 16.1.11: for i.i.d. $X_i\sim p$ with empirical pmf $\hat p_n$, $ED(\hat p_n\|p)\le ED(\hat p_{n-1}\|p)$ \tag{16.16}. (p. 485)

*Intuition note:* The author says many of these basic inequalities follow directly from convexity (p. 482). The basic form is Jensen's inequality: for convex $f$, $f(EX)\le Ef(X)$. The equality conditions (independence, $p=q$) state when each inequality is tight.

### 16.2 Differential entropy
- $h(X_1,\dots,X_n)=-\int f(\mathbf x)\log f(\mathbf x)\,d\mathbf x$ \tag{16.17}. Table 16.1 lists $h$ (in nats) for many densities, e.g. normal $\frac12\ln(2\pi e\sigma^2)$, uniform $\ln(\beta-\alpha)$, exponential $1+\ln\lambda$, Laplace $1+\ln(2\lambda)$. (pp. 485–487)
- $D(f\|g)=\int f\log(f/g)\,d\mathbf x$ \tag{16.18}. Its properties are identical to the discrete case, but differential entropy can be negative. (p. 485)
- Conditioning reduces entropy and the chain rule hold for $h$ (Thms 16.2.1, 16.2.2, \tag{16.19}), with equality iff independent. (p. 485)
- Lemma 16.2.1: if $X,Y$ independent, $h(X+Y)\ge h(X)$. Proof: $h(X+Y)\ge h(X+Y|Y)=h(X|Y)=h(X)$. (p. 488)
- Thm 16.2.3: if $\mathbf X\in\mathbb R^n$ has zero mean and covariance $K=E\mathbf X\mathbf X^t$,
$$h(\mathbf X)\le \tfrac12\log(2\pi e)^n|K|\tag{16.20}$$
with equality iff $\mathbf X\sim\mathcal N(0,K)$. (p. 488)

*Intuition note:* For a fixed covariance, the Gaussian is the most "spread out" distribution. This lets bounds on $h$ turn into bounds on $|K|$.

### 16.3 Bounds on entropy and relative entropy
- Fano (Thm 16.3.1): with $P_e$ the error probability of the best estimator of $X$ from $Y$,
$$H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)\tag{16.21}$$
Consequently, if $H(X|Y)>0$ then $P_e>0$. The author notes its use for bounding error away from zero at rates above capacity. (p. 488)
- $\mathcal L_1$ bound (Thm 16.3.2): if $\|p-q\|_1=\sum|p(x)-q(x)|\le\frac12$ \tag{16.22}, then
$$|H(p)-H(q)|\le-\|p-q\|_1\log\frac{\|p-q\|_1}{|\mathcal X|}\tag{16.23}$$
(p. 488)
- Proof. $f(t)=-t\log t$ is concave with $f(0)=f(1)=0$ (Fig. 16.1), hence non-negative on $[0,1]$. A chord from $t$ to $t+\nu$ ($\nu\le\frac12$) has maximal absolute slope at an end, so for $0\le t\le1-\nu$:
$$|f(t)-f(t+\nu)|\le\max\{f(\nu),f(1-\nu)\}=-\nu\log\nu\tag{16.24}$$
Let $r(x)=|p(x)-q(x)|$ and $s=\|p-q\|_1$. Then (pp. 488–489)
$$|H(p)-H(q)|=\Big|\sum(-p\log p+q\log q)\Big|\le\sum|{-p\log p+q\log q}|\le\sum-r(x)\log r(x)$$
(16.25–16.27, using 16.24). Writing $r=s\cdot(r/s)$ (added step; the book prints this as (16.28), which is garbled in the text layer) gives $=-s\log s+s\,H\!\big(r(x)/s\big)\le-s\log s+s\log|\mathcal X|$ (16.28–16.30). (p. 489)
- Thm 16.3.3 (from Thm 9.7.1): for a distribution on the positive integers,
$$H(p_1,p_2,\dots)\le\tfrac12\log(2\pi e)\Big(\sum i^2p_i-\big(\sum ip_i\big)^2+\tfrac1{12}\Big)\tag{16.31}$$
(p. 489)
- Lemma 16.3.1: relative entropy is "stronger" than $\mathcal L_1$: $D(p_1\|p_2)\ge\frac{1}{2\ln2}\|p_1-p_2\|_1^2$ \tag{16.32}. (p. 489)

### 16.4 Inequalities for types
Restated from Chapter 12 (p. 490):
- Number of types with denominator $n$: $|\mathcal P_n|\le(n+1)^{|\mathcal X|}$ \tag{16.33}.
- For i.i.d. $X_i\sim Q$, $Q^n(x^n)=2^{-n(H(P_{x^n})+D(P_{x^n}\|Q))}$ \tag{16.34}.
- Type class size: $\frac1{(n+1)^{|\mathcal X|}}2^{nH(P)}\le|T(P)|\le2^{nH(P)}$ \tag{16.35}.
- $\frac1{(n+1)^{|\mathcal X|}}2^{-nD(P\|Q)}\le Q^n(T(P))\le2^{-nD(P\|Q)}$ \tag{16.36}, i.e. $2^{-nD(P\|Q)}$ to first order in the exponent.

### 16.5 Entropy rates of subsets
Goal: extend the chain-rule bound $h(X_1,\dots,X_n)\le\sum h(X_i)$ \tag{16.37}. For $S\subseteq\{1,\dots,n\}$, $X(S)=\{X_i:i\in S\}$. Define
$$h_k^{(n)}=\frac1{\binom nk}\sum_{S:|S|=k}\frac{h(X(S))}{k}\tag{16.38}$$
the average entropy per symbol of a random $k$-subset. (pp. 490–491)

**Thm 16.5.1 (Han):** $h_1^{(n)}\ge h_2^{(n)}\ge\dots\ge h_n^{(n)}$ \tag{16.39}. (p. 491)
Proof. First $h_n^{(n)}\le h_{n-1}^{(n)}$. By the chain rule and conditioning reduces entropy,
$h(X_1..X_n)=h(X_1..X_{n-1})+h(X_n|X_1..X_{n-1})$;
$h(X_1..X_n)=h(X_1..X_{n-2},X_n)+h(X_{n-1}|X_1..X_{n-2},X_n)\le h(X_1..X_{n-2},X_n)+h(X_{n-1}|X_1..X_{n-2})$;
… ; $h(X_1..X_n)\le h(X_2..X_n)+h(X_1)$.
Adding the $n$ inequalities and using the chain rule:
$$nh(X_1,\dots,X_n)\le\sum_{i=1}^nh(X_1,\dots,X_{i-1},X_{i+1},\dots,X_n)+h(X_1,\dots,X_n)\tag{16.40}$$
Subtracting $h(X_1..X_n)$ (added step) and dividing by $n(n-1)$:
$$\frac1nh(X_1,\dots,X_n)\le\frac1n\sum_{i=1}^n\frac{h(X_1,\dots,X_{i-1},X_{i+1},\dots,X_n)}{n-1}\tag{16.41}$$
which is $h_n^{(n)}\le h_{n-1}^{(n)}$. For general $k$: the inequality holds within each $k$-subset ($h_k^{(k)}\le h_{k-1}^{(k)}$), so it survives averaging over all $k$-subsets. (p. 491)

*Intuition note:* Larger groups contain more mutual dependence, so the average entropy per member falls as the group grows.

**Thm 16.5.2:** for $r>0$ let $t_k^{(n)}=\frac1{\binom nk}\sum_{S:|S|=k}e^{rh(X(S))/k}$ \tag{16.42}. Then $t_1^{(n)}\ge t_2^{(n)}\ge\dots\ge t_n^{(n)}$ \tag{16.43}. Proof: multiply (16.41) by $r$, exponentiate, and apply the arithmetic–geometric mean inequality (16.44–16.45); this gives $t_n^{(n)}\le t_{n-1}^{(n)}$. Then average over subsets as before. (p. 492)

**Conditional version.** $g_k^{(n)}=\frac1{\binom nk}\sum_{S:|S|=k}\frac{h(X(S)|X(S^c))}{k}$ \tag{16.46}. As $k$ grows, the conditioning set $S^c$ shrinks, and the resulting rise in entropy dominates the extra dependence. So the order is reversed. (p. 492)

**Thm 16.5.3 (Han):** $g_1^{(n)}\le g_2^{(n)}\le\dots\le g_n^{(n)}$ \tag{16.47}. Proof: from $h(X_1..X_n)\le\sum h(X_i)$ \tag{16.48}, subtracting from $nh$:
$$(n-1)h(X_1,\dots,X_n)\ge\sum_i\big(h(X_1,\dots,X_n)-h(X_i)\big)\tag{16.49}$$
$$=\sum_ih(X_1,\dots,X_{i-1},X_{i+1},\dots,X_n|X_i)\tag{16.50}$$
Dividing by $n(n-1)$ gives $\frac{h(X_1..X_n)}n\ge\frac1n\sum_i\frac{h(\dots|X_i)}{n-1}$ \tag{16.51}, i.e. $g_n^{(n)}\ge g_{n-1}^{(n)}$; averaging over subsets gives the rest. (p. 493)

**Thm 16.5.4:** with $f_k^{(n)}=\frac1{\binom nk}\sum_{S:|S|=k}\frac{I(X(S);X(S^c))}{k}$ \tag{16.52}, $f_1^{(n)}\ge f_2^{(n)}\ge\dots\ge f_n^{(n)}$ \tag{16.53}. Proof: $I(X(S);X(S^c))=h(X(S))-h(X(S)|X(S^c))$ with Thms 16.5.1 and 16.5.3. (p. 493)

### 16.6 Entropy and Fisher information
Differential entropy measures descriptive complexity; Fisher information measures the minimum error in estimating a parameter (p. 494). For a location family $f(x-\theta)$, $J(\theta)=\int f(x-\theta)[\partial_\theta\ln f(x-\theta)]^2dx$. Differentiating in $x$ is equivalent to differentiating in $\theta$, so the Fisher information of $X$'s distribution is $J(X)=\int f(x)\,[\partial_x\ln f(x)]^2dx$ (16.55–16.56; exact printed form of these lines [unreadable p. 494]). Like entropy, it is a function of the density. (p. 494)

- Cramér–Rao (Thm 16.6.1): for an unbiased estimator $T(X)$ of $\theta$, $\operatorname{var}(T)\ge1/J(\theta)$ \tag{16.57}. (p. 494)
- **de Bruijn's identity (Thm 16.6.2):** $X$ with finite variance and density $f$, $Z\sim\mathcal N(0,1)$ independent:
$$\frac{\partial}{\partial t}h_e(X+\sqrt tZ)=\frac12J(X+\sqrt tZ)\tag{16.58}$$
and, if the limit exists, $\frac{\partial}{\partial t}h_e(X+\sqrt tZ)\big|_{t=0}=\frac12J(X)$ \tag{16.59}. (p. 495)

Proof. $Y_t=X+\sqrt tZ$ has density $g_t(y)=\int f(x)\frac1{\sqrt{2\pi t}}e^{-(y-x)^2/2t}dx$ \tag{16.60}. Differentiating (16.61–16.66):
$$\partial_tg_t=\int f(x)\Big[-\frac1{2t}\frac1{\sqrt{2\pi t}}e^{-\frac{(y-x)^2}{2t}}+\frac{(y-x)^2}{2t^2}\frac1{\sqrt{2\pi t}}e^{-\frac{(y-x)^2}{2t}}\Big]dx\tag{16.62}$$
$$\partial_yg_t=\int f(x)\frac1{\sqrt{2\pi t}}\Big[-\frac{y-x}te^{-\frac{(y-x)^2}{2t}}\Big]dx\tag{16.64}$$
$$\partial_y^2g_t=\int f(x)\frac1{\sqrt{2\pi t}}\Big[-\frac1te^{-\frac{(y-x)^2}{2t}}+\frac{(y-x)^2}{t^2}e^{-\frac{(y-x)^2}{2t}}\Big]dx\tag{16.66}$$
Thus $\partial_tg_t=\frac12\partial_y^2g_t$ \tag{16.67}. With $h_e(Y_t)=-\int g_t\ln g_t\,dy$ \tag{16.68}, differentiating gives $-\int\partial_tg_t\ln g_t\,dy-\int\partial_tg_t\,dy$ (16.69–16.70). The term $\int\partial_tg_t\,dy$ is zero because $\int g_t\,dy=1$ (the source calls it 'the first term'; the order of terms in (16.69–16.70) is not visible in the text layer). The other term, by (16.67) and integration by parts, is
$$\frac12\Big[-\partial_yg_t\ln g_t\Big]_{-\infty}^{\infty}+\frac12\int\frac{(\partial_yg_t)^2}{g_t}dy\tag{16.71}$$
The second term is $\frac12J(Y_t)$. The boundary term is zero: rewrite $\partial_yg_t\ln g_t=\big(\partial_yg_t/\sqrt{g_t}\big)\cdot\big(\sqrt{g_t}\ln g_t\big)$ \tag{16.72}. The square of the first factor integrates to the Fisher information, so it is bounded; the second goes to $0$ as $g_t\to0$ at $\pm\infty$. The author exchanged integration and differentiation in (16.61), (16.63), (16.65), (16.69); strict justification is in Barron. (p. 496)

*Intuition note:* Blurring a density with a little Gaussian noise raises its entropy, and the speed of that rise is half its Fisher information. A larger Fisher information means a faster entropy increase.

- **Entropy power inequality (Thm 16.6.3):** for independent random $n$-vectors $X,Y$ with densities,
$$2^{\frac2nh(X+Y)}\ge2^{\frac2nh(X)}+2^{\frac2nh(Y)}\tag{16.73}$$
(p. 496)
- Outline of Stam–Blachman proof (p. 497). Let $X_t=X+\sqrt{f(t)}Z_1$, $Y_t=Y+\sqrt{g(t)}Z_2$, with independent $\mathcal N(0,1)$ variables $Z_1,Z_2$. The inequality reduces to $s(0)\le1$, where
$$s(t)=\frac{2^{2h(X_t)}+2^{2h(Y_t)}}{2^{2h(X_t+Y_t)}}\tag{16.74}$$
If $f(t),g(t)\to\infty$ then $s(\infty)=1$; if also $s'(t)\ge0$ for $t\ge0$, then $s(0)\le1$. Showing $s'\ge0$ uses a clever choice of $f,g$, Thm 16.6.2, and the Fisher-information convolution inequality $\frac1{J(X+Y)}\ge\frac1{J(X)}+\frac1{J(Y)}$ \tag{16.75}. The vector case follows by induction (the author cites Stam and Blachman for details). (p. 497)

### 16.7 Entropy power inequality and Brunn–Minkowski
- Restatement: let $X',Y'$ be independent normals with $h(X')=h(X)$, $h(Y')=h(Y)$. Then $2^{2h(X')}=(2\pi e)\sigma_{X'}^2$, and (16.73), written for scalar variables ($n=1$), reads $2^{2h(X+Y)}\ge(2\pi e)(\sigma^2_{X'}+\sigma^2_{Y'})=2^{2h(X'+Y')}$ \tag{16.76}. So (Thm 16.7.1) $h(X+Y)\ge h(X'+Y')$ \tag{16.77}. (pp. 497–498)
- Set sum $A+B=\{x+y:x\in A,y\in B\}$. Example 16.7.1: two unit spheres at the origin sum to a sphere of radius 2. **Brunn–Minkowski (Thm 16.7.2):** $V(A+B)\ge V(A'+B')$ \tag{16.78}, with $A',B'$ spheres of the same volumes as $A,B$. The resemblance to the entropy power inequality was pointed out in [58]; a common proof is due to Dembo and Lieb, from a strengthened Young inequality. (p. 498)
- $\mathcal L_r$ norm: $\|f\|_r=(\int f^r(x)dx)^{1/r}$ \tag{16.79}. **Lemma 16.7.1 (strengthened Young):** $\|f*g\|_r\le\big(\frac{C_pC_q}{C_r}\big)^{n/2}\|f\|_p\|g\|_q$ \tag{16.80}, where $\frac1r=\frac1p+\frac1q-1$ \tag{16.81} and $C_p=\frac{p^{1/p}}{p'^{1/p'}}$, $\frac1p+\frac1{p'}=1$ \tag{16.82}. The proof is deferred to [19], [43]. (pp. 498–499)
- Rényi entropy: $h_r(X)=\frac1{1-r}\log\int f^r(x)dx$, $0<r<\infty$, $r\ne1$ \tag{16.83}. Limit $r\to1$ is Shannon $h$ \tag{16.84}. Limit $r\to0$ is $h_0(X)=\log\mu\{x:f(x)>0\}$, the log of the support volume \tag{16.85}. (p. 499)
- Rényi entropy power:
$$V_r(X)=\begin{cases}\big[\int f^r(x)dx\big]^{-\frac2n\frac{r'}r},&0<r\le\infty,\ r\ne1,\ \frac1r+\frac1{r'}=1\\ \exp[\frac2nh(X)],&r=1\\ \mu(\{x:f(x)>0\})^{2/n},&r=0\end{cases}\tag{16.86}$$
(p. 499)
- **Thm 16.7.3:** for independent $X,Y$, $0\le r<\infty$, $0\le\lambda\le1$,
$$\log V_r(X+Y)\ge\lambda\log V_p(X)+(1-\lambda)\log V_q(Y)+H(\lambda)+\frac{1+r}{1-r}\Big[H\Big(\frac{r+\lambda(1-r)}{1+r}\Big)-H\Big(\frac r{1+r}\Big)\Big]\tag{16.87}$$
with $p=\frac r{r+\lambda(1-r)}$, $q=\frac r{r+(1-\lambda)(1-r)}$, $H(\lambda)=-\lambda\log\lambda-(1-\lambda)\log(1-\lambda)$. (pp. 499–500)

Proof. Take the log of Young's inequality (16.80):
$$\tfrac1{r'}\log V_r(X+Y)\ge\tfrac1{p'}\log V_p(X)+\tfrac1{q'}\log V_q(Y)+\log C_r-\log C_p-\log C_q\tag{16.88}$$
Set $\lambda=r'/p'$; then $1-\lambda=r'/q'$ and $p,q$ are as above. Then (16.88) becomes
$$\log V_r(X+Y)\ge\lambda\log V_p(X)+(1-\lambda)\log V_q(Y)+\tfrac{r'}r\log r-\log r'-\tfrac{r'}p\log p+\tfrac{r'}{p'}\log p'-\tfrac{r'}q\log q+\tfrac{r'}{q'}\log q'\tag{16.89}$$
$$=\lambda\log V_p(X)+(1-\lambda)\log V_q(Y)+\tfrac{r'}r\log r-(\lambda+1-\lambda)\log r'-\tfrac{r'}p\log p+\lambda\log p'-\tfrac{r'}q\log q+(1-\lambda)\log q'\tag{16.90}$$
$$=\lambda\log V_p(X)+(1-\lambda)\log V_q(Y)+\tfrac1{r-1}\log r+H(\lambda)-\tfrac{r+\lambda(1-r)}{r-1}\log\tfrac r{r+\lambda(1-r)}\tag{16.91}$$
$$\qquad-\tfrac{r+(1-\lambda)(1-r)}{r-1}\log\tfrac r{r+(1-\lambda)(1-r)}\tag{16.92}$$
which equals the right side of (16.87) (16.93); "details of the algebra for the last step are omitted". (p. 500)

Special cases (p. 501):
- $r\to1$ with $\lambda=\frac{V_1(X)}{V_1(X)+V_1(Y)}$ \tag{16.94} gives $V_1(X+Y)\ge V_1(X)+V_1(Y)$ \tag{16.95}, the entropy power inequality.
- $r\to0$ with $\lambda=\frac{\sqrt{V_0(X)}}{\sqrt{V_0(X)}+\sqrt{V_0(Y)}}$ \tag{16.96} gives $\sqrt{V_0(X+Y)}\ge\sqrt{V_0(X)}+\sqrt{V_0(Y)}$ \tag{16.97}. With $A,B$ the support sets of $X,Y$ (so $A+B$ supports $X+Y$): $[\mu(A+B)]^{1/n}\ge[\mu(A)]^{1/n}+[\mu(B)]^{1/n}$ \tag{16.98}, Brunn–Minkowski.

The theorem also gives a continuum of new inequalities between the two, strengthening the analogy between entropy power and volume. (p. 501)

*Intuition note:* The "size" of a random variable can be measured by entropy power (spread of a density) or by volume (support). In both, the size of a sum is at least the sum of the sizes: $V_1(X+Y)\ge V_1(X)+V_1(Y)$ for entropy power, and $[\mu(A+B)]^{1/n}\ge[\mu(A)]^{1/n}+[\mu(B)]^{1/n}$ for volume (p. 501).

### 16.8 Inequalities for determinants
Assume $K$ is a non-negative definite symmetric $n\times n$ matrix. (p. 501)
- **Thm 16.8.1 (Ky Fan):** $\log|K|$ is concave. Proof: take $\mathbf X_i\sim\mathcal N(0,K_i)$; $\Pr\{\theta=1\}=\lambda$ \tag{16.99}, $\Pr\{\theta=2\}=1-\lambda$ \tag{16.100}; $\theta,\mathbf X_1,\mathbf X_2$ independent; $\mathbf Z=\mathbf X_\theta$ has covariance $\lambda K_1+(1-\lambda)K_2$ but is not normal. By Thm 16.2.3 then Thm 16.2.1:
$$\tfrac12\log(2\pi e)^n|\lambda K_1+(1-\lambda)K_2|\ge h(\mathbf Z)\ge h(\mathbf Z|\theta)=\lambda\tfrac12\log(2\pi e)^n|K_1|+(1-\lambda)\tfrac12\log(2\pi e)^n|K_2|$$
(16.101–16.102), hence $|\lambda K_1+(1-\lambda)K_2|\ge|K_1|^\lambda|K_2|^{1-\lambda}$ \tag{16.103}. (p. 502)
- **Hadamard (Thm 16.8.2):** $|K|\le\prod K_{ii}$, equality iff $K_{ij}=0$ for $i\ne j$. Proof: for $\mathbf X\sim\mathcal N(0,K)$,
$$\tfrac12\log(2\pi e)^n|K|=h(X_1,\dots,X_n)\le\sum h(X_i)=\sum_i\tfrac12\log2\pi e|K_{ii}|\tag{16.104}$$
with equality iff the $X_i$ are independent. (p. 502)
- **Szász (Thm 16.8.3):** let $K(i_1,\dots,i_k)$ be a principal submatrix and $P_k=\prod_{1\le i_1<\dots<i_k\le n}|K(i_1,\dots,i_k)|$ \tag{16.105}. If $K$ is positive definite, then
$$P_1\ge P_2^{1/\binom{n-1}1}\ge P_3^{1/\binom{n-1}2}\ge\dots\ge P_n\tag{16.106}$$
Proof: Thm 16.5.1 applied to $\mathbf X\sim\mathcal N(0,K)$, with $h_k^{(n)}=\frac1{2n\binom{n-1}{k-1}}\log P_k+\frac12\log2\pi e$. (pp. 502–503)
- **Thm 16.8.4:** with $S_k^{(n)}=\frac1{\binom nk}\sum_{i_1<\dots<i_k}|K(i_1,\dots,i_k)|^{1/k}$ \tag{16.107},
$$\tfrac1n\operatorname{tr}(K)=S_1^{(n)}\ge S_2^{(n)}\ge\dots\ge S_n^{(n)}=|K|^{1/n}\tag{16.108}$$
Proof: the source cites the corollary to Thm 16.5.1 (presumably Thm 16.5.2, where $t_k^{(n)}$ is defined) with $t_k^{(n)}=(2\pi e)S_k^{(n)}$ and $r=2$. (p. 503)
- **Thm 16.8.5:** with $Q_k=\Big(\prod_{S:|S|=k}\frac{|K|}{|K(S^c)|}\Big)^{1/k\binom nk}$ \tag{16.109},
$$\Big(\prod_{i=1}^n\sigma_i^2\Big)^{1/n}=Q_1\le Q_2\le\dots\le Q_{n-1}\le Q_n=|K|^{1/n}\tag{16.110}$$
Proof: Thm 16.5.3 with $h(X(S)|X(S^c))=\frac12\log(2\pi e)^k\frac{|K|}{|K(S^c)|}$ \tag{16.111}. (p. 503)
- The outer inequality $Q_1\le Q_n$ is $|K|\ge\prod\sigma_i^2$ \tag{16.112}, where $\sigma_i^2=\frac{|K|}{|K(1,\dots,i-1,i+1,\dots,n)|}$ \tag{16.113} is the minimum mean squared error of linearly predicting $X_i$ from the other $X$'s. It is the conditional variance if the $X$'s are jointly normal. With Hadamard (Corollary): $\prod K_{ii}\ge|K|\ge\prod\sigma_i^2$ \tag{16.114}. (pp. 503–504)
- **Toeplitz (Thm 16.8.6):** a Toeplitz matrix has $K_{ij}=K_{rs}$ whenever $|i-j|=|r-s|$. $K_k$ denotes the principal minor $K(1,\dots,k)$. If $K$ is positive definite Toeplitz,
$$|K_1|\ge|K_2|^{1/2}\ge\dots\ge|K_{n-1}|^{1/(n-1)}\ge|K_n|^{1/n}\tag{16.115}$$
$|K_k|/|K_{k-1}|$ is decreasing in $k$, and $\lim|K_n|^{1/n}=\lim|K_n|/|K_{n-1}|$ \tag{16.116}. (p. 504)
 Proof: for $(X_1..X_n)\sim\mathcal N(0,K_n)$, $h(X_k|X_{k-1},\dots,X_1)=h(X^k)-h(X^{k-1})=\frac12\log(2\pi e)\frac{|K_k|}{|K_{k-1}|}$ (16.117–16.118). Monotonicity follows from
$$h(X_k|X_{k-1},\dots,X_1)=h(X_{k+1}|X_k,\dots,X_2)\ge h(X_{k+1}|X_k,\dots,X_2,X_1)$$
(16.119–16.120): equality by the Toeplitz assumption, inequality because conditioning reduces entropy. So the running averages $\frac1kh(X_1..X_k)=\frac1k\sum h(X_i|X_{i-1},\dots,X_1)$ are decreasing \tag{16.121}, and (16.115) follows from $h(X_1..X_k)=\frac12\log(2\pi e)^k|K_k|$. A decreasing sequence has a limit; by the Cesàro mean theorem, $\lim\frac{h(X_1..X_n)}n=\lim h(X_n|X_{n-1},\dots,X_1)$ \tag{16.122}, i.e. (16.116) \tag{16.123}. (pp. 504–505)
- **Minkowski (Thm 16.8.7):** $|K_1+K_2|^{1/n}\ge|K_1|^{1/n}+|K_2|^{1/n}$ \tag{16.124}. Proof: independent $\mathbf X_i\sim\mathcal N(0,K_i)$, so $\mathbf X_1+\mathbf X_2\sim\mathcal N(0,K_1+K_2)$. By the entropy power inequality,
$$(2\pi e)|K_1+K_2|^{1/n}=2^{(2/n)h(\mathbf X_1+\mathbf X_2)}\ge2^{(2/n)h(\mathbf X_1)}+2^{(2/n)h(\mathbf X_2)}=(2\pi e)|K_1|^{1/n}+(2\pi e)|K_2|^{1/n}$$
(16.125–16.127). (p. 505)

*Intuition note:* Each determinant inequality is an entropy inequality in disguise, because a Gaussian's entropy is $\frac12\log$ of $(2\pi e)^n$ times the determinant of its covariance. 

### 16.9 Inequalities for ratios of determinants
- **Lemma 16.9.1:** $\sigma_n^2=|K_n|/|K_{n-1}|$, where $\sigma_n^2$ is the minimum mean squared error of linear prediction of $X_n$ from $X_1..X_{n-1}$; for $(X_1..X_n)\sim\mathcal N(0,K_n)$, $X_n$ given the past is normal with that variance. Proof: $\frac12\log2\pi e\sigma_n^2=h(X_n|X_1..X_{n-1})=h(X_1..X_n)-h(X_1..X_{n-1})=\frac12\log(2\pi e)^n|K_n|-\frac12\log(2\pi e)^{n-1}|K_{n-1}|=\frac12\log2\pi e|K_n|/|K_{n-1}|$ (16.128–16.131). (pp. 505–506)
- **Thm 16.9.1 (Bergström):** $\log(|K_n|/|K_{n-p}|)$ is concave in $K_n$. Theorem 16.8.1 cannot be used, since this is a difference of two concave functions. (p. 506)
 Proof: let $\mathbf Z=\mathbf X_\theta$, $\mathbf X_1\sim\mathcal N(0,S_n)$, $\mathbf X_2\sim\mathcal N(0,T_n)$, $\Pr\{\theta=1\}=\lambda=1-\Pr\{\theta=2\}$, all independent; $K_n=\lambda S_n+(1-\lambda)T_n$ \tag{16.132}. Then
$$\lambda\tfrac12\log(2\pi e)^p\tfrac{|S_n|}{|S_{n-p}|}+(1-\lambda)\tfrac12\log(2\pi e)^p\tfrac{|T_n|}{|T_{n-p}|}\overset{(a)}{=}\lambda h(X_{1,n},\dots,X_{1,n-p+1}|X_{1,1},\dots,X_{1,n-p})+(1-\lambda)h(X_{2,n},\dots|X_{2,1},\dots,X_{2,n-p})\tag{16.133}$$
$$=h(Z_n,\dots,Z_{n-p+1}|Z_1,\dots,Z_{n-p},\theta)\tag{16.134}$$
$$\overset{(b)}{\le}h(Z_n,\dots,Z_{n-p+1}|Z_1,\dots,Z_{n-p})\overset{(c)}{\le}\tfrac12\log(2\pi e)^p\tfrac{|K_n|}{|K_{n-p}|}\tag{16.135–16.136}$$
(a) uses $h(X_n..X_{n-p+1}|X_1..X_{n-p})=h(X_1..X_n)-h(X_1..X_{n-p})$; (b) is the conditioning lemma; (c) is a conditional version of Thm 16.2.3. (pp. 506–507)
- **Thm 16.9.2 (Bergström):** $|K_n|/|K_{n-1}|$ is concave in $K_n$. Proof: independent $\mathbf X\sim\mathcal N(0,A_n)$, $\mathbf Y\sim\mathcal N(0,B_n)$, $\mathbf Z=\mathbf X+\mathbf Y$. Then
$$\tfrac12\log2\pi e\tfrac{|A_n+B_n|}{|A_{n-1}+B_{n-1}|}\overset{(a)}=h(Z_n|Z_{n-1},\dots,Z_1)\overset{(b)}\ge h(Z_n|Z_{n-1},..,Z_1,X_{n-1},..,X_1,Y_{n-1},..,Y_1)\overset{(c)}=h(X_n+Y_n|X_{n-1},..,X_1,Y_{n-1},..,Y_1)$$
$$\overset{(d)}=E\tfrac12\log[2\pi e\operatorname{Var}(X_n+Y_n|\cdot)]\overset{(e)}=E\tfrac12\log[2\pi e(\operatorname{Var}(X_n|X_{n-1}..X_1)+\operatorname{Var}(Y_n|Y_{n-1}..Y_1))]\overset{(f)}=\tfrac12\log\Big(2\pi e\Big(\tfrac{|A_n|}{|A_{n-1}|}+\tfrac{|B_n|}{|B_{n-1}|}\Big)\Big)$$
(16.137–16.143). Reasons: (a) Lemma 16.9.1; (b) conditioning decreases entropy; (c) $\mathbf Z$ is a function of $\mathbf X,\mathbf Y$; (d) $X_n+Y_n$ is Gaussian given the past; (e) $X_n,Y_n$ independent given the past; (f) conditional variance of jointly Gaussian variables is constant (Lemma 16.9.1). With $A=\lambda S$, $B=\bar\lambda T$:
$$\frac{|\lambda S_n+\bar\lambda T_n|}{|\lambda S_{n-1}+\bar\lambda T_{n-1}|}\ge\lambda\frac{|S_n|}{|S_{n-1}|}+\bar\lambda\frac{|T_n|}{|T_{n-1}|}\tag{16.144}$$
The author states that simple examples show $|K_n|/|K_{n-p}|$ is not necessarily concave for $p\ge2$. (pp. 507–508)

**Overall summary box (p. 508):** lists the book's key formulas: entropy, relative entropy, mutual information, $D\ge0$, AEP, $H\le L^*<H+1$, $K(x)$, capacity, $R<C$ possible / $R>C$ not, Gaussian capacity $\frac12\log(1+P/N)$, rate distortion, doubling rate.

**Historical notes (p. 509):** the entropy power inequality was stated by Shannon; the first formal proofs are due to Stam and Blachman; the unified proof of the entropy power and Brunn–Minkowski inequalities is in Dembo; most of the matrix inequalities were derived by information-theoretic methods by Cover and Thomas; some of the subset entropy-rate inequalities are in Han.

## Toy example (ours, not from the text)
Take $K=\begin{pmatrix}2&1\\1&2\end{pmatrix}$ (positive definite, Toeplitz), $n=2$.
- $|K|=2\cdot2-1\cdot1=3$. Hadamard (16.104): $3\le K_{11}K_{22}=4$ ✓.
- $\sigma_1^2=|K|/|K(2)|=3/2=1.5$; likewise $\sigma_2^2=1.5$. Corollary (16.114): $4\ge3\ge1.5\cdot1.5=2.25$ ✓.
- Thm 16.8.4: $S_1=\frac12\operatorname{tr}K=2$, $S_2=|K|^{1/2}=\sqrt3\approx1.732$; $2\ge1.732$ ✓.
- Thm 16.8.5: $Q_1=(1.5\cdot1.5)^{1/2}=1.5\le Q_2=|K|^{1/2}\approx1.732$ ✓.
- Entropy view (nats), $\mathbf X\sim\mathcal N(0,K)$: $h_1^{(2)}=\frac12\ln2\pi e+\frac12\ln2$ (each $X_i$ has variance 2) $=\frac12\ln2\pi e+0.3466$. $h_2^{(2)}=\frac12\ln2\pi e+\frac14\ln3=\frac12\ln2\pi e+0.2747$. So $h_1\ge h_2$ as Thm 16.5.1 says; the gap $0.0719$ is the dependence between $X_1,X_2$ per symbol.
- Toeplitz (16.115): $|K_1|=2\ge|K_2|^{1/2}=1.732$ ✓.

## Concepts
- [[jensen-inequality]] (new) — $f(EX)\le Ef(X)$ for convex $f$; the root of many inequalities here (p. 482)
- [[log-sum-inequality]] (new) — $\sum a_i\log(a_i/b_i)\ge(\sum a_i)\log(\sum a_i/\sum b_i)$ (p. 483)
- [[entropy-H(X)]] — $-\sum p\log p$, bounded by $\log|\mathcal X|$ (p. 483)
- [[chain-rule]] — $H(X_1..X_n)=\sum H(X_i|\text{past})\le\sum H(X_i)$ (p. 483)
- [[joint-and-conditional-entropy]] — conditioning reduces entropy; used in every proof of Sec. 16.5, 16.8–16.9 (p. 483)
- [[relative-entropy-KL-divergence]] — $D(p\|q)\ge0$ with equality iff $p=q$; stronger than $\mathcal L_1$ distance (pp. 484, 489)
- [[mutual-information-I(X;Y)]] — $D(p(x,y)\|p(x)p(y))\ge0$, zero iff independent (p. 484)
- [[differential-entropy]] — $-\int f\log f$; may be negative; Gaussian maximises it at given covariance (pp. 485, 488)
- [[fanos-inequality]] — $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ (p. 488)
- [[method-of-types]] (new) — counting bounds on types and type classes (p. 490)
- [[han-subset-entropy-inequalities]] (new) — monotonicity of average entropy per element over $k$-subsets, conditional and unconditional (pp. 491–493)
- [[fisher-information]] — here $J(X)=\int f(\partial_x\ln f)^2dx$ for a location family (p. 494)
- [[cramer-rao-bound]] (new) — variance of unbiased estimator $\ge1/J$ (p. 494)
- [[de-bruijn-identity]] (new) — $\partial_th_e(X+\sqrt tZ)=\frac12J(X+\sqrt tZ)$ (p. 495)
- [[entropy-power-inequality]] (new) — $2^{2h(X+Y)/n}\ge2^{2h(X)/n}+2^{2h(Y)/n}$ (p. 496)
- [[brunn-minkowski-inequality]] (new) — $[\mu(A+B)]^{1/n}\ge\mu(A)^{1/n}+\mu(B)^{1/n}$ (pp. 498, 501)
- [[renyi-entropy]] (new) — $h_r=\frac1{1-r}\log\int f^r$; $r\to1$ Shannon, $r\to0$ log support volume (p. 499)
- [[maximum-entropy-principle]] — Gaussian maximises $h$ for fixed covariance (p. 488)
- [[determinant-inequalities]] (new) — Ky Fan, Hadamard, Szász, Minkowski, Bergström proved via Gaussian entropy (pp. 501–508)

## Canonical instances
- [[gaussian-maxent-bound]] — $h(\mathbf X)\le\frac12\log(2\pi e)^n|K|$ (p. 488)
- [[hadamard-inequality]] — $|K|\le\prod K_{ii}$ via independence bound on entropy (p. 502)
- [[toeplitz-determinant-monotonicity]] — stationary-process entropy rate analogue for $|K_k|^{1/k}$ (p. 504)
- [[sphere-set-sum]] — two unit spheres sum to radius 2 (p. 498)
- [[cesaro-limit-entropy-rate]] — $\lim h(X^n)/n=\lim h(X_n|X^{n-1})$ used for determinants (p. 505)

## Bridges (candidates)
- [same-math] Entropy power inequality ↔ Matrix theory: Minkowski determinant inequality (via Gaussians, p. 505).
- [same-math] Brunn–Minkowski inequality ↔ Rényi order $r=0$ case of the same inequality (p. 501).
- [structural-analogy] Entropy power of a density ↔ Geometry: $n$th-root of volume of support (p. 501).
- [same-math] Cramér–Rao bound ↔ Statistics: variance lower bound by inverse Fisher information (p. 494).
- [structural-analogy] Han's subset inequalities ↔ Matrix theory: Szász's product-of-minors inequality (p. 503).

## Questions this raises
- Why does the extremal object (normal / sphere) appear in both the entropy power inequality and Brunn–Minkowski? What does the "$r$" interpolation mean?
- The proof of $s'(t)\ge0$ in Stam's argument is only outlined: how are $f(t),g(t)$ chosen?
- Why does concavity of $|K_n|/|K_{n-p}|$ fail for $p\ge2$ (the text says "simple examples show")?
- How do the bounds relate to entropy rates of stationary processes in practice?

## Exercises worth doing
- Ex. 1 (p. 509) — $|K_1+K_2|\ge|K_1|$ for positive definite matrices — difficulty: easy
- Ex. 2 (p. 509) — Ky Fan inequality for ratios of determinants (16.145) — difficulty: hard

## Reading notes
- The PDF is the 1991 first edition (title page: Copyright 1991 John Wiley & Sons, Print ISBN 0-471-06259-6), not the 2006 second edition cited in the metadata; chapter content may differ.
- Printed = pdf − 22 (pdf 504 = printed 482).
- OCR: the text layer is heavily garbled on equations. I checked those with page images where supplied. For printed p. 494 (pdf 516) no image was provided; (16.54)–(16.56) are partly unreadable and I reconstructed $J(X)$ from the readable lines.
- (16.28) is garbled in the text layer (it is printed on p. 489). I wrote out the step from (16.27) to (16.29) myself and marked it as an added step.
- In (16.115) a stray "0" appears before the dots; this seems an OCR or typesetting artefact.
- Stam's (16.74) is printed with exponent $2h$ (no $2/n$); it appears to be the scalar case, with the vector case "by induction".
- Table 16.1 (pp. 486–487) is only sampled here; Chapter 16 has no solved exercises, only two problems (p. 509).
