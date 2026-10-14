---
id: murphy-2023-pml2/ch33-interpretability
work: murphy-2023-pml2
unit: 33 Interpretability
pages: 1073-1102
fields: [bayesian]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-15
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 23
pipeline_version: 0.1
---
# Interpretability

## L0 — One line
Interpretability is not a single mathematical property but a means to an end: an explanation is judged by whether, in a given context, it helps a human do their end-task better.

## L1 — The gist (≤ 120 words)
How can humans inspect machine-learning models to catch harms, gain insight, and work with the model? The authors answer that interpretability has no universal definition. It depends on the context and the user's end-task (final goal). Methods are inherently interpretable models (self-explaining), example-based models, and post-hoc (after training) or jointly trained partial explanations. They are chosen through desired properties such as fidelity (match to the model) or sparsity (small size). Evaluation uses computational property checks and user studies. Explanations are only partial views, so they can be unstable, over-trusted or misread, and human factors matter. A footnote warns that later results show popular methods can fail, and that some doubt the whole field.

**Prerequisites:** supervised prediction and loss/metrics; gradients and decision trees at a basic level; basic experimental design (confounds, randomization, significance tests).

## L2 — Key ideas (5–10 bullets)
- Interpretability helps when the goal cannot be fully formalized. It supports blindspot discovery, novel insights, human+ML teaming and individual recourse. The best explanation depends on context; interpretability is a means to an end (pp. 1074–1075).
- The framework has two human elements (context, end-task) and three technical ones (method, metrics, properties). Properties are the glue between methods and contexts (pp. 1075–1077).
- The lemonade example shows that two explanation methods can rank the same black box's features very differently, because they have different properties (p. 1078).
- Inherently interpretable models (sparse or logic-based) are their own explanation. Example-based models are semi-inherent. Otherwise explanations are partial views, computed post hoc or by joint training (pp. 1079–1085).
- Properties include faithfulness, compactness, completeness, stability, actionability, modularity, interactivity, translucence, simulability and alignment. Cognitive science adds soundness, generality, simplicity and contrastiveness (pp. 1087–1089).
- Computational evaluation uses hypothesis-based sanity checks and datasets with known ground truth. It can show that something is wrong, but passing does not prove the absence of blindspots (pp. 1090–1094).
- User studies are the ultimate test. They need baselines, careful design, qualitative follow-up, pilots and cautions about synthetic contexts (pp. 1094–1098).
- Principles: no universal definition; interpretability is not always needed; understand enough, not everything; partial views can be unstable and attackable; the performance trade-off often does not exist; over-reliance is a risk (pp. 1098–1102).

## L3 — Walkthrough

### 33.1 Introduction
**Why inspect models.** Narrow performance metrics can miss harm; the example given is that staying in lane does not make a car safe (p. 1073). The narrow objectives of decision formalisms and reinforcement learning can be exploited, e.g. reward hacking (p. 1073). Incomplete metrics lead to shortcut learning. Metrics can be hard to estimate under limited data or distribution shift. Normative concepts such as fairness may be impossible to fully formalize (p. 1073). Interpretability lets human experts inspect a model alongside statistical measures. It can also expose how a user's own information could be incorporated, and give scientific insight (pp. 1073–1074).

**Footnote caution (p. 1073).** After publication, [Bil+24] derived theoretical results showing that popular methods such as integrated gradients and SHAP can provably fail to do better than random guessing at explaining model behaviour. Other negative results exist, and some people (e.g. [LWS18; Mil23]) doubt the validity of the whole field. The book says the reader should exercise caution.

*Intuition note.* The chapter is a framework for thinking about explanations, not a guarantee that any listed method works. The footnote on its first page warns that some popular methods can provably fail (p. 1073).

