---
id: grimmer-2022-textasdata/ch02-social
work: grimmer-2022-textasdata
unit: Chapter 2. Social Science Research and Text Analysis
pages: 38-69
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 23
pipeline_version: 0.1
---
# Social Science Research and Text Analysis

## L0 — One line
Research with text as data should be iterative and cumulative (discovery, measurement, inference, with fresh data for testing), guided by six principles, among them that the best method depends on the task and that validation is essential.

## L1 — The gist (≤ 120 words)
The authors ask how social scientists should use text and algorithms when the standard theory-first, data-later model fits real research poorly. They propose an iterative model: explore data to discover concepts, measure them, then test the refined theory on new data. They illustrate this with the King–Pan–Roberts study of Chinese censorship. They then state six principles: theory is essential; algorithms augment humans; research is iterative and cumulative (sample splitting is the safeguard); methods distill language into simpler representations; the best method depends on the task; and validation is essential. The approach is "agnostic": often there is no "true" value to target and no one best model. The book is organized by research stage.

**Prerequisites:** hypothesis testing and p-hacking; overfitting and training/test splits; causal versus predictive questions; classification versus clustering; the idea of a high-dimensional feature space.

## L2 — Key ideas (5–10 bullets)
- The standard deductive model (theory → hypotheses → data → results) has real virtues, such as reducing false discoveries from researcher discretion. It also hides how research is actually done and, if followed too closely, can cost researchers chances to discover questions and measures (pp. 38–40).
- The authors propose an iterative model: exploring data refines theory, and the refined theory is then tested on newly obtained data, which avoids p-hacking and forking paths (pp. 40–41).
- Research has three stages: discovery (develop concepts and questions), measurement (validated description), and inference (causal or predictive). A project need not pass through all three, and studies may move among them in various orders (pp. 42–47).
- The authors' "agnostic" view holds that in many instances there are no "true" values to target and no one best model for a corpus. This contrasts with the "structural" view, and it puts validation, not model-fit diagnostics, at the centre of measurement (pp. 49–50).
- King–Pan–Roberts show the whole cycle: an accidental discovery of censored posts, a hypothesis from a data subset, measurement, an observational estimate, then a randomized field experiment (pp. 51–54).
- Six principles (Table 2.1): theory is essential; text analysis augments humans; iteration and cumulation (with sample splitting) are needed; methods distill language; the best method depends on the task; validation is essential (p. 55).
- The authors argue that sample splitting is better than pre-analysis plans for guarding against multiple-testing false discoveries, especially with text (pp. 61–62).
- Confidence in text methods rests on empirical performance, not theorems about natural language. Validation therefore has several layers: task, unsupervised coherence, aggregation, face validity, hypothesis validity, label fidelity (pp. 65–68).

## L3 — Walkthrough

### Opening: deductive vs iterative research (pp. 38–42)
**The standard deductive view.** The authors describe the most common process as a linear one. On this view, researchers must have a clear theory before viewing data, must know their concepts a priori, then measure them, and finally test observable implications (King, Keohane, and Verba, 1994) (p. 38). An extreme version fixes theory and implications before looking at any original data. Achen (2002) is cited as summarizing this "new style" as insisting on a formal model plus white-noise errors as the starting point (p. 38). The authors say each of them has written papers in this mode (p. 38).

