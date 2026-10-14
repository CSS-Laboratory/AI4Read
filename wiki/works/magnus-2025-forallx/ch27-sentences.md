---
id: magnus-2025-forallx/ch27-sentences
work: magnus-2025-forallx
unit: "27 Sentences of FOL"
pages: 235–242
fields: [analytic-philosophy]
level: HS
grounding: primary-text
digested_by: claude-sonnet-5-5
digested_on: 2026-10-14
spec_version: 1.2
prompt_version: v2.2
verified: repaired
verifier_issues: 6
pipeline_version: 0.1
---
# Sentences of FOL

## L0 — One line
A sentence of FOL is a formula, built by recursive rules from terms, predicates, connectives and quantifiers, in which no variable is free.

## L1 — The gist (≤ 120 words)
The chapter asks what exactly counts as a sentence of first-order logic (FOL). The answer goes in stages. First come the six kinds of symbols. Then terms and atomic formulas. Then formulas, built by nine recursion clauses. A sentence is a formula with no free variables. A variable occurrence is bound if it lies inside the scope of a quantifier (the subformula it governs) that uses the same variable. Otherwise it is free. This matters because only sentences can be true or false. The chapter also fixes bracketing shortcuts and explains why predicates carry no superscripts for their number of places.

**Prerequisites:** the TFL recursive definition of "sentence" (ch. 6); quantifiers and predicates in FOL; the idea of a metalanguage (ch. 8).

## L2 — Key ideas
- FOL has six kinds of symbols. An expression is any string of them, in any order (p. 235).
- Formulas are defined in stages: terms, then atomic formulas, then recursion clauses. The first recursion clauses are analogous to the TFL ones (TFL is the earlier language of ch. 6); two quantifier clauses are added (pp. 236–237).
- The main logical operator is the one introduced last. Its scope is the subformula it is the main operator of. Connectives and quantifiers are both operators (p. 238).
- A variable occurrence is bound iff it is in the scope of a quantifier on that variable. Otherwise it is free. A sentence is a formula with no free variables, and only sentences can be true or false (pp. 239–240).
- The formation rules are permissive. They allow repeated quantifiers on one variable and vacuous quantification (a quantifier that binds no variable). A "closest quantifier" rule says which quantifier binds which occurrence (p. 240).
- Long conjunctions and disjunctions may drop inner brackets. Mixed connectives may not (p. 241).
- Predicates carry no superscripts. When the number of places could be unclear, you should say it (p. 242).

## L3 — Walkthrough

### 27.1 Expressions
There are six kinds of symbols (p. 235):
1. Predicates: $A, B, \dots, Z$, with subscripts if needed. The identity sign "=" is a special predicate.
2. Names: $a, b, \dots, r$, with subscripts.
3. Variables: $s, t, u, v, w, x, y, z$, with subscripts.
4. Connectives: $\neg, \wedge, \vee, \to, \leftrightarrow$.
5. Brackets: $($ and $)$.
6. Quantifiers: $\forall, \exists$.

An *expression of FOL* is any string of these symbols (p. 235).

### 27.2 Terms and formulas
The intuitive idea is that a formula is a sentence, or something that becomes a sentence when quantifiers are added in front. FOL needs this intermediate notion, unlike TFL (p. 236).

**Term:** any name or any variable (p. 236).

**Atomic formula** (p. 236):
1. Any sentence letter.
2. If $\mathcal{R}$ is an $n$-place predicate and $t_1,\dots,t_n$ are terms, then $\mathcal{R}(t_1,\dots,t_n)$.
3. If $t_1,t_2$ are terms, then $t_1=t_2$.
4. Nothing else.

Sentence letters count as formulas, so every TFL sentence is an FOL formula (p. 236). Script letters such as $\mathcal{R}$ and $t_1$ belong to the metalanguage. They talk about any predicate or term and are not FOL symbols (p. 236).

Examples, with $F$ one-place, $G$ three-place, $S$ six-place (p. 237): $D$, $x=a$, $a=b$, $F(x)$, $F(a)$, $G(x,a,y)$, $G(a,a,a)$, $S(x_1,x_2,a,b,y,x_1)$.

