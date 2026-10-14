---
id: mitchell-2009-guidedtour/ch07-defining
work: mitchell-2009-guidedtour
unit: Chapter 7 — Defining and Measuring Complexity
pages: pdf 125–145 (printed page numbers not available)
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
# Defining and Measuring Complexity

## L0 — One line
There is no single agreed definition of complexity; many proposed measures each capture something about it (size, randomness, construction effort, organization, detail across scales, hierarchy), and all have theoretical and practical limits.

## L1 — The gist (≤ 120 words)
Mitchell asks how to define and measure complexity, for example whether the human genome is more complex than the yeast genome. Even the Santa Fe Institute faculty gave different definitions, so she says there are "several different sciences of complexity." Size and Shannon entropy are poor measures: the amoeba's genome is larger than ours, and random strings get the highest entropy. Other measures aim to match intuition better: effective complexity and statistical complexity score both order and randomness low; logical and thermodynamic depth measure construction effort; fractal dimension and degree of hierarchy measure detail across scales and nesting. All have theoretical or practical limits, and she thinks complexity probably cannot be captured by a single scale.

**Prerequisites:** Shannon entropy (ch. 3); Turing machine; logistic-map bifurcation diagram (ch. 2); powers and exponents.

## L2 — Key ideas
- Lack of a universal definition of a central term is common in science. Complexity currently has several formal and informal notions (pdf 125–126).
- Lloyd's three questions organise the measures: how hard to describe, how hard to create, what degree of organization (pdf 127).
- Size (base pairs or genes) and Shannon entropy (the average information, or surprise, of a message source) do not match intuition. The amoeba has more base pairs than humans, and a random genome gets maximum entropy (pdf 128–130).
- Algorithmic information content (the length of the shortest program that generates a description of the object) also ranks random objects as most complex. Gell-Mann's effective complexity, which measures only the regularities, is low for both ordered and random things (pdf 130–131).
- Logical depth and thermodynamic depth measure construction effort (Turing-machine steps, or physical and informational resources). Both are appealing in theory but have practical problems as measures (pdf 133–134).
- Statistical complexity (the information in the simplest model that predicts a system's statistical behaviour) is low for ordered and random systems and high in between. It has been measured for real crystals and neurons (pdf 135–136).
- Fractal dimension comes from self-similarity: if each side is divided by $x$, each level has $x^{\text{dimension}}$ copies. For the Koch curve (a shape built by replacing the middle third of each segment with two sides of a triangle), $3^{D}=4$ gives $D\approx 1.26$ (pdf 142).
- Simon described complexity through degree of hierarchy and near-decomposability (many more strong interactions within subsystems than between them). McShea's nestedness scale was used to show that the maximum hierarchy in organisms increases over evolutionary time, though measuring it involves some subjectivity. Mitchell says the diversity of measures indicates that complexity has many interacting dimensions and probably cannot be captured by a single scale (pdf 144–145).

## L3 — Walkthrough

### Opening: why define complexity? (pdf 125–126)
- Open questions: is a human brain more complex than an ant brain? Is the human genome more complex than yeast's? Did biological complexity increase over four billion years? Intuition says "of course," but no universally accepted definition helps answer them (pdf 125).
- In 2004 the Santa Fe Institute (SFI) panel was asked how to define complexity. Each member gave a different definition, and some argued (pdf 125).
- Mitchell's answer: there is not yet one science of complexity but several, with different notions, some formal and some informal. A unified science would need to relate these notions (pdf 125–126).
- She argues the students should not be shocked. Newton lacked a good definition of force. Geneticists disagree on what a gene is at the molecular level. Astronomers do not know what dark matter and dark energy are. Psychologists lack precise definitions of idea and concept (pdf 126).
- Science often invents terms for poorly understood phenomena and refines them later. Forces are now seen as four fundamental kinds. Perhaps complexity will likewise be split into basic aspects and later unified (pdf 126).

### Lloyd's three dimensions (pdf 127)
- Lloyd (2001) proposed three questions: How hard is it to describe? How hard is it to create? What is its degree of organization? He listed about forty proposed measures, drawing on dynamical systems, thermodynamics, information theory and computation (pdf 127).
- Running example: the human genome has about 3 billion base pairs and about 25,000 genes (regions coding for proteins). Only about 2% of base pairs are in genes; the rest are noncoding regions, with several functions and possibly some "junk." The first sequenced yeast has about 12 million base pairs and 6,000 genes (pdf 127).

### Complexity as size (pdf 127–128)
- By base pairs, humans are about 250 times as complex as yeast; by genes, about 4 times (pdf 127–128).
- But the amoeba has about 225 times as many base pairs as humans, and the mustard plant *Arabidopsis* has about as many genes as we do (pdf 128).
- Mitchell concludes that genome size is not a very good measure of complexity (pdf 128).

*Intuition note:* Counting base pairs or genes gives a number, but Mitchell says our complexity must come from something deeper. A bigger genome is not obviously a more complex organism.

### Complexity as entropy (pdf 128–130)
- Shannon entropy is the average information or "amount of surprise" of a message source (ch. 3). Here the messages are the symbols A, C, G, T. The sequence AAAA… has entropy 0. A completely random sequence has the maximum entropy (pdf 128).
- Problem 1: the object must be put into "messages," which is not always easy (for example, a brain). Problem 2: a random artificial genome would count as more complex than the human genome (pdf 129).
- Mitchell's conclusion: the most complex entities are somewhere between ordered and random, so simple entropy does not capture intuitive complexity (pdf 130).

### Complexity as algorithmic information content (pdf 130)
- Kolmogorov, and independently Chaitin and Solomonoff, defined an object's complexity as the length of the shortest program that generates a complete description of it. This is its algorithmic information content (pdf 130).
- String 1 (ACAC…, 20 letters) is produced by a short program that prints A C ten times, so it is compressible and has low content. String 2 (from a pseudo-random generator, assumed good) needs a program that prints the exact string, so it has more content (pdf 130).
- Like entropy, this assigns higher content to random objects than to what we intuitively call complex (pdf 130).

### Effective complexity (Gell-Mann) (pdf 131–132)
- Idea: an entity combines regularity and randomness. Find the best description of its regularities. The effective complexity is the information in that description, which is the algorithmic information content of the set of regularities (pdf 131).
- String 1: regularity "A C repeated," so effective complexity is low. String 2: no regularities, so effective complexity is zero even though the string's own algorithmic content is maximal. So very ordered and very random entities both have low effective complexity (pdf 131).
- The DNA of a viable organism presumably has many independent and interdependent regularities, so it presumably has high effective complexity (pdf 131).
- Open problem: how to find the regularities, and what if observers disagree? Gell-Mann's analogy is scientific theory formation (pdf 131).
- The best set of regularities, by Occam's Razor, is the smallest one that describes the entity and minimizes its remaining random part (pdf 132).
- Mitchell calls the idea compelling but hard to measure, and critics note its subjectivity (pdf 132).

*Intuition note:* Effective complexity counts only the "pattern part" of an object, not its random noise. A pure pattern is cheap to describe and pure noise has no pattern, so both score low.

### Logical depth (Bennett, early 1980s) (pdf 132–133)
- Logical depth measures how difficult an object is to construct. Strings of pure order or pure randomness are easy to make; a DNA sequence for a viable organism is very hard to produce without looking up known genomes (pdf 132).
- Bennett: logically deep objects "contain internal evidence of having been the result of a long computation or slow-to-simulate dynamical process" (pdf 132–133). Lloyd calls it "an appealing idea" to identify a thing's complexity with the information processed in the most plausible method of its creation (pdf 133).
- Definition: encode the object as 0s and 1s (for example A=00, C=01, G=10, T=11). The logical depth is the number of steps a properly programmed Turing machine, starting from a blank tape, needs to output it (pdf 133).
- Several such machines exist, so Bennett chose the shortest one (fewest states and rules), following Occam's Razor (pdf 133).
- Limit: there is typically no practical way to find that smallest machine or its running time, or to encode a natural object as 0s and 1s (pdf 133).

### Thermodynamic depth (Lloyd and Pagels, late 1980s) (pdf 133–134)
- Also "harder to construct = more complex." It starts from the most plausible scientifically determined sequence of events leading to the thing and measures the thermodynamic and informational resources required (pdf 134).
- Example: list all evolutionary genetic events from the first creature to modern humans. Presumably humans' depth is much greater than the amoeba's (pdf 134).
- Problems: it assumes we can list all the events; and, as some critics point out, it is unclear how to define "an event," meaning how to coarse-grain the states, or choose the relevant macrostates (pdf 134).

### Computational capacity (pdf 134–135)
- Wolfram proposed that systems are complex if their computational abilities equal those of a universal Turing machine. Bennett and others reply that the ability alone does not make a system complex. One should measure the behaviour of the system coupled with its inputs: a universal Turing machine alone is not complex (pdf 135).

### Statistical complexity (pdf 135–136)
- Crutchfield and Young: the minimum information about a system's past needed to optimally predict its statistical future behaviour. Grassberger independently defined the closely related effective measure complexity (pdf 135).
- The system is treated as a message source. One builds a model whose behaviour is statistically indistinguishable from the system's. The value is the information content of the simplest such model (pdf 135).
- Models may include random choices. So string 1 has the model "repeat A C." String 2 has the simple model "choose at random from A, C, G, or T," unlike under entropy or algorithmic content. Hence it is low for ordered and random systems and high in between (pdf 135–136).
- Typically not easy to measure if the system has no ready interpretation as a message source. Yet Crutchfield, Young and colleagues have measured it for crystal atomic structure and neuron firing patterns (pdf 136).

### Fractal dimension (pdf 136–143)
- Fractal dimension comes from dynamical systems rather than from information or computation theory (pdf 136).
- A coastline looks rugged from a plane, from a car and from the beach. This similarity across scales is called self-similarity. Mandelbrot coined "fractal." Examples: coastlines, mountain ranges, snowflakes, trees, and perhaps the distribution of galaxies (pdf 136–137).
- A fractal is in general a shape with "fine structure at every scale." The chaotic region of the logistic map ($R$ above about 3.57) is sometimes called a fractal attractor (pdf 137).
- **Koch curve** rule: replace the middle third of each segment by two sides of a triangle, each 1/3 of the original length. Start from one line and repeat forever (pdf 139–140). It has true self-similarity. Real coastlines do not; they are only "fractal-like," and their self-similarity stops at small scales (pdf 140–141).
- Dimension of regular objects: a line bisected gives 2 half-size copies per level; a square gives 4 quarter-size copies; a cube gives 8 (pdf 141). General rule: dividing side lengths by $x$, each level is made of

$$x^{\text{dimension}}$$

copies of the previous level (pdf 142). Line: $2^1=2$; square: $2^2=4$; cube: $2^3=8$ (pdf 142).
- Koch curve: segments are 3 times smaller and each level has 4 copies, so $3^{\text{dimension}}=4$. Mitchell states the result, about 1.26, and puts the calculation in her notes (pdf 142). (added step) Solving: $\text{dimension}=\log 4/\log 3\approx 1.26$.
- So the Koch curve is neither one- nor two-dimensional. The total length grows by a factor 4/3 at each application of the rule. Only perfect fractals have a precise fractal dimension; real objects get an approximate one (pdf 142).
- Informal readings: roughness, ruggedness, fragmentation, density. Ireland's coastline has higher fractal dimension than South Africa's. Mitchell likes the poetic idea that fractal dimension quantifies the cascade of detail: a smooth marble eventually shows no new detail when magnified, while fractals do at all levels (pdf 143).
- Caveat: ruggedness or cascades of detail are far from the only kind of complexity we want to measure (pdf 143).

*Intuition note:* Fractal dimension asks: when I divide the sides by a factor $x$, how many copies of the smaller picture make up each level? For the Koch curve the answer is about 1.26, between the 1 of a line and the 2 of a square.

### Degree of hierarchy (pdf 144–145)
- Simon (1962, *The Architecture of Complexity*): a complex system is composed of subsystems that have their own subsystems. He saw hierarchy and near-decomposability as the most important common attributes of complex systems (pdf 144).
- Near-decomposability means many more strong interactions within a subsystem than between subsystems. For example, a cell's metabolic network has many more interactions than occur between two cells (pdf 144).
- **Simon's claim:** evolution can design complex systems only if they are hierarchical and nearly decomposable, like building blocks. He suggests that the study of complex systems needs a theory of hierarchy (pdf 144).
- McShea's scale of nestedness: Level 1 prokaryotic cells; Level 2 aggregates of level 1 (such as eukaryotic cells); Level 3 aggregates of level 2 (multicellular organisms); Level 4 aggregates of level 3 (insect colonies, the Portuguese man o' war) (pdf 145).
- Nestedness describes structure, not function. McShea used fossil and modern data to show that the maximum hierarchy in organisms increases over evolutionary time, so complexity seems to have increased in this sense. Judging what counts as a "part" or "level" can be subjective (pdf 145).

