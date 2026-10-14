---
id: popper-1959-logic/appiv-untitled-2
work: popper-1959-logic
unit: "Appendix *iv — The Formal Theory of Probability"
pages: 329–355
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Appendix *iv — The Formal Theory of Probability

## L0 — One line
Popper builds a six-axiom system for relative probability p(a, b) that does not fix what a and b are, lets p(a, b) be defined even when b has probability zero, and from which the Boolean laws can be derived once Boolean equivalence is defined by formula (*).

## L1 — The gist (≤ 120 words)
Popper asks for a truly formal calculus of probability, one whose "elements" can be statements, sets or other things. He argues that Kolmogorov and others tacitly assume Boolean algebra, and that customary systems cannot treat conditions of probability zero. He offers a "symmetrical" system whose probability axioms, with Boolean equivalence defined by (*), yield the Boolean laws. He gives models showing the system is consistent and each axiom independent. He then defines Borel fields of probabilities in his own terms; he says every Borel field in Kolmogorov's sense is one in his. He cares because universal laws may be assumed to have probability zero, yet p(s, t) and the likelihood p(e, t) should stay defined for corroboration.

**Prerequisites:** conditional probability p(a|b) = p(ab)/p(b); Boolean algebra (product, complement); limits of sequences; what "consistent" (a model exists) and "independent" (not derivable from the others) mean for axioms.

