"""Render carousel slides for every entry in tool_data/queue.json.

Single source of truth: tool_data/queue.json. Each entry renders to
Queue/<Id>_<Slug>/Slide_1..8.jpg. Queue/manifest.json records a hash of the
data each folder was rendered from, so an entry is re-rendered whenever its
data changes (e.g. the weekly review updates a price and its LastChecked date)
and the poster can refuse to publish slides that are out of date.

Slide design is the Fortnight 3 design, plus a "last checked" date on the
cover and the pricing slide.

Usage: python scripts/render_queue.py [--force]
"""
import datetime, json, os, re, sys
from PIL import Image, ImageDraw, ImageFont
from queue_common import QUEUE, OUT_ROOT, MANIFEST, RENDER_FIELDS, folder_for, data_hash, nice_date

W, H = 1080, 1080
BLACK=(0,0,2); WHITE=(255,255,255); GOLD=(242,222,156)
BLUE=(37,84,181); BLUE2=(24,120,243); DIM=(180,180,180)
SAFE=864; LEFT=(W-SAFE)//2+34; TXT=SAFE-140
FONT_DIR = os.environ.get("FONT_DIR", "_fonts")
BOLD = f"{FONT_DIR}/Poppins-Bold.ttf"
MED = f"{FONT_DIR}/Poppins-Medium.ttf"

def F(p,s): return ImageFont.truetype(p,s)

def wrap(d,t,f,mw):
    out=[]
    for para in str(t).split("\n"):
        if not para.strip(): out.append(""); continue
        cur=""
        for w in para.split():
            tr=(cur+" "+w).strip()
            if d.textlength(tr,font=f)<=mw or not cur: cur=tr
            else: out.append(cur); cur=w
        out.append(cur)
    return out

def base():
    img=Image.new("RGB",(W,H),BLACK); d=ImageDraw.Draw(img)
    d.ellipse([W-148,54,W-64,138], outline=WHITE, width=3)
    f=F(BOLD,30)
    d.text((W-106-d.textlength("AI",font=f)/2, 79), "AI", font=f, fill=WHITE)
    for a in (-1,1): d.arc([W-166,44,W-46,148], 20*a, 60*a, fill=WHITE, width=2)
    return img,d

def handle(d):
    f=F(MED,26); t="@aitoolindex"; tw=d.textlength(t,font=f); x=(W-tw)/2
    d.rounded_rectangle([x-26,H-96,x+tw+26,H-46], radius=25, fill=BLUE)
    d.text((x, H-88), t, font=f, fill=WHITE)

# block = list of (text, font, fill, line_gap, space_after)
def measure(d, block):
    h=0
    for t,f,c,lg,sa in block:
        h += len(wrap(d,t,f,TXT))*(f.size+lg) + sa
    return h

