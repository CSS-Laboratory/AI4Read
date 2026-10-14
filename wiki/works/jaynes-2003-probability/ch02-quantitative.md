---
id: jaynes-2003-probability/ch02-quantitative
work: jaynes-2003-probability
unit: "2 The quantitative rules"
pages: 24–50
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
audited: 2026-10-14
audit_fixes: 4
---
# The quantitative rules (Jaynes, ch. 2)

## L0 — One line
If degrees of plausibility are real numbers that match common sense and are consistent, then a monotonic function of them must obey the product rule and the sum rule; rescaled to an ordinary probability, it is fixed by the data (for indifferent cases, to $1/n$).

## L1 — The gist (≤ 120 words)
The chapter asks which numerical rules a reasoning robot must use if it stores plausibilities as real numbers, agrees qualitatively with common sense, and is consistent. Jaynes derives, from the associativity of "and" and from the relation between A and not-A, a product rule and a sum rule. Every acceptable plausibility scale can be rescaled to a probability $p$ obeying these rules. A symmetry (relabelling) argument then gives probability $1/n$ to $n$ exhaustive, mutually exclusive propositions on which the information is indifferent. The chapter closes with comments on "subjective" versus "objective", Gödel's theorem, Venn diagrams and Kolmogorov's axioms.

**Prerequisites:** Boolean algebra (and, or, not, implication); basic calculus (partial derivatives, integration, asymptotics); what a functional equation is; Chapter 1's desiderata (I)–(III).

## L2 — Key ideas (5–10 bullets)
- Consistency of the plausibility of a conjunction $AB$ under the two orders of reasoning (via associativity) forces a product rule $w(AB|C)=w(A|BC)\,w(B|C)$ for some positive monotonic function $w$ (pp. 25–29).
- Common sense fixes the end-points of $w$: certainty is 1, and impossibility is 0 (or $\infty$, an equivalent convention). The choice $0\le w\le1$ loses no generality (pp. 29–30).
- Consistency of the product rule applied to $AB$ and $A\bar B$ forces $w^m(A|B)+w^m(\bar A|B)=1$ with $m>0$. Setting $p=w^m$ gives the usual product and sum rules (2.63)–(2.64), and the extended sum rule (2.66) follows (pp. 30–34).
- These rules suffice for every proposition in the Boolean algebra, once the basic conjunctions are given plausibilities. Deductive logic is their limiting case. The weak syllogisms, including the policeman's, follow from the product rule (pp. 34–37).
- A permutation-symmetry argument gives $P(A_i|B)=1/n$ when $B$ is indifferent among $n$ exclusive, exhaustive propositions. The data fix $p$, not the original plausibility $x$, so the rules are unique (pp. 38–42).
- Notation uses capital $P$ for propositions. The consistency theorems have been established only for finite sets, hence the finite-sets policy for infinite problems (pp. 43–44).
- Jaynes's comments (pp. 44–50):
  - Probabilities are "subjective" in describing a state of knowledge, yet "objective" in not depending on the user.
  - Gödel's theorem is not treated as an obstacle, because the consistency-testing argument appeals to principles outside the propositions tested; whether consistency can be proved from outside probability theory is left open.
  - A Venn diagram illustrates the extended sum rule only in one special case; for practical purposes Kolmogorov's axioms are derived in this chapter, but his set-based interpretation of propositions is not adopted.

## L3 — Walkthrough

Epigraph: Laplace, "Probability theory is nothing but common sense reduced to calculation" (p. 24). The chapter deduces quantitative rules from the desiderata: (I) plausibilities are real numbers; (II) qualitative correspondence with common sense; (III) consistency (p. 24).

### 2.1 The product rule

**Which arguments should the rule use? (pp. 24–25).** To decide that $AB$ is true, the robot can:
1. decide $B$ is true, with plausibility $(B|C)$;
2. then decide $A$ is true given $B$, with plausibility $(A|BC)$.

The reverse order uses $(A|C)$ and $(B|AC)$. If $B$ is false, $AB$ is false whatever is known about $A$. So with $B|C$ and $A|BC$ the robot does not need $A|C$ (p. 25). Information the robot would have if it did not know $C$ is irrelevant once $C$ is known (the earth-is-round example, p. 25). Requiring the same value from both orders is desideratum (IIIa) (p. 25). So

$$(AB|C)=F[(B|C),(A|BC)].\tag{2.1}$$

**Rejected alternative (p. 25).** A form $(AB|C)=F[(A|C),(B|C)]$, eq. (2.2), cannot satisfy desideratum (II). $A$ and $B$ can each be quite plausible while $AB$ is plausible or implausible. Examples: blue eyes and black hair (reasonably plausible together); left eye blue and right eye brown (each plausible, both together extremely implausible).

**Proof by exhaustion (pp. 25–26).** Define
$$u=(AB|C),\; v=(A|C),\; w=(B|AC),\; x=(B|C),\; y=(A|BC).\tag{2.3}$$
Expressing $u$ as a function of two or more of $v,w,x,y$ gives 11 possibilities. Tribus (1969) finds that all but two can show qualitative violations of common sense in some extreme case. The survivors are $u=F(x,y)$ and $u=F(w,v)$, the two forms already argued for (p. 26).

**Monotonicity and continuity (p. 26).** Suppose $C\to C'$ makes $B$ more plausible but leaves $A|BC$ unchanged, i.e. $B|C'>B|C$ (2.4) and $A|BC'=A|BC$ (2.5). Common sense demands $AB|C'\ge AB|C$ (2.6), with equality iff $A|BC$ is impossibility. Likewise, if $B|C''=B|C$ (2.7) and $A|BC''>A|BC$ (2.8), then $AB|C''\ge AB|C$ (2.9). Here equality can hold only if $B$ is impossible given $C$. $F$ must also be continuous, otherwise a tiny change in an input could cause a large change in $AB|C$. If $F$ is differentiable (not necessary, see below):
$$F_1(x,y)\equiv\partial F/\partial x\ge0\tag{2.10a}$$
with equality iff $y$ represents impossibility, and
$$F_2(x,y)\equiv\partial F/\partial y\ge0\tag{2.10b}$$
with equality permitted only if $x$ represents impossibility. $F_i$ denotes differentiation with respect to the $i$th argument (p. 26).

