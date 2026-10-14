---
id: popper-1959-logic/ch03-theories
work: popper-1959-logic
unit: "3 Theories (sections 12–18)"
pages: 37–56
fields: [analytic-philosophy]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Theories (Popper, *The Logic of Scientific Discovery*, ch. 3)

## L0 — One line
Popper treats scientific laws as strictly universal statements that forbid certain events, so they can be refuted but not verified, and a refuted prediction falsifies the whole system that deduced it.

## L1 — The gist (≤ 120 words)
What logical form do scientific theories have? Popper treats laws as strictly universal statements, not finite lists of observations. Causal explanation deduces a singular prediction from laws plus initial conditions. Laws work like prohibitions, so one accepted counterexample refutes them. Purely existential statements cannot be falsified, so Popper counts them as non-empirical. Theories aim at axiom-system form because severe tests need a definite system. Axioms can be read as conventions or as empirical hypotheses; Popper adopts a rule against using undefined terms as if implicitly defined. Since a false conclusion refutes the premises it was deduced from (modus tollens), the whole premise-system is falsified; in general blame cannot be pinned on one statement.

**Prerequisites:** basic propositional logic (if-then, negation, conjunction); the idea of a class and its elements; the problem of induction (from the preceding chapters).

## L2 — Key ideas (5–10 bullets)
- A causal explanation deduces a singular statement from universal laws plus singular initial conditions. Popper notes that the initial conditions are what is usually called the 'cause' and the prediction the 'effect', and he avoids both terms (pp. 38–39).
- Popper does not assert a "principle of causality". Depending on how 'can' is read, it is either tautological or synthetic but unfalsifiable; Popper neither adopts nor rejects it and excludes it from science as metaphysical. He proposes instead a methodological rule: do not abandon the search for universal laws (p. 39).
- Strictly universal statements (about unlimited space and time) differ from numerically universal ones (about a finite region). The latter are equivalent to singular statements or conjunctions of them, and Popper classes them as singular. Popper proposes by convention to treat laws as strictly universal (pp. 40–42).
- Universal and individual concepts must be kept apart. Individual concepts need proper names in their definition. Neither "abstraction" from individual concepts nor description by universal properties can bridge the gap (pp. 43–47).
- Laws are non-existence statements ("prohibitions"), hence falsifiable. Isolated strictly existential statements are not falsifiable, so Popper treats them as metaphysical (pp. 47–49).
- Universal and existential statements are logically symmetric. The asymmetry of verification and falsification comes from the line drawn by the demarcation criterion (the rule that singular statements serve as test-statements); Popper adds that 'only' should not be taken too seriously (pp. 49–50).
- An axiomatized system needs four properties: consistent, independent, sufficient, necessary. Axioms can be read as conventions (analytic) or as empirical hypotheses, and using undefined primitive terms as if implicitly defined destroys empirical character, so Popper adopts a rule against it (pp. 50–54).
- By modus tollens (if $p$ follows from $t$ and $p$ is false, then $t$ is false), the falsification reaches the whole deducing system. Only if $p$ is independent of some part can we say that part is not involved; in some cases, perhaps by considering levels of universality, the falsification can be attributed to a definite hypothesis (pp. 55–56).

## L3 — Walkthrough

### Opening (pp. 37–38)
- The empirical sciences are systems of theories, so the logic of scientific knowledge can be called a theory of theories. Theories are universal statements (p. 37).
- Popper does not think it helpful to say that singular statements are 'concrete' while theories are merely symbolic, because the same may be said of even the most 'concrete' statements. All linguistic representation consists of signs or symbols (p. 37).
- Footnote *1 (a later comment) calls this a criticism of *instrumentalism*, the view that a theory is only a tool for prediction. Popper's position there: ordinary language is full of theories, and observation is always observation in the light of theories. The theorist is interested in explanation itself. Predictions matter to him because they test theories (p. 37, n. *1).
- Theories are nets cast to catch "the world"; we try to make the mesh finer (pp. 37–38).

