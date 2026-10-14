---
id: grimmer-2022-textasdata/ch04-selecting
work: grimmer-2022-textasdata
unit: Chapter 4. Selecting Documents
pages: 83-93
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 17
pipeline_version: 0.1
---
# Selecting Documents

## L0 — One line
When a corpus stands in for a population of interest, how well it can answer a question depends on how well it represents that population, and four types of bias (resource, incentive, medium, retrieval) recur frequently as threats to that representativeness.

## L1 — The gist (≤ 120 words)
Which documents should we analyze? The answer depends on the research question, which typically implies a population of interest (the group the question is about) and a quantity of interest. Sometimes the corpus is the object of study. Often it is a stand-in for a wider population, and then sample selection bias (a poor match between corpus and population) becomes a concern. The authors give a checklist of four recurring biases: resource, incentive, medium and retrieval. They also discuss "found data", which is dictated by availability rather than by research design. They advise transparency about why a corpus was chosen and what it may not represent. How serious each bias is depends on the question and the method.

**Prerequisites:** the idea of a population versus a sample; basic sampling bias; what a keyword search does.

## L2 — Key ideas (5–10 bullets)
- Corpus choice is sometimes dictated by availability or by interest in the collection itself. Otherwise it follows from a question, and the corpus may need rebuilding as the question changes (pp. 83–84).
- A question implies a population of interest and a quantity of interest, a numeric summary of the texts. A corpus that fails to reflect the population, or cannot yield the quantity, makes answering the question difficult (p. 85).
- Even a non-representative corpus can, with careful analysis, lead to valid insight. Gill and Spirling compare declassified or leaked records with unclassified ones (p. 86).
- Resource bias: texts often better reflect populations with more resources to produce, record and store documents (p. 87).
- Incentive bias: strategic behaviour shapes which documents are produced, kept or hidden. One study used interviews to ask what the transcripts represent (pp. 88–89).
- Medium bias: the technology of the medium shapes content, and text may omit non-textual cues (pp. 89–90).
- Retrieval bias: keyword or API (data-access interface) selection can make errors that are often systematic, not random (pp. 90–91).
- Found data are shaped by the resources and incentives of whoever makes them available. Authors should justify the choice of dataset and state what it does not represent (p. 92).
- Comparisons across time or source can worsen these problems, and platform policy changes make all four biases moving targets. How problematic they are is question-specific and depends on the method (p. 93).

## L3 — Walkthrough

### Chapter introduction (pp. 83–84)
- Corpus choice sometimes has no research question behind it. Researchers may grab many documents before a question exists. Or the collection itself is the target, as with the leaked State Department cables and the Panama Papers (p. 83).
- Mosteller and Wallace's study of the Federalist Papers concerns that specific corpus and draws no inference beyond it (p. 83).
- Often the question comes first. Catalinac chose electoral manifestos because they have the same format across candidates, go directly to voters and kept the same design over time. So they represent candidates and their persuasion strategy (p. 83).
- Goals shift. King, Pan and Roberts moved to a keyword-based stratified sample when their topic became censorship. Corpus construction may need repeating as the question evolves (pp. 83–84).
- The chapter first treats population and quantity of interest, then four biases (p. 84).

### 4.1 Populations and quantities of interest (pp. 85–86)
- In the discovery phase, analysts explore texts to learn which questions they can answer. Once a question is fixed, they revisit whether the sample reflects the population, which typically requires more data collection or refining the sample (p. 85).
- A question typically references a population. Example: "How do likely voters in the United States feel about the President?" has likely US voters as its population. A tweet corpus may suffer **sample selection bias**, among other reasons because Twitter users skew younger than likely voters (p. 85).
- A **quantity of interest** is a numeric value or set of values of particular interest to the researcher. Examples: how much users discuss a topic, or how many tweets about the president are positive versus negative (p. 85).
- If the corpus does not reflect the population, or the quantity cannot be computed from it, answering will be difficult (p. 85).
- Where text is used like a survey (opinions, flu spread, happiness), analyses depend on accounting for how online populations differ from offline ones. Even within online populations, people who discuss politics may differ from people who discuss entertainment (pp. 85–86).
- Some populations are small. Blaydes, Grimmer and McQueen collect political advice texts from Islamic and Christian European traditions, sixth to seventeenth century. They aim to reflect the most influential thinkers, not all writings (p. 86).
- Digital humanities work on a genre (Danish ghost stories) often relies on being able to tell stories that contain ghosts from those that do not (p. 86).
- A non-representative corpus can still give valid insight. Gill and Spirling see only declassified or leaked records. By comparing these with information that was unclassified, they can infer some topics that remain secret (p. 86).