**Associativity equation (p. 27).** Boolean algebra is associative, $ABC=(AB)C=A(BC)$, so the rule must give the same value either way. Treating $BC$ as one proposition:
$$(ABC|D)=F[(BC|D),(A|BCD)]\tag{2.11}$$
$$(ABC|D)=F\{F[(C|D),(B|CD)],(A|BCD)\}\tag{2.12a}$$
Treating $AB$ as one proposition:
$$(ABC|D)=F[(C|D),(AB|CD)]=F\{(C|D),F[(B|CD),(A|BCD)]\}\tag{2.12b}$$
A necessary condition for consistent reasoning is therefore the functional equation
$$F[F(x,y),z]=F[x,F(y,z)].\tag{2.13}$$
It goes back to N. H. Abel (1826). Aczél (1966) calls it "The Associativity Equation". Aczél solves it without assuming differentiability, but the proof fills 11 pages. Jaynes gives the shorter proof of R. T. Cox (1961), which assumes differentiability (p. 27). The trivial solution $F=\text{const}$ violates (2.10) and is useless, so one seeks the most general nontrivial solution (p. 27).

**Derivation (pp. 27–28).** Skip path: carry forward (2.26)–(2.28).
- Abbreviate $u\equiv F(x,y)$, $v\equiv F(y,z)$ (2.14). Then (2.13) reads $F(x,v)=F(u,z)$ (2.15).
- Differentiating with respect to $x$ and $y$:
$$F_1(x,v)=F_1(u,z)F_1(x,y),\qquad F_2(x,v)F_1(y,z)=F_1(u,z)F_2(x,y).\tag{2.16}$$
- Eliminating $F_1(u,z)$ (added step: divide the second equation by the first) and writing $G(x,y)\equiv F_2(x,y)/F_1(x,y)$:
$$G(x,v)F_1(y,z)=G(x,y).\tag{2.17}$$
- The left side of (2.17) is independent of $z$. Equivalently,
$$G(x,v)F_2(y,z)=G(x,y)G(y,z).\tag{2.18}$$
  Call the left sides of (2.17), (2.18) $U$, $V$. Then $\partial V/\partial y=\partial U/\partial z$, so $G(x,y)G(y,z)$ is independent of $y$.
- The most general such $G$ is
$$G(x,y)=r\,\frac{H(x)}{H(y)},\tag{2.19}$$
  with $r$ a constant and $H$ arbitrary. Since $G>0$ by monotonicity, $r>0$ and $H$ does not change sign.
- Then (2.17), (2.18) become
$$F_1(y,z)=\frac{H(v)}{H(y)},\tag{2.20}$$
$$F_2(y,z)=r\,\frac{H(v)}{H(z)}.\tag{2.21}$$
  The relation $dv=dF(y,z)=F_1dy+F_2dz$ takes the form
$$\frac{dv}{H(v)}=\frac{dy}{H(y)}+r\,\frac{dz}{H(z)}.\tag{2.22}$$
- Integrating (added step: the integral of $dv/H(v)$ is $\ln w(v)$):
$$w[F(y,z)]=w(v)=w(y)\,w^r(z),\tag{2.23}$$
  where
$$w(x)\equiv\exp\left\{\int^x\frac{dx}{H(x)}\right\}.\tag{2.24}$$
  The absent lower limit means $w$ has an arbitrary multiplicative factor.
- Applying $w$ to (2.15) and using (2.23) gives $w(x)w^r(v)=w(u)w^r(z)$. Applying (2.23) again:
$$w(x)\,w^r(y)\,[w(z)]^{r^2}=w(x)\,w^r(y)\,w^r(z).\tag{2.25}$$
- A nontrivial solution exists only if $r=1$. Hence
$$w[F(x,y)]=w(x)w(y)\tag{2.26}$$
$$F(x,y)=w^{-1}[w(x)w(y)].\tag{2.27}$$

**Product rule (p. 29).** Associativity and commutativity of the logical product therefore require
$$w(AB|C)=w(A|BC)\,w(B|C)=w(B|AC)\,w(A|C).\tag{2.28}$$
By (2.24), $w$ is a positive continuous monotonic function, increasing or decreasing according to the sign of $H$; otherwise it is arbitrary at this stage. (2.28) was derived as a necessary condition for (IIIa). Jaynes says it is evidently also sufficient for any number of joint propositions: all expansions of, e.g., $(ABCDEFG|H)$ by successive partitions then agree (p. 29).

