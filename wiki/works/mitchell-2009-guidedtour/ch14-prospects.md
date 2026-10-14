---
id: mitchell-2009-guidedtour/ch14-prospects
work: mitchell-2009-guidedtour
unit: Chapter 14 — Prospects of Computer Modeling
pages: 71-90
fields: [complex-systems]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Prospects of Computer Modeling

## L0 — One line
Simple "idea models", such as simulations of the Prisoner's Dilemma, give a first hand-hold on complex phenomena, but their results must be replicated and their limits stated, because some results turn out to depend on model details.

## L1 — The gist (≤ 120 words)
Mitchell asks what computer models of complex systems can teach us, and what the pitfalls are. She argues that simple "idea models" help us get a first grip on phenomena that lack precise concepts. Her main case is the evolution of cooperation: the Prisoner's Dilemma, Axelrod's tournaments, norms and metanorms, and Nowak and May's spatial model. Results from these models have fed into theory, technology proposals and policy thinking. But replication studies showed that some results change when the model is altered slightly, run longer, or given different payoff values. So models should be scrutinized, replicated, and presented with their limitations clearly stated.

**Prerequisites:** the idea of a game with payoffs; genetic algorithms and cellular automata (earlier chapters); basic probability.

## L2 — Key ideas
- Computer simulation is now a third category of science, next to theory and experiment, and is useful when math alone cannot handle a system (p. 71).
- An idea model is a simple model meant to give insight into a general concept, not detailed predictions about one system (p. 73).
- In the one-turn Prisoner's Dilemma (a two-player game in which each player chooses to cooperate or defect), defecting is the best choice whatever the other player does, yet mutual defection is worse for both than mutual cooperation (pp. 76–77).
- In Axelrod's tournaments (repeated games between submitted programs) the simplest strategy, TIT FOR TAT (cooperate first, then copy the opponent's last move), won. Axelrod noted that the top strategies were nice, forgiving and retaliatory, and that TIT FOR TAT was also clear and predictable (pp. 80–81).
- Adding norms (punishing defectors) and metanorms (punishing those who do not punish), or putting players on a spatial lattice (a grid where each player interacts only with its neighbors), changed whether cooperation survived (pp. 82–84).
- Idea models serve several roles: testing plausibility, exploring variations, inspiring technology, leading to theory, and informing policy (pp. 85–87).
- Replication means that an independent group rebuilds a model from scratch. Replications of famous models found sensitivity to asynchrony (players updating at different times, not all at once), errors, run length and payoff values (the points in the game's payoff table) (pp. 88–89).
- Mitchell's message, following Box and Draper: all models are wrong in some way, but some are very useful; replicate them and stress their limitations (p. 89).

## L3 — Walkthrough

**Introduction (p. 71).** Fast, cheap computers allow models of systems too complex for mathematics alone. The pioneers of computer science (Turing, von Neumann, Wiener and others) wanted to simulate systems that develop, think, learn and evolve. Science's theory/experiment split is now complemented by computer simulation (fig. 14.1).

**What is a model? (pp. 71–73).** A model is a simplified representation of some "real" phenomenon (p. 71). A *mathematical model* states the effects of a phenomenon, for example Newton's law of gravity. A *mechanistic model* explains how the phenomenon works in simpler concepts (p. 72). Newton was attacked for giving no mechanism. Einstein later gave a different mechanistic model (general relativity), and some physicists now propose string theory (p. 72). Models make phenomena understandable in familiar concepts and also predict. Newton's law is still used for planetary orbits, and general relativity predicts deviations from them (pp. 72–73).

**Idea models (pp. 73–74).** Applications such as weather forecasting use detailed models for detailed predictions (p. 73). *Idea models* are relatively simple models meant to give insight into a general concept. Examples listed: Maxwell's demon (entropy), Turing machine (computation), logistic model/map (dynamics, chaos), von Neumann's self-reproducing automaton, genetic algorithm (adaptation), cellular automaton, Koch curve (fractal structures), Copycat (analogy-making) (pp. 73–74). Uses:
- explore general mechanisms;
- show a proposed mechanism is plausible or implausible;
- explore variations of a simple model;
- act as Dennett's "intuition pumps" (p. 74).

Idea models also inspired technologies. Turing machines inspired programmable computers, and minimal models of evolution, the immune system and insect colonies inspired genetic algorithms, computer immune systems and swarm intelligence (p. 74).

*Intuition note.* An idea model is like a thought experiment you can run. It is not a forecast of one real system. It helps you see what a mechanism can and cannot do.

**Modeling the evolution of cooperation (pp. 74–75).** Living organisms are selfish, and common sense predicts that evolution selects selfishness (p. 75). Yet cooperation appears at many levels: multicelled organisms, ant colonies, primate societies, nations and treaties. The question is both scientific and a policy question, for example for nuclear weapons, AIDS and global warming (p. 75).

**The Prisoner's Dilemma (pp. 76–78).** Invented around 1950 by game theorists Merrill Flood and Melvin Drescher (as printed) to study cooperation dilemmas (p. 76). Story: Alice and Bob are held separately.
- If one testifies and the other does not, the testifier goes free and the other gets life.
- If both testify, each gets ten years.
- If neither testifies, each gets five years.

Alice's reasoning: if Bob testifies, testifying gives ten years instead of life. If Bob stays quiet, testifying gives freedom instead of five years. So testifying is better either way. Bob reasons identically, so both testify and both do worse than if both had kept quiet (p. 76). The same logic fits a U.S. president deciding whether to build a bigger bomb while Russia may do the same. Building is better whatever Russia does, yet both building is worse than neither building (p. 77). Axelrod: "The pursuit of self-interest by each leads to a poor outcome for all." Hardin famously called such cases the tragedy of the commons (p. 77).

The game is defined by a payoff matrix. Fig. 14.3 (points; higher is better) (p. 78):

| A | B | A's points | B's points |
|---|---|---|---|
| cooperates | cooperates | 3 | 3 |
| cooperates | defects | 0 | 5 |
| defects | cooperates | 5 | 0 |
| defects | defects | 1 | 1 |

In a one-turn game, defecting is the rational choice. In a repeated game, if both players always defect, each gets a much lower total than if they learned to cooperate. The question is how reciprocal cooperation can be induced (p. 78).

**Axelrod's question (pp. 78–79).** "Under what conditions will cooperation emerge in a world of egoists without central authority?" (p. 78). Hobbes (as reported by Axelrod) concluded cooperation needs a central authority. Einstein similarly proposed world government, but the League of Nations and the United Nations have not been very successful (p. 79). Axelrod therefore studied the repeated game. For him, cooperation "coming about" means cooperative strategies get higher total payoff than noncooperative ones even when opponents change strategy. Under Darwinian selection, their fraction in the population should rise (p. 79).

**Computer simulations: the tournaments (pp. 80–81).** Researchers submitted programs that played repeated games, 200 turns against every other program, with some memory of earlier turns (p. 80). The first tournament had 14 programs, the second 63. A strategy is a rule for the next move given the opponent's earlier behavior (p. 80). In both tournaments the winner, with the highest average score, was the simplest submission: TIT FOR TAT (Anatol Rapoport). It cooperates on turn one, then copies the opponent's previous move. It punishes defection by defecting until the opponent cooperates again (p. 80). This was surprising, since second-tournament entrants knew about it. Nobody designed a better strategy (pp. 80–81).

Axelrod's conclusions (p. 81):
- All top strategies were *nice*: never the first to defect.
- The lowest-scoring nice program was the least forgiving: it defects forever after one defection.
- The best strategies were also *forgiving* and *retaliatory*: they punish defection soon after it occurs.
- TIT FOR TAT also has *clarity and predictability*, which is important for fostering cooperation.

He then used a genetic algorithm to evolve strategies, with fitness equal to score against the other evolving strategies. It evolved strategies with the same or similar behavior as TIT FOR TAT (p. 81).

*Intuition note.* Winning here means a high average score across many opponents, not beating each opponent. A strategy that cooperates with cooperators and punishes defectors can score well overall.

**Extensions (pp. 81–85).** Many variations have been studied: different payoffs, numbers of players, choosing partners (pp. 81–82).

*Adding social norms (pp. 82–83).* Norms are social censure: negative points for a defector caught in the act. Each player has two numbers, *boldness* (probability of defecting) and *vengefulness* (probability of punishing a witnessed defection), assigned randomly at the start. Each generation:
- every player plays every other player;
- a defection is witnessed with some probability;
- each witness punishes with probability equal to its vengefulness;
- parents are selected by points;
- children are mutated copies (p. 82).

If most players start with zero vengefulness, defectors come to dominate. Axelrod expected norms to help, but norms alone did not make cooperation emerge reliably (pp. 82–83). With *metanorms* (punishers punish nonpunishers), nonpunishers evolved to punish more, and punished defectors evolved to cooperate more. Axelrod: "Meta-norms can promote and sustain cooperation in a population." (p. 83)

*Adding spatial structure (pp. 83–85).* Axelrod's original model had no space. Nowak and May put players on a two-dimensional grid (fig. 14.4) (p. 83). Each player always cooperates or always defects, with no memory. At each discrete time step:
- each player plays its eight nearest neighbors, and the eight scores are summed;
- the grid wraps at the edges;
- each player is then replaced by the highest-scoring player in its neighborhood, possibly itself;
- there is no mutation (pp. 83–84).

Depending on initial configurations and payoff values, patterns can oscillate or be "chaotically changing"; in the chaotic case both cooperators and defectors coexist indefinitely. In the nonspatial game without metanorms, defectors take over. Here cooperators can persist indefinitely without norms or metanorms (p. 84). Nowak and May believed this reflects the real world: spatial neighborhoods foster cooperation. Sigmund agreed that territoriality favouring cooperation is "likely to remain valid for real-life communities" (p. 85).

**Prospects of modeling (pp. 85–87).** Simulations of idea models, when done well, can add to experiment and theory. They are sometimes the only means when experiments are infeasible and the math is too hard (p. 85). Their most significant contribution is a first hand-hold on phenomena without precise terminology (p. 85). Mitchell lists the roles of Prisoner's Dilemma models:
- *Plausibility:* they showed that cooperation, in idealized form, can arise in leaderless populations of self-interested but adaptive individuals (p. 85).
- *Variations and intuition:* for example, what happens when a cooperator's mistake signals noncooperation. Holland likened such models to "flight simulators" (p. 86).
- *Technology:* proposals for peer-to-peer networks and preventing e-commerce fraud (p. 86).
- *Theory:* for example Nowak's "Five Rules for the Evolution of Cooperation" (p. 86).

*Policy.* A report by New Energy Finance, "How to Save the Planet: Be Nice, Retaliatory, Forgiving, and Clear", argues that climate response is best seen as a multiplayer repeated Prisoner's Dilemma. Countries either cooperate (cut carbon at economic cost) or defect (do nothing). It recommends policies implementing Axelrod's four characteristics (pp. 86–87). The norms/metanorms results have influenced research on terrorism response, arms control and environmental governance. The spatial results have informed thinking from biodiversity to bacteria producing antibiotics (p. 87).

**Computer modeling caveats (pp. 87–90).** Box and Draper: "All models are wrong, but some are useful." (p. 87). Some claims have been very ambitious, so results should be scrutinized, best by *replication*. In replication, independent groups rebuild the model from scratch and see whether they get the same results (p. 88). Axelrod argues replication guards against programming errors, misrepresentation of what was simulated, and errors in analysis. It also tests robustness of inferences (p. 88).

Replications:
- *Huberman and Glance (1995)* re-implemented Nowak–May with one change: some games and selections were played asynchronously, not all simultaneously. This typically led to complete replacement of cooperators by defectors on the lattice (p. 88).
- *Mukherji, Rajan and Slagle* independently obtained a similar result. They also showed cooperation dies out with small errors or cheating (pp. 88–89).
- *Nowak, May and Bonhoeffor (as printed)* replied that these changes cause extinction of cooperators for some payoff values. For others, cooperators persisted at least for long periods (p. 89).
- *Galan and Izquierdo (2005)* re-implemented Axelrod's norms/metanorms model and ran it much longer. Some results matched and some differed. Metanorms can help cooperation in the short term, but over a long run defectors take over. Results were quite sensitive to details such as payoff values (p. 89).

Mitchell's conclusion: replication can uncover hidden unrealistic assumptions and parameter sensitivity. Replications should themselves be replicated. Modelers should emphasize limitations so results are not misread, taken too literally or hyped (p. 89). Anderson (1977 Nobel speech) has the last word: model-building means leaving out real but irrelevant parts of a problem. The builder may omit something relevant. The reader may take literally a schematized model whose main aim is to demonstrate that something is possible (pp. 89–90).

*Intuition note.* A model shows that something *can* happen under its assumptions. Replication asks whether it still happens when the assumptions are changed a little.

## Toy example (ours, not from the text)
Use the payoff matrix of fig. 14.3. Take 5-turn games. ALLD means always defect.
- TFT vs TFT: C,C each turn → 3 × 5 = 15 each.
- ALLD vs ALLD: 1 × 5 = 5 each.
- TFT vs ALLD: turn 1 TFT cooperates, ALLD defects → TFT 0, ALLD 5. Turns 2–5 both defect → 1 each. TFT = 0 + 4 = 4, ALLD = 5 + 4 = 9.

Population 1: two TFT and one ALLD, with each player's average over its two opponents.
- TFT: (15 + 4)/2 = 9.5.
- ALLD: (9 + 9)/2 = 9.
- TFT scores higher.

Population 2: one TFT and two ALLD.
- TFT: (4 + 4)/2 = 4.
- ALLD: (9 + 5)/2 = 7.
- ALLD scores higher.

So a strategy's success depends on who else is in the population. This is consistent with the chapter's caution about model details. It illustrates only the mechanism, not the tournament results themselves.

## Concepts
- [[idea-model]] (new) — simple model for insight into a general concept, not detailed prediction (p. 73)
- [[mechanistic-model]] (new) — model explaining a phenomenon through simpler concepts, i.e. mechanisms (p. 72)
- [[prisoner-dilemma]] (new) — two-player game where self-interest gives both a worse payoff than cooperation (pp. 76–78)
- [[tit-for-tat]] (new) — cooperate first, then copy opponent's last move (p. 80)
- [[micromotives-macrobehavior]] — self-interest by each leads to a poor outcome for all (p. 77)
- [[norms-and-metanorms]] (new) — punishing defectors, and punishing those who do not punish (pp. 82–83)
- [[spatial-structure-cooperation]] (new) — local neighborhoods let cooperators persist in Nowak–May's model (pp. 83–85)
- [[model-replication]] (new) — independent rebuild of a model from scratch to test results (p. 88)
- [[generative-explanation]] — here, only loosely: simulations show cooperation *can* arise among self-interested agents (p. 85)

## Canonical instances
- [[axelrod-tournaments]] — simple TIT FOR TAT beat complicated strategies (pp. 80–81)
- [[nowak-may-spatial-pd]] — lattice players; cooperators can persist without norms (pp. 83–84)
- [[axelrod-norms-metanorms]] — metanorms sustained cooperation in the original model (pp. 82–83)
- [[huberman-glance-replication]] — asynchronous updating typically wiped out cooperators (p. 88)
- [[galan-izquierdo-replication]] — long runs: defectors take over despite metanorms (p. 89)
- [[tragedy-of-the-commons]] — selfish pursuit of interests harms the group; global warming (p. 77)

## Bridges (candidates)
- [structural-analogy] Nowak–May lattice (play neighbors, copy best neighbor, wrapping grid) ↔ cellular automata: local update rule on a grid (p. 83; text says "like a cellular automaton")
- [structural-analogy] Axelrod's genetic-algorithm evolution of strategies ↔ evolutionary computation: fitness is score against other evolving strategies (p. 81)
- [metaphor] Replication of simulations ↔ replication in experimental science: independent groups rebuild and compare (p. 88)
- [structural-analogy] Prisoner's Dilemma payoffs ↔ game theory: dominant choice leads to a worse joint outcome (pp. 77–78)

## Questions this raises
- Which changes to a model (asynchrony, error, payoff values) count as realistic enough to override its original result?
- If results depend on payoff values, how can we know which values fit a real situation like climate treaties?
- What makes metanorms work only in the short term in the replication (p. 89)?
- How should policy analysts weigh idea-model results when the models are "wrong" in some way?

## Reading notes
- Printed page = pdf − 188 (pdf 259 = p. 71). Page labels gave printed numbers.
- Page images were provided only for pdf 260, 264, 266 and 272; the other pages were read from the text layer. The payoff table (fig. 14.3) was checked against the image.
- The caption of fig. 14.4 continues on p. 85.
- Misprint in the source: "Axlerod" (p. 80; the name is spelled "Axelrod" elsewhere on these pages). "Bonhoeffor" (p. 89) and "Melvin Drescher" (p. 76) are given as printed; their spelling cannot be checked from these pages.
- Endnotes are referred to ("See the notes", p. 87) but are not part of these pages.
