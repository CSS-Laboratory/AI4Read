---
id: mitchell-2009-guidedtour/ch13-make
work: mitchell-2009-guidedtour
unit: "Chapter 13 — How to Make Analogies (if You Are a Computer)"
pages: 43–70
fields: [complex-systems]
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
# How to Make Analogies (if You Are a Computer)

## L0 — One line
Good analogy-making means finding fitting "conceptual slippages", and Mitchell's Copycat program does this through many probabilistic, ant-colony-like agents whose randomness falls as a "temperature" drops.

## L1 — The gist (≤ 120 words)
How can a computer make analogies, that is, see abstract similarity despite surface differences? Mitchell describes Hofstadter's letter-string microworld (a simplified toy domain), where good answers come from "conceptual slippages" (a concept in a rule giving way to a related one). She then describes Copycat, the program she built for it. Copycat has a network of concepts (the Slipnet), a Workspace, many small agents (codelets) and a "temperature". Exploration starts random and parallel, then becomes focused as structure is built. She compares this to ant colonies and the immune system. Because decisions are probabilistic, answers differ between runs. She suggests Copycat has a very primitive kind of meaning, but says the "barrier of meaning" remains for AI.

**Prerequisites:** basic probability (random choice, relative frequency); the idea of feedback; chapter 12's ideas of exploration vs. exploitation (restated briefly in the text).

## L2 — Key ideas
- Computers are good in narrow domains but still lack common sense and are notoriously bad at analogy-making; Minsky's phrase is "Easy things are hard" (pp. 43–44).
- Mitchell defines analogy-making as perceiving abstract similarity between two things despite superficial differences. She says it pervades almost all of intelligence (p. 44).
- Hofstadter's letter-string microworld keeps the essence of analogy. Its key mechanism is conceptual slippage, e.g. *rightmost* ⇒ *leftmost*, *successor* ⇒ *predecessor* (pp. 48–51).
- A good explorer needs all possibilities to be potentially available but not equally available. Ant colonies and the immune system do this by mixing randomness with feedback. Hofstadter's "parallel terraced scan" does the same (pp. 52–55).
- Copycat has four parts: Slipnet (concepts with activation and resistance), Workspace, codelets (small agents), and temperature (pp. 55–57).
- Temperature measures how much perceptual organization exists. It also feeds back to control how random codelet decisions are (p. 57).
- Over 1,000 runs, the most frequent answer was not the one with the lowest final temperature (p. 68).
- Mitchell says this random-to-focused shift seems to be common to at least some complex adaptive systems. She hopes Copycat shows "the beginning of meaning", while AI's "barrier of meaning" is still unbroken (pp. 69–70).

## L3 — Walkthrough

### Easy Things Are Hard (pp. 43–44)
- **Story:** Her son Jake puts his socks on his head when told to put his socks on. The joke works because humans normally know what is meant, although most statements are ambiguous in principle. She calls this "common sense" or "sensitivity to context" (p. 43).
- Computers are not sensitive to context. Her spam filter may miss a "word" like V!a&®@. Journalists tailor headlines to literal-minded search engines (pp. 43–44).
- Computers are strong in narrow domains: driving across rugged desert terrain, diagnosing some diseases, solving equations, chess. Eric Horvitz is quoted saying people say "human-level AI" "without blushing" (p. 44).
- Computers still cannot understand human language, describe a photograph, or use common sense. Minsky described this paradox in four words: easy things are hard (p. 44).

