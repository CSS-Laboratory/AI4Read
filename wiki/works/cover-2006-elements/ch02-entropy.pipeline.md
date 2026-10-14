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
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 5
---
# Entropy, Relative Entropy and Mutual Information

## L0 — One line
Entropy measures the uncertainty of a random variable; mutual information extends this notion and is a special case of relative entropy, and Jensen's inequality underlies many of their basic properties (such as non-negativity); together with the chain rules it gives the data processing inequality.

## L1 — The gist (≤ 120 words)
This chapter defines the basic quantities of information theory for discrete random variables: entropy (uncertainty of one variable), joint and conditional entropy, relative entropy (a non-symmetric "distance" between distributions) and mutual information (how much one variable tells about another). It proves their main properties: chain rules, non-negativity of relative entropy and mutual information, conditioning on average reduces entropy, the data processing inequality, and Fano's inequality. Jensen's inequality and the log sum inequality are the main tools. It also shows that for Markov chains relative entropy does not increase, a version of the second law of thermodynamics, and links mutual information to sufficient statistics.

**Prerequisites:** discrete probability (joint, marginal, conditional pmf; expectation); logarithms; second derivatives and convexity; the idea of a Markov chain (defined in 2.8).

## L2 — Key ideas (5–10 bullets)
- Entropy $H(X)=-\sum p\log p$ depends only on the probabilities, is $\ge 0$, and is at most $\log|\mathcal X|$, with equality iff $X$ is uniform (pp. 13–14, 27).
- The chain rule $H(X,Y)=H(X)+H(Y|X)$ extends to $n$ variables, to mutual information and to relative entropy (pp. 16, 21–23).
- Mutual information is the relative entropy between the joint distribution and the product of the marginals; it equals $H(X)-H(X|Y)$, is symmetric, and is $\ge 0$ with equality iff independence (pp. 18–20, 27).
- Jensen's inequality (for convex $f$, $Ef(X)\ge f(EX)$) gives $D(p\|q)\ge 0$; the log sum inequality gives convexity of $D$, concavity of $H$, and concavity or convexity of $I$ (pp. 25–31).
- Conditioning reduces entropy on average, not for every value of the conditioning variable (p. 28).
- Data processing inequality: if $X\to Y\to Z$ is a Markov chain, then $I(X;Y)\ge I(X;Z)$, so processing cannot add information about $X$ (p. 32).
- For Markov chains, relative entropy between two state distributions does not increase with time; entropy itself need not increase unless the stationary distribution is uniform (pp. 34–36).
- A statistic is sufficient iff it preserves mutual information with the parameter for all distributions on the parameter (pp. 36–37, 42).
- Fano's inequality bounds $H(X|Y)$ above by a function of the error probability $P_e$ of guessing $X$ from $Y$; a weaker form is $P_e\ge\frac{H(X|Y)-1}{\log|\mathcal X|}$ (pp. 38–40).

## L3 — Walkthrough

**Chapter introduction (p. 12).** The chapter defines entropy and mutual information, then proves chain rules, non-negativity of mutual information, the data processing inequality, and studies whether the second law of thermodynamics holds for Markov processes. The author says the concept of information is too broad for one definition. Entropy has properties that match what a measure of information should be. Mutual information extends it, and entropy then becomes the "self-information" of a random variable. Mutual information is a special case of relative entropy (p. 12). Their value is to be tested in later chapters (p. 12).

### 2.1 Entropy (pp. 12–15)
Let $X$ be a discrete random variable (takes countably many values) with alphabet $\mathcal X$ and pmf (probability mass function) $p(x)=\Pr\{X=x\}$. Here $p(x)$ and $p(y)$ denote different pmfs $p_X$, $p_Y$ (p. 13).

**Definition.** The entropy is
$$H(X)=-\sum_{x\in\mathcal X}p(x)\log p(x).\tag{2.1}$$
- $\log$ is base 2 and entropy is in bits. A fair coin toss has 1 bit. Convention $0\log 0=0$, justified by continuity ($x\log x\to0$ as $x\to0$), so zero-probability terms change nothing (p. 13).
- With base $b$ the entropy is $H_b(X)$; base $e$ gives nats (p. 13).
- Entropy is a functional of the distribution: it does not depend on the values $X$ takes, only on the probabilities (p. 13).
- Expectation: $E_pg(X)=\sum_{x}g(x)p(x)$ (2.2). Entropy is the expectation of $\log\frac1{p(X)}$ (the author calls this "eerily self-referential"):
$$H(X)=E_p\log\frac1{p(X)}.\tag{2.3}$$
- The author will not justify $H$ axiomatically. He will show it answers natural questions such as the average length of the shortest description (pp. 13–14). An axiomatic route is in Problem 4 (p. 43).

**Lemma 2.1.1.** $H(X)\ge0$, because $0\le p(x)\le1$ implies $\log(1/p(x))\ge0$ (p. 14).

**Lemma 2.1.2.** $H_b(X)=(\log_ba)H_a(X)$, because $\log_bp=\log_ba\,\log_ap$ (p. 14).

**Example 2.1.1 (binary entropy).** $X=1$ with probability $p$, $0$ with probability $1-p$. Then
$$H(X)=-p\log p-(1-p)\log(1-p)\overset{\text{def}}{=}H(p).\tag{2.5}$$
$H(p)=1$ bit at $p=1/2$, equals $0$ at $p=0$ or $1$ (no randomness), and is concave in the distribution (Fig. 2.1) (p. 14).

**Example 2.1.2.** $X=a,b,c,d$ with probabilities $1/2,1/4,1/8,1/8$:
$$H(X)=-\tfrac12\log\tfrac12-\tfrac14\log\tfrac14-\tfrac18\log\tfrac18-\tfrac18\log\tfrac18=\tfrac74\text{ bits}.\tag{2.7}$$
Asking "Is $X=a$?", then "$X=b$?", then "$X=c$?" needs 1.75 questions on average. This is the minimum expected number of binary questions. Chapter 5 shows the minimum lies between $H(X)$ and $H(X)+1$ (p. 15).

