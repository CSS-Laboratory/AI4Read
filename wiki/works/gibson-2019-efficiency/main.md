---
id: gibson-2019-efficiency/main
work: gibson-2019-efficiency
unit: paper
pages: 1-19
fields: [information-theory]
level: UG
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 8
pipeline_version: 0.1
---
# How Efficiency Shapes Human Language (Gibson, Futrell, Piantadosi, Dautriche, Mahowald, Bergen & Levy, 2019)

## L0 — One line
Across the lexicon, syntax and morphology, many features of human languages fit the idea that languages are shaped by a pressure for efficient communication, balanced against how complex and learnable they are.

## L1 — The gist (≤ 120 words)
The review asks why languages look the way they do, and whether recurring patterns can be explained by communicative efficiency. Efficiency means successful communication with little average effort, usually short messages. The authors use information-theoretic tools (surprisal, entropy, mutual information). They argue that ambiguity is not a counter-argument, because context usually resolves it. They then collect evidence: word length tracks predictability in context, kinship and colour words, dependency locality, word order, and the trade-off between morphology and fixed word order. Efficiency is traded off against complexity and learnability (compositionality, iconicity). They end with open problems: measuring complexity, choosing null baselines, estimating quantities, and modelling utility and change.

**Prerequisites:** logarithms and probability; the idea of a code with message lengths; very basic sentence structure (subject, verb, object; head and dependent).

## L2 — Key ideas (5–10 bullets)
- Efficiency is defined from information theory: a code is efficient if communication succeeds with little average effort, usually short signals (pp. 3–4). Language is treated as a code from speaker to listener. The tools are surprisal (the negative log probability of an event), entropy (average surprisal, i.e. uncertainty) and mutual information (how much knowing one variable tells about another) (p. 4).
- Ambiguity out of context is not evidence against efficiency. Context usually resolves it, so leaving out inferable information makes speech shorter (p. 5).
- Optimal signal length depends on probability in context, not raw frequency. In corpora, 3-gram predictability (how predictable a word is from the two previous words) correlates with word length more strongly than frequency does, in the languages tested (pp. 5–6, Fig. 2).
- Word-meaning systems are described as trade-offs between informativeness and complexity. Kinship systems lie near the Pareto frontier (the range of optimal trade-offs), and colour naming is analysed through perceptual structure and communicative need (pp. 6–8).
- Languages tend to keep words that are linked in a head–dependent relation close together (dependency locality) in 37 languages (50 in a replication). Information locality (words with high mutual information should be close) is a proposed generalisation of it (pp. 9–10, Fig. 4).
- Word order and morphology appear to trade off. Redundant marking such as grammatical gender may help processing like parity bits (redundancy in a code that makes the signal robust to noise), but this is speculative (pp. 10–11).
- Learnability pressures interact with efficiency. Compositionality (the meaning of a larger form is a predictable function of its parts) may arise from cultural transmission, and the lexicon is less arbitrary (form less unrelated to meaning) than assumed (pp. 11–14).
- Open problems: complexity measures, null baselines (counterfactual comparison languages), data needs, utility (e.g. taboo), population differences, historical change (pp. 14–15).

## L3 — Walkthrough

### Introduction: "Why Do Languages Look the Way they Do?" (pp. 1–2)
- There are 6000–8000 languages, yet linguists document strong recurring patterns across them (p. 1). These **language universals** may be exceptionless or strong statistical tendencies (p. 1). The paper reviews attempts to explain some of them within a framework where languages must offer **communicative efficiency** under information-processing and learning constraints (p. 1).
- Traditional theories de-emphasised efficiency, mainly because of ambiguity at all levels of structure (p. 1). Recent information-theoretic analyses show ambiguity is "actually not a problem" in use, because context usually disambiguates [14] (p. 1).
- Large corpora and NLP tools now allow quantitative tests (p. 1). A language's utility can be seen as both learnability (or complexity) and efficiency of use (p. 1).
- The authors claim that across levels, from words to syntax, language form shows a strong tendency to be structured for efficient use (p. 1). The plan is: definitions, ambiguity, the main evidence, balance with complexity/learnability, and challenges (p. 2).

