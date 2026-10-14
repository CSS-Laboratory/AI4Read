---
id: schelling-1971-segregation/main-p2
work: schelling-1971-segregation
unit: paper (part 2/2) — end of the checkerboard model, the bounded-neighborhood model, and tipping
pages: 13–36
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
# Dynamic Models of Segregation (part 2): density, integrationist preferences, the bounded-neighborhood model, tipping

## L0 — One line
Individual tolerance limits, applied to a shared area, can give one or several self-reinforcing equilibria, and which one is reached depends on group sizes, tolerance schedules and starting conditions, not on average tolerance alone.

## L1 — The gist (≤ 120 words)
This part finishes the checkerboard ("proximity") model and then builds a second model with one shared, bounded neighborhood. Each person leaves if the share of the other color passes a personal limit. Plotting white and black tolerance as curves in absolute numbers shows when stable mixtures exist, when only all-white or all-black outcomes are stable, and how quotas or concerted action change this. The same model fits both a preference for separation and a preference for integration. Applied to "tipping", it shows that it is often unclear which point is the tipping point, and that none need sit at the typical tolerance value. This matters because collective results need explicit analysis of how individual decisions combine.

**Prerequisites:** the star/zero checkerboard rules from part 1; reading curves on a graph; cumulative distributions; the idea of a stable equilibrium.

## L2 — Key ideas
- When demands are equal but numbers differ, the minority clusters at higher density, and its territory is more fully occupied (about 83% vs about 64%) (p. 13).
- A pure preference to have three like neighbors, with no dislike of the other color, segregates about as strongly as a demand for majority status (p. 14).
- Tentative experiments suggest that integrationist preferences also give striking non-random patterns, but with many more moves, a "rationed" minority (if one color is a minority) and empty "dead spaces" (p. 16).
- Bounded-neighborhood model: tolerance schedules are converted into absolute-number curves; where they overlap a mixture is statically viable, but in the Fig. 18 example the dynamics push to a one-color extreme (pp. 18–21).
- Stable mixtures depend on the shapes and relative sizes of the schedules. Limits on numbers can sometimes create them, and swapping in more tolerant members does not necessarily make a stable mixture more likely (pp. 21–25, 28–29).
- The model fits integrationist and separatist preferences alike, so results do not need a wish to live apart (p. 30).
- "Tipping" often has no clearly identifiable single point; the cases shown depend on curve shapes, capacity, group sizes, speculation and boundaries, and need not occur at the modal tolerance value (pp. 32–36).

## L3 — Walkthrough

### Checkerboard model, continued (density, neighborhood size, preferences)
**Density.** Equal demands but unequal numbers also produce a density difference: the minority gathers in denser neighborhoods (p. 13).
- Fig. 13: mean neighbors per zero 6.0, per star just under 5.0.
- Zero territory has about 83% occupancy, star territory about 64%. Star territory's vacancy rate is just over twice that of zero territory. Four ambiguous blanks were split two each (p. 13).
- Fig. 15 (more extreme): stars outnumber zeros almost 4:1. Stars want at least one star among four or fewer neighbors, at least two among five or more. Zeros want at least two of five or fewer, three of six or seven, four of eight (p. 13).
- Result: clear separation, nearly complete occupancy of zero territory amid dispersed stars. Stars average 5.1 neighbors, zeros 6.8 (maximum 7.0 given their positions) (p. 13).
- Schelling warns that this is "suggestive but not easily related to residential patterns". The model ignores incomes, family sizes and the cost of space (p. 13). Illustration: if surfers want solitude but swimmers want even more to avoid surfboards, the groups separate and the surfers get more acreage per capita (p. 13).

**Size of neighborhood.** Counting neighbors over a larger area attenuates segregation, at least for moderate demands and near-equal numbers. This may not hold with less tolerant demands and greater numerical differences (pp. 13–14).

**Congregationist preferences (Fig. 16).** Each individual wants three like neighbors out of eight (two of five at the edge) and is indifferent to the other color; opposite neighbors count like blanks (p. 14).
- Result: like neighbors just over 75% overall; 38% have no opposite neighbor. This is comparable to Fig. 10 (p. 14).
- Everyone's demands tolerate up to five opposite neighbors out of eight. Yet seeking an absolute number of like neighbors separates people "just as if he had demanded majority status" (p. 14).

