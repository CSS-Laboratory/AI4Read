---
id: ashby-1956-cybernetics/index
work: ashby-1956-cybernetics
type: work-map
units: [ashby-1956-cybernetics/ch02-change, ashby-1956-cybernetics/ch03-determinate, ashby-1956-cybernetics/ch04-machine, ashby-1956-cybernetics/ch05-stability, ashby-1956-cybernetics/ch06-black, ashby-1956-cybernetics/ch07-quantity, ashby-1956-cybernetics/ch08-transmission, ashby-1956-cybernetics/ch09-incessant, ashby-1956-cybernetics/ch10-regulation, ashby-1956-cybernetics/ch11-requisite, ashby-1956-cybernetics/ch12-error, ashby-1956-cybernetics/ch13-regulating, ashby-1956-cybernetics/ch14-amplifying]
---

# Ashby, W. R. (1956). *An Introduction to Cybernetics*. Chapman & Hall, London.

## In one paragraph
Ashby treats cybernetics as the study of how machines behave, whatever they are made of. He first makes "change" exact as a transformation of states. He then builds up the machine with input, stability, and the black box. Next he measures "what could happen" as variety and follows it through coding and transmission. The book's centre is regulation. Survival means keeping essential variables inside a permitted set. By the law of requisite variety, only variety in the regulator can absorb variety in the disturbances. Ashby then asks how real regulators work, through error control. He also asks how they can be made, since making one is itself selection. A small amount of selection can bring a large amount of regulation if it is supplemented from other sources. Throughout, he uses only school-level mathematics.

## The path through the work
- [[ashby-1956-cybernetics/ch02-change]] — Cybernetics studies the possible behaviours of any machine, whatever it is made of, and its first tool is "change" made exact as a transformation: a table saying what each state becomes.
- [[ashby-1956-cybernetics/ch03-determinate]] — A determinate machine is defined as a system whose successive states follow a closed, single-valued transformation, so that its whole future behaviour can be computed from one starting state.
- [[ashby-1956-cybernetics/ch04-machine]] — A machine that outside conditions can act on is a set of transformations selected by a parameter, and machines are coupled by making one machine's parameters depend on another's states.
- [[ashby-1956-cybernetics/ch05-stability]] — "Stability" is shorthand for a compound of precisely defined facts (equilibrium, stable sets, return after a specified disturbance), and Ashby wants us to think of those facts rather than the word.
- [[ashby-1956-cybernetics/ch06-black]] — With given inputs and outputs, everything an experimenter can learn about a sealed system can be got from the recorded sequence of (input state, output state) pairs, so he can learn its pattern of behaviour (up to isomorphism) but not its unique inner mechanism, and simplified or partial views of a large system depend on the observer.
- [[ashby-1956-cybernetics/ch07-quantity]] — Cybernetics studies the set of what could happen, measures its size as "variety" (counted in bits), and links laws of nature, objects, predictability and learning to constraint, meaning that a set is smaller than it might be.
- [[ashby-1956-cybernetics/ch08-transmission]] — In a determinate machine, a set of possibilities passes orderly from system to system through coding; it is lost only when the coding merges distinct messages, and it moves through a channel at a rate bounded by the channel's number of states.
- [[ashby-1956-cybernetics/ch09-incessant]] — When variety must be carried on indefinitely, a useful model is the stochastic (Markov) transformation, in which each next state has a constant probability, and Shannon's entropy then measures its variety per step, so that channel capacity, redundancy, noise and error-free coding can be stated quantitatively.
- [[ashby-1956-cybernetics/ch10-regulation]] — Survival can be stated as keeping the states of an organism (often, its essential variables) within a chosen set, and an essential feature of a good regulator is that it blocks the flow of variety from disturbances to the essential variables.
- [[ashby-1956-cybernetics/ch11-requisite]] — When no outcome repeats within a column of the game table, a regulator can reduce the variety (number of distinct states) of outcomes caused by disturbances only by having variety of its own: in logarithmic form, $V_O \ge V_D - V_R$.
- [[ashby-1956-cybernetics/ch12-error]] — When a regulator learns about disturbances only through their effect on the essential variables, it cannot be perfect (in the sense of ch. 11), but when errors lie on a continuous scale it can still regulate usefully, and the scheme holds whether its machinery is determinate or probabilistic ("hunt and stick").
- [[ashby-1956-cybernetics/ch13-regulating]] — In a very large system the difficulty of regulation usually lies in the variety of the disturbances, not in size, so finding a constraint (a restriction on which disturbances occur) can make regulation possible, and making a regulator is itself a measurable act of selection.
- [[ashby-1956-cybernetics/ch14-amplifying]] — A small amount of selection (design) can bring about a much larger amount of regulation if it is supplemented from other sources; the law of requisite variety forbids direct magnification, not supplementation.

