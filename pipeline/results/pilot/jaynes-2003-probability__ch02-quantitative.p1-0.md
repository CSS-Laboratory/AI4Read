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
If degrees of plausibility are real numbers that must agree with common sense and be consistent, the product rule and the sum rule are forced, and a symmetry argument then fixes the numerical values of probabilities.

## L1 — The gist (≤ 120 words)
Chapter 1 set three desiderata for a reasoning "robot": plausibilities are real numbers, they agree qualitatively with common sense, and they are consistent. This chapter deduces what follows. Consistency of the logical product forces the associativity functional equation, which gives the product rule. Consistency of negation forces a second functional equation, which gives the sum rule. Any monotonic rescaling of plausibility is allowed, so one can choose the scale $p$ that obeys the plain rules. Indifference between labels then forces $p=1/n$ for $n$ exclusive and exhaustive propositions. Aristotelian logic and the weak syllogisms drop out as special cases. The comments section answers objections about subjectivity, Gödel, Venn diagrams and Kolmogorov. (p. 24–50)

## L2 — Key ideas
- **Product rule from associativity.** The plausibility of $AB$ must be a function $F$ of $(B|C)$ and $(A|BC)$. Associativity of the logical product forces $F$ to satisfy $F[F(x,y),z]=F[x,F(y,z)]$. The solution is $w(AB|C)=w(A|BC)\,w(B|C)$ for some positive monotonic $w$ (p. 25–29).
- **Sum rule from consistency of negation.** Write $\bar A$ for "$A$ is false". Requiring that the product rule give the same answer for $AB$ and $B A$, with $\overline{A}$ expressed through a function $S$, gives the functional equation (2.45). Its only solution is $S(x)=(1-x^m)^{1/m}$ (p. 30–33).
- **The exponent $m$ is not a freedom.** Setting $p\equiv w^m$ gives $p(AB|C)=p(A|C)p(B|AC)$ and $p(A|B)+p(\bar A|B)=1$. This covers every choice allowed by the desiderata (p. 33–34).
- **The rules are complete.** The generalized sum rule $p(A+B|C)=p(A)+p(B)-p(AB)$ follows. Conjunction and negation generate all of Boolean algebra, so the rules suffice. For $n$ propositions, $2^n$ basic conjunctions give $2^{2^n}$ propositions (p. 34–35).
- **Logic and common sense are special cases.** The strong syllogisms are the limit of the rules at certainty. The weak syllogisms and the policeman's syllogism follow from the product rule. The rule also says when evidence is strong: only when $p(B|C)$ is small (p. 35–37).
- **Indifference gives numbers.** A permutation-symmetry argument shows that if information $B$ is indifferent between $n$ exclusive and exhaustive propositions, each gets $1/n$. The data fix $p$, not the original plausibility $x$ (p. 38–42).
- **Finite-sets policy.** The consistency theorems hold for finite sets of propositions. Infinite sets are allowed only as limits of finite ones, with the limiting process stated (p. 43–44).
- **Comments.** "Subjective" means "state of knowledge", and the interface desiderata make it objective. Gödel's theorem does not block the theory. The Venn diagram is a special-case illustration. The Kolmogorov axioms are derived here (p. 44–50).

## L3 — Walkthrough

### Opening (p. 24)
The desiderata are (I) representation of plausibility by real numbers, (II) qualitative correspondence with common sense, (III) consistency (p. 24). The chapter deduces the quantitative rules from them (p. 24).

### 2.1 The product rule (p. 24–30)

**Choosing the arguments of $F$.** To decide that $AB$ is true, the robot can first decide $B$ (plausibility $B|C$) and then $A$ given $B$ ($A|BC$). Or it can go in the other order ($A|C$, then $B|AC$) (p. 24). If $B$ is false, $AB$ is false whatever one knows about $A$. So once the robot has $B|C$ and $A|BC$, it does not need $A|C$ (p. 25). Equal values from the two orders is desideratum (IIIa) (p. 25). Hence
$$(AB|C)=F[(B|C),(A|BC)].\tag{2.1}$$

**A rejected alternative.** The form
$$(AB|C)=F[(A|C),(B|C)]\tag{2.2}$$
cannot satisfy desideratum (II). Example: "blue eyes" and "black hair" are both quite plausible, and both together are reasonably plausible. "Left eye blue" and "right eye brown" are each plausible, but both together are very implausible. A function of the two separate plausibilities cannot capture both cases (p. 25).

**Exhaustive check.** Define the numbers
$$u=(AB|C),\; v=(A|C),\; w=(B|AC),\; x=(B|C),\; y=(A|BC).\tag{2.3}$$
There are 11 ways to write $u$ as a function of two or more of $v,w,x,y$. Tribus (1969) found that all but two show qualitative violations of common sense in some extreme case. The survivors are $u=F(x,y)$ and $u=F(w,v)$ (p. 25–26).

