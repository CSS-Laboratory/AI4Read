---
id: bender-2020-octopus/main
work: bender-2020-octopus
unit: paper
pages: 5185–5198
fields: [llm]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 18
pipeline_version: 0.1
---
# Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data

## L0 — One line
A system trained only on linguistic form has a priori no way to learn meaning (the link between form and communicative intent), so claims that large LMs "understand" language are overclaims (p. 5185).

## L1 — The gist (≤ 120 words)
Do large neural language models "understand" language? This position paper argues that a system trained only on linguistic form has a priori no way to learn meaning, defined as the relation between form and communicative intent. The authors support this with an "octopus" thought experiment, two constrained thought experiments (Java; English plus unconnected photos), and evidence from child language acquisition and distributional semantics. They conclude that LMs do not learn meaning but learn some useful reflection of it. They recommend precise wording and top-down checks on whether research is climbing the right hill. It matters because, they argue, progress depends on clarity about meaning in task design and reporting.

**Prerequisites:** sets and relations (a subset of a Cartesian product); what a language model is (string prediction); the idea of the Turing test.

## L2 — Key ideas (5–10 bullets)
- **Definitions.** An LM is any system trained only on string prediction. Meaning is the relation between form and communicative intent. The thesis is that form alone does not provide enough signal to learn it (pp. 5185, 5187).
- **Three notions.** Form, conventional (standing) meaning and communicative intent must be kept apart, and intent must not be confused with ground truth (p. 5187).
- **Octopus test.** An octopus that only sees form may be able to act as a chatbot in social talk. It would fail the Turing test when talk must connect to the world, e.g. the bear emergency. The listener does the work of making sense (pp. 5188–5189).
- **Constrained thought experiments.** Java code without inputs and outputs, and English text with unconnected photos, look ridiculous and unfair, but the authors' point is what makes them impossible: grounding is missing from the training data (p. 5190).
- **Child language learning.** Children do not learn from passive exposure; learning relies on interaction and joint attention (p. 5190).
- **Scope.** If form is augmented with grounding data (e.g. perceptual or interaction data), meaning could conceivably be learned to the extent that the intent is represented in that data. The authors say their arguments do not apply to downstream systems trained on tasks whose data include information beyond form (pp. 5191–5192).
- **Right hill.** Fast bottom-up progress does not by itself answer whether we are climbing the right hill. The authors give five diagnostic practices (pp. 5191–5192).
- **Probing and artifacts.** BERT's apparent reasoning on some tasks was found to rest on dataset artifacts. The authors recommend a healthy skepticism towards results that look too good to be true (pp. 5186, 5192).

## L3 — Walkthrough

### Abstract and §1 Introduction (p. 5185)
- Large LMs such as BERT and GPT-2 progress on many tasks, including ostensibly meaning-sensitive ones. Academic and popular pieces claim that they "understand", "comprehend" or learn "meaning". The authors call these overclaims caused by a misunderstanding of how form and meaning relate (p. 5185).
- **Thesis:** because language modeling uses only form as training data, it "cannot in principle" lead to learning meaning (p. 5185).
- **Definitions:** *language model* = any system trained only on string prediction, over characters, words or sentences, sequential or not. *Meaning* = the relation between a linguistic form and communicative intent (p. 5185).
- Human-analogous NLU is called a grand challenge. Large LMs may become components of a solution, but they are "not nearly-there solutions" (p. 5185).
- Roadmap: hype and BERTology (§2), a definition of meaning (§3), thought experiments (§4–5), language acquisition (§6), distributional semantics (§7), research direction (§8), counterarguments (§9) (p. 5185).

