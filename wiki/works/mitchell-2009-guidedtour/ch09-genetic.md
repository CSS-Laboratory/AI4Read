---
id: mitchell-2009-guidedtour/ch09-genetic
work: mitchell-2009-guidedtour
unit: Chapter 9 — Genetic Algorithms
pages: 1–13 as labelled (the unit as supplied continues to pdf 180; see Reading notes)
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
# Genetic Algorithms

## L0 — One line
A genetic algorithm "breeds" candidate solutions by letting fitter ones become parents of recombined, occasionally mutated children, and in Mitchell's robot example it found a strategy that works very well even though it is hard to see why from the strategy's code.

## L1 — The gist (≤ 120 words)
Holland wondered whether programs could be "bred" like horses or corn. His genetic algorithm (GA) keeps a population of candidate solutions, each scored by a fitness function (a measure of how well it does the task). Fitter ones are more likely to become parents. Children come from crossover (mixing parts of two parents) and occasional mutation (random changes). In Mitchell's example, a GA evolved a control strategy for a soda-can-collecting robot. It scored about 483 per session, against about 346 for a hand-made strategy; the maximum is about 500. Its genome (its string of numbers) was hard to interpret, and one of its tricks is reported as never having occurred to the author.

**Prerequisites:** probability and random choice; averages; powers ($3^5$); a string as an ordered list of symbols.

## L2 — Key ideas
- Von Neumann wanted self-reproducing programs that mutate and compete. He died before working on it, and others took it up (pdf 161). Holland, who was inspired by breeding, proposed genetic algorithms in his 1975 book (pdf 162).
- A GA takes a population and a fitness function as input. It repeats: score, select parents, recombine with some chance of mutation, replace the population (pp. 1–2).
- For the robot Robby, a strategy is a table giving one of seven actions for each of 243 possible situations. The GA evolves the list of 243 actions (pp. 5–7).
- In the author's run, the best final strategy (G) averaged about 483 against about 346 for the hand-made strategy M (pp. 7–10).
- Reading G's genome did not help much. The author found out how G works by watching its behavior and attributes its success to interacting genes (the numbers in its string) (pp. 10–11).
- G showed two behaviors: circling the grid edge when no can is in view, and sometimes leaving a can as a marker. Resetting the marker-related genes to the PickUp action lowered G's score from 483 to 443 (pp. 11–15).
- The run's best fitness rose from −81 to near 500. The author lists which traits had appeared by which generation (pp. 15–17).
- GAs are used in many fields. The author says they often produce working solutions that are hard to understand (pp. 2–3, 17–18).

## L3 — Walkthrough

### Opening (pdf 161–162)
- Von Neumann wanted programs to reproduce with mutations and compete for resources. He died before working on evolution (pdf 161).
- By the early 1960s several groups worked on "evolutionary computation". The best known is the GA work of John Holland and colleagues at Michigan (pdf 161). Holland's advisor was Arthur Burks, who had worked with von Neumann (pdf 161).
- Holland read Fisher's book on natural selection and was struck by the analogy with breeding. He said: "I began to wonder if you could breed programs the way people would say, breed good horses and breed good corn." (pdf 162)
- His interest was adaptation. His 1975 book *Adaptation in Natural and Artificial Systems* proposed GAs (pdf 162).

### A Recipe for a Genetic Algorithm (pp. 1–2)
- An algorithm is a series of steps turning an input into an output (p. 1).
- A GA's output is a solution to a problem. Its input is (i) a population of candidate programs and (ii) a fitness function, which gives each candidate a value for how well it does the task (p. 1).
- Candidates can be strings of bits, numbers or symbols (p. 1). Example: for a robot-janitor program, fitness could be the floor area covered in a set time (p. 1).
- Recipe, repeated for some number of generations (rounds of new populations) (pp. 1–2):
  1. Generate an initial population of random strings ("individuals").
  2. Compute each individual's fitness.
  3. Select some of the highest-fitness individuals as parents.
  4. Pair them. Each pair makes offspring by recombining parts of the parents, with some chance of random mutation. Offspring fill the new population to the original size.
  5. Go to step 2.

