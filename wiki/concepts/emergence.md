---
id: emergence
type: concept
fields: [complex-systems, control-theory]
fields_strong: [complex-systems, control-theory]
n_sources: 13
n_works: 5
tiers: [core]
grounding: digests
sources: [anderson-1972-moreisdifferent/main, ashby-1956-cybernetics/ch06-black, castellano-2009-socialdynamics/main-p1, castellano-2009-socialdynamics/main-p2, mitchell-2009-guidedtour/ch01-complexity, mitchell-2009-guidedtour/ch03-information, mitchell-2009-guidedtour/ch05-evolution, mitchell-2009-guidedtour/ch10-cellular, mitchell-2009-guidedtour/ch12-information, mitchell-2009-guidedtour/ch13-make, mitchell-2009-guidedtour/ch18-evolution, mitchell-2009-guidedtour/ch19-past, schelling-1971-segregation/main-p1]
canon_spine: [complex-systems]
generated_by: build_kg.py
---

# emergence

## Canon spine entry

- **emergence** (complex-systems): macro-level patterns or laws that arise from micro-level interactions and need their own description (UG)

## Definitions in the sources

### complex-systems

- [[anderson-1972-moreisdifferent/main]] (p. 393): at each level of complexity, entirely new properties appear and need their own research (p. 393) (canon link; not stated in this unit) [weak: not really used in this unit]
- [[castellano-2009-socialdynamics/main-p1]] (p. 7): micro-to-macro emergence is the stated aim of ABM
- [[castellano-2009-socialdynamics/main-p2]] (pp. 30, 36, 38): lanes, collective motion, shared vocabulary arising without being imposed
- [[mitchell-2009-guidedtour/ch01-complexity]] (pdf 31): here: the hard-to-predict macroscopic behavior that arises from simple rules
- [[mitchell-2009-guidedtour/ch03-information]] (pdf 72): large-scale properties like heat arise from microscopic motions
- [[mitchell-2009-guidedtour/ch05-evolution]] (pdf 112, 116): only loosely: the Synthesis's third pillar says macro-level phenomena follow from micro-level processes, and the challengers deny this in part [weak: not really used in this unit]
- [[mitchell-2009-guidedtour/ch10-cellular]] (pdf 194): here, complex patterns arising from very simple rules
- [[mitchell-2009-guidedtour/ch12-information]] (p. 31): larger-scale information-processing behavior arising from networks of simple elements, as in ants and neurons
- [[mitchell-2009-guidedtour/ch13-make]] (pp. 55, 57): the scan and the program's "understanding" emerge from many simple components
- [[mitchell-2009-guidedtour/ch18-evolution]] (p. 162): in Kauffman's view, complex, "self-organized" behaviour that emerges once a network has many nodes controlling other nodes
- [[mitchell-2009-guidedtour/ch19-past]] (p. 170): glossed by Gordon as the whole being greater than the sum of its parts; the general principle that all complex systems exhibit emergent properties is called not very useful
- [[schelling-1971-segregation/main-p1]] (pp. 150–151, 158): clustering far beyond individual demands arises from interacting moves

### control-theory

- [[ashby-1956-cybernetics/ch06-black]] (pp. 110–111): a property of a whole not predicted from incomplete knowledge of its parts; none arises if parts and couplings are fully known [new]

## Instances that use it

- [[gpt3-instructgpt-arithmetic]] — 2-digit multiplication and 4-digit addition: emergence under Accuracy, smooth under Token Edit Distance — from [[schaeffer-2023-mirage/main]]
- [[lamda-brier-score]] — emergence under Multiple Choice Grade disappears under Brier Score — from [[schaeffer-2023-mirage/main]]
- [[induced-emergence-vision]] — autoencoder reconstruction, Omniglot Transformers, MNIST LeNet — from [[schaeffer-2023-mirage/main]]
- [[wikitext103-perplexity]] — alternative x-axis to scale for MMLU emergence — from [[wei-2022-emergent/main]]

## Candidate bridges

- [structural-analogy] Statistical mechanics (macro from micro statistics) ↔ complex systems: emergence of macro patterns from many micro interactions (pdf 72). — from [[mitchell-2009-guidedtour/ch03-information]] (complex-systems → complex-systems)
- [structural-analogy] Hard-to-read genome vs. clear behavior ↔ complex systems: macro behavior is not obvious from micro rules (emergence) — the author describes G's behavior, not its genes, in plain terms. — from [[mitchell-2009-guidedtour/ch09-genetic]] (complex-systems → complex-systems)
- [metaphor] Emergence as a mirage ↔ Anderson's "More Is Different" (p. 1): the paper questions the claim of emergence for LLMs. — from [[schaeffer-2023-mirage/main]] (llm → other:andersons-more-is-different)
- [metaphor] Laser onset of coherence from random pumping ↔ emergence / self-organization — the text calls it "self-organizing" (p. 54). — from [[strogatz-2024-nonlinear/ch03-bifurcations-p1]] (complex-systems → unspecified)
- [metaphor] Emergence in the paper's sense ↔ physics: Anderson's "more is different" and phase transitions — the paper takes the framing, but its definition is only about scaling-curve shape (p. 2). — from [[wei-2022-emergent/main]] (llm → other:physics)