**Integrationist preferences (Fig. 17).** Earlier runs had only minimum demands for like neighbors. Now there is also an upper bound, or a preferred ratio (p. 14). In both panels zeros are just over half the number of stars (p. 14).
- Left panel, limits on like neighbors. Of eight neighbors: 3–6. Of seven: 3–5. Of six: 3–4. Of five: 2–4. Of four: 2 or 3. Of three: 1 or 2. Of two: 1 (p. 16).
- Right panel, a preference scale. Of eight neighbors: five like is first choice; four and six tie for second; then three/seven; two/eight; one; none. Similarly for other counts: half for odd, just over half for even (p. 16).
- Tentative findings, absent under purely separatist demands (p. 16):
  1. Integration needs more complex patterning. It takes many more moves, more people move, more may be unsatisfiable, and the demands may be inconsistent with each other and with the overall color ratio.
  2. A minority must be "rationed": patterns must be efficient so majority members can share minority neighbors. The result looks just as non-random, but different. The minority may form conspicuous lines instead of convex clumps.
  3. Moving creates "dead spaces". The center of a densely settled area empties, neither color enters, and the boundary stays stable because it touches the other color. Blank spaces then form their own clusters.

> Intuition note: In the star/zero model, a clumped or sparse pattern is a joint result that nobody chose. Even a wish for three like neighbors, or a wish for mixing, produces structure at the group level in these runs.

### Bounded-neighborhood model
**Setup (p. 17).** There is one common area with fixed boundaries. A person is inside or outside, and cares only about the color ratio inside, not about layout. "Residence" can also mean membership in a job, club, church or voting bloc (p. 17).
- Everybody prefers this area to the alternatives. Each person stays unless the percentage of the other color exceeds a personal limit, called "tolerance". Beyond the limit, he goes elsewhere (p. 17).
- Tolerance is comparative and specific to this location. A white who seems less tolerant may merely be more tolerant of the alternatives (p. 17).
- Compatible upper bounds must add to at least 100 percent, or no contented mixture exists. If nobody tolerates extreme ratios, an area occupied by one color alone stays that way, because nobody will be the first other-colored entrant (p. 17).
- Assumptions: all preferences are upper limits on the other color; no minority-seeking and no lower limits; only ratios matter; no positions within the mix (p. 17). People both leave and return; information on the current ratio is perfect, but no one knows others' intentions or projects turnover (pp. 17–18).
- Sorting assumption: among dissatisfied people of one color, the least tolerant leaves first and the most tolerant enters first. So those inside are always more tolerant than those outside (p. 18).
- The relative speed of white and black movement is left open (p. 18).

**Straight-line example (p. 18).** The data are a cumulative distribution of tolerance. There are 100 whites. The median white accepts a black:white ratio of 1.0. The most tolerant accepts 2.0 (a one-third minority). The least tolerant accepts 0. The schedule is a straight line from 2.0 on the ratio axis to 100 whites on the horizontal axis (Fig. 18, top) (p. 18).
- Blacks have an identical schedule but number 50. Some mixtures are obviously possible. For example, the more tolerant 25 blacks with 25 of the more tolerant 50 whites would be content (p. 18). Also 10 blacks tolerate a ratio of 1.6 (16 whites), and 16 whites among those willing to accept 10:16 would join them (p. 18).

**Translation to absolute numbers (pp. 18–19).** The curve W gives, for each number of whites, the number of blacks they will tolerate: their own number times their ratio.
- Examples given: 50 whites tolerate 50 blacks; 75 tolerate 37.5; 25 tolerate 37.5; 90 tolerate 18 (p. 19).
- The straight line becomes a parabola. Economists will see the same step as from a demand curve to a total revenue curve (p. 19).
- (added step) For the line $R(W)=2(1-W/100)$, the curve is $B_{\max}(W)=W\,R(W)=2W(1-W/100)$. This matches 50→50, 75→37.5, 25→37.5, 90→18.
- The blacks' schedule gives a smaller parabola opening toward the vertical axis (p. 19).

**Static viability (p. 20).**
- A point inside both parabolas is a statically viable mixture: that many whites tolerate that many blacks, and vice versa.
- A point under the white curve but right of the black curve leaves all whites content but not all blacks.
- A point outside both curves leaves some of both colors dissatisfied (p. 20).