**Box 1 (methods), p. 2.**
- *Corpora*: naturalistic text, annotated for word boundaries, morphology and syntax. Efficiency must be judged against the distribution of messages speakers intend and the forms learners hear (p. 2). Dictionaries are used for semantic-space work (p. 2).
- *Single-language analysis*: rare constructions, e.g. locative inversion ('Onto the table jumped the cat'), still reveal properties of the grammar (p. 2).
- *Typological databases*: information is available for thousands of languages, but is very limited for most (p. 2).
- *Experiments*: they collect dense data on rare structures, deconfound correlated factors, and allow interventions. Artificial languages test learnability and iterated transmission (p. 2).
- *Computational models*: they check informal proposals, estimate quantities from corpora, compare real languages with counterfactual simulated ones, and simulate transmission across generations (p. 2).

### What is Communicative Efficiency? (pp. 3–4)
- **Information-theoretic picture (Fig. 1, p. 3):** an information source selects a message, a sender encodes it into a signal, the signal travels through a channel (with noise) to a receiver, which decodes it for the destination. Success means the recovered message equals the source message, or differs only slightly (p. 3).
- **Efficiency** = successful communication with minimal average effort by sender and receiver. Effort is typically quantified as message length, so signals are short on average while communicative success is maximised (p. 3).
- **Source coding** = choosing a code that makes signals short on average, given the distribution of messages from the source (p. 3).
- For language: speaker = source and sender, utterance = signal, listener = receiver and destination. Languages are codes sent through the acoustic or visual channel. The view is usage-based, since efficiency depends on which messages we often want to send (p. 3).
- **Noise** covers anything that introduces error (noisy rooms, speech errors, inattention) (p. 3). A code that works despite noise is **robust**. **Channel coding** = choosing a code for communication in the presence of noise, given the channel's characteristics (p. 3).
- The theory is agnostic about the form and content of messages. From the information-theoretic perspective, all that matters is that messages are transmitted accurately (p. 4). It was developed for telecommunications and cryptography, and has been applied in neuroscience, complexity theory and models of action under information constraints (pp. 4–5). Estimating entropy from language data is now possible with large datasets and computing power (p. 5).

**Box 2 (fundamental concepts), p. 4.**

Surprisal of a discrete event $x$ (base $k$; the paper then assumes $k=2$, so units are bits):
$$h(x)=\log_k \frac{1}{p(x)} \tag{I}$$
Base 10 gives bans; the natural log gives nats. Information content approximates the length of the shortest uniquely decipherable code for $x$ over an alphabet of $k$ letters (p. 4).

Entropy of a random variable $X$ is the average surprisal; it is the degree of uncertainty about $X$ and is non-negative:
$$H[X]=\sum_x p(x)\log\frac{1}{p(x)} \tag{II}$$

Conditional entropy is the uncertainty remaining about $X$ after learning $C$:
$$H[X\mid C]=\sum_x\sum_c p(x,c)\log\frac{1}{p(x\mid c)} \tag{III}$$
It satisfies $0\le H[X\mid C]\le H[X]$ for all $X, C$. The authors say this fact is key to the proof of the utility of ambiguity in [14] (p. 4).

Mutual information is the shared information content of two variables:
$$I[X:C]=H[X]-H[X\mid C] \tag{IV}$$
It tells how many bits you gain about $X$ on average on learning $C$. It is symmetric and non-negative:
$$I[X:C]=I[C:X]\ge 0 \tag{V}$$

Success may require exact equality of message, or only approximate equality. The study of efficiency under approximate equality is **rate–distortion theory**: rate is the information sent through the channel; distortion measures how far the reconstruction diverges from the intended message (p. 4).

*Intuition note.* Surprisal says rare events carry more bits. Entropy averages that. Conditional entropy says how much uncertainty is left once context is known, and it can never be larger than the uncertainty without context. The paper calls this fact key to the proof that ambiguity can be useful [14] (p. 4).