### §2 Large LMs: hype and analysis (pp. 5185–5186)
- **Hype in academic writing (examples 1–3).** These include "understands sentence relationships" (BERT paper), "machine comprehension", and "recall factual knowledge". If they are meant to describe human-analogous understanding, comprehension or recall, they are gross overclaims. If they are meant as technical terms, they should be explicitly defined (pp. 5185–5186).
- **Press.** Imprudent terminology feeds AI hype. Two NYT quotes (Marcus, Etzioni) are appropriately careful (examples 4–5). A B2C website and the Google blog post claim BERT "understands" intent (examples 6–7) (p. 5186).
- The authors say it is unclear whether all academic authors separate form from meaning. Part of the imprecision may be that we do not yet fully understand what large LMs implicitly represent (p. 5186).
- **BERTology.** Probing tasks have been used to show that large LMs learn at least some information about English subject-verb agreement, constituent types, dependency labels, NER and core semantic role types. Hewitt and Manning find information analogous to unlabeled dependency structures in ELMo and BERT vectors. Word vectors pick up syntactic and semantic word classes (p. 5186). Footnote 4 notes a caution that probing methodology can influence results (p. 5186).
- **Artifacts.** Niven and Kao: BERT's good performance on the Argument Reasoning Comprehension Task falls to chance when adversarial examples mirror the lexical-cue distribution. McCoy et al.: BERT's MNLI performance is predicated on syntactic overlap heuristics, and falls "significantly below chance" on a dataset designed to frustrate them (p. 5186).
- The apparent "reasoning" is sometimes a mirage built on leveraging artifacts in the training data, i.e. form, not meaning. The authors' own contribution is an argument on theoretical grounds (p. 5186).

*Intuition note.* High scores on a benchmark can come from surface cues in the data. Two cited studies show that balancing the cues or frustrating the heuristics sends BERT to or below chance. A good score alone does not show understanding.

### §3 What is meaning? (pp. 5186–5188)
- **Form** = any observable realization of language: marks on a page, pixels or bytes, movements of the articulators (pp. 5186–5187). **Meaning** = the relation between form and something external to language (p. 5187).
- **§3.1 Meaning and communicative intent.**
  - Humans use language for a communicative intent, e.g. to convey information, request action or socialize (p. 5187).
  - Meaning is the relation $M \subseteq E \times I$, containing pairs $(e,i)$ of expressions $e$ and the communicative intents $i$ they can be used to evoke. *Understand* = the process of retrieving $i$ given $e$ (p. 5187).
  - Intents are about something outside language: the real world, or abstract worlds such as bank accounts, file systems or a hypothetical world (p. 5187).
  - **Conventional (standing) meaning** is what is constant across all contexts of use. It is an abstract object representing the communicative potential of a form. Each linguistic system provides $C \subseteq E \times S$, pairs $(e,s)$ of expressions and conventional meanings (p. 5187).
  - The authors choose no theory of what $s$ looks like. They assume only that conventional meanings must have interpretations, e.g. a means of testing them for truth against a world model. So, like $M$, $C$ connects language to non-language (p. 5187).
  - Footnote 6 abstracts away from the fact that $C$ changes over time and is incompletely shared among speakers (p. 5187).
  - $M$ is best understood as mediated by $C$. The speaker has intent $i$ and chooses an expression $e$ with standing meaning $s$ fit to express $i$ in the situation. The listener reconstructs $s$, then uses knowledge of the situation and hypotheses about the speaker's mind to deduce $i$ (p. 5187).
  - The listener's active role is crucial (Reddy; Clark). Examples: "do a Napoleon" (a pose, hand inside coat flap) and "China trips" (people who recently traveled to China) (p. 5187). Humans also readily attribute intent to signals whose originator could not have it (p. 5187).
  - Intent should not be confused with ground truth, since speakers can be mistaken or dissembling (p. 5187).
  - **Claim:** if training data is only form, there is not sufficient signal to learn $M$ nor $C$ (p. 5187).
