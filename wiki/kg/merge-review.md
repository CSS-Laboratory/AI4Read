# Merge review (KG phase 2)

Merges that were considered and **not** applied. Each line: the two ids, and why the merge is
uncertain or wrong. Accepted merges are in `aliases.json`. A reviewer who confirms a merge adds it
to `aliases.json` and deletes the line here.

- `relative-entropy-shannon` ≟ `kl-divergence` — Shannon 1948 uses "relative entropy" for $H/H_{max}$ (shannon-1948-mathematical/main-p1, p. 14), not $D(p\|q)$. Different concept; kept apart.
- `cross-entropy` ≟ `kl-divergence` — Cover & Thomas list "cross entropy" as another name for $D(p\|q)$ (cover-2006-elements/ch02-entropy, p. 49); McElreath and Murphy define $H(p,q)=H(p)+D(p\|q)$. Same name, two quantities; kept apart.
- `thermodynamic-entropy` ≟ `entropy` — Boltzmann/Gibbs entropy $S=k\ln W$ (in J/K) vs Shannon $H$; the digests propose a same-math bridge, not identity.
- `value-function` ≟ `bellman-equation` — the id `value-function` mixes prospect theory's S-curve (thaler-2015-misbehaving) and the RL/optimal-control cost-to-go (todorov-2002-ofc); cannot be split by an alias.
- `heuristic` ≟ `heuristics-cues` — Kahneman's judgment heuristics vs political science's information shortcuts (cues) for voters; related, not the same concept.
- `heuristic` ≟ `bounded-rationality` — a heuristic is a tool of a boundedly rational agent; not a synonym.
- `mental-accounting-endowment-effect-loss-aversion` ≟ `loss-aversion / endowment-effect / mental-accounting` — canon spine bundles three concepts; the separate ids are kept and the bundle id is not merged into any of them.
- `confounding-vs-selection-bias` ≟ `confounding / selection-bias` — spine bundle of two distinct biases; not merged.
- `frequentist-vs-bayesian-inference` ≟ `bayesian-inference` — the contrast between schools is not the same as Bayesian inference itself.
- `orthonormal-basis-orthogonal-matrix` ≟ `orthonormal-basis / orthogonal-matrix` — spine bundle; an orthogonal matrix has orthonormal columns, but the concepts differ (list vs matrix).
- `dot-inner-product` ≟ `inner-product` — Axler's inner product is the general axiomatic notion that generalizes the dot product (axler-2024-ladr/ch06-inner-p1); special-case-of, not synonym.
- `paradigm-normal-science` ≟ `paradigm / normal-science` — Kuhn's paradigm and normal science are distinct notions bundled in the spine; also `paradigm` is used by Meadows for a society's deepest beliefs.
- `logical-form-vs-grammatical-form` ≟ `logical-form` — Popper's "logical form" of a hypothesis (falsifiability) is not the Russell-style contrast.
- `stereotype-lippmann` ≟ `stereotype` — Lippmann's pictures in the head vs Kahneman's group statement vs Putnam's semantic stereotype; three uses, kept apart.
- `boltzmann-softmax-rationality` ≟ `softmax` — a model of choice ($P\propto e^{\alpha U}$) vs the normalising function; related by same math, not the same concept.
- `back-door-front-door-criterion` ≟ `front-door-criterion` — two different identification criteria bundled in the spine.
- `attractor-basin-of-attraction` ≟ `attractor` — an attractor and its basin are different objects.
- `assignment-mechanism-ignorability` ≟ `ignorability` — ignorability is a property of an assignment mechanism; probably mergeable, left for review.
- `pretraining-fine-tuning` ≟ `fine-tuning` — Murphy's fine-tuning (adapt a pretrained network) is one half of the spine pair; left for review.
- `principal-agent-problem` ≟ `delegation` — Schelling's delegation (hand a decision to an agent with firmer resolve) is a commitment device, not the principal-agent problem.
- `market-failure-externality` ≟ `externality` — an externality is one cause of market failure; not a synonym.
- `modularity-tomm` ≟ `modularity` — network modularity $Q$ (rosvall-2008-maps) vs modules for theory of mind (Leslie); homonym.
- `revolutionary-threshold-cascade` ≟ `cascade` — Bak's sandpile domino cascade vs protest cascades; structural analogy, not identity.
- `social-choice-function-social-welfare-function` ≟ `social-welfare-function` — Arrow distinguishes the social welfare function (ordering) from choice functions.
- `dispersed-tacit-knowledge` ≟ `tacit-knowledge` — Hayek's dispersed local knowledge vs Polanyi's tacit (unarticulable) knowledge as cited by Kuhn.
- `framing-entman` ≟ `framing-effect` — emphasis framing (Entman; Chong & Druckman) vs equivalence framing (Kahneman, Thaler). See emphasis-vs-equivalency-framing.
- `encoding-decoding` ≟ `encoding` — Hall's encoding/decoding of meaning vs Pierce's encoding of a signal; homonym.
- `common-knowledge` ≟ `common-knowledge-vs-public-information` — the contrast in Morris & Shin is about public signals; kept as its own id.
- `priming` ≟ `priming-effect` — `priming` mixes media priming (Entman), cognitive priming (Kahneman ch11) and an agenda-setting quote (Lazer); cannot be split by an alias.
- `priming-agenda-setting` ≟ `agenda-setting / priming` — spine bundle of two media effects; not merged.
- `bootstrap` ≟ `bootstrapping` — statistical bootstrap (resampling) vs RL bootstrapping (update an estimate from an estimate); homonym.
- `feedforward` ≟ `feed-forward-mlp-block` — control feedforward (act on a measured disturbance before it hits the output) vs the feed-forward network block; homonym.
- `attention-model` ≟ `attention` — Lupia & McCubbins' attention model (principal pays to learn) is not neural attention; homonym.
- `sequential-monte-carlo` ≟ `particle-filter` — Murphy distinguishes SMC in general from particle filtering (SMC for filtering marginals).
- `shannon-information` ≟ `entropy` — Mitchell's "Shannon information" of a source is probably entropy; left for review.
- `tipping-point-k` ≟ `tipping-point` — Shepsle's k contributors needed vs tipping points in dynamical systems; structural analogy.
- `concept-drift` ≟ `concept-shift` — Grimmer's concept drift vs Murphy's concept shift (both p(y|x) change); close, left for review.
- `d-adic-distribution` ≟ `dyadic-distribution` — dyadic is the D = 2 case of D-adic; special-case-of.
- `switching-function-k` ≟ `switching-function` — Bellman's first-variation coefficients K_i vs Liberzon's switching function; same role, different objects.
- `reference-set-point` ≟ `reference` — the control-theory `reference` (astrom) is the same idea, but the bare id `reference` collides with philosophy's reference; not aliased.
- `system-1-system-2` ≟ `system-1 / system-2` — the pair id and the single systems are different granularity; kept.
- `two-systems-account` ≟ `system-1-system-2` — Apperly's two systems for mindreading vs Kahneman's System 1/2; structural analogy.
- `observer-state-estimator` ≟ `state-estimation / smoother` — Särkkä uses smoothers to reconstruct hidden states; not the observer.
- `statistical-linear-regression` ≟ `linear-regression` — Särkkä/Murphy's SLR is an approximation method, not regression on data.
- `transition-matrix` ≟ `markov-stochastic-matrix` — Kalman's state-transition matrix Φ is not a stochastic matrix.
- `relative-entropy-kl-divergence (cover ch02)` ≟ `cross-entropy` — the Cover ch02 record says the author also calls D "cross entropy" (p. 49); merged into kl-divergence, flagged on the hub page.
- `self-information-surprisal (cover ch02)` ≟ `self-information` — Cover uses "self-information" for $I(X;X)=H(X)$, not $-\log p(x)$; the record stays under self-information with its own definition.
- `probability-as-frequency` ≟ `probability-vs-frequency` — Ashby's operational frequency definition vs Jaynes's contrast; different.
- `efficiency-estimator` ≟ `efficient-estimator` — Gelman's efficiency ratio vs Cover's efficient estimator; different.
- `paradox-of-voting` ≟ `condorcet-paradox / paradox-of-voting-calculus-of-voting` — the id `paradox-of-voting` mixes the Condorcet majority cycle (achen-2016-realists, arrow-1951-socialchoice) and Downs's turnout paradox (downs-1957-democracy, clark-2017-principles, shepsle-2010-analyzing); needs a split in the digests, not an alias.
- `surprise` ≟ `self-information` — Kahneman's psychological surprise (violated expectation) is not surprisal.
