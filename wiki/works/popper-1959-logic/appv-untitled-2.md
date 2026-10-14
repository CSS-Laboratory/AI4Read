---
id: popper-1959-logic/appv-untitled-2
work: popper-1959-logic
unit: "Appendix *v — Derivations in the Formal Theory of Probability"
pages: 356-368
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Derivations in the Formal Theory of Probability

## L0 — One line
From a small set of axioms for a two-place probability $p(a,b)$, Popper derives the bounds, the Boolean laws and the usual formula $p(a,b)=p(ab)/p(b)$ (when $p(b)\neq 0$), and so argues that, in its logical interpretation, his calculus is a genuine generalization of the logic of derivation.

## L1 — The gist (≤ 120 words)
Appendix *iv gave postulates for a probability calculus written in terms of $p(a,b)$, the relative probability of $a$ given $b$. This appendix asks what follows from them. Popper derives the bounds 0 and 1 and shows they are reached. He then derives idempotence, commutation, association, complementation, addition and distribution. Next he defines absolute probability and recovers the usual ratio formula when $p(b)\neq0$. Finally he shows the elements form a Boolean algebra, so, in its logical interpretation, the system generalizes the logic of derivation. He argues that the usual systems cannot claim this, because they do not entail Boolean algebra. Later pages give modal-logic remarks and a 1964 addendum.

**Prerequisites:** basic propositional logic ("if–then", "for all", "there is"); idea of a probability between 0 and 1; reading formal proofs line by line with cited justifications.

## L2 — Key ideas (5–10 bullets)
- Notation: $\bar a$ is the complement of $a$; $ab$ is the product; $\overline{\bar a\bar b}$ means the Boolean sum $a+b$. The proofs explicitly cite A1–A3, B1, B2, C and Postulate 2; the other postulates are used implicitly, and Postulate AP is cited on p. 361 (pp. 356–357, 361).
- From the axioms alone Popper proves $0\le p(a,b)\le 1$ and $p(a,a)=1$. He also proves some $p(\bar a,a)=0$, so both bounds are reached (p. 357–358).
- Idempotence, commutation and association are derived for the first argument. For commutation and association, extending to the second argument needs A2 (pp. 358–360); a second-argument form of idempotence is given in footnote 1 (pp. 360–361).
- Complementation holds in an unconditional form, $p(a,b)+p(\bar a,b)=1+p(\bar b,b)$. It yields a workable definition of absolute probability $p(a)=p(a,\overline{b\bar b})$, the general addition law and a distribution law (pp. 360–362).
- For $p(b)\ne0$, $p(a,b)=p(ab)/p(b)$. The system therefore generalizes the usual calculus, and the generalization is genuine (p. 363).
- The system is a Boolean algebra, via Huntington's axioms. So in its logical interpretation the calculus generalizes the logic of derivation (pp. 364–365).
- Popper claims that the usual systems, where $p(a,b)$ is undefined unless $p(b)\neq0$, are formally inadequate as generalizations of logic (p. 366).
- Terms used above, in their first-argument forms: idempotence is $p(aa,b)=p(a,b)$ (p. 358); commutation is $p(ab,c)=p(ba,c)$ (p. 358); association is $p((ab)c,d)=p(a(bc),d)$ (p. 359); complementation (axiom C and its generalization) links $p(a,b)$ and $p(\bar a,b)$ (p. 360); absolute probability $p(a)$ is a one-place probability defined from $p(a,\cdot)$ (p. 361); a Boolean algebra is a system with sum, product and complement that satisfies Huntington's axioms (p. 365); "logic of derivation" is the logic of what follows from what, here read off from $ab=b$ (p. 365).

## L3 — Walkthrough

### Aims and notation (p. 356)
Popper derives the laws of upper and lower bounds, idempotence, commutation, association and distribution. He also derives a simpler definition of absolute probability and indicates how Boolean algebra arises. Notation: $\to$ "if…then", $\leftrightarrow$ "if and only if", $\&$ "and", $(Ea)$ "there is an $a$ in $S$", $(a)$ "for all $a$ in $S$" (p. 356).

