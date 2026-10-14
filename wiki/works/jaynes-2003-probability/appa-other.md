---
id: jaynes-2003-probability/appa-other
work: jaynes-2003-probability
unit: Appendix A — Other approaches to probability theory
pages: 651–660
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 14
pipeline_version: 0.1
---
# Appendix A — Other approaches to probability theory

## L0 — One line
Jaynes argues that Kolmogorov's axioms, de Finetti's coherence and comparative (ordinal) probability are either special cases of, or weaker foundations than, his consistency-based extension of logic.

## L1 — The gist (≤ 120 words)
Jaynes asks how his consistency-based, extended-logic probability theory relates to rival foundations. He argues that Kolmogorov's axioms are the set-theoretic echo of results he derived from consistency, so he sees no substantive conflict. His version is more general and uses conditional probability freely. He rejects de Finetti's betting-based coherence as a foundation. He argues that comparative theories keeping transitivity and universal comparability must reduce to the numerical theory. He then speculates that lattice theories may describe real human reasoning, with Laplace–Bayes theory as the limit of an "infinitely educated" brain.

**Prerequisites:** sum and product rules; Boolean algebra (AND, OR, NOT); sets and σ-fields; Cox's consistency theorems (Ch. 2); exchangeability; partial orders.

## L2 — Key ideas
- Kolmogorov's four measure axioms (normalization, non-negativity, additivity, continuity at zero) correspond to properties Jaynes derives from consistency. Jaynes therefore says the charge of arbitrariness now seems to him unjustified (pp. 652–653).
- Jaynes does not insist on one scale: certainty need not be $p=1$, and any monotonic rescaling $u=f(p)$ is allowed. But then the sum and product rules must change form so that the content of the theory does not change (p. 652).
- Jaynes names important differences from KSP. Conditional probability and Bayes' theorem are central for him, while KSP treats them as an afterthought. He is cautious with infinite sets. He finds resolving a proposition into a conjunction often more useful than resolving it into a disjunction, though the two methods do not conflict. Like KSP, his system needs no random experiment, which he counts as a merit (pp. 653–655).
- Jaynes rejects de Finetti's coherence as a foundation for aesthetic, strategic and pragmatic reasons. Consistency is what matters, and consistent rules are automatically coherent (pp. 655–656).
- For any finite set of propositions, transitivity plus universal comparability gives a representation by real (indeed rational) numbers, after which Cox's theorems force the standard rules (pp. 656–657).
- All the alleged counterexamples to universal comparability that Jaynes has seen involve classifying by more than one attribute. By definition, his probability theory classifies propositions by one attribute only (p. 658).
- Comparative theories may serve as approximations when only a decision is needed (p. 658).
- A speculative lattice theory models partial comparability. Laplace–Bayes theory is its limit when the lattice becomes a line (pp. 659–660).

## L3 — Walkthrough

### Introduction (p. 651)
Jaynes says his Chapter 2 axioms are not the only possible ones. Intuitive qualitative statements could be taken as axioms instead. One example: if $A$ implies $B$, then $P(A|C)\le P(B|C)$ for all $C$.

His rules already give this. The product rule is
$$P(AB|C)=P(B|AC)P(A|C)=P(A|BC)P(B|C).\tag{A.1}$$
If $A$ implies $B$, then $P(B|AC)=1$ and $P(A|BC)\le 1$. (added step: $AB=A$, so $P(A|C)=P(A|BC)P(B|C)\le P(B|C)$.)

He chose axioms that seemed most primitive and hardest to quarrel with, not those giving the shortest derivations. The aim was greatest generality (p. 651).

### A.1 The Kolmogorov system (KSP)
**Definition of KSP (pp. 651–652).** Components:
- A sample space $\Omega$ of elementary propositions ("events") $\omega_i$.
- A field $F$ of subsets $f_j\subseteq\Omega$ with three properties:
  - (I) $\Omega\in F$.
  - (II) $F$ is a σ-field: $f_j\in F$ implies the complement $\bar f_j=\Omega-f_j\in F$.
  - (III) $F$ is closed under countable unions.
