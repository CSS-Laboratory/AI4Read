---
id: mitchell-2009-guidedtour/ch18-evolution
work: mitchell-2009-guidedtour
unit: "Chapter 18 — Evolution, Complexified"
pages: 147–165
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
# Evolution, Complexified

## L0 — One line
New genetics (genes as regulatory networks, switches) and Kauffman's Random Boolean Networks are used to argue that natural selection is not the only source of biological complexity, though the evidence is still contested.

## L1 — The gist (≤ 120 words)
How, why, and whether evolution creates complexity is still open. Mitchell shows that molecular genetics has made the "gene" concept murky and has revealed networks of genes that switch each other on and off. Evo-Devo (evolutionary developmental biology) proposes that body diversity comes mostly from changes in genetic switches, not in genes. Kauffman used Random Boolean Networks (simple random on/off network models of genes; K = the number of inputs per node) to argue that at K = 2 order can arise by self-organization, without natural selection. His claims face criticism: unrealistic assumptions, effects of noise, and an attractor-count prediction that did not hold up. Mitchell ends by describing an "extended Synthesis" and three camps of evolutionists.

**Prerequisites:** DNA, genes and proteins at high-school level; the idea of a cellular automaton; the logistic map's move from fixed point to oscillation to chaos (chapter 2).

## L2 — Key ideas (5–10 bullets)
- The gene concept has become unclear: genes overlap, move, make several proteins, and are regulated without sequence change; experts disagree on what counts as a gene (pp. 149–151).
- Genes act in nonlinear regulatory networks, not as independent genes lined up like beads on a string; this troubles the biotech industry's assumptions and its gene patents (pp. 150–152).
- Evo-Devo proposes that diversity of body forms is largely due to changes in genetic switches (non-coding DNA stretches that turn genes on and off), so large changes can happen fast (pp. 153–155).
- Evo-Devo also claims that dependence on master genes (a small set of genes that regulate body-part formation) constrains possible body plans (pp. 156–157).
- Kauffman's Random Boolean Networks (RBNs) are simple models of gene regulation: on/off nodes with random links, K inputs each, and random rules. K = 2 gave an "interesting" regime, which he called the "edge of chaos" (pp. 158–161).
- Kauffman proposed that an attractor (a repeating cycle of network states) corresponds to a cell type, and so predicted about √N cell types for N genes (p. 161).
- Kauffman argued that self-organization, not only selection, produces order; he proposed what he called a candidate fourth law of thermodynamics (pp. 162–163).
- Problems for Kauffman's models: assumptions he himself admits are unrealistic, the effects of noise, and the √N attractor count not holding up in later simulations (pp. 163–164).
- Mitchell reports what some call an "extended Synthesis" and McShea's three camps (adaptationists, historicists, structuralists); evolutionary theory will be unified only when the camps show how their forces work as an integrated whole (pp. 164–165).

## L3 — Walkthrough

### Opening (p. 147)
Mitchell recalls the question from chapter 1: how evolution produced creatures with such a contrast between individual simplicity and collective sophistication. The apparent improbability of gradual accumulation of favourable mutations or of historical accident has been used from Darwin's time to the present by believers in divine creation or other supernatural means ("intelligent design") (p. 147). How, why and even if evolution creates complexity, and how to measure biological complexity, are, Mitchell says, still very much open (p. 147).

### Genetics, Complexified (pp. 147–148)
New technologies often transform a field. The "molecular revolution" in genetics (copying, sequencing, synthesising DNA, imaging, expression of thousands of genes at once) keeps revealing unexpected complexity (p. 148). The older view: DNA is a string of genes, each coding for one protein, like the cell's "computer program". Small random copying errors accumulate; the favourable ones drive adaptive change and new species (p. 148). The revolution is also a new view of DNA, genes and evolution (p. 148).