- **§3.2 Meaning and intelligence.**
  - Turing: a machine can be said to "think" if a judge cannot distinguish it from a human after arbitrary written conversation. Humans quickly attribute meaning and intelligence to artificial agents, as with ELIZA (pp. 5187–5188).
  - So evaluations must be careful. Searle's Chinese Room: a person who does not speak Chinese answers Chinese questions by consulting books by rules. From outside it seems to understand, but no understanding happens inside (p. 5188).
  - Searle assumes that forms can be manipulated well enough to be indistinguishable from understanding. The authors observe that much recent NLP work claims to build systems where both the runtime system and the process of building it have access only to form (p. 5188).
  - Learning a language requires solving the symbol grounding problem (Harnad). A non-speaker of Chinese cannot learn Chinese word meanings from Chinese dictionary definitions alone (p. 5188).
  - The authors argue that, independently of whether passing the Turing test would mean intelligence, a system trained only on form would fail a sufficiently sensitive test, because it lacks the ability to connect its utterances to the world (p. 5188).

*Intuition note.* Meaning here is a link between words and what speakers want to achieve in the world. A system that has only seen the words never sees one end of that link.

### §4 The octopus test (pp. 5188–5189)
- **Setup.** A and B, fluent English speakers, are stranded on two uninhabited islands and communicate by an underwater telegraph cable. O, a hyper-intelligent deep-sea octopus, taps the cable. O knows no English but detects statistical patterns well. He learns to predict how B responds to A, and notices that some words occur in similar contexts. He has never observed the objects, so he could not pick out a word's referent from physical alternatives (p. 5188).
- O cuts the cable and pretends to be B. This is a weak Turing test, "weak" because A has no reason to suspect a non-human. The question is whether O fails because he has seen only form (p. 5188).
- **Social chat.** The result depends on the task. For trivial daily-life notes with a primarily social function, O may produce new B-like sentences, acting as a chatbot. Internally coherent text suffices (p. 5188).
- **Coconut catapult.** A sends detailed instructions and asks for suggestions. O does not know what "rope" or "coconut" refer to, so he cannot reproduce the experiment. He may treat "mangos and nails" as similarly worded, and reply with a stock compliment because B said that often. A may accept this, but only because A does all the work of attributing meaning (pp. 5188–5189).
- **Bear.** A is chased by a bear and asks B how to build a weapon from sticks. O has no idea what A means. Such a task needs a map between words and real-world entities, plus reasoning and creativity. O would fail the Turing test here, had A not been eaten first (p. 5189). Footnote 7: the authors' GPT-2 test on a bear prompt gave an unhelpful reply; more completions are in Appendix A (p. 5189).
- **Conclusion.** O did not learn meaning. The A–B exchange is a projection of communicative intents through the meaning relation into forms. Without a way to hypothesize and test intents, reconstructing them from form alone is "hopeless". O's language use will eventually diverge from that of an agent grounded in coherent intents (p. 5189).
- O exploited statistical regularities in form. A made sense of O's utterances because agents who produce English usually have intents. A builds the conventional meaning and attributes intent. Reproducing the distribution is not sufficient for meaningful communication (p. 5189).

*Intuition note.* The octopus may get by when the listener does the interpretive work. It fails when the conversation must be tied to things in the world that O has never observed.

