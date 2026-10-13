---
id: ashby-1956-cybernetics/ch13-regulating
work: ashby-1956-cybernetics
unit: "13 Regulating the Very Large System"
pages: 244–264
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Regulating the Very Large System

## L0 — One line
Size is not in itself what makes regulation hard (the variety in the disturbances usually is), and a regulator for a very large system can be obtained by selection, which is fast if done in groups and which needs another regulator or natural selection to start it.

## L1 — The gist (≤ 120 words)
Ashby asks why regulating very large biological or social systems seems so hard, and where the regulator comes from. His answer: the difficulty usually lies in the variety of the disturbances, not in the size. Real disturbances often have constraints, such as repetition, and a regulator is then a machine that can be built. Building (designing) a machine is selection, a reduction of variety that obeys communication-theory limits, can be done in stages, and is fast when done by groups on a reducible system. A regulator is either the survivor of natural selection or made by another regulator. The made regulator need not be bounded by its maker's capacity.

**Prerequisites:** variety as a count of distinct states; the law of Requisite Variety (earlier chapters); logarithms base 2 (bits); the idea of a "machine" as a transformation of states; vectors as ordered lists.

## L2 — Key ideas (5–10 bullets)
- Largeness is usually not itself the difficulty. The main cause is usually the variety in the disturbances D (the events that push the outcome off target), which tends to rise with size (pp. 244–245).
- When the regulator R is much smaller than the system T that yields the outcome, the law of Requisite Variety is likely to dominate. If R's channel capacity is fixed, it sets an absolute limit on regulation, whatever R's internal arrangement, so the regulator should aim near that maximum (p. 245).
- Discovering a constraint in D (a dependence among its components, so that its real variety is lower than it first seems) can turn "regulation impossible" into "possible". If R's capacity is fixed it is the only way (p. 247).
- Many disturbances are repetitive, and non-repetitive ones are uncommon. In Ashby's example, a long sequence of disturbances and responses is a vector (an ordered list) with a machine-like constraint: the pair sequence defines a machine up to isomorphism (the same structure, whatever the labels). So Q, the entity responsible for the regulation, can act as regulator or build a machine to do so (pp. 247–251).
- Designing or selecting a machine is the same as fixing an input at one value. It is an act of communication whose quantity is the fall in variety, and stages add up in log measure, at most (pp. 252–258).
- Supplementing a selection by "chance" means (apart from minor, special requirements) taking variety from a system uncorrelated with the main system (p. 259).
- Selection by successive dichotomies (halving) is enormously faster than item-by-item search. It applies to reducible machines, whose parts can be set separately, and reducibility is common on earth (pp. 260–262).
- A regulator comes from natural selection or from another regulator. The second regulator's capacity is not bounded by the first's, so amplification is possible (pp. 262–264).

## L3 — Walkthrough

### 13/1–13/2. Is size the problem? (pp. 244–245)
- Regulation in the very large system matters to biologists, ecologists, economists, sociologists and psychotherapists. They deal with systems of "almost uncountably many parts" (p. 244).
- **Worry:** these cases look so different from the simple mechanisms of Chapter 12 that earlier results may seem inapplicable (p. 244).
- **Ashby's reply:** not so. Many earlier propositions are stated so that system size is irrelevant. Sometimes the number of states or variables enters, but the proposition holds whatever the number (p. 244).
- Largeness "in itself is not the source" of difficulty. It is blamed because it is obvious and because size is correlated with the real source, the variety in the disturbances (p. 244).
- Size of T tends to be correlated with variety in D for several reasons, of which Ashby gives two (pp. 244–245):
  - Uncertainty about the initial state of many parts is allocated to D (S.11/19).
  - Parts not fully isolated each bring input that adds components to D. If these components are somewhat independent, variety in D grows.
  - Other reasons may exist. When the effects of size are separated from those on D's variety, "it will usually be found" that size itself is irrelevant (p. 245).
- When T is very large and R much smaller (common in biology), the law of Requisite Variety is likely to dominate (p. 245).
  - If R's channel capacity is fixed, the law sets an absolute limit on regulation, "no matter how R is re-arranged".
  - The regulator may choose how its limited fraction is disposed, but the quantity of control stays bounded: for example, outbreaks rather than extensions, or some symptoms controlled and others neglected (p. 245).
