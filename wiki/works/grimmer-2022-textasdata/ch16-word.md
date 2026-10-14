---
id: grimmer-2022-textasdata/ch16-word
work: grimmer-2022-textasdata
unit: Chapter 16. Word Counting
pages: 283-292
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
# Word Counting (keyword counts, dictionaries, Wordscores)

## L0 — One line
Humans can supervise text measurement at the word level (keyword lists, dictionaries, reference-text word scores); this is simple and cheap to apply but has accuracy drawbacks, so the authors argue each measure needs explicit validation in its own context.

## L1 — The gist (≤ 120 words)
The chapter asks how far a researcher can get by writing the mapping from word counts to a label by hand. Keyword counting is clear and easy to communicate. It is more compelling when paired with close reading, as in Duneier's study of "ghetto". Dictionaries generalize this to a weighted average of word rates, e.g. a tone score. They can fail badly when applied outside the domain they were built for. The authors therefore insist on validation against hand labels, using fresh data. Wordscores derives word scores from reference texts. It bridges dictionaries and supervised learning, but depends heavily on the chosen reference texts. The next chapter moves supervision to the document level.

**Prerequisites:** document-term matrix $W$ (counts of word $j$ in document $i$); weighted averages; the idea of training and test sets.

## L2 — Key ideas
- Word-level supervision means humans write the mapping function directly, instead of a model learning it from labeled documents (p. 283).
- Keyword counting is clear and easy to communicate, but it is difficult to represent a complex latent concept (an idea we cannot count directly) accurately with one word or phrase: counts bring false positives (counted articles that are off-topic) and miss relevant articles (p. 284).
- In Duneier's "ghetto" study the authors judge that a simple count plus extensive reading is more compelling than either alone. Used alone, keyword counts can ultimately be less compelling, and Google Ngrams (phrase counts over a large book collection) has its own limits (pp. 285–286).
- A dictionary score is a weighted average of word scores, $\pi_i=\sum_j \mu_j W_{ij}/M_i$. It is often used as an approximately continuous measure, or can classify documents into categories if a decision rule (e.g. a threshold at 0) is added (p. 287).
- Off-the-shelf dictionaries can misfire in new domains (Loughran and McDonald on earnings reports), so use with caution and explicit validation (p. 289).
- Validate against hand labels on data different from the data used to build the dictionary. Revising and re-validating on the same data risks overfitting (choosing words to fit the validation data, so the mapping may not generalize) (p. 289).
- Wordscores derives word scores from reference texts at the ideological extremes. It is sensitive to the choice of reference texts, style and non-ideological content (pp. 290–291).

## L3 — Walkthrough

**Opening (p. 283).** Later chapters label documents into categories (Ch. 18) and train models on these labels (Ch. 19). The model then learns the mapping from $W$ (the text representation) to $y$ (the categories). This chapter instead covers methods where humans annotate *words*, and researchers write the mapping function themselves. The core assumption: applying the human-made rules to documents yields a text-level label that accurately reflects the text's category (p. 283).

**16.1 Keyword counting (p. 284).**
- The simplest dictionary approach is counting a word or phrase. It is clear and easy to communicate (p. 284).
- Example: to measure interest in US presidential politics, counting articles with *president* is imprecise, since companies and universities also have presidents. Counting *White House* gives fewer false positives, but many relevant articles lack the phrase (p. 284).
- Authors' conclusion: counting is mechanically easy but representing complex latent concepts is hard. With carefully chosen words and validation by careful reading, it can be "extraordinarily effective" (p. 284).

*Duneier (2016) case (pp. 285–286).*
- Duneier traces "ghetto" from sixteenth-century Venice to Nazi ghettos to US segregation of African Americans (p. 285).
- His single graph (Fig. 16.1) uses Google Ngrams over 800,000+ books and four phrases. *Warsaw Ghetto* and *Jewish Ghetto* rise quickly from 1940. *Black Ghetto* and *Negro Ghetto* follow, the common phrases for segregated African American residential areas (p. 285).
- **Duneier's argument:** the shift is not an accident. In 1945 Cayton and Drake's *Black Metropolis* used "Black Ghetto" to draw attention to coercive housing policy and to America's hypocrisy (p. 285). Restrictive covenants began in 1928, yet "Black ghetto" rises only after the surge in references to the Jewish ghetto, which the authors say is evidence that the term came to be associated with US cities primarily as a result of the Nazi use of the term (p. 285).
- He supports this by reading sources: Drake and Cayton's "barbed-wire fence" image, which he reads as a symbol of Nazi ghettos, not of sixteenth-century Venice (p. 286). He also reads and quotes many of the books behind the trend line (p. 285).
- **Authors' assessment:** a simple count combined with extensive reading makes a stronger argument than either alone (p. 286). Used alone, keyword counts can ultimately be less compelling. Total uses of "ghetto" far exceed the four bigrams, and Pechenick, Danforth and Dodds (2015) point out that Ngrams' source composition changes over time (p. 286).

