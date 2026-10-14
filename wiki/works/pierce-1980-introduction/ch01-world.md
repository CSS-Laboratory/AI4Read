---
id: pierce-1980-introduction/ch01-world
work: pierce-1980-introduction
unit: "1 The World and Theories"
pages: 1-18
fields: [information-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The World and Theories

## L0 — One line
A scientific theory does not explain every use of a word like "communication"; it picks out the aspects of experience that can be related, and communication theory is a strongly mathematical, quite general theory whose important results are stated as proved theorems.

## L1 — The gist (≤ 120 words)
Pierce asks what kind of thing a "theory of communication" can be. His answer, by analogy with Aristotle's "motion" and Newton's laws, is that a theory covers only the aspects of experience that can be usefully related. Theories differ in generality and in being physical or mathematical. Communication theory is highly mathematical and general, and it measures information in bits. Its results are theorems: statements shown to follow from assumptions. Two hex theorems and two theorems about mapping a square onto a line illustrate theorem and proof. The chapter prepares the reader for a theory whose mathematics matters but whose proofs will not be given in full.

**Prerequisites:** high-school arithmetic; decimal digits; the idea of a proof by contradiction.

## L2 — Key ideas (5–10 bullets)
- Words like "communication" and "motion" are broad in everyday use; a scientific theory should not be expected to answer every question phrased with them (pp. 3–4, 18).
- A theory consists of assumptions plus the mathematical working-out of their consequences; it is valid only if those consequences fit the phenomena (p. 4).
- Theories cannot simply be ranked by generality: network theory (the theory of circuits of idealized electrical parts) is less general than Maxwell's equations (the laws of electricity and magnetism) in one sense and more general in another (pp. 5–6).
- Theories lie on a scale from strongly physical (Newton, Maxwell) toward the mathematical end (network theory, arithmetic) (pp. 6–8).
- Communication theory is strongly mathematical and general. It offers the bit as a universal measure of choice or uncertainty, and tells how fast information can be sent and how to encode it (p. 8).
- A theorem is a statement proved to follow from assumptions and definitions; the key results of information theory are theorems (pp. 9–10, 18).
- Two proof styles appear: the hex Theorem II (first player can win) has a non-constructive proof, which does not show how to win; the square-onto-line mapping has a constructive proof, which gives an explicit recipe (pp. 13–15).
- Any one-to-one mapping of a square onto a line (each point of one paired with exactly one point of the other) must be discontinuous: moving smoothly through the square, the matching line points jump around (p. 16). Pierce says both mapping theorems matter later in communication theory (pp. 16–17).

## L3 — Walkthrough

### Opening: communication as a popular idea (pp. 1–2)
- Shannon published "A Mathematical Theory of Communication" in 1948 (book form 1949). Twelve years later the field is accepted, with books, symposia, a professional group and journals (p. 1).
- **Ayer's observation:** we communicate not only information but knowledge, error, opinions, orders, emotions, even heat, motion, strength, disease (p. 1).
- Pierce notes the temptation: a "mathematical" theory sounds as if a few formulae could solve our communication problems. "Unhappily, this is not the course of science." (p. 2)

### Aristotle, Newton, and the meaning of words (pp. 2–4)
- Aristotle discussed motion in the *Physics*. His concept covered increase and decrease, coming to and passing away, and being built. He found as many types of motion as there are meanings of "is" (p. 2).
- Motion stayed puzzling for over two millennia until Newton. Newton's four laws (three laws of motion plus universal gravitation) are stated on pp. 2–3. They remain a living part of physics, though later physics shows them to be special forms of more general laws for small velocities and large scales (p. 2).
- Newton's laws solved the problem of motion *as Newton defined it*. They do little for many of Aristotle's questions (p. 3).
- Language cannot have a word for every object or event, so one word covers many things ("run": horses, motors, stockings, banks). The unity lies in human language more than in physical similarity. It would be foolish to seek one theory of running, of all Aristotle's motions, or of all sorts of communication and information (p. 3).
- Science does not study words; it looks for things in nature that can be grouped and understood. It often borrows everyday words but gives them a narrow, often new meaning. Newton's terms cannot treat "force of circumstance" or "mass media" (pp. 3–4).
- A valid theory seldom if ever answers our pressing questions as we phrase them. It tells us in a fresh way which aspects of experience can be related and simply understood (p. 4).

**Intuition note.** One everyday word can hide many different things. A theory works on the part that holds together, and leaves the rest of the word alone.

### What a theory is; generality (pp. 4–6)
- A theory = assumptions (as axioms are the basis of geometry) plus the mathematical working-out of the logical consequences. Consequences must agree with the world, otherwise the theory is invalid and useless (p. 4).
- Generality is the range of phenomena a theory applies to. Newton's laws explain planets, pendulums and machines but not radio waves (pp. 4–5).
- Maxwell's equations explain all (non-quantum) electrical phenomena, including radio waves. Network theory treats circuits made of idealized resistors, inductors and capacitors, so it is less general than Maxwell's equations in that sense (p. 5).
- In another sense network theory is more general. Its mathematical results also hold for idealized mechanical systems: spring ↔ capacitor, mass ↔ inductor, dashpot ↔ resistor. That it grew out of electrical systems is "a matter of history, not of necessity" (p. 6). Maxwell's equations do not apply to mechanical systems (p. 6).
- Pierce's partial explanation: some theories are strongly physical (Newton, Maxwell); network theory is essentially mathematical, with terms that can take various physical meanings. A mathematical theory is often an offshoot of physical theories (potential theory is another example), though some seem more mathematical from the start (p. 6).

**Intuition note.** "More general" has two senses: covering more of one physical domain, or applying to more physical domains through shared mathematics. A theory can win in one sense and lose in the other.

### Mathematical theories: arithmetic and cautions (pp. 7–8)
- Arithmetic is a mathematical theory applied to collections. If 16 numbers label a group, it can be split into two groups of 8 or arranged in a $4\times4$ square. There are $2{,}092{,}278{,}988{,}800$ possible orderings (as printed; see Reading notes), matching the orderings of the integers 1 to 16. With 13 objects (13 is prime) the group cannot be divided into equal heaps (p. 7).
- Arithmetic fits nature only to the degree that the properties of numbers match the physical world. Physicists say elementary particles such as electrons are indistinguishable, so one can talk of their total number but not assign particular numbers to particular particles (p. 7).
- Euclidean geometry serves surveyors and navigators, but there is reason to believe it is not quite accurate for astronomical phenomena (p. 7).
- Classification: theories vary in scope and in how physical or mathematical they are. Newton's laws are strongly physical; network theory is more abstract; arithmetic is very abstract (pp. 7–8).

### Where communication theory sits (pp. 8–9)
- Communication theory is "both very strongly mathematical and quite general". It grew out of electrical communication but treats problems abstractly (p. 8).
- It provides the **bit**, a universal measure of information in terms of choice or uncertainty. Specifying or learning a choice between two equally probable alternatives is one bit (p. 8).
- It tells how many bits per second can be sent over perfect and imperfect channels, how to measure the rate at which a source generates information, how to encode messages efficiently for a channel, and when errors can be avoided (p. 8).
- Because it is abstract, it can be hard to apply to a particular practical problem, but it has a broad field of application: language, electrical and mechanical message transmission, the behavior of machines, and "perhaps" people. **Some feel** it matters for physics, discussed much later (pp. 8–9).
- It remains a mathematical theory, not a physical, psychological or engineering one (p. 9).

### Theorems and proofs (pp. 9–10)
- Pierce says equations will appear in the book; they state accurately ideas also given in words, and an appendix on notation is provided (p. 9).
- Pierce says the common picture of mathematics (multiplication, square roots) is misleading because it stresses notation and tricks of manipulation; theorems and proofs are of primary importance to mathematicians (p. 9).
- Mathematicians begin with assumptions and definitions and show by proof that theorems are true. Shannon did this. A theorem's truth depends on the validity of the assumptions and of the proof (pp. 9–10).
- Pierce will not take the reader through the hard proofs of communication theory. He gives simpler theorems as examples, aiming at content, meaning and importance (p. 10).

### Example 1: hex (pp. 10–14)
- **Setup:** a board of 49 hexagonal cells. Black tries to connect the left and right black areas; white tries to connect the top and bottom white areas. Players alternate, one marker per play (p. 10).
- **Theorem I: either one player or the other wins** (no draws). Needed first, for a fully filled board (p. 11).
- **Proof of Theorem I** (p. 11–13):
  1. Assume every cell is filled. Start at corner I (left end of the upper white border) and trace the boundary between black and white, always with black on the right and white on the left (p. 11).
  2. At each vertex there are two possible configurations (Fig. 1-3): two black hexagons on the right and one white on the left, or two white on the left and one black on the right. In both, a continuous black path lies to the right and a continuous white path to the left. The boundary cannot cross or join itself, since only one path through the vertex has black on the right and white on the left (p. 12).
  3. So white hexagons on the left connect to the upper white border, and black hexagons on the right connect to the left black border (p. 12).
  4. The boundary cannot circle forever. It can always be extended at a border except at corners II and III, so it ends at II or III (p. 12).
  5. If it ends at II, the black hexagons connected to the left border are also connected to the right border, and black has won. White cannot also have won, because the black band from left to right blocks any white band to the bottom. If it ends at III, white has won by a similar argument (pp. 12–13).
- **Theorem II: the player with the first move can win.** "Can" means there exists a recipe (a first move plus a correct reply to any opponent move) that wins whatever the opponent does, if only the player were wise enough to know it (p. 13).
- **Proof of Theorem II** (by contradiction, p. 13):
  1. Either the first player has a sure winning way, or the second player must be able to answer every first-player play so as to win.
  2. Assume the second player has a sure recipe. Let the first player move anywhere, then follow that hypothetical recipe as if he were second.
  3. If the recipe calls for a hexagon he already occupies, he plays any unoccupied space instead. The extra piece may block an opponent from a hexagon, but not himself.
  4. So he can occupy the hexagons the recipe designates and must win. That contradicts the assumption, so the assumption is false, and the first player can win.
- A purist would not call these proofs rigorous. The proof of Theorem II is **not constructive**: it does not show the first player how to win (p. 13).

**Intuition note.** Theorem II says a winning strategy exists without saying what it is. The proof shows only that the opposite assumption leads to contradiction.

### Why prove theorems? (p. 14)
- Theorems are inherent in the statement of the problem and its rules, for hex and for Euclid's postulates. With enough insight we might see them at once; the young Newton is said to have found Euclid obvious. Ordinarily mathematicians may suspect or conjecture a result but have to prove theorems in order to be certain; they proceed step by step and also need proofs to convince others. A theorem may also seem contrary to common sense, as in the next example (p. 14).

### Example 2: square onto line (pp. 14–17)
- **Setup:** a unit square, with point $P$ given by $x$ (distance from the left side) and $y$ (height above the base), both less than one. A **one-to-one mapping** pairs every square point with exactly one line point and vice versa (p. 14).
- **Theorem: a unit square can be mapped onto a unit line one-to-one** (p. 15).
- **Constructive proof:** take the digits of $y$ as the 1st, 3rd, 5th, … digits of $x'$, and the digits of $x$ as the 2nd, 4th, 6th, … digits. Then $x'$ is the distance of $P'$ from the left end of the line. Changing $x$ or $y$ changes $x'$, and changing $x'$ changes $x$ and $y$ (p. 15).
- **Author's example:**
$$x = 0.547000\ldots,\quad y = 0.312000\ldots,\quad x' = 0.351427000\ldots$$
- Footnote: the proof has resolvable difficulties for numbers such as ½, which can be written $.5$ followed by zeros or $.4$ followed by nines (p. 15, n. 3). The size of the square "doesn't matter" (n. 2). For most points the digit strings neither end in zeros nor repeat (p. 15).
- Many mathematicians prefer constructive proofs. The **intuitionist** school rejects non-constructive proofs about infinite sets, where members cannot all be examined (pp. 15–16).
- **Theorem: any one-to-one mapping of a square onto a line must be discontinuous.** "Continuous" would mean a small move of one pointer gives a small move of the other, and a small cluster maps to a small cluster (p. 16).
- **Proof** (by contradiction, pp. 16–17):
  1. Assume continuity. All points on a curve $AB$ in the square must map into the points between $A'$ and $B'$. Otherwise travelling along the curve would jump across the line (discontinuity) or pass a line point twice (not one-to-one).
  2. Choose $C'$ left of $A'B'$ and $D'$ right of it, and find $C$ and $D$ in the square. Draw a curve from $C$ to $D$ crossing $AB$.
  3. The crossing point lies on $AB$, so it maps between $A'$ and $B'$. All other points of the $CD$ curve are not on $AB$, so they map outside $A'B'$.
  4. This contradicts continuity.
- Pierce says both theorems are important in communication theory, so these two are useful, "unlike those concerning hex" (p. 17).

**Intuition note.** Points of a square can all be given addresses on a line, but nearby square points cannot always get nearby addresses. Some nearby points must land far apart on the line.

### Closing (pp. 17–18)
- Mathematics finds step by step facts that are inherent in the problem. Usually one first hits on the facts, then verifies them by proof. Proofs satisfying earlier mathematicians do not satisfy modern ones (p. 17).
- A reviewer of Shannon's paper doubted the author's mathematical intentions, but Shannon's theorems are true and proofs satisfying rigor-minded mathematicians exist. Pierce's own simple proofs are open to purist criticism (p. 17).
- The book will go on to the theorems (not really proved) and to implications beyond mathematical certainty (pp. 17–18).
- Communication theory handles certain aspects of communication, as Newton's laws handle mechanical motion only. It cannot be applied to all problems phrased with "communication" and "information" (p. 18).
- Unlike Newton and Maxwell, it is abstract: it applies to written, acoustical and electrical communication. It proceeds from clear assumptions to theorems about information sources and channels. A theorem is a statement shown to be a necessary consequence of initial assumptions, "the very heart of mathematics" (p. 18).

## Toy example (ours, not from the text)
Apply Pierce's digit-interleaving rule ($y$-digits odd places, $x$-digits even places) to two square points that are very close.
- $P_1$: $x = 0.3000\ldots$, $y = 0.4999000\ldots$. Digits of $y$: 4, 9, 9, 9, 0…; of $x$: 3, 0, 0, 0, 0…. Interleaved: 4, 3, 9, 0, 9, 0, 9, 0 gives $x'_1 = 0.43909090\ldots$
- $P_2$: $x = 0.3000\ldots$, $y = 0.5000\ldots$. Interleaved: 5, 3, 0, 0, 0, 0, 0, 0 gives $x'_2 = 0.53$.
- Distance in the square: $0.5000 - 0.4999 = 0.0001$. Distance on the line: $0.53 - 0.43909090 = 0.0909091$ (approx.).
- A gap of 0.0001 in the square became about 0.09 on the line. This shows the jump for this mapping only. The theorem says every one-to-one mapping has such jumps somewhere.

## Concepts
- [[bit]] — universal measure of information as choice; choosing between two equally probable alternatives is one bit (p. 8)
- [[noisy-channel]] — Pierce mentions perfect and imperfect channels only; no definition yet (p. 8)
- [[theory-generality]] (new) — how wide a range of phenomena a theory covers; it has more than one sense, so theories cannot simply be ranked (pp. 4–6)
- [[physical-vs-mathematical-theory]] (new) — strongly physical theories describe a range of phenomena completely; mathematical ones treat idealized classes or aspects (pp. 6–8)
- [[theorem-and-proof]] (new) — a theorem is a statement shown to follow necessarily from assumptions and definitions (pp. 9–10, 18)
- [[constructive-proof]] (new) — a proof that gives an explicit recipe; a non-constructive proof, like that of hex Theorem II, does not show how to proceed (pp. 13, 15–16)
- [[one-to-one-mapping]] (new) — pairing of two sets where each element has exactly one partner; here square points with line points (p. 14)
- [[continuous-mapping]] (new) — a mapping where small moves of one pointer give small moves of the other (p. 16)

## Canonical instances
- [[aristotle-motion-vs-newton]] — one broad word versus a narrow theory that handles only part of it (pp. 2–3)
- [[network-theory-vs-maxwell]] — two senses of generality; the electrical–mechanical analogy (pp. 5–6)
- [[hex-first-player-theorem]] — a non-constructive existence proof by contradiction (pp. 10–13)
- [[square-onto-line-mapping]] — digit interleaving, a constructive proof (pp. 14–15)
- [[mapping-discontinuity-theorem]] — any such mapping must be discontinuous (pp. 16–17)

## Bridges (candidates)
- [structural-analogy] spring/mass/dashpot ↔ capacitor/inductor/resistor ↔ systems theory: one mathematics, several physical readings (p. 6)
- [metaphor] one word, many things ("run", "motion") ↔ philosophy of science: a theory picks out the relatable part of a concept (p. 3)
- [structural-analogy] digit interleaving ↔ coding: a list of digits can be re-read as a different object with the same content (p. 15)

## Questions this raises
- Which aspects of "communication" does Shannon's theory choose to relate, and which does it leave out?
- Why are the square-onto-line mapping and its discontinuity useful in communication theory (p. 17)?
- How is the "amount of choice or uncertainty" in one bit made precise for more than two alternatives?
- What does the author mean when he later connects communication theory to physics (p. 9)?

## Reading notes
- Page offset: printed = pdf − 16 (pdf 17 = printed 1).
- Edition: per the unit metadata, this PDF is a library scan of the 1961 Harper & Brothers first edition, not the 1980 Dover edition named in the work citation. The pages here show only the running header "Symbols, Signals and Noise"; the text's "twelve years later" after 1948 fits a ca. 1960–61 date.
- The text layer is garbled in places (page 15 digits, primes, footnotes). The page image shows $x = 0.547000\ldots$, $y = 0.312000\ldots$, $x' = 0.351427000\ldots$ and footnotes 2 and 3 as used here.
- Page 7 gives the equation-like "16 ÷ 2 = 8" and "16 = 4 × 4" (p. 7); these are simple arithmetic. The source prints 2,092,278,988,800 as the number of orderings of 16 items, but 16! = 20,922,789,888,000 (ten times larger), so the printed figure looks like a misprint.
- Pierce says a purist would scarcely regard his proofs as rigorous (p. 13) and that they are open to purist criticism (p. 17). The digest follows his steps, not stricter versions.
