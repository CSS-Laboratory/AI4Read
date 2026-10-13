---
id: ashby-1956-cybernetics/ch14-amplifying
work: ashby-1956-cybernetics
unit: "14 Amplifying Regulation"
pages: 265–271
fields: [control-theory]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.1
verified: repaired
verifier_issues: 7
pipeline_version: 0.1
---
# Amplifying Regulation

## L0 — One line
Ashby argues that "amplifying" regulation means supplementation (adding output drawn from an abundant source), not magnification: if a regulator is built in stages, a small first regulator may lead to a much larger one, which the law of requisite variety does not prohibit.

## L1 — The gist (≤ 120 words)
Can regulation be amplified, as power can? Ashby starts from the power-amplifier. Two coupled stages each conserve energy, and an abundant reservoir supplies most of the output. He then argues that the law of requisite variety forbids direct, simple magnification of regulation but does not forbid supplementation. If a regulator is reached in stages, a small first regulator may lead to a much larger one. His examples are a thermostat, air-conditioners for many rooms, and the mammalian brain. In these, the added selection comes from other sources, such as the environment. He measures the amplification in bits of selection.

**Prerequisites:** variety and "selection" as amounts of information (bits, powers of 2); the regulator/disturbance setting and the law of requisite variety from the earlier chapters; conservation of energy.

## L2 — Key ideas
- An amplifier works by supplementation: a reservoir supplies most of the output, and the input contributes little or nothing to it (p. 265).
- Power-amplification is possible despite energy conservation because the process has two coupled stages, each conserving energy (pp. 265–266).
- The theoretician sees no real amplification; the practical man sees a very real one. Ashby says both are right (pp. 266–267).
- The quantity of design in a regulator can be measured as the amount of selection needed to make it (pp. 267–268).
- The law of requisite variety absolutely prohibits any direct and simple magnification, but not supplementation. If a regulator is built in stages, a small one may lead to a much bigger one (p. 268).
- Examples (mains stabiliser, thermostat, air-conditioners) show amplification. In the thermostat case it is about ×36 on a logarithmic scale. Amplification is not guaranteed in every case (pp. 268–270).
- The extra selection comes from other inputs, such as the manufacturer's design or the environment, which tells the machine the conditions without using the mechanic as a channel (p. 270).
- In mammals, the gene-pattern (the inherited pattern, a store of variety of limited capacity) builds a primary regulator R1, which develops the main regulator R2 in the cortex. Gene-pattern and environment together supply more design than the gene-pattern alone (pp. 270–271).

## L3 — Walkthrough

### 14/1. What is an amplifier? (pp. 265–266)
- An amplifier is a device that, given a little of something, emits a lot of it (sound, power, or money) (p. 265).
- **Supplementation** (meaning: adding from an abundant source) is the usual method. A generous reservoir holds what is to be emitted, and the input acts as controller of the flow from it. Rarely, an amplifier magnifies the input directly, like a projector lens (p. 265).
- In the power-amplifier (S.12/21, Fig. 12/21/1) the compressed air supplies most of the output power, and the input contributes little or nothing to it. The crane-driver's work goes into moving switch gear, not into lifting the load (p. 265).
- The process runs in two stages by two coupled systems. In stage 1 the operator moves point L against friction and pressure, and energy is conserved strictly. In stage 2 compressed air moves and lifts the weight at H, and energy is also conserved, because the lifting energy comes from the expanding air (p. 265).
- The coupling makes forces of 0, 1, 2… dynes at L correspond to 0, 1000, 2000… dynes (or some other multiple) at H. Without the two stages, the conservation of energy would make simple and direct amplification of power impossible (pp. 265–266).
- Sometimes the ratio matters, as in a radio amplifier, where it must be constant along the scale. In a crane, the input need only stay within a limit set by the driver's arm, and the output must be generously supplemented (p. 266).
- Ashby sets a design exercise: a "water-amplifier" giving 100x ml/sec from an input of x ml/sec (p. 266).

*Intuition note:* Amplifiers do not create power. The small stage-1 input steers a big flow from a store, and each stage still conserves energy.

### 14/2–14/3. Two points of view (pp. 266–267)
- **Theoretician (crane designer):** there is no real amplification. The power emitted does not exceed the total power supplied, and the operator succeeds by drawing on other energy sources such as coal (p. 266).
- **Practical man:** amplification is very real. It means loading ships quickly by a handle instead of slowly by hand. For a locomotive-sized load, lacking a power-amplifier might mean the job could not be done at all (p. 266).
- **Ashby:** both are right. Designers should know cranes are not really amplifiers; users should think of them as if they were (p. 267).
- For amplifying regulation, the designer must remember that he achieves only supplementation from an abundant source. When he comes to use the device, he should forget this and think of himself as a workman with power tools (p. 267).