> **Intuition note.** If the plausibility of a conjunction must come out the same however it is grouped or ordered (and must rise monotonically and continuously with its inputs), the scoring must become multiplicative after a suitable relabelling of the numbers. The labelling function $w$ is still free at this point. Besides associativity and commutativity of the logical product, the argument uses monotonicity and continuity (and, in Cox's proof, differentiability).

**Fixing the end-points of $w$ (pp. 29–30).**
- Suppose $A$ is certain given $C$. Then $AB|C=B|C$ (2.29) and $A|BC=A|C$ (2.30). So (2.28) reduces to $w(B|C)=w(A|C)w(B|C)$ (2.31). This must hold for any $B$, so certainty is represented by $w(A|C)=1$ (2.32).
- Suppose $A$ is impossible given $C$. Then $AB|C=A|C$ (2.33) and $A|BC=A|C$ (2.34). So (2.28) reduces to $w(A|C)=w(A|C)w(B|C)$ (2.35). Only $w(A|C)=0$ or $+\infty$ can satisfy this for all $B$. The value $-\infty$ is ruled out, because by continuity $w(B|C)$ would then take negative values and (2.35) would be contradicted.
- So $w$ is positive, continuous and monotonic. If increasing, it runs from 0 (impossible) to 1 (certain). If decreasing, it runs from $\infty$ to 1. The conditions say nothing yet about its behaviour between the limits.
- The two cases are equivalent in content: $w_2\equiv1/w_1$ converts one to the other. The convention $0\le w\le1$ therefore loses no generality. The opposite convention would work equally well, with less familiar equations (p. 30).

### 2.2 The sum rule

**Setting up (p. 30).** $A\bar A$ is always false and $A+\bar A$ always true. The plausibility that $A$ is false must depend on that of $A$. Define $u\equiv w(A|B)$, $v\equiv w(\bar A|B)$, so
$$v=S(u).\tag{2.36}$$
Common sense requires $S$ to be continuous, monotonic decreasing on $0\le u\le1$, with $S(0)=1$, $S(1)=0$. It must also be consistent with the product rule written for $AB$ and for $A\bar B$:
$$w(AB|C)=w(A|C)\,w(B|AC)\tag{2.37}$$
$$w(A\bar B|C)=w(A|C)\,w(\bar B|AC).\tag{2.38}$$
Using (2.36) and (2.38):
$$w(AB|C)=w(A|C)S[w(\bar B|AC)]=w(A|C)\,S\!\left[\frac{w(A\bar B|C)}{w(A|C)}\right].\tag{2.39}$$

**Functional equation for $S$ (p. 31).** Commutativity ($AB=BA$) requires
$$w(A|C)\,S\!\left[\frac{w(A\bar B|C)}{w(A|C)}\right]=w(B|C)\,S\!\left[\frac{w(B\bar A|C)}{w(B|C)}\right].\tag{2.40}$$
This must hold for all $A,B,C$, in particular when $\bar B=AD$ (2.41) for any new proposition $D$. Then $A\bar B=\bar B$ and $B\bar A=\bar A$ (2.42), so
$$w(A\bar B|C)=w(\bar B|C)=S[w(B|C)],\qquad w(B\bar A|C)=w(\bar A|C)=S[w(A|C)].\tag{2.43}$$
With $x\equiv w(A|C)$, $y\equiv w(B|C)$ (2.44), eq. (2.40) becomes (the source text says "(2.25) becomes"; see Reading notes)
$$x\,S\!\left[\frac{S(y)}{x}\right]=y\,S\!\left[\frac{S(x)}{y}\right],\qquad 0\le S(y)\le x,\; 0\le x\le1.\tag{2.45}$$
For $y=1$ (added step: $S(1)=0$ and $S(0)=1$ make the left side equal $x$):
$$S[S(x)]=x,\tag{2.46}$$
so $S$ is self-reciprocal, $S=S^{-1}$. This only expresses that the relation between $A$ and $\bar A$ is reciprocal (p. 31). The domain comes from $0\le w(D|AC)\le1$ (2.47) and $S(y)=w(AD|C)=w(A|C)w(D|AC)$. It consists of points in the unit square on or above the curve $y=S(x)$ (p. 31).

**Solving it (pp. 31–33).** Skip path: carry forward (2.58) and the sum rule (2.60). The curve's shape is fixed by (2.45) at points infinitesimally above it, $y=S(x)+\epsilon$. As $\epsilon\to0^+$ two terms tend to $S(1)=0$ at different rates, so everything depends on how $S(1-\delta)\to0$ as $\delta\to0$ (pp. 31–32).
- Define $q(x,y)$ by
$$\frac{S(x)}{y}=1-\exp\{-q\}.\tag{2.48}$$
  Take $\delta=\exp\{-q\}$ and define $J$ by
$$S(1-\delta)=S(1-\exp\{-q\})=\exp\{-J(q)\}.\tag{2.49}$$
  The task is the asymptotic form of $J(q)$ as $q\to\infty$.
- With $x,q$ as independent variables:
$$S(y)=S[S(x)]+\exp\{-q\}S(x)S'[S(x)]+O(\exp\{-2q\}).\tag{2.50}$$
- Using (2.46) and its derivative $S'[S(x)]S'(x)=1$:
$$\frac{S(y)}{x}=1-\exp\{-(\alpha+q)\}+O(\exp\{-2q\}),\tag{2.51}$$
$$\alpha(x)\equiv\log\left[\frac{-xS'(x)}{S(x)}\right]>0.\tag{2.52}$$
- Equation (2.45) becomes
$$J(q+\alpha)-J(q)=\log\frac{x}{S(x)}+\log(1-\exp\{-q\})+O(\exp\{-2q\}),\quad 0<q<\infty,\;0<x\le1.\tag{2.53}$$
- The last two terms vanish exponentially, so $J$ is asymptotically linear,
$$J(q)\sim a+bq+O(\exp\{-q\}),\tag{2.54}$$
  with positive slope
$$b=\alpha^{-1}\log\frac{x}{S(x)}.\tag{2.55}$$
  There is no periodic term of period $\alpha$, because (2.53) holds for a continuum of $x$ and hence of $\alpha(x)$.
- $J$ depends on $q$ only, so the right side of (2.55) is independent of $x$:
$$\frac{x}{S(x)}=\left[\frac{-xS'(x)}{S(x)}\right]^{b},\qquad 0<b<\infty.\tag{2.56}$$
- Rearranged (added step: raise to the power $m=1/b$, which gives $x^{m-1}dx=-S^{m-1}dS$), with $m\equiv1/b>0$:
$$S^{m-1}dS+x^{m-1}dx=0.\tag{2.57}$$
- The only solution with $S(0)=1$ (added step: integrate, $S^m+x^m=$ const, and the constant is 1) is
$$S(x)=(1-x^m)^{1/m},\qquad 0\le x\le1,\;0<m<\infty.\tag{2.58}$$
- Conversely (2.58) solves (2.45). It was first derived by Cox (1946) by a different argument, assuming $S$ twice differentiable. Aczél (1966) derives it without differentiability. Jaynes calls assuming differentiability "very innocuous", since nondifferentiable functions would have been rejected as qualitative violations of common sense. (2.58) satisfies $S(1)=0$ automatically (p. 33).

**Sufficiency (p. 33).** The choice (2.41) was special, so so far (2.58) is only necessary for (2.40). Substituting (2.58) into (2.40) gives
$$w^m(A|C)-w^m(A\bar B|C)=w^m(B|C)-w^m(B\bar A|C),\tag{2.59}$$
a trivial identity by (2.28) and (2.38). So (2.58) is necessary and sufficient for consistency in the sense (2.40).

**Summary and rescaling (pp. 33–34).** The same monotonic $w$ obeys the product rule (2.28) and, for some positive $m$, the sum rule
$$w^m(A|B)+w^m(\bar A|B)=1.\tag{2.60}$$
The product rule can be written equally as $w^m(AB|C)=w^m(A|C)w^m(B|AC)=w^m(B|C)w^m(A|BC)$ (2.61). So $m$ is irrelevant. Define
$$p(x)\equiv w^m(x),\tag{2.62}$$
giving
$$p(AB|C)=p(A|C)\,p(B|AC)=p(B|C)\,p(A|BC),\tag{2.63}$$
$$p(A|B)+p(\bar A|B)=1.\tag{2.64}$$
This loses no generality. $w^m$ is again a continuous monotonic increasing function from 0 (impossible) to 1 (certain), so choosing among values of $m$ adds no freedom beyond the arbitrariness of $w$. All possibilities allowed by the desiderata are in (2.63)–(2.64), with $p$ any continuous monotonic increasing function with range $[0,1]$ (pp. 33–34).

> **Intuition note.** The product rule only says to multiply, and the sum rule only says that $p(A)$ and $p(\bar A)$ add to one. Any scale that behaves well can be converted into the one where both hold in their familiar form. The conversion does not change what the robot concludes.

**Completeness (pp. 34–35).** Conjunction and negation are an adequate set of logic operations (noted after (1.23)), so one conjectures that the product and sum rules suffice (p. 34). For the logical sum:
$$\begin{aligned}p(A+B|C)&=1-p(\bar A\bar B|C)=1-p(\bar A|C)p(\bar B|\bar AC)\\&=1-p(\bar A|C)[1-p(B|\bar AC)]=p(A|C)+p(\bar AB|C)\\&=p(A|C)+p(B|C)p(\bar A|BC)=p(A|C)+p(B|C)[1-p(A|BC)]\end{aligned}\tag{2.65}$$
and finally
$$p(A+B|C)=p(A|C)+p(B|C)-p(AB|C).\tag{2.66}$$
Jaynes calls this one of the most useful rules in applications. The primitive sum rule (2.64) is the special case $B=\bar A$ (p. 34).

Any logic function other than the trivial contradiction is a logical sum of some of the $2^n$ basic conjunctions $Q_i$ (disjunctive normal form). Their plausibilities follow from repeated use of the product rule. Since they are mutually exclusive, the sum reduces (see (2.85)) to $\sum_ip(Q_i|C)$ with at most $2^n-1$ terms (p. 35). Adequacy is claimed in this sense: whenever the background information determines the plausibilities of the basic conjunctions, the rules determine the plausibility of every proposition in the Boolean algebra generated by $\{A_1,\dots,A_n\}$. For $n=4$: $2^4=16$ basic conjunctions determine $2^{16}=65\,536$ propositions. A real application usually needs only a small part (p. 35).

### 2.3 Qualitative properties

**Deduction as a limit (p. 35).** As $p(A|B)\to0$ or $1$, the sum rule expresses the Aristotelian postulate. With $C\equiv A\Rightarrow B$ (2.69), the strong syllogisms (2.68) (from $A$ true infer $B$ true; from $B$ false infer $A$ false) correspond to
$$p(B|AC)=\frac{p(AB|C)}{p(A|C)},\qquad p(A|\bar BC)=\frac{p(A\bar B|C)}{p(\bar B|C)}.\tag{2.70}$$
Since $p(AB|C)=p(A|C)$ and $p(A\bar B|C)=0$ under $C$, this gives $p(B|AC)=1$, $p(A|\bar BC)=0$ (2.71). Aristotelian deductive logic is the limiting form of these rules as the robot becomes more and more certain.

**Weak syllogisms (p. 36).**
- First weak syllogism ($A\Rightarrow B$, $B$ true, so $A$ more plausible) corresponds to
$$p(A|BC)=p(A|C)\frac{p(B|AC)}{p(B|C)}.\tag{2.73}$$
  With $p(B|AC)=1$ and $p(B|C)\le1$:
$$p(A|BC)\ge p(A|C).\tag{2.74}$$
- Second ($A\Rightarrow B$, $A$ false, so $B$ less plausible): $p(B|\bar AC)=p(B|C)\,p(\bar A|BC)/p(\bar A|C)$ (2.76). From (2.74), $p(\bar A|BC)\le p(\bar A|C)$ (the sum-rule step is implicit), so
$$p(B|\bar AC)\le p(B|C).\tag{2.77}$$
- Policeman's syllogism: with $C$ the background information, the major premise (if $A$ is true, $B$ becomes more plausible) is $p(B|AC)>p(B|C)$ (2.78). Then (2.73) gives at once $p(A|BC)>p(A|C)$ (2.79).

**What decides the size of the update (pp. 36–37).** By (2.73), since $p(B|AC)\le1$, a large increase in the plausibility of $A$ can occur only when $p(B|C)$ is very small. The gentleman's behaviour makes guilt nearly certain because that behaviour is otherwise very unlikely. If learning $A$ would raise $B$ only negligibly, then observing $B$ raises $A$ only negligibly (p. 37). Jaynes notes that many writers (Keynes, Jeffreys, Pólya, Cox, Tribus, de Finetti, Rosenkrantz) have demonstrated this qualitative correspondence (p. 37).

> **Intuition note.** Evidence moves a hypothesis a lot only if the evidence would be surprising without the hypothesis. This is the "ratio" in (2.73): the hypothesis's own prediction ($\le1$) divided by how expected the evidence was. (Canon link: Bayes' theorem; not named as such in this unit.)

### 2.4 Numerical values

Two tasks remain (p. 37). First, each monotonic choice of $p(x)$ appears to give different rules. Second, nothing says what initial numerical plausibilities to assign. This requires the interface desiderata (IIIb), (IIIc).

**Sum of exclusive propositions (pp. 37–38).** Applying (2.66) twice to three propositions, using $(A_1+A_2)A_3=A_1A_3+A_2A_3$ (2.81):
$$p(A_1+A_2+A_3|B)=p(A_1+A_2|B)+p(A_3|B)-p(A_1A_3+A_2A_3|B)\tag{2.80}$$
and in full
$$\begin{aligned}p(A_1+A_2+A_3|B)&=p(A_1|B)+p(A_2|B)+p(A_3|B)\\&\quad-p(A_1A_2|B)-p(A_2A_3|B)-p(A_3A_1|B)\\&\quad+p(A_1A_2A_3|B).\end{aligned}\tag{2.82}$$
If the propositions are mutually exclusive, $p(A_iA_j|B)=p(A_i|B)\delta_{ij}$ (2.83), the last four terms vanish:
$$p(A_1+A_2+A_3|B)=p(A_1|B)+p(A_2|B)+p(A_3|B).\tag{2.84}$$
By induction, for $n$ mutually exclusive propositions
$$p(A_1+\cdots+A_m|B)=\sum_{i=1}^mp(A_i|B),\qquad1\le m\le n.\tag{2.85}$$
Conventional expositions usually introduce (2.85) first as the basic but, as far as one can see, arbitrary axiom. Here it is deduced from qualitative consistency conditions (p. 38). If the propositions are also exhaustive ($B$ stipulates exactly one is true),
$$\sum_{i=1}^np(A_i|B)=1.\tag{2.86}$$
This alone does not fix the individual values. Translating information $B$ into numbers is an open-ended research problem (p. 38).

**Principle of indifference (pp. 38–41).** Jaynes asks the reader to suppress intuition and follow the logic, because intuition reaches the conclusion without showing its range of validity. He says debates based on conflicting intuitions retarded the theory for some 150 years (pp. 38–39).
- *Problem I:* exclusive, exhaustive $\{A_1,\dots,A_n\}$, evaluate $p(A_i|B)_I$.
- *Problem II:* swap the labels of the first two. $A_1'\equiv A_2$, $A_2'\equiv A_1$, $A_k'\equiv A_k$ for $3\le k\le n$ (2.87); evaluate $p(A_i'|B)_{II}$.
- The robot's state of knowledge about $A_1$ in I equals that about $A_2'$ in II (same proposition, same $B$). Hence the transformation equations
$$p(A_1|B)_I=p(A_2'|B)_{II},\qquad p(A_2|B)_I=p(A_1'|B)_{II}.\tag{2.88, 2.89}$$
  They hold whatever $B$ is.
- Suppose $B$ is indifferent between $A_1$ and $A_2$ (whatever it says about one it says about the other, so it gives no reason to prefer either). Then I and II are equivalent states of knowledge, including labelling. Desideratum (IIIc) says equivalent states of knowledge get equivalent assignments:
$$p(A_i|B)_I=p(A_i'|B)_{II},\quad i=1,\dots,n.\tag{2.90}$$
- Combining (2.88)–(2.90): $p(A_1|B)_I=p(A_2|B)_I$ (2.91). Jaynes calls this the first "baby" version of the group invariance principle, extended in Chapter 6 (p. 40).
- General case: for any permutation $\{A_1'',\dots,A_n''\}$ (Problem III) with $A_k''\equiv A_i$ there are $n$ transformation equations $p(A_i|B)_I=p(A_k''|B)_{III}$ (2.92). If $B$ is indifferent among all $A_i$, symmetry gives $p(A_k|B)_I=p(A_k''|B)_{III}$ (2.93), so
$$p(A_i|B)_I=p(A_k|B)_I\tag{2.94}$$
  for $k$ ranging over all others, over the $n!$ permutations. So all $p(A_i|B)_I$ are equal (already required by a single cyclic permutation of order $n$). With (2.86):
$$p(A_i|B)_I=\frac1n,\qquad1\le i\le n.\tag{2.95}$$
  Following Keynes (1921), this is the principle of indifference.

**Why it matters (pp. 41–42).**
- *Uniqueness:* any other assignment would give, after a permutation of labels, a second problem with the same knowledge but different values (p. 41).
- *It answers both questions:*
  - Information can lead to definite numerical values.
  - The information determines the values of $p(x)=p(A_i|B)$, not those of the original plausibilities $x=A_i|B$. As Jaynes puts it, "It is $p$ that is rigidly fixed by the data, not $x$" (p. 41).
- Whatever $p(x)$ is chosen, the same result (2.95) follows. Different choices of $p(x)$ correspond only to different internal memory codes of the robot. Storing any strict monotonic function of $p_i$ gives the same observable behaviour. So $x\equiv A|B$ is an arbitrary monotonic function of $p$, $0\le p\le1$, and there is only one consistent set of rules. Jaynes says that, for practical purposes, the original plausibilities $x$ drop out of the picture (p. 41).
- The quantities $p$ are now called *probabilities* (p. 41). Jaynes says the word was avoided until their unique determination by the data was shown (p. 42).
- $p$ is chosen as the scale not because it is more "correct" but because it obeys the simplest rules (product and sum). This is analogous to the Kelvin scale among monotonically related empirical temperature scales: thermodynamic laws ($dU=TdS-PdV$, $dG=-SdT+VdP$, etc.) take their simplest form in it, and kelvin values are directly measurable independently of the substance (p. 42).

> **Intuition note.** If two problems differ only by the names given to the options, a consistent reasoner must treat them identically. With total indifference, this symmetry leaves no way to favour one option, so every option gets $1/n$. The rules then fix the numbers, not just their ordering.

**Urn example (p. 42).** An urn holds 10 identical balls numbered 1–10. Balls 4, 6, 7 are black, the other seven white. One ball is drawn blindfolded after shaking the urn. The background information $B$ is the statements about the black and white balls and about shaking and drawing. Let $A_i$ be the proposition that the $i$th ball is drawn. By (2.95),
$$p(A_i|B)=\tfrac1{10}.\tag{2.96}$$
Drawing black means $A_4+A_6+A_7$, so
$$p(\text{black}|B)=p(A_4+A_6+A_7|B),\tag{2.97}$$
and by (2.85) (mutually exclusive)
$$p(\text{black}|B)=\frac3{10}.\tag{2.98}$$
In general, with $N$ such balls and $A$ true on a specified subset of $M$ of them ($0\le M\le N$):
$$p(A|B)=\frac MN.\tag{2.99}$$
This was James Bernoulli's (1713) original definition of probability, used for about 150 years. Laplace (1812) opens with: the probability of an event is the ratio of favourable cases to all possible cases when nothing leads us to expect any one to occur more than any other (p. 43).

### 2.5 Notation and finite-sets policy (pp. 43–44)
- Formal probabilities with proposition arguments use capital $P$: $P(A|B)$ (2.100). Probabilities with numerical arguments use other symbols, such as $f(r|np)$ (2.101), which denote ordinary functions. Lowercase $p(x|y)$ is also used loosely, with arguments either propositions or numbers, and its meaning is to be judged from context (p. 43).
- The consistency theorems are established only for probabilities on finite sets of propositions. Extension to infinite sets is permitted only as the result of a well-defined, well-behaved limit from a finite set (p. 43).
- **Finite-sets policy:** apply ordinary arithmetic and analysis only to expressions with a finite number of terms. Only after the calculation, observe how the finite expressions behave as the number of terms grows indefinitely (p. 44).
- Reasons Jaynes gives (p. 44):
  - The policy is consistent with Lebesgue's original definition of measure.
  - Measure-theory notation presupposes the infinite limit already taken, without indicating which limiting process was used.
  - Different well-behaved limiting processes can give different results.
  - Without a well-behaved limit, going directly to the limit can give nonsense.
  - Chapter 15 on infinite-set paradoxes will show results from ignoring this rule.

### 2.6 Comments (pp. 44–50)

Jaynes says it took two chapters to return to (2.99), where Laplace started about 180 years earlier. Jaynes says he will try to understand the intervening period, a weird episode of history, throughout the rest of the book (p. 44).

**2.6.1 "Subjective" vs "objective" (pp. 44–45).**
- Any probability assignment here is "subjective" in the sense that it describes only a state of knowledge, not anything measurable in a physical experiment (p. 44).
- **Objection (an anticipated questioner):** whose state of knowledge is meant? **Jaynes replies:** that of the robot, or of anyone given the same information who reasons by the desiderata (p. 44).
- Someone with the same information but a different conclusion violates a desideratum. Jaynes says it appears to him that a rational person who discovered this would wish to revise his thinking (p. 45).
- Interface desiderata (IIIb), (IIIc) make assignments "objective" in the sense of being independent of the user's personality: they encode the information given, not hopes, fears or value judgments. Jaynes holds that this is the objectivity a scientific theory of inference needs (p. 45).

**2.6.2 Gödel's theorem (pp. 45–47).**
- Desideratum (IIIa) determined the rules. This does not prove the rules consistent. It means only that other rules representing plausibility by real numbers but differing in content will lead to inconsistencies or violations of other desiderata (p. 45).
- "Inconsistency" has the same meaning as for a logician: contradictory results derivable by valid application (e.g. both $P(A|BC)=1/3$ and $2/3$ in two valid ways). A contradiction implies all propositions: $A\Rightarrow(A+B)$, so $\bar AA\Rightarrow\bar A(A+B)=\bar AA+\bar AB\Rightarrow B$ (p. 45).
- Let $\mathcal A$ be an axiom system and $T$ deducible: $\mathcal A\Rightarrow T$ (2.102). That $T$ is deducible cannot prove consistency, since a contradiction would also yield $T$. Jaynes calls this the essence of Gödel's theorem as it pertains here, following Fisher (1956). He does not suppose a logician would accept it as a proof of the full theorem (pp. 45–46).
- If the axioms are inconsistent, the opposite $\bar T$ is also deducible, $\mathcal A\Rightarrow\bar T$ (2.103). So inconsistency is proved by exhibiting some $T$ and $\bar T$. Gödel's theorem says only that no consistency-testing procedure derivable from the axioms of the system tested exists (p. 46).
- Probability theory comes close to such a procedure: probabilities conditional on contradictory premises do not exist (the hypothesis space is empty). A program computing $p(B|E)$ for $E=E_1\dots E_n$ will crash if a contradiction is hidden in $E$. Jaynes says this was found "empirically" and is a valuable diagnostic. If the program prints valid numbers, the $E_i$ are mutually consistent. This is no contradiction of Gödel, because the argument uses principles not derivable from the propositions tested (p. 46).
- Undecidability: many simple questions are undecidable by deduction. Example: two sole witnesses give opposite testimony and both die; one lied, but which one cannot be determined. Undecidability signals incomplete information, not an inherent property. New external axioms might decide the proposition. Jaynes expects that, as science becomes more information-oriented, Gödel's result will be seen as more of a platitude than a paradox, and says undecidability marks a problem calling for inference rather than deduction (p. 47).
- Whether consistency can be proved by going outside probability theory appears to Jaynes, at the moment, to be an open question. Jaynes states that no inconsistency has been found from correct application of the rules; apparent ones were misapplications. Guided by Cox's theorems, he says he has never had difficulty exhibiting inconsistencies in ad hoc rules (Chapters 5, 15, 17) (p. 47).

**2.6.3 Venn diagrams (pp. 47–49).**
- **Reader's question:** why not illustrate $P(A+B|C)=P(A|C)+P(B|C)-P(AB|C)$ (2.104) by a Venn diagram? Jaynes's answer is that the diagram illustrates it in one special case but can mislead (p. 47).
- If probability is area, then subregions of $A$ must be mutually exclusive subpropositions, and the points must represent some ultimate elementary propositions $\omega_i$ into which $A$, $B$, $C$ all resolve (p. 48).
- This imports structure (propositions as point sets, $A+B$ as union, $AB$ as intersection, probability as additive measure) that the general theory does not have (p. 48).
- Propositions such as that it will rain today (2.105) and that the roof will leak (2.106) need not be resolvable into more elementary ones. Forced resolution by irrelevancies, e.g. $B=BC_1+\dots+BC_N$ with $C_k$ the proposition that the number of penguins in Antarctica is $k$ (2.107), is valid Boolean algebra but idle. Resolving rain into raindrop trajectories does not help a meteorologist. Real problems have a natural end to resolving. Chapter 8 ("Sam's broken thermometer") is to demonstrate this (pp. 48–49).
- Where a resolution is relevant it can be a calculational device (e.g. (2.98)). But $A$, $B$ will seldom resolve into the same $\omega_i$, and one reserves the right to enlarge the context with further propositions (p. 49).
- So $AB$ means only that both $A$ and $B$ are true, and $p(AB|C)$ is an elementary quantity in its own right. Boole's notation $A+B$, $AB$ is kept to avoid set-theory associations (p. 49). Jaynes prefers to say (2.104) explains and justifies the Venn diagram, in one special case (p. 49).

**2.6.4 The "Kolmogorov axioms" (pp. 49–50).**
- Kolmogorov (1933) phrased probability in set and measure theory, which Jaynes says gives some modern works the impression that probability began with him. He formalized the Venn-diagram picture (p. 49).
- Appendix A shows that, for all practical purposes, the four axioms for his measure, stated arbitrarily, have all been derived in this chapter as necessary for consistency. Jaynes expects to defend Kolmogorov against critics on technical points. He urges readers who learned the Kolmogorov basis to read Appendix A (pp. 49–50).
- Conceptual difference: Jaynes does not interpret propositions as sets, but interprets probability distributions as carriers of incomplete information. He says that partly as a result his system has analytical resources absent from Kolmogorov's system, for "ill posed" and "generalized inverse" problems (p. 50).

## Toy example (ours, not from the text)

A fair-looking six-sided die is a "6-ball urn": balls 1–6, indifferent background information $I$. By (2.95), $P(i|I)=1/6$ for each face. Let $A=$ "even" $=\{2,4,6\}$ and $B'=$ "at least 4" $=\{4,5,6\}$.

1. By (2.85): $P(A|I)=3/6=1/2$, $P(B'|I)=3/6=1/2$, and $AB'=\{4,6\}$ gives $P(AB'|I)=2/6=1/3$.
2. Extended sum rule (2.66): $P(A+B'|I)=1/2+1/2-1/3=2/3$. Direct check: $A+B'=\{2,4,5,6\}$, $4/6=2/3$ ✓.
3. Product rule (2.63): $P(B'|AI)=2/3$ (4 and 6 among 2, 4, 6), so $P(A|I)P(B'|AI)=\tfrac12\cdot\tfrac23=\tfrac13$ ✓. The other order: $P(A|B'I)=2/3$, and $P(B'|I)P(A|B'I)=\tfrac12\cdot\tfrac23=\tfrac13$ ✓. Both orders agree, which is what (2.13) demands.
4. Different scale: take $w=p^{1/2}$ (so $m=2$ in (2.62)). Then $w(AB')=\sqrt{1/3}$ and $w(A)\,w(B'|A)=\sqrt{1/2}\sqrt{2/3}=\sqrt{1/3}$ ✓, so the product rule holds for $w$ too. The sum rule has the form $w^2(A)+w^2(\bar A)=1/2+1/2=1$ ✓ (2.60). The robot's conclusions do not depend on whether it stores $p$ or $\sqrt p$.
5. Relabelling: swapping the names of faces 1 and 2 changes no knowledge, and every $P(i|I)=1/6$ is unchanged. A different assignment, say $P(1)=0.2$, would become something else after swapping, which is the contradiction behind (2.95).

## Concepts
- [[probability-as-extended-logic]] — plausibilities as real numbers obeying the product and sum rules, deduced from desiderata; deductive logic is the limit of certainty (pp. 24, 35)
- [[cox-theorem]] — here: the functional-equation derivation of product and sum rules from consistency. Jaynes gives Cox's (1961) shorter proof of (2.27) and a derivation of (2.58) that differs from Cox's original (1946) argument; the unit mentions "Cox's theorems" (p. 47) but does not state a theorem under this name (pp. 27, 33, 47)
- [[product-rule]] (new) — $w(AB|C)=w(A|BC)w(B|C)$ forced by associativity and commutativity of the logical product; becomes (2.63) after rescaling (pp. 27–29, 33)
- [[sum-rule]] (new) — $p(A|B)+p(\bar A|B)=1$, forced by consistency of the product rule for $AB$ and $A\bar B$ (pp. 31–33)
- [[extended-sum-rule]] (new) — $P(A+B|C)=P(A|C)+P(B|C)-P(AB|C)$ (p. 34)
- [[associativity-equation]] (new) — the functional equation $F[F(x,y),z]=F[x,F(y,z)]$, with solution $F=w^{-1}[w(x)w(y)]$ (pp. 27–28)
- [[principle-of-indifference]] — $P(A_i|B)=1/n$ when $B$ is indifferent among $n$ exclusive, exhaustive propositions, derived from permutation symmetry plus desideratum (IIIc). Jaynes calls it the first "baby" group-invariance argument (pp. 38–40)
- [[subjective-probability]] — here: "subjective" means that probability describes only a state of knowledge, not that it depends on the person; assignments are meant to be objective in that sense (pp. 44–45)
- [[bayes-theorem]] — appears as product rule form (2.73); not named in this unit (p. 36)
- [[finite-sets-policy]] (new) — use arithmetic and analysis only on finite expressions, then study the limit (p. 44)
- [[frequentist-vs-bayesian-inference]] — only implicit: the Bernoulli/Laplace ratio is derived from information about equally possible cases (pp. 42–43), and probability assignments are said to describe a state of knowledge, not anything measurable in a physical experiment (p. 44); frequencies are not discussed in this unit

## Canonical instances
- [[blue-brown-eyes]] — shows that $AB|C$ cannot be a function of $A|C$ and $B|C$ alone (p. 25)
- [[policeman-syllogism]] — evidence is strong when it is unlikely otherwise, from (2.73) (pp. 36–37)
- [[bernoulli-urn]] — ten balls, three black, $P(\text{black})=3/10$; ratio form $M/N$ (p. 42)
- [[two-dead-witnesses]] — undecidability as incompleteness of information (p. 47)
- [[kelvin-temperature-scale]] — analogy for choosing $p$ as a convenient, not "correct", scale (p. 42)
- [[penguins-resolution]] — irrelevant forced resolution of a proposition into elementary ones (p. 48)

## Bridges (candidates)
- [structural-analogy] multiplicative $w$ (2.26) ↔ information-theory: surprisal $-\log p$ is additive for independent events. Taking $\log w$ turns the product rule into addition, but this unit does not make that move.
- [structural-analogy] Principle of indifference (uniform $1/n$) ↔ maximum entropy: the uniform distribution is the most uncommitted one when only normalization is known (canon link; not stated in this unit).
- [structural-analogy] Cox-style derivation of the rules ↔ Dutch book argument: two different routes to the same sum and product rules from consistency.
- [structural-analogy] Conditioning on contradictory premises is undefined (the program "crashes") ↔ conditioning on a probability-zero event in standard measure-theoretic probability.
- [metaphor] Choosing $p$ among monotonic scales ↔ thermodynamics: choosing Kelvin temperature among empirical scales (Jaynes's own analogy).

## Questions this raises
- The derivation assumes differentiability (Cox) and cites Aczél for the proof without it. What exactly do the continuity and monotonicity desiderata add, and what changes if one is dropped?
- (2.95) needs information $B$ that is truly indifferent. How are probabilities assigned when $B$ is not symmetric? Jaynes says this is open-ended and promises Chapter 6.
- Jaynes states that the consistency theorems have been established only on finite sets. How are continuous variables handled by finite-limit procedures, and which paradoxes arise otherwise (Chapter 15)?
- If the probability code stored by the robot is arbitrary up to monotonic transformation, what does it mean that $p$ "is directly determined by our information"?

## Exercises worth doing
- Ex. 2.1 (p. 34) — whether a formula for $p(C|A+B)$ analogous to (2.66) can be derived from the product and sum rules; tests understanding of what the rules do and do not determine — difficulty: medium
- Ex. 2.2 (p. 34) — show that $p(C|A_1+\dots+A_n,X)$ is a weighted average (2.67) of the $p(C|A_iX)$ for mutually exclusive $A_i$ — difficulty: medium
- Ex. 2.3 (p. 43) — bounds on $P(AB|C)$ and $P(A+B|C)$ from $a=P(A|C)\le b=P(B|C)$, with the stronger inequalities when $a+b>1$ or $a+b<1$; useful for catching calculation errors — difficulty: easy

## Reading notes
- Printed page = pdf page − 30 (pdf 54 = printed 24; the labels give printed numbers).
- Source text layer drops overbars and primes in many places (e.g. $\bar A$, $A'_i$, $A''_k$ in §§2.2, 2.4, 2.6.2) and some Greek or script symbols. I used the page images for all equations.
- Misprint: on p. 31, the text after (2.44) says "(2.25) becomes a functional equation"; the image shows "(2.25)", but the context shows the equation being specialized is (2.40).
- Exercise 2.2 (p. 34): the image shows an unbalanced parenthesis in "$p(C|(A_1+A_2+\cdots+A_nX)$"; the intended condition is the sum of the $A_i$ given $X$.
- The text uses $m$ in two senses: the exponent in (2.58) and the upper index in (2.85) ($1\le m\le n$). They are unrelated.
- Equation (2.84) uses capital $P$ in two terms on the printed page, before the notation of §2.5 is introduced.
- Added steps in L3 (marked) are mine: the elimination giving (2.17), the integration giving (2.23), the reduction to (2.46) at $y=1$, the passage from (2.56) to (2.57), and the integration giving (2.58). These are all literally derivable from the displayed equations.
