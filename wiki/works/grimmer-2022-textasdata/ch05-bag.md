---
id: grimmer-2022-textasdata/ch05-bag
work: grimmer-2022-textasdata
unit: Chapter 5. Bag of Words
pages: 94-111
fields: [political-science]
level: grad
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 13
pipeline_version: 0.1
---
# Bag of Words

## L0 — One line
A bag-of-words representation turns each text unit into a row of word counts, built by a sequence of judgement-laden preprocessing choices that are only a default recipe.

## L1 — The gist (≤ 120 words)
How can text be turned into numbers that models can use? The chapter's answer is the bag of words: choose a unit of analysis, tokenize (split into words), reduce the vocabulary (lowercase, drop punctuation and stop words such as *the*, stem or lemmatize to merge word variants, filter by frequency), and count words into an N × J document-feature matrix. This discards word order but is still, in the authors' words, "shockingly powerful". The recipe is only a default. Stop words can carry real signal (authorship, gender pronouns), and for very large corpora stemming and stop-word removal may hurt. Preprocessing choices can change results and need validation.

**Prerequisites:** matrices (rows, columns, sums); the idea of a corpus; basic probability (for the n-gram test idea).

## L2 — Key ideas
- A bag of words represents each document only by how often each word appears; word order is discarded, giving a parsimonious but lossy representation (p. 95).
- The unit of analysis (document, sentence, page, author-day) depends on logistics, the model and, most importantly, the research question (pp. 97–98).
- Tokens are the pieces counted; types are distinct tokens (the vocabulary). Words are a compromise between letters (too few types) and sentences (too many); n-grams (features made of $n$ consecutive words) recover some phrase meaning (pp. 99–100).
- Complexity-reduction steps (lowercasing, dropping punctuation, dropping stop words (very common words), stemming/lemmatizing (merging word variants), frequency filtering) shrink the vocabulary but each embeds an assumption (pp. 101–104).
- The document-feature matrix $W$ is $N \times J$ ($N$ documents by $J$ word types), sparse (mostly zeros), and simple row and column sums already summarise a corpus (p. 106–107).
- The default recipe is primarily designed for tasks about general subject matter. It can fail when function words matter, as in Federalist authorship (pp. 108–109).
- With millions of documents, preprocessing may be unnecessary or harmful; such default advice is a product of its time, and validation is needed (pp. 110, 104).

## L3 — Walkthrough

### Introduction (p. 94)
The chapter gives documents a numerical representation. It uses the State of the Union (SOTU) corpus. The bag of words underlies the multinomial language model (Ch. 6) and the vector space model (Ch. 7) (p. 94).

### 5.1 The Bag of Words Model (pp. 95–96)
- Core idea: represent each document by counting how many times each word appears in it (p. 95).
- Example 5.1 uses two SOTU sentences containing *manufacturing*, treated as documents: Doc 1 (Jackson, 1831) and Doc 2 (Obama, 2012) (p. 95).
- The result is a **document-feature matrix**: rows are documents, columns are features. This throws away much information, most notably word order, but is parsimonious (p. 95).
- Full recipe (p. 96): (1) choose the unit of analysis; (2) tokenize; (3) reduce complexity (lowercase, remove punctuation, remove stop words, create equivalence classes by lemmatizing or stemming, filter by frequency); (4) create the document-feature matrix.

*Intuition note:* Counting words is like pouring a text into a bag and shaking it: you know which words are inside and how many, not their order. Much of the rest of the book works on matrices like this (p. 107).

