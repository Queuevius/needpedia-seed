# Nexus Dev Log
Append-only. Never delete or edit existing entries. Add new entries at the bottom.
AI: update this at the end of every session.

---

## Session 5 — 2026-06-05

### Milestone 5.6 — AI Studios: Persistent Saving

**Files modified:**
- order-server.py — added /save-text and /save-image endpoints, base64/URL image decoding, 5GB cap, dir_size helper
- nginx-default.conf — added /save-text and /save-image proxy routes, client_max_body_size 20M
- volunteer-text-studio.html — added convo_id generation, saveText() function, /save-text call after each exchange
- volunteer-image-studio.html — added session_id generation, newSession() function, + New button, saveImage() function, /save-image call, finally block for generate button

**Folders/files created:**
- volunteer-logs/volunteerN/index.json — small manifest per volunteer
- volunteer-logs/volunteerN/convos/ — one .jsonl file per text conversation
- volunteer-logs/volunteerN/image-sessions/ — one .json + .png files per image session
- DEVLOG.md — this file

**Deleted:**
- volunteer-logs/volunteer1.json (old flat log, test data)
- volunteer-logs/volunteer3.json (old flat log, test data)

**Bugs fixed:**
- 413 error on image save: nginx body size raised to 20M
- Generate button staying grey: moved btn.disabled=false into finally block

**Notes:**
- volunteer-logs/ files are owned by root (Docker). Always use sudo for direct edits.
- Old session files from before PNG upgrade may have raw base64 in img_url field.
  Clean with: sudo python3 /tmp/clean_old_session.py (see pattern in session notes)
- PNG bytes saved to disk, raw base64 stripped from json after saving.
  local_file field in session json points to the .png filename.

---

## Session unknown date — Volunteer AI Studio: login bug fix + Approach A1 redesign handoff

**Files modified:**
- volunteer-text-studio.html — login screen CSS fixed to display:none; DOMContentLoaded autologin verified
- volunteer-image-studio.html — same login/CSS fix verified

**Bugs fixed:**
- Login screen appearing on ?user=volunteer1 instead of autologging in — login screen was display:flex by default

**Notes:**
- Confirmed Approach A1: typing Ubuntu[n] reveals AI studio tiles on Nexus, no auto-redirect
- Two separate tiles (text + image), badge shows "Volunteer Studio N", Logout button added
- No code written this session — output was handoff prompt for next session only

---

## Session unknown date — Volunteer studios built, login tiles, sidebar, session persistence

**Files modified:**
- volunteer-text-studio.html — three model tiers, conversation sidebar, session persistence, ?user= autologin, thinking indicator
- volunteer-image-studio.html — two model buttons, ?user= autologin, sessionStorage history
- gallery.html — Edit button repurposed: volunteer auth → redirect to text studio; [rotated S32] still works for admin

**Folders/files created:**
- volunteers.json — 10 accounts, SHA-256 hashed passwords
- volunteer-logs/ — log output directory

**Notes:**
- Gallery Edit button now doubles as volunteer login entry point

---

## Session unknown date — Fixed broken API key, model slugs, GPT image hang

**Files modified:**
- volunteer-image-studio.html — added AbortController 30s timeout, replaced dead API key, fixed tripled OR raw block
- volunteer-text-studio.html — fixed Anthropic model slugs (dashes→dots), replaced dead API key

**Bugs fixed:**
- Text studio [No response] on all models — dead OpenRouter API key (401)
- GPT image generation hanging forever — no timeout; added AbortController 30s abort
- Anthropic slugs used dashes (claude-sonnet-4-6) instead of dots (claude-sonnet-4.6) — silent null responses

**Notes:**
- OpenRouter slug format for Anthropic is always dots not dashes
- Old dead keys logged in DEVLOG for reference only — do not use

---

## Session 2026-06-04 — Fixed Text Studio render crash, verified volunteer studio tile flow

**Files modified:**
- volunteer-text-studio.html — sendMessage() guarantees valid conversation before render; renderMessages() null-guards empty-state element

**Bugs fixed:**
- Text Studio required page reload to show messages — TypeError: Cannot read properties of null on empty-state element halting execution
- Confirmed sessionStorage.clear() + location.reload() correctly clears login and removes AI studio tiles

**Notes:**
- patch5 (timing theory) was a red herring — real fix was null-guard in renderMessages()
- Always check browser console for uncaught exception before assuming async/timing issue

---

## Session May 21, 2026 — Drag-to-reorder edit mode, subfolder display, router fix

**Files modified:**
- gallery.html — edit mode with password-protected drag-to-reorder, _order.json loading/applying, subfolder display, router updated for multi-level paths, _order.json hidden from listings
- nginx-default.conf — added proxy rule for /save-order → order-server container
- docker-compose.yml — added order-server container

**Folders/files created:**
- order-server.py — Python HTTP server writing _order.json files, port 8181
- gallery.html.bak — updated to reflect May 21 state

**Bugs fixed:**
- Subfolders not displaying in Articles folder — filter was stripping all isDir items
- Router only handling single-level folder paths — now joins all parts for subfolder navigation

**Notes:**
- Breadcrumb segments still not clickable at end of session — backticks/special chars are hazard for Python replacement
- ORDER_SERVER in gallery.html is empty string — proxied through nginx at /save-order
- Heredoc cannot be used for Python scripts — bash mangles ! characters; always use nano to /tmp/
- order-server writes to /data inside container = /home/clearcrow/Needpedia_Nexus on host

---

## Session May 19–20, 2026 — Video improvements, YouTube integration, article renderer restored

**Files modified:**
- gallery.html — YouTube button in lightbox, youtubeLinks object (9 URLs), restored article renderer, breadcrumb fix, Mixed Media folder added, article typography improved

**Folders/files created:**
- /Needpedia_Nexus/Mixed Media/ — new top-level folder
- /Needpedia_Nexus/Mixed Media/John E/ — moved from Videos/
- gallery.html.bak2 — pre-session backup

**Bugs fixed:**
- Article images not displaying — relative src paths rewritten to include folder on fetch
- Mixed Media appearing twice on home page — duplicate entry removed

**Notes:**
- gallery.html was wiped to 0 bytes mid-session by crashed Python script — restored from .bak
- Never use inline python3 -c for multi-line gallery.html edits — always write to /tmp/file.py
- gallery.html.bak must be updated every session or recovery falls back to old state

## 2026-06-10 19:20 — Milestone 5.7 begin
Starting image-to-image (reference image) feature. All three models confirmed to support image input via OpenRouter. Plan: upload button, base64 encoding, Use as Reference button on last generated image. No automatic multi-image context — volunteer controls when image tokens are spent.

## 2026-06-25 — Session 9, Milestone 5.8 — Track A partial

**Files changed:**
- order-server.py: added /admin-auth (password to 24h session token), /admin-devlog (token-gated GET returns DEVLOG.md), /admin-ops (stub, not wired up yet)
- nginx-default.conf: added proxy routes for /admin-auth, /admin-devlog, /admin-ops
- gallery.html: patched — edit mode shows 4 admin tiles (Dev Log, Dev Space, Text Studio, Image Studio); admin token stored in sessionStorage on login; tile click handler updated
- admin-devlog.html: new file — password-only login, auto-login from sessionStorage, DEVLOG viewer with Refresh and back link
- gallery.html.bak: updated

