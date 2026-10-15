"""P4 work maps (DESIGN.md "Passes"): one wiki/works/<work>/index.md per multi-unit work, prompt prompts/work_index.md.

python -m pipeline.p4 plan        build requests, print forecast (no model call)
python -m pipeline.p4 submit      one Vertex batch job (refused if forecast > --max-usd or over the cap)
python -m pipeline.p4 collect     wait for the job, check each map, write index.md (never over an audited file)

Input per unit: title, L0, L1 (+ Prerequisites line) and L2 of the accepted digest, plus its Concepts links
(the prompt's "Concepts introduced" section needs real concept ids; L0-L2 rarely contain them).
"""
import argparse
import json
import re
import sys
import time
from pathlib import Path

from . import PIPE, REPO, control, state
from .build import _req, fields_of, units
from .checks import sections, split_frontmatter
from .run import bucket, text_of, usage_parts, strip_preamble
from .vertex import CFG, batch_create, batch_get, cost

WORK = PIPE / "_work" / "p4"
JOB = PIPE / "state" / "p4_jobs.jsonl"
MAP_SECTIONS = ["In one paragraph", "The path through the work", "Big ideas across units", "How to read it",
                "Concepts introduced"]
CHARS_PER_TOKEN = 3.6
PRICE = CFG["prices_usd_per_mtok"]["batch_us"]


def catalog():
    return {c["id"]: c for c in json.loads((REPO / "canon" / "catalog.json").read_text())}


def works():
    """{work_id: [unit ids in plan order]} for works with >= 2 accepted units."""
    L = state.latest()
    out = {}
    for uid, row in units().items():
        if L.get(uid, {}).get("state") == "accepted" and L[uid].get("path"):
            out.setdefault(row["work_id"], []).append(uid)
    return {w: us for w, us in out.items() if len(us) >= 2}


def unit_block(uid):
    md = (REPO / state.latest()[uid]["path"]).read_text()
    fm, body = split_frontmatter(md)
    sec = dict(sections(body))
    concepts = re.findall(r"\[\[[^\]]+\]\](?:\s*\(new\))?", sec.get("Concepts", ""))
    title = (fm or {}).get("unit", "") if isinstance(fm, dict) else ""
    parts = [f'<unit id="{uid}" title="{title}">']
    for name in ("L0", "L1", "L2"):
        parts.append(f"## {name}\n{sec.get(name, '').strip()}")
    parts.append("Concept links in this unit: " + (", ".join(concepts) or "none"))
    parts.append("</unit>")
    return "\n".join(parts)


def request(work, uids, cat):
    entry = cat.get(work, {"id": work})
    text = (f"Work id: {work}\nCatalog entry:\n{json.dumps(entry, ensure_ascii=False, indent=1)}\n\n"
            f"Accepted unit digests, in order ({len(uids)} units):\n\n" + "\n\n".join(unit_block(u) for u in uids))
    return _req("p4", fields_of(work), [{"type": "text", "text": text}])


def forecast(req, n_units):
    chars = sum(len(b["text"]) for b in req["system"]) + len(req["messages"][0]["content"][0]["text"])
    inp = chars / CHARS_PER_TOKEN
    out = 1500 + 90 * n_units + 4000          # map text + per-unit path/concept lines + thinking
    return (inp * PRICE["input"] + out * PRICE["output"]) / 1e6


def check_map(md, work, uids):
    issues = []
    fm, body = split_frontmatter(md.strip())
    if not isinstance(fm, dict):
        return ["frontmatter missing or not valid YAML"]
    if fm.get("id") != f"{work}/index" or fm.get("type") != "work-map":
        issues.append(f"frontmatter id/type wrong: {fm.get('id')} / {fm.get('type')}")
    if list(fm.get("units") or []) != uids:
        issues.append("frontmatter units differ from the accepted units")
    sec = dict(sections(body))
    for s in MAP_SECTIONS:
        if s not in sec:
            issues.append(f"missing section '{s}'")
    para = sec.get("In one paragraph", "")
    if len(para.split()) > 165:                  # 150 + 10%
        issues.append(f"one-paragraph summary has {len(para.split())} words (> 150)")
    path = re.findall(r"\[\[([^\]|]+)\]\]", sec.get("The path through the work", ""))
    if path != uids:
        missing = [u for u in uids if u not in path]
        extra = [p for p in path if p not in uids]
        issues.append(f"path links differ from units (missing {missing[:5]}, extra {extra[:5]})")
    unit_links = set(re.findall(r"\[\[(" + re.escape(work) + r"/[^\]|]+)\]\]", body))
    bad = sorted(unit_links - set(uids))
    if bad:
        issues.append(f"links to unknown units: {bad[:5]}")
    return issues


def write_map(work, md):
    p = REPO / "wiki" / "works" / work / "index.md"
    if p.exists() and re.search(r"^audited:", p.read_text(), re.M):
        p = p.with_name("index.pipeline-new.md")          # never overwrite an audited file
    p.write_text(md.strip() + "\n")
    return p


