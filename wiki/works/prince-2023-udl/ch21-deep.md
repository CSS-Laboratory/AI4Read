---
id: prince-2023-udl/ch21-deep
work: prince-2023-udl
unit: "Chapter 21 — Deep learning and ethics"
pages: 421–436
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 26
pipeline_version: 0.1
---
# Deep learning and ethics

## L0 — One line
Many AI ethics problems can be read as value-alignment problems (misspecified objectives, or information gaps between humans and systems); the authors also argue that ML research is value-laden, that responsible AI research is a collective action problem (good outcomes need cooperation), and that many social and ethical problems cannot be solved by technical innovation alone.

## L1 — The gist (≤ 120 words)
The chapter asks how deep learning and AI can harm people and what responsibility researchers have to consider and reduce that harm. It frames many harms as value alignment: the objectives given to an AI system may not match human values, or humans may not be able to see how the system works. It then covers intentional misuse, side effects (intellectual property, environment, jobs, concentration of power), a case study, and the claim that science is not value-free. It concludes that ML research cannot avoid ethics, and that responsible AI is a collective action problem. This matters because technical choices carry value judgments, and many social and ethical problems cannot be solved by technical innovation alone.

**Prerequisites:** loss function as training objective; conditional independence; classification; high-school idea of bias and fairness.

