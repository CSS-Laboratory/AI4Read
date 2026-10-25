# AI4Read component library (v1)

The writer composes widgets with **JSON configs**. It never writes JavaScript. One script (`widgets.js`) and one stylesheet (`widgets.css`) draw every widget. They work under the site's strict CSP: no `eval`, and formulas use the safe expression language below.

- **Gallery:** `gallery.html` shows every widget with a working example. Copy from it.
- **Numbers:** `node site/ai4read/components/check.mjs <post.html | config.json> [--values '{"p":0.3}'] [--seeds A] [--id cfg-id] [--hist]` prints every readout and every computed value. **Every number in the text that a widget can show must come from this output.** Never compute such numbers by hand.
- **Render test:** `node site/ai4read/components/test.mjs <page>` checks four things at 390 px under the strict CSP: 0 console errors, no horizontal scroll, page readouts equal to the Node computation, and working interactions.

## Placing a widget

```html
<div class="w" data-widget="lab" id="lab-bayes" data-config-ref="cfg-bayes"></div>
<script type="application/json" id="cfg-bayes">{ ...config... }</script>
```

Short configs can be inline: `data-config='{...}'` (single quotes outside, so no `'` inside). Every widget accepts `title`, `note` (a line under the title) and `caption` (a line at the bottom).

Label every toy in the title or caption: "(toy, ours)", or the source and page when a formula or number comes from a paper.

## Expression language

- Numbers: `0.5`, `1e-3`.
- Operators: `+ - * / % ^` (`^` is power, right-associative), comparisons `< > <= >= == !=`, `&& || !`, and `c ? a : b`.
- Functions: `exp ln log(=ln) log2 log10 sqrt abs min max pow floor ceil round sign sin cos tanh sigmoid clamp(x,a,b) if(c,a,b) fact(n) comb(n,k)`.
- Constants: `pi`, `e`.
- Variables: parameter ids, `constants`, earlier `derived` names, and the widget-specific names listed below.

**Templates** (`readout`, labels) insert values with `{expr}` or `{expr:fmt}`:

| fmt | example output |
|---|---|
| `.3f` | 0.941 |
| `.1%` | 94.1% |
| `,` | 4,096 |
| `,.2f` | 1,234.50 |
| `d` | 7 |
| `.2e` | 1.00e+6 |
| `.3g` | 0.941 |

Use `\n` in a readout for a new line.

## Widgets

### `lab`: sliders → derived values → readout (+ bars, + table, + presets)
| key | meaning |
|---|---|
| `params` | `[{id, label, min, max, step, value, fmt}]`, one slider each. `fmt` sets how the slider value is shown. |
| `constants` | `{name: number}` |
| `derived` | `{name: "expr"}`, evaluated in order; later entries may use earlier ones |
| `bars` | `{items:[{label, value:"expr"}], max, fmt, highlight: index, signed}`. With `"signed": true`, bars grow right for positive and left for negative values from a centre line (use it when a value can be negative). |
| `table` | `{head:[...], rows:[[cells]], fmt}`. A cell starting with `=` is an expression. |
| `presets` | `[{label, values:{paramId: value}}]`, buttons that set sliders. Use them for the edge case that teaches something. |
| `readout` | template |

### `plot`: curves y = f(x; params) and marked points
`x`/`y`: `{min, max, log, label, ticks:[...], tickFmt}`. `curves`: `[{expr (uses x), label}]` (at most 5). `points`: `[{x:"expr", y:"expr", label}]`. Also takes `params`, `derived`, `readout`, `samples`.

### `iterate`: a discrete-time system (feedback loops, bubbles, learning)
- `init`: `{var: expr}`. `update`: `{var: expr}`. All updates use the previous state (simultaneous); `t` is the step number. For a lag, keep the previous value in its own variable (`"Q":"P"`).
- `steps`: number or expr.
- `shocks`: `[{t, set:{var: expr}, label}]`, applied after step `t`.
- `series`: `[{var, label}]`. `y`: axis.
- The readout can use the final state plus `max_v`, `min_v`, `first_v` for each variable `v`, and `t`.

### `cascade`: failures spreading on an exposure network (systemic risk)
- `nodes`: `[{id, label, x, y, capital}]`, positioned on a 360-wide canvas (height `height`, default 240).
- `edges`: `[{from, to, w}]`. **Meaning: `to` is exposed to `from`.** If `from` fails, `to` loses `lgd × w`.
- Special params: `lgd` (default 1) and `capMult` (default 1).
- `seeds`: ids that fail at round 0. The reader taps a node to toggle it as a seed.
- A node fails when loss ≥ capital × capMult. Rounds are synchronous.
- The readout can use `failed`, `survivors`, `rounds` and `total`.

