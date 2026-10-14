---
id: simon-1962-architecture/main
work: simon-1962-architecture
unit: paper
pages: 467–482
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# The Architecture of Complexity (Simon, 1962)

## L0 — One line
Complexity in nature often takes the form of hierarchy; systems with stable intermediate forms evolve much faster and are hierarchic, and the near-decomposability of many hierarchies simplifies their behavior and makes them easier to describe and understand.

## L1 — The gist (≤ 120 words)
Simon asks what nontrivial properties very different complex systems might share. His answer is hierarchy: systems made of subsystems, made of subsystems. Systems with stable intermediate forms evolve much faster than systems without them, and the resulting forms are hierarchic. Many hierarchies are also nearly decomposable: strong links within parts, weak links between parts. Short-run and long-run behavior can then be studied separately. This also makes such systems easier to describe, because much of their structure is redundant. Simon suggests that process descriptions (recipes) may be the economical way to describe such systems, including genetic information. The paper proposes a theory of hierarchy as one route to a nontrivial theory of complexity.

**Prerequisites:** basic probability (independent events, powers of a probability); idea of a matrix of coefficients; what "equilibrium" means in heat flow; elementary biology (cells, DNA).

## L2 — Key ideas (5–10 bullets)
- A "complex system" is many parts interacting in a nonsimple way; the whole is more than the sum of the parts only in a pragmatic sense. One can be a reductionist in principle and a holist in practice (p. 468).
- "Hierarchy" is used broadly: successive sets of subsystems, with no authority relation required. Very flat hierarchies (crystals, polymers) are treated as limiting cases: a crystal has a wide span at the crystal level, and a polymer is treated as span one (pp. 468–469, 471, 473).
- Watchmaker parable: with interruption probability about .01 per added part, assembly using stable subassemblies is about 4,000 times faster (Simon says the number is not to be taken seriously). In his model, evolution time is proportional to the number of levels, $\log_s n$ (pp. 470–471).
- Selectivity, in evolution and in problem solving, is feedback of information from the environment about stable or promising configurations. Simon says it is this information, and not free energy from the sun, that guides evolution (pp. 472–473).
- Near-decomposability: short-run behavior of components is nearly independent; long-run behavior depends only on aggregates. It appears in heat flow, economies, organizations and chemistry (pp. 474–476).
- Hierarchy aids comprehension: little information is lost by treating interaction between parts in aggregate. Systems that are complex but not hierarchic may escape our understanding (p. 477).
- Most complex structures are redundant, and that often makes simple description possible. Three forms of redundancy are named; the right representation is needed to exploit them (pp. 478–479, 481).
- Blueprints (state descriptions) and recipes (process descriptions) are linked; problem solving looks for the recipe for a given blueprint. Genetic information appears to be recorded as a process description (pp. 479–480).

## L3 — Walkthrough

### Introduction (pp. 467–468)
- Simon notes proposals for a "general systems theory" covering physical, biological and social systems. **Objection he anticipates:** such diverse systems can hardly share nontrivial properties. His reply is that a metaphor helps or misleads depending on whether the similarities are significant or superficial (p. 467).
- He will report theories that arose in specific behavioral-science contexts. They say little about structural details, so they may be relevant to other complex systems. He leaves the judgment of relevance to the reader (p. 467).
- **Definition:** a complex system is one made of a large number of parts that interact in a nonsimple way. The whole is more than the sum of its parts in a pragmatic rather than an ultimate, metaphysical sense: given the parts' properties and the laws of interaction, inferring the whole's properties is not trivial (p. 468).
- Hence "an in-principle reductionist may be at the same time a pragmatic holist" (p. 468). Footnote 4 notes Weaver's split between disorganized and organized complexity. Simon is concerned mainly with organized complexity (p. 468).
- Four sections follow: hierarchy's frequency; its evolution; its dynamics; the relation between complex systems and their descriptions. The theme is that complexity frequently takes the form of hierarchy (p. 468).