### §5 More constrained thought experiments (pp. 5189–5190)
- These isolate the learning of the meaning relation from reasoning. Programming languages are unambiguous and relatively insensitive to execution context, so standing versus speaker meaning matters less (p. 5189).
- **Java.** A Java program $e$, compiled and run on the JVM, is interpreted as a function $i$ from program inputs to outputs. The Java meaning relation is $J \subseteq E \times I$, containing all such pairs $(e,i)$ (p. 5189).
- **Java experiment.** Train any type of LM, for as long as desired, on all well-formed Java code on GitHub. Input is only code: no bytecode, compiler or sample inputs and outputs. Then ask the model to execute a sample program and expect correct output (p. 5189).
- **English experiment.** Train an LM on English text with no independent indication of speaker intent. Also give it many unlabeled photos with no connection to the text. The text task is form prediction, and the image task may be anything involving only images. At test time give an utterance plus a photo (Figure 1), e.g. "How many dogs in the picture are jumping?" or "Kim saw this picture and said 'What a cute dog!' What is cute?" Correct answers are a number or a region of the photo (pp. 5189–5190).
- **Reflections.** The tests are "ridiculous" and unfair, but that is the point. A system that learned the semantics of Java knows how to execute Java. A system that learned the meaning of English can answer questions about things in the world (p. 5190).
- What is interesting is what makes the tasks impossible: what is missing from the training data. Java form without observed inputs and outputs does not include how to execute programs. English form, without acquiring $C$ and without any intent signal, does not include what language-external entities the speaker refers to. So a system trained only on the form of Java or English has "no way" to learn their meaning relations (p. 5190).

### §6 Human language acquisition (p. 5190)
- **Claim examined.** A common reason to think LMs *might* learn meaning is the claim that children acquire language by just listening. The authors say scholarly work does not support this. Learning is grounded in the physical world and in interaction with people (p. 5190).
- **Passive exposure.** Snow et al. note in passing that Dutch-speaking kids who watch German TV by choice do not learn German. Kuhl shows that English-learning infants learn Mandarin phonemic distinctions from brief interactions with a Mandarin-speaking experimenter, but not from Mandarin TV or radio (p. 5190).
- **Joint attention** (child and caregiver attend to the same thing and both know it). Baldwin and others argue it is critical, not interaction alone. Evidence: toddlers whose caregivers "follow into" their attention and label the object have larger vocabularies (Tomasello and Farrar, 15 and 21 months). Toddlers (18–20 months) do not pick up labels uttered from behind a screen but do from someone sharing attention (Baldwin). Gaze following at 10–11 months while vocalizing predicts vocabulary comprehension 7–8 months later (Brooks and Meltzoff) (p. 5190). Footnote 8: the studies do not name the language; it appears to be English (p. 5190).
- **Summary.** Acquiring a linguistic system relies on joint attention and intersubjectivity (being aware of what another attends to and guessing what they intend). "Human children do not learn meaning from form alone and we should not expect machines to do so either" (p. 5190).

### §7 Distributional semantics (pp. 5190–5191)
- Distributional semanticists have long known that grounding is hard. Lexical similarity learned from text does not by itself connect words to the world. Word distributions may also not match the distribution of things in the world (the *four-legged dogs* example) (p. 5190).
- **Routes to grounding.** One route is corpora augmented with perceptual data (photos, other modalities). Another is interaction data such as dialogue corpora with success signals (emotional stress, eye gaze) (pp. 5190–5191).
- Bisk et al. (2020) work out the idea that more information beyond text lets a learner learn more facets of meaning. The authors agree it is an exciting avenue (p. 5191).
- **"Meaning is use".** The authors read this slogan as language used in the real world to convey communicative intents to real people, not as "distribution in a text corpus". Speakers distill past experience into "meaning", and use succeeds if the listener deduces the intent. Standing meanings evolve, and this change may be reflected in changing textual distribution (p. 5191).

