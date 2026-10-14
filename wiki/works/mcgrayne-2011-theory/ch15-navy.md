---
id: mcgrayne-2011-theory/ch15-navy
work: mcgrayne-2011-theory
unit: "15. The Navy Searches"
pages: 182-210
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 20
pipeline_version: 0.1
---
# The Navy Searches

## L0 — One line
In Cold War searches for lost bombs, submarines and boats, Bayes' rule slowly proved its worth: expert-built priors were updated with search results, and growing computer power made this practical.

## L1 — The gist (≤ 120 words)
How did the U.S. Navy come to use Bayes' rule? The chapter follows the 1966 H-bomb search at Palomares, the 1968 *Scorpion* search, Coast Guard rescue and submarine tracking. Expert scenarios gave a prior. "Search effectiveness" numbers recorded what had been covered. Updating then shifted effort to unsearched cells that were still probable. At Palomares updating was not used, and the bomb was found thanks to a fisherman and the submersible *Alvin*. The *Scorpion* search used Bayes from start to end, with a prior made by Monte Carlo (random-simulation) methods. Later systems found drifting survivors and tracked a Soviet submarine. The story shows how reluctantly officers accepted Bayes, and how computers made it practical.

**Prerequisites:** prior, likelihood and posterior in plain terms; probability as a degree of belief; the idea of a grid of cells with a probability in each.

## L2 — Key ideas (5–10 bullets)
- Craven built the Palomares prior from expert guesses and his own "imagineering" because he had one night. He hired mathematicians to give it a "cloak of authenticity" (pp. 185–186).
- Wagner concluded that the navy mainly wanted a credible certification for the President that the bomb could not be found; Richardson's orders were to document that everything possible was done. Richardson's "Search Effectiveness Probability" became the focus, not Bayesian updating (pp. 188, 191–192).
- The chapter's verdict: without updating there was no Bayes at Palomares. The author names Orts and *Alvin* as the heroes (p. 195).
- Bayesian logic: a fruitless search of one cell raises the probability of the others. Richardson adds that it is generally optimal to keep searching the highest-probability area (pp. 189, 201).
- The *Scorpion* search was the first to use Bayes from beginning to end. It used a Monte Carlo prior map of 10,000 simulated points (pp. 199–201).
- Subjective information is kept and weighted, not discarded. Coast Guard rules required it (pp. 204–205).
- Bayesian updating with Monte Carlo found drifting survivors in 1974 and 1976 (pp. 205–206).
- Tracking a moving Soviet submarine (1976) succeeded, and by Richardson's account most officers became believers (pp. 207–208). Ray Hilborn left the 1979 NATO symposium convinced Bayesians "can compare hypotheses" (p. 209).

## L3 — Walkthrough
The chapter has no numbered sections. Headings below follow its narrative order.

### The Palomares accident (pp. 182–183)
- The author says the navy embraced Bayes "slowly and grudgingly" in the Cold War, at first for the trappings of statistics (p. 182).
- On 17 January 1966 a B-52 and a KC-135 tanker collided during midair refuelling over Palomares, Spain. Seven of 11 crew died (pp. 182–183).
- Four hydrogen bombs fell. None exploded, because they were not "cocked". Two bombs' parachutes failed, so their conventional explosives detonated and spread plutonium (p. 183).
- Three bombs were found within 24 hours. The fourth was missing, and it was presumably in the sea (p. 183).
- Palomares was at least the 29th serious accident involving the air force and nuclear weapons. Ten weapons in eight accidents were lost at sea or in swamps (p. 183).

### Craven's "search doctrine" (pp. 183–187)
- John Piña Craven, chief scientist of the navy's Special Projects Office, was asked to find the bomb. He and salvage chief Capt. William Searle formed a joint committee. Searle demanded a "search doctrine" (a plan) by the next morning (pp. 183–184).
- Craven already knew Bayes from several sources:
  - Rufus Reber, who turned Koopman's Bayesian antisubmarine studies into classified tables.
  - MIT visits.
  - Howard Raiffa (p. 184).