### Closing (pdf 145)
- Each measure captures something, but all have theoretical and practical limits and have rarely been useful for real systems. The diversity suggests complexity has many interacting dimensions and probably cannot be captured by a single scale (pdf 145).

## Toy example (ours, not from the text)
Take three 20-letter strings: S1 = AAAAAAAAAAAAAAAAAAAA; S2 = ACACACACACACACACACAC; S3 = a "random" string using A, C, G, T about equally often (5 of each).
- Symbol-frequency entropy $H=-\sum p\log_2 p$. S1: $p(A)=1$, so $H=0$. S2: $p(A)=p(C)=\tfrac12$, so $H=2\times(-\tfrac12\log_2\tfrac12)=1$ bit. S3: four symbols at $\tfrac14$, so $H=4\times(\tfrac14\times 2)=2$ bits.
- So entropy ranks S3 (random) as most complex. It also scores S2 above S1 even though S2 is perfectly regular, which shows how crude symbol-frequency entropy is.
- Regularity-based view: S1 is described by "repeat A"; S2 by "repeat A C"; S3 has no pattern to describe, so effective complexity is 0. A statistical-complexity model for S3 is "choose at random from A, C, G, T," also a very short model, like those for S1 and S2.
- Dimension check of the $x^D$ rule: trisect a square, so $x=3$ and there are 9 copies. $3^D=9$ gives $D=2$, matching the book's rule (pdf 142).

