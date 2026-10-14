---
id: polyanskiy-2025-information/ch08-f-p2
work: polyanskiy-2025-information
unit: "Chapter 7 (printed numbering), part 2/2: §7.8 end, §7.9–§7.14* of f-divergences"
pages: 136–157
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# f-divergences (part 2/2): empirical distributions, local expansions, Rényi, variational forms

## L0 — One line
For nearby distributions most f-divergences behave like (f''(1)/2)·χ², with Fisher information as the coefficient in parametric families, and every f-divergence has a dual form as a supremum over test functions built from the convex conjugate of f.

## L1 — The gist (≤ 120 words)
This part asks how f-divergences behave in three settings. First, how fast an empirical distribution approaches the true one: the expected KL cost is controlled, up to a factor of two, by χ²-information. Second, for nearby distributions: under regularity conditions, most f-divergences are locally quadratic with coefficient f''(1)/2 times χ², and in parametric families the quadratic coefficient is set by Fisher information. Third, global structure: Rényi divergences add over product distributions, and every f-divergence is a supremum over test functions built from a convex conjugate. These facts feed estimation, testing and GAN training.

**Prerequisites:** KL divergence, χ², Hellinger and the definition $D_f(P\|Q)=\int dQ\, f(dP/dQ)$ (part 1); Jensen's inequality; dominated convergence and Fatou's lemma; Taylor expansion with integral remainder; $o(\cdot)$, $O(\cdot)$, $\omega(\cdot)$ (ω(1/n) = decays slower than 1/n); convex conjugates (re-defined in §7.13); DPI (data-processing inequality). Weak lower semicontinuity and tensorization are explained in L3.

## L2 — Key ideas
- **Empirical distribution.** For any channel, $\mathbb E[D(P_{Y|X}\circ\hat P_n\|P_Y)]\le\log(1+I_{\chi^2}(X;Y)/n)$ and $\liminf n\,\mathbb E[\cdot]\ge\frac{\log e}{2}I_{\chi^2}$. So the rate is $O(1/n)$ iff $I_{\chi^2}<\infty$ (p. 136–137).
- **Plug-in entropy estimator** has a bias equal to $-\mathbb E\,D(\hat P_n\|P_X)$. The bound (7.58) does not vanish when the alphabet has size $\Theta(n)$, so one must de-bias or use other techniques (p. 137–138).
- **Local χ²-likeness.** If $\chi^2(P\|Q)<\infty$ and $f''$ is bounded at infinity, then $D_f(\bar\lambda Q+\lambda P\|Q)\sim\frac{f''(1)}2\lambda^2\chi^2(P\|Q)$ (p. 139).
- **Fisher information.** Under regularity conditions, $\chi^2(P_t\|P_0)=J_F(0)t^2+o(t^2)$ and $D=\frac{\log e}2J_F(0)t^2+o(t^2)$. For every $f$ with $f''$ continuous, $\liminf D_f/t^2\ge\frac{f''(1)}2J_F(0)$ (p. 140–142).
- **Failure of absolute continuity.** Location families with compact support can have $P_t\not\ll P_0$, so $\chi^2$ and $D$ are infinite for $t>0$. Hellinger and a modified $\chi^2$ still expand quadratically, with a "Fisher defect" term (p. 143–144).
- **Rényi divergences** $D_\lambda$ are monotone transforms of f-divergences, satisfy DPI, have a chain rule, and tensorize over products. This gives (7.80)–(7.83) (p. 145–146).
- **Variational representation.** $D_f(P\|Q)=\sup_g \mathbb E_P[g]-\mathbb E_Q[f^*_{\rm ext}(g)]$. This yields the $\chi^2$ test-statistic form (7.91), the Jensen–Shannon form behind GANs, and weak lower semicontinuity (p. 147–150).
- **Donsker–Varadhan** cannot come from (7.87) because its $Q$-term is linear in $Q$. Theorem 7.27 uses a different conjugate and recovers it exactly (p. 150–151).
- **Huber's sup-form of Fisher information** can be anticipated by combining the sup-form of $\chi^2$ with its local expansion (p. 151–152).

## L3 — Walkthrough

