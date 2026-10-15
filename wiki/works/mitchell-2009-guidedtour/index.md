---
id: mitchell-2009-guidedtour/index
work: mitchell-2009-guidedtour
type: work-map
units: [mitchell-2009-guidedtour/ch01-complexity, mitchell-2009-guidedtour/ch02-dynamics, mitchell-2009-guidedtour/ch03-information, mitchell-2009-guidedtour/ch04-computation, mitchell-2009-guidedtour/ch05-evolution, mitchell-2009-guidedtour/ch06-genetics, mitchell-2009-guidedtour/ch07-defining, mitchell-2009-guidedtour/ch08-self, mitchell-2009-guidedtour/ch09-genetic, mitchell-2009-guidedtour/ch10-cellular, mitchell-2009-guidedtour/ch11-computing, mitchell-2009-guidedtour/ch12-information, mitchell-2009-guidedtour/ch13-make, mitchell-2009-guidedtour/ch14-prospects, mitchell-2009-guidedtour/ch15-science, mitchell-2009-guidedtour/ch16-applying, mitchell-2009-guidedtour/ch17-mystery, mitchell-2009-guidedtour/ch18-evolution, mitchell-2009-guidedtour/ch19-past]
---

# Mitchell, M. (2009). *Complexity: A Guided Tour*. Oxford University Press.

## In one paragraph
Mitchell asks what a complex system is. In ants, brains, immune systems, economies and the Web, many simple parts with no central controller produce collective behavior, information processing and adaptation. To explain how, she tours the ideas behind the field. These include chaos, information and entropy, computation, evolution and genetics, cellular automata, genetic algorithms, analogy-making, computer models, networks and scaling. She also shows that the field has no single agreed definition of complexity and no single measure of it. Her conclusion is cautious. There may be no universal laws, only modest "common principles", and the field still lacks the right vocabulary and mathematics. The book matters as a clear, honest on-ramp that shows both what has been learned and what is still open.