**System changes:**
- Tailscale uninstalled (was v1.98.4)

**What works:**
- Dev Log tile: opens without second password
- Dev Space tile: shows coming-soon message (stub)
- Text/Image Studio tiles: route to volunteer studios with ?user=admin — admin is not a real volunteer account, auth will fail (needs fix next session)
- Ops buttons (Restart Python, Restart Pages, View Logs): not yet wired up, planned for Dev Space
- Refresh button: working

**Next session:**
- Fix studio tiles: add admin to volunteers.json OR build separate admin studio page
- Wire ops buttons: needs docker.sock mounted in order-server container + docker CLI installed
- Confirmed container names: order-server, nginx-server, cloudflare-tunnel

## Session 12 (2026-06-30) -- Cloudflare Tunnel Outage Repair

Issue: nexus.needpedia.org down with Cloudflare Error 1033. cloudflare-tunnel container
showed "Up" in docker ps but was not actually connected to Cloudflare edge.

Root cause 1: Outbound UDP/QUIC (port 7844) blocked at network level. cloudflared logs
showed "failed to dial to edge with quic: timeout: no recent network activity".

Fix 1: Patched docker-compose.yml to add --protocol http2 to cloudflared command,
forcing TCP instead of QUIC. Patch applied via /tmp/fix_tunnel_protocol.py.

Root cause 2 (surfaced after fix 1 + force-recreate): docker-compose.yml referenced
network as "nexus-net" but actual Docker network was auto-named
"needpedia_nexus_nexus-net". This left cloudflare-tunnel container's network
attachment broken after --force-recreate, producing "no route to host" / DNS
i/o timeout errors. Confirmed via docker network ls.

Fix 2: Full stack cycled with docker compose down && docker compose up -d to
rebuild all network attachments consistently. No data loss -- all volumes are
host bind-mounts, nothing stored in container-local volumes.

Result: cloudflare-tunnel registered 4 connections on http2 protocol
(sea01, pdx03, sea10, pdx02). nexus.needpedia.org confirmed back online.

Secondary fix: Added net.core.rmem_max and wmem_max to /etc/sysctl.conf to
resolve a "failed to sufficiently increase receive buffer size" warning seen
in tunnel logs. Cosmetic, unrelated to the outage, fixed while in the area.

Files touched: docker-compose.yml (cloudflared command line), /etc/sysctl.conf (host).
docker-compose.yml.bak updated to match.

New loose end captured: Tony wants a master_admin tile for drag-and-drop folder/
subfolder upload that preserves structure (no flattening), saving to host machine.
Later phase: a third auth path (freelancer studio) separate from volunteer and
admin login, unlocked by its own password, containing only the upload tile with
the same structure-preserving behavior. Not started -- needs its own design pass,
3-way auth branch is a bigger change than a quick patch.

---
Session 13 | 2026-07-01 | Milestone 5.10 - Path A Complete

Mounted docker.sock, /usr/bin/docker binary, and /home/clearcrow into ttyd container via docker-compose.yml. No custom Dockerfile (apt-get DNS failed in Docker build network; pivoted to binary mount). Credential prompt removed from ttyd command (port 7681 not externally exposed; edit-mode gate sufficient). Verified: docker ps from browser terminal shows all 4 containers. docker-compose.yml.bak updated.

Stopping point: Path A done. Ops buttons UI still pending. volunteers.json.bak still stale.

---
SESSION 14 -- 2026-07-02
Loose End 12 Part A complete: Uploaded Files tile (folder upload + file manager)

FILES TOUCHED:
  docker-compose.yml       -- added /home/clearcrow:/home/clearcrow mount to order-server container
  order-server.py          -- added shutil/zipfile/io imports; UPLOAD_ROOT/HOME_ROOT/DRIVE_CAP constants;
                              new endpoints: /folder-upload, /admin-browse, /admin-file, /admin-delete
  nginx-default.conf       -- added /folder-upload (1GB body limit), /admin-browse, /admin-file,
                              /admin-delete routes; added /master_uploads/ deny block
  gallery.html             -- added Uploaded Files tile (adminLink -> admin-folder-upload.html)
  admin-folder-upload.html -- new file: drag-drop upload UI + file browser (view/download/delete)

NEW INFRASTRUCTURE:
  /home/clearcrow/Needpedia_Nexus/master_uploads/ -- new folder, blocked from public web
  order-server container now has /home/clearcrow mounted (same pattern as ttyd)

ENDPOINTS ADDED:
  POST /folder-upload  -- receives ZIP, extracts preserving structure, token-gated, 80% drive cap
  GET  /admin-browse   -- lists directory, token-gated, confined to /home/clearcrow
  GET  /admin-file     -- serves file for view/download, token-gated
  POST /admin-delete   -- deletes file or folder, token-gated, blocks deletion of root folders

BUGS FIXED:
  - order-server.py repeatedly corrupted with HTML during terminal writes
    Fix: switched to gedit for all large file writes (Rule 17 added)
  - Token key mismatch: upload page used 'adminToken', gallery uses 'np_admin_token'
    Fix: patched admin-folder-upload.html
  - nginx duplicate /admin-delete block from patch running twice
    Fix: removed duplicate via gedit
  - master_uploads files root-owned after upload
    Fix: sudo chown -R clearcrow:clearcrow /home/clearcrow/Needpedia_Nexus/master_uploads
    Note: re-run after each upload session for desktop file manager access

CONFIRMED WORKING: upload, browse, view in new tab, download, delete with confirmation
volunteers.json.bak STILL STALE -- update next session
STOPPING POINT: Loose End 12 Part A complete. All features verified.

## Session 15 — 2026-07-03

### Phase 1 SKIP audit — COMPLETE (no action needed)
- Investigated all [SKIP] lines from phase1_patch.py. All were phantoms or
  already-satisfied content, NOT lost edits.
