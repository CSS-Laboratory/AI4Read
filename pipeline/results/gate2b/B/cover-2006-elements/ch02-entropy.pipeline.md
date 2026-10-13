---
id: cover-2006-elements/ch02-entropy
work: cover-2006-elements
unit: "2 Entropy, Relative Entropy and Mutual Information"
pages: 12–49
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Entropy, Relative Entropy and Mutual Information

## L0 — One line
Entropy measures uncertainty, relative entropy measures the cost of using the wrong distribution, and mutual information measures uncertainty removed by another variable; Jensen's inequality makes relative entropy and mutual information non-negative, which in turn yields the data processing inequality: no processing of data can increase the information it carries about its source.

## L1 — The gist (≤ 120 words)
This chapter defines the basic quantities of information theory for discrete random variables: entropy (uncertainty), joint and conditional entropy, relative entropy (a non-symmetric "distance" between distributions) and mutual information (uncertainty about one variable removed by knowing another). It proves chain rules, non-negativity of relative entropy and mutual information (via Jensen's inequality), that conditioning reduces entropy on average, and the data processing inequality: for a Markov chain X→Y→Z, processing Y cannot increase information about X. It then studies entropy under Markov chains (the "second law"), sufficient statistics, and Fano's inequality, which bounds guessing error from conditional entropy. Later chapters use these tools.

**Prerequisites:** discrete probability and expectation; base-2 logarithms; conditional probability; Taylor expansion to second order; transition probabilities of a Markov chain (a matrix $[P_{ij}]$ whose rows give next-state probabilities).

## L2 — Key ideas
- Entropy $H(X)=-\sum p(x)\log p(x)$ depends only on the probabilities, is $\ge 0$, and equals $E\log\frac1{p(X)}$. It is 1 bit for a fair coin and is at most $\log|\mathcal X|$, with equality iff $X$ is uniform (pp. 13–14, 27).
- The chain rule $H(X,Y)=H(X)+H(Y|X)$ extends to $n$ variables. Mutual information and relative entropy have chain rules too (pp. 16, 21–23).
- Relative entropy $D(p\|q)$ is the expected log-likelihood ratio, or the extra bits paid for using $q$'s code when the truth is $p$. It is not symmetric and fails the triangle inequality (pp. 18–19).
- Mutual information is $D(p(x,y)\|p(x)p(y))$ and equals $H(X)-H(X|Y)$. It is symmetric, and $I(X;X)=H(X)$ (pp. 18–20).
- Jensen's inequality ($Ef(X)\ge f(EX)$ for convex $f$) gives $D\ge0$ with equality iff $p=q$. From this follow $I\ge0$, $H(X|Y)\le H(X)$ (on average), and $H(X_1,\dots,X_n)\le\sum H(X_i)$ (pp. 25–28).
- The log sum inequality gives convexity of $D$ in the pair $(p,q)$, concavity of $H(p)$, and concavity/convexity of $I$ in $p(x)$ / in $p(y|x)$ (pp. 29–31).
- Data processing: if $X\to Y\to Z$ is a Markov chain, then $I(X;Y)\ge I(X;Z)$. This characterises sufficient statistics as those with $I(\theta;X)=I(\theta;T(X))$ (pp. 32–37).
- For Markov chains, entropy need not increase, but relative entropy to a second chain or to a stationary distribution never increases. Entropy increases if the stationary distribution is uniform (pp. 33–36).
- Fano's inequality, $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$, bounds the error of estimating $X$ from $Y$ below in terms of $H(X|Y)$ (pp. 38–40).

## L3 — Walkthrough

### Chapter introduction (p. 12)
The author says the concept of information is too broad for a single definition. For any distribution, though, entropy has properties that agree with the intuitive notion of a measure of information (p. 12). Mutual information extends it. Entropy then becomes the "self-information" of a random variable. Mutual information is a special case of relative entropy (p. 12). The chapter proves chain rules, non-negativity of mutual information, the data processing inequality, and examines the second law of thermodynamics for Markov processes. The final test of these definitions is said to be how they answer questions in later chapters (p. 12).

### 2.1 Entropy (pp. 12–15)
Notation: $X$ is discrete with alphabet $\mathcal X$ and pmf $p(x)=\Pr\{X=x\}$. $p(x)$ and $p(y)$ denote two different pmfs, $p_X$ and $p_Y$ (p. 13).

**Definition (entropy).**
$$H(X)=-\sum_{x\in\mathcal X}p(x)\log p(x).\tag{2.1}$$
- Also written $H(p)$. Log is base 2 and entropy is in bits. A fair coin toss has 1 bit (p. 13).
- Convention: $0\log0=0$, justified by continuity since $x\log x\to0$ as $x\to0$. So adding zero-probability terms changes nothing (p. 13).
- With log base $b$ the entropy is written $H_b(X)$. Base $e$ gives "nats" (p. 13).
- Entropy is a functional of the distribution. It does not depend on the values $X$ takes, only on their probabilities (p. 13).
- Expectation: $E_p g(X)=\sum_x g(x)p(x)$ (2.2). With $g(X)=\log\frac1{p(X)}$ this gives the remark
$$H(X)=E_p\log\frac1{p(X)}.\tag{2.3}$$
- The author notes a link to thermodynamic entropy, and that an axiomatic derivation exists (Problem 4). He does not use it. Instead he shows entropy arises as the answer to natural questions, e.g. the average length of the shortest description (pp. 13–14).

**Lemma 2.1.1:** $H(X)\ge0$. *Proof:* $0<p(x)\le1$ implies $\log(1/p(x))\ge0$ (p. 14).

**Lemma 2.1.2:** $H_b(X)=(\log_b a)H_a(X)$. *Proof:* $\log_b p=\log_b a\,\log_a p$ (p. 14). Changing base multiplies entropy by a constant factor (p. 14).

**Example 2.1.1 (binary).** $X=1$ with probability $p$, $0$ with probability $1-p$. Then
$$H(X)=-p\log p-(1-p)\log(1-p)\overset{\text{def}}{=}H(p).\tag{2.5}$$
$H(X)=1$ bit at $p=1/2$. Figure 2.1 shows $H(p)$ is concave in $p$, equals 0 at $p=0$ or $1$ (no randomness), and is maximal at $p=1/2$ (p. 14).

**Example 2.1.2.** $X=a,b,c,d$ with probabilities $1/2,1/4,1/8,1/8$.
$$H(X)=-\tfrac12\log\tfrac12-\tfrac14\log\tfrac14-\tfrac18\log\tfrac18-\tfrac18\log\tfrac18=\tfrac74\text{ bits}.\tag{2.7}$$
Asking "Is $X=a$?", then "Is $X=b$?", then "Is $X=c$?" gives an expected 1.75 questions. This is the minimum expected number of binary questions. In Chapter 5 the author shows the minimum lies between $H(X)$ and $H(X)+1$ (p. 15).

*Intuition note.* The smallest expected number of yes/no questions needed to pin down $X$ lies between $H(X)$ and $H(X)+1$ (p. 15), so entropy is roughly that number. Likely outcomes get short question chains, unlikely ones long chains.

### 2.2 Joint entropy and conditional entropy (pp. 15–17)
**Definition (joint entropy).** For $(X,Y)\sim p(x,y)$,
$$H(X,Y)=-\sum_{x}\sum_{y}p(x,y)\log p(x,y)=-E\log p(X,Y).\tag{2.8, 2.9}$$
The pair is just one vector-valued random variable (p. 15).

**Definition (conditional entropy).** The expected value of the entropies of the conditional distributions, averaged over the conditioning variable (p. 16):
$$H(Y|X)=\sum_x p(x)H(Y|X=x)\tag{2.10}$$
$$=-\sum_x p(x)\sum_y p(y|x)\log p(y|x)\tag{2.11}$$
$$=-\sum_x\sum_y p(x,y)\log p(y|x)\tag{2.12}$$
$$=-E_{p(x,y)}\log p(Y|X).\tag{2.13}$$

**Theorem 2.2.1 (chain rule).** $H(X,Y)=H(X)+H(Y|X)$ (2.14). (p. 16)

*Proof (p. 16).*
$$H(X,Y)=-\sum_x\sum_y p(x,y)\log p(x,y)\tag{2.15}$$
$$=-\sum_x\sum_y p(x,y)\log p(x)p(y|x)\tag{2.16}$$
$$=-\sum_x\sum_y p(x,y)\log p(x)-\sum_x\sum_y p(x,y)\log p(y|x)\tag{2.17}$$
$$=-\sum_x p(x)\log p(x)-\sum_x\sum_y p(x,y)\log p(y|x)\tag{2.18}$$
$$=H(X)+H(Y|X).\tag{2.19}$$
Equivalently, $\log p(X,Y)=\log p(X)+\log p(Y|X)$ (2.20); take expectations of both sides (p. 16).

**Corollary:** $H(X,Y|Z)=H(X|Z)+H(Y|X,Z)$ (2.21), proved along the same lines (p. 17).

**Example 2.2.1.** Joint distribution (rows $Y$, columns $X$) (p. 17):

| | X=1 | X=2 | X=3 | X=4 |
|---|---|---|---|---|
| Y=1 | 1/8 | 1/16 | 1/32 | 1/32 |
| Y=2 | 1/16 | 1/8 | 1/32 | 1/32 |
| Y=3 | 1/16 | 1/16 | 1/16 | 1/16 |
| Y=4 | 1/4 | 0 | 0 | 0 |

Marginal of $X$ is $(\frac12,\frac14,\frac18,\frac18)$ and of $Y$ is $(\frac14,\frac14,\frac14,\frac14)$. So $H(X)=7/4$ bits and $H(Y)=2$ bits. Then
$$H(X|Y)=\sum_{i=1}^4 p(Y=i)H(X|Y=i)=\tfrac14H(\tfrac12,\tfrac14,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac12,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac14,\tfrac14,\tfrac14)+\tfrac14H(1,0,0,0)\tag{2.22–2.23}$$
$$=\tfrac14\cdot\tfrac74+\tfrac14\cdot\tfrac74+\tfrac14\cdot2+\tfrac14\cdot0=\tfrac{11}{8}\text{ bits}.\tag{2.24–2.25}$$
Similarly $H(Y|X)=13/8$ and $H(X,Y)=27/8$ bits (p. 17).

**Remark:** $H(Y|X)\ne H(X|Y)$ in general, but $H(X)-H(X|Y)=H(Y)-H(Y|X)$ (p. 17).

### 2.3 Relative entropy and mutual information (pp. 18–19)
Entropy measures the average amount of information needed to describe $X$ (p. 18).

**Definition (relative entropy / Kullback–Leibler distance).**
$$D(p\|q)=\sum_{x}p(x)\log\frac{p(x)}{q(x)}=E_p\log\frac{p(X)}{q(X)}.\tag{2.26, 2.27}$$
Conventions (from continuity): $0\log\frac0q=0$ and $p\log\frac p0=\infty$ (p. 18).
- In statistics it arises as an expected log of the likelihood ratio (p. 18).
- It measures the inefficiency of assuming $q$ when the truth is $p$. A code for the true $p$ has average length $H(p)$. Using the code for $q$ would need $H(p)+D(p\|q)$ bits on average (p. 18).
- It will be shown to be always $\ge0$, and $0$ iff $p=q$. It is not a true distance, since it is not symmetric and fails the triangle inequality. The author says it is nonetheless often useful to think of it as a "distance" (p. 18).

**Definition (mutual information).** For joint pmf $p(x,y)$ with marginals $p(x),p(y)$, it is the relative entropy between the joint and the product distribution:
$$I(X;Y)=\sum_x\sum_y p(x,y)\log\frac{p(x,y)}{p(x)p(y)}\tag{2.28}$$
$$=D\big(p(x,y)\|p(x)p(y)\big)=E_{p(x,y)}\log\frac{p(X,Y)}{p(X)p(Y)}.\tag{2.29, 2.30}$$
It is the reduction in uncertainty of one variable due to knowledge of the other (p. 18).

**Example 2.3.1.** $\mathcal X=\{0,1\}$, $p(0)=1-r,\ p(1)=r$, $q(0)=1-s,\ q(1)=s$ (p. 19):
$$D(p\|q)=(1-r)\log\frac{1-r}{1-s}+r\log\frac rs,\qquad D(q\|p)=(1-s)\log\frac{1-s}{1-r}+s\log\frac sr.\tag{2.31, 2.32}$$
If $r=s$ both are 0. If $r=1/2,\ s=1/4$:
$$D(p\|q)=\tfrac12\log\frac{1/2}{3/4}+\tfrac12\log\frac{1/2}{1/4}=1-\tfrac12\log3=0.2075\text{ bits},\tag{2.33}$$
$$D(q\|p)=\tfrac34\log\frac{3/4}{1/2}+\tfrac14\log\frac{1/4}{1/2}=\tfrac34\log3-1=0.1887\text{ bits}.\tag{2.34}$$
So $D(p\|q)\ne D(q\|p)$ in general (p. 19).

### 2.4 Relationship between entropy and mutual information (pp. 19–21)
Starting from (2.28) (pp. 19–20):
$$I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}=\sum_{x,y}p(x,y)\log\frac{p(x|y)}{p(x)}\tag{2.35, 2.36}$$
$$=-\sum_{x,y}p(x,y)\log p(x)+\sum_{x,y}p(x,y)\log p(x|y)\tag{2.37}$$
$$=-\sum_x p(x)\log p(x)-\Big(-\sum_{x,y}p(x,y)\log p(x|y)\Big)\tag{2.38}$$
$$=H(X)-H(X|Y).\tag{2.39}$$
So $I(X;Y)$ is the reduction in uncertainty of $X$ due to knowing $Y$. By symmetry $I(X;Y)=H(Y)-H(Y|X)$ (2.40): "X says as much about Y as Y says about X" (p. 20). From the chain rule, $I(X;Y)=H(X)+H(Y)-H(X,Y)$ (2.41). Also $I(X;X)=H(X)-H(X|X)=H(X)$ (2.42), which is why entropy is sometimes called self-information (p. 20).

