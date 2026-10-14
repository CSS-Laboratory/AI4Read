---
id: mitchell-2009-guidedtour/ch03-information
work: mitchell-2009-guidedtour
unit: Chapter 3 — Information
pages: pdf 63–80 (printed page numbers not visible)
fields: [complex-systems]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Information (Mitchell, ch. 3)

## L0 — One line
Entropy, first a physics idea about energy, was turned by Boltzmann into a function of the number of microstates behind a macrostate and by Shannon into a measure of a message source's information, which many complex-systems scientists use to talk about order and disorder.

## L1 — The gist (≤ 120 words)
Complex systems seem to create order from disorder, so we need a precise way to measure order. Mitchell tells how "information" became precise. The Second Law says entropy (energy that cannot be turned into more work) increases. Maxwell's demon seemed to break it by sorting molecules for free. Szilard, then Landauer and Bennett, argued that the demon's information handling, and in the end its memory erasure, pays the entropy cost. Boltzmann defined entropy as a function of the number of microstates (exact molecular arrangements) behind a macrostate (a type of arrangement). Shannon adapted this idea to message sources, ignoring meaning. Information theory has many applications. Its use in defining complexity is central but controversial.

**Prerequisites:** high-school notions of force, energy, heat; counting combinations; basic probability.

## L2 — Key ideas
- Many complex-systems scientists use information to characterize order, disorder, complexity and simplicity (pdf 63).
- Entropy measures energy that cannot be converted into more work. The Second Law says that in an isolated system entropy increases to a maximum and never decreases on its own unless an outside agent works to decrease it (pdf 65–66).
- Maxwell's demon seems to lower entropy without work. Maxwell took this to show the Second Law is statistical. Szilard linked entropy to information (pdf 67–69).
- Landauer and Bennett: measurement can in principle be free, but erasing memory necessarily raises entropy. Some physicists still doubt this solution (pdf 71).
- Boltzmann's statistical mechanics: macro properties emerge from statistics of many molecules, so it gives only probable behavior, which Boltzmann argued is right "virtually all the time" (pdf 72–73).
- A macrostate can arise from many microstates. Boltzmann entropy depends on how many (pdf 75–76).
- Shannon defined a source's information from the possible messages it could send, ignoring meaning. It has sometimes been described as "average surprise" (pdf 77–79).
- Information theory is applied widely. Whether it has had much reverse impact on physics is controversial (pdf 80).

## L3 — Walkthrough

### Opening and "What Is Information?" (pdf 63–64)
- Self-organization (army-ant bridges, synchronous fireflies, markets, stem-cell organs) means order arising from disorder, against the usual decay toward disorder or entropy. Explaining it is called the "holy grail" of complex systems science. First we must say what "order" and "disorder" mean (pdf 63).
- Cohen says complex systems "sense, store, and deploy more information than do simple systems"; Beinhocker says evolution can work in any system with the right information processing and storage; Gell-Mann says complex adaptive systems resemble one another in how they handle information (pdf 63–64).
- "Information" is used loosely (newspapers, the Internet, neuron molecules). Precise mathematical definitions of information and computation date only from the twentieth century. They began with a puzzle about a "demon" (pdf 64).

### Energy, Work, and Entropy (pdf 65–66)
- Energy = a system's potential to do work. Physics defines work as force times distance moved in the force's direction (pdf 65).
- Pushing a car: energy used equals work done plus energy turned into heat (friction, body warming). This heat loss is measured by entropy, which is a measure of the energy that cannot be converted into additional work (pdf 65).
- Laws for isolated systems (no energy exchange with outside) (pdf 65–66):
  - **First law:** energy is conserved; it can change form but is never created or destroyed.
  - **Second law:** entropy always increases until it reaches its maximum, and never decreases on its own unless an outside agent works to decrease it.
- Examples: rooms do not tidy themselves; no one has found a way for a fridge to power itself from its own waste heat; perpetual motion machines are a myth (pdf 66).
- The second law defines the "arrow of time": the future is the direction of increasing entropy. It is the only fundamental law that distinguishes past from future. Particle interactions look legitimate when a film is run backward (reversible); fridge heat film does not (irreversible). Rothman: why this is so is "perhaps the greatest mystery in physics" (pdf 66–67).

*Intuition note:* Every energy conversion leaks some unusable heat. The second law adds that disorder is not undone on its own: someone has to do work to turn disorder into order.