**Formula** (recursion clauses, p. 237):
1. Every atomic formula is a formula.
2. If $\mathcal{A}$ is a formula, so is $\neg\mathcal{A}$.
3. If $\mathcal{A},\mathcal{B}$ are formulas, so is $(\mathcal{A}\wedge\mathcal{B})$.
4. Likewise $(\mathcal{A}\vee\mathcal{B})$.
5. Likewise $(\mathcal{A}\to\mathcal{B})$.
6. Likewise $(\mathcal{A}\leftrightarrow\mathcal{B})$.
7. If $\mathcal{A}$ is a formula and $x$ a variable, $\forall x\,\mathcal{A}$ is a formula.
8. Likewise $\exists x\,\mathcal{A}$.
9. Nothing else is a formula.

Build-up example (p. 238): $F(x)$; $G(a,y,z)$; $S(y,z,y,a,y,x)$; then $(G(a,y,z)\to S(y,z,y,a,y,x))$; then $\forall z(\dots)$; then $F(x)\wedge\forall z(\dots)$; then $\exists y(\dots)$; then $\forall x\exists y(\dots)$.

**Main logical operator:** the operator introduced most recently when the formula was built. **Scope** of an operator: the subformula for which it is the main logical operator. Operators are connectives or quantifiers (p. 238). The text illustrates nested scopes of $\forall x$, $\exists y$, $\forall z$ with braces (p. 238).

*Intuition note:* A formula is like a tree built from the bottom up. The last step you took is the main operator, and its scope is everything it governs.

### 27.3 Sentences and free variables
A variable such as $z$ in $L(z,z)$ names nothing, so $L(z,z)$ is a formula but cannot be true or false. A quantifier is needed: $\exists z\,L(z,z)$ is true iff someone loves themselves, and $\forall z\,L(z,z)$ is true iff everyone does (p. 239).

**Bound / free:** an occurrence of $x$ is *bound* iff it falls within the scope of $\forall x$ or $\exists x$. Otherwise it is *free* (p. 239).

Example (p. 239): $(\forall x(E(x)\vee D(y)))\to\exists z(E(x)\to L(z,x))$. The first $x$ is bound. The second and third $x$ are free, and $y$ is free. $z$ is bound.

**Sentence of FOL:** a formula with no free variables. Only sentences can be true or false (p. 240).

*Intuition note:* A free variable is a blank that nothing has filled. Until a quantifier handles it, the formula does not say anything definite.

Permissive rules (p. 240):
- The rules do not forbid reusing a variable already bound inside $\mathcal{A}$. So $\exists x(\forall x\,F(x)\to G(x))$ is a sentence. Renaming bound variables gives an equivalent sentence, e.g. $\exists x(\forall y\,F(y)\to G(x))$.
- *Closest-quantifier rule:* a bound occurrence is bound by the quantifier on the same variable that is closest to it. "Closest" means it is the main logical operator of the smallest subformula into the scope of which the occurrence falls. In the example, $\forall x$ binds $x$ in $F(x)$ but not in $G(x)$. $\exists x$ binds only the $x$ in $G(x)$.
- The rules do not require that $x$ occur free in $\mathcal{A}$. So $\exists x\,F(a)$ and $\exists x\forall x\,G(x)$ are formulas. This is *vacuous quantification*. It is rare and harmless: they are equivalent to $F(a)$ and $\forall x\,G(x)$.

### 27.4 Bracketing conventions
As in TFL, the outermost brackets may be omitted. Square brackets may replace round ones for readability (p. 241).

$A_1\wedge A_2\wedge\dots\wedge A_n$ and $A_1\vee\dots\vee A_n$ are read as $(\dots(A_1\wedge A_2)\wedge\dots\wedge A_n)$ and $(\dots(A_1\vee A_2)\vee\dots\vee A_n)$. You may only drop inner brackets. The whole chain must still be bracketed unless it is the outermost expression. You may not mix $\wedge$ and $\vee$, or other connectives: $A\vee B\wedge C\wedge D$ and $B\vee C\to D$ are not allowed (p. 241).

### 27.5 Superscripts on predicates
Predicate letters do not show how many places they have. The same $G$ may be one-place in one place and three-place in another, so it is indeterminate whether $G(a)$ is atomic (pp. 241–242). One fix is superscripts: $G^1(a)$ and $G^3(a,b,c)$ would be atomic, while $G^3(a)$ and $G^1(a,b,c)$ would not. $G^1$ and $G^3$ would be different predicates with separate key entries (p. 242). The authors reject this because it makes formulas harder to read. When ambiguity could arise, which is very rarely, you should state the number of places (p. 242).

