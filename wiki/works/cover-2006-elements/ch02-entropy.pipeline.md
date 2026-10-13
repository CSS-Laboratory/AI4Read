---
id: cover-2006-elements/ch02-entropy
work: cover-2006-elements
unit: "2 Entropy, Relative Entropy and Mutual Information"
pages: 12-49
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
spec_version: 1.1
verified: repaired
verifier_issues: 4
pipeline_version: 0.1
---
# Entropy, Relative Entropy and Mutual Information

## L0 — One line
Entropy, relative entropy and mutual information are linked by simple identities (chain rules), and one inequality, $D(p\|q)\ge 0$ (itself a consequence of Jensen's inequality), yields most of their key properties: conditioning reduces entropy, the data processing inequality, Fano's inequality, and a "second law" for Markov chains.

## L1 — The gist (≤ 120 words)
The chapter defines the basic quantities of information theory. Entropy $H(X)$ measures the uncertainty of a discrete random variable. Joint and conditional entropy extend it to several variables. Relative entropy $D(p\|q)$ measures the inefficiency of assuming $q$ when the truth is $p$. Mutual information $I(X;Y)$ is the relative entropy between the joint distribution and the product of the marginals. All are tied together by chain rules. Jensen's inequality gives non-negativity and the other inequalities. The author then proves the data processing inequality, shows that relative entropy shrinks along Markov chains (the "second law"), links sufficient statistics to mutual information, and proves Fano's inequality. These tools are used throughout the book (p. 12).

## L2 — Key ideas
- **Entropy** is $H(X)=-\sum p(x)\log p(x)=E\log\frac1{p(X)}$. It depends only on the probabilities, not on the values of $X$. It is $\ge 0$ and is maximal ($\log|\mathcal X|$) for the uniform law (pp. 13, 27).
- **Chain rule for entropy:** $H(X,Y)=H(X)+H(Y|X)$, and in general $H(X_1,\dots,X_n)=\sum_i H(X_i|X_{i-1},\dots,X_1)$. Uncertainty adds up step by step (pp. 16, 21).
- **Relative entropy** $D(p\|q)$ is $\ge 0$, and $=0$ iff $p=q$. It is not symmetric and has no triangle inequality, so it is not a true distance (pp. 18, 19, 26).
- **Mutual information** is $I(X;Y)=D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)=H(X)+H(Y)-H(X,Y)$. It is symmetric, $\ge 0$, and $0$ iff $X,Y$ are independent. $I(X;X)=H(X)$ (pp. 18–20, 27).
- **Jensen's inequality** ($Ef(X)\ge f(EX)$ for convex $f$) is the engine of the chapter. It gives $D\ge0$, and the log sum inequality gives convexity of $D$ and concavity of $H$ (pp. 25, 29, 30).
- **Conditioning reduces entropy on average**, but a particular observation can raise it (Example 2.6.1). Hence $H(X_1,\dots,X_n)\le\sum H(X_i)$ (pp. 27–28).
- **Data processing inequality:** if $X\to Y\to Z$ is a Markov chain, then $I(X;Y)\ge I(X;Z)$. No processing of data creates information about $X$. Sufficient statistics are exactly the case of equality (pp. 32, 36–37).
- **Second law for Markov chains:** relative entropy between two state distributions always decreases, but plain entropy increases only if the stationary law is uniform (pp. 33–35).
- **Fano's inequality** $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ lower-bounds the error of estimating $X$ from $Y$. It is sharp (pp. 38–40).

## L3 — Walkthrough

### Introduction (p. 12)
The chapter defines entropy and mutual information. It then proves chain rules, non-negativity of mutual information, and the data processing inequality, and finally studies the second law of thermodynamics for Markov processes. Entropy is the "self-information" of a variable. Mutual information is a special case of relative entropy, a "distance" between distributions (p. 12). The author says the later chapters (communication, statistics, complexity, gambling) are the real test of these definitions (p. 12).

### 2.1 Entropy (pp. 12–15)
Let $X$ be discrete with alphabet $\mathcal X$ and pmf $p(x)=\Pr\{X=x\}$. The author writes $p(x)$ and $p(y)$ for two different pmfs $p_X, p_Y$ (p. 13).

**Definition.**
$$H(X)=-\sum_{x\in\mathcal X}p(x)\log p(x).\tag{2.1}$$
- Also written $H(p)$.
- The log is base 2, so entropy is in bits. A fair coin toss has 1 bit.
- Convention: $0\log0=0$, justified by $x\log x\to0$ as $x\to0$. Terms of zero probability do not change $H$ (p. 13).
- For base $b$ the entropy is $H_b(X)$. For base $e$ the unit is the *nat* (p. 13).
- Entropy is a functional of the distribution: it ignores the actual values of $X$ (p. 13).

Expectation: if $X\sim p(x)$ then
$$E_pg(X)=\sum_{x\in\mathcal X}g(x)p(x).\tag{2.2}$$
**Remark.** Taking $g(X)=\log\frac1{p(X)}$ (the author calls this "eerily self-referential"):
$$H(X)=E_p\log\frac1{p(X)}.\tag{2.3}$$
The author notes a connection to thermodynamic entropy and an axiomatic derivation (Problem 4). He does not use the axiomatic route. Entropy will be justified as the answer to questions such as the average length of the shortest description of $X$ (pp. 13–14).

**Lemma 2.1.1.** $H(X)\ge0$. Proof: $0<p(x)\le1$ gives $\log(1/p(x))\ge0$ (p. 14).

**Lemma 2.1.2.** $H_b(X)=(\log_b a)H_a(X)$. Proof: $\log_b p=\log_b a\,\log_a p$ (p. 14).

**Example 2.1.1.** $X=1$ with probability $p$, $X=0$ with probability $1-p$:
$$H(X)=-p\log p-(1-p)\log(1-p)\overset{\text{def}}{=}H(p).\tag{2.5}$$
$H=1$ bit at $p=1/2$. $H(p)$ is concave, equals 0 at $p=0$ or $1$ (no randomness), and is maximal at $p=\tfrac12$ (Figure 2.1, pp. 14–15).

**Example 2.1.2.** $X=a,b,c,d$ with probabilities $\tfrac12,\tfrac14,\tfrac18,\tfrac18$:
$$H(X)=-\tfrac12\log\tfrac12-\tfrac14\log\tfrac14-\tfrac18\log\tfrac18-\tfrac18\log\tfrac18=\tfrac74\text{ bits}.\tag{2.7}$$
Ask "Is $X=a$?", then "Is $X=b$?", then "Is $X=c$?". The expected number of binary questions is $1.75$. This is the minimum. Chapter 5 shows that the minimum lies between $H(X)$ and $H(X)+1$ (p. 15).

> **Intuition note.** Entropy is the average number of yes/no questions needed to pin down the outcome. Likely outcomes get short question paths, rare ones long paths. Here the paths cost 1, 2, 3, 3 questions, and $\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=1.75$ (added step).

### 2.2 Joint entropy and conditional entropy (pp. 15–17)
A pair $(X,Y)$ is just one vector-valued variable.

