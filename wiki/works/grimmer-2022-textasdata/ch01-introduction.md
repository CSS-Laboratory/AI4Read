---
id: grimmer-2022-textasdata/ch01-introduction
work: grimmer-2022-textasdata
unit: Chapter 1. Introduction
pages: 22-37
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 12
pipeline_version: 0.1
---
# Introduction (Text as Data, ch. 1)

## L0 — One line
Text-as-data methods borrowed from computer science should be chosen, validated and interpreted according to the social-science task (discovery, measurement, prediction, causal inference), not by computer-science defaults.

## L1 — The gist (≤ 120 words)
The chapter asks how texts should be analysed when the aim is to learn about human behaviour, not to build computer-science tools. The authors argue that social-science goals differ from computer-science goals. Defaults for choosing, evaluating and validating models should therefore not be imported blindly. They organise the book around tasks (representation, discovery, measurement, prediction, causal inference). They work sequentially and inductively, and they treat models as useful (and incomplete) summaries of texts, not as recoveries of one true structure. Catalinac's study of Japanese election manifestos is the model case. The authors say the same view also serves the digital humanities, industry and government.

**Prerequisites:** the basic idea of a statistical model of text (topic model, classifier); the difference between description, prediction and causal inference.

## L2 — Key ideas
- Texts were rarely used in quantitative social science because they were hard to acquire, read and categorise at scale. Cheaper acquisition, more computing power and new methods changed this (pp. 22–23).
- Importing computer-science methods and evaluation habits without thought has created confusion, because the tasks differ. Computer science often targets retrieval, recommendation and benchmark tasks; social science studies previously studied phenomena (p. 23).
- The book is organised around tasks, not algorithms. The usual supervised/unsupervised split can hide how tools serve social-science tasks (pp. 23–24, 35).
- The authors favour research that is sequential, iterative and inductive, and that engages with theory and context. Theory here means explanations of the systematic facets of social process (p. 24).
- Catalinac (2016a) is the exemplar. She collected the data carefully, used LDA (Latent Dirichlet Allocation, a topic model) inductively, validated by social-science standards, and designed a causal test (pp. 26–29).
- The authors reject the idea that one true organisation of a text collection exists. Organisations are judged by usefulness for the research question and by the credibility of their validation (pp. 31–32).
- The same task view applies to the digital humanities, industry and government. Computational tools should amplify, not replace, the human scholar (pp. 30–34).

## L3 — Walkthrough

### Opening (pp. 22–25)
- The book is about using texts and language to make inferences about human behaviour. It addresses social science, digital humanities, industry and government (p. 22).
- Texts were used sparingly. They were hard to acquire, too long to read, and hard to sort into categories or to use to measure concepts. Use was limited to small datasets or to large, well-funded teams (p. 22).
- Three changes lowered the cost of analysis. The internet made texts easier to get. Laptops gained computing power. A literature in computer science and computational linguistics, then in the social sciences, produced tools (pp. 22–23).
- Almost all large-scale text analysis in the social sciences uses algorithms from computer science or built closely on them. Examples are topic models and supervised document classification (p. 23).
- Transfer also ran the other way. Item Response Theory models for roll-call votes are now used in computer science (p. 23).
- The authors' diagnosis is that this transfer created confusion about application, validation and interpretation. Practitioners have tended to adopt computer-science guidance reflexively, and blind importing of its default methods can lead to unintended consequences (p. 23).
- Their organising tasks are discovery, measurement, prediction and causal inference (p. 23).
  - Discovery is creating new conceptualisations, or ways to organise the world (pp. 23–24).
  - Measurement connects concepts to data, so we can describe how prevalent the concepts are (p. 24).
  - Measures are then used to make causal inferences about an intervention's effect, or to predict future values (p. 24).
