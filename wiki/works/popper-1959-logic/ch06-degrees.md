---
id: popper-1959-logic/ch06-degrees
work: popper-1959-logic
unit: "6 Degrees of Testability (§§31–40, with Addendum 1972)"
pages: 95–120
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
# Degrees of Testability

## L0 — One line
Theories can be ranked, partially, by how severely testable they are: a theory that forbids more (a larger class of potential falsifiers) says more about the world, is logically less probable, and is preferred.

## L1 — The gist (≤ 120 words)
Can we say that one theory is more falsifiable than another? Popper compares classes of potential falsifiers. Because these classes are infinite, he drops cardinality and uses the subclass relation, then the dimension of a theory (how many singular statements are needed to refute it). Greater falsifiability goes with greater empirical content, higher universality and precision, and lower logical probability. Circles are more testable than ellipses, and the dimension of a set of curves depends on its number of freely choosable parameters. The comparison is only partial, since not all theories can be ranked. Several methodological demands turn out to reduce to one rule: prefer the most severely testable theories.

**Prerequisites:** sets and subsets; universal statements and basic statements (Popper's term for singular observation reports); "(x)(φx → fx)" notation; curves and their parameters (circle, ellipse, parabola); the idea of a potential falsifier.

## L2 — Key ideas (5–10 bullets)
- Falsifiability becomes a matter of degree: theories are compared by their classes of potential falsifiers, and this "relativizes" the falsifiability requirement (pp. 95–96).
- Cardinality does not help, because all such classes have the same cardinal number. The subclass relation fits "more/fewer" but yields only a partial order (lattice) (pp. 97–98, 101).
- Fsb (degree of falsifiability) is defined through proper inclusion; tautologies and metaphysical statements get 0, contradictions get 1 (an arbitrary choice of number), and empirical statements fall strictly between (pp. 99–100).
- Whenever two statements can be compared, the less falsifiable one is the more logically probable (probable by virtue of its logical form). This logical probability is not the numerical probability of statistics (pp. 102–103).
- Empirical content (how much a statement says about experience, defined as the class of its potential falsifiers) normally orders statements like logical content (the consequence class). So "prefer the most testable theory" equals "prefer the highest empirical content" (pp. 103–105).
- Higher universality and higher precision each raise testability. The range a statement permits is the inverse notion, and testing at higher precision needs better measurement (pp. 106–110).
- Dimension: in a chosen field of relatively atomic statements (simple statements taken as units), no conjunction of $d$ of them can falsify the theory, though some conjunctions of $d+1$ can. For curves, $d$ depends on the number of freely choosable parameters, so circle (3) < parabola (4) < ellipse (5) (pp. 113–115).
- Reducing dimensions by material means (fixing individual points) differs from formal reduction (narrowing the curve's shape). The distinction rests on invariance under coordinate transformations (pp. 117–119).

## L3 — Walkthrough

### Introduction (p. 95)
Theories may be more or less severely testable, i.e. more or less easily falsifiable. Popper compares degrees of testability through the classes of potential falsifiers. This is independent of whether an absolute line between falsifiable and non-falsifiable theories can be drawn. The chapter "relativizes" the falsifiability requirement (p. 95).

### 31 A programme and an illustration (pp. 95–97)
- A theory is falsifiable if the class of its potential falsifiers (the basic statements it forbids) is non-empty (p. 95). Picture all basic statements as a circle, with events as narrow sectors. The forbidden sectors of different theories may differ in width (pp. 95–96). Whether this "more" can be made precise is left open for the moment.
- A theory with a larger class of potential falsifiers has more chances of refutation and "says more". The permitted class is smaller, but the theory asserts nothing about it. So empirical content increases with degree of falsifiability (p. 96).
- If the forbidden sector grows, only a narrow permitted sector remains (some must remain if the theory is consistent). Such a theory is easy to falsify but asserts a great deal (p. 96).
- Theoretical science aims at such theories: it restricts permitted events to a minimum, ideally so that any further restriction would produce an actual falsification. The theory would then describe "our particular world" as precisely as a theory can (pp. 96–97).

*Intuition note.* Saying more means ruling out more. A theory that rules out a lot can fail easily, and that is why it is informative.

### 32 How are classes of potential falsifiers to be compared? (pp. 97–98)
The classes are infinite, so "more" and "fewer" need a precise meaning. Counting forbidden events does not help either, because conjoining a forbidden event with any other event gives another forbidden event (p. 97). Three candidates:
1. **Cardinality.** Useless, because the classes have the same cardinal number for all theories. A footnote cites Tarski: under certain assumptions every class of statements is denumerable. Measure is inapplicable for the same reason (p. 97).
2. **Dimension.** It ranks sets by the richness of neighbourhood relations among their elements (p. 97). It can be linked to the degree of composition of basic statements: a conjunction of basic statements is again a basic statement, but more composite. One must use the composition of *permitted* statements, not forbidden ones. Forbidden events can have any degree of composition. Some statements are permitted merely because their composition is too low to contradict the theory (p. 98). (A footnote by Popper explains the choice of composite rather than complex, since the English complex suggests the opposite of simple (p. 98).)
3. **Subclass relation.** If $\alpha \subset \beta$ properly, the difference class is the complement of $\alpha$ with respect to $\beta$. This matches "more/fewer", but compares two classes only if one includes the other. Intersecting or disjoint classes are non-comparable (p. 98).

### 33 Degrees of falsifiability compared by the subclass relation (pp. 99–100)
Definitions, introduced provisionally (p. 99):
1. $\mathrm{Fsb}(x) > \mathrm{Fsb}(y)$ if and only if the class of potential falsifiers of $x$ includes that of $y$ as a proper subclass.
2. If the classes are identical, $\mathrm{Fsb}(x) = \mathrm{Fsb}(y)$.
3. If neither class includes the other as a proper subclass, the degrees are non-comparable: $\mathrm{Fsb}(x) \,\|\, \mathrm{Fsb}(y)$.

Consequences:
- Under (1) the complement class is non-empty. For universal statements it must be infinite. So two strictly universal theories cannot differ merely in that one forbids finitely many single occurrences permitted by the other (p. 99).
- Tautological and metaphysical statements have empty classes of potential falsifiers. There is only one empty class, so they are identical: $\mathrm{Fsb}(t) = \mathrm{Fsb}(m) = 0$ and $\mathrm{Fsb}(e) > 0$ for empirical $e$ (p. 99).
- A self-contradictory statement $c$ has all logically possible basic statements as potential falsifiers. So $\mathrm{Fsb}(c) > \mathrm{Fsb}(e) > 0$ (p. 100). Footnote *2 refers the reader to appendix *vii (p. 100).
- Setting $\mathrm{Fsb}(c) = 1$ arbitrarily gives $1 > \mathrm{Fsb}(e) > 0$ (open interval). This expresses both the consistency requirement and the falsifiability requirement (p. 100).

*Intuition note.* Fsb works like "is the forbidden set bigger?" Popper deliberately lets it say "no verdict" when neither set contains the other.

### 34 The structure of the subclass relation. Logical probability (pp. 100–103)
- Fig. 1 (p. 100) pairs a diagram of classes I–V (showing subclass relations) with a lattice of statements 1–5. Arrows run from better testable to less testable statements (they correspond fairly precisely to derivability arrows, §35) (p. 101).
- Sequences such as i–ii–iv or i–iii–v begin at 1 (the contradiction $c$) and end at the empty class (the tautology $t$). Paths can cross. The structure is a lattice with nodal points (statements 4 and 5). It is totally connected only at $c$ and $t$ (p. 101).
- Not all statements can be put on one scale, because that would arbitrarily make non-comparable statements comparable (pp. 101–102). A footnote maintains that any metric on all statements contains an arbitrary, extra-logical element. This is clear for statements about measurable properties (e.g. that all adult men are more than two feet high), where the metric of content would depend on the metric of the predicate (pp. 101–102).
- One sequence could be selected and numbered with proper fractions, closer to $c$ meaning a higher number. This would be arbitrary, but it shows the link to probability (p. 102).
- Whenever two statements are comparable, the less falsifiable one is the more probable by virtue of its logical form. Popper calls this **logical probability**; it must not be confused with the numerical probability of games of chance and statistics. Logical probability is complementary to falsifiability: probability 1 corresponds to falsifiability 0, and vice versa (p. 102). Footnotes: since 1938 he says "absolute logical probability" to separate it from relative (conditional) logical probability. He also notes parallels with Bolzano's "validity" and Keynes's comparison of a priori probabilities of generalizations (p. 102).
- Section 72 is said to link numerical probability to logical probability. Numerical probability is interpreted as applying to a subsequence of the logical-probability order for which a measurement system can be defined from frequency estimates (p. 103).
- The comparisons also apply to singular statements, e.g. theories together with initial conditions. There the class of potential falsifiers must not be mistaken for a class of events (a class of homotypic basic statements), since it is a class of occurrences (p. 103).

*Intuition note.* The less a statement forbids, the more likely it is to be true just because of what it says. Tautologies are the most probable and contradictions the least.

### 35 Empirical content, entailment, and degrees of falsifiability (pp. 103–105)
- **Empirical content** of $p$ = class of its potential falsifiers. **Logical content** (Carnap's "content") = class of all non-tautological statements derivable from $p$, its consequence class (p. 103).
- If $p \to q$ ($q$ derivable from $p$), the logical content of $p$ is at least that of $q$. Mutual derivability means equal content. If $q$ follows from $p$ but not conversely, $p$ has the larger consequence class and greater logical content (logical force) (pp. 103–104). A footnote clarifies that "$p \to q$" here means that the conditional is logically true, i.e. "$p$ entails $q$" (p. 104).
- If the statements contain no metaphysical elements, the two comparisons agree. Popper requires (p. 104):
  - (a) equal logical content implies equal empirical content;
  - (b) greater logical content implies greater or at least equal empirical content;
  - (c) greater empirical content implies greater or non-comparable logical content.

  The qualifications in (b) and (c) are needed because $p$ might be $q$ conjoined with a purely existential or other metaphysical statement. Then $p$ has more logical content but not more empirical content (p. 104).
- For purely empirical statements, falsifiability comparison can thus largely rest on derivability. Both relations are lattices totally connected at self-contradiction and tautology. A contradiction entails every statement, and a tautology is entailed by every statement (p. 105). Synthetic statements in general, including non-empirical ones, lie in the open interval between them (p. 105).
- **Positivist thesis** (reported): non-empirical statements are meaningless. That would make Popper's empirical/synthetic distinction superfluous. Popper says this usage is feasible but more likely to confuse than clarify (p. 105).
- Conclusion: comparing empirical content equals comparing degrees of falsifiability. So the rule to prefer the most severely testable theories (the anti-conventionalist rules, §20) equals a rule to prefer the highest empirical content (p. 105).

*Intuition note.* "Says more" can be read two ways, by what follows from the statement or by what it forbids. For purely empirical statements these agree. Metaphysical add-ons raise only the first.

### 36 Levels of universality and degrees of precision (pp. 105–107)
Popper says other methodological demands can be reduced to that for the highest possible empirical content; two outstanding ones are the highest attainable **universality** and the highest attainable **precision** (p. 105). Four conceivable laws (p. 106):
- $p$: all orbits of heavenly bodies are circles;
- $q$: all orbits of planets are circles;
- $r$: all orbits of heavenly bodies are ellipses;
- $s$: all orbits of planets are ellipses.

$p$ entails all others; $q$ and $r$ each entail $s$ (p. 106).
- $p \to q$ lowers universality (planetary orbits are a proper subclass of heavenly-body orbits). If $q$ is falsified so is $p$, but not conversely (p. 106).
- $p \to r$ lowers precision (circles are a proper subclass of ellipses). $p \to s$ lowers both, $q \to s$ precision only, and $r \to s$ universality only. Higher universality or precision means greater content and testability (p. 106).
- In the normal form $(x)(\varphi x \to f x)$: $p$ is of greater universality than $q$ if $(x)(\varphi_q x \to \varphi_p x)$ is tautological, with $\varphi_p$ not equivalent to $\varphi_q$. $p$ is of greater precision if $(x)(f_p x \to f_q x)$ is tautological (pp. 106–107).
- Rule: if both universality and precision of two statements are comparable, the less universal or less precise one is derivable from the other. This fails when one is more universal and the other more precise (as with $q$ and $r$) (p. 107).
- Footnote check formula: $[(a \to b)\cdot(c \to d)] \to [(b \to c) \to (a \to d)]$, with $p$ for $b \to c$ and $q$ for $a \to d$ (p. 107).
- The methodological decision sometimes read metaphysically as the principle of causality is to leave nothing unexplained, i.e. to try to deduce statements from others of higher universality. It reduces to preferring theories that can be most severely tested (p. 107).

*Intuition note.* Widening the "all" (heavenly bodies instead of planets) or narrowing the predicate (circles instead of ellipses) makes a claim easier to break. Where one law is more universal and the other more precise (q and r), neither entails the other.

### 37 Logical ranges. Notes on the theory of measurement (pp. 108–110)
- The **range** of a statement is the class of basic statements it permits, its "free play". Ranges are inverse to classes of potential falsifiers, so they relate as logical probabilities do (p. 108).
- If two theories differ less than measurement precision can detect, no experiment decides between them until the technique improves. The prevailing technique fixes a region within which discrepancies are permitted. So the rule of maximal testability entails raising measurement precision as much as possible (pp. 108–109). A footnote says Popper believes Duhem wrongly interpreted this point (p. 108).
- Measurement never gives strict coincidence of points. The object lies between two marks, or between imaginary marks if we estimate within the interval. So an interval always remains (p. 109). Example: Millikan's electron charge $e = 4.774\cdot 10^{-10}$ with imprecision $\pm 0.005\cdot 10^{-10}$ (p. 109).
- Problem: the bounds of the interval themselves need bounds. Giving them is useful only if they are fixed far more precisely, by several orders of magnitude. So the bounds are really small intervals, with still smaller bounds, and so on. These are the "unsharp" or **condensation bounds** (pp. 109–110).
- This does not presuppose the theory of errors or probability; rather it supplies background without which the theory of errors makes little sense (p. 110).
- Popper thinks this sheds some light on the superiority of measurement over purely qualitative methods. Condensation bounds apply only where orders of magnitude and measurement methods are defined (p. 110).

*Intuition note.* A precise theory allows only a narrow range, so testing it well calls for precise measurement. A measurement is not an exact point but an interval whose edges are themselves known only roughly, though much more precisely than the interval itself.

### 38 Degrees of testability compared by reference to dimensions (pp. 110–115)
- The subclass method sometimes works: Pauli's exclusion principle as an auxiliary hypothesis greatly raises the precision, and with it the testability, of the older quantum theory (p. 111).
- It is not enough in other cases. **Frank** (reported): very universal statements, such as conservation of energy in Planck's formulation, tend to become tautological unless the initial conditions can be fixed by few measurements. The number of parameters needed is not captured by the subclass relation (p. 111).
- A falsifying basic statement is the initial conditions conjoined with the negation of the prediction (§28). Fewer magnitudes needed means a less composite falsifier. So it may be possible to compare theories by the minimum degree of composition a basic statement needs to contradict them, provided basic statements can be compared for composition. Basic statements below that minimum are permitted by the theory merely because of low composition (p. 111).
- Difficulty: composition is hard to read off a statement. Analysing universal names can split a statement into conjuncts (e.g. a statement about a glass of water at place $k$ into one about a glass containing a fluid there and one about water there). There is no natural end to this, since new universals can always be defined (p. 112). Fixing absolute atomic statements (as in Wittgenstein, Whitehead and Russell) would give an absolute zero of composition, but Popper regards this as unsuitable. It would restrict the free use of scientific language (pp. 112–113). A footnote notes that meanings of terms such as "matter" or "atom" change with the theory (p. 113).
- **Relatively atomic** statements: choose arbitrarily a class generated by a schema or matrix (e.g. a statement that a measuring apparatus at a given place has its pointer between two given marks) (p. 113). These statements, with all their conjunctions, form a **field**. A conjunction of $n$ distinct relatively atomic statements is an **$n$-tuple** of the field, with degree of composition $n$ (p. 113).
- **Characteristic number $d$:** if a theory $t$ cannot be falsified by any $d$-tuple of the field, but can be by certain $(d+1)$-tuples, $d$ is the characteristic number of $t$ with respect to that field. All statements of the field with composition $\le d$ are permitted by $t$, whatever they say (p. 113).
- To avoid inconsistencies between fields, one uses a **field of application**, a field with a characteristic number that also meets further conditions (appendix i). The characteristic number with respect to it is the **dimension** of $t$ (pp. 113–114).
- Analogy: the permitted low-composition statements form, for $d = 3$, a three-dimensional sub-space. Going from $d=3$ to $d=2$ is like going from solid to surface. The smaller $d$, the more severely restricted the permitted class and the higher the falsifiability (p. 114).
- Singular statements of all kinds are allowed in a field of application. Highly composite singular statements are assumed to correspond to highly composite basic statements. It can thus be assumed that a theory of higher dimension has a class of basic statements of higher dimension, all permitted by it (p. 114).
- Relation of the two methods: if only one or neither applies, there is no conflict. If both apply, two theories of equal dimension may still differ in falsifiability by the subclass method; in that case the subclass verdict is accepted as the more sensitive. In all other cases the methods agree, because the dimension of a class is greater than or equal to that of its subclasses (pp. 114–115, citing Menger).

*Intuition note.* Dimension asks: how many separate observations at minimum must be put together before the theory can be contradicted? A theory that needs few is more testable.

### 39 The dimension of a set of curves (pp. 115–116)
- The field of application can sometimes be the field of graphic representation, where each point of the graph paper matches a relatively atomic statement. The theory's dimension then equals the dimension of the set of curves (p. 115).
- $q$ (circles) is three-dimensional: at least four singular statements (four points) are needed to falsify it. $s$ (ellipses) is five-dimensional: at least six points. A parabola hypothesis is four-dimensional (p. 115). So dimensions let us compare theories, such as circle versus parabola, that the subclass relation cannot compare. A set has dimension $d$ if $d$ points are necessary and sufficient to single out one curve. Algebraically, $d$ depends upon the number of freely choosable parameters, and this number is characteristic of degree of falsifiability (p. 115).
- **Kepler.** Popper does not claim the belief in perfection that guided Kepler was inspired by methodology. He believes Kepler owed his success partly to starting with an easily falsified circle hypothesis. A less testable start might have yielded no result, given calculations whose very basis was uncertain. The clear negative result was his first real success. This matches the method of elimination, applicable only to sufficiently falsifiable theories (p. 116).

### 40 Two ways of reducing the number of dimensions of a set of curves (pp. 116–119)
- Dimensions of sets (p. 116 and table, p. 117): circles 3, circles through a given point 2, through two given points 1. Each further given point reduces dimension by one. Straight lines 2 (as for circles through a point); parabolas 4; conics 5 (added step: inferred from the table, where a conic through one point is four-dimensional, through two three, through three two; the text does not state it directly). A footnote says one could start with the empty "minus-one-dimensional" class (p. 117).
- Other reductions: ellipses with a given axis ratio, or a given eccentricity, are four-dimensional (as are parabolas). Going from ellipse to circle fixes eccentricity 0 or axis ratio 1 (p. 117).
- Fixing a point will often correspond to accepting a singular statement (an initial condition). Going from ellipse to circle reduces the dimension of the theory itself (p. 117).
- **Material reduction:** specifying points or equivalents, with no stipulation on shape. **Formal reduction:** narrowing the form, e.g. ellipse to circle (p. 118).
- The distinction is hard to make sharp. Algebraically both replace a parameter by a constant. Equating two parameters to 0 and 1 gives the circle (formal). Equating the absolute term to 0 specifies a point (material). The key: material reduction brings an *individual name* into the definition of the set, formal reduction a *universal name* (p. 118).
- Definitions of "all ellipses" or "all circles" in a given plane do not depend on where the Cartesian coordinates are drawn. They are invariant under displacements and similarity transformations (the Euclidean group). A set through a specific point needs an individually specified coordinate system, so it is not invariant (pp. 118–119).
- Transformation groups form a hierarchy. $D_1$ is called equally general to, or more general than, $D_2$ if it is invariant under the same group (or a more general one). A reduction is **formal** if it does not diminish the generality of the definition, otherwise **material** (p. 119).
- When comparing falsifiability by dimension one must also take generality into account. For theories that are "geometrical" only through a graph (e.g. pressure against temperature), rotation-invariance should not be required, since the axes represent different things (p. 119).
- Closing: these methods help with the problem of simplicity (next chapter) and also put the "probability of hypotheses" and corroboration in a new light (pp. 119–120).

### Addendum, 1972 (p. 120)
Popper restates that content (or testability, or simplicity) may have degrees, which may thus be said to relativize falsifiability, whose logical basis remains modus tollens. He says the aim of science can be identified with growth of content: "the more they prohibit, the more they say" (p. 120). He adds two later developments: (3) relativizing content to the problem under discussion, and (4) truth content and verisimilitude (p. 120).

## Toy example (ours, not from the text)
Data are points $(x, y)$, and we only allow statements with distinct $x$-values (so each hypothesis is a function). **H1:** all points lie on a straight line $y = ax + b$ (2 parameters, so $d = 2$). **H2:** all points lie on a parabola $y = ax^2 + bx + c$ (3 parameters, so $d = 3$). Lines are the case $a = 0$ of parabolas.

- Subclass comparison: every set of points that fits a line fits some parabola. So H2 forbids less than H1, and H1 is falsifiable in a higher degree.
- Dimension comparison. Take three points with distinct $x$: $(0,0)$, $(1,1)$, $(2,0)$. They are not on one line (slope from the first to second is 1, from the second to third is $-1$). So three points falsify H1. A parabola passes through any three such points: with $y = ax^2 + bx$ we get $a + b = 1$ and $4a + 2b = 0$, so $b = -2a$, then $a - 2a = 1$, giving $a = -1$, $b = 2$. H2 survives.
- Add a fourth point $(3, 5)$. The parabola predicts $-9 + 6 = -3 \neq 5$, so H2 is falsified by four points.
- So H1 needs 3 points and H2 needs 4, giving $d = 2$ and $d = 3$, in line with the parameter count.

## Concepts
- [[falsifiability]] — here a matter of degree, measured by the class of potential falsifiers (p. 95)
- [[potential-falsifiers]] (new) — the class of basic statements a theory forbids (p. 95)
- [[degree-of-falsifiability]] (new) — Fsb, ordered by proper inclusion of falsifier classes; only a partial order (pp. 99, 101)
- [[empirical-content]] (new) — the class of a statement's potential falsifiers; grows with falsifiability (pp. 96, 103)
- [[logical-content]] (new) — the consequence class: all non-tautological statements derivable from it (p. 103)
- [[logical-probability]] (new) — probability due to logical form; complementary to falsifiability; not statistical probability (p. 102)
- [[range-spielraum]] (new) — the class of basic statements a statement permits, inverse to its falsifier class (p. 108)
- [[condensation-bounds]] (new) — "unsharp" interval bounds, themselves small intervals of much smaller order (p. 110)
- [[degree-of-composition]] (new) — number of relatively atomic statements conjoined in a statement (p. 113)
- [[dimension-of-a-theory]] (new) — the characteristic number $d$ with respect to a field of application (p. 114)
- [[material-vs-formal-reduction]] (new) — lowering dimension by individual stipulations (points) versus by narrowing the curve's shape; separated by invariance under coordinate transformations (p. 118)
- [[demarcation problem]] — only touched: here the absolute line is bracketed and degrees are studied (p. 95)

## Canonical instances
- [[orbits-p-q-r-s]] — four orbit laws showing the effects of universality and precision on derivability and testability (p. 106)
- [[kepler-circle-hypothesis]] — an easily falsified hypothesis that gave a clear negative result and led to progress (p. 116)
- [[millikan-electron-charge]] — a measurement quoted with an interval of imprecision (p. 109)
- [[pauli-exclusion-principle]] — an auxiliary hypothesis that raises precision and testability (p. 111)
- [[conservation-of-energy-frank]] — a highly universal law that risks becoming tautological unless initial conditions need few magnitudes (p. 111)
- [[curve-dimensions]] — circle 3, parabola 4, ellipse 5, with reductions by points (pp. 115–117)

## Bridges (candidates)
- [structural-analogy] Falsifier classes ordered by inclusion (a lattice) ↔ order theory: a partial order with top and bottom elements ($c$ and $t$) — some pairs are simply incomparable.
- [structural-analogy] Logical probability (less content means more probable) ↔ information theory: informativeness is inversely related to probability.
- [structural-analogy] Dimension of a curve set equals number of free parameters ↔ statistics/modelling: model complexity as number of parameters; fewer free parameters means more ways the data can contradict the model.
- [structural-analogy] Range of permitted basic statements ↔ probability theory: an event as a set of outcomes (a smaller permitted set is like a smaller event).

## Questions this raises
- If the subclass relation gives only a partial order, how often can rival real theories actually be compared? (Footnotes point to appendix *vii, which is not in this unit.)
- Does fewer parameters always mean better testability, given the problem that "relatively atomic" is chosen arbitrarily?
- How does "logical probability" relate to the numerical probability of hypotheses and to corroboration, which Popper promises to treat (pp. 103, 119–120)?
- How does the preference for high content relate to the concept of simplicity of theories, announced as the next topic (p. 119)?

## Reading notes
- Printed page = pdf page − 29 (pdf 124 = p. 95).
- Footnotes with an asterisk (e.g. *1, *2) are visible alongside numbered footnotes. They comment on the main text and point to appendices that are not in this unit (e.g. *vii, *ix). The "Addendum, 1972" is dated in the text. I treat all of these as later additions to the original text.
- Page 107, footnote 1: the printed formulas have unbalanced brackets. I have therefore given only the clean version of the check formula that the same footnote supplies in letters.
- Page 99: the phrase "any statements whatsoever" is printed so (apparently a slip for the singular).
- Page 109: in the text layer the exponents of Millikan's value are flattened (4.774.10 − 10); I read it as $4.774\cdot 10^{-10}$ with imprecision $\pm 0.005\cdot 10^{-10}$.
- Fig. 1 (p. 100) and the p-q-r-s diagram (p. 106) were checked in the images; the table (p. 117) was read from the text layer, where cells without a class are marked with a dash.
- Appendices i, *vii–*ix and §72, among others, are cited but not part of this unit.
