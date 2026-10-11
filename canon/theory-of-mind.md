---
field: Theory of mind
slug: theory-of-mind
layer: foundation
compiled: 2026-10-11
---
# Theory of mind — Canon

## Scope
Theory of mind (ToM, "mentalizing", "mindreading") is the capacity to explain and predict behaviour by attributing unobservable mental states such as beliefs, desires, intentions, knowledge and perceptions. This canon covers five strands: (a) philosophy of mind and folk psychology (intentional stance; theory-theory vs simulation theory); (b) developmental and comparative psychology (false-belief tasks, infants, apes, autism, two-systems and cultural-evolution accounts); (c) social and cognitive neuroscience of the mentalizing network (TPJ, mPFC); (d) computational ToM (Bayesian inverse planning, the naive utility calculus, Rational Speech Act pragmatics, machine ToM); and (e) a short strand on the current debate over whether large language models have ToM. Empathy and affective contagion, mirror-neuron theories, and clinical autism research are touched on only where they bear on belief attribution. Recursive and level-k reasoning in strategic settings is left to decision and game theory, and appears here only in the Bridges section.

## Canon

### Strand: Philosophy of mind & folk psychology

#### dennett-1987-intentional-stance
- **type:** book
- **citation:** Dennett, D. C. (1987). *The Intentional Stance*. Cambridge, MA: MIT Press (A Bradford Book), xi + 388 pp.
- **tier:** core
- **level:** UG
- **why:** Dennett argues that to have beliefs and desires is to be a system whose behaviour can be reliably predicted by treating it as a rational agent: you take the "intentional stance" instead of the physical or design stance. This is the philosophical root of every rational-agent model of ToM (inverse planning, the naive utility calculus) and of the question of when it pays to treat an LLM "as if" it believes things.
- **focus:** Ch. 2 "True Believers" (first published 1981 as "True Believers: The Intentional Strategy and Why It Works"); the chapter "Three Kinds of Intentional Psychology".
- **access:** need-copy
- **translation:** 『「志向姿勢」の哲学：人は人の行動を読めるのか？』 ダニエル・C・デネット著、若島正・河田学訳、白揚社、1996.
- **verified:** https://ci.nii.ac.jp/ncid/BA01551477 ; chapter: https://en.wikipedia.org/wiki/The_Intentional_Stance ; translation: https://ci.nii.ac.jp/ncid/BN14061698

#### gordon-1986-simulation
- **type:** paper
- **citation:** Gordon, R. M. (1986). Folk psychology as simulation. *Mind & Language*, 1(2), 158–171. doi:10.1111/j.1468-0017.1986.tb00324.x
- **tier:** deep
- **level:** grad
- **why:** This is the founding statement of simulation theory. We predict others not by consulting a tacit theory of mind but by running our own decision-making "offline" on pretend inputs. It sets up the theory-theory vs simulation-theory debate that organized the field for two decades.
- **focus:** whole
- **access:** need-copy
- **verified:** https://doi.org/10.1111/j.1468-0017.1986.tb00324.x

#### gopnik-1992-theory-theory
- **type:** paper
- **citation:** Gopnik, A., & Wellman, H. M. (1992). Why the child's theory of mind really is a theory. *Mind & Language*, 7(1–2), 145–171. doi:10.1111/j.1468-0017.1992.tb00202.x
- **tier:** deep
- **level:** grad
- **why:** This is the strongest developmental case for the "theory-theory". Children's understanding of mind is a genuine causal-explanatory theory that they revise in response to counter-evidence, much like a scientist. It is the ancestor of the "child as Bayesian scientist" programme, and so of the computational strand below.
- **focus:** whole
- **access:** free: http://deepblue.lib.umich.edu/bitstream/2027.42/73444/1/j.1468-0017.1992.tb00202.x.pdf
- **verified:** https://doi.org/10.1111/j.1468-0017.1992.tb00202.x