#### 33.1.1 The role of interpretability
Some desired behaviour can be guaranteed by design, e.g. privacy via differentially-private learning, or a chosen fairness metric. Tracking metrics or well-calibrated uncertainties may sometimes be enough warning (p. 1074). Where the goal cannot be fully specified, human inspection may be needed. Four uses are given:
- **Blindspot discovery.** A credit-scoring model was trained on a relatively affluent, middle-aged population. If inspection shows heavy reliance on mortgage payments, the model may transfer badly to college-aged applicants. It also prompts a check for bias, since historical biases limited home ownership (p. 1074). The most common industry use is engineers debugging models and making deployment decisions (p. 1074).
- **Novel insights.** Suppose a clustering finds three surgery clusters, one of which runs long. A human inspecting them may find that these surgeries occur in a different part of the hospital, a feature not in the data (p. 1074).
- **Human+ML teaming.** Suppose an anxiety-treatment algorithm reveals that comorbid insomnia constrained its recommendations. If the patient reports no longer having insomnia, the algorithm could be re-run without that constraint (p. 1074). Inspection can also let people use only part of a model (p. 1074).
- **Individual-level recourse.** A denied applicant who knows the features used has a starting point to argue the decision was wrong. Inspectability is sometimes a legal requirement (p. 1075).

The common element is combining human insight with the algorithm (p. 1075). A footnote says interpretability differs from manipulation or persuasion (p. 1075). Needs differ across tasks. A scientist may study global patterns for hours; a clinician may care only about patient-specific aspects and must decide within the time pressure of an office visit. So the best explanation depends on context and interpretability is a means to an end (p. 1075).

#### 33.1.2 Terminology and framework
To interpret is "to explain or present in understandable terms". Understanding is an alignment of mental models: what the user thinks the model does versus what it does (p. 1075). The ecosystem includes the socio-technical system, which cannot be ignored. Terminology is still evolving, so terms should always be defined (p. 1075).
- **Context:** the setting of use (who the user is, what they know, time and attention limits). Used interchangeably with *application* (p. 1075).
- **End-task:** the user's ultimate goal; interchangeable with *downstream task* (p. 1076).
- **Method:** the output given to the user is the *explanation*. If the explanation is the model itself, the method is inherently interpretable (interpretable by design). Otherwise the explanation may be a partial view. Even inherently interpretable models do not reveal everything, e.g. training data or influential points (p. 1076).
- **Metrics:** evaluation is by the human's end-task performance when given the explanation, the *downstream performance*. The model with the best predictive performance (e.g. log likelihood) may not give the best downstream performance (p. 1076).
- **Properties:** characteristics of the explanation relative to model, context and end-task. Example: to help a denied applicant improve, it may be important that the explanation include only factors that, if changed, would change the outcome. To judge fairness, it may be important that it leave out no relevant factor. Properties are the glue between methods, contexts and end-tasks (p. 1076).

**How they relate (Figure 33.1).** One starts from context and end-task. These imply the evaluation metrics and suggest the important properties. The context also determines the data and training metric of the ML model. The explanation method is chosen given the model and desired properties, and is evaluated by downstream performance (p. 1076). The grand challenge is (1) to learn which properties different contexts and end-tasks need and (2) to build methods with those properties (p. 1077).

**Simple example (lemonade stand, pp. 1077–1078).** The context is a lemonade stand. The end-task is to understand when it is most successful, to decide which days to open. The metric is whether we correctly judge if the model can be trusted, quantified as profit from opening on busy days and closing on quiet ones. Inputs are the average temperature (°F) and sidewalk cleanliness (a proportion in [0,1]). The output is whether the day was profitable. Two models fit about equally well (p. 1077):

$$p(\text{profit}) = .9\,(\text{temperature} > 75) + .1\,(\text{howCleanSidewalk}) \tag{33.1}$$

$$p(\text{profit}) = \sigma\big(.9\,(\text{temperature} - 75)/\text{maxTemperature} + .1\,(\text{howCleanSidewalk} - .5)\big) \tag{33.2}$$

Both are easy to inspect and rely mostly on temperature (p. 1077). Now treat them as black boxes and ask for important features in two ways (p. 1078):
1. *Flip-based method:* for each training point, set each feature individually to its max or min and see whether the prediction changes. Both models report temperature as dominant. Vetting with this would correctly conclude both use features sensibly (p. 1078).
2. *Derivative-based method:* sum the absolute derivatives of the output with respect to each input over the training set. Model 2 still reports temperature. Model 1 reports sidewalk cleanliness, because its derivative with respect to temperature is zero nearly everywhere. This would wrongly suggest that Model 1 relies on an unimportant feature and that the two models differ (p. 1078).