*Intuition note:* The question decides what "representative" means. The same corpus can be fine for one question and poor for another. Ask who is missing and whether the number you want can be computed from the texts.

### 4.2 Four types of bias (p. 87)
- The checklist applies after the move from discovery to measurement, causal inference or prediction. Not every bias applies to every question, and some may even help for some questions. The authors say that, for many questions and populations, these four types recur frequently (p. 87).

#### 4.2.1 Resource bias (pp. 87–88)
- **Resource bias**: texts often better reflect populations with more resources to produce, record and store documents. Illiteracy, limited internet access or barriers to entry can make large parts of a population invisible (p. 87).
- Events are more likely recorded if the press is present. Archives may be unrepresentative, and texts can be lost, burned or never stored. Historical documents should not be treated as a random sample (p. 87).
- Pechenick, Danforth and Dodds: the Google Ngrams corpus contains increasingly disproportionate scientific text over the twentieth century (p. 87).
- Government records may also reflect local resources. A ProPublica journalist found that some Illinois agency records were not digitized, and scanning costs meant some could not be provided (pp. 87–88).

#### 4.2.2 Incentive bias (pp. 88–89)
- **Incentive bias**: incentives and strategic behaviour drive production and retention of documents. Individuals and organizations may fail to record, hide or destroy damaging evidence. People may post only their happiest moments. This concern may not be an issue for studying social media interactions as such, but it can bias measures of true emotional states (p. 88).
- Governments may remove or censor content or encourage self-censoring (p. 88).
- Transparency laws make texts more accessible but also change incentives. Email transparency may push sensitive talk to unrecorded phone calls or meetings. Transparency may make leaders curtail participation. Berliner and Erlich show that Mexican states with more political competition passed transparency laws earlier (p. 88).
- To use documents as a window on government's internal workings, researchers should understand the incentives behind collection and release (p. 88).
- Example: Schonhardt-Bailey studied FOMC and Congressional banking-committee transcripts with unsupervised machine learning. She also interviewed participants about how candid they could be, whether remarks were prepared, and how transparency affected deliberation (pp. 88–89).

#### 4.2.3 Medium bias (pp. 89–90)
- **Medium bias**: the technology and type of medium shape what content is recorded (p. 89).
- Until 2017 Twitter allowed 140 characters. This allows more content in languages needing fewer characters per word (Chinese, Japanese) than in English. When the limit was doubled in November 2017, the other languages were not included (p. 89).
- Pictures, videos and live streams change the role of accompanying text over time (p. 89).
- Platform culture matters. Snapchat posts are briefly accessible, whereas Twitter posts are public and more permanent. Platforms tailor content to users, so users' experiences differ (p. 89).
- Outside social media, transcripts or notes may reflect content but not tone of voice, body language or other expressed emotion. Handwritten notes may have doodles, and emojis in text messages are central to content (pp. 89–90).
- Where possible, read texts in their original context, even if the tools use only the text (p. 90).

#### 4.2.4 Retrieval bias (pp. 90–91)
- **Retrieval bias**: because texts are sometimes selected using statistical methods, retrieval bias can sometimes affect the selection of a corpus (p. 90).
- Contrast: Abello et al. use Kristensen's hand-curated "ghost stories". These reflect his social network and categorization scheme. Selecting library books with *ghost* in the title would make errors. *Hungry Ghosts* is about famine, and *A Christmas Carol* has no *ghost* in its title (p. 90).
- These errors may seem random but are often systematic. *Ghost* may steer toward one genre and miss books about phantoms, which may have different themes (p. 90).
- Keyword selection is frequent because the population is a subset of a large corpus. Humans often have difficulty thinking of words, so limited recall may make an analyst miss important ones. One approach is machine learning for selecting documents, using techniques from the measurement part of the book. Authors should be transparent about selection (p. 90).
- APIs and search functions may hide how queries become results. Reasons may be as simple as some ignoring capitalization while others are case-sensitive; some systems may return only a random or only the most relevant selection. This affects which population the texts represent (p. 91).

*Intuition note:* Each bias is a different filter between the world and your spreadsheet: who can write, who wants to write, what the medium allows, and how you pulled the texts out. Naming the filter tells you whom the corpus might leave out.