**Theorem 2.4.1 (mutual information and entropy)** (p. 20):
$$I(X;Y)=H(X)-H(X|Y)\ (2.43),\quad I(X;Y)=H(Y)-H(Y|X)\ (2.44),\quad I(X;Y)=H(X)+H(Y)-H(X,Y)\ (2.45),$$
$$I(X;Y)=I(Y;X)\ (2.46),\qquad I(X;X)=H(X)\ (2.47).$$
Figure 2.2 is a Venn diagram. $H(X)$ and $H(Y)$ are two overlapping circles, and $I(X;Y)$ is the intersection (pp. 20–21).

**Example 2.4.1.** For the distribution of Example 2.2.1, $I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)=0.375$ bits (p. 21). (Check: $7/4-11/8=3/8$.)

*Intuition note.* $H(X|Y)$ is what is left of $X$'s uncertainty after seeing $Y$. $I(X;Y)$ is the part that disappears. Because it is also $H(Y)-H(Y|X)$, it is the same number from either side.

### 2.5 Chain rules (pp. 21–23)
**Theorem 2.5.1 (chain rule for entropy).** For $X_1,\dots,X_n\sim p(x_1,\dots,x_n)$:
$$H(X_1,\dots,X_n)=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.48}$$
*Proof (p. 21).* Repeatedly apply the two-variable rule: $H(X_1,X_2)=H(X_1)+H(X_2|X_1)$ (2.49); $H(X_1,X_2,X_3)=H(X_1)+H(X_2,X_3|X_1)=H(X_1)+H(X_2|X_1)+H(X_3|X_2,X_1)$ (2.50–2.51); and so on to (2.52–2.53).

