"""Gate 2b regression test (reviews/gate2.md).

Part A: verifier v2 (P2) on the accepted v1 digests of 4 audited units; outputs -> pipeline/results/gate2b/A/.
        Scored by hand against the audit error IDs (C*, W*, J*, D*) in pipeline/reviews/audit/.
Part B: full v2 run on 5 units with the normal runner:
        python -m pipeline.gate2b reset-b && python -m pipeline run gate2b --out pipeline/results/gate2b/B

python -m pipeline.gate2b part-a | show-a | reset-b
"""
import json
import sys
import time
from pathlib import Path

from . import PIPE, REPO, state
from .build import SPEC_VERSION, p2_request
from .run import bucket, parse_verdict, text_of, usage_parts
from .vertex import CFG, batch_create, batch_wait, cost

OUT_A = PIPE / "results" / "gate2b" / "A"
V1 = {  # audited accepted v1 digests
    "cover-2006-elements/ch02-entropy": "wiki/works/cover-2006-elements/ch02-entropy.pipeline.md",
    "wittgenstein-1953-investigations/ch04-private": "wiki/works/wittgenstein-1953-investigations/ch04-private.md",
    "jaynes-2003-probability/ch02-quantitative": "wiki/works/jaynes-2003-probability/ch02-quantitative.md",
    "dennett-1987-intentional-stance/ch02-true": "wiki/works/dennett-1987-intentional-stance/ch02-true.md",
}
B_UNITS = list(V1) + ["mackay-2003-information/ch02-probability"]


def fn(uid):
    return uid.replace("/", "__")


def part_a():
    OUT_A.mkdir(parents=True, exist_ok=True)
    rows = []
    for uid, f in V1.items():
        req, _ = p2_request(uid, (REPO / f).read_text())
        rows.append({"custom_id": f"a__{fn(uid)}", "request": req})
    stamp = time.strftime("%Y%m%d-%H%M%S")
    blob = f"{CFG['gcs_prefix']}/gate2b/A-{stamp}/input.jsonl"
    bucket().blob(blob).upload_from_string("\n".join(json.dumps(r) for r in rows) + "\n")
    out = f"gs://{bucket().name}/{CFG['gcs_prefix']}/gate2b/A-{stamp}/output"
    job = batch_create(f"ai4read-gate2b-A-{stamp}", f"gs://{bucket().name}/{blob}", out)
    print("submitted part A:", job["name"].split("/")[-1], flush=True)
    batch_wait(job["name"], every=60)
    for bl in bucket().list_blobs(prefix=out.removeprefix(f"gs://{bucket().name}/")):
        if not bl.name.endswith("predictions.jsonl"):
            continue
        for line in bl.download_as_text().splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            uid = r["custom_id"].split("__", 1)[1].replace("__", "/")
            resp = r.get("response") or {}
            u = resp.get("usage", {})
            usd = cost(u, "batch_us")
            state.add_spend(usd, "gate2b-A", unit_id=uid, usage=usage_parts(u))
            (OUT_A / f"{fn(uid)}.p2v2.txt").write_text(text_of(resp))
            (OUT_A / f"{fn(uid)}.usage.json").write_text(json.dumps(
                {"usage": usage_parts(u), "usd": round(usd, 5), "stop": resp.get("stop_reason")}))
    print("part A done")


def show_a():
    for uid in V1:
        p = OUT_A / f"{fn(uid)}.p2v2.txt"
        if not p.exists():
            continue
        v = parse_verdict(p.read_text())
        u = json.loads((OUT_A / f"{fn(uid)}.usage.json").read_text())
        hc = v["h_checks"] or []
        print(f"===== {uid}: verdict {v['verdict']} | h_checks {len(hc)} "
              f"({sum(1 for h in hc if isinstance(h, dict) and h.get('ok') is False)} not ok) | "
              f"out {u['usage']['output']} think {u['usage']['thinking']} ${u['usd']}")
        for i in v["issues"] or []:
            if i.get("severity") in ("critical", "major"):
                print(f"  {i['severity'][:4]} {i.get('check')} | {i.get('where', '')[:60]} | {i.get('problem', '')[:260]}")


def reset_b():
    for uid in B_UNITS:
        state.record(uid, "planned", note=f"gate2b part B: rerun from scratch with spec {SPEC_VERSION} / prompts v2",
                     loop=0, p2_reruns=0)
    print("reset", len(B_UNITS), "units to planned")


if __name__ == "__main__":
    {"part-a": part_a, "show-a": show_a, "reset-b": reset_b}[sys.argv[1]]()