**Definition (joint entropy).**
$$H(X,Y)=-\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}p(x,y)\log p(x,y)\tag{2.8}$$
$$=-E\log p(X,Y).\tag{2.9}$$

**Definition (conditional entropy).** If $(X,Y)\sim p(x,y)$:
$$H(Y|X)=\sum_{x}p(x)H(Y|X=x)\tag{2.10}$$
$$=-\sum_x p(x)\sum_y p(y|x)\log p(y|x)\tag{2.11}$$
$$=-\sum_x\sum_y p(x,y)\log p(y|x)\tag{2.12}$$
$$=-E_{p(x,y)}\log p(Y|X).\tag{2.13}$$
It is the average, over $x$, of the entropies of the conditional distributions (p. 16).

**Theorem 2.2.1 (Chain rule).** $H(X,Y)=H(X)+H(Y|X)$ (2.14). Proof:
$$H(X,Y)=-\sum_{x}\sum_{y}p(x,y)\log p(x,y)\tag{2.15}$$
$$=-\sum_{x}\sum_{y}p(x,y)\log p(x)p(y|x)\tag{2.16}$$
$$=-\sum_{x}\sum_{y}p(x,y)\log p(x)-\sum_{x}\sum_{y}p(x,y)\log p(y|x)\tag{2.17}$$
$$=-\sum_{x}p(x)\log p(x)-\sum_{x}\sum_{y}p(x,y)\log p(y|x)\tag{2.18}$$
$$=H(X)+H(Y|X).\tag{2.19}$$
Equivalently, $\log p(X,Y)=\log p(X)+\log p(Y|X)$ (2.20), then take expectations (p. 16).

**Corollary.** $H(X,Y|Z)=H(X|Z)+H(Y|X,Z)$ (2.21). The proof is the same as for the theorem (p. 17).

**Example 2.2.1.** Joint distribution of $(X,Y)$ (rows $Y$, columns $X$):

| Y\X | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 1/8 | 1/16 | 1/32 | 1/32 |
| 2 | 1/16 | 1/8 | 1/32 | 1/32 |
| 3 | 1/16 | 1/16 | 1/16 | 1/16 |
| 4 | 1/4 | 0 | 0 | 0 |

The marginal of $X$ is $(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$ and of $Y$ is $(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$. So $H(X)=7/4$ and $H(Y)=2$ bits (p. 17).
$$H(X|Y)=\sum_{i=1}^4p(Y=i)H(X|Y=i)=\tfrac14H(\tfrac12,\tfrac14,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac12,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac14,\tfrac14,\tfrac14)+\tfrac14H(1,0,0,0)\tag{2.22–2.23}$$
$$=\tfrac14\cdot\tfrac74+\tfrac14\cdot\tfrac74+\tfrac14\cdot2+\tfrac14\cdot0=\tfrac{11}8\text{ bits}.\tag{2.24–2.25}$$
Similarly $H(Y|X)=13/8$ and $H(X,Y)=27/8$ bits. **Remark:** $H(Y|X)\ne H(X|Y)$, but $H(X)-H(X|Y)=H(Y)-H(Y|X)$, a property used later (p. 17).

### 2.3 Relative entropy and mutual information (pp. 18–19)
Entropy measures the information needed on average to describe $X$. Relative entropy measures the inefficiency of assuming $q$ when the truth is $p$. A code built for $q$ needs $H(p)+D(p\|q)$ bits on average, instead of $H(p)$ (p. 18). In statistics it appears as an expected log-likelihood ratio (p. 18).

**Definition (relative entropy, Kullback–Leibler distance).**
$$D(p\|q)=\sum_{x\in\mathcal X}p(x)\log\frac{p(x)}{q(x)}\tag{2.26}$$
$$=E_p\log\frac{p(X)}{q(X)}.\tag{2.27}$$
Conventions: $0\log\frac0q=0$ and $p\log\frac p0=\infty$ (p. 18). It will be shown to be $\ge0$, with equality iff $p=q$. It is **not** a true distance: it is not symmetric and has no triangle inequality (p. 18).

**Definition (mutual information).** For joint pmf $p(x,y)$ with marginals $p(x),p(y)$:
$$I(X;Y)=\sum_{x\in\mathcal X}\sum_{y\in\mathcal Y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}\tag{2.28}$$
$$=D(p(x,y)\|p(x)p(y))\tag{2.29}$$
$$=E_{p(x,y)}\log\frac{p(X,Y)}{p(X)p(Y)}.\tag{2.30}$$
It is the reduction in the uncertainty of one variable due to knowing the other (pp. 18–19).

**Example 2.3.1.** $\mathcal X=\{0,1\}$, $p(0)=1-r,\ p(1)=r$, $q(0)=1-s,\ q(1)=s$:
$$D(p\|q)=(1-r)\log\frac{1-r}{1-s}+r\log\frac rs,\tag{2.31}$$
$$D(q\|p)=(1-s)\log\frac{1-s}{1-r}+s\log\frac sr.\tag{2.32}$$
If $r=s$, both are 0. For $r=\tfrac12,\ s=\tfrac14$:
$$D(p\|q)=\tfrac12\log\frac{1/2}{3/4}+\tfrac12\log\frac{1/2}{1/4}=1-\tfrac12\log3=0.2075\text{ bits},\tag{2.33}$$
$$D(q\|p)=\tfrac34\log\frac{3/4}{1/2}+\tfrac14\log\frac{1/4}{1/2}=\tfrac34\log3-1=0.1887\text{ bits}.\tag{2.34}$$
So $D(p\|q)\ne D(q\|p)$ in general (p. 19).

### 2.4 Relationship between entropy and mutual information (pp. 19–21)
$$I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}\tag{2.35}$$
$$=\sum_{x,y}p(x,y)\log\frac{p(x|y)}{p(x)}\tag{2.36}$$
$$=-\sum_{x,y}p(x,y)\log p(x)+\sum_{x,y}p(x,y)\log p(x|y)\tag{2.37}$$
$$=-\sum_xp(x)\log p(x)-\Big(-\sum_{x,y}p(x,y)\log p(x|y)\Big)\tag{2.38}$$
$$=H(X)-H(X|Y).\tag{2.39}$$
By symmetry $I(X;Y)=H(Y)-H(Y|X)$ (2.40). So $X$ says as much about $Y$ as $Y$ says about $X$. With the chain rule, $I(X;Y)=H(X)+H(Y)-H(X,Y)$ (2.41). Also $I(X;X)=H(X)-H(X|X)=H(X)$ (2.42), which is why entropy is called self-information (p. 20).

**Theorem 2.4.1 (Mutual information and entropy).**
$$I(X;Y)=H(X)-H(X|Y)\tag{2.43}$$
$$I(X;Y)=H(Y)-H(Y|X)\tag{2.44}$$
$$I(X;Y)=H(X)+H(Y)-H(X,Y)\tag{2.45}$$
$$I(X;Y)=I(Y;X)\tag{2.46}$$
$$I(X;X)=H(X)\tag{2.47}$$
Figure 2.2 shows these as a Venn diagram. $I(X;Y)$ is the intersection of the information in $X$ with that in $Y$ (pp. 20–21).

**Example 2.4.1.** For the distribution of Example 2.2.1, $I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)=0.375$ bits (p. 21).