- A measure $P$ on $F$ with four properties:
  - (1) normalization: $P(\Omega)=1$.
  - (2) non-negativity: $P(f_i)\ge 0$.
  - (3) additivity: for disjoint $f_j$, $P(\cup_j f_j)=\sum_j P(f_j)$.
  - (4) continuity at zero: if $f_1\supseteq f_2\supseteq\dots$ tends to the empty set, then $P(f_j)\to 0$.

**Jaynes's comparison with his own system.**
- Closure under complement matches his primitive operation NOT. He also took AND as primitive. (AND, NOT) suffice for deductive logic and, he says, also for his extended logic. Given $\{A_1,\dots,A_n\}$, the rules assign consistent probabilities to all propositions of the generated Boolean algebra (p. 652).
- Closure under countable unions is implied in this sense: he works with finite unions, and a well-behaved limit to an infinite set may be a convenient simplification that removes irrelevant detail (p. 652).
- A real-world proposition cannot always be viewed as a disjunction of elementary propositions from a meaningful $\Omega$. Its denial may be hard to read as set complement. Replacing logic by set operations leaves the abstract structure intact but loses generality (p. 652).

**Arbitrariness of the axioms (pp. 652–653).**
- KSP has been criticized because its axioms look arbitrary. Jaynes says they are the set-language versions of the four properties he derived from consistency.
  - Non-negativity: see (2.35).
  - Additivity: derived as necessary for consistency in (2.85).
  - Normalization: by (2.31), if certainty is not $p=1$, the sum and product rules must be restated, or an inconsistency results. With certainty at $p=100$:
$$p(A|B)+p(\bar A|B)=100,\qquad p(A|BC)p(B|C)=100\,p(AB|C).\tag{A.2}$$
- More generally, any monotonic $u=f(p)$ is a different scale, and the rules must change form to keep the same content. For $u=\log[p/(1-p)]$ the sum rule becomes
$$u(A|B)+u(\bar A|B)=0,\tag{A.3}$$
while the product rule becomes quite complicated. (added step: $p(\bar A|B)=1-p(A|B)$, so $u(\bar A|B)=\log[(1-p)/p]=-u(A|B)$.)
- Jaynes's conclusion is not that one scale is obligatory. Rather, a theory of probability whose content differs from that of a theory with a single normalized, non-negative, additive scale will contain inconsistencies (pp. 652–653).
- **Objection (Fine, 1973):** Kolmogorov's scale was arbitrary. **Jaynes replies:** Kolmogorov made the only choices that pass all the consistency tests, so the charge now seems to him unjustified (p. 653).

*Intuition note.* Setting certainty to 1, or to 100, or using log-odds, is only a change of scale. What is fixed is the content of the sum and product rules. Jaynes claims consistency leaves no real freedom there.

**Continuity at zero (p. 653).**
- Jaynes does not know how Kolmogorov saw the need for axiom (4), but his approach derives it from consistency.
- The set statement seems to need an infinite sequence of subsets. The propositional version needs only an infinite sequence of *states of knowledge*, possibly about one proposition, tending to impossibility. Sets have no notion of "state of knowledge".
- Restricting to a finite set of propositions does not remove the need for the axiom. The theory would become arbitrary and allow inconsistencies.
- In his system: if $p(A)_n$ tend to certainty, then $p(\bar A)_n$ must tend to zero. By (2.48), the functional equation for $S(x)$ ties values together so strongly that the way $S(x)$ tends to zero as $x\to1$ determines $S$ over $0\le x\le1$, and so determines additivity (2.58). Axioms (3) and (4) therefore look closely related. Jaynes says it is not obvious whether they are logically independent.