### Hierarchic systems (pp. 468–470)
- **Definition:** a hierarchic system is composed of interrelated subsystems, each hierarchic in turn, down to some lowest level of "elementary" subsystem. Where to stop is somewhat arbitrary. Atoms were elementary until recently; a cell, protein or amino acid may be elementary depending on the research (p. 468).
- Simon uses "hierarchy" more broadly than the formal-organization sense (boss plus subordinate subsystems). He includes systems with no subordination. "Formal hierarchy" names the narrow case (p. 468). Footnote 6: mathematical "partitioning" does not suffice; a hierarchy is a partitioning plus the relations among its parts (p. 468).
- **Examples:**
  - Social: firms, governments, families grouped into villages and tribes. Groups are found from who interacts with whom, not who lives near whom (p. 469).
  - Biological: cells → tissues → organs → systems; organelles inside the cell (p. 469).
  - Physical: particles, atoms, molecules, macromolecules; satellites, planetary systems, galaxies. Gases are random distributions of molecules, not of elementary particles (p. 469).
  - Symbolic: books (chapters → sections → paragraphs → sentences → words), music (p. 469–470).
- **Span:** the number of subsystems a system is partitioned into, analogous to a boss's span of control. A diamond has a wide span at the crystal level; a linear polymer is a very flat hierarchy at the molecular level. The later theory focuses on moderate spans (p. 469).
- Physical and biological hierarchies are usually spatial, but social ones are identified by interaction. The two views reconcile if hierarchy is defined by intensity of interaction, because intense interaction usually implies spatial nearness. Nerves and telephone wires weaken this link (p. 469).

*Intuition note:* Here hierarchy means parts inside parts. Simon allows it to be defined by intensity of interaction as well as by nesting, and he does not require bosses (formal hierarchy is only the special case).

### The evolution of complex systems (pp. 470–473)

**The parable (p. 470).**
- Tempus and Hora each build watches of about 1,000 parts. If Tempus is interrupted, the unfinished watch falls apart. Hora builds stable subassemblies: ten of ten parts, ten of those, then ten of those. An interruption costs Hora only a small part of his work.
- Let $p$ be the probability of interruption while adding one part.
  - Tempus completes a watch uninterrupted with probability $(1-p)^{1000}$. Each interruption costs on average the time for $1/p$ parts.
  - Hora completes a ten-part subassembly with probability $(1-p)^{10}$. Each interruption costs about five parts. He must make 111 subassemblies.
- With $p = .01$, the time ratio (Tempus : Hora) is built from three ratios:
  1. Hora makes 111 times as many assemblies, giving the factor $1/111$.
  2. Tempus loses 20 times as much per interruption (100 parts against 5).
  3. $.99^{1000} = 44\times10^{-6}$ and $.99^{10} = 9\times10^{-1}$, so Tempus needs $20{,}000$ times as many attempts per completed assembly.

$$\frac{1}{111}\times\frac{100}{5}\times\frac{.99^{10}}{.99^{1000}} = \frac{1}{111}\times 20\times 20{,}000 \sim 4{,}000.$$

Tempus takes about 4,000 times as long as Hora on average (p. 470).

*Intuition note:* Every interruption destroys unfinished, unstable work. Stable subassemblies cap what an interruption can destroy.

**Lessons for biological evolution (p. 471).**
- Read a partial subassembly of $k$ parts as $k$ parts coexisting in a small volume. Parts arrive at a constant rate and disperse with constant probability $p$ unless the assembly is stable. Simon admits these assumptions are unrealistic and probably understate hierarchy's advantage by a large factor. So the number is not to be taken seriously (p. 471).
- The lesson: evolution time depends critically on the number and distribution of potential stable intermediate forms. With about the same span $s$ at each level, time per subassembly is about the same, proportional to $1/(1-p)^s$. Assembling $n$ elements takes time proportional to $\log_s n$, the number of levels (p. 471).
- Illustratively, not literally: multi-celled organisms from single cells might take about as long as single cells from macromolecules (p. 471).
- Three objections he mentions (p. 471):
  - No teleology is assumed. Direction comes from the stability of complex forms, which Simon calls nothing more than survival of the fittest, i.e. of the stable.
  - Not all large systems look hierarchic (e.g., nylon polymers). Simon treats these as hierarchy with span one.
  - Entropy: evolution of complexity implies nothing about the entropy of the entire system. Organisms are not closed energetically, so classical thermodynamics gives neither the direction nor rate of evolution (p. 471).
