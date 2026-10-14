---
id: mitchell-2009-guidedtour/ch12-information
work: mitchell-2009-guidedtour
unit: Chapter 12 — Information Processing in Living Systems
pages: 22–42
fields: [complex-systems]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Information Processing in Living Systems

## L0 — One line
In immune systems, ant colonies and cell metabolism, "information" is a changing statistical pattern over many simple parts, and the system handles it by sampling, with random components and feedback that shifts resources toward what looks promising.

## L1 — The gist (≤ 120 words)
What does it mean to say that living systems "process information"? Mitchell asks three questions: what is the information, how is it communicated and processed, and how does it get meaning? She compares traditional computers and cellular automata, then studies the immune system, ant colonies and metabolism. In all three, information is a statistical, changing pattern over many simple components. It is passed on by sampling, and behavior contains randomness. Many components explore in parallel, and resources shift toward promising directions. She ties meaning to fitness, and says that the question of who perceives the meaning has not yet been fully explained. The term "information processing" tends to be ill-defined outside the formal setting of Turing machines.

**Prerequisites:** Turing machine and cellular automaton (earlier chapters); basic idea of natural selection; positive and negative feedback.

## L2 — Key ideas (5–10 bullets)
- "Information processing" is often ill-defined outside Turing-machine settings. Mitchell proposes three questions to pin it down: what is information, how is it processed, what does it mean (p. 23).
- In traditional computers, a high-level language gives a human-friendly description above machine code (the low-level step-by-step instructions), and compilers (programs that translate between the levels) do the translation. Cellular automata have no such tools, at least not yet; particles are one proposed approach toward a high-level language (pp. 24–25).
- The immune system, ant colonies and metabolism have no central controller. Each uses local chemical signals (cytokines from immune cells, pheromones from ants, molecule concentrations in cells) and feedback, where the results of a process adjust that process (pp. 31–34).
- Information is not stored in one place. It is a statistical and dynamic pattern over many components, so components must communicate by sampling (pp. 35–36).
- Randomness appears to be needed so that a comparatively small population of simple components can explore a much larger space, particularly when the information is statistical and there is little prior knowledge. It is balanced by self-regulation that adjusts probabilities (pp. 37–38).
- A fine-grained system (many small, simple parts working in parallel) can do a "parallel terraced scan": many explorations run at once, and resources follow perceived success (pp. 38–39).
- Systems must balance unfocused exploration against focused exploitation; the balance shifts toward exploitation as information is gained (p. 40).
- Mitchell's view: meaning is tied to survival and fitness. Who perceives meaning in a leaderless system is, she says, not yet explained to anyone's satisfaction (p. 41).

## L3 — Walkthrough

### Introduction (p. 22)
Information and computation have spread through science since Szilard's insight about Maxwell's demon. Many people treat information as a third primitive of reality beside mass and energy. Yet "information processing" tends to be ill-defined outside the formal setting of Turing machines and von Neumann-style computers. The chapter treats three systems (immune system, ant colonies, cellular metabolism) and then draws common principles (p. 22).

### What Is Information Processing? (pp. 23–26)
Mitchell uses "information processing" and "computing" as synonyms for now. When we say a system processes information or computes, three questions need to be answered (p. 23):
1. What plays the role of "information"?
2. How is it communicated and processed?
3. How does it acquire meaning, and to whom? (Some disagree that computation needs meaning; Mitchell claims it does.)

**Traditional computers.** Information is the tape symbols and the tape head's states. It is processed by reading, writing and changing state, following the program (p. 23). Programs can be viewed at (at least) two levels: machine code (low-level steps) and a programming level (high-level language such as Java). One high-level instruction usually maps to several low-level ones, so the programming level is more abstract. Meaning comes from human interpretation of inputs, outputs and intermediate steps (p. 24).

**Cellular automata (CA).** In the majority-classification CA, by analogy with traditional computers, information can be said to be located in the lattice configurations. The input is the initial configuration, the output is the final one, and each neighborhood processes information by the CA rule. Meaning comes from human interpretation of the task (p. 25). This level is analogous to "machine code" and does not give a human-friendly understanding of how the computation is done. The particles proposed in the previous chapter are one approach toward a high-level language: movement communicates information, and collisions process it (p. 25).

Computers were designed so that translation between levels is easy, and compilers and decompilers do it. For CAs no such tools exist "at least not yet", and there is no practical general way to design high-level "programs". Particles are far from a theoretical framework (p. 25). The question "In what sense do natural systems 'compute'?" is still largely unanswered (p. 25). A high-level description would give a "high-level language" for biology and let us abstract general principles (p. 26).

*Intuition note:* A computation can be described at a detailed level (every step) or at a human level (what it is for). For ordinary computers the two levels are linked by tools. For natural systems such a human-level language is still largely missing, and that is the gap this chapter explores.