- The research approach is sequential, iterative and inductive. Concepts and measures are refined as new data arrive. Evidence is considered in sequence: confirm prior work, test new hypotheses, then generate hypotheses for future work. This happens across a community, not within one article (p. 24).
- Theory is deliberately broad. It covers formal theory, political or sociological theory, and general subject expertise (p. 24).
- Their core argument is that learning from texts requires engagement with the context in which the texts were produced. Such knowledge helps researchers ask important questions, ensure valid measures, and attend to practical and ethical implications (p. 24).
- Without a guide, researchers outside computer science risk applying the wrong algorithms, validating the wrong quantities, and drawing inferences the evidence does not justify (pp. 24–25).
- The authors say the approach applies beyond text, wherever large-scale data are used to discover categories, measure their prevalence and assess their relationships (p. 25).

*Intuition note:* How good a method is depends on the job it has to do. A tool built to predict words may be the wrong tool for measuring what politicians talk about.

### 1.1 How this book informs the social sciences (pp. 26–29)
- **The puzzle.** Why did Japanese politicians give so much more attention to national security and foreign policy after 1997, despite post-WWII constraints? (p. 26)
- **The argument (Catalinac 2016a).** A 1994 electoral reform altered incentives (p. 26).
  - Before reform, districts were multi-member. Each party ran several candidates per district, trying to win the majority of seats. Co-partisans could not effectively compete on ideology, so they competed by delivering pork (spending with only local impact) (p. 26).
  - After reform, a parallel system replaced it: single-member districts, plus nationwide party-list representation. Parties could impose stricter ideological discipline, and voters chose more on platforms. Foreign policy became more advantageous than local pork (p. 26).
- **Data.** She collected 7,497 Diet candidate manifestos. They are important to candidates and voters, under candidates' control, and available for all candidates in all elections over a period before and after the reform. She found them through archival visits and digitised them by manual transcription, which took years. The authors take this to show that text work need not use the most convenient data (p. 27).
- **Discovery.** She used Latent Dirichlet Allocation (LDA) to discover topics and to measure the proportion of each manifesto in each topic. LDA is revisited in Chapter 13 (p. 27).
  - Her own description of the procedure is iterative. She sets a number of topics, runs the model, reads the high-probability words and documents, and judges whether the topics are substantively meaningful. She adds that her approach was also iterative and guided by her hypotheses (pp. 27–28, quoting Catalinac 2016a, p. 84).
  - Discovery does not start from a blank slate. Her prior work, interviews and expertise helped to shape what she found (p. 28).
- **Validation.** Her validation is social-scientific, not the computer-science kind. In computer science, validations tend to focus on how well LDA predicts unseen words in a document. That does not matter to her, because she has all the words (p. 28). She did two things (p. 28):
  1. She read the top words of each topic and the manifestos most aligned with it. This supports her labels and interpretations.
  2. She showed that her measures align with well-known facts about Japanese politics. This shows the measures are not idiosyncratic, and it supports the labels.
- **Causal inference.** She estimates the effect of the 1994 reform on the shift from pork to national security. The setting is hard because the reform hit all districts at the same time (p. 28).
  - After showing a substantial rise in national-security discussion, she rules out alternatives. She shows there was no sudden influx of candidates who would be expected to discuss security. She argues it is not merely an ideological shift in parties. She argues there is no evidence that voters suddenly wanted security-focused candidates (p. 29).
- **Lesson.** Validation is necessary and looks different from computer science. The authors say text-as-data researchers are much more interested in how well models give insight into concepts, how well measurement tools sort documents by those concepts, and whether the assumptions needed for causal inference or prediction are met (p. 29). The authors cite similar lessons in sociology, economics, psychology and law (p. 29).

*Intuition note:* The text is not the end product. It becomes a measured variable (topic share). The measure is then checked against reading and against known facts before it is used in a causal argument.