### The Existence of Ambiguity Out of Context (p. 5)
- **Chomsky's view (as reported):** ambiguity is a hallmark of an inefficient system because it permits confusion, so language is not "designed" for communication but for other functions, perhaps thinking [13] (p. 5). The authors add that it is unclear why one would design an ambiguous system [25] (p. 5).
- **Authors' resolution:** to a first approximation, context resolves all communicatively relevant ambiguity [26], even for children [27]. In conversation, participants can query each other to clear up residual uncertainty [28] (p. 5).
- Ambiguity thus becomes desirable: leaving out what context makes inferable gives more concise speech. This "can be proven rigorously in information theory" [14] (p. 5). Legal contracts and programming languages, which aim at zero ambiguity, become wordy or pedantic. The extra effort of unambiguity out of context would be wasted in ordinary use (p. 5).

### Evidence of communicative efficiency (pp. 5–11)

#### The Lexicon: word length (pp. 5–6)
- The lexicon is the set of words a speaker knows; an average American adult is estimated to know about 40 000 (p. 5).
- **Zipf's law (as stated):** more frequent words tend to be shorter ('the' vs 'accordion'). Morse code does the same ('e' is a single dot) (p. 5). This shortens the average message (p. 5).
- But Zipf predates information theory. In an optimal code, signal length depends on probability in context, not overall frequency [30] (p. 5). Example: if context says the British can land in only two ways, Paul Revere needs a one-bit message (one or two lights) (p. 5).
- **Refined prediction:** if language is efficient, word length should depend on predictability in context more than on frequency. Predictable words should be even shorter than frequency predicts (pp. 5–6).
- **Evidence:** a word's probability in context in a corpus was a stronger determinant of its length than its overall frequency, in a variety of languages [32] (p. 6). Fig. 2 plots correlations with length for 3-grams (predictability from the two previous words); predictability correlations are higher than frequency correlations across languages (p. 6).
- The authors say this pattern "likely reflects" lexicalisation of processes that shorten predictable words in production and in historical change (p. 6). In production, Mahowald et al. [33] found speakers more likely to choose the short form of a near-synonym pair ('chimp'/'chimpanzee') in a predictive context than in a neutral one (p. 6).

*Intuition note.* A word that context already makes guessable needs few bits, so a short form is cheap. Raw frequency only partly captures this.

#### Partitioning of semantic space (pp. 6–8)
- Research on why languages have the words they do covers kinship, colour, spatial relations and numerals (p. 6). The efficiency idea: lexica balance (i) **informativeness** (how well words support relevant distinctions) against (ii) **complexity** (how well the system can be represented and learned) [17,44,45] (p. 6).
- **Kinship:** Kemp and Regier [46] found that kinship systems of all the world's languages lie near the **Pareto frontier** (the range of optimal trade-offs) between informativeness and complexity (p. 6; Fig. 3A shows communicative cost against complexity). Example: Swedish has unique words for all four grandparents. This removes the maternal/paternal ambiguity of 'grandmother' and 'grandfather', but increases complexity (p. 6).
- By this analysis, these systems could not be made more useful without more complexity, nor simpler without communicative cost (p. 6).
- **Colour, perceptual structure:** colour term inventories range from two or three (like black, white, red) to about 12 (p. 6–7). The communicativity of a language's colour words is "partially optimized" according to perceptual properties of colour (CIELAB space) in the World Color Survey (p. 7). When culture needs a new term, the partition is driven by the shape of the perceptual space, which would explain similar partitions in unrelated languages (p. 7).
- **Colour, usefulness for objects [56,57]:** a colour score for a colour chip and label is a product of (i) a *production factor* (how likely a person is to use that label for that colour) and (ii) a *comprehension factor* (how hard it is for a listener to pick the right colour given the label; many colours under one word means high difficulty). The difficulty is formally the surprisal of the colour given the word (p. 7). Summing the scores over labels gives the average colour score. The text describes it as the optimal number of yes–no guesses a listener needs, i.e. the bits needed to convey the chip (p. 7).
- **Result:** all languages convey warm colours (yellow, red, orange, brown) with fewer bits than cool colours (blue, green) (p. 8; Fig. 3B). Objects tend to be warm-coloured and backgrounds cool-coloured (Fig. 3C, p. 8).
- This suggests a causal story: people invent words to describe objects, not backgrounds, so colour words may enter the space by usefulness in discriminating objects (p. 8). On this hypothesis all languages share perceptual structure, and what differs is how useful categories are in a culture, which can change (p. 8). Supporting evidence: Hadza [59] and Tsimane' [57] have colour term structure similar to industrialised languages despite relatively low total information in the World Color Survey (p. 8).