### 12. Causality, explanation, and the deduction of predictions (pp. 38–40)
- **Definition.** To give a causal explanation of an event is to deduce a statement describing it. The premises are one or more universal laws plus singular statements, the *initial conditions* (p. 38).
- **Example.** A thread has tensile strength 1 lb. and a weight of 2 lbs. is put on it.
  - Hypothesis (a universal law): whenever a thread is loaded with more than its characteristic weight, it breaks.
  - Initial conditions (singular statements): that the weight characteristic for this thread is 1 lb., and that the weight put on this thread was 2 lbs.
  - Deduced singular prediction: this thread will break (p. 38).
- Footnote *1 gives a finer analysis with two laws and two initial conditions:
  - Law 1: for every thread of structure $S$ there is a characteristic weight $w$ such that it breaks under any heavier weight.
  - Law 2: for threads of structure $S_1$, $w_1 = 1$ lb.
  - Initial conditions: that this is a thread of structure $S_1$, and that the weight to be put on it is 2 lbs. (p. 38, n. *1).
- "Prediction" includes statements about the past (retrodictions) and given statements to be explained (p. 38, n. *2).
- Initial conditions describe what is usually called the cause, and the prediction the effect. Popper avoids both terms. He does not restrict "causal explanation" to action by contact (differential equations), as physics usually does (p. 39).
- **The principle of causality** says that any event can be causally explained, that is, deductively predicted. It depends on how "can" is read (p. 39):
  - If "can" means it is always logically possible to construct such an explanation, the principle is tautological, because for any prediction some universal statements and initial conditions yield it. Whether those statements were tested is a different question.
  - If "can" means the world is governed by strict laws, the principle is synthetic. But then it is not falsifiable, as Popper says will be shown in section 78 (p. 39).
  - So Popper neither adopts nor rejects it. He excludes it from science as metaphysical (p. 39).
