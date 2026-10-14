"""Per-wave measurement: cost per text/image page (v2.1), length vs target, tier re-forecast.

python -m pipeline.wave_report wave1   -> prints a markdown block (also written to pipeline/results/<wave>_report.md)
"""
import csv
import json
import statistics as st
import sys
from collections import defaultdict

from . import PIPE, state
from .build import PROMPT_VERSION, target_words
from .control import read as read_control
from .run import wave_units


def fit(rows):
    """Least squares without intercept: usd ~ a*text_pages + b*image_pages."""
    a11 = sum(t * t for t, i, _ in rows); a12 = sum(t * i for t, i, _ in rows); a22 = sum(i * i for t, i, _ in rows)
    b1 = sum(t * y for t, i, y in rows); b2 = sum(i * y for t, i, y in rows)
    det = a11 * a22 - a12 * a12
    return (b1 * a22 - b2 * a12) / det, (a11 * b2 - a12 * b1) / det


def main(wave):
    ids = set(wave_units(wave))
    U = {f"{r['work_id']}/{r['unit_id']}": r for r in csv.DictReader(open(PIPE / "units.csv"))}
    L = state.latest()
    first_ts = min(r["ts"] for r in (json.loads(l) for l in open(PIPE / "state" / "units.jsonl"))
                   if r["unit_id"] in ids and r["state"] == "p1_submitted")
    spend = defaultdict(lambda: defaultdict(float))
    for l in open(PIPE / "state" / "spend.jsonl"):
        s = json.loads(l)
        if s.get("unit_id") in ids and s["ts"] >= first_ts and s["what"] in ("p1", "p2", "p3", "p2fix"):
            spend[s["unit_id"]][s["what"]] += s["usd"]
    rows, allin, first = [], 0.0, 0.0
    for u in ids:
        n, im = int(U[u]["n_pages"]), int(U[u]["image_pages"])
        tot = sum(spend[u].values()); allin += tot
        f = spend[u]["p1"] + spend[u]["p2"]; first += f
        rows.append((n - im, im, tot))
    ct, ci = fit(rows)
    T = sum(t for t, _, _ in rows); I = sum(i for _, i, _ in rows)
    # length vs target
    ratios = []
    for u in ids:
        r = L.get(u, {})
        if r.get("state") == "accepted" and r.get("words"):
            ratios.append(r["words"] / (r.get("target_words") or target_words(U[u])))
    over = sum(1 for x in ratios if x > 1.5)
    q = st.quantiles(ratios, n=10) if len(ratios) > 2 else []
    # forecast
    out = {}
    for tier in ("core", "deep", "reference"):
        rs = [r for r in U.values() if r["action"] == "digest" and r["tier"] == tier]
        done = [r for r in rs if L.get(f"{r['work_id']}/{r['unit_id']}", {}).get("state") == "accepted"
                and L.get(f"{r['work_id']}/{r['unit_id']}", {}).get("prompt_version") in ("v2.1", "v2.2")]
        todo = [r for r in rs if r not in done]
        tp = sum(int(r["n_pages"]) - int(r["image_pages"]) for r in todo); ip = sum(int(r["image_pages"]) for r in todo)
        out[tier] = (len(todo), tp, ip, ct * tp + ci * ip)
    # verifier issues by check letter (A..H) and severity, from the last P2 text of each unit
    from .run import OUT, parse_verdict
    from collections import Counter
    by = Counter(); sev = Counter(); hfail = 0; hall = 0
    for u in ids:
        loop = L.get(u, {}).get("loop", 0) or 0
        f = OUT / f"{u.replace('/', '__')}.p2-{loop}.txt"
        if not f.exists():
            continue
        v = parse_verdict(f.read_text())
        for i in v["issues"] or []:
            if isinstance(i, dict):
                by[(i.get("check"), i.get("severity"))] += 1
                sev[i.get("severity")] += 1
        hc = [h for h in (v["h_checks"] or []) if isinstance(h, dict)]
        hall += len(hc); hfail += sum(1 for h in hc if h.get("ok") is False)
    names = {"A": "faithfulness", "B": "math", "C": "pages", "D": "coverage", "E": "numbers", "F": "labels",
             "G": "format/level", "H": "strength/voice"}
    issue_line = " · ".join(f"{names.get(c, c)} {sum(n for (cc, s), n in by.items() if cc == c)} "
                            f"({by.get((c, 'critical'), 0)}c/{by.get((c, 'major'), 0)}M)"
                            for c in "ABCDEFGH" if any(cc == c for (cc, _) in by))
    spent = state.spent()
    cap = read_control(do_pull=False).get("max_spend_usd", 300)
    md = [f"### {wave} measured (prompts {PROMPT_VERSION})",
          f"- Units: {len(ids)} ({sum(1 for u in ids if L.get(u, {}).get('state') == 'accepted')} accepted) · text pages {T} · image pages {I}",
          f"- Cost: all-in ${allin:.2f} (first pass P1+P2 ${first:.2f}; retries/fixes +{100 * (allin / first - 1):.0f}%)",
          f"- **Per page (all-in, least squares): text ${ct:.4f} · image ${ci:.4f}**",
          f"- Length vs target (accepted): median {st.median(ratios):.2f}× · 10–90%: {q[0]:.2f}–{q[-1]:.2f}× · > 1.5×: {over}/{len(ratios)}"
          if q else "- Length: n/a",
          f"- Verifier issues ({len(ids)} units): critical {sev.get('critical', 0)} · major {sev.get('major', 0)} · "
          f"minor {sev.get('minor', 0)} — by check: {issue_line}",
          f"- h_checks: {hall} items checked, {hfail} not ok ({100 * hfail / max(hall, 1):.1f}%)",
          "- **Re-forecast (remaining units, all-in rates):** " + " · ".join(
              f"{t} {n} units ${c:.0f}" for t, (n, tp, ip, c) in out.items()),
          f"- Total remaining ≈ ${sum(c for *_, c in out.values()):.0f} + spent ${spent:.0f} = **${spent + sum(c for *_, c in out.values()):.0f}** vs ${cap} cap",
          f"- **Core + deep: spent ${spent:.0f} + ${out['core'][3] + out['deep'][3]:.0f} = ${spent + out['core'][3] + out['deep'][3]:.0f}** "
          + ("✅ within" if spent + out['core'][3] + out['deep'][3] <= cap else "❌ **EXCEEDS**") + f" the ${cap} cap"
          + f" · core only: ${spent + out['core'][3]:.0f}"]
    text = "\n".join(md)
    (PIPE / "results" / f"{wave}_report.md").write_text(text + "\n")
    print(text)


if __name__ == "__main__":
    main(sys.argv[1])