*Intuition note.* Word meanings are treated like a code that must be both precise enough to be useful and simple enough to learn. The same pressure on different cultures may give similar solutions.

#### Syntax (pp. 8–10)
- **Dependency syntax** records only how words combine to give a sentence's meaning, with a link from a head to its dependent. In 'The woman saw the red car', 'red' depends on head 'car', not 'woman' (p. 8). Heads can mostly be identified in a relatively theory-neutral way, so the work is robust to many syntactic assumptions (p. 8). Efficiency studies ask whether word order and morphology make recovering the dependency structure easy and accurate (p. 8).

**Order of subject, verb and object (pp. 8–9).**
- Across languages the most common orders are SOV, then SVO, with VSO a distant third (p. 8). English is SVO (p. 8).
- *Uniform information density (UID)*: the information of an utterance per unit time should be roughly constant. Maurits et al. [72], using co-occurrence statistics for a small set of subjects, verbs and objects, argue that SVO gives the most uniform information profile, followed by SOV and VSO (p. 8).
- *Noisy-channel theory*: the receiver may get a version with a word deleted. SVO more robustly shows which noun is subject and which object when they are confusable (p. 9).
- SOV may be favoured by more general, not fully understood cognitive biases: it is preferred in emergent sign languages and ad hoc gesture, though not strictly (p. 9). The noisy-channel theory suggests SOV languages need another strategy. They usually have morphological case marking [80], and in gesture the preferred order switches to SVO when subject and object are confusable (p. 9).

**Dependency locality (pp. 9–10).**
- Theory: the linear distance between linked words (dependency length) should be as short as possible. This reduces working-memory difficulty in incremental production and comprehension and is part of the effort of sending and receiving (p. 9). Fig. 4A shows English sentences with total dependency lengths 6, 7, 14 and 20. Sentence 4 sounds notably awkward, in part because of its long link between 'threw' and 'out'. Long dependencies cause measurable online comprehension difficulty (p. 9).
- It offers a unified account of: harmonic word-order correlations (and certain exceptions); the preference for short-before-long constituents in languages such as English, and the reverse in Japanese; and possibly the rarity of crossing links (p. 9).
- *Evidence:* Futrell et al. [87] found dependency length in hand-parsed corpora of 37 languages is minimised relative to several random baselines (p. 9). Fig. 4B is a replication on 50 languages; average observed length is below the random baseline as sentences get longer (p. 10). A locality bias also emerges in artificial language learning [102], suggesting it may act causally via learning biases (p. 9).
- *Information locality:* assuming comprehenders' memory for context is noisy, one can derive that words with high mutual information should be close [108] (p. 9). Heads and dependents are word pairs with especially high mutual information, so dependency locality becomes a special case. It extends to all statistical dependencies and might thus explain, for example, adjective-ordering preferences (pp. 9–10).

*Intuition note.* Keeping related words near each other lowers the memory effort of holding one word until its partner arrives. Information locality says the same for any pair of words that predict each other strongly.

#### Morphology (pp. 10–11)
- Morphology is the way wordforms change to express meaning gradations (e.g. English plural '-s') (p. 10).
- **Trade-off with fixed word order:** a language can encode dependency structure in fixed word order (English) or in morphology (case marking or agreement) (p. 10). The efficiency prediction: with fixed order, dependency-marking morphology is redundant; with morphology, order is free to convey other things such as information structure. So marking should trade off with fixed order (p. 10).
- Evidence: an information-theoretic measure of word-order freedom correlates negatively with morphological marking in dependency-parsed corpora for certain dependency structures [117], and there is a trade-off between word order and word-internal information [118]. It also emerges in artificial language learning [119] (p. 11).
- A possible additional factor: languages with more second-language speakers tend to disprefer morphology [120,121], possibly because morphological rules are harder for second-language learners (p. 11).
- **Redundancy:** languages often redundantly mark apparently irrelevant properties, e.g. gender on inanimate nouns, often nearly arbitrary (p. 11). A proposal: such marking eases processing. Nouns are the hardest word class [123]; effort is linked to predictability; gender marking reduces uncertainty about a noun's identity [124]. Languages without gender may use redundant prenominal adjectives [125]. Such marking may act like parity bits, giving redundancy that makes the signal robust to noise (p. 11).
- Arbitrariness of gender could be a feature: if gender markers were fully predictable, they would not give unique information about nouns [124]. The most useful system might be a random mapping, but that is complex to learn and use, so a complexity–efficiency trade-off may exist (p. 11). The authors say a causal role for efficiency in noun–gender mapping "remains speculative" (p. 11).

