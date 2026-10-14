---
id: mackay-2003-information/ch08-dependent
work: mackay-2003-information
unit: "8 Dependent Random Variables"
pages: 138-144
fields: [information-theory, bayesian]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 5
pipeline_version: 0.1
---
# Dependent Random Variables

## L0 — One line
Joint, conditional and mutual entropy for dependent variables obey simple rules (the chain rule, and $I\ge 0$), and data processing cannot increase the average information about the source.

## L1 — The gist (≤ 120 words)
Earlier chapters compressed independent symbols. Real data and noisy channels involve dependent variables, so we need entropies of joint ensembles. The chapter defines joint, conditional and marginal entropy and mutual information. It proves the chain rule $H(X,Y)=H(X)+H(Y|X)$ and shows that $I(X;Y)$ is symmetric and non-negative. Hence, on average, observing data cannot increase uncertainty. It also proves the data-processing theorem for a Markov chain $w\to d\to r$. A warning: the Venn-diagram picture of entropies is misleading, because with three variables some "areas" can be negative (XOR example). This matters for the later channel chapters.

**Prerequisites:** entropy $H=\sum p\log(1/p)$; product rule and Bayes' theorem; relative entropy and Gibbs' inequality; Jensen's inequality.

## L2 — Key ideas
- Dependence matters for compression of real data, and noisy channels are joint ensembles whose input and output are dependent (p. 138).
- $H(X,Y)=H(X)+H(Y)$ iff $X$ and $Y$ are independent (p. 138).
- Chain rule: $H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y)$; it comes from the product rule of probability (pp. 139, 143).
- $I(X;Y)=H(X)-H(X|Y)$ is symmetric and $\ge 0$. It equals a relative entropy between $P(x,y)$ and $P(x)P(y)$ (pp. 139, 143).
- A single outcome $y$ can raise uncertainty ($H(X|y)>H(X)$), but on average $H(X|Y)\le H(X)$, with equality only under independence (pp. 140, 142).
- Conditional mutual information $I(X;Y|Z)$ is defined; other three-term entropies such as $I(X;Y;Z)$ are not allowed (p. 139).
- Venn diagrams of entropies mislead: with $z=x+y \bmod 2$, $I(X;Y)=0$ but $I(X;Y|Z)=1$ bit (p. 144).
- Data processing: for $w\to d\to r$, $I(W;R)\le I(W;D)$ (p. 144).

## L3 — Walkthrough

**Chapter introduction (p. 138).** Earlier chapters used a separable distribution, where each component is independent. Two motivations now: real data are correlated, and a noisy channel with input $x$, output $y$ gives a dependent pair. If they were independent, communication would be impossible (p. 138).

**8.1 More about entropy (pp. 138–139).**
- Joint entropy: $$H(X,Y)=\sum_{xy\in\mathcal A_X\mathcal A_Y}P(x,y)\log\frac1{P(x,y)}\tag{8.1}$$
- Additivity: $$H(X,Y)=H(X)+H(Y)\ \text{ iff }\ P(x,y)=P(x)P(y)\tag{8.2}$$
- Conditional entropy given one value $y=b_k$ is the entropy of $P(x|y=b_k)$: $$H(X|y=b_k)\equiv\sum_{x}P(x|y=b_k)\log\frac1{P(x|y=b_k)}\tag{8.3}$$
- Conditional entropy given $Y$ averages this over $y$: $$H(X|Y)\equiv\sum_y P(y)\Big[\sum_x P(x|y)\log\frac1{P(x|y)}\Big]=\sum_{xy}P(x,y)\log\frac1{P(x|y)}\tag{8.4}$$ It is the average uncertainty left about $x$ once $y$ is known (p. 138).
- Marginal entropy is just another name for $H(X)$ (p. 139).
- Chain rule for information content (from the product rule): $\log\frac1{P(x,y)}=\log\frac1{P(x)}+\log\frac1{P(y|x)}$ (8.5), so $h(x,y)=h(x)+h(y|x)$ (8.6) (p. 139).
- Chain rule for entropy: $$H(X,Y)=H(X)+H(Y|X)=H(Y)+H(X|Y)\tag{8.7}$$
- Mutual information: $$I(X;Y)\equiv H(X)-H(X|Y)\tag{8.8}$$ It satisfies $I(X;Y)=I(Y;X)$ and $I(X;Y)\ge0$. It is the average reduction in uncertainty about $x$ from learning $y$, or vice versa (p. 139).
- Conditional mutual information: $I(X;Y|z=c_k)=H(X|z=c_k)-H(X|Y,z=c_k)$ (8.9). Averaging over $z$ gives $$I(X;Y|Z)=H(X|Z)-H(X|Y,Z)\tag{8.10}$$ (p. 139).
- No other three-term entropies are defined; $I(X;Y;Z)$ and $I(X|Y;Z)$ are "illegal". Each slot of $I(X;Y|Z)$ may hold several variables, e.g. $I(A,B;C,D|E,F)$ (p. 139).
- Figure 8.1 splits $H(X,Y)$ into the boxes $H(X|Y)$, $I(X;Y)$, $H(Y|X)$. $H(X)$ spans the first two, $H(Y)$ the last two. The author says: "This figure is important." (pp. 139–140).

