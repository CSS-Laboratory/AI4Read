---
id: pearl-2018-bookofwhy/ch08-counterfactuals
work: pearl-2018-bookofwhy
unit: "Chapter 8 — Counterfactuals: Mining Worlds That Could Have Been"
pages: "pdf 236–272 (printed page numbers not visible)"
fields: [bayesian]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Counterfactuals: Mining Worlds That Could Have Been

## L0 — One line
Given a structural causal model, a counterfactual about a particular individual or event can be computed in three steps (abduction, action, prediction), which lets us ask about blame, necessity and sufficiency in law and climate science.

## L1 — The gist (≤ 120 words)
Rung-two tools describe effects on populations. They cannot say what would have happened to this person or this event. Pearl asks how data plus a causal model can answer such "what if" questions. His answer is the structural causal model (SCM). Each variable is a function of its parents plus unobserved factors, and counterfactuals are computed by abduction, action and prediction. He argues that potential-outcome imputation (matching, regression) cannot answer rung-three questions from data alone. The same machinery defines the probability of necessity (PN) and of sufficiency (PS). These are used for legal "but-for" causation and for attributing heat waves to climate change. Blame, credit and responsibility are counterfactual notions.

**Prerequisites:** do-operator, back-door paths and d-separation from earlier chapters; conditional probability; reading simple linear equations.