**Agreement and differences (pp. 653–655).**
- In the set context, Jaynes's system agrees with KSP for practical purposes. In general applications he has $F$ and $P$ with the same properties but does not need, and does not always have, an elementary set $\Omega$. Where one exists, as in equilibrium statistical mechanics (stationary global quantum states, a countable set), agreement is essentially complete (p. 653).
- KSP has no statement that $P$ is a frequency in a random experiment. Jaynes counts this as a merit. Requiring a random experiment would make the theory inapplicable to most of his problems. Where frequencies matter, propositions about frequencies are elements of $F$, things inferred about, not determinations of $P$. A footnote reports de Finetti's claim that KSP cannot be interpreted as limits of frequencies (p. 653).
- **Conditional probability.** KSP centres on additive measure and treats conditional probability as an awkward afterthought. A footnote cites a whole book (Rao, 1993) that gives it a separate axiomatics (p. 654).
  - Jaynes holds that all real-world probabilities are conditional on information. In his Chapter 2 the product rule, with Bayes' theorem, comes before additivity.
  - The product rule expresses the associativity and commutativity of Boolean algebra. This gives unrestricted use of Bayes' theorem: propositions can be moved across the bar freely (p. 654).
- **Infinite sets.** In return, Jaynes accepts an inhibition. He starts from a finite set of propositions, and $F$ is the finite closure under conjunction, disjunction and negation. He resolves into finer propositions or takes infinite limits only when a problem's structure makes it useful (p. 654). Three reasons:
  1. Sam's broken thermometer (Ch. 8): beyond some point, finer resolution serves no purpose.
  2. Paradoxes of jumping into infinite sets (Ch. 15). On the Borel–Kolmogorov paradox he agrees with Kolmogorov's resolution. Infinite sets must be approached carefully, and once in an uncountable set, sets of measure zero just as carefully.
  3. Resolving $A$ into a *conjunction* $A=C_1C_2\cdots$ and using the product rule is often more useful than a disjunction $A=B_1+B_2+\cdots$ with the sum rule.
     - Analogy: specify a country by its points (Venn–Kolmogorov) or by its boundary. The boundary of $A$ is built from segments of the boundaries of the $C_i$.
     - The methods are not in conflict. Method (2) is natural for most of his problems, since physical and mathematical theories are stated as conjunctions of hypotheses or axioms (pp. 654–655).
- **Summary.** Jaynes sees no substantive conflict with Kolmogorov "as far as it goes". He claims a deeper conceptual foundation that extends to wider applications (p. 655).
- **Incompleteness.**
  - In its present state of development the robot does not know how to translate an item like "Jones was very pleased at the suggestion that $\theta$ might be greater than 100" into a statement about $p(\theta)$.
  - Human brains have more principles for converting raw information, semiquantitatively, into something usable. Jaynes is therefore convinced that more principles like maximum entropy and transformation groups remain to be discovered (p. 655).

### A.2 The de Finetti system (pp. 655–656)
- De Finetti (1937) gave the exchangeability theorem and sought to found probability on *coherence*: assign probabilities so that one cannot be made a sure loser in betting. He appears to derive the rules very easily from this (p. 655).
- Jaynes could have shortened his derivations this way, but finds coherence unsatisfactory in three respects (p. 655):
  1. *Aesthetic:* it is inelegant to base logic on expectation of profit.
  2. *Strategic:* if probability is defined via betting preferences, attention goes to eliciting people's personal probabilities, which Jaynes assigns to psychology. His robot has no betting preferences. His concern is the probabilities people *ought* to have given their information. Assigning priors by logical analysis of prior information is, for him, an essential part of the theory. Such analysis is almost absent from de Finetti-based expositions, though not forbidden.
  3. *Pragmatic:* rules that are coherent but not consistent in Cox's sense would be unusable. There would be no right way to calculate and no right answer (p. 656).
