---
id: pearl-2018-bookofwhy/ch01-ladder
work: pearl-2018-bookofwhy
unit: Chapter 1 — The Ladder of Causation
pages: pdf 27–57 (printed page numbers not visible)
fields: [bayesian]
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
# The Ladder of Causation

## L0 — One line
Pearl's Ladder of Causation has three rungs (seeing, doing, imagining), each answering questions the lower rungs cannot, and passive data alone, without a causal model, cannot lift a reasoner above the first rung.

## L1 — The gist (≤ 120 words)
Pearl asks what a causal reasoner can do that a pure data-fitter cannot. His answer is a three-rung Ladder of Causation: association (seeing), intervention (doing) and counterfactuals (imagining what would have happened otherwise). Each rung answers queries the lower rungs cannot, so even huge passive data sets cannot answer rung-two or rung-three questions without a causal model. In simple examples (firing squad, vaccination), a causal diagram plus "surgery" (deleting the arrows into a variable that is set) answers queries from all three rungs. Defining "cause" as probability raising fails because it stays on rung one; the do-operator (setting a variable instead of observing it) repairs it.

**Prerequisites:** conditional probability, P(A | B) as a proportion within a subgroup; reading a dots-and-arrows diagram; basic percentages.

## L2 — Key ideas
- Humans move from handling facts to building causal explanations. Pearl treats this as a leap needing a "push", and he links it closely to the ability to imagine non-existent worlds (pdf 28–29).
- Three levels: seeing (association), doing (intervention), imagining (counterfactuals). Each unlocks capabilities that the lower ones lack (pdf 30–31, 34).
- Pearl places present-day machine learning, including deep learning, on rung one. He says it fits functions to observed data and lacks a model of reality (pdf 34–35).
- Interventions cannot be answered from passive data alone. A sufficiently strong causal model can turn rung-one data into rung-two answers (pdf 36–37).
- Mini-Turing test: encode a story, then answer causal questions. Pearl argues that a lookup table cannot do this, while a causal diagram can. Graph surgery handles interventions and counterfactuals (pdf 45–48).
- Vaccination example: raw death counts (99 from vaccine vs 40 from smallpox) mislead, while the counterfactual comparison (3,861 lives saved) does not (pdf 50).
- Pearl argues that a diagram's structure is typically more robust than a probability distribution, and that it carries causal information that probabilities alone do not (pdf 51–52).
- Pearl argues that the idea that X raises the probability of Y cannot be written as P(Y | X) > P(Y), since that inequality can also hold because of a confounder (a common cause). The do-operator version P(Y | do(X)) > P(Y) can capture it (pdf 53–54).

## L3 — Walkthrough

### "In the beginning…" (pdf 27–30)
- Pearl rereads Genesis. God asks "what" and Adam and Eve answer "why". Both think naming causes changes how their act looks (pdf 28).
- Three implications, in Pearl's voice (pdf 28):
  1. Humans realized early that facts are glued together by cause-effect relations.
  2. Causal explanations make up the bulk of knowledge and should be the cornerstone of machine intelligence.
  3. The move from data processors to explanation makers was a leap. "No machine can derive explanations from raw data. It needs a push."
- Humans evolved over 5–6 million years. In roughly the last 50,000 years, the "Cognitive Revolution" appeared, and humans began changing their environment and abilities far faster. Pearl calls this the "super-evolutionary speedup". Eagles have superb eyesight but never invented eyeglasses (pdf 28–29).
- **Harari's view (as reported):** the capacity to imagine non-existent things was the key, because it let larger groups trust each other. Pearl says the link between imagining and causes is almost self-evident. You cannot say Eve caused you to eat unless you can imagine a world where she did not hand you the apple (pdf 29).
- Planning, such as a mammoth hunt, needs a mental model that the planner can hold, consult and manipulate (pdf 29). Figure 1.1 shows several non-deterministic causes (hunters, weather, terrain, etc.) that change the probability of success (pdf 29–30).
- Local change: replace "Hunters = 8" with "Hunters = 9" and reevaluate, without redoing every other factor. This modularity is a key feature of causal models. Causal diagrams are the core of the "causal inference engine" (pdf 30).

**Intuition note.** A causal model is a set of separate pieces. You can change one piece in your head and see what follows. That mental "what if" is what planning needs.

### The three levels of causation (pdf 30–34)
- A causal learner must master at least three distinct levels: seeing, doing and imagining (pdf 30).
  - Seeing: detecting regularities. Many animals do it.
  - Doing: predicting the effects of deliberate changes and choosing among them. Only a few species show elements of it. Intentional tool use may be a sign, but tool users may lack a "theory" of why the tool works.
  - Imagining: it was primarily this third level that prepared us for the agricultural and scientific revolutions.
