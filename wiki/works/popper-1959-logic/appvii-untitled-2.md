---
id: popper-1959-logic/appvii-untitled-2
work: popper-1959-logic
unit: "Appendix *vii — Zero Probability and the Fine-Structure of Probability and of Content"
pages: 374-391
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
# Zero Probability and the Fine-Structure of Probability and of Content

## L0 — One line
Popper argues that, in an infinite universe, every non-tautological universal law (one that says something, not true by logic alone) has probability zero, so probability cannot measure how well a theory is supported or how much it says, and he proposes a finer ordering of zero-probability theories by content.

## L1 — The gist (≤ 120 words)
Popper asks whether universal laws can have a positive probability, either absolute or given finite evidence. He answers no, at least for an infinite universe: p(a) = 0 and p(a, b) = 0. He gives several arguments, from classical probability, from independence, from Laplace's distribution, from Hume's problem of induction, and from Jeffreys's own formula. He rejects the objection that this makes learning from experience impossible, because corroboration can still grow. But since all laws then have p = 0, differences in content are invisible to p and to the content measure C = 1 − p. He therefore introduces a "fine structure": an ordering of content and probability that separates cases where the measures coincide at 0.

**Prerequisites:** the basic rules of probability (product rule, conditional probability), limits of sequences, and the meaning of "universal law" as "for all x, x has A".

## L2 — Key ideas (5–10 bullets)
- Corroboration (how well a theory has survived severe tests) is not probability: a logically stronger, more testable theory is always less probable, so higher corroboration usually goes with lower probability (p. 374).
- Thesis: in an infinite universe, p(a) = 0 and p(a, b) = 0 for any non-tautological universal law a and finite evidence b; the two formulas are equivalent (p. 375).
- Main argument: a universal law can be read as an infinite product of singular statements. If these are independent and all have the same probability below 1, the product has probability 0 (p. 377–380). Popper holds that setting p(a) = 1 is unacceptable, since contradictory laws would then both get probability 1 (p. 378).
- For absolute logical probability, independence of the singular statements seems to Popper the only reasonable assumption; dependence would be an ad hoc, non-logical (synthetic) hypothesis (p. 379). A dependence principle (+), saying that unobserved cases are likely to resemble observed ones, would be a synthetic a priori principle of induction (a non-logical principle assumed without experience), and Popper holds that Hume's criticism fully applies to it (p. 381–382).
- Popper argues that Jeffreys's formula (10) supports p(a, b) = 0, not Jeffreys's case (3). A law and a rival law can fit the same data but predict opposite next results (p. 383–384).
- Popper replies that the objection that p(a) = 0 makes learning impossible fails, because the degree of corroboration can rise even when p(a) = 0 (p. 380).
- Zero probability hides differences in content: a1 ("circles") entails a2 ("ellipses"), yet p and the content measure C = 1 − p treat them alike (p. 386–387).
- Fine structure: Popper introduces order signs ≻ ("higher") and ≺ ("lower"), with a suggested rule based on large finite universes, to express such differences (p. 388–389). The same structure also affects probabilities strictly between 0 and 1 (p. 390).

## L3 — Walkthrough

### Setting (p. 374–375)
**Corroboration vs probability.** Popper restates the book's thesis. A "well corroborated" hypothesis is only one that is severely tested (so highly testable) and has survived the severest tests so far. Degree of corroboration cannot satisfy the probability calculus. The calculus makes the logically stronger, more informative and better testable of two hypotheses always the less probable, on any evidence (p. 374). So high corroboration generally goes with low probability. Hence probability must be distinguished from corroboration, and "inductive probability" is untenable (p. 374).

**Earlier results.** In an infinite universe the probability of any non-tautological universal law is zero (p. 375). Popper adds in parentheses that scientists must choose between high probability and high informative content, and so far have always chosen content, provided the theory passed its tests (p. 375).

**The two formulas.** "Probability" means absolute logical probability or probability relative to finite evidence $b$ (a singular statement or finite conjunction of them). Popper asserts, for a law $a$:
$$p(a)=0 \tag{1}$$
$$p(a,b)=0 \tag{2}$$
They are equivalent (p. 375).
- (1) ⇒ (2): $p(a)=0$ entails $p(ab)=0$. Assuming $p(b)\neq 0$ for finite evidence, $p(a,b)=p(ab)/p(b)=0$ (Jeffreys and Keynes).
- (2) ⇒ (1): if (2) holds for any $b$, however weak, assume it holds for zero evidence, the tautology $t=\overline{b\bar b}$. Then $p(a)=p(a,t)=0$ (p. 375).