## Big ideas across units
- **Behaviour as transformation.** A machine is defined by what each state becomes, not by what it is made of. This starts with tables, graphs and powers, becomes the determinate machine, and is extended with parameters (input) and probabilities. Units: ch02, ch03, ch04, ch09, ch12.
- **Stability and equilibrium made exact.** Basins and cycles in the kinematic graph lead to a precise definition of stability, which is then reused for survival and for the regulator's goal. Units: ch02, ch03, ch05, ch10, ch12.
- **Coupling and feedback.** Machines are joined through parameters. Feedback is present when two parts affect each other, and the whole is not fixed by the parts alone. Part and whole share equilibria, and the error-controlled regulator closes the loop. Units: ch04, ch05, ch06, ch08, ch12.
- **What the observer can know.** The black box gives pattern but not unique mechanism. Models are homomorphisms. "Emergence" and "memory" depend on how much the observer can see. A real system is a variable list chosen by the investigator. Units: ch03, ch04, ch06, ch09.
- **Variety and constraint.** Variety (counted in bits) measures a set of possibilities. Constraint is what makes prediction, law and learning possible, and variety decays in an isolated machine. Units: ch07, ch08, ch09, ch10, ch11, ch13.
- **Variety in transmission and communication.** Coding, channel capacity, entropy and noise show how variety moves. Regulation is later read as a communication problem. Units: ch08, ch09, ch11.
- **The regulation law and its consequences.** The regulator blocks variety from disturbance to essential variables. Only variety can destroy variety. The error-controlled regulator cannot be perfect but works on a continuous scale. Units: ch10, ch11, ch12, ch13.
- **Selection, design and supplementation.** Making a regulator is selection, measurable in bits and quicker by groups. Supplementation lets a little selection yield more regulation, via natural selection, gene-pattern and R1 building R2. Units: ch10, ch13, ch14.

## How to read it
- **Essential.** The catalog's focus is ch04 (The Machine with Input, including feedback), ch06, ch07, ch10, ch11 and ch12. Ch11 is the centre of the book.
- **Foundations to read first.** Ch02, ch03 and ch05 supply the vocabulary (transformation, state, closure, basin, stability). Ch04 prerequisites include these.
- **Dependencies.** Ch10 and ch11 need variety from ch07. Ch12 needs ch11 (the outcome table), the determinate machine, equilibrium and basin. Ch13 needs variety and the law of requisite variety. Ch14 needs ch13's selection measured in bits plus the law.
- **Can be skimmed on a first pass.** Ch08 and ch09 are technical on coding, Markov chains and Shannon's results. The regulation chapters (ch10 and ch11) need mainly the idea of variety from ch07. The Markov material in ch12 ("hunt and stick") uses ch09's idea of transition probabilities. Ch13 and ch14 continue the regulation theme and are best read after ch11–12.

## Concepts introduced
Concept ids are given as they appear in the units, each with the unit where it first appears. Where two ids look like variants of the same idea, they are kept under the first form, with the variant in parentheses.

- ch02: [[transformation]], [[operand-operator-transform]], [[closure]], [[single-valued-one-one-many-one]], [[identity-transformation]], [[transformation-matrix]], [[power-and-product-of-transformations]], [[kinematic-graph]], [[basin]], [[state]], [[stability]], [[black box]] (variants: [[black-box]], defined in ch06)
- ch03: [[determinate-machine]], [[transformation-as-machine]], [[trajectory]], [[canonical-representation]], [[vector-state]], [[phase-space]], [[system-as-variable-list]], [[integrating-a-transformation]], [[linearization]]
- ch04: [[parameter]], [[transducer]], [[transient]], [[coupling]], [[feedback]], [[immediate-effect]], [[ultimate-effect]], [[reducibility]], [[variety]], [[very-large-system]], [[statistical-specification]], [[self-locking-property]], [[breeding-property]]
- ch05: [[invariant]], [[state-of-equilibrium]], [[cycle]], [[stable-set]], [[disturbance-and-noise]] (variant: [[disturbance and noise]], ch10), [[neutral-equilibrium]], [[negative-feedback]] (variant: [[negative (balancing) feedback]], ch12), [[positive-feedback]], [[power-of-veto]], [[homeostasis]], [[topological-description]]
- ch06: [[protocol]], [[absolute-system]], [[inaccessible-state]], [[diagram-of-immediate-effects]], [[isomorphism]], [[homomorphism]], [[lattice-of-simplifications]], [[model]], [[emergence]], [[observability]], [[memory-as-observer-relation]], [[eigenvalues and modes]]
- ch07: [[bit]], [[set-of-possibilities]], [[constraint]], [[independence-of-components]], [[degrees-of-freedom]], [[redundancy]], [[decay-of-variety]], [[law-of-experience]]
- ch08: [[coding]], [[one-one-transformation]], [[inverter]], [[delay]] (variant: [[delay (dead time)]], ch12), [[channel-capacity]], [[dominance]], [[replicates]], [[interference]]
- ch09: [[stochastic-transformation]], [[transition-probability-matrix]], [[probability-as-frequency]], [[markov-chain]], [[markov-equilibrium]], [[recoding-to-markov-form]], [[entropy]], [[noise-relative-to-recipient]], [[distortion]], [[equivocation]], [[shannon-coding-theorem]], [[error-free-transmission-theorem]]
- ch10: [[regulator-between-D-and-E]], [[essential variables]], [[passive vs active regulation]], [[autocatalytic property]]
- ch11: [[law of requisite variety]], [[plant]], [[regulation-as-communication]], [[control-via-regulation]], [[acceptable-set]], [[vector-valued-variables]]
- ch12: [[error-controlled-regulator]], [[open loop vs closed loop]], [[feedforward]], [[reference (set point)]], [[error signal]], [[markovian-machine]], [[hunt-and-stick]], [[vetoer]], [[power-amplifier]], [[pay-off-matrix]]
- ch13: [[repetitive disturbance and grand disturbance]], [[design as selection]] (variant: [[selection-as-design]], ch14), [[quantity of selection]], [[selection by groups (dichotomy)]], [[supplementation of selection]] (variant: [[supplementation]], ch14), [[regulation by stages]] (variant: [[multi-stage-regulation]], ch14)
- ch14: [[amplification-of-regulation]]