## L2 — Key ideas (5–10 bullets)
- Value alignment is hard because values are hard to define, to encode as objectives, and to get a model to learn. In ML the loss function is a proxy for the true objectives, and a mismatch between them is the outer alignment problem (pp. 421–422).
- The structural view treats alignment as a principal–agent problem (a human delegates tasks to an artificial agent). Conflicts of interest can arise when objectives are misspecified (bias, moral agency) or when the two sides have unequal information (transparency, explainability) (pp. 422–423).
- Bias can enter at problem specification, data, modeling/validation and deployment. If society is structurally biased, even complete data can encode bias, and "fairness through unawareness" (just removing protected attributes) is ineffective (pp. 423–424).
- Transparency has three levels (functional, structural, run). Transparency does not guarantee explainability (understanding how decisions are made). Local methods such as LIME (a simple model fitted to nearby points) give some insight into single decisions (pp. 426–427).
- AI can be misused deliberately (face recognition, militarization, fraud, privacy violations) and has wider side effects (IP, deskilling, energy, jobs, concentrated power) (pp. 427–431).
- The "gaydar AI" case study shows many of these problems at once (pp. 431–432).
- ML relies on inductive inference (models are constrained only at training points), so outputs can be wrong and accepting a prediction requires a value judgment. The authors argue this makes ML models value-laden, which casts doubt on the value-free ideal (the view that science should be objective, free of such values) (pp. 432–433).
- Ethical AI is a collective action problem (good outcomes need cooperation, although it is not necessarily in any individual's interest). The authors give four key points and urge reflection on one's work (pp. 433–435).

## L3 — Walkthrough

### Introduction (p. 421)
- AI has potential for social good (e.g. healthcare, climate) and for misuse and unintended harm. This produced the field of AI ethics (p. 421).
- Timeline: deep learning began in 2012 (AlexNet), but ethics interest did not follow at once. A fairness workshop was rejected from NeurIPS 2013 for lack of material. In 2016 the ProPublica COMPAS exposé and O'Neil's book gave ethics its "AlexNet" moment. FAccT submissions grew nearly ten-fold in five years from 2018 (p. 421).
- Jobin et al. found 84 AI-ethics principle documents, 88% released since 2016. These are voluntary and non-binding, so their efficacy is questioned. The authors say ethics is in its infancy and often reactive, not proactive (p. 421).
- Aim: start conversations, not give advice on being more ethical (p. 421).

### 21.1 Value alignment (pp. 421–423)
- **Value alignment problem:** ensuring AI "values" (objectives) match humanity's. Three difficulties: defining values completely and correctly, encoding them as objectives, and ensuring the model learns to carry them out (pp. 421–422).
- **Outer alignment:** the loss is a proxy for the true objective. Where the proxy is inadequate, the system can exploit "loopholes". Example: a chess RL agent rewarded for capturing pieces may produce many draws instead of wins (p. 422).
- **Inner alignment:** behavior may diverge from intended objectives even when the loss is well specified, e.g. if the learner misses the global minimum or the training data are unrepresentative (p. 422).
- Gabriel (2020): a *technical* component (how to encode values; some problems such as reward hacking and safe exploration may have purely technical solutions) and a *normative* component (what the correct values are). There may be no single answer across cultures, and encoded values should represent everyone, not only dominant groups (p. 422).
- **Structural view (LaCroix):** a human principal delegates to an artificial agent, as in the economic principal–agent problem. Conflicts arise when (i) objectives are misspecified or (ii) information is asymmetric (Fig. 21.1) (pp. 422–423).
- Bias and fairness and artificial moral agency concern specifying objectives. Transparency and explainability concern informational asymmetry (p. 422).

*Intuition note:* The loss function is what the model actually pursues. If it differs from what we want, the model can score well and still fail us. The principal–agent picture describes this as a problem of delegation, and adds a second source of conflict: unequal information.

#### 21.1.1 Bias and fairness (pp. 422–425)
- Statistical bias is deviation from a norm. In AI it is pernicious when the deviation depends on illegitimate factors, e.g. gender in hiring or race in recidivism prediction (p. 422).
- Sources of bias (Fazelpour & Danks) (p. 423):
  - **Problem specification:** choosing goals is a value judgment, and failure to operationalize goals adds bias.
  - **Data:** unrepresentative or incomplete data. PULSE, trained mostly on white celebrity photos, turned a low-resolution portrait of Barack Obama into a white man. Even complete, representative data elicit bias if society is structurally biased, e.g. Black people in the US have been policed and jailed more, so recidivism data are already biased.
  - **Modeling and validation:** choosing a fairness definition is a value judgment. Distinct but equally intuitive definitions exist that are logically inconsistent. This suggests moving toward judging whether algorithms promote justice in practice.
  - **Deployment:** feedback loops entrench bias. When GPT3 outputs are published online, training data for future models degrade (pp. 423–424).
- **Intersectionality:** social categories can combine into overlapping, interdependent systems of oppression; for example, the discrimination faced by a queer woman of color is not merely the sum of the discrimination she might face as queer, as gendered, or as racialized (Crenshaw) (p. 424). Buolamwini & Gebru found face analysis trained mainly on lighter-skinned faces does worse on darker-skinned faces, and worse on skin-colour–gender combinations than expected from each feature alone (p. 424).
- Failure rates may worsen discrimination against marginalized communities. A power-sensitive view must account for historical inequities and labor conditions encoded in data (p. 424).
- **Mitigation:** *fairness through unawareness* (removing protected attributes) is ineffective, since other features can still carry the information. More practical: define a mathematical criterion, then intervene to reduce deviation from it. *Separation* in binary classification requires the prediction $\hat y$ to be conditionally independent of the protected variable $a$ given the true label $y$ (p. 424). Fig. 21.2 lists interventions at data collection, pre-processing, training (adversarial training, fairness regularization, constraints) and post-processing (changing thresholds, trading accuracy for fairness) (p. 424).
- We cannot tell whether an algorithm is unfair to a community, or take steps to avoid this, unless community membership can be established. Most research uses ostensibly observable features. Features such as queerness, disability, neurotype, class or religion may be unobservable. The same problem arises when observable features have been removed from the data (pp. 424–425).

*Intuition note:* Removing a column need not remove its information, because the remaining columns can still carry it. More practical approaches first define a mathematical criterion for fairness, and choosing among definitions requires a value judgment (p. 423).

#### 21.1.2 Artificial moral agency (p. 425)
- Some actions carry moral weight (autonomous vehicles, lethal autonomous weapons, care robots). As autonomy grows, systems may need to decide morally without human input (p. 425).
- An **artificial moral agent** is an autonomous AI system capable of moral judgments. Moor's four levels: ethical impact agents (affect outcomes, not designed with ethics in mind); implicit ethical agents (some built-in safety features); explicit ethical agents (can contextually follow moral principles); full ethical agents (beliefs, desires, intentions, free will, consciousness) (p. 425).
- Machine ethics approaches: *top-down* (implement rules from a moral theory, e.g. Asimov's Three Laws), *bottom-up* (learn moral regularities from data, e.g. Noothigattu et al.'s voting system aggregating human preferences in moral dilemmas), and *hybrid* (p. 425).
- **Some researchers question the idea (van Wynsberghe & Robbins):** they argue that moral agency is unnecessary for ensuring safety (p. 425).

#### 21.1.3 Transparency and opacity (p. 426)
- A system is *transparent* if all details of its operation are known, and *explainable* if humans can understand how it decides. Without them, information asymmetry makes alignment hard (p. 426).
- Creel's three levels: *functional* (the algorithm's logical rules), *structural* (how a program executes the algorithm), *run* (how it was executed in one instance; for deep networks this includes knowledge of the hardware, input data, training data, and their interactions). The authors say none of these can be ascertained by scrutinizing code (p. 426).
- GPT3 is functionally transparent (architecture published) but not structurally or run transparent (no code, parameters, hardware or training data). GPT4 is not transparent at all (p. 426).

