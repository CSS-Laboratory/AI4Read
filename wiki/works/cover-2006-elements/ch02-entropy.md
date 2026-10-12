---
id: cover-2006-elements/ch02-entropy
work: cover-2006-elements
unit: "Chapter 2 — Entropy, Relative Entropy and Mutual Information"
pages: 12–49
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-12
---

# Entropy, Relative Entropy and Mutual Information

## L0 — One line
Entropy, relative entropy and mutual information are all one family of quantities, tied together by chain rules and by one inequality ($D(p\|q)\ge 0$), and from that inequality every basic fact about information follows.

## L1 — The gist (≤ 120 words)
The chapter asks: how do we measure the uncertainty in a random variable, and how much does one variable tell us about another? The answer is a small set of definitions. Entropy $H(X)$ measures uncertainty. Relative entropy $D(p\|q)$ measures the cost of assuming $q$ when the truth is $p$. Mutual information $I(X;Y)$ is the relative entropy between the joint distribution and the product of the marginals. Chain rules split big quantities into sums of small ones. Jensen's inequality gives $D\ge0$, hence "conditioning reduces entropy" and the data processing inequality. Fano's inequality turns remaining uncertainty into a lower bound on error. These facts are the toolkit for the rest of the book (p. 12).

## L2 — Key ideas (5–10 bullets)
- **Entropy depends only on probabilities, not on values.** $H(X)=-\sum p(x)\log p(x)=E\log\frac1{p(X)}$; it is $\ge0$ and is measured in bits when the log is base 2 (pp. 13–14). This is the basic "amount of uncertainty" every later result builds on.
- **Chain rule for entropy.** $H(X,Y)=H(X)+H(Y|X)$, and in general $H(X_1,\dots,X_n)=\sum_i H(X_i|X_{i-1},\dots,X_1)$ (pp. 16, 21). It lets us handle sequences one symbol at a time.
- **Relative entropy $D(p\|q)$ is a non-symmetric "distance."** It is $\ge0$ and $=0$ iff $p=q$ (pp. 18, 26). Coding with the wrong distribution $q$ costs $H(p)+D(p\|q)$ bits on average (p. 18).
- **Mutual information is a special relative entropy.** $I(X;Y)=D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$; it is symmetric, $\ge0$, and $I(X;X)=H(X)$ (pp. 18–20).
- **Jensen's inequality does most of the work.** From it come $D\ge0$, $I\ge0$, $H(X)\le\log|\mathcal X|$, and "conditioning reduces entropy" (pp. 25–28). Conditioning helps only on average: a particular observation can raise uncertainty (p. 28).
- **Convexity results.** $D(p\|q)$ is convex in the pair $(p,q)$; $H(p)$ is concave in $p$; $I(X;Y)$ is concave in $p(x)$ and convex in $p(y|x)$ (pp. 30–31). These matter later for optimisation (e.g. maximising over input distributions).
- **Data processing inequality.** If $X\to Y\to Z$ is a Markov chain, then $I(X;Y)\ge I(X;Z)$: no processing of $Y$ can add information about $X$ (p. 32).
- **Second law of thermodynamics for Markov chains.** Entropy need not increase, but relative entropy between two state distributions always decreases; $H(X_n|X_1)$ increases for stationary chains (pp. 33–36).
- **Sufficient statistics = equality in data processing.** $T(X)$ is sufficient for $\theta$ iff $I(\theta;X)=I(\theta;T(X))$ (pp. 36–37).
- **Fano's inequality.** $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$: if $X$ is still uncertain given $Y$, every estimator of $X$ must make errors (pp. 38–40).

## L3 — Walkthrough

### Introduction (p. 12)
The authors say the concept of information is too broad for one definition. For any probability distribution they define entropy; mutual information extends it to two variables; entropy then becomes the "self-information" of a variable; and mutual information is a special case of relative entropy. They promise that the real test of these definitions comes later, when each shows up as the answer to a question in communication, statistics, complexity or gambling (p. 12).

### 2.1 Entropy (pp. 12–15)
Let $X$ be a discrete random variable with alphabet $\mathcal X$ and probability mass function $p(x)=\Pr\{X=x\}$ (p. 13).

**Definition (entropy, 2.1).**
$$H(X)=-\sum_{x\in\mathcal X}p(x)\log p(x).$$
- The log is base 2, so entropy is in bits; a fair coin has 1 bit. With base $b$ we write $H_b(X)$; with base $e$ the unit is the *nat* (p. 13).
- Convention $0\log0=0$, justified by continuity because $x\log x\to0$ as $x\to0$. So adding zero-probability outcomes does not change $H$ (p. 13).
- $H$ is a functional of the distribution only; the actual values of $X$ do not matter (p. 13).

**Expectation form (2.2, 2.3).** With $E_p g(X)=\sum_x g(x)p(x)$, entropy is the expectation of $\log\frac1{p(X)}$:
$$H(X)=E_p\log\frac1{p(X)}.$$
The authors note the link to thermodynamic entropy and that an axiomatic derivation exists (Problem 4), but they will instead show entropy arises as the answer to natural questions such as the average length of the shortest description (pp. 13–14).

**Lemma 2.1.1.** $H(X)\ge0$. *Proof.* $0\le p(x)\le1$ implies $\log(1/p(x))\ge0$ (p. 14).

**Lemma 2.1.2.** $H_b(X)=(\log_b a)H_a(X)$. *Proof.* $\log_b p=\log_b a\,\log_a p$ (p. 14). So changing base only multiplies entropy by a constant.

**Example 2.1.1 (binary entropy).** $X=1$ w.p. $p$, $0$ w.p. $1-p$:
$$H(X)=-p\log p-(1-p)\log(1-p)\stackrel{\text{def}}{=}H(p).$$
$H=1$ bit at $p=1/2$, and $H=0$ at $p=0$ or $1$ (no randomness, no uncertainty). The graph (Figure 2.1) shows $H(p)$ is concave, with its maximum at $p=1/2$ (p. 14).

**Example 2.1.2.** $X=a,b,c,d$ with probabilities $1/2,1/4,1/8,1/8$:
$$H(X)=-\tfrac12\log\tfrac12-\tfrac14\log\tfrac14-\tfrac18\log\tfrac18-\tfrac18\log\tfrac18=\tfrac74\text{ bits}.$$
To find $X$ by yes/no questions, ask "Is $X=a$?", then "Is $X=b$?", then "Is $X=c$?". The expected number of questions is $1.75$ (check (added step): $\tfrac12\cdot1+\tfrac14\cdot2+\tfrac18\cdot3+\tfrac18\cdot3=1.75$), which equals $H(X)$. The authors say this is the minimum, and that Chapter 5 shows the minimum expected number lies between $H(X)$ and $H(X)+1$ (p. 15).

> **Intuition note.** Entropy is the average surprise of a source. A source whose outcomes are very unequal in probability is easier to guess, so it has lower entropy; here the answer "a" resolves half the uncertainty with one question.

### 2.2 Joint entropy and conditional entropy (pp. 15–17)
A pair $(X,Y)$ can be treated as one vector-valued variable, so nothing new is needed (p. 15).

**Definition (joint entropy, 2.8, 2.9).**
$$H(X,Y)=-\sum_{x}\sum_{y}p(x,y)\log p(x,y)=-E\log p(X,Y).$$