### 14/4. Regulation and selection (pp. 267–268)
- Question: in "Designer → Regulator" with channel C between them, how much variety or information must C carry? (p. 267)
- **Selection** (meaning: picking one item out of a set of possible items) is essential to getting a regulator made. Three examples:
  1. The regulator $R:\ 1\to\beta,\ 2\to\alpha,\ 3\to\gamma$ (S.11/3) had to be selected from all possible transformations, which numbered 27. It is "made" by being unambiguously specified (p. 267).
  2. In S.13/12 a machine that might be a regulator was designed by selecting one value from the set of possible input-values (p. 267).
  3. Building one in hardware, like a water bath. Components and modes of assembly must be selected from the other possible ones (p. 268).
- The quantity of selection can be measured. Disputes about the measure can be settled by the method of S.13/11 (final paragraph) (p. 268).
- From S.13/18: if the regulator is reached by stages, the possibility exists that a small regulator at the first stage may lead to a much bigger one (larger capacity). The process then shows amplification (p. 268).
- **Result.** The law of Requisite Variety, like conservation of energy, absolutely prohibits any direct and simple magnification but does not prohibit supplementation (p. 268).

*Intuition note:* A regulator needs a certain amount of "design", measured in selections. Design cannot be multiplied by a simple magnifier. It can be added from other sources, which is why building in stages may pay off.

### 14/5. Examples (pp. 268–270)
- **Mains voltage.** Disturbances arrive hundreds of times a second, far more variety than Q can handle as a channel. From a catalogue (television set, mains stabiliser, frequency changer) he makes one selection from three, and the supply becomes stabilised. Regulation over a year involves far more selection than one from three, so an undoubted amplification has occurred. Ashby calls the case only somewhat extreme, chosen to show one end of the scale, and says the principle is unaltered (pp. 268–269).
- **Water bath.** Restoration is needed 100 times a day for a year, so 36,500 occasions, each a one-bit selection (raise or lower). The Grand Disturbance (S.13/8) has variety $2^{36500}$. Q probably could transmit this in the year, but finds it inconvenient (p. 269).
- A thermostat costing, say, 1000 bits uses the fact that the disturbance repeats (S.13/9). Selecting from 1000 bits then gives the correct selection from 36,500 bits. That is an amplification of about ×36 on the logarithmic scale (p. 269). (added step: $36500/1000 = 36.5$.)
- Amplification is not guaranteed. The practical man weighs the cost of making the machine against the cost of doing the job himself (p. 269).
- **Twenty men, 2000 rooms.** Controlling each room directly may be beyond them. As mechanics regulating air-conditioners they may succeed, so a regulation impossible in one stage may be possible in two, if conditions are suitable (pp. 269–270). The communication quantities could be measured, so any amplification could be shown beyond dispute (p. 270).
- **Source of supplementation:** in general, whatever supplies the other inputs. Here these are the factors in the machines' design and manufacture, and the environment, which tells the conditioner the temperature and humidity without using the mechanic as a channel (p. 270).
- A doctor who keeps the mechanics healthy might claim to be a third-level regulator. Many cases will probably not form a simple hierarchy (p. 270).

### 14/6. Amplification in the brain (pp. 270–271)
- The **gene-pattern** (the inherited pattern, treated as a store or channel of variety) has limited capacity. Survival goes especially to species that use it efficiently, directly or indirectly (p. 270).
- **Direct use:** the gene-pattern specifies the regulator itself, and the organism responds to each disturbance as it determined. Amplification does not occur from our present point of view, though some advantage is gained if disturbances recur frequently (S.13/9) (p. 270).
- **Indirect use:** the gene-pattern builds a regulator R1 whose action builds the main regulator R2, possibly through several levels. This allows large-scale supplementation (p. 270).
- **Homeostat (S.12/15):** part B, built as R1, makes part A stable with its needles central. A then acts as R2 against disturbances that would make the needles diverge. Ashby says nothing in principle separates this simple case from cases with complex R2 (p. 271).
- **Mammals:** the gene-pattern determines some fundamental regulators (R1) in the embryo brain, whose action is not immediately to the organism's advantage. From birth they develop in the cortex a vast regulatory mechanism (R2), which by adulthood has larger capacity than the gene-pattern could have produced directly (p. 271).
- Supplementation comes from random sources (as in S.12/15) and from the environment, which is forced to provide much of the determination of the organism's action. The adult shows more regulatory capacity than the gene-pattern alone could have determined. Higher animals that adapt by learning discovered the method long ago (p. 271).
- **Ashby asks (as questions):** may amplification be increased even further, and can present regulatory powers form a regulator of more than human capacity for society's ills? (p. 271)

