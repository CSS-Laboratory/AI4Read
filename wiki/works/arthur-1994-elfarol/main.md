---
id: arthur-1994-elfarol/main
work: arthur-1994-elfarol
unit: paper
pages: 406–411
fields: [economics-finance]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 21
pipeline_version: 0.1
---
# Inductive Reasoning and Bounded Rationality (the El Farol bar problem)

## L0 — One line
Arthur argues that when problems are complicated or depend on guessing what others will guess, agents reason inductively (several working hypotheses, act on the best, replace failures), and this can be modelled with simulated populations of predictors, as in the bar problem.

## L1 — The gist (≤ 120 words)
Economic theory assumes perfect deductive rationality. Perfect deduction breaks down in complicated problems; in interactive ones, where agents cannot count on others being perfectly rational and so must guess, deduction cannot apply and the problem becomes ill-defined. Arthur argues that people instead reason inductively: they hold several working hypotheses, act on the most credible one, and drop those that fail. He models this in the "bar problem": 100 people each decide whether to go to a bar that is enjoyable if fewer than 60 attend. In his computer experiments, mean attendance always converges to 60, while the set of forecasting rules in use keeps changing. The paper offers a way to model bounded rationality (limited reasoning ability).

**Prerequisites:** idea of an equilibrium and of a Nash equilibrium (mixed strategy); expectations (forecasts); basic notion of simulation.