### 4.3 Considerations of "found data" (p. 92)
- **Found data** are not collected by purposeful sampling but made available by governments, individuals or institutions. Availability depends on their resources and incentives, not on the research design (p. 92).
- Critics say found data may not represent the population and can lead to flawed or wrong conclusions (p. 92).
- Use of data is nevertheless dictated by availability and subject to ethical and legal constraints (Chapter 3). Researchers should explain the logic of choosing the dataset and what it may not contain or represent (p. 92).

### 4.4 Conclusion (p. 93)
- The core challenge is a corpus representative of the population of interest, which is hard if no population is chosen. Examples: Twitter sentiment or US population? Everyone or likely voters? (p. 93)
- Comparisons across time or source may exacerbate these challenges. Platforms change policies, so all four biases are moving targets, and the phenomenon itself may change (p. 93).
- Corruption example: do large cities have more corruption, or just more established newspapers that report on it? The authors say a quite common problem in practice is that multi-decade collections essentially always have more documents later than earlier (p. 93).
- Problems are question-specific. An inconsistency that plagues one question may be the object of interest for another. Severity also depends on the analysis method (p. 93).

## Toy example (ours, not from the text)
A library has 10 books. Four are ghost stories: A, B, C, D. Titles: A "The Ghost Road", B "Ghost Tales", C "Phantom Lights", D "Marley's Visit". Another book, E, is "Hungry Ghosts", about a famine. The other 5 books have no form of "ghost" in their titles. Assume the search ignores capitalization.
- Search for *ghost* in titles retrieves A, B, E: 3 books.
- Of these 3, 2 are ghost stories. So 2/3 ≈ 0.67 of what we retrieve is relevant.
- Of the 4 ghost stories, 2 are retrieved, so 2/4 = 0.5 are found.
- The misses are C and D. C is about phantoms, so the miss is systematic: the corpus leans toward one vocabulary and genre. This is retrieval bias (p. 90).

## Concepts
- [[sample-selection-bias]] (new) — the corpus is not a good stand-in for the population of interest (p. 85)
- [[population-of-interest]] (new) — the group a research question refers to, which the corpus should reflect (p. 85)
- [[quantity-of-interest]] (new) — numeric summary of the texts that answers the research question (p. 85)
- [[resource-bias]] (new) — texts often better reflect populations with more resources to produce, record and store them (p. 87)
- [[incentive-bias]] (new) — strategic reasons shape which documents are produced, kept or hidden (p. 88)
- [[medium-bias]] (new) — the recording technology shapes and limits what content appears in text (p. 89)
- [[retrieval-bias]] (new) — selection by keywords, APIs or statistical methods can introduce errors that are often systematic (p. 90)
- [[found-data]] (new) — data made available by others, not sampled by design (p. 92)

## Canonical instances
- [[catalinac-manifestos]] (new) — corpus chosen because it matches population and construct (p. 83)
- [[gill-spirling-secrecy]] (new) — valid inference about secrecy from a non-representative corpus (p. 86)
- [[schonhardt-bailey-fomc]] (new) — transcripts plus interviews to check what transcripts represent (pp. 88–89)
- [[ghost-story-retrieval]] (new) — keyword selection errors: *Hungry Ghosts*, *A Christmas Carol* (p. 90)
- [[twitter-140-characters]] (new) — character limit means different content across languages (p. 89)

## Bridges (candidates)
- [structural-analogy] sample selection bias in text corpora ↔ political-science survey research: unrepresentative sample versus target population.
- [structural-analogy] incentive bias ↔ preference falsification: what is recorded or said publicly is shaped by strategic or social pressure.
- [structural-analogy] retrieval bias ↔ classification error in measurement: keyword rules produce false positives and false negatives, here systematically.

## Questions this raises
- How can one diagnose whether a corpus is representative when the population cannot be observed directly?
- When can inconsistencies across time or source be the object of study itself, as the authors say they may be for some questions (p. 93)?
- How much can machine-learning selection reduce retrieval bias compared with keyword lists?
- How should comparisons across time handle the growth in documents (p. 93)?

## Reading notes
- Printed page numbers equal pdf page numbers (offset 0).
- Text layer reads cleanly. No equations appear on these pages.
- Footnote 1 cites a ProPublica article (Jan. 4, 2018). Footnote 2 says "the authors" go through this thought experiment in their article and develop statistical methods for more efficient exploration of the collection (p. 93); from context this seems to mean Abello et al.
- The pages cover the whole chapter, including the conclusion. They contain no exercises.