### Arguments for (1) and (2)

**A. The classical definition (p. 376–378).** Probability is the number of favourable possibilities divided by the number of all (equal) possibilities.
- Deriving (2): if the favourable possibilities are the favourable evidence, that evidence is finite while the possibilities in an infinite universe are infinite, so $p(a,b)=0$. Any sufficiently large universe gives the same result approximately (p. 376).
- Deriving (1): write the law as $a=$ everything has property $A$, i.e. $(x)Ax$. It is an infinite product $a=a_1a_2a_3\ldots$ with $a_i=Ak_i$, $k_i$ naming the $i$-th individual. Footnote 1 says that laws like the swan law and laws of more complex form can be put in this shape by choosing $A$ suitably; if natural laws are logically stronger than assumed, the considerations hold a fortiori (p. 376). Let $a^n=a_1\cdots a_n$. Then
$$a=\lim_{n\to\infty}a^n,\qquad p(a)=\lim_{n\to\infty}p(a^n) \tag{3}$$
- $a^n$ says that all $n$ individuals have $A$. One possibility out of $2^n$ is favourable (each individual has $A$ or non-$A$), so
$$p(a^n)=1/2^n \tag{4$^c$}$$
and (3) with (4$^c$) gives (1) (p. 377).
- Popper admits the weakness: $A$ and non-$A$ need not be equally probable, since the $a_i$ are instantiation statements and more probable than their negations (potential falsifiers). But for any probability of $A$ short of unity, the infinite product has probability zero (assuming independence). This is a particularly trivial case of the one-or-zero law of probability, also called the all-or-nothing principle (p. 377). If $a$ is an infinite product of independent $a_i$ with $p(a_i)=p(a_j)$:
$$p(a)=\lim_{n\to\infty}p(a^n)=0,\ \text{unless } p(a)=p(a^n)=1 \tag{4}$$
- $p(a)=1$ is unacceptable. Popper says that his inductivist opponents, too, cannot accept that experience can never raise a law's probability. Also the laws that all swans are black and that all swans are white would both get probability 1 (likewise for every colour). Then statements that a black swan exists, and the like, would get zero. This would assert the emptiness of the universe with probability 1. So (4) establishes (1) (p. 378).

*Intuition note.* Multiplying infinitely many equal numbers below 1 drives the product to 0, and a law asserts infinitely many instances. The only escape is probability 1 for each instance, which would make contradictory laws equally certain.

**B. Weaker arguments without independence (p. 378–379).**
- *Laplace's distribution.* Take as fundamental possibilities the proportions in which $A$ occurs in a sample of $n$: $0,1/n,\ldots,n/n$, treated as equiprobable. Then
$$p(a^n)=1/(n+1),\quad \lim p(a^n)=0 \tag{5}$$
Only the proportion $n/n$ is favourable (added step: there are $n+1$ equiprobable proportions). This does not identify the observed cases as favourable or assume the number of observed cases is finite (p. 379). Footnote 2: this assumption suits mere sampling, but seems inadequate for a succession of individual events (p. 378).
- *Entailed statistical hypothesis.* Every universal law $a$ entails a statistical hypothesis $h$ of the form $p(x,y)=1$, so $p(a)\le p(h)$. By Laplace's distribution $p(h)=0$, hence $p(a)=0$. Popper finds this proof simplest and most convincing: (4) applies to $a$ and (5) to $h$ (p. 379).

**C. The logical interpretation: independence (p. 379–380).** With only tautological information, the only reasonable assumption seems to be that the $a_i$ are mutually independent: $p(a_j,a_i)=p(a_j)$ and $p(\bar a_j,a_i)=p(\bar a_j)=1-p(a_j)$ (p. 379). Any other assumption would postulate an ad hoc after-effect, a synthetic hypothesis that cannot belong to a purely logical theory (p. 379). Given a hypothesis $h$ stating an after-effect we may have
$$p(a_j,a_ih)>p(a_j,h) \tag{6}$$
$$p(a_ia_j,h)>p(a_i,h)\,p(a_j,h) \tag{7}$$
(7) is equivalent to (6). For absolute logical probabilities, or tautological $h$:
$$p(a_ia_j)=p(a_i)\,p(a_j) \tag{8}$$
$$p(a_j,a_i)=p(a_j) \tag{9}$$
(8) and (9) are equivalent. Independence with $p(a_i)<1$ gives $p(a)=0$ (p. 380).