### The Immune System (pp. 26–31)
Focus: lymphocytes (white blood cells made in bone marrow). B cells release antibodies; T cells kill invaders and regulate other cells (p. 26).

- **Receptors.** Cells have surface receptors, which receive information as molecules that bind to them if shapes match sufficiently. A lymphocyte carries identical receptors for one range of shapes. If a pathogen molecule (an antigen) fits, the lymphocyte "recognizes" it. Binding can be strong or weak (pp. 27–28).
- **Problem and solution.** The system cannot know in advance which pathogens will come, and their number is astronomical. It therefore keeps a very diverse lymphocyte population. Each newborn lymphocyte gets a random combination of receptors by shuffling in its DNA. About ten million new lymphocytes are born per day (p. 28).
- **Deciding whether to attack.** Attack can itself harm the body, and too strong an attack can be lethal. The system goes into high-gear attack mode "only if" it picks up *a lot* of sufficiently strong binding events (pp. 28–29).
- **B-cell activation.** A B cell is activated if the number of strongly bound receptors exceeds a threshold and, in the same time frame, T cells with similarly bound receptors send "go-ahead" signals. The B cell then releases antibodies, which bind antigens, neutralize them and mark them for destruction (p. 29).
- **Selection loop.** The activated B cell goes to a lymph node and divides rapidly. Many daughters carry mutated receptors. Daughters are tested on captured antigens, and non-binders die. Survivors enter the blood. Those that bind (sometimes more strongly than the mother) repeat the cycle, and the best matches produce the most daughters. This is natural selection producing antibodies "designed" for one antigen. Eradication typically takes days to weeks (p. 30).
- **Two problems.** (a) Attacking the body's own molecules; (b) toning down an attack that harms the body. Immunologists lack complete answers (p. 30).
  - *Negative selection* (thought to be one major mechanism): new lymphocytes are tested in bone marrow and thymus against "self" molecules. Strong self-binders tend to be killed or edited. This mechanism often fails, sometimes producing autoimmune disorders such as diabetes or rheumatoid arthritis (p. 30).
  - *Regulatory T cells* seem to be a second major mechanism; they secrete chemicals that suppress other T cells, though exactly how they work is not yet known (p. 30).
  - *BAFF competition* (hypothesized): self-binding B cells need more of the limited chemical BAFF, so they die more often (pp. 30–31).
  - *Cytokines:* harm to the body can cause cytokine secretion, which suppresses active lymphocytes. Presumably more harm means a higher concentration, so cells are more likely to turn off, regulating without suppressing altogether (p. 31).

### Ant Colonies (pp. 31–33)
Ant colonies are compared to brains: networks of simple elements from which larger information-processing behavior emerges. Foraging and task allocation happen with no central control, by mechanisms "surprisingly similar" to the immune system's (p. 31).

- **Foraging.** In many ant species, roughly: ants set out in random directions. An ant that finds food returns to the nest leaving a pheromone trail. Other ants are likely to follow a trail, more likely when the concentration is higher. Ants that find food reinforce the trail. Without reinforcement the trail evaporates. Trails and their strengths form a good model of the food environment found by the foragers, and it adapts to change (pp. 31–32).
- **Task allocation (Deborah Gordon, Red Harvester ants).** Workers divide among foraging, nest maintenance, patrolling and refuse sorting. If the nest is disturbed slightly, nest-maintenance workers increase. If food is plentiful and good, foragers increase (p. 32).
- **Mechanism.** The answer seems to be that an ant switches task depending on what it meets in the environment and on the *rate* of encounters with ants doing other tasks. Examples: an inactive ant meeting a foreign object, or many maintenance workers, is more likely to do maintenance. A maintenance worker meeting many foragers returning with seeds is more likely to forage. Ants apparently sense others' tasks by antenna contact, perceiving chemical residues (p. 33).
- Similar mechanisms seem to underlie other collective behavior (e.g., bridges made of ant bodies), though much is not understood (p. 33).

### Biological Metabolism (pp. 33–34)
Metabolism is the set of chemical processes by which organisms use energy from food, air or sunlight to maintain life. It runs in cells via chains of reactions called metabolic pathways (p. 33). Millions of molecules drift randomly in the cytoplasm. Enzymes occasionally meet matching molecules and speed up reactions, so large molecules are built gradually (p. 34). Pathways are controlled by self-regulating feedback, much as cytokines (immune system) and pheromones (ants) regulate those systems (p. 34).

**Example (p. 34):** glycolysis turns glucose into pyruvate, which the citric acid cycle uses to make, among other things, ATP, the cell's principal source of usable energy. A large amount of ATP slows glycolysis. A lack of ATP speeds it up. In general, a pathway's speed is often regulated by chemicals the pathway itself produces. Hundreds of pathways run at once, some independent and some interdependent (p. 34).