**Monotonicity and continuity.** Suppose $C\to C'$ makes $B$ more plausible but leaves $A|BC$ unchanged:
$$B|C'>B|C,\tag{2.4}$$
$$A|BC'=A|BC.\tag{2.5}$$
Common sense then demands
$$AB|C'\ge AB|C,\tag{2.6}$$
with equality iff $A|BC$ means impossibility (p. 26). Likewise, if $B|C''=B|C$ (2.7) and $A|BC''>A|BC$ (2.8), then
$$AB|C''\ge AB|C,\tag{2.9}$$
with equality only if $B$ is impossible given $C$ (p. 26). $F$ must also be continuous, otherwise a tiny change in an input could cause a large jump in $AB|C$ (p. 26). Assuming differentiability (not necessary, per the author):
$$F_1(x,y)\equiv\partial F/\partial x\ge 0,\tag{2.10a}$$
with equality iff $y$ represents impossibility, and
$$F_2(x,y)\equiv\partial F/\partial y\ge 0,\tag{2.10b}$$
with equality only if $x$ represents impossibility. $F_i$ is the derivative with respect to the $i$-th argument (p. 26).

**Associativity.** Boolean algebra is associative: $ABC=(AB)C=A(BC)$. Treating $BC$ as one proposition:
$$(ABC|D)=F[(BC|D),(A|BCD)],\tag{2.11}$$
$$(ABC|D)=F\{F[(C|D),(B|CD)],(A|BCD)\}.\tag{2.12a}$$
Treating $AB$ as one proposition:
$$(ABC|D)=F[(C|D),(AB|CD)]=F\{(C|D),F[(B|CD),(A|BCD)]\}.\tag{2.12b}$$
These must agree, which gives the *associativity equation*
$$F[F(x,y),z]=F[x,F(y,z)].\tag{2.13}$$
This equation goes back to Abel (1826). Aczél (1966) solves it without differentiability in 11 pages (p. 256–267 of his book). The text follows R. T. Cox's (1961) shorter proof, which assumes differentiability (p. 27). The trivial solution $F=\text{const}$ violates (2.10) and is useless (p. 27).

**Solving (2.13).** Define
$$u\equiv F(x,y),\quad v\equiv F(y,z),\tag{2.14}$$
so the equation reads
$$F(x,v)=F(u,z).\tag{2.15}$$
Differentiating with respect to $x$ and $y$:
$$F_1(x,v)=F_1(u,z)F_1(x,y),\qquad F_2(x,v)F_1(y,z)=F_1(u,z)F_2(x,y).\tag{2.16}$$
Eliminating $F_1(u,z)$, with $G(x,y)\equiv F_2(x,y)/F_1(x,y)$:
$$G(x,v)F_1(y,z)=G(x,y).\tag{2.17}$$
The left side is independent of $z$. Equation (2.17) can also be written
$$G(x,v)F_2(y,z)=G(x,y)G(y,z).\tag{2.18}$$
Call the left sides of (2.17) and (2.18) $U$ and $V$. Then $\partial V/\partial y=\partial U/\partial z$, so $G(x,y)G(y,z)$ is independent of $y$. The most general such $G$ is
$$G(x,y)=r\,\frac{H(x)}{H(y)},\tag{2.19}$$
with $r$ a constant and $H$ arbitrary. Monotonicity gives $G>0$, so $r>0$ and $H$ does not change sign (p. 28). Then
$$F_1(y,z)=\frac{H(v)}{H(y)},\tag{2.20}$$
$$F_2(y,z)=r\,\frac{H(v)}{H(z)}.\tag{2.21}$$
Since $dv=F_1dy+F_2dz$,
$$\frac{dv}{H(v)}=\frac{dy}{H(y)}+r\frac{dz}{H(z)}.\tag{2.22}$$
Integrating,
$$w[F(y,z)]=w(v)=w(y)\,w^r(z),\tag{2.23}$$
$$w(x)\equiv\exp\Big\{\int^x\frac{dx}{H(x)}\Big\}.\tag{2.24}$$
The missing lower limit means $w$ has an arbitrary multiplicative factor (p. 28). Apply $w$ to (2.15) and use (2.23) again. This gives $w(x)w^r(v)=w(u)w^r(z)$ and then
$$w(x)\,w^r(y)\,[w(z)]^{r^2}=w(x)\,w^r(y)\,w^r(z).\tag{2.25}$$
This is nontrivial only if $r=1$. The result is
$$w[F(x,y)]=w(x)w(y),\tag{2.26}$$
$$F(x,y)=w^{-1}[w(x)w(y)].\tag{2.27}$$
(added step: $w^r(v)=w^r(y)w^{r^2}(z)$ and $w(u)=w(x)w^r(y)$ give the exponents $r^2$ and $r$ in (2.25).)

**The product rule.** Associativity and commutativity require
$$w(AB|C)=w(A|BC)\,w(B|C)=w(B|AC)\,w(A|C).\tag{2.28}$$
The function $w$ is positive, continuous and monotonic, increasing or decreasing according to the sign of $H$ (p. 29). The condition (2.28) is also sufficient: any expansion of $ABCDEFG|H$ by successive partitions gives the same result (p. 29).

**Range of $w$.** Suppose $A$ is certain given $C$. Then $AB$ and $B$ are equivalent, so
$$AB|C=B|C,\tag{2.29}$$
$$A|BC=A|C.\tag{2.30}$$
Equation (2.28) becomes
$$w(B|C)=w(A|C)w(B|C),\tag{2.31}$$
valid for any plausibility of $B$. Hence
$$\text{certainty is represented by } w(A|C)=1.\tag{2.32}$$
Suppose instead $A$ is impossible given $C$. Then
$$AB|C=A|C,\tag{2.33}$$
$$A|BC=A|C,\tag{2.34}$$
and (2.28) gives
$$w(A|C)=w(A|C)w(B|C).\tag{2.35}$$
So $w(A|C)$ is $0$ or $+\infty$. The value $-\infty$ is excluded, because by continuity $w(B|C)$ would then need negative values (p. 29–30). So $w$ either rises from 0 (impossible) to 1 (certain) or falls from $\infty$ to 1. The two options differ only by $w_2=1/w_1$, so the convention $0\le w\le1$ loses nothing (p. 30).

