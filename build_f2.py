import json
DATA = '[{"Day": "1", "Slot": "1", "Hook": "Google\'s first AI art tool. It only made nightmares.", "ToolName": "DEEPDREAM", "Description": "Google\'s original neural-network tool that enhances patterns into surreal, hallucinatory art.", "Category": "Graphic Design", "Models": "DeepDream convolutional neural network, 2026", "Uses": "1. Ordinary photos into surreal art\\n2. Exaggerates patterns the network sees\\n3. Shows how neural nets \'see\' images", "Pricing": "Free, open source | Free: fully free | Tier: none", "API": "No", "Company": "Google LLC (USA)", "Website": "research.google"}, {"Day": "1", "Slot": "2", "Hook": "Tableau\'s AI isn\'t included in the price you already pay", "ToolName": "TABLEAU AI", "Description": "Salesforce\'s Tableau adds AI features like Tableau Agent and Pulse for smarter analytics.", "Category": "Data Analysis", "Models": "Tableau Agent + Tableau Pulse, 2026", "Uses": "1. Pulse monitors key metrics for you\\n2. AI summaries of dashboard changes\\n3. Ask questions about your metrics", "Pricing": "Custom | Free: none | Tier: Standard Tableau $12-70/user/mo; Tableau+ AI bundle by quote only", "API": "Yes", "Company": "Salesforce, Inc. (USA)", "Website": "www.tableau.com"}, {"Day": "2", "Slot": "1", "Hook": "The advertised price is $49. Almost nobody pays $49.", "ToolName": "APOLLO AI", "Description": "A sales intelligence platform combining a B2B contact database with AI-assisted prospecting.", "Category": "Marketing & Sales", "Models": "Apollo AI Research, Writing, and Lead Scoring, 2026", "Uses": "1. Verified contacts from 200M+ people\\n2. AI-written emails and subject lines\\n3. Leads scored by likelihood to convert", "Pricing": "Freemium | Free: 10,000 email credits/mo", "API": "Yes", "Company": "Apollo.io, Inc. (USA)", "Website": "www.apollo.io"}, {"Day": "2", "Slot": "2", "Hook": "4,000 words a day, free, and it reads your documents", "ToolName": "BEARLY", "Description": "An AI writing and research assistant that chats with documents, transcribes audio", "Category": "Research & Data", "Models": "Bearly HyperChat with Google-powered web search, 2026", "Uses": "1. Chat with several documents at once\\n2. Turn audio into interactive transcripts\\n3. Search the live web", "Pricing": "Freemium | Free: 4,000 words/day | Tier: Pro $20/mo ($200/yr), Analyst plan for heavy use", "API": "No", "Company": "Bearly AI, Inc. (USA)", "Website": "bearly.ai"}, {"Day": "3", "Slot": "1", "Hook": "Your podcast sounds amateur. This fixes it in one pass.", "ToolName": "AUPHONIC", "Description": "Automated audio post-production for podcasts and broadcasts", "Category": "Audio / Podcast", "Models": "Adaptive leveler, intelligent noise/reverb reduction", "Uses": "1. Evening out volume between speakers automatically\\n2. Reducing noise and reverb\\n3. Meeting streaming/broadcast loudness targets", "Pricing": "Freemium | Free: 2 hrs/mo | S: $11-13/mo (9 hrs) | M: $23-27/mo (21 hrs) | L: $45-53/mo (45 hrs)", "API": "Yes", "Company": "Auphonic (Austria)", "Website": "auphonic.com"}, {"Day": "3", "Slot": "2", "Hook": "They hid the pricing page after the acquisition", "ToolName": "MARKETMUSE", "Description": "An AI content planning platform that identifies content gaps and predicts how new content will", "Category": "Marketing & SEO", "Models": "MarketMuse AI content strategy engine (part of Siteimprove), 2026", "Uses": "1. Crawls your site: update or rewrite?\\n2. Finds content gaps vs competitors\\n3. Predicts performance pre-publish", "Pricing": "Freemium | Free: 10 queries/mo", "API": "No", "Company": "MarketMuse, Inc.", "Website": "www.marketmuse.com"}, {"Day": "4", "Slot": "1", "Hook": "Free plan gives you 60 shapes. Diagrams get big fast.", "ToolName": "LUCIDCHART AI", "Description": "An AI-assisted diagramming tool for flowcharts, org charts, wireframes, and system diagrams.", "Category": "Productivity", "Models": "Lucidchart AI diagram generation, 2026", "Uses": "1. Diagrams generated from text\\n2. Flowcharts, ERDs and UML\\n3. Org charts and network maps", "Pricing": "Freemium | Free: 3 documents, 60 shapes | Tier: Individual $9/mo, Team $10/user/mo", "API": "No", "Company": "Lucid Software Inc. (USA)", "Website": "www.lucidchart.com"}, {"Day": "4", "Slot": "2", "Hook": "100+ AI models. One page. No subscription.", "ToolName": "HUGGINGCHAT", "Description": "A free, open-source chat interface for trying dozens of AI models", "Category": "LLM / Chatbot", "Models": "Access to 100+ open-source models including Llama 3.1, Mistral Large 2", "Uses": "1. Comparing different open-source AI models\\n2. Free AI chat without a paywall\\n3. Building custom Assistants with your own prompts", "Pricing": "Freemium | Free: full chat access (account required) | Hugging Face Pro: adds extra compute perks", "API": "Yes", "Company": "Hugging Face (USA)", "Website": "huggingface.co/chat"}, {"Day": "5", "Slot": "1", "Hook": "A free image upscaler that runs on your own laptop", "ToolName": "UPSCAYL", "Description": "A free, open-source AI image upscaler you run on your own computer", "Category": "Image Generation", "Models": "Desktop app free and open source", "Uses": "1. Upscaling images 2x-16x on your own device\\n2. No watermarks or usage limits (desktop)\\n3. Batch processing multiple images at once", "Pricing": "Open Source | Free: unlimited, self-hosted | Cloud plans: ~$12-96/mo for 100-1,000 credits", "API": "No", "Company": "Upscayl (Open Source)", "Website": "upscayl.org"}, {"Day": "5", "Slot": "2", "Hook": "HubSpot\'s AI has no flat price - it bills by credit", "ToolName": "HUBSPOT AI", "Description": "HubSpot\'s Breeze AI suite adds an assistant, autonomous agents, and data enrichment across the CRM.", "Category": "Marketing & Sales", "Models": "HubSpot Breeze Assistant, Agents, and Intelligence, 2026", "Uses": "1. Summarises CRM records, drafts emails\\n2. Agents run multi-step campaigns\\n3. Enriches contacts with intent data", "Pricing": "Freemium (Hub required) | Free: basic AI included", "API": "Yes", "Company": "HubSpot, Inc. (USA)", "Website": "www.hubspot.com/artificial-intelligence"}, {"Day": "6", "Slot": "1", "Hook": "Unlimited free meeting recordings. Yes, really.", "ToolName": "TLDV", "Description": "A free-forever AI meeting recorder for Zoom, Meet, and Teams with multilingual transcripts.", "Category": "Productivity", "Models": "tl;dv AI summarization engine, 30+ language transcription, 2026", "Uses": "1. Unlimited free recording and transcripts\\n2. Real-time transcripts in 30+ languages\\n3. Custom AI summary prompts (Pro)", "Pricing": "Freemium | Free: unlimited recordings, 10 AI summaries/mo", "API": "Yes", "Company": "tldv, Inc. (Germany)", "Website": "tldv.io"}, {"Day": "6", "Slot": "2", "Hook": "2,000 free AI words a month, and it never expires", "ToolName": "INK", "Description": "An all-in-one AI writing and SEO platform combining content generation with real-time optimization", "Category": "Marketing & SEO", "Models": "INK AI Writer with semantic SEO scoring, 2026", "Uses": "1. Unlimited AI-written SEO articles\\n2. Live semantic SEO scoring\\n3. AI images alongside the copy", "Pricing": "Freemium | Free: 2,000 AI words/mo, ongoing (not just a trial)", "API": "No", "Company": "Ink (Ink4All, Inc.) (USA)", "Website": "ink.co"}, {"Day": "7", "Slot": "1", "Hook": "The AI editor Jasper bought and most people forgot", "ToolName": "CLIPDROP", "Description": "A toolkit of quick AI image editing tools: background removal, relighting, and more", "Category": "Image Generation", "Models": "Now owned and operated by Jasper", "Uses": "1. Removing backgrounds instantly\\n2. Relighting photos after the fact\\n3. Generating images with Stable Diffusion XL", "Pricing": "Freemium | Free: 15 images/mo with watermark | Pro: $9/mo (HD, unlimited)", "API": "Yes", "Company": "Jasper (USA)", "Website": "clipdrop.co"}, {"Day": "7", "Slot": "2", "Hook": "It reviews your pull request before your teammate does", "ToolName": "QODO", "Description": "AI code review and test generation, rebranded from CodiumAI", "Category": "Code Generation", "Models": "Qodo Merge for context-aware PR reviews and Qodo Gen for IDE-based", "Uses": "1. Generating meaningful test suites automatically\\n2. AI-powered pull request reviews\\n3. Catching bugs and edge cases before merge", "Pricing": "Freemium | Developer: free (30 PR reviews/mo pooled, 250 IDE/CLI credits)", "API": "Yes", "Company": "Qodo, formerly CodiumAI (Israel)", "Website": "qodo.ai"}, {"Day": "8", "Slot": "1", "Hook": "Millions of AI characters. Free, if you accept ads.", "ToolName": "CHARACTER.AI", "Description": "Chat with millions of AI characters, from originals to fandom favorites", "Category": "LLM / Chatbot", "Models": "Same underlying model on Free and Plus", "Uses": "1. Roleplay with custom characters\\n2. Build and share your own\\n3. Multi-Character Rooms with several AIs", "Pricing": "Freemium | Free: unlimited messages, with ads", "API": "No", "Company": "Character Technologies (USA)", "Website": "character.ai"}, {"Day": "8", "Slot": "2", "Hook": "It builds the sitemap and wireframes. You build the site.", "ToolName": "RELUME", "Description": "An AI sitemap and wireframe generator that turns text prompts into ready-to-build website", "Category": "Web Builder", "Models": "Relume AI sitemap + wireframe generator, 2026", "Uses": "1. Full sitemap from a description\\n2. Sitemaps become real wireframes\\n3. 1,000+ human-designed components", "Pricing": "Freemium | Free: basic sites for individuals | Tier: Starter $20/mo ($16 annual) | Pro: $200-250+/mo", "API": "No", "Company": "Relume (USA/Australia)", "Website": "www.relume.io"}, {"Day": "9", "Slot": "1", "Hook": "This coding assistant dropped solo devs entirely", "ToolName": "CODY", "Description": "An enterprise AI coding assistant built on deep code search", "Category": "Code Generation", "Models": "Now enterprise-only since June 2025", "Uses": "1. Coding help grounded in whole-codebase search\\n2. Enterprise security and admin controls\\n3. Batch changes across repos", "Pricing": "Enterprise only | $59/user/mo (annual contract); broader platform often starts near $16,000/year", "API": "Limited", "Company": "Sourcegraph (USA)", "Website": "sourcegraph.com/cody"}, {"Day": "9", "Slot": "2", "Hook": "FinChat is gone. The terminal behind it is not.", "ToolName": "FINCHAT", "Description": "An AI investment research terminal offering financial data, models", "Category": "Research & Data", "Models": "Fiscal.ai (formerly FinChat) AI Copilot, 2026", "Uses": "1. Data on 100,000+ public companies\\n2. DCF models and visualisations\\n3. Stock screening with custom filters", "Pricing": "Freemium | Free: core data + AI Copilot | Tier: paid tiers for higher limits (contact for pricing)", "API": "Yes", "Company": "Fiscal.ai, Inc. (USA)", "Website": "fiscal.ai"}, {"Day": "10", "Slot": "1", "Hook": "There\'s no free plan - just 14 days to decide", "ToolName": "BEAUTIFUL.AI", "Description": "A presentation tool that uses Smart Slide templates to automatically design professional-looking", "Category": "Productivity", "Models": "Beautiful.ai Smart Slides + AI content generation, 2026", "Uses": "1. Slides auto-format via Smart Slides\\n2. AI content, images and translation\\n3. Consistent brand styling", "Pricing": "Freemium (trial) | Free: 14-day trial | Tier: Pro $12/mo (annual), Team $40/seat/mo (annual)", "API": "No", "Company": "Beautiful.ai, Inc. (USA)", "Website": "www.beautiful.ai"}, {"Day": "10", "Slot": "2", "Hook": "Background music you can legally put in a client video", "ToolName": "MUBERT", "Description": "Real-time generative background music licensed for commercial use", "Category": "Music Generation", "Models": "Real-time generative engine that creates adaptive instrumental tracks", "Uses": "1. Royalty-free background music instantly\\n2. Adjust tempo, key and chords\\n3. Licensing for ads and games", "Pricing": "Freemium | Free: 25 tracks/mo, personal use | Creator: $14/mo | Pro: $39/mo | Business: $199/mo", "API": "Yes", "Company": "Mubert (USA)", "Website": "mubert.com"}, {"Day": "11", "Slot": "1", "Hook": "Product photos that look studio-shot, from your phone", "ToolName": "PHOTOROOM", "Description": "An all-in-one AI photo editor built for product and e-commerce images", "Category": "Image Generation", "Models": "AI background removal, retouching", "Uses": "1. Remove and generate backgrounds\\n2. Product shots, models and flat lays\\n3. Batch-edit thousands of images", "Pricing": "Freemium | Free: 250 exports/mo | Pro: $7.50-7.99/mo | Max: $20.99-26.99/mo | Ultra: from $82.50-99/mo", "API": "Yes", "Company": "Photoroom (France)", "Website": "photoroom.com"}, {"Day": "11", "Slot": "2", "Hook": "A coding agent that lives entirely in your terminal", "ToolName": "MENTAT", "Description": "An open-source, terminal-based AI coding assistant that edits multiple files in a codebase.", "Category": "Code Generation", "Models": "Mentat by AbanteAI, GPT-4-class models, 2026", "Uses": "1. Edits across many files at once\\n2. Learn a codebase without copy-paste\\n3. Refactor from the command line", "Pricing": "Free, open source | Free: fully free | Tier: none (bring your own API key)", "API": "Yes", "Company": "AbanteAI (USA)", "Website": "github.com/AbanteAI/mentat"}, {"Day": "12", "Slot": "1", "Hook": "It tells you whether scientists actually agree", "ToolName": "CONSENSUS", "Description": "An AI-powered academic search engine that summarizes papers and shows research agreement levels.", "Category": "Research & Data", "Models": "Consensus AI with Scholar Agent and Deep Search, 2026", "Uses": "1. Search 200M+ research papers in plain English\\n2. See how much scientists actually agree\\n3. AI summaries of findings", "Pricing": "Freemium | Free: 20 searches/mo | Tier: Premium $10/mo, Deep $15/mo, Team $9.99/seat/mo (annual)", "API": "Limited", "Company": "Consensus NLP, Inc. (USA)", "Website": "consensus.app"}, {"Day": "12", "Slot": "2", "Hook": "The voice tool built for compliance teams, not creators", "ToolName": "WELLSAID LABS", "Description": "Enterprise-grade AI voice studio built for corporate training and content", "Category": "Audio / Podcast", "Models": "Professional voice cloning with governance features like usage", "Uses": "1. Brand-safe, professional-quality voiceovers\\n2. Voice cloning for corporate use\\n3. Multilingual support (15 languages)", "Pricing": "Freemium | Trial: free, 0 downloads | Creative/Maker: $49-50/mo | Business: $160/mo | Teams: $249/seat/mo", "API": "Yes", "Company": "WellSaid Labs (USA)", "Website": "wellsaidlabs.com"}, {"Day": "13", "Slot": "1", "Hook": "Unlimited free AI art, no daily cap", "ToolName": "MAGE.SPACE", "Description": "A free-first AI art generator with access to many open models", "Category": "Image Generation", "Models": "Supports Stable Diffusion, SDXL, Flux, Z-Image, Qwen, Wan", "Uses": "1. Free unlimited image and video\\n2. Many open-source models in one place\\n3. LoRA, ControlNet and upscaling", "Pricing": "Freemium | Free: unlimited creations | Basic: ~$4-8/mo | Pro: ~$15/mo (adds video generation, all models)", "API": "Limited", "Company": "Mage Space (USA)", "Website": "mage.space"}, {"Day": "13", "Slot": "2", "Hook": "Meta\'s free music AI. Nobody has updated it since 2024.", "ToolName": "MUSICGEN", "Description": "Meta\'s free, open-source AI model for generating instrumental music", "Category": "Music Generation", "Models": "300M/1.5B/3.3B parameter variants", "Uses": "1. Instrumental music from a text prompt\\n2. Extend or reharmonise a melody\\n3. Free commercial use (Meta licence)", "Pricing": "Open Source | Free: self-hosted | Cloud hosting (Replicate, Hugging Face): a few cents per generation", "API": "Yes", "Company": "Meta (USA)", "Website": "github.com/facebookresearch/audiocraft"}, {"Day": "14", "Slot": "1", "Hook": "No free plan. It\'s betting you\'ll pay to save 2 hours.", "ToolName": "AKIFLOW", "Description": "A time-blocking productivity app that pulls tasks from email, Slack", "Category": "Productivity", "Models": "Aki AI Executive Assistant (proprietary), 2026", "Uses": "1. Pulls tasks from email, Slack, Asana\\n2. Time-block your day by keyboard\\n3. Aki as an AI executive assistant", "Pricing": "Paid only, 7-day free trial | Tier: $34/mo (billed monthly) or $19/mo (billed yearly, save 44%)", "API": "Limited", "Company": "Akiflow, Inc. (Italy)", "Website": "akiflow.com"}, {"Day": "14", "Slot": "2", "Hook": "The interview no human watches until you pass", "ToolName": "HIREVUE AI", "Description": "An AI-powered video interviewing and assessment platform that helps recruiters screen candidates.", "Category": "HR & Recruiting", "Models": "HireVue AI-assisted screening and game-based assessments, 2026", "Uses": "1. Structured video interviews at scale\\n2. Game-based cognitive assessments\\n3. Conversational AI screening", "Pricing": "Enterprise custom | Free: none", "API": "Yes", "Company": "HireVue, Inc. (USA)", "Website": "www.hirevue.com"}]'
import csv, io, os, re
from PIL import Image, ImageDraw, ImageFont