- Pearl says he cannot prove the evolutionary story, but he can prove mathematically that the three levels differ fundamentally (pdf 30–31). That proof is not given in this chapter.
- The framework follows Turing: classify a system by the queries it can answer. This avoids arguments about what causality "is" (pdf 31).
- Figure 1.2 (pdf 32) gives the ladder (the figure caption continues on pdf 33).

| Rung | Activity | Typical questions |
|---|---|---|
| 1 Association | seeing | What if I see …? How are variables related? |
| 2 Intervention | doing | What if I do …? How? |
| 3 Counterfactuals | imagining | What if I had done …? Why? |

### Rung 1: association (pdf 34–35)
- Two events are associated if observing one changes the likelihood of observing the other. Rung one means predictions from passive observation (pdf 34).
- Example: of toothpaste buyers, what proportion also buy floss? This is a conditional probability, written $P(\text{floss} \mid \text{toothpaste})$. The vertical bar means we condition on what we see (pdf 34).
- Correlation and regression (the slope of a fitted line) measure association. Statistics alone cannot say which of toothpaste or floss is cause or effect. Pearl notes that good predictions need not come with good explanations; the owl hunts well without knowing why the rat moves as it does (pdf 34).
- Pearl places present-day learning machines on rung one, alongside the owl (pdf 34–35).
  - He cites Marcus (AI is "bursting with microdiscoveries") and Darwiche, whose position-paper title asks whether the goal is human-level intelligence or only animal-like abilities.
  - Deep learning succeeded mainly by showing some tasks were easier than thought. It gives impressive abilities but, in Pearl's judgment, no intelligence, because no model of reality.
  - Deep networks add layers to the fitted function, but raw data still drives the fitting. A driverless car will not work out that a pedestrian holding a whiskey bottle may react differently to a horn. Programmers must add that explicitly.

