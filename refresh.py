import os
from PIL import Image, ImageDraw, ImageFont
W=H=1080
GOLD=(242,222,156); WHITE=(255,255,255)
B="_fonts/Poppins-Bold.ttf"; M="_fonts/Poppins-Medium.ttf"
TEXT_W=864-130; SIZE=104
P=[('01_Claude','Claude'),('02_Canva_Magic_Design','Canva Magic Design'),('03_Runway','Runway'),('04_Cursor','Cursor'),('05_Udio','Udio'),('06_ChatGPT','ChatGPT'),('07_Notion_AI','Notion AI'),('08_Stable_Diffusion','Stable Diffusion'),('09_Suno','Suno'),('10_NotebookLM','NotebookLM'),('11_Midjourney','Midjourney'),('12_Bolt.new','Bolt.new'),('13_Otter.ai','Otter.ai'),('14_Figma_AI','Figma AI'),('15_Devin','Devin'),('16_Sora','Sora'),('17_Gemini','Gemini'),('18_Perplexity','Perplexity'),('19_Ideogram','Ideogram'),('20_ElevenLabs','ElevenLabs'),('21_Synthesia','Synthesia'),('22_GitHub_Copilot','GitHub Copilot'),('23_Zapier_AI','Zapier AI'),('24_Kling_AI','Kling AI'),('25_Adobe_Firefly','Adobe Firefly'),('26_Lovable','Lovable'),('27_HeyGen','HeyGen'),('28_DALL-E_3','DALL-E 3')]

def wrap(d,t,f,mw):
    if d.textlength(t,font=f)<=mw: return [t]
    lines=[];cur=""
    for w in t.split():
        tr=(cur+" "+w).strip()
        if d.textlength(tr,font=f)<=mw or not cur: cur=tr
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def cover(name,path):
    img=Image.new("RGB",(W,H),(0,0,0)); d=ImageDraw.Draw(img)
    f=ImageFont.truetype(B,SIZE); lines=wrap(d,name.upper(),f,TEXT_W)
    asc,desc=f.getmetrics(); lh=asc+desc
    y=(H-lh*len(lines))//2-60
    for ln in lines:
        d.text(((W-d.textlength(ln,font=f))/2,y),ln,font=f,fill=GOLD); y+=lh
    ry=y+44
    d.line([(W/2-90,ry),(W/2+90,ry)],fill=GOLD,width=3)
    hf=ImageFont.truetype(M,40)
    d.text(((W-d.textlength("@aitoolindex",font=hf))/2,ry+32),"@aitoolindex",font=hf,fill=WHITE)
    sf=ImageFont.truetype(M,34); lbl="SWIPE"; lw=d.textlength(lbl,font=sf)
    gap,shaft=22,78; total=lw+gap+shaft; x=W/2-total/2; yy=940
    d.text((x,yy-22),lbl,font=sf,fill=GOLD)
    ax=x+lw+gap; ay=yy-4
    d.line([(ax,ay),(ax+shaft,ay)],fill=GOLD,width=5)
    hd=15
    d.polygon([(ax+shaft+10,ay),(ax+shaft-hd,ay-hd),(ax+shaft-hd,ay+hd)],fill=GOLD)
    img.save(path,"JPEG",quality=92,optimize=True)

n=0
for folder,name in P:
    dd=f"Fortnight_01/Carousels/{folder}"
    if not os.path.isdir(dd): print("MISSING",folder); continue
    cover(name,f"{dd}/Slide_1.jpg"); n+=1
    print("cover",folder)
print("TOTAL",n)