#### goldman-2006-simulating-minds
- **type:** book
- **citation:** Goldman, A. I. (2006). *Simulating Minds: The Philosophy, Psychology, and Neuroscience of Mindreading*. New York: Oxford University Press. doi:10.1093/0195138929.001.0001
- **tier:** reference
- **level:** grad
- **why:** This is the most thorough book-length defence of simulation theory. It compares simulation with the child-scientist, modularity and rationality theories and brings in neuroscience such as mirroring and empathy. It is the place to see the theory-theory vs simulation-theory debate argued at full depth.
- **focus:** "Philosophical and Scientific Perspectives on Mentalizing" (pp. 3–22); "Conceptualizing Simulation Theory" (pp. 23–52); "The Child-Scientist Theory" (pp. 69–94); "Simulation in Low-Level Mindreading" (pp. 113–146); "High-Level Simulational Mindreading" (pp. 147–191).
- **access:** need-copy
- **verified:** https://api.crossref.org/works/10.1093/0195138929.001.0001 (chapter DOIs 10.1093/0195138929.003.0001–0011)

#### hutto-2025-sep-folk-psychology
- **type:** website
- **citation:** Hutto, D., & Ravenscroft, I. (2025). Folk psychology as a theory. In *Stanford Encyclopedia of Philosophy* (first published 1997; substantive revision 6 Nov 2025). Metaphysics Research Lab, Stanford University.
- **tier:** reference
- **level:** UG
- **why:** This is the up-to-date map of the philosophy. It covers the varieties of theory-theory (modular, scientific, model), eliminativism, simulation theory, mindshaping and the narrative-practice hypothesis. The 2025 revision adds a section on AI and LLMs.
- **focus:** §1 Theory Theory; §2 Varieties of Theory Theory; §4.2 Simulation Theory; §4.6 Mindshaping; §5.3 Artificial Intelligence and LLMs.
- **access:** free: https://plato.stanford.edu/entries/folkpsych-theory/
- **verified:** https://plato.stanford.edu/entries/folkpsych-theory/

### Strand: Developmental & comparative psychology

