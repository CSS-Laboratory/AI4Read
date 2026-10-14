---
id: popper-1959-logic/appii-following
work: popper-1959-logic
unit: Appendices i–iii (dimension of a theory; general calculus of frequency in finite classes; first binomial formula)
pages: 283–292
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Popper, Appendices i–iii: dimension of a theory, finite-class frequency calculus, binomial formula

## L0 — One line
Popper gives a provisional definition of a theory's dimension, then derives the multiplication, addition, division and Bayes rules for frequencies in finite classes, and the first binomial formula, mostly by counting from definitions, with induction for the binomial formula.

## L1 — The gist (≤ 120 words)
These appendices supply technical support for the main text. Appendix i gives a provisional definition of a theory's dimension, using d-tuples (conjunctions of d singular statements) and falsifying d+1-tuples. It circumvents, rather than overcomes, the lack of a metric or neighbourhood structure on the field of application. Appendix ii derives multiplication, addition, division and four Bayes forms for relative frequencies in finite classes; the general theorems are identities. Appendix iii proves the first binomial formula for finite sequences of overlapping segments by mathematical induction, assuming freedom from after-effect. The main ideas: the general frequency rules follow from definitions and counting, and the theory itself determines which singular statements count as "relatively atomic".

**Prerequisites:** sets and conjunction; counting elements of a set, N(·); relative frequency as a ratio of counts; binomial coefficient; mathematical induction.

## L2 — Key ideas
- Popper's provisional definition: a theory is d-dimensional iff it clashes with no d-tuple (conjunction of d) of field statements, and any d-tuple plus the theory splits the other statements into falsifiers and compatible classes (p. 284).
- The "atomic statements" problem gets a "deductivist" answer: the theory itself fixes which singular statements are relatively atomic (p. 284–285).
- Footnote version: the dimension d(a) of a law a is the number n such that any conjunction of n field statements is compatible with a, and for any such conjunction some further statement x clashes with a together with it (plus a second condition on y) (p. 283). 1/d(a), or 1/(d(a)+1), may serve as a simplicity measure (p. 283).
- The general multiplication theorem is an identity after cancelling N(α.β) (p. 286–287).
- Independence may be described as a special case of selection (a class selected from α by a property), and its symmetry can be proved with the help of the equivalence of (1) and (1′) (p. 287–288).
- The addition theorems rest on class-calculus identities. The special form holds for all primary properties within α, since these exclude one another (p. 287–288).
- All Bayes forms are special cases of the division theorem; the fourth gives frequencies of the β_i within a γ-selection (p. 288–289).
- Formula (2), the frequency of one particular arrangement, is proved by induction on n, assuming an after-effect-freedom condition that lets successive places multiply; (1) then follows from (2) by the nCm count of arrangements and the special addition theorem (p. 290–292).

## L3 — Walkthrough

### Appendix i — Dimension of a theory (cf. §§38–39)
**Aim and difficulty.** Popper calls the definition provisional. It should match the dimension of the set of curves obtained when the field of application is drawn on graph paper. We should not assume that the field has a metric, a topology or neighbourhood relations. He admits the definition circumvents this difficulty and does not overcome it (p. 283).

**Circumvention.** Popper links the possibility of circumventing the difficulty to the fact that a theory always prohibits some "homotypic" events, i.e. occurrences differing only in spatio-temporal coordinates. So such coordinates will generally appear in the schema generating the field. The relatively atomic statements will then generally show a topological and even metrical order (p. 284).

**Definition.** A theory $t$ is *d-dimensional with respect to the field of application F* iff there is a number $d$ such that (p. 284):
- (a) the theory does not clash with any d-tuple of the field;
- (b) any given d-tuple, conjoined with the theory, divides all remaining relatively atomic statements uniquely into two infinite sub-classes A and B, where
  - (α) every statement of A, conjoined with the d-tuple, forms a "falsifying d+1-tuple", i.e. a potential falsifier;
  - (β) B is the sum of one or more, but always a finite number of, infinite sub-classes $B_i$. The conjunction of any number of statements from any one $B_i$ is compatible with the d-tuple and the theory.