### Information Processing in These Systems (pp. 35–41)
Mitchell now answers the three questions for these systems (p. 35).

**What plays the role of information? (pp. 35–36)** The relevant actions are collective, not those of single cells, ants or enzymes. Information is not statically located anywhere. It takes the form of "statistics and dynamics of patterns over the system's components" (p. 35).
- Immune system: the distribution and dynamics of lymphocytes represent the changing pathogen population. Cytokine concentrations encode information about success against pathogens and harm to the body (p. 35).
- Ants: the distribution of ants on trails represents the food environment; the distribution over tasks represents the colony's state (p. 35).
- Metabolism: the cell's state and needs are reflected in molecule concentrations and dynamics (p. 36).

**How is it communicated and processed? (pp. 36–40)**

*Communication via sampling.* No component can perceive the "big picture", so information is communicated by spatial and temporal sampling (p. 36). Lymphocytes sample antigens and cytokines through receptors, and these samples decide whether they activate. Ants sample pheromone concentrations and rates of encounters with other ants. In metabolism, enzymes sample molecule concentrations through binding (pp. 36–37).

*Random components of behavior.* Since the information is statistical, actions need random or at least "unpredictable" components (p. 37).
- Immune system: random receptor shapes, random spatial distribution by the bloodstream, and random aspects of thresholds, division rates and mutations (p. 37).
- Ants: random foraging movements and probabilistic trail-following and task-switching. Ziff and Rosenfield: an apparent "map" of paths is "really just a consequence of a series of random searches" (p. 37).
- Metabolism: random diffusion and probabilistic encounters, with probabilities changing as concentrations change (p. 37).

Such randomness appears needed for a comparatively small population of simple components to explore a far larger space, when the information to be gained is statistical and there is little prior knowledge (pp. 37–38). Randomness must be balanced with determinism: self-regulation continually adjusts the probabilities, and so how deeply to explore particular pathways (p. 38).

*Fine-grained exploration.* Many biological complex systems, "if not all", are fine-grained: many simple elements working in parallel. Several possible advantages are robustness, efficiency and evolvability; one further major advantage is the ability to do Hofstadter's "parallel terraced scan" (p. 38). This is a simultaneous exploration of many possibilities, where resources for each depend on its perceived success at that time. It is parallel because many are explored at once, and terraced because they differ in speed and depth. Information is used as it is gained to reassess what to explore (p. 38).
- Immune system: each lymphocyte is a mini-exploration of a shape range. Successful ranges get more resources (mutated offspring), yet new lymphocytes always explore novel ranges (pp. 38–39).
- Ants: resources go to paths in proportion to promise (amount and quality of food found). Unpromising paths still get explored with far fewer ants, since a better source might exist (p. 39).
- Metabolism: pathways speed up or slow down through feedback in the form of changing concentrations (p. 39).

Fine granularity lets the system change course fluidly, because only simple micro-actions are committed at any time, whereas coarse-grained actions commit time to an exploration that may not be warranted. Redundancy lets the system work when components are unreliable and information is only statistical. Fine-grained actions matter only when many components take them (p. 39).

*Interplay of unfocused and focused processes.* All three systems mix random, unfocused exploration with focused action driven by perceived needs (p. 40). Immune system: a varied lymphocyte population versus offspring that are variations of successful cells. Ants: random search versus following trails. Metabolism: random molecular exploration versus activation or inhibition driven by concentrations and genetic regulation (p. 40). The optimal balance shifts over time: early on exploration is largely random, then it becomes more deterministic and focused as information is acted on. The system "explores to obtain information and exploits that information to successfully adapt" (p. 40). This balance has been hypothesized to be a general property of adaptive and intelligent systems. John Holland cited it to explain how genetic algorithms work (p. 40).

*Intuition note:* The system must find out what is out there and also use what it has found. Early on it knows little, so it searches widely. Later it puts more effort into what has worked, but (in the immune-system and ant examples) never stops searching altogether.

**How does information acquire meaning? (p. 41)** Mitchell does not think she can add much to what philosophers have said, but claims that understanding information processing in living systems requires answering the question in some form.
- **Mitchell's view:** meaning is "intimately tied up with survival and natural selection". An event means something to an organism if it affects its well-being or reproduction, so the meaning of an event "is what tells one how to respond to it". Events in the immune system mean something because they tell it how to respond to increase the organism's fitness (used informally). The same applies to ant colonies and cells (p. 41).
- **Open question:** with no central controller, who or what perceives meaning? Mitchell treats this as the question of consciousness or self-awareness in living systems. She calls it among the most profound mysteries and says it is not yet explained to anyone's satisfaction (p. 41).
- **Spin-off:** computing ideas from these systems inspired artificial immune systems (programs that adaptively protect computers) and ant colony optimization algorithms (simulated ants, pheromones and job switching, used for cell-phone routing and truck scheduling). She knows of no AI program inspired by all three systems except one she wrote with her Ph.D. advisor, described in the next chapter (pp. 41–42).

