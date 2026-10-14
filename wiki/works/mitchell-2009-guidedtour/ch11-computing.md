---
id: mitchell-2009-guidedtour/ch11-computing
work: mitchell-2009-guidedtour
unit: Chapter 11 — Computing with Particles
pages: 11-21
fields: [complex-systems]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 9
pipeline_version: 0.1
---
# Computing with Particles

## L0 — One line
A genetic algorithm evolved cellular automata that do a "majority" task fairly well with no central control, and their working can be explained by describing the boundaries between regions as information-carrying "particles" that collide.

## L1 — The gist (≤ 120 words)
How can a grid of simple cells, each seeing only its neighbors, decide whether most cells start "on" or "off"? A reasonable first-guess local rule (copy the neighborhood majority) fails. A genetic algorithm found rules that work fairly well, but their bit strings reveal nothing obvious. Studying the space-time pictures (cells over time) with Jim Crutchfield's method, the author's group saw that boundaries between regions act as signals. These "particles" move and collide, and the collisions process information. This description predicts a rule's fitness without running it. The author believes the approach may help for other decentralized computation; the brain is only a "perhaps", and plant stomata (leaf pores) a possible case.

**Prerequisites:** what a one-dimensional cellular automaton is (cells on a line, each updating from its neighbors' states); the genetic-algorithm idea of a population of rules scored by fitness (chapter 9, only referred to here).

## L2 — Key ideas (5–10 bullets)
- Majority classification asks a cellular automaton (CA) to turn all cells to the initial majority state. It is trivial for a von-Neumann-style computer (one central processor plus memory), but a CA has no central unit and no random access memory. (pp. 11–12)
- "Each cell copies its local majority" fails: it freezes into stable black and white regions that cannot communicate their sizes. (pp. 12–13)
- A genetic algorithm (GA) evolved rules that do the task fairly well, but the 128-bit genome (the rule written as a bit string) shows nothing obvious about how the rule works. (pp. 13–14)
- In the evolved CA's space-time diagram (a picture of the cells over time), a vertical boundary and a checkerboard region act as signals. Their motion and collisions let the larger region win. (pp. 17–18)
- Crutchfield's idea: region boundaries are "particles" that carry information, and collisions process it. This CA has six particle types and five collision types. (p. 19)
- Particle descriptions let the authors predict fitness, explain why one CA beats another, and describe its mistakes. (p. 20)
- Particles are a description imposed by scientists. Neither the CA rule nor the GA uses them explicitly. (p. 20)
- The author believes the approach will turn out useful where computation is spread over simple parts with no central control; for the brain she says only "perhaps", and plant stomata networks (leaf pores) are a possible case. (p. 21)

## L3 — Walkthrough

**The task (pp. 11–12).** The author, with Peter Hraber and later Rajarshi Das, used a GA to evolve CA rules for "majority classification". If most initial cells are on, the CA must turn all cells on. If most are off, it must turn all off. An odd number of cells avoids ties (p. 11). Analogy: predicting an election from yard signs on your neighbors' lawns (p. 11).

A von-Neumann-style computer does this easily. Its central processing unit counts, stores totals in random access memory, compares them and resets the states (pp. 11–12). A CA has no such memory or central unit. Each cell knows only its own state and its neighbors' states (p. 12). The author calls this an idealized version of real systems, such as a neuron deciding whether to fire, or an ant choosing a job (p. 12). Collective decision making is therefore hard to design into CAs (p. 12).

The CAs were one-dimensional. Each cell is connected to three cells on each side, so a neighborhood has seven cells (p. 12).

**A failed design (pp. 12–13).** The "local majority vote" rule makes each cell take the majority state of its neighborhood. In figure 11.1 the lattice settles within 200 steps into stable black and white regions. The boundaries lie where majority-black and majority-white neighborhoods overlap. The final configuration is mixed, so it is wrong. One black region cannot communicate its length to the other black regions (pp. 12–13).

> *Intuition note.* Each cell sees only seven cells, so no cell can see which color is bigger overall. The rule needs a way to send size information across the lattice, and local voting has none.

**The genetic algorithm (pp. 13–14).** Each rule is a string of bits giving the update state for each possible neighborhood. There are 128 neighborhoods, so the string has 128 bits (pp. 13–14; $2^7=128$ is an added step). The GA starts from random rules. A rule's fitness is the fraction of many initial configurations on which it ends in the correct all-on or all-off state within some number of time steps (pp. 13, 15). After many generations the GA had designed rules that did the task "fairly well" (p. 14). Nothing obvious in the best genome printed hints at how it behaves (p. 14).

**What the evolved rule does (pp. 15–18).** In figure 11.4 the evolved rule is correct on a majority-black and a majority-white start (pp. 15–16). Crutchfield visited and had tools suited to this problem (p. 16). Three patterns appear: all black, all white, and a checkerboard of alternating cells. The checkerboard carries information about local density (p. 17).

Figure 11.5 (a marked-up version of 11.4a) shows the strategy (p. 17):
- Mostly black or mostly white initial regions quickly become solid regions.
- Where a black region on the left meets a white region on the right, a vertical boundary forms.
- Where a white region on the left meets a black region on the right, a checkerboard triangle grows. The lattice is circular, so the triangle wraps around the edges.
- Sides A and B of the checkerboard region move at the same speed. Side A moves southwest and hits the vertical boundary. Side B just misses it on the other side.
- So A had less distance to travel. The white region next to A is smaller than the black region next to B.
- At the collision, A disappears and the black region grows. At the triangle's bottom point, B and C disappear and the whole lattice is black, the correct answer (p. 17).

The vertical boundary and checkerboard region can be seen as *signals* made and carried by local interactions. They let the CA compare adjacent large regions, cut off the smaller one and let the larger one grow (p. 18). This is the main difference from the local-majority CA (p. 18).

> *Intuition note.* Both checkerboard sides move at the same speed, so the side that hits the vertical boundary had less distance to travel. That shows its white region was the smaller one (p. 17).

**Particles (pp. 18–19).** Crutchfield's earlier technique looks for "information processing structures". Boundaries between simple regions carry information, and information is processed when boundaries collide (pp. 18–19). Figure 11.6 colors the simple regions white and leaves only the boundaries. It looks like bubble-chamber traces of elementary particles, so he called the boundaries "particles" (p. 19).

This CA has six particle types: γ, μ, η, δ, β and α. α is short-lived and decays into γ and μ. η is the boundary between black and checkerboard regions. The author says α and β encode different types of information about the initial configuration (p. 19). There are five collision types. Three create a new particle: β+γ, μ+β and η+δ. Two are annihilations where both disappear: η+μ and γ+δ (p. 19).

Information meaning: γ carries the information that it borders a white region, and μ that it borders a black region. If γ meets β before μ does, the combined information shows that the large white region was smaller than the black region it bordered. This is encoded in the new particle η, whose job is to catch up with μ and annihilate it and itself (p. 19).

**Uses and status of the analysis (pp. 20–21).** The analysis was applied to several CAs, for majority classification and other tasks. It allowed the authors to:
- predict a CA's fitness from its particle description alone, without running it;
- explain why one CA is fitter than another;
- describe the mistakes different CAs make (p. 20).

Particles give an information-processing explanation that neither the rule nor the space-time picture alone provides. They are a description imposed by scientists, not something explicit in the CA or used by the GA, yet the GA evolved rules explainable this way (p. 20). The author suggests this vocabulary may be what Wolfram sought in his last problem: "What higher-level descriptions of information processing in cellular automata can be given?" (p. 21). The work is recent and needs development (p. 21).

**Outlook (p. 21).** The author *believes* the approach will turn out useful where computation is spread over simple components without central control. For the brain the author says only "perhaps" something particle-like, or wave-like in three dimensions, will explain it. Stomata are small leaf apertures that open and close in response to light and humidity. Open stomata admit CO₂ but let water evaporate. Mott, Peak and colleagues think stomata form something like a two-dimensional CA, with opening and closing patterns resembling two-dimensional interacting particles. They hypothesize a decentralized computation balancing CO₂ gain against water loss, possibly explainable by such particles (p. 21).

## Toy example
(Ours, not from the text; radius 1 instead of the book's radius 3, to be hand-computable.) A ring of 9 cells, each updated to the majority of (left, self, right). Start $c=[1,1,0,0,1,1,0,0,1]$: five 1s and four 0s, so the correct final answer is all 1s.
- $c_1$: neighbors $c_9=1$, self 1, $c_2=1$ gives 1.
- $c_2$: $1,1,0$ gives 1.
- $c_3$: $1,0,0$ gives 0.
- $c_4$: $0,0,1$ gives 0.
- $c_5$: $0,1,1$ gives 1.
- $c_6$: $1,1,0$ gives 1.
- $c_7$: $1,0,0$ gives 0.
- $c_8$: $0,0,1$ gives 0.
- $c_9$: $0,1,1$ gives 1.

The new state equals the old one, so the pattern is frozen and mixed. The rule fails, because each block of at least two equal cells is stable and sees nothing of the other blocks. Compare the race idea: at 1 cell per step, a signal with distance 3 arrives at step 3, and one with distance 7 at step 7. The first arrival reveals the shorter region.

## Concepts
- [[decentralized-computation]] (new) — computing a global answer with no central unit or memory, only local cell interactions (p. 12)
- [[cellular-automaton]] (new) — a lattice of cells, each updating from its own state and its neighbors' states (p. 12)
- [[genetic-algorithm]] (new) — evolves a population of rules, scoring each by fitness on many test cases (p. 13)
- [[majority-classification]] (new) — task: end all on or all off according to the initial majority (p. 11)
- [[information-processing-structure]] (new) — Crutchfield's term: boundaries between simple regions that carry information and process it on collision (p. 19)
- [[cellular-automaton-particle]] (new) — a boundary between simple regions, treated as a particle that moves and collides (p. 19)
- [[signal]] (new) — here: vertical boundary or checkerboard region carrying size information (p. 18)

## Canonical instances
- [[local-majority-vote-ca]] (new) — natural local rule that fails because regions cannot communicate (pp. 12–13)
- [[ga-evolved-majority-ca]] (new) — evolved 128-bit rule that does the task fairly well, with behavior explained through particle collisions (pp. 14–19)
- [[plant-stomata-network]] (new) — hypothesized natural decentralized computation, maybe with 2D particles (p. 21)

## Bridges (candidates)
- [metaphor] CA boundaries as "particles" ↔ physics: bubble-chamber traces of elementary particles — a visual and naming analogy (p. 19)
- [structural-analogy] Local-majority CA freezing into domains ↔ opinion dynamics: local copying rules that stall in fragmented states
- [structural-analogy] Decentralized CA computation ↔ neurons and ants (chapter 12): decisions from local information only (p. 12)

## Questions this raises
- Is a particle description an explanation, or only a useful description we impose?
- Can particles be found automatically from a rule, instead of by staring at pictures?
- Does the particle idea extend to two-dimensional lattices like stomata, and how?
- How reliable is fitness prediction from particles on rules not yet studied?

## Reading notes
- Printed = pdf − 188 (pdf 199 = printed 11). The unit has no numbered sections, so L3 headings are mine.
- The genome on printed p. 14 was only available as text; I did not reproduce it, and its line breaks in the text layer looked broken (stray "1" at line ends). No image was provided for that page.
- The text layer of other pages matched the images I could check (pp. 13, 15, 16, 18, 19, 20); the figures are only described, not read in detail. No exercises appear in this unit.