- **Analogy (Ashby):** Fisher showed that extracting information from data has a maximum, and Shannon showed that a channel has a maximum. Likewise the regulator should get near its maximum, for beyond it "he cannot go". So approach the very large system "with no extravagant ideas" (p. 245).

*Intuition note.* A small regulator facing a huge, varied world can only absorb so much variety, however clever it is. Hard problems are usually hard mainly because the disturbances are varied, not just because there are many parts.

### 13/3. Where to draw the boundary between T and D (p. 246)
- In a very large system the line between D (source of disturbance) and T (system that yields the outcome) is often vague. It can be drawn in several equally satisfactory ways (p. 246).
- On earth, biological systems tend to be many loosely coupled subsystems, each made of smaller, more tightly coupled ones. Between cattle in a herd the coupling is looser than between a cow's limbs, and looser still than between molecules in a bone (p. 246).
- So the main disturbance D often comes from other systems loosely coupled to T and much like those in T. A boundary must still be drawn in practice, or no definite statement can be made (p. 246).

### 13/4. Ways regulation may become possible (p. 246)
Failure means the organism perishes (an extremely common outcome). Ways out:
- Lower the standard of what is acceptable (a trivial solution, not to be forgotten).
- Increase R's scope and power until its capacity suffices (not examined further).
- The interesting case: regulation that seems most difficult is actually possible (p. 246).

### 13/5–13/6. Constraints (p. 247)
- If the first estimate of D's variety is too high, one may wrongly conclude that regulation to a given degree is impossible with R's capacity (p. 247).
- Further examination may show that D's components are not independent. That is a constraint, and D's real variety is lower. Then the discovery of a constraint may convert "regulation impossible" to "regulation possible" (p. 247).
- If R's capacity cannot easily be increased and other methods are unavailable, then by the law of Requisite Variety discovering a constraint is "the would-be regulator's only hope" (p. 247).
- This is another example of the thesis that a constraint, when it exists, can be turned to use (S.7/14) (p. 247).
- Constraints do not fall into a few simple classes (S.7/10). Ashby studies one form, repetitive disturbance (p. 247).

### 13/7. Disturbances are mostly repetitive (pp. 247–248)
- Many disturbances and responses repeat, especially over a long time. Examples: the cough reflex, physiological regulators, the lifeboat (pp. 247–248).
- Earlier "the regulatory response" in the singular stood for a typical member of a set (p. 248).
- A rare non-repetitive case is an observatory preparing for a supernova. The director would draw a table of D, R and E, as in S.11/4, and inspect it (p. 248).
- Such non-repetitive cases are uncommon. From here on, disturbances and responses occur more than once, and such cases "show constraint" (p. 248).

### 13/8. Grand Disturbance, Grand Response, Grand Outcome (pp. 248–250)
- A disturbance may be a vector (an ordered list of components). Two types:
  - Components act simultaneously (an air-conditioner regulating temperature and humidity; S.11/17).
  - Components come in time. Example: a thermostatically controlled water bath (p. 248).
- Over a short interval the bath's "disturbance" is one event (such as immersing a flask), and its "response" is what happens in the next minute (p. 248).
- Over a year, treat the whole year's disturbances as one **Grand Disturbance** (many small d). The bath has produced a **Grand Response** (many small r). By a standard for the year (e.g. "never fail badly once", or "average deviation under ½°"), one judges a **Grand Outcome** Good or Bad (p. 249).
- What counts as Good in the Grand Outcome must be defined anew and does not necessarily follow from the individual outcomes (p. 249).
  - Three lottery tickets: 1 good + 2 bad individual results = Good Grand Outcome.
  - Three murder trials: 1 good + 2 bad = Bad Grand Outcome.
  - If each disturbance threatens death, Good means good in every individual outcome (p. 249).