## The path through the work
- [[mitchell-2009-guidedtour/ch01-complexity]] — Many simple components with no central controller can produce complex collective behavior, information processing and adaptation, and that pattern, seen in ants, brains, immune systems, economies and the Web, is what Mitchell calls a complex system (pdf 31).
- [[mitchell-2009-guidedtour/ch02-dynamics]] — Simple deterministic rules, such as the one-line logistic map, can produce behaviour that is impossible to predict in detail over the long term, yet this chaos has universal features that are predictable.
- [[mitchell-2009-guidedtour/ch03-information]] — Entropy, first a physics idea about energy, was turned by Boltzmann into a function of the number of microstates behind a macrostate and by Shannon into a measure of a message source's information, which many complex-systems scientists use to talk about order and disorder.
- [[mitchell-2009-guidedtour/ch04-computation]] — Gödel and Turing showed that mathematics and computation have hard limits, and Turing's machine gave a precise definition of "definite procedure" that laid the groundwork for programmable computers.
- [[mitchell-2009-guidedtour/ch05-evolution]] — Darwinian natural selection, acting on small random variation in inherited traits, is the proposed way life gains organization and apparent design without a designer; its Mendelian and statistical foundations were built up in the Modern Synthesis, and that synthesis was later challenged by Gould and others (pdf 98–117).
- [[mitchell-2009-guidedtour/ch06-genetics]] — A gene is a stretch of DNA that codes for a protein, and the cell machinery that copies and decodes DNA is itself encoded in that DNA.
- [[mitchell-2009-guidedtour/ch07-defining]] — There is no single agreed definition of complexity; many proposed measures each capture something about it (size, randomness, construction effort, organization, detail across scales, hierarchy), and all have theoretical and practical limits.
- [[mitchell-2009-guidedtour/ch08-self]] — A program can copy itself without infinite regress if it uses the same stored information both as instructions and as data, and DNA and von Neumann's automaton use the same trick.
- [[mitchell-2009-guidedtour/ch09-genetic]] — A genetic algorithm "breeds" candidate solutions by letting fitter ones become parents of recombined, occasionally mutated children, and in Mitchell's robot example it found a strategy that works very well even though it is hard to see why from the strategy's code.
- [[mitchell-2009-guidedtour/ch10-cellular]] — Cellular automata (grids of simple cells with one shared local rule) are an idealized model for asking how natural systems compute, and Wolfram's ambitious answer to that question is only partly convincing to Mitchell.
- [[mitchell-2009-guidedtour/ch11-computing]] — A genetic algorithm evolved cellular automata that do a "majority" task fairly well with no central control, and their working can be explained by describing the boundaries between regions as information-carrying "particles" that collide.
- [[mitchell-2009-guidedtour/ch12-information]] — In immune systems, ant colonies and cell metabolism, "information" is a changing statistical pattern over many simple parts, and the system handles it by sampling, with random components and feedback that shifts resources toward what looks promising.
- [[mitchell-2009-guidedtour/ch13-make]] — Good analogy-making means finding fitting "conceptual slippages", and Mitchell's Copycat program does this through many probabilistic, ant-colony-like agents whose randomness falls as a "temperature" drops.
- [[mitchell-2009-guidedtour/ch14-prospects]] — Simple "idea models", such as simulations of the Prisoner's Dilemma, give a first hand-hold on complex phenomena, but their results must be replicated and their limits stated, because some results turn out to depend on model details.
- [[mitchell-2009-guidedtour/ch15-science]] — Many real networks seem to share a few structures (clustering, short paths, hubs, power-law degree distributions), and scale-free networks, which have hubs, are resilient to random failure but vulnerable if hubs are lost.
- [[mitchell-2009-guidedtour/ch16-applying]] — Small-world and scale-free ideas are used across many fields, but Mitchell stresses that their evidence and explanations are contested and that how information and failures spread (dynamics, such as cascading failure) is one of the most important open problems.
- [[mitchell-2009-guidedtour/ch17-mystery]] — Metabolic rate is observed to follow roughly a 3/4-power law of body mass (Kleiber's law), which metabolic scaling theory proposes to explain through fractal fuel-delivery networks, though both the data and the theory are disputed and power laws in general remain an open problem.
- [[mitchell-2009-guidedtour/ch18-evolution]] — New genetics (genes as regulatory networks, switches) and Kauffman's Random Boolean Networks are used to argue that natural selection is not the only source of biological complexity, though the evidence is still contested.
- [[mitchell-2009-guidedtour/ch19-past]] — Mitchell thinks no single set of useful principles will cover all complex systems; modest "common principles" might arise through a feedback cycle with studies of specific systems; and the field still lacks the right vocabulary and mathematics.

## Big ideas across units
- **Simple parts, no controller, global behavior.** Emergence and self-organization are introduced as the central question, then shown in ants, cellular automata, immune systems, Copycat's agents and gene networks. Units: ch01, ch10, ch11, ch12, ch13, ch18, ch19.
- **Deterministic rules, unpredictable detail, universal order.** The logistic map shows chaos with universal features. Simple cellular-automaton rules and Kauffman's networks again give rich behavior from simple rules. Units: ch02, ch10, ch18.
- **Information as a measurable quantity.** Entropy, Boltzmann's microstates and Shannon information are reused to measure complexity and to ask what "information processing" means in living systems. Units: ch03, ch07, ch12.
- **Computation and self-reference.** Gödel and Turing rely on statements or machines that talk about themselves. The same dual use of information appears in self-copying programs and DNA. Computation is then asked of natural systems. Units: ch04, ch06, ch08, ch10, ch11, ch12.
- **Evolution, adaptation and the sources of order.** Selection and the Modern Synthesis are the starting point. Genetics supplies the mechanisms, genetic algorithms put selection to work, and the book ends by asking whether selection is the only source of complexity. Units: ch05, ch06, ch09, ch18.
- **Exploration balanced with exploitation.** Randomness plus feedback lets many simple agents search widely and then focus. Units: ch12, ch13 (restated in ch09's GA procedure only loosely, so mainly these two).
- **Models are useful but limited.** Idea models give insight, but results must be replicated and limits stated. Skepticism about network evidence and about "fact-free" modeling continues this theme. Units: ch02, ch14, ch16, ch19.
- **Networks, power laws and scaling.** Hubs, scale-free structure, fractal supply networks and Zipf-type laws raise questions that remain unsettled. Units: ch07 (fractals), ch15, ch16, ch17.

A cross-cutting point is that complexity has no single definition. See ch01, ch07 and ch19 (also ch12 on "information processing" being ill-defined).

## How to read it
- **Essential on a first pass (the catalog's focus):** ch01, ch02, ch03, ch04, ch07, ch10, ch17 and ch19.
- **Dependencies stated in the units:**
  - ch07 uses ch03 (Shannon entropy), ch04 (Turing machine) and ch02 (bifurcation diagram).
  - ch10 uses ch04 (universal machine).
  - ch17 uses the power-law idea from earlier chapters (ch15) and the Koch curve from ch07.
  - ch05 uses the second law from ch03.
  - ch19 names topics from all earlier chapters but needs no math.
- **Can be skipped at first (outside the catalog focus):**
  - ch05 (evolution) and ch06 (genetics) are background. ch06 is needed for ch08 and ch18.
  - ch08 follows from ch04 and ch06.
  - ch09 (genetic algorithms) and ch11 (computing with particles) are best read together with ch10. ch11 needs ch09 and ch10.
  - ch12 and ch13 form a pair: ch13 builds on ch12's exploration and exploitation, and ch12 builds on ch04 and ch10.
  - ch14 uses genetic algorithms and cellular automata.
  - ch15 and ch16 are read in that order. ch15 is useful before ch17 even though ch17 is the one in the focus.
  - ch18 uses ch02, ch06 and ch10.

## Concepts introduced
Ids are kept as written in the units, so some near-variants appear separately (for example `strange attractor / fractal` and `strange-attractor-fractal`).

- Chapter 1: [[complex system]], [[emergence]], [[self-organization]], [[adaptation]], [[market-efficiency]], [[complexity measures]]
- Chapter 2: [[nonlinearity]], [[fixed point and stability]], [[attractor / basin of attraction]], [[strange attractor / fractal]], [[bifurcation]], [[period-doubling route to chaos]], [[deterministic chaos]], [[universality]], [[sensitive-dependence-on-initial-conditions]], [[idea-model]], [[unimodal-map]]
- Chapter 3: [[entropy]], [[second-law-of-thermodynamics]], [[arrow-of-time]], [[microstate-macrostate]], [[shannon-information]], [[bit]], [[channel-capacity]], [[landauer-erasure-principle]]
- Chapter 4: [[computation]], [[hilbert-three-questions]], [[godel-incompleteness]], [[definite-procedure]], [[turing-machine]], [[universal-turing-machine]], [[halting-problem]], [[entscheidungsproblem]]
- Chapter 5: [[natural-selection]], [[lamarckian-inheritance]], [[mendelian-inheritance]], [[modern-synthesis]], [[random-genetic-drift]], [[punctuated-equilibria]], [[historical-contingency]], [[path dependence]], [[biological-constraints]]
- Chapter 6: [[gene]], [[genetic-code]], [[dna-base-pairing]], [[transcription-translation]], [[gene-expression]], [[mutation-and-recombination]], [[mitosis-meiosis]], [[tipping-point]], [[self-reference-in-dna]]
- Chapter 7: [[shannon-entropy]], [[algorithmic-information-content]], [[effective-complexity]], [[occams-razor]], [[logical-depth]], [[thermodynamic-depth]], [[coarse-graining]], [[statistical-complexity]], [[self-similarity]], [[fractal-dimension]], [[hierarchy and near-decomposability]]
- Chapter 8: [[self-reproduction]], [[infinite-regress]], [[dual-use-of-information]], [[interpreter]], [[artificial-life]], [[cybernetics]]
- Chapter 9: [[genetic-algorithm]], [[fitness-function]], [[crossover-and-mutation]], [[genotype-vs-phenotype]], [[gene-interaction]], [[knockout-test]]
- Chapter 10: [[cellular-automaton]], [[cell-update-rule]], [[elementary-cellular-automata]], [[space-time-diagram]], [[universal-computation]], [[wolfram-four-classes]], [[principle-of-computational-equivalence]]
- Chapter 11: [[decentralized-computation]], [[majority-classification]], [[information-processing-structure]], [[cellular-automaton-particle]], [[signal]]
- Chapter 12: [[information-processing-in-living-systems]], [[two-levels-of-description]], [[decentralized-control]], [[feedback]], [[communication-via-sampling]], [[fine-grained-architecture]], [[parallel-terraced-scan]], [[exploration-vs-exploitation]], [[negative-selection]], [[meaning-as-fitness]]
- Chapter 13: [[conceptual-slippage]], [[analogy-making]], [[microworld]], [[exploration-exploitation-balance]], [[slipnet]], [[codelet]], [[copycat-temperature]], [[barrier-of-meaning]], [[agent-based-model]]
- Chapter 14: [[mechanistic-model]], [[prisoner-dilemma]], [[tit-for-tat]], [[micromotives-macrobehavior]], [[norms-and-metanorms]], [[spatial-structure-cooperation]], [[model-replication]], [[generative-explanation]]
- Chapter 15: [[small-world-network]], [[heavy-tail-power-law]], [[scale-invariance]], [[robustness-and-fragility]], [[network-node-link]], [[degree-and-hub]], [[clustering]], [[average-path-length]], [[network-thinking]], [[scale-free-network]]
- Chapter 16: [[hub]], [[preferential-attachment]], [[cascade]], [[synchronization]], [[self-organized-criticality]], [[highly-optimized-tolerance]], [[many-model-thinking]]
- Chapter 17: [[allometric-urban-scaling]], [[strange-attractor-fractal]], [[kleibers-law]], [[quarter-power-scaling]], [[surface-hypothesis]], [[metabolic-scaling-theory]], [[zipfs-law]], [[log-log-plot]]
- Chapter 18: [[genetic regulatory network]], [[genetic switch]], [[random Boolean network]], [[edge of chaos]], [[Evo-Devo]], [[robustness and fragility]]
- Chapter 19: [[more is different / constructionism]], [[feedback (positive/negative)]], [[self-organized criticality]], [[many-model thinking]], [[common-principles]], [[unified-theory]], [[general-system-theory]], [[autopoiesis]], [[computational-mechanics]]
