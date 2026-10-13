---
id: jaynes-2003-probability/ch02-quantitative
work: jaynes-2003-probability
unit: "2 The quantitative rules"
pages: 24-50
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-13
---

# The quantitative rules

## L0 — One line
If degrees of plausibility are real numbers that obey common-sense qualitative requirements and structural consistency, then they must be combinable by exactly two rules, the product rule and the sum rule, which are ordinary probability theory (p. 33–34).

## L1 — The gist (≤ 120 words)
The chapter asks which rules a reasoning "robot" must use to combine real-number plausibilities consistently. Associativity of the logical product forces a product rule, via the functional equation $F[F(x,y),z]=F[x,F(y,z)]$ (p. 27–29). Consistency of negation forces a sum rule $w^m(A|B)+w^m(\bar A|B)=1$ (p. 33). Rescaling to $p=w^m$ gives the usual probability rules (p. 33). Symmetry arguments then fix numerical values: equal probabilities $1/n$ for indifferent, exhaustive, exclusive propositions (p. 40). The rest shows that Aristotelian logic is the limiting case, and discusses Gödel, Venn diagrams and Kolmogorov's axioms (p. 35–50).

## L2 — Key ideas (5–10 bullets)
- **Product rule from associativity.** $AB|C$ must be a function of $B|C$ and $A|BC$. Since $(AB)C=A(BC)$, that function obeys the associativity equation. Its solution is $w(AB|C)=w(A|BC)w(B|C)$ (p. 25–29).
- **Sum rule from negation.** Let $v=S(u)$ link a plausibility to that of its negation. The product rule must give the same value for $A\bar B$ and $B\bar A$. This forces $S(x)=(1-x^m)^{1/m}$ (p. 30–33).
- **The exponent $m$ is irrelevant.** Defining $p=w^m$ gives $p(AB|C)=p(A|C)p(B|AC)$ and $p(A|B)+p(\bar A|B)=1$. All freedom left is a monotonic reparametrisation (p. 33–34).
- **The rules are complete.** From the product and sum rules, $P(A+B|C)=P(A)+P(B)-P(AB)$ follows. Conjunction and negation generate all Boolean functions (p. 34–35).
- **Logic is the limit.** The strong syllogisms are $p=1$ and $p=0$ cases. The weak ones, including the "policeman's syllogism", become quantitative inequalities (p. 35–37).
- **Numbers come from symmetry.** If the information is indifferent between propositions, permuting labels gives equal probabilities $1/n$. This is the principle of indifference, and the first form of group-invariance reasoning (p. 38–41).
- **$p$, not $x$, is fixed by the data.** The original plausibilities $x$ are arbitrary monotonic functions of $p$. The Kelvin-scale analogy shows that $p$ is a convenient scale, not a more "correct" one (p. 41–42).
- **Finite-sets policy.** The consistency theorems hold on finite sets of propositions. Infinite cases are allowed only as limits of finite ones (p. 43–44).
- **Comments.** Probabilities are "subjective" only as states of knowledge, and "objective" in being independent of the user. Gödel's theorem does not block this theory. Venn diagrams and Kolmogorov's axioms are special cases (p. 44–50).

## L3 — Walkthrough

### Opening (p. 24)
The desiderata are (I) real-number representation of plausibility, (II) qualitative correspondence with common sense, (III) consistency (p. 24). This chapter derives the rules that follow from them (p. 24).

### 2.1 The product rule (p. 24–30)

**Why $B|C$ and $A|BC$.** To decide that $AB$ is true, the robot can first decide $B$ (plausibility $B|C$). Having accepted $B$, it then decides $A$ (plausibility $A|BC$). Or it can do this in the other order, with $A|C$ and $B|AC$ (p. 24). If $B$ is false, $AB$ is false whatever is known about $A$. So with $B|C$ and $A|BC$ the robot does not need $A|C$ (p. 25). Getting the same $AB|C$ from either order is desideratum (IIIa) (p. 25). Hence

$$(AB|C)=F[(B|C),(A|BC)].\tag{2.1}$$

**Rejected alternative.** The form $(AB|C)=F[(A|C),(B|C)]$ \tag{2.2} cannot satisfy desideratum (II). Both $A$ and $B$ can be plausible while $AB$ is very plausible or very implausible. Example: "blue eyes" and "black hair" are both plausible, and their conjunction is reasonably plausible. "Left eye blue" and "right eye brown" are each plausible, but both together are extremely implausible (p. 25).

**Exhaustive check.** Define
$$u=(AB|C),\; v=(A|C),\; w=(B|AC),\; x=(B|C),\; y=(A|BC).\tag{2.3}$$
Writing $u$ as a function of two or more of $v,w,x,y$ gives 11 possibilities. Tribus (1969) finds that all but two can violate common sense in some extreme case. The survivors are $u=F(x,y)$ and $u=F(w,v)$ (p. 25–26).