- Craven understood Raiffa as saying bettors' pooled hunches work well. **Raiffa later said** Bayes enters only when subjective views are updated with new information, and that he had talked about weather forecasting (p. 185).
- Craven had experts on B-52s, bombs, parachutes, winds and sand burial. He planned to have them form hypotheses and give each a probability (p. 185).
- The author says most academic statisticians would have refused. Following Fisher and Neyman, they would confine information to verifiable sample data (p. 185).
- With one night and one technician, Craven interviewed the experts and imagined what absent ones would bet: "a lot of imagineering" (p. 185).
- He wrote seven scenarios (p. 186):
  1. The bomb stayed in the bomber's debris.
  2. It was in bomb debris along the collision path.
  3. It fell free, outside the plane's debris.
  4. One parachute deployed and carried it out to sea.
  5. Both parachutes deployed and carried it farther out.
  6. None of the above.
  7. A fisherman saw it enter the water (added later, after the navy talked to Francisco Simo Orts).
- **Craven's plan:** he told himself he could not sell the idea to operators. So he would call it Bayes' subjective probability and hire mathematicians to put a "cloak of authenticity" on it. He hired Daniel H. Wagner, Associates (p. 186).
- Wagner's view: Bayes' rule is sensitive to information of all kinds, but every clue carries some error, and the size of the error is rarely given, so it must be deduced from other information (pp. 186–187).
- Henry "Tony" Richardson, a young probability PhD, went to Craven's office. Craven showed a chart of the seabed divided into rectangular cells. He had weighted the scenarios on a contour map of probability "mountains" and "valleys" (p. 187).
- Richardson saw this as a rule-of-thumb prior, the first part of Bayes' rule. Assuming bell-shaped probabilities made hand and desk-calculator computation possible (p. 187).
- Ed Loane at Wagner's firm built a finer distribution on a remote computer, using paper tape and telephone lines. Maps were printed as typewriter symbols, for example # for a probability between 0 and .05 (pp. 187–188).

**Intuition note.** A prior can be built from expert opinion about scenarios before any search data exist. Craven did it in one night, and he knew it was subjective.

### What the navy really wanted (pp. 188–192)
- Planning sessions convinced the mathematicians that Bayes was "window dressing". If the bomb was not found, the navy wanted to be able to prove statistically that it was not there, and to give the President a credible certification that it could not be found (p. 188).
- **Wagner's conclusion:** certification was the main reason his firm was hired (p. 188).
- **Richardson's marching orders:** statistically document the search. He hoped to do more, using optimal Bayesian search (p. 188).
- Richardson briefed Capt. Frank Andrews on the flight. A large area is divided into small cells, and failure to find the target in one cell raises the probability of finding it in the others. The missing-sock analogy: after an exhaustive but fruitless search of the bedroom, the laundry becomes likelier. So Bayes gives information even from an unsuccessful search (p. 189).
- The world press was angry about the news blackout and Radio Moscow scooped it. President Johnson phoned daily (pp. 189–190).
- RAdm. William Guest commanded the task force: 3,000 personnel, 25 ships and 4 research submersibles. The search cost $12 million (p. 190).
- Craven's hypotheses were based on prevailing winds, so Guest searched the area "Alpha II" repeatedly (p. 191).
- Richardson found that the charts had search tracks but no measure of effectiveness. Some sensors could not see the bottom (p. 191).
- He coined **Search Effectiveness Probability (SEP)**. For each grid square, SEP is the probability that the bomb would have been found if it had been there, given the effort applied. SEP = 95% means the area is well searched. SEP = 1 means certain to have found it (p. 191).
- He computed SEPs by hand with paper cutouts, a slide rule and an adding machine. His luggage with reference books was lost. Many SEPs were zero, and Guest was unsettled (pp. 191–192).
- Guest used SEPs to document coverage and move equipment. He did not use updating to find new places, and he kept to his "plan of squares" even when a more likely site appeared (p. 192).
- **Richardson's explanation:** admirals are impatient with "priors and posteriors". The author adds that, as a result, evaluating effectiveness became the focus and updating Craven's scenarios was pushed aside (p. 192).

