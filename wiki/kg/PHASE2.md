# Knowledge graph — phase 2 report (2026-10-15)

Phase 2 makes the phase-1 graph trustworthy: curated aliases instead of rewrites, normalised bridge
fields, multi-field works, better canon-instance matching, a parser with no unparsed lines, and 13
curated hub pages. Nothing in `wiki/works/`, `posts/`, `pipeline/`, `site/` or `canon/` was changed.
`scripts/build_kg.py` is still stdlib-only and deterministic (two builds give identical output);
a build takes about 8 s.

## What changed

### New curated data files (`wiki/kg/`)
| file | what it holds |
|---|---|
| `aliases.json` | 241 variant concept ids → 196 canonical ids, chosen by reading the digest definitions |
| `merge-review.md` | 51 merges considered and **not** applied, each with a one-line reason |
| `field-map.json` | every free-text bridge target seen (1,891 strings) → one of the 12 field ids or `other:<name>` |
| `work-fields.json` | field overrides for 20 works (3 with unit-level additions: MacKay, Murphy, Ashby), each with a reason; 13 works checked and kept single-field |
| `instance-matches.json` | manual confirm list: 71 canon instances confirmed (to instance ids or `concept:<id>`), 6 rejected candidates |

### Generated outputs
- `unmatched-instances.md` (new): the 35 canon instances still unmatched, with fuzzy candidates.
- `hub-sources/<id>.md` (new): the generated version of each curated hub page.
- `merge-candidates.md`: now computed on canonical ids; groups already judged in `merge-review.md` are left out.
- `index.md`: new counts, strong-record cross-field ranking, curated hub list, problems and notes.
- `wiki/concepts/`: canonical pages list `aliases:` (frontmatter and an Aliases section) and every source
  definition with its digest link, page ref, and notes (`alias`, `new`, `weak`, work fields). 241 alias
  stub pages (`type: alias`, `alias_of:`) keep `[[variant]]` links in the digests working.

### `scripts/build_kg.py`
- **A. Aliases** applied after id normalisation; spine entries follow their alias, so one page shows all
  spine names that map to it. Canonical choice: the plain, readable id (e.g. `entropy`, `kl-divergence`);
  spine bundle ids of two different concepts (e.g. `mental-accounting-endowment-effect-loss-aversion`)
  are left alone.
- **B. Field map**: exact lookup in `field-map.json`, keyword rules only for unseen text. The rules were
  also fixed (`election` no longer matches "selection"; "agenda control" is political science; "X logic"
  is no longer philosophy). Policy: machine learning / deep learning → `llm` (the llm canon's textbook
  strand covers them); statistics, probability, physics, mathematics etc. → `other:<discipline>`; a
  concept name → the field of its canon spine entry or canonical instance.
- **C. Multi-field works**: a work listed under several fields in `canon/catalog.json` (MacKay, Jaynes;
  later Wiener, Centola) gets all of them automatically; `work-fields.json` adds overrides. Each record
  keeps `field` (primary, used as bridge source) and `fields` (all). Phase 1 had silently used only the
  last catalog listing.
- **D. Instances**: canon work ids are now parsed anywhere in the entry tail (e.g. "— osborne-2004-introduction (§2.2)");
  new `title-key` rule (same informative title tokens); manual confirmations, including concept-level
  matches; rejected pairs are filtered.
- **E. Parser**: the 7 phase-1 problem lines are handled — note lines such as "(none …)" are skipped as
  notes; labels like "Sentence (8), …" and bare descriptions with a page ref get an id; the two bridges
  without "↔" are split on "vs." / "like". Bullets that pack several `[[id]] — definition` entries are
  split (this also fixed 3 records whose definition contained other entries).
- **Weak records**: definitions that say the concept is only a canon link, loosely related, or not used
  in the unit (187 records) are flagged `weak`; cross-field counts use strong records only.
- **F. Curated guard**: a page with a `curated:` frontmatter key is never overwritten or deleted; its
  generated version goes to `hub-sources/`. Concept ids linked from hub pages get a page even with one digest.

## Before / after

