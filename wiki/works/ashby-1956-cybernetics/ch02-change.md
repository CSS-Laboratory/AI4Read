---
id: ashby-1956-cybernetics/ch02-change
work: ashby-1956-cybernetics
unit: "Chapters 1 (What Is New) and 2 (Change)"
pages: 1-23
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 21
pipeline_version: 0.1
---
# What Is New, and Change: cybernetics as the study of possible behaviours, and "transformation" as its basic tool

## L0 — One line
Cybernetics studies the possible behaviours of any machine, whatever it is made of, and its first tool is "change" made exact as a transformation: a table saying what each state becomes.

## L1 — The gist (≤ 120 words)
Chapter 1 asks what is new in cybernetics. Ashby answers that it studies ways of behaving, not things. It treats each machine as one of "all possible machines", and it offers one vocabulary and a method for complex systems. Chapter 2 makes "change" precise. A transformation lists operands (the things acted on) and what each becomes. Ashby defines closure, single-valued, one-one and many-one transformations, the identity, matrix form, repeated application (powers by algebraic elimination), products, and the kinematic graph, which shows where a state ends up. Ashby says the graph's separate regions have some relation to stability, which he takes up in Chapter 5.

**Prerequisites:** school algebra (substituting one equation into another); the idea of a function or table mapping inputs to outputs; reading simple arrow diagrams.

## L2 — Key ideas (5–10 bullets)
- Cybernetics asks what a thing does, not what it is. It deals with behaviour so far as it is regular, determinate or reproducible, and in no essential way depends on the laws of physics or the properties of matter (p. 1).
- Its subject is the domain of all possible machines, just as modern geometry contains the terrestrial forms as special cases. Typically, a machine is asked for its set of possible behaviours, not one act here and now (pp. 2–3).
- Its two claimed virtues are a single vocabulary for very different systems, and a method for complex systems. The older rule of varying one factor at a time is often impossible for complex systems, and the new methods show their power chiefly there (pp. 4–5).
- Ashby assumes change happens in finite steps. The parts have names: the operand (the thing acted on), the operator (the acting factor), the transform (the result) and the transition (operand → transform). A transformation is a set of transitions, defined by what happens, not why (pp. 9–11).
- A set of operands is closed under a transformation if the transforms contain no element outside it. Closure can be tested from the details of the transformation, without knowing its cause (p. 11).
- Transformations can be classed: single-valued (one transform per operand), one-one (also all transforms different), many-one (single-valued but not one-one), and the identity (nothing changes). They can be written as lists, as rules like $n \to n+3$, or as matrices of + and 0 (pp. 13–16).
- Repeated change gives powers; a power is found by eliminating intermediate symbols. The order of a product may change the result, and an unclosed transformation cannot be applied twice: it takes one step and then jams (pp. 16–21).
- The kinematic graph draws an arrow from each state to its one-step transform. In Ashby's example, following the arrows from any state leads to a stopping point or a cycle. The separate regions are called basins, and Ashby says these matters have some relation to stability (pp. 22–23).

## L3 — Walkthrough

### Chapter 1. What Is New

**1/1 Definition and aim (p. 1).** Ashby quotes Wiener: cybernetics is "the science of control and communication, in the animal and the machine". He restates this as the art of steermanship. The book's themes are co-ordination, regulation and control. He says a study of mechanism is required, but from a new, unusual angle, so some introduction is advisable. Unconscious vacillation between the old and new viewpoints is apt to lead to confusion.

**1/2 Peculiarities (p. 1).** Many books called "Theory of Machines" describe levers and cogs. Cybernetics treats ways of behaving, not things. It asks what a thing does, not what it is. It cares that a variable undergoes simple harmonic oscillation, and cares little whether the variable is a point on a wheel or a potential in a circuit. He calls it essentially functional and behaviouristic. It began closely associated with physics but depends in no essential way on the laws of physics or the properties of matter. It deals with all forms of behaviour so far as they are regular, determinate or reproducible. Materiality is irrelevant, and its truths are not conditional on another science. It has its own foundations.