- The entropy involved in forming a one-celled organism is trivially small, about $10^{-11}$ cal/degree. The "improbability" of evolution is not about this quantity. Copying a cell needs as much information as producing the first cell (pp. 471–472).
- Footnote 7: Jacobson's information-theoretic model, which ignored stable intermediate forms, gave estimates so large that evolution looked improbable. Simon's analysis, which includes them, gives much smaller estimates (p. 470).
- Simon likens the effect of stable intermediate forms to that of catalysts in open systems; in neither case does entropy change guide behavior (p. 472).

**Problem solving as natural selection (p. 472).**
- Theorem proving can be described as a search through a maze. The search is selective trial and error: signs of progress encourage a line of search; lack of progress ends it (p. 472).
- Clicking safe: 10 dials, 100 settings each.
  - Blind search: $100^{10}$ settings, so about half of them are tried on average, "fifty billion billion".
  - If a click sounds when a dial is correct, each dial can be set independently: $10 \times 50 = 500$ settings (p. 472).
- Cues signaling progress play the role of stable intermediate forms. Everything learned about problem-solving mazes points to problem solving as nothing more than varying mixtures of trial and error and selectivity (p. 472). Selectivity comes from heuristics. No process more sophisticated than organic evolution is needed to cut down the mazes (p. 473).
- Footnote 13: the watchmaker model gives a very conservative estimate of hierarchization's savings. The safe may give too high an estimate because it treats all arrangements as equally probable (p. 472).

**Sources of selectivity (p. 473).**
- Selectivity "can always be equated with some kind of feedback of information from the environment." In evolution it is information about stable configurations, not free energy or negentropy from the sun, that guides evolution and gives its rapidity (p. 473).
- Problem solving has two sources: feedback from trying paths, and previous experience. The closest evolutionary analogue of previous experience is reproduction. Reproduction allows inheritance of acquired characteristics, but only at the level of genetic material: only characteristics acquired by the genes can be inherited (p. 473).

**Empires (p. 473).** Philip's Macedonian subassembly was later combined into Alexander's empire. After Alexander's death it fragmented into its earlier subsystems rather than crumbling to dust. The watchmaker argument implies that empire-building is easier where large stable political systems already exist. Simon leaves any lesson for history to historians (p. 473).

**Conclusion of the evolutionary argument (p. 473).** Complex systems evolve from simple ones much more rapidly if stable intermediate forms exist, and the resulting forms are hierarchic. Turning the argument around explains the predominance of hierarchies: among possible complex forms, "hierarchies are the ones that have the time to evolve." The hypothesis does not distinguish flat hierarchies from others, and a fuller theory would address width of span (p. 473).

### Nearly decomposable systems (pp. 473–477)
- Interactions among subsystems and within subsystems are often of different orders of magnitude. Examples: employees within versus across departments; nuclear forces > molecular > intermolecular (p. 474).
- A rare gas is decomposable into independent particles, with a perfect-gas theory as a first approximation. Nearly decomposable systems are the second approximation: weak but not negligible interaction among subsystems (p. 474).
- **Two propositions** (p. 474):
  - (a) In the short run, each component's behavior is approximately independent of the others.
  - (b) In the long run, each component depends on the others only in an aggregate way.