**Definition (conditional entropy, 2.10–2.13).** If $(X,Y)\sim p(x,y)$, $H(Y|X)$ is the average, over $x$, of the entropy of the conditional distribution (p. 16):
$$H(Y|X)=\sum_x p(x)H(Y|X=x)=-\sum_x p(x)\sum_y p(y|x)\log p(y|x)=-\sum_{x,y}p(x,y)\log p(y|x)=-E\log p(Y|X).$$

**Theorem 2.2.1 (chain rule).** $H(X,Y)=H(X)+H(Y|X)$ (2.14).

*Proof* (p. 16).
$$\begin{aligned}H(X,Y)&=-\sum_{x,y}p(x,y)\log p(x,y)\\&=-\sum_{x,y}p(x,y)\log\big[p(x)p(y|x)\big]\\&=-\sum_{x,y}p(x,y)\log p(x)-\sum_{x,y}p(x,y)\log p(y|x)\\&=-\sum_x p(x)\log p(x)-\sum_{x,y}p(x,y)\log p(y|x)\\&=H(X)+H(Y|X).\end{aligned}$$
(The fourth line uses $\sum_y p(x,y)=p(x)$; the author leaves this implicit.) Equivalently, take expectations of $\log p(X,Y)=\log p(X)+\log p(Y|X)$ (p. 16).

**Corollary (2.21).** $H(X,Y|Z)=H(X|Z)+H(Y|X,Z)$; the proof follows the same lines (p. 17).

**Example 2.2.1.** Joint distribution of $(X,Y)$, with columns $X=1..4$ (p. 17):

| | X=1 | X=2 | X=3 | X=4 |
|---|---|---|---|---|
| Y=1 | 1/8 | 1/16 | 1/32 | 1/32 |
| Y=2 | 1/16 | 1/8 | 1/32 | 1/32 |
| Y=3 | 1/16 | 1/16 | 1/16 | 1/16 |
| Y=4 | 1/4 | 0 | 0 | 0 |

Marginal of $X$ is $(\tfrac12,\tfrac14,\tfrac18,\tfrac18)$, marginal of $Y$ is $(\tfrac14,\tfrac14,\tfrac14,\tfrac14)$, so $H(X)=7/4$ bits and $H(Y)=2$ bits. Then
$$H(X|Y)=\sum_{i=1}^4 p(Y=i)H(X|Y=i)=\tfrac14\cdot\tfrac74+\tfrac14\cdot\tfrac74+\tfrac14\cdot2+\tfrac14\cdot0=\tfrac{11}8\text{ bits}.$$
Similarly $H(Y|X)=13/8$ bits and $H(X,Y)=27/8$ bits (p. 17). (Added step: $H(X)+H(Y|X)=\tfrac74+\tfrac{13}8=\tfrac{27}8$, consistent with the chain rule.)

**Remark (p. 17).** $H(Y|X)\ne H(X|Y)$ in general, but $H(X)-H(X|Y)=H(Y)-H(Y|X)$; the authors say they will use this later.

> **Intuition note.** The chain rule says uncertainty about a pair is "uncertainty about the first, plus what is left about the second once the first is known." Order does not matter for the total, only for how the pieces are split.

### 2.3 Relative entropy and mutual information (pp. 18–19)
Entropy is the average amount of information needed to describe a variable. Relative entropy measures the inefficiency of assuming the distribution is $q$ when it is really $p$: knowing $p$ we could build a code of average length $H(p)$; using the code for $q$ costs $H(p)+D(p\|q)$ bits (p. 18).

**Definition (relative entropy, or Kullback–Leibler distance; 2.26, 2.27).**
$$D(p\|q)=\sum_{x}p(x)\log\frac{p(x)}{q(x)}=E_p\log\frac{p(X)}{q(X)}.$$
Conventions from continuity: $0\log\frac0q=0$ and $p\log\frac p0=\infty$ (p. 18). The authors announce that $D\ge0$ with equality iff $p=q$, but note that $D$ is not a true distance: it is not symmetric and does not satisfy the triangle inequality (p. 18).

**Definition (mutual information, 2.28–2.30).**
$$I(X;Y)=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}=D\big(p(x,y)\,\|\,p(x)p(y)\big)=E_{p(x,y)}\log\frac{p(X,Y)}{p(X)p(Y)}.$$
It is the reduction in uncertainty of one variable due to knowing the other (pp. 18–19).

**Example 2.3.1.** On $\mathcal X=\{0,1\}$ let $p(0)=1-r,\ p(1)=r$ and $q(0)=1-s,\ q(1)=s$. Then
$$D(p\|q)=(1-r)\log\frac{1-r}{1-s}+r\log\frac rs,\qquad D(q\|p)=(1-s)\log\frac{1-s}{1-r}+s\log\frac sr.$$
If $r=s$ both are 0. For $r=1/2,\ s=1/4$:
$$D(p\|q)=\tfrac12\log\tfrac{1/2}{3/4}+\tfrac12\log\tfrac{1/2}{1/4}=1-\tfrac12\log3=0.2075\text{ bits},$$
$$D(q\|p)=\tfrac34\log\tfrac{3/4}{1/2}+\tfrac14\log\tfrac{1/4}{1/2}=\tfrac34\log3-1=0.1887\text{ bits}.$$
So $D(p\|q)\ne D(q\|p)$ in general (p. 19).

> **Intuition note.** $D(p\|q)$ is the expected extra bits you pay for believing $q$ while nature follows $p$. Which belief is wrong matters, so the two directions differ. Mutual information asks: how far is the true joint from a world where $X$ and $Y$ were independent?

### 2.4 Relationship between entropy and mutual information (pp. 19–21)
Starting from the definition (p. 19):
$$\begin{aligned}I(X;Y)&=\sum_{x,y}p(x,y)\log\frac{p(x,y)}{p(x)p(y)}=\sum_{x,y}p(x,y)\log\frac{p(x|y)}{p(x)}\\&=-\sum_{x,y}p(x,y)\log p(x)+\sum_{x,y}p(x,y)\log p(x|y)\\&=-\sum_xp(x)\log p(x)-\Big(-\sum_{x,y}p(x,y)\log p(x|y)\Big)=H(X)-H(X|Y).\end{aligned}$$
So $I(X;Y)$ is the reduction in uncertainty of $X$ due to knowledge of $Y$ (pp. 19–20). By symmetry $I(X;Y)=H(Y)-H(Y|X)$ (2.40): "$X$ says as much about $Y$ as $Y$ says about $X$" (p. 20). With the chain rule, $I(X;Y)=H(X)+H(Y)-H(X,Y)$ (2.41). Finally $I(X;X)=H(X)-H(X|X)=H(X)$ (2.42), which is why entropy is sometimes called *self-information* (p. 20).

**Theorem 2.4.1 (mutual information and entropy; pp. 20).**
$$I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)=H(X)+H(Y)-H(X,Y),\quad I(X;Y)=I(Y;X),\quad I(X;X)=H(X).$$
A Venn diagram (Figure 2.2) shows $H(X)$ and $H(Y)$ as two overlapping circles: the overlap is $I(X;Y)$, the non-overlapping parts are $H(X|Y)$ and $H(Y|X)$, and the union is $H(X,Y)$ (pp. 20–21).