### Axioms cited (pp. 356–357)
Postulate 2: if $a,b\in S$, then $p(a,b)$ is a real number. Other postulates are used implicitly.
- A1: $(Ec)(Ed)\,p(a,b)\ne p(c,d)$
- A2: $((c)(p(a,c)=p(b,c)))\to p(d,a)=p(d,b)$
- A3: $p(a,a)=p(b,b)$
- B1: $p(ab,c)\le p(a,c)$
- B2: $p(ab,c)=p(a,bc)\,p(b,c)$
- C: $p(a,a)\ne p(b,a)\to p(a,a)=p(c,a)+p(\bar c,a)$

### Bounds (pp. 357–358)
Let $k=p(a,a)=p(b,b)$ (1, from A3).
- (2) $p((aa)a,a)\le p(aa,a)\le p(a,a)=k$ (B1).
- (3) $p((aa)a,a)=p(aa,aa)\,p(a,a)=k^2$ (B2).
- (4)–(5) So $k^2\le k$, hence $0\le k\le1$.
- (6)–(7) $k\ne p(a,b)\to k=k+p(\bar b,b)$ (C), so $p(\bar b,b)=0$.
- (8) $p(a\bar b,b)=p(a,\bar bb)\,p(\bar b,b)$ (B2).
- (9)–(10) $k\ne p(a,b)\to 0=p(a\bar b,b)\le p(a,b)$ (7, 8, B1), so $0\le p(a,b)$ in that case.
- (11)–(14) $0>p(a,b)\to k=p(a,b)$, and $k=p(a,b)\to0\le p(a,b)$ by (5). So always $0\le p(a,b)$.
- (15)–(17) $0\le p(\bar a,b)$. Then $k\ne p(a,b)\to k\ge p(a,b)$ (C, 15). With (5): $p(a,b)\le k\le1$.
- (18) $0\le p(a,b)\le k\le1$.
- (19)–(22) $k=p(aa,aa)\le p(a,aa)\le k$, and likewise for $a(aa)$. By B2, $k=p(a,a(aa))\,p(a,aa)=k^2$. So $k=k^2$.
- (23)–(25) $(Ea)(Eb)\,p(a,b)\ne0\to k=1$. A1 gives the antecedent. So $p(a,a)=k=1$.
- (26)–(27) $(Eb)(Ea)\,p(b,a)\ne k$ (A1, 1). So $(Ea)\,p(\bar a,a)=0$ (7, 26).

(14), (17), (18) give the bounds 0 and 1. (25) and (27) show they are actually reached (p. 358).

*Intuition note.* Nothing assumes probabilities lie in $[0,1]$; this follows from the axioms. $k=k^2$ forces $k=1$ once some probability is not 0.

*Skip path:* carry forward $0\le p(a,b)\le1$ (18), $p(a,a)=1$ (25), $p(\bar a,a)=0$ for some $a$ (27).

### Idempotence, commutation, association (pp. 358–360)
- Idempotence: (28) $1=p(ab,ab)\le p(a,ab)=1$ (25, B1, 17). (29) $p(aa,b)=p(a,ab)\,p(a,b)$ (B2). So (30) $p(aa,b)=p(a,b)$ (p. 358).
- Second monotony law: (31) $p(a,bc)\le1$; (32) $p(ab,c)\le p(b,c)$ (B2, 31, 14).
- Commutation (first argument), using only 25, B1, (32), B2:
  - (33) $p(a(bc),a(bc))=1$; (34) $p(bc,a(bc))=1$; (35) $p(b,a(bc))=1$.
  - (36) $p(ba,bc)=p(a,bc)$; (37) $p((ba)b,c)=p(ab,c)$.
  - (38) $p(ba,c)\ge p(ab,c)$ (B1). (39) by substitution the reverse inequality. (40) $p(ab,c)=p(ba,c)$.
  - Extending to the second argument would need A2 (p. 358).