*Intuition note.* Entropy is, up to at most one question, the minimum average number of yes/no questions needed to pin down the value (exact in the author's 7/4 example; Chapter 5 shows the minimum lies between $H(X)$ and $H(X)+1$, p. 15). Rare outcomes need more questions, but they are rare. Only the probabilities matter, not the labels.

### 2.2 Joint and conditional entropy (pp. 15–17)
**Joint entropy.** $(X,Y)$ is just one vector-valued variable, so
$$H(X,Y)=-\sum_{x}\sum_{y}p(x,y)\log p(x,y)=-E\log p(X,Y).\tag{2.8, 2.9}$$

**Conditional entropy.** It is the average, over $x$, of the entropy of the conditional distribution (p. 16):
$$H(Y|X)=\sum_xp(x)H(Y|X=x)=-\sum_x\sum_yp(x,y)\log p(y|x)=-E\log p(Y|X).\tag{2.10–2.13}$$

**Theorem 2.2.1 (Chain rule).** $H(X,Y)=H(X)+H(Y|X)$ (2.14).
Proof (p. 16): write $p(x,y)=p(x)p(y|x)$ inside the log, split the sum, and sum $p(x,y)$ over $y$ in the first part (2.15–2.19):
$$H(X,Y)=-\sum_{x,y}p(x,y)\log p(x)-\sum_{x,y}p(x,y)\log p(y|x)=H(X)+H(Y|X).$$
Equivalently, take the expectation of $\log p(X,Y)=\log p(X)+\log p(Y|X)$ (2.20).

**Corollary.** $H(X,Y|Z)=H(X|Z)+H(Y|X,Z)$ (2.21), proved the same way (p. 17).

**Example 2.2.1 (p. 17).** Joint pmf (rows $Y$, columns $X=1,2,3,4$):

| | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| $Y=1$ | 1/8 | 1/16 | 1/32 | 1/32 |
| $Y=2$ | 1/16 | 1/8 | 1/32 | 1/32 |
| $Y=3$ | 1/16 | 1/16 | 1/16 | 1/16 |
| $Y=4$ | 1/4 | 0 | 0 | 0 |

Marginal of $X$ is $(\frac12,\frac14,\frac18,\frac18)$, of $Y$ is $(\frac14,\frac14,\frac14,\frac14)$. So $H(X)=7/4$ bits and $H(Y)=2$ bits. Then
$$H(X|Y)=\tfrac14H(\tfrac12,\tfrac14,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac12,\tfrac18,\tfrac18)+\tfrac14H(\tfrac14,\tfrac14,\tfrac14,\tfrac14)+\tfrac14H(1,0,0,0)=\tfrac14\cdot\tfrac74+\tfrac14\cdot\tfrac74+\tfrac14\cdot2+\tfrac14\cdot0=\tfrac{11}8\text{ bits}.$$
Similarly $H(Y|X)=13/8$ bits and $H(X,Y)=27/8$ bits.
**Remark:** $H(Y|X)\ne H(X|Y)$, but $H(X)-H(X|Y)=H(Y)-H(Y|X)$ (p. 17).

*Intuition note.* The chain rule says: the uncertainty of a pair is the uncertainty of the first plus what is left of the second once the first is known. The order of the two variables is free.

### 2.3 Relative entropy and mutual information (pp. 18–19)
The author introduces relative entropy as a measure of the "distance" between two distributions. In statistics it is an expected log likelihood ratio. $D(p\|q)$ measures the inefficiency of assuming the distribution is $q$ when it is truly $p$. A code built for the true $p$ has average length $H(p)$. Using the code for $q$ would need $H(p)+D(p\|q)$ bits on average (p. 18).

**Definition (relative entropy, Kullback–Leibler distance).**
$$D(p\|q)=\sum_{x\in\mathcal X}p(x)\log\frac{p(x)}{q(x)}=E_p\log\frac{p(X)}{q(X)}.\tag{2.26, 2.27}$$
Conventions: $0\log\frac0q=0$ and $p\log\frac p0=\infty$ (p. 18). The author says it will be shown that $D\ge0$ with equality iff $p=q$. It is not a true distance: it is not symmetric and fails the triangle inequality, yet it is often useful to think of it as a distance (p. 18).

**Definition (mutual information).** For joint pmf $p(x,y)$ and marginals $p(x),p(y)$, $I(X;Y)$ is the relative entropy between the joint and the product distribution:
$$I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}=D\big(p(x,y)\|p(x)p(y)\big)=E_{p(x,y)}\log\frac{p(X,Y)}{p(X)p(Y)}.\tag{2.28–2.30}$$

**Example 2.3.1 (p. 19).** $\mathcal X=\{0,1\}$, $p=(1-r,r)$, $q=(1-s,s)$:
$$D(p\|q)=(1-r)\log\frac{1-r}{1-s}+r\log\frac rs,\qquad D(q\|p)=(1-s)\log\frac{1-s}{1-r}+s\log\frac sr.\tag{2.31, 2.32}$$
If $r=s$ both are 0. For $r=1/2$, $s=1/4$:
$$D(p\|q)=\tfrac12\log\frac{1/2}{3/4}+\tfrac12\log\frac{1/2}{1/4}=1-\tfrac12\log3=0.2075\text{ bits},$$
$$D(q\|p)=\tfrac34\log\frac{3/4}{1/2}+\tfrac14\log\frac{1/4}{1/2}=\tfrac34\log3-1=0.1887\text{ bits}.$$
So $D(p\|q)\ne D(q\|p)$ in general.

### 2.4 Relationship between entropy and mutual information (pp. 19–21)
Rewrite $I$ using $p(x,y)/(p(x)p(y))=p(x|y)/p(x)$:
$$I(X;Y)=\sum p(x,y)\log\frac{p(x|y)}{p(x)}=-\sum p(x,y)\log p(x)+\sum p(x,y)\log p(x|y)=H(X)-H(X|Y).\tag{2.35–2.39}$$
So $I(X;Y)$ is the reduction in uncertainty of $X$ due to knowing $Y$. By symmetry $I(X;Y)=H(Y)-H(Y|X)$ (2.40): "$X$ says as much about $Y$ as $Y$ says about $X$." With the chain rule, $I(X;Y)=H(X)+H(Y)-H(X,Y)$ (2.41). Also $I(X;X)=H(X)-H(X|X)=H(X)$ (2.42). This is why entropy is sometimes called self-information (p. 20).

**Theorem 2.4.1.** (2.43) $I(X;Y)=H(X)-H(X|Y)$; (2.44) $I(X;Y)=H(Y)-H(Y|X)$; (2.45) $I(X;Y)=H(X)+H(Y)-H(X,Y)$; (2.46) $I(X;Y)=I(Y;X)$; (2.47) $I(X;X)=H(X)$ (p. 20).