The first explanation has the property of fidelity for identifying features that, if changed, affect the prediction. The second identifies features with the most local curvature. For this end-task the first property matters more (p. 1078). Footnote 4 says other properties may matter too.

*Intuition note.* "Important feature" has no single meaning. Two definitions of importance gave opposite answers on the same step-like model. So one must first say which property the end-task needs.

### 33.2 Methods for interpretable machine learning
This section is a snapshot of a fast-changing set of options; the right choice depends on context and end-task (p. 1079).

#### 33.2.1 Inherently interpretable models
Definition: models that need no additional process or proxy to serve as the explanation for the end-task. A person can inspect the full model and, with reasonable effort, understand how inputs become outputs. A model may be inherently interpretable for one end-task and not for another (p. 1079). Two categories:
- **Compact/sparse feature-based models:** sparse regressions, small HMMs, GLMs, latent variable models, super-sparse linear integer models and checklists. Drawbacks: if a model picks one of several correlated features, the driving signal is harder to identify. Correlated features may get opposite signs that cancel, making weights meaningless. Hierarchical or modular structure (topic models, small discrete time-series models, generalized additive models, monotonicity-enforced models) can address this (p. 1079).
- **Logic-based models:** decision trees, lists, tables, sets, logic programs. They model non-linear relationships easily but can struggle with continuous ones (a linear function versus a step-wise constant one). Hierarchies, e.g. defining new concepts from literals, extend them (pp. 1079–1080).

Three decisions (p. 1080):
- *Model class.* The model class is the form of explanation. A model that grows too large to inspect is no longer inherently interpretable, even within these classes.
- *Optimization.* These classes involve discrete parameters and need more advanced optimization: programs, relaxation and rounding, search. One option is distillation (mimic): train a complex model, use its outputs to train a simpler mimic, then discard the complex one.
- *Uninterpretable input features* (e.g. pixels). One can add a "concept" layer mapping raw input to human-interpretable concepts, then concepts to output. The open challenge is to ensure the concepts match the user's exactly (p. 1080).

Advantages: no worry about faithfulness or about whether the partial view is right. They are advocated for high-stakes settings and as the first thing to try [Rud19] (p. 1080). Drawbacks: they need specialized optimization. In images, waveforms and language, deep models typically give significantly higher performance. Fitting complex behaviour with a simple function can give high bias and invite incorrect rationalization. Migrating away from a legacy model meets resistance. They do not guard against all surprises, e.g. distribution shift (pp. 1080–1081).

#### 33.2.2 Semi-inherently interpretable: example-based methods
Predictions are based on examples, e.g. K-nearest neighbours; extensions find or generate exemplars and use embeddings or parts. They can describe highly non-linear boundaries. Individual decisions seem fully inspectable: each can be shown with the exact training instances used. But a complex similarity metric is hard to convey, so users may infer the wrong features, and the global boundary is hard to convey (p. 1081).

#### 33.2.3 Post-hoc or joint training: the explanation is a partial view
Reasons to need non-inherently-interpretable models: large neural models perform better on images, waveforms and text; a legacy business-critical model; a system of interconnected models. The explanation is then necessarily partial (p. 1081).

*33.2.3.1 What the explanation consists of.*
- **Form** (p. 1082). The model class and the explanation are now different entities, e.g. a deep network explained by a decision tree. Forms: lists of important features or concepts, a simpler approximating model (local linear, rule set), prototypical examples, contrastive/counterfactual explanations, influential examples. A contrast between treatments A and B may not help when comparing A and C. Literature on human communication can guide the choice, e.g. recognition-primed decision making in trauma nurses and firefighters.
- **Local scope** (p. 1082). Answers why this input got this output. It supports checking a decision or recourse. Forms include saliency/attribution maps (e.g. first-order derivatives), a locally fit simpler model (LIME), representative or influential examples, and nearby points with different predictions. Risk: overgeneralizing beyond the region, or building an incorrect mental model from a few local explanations (pp. 1082–1083).
- **Global scope** (p. 1083). Insight into the whole model, e.g. to decide on deployment. Forms: an approximating simpler model, concepts affecting many inputs, or chosen examples (characteristic, covering a class, near decision boundaries, influential in training). A global explanation of a non-inherently-interpretable model is still partial.
- **Properties first** (p. 1083). Forms differ in expressivity: a feature list or local linear model does not expose interactions, whereas a local decision tree would. Properties may also depend on the model. Gradient-based explanations may be fairly faithful for smooth models but not for spiky ones. The authors suggest that the first step in choosing form and computation should be to determine the needed properties.

