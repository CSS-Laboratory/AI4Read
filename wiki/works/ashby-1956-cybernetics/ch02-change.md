---
id: ashby-1956-cybernetics/ch02-change
work: ashby-1956-cybernetics
unit: "1 What Is New (printed pp. 1–6) and 2 Change (printed pp. 9–23)"
pages: 1–23
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# What Is New; Change: transformations, closure, powers and kinematic graphs

## L0 — One line
Cybernetics studies what a system does (its possible behaviours), not what it is made of, and Ashby's first tool for this is the "transformation", a table saying what each state changes to, which can be closed, repeated, composed and drawn as a graph.

## L1 — The gist (≤ 120 words)
Chapter 1 says cybernetics studies ways of behaving, not material things. It asks for all the behaviours a machine could produce, not one single act. It promises one vocabulary for machines, brains and societies, and methods for complex systems. Chapter 2 starts the toolkit with "change". Ashby restricts himself to finite, discrete steps. A transformation says what each operand becomes. It can be closed or not, single-valued or not, one-one or many-one. Repeating it gives powers, found by algebraic elimination. Applying two different transformations in turn gives a product. A kinematic graph shows where each state ends up, in stopping points or cycles, and splits into basins.

**Prerequisites:** high-school algebra (substituting one equation into another); reading small tables; the idea of a function as a rule "input → output".

## L2 — Key ideas
- Cybernetics is "functional and behaviouristic": it asks "what does it do?", not "what is this thing?". It deals with regular, determinate, reproducible behaviour whatever the material (p. 1).
- Its subject is "all possible machines", much as geometry now treats forms far beyond those found on earth. It asks for the whole set of behaviours a machine could produce, not the single act here and now (pp. 2–3).
- Ashby names two virtues: one common vocabulary across very different systems, and a method for the scientific treatment of complex systems, some of which cannot be studied by varying one factor at a time (pp. 4–5).
- "Difference/change" is the most fundamental concept. Ashby assumes finite steps and finite differences, which loses nothing and lets questions be settled by counting (pp. 9–10).
- A transformation is a set of transitions (operand → transform: the thing acted on and what it becomes) on a set of operands. It is defined by what happens, not why (pp. 10–11).
- A transformation is closed on its operands if no transform falls outside the operand set. The test uses only the table, never the physical cause (p. 11). An unclosed transformation such as W cannot be applied twice (p. 18), and the repeated-application method is stated only for closed ones (p. 21).
- A transformation is single-valued if each operand has only one transform; a single-valued one is one-one if all its transforms differ, and many-one otherwise. The identity is a real transformation. Any transformation can be written as a "+"/0 matrix (pp. 14–16).
- Repeated change gives powers $T^2, T^3,\dots$. They are computed by eliminating intermediate primes (pp. 17–19). Applying two different transformations in order gives a product, and order matters (pp. 20–21).
- A kinematic graph draws an arrow from each state to the state it changes to; it makes it easy to follow a closed transformation from a single start state (pp. 21–22). In Ashby's p. 23 example, the moving ("representative") point always ends at a stopping state or in a cycle. The graph divides into basins, the separate regions where points end up, which Ashby says have some relation to "stability" (Chapter 5) (pp. 22–23).

## L3 — Walkthrough

### Chapter 1. What Is New

**1/1. Aim.** Ashby takes Wiener's definition: cybernetics is "the science of control and communication, in the animal and the machine". Ashby also calls it the art of steermanship. His themes will be co-ordination, regulation and control. Because the angle is new, a study of mechanism needs an introduction. Otherwise Chapter 2 may seem faulty, and mixing the old and new views causes confusion (p. 1).

**1/2. Peculiarities.** Cybernetics is a "theory of machines" but treats ways of behaving, not things. It does not ask "what is this thing?" but "what does it do?" It cares about "this variable is undergoing a simple harmonic oscillation", not whether the variable is a point on a wheel or an electric potential. It is "functional and behaviouristic". It began close to physics but "depends in no essential way" on the laws of physics or the properties of matter. It covers all behaviour in so far as it is regular, determinate or reproducible. Its truths are not conditional on another science, and it has its own foundations (p. 1).