**1/3 The geometry analogy (p. 2).** Once "geometry" meant what could be shown in ordinary space, and forms not demonstrable there were suspect. Now geometry exists in its own right and contains terrestrial forms as special cases. For geometry, the gain is a framework in which all forms find a place with their relations visible, and, with better understanding, a correspondingly increased power of control. Cybernetics stands to real machines (electronic, mechanical, neural, economic) as geometry stands to real objects. Its subject is "all possible machines". It is only secondarily interested if informed that some have not yet been made, by Man or by Nature. It offers the framework on which individual machines may be ordered, related and understood.

**1/4 Indifference to non-existent machines (pp. 2–3).** Mathematical physics studies non-existent systems (massless springs, perfect gases), and the massless-spring theory is invaluable even for understanding a watch (p. 2). The biologist's detailed study of *Amphioxus* or an extinct form, out of proportion to its present importance, uses the same principle (p. 3). Cybernetics picks out types of mechanism important to general theory, regardless of whether terrestrial machines make them common. Only after surveying the possible relations between machine and machine adequately does it turn to the forms found in a particular science (p. 3).

**1/5 Sets of possibilities (p. 3).** Cybernetics typically treats a given machine by asking "what are all the possible behaviours that it can produce?" rather than what individual act it will produce here and now. So information theory plays an essential part, because it always deals with a set of possibilities. The older view asked why an ovum grows into a rabbit and not just stays an ovum, and answered through energetics (oxidising fat, a Krebs cycle). Cybernetics takes for granted that the ovum has abundant free energy and is so delicately poised metabolically that it is, in a sense, explosive. It asks why the changes go to rabbit-form and not dog-form, fish-form or teratoma-form. It envisages a set of possibilities much wider than the actual, and asks why the actual case obeys its usual restriction. Energy plays almost no part, and whether the system is closed or open to energy is often irrelevant. What matters is how far the system is subject to determining and controlling factors. No signal or determining factor passes between parts without being recorded as a significant event. Ashby says cybernetics might, in fact, be defined as the study of systems open to energy but closed to information and control, that is, "information-tight" (pp. 3–4).

*Intuition note.* Cybernetics does not ask how a thing is built or powered. It lists everything a system could do and asks what limits it to what it does do. This fits Ashby's claim that very different systems, such as a servo-mechanism and a cerebellum, can be described in one vocabulary (p. 4).

**1/6 First virtue: one vocabulary (p. 4).** Ashby confines the review of applications to those promising most in the biological sciences, and says it can only be brief and very general. The first virtue is a single vocabulary and set of concepts for very different systems. Servo-mechanisms and the cerebellum were described in words that made relating them unnecessarily difficult (automatic pilot, radio set versus dissecting room, bedside). Concepts with exact correspondences to each branch of science can bring branches into exact relation. When two branches are found to be related, each often helps the other develop, often with markedly accelerated growth. Ashby gives the infinitesimal calculus and astronomy, the virus and the protein molecule, and the chromosomes and heredity. Neither branch can give proofs about the other's laws, but each can give suggestions. Cybernetics is "likely to reveal" many parallelisms between machine, brain and society.

**1/7 Second virtue: the complex system (pp. 4–6).** The second virtue is a method for the scientific treatment of systems where complexity is outstanding and too important to ignore, as it is in biology. In simple systems the methods sometimes show no obvious advantage. They reveal their power chiefly when systems become complex (p. 5).

- Science has for two centuries explored systems that are simple or reducible to simple parts. The dogma of varying the factors one at a time, accepted for a century, suited such systems; Ashby says the method is often fundamentally impossible in complex ones. Fisher's 1920s work on agricultural soils (printed "Sir Donald Fisher") made clear that some systems do not allow one factor to be varied alone. They are so dynamic and interconnected that changing one factor evokes changes in others (p. 5).
- Some complexity could not be evaded: the cerebral cortex, the ant-hill as a society, the human economic system. The scientist can do little more than appreciate the complexity. Science is now taking first steps towards studying "complexity" as a subject (p. 5).
- Cybernetics is prominent among such methods. It rejects vague intuitions from simple machines such as the alarm clock and bicycle and builds a rigorous discipline. The first chapters may seem to treat truisms, but only because the foundations are built broad and strong (p. 5).
- It offers *hope* of effective methods for studying and controlling very complex systems. It would do this first by marking out what is achievable, since probably many past investigations attempted the impossible. It would then give generalised strategies of demonstrable value. Part III does not pretend to offer such methods perfected; it attempts to offer a foundation and a start (p. 6).