*33.2.3.2 How the explanation is computed.* The computation strongly affects properties (p. 1083). "Importance" has several definitions:
- perturbation-based, e.g. the smallest image region that changes the prediction. This still requires choices: stay in the training distribution? preserve pixel correlations? (pp. 1083–1084);
- sensitivity-based (largest gradients), with many computational choices (p. 1084);
- membership in a "winning coalition", e.g. Shapley or Banzhaf scores (p. 1084).

These have different properties and computational costs. Similarly, example-based explanations require defining similarity (cosine of activations? an L2 ball?). Counterfactuals can use distance functions, causal frameworks or SAT formulations (p. 1084).

**Joint training vs post-hoc** (pp. 1084–1085). Post-hoc means extracting an explanation from a trained model. Its limits do not mean the explanation is wrong. A local linear view is just insufficient if the true boundary is curvy. Joint training adds a regularizer penalizing violations of desired properties. It is often possible because most complex model classes have multiple high-performing optima [Bre01]. Examples: using human-like features, controlling input dimensions, compactness, constraints on concepts. Caveats: joint training needs re-training, which may be impossible for a long-deployed system. It is not a panacea, since optimizing some properties may violate other unspecified ones, so explanations remain partial (p. 1084).

**When post-hoc?** Advantages: applicable to any model, including systems of many models, and they may give broader knowledge to spot concerns. Disadvantages: as approximations they may not be fully faithful or complete. A method tuned for one context may not transfer, and blindspots may remain. In high-stakes settings, try an inherently interpretable model first if possible; whenever post-hoc explanations are used, warn users appropriately that they are one tool among many in a broader accountability toolkit (p. 1085).

#### 33.2.4 Transparency and visualization
Transparency is an umbrella term for exposing the modeling process and context: data collection, training, and released code. Visualization is one way to create transparency; interactive visualization can convey more, and presentation choices (even for a rule list) affect how easily users consume an explanation (p. 1085). Problems may lie in the training pipeline. Examples: policing data with historical bias gives biased hot-spot predictions. If clinicians only order tests when concerned, a model trained on tests ordered will only recapitulate what they already know (p. 1085). These methods need time and are ill-suited to quick bedside decisions (pp. 1085–1086). Code access can help find bugs and enable third-party testing. For sufficiently complex models it is likely not enough for understanding (p. 1086).

### 33.3 Properties: the abstraction between context and method
Context and end-task determine the needed properties. A high-stakes setting may need fidelity. A discovery setting may need interactivity. Lacking a key property may harm downstream performance (p. 1086). Methods sharing properties may have similar downstream performance, and contexts needing the same properties may be served by the same method (p. 1086). Finding the right properties will likely require iteration via user studies. This is still a smaller space than iterating over methods, e.g. one can create explanations of varying sparsity to test whether sparsity matters (p. 1086).

