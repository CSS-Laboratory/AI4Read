---
id: cover-2006-elements/ch02-entropy
work: cover-2006-elements
unit: "Chapter 2 — Entropy, Relative Entropy and Mutual Information"
pages: 12-49
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
---

# Entropy, Relative Entropy and Mutual Information

## L0 — One line
Entropy, relative entropy and mutual information are linked by chain rules, and one inequality, $D(p\|q)\ge 0$ (Jensen's inequality), gives conditioning-reduces-entropy, the data processing inequality, a "second law" for Markov chains, and Fano's inequality.

## L1 — The gist (≤ 120 words)
The chapter defines the basic quantities of information theory for discrete variables: entropy $H(X)$, joint and conditional entropy, relative entropy $D(p\|q)$ and mutual information $I(X;Y)$. It proves how they fit together: chain rules, the identity $I(X;Y)=H(X)-H(X|Y)$, and non-negativity of $D$ and $I$ (from Jensen's inequality). From these come concavity/convexity results, the data processing inequality (no processing of data adds information), several readings of the second law of thermodynamics for Markov chains, sufficient statistics, and Fano's inequality (a lower bound on guessing error). Later chapters use all of these as the basic toolkit; the chapter itself says their value will be tested there. (p. 12)

## L2 — Key ideas
- Entropy $H(X)=-\sum p(x)\log p(x)=E\log\frac1{p(X)}$ depends only on the probabilities, not on the values of $X$. It is $\ge 0$, and base changes only multiply it by a constant. (pp. 13–14)
- Chain rule: $H(X,Y)=H(X)+H(Y|X)$, and in general $H(X_1,\dots,X_n)=\sum_i H(X_i|X_{i-1},\dots,X_1)$. Uncertainty adds up step by step. (pp. 16, 21)
- Relative entropy $D(p\|q)$ measures the inefficiency of using a code built for $q$ when the truth is $p$. It is $\ge 0$, zero iff $p=q$, but not symmetric and not a true metric. (pp. 18, 26)
- Mutual information is a relative entropy: $I(X;Y)=D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)=H(X)+H(Y)-H(X,Y)$. It is symmetric, and $I(X;X)=H(X)$, so entropy is "self-information". (pp. 18–20)
- Jensen's inequality ($Ef(X)\ge f(EX)$ for convex $f$) is the engine behind $D\ge0$, $I\ge0$, $H(X|Y)\le H(X)$, $H(X)\le\log|\mathcal X|$ and the log sum inequality. (pp. 25–29)
- Entropy is concave in $p$. $D(p\|q)$ is convex in the pair $(p,q)$. $I(X;Y)$ is concave in $p(x)$ and convex in $p(y|x)$. (pp. 30–31)
- Data processing: if $X\to Y\to Z$ is a Markov chain then $I(X;Y)\ge I(X;Z)$. No function or randomization of $Y$ can add information about $X$. (p. 32)
- For Markov chains, relative entropy to another chain or to a stationary distribution never increases. Entropy itself increases only if the stationary distribution is uniform (doubly stochastic matrix). $H(X_n|X_1)$ grows for a stationary chain. (pp. 34–36)
- A sufficient statistic is exactly one for which the data processing inequality holds with equality. (pp. 36–37)
- Fano's inequality $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ turns residual conditional entropy into a lower bound on error probability. It is sharp. (pp. 39–40)

## L3 — Walkthrough

### Introduction (p. 12)
The chapter introduces the basic definitions, then proves chain rules, non-negativity of mutual information, the data processing inequality, and studies how far the second law of thermodynamics holds for Markov processes. The author says information is too broad a concept for one definition. Entropy has many properties matching the intuitive idea of a measure of information. Mutual information measures how much one variable tells about another. Entropy is then the "self-information" of a variable. Relative entropy is the more general quantity, a measure of distance between distributions. Their value is to be shown in later chapters (communication, statistics, complexity, gambling). (p. 12)

### 2.1 Entropy (pp. 12–15)
Notation: $X$ is discrete with alphabet $\mathcal X$ and pmf $p(x)=\Pr\{X=x\}$. $p(x)$ and $p(y)$ are different functions ($p_X$, $p_Y$). (p. 13)

**Definition.**
$$H(X)=-\sum_{x\in\mathcal X}p(x)\log p(x).\tag{2.1}$$
Also written $H(p)$. The log is base 2, so entropy is in bits. A fair coin has 1 bit. Convention: $0\log0=0$, justified by continuity since $x\log x\to0$ as $x\to0$. So zero-probability terms change nothing. (p. 13)

With base $b$ the entropy is $H_b(X)$. With base $e$ it is measured in nats. Entropy is a functional of the distribution only. It does not depend on the values taken by $X$. (p. 13)

Expectation:
$$E_pg(X)=\sum_{x\in\mathcal X}g(x)p(x).\tag{2.2}$$
With $g(X)=\log\frac1{p(X)}$:
$$H(X)=E_p\log\frac1{p(X)}.\tag{2.3}$$
The author remarks that the definition relates to thermodynamic entropy, and that an axiomatic derivation exists (Problem 4). He does not use it. Instead entropy will arise as the answer to natural questions, such as the average length of the shortest description of $X$. (pp. 13–14)

**Lemma 2.1.1.** $H(X)\ge0$. Proof: $0\le p(x)\le1$ gives $\log(1/p(x))\ge0$. (p. 14)

**Lemma 2.1.2.** $H_b(X)=(\log_ba)H_a(X)$. Proof: $\log_bp=\log_ba\,\log_ap$. (p. 14)

**Example 2.1.1.** $X=1$ w.p. $p$, $0$ w.p. $1-p$ (2.4). Then
$$H(X)=-p\log p-(1-p)\log(1-p)\stackrel{\text{def}}{=}H(p).\tag{2.5}$$
$H(X)=1$ bit at $p=1/2$. $H(p)$ is concave and equals 0 at $p=0$ or $1$ (no randomness). It is maximal at $p=\tfrac12$ (Figure 2.1). (p. 14)

**Example 2.1.2.** $X\in\{a,b,c,d\}$ with probabilities $1/2,1/4,1/8,1/8$ (2.6).
$$H(X)=-\tfrac12\log\tfrac12-\tfrac14\log\tfrac14-\tfrac18\log\tfrac18-\tfrac18\log\tfrac18=\tfrac74\text{ bits}.\tag{2.7}$$
The questions "Is $X=a$?", "Is $X=b$?", "Is $X=c$?" need on average 1.75 binary questions. This is the minimum. Chapter 5 will show the minimum expected number lies between $H(X)$ and $H(X)+1$. (pp. 14–15)

> **Intuition note.** Entropy is the average number of yes/no questions needed to pin down $X$ when you ask smartly. Skewed variables are cheaper to describe than uniform ones.

### 2.2 Joint entropy and conditional entropy (pp. 15–17)
**Joint entropy** of $(X,Y)\sim p(x,y)$; $(X,Y)$ is just one vector-valued variable:
$$H(X,Y)=-\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}p(x,y)\log p(x,y)\tag{2.8}$$
$$H(X,Y)=-E\log p(X,Y).\tag{2.9}$$
(p. 15)

**Conditional entropy**: the expected entropy of the conditional distributions, averaged over the conditioning variable. (p. 16)
$$H(Y|X)=\sum_xp(x)H(Y|X=x)\tag{2.10}$$
$$=-\sum_xp(x)\sum_yp(y|x)\log p(y|x)\tag{2.11}$$
$$=-\sum_x\sum_yp(x,y)\log p(y|x)\tag{2.12}$$
$$=-E_{p(x,y)}\log p(Y|X).\tag{2.13}$$
(p. 16)

