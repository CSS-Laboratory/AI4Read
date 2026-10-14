---
id: jaynes-2003-probability/ch01-plausible
work: jaynes-2003-probability
unit: "1 Plausible reasoning"
pages: 3-23
fields: [information-theory, bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# Plausible reasoning

## L0 — One line
Where deduction cannot settle a question, we need an extension of logic that assigns degrees of plausibility, and Jaynes proposes to derive its rules from a few desiderata imposed on an idealized reasoning robot.

## L1 — The gist (≤ 120 words)
Jaynes asks how to reason when information is incomplete and deduction fails. Everyday and scientific reasoning use weak syllogisms: confirming a consequence of A makes A more plausible. He proposes to design an idealized "robot" that reasons about two-valued propositions. He reviews Boolean algebra (AND, OR, NOT, implication; NAND, i.e. not-AND, alone suffices). He then states three desiderata (requirements, not axioms): plausibilities are real numbers, they agree qualitatively with common sense, and the reasoning is consistent. He announces, without proving it here, that these determine the rules uniquely (derived in Chapter 2). He also warns against confusing implication with causation, and epistemological (about perception) with ontological (about existence) statements (the "mind projection fallacy").

**Prerequisites:** propositional logic (AND, OR, NOT, truth tables); the idea of a real-valued degree of belief.

## L2 — Key ideas
- Deduction uses two strong syllogisms (1.1)–(1.2). Most real reasoning uses weaker patterns (1.3)–(1.5), which move plausibility up or down without proving anything (pp. 4–5).
- The theory of plausible reasoning built on weak syllogisms is an extension of logic, not a weakened logic. Syllogisms (1.3) and (1.4) apply just where "A implies B" says nothing: when A is false or B is true (p. 12).
- Logical implication is not physical causation. Formal "A ⇒ B" is also not "B is deducible from A" (pp. 5, 12).
- Three connectives (AND, OR, NOT) generate all $2^{2^n}$ logic functions of $n$ propositions; AND with NOT suffices; NAND alone, or NOR alone, suffices (pp. 13–16).
- The robot is an idealized, normative design, not a model of human psychology. Its rules are fixed by desiderata, not by assumed truths (pp. 8–9, 16).
- Desiderata: (I) plausibilities are real numbers, (II) qualitative agreement with common sense, (IIIa–c) consistency. Jaynes states they uniquely determine the rules (pp. 17–19).
- Plausibility judgments are one-dimensional in the robot. A human mind may have many "coordinates" for a proposition, and Jaynes does not claim that human plausibilities have a unique numerical measure (pp. 19–20).
- Epistemological statements (those that express only the speaker's perception, such as saying that a room is noisy) must not be read as ontological ones. Jaynes calls this error the mind projection fallacy (p. 22).

## L3 — Walkthrough

**Opening (p. 3).** A policeman sees a masked man crawl out of a broken jeweller's window with a bag of jewels. He concludes the man is dishonest. The text asks by what reasoning process (p. 3).

### 1.1 Deductive and plausible reasoning (pp. 3–6)
- The policeman's conclusion is not a deduction, since an innocent explanation is possible (the owner, in a mask, protecting his shop). It is still highly plausible (p. 3).
- Aristotle's deductive reasoning reduces to two **strong syllogisms** (p. 4):
$$\frac{\text{if } A \text{ then } B;\ A \text{ true}}{B \text{ true}} \tag{1.1}$$
$$\frac{\text{if } A \text{ then } B;\ B \text{ false}}{A \text{ false}} \tag{1.2}$$
- Weaker syllogisms (epagoge) apply when we lack such information (pp. 4–5):
$$\frac{\text{if } A \text{ then } B;\ B \text{ true}}{A \text{ becomes more plausible}} \tag{1.3}$$
$$\frac{\text{if } A \text{ then } B;\ A \text{ false}}{B \text{ becomes less plausible}} \tag{1.4}$$
- Jaynes says the reasoning by which a scientist accepts or rejects theories consists almost entirely of syllogisms "of the second and third kind" (p. 5).
- Example for (1.3): A = rain starts by 10 am at the latest, B = the sky becomes cloudy before 10 am. Clouds at 9:45 do not make rain certain; if they are dark enough, common sense may still lead us to change plans (p. 4).
- The major premise "if A then B" expresses *logical* consequence, not causal. Rain is not the physical cause of the earlier clouds, yet (rain ⇒ clouds) is certain (pp. 4–5).
- Simon and Rescher (as cited): all attempts to read implication as physical causation fail for lack of contraposition, i.e. (1.2). Jaynes says Chapter 3 will show that causal readings of plausible inference fare no better (p. 5).
- The policeman uses a still weaker pattern (p. 5):
$$\frac{\text{if } A \text{ then } B \text{ becomes more plausible};\ B \text{ true}}{A \text{ becomes more plausible}} \tag{1.5}$$
- Despite its abstract weakness, in this case it is nearly as convincing as deduction (p. 5).
- The brain also evaluates *degrees* of plausibility and uses prior information. Jaynes's thought experiment: if events like these happened several times every night to every policeman and always turned out innocent, policemen would soon learn to ignore them (pp. 5–6).
- Deductive chains keep the certainty of their premises. With (1.3)–(1.5) reliability changes along a chain. In quantitative form, Jaynes says, conclusions can in many cases still approach deductive certainty (p. 6).
- Pólya (as cited) found qualitative rules of plausible reasoning. He showed that even pure mathematicians mostly use the weak forms when discovering theorems; Jaynes will make these rules quantitative (p. 6).

*Intuition note.* Deduction says what must follow. Plausible reasoning says which way our confidence should move, and (later) by how much. The "how much" is what the book will supply (p. 8).

### 1.2 Analogies with physical theories (pp. 6–7)
Like physics, the study proceeds by idealized models that reproduce a few features of common sense. The most familiar things may be the hardest to model. Jaynes expects any successful model to be a powerful extension of common sense in some field, as advances in physics bring practical benefits of an unpredictable kind (p. 7).

### 1.3 The thinking computer (pp. 7–8)
- **von Neumann's reply** (as quoted): tell me precisely what a machine cannot do, and I can build a machine that does it (p. 7).
- Jaynes's gloss: in principle, the only operations a machine cannot perform for us are those we cannot describe in detail or that could not be completed in finitely many steps. Each time we construct a model that reproduces part of common sense by prescribing definite operations, this shows how to write a program that does plausible reasoning with quantitative versions of the weak syllogisms (pp. 7–8).
- Motivating task: 10 000 observations, 100 hypotheses, find their relative plausibilities. What decides whether (1.5) raises A's plausibility almost to certainty or only negligibly? The book aims to answer this (p. 8).
- The topic is *normative* principles of logic, not psychology or neurophysiology (p. 8).

### 1.4 Introducing the robot (pp. 8–9)
- The robot's rules will be deduced from simple desiderata; Jaynes thinks a rational person who found they were violating one would wish to revise their thinking. If you resemble the robot, trusting it is an accomplishment of the theory, not a premise (p. 9).
- The robot reasons about propositions $A, B, C,\dots$ that are unambiguous and strictly true or false (two-valued, Aristotelian). Their truth need not be ascertainable (p. 9).
- Example: the statement that Beethoven and Berlioz never met is permissible; the vague claim that Beethoven's music has better sustained quality than Berlioz's is not, at present. Chapter 18 is cited for relaxing this (p. 9).

### 1.5 Boolean algebra (pp. 9–12)
- **Conjunction** $AB$: both true. **Disjunction** $A+B$: at least one true. These are shorthand for propositions, not numbers (p. 10).
- *Same truth value* means each is true iff the other is. Such propositions are logically equivalent. **Primitive axiom of plausible reasoning:** propositions with the same truth value are equally plausible (p. 10). Boole himself erred here in 1854 and revised his theory in 1857 (p. 10).
- "=" in Boolean algebra means equal truth value; "≡" means "equals by definition". Without parentheses, $AB+C$ means $(AB)+C$ (p. 10).
- Denial: $\overline{A}\equiv$ "A is false" (1.8); $A=$ "$\overline{A}$ is false" (1.9) (pp. 10–11).
- (1.10) $\overline{AB}$ = "$AB$ is false". (1.11) $\overline{A}\,\overline{B}$ = "both $A$ and $B$ are false". These differ: $\overline{AB}=\overline{A}+\overline{B}$ (p. 11).
- Basic identities (1.12) (p. 11):
  - Idempotence: $AA=A$, $A+A=A$.
  - Commutativity: $AB=BA$, $A+B=B+A$.
  - Associativity: $A(BC)=(AB)C=ABC$, $A+(B+C)=(A+B)+C=A+B+C$.
  - Distributivity: $A(B+C)=AB+AC$, $A+(BC)=(A+B)(A+C)$.
  - Duality: if $C=AB$ then $\overline{C}=\overline{A}+\overline{B}$; if $D=A+B$ then $\overline{D}=\overline{A}\,\overline{B}$.
- A theorem used later (1.13): if $\overline{B}=AD$ then $A\overline{B}=\overline{B}$ and $B\overline{A}=\overline{A}$ (p. 11).
- **Implication** $A\Rightarrow B$ (1.14) asserts neither $A$ nor $B$. It means $A\overline{B}$ is false, equivalently $(\overline{A}+B)$ is true, equivalently $A=AB$. This is what (1.1) and (1.2) state (p. 11).
- If $A$ is false, or $B$ is true, (1.14) says nothing about the other proposition. Those are exactly the cases where (1.3) and (1.4) speak. So plausible reasoning is an *extension* of logic with new content, not a weakened logic. Jaynes says the next chapter, (2.69) and (2.70), will show that the rules contain deduction as a special case (p. 12).
- **A tricky point (p. 12).** Ordinary language reads "A implies B" as "B is deducible from A". Formal logic means only that $A$ and $AB$ have the same truth value; deducibility depends on all propositions we accept. The truth table for implication (as given by Devinatz and Hamilton) makes $A\Rightarrow B$ false only when $A$ is true and $B$ false. Jaynes's justification:
  - If $A$ and $B$ are both true, then $A=AB$, so every true statement implies every other true statement.
  - If $A$ is false, $AQ$ is false for any $Q$, so $A=AB$ and $A=A\overline{B}$ both hold. A false proposition "implies" every proposition.
  - Read as deducibility, this would make every false proposition self-contradictory. "Beethoven outlived Berlioz" is false but not contradictory.

*Intuition note.* Formal implication says only that the combination of A true with B false is excluded; it does not say that B can be derived from A. Because it excludes just that one combination, it says nothing when A is false or when B is true, which are the cases where (1.3) and (1.4) speak (pp. 11–12).

### 1.6 Adequate sets of operations (pp. 12–16)
- Four connectives so far: $AB$, $A+B$, $A\Rightarrow B$, $\overline{A}$. They can build propositions such as (p. 13)
$$C\equiv (A+\overline{B})(\overline{A}+A\overline{B})+\overline{A}B(A+B). \tag{1.15}$$
  Jaynes says this equals the implication $C=(B\Rightarrow\overline{A})$ and leaves the check to the reader (p. 13). (added step) Check: $(A+\overline{B})(\overline{A}+A\overline{B})=A\overline{B}+\overline{A}\,\overline{B}=\overline{B}$ and $\overline{A}B(A+B)=\overline{A}B$, so $C=\overline{B}+\overline{A}B=\overline{A}+\overline{B}$.
- Aim: find the smallest set of operations that generates all logic functions. Equations like (1.15) are meant to hold for every way of defining $A, B$: a variable statement rather than a statement variable (p. 13).
- Counting: for $n=2$ the "space" has $2^2=4$ points {TT, TF, FT, FF}, so there are $2^4=16$ logic functions. For $n$ propositions, $M=2^n$ points and exactly $2^M$ functions (p. 13).
- $n=1$: four functions, listed by truth table, equal (p. 14)
$$f_1=A+\overline{A},\quad f_2=A,\quad f_3=\overline{A},\quad f_4=A\overline{A}. \tag{1.16}$$
  So conjunction, disjunction and negation generate all functions of one proposition (p. 14).
- For $n=2$, the functions true at exactly one point are the four basic conjunctions (p. 14):
$$AB,\quad A\overline{B},\quad \overline{A}B,\quad \overline{A}\,\overline{B}. \tag{1.17}$$
- Any function true on some points is the logical sum of the basic conjunctions true there. Jaynes calls this nontrivial and asks the reader to verify it. Examples (p. 15), with $f_5$ true at TF, FF and $f_6$ true at TT, FT, FF:
$$f_5=A\overline{B}+\overline{A}\,\overline{B}=(A+\overline{A})\overline{B}=\overline{B}, \tag{1.18}$$
$$f_6=AB+\overline{A}B+\overline{A}\,\overline{B}=B+\overline{A}\,\overline{B}=\overline{A}+B. \tag{1.19}$$
  So $f_6=(A\Rightarrow B)$ (p. 15).
- There are $2^4-1=15$ functions true somewhere. The remaining one is the contradiction $A\overline{A}$ (p. 15).
- This "disjunctive normal form" works for any $n$. For $n=5$ there are $2^5=32$ basic conjunctions and $2^{32}=4\,294\,967\,296$ functions. All but the contradiction, (1.21), are sums of basic conjunctions (1.20) (p. 15).
- Hence {AND, OR, NOT} is an **adequate set** (1.22) (p. 15).
- Duality gives $A+B=\overline{\overline{A}\,\overline{B}}$ (1.23), so {AND, NOT} is already adequate. Neither can be dropped alone: AND cannot be reduced to negations, and negation cannot be got from ANDs (pp. 15–16).
- **NAND** and **NOR** (p. 16):
$$A\uparrow B\equiv\overline{AB}=\overline{A}+\overline{B}, \tag{1.24}$$
$$\overline{A}=A\uparrow A,\quad AB=(A\uparrow B)\uparrow(A\uparrow B),\quad A+B=(A\uparrow A)\uparrow(B\uparrow B). \tag{1.25}$$
$$A\downarrow B\equiv\overline{A+B}=\overline{A}\,\overline{B}, \tag{1.26}$$
$$\overline{A}=A\downarrow A,\quad A+B=(A\downarrow B)\downarrow(A\downarrow B),\quad AB=(A\downarrow A)\downarrow(B\downarrow B). \tag{1.27}$$
  Each alone generates every logic function. Jaynes notes one can exploit this in designing computer and logic circuits: a NAND gate outputs "up" iff at least one input is "down" (p. 16).

*Intuition note.* A logic function is just a choice of true/false for each of the $2^n$ input combinations. Listing the true combinations as OR-ed ANDs shows that three operations suffice. Jaynes says the fact that {AND, NOT} suffice will be essential later for judging whether a set of rules for plausible reasoning is adequate (pp. 14–15).

### 1.7 The basic desiderata (pp. 16–19)
- They are called *desiderata*, not axioms, because they claim no truth but state desirable goals. Whether they can be met without contradiction and determine a unique extension is settled in Chapter 2 (pp. 16–17).
- **(I)** Degrees of plausibility are represented by real numbers (1.28). It is practically forced by the need to store them physically. Appendix A is cited for a theoretical requirement. Greater plausibility ↔ greater number is a nonessential convention. A continuity property is also assumed (p. 17).
- Notation: $A|B$ is the conditional plausibility that $A$ is true given that $B$ is true, or just "$A$ given $B$" (1.29). Examples: $A|BC$ (1.30), $A+B|CD$ (1.31), $(A|B)>(C|B)$ (1.32), also written $A|B>C|B$ (1.33) (pp. 17–18).
- $A|BC$ is undefined when $B, C$ are contradictory (p. 18).
- **(II)** Qualitative correspondence with common sense (1.38). Direction only, no amounts. If old information $C$ is updated to $C'$ so that
$$(A|C')>(A|C) \tag{1.34}$$
  while
$$(B|AC')=(B|AC), \tag{1.35}$$
  then
$$(AB|C')\ge(AB|C), \tag{1.36}$$
$$(\overline{A}|C')<(\overline{A}|C). \tag{1.37}$$
  Continuity also requires that an infinitesimal change in $A|C$ induce only infinitesimal changes in $AB|C$ and $\overline{A}|C$ (p. 18).
- **(III) Consistency** (p. 19):
  - (IIIa) if a conclusion can be reasoned in more than one way, every way must give the same result (1.39a);
  - (IIIb) the robot uses all relevant evidence and does not ignore some of it, so it is "completely nonideological" (1.39b);
  - (IIIc) equivalent states of knowledge give equivalent plausibility assignments, apart from labels (1.39c).
- (I), (II), (IIIa) are *structural* requirements. (IIIb), (IIIc) are *interface* conditions with the outer world (p. 19).
- Jaynes states that these conditions uniquely determine the robot's reasoning rules. They are deduced in Chapter 2 (p. 19).

*Intuition note.* Nothing in this chapter says how plausibilities are computed; the desiderata are requirements that any acceptable method must meet. Jaynes states that they fix the rules uniquely; that claim is announced here and proved in Chapter 2, not here (p. 19).

### 1.8 Comments (pp. 19–23)
- By (I), the robot's state of mind about a proposition is one number. Humans also judge desirability, importance and so on, which would need a vector. Jaynes does not claim human plausibilities have a unique numerical measure. The question is whether a consistent one-dimensional model can be built (pp. 19–20).
- Objection: why not a comparative theory with only orderings like $(A|C)>(B|C)$? Jaynes defers to Appendix A. Comparative attempts did not turn out simpler or more general, and the final results are said not to differ (p. 20).

**1.8.1 Common language vs. formal logic (pp. 21–22).**
- Ordinary language carries nuances that formal logic loses. Mr A says he believes what he sees; Mr B retorts that he doesn't see what he doesn't believe. Formally these look equivalent, but the intent and effect are opposite (p. 21).
- Textbook example: the statement that the projection of the limit is the limit of the projections was held true, and its reverse was held not true in general. Ordinary "A is B" presupposes that A exists (p. 21).
- "Knowledge is power" vs. "power is knowledge" (p. 21).
- "Is" has two meanings: "The room is noisy" (epistemological: the speaker's perception) vs. "There is noise in the room" (ontological: existence). English disguises epistemological statements as ontological ones (pp. 21–22).
- Treating the first kind as ontological is the **mind projection fallacy**: it asserts that private thoughts and sensations are external realities. Jaynes says it is a major source of error in current probability theory (p. 22).
- The robot reads statements literally, like a small child (p. 22).
- Jaynes says today's nontrivial probability computations are done by computers, so each program is part of a robot's brain. Most programs are intuitive ad hoc procedures that do not satisfy the desiderata. Ch. 2's proofs are said to show that any adhockery conflicting with probability rules must produce demonstrable inconsistencies beyond a restricted area (p. 22).

**1.8.2 Nitpicking (p. 23).**
- "Boolean algebra" here means two-valued logic of propositions. Quantifiers are only abbreviations for "for all" and "there is a" (p. 23).
- On the second strong syllogism's validity: counterexamples, contradictions and reductio ad absurdum are still accepted in mathematics. Jaynes's stance: logic may move forward but a new logic that conflicted with Aristotelian logic where it applies would be fatally flawed (p. 23).
- Multiple-valued logics: Appendix A is cited for arguments which, Jaynes says, suggest that an $n$-valued logic is either equivalent to a two-valued logic on an enlarged set of propositions or contains inconsistencies. Jaynes says that supposed difficulties he knows of (quantum theory, fuzzy sets, AI) have proved to be mind projection fallacy (p. 23).

## Toy example (ours; not from the text)
Take the four worlds for $(A,B)$: TT, TF, FT, FF. The premise $A\Rightarrow B$ means $A\overline{B}$ is false, so it removes TF (p. 11). Remaining: TT, FT, FF.
- **(1.1):** $A$ true leaves only TT, so $B$ is true.
- **(1.2):** $B$ false leaves only FF, so $A$ is false.
- **(1.3):** $B$ true leaves TT, FT, so logic says nothing about $A$. Illustration only, assuming equal weight per remaining world (our assumption, not Jaynes's rule): $A$ is true in 1 of 3 worlds beforehand, i.e. $1/3$, and in 1 of 2 after $B$ is learned, i.e. $1/2$. So $A$ becomes more plausible.
- **(1.4):** $A$ false leaves FT, FF. Under the same weighting, $B$ is true in 2 of 3 worlds beforehand, i.e. $2/3$, and in 1 of 2 afterwards, i.e. $1/2$. So $B$ becomes less plausible.

The strong syllogisms need one world; the weak ones start where logic leaves several worlds open.

## Concepts
- [[probability-as-extended-logic]] — plausible reasoning as an extension of deductive logic by weak syllogisms; Jaynes states that the rules follow from the desiderata (pp. 12, 19)
- [[weak-syllogism]] (new) — patterns (1.3)–(1.5) that move plausibility up/down without proving anything (pp. 4–5)
- [[strong-syllogism]] (new) — the two strong syllogisms (1.1) and (1.2) (p. 4)
- [[boolean-algebra]] (new) — algebra of two-valued propositions, with "=" meaning same truth value (p. 10)
- [[material-implication]] (new) — $A\Rightarrow B$ means $A\overline{B}$ is false; not deducibility, not causation (pp. 11–12)
- [[adequate-set-of-operations]] (new) — set of connectives generating all logic functions; {AND, OR, NOT}, {AND, NOT}, {NAND}, {NOR} (pp. 15–16)
- [[plausibility-notation]] (new) — $A|B$: real-valued plausibility of $A$ given $B$ (p. 17)
- [[desiderata-of-plausible-reasoning]] (new) — (I) real numbers, (II) qualitative common sense, (IIIa–c) consistency (pp. 17–19)
- [[reasoning-robot]] (new) — idealized reasoner defined by its rules; normative, not psychological (pp. 8–9)
- [[mind-projection-fallacy]] (new) — reading epistemological statements as ontological (p. 22)

## Canonical instances
- [[policeman-and-jewellery-store]] (new) — a weak syllogism of type (1.5) is strongly convincing given prior experience (pp. 3, 5–6)
- [[rain-and-clouds]] (new) — illustrates (1.3) and the logical vs. causal direction (pp. 4–5)
- [[nand-universality]] (new) — one operation, via (1.24)–(1.25), generates all logic functions (p. 16)
- [[disjunctive-normal-form]] (new) — functions as sums of basic conjunctions; $2^{2^n}$ functions (pp. 13–15)

## Bridges (candidates)
- [structural-analogy] Weak syllogism (1.3) ↔ bayesian: Bayes' theorem — evidence consistent with a hypothesis raises its posterior (canon link; not stated in this unit)
- [structural-analogy] Desideratum (IIIc), equivalent knowledge gives equal plausibilities ↔ bayesian: principle of indifference/maximum entropy
- [same-math] NAND/NOR universality ↔ digital logic design: all Boolean functions built from one gate type (p. 16)
- [metaphor] Mind projection fallacy ↔ bayesian: probability as a state of knowledge rather than a property of the world (canon link; not stated in this unit)

## Questions this raises
- Why do real-valued plausibilities, qualitative common sense and consistency force one unique rule set (Chapter 2)?
- What determines how much (1.5) raises $A$'s plausibility: "large, almost certainty" vs. "negligible" (p. 8)?
- How can vague propositions, such as a judgment that one composer's music is better than another's, be admitted (Chapter 18)?
- Does a comparative-only theory really lead to the same results (Appendix A, p. 20)?

## Exercises worth doing
The unit has no numbered exercises. It has informal "left to the reader" tasks:
- Verify $C$ in (1.15) equals $(B\Rightarrow\overline{A})$ (p. 13) — builds Boolean-algebra skill — medium.
- Verify that the sum-of-conjunctions construction yields $f_5$, $f_6$ and the 15 functions true somewhere (p. 15) — easy.
- Footnote 4: does it follow that AND and NOT are the only commands needed to write any computer program? (p. 15) — thought question; no answer is given in the unit — medium.

## Reading notes
- Page offset: printed = pdf − 30 (pdf 33 = printed 3). Both labels were given.
- The text layer drops all overbars and primes (e.g. in 1.10, 1.11, 1.13, 1.15–1.19, 1.24–1.27, 1.34–1.37). I rewrote these from the page images.
- (1.15): the text layer drops the bars. In the image the last factor is $(A+B)$ with no bar. With that reading the expansion gives $\overline{A}+\overline{B}$, which matches $B\Rightarrow\overline{A}$ as stated on p. 13 (see the added check in 1.6).
- Appendix A, Chapters 2, 3, 4 and 18 are cited but are not in this unit. Claims about them are Jaynes's announcements only.
- Epigraph by Maxwell (1850) and the Banach and von Neumann remarks are quoted by the author (pp. 3, 6, 7).