**Purpose and "deductivist" reading.** The definition is intended to exclude a theory's having two fields of application where the atomic statements of one are conjunctions of those of the other. This exclusion is needed if the field is to be identifiable with its graphic representation (p. 284). Popper adds that the problem of atomic statements is solved in a manner that might be described as "deductivist": the theory itself determines which singular statements are relatively atomic. They are not found as elementary statements from which others are built inductively or by truth-functions. Instead the relatively atomic statements (and with them the singular statements) appear as "a sort of precipitation, as it were", or a "(relatively) solid deposit", laid down by the theory's universal statements (p. 284–285).

**Footnote *1 (simplified, more general definition).** Let A and X be sets of statements. X is a homogeneous field of application with respect to A (X = $F_A$) iff for every $a$ in A there is a natural number $d(a)=n$ such that (p. 283):
- (i) any conjunction $c_n$ of $n$ different statements of X is compatible with $a$;
- (ii) for any such $c_n$ there are $x, y$ in X such that $x.c_n$ is incompatible with $a$, and $y.c_n$ is derivable from $a.c_n$ but neither from $a$ nor from $c_n$.

$d(a)$ is the dimension, or degree of composition, of $a$; 1/d(a) or 1/(d(a)+1) may be taken as a measure of simplicity. Appendix *viii develops this further (p. 283).

*Intuition note.* The dimension counts how many field statements you can hold fixed before the next one can contradict the law. On the proposed measure 1/d(a), a law with smaller d counts as simpler (p. 283). The theory, not a prior metric, picks out the statements that play the same role.

### Appendix ii — General calculus of frequency in finite classes (cf. §§52–53)
Notation: α is the finite reference class; β, γ are property classes; ${}_\alpha F''(\beta)$ is the relative frequency of β in α. Popper later developed this appendix into an axiomatic treatment of probability (appendices *iii–*v) (p. 286).

**General multiplication theorem** (p. 286):
$$ {}_\alpha F''(\beta.\gamma) = {}_\alpha F''(\beta)\cdot {}_{\alpha.\beta}F''(\gamma) \tag{1}$$
$$ {}_\alpha F''(\beta.\gamma) = {}_{\alpha.\gamma}F''(\beta)\cdot {}_\alpha F''(\gamma) \tag{1′}$$
Proof, by substituting the §52 definition in (1) (p. 287):
$$\frac{N(\alpha.\beta.\gamma)}{N(\alpha)}=\frac{N(\alpha.\beta)}{N(\alpha)}\cdot\frac{N(\alpha.\beta.\gamma)}{N(\alpha.\beta)} \tag{1,1}$$
This is an identity after cancelling $N(\alpha.\beta)$. Popper contrasts this proof with Reichenbach's (p. 287).

**Independence** (§53) is the condition
$$ {}_{\alpha.\beta}F''(\gamma)={}_\alpha F''(\gamma) \qquad (1^s)$$
It gives the special multiplication theorem
$$ {}_\alpha F''(\beta.\gamma)={}_\alpha F''(\beta)\cdot{}_\alpha F''(\gamma) \qquad (1_s)$$
With the help of the equivalence of (1) and (1′), the symmetry of independence can be proved (p. 287).

**Addition theorems.** Between class names, "+" means non-exclusive "or". The general theorem (p. 287):
$$ {}_\alpha F''(\beta+\gamma)={}_\alpha F''(\beta)+{}_\alpha F''(\gamma)-{}_\alpha F''(\beta.\gamma) \tag{2}$$
It follows from the §52 definition together with two universally valid formulas:
$$\alpha.(\beta+\gamma)=(\alpha.\beta)+(\alpha.\gamma) \tag{2,2}$$
$$N(\beta+\gamma)=N(\beta)+N(\gamma)-N(\beta.\gamma) \tag{2,1}$$
If β and γ have no common member within α, i.e. $N(\alpha.\beta.\gamma)=0$ $(2^s)$, then (p. 287–288):
$$ {}_\alpha F''(\beta+\gamma)={}_\alpha F''(\beta)+{}_\alpha F''(\gamma) \qquad (2_s)$$
This holds for all primary properties within α, since they exclude one another. Their relative frequencies sum to 1 (p. 288).