### Making Analogies (pp. 44–46)
- **Definition (author's):** analogy-making is the ability to perceive abstract similarity between two things in the face of superficial differences. It is much broader than standardized-test questions of the form shoe : foot :: glove : ? (p. 44).
- **Examples:** a child's concept of "dog"; recognising the letter A in many typefaces; a reply that means one's *own* parents, not the speaker's; Perrier described as a Cadillac among bottled waters; Greece siding with Britain over the Falklands because of Cyprus; recognising Bach's style; Yukawa's analogy between the nuclear and electromagnetic force, which led to a predicted particle that was later found (pp. 45–46).
- Humans do this by letting concepts "slip" fluidly from situation to situation (p. 46). Computers are "notoriously bad" at it. For example, she cannot simply show one a picture of a dog swimming in a pool and ask it to find similar pictures in her online photo collection (p. 46).

### My Own Route to Analogy (pp. 46–48)
- This is a personal story. In the early 1980s she read Hofstadter's *Gödel, Escher, Bach*. She says it was fundamentally about thinking and consciousness emerging from the decentralized interactions of many simple neurons, and it introduced her to complex systems (pp. 46–47).
- After letters, a lecture and phone calls, she reached Hofstadter by phoning at night. His current project was a program that makes analogies (p. 48).

### Simplifying Analogy (pp. 48–51)
Hofstadter built a **microworld** (a simplified domain that keeps the problem's interesting features) of analogies between letter strings (p. 48).

| Problem (abc ⇒ abd) | Most common answer and rule | Other answers |
|---|---|---|
| ijk ⇒ ? | **ijl**: replace the rightmost letter by its alphabetic successor (p. 49) | ijd, ijk, abd, ijxx (p. 49) |
| iijjkk ⇒ ? | **iijjll**: replace the rightmost *group* of letters by its successor. *Letter* slips to *group of letters*. Literal rule gives iijjkl (p. 49) | — |
| kji ⇒ ? | **lji**: *rightmost* slips to *leftmost*. Literal rule gives kjj (pp. 49–50) | kjh: *successor* slips to *predecessor*, rule "replace rightmost letter by predecessor" (p. 50) |
| mrrjjj ⇒ ? | Most people: mrrkkk (or mrrjjk) (p. 50) | **mrrjjjj**: many people find it more satisfying; see below |
| xyz ⇒ ? | Z has no successor and the alphabet is not circular, so xya is excluded (p. 51) | xy, xyd, xyy (p. 51); **wyz**: see below |

- **Why ijl:** Mitchell says she may not be able to convince someone who prefers ijd. She suggests that humans seem to have evolved to make analogies that matter for survival, that this ability seems to carry over into abstract domains, and that almost all of us will therefore agree on a most appropriate level of abstraction. She adds a remark about people who prefer ijd being eaten by tigers in the Pleistocene (p. 49).
- **mrrjjj:** the "successorship fabric" of abc seems absent from mrrjjj. It appears if you ignore the letters and look at group lengths, which increase as 1-2-3. The rule becomes: replace the rightmost group of letters by its length successor, giving 1-2-4, i.e. mrrjjjj (p. 50).
- **xyz:** the impasse forces a restructuring. View abc and xyz as "mirror images": xyz is wedged against the end of the alphabet and abc against the beginning. Then z corresponds to a, and x to c. The slippages are *alphabetic-first* ⇒ *alphabetic-last*, *rightmost* ⇒ *leftmost*, *successor* ⇒ *predecessor*. The rule becomes: replace the leftmost letter by its predecessor, giving **wyz** (p. 51).
- **Conclusion:** the key to analogy-making here (and, she says, in the real world) is *conceptual slippage*. Finding appropriate slippages given the context is, she says, the essence of finding a good analogy (p. 51).

*Intuition note:* A rule that talks about the rightmost letter is a description. To copy it onto a new string, some words in the description must be swapped for neighbours (rightmost → leftmost). Which swaps are sensible depends on the new string's structure.

### Being a Copycat (p. 52)
- Hofstadter's plan: she would write a program making letter-string analogies by the mechanisms he believed underlie human analogy-making. It was named "Copycat", because analogy-making is a subtle form of imitation (p. 52).
- It took six years of close work with Hofstadter to build it. The results were a program with human-like analogies in its microworld and her Ph.D. (p. 52).

### How to Do the Right Thing (pp. 52–55)
- **Problem:** a situation allows an "intractably huge" number of possible interpretations. How can one explore them? (p. 52)
- **Two strategies Mitchell rejects:**
  1. Some possibilities are excluded in advance (e.g. fix a candidate list for mrrjjj). This loses flexibility, because a concept like *group length* might become central later (pp. 52–53).
  2. All possibilities are equally easy to explore. With real-life possibilities this cannot work for a finite brain. Her timing-belt example: a broken belt, a malicious neighbour, quantum tunnelling into a parallel universe (p. 53).
- **Upshot:** all possibilities must be potentially available, but not equally available. Counterintuitive ones need significant pressure to be considered (p. 53).
- **Nature's solution:** ant colonies keep a balance of *exploration and exploitation* (chapter 12). Promising trails get more ants through pheromone feedback, while some ants still forage randomly. The immune system keeps a huge B-cell repertoire (exploration) and amplifies cells matched to actual antigens (exploitation). Both combine randomness with directed, feedback-based behaviour (pp. 53–54).
- **Parallel terraced scan (Hofstadter):** many possibilities are explored in parallel, each given resources according to its current estimated promise, which is continually updated. With little information, exploration is random, highly parallel and unfocused. As information accumulates, it becomes more focused and less random. In Copycat this strategy emerges from many interactions of simple components (pp. 54–55).

*Intuition note:* Imagine scouts searching a big area. Most follow the best-looking path, a few keep wandering. Every option stays open, but the budget is not spread evenly.

### Overview of the Copycat Program (pp. 55–57)
- **Task:** use its concepts to build *perceptual structures* on top of three raw letter strings. Structures are descriptions of objects, links between objects in the same string, groupings, and correspondences between strings. Every problem starts from the same state and the same concepts, so concepts must adapt in relevance and associations (p. 55).
- **Slipnet:** a network of concepts, each a central node with potential associations and slippages (figure 13.1) (pp. 55–56).
  - Each node has a dynamic *activation* (current perceived relevance). Activation spreads to neighbours and decays if not reinforced (p. 56).
  - Each link has a dynamic *resistance* to slippage, inversely proportional to the activation of the node naming the link. When *opposite* is highly active, resistance between *successor* and *predecessor* drops and such slippages become more probable (p. 56).
- **Workspace:** the working area holding the letters and the structures built on them (p. 56).
- **Codelets:** small agents that explore possible structures and try to build them. Teams cooperate and compete, with resources (codelet time) allocated according to the promise of the structure, assessed dynamically. A parallel terraced scan emerges and builds a hierarchy of structures that is the program's "understanding" (pp. 56–57).
- **Temperature:** measures the amount of perceptual organization (high = disorganized). It also feeds back to control codelet randomness. High temperature means more random decisions, and low temperature means more deterministic ones (p. 57).

### A Run of Copycat (pp. 57–68)
The run is on abc ⇒ abd, mrrjjj ⇒ ? (p. 58).

- **Fig. 13.2:** the problem is displayed. Temperature is 100 (maximum, no structures). Zero codelets have run (p. 58).
- **Fig. 13.3 (30 codelets):**
  - Codelets propose structures at random. A structure that more codelets find worthwhile becomes stronger. Above a threshold it is "built" and can influence later building (p. 59).
  - Conceptually, codelets can be thought of as antlike agents, each probabilistically following a path to explore while guided by paths laid down by other codelets; here the paths are candidate structures (p. 59).
  - Dotted, dashed and solid lines mean early consideration, serious consideration and built (p. 59).
  - The a–m correspondence is rated promising, since both are *leftmost* and identity mappings are always strong. The a–j correspondence is rated much weaker (*leftmost* ⇒ *rightmost*, with *opposite* not active) (p. 59).
  - Temperature falls to 94 after one structure, the sameness link between the two rightmost j's. It activates *same* in the Slipnet, which sends focused codelets to look for sameness elsewhere (p. 59).
- **Fig. 13.4 (96 codelets):**
  - The successor links in abc are built and support each other. The c-to-b predecessor link lost to a successor link (p. 60).
  - Rival groups bc and abc compete. abc is stronger because it covers more objects. jjj is being considered (p. 60).
  - The a–j correspondence was aborted. A c–j correspondence was built, based on rightmost ⇒ rightmost (p. 60).
  - Successor, sameness and identity-mapping nodes are highly active, and create focused pressure for more of them (pp. 60–61).
  - Temperature is 76. Lower temperature makes unlikely structures, such as the bc group, even less likely (p. 61).
- **Fig. 13.5:**
  - The abc and jjj groups are built, and rr is being considered. A group becomes a new object that can have descriptions and correspondences (p. 61).
  - Group length is not noticed automatically. Codelets must notice it, like any attribute. Activated group nodes spread some activation to *length*, which is only weakly active so far (pp. 61–62).
  - A rule is built: *replace letter-category of rightmost letter by successor*. The program assumes the example change replaces exactly one letter. Rule codelets fill the template "Replace ___ by ___", with a bias toward more abstract descriptions (p. 62).
  - Temperature is 53 (p. 62).
- **Fig. 13.6 (225 codelets):**
  - The letter-to-group c–J correspondence defeated c–j. It covers more objects, and *group* is highly active. A *letter* ⇒ *group* mapping joins rightmost ⇒ rightmost (p. 62).
  - The rr group is built and its length (2) noticed by a codelet, a probabilistic event. That activates *length* (p. 63).
  - A weaker rule, *replace the letter category of the rightmost letter by D*, replaced the old one. Competitions are probabilistic, and this one happened to win. Temperature rises to 58 (p. 63).
  - If the program stopped now (unlikely, as stopping depends probabilistically on temperature), the answer would be mrrddd, which Copycat produces only on very rare occasions (p. 63).
  - Answer-building codelets run often throughout, but are unlikely to succeed unless the temperature is low (p. 63).
- **Fig. 13.7 (480 codelets):**
  - The successor rule is restored. The c–J correspondence is broken and replaced by c–j. A stop now would give mrrjjk (p. 64).
  - c–J will likely be seen as stronger than before, because of the parallel b–R correspondence (p. 64).
  - The activation of *length* has decayed, since the length description has not been used (p. 64).
  - The temperature is still fairly high, because the program has trouble making one coherent structure of mrrjjj. This difficulty plus pressure from two sameness groups makes it consider an a priori very unlikely single-letter sameness group around m (p. 64).
- **Fig. 13.8:**
  - The M group (length 1) is built, activating *length* again. A successor link between the lengths 1 and 2 is built, probably due to focused pressure from abc (p. 65).
  - A consistent trio of letter ⇒ group correspondences exists. Temperature falls to 36, which helps lock in this view (p. 65).
  - A stop here would give mrrkkk, the most frequent answer (p. 65).
- **Figs. 13.9–13.10:**
  - Length descriptions are attached to jjj and abc, and a 2–3 successor link is built. A whole-string group based on successorship of numbers is then built over the three sameness groups. A correspondence between abc and mrrjjj is being considered (p. 65).
  - A "renegade" codelet then replaces c–J with c–j, a global setback. Temperature does not drop as much as it otherwise would, since the correspondences are no longer parallel. A stop now would give mrrjjk (pp. 66–67).
- **Fig. 13.11 (890 codelets, read from the figure; not stated in the text):**
  - c–J is restored and the abc–mrrjjj whole-string correspondence is built. Its underlying mappings are whole ⇒ whole, successor-group ⇒ successor-group, right ⇒ right, successor ⇒ successor, letter-category ⇒ length, and 3 ⇒ 3 (p. 67).
  - Temperature is 11. A codelet translates the rule using the slippages *letter ⇒ group* and *letter-category ⇒ length* (all others are identity). The rule becomes *replace the length of the rightmost group by its successor*, and the answer is **mrrjjjj** (p. 67).

*Intuition note:* No codelet sees the whole picture, and early structures can be destroyed by luck. Still, mutually supporting structures gradually win. Then the temperature is low and the interpretation is locked in.

- **Fig. 13.12 (1,000 runs, each with a different random seed):**
  - Frequency roughly corresponds to how obvious or immediate an answer is, given the program's biases (p. 68).
  - mrrkkk occurred 705 times and mrrjjjj 42 times. The average final temperature was 43 for mrrkkk and 21 for mrrjjjj. So although mrrkkk is more immediate, the program judges mrrjjjj the better answer, in terms of the strength and coherence of its structures (p. 68).
  - The bar graph also shows (read from the image): mrrjjk 197 (T 49), mrrjkk 48 (T 46), mrrjjd 6 (T 62), mrrjjj 2 (T 82).

*Intuition note:* "Most common" and "best-judged" can differ. The lower average final temperature indicates that the program judges an answer to be better; it is not a frequency count.

### Summary (pp. 69–70)
- **Catch-22 of perception:** you cannot explore everything, but you do not know what is worth exploring without exploring it. Copycat starts with high temperature, much randomness and parallel exploration. As information arrives, temperature falls and exploration becomes more deterministic and serial. The system moves from a mostly random, parallel, bottom-up mode of processing to a deterministic, serial, focused one (p. 69).
- She says, referring back to chapter 12, that this gradual shift between processing modes seems to be shared by at least some complex adaptive systems (p. 69).
- **Bio analogies suggest ideas.** If cytokines in immune signalling resemble codelets that call attention to sites, one thinks at a general information-processing level. If fever and inflammation emerge from many agents, this might suggest better ways to model temperature in Copycat (p. 69).
- **Meaning:** in chapter 12 she said that for traditional computers meaning lies with humans. She would "like to think" Copycat, a nontraditional kind of computation, perceives a very primitive kind of meaning. For instance, *successor group* sits in a network of similar concepts and is used appropriately in diverse situations. She calls this "the beginning of meaning" (pp. 69–70).
- But meaning is tied to survival and natural selection, which do not apply to Copycat except for its weak "survival" instinct of lowering its temperature. It is still far from biological systems in this respect (p. 70).
- AI's hardest problem is to take humans out of the meaning loop. Rota called this "the barrier of meaning". She personally does not think it will be crashed soon, but suspects that if and when the barrier is unlocked, analogy will be the key (p. 70).

## Toy example
*Our own illustration, not Copycat's actual formula.* Suppose an explorer picks which of three candidate structures to test next. Their strengths are 6, 3 and 1 (total 10). Let "temperature" set an exponent $k$: choice probability is strength$^k$ divided by the sum of strength$^k$.

- High temperature, $k=0$: each strength$^0$ = 1, sum 3, so each has probability 1/3 ≈ 0.33. This is unfocused.
- Medium, $k=1$: 6/10, 3/10, 1/10 = 0.60, 0.30, 0.10.
- Low temperature, $k=2$: squares are 36, 9, 1; sum 46. Probabilities: 36/46 ≈ 0.78, 9/46 ≈ 0.20, 1/46 ≈ 0.02.

Every option stays possible at every step, since none gets probability 0. As $k$ grows, the weak option fades, like the bc group becoming "even more unlikely" at lower temperature (p. 61). Unlike here, Copycat's temperature falls as a result of the structures built, and not by schedule (p. 57).

## Concepts
- [[conceptual-slippage]] (new) — letting a concept in a rule give way to a related one (*rightmost* → *leftmost*) so the rule fits a new situation (p. 51)
- [[analogy-making]] (new) — perceiving abstract similarity between two things despite superficial differences (p. 44)
- [[microworld]] (new) — a simplified domain keeping the essence of a hard problem; here, letter strings (p. 48)
- [[exploration-exploitation-balance]] (new) — keeping some resources on promising options and some on new ones (p. 54)
- [[parallel-terraced-scan]] (new) — many options explored in parallel, resources following current promise, which narrows over time (p. 54)
- [[slipnet]] (new) — Copycat's concept network with activation values and slippage resistances (p. 55)
- [[codelet]] (new) — a small agent that probes and builds perceptual structures; teams compete and cooperate (pp. 56–57)
- [[copycat-temperature]] (new) — measure of lack of perceptual organization that also sets the randomness of decisions (p. 57)
- [[barrier-of-meaning]] (new) — Rota's name for AI's problem of having the computer itself perceive meaning (p. 70)
- [[emergence]] — the scan and the program's "understanding" emerge from many simple components (pp. 55, 57)
- [[feedback]] — pheromone-like and temperature feedback steer exploration (pp. 54, 57)
- [[agent-based-model]] — loosely: codelets act as many small agents; the text does not use this term

## Canonical instances
- [[copycat-abc-abd-mrrjjj]] — a full run showing structures competing, temperature falling, and the answer mrrjjjj (pp. 58–67)
- [[letter-string-analogies]] — ijk, iijjkk, kji, mrrjjj, xyz problems and their answers (pp. 48–51)
- [[ant-colony-foraging]] — exploration and exploitation via pheromone feedback (pp. 53–54)
- [[immune-system-exploration]] — B-cell repertoire as exploration, amplification as exploitation (p. 54)
- [[yukawa-nuclear-force-analogy]] — an analogy leading to a Nobel prize (pp. 45–46)

## Bridges (candidates)
- [structural-analogy] Copycat's temperature ↔ statistical physics: temperature as disorder, with lower temperature meaning more ordered, less random states. The text draws this parallel to the physical world (p. 57), but gives no shared equations.
- [structural-analogy] Pheromone-weighted trail choice ↔ codelet resource allocation by promise: positive feedback plus residual random search.
- [metaphor] Immune cytokines ↔ codelets calling attention to sites; fever and inflammation ↔ temperature (p. 69).
- [metaphor] Rising temperature after a random weak win ↔ noise-driven transitions in other systems (the text does not state this).

## Questions this raises
- How would one test whether Copycat's final temperature is a good measure of answer quality, beyond the 1,000-run comparison?
- If frequency and final temperature disagree (mrrkkk vs. mrrjjjj), which should count as "the" answer?
- What is a minimal behavioural test for "perceiving meaning" that Copycat passes or fails?
- Is Copycat's transition from random to focused processing a general property of complex adaptive systems, or only an analogy? The text says "at least some" (p. 69).

## Reading notes
- Page offset: printed = pdf − 188. Printed numbers 43–70 are on the page labels.
- The unit contains no exercises.
- Figures 13.2–13.11 are low-resolution screenshots; 13.12 is a bar graph. The text does not state the temperatures for figures 13.7, 13.9 and 13.10, nor the codelet counts for figures 13.5 and 13.8–13.11, so they are left out here, except the 890 for fig. 13.11, which is read from the image. The values for the less frequent answers in figure 13.12 are read from the image and may be slightly blurry.
- Minor typo seen on p. 51: "xyzis" (missing space).
- Personal anecdotes (pp. 43, 46–48) are summarised only briefly.