### Rung 2: intervention (pdf 35–37)
- Example: what will happen to our floss sales if we double the price of toothpaste? This needs knowledge absent from the data (pdf 35–36). Seeing smoke tells a different story from making smoke (pdf 36).
- Passive data cannot answer it, however big. Past high prices may have come from other causes, such as shortage with every store raising prices. A deliberate price ignores market conditions (pdf 36).
- Experiments (such as Facebook's) are a very direct way to predict the result of an intervention. Pearl adds that effects can sometimes be predicted without an experiment, for example when the model includes market conditions or enough key surrogates for them (pdf 36).
- A sufficiently strong and accurate causal model can allow rung-one (observational) data to answer rung-two queries. Without the model, one cannot go from rung one to rung two. So deep-learning systems that use only rung-one data and have no causal model will never be able to answer questions about interventions (pdf 36–37).
- Notation: $P(\text{floss} \mid do(\text{toothpaste}))$, the query of what happens if we do something. The "How?" question (how can we sell the surplus toothpaste?) is a cousin (pdf 37).
- Taking aspirin is an everyday intervention (pdf 37).

**Intuition note.** Seeing a high price tells you about the world that produced it. Setting a price changes the world. Data from the first cannot by itself describe the second.

### Rung 3: counterfactuals (pdf 37–43)
- Headache gone: was it the aspirin? To answer, we must go back in time and ask what would have happened without aspirin. No experiment can deny treatment to an already treated person and compare (pdf 37).
- Data are facts. They cannot tell us what happens in a world where observed facts are negated. Humans still make such inferences, as Eve did. Pearl says this ability most distinguishes human from animal intelligence and from model-blind AI (pdf 37).
- Science does this too. Hooke's law (had the weight doubled, the length would have doubled as well) is read as a functional relation holding for this very spring. Worlds with weight $x$ and length $L_x$ are treated as objectively knowable (pdf 38).
- Toothpaste counterfactual: the probability that a toothpaste buyer would still have bought it had the price doubled. This compares the real world with a fictitious one (pdf 38).
- Rewards: finding why a blunder occurred or why a treatment worked for some people lets us learn from history. Democritus is quoted (pdf 38).
- The Lion Man sculpture (about 40,000 years old, Stadel Cave) is, for Pearl, a sign of the new ability to imagine. Pearl states that all other hominids except the Flores ones became extinct within 10,000 years of its creation (pdf 38–39, 43). The advantage of counterfactuals is flexibility, learning from past actions and willingness to take responsibility (pdf 43).
- Experiments alone cannot answer rung-three queries. Rung one deals with the seen world, rung two with a "seeable" new world, and rung three with a world that cannot be seen because it contradicts what is seen. Bridging this needs a model of the causal process, a "theory" or "law of nature". Having such laws lets us selectively violate them to create worlds that contradict ours (pdf 43).

### The mini-Turing test (pdf 43–52)
- **Turing's test and advice (reported):** a computer counts as thinking if a human cannot tell it from a human. Turing predicted that in about fifty years computers could play so well that an average interrogator would have no more than a 70 percent chance of a right identification after five minutes. Pearl says Turing was slightly off, since no Loebner Prize entrant had fooled all four judges, or even half, as of 2015 (pdf 44). Turing suggested simulating a child's mind, which he thought like a blank notebook. Pearl says this was wrong, since the child's brain has rich mechanisms and prestored templates (pdf 44).
- Pearl thinks mastering causation is a key component of childlike intelligence (pdf 44).
- **Mini-Turing test:** encode a simple story in any convenient representation, then test whether the machine answers the causal questions a human can. It is "mini" because it covers only causal reasoning, and the machine need not acquire the story itself. The principle is that representation comes before acquisition (pdf 45).
- **Objection (Searle's Chinese Room, reported):** the machine could cheat with a stored list of all questions and answers. **Pearl replies:** cheating is impossible. With ten binary variables there are roughly 30 million possible queries (Pearl's figure), and more variables or states make the list astronomically larger, beyond the number of atoms in the universe (pdf 45–46).
- So humans must have a compact representation plus an answer-extraction procedure. Pearl believes it is a causal diagram, and says no other model is known to pass the test (pdf 46).

**Firing squad (Figure 1.4, pdf 46–49).** Court order $CO \to C$ (captain) $\to A, B \to D$ (death). All five variables are true/false. Assumed in the story: the soldiers fire only on command, and if either shoots the prisoner dies (pdf 46–47).
- *Rung 1.* If the prisoner is dead, the court order was given (follow the arrows backward). If $A$ fired, then $B$ fired too, although $A$ does not cause $B$ (no arrow) (pdf 47).
- *Rung 2.* What if $A$ fires on his own? Pure logic finds this contradictory ("That does not compute"). The rule taught to the machine: remove all arrows pointing into the intervened event, set it to its value, and continue by ordinary logic. This is "surgery". It frees the event from other influences and leaves one influence, the one enforcing it (pdf 47).
- Figure 1.5: delete $C \to A$ and set $A$ = true. The prisoner dies, because $A \to D$ is intact. $B$ (in all likelihood) did not shoot (pdf 47–48).
- If we *see* $A$ shoot, $B$ shot too. If $A$ *decides* to shoot, or we make him, the opposite holds. This is the difference between seeing and doing (pdf 48).
- Big Data (records where all five variables are true or all false) cannot predict the effect of persuading $A$ not to shoot without knowing who listens to whom (pdf 48).
- *Rung 3.* The prisoner is dead, so $A$, $B$, $C$ and $CO$ are all true. What if $A$ had decided not to shoot? Erase the arrow into $A$ and set $A$ = false, keeping the rest of the past as it was (Figure 1.6). $B$ = true still holds, so the prisoner would be dead anyway (pdf 48–49).
- Computers must be taught to break the rules of logic selectively, as children do (pdf 49).
- Humans may have a harder time with many variables, non-binary variables (e.g. unemployment after a minimum-wage rise) and uncertainty (e.g. a jammed gun). Uncertainty needs likelihood information about such abnormalities (pdf 49).

**Intuition note.** Seeing and doing differ by one operation. For doing, cut the arrows into the variable you set, then reason as usual. For counterfactuals, do the same cut but keep the facts you observed about everything else.

**Vaccination example (Figure 1.7, pdf 50).** Fictitious data, 1 million children.

| Group | Number | Outcome |
|---|---|---|
| Vaccinated (99%) | 990,000 | 1/100 get reaction, so 9,900; 1/100 of those fatal, so 99 deaths; no smallpox |
| Unvaccinated (1%) | 10,000 | 1/50 get smallpox, so 200; fatal in 1/5, so 40 deaths |

- More children die from vaccination (99) than from smallpox (40). Parents might say "Vaccines kill!" (pdf 50).
- Counterfactual: set the vaccination rate to zero. Then $1{,}000{,}000/50 = 20{,}000$ get smallpox, and $4{,}000$ die. Real deaths are $99 + 40 = 139$. Difference: 3,861 lives. Vaccination saves lives (pdf 50).

**Lessons (pdf 51–52).**
- A causal model is more than arrows. Behind each arrow $X \to Y$ is a probability rule for how $Y$ would change if $X$ changed. Often the diagram's structure alone lets us estimate causal and counterfactual relations without specifying the rules (pdf 51).
- One routine for all queries: draw the diagram, listen to the query, do the surgery (none for association), compute with the modified model. No retraining is needed for new stories (pdf 51).
- A diagram works because it carries causal information, built by asking who could directly cause the outcome. Reversing the arrow Vaccination → Smallpox would give the same data associations but the wrong conclusion that smallpox affects vaccination (pdf 51).
- Pearl's conviction: causes and effects are more fundamental than probability. He reports that research shows three-year-olds understand the entire ladder (pdf 52).
- Diagram structure survives changes in probabilities (a safer vaccine, less smallpox). The same estimand (recipe for answering the query) stays valid and can be applied to new data. Pearl conjectures that this robustness is why human intuition is organized around causal relations (pdf 52).

### On probabilities and causation (pdf 52–55)
- Philosophers (Reichenbach and Suppes onward) tried to define causation by probability raising: X causes Y if X raises the probability of Y (pdf 52). This seemed a natural bridge between rungs one and two, but it led to decades of failed attempts (pdf 52).
- Almost without exception they wrote it as $P(Y \mid X) > P(Y)$. Pearl says the attempts failed not because of the idea itself but because of this formal wording, which he calls wrong since "raises" is a causal concept. The expression speaks only about observations: if we see $X$, the probability of $Y$ increases. That can happen for other reasons, including $Y$ causing $X$ or a third variable $Z$ causing both (pdf 53).
- Probabilities like $P(Y \mid X)$ lie on rung one and cannot by themselves answer rung-two or rung-three queries. Hence Pearl does not define causation. Definitions demand reduction to a lower rung. He compares this to Euclid, where "point" and "line" are undefined (pdf 53).
- Ice-cream sales and crime: the criterion would call ice cream a cause of crime, since both rise in summer (pdf 53).
- Attempted repair: condition on background factors $K$, i.e. $P(Y \mid X, K = k) > P(Y \mid K = k)$. With $K$ = temperature, at 90 degrees no residual association remains (pdf 53–54).
- Nobody could say generally which variables belong in $K$, because confounding is itself a causal concept. Cartwright (1983) proposed conditioning on "causally relevant" factors. This borrows a rung-two concept, but risks defining a cause in terms of itself (pdf 54). Pearl says the correct criterion comes in Chapter 4 and is practically impossible to state without diagrams (pdf 54).
- Pearl's conclusion: "probabilistic causality has always foundered on the rock of confounding". The proper repair is $P(Y \mid do(X)) > P(Y)$, which can be decided from a causal diagram and data (pdf 54).
- Pearl says similar ideas persist in econometrics ("Granger causality", "vector autocorrelation") (pdf 55).

**Intuition note.** $P(Y \mid X) > P(Y)$ compares groups that differ in many ways. $P(Y \mid do(X)) > P(Y)$ compares what happens when only $X$ is changed.

### Pearl's own path (pdf 55–56)
- In the early 1980s Pearl thought uncertainty was AI's missing piece and that probability should represent it. He developed Bayesian networks (Chapter 3), which compute the likelihood of facts given what is seen (pdf 55).
- They did not bridge human and artificial intelligence. Arrows pointed from causes to effects, but he saw this as a cultural habit. In his 1988 book he called causation a language for talking about "relevance relationships", which he now finds embarrassing because relevance is a rung-one notion (pdf 55–56).
- Bayesian networks stay on rung one. Two twists lifted them: graph surgery in 1991 (observations plus interventions) and, in 1994, counterfactuals. Probabilities encode beliefs about a static world. Causality tells how they change when the world changes, by intervention or imagination (pdf 56).

## Toy example (ours, not from the text)
Ice cream ($I$) and crime ($C$) share a cause, weather ($W$): arrows $W \to I$ and $W \to C$, with none between $I$ and $C$. Half of all days are hot, half cold.
- Hot days: $P(I=1)=0.8$, $P(C=1)=0.6$. Cold days: $P(I=1)=0.2$, $P(C=1)=0.2$.
- Rung 1 (seeing): $P(I=1)=0.5(0.8)+0.5(0.2)=0.5$. $P(C=1)=0.5(0.6)+0.5(0.2)=0.4$. $P(C=1, I=1)=0.5(0.8)(0.6)+0.5(0.2)(0.2)=0.24+0.02=0.26$. So $P(C=1 \mid I=1)=0.26/0.5=0.52 > 0.4$. Naive probability raising holds.
- Condition on $K$ = hot: $P(C=1 \mid I=1, \text{hot})=0.6=P(C=1 \mid \text{hot})$. No raising, as in the text's 90-degree days.
- Rung 2 (doing): surgery deletes $W \to I$. Crime depends only on $W$, so $P(C=1 \mid do(I=1))=P(C=1)=0.4$. Since $0.4 \not> 0.4$, ice cream is not a cause in the $do$ sense.

## Concepts
- [[ladder-of-causation]] — three rungs: association, intervention, counterfactuals, ordered by the queries each can answer (pdf 34)
- [[do-operator]] — $P(Y \mid do(X))$: probability when $X$ is set by intervention, not just observed (pdf 37)
- [[causal-dag]] — dots-and-arrows model; here also an answer-extraction representation for all three rungs (pdf 29, 46)
- [[graph-surgery]] (new) — to model setting a variable, delete its incoming arrows and fix its value (pdf 47)
- [[counterfactual]] (new) — a query about a world contradicting observed facts, such as asking what would have happened had A not shot (pdf 37, 48)
- [[mini-turing-test]] (new) — encode a simple story and test whether a machine answers causal queries correctly (pdf 45)
- [[probability-raising]] (new) — the idea that X raises Y's probability; Pearl says it needs do-notation, not conditional probability (pdf 53–54)
- [[estimand]] (new) — a recipe for answering a query from data; valid while the diagram is unchanged (pdf 52)
- [[bayesian-network]] (new) — Pearl's earlier probabilistic model of uncertain reasoning; rung one until later extensions (pdf 55–56)
- [[confounding-vs-selection-bias]] — here only confounding: a common cause makes association misleading; Pearl calls it a causal concept (pdf 53–54)

## Canonical instances
- [[mammoth-hunt-model]] — a non-deterministic causal model with modular local changes (pdf 29–30)
- [[toothpaste-floss-example]] — one scenario used for all three rungs (pdf 34–38)
- [[firing-squad-example]] — a diagram answering rung-one, two and three queries by surgery (pdf 46–49)
- [[smallpox-vaccination-example]] — counterfactual comparison reverses the raw death-count impression: 99 vs 40, then 3,861 lives saved (pdf 50)
- [[ice-cream-crime-example]] — confounding by temperature defeats $P(Y \mid X) > P(Y)$ (pdf 53–54)
- [[lion-man-sculpture]] — Pearl's emblem of imagination (pdf 38–43)

## Bridges (candidates)
- [structural-analogy] $P(Y \mid X) > P(Y)$ ("probability raising") ↔ bayesian: evidence raising a posterior over a hypothesis — both are rung-one updating on observation, with no causal claim.
- [structural-analogy] Vaccination counterfactual (everyone unvaccinated vs actual) ↔ potential outcomes: outcomes of the same units under different treatments.
- [same-math] $P(Y \mid do(X))$ via graph surgery ↔ do-operator (canon): the chapter pairs the do-notation for interventions with graph surgery as the way to answer them, without a formal statement of the link.
- [structural-analogy] Bayesian networks (Pearl, rung one) ↔ causal DAG: same graph, different questions answerable.
- [metaphor] Searle's lookup-table cheat vs compact causal diagram ↔ Bayesian model: a small generative model, not a table of all data.

## Questions this raises
- What exactly must we know to compute $P(Y \mid do(X))$ from observational data? (Pearl promises a criterion in Chapter 4, pdf 54.)
- How can a machine learn the causal diagram, given that Pearl says acquisition comes after representation (pdf 44–45)?
- How are probabilities attached to arrows for uncertainty such as a jammed gun or a late order (pdf 49, 51)?
- If $P(Y \mid do(X)) > P(Y)$ is the right "probability raising", how does it handle unmeasured confounders?

## Reading notes
- No printed page numbers are visible in the text layer or in the page images supplied (pdf 29, 32, 43, 46–49, 51). Citations use pdf numbers (source pdf 27–57).
- pdf 40–42 are blank in the extracted text. The Lion Man photo caption is on pdf 43, and the sculpture's text is on pdf 38–39.
- Figure 1.2's caption splits across pdf 32–33.
- The arrow symbol in "Vaccination → Smallpox" (pdf 51) was missing in the text layer, but the image shows it.
- pdf 57 holds only a Galton board caption, which does not connect to the surrounding text. It is not summarized here.
- The "mathematical proof" that the three levels differ (pdf 30–31) is asserted, not shown, in this chapter.
- The 30-million query count (pdf 45) is Pearl's rough figure; I did not recompute it.