**Theorem 2.2.1 (Chain rule).**
$$H(X,Y)=H(X)+H(Y|X).\tag{2.14}$$
Proof (p. 16):
$$H(X,Y)=-\sum_{x,y}p(x,y)\log p(x,y)\tag{2.15}$$
$$=-\sum_{x,y}p(x,y)\log p(x)p(y|x)\tag{2.16}$$
$$=-\sum_{x,y}p(x,y)\log p(x)-\sum_{x,y}p(x,y)\log p(y|x)\tag{2.17}$$
$$=-\sum_xp(x)\log p(x)-\sum_{x,y}p(x,y)\log p(y|x)\tag{2.18}$$
$$=H(X)+H(Y|X).\tag{2.19}$$
Equivalently, $\log p(X,Y)=\log p(X)+\log p(Y|X)$ (2.20); take expectations. (p. 16)

**Corollary.** $H(X,Y|Z)=H(X|Z)+H(Y|X,Z)$ (2.21). The proof is the same as the theorem's. (p. 17)

**Example 2.2.1.** Joint pmf $p(x,y)$ (rows $Y$, columns $X=1..4$):

| | X=1 | X=2 | X=3 | X=4 |
|---|---|---|---|---|
| Y=1 | 1/8 | 1/16 | 1/32 | 1/32 |
| Y=2 | 1/16 | 1/8 | 1/32 | 1/32 |
| Y=3 | 1/16 | 1/16 | 1/16 | 1/16 |
| Y=4 | 1/4 | 0 | 0 | 0 |

Marginal of $X$ is $(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ and of $Y$ is $(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$. So $H(X)=7/4$ bits and $H(Y)=2$ bits. (p. 17)
$$H(X|Y)=\sum_{i=1}^4p(Y=i)H(X|Y=i)=\tfrac14H(\tfrac12,\tfrac14,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac12,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac14,\tfrac14,\tfrac14)+\tfrac14H(1,0,0,0)\tag{2.22–2.23}$$
$$=\tfrac14\cdot\tfrac74+\tfrac14\cdot\tfrac74+\tfrac14\cdot2+\tfrac14\cdot0=\tfrac{11}8\text{ bits}.\tag{2.24–2.25}$$
Similarly $H(Y|X)=13/8$ and $H(X,Y)=27/8$ bits. Remark: $H(Y|X)\ne H(X|Y)$, but $H(X)-H(X|Y)=H(Y)-H(Y|X)$, which will be used later. (p. 17)

> **Intuition note.** The chain rule says the cost of describing a pair is the cost of the first part plus the leftover cost of the second part once the first is known. Conditioning is an average over cases, not a single case.

### 2.3 Relative entropy and mutual information (pp. 18–19)
Entropy measures the information needed on average to describe $X$. Relative entropy $D(p\|q)$ measures the inefficiency of assuming the distribution is $q$ when it is $p$. A code for the true $p$ has average length $H(p)$. A code for $q$ needs $H(p)+D(p\|q)$ bits on average. In statistics it is an expected log-likelihood ratio. (p. 18)

**Definition (relative entropy / Kullback–Leibler distance).**
$$D(p\|q)=\sum_{x\in\mathcal X}p(x)\log\frac{p(x)}{q(x)}\tag{2.26}$$
$$=E_p\log\frac{p(X)}{q(X)}.\tag{2.27}$$
Conventions: $0\log\frac0q=0$ and $p\log\frac p0=\infty$. It will be shown to be $\ge0$ and $=0$ iff $p=q$. It is not a true distance: it is not symmetric and has no triangle inequality. (p. 18)

**Definition (mutual information).** For $p(x,y)$ with marginals $p(x),p(y)$, it is the relative entropy between the joint and the product distribution:
$$I(X;Y)=\sum_{x}\sum_yp(x,y)\log\frac{p(x,y)}{p(x)p(y)}\tag{2.28}$$
$$=D\big(p(x,y)\|p(x)p(y)\big)\tag{2.29}$$
$$=E_{p(x,y)}\log\frac{p(X,Y)}{p(X)p(Y)}.\tag{2.30}$$
It is the reduction in uncertainty of one variable due to knowing the other. (pp. 18–19)

**Example 2.3.1.** $\mathcal X=\{0,1\}$; $p(0)=1-r,\ p(1)=r$; $q(0)=1-s,\ q(1)=s$.
$$D(p\|q)=(1-r)\log\frac{1-r}{1-s}+r\log\frac rs\tag{2.31}$$
$$D(q\|p)=(1-s)\log\frac{1-s}{1-r}+s\log\frac sr.\tag{2.32}$$
If $r=s$ both are 0. For $r=1/2$, $s=1/4$:
$$D(p\|q)=\tfrac12\log\frac{1/2}{3/4}+\tfrac12\log\frac{1/2}{1/4}=1-\tfrac12\log3=0.2075\text{ bits}\tag{2.33}$$
$$D(q\|p)=\tfrac34\log\frac{3/4}{1/2}+\tfrac14\log\frac{1/4}{1/2}=\tfrac34\log3-1=0.1887\text{ bits}.\tag{2.34}$$
So $D(p\|q)\ne D(q\|p)$ in general. (p. 19)

> **Intuition note.** $D(p\|q)$ is a penalty in bits for believing $q$ when reality is $p$. The penalty depends on which one is "reality", hence the asymmetry.

### 2.4 Relationship between entropy and mutual information (pp. 19–21)
$$I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}\tag{2.35}$$
$$=\sum_{x,y}p(x,y)\log\frac{p(x|y)}{p(x)}\tag{2.36}$$
$$=-\sum_{x,y}p(x,y)\log p(x)+\sum_{x,y}p(x,y)\log p(x|y)\tag{2.37}$$
$$=-\sum_xp(x)\log p(x)-\Big(-\sum_{x,y}p(x,y)\log p(x|y)\Big)\tag{2.38}$$
$$=H(X)-H(X|Y).\tag{2.39}$$
(pp. 19–20) By symmetry $I(X;Y)=H(Y)-H(Y|X)$ (2.40), so $X$ says as much about $Y$ as $Y$ about $X$. With the chain rule:
$$I(X;Y)=H(X)+H(Y)-H(X,Y)\tag{2.41}$$
$$I(X;X)=H(X)-H(X|X)=H(X).\tag{2.42}$$
This is why entropy is called self-information. (p. 20)

**Theorem 2.4.1 (Mutual information and entropy).**
$$I(X;Y)=H(X)-H(X|Y)\tag{2.43}$$
$$I(X;Y)=H(Y)-H(Y|X)\tag{2.44}$$
$$I(X;Y)=H(X)+H(Y)-H(X,Y)\tag{2.45}$$
$$I(X;Y)=I(Y;X)\tag{2.46}$$
$$I(X;X)=H(X).\tag{2.47}$$
Figure 2.2 is a Venn diagram: two overlapping circles $H(X)$ and $H(Y)$; the overlap is $I(X;Y)$, the non-overlapping parts are $H(X|Y)$ and $H(Y|X)$, and the union is $H(X,Y)$. (p. 20–21)

**Example 2.4.1.** For the joint distribution of Example 2.2.1, $I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)=0.375$ bits. (p. 21)