### Orts, *Alvin* and the find (pp. 192–194)
- Fisherman Orts had seen a large parachute splash down. The navy had discounted him because he did not triangulate in the standard way. Lt. Cdr. Brad Mooney believed him after Orts twice pointed minesweepers to the same spot (p. 192).
- Orts's testimony formed a high-likelihood hypothesis: one parachute, then a deep canyon. Mooney drew a one-mile circle, "Alpha I". Of Guest's whole squadron, only the submersible *Alvin* could reach the depths of the highest-probability site, and its battery was fading (p. 193).
- Six weeks after the crash, *Alvin*'s crew saw a drag track on a slope, but a low battery and a storm stopped them (p. 193).
- Johnson was told only probabilities, and he demanded a date. Craven convened professors at the Pentagon on 15 March 1966. They endorsed the Bayesian plan and went to lunch (p. 193).
- During the lunch break, *Alvin*, on its nineteenth dive, spotted the bomb with its parachute (p. 194).
- The bomb had hit the ground in 1,300 feet of water and slid down to almost 2,850 feet. It lay within a mile of Orts's pointing (p. 194).
- Orts sued for $5 million. Richardson estimated that his testimony saved at least a year. In 1971 Orts was awarded $10,000 (p. 194).

### Consequences and verdict (pp. 194–195)
- Military flights over Spain were forbidden and SAC air-alert missions halved. A second accident at Thule, Greenland, and rising costs led McNamara to end airborne alert in 1968 (p. 194).
- Later official reports say residents inhaled far less than the safe maximum of plutonium. Radioactive snails found in 2006 prompted new fears and a joint study (pp. 194–195).
- **Richardson:** his numbers were coverage numbers, and "Bayes was a sidelight" (p. 195).
- **The author's judgment:** priors and shipboard data were never combined in time to help, and "without updating, there was no Bayes". The heroes were Orts and *Alvin* (p. 195).
- Richardson could not get a journal article published. The search did develop SEPs, later called LEPs (local effectiveness probability) (p. 195).
- Craven's faith in Bayes grew. The team concluded that future Bayesian search depended on computer power. Wagner, Associates soon bought a punched-tape terminal (p. 195).

**Intuition note.** In the author's view, having a prior and having coverage data is not yet Bayes: without updating there was no Bayes. At Palomares the two were never combined in time to help the search.

### The Soviet K-129 (pp. 196–197)
- In spring 1968, a Soviet submarine, K-129, and a U.S. one disappeared. Craven headed the Deep Submergence Systems Project and was responsible for both searches (p. 196).
- U.S. sensors recorded a "good-sized bang" on the International Date Line, far from the Soviet search area. Craven hired Wagner, Associates for a probability analysis without telling them the target. Forty years later Richardson still did not know he had worked on that search (p. 196).
- **Craven's three scenarios:**
  - The sound was unrelated.
  - The sub made it but did not sink.
  - The compartments were open and it flooded without collapsing (p. 196).
- **Craven eventually concluded** the sub was a rogue, off on its own against orders. The U.S. told Brezhnev the bang's location. The sub was later photographed but not raised (pp. 196–197).