#### 33.3.1 Properties from interpretable ML (pp. 1087–1088)
- **Faithfulness/fidelity:** how well a partial view matches the model. For a mimic: how often it gives the same outputs, or has the same first derivatives. For key features: whether the prediction changes when the "important" features are flipped, or does not change when "unimportant" ones are flipped (p. 1087).
- **Compactness/sparsity:** small enough to process within task constraints. Compactness adds not including anything irrelevant (p. 1087).
- **Completeness:** includes all relevant elements, and derived concepts are expressive enough for all directions of variation that change the prediction. An explanation can be faithful in some ways but incomplete: flipping a set of "unimportant" features together may change the prediction (p. 1087).
- **Stability:** similar explanations for similar inputs. It may be impossible when the model has high curvature and the explanation is of limited expressiveness (p. 1087).
- **Actionability:** focus on aspects the user can intervene on (e.g. exercise, not age). Recourse is actionability in a justice context (p. 1087).
- **Modularity:** explanation breaks into understandable parts (p. 1087).
- **Interactivity:** the user can ask questions or navigate (p. 1087).
- **Translucence:** the explanation is clear about its own limitations (e.g. a local linear fit warns of strong feature interactions nearby). It concerns limits of the explanation, not the model (p. 1088).
- **Simulability:** a user can compute the output from model and input. A feature list is not simulable; a shallow decision tree is. Compact does not imply simulable. Easy-to-simulate forms can become computational training constraints (p. 1088).
- **Alignment to user's vocabulary and mental model:** e.g. medical conditions instead of raw sensor readings. Parameter variances may suit an engineer but not a loan applicant (p. 1088).

Properties must be operationalized (is the L1 norm enough for sparsity?). This is a human-centric decision. Most properties can then be optimized and should be evaluated with context, end-task, model and method. Achievability depends on the model: a highly nonlinear model with interactions is harder to understand than a linear one (p. 1088).

#### 33.3.2 Properties from cognitive science (p. 1089)
Human explanations must fit the context, but they are also social constructs with post-hoc rationalizations and biases, so we should adopt properties that help users reach goals. Listed, with the ML analogues the text gives:
- *Soundness* (nothing but the truth) ~ compactness and faithfulness.
- *Completeness* (the whole truth) ~ completeness and faithfulness.
- *Generality* (reflects an underlying principle, applies to similar cases) ~ stability.
- *Simplicity* (simpler preferred, all else equal) ~ sparsity.
- *Contrastiveness* (how it differs from an alternative) ~ actionability and counterfactuals.

Human explanations are goal-directed and take forms such as deductive-nomological (logical proofs), mechanism-giving, or understanding-conveying (p. 1089).

*Intuition note.* Properties are the shared vocabulary that lets us ask what a task needs without naming a method. The authors note that searching over properties is a much smaller space than searching over methods (p. 1086).

### 33.4 Evaluation
Interpretability cannot be formalized without context, end-task and downstream metric. If one explanation enables better end-task performance, it is more useful (p. 1090). Two categories:

#### 33.4.1 Computational evaluation (without people)
Checks properties such as faithfulness under different data distributions, or sparsity. It is useful when properties are known to matter, and as a cheap sanity check before expensive user studies. It can pinpoint how an explanation falls short, which a user study may confound (p. 1090). Some properties may be proved; others are tested empirically. Strategies are a hypothesis-based sanity check ("phenomenon X should never occur" – try to make it occur) and datasets with known ground truth (synthetic, semi-synthetic, or slices of real data). These tests can only show that something is wrong; passing does not rule out blindspots (pp. 1090–1091).

- **[Ade+20a]:** a faithful explanation should be a function of the model's prediction. So it should change significantly between a trained and an untrained (random-prediction) model. Many methods fail (Figure 33.4: cascading randomization of layers from the logits downward) (pp. 1091–1092).
- **[Kin+19]:** they hypothesize that a faithful explanation should be invariant to input transformations that do not affect predictions or weights, e.g. adding 10 to all inputs. This tests faithfulness and stability, and some methods fail (pp. 1091–1092).
- **[GAZ19]:** adversarial attacks show two perceptively indistinguishable inputs with the same predicted label can get very different explanations (p. 1092).
- **[YK19] (semi-synthetic, Figure 33.3):** targets compactness and faithfulness, i.e. not marking unimportant features as important. Foreground objects are placed on backgrounds with known co-occurrence rates. Each image has an object label and a background label. One model classifies objects and another classifies backgrounds. If objects share one background, the background should be less important for the object model than for the background model ("model contrast score"). The background model should also not attribute to foreground objects (p. 1092).
- **Real datasets without ground truth (Figure 33.5):** assuming features do not interact, build predictions from the top-1, top-2, … ranked features and look for diminishing returns in accuracy. With interactions the test fails; if C matters only when B is present, C's importance is over-estimated (p. 1093). [Gho+19a] add the top-n patches one by one, and deleting them gives reverse evidence (p. 1093). [DG17] define "smallest sufficient region" and "smallest destroying region", turn them into optimization objectives, and evaluate saliency separately via the tightest rectangular crop fed to the classifier. The rectangle may introduce artifacts, but is described as a neat trick (pp. 1093–1094).
- **Evaluating the evaluations:** [Tom+20] found many saliency-quality metrics statistically unreliable and inconsistent. Each may still have a use [Say+19] (p. 1094).

