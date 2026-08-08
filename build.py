import os
from PIL import Image, ImageDraw, ImageFont
W=H=1080
GOLD=(242,222,156); WHITE=(255,255,255)
B="_fonts/Poppins-Bold.ttf"; M="_fonts/Poppins-Medium.ttf"
TEXT_W=864-130; SIZE=104
P=[('01_Claude', 'Claude'), ('02_Canva_Magic_Design', 'Canva Magic Design'), ('03_Runway', 'Runway'), ('04_Cursor', 'Cursor'), ('05_Udio', 'Udio'), ('06_ChatGPT', 'ChatGPT'), ('07_Notion_AI', 'Notion AI'), ('08_Stable_Diffusion', 'Stable Diffusion'), ('09_Suno', 'Suno'), ('10_NotebookLM', 'NotebookLM'), ('11_Midjourney', 'Midjourney'), ('12_Bolt.new', 'Bolt.new'), ('13_Otter.ai', 'Otter.ai'), ('14_Figma_AI', 'Figma AI'), ('15_Devin', 'Devin'), ('16_Sora', 'Sora'), ('17_Gemini', 'Gemini'), ('18_Perplexity', 'Perplexity'), ('19_Ideogram', 'Ideogram'), ('20_ElevenLabs', 'ElevenLabs'), ('21_Synthesia', 'Synthesia'), ('22_GitHub_Copilot', 'GitHub Copilot'), ('23_Zapier_AI', 'Zapier AI'), ('24_Kling_AI', 'Kling AI'), ('25_Adobe_Firefly', 'Adobe Firefly'), ('26_Lovable', 'Lovable'), ('27_HeyGen', 'HeyGen'), ('28_DALL-E_3', 'DALL-E 3')]
def wrap(d,t,f,mw):
    if d.textlength(t,font=f)<=mw: return [t]
    ls=[];c=""
    for w in t.split():
        tr=(c+" "+w).strip()
        if d.textlength(tr,font=f)<=mw or not c: c=tr
        else: ls.append(c); c=w
    if c: ls.append(c)
    return ls
def cover(name,path):
    im=Image.new("RGB",(W,H),(0,0,0)); d=ImageDraw.Draw(im)
    f=ImageFont.truetype(B,SIZE); lines=wrap(d,name.upper(),f,TEXT_W)
    a,de=f.getmetrics(); lh=a+de; y=(H-lh*len(lines))//2-60
    for ln in lines:
        d.text(((W-d.textlength(ln,font=f))/2,y),ln,font=f,fill=GOLD); y+=lh
    ry=y+44; d.line([(W/2-90,ry),(W/2+90,ry)],fill=GOLD,width=3)
    hf=ImageFont.truetype(M,40)
    d.text(((W-d.textlength("@aitoolindex",font=hf))/2,ry+32),"@aitoolindex",font=hf,fill=WHITE)
    sf=ImageFont.truetype(M,34); lab="SWIPE"; lw=d.textlength(lab,font=sf)
    gap=22; sh=78; tot=lw+gap+sh; x=W/2-tot/2; yy=940
    d.text((x,yy-22),lab,font=sf,fill=GOLD)
    ax=x+lw+gap; ay=yy-4
    d.line([(ax,ay),(ax+sh,ay)],fill=GOLD,width=5)
    hd=15; d.polygon([(ax+sh+10,ay),(ax+sh-hd,ay-hd),(ax+sh-hd,ay+hd)],fill=GOLD)
    im.save(path,"JPEG",quality=92,optimize=True)
done=0
for folder,name in P:
    base="Fortnight_01/Carousels/"+folder
    if not os.path.isdir(base): print("MISSING",base); continue
    if os.path.exists(base+"/Slide_9.jpg"): print("skip (already 9)",folder); continue
    for i in range(8,0,-1):
        os.rename(base+"/Slide_%d.jpg"%i, base+"/Slide_%d.jpg"%(i+1))
    cover(name, base+"/Slide_1.jpg")
    done+=1
    print("built",folder,name)
print("TOTAL",done)