W = H = 1080
BLACK=(0,0,2); WHITE=(255,255,255); GOLD=(242,222,156)
BLUE=(37,84,181); BLUE2=(24,120,243); DIM=(180,180,180)
SAFE=864; LEFT=(W-SAFE)//2+34; TXT=SAFE-140
BOLD="/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
MED ="/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
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

def cover(name,path,hook=""):
    img,d=base()
    nf=F(BOLD,92)
    nlines=wrap(d,name.upper(),nf,TXT)
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
    sf=F(MED,34); lbl="SWIPE"; lw=d.textlength(lbl,font=sf)
    gap,shaft=22,78; x=W/2-(lw+gap+shaft)/2; yy=952
    d.text((x,yy-22),lbl,font=sf,fill=GOLD)
    ax=x+lw+gap; ay=yy-4
    d.line([(ax,ay),(ax+shaft,ay)],fill=GOLD,width=5)
    d.polygon([(ax+shaft+10,ay),(ax+shaft-15,ay-15),(ax+shaft-15,ay+15)],fill=GOLD)
    img.save(path,"JPEG",quality=92,optimize=True)

def s_title(r,path):
    img,d=base()
    draw_block(d,[(r["ToolName"].upper(),F(BOLD,42),GOLD,12,34),
                  (r["Hook"],F(BOLD,62),WHITE,16,34),
                  (r["Description"],F(MED,32),DIM,18,0)])
    handle(d); img.save(path,"JPEG",quality=92,optimize=True)