**Example 2.4.1.** For the distribution of Example 2.2.1, $I(X;Y)=H(X)-H(X|Y)=\tfrac74-\tfrac{11}8=0.375$ bits $=H(Y)-H(Y|X)=2-\tfrac{13}8$ (p. 21).

> **Intuition note.** Mutual information is the "shared part" of two uncertainties. It is symmetric even though "how much $Y$ tells about $X$" sounds directional.

### 2.5 Chain rules for entropy, relative entropy and mutual information (pp. 21–23)
**Theorem 2.5.1 (chain rule for entropy).** If $X_1,\dots,X_n\sim p(x_1,\dots,x_n)$,
$$H(X_1,\dots,X_n)=\sum_{i=1}^nH(X_i|X_{i-1},\dots,X_1).\quad(2.48)$$
*Proof.* Apply the two-variable rule repeatedly: $H(X_1,X_2)=H(X_1)+H(X_2|X_1)$; $H(X_1,X_2,X_3)=H(X_1)+H(X_2,X_3|X_1)=H(X_1)+H(X_2|X_1)+H(X_3|X_2,X_1)$; and so on up to $n$ (p. 21).

*Alternative proof* (pp. 21–22). Write $p(x_1,\dots,x_n)=\prod_{i=1}^np(x_i|x_{i-1},\dots,x_1)$. Then
$$H(X_1,\dots,X_n)=-\sum p(x_1,\dots,x_n)\log\prod_i p(x_i|x_{i-1},\dots,x_1)=-\sum_{i=1}^n\sum_{x_1,\dots,x_n}p(x_1,\dots,x_n)\log p(x_i|x_{i-1},\dots,x_1).$$
For each $i$ the inner sum can be reduced to the marginal over $x_1,\dots,x_i$ (the later variables sum out), giving $-\sum_{x_1..x_i}p(x_1,\dots,x_i)\log p(x_i|x_{i-1},\dots,x_1)=H(X_i|X_{i-1},\dots,X_1)$.

**Definition (conditional mutual information, 2.60, 2.61).** The reduction in uncertainty of $X$ due to $Y$ when $Z$ is given:
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=E_{p(x,y,z)}\log\frac{p(X,Y|Z)}{p(X|Z)p(Y|Z)}.$$

**Theorem 2.5.2 (chain rule for information).**
$$I(X_1,\dots,X_n;Y)=\sum_{i=1}^nI(X_i;Y|X_{i-1},\dots,X_1).\quad(2.62)$$
*Proof.* $I(X_1..X_n;Y)=H(X_1..X_n)-H(X_1..X_n|Y)=\sum_iH(X_i|X_{i-1}..X_1)-\sum_iH(X_i|X_{i-1}..X_1,Y)=\sum_iI(X_i;Y|X_1..X_{i-1})$ (p. 22).

**Definition (conditional relative entropy, 2.65, 2.66).** The average, over $p(x)$, of the relative entropies between the conditionals:
$$D\big(p(y|x)\|q(y|x)\big)=\sum_xp(x)\sum_yp(y|x)\log\frac{p(y|x)}{q(y|x)}=E_{p(x,y)}\log\frac{p(Y|X)}{q(Y|X)}.$$
The notation omits the distribution $p(x)$ of the conditioning variable; it is understood from context (p. 23).

**Theorem 2.5.3 (chain rule for relative entropy).**
$$D\big(p(x,y)\|q(x,y)\big)=D\big(p(x)\|q(x)\big)+D\big(p(y|x)\|q(y|x)\big).\quad(2.67)$$
*Proof* (p. 23).
$$D(p(x,y)\|q(x,y))=\sum_{x,y}p(x,y)\log\frac{p(x)p(y|x)}{q(x)q(y|x)}=\sum_{x,y}p(x,y)\log\frac{p(x)}{q(x)}+\sum_{x,y}p(x,y)\log\frac{p(y|x)}{q(y|x)}.$$
The authors say this chain rule is used in Section 2.9 to prove a version of the second law (p. 23).

> **Intuition note.** All three chain rules say the same thing: a joint quantity is the sum of "first part" plus "second part given the first."

### 2.6 Jensen's inequality and its consequences (pp. 23–28)
**Definitions (p. 23).** $f$ is *convex* on $(a,b)$ if for all $x_1,x_2\in(a,b)$ and $0\le\lambda\le1$:
$$f(\lambda x_1+(1-\lambda)x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2).\quad(2.72)$$
It is *strictly convex* if equality holds only for $\lambda=0$ or $1$. $f$ is *concave* if $-f$ is convex. A convex function lies below every chord; a concave one lies above (p. 23). Convex examples: $x^2,|x|,e^x,x\log x$ ($x\ge0$). Concave: $\log x$, $\sqrt x$ ($x\ge0$). Linear functions are both (p. 24).

**Theorem 2.6.1.** If $f''\ge0$ everywhere ($>0$ for strict), then $f$ is convex (strictly convex).
*Proof* (pp. 24–25). Taylor expansion about $x_0$: $f(x)=f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x^*)}2(x-x_0)^2$ with $x^*$ between $x_0$ and $x$. Since $f''(x^*)\ge0$, the last term is non-negative, so $f(x)\ge f(x_0)+f'(x_0)(x-x_0)$. Put $x_0=\lambda x_1+(1-\lambda)x_2$:
$$f(x_1)\ge f(x_0)+f'(x_0)[(1-\lambda)(x_1-x_2)],\qquad f(x_2)\ge f(x_0)+f'(x_0)[\lambda(x_2-x_1)].$$
Multiply the first by $\lambda$, the second by $1-\lambda$, and add: the derivative terms cancel (added step), leaving (2.72). The strict case is similar (p. 25). Consequence: $x^2$, $e^x$, $x\log x$ are strictly convex and $\log x$, $\sqrt x$ strictly concave (p. 25).