| measure | phase 1 | phase 2 |
|---|---|---|
| distinct concept ids | 8,232 | 7,999 canonical (241 aliases) |
| concept pages | 1,766 | 1,679 (+241 alias stubs, +13 curated hubs among them) |
| merge-candidates.md | 4,583 lines; rule-1 groups 51 | 4,056 lines; rule-1 groups 0, rule-2 15, rule-3 66 |
| concepts in ≥ 3 fields, phase-1 method (all records, one field per work) | 86 | 108 (aliases only) |
| concepts in ≥ 3 fields, strong records, multi-field works | — | 197 (1,264 in ≥ 2 fields) |
| bridge targets mapped to a canon field | 2,135 = 42.5% of all, 48.3% of the 4,417 that name a target | 2,985 = 59.4% of all, 67.6% of named |
| canon instances matched by a digest instance id | 63 / 173 | 117 / 173 |
| … including confirmed concept-level matches | — | 138 / 173 (35 unmatched; 30 of these are from works not digested yet) |
| unparsed lines | 7 | 0 (2 bridge lines split on vs./like; 2 note lines skipped) |

The rise from 108 to 197 cross-field concepts comes mainly from multi-field works: a record of MacKay
ch. 39 now counts in information theory, Bayesian and llm. The index therefore ranks by fields, then
number of works, then digests, and shows the per-field record counts so a single work's spread is visible.

## Curated hub pages (13)

Chosen from the rebuilt cross-field ranking: `loss-function`, `bayes-theorem`, `feedback`, `likelihood`,
`kl-divergence`, `maximum-likelihood-estimation`, `entropy`, `curse-of-dimensionality`, `expected-utility`,
`overfitting`, `regularization`, `mutual-information`, `nash-equilibrium`. Softmax (2 fields) and
attention (1 field) are not cross-field in the digests, so they have no hub. Each hub has a one-line gist,
quotes per field with page refs, bridges with link type and justification (quoted from the digests'
Bridges sections), "where definitions disagree", and links to the digests.

## Verification

- Hub quotes: a script checks every “…” span on the 13 hub pages against the first digest linked after it:
  **299 / 299 exact substrings**. Page refs written as "— [[digest]] (ref)": **196 / 196 found in the digest**.
- Merged pages: 10 pages with aliases (kl-divergence, entropy, mutual-information, expected-utility,
  markov-chain-monte-carlo, hamiltonian-monte-carlo, bounded-rationality, principal-agent-problem,
  receive-accept-sample-model, self-information): **359 / 359 source definitions are verbatim substrings
  of their digests; all 25 listed aliases occur as links in those digests**.
- Every alias variant and canonical id exists in the records or the canon spine; no alias chains.
- Two consecutive builds produce byte-identical output.

## Update 2026-10-15 (after the post-01 fact-check)

User-approved changes; digests, `canon/` and `catalog.json` untouched by the KG code.

1. **Work maps skipped.** `digest_files()` now skips `wiki/works/<work>/index.md` (177 work maps, not
   digests). Without the skip the build read 1,516 files and reported 177 × 2 "missing section" problems;
   with it, 1,339 digests and no parse problems (same as the phase-2 build).
2. **ML / deep learning → `llm` (decision recorded).** Bridge targets naming machine learning or deep
   learning stay mapped to `llm` in `field-map.json` and in the keyword rules. Reason: the llm canon's
   textbook strand covers them, and there is no separate ML field. Revisit only if the canon adds an ML field.