- Association:
  - (41)–(42) $p(ab,d((ab)c))=1$, so $p(a,d((ab)c))=1=p(b,d((ab)c))$.
  - (43)–(48) $p(a(bc),(ab)c)=p(bc,(ab)c)=p(b,c((ab)c))\,p(c,(ab)c)=1$. This is a preliminary form. Popper says (62) also follows by A2$^+$ and B2, but he avoids A2 where possible (p. 359).
  - (49)–(51) By (40) and B2: $p(a(b(cd)),d)=p(cd,b(ad))\,p(b,ad)\,p(a,d)$ and $p(a(bc),d)=p(c,b(ad))\,p(b,ad)\,p(a,d)$. By B1, $p(a(bc),d)\ge p(a(b(cd)),d)$.
  - (52)–(57) $p(a(b(cd)),(ab)(cd))=1$ gives $p(a(b(cd)),cd)\ge p(ab,cd)$. Then $p(a(b(cd)),d)\ge p((ab)c,d)$. With (51): (57) $p(a(bc),d)\ge p((ab)c,d)$, one half.
  - (58)–(61) Using (57) and (40) with substitutions: (61) $p((ab)c,d)\ge p(a(bc),d)$.
  - (62) $p((ab)c,d)=p(a(bc),d)$. The second-argument law follows by A2. Applying B2 twice to each side of (62) only leads to a conditional form with antecedent $p(bc,d)\ne0$ (p. 360).

*Intuition note.* The order of "and" does not matter for the first argument. Popper's derivation cites no A2; it rests mainly on $p(a,a)=1$, the two monotony laws and B2, with several steps of the form $p(x,y)=1$ (pp. 358–359).

### Complementation and absolute probability (pp. 360–361)
- (63) $p(\bar b,b)\ne0\leftrightarrow(c)\,p(c,b)=1$ (7, 25).
- (64) $p(a,b)+p(\bar a,b)=1+p(\bar b,b)$ (C, 25, 63). This is an unconditional form of C.
- (65)–(68) Since $a$ is absent on the right of (64), substitute: (65) $p(a,b)+p(\bar a,b)=p(c,b)+p(\bar c,b)$. Then (66) with $bd$ in place of $b$. Multiplying by $p(b,d)$ (B2): (67) $p(ab,d)+p(\bar ab,d)=p(cb,d)+p(\bar cb,d)$. Then (68) the same with $c$ in place of $d$.
- (69) $p(\bar cb,c)=p(\bar c,c)$. (70) $p(ab,c)+p(\bar ab,c)=p(b,c)+p(\bar c,c)$. Footnote 1 supplies the needed (29′): $p(cb,c)=p(b,c)$.
- Footnote 1 also gives (28′)–(35′). Examples: $p(a,a\bar a)=1$ (31′); $p(\bar a,a\bar a)=1$ (32′); $p(a,\bar bb)=1$ (33′); $(Eb)(a)\,p(a,b)=1$ (34′). Popper says (31′)–(35′) do not belong to the usual systems (p. 361).
- (71)–(74) $p(aa,b)+p(\bar aa,b)=p(a,b)+p(\bar b,b)$. So $p(\bar aa,b)=p(a\bar a,b)=p(\bar b,b)$. Applying (64) to the complement of $\bar aa$ gives $p(\overline{\bar aa},b)=1=p(\overline{a\bar a},b)$.
- Hence the elements $\overline{a\bar a}$ satisfy the condition of Postulate AP. (75) $p(a)=p(a,\overline{a\bar a})=p(a,\overline{\bar aa})=p(a,\overline{b\bar b})=p(a,\overline{\bar bb})$. Popper calls this a more workable definition of absolute probability (p. 361).

