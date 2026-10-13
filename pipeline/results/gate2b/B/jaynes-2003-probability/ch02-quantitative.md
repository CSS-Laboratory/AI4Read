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
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The quantitative rules (Jaynes, ch. 2)

## L0 — One line
If a reasoning robot represents plausibility by real numbers, agrees qualitatively with common sense and is consistent, then some monotonic function p of its plausibilities must obey the product rule p(AB|C)=p(A|C)p(B|AC) and the sum rule p(A|B)+p(Ā|B)=1; and when its information is indifferent among exclusive, exhaustive propositions, a symmetry argument fixes their values as p = 1/n.

## L1 — The gist (≤ 120 words)
Which rules must a reasoning robot follow if it measures plausibility by real numbers, agrees qualitatively with common sense, and is consistent? Consistency of the logical product leads to a functional equation (an equation whose unknown is a function); its solution is the product rule. Consistency of the product rule written for AB and AB̄, together with commutativity, gives the sum rule. Some monotonic function p of plausibility (one that only rises or only falls) obeys both rules. When the information is indifferent among exclusive, exhaustive propositions, p = 1/n, so the data fix p, not the original scale; p is called probability. Importance: the rules are deduced, not posed as arbitrary axioms.

**Prerequisites:** Boolean algebra (AND, OR, NOT, implication); partial derivatives and the chain rule; solving simple differential equations; basic probability vocabulary; Chapter 1's desiderata (I, II, IIIa–c).