*Intuition note.* The graph makes it readily apparent *that* usage changed. Duneier's reading of the sources supports his argument about *why*. The authors say this extra evidence is essential to the credibility of the argument, and that counts used alone can be less compelling (p. 286).

**16.2 Dictionary methods (pp. 287–288).**
- A dictionary generalizes keyword counting. It uses a weighted average of keyword rates to classify documents or to measure how far they belong to categories (p. 287).
- For tone, each word $j$ has a score $\mu_j$. In the simplest case $\mu_j=-1$ (negative) or $\mu_j=1$ (positive). With $M_i=\sum_{j=1}^{J}W_{ij}$ words in document $i$, tone is
$$\pi_i=\frac{\sum_{j=1}^{J}\mu_j W_{ij}}{M_i}. \tag{unnumbered, p. 287}$$
- $\pi_i$ is often used as an approximately continuous measure. With a decision rule it can classify, e.g. $\pi_i>0$ positive, $\pi_i<0$ negative (p. 287).
- Dictionaries cover more than tone. They are relatively easy and cheap to apply. Researchers can write their own or use existing off-the-shelf ones (p. 287).
- With already-coded documents, dictionary-like word scores can be derived using the Chapter 11 methods. Monroe, Colaresi and Quinn (2008) describe methods measuring how well words separate known categories. These scores can then be applied in other contexts (pp. 287–288).

*Intuition note.* $\pi_i$ is the average score per word in the document. (added step) Words with $\mu_j=0$ add nothing to the numerator but still count in $M_i$.

**16.3 Limitations and validation (pp. 289–290).**
- For dictionaries to work well, word scores must closely align with how words are used in the particular context. This should be easy to justify for task-specific dictionaries, though Barberá et al. (2021) find even these may underperform supervised learning (p. 289).
- **Loughran and McDonald (2011):** off-the-shelf dictionaries used for the tone of corporate earnings reports misfire. Words like *tax, cost, crude, cancer* may be positive in earnings reports. A healthcare firm mentions cancer often, and an oil firm discusses crude. Words like *unanticipated* may be quite negative there but are not flagged by off-the-shelf dictionaries (p. 289).
- **Prescription:** use dictionaries with substantial caution and explicit validation. Show that word lists from other contexts apply, or build a domain-specific one. Hand-label a sample of documents and compare the dictionary's aggregate measure to it (p. 289).
- Validate on data different from that used to create the dictionary. If the dictionary is changed after validation, it cannot be validated again on the same data (overfitting: words chosen from what is seen in the validation set may not generalize). Use a new set of fresh data (p. 289).
- Authors' diagnosis: in practice dictionary measures are rarely validated. Many analyses therefore rest on shaky foundations. The question is whether variation in the weighted scores reflects real differences in the quantity or just noise. The authors say case-specific validation is paramount (p. 290).

*Intuition note.* A dictionary builds in assumptions about word meaning, and the authors note that dictionaries do not necessarily produce a measure with any particular properties (p. 290). Comparison with hand labels is how one checks whether those assumptions hold in the application (p. 289).