> **Intuition note.** Mutual information is the overlap of two uncertainties: what you save in describing $X$ once $Y$ is known. The Venn picture is only an analogy (the author later notes three-way "overlap" can be negative, Problem 12).

### 2.5 Chain rules for entropy, relative entropy and mutual information (pp. 21–23)
**Theorem 2.5.1 (Chain rule for entropy).** For $X_1,\dots,X_n\sim p(x_1,\dots,x_n)$:
$$H(X_1,\dots,X_n)=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.48}$$
*Proof.* Repeat the two-variable rule:
$$H(X_1,X_2)=H(X_1)+H(X_2|X_1)\tag{2.49}$$
$$H(X_1,X_2,X_3)=H(X_1)+H(X_2,X_3|X_1)\tag{2.50}$$
$$=H(X_1)+H(X_2|X_1)+H(X_3|X_2,X_1)\tag{2.51}$$
$$\vdots$$
$$H(X_1,\dots,X_n)=H(X_1)+H(X_2|X_1)+\dots+H(X_n|X_{n-1},\dots,X_1)\tag{2.52}$$
$$=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.53}$$
*Alternative proof.* Write $p(x_1,\dots,x_n)=\prod_{i=1}^np(x_i|x_{i-1},\dots,x_1)$. Then
$$H(X_1,\dots,X_n)=-\sum_{x_1,\dots,x_n}p(x_1,\dots,x_n)\log p(x_1,\dots,x_n)\tag{2.54}$$
$$=-\sum p(x_1,\dots,x_n)\log\prod_{i=1}^np(x_i|x_{i-1},\dots,x_1)\tag{2.55}$$
$$=-\sum p(x_1,\dots,x_n)\sum_{i=1}^n\log p(x_i|x_{i-1},\dots,x_1)\tag{2.56}$$
$$=-\sum_{i=1}^n\sum_{x_1,\dots,x_n}p(x_1,\dots,x_n)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.57}$$
$$=-\sum_{i=1}^n\sum_{x_1,\dots,x_i}p(x_1,\dots,x_i)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.58}$$
$$=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.59}$$
(Step 2.57→2.58 sums out $x_{i+1},\dots,x_n$ (added step).)

**Definition (conditional mutual information).**
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)\tag{2.60}$$
$$=E_{p(x,y,z)}\log\frac{p(X,Y|Z)}{p(X|Z)p(Y|Z)}.\tag{2.61}$$

**Theorem 2.5.2 (Chain rule for information).**
$$I(X_1,\dots,X_n;Y)=\sum_{i=1}^nI(X_i;Y|X_{i-1},X_{i-2},\dots,X_1).\tag{2.62}$$
*Proof.*
$$I(X_1,\dots,X_n;Y)=H(X_1,\dots,X_n)-H(X_1,\dots,X_n|Y)\tag{2.63}$$
$$=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1)-\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1,Y)=\sum_{i=1}^nI(X_i;Y|X_1,\dots,X_{i-1}).\tag{2.64}$$

**Definition (conditional relative entropy).** It is the average over $p(x)$ of the relative entropies between $p(y|x)$ and $q(y|x)$:
$$D(p(y|x)\|q(y|x))=\sum_xp(x)\sum_yp(y|x)\log\frac{p(y|x)}{q(y|x)}\tag{2.65}$$
$$=E_{p(x,y)}\log\frac{p(Y|X)}{q(Y|X)}.\tag{2.66}$$
The notation omits $p(x)$, which is understood from context (pp. 22–23).

**Theorem 2.5.3 (Chain rule for relative entropy).**
$$D(p(x,y)\|q(x,y))=D(p(x)\|q(x))+D(p(y|x)\|q(y|x)).\tag{2.67}$$
*Proof.*
$$D(p(x,y)\|q(x,y))=\sum_x\sum_yp(x,y)\log\frac{p(x,y)}{q(x,y)}\tag{2.68}$$
$$=\sum_x\sum_yp(x,y)\log\frac{p(x)p(y|x)}{q(x)q(y|x)}\tag{2.69}$$
$$=\sum_x\sum_yp(x,y)\log\frac{p(x)}{q(x)}+\sum_x\sum_yp(x,y)\log\frac{p(y|x)}{q(y|x)}\tag{2.70}$$
$$=D(p(x)\|q(x))+D(p(y|x)\|q(y|x)).\tag{2.71}$$
This rule is used in Section 2.9 for the second law (p. 23).

> **Intuition note.** All three chain rules say the same thing. A joint quantity splits into "first variable" plus "second given the first", because $\log$ turns products of conditional probabilities into sums.

### 2.6 Jensen's inequality and its consequences (pp. 23–28)
**Definition.** $f$ is *convex* on $(a,b)$ if for all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$,
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2).\tag{2.72}$$
It is *strictly convex* if equality holds only for $\lambda=0$ or $1$. $f$ is *concave* if $-f$ is convex. A convex function lies below every chord; a concave function lies above (p. 23). Convex examples: $x^2$, $|x|$, $e^x$, $x\log x$ ($x\ge0$). Concave examples: $\log x$, $\sqrt x$ ($x\ge0$). Linear functions are both (p. 24).

**Theorem 2.6.1.** If $f''\ge0$ (resp. $>0$) everywhere, then $f$ is convex (strictly convex). *Proof.* Taylor expansion:
$$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x^*)}2(x-x_0)^2,\tag{2.73}$$
with $x^*$ between $x_0$ and $x$. The last term is $\ge0$. Put $x_0=\lambda x_1+(1-\lambda)x_2$ and take $x=x_1$:
$$f(x_1)\ge f(x_0)+f'(x_0)[(1-\lambda)(x_1-x_2)],\tag{2.74}$$
and $x=x_2$:
$$f(x_2)\ge f(x_0)+f'(x_0)[\lambda(x_2-x_1)].\tag{2.75}$$
Multiply (2.74) by $\lambda$ and (2.75) by $1-\lambda$ and add to get (2.72). Strict convexity is similar (pp. 24–25). Consequence: $x^2,e^x,x\log x$ are strictly convex, and $\log x,\sqrt x$ strictly concave, for $x\ge0$ (p. 25).