### 1.2 How this book informs the digital humanities (pp. 30–32)
- Digital humanities (DH) uses computational tools for literature, history and the humanities. It follows procedures similar to the social sciences: texts are turned into numbers, then models from other fields are applied (p. 30).
- A major difference is that digital humanists are often interested in the particular text itself, not the text as an indicator of a larger process. So DH has so far tended to focus on discovery and measurement and to give less attention to causal inference or prediction (p. 30).
- **Objection (Da 2019):** "what is robust is obvious (in the empirical sense) and what is not obvious is not robust" (p. 31, quoting Da 2019, p. 45).
- **The authors' reply.**
  - Da's critique relies heavily on procedures imported from computer science, as does much of the work she criticises. Directly importing such rules can give problematic inferences or misplaced judgements of feasibility (p. 31).
  - They hold a "radically agnostic" view, with six principles set out in Chapter 2. They reject the idea that models should be optimised to recover one true underlying organisation, because, they argue, no one such organisation exists (p. 31).
  - They say that the assumption is implicit in much DH work and in Da's critique. They suggest it comes from computer science and statistics, where it is a convenient fiction for evaluating model performance (p. 31).
  - Organisations are useful if they help answer a research question. If two models disagree, there is no sense in judging one more "right". For example, a sentiment organisation is not more right than a topic organisation (pp. 31–32).
  - Once an organisation is chosen, one finds the best measurement of it and validates it extensively. Lack of a "robust" single organisation is therefore less worrying than critics argue. What matters is the credibility of the validations and the organisation's utility for the research question (p. 32).
- Text-as-data methods should not displace the careful humanist, and there is no sense in which inferences should be made in the humanities without the reader directly involved. When used well, tools should help provide broader context, illuminate patterns otherwise impossible to identify manually, and amplify rather than replace the scholars' own efforts (p. 32).

*Intuition note:* Usefulness for a question replaces the truth of one underlying structure as the standard for an organisation of texts. Rigour then moves into validating the chosen organisation.

### 1.3 Industry and government (pp. 33–34)
- Companies use text for ad targeting, content suggestions and connecting people with officials. Government may use text to represent constituents' views, for example in public comments on proposed rules (p. 33).
- Stakes are high. Content moderation is described as perhaps the most politically sensitive application. After the Russian misinformation campaign in the 2016 US election, platforms faced pressure to remove misinformation, report on its effect, and show procedures were fair across ideologies. Large sums are also at stake, as in trading and advertising (p. 33).
- The authors map industry problems onto their tasks. Moderating misinformation or hate speech is a measurement task. Choosing ads that raise sales is causal inference. Trading on documents or statements is prediction (p. 33).
- Many data scientists are trained outside the social sciences. Their fields teach computational tools well but often not the core design principles behind the tasks (pp. 33–34).
- The book's structure shifts focus from models to tasks. Different tasks imply different models, different information sets to condition on, and different assumptions to justify conclusions (p. 34).

### 1.4 A guide to this book (pp. 35–36)
- The book is organised around five tasks: representation, discovery, measurement, prediction, causal inference. This lets the authors explain how the same algorithm can serve different tasks and need different validation (p. 35).
- Chapter 2 sets out the principles. The authors generally reject the view that models recover an underlying structure; they view statistical models as useful (and incomplete) summaries (p. 35).
- **Part 2: selection and representation.** It covers acquiring texts and representing them quantitatively. Sample-selection principles matter despite the pull toward convenient data (p. 35).
- **Part 3: discovery.** It covers (pp. 35–36):
  - words that distinguish how two groups speak;
  - partitioning methods that assign each observation to one category;
  - extension of clustering to admixture models, where each document is split proportionally among categories;
  - embeddings into lower-dimensional spaces, which can reveal underlying continuous variables.
- **Part 4: measurement.** It measures prevalence within categories or location on a predetermined spectrum. It combines human judgement with machine learning to extend training-set annotations to a larger dataset. A discovery method can be repurposed for measurement. Validation is covered for every measure, whatever method produced it (p. 36).
- **Part 5: prediction and causal inference.** It covers prediction, where threats to inference vary by setting. It also covers causal inference with text measures as outcome or intervention, including tools for assessing when a stringent set of assumptions is met (p. 36).

