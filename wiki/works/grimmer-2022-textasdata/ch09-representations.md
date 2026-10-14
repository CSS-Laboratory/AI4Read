---
id: grimmer-2022-textasdata/ch09-representations
work: grimmer-2022-textasdata
unit: "Chapter 9. Representations from Language Sequences"
pages: 157-170
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 11
pipeline_version: 0.1
---
# Representations from Language Sequences

## L0 — One line
Methods that treat text as an ordered sequence (text reuse, POS tagging, NER, dependency parsing) let social scientists measure copying, phrases, actors and events by using word order, which the word-focused methods of Chapters 5–8 did not.

## L1 — The gist (≤ 120 words)
Chapters 5–8 mostly ignored word order. This chapter asks what social scientists gain from methods that use it. The authors review text reuse, part-of-speech (POS) tagging with noun-phrase detection, named-entity recognition (NER), dependency parsing, and the information-extraction tasks built on them. Each is tied to published applications: press-release copying, bill histories, Chinese elite power, police killings, political event data. The authors argue that a representation is a choice about which information to keep, so it should follow the research question and the stage of research. They stress applications, not estimation details.

**Prerequisites:** document-feature matrices and unigrams (Chs. 5–8); the idea of a regular expression; directed graphs.

## L2 — Key ideas (5–10 bullets)
- Text reuse finds long shared sequences between documents that are unlikely to be chance. It lets researchers trace influence, such as press releases into newspapers (pp. 158–159).
- Reuse methods compare documents in pairs, so cost grows fast. Preprocessing is needed for large corpora (p. 159).
- POS tags can subset features and, with grammatical patterns, find noun phrases, which often mean more than the sum of their words (pp. 160–161).
- In the State of the Union example, noun-phrase word clouds are arguably more informative than unigram clouds (pp. 162–163).
- NER turns mentions of people and organizations into counts. Jaros and Pan use them as a proxy for power in Chinese official papers (pp. 164–165).
- Dependency parsing gives a directed graph of syntactic relations. It is mainly a tool for further extraction (p. 166).
- Information extraction covers entities, relations and events. Political event data is an early and ongoing application (pp. 167–168).
- Representation should be driven by the question and research stage; reducing complexity is a key step (pp. 169–170).

## L3 — Walkthrough

**Chapter intro.** Ignoring word order can get "shockingly far", because such analyses are simple and tractable. This chapter instead focuses on words within a sequence and on what the outputs of the models are useful for, not on how the models are estimated (p. 157).

### 9.1 Text Reuse
- Text reuse algorithms identify sequences common to a pair of documents. The sequences are long enough that chance is improbable. Usually one document was copied from the other, or both from a common source (p. 158).
- **Grimmer (2010):** 24,000 Senate press releases from 2007. Off-the-shelf plagiarism software showed local papers reprint large sections almost word-for-word. This supports the claim that press-release information reaches news consumers. For smaller local papers, as many as 30% of a state senator's releases might be copied. The San Francisco Chronicle quoted 6–7% of the California senators' releases (p. 158).
- **Bail (2012):** found mainstream news that substantially reused civil-society press releases about Muslims after 9/11. He added qualitatively coded information on why some releases spread. Media amplified well-resourced organizations and also fringe ones promoting angry and fearful frames (p. 158). Reuse can thus be an innovation in measuring culture, beyond showing that copying occurred (p. 158).
- **Wilkerson, Smith and Stramp (2015):** traced policy ideas through text reuse across earlier failed bills. The Affordable Care Act drew ideas from 232 previously introduced bills, including some sponsored by Republicans who later voted against it (p. 159). State legislatures may offer richer cases, since groups such as ALEC distributed model text (p. 159).
- **Cost:** pairwise comparison of nearly 120,000 bill sections would need over seven billion comparisons if done naively. Preprocessing cut comparisons by three orders of magnitude (p. 159).

*Intuition note.* Long shared strings are a fingerprint of influence. The cost lies in comparing every pair of documents, so large studies need shortcuts first.

### 9.2 Parts of Speech Tagging
- POS tagging assigns a grammatical tag (verb, noun, preposition, adjective) to each word. It uses rules or a classifier trained on hand-tagged data. The Penn Treebank has 4.8 million words with 45 tags and is often used for English. Other resources exist for Twitter and online conversation (p. 160).
- Uses: input to other techniques; subsetting document-feature matrices (e.g. keep adjectives and adverbs for sentiment, which are more likely to carry sentiment cues); separating word senses when senses differ by POS (p. 160).
- **Noun-phrase detection.** Noun phrases (a noun plus words modifying it, e.g. *health care*, *World Cup*) often mean more than their unigrams combined. Steps: tag each word; take all phrases of a given length (e.g. 4); test each against a grammatical pattern written as a regular expression (p. 160).
- Simple pattern, where N = noun, A = adjective, and | means OR (matches *New York*, *World Cup*, *old songs*) (pp. 160–161):
$$(N|A)+N$$
- Pattern allowing a trailing preposition phrase, with P = preposition and D = determiner (e.g. *woman from New York*). The author says * marks the previous clause as optional (p. 161):
$$(N|A)+N(P+D*(A|N)*N)*$$
- Noun phrases are used for digital-library search, biographical information, and partisan language. Similar strategies can find verb phrases, useful for identifying events (p. 161).

