"""A/B test of cost levers on pilot units (approved by Kunhao 2026-10-13).

Arms
  E1  P2 effort: re-verify the pilot's loop-0 P1 digest at effort medium and low (baseline = pilot P2 at high).
  E2  image size: P1 at 1200 px long side (baseline 1500), then verified by P2 at 1500 px / high.

python -m pipeline.ab stage1 | stage2 | report
"""
import json
import sys
import time
from collections import Counter
from pathlib import Path

from . import PIPE, build, state
from .build import p1_request, p2_request
from .checks import check, errors
from .run import OUT, bucket, parse_verdict, strip_fence, text_of, usage_parts
from .vertex import CFG, batch_create, batch_wait, cost

AB = PIPE / "_work" / "ab"
LOG = PIPE / "state" / "ab.jsonl"
E1_UNITS = ["cover-2006-elements/ch02-entropy", "mackay-2003-information/ch02-probability",
            "dennett-1987-intentional-stance/ch02-true", "kahneman-2011-thinking/ch03-lazy"]
E2_UNITS = E1_UNITS[:3]                       # units with page images


def fn(uid):
    return uid.replace("/", "__")


def p1_digest(uid):
    return (OUT / f"{fn(uid)}.p1-0.md").read_text()


def submit(name, rows):
    stamp = time.strftime("%Y%m%d-%H%M%S")
    blob = f"{CFG['gcs_prefix']}/ab/{name}-{stamp}/input.jsonl"
    bucket().blob(blob).upload_from_string("\n".join(json.dumps(r) for r in rows) + "\n")
    out = f"gs://{bucket().name}/{CFG['gcs_prefix']}/ab/{name}-{stamp}/output"
    job = batch_create(f"ai4read-ab-{name}-{stamp}", f"gs://{bucket().name}/{blob}", out)
    print("submitted", name, len(rows), "rows:", job["name"].split("/")[-1], flush=True)
    batch_wait(job["name"], every=60)
    res = {}
    for bl in bucket().list_blobs(prefix=out.removeprefix(f"gs://{bucket().name}/")):
        if bl.name.endswith("predictions.jsonl"):
            for line in bl.download_as_text().splitlines():
                if line.strip():
                    r = json.loads(line)
                    res[r["custom_id"]] = r.get("response") or {}
    return res


def record(arm, uid, resp, **kw):
    u = resp.get("usage", {})
    usd = cost(u, "batch_us")
    state.add_spend(usd, f"ab-{arm}", unit_id=uid, usage=usage_parts(u))
    rec = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "arm": arm, "unit_id": uid, "usd": round(usd, 5),
           "usage": usage_parts(u), "stop": resp.get("stop_reason"), **kw}
    with open(LOG, "a") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    return rec


def stage1():
    AB.mkdir(parents=True, exist_ok=True)
    rows = []
    for uid in E1_UNITS:
        for eff in ("medium", "low"):
            req, _ = p2_request(uid, p1_digest(uid))
            req["output_config"] = {"effort": eff}
            rows.append({"custom_id": f"p2-{eff}__{fn(uid)}", "request": req})
    build.LONG_SIDE = 1200
    for uid in E2_UNITS:
        req, stats = p1_request(uid)
        rows.append({"custom_id": f"p1-1200__{fn(uid)}", "request": req})
    build.LONG_SIDE = CFG["image"]["long_side_px"]
    res = submit("stage1", rows)
    for cid, resp in res.items():
        arm, f = cid.split("__", 1)
        uid = f.replace("__", "/")
        txt = text_of(resp)
        (AB / f"{cid}.txt").write_text(txt)
        if arm.startswith("p2"):
            v = parse_verdict(txt)
            record(arm, uid, resp, verdict=v["verdict"], issues=v["issues"],
                   n_edits=len(v["edits"] or []), rewrite=bool(v["corrected"]))
        else:
            md = strip_fence(txt)
            (AB / f"{cid}.md").write_text(md)
            record(arm, uid, resp, det_errors=[e["msg"] for e in errors(check(md, build.units()[uid], uid))])
    print("stage1 done:", len(res), "results")


def stage2():
    rows = []
    for uid in E2_UNITS:
        md = (AB / f"p1-1200__{fn(uid)}.md").read_text()
        req, _ = p2_request(uid, md)              # verifier sees 1500 px images, effort high (default)
        rows.append({"custom_id": f"p2-high-on-1200__{fn(uid)}", "request": req})
    res = submit("stage2", rows)
    for cid, resp in res.items():
        arm, f = cid.split("__", 1)
        uid = f.replace("__", "/")
        txt = text_of(resp)
        (AB / f"{cid}.txt").write_text(txt)
        v = parse_verdict(txt)
        record(arm, uid, resp, verdict=v["verdict"], issues=v["issues"], n_edits=len(v["edits"] or []),
               rewrite=bool(v["corrected"]))
    print("stage2 done:", len(res), "results")


def baseline_p2(uid):
    v = parse_verdict((OUT / f"{fn(uid)}.p2-0.txt").read_text())
    return v


def sev(issues):
    c = Counter(i.get("severity") for i in issues or [])
    return f"{c.get('critical', 0)}c/{c.get('major', 0)}M/{c.get('minor', 0)}m"


def report():
    recs = [json.loads(l) for l in LOG.read_text().splitlines() if l.strip()]
    L = state.latest()
    print("E1 — P2 effort on the same P1 digest")
    for uid in E1_UNITS:
        b = baseline_p2(uid)
        bu = L[uid].get("p2_usage", {})
        print(f"  {uid}\n    high  : {b['verdict']:7s} {sev(b['issues'])}  out {bu.get('output')} (think {bu.get('thinking')})")
        for r in recs:
            if r["unit_id"] == uid and r["arm"] in ("p2-medium", "p2-low"):
                print(f"    {r['arm'][3:]:6s}: {r['verdict']:7s} {sev(r['issues'])}  out {r['usage']['output']} "
                      f"(think {r['usage']['thinking']})  ${r['usd']:.3f}")
    print("E2 — P1 images 1200 px (judged by P2 @1500/high)")
    for uid in E2_UNITS:
        b = baseline_p2(uid)
        bu = L[uid].get("p1_usage", {})
        p1 = next(r for r in recs if r["unit_id"] == uid and r["arm"] == "p1-1200")
        j = next((r for r in recs if r["unit_id"] == uid and r["arm"] == "p2-high-on-1200"), None)
        print(f"  {uid}\n    1500: P1 in {bu.get('input', 0) + bu.get('cache_read', 0) + bu.get('cache_write', 0)}"
              f" out {bu.get('output')} | verdict {b['verdict']} {sev(b['issues'])}")
        u = p1["usage"]
        print(f"    1200: P1 in {u['input'] + u['cache_read'] + u['cache_write']} out {u['output']} ${p1['usd']:.3f}"
              f" det={p1['det_errors']} | verdict {j and j['verdict']} {j and sev(j['issues'])}")


if __name__ == "__main__":
    {"stage1": stage1, "stage2": stage2, "report": report}[sys.argv[1]]()