- To Jaynes's knowledge, de Finetti does not mention consistency as a desideratum or test for it. Rules that satisfy consistency automatically (and trivially) satisfy coherence (p. 656).
- Like Kolmogorov, de Finetti works mostly with probabilities on arbitrary uncountable sets. He treats additivity differently, which leads to layers, "like an onion", of different orders of zero probability. Jaynes says de Finetti's followers produced most of the infinite-set paradoxes, which pushed Jaynes to the finite-sets policy (Ch. 15 continues) (p. 656).

### A.3 Comparative probability (pp. 656–657)
Desideratum (I) says plausibilities are real numbers. Jaynes's reason is pragmatic: a robot brain needs a definite physical quantity. He grants that this ignores aesthetic considerations such as Euclid's qualitative style (p. 656).

(I) can be split into two simpler axioms, read as verbal statements ("given $C$, $A$ is more plausible than $B$"):
- (Ia) Transitivity: $(A|X)\ge(B|X)$ and $(B|X)\ge(C|X)$ imply $(A|X)\ge(C|X)$.
- (Ib) Universal comparability: one of $(A|C)>(B|C)$, $(A|C)=(B|C)$, $(A|C)<(B|C)$ must hold.

With both axioms, any finite set of propositions can be represented by rational numbers obeying all the orderings. A new proposition fits a unique place in the order. Between any two rationals there is another, so a number can always be assigned (p. 656).

Then Cox's theorems take over. Either some monotonic function of the numbers obeys the standard sum and product rules, or inconsistencies can be exhibited in the comparative theory (p. 657).

- Dropping transitivity is hopeless, since it would trap reasoning in circular loops (p. 657).
- Dropping universal comparability gives a *lattice* theory. $A$ and $C$ may be comparable, and $B$ and $C$ comparable, while $A$ and $B$ are not. A single real number per proposition would create false comparisons, though a lattice of vectors can represent it (p. 657).
- Savage (1954) is perhaps the best-known attempt at qualitative orderings that yield an additive measure. Fine (1973) summarizes such attempts. Jaynes says they seem motivated only by aesthetics (p. 657).
- Jaynes argues that orderings cannot be assigned arbitrarily, because the field of discourse must always be extendable without contradiction. When the ordered propositions become "everywhere dense" between impossibility and certainty, consistency requires that the theory approach the numerical one (p. 657).
- Jaynes says it appears that any computer implementing a comparative theory must at some stage represent the orderings as inequalities between real numbers. He says evading numbers offers no pragmatic advantage and is futile, and that the study of comparative theories only shows another aspect of the superiority of the Cox approach (p. 657).

*Intuition note.* If every pair of propositions in a finite set can be ranked consistently, you can attach numbers to the ranks. Cox's theorems then force the usual probability rules on those numbers. Jaynes treats transitivity as not droppable, so universal comparability is the axiom that could be relaxed (lattice theories). He argues that filling in more comparisons pushes the theory back towards the numerical one.

### A.4 Holdouts against universal comparability (pp. 658–659)
Some critics of probability as logic consider it absurd that all propositions can be compared. Jaynes says this view seems to arise from two beliefs: (1) human brains cannot do it, (2) there are examples where comparison is fundamentally impossible (p. 658).

- **Belief (1).** It carries no weight for Jaynes. His aim is to correct brains, not imitate them, and the ability to compare across contexts improves with education.
  - Example: is a severe earthquake in Tokyo on June 1, 2230 more likely than an unusually good Norwegian fish catch that day? The contexts seem unrelated. With geophysics and astrophysics one sees that the moon may affect both, through tides and crustal stresses with phase-locked periodic variations. Then the propositions seem comparable (p. 658).
- **Belief (2).** Jaynes says all alleged counterexamples he has seen involve classifying by more than one attribute.
  - Example: rocks classed by density $d$ and hardness $h$. Within a subclass where only $d$ varies, a real-number order exists, and likewise for $h$. Together they need the pair $(d,h)$, and any one-dimensional order would be arbitrary.
  - A value judgment $f(d,h)$ that fixes the trade-off, e.g. $f(d_1,h_1)=f(d_2,h_2)$, removes the arbitrariness. But then the rocks are classified by one attribute, $f$, and universal comparability returns (p. 658).
  - Plausibility theory classifies propositions by a single attribute, "degree of plausibility". Once this is understood, Jaynes thinks real-number representation need not be questioned (p. 658).