**9.2.1 Phrases to improve visualization.**
- Chuang, Manning and Heer (2012): coders wrote keyphrases for dissertation abstracts. Noun phrases were 13% of all phrases but 65% of the keyphrases humans chose. Crowdsourced judges found word clouds with phrases more informative (p. 161).
- **Example:** Rule, Cointet and Bearman (2015) report that the "statecraft" topic declines and "foreign policy" replaces it, around 1917 (p. 162). The authors take all State of the Union sentences containing *foreign*, split before and after 1917, and remove *foreign* itself (p. 162).
- Unigram clouds (Fig. 9.1) show *polici* as most common after 1917 and states perhaps more common before. Beyond that, the periods are hard to tell apart (p. 162).
- Noun-phrase clouds (Fig. 9.2) are arguably far more informative. They show growth of *foreign oil* and *foreign aid* after 1917. They also show a shift from Great Britain to Middle East (pp. 162–163).
- POS tagging is relatively fast and, for formal text such as news, quite accurate (p. 163).

*Intuition note.* Tags let you keep word groups that often act like single concepts. "Foreign oil" says more than "foreign" and "oil" counted apart.

### 9.3 Named-Entity Recognition
- NER tags people, organizations and places, and in specialized settings dates, drug names or chemical reactions. It is built on sequence-based machine learning and is fairly accurate out of the box for formal writing (p. 164).
- **Jaros and Pan (2018):** Official Chinese newspapers are the data. *Speculation (others):* Xi Jinping consolidated more power than Hu Jintao. Other experts: the Party gained power relative to government, and anti-West sentiment seemed to rise (p. 164).
- Power is hard to measure. Jaros and Pan note that previous research has shown that official papers often reflect consolidation of power within the CCP. So more powerful entities would be mentioned more often (p. 164).
- **Measure:** NER on provincial papers. Power = mentions of an entity as a proportion of all other entities mentioned (p. 165).
- **Findings:** Xi was mentioned much more than his predecessor during his time. Party institutions gained prominence. Unexpectedly, mentions of foreign organizations did not decline (p. 165).

*Intuition note.* Tagging names converts text into counts of who gets attention. The step from mention counts to power relies on the premise, which Jaros and Pan take from earlier research, that official papers reflect power (p. 164).

### 9.4 Dependency Parsing
- A dependency parse is a directed graph of how words and phrases are syntactically connected. It identifies a root, often the main verb, and relates other words to it (p. 166).
- **Example** (Fig. 9.3): "The U.S. military retired hundreds of attack helicopters." The root is *retired*. The nominal subject is *The U.S. military* (DET *The*, NN *U.S.*). The direct object is *hundreds of attack helicopters* (PREP *of*, POBJ *helicopters*, AMOD *attack*) (pp. 164, 166).
- Parses show which words modify which. They help with sentiment, actor–issue relations, and political complexity of a text. For social scientists the parse enables information extraction rather than being an end itself (p. 166).

### 9.5 Broader Information Extraction Tasks
- Information extraction identifies discrete structured information: entities, relations between entities, and events. NER is one case (p. 167).
- **Relation extraction:** identifies relations between entities (e.g. Mark Zuckerberg founded Facebook), often as facts in fixed slots (p. 167).
- **Event extraction:** an action at some time, usually between two or more entities. Events carry more attached information (time, location, nature, participants). One branch uses templates with slots that must be filled (p. 167).
- **Keith et al. (2017):** to extract names of people killed by police, they use NER to find candidate targets. From each sentence they extract dependency paths including the target. With other features, these train a model to flag sentences saying the target was killed by police. Federal data are incomplete and current efforts rely on manual extraction. In a six-month test they found 39 individuals not in The Guardian's "The Counted", which indicates that automation could improve existing datasets (p. 167).

**Political event data.**
- Event coding of "someone did something to someone else" dates back to the 1980s and is useful in forecasting. Early systems were primarily based on POS tagging. Modern ones use dependency parsing and record more (p. 168).
- Early methods used pattern matching on fixed actor and event dictionaries. They failed on sentences like "The U.S. embassy in Baghdad suffered an attack." Parsing identifies whether *attack* is the root and who the actor is, even if not adjacent. The sentence can then be rearranged for pattern matching (p. 168).
- Remaining problem: event dictionaries are expensive to create and maintain. Some work learns actions automatically with discovery methods (p. 168).
- Open challenge: other media. Zhang and Pan (2019) build a classifier for protest events in China from social media. They find that both the text and photographs provide more information than text alone (p. 168).

