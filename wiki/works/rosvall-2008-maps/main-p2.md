---
id: rosvall-2008-maps/main-p2
work: rosvall-2008-maps
unit: "paper (part 2/3): supplementary figures — merging sequence of code lengths, maps of science and social science, journal lists"
pages: pdf 22–41
fields: [information-theory]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Rosvall & Bergstrom (2008), part 2/3: code-length panels, maps of science, journal lists

## L0 — One line
These pages show, in pictures and lists only, a description length L(M) printed as a sum of two shifting terms for one 25-node network, with the total falling from 4.19 to 3.09 bits across eleven panels, plus maps of science and social science made "with the presented method" (as the Fig. S3 and S2 captions say).

## L1 — The gist (≤ 120 words)
This part holds no running prose. It has three kinds of material. The first is eleven panels of one 25-node network. Each panel shows node codewords, two codebook bar charts and a total L(M). The first term falls from 1.76 to 0.13 bits, the second rises from 2.43 to 2.97 bits, and the total falls from 4.19 to 3.09 bits. The second is two network maps, of science and of social science. The third is ranked journal lists for the largest science fields. The definitions and the argument are not on these pages. They belong to the main text and caption material outside this part.

**Prerequisites:** codewords and codebooks (variable-length binary codes); entropy as bits per symbol; the idea of a random walk on a network; a module is a group of nodes in a partition; a random surfer is a random walker on the network.

## L2 — Key ideas (5–10 bullets)
- Each panel of the 25-node network labels every node with a binary codeword and prints L(M) as a sum of two terms (pdf 22–32).
- Across the eleven panels the first term falls strictly, from 1.76 to 0.13 bits (pdf 22, 32).
- The second term never decreases, rising from 2.43 to 2.97 bits (pdf 22, 32).
- The total falls from 4.19 to 3.09 bits, and the last panel's total is printed in red (pdf 22, 32).
- In the final panel the same short codewords (e.g. 001, 10, 01, 11) appear on nodes in different modules (pdf 32).
- Fig. S3 is a map of science with 88 fields (51 drawn). Fields and journals are ranked by the fraction of time a random surfer visits them (pdf 33).
- Fig. S2 is a map of social science with 54 fields (36 drawn), ranked the same way (pdf 34).
- Journal lists give each field's journals in ranked order, with shares for the top fields: 20%, 14%, 10%, 5.8%, 4.3% (pdf 35–41).

## L3 — Walkthrough

### A. The merging sequence of code lengths (pdf 22–32)

**What each panel contains (from the page images, pdf 26–32).** A weighted network of 25 nodes (my count). Node colour appears to mark module membership (my reading of the images; no caption on these pages says so). Each node carries a binary codeword written inside the circle. Edge thickness varies. An unlabelled vertical scale (0.5 to 2.0) stands beside two stacked bar charts, and the pages do not say what unit it uses. The left chart is a short stack of codewords. Thin lines run from it to the right chart, a taller stack in colour blocks, one block per module. Under both charts is printed
$$L(\mathsf M) = a + b = \text{total bits},$$
with $a$ under the left chart and $b$ under the right. Pages 22–25 are available only as extracted text, so I take their numbers from the text layer.

**The numbers.** Values are as printed in the panels. The step-change row is my own subtraction (added step).

| pdf | $a$ (left chart) | $b$ (right chart) | $L(\mathsf M)$ | drop from previous panel (added step) |
|---|---|---|---|---|
| 22 | 1.76 | 2.43 | 4.19 | – |
| 23 | 1.59 | 2.46 | 4.05 | 0.14 |
| 24 | 1.30 | 2.57 | 3.88 | 0.17 |
| 25 | 1.16 | 2.58 | 3.74 | 0.14 |
| 26 | 0.97 | 2.66 | 3.63 | 0.11 |
| 27 | 0.75 | 2.73 | 3.48 | 0.15 |
| 28 | 0.58 | 2.79 | 3.37 | 0.11 |
| 29 | 0.51 | 2.79 | 3.30 | 0.07 |
| 30 | 0.36 | 2.88 | 3.24 | 0.06 |
| 31 | 0.23 | 2.95 | 3.19 | 0.05 |
| 32 | 0.13 | 2.97 | 3.09 | 0.10 |

Checks: $a$ falls at every step; $b$ rises at every step except 28→29, where it stays at 2.79; the total falls at every step (pdf 22–32). Three printed totals differ by 0.01 from the sum of their parts (1.30 + 2.57 = 3.87 vs 3.88 printed; 0.23 + 2.95 = 3.18 vs 3.19 printed; 0.13 + 2.97 = 3.10 vs 3.09 printed). This is presumably rounding of the displayed terms; the pages do not say. The total drops 1.10 bits from the first panel to the last. The per-step drops are 0.11–0.17 for pdf 23–28, 0.05–0.07 for pdf 29–31, then 0.10 at the last step.

