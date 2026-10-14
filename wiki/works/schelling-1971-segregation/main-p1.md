---
id: schelling-1971-segregation/main-p1
work: schelling-1971-segregation
unit: paper (part 1/2) — pp. 143–163, from the abstract to the start of "Population Densities"
pages: 143–163
fields: [complex-systems]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 16
pipeline_version: 0.1
---
# Dynamic Models of Segregation (part 1: scope, constraints, and the spatial proximity model)

## L0 — One line
Individuals who only mildly prefer not to be a local minority, and who move when dissatisfied, can produce strong collective segregation that nobody demanded (pp. 143, 150–151, 158).

## L1 — The gist (≤ 120 words)
Schelling asks how segregation can arise from unorganized individual choices. He sets aside organized segregation and the largely economic sorting of rich from poor. He first notes logical constraints on mixing. He then runs "tabletop" experiments in which two kinds of counters, on a line and on a checkerboard, move whenever too few neighbors are like them. Mild demands, such as half of one's neighbors alike, give clusters and neighborhoods far more homogeneous than required. Results depend on intensity of demand, group sizes and vacancies. So inferences about individual motives can usually not be drawn from aggregate patterns, and segregation can emerge without a segregationist plan.

**Prerequisites:** proportions and ratios; the idea of an equilibrium (a state in which nobody wants to move); reading simple grids and strings of symbols.

## L2 — Key ideas
- The paper is about segregation that can result from the interplay of discriminatory individual choices. Organized action and the largely economic sorting of rich from poor are deliberately left out, though Schelling says the lines between the three are blurred (pp. 143–145).
- Aggregate results need not match individual intentions. One of his analogies is depressions and inflations, which do not reflect any universal desire for lower incomes or higher prices (pp. 145–146).
- Pure arithmetic limits mixing. For example, if each group insists on being a local majority, only complete segregation works (p. 147).
- Linear model: counters want at least half of their eight nearest neighbors alike. Moving until everyone is content gives about six clusters averaging 12, with 81.5% like neighbors (pp. 149–151).
- Smaller minorities form absolutely larger clusters. Travel limits can substitute for coordinated movement (pp. 152–154).
- Checkerboard model, with equal numbers and equal demands: a demand of about one-third alike gives slight segregation; a demand of one-half gives striking segregation. The outcome rises rapidly over roughly 35–50% (pp. 154–159).
- When the two colors are about equal in number, separation is reciprocal, so a more demanding color ends up higher in like-neighbor ratio but not much higher. It ends up in denser territory (pp. 159–163).

## L3 — Walkthrough

### Abstract and opening (pp. 143–145)
Schelling lists several sources of segregation. These are organizations, specialized communication systems, correlation with a non-random variable, and the interplay of individual choices (p. 143). This paper is an abstract study of the last. It uses a simulation model of individuals who define neighborhoods around themselves and an analytic model of compartmented space. The abstract also announces a section on "neighborhood tipping" (that section lies outside the pages digested here) (p. 143).

His definition: "discriminatory" means reflecting an awareness, conscious or not, of the group distinction, and that awareness influences choices (p. 144). The distinction must be twofold, exhaustive and recognizable. Any such pair fits: whites/blacks, boys/girls, students/faculty (p. 144). The ultimate concern is color in the United States (p. 144).

Two processes are omitted: organized action, and the largely economic sorting of poor from rich and so on (p. 144). Schelling does not say these are less important. On civil-rights and equity grounds they may matter more (pp. 144–145). The three kinds blur into each other (p. 145):
- Habit and fear of sanctions can substitute for organization.
- Choosing a neighborhood is choosing neighbors.
- If avoidance is reciprocated, positive feedback amplifies it.
- Economic segregation might explain an initial degree of segregation, and a "superstructure of pure discrimination" could complete the job. Removing the economic cause might then not undo the result (p. 145).

### Individual incentives and collective results (pp. 145–146)
Economists know systems whose aggregate results the individual neither intends nor is aware of. Examples are money creation by banks and savings decisions causing depressions (p. 145). Further examples are species sorting in evolution, the survival of second languages, and the genetic effects of marriage (pp. 145–146). Small incentives can give polarized results, as in Gresham's Law (p. 146).