### §8 On climbing the right hills (pp. 5191–5192)
- **Downstream systems.** For systems trained on another task (semantic parsing, reading comprehension) using BERT embeddings, the authors' arguments "do not apply". Reading comprehension datasets specify semantic relations between pieces of text, so a sufficiently sophisticated model might learn some aspects of meaning. Also, a pretrained LM's information might help without being meaning itself (p. 5191).
- Even so, one should interpret such findings with caution, given McCoy et al. and Niven and Kao (p. 5191).
- **§8.1 Top-down vs bottom-up.** *Bottom-up*: progress means solving specific research challenges. *Top-down*: the focus is the end goal of a complete, unified theory, which raises doubt whether bottom-up progress leads the right way (p. 5191).
- NLP is in "rapid hill-climbing", with state of the art improved yearly, often through better pretrained LMs. Bottom-up, all is going well. Top-down, the question is whether this is the right hill to climb (p. 5191).
- **History.** The field went through fashion cycles (grammar- and knowledge-based, then statistical, then neural). Each generation felt it was making progress, but serious shortcomings later emerged. The authors say that judgment (that it was not the right hill) can only be made from a top-down perspective. The paper's discussion of what meaning requires is an attempt to bring that perspective into focus (pp. 5191–5192).
- **§8.2 Hillclimbing diagnostics.** One can tell definitively only in hindsight, but five practices are proposed (p. 5192):
  1. Cultivate humility toward language and ask top-down questions. Neural methods are not the first bottom-up success, and will probably not be the last.
  2. Know the limits of tasks. Artificial tasks (bAbI) can help start a field, but their language distribution need not resemble real language. Crowdsourced datasets (the paper calls SQuAD and SNLI "NLI datasets") reflect an unnatural communicative situation. If a system beats inter-annotator agreement, the task "probably" has statistical artifacts. Barbu et al. offer a more realistic-distribution vision dataset.
  3. Value careful creation of new tasks, e.g. DROP, which needs simple arithmetic over different parts of a paragraph (footnote 10 points to Appendix B).
  4. Evaluate across tasks, because standing meaning is task-independent. SuperGLUE seems a good step in this direction.
  5. Analyze both errors and successes. Healthy skepticism and probing tasks can be good ways to find out whether the system performs well for the right reasons.

### §9 Possible counterarguments (pp. 5192–5193)
- **"Meaning doesn't mean what you say."** The working definition is meant to be general: meaning rests on a link between form and something not language. Meaning cannot simply be the relation between form and "deep syntax" (e.g. semantic dependency graphs). Like syntax, such structures could perhaps be learned from form alone. Equating them with meaning ignores that language conveys communicative intents (p. 5192).
- **"Meaning could be learned from …"** If form is augmented with grounding data, meaning can conceivably be learned to the extent that the intent is represented in that data (p. 5192).
  - Some tasks declare certain forms to represent semantic relations. NLI pairs text and hypothesis with "entailed". Control codes or tokens like *tl;dr* prompt LMs to summarize. Together with distributional similarity to phrases like "in summary", this may be enough to bootstrap a successful summarizer (p. 5192).
  - Depending on perspective, one may argue either that such a system finds instances of the relation without understanding the text, or that the declared cues give a signal beyond pure form (pp. 5192–5193).
  - **Java unit tests.** GitHub Java code contains unit tests, which are input–output pairs. A learner could get weak interaction data. This is true, but requires a learner equipped by its developer to identify and interpret unit tests. Such a learner has partial grounding in addition to form (p. 5193).
- **"There is so much form."** Quantity is not relevant: the octopus may observe forever, and the §5 data is unlimited. Without meaning, O would need to memorize infinitely many stimulus–response pairs, because people constantly produce new intents. That may give high scores where perfection is not expected, but "probably" not human-analogous NLU (p. 5193).
- **"Aren't neural representations meaning too?"** They capture some aspects such as semantic similarity, but similarity is "only a weak reflection". Representations are neither standing meanings $s$ (they lack interpretations) nor intents $i$ (insufficient to build the catapult) (p. 5193).
- **Unsupervised MT.** Models trained only with a language-modeling objective on monolingual corpora (Lample et al.) would seem to contradict the conclusion if they reached supervised accuracy. The surprising consequence of the authors' argument would then be that accurate MT does not require understanding the meaning of source or target sentences (p. 5193).
- **"BERT improves meaning-related tasks."** BERT has "probably" learned something about meaning, in the same sense that syntax and semantic similarity capture something: a useful but incomplete reflection. McCoy et al. and Niven and Kao are cautionary tales. What exactly BERT learns is an interesting question for BERTology (p. 5193).