**D. The "transcendental" objection (p. 380).** *Objection (some authors):* (8) must be false, otherwise we could not learn from experience. *Popper replies:* this is incorrect. We may learn even though $p(a)=p(a,b)=0$, because the degree of corroboration $C(a,b)$ may increase with new tests (cf. appendix *ix). Footnote 3 explains that a "transcendental argument" infers from the fact that we have knowledge that every theory excluding it is false. Popper allows such arguments critically, but says we must not assume uncritically that we have probable knowledge in the sense of the calculus. He holds that empirical knowledge consists of guesses, many of which are not probable (or have probability zero) though well corroborated (p. 380, n. 3).

### Against the dependence principle (+) (p. 381–384)
**The principle.** The opposing view says $p(a_ia_j)>p(a_i)p(a_j)$, hence
$$p(a_n,a_1a_2\ldots a_{n-1})>p(a_n) \tag{$+$}$$
Hume's terminology: unexperienced instances are likely to resemble experienced ones (p. 381).

**Hume's criticism.** Hume's criticism applies fully to (+). Appealing to experience to justify conclusions about unobserved cases leads to an infinite regress, even for merely probable conclusions (Hume, *Abstract*, p. 382). So (+) cannot be justified by experience. To be logically valid it would have to be a tautology, valid in every logically possible universe, and it is not. Thus (+), if true, would be a synthetic a priori principle of induction (p. 382).

**(+) is not enough.** (+) may be true while $p(a)=0$; Carnap's theory accepts both (n. 7, p. 382). An effective probabilistic principle of induction would need at least $p(a,b)>1/2$ for some $b$, which is possible only if $p(a)>0$, i.e. (1) false (p. 382–383).

**Jeffreys's formula.** Jeffreys's formula, in Popper's symbols: provided $p(b_i,a)=1$ for every $i\le n$, so that $p(ab^n)=p(a)$,
$$p(a,b^n)=\frac{p(a)}{p(b^n)}=\frac{p(a)}{p(b_1)\,p(b_2,b^1)\cdots p(b_n,b^{n-1})} \tag{10}$$
Jeffreys's three possibilities after enough verifications: (1) the probability of $a$ exceeds 1 (impossible, trivially); (2) it is always 0; (3) $p(b_n,b^{n-1})$ tends to 1 (p. 383).

**Popper's refutation of case (3) as a general rule.** (10) needs only $0<p(b_i)<1$ and the existence of some $a$ with $p(b^n,a)=1$. For reports $b_i$ on penny tosses, such an $a$ can always be constructed: a universal law entailing the $n-1$ observed tosses and predicting the rest. A rival law $a'$ gives the same first $n-1$ results but the opposite $n$-th result (p. 383–384). Case (3) would then give both $p(b_n,b^{n-1})$ and $p(\bar b_n,b^{n-1})$ close to 1, which is paradoxical. So Jeffreys's mathematically inescapable argument proves his case (2), i.e. formula (2). Jeffreys himself draws the opposite conclusion (n. 10, p. 384). Footnote 9 shows how to define a predicate $B$ so that each $b_i$ has the form $B(k_i)$ (p. 383).

**"Belief in magic."** Some believe that, for purely logical reasons, the probability that the next thing is red grows with the number of red things seen. Popper calls this belief a belief in magic, the magic of human language (p. 384). For any observations there are predicates $A$ and $B$, both true of all observed things, with incompatible probabilistic predictions for the next thing. Such predicates can always be constructed, even if they do not occur in ordinary languages. Popper notes the belief is found among builders of artificial languages rather than analysts of ordinary language (p. 384). This criticism defends independence, (4) and (1) (p. 384).

*Intuition note.* Popper argues that, for purely logical reasons, past observations do not in general make one prediction more likely than a rival one, because rival laws fit the same data. Any rule that said otherwise would have to be assumed, not derived from logic.

### The Jeffreys–Wrinch argument (p. 384–386)
Let $e$ be a set of singular data to be explained by a universal law. There are infinitely many mutually exclusive explanations, whose probabilities (given $e$) sum to at most 1. So almost all must have probability zero, unless the laws can be ordered in a sequence with positive, convergent probabilities, earlier ones more probable. This requires a **consistency condition**: the ordering must never place a law before another when it can be proved that the latter is more probable (p. 384–385). Jeffreys and Wrinch proposed ordering by simplicity, or by number of adjustable parameters. Popper says it will be shown in appendix *viii that this ordering, or any other, violates the condition (p. 385). So $p(a,e)=0$ for all explanatory hypotheses, giving (2) and indirectly (1) (p. 385).