**1/3–1/4. The domain of all possible machines.** Ashby's analogy:
- Cybernetics is to real machines (electronic, mechanical, neural, economic) as geometry is to real objects in terrestrial space (p. 2).
- Geometry once meant only what could be shown in ordinary space. Now it contains the terrestrial forms as special cases and gives a framework that increases power of control (p. 2).
- Cybernetics likewise takes "all possible machines" as its subject. It is only secondarily interested that some are not yet made (p. 2).
- It is therefore indifferent to the criticism that some machines it considers do not exist. Mathematical physics studies non-existent systems such as massless springs and perfect gases; the theory of the massless spring is invaluable to the physicist, even for understanding a watch (p. 2).
- A biologist studies Amphioxus in a similar way (p. 3).
- Cybernetics studies the possible relations between machine and machine first, and only afterwards the forms actually found in a particular science (p. 3).

**1/5. Sets of possibilities.** Cybernetics asks of any machine not "what individual act will it produce here and now?" but "what are all the possible behaviours that it can produce?" This is why information theory is essential: it always deals with a set of possibilities, and its primary data and final statements are almost always about the set as such (p. 3). Ashby's example is the ovum (p. 3):
- The older view asks why the ovum changes at all. It answered with energetics (fat oxidation, a Krebs' cycle) (p. 3).
- Cybernetics takes the free energy for granted. It asks why the changes lead to the rabbit-form and not a dog-form, fish-form or teratoma-form (p. 3).
- It considers a set of possibilities wider than the actual, then asks why the real case obeys its usual restriction. What matters is how far the system is subject to determining and controlling factors, and no signal or determining factor passes from part to part without being recorded as a significant event (pp. 3–4).
- Ashby therefore says cybernetics "might, in fact, be defined" as the study of systems open to energy but closed to information and control, "information-tight" (p. 4).

**1/6. First virtue: one vocabulary.** Cybernetics offers one set of concepts for the most diverse systems. Relating servo-mechanisms to the cerebellum was made harder because each was described in its own vocabulary (automatic pilot, radio set; dissecting room, bedside). Cybernetics gives exact correspondences with each branch. Ashby notes that linking two branches has repeatedly sped up both (calculus and astronomy, virus and protein molecule, chromosomes and heredity). Neither branch can prove laws for the other, but each can give suggestions. He expects cybernetics to reveal many parallelisms between machine, brain and society (p. 4).

**1/7. Second virtue: the complex system.** Cybernetics offers a method for the scientific treatment of complex systems (pp. 4–5).
- In simple systems its methods sometimes show no obvious advantage. They show their power when systems become complex (p. 5).
- Science has for two centuries explored systems that are simple or reducible to simple parts. The rule "vary the factors one at a time" was accepted for a century. Ashby says this shows that scientists studied systems that allowed that method (p. 5).
- Fisher's work in the 1920s on agricultural soils made it clear that some systems do not allow one-factor-at-a-time variation, because changing one factor changes others (p. 5).
- Some complex systems could not be evaded: the cerebral cortex, the ant-hill, the human economic system. Science can do little more than appreciate their complexity, but is taking first steps towards studying "complexity" in its own right (p. 5).
- Cybernetics is "prominent among" the methods for complexity. It drops vague intuitions drawn from simple machines (alarm clock, bicycle) and builds a rigorous discipline. The first chapters may seem to deal with truisms because the foundations are built broad and strong (p. 5).
- It hopes to mark out what is achievable, since, he says, probably many past investigations attempted the impossible. It then hopes to give general strategies. Part III offers only "a foundation" and "a start", not perfected methods (pp. 5–6).

*Intuition note.* Ashby wants a science of behaviour that does not depend on the material (p. 1). Because its subject is all possible machines, it is not troubled if some do not exist, just as mathematical physics still uses the massless spring (p. 2).

### Chapter 2. Change

**2/1. Difference and finite steps.** The most fundamental concept is "difference": two things are recognisably different, or one thing has changed with time. Any growth, ageing or movement implies a change from one state to another (p. 9).
- Ashby *chooses* to assume all changes occur by finite steps and all differences are finite, like a bank balance changing by at least a penny (p. 9).
- Reason: continuous change brings mathematical difficulties with infinitesimals, whereas for finite differences "all the important questions" can be decided by simple counting (p. 9).
- A discrete change can be carried over to the continuous by plotting separate points and imagining them becoming infinitely close (pp. 9–10).
- Nothing is lost. Settle the case for a given size of difference, then for smaller ones, until the trend is clear and the limit as the difference tends to zero can be stated. Ashby says this is the mathematician's own method for continuous change (p. 10).
- The topic is taken up again in S.3/3 (p. 10).

**2/2. Words.** Take pale skin turning dark in sunshine:
- The pale skin is the **operand** (what is acted on).
- The sunshine is the **operator** (the factor).
- The dark skin is the **transform** (what the operand changes to).
- The change $\text{pale skin} \to \text{dark skin}$ is the **transition**. It is specified by the two states and which changed to which (p. 10).

**2/3. Transformation.** A single transition is too simple. The operator may act on several operands and induce a transition in each. Ashby's examples for "exposure to sunshine" are cold soil → warm soil, unexposed photographic plate → exposed plate, and coloured pigment → bleached pigment. A set of transitions on a set of operands is a **transformation** (p. 10).

His second example is a letter code, Alpha: each letter goes to the next in the alphabet, Z to A, so CAT becomes DBU. The table is $A\to B,\ B\to C,\ \dots,\ Y\to Z,\ Z\to A$ (p. 11). Points made:
- The transformation is defined not by what the operator "really" is, nor by any physical cause, but by the set of operands and what each is changed to. It concerns "what happens", not "why it happens" (p. 11).
- Knowing the operator as a thing in itself is often not essential. One must know the transformation it effects (p. 11).
- The standard printed form puts operands in an upper row and transforms below, with a downward arrow at the left: $A\ B \dots Y\ Z$ over $B\ C \dots Z\ A$ (p. 11).

**2/4. Closure.** An operator acting on a set of operands may produce no element outside that set. Then the set of operands is **closed** under the transformation. In Alpha, every element of the lower line also occurs in the upper (p. 11).
- Closure is a relation between a transformation and a particular operand set. If either changes, closure may change (p. 11).
- The test uses only the details of the transformation, not its cause. So it can be applied even when the cause is unknown (p. 11).
- Exercises on p. 12 ask whether given tables are closed; for instance, Mr. D plays Mr. C, whose chess system defines a closed transformation from position to position (p. 12).

**2/5. Infinite operand sets.** A transformation may have infinitely many discrete operands, e.g. $1,2,3,4,\dots \to 4,5,6,7,\dots$. Ashby considers only the simple and clear cases here. It is closed or not according to whether one cannot, or can, find a nameable transform that is not among the operands. For this example, a transform such as 142857 is obviously among the operands, so it is closed (p. 12).

**2/6. Notation.** These are shorthand only; the transformation is still specified as in 2/3 (p. 13).
- "Operand → operand plus three" becomes $\text{Op.}\to\text{Op.}+3$, with the statement that the operands are 1, 2, 3, 4. Shorter still: $n \to n+3\ (n=1,2,3,4)$ (p. 13).
- $n$ can mean one particular operand (e.g. $2 \to 5$) or the whole transformation. Ashby says context shows which, and this causes no confusion in practice (p. 13).
- A prime marks the transform: $n \to n'$. So the transformation of Ex. 1 is $n' = n+10\ (n=1,2,3)$ (p. 14).

**2/7. Single-valued.** A transformation is single-valued if each operand goes to only one transform. $A,B,C,D \to B,A,A,D$ is single-valued. A table in which some operands have two possible transforms (for example $A \to B \text{ or } D$) is not. Other types are said to be important later (S.9/2, 12/8) (p. 14).

**2/8. One-one and many-one.** A single-valued transformation is **one-one** if all its transforms are different, so each transform indicates a unique operand. Example: $A\dots H \to F\,H\,K\,L\,G\,J\,E\,M$. It is one-one but not closed (K, L, J, M are not operands) (p. 14). A single-valued transformation that is not one-one is **many-one**. For example $1,2,3 \to 1,1,1$ is not one-one, because "1" does not indicate a unique operand (pp. 14–15).

**2/9. Identity.** The identical transformation, in which each transform equals its operand, is not a nullity. If the operands are all different, it is necessarily one-one. In condensed notation, $n' = n$ (p. 15).

**2/10. Matrix.** All these transformations can be shown in one schema (p. 15):
- Write operands in a horizontal row and possible transforms in a column at the left.
- Put "+" where the column's operand goes to the row's element, and 0 otherwise.
- The arrow at the top left shows the direction of transition.

Example: $A,B,C \to A,C,C$ gives rows A: $+\ 0\ 0$; B: $0\ 0\ 0$; C: $0\ +\ +$ (p. 15). Large matrices use dots. For $n' = n+2$ on the positive integers, the "+"s run along a diagonal that starts at row 3, column 1 (p. 16).

**2/11. Power.** A closed single-valued transformation can be applied repeatedly. This gives a series of changes analogous to those of an active dynamic system (pp. 16–17). Take Alpha twice: $A \to B \to C$, ..., $Y \to A$, $Z \to B$. This equals one application of $\begin{smallmatrix} A & B & \dots & Y & Z\\ C & D & \dots & A & B\end{smallmatrix}$ (p. 17).
- From each closed transformation $T$ we get another closed transformation, whose single effect equals $T$ applied twice. It is the "square" $T^2$, one of the "powers" of $T$ (p. 17).
- For now $T^2$ is just a convenient label (p. 17).

**2/12. Closure matters.** The unclosed transformation $W: f,g,h \to g,h,k$ cannot be applied twice. It changes $h$ to $k$, but its effect on $k$ is undefined. It is "like a machine that takes one step and then jams" (p. 18).

**2/13. Elimination.** For $T: n' = n+1$ on the positive integers (p. 18):
1. The second application gives $n'' = n' + 1$, and the first gives $n' = n+1$ (p. 18).
2. Eliminate $n'$ by substitution: $n'' = (n+1)+1$, i.e. $n'' = n+2$ (p. 18).
3. Rename the operand for uniformity: $m' = m+2$ is $T^2$ (p. 18).

The rule is general. For $n' = 2n - 3$, the second application gives $n'' = 2n' - 3$, so
$$n'' = 2(2n-3) - 3 = 4n - 9,$$
i.e. $m' = 4m - 9$ (pp. 18–19).

**2/14. Higher powers.** Add symbols $n''', \dots$ and eliminate intermediate ones. For three applications of $n' = 2n-3$ (p. 19):
$$n' = 2n-3,\quad n'' = 2n'-3,\quad n''' = 2n''-3.$$
Substituting for $n''$:
$$n''' = 2(2n'-3)-3 = 4n'-9.$$
Substituting for $n'$:
$$n''' = 4(2n-3)-9 = 8n-21.$$
So $T^3$ is $m' = 8m - 21$ (p. 19).

**2/15. Function notation.** The prime is convenient with one transformation. When several could act, $T(n)$ shows which one acted. $T(T(n))$ is written $T^2(n)$. The change is "only one of notation" (p. 20).

**2/16. Product.** After $T$, the transform $T(n)$ may be an operand for another transformation $U$, giving $U(T(n))$ (pp. 20–21). With
$$T: a,b,c,d \to b,d,a,b \qquad U: a,b,c,d \to d,c,d,b,$$
we get $T(b)=d$ and $U(T(b)) = U(d) = b$. Applying $T$ then $U$ to every operand gives
$$V: a,b,c,d \to c,b,d,c \quad (V = UT).$$
$V$ is the **product** or composition of $T$ and $U$ (p. 21).
- If $U$ is applied first, $U(b) = c$ and $T(c) = a$, so $T(U(b)) = a \ne U(T(b))$. The other order gives $W: a,b,c,d \to b,a,b,d$, written $W = TU$ (p. 21).
- "A change of the order in the product may change the transformation." The product may not exist if some of $T$'s transforms are not operands for $U$ (p. 21).
- Ex. 3 (starred) asks the reader to compare the matrix product with the matrix of $V$ (p. 21).

*Intuition note.* A power is a transformation applied to its own results, so it needs closure: every output must be a legal input. A product is the same idea with two different rules in a row, and order can matter (p. 21).

**2/17. Kinematic graph.** So far each transformation has been studied through a single action on all operands. A second method, applicable only if the transformation is closed, follows one operand through many repeated applications. This corresponds to setting a dynamic system at an initial state and letting it run, without interference, through the changes its inner nature determines (pp. 21–22).

Example $U: A,B,C,D,E \to D,A,E,D,D$ (p. 22):
- From C: C, E, D, D, D, … (D continues forever).
- From A: A, D, D, D, … (p. 22).
- **Kinematic graph:** write the operands anywhere and draw an arrow from A to B if and only if A goes to B in one step. For $U$ it is $C \to E \to D \leftarrow A \leftarrow B$. A re-entrant arrow on D is optional (p. 22).
- Different drawings with identical connexions count as the same graph ("buttons tied with string") (p. 22).
- A point moving along arrows is the **representative point**. Its path corresponds to $U(C), U^2(C),\dots$, and following arrows is often easier than computing (p. 22).

More complex example (p. 23):
$$T: A,B,C,D,E,F,G,H,I,J,K,L,M,N,P,Q \to D,H,D,I,Q,G,Q,H,A,E,E,N,B,A,N,E.$$
- By following arrows, the representative point always moves either to some state where it stops, or to a cycle around which it circulates indefinitely (p. 23).
- The graph is like a drainage map. The separate regions where a point ends up are the graph's **basins** (p. 23).
- Ashby says these matters "obviously have some relation to" stability, treated in Chapter 5 (p. 23).
- (added step: worked out from the table of $T$ above) The graph has three basins: one containing the cycle A→D→I→A, one ending at the stopping state H, and one containing the cycle E⇄Q.

*Intuition note.* The graph turns a table into a picture of the long-run behaviour of a system. Where you start decides which basin you are in, and the basin decides whether you stop or cycle.

## Toy example (ours, not from the text)
Operands $\{1,2,3,4,5\}$, transformation $R$: $1\to2,\ 2\to3,\ 3\to1,\ 4\to5,\ 5\to5$.
- **Closed?** Transforms are 2, 3, 1, 5, 5; all are in $\{1,\dots,5\}$, so yes.
- **Single-valued?** Yes. **One-one?** No: 5 is the transform of both 4 and 5, so it is many-one.
- **Square $R^2$** (apply $R$ twice): $1\to R(2)=3$; $2\to R(3)=1$; $3\to R(1)=2$; $4\to R(5)=5$; $5\to R(5)=5$. So $R^2: 1,2,3,4,5 \to 3,1,2,5,5$.
- **Kinematic graph:** $1\to2\to3\to1$ (a cycle), and $4\to5$ with 5 pointing at itself (a stopping state).
- **Basins:** $\{1,2,3\}$ and $\{4,5\}$. The representative point from 1 gives 1,2,3,1,2,3,…; from 4 it gives 4,5,5,5,…
- **Matrix** (rows = transforms, columns = operands; one "+" per column):

| | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | 0 | 0 | + | 0 | 0 |
| 2 | + | 0 | 0 | 0 | 0 |
| 3 | 0 | + | 0 | 0 | 0 |
| 4 | 0 | 0 | 0 | 0 | 0 |
| 5 | 0 | 0 | 0 | + | + |

Nothing here mentions what the operands are, only what happens, which is Ashby's point.

## Concepts
- [[cybernetics]] (new) — study of ways of behaving, regular and reproducible, whatever the material; "functional and behaviouristic" (p. 1)
- [[information-tight]] (new) — open to energy but closed to information and control (p. 4)
- [[state]] — here, a recognisable condition of the thing; change is a move from one state to another (p. 9)
- [[transformation]] (new) — set of transitions on a set of operands; defined by what each goes to, not why (p. 10)
- [[operand-operator-transform]] (new) — thing acted on, factor acting, result of the change (p. 10)
- [[transition]] (new) — a single change, e.g. pale skin → dark skin (p. 10)
- [[closure]] (new) — a transformation creates no element outside its operand set; tested from the table alone (p. 11)
- [[single-valued-transformation]] (new) — each operand has only one transform (p. 14)
- [[one-one-and-many-one]] (new) — one-one: all transforms differ; many-one: single-valued but not one-one (pp. 14–15)
- [[identity-transformation]] (new) — $n'=n$; no change (p. 15)
- [[matrix-of-transformation]] (new) — array with "+" where column operand goes to row transform, else 0 (p. 15)
- [[power-of-transformation]] (new) — $T^k$, one application with the effect of $k$ applications of $T$ (p. 17)
- [[elimination]] (new) — substituting between $n'', n', n$ to get a one-step rule for a power (p. 18)
- [[product-of-transformations]] (new) — $UT$: apply $T$, then $U$; order may matter (p. 21)
- [[kinematic-graph]] (new) — arrows $A\to B$ iff $A$ goes to $B$ in one step (p. 22)
- [[basin]] (new) — region of a kinematic graph where a point ends in the same stop or cycle (p. 23)
- [[stability]] — Ashby only says basins relate to it; Chapter 5 will treat it (p. 23)

## Canonical instances
- [[alpha-letter-shift-code]] — CAT → DBU; closed; its square shifts by two (pp. 11, 17)
- [[ovum-to-rabbit]] — cybernetics asks why rabbit-form and not dog- or fish-form, taking energy for granted (p. 3)
- [[massless-spring]] — non-existent systems still useful in mathematical physics (p. 2)
- [[vary-one-factor-at-a-time]] — method that fails for interconnected systems (Fisher, soils) (p. 5)
- [[kinematic-graph-sixteen-states]] — T on A…Q, with stops and cycles (p. 23)

## Bridges (candidates)
- [same-math] repeated application $T^k$ of a closed transformation ↔ dynamical systems: a discrete-time state map iterated from an initial state — both are the same iterated function.
- [same-math] kinematic graph, stopping states and cycles ↔ functional graphs of maps on finite sets: same objects (fixed points, cycles, basins).
- [structural-analogy] "+"/0 matrix of a transformation ↔ state-space/Markov transition matrix: one entry per operand column is a deterministic special case.
- [structural-analogy] basins of a kinematic graph ↔ control-theory stability: Ashby only says they are "related" (Chapter 5).
- [structural-analogy] "the set of all possible behaviours" ↔ variety/information theory: Ashby links the set viewpoint with information theory (p. 3).

## Questions this raises
- If a system is not closed on its operands, what do we do with the extra states, so that the system can still be studied (p. 18)?
- How does a kinematic graph relate to stability and equilibrium (promised for Chapter 5, p. 23)?
- What are the non-single-valued transformations of S.9/2 and 12/8 used for (p. 14)?
- How does the "set of possibilities" view connect with information theory and with the "information-tight" definition (pp. 3–4)?

## Exercises worth doing
- Ex. 2/4/5 (p. 12) — Mr. C's closed chess system: does closure make D's offer wise? Tests what closure does and does not promise — difficulty: medium
- Ex. 2/14/7 (p. 19) — find double applications by elimination — difficulty: medium
- Ex. 2/14 Ex. 9 (p. 19) — repeated $n'=1/(1+n)$, linked to the Fibonacci series — difficulty: hard
- Ex. 2/16 Ex. 3 (p. 21, starred) — matrix product of $T$ and $U$ versus the matrix of $V$ — difficulty: hard
- Ex. 2/17 Ex. 9 (p. 23) — can one basin of a single-valued transformation contain two cycles? — difficulty: medium
- Ex. 2/17 Ex. 6–7 (p. 23) — arrows into one point, one-one versus many-one — difficulty: easy

## Reading notes
- The PDF has two printed pages per image (scanned spreads). Text-layer labels say `printed="?"`, but page numbers are visible in the images. Mapping: pdf 5 = p. 1; pdf 6 = pp. 2–3; pdf 7 = pp. 4–5; pdf 8 = p. 6 (plus the Part One title page); pdf 9 = p. 9; pdf 10 = pp. 10–11; pdf 11 = pp. 12–13; pdf 12 = pp. 14–15; pdf 13 = pp. 16–17; pdf 14 = pp. 18–19; pdf 15 = pp. 20–21; pdf 16 = pp. 22–23. The offset is not constant. The Part One title page shares an image with p. 6, and no page number 7 or 8 is printed in the images. No image of p. 9 was provided (the text is from the layer).
- This unit covers Chapter 1 ("What Is New") and Chapter 2 ("Change"), plus the Part One title (motto from Herrick: properties are "names for its behavior").
- The two-column text layer interleaves columns, so I assigned text to printed pages by the images. The p. 17 Ex. 1 table prints "c c a'" with a prime that the page does not explain. A p. 21 passage prints "T(b,)", evidently a misprint for $T(b)$. Another passage on p. 12 prints "slack" for "black".
- The "three basins" statement for the p. 23 graph is my own reading, worked out from the table of $T$ and marked as an added step.
- The text names "Sir Donald Fisher" (p. 5); I give it as printed.
- Exercises are listed, not solved.