> **Intuition note.** Mutual information is the overlap of two uncertainties: what you save in describing $X$ once you know $Y$ (and vice versa).

### 2.5 Chain rules for entropy, relative entropy and mutual information (pp. 21–23)
**Theorem 2.5.1 (Chain rule for entropy).** For $X_1,\dots,X_n\sim p(x_1,\dots,x_n)$:
$$H(X_1,\dots,X_n)=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.48}$$
Proof: repeat the two-variable rule (p. 21):
$$H(X_1,X_2)=H(X_1)+H(X_2|X_1)\tag{2.49}$$
$$H(X_1,X_2,X_3)=H(X_1)+H(X_2,X_3|X_1)\tag{2.50}$$
$$=H(X_1)+H(X_2|X_1)+H(X_3|X_2,X_1)\tag{2.51}$$
$$\vdots$$
$$H(X_1,\dots,X_n)=H(X_1)+H(X_2|X_1)+\cdots+H(X_n|X_{n-1},\dots,X_1)\tag{2.52}$$
$$=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.53}$$
(p. 21)

Alternative proof: write $p(x_1,\dots,x_n)=\prod_{i=1}^np(x_i|x_{i-1},\dots,x_1)$ and evaluate (pp. 21–22):
$$H(X_1,\dots,X_n)=-\sum_{x_1,\dots,x_n}p(x_1,\dots,x_n)\log p(x_1,\dots,x_n)\tag{2.54}$$
$$=-\sum p(x_1,\dots,x_n)\log\prod_{i=1}^np(x_i|x_{i-1},\dots,x_1)\tag{2.55}$$
$$=-\sum_{x_1,\dots,x_n}\sum_{i=1}^np(x_1,\dots,x_n)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.56}$$
$$=-\sum_{i=1}^n\sum_{x_1,\dots,x_n}p(x_1,\dots,x_n)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.57}$$
$$=-\sum_{i=1}^n\sum_{x_1,\dots,x_i}p(x_1,\dots,x_i)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.58}$$
$$=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.59}$$
(p. 22)

**Definition (conditional mutual information).** The reduction in uncertainty of $X$ due to $Y$ when $Z$ is given:
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)\tag{2.60}$$
$$=E_{p(x,y,z)}\log\frac{p(X,Y|Z)}{p(X|Z)p(Y|Z)}.\tag{2.61}$$
(p. 22)

**Theorem 2.5.2 (Chain rule for information).**
$$I(X_1,\dots,X_n;Y)=\sum_{i=1}^nI(X_i;Y|X_{i-1},X_{i-2},\dots,X_1).\tag{2.62}$$
Proof:
$$I(X_1,\dots,X_n;Y)=H(X_1,\dots,X_n)-H(X_1,\dots,X_n|Y)\tag{2.63}$$
$$=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1)-\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1,Y)=\sum_{i=1}^nI(X_i;Y|X_1,\dots,X_{i-1}).\tag{2.64}$$
(p. 22)

**Definition (conditional relative entropy).** Averaged over $p(x)$:
$$D\big(p(y|x)\|q(y|x)\big)=\sum_xp(x)\sum_yp(y|x)\log\frac{p(y|x)}{q(y|x)}\tag{2.65}$$
$$=E_{p(x,y)}\log\frac{p(Y|X)}{q(Y|X)}.\tag{2.66}$$
The notation omits $p(x)$, which is understood from context. (pp. 22–23)

**Theorem 2.5.3 (Chain rule for relative entropy).**
$$D\big(p(x,y)\|q(x,y)\big)=D\big(p(x)\|q(x)\big)+D\big(p(y|x)\|q(y|x)\big).\tag{2.67}$$
Proof:
$$D(p(x,y)\|q(x,y))=\sum_x\sum_yp(x,y)\log\frac{p(x,y)}{q(x,y)}\tag{2.68}$$
$$=\sum_x\sum_yp(x,y)\log\frac{p(x)p(y|x)}{q(x)q(y|x)}\tag{2.69}$$
$$=\sum_x\sum_yp(x,y)\log\frac{p(x)}{q(x)}+\sum_x\sum_yp(x,y)\log\frac{p(y|x)}{q(y|x)}\tag{2.70}$$
$$=D(p(x)\|q(x))+D(p(y|x)\|q(y|x)).\tag{2.71}$$
This chain rule is used in Section 2.9 for the second law. (p. 23)

> **Intuition note.** All three chain rules say the same thing: a joint quantity splits into "first variable" plus "second variable given the first".

### 2.6 Jensen's inequality and its consequences (pp. 23–28)
**Definition (convex).** $f$ is convex on $(a,b)$ if for all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$:
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2).\tag{2.72}$$
Strictly convex: equality only for $\lambda=0$ or $1$. $f$ is concave if $-f$ is convex. Convex means "below any chord". (p. 23) Convex examples: $x^2$, $|x|$, $e^x$, $x\log x$ ($x\ge0$). Concave: $\log x$, $\sqrt x$ ($x\ge0$). Linear functions are both. (p. 24)

**Theorem 2.6.1.** If $f''\ge0$ (resp. $>0$) everywhere, $f$ is convex (strictly convex). Proof (pp. 24–25): Taylor expansion about $x_0$,
$$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x^*)}2(x-x_0)^2,\tag{2.73}$$
with $x^*$ between $x_0$ and $x$. The last term is $\ge0$. Let $x_0=\lambda x_1+(1-\lambda)x_2$.
Taking $x=x_1$:
$$f(x_1)\ge f(x_0)+f'(x_0)[(1-\lambda)(x_1-x_2)]\tag{2.74}$$
Taking $x=x_2$:
$$f(x_2)\ge f(x_0)+f'(x_0)[\lambda(x_2-x_1)].\tag{2.75}$$
Multiply (2.74) by $\lambda$ and (2.75) by $1-\lambda$ and add to get (2.72). (added step: the two derivative terms cancel, since $\lambda(1-\lambda)(x_1-x_2)+(1-\lambda)\lambda(x_2-x_1)=0$.) So $x^2,e^x,x\log x$ are strictly convex and $\log x,\sqrt x$ strictly concave. (p. 25)