*Intuition note:* The gene-pattern has limited capacity. Letting it start a first regulator that develops a larger one, with the environment supplying part of the determination, adds design the gene-pattern alone did not hold.

### 14/7. Amplifying intelligence (p. 271)
Only the opening is in these pages. Ashby says the book is meant as an Introduction and kept to that purpose for twelve chapters. The text breaks off at "the last two chapters, however, have developed the subject some-" (p. 271).

## Toy example (ours, not from the text)
Q must correct a heater once a day, up or down (1 bit per day), for 200 days. That is 200 bits, i.e. $2^{200}$ possible disturbance sequences. Suppose the disturbance repeats the same pattern, and a simple thermostat costs 20 bits of selection to build. Choosing among thermostat designs (20 bits) then fixes the correct response to all 200 days. Amplification on the log scale is $200/20 = 10$. If the thermostat cost 250 bits, the ratio would be $200/250 = 0.8$, so no amplification. This matches Ashby's remark that amplification is not guaranteed (p. 269).

## Concepts
- [[amplification-by-supplementation]] (new) — emitting more than is put in by drawing on an abundant reservoir, with the input acting as controller (p. 265)
- [[law of requisite variety]] — here: prohibits direct, simple magnification of regulation, not supplementation (p. 268)
- [[variety]] — number of distinguishable possibilities, here measured in bits (p. 269)
- [[selection-as-design]] (new) — picking one item from a set, with its amount measuring the design in a regulator (pp. 267–268)
- [[regulator-hierarchy-R1-R2]] (new) — a regulator R1 that builds or shapes a larger regulator R2 (p. 270)
- [[disturbance and noise]] — the "Grand Disturbance": all the disturbances over a period, with total variety (p. 269)

## Canonical instances
- [[crane-power-amplifier]] — two coupled stages; forces of 0, 1, 2… dynes at L correspond to 0, 1000, 2000… dynes (or some other multiple) at H (pp. 265–266)
- [[thermostat-36500-bits]] — 1000 bits of selection against 36,500, about ×36 (p. 269)
- [[air-conditioner-mechanics]] — twenty mechanics regulating machines that regulate 2000 rooms (pp. 269–270)
- [[mammal-gene-pattern-brain]] — gene-pattern → R1 → cortex R2, supplemented by the environment (p. 271)
- [[homeostat-R1-R2]] — part B as R1 stabilises part A, which then acts as R2 (p. 271)

## Bridges (candidates)
- [structural-analogy] Amplification by stages ↔ control theory: a low-power controller commanding a high-power actuator — both use a small signal to steer a large supply.
- [structural-analogy] R1 building R2 ↔ reinforcement learning: a learning process that builds a better policy than was specified at the start.
- [metaphor] Supplementation from the environment ↔ social science: institutions that gain capacity from information outside the designers.

## Questions this raises
- How would one measure, in bits, the "selection" in a real design such as a thermostat or a brain?
- When does the cost of building a first-stage regulator exceed the amplification gained?
- What is the source of the extra variety in each stage (random sources, environment, other designers)?
- Could a society-scale regulator, as Ashby asks, be built in stages, and what would supply its supplementation?

## Exercises worth doing
- Ex. (p. 266) — design a "water-amplifier" giving 100x ml/sec from x ml/sec; shows that a reservoir must supply the extra — difficulty: easy

## Reading notes
- Page labels give no printed number, but the text layer shows printed numbers: pdf 141 = p. 265; pdf 142 = pp. 266–267; pdf 143 = pp. 268–269; pdf 144 = pp. 270–271. Only the pdf 142 page image was available. Other pages were read from the text layer.
- Text-layer errors: "brains' supply" for mains' supply (p. 268), "2^36S00" for $2^{36500}$ (p. 269), "Rl" for R1 (p. 271), "see" for sec in the exercise (p. 266).
- The unit ends mid-sentence in 14/7 (p. 271).