**Virtues (author's view).** The deductive approach can be particularly powerful when established theories have testable implications. It encourages analysts to reflect on mechanisms. If followed explicitly, it helps reduce false discoveries from researcher discretion, which is the logic of pre-registration (p. 39).

**Weaknesses.** Forcing tests of theories formed before the data arrive has substantial weaknesses. Qualitative researchers accept induction (full-cycle research design, grounded theory, nested analysis) (p. 39). The authors report that quantitative researchers also discover new questions and measures in their data (p. 39). Their own example is King, Pan, and Roberts (2013): the study began as validation of the text-analysis method ReadMe and became a study of the strategy behind Chinese social media censorship (p. 39). Aversion to induction may also stop scholars from building new theory at the end of a series of tests, for fear of a post-hoc justification (p. 39).

**A problem of reporting.** Papers conventionally state theory first and introduce data afterwards, whatever really happened (pp. 39–40). This is a problem for inference if the same data are used both to develop and to test a theory but are presented as fresh (p. 40). The authors say there is nothing inherently wrong with induction. One misstep to avoid is using the same dataset to develop and test a theory (p. 40).

**The iterative model (Figure 2.1, p. 41).** Left (deductive): Theory/Model → Hypotheses → Data Collection and Analysis → Results. Right (iterative): a cycle Data Collection → Data Analysis → Theory/Model → back to Data Collection; then Hypotheses → Data Collection and Analysis → Results. After the inductive loop, the researcher must obtain new data to test the refined theories. This avoids the concerns of p-hacking, forking paths and researcher degrees of freedom associated with induction (p. 40). The need for induction is not new nor specific to text. But the richness of text makes it helpful both early and late in a project (p. 41).

**Three stages.** Discovery, measurement and inference (including causal inference and prediction) (p. 42). A project need not pass through all three to be useful. Stages can be visited in various orders, and an inferential task may lead us to reconsider our measures or discover a new question (p. 42).

> **Intuition note.** Researchers often learn from looking at data, but the test of the resulting idea must then use data that did not shape it. On the authors' account, new data lets the iterative model keep the learning while avoiding the p-hacking concerns (p. 40).

### 2.1 Discovery (pp. 43–44)
The primary goal is to develop the research question. This includes deciding what to measure, which requires a **conceptualization**: a way of organizing the world that simplifies it to one or two aspects (p. 43). Example: social media posts could be organized by topic, sentiment, readability, informativeness or civility, or by a dimension the analyst does not yet know (p. 43). Text analysis helps by pointing to new organizations: **clusters** (groups similar within and distinct between), or an underlying **spectrum** (a low-dimensional summary where nearer texts are more similar). It can also find words that characterize groups (p. 43). Not all organizations are useful. Context and existing theory must be used to judge them (p. 43). Discovery is often left out of the standard model. Methods for it are underdeveloped, partly because questions come from many sources (earlier results, a new dataset, even a mistake). Grounded theory is the qualitative example (pp. 43–44). Acknowledging discovery licenses scholars to describe it in publications (p. 44).

### 2.2 Measurement (p. 45)
With concepts in hand, researchers measure their prevalence or locate texts on a spectrum. Examples: the Policy Agendas and Comparative Agendas Projects measure topic prevalence in party manifestos; measuring negativity in advertisements allows study of turnout effects (p. 45). Measurement is the essential ingredient for description, which is an important goal in itself (p. 45). Researchers must validate that the measure describes the intended concept. If it does not, they refine the measure or, in some cases, redefine the concept (p. 45).

### 2.3 Inference (p. 46)
Measures can be used for prediction (e.g. forecasting stock prices or conflict locations: how today's information informs tomorrow) or for causal inference (e.g. the effect of going negative on news coverage). The authors will keep separate which of the two is being done, because research designs differ (p. 46).

### 2.4 Social science as iterative and cumulative (pp. 47–48)
Attending to the stage matters. Discovery feeds measurement, and both feed descriptive, causal and predictive inference (p. 47). Even the best-designed study should not have the final word: later work can redefine concepts, refine measures or replicate on new data, especially since the social world changes (p. 47). The book is organized by research stage rather than by technical model type, as in earlier overviews (Grimmer and Stewart, 2013) (p. 47). Reason: which method to use, how to interpret and how to validate depend on the stage (pp. 47–48). The same model serves different purposes. A classifier (measurement) can find characteristic words (discovery); LDA, designed for discovery, can be repurposed for measurement. The task shapes interpretation and validation (p. 48). Tools will change but tasks will not, so the stage-based organization will not become obsolete (p. 48). The chapter's six principles come from statistical properties, from how designs behave with text, and from the authors' experience, and so were themselves learned inductively (p. 48).

### 2.5 An agnostic approach (pp. 49–50)
**Agnostic** (author's term): in many instances there are no "true" values for text-as-data methods to target, and no one best model for all applications of a corpus (p. 49). This shapes how findings are evaluated, how models are chosen, and when aggregating models is reasonable (p. 49).

**Contrast: the structural approach.** It posits an underlying true data-generating process even at discovery. The clearest statement is attributed to Denny and Spirling (2018). Under it, model selection is more straightforward, but it may force uncomfortable assumptions, such as a true set of categories (p. 49). Example: campaign ads can be organized by tone, by topic, or by a nested scheme of coarse topics with finer subdivisions. None is "correct" without knowing the research goal (p. 49). In discovery the authors may even prefer methods that are not "consistent" or "unbiased" if they yield useful insights (p. 49).

**Measurement.** Once the question is set, accuracy for the specific concept can be assessed. The authors are agnostic about which model is used, provided it measures the concept accurately and reliably (p. 50). They therefore stress validations that often involve careful reading, codebooks and application-specific criteria rather than model-fitting diagnostics, because the model is only a useful approximation (p. 50). They say the structural view is useful and important. They simply disagree that there is one "best" set of concepts or one underlying organization (p. 50).

> **Intuition note.** A corpus has many valid ways to be sliced. The question shifts from whether this is the right model to whether the model measures the needed concept and whether that can be shown.

### 2.6 Worked case: how the Chinese government censors social media (pp. 51–54)
Research programs rarely emerge as papers present them. Questions often come from an initial inspection of data, guided by background knowledge, which reveals a puzzle or pattern. Text is especially amenable to this because reading allows deep exploration (p. 51).

**Discovery (pp. 51–52).**
- King, Pan and Roberts (KPR) began by extending automated text analysis to Chinese. They downloaded millions of posts from more than 1,400 social media sites (p. 51).
- Revisiting the original URLs, they found many posts missing, replaced by notices of removal. This indicated government censorship (p. 51).
- This gave them a question (what is the target of censorship?) and one organization of the texts (censored vs not censored). They drew on general knowledge of censorship in authoritarian regimes (p. 51).
- For a hypothesis, they first grouped posts by topics expected to vary in sensitivity, but censorship varied little across topics (pp. 51–52).
- A computer-assisted look at censorship over time suggested higher rates for posts tied to collective action events (p. 52). This changed the unit of analysis to the event and the key quantity to whether the event involved collective action (p. 52).
- Sentiment (critical vs supportive of the government) also seemed not to explain censorship. If right, censorship would depend on protest relatedness, not criticism (p. 52).
- The authors call this discovery. They use a subset of data and statistical methods to find the question, generate a hypothesis and fix the conceptualization (p. 52).

**Measurement (p. 52).**
- KPR identified 87 events based on bursts of posts in 85 topic areas. They manually coded whether each burst was related to collective action (p. 52).
- Censorship status was straightforward to measure from their own records (p. 52).
- Sentiment was harder. The goal was the proportion of critical or supportive posts within censored and uncensored groups, not each post's sentiment (p. 52).
- They hand-labelled a sample of posts as critical or supportive, then used the supervised method ReadMe (Hopkins and King, 2010) to extrapolate to the whole collection (p. 52).

**Causal inference (pp. 52–53).**
- They estimated the average effect of a post's being about collective action on the probability of censorship, and the average effect of sentiment (pp. 52–53).
- Posts in bursts about collective action events were censored at an extremely high rate. Censorship was essentially unrelated to whether the post supported the government (p. 53).
- Their conclusions provide evidence that the censorship rules were intended to avoid mass protest rather than to suppress online dissent (p. 53).

**Limits of the observational study, and the experiment (p. 53).**
- Observational data necessarily excluded posts censored automatically and never posted (p. 53).
- Since the post's subject could not be manipulated, collective-action discussion might not be the property of the text that causes censorship (p. 53).
- KPR (2014) therefore ran a randomized field experiment. They created accounts on one hundred sites across China and varied (1) protest-related vs unrelated events and (2) critical vs supportive stance (p. 53).
- The results gave the same conclusion as the observational study (p. 53).

**Why this is not "overfit" (pp. 53–54).**
- Exploration used a subset, so KPR could be shown wrong on new data (p. 53).
- Theory played a role: a simple account of why the government censors led to the new question (pp. 53–54).
- Later formal models (Chen, Pan, and Xu, 2016; Lorentzen, 2014) were inspired by the results. The research program grew cumulatively across studies and scholars (p. 54).

> **Intuition note.** One accident (missing posts) led to a question. A data subset led to a hypothesis. Fresh or new-design data led to a test. The authors present this explore-then-test pattern as one model of how empirical social science can proceed (p. 54).

### 2.7 Six principles (p. 55; Table 2.1)
1. Social science theories and substantive knowledge are essential for research design.
2. Text analysis does not replace humans; it augments them.
3. Building, refining and testing theories requires iteration and cumulation.
4. Text analysis methods distill generalizations from language.
5. The best method depends on the task.
6. Validations are essential and depend on the theory and the task.

#### 2.7.1 Theory and substantive knowledge (pp. 55–57)
"Theory" means explanations of systematic facets of social processes, whether a formal model or a sentence. It determines which data are relevant, how to interpret results, and why they matter (p. 55). Sometimes a literature already defines concepts (e.g. a "negative advertisement" is one that casts opponents in unfavorable terms) and suggests hypotheses (p. 55). In other cases concepts are vague. KPR started in 2009 on a new field, with a rich literature on how citizens in repressive regimes express preferences but limited guidance on social media (p. 56). They explored a subset. Interpreting the exploratory output required thinking about the incentives of posters, how the government constrains companies, and Chinese online culture (p. 56). Recognizing that missing posts meant censorship required knowing about censorship practice, how to detect it and why it matters. Algorithms made the dataset possible, but substantive attention was needed (p. 56). Massive text and sophisticated algorithms make theoretical reasoning more, not less, important. The authors add that massive datasets help researchers think more precisely about theory because the extra data often lets them test hypotheses they previously lacked data for (p. 56).

**Opposing view (Anderson, 2008):** big data would end theory (in a piece titled "The End of Theory") by replacing theorizing with more data (p. 57). **Authors' reply:** these claims are wrong because they overstate what algorithms provide. An amount of interpretive work essential to these approaches cannot be automated, at least in the foreseeable future. Context is essential to important questions and ethics, and many of the book's models are useful only with close interpretation (p. 57).

#### 2.7.2 Augmenting, not replacing (pp. 57–60)
Text has long been analyzed (books, laws, transcripts). Qualitative methods emphasize careful reading plus analysis. Example: McQueen (2018) analyzes thousands of documents to argue that Machiavelli, Hobbes and Morgenthau were influenced by apocalyptic movements (p. 57). Computer-assisted analysis augments reading and helps us "read differently, not avoid reading at all" (p. 57).

**The hay analogy (Hopkins and King, 2010).** Texts are straws in a field.
- *Task A:* analyze one straw (a poem's beauty, a line's meaning, what is left unwritten). Humans are adept; the book's methods are rarely designed for this and typically fail on small or isolated documents (p. 58).
- *Task B:* sort straws into piles of similar ones. Humans are ill equipped (small active memory, distraction, misread instructions). Algorithms do this well given a well-defined objective or human guidance (p. 58). Computers are therefore good at discovering organizations and compressing text to lower dimensions (p. 58).

**Example:** Blaydes, Grimmer, and McQueen (2018) analyze advice-for-rulers texts from Muslim and Christian countries, 1000–1600 CE, using a method that discovers coarse and granular topics (p. 58). In Christian texts, religion occupies a smaller and smaller share; in Muslim texts it stays constant (pp. 58–59). They theorize that the later divergence between governments is due in part to religion's importance for just rule. They relied on both computer-assisted sorting and close reading (p. 59).

**Cost.** New methods make some research tasks cheaper. Supervised classification reduces hand coding. Other methods use proxies and need no human coding. Supervised scaling such as WordScores (Laver, Benoit, and Garry, 2003) places documents in a low-dimensional space with researcher-set anchors (p. 59).

**Speed and the Bell number.** Even 100 open-ended survey responses ("artisanal data", Wallach's term) pose a huge search problem if we want the most interesting *partition*, an assignment of every text to exactly one category (p. 59). The number of partitions is the Bell number:
- 2 documents {A, B}: 2 partitions (AB together; A,B apart) (p. 59).
- 3 documents: 5 partitions: ABC; A,BC; AB,C; AC,B; A,B,C (p. 59).
- 100 documents: about $10^{115.68}$ (exponent reconstructed from a garbled text layer; see Reading notes). By comparison, about $10^{80}$ atoms are estimated in the known universe (p. 59).

The authors conclude that even small collections have a massive space of organizations that computers help explore (p. 59). Text analysis serves a fundamentally qualitative task, extracting meaning, and bridges the quantitative–qualitative divide (pp. 59–60).

> **Intuition note.** Machines are good at the tedious, large-scale sorting that humans do badly. Humans are still needed to read, interpret and decide what an organization means.

#### 2.7.3 Iteration and cumulation (pp. 60–62)
The belief that theory building is almost exclusively deductive reflects a time when data were expensive and thinking comparatively cheap. The cost of thinking has stayed about constant while data collection and analysis have become far cheaper. So initial samples can be used for exploration, leading to new organizations, measurements, questions and designs (p. 60). The approach is not atheoretical. Each stage is informed by theory: conceptualization needs knowledge of prior organizations; measures matter insofar as they match theoretical quantities; causal estimates test which observable implications hold (p. 60). The authors claim this matches how social science is actually practiced (p. 61).

**Sample splitting (train/test).** Recommended at nearly every stage (p. 61):
- *Discovery:* shows whether a pattern is prominent in only one subsample or holds in the whole set.
- *Measurement:* prevents overfit classifiers, and fresh data evaluates performance on new data.
- *Causal inference* (Part 5): training tunes the method to find conceptualizations likely to yield interventions with causal effects; testing credibly evaluates effect size and avoids common problems of fishing.
- *Prediction:* perhaps the most common application, where splitting plays a vital role in assessing accuracy.

**Versus pre-analysis plans.** Splitting addresses the concern that many tests on one dataset yield non-generalizable results through multiple testing. The popular fix under the deductive model is pre-registration. The authors say splitting is better, especially for text, because pre-analysis plans are often effective only when others check them, researchers lack time to check, registries make linking paper to plan hard, and amendments are allowed (pp. 61–62). Splits are transparent to readers (p. 62).

**Two objections to splitting, and replies (p. 62).**
- *Objection 1:* experiments are costly and the power loss is not justified. **Reply:** the authors do not believe any loss in power outweighs the risks of not splitting, especially where stakes are high. Splitting detects overfitting and ensures cleaning rules reflect the dataset.
- *Objection 2:* some historical data occur once. **Reply:** sometimes true, but less often than people realize, because analogous interventions exist. Fowler and Montagnes (2015) tested the finding of Healy, Malhotra, and Mo (2010) (college football scores affect Congressional elections) with NFL games and found no indication that NFL scores affect elections. If the original logic were correct, a similar effect would be expected.

#### 2.7.4 Distilling language (pp. 62–64)
Text is complex. Example: Martin Luther King Jr.'s "I've Been to the Mountaintop", delivered on the eve of his assassination. It alludes to Exodus, with King implicitly as Moses (pp. 62–63). Part of its power comes from its timing and speaker, so, the authors say, no text analysis method could hope to fully capture its complexity, much of which does not come from the text alone (p. 63).

**Goal.** Text is high-dimensional: a numerical representation holding all its information would need very many features (columns), unlike a survey respondent's income or age, each a single number. Methods compress to a lower-dimensional representation that retains content useful for the research agenda, from a positive/negative label to annotation along dozens of categories (p. 63).

**Three reasons to reduce.**
1. *Interpretability and generalization:* it lets us relate texts on some dimension. It informs reading in discovery and clarifies what is measured. Example: reducing legislation plus roll-call votes to one ideology or partisanship dimension (p. 63).
2. *Statistical:* the "curse of dimensionality". Without reduction, prediction overfits and forecasts perform poorly, and causal effects lack the basic information needed for reliable estimation (p. 64).
3. *Theory:* most social science theories concern low-dimensional concepts, such as a one-dimensional ideological spectrum (Downs, 1957). Testing them needs measures along it, e.g. classifying posts from very conservative to very liberal (p. 64).

**Forms of distillation (p. 64).** (a) Hand coding by research assistants; (b) supervised learning from manual codings to assign unseen documents to known categories; (c) partitioning documents into discovered categories and assigning documents to them; (d) discovering treatments present in a collection. All lose information. The authors say the compression itself is the point of the exercise (p. 64).

#### 2.7.5 The best method depends on the task (pp. 64–66)
No single best method exists, and even one task may have several useful methods. The authors do not claim their own models are superior (p. 64). Practice: try several methods, evaluate, and select the best (pp. 64–65). Reasons:
- *Texts differ* in length, content, formality and grammar. Topic models, in the authors' experience, tend to perform extremely well on newspaper articles or prepared elite statements but unevenly on short or informal text (p. 65).
- *Features of interest differ:* topic, sentiment, ideology and authorship (stylometry) need different content (p. 65).
- *Tasks differ:* discovering an organization, classifying into preexisting categories, and inferring a text's causal effect are fundamentally different (p. 65).
- *Little theory ties methods to language:* estimators have deep statistical properties, but few theorems relate performance to natural language or to social science tasks. Properties are proven conditional on simplified representations of text (pp. 65–66).

So confidence rests on empirical evidence of performance across problems, not proofs, and every application needs extensive evaluation (p. 66).

#### 2.7.6 Validation (pp. 66–68)
Few if any theorems justify methods on natural language, so the justification is empirical (methods that worked before on similar problems). Collections differ in many ways, so validation is needed (p. 66). Doing the literal task well is "neither necessary nor sufficient" for a valid social science inference: low-level errors may accumulate when aggregated, and unit-level accuracy does not prove the concept is captured. Several validation steps are therefore typical (p. 66).

1. **Task validation (p. 67).** For supervised classification and prediction, ask whether the task can be replicated where the answer is known. Tools: validation datasets, cross-validation (Part 4), held-out data for forecasts (Part 5).
2. **Unsupervised models (p. 67).** Read texts in a category to judge coherence; inspect features indicative of a category or dimension; use quantitative model-fit measures.
3. **Humans in the loop (p. 67).** For many tasks models should be judged by how humans use their output. Designing experiments to include human judgment avoids arbitrary criteria. The book describes experiments to assess topic and cluster quality.
4. **Aggregation (pp. 67–68).** Example: a spam filter sometimes lets spam into the inbox but only very rarely sends important mail to the spam folder. The authors say this means the probability an email is not spam is likely systematically overestimated, and that summing estimates gives an upwardly biased estimate of spam received (p. 67; see Reading notes). General point: show that combining individual decisions does not introduce systematic bias (pp. 67–68).
5. **Face validity (p. 68).** The measure should pass inspection by a subject expert.
6. **Hypothesis validity (p. 68).** The dataset follows an expected pattern. Hypotheses should be so obvious that a negative finding would be hard to explain, since the line between a failed validation and a finding is blurred. Example: Grimmer (2013b) shows committee chairs focus more than the average senator on issues under their committee's jurisdiction, validating the topical classification of Senate press releases.
7. **Label fidelity (p. 68).** Does the label attached to the compression match what the measure captures? For hand coding or supervised methods, make codebook definitions transparent and show coders followed the rules. For unsupervised methods, show sample text, or recover the discovered categories with a researcher-defined codebook and supervised methods.

> **Intuition note.** A method that scores well on its own narrow test may still mislead when you add up its outputs or name its categories. So, according to the authors, research projects typically need several validation steps between raw text and the theoretical concept.

### 2.8 Conclusion (p. 69)
The authors advocate using data and algorithms at every stage, including the earliest, to refine questions, develop measures and generate hypotheses (p. 69). Their experience is that this yields better questions, theories and concepts (p. 69). Specific methods may become outdated, but the model of social science inference depends on none of them. The tasks are long-standing, and transparency means new methods have a clear place and can be checked by the validations (p. 69). The next chapter begins representing text as quantitative data (p. 69).

## Toy example (ours, not from the text)
Illustrates the explore-then-test cycle with sample splitting. Take 8 posts with a protest flag and a censored flag.

- **Explore half (4 posts).** Protest posts: 2, censored 2. Non-protest posts: 2, censored 0.
  - Censorship rate: protest 2/2 = 1.00; non-protest 0/2 = 0.00. Gap = 1.00 − 0.00 = 1.00.
  - Hypothesis formed: protest posts are censored more.
- **Test half (4 new posts, untouched during exploration).** Protest posts: 2, censored 1. Non-protest posts: 2, censored 0.
  - Rates: protest 1/2 = 0.50; non-protest 0/2 = 0.00. Gap = 0.50.
- **Reading.** The direction survives in fresh data. The size of the gap shrinks from 1.00 to 0.50, so the explore-half number alone would have overstated the effect. Testing on new data gives the credible estimate. (With only 4 posts per half this is an illustration, not evidence.)

## Concepts
- [[text-as-data-validation]] — treating text as measurements whose validity must be shown by task-specific checks; here validation is multi-layered (task, aggregation, face, hypothesis, label fidelity) (pp. 66–68)
- [[observable-implications]] — testable consequences of a theory; here, causal estimates show which implications appear in the data and which do not (p. 60)
- [[iterative-research-model]] (new) — cycle of data collection, analysis and theory refinement, followed by hypotheses tested on new data (pp. 40–41)
- [[discovery-measurement-inference]] (new) — the three stages of the research process; stages can be visited in various orders (pp. 42–47)
- [[agnostic-approach]] (new) — view that there is often no "true" organization of a corpus or single best model; methods are judged by usefulness for the task (pp. 49–50)
- [[structural-approach]] (new) — view that a true underlying data-generating process exists even in discovery (Denny and Spirling, 2018) (p. 49)
- [[sample-splitting]] (new) — dividing data into training and test sets at nearly every stage, guarding against overfitting and multiple-testing false discoveries (pp. 61–62)
- [[distillation-dimensionality-reduction]] (new) — compressing high-dimensional text into a simpler representation that retains task-relevant content (pp. 63–64)
- [[face-hypothesis-label-validity]] (new) — expert plausibility check, obvious-pattern check, and check that a category label matches what is measured (p. 68)
- [[humans-in-the-loop]] (new) — validation that explicitly relies on human judgment in a partly automated process (p. 67)

## Canonical instances
- [[kpr-censorship-study]] — discovery, measurement, observational and experimental inference in one research program (pp. 51–54)
- [[hay-analogy]] — humans suit deep reading of single texts, algorithms suit sorting many (p. 58)
- [[blaydes-advice-for-rulers]] — computer-discovered topics plus close reading show diverging religious content in Christian vs Muslim texts (pp. 58–59)
- [[bell-number-partitions]] — 2 documents give 2 partitions, 3 give 5, 100 give about $10^{115.68}$ (p. 59)
- [[nfl-football-replication]] — an analogous intervention tests a "one-time" finding (p. 62)
- [[mountaintop-speech]] — text complexity that no method can fully capture (pp. 62–63)
- [[spam-filter-aggregation]] — unit-level accuracy does not guarantee an unbiased aggregate (p. 67)
- [[senate-press-releases-validation]] — hypothesis validity via committee chairs' issue focus (p. 68)

## Bridges (candidates)
- [structural-analogy] sample splitting for discovery vs test ↔ political-science (research design): avoiding use of the same data to build and test a theory — both guard against testing an idea on the data that produced it.
- [structural-analogy] distillation of high-dimensional text ↔ spatial model of voting: reducing complex documents or votes to a low-dimensional ideological spectrum (the text cites Downs, 1957).
- [metaphor] hay analogy (humans read one straw, machines sort the field) ↔ rational ignorance / information costs: both concern what can be processed at scale.
- [structural-analogy] agnostic vs structural view ↔ text-as-data validation: no single true model, so judge by validated task performance.

## Questions this raises
- How should one decide how much data to hold out when each half must still be large enough for discovery and for testing?
- When is a "hypothesis validity" test obvious enough to be informative but not so trivial that it proves nothing?
- If the best method depends on the task and texts, how can a researcher choose among candidate methods without peeking at test data?
- The authors say there are few theorems tying text methods to natural language. Could such theory be developed, and would it change the agnostic stance?

## Reading notes
- Printed page = pdf page (38–69); no offset.
- Page 59: the text layer for the Bell number and atom count is garbled ("1 0 1 1 5 . 6 8", "1 0 8 0"). No page image was provided for p. 59. I read these as $10^{115.68}$ and $10^{80}$. Check against the printed page.
- Page 67 (spam example): the text says the probability an email is "not spam" is overestimated, yet says the aggregate spam estimate is "upwardly biased". Those two claims seem to point in opposite directions; I report the author's wording without resolving it.
- Small typos in the source: the word "notation" where "notion" seems intended (p. 40); and a garbled phrase about the large collection of texts (p. 58).
- Footnote 1 (p. 69): parts of the chapter's introduction and Section 2.5 are drawn from Grimmer, Roberts, and Stewart (2021).
- The chapter has no exercises. Only Figure 2.1 (p. 41) and Table 2.1 (p. 55) were checked against images.