Figure 2.2 is a Venn diagram: two overlapping circles $H(X)$ and $H(Y)$, with the overlap $I(X;Y)$, the left part $H(X|Y)$, the right part $H(Y|X)$ and the union $H(X,Y)$ (pp. 20–21).

**Example 2.4.1.** For the distribution of Example 2.2.1, $I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)=0.375$ bits (p. 21). (Check: $7/4-11/8=3/8$.)

*Intuition note.* Mutual information is the shared part of two uncertainties. It is the same number whichever variable you consider "the one being learned about".

### 2.5 Chain rules for entropy, relative entropy and mutual information (pp. 21–23)
**Theorem 2.5.1 (Chain rule for entropy).** For $X_1,\dots,X_n\sim p(x_1,\dots,x_n)$:
$$H(X_1,\dots,X_n)=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\tag{2.48}$$
Proof (p. 21): repeat the two-variable rule: $H(X_1,X_2)=H(X_1)+H(X_2|X_1)$ (2.49), $H(X_1,X_2,X_3)=H(X_1)+H(X_2,X_3|X_1)=H(X_1)+H(X_2|X_1)+H(X_3|X_2,X_1)$ (2.50, 2.51), and so on up to (2.52, 2.53). Alternative proof (pp. 21–22): write $p(x_1,\dots,x_n)=\prod_ip(x_i|x_{i-1},\dots,x_1)$, so $-\log p=-\sum_i\log p(x_i|x_{i-1},\dots,x_1)$. Swap the sums, and sum out the variables $x_{i+1},\dots,x_n$ (2.54–2.59).

**Definition (conditional mutual information).**
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=E_{p(x,y,z)}\log\frac{p(X,Y|Z)}{p(X|Z)p(Y|Z)}.\tag{2.60, 2.61}$$

**Theorem 2.5.2 (Chain rule for information).**
$$I(X_1,\dots,X_n;Y)=\sum_{i=1}^nI(X_i;Y|X_{i-1},\dots,X_1).\tag{2.62}$$
Proof (p. 22): $I(X_1,\dots,X_n;Y)=H(X_1,\dots,X_n)-H(X_1,\dots,X_n|Y)$, expand both terms with Theorem 2.5.1, and group termwise (2.63, 2.64).

**Definition (conditional relative entropy).** The average, over $p(x)$, of the relative entropies between $p(y|x)$ and $q(y|x)$:
$$D(p(y|x)\|q(y|x))=\sum_xp(x)\sum_yp(y|x)\log\frac{p(y|x)}{q(y|x)}=E_{p(x,y)}\log\frac{p(Y|X)}{q(Y|X)}.\tag{2.65, 2.66}$$
The notation omits the distribution $p(x)$ of the conditioning variable; it is understood from context (p. 23).

**Theorem 2.5.3 (Chain rule for relative entropy).**
$$D(p(x,y)\|q(x,y))=D(p(x)\|q(x))+D(p(y|x)\|q(y|x)).\tag{2.67}$$
Proof (p. 23): factor $p(x,y)=p(x)p(y|x)$ and $q(x,y)=q(x)q(y|x)$, split the log of the ratio into two terms, and sum out $y$ in the first (2.68–2.71). It is used in 2.9 to prove a form of the second law.

### 2.6 Jensen's inequality and its consequences (pp. 23–28)
**Definition (convex).** $f$ is convex on $(a,b)$ if for all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$,
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2).\tag{2.72}$$
It is strictly convex if equality holds only for $\lambda=0$ or $1$. $f$ is concave if $-f$ is convex. A convex function lies below its chords; a concave one above (p. 23). The author's convex examples are $x^2,|x|,e^x,x\log x$ ($x\ge0$); concave examples are $\log x$ and $\sqrt x$ ($x\ge0$). Linear functions are both (p. 24).

**Theorem 2.6.1.** If $f$ has a second derivative that is non-negative (positive) everywhere, then $f$ is convex (strictly convex).
Proof (pp. 24–25): Taylor expansion
$$f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x^*)}2(x-x_0)^2,\tag{2.73}$$
with $x^*$ between $x_0$ and $x$. The last term is $\ge0$, so $f(x)\ge f(x_0)+f'(x_0)(x-x_0)$. Take $x_0=\lambda x_1+(1-\lambda)x_2$:
$$f(x_1)\ge f(x_0)+f'(x_0)[(1-\lambda)(x_1-x_2)],\quad f(x_2)\ge f(x_0)+f'(x_0)[\lambda(x_2-x_1)].\tag{2.74, 2.75}$$
Multiply by $\lambda$ and $1-\lambda$ and add; this gives (2.72). (added step: the derivative terms cancel because $\lambda(1-\lambda)(x_1-x_2)+(1-\lambda)\lambda(x_2-x_1)=0$.) Strict convexity is similar. Hence $x^2,e^x,x\log x$ are strictly convex and $\log x,\sqrt x$ strictly concave (p. 25).

**Theorem 2.6.2 (Jensen's inequality).** If $f$ is convex and $X$ a random variable, $Ef(X)\ge f(EX)$ (2.76). If $f$ is strictly convex, equality implies $X=EX$ with probability 1, i.e. $X$ is constant.
Proof for discrete $X$ by induction on the number of mass points (pp. 25–26). Two points: the inequality is exactly (2.72), i.e. $p_1f(x_1)+p_2f(x_2)\ge f(p_1x_1+p_2x_2)$ (2.77). Suppose true for $k-1$ points; put $p_i'=p_i/(1-p_k)$:
$$\sum_{i=1}^kp_if(x_i)=p_kf(x_k)+(1-p_k)\sum_{i=1}^{k-1}p_i'f(x_i)\ge p_kf(x_k)+(1-p_k)f\Big(\sum_{i=1}^{k-1}p_i'x_i\Big)\ge f\Big(\sum_{i=1}^kp_ix_i\Big).\tag{2.78–2.81}$$
The first inequality is the induction hypothesis, the second is convexity. The equality conditions are left to the reader; the continuous case follows by continuity arguments (p. 26).

**Theorem 2.6.3 (Information inequality).** $D(p\|q)\ge0$ (2.82), with equality iff $p(x)=q(x)$ for all $x$ (2.83).
Proof (p. 26). Let $A=\{x:p(x)>0\}$.
$$-D(p\|q)=\sum_{x\in A}p(x)\log\frac{q(x)}{p(x)}\le\log\sum_{x\in A}p(x)\frac{q(x)}{p(x)}=\log\sum_{x\in A}q(x)\le\log\sum_{x\in\mathcal X}q(x)=\log1=0.\tag{2.84–2.90}$$
The first inequality (2.86) is Jensen with the strictly concave $\log$. Equality there holds iff $q(x)/p(x)=1$ everywhere, i.e. $p=q$.