### What Is a Gene? (pp. 148–152)
The chapter 6 mechanics (DNA transcribed, translated into proteins) still hold, but are only part of the story (p. 149). Examples:
- Genes are not like beads on a string: genes overlap or sit inside other genes (p. 149).
- Genes move ("jumping genes") within and between chromosomes, also in sperm and egg cells, so effects can be inherited. This can give a higher mutation rate than copying errors. Some scientists propose that such mobile elements might be responsible for differences between close relatives and even identical twins, and for some of the diversity of life (p. 149).
- One gene can code several proteins. Over 100,000 protein types may exist versus about 25,000 human genes. Alternative splicing and RNA editing alter messenger RNA after transcription and before translation, so the same gene can yield different proteins (pp. 149–150).
- In a survey, 500 biologists judged unusual real DNA sequences; for many, opinion split about 60% / 40%. Nature is quoted: expertise makes it harder to know what a gene is (p. 150).
- Networks, not independent genes: the old view (as in Mendel's laws) treats genes as linear, each contributing independently to the phenotype. The new, generally accepted view: genes work in nonlinear information-processing networks in which some genes control others (p. 150).
- Epigenetics: heritable changes in gene function with no change in DNA sequence. In DNA methylation, an enzyme attaches molecules to parts of the DNA and effectively turns them off. All descendants of that cell inherit it; if it happens in sperm or egg, it is inherited (p. 150). It happens all the time and is essential in many respects (e.g. turning off juvenile-development genes in adults), but incorrect or absent methylation is the cause of some disorders. Some think missing methylation explains why many cloned embryos or animals fail (pp. 150–151).
- Noncoding RNA: in most organisms much transcribed DNA is not translated into protein. This RNA has regulatory and functional roles once thought to belong only to proteins (p. 151).

Consequences: the Human Genome Project (2003) gave less than some had hoped; knowing the DNA sequence is "not nearly enough" to understand an organism's traits and defects (p. 151). The New York Times is quoted: the presumption that genes act independently is the economic and regulatory foundation of biotech since 1976 (p. 151). Mitchell asks whether gene patents are defensible if a "functional product" depends on epigenetic processes or on chains of regulating genes, some perhaps patented by others; with essential nonlinearity, she says, their meaning becomes very murky. The Times is also quoted saying that evidence of a networked genome undermines the scientific basis of nearly every official risk assessment of today's commercial biotech products (p. 152).

*Intuition note:* If genes work in networks, a gene's effect depends on many others, so one gene's sequence alone is a poor guide to a trait. Mitchell links the wider complexity (networks, epigenetics, splicing) to the finding that the sequence alone was not nearly enough to explain a person's traits (p. 151).

### Evo-Devo (pp. 152–156)
Evo-Devo ("evolutionary developmental biology") is claimed to answer at least three puzzles: (1) what makes humans complex with only about 25,000 genes; (2) why bodies differ from other animals' although over 90% of our DNA is shared with mice and over 95% with chimps; (3) how big morphological changes can occur quickly if punctuated equilibria (Gould and others) are right (p. 152).

Background: the Modern Synthesis treated development as a "black box" (Sean Carroll), expecting morphological diversity to come from large differences in gene number and makeup (p. 153). In the 1980s–90s embryologists found that all complex animals studied have a small set of "master genes" regulating body-part formation, sharing many DNA sequences across species as different as fruit flies and humans (p. 153).

Evo-Devo's proposal: morphological diversity is, for the most part, due to differences in **genetic switches**, not genes. Switches are non-coding DNA sequences, often several hundred base pairs long, once called "junk DNA" (p. 153). A switch sits near a gene and typically has about a dozen signature subsequences, each binding a particular protein. Whether and how fast the gene is transcribed depends on the combination of bound proteins. Some allow transcription by creating strong binding sites for transcribing RNA; some block it; some negate others (pp. 153–154; fig. 18.1). Regulatory proteins come from regulatory genes, whose own switches respond to proteins signalling the cell's state, often encoded by other regulatory genes (p. 154). A regulatory network thus has functional genes (maintenance or building) and regulatory genes (turning others on or off) (p. 154).

Evo-Devo's answers (p. 155):
1. Humans can be more complex than their gene count suggests for many reasons (see the gene section above); a primary reason is that networks allow a huge number of expression patterns, because proteins can attach to switches in so many ways.
2. Shared genes can differ in switch sequences; small switch changes give very different on/off patterns during development.
3. Large morphological changes, possibly including speciation, can be fast: master genes stay the same, switches change. Switch changes are, according to Evo-Devo, the major force in evolution rather than new genes.

*Intuition note:* Think of genes as the same set of instruments and switches as the sheet music: small edits to the music change what gets played and when. This is Evo-Devo's proposed explanation, as Mitchell reports it, of why similar genes can give very different bodies (p. 155); the sheet-music picture is ours.

**Finch beaks** (pp. 155–156). Until recently most biologists would have assumed beak variation came from gradual accumulation of chance mutations in several genes. The gene BMP4 helps control beak size and shape by regulating bone-producing genes; stronger expression gives larger, stronger beaks. Calmodulin is associated with long, thin beaks. Raising each gene's expression in chicken embryos produced finch-like beaks (wide and robust for BMP4, long for calmodulin). The reported conclusion: with just two genes, large beak changes can happen rapidly without waiting for many chance mutations (p. 156).

**Convergent evolution and PAX6** (p. 156). The octopus eye and human eye were taught as independent evolution. Humans, octopi, flies and others share the gene PAX6, which helps direct eye development. Gehring inserted mouse PAX6 into fly genome regions directing legs, wings and antennae; eye-like structures grew there, and they were fly-like, not mouse-like. His conclusion is that the eye evolved once, in a common ancestor with PAX6. Mitchell says this conclusion is "still quite controversial" (p. 156).

**Constraints** (pp. 156–157). Evo-Devo scientists claim body plans are highly constrained by master genes, which is why only a few basic plans are seen. On this view, very different genomes might give new plans, but in practice evolution cannot get there because we rely so heavily on existing regulatory genes. According to Evo-Devo, the notion that every trait can vary indefinitely is wrong (p. 157).

### Genetic Regulation and Kauffman's "Origins of Order" (pp. 157–163)
Stuart Kauffman, a theoretical biologist, has studied regulatory networks and their constraint on evolution for over forty years, and the "order" that emerges from them (p. 157). Mitchell gives a personal profile (physician turned geneticist, MacArthur award, Santa Fe Institute, a patent on evolving protein sequences in the lab) (pp. 157–158).

**Random Boolean Networks (pp. 158–160).** An RBN is an extension of cellular automata: nodes and directed links, discrete time steps, each node on or off (p. 158). A Boolean rule takes inputs of 0 or 1 and outputs 0 or 1 (p. 159). Every node has the same in-degree K (number of incoming links) (p. 159).
- *Build:* for each node, create in-links from K randomly chosen nodes (a self-link is possible) and give it a randomly chosen Boolean rule on K inputs (p. 159).
- *Run:* give each node a random initial state. At each step each node receives its inputs' states and applies its rule to get its next state (pp. 159–160). Fig. 18.2 shows five nodes with K = 2 over one step.
- Differences from cellular automata: links are random, not between spatial neighbours, and each node has its own rule (p. 160).
- Interpretation: nodes are "genes", and "A links to B" means "gene A regulates gene B". The model is far simpler than real networks (p. 160).

**Life at the edge of chaos (pp. 160–161).** From random starts, RBNs settle to a fixed point, an oscillation, or never settle (random-looking, chaotic, sensitive to initial state) (p. 160). Typical behaviour depends on the number of nodes and K. As K rises from 1 to the number of nodes, behaviour moves through fixed-point, oscillating and chaotic regimes, paralleling the logistic map as R increases (p. 160). At K = 2 Kauffman found an "interesting" regime, called the "edge of chaos" by analogy with "onset of chaos" (pp. 160–161).

Assuming RBNs reflect real genetic networks, and by analogy with phases of water, Kauffman concluded that genomic networks can be in a frozen ordered regime, a gaseous chaotic regime, or a "liquid" regime between (p. 161). He reasoned that to be alive and stable, networks must be in the liquid regime: "life exists at the edge of chaos" (p. 161).

**Attractors and cell types (p. 161).** A *global state* is a configuration of all node states. With finitely many nodes there are finitely many global states, so a long run must repeat one and then cycle. Kauffman called this cycle an *attractor*. By simulation he estimated that K = 2 networks have on average about √(number of nodes) attractors. He proposed that an attractor (a pattern of "gene expression" over time) represents a **cell type**, since cells share DNA but differ in expression patterns. For 100,000 genes the prediction was $\sqrt{100{,}000}\approx 316$ cell types, "not too far" from the roughly 256 identified in humans (p. 161). With the now-known 25,000 genes, the model predicts about 158 (p. 162).

*Intuition note:* A network with a finite number of states must eventually loop, and each loop is a stable long-run "pattern". Kauffman's bold step was to propose that each loop corresponds to a cell type in the body.

**The origin of order (pp. 162–163).** Kauffman believed his model illustrated his central point: natural selection is "in principle not necessary" to create a complex creature, since many K = 2 RBNs showed "complex" behaviour with no selection or evolutionary algorithm (p. 162). His view: once a network is complex enough (many nodes controlling others), complex, self-organized behaviour will emerge. He contrasts Darwinian biologists (order as a "Rube Goldberg machine" built piece by piece) with his thesis that most ontogeny order is spontaneous: "Order, vast and generative, arises naturally" (p. 162). Influenced by statistical mechanics, he proposed a statistical law for the emergence of complexity from many mutually regulating parts, a "candidate fourth law of thermodynamics": as the second law gives an innate tendency to rising entropy, his law proposes an innate tendency of life to become more complex, independent of selection (pp. 162–163). In Kauffman's view, as Mitchell puts it, evolution of complex organisms is due partly to self-organization and partly to selection, and perhaps self-organization is what predominates, severely limiting the possibilities for selection to act on (p. 163).

### Reactions to Kauffman's Work (pp. 163–164)
Reactions are strong. Admirers say his approach opens up new vistas, while skeptics doubt both his results and his broad interpretations; one reviewer called his style "dangerously seductive" (p. 163). Kauffman himself admits RBNs require unrealistic assumptions: binary states (real expression has degrees), identical in-degree, and synchronous discrete updating (p. 163). The most troublesome issue is noise: real networks make errors yet stay resilient, but simulations show noise significantly affects RBNs and sometimes prevents a stable attractor (pp. 163–164). Further simulations show the number of attractors is not well approximated by the square root of the number of nodes (p. 164). Mitchell notes this does not necessarily mean that Kauffman is wrong in his broader claims; it shows that more work on more accurate models is needed (p. 164).

### Summary (pp. 164–165)
Biology's complexity is only beginning to be appreciated. Some call the current direction an "extended Synthesis": selection remains important, but historical accidents, developmental constraints and self-organization join it (p. 164). Evolutionists, especially in the US, are under attack from religious extremists and are often on the defensive, reluctant to admit that natural selection may not be the entire story (p. 164); Hoelzer, Pepper and Smith say this defensiveness has a scientific cost (pp. 164–165). Dan McShea's three categories: **adaptationists** (selection primary), **historicists** (historical accident), **structuralists** such as Kauffman (organized structure without selection). Evolutionary theory will be unified only when they show how their forces work as an integrated whole (p. 165). McShea: "intellectual chaos" of a very productive kind (p. 165).

## Toy example (ours, not from the text)
A 3-node RBN, nodes A, B, C, each with K = 2. We chose the rules by hand (not randomly).
- A = B AND C
- B = A OR C
- C = A XOR B (on if exactly one input is on)

Start (A,B,C) = (1,0,1).
- Step 1: A = 0 AND 1 = 0; B = 1 OR 1 = 1; C = 1 XOR 0 = 1 → (0,1,1).
- Step 2: A = 1 AND 1 = 1; B = 0 OR 1 = 1; C = 0 XOR 1 = 1 → (1,1,1).
- Step 3: A = 1; B = 1; C = 1 XOR 1 = 0 → (1,1,0).
- Step 4: A = 1 AND 0 = 0; B = 1 OR 0 = 1; C = 1 XOR 1 = 0 → (0,1,0).
- Step 5: A = 1 AND 0 = 0; B = 0 OR 0 = 0; C = 0 XOR 1 = 1 → (0,0,1).
- Step 6: A = 0 AND 1 = 0; B = 0 OR 1 = 1; C = 0 XOR 0 = 0 → (0,1,0).

State (0,1,0) has returned, so (0,1,0) ↔ (0,0,1) is an attractor of period 2. There are only $2^3 = 8$ global states, so a repeat must happen. Another attractor is (0,0,0), a fixed point: A = 0 AND 0 = 0, B = 0 OR 0 = 0, C = 0 XOR 0 = 0. Different starts end in different attractors; in Kauffman's reading each would be a "cell type".

## Concepts
- [[complex system]] — here, living systems whose complexity is largely due to networks of interacting genes (p. 150)
- [[emergence]] — in Kauffman's view, complex, "self-organized" behaviour that emerges once a network has many nodes controlling other nodes (p. 162)
- [[nonlinearity]] — genes act in networks where some control others, not as independent additive effects (p. 150)
- [[attractor / basin of attraction]] — Kauffman's term for the repeating cycle of global states of an RBN; basins not discussed (p. 161)
- [[deterministic chaos]] — RBN behaviour that never settles, with sensitive dependence on the initial state (p. 160)
- [[robustness and fragility]] — genetic networks make errors all the time yet are usually resilient; in simulations noise significantly affects RBNs and sometimes prevents a stable attractor (pp. 163–164)
- [[self-organization]] (new) — order arising spontaneously in very complex regulatory networks; Kauffman argued selection is in principle not necessary for it (p. 162)
- [[genetic regulatory network]] (new) — functional and regulatory genes that switch each other on and off (p. 154)
- [[genetic switch]] (new) — non-coding DNA near a gene whose bound proteins control its transcription (p. 153)
- [[random Boolean network]] (new) — nodes with random links (in-degree K), random Boolean rules, synchronous updates (p. 159)
- [[edge of chaos]] (new) — Kauffman's "liquid" regime between frozen order and gaseous chaos, found at K = 2 (pp. 160–161)
- [[Evo-Devo]] (new) — view that diversity comes mainly from changes in switches, not genes (p. 153)

## Canonical instances
- [[random-boolean-network]] — Kauffman's gene-network model, with the √N attractor claim (pp. 159–161)
- [[finch-beaks-BMP4]] — beak size changed by regulating one gene's expression (pp. 155–156)
- [[PAX6-eye-experiment]] — mouse PAX6 triggers fly-type eyes on flies (p. 156)
- [[human-genome-project]] — complete sequence in 2003 did not give hoped-for understanding (p. 151)
- [[logistic-map]] — compared with RBN regimes as K rises (p. 160)

## Bridges (candidates)
- [structural-analogy] RBN regimes as K rises ↔ dynamical systems: logistic map as R rises — fixed point, oscillation, chaos in both
- [metaphor] Edge of chaos as "liquid" ↔ physics: phases of water — Kauffman's own analogy, not shared math
- [structural-analogy] RBN ↔ cellular automata: same synchronous discrete updating, but random wiring and per-node rules
- [metaphor] "Fourth law of thermodynamics" ↔ statistical mechanics: Kauffman's proposed law, not an established one

## Questions this raises
- Which features of real regulatory networks (graded expression, noise, unequal in-degree) would change the RBN regimes?
- If the attractor count is not √N, can the cell-type idea survive in a different form?
- How could one test whether self-organization or selection predominates?
- What evidence would settle the Gehring claim that the eye evolved only once?

## Reading notes
- Printed page = pdf − 188 (pdf 335 = printed 147).
- Text layer was clean. I checked figures 18.1 and 18.2 against the images. Fig. 18.1 shows two signature subsequences and two master genes, while the text says a switch typically has about a dozen. Fig. 18.2 shows five nodes, each with a rule.
- The page with Kauffman's photograph was not shown as an image; the caption is only in the text.
- The unit has no exercises. The statement that roughly 256 human cell types exist is the author's (p. 161).