## Toy example (ours, not from the text)
A parallel terraced scan with 120 ants and 3 candidate paths A, B, C.
- Round 0, no information: 40 ants per path (120 / 3).
- Suppose food quality found is A = 6, B = 3, C = 1 (total 10).
- Rule: 30 ants keep exploring at random, 10 per path; the other 90 follow trails in proportion to quality.
- Focused ants: A = 90 × 6/10 = 54; B = 90 × 3/10 = 27; C = 90 × 1/10 = 9 (sum 90).
- Totals: A = 10 + 54 = 64; B = 10 + 27 = 37; C = 10 + 9 = 19; 64 + 37 + 19 = 120.
- A gets most resources, but C still gets 19 ants, so a later improvement of C could still be noticed. This is the exploration–exploitation balance in miniature.

## Concepts
- [[information-processing-in-living-systems]] (new) — at a very general level, computation is what a system does with information to succeed or adapt; to say a system does this, three questions must be answered (information, processing, meaning) (p. 23)
- [[two-levels-of-description]] (new) — machine-code level versus a human-friendly high-level language; not yet available for CAs (particles are one proposal) or for living systems (pp. 24–26)
- [[decentralized-control]] (new) — behavior arises from simple components with no central controller or leader (p. 31)
- [[emergence]] — larger-scale information-processing behavior arising from networks of simple elements, as in ants and neurons (p. 31)
- [[feedback]] — in metabolism, a pathway's speed is regulated by chemicals it produces (e.g., ATP slowing glycolysis); the author also calls ant trail allocation feedback (pp. 34, 39)
- [[communication-via-sampling]] (new) — no individual component perceives the global "big picture", so information is communicated by spatial and temporal sampling of statistical patterns (p. 36)
- [[fine-grained-architecture]] (new) — many simple, redundant elements working in parallel; several possible advantages, including robustness, efficiency and evolvability, and parallel terraced scans (p. 38)
- [[parallel-terraced-scan]] (new) — Hofstadter's term: many parallel explorations, resources allocated by perceived success (p. 38)
- [[exploration-vs-exploitation]] (new) — balance of random exploration and focused use of information; shifts toward focus over time (p. 40)
- [[negative-selection]] (new) — thought to be a mechanism that kills or edits lymphocytes binding strongly to self (p. 30)
- [[meaning-as-fitness]] (new) — Mitchell's view that an event's meaning is what tells the organism how to respond, tied to survival (p. 41)

## Canonical instances
- [[immune-system-lymphocytes]] — random diversity, threshold activation, selection of B-cell daughters (pp. 28–30)
- [[ant-foraging-pheromone-trails]] — random search, trail reinforcement and evaporation (pp. 31–32)
- [[ant-task-allocation-gordon]] — Red Harvester ants shifting tasks by encounter rates (pp. 32–33)
- [[glycolysis-atp-feedback]] — ATP level slows or speeds glycolysis (p. 34)
- [[majority-classification-ca-particles]] — CA information processing described via particles (p. 25)
- [[artificial-immune-systems-and-ant-colony-optimization]] — computing inspired by these systems (p. 41)

## Bridges (candidates)
- [structural-analogy] Parallel terraced scan ↔ reinforcement learning / bandits: exploration versus exploitation — both shift effort toward promising options while still sampling others.
- [structural-analogy] B-cell activation threshold ↔ threshold models of cascades: action only when enough local signals pass a threshold.
- [metaphor] Ant colony as brain ↔ neural networks: simple units without a central controller yielding adaptive behavior.
- [structural-analogy] Pheromone reinforcement and evaporation ↔ positive and negative feedback in dynamical systems.

## Questions this raises
- Can a "high-level language" for biology be built, as particles were proposed for CAs? What would its compilers look like?
- If information is a distributed statistical pattern, how can we measure how much a colony or immune system "knows"?
- How does a system tune the balance of exploration and exploitation over time, and what happens when the balance is wrong (e.g., autoimmune failure)?
- If meaning is tied to fitness, what is the "who" that perceives it in a leaderless system?

## Reading notes
- Printed page = pdf page − 188 (pdf 210 = printed 22).
- Figures 12.1–12.4 (lymphocyte photo, receptor binding, B-cell activation, ant trail) appear on printed pp. 27, 29 and 33; they are illustrations, and the digest does not rely on them.
- The text of p. 34 reads "pryruvate"; this looks like a misprint of "pyruvate" (no page image of that page was available to confirm), and the digest writes "pyruvate".
- The chapter has no equations or exercises. The Toy example, Bridges and Questions are our own material, and the concept and instance ids are our labels.