### Addition and distribution (pp. 361–363)
- (76) $p(a\bar b,c)=p(a,c)-p(ab,c)+p(\bar c,c)$ (70, 40).
- (77) $p(\bar a\bar b,c)=p(\bar a,c)-p(\bar ab,c)+p(\bar c,c)$.
- (78) $p(\bar a\bar b,c)=1-p(a,c)-p(b,c)+p(ab,c)+p(\bar c,c)$ (77, 76, 64, 40).
- (79) $p(\overline{\bar a\bar b},c)=p(a,c)+p(b,c)-p(ab,c)$ (78, 64). This is the general addition law, since $\overline{\bar a\bar b}$ is $a+b$ in Boolean sense. It is unconditional and free of the unusual "$+p(\bar c,c)$" (pp. 361–362).
- (80)–(81) Generalizations: $p(\overline{\bar b\bar c},ad)=p(b,ad)+p(c,ad)-p(bc,ad)$, and $p(a\overline{\bar b\bar c},d)=p(ab,d)+p(ac,d)-p(a(bc),d)$.
- Distribution lemma: (82)–(83) rewrite $p(a(bc),d)$ using B2, (30) and (62). (84) $p(a(bc),d)=p((ab)(ac),d)$ (p. 362).
- (85) By (79): $p(\overline{\overline{ab}\,\overline{ac}},d)=p(ab,d)+p(ac,d)-p((ab)(ac),d)$.
- (86) By 81, 85, 84: $p(a\overline{\bar b\bar c},d)=p(\overline{\overline{ab}\,\overline{ac}},d)$. This is the first law of distribution.
- (87)–(88) $p(\overline{b\bar b}\,a,c)=p(\overline{b\bar b},ac)\,p(a,c)=p(a,c)$. Hence $p(\overline{\overline{ab}\,\overline{a\bar b}},c)=p(a,c)$.
- (89)–(90) $p(\bar{\bar a}b,c)=p(ab,c)$. Also $p(a,c)=p(b,c)\to p(\bar a,c)=p(\bar b,c)$ (64) (pp. 362–363).
- (91)–(94) give association, commutation and idempotence for the Boolean sum: $p(\overline{\bar a\bar b},c)=p(\overline{\bar b\bar a},c)$ and $p(\overline{\bar a\bar a},b)=p(a,b)$ (p. 363). The two-line associativity formulas (91)–(92) are written in the source with nested overlines; read them as "$(a+b)+c$ equals $a+(b+c)$ under $p(\cdot,d)$"; Popper calls this the law of association for the Boolean sum (p. 363).

### Link with the usual calculus (p. 363)
- (95) $p(a,b)=p(a,b\overline{c\bar c})$ (87, 40, A2).
- (96) $p(a,b)\,p(b)=p(ab)$ (95, B2, 75).
- (97) $p(b)\ne0\to p(a,b)=p(ab)/p(b)$.

So the relative probability coincides with the usual one for $p(b)\ne0$. The calculus is a genuine generalization, as shown by the consistency examples of appendix *iv with formula (E): $(Ea)(Eb)(Ec)\,p(a,b)=1\ \&\ p(a,bc)=0$. This formula is invalid in many finite interpretations but valid in the normal infinite ones (p. 363).

*Intuition note.* The ratio formula is a special case. Popper's system also gives values of $p(a,b)$ when $p(b)=0$.

### $S$ is a Boolean algebra (pp. 364–365)
- (98) $((x)\,p(a,x)=p(b,x))\to p(ay,z)=p(by,z)$ (B2). (99) $\ldots\to p(y,az)=p(y,bz)$ (98, A2).
- (99) needs A2. It does not follow from 98, 40, B2, because possibly $p(a,z)=p(b,z)=0$ (e.g. if $\bar a=z\ne x\bar x$).
- (100) $((x)(p(a,x)=p(b,x)\ \&\ p(c,x)=p(d,x)))\to p(ac,y)=p(bd,y)$ (99, B2).
- With (90), (100), A2: if (*) $p(a,x)=p(b,x)$ for every $x$ in $S$, then $a$ and $b$ are substitutionally equivalent (any name of $a$ may replace $b$ in any well-formed formula without changing truth value).
- (D1) $a=b\leftrightarrow(x)\,p(a,x)=p(b,x)$. Hence (A) $a=a$; (B) $a=b\to b=a$; (C) $(a=b\ \&\ b=c)\to a=c$; (D) replaceability (A2, 90, 100).
- (D2) $a=b+c\leftrightarrow a=\overline{\bar b\bar c}$.
- (i) $a,b\in S\to a+b\in S$ (Postulate 3, D2, D1, 90, 100). (ii) $a\in S\to\bar a\in S$ (Postulate 4). (iii) $a+b=b+a$ (93). (iv) $(a+b)+c=a+(b+c)$ (92). (v) $a+a=a$ (94). (vi) $ab+a\bar b=a$ (88). (vii) $(Ea)(Eb)\,a\ne b$ (27, 74, 90, D1).
- (A)–(D2) with (i)–(vi) is Huntington's axiom system ("fourth set"). All valid Boolean formulae are derivable from it. So $S$ is a Boolean algebra (p. 365). Footnote 2: (v) is redundant, as Huntington showed; (vii) is also assumed by him.
- Conclusion: in its logical interpretation, the probability calculus is a genuine generalization of the logic of derivation (p. 365).