**Finite-universe example.** The argument holds even in a finite universe if hypotheses are expressed in a mathematical language allowing infinitely many hypotheses. Discs are placed on a large chessboard only on squares lying on a mathematical curve unknown to us. There are infinitely many incompatible curves, some indistinguishable on the discs placed so far. Any of them may be refuted by later discs (p. 385). Popper notes that this example is not part of his main argument. Against the instrumentalist reply that differences between theories fixing the same squares are "meaningless", he says a finer mesh can often give them meaning (p. 386).

### Content and the failure of $p$ and $C$ (p. 386–388)
Take $a_1=$ all planets move in circles and $a_2=$ all planets move in ellipses. Since circles are ellipses, $a_1$ entails $a_2$ but not conversely, so $a_1$ has much greater content (p. 386). Some tests of $a_1$ are not tests of $a_2$, but every genuine test of $a_2$ also tests $a_1$. So $a_1$ is more testable and can reach a higher corroboration (p. 386). Similar relations hold if $a_1$ entails only something that $a_2$ approximates well (Newton's dynamics vs Kepler's laws) (p. 386–387).

Since $p(a_1)=p(a_2)=0$, probability cannot express this. With the book's content measure $C(a)=1-p(a)$ we get $C(a_1)=C(a_2)$. Likewise $p(a\bar a)=p(a)=0$ and $C(a\bar a)=C(a)=1$ for a self-contradictory statement $a\bar a$ (p. 387).

Footnotes on pp. 387–388 add the following.
- **Hempel (n. 13).** Popper says Hempel's adequacy condition (8.3) cannot cover corroborating evidence: it requires that if $e$ confirms $h_1$ and $h_2$, then $h_1$, $h_2$ and $e$ are consistent. Yet Newton's and Einstein's theories are incompatible, and the known evidence for Newton's theory also corroborates Einstein's. Likewise failed searches for a red or yellow swan corroborate both the white-swan law and the black-swan law, which contradict each other given that at least one swan exists.
- **Infinite universes (n. 14).** In any probability theory applied to an infinite universe a self-contradictory statement can have the same probability as a consistent synthetic one. Examples are the probability of $n$ successive heads, $1/2^n$, which becomes 0 for infinitely many throws, and the probability of drawing a prime-numbered ball, which tends to 0 as $n\to\infty$. Popper rejects criticisms of the frequency theory (Kneale) and of Jeffreys for this.

### The fine structure (p. 388–390)
**Using conditional probability.** In some cases the difference can be expressed: $a_1$ entails $a_2$ but not vice versa, so
$$p(a_1,a_2)=0,\quad p(a_2,a_1)=1 \quad\text{although}\quad p(a_1)=p(a_2)=0,$$
hence $p(a_1,a_2)<p(a_2,a_1)$, indicating greater content of $a_1$ (p. 388).

**The fine structure.** Popper calls the differences that $C$ and $p$ are too coarse to show a "fine structure" of content and probability. He expresses it with order signs. I write $\succ$ ("is higher"), $\prec$ ("is lower"), $\succcurlyeq$, $\preccurlyeq$ (higher-or-equal, lower-or-equal). The glyphs are partly lost in the text layer and were read from the image. Rules (p. 389):
1. $C(a)\succ C(b)$, equivalently $p(b)\prec p(a)$, says the content of $a$ is greater than that of $b$ at least in the fine-structure sense. It entails $C(a)\succcurlyeq C(b)$, which entails $C(a)\ge C(b)$ (the falsity of $C(a)<C(b)$). None of the opposite entailments hold.
2. $C(a)\succcurlyeq C(b)$ and $C(a)\preccurlyeq C(b)$ together entail $C(a)=C(b)$. But $C(a)=C(b)$ is compatible with $\succ$, $\prec$, $\succcurlyeq$ and $\preccurlyeq$.
3. $C(a)>C(b)$ always entails $C(a)\succ C(b)$.
4. Corresponding rules hold for $p$.