## L2 — Key ideas
- Counterfactuals sit on rung three (the top rung of the Ladder of Causation, the rung of imagined alternatives). Hume's second definition of cause is one, and the text says it differs completely from his regularity definition (pdf 242–243).
- Lewis's idea of the most similar possible world is reinterpreted by Pearl as the minimal alteration of a shared causal model. Pearl thinks it very likely that structural models are the brain's economical code for this. He says the stronger assertion that causal diagrams are close to how our brains represent counterfactuals must remain unproven for now (pdf 244–245).
- In the Rubin model a potential outcome $Y_x(u)$, the value $Y$ would have taken for individual $u$ had $X$ been $x$, is defined for an individual. Table 8.1 shows only one outcome per person, and Pearl argues that filling the blanks by matching or regression is data-driven and cannot reach rung three (pdf 246–250).
- In an SCM each variable is a function of its parents and an exogenous term (an unobserved factor outside the model). A counterfactual follows from three steps: abduction (infer the individual's hidden factors from what we saw), action (use the do-operator: force the variable to a value and cut the arrows into it) and prediction (recompute the outcome). This is summed up as $Y_x(u)=Y_{M_x}(u)$ (pdf 252–255).
- Ignorability (Rubin's assumption that the potential outcome is independent of the treatment received, given confounders $Z$) is hard to judge mentally. The diagram gives a check, and d-separation (a diagram rule that tells which variables should be independent in the data) makes the model testable, while a potential-outcome model cannot be tested this way (pdf 255–258).
- Necessity and sufficiency are defined as probabilities, $PN=P(Y_{X=0}=0\mid X=1,Y=1)$ and $PS=P(Y_{X=1}=1\mid X=0,Y=0)$. Hindsight (knowing what actually happened) separates counterfactuals from interventions (pdf 260–262).
- Under no confounding (no common cause) and monotonicity (the treatment never has the opposite effect), the climate fraction of attributable risk (FAR, a data-based measure of how much of the risk is due to climate change) equals PN. For the 2003 heat wave, PN = 0.9 and PS ≈ 0.0072 (pdf 265–267).

## L3 — Walkthrough

### Opening (pdf 236–238)
- Rung-two tools (randomized trials, back-door and front-door adjustment, instrumental variables, do-calculus) give effects on populations or a typical individual (pdf 236).
- Missing is *personalized* causation. Pearl's example: Uncle Joe, who smoked for thirty years and died, can never be observed in the alternate world where he did not smoke for thirty years. Blame, regret and credit need a comparison with what would have happened (pdf 237).
- The chapter has four aims:
  - show counterfactuals inside SCMs;
  - compare them with Neyman–Rubin potential outcomes;
  - treat "but-for" causation in law;
  - treat climate attribution (pdf 237–238).
- Counterfactual analysis needs a slight addition to our vocabulary, three kinds of cause: necessary (same as but-for), sufficient, and necessary-and-sufficient. Example statements a climate scientist could make: a 90 percent probability that man-made climate change was a necessary cause of this heat wave (attribution), and an 80 percent probability that climate change will be sufficient to produce a heat wave this strong at least once every 50 years (policy) (pdf 238).

### From Thucydides and Abraham to Hume and Lewis (pdf 238–246)
- **Thucydides** explains the 426 BC tsunami at Orobiae by an earthquake, without gods. His last sentence, that without an earthquake he does not see how such an accident could happen, is but-for causation. Pearl says it promotes the earthquake from an antecedent to an actual cause (pdf 238–239).
- **Abraham** bargains with God over Sodom (fifty righteous, then forty-five, … ten). Pearl reads this as Abraham seeking the law behind collective punishment, a dose-response or threshold function. A complete causal model needs it (pdf 239–240).
- **Aristotle's** taxonomy of causes (material, formal, efficient, final) contains no counterfactual statement (pdf 240).
- **Hume** gave two definitions. 1739 (*Treatise*): the "regularity" definition, in which flame and heat are constantly conjoined. Pearl says Hume here seems happy to treat causation as merely a species of correlation, cutting off rungs two and three so that only rung one remains (pdf 240–241). 1748 (*Enquiry*): adds "if the first object had not been, the second never had existed". Hume passes the two off as one ("in other words"). Pearl says the second is completely different and lies on rung three because it explicitly invokes a counterfactual: regularities can be observed, but counterfactuals can only be imagined (pdf 242–243).
- Under regularity the rooster's crow would cause sunrise. The counterfactual definition rejects it, since the sun would rise anyway if the rooster stayed silent (pdf 242–243).
- Pearl's view: Hume defined cause by counterfactual because the counterfactual is less ambiguous. It asks only for a mental test: imagine a world without the earthquake and ask whether a tsunami is there (pdf 243).
- Philosophers mostly ignored the second definition in the 19th and 20th centuries and tried to rescue regularity through probabilistic causation (pdf 243).
- **Lewis (1973)** proposed reading "A has caused B" as "B would not have occurred if not for A". **Lewis's view:** a counterfactual is true if the *most similar* possible world where the antecedent holds contains the outcome. Example: Joe's aspirin and headache (pdf 243–244).
- **Pearl's reading:** we need not believe such worlds exist. To explain what people mean by "A causes B", we need only postulate that people can generate alternative worlds in their heads and judge closeness coherently, so as to form a consensus. That is possible because we share a mental causal model. Closeness can then be judged by how much we must take apart and perturb the shared model to meet the contrary-to-fact condition (pdf 244).
- In structural models, "had $X$ been $x$" is handled like $do(X=x)$, by deleting arrows or equations. This is the minimal alteration needed to make $X=x$, so it is compatible with Lewis's "most similar world" (pdf 244–245).
- Pearl's claim: structural models may solve the "representation problem" (how a brain stores and searches so many worlds). He gives two reasons:
  - SCMs are a shortcut that works, and he knows of no competitor;
  - they descend from Bayesian networks, which were modeled on Rumelhart's message passing in the brain.
  
  Philosophers tended to see structural models as just one implementation of Lewis's possible-worlds logic. Pearl suggests they are much more, since logic void of representation is metaphysics. He says causal diagrams must be close to the way our brains represent counterfactuals, but that this assertion must remain unproven for the time being (pdf 245).
- He entered counterfactual analysis in 1994 with Alex Balke. The upshot, he says, is that counterfactuals have ceased to be mystical (pdf 245–246).

> **Intuition note.** Hume's second definition turns "A caused B" into a simple test: remove A in imagination and see if B remains. Pearl's contribution is a mechanical way to run that test, namely editing a causal model.

### Potential outcomes, structural equations, and the algorithmization of counterfactuals (pdf 246–255)
**Rubin's potential outcomes.**
- Rubin began publishing on potential outcomes in the mid-1970s. Pearl credits him with breaking the long silence about causality in statistics and giving a flexible language for causal questions at both population and individual levels (pdf 246). The first scientific appearance was in Neyman's 1923 master's thesis (the unknown potential yield of a given seed variety on a plot), untranslated until 1990 (pdf 246–247).
- Definition: $Y_x(u)$, or $Y_{X=x}(u)$, is the value that $Y$ would have taken for individual $u$ had $X$ been assigned the value $x$ (pdf 246).
- Pearl stresses the assumption: $Y$ definitely would have taken some value, with as much objective reality as the value it did take. It is defined for an individual, not a population (pdf 246).
- The Fisher–Neyman quarrel (1934–35) is told in a few pages. Pearl says Fisher's refusal of the notation helped lead him into the Mediation Fallacy (Chapter 9) (pdf 247–248).

**Table 8.1 (fictitious data, pdf 249).** Columns $EX(u)$, $ED(u)$, $S_0(u)$, $S_1(u)$, $S_2(u)$. $ED=0,1,2$ means high school, college, graduate degree.

| Employee | EX | ED | $S_0$ | $S_1$ | $S_2$ |
|---|---|---|---|---|---|
| Alice | 6 | 0 | 81,000 | ? | ? |
| Bert | 9 | 1 | ? | 92,500 | ? |
| Caroline | 9 | 2 | ? | ? | 97,000 |
| David | 8 | 1 | ? | 91,000 | ? |
| Ernest | 12 | 1 | ? | 100,000 | ? |
| Frances | 13 | 0 | 97,000 | ? | ? |

- Question: what is $S_1(\text{Alice})$? Only one potential outcome per person is observed. Holland gave this fact a name that stuck, the fundamental problem of causal inference (pdf 248).
- **Pearl disagrees.** The table has no causal information, and he says that treating the task as missing-data imputation can be terribly misleading (pdf 249).
- **Matching:** Bert and Caroline match on experience, so one would fill in Bert's $S_2$ as $97{,}000$ and Caroline's $S_1$ as $92{,}500$ (pdf 249).
- **Regression** gives
$$S = \$65{,}000 + 2{,}500\times EX + 5{,}000\times ED \tag{8.1}$$
  and the analyst estimates Alice's college salary as $65{,}000+2{,}500\times 6+5{,}000\times 1=\$85{,}000$ (pdf 250).
- Pearl's criticism: both methods are data driven. No method based only on data (rung one) can answer rung-three questions (pdf 250).
- **Why matching fails.** Experience likely depends on Education, since each extra degree took years. If Caroline had only one degree she could have used the extra time to gain more experience, giving her equal education and more experience than Bert. So $S_1(\text{Caroline})>S_1(\text{Bert})$, contrary to naive matching. Once Education affects Experience, matching on Experience creates a mismatch (pdf 250–251).

**The SCM approach (pdf 251–254).**
- Draw Figure 8.3 first: $ED\to EX$, $ED\to S$, $EX\to S$. If instead $EX$ caused $ED$, Experience would be a confounder and matching would be fine. With $ED\to EX$, Experience is a mediator. Pearl calls mistaking a mediator for a confounder one of the deadliest sins in causal inference (pdf 251).
- "Listens to" means a function: $S=f_S(EX,ED,U_S)$, where $U_S$ stands for unobserved variables. This is the difference from Bayesian networks or regressions (pdf 252).
- Same linear fit, now structural:
$$S = \$65{,}000 + 2{,}500\times EX + 5{,}000\times ED + U_S \tag{8.2}$$
$$EX = 10 - 4\times ED + U_{EX} \tag{8.3}$$
- The formal likeness of 8.1 and 8.2 is "profoundly deceptive". Regression is "cause blind" (Galton, Chapter 2), and one could regress in any order. A structural equation commits the author to who listens to whom. The absence of an equation $ED=f_{ED}(EX,S,U_{ED})$ says $ED$ is oblivious to $EX$ and $S$. This commitment is what lets structural equations support counterfactuals (pdf 252).
- Eq. 8.3 has no $S$ term although $S$ and $EX$ are likely correlated. It says that experience is unaffected by current salary (pdf 252–253).

**The three-step procedure for $S_{ED=1}(\text{Alice})$ (pdf 253).**
1. *Abduction:* use data to estimate $U_S(\text{Alice})$ and $U_{EX}(\text{Alice})$.
2. *Action:* use the do-operator to set $ED(\text{Alice})=1$, erasing arrows into $ED$. Here there are none, so the step is trivial. In general it cannot be skipped, because it affects Step 3: variables that might have affected the outcome through the intervened variable are no longer allowed to do so.
3. *Prediction:* recompute with the modified model and updated exogenous values.

Numbers (pdf 253):
- Abduction: from $EX=6$, $ED=0$, Eq. 8.3 gives $U_{EX}=6-10=-4$, and Eq. 8.2 gives $U_S=\$1{,}000$.
- Prediction, experience: $EX_{ED=1}(\text{Alice})=10-4-4=2$ years.
- Prediction, salary: $S_{ED=1}(\text{Alice})=65{,}000+2{,}500\times2+5{,}000\times1+1{,}000=\$76{,}000$.

> **Intuition note.** First we learn what is special about Alice from what we saw, then we change her education in the model, then we let the change flow through her experience to her salary. Regression's $85{,}000$ ignores that more schooling would have cost her experience.

- $\$76{,}000$ is valid *if the model assumptions are valid*. The result follows logically from the displayed assumptions, while the regression answer, Pearl says, is as whimsical as spurious correlations. Strong results required strong assumptions, namely the diagram and known functions (pdf 254).
- A model is "completely specified" if the functions are known, "partially specified" otherwise. If the model is partially specified, we may only get a probability statement, for example a 10 to 20 percent chance that her salary would be $76{,}000$ (pdf 254).
- **First law of causal inference:** $Y_x(u)=Y_{M_x}(u)$. The potential outcome is computed in the model $M_x$ with arrows into $X$ deleted. All estimable rung-two and rung-three quantities follow from it (pdf 254–255).

### The virtue of seeing your assumptions (pdf 255–260)
- **Rubin's model usually needs three assumptions** (pdf 255–256):
  - *SUTVA*: a unit's treatment effect does not depend on others' treatments.
  - *Consistency*: giving aspirin by experiment gives the same result as taking it freely. In SCMs this is a theorem.
  - *Ignorability*: $Y_x$ is independent of the treatment actually received $X$, given confounders $Z$. Pearl says it is "in essence" Robins and Greenland's exchangeability (Chapter 4).
- Credit to Rubin: ignorability puts nonconfoundedness into probability syntax, so conditional-independence machinery applies. It makes the Rubin model "actually a model"; Table 8.1 alone is not (pdf 256).
- **Pearl's objection:** he says he has yet to find a single person who can explain ignorability in the language of those who must assess it. In the example it asks us to judge whether employees with potential salary $S_1=s$ are as likely to have each education level as those with $S_1=s'$, even before knowing Alice's answer. He calls this circular and "a cognitive nightmare" (pdf 256).
- ED is not ignorable given EX, so matching Bert and Caroline is wrong. Text: their estimates should differ by $S_1(\text{Bert})-S_1(\text{Caroline})=\$5{,}000$ (pdf 256–257; see Reading notes on sign and size).
- **Diagram test (author's statement):** To test whether $X$ is ignorable relative to $Y$ given $Z$, Pearl says we need only check that $Z$ blocks all back-door paths between $X$ and $Y$ and that no member of $Z$ is a descendant of $X$. $EX$ blocks all back-door paths (there are none) but is a descendant of $ED$, so it fails. A Harvard Law Review article had the same story as Figure 8.3 and used matching (pdf 257).
- Pearl reports that Rubin does not consider causal diagrams to aid the drawing of causal inferences. Pearl cites Joffe (2010): ignorability is usually assumed because it justifies available methods, not because it is believed (pdf 257).
- **Testability:** if $Z$ blocks all paths between $X$ and $Y$, then in the data $X$ and $Y$ should be independent given $Z$ (d-separation). A model written only as ignorability statements lacks the machinery to expose its implied independencies, so it cannot be tested this way (pdf 257–258).

**Assumptions in SCMs themselves (pdf 258–260).**
- The *response function* is the key ingredient. In a Bayesian network (causal or not), arrows into $Y$ mean a conditional probability table, which specifies probabilities of $Y$, not a value. In an SCM there are no tables:
$$Y = f_Y(X, A, B, C, \ldots, U_Y) \tag{8.4}$$
  So Abraham's instinct was sound: counterfactual queries need a dose-response relation at each node (pdf 258).
- History: Pearl's 1991 insight was to make $Y$ a function of its parents and let $U_Y$ carry the uncertainty. Cyclic models had resisted probability-table formulations (pdf 258–259).
- SEMs date from the 1950s–60s (Haavelmo, Duncan). Over time economists confused them with regression lines. In 1988 Freedman challenged eleven SEM researchers to explain interventions in an SEM and none could. Pearl says the response-function view restores their original intent (pdf 259).
- Pearl says that from every SEM, no matter how simple, one can compute all counterfactuals among its variables. SCMs, unlike linear SEMs, need not be linear (pdf 259). Linear models cannot represent non-straight dose-response curves, threshold effects or interactions (pdf 259–260).
- Message: with a fully specified SCM we can answer any counterfactual query. With a partial SCM we can in many cases still answer (pdf 260).

### Counterfactuals and the law (pdf 260–264)
- **But-for causation** (Model Penal Code): conduct is the cause if it is an antecedent but for which the result would not have occurred. Indirect causes count: Joe blocks the fire exit and Judy dies in a fire (pdf 260).
- Let $Y=1$ if Judy dies and $X=1$ if the exit was blocked. The probability of necessity is
$$PN = P(Y_{X=0}=0 \mid X=1, Y=1).$$
  It contrasts the actual world ($X=1$) with a counterfactual world ($X=0$) (pdf 260–261).
- **Hindsight** separates rung three from rung two. Without it, $P(Y_{X=0}=0)=P(Y=0\mid do(X=0))$. With hindsight, $P(Y_{X=0}=0\mid X=1,Y=1)\neq P(Y_{X=0}=0\mid X=1)$, because Judy's death is evidence of the fire's strength. The text says this quantity cannot be captured in a do-expression, so counterfactuals lie above interventions (pdf 261).
- Standards of proof are probabilistic. Criminal: "beyond reasonable doubt" (1880; Pearl conjectures a threshold like 99 or 99.9 percent). Civil: "preponderance of evidence", which Pearl reads as more than 50 percent (pdf 261).
- **Falling piano:** the defendant fires and misses, the victim flees under a falling piano. But-for makes him a murderer, which intuition rejects. Lawyers say the piano is the *proximate cause*. Pearl suggests proximate cause is a form of *sufficient cause* (pdf 261–262).
- Probability of sufficiency:
$$PS = P(Y_{X=1}=1 \mid X=0, Y=0).$$
  For the piano, Pearl thinks most of us would agree PS is extremely small. Intuition and the Model Penal Code suggest that if PS is too small, we should not convict the defendant of causing $Y=1$ (pdf 262).
- Firing squad (Chapter 1): either soldier's shot is sufficient and neither is necessary, so $PS=1$ and $PN=0$. If Soldier A misses with probability $p_A$, then $PS_A=1-p_A$. His PN depends on how likely B is to refrain or miss (pdf 262–263).
- **Match vs oxygen:** both are logically equally necessary, yet we blame the match. Pearl's two sentences, that the house would still be standing if only the match had not been struck, and if only the oxygen had not been present, are both true. With the match being the rarer event, Match has high PN and high PS, Oxygen has high PN but low PS. Pearl says this quite possibly explains our preference, but it may be only part of the answer (pdf 263).
- Kahneman and Tversky (1982): people more easily undo rare events and their own actions. PN and PS offer a systematic account, which could teach robots explanations (pdf 263–264).
- Pearl believes PS should enter criminal and tort law, since it concerns foreseeable consequences. A robot explaining a fire must use both: PN alone would rate match and oxygen as equally adequate (pdf 264).

> **Intuition note.** PN asks "was it needed?", PS asks "would it have been enough?". A rare act under our control with high PN and high PS fits the pattern of the culprit we pick, though Pearl says this may be only part of the answer. A common background condition like oxygen has high PN but low PS.

### Necessary causes, sufficient causes, and climate change (pdf 264–268)
- August 2003: the most intense European heat wave in five centuries, about 15,000 deaths blamed in France. Conventional wisdom was that no single event can be attributed to past emissions (pdf 264).
- Allen proposed the *fraction of attributable risk*. With $p_0$ the pre-climate-change and $p_1$ the current probability of such a heat wave, doubling means half the risk is due to climate change, tripling means two-thirds (pdf 264–265). (Added step: these examples fit $FAR=1-p_0/p_1$; the text gives only the examples.)
- FAR is defined from data, so it need not have causal meaning. It equals PN under two assumptions (pdf 265):
  - no confounding between greenhouse gases and heat waves;
  - monotonicity: greenhouse gases never protect against heat waves.
- Estimation uses computer simulation, since only one such heat wave has been observed (pdf 265).
- Allen and Stott (2004) wrote that it is very likely that over half the risk of European summer temperature anomalies exceeding a threshold of 1.6° C is attributable to human influence. Pearl unpacks it as a 90 percent chance that FAR > 50 percent. This is a probability of a probability (uncertainty about climate change plus weather variability). Pearl's causal version: CO$_2$ emissions are very likely to have been a necessary cause of the 2003 heat wave (pdf 265–266).
- Hannart's graph (Figure 8.4): Greenhouse Gases, Natural Forcing and Internal Variability point into Climate Response. Greenhouse Gases is top-level, so no confounding (pdf 266–267).
- Hannart's results for 2003: $PS\approx0.0072$ and $PN=0.9$ (matching Allen and Stott) (pdf 267).
- Over longer time frames PN decreases and PS increases. Hannart computes an 80 percent probability that climate change will be a sufficient cause of another heat wave like 2003 (or worse) in a two-hundred-year period, at today's CO$_2$ levels (pdf 267).
- Pearl says two conflicting studies of Russia's 2010 heat wave probably differed because the groups defined their outcome differently: one apparently based its argument on PN and the other used PS. Any study using PS over a short period sets a high bar for proving causation (pdf 267–268).
- Computer models give counterfactuals easily, with a very complex response function behind Figure 8.4. Pearl considers the response function in this example much more credible than the linear models often chosen only for convenience, with one caveat: climate models have never been verified in a prospective trial over century-long timescales, so they could still contain unknown systematic errors (pdf 268).

### A world of counterfactuals (pdf 268–269)
- Effect of treatment on the treated (ETT) is a counterfactual measure. It asks whether those who get a treatment are those who benefit most. The average causal effect (ACE) averages over the whole population. Shpitser showed when ETT is estimable from data, given a diagram (pdf 268–269).
- Mediation analysis separates the direct effect from the indirect effect through a mediator. Example: Smoking → Tar → Cancer, with the question of tar-free cigarettes. Direct and indirect effects are counterfactual, to be shown in Chapter 9 (pdf 269).

## Toy example (ours, not from the text)
Model for a student: $M=6-2X+U_M$ and $Y=20+3M+5X+U_Y$. Here $X$ is a binary treatment, $M$ a mediator and $Y$ an outcome. Observed for Sam: $X=1$, $M=5$, $Y=45$. Query: what would $Y$ be if $X=0$?
1. *Abduction:* $U_M=M-6+2X=5-6+2=1$. Then $20+3(5)+5(1)=40$, so $U_Y=45-40=5$.
2. *Action:* set $X=0$. No arrows enter $X$, so nothing is erased.
3. *Prediction:* $M_{X=0}=6-0+1=7$, then $Y_{X=0}=20+3(7)+0+5=46$.

Holding the mediator at its observed value $M=5$ (like matching on Experience) gives $20+15+0+5=40$, which is wrong. This is the mistake Pearl describes for Bert and Caroline. Hindsight also matters: with $E[U_Y]=0$ the population value would be $20+3\,E[M_{X=0}]+0$, whereas Sam's own value uses his $U_M=1$, $U_Y=5$.

## Concepts
- [[counterfactual]] (new) — a statement of what would have happened had X been x, about a particular individual or event; rung three (pdf 237, 243).
- [[ladder-of-causation]] — Hume's second definition and PN/PS sit on rung three; hindsight separates it from rung two (pdf 243, 261).
- [[potential-outcomes]] — $Y_x(u)$, value $Y$ would take for unit $u$ had $X=x$; assumed to have objective reality (pdf 246).
- [[fundamental-problem-of-causal-inference]] — Holland's name for one observed potential outcome per unit; Pearl rejects the missing-data framing (pdf 248–249).
- [[structural-causal-model]] — each variable is a function of its parents plus an exogenous $U$; no conditional probability tables (pdf 252, 258).
- [[do-operator]] — used to delete arrows into the variable set counterfactually (pdf 245, 253).
- [[abduction-action-prediction]] (new) — three-step algorithm for computing a counterfactual in an SCM (pdf 253).
- [[assignment-mechanism-ignorability]] — $Y_x$ independent of received $X$ given $Z$; Pearl says it is in essence exchangeability (pdf 255–256).
- [[sutva]] — one unit's effect does not depend on others' treatments (pdf 255).
- [[d-separation]] — blocking implies conditional independence; gives a test of a diagram (pdf 257).
- [[back-door-front-door-criterion]] — diagram test for ignorability: $Z$ blocks back-door paths and has no descendant of $X$ (pdf 257).
- [[probability-of-necessity]] (new) — $PN=P(Y_{X=0}=0\mid X=1,Y=1)$; legal but-for causation (pdf 260–261).
- [[probability-of-sufficiency]] (new) — $PS=P(Y_{X=1}=1\mid X=0,Y=0)$ (pdf 262).
- [[fraction-of-attributable-risk]] (new) — from $p_0$, $p_1$; equals PN under no confounding and monotonicity (pdf 264–265).
- [[mediation-direct-indirect-effect]] (new) — effect transmitted through a mediator vs not; introduced as counterfactual (pdf 269).

## Canonical instances
- [[alice-salary]] — SCM counterfactual $S_{ED=1}(\text{Alice})=\$76{,}000$ vs regression $\$85{,}000$ (pdf 250, 253).
- [[bert-caroline-matching]] — matching on a mediator creates mismatch (pdf 249–251).
- [[firing-squad]] — $PS=1$, $PN=0$ with two sufficient shooters (pdf 262).
- [[judy-fire-escape]] — PN and hindsight (pdf 260–261).
- [[falling-piano]] — but-for vs proximate (sufficient) cause (pdf 261–262).
- [[match-and-oxygen]] — equally necessary, unequal PS (pdf 263).
- [[2003-european-heat-wave]] — FAR, PN = 0.9, PS ≈ 0.0072 (pdf 264–267).
- [[hume-rooster]] — counterfactual definition excludes the crow as cause of sunrise (pdf 242–243).

## Bridges (candidates)
- [structural-analogy] Abduction (infer $U$ from observed data) ↔ Bayesian inference: posterior over latent variables given evidence — here $U$ is solved exactly because functions are deterministic.
- [structural-analogy] Ignorability ↔ exchangeability — the text calls them "in essence" the same, expressed on $Y_x$.
- [metaphor] Lewis's "closest possible world" ↔ minimal edit of a shared model — distance as how much we perturb the model.

## Questions this raises
- If a model is only partially specified, how tight are the probability bounds on PN and PS, and what do we need to assume for them?
- If counterfactuals are unobservable, how can a claimed counterfactual answer (e.g. $\$76{,}000$) ever be tested?
- How would the legal system weigh PN versus PS if both were estimated?
- Why can direct and indirect effects be counterfactual quantities (Chapter 9)?

## Reading notes
- Printed page numbers are not visible in the pages given, so all references use (pdf N). pdf 270 is blank, and pdf 271–272 hold only a photo caption (about Scott's South Pole expedition).
- Possible inconsistency: pdf 251 says $S_1(\text{Caroline})>S_1(\text{Bert})$, but pdf 256–257 writes $S_1(\text{Bert})-S_1(\text{Caroline})=\$5{,}000$. (Added check: Eqs. 8.2–8.3 with Table 8.1 give $S_1(\text{Caroline})=102{,}000$, so $S_1(\text{Caroline})-S_1(\text{Bert})=9{,}500$. Sign and amount differ from the text; I did not resolve this.)
- The 80 percent statement on pdf 238 ("at least once every 50 years") is an illustrative example of what a climate scientist could say. Hannart's computed 80 percent figure on pdf 267 is for a two-hundred-year period. The text does not say these are the same number.
- Table 8.1 and equations were checked against page images; the table text is clear.
- The unit contains no exercises (pdf 257 invites the reader to verify the Bert–Caroline difference).
