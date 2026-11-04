"""Render carousel slides for every entry in tool_data/queue.json.

Single source of truth: tool_data/queue.json. Each entry renders to
Queue/<Id>_<Slug>/Slide_N.jpg at 1080x1350 (4:5). Queue/manifest.json records a
hash of the data each folder was rendered from, so an entry is re-rendered
whenever its data changes (e.g. the weekly review updates a price and its
LastChecked date) and the poster can refuse to publish out-of-date slides.

Design lives in templates/base.css + templates/slide.html.j2 (HTML/CSS rendered
with headless Chromium via Playwright). Change the CSS and bump RENDER_VERSION
in queue_common.py to restyle every unposted carousel.

Usage: python scripts/render_queue.py [--force] [--only Q0042,Q0043] [--out DIR]
"""
import argparse, base64, datetime, json, os, sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from playwright.sync_api import sync_playwright

from queue_common import (QUEUE, MANIFEST, REQUIRED, fmt, num_slides, folder_for,
                          data_hash, nice_date)

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
FONTS = [("Archivo Black", "ArchivoBlack-Regular.ttf", "400"),
         ("Inter", "Inter-Variable.ttf", "100 900"),
         ("JetBrains Mono", "JetBrainsMono-Variable.ttf", "100 800")]


def font_faces():
    """Embed the bundled OFL fonts (_fonts/) so rendering never depends on the network."""
    out = []
    for family, file, weight in FONTS:
        b64 = base64.b64encode((ROOT / "_fonts" / file).read_bytes()).decode()
        out.append(f'@font-face {{ font-family: "{family}"; font-weight: {weight}; font-display: block; '
                   f'src: url(data:font/ttf;base64,{b64}) format("truetype"); }}')
    return "\n".join(out)


def lines(text):
    return [x.split(". ", 1)[-1] if x[:2].strip(".").isdigit() else x
            for x in (l.strip() for l in str(text).split("\n")) if x]


def slides_for(r):
    checked = nice_date(r["LastChecked"])
    if fmt(r) == "prompt":
        n = int(r["Number"])
        tag = f"Run this prompt · Day {n:02d}"
        return [
            dict(kind="cover", inverted=True, tag=tag, text=r["Hook"],
                 note=f"Prompt tested {checked} · works in Claude or ChatGPT"),
            dict(kind="statement", label="Doing it by hand", text=r["Cost"]),
            dict(kind="code", label="The prompt · copy it", text=r["Prompt"],
                 note="Replace everything in [BRACKETS] with your own details."),
            dict(kind="output", label="What you get · example, shortened", text=r["Output"]),
            dict(kind="statement", label="The upgrade", text=r["Upgrade"],
                 sub="One extra line that makes the result twice as useful."),
            dict(kind="cta", text=f"Day {n} of daily prompts.", sub="Save this for the next time you need it.",
                 pill="Follow for tomorrow's"),
        ]
    if fmt(r) == "teardown":
        pp = [p.strip() for p in str(r["Pricing"]).split("|") if p.strip()]
        price = r.get("Price") or " · ".join(pp[1:3]) or pp[0]
        return [
            dict(kind="cover", inverted=True, tag="Tool teardown", text=r["Hook"],
                 note=f"Prices and details checked {checked}"),
            dict(kind="statement", label="The job", text=r["Job"]),
            dict(kind="tool", label="The tool", name=r["DisplayName"], line=r["ToolLine"],
                 price=price, site=r["Website"],
                 note=f"Last checked {checked}. Prices change, so confirm on the official site."),
            dict(kind="steps", label="Get it done in 3 steps", steps=lines(r["Steps"])[:3]),
            dict(kind="statement", label="The honest limit", text=r["Limit"]),
            dict(kind="statement", label="Cheaper option · when it's enough", text=r["Alternative"]),
            dict(kind="cta", text="Want the other 249?", sub="The full AI Tool Index is linked in the bio.",
                 pill="Follow @aitoolindex"),
        ]
    raise ValueError(f"{r['Id']}: no renderer for format {fmt(r)!r}")


def validate(rows):
    errs, ids = [], set()
    for r in rows:
        f = fmt(r)
        if f not in REQUIRED:
            errs.append(f"{r.get('Id','?')}: unknown Format {f!r}"); continue
        for k in ["Id"] + REQUIRED[f]:
            if not str(r.get(k, "")).strip():
                errs.append(f"{r.get('Id','?')}: missing {k}")
        if r.get("Id") in ids:
            errs.append(f"duplicate Id {r.get('Id')}")
        ids.add(r.get("Id"))
        if f != "legacy":
            try: datetime.date.fromisoformat(r.get("LastChecked", ""))
            except ValueError: errs.append(f"{r.get('Id')}: LastChecked must be YYYY-MM-DD")
            if len(str(r.get("Hook", "")).split()) > 14:
                errs.append(f"{r.get('Id')}: Hook is over 14 words")
    return errs


def render(rows, out_root, force=False):
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html", "j2"]))
    tpl = env.get_template("slide.html.j2")
    css = (TEMPLATES / "base.css").read_text(encoding="utf-8")
    fonts = font_faces()
    manifest_path = Path(out_root) / MANIFEST
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}
    built, problems = 0, []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1350})
        for r in rows:
            if fmt(r) == "legacy":
                continue
            folder, h = folder_for(r), data_hash(r)
            target = Path(out_root) / folder
            if not force and manifest.get(folder) == h and all(
                    (target / f"Slide_{n}.jpg").exists() for n in range(1, num_slides(r) + 1)):
                continue
            target.mkdir(parents=True, exist_ok=True)
            specs = slides_for(r)
            for n, s in enumerate(specs, 1):
                page.set_content(tpl.render(css=css, fonts=fonts, fmt=fmt(r), s=s, n=n, total=len(specs)),
                                 wait_until="load")
                page.wait_for_function("document.body.dataset.ready === '1'", timeout=20000)
                over = page.evaluate("document.body.dataset.overflow || ''")
                if over:
                    problems.append(f"{r['Id']} slide {n}: text overflows ({over.strip()})")
                page.screenshot(path=str(target / f"Slide_{n}.jpg"), type="jpeg", quality=92)
            manifest[folder] = h; built += 1
            print("rendered", folder, h)
        browser.close()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True), encoding="utf-8")
    return built, problems


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", help="comma-separated Ids")
    ap.add_argument("--out", default=".", help="render somewhere else (previews)")
    ap.add_argument("--queue", default=QUEUE)
    a = ap.parse_args()
    os.chdir(ROOT)
    rows = json.loads(Path(a.queue).read_text(encoding="utf-8"))
    errs = validate(rows)
    if errs:
        sys.exit("queue.json invalid:\n  " + "\n  ".join(errs))
    if a.only:
        keep = set(a.only.split(","))
        rows = [r for r in rows if r["Id"] in keep]
    built, problems = render(rows, a.out, a.force)
    print(f"{built} rendered, {len(rows)} entries")
    if problems:
        sys.exit("Text did not fit:\n  " + "\n  ".join(problems))


if __name__ == "__main__":
    main()
