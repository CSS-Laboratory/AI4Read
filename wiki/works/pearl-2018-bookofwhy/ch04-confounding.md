---
id: pearl-2018-bookofwhy/ch04-confounding
work: pearl-2018-bookofwhy
unit: "Chapter 4 — Confounding and Deconfounding: Or, Slaying the Lurking Variable"
pages: "pdf 130–156 (printed page numbers not given)"
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 15
pipeline_version: 0.1
---
# Confounding and Deconfounding: Or, Slaying the Lurking Variable

## L0 — One line
Pearl argues that confounding is a causal idea, defined as P(Y | X) ≠ P(Y | do(X)), so the back-door criterion on a causal diagram, not a statistical test or a randomized trial, tells you what to adjust for.

## L1 — The gist (≤ 120 words)
How can we separate a true causal effect from a spurious association? Pearl says confounding is any discrepancy between P(Y | X) and P(Y | do(X)). Randomized trials remove confounding by simulating the intervention world. Older statistical definitions (correlated with X and Y; "adjusted differs from crude") are shown to fail. A causal diagram gives a mechanical rule instead: block every back-door path from X to Y without adjusting for descendants of X. Adjusting for everything measurable can create bias, for example by opening a collider or blocking a mediator. If the diagram is defensible, an observational study can give a "provisional" causal answer.

**Prerequisites:** causal diagrams (arrows, forks, chains, colliders); conditional probability; the do-operator idea from Chapters 1 and 3.