**Tempting view (Schelling raises it, then doubts it):** an "unseen hand" separates people in a way matching a consensus or popular will. Schelling counters that depressions and inflations do not reflect any universal desire for lower incomes or higher prices. The "hearts and minds" of participants may or may not correspond to the massive results they generate (p. 146). People acting alone often can only change their own position within an overall result, not the result (p. 146).

A special reason to doubt social efficiency in segregation is that the range of choice is meager. Schelling says the demographic map of almost any American metropolitan area suggests that it is easy to find nearly all-white or all-black areas. It is hard to find areas where neither group exceeds, say, three-quarters. Comparing decennial maps, it is nearly impossible to find such an area that stays mixed long enough for a man to pay off his house or put his children through school. The distribution is U-shaped, "virtually a choice of two extremes" (p. 146).

> **Intuition note:** A collective outcome need not match what individuals chose or want. The motives of participants may or may not correspond closely to the massive results they generate (p. 146).

### Some quantitative constraints (p. 147)
These are logical constraints, like balance-sheet identities. They "contain no news" unless one had not thought of them (p. 147).
- Within given boundaries, both groups cannot be local majorities. If each insists on being a majority, only complete segregation satisfies both (p. 147).
- If whites want at least three-fourths and blacks at least one-third, this cannot work. If whites want at least two-thirds and blacks at least one-fifth, a small range of mixtures works, and not everyone fits if the overall ratio is outside it (p. 147).
- Small numbers: a classroom's teacher is one color, and a team of two gives each member company of one color only (p. 147).
- In a row of neighbors, if you have a neighbor on each side, the minimum nonzero share of the opposite color is 50% (p. 147).
- At a dinner with alternating sexes, each person is outnumbered two to one locally. Extending the horizon one person each way gives a three-fifths majority (p. 147).
- Hospital: with one-sixth of beds black and four beds per room, at least 40% of whites are in all-white rooms (p. 147).
- A college wanting 10% black students suddenly must admit 40% black freshmen. It then must pass three classes before admitting more (p. 147).

### Separating mechanisms (pp. 147–148)
Ratios say what is possible, not what behavior leads to. Schelling lists incentives that can separate groups:
- Each prefers its own kind.
- Each avoids the other.
- Only one group cares.
- One group can afford where the other cannot follow (p. 148).

Case: both groups dislike being a minority but not integration (p. 148).
- Only a 50:50 mix is self-sustaining. Any other mix has a minority, and if it leaves, complete segregation follows.
- If each tolerates being a minority down to 25%, initial mixtures from 25% to 75% survive. More extreme mixtures lose their minority (p. 148).
- If there are lower limits on tolerable minority status and the start is complete segregation, nobody moves into the other group's area. Complete segregation is a stable equilibrium, because "somebody has to move first and nobody will" (p. 148).

Roadmap: a spatial model with self-defined neighborhoods, then a compartmented model with varied tolerances, then neighborhoods with limited capacity (p. 148). Only the first is in this part.

### Spatial proximity model (pp. 149–163)
The results are "experimental", crude and reproducible with simple materials (p. 149). Assumptions: a population exhaustively divided into two permanently recognizable groups. Everyone observes the color mix around them and may move if dissatisfied (p. 149).

#### Linear distribution (pp. 149–152)
**Setup.** Odd and even digits from a random-number column give 35 stars and 35 zeros (Fig. 1) (p. 149). Each person's neighborhood is the four nearest neighbors on each side. Each wants at least four of his eight neighbors alike, i.e. five of nine counting himself (p. 149). Near an end, the neighborhood is the four toward the center plus the one, two or three outboard neighbors, and half must be alike (p. 149).

**Initial state.** 12 stars and 14 zeros are dissatisfied (the text gives the expected number as "just under 13", without saying whether this is per color) (pp. 149–150).

**Rules of movement (p. 150).**
- A discontent moves to the nearest point where half his neighbors will be like him on arrival.
- "Nearest" means passing the fewest neighbors. He inserts himself between two others.
- Order is left to right.
- A discontent who is content when his turn comes does not move.
- Those newly discontent move after the 26 originals.
- Neighborhoods are recomputed at each decision. Nobody anticipates others' moves (p. 150).