## Concepts
- [[complexity measures]] — proposed quantitative measures of complexity; Mitchell says there is no universally accepted definition of complexity, and the measures all have theoretical and practical limits (pdf 125, 145)
- [[shannon-entropy]] (new) — average information or surprise of a message source; maximal for random sequences (pdf 128)
- [[algorithmic-information-content]] (new) — length of the shortest program that generates a full description of the object (pdf 130)
- [[effective-complexity]] (new) — information needed to describe an entity's regularities only (Gell-Mann) (pdf 131)
- [[occams-razor]] (new) — choose the smallest description that fits and minimizes leftover randomness (pdf 132)
- [[logical-depth]] (new) — number of steps for the shortest properly programmed Turing machine to output the object (pdf 133)
- [[thermodynamic-depth]] (new) — resources needed by the most plausible physical construction process (pdf 134)
- [[coarse-graining]] (new) — choosing which macrostates count when listing events (pdf 134)
- [[statistical-complexity]] (new) — information in the simplest model that predicts the system's statistical behaviour; models may be random (pdf 135)
- [[strange attractor / fractal]] — a shape with fine structure at every scale; the chaotic logistic-map region is sometimes called a fractal attractor (pdf 137)
- [[self-similarity]] (new) — similar shape at different scales (pdf 136)
- [[fractal-dimension]] (new) — non-integer dimension from $x^{\text{dimension}}$ copies when sides are divided by $x$ (pdf 142)
- [[hierarchy and near-decomposability]] — nested subsystems, with stronger interactions within than between subsystems (Simon) (pdf 144)