#### 33.4.2 User-study-based evaluation
Tasks may be the real end-task or a synthetic one; rigorous design is critical (p. 1094). Real contexts are the gold standard (p. 1094).

**Basic elements (pp. 1094–1096).**
- *Interface design:* extrinsic difficulty (presentation) can be conflated with intrinsic difficulty (model complexity). Interfaces and training should be neutral across conditions (pp. 1094–1095).
- *Baselines:* no ML system; ML without explanation; ML with a placebo explanation (no information); ML with hand-crafted explanations (p. 1095).
- *Design and hypotheses:* define independent and dependent variables, hypotheses and inclusion/exclusion criteria beforehand. Example: independent variable = form of assistance; dependent variable = whether the developer finds bugs. Criteria might be experience, engagement on practice rounds, no prior experience with the explanation types (p. 1095). Studies that only ask whether one explanation beats another in a given context may give little insight into why. One can manipulate factors directly, e.g. hand-crafted complete, one-missing and several-missing explanations, or fake or buggy classifiers (wizard-of-Oz studies) (pp. 1095–1096).
- *Randomization/matching:* randomization marginalizes over confounds (subject prior knowledge; task-order learning effects). Matching (same subject, two explanations) and repeated measures reduce variance. Latin-square or block designs randomize explanation order. Within-subject comparisons have lower variance but a possible learning bias. Across-subject comparisons have higher variance and possible population-shift bias. The significance test and multiple-hypothesis correction must fit the design (p. 1096).
- *Qualitative studies:* think-aloud protocols can help identify why an explanation seems useful or not. Example: users shown clips of a video-game agent may presume it always chases coins, or attribute a pit fall to one-off sloppiness rather than a repeated mistake (p. 1096).
- *Pilot studies:* small pilots check whether participants attend to information in unexpected ways and whether instructions are clear. Pilot results are not included in final results. More factors mean more participants and longer sessions, so decide what can be done computationally (p. 1097).

**Synthetic contexts (p. 1097).** Used when real testing is unethical or costly (e.g. made-up patients), and they allow larger pools and controlled bugs. Cautions: subjects may take stakes less seriously, face fewer distractions, or click through. Small task changes (e.g. asking questions about the explanation first) can change results greatly. Priming with a scenario may help (pp. 1097–1098).