*Intuition note.* On average, the log of the ratio $p/q$ cannot be negative when the average is taken under $p$, the numerator's own distribution. Coding with the wrong distribution never helps on average.

**Corollaries (p. 27).**
- (2.91) $I(X;Y)\ge0$, equality iff $X,Y$ independent, because $I=D(p(x,y)\|p(x)p(y))$.
- (2.92) $D(p(y|x)\|q(y|x))\ge0$, equality iff $p(y|x)=q(y|x)$ for all $y$ and all $x$ with $p(x)>0$.
- (2.93) $I(X;Y|Z)\ge0$, equality iff $X,Y$ are conditionally independent given $Z$.

**Theorem 2.6.4.** $H(X)\le\log|\mathcal X|$, with equality iff $X$ is uniform over $\mathcal X$. With $u(x)=1/|\mathcal X|$:
$$D(p\|u)=\sum p(x)\log\frac{p(x)}{u(x)}=\log|\mathcal X|-H(X)\ge0.\tag{2.94, 2.95}$$
The uniform distribution is the maximum entropy distribution on a given range (p. 27).

**Theorem 2.6.5 (Conditioning reduces entropy).** $H(X|Y)\le H(X)$ (2.96), equality iff $X,Y$ independent, since $0\le I(X;Y)=H(X)-H(X|Y)$ (pp. 27–28). This is true only on average: $H(X|Y=y)$ may be greater than, less than or equal to $H(X)$, while $H(X|Y)=\sum_yp(y)H(X|Y=y)\le H(X)$. In a court case, a specific piece of evidence may increase uncertainty, but on average evidence decreases it (p. 28).

**Example 2.6.1 (p. 28).** Joint pmf: $p(X{=}1,Y{=}1)=0$, $p(2,1)=3/4$, $p(1,2)=1/8$, $p(2,2)=1/8$. Then $H(X)=H(\frac18,\frac78)=0.544$ bits, $H(X|Y=1)=0$, $H(X|Y=2)=1$ bit. So $H(X|Y)=\frac34\cdot0+\frac14\cdot1=0.25$ bits. Observing $Y=2$ increases the uncertainty in $X$, observing $Y=1$ decreases it, and it decreases on average.

**Theorem 2.6.6 (Independence bound).** $H(X_1,\dots,X_n)\le\sum_iH(X_i)$ (2.97), with equality iff the $X_i$ are independent. Proof (p. 28): by the chain rule (2.98), then each $H(X_i|X_{i-1},\dots,X_1)\le H(X_i)$ (2.99). Equality iff each $X_i$ is independent of $X_{i-1},\dots,X_1$.

### 2.7 The log sum inequality and its applications (pp. 29–31)
**Theorem 2.7.1 (Log sum inequality).** For non-negative $a_1,\dots,a_n$ and $b_1,\dots,b_n$,
$$\sum_{i=1}^na_i\log\frac{a_i}{b_i}\ge\Big(\sum_{i=1}^na_i\Big)\log\frac{\sum_ia_i}{\sum_ib_i},\tag{2.100}$$
with equality iff $a_i/b_i$ is constant. Conventions: $0\log0=0$, $a\log\frac a0=\infty$ for $a>0$, $0\log\frac00=0$ (p. 29).
Proof (p. 29): assume $a_i,b_i>0$. $f(t)=t\log t$ is strictly convex since $f''(t)=\frac1t\log e>0$. Jensen gives $\sum\alpha_if(t_i)\ge f(\sum\alpha_it_i)$ (2.101) for $\alpha_i\ge0$, $\sum\alpha_i=1$. Set $\alpha_i=b_i/\sum_jb_j$ and $t_i=a_i/b_i$:
$$\sum_i\frac{a_i}{\sum b_j}\log\frac{a_i}{b_i}\ge\Big(\sum_i\frac{a_i}{\sum b_j}\Big)\log\sum_i\frac{a_i}{\sum b_j}.\tag{2.102}$$
Multiplying by $\sum_jb_j$ gives (2.100) (added step).

**Re-proof of $D\ge0$ (p. 29).** $D(p\|q)=\sum p\log\frac pq\ge(\sum p)\log\frac{\sum p}{\sum q}=1\log\frac11=0$ (2.103–2.105), with equality iff $p(x)/q(x)=c$; since both sum to 1, $c=1$.

**Theorem 2.7.2.** $D(p\|q)$ is convex in the pair $(p,q)$: $D(\lambda p_1+(1-\lambda)p_2\|\lambda q_1+(1-\lambda)q_2)\le\lambda D(p_1\|q_1)+(1-\lambda)D(p_2\|q_2)$ for $0\le\lambda\le1$ (2.106).
Proof (p. 30): apply the log sum inequality to one term:
$$(\lambda p_1+(1-\lambda)p_2)\log\frac{\lambda p_1+(1-\lambda)p_2}{\lambda q_1+(1-\lambda)q_2}\le\lambda p_1\log\frac{\lambda p_1}{\lambda q_1}+(1-\lambda)p_2\log\frac{(1-\lambda)p_2}{(1-\lambda)q_2},\tag{2.107}$$
and sum over $x$.

**Theorem 2.7.3 (Concavity of entropy).** $H(p)$ is concave in $p$. Proof: $H(p)=\log|\mathcal X|-D(p\|u)$ (2.108), with $u$ uniform; use convexity of $D$ (p. 30). Alternative proof (p. 30): let $X_1\sim p_1$, $X_2\sim p_2$ on the same set, let $\theta=1$ with probability $\lambda$ and $2$ with probability $1-\lambda$, and $Z=X_\theta$ (2.109). Then $Z\sim\lambda p_1+(1-\lambda)p_2$. Since conditioning reduces entropy, $H(Z)\ge H(Z|\theta)$ (2.110), i.e. $H(\lambda p_1+(1-\lambda)p_2)\ge\lambda H(p_1)+(1-\lambda)H(p_2)$ (2.111). One consequence: mixing two gases of equal entropy gives a gas with higher entropy (p. 31).