#### 21.1.4 Explainability and interpretability (pp. 426–427)
- Transparency does not imply understanding. Deep networks may contain billions of parameters, so there is no way we can understand how they work based on examination alone. The EU GDPR Article 22 suggests a right to "obtain an explanation of the decision reached" for solely automated decisions, though whether it mandates this is debatable (p. 426).
- **LIME** (local interpretable model-agnostic explanations) samples model outputs at nearby inputs and builds a simpler model (Fig. 21.3). It probes nearby points, weights them by proximity, and fits logistic regression (a linear function passed through a sigmoid). The fit's parameters show, e.g., that increasing $x_1$ or decreasing $x_2$ raises $Pr(y=1|\mathbf x)$ (pp. 426–427).
- Whether fully understandable complex systems are possible remains open. There is currently no concrete definition of explainable, understandable or interpretable (p. 426).

*Intuition note:* LIME does not explain the whole model. It fits a simple model that is close to the original only near one input and reads the explanation off that.

### 21.2 Intentional misuse (pp. 427–429)
- Even a correctly functioning system can be unethical or misused (p. 427).
- **Face recognition and analysis:** authoritarian states can use it to silence protesters. Smith & Miller argue its use cases mismatch liberal-democratic values, so some question whether it should exist. It often does not do what it claims: the NY MTA expanded its use despite a trial with a 100% failure rate to detect faces within acceptable parameters. Tools claim to infer sexual orientation, emotions, hireability or criminality. Stark & Hutson say they revive physiognomy and phrenology (pp. 427–428).
- **Militarization and political interference:** state funding risks an arms race. AI also enables cyber-attacks and disinformation at scale. Kosinski et al. suggest sensitive variables can be predicted from social-media "likes" alone. The chapter then says that from this information, traits like "openness" can be used for manipulative purposes, e.g. to change voting behavior (p. 428).
- **Fraud:** AI automates scams, fake documents and more convincing phishing. Transparency has a downside: the more open a system, the more vulnerable it may be to bad-faith use. ChatGPT has been used to write software and emails that could be used for espionage, ransomware and other malware. The **ELIZA effect** (anthropomorphizing computer behaviour and projecting meaning onto symbol strings) gives a false sense of security and raises susceptibility to text fraud (pp. 428–429).
- **Data privacy:** large crowd-sourced datasets may hold private information. Auxiliary knowledge can de-anonymize them: a student matched stripped health records to public voter rolls and identified Massachusetts Governor William Weld's records in 1997. Differential privacy and semantic security (homomorphic encryption, secure multi-party computation) can protect data in training (p. 429).

