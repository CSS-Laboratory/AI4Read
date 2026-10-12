"""Thin Vertex AI helpers: online call (global) and batch jobs (us multi-region, GCS JSONL)."""
import json
import time

import google.auth
import google.auth.transport.requests
import requests
import yaml

from . import PIPE

CFG = yaml.safe_load((PIPE / "config.yaml").read_text())


def _session():
    creds, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    creds.refresh(google.auth.transport.requests.Request())
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {creds.token}"
    return s


def host(location):
    if location == "global":
        return "https://aiplatform.googleapis.com"
    if location in ("us", "eu"):
        return f"https://aiplatform.{location}.rep.googleapis.com"
    return f"https://{location}-aiplatform.googleapis.com"


def cost(usage, kind="batch_us"):
    p = CFG["prices_usd_per_mtok"][kind]
    inp = usage.get("input_tokens", 0) * p["input"]
    out = usage.get("output_tokens", 0) * p["output"]
    inp += usage.get("cache_read_input_tokens", 0) * p.get("cache_hit", p["input"])
    inp += usage.get("cache_creation_input_tokens", 0) * p.get("cache_write_5m", p["input"])
    return (inp + out) / 1e6


def online(body, location=None):
    loc = location or CFG["online_location"]
    url = (f"{host(loc)}/v1/projects/{CFG['project']}/locations/{loc}"
           f"/publishers/anthropic/models/{CFG['model']}:rawPredict")
    body = {"anthropic_version": CFG["anthropic_version"], **body}
    r = _session().post(url, json=body, timeout=600)
    if r.status_code != 200:
        raise RuntimeError(f"{r.status_code}: {r.text[:2000]}")
    return r.json()


def batch_create(name, input_uri, output_prefix, location=None):
    loc = location or CFG["batch_location"]
    url = f"{host(loc)}/v1/projects/{CFG['project']}/locations/{loc}/batchPredictionJobs"
    body = {
        "displayName": name,
        "model": f"publishers/anthropic/models/{CFG['model']}",
        "inputConfig": {"instancesFormat": "jsonl", "gcsSource": {"uris": [input_uri]}},
        "outputConfig": {"predictionsFormat": "jsonl",
                         "gcsDestination": {"outputUriPrefix": output_prefix}},
    }
    r = _session().post(url, json=body, timeout=120)
    if r.status_code != 200:
        raise RuntimeError(f"{r.status_code}: {r.text[:2000]}")
    return r.json()


def batch_get(job_name, location=None):
    loc = location or CFG["batch_location"]
    r = _session().get(f"{host(loc)}/v1/{job_name}", timeout=60)
    r.raise_for_status()
    return r.json()


def batch_wait(job_name, every=60, location=None):
    while True:
        j = batch_get(job_name, location)
        print(time.strftime("%H:%M:%S"), j["state"], flush=True)
        if j["state"] in ("JOB_STATE_SUCCEEDED", "JOB_STATE_FAILED",
                          "JOB_STATE_CANCELLED", "JOB_STATE_PARTIALLY_SUCCEEDED", "JOB_STATE_EXPIRED"):
            return j
        time.sleep(every)