### End of §7.8 (proof of (7.52) for $I_{\rm SKL}$)
The proof of (7.52) is cut at the start of this part. (7.52) itself is stated before this part.
- Rewritten condition: $\sum_{x,x'}P_X(x)P_X(x')\sum_y P_Y(y)\log\frac{P_{Y|X}(y|x)}{P_{Y|X}(y|x')}=0$ (7.53) (p. 136).
- By definition $I_{\rm SKL}(X;Y)=\sum_{x,y}[P_{X,Y}-P_XP_Y]\log\frac{P_{X,Y}}{P_XP_Y}$ (p. 136).
- Since $P_{X,Y}$ and $P_XP_Y$ have the same marginals, $\log\frac{P_{X,Y}}{P_XP_Y}$ can be replaced by $\log\frac{P_{Y|X}(y|x)}{f(y)}$ for any $f$. Choose $f(y)=P_{Y|X}(y|x')$ (p. 136).
- Average over $P_X(x')$ and use (7.53) to remove the second term, which gives (7.52) (p. 136).

### §7.9 Empirical distribution and χ²-information
Setup: $X_i\overset{\rm iid}\sim P_X$, $\hat P_n=\frac1n\sum_i\delta_{X_i}$, $P_Y=P_{Y|X}\circ P_X$. $P_{Y|X}\circ\hat P_n$ is a random output distribution. If $P_{Y|X=x}=\varphi(\cdot-x)$, it is a kernel density estimator (KDE) (p. 136).

Since $\mathbb E[P_{Y|X}\circ\hat P_n]=P_Y$ (p. 136):
$$\mathbb E[D(P_{Y|X}\circ\hat P_n\|P_X)]=D(P_Y\|P_X)+\mathbb E[D(P_{Y|X}\circ\hat P_n\|P_Y)].$$
The first term is the bias, which grows with the bandwidth of $\varphi$. The second is the variability, which shrinks with it. The second is pinned down within a factor of two by $I_{\chi^2}$ (p. 136).

**Proposition 7.17** (p. 136–137):
$$\mathbb E[D(P_{Y|X}\circ\hat P_n\|P_Y)]\le\log\Big(1+\tfrac1n I_{\chi^2}(X;Y)\Big)\tag{7.54}$$
$$\liminf_{n\to\infty} n\,\mathbb E[D(P_{Y|X}\circ\hat P_n\|P_Y)]\ge\tfrac{\log e}{2}I_{\chi^2}(X;Y)\tag{7.55}$$
So the quantity is $O(1/n)$ if $I_{\chi^2}<\infty$ and $\omega(1/n)$ otherwise. Section 25.4* extends this: about $n=\exp\{I(X;Y)+K\}$ observations suffice for $D=e^{-O(K)}$ in many cases (p. 137).

*Proof.*
- A simple calculation gives $\mathbb E[\chi^2(P_{Y|X}\circ\hat P_n\|P_Y)]=\frac1n I_{\chi^2}(X;Y)$. Then (7.34) (not in this part) and Jensen give (7.54) (p. 137).
- Lower bound: draw $\bar X$ uniformly from $\{X_1,\dots,X_n\}$ and let $\bar Y$ be the channel output. Then $\mathbb E[D(P_{Y|X}\circ\hat P_n\|P_Y)]=I(X^n;\bar Y)$ (7.56) (p. 137).
- By (6.2), $I(X^n;\bar Y)\ge\sum_i I(X_i;\bar Y)=nI(X_1;\bar Y)$ (p. 137).
- Finally $I(X_1;\bar Y)=D\big(\frac{n-1}nP_XP_Y+\frac1nP_{X,Y}\,\big\|\,P_XP_Y\big)$. The local expansion of KL (Prop. 2.21) gives (7.55) (p. 137).

**Corollary 7.18** (identity channel $Y=X$, $P_X$ discrete with support $\mathcal X$; $I_{\chi^2}(X;X)=|\mathcal X|-1$) (p. 137):
- If $\mathcal X$ is infinite, $\lim_n n\,\mathbb E[D(\hat P_n\|P_X)]=\infty$ (7.57).
- Otherwise $\mathbb E[D(\hat P_n\|P_X)]\le\log\big(1+\frac{|\mathcal X|-1}{n}\big)\le\frac{\log e}{n}(|\mathcal X|-1)$ (7.58).

**Remark 7.9.** For fixed $P_X$ the tight limit is $\lim_n n\,\mathbb E[D(\hat P_n\|P_X)]=\frac{\log e}2(|{\rm supp}(P_X)|-1)$ (7.59). See Lemma 13.2 (p. 138).

**Entropy estimation** (p. 138). The plug-in estimator is $\hat H_{\rm emp}=H(\hat P_n)$, with bias $\mathbb E[\hat H_{\rm emp}]-H(P_X)=-\mathbb E[D(\hat P_n\|P_X)]$, so it is an underestimate. For fixed $P_X$ it is known to be consistent even on countably infinite alphabets, but the rate can be arbitrarily slow, in line with (7.57). For alphabet size $\Theta(n)$ the bound (7.58) does not vanish. The text says this is tight, e.g. for the uniform distribution. Then one must de-bias, e.g. via (7.59), or use other techniques (Section 29.4) (p. 138).

*Intuition note.* Each sample point adds noise to the empirical distribution. The total KL error is about $\frac{\log e}{2n}$ per "degree of freedom", and $\chi^2$-information counts those degrees of freedom. If $\chi^2$-information is infinite (infinite alphabet), no $1/n$ rate is possible.

### §7.10 Most f-divergences are locally χ²-like
**Theorem 7.19.** Suppose $D_f(P\|Q)<\infty$ and $f'(1)$ exists. Then
$$\lim_{\lambda\to0}\tfrac1\lambda D_f(\lambda P+\bar\lambda Q\|Q)=(1-P[{\rm supp}(Q)])\,f'(\infty),$$
with $0\cdot\infty=0$ (p. 138).

**Remark 7.10.** Swapping the arguments gives another f-divergence with $f(x)$ replaced by $xf(1/x)$, so no separate theorem is needed for $D_f(Q\|\lambda P+\bar\lambda Q)$ (p. 138).

*Proof* (p. 138).
- WLOG $f(1)=f'(1)=0$ and $f\ge0$.
- Decompose $P=\mu P_1+\bar\mu P_0$ with $P_0\perp Q$ and $P_1\ll Q$. Then
$$\tfrac1\lambda D_f(\lambda P+\bar\lambda Q\|Q)=\bar\mu f'(\infty)+\int dQ\,\tfrac1\lambda f\Big(1+\lambda\big(\mu\tfrac{dP_1}{dQ}-1\big)\Big).$$
- For each real $t$, $g(\lambda)=f(1+\lambda t)$ is positive and convex, so $\frac1\lambda g(\lambda)$ decreases monotonically to $g'(0)=0$ as $\lambda\searrow0$.
- At $\lambda=1$ the integrand is $Q$-integrable, so dominated convergence applies.

**Theorem 7.20.** Let $f$ be twice continuously differentiable on $(0,\infty)$ with $\limsup_{x\to+\infty}f''(x)<\infty$. If $\chi^2(P\|Q)<\infty$, then $D_f(\bar\lambda Q+\lambda P\|Q)<\infty$ for all $0\le\lambda<1$ and
$$\lim_{\lambda\to0}\tfrac1{\lambda^2}D_f(\bar\lambda Q+\lambda P\|Q)=\tfrac{f''(1)}2\chi^2(P\|Q).\tag{7.60}$$
If $\chi^2(P\|Q)=\infty$ and $f''(1)>0$, then $D_f(\bar\lambda Q+\lambda P\|Q)=\omega(\lambda^2)$ (p. 139).

**Remark 7.11.** The conditions cover $D$, $D_{\rm SKL}$, $H^2$, JS, LC and all Rényi divergences of order $\lambda<2$ (with $f(x)=\frac1{\lambda-1}(x^\lambda-1)$). A similar result holds when $f''(x)\to\infty$ as $x\to+\infty$ (e.g. Rényi with $\lambda>2$), but then extra assumptions are needed for dominated convergence (often just $D_f(P\|Q)<\infty$) (p. 139).

*Proof* (p. 139–140).
- $\chi^2<\infty$ forces $P\ll Q$, so (7.1) can be used. WLOG $f(1)=f'(1)=0$, since adding a multiple of $(x-1)$ to $f$ does not change $D_f$.
- Taylor: $f(1+u)=u^2\int_0^1(1-t)f''(1+tu)\,dt$. With $u=\lambda\frac{P-Q}{Q}$:
$$D_f(\bar\lambda Q+\lambda P\|Q)=\int dQ\int_0^1dt\,(1-t)\lambda^2\Big(\tfrac{P-Q}{Q}\Big)^2f''\Big(1+t\lambda\tfrac{P-Q}Q\Big).\tag{7.61}$$
- Let $C_\epsilon=\sup_{x\ge\epsilon}|f''(x)|<\infty$. Since $\frac{P-Q}Q\ge-1$, the integrand is non-negative and bounded by $\big(\frac{P-Q}Q\big)^2C_{1-\lambda}$ (7.62). This is integrable over $dQ\times{\rm Leb}[0,1]$ by $\chi^2<\infty$ and Fubini (non-negativity). Hence $D_f<\infty$.
- Divide (7.61) by $\lambda^2$. The integrand is dominated by (7.62), so dominated convergence (step (a)) gives $\int_0^1dt(1-t)\int dQ\big(\frac{P-Q}Q\big)^2f''(1)=\frac{f''(1)}2\chi^2(P\|Q)$. Here $\int_0^1(1-t)dt=\frac12$ (added step).
- If $\chi^2=\infty$ and $P\ll Q$: replace "=" in (a) by "≥" using Fatou's lemma.
- If $P\not\ll Q$: write $P=\mu P_1+\bar\mu P_0$ with $P_1\ll Q$, $P_0\perp Q$, and $\lambda_1=\frac{\lambda\mu}{1-\lambda\bar\mu}$. By (7.2), $D_f(\lambda P+\bar\lambda Q\|Q)=(1-\lambda\bar\mu)D_f(\lambda_1P_1+\bar\lambda_1Q\|Q)+\lambda\bar\mu D_f(P_0\|Q)\ge\lambda\bar\mu D_f(P_0\|Q)$. By Prop. 7.2, $D_f(P_0\|Q)>0$ unless $f(x)=c(x-1)$. Since $f''(1)>0$ excludes that, and $\bar\mu>0$ when $P\not\ll Q$, the lower bound is of order $\lambda$ (added step: this is why it is $\omega(\lambda^2)$) (p. 140).

*Intuition note.* Mixing a small amount $\lambda$ of $P$ into $Q$ makes a small perturbation of relative size $\lambda(P-Q)/Q$. Any smooth $f$ is then well approximated by its second-order Taylor term, which is $\chi^2$ up to the factor $f''(1)/2$. A part of $P$ outside the support of $Q$ is different: it costs first order in $\lambda$.

### §7.11 f-divergences in parametric families: Fisher information
For the Gaussian location model $P_t=\mathcal N(t,1)$, the identities of §7.7 give, as $t\to0$ (p. 140; LC read from the page image):
$$\mathrm{TV}(P_t,P_0)=\tfrac{|t|}{\sqrt{2\pi}}+o(|t|),\quad H^2=\tfrac{t^2}4+o(t^2),\quad\chi^2=t^2+o(t^2),$$
$$D(P_t\|P_0)=\tfrac{t^2}{2\log e}+o(t^2)\ \text{(as printed)},\quad \mathrm{LC}=\tfrac14t^2+o(t^2).$$
All except TV are quadratic in $t$. The coefficient is the Fisher information at $t=0$ (p. 140).

**Definition 7.21 (regularity at $t=0$)** for a family $P_t$, $t\in[0,\tau)$ (p. 140–141):
- (a) $P_t(dx)=p_t(x)\mu(dx)$ for a fixed measure $\mu$ and measurable $(t,x)\mapsto p_t(x)\in\mathbb R_+$.
- (b$_0$) There is a measurable $\dot p_s(x)$ such that for $\mu$-a.e. $x_0$, $\int_0^\tau|\dot p_s(x_0)|ds<\infty$ and
$$p_t(x_0)=p_0(x_0)+\int_0^t\dot p_s(x_0)ds,\tag{7.63}$$
and $\lim_{t\searrow0}\dot p_t(x_0)=\dot p_0(x_0)$.
- (b$_1$) $\dot p_t(x)=0$ whenever $p_0(x)=0$, and $\int_{\mathcal X}\mu(dx)\sup_{0\le t<\tau}\frac{(\dot p_t(x))^2}{p_0(x)}<\infty$ (7.64).
- (c$_0$) The same as (b$_0$) for $h_t=\sqrt{p_t}$: $h_t(x_0)=\sqrt{p_0(x_0)}+\int_0^t\dot h_s(x_0)ds$ (7.65), with $\dot h_t\to\dot h_0$.
- (c$_1$) $\{(\dot h_t)^2:t\in[0,\tau)\}$ is uniformly $\mu$-integrable.

**Remark 7.12.** (c$_1$) is implied by the stronger $\int\mu(dx)\sup_{0\le t<\tau}(\dot h_t(x))^2<\infty$ (7.66). If $h_t$ is also continuously differentiable, (c$_1$) is equivalent to continuity of $t\mapsto J_F(t)\triangleq4\int\mu(dx)(\dot h_t(x))^2$ (7.67) (p. 141).

**Theorem 7.22.** Under (a), (b$_0$), (b$_1$):
$$\chi^2(P_t\|P_0)=J_F(0)t^2+o(t^2)\tag{7.68}$$
$$D(P_t\|P_0)=\tfrac{\log e}2J_F(0)t^2+o(t^2)\tag{7.69}$$
where $J_F(0)=\int_{\mathcal X}\mu(dx)\frac{(\dot p_0(x))^2}{p_0(x)}<\infty$ (p. 141).

*Proof of (7.68)* (p. 141).
- By (b$_1$), $p_0(x_0)=0$ implies $\dot p_t(x_0)=0$ and so $p_t(x_0)=0$ for all $t$. So restrict integrals to $\{p_0>0\}$.
- Using (7.63), $p_t-p_0=t\int_0^1du\,\dot p_{tu}$, so
$$\tfrac1{t^2}\chi^2(P_t\|P_0)=\tfrac1{t^2}\int\mu(dx)\tfrac{(p_t-p_0)^2}{p_0}=\int\mu(dx)\int_0^1du_1\int_0^1du_2\tfrac{\dot p_{tu_1}(x)\dot p_{tu_2}(x)}{p_0(x)}\ \ (a).$$
- As $t\to0$, $\dot p_{tu_1}\dot p_{tu_2}\to\dot p_0^2$ pointwise. The integrand is bounded by $\sup_{0\le t<\tau}\frac{(\dot p_t)^2}{p_0}$, integrable by (7.64). Dominated convergence on (a) gives (7.68).

*Proof of (7.69), first a lower bound valid for every twice continuously differentiable f, then KL* (p. 142).
- For any $f$ twice continuously differentiable (without (7.64)):
$$\liminf_{t\to0}\tfrac1{t^2}D_f(P_t\|P_0)\ge\tfrac{f''(1)}2J_F(0).\tag{7.70}$$
- Like (7.61):
$$D_f(P_t\|P_0)=\int_0^1dz(1-z)\,\mathbb E_{X\sim P_0}\Big[f''\Big(1+z\tfrac{p_t-p_0}{p_0}\Big)\Big(\tfrac{p_t-p_0}{p_0}\Big)^2\Big].\tag{7.71}$$
- Divide by $t^2$. By (b$_0$), $\frac{p_t-p_0}{tp_0}\to\frac{\dot p_0}{p_0}$ a.s., so the integrand tends to $f''(1)(\dot p_0/p_0)^2$. Fatou's lemma gives (7.70).
- For KL ($f=x\log x$), (7.71) becomes
$$\tfrac1{t^2}D(P_t\|P_0)=(\log e)\int_0^1dz\,\mathbb E_{P_0}\Big[\tfrac{1-z}{1+z\frac{p_t-p_0}{p_0}}\Big(\tfrac{p_t-p_0}{tp_0}\Big)^2\Big].\tag{7.72}$$
- The first fraction lies between 0 and 1. The second factor is bounded by $\sup_{0<t<\tau}(\dot p_t/p_0)^2$, which is $P_0$-integrable by (b$_1$). Dominated convergence gives $\lim\frac1{t^2}D=(\log e)\int_0^1dz\,\mathbb E_{P_0}[(1-z)(\dot p_0/p_0)^2]=\frac{\log e}2J_F(0)$ (using $\int_0^1(1-z)dz=\frac12$, added step).

**Remark 7.13** (multi-dimensional). $J_F(\theta)\triangleq\int\mu(dx)\nabla_\theta\sqrt{p_\theta(x)}\,\nabla_\theta\sqrt{p_\theta(x)}^{\top}$ (7.73). Then $\chi^2(P_t\|P_0)=t^\top J_F(0)t+o(\|t\|^2)$ and similarly for (7.69), as in (2.34). Theorem 7.22 covers e.g. smooth subfamilies of exponential families (take $\mu=P_0$, $p_0\equiv1$), but not everything (p. 142).

*Intuition note.* Locally, a smooth family looks like a straight line in "$\sqrt p$ space". Squared distances along it grow like $t^2$ times the squared speed, and that squared speed is the Fisher information. TV is the exception in the Gaussian example: it grows like $|t|$ (p. 140).

**Example 7.1 (location families with compact support)** (p. 142–143). A scalar location family has $\mathcal X=\mathbb R$, $\mu={\rm Leb}$, $p_t(x)=p_0(x-t)$. For $\alpha>-1$, take $p_0(x)=C_\alpha x^\alpha$ on $[0,1]$, $C_\alpha(2-x)^\alpha$ on $[1,2]$, and $0$ otherwise ($C_\alpha$ from normalization).
- (7.64) fails. $\chi^2(P_t\|P_0)$ and $D(P_t\|P_0)$ are infinite for $t>0$ since $P_t\not\ll P_0$. Yet $J_F(0)<\infty$ whenever $\alpha>1$.
- Hellinger as $t\to0$ (7.74): $H^2(P_t,P_0)=\Theta(t^{1+\alpha})$ for $0\le\alpha<1$; $\Theta(t^2\log\frac1t)$ for $\alpha=1$; $\Theta(t^2)$ for $\alpha>1$.
- Footnote 5 (p. 143): the optimal estimator of $t$ from $n$ iid samples has precision $\delta_n^*$ solving $H^2(P_{\delta_n^*},P_0)\asymp\frac1n$. For $\alpha<1$ this gives $\delta_n^*\asymp n^{-1/(1+\alpha)}$, notably better than the empirical mean ($n^{-1/2}$). For $\alpha=\frac12$ this was noted by D. Bernoulli in 1777 as a consequence of his newly proposed maximum likelihood estimation.
- Condition (c$_1$) holds for all $\alpha>1$, while the stronger (7.66) only applies to $\alpha\ge2$ (p. 143).

**Theorem 7.23.** Under (a), (c$_0$), (c$_1$), with $J_F(0)=4\int\dot h_0^2d\mu<\infty$ and **Fisher defect** $J^\#(0)=\int\dot h_0^2\mathbf 1\{h_0=0\}d\mu$:
$$\chi^2(P_t\|\bar\epsilon P_0+\epsilon P_t)=t^2\bar\epsilon^2\Big(J_F(0)+\tfrac{1-4\epsilon}\epsilon J^\#(0)\Big)+o(t^2),\ \ \forall\epsilon\in(0,1)\tag{7.75}$$
$$H^2(P_t,P_0)=\tfrac{t^2}4J_F(0)+o(t^2)\tag{7.76}$$
(p. 143).

**Example 7.2 (on Fisher defect)** (p. 144).
- If $t\mapsto h_t(x)$ is differentiable on a two-sided neighbourhood $(-\tau,\tau)$, then $h_0(x)=0$ is a local minimum, so $\dot h_0(x)=0$ and $J^\#=0$.
- For other families $J^\#\ne0$, even when $p_t$ is smooth on $(-\tau,\tau)$ but $h_t$ is not. Take $P_t={\rm Ber}(t^2)$: $\chi^2(P_t\|\bar\epsilon P_0+\epsilon P_t)=t^2\frac{\bar\epsilon^2}\epsilon+O(t^4)$ and $H^2(P_t,P_0)=2(1-\sqrt{1-t^2})=t^2+O(t^4)$.
- With counting measure: $h_t(0)=\sqrt{1-t^2}$, $h_t(1)=|t|$. $\dot h_t(0)=\frac{-t}{\sqrt{1-t^2}}$; $\dot h_t(1)={\rm sign}(t)$ for $t\ne0$, and $1$ at $t=0$ "just as an agreement".
- On $[0,\tau)$, conditions (a), (c$_0$), (c$_1$) hold. $J_F(0)=4$, $J^\#(0)=1$, and (7.75), (7.76) recover the correct expansions.
- Densities: $p_t(0)=1-t^2$, $p_t(1)=t^2$, $\dot p_t(0)=-2t$, $\dot p_t(1)=2t$; $p_t$ is smooth on $(-\tau,\tau)$. But $\mathbb E_{X\sim P_t}[(\dot p_t/p_t)^2]$ equals $0$ at $t=0$ and $4+\frac{4t^2}{1-t^2}$ for $t\ne0$. It is discontinuous at $0$ and does not match $J_F(0)$, so it gives wrong small-$t$ behaviour for $\chi^2$ and $H^2$.
- Advice: restrict to families with $t\mapsto h_t(x)$ continuously differentiable on $(-\tau,\tau)$ (p. 144).

### §7.12 Rényi divergences and tensorization
**Definition 7.24.** For $\lambda\in\mathbb R\setminus\{0,1\}$,
$$D_\lambda(P\|Q)\triangleq\tfrac1{\lambda-1}\log\mathbb E_Q\Big[\Big(\tfrac{dP}{dQ}\Big)^\lambda\Big],$$
where $\mathbb E_Q[(dP/dQ)^\lambda]$ is understood as ${\rm sign}(\lambda-1)D_f(P\|Q)+1$ with $f(x)={\rm sign}(\lambda-1)(x^\lambda-1)$. The conditional version is $D_\lambda(P_{X|Y}\|Q_{X|Y}|P_Y)\triangleq D_\lambda(P_Y\times P_{X|Y}\|P_Y\times Q_{X|Y})=\frac1{\lambda-1}\log\mathbb E_{Y\sim P_Y}\int(dP_{X|Y}(x))^\lambda(dQ_{X|Y}(a))^{1-\lambda}$ (p. 145).

$D_\lambda$ is not an f-divergence, but it is a monotone transform of one. So it satisfies DPI and the other f-divergence properties (p. 144). Properties listed (p. 145):
- Under mild regularity, $\lim_{\lambda\to1}D_\lambda=D$. $D_2=\log(1+\chi^2)$; $D_{1/2}=-2\log(1-\frac{H^2}2)$.
- $\lambda\mapsto D_\lambda$ is non-decreasing; $\lambda\mapsto(1-\lambda)D_\lambda$ is concave.
- For $\lambda\in[0,1]$, $(P,Q)\mapsto D_\lambda$ is convex. For $\lambda\ge0$, $Q\mapsto D_\lambda$ is convex.
- For $Q$ uniform on $m$ points, $D_\lambda(P\|Q)=\log m-H_\lambda(P)$ (Rényi entropy, (1.4)). At $\lambda=1$ this recovers Theorem 2.2.
- Chain rule:
$$D_\lambda(P_{A,B}\|Q_{A,B})=D_\lambda(P_B\|Q_B)+D_\lambda\big(P_{A|B}\|Q_{A|B}\,\big|\,P_B^{(\lambda)}\big)\tag{7.77}$$
with the $\lambda$-tilting $P_B^{(\lambda)}(b)\triangleq P_B^\lambda(b)Q_B^{1-\lambda}(b)\exp\{-(\lambda-1)D_\lambda(P_B\|Q_B)\}$ (7.78).
- **Tensorization:** $D_\lambda\big(\prod_iP_{X_i}\|\prod_iQ_{X_i}\big)=\sum_iD_\lambda(P_{X_i}\|Q_{X_i})$ (7.79), a simple consequence of (7.77). The text says (citing [310]) that the $D_\lambda$ are the only divergences satisfying DPI and tensorization. Special cases include Hellinger (7.26) and $1+\chi^2\big(\prod_iP_i\|\prod_iQ_i\big)=\prod_i(1+\chi^2(P_i\|Q_i))$.
- Additive bounds for non-product distributions: Ex. I.42, I.43.

**Proposition 7.25.** For product channels $P_{Y^n|X^n}=\prod P_{Y_i|X_i}$ and $Q_{Y^n|X^n}=\prod Q_{Y_i|X_i}$ (all optimizations over all distributions) (p. 146):
$$\inf_{P_{X^n},Q_{X^n}}D_\lambda(P_{Y^n}\|Q_{Y^n})=\sum_{i=1}^n\inf_{P_{X_i},Q_{X_i}}D_\lambda(P_{Y_i}\|Q_{Y_i})\tag{7.80}$$
$$\sup_{P_{X^n},Q_{X^n}}D_\lambda(P_{Y^n}\|Q_{Y^n})=\sum_{i=1}^n\sup_{P_{X_i},Q_{X_i}}D_\lambda(P_{Y_i}\|Q_{Y_i})=\sum_{i=1}^n\sup_{x,x'}D_\lambda(P_{Y_i|X_i=x}\|Q_{Y_i|X_i=x'})\tag{7.81}$$
For collections $\{P_\theta\},\{Q_\theta\}$, with co = convex hull:
$$\inf_{P\in{\rm co}\{P_\theta^{\otimes n}\},\,Q\in{\rm co}\{Q_\theta^{\otimes n}\}}D_\lambda(P\|Q)\ge n\inf_{P\in{\rm co}\{P_\theta\},Q\in{\rm co}\{Q_\theta\}}D_\lambda(P\|Q)\tag{7.82}$$
$$\sup_{P\in{\rm co}\{P_\theta^{\otimes n}\},\,Q\in{\rm co}\{Q_\theta^{\otimes n}\}}D_\lambda(P\|Q)\le n\sup_{P\in{\rm co}\{P_\theta\},Q\in{\rm co}\{Q_\theta\}}D_\lambda(P\|Q)\tag{7.83}$$

**Remark 7.14.** Mnemonic: "mixtures of products are less distinguishable than products of mixtures" (p. 146).

*Proof* (p. 146).
- Second equality of (7.81): $D_\lambda$ is an increasing function of an f-divergence. So the maximum is attained at an extreme point of the probability space, i.e. point masses.
- Main equalities: restrict to product distributions and use (7.79); then use the chain rule. For $n=2$, fix $P_{X^2},Q_{X^2}$. Then $D_\lambda(P_{Y_1|Y_2=y}\|Q_{Y_1|Y_2=y'})\ge\inf_{\tilde P_{X_1},\tilde Q_{X_1}}D_\lambda(\tilde P_{Y_1}\|\tilde Q_{Y_1})$, since $P_{Y_1|Y_2=y}$ is induced by $\tilde P_{X_1}=P_{X_1|Y_2=y}$ (same for $Q$).
- Hence $D_\lambda(P_{Y^2}\|Q_{Y^2})=D_\lambda(P_{Y_2}\|Q_{Y_2})+D_\lambda(P_{Y_1|Y_2}\|Q_{Y_1|Y_2}|P_{Y_2}^{(\lambda)})\ge\sum_{i=1}^2\inf D_\lambda(P_{Y_i}\|Q_{Y_i})$. The sup case is similar.
- (7.82)–(7.83): take $\mathcal X=\Theta$ and restrict to diagonal $P_{X^n},Q_{X^n}$ (all $X_i$ equal with probability 1).

*Intuition note.* Rényi divergences turn products into sums, as KL does, so for a product of $n$ identical factors $D_\lambda$ is exactly $n$ times the single-factor value (7.79). Remark 7.14 gives the mnemonic "mixtures of products are less distinguishable than products of mixtures". The mixture-of-products case arises when iid observations come from a single distribution whose parameter is drawn from a prior, and (7.82)–(7.83) compare the corresponding $D_\lambda$ with $n$ times the single-observation value.

### §7.13 Variational representation of f-divergences
**Convex conjugate** of convex $f:(0,\infty)\to\mathbb R$: $f^*(y)=\sup_{x\in\mathbb R_+}xy-f(x)$, $y\in\mathbb R$ (7.84). ${\rm dom}(f^*)=\{y:f^*(y)<\infty\}$. Properties: (1) $f^*$ is convex (whether or not $f$ is). (2) Biconjugation $(f^*)^*=f$, i.e. $f(x)=\sup_yxy-f^*(y)$, which implies $f(x)+f^*(y)\ge xy$ (p. 147).

For a convex functional $\Psi$ on measures, $\Psi^*(g)=\sup_P\int g\,dP-\Psi(P)$ (7.85). Under appropriate conditions (e.g. finite $\mathcal X$), $\Psi(P)=\sup_g\int g\,dP-\Psi^*(g)$ (7.86) (p. 147).

Extend $D_f$ to signed measures with an extension $f_{\rm ext}:\mathbb R\to\mathbb R\cup\{+\infty\}$ that equals $f$ on $x\ge0$ and is convex. One can always take $f_{\rm ext}=\infty$ for $x<0$. For $f=|x-1|/2$ or $(x-1)^2$ one can take $f_{\rm ext}=f$ (p. 147).

**Theorem 7.26.** With $f^*_{\rm ext}(y)=\sup_{x\in\mathbb R}xy-f_{\rm ext}(x)$:
$$D_f(P\|Q)=\sup_{g:\mathcal X\to{\rm dom}(f^*_{\rm ext})}\mathbb E_P[g(X)]-\mathbb E_Q[f^*_{\rm ext}(g(X))]\tag{7.87}$$
The supremum may be taken over (a) all simple $g$ or (b) all $g$ with $\mathbb E_Q[f^*_{\rm ext}(g(X))]<\infty$. If $P\ll Q$, both also hold for $g:\mathcal X\to\mathbb R$ without restricting to ${\rm dom}(f^*_{\rm ext})$ (p. 148).

Consequences (p. 148):
1. **Convexity.** $D_f$ is a supremum of affine functions of $(P,Q)$, hence convex (proved differently in Theorem 7.5).
2. **Weak lower semicontinuity.** Let $X_i$ be iid Rademacher ($\pm1$). Then $\sum X_i/\sqrt n\to\mathcal N(0,1)$ in distribution, but for all $n$, $D_f(P_{X_1+\dots+X_n\over\sqrt n}\|\mathcal N(0,1))=f(0)+f'(\infty)>0$ (Prop. 7.2), since one is discrete and the other continuous. So only semicontinuity can be hoped for. On a nice space such as Euclidean space, $g$ in (7.87) can be restricted to bounded continuous functions. Then $P_n\xrightarrow{w}P$, $Q_n\xrightarrow{w}Q$ implies $\liminf_nD_f(P_n\|Q_n)\ge D_f(P\|Q)$.
3. **Relation to DPI.** Variational forms extend DPI (see (4.15)). The text suggests, as an exercise, deriving $|P[A]-Q[A]|\le\sqrt{Q[A]\cdot\chi^2(P\|Q)}$ via both DPI and (7.91).

**Example 7.3 (TV and Hellinger)** (p. 149).
- TV: $f=\frac12|x-1|$, $f_{\rm ext}$ the same. $f^*_{\rm ext}(y)=+\infty$ if $|y|>\frac12$ and $y$ if $|y|\le\frac12$. So ${\rm TV}(P,Q)=\sup_{g:|g|\le\frac12}\mathbb E_P[g]-\mathbb E_Q[g]$ (7.88).
- Squared Hellinger: $f^*_{\rm ext}(y)=\frac y{1-y}$ on $y\in(-\infty,1)$. With $h=1-g$: $H^2(P,Q)=2-\inf_{h>0}\mathbb E_P[h]+\mathbb E_Q[\frac1h]$.
- Application: for $f:\mathcal X\to[0,1]$ and $\tau\in(0,1)$, $h=1-\tau f$ satisfies $\frac1h\le1+\frac\tau{1-\tau}f$. Hence $\mathbb E_P[f]\le\frac1{1-\tau}\mathbb E_Q[f]+\frac1\tau H^2(P,Q)$ for all such $f,\tau$.

**Example 7.4 (χ²)** (p. 149). $f=(x-1)^2=f_{\rm ext}$, $f^*_{\rm ext}(y)=y+\frac{y^2}4$.
$$\chi^2(P\|Q)=\sup_g\mathbb E_P[g]-\mathbb E_Q\Big[g+\tfrac{g^2}4\Big]\tag{7.89}$$
$$=\sup_g2\mathbb E_P[g]-\mathbb E_Q[g^2]-1\tag{7.90}$$
(7.90) is not scale-invariant. Setting $g=\lambda h$ and optimizing over $\lambda$ gives
$$\chi^2(P\|Q)=\sup_h\frac{(\mathbb E_P[h]-\mathbb E_Q[h])^2}{{\rm Var}_Q(h)}.\tag{7.91}$$
(Added step: from (7.89), $g=\lambda h$ gives $\lambda(\mathbb E_Ph-\mathbb E_Qh)-\frac{\lambda^2}4\mathbb E_Q[h^2]$. Its maximum over $\lambda$ is $(\mathbb E_Ph-\mathbb E_Qh)^2/\mathbb E_Q[h^2]$. The numerator is unchanged by adding a constant to $h$, and $\mathbb E_Q[(h-c)^2]$ is smallest at $c=\mathbb E_Qh$, giving ${\rm Var}_Q(h)$.)

Interpretation: if a test statistic $h(X)$ has $P$-vs-$Q$ separation of means far exceeding its standard deviation, the hypotheses can be reliably distinguished. (7.91) will be used in Chapter 29 for the Hammersley–Chapman–Robbins bound, its Bayesian version (§29.1.2), and ultimately the Cramér–Rao and van Trees bounds (p. 149).

**Example 7.5 (JS and GANs)** (p. 149–150). $f(x)=x\log\frac{2x}{1+x}+\log\frac2{1+x}$, $f^*(s)=-\log(2-\exp(s))$ on $s\in(-\infty,\log2)$. Then
$$\mathrm{JS}(P,Q)=\sup_{g:\mathcal X\to(-\infty,\log2)}\mathbb E_P[g]+\mathbb E_Q[\log(2-\exp\{g(X)\})],$$
and with $h=\exp\{g\}/2$, as printed: $\mathrm{JS}(P,Q)=\sup_{h:\mathcal X\to(0,1)}\log2+\mathbb E_P[\log h]+\mathbb E_Q[\log(1-h)]$. See Reading notes on the constant.

GAN idea (p. 150): approximate a complicated $P$ on $\mathbb R^d$ by the law of $G(Z)$, with $G:\mathbb R^m\to\mathbb R^d$ and $Z\sim\mathcal N(0,I_m)$. Minimize ${\rm JS}(P,P_{G(Z)})$. By the variational form this is
$$\inf_G\sup_h\mathbb E_{X\sim P}[\log h(X)]+\mathbb E_{Z\sim\mathcal N}[\log(1-h(G(Z)))],$$
where $h$ is called the discriminator (less often, critic). Since $P$ is seen only through iid samples $x_1,\dots,x_n$, replace $\mathbb E_P$ by $\frac1n\sum_i\log h(x_i)$. The infinite-dimensional optimizations over $G$ and $h$ are replaced by neural networks, via alternating gradient ascent/descent steps. The text says variations of this idea produced realistic images, music, videos and 3D scenery.

**Example 7.6 (KL)** (p. 150). $f=x\log x$, $f_{\rm ext}=\infty$ for $x<0$, $f^*(y)=\frac{\log e}e\exp(y)$. So
$$D(P\|Q)=\sup_g\mathbb E_P[g(X)]-(\mathbb E_Q[\exp\{g(X)\}]-1)\log e.\tag{7.92}$$
This is weaker than Donsker–Varadhan, $D(P\|Q)=\sup_g\mathbb E_P[g]-\log\mathbb E_Q[\exp\{g\}]$ (7.93), because for each $g$ its lower bound is smaller. For any $f_{\rm ext}$, DV cannot be obtained from Theorem 7.26, since the second term in (7.87) is always linear in $Q$. Defining $D_f(P\|Q)=\infty$ for non-probability $P$ and taking the conjugate gives a different representation that recovers DV exactly (p. 150).

**Theorem 7.27.** Let $f_{\rm ext}(x)=\infty$ for $x<0$ and $S=\{x:q(x)>0\}$, with $q$ as in (7.2). Then
$$D_f(P\|Q)=f'(\infty)P[S^c]+\sup_g\mathbb E_P[g\mathbf 1_S]-\Psi^*_{Q,P}(g),\tag{7.94}$$
$$\Psi^*_{Q,P}(g)\triangleq\inf_{a\in\mathbb R}\mathbb E_Q[f^*_{\rm ext}(g(X)-a)]+aP[S].$$
If $f'(\infty)=\infty$:
$$D_f(P\|Q)=\sup_g\mathbb E_P[g]-\Psi^*_Q(g),\quad\Psi^*_Q(g)\triangleq\inf_{a\in\mathbb R}\mathbb E_Q[f^*_{\rm ext}(g(X)-a)]+a\tag{7.95}$$
(p. 151).

**Remark 7.15 (Marton's divergence)** (p. 151). Theorem 7.7 gave both sup and inf (coupling) characterizations of TV. The only other known example "to us" is Marton's $D_m(P\|Q)=\int dQ\big(1-\frac{dP}{dQ}\big)_+^2$, an f-divergence with $f(x)=(1-x)_+^2$. Then $D_m(P\|Q)=\inf\{\mathbb E[P[X\ne Y|Y]^2]:X\sim P,Y\sim Q\}$ over couplings ([69, Lemma 8.3]; Ex. I.44). It matters for concentration of measure. Theorem 7.20 does not apply to $D_m$ (no twice continuous differentiability) but does apply to the symmetrized $D_{sm}(P\|Q)=D_m(P\|Q)+D_m(Q\|P)$.

**Fisher information analogues** (p. 151–152).
- Fisher information is expected to inherit monotonicity, DPI and a variational form. The first two can be shown directly (Ex. I.46).
- Huber [220] introduced, for $P\in\mathcal P(\mathbb R)$:
$$J(P)=\sup_h\frac{\mathbb E_P[h'(X)]^2}{\mathbb E_P[h(X)^2]}\tag{7.96}$$
over $h\in C^1_c$ (continuously differentiable, compact support) with $\mathbb E_P[h^2]>0$. Huber showed $J(P)<\infty$ iff $P$ has an absolutely continuous density $p$ with $\int(p')^2/p<\infty$, in which case (7.96) equals the usual (2.40). Footnote 6: $J({\rm Unif}(0,1))=\infty$, via $h(x)=\cos^2\frac{x\pi}\epsilon\mathbf 1\{|x|\le\epsilon/2\}$, $\epsilon\to0$.
- Heuristic (regularity aside): by (7.91) and Taylor, $\chi^2(P_t\|P)=\sup\frac{(\mathbb E[h(X+t)-h(X)])^2}{\mathbb E[h^2(X)]}=\sup\frac{\mathbb E[h'(X)]^2}{\mathbb E[h^2(X)]}t^2+o(t^2)$, and this is $J(P)t^2+o(t^2)$.
- Direct proof: integration by parts and Cauchy–Schwarz give $(\int ph')^2=(\int p'h)^2\le\int h^2p\int(p')^2/p$. The optimal $h$ is the score function $p'/p$ (see [220, Thm 4.2]).

*Intuition note.* Every f-divergence is the best "score" an observer can get from a test function $g$, once the penalty $f^*$ for large $g$ values is paid. Different $f$ give different penalties: for $\chi^2$ it is quadratic, which turns the problem into "signal-to-noise" of a statistic.

### §7.14* Technical proofs
**Proof of Theorem 7.23** (p. 152–154).
- Define $L(t)\triangleq\frac1{\bar\epsilon^2t^2}\chi^2(P_t\|\bar\epsilon P_0+\epsilon P_t)=\frac1{t^2}\int\mu(dx)\frac{(p_t-p_0)^2}{\bar\epsilon p_0+\epsilon p_t}=\frac1{t^2}\int\mu(dx)g(t,x)^2$ (7.97), with $g(t,x)=\frac{p_t-p_0}{\sqrt{\bar\epsilon p_0+\epsilon p_t}}=\varphi(h_t(x);x)$ and $\varphi(h;x)=\frac{h^2-p_0}{\sqrt{\bar\epsilon p_0+\epsilon h^2}}$.
- By (c$_0$), $h_t$ is absolutely continuous. Claim: $\|\varphi(\cdot;x)\|_{\rm Lip}=\sup_{h\ge0}|\varphi'|\le\frac{2-\epsilon}{(1-\epsilon)\sqrt\epsilon}$. So $g(t,x)$ is absolutely continuous in $t$: $g(t,x)=t\int_0^1du\,\dot g(tu,x)$ with $\dot g=\varphi'(h_t)\dot h_t$.
- $\varphi'(h)=2h\frac{h_0^2(1-\frac\epsilon2)+\frac\epsilon2h^2}{(\bar\epsilon h_0^2+\epsilon h^2)^{3/2}}$. Use $\frac h{\sqrt{\bar\epsilon h_0^2+\epsilon h^2}}\le\frac1{\sqrt\epsilon}$ and $\frac{h_0^2(1-\epsilon/2)+\epsilon h^2/2}{\bar\epsilon h_0^2+\epsilon h^2}\le\frac{1-\epsilon/2}{1-\epsilon}$ for the Lipschitz bound.
- $\varphi'(h_0(x);x)=2$ if $h_0(x)>0$, and $\frac1{\sqrt\epsilon}$ if $h_0(x)=0$ (7.98). $\varphi'$ is continuous (for $h_0=0$ it equals $\frac1{\sqrt\epsilon}$ for all $h$). Hence
$$\lim_{s\to0}\dot g(s,x)=\dot h_0(x)\Big(2\cdot\mathbf 1\{h_0>0\}+\tfrac1{\sqrt\epsilon}\mathbf 1\{h_0=0\}\Big).\tag{7.99}$$
- $L(t)=\int\mu(dx)\int_0^1du_1\int_0^1du_2\,\dot g(tu_1,x)\dot g(tu_2,x)$ (7.100). With $|\dot g(s,x)|\le C|\dot h_s(x)|$, Cauchy–Schwarz and (c$_1$) give $\int\mu|\dot g(s_1)\dot g(s_2)|\le C^2\sup_t\int\mu\,\dot h_t^2<\infty$ (7.101). So Fubini applies: $L(t)=\int_0^1\int_0^1G(tu_1,tu_2)$, $G(s_1,s_2)=\int\mu(dx)\dot g(s_1,x)\dot g(s_2,x)$.
- A uniformly square-integrable family $\{f_\alpha\}$ has uniformly integrable products, since $|f_\alpha f_\beta|\le\frac12(f_\alpha^2+f_\beta^2)$. So limits pass inside: $G(tu_1,tu_2)\to G(0,0)=\int\mu\,\dot h_0^2(4\cdot\mathbf 1\{h_0>0\}+\frac1\epsilon\mathbf 1\{h_0=0\})=J_F(0)+\frac{1-4\epsilon}\epsilon J^\#(0)$. ($G$ is bounded, so bounded convergence applies.) This gives (7.75).
- Hellinger: $M(t)\triangleq\frac1{t^2}H^2(P_t,P_0)=\int\mu\int_0^1\int_0^1\dot h_{tu_1}\dot h_{tu_2}$. As above, Fubini applies. $H(s_1,s_2)=\int\mu\,\dot h_{s_1}\dot h_{s_2}$ is bounded and $H(tu_1,tu_2)\to\frac14J_F(0)$. So $\lim M(t)=\frac14J_F(0)$, proving (7.76).
- *Skip path:* carry forward only that $\varphi'$ is bounded and equals $2$ or $1/\sqrt\epsilon$ at $t=0$, which is where the defect term comes from.

**Proof of Theorem 7.6** (the partition-supremum theorem, stated before this part; counterpart of Gelfand–Yaglom–Perez Theorem 4.5) (p. 154–155).
- $D_f(P\|Q)\ge D_f(P_{\mathcal E}\|Q_{\mathcal E})$ is DPI. For the upper bound, reduce to $f\ge0$ (property 6 of Prop. 7.2).
- Define $S={\rm supp}\,Q$, $F_\infty=\{\frac{dP}{dQ}=0\}$, and for $\epsilon>0$, $F_m=\{\epsilon m\le f(\frac{dP}{dQ})<\epsilon(m+1)\}$. Then
$$\epsilon\sum_mmQ[F_m]\le\int_SdQ\,f\Big(\tfrac{dP}{dQ}\Big)\le\epsilon\sum_m(m+1)Q[F_m]+f(0)Q[F_\infty]\le\epsilon\sum_mmQ[F_m]+f(0)Q[F_\infty]+\epsilon.\tag{7.102}$$
- $f$ is increasing on $I_m^+=\{x>1:\epsilon m\le f<\epsilon(m+1)\}$ and decreasing on $I_m^-=\{x\le1:\dots\}$. Split $F_m=F_m^+\cup F_m^-$ accordingly. Then $f\big(\frac{P[F_m^\pm]}{Q[F_m^\pm]}\big)\ge\epsilon m$.
- For the partition $\mathcal E=\{F_0^\pm,\dots,F_n^\pm,F_\infty,S^c,\cup_{m>n}F_m\}$:
$$D_f(P_{\mathcal E}\|Q_{\mathcal E})\ge\epsilon\sum_{m\le n}mQ[F_m]+f(0)Q[F_\infty]+f'(\infty)P[S^c].\tag{7.103}$$
- Cases: if $f(0)Q[F_\infty]=\infty$, both sides are infinite. If $\int_SdQ\,f=\infty$, the sum can be made arbitrarily large. Otherwise pick $n$ with $\sum_{m>n}mQ[F_m]\le\frac12$; then by (7.102), $\epsilon\sum_{m\le n}mQ[F_m]+f(0)Q[F_\infty]\ge\int_SdQ\,f-\frac32\epsilon$. So (7.103) exceeds $D_f(P\|Q)-\frac32\epsilon$.

**Proof of Theorem 7.26** (p. 155–156).
- *Inequality* $\mathbb E_P[g]\le D_f(P\|Q)+\mathbb E_Q[f^*_{\rm ext}(g)]$ (7.104). For $q(x)>0$: $f^*_{\rm ext}(g(x))+f_{\rm ext}(\frac{p(x)}{q(x)})\ge g(x)\frac{p(x)}{q(x)}$. Integrating over $\{q>0\}$ gives (7.105): $\mathbb E_Q[f^*_{\rm ext}(g)]+\int_{q>0}qf_{\rm ext}(p/q)d\mu\ge\mathbb E_P[g\mathbf 1\{q>0\}]$.
- Since $\sup{\rm dom}(f^*_{\rm ext})=\lim_{x\to\infty}f_{\rm ext}(x)/x=f'(\infty)$ (7.106), we have $f'(\infty)P[q=0]\ge\mathbb E_P[g\mathbf 1\{q=0\}]$. Summing gives (7.104).
- *Tightness.* By Theorem 7.6, $D_f(P\|Q)=\sup_{\mathcal E}D_f(P_{\mathcal E}\|Q_{\mathcal E})$, so it suffices to prove (7.87) for finite $\mathcal X$. The sup over partitions combined with the sup over $\mathcal E$-compatible $g$ equals the sup over simple $g$.
- Finite $\mathcal X$: with $S=\{Q>0\}$, show
$$D_f(P\|Q)=\sup_{g:S\to{\rm dom}(f^*_{\rm ext})}\mathbb E_P[g]-\mathbb E_Q[f^*_{\rm ext}(g)]+f'(\infty)P(S^c).\tag{7.107}$$
Write $D_f=\Psi(P)+f'(\infty)P(S^c)$ with $\Psi(P)=\sum_{x\in S}Q(x)f_{\rm ext}(P(x)/Q(x))$, $P$ ranging over signed measures on $S\cong\mathbb R^S$.
- Conjugate: $\Psi^*(g)=\sup_P\sum_xP(x)g(x)-Q(x)\{\sup_{h\in{\rm dom}(f^*_{\rm ext})}\frac{P(x)}{Q(x)}h-f^*_{\rm ext}(h)\}=\sup_P\inf_h\sum_xP(x)(g(x)-h(x))+Q(x)f^*_{\rm ext}(h(x))\overset{(a)}=\inf_h\sup_P\dots$, which equals $\mathbb E_Q[f^*_{\rm ext}(g)]$ if $g:S\to{\rm dom}(f^*_{\rm ext})$ and $+\infty$ otherwise. Step (a) is the minimax theorem (finite $\mathcal X$). Convex duality (7.86) gives (7.107).

**Proof of Theorem 7.27** (p. 156–157).
- *Reduction to simple $g$.* Fix $g$ and $\delta$. There is $a$ with $\mathbb E_Q[f^*_{\rm ext}(g-a)]\pm aP[S]\le\Psi^*_{Q,P}(g)+\delta$ (see Reading notes on the sign). Approximating by simple functions yields simple $\tilde g$ with $\mathbb E_P[\tilde g\mathbf 1_S]\ge\mathbb E_P[g\mathbf 1_S]-\delta$ and $\Psi^*_{Q,P}(\tilde g)\le\Psi^*_{Q,P}(g)+2\delta$. So restricting to simple $g$ does not change the right side of (7.94). By Theorem 7.6, finite $\mathcal X$ suffices.
- *Finite $\mathcal X$.* Let $\Psi(P)=D_f(P\|Q)$ for probability $P$, $+\infty$ otherwise. Then $\Psi^*(g)=\sup_P\sum P g-D_f(P\|Q)$ becomes, by $\sup_P\inf_h\to\inf_h\sup_P$ (a), then (b) taking $\sup_P$ over probability measures as a max over points, then (c) restricting to $h=g-a$ on $S$ (valid since $f^*_{\rm ext}$ is non-decreasing, as printed):
$$\Psi^*(g)=\inf_{a\in\mathbb R}\Big\{\max\Big(a,\max_{x\in S^c}g(x)-f'(\infty)\Big)+\mathbb E_Q[f^*_{\rm ext}(g(X)-a)]\Big\}.$$
- By duality $D_f=\sup_g\mathbb E_P[g]-\Psi^*(g)$. WLOG $g=f'(\infty)+b$ on $S^c$. Interchanging the optimization over $b$ with that over $a$, $\sup_bbP[S^c]-\max(a,b)=-aP[S]$, which recovers (7.94).
- (7.95): if $P[S^c]>0$, both sides are infinite ($\Psi^*_Q$ ignores $g$ outside $S$). Otherwise (7.95) coincides with (7.94).

## Toy example (ours): local χ²-likeness (Theorem 7.20, eq. (7.60))
Take $Q=(\tfrac12,\tfrac12)$ and $P=(1,0)$ on two points. Use natural logs, $f=x\ln x$ (so $D$ is KL in nats, $f''(1)=1$).
- $\chi^2(P\|Q)=\frac{(1-0.5)^2}{0.5}+\frac{(0-0.5)^2}{0.5}=0.5+0.5=1$.
- Mixture $\lambda P+\bar\lambda Q=(0.5+0.5\lambda,\;0.5-0.5\lambda)$. Prediction of (7.60): $\frac{f''(1)}2\lambda^2\chi^2=0.5\lambda^2$.
- $\lambda=0.1$: mixture $(0.55,0.45)$. $D=0.55\ln\frac{0.55}{0.5}+0.45\ln\frac{0.45}{0.5}=0.55\ln1.1+0.45\ln0.9=0.55(0.0953102)+0.45(-0.1053605)=0.052421-0.047412=0.005008$. Prediction: $0.5(0.01)=0.005$. Ratio $\approx1.002$.
- $\lambda=0.2$: mixture $(0.6,0.4)$. $D=0.6\ln1.2+0.4\ln0.8=0.6(0.1823216)+0.4(-0.2231436)=0.109393-0.089257=0.020136$. Prediction: $0.5(0.04)=0.02$. Ratio $\approx1.007$.
- Check with $f=(x-1)^2$ ($f''(1)=2$): $\chi^2(\text{mixture}\|Q)=\sum\frac{(\lambda(P-Q))^2}Q=\lambda^2\chi^2(P\|Q)=0.01$ at $\lambda=0.1$. The formula gives $\frac22(0.01)(1)=0.01$. (Here the expansion is exact.)

The ratio tends to 1 as $\lambda\to0$, as (7.60) says.

## Concepts
- [[f-divergence]] — $D_f(P\|Q)=\int dQ\,f(dP/dQ)$ for convex $f$ with $f(1)=0$; this part studies its local and dual behaviour (p. 138–139, 147)
- [[relative-entropy-kl-divergence]] — $D$ is the case $f=x\log x$; locally $\frac{\log e}2J_F t^2$ (p. 141–142, 150)
- [[chi-square-divergence-and-information]] (new) — $\chi^2(P\|Q)$ and $I_{\chi^2}(X;Y)$; controls empirical-distribution error and is the local model of other f-divergences (p. 136–139)
- [[empirical-distribution-bound]] (new) — $\mathbb E\,D(P_{Y|X}\circ\hat P_n\|P_Y)\le\log(1+I_{\chi^2}/n)$ (p. 136)
- [[fisher-information]] — $J_F(t)=4\int\mu\,\dot h_t^2$, with $J_F(0)=\int\mu\,\dot p_0^2/p_0$ in Theorem 7.22; coefficient of local quadratic behaviour (p. 141)
- [[fisher-defect]] (new) — $J^\#(0)=\int\dot h_0^2\mathbf 1\{h_0=0\}d\mu$; extra term in (7.75) when $h_t$ is non-smooth at $0$ (p. 143)
- [[renyi-divergence]] (new) — $D_\lambda=\frac1{\lambda-1}\log\mathbb E_Q[(dP/dQ)^\lambda]$; monotone transform of an f-divergence, satisfies DPI (p. 145)
- [[tensorization]] (new) — additivity of $D_\lambda$ over product measures (7.79) (p. 145)
- [[convex-conjugate-variational-representation]] (new) — $f^*(y)=\sup_xxy-f(x)$ and $D_f=\sup_g\mathbb E_P g-\mathbb E_Qf^*_{\rm ext}(g)$ (p. 147–148)
- [[plug-in-entropy-estimator]] (new) — $H(\hat P_n)$; its bias is $-\mathbb E\,D(\hat P_n\|P_X)\le0$ (p. 138)
- [[total-variation-distance]] — local behaviour is linear in $t$, unlike the other f-divergences listed there (p. 140); sup form (7.88) (p. 149)

## Canonical instances
- [[gaussian-location-model]] — $P_t=\mathcal N(t,1)$: all listed f-divergences except TV are quadratic in $t$ (p. 140)
- [[compact-support-location-family]] — Example 7.1: $\chi^2$ and $D$ infinite but $H^2=\Theta(t^2)$ for $\alpha>1$ (p. 143)
- [[bernoulli-t-squared-family]] — Example 7.2: ${\rm Ber}(t^2)$ with Fisher defect $1$ and discontinuous $\mathbb E[(\dot p_t/p_t)^2]$ (p. 144)
- [[gan-js-objective]] — Example 7.5: $\inf_G\sup_h$ form of Jensen–Shannon (p. 150)
- [[rademacher-clt-semicontinuity]] — $D_f$ stays $f(0)+f'(\infty)$ while the distributions converge weakly (p. 148)
- [[marton-divergence]] — $f=(1-x)_+^2$ with a coupling inf-form (p. 151)

## Bridges (candidates)
- [same-math] JS variational formula (Example 7.5) ↔ machine learning: the text says this characterization is the basis of the GAN objective.
- [same-math] $\chi^2$ sup-form (7.91) ↔ statistics: the text says it leads to the Hammersley–Chapman–Robbins lower bound (Ch. 29).
- [structural-analogy] Plug-in entropy bias $-\mathbb E\,D(\hat P_n\|P_X)$ ↔ statistics: finite-sample bias of plug-in estimators when the alphabet grows with $n$.
- [structural-analogy] Rényi tensorization ↔ hypothesis testing: the text says Rényi divergence will feature prominently in characterizing optimal error exponents (§16.1).

## Questions this raises
- What does the sharp asymptotic (7.59), $\frac{\log e}2(|{\rm supp}|-1)$, imply for explicit bias corrections of the plug-in entropy estimator (Lemma 13.2, §29.4)?
- When does a non-zero Fisher defect appear in practice, and what does it change in estimation rates?
- Which f-divergences besides TV and Marton's have an inf (coupling) characterization?
- How do the sup-forms for other f (not JS) behave as training objectives for generative models?

## Exercises worth doing
- In-text exercise (p. 148) — derive $|P[A]-Q[A]|\le\sqrt{Q[A]\chi^2(P\|Q)}$ via DPI and via (7.91): shows the link between variational forms and DPI — difficulty: medium (our estimate).
- Ex. I.44 (p. 151) — Marton's coupling inf-form of $D_m$ — difficulty: hard (our estimate).
- Ex. I.46 (p. 151) — monotonicity and DPI for Fisher information — difficulty: medium (our estimate).
- Ex. I.42 and I.43 (p. 145) — additive Rényi bounds for non-product distributions — difficulty: medium (our estimate).
- Ex. I.54 (p. 136) — another property of $I_{\rm SKL}$ — difficulty: medium (our estimate).

## Reading notes
- This part starts mid-proof of (7.52) in §7.8 (printed p. 136) and ends at the end of §7.14* (printed p. 157). Printed = pdf − 25. The header "itbook-export … Page-N" is an export artefact. The text layer is garbled in several equations; I used the page images.
- Misprints, as I read the images:
  - p. 138: "the bias … is always non-negative", but the formula given is $-\mathbb E\,D(\hat P_n\|P_X)\le0$.
  - p. 140: $D(P_t\|P_0)=\frac{t^2}{2\log e}$. Theorem 7.22 gives $\frac{\log e}2J_F t^2$ with $J_F=1$ for the Gaussian location model. The two agree only with natural logs.
  - p. 149: the substitution "$g\leftarrow\frac12g-1$" to get (7.90) does not reproduce it. $g=2u-2$ does (added check).
  - p. 150: with $h=e^g/2$, direct substitution gives $2\log2+\mathbb E_P\log h+\mathbb E_Q\log(1-h)$, not $\log2+\dots$. Check: for $P=Q$, $h\equiv\frac12$ with the printed constant gives $-\log2\ne0={\rm JS}(P,P)$.
  - p. 156–157: the approximation step writes "$-aP[S]$" where the definition of $\Psi^*_{Q,P}$ has "$+aP[S]$". The final computation $\sup_b bP[S^c]-\max(a,b)=-aP[S]$ is consistent with "+". Also, line 2 of the $\Psi^*$ chain on p. 156 lacks $f'(\infty)$ in the $S^c$ term, which line 3 includes.
  - p. 136: "is is".
- (7.34), (6.2), Prop. 2.21, (7.1), (7.2), Prop. 7.2, Theorem 7.6 and Theorem 7.7 are used here but stated outside this part. I did not reproduce them.