### §10 Conclusion (p. 5193)
- Meaning cannot be learned from form alone. Large LMs such as BERT do not learn "meaning"; they learn "some reflection of meaning into the linguistic form" that is very useful in applications (p. 5193).
- The paper is a call for precise language about model success and for humility toward language. It encourages a top-down view to help pick the right hill (p. 5193).

### Appendix A: GPT-2 on fighting bears with sticks (p. 5197–5198)
- GPT-2 (774M, a demo site) was prompted with "Robinson cried out, 'Help! I'm being chased by a bear! All I have is these sticks. What should I do?' The survivalist said, 'Here's what you can do.'" The first five random completions, with no cherrypicking, were shown. Suggestions included punching the bear and running to the store, taking a gun, and strapping the sticks to the chest and running. Some completions drifted into unrelated text (p. 5197).
- The authors conclude GPT-2 learned which activity words co-occur with bears and sticks, but none of the completions would help A. They think this is because GPT-2 does not know the meaning of the prompt and replies, so it cannot ground them in reality (p. 5197).
- Characters in the prompt matter a lot. Robinson and the survivalist gave the best completions of those tried. With Crocodile Dundee as the character, the reply began with reassurance and then advice to hug the bear and die (p. 5198).

### Appendix B: GPT-2 and arithmetic (p. 5198)
- DROP requires interpretation of language into an external world (arithmetic). GPT-2 completed "Three plus five equals" five times. The completions give "seven", "six", an unrelated continuation, "ten", and "five". The authors say the problem is beyond the current capability of GPT-2 and, they would argue, of any pure LM (p. 5198).

*Intuition note.* The appendix completions fit the thesis: GPT-2 continues the surface pattern of text that mentions bears or sums, but nothing ties the words to a real bear or to quantity.

## Toy example (ours, not from the text)
A tiny count-based "LM" cannot tell two meaning assignments apart.

Corpus (4 sentences, 4 tokens each, 16 tokens in total): "I see a zup", "I see a zup", "I see a wib", "I see a wib".

Bigram counts after "a": zup 2, wib 2. Bigram probabilities: $P(\text{zup}\mid a) = 2/(2+2) = 0.5$ and $P(\text{wib}\mid a) = 2/4 = 0.5$.

Now consider two meaning assignments. Under $M_1$, zup = dog and wib = cat. Under $M_2$, zup = cat and wib = dog. The corpus is the same under both, so every count and probability is identical (0.5 and 0.5). Nothing computed from the forms can say which assignment holds. Resolving it needs a signal from outside the text, e.g. a photo with a label, or someone pointing, as in joint attention.

This is our illustration of why the paper says $M$ and $C$ need a signal beyond form (p. 5187). Real text has asymmetric statistics, so the toy shows only that statistics do not by themselves fix the link to the world. The paper's claim is that the training data contains no such link.

## Concepts
- [[form-vs-meaning]] — form = any observable realization of language; meaning = relation between form and communicative intent (pp. 5185–5187)
- [[language-model]] — here, any system trained only on string prediction, at any granularity and in any order (p. 5185)
- [[symbol-grounding]] — the need to connect symbols to the world; Harnad's dictionary-only Chinese learner cannot learn (p. 5188)
- [[communicative-intent]] (new) — what a speaker wants to achieve with an utterance; about something outside language; not the same as ground truth (p. 5187)
- [[conventional-meaning]] (new) — standing meaning $s$: what is constant across contexts of use; related to forms by $C \subseteq E \times S$ (p. 5187)
- [[meaning-relation-M]] (new) — $M \subseteq E \times I$; pairs of expressions and intents they can evoke; "understand" = retrieve $i$ from $e$ (p. 5187)
- [[joint-attention]] (new) — child and caregiver attend to the same thing and both know it; argued critical for language learning (p. 5190)
- [[bertology]] (new) — the subfield asking what large LMs implicitly represent, using probing tasks (p. 5186)
- [[benchmark-artifacts]] (new) — dataset cues (lexical or syntactic heuristics) that let models score well without the intended reasoning (p. 5186)
- [[top-down-vs-bottom-up]] (new) — bottom-up: success is solving specific challenges. Top-down: focus on the remote end goal (p. 5191)
- [[distributional-hypothesis]] — the paper discusses distribution-based lexical similarity and says it does not itself connect words to the world (p. 5190). It adds the qualifier that "meaning is use" does not mean corpus distribution (p. 5191).