### 1.5 Conclusion (p. 37)
- The promise is large, but with big data, complicated models and custom measures, research can also go wrong. Text is complicated and meaning is subtle. Overclaiming risks undermining the case for text methods (p. 37).
- The book aims to show what is feasible and infeasible. Chapter 2 gives the guiding principles (p. 37).

## Toy example (ours, not from the text)
Four one-line "manifestos". Docs 1–2 are from before a reform, docs 3–4 from after.
- D1: "tax cut helps workers" (before)
- D2: "tax cut hurts schools" (before)
- D3: "new bridge helps town" (after)
- D4: "new bridge hurts river" (after)

Organisation A (by topic): {D1, D2} = taxes, {D3, D4} = bridges. Organisation B (by sentiment): {D1, D3} = "helps", {D2, D4} = "hurts". Both organisations fit the same words, and neither is "more right".

Research question: did attention to local public works rise after the reform?
- Under A, the share of "bridge" documents is 0/2 = 0 before and 2/2 = 1 after. The change is +1.
- Under B, the share of "helps" documents is 1/2 = 0.5 before and 1/2 = 0.5 after. The change is 0.

A is useful for this question and B is not. For a question about tone, the verdict would reverse. The chapter's point is that usefulness for the question, plus validation of the chosen organisation, is what counts.

## Concepts
- [[text-as-data-validation]] — validation judged by whether measures capture concepts and meet task assumptions, not by predicting unseen words (pp. 28–29). Canon id: text as data / validation.
- [[discovery]] (new) — creating new conceptualisations or ways to organise the world (pp. 23–24).
- [[measurement]] (new) — connecting concepts to data to describe how prevalent they are, or where documents lie on a spectrum (pp. 24, 36).
- [[theory-broad-sense]] (new) — explanations of systematic facets of social process, including formal theory and subject expertise (p. 24).
- [[radical-agnosticism]] (new) — rejecting the idea that a single true organisation of texts exists. Organisations are judged by usefulness for a question (p. 31).
- [[task-based-organization]] (new) — organising methods by research task, not by algorithm class (pp. 24, 35).
- [[topic-model-lda]] (new) — a statistical model that finds topics and each document's proportion in each topic (p. 27).
- [[admixture-model]] (new) — a model where each document is proportionally assigned to different categories (p. 36).

## Canonical instances
- [[catalinac-japan-manifestos]] (new) — 7,497 manifestos analysed with LDA to study whether the 1994 electoral reform shifted candidate attention from pork to security (pp. 26–29).
- [[da-critique-computational-literary-analysis]] (new) — an objection that DH results are either robust and obvious or non-obvious and not robust (p. 31).
- [[content-moderation]] (new) — a high-stakes industry application that the authors treat as a measurement task (p. 33).

## Bridges (candidates)
- [metaphor] "no one true organisation exists" ↔ political-science: preferences with no unique collective ranking (cycling). Both undercut the idea of one correct aggregate structure, but the maths differs.
- [structural-analogy] Catalinac's pork vs national-issue incentives ↔ political-science: electoral rules shape candidate strategy (spatial model of voting, party discipline). Both link institutional design to behaviour.
- [structural-analogy] Task-specific validation ↔ political-science: observable implications (KKV). Both test a theory or measure through varied checks.

## Questions this raises
- If no organisation is "more right", what makes a validation credible enough to compare two organisations?
- How can a hypothesis-guided, iterative choice of topic number avoid simply confirming the researcher's priors?
- Can inference stay valid when the measure is built from the same data used to discover the categories?
- What do digital humanists lose or gain by focusing on the specific text rather than on a larger process?

## Reading notes
- Printed page numbers equal pdf page numbers (offset 0).
- The chapter has no exercises.
- The Catalinac block quote starts on p. 27 and its attribution "(Catalinac, 2016a, p. 84)" appears at the top of p. 28.
- Misprint on p. 28: "Japenese" for "Japanese".
- Figure 1.1 (p. 27) is a Japanese-language manifesto image from 2003. Its text is not translated in the source.
- The claims about Chapter 2, 4 and 13 content are only previews. This unit does not give the six principles.