**How the partition changes (my count of colours in the images, pdf 26–32).** From pdf 26 onward, each panel appears to have one fewer module than the one before:
- pdf 26 (3.63): 10 modules
- pdf 27 (3.48): 9
- pdf 28 (3.37): 8
- pdf 29 (3.30): 7
- pdf 30 (3.24): 6
- pdf 31 (3.19): 5
- pdf 32 (3.09): 4

Some modules are single nodes, shown with codeword "0" in separate colours at pdf 26. These single-node modules are absorbed one by one into neighbouring groups. Node placement and edges do not change. I could not check pdf 22–25 as images, so I cannot say how many modules they have.

**The final panel (pdf 32).**
- Four colour groups: red with 6 nodes, orange with 7, green with 8, blue with 4 (my count).
- The total 3.09 is printed in red, with no caption on these pages to explain the colour.
- The left chart has four codewords (0, 10, 110, 111). Each colour block in the right chart has one more codeword than the module has nodes (e.g. the orange block lists 8 codewords for 7 nodes; my count).
- The same short codewords label nodes in different modules. For instance 001 appears on a red, a green and a blue node; 10 on a green and a blue node; 01 and 11 on a red and a blue node (pdf 32).

**Intuition note.** The figure splits the total into two printed terms: the left-chart term falls across the panels and the right-chart term rises. By inference only (the pages do not label the charts), the left chart may price moves between modules and the right chart naming nodes inside modules. The reuse of short codewords across modules is what the colours make visible. The pages give no further explanation of these labels; the figure itself is all there is here.

### B. Fig. S3: map of science (pdf 33)
- Caption: a map of science with fields according to a partitioning "with the presented method" (pdf 33).
- There are 88 field names in the caption and 51 in the map. Fields and journals are ranked by the fraction of time a random surfer visits them (pdf 33).
- The caption numbers fields from 1 Molecular & Cell Biology, 2 Medicine, 3 Physics, 4 Neuroscience, 5 Ecology & Evolution, 6 Economics, 7 Geosciences, 8 Psychology, 9 Chemistry, 10 Psychiatry, down to 88 Futurist (pdf 33).
- In the image, higher-ranked fields are drawn as larger nodes. The three largest nodes are Molecular & Cell Biology, Medicine and Physics.
- Arrows join fields. The thickest, darkest arrows run among Medicine, Molecular & Cell Biology and Neuroscience, and between Physics and Chemistry. The caption does not say what arrow width encodes.

**Intuition note.** The map has a few big, densely linked fields and many small ones. Its picture follows the ranking stated in the caption, but this part gives no figure for what the arrows measure.

### C. Fig. S2: map of social science (pdf 34)
- Same construction: 54 field names in the caption, 36 in the map, ranked by random-surfer visit fraction (pdf 34).
- The first ranks are 1 Economics, 2 Psychology, 3 Psychiatry, 4 Healthcare, 5 Political Science, 6 Sociology (Behavioral) (pdf 34).
- The caption ends with 54 Hypnosis (pdf 34).

### D. Journal lists for the largest fields (pdf 35–41)
The heading "Fields of science" introduces numbered lists. Each field gives its share in brackets and its journals in rank order (pdf 35).

| Field | Share | Journals listed | First five | Last |
|---|---|---|---|---|
| 1 Molecular & Cell Biology | 20% | 512 | J Biol Chem, Cell, J Immunol, Embo J, Blood | J Clin Biochem Nutr (pdf 35–36) |
| 2 Medicine | 14% | 766 | New Engl J Med, Lancet, Circulation, Jama-J Am Med Assoc, Brit Med J | Man India (pdf 36–39) |
| 3 Physics | 10% | 502 | Phys Rev Lett, Phys Rev B, Appl Phys Lett, J Appl Phys, J Chem Phys | Silic Ind (pdf 39–40) |
| 4 Neuroscience | 5.8% | 224 | J Neurosci, Neuron, Neurology, Nat Neurosci, J Neurophysiol | Cesk Slov Neurol N (pdf 40–41) |
| 5 Ecology & Evolution | 4.3% | continues past this unit; the list reaches 213 | Ecology, P Roy Soc B-Biol Sci, Mar Ecol-Prog Ser, Oecologia, Trends Ecol Evol | not in this part (pdf 41) |