**Run.** The leftmost mover (second star) passes six neighbors. The next movers join him, and a zero moves left passing four stars (p. 150). The first round leaves eight newly discontent (top of Fig. 2). A second round leaves everyone content. In general one round may suffice or more than two may be needed (p. 150).

**Result.** Six clusters of 8, 15, 10, 15, 16 and 6, averaging 12 (p. 150). Of 540 neighbor slots, 440 are same-colored (81.5%) (p. 150). Counting himself, each person's own color predominates by an average ratio somewhat above 5 to 1, although each only sought at least 5 to 4 (p. 150).

**Comments (pp. 151–152).**
- Equilibria must give everyone at least five-ninths his own color if they exist. The result is nonetheless "more striking" (p. 151).
- Regular alternation (+O+O…) and alternating pairs (++OO…) satisfy everyone with exactly half like. Alternating groups of three or four fail. Groups of five or more in alternation satisfy everyone. The model gave groups of about twelve (p. 151).
- If people also prefer some opposite neighbors (while avoiding minority status), only 40 of 70 manage it. Thirty have no opposite neighbors (p. 151). Such people shuffle to just inside their group's boundary without changing the grouping (p. 151).
- A second random sequence (Fig. 3): 72 members, 30 discontents, one round, six groups of 7, 14, 14, 9, 17, 11 (p. 151).
- Tabletop trials give about five groups averaging 14 up to seven or eight averaging 9–10. The modal outcome is six groups of size 12 (p. 151).
- Similar experimentation suggests that order of moves matters little unless people anticipate outcomes to maximize or minimize group sizes (pp. 151–152).

> **Intuition note:** Each mover wants only a bare majority nearby. But each move adds a like neighbor to others and removes one from others, so the demands compound. The final clusters are much more homogeneous than any individual asked for (pp. 150–151).

#### Variations of the linear model (pp. 152–153)
Five elements can be varied: neighborhood size, demanded share, population ratio, movement rules, initial configuration (p. 152).

**Smaller neighborhood.** With three people each side, the same alternating clusters appear (p. 152).
- First sequence: 37 initial discontents, 5 new after round one, ten groups averaging 7.
- Second: 29 discontents, 3 new, seven clusters averaging 10.
- Further trials suggest a mean of 7–8, about twice the minimum satisfying cluster (alternating clusters of 4). The average person's neighborhood is 75–80% own color (p. 152).
- Footnote: for this six-neighbor neighborhood, short of clusters of four or more, the only pattern giving half-alike neighbors is …OO+O++O+OO+O++…. It unravels at the ends unless it runs indefinitely or closes into a curve (p. 152).

**Unequal totals.** Seventeen of the 35 zeros of Fig. 1 were removed by die rolls (Fig. 4). All zeros and three stars are then discontent. In one round all zeros congregate (Fig. 5: clusters of 15, 18 and 20) (p. 152). A second sequence, about two stars per zero, started with 18 of 20 zeros and 2 stars discontent. After round one 4 were still discontent, after round two 2. After round three it reached the top line of Fig. 6. Other random deletions gave the other two lines (pp. 152–153).

**Result for minorities (p. 153).**
- As the numerical inequality grows, one expects the majority's segregation to become more extreme. With stars 4:1, even a regular distribution gives stars on average only one-fifth opposite neighbors. The minimum satisfying minority cluster is 5, so the majority needs clustering of at least 4 × 5 = 20 (p. 153).
- Less obviously, the minority itself tends to become more segregated as its relative size shrinks. Minority clusters become absolutely larger, and their number falls more than proportionately (p. 153).
- Reason: the chance of four or more minority members among eight consecutive people falls more than proportionately. So potentially stable clusters ("growth nodes") become scarcer relative to the minority. Everyone moves to places where at least four of eight coincided by chance (p. 153).
- With a demand of only three alike, a 10% minority forms clusters about twice the size of Figs. 2–3. With a demand of half, its mean cluster is upwards of 100, if the population is large enough to sustain any growth nodes (p. 153).