## L2 — Key ideas (5–10 bullets)
- Popper wants a probability calculus that is formal (no fixed interpretation), autonomous (probabilities only from probabilities) and symmetrical (p(a, b) is defined whenever p(b, a) is, even if p(b) = 0) (p. 330).
- Popper argues that existing "abstract" systems (Kolmogorov's) still assume a more or less specific interpretation, e.g. that the elements are sets, so they are not fully formal (pp. 330–331).
- Formulae (d) and (e) alone, with substitutivity of equal probabilities, imply a form of the associative law; assuming the Boolean laws first hides what the probability axioms imply (pp. 332–333).
- In customary systems most relative-probability formulae need a prefixed condition p(b) ≠ 0. Popper says authors who overlooked this (Jeffreys, von Wright) have inconsistent systems, and authors who saw it have very weak ones. Such systems cannot properly treat statements of probability zero, such as universal laws (pp. 333–335).
- The system rests on six axioms A1, A2, A3, B1, B2, C. C is the only axiom with a proviso of the "if p(b) ≠ 0" kind. Alternative systems with four or three axioms are given (pp. 336–340).
- Consistency is shown by finite and denumerable models; independence by countermodels for each axiom and postulate, which Popper believes is new for probability (pp. 342–348).
- The Boolean laws are derivable if Boolean equivalence is defined by (*). The axioms stay non-redundant even if Boolean algebra is postulated, apart from the exceptions Popper names ("autonomous independence") (pp. 349–350).
- A Boolean product element of a decreasing sequence lets Popper state a version of Kolmogorov's continuity axiom and of Borel fields. The example of the missing half-interval separates the Boolean product from the set-theoretic product (pp. 350–355).

## L3 — Walkthrough

### 0. Aims (pp. 329–331)
- Popper says p(a, b) = r can be interpreted in many ways. He therefore wants a purely formal, abstract or autonomous system: its elements a, b, … can be interpreted in many ways and no single interpretation binds us (p. 329). He first proposed such a system in a 1938 Note in *Mind* (reprinted in appendix *ii) and has since built many simplified ones (p. 329).
- A *complete* formalization would still need an embedding in some mathematical formalism; Tarski's elementary algebra would suffice (n. 1, p. 329).
- Footnote 1 asks whether a decision procedure (a mechanical test of provability) exists for Tarski's algebra plus A1, B and C⁺. The answer is no. The footnote's argument: the system proves that there is an a in S with $p(a,\bar a) \neq p(\bar a,a)$. Adding formula (0), saying that for every a in S $p(a,\bar a) \neq p(\bar a,a)$, would force exactly two elements. The consistency models given below show that S may have any number of elements. So (0), and all similar formulae fixing the size of S, can be neither derived nor refuted: the system is incomplete (n. 1, pp. 329–330).
- Three marks of the theory (p. 330):
  - **Formal:** it assumes no particular interpretation, while allowing at least all known interpretations.
  - **Autonomous:** probability conclusions can be derived only from probability premises. The calculus transforms probabilities into other probabilities.
  - **Symmetrical:** whenever p(b, a) exists, p(a, b) also exists, even when p(b) = p(b, aā) = 0.
- Popper says a theory of this kind does not seem to have existed before his own attempts. Others, such as Kolmogorov, intended an abstract theory but always assumed a more or less specific interpretation: the elements are statements (or systems of statements), sets (or systems of sets), properties, or finite classes (p. 330).
- **Kolmogorov's view (as Popper reports it):** probability theory can and should be developed from axioms, in the same way as geometry and algebra; Kolmogorov refers to Hilbert's *Foundations of Geometry* (p. 330). **Popper's objection:** Kolmogorov still takes a and b to be sets. This excludes, among others, the reading of a and b as statements. Popper says Kolmogorov rightly remarks that what the members of the sets represent is of no importance, but this does not secure formality, because in some interpretations a and b have no members (pp. 330–331).
- Whoever reads the elements as statements assumes the propositional calculus; Kolmogorov assumes set operations. Laws such as (a) $(ab)c = a(bc)$, (b) $ab = ba$ and (c) $a = aa$ are always presupposed, often only tacitly, before the probability axioms are laid down (p. 331).

### 1. The Boolean laws are partly consequences, not premises (pp. 332–333)
Popper's claim: some of the adopted postulates for relative probability alone guarantee that the Boolean laws hold for the elements (p. 332). Take

$$p(ab) = p(a,b)\,p(b) \tag{d}$$
$$p(ab,c) = p(a,bc)\,p(b,c) \tag{e}$$

(d) also gives rise to a kind of definition of relative probability by absolute probability:
$$\text{If } p(b)\neq 0 \text{ then } p(a,b) = p(ab)/p(b) \tag{d$'$}$$
(e) is the well-known general law of multiplication. (d) and (e) entail, with no further assumption except substitutivity of equal probabilities,
$$p((ab)c) = p(a(bc)). \tag{f}$$
Derivation (n. 3, p. 332):
1. $p((ab)c) = p(ab,c)\,p(c)$ by (d).
2. $p((ab)c) = p(a,bc)\,p(b,c)\,p(c)$ by 1 and (e).
3. $p(a(bc)) = p(a,bc)\,p(bc)$ by (d).
4. $p(a(bc)) = p(a,bc)\,p(b,c)\,p(c)$ by 3 and (d).
5. $p((ab)c) = p(a(bc))$ by 2 and 4.

If one instead assumes the law (a) first, (f) follows trivially by substitution into $p(x) = p(x)$. The derivability of (f) from (d) and (e) then goes unnoticed. Assumption (a) is completely redundant if the axiom system contains or implies (d) and (e). Assuming it anyway keeps us from finding out what relations the axioms imply, which Popper counts among the main points of the axiomatic method (pp. 332–333).

(d) and (e) do **not** alone imply the relative-probability forms
$$p((ab)c, d) = p(a(bc), d) \tag{g}$$
$$p(a, (bc)d) = p(a, b(cd)) \tag{h}$$
Deriving these needs much more (appendix *v, (41)–(62)) (p. 333).

Popper says he gave this example to show that Kolmogorov fails to carry out his programme, and that the same holds for all other systems known to him. In Popper's own systems all theorems of Boolean algebra can be deduced. Boolean algebra can in turn be interpreted as an algebra of sets, predicates or statements (p. 333).

*Intuition note.* Popper points out that some Boolean laws already follow from the probability rules. If you assume all of Boolean algebra at the start, you never learn how much the probability axioms already contain.

### 2. Why symmetry is needed (pp. 333–336)
- The condition If p(b) ≠ 0 in (d′) is unavoidable, since division by 0 is undefined. So in customary systems most relative-probability formulae can be asserted only in conditional form. For example, in most systems (g) is invalid and should be replaced by the much weaker
$$\text{If } p(d)\neq 0 \text{ then } p((ab)c, d) = p(a(bc), d) \tag{g$^-$}$$
with an analogous condition prefixed to (h) (pp. 333–334).
- Popper says Jeffreys and von Wright overlooked this point. Von Wright uses conditions amounting to $b \neq 0$, which do not ensure $p(b) \neq 0$, especially since his system contains an axiom of continuity. Their systems are, in Popper's judgement, inconsistent as they stand, though they can sometimes be mended (p. 334).
- Other authors saw the point, but their systems are (at least compared with Popper's) very weak. In them $p(a,b) = r$ may be meaningful while $p(b,a) = r$ is not defined, because $p(a) = 0$ (p. 334).
- Such systems are also inadequate. We may here assume (appendices *vii, *viii) that universal laws have zero probability. If universal theory s is deducible from universal theory t, we should like to assert $p(s,t) = 1$. But if $p(t) = 0$ the customary systems prevent this. Likewise $p(e,t)$, with e evidence in favour of t, may be undefined, though it is Fisher's likelihood of t on e (pp. 334–335).
- Hence Popper says a probability calculus is needed that allows second arguments of zero absolute probability; he calls it indispensable for any serious discussion of the theory of corroboration or confirmation (p. 335).
- He therefore seeks a calculus where, whenever $p(a,b) = r$ is well-formed, $p(b,a) = r$ is well-formed too, even if $p(a) = 0$. Such a system may be labelled symmetrical. He published his first one in 1955 (n. 4, p. 335).
- In every satisfactory symmetrical system rules such as these are valid: $p(a, b\bar b) = 1$; if $p(\bar b, b) \neq 0$ then $p(a,b) = 1$; if $p(a, \bar a b) \neq 0$ then $p(a,b) = 1$. They are invalid in customary systems, or (the second and third) only vacuously satisfied. Popper first believed that some of them would have to appear among his axioms, but after simplification he derived them all from formulae with a completely normal look (p. 335).
- The simplified system (six axioms) first appeared in his paper *Philosophy of Science: A Personal Report* (p. 336). Its power, he says, is due merely to omitting, from all formulae except axiom C, any condition of the form If p(b) ≠ 0 then … (p. 336). In that paper the axioms were numbered B1, B2, B3, C1, D1, E1 for B1, C, B2, A3, A2, A1 here (n. 5, p. 336).

*Intuition note.* In the usual definition p(a,b) = p(ab)/p(b), conditioning on a zero-probability b is simply undefined. Popper takes p(a, b) as primitive and lets it exist even then. This matters because he is prepared to assume that universal laws have probability zero.

### 3. The axiom system (pp. 336–342)
**Undefined notions** (p. 336): S, the universe of discourse (elements $a, b, c, \dots$); a numerical binary function $p(a,b)$, the probability of a given b; the product $ab$ (meet, conjunction); the complement $\bar a$. Absolute probability $p(a)$ may be treated as undefined or defined. It helps to remember that $p(a,a) = 1 = p(b,b)$, which is provable (p. 336).

**Postulates and axioms** (pp. 336–337):
- **Postulate 1.** S has at most denumerably many elements.
- **Postulate 2.** If a, b are in S, $p(a,b)$ is a real number, and:
  - A1 (Existence): there are c, d in S with $p(a,b) \neq p(c,d)$.
  - A2 (Substitutivity): if $p(a,c) = p(b,c)$ for every c in S, then $p(d,a) = p(d,b)$ for every d in S.
  - A3 (Reflexivity): $p(a,a) = p(b,b)$.
- **Postulate 3.** If a, b in S then $ab$ in S; for c in S:
  - B1 (Monotony): $p(ab,c) \le p(a,c)$.
  - B2 (Multiplication): $p(ab,c) = p(a,bc)\,p(b,c)$.
- **Postulate 4.** If a in S then $\bar a$ in S; and
  - C (Complementation): $p(a,b) + p(\bar a,b) = p(b,b)$, unless $p(b,b) = p(c,b)$ for every c in S.
- **Postulate AP** (definition of absolute probability): if $p(b,c) \ge p(c,b)$ for every c in S, then $p(a) = p(a,b)$. It rests on the theorem: if $p(b,c) = 1$ then $p(a,bc) = p(a,c)$ (n. 6, p. 337). Postulate AP can later be replaced by $p(a) = p(a, \overline{\bar a a})$, which uses Postulates 3 and 4 and is derived as formula 75 in appendix *v (p. 342).

The six axioms actually used in derivations are A1, A2, A3, B1, B2, C. The existential parts of the postulates can be taken for granted (p. 338). (The printed list on p. 338 ends with B3; see Reading notes.)

**Alternative systems.**
- Footnote 7 (p. 337): keep the postulates, A1, A2 and B2. Replace A3 and B1 by $p(a,a) = 1$ (A3′), $p(a,b) \ge 0$ (A4′) and the condition that if $p(ab,c) > p(a,c)$ then $p(ab,c) > p(b,c)$ (B1′). Replace C by the condition that if $p(a,b) \neq 1$ then $p(c,b) + p(\bar c,b) = 1$ (C′).
  - Popper says this system looks like some customary systems and yet yields the Boolean theorems that are ordinarily assumed separately. But he calls it unnecessarily strong: it introduces the numbers 1 and 0, which need not be mentioned, and A3, B1 and C follow immediately from A3′, A4′, C′; for the reverse, all axioms but A2 are indispensable (n. 7, p. 338; proofs in *v). In both systems the conjunction of A4′ and B1′ is replaceable by B1, and vice versa (n. 7, p. 338).
  - The derivation of B1 from A4′, B1′ (given A3 or A3′, C or C′, B2) runs: (1) $0 \le p(a,b) \le p(a,a)$; (2) $p(a,a) \ge p((aa)a,a) = p(aa,aa)\,p(a,a) = p(a,a)^2$; (3) hence $0 \le p(a,b) \le p(a,a) \le 1$; (4) $p(ba,c) \le p(a,c)$ by B2 and (3); (5) $p(ab,c) \le p(a,c)$ by (4) and B1′ (n. 7, p. 338). (Added step: swapping the roles of a and b in (4) gives $p(ab,c) \le p(b,c)$. This contradicts the consequent of B1′, so the antecedent $p(ab,c) > p(a,c)$ must fail, which gives (5).)
- **Four-axiom system** (A1, A2, B⁺, C⁺; needs a fourth variable d in Postulates 3 and 4) (p. 338). As printed in the text layer of p. 338 (no page image was available for it):
  - B⁺: if $p(a,bc)p(b,c) \neq p(d,c)$ provided that $p(a,c) \ge p(d,c)$, then $p(ab,c) \neq p(d,c)$.
  - C⁺: if $p(a,b) + p(\bar a,b) \neq p(c,c)$ then $p(c,c) = p(d,b)$.

  B⁺ is equivalent to the conjunction of B1 and B2, and C⁺ to that of A3 and C (pp. 338–339). C⁺ follows immediately from A3 and C. The converse step, deriving A3 from C⁺, runs (n. 8, p. 339):
  1. $p(c,b) + p(\bar c,b) \neq p(b,b) \to p(b,b) = p(d,b) = p(c,b) = p(\bar c,b)$ [C⁺].
  2. $p(a,a) \neq p(b,b) \to p(a,a) = p(c,b) + p(\bar c,b) \neq p(b,b) = p(c,b) = p(\bar c,b)$ [C⁺, 1].
  3. $p(a,a) \neq p(b,b) \to p(a,a) = 2p(b,b)$ [2].
  4. $p(b,b) \neq p(a,a) \to p(b,b) = 2p(a,a) = 4p(b,b) = 0 = p(a,a)$ [3].
  5. $p(a,a) = p(b,b)$ [4].
- This four-axiom system shares many advantages of the six: product and complement occur separately, all axioms except those lettered B are free of the product, and the complement occurs once only. Popper still prefers the six-axiom system. His reasons: its axioms are a little less unusual and so a little more intuitive; an extra variable is too high a price for fewer axioms; B⁺'s organicity is a mechanical trick of little value (n. 9, p. 339).

**Comments on each part** (pp. 339–342):
- *Postulate 1* can be dispensed with. A non-denumerable S satisfies all other postulates: finite sums of half-open subintervals $[x,y)$ of $[0,1)$ with real endpoints. Take $p(a)$ as length, and $p(a,b) = p(ab)/p(b)$ provided $p(b) \neq 0$, equal to 1 provided $b = 0$, or else $\lim p(ab)/p(b)$ provided the limit exists. Its function is merely to characterize elementary systems, where S is a denumerable Boolean algebra (pp. 339–340).
- *A1* is needed to establish that not all probabilities are equal. *A2* extends the probabilistic equivalence of a and b to the second argument even when a, b have zero absolute probability; without A2 this can be done only if $p(a) \neq 0 \neq p(b)$ (p. 340).
- A2 may be replaced by a stronger A2⁺: if $p(a,a) = p(b,c) = p(c,b)$ then $p(a,b) = p(a,c)$. It may also be replaced by B3: if $p(ab,c) = p(ba,c)$ then $p(c,ab) = p(c,ba)$; or by the weaker B3⁻: if $p(ab,ac) = p(ab,c)$ then $p(ba,ca) = p(ba,c)$; or by the much stronger B3⁺: $p(a,bc) = p(a,cb)$. Popper finds B3⁺ stronger than necessary and misleading, since the other axioms alone prove commutation for the first argument. He prefers A2⁺ to these formulae because, like A2, it avoids the product of a and b (p. 340).
- A three-axiom system consists of A1, C⁺ and the following axiom B, which combines B3⁺ with B⁺: if $p(ab,c) \neq p(a,d)p(b,c)$ provided that $p(a,c) \ge p(a,d)p(b,c)$ and $p(a,d) = p(a,bc)$, then $p(a,cb) \neq p(a,d)$. It is stronger than one might wish but has all the advantages of the four-axiom system (p. 340).
- *A3* is needed to prove $p(a,a) = 1$. It becomes redundant if C is strengthened by replacing both occurrences of $p(b,b)$ by $p(d,d)$, or only the second (p. 341).
- *Postulate 3* demands the existence of products and, through two axioms, characterizes all their properties (idempotence, commutation, association). *B1* is, in Popper's opinion, the most intuitively obvious axiom. He prefers it to A4′ plus B1′: A4′ may be mistaken for a convention, and B1′ concerns the product rather than a metrical aspect of probability (p. 341).
- *BD*: a long axiom that, like B, may replace A2, B1 and B2; it can be turned into a definitional form. The form printed on p. 341 is given below (footnote *1 says an improved, shorter version is on page 367, outside this unit) (p. 341):

$$\begin{aligned}p(xy,a)=p(z,a)\to{}&(Eb)(c)(d)(Ee)(Ef)(Eg)\big(p(x,a)\ge p(z,a)=p(x,b)p(y,a)\ \&\ p(a,c)\ge p(b,c)\le p(y,c)\\&\&\ (p(a,e)\ge p(c,e)\le p(y,e)\to p(c,d)\le p(b,d))\ \&\ (p(a,f)=p(y,f)\to p(x,a)=p(x,b)=p(x,y))\\&\&\ (p(x,g)\ge p(c,g)\le p(y,g)\to p(c,a)\le p(z,a))\big)\end{aligned}$$

- *Postulate 4 / axiom C.* The condition is needed because if $c = a\bar a$ (the empty element) then $p(a,c) = 1 = p(\bar a,c)$ and the obvious formula $p(a,c) + p(\bar a,c) = 1$ breaks down (pp. 341–342). C has the character of a definition (p. 342):
  - (i) $p(\bar a,b) = p(a,a) - p(a,b)$, provided there is a c with $p(c,b) \neq p(a,a)$;
  - (ii) $p(\bar a,b) = p(a,a)$, provided there is no such c.
- Popper thinks A1, BD, CD slightly preferable to A1, B, C⁺ despite BD's complexity (CD appears in an Addendum on page 367, outside this unit) (p. 342).

*Intuition note.* In plain words the axioms say: there are at least two different probability values (A1); equal probabilities can be substituted (A2); p(a,a) is the same for all a (A3); probabilities never increase when a conjunct is added (B1); they multiply in the usual way (B2); and a and its complement add up correctly unless the condition is empty (C). The other facts, such as p(a,a) = 1, are derived.

### 4. Consistency (pp. 342–345)
Popper says the system can be proved consistent, using finite models (trivial) and infinite ones, and can be proved independent; the proofs are quite easy because the axioms are weak (p. 342).

- **Two-element model.** $S = \{1, 0\}$; product and complement are arithmetical (complement with respect to 1). Define $p(0,1) = 0$ and $p(a,b) = 1$ otherwise. All axioms hold (p. 342).
- Two further finite models also satisfy (E): there are a, b, c in S with $p(a,b) = 1$ and $p(a,bc) = 0$. A similar assertion is (E′): there is a with $p(a) = p(a,\bar a) = p(\bar a,a) = 0 \neq p(a,a) = 1$. Popper says (E) is not satisfied by the two-element model and holds in no probability system known to him apart from some of his own (p. 343).
- **Four-element model.** $S = \{0,1,2,3\}$. $ab$ is the smaller of the two numbers, except $1\cdot 2 = 2\cdot 1 = 0$; $\bar a = 3 - a$. $p(a) = p(a,3) = 0$ for $a = 0,1$ and $= 1$ for $a = 2,3$. $p(a,0) = 1$. $p(a,1) = 0$ unless $a = 1$ or $3$, where it is 1. Otherwise $p(a,b) = p(ab)/p(b)$. Element 1 may be read as a universal law of zero absolute probability and 2 as its existential negation. (E) holds for $a = 2$, $b = 3$, $c = 1$ (p. 343). Tables (rows = first argument; columns = second argument for p):

| ab | 0 | 1 | 2 | 3 | $\bar a$ |   | p(a,b) | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 3 |   | 0 | 1 | 0 | 0 | 0 |
| 1 | 0 | 1 | 0 | 1 | 2 |   | 1 | 1 | 1 | 0 | 0 |
| 2 | 0 | 0 | 2 | 2 | 1 |   | 2 | 1 | 0 | 1 | 1 |
| 3 | 0 | 1 | 2 | 3 | 0 |   | 3 | 1 | 1 | 1 | 1 |

- **Generalization** (p. 344): any S forming a Boolean algebra with $2^n$ elements, where n is the number of smallest exclusive classes. Give each class a probability $0 \le r \le 1$, summing to 1; Boolean sums get arithmetic sums, complements the complement to 1. One or several of the smallest non-empty classes may get probability 0. If b is such a class, put $p(a,b) = 0$ when $ab = 0$ and $p(a,b) = 1$ otherwise; put $p(a,0) = 1$; in other cases $p(a,b) = p(ab)/p(b)$.
- **Denumerably infinite model** (pp. 344–345; connected with the frequency interpretation). S is the class of rational fractions in dyadic representation, i.e. sequences $a = a_1, a_2, \dots$ with $a_i \in \{0,1\}$. Define $(ab)_i = a_i b_i$ and $\bar a_i = 1 - a_i$. Let $A_n = \sum_n a_i$ (the printed sum sign has n beneath it; I read it as the sum of the first n terms), so $(AB)_n = \sum_n a_i b_i$. Put $q(a_n,b_n) = 1$ whenever $B_n = 0$, and $q(a_n,b_n) = (AB)_n / B_n$ whenever $B_n \neq 0$. Then
$$p(a,b) = \lim q(a_n, b_n).$$
The limit exists for all a, b in S, and all axioms are easily shown to hold (p. 345; see appendix *vi, points 8–14).

*Intuition note.* Consistency here means a model exists. Even the one-line two-element model works. The richer models matter because they contain zero-probability elements that still have well-defined conditional probabilities, which customary systems cannot handle.

### 5. Independence (pp. 345–350)
Method: for each axiom, give a model where all other axioms hold and this one fails.
- **A1:** $p(a,b) = 0$ for all a, b (p. 345).
- **A2:** $S = \{0,1,2\}$, product non-commutative: $1\cdot 2 = 2$, all other products (including $2\cdot 1$) equal the minimum. $\bar a = 1$ iff $a = 0$, else $0$. $p(0,2) = 0$ and $p(a,b) = 1$ otherwise. Then $p(1,b) = p(2,b)$ for every b, but $p(0,1) = 1 \neq 0 = p(0,2)$. The table:

| ab | 0 | 1 | 2 | $\bar a$ |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 1 |
| 1 | 0 | 1 | 2 | 0 |
| 2 | 0 | 1 | 2 | 0 |

  Popper says this proof was found at the same time by J. Agassi and himself. It satisfies AP only with a bar over the letters b; it satisfies $p(a) = p(a,\overline{\bar a a})$ (n. 10, p. 345).
- **A3:** $S = \{0,1\}$, arithmetic product and complement, $p(1,1) = 1$ and $p(a,b) = 0$ otherwise, so $p(1,1) \neq p(0,0)$ (pp. 345–346).
- **B1:** $S = \{-1,0,+1\}$; $ab$ the arithmetic product; $\bar a = -a$; $p(a,b) = a(1 - |b|)$. B1 fails for $a = -1$, $b \neq +1$, $c = 0$. This model also shows A4′ independent (p. 346). Tables:

| ab | −1 | 0 | +1 | $\bar a$ |   | p(a,b) | −1 | 0 | +1 |
|---|---|---|---|---|---|---|---|---|---|
| −1 | +1 | 0 | −1 | +1 |   | −1 | 0 | −1 | 0 |
| 0 | 0 | 0 | 0 | 0 |   | 0 | 0 | 0 | 0 |
| +1 | −1 | 0 | +1 | −1 |   | +1 | 0 | +1 | 0 |

  A second, non-commutative example (rows 0: 0 1 0, $\bar{0} = 2$; 1: 0 1 1, $\bar 1 = 0$; 2: 0 1 2, $\bar 2 = 0$; $p(0,2) = 0$, all others 1) shows independence of B1 and B1′. B1 fails for $a = 0$, $b = 1$, $c = 2$ (p. 346).
- **B2:** same S as for A3, $p(0,1) = 0$ and $p(a,b) = 2$ otherwise. B2 fails because $2 = p(1\cdot 1, 1) \neq p(1, 1\cdot 1)\,p(1,1) = 4$ (p. 346). Alternatively, use the second B1 example but change $1\cdot 0$ from 0 to 1 and $0\cdot 1$ from 1 to 0. B2 then fails for $a = 1$, $b = 0$, $c = 2$ (pp. 346–347). Popper notes B2 is needed to prove the dual of B1, $p(ba,c) \le p(a,c)$ (p. 347).
- **C:** same S, $\bar a = a$, $p(0,1) = 0$ and $p(a,b) = 1$ otherwise. C fails because $p(\bar 0, 1) \neq p(1,1)$ (p. 347).
- **Non-operational parts** (pp. 347–348):
  - *Postulate 1:* shown earlier (non-denumerable S).
  - *Postulate 2* (values are real numbers): take S as a non-numerical Boolean algebra, e.g. of statements, with $\bar x$, $xy$, $x + y$, $x \le y$ read arithmetically for numbers and Booleanly for Boolean elements (for statements, $x \le y$ means x entails y). Interpret $p(a,b)$ as $a + \bar b$ in the Boolean sense. Postulate 2 fails while the other axioms and postulates become Boolean theorems (a variant makes them propositional tautologies) (n. 11, p. 347).
  - *Postulates 3 and 4* (existence of product and complement): define on $S' = \{0,1,2,3\}$ the product and complement of the four-element table above, with $p(a) = 0,0,1,1$ for $a = 0,1,2,3$. Define $p(a,b) = 0$ whenever $p(a) \neq 1 = p(b)$, else 1. $S'$ satisfies all axioms and postulates. Restrict S to $\{1,2\}$: the product of 1 and 2 is not in S, so Postulate 3 fails. Restrict S to $\{0,1\}$: Postulate 4 fails. Popper adds that $\{2,3\}$, or any three of the four elements except $\{1,2,3\}$, can be used for Postulate 4 (p. 348).
  - *Postulate AP:* use the first consistency model with $p(a) = $ a constant (0, 1/2, 1 or 2) (p. 348).
- Popper's conclusion: every single assertion of the system is independent. To his knowledge no independence proofs for probability axiom systems were published before; he supposes the reason is that the known systems, provided they are otherwise satisfactory, are not independent (p. 348).

**Autonomous independence** (pp. 349–350). Popper says the redundancy of the usual systems is due to their postulating, implicitly or explicitly, some or all of the rules of Boolean algebra for the elements of S. In his system these rules are all derivable (proved at the end of *v) if Boolean equivalence is defined by
$$a = b \iff p(a,c) = p(b,c) \text{ for every } c \text{ in } S. \tag{*}$$
If one postulates that $ab$ is a Boolean product, $\bar a$ a Boolean complement, and (*), none of the axioms except B1′ (which belongs to the alternative system of n. 7) becomes redundant. Only if one also allowed Boolean-equivalent elements to be substituted in the *second* argument would A2 become redundant, since A2 serves that very purpose. Independence (except that of A2 and B1′) can be proved with examples satisfying Boolean algebra. A new one for B1 (and A4′) and C uses elements $\{-1,0,1,2\}$ with $\bar a = 1 - a$ and the product table below (p. 349):

| ab | −1 | 0 | 1 | 2 | $\bar a$ |
|---|---|---|---|---|---|
| −1 | −1 | 0 | −1 | 0 | 2 |
| 0 | 0 | 0 | 0 | 0 | 1 |
| 1 | −1 | 0 | 1 | 2 | 0 |
| 2 | 0 | 0 | 2 | 2 | −1 |

For B1 (and A4′): $p(a) = a$, $p(a,0) = 1$, otherwise $p(a,b) = p(ab)/p(b) = ab/b$. For C: $p(a,b) = 0$ if $ab = 0 \neq b$, else 1. B1 is violated since $2 = p(1\cdot 2, 1) > p(1,1) = 1$. C is violated since $p(\bar 2,1) + p(2,1) = 2$ though $p(0,1) \neq p(1,1)$ (p. 350). Popper calls the property that the system stays independent even if Boolean algebra and (*) are postulated autonomous independence; it seems to him an interesting (and desirable) property. It is lost if B1 is replaced by A4′ and B1′ (p. 350).

*Intuition note.* The Boolean laws need not be postulated separately: they are derivable once equal means having the same probability given every c. And the axioms stay non-redundant even if you postulate Boolean algebra and (*) (the stated exceptions being B1′, and A2 if an extra second-argument substitution postulate were added).

### 6. Borel fields of probabilities (pp. 350–355)
Popper defines an *admissible system* and a *Borel field of probabilities* in his autonomous terms. He uses Kolmogorov's term in a slightly wider sense (p. 350).

**Definitions** (pp. 350–351):
- $a \ge b$ (a is a *super-element* of b, b a *sub-element* of a) iff $p(a,x) \ge p(b,x)$ for every x in S.
- A *decreasing* (non-increasing) sequence has $a_n \ge a_{n+1}$ for each consecutive pair.
- The (Boolean) *product element* $a = \pi a_n$ of a sequence $A = a_1, a_2, \dots$ of elements of S (elements may recur) is the widest sub-element of every $a_n$. Formally, a satisfies:
  - (i) $p(a_n,x) \ge p(a,x)$ for all $a_n$ in A and every x in S;
  - (ii) $p(a,x) \ge p(b,x)$ for all x in S and every b in S such that $p(a_n,y) \ge p(b,y)$ for all $a_n$ and every y in S.
- To contrast this with the set-theoretic product, Popper confines the discussion to systems S satisfying postulates 2 to 5 whose elements are sets, with $xy$ their set-theoretic product (p. 351).

**Example S₁ (the example of the missing half-interval)** (p. 351). S₁ consists of half-open subintervals of $u = (0,1]$: the decreasing sequence $A$ with $a_n = (0, \tfrac12 + 2^{-n}]$, plus set-theoretic products of any two of its elements and complements of any one. It contains neither $h = (0,\tfrac12]$ nor any non-empty subinterval of h. h is the set-theoretic product of A, so S₁ lacks that product. But S₁ has a Boolean product element of A: the empty interval satisfies (i) trivially, and being the widest interval satisfying (i), satisfies (ii). Adding $b_1 = (0,\tfrac18]$ or $b_2 = (0,\tfrac3{16}]$ etc. makes the largest of them the product element, though none is the set-theoretic product (p. 351).

**Example S₂** (p. 352). S₂ adds to S₁ the sequence $B = b_1, b_2, \dots$ with $b_n = (0, (2^n - 1)/2^{n+2}]$ (plus products and complements). Each $b_n$ satisfies (i) for A but none satisfies (ii): there is no widest element satisfying (i). So S₂ has neither a set-theoretic nor a Boolean product of A. S₁, and any system obtained by adding finitely many new intervals, has a Boolean product element but not a set-theoretic one, unless h itself is added (p. 352).

**Definitions of the systems** (pp. 352–353). The emptiness of a may be characterized by $p(\bar a, a) \neq 0$.
- (i) A system S satisfying Postulates 2–4 is *admissible* iff it satisfies the postulates and: if $bA = a_1 b, a_2 b, \dots$ is a decreasing sequence (A is then said to be decreasing relative to b) and its product element $ab$ is in S, then
$$\lim p(a_n, b) = p(a, b).$$
  A footnote says Popper might have added the condition that $p(\overline{ab}, ab) \neq 0$, so that $ab$ is empty, which would be closer to Kolmogorov, but it is not necessary (n. 12, p. 352). He says Rényi's 1955 paper encouraged him and showed how fertile a relativized system can be. His own relative systems since 1955 are more general still: Rényi's, like Kolmogorov's, is set-theoretical and non-symmetrical (n. 12, p. 352).
- (ii) An admissible S is a *Borel field of probabilities* iff S contains a product element of any (absolutely or relatively) decreasing sequence of elements of S (p. 353).

(i) corresponds precisely to Kolmogorov's axiom of continuity; (ii) plays a role analogous to his definition of Borel fields. Popper states it can be shown that any Borel field in Kolmogorov's sense is also one in his sense, with probability a countably additive measure on the sets (p. 353).

**Non-redundancy** (pp. 353–354). Finite systems are always admissible and Borel; the definitions matter only for infinite S. Take $p(x) = l(x)$, the length of x. In S₁, (i) is violated: $\lim p(a_n) = \tfrac12$ but the product element has $p(a) = 0$. (ii) is violated by S₂ (which vacuously satisfies (i)) (p. 353).

This does not show Kolmogorov's axiom independent, because it holds in S₁: with $a = h$, $\lim p(a_n) = p(a)$ (p. 353). Popper notes that Kolmogorov claims independence for his axiom but gives no proof (p. 354). Popper's proof: take S₃, like S₁ but based on $C = c_1, c_2, \dots$ with $c_n = (0, 2^{-n}]$. Define $p(c_n) = l(c_n) + \tfrac12 = p(a_n)$. This is counter-intuitive: both $(0,\tfrac12]$ and $(0,1]$ get probability one, hence $(\tfrac12, 1]$ gets zero. It violates Kolmogorov's axiom because $\lim p(c_n) = \tfrac12$ though $p(c) = 0$ (p. 354). Consistency follows from the one-one correspondence between S₁ and S₃, since $p(a_n)$ and $p(c_n)$ coincide, so S₁'s consistency proves S₃'s. Popper says any such independence example must be equally counter-intuitive and so must essentially rest on a Boolean rather than a set-theoretic product (p. 354).

**Wider than Kolmogorov's** (p. 355). Let S₄ be like S₁ with h missing but containing the open interval $g = (0,\tfrac12)$ with $p(g) = \tfrac12$ (the text layer of p. 355 shows (a, for (0,; see Reading notes). Define $\bar g = u - g = (\tfrac12, 1]$ and $u - (g + \bar g) = u\bar u$ (not the point ½). S₄ is a Borel field in Popper's sense with g as product element of A. It is not one in Kolmogorov's sense, since it lacks the set-theoretic product of A. So Popper's definition is wider and allows interpretation by a system of sets that is not a Borel system of sets (p. 355).

**Functions of (i) and (ii)** (p. 355). (i) excludes systems such as S₁ and ensures measure-theoretical adequacy: the limit of the measures equals the measure of the limit. (ii) excludes systems such as S₂, with increasing sequences without limits, and ensures every decreasing sequence has a product in S and every increasing sequence a sum.

*Intuition note.* In S₁ the shrinking intervals have a Boolean product (the empty interval) but their probabilities do not shrink to its probability. The two conditions say that limits must exist inside S and that probability must respect them.

## Toy example (ours, not from the text)
Take the Boolean algebra of events of a coin whose outcomes are x and y: $S = \{\emptyset, X, Y, U\}$, with X = {x}, Y = {y}, U = both. Give absolute probabilities $p(\emptyset) = 0$, $p(X) = 1$, $p(Y) = 0$, $p(U) = 1$. This is the generalization recipe of p. 344 with Y a zero-probability smallest class.
- Ordinary rule: $p(a,U) = p(a)/p(U)$, so $p(Y,U) = 0/1 = 0$.
- Popper's rule for b = Y: $p(a,Y) = 0$ if $aY = \emptyset$, else 1. So $p(\emptyset,Y) = 0$, $p(X,Y) = 0$ (since $XY = \emptyset$), $p(Y,Y) = 1$, $p(U,Y) = 1$. The ratio rule would divide by $p(Y) = 0$ here.
- Both $p(Y,U) = 0$ and $p(U,Y) = 1$ are defined (symmetry).
- Check B2, $p(ab,c) = p(a,bc)\,p(b,c)$, with $a = U$, $b = Y$, $c = U$: left $p(UY,U) = p(Y,U) = 0$; right $p(U,YU)\,p(Y,U) = p(U,Y)\cdot 0 = 0$. ✓.
- Check B2 with $a = X$, $b = U$, $c = Y$: left $p(XU,Y) = p(X,Y) = 0$; right $p(X,UY)\,p(U,Y) = p(X,Y)\cdot 1 = 0$. ✓.
- Check C with $a = X$, $b = Y$: $p(X,Y) + p(\bar X,Y) = 0 + p(Y,Y) = 1 = p(Y,Y)$. ✓ (the exempting condition fails since $p(\emptyset,Y) = 0 \neq 1$).
- Check $p(a) = p(a, \overline{\bar a a})$ for $a = Y$: $\bar Y = X$, $XY = \emptyset$, complement of $\emptyset$ is U, so $p(Y) = p(Y,U) = 0$. ✓.

## Concepts
- [[formal-autonomous-symmetrical-probability]] (new) — probability calculus with no fixed interpretation, deriving probabilities only from probabilities, with p(a,b) defined whenever p(b,a) is (p. 330).
- [[relative-probability-primitive]] (new) — p(a,b) taken as basic, absolute probability defined from it (Postulate AP or $p(a) = p(a,\overline{\bar a a})$), so zero-probability conditions are allowed (pp. 336–337, 342).
- [[boolean-laws-from-probability-axioms]] (new) — the Boolean laws follow from the probability axioms once equivalence is defined by (*) (pp. 332–333, 349).
- [[axiom-independence-by-countermodel]] (new) — an axiom is shown independent by a model where the others hold and it fails (pp. 345–348).
- [[autonomous-independence]] (new) — axioms stay non-redundant even when Boolean algebra and (*) are postulated, with the exceptions Popper names (pp. 349–350).
- [[boolean-product-element]] (new) — the widest element of S that is a sub-element of every member of a sequence; it may differ from the set-theoretic product (pp. 350–351).
- [[borel-field-of-probabilities]] (new) — an admissible system containing a product element of every decreasing sequence; wider than Kolmogorov's notion (pp. 352–355).
- [[kolmogorov-continuity-axiom]] (new) — for decreasing sequences with product a, $\lim p(a_n) = p(a)$; Popper's condition (i) corresponds to it (p. 353).
- [[corroboration]] — Popper says the theory of corroboration needs second arguments of zero absolute probability (p. 335); the unit does not define corroboration.

## Canonical instances
- [[four-element-probability-model]] (new) — model with a zero-probability universal-law element 1 and its existential negation 2; satisfies (E) (p. 343).
- [[dyadic-sequence-model]] (new) — denumerable model with $p(a,b) = \lim q(a_n,b_n)$, where $q = (AB)_n/B_n$ when $B_n \neq 0$; connected to the frequency interpretation (pp. 344–345).
- [[missing-half-interval-example]] (new) — S₁, S₂, S₃, S₄ separate the Boolean and set-theoretic product and show the roles of (i) and (ii) (pp. 351–355).
- [[universal-laws-zero-probability]] (new) — if s follows from universal t with $p(t) = 0$, customary systems cannot assert $p(s,t) = 1$ (p. 334).

## Bridges (candidates)
- [same-math] Popper's $p(e,t)$ with $p(t) = 0$ ↔ statistics: Fisher's likelihood of t on e (p. 335). Popper identifies it with Fisher's likelihood; the point is that it stays defined.
- [structural-analogy] conditional probability as a primitive for zero-probability conditions ↔ measure theory: relativized systems such as Rényi's, which Popper mentions in n. 12 (p. 352).
- [structural-analogy] independence proof by countermodel ↔ mathematical logic: showing an axiom unprovable by a model where the rest hold.
- [structural-analogy] Popper's insistence on a formal, uninterpreted system ↔ formalism in geometry (Hilbert), which Kolmogorov invokes (p. 330).
- [metaphor] the autonomy principle ↔ philosophy of science: a closed rule that probabilities are only transformed into other probabilities (p. 330).

## Questions this raises
- Does allowing $p(a,b)$ when $p(b) = 0$ avoid every contradiction that conditioning on null events causes in measure-theoretic probability, or does it only trade one problem for another?
- Why does Popper hold that universal laws may be assumed to have probability zero (appendices *vii, *viii), and does the success of this formal system depend on that assumption?
- How does the symmetrical system compare with Rényi's relativized system, which Popper says is less general than his (n. 12, p. 352)?
- What is gained by the autonomous-independence requirement, other than elegance?

## Reading notes
- Printed page = pdf page − 29 (pdf 358 = p. 329 … pdf 384 = p. 355).
- Page images were supplied only for some pages (pdf 361–364, 366, 368–383). Pdf 358–360, 365, 367 and 384 (pp. 329–331, 336, 338, 355) were read from the text layer only.
- B⁺ and C⁺ (p. 338) are transcribed from the text layer, since p. 338 has no image. The same ≠ pattern appears in footnote 8 (p. 339) and in axiom B (p. 340), both of which have images. The footnote 7 derivation on p. 338 is likewise from the text layer.
- Likely misprints as printed: (i) the text layer of p. 338 lists the six axioms as A1, A2, A3, B1, B2 and B3; the system on p. 337 has C, not B3. (ii) p. 349 says examples were given for all except B1 and C1; C1 presumably means axiom C. (iii) The text layer of p. 355 shows (a, ½] and g = (a, ½) where (0, ½] and (0, ½) are expected. There is no image of p. 355, so this may be an OCR error; the images of pp. 351–353 show (0, ½]. I wrote 0.
- p. 331 spells indempotence (text layer); p. 344 diadic (image). On p.
- The text refers to appendices *ii, *iii, *v, *vi, *vii, *viii, *ix and to page 367 (BD, CD, A2 addendum), none of which is in this unit.
- No exercises in this unit.