- The bracketed shares are presumably each field's share of random-surfer visits, since the caption on pdf 33 ranks fields that way. These pages do not define them.
- My observation: the lists mix kinds of journals. For example Physics includes Langmuir and Macromolecules, and Medicine includes Soc Sci Med (#38) (pdf 36–39).

## Toy example (ours, not from the text)
Aim: show how a two-module code can be cheaper than a one-module code, using the usual two-term cost (module-switch bits plus within-module bits). The exact formula is in the paper's main text, not in these pages.

Setup: a walker on 4 nodes A, B, C, D, each visited 1/4 of the time. Modules are {A,B} and {C,D}. Assume 1 step in 10 crosses modules, so each module is left with probability 0.05 per step.
- **One module.** Four equally likely nodes need $\log_2 4 = 2$ bits per step.
- **Two modules, switch term.** The two modules are equally used, so naming the new module costs 1 bit, paid on 0.1 of the steps: $0.1 \times 1 = 0.1$ bits.
- **Two modules, within-module term.** Each module's codebook has three events: A, B, and exit. Their weights are 0.25, 0.25 and 0.05, total 0.55. Normalised: 5/11, 5/11, 1/11.
  - $\log_2(11/5) = \log_2 2.2 \approx 1.1375$. So $2 \times (5/11)\times 1.1375 \approx 1.0341$.
  - $\log_2 11 \approx 3.4594$. So $(1/11)\times 3.4594 \approx 0.3145$.
  - Entropy $\approx 1.0341 + 0.3145 = 1.3486$ bits.
  - Each module's codebook is used 0.55 of the time, so the term is $2 \times 0.55 \times 1.3486 \approx 1.4835$.
- **Total.** $0.1 + 1.4835 \approx 1.58$ bits per step, below the 2 bits for one module.

## Concepts
- [[two-level-codebook]] (new) — presumably an index codebook for module switches plus one codebook per module for nodes (an inference from the figure; not stated on these pages); codewords are seen to repeat across modules (pdf 32).
- [[description-length-of-a-partition]] (new) — here written $L(\mathsf M)$ and split into two printed terms $a + b$ (pdf 22–32).
- [[prefix-code-kraft]] — node codewords appear as binary strings of varying length (e.g. 0, 10, 0001). The pages do not state that the code is prefix-free.
- [[entropy]] — behind the bar charts only by inference; not defined on these pages.

## Canonical instances
- [[merging-sequence-25-node-network]] (new) — eleven panels of one network, total falling 4.19 → 3.09 bits over the panels; by my image count the module number drops by one per panel in pdf 26–32 (pdf 22–32).
- [[map-of-science-S3]] (new) — 88-field partition, ranked by random-surfer visits (pdf 33).
- [[map-of-social-science-S2]] (new) — 54-field partition (pdf 34).
- [[journal-field-lists]] (new) — ranked journals for the top five fields (pdf 35–41).

## Bridges (candidates)
- [structural-analogy] Two-term code length (module switches + within-module names) ↔ information-theory: the two parts of a two-stage code — choose a codebook, then a word in it.
- [structural-analogy] Agglomerative module merging ↔ information-theory: model selection by description length (MDL), where the total is a trade-off between two parts.
- [metaphor] Random surfer visiting fractions ↔ information-theory: how often a source emits each symbol, which sets ideal code lengths.

## Questions this raises
- Does the total keep falling if modules are merged beyond four, or does it rise again? (The panels stop at 4 modules, pdf 32.)
- What exactly do the arrow widths and node sizes in Fig. S3 encode?
- Why do the two terms move in opposite directions as modules merge?
- How are the field shares (20%, 14%, …) defined?

## Reading notes
- This part is pdf 22–41 of the paper. Per the source notes it ends at an even boundary. It begins at the panel L(M) = 4.19 (whether earlier panels exist is not visible here), with no running text, and ends mid-list, in the Ecology & Evolution journal list (journal 213).
- The page labels carry printed numbers (13, 13, 13, 13, 10, 11, 12, …) that are inconsistent and not usable as pagination. All references here use (pdf N).
- Page images were supplied for pdf 26–33 and 35–41. For pdf 22–25 and 34 I used the text layer only. The text layer of pdf 22–32 is garbled, with codewords interleaved. The totals and terms were checked against the images for pdf 26–32.
- Counts of nodes, modules and journals are mine from the images and lists, and are marked as such where used.
- Two printed totals differ by 0.01 from the sum of their terms (3.88 vs 1.30 + 2.57; 3.19 vs 0.23 + 2.95); a third differs by −0.01 (3.09 vs 0.13 + 2.97). The cause is presumably rounding, but the source does not say.
- No caption for the panel series appears in this part, so the meaning of the left and right charts, the vertical scale, and the red colour of the last total is not stated here.