**Dynamics (p. 20).** If all whites present are content, they stay, and outsiders who would be content enter. If some are discontent, the least tolerant leave, until those remaining are content. Blacks follow the same rule (p. 20).
- Inside the overlap, both numbers rise. Under W but outside B, whites enter and blacks leave, toward the lower right, until all blacks have left. Under B but outside W, the reverse. Outside both, both colors depart until one is within its own curve; then the other color leaves entirely (p. 20).
- For the Fig. 18 curves there are only two stable equilibria: all black and no white, or all white and no black (p. 20).
- Which one occurs depends on initial conditions and possibly on relative speeds. If one color predominates it takes over. If both start in viable numbers, relative speeds of entry decide. If both start large, relative speeds of exit decide (p. 20).
- Mixes in the overlap exist, but they attract more outsiders and eventually mostly one color. A few of the opposite color then leave, which weakens the status of those who stay, and the minority evacuates cumulatively (pp. 20–21).

> Intuition note: In the Fig. 18 example, a viable mixture can exist and still not last. Each entry or exit changes the ratio that others face, so the change feeds itself until one color is gone.

**Alternative schedules (pp. 21–22).** The outcome depends on schedule shapes and group sizes.
- Fig. 19: equal numbers (100 each). The median white tolerates 2.5 blacks per white. The most tolerant tolerates 5. The least tolerates none. Both colors have identical schedules (p. 21).
- Besides the all-white and all-black equilibria there is a stable mixture of 80 blacks and 80 whites (p. 21). (added step) For this schedule $B_{\max}=5W(1-W/100)$, which gives 80 at $W=80$.
- If slightly over 40% of both colors are present, entry and exit lead to 80–80. Even with very small numbers present it is reached if the initial ratios lie within the slopes of the two curves (a bit over 4:1 either way) and neither color enters much faster. Starting from a one-color area, concerted entry of more than 25% of the other color is needed. So all three equilibria are stable against fairly large perturbations (p. 22).

**Alternative numbers (p. 22).** The stable mixture disappears if blacks exceed whites, or whites exceed blacks by, say, two to one: one curve then lies inside the other (Fig. 20). It also disappears with equal numbers and less steep schedules (the Fig. 18 case, Fig. 21). For straight-line schedules and equal numbers, there is no stable intersection unless the vertical intercepts are 3.0, with median tolerance 1.5 (p. 22). The text says "unless the tolerance schedules have vertical intercepts of 3.0".

**Limiting numbers (pp. 23–24).**
- Limiting whites in the area to 40, with the most tolerant 40 first in and last out, turns Fig. 20 into Fig. 22. This has a stable mixture at 40 whites and a comparable number of blacks (p. 23).
- With the Fig. 18 curves, both colors must be restricted (Fig. 23). If only the total can be restricted, there is a neutral equilibrium along the overlapped part of the 45-degree line (Fig. 24). With turnover the mix may drift; if it leaves the overlap to the lower right, the black minority evacuates (pp. 23–24).
- A cap on whites acts as if the excess whites had no tolerance at all. Their absence keeps whites from overwhelming blacks by numbers (p. 24).