## L2 — Key ideas (5–10 bullets)
- Confounding means a variable influences both who gets the treatment and the outcome. In a diagram, the basic case is the fork X ← Z → Y (Pearl says a more universal definition comes later). It "mixes" the true effect with a spurious association (pdf 132–133).
- Confounding is a rung-two (causal) concept, not a statistical one. It is defined as P(Y | X) ≠ P(Y | do(X)) (pdf 134, 143).
- RCTs work because randomization erases all arrows into the treatment, including ones from unknown or unmeasurable causes. This simulates the intervention world (Model 2) (pdf 141–142).
- Pearl says there is no need to treat RCTs as the "gold standard" that other methods must emulate; their legitimacy derives from more basic principles. Observational studies can give "provisional causality" that depends on the diagram's assumptions (pdf 134, 142).
- Older definitions of confounding (three-part classical test, noncollapsibility) are wrong. Greenland and Robins's counterfactual "exchangeability" fixed the definition but could not be applied in practice (pdf 144–148).
- Back-door criterion: block every back-door path, and do not adjust for descendants of X. This turns deconfounding into a maze-like puzzle (pdf 148–150).
- Controlling for everything is misguided. Adjusting can open a collider path (M-bias) or block a mediator. In the M-bias example, a variable like B is not a confounder unless you control for it (pdf 151–152).
- Worked examples (Games 1–5, Forbes's model) show sufficient adjustment sets, sometimes empty (pdf 150–154).

## L3 — Walkthrough

### Opening: Daniel's experiment (pdf 130–134)
- Daniel proposes a ten-day trial: some boys eat vegetables, others eat the king's meat and wine. Pearl reads this as the logic of a **controlled experiment**. You compare a treated group with a control group that is identical in all relevant ways. This stands in for the unobservable comparison of one person under both treatments (pdf 131).
- Two good features: it compares groups (a friend's experience assumes you are similar to the friend in everything relevant), and it is **prospective**, meaning the groups are chosen in advance. Infomercial testimonials come from people already selected for success (pdf 132).
- Missing: **confounding bias**. If Daniel's group were healthier at the start, their good looks might not come from the diet. Confounding occurs when a variable influences both selection for treatment and the outcome (pdf 132).
- The fork Z at the centre of X ← Z → Y (Fig. 4.1) is the basic confounder. "Confounding" originally meant "mixing": the true effect X → Y is mixed with the spurious correlation made by the fork (pdf 133).
- Without data on Z (for example age) you cannot separate the effects. With data, you compare treated and control groups within each age group. Then you average the effects, weighting each group by its share of the target population. This is "adjusting for Z" or "controlling for Z" (pdf 133).
- Pearl's claims about practice:
  - Statisticians overrate adjustment. They control for everything measurable, even variables they should not control for (Klein is quoted on "overcontrolling"). The Causal Revolution ends this confusion (pdf 133).
  - Statisticians also underrate adjustment. If a sufficient set of deconfounders is found, measured and adjusted for, you may say you computed the causal effect, provided the diagram is scientifically defensible (pdf 133–134).
- Pearl says Fisher "was exactly right, but not for exactly the right reasons". Fisher's followers had no language to write down the causal effect, so they could not prove what the RCT delivers (pdf 134).
- Shift of emphasis: from **confounders** (cause the problem) to **deconfounders** (cure it). The sets may overlap but need not. With data on a sufficient set of deconfounders, ignoring some or all confounders does not matter (pdf 134).
- The back-door criterion, introduced later, picks out the deconfounders. Pearl says Chapter 7 will show cases where confounding can be controlled without data on a sufficient set of deconfounders, using different adjustment formulas (pdf 134–135).
- Pearl says there is now an almost universal consensus, at least among epidemiologists, philosophers and social scientists, that (1) confounding needs and has a causal solution and (2) causal diagrams provide a complete and systematic way of finding it (pdf 135).

*Intuition note:* A confounder is a common cause, sometimes known and sometimes only a "lurking" suspect, that makes two things move together. Adjusting means comparing like with like inside each level of that cause. Which variables to adjust for is a causal question, not a data question.

### The chilling fear of confounding (pdf 135–137)
- Honolulu Heart Program study (Abbott et al.): 707 men, 12 years. 43% of casual walkers (under 1 mile a day) died, against 21.5% of intense walkers (over 2 miles a day) (pdf 135).
- The authors adjusted for age, physical condition, alcohol, diet and others. The age-adjusted death rates were 41% versus 24% (pdf 136). Fig. 4.2: Age is a fork between Walking and Mortality (pdf 136).
- **Abbott's team** wrote that the effects of intentional efforts to walk more "cannot be addressed in our study" (pdf 136). **Pearl replies:** he asserts that the general belief that an observational study can never illuminate a causal claim is overexaggerated. Why adjust at all, if not to expose the causal part? If we believe the team identified all the important confounders, we must also believe that intentional walking tends to prolong life (at least in Japanese males) (pdf 136–137).
- The conclusion is provisional: it assumes no other major confounder. That is valuable, because it tells precisely what kind of uncertainty remains and guides future studies (pdf 137).

### The skillful interrogation of Nature: why RCTs work (pdf 137–143)
- Joan Fisher Box writes that Nature responds to the question as set out in the field, not necessarily to the one in the experimenter's mind; Pearl likes this as the image of Nature as a genie. Fertilizer on two halves of a field mixes treatment effects with soil fertility, drainage and other variables (pdf 137–138).
- Pearl's reading: the answer to the question we want exists in nature. do(X = x) comes first, and randomization is only a man-made means of eliciting it. He compares randomization to a thermometer's gauge, which is not the temperature itself (pdf 138).
- Fisher first used structured layouts (grids, Latin squares, Fig. 4.3). Around 1923–24 he began to realize that the only design the genie could not defeat was a random one (pdf 138–139). Over many repetitions with fresh random assignments, most of the time the fertilizer lands on a representative set of subplots, since the field's fertility stays fixed (pdf 139).
- His colleagues were dismayed at the idea. Fisher held that an uncertain answer to the right question beats a certain answer to the wrong one. The uncertainty can be quantified because it comes from the known randomization procedure (pdf 140).
- Two benefits: (1) removes confounder bias; (2) lets the researcher quantify uncertainty. **Stigler's view (historian):** the second was Fisher's main reason. Pearl adds that Fisher's understanding of deconfounding was purely intuitive because he lacked a mathematical notation (pdf 140).
- Three models:
  - **Model 1** (Fig. 4.4): soil fertility, texture, drainage, microflora and other factors point into both Fertilizer and Yield. The query is P(yield | do(fertilizer = 1)) (pdf 140). Naive designs bring in confounders such as Drainage or Weather (pdf 141).
  - **Model 2** (Fig. 4.5): do() erases all arrows into Fertilizer and sets it to 1. This is the world we want to know about (pdf 141).
  - **Model 3** (Fig. 4.6): Fertilizer is set by a random Card with no arrow Card → Yield. Fertilizer and Yield are unconfounded (no common cause), so seeing and doing Fertilizer = 1 give the same result (pdf 141).
- Punch line: randomization simulates Model 2. It disables all old confounders and adds none (pdf 141–142). It fails if the experimenter chooses by judgment or if subjects "know" their card, hence double blinding (pdf 142).
- Second punch line: other ways to simulate Model 2 exist, such as measuring and adjusting for confounders. Randomization's advantage is that it severs every incoming link, including unknown or unmeasurable ones. In a nonrandomized study a confounder may be missed (pdf 142).
- RCTs are still preferred "all things being equal", like safety nets. But intervention may be impossible (obesity), unethical (smoking), or the volunteers may be unrepresentative (pdf 142). Observational estimates are "provisional causality" and are not second-class: they happen in the natural habitat of the target population (pdf 142–143).

*Intuition note:* A random draw (Fisher's deck of cards) is not influenced by soil or other plot features. So it cuts every link from "why this plot" into the treatment. What remains is a comparison without confounders, though still subject to chance.

### The new paradigm of confounding (pdf 143–148)
- Greenland and Robins (1986) noted little consistency among definitions of confounding (pdf 143).
- **Pearl's definition:** confounding is anything leading to P(Y | X) ≠ P(Y | do(X)). It is not a statistical notion, because it is the gap between the causal effect we want and what statistics measures (pdf 143–144).
- The old ideas, incomparability and a lurking third variable, resisted formalization. How do we tell relevant attributes (age) from irrelevant ones (alphabetical order of name)? Should a confounder be a common cause, or merely correlated with X and Y? (pdf 144). The diagram answers by checking which variables produce a discrepancy between P(X | Y) and P(X | do(Y)) (as printed; see Reading notes) (pdf 144).
- Surrogate definitions:
  - **Declarative (wrong):** a confounder is any variable correlated with both X and Y (pdf 144).
  - **Procedural, "noncollapsibility" (Hernberg 1996):** compare crude and adjusted relative risk. A difference means confounding, so use the adjusted estimate. No difference means the crude one is preferred. Pearl says this misguided a century of researchers (pdf 144–145).
  - **Classical epidemiological definition:** Z is a confounder if (1) Z is associated with X in the population, (2) Z is associated with Y among the unexposed, and (3) Z is not on the causal path from X to Y. Condition 3 was added later. Conditions 1–2 are purely statistical. Pearl reads Simpson's "among the unexposed" as apparently a way to discount X's effect on Y, since statistical vocabulary had no word "effect" and paths were forbidden (pdf 145).
- Two failures (the figures are missing from the text layer; described from the prose):
  - (i) Z is a **mediator**, a variable that carries X's effect on Y. It meets conditions 1–2, but controlling for it blocks X's effect and wrongly suggests X has no effect (pdf 145–146).
  - (ii) Z is a proxy for a mediator M. Controlling for Z lets some effect leak through, but is still a mistake. The bias may be smaller than when controlling for M, but it remains (pdf 146).
- Cox (1958) advised controlling for Z only with a "strong prior reason" to believe X does not affect it. Pearl calls this a causal assumption. Pearl says each of conditions 1–2 can be shown to be both unnecessary and insufficient, a conclusion Greenland and Robins drew in 1986 (pdf 146).
- **Exchangeability (Greenland–Robins)** is a counterfactual definition. Imagine what would have happened to the treated group without treatment, and judge whether outcomes would match those of the actually untreated. Only then can we say no confounding exists (pdf 146–147). It builds on Rubin's 1974 potential outcomes (pdf 147).
- Four response types (Table 4.1; treatment = flu vaccine, outcome = flu) (pdf 147–148):

| Group | Share | Flu if vaccinated | Flu if not |
|---|---|---|---|
| Doomed | d | Flu | Flu |
| Causative | c | Flu | No flu |
| Preventive | p | No flu | Flu |
| Immune | i | No flu | No flu |

- Exchangeability means the proportions d, c, p, i are the same in treated and control groups. The groups may differ in many other ways. Only equality of d, c, p, i decides exchangeability. This reduces the problem to two sets of four proportions (pdf 147).
- Using it, Greenland and Robins showed the statistical definitions give wrong answers. A variable can pass the three-part test and still increase bias if adjusted for (pdf 148).
- Drawback: the "stickers on the forehead" do not exist, so we do not even have counts of d, c, p, i. The back-door criterion is the practical test (pdf 148).

### The do-operator and the back-door criterion (pdf 148–154)
- Pearl likes to think of the links as pipes that convey information, in both causal and noncausal directions. Noncausal paths are the source of confounding. do() erases arrows into X and so stops noncausal flow. Randomization does the same, and so does adjusting for the right variables (pdf 148–149).
- Junction rules (pdf 149):
  - (a) Chain A → B → C: controlling for B blocks flow.
  - (b) Fork A ← B → C: controlling for B blocks flow.
  - (c) Collider A → B ← C: A and C start independent. Controlling for B opens the pipe (explain-away effect).
  - (d) Controlling for a descendant or proxy is "partial" control of the variable itself. For a mediator's descendant it partly closes the pipe. For a collider's descendant it partly opens it.
- A long path is blocked if any single junction on it is blocked. In the chain A…J example (arrow directions not shown in the text layer), colliders at D and G block the path with no control. Controlling for D and G would open it (pdf 149).
- **Back-door criterion:** a back-door path is any path from X to Y that starts with an arrow into X. X and Y are deconfounded if we block every back-door path. If we do so by controlling for a set Z, no member of Z may be a descendant of X on a causal path, which would close the causal path (pdf 149–150).
- Games (arrows reconstructed from the text; figures not in the text layer):
  - **Game 1:** X has no incoming arrows, so no back-door path. Nothing to control. B is a descendant of A (X → A → B). Some researchers would still call B a confounder, since it passes the three-part test. It does not pass the back-door criterion, and controlling for it leads to disaster (pdf 150).
  - **Game 2:** one back-door path, X ← A → B ← D → E → Y, blocked by the collider at B. Control for nothing. Controlling for B or C would open it. Controlling for A or D recloses it. Different valid strategies give the same result, given a correct model and enough data (pdf 150–151).
  - **Game 3:** back-door path X ← B → Y. B must be controlled. If B is unobservable, only an RCT estimates the effect. Controlling for A, a proxy for B, only partly removes the bias and adds collider bias (pdf 151).
  - **Game 4 (M-bias):** X ← A → B ← C → Y. The back-door path is blocked at B, so control for nothing. B is associated with X and with Y via a path not through X, so it passes the classical test. It is not a confounder unless you control for it: "B only becomes a confounder when you control for it!" (pdf 151–152). Seat-belt usage may be such a B (smoking X, lung disease Y). Controlling for B plus A or C is fine, but A and C are attitudes and unlikely to be observable (pdf 152).
  - **Game 5:** Game 4 with a second back-door path, X ← B ← C → Y (reconstructed). Controlling for B opens X–A–B–C–Y, so also control A or C. Controlling for C alone closes the second path without affecting the other (pdf 152).
- Sources: Games 1–3 are from Weinberg (1993), who verified exchangeability by arithmetic. She studied smoking (X) and miscarriage (Y). In Game 1, adjusting for previous miscarriages (B) underestimates smoking's effect. In Game 2, adjusting for prior miscarriages (C) is a bad idea unless you also adjust for first-pregnancy smoking (A) (pdf 152–153). Games 4–5 are from Forbes et al. (2014), smoking and adult asthma: A = parental smoking, B = childhood asthma (collider), C = unobservable predisposition (pdf 153).
- **Forbes's full model (Fig. 4.7):** Game 5 is embedded. We must control for A and B, or for C, and C is unobservable. New variables: D parental asthma, E chronic bronchitis, F sex, G socioeconomic status. Control E, F, G, not D. A sufficient set is {A, B, E, F, G} (pdf 154).
- Forbes found a small, statistically insignificant association in the raw data, and an even smaller one after adjustment (pdf 154). Pearl calls the confounding problem solved and "a quiet revolution" (pdf 154–155).

*Intuition note:* To deconfound, close every route that goes into X from behind, and do not touch routes that come out of X. Adding controls can open closed routes (colliders) or close the real one (mediators), so more controls are not safer.

## Toy example (ours, not from the text)
Z = age (half young, half old). Recovery probabilities: young 0.8 with drug, 0.7 without; old 0.4 with drug, 0.3 without. Assignment is confounded: of 1000 young, 900 get the drug; of 1000 old, 100 get it.
- Crude, treated: (900 × 0.8 + 100 × 0.4) / 1000 = (720 + 40) / 1000 = 0.76.
- Crude, untreated: (100 × 0.7 + 900 × 0.3) / 1000 = (70 + 270) / 1000 = 0.34. Crude difference = 0.42.
- Adjusted (weight each age group by its 50% share, as on pdf 133): do(drug) = 0.5 × 0.8 + 0.5 × 0.4 = 0.60. do(no drug) = 0.5 × 0.7 + 0.5 × 0.3 = 0.50. Causal effect = 0.10.
- The crude gap (0.42) mixes the true +0.10 with the spurious age link: young people are both more often treated and more likely to recover. If Z were a mediator instead, the same stratification would wrongly show no effect (pdf 145–146).

## Concepts
- [[confounding]] (new) — anything making P(Y | X) differ from P(Y | do(X)); originally "mixing" of true and spurious effects (pdf 133, 143)
- [[deconfounder]] (new) — a set of variables that blocks all back-door paths; may differ from the set of confounders (pdf 134, 150)
- [[back-door-front-door-criterion]] — block every back-door path (paths starting with an arrow into X) without adjusting for descendants of X (pdf 149–150)
- [[do-operator]] — erases arrows into a variable and sets it; the query P(Y | do(X)) (pdf 140–141)
- [[fork-chain-collider]] — three junction types; controlling for a collider opens its path (pdf 149)
- [[causal-dag]] — diagram used to find confounders and sufficient adjustment sets (pdf 132, 149)
- [[ladder-of-causation]] — confounding sits on rung two; counterfactuals on rung three (pdf 134, 146)
- [[potential-outcomes]] — Rubin's counterfactual variables, both treatments for each person (pdf 147)
- [[exchangeability]] — here the Greenland–Robins counterfactual sense: equal shares of doomed, causative, preventive, immune in both groups (pdf 146–147)
- [[randomized-controlled-trial]] (new) — random assignment simulates Model 2, removing all incoming arrows to X (pdf 141–142)
- [[mediator]] (new) — variable on the causal path from X to Y; controlling for it blocks the effect (pdf 145–146)
- [[m-bias]] (new) — adjusting for a collider (the middle of the M) opens a spurious path; the collider becomes a confounder only when controlled (pdf 151–152)
- [[noncollapsibility-test]] (new) — a procedural, wrong definition: confounding if adjusted and crude estimates differ (pdf 144–145)
- [[overcontrolling]] (new) — controlling for many variables, including ones that should not be controlled for (pdf 133)

## Canonical instances
- [[daniel-diet-experiment]] — prospective controlled trial; confounding by baseline health (pdf 131–132)
- [[honolulu-walking-study]] — observational study with confounder adjustment and "provisional" causal reading (pdf 135–137)
- [[fisher-fertilizer-field]] — why randomization asks Nature the right question; Models 1–3 (pdf 138–142)
- [[flu-vaccine-response-types]] — four response types behind exchangeability (pdf 147–148)
- [[weinberg-smoking-miscarriage]] — adjusting for prior miscarriages biases estimates (pdf 152–153)
- [[forbes-smoking-asthma]] — M-graph in practice; adjustment set A, B, E, F, G (pdf 153–154)
- [[seat-belt-m-bias]] — seat-belt use as a collider in Pearl's example model of smoking and lung disease (pdf 152)

## Bridges (candidates)
- [structural-analogy] Randomization erases arrows into X ↔ do-operator: the graph surgery in Model 3 mimics the intervention in Model 2 (pdf 141).
- [structural-analogy] Adjustment formula (weighted average over strata of Z) ↔ Bayesian marginalization: averaging a conditional over a distribution of Z. The text does not state this link.
- [metaphor] Pipes carrying information ↔ information flow and conditional independence in probabilistic graphical models (canon link; not stated in this unit).

## Questions this raises
- If I measure a proxy for an unobserved confounder, how much bias remains, and can it be bounded (Game 3)?
- How sure can we be that a diagram is right, given that its assumptions "advertise" provisional causality?
- What adjustment formulas work when no sufficient deconfounder set is measured (promised for Chapter 7)?
- Is the back-door criterion complete, or are there deconfounding strategies it misses?

## Reading notes
- Printed page numbers are not given in the extracted pages, so all citations are by pdf page.
- Several arrow symbols are lost in the text layer, and the Game 1–5 figures and the two "classical definition" example diagrams (i) and (ii) on pdf 145, were blank in the text layer, and no page images of pdf 145 or pdf 150–152 were supplied. Arrow directions for Games 1–5 are reconstructed from Pearl's prose, including collider and path descriptions. They are marked as such.
- The text layer of pdf 144 prints "P(X | Y) and P(X | do(Y))" (no page image of pdf 144 was supplied). Given the surrounding definition P(Y | X) vs P(Y | do(X)), this looks like a swapped-letter misprint. I kept it as printed.
- pdf 156 holds only an illustration caption ("Abe and Yak"). pdf 155 is the chapter's last text page.
- The unit has no exercises.