#### Restricted movement (pp. 153–154)
Suppose the minority is 20% or 10% and travel distance is limited. Many may be unable to reach a place meeting their demand. Modified rule: if no half-alike neighborhood lies within the radius, move to the nearest place where three of eight are alike (pp. 153–154). Result: everyone ends with half or more his own color, without traveling as far as if all had been free to travel. The limit channels people into the smaller, more frequent growth nodes, which then grow past their needs (p. 154). Schelling concludes that travel limits can substitute for concerted movement and for anticipatory movement (p. 154). He adds that the model is too abstract and artificial to be a "motion picture" of real choices, but suggestive of the dynamics (p. 154).

#### Area distribution (pp. 154–155)
**Setup.** In two dimensions the rule for who shifts to make room is awkward. So he divides the area into a fixed grid of squares, leaving some vacant. A person moves only into a vacant square (p. 154).
- Neighborhood: own square plus the 8 surrounding squares (3 × 3). A 5 × 5 block (24 surrounding squares) is also considered (p. 154).
- Edge squares have 5 neighbors, corners 3 (p. 154).
- 25–30% vacancies allow fair freedom of movement without making the board too empty (p. 154).

**Rules (pp. 154–155).**
- Discontents move to the nearest vacant spot meeting their demands. Distance is the count of squares traversed horizontally and vertically.
- Demands can be absolute (number of like neighbors) or relative (ratio like:opposite). Because neighbor count ranges from 0 to 8, there are eight denominators and eight numerators to specify (p. 155).
- The initial placement of colors and blanks is random.
- Order of moves is by board position (generally left to right), or one color completes its moves before the other.
- All runs were done by hand and eye, so no exact order rule was strictly followed (p. 155).

**Figure 7 start (pp. 155–156).** The board has 13 rows and 16 columns, 208 squares, with 138 counters (p. 156). Schelling shows a random picture on purpose. Random patterns still contain apparent "homogeneous neighborhoods": "Randomness is not regularity" (p. 156).

**Measures (p. 156).** One measure is the average share of neighbors of like color. In Fig. 7, zeros average 53% like neighbors and stars 46%. The difference arises because they can have different numbers of blank neighboring spaces (p. 156). Many regular patterns also give each person half like neighbors, for example a checkerboard or checkerboard of 2 × 2 blocks. So patterning is related to, but distinct from, any measure of homogeneity (p. 156). Footnote: departure from randomness will prove characteristic of integration too, if integration results from choice and not chance (p. 156).

**"Solitaire."**
- Fig. 7 has 25 discontent stars and 18 discontent zeros, under a demand of half like (p. 156).
- Moved in turn until equilibrium, the particular outcome depends much on move order, the character of the outcome little (p. 156).
- Moving from the upper left gives Fig. 8, very striking segregation. Moving from the center outward gives Fig. 9, also striking but more fragmented. Fig. 10 is Fig. 9 with boundaries drawn, which Schelling admits may be "cheating a little" (p. 156).

**Figure 9 statistics (pp. 156–158).**
- Zeros average neighbors five-sixths zeros, stars four-fifths stars (p. 158).
- The average zero has five neighbors, of whom not quite one is a star. The average star has about 4.5 neighbors, one of them a zero (p. 158).
- Share with no opposite neighbors: 13 (about 10%) in random Fig. 7, 54 (about 40%) in Fig. 9 (p. 158).
- For Fig. 8: counting himself, the average person lives in a neighborhood 90% own color (89 zeros, 91 stars). Two-thirds of both colors have no opposite neighbors (p. 158).

**Footnote reference patterns (p. 158).** The neighbor count of Fig. 9 matches blocks of 7 × 7 squares of 49. Blocks of 2 × 2 give the same one-to-one count as random. The 39% with no opposite neighbors matches 5 × 6 blocks (12 of 30, 40%) (p. 158).

Schelling stresses that his samples are small and the numbers apply only to a checkerboard. He offers hypotheses, and thinks only comparisons, such as the effect of a smaller minority, may extend to the real world (p. 158). Schelling says all following runs involve the same 13 rows and 16 columns, with blanks usually about 30% of the total and a random distribution of the two colors (p. 158).