def cmd_plan(a):
    WORK.mkdir(parents=True, exist_ok=True)
    W, cat = works(), catalog()
    if a.works:
        W = {w: W[w] for w in a.works}
    rows, total = [], 0.0
    with open(WORK / "requests.jsonl", "w") as f:
        for w, uids in W.items():
            req = request(w, uids, cat)
            fc = forecast(req, len(uids))
            total += fc
            rows.append((w, len(uids), fc))
            f.write(json.dumps({"custom_id": w, "request": req}) + "\n")
    json.dump({w: uids for w, uids in W.items()}, open(WORK / "works.json", "w"), indent=1)
    big = sorted(rows, key=lambda r: -r[2])[:5]
    print(f"{len(W)} multi-unit works, {sum(r[1] for r in rows)} units; forecast ${total:.2f}")
    print("largest: " + "; ".join(f"{w} ({n} units, ${fc:.2f})" for w, n, fc in big))
    return total


def cmd_submit(a):
    total = cmd_plan(a)
    ctl = control.read(do_pull=True)
    if ctl["mode"] == "stop":
        sys.exit("control: stop")
    room = ctl["max_spend_usd"] - state.spent()
    if total > a.max_usd or total > room:
        sys.exit(f"STOP: forecast ${total:.2f} > limit ${min(a.max_usd, room):.2f}")
    stamp = time.strftime("%Y%m%d-%H%M%S")
    blob = f"{CFG['gcs_prefix']}/p4/{stamp}/input.jsonl"
    bucket().blob(blob).upload_from_string((WORK / "requests.jsonl").read_text())
    out = f"gs://{bucket().name}/{CFG['gcs_prefix']}/p4/{stamp}/output"
    job = batch_create(f"ai4read-p4-{stamp}", f"gs://{bucket().name}/{blob}", out)
    rec = {"ts": stamp, "job": job["name"], "output": out, "forecast_usd": round(total, 4),
           "works": json.load(open(WORK / "works.json"))}
    with open(JOB, "a") as f:
        f.write(json.dumps(rec) + "\n")
    print(f"submitted p4 for {len(rec['works'])} works: {job['name'].split('/')[-1]} (forecast ${total:.2f})")


def cmd_collect(a):
    rec = [json.loads(l) for l in open(JOB) if l.strip()][-1]
    while True:
        st = batch_get(rec["job"])["state"]
        if st not in ("JOB_STATE_PENDING", "JOB_STATE_RUNNING", "JOB_STATE_QUEUED"):
            break
        time.sleep(a.sleep)
    print(f"job {rec['job'].split('/')[-1]} -> {st}")
    W, results, usd = rec["works"], {}, 0.0
    prefix = rec["output"].removeprefix(f"gs://{bucket().name}/")
    for bl in bucket().list_blobs(prefix=prefix):
        if not bl.name.endswith(".jsonl") or "incremental_predictions" in bl.name:
            continue
        for line in bl.download_as_text().splitlines():
            r = json.loads(line) if line.strip() else {}
            w = r.get("custom_id")
            resp = r.get("response") or {}
            if not w or w in results or not resp.get("content"):
                continue
            c = cost(resp.get("usage", {}), "batch_us")
            usd += c
            state.add_spend(c, "p4", work=w, job=rec["job"], usage=usage_parts(resp.get("usage", {})))
            results[w] = (strip_preamble(text_of(resp)), resp.get("stop_reason"))
    report = []
    for w, uids in W.items():
        if w not in results:
            report.append({"work": w, "status": "no result"})
            continue
        md, stop = results[w]
        (WORK / f"{w}.index.md").write_text(md)
        issues = check_map(md, w, uids) + ([f"stop_reason {stop}"] if stop != "end_turn" else [])
        p = write_map(w, md)
        report.append({"work": w, "units": len(uids), "status": "ok" if not issues else "issues",
                       "issues": issues, "path": str(p.relative_to(REPO)), "words": len(md.split())})
    (PIPE / "results" / "p4_report.json").write_text(json.dumps(report, indent=1))
    ok = sum(r["status"] == "ok" for r in report)
    print(f"{ok}/{len(report)} maps pass checks; spend ${usd:.2f}; total ${state.spent():.2f}")
    for r in report:
        if r["status"] != "ok":
            print(f"  {r['work']}: {r.get('issues') or r['status']}")


def main(argv=None):
    ap = argparse.ArgumentParser(prog="pipeline.p4")
    ap.add_argument("cmd", choices=["plan", "submit", "collect"])
    ap.add_argument("--works", nargs="*")
    ap.add_argument("--max-usd", type=float, default=10.0)
    ap.add_argument("--sleep", type=int, default=120)
    a = ap.parse_args(argv)
    {"plan": cmd_plan, "submit": cmd_submit, "collect": cmd_collect}[a.cmd](a)


if __name__ == "__main__":
    main()