**16.3.1 Wordscores (pp. 290–291).**
- Laver, Benoit and Garry (2003): a fully automated method to place actors in ideological space from their words, using exemplar texts. The authors call it a true breakthrough and one of the first large-scale text analyses in the social sciences. It is presented as a bridge between dictionaries and supervised learning (p. 290).
- Steps: (1) choose reference texts defining positions, e.g. all speeches of a very liberal senator (Wyden, Boxer) and a very conservative one (Coburn, DeMint) (p. 290). (2) Score each word by its relative rate of use in the reference texts, a measure of how well it separates the two positions (p. 290). (3) For each "virgin" (= test-set) text, compute word-use rates. Its position is the weighted average of the word scores, with weights given by those rates (p. 291).
- Wordscores generalizes to multiple dimensions and several reference texts. The authors nonetheless find it hard to recommend for general use (see Lowe 2008). By defining the extremes using only reference texts that are indicative of the extremes, Laver, Benoit and Garry (in the authors' critique) conflate ideological language with stylistic differences across authors. It also imposes the "ideological dominance assumption" (not defined in this unit). Results depend strongly on the reference texts, partly through style and non-ideological content (p. 291).
- Mitigation: careful preprocessing to remove stylistic words. Beauchamp (2011) shows removing technical language, which coincides more with party power than with ideology, significantly improves results (p. 291).

**16.4 Conclusion (p. 292).** Word counting is the simplest supervision. Dictionaries and Wordscores are simple, but have accuracy drawbacks. Supervised learning (next chapter) puts supervision at the document level, which costs more effort and time, but the authors believe it is often worth it (p. 292).

## Toy example (ours, not from the text)
Dictionary: *profit* $\mu=+1$, *loss* $\mu=-1$, *cancer* $\mu=-1$ (as in an off-the-shelf list). All other words $\mu=0$ (our choice).

- Doc A (10 words): *profit* ×3, *loss* ×1, 6 other words. $\pi_A=(3\cdot1+1\cdot(-1))/10=2/10=0.2>0$, so positive.
- Doc B (healthcare report, 20 words): *cancer* ×4, *profit* ×1, 15 other words. $\pi_B=(4\cdot(-1)+1\cdot 1)/20=-3/20=-0.15<0$, so negative.

Doc B is classed negative only because the firm treats cancer. In earnings-report usage, cancer may carry a positive connotation (Loughran and McDonald). A hand-labeled sample would expose this mismatch.

## Concepts
- [[keyword-counting]] (new) — counting occurrences of a chosen word or phrase as a measure of a concept (p. 284)
- [[dictionary-method]] (new) — classify or score documents by a weighted average of word rates, with human-set word scores (p. 287)
- [[wordscores]] (new) — word scores derived from reference texts at extremes, then used to scale test texts (p. 290)
- [[text-as-data-validation]] — compare dictionary measures to hand labels on fresh data; revised dictionaries need new data (p. 289)
- [[overfitting-in-validation]] (new) — changing words after seeing validation data means re-validating on that same data risks overfitting (p. 289)
- [[domain-specificity]] (new) — word scores that fit one context can be wrong in another (p. 289)

## Canonical instances
- [[duneier-ghetto-ngrams]] — four-phrase Ngram counts plus close reading support a historical argument (pp. 285–286)
- [[loughran-mcdonald-earnings-tone]] — off-the-shelf tone dictionaries misclassify words in earnings reports (p. 289)
- [[wordscores-senators-example]] — hypothetical illustration: scaling US senators using all speeches of a very liberal and a very conservative senator as reference texts (p. 290)

## Bridges (candidates)
- [structural-analogy] Dictionary score $\pi_i$ ↔ supervised learning: a linear function of normalized word counts, but with weights set by hand rather than learned (p. 283 describes this contrast).
- [structural-analogy] Validating on fresh data ↔ train/test split in machine learning: Wordscores' "virgin" texts are explicitly called the test set (p. 291).
- [structural-analogy] Wordscores' dependence on reference texts ↔ confounding of the measured trait with author style in any measure trained on few exemplars.

## Questions this raises
- How large and how varied should a hand-labeled validation sample be, and how should agreement with the dictionary be measured?
- How can an off-the-shelf word list be adapted to a new domain without invalidating its validation?
- What is the "ideological dominance assumption", and how does it bias scaling?
- When does the extra labeling effort of supervised learning pay off relative to dictionaries?

## Reading notes
- Printed page = pdf page (283–292).
- The equation is flattened in both the text layer and the page image of p. 287. The fraction layout is read from the symbol order: $\sum_j\mu_jW_{ij}$ over $M_i$, which fits the verbal description (a weighted average of word rates). It has no equation number.
- Figure 16.1 is not visible in the text layer or in the page image of p. 285 (only the caption); only the caption and the authors' description were used.
- The chapter does not give a Wordscores formula or define the "ideological dominance assumption".
- Footnote 1 (p. 292): part of the dictionary section is drawn from Grimmer and Stewart (2013).