*Intuition note:* Fitter strings get more chances to pass on their parts, and children mix parts of two parents. A population can therefore change from one generation to the next without anyone writing the solution.

### Genetic Algorithms in the Real World (pp. 2–3)
- Versions of this simple GA have been used in science, engineering, art, architecture and music (p. 2).
- Examples named: aircraft design (General Electric), satellite images (Los Alamos), assembly-line scheduling (John Deere), chip design (Texas Instruments), movie animation (horses in a 2003 film and stunt doubles in *Troy*), drug discovery, finance (fraud detection, credit card data, forecasting), and interactive-GA artwork shown in museums (pp. 2–3).

### Evolving Robby, the Soda-Can-Collecting Robot (pp. 3–9)
**Setup (pp. 3–4).**
- The world is a simulated 10 × 10 grid with a wall around it and at most one can per site (p. 3).
- Robby sees his own site and the sites north, south, east and west. Each can be empty, hold a can, or be a wall (p. 3).
- A session has exactly 200 actions. Each action is one of seven: move N, S, E or W; move in a random direction; stay put; bend to pick up (p. 4).
- Rewards: +10 for picking up a can. Fines: −1 for bending where there is no can; −5 for hitting a wall, after which Robby bounces back (p. 4).

**What is evolved (p. 5).**
- A strategy is a set of rules giving the action to take in any situation. Here a situation is what Robby sees, in five sites (p. 5).
- Number of situations: five sites with three possible contents each, so $3^5 = 243$ (added step; the text gives 243 and refers to the notes). Some of these can never occur, for example the current site being a wall. The author lists all 243 anyway (p. 5).
- Example: for Robby's situation in figure 9.1 (north wall, south empty, east can, west wall, current empty), the partial table 9.1 says MoveWest. He moves west and crashes. The author says finding a good strategy is the GA's job (p. 5).

**Encoding and algorithm (pp. 6–9).**
- An individual is just the list of 243 actions. The position in the list fixes the situation, so situations are not written out. The author's GA looks up the action by the situation's number (p. 6).
- Each entry is a "gene", a number 0–6: 0 MoveNorth, 1 MoveSouth, 2 MoveEast, 3 MoveWest, 4 StayPut, 5 PickUp, 6 RandomMove (p. 7).
- Settings:
  1. The initial population is 200 random strategies (figure 9.2) (pp. 7–8).
  2. Repeat for 1,000 generations. Fitness is the average score over 100 sessions. Each session starts Robby at site 0,0, gives each site a can with probability 50%, and runs 200 actions. A session's score is rewards minus fines (p. 7).
  3. Build the new population until it has 200 individuals (pp. 8–9):
     - (a) Choose two parents with probability based on fitness; higher fitness gives more chance.
     - (b) Crossover: pick a random split position. Child 1 takes the numbers before it from parent A and after it from parent B; child 2 the reverse.
     - (c) With small probability, replace one or more numbers in a child by random numbers from 0 to 6 (mutation).
     - (d) Add both children to the new population.
  4. Return to step 2 (p. 9).
- Population size, generations, actions per session and sessions per fitness were chosen "somewhat arbitrarily". Other numbers can also give good strategies (p. 9).

**Comparison with a hand-made strategy M (pp. 9–10).**
- M: pick up a can in the current site; otherwise move to an adjacent can; otherwise move randomly (p. 9).
- M can get stuck cycling around empty sites (p. 9).
- On 10,000 sessions M averaged about 346. About 50 of 100 sites hold cans, so the maximum is about 500 (p. 9).
- The best individual of the final generation (G), tested on 10,000 new sessions, averaged about 483 (pp. 9–10).

*Intuition note:* Scores are per session out of a maximum of about 500. The GA-evolved G (about 483) is near that maximum, and the hand-made M (about 346) is not.