### 21.3 Other social, ethical and professional issues (pp. 429–431)
- **Intellectual property:** models are trained on copyrighted material. Language models may output copyrighted text verbatim, and diffusion models raise similar issues. Even under "fair use", moral rights of creators may in some cases be violated. Open questions: can model outputs be copyrighted or patented, and is fine-tuning on one artist's work to copy their style acceptable? Existing law was not made with ML in mind (pp. 429–430).
- **Automation bias and moral deskilling:** automation bias is expecting outputs to be correct because they are "objective". Deskilling is the redundancy and devaluation of skills in light of automation. Automating morally loaded decisions may reduce moral abilities (e.g. dehumanizing war victims, reducing our ability to care for each other) (p. 430).
- **Environmental impact:** Strubell et al. estimate that training a 213-million-parameter transformer emitted about 284 tonnes of CO$_2$. The footnote gives about 5 tonnes per year per average human. Closed proprietary models hide their impact (p. 430).
- **Employment:** McKinsey (2018) estimated that AI may increase economic output by about US $13 trillion by 2030, primarily from the substitution of labor by automation. Another McKinsey study suggests up to 30% of the global workforce (10–800 million people) could be displaced between 2016 and 2030 (p. 430). Forecasting is hard. Keynes called technological unemployment a "temporary phase of maladjustment" and new jobs may appear, but short-term social programs may be needed. Whether optimistic, neutral or pessimistic, society will change significantly (p. 431).
- **Concentration of power:** growing data and compute needs may let large firms outcompete small ones, creating a feedback loop of concentration. Many views hold such concentration incompatible with just distribution (Rawls). Calls to *democratize AI* urge open source and open science to cut barriers (p. 431).

### 21.4 Case study: "gaydar AI" (pp. 431–432)
- Wang & Kosinski (2018) drew sensational headlines. Six problems (pp. 431–432):
  1. The dataset was biased and unrepresentative (mostly Caucasian).
  2. Modeling and validation are questionable given the fluidity of gender and sexuality.
  3. The obvious use is discrimination and persecution where queerness is criminalized.
  4. The model appears to pick up spurious correlations from grooming, presentation and lifestyle, not facial structure, contrary to what the paper's authors (Wang & Kosinski) claimed.
  5. Scraping "public" photos and labels from a dating site raises privacy questions.
  6. Scientific communication: the paper's title overstates what the model can do. The chapter's authors (not Wang & Kosinski) add, "(They cannot.)"
- Such a model does nothing to benefit the LGBTQ+ community. The key question is whether work serves the interests of the community it concerns (p. 432).

### 21.5 The value-free ideal of science (pp. 432–433)
- **Authors' claim:** scientists are not neutral, and their values inevitably affect their work. The **value-free ideal** says science is or should be objective. Four stages where practitioners' values act: choice of problem, gathering evidence, accepting a hypothesis, applying results (p. 432).
- It is perhaps uncontroversial that values play a significant role at stages 1 and 4. The ideal prescribes minimizing values at stages 2–3 and presupposes the *value-neutrality thesis*: scientists can, at least in principle, handle those stages without value judgments (p. 432).
- ML values are mostly epistemic (performance, generalization, novelty, efficiency). Choosing this set is itself value-laden, and few papers discuss societal need or negative impacts (p. 432).
- **Longino:** these epistemic values are not purely epistemic. **Kitcher:** scientists don't typically care about truth itself; they pursue truths relevant to their goals and interests (p. 433).
- **Inductive risk:** models are constrained only at training points, a tiny part of the input space (curse of dimensionality). Outputs can always be wrong however much data we use. Accepting or rejecting a prediction therefore requires a value judgment that the risk of wrongly accepting is lower than the risk of wrongly rejecting (p. 433).
- Hence ML models are deeply value-laden (Johnson). If they were not, they would have no application. The authors say these insights have implications for researchers who believe algorithms are more objective than human decision-makers (and so ought to replace them where objectivity matters); the page does not spell the implications out (p. 433).