### 33.5 Discussion: principles
- **No universal mathematical definition of interpretability, and there never will be.** A downstream metric must be defined per context. Other ML areas also lack universal metrics: fairness metrics cannot all be satisfied at once [KMR16], and accuracy, precision and recall differ. Evaluation can still be rigorous if assumptions are precise. Interpretability evaluations often require human input, so experimental-design knowledge is needed (p. 1098).
- **Interpretability is only part of the solution** for fairness, calibrated trust, accountability and causality (goals versus a means) (p. 1098). It is not always needed: a fully formalized goal (a mandated fairness metric), or good behaviour across an exhaustive set of inputs, may not require it (p. 1098). It is needed when human input is needed, e.g. the end-task of checking whether the model is causal, since under many circumstances a model guaranteed to be causal cannot be learned from a dataset alone. Inspection before deployment can also support safety, which tracking harm alone would reveal only after a significant number of patients have been harmed (p. 1099). Complex notions such as accountability need many people and methods (p. 1099).
- **Understand enough to do the end-task, not everything.** Example: listing likely heat sources may suffice for an overheating laptop but not for a freezing one. AlphaGo's move 37 cannot be fully understood, yet partial probes may help a go expert (p. 1099). Interpretability differs from full transparency: staring at every neuron's weights is compared to dismantling a laptop to find a code bug (p. 1099).
- **Partial views are only partial** (e.g. features needed to change a loan decision say nothing about discrimination) (pp. 1099–1100). **They can lack stability and enable attacks.** Overparameterized models can learn to say a feature is unimportant while using it. Joint training can exacerbate this. Inputs can be perturbed to change the explanation while holding the prediction fixed, or vice versa. This motivates translucence, since misread explanations that favor a user's views create false trust (p. 1100).
- **The interpretability–performance trade-off often does not exist** [Rud19]. Simple models can fit surprisingly well (e.g. with high noise) and sparsity regularizers were originally developed to improve performance. Validation metrics may not tell the full story: an interpretable model may reveal confounding, and may enable human override (p. 1100).
- **Human factors are essential** (pp. 1100–1102):
  - *Over-reliance:* any explanation can increase trust. Data scientists over-trusted explanations [Kau+20], and evocative but inaccurate presentations can create a feeling of comprehension [LM20]. Countermeasures: ask for the user's decision first; ask questions about the explanation; show the explanation without the recommendation. Too much effort may lead users to ignore the information (p. 1101).
  - *Misuse:* explanations can manipulate. Users may like simple explanations that do not help their task (p. 1101).
  - *Misunderstanding of ML:* users may not know additive factors or Shapley values and may over-attribute concepts to the model (p. 1101).
  - *Perception:* in Figure 33.6, saliency maps from a trained and a random-prediction network look similar to humans. Multiplying the image by a black-and-clear importance mask makes black objects never appear important, and percentile clipping adds another artifact (pp. 1101–1102).

The authors conclude that interpretable ML cannot be separated from its socio-technical context (p. 1102).

*Intuition note.* The final message is that an explanation is judged by what the user then does with it. The chapter warns that the mere presence of an explanation can raise trust, and that inaccurate but evocative presentations can create a feeling of comprehension (p. 1101).

## Toy example (ours, not from the text)
Take a model $f(t,c)=0.8\cdot[t\ge 60]+0.2\,c$ with label $[f\ge 0.5]$. Here $t$ is temperature and $c$ is cleanliness. Four data points: $(50,0.2),(65,0.4),(70,0.6),(90,0.8)$.

Outputs: $0+0.04=0.04$; $0.8+0.08=0.88$; $0.8+0.12=0.92$; $0.8+0.16=0.96$. Labels: 0, 1, 1, 1.

*Flip-based method* (set a feature to its data min or max; does the label change?).
- Feature $t$ (min 50, max 90): point 1 → $t=90$ gives 0.84, label 1, changed. Point 2 → $t=50$ gives $0.08$, label 0, changed. Point 3 → $t=50$ gives $0.12$, changed. Point 4 → $t=50$ gives $0.16$, changed. Total 4/4.
- Feature $c$ (min 0.2, max 0.8): point 1 → $c=0.8$ gives $0.16$, still 0. Point 2 → $c=0.2$ gives $0.84$, still 1. Points 3 and 4 likewise unchanged. Total 0/4.

*Derivative-based method.* No point lies at $t=60$, so $\partial f/\partial t=0$ at all four points, with sum 0. $\partial f/\partial c=0.2$ at each point, with sum $4\times0.2=0.8$.

The flip method says temperature dominates and the derivative method says cleanliness dominates, for the same model. Which one to trust depends on the property the end-task needs (here fidelity to "what changes the prediction").