**Part One, "Mechanism".** The epigraph (Herrick) reads: "The properties commonly ascribed to any object are, in last analysis, names for its behavior." (p. 6)

### Chapter 2. Change

**2/1 Why finite steps (pp. 9–10).** The most fundamental concept in cybernetics is "difference": two things recognisably different, or one thing changed with time. Changes may be continuous, such as the earth moving or skin darkening. Ashby avoids infinitesimals and assumes changes occur in finite steps with finite differences, like a bank balance changing by at least a penny (p. 9).

- With finite differences, the important questions can be decided "by simple counting" (p. 9).
- Continuous cases need comparing infinitesimals or summing infinitely many, which is hard (p. 9).
- A discrete case can often be carried to the continuous by graphing the separate points (pp. 9–10).
- Ashby holds that nothing is lost. Establish the result for one size of difference, then a smaller one, and so on until the trend shows, then take the limit as the difference tends to zero. Ashby says this is the mathematician's own method for being sure about continuous change. He concludes that the finite case can always be converted to the continuous form if that is desired (p. 10).

**2/2 Words (p. 10).** In "pale skin → dark skin under sunshine", the thing acted on (pale skin) is the **operand**, the acting factor (sunshine) is the **operator**, and the result (dark skin) is the **transform**. The change is the **transition**, specified by the two states and which changed to which.

**2/3 Transformation (pp. 10–11).** A single transition is too simple. The operator may act on several operands, each with a characteristic transition. "Exposure to sunshine" gives cold soil → warm soil, unexposed plate → exposed plate, coloured pigment → bleached pigment (p. 10). A set of transitions on a set of operands is a **transformation**. Another example is the coding that replaces each letter by the next one, Z becoming A, so CAT becomes DBU. It is defined by the table A→B, B→C, …, Y→Z, Z→A (p. 11).

- A transformation is defined by giving the operands and what each is changed to, not by what it "really" is or by a physical cause. It concerns what happens, not why. Knowledge of the operator as a thing in itself is often not essential; one must know how it acts on the operands (p. 11).
- Standard printed form: operands in an upper line, transforms in a lower line, with an arrow ↓ at the left:

  ↓ A B … Y Z
  &nbsp;&nbsp;&nbsp;B C … Z A

**2/4 Closure (p. 11).** If the transforms contain no element absent from the operands, the set of operands is **closed** under the transformation. Closure relates a transformation to a particular set of operands, and altering either may alter closure. The test uses the details of the transformation, not its cause, so it works even when the cause is unknown. The letter-shift above is closed, because every element of the lower line is in the upper. Exercises 1–5 follow (p. 12), including Mr. C's chess system and its closed position-to-position transformation.

**2/5 Infinite operands (p. 12).** For a transformation with infinitely many discrete operands, such as 1 2 3 4 … → 4 5 6 7 …, the set is closed if one cannot find some particular, namable transform that is not among the operands, and not closed if one can. For 142857 and every other transform, the operand list contains it, so this transformation is closed. Ashby says infinite sets can cause difficulties, so he considers only simple and clear cases here.

**2/6 Notation (pp. 13–14).** Abbreviations are only shorthand and imply nothing more than the last few sections already stated. The rule "Operand → operand plus three" becomes Op. → Op. + 3, then $n \to n+3\ (n=1,2,3,4)$. The letter n can mean one particular operand (n = 2 changes to 5) or, with no value given, the whole transformation. Ashby says context will always show which is meant (p. 13). A prime marks the transform: $n \to n'$, so a transformation can be written $n' = n + 10\ (n=1,2,3)$ (p. 14).

