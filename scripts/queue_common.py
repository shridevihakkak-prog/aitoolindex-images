"""Shared by render_queue.py (this repo) and post_queue.py (aitoolindex-bot).

No third-party imports, so the poster can use it without installing Pillow.
The poster compares data_hash(entry) with Queue/manifest.json to make sure the
slides it is about to publish were rendered from the current data.
"""
import datetime, hashlib, json, re

QUEUE = "tool_data/queue.json"
OUT_ROOT = "Queue"
MANIFEST = f"{OUT_ROOT}/manifest.json"
RENDER_VERSION = "q1"  # bump to force a full re-render after a design change
NUM_SLIDES = 8
RENDER_FIELDS = ["Hook","ToolName","Description","Category","Models","Uses","Pricing",
                 "API","Company","Website","LastChecked"]

def nice_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%b %Y')}"

def folder_for(r):
    return f"{OUT_ROOT}/{r['Id']}_" + re.sub(r"[^A-Za-z0-9]+","_",r["ToolName"].title()).strip("_")

def data_hash(r):
    payload = json.dumps({k: r[k] for k in RENDER_FIELDS} | {"v": RENDER_VERSION}, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]