**Division theorems.** Inverting (1) gives the frequency of γ in a class selected from α by β (p. 288):
$$ {}_{\alpha.\beta}F''(\gamma)={}_\alpha F''(\beta.\gamma)/{}_\alpha F''(\beta) \tag{3}$$
With the special multiplication theorem this becomes ${}_{\alpha.\beta}F''(\gamma)={}_\alpha F''(\gamma)$ $(3^s)$, which is condition $(1^s)$. So independence is a special case of selection (p. 288).

**Bayes's theorems.** The various theorems that may be connected with Bayes's name are all special cases of the division theorem (3) (p. 288–289).
- *First form.* Assume $\alpha.\gamma\subset\beta$ $(3^{bs})$. Then
$$ {}_{\alpha.\beta}F''(\gamma)={}_\alpha F''(\gamma)/{}_\alpha F''(\beta) \qquad (3_{bs})$$
(added step: here $\alpha.\beta.\gamma=\alpha.\gamma$, so the numerator of (3) is ${}_\alpha F''(\gamma)$.)
- *Second form* (universally valid), using the sum $\Sigma\beta_i$ of classes $\beta_1,\dots,\beta_n$:
$$ {}_{\alpha.\Sigma\beta_i}F''(\beta_i)={}_\alpha F''(\beta_i)/{}_\alpha F''(\Sigma\beta_i) \qquad (3_b)$$
- *Third form.* Assume $N(\alpha.\beta_i.\beta_j)=0$ for $i\neq j$ $(3/2^s)$. Then $(2_s)$ applies to the sum $\Sigma\beta_i$ in $(3_b)$ (the text says "numerator", but the sum stands in the denominator), giving
$$ {}_{\alpha.\Sigma\beta_i}F''(\beta_i)={}_\alpha F''(\beta_i)\Big/\Big(\Sigma\,{}_\alpha F''(\beta_i)\Big) \qquad (3/2_s)$$
It is always applicable to primary properties $\beta_i$ (p. 289).
- *Fourth form* ("most important"). Assume $(3/2^s)$ and $\alpha.\gamma\subset\Sigma\beta_i$ $(4^{bs})$, which is always satisfied if $\gamma\subset\Sigma\beta_i$.
  - Substitute $\beta_i\gamma$ for $\beta_i$ in $(3/2_s)$.
  - Apply $\alpha.\Sigma\beta_i.\gamma=\alpha.\gamma$ $(4^{bs}.1)$ on the left.
  - Apply (1′) to numerator and denominator on the right.
$$ {}_{\alpha.\gamma}F''(\beta_i)=\frac{{}_{\alpha.\beta_i}F''(\gamma)\cdot{}_\alpha F''(\beta_i)}{\Sigma\big({}_{\alpha.\beta_i}F''(\gamma)\cdot{}_\alpha F''(\beta_i)\big)} \qquad (4_s)$$
So, in the text's words, if $\beta_i$ is an exclusive system of property classes "and any property class which is (within α) part of βi" (unclear wording; see Reading notes), $(4_s)$ gives the frequency of each $\beta_i$ in the selection by γ (p. 289).

*Intuition note.* These rules are counting facts about a finite class. In our words, the theorems restate a fraction of a fraction and an overlap counted once. Bayes's rule re-weights the fractions of the $\beta_i$ by how often γ occurs inside each.

### Appendix iii — First binomial formula (finite sequences of overlapping segments, cf. §56)
**Claim.** With $p={}_\alpha F''(1)$, $q={}_\alpha F''(0)$, $m\le n$ (p. 290):
$$ {}_{\alpha_{(n)}}F''(m)={}^nC_m\,p^mq^{n-m} \tag{1}$$
It may be said to be proved, neglecting errors at the last term (cf. §56), under the assumption that α is at least $(n-1)$-free (from after-effect), if we can show
$$ {}_{\alpha_{(n)}}F''(\sigma_m)=p^mq^{n-m} \tag{2}$$
Here $\sigma_m$ is one particular n-tuple with $m$ ones; its complete arrangement is given, not only the count of ones (p. 290).