- **Methodological rule** (proposed by Popper; it corresponds so closely to the principle of causality that the principle might be regarded as the rule's metaphysical version): we must not abandon the search for universal laws and a coherent theoretical system. We must never give up trying to explain causally any kind of event we can describe (p. 39). Popper rejects the view that recent physics requires giving up this rule (p. 40, discussed in section 78).
- Footnote marked only * in the text layer (p. 40): the decision to seek causal explanation is the theoretician's adoption of his aim, namely explanatory theories, if possible true ones. Popper says this interest is irreducible to the technological interest in predictions. The theorist's interest in predictions arises from his interest in testing his theories (p. 40, n. *).

*Intuition note.* An explanation is a deduction: laws plus facts about this case give a statement about the event. Popper does not claim that every event has such an explanation. He proposes instead a rule that we should keep looking for one.

### 13. Strict and numerical universality (pp. 40–42)
- Two kinds of universal synthetic statement (p. 40):
  - *Strictly universal* statements are theories or natural laws.
  - *Numerically universal* statements are equivalent to singular statements or to conjunctions of them, and Popper classes them as singular.
- **Examples.** (a) The energy of all harmonic oscillators never falls below $h\nu/2$. (b) The height of all human beings now living on earth never exceeds, say, 8 ft (pp. 40–41).
  - Formal logic treats them alike, as "formal" or "general" implications. Popper stresses the difference (p. 41).
  - (a) claims truth for any place and time. (b) concerns a finite class in a finite spatio-temporal region. In principle (b) can be replaced by a conjunction of singular statements, because one can enumerate the finite class (p. 41).
  - (a) could be so replaced only if the world were bounded in time with finitely many oscillators. Popper makes no such assumption, so he reads (a) as an "all-statement" about unlimited individuals (p. 41).
- **Opponents.** Some hold that every synthetic universal statement must be translatable into a finite conjunction of singular statements. They say strictly universal statements can never be verified and reject them, citing a verifiability criterion of meaning or a similar consideration (pp. 41–42).
- On that view the problem of induction would seem solved, since inferences to numerically universal statements can be admissible. But the *methodological* problem remains. Verifying a natural law would require checking every event it could apply to, which is impossible (p. 42).
- **Decision.** Whether laws are strictly or numerically universal cannot be settled by argument, only by convention. Popper finds it useful and fruitful to treat laws as synthetic, strictly universal, non-verifiable statements of the form "Of all points in space and time it is true that …" (p. 42).
- The distinction is applied to synthetic statements only, though it could be applied to analytic ones. Examples in footnote 3: every natural number has a successor (apparently the strict kind), against: with the exception of 11, 13, 17 and 19, all numbers between 10 and 20 are divisible (apparently the numerical kind; the footnote gives them as examples without labels) (p. 42, n. 3).

*Intuition note.* The claim that all people in this room are under 8 ft can be checked person by person. The claim about all oscillators, anywhere, ever, cannot be exhausted. Popper chooses to read laws in the second way, so laws cannot be verified, though they can be falsified.

### 14. Universal concepts and individual concepts (pp. 42–47)
- **Examples.** Universal: "dictator", "planet", "H₂O". Individual: "Napoleon", "the earth", "the Atlantic". Individual concepts appear to be characterized by being proper names or by having to be defined using proper names. Universal concepts can be defined without them (p. 43).
- **Why it matters.** Applying science means deducing singular predictions from universal hypotheses, and every singular statement must contain individual names (p. 43).
  - Spatio-temporal coordinates rest on proper names for their origin (Greenwich, the year of Christ's birth). Footnote 1 notes that units of measurement could in principle be defined by universal names such as the wavelength of light (p. 43 and n. 1).
- Vague words like 'this thing here', with ostensive gestures (pointing), can sometimes act as individual names. Universal concepts can also be indicated, if only vaguely, by pointing plus a phrase like 'and other similar things'. We learn universal words this way (pp. 43–44).
- **Logical basis.** Individual concepts can be concepts of classes. Example: Lux, the author's dog, is an element of the individual class "Viennese dogs" and also of the universal class "mammals". The Viennese dogs are a sub-class of the individual class "Austrian dogs" and of the universal class "mammals" (p. 44).
  - Words like "mammal" and "dog" are ambiguous. Whether they are individual or universal depends on whether we mean a race of animals on our planet or a kind of physical body described by universal properties (p. 44).
  - Footnote *1: "pasteurized" is individual if defined by Pasteur's advice, and universal if defined as heated to 80 °C for ten minutes (p. 44, n. *1).
- **Definition** (Popper says it is of little value, since it just reduces the idea to that of a proper name): an individual concept is one in whose definition proper names or equivalent signs are indispensable. If all reference to proper names can be eliminated, it is universal (p. 44).
- **Two failures** (p. 45):
  - Identifying an individual thing only by universal properties describes the universal class of all things having them. Whether any individual things fit, and how many, stays open. A universal coordinate system does not change this (p. 45).
  - Defining universal names from individual names also fails. "Abstraction" from individual to universal concepts is a near relation of inductive logic, and the two are "equally impracticable". The classes obtained, such as "Napoleon's generals", remain individual concepts (p. 45).
  - Popper notes "a complete analogy" between the problem of universals and the problem of induction (p. 45).
- The distinction is not the distinction between classes and elements. Both kinds of name can name classes and elements (p. 45).
- **Carnap.** Carnap argues that the distinction is unjustified, because every concept can be seen as individual or universal and almost all individual concepts are class names. Popper replies that the last assertion is correct but irrelevant (p. 46).
- Footnote 5: Russell's individuals/universals distinction is different. In Russell's terms "nitrogen" is an individual, in Popper's scheme a universal (p. 46, n. 5).
- Symbolic logic is no more adequate for the problem of universals than for the problem of induction (pp. 46–47).
- Footnote 6: any singular statement can be written as a general implication, so general implications need not be universal statements. Example: the statement that Napoleon was born in Corsica becomes $(x)\,(x = N \rightarrow \phi x)$, where $\phi x$ means that $x$ was born in Corsica (p. 47, n. 6).

*Intuition note.* A law is about kinds of things. A prediction about this thread, today, must name something particular. Popper says you cannot get the first kind of word from the second by piling up cases.

### 15. Strictly universal and existential statements (pp. 47–50)
- The absence of individual names is not enough to make a statement universal. Many ravens are black, some ravens are black and there are black ravens also contain only universal names, yet Popper would not call them universal (p. 47).
- Statements with only universal names are *strict* or *pure*. These include:
  - strictly universal statements (all ravens are black), and
  - strictly (purely) existential, or "there-is", statements (there exists at least one black raven) (p. 47).
- The negation of a strictly universal statement is equivalent to a strictly existential one, and vice versa. Not all ravens are black says that there are non-black ravens (p. 47).
- **Laws as prohibitions.** Natural laws are strictly universal, so they can be written as non-existence statements. Examples: there is no perpetual motion machine (conservation of energy) and there is no electrical charge other than a multiple of the elementary charge (p. 48).
  - Laws rule out states of affairs, and that is why they are falsifiable. Accepting one singular statement that asserts a forbidden thing refutes the law (p. 48).
- Strictly existential statements cannot be falsified. No basic statement contradicts the statement that there are white ravens. Under the demarcation criterion adopted, Popper treats them as non-empirical or "metaphysical" (p. 48).
- **Objection** (admitted "with justice"): some physical theories have existential form, such as statements derived from the periodic system asserting elements of given atomic numbers (p. 48).
  - **Reply:** a testable version needs much more than a purely existential statement. Hafnium (atomic number 72) was found only after Bohr deduced several of its properties from his theory. Bohr's theory is strictly universal, not an isolated existential statement (pp. 48–49).
  - Footnote *1: an isolated existential statement is never falsifiable. In context with other statements it may add to the empirical content of the whole and raise its testability. The system is then scientific rather than metaphysical (p. 49, n. *1).
- Strict statements are not limited in space and time. That is why existentials are not falsifiable (we cannot search the whole world to show something never exists) and universals are not verifiable (p. 49).
- Both kinds are *unilaterally decidable* in principle: finding something somewhere may verify an existential statement or falsify a universal one (p. 49).
- The asymmetry from section 6 is not a logical one. The logical relations are symmetric. Only the line drawn by the demarcation criterion produces the asymmetry (pp. 49–50).
  - Footnote *2: "only" should not be taken too seriously. If singular statements are the test-statements, universals are only falsifiable and existentials only verifiable (p. 50, n. *2).

*Intuition note.* A claim that there is no X can be broken by finding one X. A claim that there is an X cannot be broken by failing to find X, because you might not have looked everywhere. Under Popper's demarcation criterion, statements of the first kind count as empirical, and isolated statements of the second kind do not.

### 16. Theoretical systems (pp. 50–51)
- Theories keep changing, as one would expect given Popper's characterisation of empirical science. As a rule only branches of science, and only temporarily, acquire a well-built system form (p. 50).
- A severe test requires a system definite enough that no new assumption can be smuggled in. Any new assumption must be recognisable as a revision (p. 50).
- Popper believes this is why the *axiomatized* form is aimed at (Hilbert gave it to parts of physics). The axioms are the assumptions at the apex, and Popper notes that no claim to truth is implied by the word. All other statements are derived by purely logical or mathematical transformation (p. 50).
- **Four requirements** for an axiomatized system (pp. 50–51):
  - (a) The axioms are free from contradiction. This is equivalent to the demand that not every arbitrary statement is deducible.
  - (b) They are independent: no axiom is deducible from the others.
  - (c) They are sufficient for deducing all statements of the theory.
  - (d) They are necessary for that purpose: no superfluous assumptions.
- In such a system we can study the dependence of parts. This explains how falsifying a deduced statement may affect only part of the system. In physics, although theories are generally not completely axiomatized, the connections between parts may still be clear enough to decide which sub-systems a falsifying observation affects (p. 51).

### 17. Some possibilities of interpreting a system of axioms (pp. 51–54)
- Popper does not share the rationalist view that axioms are self-evident. He admits two interpretations: the axioms are (i) conventions or (ii) empirical or scientific hypotheses (pp. 51–52).
- **(i) Conventions** (p. 52):
  - The axioms fix the meaning of the primitive terms they introduce. They are sometimes called "implicit definitions".
  - *Analogy with equations.* A system of equations allows only certain value-combinations for its unknowns, even without a unique solution. A *statement-function* is a statement with blanks, such as $x + y = 12$ or: an isotope of the element $x$ has atomic weight 65. Substituting "copper" or "zinc" for $x$ gives a true statement.
  - A *statement-equation* results when we decide to admit only substitutions that make the statement-function true. It defines a class of admissible value-systems. $x + y = 12$ read this way is an ordinary equation (pp. 52–53).
  - Primitive terms can be regarded as blanks. An axiom system, if only value-combinations satisfying it are admitted, becomes a system of statement-equations and implicitly defines admissible systems of concepts. Any system satisfying the axioms is a *model* of them (p. 53).
  - Reading axioms this way means admitting only models as substitutes. The result is analytic (true by convention). Such a system is not an empirical hypothesis system, because it cannot be refuted by falsifying its consequences, which are also analytic (p. 53).
  - Footnote *2: Popper would now distinguish the objects satisfying the axioms (the model) from the names substituted for them, and call only the former a model (p. 53, n. *2).
- **(ii) Empirical hypotheses** (p. 53):
  - The usual view treats primitive terms as "extra-logical constants". For example, "straight line" and "point" become "light ray" and intersection of light rays, and the statements are then thought to become synthetic.
  - *Difficulty:* it is unclear what an empirical definition of a concept would be. Ostensive definition (pointing, labelling) fixes only individual names. The concepts of an axiom system should be universal names, which can be defined only explicitly by other universal names, or else left undefined (p. 54).
  - Some universal names must remain undefined. These undefined names can always be used in the non-empirical sense (i), as if implicitly defined, and Popper says such use must inevitably destroy the system's empirical character (p. 54).
  - *Popper's remedy:* he believes the difficulty can only be overcome by a methodological decision, namely the rule not to use undefined concepts as if they were implicitly defined (taken up again in section 20) (p. 54).
- Primitive concepts of one system, such as geometry, can often be correlated with concepts of another, such as physics. This matters when a more general system explains an older one, and its fundamental concepts may then be defined via concepts of the old systems (p. 54).

*Intuition note.* If the word point just means whatever satisfies these axioms, the axioms are true by decision and nothing could refute them. If it means a real light-ray intersection, the statements are meant as empirical hypotheses. Popper says that slipping from the empirical reading into the first one destroys the empirical character, so he adopts a rule against it.

### 18. Levels of universality. The modus tollens (pp. 54–56)
- Within a theoretical system, statements lie on levels of universality. Axioms are on the highest level and lower-level statements are deduced from them. Higher-level empirical statements are hypotheses relative to the lower-level statements deducible from them, and can be falsified by falsifying those (pp. 54–55).
- Lower-level universal statements are still strictly universal and so are also hypotheses. Popper says this is often overlooked (p. 55).
  - **Mach's case.** Mach calls Fourier's heat-conduction theory a "model theory" because it rests on "an observable fact" rather than a hypothesis. But the fact is stated as: the speed of levelling out of small temperature differences is proportional to the differences. This is an all-statement, plainly hypothetical (p. 55).
- Some singular statements are also hypothetical, since conclusions deduced from them (with a theory) may be falsified (p. 55).
- **Modus tollens** is the inference by which falsifying a conclusion falsifies the system it came from (p. 55).
  - Let $p$ be a conclusion of a system $t$ (theories plus initial conditions, not distinguished here). "$t \rightarrow p$" is read as: $p$ follows from $t$ (p. 55).
  - If $p$ is false ($\bar p$), we infer $\bar t$, and $t$ counts as falsified (p. 56). With "$\cdot$" for conjunction:
$$((t \rightarrow p)\cdot \bar p) \rightarrow \bar t$$
  In words: if $p$ is derivable from $t$ and $p$ is false, then $t$ is false (p. 56).
  - Footnote *1: when writing the book Popper confused a conditional statement with a statement of deducibility. He learnt the distinction from Tarski soon after publication and says the problem is "not very relevant" to the book's context (p. 55, n. *1).
- **Consequence.** The whole system required for deducing $p$, theory and initial conditions, is falsified. We cannot say of any one statement that it is, or is not, specifically upset. Only if $p$ is independent of some part of the system can we say that part is not involved (p. 56).
- **Possible attribution:** in some cases, perhaps by considering levels of universality, we can attribute the falsification to a definite hypothesis, such as a newly introduced one. This can happen when a well-corroborated theory has been deductively explained by a new higher-level hypothesis. If consequences of the new hypothesis fail, we may blame it alone, seek other high-level generalisations, and not regard the old, less general system as falsified (p. 56).
- Footnote 2: we cannot at first know which statements of the remaining sub-system to blame. Often the investigator's "scientific instinct" guides the choice. A decisive advance may come from modifying what seems obviously harmless, such as Einstein's modification of the concept of simultaneity (p. 56, n. 2).

*Intuition note.* A failed prediction shows that something in the whole package of laws and initial conditions is wrong. It does not say what. Logic alone does not tell you which part to drop, and independence of $p$ from some part, or higher-level structure, can narrow the blame.

## Toy example (ours, not from the text)
Law $L$: every rope of structure $S$ breaks under any load above 3 lb. (strictly universal; equivalent to saying that no $S$-rope survives a load above 3 lb).
- Initial conditions: $I_1$: this rope is of structure $S$; $I_2$: the load put on it is 5 lb. Since $5 > 3$, deduce $p$ = "this rope breaks". So $t = L \cdot I_1 \cdot I_2$ and $t \rightarrow p$.
- Observation: the rope holds, so $\bar p$. By modus tollens, $\bar t$: at least one of $L$, $I_1$, $I_2$ is false. The logic does not say which. Perhaps the load was really 2 lb., or the rope was a different structure.
- Contrast with numerical universality: the claim that all 4 people in this room are under 8 ft is settled by 4 height checks. $L$ can never be exhausted this way, because infinitely many possible $S$-ropes are unchecked. A single $S$-rope holding 5 lb., once $I_1$ and $I_2$ are secured, would refute $L$.

## Concepts
- [[deductive-nomological-explanation]] — causal explanation as deducing a singular statement from universal laws plus initial conditions (p. 38)
- [[initial-conditions]] (new) — singular statements describing the specific event; informally the "cause" (p. 38)
- [[principle-of-causality]] (new) — assertion that every event can be causally explained; tautological or, if synthetic, unfalsifiable, depending on how 'can' is read; Popper excludes it from science as metaphysical (p. 39)
- [[strictly-universal-statement]] (new) — "all-statement" about unlimited space and time; not replaceable by a finite conjunction of singular statements unless the world is bounded in time with finitely many instances (pp. 40–41)
- [[numerical-universality]] (new) — universality over a finite class in a finite region; counted among singular statements (p. 40)
- [[universal-vs-individual-concepts]] (new) — individual concepts need proper names in their definition; universal concepts do not (p. 43)
- [[strictly-existential-statement]] (new) — a claim that there is at least one … using only universal names; not falsifiable in isolation (p. 47)
- [[falsifiability]] — laws are non-existence statements, so one accepted singular counter-instance refutes them (p. 48)
- [[demarcation-problem]] — here the criterion produces the asymmetry (universals falsifiable only, existentials verifiable only) (pp. 48–50)
- [[axiomatized-system]] (new) — axioms that are consistent, independent, sufficient and necessary (pp. 50–51)
- [[implicit-definition]] (new) — axioms taken as conventions fixing the meaning of primitive terms; the result is analytic (p. 52)
- [[model-of-axioms]] (new) — a system of concepts satisfying a system of axioms (p. 53)
- [[analytic-synthetic-distinction]] — the principle of causality is analytic or synthetic depending on how 'can' is read; axioms-as-conventions yield analytic statements (pp. 39, 53)
- [[modus-tollens]] (new) — $((t \rightarrow p)\cdot\bar p)\rightarrow\bar t$; falsification passes to the whole premise-system (p. 56)
- [[instrumentalism]] (new) — theory as mere instrument of prediction; Popper rejects it (p. 37, n. *1)

## Canonical instances
- [[thread-breaking-example]] — causal explanation with law plus initial conditions (p. 38)
- [[oscillators-vs-human-height]] — strict versus numerical universality (pp. 40–41)
- [[lux-the-dog]] — individual concepts as classes related to universal classes (p. 44)
- [[ravens-black-and-white]] — universal versus existential statements and their negations (pp. 47–48)
- [[hafnium-and-bohr]] — an existential claim becomes testable through universal theory (pp. 48–49)
- [[mach-on-fourier-heat-theory]] — a lower-level universal statement is still a hypothesis (p. 55)

## Bridges (candidates)
- [structural-analogy] Axioms as implicit definitions ↔ mathematics: a system of equations restricts the admissible values of its unknowns. Popper makes this analogy himself (p. 52).
- [structural-analogy] Modus tollens falsifies the whole premise-system, not one statement ↔ philosophy of science: confirmation holism. Both say a failed prediction does not by itself assign blame (p. 56).
- [metaphor] Laws as prohibitions that rule out states of affairs ↔ law and rules: a rule forbids acts and is broken by a single violation (p. 48).
- [structural-analogy] Popper says the problem of universals is completely analogous to the problem of induction ↔ epistemology: going from singular to universal fails in both (p. 45).

## Questions this raises
- If a failed prediction falsifies the whole system, how do scientists decide which part to revise? Popper points to "scientific instinct" and levels of universality (p. 56).
- Is treating laws as strictly universal a mere convention (p. 42) or does it have deeper support?
- If isolated existential statements are metaphysical, how exactly does an existential statement inside a theory add empirical content (p. 49, n. *1)?
- Can the rule against using undefined concepts as implicitly defined (p. 54) always be applied in practice?

## Reading notes
- Printed page = pdf page − 29. Printed page numbers are used throughout.
- Footnotes with an asterisk (*1, *2, …) appear to be later comments by Popper, judging by their wording: a view Popper later described as instrumentalism (p. 37), his saying that today he would distinguish model and names (p. 53), and his admitting past confusion (p. 55). Note 4 on p. 46 itself contains a bracketed addition made in 1934 while the work was in proof. The footnote at the foot of p. 40 appears in the text layer with a bare asterisk.
- On p. 47, footnote 6, the text layer lost the Greek letter φ in the formulas. The image shows $(x)(x = N \to \phi x)$ and $(x)(\phi x \to fx)$.
- The chapter refers to section 6 (earlier) and to sections 20, 63–68, 75–78 and 85 (later). These are not in the unit, so the claims are reported as Popper's promises only.
- Popper's own footnote (p. 55, n. *1) says that, when writing the book, he was still confused about the difference between a conditional and a statement of deducibility; the note applies to this passage and two later ones (sections 35 and 36).