3. **Mixed-sense ids split by record** (`wiki/kg/splits.json`, applied after id normalisation and before
   aliases; each record's sense chosen by reading its definition):
   | plain id | sense ids (records) |
   |---|---|
   | `value-function` | `value-function-econ` (thaler-2015 ch04), `value-function-rl` (todorov-2002) |
   | `priming` | `priming-media` (entman-1993, lazer-2018; carries the communication-theory spine entry), `priming-cognitive` (kahneman-2011 ch11) |
   | `paradox-of-voting` | `paradox-of-voting-turnout` (downs-1957, clark-2017 ch14, shepsle-2010 ch09; carries the political-science spine entry), `paradox-of-voting-cycle` (achen-2016 ch02, arrow-1951 ch05; joins arrow ch01's existing id) |
   | `stereotype` | `stereotype-social` (kahneman-2011 ch16), `stereotype-semantic` (putnam-1975); Lippmann's records already use `stereotype-lippmann` |
   The plain ids get a generated `type: disambiguation` page listing the senses, so `[[priming]]` etc. in
   the digests still resolve; every sense id gets a page. Records carry `split_from`. The build stops if an
   id is both a split id and an alias, and reports any split that matches no record.
4. **Kelly id mismatch.** `wiki/kg/work-aliases.json` maps `kelly-1956-new` (information-theory canon and
   catalog) → `kelly-1956-information` (digested work). Applied when reading the catalog (both listings now
   count for the work, so its tier becomes `core` instead of `deep`) and the canon instances (Kelly's
   gambler now matches `private-wire-gambler` by rule `same-work-tokens`, not only by the manual list).

| measure | phase 2 (committed) | after this update |
|---|---|---|
| digests parsed | 1,339 (1,516 if index.md were read) | 1,339 |
| distinct canonical concept ids | 7,999 | 8,002 |
| concept pages | 1,679 (+241 alias stubs) | 1,683 (+241 alias stubs, +4 disambiguation pages) |
| concepts in ≥ 3 / ≥ 2 fields (strong) | 197 / 1,264 | 197 / 1,261 |
| concept ids in one digest only | 6,423 | 6,427 |
| merge-candidate groups (rule 2 / rule 4) | 15 / 734 | 14 / 731 |
| canon instances matched (instance record / incl. concept) | 117 / 138 | 117 / 138 (Kelly now matched automatically) |
| parse problems | 0 | 0 |

Verification after the rebuild: hub quotes **299 / 299** exact substrings of the cited digest; page refs
**196 / 196** found (no hub-quoted digest text changed in the post-01 digest fixes, see
`pipeline/reviews/audit/post01-digest-fixes.md`). Two consecutive builds are byte-identical.

## Open issues

1. ~~Mixed-sense ids that an alias cannot split~~ — done by record-level splits (update above). Possible
   follow-ups for review: `priming-cognitive` ≟ `priming-effect` (Kahneman ch04), `priming-media` ≟
   `priming-agenda-setting`, `value-function-econ` ≟ `prospect-theory-value-function`; and confirming the
   canon instance "Paradox of voting (calculus of voting)" to `concept:paradox-of-voting-turnout` in
   `instance-matches.json`.
2. **51 review items** in `merge-review.md` need a human decision (e.g. `assignment-mechanism-ignorability`
   ≟ `ignorability`, `concept-drift` ≟ `concept-shift`, `shannon-information` ≟ `entropy`).
3. **merge-candidates.md is still long** (rule 4, containment, 734 ids): most are sub-concepts, not synonyms;
   further curation should be done on the ids with ≥ 2 digests first.
4. **Bridge targets**: 524 bridges name a target that is neither a field nor a known discipline/concept
   (mapped to `other:<slug>`), and 606 bridges name no target field at all. The ML → llm policy is now a
   recorded, user-approved decision (update above); change it in `field-map.json` only if the canon gets an ML field.
5. **Canon data issues (read-only)**: the Kelly work-id mismatch (`kelly-1956-new` vs `kelly-1956-information`)
   is now aliased inside the KG (`work-aliases.json`); the canon files themselves still carry both ids, and the
   Kelly gambler instance still appears in two canon files under two ids (both match `private-wire-gambler`).
6. **Unmatched canon instances**: 30 belong to works not digested; 5 have digested works but no matching
   instance (2008 financial crisis, Dennett's false-belief proposal, few-shot curves, least squares as
   orthogonal projection, Downs's paradox of voting).
7. **Weak-record flag** is a regular expression over the definition text; it may miss some loose uses and
   catch a few real ones.
8. **Hubs**: the curse-of-dimensionality hub contains one paragraph marked "Knowledge-manager reading (not a
   digest claim; for review)", and the loss-function hub one sentence marked as not stated by the digests.
   Per CHARTER §9, any claim taken from a hub into a post must be re-checked against the source page.