**From (2) to (1).** Assume (2) holds for all $n, m, \sigma$. By a well-known combinatorial theorem there are ${}^nC_m$ distinct ways of distributing $m$ ones in $n$ places, and in view of the special addition theorem we could then assert (1) (p. 291).

**Induction step.** Suppose (2) holds for one $n$, and for all $m$ and $\sigma$ compatible with it. We show (p. 291):
$$ {}_{\alpha_{(n+1)}}F''(\sigma_{m+0})=p^mq^{n+1-m} \tag{3,0}$$
$$ {}_{\alpha_{(n+1)}}F''(\sigma_{m+1})=p^{m+1}q^{(n+1)-(m+1)} \tag{3,1}$$
Here $\sigma_{m+0}$, $\sigma_{m+1}$ are the length-$(n+1)$ sequences made by adding a 0 or a 1 at the end of $\sigma_m$. Assume α is at least $(n-1)$-free for every length $n$, so for segments of length $n+1$ it is at least $n$-free. Let $\acute\sigma_m$ be the property of being a successor of an n-tuple $\sigma_m$. Then (p. 291):
$$ {}_\alpha F''(\acute\sigma_m.0)={}_\alpha F''(\acute\sigma_m)\cdot{}_\alpha F''(0)={}_\alpha F''(\acute\sigma_m)\cdot q \tag{4,0}$$
$$ {}_\alpha F''(\acute\sigma_m.1)={}_\alpha F''(\acute\sigma_m)\cdot{}_\alpha F''(1)={}_\alpha F''(\acute\sigma_m)\cdot p \tag{4,1}$$
(The text asserts these once the freedom assumption is made.) There are as many successors of $\sigma_m$ in α as sequences $\sigma_m$ in $\alpha_{(n)}$, so
$$ {}_\alpha F''(\acute\sigma_m)={}_{\alpha_{(n)}}F''(\sigma_m) \tag{5}$$
and, for the same reason,
$$ {}_\alpha F''(\acute\sigma_m.0)={}_{\alpha_{(n+1)}}F''(\sigma_{m+0}) \tag{6,0}$$
$$ {}_\alpha F''(\acute\sigma_m.1)={}_{\alpha_{(n+1)}}F''(\sigma_{m+1}) \tag{6,1}$$
Substituting (5) and (6) in (4) (p. 292):
$$ {}_{\alpha_{(n+1)}}F''(\sigma_{m+0})={}_{\alpha_{(n)}}F''(\sigma_m)\cdot q \tag{7,0}$$
$$ {}_{\alpha_{(n+1)}}F''(\sigma_{m+1})={}_{\alpha_{(n)}}F''(\sigma_m)\cdot p \tag{7,1}$$
So if (2) holds for some $n$, (3) follows by mathematical induction. (Added step: $p^mq^{n-m}\cdot q=p^mq^{n+1-m}$ and $p^mq^{n-m}\cdot p=p^{m+1}q^{(n+1)-(m+1)}$.) (2) holds for $n=2$ and all $\sigma_m$ ($m\le 2$), seen by taking first $m=1$, then $m=0$. Hence (3), (2) and (1) are asserted (p. 292).

*Intuition note.* Each particular arrangement of ones and zeros has relative frequency $p^mq^{n-m}$ in $\alpha_{(n)}$, because each new place multiplies in $p$ or $q$. Freedom from after-effect is what lets the factors multiply. Counting arrangements then gives the binomial coefficient.

## Toy example (ours)
Let α have 10 elements. β₁ has 6, β₂ has 4 (exclusive, together all of α). γ has 4 elements: 3 in β₁, 1 in β₂.
- Multiplication (1): ${}_\alpha F''(\beta_1)=6/10=.6$; ${}_{\alpha.\beta_1}F''(\gamma)=3/6=.5$; product $.3=3/10={}_\alpha F''(\beta_1.\gamma)$ ✓.
- Addition (2): $\beta_1+\gamma$ has $6+4-3=7$ members, so $.7=.6+.4-.3$ ✓.
- Bayes $(4_s)$: ${}_{\alpha.\beta_2}F''(\gamma)=1/4=.25$, ${}_\alpha F''(\beta_2)=.4$. Numerators: $.5\cdot.6=.3$ and $.25\cdot.4=.1$; denominator $.3+.1=.4$. So ${}_{\alpha.\gamma}F''(\beta_1)=.3/.4=.75=3/4$, matching direct counting (3 of the 4 γ-elements lie in β₁) ✓.