*Intuition note:* A model can never be sure to be right. Deciding when to trust its output means weighing which mistake costs more, and that weighing is a value choice.

### 21.6 Responsible AI as a collective action problem (pp. 433–434)
- Deferring responsibility is a mistake. Researchers choose projects, employers, knowledge sought, circles and how they communicate. Doing right is often a social dilemma: best outcomes need cooperation although individuals may not benefit from cooperating (p. 433).
- **Scientific communication:** misinformation spreads faster and persists more than truth in many social networks. Avoid overstating abilities and misleading anthropomorphism, and be aware of the potential for misapplication (pseudoscience such as phrenology and physiognomy has resurged in AI) (p. 433).
- **Diversity:** in homogeneous or homophilous groups the dominant group tends to have its conventions recapitulated and stabilized (O'Connor & Bruner). Remedies at institutional, research and individual levels. **Standpoint epistemology** (Harding): knowledge is socially situated. Broussard argues technology made mostly by able-bodied, white, cisgender, American men is optimized for them. Design justice holds affected communities should help design technologies (p. 434).

### 21.7 Ways forward (pp. 434–435)
- Optimistic visions need caution. Green: "AI for Social Good" was applied both to police accountability and to predictive policing, so the label is a value judgment. Check whether benefits are distributed equitably. *Technochauvinism* is assuming the most advanced technology is best (p. 434).
- Four key points: (1) ML research cannot avoid ethics, since commercial incentives and industry funding erode lab isolation; (2) even purely technical decisions can be value-laden; (3) question the structures AI work sits in, since fairness may not be instantiable within existing structures, so technology is inherently political; (4) social and ethical problems do not necessarily need technical solutions (pp. 434–435).
- Perhaps the imperative: reflect on the moral and social dimensions of one's work, engage affected communities and other disciplines. Venues: FAccT and AIES (p. 435).

### 21.8 Summary (p. 435)
- Bias, explainability, moral agency and other topics can be viewed through the value-alignment lens. AI can be intentionally misused. Ethical AI is a collective action problem. Not every issue is within one scientist's control, but researchers still have responsibility to consider and mitigate misuse where they can (p. 435).

## Toy example
*(Ours, not from the text.)* Proxy versus true objective, as in the chess example (p. 422). Reward = 1 per piece captured. Policy A captures 15 pieces and draws. Policy B captures 8 pieces and wins.
- Proxy score: A = 15, B = 8, so training on the proxy prefers A.
- True objective (win = 1, else 0): A = 0, B = 1, so we would prefer B.
- The proxy ranks the policies in the opposite order to the true objective. This is an outer alignment failure: the loss has a loophole.

## Concepts
- [[value-alignment-problem]] (new) — ensuring AI objectives match human values; hard to define, encode and learn (pp. 421–422)
- [[outer-alignment]] (new) — mismatch between loss function and true objectives (p. 422)
- [[inner-alignment]] (new) — behaviour diverges from intended objectives even with a well-specified loss (p. 422)
- [[principal-agent-problem]] (new) — conflicts can arise when a human delegates to an artificial agent: misspecified objectives or informational asymmetry (p. 422)
- [[algorithmic-bias]] (new) — statistical deviation from a norm, pernicious when it depends on illegitimate factors; can enter through specification, data, validation, deployment (pp. 422–423)
- [[fairness-through-unawareness]] (new) — removing protected attributes; ineffective (p. 424)
- [[separation-criterion]] (new) — $\hat y$ conditionally independent of protected $a$ given $y$ (p. 424)
- [[intersectionality]] (new) — social categories that can combine into overlapping systems of oppression; discrimination is then not merely a sum of parts (p. 424)
- [[artificial-moral-agent]] (new) — autonomous AI able to make moral judgments; Moor's four levels (p. 425)
- [[transparency-levels]] (new) — Creel's functional, structural, run transparency (p. 426)
- [[lime]] (new) — local explanation by fitting a simple model to nearby samples (p. 426)
- [[inductive-risk]] (new) — outputs may be wrong, so accepting them needs a value judgment (p. 433)
- [[value-free-ideal]] (new) — science should minimize the influence of moral, personal, social, political and cultural values on the intervening scientific process (p. 432)
- [[collective-action-problem]] (new) — best outcomes depend on cooperation although it is not necessarily in any individual's interest (p. 433)
- [[eliza-effect]] (new) — projecting meaning onto symbol strings and anthropomorphizing (p. 429)
- [[automation-bias]] (new) — expecting model outputs to be correct because they seem objective (p. 430)

## Canonical instances
- [[compas-recidivism]] — ProPublica exposé of bias in a recidivism model (p. 421)
- [[pulse-obama]] — super-resolution of Obama's portrait gave a white man (p. 423)
- [[gender-shades-intersectional]] — face analysis worse on skin-colour–gender combinations (p. 424)
- [[weld-deanonymization]] — health records matched to voter rolls (p. 429)
- [[gaydar-ai-case]] — facial "sexual orientation" model with six problems (pp. 431–432)
- [[training-emissions]] — 213M-parameter transformer, about 284 tonnes CO$_2$ (p. 430)

## Bridges (candidates)
- [same-math] separation criterion $\hat y \perp a \mid y$ ↔ probability: conditional independence — literally the same statement.
- [structural-analogy] loss as proxy for objectives ↔ economics: Goodhart-style proxy failure (the chapter's Problem 21.2 mentions the law) — optimizing a measure degrades it.
- [structural-analogy] LIME's local linear fit ↔ calculus: first-order local approximation of a nonlinear function.
- [structural-analogy] biased training data ↔ social science: sampling bias and measurement validity — unrepresentative data give distorted inference.
- [structural-analogy] inductive risk ↔ decision theory: choosing a threshold by the relative cost of the two error types.

## Questions this raises
- If fairness definitions are mutually inconsistent, how should one choose among them in a given deployment?
- Can an explanation that is only locally valid (LIME) justify a decision to the person affected?
- How would one measure whether the value-neutrality thesis fails in a particular ML paper?
- When is a social problem better addressed without a technical solution?

## Exercises worth doing
- Ex. 21.2 (p. 436) — reformulate Goodhart's law for proxy loss functions — difficulty: medium
- Ex. 21.3 (p. 436) — trace bias through the four stages in a "student success" model — difficulty: medium
- Ex. 21.4 (p. 436) — show the three transparency types are not tied together — difficulty: medium
- Ex. 21.7 (p. 436) — argue for and against open-source research given misuse — difficulty: medium
- Ex. 21.12 (p. 436) — relate a pause letter to collective action — difficulty: hard

## Reading notes
- Printed page = pdf − 14 (pdf 435 = p. 421).
- Figures 21.1–21.3 are images; I checked their captions against the page images. The text layer of Fig. 21.2 is garbled but the image is clear.
- The draft footer ("please send errata") appears at the foot of odd-numbered pages ("Draft: please send errata to udlbookmail@gmail.com"). The chapter is credited to Travis LaCroix and Simon J.D. Prince (p. 421).
- Citations are as printed: e.g. Ahmed & Wahed is dated 2016 for a "recent study" (p. 431). Wang & Kosinski is dated 2018 while the cited headlines are 2017 (p. 431).
- References are not included in these pages. The "Problems" list (p. 436) is summarized only in the exercise list.