**Theorem 2.6.2 (Jensen's inequality).** If $f$ is convex,
$$Ef(X)\ge f(EX).\tag{2.76}$$
If $f$ is strictly convex, equality implies $X=EX$ with probability 1. *Proof* (discrete, by induction on the number of mass points). For two points it is the definition:
$$p_1f(x_1)+p_2f(x_2)\ge f(p_1x_1+p_2x_2).\tag{2.77}$$
Assume it holds for $k-1$ points. Put $p_i'=p_i/(1-p_k)$ for $i\le k-1$:
$$\sum_{i=1}^kp_if(x_i)=p_kf(x_k)+(1-p_k)\sum_{i=1}^{k-1}p_i'f(x_i)\tag{2.78}$$
$$\ge p_kf(x_k)+(1-p_k)f\Big(\sum_{i=1}^{k-1}p_i'x_i\Big)\tag{2.79}$$
$$\ge f\Big(p_kx_k+(1-p_k)\sum_{i=1}^{k-1}p_i'x_i\Big)\tag{2.80}$$
$$=f\Big(\sum_{i=1}^kp_ix_i\Big).\tag{2.81}$$
The first inequality is the induction hypothesis, the second is the definition of convexity. The equality case is left to the reader. Continuous distributions follow by continuity arguments (pp. 25–26).

**Theorem 2.6.3 (Information inequality).** For pmfs $p,q$ on $\mathcal X$:
$$D(p\|q)\ge0,\tag{2.82}$$
with equality iff $p(x)=q(x)$ for all $x$ (2.83). *Proof.* Let $A=\{x:p(x)>0\}$.
$$-D(p\|q)=-\sum_{x\in A}p(x)\log\frac{p(x)}{q(x)}\tag{2.84}$$
$$=\sum_{x\in A}p(x)\log\frac{q(x)}{p(x)}\tag{2.85}$$
$$\le\log\sum_{x\in A}p(x)\frac{q(x)}{p(x)}\tag{2.86}$$
$$=\log\sum_{x\in A}q(x)\tag{2.87}$$
$$\le\log\sum_{x\in\mathcal X}q(x)\tag{2.88}$$
$$=\log1=0.\tag{2.89–2.90}$$
Step (2.86) is Jensen with concave $\log$. Since $\log t$ is strictly concave, equality in (2.86) needs $q(x)/p(x)=1$ everywhere, so $p=q$ (p. 26).

> **Intuition note.** On average, a wrong model $q$ cannot assign higher log-probability to data from $p$ than $p$ itself does. This is the root of almost every inequality in the chapter.

**Corollaries (p. 27).**
- $I(X;Y)\ge0$, with equality iff $X,Y$ are independent (2.91). Proof: $I=D(p(x,y)\|p(x)p(y))$.
- $D(p(y|x)\|q(y|x))\ge0$, with equality iff $p(y|x)=q(y|x)$ for all $y$ and all $x$ with $p(x)>0$ (2.92).
- $I(X;Y|Z)\ge0$, with equality iff $X,Y$ are conditionally independent given $Z$ (2.93).

**Theorem 2.6.4.** $H(X)\le\log|\mathcal X|$, with equality iff $X$ is uniform on $\mathcal X$. *Proof.* With $u(x)=1/|\mathcal X|$:
$$D(p\|u)=\sum p(x)\log\frac{p(x)}{u(x)}=\log|\mathcal X|-H(X),\tag{2.94}$$
and $0\le D(p\|u)=\log|\mathcal X|-H(X)$ (2.95) (p. 27).

**Theorem 2.6.5 (Conditioning reduces entropy).** $H(X|Y)\le H(X)$ (2.96), with equality iff $X,Y$ are independent. Proof: $0\le I(X;Y)=H(X)-H(X|Y)$ (pp. 27–28). The statement holds only on average: $H(X|Y=y)$ may be larger or smaller than $H(X)$, but $\sum_yp(y)H(X|Y=y)\le H(X)$. In a court case, specific new evidence may raise uncertainty, but on average evidence lowers it (p. 28).

**Example 2.6.1.** Joint distribution: $p(X{=}1,Y{=}1)=0$, $p(X{=}2,Y{=}1)=\tfrac34$, $p(X{=}1,Y{=}2)=\tfrac18$, $p(X{=}2,Y{=}2)=\tfrac18$. Then $H(X)=H(\tfrac18,\tfrac78)=0.544$ bits, $H(X|Y=1)=0$, $H(X|Y=2)=1$ bit, and $H(X|Y)=\tfrac34\cdot0+\tfrac14\cdot1=0.25$ bits. Observing $Y=2$ raises the uncertainty in $X$, observing $Y=1$ lowers it, and on average it falls (p. 28).

**Theorem 2.6.6 (Independence bound on entropy).**
$$H(X_1,\dots,X_n)\le\sum_{i=1}^nH(X_i),\tag{2.97}$$
with equality iff the $X_i$ are independent. Proof: chain rule (2.98), then conditioning reduces entropy (2.99). Equality needs $X_i$ independent of $X_{i-1},\dots,X_1$ for all $i$ (p. 28).

### 2.7 The log sum inequality and its applications (pp. 29–31)
**Theorem 2.7.1 (Log sum inequality).** For non-negative $a_1,\dots,a_n$, $b_1,\dots,b_n$:
$$\sum_{i=1}^na_i\log\frac{a_i}{b_i}\ge\Big(\sum_{i=1}^na_i\Big)\log\frac{\sum_{i=1}^na_i}{\sum_{i=1}^nb_i},\tag{2.100}$$
with equality iff $a_i/b_i=$ const. Conventions: $0\log0=0$, $a\log\frac a0=\infty$ for $a>0$, $0\log\frac00=0$ (p. 29).

*Proof.* Assume $a_i,b_i>0$. $f(t)=t\log t$ is strictly convex because $f''(t)=\frac1t\log e>0$. Jensen gives
$$\sum\alpha_if(t_i)\ge f\Big(\sum\alpha_it_i\Big)\tag{2.101}$$
for $\alpha_i\ge0$, $\sum\alpha_i=1$. Put $\alpha_i=b_i/\sum_jb_j$ and $t_i=a_i/b_i$:
$$\sum\frac{a_i}{\sum b_j}\log\frac{a_i}{b_i}\ge\sum\frac{a_i}{\sum b_j}\log\sum\frac{a_i}{\sum b_j},\tag{2.102}$$
which is (2.100) after multiplying by $\sum b_j$ (added step) (p. 29).

**Reproof of Theorem 2.6.3.** $D(p\|q)=\sum p\log\frac pq\ge(\sum p)\log\frac{\sum p}{\sum q}=1\log\frac11=0$ (2.103–2.105). Equality iff $p(x)/q(x)=c$, and $c=1$ because both sum to 1 (p. 29).

**Theorem 2.7.2.** $D(p\|q)$ is convex in the pair $(p,q)$:
$$D(\lambda p_1+(1-\lambda)p_2\|\lambda q_1+(1-\lambda)q_2)\le\lambda D(p_1\|q_1)+(1-\lambda)D(p_2\|q_2).\tag{2.106}$$
*Proof.* Apply the log sum inequality to each $x$:
$$(\lambda p_1(x)+(1-\lambda)p_2(x))\log\frac{\lambda p_1(x)+(1-\lambda)p_2(x)}{\lambda q_1(x)+(1-\lambda)q_2(x)}\le\lambda p_1(x)\log\frac{\lambda p_1(x)}{\lambda q_1(x)}+(1-\lambda)p_2(x)\log\frac{(1-\lambda)p_2(x)}{(1-\lambda)q_2(x)}.\tag{2.107}$$
Sum over $x$ (p. 30).

**Theorem 2.7.3 (Concavity of entropy).** $H(p)$ is concave in $p$.
- *Proof 1:* $H(p)=\log|\mathcal X|-D(p\|u)$ (2.108), with $u$ uniform. Concavity follows from convexity of $D$.
- *Proof 2:* Let $X_1\sim p_1$ and $X_2\sim p_2$ on the same set. Let $\theta$ be an independent choice with $\Pr(\theta=1)=\lambda$, and let $Z=X_\theta$ (2.109). Then $Z\sim\lambda p_1+(1-\lambda)p_2$. Conditioning reduces entropy, so $H(Z)\ge H(Z|\theta)$ (2.110), i.e.
$$H(\lambda p_1+(1-\lambda)p_2)\ge\lambda H(p_1)+(1-\lambda)H(p_2).\tag{2.111}$$

The author notes a physical consequence: mixing two gases of equal entropy yields a gas of higher entropy (pp. 30–31).

**Theorem 2.7.4.** For $(X,Y)\sim p(x)p(y|x)$, $I(X;Y)$ is a *concave* function of $p(x)$ for fixed $p(y|x)$ and a *convex* function of $p(y|x)$ for fixed $p(x)$ (p. 31).
- *Part 1:* $I(X;Y)=H(Y)-H(Y|X)=H(Y)-\sum_xp(x)H(Y|X=x)$ (2.112). For fixed $p(y|x)$, $p(y)$ is linear in $p(x)$, so $H(Y)$ is concave in $p(x)$. The second term is linear in $p(x)$. So the difference is concave.
- *Part 2:* Fix $p(x)$ and take two channels $p_1(y|x),p_2(y|x)$. The mixture $p_\lambda(y|x)=\lambda p_1(y|x)+(1-\lambda)p_2(y|x)$ (2.113) gives the joint $p_\lambda(x,y)=\lambda p_1(x,y)+(1-\lambda)p_2(x,y)$ (2.114) and marginal $p_\lambda(y)=\lambda p_1(y)+(1-\lambda)p_2(y)$ (2.115). With $q_\lambda(x,y)=p(x)p_\lambda(y)$ we get $q_\lambda=\lambda q_1+(1-\lambda)q_2$ (2.116). Since $I(X;Y)=D(p_\lambda\|q_\lambda)$ (2.117) and $D$ is jointly convex, $I$ is convex in $p(y|x)$.

> **Intuition note.** Mixing distributions never lowers entropy (concavity). Information through a channel is concave in the input law and convex in the channel.

### 2.8 Data processing inequality (pp. 32–33)
**Definition.** $X,Y,Z$ form a *Markov chain* $X\to Y\to Z$ if
$$p(x,y,z)=p(x)p(y|x)p(z|y).\tag{2.118}$$
Consequences (p. 32):
- $X\to Y\to Z$ iff $X$ and $Z$ are conditionally independent given $Y$: $p(x,z|y)=\frac{p(x,y,z)}{p(y)}=\frac{p(x,y)p(z|y)}{p(y)}=p(x|y)p(z|y)$ (2.119). This characterization extends to Markov fields (interior and exterior independent given the boundary).
- $X\to Y\to Z$ implies $Z\to Y\to X$, so it is sometimes written $X\leftrightarrow Y\leftrightarrow Z$.
- If $Z=f(Y)$, then $X\to Y\to Z$.

**Theorem 2.8.1 (Data processing inequality).** If $X\to Y\to Z$ then $I(X;Y)\ge I(X;Z)$. *Proof.* Expand $I(X;Y,Z)$ two ways by the chain rule:
$$I(X;Y,Z)=I(X;Z)+I(X;Y|Z)\tag{2.120}$$
$$=I(X;Y)+I(X;Z|Y)\quad\text{(intended form of 2.121; see Reading notes)}.$$
Markovity gives $I(X;Z|Y)=0$, and $I(X;Y|Z)\ge0$, so
$$I(X;Y)\ge I(X;Z).\tag{2.122}$$
Equality iff $I(X;Y|Z)=0$, i.e. $X\to Z\to Y$ is also a Markov chain. Similarly $I(Y;Z)\ge I(X;Z)$ (pp. 32–33).

**Corollary.** $I(X;Y)\ge I(X;g(Y))$, because $X\to Y\to g(Y)$ is Markov. Functions of the data cannot increase information about $X$ (p. 33).

**Corollary.** If $X\to Y\to Z$, then $I(X;Y|Z)\le I(X;Y)$ (2.123). This follows from (2.120)–(2.121) with $I(X;Z|Y)=0$ and $I(X;Z)\ge0$. Observing a downstream variable cannot increase the dependence of $X$ and $Y$ (p. 33).

**Warning example.** Without Markovity, $I(X;Y|Z)>I(X;Y)$ is possible. Let $X,Y$ be independent fair bits and $Z=X+Y$. Then $I(X;Y)=0$, but
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=H(X|Z)=P(Z=1)H(X|Z=1)=\tfrac12\text{ bit}.$$
(p. 33)

> **Intuition note.** Every extra processing step is a (possibly lossy) channel. Information can only leak away along a chain, never be created.

### 2.9 The second law of thermodynamics (pp. 33–36)
The second law says the entropy of an isolated system is non-decreasing. In statistical thermodynamics, entropy is the log of the number of microstates, which matches $H$ when all states are equally likely. The author models the isolated system as a Markov chain with transitions obeying the physics (p. 33). He says there are four interpretations of the second law, and then lists five (pp. 34–36). He warns that plain entropy does not always increase, but *relative* entropy always decreases (pp. 33–34).

**1. $D(\mu_n\|\mu_n')$ decreases with $n$.** Let $\mu_n,\mu_n'$ be two distributions on the states at time $n$, with joint laws $p(x_n,x_{n+1})=p(x_n)r(x_{n+1}|x_n)$ and $q(x_n,x_{n+1})=q(x_n)r(x_{n+1}|x_n)$, where $r$ is the transition function. By the chain rule for relative entropy, two expansions:
$$D(p(x_n,x_{n+1})\|q(x_n,x_{n+1}))=D(p(x_n)\|q(x_n))+D(p(x_{n+1}|x_n)\|q(x_{n+1}|x_n))$$
$$=D(p(x_{n+1})\|q(x_{n+1}))+D(p(x_n|x_{n+1})\|q(x_n|x_{n+1})).$$
The conditionals $p(x_{n+1}|x_n),q(x_{n+1}|x_n)$ both equal $r$, so the first conditional term is 0. The last term is $\ge0$ by the corollary to Theorem 2.6.3. Hence
$$D(p(x_n)\|q(x_n))\ge D(p(x_{n+1})\|q(x_{n+1})),\tag{2.124}$$
$$D(\mu_n\|\mu_n')\ge D(\mu_{n+1}\|\mu_{n+1}').\tag{2.125}$$
The author's illustration: if the tax redistribution system is the same in Canada and England, the relative-entropy distance between the two wealth distributions decreases with time (p. 34).

**2. $D(\mu_n\|\mu)$ to a stationary $\mu$ decreases.** Take $\mu_n'=\mu$ stationary, so $\mu_{n+1}'=\mu$ too:
$$D(\mu_n\|\mu)\ge D(\mu_{n+1}\|\mu).\tag{2.126}$$
Any state distribution gets closer to each stationary distribution. The sequence is non-increasing and non-negative, so it has a limit. The limit is 0 if the stationary distribution is unique, which the author says is harder to prove (pp. 34–35).

**3. Entropy increases if the stationary distribution is uniform.** Decreasing relative entropy does not by itself imply increasing entropy. Counterexample: any chain with a non-uniform stationary law, started from the uniform law (maximum entropy), tends to a stationary law with lower entropy (p. 35). If the stationary law is uniform:
$$D(\mu_n\|\mu)=\log|\mathcal X|-H(\mu_n)=\log|\mathcal X|-H(X_n),\tag{2.127}$$
so the monotone decrease of $D$ is a monotone increase of $H(X_n)$. This matches statistical thermodynamics, where all microstates are equally likely (p. 35).

**Definition.** A transition matrix $[P_{ij}]$, $P_{ij}=\Pr\{X_{n+1}=j|X_n=i\}$, is *doubly stochastic* if
$$\sum_iP_{ij}=1,\ j=1,2,\dots\tag{2.128}$$
$$\sum_jP_{ij}=1,\ i=1,2,\dots\tag{2.129}$$
**Remark.** The uniform distribution is stationary for $P$ iff $P$ is doubly stochastic (see Problem 1, Chapter 4) (p. 35).

**4. $H(X_n|X_1)$ increases with $n$ for a stationary Markov process.** $H(X_n)$ is constant, but the conditional uncertainty of the future grows. Proof 1:
$$H(X_n|X_1)\ge H(X_n|X_1,X_2)\ \text{(conditioning reduces entropy)}\tag{2.130}$$
$$=H(X_n|X_2)\ \text{(Markovity)}\tag{2.131}$$
$$=H(X_{n-1}|X_1)\ \text{(stationarity)}.\tag{2.132}$$
Proof 2: apply the data processing inequality to $X_1\to X_{n-1}\to X_n$:
$$I(X_1;X_{n-1})\ge I(X_1;X_n),\tag{2.133}$$
$$H(X_{n-1})-H(X_{n-1}|X_1)\ge H(X_n)-H(X_n|X_1).\tag{2.134}$$
Stationarity gives $H(X_{n-1})=H(X_n)$, hence
$$H(X_{n-1}|X_1)\le H(X_n|X_1).\tag{2.135}$$
The same techniques show $H(X_0|X_n)$ increases in $n$ for any Markov chain (Problem 35) (pp. 35–36).

**5. Shuffles increase entropy.** If $T$ is a shuffle (permutation) of a deck, independent of the initial arrangement $X$, then
$$H(TX)\ge H(X).\tag{2.136}$$
Problem 31 outlines the proof (p. 36).

> **Intuition note.** A Markov chain forgets its past, so two different starting beliefs become indistinguishable ($D$ falls). The *entropy* of the state, however, can fall if the chain settles on a non-uniform stationary law. Entropy rises only toward the uniform law, the maximum.

### 2.10 Sufficient statistics (pp. 36–38)
Let $\{f_\theta(x)\}$ be a family of pmfs indexed by $\theta$. Let $X$ be a sample and $T(X)$ any statistic. Then $\theta\to X\to T(X)$, so by data processing
$$I(\theta;T(X))\le I(\theta;X)\tag{2.137}$$
for any distribution on $\theta$. Equality means no information is lost (p. 36).

**Definition.** $T(X)$ is a *sufficient statistic* relative to $\{f_\theta\}$ if $\theta\to T(X)\to X$ is a Markov chain, i.e. $X$ is independent of $\theta$ given $T(X)$. This is the equality condition of the data processing inequality:
$$I(\theta;X)=I(\theta;T(X))\tag{2.138}$$
for all distributions on $\theta$. So sufficient statistics preserve mutual information, and conversely (p. 37).

**Examples (pp. 37–38).**
1. $X_1,\dots,X_n$ i.i.d. coin tosses with $\theta=\Pr(X_i=1)$. $T=\sum X_i$ is sufficient. Given $T=k$ all sequences with $k$ ones are equally likely and independent of $\theta$:
$$\Pr\{(X_1,\dots,X_n)=(x_1,\dots,x_n)\mid\textstyle\sum X_i=k\}=\begin{cases}\frac1{\binom nk}&\text{if }\sum x_i=k,\\0&\text{otherwise.}\end{cases}\tag{2.139}$$
So $\theta\to\sum X_i\to(X_1,\dots,X_n)$ is Markov.
2. $f_\theta(x)=\frac1{\sqrt{2\pi}}e^{-(x-\theta)^2/2}=\mathcal N(\theta,1)$ (2.140), $X_i$ i.i.d. The sample mean $\bar X_n=\frac1n\sum X_i$ is sufficient. The conditional law of the sample given $\bar X_n$ and $n$ does not depend on $\theta$. (Entropy for continuous variables is defined in Chapter 9.)
3. $f_\theta=\mathrm{Uniform}(\theta,\theta+1)$. A sufficient statistic is
$$T(X_1,\dots,X_n)=(\max\{X_1,\dots,X_n\},\min\{X_1,\dots,X_n\}).\tag{2.141}$$
The author says the proof is "slightly more complicated".

**Definition (minimal sufficient statistic).** $T(X)$ is minimal sufficient if it is a function of every other sufficient statistic $U$. In terms of data processing:
$$\theta\to T(X)\to U(X)\to X.\tag{2.142}$$
A minimal sufficient statistic maximally compresses the information about $\theta$. Example of a non-minimal one: for $\mathcal N(\theta,1)$, the pair (mean of odd samples, mean of even samples) is sufficient but not minimal. In the three examples above the statistics are also minimal (p. 38).

### 2.11 Fano's inequality (pp. 38–40)
$H(X|Y)=0$ iff $X$ is a function of $Y$ (a fact the author takes from the problems), so $X$ can be estimated from $Y$ with zero error iff $H(X|Y)=0$. Fano's inequality quantifies "low error needs small $H(X|Y)$". It is crucial for the converse of Shannon's second theorem (Chapter 8) (p. 38). Observe $Y\sim p(y|x)$ and compute $\hat X=g(Y)$. Then $X\to Y\to\hat X$ is Markov. Define
$$P_e=\Pr\{\hat X\ne X\}.\tag{2.143}$$

**Theorem 2.11.1 (Fano's inequality).**
$$H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y).\tag{2.144}$$
Weakened forms:
$$1+P_e\log|\mathcal X|\ge H(X|Y),\tag{2.145}$$
$$P_e\ge\frac{H(X|Y)-1}{\log|\mathcal X|}.\tag{2.146}$$
$P_e=0$ implies $H(X|Y)=0$ (p. 39).

*Proof.* Define the error variable $E=1$ if $\hat X\ne X$, else $0$ (2.147). Expand $H(E,X|Y)$ two ways by the chain rule:
$$H(E,X|Y)=H(X|Y)+\underbrace{H(E|X,Y)}_{=0}\tag{2.148}$$
$$=\underbrace{H(E|Y)}_{\le H(P_e)}+\underbrace{H(X|E,Y)}_{\le P_e\log(|\mathcal X|-1)}.\tag{2.149}$$
- $H(E|Y)\le H(E)=H(P_e)$, since conditioning reduces entropy and $E$ is binary.
- $H(E|X,Y)=0$ because $E$ is a function of $X$ and $g(Y)$.
- Bounding the last term:
$$H(X|E,Y)=\Pr(E{=}0)H(X|Y,E{=}0)+\Pr(E{=}1)H(X|Y,E{=}1)\tag{2.150}$$
$$\le(1-P_e)\,0+P_e\log(|\mathcal X|-1).\tag{2.151}$$
Given $E=0$, $X=g(Y)$. Given $E=1$, the conditional entropy is at most the log of the number of remaining outcomes ($|\mathcal X|-1$ if $g(Y)\in\mathcal X$, else $|\mathcal X|$) (pp. 39–40).

**Remark (sharpness, no $Y$).** Guess $X\in\{1,\dots,m\}$ with $p_1\ge\dots\ge p_m$. Best guess $\hat X=1$ and $P_e=1-p_1$. Fano becomes
$$H(P_e)+P_e\log(m-1)\ge H(X).\tag{2.152}$$
The pmf
$$(p_1,\dots,p_m)=\Big(1-P_e,\frac{P_e}{m-1},\dots,\frac{P_e}{m-1}\Big)\tag{2.153}$$
achieves equality, so Fano's inequality is sharp (p. 40).

> **Intuition note.** If, after seeing $Y$, you are still left with $H(X|Y)$ bits of doubt, you must make mistakes at least at the rate that pays for those bits: one bit for "was I wrong?", plus $\log(|\mathcal X|-1)$ bits for "which other value?".

### Summary of Chapter 2 (pp. 40–42)
The author's own summary lists:
- the definitions (2.154–2.162);
- properties of $H$: $H\ge0$, change of base, conditioning reduces entropy, independence bound, $H\le\log|\mathcal X|$, concavity;
- properties of $D$ and $I$, including $D(p\|u)=\log m-H(p)$ and convexity of $D$ in $(p,q)$;
- the three chain rules, Jensen, and the log sum inequality (2.163);
- the data processing inequality, the five "second law" statements, the sufficient-statistic criterion, and Fano (2.164).

### Problems for Chapter 2 (pp. 42–49)
There are 35 problems. Examples: coin flips until the first head (Problem 1), entropy of functions (Problems 2, 5), the axiomatic derivation of entropy from normalization, continuity and grouping (Problem 4), bent coins and pure randomness (Problem 7), the World Series (Problem 8), infinite entropy (Problem 9), three-way $I(X;Y;Z)$ (Problem 12), coin weighing (Problem 13), the metric $\rho(X,Y)=H(X|Y)+H(Y|X)$ (Problem 15), bottleneck (Problem 22), shuffles (Problem 31), and Fano without conditioning (Problem 33).

### Historical notes (p. 49)
- Entropy came from thermodynamics. Boltzmann had $S=k\ln W$ on his gravestone.
- Hartley introduced a logarithmic information measure in the 1930s.
- Shannon defined entropy and mutual information as used here.
- Kullback and Leibler defined relative entropy. It is also known as cross entropy, information divergence, and information for discrimination.
- Fano proved his inequality. Fisher defined sufficient statistics. Lehmann and Scheffé introduced minimal sufficiency. Kullback linked mutual information and sufficiency.
- Thermodynamics and information were discussed by Brillouin and Jaynes, and limits to computation by Bennett and Landauer (p. 49).

## Toy example (ours, not from the text)
**Setup.** $X$ is a fair bit. $Y$ is $X$ flipped with probability $\tfrac14$. $Z$ is $Y$ flipped again, independently, with probability $\tfrac14$. So $X\to Y\to Z$ is a Markov chain.

**Entropy of the noise.** $H(\tfrac14)=-\tfrac14\log\tfrac14-\tfrac34\log\tfrac34=\tfrac14\cdot2+\tfrac34\cdot0.41504=0.5+0.31128=0.8113$ bits (using $\log_2\frac43=0.41504$).

**Chain rule and $I(X;Y)$.** $Y$ is uniform, so $H(Y)=1$. $H(Y|X)=H(\tfrac14)=0.8113$. Then $H(X,Y)=H(X)+H(Y|X)=1+0.8113=1.8113$. Then $I(X;Y)=H(X)+H(Y)-H(X,Y)=1+1-1.8113=0.1887$. This equals $H(Y)-H(Y|X)=1-0.8113=0.1887$ (identities 2.44, 2.45).

**$I(X;Z)$.** $Z\ne X$ iff exactly one of the two flips happens: probability $2\cdot\tfrac14\cdot\tfrac34=\tfrac38$. $Z$ is uniform, so $I(X;Z)=1-H(\tfrac38)$.
- $\log_2\tfrac38=\log_23-3=-1.41504$, so $\tfrac38\cdot1.41504=0.53064$.
- $\log_2\tfrac58=\log_25-3=-0.67807$, so $\tfrac58\cdot0.67807=0.42379$.
- $H(\tfrac38)=0.95443$, so $I(X;Z)=0.0456$.

**Data processing check.** $I(X;Y)=0.1887\ge I(X;Z)=0.0456$ ✓.

**Fano check.** Guess $\hat X=Y$. Then $P_e=\tfrac14$ and $|\mathcal X|=2$, so $\log(|\mathcal X|-1)=0$. Fano says $H(\tfrac14)\ge H(X|Y)$. Here $H(X|Y)=H(X)-I(X;Y)=1-0.1887=0.8113$, so Fano holds with equality (2.144).

## Concepts
- [[bit]] — unit of entropy when the log is base 2; a fair coin toss is 1 bit (p. 13)
- [[self-information]] — $\log\frac1{p(x)}$; entropy is its expectation, and $I(X;X)=H(X)$ is why entropy is called self-information (pp. 13, 20)
- [[entropy]] — $H(X)=-\sum p\log p=E\log\frac1{p(X)}$; $\ge0$, $\le\log|\mathcal X|$, concave in $p$ (pp. 13, 27, 30)
- [[joint-and-conditional-entropy]] — $H(X,Y)$ and $H(Y|X)=\sum_xp(x)H(Y|X=x)$ (pp. 15–16)
- [[chain-rule]] — $H(X,Y)=H(X)+H(Y|X)$ and its versions for $I$ and $D$ (pp. 16, 21–23)
- [[mutual-information]] — $I(X;Y)=D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$; symmetric, $\ge0$ (pp. 18–20, 27)
- [[relative-entropy-kl-divergence]] — $D(p\|q)$; $\ge0$, asymmetric, convex in $(p,q)$ (pp. 18, 26, 30)
- [[data-processing-inequality]] — $X\to Y\to Z$ implies $I(X;Y)\ge I(X;Z)$ (p. 32)
- [[fanos-inequality]] — $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ (p. 39)
- [[maximum-entropy-principle]] — only its simplest case appears: the uniform law maximizes $H$ over a given alphabet (p. 27)
- [[conditional-mutual-information]] (new) — $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)\ge0$ (pp. 22, 27)
- [[jensens-inequality]] (new) — $Ef(X)\ge f(EX)$ for convex $f$ (p. 25)
- [[log-sum-inequality]] (new) — $\sum a_i\log\frac{a_i}{b_i}\ge(\sum a_i)\log\frac{\sum a_i}{\sum b_i}$ (p. 29)
- [[markov-chain-information]] (new) — $X\to Y\to Z$ iff $p(x,y,z)=p(x)p(y|x)p(z|y)$, iff $X\perp Z\mid Y$ (p. 32)
- [[sufficient-statistic]] (new) — $T(X)$ with $\theta\to T(X)\to X$; equals equality in data processing (p. 37)
- [[doubly-stochastic-matrix]] (new) — rows and columns sum to 1; uniform law is stationary iff doubly stochastic (p. 35)

## Canonical instances
- [[binary-entropy-function]] — $H(p)$, concave, 1 bit at $p=\tfrac12$ (p. 14)
- [[four-symbol-source-7-4-bits]] — probabilities $\tfrac12,\tfrac14,\tfrac18,\tfrac18$ give $H=7/4$ and 1.75 expected questions (pp. 14–15)
- [[joint-table-4x4-example]] — $H(X)=7/4$, $H(Y)=2$, $H(X|Y)=11/8$, $H(Y|X)=13/8$, $H(X,Y)=27/8$, $I=0.375$ (pp. 17, 21)
- [[kl-asymmetry-bernoulli]] — $D(p\|q)=0.2075\ne D(q\|p)=0.1887$ bits for $r=\tfrac12,s=\tfrac14$ (p. 19)
- [[conditioning-can-increase-entropy-example]] — $H(X|Y=2)=1>H(X)=0.544$ but $H(X|Y)=0.25$ (p. 28)
- [[sum-conditional-mi-example]] — $Z=X+Y$ gives $I(X;Y)=0$ but $I(X;Y|Z)=\tfrac12$ bit (p. 33)
- [[canada-england-wealth-distributions]] — relative entropy between wealth distributions falls under identical tax systems (p. 34)
- [[coin-toss-sufficient-statistic]] — number of ones is sufficient for Bernoulli $\theta$ (p. 37)
- [[gaussian-mean-sufficient-statistic]] — sample mean is sufficient for $\mathcal N(\theta,1)$ (p. 37)
- [[uniform-theta-minmax-statistic]] — (max, min) is sufficient for Uniform$(\theta,\theta+1)$ (p. 38)
- [[shuffle-entropy-increase]] — $H(TX)\ge H(X)$ for a shuffle independent of the deck (p. 36)

## Bridges (candidates)
- [same-math] $D(p\|q)\ge0$ via Jensen on $\log$ ↔ statistics: Gibbs' inequality and non-negativity of expected log-likelihood ratio — same expectation of $\log(p/q)$ under $p$; the book itself says $D$ arises as an expected log-likelihood ratio (p. 18).
- [structural-analogy] Fano's inequality ↔ statistical decision theory: lower bounds on estimation error from conditional entropy — both bound the error of guessing $X$ from $Y$ (p. 38).
- [same-math] Sufficient statistic ($I(\theta;T)=I(\theta;X)$) ↔ statistics: Fisher/Neyman sufficiency — the author defines it by $\theta\to T\to X$ being Markov (p. 37).
- [structural-analogy] $H(X_n|X_1)$ increasing and $D(\mu_n\|\mu)$ decreasing ↔ physics: the second law of thermodynamics — the same monotone quantities, but only for uniform stationary laws is $H$ itself monotone (pp. 33–35).
- [structural-analogy] Data processing inequality ↔ computational social science: any aggregation, coarse-graining or feature extraction cannot add information about the latent variable of interest (p. 32).
- [metaphor] Venn diagram of $H$ and $I$ ↔ set measure: entropies as areas — the three-variable analogue can go negative (Problem 12, p. 45).

## Questions this raises
- If $D(p\|q)$ is not a metric, which symmetrized versions (e.g. $H(X|Y)+H(Y|X)$ in Problem 15, p. 45) are true metrics, and what do they measure?
- Entropy of $X_n$ may fall under a non-uniform stationary law, so what exactly is the thermodynamic entropy a model of a Markov chain should track (p. 35)?
- How does Fano's inequality become the converse of the noisy-channel theorem, as promised for Chapter 8 (p. 38)?
- The entropy of a discrete variable can be infinite (Problem 9). What changes for continuous variables (Chapter 9, p. 37)?

## Exercises worth doing
- Ex. 1 (p. 42) — entropy of a geometric variable and matching it to a question strategy — easy
- Ex. 5 (p. 43) — $H(g(X))\le H(X)$ via the chain rule applied two ways — easy
- Ex. 12 (p. 45) — three-way $I(X;Y;Z)$ can be negative; two identities — medium
- Ex. 15 (p. 45) — $H(X|Y)+H(Y|X)$ is a metric; use the triangle inequality and data processing — medium
- Ex. 22 (p. 47) — bottleneck: $I(X_1;X_3)\le\log k$ — medium
- Ex. 31 (p. 48) — shuffles increase entropy, a step-by-step argument — medium

## Reading notes
- **Edition.** The PDF is the 1991 first edition (Wiley copyright line on p. 12), not the 2006 second edition. Numbering and content differ from the 2nd edition (e.g. no universal source coding or portfolio-theory chapters). Page numbers cited here are first-edition printed pages.
- **OCR.** The text layer is garbled in many places (e.g. headers read "36", "38" for printed pages 16, 18; sub/superscripts lost). I checked all equations against the page images. In Example 2.1.1 the displayed cases of (2.4) were missing in the text layer, but the image is clear.
- **Misprint (p. 32).** (2.120)–(2.121) show the same right-hand side, $I(X;Z)+I(X;Y|Z)$, twice. The second should be $I(X;Y)+I(X;Z|Y)$. This is what the proof uses ($I(X;Z|Y)=0$). I wrote the intended form and marked it.
- **Inconsistency (p. 33).** The author says "four different interpretations" of the second law, but five are listed on pp. 34–36 and in the summary (p. 42).
- **Notation.** In the alternative proof of Theorem 2.7.3, the OCR reads "$Z=X_0$"; the image shows the choice variable (written $\theta$ here). I used $\theta$ for clarity.
- **Skipped.** The author leaves the equality case of Jensen (p. 25), the Uniform($\theta,\theta+1$) sufficiency proof (p. 38), and the uniqueness of the stationary limit (p. 35) unproved. I have not filled these in.
- **Exercises.** The problems are listed but not solved. Problem 4 is flagged by the author as much harder than the rest (p. 43).