## Concepts
- [[dimension-of-theory]] (new) — number $d$ such that no d-tuple of field statements clashes with the theory, but a d-tuple plus the theory sorts the rest into falsifiers and compatible classes (p. 284).
- [[field-of-application]] (new) — set of singular statements generated by the theory's schema; "homogeneous" in the footnote sense (p. 283–284).
- [[relatively-atomic-statement]] (new) — singular statement whose status as "atomic" is fixed by the theory, not by elementary form (p. 284–285).
- [[falsifiability]] — here the potential falsifier is a falsifying d+1-tuple (p. 284).
- [[relative-frequency-finite-class]] (new) — ${}_\alpha F''(\beta)=N(\alpha.\beta)/N(\alpha)$ (p. 287).
- [[independence-frequency]] (new) — $\gamma$ is independent of β in α iff $(1^s)$ holds; independence is symmetric and is a special case of selection (p. 287–288).
- [[bayes-theorem-finite-frequency]] (new) — special forms of the division theorem; $(4_s)$ is the fourth (p. 288–289).
- [[freedom-from-after-effect]] (new) — "n-free" (defined in the main text, not on these pages); assumed, so that successive places multiply in (4,0)–(4,1) of the binomial proof (p. 290–291).

## Canonical instances
None named. The appendices contain only formulas and definitions, no worked cases.

## Bridges (candidates)
- [same-math] special multiplication theorem $(1_s)$ ↔ probability: product rule for independent events — the same counting identity in frequency form.
- [same-math] fourth form of Bayes $(4_s)$ ↔ Bayesian confirmation: posterior from priors and likelihoods — same formula, but here read as frequencies in a finite class, not degrees of belief.
- [structural-analogy] dimension $d(a)$ and simplicity $1/d(a)$ ↔ statistics/model selection: number of free parameters as complexity — both tie complexity to the amount of data needed to refute.
- [structural-analogy] theory deciding what is "atomic" ↔ analytic philosophy: theory-laden observation — the vocabulary of basic statements depends on the theory.

## Questions this raises
- Why does Popper accept a definition that circumvents the missing topology of the field, and what could overcome it?
- How strong is the assumption of freedom from after-effect, and what happens to the binomial formula if it fails?
- What does the axiomatic treatment in appendices *iii–*v add to this finite-class calculus?
- How is the later development of dimension in appendix *viii different from this provisional version?

## Reading notes
- Printed page = pdf − 29 (pdf 312–321 = printed 283–292). This unit includes Appendix i, as well as Appendices ii and iii.
- Misprint: p. 290 prints "n − I-free" (capital I) in both the text layer and the image; p. 291 prints "n − 1-free", which is evidently intended. The sub/superscript labels $(1^s)$ vs. $(1_s)$ and $(3^{bs})$ vs. $(3_{bs})$ are garbled in the text layer; I took them from the images. The second condition for $(3^{bs})$ is printed "(3bs)" twice in the text, for the assumption and for the result.
- Page 289: the closing sentence says "any property class which is (within α) part of βi". Given the assumption $(4^{bs})$, this presumably means γ (or $\gamma\subset\Sigma\beta_i$). I did not change the formula.
- Page 287: the Reichenbach reference cites the proof of $(2_s)$; the image shows the subscript clearly.
- The word "denumerator" on p. 289 ("both to the denumerator and denominator") is as printed; it evidently stands for "numerator".
- Page 289: the text says the special addition theorem is applied "to the numerator" of $(3_b)$. The sum $\Sigma\beta_i$ stands in the denominator, so L3 says denominator and notes the wording.
- Appendix iii proves the induction step before the base case; the base case is stated at n = 2.