## Toy example (ours)
Formula: $\forall x(F(x)\to R(x,y))$, with $F$ one-place and $R$ two-place.
1. $F(x)$ and $R(x,y)$ are atomic (clause 2 of atomic formulas).
2. $(F(x)\to R(x,y))$ is a formula (clause 5).
3. $\forall x(F(x)\to R(x,y))$ is a formula (clause 7). Its main operator is $\forall x$, and its scope is the whole formula.
4. Both occurrences of $x$ lie in the scope of $\forall x$, so they are bound. $y$ lies in no quantifier's scope, so it is free.
5. A free variable remains, so this is a formula but not a sentence.
6. Adding $\exists y$ gives $\exists y\forall x(F(x)\to R(x,y))$. Now $y$ is bound and no variable is free, so it is a sentence.

## Concepts
- [[fol-symbols]] (new) — six kinds of symbol: predicates, names, variables, connectives, brackets, quantifiers (p. 235)
- [[fol-expression]] (new) — any string of FOL symbols, well-formed or not (p. 235)
- [[fol-term]] (new) — a name or a variable (p. 236)
- [[atomic-formula]] (new) — sentence letter, $\mathcal{R}(t_1,\dots,t_n)$, or $t_1=t_2$ (p. 236)
- [[fol-formula]] (new) — anything built by the nine recursion clauses (p. 237)
- [[main-logical-operator-scope]] (new) — the last-introduced operator, and the subformula it governs (p. 238)
- [[bound-free-variable]] (new) — bound if inside the scope of a quantifier on that variable; else free (p. 239)
- [[fol-sentence]] (new) — a formula with no free variables; only these are true or false (p. 240)
- [[vacuous-quantification]] (new) — a quantifier that binds no variable; harmless (p. 240)
- [[predicate-arity-superscripts]] (new) — optional superscripts fixing the number of places; not adopted (p. 242)

## Canonical instances
- [[free-variable-L(z,z)]] — $L(z,z)$ is a formula that is not truth-evaluable; $\exists z\,L(z,z)$ is (p. 239)
- [[repeated-quantifier-example]] — $\exists x(\forall x\,F(x)\to G(x))$ shows the closest-quantifier rule (p. 240)
- [[G-arity-ambiguity]] — whether $G(a)$ is atomic depends on the arity of $G$ (p. 242)

## Bridges (candidates)
- [structural-analogy] Recursive formula definition ↔ computer science: grammar rules that generate valid strings — each clause builds bigger well-formed objects from smaller ones.
- [structural-analogy] Bound vs. free variable ↔ mathematics/programming: a local dummy variable vs. a variable that must be supplied — only the bound kind is "internal" to the expression.
- [structural-analogy] Main logical operator and scope ↔ the TFL case of main operator and scope (p. 238: "Here we follow the case of TFL") — quantifiers now count as operators too.

## Questions this raises
- If formation rules allow odd cases such as $\exists x\forall x\,G(x)$, why not forbid them, and what is gained or lost?
- How does the truth of a quantified sentence get defined when its subformulas contain free variables?
- Does the left-nested bracketing convention matter for truth value in long conjunctions and disjunctions?

## Exercises worth doing
- Ex. A.1 (p. 242) — find bound and free occurrences when the same variable appears both bound and free — difficulty: easy
- Ex. A.3 (p. 242) — $x$ is bound in one conjunct but free in another — difficulty: easy
- Ex. A.4 (p. 242) — nested quantifiers with square brackets and a free $z$ — difficulty: medium
- Ex. A.5 (p. 242) — subscripted variables $x_1,x_2,x_3$ with quantifiers on some — difficulty: medium

## Reading notes
- Printed page = pdf − 10 (pdf 245–252 ↔ pp. 235–242).
- Misprint on p. 238: the build-up list ends with $F(x)\wedge\forall z(\dots)$, but the scope diagram uses $F(x)\leftrightarrow\forall z(\dots)$. The images show these two connectives differ. The diagram's scopes still hold either way.
- In 27.2 the text says "In part VII, we will again also allow the contradiction ‘⊥’ as an atomic formula" (p. 236). This unit does not explain it.
- Only the five practice items of exercise set A (p. 242) appear in this unit. No solutions are printed.