### The *Scorpion* search (pp. 197–203)
- The USS *Scorpion* vanished in May 1968, along a 3,000-mile route in the Atlantic. Craven learned that a secret listening post had recorded "blips" about 400 miles southwest of the Azores. This cut the search area to three or four square miles (p. 197).
- Craven organized a full Bayesian hunt for *Scorpion* from the start. The plan was a prior computed by a powerful computer, then updated on shipboard with daily results (p. 197).
- The research ship *Mizar* towed a sled with a camera, sonars and magnetometers. Chief scientist Buck Buchanan vowed not to shave until *Scorpion* was found (p. 198).
- Uncertainties were larger than at Palomares: remote location, deep floor, no witness, poor navigation (p. 198).
- *Mizar* was ordered to search Point Oscar repeatedly. Richardson showed graphically that Oscar was oversearched and little probability remained, but the search continued. Changing orders needed persuasion by a detailed prior map. Washington later ordered the map to be treated as an important factor (p. 198).
- Craven and Andrews wrote nine scenarios and weighted them by believability, as at Palomares. A high-priority scenario was based on shiny bent metal found by *Mizar* far from Oscar (pp. 198–199).
- The grid around the blip had cells of 1 mile by 0.84 miles, 140 square miles in all (p. 199).
- **Monte Carlo prior.** Richardson used "little hypothetical submarines" in place of neutrons, a method from the Manhattan Project (p. 199). The author says academic Bayesians adopted Monte Carlo about 20 years later (p. 199).
- **Richardson's description of the simulation** (pp. 199–200):
  - Roll dice to pick a scenario, with its probability.
  - Roll for speed, direction and the unknown time of collision with the bottom.
  - The computer places a point where the sub would have hit the bottom.
  - Repeat 10,000 times. The points are equally likely positions.
  - Draw a grid and count the points per cell. These percentages are the prior.
- Directions were first treated as equally probable, which the author calls Thomas Bayes' simplification (p. 199).
- The map covered 172 cells. Cells E5 and B7 had 1,250 and 1,096 hits. The next 18 cells had 100–1,000, and most cells had under 100 (p. 200).
- The author calls it a real scientific advance over the H-bomb analyses (p. 200).
- Aboard *Mizar*, Wagner's staff estimated the sensors' capability and combined it into one effectiveness number per cell. The author says these numbers would eventually become the second component in Bayes' formula (p. 201).
- **Stone:** with no find, prospects get worse, because remaining time grows. **Richardson:** searched areas go down in probability and unsearched areas go up. It is generally optimal to keep looking in the highest-probability area (p. 201).
- The biggest problem was overestimated sensor capability. Bayes' rule became the "group memory" of the search, used from beginning to end for the first time (p. 201).
- But the prior map took almost a month to reach the scene. Detailed priors were available only on the fourth and fifth cruises in October (p. 202).
- Craven's acoustic studies, using depth charges at known positions, moved the likely spot toward the shiny metal (p. 202).
- In late October *Mizar*'s magnetometer spiked at anomalies in cell F6. On 28 October, after returning to the area, its cameras showed *Scorpion*, 260 yards from the high-probability square. An earlier faulty sonar had passed over it (p. 202).
- **Andrews:** Bayes was one day and half a mile behind Buchanan, and would have found it first otherwise (p. 202).
- Excluding time spent on a misleadingly magnetic, hull-shaped rock, the sled had covered 1,026 miles at one knot, equal to 43 days. This was two days earlier than Bayesian predictions (p. 203).
- Johnson was told the sinking was most probably an accident on board (p. 203).
- Sound analyses suggested *Scorpion* had been heading east, not west. Twenty years later Craven learned it could have been destroyed by a "hot-running torpedo". The text says a defective torpedo, if fired, would probably have turned back and struck the sub that launched it (p. 203).
- **Stone** wrote *Theory of Optimal Search* (1975). It is an unabashedly Bayesian book, and cheaper computers were turning searches into software algorithms (p. 203).

**Intuition note.** The Monte Carlo prior turns the experts' scenarios into counts of simulated sub positions per cell. Counts divided by 10,000 are the prior probabilities. Each day's search results then lower searched cells and raise the others.

### Suez Canal clearance (pp. 203–204)
- After the 1973 war, the U.S. helped Egypt clear unexploded ammunition from the Suez Canal. The unknown quantity was the number of bombs remaining (p. 203).
- Wagner, Associates chose three priors for high, middle and low numbers. They used the conjugate priors of Raiffa and Schlaifer (1961), so each posterior stays in the same class. This gave Poisson, binomial and negative binomial distributions (p. 203).
- Richardson reported that computing became easy, but the system could not be explained to the ordnance-disposal specialists. In the end, no one talked about Bayes at Suez (pp. 203–204).