### How Does the GA-Evolved Strategy Solve the Problem? (pp. 10–15)
- M and G are each printed as a long string of digits (their genomes) (p. 10).
- Staring at a genome "doesn't help us too much" in understanding how the strategy works (p. 10). A few genes make sense. The situation "Empty Empty Empty Empty Can" has action 5 (PickUp) in both M and G (p. 10).
- Current-site-can situations always have action 5 in M, but only most of the time in G. One such situation in G has action 3 (MoveWest), so Robby does not pick up the can there. Yet G does better overall (pp. 10–11).
- The author says the key is how genes interact, not these isolated genes, "just as has been found in real genetics". It is hard to tell how interactions produce behavior (p. 11).
- The author therefore watched behavior (the phenotype) with a graphics program. G and M behave alike in many situations, but G uses two tricks (p. 11).

**Trick 1: circling the edge (pp. 11–13).**
- With no can in the current or adjacent sites, M moves randomly. G moves east until it finds a can or reaches a wall. It then goes north and circles the edge counterclockwise until a can is met or sensed (p. 11; figure 9.3, p. 12).
- This avoids wall crashes that random moves can cause under M. The author adds that it also turns out to be a more efficient way to meet cans than random moves (p. 13).

**Trick 2: not picking up a can (pp. 13–15).**
- In the cluster of figure 9.4a, M picks up the can on its site, moves west and picks up the next can. It then cannot see the rest of the cluster. It must move at random until it meets another can (p. 13).
- G (figure 9.5) does not pick up the current can. It moves west, picks up the western-most can of the cluster, and then picks up all the remaining cans (figure 9.5d–k; the author says the left-behind can acts as a marker). (pp. 13–14)
- The author writes that this little trick "never occurred to me". The author also says GAs often come up with things humans do not consider (p. 15).
- Knockout test: set every gene for a "can in current site" situation to PickUp. G's average fell from 483 to 443. The author says this supports the hypothesis that the trick is partly responsible for G's success (p. 15).

*Intuition note:* G's behavior can be described in words, such as circling the edge and leaving a can. The raw number string does not make these behaviors easy to see. The author's evidence is a mix of watching Robby and one knockout test.

### How Did the GA Evolve a Good Strategy? (pp. 15–17)
- Figure 9.6 plots the best fitness per generation. It starts well below zero, rises quickly until about generation 300, then improves more slowly (p. 16).
- Generation 1: best fitness −81, worst −825 (p. 16). The worst strategy sometimes gets stuck on StayPut, sometimes keeps hitting a wall, sometimes keeps trying to pick up a can that is not there (p. 16).
- The best of generation 1 is also bad. It is less likely to keep crashing and sometimes picks up a can. It has an excellent chance of being selected, and its children inherit these traits along with many bad ones (p. 17).
- By generation 10 the best fitness is about zero; the strategy usually gets stuck in a StayPut loop (p. 17).
- By generation 200 the best strategy moves to cans and picks them up at least a lot of the time, but makes random moves in a "no-can wilderness" (p. 17).
- By generation 250 a strategy equal in quality to M exists. By generation 400 fitness is above 400. By generation 800 the can-marker trick has been discovered. By generation 900 the perimeter trick is nearly perfected, and a few more tweaks come by generation 1,000 (p. 17).

### Closing remarks (pp. 17–18)
- The author says Robby is not all that different from real-world GA use. There, a GA will often evolve a solution that works while it is hard to see why. This is often because GAs find good solutions "quite different" from human ones (p. 17).
- Jason Lohn (NASA) is quoted as calling evolutionary algorithms "a great tool for exploring the dark corners of design space" (p. 17). The same quotation (with a gap in the source) continues: "We frequently see evolved designs that are completely unintelligible." (p. 18)
- Lohn describes showing designs to people with 25 years' experience, who ask if the design really works (pp. 17–18).
- In 2005 Lohn and colleagues won a "Human Competitive" award for a GA-designed antenna for NASA spacecraft. It improved on the human engineers' design (p. 18).