- **Heat example** (pp. 474–475; based on Simon–Ando, fn. 15).
  - A building has perfectly insulating outer walls. Rooms are separated by good but imperfect insulators; each room is divided into cubicles by poor insulators; one thermometer per cubicle.
  - Starting from disequilibrium: after hours, temperatures are nearly uniform within each room but still differ among rooms. After days, the whole building is nearly uniform (p. 474).
  - Let $r_{ij}$ be the rate heat flows from cubicle $i$ to $j$ per degree of difference. It is zero without a common wall, large within a room, nonzero but small across a room wall.
  - Grouping cubicles by room puts all large elements in square submatrices along the diagonal. Elements outside them are zero or at most a small $\varepsilon$ (Fig. 1). Such a matrix is a *nearly decomposable matrix* (p. 475).
  - Simon states that it has been proved that a dynamic system described by such a matrix has properties (a) and (b). So each room reaches its own equilibrium first, and then one thermometer per room suffices (p. 475).
- **How special is the property?** Near-decomposability is strong for a matrix. Few thinkable dynamic systems have it, and fewer as $\varepsilon$ shrinks. But nearly decomposable systems are common in nature, while systems where every variable links equally strongly to almost all others are rarer and less typical (p. 475).
- **Social and economic systems (p. 475).**
  - In the economy, prices and quantities of a commodity depend significantly on only a few others plus aggregates. Input-output matrices show near-decomposability, with one qualification: the consumption subsystem links strongly to most others.
  - In organizations, formal authority links each member to one superior and a few subordinates, and other channels also reach few people. Departmental boundaries act like the walls in the heat example.
- **Physico-chemical systems (pp. 475–476).**
  - Take nuclei as parts. Bond strengths fall in groups: covalent, ionic, hydrogen, van der Waals. An $\varepsilon$ just below covalent strength makes molecules the subsystems (p. 475).
  - Higher-frequency vibrations belong to smaller subsystems (molecular vibrations are lower in frequency than electron vibrations, which are lower than nuclear ones). Molecular systems are nearly decomposable: internal structure gives short-run dynamics, interaction of subsystems gives long-run dynamics (p. 476).
  - Some physical approximations depend on this property. Irreversible-process thermodynamics assumes macroscopic disequilibrium with microscopic equilibrium; quantum calculations treat weak interactions as perturbations (p. 476).