**2/7 Single-valued (p. 14).** A transformation is **single-valued** if it converts each operand to only one transform. ↓ A B C D / B A A D is single-valued. One where A goes to "B or D" is not. Other types are said to matter later (S.9/2, 12/8).

**2/8 One-one and many-one (pp. 14–15).** A single-valued transformation is **one-one** if all its transforms are different, so each transform points back to a unique operand. Example: A B C D E F G H → F H K L G J E M, which is one-one but not closed. A single-valued transformation that is not one-one is **many-one** (p. 15).

**2/9 Identity (p. 15).** The **identical transformation** has no change: each transform equals its operand, $n' = n$. It is apt to be dismissed as a nullity but is important. If its operands are all different it is necessarily one-one.

**2/10 Matrix (pp. 15–16).** Operands are written along a horizontal row. Possible transforms are written in a column at the left. Put "+" where the column's operand is transformed to the row's element, and 0 otherwise. The arrow at top left shows the direction. For ↓ A B C / A C C, the matrix is:

| ↓ | A | B | C |
|---|---|---|---|
| A | + | 0 | 0 |
| B | 0 | 0 | 0 |
| C | 0 | + | + |

Every transformation can be shown this way, and dots may be used for large cases. For $n' = n+2$ on the positive integers, the first + in column 1 is at row 3, then column 2 at row 4, and so on (p. 16). Exercises 1–7 follow (p. 16).

**2/11 Power (pp. 16–17).** A closed single-valued transformation can be applied repeatedly, like a dynamic system going through successive changes. Take the letter-shift (call it Alpha) applied twice. A→B→C, so A→C; B→D; Y→A; Z→B. Two applications of Alpha equal one application of ↓ A B … Y Z / C D … A B. This is a closed transformation, called the **square** of the first, one of its **powers**. If the first is T, the square is labelled $T^2$ (p. 17).

**2/12 Why closure matters (p. 18).** An unclosed transformation, such as W: ↓ f g h / g h k, cannot be applied twice. It changes h to k, but k's transform is undefined. Ashby compares it to a machine that takes one step and then jams.

**2/13 Elimination (p. 18).** To find $T^2$ for $T: n' = n+1$ without rewriting every operand, write the second step as $n'' = n'+1$ and eliminate $n'$:

$$n'' = (n+1)+1 = n+2.$$

Renamed for uniformity, this is $m' = m+2$. One application of it equals two applications of T. The rule is general. For $n' = 2n-3$ the second step is $n'' = 2n'-3$:

$$n'' = 2(2n-3)-3 = 4n-9,$$

so $T^2$ is $m' = 4m-9$.

**2/14 Higher powers (p. 19).** For three applications of $n' = 2n-3$, write the step equations $n'=2n-3$, $n''=2n'-3$, $n'''=2n''-3$. Substituting for $n''$ gives

$$n''' = 2(2n'-3)-3 = 4n'-9.$$

Substituting for $n'$ gives

$$n''' = 4(2n-3)-9 = 8n-21.$$

So $T^3$ is $m' = 8m-21$. Exercises 1–12 follow, including the Fibonacci-linked $n' = 1/(1+n)$ (pp. 19–20).

*Intuition note.* Applying a rule twice is itself a rule, and algebra finds it by substituting the first step into the second. Closure guarantees the output can be fed back in.

**2/15 Notation $T(n)$ (p. 20).** When several transformations might act, a prime does not say which. So $T(n)$ denotes the transform of n under T. $T(T(n))$ is written $T^2(n)$, and $n''$ corresponds to $T^2(n)$. This is only a change of notation.

**2/16 Product (p. 21).** Let T: a b c d → b d a b and U: a b c d → d c d b. The transform T(b) = d (the text prints "T(b,)"), and U(T(b)) = U(d) = b. Applying T then U defines a new transformation, the **product** or **composition**, written UT:

V = UT: a b c d → c b d c.

Applying U first gives W = TU: a b c d → b a b d. Since T(U(b)) = a but U(T(b)) = b, changing the order of a product may change the transformation. V may not exist if some of T's transforms are not operands of U.