### Logic and the usual systems (pp. 365–367)
- $a\ge b$ is definable by $ab=b$; in the logical interpretation it is read "$a$ follows from $b$" (or "$b$ entails $a$"). Then (+) $a\ge b\to p(a,b)=1$ (said to be easily proved).
- **Popper's criticism:** (+) is asserted by many authors, but is invalid in the usual systems if they are consistent. Footnote 3: Jeffreys asserts it, without a condition like $p(b)\ne0$, which Popper says makes his Theorem 4 contradictory. Popper says Jeffreys's second edition is still inconsistent (p. 365).
- Making (+) valid requires allowing $p(a,a\bar a)+p(\bar a,a\bar a)=2$, although $p(a+\bar a,a\bar a)=1$. So $p(a+\bar a,b)=p(a,b)+p(\bar a,b)$ must not be asserted unconditionally (p. 366).
- The converse $p(a,b)=1\to a\ge b$ must not be demonstrable; the second and third consistency examples show this.
- Valid in this system: ($\ddagger$) $a\ge b\leftrightarrow p(a,\bar ab)\ne0$, and $a\ge b\leftrightarrow p(a,\bar ab)=1$. None can hold in the usual systems, where $p(a,b)$ is undefined unless $p(b)\ne0$.
- So Popper concludes the usual systems are wrongly described as generalizations of logic: they do not even entail Boolean algebra (p. 366).
- The system can be read as a many-valued propositional logic (discrete, dense or continuous) or as modal logic. Examples: "$a$ necessarily implies $b$" as $p(b,a\bar b)\ne0$; "$a$ is logically necessary" as $p(a,\bar a)=1$ (p. 366).
- Necessary necessity: write $\vdash x$ for "$x$ is necessary (or demonstrable)" and $h$ for $p(a,\bar a)=1$. Roughly, $\vdash a\leftrightarrow\vdash h$ and $\vdash a\to\vdash{}$"$p(h,\bar h)=1$". This gives secondary probability statements about primary ones. Other interpretations are possible, some putting them at different linguistic levels (p. 367; cf. appendix *ix, Third Note, *13).

### Addendum, 1964 (pp. 367–368)
- Popper reports a system of three axioms, A, BD, CD, equivalent to the six axioms:
  - A: $(Ea)(Eb)\,p(a,a)\ne p(a,b)$
  - BD: $((d)\,p(ab,d)=p(c,d))\leftrightarrow(e)(f)\big(p(a,b)\leqq p(c,b)\ \&\ p(a,e)\geqq p(c,e)\leqq p(b,c)\ \&\ ((p(b,e)\leqq p(f,e)\ \&\ p(b,f)\geqq p(f,f)\leqq p(e,f))\to p(a,f)p(b,e)=p(c,e))\big)$
  - CD: $p(\bar a,b)=p(b,b)-p(a,b)\leftrightarrow(Ec)\,p(b,b)\ne p(c,b)$
- He also found an example violating A2 but satisfying the other axioms and Postulate AP. A modification of the example on p. 348 gives a Boolean algebra proving the independence of C. He lists further references (p. 368).