### How Learnability Interacts with Efficiency (pp. 11–14)
- **Learnability vs UG (pp. 11–12).** Traditional generative theories stressed that some languages may be unlearnable without strong innate principles [126], but had difficulty explaining the range of variation [12,127] (p. 11). Newer arguments say systems differ in complexity, more complex ones being harder to learn but not impossible, [128,129]; universals then follow if simpler systems are preferred [45,130] (p. 11). In typical UG theories, compatibility with UG decides learnability. The efficiency view is graded: among learnable languages, more complex ones are harder to learn, a general property of algorithmic and statistical learning theories (p. 12).
- **Compositionality (p. 12).** Why do sentences consist of words in dependency trees? Learners' experience is extraordinarily sparse compared with the meanings they may need. Frequent meanings can be learned holistically ('Hello'). Language is compositional: smaller meaningful forms combine into larger forms whose meaning is a predictable function of the parts (p. 12). Two accounts: a strong inductive bias for compositional systems (maybe a side effect of evolution [134], or selected directly [135]); or a usage-based account in which languages became compositional through selection at the cultural transmission bottleneck [136–138]. The authors say that even a noncompositional system learnable from enough evidence could not survive generations, due to input sparsity for any individual learner (p. 12).
- **Iconicity and systematicity (pp. 12–14).** Since Saussure, form–meaning relations are seen as arbitrary ('shoe' means footwear in English, cabbage in French). Arbitrariness lets speakers coin words freely but poses an acquisition problem: any use of 'shoe' fits many meanings [140] (p. 12). But evidence suggests less arbitrariness than thought, in spoken and signed languages (p. 12).
  - Dautriche et al. [149] compared four lexicons with 30 simulated lexicons generated from phonotactic and articulatory information only. Fig. 5: all four languages (Dutch, English, French, German) have significantly more minimal pairs than the simulated baseline. Similar results appeared on other clustering measures (p. 13). Natural lexicons therefore use a smaller part of the phonological space allowed by their phonotactics (pp. 12–13).
  - *Iconicity* = sounds or signs that intrinsically match meanings (e.g. vowel contrasts and magnitude). *Systematicity* = language-specific correlations, such as stressed back vowels in English nouns ('school') vs front vowels in verbs ('meet'), or phonesthemes 'gl-' (light) and 'sn-' (nose) (p. 13).
  - Large-scale studies find word-pair phonological distance correlates positively with semantic distance (vector representations) above chance in many languages [149], and recover 'gl-' and 'sn-' by regression [148]. Such regularities appear in typologically unrelated languages [147,150], suggesting "a fundamental drive" for phonological and semantic clustering (p. 13).
  - *Learning benefits:* non-arbitrariness may help bootstrap language [154]. The first words children learn show more non-arbitrariness than later ones [146,155,156]. Experiments find it helps early word learning, broad distinctions such as noun vs verb, and generalisation to novel words [157–159] (p. 13).
  - *Feedback to the lexicon:* in laboratory language evolution, arbitrary signals can become systematic after repeated generations [137,138,160,161]. Arbitrary and non-arbitrary mappings each bring advantages and disadvantages, which over generations will shape vocabulary structure (p. 14).