- **Two uses of comparative ideas (pp. 658–659).**
  1. For choosing between two hypotheses or actions, many numerical values lead to the same choice, so precise values would be wasted effort. A comparative theory then appears as an approximation to the numerical theory, not a generalization.
  2. The Tokyo/Norway case suggests a lattice theory might describe how we actually think better than Laplace–Bayes does, if brains lack universal comparability.

### A.5 Speculations about lattice theories (pp. 659–660)
Jaynes labels this speculative.
- Plausible reasoning would work only inside "domains" of comparable propositions. Plausibility scales might differ wildly between parts of the lattice, and this would be unnoticed until comparability increased (p. 659).
- Education is described as becoming aware of more propositions and of more logical relations among them. A small child would reason on a very open lattice, with large unconnected parts.
  - Example: a child who had studied Tutankhamen's treasures came home asking "Was Abraham Lincoln the first person?" (p. 659). He had been told the artifacts were over 3000 years old and that Lincoln lived 120 years ago, but the statements had not registered.
  - Jaynes wonders whether some primitive cultures lack any notion of time beyond one's own life, and whether anthropologists would have thought to ask (p. 659).
- As learning proceeds, the lattice gains points and links, and the scale of plausibility becomes more rigidly defined. No adult approaches universal comparability, but within a narrow specialty there may be "quasi-universal comparability" approximating Laplace–Bayes. A brain might hold several dense regions (e.g. biochemistry and musicology) with no way to relate them (p. 659).
- In the limit of universal comparability the lattice would collapse into a line, and a unique association of all plausibilities with real numbers would be possible. Within this speculation, Jaynes concludes that Laplace–Bayes theory describes the ideal limit of an "infinitely educated" brain, not actual brains. He admits the idea may be "science fiction", yet feels it must contain at least a little bit of truth, and leaves the decision to the future (p. 660).

## Toy example (ours)
*Same content, different scale.* Let $p(A|C)=0.8$. Then $p(\bar A|C)=0.2$.

- **Percent scale (A.2):** $80+20=100$ ✓.
- **Logit scale (A.3):** with natural log, $u(A|C)=\ln(0.8/0.2)=\ln 4\approx1.386$. And $u(\bar A|C)=\ln(0.2/0.8)=\ln0.25\approx-1.386$. The sum is $0$ ✓.

Now the product rule. Take $p(A|BC)=0.5$, $p(B|C)=0.6$, so $p(AB|C)=0.5\times0.6=0.3$.
- **Percent scale:** $50\times60=3000$ and $100\times30=3000$ ✓ (A.2).
- **Logit scale:** $u(AB|C)=\ln(0.3/0.7)\approx-0.847$. Meanwhile $u(A|BC)=\ln1=0$ and $u(B|C)=\ln(0.6/0.4)=\ln1.5\approx0.405$. Their sum, $0.405$, is not $-0.847$. So the product rule is not additive in $u$. It takes a more complicated form, which is Jaynes's point: the form changes with the scale but the content does not.

