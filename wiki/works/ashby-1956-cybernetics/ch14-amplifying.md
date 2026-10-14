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
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Amplifying Regulation

## L0 — One line
A small amount of selection (design) can bring about a much larger amount of regulation if it is supplemented from other sources; the law of requisite variety forbids direct magnification, not supplementation.

## L1 — The gist (≤ 120 words)
Can a small regulator produce a much bigger regulator? Ashby starts from the power amplifier. It does not break conservation of energy, because it works in two coupled stages and the output is supplemented from a reservoir. He applies the same idea to regulation. A little selection at a first stage, such as making a thermostat, can fix a regulator that later handles far more variety than the selection itself carried. The extra variety comes from other sources, such as manufacturers and the environment. Ashby argues that mammals use this method: gene-pattern builds R1, and R1 builds R2, the cortex's regulatory machinery. He then asks whether it could be pushed further.

**Prerequisites:** variety measured in bits (logarithm base 2); the law of requisite variety; the idea of a regulator facing disturbances; conservation of energy; selection (choosing one item from a set of possibilities).

## L2 — Key ideas
- An amplifier works by supplementation: the input controls the flow from a reservoir, and the reservoir supplies most of the output (p. 265).
- Amplification is possible because the process is split into two stages. Energy is conserved strictly within each stage (pp. 265–266).
- Theorist and practical man disagree about whether amplification "really" occurs. Ashby says both are right: the designer knows it is supplementation, the user treats it as amplification (pp. 266–267).
- Making a regulator always needs selection. This selection can be measured in bits, and it can happen in stages (pp. 267–268).
- The law of requisite variety forbids direct, simple magnification of regulation. It does not forbid supplementation (p. 268).
- Examples: a mains stabiliser, a thermostat (about ×36 on the log scale), and twenty mechanics serving two thousand rooms. The amplification may be measured exactly, but it is not guaranteed (pp. 268–270).
- The supplementation comes from whatever supplies the other inputs, including the environment, which informs the machine and not the mechanic (p. 270).
- In higher animals the gene-pattern builds R1, R1 builds R2, and the environment adds design. So the adult has more regulatory capacity than the gene-pattern alone could fix (pp. 270–271).

## L3 — Walkthrough

**14/1 What is an amplifier?** An amplifier, if given a little of something, emits a lot of it (p. 265). It holds a generous reservoir and uses the input as controller of the flow from it. Rarely it magnifies the input directly (a projector lens does). Usually it supplements: in the power amplifier of Fig. 12/21/1, compressed air supplies most of the output power (p. 265).

The lifting of a weight at H by a force at L goes in two coupled stages (p. 265).
- Stage 1: the operator moves L against friction and pressure. Energy is conserved strictly.
- Stage 2: compressed air moves and lifts the load. Energy is again conserved, because it comes from the expansion of the air.
- The coupling is such that forces of 0, 1, 2, … dynes at L correspond to 0, 1000, 2000, … dynes at H (pp. 265–266).