**Theorem 2.6.2 (Jensen's inequality).** If $f$ is convex and $X$ is a random variable, $Ef(X)\ge f(EX)$ (2.76). If $f$ is strictly convex, equality forces $X=EX$ with probability 1 (p. 25).
*Proof* (discrete case, induction on the number of mass points; pp. 25–26). For two mass points it is the definition of convexity (2.77). Assume it holds for $k-1$ points; set $p'_i=p_i/(1-p_k)$ for $i<k$. Then
$$\sum_{i=1}^kp_if(x_i)=p_kf(x_k)+(1-p_k)\sum_{i=1}^{k-1}p'_if(x_i)\ \ge\ p_kf(x_k)+(1-p_k)f\Big(\sum_{i=1}^{k-1}p'_ix_i\Big)\ \ge\ f\Big(p_kx_k+(1-p_k)\sum_{i=1}^{k-1}p'_ix_i\Big)=f\Big(\sum_{i=1}^kp_ix_i\Big).$$
The first inequality is the induction hypothesis and the second is convexity. Continuous distributions follow by continuity arguments; the equality condition is left to the reader (p. 26).

> **Intuition note.** For a convex function, averaging first and then applying $f$ gives a smaller value than applying $f$ first and then averaging. Because $\log$ is concave the inequality flips, and that flip is what produces $D\ge0$.

**Theorem 2.6.3 (information inequality).** For pmfs $p,q$ on $\mathcal X$: $D(p\|q)\ge0$ (2.82), with equality iff $p(x)=q(x)$ for all $x$ (2.83) (p. 26).
*Proof.* Let $A=\{x:p(x)>0\}$.
$$-D(p\|q)=\sum_{x\in A}p(x)\log\frac{q(x)}{p(x)}\ \le\ \log\sum_{x\in A}p(x)\frac{q(x)}{p(x)}=\log\sum_{x\in A}q(x)\ \le\ \log\sum_{x\in\mathcal X}q(x)=\log1=0.$$
The first inequality is Jensen for the strictly concave $\log$. Equality in it holds iff $q(x)/p(x)=1$ everywhere on $A$, i.e. $p=q$ (p. 26).

**Corollaries (p. 27).**
- *Non-negativity of mutual information* (2.91): $I(X;Y)=D(p(x,y)\|p(x)p(y))\ge0$, with equality iff $X$ and $Y$ are independent.
- $D(p(y|x)\|q(y|x))\ge0$ (2.92), with equality iff $p(y|x)=q(y|x)$ for all $y$ and all $x$ with $p(x)>0$.
- $I(X;Y|Z)\ge0$ (2.93), with equality iff $X$ and $Y$ are conditionally independent given $Z$.

**Theorem 2.6.4.** $H(X)\le\log|\mathcal X|$, with equality iff $X$ is uniform on $\mathcal X$ (p. 27).
*Proof.* Let $u(x)=1/|\mathcal X|$. Then $D(p\|u)=\sum p(x)\log\frac{p(x)}{u(x)}=\log|\mathcal X|-H(X)\ge0$ (2.94, 2.95). So the uniform distribution has maximum entropy over a given range (p. 27).

**Theorem 2.6.5 (conditioning reduces entropy).** $H(X|Y)\le H(X)$, with equality iff $X,Y$ independent (p. 27).
*Proof.* $0\le I(X;Y)=H(X)-H(X|Y)$ (p. 28).
This holds only *on average*: $H(X|Y=y)$ may be larger, smaller or equal to $H(X)$, while $H(X|Y)=\sum_yp(y)H(X|Y=y)\le H(X)$. The authors' picture: a specific new piece of evidence in a court case may raise uncertainty, but on average evidence reduces it (p. 28).

**Example 2.6.1 (p. 28).** Joint pmf: $p(X{=}1,Y{=}1)=0$, $p(X{=}2,Y{=}1)=3/4$, $p(X{=}1,Y{=}2)=1/8$, $p(X{=}2,Y{=}2)=1/8$. Then $H(X)=H(\tfrac18,\tfrac78)=0.544$ bits, $H(X|Y=1)=0$, $H(X|Y=2)=1$ bit, and
$$H(X|Y)=\tfrac34H(X|Y=1)+\tfrac14H(X|Y=2)=0.25\text{ bits}.$$
Observing $Y=2$ increases the uncertainty in $X$, observing $Y=1$ decreases it, and on average it decreases.

**Theorem 2.6.6 (independence bound on entropy).** $H(X_1,\dots,X_n)\le\sum_iH(X_i)$ with equality iff the $X_i$ are independent (2.97).
*Proof.* By the chain rule, $H(X_1..X_n)=\sum_iH(X_i|X_{i-1}..X_1)\le\sum_iH(X_i)$ by Theorem 2.6.5. Equality iff each $X_i$ is independent of $X_{i-1},\dots,X_1$, i.e. iff all are independent (p. 28).

> **Intuition note.** Knowing something can never hurt on average, and the best you can do for a variable with $m$ outcomes is to make them all equally likely.

### 2.7 The log sum inequality and its applications (pp. 29–31)
**Theorem 2.7.1 (log sum inequality).** For non-negative $a_1..a_n$ and $b_1..b_n$:
$$\sum_{i=1}^na_i\log\frac{a_i}{b_i}\ \ge\ \Big(\sum_{i=1}^na_i\Big)\log\frac{\sum a_i}{\sum b_i}\quad(2.100)$$
with equality iff $a_i/b_i$ is constant. Conventions: $0\log0=0$, $a\log\frac a0=\infty$ for $a>0$, $0\log\frac00=0$ (p. 29).
*Proof* (p. 29). Assume all $a_i,b_i>0$. $f(t)=t\log t$ is strictly convex since $f''(t)=\frac1t\log e>0$. Jensen gives $\sum\alpha_if(t_i)\ge f(\sum\alpha_it_i)$ for $\alpha_i\ge0$, $\sum\alpha_i=1$. Set $\alpha_i=b_i/\sum_jb_j$ and $t_i=a_i/b_i$:
$$\sum_i\frac{a_i}{\sum_jb_j}\log\frac{a_i}{b_i}\ \ge\ \Big(\sum_i\frac{a_i}{\sum_jb_j}\Big)\log\Big(\sum_i\frac{a_i}{\sum_jb_j}\Big).$$
Multiplying by $\sum_jb_j$ gives (2.100) (added step).

**Re-proof of $D\ge0$** (p. 29). Take $a_i=p(x)$, $b_i=q(x)$: $D(p\|q)\ge(\sum p)\log\frac{\sum p}{\sum q}=1\cdot\log\frac11=0$, with equality iff $p(x)/q(x)=c$; since both sum to 1, $c=1$.

**Theorem 2.7.2.** $D(p\|q)$ is convex in the pair $(p,q)$: for pairs $(p_1,q_1),(p_2,q_2)$ and $0\le\lambda\le1$,
$$D(\lambda p_1+(1-\lambda)p_2\,\|\,\lambda q_1+(1-\lambda)q_2)\le\lambda D(p_1\|q_1)+(1-\lambda)D(p_2\|q_2).\quad(2.106)$$
*Proof.* Apply the log sum inequality with $a_1=\lambda p_1(x),a_2=(1-\lambda)p_2(x),b_1=\lambda q_1(x),b_2=(1-\lambda)q_2(x)$ to each term, then sum over $x$ (p. 30).

**Theorem 2.7.3 (concavity of entropy).** $H(p)$ is concave in $p$.
*Proof.* $H(p)=\log|\mathcal X|-D(p\|u)$ (2.108) and $D$ is convex (p. 30). *Alternative proof* (p. 30): let $X_1\sim p_1,X_2\sim p_2$ on the same set and $\theta=1$ w.p. $\lambda$, $2$ w.p. $1-\lambda$; let $Z=X_\theta$, so $Z\sim\lambda p_1+(1-\lambda)p_2$. Conditioning reduces entropy, so $H(Z)\ge H(Z|\theta)$, i.e. $H(\lambda p_1+(1-\lambda)p_2)\ge\lambda H(p_1)+(1-\lambda)H(p_2)$.
The authors note a physical reading: mixing two gases of equal entropy gives a gas of higher entropy (p. 31).

**Theorem 2.7.4.** For $(X,Y)\sim p(x)p(y|x)$, $I(X;Y)$ is a concave function of $p(x)$ for fixed $p(y|x)$ and a convex function of $p(y|x)$ for fixed $p(x)$ (p. 31).
*Proof* (p. 31). (i) $I(X;Y)=H(Y)-\sum_xp(x)H(Y|X=x)$. For fixed $p(y|x)$, $p(y)$ is linear in $p(x)$, so $H(Y)$ is concave in $p(x)$; the second term is linear in $p(x)$; a concave minus a linear function is concave. (ii) Fix $p(x)$; mix two conditionals $p_\lambda(y|x)=\lambda p_1(y|x)+(1-\lambda)p_2(y|x)$. The joint $p_\lambda(x,y)=\lambda p_1(x,y)+(1-\lambda)p_2(x,y)$ and $p_\lambda(y)=\lambda p_1(y)+(1-\lambda)p_2(y)$ are mixtures, so the product of marginals $q_\lambda(x,y)=p(x)p_\lambda(y)=\lambda q_1+(1-\lambda)q_2$ is a mixture too. Since $I(X;Y)=D(p_\lambda\|q_\lambda)$ and $D$ is jointly convex, $I$ is convex in $p(y|x)$.

> **Intuition note.** Entropy is "dome-shaped" (concave), relative entropy "bowl-shaped" (convex). Later, the first fact lets us find the input distribution that maximises information, and the second helps minimise it over channels or codes. (The authors say only that these results are consequences of convexity; the later use is our remark.)

### 2.8 Data processing inequality (pp. 32–33)
**Definition (Markov chain).** $X\to Y\to Z$ if $p(x,y,z)=p(x)p(y|x)p(z|y)$ (2.118) (p. 32).
Consequences (p. 32):
- $X\to Y\to Z$ iff $X$ and $Z$ are conditionally independent given $Y$, because $p(x,z|y)=\frac{p(x,y,z)}{p(y)}=\frac{p(x,y)p(z|y)}{p(y)}=p(x|y)p(z|y)$ (2.119).
- $X\to Y\to Z$ implies $Z\to Y\to X$, so one writes $X\leftrightarrow Y\leftrightarrow Z$.
- If $Z=f(Y)$ then $X\to Y\to Z$.
The authors remark that this characterisation extends to Markov fields: $n$-dimensional processes in which interior and exterior are independent given the boundary (p. 32).

**Theorem 2.8.1 (data processing inequality).** If $X\to Y\to Z$ then $I(X;Y)\ge I(X;Z)$ (p. 32).
*Proof* (pp. 32–33). Expand $I(X;Y,Z)$ by the chain rule in two ways:
$$I(X;Y,Z)=I(X;Z)+I(X;Y|Z)\ \ (2.120),\qquad I(X;Y,Z)=I(X;Y)+I(X;Z|Y)\ \ (2.121).$$
(The printed (2.121) repeats the right side of (2.120); the line above is the corrected version, an added step. See Reading notes.) Since $X,Z$ are conditionally independent given $Y$, $I(X;Z|Y)=0$. Since $I(X;Y|Z)\ge0$,
$$I(X;Y)\ge I(X;Z).\quad(2.122)$$
Equality iff $I(X;Y|Z)=0$, i.e. iff $X\to Z\to Y$ is a Markov chain. Likewise $I(Y;Z)\ge I(X;Z)$ (p. 33).

**Corollaries (p. 33).**
- If $Z=g(Y)$: $I(X;Y)\ge I(X;g(Y))$, because $X\to Y\to g(Y)$ is a Markov chain. "Functions of the data $Y$ cannot increase the information about $X$."
- If $X\to Y\to Z$: $I(X;Y|Z)\le I(X;Y)$ (2.123), using $I(X;Z|Y)=0$ and $I(X;Z)\ge0$ in the two expansions. So the dependence of $X$ and $Y$ can only decrease on observing a "downstream" $Z$.

**Warning example (p. 33).** Without the Markov property, $I(X;Y|Z)>I(X;Y)$ is possible. Let $X,Y$ be independent fair bits and $Z=X+Y$. Then $I(X;Y)=0$, but
$$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)=H(X|Z)=\Pr(Z=1)H(X|Z=1)=\tfrac12\text{ bit}.$$
(Added step: $Z=0$ or $2$ fixes $X$, so only $Z=1$, probability $1/2$, leaves one bit of uncertainty.)