**Criterion for when $C(a)\succ C(b)$ though $C(a)=C(b)$.** Unilateral entailment of $b$ by $a$ is a clear case. More generally Popper "suggests" a rule: if $C(a)>C(b)$ in all sufficiently large finite universes (all with more than $N$ members, for some $N$), then keep $C(a)\succ C(b)$ in an infinite universe even if there $C(a)=C(b)$. He says the rule seems to cover most cases of interest, perhaps not all (p. 389). It covers $a_1$ vs $a_2$, and $a_1$ vs $a_3=$ the law that all planets move in ellipses with eccentricity other than zero, since $p(a_3)>p(a_1)$ in all large finite universes of possible observations: more possibilities are compatible with $a_3$ (p. 389). Footnote 15 mentions Kemeny's related paper.

**Probabilities between 0 and 1.** Let $p(a_2)=0$, $p(a_1)\prec p(a_2)$, $b$ entailed neither by $a_1$, $a_2$ nor their negations, and $0<p(b)=r<1$. Then
$$p(a_1\vee b)=p(a_2\vee b)=r,\qquad p(a_1\vee b)\prec p(a_2\vee b)$$
$$p(\bar a_1b)=p(\bar a_2b)=r,\qquad p(\bar a_1b)\succ p(\bar a_2b)$$
the latter because $p(\bar a_1)\succ p(\bar a_2)$ although $p(\bar a_1)=p(\bar a_2)=1$. So for every $b$ with $p(b)=r$ there is a $c_1$ with $p(c_1)=p(b)$ and $p(c_1)\prec p(b)$, and a $c_2$ with $p(c_2)=p(b)$ and $p(c_2)\succ p(b)$ (p. 390). This matters for the simplicity or dimension of a theory, to be treated in the next appendix (p. 390).

*Intuition note.* When a measure gives "0" to both $a_1$ and $a_2$, we can still rank them by looking at finite cases, where (in the cases the rule covers) the stronger law is less probable in every large finite universe. The ranking survives in the limit as a finer order, not as a number.

### Addendum, 1972 (p. 390–391)
Popper says that the fine structure matters for comparing simplicity and dimension of theories, and conversely that simplicity and especially dimension matter for the theory of fine structure (see the next appendix). The dimension of a theory is relative to a field of application and to a set of problems for which it offers a solution; the same relativization is relevant to fine structure and thus to the "goodness" of theories (p. 390–391).

## Toy example (ours, not from the text)
Each individual independently has one of three colours (red, blue, green), each with probability 1/3. Let $a_1$ = "all $n$ individuals are red" and $a_2$ = "all $n$ are red or blue". Then $p(a_1^n)=(1/3)^n$ and $p(a_2^n)=(2/3)^n$.
- $n=2$: $1/9$ vs $4/9$.
- $n=5$: $1/243$ vs $32/243$.
- $n=10$: $1/59049$ vs $1024/59049$ (since $3^{10}=59049$, $2^{10}=1024$).

Both tend to 0 as $n\to\infty$, so $p(a_1)=p(a_2)=0$ and $C(a_1)=C(a_2)=1$. But $p(a_1^n)<p(a_2^n)$ for every finite $n$. By Popper's rule this gives $p(a_1)\prec p(a_2)$: the more specific law is "lower" in the fine structure. Also $a_1$ entails $a_2$, so $p(a_1,a_2)=0$ and $p(a_2,a_1)=1$ in the limit.

## Concepts
- [[corroboration]] — degree to which a theory has survived severe tests; Popper says it is not a probability (p. 374)
- [[falsifiability]] — testability (the text does not use the word falsifiability): a logically stronger, more informative theory is better testable and can be better corroborated (p. 374, 386)
- [[bayesian-confirmation]] — nearest spine id: the probabilistic theory of induction (inductive probability), which Popper calls untenable (p. 374); he holds that $p(a,b)=0$ for universal laws on any finite evidence $b$ (p. 375, 380). The text does not use the word Bayesian
- [[zero-probability-of-universal-laws]] (new) — thesis $p(a)=p(a,b)=0$ for every non-tautological universal law (p. 375)
- [[all-or-nothing-principle]] (new) — an infinite product of independent, equiprobable statements has probability 0, unless that probability is 1 (p. 377–378)
- [[laplace-distribution]] (new) — treating possible sample proportions of $A$ as equiprobable; gives $p(a^n)=1/(n+1)$ (p. 378)
- [[independence-of-singular-statements]] (new) — Popper's view that, with only tautological information, the $a_i$ should be taken as independent; he calls dependence a synthetic, ad hoc after-effect (p. 379–380)
- [[transcendental-argument]] (new) — an argument from the fact that we have knowledge to the falsity of any theory that excludes it; Popper allows it only critically (p. 380, n. 3)
- [[synthetic-a-priori-induction-principle]] (new) — what principle (+) would have to be to be valid; Hume's criticism applies (p. 382)
- [[fine-structure-of-content]] (new) — finer order $\succ$ on content and probability that separates cases where $C$ and $p$ are equal at 0 or 1 (p. 388–389)
- [[underdetermination]] — rival laws fit the same finite data yet predict differently (penny tosses, discs on the chessboard) (p. 383–385)