**Theorem 2.7.4.** For $(X,Y)\sim p(x)p(y|x)$, $I(X;Y)$ is a concave function of $p(x)$ for fixed $p(y|x)$, and a convex function of $p(y|x)$ for fixed $p(x)$ (p. 31).
Proof, part 1: $I=H(Y)-\sum_xp(x)H(Y|X=x)$ (2.112). For fixed $p(y|x)$, $p(y)$ is linear in $p(x)$, so $H(Y)$ is concave in $p(x)$. The second term is linear in $p(x)$. A concave function minus a linear one is concave.
Part 2: fix $p(x)$; take $p_1(y|x)$, $p_2(y|x)$ and the mixture $p_\lambda(y|x)=\lambda p_1(y|x)+(1-\lambda)p_2(y|x)$ (2.113). The joint $p_\lambda(x,y)=\lambda p_1(x,y)+(1-\lambda)p_2(x,y)$ (2.114) and $p_\lambda(y)=\lambda p_1(y)+(1-\lambda)p_2(y)$ (2.115) are mixtures. So is the product $q_\lambda(x,y)=p(x)p_\lambda(y)=\lambda q_1+(1-\lambda)q_2$ (2.116). Since $I=D(p_\lambda\|q_\lambda)$ (2.117) and $D$ is jointly convex, $I$ is convex in $p(y|x)$.

*Intuition note.* Mixing distributions can only raise entropy above the average of the parts. Information through a channel is concave in the input distribution and convex in the channel's conditional distribution (the author does not use the word "channel" here).

### 2.8 Data processing inequality (pp. 32–33)
**Definition (Markov chain).** $X\to Y\to Z$ if the conditional distribution of $Z$ depends only on $Y$ and is conditionally independent of $X$, i.e. $p(x,y,z)=p(x)p(y|x)p(z|y)$ (2.118) (p. 32).
Consequences (p. 32):
- $X\to Y\to Z$ iff $X$ and $Z$ are conditionally independent given $Y$, since $p(x,z|y)=\frac{p(x,y)p(z|y)}{p(y)}=p(x|y)p(z|y)$ (2.119). The author notes that this characterization extends to Markov fields.
- $X\to Y\to Z$ implies $Z\to Y\to X$, so one writes $X\leftrightarrow Y\leftrightarrow Z$.
- If $Z=f(Y)$ then $X\to Y\to Z$.

**Theorem 2.8.1 (Data processing inequality).** If $X\to Y\to Z$, then $I(X;Y)\ge I(X;Z)$.
Proof (p. 33): expand $I(X;Y,Z)$ in two ways by the chain rule: $I(X;Y,Z)=I(X;Z)+I(X;Y|Z)$ (2.120) and $=I(X;Y)+I(X;Z|Y)$ (the second line printed as (2.121) repeats the first; see Reading notes). Markovity gives $I(X;Z|Y)=0$, and $I(X;Y|Z)\ge0$, so $I(X;Y)\ge I(X;Z)$ (2.122). Equality iff $I(X;Y|Z)=0$, i.e. iff $X\to Z\to Y$ is a Markov chain. Similarly $I(Y;Z)\ge I(X;Z)$.

**Corollaries (p. 33).**
- If $Z=g(Y)$, then $I(X;Y)\ge I(X;g(Y))$: functions of the data cannot increase information about $X$.
- If $X\to Y\to Z$, then $I(X;Y|Z)\le I(X;Y)$ (2.123). Proof: from (2.120) and (2.121), using $I(X;Z|Y)=0$ and $I(X;Z)\ge0$. So observing a "downstream" $Z$ decreases (or leaves unchanged) the dependence of $X$ and $Y$.

**Counterexample without Markov structure (p. 33).** $X,Y$ independent fair bits, $Z=X+Y$. Then $I(X;Y)=0$ but $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=H(X|Z)=P(Z=1)H(X|Z=1)=\frac12$ bit.

