---
id: brin-1998-anatomy/index
work: brin-1998-anatomy
type: work-map
units: [brin-1998-anatomy/main]
generated: deterministic
---

# Brin, S., & Page, L. (1998). The anatomy of a large-scale hypertextual Web search engine. *Computer Networks and ISDN Systems*, 30(1–7), 107–117. https://doi.org/10.1016/S0169-7552(98)00110-X

## One digest
This work has a single digest, which is also its work-level summary: [[brin-1998-anatomy/main]].

## In one line
Google ranks web pages by combining a link-based importance score (PageRank, said to be the principal eigenvector of the normalized link matrix) with text, anchor and proximity evidence, inside an architecture built to scale with the Web.

## The gist
The authors ask how to build a practical search engine that gives high-precision results on the huge, uncontrolled Web. Their answer is Google. It uses the link graph to compute PageRank, a citation-importance score. It indexes anchor text (the text of links) under the page the link points to. It uses word proximity and font information. Rank is built from dot products of hit-count weights with type weights, then combined with PageRank. Compact data structures and a distributed crawl/index/sort pipeline handle 24 million pages. The paper is an early public description of a full search engine. Linear algebra appears in dot products of weight vectors and in a stated (not derived) eigenvector link.

**Prerequisites:** vectors and the dot product; sums over neighbours in a graph; the idea of an eigenvector; basic ideas of files, indexes and sorting.