#### premack-1978-chimpanzee
- **type:** paper
- **citation:** Premack, D., & Woodruff, G. (1978). Does the chimpanzee have a theory of mind? *Behavioral and Brain Sciences*, 1(4), 515–526. doi:10.1017/S0140525X00076512
- **tier:** core
- **level:** UG
- **why:** This paper coined the term "theory of mind". A chimpanzee, Sarah, chose photographs that completed videotaped scenes of a human struggling with problems, which suggested she attributed purposes to the actor. In the published peer commentaries, Dennett, Bennett and Harman pointed out that only a *false* belief would show mental-state attribution unambiguously, and that observation led directly to the false-belief test.
- **focus:** Target article plus the open peer commentaries (especially Dennett's).
- **access:** free: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1E96B02CD9850016B7C93BC6D2FEF1D0/S0140525X00076512a.pdf/div-class-title-does-the-chimpanzee-have-a-theory-of-mind-div.pdf
- **verified:** https://www.cambridge.org/core/product/1E96B02CD9850016B7C93BC6D2FEF1D0

#### wimmer-1983-beliefs-about-beliefs
- **type:** paper
- **citation:** Wimmer, H., & Perner, J. (1983). Beliefs about beliefs: Representation and constraining function of wrong beliefs in young children's understanding of deception. *Cognition*, 13(1), 103–128. doi:10.1016/0010-0277(83)90004-5
- **tier:** core
- **level:** UG
- **why:** This paper turned the philosophers' suggestion into an experiment, the "Maxi and the chocolate" unexpected-transfer task. Most 3-year-olds fail it, and most children pass between about 4 and 6. It created the false-belief paradigm, the standard ToM test for 40 years.
- **focus:** whole
- **access:** need-copy
- **verified:** https://europepmc.org/article/MED/6681741

#### baron-cohen-1985-autism
- **type:** paper
- **citation:** Baron-Cohen, S., Leslie, A. M., & Frith, U. (1985). Does the autistic child have a "theory of mind"? *Cognition*, 21(1), 37–46. doi:10.1016/0010-0277(85)90022-8
- **tier:** core
- **level:** UG
- **why:** This paper introduced the Sally–Anne doll task. Autistic children with relatively high verbal mental age failed it, while children with Down syndrome and typically developing children passed. That suggested ToM is a specific, dissociable cognitive capacity, and the "mindblindness" hypothesis grew from it.
- **focus:** whole (short, 10 pages)
- **access:** need-copy
- **verified:** https://europepmc.org/article/MED/2934210

#### wellman-2001-meta-analysis
- **type:** paper
- **citation:** Wellman, H. M., Cross, D., & Watson, J. (2001). Meta-analysis of theory-of-mind development: The truth about false belief. *Child Development*, 72(3), 655–684. doi:10.1111/1467-8624.00304
- **tier:** deep
- **level:** grad
- **why:** This meta-analysis pools the false-belief literature and finds a robust developmental shift around age 4 that holds across task variants and countries. It is evidence for real conceptual change rather than task artefacts, and the standard empirical anchor for the "explicit" ToM transition.
- **focus:** whole; the results by age, task type and country are the heart of it.
- **access:** need-copy
- **verified:** https://doi.org/10.1111/1467-8624.00304

#### onishi-2005-infant-false-belief
- **type:** paper
- **citation:** Onishi, K. H., & Baillargeon, R. (2005). Do 15-month-old infants understand false beliefs? *Science*, 308(5719), 255–258. doi:10.1126/science.1107621
- **tier:** deep
- **level:** UG
- **why:** In a violation-of-expectation (looking-time) study, 15-month-olds looked longer when an agent searched where the object really was rather than where she falsely believed it was. This launched the "infant false-belief" controversy: either ToM is present long before age 4, or there are two systems (see apperly-2009).
- **focus:** whole
- **access:** free: https://pmc.ncbi.nlm.nih.gov/articles/PMC3357322/
- **verified:** https://europepmc.org/article/PMC/PMC3357322

#### apperly-2009-two-systems
- **type:** paper
- **citation:** Apperly, I. A., & Butterfill, S. A. (2009). Do humans have two systems to track beliefs and belief-like states? *Psychological Review*, 116(4), 953–970. doi:10.1037/a0016923
- **tier:** core
- **level:** grad
- **why:** This paper resolves the infant-vs-4-year-old puzzle with a dual-system account. A fast, efficient but limited system tracks "belief-like states" in infants, animals and adults under load. A slow, flexible, language-dependent system represents beliefs as such. It is the main conceptual frame behind the "implicit vs explicit ToM" literature.
- **focus:** whole
- **access:** free (author's pre-publication manuscript): https://warwick.ac.uk/fac/soc/philosophy/people/butterfill/beliefs_and_belief-like_states.pdf
- **verified:** https://wrap.warwick.ac.uk/17110/

#### apperly-2011-mindreaders
- **type:** book
- **citation:** Apperly, I. (2011). *Mindreaders: The Cognitive Basis of "Theory of Mind"*. Hove: Psychology Press.
- **tier:** core
- **level:** UG
- **why:** This is the best single on-ramp. It goes through the evidence from children, infants and animals, neuroimaging and adults, then builds a cognitive (processing-cost) account of mindreading. It treats ToM as something adults do effortfully and imperfectly, not just as a milestone children pass.
- **focus:** Ch. 1 Introduction; Ch. 2 Evidence from Children; Ch. 3 Evidence from Infants and Non-human Animals; Ch. 5 Evidence from Adults; Ch. 6 The Cognitive Basis of Mindreading.
- **access:** need-copy
- **verified:** https://www.routledge.com/Mindreaders-The-Cognitive-Basis-of-Theory-of-Mind/Apperly/p/book/9780415655583

#### tomasello-2005-shared-intentionality
- **type:** paper
- **citation:** Tomasello, M., Carpenter, M., Call, J., Behne, T., & Moll, H. (2005). Understanding and sharing intentions: The origins of cultural cognition. *Behavioral and Brain Sciences*, 28(5), 675–691; discussion 691–735. doi:10.1017/S0140525X05000129
- **tier:** deep
- **level:** grad
- **why:** This target article argues that what is distinctively human is not just reading intentions but *sharing* them (joint attention, joint goals, collaboration). On this view, shared intentionality is the foundation of language and culture. It moves ToM from a solitary inference problem to a social, coordinative one.
- **focus:** Target article; skim the commentaries.
- **access:** need-copy
- **verified:** https://europepmc.org/article/MED/16262930

#### call-2008-chimpanzee-30-years
- **type:** paper
- **citation:** Call, J., & Tomasello, M. (2008). Does the chimpanzee have a theory of mind? 30 years later. *Trends in Cognitive Sciences*, 12(5), 187–192. doi:10.1016/j.tics.2008.02.010
- **tier:** deep
- **level:** UG
- **why:** This is the authoritative 30-year answer to Premack and Woodruff. Chimpanzees understand others' goals, intentions, perception and knowledge, but there is no evidence that they understand false beliefs. It teaches that ToM is a bundle of separable components, not a single yes/no capacity.
- **focus:** whole
- **access:** need-copy
- **verified:** https://doi.org/10.1016/j.tics.2008.02.010

#### heyes-2014-cultural-evolution
- **type:** paper
- **citation:** Heyes, C. M., & Frith, C. D. (2014). The cultural evolution of mind reading. *Science*, 344(6190), 1243091. doi:10.1126/science.1243091
- **tier:** core
- **level:** UG
- **why:** This review argues that explicit mindreading is culturally inherited and taught through social interaction and language, much as print reading is. Only an implicit "start-up kit" would be genetic. It bears directly on computational social science, because it makes ToM a product of cultural transmission that can vary across populations.
- **focus:** whole
- **access:** need-copy
- **verified:** https://europepmc.org/article/MED/24948740

#### heider-1944-apparent-behavior
- **type:** paper
- **citation:** Heider, F., & Simmel, M. (1944). An experimental study of apparent behavior. *The American Journal of Psychology*, 57(2), 243ff. doi:10.2307/1416950 (end page not confirmed)
- **tier:** deep
- **level:** UG
- **why:** Observers watching a short film of moving triangles and a circle spontaneously described them as agents with goals, emotions and personalities. It is the classic demonstration that mental-state attribution is automatic and driven by motion cues, and the ancestor of every "inverse planning from trajectories" model.
- **focus:** whole
- **access:** need-copy
- **verified:** https://doi.org/10.2307/1416950

### Strand: Social & cognitive neuroscience

#### saxe-2003-tpj
- **type:** paper
- **citation:** Saxe, R., & Kanwisher, N. (2003). People thinking about thinking people: The role of the temporo-parietal junction in "theory of mind". *NeuroImage*, 19(4), 1835–1842. doi:10.1016/S1053-8119(03)00230-1
- **tier:** core
- **level:** UG
- **why:** fMRI showed that the temporo-parietal junction (TPJ) responds selectively to stories about people's beliefs, not to matched "false photograph" stories about outdated physical representations. It established the false-belief vs false-photo localizer and the TPJ as the signature region of the mentalizing network.
- **focus:** whole
- **access:** free: https://saxelab.mit.edu/wp-content/uploads/2018/11/d0997cf0c442ed6b5dd287a3ef9f2dfdb9e1.pdf
- **verified:** https://europepmc.org/article/MED/12948738

#### frith-2006-neural-basis
- **type:** paper
- **citation:** Frith, C. D., & Frith, U. (2006). The neural basis of mentalizing. *Neuron*, 50(4), 531–534. doi:10.1016/j.neuron.2006.05.001
- **tier:** core
- **level:** UG
- **why:** This is a four-page review of the mentalizing network: medial prefrontal cortex, temporo-parietal junction and temporal poles. It separates automatic, low-level mentalizing from deliberate reasoning about others. It is the quickest way to get the neural map in your head. Their longer 2003 review in *Phil. Trans. R. Soc. B* 358:459–473 (free on PMC1693139) is the deeper companion.
- **focus:** whole
- **access:** free: http://www.cell.com/article/S0896627306003448/pdf
- **verified:** https://europepmc.org/article/MED/16701204

### Strand: Computational theory of mind

#### baker-2009-inverse-planning
- **type:** paper
- **citation:** Baker, C. L., Saxe, R., & Tenenbaum, J. B. (2009). Action understanding as inverse planning. *Cognition*, 113(3), 329–349. doi:10.1016/j.cognition.2009.07.005
- **tier:** core
- **level:** grad
- **why:** This paper formalizes Dennett's intentional stance as Bayesian inversion of a rational planning model (an MDP). Observers infer an agent's goal by asking which goal would make the observed path efficient. It closely fits human goal judgments for agents moving in 2-D mazes and is the founding paper of "inverse planning" (cognitive inverse reinforcement learning).
- **focus:** whole; the model section is the payoff.
- **access:** free: https://dspace.mit.edu/bitstreams/dafb0d31-77f9-4708-8f24-f37e1bcb7b04/download
- **verified:** https://dspace.mit.edu/handle/1721.1/60852

#### baker-2017-bdp
- **type:** paper
- **citation:** Baker, C. L., Jara-Ettinger, J., Saxe, R., & Tenenbaum, J. B. (2017). Rational quantitative attribution of beliefs, desires and percepts in human mentalizing. *Nature Human Behaviour*, 1(4), 0064. doi:10.1038/s41562-017-0064
- **tier:** deep
- **level:** grad
- **why:** The Bayesian theory of mind (BToM) model jointly infers an agent's beliefs, desires and percepts with a partially observable MDP (POMDP). In the "food truck" scenario, a student searching for lunch, people's graded inferences about what he wants and what he believes are captured quantitatively. It is the reference implementation of ToM as joint Bayesian inference.
- **focus:** whole
- **access:** need-copy
- **verified:** https://doi.org/10.1038/s41562-017-0064

#### jara-ettinger-2016-naive-utility
- **type:** paper
- **citation:** Jara-Ettinger, J., Gweon, H., Schulz, L. E., & Tenenbaum, J. B. (2016). The naïve utility calculus: Computational principles underlying commonsense psychology. *Trends in Cognitive Sciences*, 20(8), 589–604. doi:10.1016/j.tics.2016.05.011
- **tier:** deep
- **level:** grad
- **why:** This paper proposes that even young children interpret action by assuming agents maximize utility = reward − cost. It unifies inferences about preferences, competence and effort under one principle. It is the bridge between developmental ToM and economic rational-choice models.
- **focus:** whole
- **access:** free: http://hdl.handle.net/1721.1/113204
- **verified:** https://europepmc.org/article/MED/27388875

#### frank-2012-rsa
- **type:** paper
- **citation:** Frank, M. C., & Goodman, N. D. (2012). Predicting pragmatic reasoning in language games. *Science*, 336(6084), 998. doi:10.1126/science.1218633
- **tier:** core
- **level:** UG
- **why:** This one-page paper introduces the Rational Speech Act (RSA) model. Listeners interpret words by reasoning about a speaker who chooses informative utterances, and the speaker reasons about a literal listener. It turns Gricean pragmatics into a recursive Bayesian ToM computation that predicts reference-game data quantitatively.
- **focus:** whole (plus supplementary materials)
- **access:** free: https://langcog.stanford.edu/papers/FG-science2012.pdf
- **verified:** https://europepmc.org/article/MED/22628647

#### goodman-2016-pragmatics
- **type:** paper
- **citation:** Goodman, N. D., & Frank, M. C. (2016). Pragmatic language interpretation as probabilistic inference. *Trends in Cognitive Sciences*, 20(11), 818–829. doi:10.1016/j.tics.2016.08.005
- **tier:** deep
- **level:** grad
- **why:** This is the review of the RSA framework four years on. It extends RSA to scalar implicature, hyperbole, vagueness and other phenomena. It is the best entry point for using RSA-style speaker/listener models in communication research.
- **focus:** whole
- **access:** need-copy
- **verified:** https://europepmc.org/article/MED/27692852

#### rabinowitz-2018-machine-tom
- **type:** paper
- **citation:** Rabinowitz, N. C., Perbet, F., Song, H. F., Zhang, C., Eslami, S. M. A., & Botvinick, M. (2018). Machine theory of mind. In *Proceedings of the 35th International Conference on Machine Learning* (PMLR, Vol. 80, pp. 4218–4227).
- **tier:** deep
- **level:** grad
- **why:** ToMnet is a neural network that meta-learns to predict other agents' behaviour from a few observations. It forms a "character" embedding and a "mental state" embedding, and passes a Sally–Anne-style false-belief test in gridworlds. It is the learned, non-symbolic alternative to Bayesian inverse planning and a precursor to the LLM debate.
- **focus:** whole
- **access:** free: http://proceedings.mlr.press/v80/rabinowitz18a/rabinowitz18a.pdf
- **verified:** https://proceedings.mlr.press/v80/rabinowitz18a.html

### Strand: The LLM theory-of-mind debate

#### kosinski-2024-llm-tom
- **type:** paper
- **citation:** Kosinski, M. (2024). Evaluating large language models in theory of mind tasks. *Proceedings of the National Academy of Sciences*, 121(45), e2405460121. doi:10.1073/pnas.2405460121
- **tier:** deep
- **level:** UG
- **why:** This is the paper that started the debate (preprint arXiv:2302.02083, 2023). Successive GPT models solved more and more hand-written false-belief tasks, reaching child-like performance, which Kosinski reads as ToM-like ability emerging as a by-product of language training. Read it together with ullman-2023 for the critique.
- **focus:** whole
- **access:** free: https://pmc.ncbi.nlm.nih.gov/articles/PMC11551352/
- **verified:** https://europepmc.org/article/MED/39471222

#### ullman-2023-trivial-alterations
- **type:** paper
- **citation:** Ullman, T. (2023). Large language models fail on trivial alterations to theory-of-mind tasks. arXiv:2302.08399 [cs.AI].
- **tier:** deep
- **level:** UG
- **why:** Small, logically decisive changes to the standard vignettes, such as a transparent container or a protagonist who was told the truth, flip the model's answers. This suggests pattern-matching rather than belief tracking. It is also a methodological argument: treat "AI passes test X" with the default scepticism used for animal and infant claims.
- **focus:** whole (short)
- **access:** free: https://arxiv.org/pdf/2302.08399
- **verified:** https://arxiv.org/abs/2302.08399

#### strachan-2024-llm-humans
- **type:** paper
- **citation:** Strachan, J. W. A., Albergo, D., Borghini, G., Pansardi, O., Scaliti, E., Gupta, S., Saxena, K., Rufo, A., Panzeri, S., Manzi, G., Graziano, M. S. A., & Becchio, C. (2024). Testing theory of mind in large language models and humans. *Nature Human Behaviour*, 8(7), 1285–1295. doi:10.1038/s41562-024-01882-z
- **tier:** core
- **level:** UG
- **why:** This is the most careful human-vs-LLM comparison: a full battery (false belief, irony, hinting, strange stories, faux pas) with large human samples and follow-up manipulations. It finds uneven, task-specific profiles, for example faux-pas failures that partly reflect hyper-conservative answering rather than missing inference. It is a model of how to run psychometrics on LLMs.
- **focus:** whole
- **access:** free: https://pmc.ncbi.nlm.nih.gov/articles/PMC11272575/
- **verified:** https://europepmc.org/article/MED/38769463

#### shapira-2024-clever-hans
- **type:** paper
- **citation:** Shapira, N., Levy, M., Alavi, S. H., Zhou, X., Choi, Y., Goldberg, Y., Sap, M., & Shwartz, V. (2024). Clever Hans or neural theory of mind? Stress testing social reasoning in large language models. In *Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 2257–2273). St. Julian's, Malta: ACL. doi:10.18653/v1/2024.eacl-long.138
- **tier:** deep
- **level:** grad
- **why:** This paper stress-tests LLMs across many ToM tasks and adversarial variants. It concludes that apparent successes often rest on shallow heuristics ("Clever Hans") rather than robust ToM, and argues against using standard psychological tests as-is to evaluate LLMs. It is the NLP-side counterpart to ullman-2023.
- **focus:** whole
- **access:** free: https://aclanthology.org/2024.eacl-long.138.pdf
- **verified:** https://aclanthology.org/2024.eacl-long.138/

## Concept spine
- **theory of mind / mentalizing / mindreading** — attributing unobservable mental states (beliefs, desires, intentions) to explain and predict behaviour (HS)
- **folk psychology** — the everyday belief–desire framework people use to make sense of each other (UG)
- **intentional stance** — predicting a system by treating it as a rational agent with beliefs and desires appropriate to its situation (UG)
- **physical / design stance** — Dennett's alternative strategies: predict from physics, or from what the system was designed to do (UG)
- **propositional attitude** — a mental state that relates an agent to a proposition ("believes that p", "wants that p") (UG)
- **intentionality** — the "aboutness" of mental states: they represent something, possibly something false or non-existent (UG)
- **referential opacity** — inside "believes that…", substituting co-referring terms can change truth value; a mark of representing a representation (grad)
- **theory-theory** — ToM is a tacit, causal-explanatory theory of mind, learned or revised like a scientific theory (UG)
- **simulation theory** — ToM works by running one's own cognitive machinery offline on pretend inputs (UG)
- **hybrid accounts** — mindreading uses both theory-like inference and simulation, depending on task (grad)
- **modularity (ToMM)** — an innate, domain-specific mechanism dedicated to computing mental states (grad)
- **mindshaping** — folk psychology works partly by shaping people to be predictable, not only by describing them (grad)
- **first-order false belief** — understanding that someone holds a belief that differs from reality (HS)
- **second-order false belief** — understanding beliefs about beliefs ("John thinks that Mary thinks…") (UG)
- **unexpected transfer task** — an object is moved while the protagonist is absent; where will they look? (HS)
- **unexpected contents task** — a familiar container holds something unexpected; what will someone else think is inside? (HS)
- **reality bias / curse of knowledge** — the pull of one's own true knowledge when judging others' beliefs (UG)
- **age-4 transition** — the robust shift from failing to passing explicit false-belief tasks around age 4 (UG)
- **violation-of-expectation paradigm** — infants look longer at events that contradict their predictions; used to probe implicit ToM (UG)
- **implicit vs explicit ToM** — spontaneous, non-verbal belief tracking vs deliberate, verbally reportable belief reasoning (grad)
- **two-systems account** — an efficient-but-limited system tracks belief-like states; a flexible-but-costly system represents beliefs as such (grad)
- **perspective-taking (level 1 / level 2)** — knowing *what* another can see vs *how* it looks to them (UG)
- **knowledge vs ignorance attribution** — tracking who has seen what, a simpler capacity than false-belief attribution (UG)
- **joint attention** — two agents attending to the same thing and knowing they both are (UG)
- **shared intentionality** — the capacity to form joint goals and intentions with others; claimed to be uniquely human (grad)
- **mindblindness** — the hypothesis that autism involves a specific deficit in attributing mental states (UG)
- **cultural evolution of mindreading** — explicit ToM is a culturally transmitted skill, like literacy (grad)
- **mentalizing network** — brain regions reliably engaged by mental-state reasoning: TPJ, mPFC, precuneus, temporal poles (UG)
- **temporo-parietal junction (TPJ)** — cortical region, especially the right TPJ, selectively engaged when representing others' beliefs (UG)
- **false-belief vs false-photograph contrast** — fMRI localizer separating belief representation from representation in general (grad)
- **rational-agent assumption / principle of efficiency** — agents take the most efficient means to their goals; the core constraint for inferring goals (UG)
- **inverse planning** — inferring goals and beliefs by inverting a model of rational planning with Bayes' rule (grad)
- **Bayesian theory of mind (BToM)** — joint Bayesian inference over beliefs, desires and percepts given observed actions (grad)
- **POMDP** — partially observable Markov decision process: planning under uncertainty about the world state, used to model agents with beliefs (grad)
- **inverse reinforcement learning** — recovering a reward function from observed behaviour; the ML twin of inverse planning (grad)
- **naive utility calculus** — the intuitive assumption that agents maximize rewards minus costs (UG)
- **Boltzmann (softmax) rationality** — agents choose actions with probability proportional to exp(β × utility); "noisy" rational choice (grad)
- **Rational Speech Act (RSA)** — pragmatics as recursive reasoning between a speaker and a listener who model each other (grad)
- **literal listener / pragmatic speaker / pragmatic listener** — the three levels of the RSA recursion (grad)
- **scalar implicature** — inferring "not all" from "some" because a cooperative speaker would have said "all" (UG)
- **recursive mindreading / orders of intentionality** — nested mental states ("I think you want me to believe…") (UG)
- **machine theory of mind** — an AI system that models other agents' behaviour and mental states, learned or engineered (grad)
- **Clever Hans effect** — apparent competence that actually exploits superficial cues in the test (UG)
- **construct validity in LLM evaluation** — whether passing a human-designed test measures the same capacity in a model (grad)
- **data contamination** — test items, or close variants, appearing in a model's training data (UG)

## Canonical instances
- **Premack's chimpanzee Sarah** — Sarah chooses photos completing videos of a human struggling to reach bananas or escape a cage, read as attributing purpose — premack-1978-chimpanzee
- **Dennett's false-belief proposal** — a BBS commentary arguing that only an agent's *false* belief cleanly tests mental-state attribution — premack-1978-chimpanzee
- **Maxi and the chocolate** — Maxi doesn't see his chocolate being moved; children must say where he will look — wimmer-1983-beliefs-about-beliefs
- **Sally–Anne task** — Sally's marble is moved to Anne's box while Sally is out; autistic children disproportionately failed — baron-cohen-1985-autism
- **Unexpected contents (deceptive container)** — a candy box contains pencils; predict another person's belief about the contents; one of the task families in the meta-analysis — wellman-2001-meta-analysis
- **Infant violation-of-expectation false belief** — 15-month-olds watch an actor hide a toy watermelon slice in a green or yellow box, and look longer when her search conflicts with her (false) belief — onishi-2005-infant-false-belief
- **Heider–Simmel animation** — moving triangles and a circle are spontaneously narrated as bullying, chasing and rescuing — heider-1944-apparent-behavior
- **False-belief vs false-photograph localizer** — belief stories vs outdated-photo stories isolate the TPJ — saxe-2003-tpj
- **2-D maze goal inference** — participants judge an agent's goal as its path unfolds; fit by Bayesian inverse planning — baker-2009-inverse-planning
- **The food-truck task** — a student searches for a preferred food truck behind a wall; people infer what he wants and what he believed was there — baker-2017-bdp
- **RSA reference game** — given a one-word utterance and a small set of objects differing in shape and colour, which object does the speaker mean? — frank-2012-rsa
- **ToMnet Sally–Anne in gridworld** — a network predicts where an agent will go after a swap it did not observe — rabinowitz-2018-machine-tom
- **Transparent-bag alteration** — the unexpected-contents vignette is changed so the container is transparent, and LLM answers break — ullman-2023-trivial-alterations
- **Faux pas test on LLMs** — models fail to commit to the inference that a speaker didn't know, which partly reflects hyper-conservatism — strachan-2024-llm-humans

## Bridges
- [same-math] inverse planning / BToM ↔ Bayesian theory & causal inference: Bayes' rule — goal inference is literally P(goal | actions) ∝ P(actions | goal) · P(goal), with a planner as the likelihood.
- [same-math] Boltzmann-rational agent and RSA speaker ↔ decision & game theory: logit / Luce choice rule — the softmax over utilities with rationality β is the same equation as the logit quantal-response choice rule.
- [same-math] RSA speaker informativity ↔ information theory: surprisal — the RSA speaker's utility is log P_L0(world | utterance), the negative self-information (surprisal) under the literal listener.
- [structural-analogy] recursive mindreading (RSA levels, second-order belief) ↔ decision & game theory: level-k / cognitive hierarchy — both stack bounded recursions of "I model you modelling me", anchored at a non-strategic level-0.
- [structural-analogy] beliefs about beliefs ↔ decision & game theory: common knowledge and belief hierarchies — false-belief tasks probe one rung of the infinite belief hierarchy that game theory formalizes.
- [structural-analogy] naive utility calculus / inverse planning ↔ economics & finance: revealed preference — inferring hidden utilities from observed choices under a rationality assumption (the economist's inverse-planning problem).
- [structural-analogy] intentional stance ↔ analytic philosophy: Davidson's radical interpretation and the principle of charity — beliefs are whatever attributions make the agent come out most rational.
- [structural-analogy] RSA pragmatics ↔ communication theory: Gricean cooperative principle and audience design — RSA is a quantitative formalization of the speaker who tailors messages to the receiver's inferred state.
- [structural-analogy] LLM ToM evaluation ↔ LLMs: shortcut learning, benchmark contamination and construct validity — the Clever Hans critique is the same validity problem as other LLM capability claims.
- [metaphor] cultural evolution of mindreading ↔ complex systems: cumulative cultural evolution — ToM as a socially transmitted "cognitive gadget" whose distribution can drift across populations.