def s_pair(a,av,b,bv,path):
    img,d=base()
    draw_block(d,[(a,F(BOLD,50),WHITE,12,14),(av,F(MED,36),DIM,18,58),
                  (b,F(BOLD,50),WHITE,12,14),(bv,F(MED,36),DIM,18,0)])
    handle(d); img.save(path,"JPEG",quality=92,optimize=True)

def s_single(lbl,val,path,ls=58,vs=40):
    img,d=base()
    draw_block(d,[(lbl,F(BOLD,ls),WHITE,12,26),(val,F(MED,vs),DIM,20,0)])
    handle(d); img.save(path,"JPEG",quality=92,optimize=True)

def s_uses(r,path):
    img,d=base()
    items=[x.strip() for x in re.split(r"\n|(?<=\D)(?=[123]\.)", str(r["Uses"])) if x.strip()][:3]
    block=[("3 Uses",F(BOLD,72),GOLD,14,52)]
    for it in items: block.append((it,F(MED,38),WHITE,18,34))
    draw_block(d,block)
    handle(d); img.save(path,"JPEG",quality=92,optimize=True)

def s_cta(path):
    img,d=base()
    f=F(BOLD,84); y=(H-3*100)//2-70
    for ln in ["Save for","when you","need it!"]:
        d.text((LEFT,y),ln,font=f,fill=WHITE); y+=100
    d.rounded_rectangle([LEFT,y+46,LEFT+256,y+124], radius=39, fill=BLUE2)
    fb=F(BOLD,32); d.text((LEFT+76,y+68),"SHARE",font=fb,fill=WHITE)
    handle(d); img.save(path,"JPEG",quality=92,optimize=True)