### Challenges for the Efficiency Approach (pp. 14–15)
- **Complexity measurement:** there is less agreement on how to measure complexity or learnability. One measure is description length in a meta-language [46], which depends on the meta-language chosen. Estimates are partly independent of it [129] but may still vary by large magnitudes. A precise metric is needed to relate learnability, compositionality, systematicity and iconicity (p. 14).
- **Null hypotheses:** efficiency claims need a counterfactual baseline. Examples: all logically possible kinship systems [46]; randomly reordered sentences [87] (p. 14). Making such baselines is "often the most challenging part". Claiming one utterance is the most efficient would require comparing it with everything the speaker could have said, including pragmatics. No general, satisfactory method exists (p. 14).
- **Measurement:** entropies must be estimated from corpora, and reliable estimates need very large datasets [162,163]. Piantadosi et al. used Google web-scale n-grams [32]. This confines many studies to modern English (p. 14).
- **Communicative utility:** other factors affect utility, e.g. taboo words, which are avoided even if efficient. It is unclear whether these fit into efficiency or need extra terms (p. 15).
- **Populations and cultures:** communicative needs differ (new technologies create new words; Japanese honorifics). Population structure and non-native speakers may affect shared knowledge and hence the encodings needed. The extent to which this yields explanatory theories remains unclear (p. 15).
- **Historical change:** SOV order can change completely in a few hundred years (as in early English), but not all changes among the six orders are equally likely [165,166]. Understanding constraints on models of change remains limited (p. 15).

### Concluding Remarks and Outstanding Questions (pp. 15–16)
- The studies reveal phenomena driven by efficiency, balancing efficient use and complexity. Theories of the evolutionary and developmental origins of language are likely to be best constrained by its social and communicative function (p. 15).
- Information theory assumes idealised communication. A productive direction is to connect it to testable cognitive processes, since information is defined via probabilistic expectations, and the psychological capacity for computing them will constrain theory (p. 15). A compelling future connects linguistics, information theory and cognitive psychology (p. 16).
- Outstanding questions (p. 16) include: how conflicts between efficiency and learnability are resolved; whether the principles explain finer grammatical phenomena such as syntactic islands; connections to neural principles; effects of individual and social variation; extension to gesture, programming languages and mathematics; and how far a language's structure shapes the messages speakers want to communicate.

## Toy example (ours, not from the text)
Four words, each with overall frequency 1/4: $w_1,w_2$ occur only in context A, and $w_3,w_4$ only in context B. Each context is equally likely, so $p(x,c)=1/4$ for the four pairs $(w_1,A),(w_2,A),(w_3,B),(w_4,B)$.