> **Intuition note:** The first count to trust is not the picture but the neighbor count. A board that starts at roughly half like neighbors, matching the minimum demanded, ends at about five-sixths or four-fifths (p. 158).

#### Intensity of demand for like neighbors (pp. 158–159)
For equal numbers, 8-square neighborhoods and equal demands, segregation is slight when the demand is about one-third like neighbors and striking at one-half. At one-half or more the like-to-opposite ratio is upwards of four to one. At about one-third it is less than 1.5 (pp. 158–159). Figure 11 uses demands of about one-third. Footnote: one like neighbor out of four or fewer, two out of five or more. Average neighbors fall from 5.5 initially to about 4.5, so effective preference is near one-third (p. 159).

Raising the demand does three things (p. 159):
1. More people start discontent.
2. Each mover gains more like neighbors, and also becomes a like neighbor to more people.
3. More movement is induced among those originally content.

These compound, so segregation is a rapidly rising function of demand between roughly 35% and 50% (p. 159). With fixed boundaries, demands summing to more than one allow no coexistence. Here boundaries are not fixed, but flexibility is limited. So demands above one in total should produce extreme segregation, "as apparently they do" (p. 159).

#### Unequal demands (pp. 159–160)
With about equal numbers but unequal demands, the more demanding color ends up with a higher like-neighbor ratio, but not much higher (p. 159). In Fig. 12, zeros (77) are less demanding. They want one of four or fewer neighbors alike, two of five or more. Stars (72) want two like neighbors if they have 3–5 neighbors, three if 6–7, four of eight (pp. 159–160). Zeros end at a ratio of 2:1 like to opposite. Stars end at "2:5" as printed, which presumably means 2.5:1 (p. 160; compare p. 163).

Why it is not more: separation is reciprocal. For every white with a black neighbor there is exactly one black with a white neighbor, if neighbors are defined consistently (p. 160). So the two colors' ratios can differ only if their neighborhoods differ in population density. That difference is limited, among other things, by the number of blanks (p. 160). With no blanks and equal numbers, the like-neighbor ratios are forced equal. With unequal numbers they differ strictly by numerical ratio. The majority's opposite-color percentage equals the minority's multiplied by (minority size / majority size) (p. 160). In Fig. 12 stars are more compacted and zeros more spaced out (p. 160).

> **Intuition note:** Every mixed neighbor pair counts for both sides. In the example shown, the stricter group ends only somewhat more separated, because the two colors' ratios can differ only through differences in neighborhood density (p. 160).

#### Unequal numbers, equal demands (pp. 160–161)
If one color is outnumbered two to one or four to one, segregation is greater than with equal numbers for the same demands. With the minority at half and demands of about one-third, the minority's ratio is close to 2:1, and the majority's is higher (p. 160). Fig. 13: stars outnumber zeros about 2:1, each wants at least two like neighbors (effective demand about 35%). Zeros go from about 1:2 initially to 2:1, a fourfold rise. Stars go from 2:1 to 4:1 (pp. 160–161).

**Absolute-density effect for extreme ratios (five to one or more) (p. 161).**
- Nearly every minority member moves, and everyone moves toward whatever like cluster exists.
- The number of such clusters falls disproportionately as the minority shrinks.
- The minority therefore forms larger clusters, large enough to make even a tolerant majority locally dissatisfied (p. 161).

**Thought experiment (p. 161).** An area is populated by one color. Newcomers of the other color arrive one by one. The first lands at random with nowhere to go, and the second can only join the first. Every later newcomer who wants any like neighbors joins the one cluster. If vacancies allow a significant density, the original residents begin to vacate near the cluster. A solid neighborhood of the new color results, independent of how moderate the newcomers' demands are (p. 161).

**Figure 14 (pp. 161–163).** Stars outnumber zeros five to one. Neighborhoods are the 24 surrounding squares. Zeros demand only two zeros among the 24. Stars demand that zeros be no more than one-third of the 24 (p. 161). In the random start only one star is dissatisfied, but 11 of the 15 zeros are. Results depend somewhat on move order, and two outcomes are shown (pp. 161–163). In the larger neighborhoods zeros achieve not quite one-half like neighbors. Computed on 8-neighbor neighborhoods, they achieve almost three-quarters (p. 163).