*Intuition note.* Consistency of "A and B" in either order leaves essentially one way to combine plausibilities: multiplication, after a suitable relabeling $w$ of the scale. The relabeling is a freedom of scale, not of content (p. 28–30).

### 2.2 The sum rule (p. 30–35)

**Setup.** Let $u\equiv w(A|B)$ and $v\equiv w(\bar A|B)$. Then
$$v=S(u),\tag{2.36}$$
with $S$ continuous, monotonic decreasing, $S(0)=1$, $S(1)=0$ (p. 30). The product rule holds for $AB$ and $A\bar B$:
$$w(AB|C)=w(A|C)w(B|AC),\tag{2.37}$$
$$w(A\bar B|C)=w(A|C)w(\bar B|AC).\tag{2.38}$$
Hence
$$w(AB|C)=w(A|C)S[w(\bar B|AC)]\ \text{(sic)}=w(A|C)\,S\!\left[\frac{w(A\bar B|C)}{w(A|C)}\right].\tag{2.39}$$
As printed, the middle term of (2.39) is $S[w(\bar B|AC)]$; the identity actually used is that (2.37)–(2.38) give $w(AB|C)=w(A|C)\,S[w(A\bar B|C)/w(A|C)]$ (p. 30; see Reading notes).

**Commutativity.** Since $w(AB|C)$ is symmetric in $A,B$:
$$w(A|C)\,S\!\left[\frac{w(A\bar B|C)}{w(A|C)}\right]=w(B|C)\,S\!\left[\frac{w(B\bar A|C)}{w(B|C)}\right].\tag{2.40}$$
Choose $\bar B=AD$ with $D$ arbitrary (2.41). Then
$$A\bar B=\bar B,\qquad B\bar A=\bar A,\tag{2.42}$$
$$w(A\bar B|C)=w(\bar B|C)=S[w(B|C)],\qquad w(B\bar A|C)=w(\bar A|C)=S[w(A|C)].\tag{2.43}$$
With $x\equiv w(A|C)$, $y\equiv w(B|C)$ (2.44), this becomes
$$x\,S\!\left[\frac{S(y)}{x}\right]=y\,S\!\left[\frac{S(x)}{y}\right],\qquad 0\le S(y)\le x,\ 0\le x\le1.\tag{2.45}$$
Setting $y=1$ gives
$$S[S(x)]=x,\tag{2.46}$$
so $S$ is its own inverse. This is the evident reciprocity between $A$ and $\bar A$ (p. 31). (added step: with $y=1$, $S(1)=0$, so the left side is $xS(0)=x$ and the right side is $S[S(x)]$.)

**Domain.** The proposition $D$ is arbitrary, so
$$0\le w(D|AC)\le1.\tag{2.47}$$
Since $S(y)=w(AD|C)=w(A|C)w(D|AC)$, (2.47) is exactly $0\le S(y)\le x$. Geometrically the domain is the unit square on or above the curve $y=S(x)$ (p. 31).