### Coast Guard rescue and filters (pp. 204–206)
- Joseph Discenza, a Coast Guard rescue coordinator, set out to computerize the manual. He found that the Coast Guard had used Koopman's Bayesian search theory since the Second World War, without knowing it (p. 204).
- Wagner's firm built a computerized system. Probabilities and weights were set by group decision. Each person weighted scenarios privately before averaging, and no scenario was discarded (p. 204).
- **Stone:** leaving out subjective information throws away valuable information. If a ship's radio position and a plane's report disagree, discarding one means giving it weight zero and the other weight one (pp. 204–205).
- Bayesian updating and Monte Carlo (10,000 possible locations) entered the system in 1972 (p. 205).
- Stone used an early Kalman filter. It lets new observations be added without recalculating everything. The author says Kalman denied any link to Bayes, but Aoki proved in 1967 that it can be derived from Bayes' rule (p. 205).
- Data were turned into likelihood functions and combined with priors on movement. The filter concentrated a small number of highly probable paths (p. 205).
- 1974: a tuna boat sank and a freighter chanced on 12 survivors. The Coast Guard calculated backward to the capsize point and forward again, then rescued three more men (p. 205).
- 1976: after a ship capsized, two survivors were found after 22 days by chance. The program then found a third survivor, adrift 28 days, six days later (p. 206).

### Hunting a moving submarine (pp. 206–208)
- The new question was whether Bayes could handle evasive targets operated by humans (p. 206).
- In 1975 John "Nick" Nicholson (later a vice admiral), who had taken command of the U.S. submarine fleet in the Mediterranean, obtained a $100,000 ONR grant to bring Richardson to Naples. Richardson fed an old computer track histories, Soviet sub types, sonobuoy reports and geography (p. 206).
- He made subjective assessments of Soviet officers' behavior. He also used real-time feedback from search results, which the author says Second World War submarine hunters would have called science fiction (p. 206).
- Probabilities were the "common currency" that fused vague data from many sources (p. 207).
- In summer 1976 a Soviet Echo II submarine entered the Mediterranean and was lost near Italy. Nicholson's destroyers were placed across the Sicily Straits (p. 207).
- His superiors pressed him to move east. Richardson estimated about 55% that it had not yet passed, and urged waiting one to two more days (pp. 207–208).
- Nicholson waited, and contact was made. Richardson described the brass as becoming believers in Bayesian search methods (p. 208).
- Later the sub rammed the destroyer *Voge*, perhaps trying to cut its trailing-wire sonar. Its captain was relieved of command (p. 208).

### The 1979 NATO symposium (p. 209)
- The military also explored Bayes for asteroids and Soviet satellites. At the 1979 NATO symposium in Portugal, Richardson and Stone spoke (p. 209).
- Ray Hilborn, a zoologist, said to himself during the talks that real decisions require asking "what are the alternative states of nature, and how much do I believe they're true?" In his words, frequentists cannot ask that question, while Bayesians can compare hypotheses (p. 209).

## Toy example (ours, not from the text)
Three cells hold a lost object. Prior: A = 0.5, B = 0.3, C = 0.2 (sum 1). Search cell A once, with SEP 0.8, and find nothing.

The chapter defines SEP but does not print this formula. We assume that failing to detect leaves a fraction $1-\text{SEP}$ of a searched cell's probability, and that other cells are unchanged. This is the likelihood of "not found".

- Unnormalized: A $= 0.5 \times (1-0.8) = 0.10$. B $= 0.3 \times 1 = 0.30$. C $= 0.2 \times 1 = 0.20$.
- Sum $= 0.10 + 0.30 + 0.20 = 0.60$.
- Posterior: A $= 0.10/0.60 \approx 0.167$. B $= 0.30/0.60 = 0.500$. C $= 0.20/0.60 \approx 0.333$. These sum to 1.