**Varying tolerance (pp. 24–25).** "Greater tolerance" does not necessarily raise the chance of a stable mixture. This holds if it means swapping some members of a population for more tolerant ones (p. 24).
- Replacing the two-thirds least tolerant whites in Fig. 22 by even less tolerant whites keeps the whites from overwhelming the blacks (p. 24).
- Making all whites less tolerant (a merely less steep schedule, shortening the whites' parabola in Fig. 22) does not give the stable intersection (p. 24).
- What is needed: near a dividing point of about 40% of whites, those just inside stay as tolerant, and those just beyond become even less tolerant. The very most and very least tolerant matter little if they do not change drastically (pp. 24–25). Fig. 25's broken line gives a stable mixture with blacks outnumbered 2:1 (p. 25).

> Intuition note: In these examples the shape of the whole schedule and the group sizes matter, not just how tolerant people are overall. Making some whites less tolerant can help a mixture survive, because their absence keeps the whites from overwhelming the blacks by numbers (p. 24).

### Varieties of results (pp. 25–30)
Schelling lists results without showing all the analysis (p. 25):
1. The only logical restriction on a tolerance schedule is that it slopes downward to the right. For the absolute-number curves, a ray from the origin crosses the curve only once. Within this, one, two, three or more stable equilibria are possible, including several mixtures. Several mixed equilibria are usually sensitive to small changes. The one-color extremes tend to be least disturbed by shifts in schedules or numbers, and a single mixed equilibrium may be fairly immune to shifts (pp. 26–27).
   - Fig. 26: whites split into unlimited, same limited, and zero tolerance. With equal and similarly divided blacks there are three stable equilibria. With blacks at half the whites' number there is a single equilibrium (p. 27).
   - Fig. 27: a rectangular hyperbola $RN=.9$ (R = opposite:own ratio, N = number) versus a horizontal line $R=1.1$. The line lies almost wholly inside the hyperbola and looks much less tolerant. Yet it yields a precarious stable equilibrium with all blacks and all whites present, stable only against small perturbations. So a schedule that is less tolerant throughout can still produce stable mixtures (p. 28).
2. To make a stable mixture possible it is sometimes sufficient to limit one color's number. It is sometimes necessary to limit both. If the curves do not overlap at all, no numbers limit will help (p. 28).
3. A ratio limit on entry (Figs. 28, 29) may or may not give a stable equilibrium. It may also exclude some stable equilibria. In Fig. 28 the ratio limits give no stable mixture; the stable equilibria are all-white and all-black without all the people. In Fig. 29 a stable equilibrium appears where the white/black limit meets the blacks' reaction curve (pp. 28–29).
4. A limit on total occupancy can give a neutral equilibrium, wide or narrow (p. 29).
5. With similar schedules, a stable mixture is more likely the more nearly equal the two numbers are. A greater disparity leaves fewer schedules that work (p. 29).
6. In general, for a stable mixture the minority must be the more tolerant group. Either the majority outnumbers the minority locally, or a larger share of the majority stays out. If whites outnumber blacks 5:1 overall, a mixed local population needs either whites outnumbering blacks locally, or four-fifths or more of whites unable to abide equal numbers (p. 29).
7. With only two locations, one preferred by both colors, the alternative location must end up with one color only. The reason: any ratio difference between the places gives the color with the worse ratio there a double motive to enter the preferred area, and at equal ratios both colors would want to move (pp. 29–30). This restriction can create or destroy a mixed equilibrium in the preferred area. On Fig. 20 it gives a mixture of all the blacks and some whites, plus two segregated equilibria. On Fig. 19 it removes the mixture (p. 30). If preferences are divided between two areas, results may include mixtures in both, one mixture plus a one-color remainder, or segregation, depending on curves and initial conditions (p. 30).

### Integrationist preferences, again (p. 30)
The results do not need a preference for living separately or even for being in the majority (p. 30).
- The same schedules can be reinterpreted as the upper limits at which a preference for mixed living is outweighed by extreme minority status. The same model and the same results fit both hypotheses. The only asymmetry is that no lower limit on the other color is postulated (p. 30).

### Policies and instruments (pp. 30–31)
- The analysis applies to numerical or ratio quotas, limits on totals, and concerted action. An intersection of curves is a stable equilibrium but usually competes with one-color equilibria. When there are two or more potential stable equilibria, initial conditions and rates of movement decide which results (pp. 30–31).
- Getting "over the hump" to another equilibrium often needs a large perturbation or concerted action. Blacks and whites cannot both successfully concert in opposition to each other; either color may overwhelm the other by concerted action, but not both at once (p. 31).
- Limits: no speculation, time lags, organized action, misperception, or many areas. The model can be enlarged to include some of these (p. 31).

### Tipping (pp. 31–36)
**Evidence and definitions.** "Tipping" occurs when a recognizable new minority enters a neighborhood in sufficient numbers to make earlier residents start to leave (p. 31).
- **Grodzins:** "for the vast majority of white Americans a tipping point exists"; he cites 20% Negroes as a commonly estimated limit in some Eastern cities. He holds that once a change begins it is rarely reversed. Schelling notes, in a parenthesis, that this could mean either that tipping is nearly universal and irreversible, or that tipping, when it occurs, accelerates a process that is inevitable and irreversible anyway (p. 31).
- Duncan and Duncan (Chicago, 1940–50): no mixed neighborhood (25–75% white) in which succession was arrested or reversed (p. 31).
- Mayer: a neighborhood of about 700 single-family homes. A few houses were sold in 1955; a year later 40 had been sold and all called it "mixed"; in another two years, above 50%, and the end result was no longer questioned (p. 31).
- Similar cases: other ethnic groups, clubs, schools, occupations, apartments, sexes, age groups. An ice cream parlor in Lexington, Massachusetts "tipped" to a teenage clientele and closed (p. 31).

**Characteristics a model needs (pp. 31–32).** Boundaries; recognizability of entrants; turnover; potential entrants and their rate; alternatives for evacuees and for the minority (pp. 31–32).
- Schelling says the phenomenon is alleged to occur in a well-defined neighborhood when something disturbs the original equilibrium at 100% white. For houses there is a capacity limit; entry is limited by turnover or by how fast residents can leave. Resident whites may be more tolerant than outsiders, since it takes more to make a family move out than to decide not to move in (p. 32).

**Results (Figs. 30–32).**
- It is often unclear what to call the "tipping point". Several points show a discontinuity or the start of a cumulative process. None need occur at the modal tolerance value. If "most Americans can tolerate about 20 percent", tipping points will tend to be at quite different figures (p. 32).
- *In-tipping.* If the black reaction curve encloses the all-white point (Fig. 30, upper left), blacks are ready to enter as houses open. If not, the all-white equilibrium must be overcome. Ways: concerted entry, erroneous entry, organized introduction, or redefining the boundary (p. 32).
- The number of blacks willing to enter as a small minority may be too small to attract others yet grow large cumulatively over time. Where the black curve cuts the 45-degree capacity line, "we might say" tipping-in has begun: blacks surge in if houses are available, rather than merely show up from time to time (pp. 32–33).
- Fig. 31: if there are too few blacks to fill the area, two outcomes arise. Whites evacuate and the area ends all black and partly vacant (middle panel). Or a mixed equilibrium remains with excess capacity (lower panel) (p. 33).
- Fig. 32: a few blacks cause appreciable white evacuation, but white tolerance becomes inelastic, and the white curve steeply cuts the 45-degree line. Evacuation then stops, and more blacks enter only through normal turnover. If the mix later reaches a point where the curve cuts the line again, cumulative evacuation resumes (pp. 33–34).
- Subneighborhoods. If blacks accept 30% of a subneighborhood of 50 houses, they may tip in at 15 black homes. In a neighborhood of 1,000 houses that is only $1\tfrac12$% (p. 34). Where whites count adjacent blacks, the checkerboard model may apply in the small and the bounded-area model in the large (p. 35).
- Speculation. Whites may react to an anticipated increase. Then the number needed for "out-tipping" is the number that induces the belief, not the number that starts the cumulative process above. Early leavers may strengthen others' belief (p. 35). Speculative departure needs a penalty for late departure or a premium for early departure (p. 36).
- Channeling. Fixed neighborhoods may concentrate black demand on one area, make whites believe it will, confirm the tipping hypothesis, and focus real estate activity on a target neighborhood. So neighborhood tipping, unlike the domino effect of very local proximity avoidance, depends on comparatively small and well-defined neighborhoods (p. 36).
- Open questions: whether a whole metropolitan area, or the U.S. Army, could tip; city school systems seem to lend themselves to it (p. 36).

**Conclusion (p. 36).** Studying tipping anywhere, for any dichotomy, requires "explicit attention to the dynamic relationship between individual behavior and collective results" (p. 36). Even recognizing tipping requires knowing what it would look like given individuals' motives or decision rules (p. 36).

## Toy example (ours, not from the text)
Four whites and four blacks, as a small version of the bounded-neighborhood model. Each person's tolerance is the maximum number of the other color per own color.
- White limits, from most to least tolerant: 3, 2, 1, 0.5. Black limits are the same.
- With $w$ whites present (the $w$ most tolerant), the whites tolerate $w\cdot r_w$ blacks. Here $w=1$: $1\times3=3$; $w=2$: $2\times2=4$; $w=3$: $3\times1=3$; $w=4$: $4\times0.5=2$. So the white curve is $(3,4,3,2)$ and the black curve is the same.
- Start at $(w,b)=(1,1)$. Whites are content since $1\le3$, and so are blacks. Outsiders would also be content, so both enter. At $(2,2)$: $2\le4$, content. At $(3,3)$: $3\le3$, content.
- A fourth white would need $b\le 2$ but $b=3$, so he stays out. A fourth black likewise. So $(3,3)$ is a stable mixture. If one white leaves, $(2,3)$ is still content ($3\le4$) and he returns.
- Start at $(4,0)$ (all white). A first black would face 4 whites, but his limit allows only $1\times3=3$. He does not enter, so $(4,0)$ is stable.
- Lesson: the same schedules give a stable mixture and a one-color equilibrium. The start decides which. (We assumed both colors enter at the same speed.)

## Concepts
- [[tipping point]] — Schelling's "tipping": a minority's entry causes cumulative evacuation; often no clear single point, and none need occur at the modal tolerance (pp. 31–32)
- [[threshold model]] — each person stays only while the other-color ratio is within a personal limit; outcomes depend on the distribution of limits (p. 17)
- [[fixed point and stability]] — stable equilibria are curve intersections or one-color corners; stability against small or large perturbations (pp. 20, 22)
- [[attractor / basin of attraction]] — initial conditions and relative speeds decide which stable equilibrium is reached (p. 20)
- [[micromotives vs. macrobehavior]] — collective patterns (density, dead spaces, tipping) that arise from individual decision rules; tipping analysis must relate collective results to individual motives (pp. 13, 36)
- [[feedback (positive/negative)]] — each exit worsens the ratio for those who stay, producing cumulative evacuation (p. 21)
- [[path dependence]] — the outcome depends on starting mix and relative speeds (p. 20)
- [[homophily and social influence]] — checkerboard sorting from a preference for like neighbors (p. 14)
- [[reaction curve]] (new) — the absolute-number curve (W or B) giving how many of the other color each group tolerates (pp. 19, 28)
- [[static viability]] (new) — a mixture inside both curves, where all present of both colors are content (p. 20)

## Canonical instances
- [[schelling-checkerboard]] — density, congregationist and integrationist variants of the star/zero model (pp. 13–16)
- [[bounded-neighborhood-model]] — one shared area, tolerance schedules, parabolic reaction curves (pp. 17–30)
- [[russell-woods-mayer]] — a neighborhood of about 700 homes that tipped in a few years (p. 31)
- [[chicago-duncan-1940-50]] — no mixed neighborhood arrested or reversed succession in 1940–50 (p. 31)

## Bridges (candidates)
- [structural-analogy] stable equilibria from curve intersections ↔ dynamical systems: fixed points and basins of attraction — the same picture of several stable states, with initial conditions choosing.
- [structural-analogy] cumulative evacuation ↔ positive feedback — each departure raises the ratio pressure on those who remain.
- [same-math] translating a cumulative tolerance schedule into absolute numbers ↔ economics: demand curve to total revenue curve — the text states the same arithmetic (p. 19).
- [structural-analogy] distribution of individual limits ↔ threshold models of collective behavior — cascade size depends on the distribution of thresholds.

## Questions this raises
- How would the stable mixtures change if people could observe each other's intentions, or if moves had lags and costs?
- If tolerance shape matters more than its average, what data would show the real schedules?
- When do proximity (adjacency) reactions and area-ratio reactions interact, as Schelling suggests for small and large scales?
- Can concerted action realistically reach a mixed equilibrium when one-color equilibria compete with it?

## Reading notes
- This is part 2 of 2. It starts mid-section, in the checkerboard model's discussion of density (printed p. 13, journal p. 164), and ends with the references (printed p. 36, journal p. 186). The split was at an even boundary, so there is no title page.
- Page labels: printed 13–36 are the page labels supplied with the source pages; the page images themselves show only the journal page numbers. The running heads show journal pages 164–186. The labels skip 15 (pdf 24 = label 14, pdf 25 = label 16), though the running heads are consecutive (165, 166). Journal page = label + 151 for labels 13–14, and + 150 for labels 16–36. All citations here use the labels.
- Text layer is garbled on the figures (the checkerboards); I took the figure descriptions from the prose only.
- Possible slips in the source: (1) p. 19 says "20 can tolerate 36", but the straight line $R=2(1-W/100)$ gives $20\times1.6=32$. (2) p. 18 says "80 or so whites" tolerate a ratio of 10:16 (0.625); the line gives about 69. I report the author's numbers as printed and flag both here.
- p. 22 says the equal-number mixture needs "vertical intercepts of 3.0". I give this as printed; I did not check it.
- The final footnote refers to Schelling (1969) and Morrill (1965); I did not use them.