## Canonical instances
- [[octopus-test]] — O taps the A–B cable, may manage social chat, cannot build the catapult, and would fail the Turing test at the bear emergency (pp. 5188–5189)
- [[java-lm-thought-experiment]] — LM trained on GitHub Java with no inputs and outputs cannot execute programs (p. 5189)
- [[english-photos-thought-experiment]] — English text plus unconnected photos cannot answer questions about the photos (pp. 5189–5190)
- [[chinese-room]] — Searle's form-manipulating "system" that appears to understand Chinese (p. 5188)
- [[eliza-effect]] — people formed attachments to ELIZA, attributing meaning to a program (p. 5188)
- [[niven-kao-arct]] — BERT falls to chance on ARCT once the lexical cues are balanced (p. 5186)
- [[mccoy-hans]] — BERT on MNLI relies on overlap heuristics and falls significantly below chance when they are frustrated (p. 5186)
- [[gpt2-bear-prompt]] — GPT-2 completions to the bear prompt are unhelpful (pp. 5189, 5197)
- [[gpt2-arithmetic]] — "Three plus five equals" completions fail (p. 5198)

## Bridges (candidates)
- [structural-analogy] Benchmark artifacts (cues that predict labels without the intended reasoning) ↔ causal inference / social-science measurement: spurious or confounded correlates satisfy the test without the construct — high scores can be "right for the wrong reasons".
- [structural-analogy] A form-only LM versus real human subgroups ↔ silicon samples / algorithmic fidelity: an LM reproduces distributions of forms that people produced, which the paper describes as a reflection of the speakers' communicative intents and the meaning relation.
- [metaphor] "Climbing the right hill" ↔ optimization: local ascent of the current benchmark can be fast without guaranteeing progress toward the goal (a loose analogy).
- [structural-analogy] Meaning as the relation $M \subseteq E \times I$ ↔ measurement validity: a text is an indicator whose link to the underlying intent must be established by outside evidence.

## Questions this raises
- What would count as enough grounding signal? Could the unit tests, control codes or interaction data in §§7 and 9 supply it, and how would one test this?
- Where does the line fall between learning a reflection of meaning (p. 5193) and learning meaning, and what evaluation could tell them apart?
- If unsupervised MT matched supervised MT (p. 5193), would the authors' argument or the premise about MT need to change?
- How can a researcher check that a system performs for the right reasons (p. 5192) beyond error analysis and probing?

## Reading notes
- Printed page numbers (5185–5198) are visible on every page; pdf N = printed − 5184. No offset problem.
- References run from p. 5194 to the top of p. 5197 and are not digested.
- Footnote 7 and Appendices A–B give GPT-2 outputs. The GPT-2 completions are incoherent in places and are cut off mid-sentence in the source itself (e.g. completions end with "The survivalist placed", "You can't").
- §8.2 calls SQuAD "crowdsourced NLI datasets" together with SNLI. The reference list (p. 5196) titles SQuAD as a dataset of questions for machine comprehension of text; I report the body text's wording as written.
- §9 contains the phrase "would seem contradict" (a missing "to") and §9 says "As we argued in §4" about semantic similarity, though §4 does not discuss similarity at length; I left both as printed.
- Intuition notes and the Toy example are my own explanations and are not in the source.