## Canonical instances
- [[swan-laws]] — the laws that all swans are white and that all swans are black: $p=1$ for both is unacceptable, Popper says; failed searches for red or yellow swans corroborate both (p. 378, 387)
- [[penny-toss-rival-laws]] — laws $a$, $a'$ fit the first $n-1$ tosses and predict opposite $n$-th tosses; Popper takes this to refute Jeffreys's case (3) as a general rule (p. 383–384)
- [[chessboard-curve-universe]] — finite universe with infinitely many incompatible curves as hypotheses (p. 385)
- [[circles-vs-ellipses]] — $a_1$ entails $a_2$; shows content difference invisible to $p$ and $C$ (p. 386–389)
- [[newton-kepler-einstein]] — evidence for Newton also corroborates Einstein, though they conflict; Newton's theory has more content than Kepler's laws (p. 386–387)
- [[prime-numbered-balls]] — probability of drawing a prime tends to 0 as $n\to\infty$ in any adequate probability theory (p. 388, n. 14)

## Bridges (candidates)
- [same-math] infinite product of independent, equal probabilities $q<1$ tends to 0 ↔ analysis: $q^n\to 0$; the core of (4) is exactly this limit.
- [structural-analogy] Laplace's equiprobable proportions, $p(a^n)=1/(n+1)$ ↔ Bayesian statistics: a uniform prior over the unknown proportion; the unit gives only the "equiprobable proportions" step, not the analogy.
- [structural-analogy] fine structure within probability 0 ↔ measure theory/lexicographic probability: probability-zero events may differ in size, and a finer order separates them.
- [structural-analogy] Popper's penny-toss rival laws and constructed predicates ↔ underdetermination and "gruesome"-type predicates: any finite data fit incompatible generalizations.
- [metaphor] belief in magic (the magic of human language) ↔ philosophy of language: formal languages are said to carry inductive power by their form alone (p. 384).

## Questions this raises
- If $p(a)=0$ for all laws, in what sense is corroboration $C(a,b)$ computed, and how does it differ from the content measure $C(a)$? (The unit points to appendix *ix.)
- Does the finite-universe rule for $\succ$ give a unique answer when two theories' finite probabilities cross over at different universe sizes?
- Is independence of the $a_i$ truly a purely logical default, or does it already encode an assumption about the world?
- Can the Jeffreys–Wrinch consistency condition really fail for every ordering of laws? (Promised in appendix *viii.)

## Reading notes
- Printed page = pdf page − 29 (pdf 403 = printed 374).
- Running heads: "appendix *vii" and "new appendices". The extract ends on p. 391 with the last lines of the addendum of 1972; the addendum points to the next appendix on p. 390.
- The text layer loses many glyphs: $\succ$, $\prec$, $\succcurlyeq$, $\preccurlyeq$ (pp. 388–390) and subscripts/superscripts in (10). I read them from the images. On p. 390 the text layer prints $p(\bar a_1b)=p(\bar a_2b)$ for the second at-the-same-time clause. The glyph is hard to make out; I give $\succ$ because it follows from $p(\bar a_1)\succ p(\bar a_2)$ in the next line.
- In $t=\overline{b\bar b}$ (p. 375) the overline covers both letters in the image.
- Misprint on p. 383: "three exists" for "there exists". Footnote 14 (p. 388) writes "Jeffrey's" for Jeffreys.
- Rule (1) on p. 389 is printed with $p(b)\prec p(a)$ as the equivalent of $C(a)\succ C(b)$; since $C=1-p$ (p. 387) and p. 390 uses $p(a_1)\prec p(a_2)$ for the stronger $a_1$, one would expect $p(a)\prec p(b)$. I give the printed form. Rule (2) on p. 389 is printed as I give it; I did not reinterpret it. The distinction between $\succcurlyeq$ and plain $\ge$ rests on glyphs I could only read approximately.
- Many cross-references (appendices *viii, *ix, *x, Postscript) point to material outside these pages and are not digested here.
