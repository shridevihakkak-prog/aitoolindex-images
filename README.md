# aitoolindex-images

Public image host for @aitoolindex Instagram carousel posts. Images referenced by GITHUB_RAW_BASE_URL in aitoolindex-bot.

## Rolling queue (from Nov 2026)

`tool_data/queue.json` is the single source of truth for upcoming carousels.
Editing it triggers `Render queue slides`, which renders `Queue/<Id>_<Tool>/Slide_1..8.jpg`
and records a data hash per folder in `Queue/manifest.json`. aitoolindex-bot posts the
next unposted entry and refuses to post slides that don't match the current data.
Every entry carries `LastChecked`, shown on the cover, the pricing slide and in the caption.
The weekly review re-verifies upcoming entries, adds newly launched tools and tops the queue up.