*Intuition note.* Passing a signal through any further step, deterministic or random, cannot tell you more about the original. Conditioning on a downstream variable cannot raise dependence when the chain structure holds; without it, conditioning can raise dependence (the author's $Z=X+Y$ example).

### 2.9 The second law of thermodynamics (pp. 33–36)
The second law says the entropy of an isolated system is non-decreasing. In statistical thermodynamics entropy is often the log of the number of microstates; this matches the author's entropy exactly if all states are equally likely (p. 33). The isolated system is modelled as a Markov chain with transitions obeying physical laws; implicit is that, given the present state, the future is independent of the past. The author says he finds four interpretations of the second law (p. 33), but the text lists five numbered items (pp. 34–36). Entropy does not always increase, but relative entropy always decreases (pp. 33–34).

1. **$D(\mu_n\|\mu_n')$ decreases with $n$** (p. 34). Let $\mu_n,\mu_n'$ be two state distributions at time $n$, with joint pmfs $p(x_n,x_{n+1})=p(x_n)r(x_{n+1}|x_n)$ and $q(x_n,x_{n+1})=q(x_n)r(x_{n+1}|x_n)$, where $r$ is the transition function. The chain rule gives two expansions:
$$D(p(x_n,x_{n+1})\|q(x_n,x_{n+1}))=D(p(x_n)\|q(x_n))+D(p(x_{n+1}|x_n)\|q(x_{n+1}|x_n))=D(p(x_{n+1})\|q(x_{n+1}))+D(p(x_n|x_{n+1})\|q(x_n|x_{n+1})).$$
The conditional terms in the first line are both $r$, so that term is 0. The last term is $\ge0$ by the corollary to Theorem 2.6.3. Hence
$$D(p(x_n)\|q(x_n))\ge D(p(x_{n+1})\|q(x_{n+1})),\ \text{i.e. } D(\mu_n\|\mu_n')\ge D(\mu_{n+1}\|\mu_{n+1}').\tag{2.124, 2.125}$$
The author's illustration: if the tax system for redistributing wealth were the same in Canada and England, the wealth distributions would become more similar over time (p. 34).

2. **$D(\mu_n\|\mu)$ decreases for a stationary $\mu$** (pp. 34–35). Taking $\mu_n'$ to be a stationary distribution $\mu$ in (2.125), $\mu_{n+1}'$ is the same, so $D(\mu_n\|\mu)\ge D(\mu_{n+1}\|\mu)$ (2.126). The sequence is non-increasing and non-negative, so it has a limit. The limit is 0 if the stationary distribution is unique, "but this is more difficult to prove" (p. 35).

3. **Entropy increases if the stationary distribution is uniform** (p. 35). In general, falling relative entropy does not imply rising entropy. Counterexample: any Markov chain with a non-uniform stationary distribution, started from the uniform distribution (already of maximum entropy). It tends to the stationary distribution, which has lower entropy. If the stationary distribution is uniform,
$$D(\mu_n\|\mu)=\log|\mathcal X|-H(\mu_n)=\log|\mathcal X|-H(X_n),\tag{2.127}$$
so falling $D$ means rising $H$. The author says this is the explanation closest to statistical thermodynamics. **Definition:** a transition matrix $[P_{ij}]$, $P_{ij}=\Pr\{X_{n+1}=j|X_n=i\}$, is *doubly stochastic* if $\sum_iP_{ij}=1$ for all $j$ (2.128) and $\sum_jP_{ij}=1$ for all $i$ (2.129). **Remark:** the uniform distribution is stationary for $P$ iff $P$ is doubly stochastic (proof: Problem 1 of Chapter 4, outside this unit).

4. **$H(X_n|X_1)$ increases with $n$ for a stationary Markov process** (pp. 35–36). $H(X_n)$ is constant for a stationary process, but the conditional uncertainty of the future increases. Proof 1:
$$H(X_n|X_1)\ge H(X_n|X_1,X_2)=H(X_n|X_2)=H(X_{n-1}|X_1),\tag{2.130–2.132}$$
by conditioning reducing entropy, then Markovity, then stationarity. Proof 2: the data processing inequality for $X_1\to X_{n-1}\to X_n$ gives $I(X_1;X_{n-1})\ge I(X_1;X_n)$ (2.133), i.e. $H(X_{n-1})-H(X_{n-1}|X_1)\ge H(X_n)-H(X_n|X_1)$ (2.134). Stationarity gives $H(X_{n-1})=H(X_n)$, hence $H(X_{n-1}|X_1)\le H(X_n|X_1)$ (2.135). The same techniques show $H(X_0|X_n)$ is increasing in $n$ for any Markov chain (Problem 35) (p. 36).

5. **Shuffles increase entropy** (p. 36): if $T$ is a shuffle (permutation) of a deck, $X$ the initial random order, and $T$ independent of $X$, then $H(TX)\ge H(X)$ (2.136). Problem 31 outlines a proof.

*Intuition note.* Two different starting distributions fed through the same dynamics become harder to tell apart. This does not mean disorder grows: entropy is guaranteed to rise if the long-run (stationary) state is uniform, but with a non-uniform stationary state it can fall (e.g. when starting from the uniform distribution).

### 2.10 Sufficient statistics (pp. 36–38)
Let $\{f_\theta(x)\}$ be a family of pmfs indexed by $\theta$, $X$ a sample from one of them, and $T(X)$ any statistic (function of the sample). Then $\theta\to X\to T(X)$ and
$$I(\theta;T(X))\le I(\theta;X)\tag{2.137}$$
for any distribution on $\theta$. If equality holds, no information is lost (p. 36).

**Definition.** $T(X)$ is a *sufficient statistic* relative to $\{f_\theta\}$ if $X$ is independent of $\theta$ given $T(X)$, i.e. $\theta\to T(X)\to X$ is a Markov chain (p. 37). This is the equality condition of the data processing inequality: $I(\theta;X)=I(\theta;T(X))$ for all distributions on $\theta$ (2.138). So sufficient statistics preserve mutual information, and conversely (p. 37).

**Examples (pp. 37–38).**
1. $X_1,\dots,X_n\in\{0,1\}$ i.i.d. coin tosses with $\theta=\Pr(X_i=1)$: $T=\sum X_i$ is sufficient. Given $T=k$, all sequences with $k$ ones are equally likely and independent of $\theta$:
$$\Pr\Big\{(X_1,\dots,X_n)=(x_1,\dots,x_n)\,\Big|\,\sum X_i=k\Big\}=\begin{cases}1/\binom nk&\text{if }\sum x_i=k\\0&\text{otherwise}\end{cases}\tag{2.139}$$
2. $X\sim\mathcal N(\theta,1)$, $f_\theta(x)=\frac1{\sqrt{2\pi}}e^{-(x-\theta)^2/2}$ (2.140): for i.i.d. samples the sample mean $\bar X_n$ is sufficient. The author says it "can be verified" that the conditional distribution of the sample given $\bar X_n$ and $n$ does not depend on $\theta$.
3. $f_\theta=\text{Uniform}(\theta,\theta+1)$: $T=(\max\{X_i\},\min\{X_i\})$ is sufficient (2.141). The proof is "slightly more complicated".
(Examples 2 and 3 use densities; entropy for continuous variables is defined in Chapter 9, p. 37.)

**Definition (minimal sufficient statistic).** $T(X)$ is minimal sufficient if it is a function of every other sufficient statistic $U$; in terms of data processing, $\theta\to T(X)\to U(X)\to X$ (2.142) (p. 38). It maximally compresses the information about $\theta$. Other sufficient statistics may carry irrelevant information: for a normal with mean $\theta$, the pair (mean of odd-numbered samples, mean of even-numbered samples) is sufficient but not minimal. In the three examples above the statistics are also minimal (p. 38).

### 2.11 Fano's inequality (pp. 38–40)
We observe $Y$ and wish to guess a correlated $X$. Known from the chapter's problems: $H(X|Y)=0$ iff $X$ is a function of $Y$; so $X$ can be estimated from $Y$ with zero error probability iff $H(X|Y)=0$ (p. 38; Problem 6, p. 43, shows one direction). The author expects low error only if $H(X|Y)$ is small; Fano quantifies this. It will be crucial for the converse to Shannon's second theorem in Chapter 8 (p. 38).

Set-up: $\hat X=g(Y)$ estimates $X$; $X\to Y\to\hat X$ is a Markov chain; $P_e=\Pr\{\hat X\ne X\}$ (2.143) (p. 39).

**Theorem 2.11.1 (Fano's inequality).**
$$H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y).\tag{2.144}$$
Weakened forms: $1+P_e\log|\mathcal X|\ge H(X|Y)$ (2.145), or $P_e\ge\dfrac{H(X|Y)-1}{\log|\mathcal X|}$ (2.146). **Remark:** $P_e=0$ implies $H(X|Y)=0$ (p. 39).

Proof (pp. 39–40). Let $E=1$ if $\hat X\ne X$, else $0$. Expand $H(E,X|Y)$ two ways:
$$H(E,X|Y)=H(X|Y)+H(E|X,Y)=H(E|Y)+H(X|E,Y).\tag{2.148, 2.149}$$
- $H(E|X,Y)=0$, since $E$ is a function of $X$ and $g(Y)$.
- $H(E|Y)\le H(E)=H(P_e)$ (conditioning reduces entropy; $E$ is binary).
- $H(X|E,Y)=\Pr(E{=}0)H(X|Y,E{=}0)+\Pr(E{=}1)H(X|Y,E{=}1)\le(1-P_e)\cdot0+P_e\log(|\mathcal X|-1)$ (2.150, 2.151). Given $E=0$, $X=g(Y)$; given $E=1$, the conditional entropy is bounded by the log of the number of remaining outcomes ($|\mathcal X|-1$ if $g(Y)\in\mathcal X$, else $|\mathcal X|$).
Combining gives (2.144). The weakened forms use $H(P_e)\le1$ and $\log(|\mathcal X|-1)\le\log|\mathcal X|$ (added step).

**Remark: no knowledge of $Y$ (p. 40).** Let $X\in\{1,\dots,m\}$, $p_1\ge p_2\ge\dots\ge p_m$. The best guess is $\hat X=1$ with $P_e=1-p_1$, and Fano becomes $H(P_e)+P_e\log(m-1)\ge H(X)$ (2.152). The pmf $(p_1,\dots,p_m)=(1-P_e,\frac{P_e}{m-1},\dots,\frac{P_e}{m-1})$ achieves equality (2.153), so Fano's inequality is sharp.

*Intuition note.* If a lot of uncertainty about $X$ remains after seeing $Y$, no guessing rule can be reliably right. The inequality turns leftover uncertainty into a minimum error probability.

### Summary of Chapter 2 (pp. 40–42)
The author's "telegraphic" summary, which "omits qualifying conditions", restates: definitions (2.154–2.164); properties of $H$ (non-negative; base change; conditioning reduces entropy; $H(X_1..X_n)\le\sum H(X_i)$; $H\le\log|\mathcal X|$; concavity); properties of $D$ and $I$ ($I=H(X)-H(X|Y)=H(Y)-H(Y|X)=H(X)+H(Y)-H(X,Y)$; $D\ge0$; $I=D(p(x,y)\|p(x)p(y))\ge0$; $D(p\|u)=\log m-H(p)$; $D$ convex); chain rules; Jensen; log sum; data processing; the second-law items; sufficiency; Fano. Beyond 2.9, item 5 of the second law is stated as "$H(X_0|X_n)$ increases for any Markov chain" (p. 42). The summary states a sufficient statistic "if and only if" $I(\theta;X)=I(\theta;T(X))$ for all distributions on $\theta$ (p. 42).

### Problems (pp. 42–48) and Historical notes (p. 49)
There are 35 problems (listed under Exercises). Historical notes (p. 49), as stated: entropy first arose in thermodynamics; Boltzmann connected it to microstates, with $S=k\ln W$ on his gravestone; Hartley (1930s) used the logarithm of the alphabet size; Shannon first defined entropy and mutual information as here; Kullback and Leibler defined relative entropy, also known as Kullback–Leibler distance, cross entropy, information divergence and information for discrimination. Fano proved his inequality; Fisher defined sufficient statistics; Lehmann and Scheffé the minimal ones; Kullback related sufficiency and mutual information. Brillouin, Jaynes, Bennett and Landauer are cited on information and physics.

## Toy example (ours, not from the text)
Let $X,Y$ be bits with joint pmf $p(0,0)=p(1,1)=3/8$, $p(0,1)=p(1,0)=1/8$.

1. Marginals: $p(X{=}0)=3/8+1/8=1/2$, same for $Y$. So $H(X)=H(Y)=1$ bit.
2. Joint entropy: $H(X,Y)=-2\cdot\frac38\log\frac38-2\cdot\frac18\log\frac18$. With $\log\frac38=\log3-3=-1.41504$: $\frac34(1.41504)+\frac14(3)=1.06128+0.75=1.81128$ bits.
3. Chain rule: $H(Y|X)=H(X,Y)-H(X)=0.81128$. Check: given $X$, $Y$ has distribution $(3/4,1/4)$, and $H(3/4,1/4)=0.8113$. ✓
4. Mutual information (three ways): $H(X)-H(X|Y)=1-0.81128=0.18872$; $H(X)+H(Y)-H(X,Y)=2-1.81128=0.18872$; and as relative entropy, $D(p\|p_Xp_Y)=2\cdot\frac38\log\frac{3/8}{1/4}+2\cdot\frac18\log\frac{1/8}{1/4}=\frac34\log1.5+\frac14\log0.5=0.75(0.58496)-0.25=0.18872$. ✓ All equal and positive, since $X,Y$ are not independent.
5. Data processing: let $Z=g(Y)$ be a constant. Then $X\to Y\to Z$, $I(X;Z)=0\le0.18872=I(X;Y)$, as Theorem 2.8.1 requires.

## Concepts
- [[bit]] — unit of entropy when $\log$ is base 2; a fair coin has 1 bit; base $e$ gives nats (p. 13)
- [[entropy-HX]] — $H(X)=-\sum p\log p=E\log\frac1{p(X)}$; depends only on probabilities; $0\le H\le\log|\mathcal X|$ (pp. 13–14, 27)
- [[self-information-surprisal]] — here "self-information" means $I(X;X)=H(X)$, the entropy of a variable; the text does not use the per-outcome $-\log p(x)$ sense (p. 20)
- [[joint-and-conditional-entropy]] — $H(X,Y)$ is the entropy of the pair; $H(Y|X)=\sum_xp(x)H(Y|X=x)$ (pp. 15–16)
- [[chain-rule]] — $H(X_1..X_n)=\sum H(X_i|X_{i-1}..X_1)$; analogues for $I$ and $D$ (pp. 16, 21–23)
- [[mutual-information]] — $D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$; symmetric; $\ge0$, $=0$ iff independent (pp. 18–20, 27)
- [[conditional-mutual-information]] (new) — $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)$; $\ge0$; can exceed $I(X;Y)$ without a Markov chain (pp. 22, 33)
- [[relative-entropy-kl-divergence]] — $D(p\|q)=E_p\log\frac{p}{q}$; $\ge0$; not symmetric; no triangle inequality (p. 18). The author also lists "cross entropy" as another name for it (p. 49), unlike the canon's $H(p)+D(p\|q)$.
- [[jensen-inequality]] (new) — $Ef(X)\ge f(EX)$ for convex $f$ (p. 25)
- [[log-sum-inequality]] (new) — $\sum a_i\log\frac{a_i}{b_i}\ge(\sum a_i)\log\frac{\sum a_i}{\sum b_i}$ (p. 29)
- [[conditioning-reduces-entropy]] (new) — $H(X|Y)\le H(X)$ on average, not for each $y$ (p. 28)
- [[maximum-entropy-principle]] — only the fact that the uniform pmf maximizes $H$ on a finite alphabet (Thm 2.6.4); no constraints in the chapter text (Problem 30, p. 48, adds a mean constraint) (p. 27)
- [[markov-chain-xyz]] (new) — $X\to Y\to Z$ iff $p(x,y,z)=p(x)p(y|x)p(z|y)$, iff $X\perp Z\mid Y$ (p. 32)
- [[data-processing-inequality]] — $X\to Y\to Z\Rightarrow I(X;Y)\ge I(X;Z)$ (p. 32)
- [[second-law-markov-chains]] (new) — relative entropy between state distributions does not increase; entropy rises if the stationary distribution is uniform (pp. 33–36)
- [[doubly-stochastic-matrix]] (new) — rows and columns sum to 1; iff the uniform distribution is stationary (p. 35)
- [[sufficient-statistic]] (new) — $T$ with $\theta\to T(X)\to X$; equivalent to $I(\theta;T(X))=I(\theta;X)$ (p. 37)
- [[minimal-sufficient-statistic]] (new) — a sufficient statistic that is a function of every other sufficient statistic (p. 38)
- [[fanos-inequality]] — $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ (p. 39)

## Canonical instances
- [[binary-entropy-function]] — $H(p)$, concave, 0 at $p\in\{0,1\}$, 1 bit at $p=1/2$ (p. 14)
- [[dyadic-four-symbol-source]] — probabilities $1/2,1/4,1/8,1/8$: $H=7/4$ bits, 1.75 expected questions (pp. 14–15)
- [[joint-pmf-4x4-example]] — $H(X)=7/4$, $H(Y)=2$, $H(X|Y)=11/8$, $H(Y|X)=13/8$, $H(X,Y)=27/8$, $I=0.375$ (pp. 17, 21)
- [[kl-asymmetry-example]] — $D(p\|q)=0.2075\ne D(q\|p)=0.1887$ bits (p. 19)
- [[conditioning-can-raise-entropy-example]] — $H(X|Y=2)=1>H(X)=0.544$ but $H(X|Y)=0.25$ (p. 28)
- [[sum-of-fair-bits-example]] — $Z=X+Y$ gives $I(X;Y|Z)=\frac12>I(X;Y)=0$ (p. 33)
- [[bernoulli-sum-sufficiency]] — number of 1s is sufficient for a coin's $\theta$ (p. 37)
- [[canada-england-wealth-example]] — same redistribution system makes wealth distributions more similar (p. 34)
- [[fano-sharpness-example]] — pmf $(1-P_e,\frac{P_e}{m-1},\dots)$ attains Fano with equality (p. 40)

## Bridges (candidates)
- [same-math] $\log$ (number of equally likely microstates) = $H$ ↔ statistical thermodynamics: Boltzmann's entropy equals Shannon's $H$ when all states are equally likely (p. 33).
- [same-math] Sufficient statistic ↔ statistics: equality condition of the data processing inequality $I(\theta;T(X))=I(\theta;X)$ is the sufficiency condition (p. 37).
- [structural-analogy] Monotone fall of $D(\mu_n\|\mu)$ under a Markov transition ↔ convergence of Markov-chain simulation toward its stationary distribution: both are about a distribution approaching a fixed point.
- [structural-analogy] Fano's inequality ↔ classification or prediction from noisy data: leftover uncertainty $H(X|Y)$ forces a minimum error rate.

## Questions this raises
- Why is $\log$ the right function? What do the axioms of Problem 4 (grouping, continuity, normalization) force?
- If relative entropy only decreases along a Markov chain, when does it reach 0, and how fast?
- Chapter 5 will show that the minimum expected description length lies between $H(X)$ and $H(X)+1$. How exactly does this give the "shortest description" meaning of entropy?
- For continuous variables (Chapter 9), which of these properties survive (e.g. $H\ge0$)?

## Exercises worth doing
- Ex. 1 (p. 42) — entropy of a geometric variable; efficient yes–no questions versus $H(X)$ — difficulty: easy
- Ex. 5 (p. 43) — $H(g(X))\le H(X)$ by justifying steps with the chain rule — difficulty: easy
- Ex. 10 (p. 44) — examples where $I(X;Y|Z)$ is below or above $I(X;Y)$ — difficulty: medium
- Ex. 12 (p. 45) — three-variable mutual information can be negative; two identities — difficulty: medium
- Ex. 22 (p. 47) — bottleneck Markov chain: $I(X_1;X_3)\le\log k$ — difficulty: medium
- Ex. 7 (pp. 43–44) — extracting fair coin flips from a bent coin; at most $nH(p)$ on average — difficulty: hard

## Reading notes
- The chapter's first page prints "Copyright © 1991 John Wiley & Sons, Inc." and Print ISBN 0-471-06259-6; no edition number is printed. The metadata cites the 2006 second edition, so chapter content and numbering may differ from it.
- Page offset: printed = pdf − 22 (pdf 34 = printed 12). Printed numbers are given in the page labels; the unit is pp. 12–49.
- The text layer is heavily garbled (e.g. pdf 38 header shows "36" while the image shows 16; many equations mangled). Equations were taken from the page images.
- Misprint at p. 32/33: eq. (2.121) is printed as $I(X;Y,Z)=I(X;Z)+I(X;Y|Z)$, a repeat of (2.120). The proof needs $I(X;Y)+I(X;Z|Y)$ there; this is the version used in the text that follows.
- In 2.9 item 4 the text says "H(X_n) is constant. So the entropy is nonincreasing" (p. 35); it means the entropy does not increase.
- The proof of Theorem 2.6.4 as printed ends with the inequality (2.95); the "iff uniform" part follows from the equality case of Theorem 2.6.3 (added step). Jensen's equality conditions are left to the reader (p. 25).
- Sections 2.9–2.10 refer to Chapter 4 (doubly stochastic remark, p. 35) and Chapter 9 (continuous entropy, p. 37); these are outside the unit.
- The summary box (p. 41) says the log sum inequality holds "for $n$ positive numbers", while Theorem 2.7.1 says non-negative.