Without the two stages, conservation of energy would forbid simple direct amplification (p. 265). Sometimes the ratio matters, as in a radio amplifier. In a crane it hardly matters. There the input must stay within the driver's strength, and the output must be supplemented generously, so that it much exceeds the input (p. 266).
Ex. (Ashby's): design a water-amplifier turning $x$ ml/sec in into $100x$ ml/sec out (p. 266).

*Intuition note:* The small input contributes little or nothing to lifting the load; it acts as controller of the flow from a big supply (the valve is our picture). Energy is not created; it is borrowed from the reservoir.

**14/2 Two points of view.** *The theoretician (crane designer):* there is no real amplification; the power out does not exceed the total power supplied. The operator "robs" coal and oil, like the boy who lifts big weights because his father lifts them for him (p. 266). *The practical man* (choosing quay machinery): abundant cheap power makes amplification real. It means the difference between quick, easy loading by a handle and slow, laborious loading by hand; for a very large load such as a locomotive, having no power-amplifier might mean the job could not be done at all (p. 266). **Ashby's verdict:** both are right. Designers should know cranes are not really amplifiers, and users should think of them as if they were (p. 267).

**14/3** During the designing (this chapter), Ashby says we must be clearly aware that the designer is really achieving only a supplementation, by robbing an easily available, abundant source. When he comes to use the result (a matter for the future), he should forget that fact and know only that he is like a workman with power-operated tools, able to do tasks impossible to the unaided workman (p. 267).

**14/4 Regulation and selection.** Question: in "Designer → Regulator" with channel C, how much variety must C carry (p. 267)? Recalling S.13/10 and S.13/18, Ashby notes that the quantity of design going into a regulator can be measured by the amount of selection needed, and that selection can in a sense be amplified (p. 267). To get a regulator made, selection is essential. He gives three examples (pp. 267–268).
- The regulator R of S.11/3, $\downarrow\,\beta\,\alpha\,\gamma$ for inputs 1, 2, 3, is picked out from 27 possible transformations (p. 267).
- A machine, which might be a regulator, is "designed" by selecting one value from the set of possible input-values, as in S.13/12 (p. 267).
- A regulator is built in hardware, such as a water bath. Components and ways of assembling them must be selected. The amount of selection can be measured, and disputes are settled by the method of S.13/11 (p. 268).

If selection can occur in stages (S.13/18), a small regulator at the first stage may lead to a much bigger one at the end. If that happens, the process shows amplification (p. 268). **Conclusion:** the law of requisite variety, like conservation of energy, "absolutely" prohibits direct simple magnification, "but it does not prohibit supplementation" (p. 268).

*Intuition note:* Selection is the "input" to be counted in bits. A little of it, at a first stage, may fix a machine that then deals with far more variety than the selection itself carried.

**14/5 Examples.** (p. 268) (i) *Mains voltage:* fluctuations arrive hundreds of times a second, far beyond Q's capacity as a channel. From a catalogue (television set, mains stabiliser, frequency changer) Q makes one selection out of three. The result is a stabilised supply. Regulating a whole year involves far more selection than one from three, so Ashby calls this an undoubted amplification. The supplementation is blatant, but no more than the crane-driver's dependence on a power supply (pp. 268–269).

(ii) *Water bath:* restorations are needed 100 times a day for a year. That is 36,500 corrections, each a one-bit choice (raise or lower). The Grand Disturbance (S.13/8) then has variety $2^{36500}$ (p. 269). Suppose Q can make a thermostat for 1000 bits. Because the disturbance repeats (S.13/9), selecting from 1000 bits brings the correct selection from 36,500 bits. That is an amplification of about ×36 on the logarithmic scale (p. 269). Ashby notes there is "not necessarily any amplification" (p. 269): the practical man, before building a machine, always makes at least an intuitive assessment of the balance between the cost of making the machine and the cost of doing the job himself (p. 269).

(iii) *Twenty men, 2000 rooms:* direct control of every room may exceed the twenty men's capacity. If they become mechanics who regulate air-conditioners, and their regulation suffices to keep the conditioners in control, the regulation that could not be done in one stage may, if conditions are suitable, be possible in two (pp. 269–270). The channel capacities could be measured to any desired accuracy, so if amplification had actually occurred, its reality could be demonstrated beyond dispute (p. 270).

*Where does the supplementation come from?* In general, from whatever supplies the other inputs. Here these are the other factors in the design and manufacture of the machines, and the environment. The environment tells the conditioner, not the mechanic, the temperature and humidity at each moment (p. 270). There is no reason to stop at two levels. A doctor who keeps the mechanics healthy could claim to be a regulator at the third level. Many cases will probably not form a simple hierarchy (p. 270).

**14/6 Amplification in the brain.** (p. 270) Ashby says we can now understand quantitatively why the indirect method has proved superior, being the method of organisms with the most powerful regulatory resources: it allows amplification. The gene-pattern is a store or channel for variety of limited capacity. Species that use it efficiently are favoured in survival.
- *Direct use:* the gene-pattern specifies the regulator, and the organism responds to each disturbance as determined. No amplification occurs in the sense used here, though some advantage exists if disturbances recur often (p. 270).
- *Indirect use:* the gene-pattern builds R1, which builds the main regulator R2, possibly through several levels. This opens the possibility of large-scale supplementation (pp. 270–271).

The homeostat of S.12/15 is an example. Part B becomes R1. It makes Part A stable, and A then acts as regulator R2 against disturbances. This R2 is very simple, but in principle nothing separates it from complex cases (p. 271).

Mammals: the gene-pattern acts on the embryo brain to develop fundamental regulators R1 at birth. Their action is not immediately to the organism's advantage. From birth they develop in the cortex a vast regulatory mechanism R2, by adulthood a much better regulator (of larger capacity) than the gene-pattern could directly produce (p. 271). The supplementation comes from random sources (as in S.12/15) and from the environment, which is forced to provide much of the determination of how the organism acts. So design from the gene-pattern is supplemented by design from the environment (p. 271). The adult thus shows more regulatory capacity than the gene-pattern alone could have determined. Higher animals that adapt by learning "discovered the method long ago" (p. 271).

**Author's question:** can amplification be increased still further, to build a regulator of much more than human capacity for the ills of society? (p. 271)

*Intuition note:* In the mammal example, the gene-pattern does not fix the adult's regulation directly. It builds regulators that develop a cortex shaped by the environment. The world's information supplies the rest of the "design".

**14/7 Amplifying intelligence** begins on p. 271. Only its opening sentences are in these pages, so it is not digested here.

## Toy example (ours, not from the text)
Assume a heater must be switched on or off, one bit per decision, 4 times a day for 30 days. That is 4 × 30 = 120 one-bit choices, so the variety is $2^{120}$, or 120 bits. Suppose building a thermostat needs only 12 bits of selection (assumed). Then 12 bits of selection fixes a regulator that deals with 120 bits of disturbance. The amplification on the log scale is 120 / 12 = 10. Ashby's thermostat has the same form: 36,500 / 1000 ≈ 36 (p. 269). If the thermostat needed 150 bits, 120 / 150 = 0.8 < 1, and there would be no amplification in these terms, so building it would probably not pay. This matches Ashby's remark that amplification is not guaranteed (p. 269).

## Concepts
- [[amplification-of-regulation]] (new) — a small selection at a first stage leads to a much larger regulator; measured on the log scale (p. 268)
- [[supplementation]] (new) — adding output or variety taken from an abundant outside source, not magnifying the input (p. 265)
- [[selection-as-design]] (new) — distinguishing one item from a set of alternatives; its quantity is measured in bits (p. 267)
- [[variety]] — the number of possible states, here counted in bits; e.g. $2^{36500}$ (p. 269)
- [[law of requisite variety]] — here: forbids direct, simple magnification of regulation but not supplementation (p. 268)
- [[multi-stage-regulation]] (new) — a regulator R1 builds R2, possibly through several levels (p. 270)
- [[disturbance and noise]] — here: the Grand Disturbance (S.13/8), whose variety in the water-bath example is $2^{36500}$; its definition is in an earlier chapter (p. 269)

## Canonical instances
- [[power-amplifier-crane]] — two coupled stages, each conserving energy (pp. 265–266)
- [[thermostat-water-bath]] — 1000 bits of design against 36,500 bits of disturbance (p. 269)
- [[mains-stabiliser-catalogue]] — one choice out of three yields a stabilised supply (p. 268)
- [[air-conditioning-mechanics]] — twenty mechanics regulating machines that regulate 2000 rooms (pp. 269–270)
- [[gene-pattern-to-cortex]] — gene-pattern → R1 → R2, with the environment supplementing (p. 271)
- [[homeostat]] — Part B is R1, Part A becomes R2 (p. 271)

## Bridges (candidates)
- [structural-analogy] two-stage power amplification ↔ control theory: a small control signal modulating a large power flow — same split of control and power.
- [metaphor] gene-pattern building R1 which builds R2 ↔ learning to learn: a design that builds the learner.
- [structural-analogy] thermostat as stored design against repeating disturbances ↔ feedforward: fixed design used against recurrent disturbance.

## Questions this raises
- How exactly is the "amount of selection" in a design measured, and who settles disputes about it (S.13/11)?
- What limits how many levels of regulation can be stacked (R1 → R2 → R3)?
- If the supplementation comes from the environment, what happens when the environment supplies misleading information?
- Could the method in 14/6 be used to build a regulator for society?

## Exercises worth doing
- Ex. in 14/1 (p. 266) — design a water-amplifier from $x$ ml/sec to $100x$ ml/sec; shows supplementation versus magnification — difficulty: medium

## Reading notes
- Page numbers: the PDF pages are spreads. pdf 141 = p. 265 (printed number visible at the foot of the text), pdf 142 = pp. 266–267, pdf 143 = pp. 268–269, pdf 144 = pp. 270–271. Page images were available only for pp. 266–267. The other pages were read from the text layer.
- Text-layer readings (pp. 265 and 268–271 had no image, so they are not checked against the print): "236S00" is $2^{36500}$ (superscript lost). "brains' supply" in 14/5 is evidently "mains' supply". "Rl" means R1. "ml/see" is printed as such in the page image of p. 266, so it is a misprint in the source (for ml/sec), not a text-layer error.
- The unit stops in the opening of 14/7 (p. 271). That section is not covered.
- Terms such as "Grand Disturbance" and the references S.13/8, S.13/9, S.13/11 and S.13/18 point to earlier chapters, which are not in these pages. This unit only uses them.