## L2 — Key ideas
- Associativity of the logical product (ABC = (AB)C = A(BC)) forces a functional equation F[F(x,y),z] = F[x,F(y,z)]. Its general solution gives the product rule w(AB|C) = w(A|BC)w(B|C) for some monotonic w (pp. 26–29).
- Common sense requires w = 1 for certainty and w = 0 or ∞ for impossibility. The author adopts 0 ≤ w ≤ 1 as a convention without loss of content (pp. 29–30).
- Consistency of the product rule written for AB and AB̄ gives a second functional equation for the function S that links w(Ā|B) to w(A|B). Its solution is S(x) = (1−x^m)^{1/m}. After the definition p = w^m this yields the sum rule p(A|B)+p(Ā|B)=1, and m drops out (pp. 30–34).
- From these two rules one gets P(A+B|C) = P(A|C)+P(B|C)−P(AB|C). Conjunction and negation suffice to build all logic functions, so the rules are adequate, in the sense that they determine the plausibility of every proposition in the Boolean algebra whenever the basic conjunctions have known plausibilities (pp. 34–35).
- Deductive logic is the limiting case of the rules. The product rule also gives quantitative forms of the weak syllogisms, including the policeman's syllogism (pp. 35–37).
- A symmetry argument (relabeling propositions) yields the principle of indifference, p = 1/n, for exclusive, exhaustive propositions with indifferent information. Hence the data fix p, not x, and the infinite number of seemingly different rule sets collapses to one rule set (pp. 38–42).
- The theorems hold for finite sets of propositions. Infinite sets are allowed only as well-defined and well-behaved limits of finite ones (pp. 43–44).
- Comments: probabilities are "subjective" (they describe a state of knowledge) yet "objective" (independent of the user's personality). The author argues that Gödel's theorem does not undermine the approach, but whether the consistency of the rules can be proved is left as an open question. The Venn diagram illustrates the sum rule only in the special case of propositions about sets. Kolmogorov's four axioms are, for practical purposes, derived in this chapter (pp. 44–50).

## L3 — Walkthrough

### Introduction (p. 24)
The three desiderata are: (I) degrees of plausibility are represented by real numbers; (II) qualitative correspondence with common sense; (III) consistency. The chapter deduces the quantitative rules that follow from them (p. 24).

### 2.1 The product rule (pp. 24–30)

**Orientation (pp. 24–25).** The robot can decide AB is true in two ways. It can first decide B (plausibility B|C), then A given B (A|BC). Or it can decide A first (A|C), then B given A (B|AC). If B is false, AB is false whatever A|B̄C says, so with B|C and A|BC the robot does not need A|C (p. 25). Likewise A|B and B|A (the plausibilities without C) are not needed once C is known. Example: a robot that learns the earth is round does not need its opinions from before it knew this (p. 25). That the two routes agree is desideratum (IIIa) (p. 25).

**The form of the rule.**
$$(AB|C)=F[(B|C),(A|BC)]\tag{2.1}$$
Here F is an unknown function. The alternative
$$(AB|C)=F[(A|C),(B|C)]\tag{2.2}$$
cannot satisfy desideratum (II). Both "blue eyes" and "black hair" can be plausible and jointly plausible. But "left eye blue" and "right eye brown" are each plausible while their conjunction is extremely implausible (p. 25).

**Proof by exhaustion (pp. 25–26).** Define
$$u=(AB|C),\; v=(A|C),\; w=(B|AC),\; x=(B|C),\; y=(A|BC).\tag{2.3}$$
Expressing u as a function of two or more of v, w, x, y gives 11 possibilities. Each can be tested against extreme conditions, such as A implies B̄, A = B, A = C, or C ⇒ Ā. Tribus (1969) finds that all but two can show qualitative violations of common sense. The survivors are u = F(x,y) and u = F(w,v), which are the two forms suggested by the earlier reasoning (p. 26).

**Qualitative requirements on F (p. 26).** Let the prior information change C → C′ so that B becomes more plausible and A|BC does not change:
$$B|C'>B|C,\tag{2.4}$$
$$A|BC'=A|BC.\tag{2.5}$$
Common sense then demands
$$AB|C'\ge AB|C,\tag{2.6}$$
with equality if and only if A|BC corresponds to impossibility. Likewise, if
$$B|C''=B|C,\qquad A|BC''>A|BC,\tag{2.7, 2.8}$$
then
$$AB|C''\ge AB|C.\tag{2.9}$$
Equality is possible only if B is impossible given C. F must also be continuous. Otherwise an arbitrarily small increase in one plausibility could cause a large increase in AB|C. So F(x,y) is continuous and monotonic increasing in both arguments. Assuming differentiability (not necessary, according to the author):
$$F_1(x,y)\equiv \frac{\partial F}{\partial x}\ge 0\tag{2.10a}$$
with equality if and only if y represents impossibility, and
$$F_2(x,y)\equiv \frac{\partial F}{\partial y}\ge 0\tag{2.10b}$$
with equality permitted only if x represents impossibility. F_i means differentiation with respect to the i-th argument (p. 26).

**Associativity (pp. 26–27).** Boolean algebra is associative: ABC = (AB)C = A(BC). Treating BC as one proposition:
$$(ABC|D)=F[(BC|D),(A|BCD)]\tag{2.11}$$
$$(ABC|D)=F\{F[(C|D),(B|CD)],(A|BCD)\}\tag{2.12a}$$
Treating AB as one proposition:
$$(ABC|D)=F[(C|D),(AB|CD)]=F\{(C|D),F[(B|CD),(A|BCD)]\}\tag{2.12b}$$
For consistency the two must agree, which gives the necessary condition
$$F[F(x,y),z]=F[x,F(y,z)].\tag{2.13}$$
This "Associativity Equation" goes back to Abel (1826). Aczél (1966) derives the general solution without assuming differentiability; the proof fills 11 pages. The author gives Cox's (1961) shorter proof, which assumes differentiability (p. 27). The trivial solution F = const violates monotonicity (2.10) and is useless, so the most general nontrivial solution is sought (p. 27).

**Cox's solution (pp. 27–28).** Skip path: carry forward only the result (2.28).

Abbreviate
$$u\equiv F(x,y),\qquad v\equiv F(y,z),\tag{2.14}$$
with (x,y,z) still the independent variables. Then (2.13) reads
$$F(x,v)=F(u,z).\tag{2.15}$$
Differentiating with respect to x and y:
$$F_1(x,v)=F_1(u,z)F_1(x,y),\qquad F_2(x,v)F_1(y,z)=F_1(u,z)F_2(x,y).\tag{2.16}$$
Eliminating F₁(u,z) gives
$$G(x,v)F_1(y,z)=G(x,y),\qquad G(x,y)\equiv F_2(x,y)/F_1(x,y).\tag{2.17}$$
(added step: divide the second equation of (2.16) by the first.) The left side of (2.17) must be independent of z. Equation (2.17) can be rewritten
$$G(x,v)F_2(y,z)=G(x,y)G(y,z).\tag{2.18}$$
(added step: multiply (2.17) by G(y,z) = F₂/F₁.) Call the left sides of (2.17) and (2.18) U and V. One verifies ∂V/∂y = ∂U/∂z, so G(x,y)G(y,z) must be independent of y. The most general G with this property is
$$G(x,y)=r\,\frac{H(x)}{H(y)},\tag{2.19}$$
with r a constant and H arbitrary. Since G > 0 by monotonicity, r > 0 and H may not change sign in the region of interest. Then (2.17) and (2.18) become
$$F_1(y,z)=\frac{H(v)}{H(y)},\tag{2.20}$$
$$F_2(y,z)=r\,\frac{H(v)}{H(z)},\tag{2.21}$$
and dv = dF(y,z) = F₁dy + F₂dz becomes
$$\frac{dv}{H(v)}=\frac{dy}{H(y)}+r\,\frac{dz}{H(z)}.\tag{2.22}$$
Integrating:
$$w[F(y,z)]=w(v)=w(y)\,w^{r}(z),\tag{2.23}$$
$$w(x)\equiv\exp\left\{\int^{x}\frac{dx}{H(x)}\right\}.\tag{2.24}$$
The missing lower limit means w has an arbitrary multiplicative factor. Applying w to (2.15) and using (2.23) gives w(x)w^r(v) = w(u)w^r(z). Applying (2.23) again reduces the functional equation to
$$w(x)\,w^{r}(y)\,[w(z)]^{r^{2}}=w(x)\,w^{r}(y)\,w^{r}(z).\tag{2.25}$$
(added step: w(v) = w(y)w^r(z) and w(u) = w(x)w^r(y).) A nontrivial solution exists only if r = 1 (added step: r² = r with r > 0). The result is
$$w[F(x,y)]=w(x)\,w(y)\tag{2.26}$$
$$F(x,y)=w^{-1}[w(x)\,w(y)].\tag{2.27}$$

**The product rule (p. 29).**
$$w(AB|C)=w(A|BC)\,w(B|C)=w(B|AC)\,w(A|C).\tag{2.28}$$
By its construction w is a positive continuous monotonic function, increasing or decreasing according to the sign of H, and otherwise arbitrary at this stage (p. 29). Rule (2.28) is derived as necessary for consistency (IIIa). The author says it is evidently also sufficient for consistency for any number of joint propositions. For example, all the successive expansions of (ABCDEFG|H) then give the same result (p. 29).

> **Intuition note.** Requiring that "A and B and C" gets the same plausibility whichever way you group it forces, given monotonicity and continuity, a multiplication rule up to a hidden re-scaling w. At this stage only the shape of the rule is forced; the scale is still free.

**Values of w at the extremes (pp. 29–30).** Suppose A is certain given C. Then AB and B have the same truth value, so by the primitive axiom of Chapter 1
$$AB|C=B|C,\tag{2.29}$$
$$A|BC=A|C\tag{2.30}$$
(if C implies A, further non-contradicting information B leaves A certain). Then (2.28) reduces to
$$w(B|C)=w(A|C)\,w(B|C),\tag{2.31}$$
which must hold however plausible B is. So
$$\text{certainty is represented by } w(A|C)=1.\tag{2.32}$$
Now suppose A is impossible given C. Then
$$AB|C=A|C,\qquad A|BC=A|C,\tag{2.33, 2.34}$$
and (2.28) reduces to
$$w(A|C)=w(A|C)\,w(B|C),\tag{2.35}$$
which must hold whatever B is. So w(A|C) is 0 or +∞. The choice −∞ is excluded because by continuity w(B|C) would then have to take negative values, and (2.35) would be a contradiction (p. 30). Thus w is positive, continuous and monotonic. If increasing, it runs from 0 (impossibility) to 1 (certainty). If decreasing, it runs from ∞ down to 1. The two options do not differ in content: given w₁ with impossibility at ∞, w₂ ≡ 1/w₁ has impossibility at 0. So the author adopts 0 ≤ w ≤ 1 as a convention, without loss of generality (p. 30).

### 2.2 The sum rule (pp. 30–35)

The logical product AĀ is always false and the logical sum A+Ā always true. The plausibility of Ā must depend on that of A. With u ≡ w(A|B), v ≡ w(Ā|B):
$$v=S(u).\tag{2.36}$$
S is continuous and monotonic decreasing on 0 ≤ u ≤ 1, with S(0)=1 and S(1)=0 (p. 30). But S is constrained, because the product rule can be written for AB and for AB̄:
$$w(AB|C)=w(A|C)\,w(B|AC)\tag{2.37}$$
$$w(A\overline B|C)=w(A|C)\,w(\overline B|AC).\tag{2.38}$$
Using (2.36) and (2.38), (2.37) becomes
$$w(AB|C)=w(A|C)\,S[w(\overline B|AC)]=w(A|C)\,S\!\left[\frac{w(A\overline B|C)}{w(A|C)}\right].\tag{2.39}$$
Commutativity (AB = BA) then requires
$$w(A|C)\,S\!\left[\frac{w(A\overline B|C)}{w(A|C)}\right]=w(B|C)\,S\!\left[\frac{w(B\overline A|C)}{w(B|C)}\right].\tag{2.40}$$
This must hold for all A, B, C, in particular when
$$\overline B=AD,\tag{2.41}$$
with D any new proposition. Then
$$A\overline B=\overline B,\qquad B\overline A=\overline A,\tag{2.42}$$
$$w(A\overline B|C)=w(\overline B|C)=S[w(B|C)],\qquad w(B\overline A|C)=w(\overline A|C)=S[w(A|C)].\tag{2.43}$$
With
$$x\equiv w(A|C),\qquad y\equiv w(B|C),\tag{2.44}$$
(2.40) becomes the functional equation
$$x\,S\!\left[\frac{S(y)}{x}\right]=y\,S\!\left[\frac{S(x)}{y}\right],\qquad 0\le S(y)\le x,\; 0\le x\le 1.\tag{2.45}$$
The page prints "(2.25) becomes" at this point; the equation in question is (2.40) (see Reading notes). For y = 1:
$$S[S(x)]=x,\tag{2.46}$$
so S is self-reciprocal, S = S⁻¹. This only says the relation between A and Ā is reciprocal (p. 31).

**Domain (p. 31).** D is arbitrary, so all values in
$$0\le w(D|AC)\le 1\tag{2.47}$$
are achievable. Since S(y) = w(AD|C) = w(A|C)w(D|AC), (2.47) is the condition 0 ≤ S(y) ≤ x. The domain is symmetric in x and y. Geometrically it is the part of the unit square on or above the curve y = S(x) (p. 31).

**Solving (2.45) (pp. 31–33).** Skip path: carry forward only (2.58).

The shape of the curve is fixed by what (2.45) says for points infinitesimally above it. Set y = S(x) + ε with ε → 0⁺. Two terms in (2.45) tend to S(1)=0 at different rates, so everything depends on how S(1−δ) tends to zero as δ → 0 (pp. 31–32). Define q(x,y) by
$$\frac{S(x)}{y}=1-\exp\{-q\}.\tag{2.48}$$
Choose δ = exp{−q} and define J(q) by
$$S(1-\delta)=S(1-\exp\{-q\})=\exp\{-J(q)\}.\tag{2.49}$$
The goal is the asymptotic form of J(q) as q → ∞. With x, q as independent variables,
$$S(y)=S[S(x)]+\exp\{-q\}\,S(x)\,S'[S(x)]+O(\exp\{-2q\}).\tag{2.50}$$
Using (2.46) and its derivative S′[S(x)]S′(x) = 1:
$$\frac{S(y)}{x}=1-\exp\{-(\alpha+q)\}+O(\exp\{-2q\}),\tag{2.51}$$
$$\alpha(x)\equiv\log\!\left[\frac{-xS'(x)}{S(x)}\right]>0.\tag{2.52}$$
Equation (2.45) then becomes
$$J(q+\alpha)-J(q)=\log\!\left[\frac{x}{S(x)}\right]+\log(1-\exp\{-q\})+O(\exp\{-2q\}),\qquad 0<q<\infty,\ 0<x\le 1.\tag{2.53}$$
As q → ∞ the last two terms vanish exponentially fast, so J is asymptotically linear:
$$J(q)\sim a+bq+O(\exp\{-q\}),\tag{2.54}$$
$$b=\alpha^{-1}\log\!\left[\frac{x}{S(x)}\right]>0.\tag{2.55}$$
There is no periodic term of period α in (2.54), because (2.53) holds for a continuum of x and hence of α(x). Since J depends on q only, the right side of (2.55) must be independent of x. Using (2.52):
$$\frac{x}{S(x)}=\left[\frac{-xS'(x)}{S(x)}\right]^{b},\qquad 0<b<\infty,\tag{2.56}$$
which is the differential equation
$$S^{m-1}dS+x^{m-1}dx=0,\qquad m\equiv 1/b>0.\tag{2.57}$$
(added step: raise (2.56) to the power m = 1/b, giving x^{m−1} = −S′S^{m−1}; integrating gives S^m + x^m = const, and S(0)=1 fixes the constant.) The only solution with S(0)=1 is
$$S(x)=(1-x^{m})^{1/m},\qquad 0\le x\le 1,\ 0<m<\infty.\tag{2.58}$$
Conversely, (2.58) solves (2.45) (p. 33).

**Remarks (p. 33).** Cox (1946) first derived (2.58) by a different argument that assumed S twice differentiable. Aczél derives it without assuming differentiability. The author says assuming differentiability here is "innocuous": nondifferentiable functions would have been rejected as a qualitative violation of common sense. (2.58) is the most general solution of (2.45) with S(0)=1, and it automatically satisfies S(1)=0.

**Sufficiency (p. 33).** (2.41) was a special choice, so (2.58) is so far only necessary for (2.40). Substituting (2.58) into (2.40) gives
$$w^{m}(A|C)-w^{m}(A\overline B|C)=w^{m}(B|C)-w^{m}(B\overline A|C),\tag{2.59}$$
which the author calls a trivial identity by virtue of (2.28) and (2.38). So (2.58) is necessary and sufficient for consistency in the sense (2.40).

**The two rules (pp. 33–34).** Associativity requires some monotonic function w obeying the product rule (2.28). The same w must obey the sum rule
$$w^{m}(A|B)+w^{m}(\overline A|B)=1\quad\text{for some positive } m.\tag{2.60}$$
The product rule can be written
$$w^{m}(AB|C)=w^{m}(A|C)\,w^{m}(B|AC)=w^{m}(B|C)\,w^{m}(A|BC).\tag{2.61}$$
So m is irrelevant. Define
$$p(x)\equiv w^{m}(x).\tag{2.62}$$
Then
$$p(AB|C)=p(A|C)\,p(B|AC)=p(B|C)\,p(A|BC),\tag{2.63}$$
$$p(A|B)+p(\overline A|B)=1.\tag{2.64}$$
Nothing is lost: w^m is again continuous, monotonic increasing, and runs from 0 (impossibility) to 1 (certainty). All possibilities allowed by the desiderata are in (2.63)–(2.64), with p any continuous monotonic increasing function with range [0,1] (pp. 33–34).

> **Intuition note.** The first rule fixes how "and" combines; the second fixes how "not" relates to "yes". A free exponent m remains, but it only relabels the scale, so one may take p as the number to compute with.

**Completeness (pp. 34–35).** Conjunction and negation are adequate to build all logic functions (noted after (1.23)), so repeated use of (2.63) and (2.64) should give the plausibility of any proposition in the Boolean algebra generated by {A₁,…,Aₙ} (p. 34). For the logical sum:
$$\begin{aligned}p(A+B|C)&=1-p(\overline A\,\overline B|C)=1-p(\overline A|C)\,p(\overline B|\overline AC)\\&=1-p(\overline A|C)[1-p(B|\overline AC)]=p(A|C)+p(\overline AB|C)\\&=p(A|C)+p(B|C)\,p(\overline A|BC)=p(A|C)+p(B|C)[1-p(A|BC)]\end{aligned}\tag{2.65}$$
$$p(A+B|C)=p(A|C)+p(B|C)-p(AB|C).\tag{2.66}$$
This generalized sum rule is "one of the most useful in applications". The primitive sum rule (2.64) is the special case B = Ā (p. 34).

Any logic function other than the trivial contradiction is a logical sum of the basic conjunctions Qᵢ, 1 ≤ i ≤ 2ⁿ (disjunctive normal form). The product rule gives each Qᵢ. Repeated use of (2.66) gives any sum of Qᵢ. Since the Qᵢ are mutually exclusive, this reduces by (2.85) to a simple sum of at most (2ⁿ − 1) terms (p. 35). Adequacy holds in this sense: whenever the background information determines the plausibilities of the basic conjunctions, the rules determine the plausibility of every proposition in the algebra. For n = 4: 2⁴ = 16 basic conjunctions determine all 2¹⁶ = 65 536 propositions. This is almost always more than a real application needs (p. 35).

> **Intuition note.** Two rules are enough: with the plausibilities of the basic conjunctions known, the plausibility of anything built from them follows by adding and multiplying.

### 2.3 Qualitative properties (pp. 35–37)

**Deductive logic as a limit (p. 35).** As p(A|B) → 0 or 1, the sum rule expresses the postulate of Aristotelian logic (if A is true, Ā is false). The strong syllogisms are
$$\frac{A\Rightarrow B,\ A\text{ is true}}{B\text{ is true}}\qquad\frac{A\Rightarrow B,\ B\text{ is false}}{A\text{ is false}}\tag{2.68}$$
Let C ≡ A ⇒ B (2.69). They correspond to the product rule in the forms
$$p(B|AC)=\frac{p(AB|C)}{p(A|C)},\qquad p(A|\overline BC)=\frac{p(A\overline B|C)}{p(\overline B|C)}.\tag{2.70}$$
From (2.68), p(AB|C) = p(A|C) and p(AB̄|C) = 0, so
$$p(B|AC)=1,\qquad p(A|\overline BC)=0.\tag{2.71}$$
Aristotelian deductive logic is the limiting form of the rules as the robot becomes more and more certain (p. 35).

**Weak syllogisms (p. 36).** First weak syllogism (A ⇒ B; B true; so A becomes more plausible) corresponds to
$$p(A|BC)=p(A|C)\,\frac{p(B|AC)}{p(B|C)}.\tag{2.73}$$
Since p(B|AC)=1 and p(B|C) ≤ 1,
$$p(A|BC)\ge p(A|C).\tag{2.74}$$
Second (A ⇒ B; A false; so B becomes less plausible):
$$p(B|\overline AC)=p(B|C)\,\frac{p(\overline A|BC)}{p(\overline A|C)}.\tag{2.76}$$
From (2.74), p(Ā|BC) ≤ p(Ā|C), so
$$p(B|\overline AC)\le p(B|C).\tag{2.77}$$
Policeman's syllogism: C is the background information. The premise "if A is true, B becomes more plausible" is
$$p(B|AC)>p(B|C),\tag{2.78}$$
and (2.73) gives at once
$$p(A|BC)>p(A|C).\tag{2.79}$$
(p. 36)

**What decides the strength of the effect (pp. 36–37).** Since p(B|AC) cannot exceed 1, a large increase in the plausibility of A can occur only when p(B|C) is very small. Example: the gentleman's behavior makes his guilt seem virtually certain because that behavior is otherwise very unlikely on the background information. Conversely, if knowing A is true raises the plausibility of B only negligibly, then observing B raises that of A only negligibly (p. 37). The author notes that many writers have demonstrated this qualitative correspondence (Keynes, Jeffreys, Pólya, Cox, Tribus, de Finetti, Rosenkrantz) (p. 37).

> **Intuition note.** Evidence B helps A in proportion to how much more likely B is when A is true than on average. A surprising observation that A predicts almost certainly is strong evidence for A.

### 2.4 Numerical values (pp. 37–43)

**Two gaps (p. 37).** (1) Each monotonic p(x) seems to give different rules, so uniqueness is unclear. (2) Nothing yet tells the robot which numerical values to assign at the start. The unused interface desiderata (IIIb), (IIIc) are invoked (p. 37).

**Sum of several propositions (pp. 37–38).** By two applications of (2.66), using (A₁+A₂)A₃ = A₁A₃ + A₂A₃ (2.81):
$$p(A_1+A_2+A_3|B)=p(A_1+A_2|B)+p(A_3|B)-p(A_1A_3+A_2A_3|B)\tag{2.80}$$
Applying (2.66) again gives seven terms:
$$\begin{aligned}p(A_1+A_2+A_3|B)&=p(A_1|B)+p(A_2|B)+p(A_3|B)\\&\quad-p(A_1A_2|B)-p(A_2A_3|B)-p(A_3A_1|B)\\&\quad+p(A_1A_2A_3|B).\end{aligned}\tag{2.82}$$
If the propositions are mutually exclusive (B implies that no two are true together)
$$p(A_iA_j|B)=p(A_i|B)\,\delta_{ij},\tag{2.83}$$
the last four terms vanish:
$$p(A_1+A_2+A_3|B)=p(A_1|B)+p(A_2|B)+p(A_3|B).\tag{2.84}$$
By induction, for n mutually exclusive propositions
$$p(A_1+\cdots+A_m|B)=\sum_{i=1}^{m}p(A_i|B),\qquad 1\le m\le n.\tag{2.85}$$
Conventional expositions usually introduce (2.85) as a basic but, as far as one can see, arbitrary axiom. Here it is deduced. If the propositions are also exhaustive (B stipulates that one and only one is true),
$$\sum_{i=1}^{n}p(A_i|B)=1.\tag{2.86}$$
This alone does not fix the individual values. Finding p(Aᵢ|B) from B can be difficult and open-ended, and the author calls it one of the most important current research problems (p. 38).

**Symmetry argument (pp. 38–40).** The author warns that this is a delicate area of controversy and asks the reader to follow only the logical analysis, setting intuition aside (pp. 38–39).

Problem I: mutually exclusive, exhaustive {A₁,…,Aₙ}; find p(Aᵢ|B)_I. Problem II: labels of the first two are interchanged:
$$A_1'\equiv A_2,\quad A_2'\equiv A_1,\quad A_k'\equiv A_k\ (3\le k\le n).\tag{2.87}$$
Find p(A′ᵢ|B)_II. The robot's state of knowledge about A₁ in I equals that about A′₂ in II (same proposition, same B), so the transformation equations hold:
$$p(A_1|B)_I=p(A_2'|B)_{II},\qquad p(A_2|B)_I=p(A_1'|B)_{II}.\tag{2.88, 2.89}$$
They hold whatever B is. Now suppose B is indifferent between A₁ and A₂, meaning that whatever B says about one it says about the other, so it gives no reason to prefer either. Then Problems I and II are entirely equivalent, including labeling. Desideratum (IIIc) (equivalent states of knowledge are represented by equivalent plausibility assignments) gives the symmetry equations
$$p(A_i|B)_I=p(A_i'|B)_{II},\qquad i=1,\dots,n.\tag{2.90}$$
Combining (2.88)–(2.90):
$$p(A_1|B)_I=p(A_2|B)_I.\tag{2.91}$$
This is a "baby" version of the group invariance principle, extended in Chapter 6 on noninformative priors (p. 40).

For any permutation {A″₁,…,A″ₙ} of {A₁,…,Aₙ} (Problem III), with A″ₖ ≡ Aᵢ:
$$p(A_i|B)_I=p(A_k''|B)_{III}\tag{2.92}$$
If B is indifferent between all Aᵢ, then
$$p(A_k|B)_I=p(A_k''|B)_{III},\qquad k=1,\dots,n,\tag{2.93}$$
and so
$$p(A_i|B)_I=p(A_k|B)_I.\tag{2.94}$$
This must hold for all n! permutations, so all p(Aᵢ|B)_I are equal. (A single cyclic permutation of order n already requires this.) With (2.86):
$$p(A_i|B)_I=\frac1n,\qquad 1\le i\le n.\tag{2.95}$$
Following Keynes (1921) this is the principle of indifference (p. 40).

> **Intuition note.** If two relabeled problems describe exactly the same knowledge, they must get the same numbers; applied to every permutation, this forces equal probabilities. The argument uses that B is indifferent among the Aᵢ (together with desideratum IIIc); the value 1/n also uses that the Aᵢ are exclusive and exhaustive, so that (2.86) holds.

**Uniqueness and importance (pp. 41–42).** If the robot assigned values different from (2.95), a mere relabeling would exhibit a second problem with the same knowledge and different assignments (p. 41). The result answers both questions. It shows, in one case that can be greatly generalized, how information gives definite numbers. It also shows that the information fixes the values of p(x) = p(Aᵢ|B), not those of the plausibilities x = Aᵢ|B. The author says this also will be found true in general (p. 41). Whatever monotonic p(x) is chosen, the same value (2.95) results, so the author concludes that there is only one consistent set of rules. Different choices of p(x) correspond only to different internal memory codes for the robot. Storing any strict monotonic function of pᵢ would give the same external behavior (p. 41). So it is better to say: "The plausibility x ≡ A|B is an arbitrary monotonic function of p, defined in (0 ≤ p ≤ 1)" (p. 41). The p's are now called probabilities. The word was avoided earlier because it was not yet shown to be uniquely determined by the data (pp. 41–42).

**Why this scale (p. 42).** The scale p is chosen not because it is more "correct" but because it is more convenient: it obeys the simplest combination rules and is directly determined by the information. Author's analogy: out of all empirical temperature scales t that are monotonic functions of each other, the Kelvin scale T is used because the laws of thermodynamics take their simplest form in it (dU = TdS − PdV, dG = −SdT + VdP). Kelvin values are "rigidly fixed" because they are directly measurable independently of any particular substance (p. 42).

**Bernoulli urn (pp. 42–43).** Ten identical balls numbered 1–10; balls 4, 6, 7 are black, the rest white; one ball is drawn blindfolded. The propositions are Aᵢ ≡ "the i-th ball is drawn". By (2.95),
$$p(A_i|B)=\frac1{10},\qquad 1\le i\le 10.\tag{2.96}$$
Drawing black means drawing 4, 6 or 7:
$$p(\text{black}|B)=p(A_4+A_6+A_7|B).\tag{2.97}$$
These are mutually exclusive, so (2.85) gives
$$p(\text{black}|B)=\frac{3}{10}.\tag{2.98}$$
In general, with N balls and A true on a specified subset of M of them (0 ≤ M ≤ N):
$$p(A|B)=\frac MN.\tag{2.99}$$
This was the original definition of probability by James Bernoulli (1713), used for the next 150 years. Laplace's *Théorie Analytique* (1812) opens with: the ratio of favorable cases to all possible cases, when nothing leads us to expect one more than another (p. 43).

### 2.5 Notation and finite-sets policy (pp. 43–44)
Formal probability uses capital P with propositions as arguments: P(A|B) (2.100). Functions of numerical arguments use other symbols, e.g. f(r|np) (2.101). Small-p notation is used loosely with arguments of either kind, to be judged by context (p. 43). The consistency theorems are established only for finite sets of propositions. Extension to infinite sets is permitted only as the result of a well-defined and well-behaved limit from a finite set (p. 43). The finite-sets policy: apply ordinary arithmetic and analysis only to expressions with a finite number of terms, and only afterward see how the finite expressions behave as the number of terms increases indefinitely. The author says this policy has been considered necessary by mathematicians from Archimedes to Gauss, and that it is consistent with Lebesgue's original definition of measure. The danger of measure-theory notation is that it presupposes the limit is already taken and does not show which limiting process was used. Different well-behaved limiting processes lead in general to different results. This is the introduction to Chapter 15 on infinite-set paradoxes, where results obtained without a limit from a finite set are said to be at best ambiguous, at worst nonsensical (p. 44).

### 2.6 Comments (pp. 44–50)

**2.6.1 "Subjective" vs. "objective" (pp. 44–45).** Any probability assignment here is "subjective" in the sense that it describes only a state of knowledge, not anything measurable in a physical experiment. **Interlocutor:** "Whose state of knowledge?" **Author:** that of the robot, or of anyone else given the same information who reasons by the desiderata. Anyone with the same information but a different conclusion violates a desideratum. The author expects a rational person to revise his thinking on discovering this (p. 44). The interface desiderata (IIIb), (IIIc) make assignments "objective" in the sense of independent of the user's personality, hopes, fears or value judgments. This is the objectivity the author says a scientific theory of inference needs (p. 45).

**2.6.2 Gödel's theorem (pp. 45–47).**
- *What was proved.* (IIIa) determined the rules. This does not prove the rules consistent. It means only that other rules which represent plausibility by real numbers but differ in content lead necessarily to inconsistencies or violations of other desiderata (p. 45).
- *Meaning of inconsistency.* The author's meaning (deriving contradictory results, e.g. P(A|BC)=1/3 and 2/3) is not really different from the logician's (some Q and Q̄ both deducible) (p. 45).
- *Fisher's argument.* A contradiction ĀA implies every proposition: A ⇒ (A+B), hence ĀA ⇒ Ā(A+B) = ĀA + ĀB ⇒ B. Let $\mathcal A$ be the axioms and T a deducible theorem: $\mathcal A \Rightarrow T$ (2.102). That T can be deduced cannot prove the axioms free of contradiction, since T would be deducible from a contradiction too. If the axioms are inconsistent, then also
$$\mathcal A\Rightarrow\overline T.\tag{2.103}$$
An inconsistency is proved by exhibiting some T and T̄ both deducible, but such a T may be hard to find (pp. 45–46). The author calls this the intuitive reason for Gödel's result, while saying no logician would accept it as a proof of the full theorem (p. 46).
- *Probability as a consistency tester.* Gödel's theorem says only that no such procedure derivable from the tested axioms exists. Probabilities conditional on contradictory premises do not exist (the hypothesis space is empty). A program computing p(B|E), with E = E₁E₂…Eₙ, will crash if a contradiction is hidden in E. The author says they discovered this "empirically". If the program prints valid numbers, the Eᵢ are mutually consistent. This does not conflict with Gödel because probability theory appeals to principles not derivable from the propositions tested (p. 46).
- *Undecidability.* Many simple questions are undecidable by deduction. Example: two sole witnesses give opposite testimony and then die; one lied, but which one cannot be determined. Undecidability signals incomplete information. In a formal system, new axioms external to it might decide the proposition (pp. 46–47). The author expects Gödel's result to be seen as "more of a platitude than a paradox"; undecidability merely signals a problem calling for inference rather than deduction (p. 47).
- *Status.* Whether probability theory's consistency can be proved with external principles is "an open question". The author reports no inconsistency from correct application. Apparent ones proved to be misapplications. Inconsistencies in ad hoc rules are easily exhibited, guided by Cox's theorems (examples in Chapters 5, 15, 17) (p. 47).

**2.6.3 Venn diagrams (pp. 47–49).**
- **Interlocutor:** why not illustrate (2.104) by a Venn diagram? **Author:** it is useful in one special case but can mislead.
$$P(A+B|C)=P(A|C)+P(B|C)-P(AB|C).\tag{2.104}$$
- If probability is area, the subregions of A must represent mutually exclusive subpropositions ωᵢ, and B and C must resolve into the same ωᵢ. This assumes that propositions correspond to sets of points, A+B to the union and AB to the intersection, with probabilities as an additive measure. The general theory has no such structure; these are properties only of the diagram (p. 48).
- Typical propositions (A ≡ "it will rain today" (2.105), B ≡ "the roof will leak" (2.106)) are declarative statements that may not be resolvable into more elementary ones in the problem's context. A resolution can be forced by irrelevancies (B = BC₁+⋯+BC_N, with Cₖ ≡ "the number of penguins in Antarctica is k") (2.107), but that is idle. A resolution can also be useless (every raindrop trajectory for forecasting rain); real problems have a natural end to resolving. Chapter 8 ("Sam's broken thermometer") is to show this. Sometimes a resolution is a useful device, e.g. (2.98) (pp. 48–49).
- A and B would seldom be resolvable into the same set ωᵢ, and the author reserves the right to add propositions D, E, F, … So AB means only "both A and B are true", and p(AB|C) is an elementary quantity in its own right. Boole's notation A+B, AB is kept to avoid set-theory associations. The author prefers to say that (2.104) explains and justifies the Venn diagram in one special case (p. 49).

**2.6.4 The "Kolmogorov axioms" (pp. 49–50).** Kolmogorov (1933) phrased probability in set and measure theory, which was becoming fashionable. The author says this gives some modern works the impression that probability theory started with him. Kolmogorov formalized the Venn-diagram picture. Per the author, Appendix A shows that, for all practical purposes, his four axioms (first stated arbitrarily, for which he has been criticized) are all derived in this chapter from the consistency requirements. The author therefore expects to defend Kolmogorov against critics on technical points (p. 49). Conceptually the systems differ: here propositions are not interpreted as sets, and probability distributions are interpreted as carriers of incomplete information. As a result the author claims analytical resources absent from the Kolmogorov system, enabling "ill posed" and "generalized inverse" problems that the Kolmogorov system would put outside probability theory (p. 50).

## Toy example (ours, not from the text)
An urn holds 5 balls: balls 1 and 2 are red, balls 3, 4, 5 are white. We draw two balls in turn without replacement. The background information B says only this.

1. Indifference (2.95): the first draw has p = 1/5 for each ball. So P(R₁|B) = 1/5 + 1/5 = 2/5, by (2.85).
2. Given R₁, four balls remain (one red, three white), and B is indifferent among them. So P(R₂|R₁B) = 1/4.
3. Product rule (2.63): P(R₁R₂|B) = 2/5 · 1/4 = 1/10.
4. Sum rule (2.64): P(R̄₁|B) = 1 − 2/5 = 3/5. Given R̄₁, the four balls left are 2 red and 2 white, so P(R₂|R̄₁B) = 2/4. Then P(R̄₁R₂|B) = 3/5 · 1/2 = 3/10.
5. P(R₂|B) = P(R₁R₂|B) + P(R̄₁R₂|B) = 1/10 + 3/10 = 2/5.
6. Generalized sum rule (2.66): P(R₁+R₂|B) = 2/5 + 2/5 − 1/10 = 7/10. Check: P(no red) = 3/5 · 2/4 = 3/10, and 1 − 3/10 = 7/10 ✓.
7. The scale is free (p. 41). Take w = p^{1/2} (m = 2). Then w(R₁) = √0.4 ≈ 0.6325 and w(R̄₁) = √0.6 ≈ 0.7746, and w²(R₁) + w²(R̄₁) = 0.4 + 0.6 = 1 (the form (2.60)). The product rule holds in the form (2.28): w(R₁R₂) = √0.1 ≈ 0.3162 and w(R₁)w(R₂|R₁) = 0.6325 · 0.5 = 0.3162. Computing with w or with p gives the same conclusions. Only p, not w, is directly fixed by the data (1/5 each) (compare p. 41).

## Concepts
- [[probability-as-extended-logic]] — probability as the unique consistent calculus of plausibility, extending deductive logic (p. 35)
- [[cox-theorem]] — consistency requirements force the product and sum rules; here via functional equations (2.13) and (2.45) (pp. 27–33)
- [[desiderata]] (new) — (I) real-number plausibilities, (II) qualitative common sense, (III) consistency (IIIa structural, IIIb, IIIc interface), as used in this chapter (p. 24)
- [[product-rule]] (new) — p(AB|C) = p(A|C)p(B|AC) = p(B|C)p(A|BC), derived from associativity (pp. 29, 33)
- [[sum-rule]] (new) — p(A|B)+p(Ā|B)=1, with the generalized form P(A+B|C)=P(A|C)+P(B|C)−P(AB|C) (pp. 33–34)
- [[associativity-equation]] (new) — F[F(x,y),z]=F[x,F(y,z)]; Jaynes follows Cox's differentiable proof (p. 27)
- [[principle-of-indifference-maxent]] — Jaynes derives p=1/n from a relabeling symmetry for exclusive, exhaustive propositions with indifferent information; the "baby" group-invariance argument (pp. 38–40). The maximum-entropy side of the canon id is not stated here.
- [[weak-syllogism]] (new) — quantitative forms of the inductive syllogisms, including the policeman's syllogism, from (2.73) (pp. 36–37)
- [[mutually-exclusive-exhaustive]] (new) — pairwise incompatible and exactly one true; gives (2.85) and (2.86) (p. 38)
- [[finite-sets-policy]] (new) — apply arithmetic and analysis only to finite expressions, then take limits (p. 44)
- [[subjective-personal-probability]] — Jaynes's sense: probability describes a state of knowledge, yet is objective in being independent of the user's personality (pp. 44–45)
- [[consistency-and-godel]] (new) — Fisher's argument; probabilities conditional on contradictory premises do not exist, so a program would crash (pp. 45–46)
- [[kolmogorov-axioms]] (new) — set/measure-theoretic formalization; per Jaynes, its four axioms are derived here "for all practical purposes" (p. 49)

## Canonical instances
- [[bernoulli-urn]] — ten balls, three black: p(black)=3/10; general M/N (p. 42)
- [[blue-eyes-black-hair]] — why (AB|C) cannot be a function of (A|C) and (B|C) alone (p. 25)
- [[policeman-syllogism]] — behavior B raises guilt A when B is otherwise very unlikely (pp. 36–37)
- [[kelvin-scale-analogy]] — choosing p like choosing the Kelvin temperature scale (p. 42)
- [[two-witnesses]] — undecidability as incomplete information (p. 47)
- [[penguins-resolution]] — forced irrelevant resolution of B into BCₖ (p. 48)
- [[sams-broken-thermometer]] — announced for Chapter 8 only; not worked here (p. 49)

## Bridges (candidates)
- [structural-analogy] Product rule (2.63) ↔ information-theory chain rule: taking −log of p(AB|C)=p(B|C)p(A|BC) gives additive surprisal, and in expectation the chain rule H(X,Y)=H(X)+H(Y|X). The unit does not itself state this log step, and the entropy version needs logs and expectations.
- [same-math] Weak syllogism (2.73) ↔ Bayes' theorem: p(A|BC)=p(A|C)p(B|AC)/p(B|C) is posterior ∝ prior × likelihood (canon link; not stated in this unit).
- [structural-analogy] Principle of indifference (2.95) ↔ maximum entropy: the uniform distribution maximizes entropy when only normalization is known, though the unit derives it by a symmetry argument, not by optimization (canon link; not stated in this unit).
- [structural-analogy] Choosing p over arbitrary monotonic x ↔ choosing a canonical scale in physics (Kelvin): the content is invariant, the scale is chosen for simple laws (p. 42).
- [structural-analogy] Cox-style functional equations ↔ Dutch book argument: both argue that consistency constraints force the probability calculus.
- [structural-analogy] "Probabilities conditional on contradictory premises do not exist" ↔ conditioning on an empty event is undefined in measure-theoretic probability.

## Questions this raises
- The symmetry argument needs "indifference" in B. What principles turn richer information (not just symmetry) into numbers p(Aᵢ|B)? (The author calls this an open-ended research problem; p. 38.)
- Cox's proof assumes differentiability and Aczél's does not. Does dropping it change anything for the applications? (The author calls the assumption innocuous; p. 33.)
- How exactly does a limit from a finite set of propositions to an infinite one go wrong when the limiting process is not specified? (Promised for Chapter 15; p. 44.)
- Can consistency of the rules be proved using principles external to probability theory? (The author says this is open; p. 47.)

## Exercises worth doing
- Ex. 2.1 (p. 34) — whether a formula for p(C|A+B) analogous to (2.66) follows from the product and sum rules; tests understanding of what the rules do and do not give — difficulty: medium
- Ex. 2.2 (p. 34) — show that p(C|A₁+⋯+Aₙ X) is a weighted average of the p(C|AᵢX), formula (2.67), for mutually exclusive Aᵢ — difficulty: medium
- Ex. 2.3 (p. 43) — bounds on P(AB|C) and P(A+B|C) from a = P(A|C) ≤ b = P(B|C), with sharper bounds when a+b>1 or a+b<1; helpful in detecting calculation errors — difficulty: medium

## Reading notes
- The source PDF pages run 54–80; the printed pages are 24–50 (offset 30). All page numbers above are printed.
- Overbars (negations) and primes are often lost in the text layer; all formulas were checked against the page images.
- p. 31: the page prints "(2.25) becomes a functional equation" before (2.45). The surrounding derivation shows the starting equation is (2.40), so "(2.25)" appears to be a misprint for (2.40).
- p. 38: in (2.84), the second and third terms are printed with capital P ("P(A₂|B)", "P(A₃|B)") while the others use small p. This is a typographical inconsistency only.
- p. 34, Exercise 2.2: the formula (2.67) is printed with a missing closing parenthesis in "p(C|(A₁+⋯+AₙX)"; I read it as p(C|(A₁+⋯+Aₙ)X).
- Everything in this unit is reported from the printed text; appendices referred to (A, B), Chapters 6, 8, 15, 17 and Aczél's and Cox's proofs were not available and are not summarized.