Searching A found nothing, so A fell from 0.5 to 0.167 and B and C rose, as the chapter describes (p. 201). The best next search is B. If SEP were 0, the posterior would equal the prior, which is the "zeros" problem at Palomares (pp. 191–192).

## Concepts
- [[prior-distribution]] — here a map of probabilities over seabed cells, built from expert scenarios (pp. 187, 199–200)
- [[subjective-probability]] — expert and commander judgments kept as weights, not discarded (pp. 185, 204–205)
- [[posterior-distribution]] — probabilities updated by daily search results: searched cells go down, unsearched go up (p. 201)
- [[sequential-updating]] — daily recomputation, with Bayes as the search's "group memory" (p. 201)
- [[likelihood]] — in the Coast Guard system, sensor and weather data turned into likelihood functions (p. 205)
- [[conjugate-prior]] — a prior whose posterior stays in the same distribution class, used at Suez (p. 203)
- [[frequentist-vs-bayesian]] — Hilborn's contrast: Bayesians can ask how much each alternative is believed (p. 209)
- [[monte-carlo-integration]] — here Monte Carlo simulation of random submarine paths to build a prior, not an integral (pp. 199–200)
- [[search-effectiveness-probability]] (new) — probability that the target would have been found if in that cell, given effort applied; later LEP (pp. 191, 195)
- [[bayesian-search-theory]] (new) — search by prior map plus effectiveness data. Failure in one cell raises the others, and Richardson says it is generally best to search the highest-probability cell next (pp. 189, 201)
- [[kalman-filter]] (new) — a procedure that adds new observations without full recalculation. The author says it can be derived from Bayes' rule (p. 205)

## Canonical instances
- [[palomares-h-bomb-search]] — a prior and coverage numbers, but no updating during the search. The author names Orts and *Alvin* as the heroes (pp. 185–195)
- [[uss-scorpion-search]] — first full prior-to-update Bayesian search, using a Monte Carlo prior (pp. 197–203)
- [[suez-canal-clearance]] — conjugate priors for the unknown number of bombs (p. 203)
- [[coast-guard-sar-system]] — scenario weighting, Monte Carlo and a filter for drifting boats (pp. 204–206)
- [[soviet-sub-tracking-1976]] — a Bayesian estimate of 55% that the sub had not yet passed (pp. 207–208)

## Bridges (candidates)
- [structural-analogy] Scenario-weighted prior map with simulated paths ↔ bayesian: prior predictive simulation — both generate possible worlds from assumptions before data arrive.
- [same-math] Updating after a failed search ↔ bayesian: conditioning on "not detected" — the likelihood is $1-\text{SEP}$ for the searched cell and 1 elsewhere (our reading, not printed).
- [same-math] Kalman filter as derived from Bayes' rule (Aoki 1967) ↔ bayesian: sequential updating — the author says it can be derived directly from Bayes' rule (p. 205).
- [structural-analogy] Expert pooling on scenarios ↔ bayesian: elicited priors and hierarchical pooling of opinions — loose analogy.

## Questions this raises
- Why did commanders resist updating but accept SEPs? Is coverage reporting easier to explain than priors and posteriors?
- How sensitive is the Scorpion map to the nine scenario weights and to the equal-direction assumption?
- How was the sensor-effectiveness number actually computed, and how did uncertainty about it enter the update?
- How would one test whether subjective expert weights are better than uniform ones in past searches?

## Reading notes
- Printed page = pdf page − 15. The unit covers printed pp. 182–210; p. 210 is blank.
- The text layer was clean, with ligature problems only (e.g. "ﬁ").
- The text has the spelling "Moony" once for Mooney (p. 192).
- The chapter gives no formulas. The toy example's update formula is ours.
- The instruction on p. 190 to pay attention to Richardson is Washington's message as Guest understood it, not Guest's own words.
- The text gives nine scenarios for *Scorpion* on p. 198, but Richardson's description on p. 199 speaks of ten.