### `diagram`: boxes and arrows, optionally revealed in steps
- `nodes`: `[{id, x, y, w=90, h=34, label (\n for a new line), kind: bx|hl|soft|leaf|emb|ghost, round}]`.
- `edges`: `[{id, from, to, label, dashed, dx, dy}]`.
- `labels`: `[{x, y, text, a, c}]`. `width`, `height`.
- `steps`: `[{show:[ids], text}]`. Items named in no step are always shown; items in a step appear from that step on. With `"preview": true`, items of later steps are drawn faded from the start, so a tall diagram is never mostly blank on a phone.

### `vec2d`: vectors in the plane, a draggable probe direction, a draggable push (added 2026-10-25, post 03)
The reader drags arrows on a square grid (equal scale on both axes, so angles look right). Every drag moves the matching slider, and the sliders stay under the canvas for keyboard and screen-reader use. A focused arrow handle also moves with the arrow keys.
| key | meaning |
|---|---|
| `x`, `y` | `{min, max}` view ranges (default −6 to 6). `grid` (default 1) sets the grid step; `tickEvery` (default 2 × grid) the labels. |
| `params`, `constants`, `presets`, `readout`, `caption` | as in `lab`. |
| `pre` | `{name: "expr"}` evaluated **before** the geometry (for values the points or arrows use). |
| `probe` | `{x:"expr", y:"expr"}` the probe direction u (normalised unless `"normalize": false`). Options: `"line": false` hides the dashed line through the origin; `"feet": true` draws each point's foot on the line; `"boundary": true` (or an expr c) draws the line u·p = c. |
| `shift` | `{x:"expr", y:"expr", trail:true}` a vector v added to every point (steering). `trail` shows where each point came from. A point with `"fixed": true` is not shifted. |
| `points` | `[{x, y, label, group: 0/1/2}]`. Group 0 is blue, 1 red, 2 green. |
| `vectors` | `[{x, y, from:{x,y}, label, cls: c0–c4, scale, drag}]`. `scale` multiplies the drawn length only (say so in the caption). `drag`: `{angle:"paramId"}` turns the arrow (the angle is put into the slider's range; outside it, the nearer end is used); add `length:"paramId"` (with `lengthUnit`) to stretch it; or `{x:"paramId", y:"paramId"}` to move its tip freely. `drag.label` names the handle for screen readers. |
| `derived` | evaluated **after** the geometry and may use the variables below. |

Variables after the geometry: `ux, uy` (unit probe), `vx, vy` (shift), `uv` = u·v, and for point i (1-based) `x_i`, `y_i` (after the shift; written `x1`, `y1`, …) and `s_i` = u·(x_i, y_i) (written `s1`, `s2`, …); `n` is the number of points. Example: `"margin": "min(s4,min(s5,s6))-max(s1,max(s2,s3))"`. Copy the working example in `gallery.html` (`cfg-vec2d`).

### `stepper`: walk through a worked table row by row
`head`, `rows` (strings; compute them with `check.mjs` or code first), `notes` (one per row).

### `switch`: segmented panels
Written in HTML: `<div class="w" data-widget="switch"><section data-label="A">…</section><section data-label="B">…</section></div>`.

## Text blocks (post template classes, no JavaScript)
These come from the post stylesheet (post 01 `src/style.css`). Copy the markup from post 01 `src/content.html`:
- **Term box** `<div class="term"><p class="term-h">Term · …</p><p>…</p></div>`
- **Trap** `<div class="trap">`
- **Guess-first** `<div class="quiz" data-q="g1">` with `<p class="q">`, and the answer `<div class="reveal" data-for="g1">`. The question is copied into its answer automatically.
- **Exercise** `<div class="exercise">`
- **Deep-dive fold-out** `<details class="deep" id="box-…">` ("Look inside: …")
- **Citations** `<span class="cite">Author Year, p. N</span>`. The build links each one to its source entry `<li id="src-key">`. Name the author in every cite, or in the sentence just before it.
- **English section** `<section id="english">` blocks.

## Rules for the writer
1. One mechanism, one widget. Pick the simplest widget that lets the reader *do* the mechanism.
2. Every toy has an edge case that teaches something; expose it as a preset.
3. Numbers in prose come from `check.mjs` output. Quote the readout's numbers exactly.
4. Keep it phone-first: at most 4 sliders and 6–8 nodes, with labels of 2 words or fewer.
5. If no widget fits, describe the needed widget in an HTML comment `<!-- WIDGET-REQUEST: ... -->`. The meta-manager decides whether to add it to the library. Do not write custom JavaScript.