*Intuition note.* Entropy of a pair adds up like bookkeeping: first what $X$ costs, then what $Y$ still costs once $X$ is known. Mutual information is the part of $X$'s uncertainty that knowing $Y$ removes.

**8.2–8.3 Exercises (pp. 140–142).** Problems only; see "Exercises worth doing". Exercise 8.8 asks why the Venn drawing of Figure 8.1 (Figure 8.2) misleads. Exercise 8.9 introduces the Markov chain $w\to d\to r$, meaning $P(w,d,r)=P(w)P(d|w)P(r|d)$ (8.14–8.15) (p. 141). The author adds that the data-processing theorem is as much a caution about the definition of "information" as about processing (p. 141).

**8.4 Solutions (pp. 142–144).**

*Ex. 8.2: data do not increase uncertainty on average (p. 142).* A single $y$ can raise uncertainty: in Exercise 8.6 with $y=3$, $H(X|y)$ exceeds $H(X)$ (p. 142). For the average, rewrite with Bayes' theorem:
$$H(X|Y)=\sum_{xy}P(x,y)\log\frac1{P(x|y)}\tag{8.16}$$
$$=\sum_{xy}P(x)P(y|x)\log\frac{P(y)}{P(y|x)P(x)}\tag{8.17}$$
$$=\sum_x P(x)\log\frac1{P(x)}+\sum_xP(x)\sum_yP(y|x)\log\frac{P(y)}{P(y|x)}\tag{8.18}$$
The author calls the last term a sum of relative entropies between $P(y|x)$ and $P(y)$. (Added step: each inner sum is the *negative* of a relative entropy, so it is $\le0$ by Gibbs' inequality.) Hence
$$H(X|Y)\le H(X)+0,\tag{8.19}$$
with equality only if $P(y|x)=P(y)$ for all $x,y$, i.e. only if $X,Y$ are independent (p. 142).

*Ex. 8.3: chain rule (p. 143).* Split the logarithm of $P(x,y)=P(x)P(y|x)$:
$$H(X,Y)=\sum_{xy}P(x,y)\log\frac1{P(x,y)}=\sum_{xy}P(x)P(y|x)\Big[\log\frac1{P(x)}+\log\frac1{P(y|x)}\Big]$$
$$=\sum_xP(x)\log\frac1{P(x)}+\sum_xP(x)\sum_yP(y|x)\log\frac1{P(y|x)}=H(X)+H(Y|X)\tag{8.20–8.23}$$

*Ex. 8.4: symmetry and positivity of $I$ (p. 143).*
$$I(X;Y)=\sum_xP(x)\log\frac1{P(x)}-\sum_{xy}P(x,y)\log\frac1{P(x|y)}=\sum_{xy}P(x,y)\log\frac{P(x|y)}{P(x)}=\sum_{xy}P(x,y)\log\frac{P(x,y)}{P(x)P(y)}\tag{8.24–8.27}$$
This is symmetric in $x,y$, so $I(X;Y)=H(X)-H(X|Y)=H(Y)-H(Y|X)$ (8.28). Positivity, two ways. (i) The expression (8.29) is a relative entropy, so Gibbs' inequality gives $\ge0$, with equality only if $P(x,y)=P(x)P(y)$. (ii) Jensen's inequality:
$$-\sum_{x,y}P(x,y)\log\frac{P(x)P(y)}{P(x,y)}\ \ge\ -\log\sum_{x,y}\frac{P(x,y)}{P(x,y)}P(x)P(y)=\log1=0\tag{8.30}$$

*Intuition note.* $I(X;Y)$ measures how far the joint distribution is from the product of its marginals. A distance-like quantity of this kind cannot be negative, and it is zero exactly at independence.

*Ex. 8.7: $z=(x+y)\bmod2$, $x,y$ independent (p. 143).* (a) If $q=\tfrac12$: $P_Z=\{\tfrac12,\tfrac12\}$ and $I(Z;X)=H(Z)-H(Z|X)=1-1=0$. (b) In general $P_Z=\{pq+(1-p)(1-q),\ p(1-q)+q(1-p)\}$ and $I(Z;X)=H_2(pq+(1-p)(1-q))-H_2(q)$ (p. 143). This is the binary symmetric channel: $x$ input, $y$ noise, $z$ output (p. 141).

*Ex. 8.8: why Venn diagrams mislead (pp. 143–144).*
1. Venn diagrams depict sets, but it is unclear what the "sets" $H(X)$, $H(Y)$ contain. Students may treat an outcome $(x,y)$ as a point and confuse entropies with probabilities (pp. 143–144).
2. They suggest all areas are positive. For two variables $H(X|Y)$, $I(X;Y)$, $H(Y|X)$ are indeed non-negative. For three variables, positive-looking areas may be negative (p. 144).
Figure 8.3 correctly shows $H(X)+H(Z|X)+H(Y|X,Z)=H(X,Y,Z)$ (8.31), but wrongly suggests $I(X;Y|Z)$ is less than $I(X;Y)$ (p. 144).
- Example: $x,y$ independent fair bits, $z=x+y\bmod2$. Then $H(X)=H(Y)=H(Z)=1$ bit and $H(Y|X)=H(Y)=1$, so $I(X;Y)=0$.
- Given $z$, knowing $x$ gives $y=z-x\bmod 2$, so $I(X;Y|Z)=1$ bit. The region $A$ would have to be $-1$ bit.
- This is not exceptional: in the binary symmetric channel $I(X;Y)=0$ but $I(X;Y|Z)>0$.
- The diagram is valid only if one remembers that positive areas may be negative quantities (p. 144).

*Intuition note.* Two independent causes can become dependent once you see their combined effect. Observing $z$ links $x$ and $y$, so conditioning can create information between variables.

*Ex. 8.9: data-processing theorem (p. 144).* For any $XYZ$: $$I(X;Y,Z)=I(X;Y)+I(X;Z|Y)\tag{8.32}$$ For $w\to d\to r$, $w$ and $r$ are independent given $d$, so $I(W;R|D)=0$. Applying (8.32) twice: $I(W;D,R)=I(W;D)$ (8.33) and $I(W;D,R)=I(W;R)+I(W;D|R)$ (8.34). Therefore $$I(W;R)-I(W;D)\le0\tag{8.35}$$ (Added step: this uses $I(W;D|R)\ge0$.)

*Intuition note.* Processing $d$ into $r$ can only discard information about $w$ (on average), never add any, if $r$ depends on $w$ only through $d$.

## Toy example (ours)
Let $P(0,0)=\tfrac12$, $P(0,1)=0$, $P(1,0)=\tfrac14$, $P(1,1)=\tfrac14$ (first index $x$, second $y$).
- $P(x)=(\tfrac12,\tfrac12)$, so $H(X)=1$. $P(y)=(\tfrac34,\tfrac14)$, so $H(Y)=\tfrac34\log_2\tfrac43+\tfrac14\cdot2=0.3113+0.5=0.8113$.
- $H(X,Y)=\tfrac12\cdot1+\tfrac14\cdot2+\tfrac14\cdot2=1.5$.
- Chain rule: $H(Y|X)=1.5-1=0.5$ and $H(X|Y)=1.5-0.8113=0.6887$.
- Check via (8.4): $P(x|y{=}0)=(\tfrac23,\tfrac13)$ has entropy $0.9183$. $P(x|y{=}1)=(0,1)$ has entropy $0$. Average: $0.75\cdot0.9183+0.25\cdot0=0.6887$ ✓.
- $I(X;Y)=1-0.6887=0.3113$, and $H(Y)-H(Y|X)=0.8113-0.5=0.3113$ ✓ (symmetry). $H(X|Y)<H(X)$ ✓.

## Concepts
- [[joint-and-conditional-entropy]] — $H(X,Y)$; $H(X|y)$ is entropy of one conditional distribution; $H(X|Y)$ averages over $y$ (p. 138)
- [[chain-rule]] — $H(X,Y)=H(X)+H(Y|X)$, from the product rule; also $h(x,y)=h(x)+h(y|x)$ (p. 139)
- [[mutual-information]] — $H(X)-H(X|Y)$; symmetric, $\ge0$, zero iff independent (pp. 139, 143)
- [[relative-entropy-kl-divergence]] — $I(X;Y)=D_{KL}(P(x,y)\|P(x)P(y))$; Gibbs' inequality gives non-negativity (pp. 140, 143)
- [[data-processing-inequality]] — on a Markov chain $w\to d\to r$, $I(W;R)\le I(W;D)$ (pp. 141, 144)
- [[conditional-mutual-information]] (new) — $I(X;Y|Z)=H(X|Z)-H(X|Y,Z)$; may exceed $I(X;Y)$ (pp. 139, 144)
- [[entropy-venn-diagram-caveat]] (new) — Venn areas for entropies can be negative with three variables (p. 144)
- [[noisy-channel]] — a joint ensemble with dependent input and output (p. 138)

## Canonical instances
- [[xor-three-variable-ensemble]] (new) — $z=x+y \bmod 2$: $I(X;Y)=0$ but $I(X;Y|Z)=1$ bit (p. 144)
- [[binary-symmetric-channel]] — input $x$, noise $y$, output $z$ (pp. 141, 144)
- [[three-cards-problem]] (new) — inference exercise (white/black card), posed, not solved here (p. 142)

## Bridges (candidates)
- [structural-analogy] Data-processing inequality ↔ bayesian: posterior inference from a statistic $r(d)$ cannot be more informative about $w$ than from full data $d$ — same Markov structure.
- [structural-analogy] $I(X;Y|Z)>0$ while $I(X;Y)=0$ ↔ bayesian (causal DAGs): conditioning on a collider opens a path between independent causes.
- [same-math] $I(X;Y)=D_{KL}(P(x,y)\|P(x)P(y))$ ↔ information-theory: relative entropy and Gibbs' inequality.

## Questions this raises
- How does $I(X;Y)$ for a channel turn into a maximum rate of reliable communication (chapters 9–11)?
- Why is $I(X;Y|Z)$ not bounded by $I(X;Y)$, and when is it smaller?
- Does the forward vs reversed $N$-gram language question (Ex. 8.11) have the same entropy rate in both directions?
- If data processing never adds information, why do features and summaries still help in practice?

## Exercises worth doing
- Ex. 8.1 (p. 140) — entropies of overlapping variables $X=(U,V)$, $Y=(V,W)$; practice with the chain rule — easy
- Ex. 8.2 (p. 140) — example where $H(X|y)>H(X)$ yet $H(X|Y)<H(X)$ — medium
- Ex. 8.6 (p. 140) — full table of joint, marginal, conditional entropies and $I$ — medium
- Ex. 8.7 (p. 141) — $z=x+y\bmod 2$; link to the binary symmetric channel — medium
- Ex. 8.10 (p. 142) — three cards: inference plus information measures — medium
- Ex. 8.11 (p. 142) — forward vs reversed text under an $N$-gram model — medium

## Reading notes
- Printed page = pdf − 12 (pdf 150 = p. 138).
- The text layer of p. 144 is badly garbled in the figure area; the images show Figure 8.3 labels as expected. Equations were checked against the images.
- Solutions for Exercises 8.1, 8.5, 8.6, 8.10, 8.11 are not printed in these pages. Ex. 8.2's solution points to Ex. 8.6 (p. 140) for its example; the solution to Ex. 8.6 itself (listed as p. 147) lies outside this unit.
- Exercise 8.5 defines "entropy distance" $D_H(X,Y)=H(X,Y)-I(X;Y)$ (8.12); the author says it is unlikely to appear again.
- Solution 8.2 (8.18) calls the sum a "sum of relative entropies"; the terms as written carry a minus sign (see the added step).