def build(r,outdir):
    os.makedirs(outdir,exist_ok=True)
    cover(r["ToolName"], f"{outdir}/Slide_1.jpg", r["Hook"])
    s_title(r, f"{outdir}/Slide_2.jpg")
    s_pair("Tool Category",r["Category"],"Latest Models & Versions",r["Models"], f"{outdir}/Slide_3.jpg")
    s_uses(r, f"{outdir}/Slide_4.jpg")
    s_single("Pricing Plan", str(r["Pricing"]).replace(" | ","\n"), f"{outdir}/Slide_5.jpg")
    s_single("API provided?", r["API"], f"{outdir}/Slide_6.jpg", 64, 46)
    s_pair("Company",r["Company"],"Official Website",r["Website"], f"{outdir}/Slide_7.jpg")
    s_cta(f"{outdir}/Slide_8.jpg")


ROWS = json.loads(DATA)
def slug(n,t):
    return f"{n:02d}_" + re.sub(r"[^A-Za-z0-9]+","_",t.title()).strip("_")
n=0
for i,r in enumerate(ROWS,1):
    out=f"Fortnight_02/Carousels/{slug(i,r['ToolName'])}"
    if os.path.isdir(out) and len([x for x in os.listdir(out) if x.endswith('.jpg')])==8:
        print("skip", out); continue
    build(r,out); n+=1
    print("built", out)
print("TOTAL", n)
