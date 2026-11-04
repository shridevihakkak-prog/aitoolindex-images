# aitoolindex-images

Public image host for @aitoolindex Instagram carousel posts. Images referenced by GITHUB_RAW_BASE_URL in aitoolindex-bot.

## Rolling queue (from Nov 2026)

`tool_data/queue.json` is the single source of truth for upcoming carousels.
Editing it triggers `Render queue slides`, which renders `Queue/<Id>_<Tool>/Slide_1..8.jpg`
and records a data hash per folder in `Queue/manifest.json`. aitoolindex-bot posts the
next unposted entry and refuses to post slides that don't match the current data.
Every entry carries `LastChecked`, shown on the cover, the pricing slide and in the caption.
The weekly review re-verifies upcoming entries, adds newly launched tools and tops the queue up.

## Formats (v2, Nov 2026)

Two formats from `aitoolindex_post_strategy.md`, rendered at 1080x1350 from
`templates/base.css` + `templates/slide.html.j2` (HTML/CSS, headless Chromium):

- **Run This Prompt** (`Format: "prompt"`, 6 slides) - 09:00 IST daily
- **Tool Teardown** (`Format: "teardown"`, 7 slides, with an honest-limit and a cheaper-option slide) - 21:00 IST Mon/Wed/Fri/Sun

Fonts are bundled in `_fonts/` (Archivo Black, Inter, JetBrains Mono - SIL Open Font License, see `_fonts/OFL.txt`).
