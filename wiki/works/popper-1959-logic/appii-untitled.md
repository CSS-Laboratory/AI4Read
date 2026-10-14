---
id: popper-1959-logic/appii-untitled
work: popper-1959-logic
unit: "Appendix *ii — A Note on Probability, 1938"
pages: 319-324
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# A Note on Probability, 1938 (Appendix *ii)

## L0 — One line
Popper argues that probability theory should be built as an uninterpreted formal axiom system, which classical, frequency and logical readings can all satisfy, with absolute probability defined from relative probability or the reverse.

## L1 — The gist (≤ 120 words)
Popper reprints the introduction to his 1938 note on axioms for probability and adds later commentary. The question is how to axiomatise probability so that the classical, frequency and logical interpretations all fit. His answer is to treat probability as a formal two-argument functor whose arguments are uninterpreted "elements". Absolute probability is defined from relative probability, or the reverse. This matters for two reasons. Popper hoped later to show that "degree of corroboration" is not a probability. He also wanted to identify "logical probability" as the logical reading of absolute probability. He restates a simpler axiom system, devised soon after the note, and withdraws his early preference for the absolute system.

**Prerequisites:** basic probability (conjunction, negation, conditional probability as a ratio); the idea of an axiom system with undefined primitive terms.

## L2 — Key ideas (5–10 bullets)
- Popper says he believes the note was the first to state that probability theory should be a "formal" system open to many interpretations (classical, frequency, logical). (p. 319)
- One reason for a formal theory was his hope of later showing that corroboration is not a probability, since its properties were incompatible with the formal calculus. (p. 319)
- Absolute probability is relative probability with a tautological second argument: $p(x)=p(x,\overline{x\bar x})$. Popper wanted to show that his earlier "logical probability" is the logical interpretation of absolute probability. (p. 320)
- Kolmogorov's system takes the arguments as sets with members. Popper's assumes nothing about them, so Kolmogorov's is one interpretation of his. (p. 320)
- The simpler system restated here has seven axioms (A1–A4, B1–B3) on absolute probability, in product and complement. (pp. 320–321)
- Two routes exist. System s1 takes $p(x_1,x_2)$ as primitive and defines $p_a$ (Df1). System s2 takes $p_a$ as primitive and defines $p(x_1,x_2)$ as a ratio (Df2). (pp. 322–323)
- In the note Popper judged s2 superior in certain respects, chiefly because it allows a much stronger "axiom of uniqueness"; he ties this to $p(x_1,x_2)$ being indeterminate when $p_a(x_2)=0$. He now considers the relative system superior, since appendix *iv gives a system where relative probabilities are determinate even then. (p. 323)

## L3 — Walkthrough

**Popper's later introduction (pp. 319–320).** Popper calls the 1938 note badly written. It was his first English publication, and the proofs never reached him in New Zealand. (p. 319)
- *Aim 1.* He believes the note stated for the first time that probability theory should be a formal system, open to many interpretations, among them the classical, the frequency and the logical (now sometimes called "semantic") interpretation. (p. 319)
- *Aim 2.* He hoped later to show that "degree of corroboration" is not a probability: that its properties were incompatible with the formal calculus. He points to appendix *ix and Postscript §§*27–*32. (p. 319)
- *Aim 3.* He wanted to show that his earlier "logical probability" is the logical interpretation of an *absolute probability*, i.e. $p(x,y)$ with tautological $y$. Writing a tautology as $\overline{x\bar x}$ (not-(x and not-x)), he defines: (p. 320)
$$p(x)=p(x,\overline{x\bar x}),\qquad\text{or}\qquad p_a(x)=p(x,\overline{x\bar x})=p(x,\overline{y\bar y}).$$
- *Kolmogorov.* Popper did not know Kolmogorov's 1933 book when he wrote the note. Kolmogorov had very similar aims, but his system is less formal than Popper's and so open to fewer interpretations. Kolmogorov interprets the arguments as sets, so they have members. Popper assumes nothing about his "elements" except that their probabilities obey the axioms. Kolmogorov's system is therefore one interpretation of Popper's. (p. 320)
- The original axiom system was clumsy. Popper had not then managed to derive the distributive law from simpler axioms, so he stated it as an axiom; in product and complement form it is very clumsy. Popper therefore omits them and restates a simpler system on absolute probability. It is derivable from the relative system of appendix *iv. (p. 320)