## Concepts
- [[kolmogorov-axioms]] (new) — KSP: σ-field $F$ on $\Omega$ plus a measure with normalization, non-negativity, additivity, continuity at zero (pp. 651–652)
- [[sigma-field]] (new) — a family of subsets containing $\Omega$, closed under complement and countable union (p. 651)
- [[continuity-at-zero]] (new) — Kolmogorov's axiom (4); for Jaynes, a sequence of states of knowledge tending to impossibility gives probability tending to 0 (pp. 652–653)
- [[probability-as-extended-logic]] — Jaynes's foundation: plausibilities obey rules forced by consistency, with AND and NOT as primitives (p. 652)
- [[cox-theorem]] — consistency forces the sum and product rules once plausibilities are real numbers (p. 657)
- [[dutch-book-argument]] — de Finetti's *coherence* (no sure loss in betting), which Jaynes rejects as a foundation (p. 655)
- [[subjective-probability]] — probability tied to betting preferences and personal opinion; Jaynes assigns the elicitation of personal probabilities to psychology (p. 655)
- [[exchangeability]] — de Finetti's theorem, called "marvellous and indispensable" (p. 655)
- [[bayes-theorem]] — for Jaynes, a consequence of Boolean associativity and commutativity, used without restriction (p. 654)
- [[principle-of-indifference-max-entropy]] — cited as an example of principles for converting information into priors, with transformation groups (p. 655)
- [[finite-sets-policy]] (new) — start from finitely many propositions; take infinite limits only when well behaved and useful (p. 654)
- [[comparative-probability]] (new) — theories using only orderings $(A|C)\ge(B|C)$ of plausibility (p. 656)
- [[universal-comparability]] (new) — any two propositions can be ordered given the same information; with transitivity it yields a real-number representation of any finite set of propositions (p. 656)
- [[lattice-theory-of-plausibility]] (new) — partially ordered plausibilities; Jaynes's speculative model of real reasoning (pp. 657, 659–660)

## Canonical instances
- [[sams-thermometer]] — finer resolution of propositions eventually serves no purpose (p. 654)
- [[borel-kolmogorov-paradox]] — Jaynes agrees with Kolmogorov's resolution (p. 654)
- [[country-boundary-analogy]] — specify a set by its points or by its boundary, i.e. disjunction or conjunction (p. 654)
- [[jones-theta-statement]] — information the robot cannot yet convert into $p(\theta)$ (p. 655)
- [[tokyo-norway-comparison]] — an apparently incomparable pair becomes comparable through a possible common cause (p. 658)
- [[rocks-density-hardness]] — two attributes force a two-number representation (p. 658)
- [[child-lincoln-question]] — an unconnected region of a child's plausibility lattice (p. 659)

## Bridges (candidates)
- [same-math] logit scale $u=\log[p/(1-p)]$ (A.3) ↔ bayesian: log-odds — the same transformation, under which the sum rule becomes $u(A)+u(\bar A)=0$.
- [structural-analogy] partially ordered plausibilities (lattice) ↔ decision theory: preferences that are incomplete — both drop completeness of the ordering.
- [structural-analogy] rocks ranked by $(d,h)$ vs. a scalar $f(d,h)$ ↔ multi-objective optimization: Pareto fronts vs. a scalarized objective — a scalar objective restores total order.
- [metaphor] "infinitely educated brain" as the limit of a dense lattice ↔ information-theory: a code approaching the entropy bound only in the limit — an ideal reached only asymptotically.

## Questions this raises
- Are Kolmogorov's axioms (3) and (4) logically independent? Jaynes says only that this is not obvious (p. 653).
- How should the robot convert qualitative information, like Jones's reaction, into a prior, and which other principles beyond maximum entropy and transformation groups exist (p. 655)?
- If orderings become "everywhere dense", can one state precisely how a comparative theory converges to the numerical one (p. 657)?
- Could a lattice theory be given exact rules for domains of comparability, and tested against human reasoning (pp. 659–660)?

## Reading notes
- Printed page = pdf − 30 (pdf 681 = p. 651).
- The text layer drops overbars and some symbols ($\Omega$, $\bar A$, $\bar f_j$). I checked them against the page images.
- On p. 652 additivity is cited as (2.85). On p. 653 it is cited as (2.58) in the sentence on $S(x)$. The images show both as printed. On p. 657 the additive measure is also cited as having property (2.85). I cannot check the equation numbers against Chapter 2 from these pages.
- Footnote 3 (p. 659) on Watson, Franklin and Crick is skipped as a side remark. Footnotes 1 and 2 are summarized in L3. The source has no exercises.