*Alternative proof (pp. 21–22).* Write $p(x_1,\dots,x_n)=\prod_{i=1}^np(x_i|x_{i-1},\dots,x_1)$. Then
$$H(X_1,\dots,X_n)=-\sum p(x_1,\dots,x_n)\log\prod_{i=1}^np(x_i|x_{i-1},\dots,x_1)\tag{2.54, 2.55}$$
$$=-\sum_{x_1..x_n}\sum_{i=1}^np(x_1,\dots,x_n)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.56}$$
$$=-\sum_{i=1}^n\sum_{x_1..x_n}p(x_1,\dots,x_n)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.57}$$
$$=-\sum_{i=1}^n\sum_{x_1..x_i}p(x_1,\dots,x_i)\log p(x_i|x_{i-1},\dots,x_1)\tag{2.58}$$
$$=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.59}$$

**Definition (conditional mutual information).** The reduction in uncertainty of $X$ due to knowledge of $Y$ when $Z$ is given:
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=E_{p(x,y,z)}\log\frac{p(X,Y|Z)}{p(X|Z)p(Y|Z)}.\tag{2.60, 2.61}$$

**Theorem 2.5.2 (chain rule for information).**
$$I(X_1,\dots,X_n;Y)=\sum_{i=1}^nI(X_i;Y|X_{i-1},\dots,X_1).\tag{2.62}$$
*Proof (p. 22).*
$$I(X_1,\dots,X_n;Y)=H(X_1,\dots,X_n)-H(X_1,\dots,X_n|Y)\tag{2.63}$$
$$=\sum_iH(X_i|X_{i-1},\dots,X_1)-\sum_iH(X_i|X_{i-1},\dots,X_1,Y)=\sum_iI(X_i;Y|X_1,\dots,X_{i-1}).\tag{2.64}$$

**Definition (conditional relative entropy).** The average, over $p(x)$, of the relative entropies between $p(y|x)$ and $q(y|x)$:
$$D\big(p(y|x)\|q(y|x)\big)=\sum_xp(x)\sum_yp(y|x)\log\frac{p(y|x)}{q(y|x)}=E_{p(x,y)}\log\frac{p(Y|X)}{q(Y|X)}.\tag{2.65, 2.66}$$
The notation omits $p(x)$, which is understood from context (p. 23).

**Theorem 2.5.3 (chain rule for relative entropy).**
$$D\big(p(x,y)\|q(x,y)\big)=D\big(p(x)\|q(x)\big)+D\big(p(y|x)\|q(y|x)\big).\tag{2.67}$$
*Proof (p. 23).*
$$D=\sum_x\sum_yp(x,y)\log\frac{p(x,y)}{q(x,y)}=\sum_x\sum_yp(x,y)\log\frac{p(x)p(y|x)}{q(x)q(y|x)}\tag{2.68, 2.69}$$
$$=\sum_x\sum_yp(x,y)\log\frac{p(x)}{q(x)}+\sum_x\sum_yp(x,y)\log\frac{p(y|x)}{q(y|x)}=D(p(x)\|q(x))+D(p(y|x)\|q(y|x)).\tag{2.70, 2.71}$$
This rule is used in Section 2.9 for the second law (p. 23).

*Intuition note.* Uncertainty, shared information and "wrong-model cost" all add up one variable at a time. The total is the first piece plus what the second adds once the first is known.

### 2.6 Jensen's inequality and its consequences (pp. 23–28)
**Definitions.** $f$ is *convex* on $(a,b)$ if for all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$,
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2).\tag{2.72}$$
It is *strictly convex* if equality holds only for $\lambda=0$ or $1$. $f$ is *concave* if $-f$ is convex. A convex function lies below any chord, a concave one above (p. 23). Convex examples: $x^2,|x|,e^x,x\log x$ ($x\ge0$). Concave examples: $\log x,\sqrt x$ ($x\ge0$). Linear functions are both (p. 24).

**Theorem 2.6.1.** If $f$ has a second derivative that is non-negative (positive) everywhere, then $f$ is convex (strictly convex).
*Proof (pp. 24–25).* Taylor: $f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x^*)}2(x-x_0)^2$ with $x^*$ between $x_0$ and $x$ (2.73). Since $f''(x^*)\ge0$, the last term is non-negative, so $f(x)\ge f(x_0)+f'(x_0)(x-x_0)$. Let $x_0=\lambda x_1+(1-\lambda)x_2$ and take $x=x_1$:
$$f(x_1)\ge f(x_0)+f'(x_0)[(1-\lambda)(x_1-x_2)].\tag{2.74}$$
Taking $x=x_2$:
$$f(x_2)\ge f(x_0)+f'(x_0)[\lambda(x_2-x_1)].\tag{2.75}$$
Multiply (2.74) by $\lambda$, (2.75) by $1-\lambda$, and add. The $f'$ terms cancel, since $\lambda(1-\lambda)(x_1-x_2)+(1-\lambda)\lambda(x_2-x_1)=0$ (added step). This gives (2.72). Strict convexity is analogous (p. 25).
Consequence: strict convexity of $x^2,e^x,x\log x$ and strict concavity of $\log x,\sqrt x$ (p. 25).