> **Intuition note.** If $Z$ is made from $Y$ alone, $Z$ can only know what $Y$ knew. Any computation, compression or noise applied to $Y$ is a one-way valve for information about $X$.

### 2.9 The second law of thermodynamics (pp. 33–36)
The second law says the entropy of an isolated system is non-decreasing. In statistical thermodynamics entropy is often the log of the number of microstates, which equals our entropy if all states are equally likely (p. 33). The authors model the isolated system as a Markov chain with transitions obeying the physical laws: the present state determines the future independently of the past (p. 33). In such a system there are several readings of the second law. "It may come as a shock to find that the entropy does not always increase," but relative entropy always decreases (pp. 33–34).

**1. Relative entropy $D(\mu_n\|\mu'_n)$ decreases with $n$** (p. 34). Let $\mu_n,\mu'_n$ be two state distributions at time $n$ and $\mu_{n+1},\mu'_{n+1}$ those at time $n+1$. Define joint pmfs $p(x_n,x_{n+1})=p(x_n)r(x_{n+1}|x_n)$ and $q(x_n,x_{n+1})=q(x_n)r(x_{n+1}|x_n)$, with the same transition function $r$. The chain rule for relative entropy gives two expansions:
$$D(p(x_n,x_{n+1})\|q(x_n,x_{n+1}))=D(p(x_n)\|q(x_n))+D(p(x_{n+1}|x_n)\|q(x_{n+1}|x_n))=D(p(x_{n+1})\|q(x_{n+1}))+D(p(x_n|x_{n+1})\|q(x_n|x_{n+1})).$$
Both conditionals $p(x_{n+1}|x_n)$ and $q(x_{n+1}|x_n)$ equal $r(\cdot|\cdot)$, so the second term in the first line is 0. The last term is $\ge0$ by the corollary to Theorem 2.6.3. Hence
$$D(\mu_n\|\mu'_n)\ge D(\mu_{n+1}\|\mu'_{n+1}).\quad(2.124,\,2.125)$$
Example from the text: if the tax system for wealth redistribution is the same in Canada and England, the relative entropy "distance" between the two wealth distributions decreases, so they become more similar (p. 34).

**2. Relative entropy to a stationary distribution decreases** (pp. 34–35). If $\mu'_n=\mu$ is stationary then $\mu'_{n+1}=\mu$, so $D(\mu_n\|\mu)\ge D(\mu_{n+1}\|\mu)$ (2.126). The sequence is non-increasing and non-negative, so it has a limit; the limit is 0 if the stationary distribution is unique, "but this is more difficult to prove" (p. 35).

**3. Entropy increases if the stationary distribution is uniform** (p. 35). Decreasing relative entropy does not in general imply increasing entropy. Counterexample: any chain with a non-uniform stationary distribution, started from the uniform distribution (already maximum entropy), moves toward a lower-entropy stationary distribution, so entropy falls. If the stationary distribution *is* uniform,
$$D(\mu_n\|\mu)=\log|\mathcal X|-H(\mu_n)=\log|\mathcal X|-H(X_n)\quad(2.127)$$
(added step: this is (2.94) with $u=\mu$), so the monotone decrease of $D$ is a monotone increase of $H(X_n)$. This ties most closely to statistical thermodynamics, where all microstates are equally likely.
*Definition (doubly stochastic matrix; 2.128, 2.129).* $[P_{ij}]$, $P_{ij}=\Pr\{X_{n+1}=j|X_n=i\}$, is doubly stochastic if $\sum_iP_{ij}=1$ for every $j$ and $\sum_jP_{ij}=1$ for every $i$. *Remark.* The uniform distribution is stationary for $P$ iff $P$ is doubly stochastic (see Problem 1 of Chapter 4, cited on p. 35).

**4. $H(X_n|X_1)$ increases with $n$ for a stationary Markov process** (pp. 35–36). For a stationary process $H(X_n)$ is constant, so entropy is non-increasing, but the conditional uncertainty of the future grows. Proof 1:
$$H(X_n|X_1)\ge H(X_n|X_1,X_2)=H(X_n|X_2)=H(X_{n-1}|X_1)$$
by "conditioning reduces entropy," Markovity, and stationarity (2.130–2.132). Proof 2: apply data processing to the chain $X_1\to X_{n-1}\to X_n$: $I(X_1;X_{n-1})\ge I(X_1;X_n)$ (2.133). Expanding, $H(X_{n-1})-H(X_{n-1}|X_1)\ge H(X_n)-H(X_n|X_1)$ (2.134), and since $H(X_{n-1})=H(X_n)$ by stationarity, $H(X_{n-1}|X_1)\le H(X_n|X_1)$ (2.135). The same techniques show that $H(X_0|X_n)$ increases for any Markov chain (Problem 35; p. 36, and summary item 5 on p. 42).

**5. Shuffles increase entropy** (p. 36). If $T$ is a shuffle (permutation) of a deck, $X$ the initial random arrangement, and $T$ independent of $X$, then $H(TX)\ge H(X)$ (2.136). Problem 31 outlines the proof (pp. 36, 48).

> **Intuition note.** Entropy of the state can go either way, but "distance between two descriptions of the system" can only shrink when the same dynamics acts on both. The system forgets where it started, not necessarily how ordered it is.

### 2.10 Sufficient statistics (pp. 36–38)
The section is "a sidelight showing the power of the data processing inequality" (p. 36). Let $\{f_\theta(x)\}$ be a family of pmfs indexed by $\theta$, $X$ a sample from one member, and $T(X)$ any statistic (function of the sample). Then $\theta\to X\to T(X)$ and by data processing
$$I(\theta;T(X))\le I(\theta;X)\quad(2.137)$$
for any distribution on $\theta$; if equality holds, no information is lost (p. 36).

**Definition (sufficient statistic).** $T(X)$ is sufficient relative to $\{f_\theta\}$ if $X$ is independent of $\theta$ given $T(X)$, i.e. $\theta\to T(X)\to X$ is a Markov chain (p. 37). This is the equality condition of data processing, $I(\theta;X)=I(\theta;T(X))$ (2.138) for all distributions on $\theta$: sufficient statistics preserve mutual information, and conversely (p. 37).

**Examples (pp. 37–38).**
1. $X_1..X_n$ i.i.d. coin tosses, $\theta=\Pr(X_i=1)$. $T=\sum X_i$ is sufficient. Given $T=k$, every sequence with $k$ ones is equally likely, regardless of $\theta$:
$$\Pr\Big\{(X_1..X_n)=(x_1..x_n)\ \Big|\ \sum X_i=k\Big\}=\begin{cases}1/\binom nk&\text{if }\sum x_i=k,\\0&\text{otherwise.}\end{cases}\quad(2.139)$$
2. $X_i$ i.i.d. $\mathcal N(\theta,1)$: the sample mean $\bar X_n$ is sufficient; the conditional distribution of the sample given $\bar X_n$ and $n$ does not depend on $\theta$ (p. 37). (The authors say this "can be verified.")
3. $f_\theta=\text{Uniform}(\theta,\theta+1)$: $T=(\max_iX_i,\min_iX_i)$ is sufficient; the proof is "slightly more complicated" (p. 38).

**Definition (minimal sufficient statistic).** $T(X)$ is minimal if it is a function of every other sufficient statistic $U$; in chain form $\theta\to T(X)\to U(X)\to X$ (2.142). So a minimal sufficient statistic maximally compresses the information about $\theta$. For a normal mean, the pair (mean of odd samples, mean of even samples) is sufficient but not minimal. In the three examples above the statistics are also minimal (p. 38).

> **Intuition note.** A sufficient statistic is a lossless summary *for the question about $\theta$*. Data processing says summaries can only lose information; sufficiency is the case where nothing relevant is lost.

### 2.11 Fano's inequality (pp. 38–40)
Suppose we observe $Y$ and wish to guess a correlated $X$. From the problems at the end of the chapter, $H(X|Y)=0$ iff $X$ is a function of $Y$, so $X$ can be estimated with zero error iff $H(X|Y)=0$ (p. 38). Fano's inequality makes the converse quantitative. Estimate $\hat X=g(Y)$; then $X\to Y\to\hat X$ is a Markov chain. Define $P_e=\Pr\{\hat X\ne X\}$ (2.143) (pp. 38–39). The authors say the inequality is crucial for proving the converse of Shannon's second theorem (their Chapter 8; p. 38).

**Theorem 2.11.1 (Fano's inequality).**
$$H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y).\quad(2.144)$$
Weakened forms: $1+P_e\log|\mathcal X|\ge H(X|Y)$ (2.145), or
$$P_e\ge\frac{H(X|Y)-1}{\log|\mathcal X|}.\quad(2.146)$$
(Added step: (2.145) follows from (2.144) using $H(P_e)\le1$ and $\log(|\mathcal X|-1)\le\log|\mathcal X|$.) Remark: $P_e=0$ implies $H(X|Y)=0$ (p. 39).

*Proof* (pp. 39–40). Define $E=1$ if $\hat X\ne X$ and $E=0$ otherwise (2.147). Expand $H(E,X|Y)$ in two ways with the chain rule:
$$H(E,X|Y)=H(X|Y)+H(E|X,Y)=H(E|Y)+H(X|E,Y).$$
- $H(E|X,Y)=0$, because $E$ is a function of $X$ and $g(Y)$.
- $H(E|Y)\le H(E)=H(P_e)$, since conditioning reduces entropy and $E$ is binary with $\Pr(E=1)=P_e$.
- $H(X|E,Y)=\Pr(E{=}0)H(X|Y,E{=}0)+\Pr(E{=}1)H(X|Y,E{=}1)\le(1-P_e)\cdot0+P_e\log(|\mathcal X|-1)$ (2.150, 2.151). Given $E=0$, $X=g(Y)$ is determined. Given $E=1$, $X$ takes one of the remaining outcomes, at most $|\mathcal X|-1$ of them (the text notes it is $|\mathcal X|-1$ if $g(Y)\in\mathcal X$, else $|\mathcal X|$).
Combining: $H(X|Y)=H(E|Y)+H(X|E,Y)-0\le H(P_e)+P_e\log(|\mathcal X|-1)$ (added step: the zero term drops out). $\square$

**Remark: no side information (pp. 40).** Let $X\in\{1,\dots,m\}$ with $p_1\ge p_2\ge\dots\ge p_m$. The best guess is $\hat X=1$, with $P_e=1-p_1$, and Fano becomes $H(P_e)+P_e\log(m-1)\ge H(X)$ (2.152). The pmf
$$(p_1,\dots,p_m)=\Big(1-P_e,\ \tfrac{P_e}{m-1},\dots,\tfrac{P_e}{m-1}\Big)\quad(2.153)$$
achieves equality, so Fano's inequality is sharp. (Added step: its entropy is $H(P_e)+P_e\log(m-1)$ by grouping.)

> **Intuition note.** If, after seeing $Y$, you still have $H(X|Y)$ bits of doubt about $X$, then no guesser can be right every time: a guess wrong with probability $P_e$ "uses up" at most $H(P_e)+P_e\log(|\mathcal X|-1)$ of that doubt, so the doubt forces a minimum error rate.

### Summary of Chapter 2 (pp. 40–42)
The authors collect: properties of $H$ (non-negative, change of base, conditioning reduces entropy, independence bound, $H\le\log|\mathcal X|$, concavity); definitions of $D$ and $I$; the expectation forms of $H,H(X,Y),H(X|Y),I,D$ (2.158–2.162); properties of $D$ and $I$ including $D(p\|u)=\log m-H(p)$ and joint convexity of $D$; the three chain rules; Jensen; log sum (stated for "positive numbers" in the summary, p. 41); data processing; the five second-law statements; sufficient statistics; and Fano (2.164). The summary adds one second-law statement not proved in the text: $H(X_0|X_n)$ increases for any Markov chain (p. 42).

### Problems for Chapter 2 and Historical notes (pp. 42–49; not worked here)
There are 35 problems (pp. 42–49). The ones that connect directly to results above:
- Problem 4: derive $H=-\sum p_i\log p_i$ from normalisation, continuity and grouping axioms (pp. 42–43).
- Problem 5: $H(g(X))\le H(X)$ via $H(X,g(X))$ expanded two ways (p. 43).
- Problem 12: the three-way "mutual information" $I(X;Y;Z)=I(X;Y)-I(X;Y|Z)$ is symmetric but can be negative (p. 45).
- Problem 15: $\rho(X,Y)=H(X|Y)+H(Y|X)$ is a metric on random variables, $=H(X)+H(Y)-2I(X;Y)$ (pp. 45–46).
- Problem 22: a Markov chain that "necks down" to $k$ states has $I(X_1;X_3)\le\log k$ (p. 47).
- Problem 30: maximum entropy of a non-negative integer variable with fixed mean $A$ (p. 48).
- Problem 34: expected relative entropy from empirical to true distribution decreases with sample size (p. 49).

Historical notes (p. 49): entropy began in thermodynamics (Boltzmann's $S=k\ln W$); Hartley in the 1930s proposed essentially the log of the alphabet size; Shannon was first to define entropy and mutual information as here; relative entropy is due to Kullback and Leibler, and is also known as Kullback–Leibler distance, cross entropy, information divergence and information for discrimination; Fano proved his inequality; Fisher defined sufficient statistics, Lehmann and Scheffé minimal ones, and Kullback linked mutual information to sufficiency; the authors cite Brillouin, Jaynes, Bennett and Landauer on information and physics.

## Toy example
*(Ours, not from the text.)* Let $X$ be a fair bit and let $Y$ be $X$ sent through a "flip with probability $1/4$" noise step. The joint pmf is
$$p(0,0)=p(1,1)=\tfrac38,\qquad p(0,1)=p(1,0)=\tfrac18.$$
Both marginals are uniform, so $H(X)=H(Y)=1$ bit.
- Conditional: given $Y=y$, $X$ equals $y$ w.p. $3/4$, so $H(X|Y)=H(\tfrac14)=\tfrac14\cdot2+\tfrac34\log\tfrac43=0.8113$ bits.
- Mutual information (Thm 2.4.1): $I(X;Y)=H(X)-H(X|Y)=1-0.8113=0.1887$ bits.
- Check as relative entropy (2.29): $D(p_{XY}\|p_Xp_Y)=2\cdot\tfrac38\log\frac{3/8}{1/4}+2\cdot\tfrac18\log\frac{1/8}{1/4}=\tfrac34\log\tfrac32-\tfrac14=0.4387-0.25=0.1887$ bits. Same answer.
- **Data processing.** Send $Y$ through a second identical noise step to get $Z$, so $X\to Y\to Z$. $X\ne Z$ exactly when one of the two flips happens: $\Pr=2\cdot\tfrac34\cdot\tfrac14=\tfrac38$. Then $I(X;Z)=1-H(\tfrac38)=1-0.9544=0.0456$ bits $\le0.1887=I(X;Y)$, as Theorem 2.8.1 says.
- **Fano.** Guess $\hat X=Y$: $P_e=\tfrac14$, $|\mathcal X|=2$, so $\log(|\mathcal X|-1)=0$ and Fano reads $H(\tfrac14)\ge H(X|Y)$, i.e. $0.8113\ge0.8113$. It holds with equality (the binary case is sharp, as in Remark (2.153) with $m=2$).

## Concepts
The canon's concept spine has no explicit ids; ids below are kebab-case forms of the spine names. `(new)` = not in the spine.
- [[bit]] — unit of entropy when the log is base 2; a fair coin toss is 1 bit; base $e$ gives nats (p. 13)
- [[entropy]] — $H(X)=-\sum p(x)\log p(x)=E\log\frac1{p(X)}$, uncertainty of $X$; depends only on probabilities (pp. 13–14)
- [[self-information-surprisal]] — here "self-information" is used for the *average* quantity $H(X)=I(X;X)$, not for the single-outcome $-\log p(x)$; the per-outcome term $\log\frac1{p(x)}$ appears only inside the expectation (pp. 13, 20)
- [[joint-and-conditional-entropy]] — $H(X,Y)$ for a pair; $H(Y|X)=\sum_xp(x)H(Y|X=x)$, the average residual uncertainty (pp. 15–16)
- [[chain-rule]] — $H(X,Y)=H(X)+H(Y|X)$ and its $n$-variable, mutual-information and relative-entropy versions (pp. 16, 21–23)
- [[mutual-information]] — $I(X;Y)=D(p(x,y)\|p(x)p(y))=H(X)-H(X|Y)$; symmetric, $\ge0$, zero iff independent (pp. 18–20, 27)
- [[relative-entropy-kl-divergence]] — $D(p\|q)=E_p\log\frac{p(X)}{q(X)}$; $\ge0$, zero iff $p=q$, not symmetric, no triangle inequality, jointly convex; cost of coding $p$ with $q$'s code is $H(p)+D(p\|q)$ (pp. 18, 26, 30)
- [[data-processing-inequality]] — if $X\to Y\to Z$ then $I(X;Y)\ge I(X;Z)$ (p. 32)
- [[fanos-inequality]] — $H(P_e)+P_e\log(|\mathcal X|-1)\ge H(X|Y)$ (p. 39)
- [[maximum-entropy-principle]] — only in the narrow form of Theorem 2.6.4: the uniform pmf maximises entropy over a given range; the general constrained principle is left to Problem 30 (pp. 27, 48)
- [[conditional-mutual-information]] (new) — $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)\ge0$ (p. 22)
- [[conditional-relative-entropy]] (new) — $D(p(y|x)\|q(y|x))$ averaged over $p(x)$ (p. 22)
- [[conditioning-reduces-entropy]] (new) — $H(X|Y)\le H(X)$ on average, though a single observation can raise uncertainty (pp. 27–28)
- [[jensen-inequality]] (new) — $Ef(X)\ge f(EX)$ for convex $f$ (p. 25)
- [[log-sum-inequality]] (new) — $\sum a_i\log\frac{a_i}{b_i}\ge(\sum a_i)\log\frac{\sum a_i}{\sum b_i}$ (p. 29)
- [[markov-chain-triple]] (new) — $X\to Y\to Z$: $Z$ depends on $X$ only through $Y$ (p. 32)
- [[sufficient-statistic]] (new) — $T(X)$ with $I(\theta;X)=I(\theta;T(X))$; equivalently $\theta\to T(X)\to X$ (p. 37)
- [[minimal-sufficient-statistic]] (new) — a sufficient statistic that is a function of every other sufficient statistic (p. 38)
- [[second-law-for-markov-chains]] (new) — relative entropy between state distributions decreases; $H(X_n|X_1)$ increases for stationary chains (pp. 33–36)
- [[doubly-stochastic-matrix]] (new) — transition matrix with all row and column sums 1; uniform is stationary iff doubly stochastic (p. 35)

## Canonical instances
Instance ids are kebab-case forms of the canon names.
- [[twenty-questions-binary-search]] — asking "Is $X=a$? … $b$? … $c$?" for the pmf $(1/2,1/4,1/8,1/8)$ takes 1.75 questions on average, which equals $H(X)=7/4$ bits (pp. 14–15)
- [[twelve-ball-weighing-puzzle]] — appears only as an unsolved exercise (Problem 13, 12 coins with 3 weighings on a balance), not as a worked instance (p. 45)

## Bridges (candidates)
- [same-math] cross-entropy $H(p)+D(p\|q)$ ↔ machine learning / LLMs: classifier and language-model training loss — the book's coding cost of using $q$ for data from $p$ (p. 18) is the loss that is minimised when $q$ is the model; minimising it equals minimising $D(p\|q)$
- [same-math] chain rule $H(X_1..X_n)=\sum_iH(X_i|X_{<i})$ ↔ LLMs: autoregressive factorisation — the sum of per-token conditional entropies is the sequence entropy that next-token models are trained to estimate
- [same-math] $I(X;Y)=D(p(x,y)\|p(x)p(y))$ ↔ political science / sociology: Theil-type segregation index — group-vs-unit association measured as distance from independence
- [same-math] data processing inequality ↔ machine learning: information bottleneck and representation learning — each layer or encoding $Z$ of $Y$ cannot carry more about $X$ than $Y$ does; Problem 22's $I(X_1;X_3)\le\log k$ is the bottleneck bound
- [same-math] sufficient statistic as equality in data processing ↔ statistics / Bayesian inference: sufficiency of $T$ — the posterior of $\theta$ depends on the data only through $T$ (ours: needs checking against a statistics text)
- [same-math] Fano's inequality ↔ statistical learning: lower bounds on classification or estimation error from residual conditional entropy
- [structural-analogy] relative entropy decreasing under a common Markov kernel (§2.9, items 1–2) ↔ network science: convergence of random walks and diffusion on networks to a stationary distribution — the same contraction argument, with the assumption that both distributions evolve under the *same* transition rule
- [metaphor] Canada–England wealth distributions "becoming more similar" under the same tax system (p. 34) ↔ economics: convergence of inequality across countries — it is a mathematical statement only if wealth really evolves as a Markov chain with one shared kernel; the book offers it as an interpretation, not a model

## Questions this raises
1. $D(p\|q)$ is not a metric. Which symmetric or metric-like relatives exist, and when does the direction of the divergence matter in practice (e.g. $D(p\|q)$ vs $D(q\|p)$ in Example 2.3.1)?
2. The chapter shows entropy of the *state* may fall under Markov dynamics while relative entropy always falls. What does this say about which "entropy" a physicist or a social scientist should track?
3. If conditioning reduces entropy only on average, how large can the single-observation increase $H(X|Y=y)-H(X)$ be, and does Fano's inequality say anything about worst cases?
4. The chapter promises that these definitions arise as answers to questions in compression, gambling, statistics and communication (pp. 12, 14). Which question does each of $H$, $D$ and $I$ answer in Chapters 3–8?

## Reading notes
- **Edition: this is the 1991 FIRST edition, not the 2006 second edition.** The file is named `cover-2006-elements.pdf`, but PDF p. 1 reads "Copyright © 1991 John Wiley & Sons, Inc. Print ISBN 0-471-06259-6 Online ISBN 0-471-20061-1"; PDF p. 3 is the title page (Cover: Stanford; Thomas: IBM T. J. Watson); PDF p. 4 carries "Copyright © 1991" and "Q360.C68 1991" with no edition statement for a 2nd edition. The canon entry cites the 2006 2nd edition (ISBN 9780471241959). Page numbers here are the 1991 printed pages and will not match the 2nd edition.
- **Cross-reference chapter numbers are those of the 1991 edition.** The text sends the converse of Shannon's second theorem to "Chapter 8" (p. 38) and continuous entropy to "Chapter 9" (p. 37). The canon lists channel capacity as Ch. 7 in the 2nd edition, so these numbers probably shift between editions. Check before citing.
- **Page range.** The assignment gave PDF pp. 34–57 (printed ~12–35), but the chapter runs to printed p. 49 (PDF p. 71), including §§2.9 (second half) to 2.11, the summary, 35 problems and the historical notes. I read PDF pp. 34–71 and digested the whole chapter.
- **OCR.** The text file garbles most equations (e.g. $\sum$ read as "c", $\ge$ as "1" or "2", $\le$ as "5", $\epsilon$ as "E"). All equations were checked against the page images. Eq. (2.80) is hard to read in the image; I took it as "$\ge$" because the text says the second inequality comes from the definition of convexity (p. 26).
- **Printed errors / oddities.**
  - Eq. (2.121) (p. 32) repeats the right-hand side of (2.120), $I(X;Z)+I(X;Y|Z)$. The proof needs $I(X;Y)+I(X;Z|Y)$; I wrote that and marked it (added step).
  - §2.9 opens by promising "four different interpretations" of the second law (p. 33), but five are listed (pp. 34–36) and the summary lists five (p. 42).
  - The log sum inequality is stated for non-negative numbers (p. 29), but the summary says "positive" (p. 41).
  - The summary (p. 42) adds a fifth second-law statement ($H(X_0|X_n)$ increases) that the text only mentions in passing (p. 36, Problem 35).
- **Terminology differs from the canon.** The book calls relative entropy the "Kullback Leibler distance" (p. 18) and lists "cross entropy" as another name for it (p. 49), whereas the canon defines cross-entropy as $H(p)+D(p\|q)$. The book uses "self-information" for $H(X)$ itself (p. 20), while the canon uses it for $-\log p(x)$.
- **Skipped.** I did not work the 35 problems; I only listed the ones tied to the chapter's results. No external facts were added; the toy example and the bridge candidates are ours and are marked as such.
