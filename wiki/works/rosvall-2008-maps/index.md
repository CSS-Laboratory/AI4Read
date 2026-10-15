---
id: rosvall-2008-maps/index
work: rosvall-2008-maps
type: work-map
units: [rosvall-2008-maps/main-p1, rosvall-2008-maps/main-p2, rosvall-2008-maps/main-p3]
---

# Rosvall, M., & Bergstrom, C. T. (2008). *Maps of random walks on complex networks reveal community structure*. Proceedings of the National Academy of Sciences, 105(4), 1118–1123. DOI 10.1073/pnas.0706851105.

## In one paragraph
The paper treats finding modules in a directed, weighted network as a compression problem. A random walker stands in for information flow. The best division of the network into modules is the one that gives the shortest two-level code for the walker's path. Modules get unique names, and node names are reused inside modules, like street names across cities. The expected code length per step is the "map equation". Minimizing it over partitions finds communities that follow flow, not just link density, and it can disagree with modularity. The authors apply the method to citations among 6,128 journals. The result is an 88-module map of science, with citations flowing from applied to basic fields. It matters because it applies Shannon coding and description-length thinking directly to network science.

## The path through the work
- [[rosvall-2008-maps/main-p1]] — Finding modules in a directed, weighted network is the same problem as finding the shortest two-level code for a random walk on it, and the expected per-step length of that code (a Shannon limit) is the "map equation".
- [[rosvall-2008-maps/main-p2]] — These pages show, in pictures and lists only, a description length L(M) printed as a sum of two shifting terms for one 25-node network, with the total falling from 4.19 to 3.09 bits across eleven panels, plus maps of science and social science made "with the presented method" (as the Fig. S3 and S2 captions say).
- [[rosvall-2008-maps/main-p3]] — These pages contain no argument, only two numbered lists of journal abbreviations grouped into named fields, each field printed with a percentage.

## Big ideas across units
- **A good map is a good compression.** Code length measures how well a partition simplifies the flow without losing structure. Part 1 states the idea. Part 2 shows the total code length falling from 4.19 to 3.09 bits as modules are merged. Units: [[rosvall-2008-maps/main-p1]], [[rosvall-2008-maps/main-p2]].
- **Two-level code with reused names.** Module names are unique and node codewords repeat across modules. Part 1 defines the code. Part 2 shows the same short codewords (001, 10, 01, 11) on nodes in different modules in the final panel. Units: [[rosvall-2008-maps/main-p1]], [[rosvall-2008-maps/main-p2]].
- **A trade-off inside the description length.** Across the eleven panels in part 2, the first term of L(M) falls (1.76 to 0.13 bits) and the second rises (2.43 to 2.97 bits), while the total falls. This fits the map equation's two parts from part 1, but part 2 does not tie them together explicitly. Units: [[rosvall-2008-maps/main-p1]], [[rosvall-2008-maps/main-p2]].
- **A random walk as a proxy for flow, and a way to rank.** The walker uses only the information in the network diagram. Teleportation makes the walk ergodic and turns it into the random surfer. Part 2 ranks fields and journals by the fraction of time the surfer visits them. Units: [[rosvall-2008-maps/main-p1]], [[rosvall-2008-maps/main-p2]].
- **The map of science as the worked application.** Part 1 reports 88 modules from 6,128 journals and the applied-to-basic pattern. Part 2 draws the science map (88 fields) and a social-science map (54 fields). Part 3 lists the journals in each field. Units: [[rosvall-2008-maps/main-p1]], [[rosvall-2008-maps/main-p2]], [[rosvall-2008-maps/main-p3]].
- **Percentages in the field lists are not defined in the supplementary pages.** Part 3 gives a percentage per field and says nothing about what it measures. Part 2 says fields are ranked by the fraction of time a random surfer visits them, which is a likely reading but not stated in part 3. Units: [[rosvall-2008-maps/main-p2]], [[rosvall-2008-maps/main-p3]].

## How to read it
- **Essential:** [[rosvall-2008-maps/main-p1]]. It holds the question, the map equation, teleportation, the comparison with modularity, the search method and the science map.
- **Useful second:** [[rosvall-2008-maps/main-p2]]. It depends on part 1 for the definitions and shows the code length changing panel by panel on one small network. Part 2 has no prose of its own.
- **Skippable on a first pass:** [[rosvall-2008-maps/main-p3]]. It is a lookup table of journals by field, with no argument. Use it only to check which journals fall in a field. Do not assume what its percentages mean.
- **Prerequisites for part 1:** entropy, Huffman code, Shannon's source coding bound, Markov chain steady state, and basic directed and weighted graph terms.

## Concepts introduced
- [[entropy]] — [[rosvall-2008-maps/main-p1]]
- [[source-coding-theorem]] — [[rosvall-2008-maps/main-p1]]
- [[huffman-arithmetic-coding]] — [[rosvall-2008-maps/main-p1]]
- [[prefix-code-kraft]] — [[rosvall-2008-maps/main-p1]]
- [[entropy-rate]] — [[rosvall-2008-maps/main-p1]]
- [[map-equation]] — [[rosvall-2008-maps/main-p1]]
- [[two-level-code]] — [[rosvall-2008-maps/main-p1]]
- [[random-surfer-teleportation]] — [[rosvall-2008-maps/main-p1]]
- [[modularity]] — [[rosvall-2008-maps/main-p1]]
- [[ergodic-visit-frequency]] — [[rosvall-2008-maps/main-p1]]
- [[community-detection]] — [[rosvall-2008-maps/main-p1]]
- [[two-level-codebook]] — [[rosvall-2008-maps/main-p2]]
- [[description-length-of-a-partition]] — [[rosvall-2008-maps/main-p2]]
- [[journal-cluster-field]] — [[rosvall-2008-maps/main-p3]]
- [[percentage-per-field]] — [[rosvall-2008-maps/main-p3]]