- **Observations on span (p. 476).**
  - The critical consideration is how far interaction between two or a few subsystems excludes their interaction with others. If a combination keeps as many external bonds as its parts, bonding can continue indefinitely (crystals, polymers). If fewer, agglomeration halts.
  - Gases do not agglomerate because bonding uses up capacity ($O_2$ has zero valence). Indefinite chains of single-bonded carbon atoms can be built up because a chain of any number of such atoms, each with two side groups, has a valence of exactly two.
  - With both strong and weak bonds, strong ones are used up first and subsystems then link by weaker second-order bonds (water's dipole).
  - Gravity dominates astronomically although electrical forces are stronger, because bipolar electrical forces are "used up" in small subsystems (p. 476).
  - Social limits: a person is closer to a serial than a parallel information processor, and roles take time (one cannot be a friend to very many) (pp. 476–477).
- Simon says it is "probably true" in social as in physical systems that higher-frequency dynamics belong to subsystems. Executives' planning horizons are generally believed to lengthen with rank; interactions are probably longer and rarer higher up (p. 477).
- **Summary:** intra-component links are generally stronger than inter-component links. This separates high-frequency internal dynamics from low-frequency dynamics among components (p. 477).

*Intuition note:* If parts talk mostly to their own group, one can first study each group alone (fast) and then the groups as units (slow). That is why one thermometer per room is enough after the first hours.

### The description of complexity (pp. 477–481)
- **Drawing and comprehensibility (p. 477).** Asked to draw a face, a person will almost always proceed hierarchically: outline, then features, then details. Information is stored like a topical outline. It is easy to include relations among major parts and within parts, but relations between subparts of different parts have no place in the outline and are likely to be lost. Footnote 20 cites Miller's drawing protocols (private communication) (p. 477).
- Since little information is lost by treating interactions between parts in aggregate, hierarchy helps us understand and "see" systems. Put the other way round, if important systems are complex without being hierarchic, they may to a considerable extent escape our observation and understanding (p. 477).
- Simon will not settle "chicken or egg": whether we understand the world because it is hierarchic, or it looks hierarchic because we cannot grasp the rest. He says he has given some reasons for supposing the former is "at least half the truth" (that evolving complexity would tend to be hierarchic), but it may not be the whole truth (p. 478). Footnote 21: he believes the fallacy in Elsasser's central thesis lies in ignoring the simplification that hierarchic structure brings, and concludes we should not despair of unravelling the web of causes (pp. 477–478).

**Simple descriptions (p. 478).**
- Descriptions need not be as cumbersome as the object. Example: an $8\times8$ array of letters, built from $2\times2$ blocks $a, m, r, h$ (e.g. $a=\begin{smallmatrix}AB\\CD\end{smallmatrix}$). Define $w=\begin{smallmatrix}am\\ma\end{smallmatrix}$, $x=\begin{smallmatrix}rh\\hr\end{smallmatrix}$, and $S=\begin{smallmatrix}wx\\xw\end{smallmatrix}$. The 64 symbols need only 35 to describe (p. 478).
- A completely unredundant structure is its own simplest description. Hierarchic structures are highly redundant. Three forms of redundancy (p. 478):
  1. A few kinds of subsystems in many arrangements (twenty amino acids; ninety-odd elements), so a restricted alphabet suffices.
  2. Hierarchic systems are often nearly decomposable, so only aggregate properties of their parts enter the description of their interactions. A generalization of near-decomposability, which Simon calls the "empty world hypothesis": most things are only weakly connected with most others, so for a tolerable description only a tiny fraction of possible interactions need be described.
  3. Recoding: replace a time path with a differential law generating it. Example: $1, 3, 5, 7, 9, 11\ldots$ is "add 2 to the previous one". Galileo found this sequence for a ball rolling down an inclined plane (pp. 478–479).

**State and process descriptions (p. 479).**
- *State description*: characterizes the world as sensed (pictures, blueprints, structural formulae; e.g. the definition of a circle as the locus of points equidistant from a given point). *Process description*: characterizes the world as acted upon (recipes, differential equations, reaction equations; "rotate a compass…") (p. 479).
- Adaptive organisms must correlate goals in the sensed world with actions in the world of process. Made conscious, this is means-end analysis: find the difference between desired and existing states, then the process that erases it (p. 479).
- This addresses a paradox from Plato's *Meno* (voice: Plato, who argued that all learning is remembering). We pose a problem by giving a state description of the solution. Translating process descriptions into state descriptions lets us recognize success, so the solution is genuinely new (p. 479).
- Simon cites a growing body of evidence that human problem solving is basically means-end analysis seeking a process description: "given a blueprint, to find the corresponding recipe". Much of science fits this paradigm (p. 479).

**Self-reproducing systems (pp. 479–480).**
- Complexity does not imply self-reproduction (heavy atoms, inorganic molecules). If a complex form raises the probability of creating another like itself, the equilibrium between complexes and components could shift greatly toward complexes (p. 479).
- A sufficiently clear and complete description lets us reproduce an object. Perhaps the simplest possibility is a template: a DNA double helix unwinds and each half serves as template for a new matching half (p. 480).
- Under the "prevailing theory": DNA is template for itself and RNA, RNA for protein. But proteins guide metabolism as catalysts. So "RNA is a blueprint for protein, protein is a recipe for metabolism" (p. 480; fn. 24 says Anfinsen qualifies this sketchy account).

**Ontogeny recapitulates phylogeny (pp. 480–481).**
- If current theories are even approximately correct, genetic information is recorded not as a state description of the organism but as instructions, like a recipe or computer program. Viewed as a program, it is self-reproducing and has developed by Darwinian evolution; by the watchmaker argument, Simon says, many of its ancestors were also viable programs (p. 480).
- The biological generalization "ontogeny recapitulates phylogeny" (individual development resembles ancestral forms) holds, Simon says, "in rough approximation", despite biologists' qualifications. One interpretation: solve a new problem by reducing it to an earlier solution. Compare telling a workman to turn a wagon into an automobile; or construct a gastrula by altering a blastula (p. 480).
- Cell division would require, as a minimum, a state description (DNA) plus a simple interpretive process that copies it; that would not suffice for differentiation. It appears more natural to base differentiation on a process description with a more complex interpretive process, each stage an operator acting on the previous one. How the two interrelate is harder to conceptualize. The single clue from the earlier discussion is that the description may be hierarchical or nearly decomposable: lower levels govern fast cell dynamics, higher levels slow dynamics of the developing organism (pp. 480–481).
- Simon says there are only bits of evidence, apart from the facts of recapitulation, that the genetic program is organized this way, but what exists is compatible with the notion; footnote 25 cites some. Simon says he has perhaps pressed the speculation far enough (p. 481).
- General claim: when descriptions of evolving systems are stored in a process language, ontogeny may partially recapitulate phylogeny. Education is an example: advanced courses often replay a science's conceptual history. The recapitulation is seldom literal, and it may sometimes be the most expeditious route (p. 481).

**Summary on description (p. 481).** How complex a structure is depends critically on how we describe it. Most complex structures are enormously redundant, but exploiting that needs the right representation. Replacing state descriptions by process descriptions has been central to modern science. Simon suggests the multi-cellular organism's genetic program is a parsimonious representation of itself (p. 481).

### Conclusion (pp. 481–482)
- Thesis: a theory of hierarchy is one path to a nontrivial theory of complex systems. Empirically many natural complex systems are hierarchic. Theoretically we expect it if complexity had to evolve from simplicity. Near-decomposability simplifies dynamics and description, and makes it easier to see how developmental information can be stored "in reasonable compass" (p. 482).
- "Systems" studies are popular more from need than from a developed body of knowledge. The explorations here are one direction for supplying substance (p. 482).

## Toy example (our own, not from the text)
Build 16 parts; each part-addition is interrupted with probability $p = 0.1$, and an interruption destroys the unstable assembly. Crude work measure for a stage with $k$ parts: $k / 0.9^k$ (each attempt is charged the full $k$ additions, which overstates the cost of failed attempts equally in both cases).

- **Flat:** $0.9^{16} = 0.1853$ (since $0.9^2=0.81$, $0.9^4=0.6561$, $0.9^8=0.4305$, $0.9^{16}=0.1853$). Work $\approx 16/0.1853 = 86.3$.
- **Span 4:** four subassemblies of 4 parts, then one assembly joining the 4 subassemblies: 5 stages of $k=4$. Each stage: $4/0.6561 = 6.10$. Total $\approx 5 \times 6.10 = 30.5$.
- Ratio $\approx 86.3/30.5 \approx 2.8$. With more parts the advantage grows quickly; Simon's own figure for 1,000 parts and $p=.01$ uses a different cost measure and is about 4,000 (p. 470). With span 4 the number of levels is $\log_4 16 = 2$ (added step).

## Concepts
- [[complex-system]] — many parts interacting in a nonsimple way; inferring the whole from parts is not trivial (p. 468)
- [[more-is-different-constructionism]] — in-principle reductionism can coexist with pragmatic holism (p. 468)
- [[organized-vs-disorganized-complexity]] — Weaver's distinction, cited; Simon focuses on organized complexity (p. 468, fn. 4)
- [[hierarchy-and-near-decomposability]] — hierarchy = successive subsystems, no authority relation required; near-decomposability = strong within, weak between, giving separated fast and slow dynamics (pp. 468, 474)
- [[span-of-hierarchy]] (new) — number of subsystems a system is partitioned into; flat = wide span (p. 469)
- [[stable-intermediate-forms]] (new) — stable subassemblies that persist and serve as building blocks; they speed evolution (pp. 470–471)
- [[selective-trial-and-error]] (new) — trial and error guided by selectivity: cues about progress or stable forms steer the search, in problem solving and in evolution (pp. 472–473)
- [[feedback]] — selectivity equals feedback of information from the environment (p. 473)
- [[empty-world-hypothesis]] (new) — most things are only weakly connected to most others; so descriptions can omit most possible interactions (p. 478)
- [[redundancy-in-description]] (new) — structure inferable from other structure; allows economical description (p. 478)
- [[state-vs-process-description]] (new) — blueprint (world as sensed) versus recipe (world as acted upon) (p. 479)
- [[means-end-analysis]] (new) — find the difference between desired and existing states, then the process that removes it (p. 479)

## Canonical instances
- [[hora-tempus-watchmakers]] — hierarchy's evolutionary advantage; ratio about 4,000 (p. 470)
- [[clicking-safe]] — feedback cues cut an expected search of about half of $100^{10}$ settings to 500 (p. 472)
- [[heat-exchange-cubicles]] — nearly decomposable matrix and two-stage equilibration (pp. 474–475)
- [[input-output-economy]] — economic near-decomposability, with the consumption subsystem as exception (p. 475)
- [[covalent-bond-hierarchy]] — bond strengths and frequencies give molecular near-decomposability (pp. 475–476)
- [[array-description-64-to-35]] — redundancy gives a 35-symbol description of 64 symbols (p. 478)
- [[dna-rna-protein-blueprint-recipe]] — blueprint-versus-recipe in genetic mechanisms (p. 480)
- [[alexander-empire]] — stable political subsystems as building blocks (p. 473)

## Bridges (candidates)
- [structural-analogy] Near-decomposability ↔ complex-systems: time-scale separation between fast within-module and slow between-module dynamics — block-structured coupling gives two time scales (pp. 474–475).
- [structural-analogy] Aggregate-only long-run dependence ↔ complex-systems: mean-field approximation — both replace detailed neighbors with an average (p. 474).
- [structural-analogy] Stable intermediate forms ↔ complex-systems: building blocks and path dependence — existing stable units constrain and speed later construction (p. 473).
- [metaphor] Clicking safe ↔ complex-systems: tipping-point or feedback-guided search — cues turn blind search into incremental progress (p. 472).

## Questions this raises
- How do heterogeneous spans (flat versus narrow hierarchies) arise? Simon says a fuller theory would address the determinants of width of span (p. 473).
- Which important systems are complex but not hierarchic, and do they escape our understanding, or only our current methods (p. 477)?
- How do the state description (DNA as copied) and process description (development) interrelate in the genetic program (p. 481)?
- When a nearly decomposable structure has exceptions (like the consumption subsystem), how should the theory be modified (p. 475)?

## Reading notes
- Printed pages 467–482; the PDF's first page (printed 466) is the JSTOR cover sheet, so printed = pdf + 465. Source journal: *Proceedings of the American Philosophical Society* 106(6), Dec. 12, 1962. The paper was read April 26, 1962 (p. 467).
- The text layer is OCR-noisy (e.g. "Xewell", "IVe", broken exponents). I checked pages 470, 473 and 478 against page images. Exponents and numbers elsewhere (e.g. the entropy figure of order $10^{-11}$ cal/degree, which the text layer may give with a minus sign that I could not confirm, and "about $10^{13}$ bits" in fn. 10, p. 471; wave numbers in fn. 17) are from the text layer only.
- Figure 1 (p. 474) was not inspected in image form; I give no numerical entries from it.
- Small slips in the source: on p. 475 the room equilibrium is called an average of "offices" although the example uses cubicles. On p. 470 the text says Hora makes 111 times as many assemblies; the formula uses $1/111$ for the Tempus : Hora time ratio, which is consistent.
- The paper contains no exercises.