**The simpler axiom system (pp. 320–321).** Here $xy$ is the product (conjunction) and $\bar y$ the complement (negation). The symbol $\geqslant$ is printed as shown. (See Reading notes.)
- A1 (Commutation): $p(xy)\geqslant p(yx)$
- A2 (Association): $p((xy)z)\geqslant p(x(yz))$
- A3 (Tautology): $p(xx)\geqslant p(x)$
- A4 (Existence): there are at least one $x$ and one $y$ with $p(x)\neq p(y)$
- B1 (Monotony): $p(x)\geqslant p(xy)$
- B2 (Complement): $p(x)=p(xy)+p(x\bar y)$
- B3 (Independence): for every $x$ there is a $y$ such that $p(y)\geqslant p(x)$ and $p(xy)=p(x)p(y)$

Footnote *1 explains B3. Without B3 the upper bound of $p(x)$ is not fixed: $p(\overline{x\bar x})=k$ for arbitrary $k$. Then $x$ is independent of $y$ iff $p(xy)=p(x)p(y)/k$. That is clumsy unless $k=1$, and B3 leads to $k=1$. If B3 says $p(y)\neq 0$ instead of $p(y)\geqslant p(x)$, then A4 becomes redundant. (p. 321)

*Intuition note.* These axioms say nothing about dice or frequencies. B3 fixes the scale at 1, so independence is simply "probability of the product = product of probabilities". (p. 321)

**The 1938 note (pp. 321–324).**
- *Probability as functor.* Probability is a two-termed functor: a numerical function of two arguments that need not themselves be numbers. The arguments are names, e.g. of predicates or of statements. If both arguments follow the same substitution rules and the same interpretation, it is written $p(x_1,x_2)$, "the probability of $x_1$ with regard to $x_2$". (p. 321)
- *System $s_1$.* Popper wants a system $s_1$ with $p(x_1,x_2)$ as undefined primitive, interpretable by any proposed reading. (p. 322) The three readings:
  1. Classical: the ratio of favourable to equally possible cases.
  2. Frequency: relative frequency of one class of occurrences within another.
  3. Logical: the degree of a logical relation between statements. It equals 1 if $x_1$ follows from $x_2$ and 0 if the negation of $x_1$ follows from $x_2$.
- *Group A axioms.* Group A introduces undefined conjunction $x_1x_2$ and negation $\bar x_1$. Then "$x_1$ and not $x_1$" is $x_1\bar x_1$, and its negation is $\overline{x_1\bar x_1}$. (p. 322)
- *Df1.* If the substitution rules are suitable, it can be proved for any $x_1,x_2,x_3$ that $p(x_1,\overline{x_2\bar x_2})=p(x_1,\overline{x_3\bar x_3})$. So the value depends only on $x_1$. This justifies (p. 322):
$$p_a(x_1)=p(x_1,\overline{x_2\bar x_2})\tag{Df$_1$}$$
A footnote adds that $p_a(x_1)=p(x_1,\overline{x_1\bar x_1})$ would have been simpler. (p. 322)
- *Logical reading.* Popper's earlier "logical probability" is an example of the logical interpretation of $p_a$. (p. 323)
- *System $s_2$ and Df2.* One can start from the other end. System $s_2$ takes $p_a$ as primitive and defines (p. 323):
$$p(x_1,x_2)=\frac{p_a(x_1x_2)}{p_a(x_2)}\tag{Df$_2$}$$
Then the axioms and Df1 of $s_1$ become theorems of $s_2$. (p. 323)
- *Why prefer $s_2$.* In 1938 Popper says $s_2$ is superior in some respects. The chief one is that $s_2$ admits a much stronger "axiom of uniqueness" than $s_1$, if $s_1$'s generality is not restricted. The reason is that $p(x_1,x_2)$ is indeterminate when $p_a(x_2)=0$. (p. 323)
- *Group B.* $s_2$ with Df2 suffices to deduce the mathematical theory of probability. Group A gives axioms for conjunction and negation, practically an adaptation of the postulates of the "Algebra of Logic". Group B gives axioms peculiar to measuring probability. Group A corresponds to five propositions of *Principia Mathematica*. The original axioms are not reprinted. (pp. 323–324)

**Later retraction (fn. *2, p. 323).** The absolute system has an advantage only while $p(x,y)$ counts as indeterminate when $p_a(y)=0$. Popper has since developed a system (appendix *iv) where relative probabilities are determinate even then. He now considers the relative system superior and calls "axiom of uniqueness" a badly chosen term. (p. 323)

