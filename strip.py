import os
P=['01_Claude','02_Canva_Magic_Design','03_Runway','04_Cursor','05_Udio','06_ChatGPT','07_Notion_AI','08_Stable_Diffusion','09_Suno','10_NotebookLM','11_Midjourney','12_Bolt.new','13_Otter.ai','14_Figma_AI','15_Devin','16_Sora','17_Gemini','18_Perplexity','19_Ideogram','20_ElevenLabs','21_Synthesia','22_GitHub_Copilot','23_Zapier_AI','24_Kling_AI','25_Adobe_Firefly','26_Lovable','27_HeyGen','28_DALL-E_3']
n=0
for f in P:
    d=f"Fortnight_01/Carousels/{f}"
    if not os.path.isdir(d):
        print("MISSING",f); continue
    have=[x for x in os.listdir(d) if x.startswith("Slide_") and x.endswith(".jpg")]
    if len(have)!=9:
        print(f"skip {f} (has {len(have)})"); continue
    os.remove(f"{d}/Slide_8.jpg")          # the "Use this instead" page
    os.rename(f"{d}/Slide_9.jpg", f"{d}/Slide_8.jpg")   # CTA moves up
    n+=1
    print("stripped",f)
print("TOTAL",n)