**Theorem 2.6.2 (Jensen's inequality).** If $f$ is convex,
$$Ef(X)\ge f(EX).\tag{2.76}$$
If $f$ is strictly convex, equality implies $X=EX$ with probability 1. (p. 25) Proof by induction on mass points (discrete case). Two points:
$$p_1f(x_1)+p_2f(x_2)\ge f(p_1x_1+p_2x_2)\tag{2.77}$$
(this is the definition of convexity). Assume it holds for $k-1$ points. With $p_i'=p_i/(1-p_k)$:
$$\sum_{i=1}^kp_if(x_i)=p_kf(x_k)+(1-p_k)\sum_{i=1}^{k-1}p_i'f(x_i)\tag{2.78}$$
$$\ge p_kf(x_k)+(1-p_k)f\Big(\sum_{i=1}^{k-1}p_i'x_i\Big)\tag{2.79}$$
$$\ge f\Big(p_kx_k+(1-p_k)\sum_{i=1}^{k-1}p_i'x_i\Big)\tag{2.80}$$
$$=f\Big(\sum_{i=1}^kp_ix_i\Big).\tag{2.81}$$
The first inequality is the induction hypothesis, the second is convexity. The continuous case follows by continuity arguments. The equality condition is left to the reader. (pp. 25–26)

**Theorem 2.6.3 (Information inequality).**
$$D(p\|q)\ge0,\tag{2.82}$$
with equality iff
$$p(x)=q(x)\ \ \forall x.\tag{2.83}$$
Proof: let $A=\{x:p(x)>0\}$ (the support of $p$). Then
$$-D(p\|q)=-\sum_{x\in A}p(x)\log\frac{p(x)}{q(x)}\tag{2.84}$$
$$=\sum_{x\in A}p(x)\log\frac{q(x)}{p(x)}\tag{2.85}$$
$$\le\log\sum_{x\in A}p(x)\frac{q(x)}{p(x)}\tag{2.86}$$
$$=\log\sum_{x\in A}q(x)\tag{2.87}$$
$$\le\log\sum_{x\in\mathcal X}q(x)\tag{2.88}$$
$$=\log1\tag{2.89}$$
$$=0.\tag{2.90}$$
(2.86) is Jensen's inequality. $\log t$ is strictly concave, so equality in (2.86) holds iff $q(x)/p(x)=1$ everywhere. Hence $D=0$ iff $p=q$. (p. 26)

> **Intuition note.** Believing the wrong distribution can never help you on average. The only free lunch is zero loss when your belief is exactly right.

**Corollaries (p. 27).**
- Non-negativity of mutual information: $I(X;Y)\ge0$ (2.91), with equality iff $X,Y$ independent. Proof: $I=D(p(x,y)\|p(x)p(y))\ge0$ with equality iff $p(x,y)=p(x)p(y)$.
- $D(p(y|x)\|q(y|x))\ge0$ (2.92), with equality iff $p(y|x)=q(y|x)$ for all $y$ and all $x$ with $p(x)>0$.
- $I(X;Y|Z)\ge0$ (2.93), with equality iff $X$ and $Y$ are conditionally independent given $Z$.

**Theorem 2.6.4.** $H(X)\le\log|\mathcal X|$, with equality iff $X$ is uniform on $\mathcal X$. Proof: with $u(x)=1/|\mathcal X|$,
$$D(p\|u)=\sum p(x)\log\frac{p(x)}{u(x)}=\log|\mathcal X|-H(X)\tag{2.94}$$
$$0\le D(p\|u)=\log|\mathcal X|-H(X).\tag{2.95}$$
(p. 27)

**Theorem 2.6.5 (Conditioning reduces entropy).**
$$H(X|Y)\le H(X)\tag{2.96}$$
with equality iff $X$ and $Y$ are independent. Proof: $0\le I(X;Y)=H(X)-H(X|Y)$. This holds only on average: $H(X|Y=y)$ can be larger or smaller than $H(X)$, but $H(X|Y)=\sum_yp(y)H(X|Y=y)\le H(X)$. In a court case, specific evidence may raise uncertainty, but on average evidence reduces it. (pp. 27–28)

**Example 2.6.1.** Joint pmf: $p(Y{=}1,X{=}1)=0$, $p(Y{=}1,X{=}2)=\tfrac34$, $p(Y{=}2,X{=}1)=\tfrac18$, $p(Y{=}2,X{=}2)=\tfrac18$. Then $H(X)=H(\tfrac18,\tfrac78)=0.544$ bits, $H(X|Y=1)=0$, $H(X|Y=2)=1$ bit, and $H(X|Y)=\tfrac34H(X|Y=1)+\tfrac14H(X|Y=2)=0.25$ bits. Seeing $Y=2$ raises uncertainty, seeing $Y=1$ lowers it, and on average it falls. (p. 28)

**Theorem 2.6.6 (Independence bound on entropy).**
$$H(X_1,\dots,X_n)\le\sum_{i=1}^nH(X_i)\tag{2.97}$$
with equality iff the $X_i$ are independent. Proof: by the chain rule (2.98), then conditioning reduces entropy (2.99). Equality iff each $X_i$ is independent of $X_{i-1},\dots,X_1$. (p. 28)

> **Intuition note.** Dependence is redundancy: a dependent collection needs fewer bits to describe than the sum of its parts.

### 2.7 The log sum inequality and its applications (pp. 29–31)
**Theorem 2.7.1 (Log sum inequality).** For non-negative $a_1,\dots,a_n$ and $b_1,\dots,b_n$:
$$\sum_{i=1}^na_i\log\frac{a_i}{b_i}\ge\Big(\sum_{i=1}^na_i\Big)\log\frac{\sum_ia_i}{\sum_ib_i}\tag{2.100}$$
with equality iff $a_i/b_i=$ const. Conventions: $0\log0=0$, $a\log\frac a0=\infty$ for $a>0$, $0\log\frac00=0$. (p. 29)

Proof: assume $a_i,b_i>0$. $f(t)=t\log t$ is strictly convex because $f''(t)=\frac1t\log e>0$. By Jensen,
$$\sum\alpha_if(t_i)\ge f\Big(\sum\alpha_it_i\Big),\quad\alpha_i\ge0,\ \sum\alpha_i=1.\tag{2.101}$$
Set $\alpha_i=b_i/\sum_jb_j$ and $t_i=a_i/b_i$:
$$\sum\frac{a_i}{\sum b_j}\log\frac{a_i}{b_i}\ge\Big(\sum\frac{a_i}{\sum b_j}\Big)\log\sum\frac{a_i}{\sum b_j}.\tag{2.102}$$
Multiplying by $\sum_jb_j$ gives the log sum inequality. (p. 29)

Re-proof of Theorem 2.6.3: by log sum,
$$D(p\|q)=\sum p(x)\log\frac{p(x)}{q(x)}\ge\Big(\sum p(x)\Big)\log\frac{\sum p(x)}{\sum q(x)}=1\log\frac11=0,\tag{2.103–2.105}$$
with equality iff $p(x)/q(x)=c$; since both sum to 1, $c=1$. (p. 29)

**Theorem 2.7.2.** $D(p\|q)$ is convex in the pair $(p,q)$:
$$D(\lambda p_1+(1-\lambda)p_2\|\lambda q_1+(1-\lambda)q_2)\le\lambda D(p_1\|q_1)+(1-\lambda)D(p_2\|q_2).\tag{2.106}$$
Proof: apply the log sum inequality to each term (two summands):
$$(\lambda p_1+(1-\lambda)p_2)\log\frac{\lambda p_1+(1-\lambda)p_2}{\lambda q_1+(1-\lambda)q_2}\le\lambda p_1\log\frac{\lambda p_1}{\lambda q_1}+(1-\lambda)p_2\log\frac{(1-\lambda)p_2}{(1-\lambda)q_2},\tag{2.107}$$
and sum over $x$. (p. 30) (The $\lambda$'s cancel in the right-hand logs, giving $\lambda p_1(x)\log\frac{p_1(x)}{q_1(x)}$ etc. (added step))

**Theorem 2.7.3 (Concavity of entropy).** $H(p)$ is concave in $p$. Proof 1: $H(p)=\log|\mathcal X|-D(p\|u)$ (2.108), and $D$ is convex. Proof 2: let $X_1\sim p_1$, $X_2\sim p_2$, $\theta=1$ w.p. $\lambda$, $2$ w.p. $1-\lambda$, and $Z=X_\theta$. Then $Z\sim\lambda p_1+(1-\lambda)p_2$ (2.109). Conditioning reduces entropy, so
$$H(Z)\ge H(Z|\theta)\tag{2.110}$$
$$H(\lambda p_1+(1-\lambda)p_2)\ge\lambda H(p_1)+(1-\lambda)H(p_2).\tag{2.111}$$
(p. 30) A consequence: mixing two gases of equal entropy yields a gas of higher entropy. (p. 31)

**Theorem 2.7.4.** For $(X,Y)\sim p(x)p(y|x)$, $I(X;Y)$ is concave in $p(x)$ for fixed $p(y|x)$, and convex in $p(y|x)$ for fixed $p(x)$. (p. 31)

Proof, part 1: $I(X;Y)=H(Y)-H(Y|X)=H(Y)-\sum_xp(x)H(Y|X=x)$ (2.112). For fixed $p(y|x)$, $p(y)$ is linear in $p(x)$. So $H(Y)$ is concave in $p(x)$, the second term is linear, and the difference is concave. (p. 31)

Part 2: fix $p(x)$; take two conditionals $p_1(y|x)$, $p_2(y|x)$ with joints $p_i(x,y)=p(x)p_i(y|x)$. Mixture:
$$p_\lambda(y|x)=\lambda p_1(y|x)+(1-\lambda)p_2(y|x)\tag{2.113}$$
$$p_\lambda(x,y)=\lambda p_1(x,y)+(1-\lambda)p_2(x,y)\tag{2.114}$$
$$p_\lambda(y)=\lambda p_1(y)+(1-\lambda)p_2(y).\tag{2.115}$$
With $q_\lambda(x,y)=p(x)p_\lambda(y)$:
$$q_\lambda(x,y)=\lambda q_1(x,y)+(1-\lambda)q_2(x,y)\tag{2.116}$$
$$I(X;Y)=D(p_\lambda\|q_\lambda).\tag{2.117}$$
Since $D$ is convex in $(p,q)$, $I$ is convex in $p(y|x)$. (p. 31)

> **Intuition note.** Mixing distributions tends to raise entropy (concavity). The channel-input/channel-law asymmetry in 2.7.4 (concave in input, convex in channel) is what later makes capacity well-behaved. The chapter itself only states this as "basic properties".

### 2.8 Data processing inequality (pp. 32–33)
**Definition (Markov chain).** $X\to Y\to Z$ if the conditional distribution of $Z$ depends only on $Y$ and is conditionally independent of $X$, i.e.
$$p(x,y,z)=p(x)p(y|x)p(z|y).\tag{2.118}$$
(p. 32) Consequences:
- $X\to Y\to Z$ iff $X,Z$ are conditionally independent given $Y$:
$$p(x,z|y)=\frac{p(x,y,z)}{p(y)}=\frac{p(x,y)p(z|y)}{p(y)}=p(x|y)p(z|y).\tag{2.119}$$
This is the characterization that extends to Markov fields: $n$-dimensional processes where the interior and exterior are independent given the boundary.
- $X\to Y\to Z$ implies $Z\to Y\to X$, written $X\leftrightarrow Y\leftrightarrow Z$.
- If $Z=f(Y)$ then $X\to Y\to Z$. (p. 32)

**Theorem 2.8.1 (Data processing inequality).** If $X\to Y\to Z$ then $I(X;Y)\ge I(X;Z)$. Proof: expand $I(X;Y,Z)$ by the chain rule in two ways (p. 32):
$$I(X;Y,Z)=I(X;Z)+I(X;Y|Z)\tag{2.120}$$
$$=I(X;Y)+I(X;Z|Y).\tag{2.121}$$
Markov gives $I(X;Z|Y)=0$ and $I(X;Y|Z)\ge0$, so
$$I(X;Y)\ge I(X;Z).\tag{2.122}$$
Equality iff $I(X;Y|Z)=0$, i.e. $X\to Z\to Y$ is also a Markov chain. Similarly $I(Y;Z)\ge I(X;Z)$. (p. 33) (See Reading notes: the printed (2.121) repeats (2.120); the second expansion above is the one the proof needs.)

**Corollary.** $Z=g(Y)$ gives $I(X;Y)\ge I(X;g(Y))$, because $X\to Y\to g(Y)$ is a Markov chain. Functions of data cannot add information about $X$. (p. 33)

**Corollary.** If $X\to Y\to Z$, then $I(X;Y|Z)\le I(X;Y)$ (2.123). Proof: from the two expansions, using $I(X;Z|Y)=0$ and $I(X;Z)\ge0$. So observing a "downstream" variable can only reduce the dependence of $X$ and $Y$. (p. 33)

Without the Markov property it can fail: let $X,Y$ be independent fair bits and $Z=X+Y$. Then $I(X;Y)=0$ but $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=H(X|Z)=P(Z{=}1)H(X|Z{=}1)=\tfrac12$ bit. (p. 33)

> **Intuition note.** If information reaches you through a chain, each extra link can only leak information, never create it.

### 2.9 The second law of thermodynamics (pp. 33–36)
The second law says the entropy of an isolated system is non-decreasing. Statistical thermodynamics defines entropy as the log of the number of microstates, which matches the chapter's entropy if all states are equally likely. The system is modeled as a Markov chain (Chapter 4) with transitions obeying the physical laws. The author finds four (plus one) readings of the second law. Entropy need not always increase, but relative entropy always decreases. (p. 33–34)

1. **$D(\mu_n\|\mu_n')$ decreases with $n$.** Let $\mu_n,\mu_n'$ be two distributions on the state space at time $n$, and $\mu_{n+1},\mu_{n+1}'$ at time $n+1$. The joint pmfs are $p(x_n,x_{n+1})=p(x_n)r(x_{n+1}|x_n)$ and $q(x_n,x_{n+1})=q(x_n)r(x_{n+1}|x_n)$, with $r$ the transition function. The chain rule gives two expansions:
$$D(p(x_n,x_{n+1})\|q(x_n,x_{n+1}))=D(p(x_n)\|q(x_n))+D(p(x_{n+1}|x_n)\|q(x_{n+1}|x_n))$$
$$=D(p(x_{n+1})\|q(x_{n+1}))+D(p(x_n|x_{n+1})\|q(x_n|x_{n+1})).$$
Both conditionals $p(x_{n+1}|x_n),q(x_{n+1}|x_n)$ equal $r$, so the first conditional term is 0. The second conditional term is $\ge0$. Hence
$$D(p(x_n)\|q(x_n))\ge D(p(x_{n+1})\|q(x_{n+1}))\tag{2.124}$$
$$D(\mu_n\|\mu_n')\ge D(\mu_{n+1}\|\mu_{n+1}').\tag{2.125}$$
Interpretation: with the same wealth-redistribution tax system in Canada and England, the wealth distributions of the two countries become more similar over time. (p. 34)

2. **$D(\mu_n\|\mu)$ decreases for stationary $\mu$.** Let $\mu_n'=\mu$ be a stationary distribution, so $\mu_{n+1}'=\mu$ too:
$$D(\mu_n\|\mu)\ge D(\mu_{n+1}\|\mu).\tag{2.126}$$
Any state distribution gets closer to each stationary distribution. The sequence is monotone non-increasing and non-negative, so it has a limit. The limit is 0 if the stationary distribution is unique, which is harder to prove. (pp. 34–35)

3. **Entropy increases if the stationary distribution is uniform.** In general, decreasing relative entropy does not imply increasing entropy. Counterexample: any chain with a non-uniform stationary distribution, started from the uniform (maximum-entropy) distribution. It moves toward the lower-entropy stationary distribution, so entropy decreases. If the stationary distribution is uniform:
$$D(\mu_n\|\mu)=\log|\mathcal X|-H(\mu_n)=\log|\mathcal X|-H(X_n).\tag{2.127}$$
Then decreasing relative entropy means increasing entropy. This matches statistical thermodynamics, where microstates are equally likely. (p. 35)

**Definition (doubly stochastic).** A transition matrix $[P_{ij}]$, $P_{ij}=\Pr\{X_{n+1}=j|X_n=i\}$, is doubly stochastic if
$$\sum_iP_{ij}=1,\ j=1,2,\dots\tag{2.128}$$
$$\sum_jP_{ij}=1,\ i=1,2,\dots\tag{2.129}$$
Remark: the uniform distribution is stationary iff $P$ is doubly stochastic (Problem 1, Chapter 4). (p. 35)

4. **$H(X_n|X_1)$ increases with $n$ for a stationary Markov process.** $H(X_n)$ is constant, so the entropy is non-increasing, but the conditional uncertainty of the future grows. First proof:
$$H(X_n|X_1)\ge H(X_n|X_1,X_2)\ \text{(conditioning reduces entropy)}\tag{2.130}$$
$$=H(X_n|X_2)\ \text{(Markovity)}\tag{2.131}$$
$$=H(X_{n-1}|X_1)\ \text{(stationarity)}.\tag{2.132}$$
Second proof: data processing on $X_1\to X_{n-1}\to X_n$ gives
$$I(X_1;X_{n-1})\ge I(X_1;X_n)\tag{2.133}$$
$$H(X_{n-1})-H(X_{n-1}|X_1)\ge H(X_n)-H(X_n|X_1).\tag{2.134}$$
By stationarity $H(X_{n-1})=H(X_n)$, so
$$H(X_{n-1}|X_1)\le H(X_n|X_1).\tag{2.135}$$
The same techniques show $H(X_0|X_n)$ increases in $n$ for any Markov chain (Problem 35). (pp. 35–36)

5. **Shuffles increase entropy.** If $T$ is a shuffle (permutation) of a deck, $X$ the initial random order, and $T$ independent of $X$, then
$$H(TX)\ge H(X).\tag{2.136}$$
Problem 31 outlines a proof. (p. 36)

> **Intuition note.** Entropy of the state can go either way, but the "distance" between two descriptions of a Markov system shrinks with time, because the dynamics forget the difference. Entropy rises only when the equilibrium is the uniform distribution.

### 2.10 Sufficient statistics (pp. 36–38)
Setup: a family $\{f_\theta(x)\}$, a sample $X$, and a statistic $T(X)$ (any function of the sample). Then $\theta\to X\to T(X)$ and
$$I(\theta;T(X))\le I(\theta;X)\tag{2.137}$$
for any distribution on $\theta$. Equality means no information is lost. (p. 36)

**Definition.** $T(X)$ is a sufficient statistic relative to $\{f_\theta\}$ if $X$ is independent of $\theta$ given $T(X)$, i.e. $\theta\to T(X)\to X$ is a Markov chain. This is the equality condition of data processing:
$$I(\theta;X)=I(\theta;T(X))\tag{2.138}$$
for all distributions on $\theta$. Sufficient statistics preserve mutual information, and conversely. (p. 37)

Examples (p. 37–38):
1. $X_1,\dots,X_n\in\{0,1\}$ i.i.d. coin tosses with $\theta=\Pr(X_i=1)$. $T=\sum X_i$ is sufficient:
$$\Pr\Big\{(X_1,\dots,X_n)=(x_1,\dots,x_n)\Big|\sum X_i=k\Big\}=\begin{cases}\frac1{\binom nk}&\text{if }\sum x_i=k\\0&\text{otherwise.}\end{cases}\tag{2.139}$$
Given $T$, all sequences with that many 1s are equally likely and independent of $\theta$.
2. $f_\theta(x)=\frac1{\sqrt{2\pi}}e^{-(x-\theta)^2/2}=\mathcal N(\theta,1)$ (2.140). The sample mean $\bar X_n$ is sufficient for $\theta$. The conditional distribution of $X_1..X_n$ given $\bar X_n$ and $n$ does not depend on $\theta$. (Densities are used here. Entropy for continuous variables is defined in Chapter 9.)
3. $f_\theta=\text{Uniform}(\theta,\theta+1)$. A sufficient statistic is
$$T(X_1,\dots,X_n)=(\max\{X_i\},\min\{X_i\}).\tag{2.141}$$
The proof is "slightly more complicated". (p. 38)

**Definition (minimal sufficient statistic).** $T(X)$ is minimal sufficient if it is a function of every other sufficient statistic $U$; in data-processing terms
$$\theta\to T(X)\to U(X)\to X.\tag{2.142}$$
It maximally compresses the information about $\theta$. Example: for a normal with mean $\theta$, the pair (mean of odd-indexed samples, mean of even-indexed samples) is sufficient but not minimal. The earlier examples are minimal. (p. 38)

> **Intuition note.** A sufficient statistic is a lossless summary of the data *for the purpose of learning $\theta$*. Mutual information with $\theta$ is the quantity that is preserved.

### 2.11 Fano's inequality (pp. 38–40)
Guess $X$ from a correlated $Y$ via $\hat X=g(Y)$. $H(X|Y)=0$ iff $X$ is a function of $Y$ (a problem at the chapter's end), so error-free estimation is possible iff $H(X|Y)=0$. Fano quantifies the idea that small error needs small $H(X|Y)$. It is needed for the converse of Shannon's second theorem (Chapter 8). (p. 38)

$X\to Y\to\hat X$ is a Markov chain. Define
$$P_e=\Pr\{\hat X\ne X\}.\tag{2.143}$$

**Theorem 2.11.1 (Fano's inequality).**
$$H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y).\tag{2.144}$$
Weakened forms (the weakening step itself is not shown in the text):
$$1+P_e\log|\mathcal X|\ge H(X|Y)\tag{2.145}$$
$$P_e\ge\frac{H(X|Y)-1}{\log|\mathcal X|}.\tag{2.146}$$
(these use $H(P_e)\le1$ and $\log(|\mathcal X|-1)\le\log|\mathcal X|$ (added step)). Remark: $P_e=0$ implies $H(X|Y)=0$. (p. 39)

Proof: define $E=1$ if $\hat X\ne X$, $E=0$ if $\hat X=X$ (2.147). Expand $H(E,X|Y)$ two ways:
$$H(E,X|Y)=H(X|Y)+\underbrace{H(E|X,Y)}_{=0}\tag{2.148}$$
$$=\underbrace{H(E|Y)}_{\le H(P_e)}+\underbrace{H(X|E,Y)}_{\le P_e\log(|\mathcal X|-1)}.\tag{2.149}$$
Reasons: conditioning reduces entropy, so $H(E|Y)\le H(E)=H(P_e)$ ($E$ is binary). $E$ is a function of $X$ and $g(Y)$, so $H(E|X,Y)=0$. Then
$$H(X|E,Y)=\Pr(E{=}0)H(X|Y,E{=}0)+\Pr(E{=}1)H(X|Y,E{=}1)\tag{2.150}$$
$$\le(1-P_e)\cdot0+P_e\log(|\mathcal X|-1).\tag{2.151}$$
Given $E=0$, $X=g(Y)$. Given $E=1$, the conditional entropy is at most the log of the number of remaining outcomes ($|\mathcal X|-1$ if $g(Y)\in\mathcal X$, else $|\mathcal X|$). (pp. 39–40)

**Remark (no knowledge of $Y$; sharpness).** Let $X\in\{1,\dots,m\}$ with $p_1\ge p_2\ge\dots\ge p_m$. The best guess is $\hat X=1$, so $P_e=1-p_1$, and Fano becomes
$$H(P_e)+P_e\log(m-1)\ge H(X).\tag{2.152}$$
The pmf
$$(p_1,\dots,p_m)=\Big(1-P_e,\frac{P_e}{m-1},\dots,\frac{P_e}{m-1}\Big)\tag{2.153}$$
achieves equality, so Fano's inequality is sharp. (p. 40)

> **Intuition note.** If, after seeing $Y$, you still have a lot of uncertainty about $X$ (many bits), you cannot guess $X$ correctly most of the time. Fano converts bits of leftover uncertainty into a minimum error rate.

### Summary of Chapter 2 (pp. 40–42)
The author's own summary restates (2.154)–(2.164): definitions of $H,D,I$ and alternative expectation forms (2.158)–(2.162), e.g. $I(X;Y)=E_p\log\frac{p(X,Y)}{p(X)p(Y)}$ and $D(p\|q)=E_p\log\frac{p(X)}{q(X)}$. Properties of $H$: $\ge0$; base change; conditioning reduces entropy (2.155); $H(X_1..X_n)\le\sum H(X_i)$; $H(X)\le\log|\mathcal X|$; concavity. Properties of $D$ and $I$: $I=H(X)-H(X|Y)=\dots$; $D\ge0$; $I=D(p(x,y)\|p(x)p(y))\ge0$; $D(p\|u)=\log m-H(p)$; $D$ convex in $(p,q)$. It lists the three chain rules, Jensen, the log sum inequality (2.163), data processing, the five second-law statements, the sufficient-statistic criterion, and Fano (2.164). (pp. 40–42) The summary's item 5 on the second law is "$H(X_0|X_n)$ of the initial condition increases for any Markov chain". (p. 42)

### Problems for Chapter 2 (pp. 42–48)
There are 35 problems; the unit contains no solutions. Highlights: coin flips until first head (Prob. 1); entropy of functions (Prob. 2, 5); minimum entropy (3); axiomatic definition of entropy from normalization, continuity and grouping (4, "considerably more difficult" p. 43); zero conditional entropy (6); extracting fair bits from a bent coin, bounded by $nH(p)$ (7); World Series (8); infinite entropy (9); conditional vs unconditional MI (10); Venn diagrams and three-way $I(X;Y;Z)$, which can be negative (12); coin weighing (13); a metric $\rho(X,Y)=H(X|Y)+H(Y|X)$ (15); bottleneck (22); run-length coding (23); Markov's inequality for probabilities (24); mixing increases entropy (28); max-entropy with a mean constraint (30); shuffles (31); Fano without conditioning (33); monotone convergence of the empirical distribution (34); and monotonicity of $H(X_0|X_n)$ (35). (pp. 42–49)

### Historical notes (p. 49)
Entropy began in thermodynamics. Boltzmann linked it to microstates with $S=k\ln W$. Hartley (1930s) proposed a log-of-alphabet-size measure. Shannon defined entropy and mutual information as used here. Kullback and Leibler defined relative entropy, which also goes by Kullback–Leibler distance, cross entropy, information divergence and information for discrimination; Csiszár and Amari studied it. Fano proved his inequality. Fisher defined sufficiency, Lehmann and Scheffé minimal sufficiency, and Kullback linked mutual information to sufficiency. Brillouin and Jaynes discussed information theory and thermodynamics, and Bennett and Landauer physical limits to computation. (p. 49)

## Toy example
*(Ours, not from the text.)* Let $X,Y\in\{0,1\}$ with joint pmf $p(0,0)=p(1,1)=3/8$ and $p(0,1)=p(1,0)=1/8$. Use $\log_23=1.58496$.

1. Marginals: $p(X{=}0)=3/8+1/8=1/2$, same for $Y$. So $H(X)=H(Y)=1$ bit.
2. Joint entropy: $H(X,Y)=-2\cdot\frac38\log\frac38-2\cdot\frac18\log\frac18=\frac34(3-1.58496)+\frac34\cdot3-\frac34\cdot 3+\frac34$. Simplify directly: first part $\frac34\log\frac83=\frac34(3-1.58496)=\frac34(1.41504)=1.06128$; second part $\frac14\log8=\frac14\cdot3=0.75$. Total $H(X,Y)=1.81128$ bits.
3. Chain rule (2.14): $H(Y|X)=H(X,Y)-H(X)=0.81128$. Check directly: given $X=0$, $Y\sim(3/4,1/4)$, and $H(\frac14)=\frac14\cdot2+\frac34\log\frac43=0.5+0.75(0.41504)=0.81128$. ✓.
4. Mutual information (2.43): $I(X;Y)=1-0.81128=0.18872$ bits. Check via (2.29) against the product $1/4$: $2\cdot\frac38\log\frac{3/8}{1/4}+2\cdot\frac18\log\frac{1/8}{1/4}=\frac34(0.58496)-\frac14=0.43872-0.25=0.18872$ ✓.
5. Data processing (2.122): make $Z$ a noisy copy of $Y$ that flips $Y$ with probability $1/4$. This gives $X\to Y\to Z$. $P(X=Z)=P(X{=}Y)\cdot\frac34+P(X{\ne}Y)\cdot\frac14=\frac34\cdot\frac34+\frac14\cdot\frac14=\frac{10}{16}=\frac58$. $Z$ is uniform and the pair $(X,Z)$ is a symmetric binary pair with agreement probability $5/8$, so $I(X;Z)=1-H(\frac38)$. $H(\frac38)=\frac38(1.41504)+\frac58(0.67807)=0.53064+0.42379=0.95443$ (using $\log_2\frac85=3-2.32193=0.67807$). So $I(X;Z)=0.04557\le0.18872=I(X;Y)$ ✓.
6. Fano check for guessing $X$ from $Y$ with $\hat X=Y$: $P_e=1/4$. $H(P_e)+P_e\log(|\mathcal X|-1)=0.81128+0.25\cdot0=0.81128\ge H(X|Y)=0.81128$. Equality, so Fano is tight here (binary alphabet).

## Concepts
- [[entropy]] — average surprisal $H(X)=-\sum p\log p$, depends only on probabilities (p. 13)
- [[bit]] — unit of entropy with base-2 log; nats for base $e$ (p. 13)
- [[self-information]] — $I(X;X)=H(X)$, why entropy is called self-information (p. 20)
- [[joint-and-conditional-entropy]] — $H(X,Y)$ and $H(Y|X)=\sum_xp(x)H(Y|X=x)$ (p. 16)
- [[chain-rule]] — chain rules for $H$, $I$ and $D$ (pp. 16, 21, 22, 23)
- [[mutual-information]] — $I(X;Y)=D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$, symmetric, $\ge0$ (pp. 18–20, 27)
- [[relative-entropy]] — $D(p\|q)$, a non-symmetric "distance", $\ge0$ (pp. 18, 26)
- [[data-processing-inequality]] — $X\to Y\to Z\Rightarrow I(X;Y)\ge I(X;Z)$ (p. 32)
- [[fanos-inequality]] — $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ (p. 39)
- [[maximum-entropy-principle]] — only the basic fact appears: uniform maximizes $H$ over a finite alphabet (Thm 2.6.4, p. 27); the constrained MaxEnt problem appears as Problem 30 (p. 48)
- [[jensen-inequality]] (new) — $Ef(X)\ge f(EX)$ for convex $f$ (p. 25)
- [[log-sum-inequality]] (new) — $\sum a_i\log\frac{a_i}{b_i}\ge(\sum a_i)\log\frac{\sum a_i}{\sum b_i}$ (p. 29)
- [[sufficient-statistic]] (new) — $T(X)$ with $\theta\to T(X)\to X$; preserves $I(\theta;X)$ (p. 37)
- [[markov-chain]] (new) — $p(x,y,z)=p(x)p(y|x)p(z|y)$, conditional independence of ends given the middle (p. 32)
- [[doubly-stochastic-matrix]] (new) — row and column sums 1; uniform distribution is stationary (p. 35)
- [[second-law-of-thermodynamics]] (new) — in the Markov model, $D$ to stationarity falls and $H$ rises if the stationary law is uniform (pp. 33–35)

## Canonical instances
- [[binary-entropy-function]] (new) — $H(p)$ concave, 1 bit at $p=1/2$ (Ex. 2.1.1, p. 14)
- [[dyadic-four-symbol-source]] (new) — $(1/2,1/4,1/8,1/8)$ has $H=7/4$ = expected number of questions (Ex. 2.1.2, p. 14)
- [[joint-4x4-example]] (new) — $H(X)=7/4$, $H(Y)=2$, $H(X|Y)=11/8$, $H(Y|X)=13/8$, $H(X,Y)=27/8$, $I=0.375$ (Ex. 2.2.1, 2.4.1, pp. 17, 21)
- [[kl-asymmetry-example]] (new) — $D(p\|q)=0.2075$, $D(q\|p)=0.1887$ for $r=1/2$, $s=1/4$ (Ex. 2.3.1, p. 19)
- [[court-evidence-example]] (new) — specific evidence can raise uncertainty but on average lowers it (Ex. 2.6.1, p. 28)
- [[xplusy-conditioning-increases-mi]] (new) — independent bits $X,Y$ with $Z=X+Y$ gives $I(X;Y|Z)=1/2>I(X;Y)=0$ (p. 33)
- [[canada-england-wealth]] (new) — relative entropy between two wealth distributions shrinks under the same redistribution (p. 34)
- [[sufficient-statistics-examples]] (new) — Bernoulli sum, normal sample mean, uniform$(\theta,\theta+1)$ (max, min) (pp. 37–38)
- [[fano-sharpness]] (new) — the pmf $(1-P_e,\frac{P_e}{m-1},\dots)$ attains Fano with equality (p. 40)

## Bridges (candidates)
- [same-math] $I(X;Y)=D(p(x,y)\|p(x)p(y))$ ↔ statistics: expected log-likelihood ratio of dependence vs independence (the chapter itself says $D$ is an expected log-likelihood ratio, p. 18) — the formulas coincide.
- [same-math] Data processing inequality ↔ machine learning: no feature map or layer can add information about the label beyond what its input carries.
- [same-math] Sufficient statistic ($I(\theta;T)=I(\theta;X)$) ↔ statistics/Bayesian inference: posterior depends on data only through $T$.
- [same-math] Fano's inequality ↔ machine learning/classification: a lower bound on any classifier's error from the conditional entropy of labels given features.
- [same-math] Monotone decrease of $D(\mu_n\|\mu)$ to a stationary distribution ↔ Markov chain Monte Carlo / social-science Markov models: convergence diagnostics for chains.
- [structural-analogy] Concavity of entropy and "mixing raises entropy" ↔ physics: mixing gases (the text states the gas remark, p. 31).
- [structural-analogy] Chain rule $H(X,Y)=H(X)+H(Y|X)$ ↔ probability: product rule $p(x,y)=p(x)p(y|x)$ taken in logs and expectation.
- [metaphor] Entropy as "number of yes/no questions" ↔ game of Twenty Questions (the example on p. 15 is a literal binary-question model; the game analogy is ours).

## Questions this raises
- When does conditioning on a *specific* value increase entropy ($H(X|Y=y)>H(X)$), and can one bound how often (Ex. 2.6.1)?
- The text says the minimum expected number of questions lies between $H(X)$ and $H(X)+1$. What code structure (Ch. 5) makes the lower bound reachable?
- If $D$ is not a metric, what symmetrized or square-rooted versions are metrics, and how do they relate to the local geometry of $D$? (Problem 15 gives a metric from $H(X|Y)+H(Y|X)$.)
- For which Markov chains does $H(X_n)$ itself increase without a uniform stationary law, and how fast does $D(\mu_n\|\mu)\to0$?

## Exercises worth doing
- Ex. 1 (p. 42) — entropy of the geometric "first head" variable, compare with expected number of questions — difficulty: easy
- Ex. 5 (p. 43) — $H(g(X))\le H(X)$ by justifying chain-rule steps (a)–(d) — difficulty: easy
- Ex. 7 (p. 43) — bent coin to fair bits: at most $nH(p)$ fair flips on average — difficulty: medium
- Ex. 12 (p. 45) — three-variable mutual information can be negative; prove identities — difficulty: medium
- Ex. 22 (p. 47) — bottleneck: $I(X_1;X_3)\le\log k$ — difficulty: medium
- Ex. 33 (p. 48) — Fano without conditioning by maximizing $H(\mathbf p)$ — difficulty: medium
- Ex. 4 (p. 42) — axiomatic derivation of entropy — difficulty: hard

## Reading notes
- **Edition warning.** This PDF is the 1991 first edition (Wiley), not the 2nd edition (2006). The content and chapter numbering differ from the 2nd edition (the metadata notes missing chapters such as universal source coding and portfolio theory). Page numbers cited are the printed ones of the 1991 edition (12–49).
- **OCR.** The text layer is noisy. Symbols such as $\mathcal X$ appear as "Z!?", "%", "2f" etc., and many equations are garbled. I read equations against the page images and the logical structure of the proofs. Running-header page numbers in the text layer are sometimes wrong (e.g. "36" on printed p. 16).
- **Likely misprint, p. 32, (2.121).** The text layer shows (2.121) as "$I(X;Z)+I(X;Y|Z)$", repeating (2.120). The proof needs $I(X;Y,Z)=I(X;Y)+I(X;Z|Y)$. I used that and flagged it. The original misprint is probably real in the book.
- **p. 30, Theorem 2.7.3 (2.108).** The text layer is garbled. I reconstructed $H(p)=\log|\mathcal X|-D(p\|u)$ from (2.94)–(2.95).
- **p. 28, Example 2.6.1.** The table is garbled in the text layer. I used the image values $0,\tfrac34;\tfrac18,\tfrac18$, consistent with the printed results $H(X)=0.544$ and $H(X|Y)=0.25$. In Example 2.3.1 (2.33–2.34) the logs are as printed and consistent with 0.2075 and 0.1887.
- **Minor inconsistency.** Theorem 2.7.1 states "non-negative numbers", while the summary (2.163) says "positive numbers". Section 2.9 item 4 proves $H(X_n|X_1)$ increasing, while the summary's item 5 states $H(X_0|X_n)$ for general chains. The proof is deferred to Problem 35.
- **Not given in the text.** The weakening of Fano (2.144)→(2.145)–(2.146) is stated without derivation. The equality conditions in Jensen's inequality are left to the reader. Example 3 in 2.10 (uniform) is stated without proof.
- Problems are listed but not solved. Problem statements are summarised, not reproduced in full.