## Concepts
- [[interpretability]] (new) — enabling humans to inspect a model so they can do an end-task better; no universal definition; a means to an end (pp. 1074–1075, 1098)
- [[context-and-end-task]] (new) — the setting of use and the user's ultimate goal; they fix metrics and properties (pp. 1075–1076)
- [[downstream-performance]] (new) — the human's end-task performance when given the explanation; the metric for interpretability (p. 1076)
- [[inherently-interpretable-model]] (new) — a model that is its own explanation, needing no extra proxy for the end-task (p. 1079)
- [[post-hoc-explanation]] (new) — a partial view extracted from an already-trained model; the alternative is joint training with a regularizer (pp. 1081, 1084)
- [[local-vs-global-explanation]] (new) — explanation of one input's neighbourhood versus the whole model or a set of inputs (pp. 1082–1083)
- [[explanation-properties]] (new) — computable or human-centred characteristics of an explanation (fidelity, sparsity, completeness, stability, actionability, modularity, interactivity, translucence, simulability, alignment); glue between method and context (pp. 1076, 1086–1088)
- [[faithfulness-fidelity]] (new) — how well a partial explanation matches the model; several operationalizations, e.g. mimic agreement or flip tests (p. 1087)
- [[simulability]] (new) — a user can compute the output from model and input; not the same as compactness (p. 1088)
- [[translucence]] (new) — the explanation states its own limits (p. 1088)
- [[saliency-attribution-map]] (new) — local explanation estimating the importance of each input dimension, e.g. via derivatives (p. 1082)
- [[distillation-mimic]] (new) — train a simple model on a complex model's outputs to mimic it (p. 1080)
- [[explanation-sanity-check]] (new) — hypothesis-based test that tries to produce a phenomenon a working explanation should rule out; can only reveal failure (pp. 1090–1091)
- [[user-study-design]] (new) — baselines (including a placebo explanation), randomization, matching, qualitative and pilot studies (pp. 1095–1097)
- [[over-reliance-on-explanations]] (new) — the presence of an explanation can increase trust beyond what is warranted (p. 1101)

## Canonical instances
- [[lemonade-stand-explanation-example]] — two models, two importance methods, opposite rankings for the same behaviour (pp. 1077–1078)
- [[credit-scoring-blindspot]] — heavy reliance on mortgage payments may suggest poor transfer and prompts a bias check (p. 1074)
- [[randomization-sanity-check-adebayo]] — explanations should change between trained and untrained models; many fail (pp. 1091–1092)
- [[object-background-semisynthetic-test]] — [YK19] datasets with controlled co-occurrence of foreground and background (p. 1092)
- [[patch-add-delete-test]] — adding or deleting top-ranked patches should change accuracy (p. 1093)
- [[alphago-move-37]] — partial probes may help without full understanding (p. 1099)

## Bridges (candidates)
- [structural-analogy] Randomization in user-study design "marginalizes over" confounds ↔ causal inference: randomized assignment makes the assignment mechanism independent of potential outcomes (canon link; not stated in this unit).
- [structural-analogy] Explanations as partial views that can mislead ↔ Bayesian workflow: model checking can reveal misfit but cannot prove a model correct; passing sanity checks likewise shows no blindspots (pp. 1090–1091).
- [metaphor] Downstream performance of the human+explanation ↔ rational analysis: judge a system by how well it serves the goal in its environment.
- [same-math] Shapley-style importance (winning coalitions, p. 1084) ↔ cooperative game theory: the same coalition-based credit allocation the text names (the chapter does not give the formula).

## Questions this raises
- Which concrete properties does a given end-task such as debugging or recourse need, and can they be measured without a user study?
- Given the footnote results that popular methods can fail, which explanation methods retain guarantees?
- How should translucence be built into an explanation so that it states its own limits?
- When user studies are small (e.g. one or two physicists), how can their results be generalized rigorously?

## Reading notes
- Printed = pdf − 34 (pdf 1107 = p. 1073). Text layer was usable. Equations 33.1–33.2 were checked against the page image.
- The first lines of printed p. 1092 ("properties. Their work shows that some methods fail this sanity check.") appear below Figure 33.4 at the top of the running text on that page. The sentence continues from p. 1091.
- Minor typos in the source: "Predication/Action" in a Figure 33.1 box; "e.g.„"; "Fore example"; "interpretion" (p. 1079); "is likely not be enough" (p. 1086). None affect content.
- In Section 33.2.3.1 the subheading "Decision: determining what properties the context needs" is placed under the global-explanation paragraph; I treated it as a separate decision.
- Footnote 1 on p. 1073 is a later addition (it mentions post-publication results); the page footer says "Online version. December 10, 2025".
- The chapter has no exercises.