### Maxwell's Demon (pdf 67–71)
- **Setup (Maxwell, 1871):** a box split by a wall with a door. A tiny demon watches molecules. He lets fast ones pass right-to-left and slow ones left-to-right, closing the door otherwise. Result: fast molecules left, slow right, so entropy decreases (pdf 67–68).
- The door is assumed massless and frictionless, so opening it costs negligible work. **Maxwell's answer:** no work is done, only "intelligence" is used (pdf 68–69).
- **Maxwell's own conclusion:** the second law is a statistical effect for large collections of molecules, not a strict law at the individual-molecule scale (pdf 69).
- **Other physicists:** the law must be inviolate, so some subtle work must be hidden. No satisfactory solution came for almost sixty years (pdf 69).
- **Szilard (1929):** the demon's act of obtaining information by measurement is the missing work. One bit (the answer to a yes/no, here fast/slow, question) costs energy and must produce at least as much entropy as the sorting removes. So box + molecules + demon obey the second law. This was the first link between entropy and information (pdf 69).
- Mitchell suggests Maxwell may have missed this because people tended to see physical and mental processes as completely separate. The link became clear in the twentieth century, starting with the observer's role in quantum mechanics (pdf 70).
- Brillouin and Gabor extended Szilard's work. Many in the 1950s and later believed Brillouin had finished off the demon (pdf 70).
- **Bennett (1980s):** there are ways to observe and remember a molecule's speed without raising entropy. This underlies reversible computing: in theory any computation can be done without expending energy (pdf 70–71).
- **Landauer (1960s), used by Bennett:** it is erasing memory, not measuring, that necessarily raises entropy. Erasure is irreversible. The demon's memory must eventually be erased, and the heat produced raises entropy by exactly the amount the sorting lowered it (pdf 71).
- Some physicists do not accept this; the demon "remains controversial". Its resolutions founded information theory and the physics of information (pdf 71).

*Intuition note:* On the Szilard and Landauer–Bennett account (still disputed by some physicists), the paradox is resolved by counting the demon's information handling as a physical cost. Szilard put the cost in measurement. Landauer and Bennett moved it to erasure.

### Statistical Mechanics in a Nutshell (pdf 71–73)
- Clausius (1865) defined entropy when heat was thought a fluid. Boltzmann's view: heat is molecular motion (kinetic energy). He developed statistical mechanics (pdf 71–72).
- Statistical mechanics: large-scale properties (heat) emerge from microscopic ones (motions of trillions of molecules). Tracking every molecule is impossible in practice and, per quantum mechanics, in principle. So it predicts average positions and velocities of large ensembles (pdf 72–73).
- Three levels: classical mechanics (every molecule, Newton), thermodynamics (macro laws, no molecules), statistical mechanics (bridge between them) (pdf 73).
- The approach gives only probable behavior. Statistical mechanics allows a very small chance that air molecules all fly into one corner. Nothing in Newton's laws forbids this, it is just incredibly unlikely. Boltzmann argued that with enough entities it is right "virtually all the time" (pdf 73).
- Many colleagues rejected both a law holding only "virtually all" the time and the reality of molecules. Some speculate the rejection contributed to his 1906 suicide. His ideas were generally accepted only years after his death (pdf 73).

### Microstates and Macrostates (pdf 74–76)
- **Microstate:** exact positions and velocities of all molecules at an instant. The most probable kind has molecules spread uniformly. Reason (Boltzmann): far more microstates are spread out than clumped (pdf 74).
- **Macrostate:** a type of microstate (e.g. "uniformly spread, we can breathe"). It can correspond to many microstates. Temperature is a macrostate (many velocity patterns average to the same temperature) (pdf 75).
- **Slot machine (fig. 3.2):** three pictures, each with 5 options, give 125 microstates: 5 are "all the same—you win", 120 are "not all the same—you lose". The losing macrostate has the higher Boltzmann entropy. With fifty quadrillion pictures, "all same" has probability near zero (pdf 74–76).
- Boltzmann read the second law as: an isolated system is more likely to be in a more probable macrostate. This sounds like a tautology (a statement true by its own wording) but introduced probability, which was revolutionary then (pdf 75).
- **Boltzmann entropy** of a macrostate is a function of the number of microstates giving that macrostate. Unless work is done, it rises to the highest-entropy macrostate. Under many conditions it is equivalent to Clausius's definition (pdf 75–76).
- The equation is on his tombstone (fig. 3.3). The text does not write it out (pdf 76).

*Intuition note:* "Disorder" means a macrostate with very many microstates. Systems drift toward it because it is overwhelmingly more likely, not because of a mysterious force.

