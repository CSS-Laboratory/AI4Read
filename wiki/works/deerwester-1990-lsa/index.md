---
id: deerwester-1990-lsa/index
work: deerwester-1990-lsa
type: work-map
units: [deerwester-1990-lsa/main]
generated: deterministic
---

# Deerwester, S., Dumais, S. T., Furnas, G. W., Landauer, T. K., & Harshman, R. (1990). Indexing by latent semantic analysis. *Journal of the American Society for Information Science*, 41(6), 391–407. https://doi.org/10.1002/(SICI)1097-4571(199009)41:6<391::AID-ASI1>3.0.CO;2-9

## One digest
This work has a single digest, which is also its work-level summary: [[deerwester-1990-lsa/main]].

## In one line
Replace raw words by about 100 factors from a truncated singular-value decomposition of the term-by-document matrix, so that terms, documents and queries share one space where cosine measures similarity, and relevant documents can be found even when they share no words with the query.

## The gist
Word-matching retrieval fails because people use many words for one idea (synonymy) and one word for many ideas (polysemy). The authors assume a latent semantic structure partly hidden by random word choice. They estimate it by a truncated SVD of the term-by-document matrix, with about 100 dimensions. A query becomes a pseudo-document at the centroid of its term vectors, and documents are ranked by cosine. On the MED collection this beats term matching and SMART (a standard retrieval system). On CISI it is no better than term matching, and SMART is better. The authors call the results "modestly encouraging", and say LSI gives only a partial answer to polysemy.

**Prerequisites:** matrix products and transposes; orthonormal columns ($T'T=I$); diagonal matrices; dot product and cosine; rank; the idea of eigenvectors.