*Intuition note.* Absolute probability is "probability given a statement that is always true". Df2 goes the other way and is the usual ratio definition of conditional probability. It breaks down when the conditioning event has probability 0, which is why Popper later changed his preference. (pp. 322–323)

## Toy example (ours, not from the text)
Classical reading: a fair die with outcomes 1–6. Let $p_a(S)=|S|/6$. Let $x$ = "even" = {2,4,6} and $y$ = "at most 2" = {1,2}.
- $p(x)=3/6=1/2$. $xy=\{2\}$, so $p(xy)=1/6$. B1: $1/2\geqslant 1/6$ ✓.
- $x\bar y=\{4,6\}$, so $p(x\bar y)=2/6$. B2: $1/6+2/6=3/6=p(x)$ ✓.
- B3 for $x$: take $y'$ = "at most 4" = {1,2,3,4}, so $p(y')=4/6\geqslant 1/2$. $xy'=\{2,4\}$, so $p(xy')=2/6$. And $p(x)p(y')=\tfrac12\cdot\tfrac46=\tfrac13=\tfrac26$ ✓.
- Df2: $p(x,y)=p_a(xy)/p_a(y)=(1/6)/(2/6)=1/2$.

The same axioms would hold if $p_a$ were read as a relative frequency, which is the point of a formal system.

## Concepts
- [[formal-axiomatic-probability]] (new) — probability as an uninterpreted system, open to several interpretations (p. 319)
- [[absolute-probability]] (new) — $p_a(x)=p(x,\overline{x\bar x})$; one-argument probability, with a tautology as condition (p. 320, 322)
- [[relative-probability]] (new) — $p(x_1,x_2)$, "probability of $x_1$ with regard to $x_2$"; primitive in $s_1$, defined by a ratio in $s_2$ (pp. 321, 323)
- [[corroboration]] — here only mentioned: Popper wants to show it is not a probability (p. 319)

## Canonical instances
- [[classical-interpretation]] (new) — favourable over equally possible cases (p. 322)
- [[frequency-interpretation]] (new) — relative frequency of one class within another (p. 322)
- [[logical-interpretation-of-probability]] (new) — degree of a logical relation; 1 if $x_1$ follows from $x_2$ (p. 322)
- [[kolmogorov-system]] (new) — arguments are sets; one interpretation of Popper's system (p. 320)

## Bridges (candidates)
- [same-math] $p(x_1,x_2)=p_a(x_1x_2)/p_a(x_2)$ ↔ standard probability: conditional probability as a ratio — the same formula, with Df2 as definition.
- [structural-analogy] Uninterpreted "elements" with axioms ↔ analytic-philosophy: formal system vs. interpretation (e.g. explication) — syntax is fixed and meaning supplied separately.
- [metaphor] Absolute probability as "probability given a tautology" ↔ logic: validity as truth under no assumptions — a loose parallel.

## Questions this raises
- Which properties of corroboration conflict with the calculus (appendices *ix and the Postscript)?
- How does appendix *iv make $p(x,y)$ determinate when $p_a(y)=0$?
- What does "$p_a(x_2)=0$ makes $p(x_1,x_2)$ indeterminate" cost in practice for the logical reading?
- Do the A1–A3 axioms really need equality signs? (See Reading notes.)

## Reading notes
- Printed = pdf − 29 (pdf 348 = p. 319); printed numbers are given in the labels.
- Source: Routledge Classics edition, running heads "appendix *ii" and "new appendices".
- Only the introduction of the 1938 note is reprinted. The original axiom list, which had misprints, is omitted (p. 324).
- The overlines over whole expressions ($\overline{x\bar x}$ etc.) are lost in the text layer on pp. 320 and 322. The image of p. 322 shows the overline over the whole product, and I followed that. The p. 320 image was not supplied, so there I follow the sentence "not-(x and not-x)".
- A3, B1 and B3 use the same ≥-type glyph in the image. The text layer gives the same glyph for A1 and A2 (their images were not supplied). Labels like "Commutation" and "Tautology" would normally suggest equality for A1–A3. I transcribe as printed and do not decide whether this is a typesetting artefact.
- Footnotes 1–7 give references (Carnap, Tarski, Keynes, Mazurkiewicz, Huntington, Whitehead–Russell). Other references: Levy-Roth and Popper's Logik der Forschung (fns 2–3). I use the footnotes only for the points stated in L3 (fn 5 on Df1 and fn 7 on Group A).