**2/17 Kinematic graph (pp. 21–23).** Another way to study a closed transformation is to apply it repeatedly to one operand. This corresponds to setting a dynamic system at an initial state and letting it run on, without interference (p. 21). Examples are numbers dialled in a telephone system, or an ants' colony given a piece of meat (p. 22).

Take U: ↓ A B C D E / D A E D D. Starting at C gives the series C, E, D, D, D, … Starting at A gives A, D, D, D, … The **kinematic graph** has the operands as points, with an arrow from A to B if and only if A is transformed to B in one step. For U it is C → E → D ← A ← B. A self-loop at D is optional (p. 22).

- The graph can be redrawn in other shapes (as buttons tied with string) and is the same graph if the internal connexions are identical (p. 22).
- A point that moves along arrows (the **representative point**) follows the series $U(C), U^2(C), \dots$. This is often easier than computing, especially for complicated transformations (p. 22).
- For a 16-element T (A B C D E F G H I J K L M N P Q → D H D I Q G Q H A E E N B A N E), the graph shows several separate groups of states (p. 23).
- Starting anywhere and following the arrows, the representative point always moves either to a state where it stops, or to a cycle it circulates in indefinitely (p. 23).
- Ashby compares the graph to a map of a country's water drainage. The separate regions are the **basins**. He says these matters obviously have some relation to what is meant by stability, which he takes up in Chapter 5 (p. 23).

Exercises 1–9 follow (p. 23).

*Intuition note.* The graph shows at a glance where each state ends up. This long-run fate, a stopping state or a cycle, is the kind of question regulation and stability will ask later.

## Toy example (ours, not from the text)
Operands {1, 2, 3, 4}; transformation S: ↓ 1 2 3 4 / 2 4 4 1.

- **Closed?** Transforms are 2, 4, 4, 1, all in {1, 2, 3, 4}. Yes.
- **Type:** single-valued. Not one-one, since 2 → 4 and 3 → 4 give the transform 4 twice, so it is many-one.
- **Matrix** (columns = operands 1–4, rows = transforms). Each column has one + because S is single-valued (added step).

| ↓ | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | + |
| 2 | + | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 | 0 |
| 4 | 0 | + | + | 0 |

- **Square:** 1 → S(2) = 4; 2 → S(4) = 1; 3 → S(4) = 1; 4 → S(1) = 2. So $S^2$: ↓ 1 2 3 4 / 4 1 1 2.
- **Kinematic graph:** 1 → 2 → 4 → 1, plus 3 → 4. Start at 3: 3, 4, 1, 2, 4, 1, 2, … After one step the point enters the cycle 1 → 2 → 4 → 1 and never leaves. There is one basin.
- **Elimination check:** for $n' = 3n+1$, $n'' = 3n'+1 = 3(3n+1)+1 = 9n+4$. At n = 1: n' = 4, n'' = 13, and 9·1 + 4 = 13. ✓

## Concepts
- [[transformation]] (new) — a set of transitions on a set of operands, defined by what each becomes, not why (p. 10)
- [[operand-operator-transform]] (new) — the thing acted on, the acting factor, and the result (p. 10)
- [[closure]] (new) — set of operands is closed if no transform lies outside it; tested from the transformation alone (p. 11)
- [[single-valued-one-one-many-one]] (new) — each operand has one transform; additionally all transforms distinct; or not (pp. 14–15)
- [[identity-transformation]] (new) — each transform equals its operand, n' = n (p. 15)
- [[transformation-matrix]] (new) — grid of + and 0 showing which operand goes to which transform (p. 15)
- [[power-and-product-of-transformations]] (new) — repeated application $T^k$, found by elimination; product UT is T then U, and order may matter (pp. 17–21)
- [[kinematic-graph]] (new) — arrows from each state to its one-step transform; shows long-run fates (p. 22)
- [[basin]] (new) — a separate region of the graph; the graph is compared to a drainage map showing where a point starting at any place ends up (p. 23)
- [[state]] — used informally here as one of the two ends of a transition; no formal state concept yet (p. 10)
- [[stability]] — only pointed to; the graph is said to "have some relation" to it, with a full treatment promised for Chapter 5 (p. 23)
- [[black box]] — the idea that one can know a transformation without knowing the cause of change; this id is the nearest canon link, and the text does not use the term (p. 11)