## Toy example (ours, not from the text)
Task: evolve a 4-bit string with as many 1s as possible. Fitness = number of 1s.
- Population of 4: 1100 (fitness 2), 0100 (1), 1011 (3), 0001 (1). Total = 7, mean = 7/4 = 1.75.
- Selection (our choice: probability proportional to fitness): 1011 has chance 3/7, 1100 has 2/7, and each of the other two has 1/7. Suppose 1011 and 1100 are picked.
- Crossover after position 2. Parent A = 10|11, parent B = 11|00. Child 1 = 10 + 00 = 1000 (fitness 1). Child 2 = 11 + 11 = 1111 (fitness 4).
- Mutation (ours: flip one bit with small probability). Suppose the last bit of 1000 flips, giving 1001 (fitness 2).
- Child 2 (fitness 4) beats both parents (3 and 2), while child 1 before mutation (fitness 1) is worse than both parents; after mutation it is 1001 (fitness 2), worse than 1011 and equal to 1100. Here, mixing parts produced a better string, while a single child can also be worse.

## Concepts
- [[genetic-algorithm]] (new) — a procedure that evolves a population of candidate solutions by fitness-based selection, crossover and mutation (p. 1)
- [[fitness-function]] (new) — maps a candidate to a number for how well it does the task (p. 1)
- [[crossover-and-mutation]] (new) — children made by splitting two parent strings and joining the parts; random changes to genes with small probability (pp. 8–9)
- [[genotype-vs-phenotype]] (new) — the gene string versus the behavior it produces; the author inspects behavior because the genome is hard to read (pp. 10–11)
- [[gene-interaction]] (new) — the author's explanation for why G beats M: how genes interact, not isolated genes (p. 11)
- [[knockout-test]] (new) — setting chosen genes to a fixed value to test their role; here the PickUp genes (p. 15)

## Canonical instances
- [[robby-the-robot]] — GA evolves a strategy table for a can-collecting robot; best strategy about 483 vs 346 hand-made (pp. 3–10)
- [[robby-marker-trick]] — G leaves a can in place to mark a cluster; the author says it never occurred to the author (pp. 13–15)
- [[ga-antenna-design]] — Lohn's GA-designed NASA antenna, an award-winning improvement over human design (p. 18)

## Bridges (candidates)
- [structural-analogy] Hard-to-read genome vs. clear behavior ↔ complex systems: macro behavior is not obvious from micro rules (emergence) — the author describes G's behavior, not its genes, in plain terms.
- [structural-analogy] Population of strategies under fitness-based selection ↔ agent-based models: many agents, simple local rules, collective outcome — both build the result by simulation.
- [metaphor] Breeding horses and corn ↔ evolving programs — Holland's own analogy (pdf 162).

## Questions this raises
- The text reports one run. Would other runs evolve the same two tricks, or other ones?
- The knocked-out G scores 443, still above M's 346. What else explains the remaining gap?
- The author says other parameter values can also work. How much does changing population size or mutation rate change the result?
- How can one test whether an evolved solution that is "unintelligible" is reliable outside the situations it was tested on?

## Reading notes
- Page numbers: pdf 163–175 are labelled printed 1–13. The page images for pdf 176 and 178 show no printed number, and the labels give "?" for pdf 176–180. I cite them as pp. 14–18 by continuing the offset (printed = pdf − 162); these five numbers are inferred, not seen. pdf 161–162 have no printed number and are cited as (pdf 161), (pdf 162).
- Table 9.1 appears only as a heading on p. 5; its contents are not on the pages supplied. The pictures of situations on pp. 6, 10 and 11 are missing from the text layer.
- Figure 9.5 is "continued on next page": the images for panels (i)–(k) were not supplied.
- Figure 9.6 image shows the best-fitness curve starting at about −80 (well below zero) and ending near 500. This matches the text's −81 and its "way below zero".
- The unit's text is exercise-free; no Exercises section.