*Intuition note.* Sentence structure recovers who did what to whom when word order alone misleads. Parsing helps matching but does not remove the cost of dictionaries.

### 9.6 Conclusion
- These tasks treat language as a sequence. POS tagging and parsing are relatively underutilized in the social sciences (p. 169).
- A representation is a choice about which information to keep and discard, so it is tied to the research question and the stage of the process (p. 169).
- *Discovery stage:* try several creative representations to find new ways of organizing the corpus (p. 169).
- *Known quantity of interest:* let it drive the representation. Not all text complexity is needed, and keeping it can block success. Analyses are often focused on "characterizing the haystack instead of a straw of hay", so reducing complexity is a key step (pp. 169–170).

## Toy example (ours)
Tagged sentence: *We/Pron sang/V old/A songs/N at/P the/D World/N Cup/N*.
- Pattern $(N|A)+N$ needs at least two tokens, each of type N or A, ending in N. *old songs* = A N: match. *songs* alone: only one token, no match. *World Cup* = N N: match. Result: {old songs, World Cup}.
- Longer pattern $(N|A)+N(P+D*(A|N)*N)*$: *old* (A) + *songs* (N), then *at* (P), *the* (D), *World* (N, in the (A|N)* part), *Cup* (N). Result: the whole phrase *old songs at the World Cup*.

## Concepts
- [[text-reuse]] (new) — finding long shared word sequences between documents, unlikely to arise by chance (p. 158)
- [[pos-tagging]] (new) — assigning a grammatical tag to each word, by rules or a trained classifier (p. 160)
- [[noun-phrase-extraction]] (new) — tag words, then match grammatical patterns (regular expressions) to find phrases (pp. 160–161)
- [[named-entity-recognition]] (new) — tagging people, organizations and places in text (p. 164)
- [[dependency-parsing]] (new) — extracting a directed graph of syntactic relations, with a root word (p. 166)
- [[information-extraction]] (new) — pulling structured entities, relations and events from text (p. 167)
- [[event-extraction]] (new) — recovering actions between entities with time, place, participants (p. 167)
- [[text-as-data-validation]] — the authors stress that representation choices depend on the question (p. 169); validation itself is not discussed here

## Canonical instances
- [[grimmer-2010-press-release-reuse]] — Senate press releases reprinted by local papers (p. 158)
- [[bail-2012-muslim-coverage-reuse]] — text reuse tracks civil-society influence on media (p. 158)
- [[aca-bill-text-reuse]] — Obamacare drew ideas from 232 earlier bills (p. 159)
- [[sotu-foreign-noun-phrases]] — noun-phrase clouds show shifts in foreign-policy language (pp. 162–163)
- [[jaros-pan-ner-power]] — entity mention share as a proxy for power in Chinese papers (p. 165)
- [[keith-police-killings-extraction]] — NER plus dependency paths find unlisted police killings (p. 167)
- [[zhang-pan-protest-events]] — text plus photographs for protest events (p. 168)

## Bridges (candidates)
- [structural-analogy] Dependency parse as a directed graph with a root ↔ graph theory: rooted directed trees — the parse is described as a directed graph; the tree shape is read off Fig. 9.3.
- [structural-analogy] Entity-mention share as a power proxy ↔ measurement and validity: an indirect indicator whose validity rests on an assumed link.
- [metaphor] Pairwise text-reuse cost ↔ computational scaling: all-pairs comparison explodes with corpus size.

## Questions this raises
- How well do POS taggers and NER work on informal text compared with the formal news the authors cite?
- What validation would support mention share as a measure of power in Jaros and Pan?
- When do noun-phrase features improve classification or topic models, beyond visualization?
- How can event dictionaries be reduced or learned automatically?

## Reading notes
- Printed pages equal pdf pages (157–170).
- Text says the 1917 change was "around the time of the US entry into World War II". The date and the war name look inconsistent. I report as printed.
- Misprints as printed: "Jursfsky" for the Jurafsky and Martin citation; "determinant" for determiner; "word Great Britain" where a phrase is meant; "3 0 %" spacing in the extracted text.
- The author glosses * in the regex as "optional"; I report this as written.
- Fig. 9.3's caption is split across pp. 164–165. The sentence parsed is "The U.S. military retired hundreds of attack helicopters."
- Figs. 9.1 and 9.2 are word clouds. I read only the labels the authors discuss (foreign oil, foreign aid, Great Britain, Middle East).