### 5.2 Choose the Unit of Analysis (pp. 97–98)
- The unit may be the document, or smaller or larger (headlines, paragraphs, all of one author's tweets in a day). The authors use sentences for the example because they are short (p. 97).
- Three considerations: logistics of splitting, the model, the question (p. 97).
- *Logistics:* Chronicling America newspapers are OCR-digitised from print. Columns and jumps across pages make article text hard to extract, so one might analyse the page instead (Young, 2012) (p. 97).
- *Model:* splitting a text can raise or lower computational cost and statistical efficiency. Digital-humanities researchers often split novels into chunks of a few hundred words (Jockers, 2013) (p. 97).
- *Question (the most important):* a study of when countries go to war should use countries or dyads, not provinces. A study of how a novel's plot varies over time should use the novel, not single chapters or sentences (p. 97).
- Computational convenience may conflict with the question. Sometimes a model fitted on small chunks can be aggregated to the relevant unit, but depending on the model this might not be straightforward; decide case by case (p. 98).
- Typically, from here on, "document" refers to whatever the unit is, not necessarily a full document (p. 98).

### 5.3 Tokenize (pp. 99–100)
- Tokenization splits a document into words. A **token** is an individual unit counted; its **type** is the column name; the set of types is the **vocabulary** (p. 99).
- In English, splitting on white space is essentially enough, and this works for most languages. Chinese, Japanese and Lao need a *word segmentation model* because words are not space-separated (p. 99).
- Why words? Letters give only 26 types but carry no meaning alone. Sentences carry complete ideas, but nearly every sentence is probably unique, so there are far too many types. Words compromise (p. 99).
- Some concepts span words (*white house*). **n-grams** are ordered sets of $n$ words: unigrams, bigrams, trigrams. Higher-order n-grams greatly increase the number of types but keep more information (p. 99).
- Two ways to include them: (a) all consecutive word pairs, giving a very large number of columns (to be handled by filtering, §5.4.5); or (b) a chosen list of bigrams and trigrams, e.g. *national security*, *local government* in Rule, Cointet and Bearman (2015). The authors mark these with an underscore. When the list is small this avoids a large vocabulary, but it requires an n-gram list (p. 100).
- A common way to build such lists uses statistical tests. The shared logic: add a bigram if the probability of the pair is high enough relative to the probability of seeing each word separately (e.g. *white house*). Grammar-based methods are deferred to Ch. 9 (p. 100).
- Example 5.2: *United States* becomes `United_States` (p. 100).

### 5.4 Reduce Complexity (pp. 101–105)
Without dropping some types, for many applications the vocabulary is far too large to be productive, so bag-of-words models usually include a stage that drops some types. Reducing it helps computation and parsimony (p. 101).

**5.4.1 Lowercase.** *In* and *in* are treated as the same for most applications. A variant lowercases only sentence-initial words (p. 101).

**5.4.2 Remove punctuation.** Researchers often do not care about commas or periods. Headings, page numbers and html tags may also be discarded. Some punctuation may be essential, e.g. `#` on Twitter. For certain tasks such as sentiment analysis, emoticons such as `:)` and exclamation marks can be strong predictors of sentiment, so this step must be done carefully. The underscore is kept for n-grams (pp. 101–102).

**5.4.3 Remove stop words.** These are common words that carry little information about the task (*and*, *the*, *that*). Removal often takes out a very high fraction of tokens but very few types, which can bring large computational savings if those words carry little meaning. This reflects the fact that in most languages a few words are extremely common (p. 102). Footnote 1 says the idea of omitting a list of common words appears to have originated in Luhn's early information-retrieval work (Luhn, 1960); Flood (1999) recounts calling such words a "stop list" in 1961 (p. 111). After removal the example reads: *undoubtedly power congress seriously affect agricultural manufacturing interests france passage laws relating trade united_states* (p. 103).

**5.4.4 Equivalence classes.**
- A **lemma** is the dictionary form of words related by inflection. **Lemmatization** maps words to lemmas; it is an "equivalence assertion" that variants are treated alike (p. 103).
- It can be hard. *saw* → *see* needs a dictionary lookup. The token *writing* has lemma *writing* (a piece of writing) or *write* (the act), so part-of-speech tagging is needed (p. 103).
- **Stemming** approximates this by discarding word endings with simple rules (*family, families, family's* → *famili*). It is faster but misses irregular forms. It can also merge words with distinct meanings (*secure*, *securities*) (p. 103).
- Example result: *undoubt power congress serious affect agricultur manufactur interest franc passag law relat trade united_states* (p. 104). The Porter algorithm (Porter, 1980) is among the most common. Stemming is still more popular than lemmatization, probably through speed, availability across languages and momentum (p. 104).

**5.4.5 Filter by frequency.**
- Words appearing once in the corpus are unlikely to be used effectively, and there are often many of them. Removing them may save computation depending on the model (p. 104).
- Very common words, e.g. one in every document, are unlikely to discriminate between documents. The authors call these "application-specific stop words"; they often arise when the corpus was selected on a keyword or topic (p. 104).
- Order of steps matters: e.g. removing stop words before tokenization leads to different bigrams and trigrams than under a different order (the contrast is garbled in the source). The analyst uses judgement. Downstream **validation** is needed to check that the information relevant to the question survived (p. 104). (The source text says "before" twice; see Reading notes.)

*Intuition note:* Each preprocessing step amounts to saying that these differences do not matter for my question. That is a substantive claim, which fits the authors' point that validation is needed (p. 104).

### 5.5 Construct the Document-Feature Matrix (pp. 106–107)
- Let $N$ be the number of text units, indexed by $i$. Let $J$ be the vocabulary size after preprocessing, indexed by $j$. The document-feature matrix $W$ is $N \times J$, and each entry $W_{ij}$ is the number of times type $j$ appears in document $i$ (p. 106).
- $W$ is usually sparse (mostly zeros), since documents contain few of the corpus's types (p. 106).
- Running example: after lowercasing, punctuation removal, stop-word removal and stemming, the two sentences have 28 unique types, so $W$ is $2 \times 28$ (Table 5.1) (p. 106–107).
- Column sums give how often each type appears in the corpus (Table 5.2). In the example, *congress* and *manufactur* each have count 2 and every other type has count 1 (p. 107).
- Row sums give tokens per document after preprocessing (Table 5.3): Doc 1 = 15, Doc 2 = 15. The maximum row sum is the length of the longest document and the minimum that of the shortest (p. 107).

### 5.6 Rethinking the Defaults (pp. 108–110)
The default aims at general subject matter. One may want to abandon parts of it in two kinds of settings: when it is inappropriate for the problem, or when the data are large enough that it is harmful (p. 108).

**5.6.1 Federalist Papers.**
- Mosteller and Wallace (1963) addressed 12 disputed papers (Hamilton, Jay, Madison). They found the three authors' styles differed in the use of filler words such as *upon*, *by*, *to*. These are the kind of words one would filter out as stop words, but here that was exactly the objective (p. 108).
- In his autobiography Mosteller recalled that they wanted words whose use is unrelated to the topic and may be regarded as reflecting "minor or perhaps unconscious preferences of the author" (p. 108).
- Social scientists have shown the importance of features the default can treat as content-free (Biber 1991; Chung and Pennebaker 2007; Breiger et al. 2018). Monroe, Colaresi and Quinn (2008) show that *he* and *she* are highly associated with speaker party in the Congressional Record, yet nearly every English stop list contains them (p. 108).
- Denny and Spirling (2018) show that varying these steps can affect downstream results, and suggest testing several combinations (pp. 108–109).

**5.6.2 The scale argument.**
- Two reasons for reducing vocabulary: aesthetics and efficiency (p. 109).
- *Aesthetics:* Figure 5.1 compares word clouds of SOTU sentences containing *manufacturing*. The left panel has only punctuation removed and is dominated by *of*, *the*, *and*. The right panel uses the default recipe and is more informative about subject matter. But this can be handled by changing the visualisation (omit stop words from the plot, keep them in $W$) rather than the inputs (p. 109).
- *Efficiency:* stemming asserts that *car* and *cars* are equivalent. This helps with relatively few documents. With millions of documents, models may learn such relations themselves. The assertion may even be wrong: when predicting author wealth, *cars* may mean something different from *car* on average (p. 110).
- Schofield and Mimno (2016) and Schofield, Magnusson and Mimno (2017) report that default stemming and stop-word removal can harm topic-model performance when the corpus is large (p. 110).
- Lesson: default recipes are "always a product of its time"; reexamining them signals a maturing field (p. 110).

*Intuition note:* Preprocessing buys speed by betting that dropped distinctions are irrelevant. The chapter suggests the bet is more reasonable for small corpora and subject-matter questions, and riskier for authorship-style questions or very large corpora (pp. 108–110).

### 5.7 Conclusion (p. 111)
The bag of words is "shockingly powerful" despite discarding so much information. Chapters 6 and 7 build methods on it (p. 111).

## Toy example (ours, not from the text)
Corpus: A = "Cats chase mice, and the cat naps." B = "The mouse naps."
Rules (toy): lowercase; strip punctuation; stop words = {the, and}; crude stemmer = drop a final "s".
1. A: cats chase mice and the cat naps (7 tokens) → remove stop words: cats chase mice cat naps (5) → stem: cat chase mice cat nap.
2. B: the mouse naps → mouse naps → mouse nap.
3. Vocabulary: cat, chase, mice, mouse, nap, so $J=5$ and $N=2$.

| | cat | chase | mice | mouse | nap |
|---|---|---|---|---|---|
| A | 2 | 1 | 1 | 0 | 1 |
| B | 0 | 0 | 0 | 1 | 1 |

Row sums: A = 2+1+1+0+1 = 5; B = 0+0+0+1+1 = 2. Column sums: 2, 1, 1, 1, 2. The stemmer did not merge *mice* and *mouse*, an irregular form like the chapter's *saw*/*see*; this is where lemmatization would help.

## Concepts
- [[bag-of-words]] (new) — represent a document only by word counts, ignoring order (p. 95)
- [[document-feature-matrix]] (new) — $N \times J$ matrix $W$ with $W_{ij}$ = count of type $j$ in document $i$; usually sparse (p. 106)
- [[unit-of-analysis]] (new) — the text unit treated as one "document"; chosen by logistics, model, and question (p. 97)
- [[tokenization]] (new) — splitting a document into tokens; types form the vocabulary (p. 99)
- [[n-gram]] (new) — ordered set of $n$ words used as one feature (p. 99)
- [[stop-words]] (new) — common words dropped as low-information for the task at hand; may be informative for other tasks (p. 102)
- [[stemming-lemmatization]] (new) — mapping word variants to a common form; lemmatization uses dictionary forms, stemming truncates endings (p. 103)
- [[text-as-data-validation]] — here: checking that preprocessing kept the information relevant to the question (p. 104)

## Canonical instances
- [[sotu-manufacturing-example]] (new) — Jackson 1831 and Obama 2012 sentences turned into a $2\times28$ matrix (pp. 95, 106–107)
- [[federalist-authorship]] (new) — function words like *upon*, *by*, *to* distinguish the authors' styles, so the default stop-word removal is inappropriate for this task (p. 108)
- [[monroe-gender-pronouns]] (new) — *he*/*she* associated with party in the Congressional Record (p. 108)
- [[schofield-mimno-preprocessing]] (new) — default stemming and stop-word removal can harm topic models on large corpora (p. 110)

## Bridges (candidates)
- [structural-analogy] choosing the unit of analysis ↔ political science research design: choosing countries or dyads rather than provinces (the text's own analogy, p. 97)
- [structural-analogy] stop-word removal as an assumption about which features are "noise" ↔ measurement validity: dropped variables may carry the signal for a different question
- [structural-analogy] document-feature matrix $W$ ↔ a units-by-variables data matrix in statistics, with counts as variables

## Questions this raises
- How do Chapters 6 and 7 turn $W$ into a model (multinomial) and into a geometry (vectors)?
- How should one validate that a preprocessing choice did not discard relevant information?
- How can a researcher test sensitivity to preprocessing, as Denny and Spirling suggest, and report it?
- At what corpus size do default steps stop helping, and does that depend on the model?

## Reading notes
- Printed page = pdf page (94–111). Page 105 is nearly blank; Tables 5.1–5.3 are visible in the image of p. 107; in the text layer only Table 5.3 appears, and Tables 5.1 and 5.2 are missing. I checked the 28 columns and row sums (15, 15) against the image.
- Misprint p. 106: "these three documents have 28 unique words"; only two documents are used, and Table 5.1 has two rows and 28 columns.
- p. 104: the sentence "if stop words are removed before tokenization ... than if they are removed before" repeats "before"; presumably the second should be "after" (the intended contrast is not stated).
- p. 104: the recap of the recipe omits stop-word removal and the choice of unit, which the numbered list on p. 96 includes.
- No exercises appear in this unit.