def draw_block(d, block, top=None):
    total=measure(d,block)
    y = top if top is not None else max(210,(H-total)//2-40)
    for t,f,c,lg,sa in block:
        for ln in wrap(d,t,f,TXT):
            d.text((LEFT,y),ln,font=f,fill=c); y += f.size+lg
        y += sa
    return y

def save(img,path): img.save(path,"JPEG",quality=92,optimize=True)

def cover(name,path,hook,checked):
    img,d=base()
    nf=F(BOLD,92)
    nlines=wrap(d,name.upper(),nf,TXT)
    if len(nlines)>2:
        nf=F(BOLD,72); nlines=wrap(d,name.upper(),nf,TXT)
    hf=F(MED,40)
    hlines=wrap(d,hook,hf,TXT-20) if hook else []
    asc,desc=nf.getmetrics(); nlh=asc+desc
    hlh=hf.size+16
    total=nlh*len(nlines)+ (34+3+30 if hlines else 0) + hlh*len(hlines)
    y=(H-total)//2-70
    for ln in nlines:
        d.text(((W-d.textlength(ln,font=nf))/2,y),ln,font=nf,fill=GOLD); y+=nlh
    if hlines:
        ry=y+30; d.line([(W/2-90,ry),(W/2+90,ry)],fill=GOLD,width=3); y=ry+34
        for ln in hlines:
            d.text(((W-d.textlength(ln,font=hf))/2,y),ln,font=hf,fill=WHITE); y+=hlh
    tf=F(MED,30)
    d.text(((W-d.textlength("@aitoolindex",font=tf))/2, 852),"@aitoolindex",font=tf,fill=DIM)
    cf=F(MED,26); ct=f"Details checked {checked}"
    d.text(((W-d.textlength(ct,font=cf))/2, 896),ct,font=cf,fill=DIM)
    sf=F(MED,34); lbl="SWIPE"; lw=d.textlength(lbl,font=sf)
    gap,shaft=22,78; x=W/2-(lw+gap+shaft)/2; yy=972
    d.text((x,yy-22),lbl,font=sf,fill=GOLD)
    ax=x+lw+gap; ay=yy-4
    d.line([(ax,ay),(ax+shaft,ay)],fill=GOLD,width=5)
    d.polygon([(ax+shaft+10,ay),(ax+shaft-15,ay-15),(ax+shaft-15,ay+15)],fill=GOLD)
    save(img,path)

def s_title(r,path):
    img,d=base()
    draw_block(d,[(r["ToolName"].upper(),F(BOLD,42),GOLD,12,34),
                  (r["Hook"],F(BOLD,62),WHITE,16,34),
                  (r["Description"],F(MED,32),DIM,18,0)])
    handle(d); save(img,path)

def s_pair(a,av,b,bv,path):
    img,d=base()
    draw_block(d,[(a,F(BOLD,50),WHITE,12,14),(av,F(MED,36),DIM,18,58),
                  (b,F(BOLD,50),WHITE,12,14),(bv,F(MED,36),DIM,18,0)])
    handle(d); save(img,path)

def s_single(lbl,val,path,ls=58,vs=40,note=None):
    img,d=base()
    block=[(lbl,F(BOLD,ls),WHITE,12,26),(val,F(MED,vs),DIM,20,30 if note else 0)]
    if note: block.append((note,F(MED,28),GOLD,12,0))
    draw_block(d,block)
    handle(d); save(img,path)

def s_uses(r,path):
    img,d=base()
    items=[x.strip() for x in re.split(r"\n|(?<=\D)(?=[123]\.)", str(r["Uses"])) if x.strip()][:3]
    block=[("3 Uses",F(BOLD,72),GOLD,14,52)]
    for it in items: block.append((it,F(MED,38),WHITE,18,34))
    draw_block(d,block)
    handle(d); save(img,path)

def s_cta(path):
    img,d=base()
    f=F(BOLD,84); y=(H-3*100)//2-70
    for ln in ["Save for","when you","need it!"]:
        d.text((LEFT,y),ln,font=f,fill=WHITE); y+=100
    d.rounded_rectangle([LEFT,y+46,LEFT+256,y+124], radius=39, fill=BLUE2)
    fb=F(BOLD,32); d.text((LEFT+76,y+68),"SHARE",font=fb,fill=WHITE)
    handle(d); save(img,path)

def build(r,outdir):
    os.makedirs(outdir,exist_ok=True)
    checked=nice_date(r["LastChecked"])
    cover(r["ToolName"], f"{outdir}/Slide_1.jpg", r["Hook"], checked)
    s_title(r, f"{outdir}/Slide_2.jpg")
    s_pair("Tool Category",r["Category"],"Latest Models & Versions",r["Models"], f"{outdir}/Slide_3.jpg")
    s_uses(r, f"{outdir}/Slide_4.jpg")
    s_single("Pricing Plan", str(r["Pricing"]).replace(" | ","\n"), f"{outdir}/Slide_5.jpg",
             note=f"Last checked {checked}. Prices change - confirm on the official site.")
    s_single("API provided?", r["API"], f"{outdir}/Slide_6.jpg", 64, 46)
    s_pair("Company",r["Company"],"Official Website",r["Website"], f"{outdir}/Slide_7.jpg")
    s_cta(f"{outdir}/Slide_8.jpg")

def validate(rows):
    errs=[]; ids=set()
    for r in rows:
        for k in ["Id"]+RENDER_FIELDS:
            if not str(r.get(k,"")).strip(): errs.append(f"{r.get('Id','?')}: missing {k}")
        if r.get("Id") in ids: errs.append(f"duplicate Id {r.get('Id')}")
        ids.add(r.get("Id"))
        try: datetime.date.fromisoformat(r.get("LastChecked",""))
        except ValueError: errs.append(f"{r.get('Id')}: LastChecked must be YYYY-MM-DD")
    return errs

def main():
    force = "--force" in sys.argv
    rows = json.load(open(QUEUE, encoding="utf-8"))
    errs = validate(rows)
    if errs: sys.exit("queue.json invalid:\n  " + "\n  ".join(errs))
    manifest = json.load(open(MANIFEST, encoding="utf-8")) if os.path.exists(MANIFEST) else {}
    built = 0
    for r in rows:
        folder, h = folder_for(r), data_hash(r)
        if not force and manifest.get(folder) == h and all(
                os.path.exists(f"{folder}/Slide_{n}.jpg") for n in range(1, 9)):
            continue
        build(r, folder); manifest[folder] = h; built += 1
        print("rendered", folder, h)
    os.makedirs(OUT_ROOT, exist_ok=True)
    json.dump(manifest, open(MANIFEST, "w", encoding="utf-8"), indent=1, sort_keys=True)
    print(f"{built} rendered, {len(rows)} entries in queue")

if __name__ == "__main__":
    main()