### Shannon Information (pdf 76–80)
- Thermodynamics was driven by steam engines; Shannon's work by telegraph and telephone. At Bell Labs (AT&T) the problem was sending signals faster and more reliably (pdf 76–77).
- Shannon's 1948 paper "A Mathematical Theory of Communication" gave a narrow definition of information. His theorem gives the maximum transmission rate over a channel even with noise, the **channel capacity** (pdf 77).
- A source sends messages to a receiver. The definition ignores meaning and counts only how often each possible message is sent (pdf 77–78).
- By analogy with Boltzmann, a source (macrostate) has information as a function of the number of possible message ensembles (microstates). **Nicky** says only "da": one possible microstate, information zero. **Jake** has a large vocabulary: many possible microstates, so higher information (pdf 79).
- Shannon defined information content as the entropy of the message source ("Shannon entropy"), nearly identical to Boltzmann's. It has sometimes been characterized as the receiver's "average amount of surprise", meaning uncertainty about what comes next (pdf 79).
- A message can be a letter, word, sentence or one bit. Entropy depends on message probabilities, not meaning (pdf 79–80).
- Applications: coding theory (compression, reliable transmission: phones, networks, GPS), cryptography, bioinformatics, language, music, psychology, statistical inference, AI (pdf 80).
- It is controversial whether information theory has had much reverse impact on physics. Pierce (1961): marrying communication theory and physics was "more interesting than fruitful". New approaches such as quantum information theory are beginning to be fruitful. Later chapters use entropy, mutual information and similar notions in defining complexity, controversially (pdf 80).

*Intuition note:* A source with no uncertainty carries no information. The more different messages it might send, the more each message tells you.

## Toy example (ours)
Three fair coins stand in for the slot machine. Each coin is H or T, so there are $2\times2\times2=8$ microstates (added step).
- Macrostate "number of heads": 0 heads → 1 microstate (TTT); 1 head → 3 (HTT, THT, TTH); 2 heads → 3; 3 heads → 1. Total $1+3+3+1=8$.
- "1 head" has 3 microstates and "3 heads" has 1, so Boltzmann's way of counting gives "1 head" the higher entropy and makes it more probable: $3/8$ against $1/8$.
- Nicky-style source: sends only "H". Possible length-3 messages: 1. Information zero.
- Jake-style source: sends H or T freely. Possible length-3 messages: 8. Higher information.
- This only counts possibilities. Shannon's exact formula is not given in this unit.

## Concepts
- [[entropy]] (new) — in physics, energy unavailable for more work; in Boltzmann's sense, a function of the number of microstates behind a macrostate (pdf 65, 75)
- [[second-law-of-thermodynamics]] (new) — in isolated systems entropy increases to a maximum and never decreases on its own unless an outside agent works to decrease it (pdf 66)
- [[arrow-of-time]] (new) — the second law, uniquely among fundamental laws, distinguishes past from future (pdf 66)
- [[microstate-macrostate]] (new) — exact detailed state versus a type of state that many microstates can realize (pdf 74–75)
- [[emergence]] — large-scale properties like heat arise from microscopic motions (pdf 72)
- [[shannon-information]] (new) — information of a source from its possible messages and their probabilities; meaning ignored (pdf 78–79)
- [[bit]] (new) — information from the answer to a yes/no question (pdf 69)
- [[channel-capacity]] (new) — maximum transmission rate over a channel, even with noise (pdf 77)
- [[landauer-erasure-principle]] (new) — erasing memory, not measuring, necessarily increases entropy (pdf 71)

## Canonical instances
- [[maxwells-demon]] — apparent entropy decrease; led to information-entropy link (pdf 67–71)
- [[slot-machine-microstates]] — 125 microstates, 5 win and 120 lose (pdf 74–76)
- [[nicky-jake-phone-calls]] — zero versus high Shannon information (pdf 79)
- [[air-molecules-in-corner]] — improbable but not forbidden event (pdf 73)

## Bridges (candidates)
- [structural-analogy] Boltzmann entropy (microstate counts) ↔ Shannon entropy of a source (possible message sets) — author calls definitions "nearly identical" (pdf 79).
- [structural-analogy] Statistical mechanics (macro from micro statistics) ↔ complex systems: emergence of macro patterns from many micro interactions (pdf 72).
- [metaphor] Landauer's erasure cost ↔ the cost of forgetting in information-processing living systems — speculative; this unit does not make this link.

## Questions this raises
- What is Shannon's exact entropy formula, and how does it match Boltzmann's counting?
- If entropy always rises, how can self-organization occur (opening question, pdf 63)?
- Why is the second law the only time-asymmetric fundamental law (pdf 66–67)?
- Can information measures define complexity, and why is that controversial (pdf 80)?

## Reading notes
- The page labels show no printed numbers and the page images checked show none, so all references use pdf numbers.
- Figure 3.3 (image, pdf 76) shows a tombstone inscription that appears to read "S = k log W". The text itself does not write it.
- Page images were checked for pdf 68, 75, 76 and 79. The text layer matched them. No misprints found.
- Chapter title and epigraph (Eddington) are on pdf 63.