**Theorem 2.6.2 (Jensen's inequality).** If $f$ is convex and $X$ a random variable, $Ef(X)\ge f(EX)$ (2.76). If $f$ is strictly convex, equality implies $X=EX$ with probability 1 (so $X$ is constant) (p. 25).
*Proof (pp. 25–26), discrete case by induction on mass points.* Two points: $p_1f(x_1)+p_2f(x_2)\ge f(p_1x_1+p_2x_2)$ (2.77), which is the definition of convexity. Suppose it holds for $k-1$ points. Write $p_i'=p_i/(1-p_k)$ for $i=1..k-1$:
$$\sum_{i=1}^kp_if(x_i)=p_kf(x_k)+(1-p_k)\sum_{i=1}^{k-1}p_i'f(x_i)\tag{2.78}$$
$$\ge p_kf(x_k)+(1-p_k)f\Big(\sum_{i=1}^{k-1}p_i'x_i\Big)\ge f\Big(p_kx_k+(1-p_k)\sum_{i=1}^{k-1}p_i'x_i\Big)=f\Big(\sum_{i=1}^kp_ix_i\Big).\tag{2.79–2.81}$$
The first inequality is the induction hypothesis, the second is convexity. The equality condition for strictly convex $f$ is left to the reader. Continuous distributions follow by continuity arguments (p. 26).

**Theorem 2.6.3 (information inequality).** For pmfs $p,q$ on $\mathcal X$, $D(p\|q)\ge0$ (2.82), with equality iff $p(x)=q(x)$ for all $x$ (2.83) (p. 26).
*Proof (p. 26).* Let $A=\{x:p(x)>0\}$.
$$-D(p\|q)=-\sum_{A}p\log\frac pq=\sum_Ap\log\frac qp\tag{2.84, 2.85}$$
$$\le\log\sum_Ap\frac qp=\log\sum_Aq\tag{2.86, 2.87}$$
$$\le\log\sum_{\mathcal X}q=\log1=0.\tag{2.88–2.90}$$
(2.86) is Jensen's inequality for the concave $\log$. Since $\log t$ is strictly concave, equality in (2.86) holds iff $q(x)/p(x)=1$ everywhere, i.e. $p=q$.

*Intuition note.* On average, a wrong model can never "beat" the true one: describing data from $p$ with a code built for $q$ costs at least as much. The cost is zero only when $q=p$.

**Corollaries (p. 27).**
- *Non-negativity of mutual information:* $I(X;Y)\ge0$ (2.91), with equality iff $X,Y$ independent. *Proof:* $I=D(p(x,y)\|p(x)p(y))\ge0$, with equality iff $p(x,y)=p(x)p(y)$.
- $D(p(y|x)\|q(y|x))\ge0$ (2.92), with equality iff $p(y|x)=q(y|x)$ for all $y$ and all $x$ with $p(x)>0$.
- $I(X;Y|Z)\ge0$ (2.93), with equality iff $X$ and $Y$ are conditionally independent given $Z$.

**Theorem 2.6.4.** $H(X)\le\log|\mathcal X|$, with equality iff $X$ is uniform on $\mathcal X$ (p. 27).
*Proof.* With $u(x)=1/|\mathcal X|$: $D(p\|u)=\sum p\log\frac{p}{u}=\log|\mathcal X|-H(X)$ (2.94), and $0\le D(p\|u)$ gives (2.95).

**Theorem 2.6.5 (conditioning reduces entropy).** $H(X|Y)\le H(X)$ (2.96), with equality iff $X$ and $Y$ are independent. *Proof:* $0\le I(X;Y)=H(X)-H(X|Y)$ (pp. 27–28).
This holds only on average. $H(X|Y=y)$ may be greater than, less than, or equal to $H(X)$, but $H(X|Y)=\sum_yp(y)H(X|Y=y)\le H(X)$. The author's illustration: in a court case, specific new evidence might increase uncertainty, but on average evidence decreases it (p. 28).

**Example 2.6.1.** Joint distribution: $p(X{=}1,Y{=}1)=0$, $p(X{=}2,Y{=}1)=3/4$, $p(X{=}1,Y{=}2)=1/8$, $p(X{=}2,Y{=}2)=1/8$. Then $H(X)=H(\frac18,\frac78)=0.544$ bits, $H(X|Y{=}1)=0$, $H(X|Y{=}2)=1$ bit. $H(X|Y)=\frac34\cdot0+\frac14\cdot1=0.25$ bits. Observing $Y=2$ raises uncertainty about $X$, observing $Y=1$ lowers it, and the average falls (p. 28).

**Theorem 2.6.6 (independence bound on entropy).**
$$H(X_1,\dots,X_n)\le\sum_{i=1}^nH(X_i),\tag{2.97}$$
with equality iff the $X_i$ are independent. *Proof:* chain rule gives $\sum H(X_i|X_{i-1},\dots,X_1)$ (2.98), which is $\le\sum H(X_i)$ (2.99) by the previous theorem. Equality holds iff each $X_i$ is independent of $X_{i-1},\dots,X_1$ (p. 28).

### 2.7 The log sum inequality and its applications (pp. 29–31)
**Theorem 2.7.1 (log sum inequality).** For non-negative $a_1..a_n$, $b_1..b_n$:
$$\sum_{i=1}^na_i\log\frac{a_i}{b_i}\ge\Big(\sum_{i=1}^na_i\Big)\log\frac{\sum a_i}{\sum b_i},\tag{2.100}$$
with equality iff $a_i/b_i=$ const. Conventions: $0\log0=0$, $a\log\frac a0=\infty$ if $a>0$, $0\log\frac00=0$ (p. 29).
*Proof (p. 29).* Assume $a_i,b_i>0$. $f(t)=t\log t$ is strictly convex since $f''(t)=\frac1t\log e>0$. Jensen: $\sum\alpha_if(t_i)\ge f(\sum\alpha_it_i)$ for $\alpha_i\ge0$, $\sum\alpha_i=1$ (2.101). Set $\alpha_i=b_i/\sum_jb_j$ and $t_i=a_i/b_i$:
$$\sum\frac{a_i}{\sum b_j}\log\frac{a_i}{b_i}\ge\Big(\sum\frac{a_i}{\sum b_j}\Big)\log\Big(\sum\frac{a_i}{\sum b_j}\Big).\tag{2.102}$$
Multiplying through by $\sum b_j$ (added step) gives (2.100).

**Re-proof of $D\ge0$ (p. 29).** $D(p\|q)=\sum p\log\frac pq\ge(\sum p)\log\frac{\sum p}{\sum q}=1\log\frac11=0$ (2.103–2.105). Equality iff $p(x)/q(x)=c$. Since both sum to 1, $c=1$.

**Theorem 2.7.2.** $D(p\|q)$ is convex in the pair $(p,q)$: for pairs $(p_1,q_1),(p_2,q_2)$ and $0\le\lambda\le1$,
$$D(\lambda p_1+(1-\lambda)p_2\|\lambda q_1+(1-\lambda)q_2)\le\lambda D(p_1\|q_1)+(1-\lambda)D(p_2\|q_2).\tag{2.106}$$
*Proof (p. 30).* Apply the log sum inequality to each term on the left (two summands $\lambda p_1(x)$ over $\lambda q_1(x)$, and $(1-\lambda)p_2(x)$ over $(1-\lambda)q_2(x)$) (2.107), then sum over $x$.

**Theorem 2.7.3 (concavity of entropy).** $H(p)$ is concave in $p$.
*Proof (p. 30).* $H(p)=\log|\mathcal X|-D(p\|u)$ (2.108), with $u$ uniform. Concavity follows from convexity of $D$.
*Alternative proof.* Let $X_1\sim p_1$, $X_2\sim p_2$ on the same set. Let $\theta=1$ with probability $\lambda$ and $\theta=2$ with probability $1-\lambda$, and $Z=X_\theta$ (2.109). Then $Z\sim\lambda p_1+(1-\lambda)p_2$. Conditioning reduces entropy: $H(Z)\ge H(Z|\theta)$ (2.110), i.e. $H(\lambda p_1+(1-\lambda)p_2)\ge\lambda H(p_1)+(1-\lambda)H(p_2)$ (2.111).
The author adds: one consequence of concavity is that mixing two gases of equal entropy gives a gas of higher entropy (p. 31).

**Theorem 2.7.4.** Let $(X,Y)\sim p(x,y)=p(x)p(y|x)$. $I(X;Y)$ is a concave function of $p(x)$ for fixed $p(y|x)$, and a convex function of $p(y|x)$ for fixed $p(x)$ (p. 31).
*Proof (p. 31).* *First part:* $I(X;Y)=H(Y)-H(Y|X)=H(Y)-\sum_xp(x)H(Y|X=x)$ (2.112). With $p(y|x)$ fixed, $p(y)$ is linear in $p(x)$, so $H(Y)$ (concave in $p(y)$) is concave in $p(x)$. The second term is linear in $p(x)$, so the difference is concave.
*Second part:* fix $p(x)$. Take conditionals $p_1(y|x),p_2(y|x)$ and the mixture $p_\lambda(y|x)=\lambda p_1(y|x)+(1-\lambda)p_2(y|x)$ (2.113). The joint is the mixture $p_\lambda(x,y)=\lambda p_1(x,y)+(1-\lambda)p_2(x,y)$ (2.114), and $p_\lambda(y)=\lambda p_1(y)+(1-\lambda)p_2(y)$ (2.115). With $q_\lambda(x,y)=p(x)p_\lambda(y)$, also $q_\lambda=\lambda q_1+(1-\lambda)q_2$ (2.116). Since $I(X;Y)=D(p_\lambda\|q_\lambda)$ (2.117) and $D$ is convex in the pair, $I$ is convex in $p(y|x)$.

*Intuition note.* Mixing distributions never lowers entropy below the average of the parts. Mutual information, as a function of the input distribution, is "bowl-down", and as a function of the channel $p(y|x)$ it is "bowl-up".

### 2.8 Data processing inequality (pp. 32–33)
**Definition (Markov chain).** $X,Y,Z$ form a Markov chain in that order, $X\to Y\to Z$, if the conditional distribution of $Z$ depends only on $Y$ and is conditionally independent of $X$. Equivalently the joint pmf is
$$p(x,y,z)=p(x)p(y|x)p(z|y).\tag{2.118}$$
Consequences (p. 32):
- $X\to Y\to Z$ iff $X$ and $Z$ are conditionally independent given $Y$, because $p(x,z|y)=\frac{p(x,y,z)}{p(y)}=\frac{p(x,y)p(z|y)}{p(y)}=p(x|y)p(z|y)$ (2.119). This characterisation extends to Markov fields.
- $X\to Y\to Z$ implies $Z\to Y\to X$, so it is sometimes written $X\leftrightarrow Y\leftrightarrow Z$.
- If $Z=f(Y)$, then $X\to Y\to Z$.

**Theorem 2.8.1 (data processing inequality).** If $X\to Y\to Z$, then $I(X;Y)\ge I(X;Z)$ (p. 32).
*Proof (pp. 32–33).* Expand $I(X;Y,Z)$ by the chain rule in two ways: $I(X;Y,Z)=I(X;Z)+I(X;Y|Z)$ and $I(X;Y,Z)=I(X;Y)+I(X;Z|Y)$ (the second is the expansion intended by (2.120)–(2.121); see Reading notes). By Markovity $I(X;Z|Y)=0$, and $I(X;Y|Z)\ge0$, so
$$I(X;Y)\ge I(X;Z).\tag{2.122}$$
Equality holds iff $I(X;Y|Z)=0$, i.e. iff $X\to Z\to Y$ is a Markov chain. Similarly $I(Y;Z)\ge I(X;Z)$ (p. 33).

**Corollaries (p. 33).**
- If $Z=g(Y)$, then $I(X;Y)\ge I(X;g(Y))$, since $X\to Y\to g(Y)$ is a Markov chain. Functions of the data cannot increase information about $X$.
- If $X\to Y\to Z$, then $I(X;Y|Z)\le I(X;Y)$ (2.123). *Proof:* from the two expansions, using $I(X;Z|Y)=0$ and $I(X;Z)\ge0$. Observing a "downstream" $Z$ decreases (or leaves unchanged) the dependence of $X$ and $Y$.
- **Counterexample without a Markov chain:** $X,Y$ independent fair bits, $Z=X+Y$. Then $I(X;Y)=0$ but $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=H(X|Z)=P(Z{=}1)H(X|Z{=}1)=\frac12$ bit. So $I(X;Y|Z)>I(X;Y)$ is possible when $X,Y,Z$ are not a Markov chain (p. 33).

*Intuition note.* If $Z$ is made from $Y$ alone, $Z$ can only know what $Y$ knew about $X$. Any computation on $Y$, deterministic or random, can lose information about $X$ (or at best keep it), never add it.

### 2.9 The second law of thermodynamics (pp. 33–36)
The second law states that the entropy of an isolated system is non-decreasing (p. 33). In statistical thermodynamics, entropy is often the log of the number of microstates. This matches the chapter's entropy exactly if all states are equally likely (p. 33). The system is modelled as a Markov chain (see Chapter 4) with transitions obeying physical laws. This assumes an overall state, and that given the present state the future is independent of the past (p. 33). Under this model the author says he can find four interpretations of the second law (p. 33), though five numbered statements follow. His headline: entropy does not always increase, but relative entropy always decreases (pp. 33–34).

1. **$D(\mu_n\|\mu_n')$ decreases with $n$** (p. 34). Let $\mu_n,\mu_n'$ be two distributions on the state space at time $n$, with joint pmfs $p(x_n,x_{n+1})=p(x_n)r(x_{n+1}|x_n)$ and $q(x_n,x_{n+1})=q(x_n)r(x_{n+1}|x_n)$, where $r$ is the transition function. The chain rule for relative entropy gives two expansions:
$$D(p(x_n,x_{n+1})\|q(x_n,x_{n+1}))=D(p(x_n)\|q(x_n))+D(p(x_{n+1}|x_n)\|q(x_{n+1}|x_n))$$
$$=D(p(x_{n+1})\|q(x_{n+1}))+D(p(x_n|x_{n+1})\|q(x_n|x_{n+1})).$$
Both conditionals $p(x_{n+1}|x_n),q(x_{n+1}|x_n)$ equal $r(x_{n+1}|x_n)$, so the first conditional term is 0. The last term is $\ge0$ (Corollary to Theorem 2.6.3). Hence
$$D(p(x_n)\|q(x_n))\ge D(p(x_{n+1})\|q(x_{n+1}))\ \text{ i.e. }\ D(\mu_n\|\mu_n')\ge D(\mu_{n+1}\|\mu_{n+1}').\tag{2.124, 2.125}$$
The distance between the two distributions decreases with time for any Markov chain.
*Author's illustrative example:* if the wealth-redistribution tax system were the same in Canada and England, with $\mu_n,\mu_n'$ the wealth distributions, the relative-entropy distance between them would decrease with time, i.e. the distributions would become more similar (p. 34).

2. **$D(\mu_n\|\mu)$ to a stationary distribution decreases with $n$** (pp. 34–35). In (2.125) let $\mu_n'$ be a stationary distribution $\mu$, so $\mu_{n+1}'$ is the same. Then
$$D(\mu_n\|\mu)\ge D(\mu_{n+1}\|\mu).\tag{2.126}$$
So any state distribution gets closer to each stationary distribution over time. The sequence is monotonically non-increasing and non-negative, so it has a limit. The limit is actually 0 if the stationary distribution is unique, which the author says is more difficult to prove (p. 35).

3. **Entropy increases if the stationary distribution is uniform** (p. 35). In general, decreasing relative entropy does not imply increasing entropy. Counterexample: any Markov chain with a non-uniform stationary distribution, started from the uniform distribution (already maximum entropy). It tends to the stationary distribution, which has lower entropy, so entropy decreases. If the stationary distribution is uniform, then
$$D(\mu_n\|\mu)=\log|\mathcal X|-H(\mu_n)=\log|\mathcal X|-H(X_n),\tag{2.127}$$
so decreasing relative entropy means increasing entropy. The author says this ties most closely to statistical thermodynamics, where all microstates are equally likely.
**Definition:** a transition matrix $[P_{ij}]$, $P_{ij}=\Pr\{X_{n+1}=j|X_n=i\}$, is *doubly stochastic* if $\sum_iP_{ij}=1$ for all $j$ (2.128) and $\sum_jP_{ij}=1$ for all $i$ (2.129).
**Remark:** the uniform distribution is stationary for $P$ iff $P$ is doubly stochastic (the author refers to Problem 1 of Chapter 4 for this).

4. **$H(X_n|X_1)$ increases with $n$ for a stationary Markov process** (pp. 35–36). For a stationary process $H(X_n)$ is constant, so entropy is non-increasing (indeed constant). But the conditional uncertainty of the future increases. *First proof:*
$$H(X_n|X_1)\ge H(X_n|X_1,X_2)\ \text{(conditioning reduces entropy)}=H(X_n|X_2)\ \text{(Markovity)}=H(X_{n-1}|X_1)\ \text{(stationarity)}.\tag{2.130–2.132}$$
*Alternative proof:* apply data processing to the chain $X_1\to X_{n-1}\to X_n$: $I(X_1;X_{n-1})\ge I(X_1;X_n)$ (2.133). Expanding, $H(X_{n-1})-H(X_{n-1}|X_1)\ge H(X_n)-H(X_n|X_1)$ (2.134). By stationarity $H(X_{n-1})=H(X_n)$, so
$$H(X_{n-1}|X_1)\le H(X_n|X_1).\tag{2.135}$$
The same techniques show $H(X_0|X_n)$ increases in $n$ for any Markov chain (Problem 35).

5. **Shuffles increase entropy** (p. 36). If $T$ is a shuffle (permutation) of a deck, $X$ the initial random order, and $T$ is independent of $X$, then $H(TX)\ge H(X)$ (2.136). Problem 31 outlines a proof.

*Intuition note.* The entropy of the system's state need not rise. What never grows is the relative entropy between the distributions that two different starting situations lead to (p. 34), because both follow the same transition rule. Entropy is guaranteed to rise when the stationary distribution is uniform; with a non-uniform stationary distribution it can fall (p. 35).

### 2.10 Sufficient statistics (pp. 36–38)
The author calls this a sidelight on the power of data processing (p. 36). Let $\{f_\theta(x)\}$ be a family of pmfs indexed by $\theta$, $X$ a sample, $T(X)$ any statistic (function of the sample). Then $\theta\to X\to T(X)$ and
$$I(\theta;T(X))\le I(\theta;X)\tag{2.137}$$
for any distribution on $\theta$. If equality holds, no information is lost (p. 36).

**Definition (sufficient statistic).** $T(X)$ is sufficient relative to $\{f_\theta\}$ if $X$ is independent of $\theta$ given $T(X)$, i.e. $\theta\to T(X)\to X$ is a Markov chain (p. 37). This is the equality condition of data processing:
$$I(\theta;X)=I(\theta;T(X))\tag{2.138}$$
for all distributions on $\theta$. So sufficient statistics preserve mutual information and conversely (p. 37).

**Examples (pp. 37–38).**
1. $X_1..X_n\in\{0,1\}$ i.i.d. coin tosses with $\theta=\Pr(X_i=1)$. $T=\sum X_i$ (number of 1s) is sufficient. Given $T=k$ all sequences with $k$ ones are equally likely and independent of $\theta$:
$$\Pr\Big\{(X_1..X_n)=(x_1..x_n)\Big|\sum X_i=k\Big\}=\begin{cases}1/\binom nk&\text{if }\sum x_i=k,\\0&\text{otherwise.}\end{cases}\tag{2.139}$$
So $\theta\to\sum X_i\to(X_1..X_n)$ is a Markov chain.
2. $X\sim\mathcal N(\theta,1)$ (2.140), $X_1..X_n$ i.i.d.: the sample mean $\bar X_n=\frac1n\sum X_i$ is sufficient for $\theta$. The conditional distribution of the sample given $\bar X_n$ and $n$ does not depend on $\theta$ (the author says "it can be verified"). (Examples 2 and 3 use densities. Entropy for continuous variables is defined in Chapter 9.)
3. $f_\theta=\text{Uniform}(\theta,\theta+1)$: $T=(\max\{X_i\},\min\{X_i\})$ (2.141) is sufficient. The proof is "slightly more complicated" and not given.

**Definition (minimal sufficient statistic).** $T(X)$ is minimal sufficient if it is a function of every other sufficient statistic $U$. In data-processing terms: $\theta\to T(X)\to U(X)\to X$ (2.142). It maximally compresses the information about $\theta$. Other sufficient statistics may carry irrelevant information. Example: for a normal with mean $\theta$, the pair (mean of odd-indexed samples, mean of even-indexed samples) is sufficient but not minimal. In the three examples above the sufficient statistics are also minimal (p. 38).

### 2.11 Fano's inequality (pp. 38–40)
Setting: guess $X\sim p(x)$ from $Y$ with $p(y|x)$, using $\hat X=g(Y)$. Then $X\to Y\to\hat X$ is a Markov chain. Define $P_e=\Pr\{\hat X\ne X\}$ (2.143) (p. 39). The author says conditional entropy $H(X|Y)=0$ iff $X$ is a function of $Y$ (known from the chapter problems), so zero-error estimation is possible iff $H(X|Y)=0$. Extending this, the author expects to be able to estimate $X$ with low error probability only if $H(X|Y)$ is small. Fano's inequality quantifies this. It will be crucial for the converse of Shannon's second theorem in Chapter 8 (p. 38).

**Theorem 2.11.1 (Fano).**
$$H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y).\tag{2.144}$$
Weakened forms:
$$1+P_e\log|\mathcal X|\ge H(X|Y)\ (2.145),\qquad P_e\ge\frac{H(X|Y)-1}{\log|\mathcal X|}.\ (2.146)$$
Remark: $P_e=0$ implies $H(X|Y)=0$ (p. 39).

*Proof (pp. 39–40).* Let $E=1$ if $\hat X\ne X$ and $E=0$ otherwise (2.147). Expand $H(E,X|Y)$ in two ways:
$$H(E,X|Y)=H(X|Y)+H(E|X,Y)=H(X|Y)\tag{2.148}$$
since $E$ is a function of $X$ and $g(Y)$, so $H(E|X,Y)=0$;
$$H(E,X|Y)=H(E|Y)+H(X|E,Y)\le H(P_e)+P_e\log(|\mathcal X|-1).\tag{2.149}$$
Reasons: conditioning reduces entropy, so $H(E|Y)\le H(E)=H(P_e)$ ($E$ is binary with $\Pr(E{=}1)=P_e$). And
$$H(X|E,Y)=\Pr(E{=}0)H(X|Y,E{=}0)+\Pr(E{=}1)H(X|Y,E{=}1)\le(1-P_e)\cdot0+P_e\log(|\mathcal X|-1).\tag{2.150, 2.151}$$
Given $E=0$, $X=g(Y)$ (entropy 0). Given $E=1$, the entropy is bounded by the log of the number of remaining outcomes ($|\mathcal X|-1$ if $g(Y)\in\mathcal X$, else $|\mathcal X|$) (p. 40).

**Remark (no side information; sharpness).** Let $X\in\{1..m\}$, $p_1\ge p_2\ge\dots\ge p_m$. The best guess is $\hat X=1$ with $P_e=1-p_1$. Fano becomes
$$H(P_e)+P_e\log(m-1)\ge H(X).\tag{2.152}$$
The pmf $(p_1,\dots,p_m)=(1-P_e,\frac{P_e}{m-1},\dots,\frac{P_e}{m-1})$ achieves this with equality (2.153). Thus Fano's inequality is sharp (p. 40).

*Intuition note.* If $Y$ leaves a lot of uncertainty about $X$, no guessing rule can be right most of the time. The error probability must be at least roughly the leftover uncertainty (minus 1 bit) divided by the size of the alphabet in bits.

### Summary of Chapter 2 (pp. 40–42)
The author's "telegraphic summary" omits qualifying conditions (p. 40). It restates: properties of $H$ (non-negative, base change, conditioning reduces entropy, independence bound, $H\le\log|\mathcal X|$, concavity); $D\ge0$; $I=D(p(x,y)\|p(x)p(y))\ge0$; if $u$ is uniform on $m$ points, $D(p\|u)=\log m-H(p)$; $D$ convex in $(p,q)$ (p. 41). It also restates the three chain rules, Jensen, log sum, data processing, the five second-law statements (p. 42), the sufficient-statistic criterion, and Fano (2.164) (p. 42). Each restated item is treated above, except that the fifth second-law item is only mentioned on p. 36 and left to Problem 35.

### Problems for Chapter 2 (pp. 42–49)
35 problems are listed (coin-flip entropy, entropy of functions, axiomatic definition of entropy, bent coins and fair bits, World Series, infinite entropy, Venn diagrams and three-variable $I(X;Y;Z)$, coin weighing, metric $\rho(X,Y)=H(X|Y)+H(Y|X)$, bottleneck, run-length coding, maximum entropy for integer-valued $X$ with fixed mean, shuffles, Fano without conditioning, empirical distribution, etc.). Worth-doing items are listed below.

### Historical notes (p. 49)
The author states that entropy was first introduced in thermodynamics. Boltzmann's $S=k\ln W$ was inscribed on his gravestone. Hartley introduced a logarithmic information measure in the 1930s. Shannon was first to define entropy and mutual information as in this chapter. Kullback and Leibler first defined relative entropy. Fano proved his inequality. Fisher defined sufficient statistics, Lehmann and Scheffé minimal sufficient statistics, and Kullback related mutual information to sufficiency (p. 49).

## Toy example (ours, not from the text)
Let $X,Y$ be bits with joint pmf $p(0,0)=p(1,1)=3/8$, $p(0,1)=p(1,0)=1/8$. Use $\log_23=1.58496$.

1. Marginals: $p(X{=}0)=3/8+1/8=1/2$, likewise for $X{=}1$, $Y{=}0$, $Y{=}1$. So $H(X)=H(Y)=1$ bit.
2. Joint entropy: $H(X,Y)=2\cdot\frac38\log\frac83+2\cdot\frac18\log8=\frac34(3-1.58496)+\frac34=1.06128+0.75=1.81128$ bits.
3. Chain rule: $H(Y|X)=H(X,Y)-H(X)=0.81128$ bits. Check directly: given $X$, $Y$ agrees with probability $3/4$, and $H(\frac14,\frac34)=\frac14\cdot2+\frac34\log\frac43=0.5+0.75\cdot0.41504=0.81128$. ✓.
4. Mutual information: $I(X;Y)=H(Y)-H(Y|X)=1-0.81128=0.18872$ bits. Check via $D(p\|p_Xp_Y)$, where $p_Xp_Y=1/4$ each: $2\cdot\frac38\log\frac{3/8}{1/4}+2\cdot\frac18\log\frac{1/8}{1/4}=\frac34\log1.5+\frac14\log0.5=0.75\cdot0.58496-0.25=0.18872$. ✓ ($\ge0$, and $\ne0$ since $p\ne p_Xp_Y$.)
5. Data processing: let $Z=g(Y)=0$ (constant). Then $X\to Y\to Z$ and $I(X;Z)=0\le0.18872=I(X;Y)$. With $Z=Y$ (a one-to-one function) $I(X;Z)=0.18872$, so equality holds, as the corollary allows.

## Concepts
- [[entropy-H-X]] — $H(X)=-\sum p\log p=E\log\frac1{p(X)}$; depends only on the probabilities (p. 13).
- [[bit]] — unit of entropy when the log is base 2; a fair coin toss is 1 bit (p. 13).
- [[self-information-surprisal]] — the text says entropy is sometimes called self-information because $I(X;X)=H(X)$ (p. 20). The word "surprisal" in the id is ours, not the text's.
- [[joint-and-conditional-entropy]] — $H(X,Y)$ and $H(Y|X)=\sum_xp(x)H(Y|X=x)$ (p. 16).
- [[chain-rule]] — $H(X,Y)=H(X)+H(Y|X)$ and its versions for mutual information and relative entropy (pp. 16, 21–23).
- [[mutual-information-I-X-Y]] — $D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$; symmetric; zero iff independent (pp. 18–20, 27).
- [[relative-entropy-KL-divergence]] — $D(p\|q)=E_p\log\frac{p}{q}$; extra bits for using $q$ when truth is $p$; not symmetric (p. 18).
- [[data-processing-inequality]] — $X\to Y\to Z$ implies $I(X;Y)\ge I(X;Z)$ (p. 32).
- [[fanos-inequality]] — $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ (p. 39).
- [[jensen-inequality]] (new) — $Ef(X)\ge f(EX)$ for convex $f$; basis for $D\ge0$ (p. 25).
- [[convex-concave-function]] (new) — convex: lies below its chords; concave: $-f$ is convex (p. 23).
- [[log-sum-inequality]] (new) — $\sum a_i\log\frac{a_i}{b_i}\ge(\sum a_i)\log\frac{\sum a_i}{\sum b_i}$ (p. 29).
- [[conditioning-reduces-entropy]] (new) — $H(X|Y)\le H(X)$ on average, equality iff independent (p. 27).
- [[markov-chain-three-variables]] (new) — $X\to Y\to Z$: $p(x,y,z)=p(x)p(y|x)p(z|y)$ (p. 32).
- [[second-law-markov-chains]] (new) — relative entropy between chain distributions never increases; entropy increases if stationary distribution is uniform (pp. 33–36).
- [[doubly-stochastic-matrix]] (new) — transition matrix with all row and column sums 1; uniform is stationary iff doubly stochastic (p. 35).
- [[sufficient-statistic]] (new) — $T(X)$ with $\theta\to T(X)\to X$; equivalent to $I(\theta;X)=I(\theta;T(X))$ (pp. 36–37).
- [[minimal-sufficient-statistic]] (new) — sufficient statistic that is a function of every other sufficient statistic (p. 38).
- [[maximum-entropy-principle]] — only the finite-range case appears here: $H(X)\le\log|\mathcal X|$ with equality iff uniform (p. 27). The general principle is not stated in this unit.

## Canonical instances
- [[binary-entropy-function]] — $H(p)$, concave, 0 at $p\in\{0,1\}$, 1 bit at $p=\frac12$ (p. 14).
- [[example-seven-quarters-bits]] — pmf $(\frac12,\frac14,\frac18,\frac18)$ has $H=7/4$ bits, matching 1.75 expected binary questions (p. 15).
- [[joint-distribution-4x4-example]] — $H(X)=7/4$, $H(Y)=2$, $H(X|Y)=11/8$, $H(Y|X)=13/8$, $H(X,Y)=27/8$, $I=0.375$ (pp. 17, 21).
- [[kl-asymmetry-example]] — $D(p\|q)=0.2075\ne D(q\|p)=0.1887$ bits (p. 19).
- [[evidence-increases-uncertainty-example]] — $H(X|Y{=}2)>H(X)$ yet $H(X|Y)=0.25<0.544$ (p. 28).
- [[sum-of-independent-bits-example]] — $Z=X+Y$ gives $I(X;Y|Z)=\frac12>I(X;Y)=0$ (p. 33).
- [[canada-england-wealth-example]] — author's illustration of decreasing relative entropy between two Markov distributions (p. 34).
- [[coin-toss-sufficient-statistic]] — number of 1s is sufficient for the bias $\theta$ (p. 37).
- [[card-shuffle-entropy]] — shuffling independent of the deck order does not decrease entropy (p. 36).

## Bridges (candidates)
- [same-math] $D(p\|q)$ ↔ statistics: expected log-likelihood ratio — the text says $D$ arises as such (p. 18).
- [same-math] $H(p)+D(p\|q)$ as average code length with $q$'s code ↔ cross-entropy loss: $H(p)+D(p\|q)$ is the average length with $q$'s code (p. 18). The historical note lists "cross entropy" as one name for $D$ itself (p. 49), so check the naming before confirming.
- [same-math] Sufficient statistic as equality case of data processing ↔ statistics: Markov chain $\theta\to T(X)\to X$ (p. 37).
- [structural-analogy] $H(X|Y)\le H(X)$ only on average ↔ social science/evidence: specific evidence can raise uncertainty, but expected evidence cannot (p. 28).
- [structural-analogy] Decreasing $D(\mu_n\|\mu_n')$ under a shared transition rule ↔ economics: two populations under the same redistribution rule becoming more alike (p. 34). This is the author's illustration, not a derived result.

## Questions this raises
- Under what conditions is the limit of $D(\mu_n\|\mu)$ exactly 0? The text says uniqueness of the stationary distribution suffices but gives no proof (p. 35).
- How do these quantities change for continuous variables? The text defers this to Chapter 9 (p. 37).
- What does $I(X;Y;Z)=I(X;Y)-I(X;Y|Z)$ mean if it can be negative? (Problem 12, p. 45.)
- How does Fano's inequality feed the converse of the noisy-channel coding theorem (Chapter 8, p. 38)?

## Exercises worth doing
- Ex. 1 (p. 42) — entropy of a geometric variable and an efficient question scheme; connects $H(X)$ to expected question count — difficulty: easy
- Ex. 5 (p. 43) — $H(g(X))\le H(X)$ via the chain rule applied two ways — difficulty: easy
- Ex. 10 (p. 44) — conditional MI both smaller and larger than $I(X;Y)$; shows what a Markov structure rules out — difficulty: medium
- Ex. 12 (p. 45) — three-variable mutual information, which can be negative — difficulty: medium
- Ex. 22 (p. 47) — bottleneck: $I(X_1;X_3)\le\log k$ via data processing — difficulty: medium
- Ex. 33 (p. 48) — Fano's inequality without conditioning, by maximising $H(\mathbf p)$ under $1-p_1=P_e$ — difficulty: medium

## Reading notes
- The PDF is the 1991 first edition (title page: "Copyright 1991 John Wiley & Sons, Inc.", Print ISBN 0-471-06259-6), not the 2006 second edition. Chapter content and numbering may differ from the second edition.
- Page offset: printed = pdf − 22 (PDF page 34 is printed page 12). Printed numbers are shown in the page labels.
- The text layer is garbled in many equations. I checked the page images for everything cited above (e.g. (2.4)–(2.5), the table on p. 17, the table on p. 28).
- Apparent misprint on p. 33: in the image, (2.120) and (2.121) show the same right-hand side, $I(X;Z)+I(X;Y|Z)$. The proof needs the second expansion $I(X;Y)+I(X;Z|Y)$, which I used, and I flagged this in L3.
- In the proof of Fano's inequality (p. 40), the bound on $H(X|E{=}1,Y)$ mentions "$|\mathcal X|$ if $g(Y)\notin\mathcal X$" but then uses $\log(|\mathcal X|-1)$. This seems to assume $g(Y)\in\mathcal X$ (my observation).
- Notation in the text layer sometimes writes $I(X,Y)$ with a comma. The page images mostly show $I(X;Y)$, which I used.
- Chapter summary item "Entropy $H(X_n)$ increases if the stationary distribution is uniform" is as printed on p. 42.
- Historical notes (p. 49) cite reference numbers (e.g. [238]) without bibliographic details in these pages.