**Monotonicity.** Suppose $C\to C'$ makes $B$ more plausible but leaves $A|BC$ unchanged:
$$B|C'>B|C,\tag{2.4}$$
$$A|BC'=A|BC.\tag{2.5}$$
Then common sense requires
$$AB|C'\ge AB|C,\tag{2.6}$$
with equality iff $A|BC$ is impossibility (p. 26). Similarly
$$B|C''=B|C,\tag{2.7}$$
$$A|BC''>A|BC,\tag{2.8}$$
require
$$AB|C''\ge AB|C,\tag{2.9}$$
with equality only if $B$ is impossible given $C$ (p. 26). $F$ must also be continuous, otherwise a tiny change in one input could cause a large jump in $AB|C$ (p. 26). With differentiability (not necessary, p. 26):
$$F_1(x,y)\equiv \frac{\partial F}{\partial x}\ge 0\tag{2.10a}$$
(equality iff $y$ represents impossibility), and
$$F_2(x,y)\equiv \frac{\partial F}{\partial y}\ge 0\tag{2.10b}$$
(equality only if $x$ represents impossibility) (p. 26).

**Associativity.** Since $ABC=(AB)C=A(BC)$, the plausibility $(ABC|D)$ can be computed in two ways:
$$(ABC|D)=F[(BC|D),(A|BCD)],\tag{2.11}$$
$$(ABC|D)=F\{F[(C|D),(B|CD)],(A|BCD)\},\tag{2.12a}$$
$$(ABC|D)=F[(C|D),(AB|CD)]=F\{(C|D),F[(B|CD),(A|BCD)]\}.\tag{2.12b}$$
Consistency requires (2.12a) = (2.12b), which gives the functional equation
$$F[F(x,y),z]=F[x,F(y,z)].\tag{2.13}$$
This is Aczél's "Associativity Equation", with a history going back to Abel (1826) (p. 27). Aczél solves it without differentiability, but the proof takes 11 pages in his book. Jaynes gives Cox's shorter proof, which assumes differentiability (p. 27). The trivial solution $F=\text{const}$ violates (2.10) (p. 27).

**Cox's solution.** Put $u\equiv F(x,y)$, $v\equiv F(y,z)$ (2.14). Then (2.13) reads
$$F(x,v)=F(u,z).\tag{2.15}$$
Differentiating with respect to $x$ and $y$:
$$F_1(x,v)=F_1(u,z)F_1(x,y),\qquad F_2(x,v)F_1(y,z)=F_1(u,z)F_2(x,y).\tag{2.16}$$
Eliminating $F_1(u,z)$, with $G(x,y)\equiv F_2(x,y)/F_1(x,y)$:
$$G(x,v)F_1(y,z)=G(x,y).\tag{2.17}$$
The left side must not depend on $z$ (p. 27–28). Using $F_2=GF_1$ (added step), (2.17) can also be written
$$G(x,v)F_2(y,z)=G(x,y)G(y,z).\tag{2.18}$$
Call the left sides of (2.17) and (2.18) $U$ and $V$. Then $\partial V/\partial y=\partial U/\partial z$, so $G(x,y)G(y,z)$ is independent of $y$. The most general such $G$ is
$$G(x,y)=r\frac{H(x)}{H(y)},\tag{2.19}$$
with $r>0$ constant (since $G>0$) and $H$ of one sign (p. 28). Then
$$F_1(y,z)=\frac{H(v)}{H(y)},\tag{2.20}$$
$$F_2(y,z)=r\frac{H(v)}{H(z)}.\tag{2.21}$$
(Added step: (2.20) is $G(x,y)/G(x,v)$ from (2.17). (2.21) is $G(x,y)G(y,z)/G(x,v)$ from (2.18).) With $dv=F_1dy+F_2dz$:
$$\frac{dv}{H(v)}=\frac{dy}{H(y)}+r\frac{dz}{H(z)}.\tag{2.22}$$
Integrating,
$$w[F(y,z)]=w(v)=w(y)w^r(z),\tag{2.23}$$
$$w(x)\equiv\exp\left\{\int^x\frac{dx}{H(x)}\right\}.\tag{2.24}$$
The missing lower limit means $w$ has an arbitrary multiplicative factor (p. 28). Apply $w$ to (2.15) and use (2.23) twice:
$$w(x)w^r(y)[w(z)]^{r^2}=w(x)w^r(y)w^r(z).\tag{2.25}$$
This holds nontrivially only if $r=1$, so
$$w[F(x,y)]=w(x)w(y),\tag{2.26}$$
$$F(x,y)=w^{-1}[w(x)w(y)].\tag{2.27}$$
That is, associativity plus commutativity of the logical product force the **product rule**:
$$w(AB|C)=w(A|BC)w(B|C)=w(B|AC)w(A|C).\tag{2.28}$$
By construction $w$ is positive, continuous and monotonic (p. 29). The rule is also sufficient for consistency, for any number of joint propositions (p. 29).

*Intuition note.* Once you insist that "A and B" be computed the same way whichever proposition you condition on first, the only freedom left is a relabelling $w$ under which plausibilities simply multiply.