## Canonical instances
- [[human-vs-yeast-genome]] — numbers showing size is a poor measure of complexity (pdf 127–128)
- [[dna-string-1-and-2]] — ordered versus random strings, used to compare measures (pdf 130–131, 135)
- [[koch-curve]] — fractal built by a rule; dimension about 1.26 (pdf 139–142)
- [[coastline-fractal]] — Ireland versus South Africa, and self-similarity across scales (pdf 136, 143)
- [[mcshea-hierarchy-scale]] — four nesting levels of organisms (pdf 145)

## Bridges (candidates)
- [structural-analogy] Effective complexity (low at order and randomness) ↔ statistical complexity: both rank "in between" highest, but they are defined differently.
- [same-math] Algorithmic information content ↔ information theory: the length of the shortest program is the same quantity Kolmogorov, Chaitin and Solomonoff each defined.
- [structural-analogy] Simon's near-decomposability ↔ network community structure: dense links inside modules, sparse links between them.
- [metaphor] Fractal "cascade of detail" ↔ scale invariance in complex systems (canon link; not stated in this unit).

## Questions this raises
- Can any of these measures be computed for a real system such as a brain, and how would one choose the "messages" or "events"?
- How do the different measures relate to one another, for example logical depth versus effective complexity?
- Is McShea's result (rising maximum hierarchy) enough to say complexity increased in evolution?
- If complexity has several dimensions, is a single unified science of complexity even the right goal?

## Reading notes
- Printed page numbers are not visible in the text layer or the page images; all citations use pdf numbers.
- Only pdf 129, 138, 139 and 143 came with page images; all other pages (125–128, 130–137, 140–142, 144–145) came as text only. Figures 7.1–7.4 were checked where images were given (pdf 129, 138, 139, 143).
- The inline diagrams (Koch curve steps, bisection of line, square and cube) are not in the text layer, so I describe them only from the author's words.
- String 2 as printed is "ATCTGTCAAGACGGAACAT" (19 letters), but the program quoted afterwards reads A T C T G T C A A A A C G G A A C A T. The two differ at one position (text layer; pdf 130).
- Source spellings "decomposibility" and "hierachical" appear (pdf 144). The calculation of the Koch dimension is placed in the book's notes, which are not in this unit.