## Canonical instances
- [[alphabet-shift-code]] — the letter-to-next-letter transformation: closed, with its square (pp. 11, 17)
- [[sunshine-transformations]] — pale skin, cold soil and photographic plate under one operator (p. 10)
- [[ovum-to-rabbit]] — cybernetic versus energetic questions about growth (p. 3)
- [[massless-spring-and-geometry]] — non-existent or merely possible systems still give the framework (pp. 2–3)
- [[fisher-soil-experiments]] — a complex system that does not allow one factor to be varied alone (p. 5)
- [[kinematic-graph-U-and-T]] — worked graphs with a stopping state, cycles and several basins (pp. 22–23)

## Bridges (candidates)
- [structural-analogy] Repeated transformation and trajectory on the kinematic graph ↔ control-theory: state evolution of a discrete-time system, with the initial state set and then left to run without input (the text calls the correspondence "analogous").
- [same-math] Kinematic graph of a single-valued transformation ↔ graph theory: the directed graph of a function on a finite set, where each point has one outgoing arrow.
- [structural-analogy] Matrix of + and 0 with composition by row-into-column multiplication (Ex. 2/16/3) ↔ Markov-chain transition matrices: the same layout, but 0/+ entries rather than probabilities.
- [structural-analogy] Basin and cycle ↔ stability: a region that drains to one equilibrium or oscillation is an early picture of what stability analysis will test.

## Questions this raises
- Ashby says using finite differences loses nothing. For which questions does finite counting truly give the same answers as the continuous limit?
- If the graph of a single-valued transformation always ends in a stop or cycle (p. 23), what extra condition does this need? (Closure is needed to apply the transformation repeatedly.)
- How would "not single-valued" transformations (S.9/2, 12/8) change closure and the graph?
- What does "information-tight" (p. 4) mean once regulation is formalised with these tools?

## Exercises worth doing
- Ex. 2/4/5 (p. 12) — chess system as a closed transformation; tests what closure does and does not tell you — difficulty: medium
- Ex. 2/10/6–7 (p. 16) — counting possible matrices for two operands, and how many are single-valued — difficulty: easy
- Ex. 2/14/7 (p. 19) — elimination for double applications of three different rules — difficulty: medium
- Ex. 2/16/3 (p. 21) — tests whether matrix multiplication matches composition — difficulty: hard
- Ex. 2/17/6–7 (p. 23) — can two arrows meet in one point for one-one and many-one transformations — difficulty: easy
- Ex. 2/17/9 (p. 23) — can a basin contain two cycles — difficulty: medium

## Reading notes
- **Scope:** This unit combines Chapter 1 ("What Is New", pp. 1–6) and Chapter 2 ("Change", pp. 9–23). Page 6 holds the end of Ch. 1 and the Part One title page with the Herrick epigraph. The spread labelled 8-9 shows only the Chapter 2 opening text, ending with the number 9; no printed page 7 appears.
- **Page labels:** Pages are given as two-page spreads (e.g. "2-3"). Citations use the printed number of the half where the text appears. Printed numbers are continuous from pdf 5 = p. 1, but spreads share one pdf number, so there is no fixed offset.
- **Text-layer problems:** The text layer joins spread columns and corrupts words ("arm", "he", "In full", "t e" for "the"). I used the images.
- **Misprints seen in the images:**
  - p. 18: the text says n" must be "I more than n""; the "I" is a misprint for 1, and the second n" should be n'.
  - p. 21: "T(b,)" should be T(b).
  - p. 12: "slack" for Black in the chess exercise.
  - p. 5: "Sir Donald Fisher" is as printed.
- **Kinematic graph (p. 23), unresolved:** By the table, T sends D → I and I → A, and A → D. In the printed drawing, the two short arrows under A and D both point down toward I, but the table gives I → A, so the drawing appears not to match the table at that point. The L3 claims about the graph rely only on the author's statement and the group structure.
- **Exercises:** Exercise solutions are not printed in this unit. None are given here.