**Limits of $w$.**
- If $A$ is certain given $C$, then $AB|C=B|C$ (2.29) and $A|BC=A|C$ (2.30). Then (2.28) becomes $w(B|C)=w(A|C)w(B|C)$ (2.31). This must hold for every $B$, so certainty is $w(A|C)=1$ (2.32) (p. 29).
- If $A$ is impossible given $C$, then $AB|C=A|C$ (2.33) and $A|BC=A|C$ (2.34). Then $w(A|C)=w(A|C)w(B|C)$ (2.35). So $w=0$ or $+\infty$. The value $-\infty$ is excluded because continuity would then require negative $w(B|C)$ (p. 29–30).
- So $w$ is either increasing from 0 (impossible) to 1 (certain), or decreasing from $\infty$ to 1. The two are equivalent through $w_2=1/w_1$. The convention $0\le w\le 1$ loses nothing (p. 30).

### 2.2 The sum rule (p. 30–34)

Since $A\bar A$ is always false and $A+\bar A$ always true, $\bar A|B$ depends on $A|B$. With $u\equiv w(A|B)$ and $v\equiv w(\bar A|B)$,
$$v=S(u).\tag{2.36}$$
$S$ is continuous and monotonic decreasing, with $S(0)=1$ and $S(1)=0$ (p. 30). The product rule written for $AB$ and $A\bar B$ gives
$$w(AB|C)=w(A|C)w(B|AC),\tag{2.37}$$
$$w(A\bar B|C)=w(A|C)w(\bar B|AC).\tag{2.38}$$
Using (2.36) and (2.38),
$$w(AB|C)=w(A|C)S[w(\bar B|AC)]=w(A|C)S\!\left[\frac{w(A\bar B|C)}{w(A|C)}\right].\tag{2.39}$$
This equation is correct as printed. Its middle term follows from (2.36) and its last term from (2.38) (p. 30).

Next, commutativity: $w(AB|C)$ is symmetric in $A$ and $B$. Applying (2.39) with $A$ and $B$ interchanged gives
$$w(A|C)S\!\left[\frac{w(A\bar B|C)}{w(A|C)}\right]=w(B|C)S\!\left[\frac{w(B\bar A|C)}{w(B|C)}\right].\tag{2.40}$$
This must hold for all $A,B,C$, in particular for $\bar B=AD$ with $D$ arbitrary (2.41). Then
$$A\bar B=\bar B,\qquad B\bar A=\bar A,\tag{2.42}$$
$$w(A\bar B|C)=w(\bar B|C)=S[w(B|C)],\qquad w(B\bar A|C)=w(\bar A|C)=S[w(A|C)].\tag{2.43}$$
With $x\equiv w(A|C)$ and $y\equiv w(B|C)$ (2.44), this becomes the scaling equation
$$xS\!\left[\frac{S(y)}{x}\right]=yS\!\left[\frac{S(x)}{y}\right],\qquad 0\le S(y)\le x,\; 0\le x\le1.\tag{2.45}$$
For $y=1$ (added step: $S(1)=0$, $S(0)=1$) this reduces to
$$S[S(x)]=x,\tag{2.46}$$
so $S$ is self-reciprocal (p. 31).

**Domain.** Choosing $D$ arbitrarily, $0\le w(D|AC)\le1$ (2.47). Since $S(y)=w(AD|C)=w(A|C)w(D|AC)$, this is $0\le S(y)\le x$. Geometrically, the domain is the unit square on or above the curve $y=S(x)$ (p. 31).