#### Population densities (beginning, p. 163)
The unit ends here, partway through this subsection.
- That the more demanding color ends in more homogeneous clusters is mathematically equivalent to its ending with more neighbors, in more densely populated neighborhoods (p. 163).
- Fig. 12: like-to-opposite ratios 2.5 (stars) vs 2.0 (zeros). Stars average 5.35 neighbors, zeros 4.55. They occupy similar numbers of border positions, so the gap is not from neighboring-space counts (p. 163).
- The neighbor count misses blank spaces that lie inside a color's clear territory. Drawing "collective territories" in Fig. 12: of 59 blanks, about 14 go to stars and about 45 to zeros (10 ambiguous ones split five each) (p. 163).
- 72 stars occupy 86 spaces (density .83, 17% vacant). 77 zeros occupy 122 spaces (density .63, 37% vacant) (p. 163).
- Schelling says Fig. 12 may show the effect more than average, but it introduces the useful notion of "collective territory" (p. 163). The sentence breaks off at the end of the unit.

## Toy example (ours, not from the text)
**Setup:** a line of 8 people, each seeing one neighbor on each side (an end person has one neighbor). Each wants at least half of his neighbors alike. Rules follow Schelling's: nearest acceptable insertion point, left-to-right turns, a discontent who is content on his turn stays, no anticipation.

**Start:** positions 1–8 = `+ O + O O + O +`.
- Check each person: 1 (nbr O) discontent; 2 (+,+) discontent; 3 (O,O) discontent; 4 (+,O) content; 5 (O,+) content; 6 (O,O) discontent; 7 (+,+) discontent; 8 (nbr O) discontent.
- Discontents: persons 1, 2, 3, 6, 7 and 8 (six people).

**Turn of person 1 (+).** Remove him: `O + O O + O +`. The gap before the first O has only an O neighbor, so it fails. The gap between O and + has neighbors O and +, one of two alike, so it works (he passes one neighbor). New line: `O + + O O + O +` (labels: 2,1,3,4,5,6,7,8). Person 3 now has neighbors + and O, so he is content.

**Turn of person 2 (O).** At the left end he has only a + neighbor, so he is discontent. Remove him: `+ + O O + O +`. The gap between the two stars gives neighbors + and +, which fails. The gap between + and O (after the second star) gives +, O, one of two alike, so it works. He passes two neighbors. New line: `+ + O O O + O +`.

**Turn of person 3.** He is a star with neighbors + and O, so he is content and stays.

**Turn of person 6 (+).** His neighbors are O and O, so he is discontent. Remove him: `+ + O O O O +` (the last + is person 8). Moving right passes one person (O7) and lands between O7 and +8 (neighbors O,+), which works. Moving left passes three. Nearest is right. New line: `+ + O O O O + +`.

**Turns of persons 7 and 8.** Person 7 (O) now has neighbors O and +, so he is content. Person 8 (+) has neighbor +, so he is content. They stay.

**Final:** `+ + O O O O + +`. Check everyone: positions 1–8 have like-neighbor counts 1 of 1, 1 of 2, 1 of 2, 2 of 2, 2 of 2, 1 of 2, 1 of 2, 1 of 1. All are content.

**Measure (like neighbor slots / all slots).** Adjacent pairs: 7. Each pair counts for two people, so 14 slots.
- Start `+ O + O O + O +`: alike pairs: only (O,O), so 1 of 7. Like slots = 2 of 14, about 14%.
- End `+ + O O O O + +`: alike pairs: (+,+), (O,O), (O,O), (O,O), (+,+), so 5 of 7. Like slots = 10 of 14, about 71%.

The demand was only "at least half". Yet the average like share rose from 14% to 71%. Even a pattern that just satisfies everyone, `+ + O O + + O O`, would have had 4 alike pairs of 7. This tiny run has no equilibrium proof. It only shows the compounding in a case small enough to check.

