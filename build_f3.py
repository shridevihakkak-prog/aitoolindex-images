import json
DATA = '[{"Day": "1", "Slot": "1", "Hook": "AI that scores film music, not pop songs", "ToolName": "AIVA", "Description": "An AI composer specializing in cinematic and classical instrumental music", "Category": "Music Generation", "Models": "250+ musical styles, MIDI export for Logic Pro, Ableton, and Cubase", "Uses": "1. Cinematic, emotional soundtracks\\n2. Editable MIDI export\\n3. Monetise on YouTube and Twitch (paid)", "Pricing": "Freemium | Free: watermarked | Standard: ~€15/mo (~$11/mo) | Pro: ~€49/mo", "API": "Limited", "Company": "AIVA Technologies (Luxembourg)", "Website": "aiva.ai"}, {"Day": "1", "Slot": "2", "Hook": "Describe the app. The agent builds and runs it.", "ToolName": "REPLIT AGENT", "Description": "An autonomous AI agent integrated into the Replit IDE that plans, writes", "Category": "Code Generation", "Models": "Replit AI Agent (2025/2026)", "Uses": "1. App scaffolding from one prompt\\n2. Installs deps, configures the env\\n3. Debugs runtime errors on its own", "Pricing": "Freemium | Free: Starter $0/mo | Core: $20/mo | Pro: $100/mo", "API": "No", "Company": "Replit (USA)", "Website": "replit.com"}, {"Day": "2", "Slot": "1", "Hook": "It clones your voice from 5 seconds of audio", "ToolName": "ALTERED", "Description": "Real-time AI voice changer and cloning studio for streamers and creators", "Category": "Audio / Podcast", "Models": "Rapid voice cloning from 5 seconds of audio", "Uses": "1. Clone a voice from 5 seconds\\n2. Real-time voice changing on calls\\n3. Works as a mic in Discord and Zoom", "Pricing": "Freemium | Free: basic features | Creator: $30/mo | Professional: $90/mo | Agency: $90-120/mo", "API": "Limited", "Company": "Altered Studio (France)", "Website": "altered.ai"}, {"Day": "2", "Slot": "2", "Hook": "It time-blocks your day so you stop deciding", "ToolName": "TREVOR AI", "Description": "A daily planner that uses AI to time-block your tasks and calendar events automatically.", "Category": "Productivity", "Models": "Trevor AI planning engine (proprietary), 2026", "Uses": "1. Drag-and-drop time blocking of to-dos\\n2. Syncing Google Calendar and Microsoft 365\\n3. Suggesting optimal time slots for tasks", "Pricing": "Freemium | Free: free plan for personal use | Tier: Pro $3.99/mo or $29.99/yr", "API": "No", "Company": "Trevor Labs (Bulgaria)", "Website": "www.trevorai.com"}, {"Day": "3", "Slot": "1", "Hook": "700,000 community models. $5.99 a month.", "ToolName": "SEAART", "Description": "A budget-friendly AI art and video generator with a huge model library", "Category": "Image Generation", "Models": "700,000+ community model library", "Uses": "1. Text-to-image with 700,000+ models\\n2. Easy Mode or full workflow control\\n3. AI video via SeaArt Flow 2.0", "Pricing": "Freemium | Free: daily Stamina allowance | Beginner: $5.99/mo | Standard: $29.99/mo", "API": "Limited", "Company": "SeaArt AI (Singapore)", "Website": "seaart.ai"}, {"Day": "3", "Slot": "2", "Hook": "It quit being a search engine and became an API", "ToolName": "YOU.COM", "Description": "A customizable AI search and research platform, now built for developers", "Category": "Search Engine", "Models": "Shifted in 2026 from a consumer search app to a usage-based retrieval", "Uses": "1. Building custom AI search agents\\n2. Multi-model chat\\n3. Automated research reports (ARI)", "Pricing": "Paid | $100 free credit for new users", "API": "Yes", "Company": "You.com Inc (USA)", "Website": "you.com"}, {"Day": "4", "Slot": "1", "Hook": "It scores how engaged people were in your meeting", "ToolName": "READ AI", "Description": "An AI meeting copilot that scores engagement and summarizes meetings, emails, and messages.", "Category": "Productivity", "Models": "Read AI engagement + summarization engine, 2026", "Uses": "1. Meeting summaries and action items\\n2. Scores participant engagement\\n3. Analyses emails and Slack too", "Pricing": "Freemium | Free: 5 transcripts/mo | Tier: Pro $15-19.75/user/mo, Enterprise $22.50-29.75/user/mo", "API": "Limited", "Company": "Read AI, Inc. (USA)", "Website": "www.read.ai"}, {"Day": "4", "Slot": "2", "Hook": "Build a full app with zero code - but not on free", "ToolName": "BUBBLE AI", "Description": "A full-stack no-code platform for building web and mobile apps with AI-assisted prototyping.", "Category": "Web Builder", "Models": "Bubble AI-powered prototyping and workflow generation, 2026", "Uses": "1. Full web apps with no code\\n2. Visual workflows and a built-in database\\n3. 6,000+ plugins incl. Stripe", "Pricing": "Freemium | Free: 3 trial apps, no publish | Tier: Starter $29/mo, Growth $119/mo, Team $349/mo", "API": "Yes", "Company": "Bubble Group (USA)", "Website": "bubble.io"}, {"Day": "5", "Slot": "1", "Hook": "Upload one photo. Watch it dance.", "ToolName": "VIGGLE", "Description": "Turns a photo into a dancing, lip-syncing, meme-style AI video", "Category": "Video Generation", "Models": "JST-1 video-3D foundation model, enabling physics-based motion control", "Uses": "1. Making a photo dance or move with physics-based motion\\n2. Lip-syncing characters to audio\\n3. Meme-style video creation", "Pricing": "Freemium | Free: 5 videos/day, watermarked | Pro: $4.99-9.99/mo | Live and Max: higher credit tiers", "API": "Yes", "Company": "Viggle AI (USA)", "Website": "viggle.ai"}, {"Day": "5", "Slot": "2", "Hook": "The only AI image tool that exports real SVG vectors", "ToolName": "RECRAFT", "Description": "An AI image generator built for designers, with strong text and vector support", "Category": "Graphic Design", "Models": "Recraft V4.1 model", "Uses": "1. Vector SVG graphics from text\\n2. Accurate typography inside images\\n3. Custom styles from reference images", "Pricing": "Freemium | Free: 30 credits/day, no commercial license", "API": "Yes", "Company": "Recraft (UK)", "Website": "recraft.ai"}, {"Day": "6", "Slot": "1", "Hook": "They renamed every plan. Your old guide is wrong.", "ToolName": "SURFERSEO", "Description": "An SEO and AI search optimization platform with a real-time content editor scored against top", "Category": "Marketing & SEO", "Models": "Surfer Content Editor + AI Tracker for AI search visibility, 2026", "Uses": "1. Live Content Score as you write\\n2. Keyword research and topic maps\\n3. Audit old content for gaps", "Pricing": "Freemium (trial) | Free: trial", "API": "Limited", "Company": "Surfer (Groupe Positive) (Poland)", "Website": "surferseo.com"}, {"Day": "6", "Slot": "2", "Hook": "3D objects from a text prompt - but AI isn\'t in the free tier", "ToolName": "SPLINE AI", "Description": "A 3D design tool with an AI add-on that generates editable 3D objects from text or image prompts.", "Category": "3D Generation", "Models": "Spline AI 3D Generation add-on (text-to-3D, image-to-3D), 2026", "Uses": "1. Editable 3D objects from a text prompt\\n2. 3D models from reference images\\n3. Remix objects into new variants", "Pricing": "Freemium | Free: editor only, no AI", "API": "No", "Company": "Spline, Inc. (USA)", "Website": "spline.design"}, {"Day": "7", "Slot": "1", "Hook": "It writes the article and tells you if it\'ll rank", "ToolName": "SCALENUT", "Description": "SEO-focused AI content platform with built-in ranking tools", "Category": "Content Generation", "Models": "Content optimizer with SERP analysis and NLP-driven suggestions", "Uses": "1. SEO content briefs based on top-ranking pages\\n2. Long-form blog writing\\n3. Content scoring against target keywords", "Pricing": "Freemium | 7-day free trial | Starter: $30-59/mo | Plus: $45-89/mo | Professional: $100-199/mo", "API": "Limited", "Company": "Scalenut (India)", "Website": "scalenut.com"}, {"Day": "7", "Slot": "2", "Hook": "An AI that reads contracts and flags the risky clauses", "ToolName": "ROBIN AI", "Description": "An AI legal assistant that reviews, drafts, and reports on contracts with clause-level risk scoring.", "Category": "Research & Data", "Models": "Robin AI contract intelligence engine, 2026", "Uses": "1. Contract review with clause-level risk\\n2. Redlining against your playbooks\\n3. A searchable contract repository", "Pricing": "Freemium | Free: 10 messages/day | Tier: Pro (up to 5 users), Enterprise ~$5,000-$80,000/yr", "API": "No", "Company": "Robin AI Ltd. (UK)", "Website": "www.robinai.com"}, {"Day": "8", "Slot": "1", "Hook": "Scrape any website without writing a line of code", "ToolName": "HEXOMATIC", "Description": "A no-code automation platform for web scraping, lead generation, and AI-powered content workflows.", "Category": "Data Analysis", "Models": "Hexomatic automation engine with ChatGPT and Gemini integrations, 2026", "Uses": "1. Scrape websites with no code\\n2. 100+ prebuilt sales and research flows\\n3. Lead enrichment and email finding", "Pricing": "Paid, credit-based | Free: none confirmed | Tier: starts at $24/mo, premium credits from $9.99/mo", "API": "Yes", "Company": "Hexact, Inc. (USA)", "Website": "hexomatic.com"}, {"Day": "8", "Slot": "2", "Hook": "AI websites with real 3D animation, from one prompt", "ToolName": "DORA", "Description": "A no-code AI website builder focused on generating 3D animated landing pages from a single prompt.", "Category": "Web Builder", "Models": "Dora AI 3D site generation engine (alpha 2.0), 2026", "Uses": "1. A landing page from one prompt\\n2. 3D objects and scroll animations\\n3. Drag-and-drop layout tweaks", "Pricing": "Freemium | Free: alpha access, SSL, instant publishing | Tier: Basic $14/mo, Pro $25/mo", "API": "No", "Company": "Dora Labs, Inc. (USA)", "Website": "www.dora.run"}, {"Day": "9", "Slot": "1", "Hook": "It watches a website and tells you when data changes", "ToolName": "BROWSE AI", "Description": "A no-code web scraping tool that trains AI robots to extract and monitor data from any website.", "Category": "Productivity", "Models": "Browse AI robot training engine, 2026", "Uses": "1. Extract website data with no code\\n2. Monitor pages for changes on a schedule\\n3. Chain robots into pipelines", "Pricing": "Freemium | Free: 50 credits/mo", "API": "Yes", "Company": "Browse AI, Inc. (Canada)", "Website": "www.browse.ai"}, {"Day": "9", "Slot": "2", "Hook": "900+ voices. 142 languages. One text box.", "ToolName": "PLAY.HT", "Description": "A large voice library for turning text into lifelike speech", "Category": "Audio / Podcast", "Models": "900+ voices across 142 languages with adjustable tone, pitch", "Uses": "1. Converting text to natural speech in 142\\n2. Choosing from 900+ voice options\\n3. Embedding an audio player on your website", "Pricing": "Freemium | Free: basic tier | Pro: $31/mo | Higher tiers: up to $99/mo", "API": "Yes", "Company": "Play.ht (USA)", "Website": "play.ht"}, {"Day": "10", "Slot": "1", "Hook": "This agent tool was archived in January. It still runs.", "ToolName": "AGENTGPT", "Description": "A browser-based tool that lets you assemble and deploy simple autonomous AI agents from a goal.", "Category": "Autonomous Agents", "Models": "AgentGPT, 2026", "Uses": "1. Spin up an agent from a name and a goal\\n2. Runs in the browser, no setup\\n3. Watch its progress live", "Pricing": "Freemium (frozen pricing) | Free: limited free state | Tier: Pro $40/mo, Enterprise custom", "API": "Limited", "Company": "Reworkd, Inc. (USA)", "Website": "agentgpt.reworkd.ai"}, {"Day": "10", "Slot": "2", "Hook": "Unlimited free AI art from 45+ models", "ToolName": "NIGHTCAFE", "Description": "A community-driven AI art generator with a generous free tier", "Category": "Image Generation", "Models": "Access to 45+ image and video models including Flux, SDXL, Nano Banana", "Uses": "1. Unlimited free Stable Diffusion runs\\n2. Daily art challenges and gallery\\n3. 45+ models in one place", "Pricing": "Freemium | Free: unlimited base generations | AI Beginner: $5.99/mo | Hobbyist: $9.99/mo", "API": "No", "Company": "NightCafe Studio (Australia)", "Website": "nightcafe.studio"}, {"Day": "11", "Slot": "1", "Hook": "It scores your cold email before you hit send", "ToolName": "LAVENDER", "Description": "An AI email coach that scores cold emails and suggests rewrites to improve sales reply rates.", "Category": "Marketing & Sales", "Models": "Lavender email scoring engine + Ora AI SDR agent, 2026", "Uses": "1. Scores emails 0-100 on tone and length\\n2. AI rewrites to lift reply rates\\n3. Pulls LinkedIn data into the sidebar", "Pricing": "Freemium | Free: 5 emails/mo | Tier: Starter $29/mo, Individual Pro $49/mo, Teams $69/user/mo", "API": "No", "Company": "Lavender.ai, Inc. (USA)", "Website": "www.lavender.ai"}, {"Day": "11", "Slot": "2", "Hook": "One photo becomes an avatar that answers live", "ToolName": "D-ID", "Description": "Turns a photo and script into a talking avatar, with real-time AI agents", "Category": "Video Generation", "Models": "Creative Reality Studio plus real-time conversational AI Agents", "Uses": "1. A photo becomes a talking avatar\\n2. Interactive AI agents for websites\\n3. Natural multi-language dialogue", "Pricing": "Freemium | 14-day free trial | Lite: $4.70-5.90/mo | Pro: $29/mo | Advanced: $196/mo | Enterprise: custom", "API": "Yes", "Company": "D-ID (Israel)", "Website": "d-id.com"}, {"Day": "12", "Slot": "1", "Hook": "It predicts how your ad copy will perform before you run it", "ToolName": "ANYWORD", "Description": "AI copywriting tool that predicts how well your marketing text will perform", "Category": "Content Generation", "Models": "Predictive Performance Scoring, Data-Driven Personas", "Uses": "1. Scores ad copy before you publish\\n2. Personas built from your CRM data\\n3. Image captions and video scripts", "Pricing": "Freemium | Free: 7-day trial | Starter: $39-49/mo | Data-Driven: $79-99/mo | Business/Enterprise: custom", "API": "Yes", "Company": "Anyword (Israel)", "Website": "anyword.com"}, {"Day": "12", "Slot": "2", "Hook": "Drop in a spreadsheet, get a dashboard back", "ToolName": "POLYMER", "Description": "A no-code AI analytics tool that turns spreadsheets into charts and dashboards automatically.", "Category": "Data Analysis", "Models": "Polymer AI visualization engine, 2026", "Uses": "1. Upload a spreadsheet, get charts\\n2. Dashboards with no formulas\\n3. Spots patterns automatically", "Pricing": "Paid only | Free: none confirmed | Tier: starts around $10-25/mo", "API": "No", "Company": "Polymer Search, Inc. (USA)", "Website": "www.polymersearch.com"}, {"Day": "13", "Slot": "1", "Hook": "Make a song and release it to Spotify the same day", "ToolName": "BOOMY", "Description": "Make and release AI-generated songs straight to Spotify and Apple Music", "Category": "Music Generation", "Models": "AI composition engine plus built-in distribution to major streaming", "Uses": "1. Songs generated in seconds\\n2. Publish to Spotify and Apple Music\\n3. Add vocals, adjust instruments", "Pricing": "Freemium | Free: 25 songs/mo, no distribution | Creator: $2.99-9.99/mo", "API": "Limited", "Company": "Boomy (USA)", "Website": "boomy.com"}, {"Day": "13", "Slot": "2", "Hook": "An AI companion that remembers your conversations", "ToolName": "REPLIKA", "Description": "A personal AI companion for daily conversation and emotional support", "Category": "LLM / Chatbot", "Models": "Replika\'s proprietary conversational model", "Uses": "1. Daily companionship and check-ins\\n2. Voice calls with your AI companion\\n3. Customizing your Replika\'s look and personality", "Pricing": "Freemium | Free: basic chat | Pro: $19.99/mo or $69.99/yr | Ultra: $29.99/mo | Lifetime: $299.99 one-time", "API": "No", "Company": "Luka, Inc. (USA)", "Website": "replika.com"}, {"Day": "14", "Slot": "1", "Hook": "Free autonomous agents, running in your browser", "ToolName": "GODMODE", "Description": "A browser-based platform that runs generative AI agents inspired by AutoGPT and BabyAGI to automate", "Category": "Autonomous Agents", "Models": "Godmode.space generative agent interface (GPT-3.5/GPT-4 powered), 2026", "Uses": "1. Give an agent a task, it works alone\\n2. Content generation and basic analysis\\n3. Runs in-browser, no install", "Pricing": "Free | Free: free to use | Tier: none (OpenAI API costs may apply)", "API": "Limited", "Company": "Emil Ahlback (indie)", "Website": "godmode.space"}, {"Day": "14", "Slot": "2", "Hook": "The AI SDR costs $800/mo. The email tool costs $49.", "ToolName": "REPLY AI", "Description": "A sales engagement platform with an AI SDR that sources leads and runs outbound sequences", "Category": "Marketing & Sales", "Models": "Reply.io Jason AI SDR + multichannel sequencing, 2026", "Uses": "1. Outbound across email, LinkedIn, calls\\n2. Jason AI SDR sources leads and writes\\n3. Inbox warm-up for deliverability", "Pricing": "Freemium (trial) | Free: limited trial", "API": "Yes", "Company": "Reply.io, Inc. (USA)", "Website": "reply.io"}]'
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
    out=f"Fortnight_03/Carousels/{slug(i,r['ToolName'])}"
    if os.path.isdir(out) and len([x for x in os.listdir(out) if x.endswith('.jpg')])==8:
        print("skip", out); continue
    build(r,out); n+=1
    print("built", out)
print("TOTAL", n)