**Shape of $S$.** The curve is fixed by (2.45) just above it, with $y=S(x)+\epsilon$ and $\epsilon\to0^+$. Everything then depends on how $S(1-\delta)\to0$ as $\delta\to0$ (p. 31–32). Define $q(x,y)$ by
$$\frac{S(x)}{y}=1-\exp\{-q\}.\tag{2.48}$$
Let $\delta=e^{-q}$ and define $J(q)$ by
$$S(1-\delta)=S(1-\exp\{-q\})=\exp\{-J(q)\}.\tag{2.49}$$
(The closing parenthesis is missing in the printed second term.) We need the asymptotics of $J$ as $q\to\infty$ (p. 32). With $x,q$ independent,
$$S(y)=S[S(x)]+\exp\{-q\}S(x)S'[S(x)]+O(\exp\{-2q\}).\tag{2.50}$$
Using (2.46) and its derivative $S'[S(x)]S'(x)=1$,
$$\frac{S(y)}{x}=1-\exp\{-(\alpha+q)\}+O(\exp\{-2q\}),\tag{2.51}$$
$$\alpha(x)\equiv\log\left[\frac{-xS'(x)}{S(x)}\right]>0.\tag{2.52}$$
(Added step: $S(x)S'[S(x)]/x=S(x)/(xS'(x))=e^{-\alpha}$ with the sign absorbed.) Then (2.45) becomes
$$J(q+\alpha)-J(q)=\log\left[\frac{x}{S(x)}\right]+\log(1-\exp\{-q\})+O(\exp\{-2q\}),\quad 0<q<\infty,\;0<x\le1.\tag{2.53}$$
(Added step: the left of (2.45) gives $x\exp\{-J(q+\alpha)\}$ and the right gives $y\exp\{-J(q)\}$, with $y=S(x)/(1-e^{-q})$.) As $q\to\infty$ the last two terms vanish exponentially, so $J$ is asymptotically linear:
$$J(q)\sim a+bq+O(\exp\{-q\}),\tag{2.54}$$
$$b=\alpha^{-1}\log\left[\frac{x}{S(x)}\right].\tag{2.55}$$
No periodic term with period $\alpha$ is possible, because (2.53) holds for a continuum of $\alpha(x)$ values. $J$ depends only on $q$, so the right side of (2.55) cannot depend on $x$. Using (2.52),
$$\frac{x}{S(x)}=\left[\frac{-xS'(x)}{S(x)}\right]^b,\qquad 0<b<\infty.\tag{2.56}$$
With $m\equiv1/b$ (added step: raise to the power $m$), this is the differential equation
$$S^{m-1}dS+x^{m-1}dx=0.\tag{2.57}$$
The only solution with $S(0)=1$ is
$$S(x)=(1-x^m)^{1/m},\qquad 0\le x\le1,\;0<m<\infty.\tag{2.58}$$
Conversely, (2.58) solves (2.45). It automatically satisfies $S(1)=0$ (p. 32–33). Cox (1946) first got (2.58) by a different argument assuming twice-differentiable $S$. Aczél derives it without differentiability. Jaynes calls the differentiability assumption "innocuous" (p. 33).

**Sufficiency.** Since (2.41) was a special choice, (2.58) is so far only necessary. Substituting (2.58) into (2.40) gives
$$w^m(A|C)-w^m(A\bar B|C)=w^m(B|C)-w^m(B\bar A|C),\tag{2.59}$$
a trivial identity by (2.28) and (2.38). So (2.58) is necessary and sufficient (p. 33).

**Summary.** Some monotonic function $w$ obeys both the product rule (2.28) and the sum rule
$$w^m(A|B)+w^m(\bar A|B)=1.\tag{2.60}$$
The product rule can be written
$$w^m(AB|C)=w^m(A|C)w^m(B|AC)=w^m(B|C)w^m(A|BC).\tag{2.61}$$
Define
$$p(x)\equiv w^m(x).\tag{2.62}$$
Then
$$p(AB|C)=p(A|C)p(B|AC)=p(B|C)p(A|BC),\tag{2.63}$$
$$p(A|B)+p(\bar A|B)=1.\tag{2.64}$$
This loses no generality. $w^m$ is again continuous, monotonic and ranges over $[0,1]$. So all possibilities allowed by the desiderata are (2.63)–(2.64) with $p$ any continuous monotonic increasing function with $0\le p\le1$ (p. 33–34).

*Intuition note.* Requiring that "not-A" be consistent with the product rule forces $x^m+\bar x^m=1$. The exponent can be absorbed into the scale, leaving ordinary probabilities.

**Completeness.** Conjunction and negation generate all logic functions (p. 34). Logical sum:
$$\begin{aligned}p(A+B|C)&=1-p(\bar A\bar B|C)=1-p(\bar A|C)p(\bar B|\bar AC)\\&=1-p(\bar A|C)[1-p(B|\bar AC)]=p(A|C)+p(\bar AB|C)\\&=p(A|C)+p(B|C)p(\bar A|BC)=p(A|C)+p(B|C)[1-p(A|BC)]\end{aligned}\tag{2.65}$$
$$p(A+B|C)=p(A|C)+p(B|C)-p(AB|C).\tag{2.66}$$
The primitive sum rule is the special case $B=\bar A$ (p. 34). Exercise 2.1 asks for a formula for $p(C|A+B)$. Exercise 2.2 asks to show
$$p(C|(A_1+\cdots+A_n)X)=\frac{\sum_ip(A_i|X)p(C|A_iX)}{\sum_ip(A_i|X)}\tag{2.67}$$
for mutually exclusive $A_i$ (p. 34).

Any logic function other than the contradiction is a logical sum of basic conjunctions $Q_i$, $1\le i\le 2^n$. Each $Q_i$ follows from repeated use of the product rule. Because the $Q_i$ are mutually exclusive, their sum reduces to $\sum_ip(Q_i|C)$ of at most $2^n-1$ terms (p. 34–35). Whenever the background information fixes the basic conjunctions, the rules determine every proposition in the algebra. For $n=4$: $2^4=16$ conjunctions, and $2^{16}=65\,536$ propositions (p. 35). Usually only a small part of this is needed (p. 35).

### 2.3 Qualitative properties (p. 35–37)

With $p\to0$ or $1$, the sum rule gives the Aristotelian postulate (p. 35). The strong syllogisms are
$$A\Rightarrow B,\; A\text{ true}\;\therefore\; B\text{ true};\qquad A\Rightarrow B,\; B\text{ false}\;\therefore\; A\text{ false}.\tag{2.68}$$
Let $C\equiv A\Rightarrow B$ (2.69). The product rule gives
$$p(B|AC)=\frac{p(AB|C)}{p(A|C)},\qquad p(A|\bar BC)=\frac{p(A\bar B|C)}{p(\bar B|C)}.\tag{2.70}$$
Since $p(AB|C)=p(A|C)$ and $p(A\bar B|C)=0$,
$$p(B|AC)=1,\qquad p(A|\bar BC)=0.\tag{2.71}$$
So deductive logic is the limiting form of the rules as the robot becomes certain (p. 35).

**Weak syllogisms.** First, "$A\Rightarrow B$, $B$ true, so $A$ more plausible" (2.72) uses
$$p(A|BC)=p(A|C)\frac{p(B|AC)}{p(B|C)}.\tag{2.73}$$
With $p(B|AC)=1$ and $p(B|C)\le1$,
$$p(A|BC)\ge p(A|C).\tag{2.74}$$
Second, "$A\Rightarrow B$, $A$ false, so $B$ less plausible" (2.75) uses
$$p(B|\bar AC)=p(B|C)\frac{p(\bar A|BC)}{p(\bar A|C)}.\tag{2.76}$$
From (2.74), $p(\bar A|BC)\le p(\bar A|C)$, so
$$p(B|\bar AC)\le p(B|C).\tag{2.77}$$
Third, the policeman's syllogism. The premise "if $A$ is true, $B$ becomes more plausible" is
$$p(B|AC)>p(B|C),\tag{2.78}$$
and (2.73) gives at once
$$p(A|BC)>p(A|C).\tag{2.79}$$
(p. 36)

**Quantitative answer.** What decides whether $B$ lifts $A$ almost to certainty? By (2.73), a large increase requires $p(B|C)$ to be very small. The gentleman's behaviour makes guilt near-certain because that behaviour is otherwise very unlikely. If $A$ barely raises $B$, then $B$ barely raises $A$ (p. 36–37). Several other authors have shown the full qualitative agreement with common sense (p. 37).

*Intuition note.* Evidence $B$ moves $A$ by the factor $p(B|AC)/p(B|C)$. Surprising evidence that $A$ predicts well gives a big jump.

### 2.4 Numerical values (p. 37–42)

Two things are still missing. The choice of $p(x)$ seems to leave infinitely many rule sets. And nothing yet gives starting numerical values, which needs desiderata (IIIb) and (IIIc) (p. 37).

**Sum of mutually exclusive propositions.** Apply (2.66) twice, with
$$(A_1+A_2)A_3=A_1A_3+A_2A_3.\tag{2.81}$$
The first application gives (2.80):
$$p(A_1+A_2+A_3|B)=p(A_1+A_2|B)+p(A_3|B)-p(A_1A_3+A_2A_3|B).$$
After the second application, seven terms remain:
$$\begin{aligned}p(A_1+A_2+A_3|B)&=p(A_1|B)+p(A_2|B)+p(A_3|B)\\&\quad-p(A_1A_2|B)-p(A_2A_3|B)-p(A_3A_1|B)\\&\quad+p(A_1A_2A_3|B).\end{aligned}\tag{2.82}$$
If the $A_i$ are mutually exclusive,
$$p(A_iA_j|B)=p(A_i|B)\delta_{ij},\tag{2.83}$$
the last four terms vanish:
$$p(A_1+A_2+A_3|B)=p(A_1|B)+p(A_2|B)+p(A_3|B).\tag{2.84}$$
By induction,
$$p(A_1+\cdots+A_m|B)=\sum_{i=1}^mp(A_i|B),\qquad1\le m\le n.\tag{2.85}$$
Conventional texts treat (2.85) as an arbitrary axiom. Here it is deduced (p. 38). If the propositions are also exhaustive,
$$\sum_{i=1}^np(A_i|B)=1.\tag{2.86}$$
This does not fix the individual values. Translating information $B$ into $p(A_i|B)$ is an open-ended research problem (p. 38).

**The symmetric case.** Jaynes asks the reader to put intuition aside for the following logical argument (p. 38–39). Problem I: find $p(A_i|B)_I$ for exclusive, exhaustive $\{A_1,\dots,A_n\}$. Problem II relabels the first two:
$$A_1'\equiv A_2,\quad A_2'\equiv A_1,\quad A_k'\equiv A_k\;(3\le k\le n).\tag{2.87}$$
The same state of knowledge about the same proposition gives the transformation equations
$$p(A_1|B)_I=p(A_2'|B)_{II},\tag{2.88}$$
$$p(A_2|B)_I=p(A_1'|B)_{II}.\tag{2.89}$$
They hold whatever $B$ is. Now suppose $B$ is indifferent between $A_1$ and $A_2$. Then the two problems are entirely equivalent. Desideratum (IIIc) (equivalent states of knowledge give equivalent assignments) gives the symmetry equations
$$p(A_i|B)_I=p(A_i'|B)_{II},\quad i=1,\dots,n.\tag{2.90}$$
Combining (2.88)–(2.90):
$$p(A_1|B)_I=p(A_2|B)_I.\tag{2.91}$$
This is a "baby" version of the group-invariance principle, extended in Chapter 6 to noninformative priors (p. 40).

**General permutation.** Let $\{A_1'',\dots,A_n''\}$ be any permutation, with $A_k''\equiv A_i$ (Problem III). Then
$$p(A_i|B)_I=p(A_k''|B)_{III},\tag{2.92}$$
and, if $B$ is indifferent among all $A_i$,
$$p(A_k|B)_I=p(A_k''|B)_{III},\quad k=1,\dots,n.\tag{2.93}$$
Hence
$$p(A_i|B)_I=p(A_k|B)_I.\tag{2.94}$$
There are $n!$ permutations, so for given $i$ the index $k$ runs over all other values. All $p(A_i|B)_I$ are equal (a single cyclic permutation of order $n$ already suffices). With (2.86),
$$p(A_i|B)_I=\frac1n,\qquad1\le i\le n.\tag{2.95}$$
Following Keynes (1921), this is the **principle of indifference** (p. 40).

**Why it matters.**
- *Uniqueness.* Any other values could be contradicted by relabelling (p. 41).
- *Which quantity is fixed.* The data fix the numbers $p=p(A_i|B)$, not the plausibilities $x=A_i|B$ from which we started. So any choice of $p(x)$ gives the same $p$, and the rules are in effect unique (p. 41).
- *Robot memory.* Choosing $p(x)$ corresponds only to how the robot's memory stores numbers. Any strict monotonic function of $p_i$ would give identical external behaviour. So we should say: $x\equiv A|B$ is an arbitrary monotonic function of $p\in[0,1]$, and "it is $p$ that is rigidly fixed by the data" (p. 41).
- The quantities $p$ are now called **probabilities**. They are a convenient scale, not a more "correct" one (p. 41–42).
- *Kelvin analogy.* Out of the monotonically related empirical temperature scales, the Kelvin scale $T$ is chosen because the laws take the simplest form there, e.g. $dU=TdS-PdV$, $dG=-SdT+VdP$ (p. 42).

*Intuition note.* Symmetry alone, with no probabilistic assumption beyond consistency, forces equal probabilities when the information treats alternatives alike. The numbers come from the information, not from the representation chosen.

**Bernoulli urn example.** Ten identical balls $\{1,\dots,10\}$. Balls 4, 6, 7 are black and the rest white. One ball is drawn blindfolded. Let $A_i\equiv$ "the $i$th ball is drawn":
$$p(A_i|B)=\frac1{10},\quad1\le i\le10.\tag{2.96}$$
$$p(\text{black}|B)=p(A_4+A_6+A_7|B).\tag{2.97}$$
By (2.85):
$$p(\text{black}|B)=\frac3{10}.\tag{2.98}$$
In general, for $N$ balls and $A$ true on a subset of $M$:
$$p(A|B)=\frac MN.\tag{2.99}$$
This was James Bernoulli's (1713) definition, used for about 150 years. Laplace's *Théorie Analytique* opens with the same ratio (p. 42–43).

**Exercise 2.3** (p. 43). With $a=P(A|C)\le b=P(B|C)$, show $0\le P(AB|C)\le a$ and $b\le P(A+B|C)\le1$. Then show stronger inequalities when $a+b>1$ (conjunction) or $a+b<1$ (disjunction). These help detect calculation errors (p. 43).

### 2.5 Notation and finite-sets policy (p. 43–44)
Formal probability symbols use capital $P$ with propositions as arguments (2.100). Ordinary functions of numbers use other symbols, such as $f(r|np)$ (2.101). Small-$p$ symbols may mix both, with meaning set by context (p. 43).

The consistency theorems were established only for finite sets of propositions. Extension to infinite sets is allowed only as a well-behaved limit of finite ones (p. 43). The **finite-sets policy** says to apply ordinary arithmetic and analysis only to expressions with finitely many terms. Only afterwards should one see how the results behave as the number of terms grows without bound (p. 44). Jaynes says this agrees with Lebesgue's original definition of measure. The danger is that measure-theoretic notation presupposes the limit and hides which limiting process was used. Different well-behaved limiting processes can give different results. Chapter 15 on infinite-set paradoxes follows up (p. 44).

### 2.6 Comments (p. 44–50)

**2.6.1 "Subjective" vs. "objective" (p. 44–45).** Every probability assignment describes only a state of knowledge, not a physical measurement, so it is "subjective" in that sense. "Whose state of knowledge?" The answer is the robot's, or anyone with the same information who reasons by the same desiderata. Someone reaching a different conclusion from the same information violates a desideratum (p. 44–45). The interface desiderata (IIIb), (IIIc) make assignments "objective" in the sense of being independent of the user's personality, hopes or value judgments (p. 45).

**2.6.2 Gödel's theorem (p. 45–47).**
- The consistency requirement (IIIa) does not prove the rules consistent. It shows that other real-number rules with different content lead to inconsistencies or violate other desiderata (p. 45).
- "Inconsistent" means that contradictory results can be derived. This matches the logician's meaning: some $Q$ and $\bar Q$ both deducible (p. 45).
- A contradiction implies every proposition: $A\Rightarrow(A+B)$, so $\bar AA\Rightarrow\bar A(A+B)=\bar AA+\bar AB\Rightarrow B$ (p. 45).
- Let $A$ stand for the axioms and $T$ for a theorem: $A\Rightarrow T$ (2.102). The deducibility of $T$ cannot prove consistency, since a contradiction would also yield $T$ (p. 45–46). If there is an inconsistency, then $A\Rightarrow\bar T$ also holds (2.103). This is Fisher's (1956) intuitive reason for Gödel's result (p. 46).
- A procedure that finds contradictions would prove consistency. Gödel implies only that none derivable from the axioms being tested exists (p. 46).
- Probability theory comes close. Probabilities conditional on contradictory premises do not exist (the hypothesis space is empty). A program computing $p(B|E)$ for $E=E_1\cdots E_n$ will crash if $E$ hides a contradiction. This was found "empirically" and is a useful diagnostic. If it prints valid numbers, the $E_i$ are mutually consistent, because the theory appeals to principles not derivable from the propositions tested (p. 46).
- Undecidability only signals that the axioms hold too little information. Example: two sole witnesses give opposite testimony and then die. One lied, but we cannot decide which. Gödel's result will be seen as "more of a platitude than a paradox" (p. 46–47).
- Whether the rules' consistency can be proved from outside principles is called "open". No inconsistency has been found from correct application, while ad hoc rules in the literature are easily shown inconsistent (Chapters 5, 15, 17) (p. 47).

**2.6.3 Venn diagrams (p. 47–49).** The extended sum rule is
$$P(A+B|C)=P(A|C)+P(B|C)-P(AB|C).\tag{2.104}$$
A Venn diagram illustrates it in one special case. But reading probability as area suggests that propositions are sets of "elementary" points $\omega_i$, with $A+B$ as union and $AB$ as intersection. The general theory has no such structure (p. 47–48). Propositions like
$$A\equiv\text{it will rain today},\tag{2.105}$$
$$B\equiv\text{the roof will leak}\tag{2.106}$$
need not resolve into elementary propositions. A resolution can be forced with irrelevancies, e.g.
$$B=BC_1+BC_2+\cdots+BC_N,\tag{2.107}$$
with $C_k\equiv$ "the number of penguins in Antarctica is $k$". That is idle (p. 48). Even a real resolution may be useless, like raindrop trajectories for a forecaster. Chapter 8's "Sam's broken thermometer" will return to this. Eq. (2.98) is a case where the resolution helps (p. 48–49). Hence $AB$ should be read just as "both true", and $p(AB|C)$ is an elementary quantity. Jaynes keeps Boole's $A+B$, $AB$ to avoid set-theory connotations. He prefers to say that (2.104) justifies the Venn diagram in one special case (p. 49).

**2.6.4 The "Kolmogorov axioms" (p. 49–50).** Kolmogorov (1933) axiomatised the Venn-diagram picture in set and measure language. Jaynes says that for practical purposes his four axioms are all derived in this chapter. Appendix A discusses this (p. 49). Conceptually, Jaynes does not interpret propositions as sets, but interprets probability distributions as carriers of incomplete information. This gives resources, such as for ill-posed and generalized inverse problems, that Kolmogorov's system lacks (p. 50).

## Toy example
*(Ours, not from the text.)*

**1. Sum rule with different $m$.** Take $m=2$ and $w(A|B)=0.6$. The sum rule (2.58) gives $w(\bar A|B)=S(0.6)=(1-0.6^2)^{1/2}=(1-0.36)^{1/2}=\sqrt{0.64}=0.8$. Check self-reciprocity (2.46): $S(0.8)=(1-0.64)^{1/2}=\sqrt{0.36}=0.6$ ✓. Now $p=w^2$: $p(A)=0.36$ and $p(\bar A)=0.64$, and $0.36+0.64=1$ ✓ as in (2.64). A robot using $m=1$ with $w'(A)=0.36$ would get $w'(\bar A)=1-0.36=0.64$ and behave identically.

**2. Extended sum rule (2.66).** Fair die, $A$ = "even" $=\{2,4,6\}$, $B$ = "at least 4" $=\{4,5,6\}$. Then $P(A)=3/6$, $P(B)=3/6$, $P(AB)=P(\{4,6\})=2/6$. Formula: $P(A+B)=3/6+3/6-2/6=4/6$. Direct count: $A+B=\{2,4,5,6\}$ gives $4/6$ ✓.

**3. Weak syllogism (2.73).** Let $A\Rightarrow B$, $P(A|C)=0.2$, $P(B|C)=0.5$. Then $P(B|AC)=1$, so $P(A|BC)=0.2\times1/0.5=0.4$. Learning $B$ doubled the plausibility of $A$. Check (2.77): $P(AB)=0.2$, so $P(\bar AB)=0.5-0.2=0.3$ and $P(\bar A)=0.8$. Then $P(B|\bar AC)=0.3/0.8=0.375\le0.5$ ✓. Via (2.76): $0.5\times P(\bar A|BC)/P(\bar A|C)=0.5\times0.6/0.8=0.375$ ✓.

**4. Indifference (2.95), $n=3$.** Cyclic relabelling $A_1\to A_2\to A_3\to A_1$ gives $p_1=p_2=p_3$. With $p_1+p_2+p_3=1$, each is $1/3$.

## Concepts
- [[product-rule]] — $P(AB|C)=P(A|BC)P(B|C)$, forced by associativity of the logical product (p. 29, 33) (new)
- [[sum-rule]] — $P(A|B)+P(\bar A|B)=1$, forced by consistency of negation, plus the derived $P(A+B)=P(A)+P(B)-P(AB)$ (p. 33–34) (new)
- [[cox-theorem]] — derivation of the probability rules from desiderata via functional equations (p. 27–34) (new)
- [[functional-equation-associativity]] — $F[F(x,y),z]=F[x,F(y,z)]$ and its solution $F=w^{-1}[w(x)w(y)]$ (p. 27–28) (new)
- [[principle-of-indifference]] — equal probabilities $1/n$ when the information is symmetric between exclusive, exhaustive propositions (p. 40) (new)
- [[group-invariance-symmetry]] — equivalent states of knowledge must give equivalent assignments; the "baby" form of group invariance (p. 39–40) (new)
- [[finite-sets-policy]] — treat infinite sets only as limits of finite ones (p. 44) (new)
- [[probability-as-logic]] — probabilities as states of knowledge, with Aristotelian logic as the limiting case (p. 35, 44–45) (new)

## Canonical instances
- [[brown-blue-eyes-example]] — shows $F[(A|C),(B|C)]$ cannot give $AB|C$ (p. 25) (new)
- [[policeman-syllogism]] — weak syllogism of plausible reasoning, made quantitative by (2.73) (p. 36–37) (new)
- [[bernoulli-urn]] — ten balls, three black; $p(\text{black})=3/10$ (p. 42) (new)
- [[sams-broken-thermometer]] — mentioned only as a later scenario about useful resolution (p. 49) (new)

## Bridges (candidates)
- [structural-analogy] Product rule $w(AB)=w(A)w(B)$ turning multiplication into addition under a logarithm ↔ information-theory: additivity of surprisal for independent events — both reflect a multiplicative law made additive by $\log$.
- [structural-analogy] Principle of indifference (2.95) ↔ maximum entropy principle: the uniform distribution is the symmetric choice, and is also the entropy maximiser when only normalisation is known.
- [metaphor] Kelvin scale as the convenient scale among monotonic temperature scales (p. 42) ↔ choice of $p=w^m$ among monotonic plausibility scales — only the simplicity of the laws recommends it.
- [structural-analogy] Symmetry under relabelling forcing equal probabilities ↔ invariance arguments for noninformative priors (the chapter itself points ahead to Chapter 6, p. 40).

## Questions this raises
- The derivation assumes a real-number scale and differentiability. How much does Aczél's non-differentiable proof relax this, and what other scales (e.g. intervals) are excluded?
- The indifference argument requires information "indifferent" among propositions. How does one decide that, and what happens when different symmetries conflict?
- How would the derivation change for infinite sets, given the finite-sets policy?
- What other principles (beyond symmetry) turn information $B$ into numerical $p(A_i|B)$? Jaynes calls this open-ended (p. 38).

## Exercises worth doing
- Ex. 2.1 (p. 34) — can $p(C|A+B)$ be derived from the product and sum rules? Tests the grasp of what these rules determine — difficulty: medium
- Ex. 2.2 (p. 34) — show that conditioning on a disjunction of exclusive propositions gives a weighted average (2.67) — difficulty: medium
- Ex. 2.3 (p. 43) — bounds on conjunction and disjunction from $a=P(A|C)$ and $b=P(B|C)$; useful for error checking — difficulty: easy

## Reading notes
- The text layer loses overlines (negation bars) in many equations. I checked these against the page images, e.g. (2.38)–(2.43), (2.59), (2.65) and (2.70).
- Printed misprint, p. 31: the sentence after (2.44) says "(2.25) becomes a functional equation". It should refer to (2.40), since (2.25) is a different equation.
- p. 32: (2.49) lacks a closing parenthesis in its second term.
- p. 29, text after (2.33): the phrase "C implies A" should read "C implies $\bar A$"; the text layer drops the bar. (The same slip appears at (2.34).)
- Steps marked "(added step)" are ours. Jaynes writes (2.50)–(2.57) tersely.
- References to Aczél's book pages are omitted. The text only says the proof is long (p. 27).
- Ex. 2.2 is printed with an unclosed parenthesis in its left-hand side; the formula is copied as intended.
- (2.84) prints $P$ capital on two terms, which is a typographic inconsistency in the source (p. 38).
- The "Venn diagram" in 2.6.3 is described in words only, with no figure given in the text.