- Grand Disturbances are vectors with a constraint. Compare A (age, horse power, colour of one car) with B (age of Jack's car, of Jill's car, of Tom's car). The varieties of the left-hand words are three in A and one in B, so B is restricted (p. 249).
- Vectors like B appear in probability as "sampling with replacement". A coin spun six times gives $2^6 = 64$ possible sequences (p. 249).
- Two varieties can be distinguished (pp. 249–250):
  - (i) within the basic class (2 for the coin);
  - (ii) built up by using the class $n$ times.
- If the basic class has variety $k$ and the vector has $n$ components, the two varieties are at most $k$ and $k^n$. If the first variety has a limit, a large enough $n$ makes the second exceed it (p. 250).

### 13/9. Water-bath example (pp. 250–251)
- Each minute the bath meets one of: (a) cooling draught, (b) sunshine, (c) cold object immersed. The variety is 3 (p. 250).
- Over a year the Grand Disturbance might be a vector of 400 components, such as $(a,b,a,b,b,a,c,b,b,c,c,b,b,\dots,c,b,a,b)$. If the correct individual responses are $\alpha,\beta,\gamma$, the Grand Response is $(\alpha,\beta,\alpha,\beta,\beta,\alpha,\gamma,\beta,\beta,\gamma,\gamma,\beta,\beta,\dots,\gamma,\beta,\alpha,\beta)$ (p. 250).
- With no constraint from component to component, the set of possible Grand Disturbances has variety $3^{400}$, and the Grand Response needs at least as much for full regulation (p. 250).
- **The point:** the double sequence as it occurred in time (a→α, b→β, a→α, …, "not necessarily at equal time-intervals") shows the constraint of a machine and defines a machine up to isomorphism. As a protocol (the recorded sequence of events), it defines the machine with input (pp. 250–251):

$$
\begin{array}{c|ccc}
\downarrow & \alpha & \beta & \gamma\\ \hline
a & \alpha&\alpha&\alpha\\
b & \beta&\beta&\beta\\
c & \gamma&\gamma&\gamma
\end{array}
$$

- So when the Grand Disturbance is a vector from one basic set, the Grand Response can be a vector of equal variety or the output of a suitable machine with input (p. 251).

*Intuition note.* A long sequence of different disturbances looks hugely varied ($3^{400}$ possibilities). But if each type always gets the same response, one small rule (a machine) produces the whole response sequence.

### 13/10. Q: regulate directly, or build a machine? (p. 251)
- Let Q be the entity responsible for regulation, often the possessor of the essential variables E. With repetitive disturbances, Q can either act as R, or build a machine that, once built, regulates indefinitely without further action by Q (p. 251).
- Also, Part III assumed the regulator existed and never said how it came to be made. So we must consider how a regulatory machine is designed and made, whether by the brain developing machinery in nervous material or by a sociologist building a regulatory organisation (p. 251).

### 13/11. Design as communication (pp. 251–253)
- Take "Entity Ω designs machine M" very broadly. It includes genes determining the heart, a mechanic making a bicycle, one part of the brain fixing connexions in a nerve-net, a works-manager laying out a factory, and a mathematician programming a computer (p. 252).
- Cybernetically, the interest is in what determines the final model, how it comes to be selected. This is tracing chains of cause and effect, like a telephone mechanic relating each wire at one end to one at the other. Ashby follows D. M. MacKay's thesis that quantity of information corresponds to some quantity of selection, actual or imaginable (p. 252).
- Genes illustrate this. The gene-pattern in *Lumbricus*, *Rana* and *Homo* leads to a worm's, frog's and man's heart. This is control. It is also regulation, because whatever the molecules' initial state, the variety disappears and a standard heart appears (p. 252).
- Design applies to sets, even when language uses the singular. "The gene-pattern determines the heart" means the set of gene-patterns is matched to the set of hearts, like wires in a cable (p. 253).
- So designing is an act of communication from Maker to Made. Communication measures for reducing many possible messages to one apply to reducing many possible machines to one. Imagining the design done through a telephone helps identify the quantity of information to be transmitted (p. 253).

### 13/12. Selecting a machine = fixing an input (pp. 253–254)
- Three cases are abstractly equivalent: a buyer picks one of three radios, a designer picks one of three circuits, an owner sets a three-position switch. Selecting one machine from three is selecting one value of a parameter (p. 253).
- Machines on states a, b: $\alpha$: a→b, b→a; $\beta$: a→a, b→a; $\gamma$: a→b, b→b. Selecting $\beta$ is the same as having one machine with a three-valued input and fixing the input permanently at $\beta$ (pp. 253–254):

$$
\begin{array}{c|cc}
\downarrow & a & b\\ \hline
\alpha & b & a\\
\beta & a & a\\
\gamma & b & b
\end{array}
$$

- An observer who watches only the results cannot tell the two processes apart (p. 254).
- Fixing the input leaves an absolute system (no input). To end with a machine that still has input, the original must start with two or more inputs, so fixing one leaves the others free (p. 254).
- The designer's act of selecting one model from many is equivalent to some determining factor fixing an input at a permanent value (p. 254).

### 13/13. A minor complication (pp. 254–255)
- What if the choice is between machines with different state sets, such as one on $\{a,b\}$ and one on $\{p,q,r\}$? This reduces to the earlier case by notation. Use a reducible machine whose states are couples $(a,p),\dots,(b,r)$ with two inputs $\mu$ and $\nu$ (p. 254).
- $\mu$ acts on the first component ($a\to b$, $b\to a$), with the second left as "dots" (do not matter). $\nu$ acts on the second ($p\to r$, $q\to q$, $r\to r$), with the first left as dots (p. 254).
- Choosing $\mu$ gives the first machine and ignores the rest. Choosing $\nu$ gives the second. So "the initial formulation is really quite general" (p. 255).

### 13/14. Design in a Black Box (p. 255)
- Design as defined can be done inside a Black Box that has an input. An owner who does not know the radio's contents but knows how the switch affects the output performs "design in a Black Box" by setting the switch (p. 255).
- If another machine dominates the radio and fixes the switch, it "designs" the radio, in the sense that it shows the behaviour objectively shown by a designer (p. 255).
- The same applies to the brain. One part (perhaps a basal structure) may stand to a neural network as designer to machine. The relation is exact in that experiment can test objectively whether it holds (p. 255).

### 13/15–13/16. Quantity of selection (pp. 255–257)
- The reduction from many initial possibilities to the final few or one is measured on the same scales as variety and information (S.7/7, 9/11), directly or logarithmically (p. 256).
- The measure specifies the capacity the channel C (Designer → Machine) must have if the necessary variety can be transmitted at all (p. 256).
- It does not say "how much design is in this machine" without reference to what it might have been. It applies to the act of communication and to the set of possibilities, not to the resulting thing (p. 256).
- **Markovian machines (13/16):** choosing between two Markov machines (matrices of transition probabilities) involves just 1 bit. We are choosing between two objects, and the fractions inside are irrelevant. This differs from the 1.58 bits that the all-$1/3$ matrix produces on average per step as an information source (p. 257).
- Exercises follow both after 13/15 and after 13/17 (see below).

### 13/17. Selection in stages (pp. 257–258)
- Selection may be spread out in time or occur in stages. A car buyer adds criteria (price under £1000, seats five) until one car is left, with a coin spin as final selector if needed (p. 257).
- For a machine on states a, b, c, d, the transformation $T$ below leaves all possibilities open. $U$ is a partial selection (a smaller set). $V$ excludes all single-valued transformations containing $a\to a$ or $a\to d$ (pp. 257–258):

$$
T:\ \begin{array}{c|cccc} \downarrow & a&b&c&d\\ \hline & *&*&*&*\end{array}\qquad
U:\ \begin{array}{c|cccc} \downarrow & a&b&c&d\\ \hline & c&*&b&*\end{array}\qquad
V:\ \begin{array}{c|cccc} \downarrow & a&b&c&d\\ \hline & b\text{ or }c&*&*&*\end{array}
$$

  (asterisks: not yet decided).
- **Fundamental result:** the overall selection cannot be more than the sum, measured logarithmically, of the separate selections. Selection is measured by the fall in variety (p. 258).
- Example: from a pack of 52 cards, a 2-bit selection then a 3-bit selection leaves a further selection of at least 0.7 bits needed, because $\log_2 52 = 5.7$. The limit is absolute and does not depend on the type of machine or mode of selection (p. 258).
  - Check (added step): $2+3 = 5$ and $5.7-5 = 0.7$.

*Intuition note.* Each criterion removes some options, and bits of removal add up at best. You cannot pin down one item among $N$ with fewer than $\log_2 N$ bits in total, however you split the work.

### 13/18. Supplementation of selection (pp. 258–259)
- Because selection works in stages, several selectors can supplement one another: a husband sets a price limit and his wife chooses, or she spins a coin (p. 258).
- Random supplements: in Bridge, shuffling assigns a definite part of the determination to chance. The Roman general left the remainder to birds or entrails. Fisher apparently first deliberately used wholly uncorrelated selectors in science (p. 259).
- "Random" here refers to the factor's relation to the main system, not to what it is in itself. A thousand digits of $\pi$ may serve for agricultural experiments, not because they are random but because they are probably uncorrelated with the plots' peculiarities (p. 259).
- Supplementation by chance means taking variety from a system whose behaviour is uncorrelated with the main system. Yesterday's gold-share price might suit a rat in a maze, but not a financial-economic system (p. 259).

### 13/19. Selection by a machine (pp. 259–260)
- Whatever selects, $L \to M$, must itself be considered a mechanism. Three ways a machine selects (p. 260):
  - Following one trajectory (state $i$ goes to $j$ and no other).
  - Every determinate machine reduces its variety of states from the maximum to the number of its basins (S.7/24).
  - One part vetoing another's states of equilibrium (S.5/13): "no good, still no good … Hold It!". Ashby says a machine built as a selector will, "so far as I can see", have to act in this way, like the second-order feedback of Fig. 5/14/1 (p. 260).
- In Shannon's theory every act of communication is also an act of selection (p. 260).

### 13/20. Duration of selection (pp. 260–261)
- Estimated selection may look cosmologically long, but, Ashby says, it does not follow that the time actually taken is equally long: "This is far from being the case" (p. 260).
- Shannon showed: to pick 1 from $N$ when the selector can only indicate whether the wanted element is in a given set, the fastest method is successive dichotomies (halving). Early selections are between groups, not elements, and for very large $N$ this is "almost incomparably faster" than going one by one (p. 261).
- **Example: one atom in the visible universe** (p. 261).
  - Counts (author's figures): about $10^{8}$ galaxies; about $10^{11}$ suns each; about $3\times10^{5}$ bodies per solar system; about $10^{12}$ cubic miles in the earth; about $10^{21}$ dust particles per cubic mile; about $10^{16}$ atoms per particle.
  - Ashby calls this 1 **mega-pick**, "about 1 from $10^{73}$".
  - One at a time, testing a million per second: the number of centuries needs more than a page's width to write.
  - By dichotomy at one step per second: "just over four minutes".
  - (added step) $\log_2 10^{73}\approx 242.5$ steps, so about 242 s, a little over 4 minutes.
- The method of groups shows its power exactly when item-by-item search becomes excessively long (p. 261).

### 13/21. Selection and reducibility (pp. 261–262)
- Take a machine with 50 inputs, each with 25 values, where one particular form is sought. This is about 1 mega-pick, so selecting seriatim is hopeless. Selecting by groups needs a practical way to group the input-states (pp. 261–262).
- If the machine is **reducible** (S.4/14) and the inputs go separately to the sub-systems, one can select the right value for part 1 on its input, then for part 2, and so on. That is the fast method by groups (p. 262).
- Reducibility is extremely common on earth, and "he who would learn how to regulate the very large system" must be fully aware of it (p. 262).
  - If reducibility were lost, so that every variable affected every other, turning a page might change the lights, the table and the clock. Regulation would be so difficult as to be impossible, and no organised life could persist (S.7/17) (p. 262).
- **Conclusion:** if Q is to design a machine to regulate a very large system, and the regulator is itself somewhat large, success in reasonably short time is likely to depend much on whether the regulator can be made reducible (p. 262).

*Intuition note.* If the parts can be set one at a time, selection can go by groups, which is the fast method. (added step) Counting options, you try the sum of the part-sizes instead of their product, which can turn an impossible search into a short one. Ashby says reducibility is extremely common on earth (p. 262).

### 13/22. Whence the regulator? (pp. 262–263)
- Making a machine of desired properties implies selection. Q worked to a goal despite initial variety, so he acted as a regulator. Making such a machine is an act of regulation (p. 263).
- If the machine is the Part III regulator, "the answer is inescapable: by another regulator" (p. 263).
- **Is this a reductio ad absurdum? Ashby: "I think not."** As biologists, the earth has existed for a long time, selection has acted throughout, and selection favours the appearance of regulators (S.10/3, 10/5). These facts suffice to account for many good regulators on earth. No further explanation is needed if some regulators have as goal the bringing of some mechanism to standard form, even a regulator (p. 263).
- **Answer:** a regulator can be selected from a general set of mechanisms (non-regulatory ones) only by being the survivor of natural selection or by being made by another regulator (p. 263).

### 13/23. Is two-stage making wasteful? (pp. 263–264)
- Making a regulator by two stages seems wasteful. Does it imply that the regulator must already exist before one can be made? And does it imply no advance for sociologists limited to human capacity? (p. 263).
- **Ashby: it does not.** When $R_1$ brings $R_2$ into existence, $R_2$'s capacity is not bounded by $R_1$'s. $R_2$ may exceed $R_1$, so that an amplification occurs. This is studied in the next chapter, where regulation by stages, "apart from being necessarily wasteful", opens remarkable possibilities (pp. 263–264).

## Toy example (ours, not from the text)
**Combination lock with 3 dials, each with 10 positions.** Seen as a machine with 3 inputs, there are $10^3 = 1000$ possible forms. The designer (the person opening it) needs $\log_2 1000 \approx 9.97$ bits of selection. By 13/17 these add by stages: $\log_2 10 \approx 3.32$ bits per dial, and $3 \times 3.32 = 9.97$ bits.
- **One by one (seriatim):** try the combinations in turn. At most 1000 trials; on average about 500.
- **By parts (reducibility, 13/21):** suppose each dial gives a click when right, so the dials can be set separately. Then at most $3\times10 = 30$ trials, on average about $3\times5 = 15$.
- **By halving (dichotomy, 13/20):** if one could ask "is the digit in 0–4 or 5–9?", each dial takes about 4 yes/no questions ($2^4=16\ge10$), so about 12 questions in all, close to the 9.97-bit minimum.

The number of bits is a fixed limit. How quickly you reach it depends on whether the parts can be selected separately (the lock's reducibility) and on how well you can ask group questions.

## Concepts
- [[variety]] — the number of distinct states or elements in a set; can be measured as a count or in logarithms (p. 256).
- [[law of requisite variety]] — if R's capacity is fixed, it sets an absolute limit on regulation, whatever R's inner arrangement (p. 245).
- [[constraint]] (new) — dependence among components of D that makes the real variety lower than the nominal one. Finding it may make regulation possible (p. 247).
- [[repetitive disturbance]] (new) — a disturbance and response recurring many times. The sequence defines a machine, so Q can build a regulator (pp. 248–250).
- [[disturbance and noise]] — here D, the source of disturbances. Its boundary with T is often arbitrary (p. 246).
- [[black box]] — a system known only by input–output behaviour. "Design in a Black Box" means setting its input to get the wanted behaviour (p. 255).
- [[design as selection]] (new) — designing a machine is fixing an input at a permanent value. It is an act of communication from Maker to Made (pp. 252–254).
- [[quantity of selection]] (new) — the fall in variety when the possible machines are reduced to one. It sets the channel capacity needed (p. 256).
- [[selection in stages]] (new) — selection done by successive criteria. The total cannot exceed the sum of the stages (log measure) (p. 258).
- [[supplementation by chance]] (new) — completing a selection with an uncorrelated random factor, defined by its relation to the main system (p. 259).
- [[selection by dichotomy]] (new) — selecting by groups, halving at each step. It is far faster than item-by-item search (p. 261).
- [[reducibility]] (new) — a machine whose sub-systems can be set separately, allowing fast selection. It is common on earth (p. 262).

## Canonical instances
- [[grand-disturbance-water-bath]] — a thermostatic bath over a year: 400-step sequence from three disturbances, with $3^{400}$ unconstrained possibilities (p. 250).
- [[coin-spun-six-times]] — 64 possible sequences, with varieties 2 and $2^6$ (p. 249).
- [[radio-set-three-circuits]] — selecting one of three machines equals setting a switch (p. 253).
- [[card-pack-selection]] — 2 + 3 bits leaves at least 0.7 bits of the 5.7 bits needed (p. 258).
- [[mega-pick-atom]] — one atom in the visible universe: a few minutes by dichotomy, impractically long item by item (p. 261).
- [[heart-gene-pattern]] — gene-patterns select the heart of worm, frog or man (p. 252).
- [[bridge-and-roman-general]] — supplementation of selection by chance (p. 259).

## Bridges (candidates)
- [structural-analogy] Fisher's maximum on extracting information and Shannon's maximum on a channel ↔ the law of Requisite Variety as a limit on regulation — Ashby says the change in point of view is "not unlike" theirs (p. 245).
- [structural-analogy] Selection by successive halving ↔ binary search in computing: both reduce 1-of-$N$ search to about $\log_2 N$ steps (p. 261).
- [structural-analogy] Setting part 1, then part 2, etc., on a reducible machine ↔ decomposition in optimisation: independent subproblems add instead of multiply (p. 262).
- [structural-analogy] Machine as a record of (disturbance, response) pairs ↔ learning a policy from repeated experience (p. 250).
- [metaphor] One regulator building a better regulator ↔ evolution or learning-to-learn: capacity of the made regulator is not bounded by the maker (p. 264).

## Questions this raises
- How can the real constraint in a very large D be found in practice, and how reliably can one be sure that the first estimate of variety was too high?
- How exactly can $R_2$ exceed $R_1$ in capacity without breaking the law of Requisite Variety? (Ashby defers to the next chapter, p. 264.)
- When is a real system only approximately reducible, and how does that change the speed of selection?
- Does the limit that bits of selection add up at best hold when the selectors are not independent?

## Exercises worth doing
- Ex. 13/15/1 (p. 256) — three resistors, each with seven values: the variety the designer must supply (the basic count for selection) — easy.
- Ex. 13/15/3 (p. 256) — resistors in parallel: variety counts electrical properties, not component settings — medium.
- Ex. 13/15/5 (p. 256) — design of a stamp counted two ways, and why the answers disagree — medium.
- Ex. 13/17/1 (p. 258) — how many possibilities a restriction removes from 27 transformations — easy.
- Ex. 13/17/4–5 (p. 258) — selection for "no state of equilibrium" on $n$ states, and its limit as $n\to\infty$ — hard.
- Ex. 13/17/6–7 (p. 258) — information gained by systematic versus random searching of a shuffled pack — hard.

## Reading notes
- **Page numbers:** the metadata says printed pages are unknown, and the labels give none. The page images, however, show printed numbers on spreads, so printed numbers are used. Each pdf page is a two-page spread: pdf 130 = pp. 244–245, … pdf 139 = pp. 262–263, and pdf 140 = p. 264 (left half only; blank after). Rule: pdf $N$ = pp. $2N-16$ and $2N-15$. In the text layer of pdf 131–135 the left-hand page's text comes first; on pdf 130 and 136–139 the lines of the two pages are interleaved.
- **Misprints and OCR:** the section heading reads "3|11" in the image for 13/11. Ex. 13/15/1 shows "loo ohms" for 100. "1 58 bits" in 13/16 is 1.58 bits. On p. 263 the text layer has "an with", "I thin not", cut-off line ends (e.g. "appearance c", "some o") and "(man, non- regulatory)", which looks damaged. The phrase "Ex. I" in Ex. 13/17/3 means Ex. 1.
- **Cross-references:** many references (S.11/19, S.7/8, S.10/5, etc.) point to chapters not in this unit. They are reported as stated, not checked.
- **Exercises:** two sets, one after 13/15 (Ex. 1–7) and one after 13/17 (Ex. 1–7; starred ones marked *). Solutions are not printed here.
- **13/13** is flagged by the author as a minor complication. Its tables are given in prose only here.