## Toy example (ours, not from the text)
Let $S$ be all subsets of $\{1,2,3,4\}$ with equal weight. Define $p(a,b)=|a\cap b|/|b|$ for non-empty $b$, and $p(a,\varnothing)=1$. Complement is relative to $\{1,2,3,4\}$. Take $a=\{1,2\}$, $b=\{2,3\}$, $c=\{1,2,3\}$.
- Ratio formula (97): $p(a,c)=2/3$ and $p(b,c)=2/3$. Also $ab=\{2\}$, so $p(ab,c)=1/3$.
- Addition (79): $a+b=\{1,2,3\}$, so $p(a+b,c)=3/3=1$. The right side is $2/3+2/3-1/3=3/3=1$ ✓.
- Complementation (64) with $b=\varnothing$ (so $p(b)=0$): $p(a,\varnothing)+p(\bar a,\varnothing)=1+1=2$. The right side is $1+p(\bar\varnothing,\varnothing)=1+p(\{1,2,3,4\},\varnothing)=1+1=2$ ✓. The "$+p(\bar b,b)$" term is exactly what keeps the formula true here.

## Concepts
- [[relative-probability-primitive]] (new) — $p(a,b)$, the probability of $a$ given $b$, is basic; it can be defined even when $b$ has probability 0 (pp. 356, 363).
- [[absolute-probability-definition]] (new) — $p(a)=p(a,\overline{b\bar b})$, given Postulate AP (p. 361).
- [[boolean-algebra-derivability]] (new) — the elements of $S$ satisfy Huntington's axioms, so $S$ is a Boolean algebra (p. 365).
- [[substitutional-equivalence]] (new) — $a=b$ iff $p(a,x)=p(b,x)$ for all $x$; then $a$ may replace $b$ in any formula (p. 364).
- [[logic-of-derivation-generalization]] (new) — in its logical interpretation the probability calculus is a genuine generalization of the logic of derivation; with $a\ge b$ read "$a$ follows from $b$", one has $a\ge b\to p(a,b)=1$ (p. 365).
- [[usual-systems-inadequate-for-logic]] (new) — Popper's claim that systems with $p(a,b)$ undefined for $p(b)=0$ do not entail Boolean algebra (p. 366).

## Canonical instances
- [[jeffreys-theory-of-probability]] (new) — footnote 3: Popper's objection that Jeffreys's convention, stated without $p(b)\ne0$, makes his Theorem 4 contradictory; Popper also calls the system, even in the second edition, still inconsistent (p. 365).
- [[formula-E-finite-vs-infinite]] (new) — (E) is invalid in many finite interpretations but valid in the normal infinite ones (p. 363).

## Bridges (candidates)
- [same-math] $p(a,b)=p(ab)/p(b)$ for $p(b)\ne0$ (97) ↔ standard conditional probability — the same ratio formula.
- [structural-analogy] Substitutional equivalence (D1) ↔ analytic-philosophy: Leibniz-style identity of indiscernibles — equality means interchangeability in all contexts.
- [structural-analogy] Interpreting $p(a,\bar a)=1$ as logical necessity ↔ modal logic — probability one given the negation as a necessity operator.

## Questions this raises
- Which axioms are really independent? The 1964 addendum gives only some independence results.
- Does the finite/infinite split for (E) matter for applications, or only for foundations?
- How does one interpret $p(a,b)$ when $p(b)=0$ outside pure logic?
- Can primary and secondary probability statements always be kept at one linguistic level?

## Reading notes
- Printed pages 356–368; PDF pages 385–397 (printed = pdf − 29).
- Text-layer symbols are garbled (e.g. "⭐" for ≤, ⭓ for ≥). I checked the page images and used ≤, ≥ as shown.
- The overlines in (73)–(75), (87), (91)–(92) are fragile in the text layer. I checked them against the images; (91)–(92) are summarized in words, not transcribed.
- Postulate AP and A2$^+$ are cited but not stated in this unit; I did not restate them.
- BD (p. 367) uses unusual inequality glyphs ($\leqq$, $\geqq$); I reproduced them as I read them in the image, so check against the printed page.
- In the addendum (p. 368) the image shows "$p(2)=12$", presumably a lost fraction; I cannot verify the intended value.
- The text states (+) as "easily proved" and gives no proof here.