- Frequency-only code: $h(w)=\log_2 4=2$ bits for every word. Average length $=H[X]=4\cdot\tfrac14\cdot 2=2$ bits.
- Context-aware code: $p(w_1\mid A)=p(w_2\mid A)=\tfrac12$, and likewise for B. Then
$$H[X\mid C]=\sum p(x,c)\log_2\frac{1}{p(x\mid c)}=4\cdot\tfrac14\cdot\log_2 2=1\text{ bit}.$$
So in each context a one-bit signal suffices (like Paul Revere's one or two lights).
- Mutual information: $I[X:C]=H[X]-H[X\mid C]=2-1=1$ bit. Knowing the context removes half the uncertainty.
- Lesson: all four words have the same frequency, so frequency alone predicts no length difference. Probability in context predicts the shorter length, which is the pattern the paper reports for word length (p. 6).

## Concepts
- [[entropy-H-X]] — average surprisal of a random variable, as uncertainty about its value (p. 4)
- [[self-information-surprisal]] — $h(x)=\log_k 1/p(x)$; approximates the shortest code length for $x$ (p. 4)
- [[bit]] — information unit when the log base is 2 (p. 4)
- [[joint-and-conditional-entropy]] — $H[X\mid C]$, uncertainty left about $X$ given $C$; between 0 and $H[X]$ (p. 4)
- [[mutual-information]] — $I[X:C]=H[X]-H[X\mid C]$, symmetric and non-negative (p. 4)
- [[noisy-channel]] — transmission with errors from speech errors, noise or inattention (p. 3)
- [[source-coding-theorem]] — here only the *task* of source coding (short signals on average) is defined, not the theorem (p. 3)
- [[redundancy]] — extra marking (e.g. gender) that may act like parity bits against noise (p. 11)
- [[error-correcting-code]] — only the analogy to parity bits is made (p. 11)
- [[rate-distortion-function]] — efficiency under approximate message reconstruction; only named (p. 4)
- [[uniform-information-density]] — information per unit time should be roughly constant (p. 8)
- [[communicative-efficiency]] (new) — successful communication with minimal average effort, usually short messages (p. 3)
- [[pareto-frontier-informativeness-complexity]] (new) — optimal trade-offs between informativeness and complexity of a lexicon (p. 6)
- [[dependency-locality]] (new) — linked words should be linearly close; reduces memory effort (p. 9)
- [[information-locality]] (new) — words with high mutual information should be close (p. 9)
- [[arbitrariness-iconicity-systematicity]] (new) — form–meaning mapping: arbitrary, intrinsically matching, or language-specifically patterned (pp. 12–13)

## Canonical instances
- [[paul-revere-one-bit]] — in a two-option context, one bit suffices (p. 5)
- [[morse-code-length]] — frequent letters get shorter codes ('e' vs 'q') (p. 5)
- [[word-length-predictability]] — in-context predictability beats frequency as a predictor of word length across languages (pp. 5–6, Fig. 2)
- [[chimp-chimpanzee]] — short form chosen more in predictive contexts (p. 6)
- [[kinship-pareto-frontier]] — kinship systems near the informativeness–complexity frontier; Swedish grandparents (p. 6)
- [[color-warm-cool-surprisal]] — warm colours cost fewer bits than cool in all languages tested (p. 8)
- [[dependency-length-37-languages]] — dependency length below random baselines (p. 9, Fig. 4)
- [[minimal-pairs-clustering]] — the four lexicons tested (Dutch, English, French, German) have more minimal pairs than phonotactic baselines (p. 13, Fig. 5)

## Bridges (candidates)
- [structural-analogy] Zipf's frequency–length law ↔ information theory: code length $\approx$ surprisal in optimal codes — both give short codes to likely messages, with probability taken in context.
- [same-math] Surprisal, entropy, conditional entropy, mutual information in Box 2 ↔ information theory: the standard definitions (I)–(V).
- [structural-analogy] Redundant gender marking ↔ error-correcting codes: parity bits add redundancy for robustness to noise.
- [structural-analogy] Informativeness–complexity trade-off in lexica ↔ rate–distortion theory: bits spent against loss of useful distinctions.
- [structural-analogy] Complexity as description length in a meta-language ↔ Kolmogorov complexity / MDL: the paper cites [46,129] and notes the dependence on the meta-language.
- [metaphor] Languages as codes selected by cultural transmission ↔ evolution: differential survival of forms across learners.

## Questions this raises
- How can the "complexity" side of the trade-off be measured so that it is comparable across lexicon, syntax and morphology (p. 14)?
- What counterfactual baseline would make an efficiency claim for a whole language, or a single utterance, rigorous (p. 14)?
- If efficiency depends on probabilistic expectations, what do human memory and prediction limits imply for the information-theoretic quantities used (p. 15)?
- Which findings (e.g. SOV preference, gender systems) are explained by efficiency and which by other biases, given the authors' own caveats (pp. 9, 11)?

## Reading notes
- Printed page numbers equal pdf page numbers (offset 0). Source is the "Article in Press" version (running header "Month Year, Vol. xx, No. yy"; copyright line "© 2019 Published by Elsevier Ltd."). Pages 16–19 hold the references and the Outstanding Questions box, not digested in detail.
- Misprints seen: author "Piandadosi" on p. 1 (should be Piantadosi); "Chomksyan" in the glossary (p. 3); "Church Salvonic" in the Fig. 4B panel labels. The text layer of Box 2 garbles symbols; equations (I)–(V) were transcribed from the page layout and checked against the surrounding prose.
- Fig. 3B legend says "Bolivian-Spanish"; the panel labels read English, Spanish, Tsimane'.
- The glossary says dependency locality holds "in sentences of all human languages" (words "closer together than any reasonable baseline"). The main text (p. 9) gives as its worked example the narrower result: minimised versus several random baselines in 37 (replicated on 50) languages.
- The text says kinship systems of "all the world's languages" lie near the frontier (p. 6); the Fig. 3A caption says "on or near".
- Several claims about the colour-score formula and the "yes–no guesses" interpretation are given only in words; no formula is printed (p. 7).