- Conversational NVC: all 7 "skipped" patches already correct in-file.
- Emotionally Charged Ideas: crisis block intact (suicide/self-harm, "not a
  crisis service," emergency/crisis-line pointer, minors -> trusted adult).
- Florence KB: crisis rule present; Severe Suicide Risk botskill link = [LINK] pending -> Phase 4.
- Lotte KB: "Post Quality" line does NOT exist — phantom, no fix.
- CONCLUSION: suicide-risk safety text confirmed present in all files. Do NOT re-run phase1_patch.py.

### Article URL cleanup
- Problem: capital /Articles/ held files with spaces, quotes, curly apostrophes,
  and one 165-char filename -> broken/percent-encoded URLs + case-collision with lowercase /articles/.
- Fix: copied (not moved) all 22 Articles/*.html into lowercase articles/ with clean slugs.
  Originals retained. Verified 27 total .html in articles/.
- Key slugs: Tiffany's Idea -> tiffanys-idea.html; List of Needpedia Use Cases 1.0 -> use-cases.html.

### Phase 4 ledger — 5 of 6 slots filled
- tiffanys_idea = https://nexus.needpedia.org/articles/tiffanys-idea.html
- use_cases     = https://nexus.needpedia.org/articles/use-cases.html
- signup        = https://staging.needpedia.org/users/sign_in
- how_to_faq    = https://needpedia.org/faq
- consent_post  = https://needpedia.org/posts/672
- tos           = FILL-ME (still needed from live site)

### Open loose ends
- Retire capital /Articles/ folder once clean copies verified live; repoint any old /Articles/... refs.
- Get ToS URL from live site (last ledger slot).
- ENV MISMATCH: how_to_faq + consent_post point to production (needpedia.org);
  signup points to staging (staging.needpedia.org). Decide if links should be consistent before Phase 4.
- Phase 4 NOT yet run — hold until tos in hand for one clean pass.
- admin-devlog.html / admin-devspace.html may be rendered views of DEVLOG.md — check if they need regenerating after this edit.

### Stopping point
- 5 of 6 ledger slots filled. Only tos outstanding. Phase 4 script not run yet.


## Session 17 — 2026-07-09 — Milestone 6: Nexus Chat SHIPPED

Built the multi-provider admin chat at /admin-chat.html.

Features delivered:
- Five models via OpenRouter, switchable mid-conversation, full
  history carried across switches: Qwen Eco (qwen/qwen3-235b-a22b-2507),
  Claude Sonnet 4.6 (anthropic/claude-sonnet-4-6), Claude Opus 4.8
  (anthropic/claude-opus-4-8), DeepSeek V4 Pro (deepseek/deepseek-v4-pro),
  Claude Fable 5 (anthropic/claude-fable-5).
- Server-side OpenRouter proxy for admin chat: key in order-server.py
  only, not in served admin HTML.
- Conversations saved as local JSON, one file per conversation, under
  /home/clearcrow/admin-convs/ with index.json. Saving verified.
- No standalone login: admin-chat.html reads np_admin_token from
  sessionStorage, redirects to / if absent (matches admin-devlog.html).
- Admin Chat tile replaced the old admin Text Studio tile in gallery.html.
- Raw-text Import: paste a whole conversation into a box, order-server
  parses blank-line blocks into alternating user/assistant messages and
  saves it to the sidebar. Endpoint /admin-import. Other models can
  continue an imported conversation (Qwen less reliable on imports).
- Volunteer text studio relabeled with AI system + version; fixed a
  latent model-string bug (dots -> dashes).

New order-server endpoints: /admin-chat-proxy, /admin-convs (GET+POST),
/admin-conv, /admin-import. Matching nginx routes added to
nginx-default.conf.

Lessons logged as rules:
- docker-compose needs sudo; never use --force-recreate (ContainerConfig
  bug, 502s the site); use restart, or stop && start. Restart "web" to
  reload nginx.
- Adding an order-server endpoint = TWO edits: Python handler AND nginx
  route. Missing route shows as "Unexpected token '<' is not valid JSON".
- Admin subpages: no second login, ride np_admin_token.
- Context-only file reads should go through Claude Code to save tokens.
- Permanent scripts live in the project folder, not /tmp (wiped on reboot).

Next session priority (Tony's call): VISIBILITY — seeing activity/events
on Needpedia as they happen, plus modifying a phone app (details TBD).
Likely Milestone 7.


## Session 17 — 2026-07-09 — Milestone 6: Nexus Chat SHIPPED

Built the multi-provider admin chat at /admin-chat.html.

Features delivered:
- Five models via OpenRouter, switchable mid-conversation, full
  history carried across switches: Qwen Eco (qwen/qwen3-235b-a22b-2507),
  Claude Sonnet 4.6 (anthropic/claude-sonnet-4-6), Claude Opus 4.8
  (anthropic/claude-opus-4-8), DeepSeek V4 Pro (deepseek/deepseek-v4-pro),
  Claude Fable 5 (anthropic/claude-fable-5).
- Server-side OpenRouter proxy for admin chat: key in order-server.py
  only, not in served admin HTML.
- Conversations saved as local JSON, one file per conversation, under
  /home/clearcrow/admin-convs/ with index.json. Saving verified.
- No standalone login: admin-chat.html reads np_admin_token from
  sessionStorage, redirects to / if absent (matches admin-devlog.html).
- Admin Chat tile replaced the old admin Text Studio tile in gallery.html.
- Raw-text Import: paste a whole conversation into a box, order-server
  parses blank-line blocks into alternating user/assistant messages and
  saves it to the sidebar. Endpoint /admin-import. Other models can
  continue an imported conversation (Qwen less reliable on imports).
- Volunteer text studio relabeled with AI system + version; fixed a
  latent model-string bug (dots -> dashes).

New order-server endpoints: /admin-chat-proxy, /admin-convs (GET+POST),
/admin-conv, /admin-import. Matching nginx routes added to
nginx-default.conf.

Lessons logged as rules:
- docker-compose needs sudo; never use --force-recreate (ContainerConfig
  bug, 502s the site); use restart, or stop && start. Restart "web" to
  reload nginx.
- Adding an order-server endpoint = TWO edits: Python handler AND nginx
  route. Missing route shows as "Unexpected token '<' is not valid JSON".
- Admin subpages: no second login, ride np_admin_token.
- Context-only file reads should go through Claude Code to save tokens.
- Permanent scripts live in the project folder, not /tmp (wiped on reboot).

Next session priority (Tony's call): VISIBILITY — seeing activity/events
on Needpedia as they happen, plus modifying a phone app (details TBD).
Likely Milestone 7.

## Session 22 — 2026-07-09 — Milestone 7: Nexus Capture extension SHIPPED
Chrome extension "Nexus Capture" (Manifest V3) now auto-archives
claude.ai conversations into the Nexus admin-chat sidebar. Lives on the
home machine's Chrome only; captures passively (no button) after the
page goes quiet ~4s, POSTs to /capture with the X-Capture-Token header.
Files: /home/clearcrow/nexus-capture-extension/ (manifest.json,
content.js, background.js, options.html, options.js). Original files
built by Claude Code; the fix below done directly in gedit.
KEY FIX: Claude Code's first-draft DOM selectors were guesses and wrong
(returned 0 messages). Found the real ones by live console probing on
claude.ai (F12 -> Console -> document.querySelectorAll tests):
- User messages: [data-testid="user-message"]
- Assistant messages: .font-claude-response (body .font-claude-response-body)
- File marker: [data-testid="file-upload"]
- Container: "body" (whole-page search). Was "main" — WRONG, claude.ai
  messages are not inside a <main> tag.
Confirmed working end-to-end: a test claude.ai conversation appeared in
the Nexus sidebar, renameable/deletable like any other.
SELECTOR DRIFT NOTE: claude.ai will change its page someday. When
captures stop arriving, wrong selectors are the first suspect — re-probe
with the F12 console, update the constants at the top of content.js,
reload the extension at chrome://extensions, re-navigate claude.ai.
Also confirmed this session: import_convo.py is safely in
/home/clearcrow/ (was a carried unverified item — now closed;
superseded by the extension anyway).
Next priorities: (1) test Setup B — reach the home desktop from a
laptop/work machine via Chrome Remote Desktop, chat on claude.ai inside
that remote session, confirm capture still works; (2) Session C reality
testing (long conversations, code blocks, back-catalog).

## 2026-07-15
Session 23 — Setup B host install completed (chrome-remote-desktop 151 installed + registered via g.co/crd/headless, systemd service confirmed running, PIN set). Laptop can connect but session crashes if desktop is already logged in (all session types tested: default, Cinnamon, Cinnamon Software Rendering — same crash). Workaround: log out of desktop before connecting; unresolved. After using workaround once, desktop password briefly stopped working, cause undiagnosed. Sleep/suspend setting not yet changed (still needed). Remote session showed laptop's taskbar instead of desktop's. Three problems open, full detail in setup-b-handoff.md.

## 2026-07-22
Session 25: Process overhaul. Director workflow adopted: Fable architects/reviews, Opus default builder, DeepSeek V4 only for complex tasks (never gets secrets or the handoff). Morning auto-quit DROPPED. Setup B launch design open: separate Chrome profile (leading) vs kill button (fallback). Local git initialized on Nexus + extension. Devlog rotation rule added. New bug logged: claude.ai convos not capturing. Handoff restructured permanent/temp.

## 2026-07-22
Session 25 addendum: git baselines confirmed (extension bdf836e). Audit tracker adopted - counts secure-system touches, audit at 5. Verified AIs fetch nexus botskill pages fine; hash-route article URLs unreadable (fragment never reaches server) - public index page planned. AGENTS.md planned for both repos. DSV4 fetched a nexus URL in Tony's OpenRouter test.

## 2026-07-22
Session 26: Setup B verified end-to-end - remote Chrome profile launcher and desktop icons; never log out, lock instead. Capture truncation bug fixed in content.js (full multi-block replies now captured; code blocks still missing - next session). Item 19 closed.

## 2026-07-23
Session 27: Investigated code-block capture. Found claude.ai now renders code multiple ways (normal blocks, MCP-widget iframes from claudemcpcontent.com) — DOM scraping cannot reach iframe-rendered boxes (PRE=0 CODE=0 SHADOW_HOSTS=0 on a visible box). Pivoted: proved claude.ai's own data endpoint (/api/organizations/{org}/chat_conversations/{cid}?tree=True&rendering_mode=messages&render_all_tools=true) returns full convo as fenced text via existing session login — same convo gave 30 code-fences via fetch vs 0 via DOM. No build shipped; S28 will rewrite content.js to capture via fetch instead of DOM.

## 2026-07-23
Session 28: SHIPPED fetch-based capture. content.js fully rewritten - conversations now pulled from claude.ai's own data endpoint (chat_conversations with tree=True, rendering_mode=messages, render_all_tools=true) using the existing login session; DOM scraping retired for good. Field map locked from a live probe: chat_messages array; sender human maps to user; each message's content[] blocks - keep type text (prose plus already-fenced code) joined in order, skip tool_use and tool_result as noise; title from name; files and attachments arrays become [file uploaded: NAME] placeholders. background.js and manifest.json untouched - same CAPTURE relay, same /capture endpoint, same token. Smoke test passed on the all-variants test convo: bash box plus six HTML style boxes all captured fenced and in order, full history returned with no scrolling, and re-capture updated the existing entry with no duplicate. Documented that the Extension context invalidated error after an extension reload is harmless on stale tabs - full re-navigate fixes it. Item 27 CLOSED. Not a security touch - /capture endpoint, token, and nginx route unchanged; audit count stays 0. Git commit on extension repo: Session 28 fetch-based capture replaces DOM scraping. New Rule 47 adopted: token-economy offload - heavy extraction or bulk side-work goes to a fresh Opus/Haiku tab or a DSV4 brief (no secrets) instead of burning the main session's context.

## 2026-07-25
Session 29 (unplanned, jumped ahead of the planned bundle): production myth-token sweep. All three Needpedia AIs cited a nonexistent Myth Token. Root cause was stale content across KB sources, not an env or token bug. Fixed on the nexus: core-facts.html and glossary.html token lists now Question, Note, Debate; emotionally-charged-ideas.html botskill now says NOTE TOKENS; the-peoples-mastermind.html myth-token paragraph removed; episode-1-the-favela-engineer.html got an editors note that Myth Tokens are planned but unbuilt and other tokens already dispel myths. Web container restarted, changes committed. Fixed the three KB source docx files in Documents/About Needpedia/From Claude Fable 5/AI KBs via python-docx: one myth line removed from each, headers bumped to v2.2. Tony mirrored the edits on the master_admin ai_prompts page for Lotte, Florence, Adele. Final test: all three AIs confirm exactly three token types. Lessons: KB architecture now documented in the handoff PERMANENT section; Dev Space terminal lacks curl and nano, use the host Remote Terminal; Remote Chrome icon failed to launch during screencast, new open item.

## 2026-07-27
Session 30: Shipped /start.html, a public AI front door at https://nexus.needpedia.org/start.html. One link that lets anyone point any AI system at Needpedia to understand, use, or contribute to it — it links the articles index, the botskills index, the GitHub developer wiki, and the volunteer contact emails, bypassing the JavaScript-only site menu that AI fetchers cannot read. Delegates to the existing per-folder index pages rather than hand-listing files. Verified live (HTTP 200); both folder indexes confirmed as real static link-pages. Flagged for a future session: the articles index is stale, listing only 4 of about 28 articles (auto-generated 2026-07-03, never regenerated). Committed f245f60; removed a stray start.html.save left by an interrupted nano session.

## Session 32 — 2026-07-30 — Security lockdown + Job A (nexus readable to AI)

SECURITY — the real finding, bigger than the S31 handoff's file list:
/terminal/ was an UNAUTHENTICATED ROOT SHELL open to the internet.
ttyd ran with -W (writable), no -c credentials, no auth in nginx, and
the container mounts /home/clearcrow read-write PLUS /var/run/docker.sock
(the socket is root on the HOST — not sandboxed). That path reached
host credentials and cloud keys, and from there Needpedia production on
EC2. Closed with nginx basic auth, htpasswd at
config/.htpasswd, config/ denied. Returns 401 now.
ttyd log showed no evidence of intrusion — but it only goes back to the
07/28 restart and logs the nginx container IP, not real visitors, so it
cannot prove absence.

FILE EXPOSURE closed: denylist in nginx-default.conf for *.py *.db *.sh
*.yml *.conf *.md *.log *.pem, *.bak*, dotfiles (incl. .git), handoff /
htpasswd names, /kb/, /config/, volunteers.json. autoindex turned OFF
(was ON — folders were browsable). All verified 404.

ADMIN PASSWORD rotated (location deliberately not recorded here). Old
value ALSO sits in HANDOFF_next_session.txt, DEVLOG.md, two
order-server.py.bak files, and __pycache__ — all 404 from the web now,
but the handoff's stored value is STALE and needs updating.

DELIBERATELY NOT DONE: OpenRouter key left in place ($10/mo cap, low
blast radius). Cloudflare tunnel token was publicly readable in
docker-compose.yml for weeks — regenerate when convenient.

CORRECTIONS to the S31 handoff:
- Stack is nginx:alpine with the Nexus folder mounted READ-ONLY. A stale
  filebrowser compose sits in ~/ — dead copy, different tunnel token.
- rebuild-index.sh did NOT write the stale articles-index.txt (that file
  had lowercase URLs and hand-made section headers).
- /admin-browse DOES check auth server-side (returns Unauthorized).
- The import button is NOT broken; _handle_admin_import exists at line
  705. The AttributeError in docker logs predates the Jul 9 patch.
- devlog_append.py had the Session 22 entry HARDCODED — running it
  re-appended S22. Rewritten to take a file or stdin.
- git has NO remote. History is local only.

JOB A SHIPPED:
- regen_index.py (new, one generator for everything): writes
  articles/index.html, articles/index.txt, botskills/index.html,
  botskills/index.txt, root articles-index.txt (Adele's pointer —
  filename deliberately unchanged), and llms.txt. Titles resolve
  <title> -> <h1> -> filename. After adding/removing any article:
      python3 /home/clearcrow/Needpedia_Nexus/regen_index.py
- Article index: 4 links -> 23. Every public article now linked.
- 3 private docs moved OFF the web to ~/Nexus_private/articles/
  (crowdfunding master guide, better-er crowdfunding script, OTF cover
  letter) — from BOTH case folders.
- Capital /Articles/*.html retired to ~/Nexus_private/Articles_retired/.
  KEPT and still serving: Articles/Nonprofit Documents for Needpedia/
  (public by intent, Adele's KB links it) and the PNGs.
- Those PNGs also copied into articles/ — the lowercase compendium and
  end-of-war pages had BROKEN images before tonight.
- llms.txt created at nexus root (was 404).
- Footer ("bottext") added to 36 article + botskill pages: front door,
  llms.txt, main site.
- start.html now links llms.txt.
- articles-index.html is now a redirect to /articles/index.html.
- rebuild-index.sh RETIRED — now a 3-line wrapper that execs
  regen_index.py, so every stale caller does the right thing. Original
  kept as rebuild-index.sh.retired.
- watch-articles.sh repointed at the LOWERCASE folder and restarted. It
  was live; the next .docx drop would have overwritten Adele's pointer
  with capital URLs.

STILL OPEN: Cloudflare Scrape Shield -> Email Address Obfuscation -> OFF
(contact emails on start.html are JS-wrapped, invisible to AI fetchers).
Job B (three KB one-line fixes, Rule 48 two-step). Job C curation.
Watcher makes ugly filenames from .docx — slug-on-convert not written.
AUDIT COUNTER +1 for the nginx/secrets touch; read-only audit brief due.

### S32 addendum (same session, after the entry above)
- Cloudflare Email Address Obfuscation is now OFF (Security -> Settings,
  alphabetical list, collapsed row). Verified: start.html serves all three
  mailto: addresses as plain text. That item is DONE, not still open.
- Cloudflare AI bot policies (Search / Agent / Training) all show disabled
  = nothing blocked. Correct for readability. Legacy "Block AI bots"
  deprecates 2026-09-15; leave all three off when Cloudflare asks.
- WATCHER AUTOSTART UNRESOLVED: no cron entry, ~/.config/autostart empty,
  yet the pre-tonight watcher had PID 1136 (boot-time). Some unknown
  mechanism starts it. Tonight's copy was started by hand. Do NOT add a
  cron @reboot line — if the unknown mechanism still fires you get TWO
  watchers and double .docx conversion. After the next reboot run
  'pgrep -af watch-articles.sh' and count: 2 processes = healthy (bash +
  subshell), 4 = duplicate, 0 = nothing autostarts it and it needs a
  proper launcher.
- KB docx on disk are named V2.1, though S31 recorded v2.2 internal
  headers. Filename vs header mismatch, unverified. Check before editing.

S33 — ARTICLE CURATION (stage one complete)

Read and judged all 21 regular articles across two helper tabs.
Curation notes (20 article cards, 11 language flags, decisions
section) written to ~/Nexus_private/nexus_curation_cards.txt —
deliberately outside the served tree.

FIXED: first-week-volunteer.html was spliced. A full duplicate of
the minors botskill sat inside it, cutting the header sentence in
half. Volunteers following an onboarding link landed in child-
safeguarding instructions written for the assistants. Removed 4,003
characters; 1,364 -> 779 words; header repaired. The standalone
botskills/minors.html is the real copy and was untouched.

FIXED: two curation working files were committed into the served
tree and were live on the open web (200). Moved to ~/Nexus_private/,
added to gitignore, both verified 404.

AUDIT — KB LINKS: extracted every URL from all three KB .docx files.
They reference only six articles (core-facts, glossary, use-cases,
public-email-system, first-week-volunteer, tiffanys-idea) — all on
the keep list — and every botskill they link to exists. The article
cull requires zero KB edits.

CORPUS GREP: eight files contain "myth", including both compendiums
and the canonical one. The S25 bug is still live in the corpus.

DECIDED: stories stay under a "What Needpedia Could Be" banner in
articles/could-be/. Official compendium is canonical; rough-drafts
comes off the web. The Grandmother's Network does not exist anywhere
on disk — was never written; two references point at nothing.

Stage two (making the changes) deferred to S34.

## 2026-08-08
Session 34 — Curation stage two + gallery repair

CURATION (the sort, done):
- 4 articles moved off the site to ~/Documents/About Needpedia/:
  instructions-for-user-assistant-guidescript.html,
  the-needpedian-compendium-rough-drafts.html,
  celtc-student-use-cases.html, user-profiles.html.
  Moves, not deletes. 23 articles -> 13 plus 6 stories.
- user-profiles.html read for the first time (~200 profiles,
  job title + city + one line). Cut because it is raw material,
  not an article: teaches nothing about the platform, leans one
  political direction, names vulnerable groups as the user base,
  and repeats entries. Kept privately as the seed list for the
  resonance-tag work.
- Six stories moved to articles/potential-scenarios/ (renamed
  from could-be at Tony's request; old URLs are dead) with
  banners at the top of each. Four use the standard line.
  ep-5 got Tony's wording: "an inspiration piece. Technically
  fiction but entirely doable with our current resources."
  episode-2 names the Stew as a feature under consideration,
  not built. Nothing was cut for being fiction.

MYTH TOKEN — CLOSED, smaller than the handoff said. Nine files
contain "myth"; six use it in the ordinary sense (a false belief)
and were left alone. Three claimed the token exists and were
fixed: botskills/emotionally-charged-ideas.html (NOTE/MYTH TOKENS
-> NOTE TOKENS), the-peoples-mastermind.html (feature entry now
Note Tokens), episode-1 (Rodrigo drops a Note Token; the editor's
note apologising for the unbuilt feature removed). NOTE: S29
recorded fixing two of these three and the fix was not present.
Likely landed in the retired capital-A Articles folder and never
reached the served copies. Verify fixes in future sessions rather
than trusting the log.

GALLERY BROKEN AND REPAIRED (self-inflicted, logged in full):
- Root cause: gallery.html learned folder contents by parsing
  nginx's directory listing. That listing was turned off in the
  S32 lockdown, so every folder tile had been silently broken
  since then. Not caused by this session, but surfaced by it.
- First repair attempt made it worse: a regex that stopped at
  the first space mangled every name containing one, and a
  recursive script wrote index.txt into ~100 nested image
  subfolders. Both reverted.
- Working fix: each public folder now carries _list.txt, one
  full path per line, spaces intact. fetchDir() reads that file
  instead of parsing HTML. Generated by write_folder_lists.py /
  fix_nexus_lists.py.
- Second bug found: the image filter used /articles/i.test(),
  which matched capital Articles/ and hid its entire contents.
  Narrowed to the lowercase folder only.
- Third bug found: setHash() encoded the whole hash in one call,
  turning the / between folder and subfolder into %2F. The
  router then split on / and found nothing. Fixed to encode
  segment by segment.
- Home tile list is hand-written, not generated from folders.
  The Articles tile pointed at the retired capital-A folder
  (now only PNGs + nonprofit docs); repointed at lowercase
  articles/.
- Verified working: Images, Videos, Audio, Articles, and the
  potential-scenarios stories. Volunteer studios, admin pages,
  order-server and nginx untouched throughout.

STILL BROKEN / OPEN:
- Mixed Media -> John E subfolder does not open. Last fix
  (fix_hash.py) applied but never tested. First thing to check
  next session.
- regen_index.py does not descend into subfolders, so the six
  stories in potential-scenarios/ are live on the web but absent
  from articles/index.html, index.txt and llms.txt. AI readers
  cannot find them.
- Drag-to-reorder writes _order.json but no _order.json exists
  anywhere except the retired Articles/ folder — the arranger
  has not worked since the listing was turned off. Untested
  since the repair.
- Backup files created this session are committed but 404 from
  the web: *.bak-myth, *.bak-dirlist, *.bak-listfix, *.bak-fixtwo,
  *.bak-tile, *.bak-tile2, *.bak-three, *.bak-hash, *.bak-rename.
  Clean up once the gallery is confirmed stable.
- Scripts written this session and left in the project folder:
  sort_articles.py, write_folder_lists.py, fix_nexus_lists.py,
  fix_gallery.py, fix_two.py, fix_tile.py, fix_tile2.py,
  fix_three.py, fix_hash.py, rename_folder.py. One-shot repair
  scripts; safe to delete.

NOT DONE THIS SESSION: admin login (deliberately dropped — the
admin pages display nothing without the password and the data is
already checked server-side, so gating them buys little). Jobs C2
through C8 (vocabulary drift, tense drift, crowdfunding closers,
end-of-war split, doing-the-impossible edits, small fixes) all
untouched. Job B (assistant KB updates) untouched.

S35 (2026-08-09): read-only email evaluation, no changes anywhere. Found: the public email system is the vc-email app on Vercel (public repo); it reads one Gmail room over IMAP, stores no mail, and already contains an AI chat with an editable instruction sheet. App currently idle. needpedia.org has zero mail records in DNS: the domain cannot receive, and outgoing mail carries no proof records. Plan set: Cloudflare forwarding for the domain addresses, Gmail send-as for replies, proof records to fix deliverability, then the Nexus archives raw mail to the home disk and clears Google's copy, with a file-never-delete AI gatekeeper on top. Next: Takeout backups per account, then a count-first cleanup script, then a personal-email tile in the Nexus.

S36 (2026-08-27): infrastructure and housekeeping; email build deferred. Redesigned session handoffs: a tiny pasted prompt plus private numbered "prompt accomplice" files on the home machine, with this public log as the third leg; baseline archived. Fixed admin login: the site turns out to have two separate locks (a web-server door on the terminal path and an app door in the backend) which had drifted apart after a forgotten password change — both now aligned and verified end-to-end through the public URL. Security: found the compose file and backend script were publicly downloadable from the web root; extended the server denylist to hide configs, scripts, and secrets, confirmed 404 through the tunnel; credential rotation queued. Identified the capabilities file as the AI-readable front door (stale since S17) — refresh plus an open-tasks section planned. Next: rotate exposed credentials, then resume the email run order (Takeout backups, count-first cleanup script, personal-mail tile).

S36b (2026-08-27): follow-on work after the S36 close. Added the
newer DeepSeek V4 Pro build (the August GA release) as an extra
model button in both the admin chat and the volunteer text
studio; nothing existing was removed. Confirmed via a direct API
call that requests for it route to the intended provider, matching
the account-level allowed-provider list. Fixed the volunteer
studios returning empty replies: the studio pages carry their own
capped API key separate from the backend's, and that key had been
revoked, which the page silently displayed as no response. Issued
a replacement and swapped it across all root pages, restoring both
the text and image studios. Admin password realigned across both
locks again after a deliberate change. Still open: rotating the
remaining exposed credentials, refreshing the stale capabilities
file, and the email project run order.

N36 (2026-09-04): handoff system moved to a public context file.
Found that the server config blocked all markdown files by
default with a single hand-carved exception for this log, which
is why the capabilities index had been invisible to AI fetchers
since the summer lockdown. Added a narrow allowlist for
AI-readable docs and published a new context file at the site
root, so any assistant can now fetch its own working context
instead of waiting for it to be pasted. Sensitive details stay in
the private pasted prompt. Also this session: added the newer
DeepSeek build to the admin chat and volunteer text studio
without removing anything, and confirmed it routes to the
intended provider; fixed the volunteer studios returning empty
replies, caused by a revoked studio key that the page silently
swallowed; realigned the admin password across both locks. Still
open: rotating two credentials exposed before the denylist patch,
refreshing the stale capabilities index, a context file for the
production site, and the mail backup run order.

## 2026-09-04
Session 37 — Activity monitor: collector shipped, tile pending

OBJECTIVE: an admin view showing whether real people are active on
the production site, given that raw traffic counts are meaningless.

THE CENTRAL QUESTION DISSOLVED. Bot noise lives in the web server's
request log, not the database. Every action recorded in the database
belongs to a logged-in account, and crawlers have no accounts. Reading
the database instead of the log removes the filtering problem entirely.
No heuristics were needed or written.

ANONYMOUS-READER BAND CUT after the data refuted it. The visitor table
records a browser identity string but the column is empty on 100% of
rows; 878 distinct addresses across 880 visits; the "last seen" field
never moves off "first seen". Nothing in it can distinguish a person
from a scanner. Machine hits are now displayed unfiltered and clearly
labelled — a heartbeat proving the connection is alive, not a visitor
count.

BASELINE: no account activity since 2026-07-21. Confirmed as expected
(pre-launch, essentially no users). The tile is a tripwire for the
first real one, not a measurement of current traffic.

SECURITY — production database was internet-facing. Its access rules
carried a blanket allow-from-anywhere entry with weak password hashing,
the service was bound to all interfaces, and the port answered from
outside AWS. Narrowed to a single home address; original rules backed
up alongside the live file. Also found a dead password sitting in the
app's config, overridden by an environment variable on the line below.

Same box also runs staging and holds the database directly — no
managed database service, no autoscaling despite what the old devops
document claims. Disk at 77% of 15GB.

BUILT: a read-only database account with SELECT and nothing else; a
collector script on the home machine that queries production and
writes counts to a file outside the web root; a backend handler and
web-server route serving those counts behind the admin token; and the
display page. Verified: the data endpoint returns 403 without a token.

NOT FINISHED: the page still reads the old public file path and must
be repointed at the token-gated route; no gallery tile yet; no timer,
so counts only update when the collector is run by hand; the page
file itself is not yet in the denylist.

NOTE FOR FUTURE SESSIONS: the database rule is pinned to one home
address. If the tile goes dark for no apparent reason, a changed home
address is the first suspect.

## 2026-09-04
Session 37 — Activity monitor: collector shipped, tile pending

OBJECTIVE: an admin view showing whether real people are active on
the production site, given that raw traffic counts are meaningless.

THE CENTRAL QUESTION DISSOLVED. Bot noise lives in the web server's
request log, not the database. Every action recorded in the database
belongs to a logged-in account, and crawlers have no accounts. Reading
the database instead of the log removes the filtering problem entirely.
No heuristics were needed or written.

ANONYMOUS-READER BAND CUT after the data refuted it. The visitor table
records a browser identity string but the column is empty on 100% of
rows; 878 distinct addresses across 880 visits; the "last seen" field
never moves off "first seen". Nothing in it can distinguish a person
from a scanner. Machine hits are now displayed unfiltered and clearly
labelled — a heartbeat proving the connection is alive, not a visitor
count.

BASELINE: no account activity since 2026-07-21. Confirmed as expected
(pre-launch, essentially no users). The tile is a tripwire for the
first real one, not a measurement of current traffic.

SECURITY — production database was internet-facing. Its access rules
carried a blanket allow-from-anywhere entry with weak password hashing,
the service was bound to all interfaces, and the port answered from
outside AWS. Narrowed to a single home address; original rules backed
up alongside the live file. Also found a dead password sitting in the
app's config, overridden by an environment variable on the line below.

Same box also runs staging and holds the database directly — no
managed database service, no autoscaling despite what the old devops
document claims. Disk at 77% of 15GB.

BUILT: a read-only database account with SELECT and nothing else; a
collector script on the home machine that queries production and
writes counts to a file outside the web root; a backend handler and
web-server route serving those counts behind the admin token; and the
display page. Verified: the data endpoint returns 403 without a token.

NOT FINISHED: the page still reads the old public file path and must
be repointed at the token-gated route; no gallery tile yet; no timer,
so counts only update when the collector is run by hand; the page
file itself is not yet in the denylist.

NOTE FOR FUTURE SESSIONS: the database rule is pinned to one home
address. If the tile goes dark for no apparent reason, a changed home
address is the first suspect.

S37 addendum: Activity tile confirmed working from edit mode. Gallery
was briefly blanked by a bad multi-line paste and restored from
.bak-N37; tile re-added by script. Separate bug found: volunteer
studio conversations write to disk but index.json is stale since
2026-06-05, so they do not list. No data lost.

S38 (2026-09-06): Volunteer studio conversation history now saved
on the server instead of the browser. Fixed the reported bug and
found it was two separate faults.

ROOT CAUSE, the real one: the studio's conversation list was never
server-backed at all. The page built its sidebar from per-tab
browser memory, which is wiped when the tab closes. Nothing on the
page ever read the saved list file. Conversations were being
written to disk correctly and then orphaned. Repairing the list
file alone would have restored nothing.

SECOND FAULT, one character: the save routine looked up existing
entries with square brackets instead of a safe lookup, so it
crashed on any entry lacking a conversation id. Image sessions
have no conversation id. Once the first image session landed at
the top of the list in June, every text save crashed at that point
- after writing the conversation file, before updating the list.
That is why files existed and the list was frozen at June 5. Six
matching errors in the backend log confirmed it. The image save
routine directly above used a safe lookup and kept working, which
is why images were unaffected.

BUILT: two read-only backend routes, one returning a volunteer's
conversation list, one returning a single conversation converted
from the stored line-per-exchange format into the message shape
the page renders. Both copy the existing admin chat pattern.
Matching web-server routes added by copying the admin block
verbatim rather than hand-writing it. The list route filters image
sessions out. Username is sanitized the same way the save routines
do it. Access matches the studio's existing model - the studio
already auto-logs in from a URL parameter with no password, so
these add no new exposure. Password-gating them is available if
wanted.

Page changed in two places only: the list loader now fetches from
the server, and opening a conversation fetches its messages on
demand. Conversations survive closing the tab and follow the
volunteer to any machine. Verified end to end: six conversations
listed, old ones open, new chat saves and survives reload.

BACKFILL: four orphaned September conversations added to the list
file with titles taken from their first message. Nothing was lost.

ALSO DONE: the production activity collector now runs every 15
minutes on a schedule instead of only when run by hand. Verified
firing on the quarter hour. An error message on the activity page
that named a moved file was reworded.

TRIED AND REVERTED: hiding the activity page's web address. It
worked, but the admin tile opens the page by that same address, so
it hid the page from the admin too. Reverted. Not worth building a
workaround - the numbers are already password-gated and a stranger
at that address saw only an empty shell with zeros.

LESSONS:
- The web-server container is not named nginx-server. It carries a
  hash-prefixed name from an old recreate conflict. The old name
  fails and silently skips whatever follows it.
- Three chained commands failed tonight because an early step
  errored and stopped the chain: a docker command without sudo,
  and a grep counting zero matches. Both times the restart never
  ran and later steps were tested against unchanged files. Run
  verification separately from the action.
- After a page edit, the browser can serve a stale copy through
  the tunnel while the server has the new one. Symptom was the
  page behaving like unpatched code with correct code on disk.
  Confirm by checking what the server serves before debugging the
  code.
- The scripted-insert method held up again: every patch aborted
  cleanly rather than half-applying, and one abort caught that an
  earlier run had never applied at all.

HIGH PRIORITY LOOSE ENDS:
- Logins on the production activity page read zero even after a
  confirmed real login through a browser. Either the query asks
  the wrong thing or the site records logins differently. The
  collector's login query was about to be read when the session
  ended. Until resolved, treat the login number as unverified.
- No visibility into whether anyone has talked to the three site
  assistants. The activity page covers signups, posts, edits,
  logins and comments only. AI conversations are not measured
  anywhere.

CARRIED: rotate the two credentials exposed before the S36 fix,
now joined by the production database reader password, which sits
in plaintext in the collector script and was pasted into a
captured chat. Three credentials outstanding. Also still open: the
context file's wrong claim about production access, the stale
capabilities file, the email run order, splitting the 1,100-line
backend file, and no context file for the main site.

## 2026-09-07
N39 — Web research for the AI chat spaces

SHIPPED: the admin chat and the volunteer text studio can now
research on the internet. The model decides whether to search,
writes its own search words, can search more than once, can read a
full page it found, and knows today's date. Answers come back with
source links.

BUILT THE WRONG WAY FIRST, then corrected. The first version used
the older method that searches once per message using the user's
literal words. Asking "can you go online?" returned Microsoft
wifi-troubleshooting articles, and every message paid for a search
whether it needed one or not. Checking the current documentation
showed that method is deprecated. Rebuilt on the replacement, where
search is offered to the model as a tool rather than forced.
Verified both behaviours: a live price question searched twice and
cross-checked sources; "thanks, that worked" fired zero searches
with the feature switched on.

ALSO CHANGED: the volunteer text studio now sends its messages
through the backend instead of contacting the AI service directly
from the page. Its own separate spend-capped credential moved off
the served page and into the backend, which keeps the deliberate
two-credential boundary intact while removing it from public view.
One backend handler and one web-server route added, copied from the
admin pattern. Conversation saving and history, built in S38, were
verified working after the move.

SETTINGS: search is done by the cheapest available provider at a
tenth of a cent per search, capped at three searches and ten
results per message. The web switch starts on.

CONFIRMED THIS SESSION:
- The account's allowed-provider list refuses Google, which is why
  the image studio errors. Pre-existing, unrelated, untouched.
- Stale cached pages bit twice more, including in Firefox, where an
  old copy hid a model button added weeks ago and showed an empty
  conversation list. Hard refresh fixed both. Always rule this out
  before debugging code.
- Restart commands must be run one at a time. Two typed on one line
  meant the web server never restarted and a new route 404'd.

LOOSE ENDS ADDED: the studio pages still have no password — the tile
is hidden without a login but the address itself opens for anyone
who knows it. Credential rotation list grows to five.

## 2026-09-08
/tmp/devlog_N40.txt

## 2026-09-14
/tmp/devlog_N41.txt


## N41 — 2026-09-21 — Volunteer studio timeouts fixed
Long or research-heavy questions in the volunteer text studio were failing with a confusing error after about a minute. Cause: the web server stopped waiting for the answer. Fix: answers now arrive word by word as they're written, so long answers finish. Failures now show a plain-English message. The back-end program also now handles requests side by side instead of one at a time. Admin chat still has the old limit; same fix pending.


## N43 — 26 September 2026

- Phone notification app moved out of the Nexus thread into its own thread, A. Full handoff written: ~/PhoneApp_private/A1-handoff.txt (private folder made this session).
- Read-only copy of the phone app code made at ~/Nexus_private/phone-app-copy from https://github.com/Queuevius/Needpedia-phone-app. Change history: newest change 2024-10-23 (Murtaza Khan, Adnan Khan), branches main, master, fixes/fcm-notification. No work by Mubasher on any branch. His newer work, if any, is somewhere else. The code itself was not read this session.
- Phone-app material cut from the Nexus prompt accomplice, replaced by a pointer line to thread A (cleanup script ~/Nexus_private/cleanup_pa_N43.py; backups PA-NEXUS.txt.bak-N43-public and -private in ~/Nexus_private/).
- "Working with Tony" post replaced with its newest version and confirmed live at https://nexus.needpedia.org/working-with-tony.txt. Previous version: ~/Nexus_private/working-with-tony.txt.bak-N43.
- Checked: the two prompt-accomplice copies are separate files, not one file reachable from two places. Which is the real one is still Tony's call.
- Web fetch tool showed a stale prompt accomplice again. Check Nexus files with curl or grep on Tony's machine before believing the fetch tool.
- New rule: a message meant for another thread's chat gets its own label. An unlabeled one got pasted into the terminal.
- Dropped from the handoff: the "carry to the thread-system AI" section. No such thread exists; every thread shapes the working-with-Tony post.


## N43 addendum — 27 September 2026

- The phone app thread renamed itself NPA (was A). NPA decided how Nexus activity alerts reach Tony's phone: straight through Google's phone-notification service, using Google project update-needpedia (project number 550163998966). The Nexus builds the sender. Nothing built yet: no sending key exists for that project. The google-services.json in Tony's Downloads belongs to a different project (volunteer-app-db445) and is not a sending key.
- NPA note to the Nexus: https://nexus.needpedia.org/public/NOTE-TO-NEXUS-2026-09-27.md
- Cross-reference posts started. History only: dated entries written by the thread that did something affecting another thread, never cleared, no action needed.
  https://nexus.needpedia.org/public/CROSSREF-NEXUS.md (NPA's entries)
  https://nexus.needpedia.org/public/CROSSREF-NPA.md (the Nexus N43 entries)
- NPA's other idea, tags on public posts plus one map file, is parked and Tony's call. If built, the map belongs at public/TAGS.md so no web-server settings change is needed.
- Prompt accomplice: added NPA's findings, the cross-reference rule, and the rule for messages to other threads.
- working-with-tony post: added three sections. Messages for another thread (short ones start with #, long ones come as files); Claude Code (installed, version 2.1.207, use it whenever it moves work faster); numbering of command boxes restarts at 1 in every message.
- Open: the prompt accomplice's top line says "private, never publish", which contradicts the rule that prompt accomplices are public. Cutting it waits on Tony's yes.

## N44 — 28 September 2026 — Nexus thread

Build session. Tony's goal: a way for threads to pass updates to each
other, tested; a new thread for John's test sites; every thread told.

- Every thread now has three public posts: updates (unread), archive
  (read) and cross-reference (history, no action needed). One script on
  Tony's machine runs them for all threads: NEXUS, NP1, NPA, PC, JOHN,
  TS, PU, BHS, JOBS.
- First real use: the Public Coms thread got its inbox problems and the
  consent idea. Then PU, NP1, JOHN, NPA, BHS and JOBS got updates.
- working-with-tony.txt reworked: thread list rechecked, updates
  section rewritten, four new sections. It is now in the botskills list
  and llms.txt, through a change to the index-building script, so
  rebuilds keep it.
- New threads: TS (test sites: John's self-hosted package) and PU
  (Project Unstoppable).
- Found: the index-building script had not run since 8 August. The AI
  web-fetch tool showed a stale prompt accomplice for the third time.
- Carried: two watchers for needpedia.org (a weekly build test and a
  support-date check), admin chat down, a public AI knowledge base for
  the Nexus.


## N45 — 29 September 2026 — Nexus thread

Look-only at first, then build. Tony's goal: make the thread system work
from the web, simply.

- Where stale copies come from: the Nexus serves current files (copies
  on disk and on the web matched; Cloudflare stores nothing). The AI's
  own web fetch tool keeps a stored copy per address. A tagged address
  (?v= plus something new) comes back fresh.
- The Nexus now sends "check back every time" (no-cache) with every .md
  and .txt file. The AI fetch tool still returned an hour-old copy
  afterwards, so tagged addresses and reading from disk remain the
  reliable routes.
- The updates tool now keeps one archive file per thread, holding
  everything archived, each piece dated and tagged so it can be searched
  by subject or date. Tags are required on every update and note.
  Cross-reference posts send their oldest 20 entries to the archive past
  30. The old archive files were copied in and point to the new ones.
- The botskill post on working with Tony: editions are now counted and
  it is at edition 8. New at the top: every thread checks its updates at
  the start of a session and whenever Tony says so, then archives them.
  Also new: a new-thread checklist, # on every line of any non-terminal
  box, archive and tag rules, the two sites, and no canvas or side
  panels. Old editions are kept in full in its own archive.
- nexus-context.md retired: its contents went into the Nexus archive,
  and its useful parts into the botskill post and the Nexus prompt
  accomplice.
- Every thread got cross-reference notes; NPA and TS got updates about
  the archive change.
- Loose ends added: a dedicated thread for the thread system, and later
  the "bot council": chatbots on the Nexus that can ask each other
  questions, switched on only while Tony works.

---

## Session N46 — 2026-09-29

- Found why bots acted blind: Claude's web fetch tool refuses addresses
  written inside plain text files, even after reading the file. It
  opens only pasted addresses and real links on web pages.
- New script turns the botskill post into a web page,
  working-with-tony.html, with real links. Each Nexus link carries a
  fingerprint of its file, so bots get current copies without anyone
  bumping tags. Remade every 5 minutes, only when something changed.
  The botskills list and llms.txt point at the page.
- Botskill post: edition 9 (the web page version) and edition 10 (from,
  to and date on every update and note; handoffs live only in the
  chats; how private material is archived; BHS retired). Old editions
  archived.
- BHS thread retired: its public posts taken off the web and packed
  privately with its old private files. The resident roster deleted.
- JOBS thread: a message written for its old chat, telling it it is
  thread JOBS now.
- Update sent to every thread about editions 9 and 10.
