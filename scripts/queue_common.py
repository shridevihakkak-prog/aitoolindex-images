"""Shared by render_queue.py (this repo) and post_queue.py (aitoolindex-bot).

No third-party imports, so the poster can use it without installing a renderer.
The poster compares data_hash(entry) with Queue/manifest.json to make sure the
slides it is about to publish were rendered from the current data.

Formats (aitoolindex_post_strategy.md, 12 Sep 2026):
  prompt   - "Run This Prompt", 6 slides, 09:00 IST daily
  teardown - "Tool Teardown", 7 slides, 21:00 IST Mon/Wed/Fri/Sun
  legacy   - the old square tool carousel (8 slides); kept only for posted history
"""
import datetime, hashlib, json, re

QUEUE = "tool_data/queue.json"
OUT_ROOT = "Queue"
MANIFEST = f"{OUT_ROOT}/manifest.json"
RENDER_VERSION = "v2"  # bump to force a full re-render after a design change

NUM_SLIDES = {"prompt": 6, "teardown": 7, "legacy": 8}
REQUIRED = {
    "prompt": ["Number", "Hook", "Cost", "Prompt", "Output", "Upgrade", "Question", "LastChecked"],
    "teardown": ["ToolName", "DisplayName", "Hook", "Job", "ToolLine", "Price", "Steps", "Limit", "Alternative",
                 "Pricing", "Category", "Company", "Website", "LastChecked"],
    "legacy": [],
}
# Fields that only feed the caption; changing them must not force a re-render.
CAPTION_ONLY = {"Id", "Source", "NewsNote", "Question", "Description", "Models", "Uses", "API"}

def fmt(r):
    return r.get("Format", "legacy")

def num_slides(r):
    return NUM_SLIDES[fmt(r)]

def nice_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%b %Y')}"

def slug_name(r):
    if fmt(r) == "prompt":
        return f"Prompt_{int(r['Number']):03d}"
    return re.sub(r"[^A-Za-z0-9]+", "_", r["ToolName"].title()).strip("_")

def folder_for(r):
    return f"{OUT_ROOT}/{r['Id']}_{slug_name(r)}"

def data_hash(r):
    if fmt(r) == "legacy":   # rendered by the retired v1 renderer; hash kept as it was
        keys = ["Hook","ToolName","Description","Category","Models","Uses","Pricing",
                "API","Company","Website","LastChecked"]
        payload = json.dumps({k: r[k] for k in keys} | {"v": "q1"}, sort_keys=True, ensure_ascii=False)
    else:
        data = {k: v for k, v in r.items() if k not in CAPTION_ONLY}
        payload = json.dumps(data | {"v": RENDER_VERSION}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