**Shape of $S$.** Set $y=S(x)+\epsilon$ and let $\epsilon\to0^+$. Everything depends on how $S(1-\delta)\to0$ as $\delta\to0$ (p. 31–32). Define $q$ by
$$\frac{S(x)}{y}=1-\exp\{-q\},\tag{2.48}$$
let $\delta=e^{-q}$, and define $J$ by
$$S(1-\delta)=S(1-e^{-q})=\exp\{-J(q)\}.\tag{2.49}$$
The goal is the asymptotic form of $J(q)$ as $q\to\infty$. With $x,q$ as the independent variables,
$$S(y)=S[S(x)]+e^{-q}S(x)S'[S(x)]+O(e^{-2q}).\tag{2.50}$$
Using (2.46) and $S'[S(x)]S'(x)=1$, this becomes
$$\frac{S(y)}{x}=1-\exp\{-(\alpha+q)\}+O(e^{-2q}),\tag{2.51}$$
$$\alpha(x)\equiv\log\!\left[\frac{-xS'(x)}{S(x)}\right]>0.\tag{2.52}$$
Equation (2.45) becomes
$$J(q+\alpha)-J(q)=\log\!\left[\frac{x}{S(x)}\right]+\log(1-e^{-q})+O(e^{-2q}),\qquad 0<q<\infty,\ 0<x\le1.\tag{2.53}$$
(added step: in (2.45), $S(x)/y=1-e^{-q}$ and $S(y)/x=1-e^{-(\alpha+q)}$, so the equation reads $x\,e^{-J(q+\alpha)}=y\,e^{-J(q)}$ with $y=S(x)/(1-e^{-q})$.) The last two terms vanish exponentially as $q\to\infty$, so $J$ is asymptotically linear:
$$J(q)\sim a+bq+O(e^{-q}),\tag{2.54}$$
$$b=\alpha^{-1}\log\!\left[\frac{x}{S(x)}\right]>0.\tag{2.55}$$
There is no periodic term of period $\alpha$, because (2.53) holds for a continuum of $x$ and so of $\alpha(x)$. $J$ depends only on $q$, so the right side of (2.55) cannot depend on $x$. Using (2.52),
$$\frac{x}{S(x)}=\left[\frac{-xS'(x)}{S(x)}\right]^b,\qquad 0<b<\infty,\tag{2.56}$$
which is the differential equation
$$S^{m-1}dS+x^{m-1}dx=0,\qquad m\equiv1/b>0.\tag{2.57}$$
With $S(0)=1$ the only solution is
$$S(x)=(1-x^m)^{1/m},\qquad 0\le x\le1,\ 0<m<\infty,\tag{2.58}$$
and one checks directly that (2.58) solves (2.45) (p. 32–33). It automatically satisfies $S(1)=0$ (p. 33). (added step: integrating (2.57) gives $S^m+x^m=\text{const}=1$.)

**History.** Cox (1946) derived (2.58) by another argument that assumed $S$ twice differentiable. Aczél derived it without differentiability. The author calls assuming differentiability "very innocuous": a non-differentiable $S$ would itself be a qualitative violation of common sense (p. 33).

**Sufficiency.** Since the special choice (2.41) was used, (2.58) so far is only necessary. Substituting (2.58) into (2.40) gives
$$w^m(A|C)-w^m(AB|C)... $$
as printed:
$$w^m(A|C)-w^m(A\bar B|C)=w^m(B|C)-w^m(B\bar A|C),\tag{2.59}$$
which is a trivial identity by (2.28) and (2.38). So (2.58) is necessary and sufficient for the consistency condition (2.40) (p. 33).

**The two rules together.**
$$w^m(A|B)+w^m(\bar A|B)=1\tag{2.60}$$
for some $m>0$. The product rule can be raised to the power $m$:
$$w^m(AB|C)=w^m(A|C)w^m(B|AC)=w^m(B|C)w^m(A|BC).\tag{2.61}$$
So $m$ is irrelevant. Define
$$p(x)\equiv w^m(x),\tag{2.62}$$
which gives
$$p(AB|C)=p(A|C)p(B|AC)=p(B|C)p(A|BC),\tag{2.63}$$
$$p(A|B)+p(\bar A|B)=1.\tag{2.64}$$
There is no loss of generality. If $w$ is continuous, monotonic increasing and ranges from 0 to 1, so is $w^m$. Allowing different $m$ gives no freedom beyond the arbitrariness of $w$ already present. Everything is contained in (2.63)–(2.64), with $p$ any continuous monotonic increasing function with $0\le p\le1$ (p. 33–34).

*Intuition note.* The sum rule is not an extra axiom. Requiring that "$A$ and not-$B$" be handled consistently with "$A$ and $B$" pins the negation function down to $S(x)=(1-x^m)^{1/m}$, and a change of scale turns that into $p+\bar p=1$ (p. 30–34).

**Completeness.** Conjunction and negation are an adequate set of operations for all logic functions (discussion after (1.23)). So repeated use of (2.63)–(2.64) should give the plausibility of any proposition in the Boolean algebra (p. 34). For the logical sum:
$$p(A+B|C)=1-p(\bar A\bar B|C)=1-p(\bar A|C)p(\bar B|\bar AC)$$
$$=1-p(\bar A|C)[1-p(B|\bar AC)]=p(A|C)+p(\bar AB|C)$$
$$=p(A|C)+p(B|C)p(\bar A|BC)=p(A|C)+p(B|C)[1-p(A|BC)]\tag{2.65}$$
and finally the generalized sum rule
$$p(A+B|C)=p(A|C)+p(B|C)-p(AB|C).\tag{2.66}$$
The primitive sum rule (2.64) is the special case $B=\bar A$ (p. 34).

*Exercise 2.1* (p. 34) asks whether a formula for $p(C|A+B)$ analogous to (2.66) exists. *Exercise 2.2* (p. 34) asks to show, for mutually exclusive $A_i$ given $X$, that $p(C|(A_1+\dots+A_n)X)$ is a weighted average:
$$p(C|(A_1+\cdots+A_n)X)=\frac{\sum_ip(A_i|X)p(C|A_iX)}{\sum_ip(A_i|X)}.\tag{2.67}$$

**Disjunctive normal form.** Any logic function other than the trivial contradiction is a logical sum of the $2^n$ basic conjunctions $Q_i$. Each $Q_i$ is evaluated by the product rule, and the sum by (2.66). Because the $Q_i$ are mutually exclusive, this reduces to a simple sum of at most $2^n-1$ terms (see (2.85)) (p. 34–35). If the background information fixes the plausibilities of the basic conjunctions, the rules determine every proposition in the algebra. For $n=4$: $2^4=16$ basic conjunctions determine $2^{16}=65\,536$ propositions. Real applications usually need only a small part (p. 35).

### 2.3 Qualitative properties (p. 35–37)

**Strong syllogisms.** As $p(A|B)\to0$ or $1$, the sum rule gives the Aristotelian postulate that if $A$ is true, $\bar A$ is false (p. 35). Write the strong syllogisms as
$$A\Rightarrow B,\ A\text{ true}\ \therefore B\text{ true};\qquad A\Rightarrow B,\ B\text{ false}\ \therefore A\text{ false}\tag{2.68}$$
and let
$$C\equiv A\Rightarrow B.\tag{2.69}$$
The product rule gives
$$p(B|AC)=\frac{p(AB|C)}{p(A|C)},\qquad p(A|\bar BC)=\frac{p(A\bar B|C)}{p(\bar B|C)}.\tag{2.70}$$
From (2.68), $p(AB|C)=p(A|C)$ and $p(A\bar B|C)=0$, so
$$p(B|AC)=1,\qquad p(A|\bar BC)=0.\tag{2.71}$$
Thus deductive logic is the limiting form of the rules as the robot becomes certain (p. 35).

**Weak syllogisms.** The first weak syllogism is "$A\Rightarrow B$; $B$ true; therefore $A$ becomes more plausible" (2.72). The product rule gives
$$p(A|BC)=p(A|C)\frac{p(B|AC)}{p(B|C)}.\tag{2.73}$$
Here $p(B|AC)=1$ and $p(B|C)\le1$, so
$$p(A|BC)\ge p(A|C).\tag{2.74}$$
The second is "$A\Rightarrow B$; $A$ false; therefore $B$ becomes less plausible" (2.75):
$$p(B|\bar AC)=p(B|C)\frac{p(\bar A|BC)}{p(\bar A|C)}.\tag{2.76}$$
From (2.74), $p(\bar A|BC)\le p(\bar A|C)$, so
$$p(B|\bar AC)\le p(B|C).\tag{2.77}$$
The policeman's syllogism has major premise
$$p(B|AC)>p(B|C),\tag{2.78}$$
and (2.73) gives at once
$$p(A|BC)>p(A|C).\tag{2.79}$$
(p. 36)

**How strong is the evidence?** From (2.73), since $p(B|AC)\le1$, a large rise in $A$ is possible only when $p(B|C)$ is very small. The gentleman's behavior makes guilt nearly certain because that behavior is otherwise very unlikely. If $A$ barely raises $B$, then observing $B$ barely raises $A$ (p. 36–37). Many writers have shown the full qualitative correspondence: Keynes, Jeffreys, Pólya, Cox, Tribus, de Finetti, Rosenkrantz (p. 37).

*Intuition note.* The product rule is Bayes' rule in disguise (2.73): the evidence for $A$ is the ratio $p(B|AC)/p(B|C)$, and surprising evidence moves belief most (p. 36–37).

### 2.4 Numerical values (p. 37–43)

Two gaps remain. There seems to be a different rule set for each monotonic $p(x)$. And nothing says which numbers to assign initially. For the second, the interface desiderata (IIIb), (IIIc) are needed (p. 37).

**Mutually exclusive propositions.** For the sum of three:
$$p(A_1+A_2+A_3|B)=p(A_1+A_2|B)+p(A_3|B)-p(A_1A_3+A_2A_3|B),\tag{2.80}$$
using
$$(A_1+A_2)A_3=A_1A_3+A_2A_3.\tag{2.81}$$
A second use of (2.66) gives seven terms:
$$p(A_1+A_2+A_3|B)=p(A_1|B)+p(A_2|B)+p(A_3|B)-p(A_1A_2|B)-p(A_2A_3|B)-p(A_3A_1|B)+p(A_1A_2A_3|B).\tag{2.82}$$
Assume mutual exclusion:
$$p(A_iA_j|B)=p(A_i|B)\delta_{ij}.\tag{2.83}$$
The last four terms vanish, leaving
$$p(A_1+A_2+A_3|B)=p(A_1|B)+p(A_2|B)+p(A_3|B).\tag{2.84}$$
By induction, for $n$ mutually exclusive propositions,
$$p(A_1+\cdots+A_m|B)=\sum_{i=1}^mp(A_i|B),\qquad 1\le m\le n.\tag{2.85}$$
Conventional texts take (2.85) as an arbitrary axiom. Here it is derived (p. 37–38). If the set is also exhaustive,
$$\sum_{i=1}^np(A_i|B)=1.\tag{2.86}$$
This alone does not fix the individual values. Finding $p(A_i|B)$ from complicated information $B$ is an open-ended research problem, and each new principle opens a new class of applications (p. 38).

**The symmetry argument.** The author warns that intuition has led to conflicting views for about 150 years and asks the reader to follow only the logic (p. 38–39). Problem I: evaluate $p(A_i|B)_I$ for exclusive and exhaustive $\{A_1,\dots,A_n\}$. Problem II: the labels of the first two are swapped,
$$A_1'\equiv A_2,\quad A_2'\equiv A_1,\quad A_k'\equiv A_k\ (3\le k\le n).\tag{2.87}$$
The robot's knowledge of $A_1$ in I equals its knowledge of $A_2'$ in II (same proposition, same $B$). So the transformation equations hold:
$$p(A_1|B)_I=p(A_2'|B)_{II},\tag{2.88}$$
$$p(A_2|B)_I=p(A_1'|B)_{II}.\tag{2.89}$$
These hold for any $B$ (p. 39). Now let $B$ be indifferent between $A_1$ and $A_2$. Then I and II are equivalent states of knowledge, including labeling. Desideratum (IIIc) (equivalent states give equivalent assignments) gives the symmetry equations
$$p(A_i|B)_I=p(A_i'|B)_{II},\qquad i=1,\dots,n.\tag{2.90}$$
Combining (2.88)–(2.90):
$$p(A_1|B)_I=p(A_2|B)_I.\tag{2.91}$$
This is a "baby" version of the group invariance principle, extended in Chapter 6 to noninformative priors (p. 39–40).

**General permutation.** Let $\{A_1'',\dots,A_n''\}$ be any permutation, with $A_k''\equiv A_i$ (Problem III). Then
$$p(A_i|B)_I=p(A_k''|B)_{III}.\tag{2.92}$$
If $B$ is indifferent to all $A_i$,
$$p(A_k|B)_I=p(A_k''|B)_{III},\qquad k=1,\dots,n.\tag{2.93}$$
Hence
$$p(A_i|B)_I=p(A_k|B)_I.\tag{2.94}$$
With $n!$ permutations, $k$ ranges over all other indices, so all values are equal (a single cyclic permutation of order $n$ already suffices). With (2.86):
$$p(A_i|B)_I=\frac1n,\qquad 1\le i\le n.\tag{2.95}$$
Following Keynes (1921) this is the *principle of indifference* (p. 40).

**Uniqueness and importance.** Any other assignment could be contradicted by a relabeling that exhibits the same knowledge with different numbers (p. 41). More importantly, the information fixes the values of $p=p(A_i|B)$, not those of the original $x=A_i|B$. So the freedom in $p(x)$ is only a choice of internal representation. The robot could store any strictly monotonic function of $p_i$ without changing its external behavior. The correct statement is therefore:

> "The plausibility $x\equiv A|B$ is an arbitrary monotonic function of $p$." (p. 41)

Only one consistent rule set remains, and the $p$ are now called *probabilities* (p. 41–42).

**Why this scale.** $p$ is chosen because it obeys the simplest rules, not because it is more correct. The author compares the Kelvin scale, which makes thermodynamic laws simplest (e.g. $dU=TdS-PdV$, $dG=-SdT+VdP$) and is fixed independently of any substance (p. 42).

**Urn example.** An urn holds ten balls labeled $1,\dots,10$. Balls 4, 6, 7 are black, the rest white. $A_i\equiv$ "ball $i$ is drawn". By (2.95),
$$p(A_i|B)=\frac1{10},\quad1\le i\le10.\tag{2.96}$$
Then
$$p(\text{black}|B)=p(A_4+A_6+A_7|B),\tag{2.97}$$
and by (2.85)
$$p(\text{black}|B)=\frac3{10}.\tag{2.98}$$
For $N$ balls and a proposition true on a subset of $M$,
$$p(A|B)=\frac MN.\tag{2.99}$$
This was Bernoulli's (1713) definition of probability, used for about 150 years. Laplace's *Théorie Analytique* (1812) opens with it (p. 42–43).

*Intuition note.* Symmetry of information, not an extra axiom, produces the first numbers. And the numbers belong to the rescaled $p$, which is why different plausibility scales do not give different theories (p. 40–42).

*Exercise 2.3* (p. 43): given $a=P(A|C)\le b=P(B|C)$, show $0\le P(AB|C)\le a$ and $b\le P(A+B|C)\le1$, with stronger bounds when $a+b>1$ (conjunction) or $a+b<1$ (disjunction).

### 2.5 Notation and finite-sets policy (p. 43–44)
Formal probability symbols use capital $P$ with propositions as arguments (2.100), e.g. $P(A|B)$. Functions of numerical values use other symbols, e.g. $f(r|np)$ (2.101). Small-$p$ notation may mix arguments, and the meaning is then read from context (p. 43). The consistency theorems are established only for finite sets of propositions. Extension to infinite sets is permitted only as a well-behaved limit of finite sets (p. 43). The *finite-sets policy* is:

> Apply the ordinary processes of arithmetic and analysis only to expressions with a finite number of terms; then observe how results behave as the number of terms grows (paraphrase, p. 44).

The author says this agrees with Lebesgue's original definition of measure. The danger is that measure-theory notation presupposes the limit and does not record which limiting process was used. Different well-behaved limiting processes can give different results. Chapter 15 on infinite-set paradoxes will show the consequences (p. 44).

### 2.6 Comments (p. 44–50)

**2.6.1 "Subjective" vs. "objective" (p. 44–45).** Any probability assignment is "subjective" in that it describes only a state of knowledge, not something measurable in an experiment. Whose state? That of the robot, or anyone given the same information who reasons by the same desiderata. A person who gets a different answer violates a desideratum. The interface desiderata (IIIb), (IIIc) make assignments "objective": independent of the user's personality and feelings, and a way of encoding the given information (p. 44–45).

**2.6.2 Gödel's theorem (p. 45–47).** The desideratum (IIIa) determined the rules. This does not prove the rules consistent. It shows only that any other number-based rules that differ in content lead to inconsistency or to violation of other desiderata (p. 45). "Inconsistency" here means deriving contradictory values, e.g. $P(A|BC)=1/3$ and $2/3$ for the same quantity. A logician means deducing $Q$ and $\bar Q$; these are not really different (p. 45). A contradiction implies every proposition: since $A\Rightarrow(A+B)$, we get $\bar AA\Rightarrow\bar A(A+B)=\bar AA+\bar AB\Rightarrow B$ (p. 45). Let $\mathcal A=\{A_1,\dots,A_n\}$ be the axioms and $T$ a theorem:
$$\mathcal A\Rightarrow T.\tag{2.102}$$
Deducing $T$ cannot prove consistency, because a contradiction would also yield $T$. This is Fisher's (1956) intuitive reason for Gödel's result, not a proof of the full theorem (p. 45–46). If the axioms are inconsistent, then also
$$\mathcal A\Rightarrow\bar T.\tag{2.103}$$
Consistency would be provable by a procedure guaranteed to find an inconsistency if one exists. Gödel's theorem says only that no such procedure derivable from the axioms being tested exists (p. 46). Probabilities conditional on contradictory premises do not exist (the hypothesis space is empty). So a program computing $p(B|E_1E_2\dots E_n)$ crashes if a contradiction is hidden in $E$. If it prints valid numbers, the $E_i$ are consistent. This uses principles external to the tested propositions, so there is no conflict with Gödel (p. 46). Undecidability simply signals missing information. The example is two sole witnesses who give opposite testimony and then die: one lied, but which one cannot be decided (p. 46–47). The author sees "undecidability" as marking problems that need inference rather than deduction. He calls consistency of the rules from outside principles an open question. No inconsistency has ever been found from correct application, while ad hoc rules in the literature are easily shown inconsistent (p. 47).

**2.6.3 Venn diagrams (p. 47–49).** The Venn diagram illustrates
$$P(A+B|C)=P(A|C)+P(B|C)-P(AB|C)\tag{2.104}$$
in one special case. But it suggests that propositions are sets of points $\omega_i$, that $A+B$ is a union, $AB$ an intersection, and probability an additive measure. The general theory has no such structure (p. 47–48). Propositions such as
$$A\equiv\text{it will rain today},\tag{2.105}$$
$$B\equiv\text{the roof will leak}\tag{2.106}$$
need not be resolvable into elementary propositions. One can force resolution with irrelevancies, e.g. penguins:
$$B=BC_1+BC_2+\cdots+BC_N,\tag{2.107}$$
with $C_k\equiv$ "the number of penguins in Antarctica is $k$". This is valid but useless (p. 48). Even a meaningful resolution (raindrop trajectories) may not help. A resolution is sometimes useful, as in (2.98). A and B would seldom be resolvable into the same set of $\omega_i$, and enlarging the context with $D,E,F,\dots$ would break any fixed set (p. 48–49). So $AB$ means only "both true", and $p(AB|C)$ is an elementary quantity. Boole's notation $A+B$, $AB$ is kept to avoid set-theory associations. The author prefers to say that (2.104) justifies the Venn diagram in one special case, not the reverse. Sam's broken thermometer (Chapter 8) will show where resolution matters (p. 49).

**2.6.4 The "Kolmogorov axioms" (p. 49–50).** In 1933 Kolmogorov phrased probability in set and measure theory, formalizing the Venn picture (p. 49). The four axioms, stated arbitrarily by him, are derived here as necessary for consistency; Appendix A shows this (p. 49). The author contrasts Haar measure replacing "Hurwitz invariant integral" as an example of naming by restatement (p. 49). Conceptually, this system does not interpret propositions as sets, but interprets distributions as carriers of incomplete information. It therefore handles "ill posed" and "generalized inverse" problems, which the Kolmogorov system would place outside probability theory (p. 50).

## Toy example (ours)
A fair die has six equally likely faces (principle of indifference, (2.95): each $1/6$). Let $A$ = "even" $=\{2,4,6\}$, $B$ = "at least 4" $=\{4,5,6\}$.

- $P(A)=3/6=1/2$, $P(B)=3/6=1/2$, $AB=\{4,6\}$, so $P(AB)=2/6=1/3$. By (2.85) these are sums of $1/6$ terms.
- Product rule (2.63): $P(B|A)=P(AB)/P(A)=(1/3)/(1/2)=2/3$. Check: $P(A)P(B|A)=\tfrac12\cdot\tfrac23=\tfrac13$.
- Generalized sum rule (2.66): $P(A+B)=\tfrac12+\tfrac12-\tfrac13=\tfrac23$. Direct count: $A+B=\{2,4,5,6\}$, $4/6=2/3$. ✓.
- Rule (2.73): $P(A|B)=P(A)\,P(B|A)/P(B)=\tfrac12\cdot\tfrac23\big/\tfrac12=\tfrac23$. Direct count: $\{4,6\}$ of $\{4,5,6\}$ is $2/3$. ✓.
- Weak syllogism: let $A'$ = "shows 6", $B'$ = "even", so $A'\Rightarrow B'$. Then $P(A')=1/6$ and $P(B')=1/2$. By (2.73), $P(A'|B')=\tfrac16\cdot1/\tfrac12=\tfrac13\ge\tfrac16$. ✓. The jump is a factor 2 $=1/P(B')$, the largest the evidence could give only if $P(B')$ were smaller.
- Ex. 2.3 bounds: $a=b=1/2$, $a+b=1$, so $0\le P(AB)\le1/2$ and $1/2\le P(A+B)\le1$. Our values $1/3$ and $2/3$ lie inside.
- Scale freedom: take $m=2$ and $w=\sqrt p$. Then $w(A)=w(\bar A)=\sqrt{1/2}$, and $w^2(A)+w^2(\bar A)=1/2+1/2=1$, as (2.60) requires. Squaring $w$ returns $p$, so the content is identical.

## Concepts
- [[product-rule]] — $P(AB|C)=P(A|C)P(B|AC)$, forced by associativity of conjunction (p. 29, 33) (new)
- [[sum-rule]] — $P(A|B)+P(\bar A|B)=1$, and generalized $P(A+B)=P(A)+P(B)-P(AB)$ (p. 33–34) (new)
- [[cox-theorem]] — derivation of probability rules from desiderata via functional equations (p. 27–34) (new)
- [[associativity-equation]] — $F[F(x,y),z]=F[x,F(y,z)]$ (p. 27) (new)
- [[principle-of-indifference]] — equal probabilities $1/n$ when information is symmetric over labels (p. 40) (new)
- [[probability-as-extended-logic]] — probabilities as a state of knowledge; deductive logic is the limit of certainty (p. 35, 44) (new)
- [[finite-sets-policy]] — compute with finite expressions, then take limits (p. 44) (new)
- [[bayes-theorem]] — the product-rule form (2.73) $p(A|BC)=p(A|C)p(B|AC)/p(B|C)$ (p. 36) (new)
- [[kolmogorov-axioms]] — set/measure-theory axiomatization, here derived from consistency (p. 49) (new)
- [[self-information]] — see Bridges; not in the chapter, only possibly related via the scale freedom (p. 41)

## Canonical instances
- [[bernoulli-urn]] — 10 balls, 3 black, $P(\text{black})=3/10$; Bernoulli/Laplace definition $M/N$ (p. 42–43)
- [[policeman-syllogism]] — weak evidence reasoning follows from (2.73); strength depends on $p(B|C)$ (p. 36–37)
- [[blue-brown-eyes]] — why $F[(A|C),(B|C)]$ cannot work (p. 25)
- [[two-witnesses-undecidable]] — undecidability as missing information (p. 47)
- [[kelvin-scale-analogy]] — choosing $p$ like choosing the Kelvin scale (p. 42)
- [[penguin-resolution]] — a pointless resolution of $B$ into elementary propositions (p. 48)

## Bridges (candidates)
- [same-math] Product rule $p(AB|C)=p(A|C)p(B|AC)$ ↔ information theory: chain rule for surprisal, $-\log p(AB)=-\log p(A)-\log p(B|A)$, which becomes $H(X,Y)=H(X)+H(Y|X)$ on averaging — the same equation after taking logs.
- [structural-analogy] Rescaling $w\mapsto w^m$ leaves content unchanged ↔ information theory: choice of log base (bit vs. nat) — both are a free monotone/scale choice that does not change the content.
- [structural-analogy] Symmetry argument for $p=1/n$ ↔ information theory: maximum entropy (uniform distribution when no constraint beyond normalization) — both are "choose the least committal assignment"; the chapter itself does not mention entropy.
- [structural-analogy] Associativity equation giving $w(x)w(y)$ ↔ information theory: additivity of information from logs of products; solutions of functional equations pin down logarithmic measures.
- [metaphor] Kelvin scale vs. other temperature scales ↔ probability scale vs. other plausibility scales — the author's own analogy (p. 42).
- [structural-analogy] $P(A|B)$ as a state of knowledge about a labeled outcome ↔ information theory: entropy as uncertainty about a source given the observer's knowledge.

## Questions this raises
- If the exponent $m$ is arbitrary, is there a natural reason to prefer $\log p$ as a scale (it is additive for products)? How does that relate to bits?
- The principle of indifference needs $B$ to be "indifferent" among labels. What rules exist for assigning numbers when $B$ is not symmetric (the author calls this an open-ended research problem, p. 38)?
- How exactly does the finite-sets policy change results in cases where naive measure-theoretic limits are ambiguous (Chapter 15)?
- How does the crash-on-contradiction test work in practice, and what does it say about probabilities conditional on a measure-zero event?

## Exercises worth doing
- Ex. 2.1 (p. 34) — whether a formula for $p(C|A+B)$ exists; tests understanding of what the product and sum rules can determine — difficulty: medium
- Ex. 2.2 (p. 34) — shows $p(C|(A_1+\dots+A_n)X)$ is a weighted average (2.67); a result used constantly for mutually exclusive hypotheses — difficulty: medium
- Ex. 2.3 (p. 43) — bounds on conjunction and disjunction from $a,b$; useful as an error check in calculations — difficulty: easy

## Reading notes
- The text layer loses overbars (negation) in many places. Checked against the images (pp. 25–35, 45–46): e.g. $A\bar B$, $\bar B C$, $\bar A$. The images were used to restore them.
- p. 31: the text says "(2.25) becomes a functional equation" before (2.45). This should refer to (2.40); looks like a misprint in the source.
- p. 30: in (2.39) the middle expression $S[w(\bar B|AC)]$ is correct by (2.38) and (2.36); the final fraction is $w(A\bar B|C)/w(A|C)$. The text has $\bar A\bar B$ lost in places; no change of meaning.
- p. 29–30: the phrases "(i.e. $C$ implies $\bar A$)" and similar lose bars in the text layer, but the page image shows them.
- p. 38: (2.84) uses capital $P$ for some terms and small $p$ for others; a notational inconsistency, not a mathematical error. Capitalization in "formal probability Symbols" on p. 43 looks like an OCR/typo.
- p. 45: the contradictory-result example prints $P(A|BC)=1/3$ and $P(A|BC)=2/3$; the second probably should show a bar or differ in conditioning. The meaning (two incompatible values for the same quantity) is clear.
- The Venn diagram on p. 47 is described in words only (no figure was included in the pages I received).
- Intermediate steps in the derivation of (2.50)–(2.58) are partly marked "(added step)"; the author gives only the key results.
- Appendix A, Appendix B, Chapters 6, 8, 15 are referred to but are not part of this unit.