## Concepts
- [[micromotives-vs-macrobehavior]] — individual choices can produce collective outcomes that no one intended and that need not reflect what anyone wants (pp. 145–146)
- [[agent-based-model]] — hand-run counters on a line or board that move by local rules (pp. 149, 154–155)
- [[generative-explanation]] — shows by simulation that simple preferences can produce the aggregate pattern (pp. 150–151, 156)
- [[emergence]] — clustering far beyond individual demands arises from interacting moves (pp. 150–151, 158)
- [[fixed-point-and-stability]] — an arrangement in which nobody wants to move; complete segregation can be stable (pp. 148, 150)
- [[feedback]] — reciprocated avoidance amplifies segregation (p. 145); a mover also becomes a like neighbor to others (p. 159)
- [[homophily-and-social-influence]] — here, an assumed preference about the color of one's neighbors (p. 149)
- [[nonlinearity]] — segregation rises rapidly with demand between about 35% and 50% (p. 159)
- like-neighbor share (new) — average proportion of neighbors of own color; one measure Schelling uses (p. 156)
- growth nodes (new) — chance spots where enough like members coincide to anchor a stable cluster (p. 153)
- absolute-density effect (new) — small minorities cluster by absolute numbers, not relative size (pp. 153, 161)
- collective territory (new) — a region imputed to one group, including vacant squares, unlike individual neighbor counts (p. 163)
- patterning (new) — departure from randomness, related to but distinct from homogeneity (p. 156)

## Canonical instances
- [[schelling-linear-model]] — 70 stars and zeros on a line, demand half like among eight neighbors, six clusters of average size 12 (pp. 149–151)
- [[schelling-checkerboard-model]] — 13 × 16 board, ~30% vacancies, 3 × 3 neighborhoods, nearest-vacant-square moves (pp. 154–158)
- [[segregation-quantitative-constraints]] — hospital rooms, alternate seating, college freshmen as logical limits on mixing (p. 147)
- [[minority-in-an-all-majority-area]] — newcomers arriving one by one cluster together and may displace residents (p. 161)

## Bridges (candidates)
- [structural-analogy] Equilibrium of "everybody content" in Schelling's models ↔ fixed point and stability: a state where nobody moves, stable against small deviations but not toward other states (p. 148).
- [structural-analogy] Compounding of demands through moves ↔ feedback: each move changes others' satisfaction (p. 159).
- [metaphor] Schelling's depressions and bank failures as macro-effects of savers ↔ micromotives vs. macrobehavior (p. 146).

## Questions this raises
- How robust are the clusters to different move orders, board shapes or fully random simultaneous moves, given that Schelling ran these by hand (p. 155)?
- Schelling suggests the minority-size effect may extend to real cases. What data would show it (p. 158)?
- Do the "mixed" stable outcomes appear in a model with individual-specific tolerances, as the second model promises (p. 148)?
- How much of observed segregation can be inferred about individual motives from aggregate patterns? The abstract says usually not (p. 143).

## Reading notes
- **Part boundaries:** this unit starts at the abstract (journal p. 143) and ends mid-sentence on journal p. 163, inside "Population Densities" ("…a necessary"). The remainder of the paper (the compartmented model, tipping and later material) is not covered.
- **Page numbers:** the extracted labels give "printed=?" for the first pages and values 2–15 for later pages, but the page images show the journal's own page numbers 143–163 (e.g. "150" on the page labelled printed 2). I cite journal pages; **journal page = pdf + 141**. Pdf 1 is the publisher's cover sheet.
- **Misprints and oddities seen:** p. 160 prints the stars' ratio as "2:5"; p. 163 gives 2.5 versus 2.0. On p. 150 "440 out of 540 neighbors" is printed. 70 people × 8 neighbors is 560, and the 540 is not explained on these pages. The "11 × 16 matrix" on p. 158 differs from the 13-row board on p. 155. Percent 40% (p. 158) vs 39% (p. 158 footnote) is also a small inconsistency.
- **Figures:** the text layer for Figs. 7–14 is garbled. I used the images only for the visible counts and did not recount counters.
- Schelling says all checkerboard runs were done by hand and eye (p. 155).