## L2 — Key ideas (5–10 bullets)
- Perfect deductive rationality (reasoning by perfect logic from well-defined premises) demands more of humans than they can usually deliver, and it also breaks down in interactive, complicated problems, because agents cannot rely on others being perfectly rational (p. 406).
- Psychology suggests humans are only moderately good at deduction but superb at pattern recognition. They build temporary internal models (hypotheses) and act on them (p. 406–407).
- One way to model induction: heterogeneous (different from one another) agents, each with a private set of subjective hypotheses, tracking their performance, acting on the most credible one, and replacing poor ones (p. 407).
- This generalises the standard learning framework (one shared model, unknown parameters) to a coevolutionary world (where hypotheses and their environment shape each other) in which hypotheses compete within an environment made by other agents' hypotheses (p. 408).
- The bar problem has no deductive solution. Expectations that are commonly held defeat themselves, so expectations are forced to differ (p. 408–409).
- In simulations, mean attendance converges to 60, and the active predictors (each agent's currently most accurate forecasting rules) split on average about 40/60 above/below 60, with changing membership. This is robust to predictor types and numbers (p. 409–410).
- Arthur gives a partial, informal explanation of this and notes that making it mathematically exact appears to be a nontrivial task (p. 410).
- Sometimes there is a unique consistent set of hypotheses (which corresponds to a standard rational expectations equilibrium); more often there are very many such sets. In that case Arthur suggests inductive systems might cycle through, or temporarily lock into, path-dependent patterns (p. 410–411).

## L3 — Walkthrough

### Introduction (p. 406)
- Perfect, logical, deductive rationality is very useful for producing theoretical solutions, but it demands much more of human behaviour than humans can usually deliver (p. 406).
- Image: imagine decision problems as a sea, with easy ones on top and harder ones deeper. Deductive rationality would describe behaviour accurately only "within a few feet of the surface". Tic-tac-toe has a perfectly rational minimax solution; such solutions are not found at the depth of checkers, chess or go (p. 406).
- Two reasons for breakdown (p. 406):
  1. Human logical capacity is bounded.
  2. In interactive situations of complication, agents cannot count on the other agents behaving with perfect rationality, so they must guess. This leads to subjective beliefs, and to subjective beliefs about subjective beliefs. Shared, well-defined assumptions then stop applying, so deductive reasoning cannot apply, and the problem becomes ill-defined (p. 406).
- Arthur says the question is not whether perfect rationality works but what to put in its place. Many ideas have been suggested in the small but growing bounded-rationality literature, but there is not yet convergence among them. Psychologists, by contrast, are in reasonable agreement that in complicated or ill-defined situations humans use characteristic, predictable methods that are inductive, not deductive (p. 406).

### I. Thinking Inductively (p. 406–408)
- Humans are only moderately good at deductive logic and use it moderately. They are superb at seeing or recognising patterns. Faced with complication, they look for patterns and build temporary internal models, hypotheses or *schemata* (mental templates). They do localised deductions from current hypotheses and act. Feedback strengthens or weakens beliefs, poor hypotheses are dropped and replaced (p. 406–407).
- Footnote 1: not all decision problems work this way. Most mundane actions such as walking or driving are subconsciously directed, and pattern-cognition maps directly into action; connectionist models suit those cases better (p. 406–407).
- Chess example: players study the board and recall the opponent's past play to find patterns. They form hypotheses about the opponent's strategy, perhaps several at once ("He's using a Caro-Kann defense"). They deduce locally, several moves deep, and keep or drop hypotheses as play unfolds. The sequence is pattern recognition, hypothesis formation, deduction, replacement (p. 407).
- Advantages: it lets us cope with complication (simpler plausible models) and with ill-definedness (working models fill gaps). Arthur says it is not antithetical to reason or to science; he says it is the way science itself operates (p. 407).

**Modeling induction (p. 407–408)**
- Set up a collection of agents, probably heterogeneous. Each can form hypotheses of several kinds: simple mathematical expressions that describe or predict a variable or action; complicated expectational models of the usual economic kind; statistical hypotheses; or condition/prediction rules ("If situation Q is observed, predict outcome or action D"). These will normally be subjective, that is, they will differ among agents (p. 407).
- Each agent will normally keep track of the performance of a private collection of such belief-models. He acts on the currently most credible (or possibly most profitable) one, or on a combination. Humans tend to hold many hypotheses and act on the most plausible (Feldman, 1962). After actions, the aggregate picture is updated and every agent updates the track record of all his hypotheses (p. 407).
- This is a learning system. Agents linger with their currently most believable hypothesis but drop it when it no longer functions well, in favour of a better one. This gives built-in hysteresis (persistence). A model is kept not because it is "correct" (no way to know) but because it has worked and has not yet accumulated enough failure. There may be a constant slow turnover. Arthur says one could speak of this as a system of *temporarily fulfilled expectations* (p. 407–408).
- Relation to standard theory: the standard learning framework has agents sharing one expectational model with unknown parameters. Here agents differ and each uses several subjective models. Arthur asks whether, in a particular context, this converges to a standard equilibrium of beliefs or stays open-ended, always producing new hypotheses (p. 408).
- It is *coevolutionary* (species and hypotheses evolve in response to each other). As species must prove themselves within an environment created by other species, hypotheses must prove themselves within an environment created by other agents' hypotheses. So the set of hypotheses acted on coevolves (p. 408).
- Footnote 2: a similar statement holds for strategies in evolutionary game theory, but there a small number of strategies compete, not many private expectational models (p. 408).
- Where do hypotheses come from? This is a deep psychological question that Arthur does not pursue. Simple options (p. 408):
  - give agents *focal* models (obvious, simple, easily handled patterns), a "bank" of which is distributed among agents;
  - let a genetic algorithm or similar search device generate ever "smarter" models in a suitable model-space;
  - let agents "pick up" mental models from one another (psychologists call this *transfer*).
- The framework is independent of the specific hypotheses used, as consumer theory is independent of which products are chosen. But to use the framework in a particular problem, some system of generating beliefs must be adopted (p. 408).

*Intuition note:* The idea is to replace the idea that everyone computes the one right answer with the idea that everyone has a few rules of thumb and acts on the one that has worked best lately. Because everyone's rules affect the outcome that tests everyone's rules, the system can keep adjusting itself.

### II. The Bar Problem (p. 408–410)
- Setup: $N$ people decide independently each week whether to go to a bar with entertainment; $N=100$. The evening is enjoyable if fewer than 60 percent of the 100 are present. A person goes if he expects fewer than 60 to show up, and stays home if he expects more than 60. Choices are unaffected by earlier visits, there is no collusion or prior communication, and the only information is the past attendance numbers. It was inspired by the bar El Farol in Santa Fe. Arthur says the reader may recognise it as applying to lunch-room crowding and to other commons or coordination problems with limits to desired coordination. The interest is in the week-to-week dynamics of attendance (p. 408).
- Two features (p. 408–409):
  1. If an obvious model existed that all agents could use to forecast attendance, a deductive solution would be possible. Here many expectational models might be reasonable and defensible. Not knowing which model others choose, a reference agent cannot choose his own in a well-defined way. There is no deductively rational, "correct" expectational model, so from the agents' viewpoint the problem is ill-defined and they are pushed into induction (p. 408–409).
  2. Commonly held expectations break themselves up. If all believe few will go, all go; if all believe most will go, nobody goes; either way the belief is invalidated. Expectations are forced to differ (p. 409).

*Intuition note:* A forecast that everyone shares changes the thing it forecasts, so it cannot be right. This is why a single "correct" model cannot exist here.

#### A. A Dynamic Model (p. 409)
- Each of the 100 agents can form several predictors: functions that map the past $d$ weeks' attendance into next week's. Example history: …, 44, 78, 56, 15, 23, 67, 84, 34, 45, 76, 40, 56, 22, 35 (p. 409).
- Example predictors of next week's number, with the bracketed values printed in the source (p. 409; see Reading notes on [49]): the same as last week's [35]; a mirror image around 50 of last week's [65]; a rounded average of the last four weeks [49]; the trend in the last 8 weeks, bounded by 0 and 100 [29]; the same as 2 weeks ago (2-period cycle detector) [22]; the same as 5 weeks ago (5-period cycle detector) [76].
- Each agent keeps track of an individual set of $k$ such focal predictors. He goes or stays according to the currently most accurate one (his *active* predictor), then learns the new attendance and updates the accuracy of all his monitored predictors (p. 409).
- Loop: the set of active hypotheses determines attendance, and the attendance history determines the set of active hypotheses. Following Holland, these active hypotheses form an *ecology*. The question is how it evolves (p. 409).

#### B. Computer Experiments (p. 409–410)
- Analysis looks difficult for most hypothesis sets, so Arthur uses simulation. He creates an "alphabet soup" of several dozen focal predictors replicated many times, and randomly gives each of the 100 agents $k$ of them ($k$ = 6, 12 or 23, say). Useless predictors need not be a worry: they are not used. With fixed starting conditions and fixed predictor sets, the dynamics are deterministic (p. 409).
- Results (Fig. 1, attendance over the first 100 weeks) (p. 409–410):
  - Where cycle-detector predictors are present, cycles are quickly "arbitraged" away (if many expect many to go because many went three weeks ago, they stay home), so there are no persistent cycles.
  - Mean attendance converges always to 60.
  - The predictors self-organise into an ecology in which, of the active predictors, on average 40 percent forecast above 60 and 60 percent below 60.
  - Membership of this 60/40 split keeps changing forever: like a forest whose contours do not change but whose individual trees do.
  - Results appear throughout the experiments and are robust to changes in predictor types and numbers.
- Partial explanation (p. 410):
  - 60 may be a natural "attractor". Viewed as a pure predicting game, forecasting above 60 with probability 0.4 and below with probability 0.6 is a Nash equilibrium (mixed strategy). But this does not explain how agents with realistic subjective reasoning approximate it.
  - Suppose 70 percent of predictors forecast above 60 for a longish time. Then on average only 30 would show up. This validates predictors near 30 and invalidates the above-60 ones, restoring the balance. Eventually the 40–60 combination would assert itself. Making this exact "appears to be nontrivial".
  - The set-up does not need a 40–60 balance in the predictors. Many could tend to predict high, but aggregate behaviour calls the equilibrium ratio to the fore.
  - The result would fail if all predictors could only predict below 60: then all 100 always show up. Predictors must "cover" the prediction space to some modest degree. Arthur invites the reader to consider what happens if all agents share the same set of predictors.
- Objection: fixed sets of "clunky" predictors may drive the result. Arthur says genetic programming (Koza) could generate new, increasingly complex predictors, but he would be surprised if this changed the results qualitatively. He notes the problem can be generalised (Grannan and Swindle, 1994) (p. 410).

*Intuition note:* Each agent just follows his currently most accurate predictor. In Arthur's informal argument, if too many predictors forecast high, attendance falls and those predictors are invalidated, which restores the balance (p. 410). The simulations show a 60/40 split; the paper does not prove it.

### III. Conclusion (p. 410–411)
- The system is an *adaptive complex system* of hypotheses that adapt to the aggregate environment they jointly create. After initial learning, the hypotheses in use are mutually coadapted. A consistent set is one with a high degree of mutual adaptedness (p. 410).
- Sometimes there is a unique such set; it corresponds to a standard rational expectations equilibrium and beliefs gravitate into it. More often there is a high, possibly very high, multiplicity of such sets (p. 410).
- In that case, inductive-reasoning systems (stock-market speculating, negotiating, poker, oligopoly pricing, product positioning) might cycle through, or temporarily lock into, psychological patterns that may be nonrecurrent, path-dependent and increasingly complicated (p. 410–411).
- Summary: Arthur believes that humans in these complicated, potentially ill-defined contexts use inductive reasoning: they induce several working hypotheses, act on the most credible, and replace ones that cease to work. Usually this leads to a world in which ideas compete for survival against others' ideas, and it is both evolutionary and complex (p. 411).

## Toy example (ours, not from the text)
Scaled-down bar: 10 agents; the bar is enjoyable if fewer than 6 attend (60%). Last week's attendance was 7. Two predictors exist: "same as last week" and "mirror around 5" (10 − last week). Assume each agent uses one active predictor. For simplicity, we treat accuracy as last week's single error (the paper tracks accuracy over time).
- Week 1: 4 agents use "same": predict 7, not fewer than 6, so they stay home. 6 agents use "mirror": predict 10 − 7 = 3, so they go. Attendance = 6, so it is crowded.
- Errors: "same" |7 − 6| = 1; "mirror" |3 − 6| = 3. The mirror users switch to "same".
- Week 2: all 10 now predict 6 (the last attendance), so all stay home (we treat a forecast of exactly 6 as not "fewer than 6"; the paper's rule does not cover this tie). Attendance = 0, and the shared forecast was wrong by 6.
- Lesson: a forecast used by everyone defeats itself, so forecasts must differ across agents, and the mix keeps shifting. This echoes the paper's point that commonly held expectations break themselves up (p. 409).

## Concepts
- [[inductive reasoning in economics]] — agents act on a changing pool of hypotheses that are tested against experience; pattern recognition, local deduction, replacement of failures (p. 406–407)
- [[bounded rationality / heuristics]] — rationality is limited by human logical capacity and by ill-defined interactive problems; Arthur proposes induction as what to put in its place (p. 406, 411)
- [[agent-based modeling]] — simulation of many heterogeneous agents with private predictor sets (p. 409)
- [[rational expectations]] — appears as the special case where a unique consistent set of hypotheses exists (p. 410)
- [[Nash equilibrium]] — the mixed forecasting strategy (above 60 w.p. 0.4) is one in the pure predicting game (p. 410)
- [[equilibrium]] — the paper speaks of an "equilibrium pattern" of predictors (p. 409–410) and of consistent, mutually coadapted sets of hypotheses; a unique such set corresponds to a rational expectations equilibrium (p. 410)
- [[coordination game / multiple equilibria]] — Arthur says the reader may see the bar problem as applying to commons or coordination problems with limits to desired coordination; he says multiple consistent sets of hypotheses are more often found than a unique one (p. 408, 410)
- [[beauty contest / higher-order beliefs]] — beliefs about others' beliefs; Arthur states this as "subjective beliefs about subjective beliefs" (p. 406)
- [[temporarily fulfilled expectations]] (new) — beliefs that are fulfilled for now; replaced when they stop being fulfilled (p. 407–408)
- [[active predictor / ecology of hypotheses]] (new) — the agent's currently most accurate predictor; the set of active ones coevolves (p. 409)
- [[adaptive complex system]] (new) — many hypotheses adapting to the aggregate environment they jointly create (p. 410)

## Canonical instances
- [[el-farol-bar-problem]] — 100 people, enjoyable if fewer than 60 attend; in his simulations mean attendance converges to 60 (p. 408–410)
- [[chess-as-induction]] — players form and replace hypotheses about the opponent's strategy (p. 407)

## Bridges (candidates)
- [structural-analogy] Bar problem's self-defeating common forecast ↔ Keynesian beauty contest: payoff depends on others' beliefs about others' beliefs.
- [structural-analogy] Cycle detectors being "arbitraged away" ↔ efficient markets: exploitable patterns vanish once many act on them.
- [metaphor] Active-predictor ecology that keeps its shape but changes members ↔ biology: a forest whose contours persist while trees turn over.

## Questions this raises
- Why do simulated agents with different predictors end near a 60/40 split? Can this be proved?
- What happens if all agents share the same set of predictors, as Arthur invites the reader to consider (p. 410)?
- When does a population of inductive agents reach a unique rational expectations equilibrium, and when does it stay in many possible equilibria or wander (p. 410)?
- Would richer, open-ended predictor generation (e.g. genetic programming) change the results qualitatively (p. 410)?

## Reading notes
- The page labels show no printed number, but the page images show printed numbers 406–411. Used here: printed = pdf + 404. Pdf 1 is the JSTOR cover sheet (not part of the article).
- Source: *American Economic Review* 84(2), Papers and Proceedings, May 1994, under the heading Complexity in Economic Theory. Discussants are listed on p. 406.
- Footnote 1 continues from p. 406 to p. 407; the page images show it complete.
- Fig. 1 (p. 410) is a line plot of attendance (0–100) over weeks 0–100. I give only the values stated in the text.
- On p. 409 the example four-week average is printed as [49], but averaging the last four listed values (40, 56, 22, 35) gives about 38. I report the bracketed values as printed.
- The explanation of why 60 emerges is informal. The text says that making the argument mathematically exact appears to be nontrivial. No equations appear in the paper.
- No exercises.
