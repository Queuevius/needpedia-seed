# ARCHIVE - NEXUS

Public. Nothing sensitive in here, ever.

Everything archived for NEXUS, oldest first: read updates, older
cross-reference entries, old editions of public documents, and
reference entries pointing at private files (path, date and tags only,
never their contents). Nothing here needs action.

Every piece starts with one line: the date it was archived, where it
came from, and its tags. Search it on Tony's computer, for example:
grep -n "tags:.*nginx" ~/Needpedia_Nexus/public/ARCHIVE-NEXUS.md
grep -n "archived 2026-09-2" ~/Needpedia_Nexus/public/ARCHIVE-NEXUS.md

Made 2026-09-29.

----- archived 2026-09-29 | from PA | file PA-NEXUS.txt | tags: prompt-accomplice, nexus, before-n45 -----
== PROMPT ACCOMPLICE — NEXUS THREAD — 2026-09-21 ==
private, never publish. Read only from ~/Nexus_private/.
The NP-1 thread has its own folder and its own accomplice.
Do not read or write across threads.

MACHINE FACTS
- Production server: 18.223.241.10, AWS EC2. Live site, practice
  site and database all on one box. Disk 77% of 15GB in September.
- Tony's desktop key (~/.ssh/id_ed25519, Oct 2025) is REFUSED by
  that server as both deploy and ubuntu. Do not retry it. Way in:
  AWS console > EC2 > Instances > tick instance > Connect >
  EC2 Instance Connect > Connect. Browser terminal, no key.
- Collector: ~/Nexus_private/activity_monitor.sh
  Output: ~/Nexus_private/data/activity.json
  Runs every 5 minutes. Old schedule saved at ~/crontab.bak-N40.
  Backup: activity_monitor.sh.bak-N40
- Activity page: ~/Needpedia_Nexus/activity-monitor.html
  Backups: .bak-N40 (before rows), .bak-N40b (before rewrite)
- Reading the live database from the desktop needs no login prompt.
  Pattern used throughout N40:
  source <(grep -E '^(DB_HOST|DB_USER|DB_NAME|PGPASSWORD|export PG)'
  ~/Nexus_private/activity_monitor.sh) && psql -h "$DB_HOST"
  -U "$DB_USER" -d "$DB_NAME" -Atc "YOUR QUESTION"
- Claude Code is installed on Tony's machine and unused. Good fit
  for reading the repo and editing Nexus files directly instead of
  through paste boxes. Not a fit for design conversations.

WHAT THE LIVE DATABASE HOLDS
- chat_threads and chat_messages: every assistant conversation,
  full question text, since Nov 2025. Confirmed on the live site.
- Conversation labels are "Needpedia Assistant", "Needpedia
  Greeter", "VC Email Assistant" - NOT Lotte, Florence, Adele.
  Mapping unconfirmed; asked in the lead-dev email.
- login_attempts holds failures only, by design. Never try to count
  successful logins from the database. Independently re-verified by
  NP-1 against commit 26563af.
- Reader account has SELECT only. Its password sits in plaintext in
  the collector script and is one of the five overdue rotations.

THE DEPLOY LANDMINE (unresolved, blocking)
config/deploy.rb sets deploy_to to /home/deploy/needpedia_staging
with the production line commented out; production.rb and
staging.rb both name 18.223.241.10. A production deploy could land
in the practice folder. Two read-only checks written and waiting
for the AWS browser terminal:
  sudo grep -rnE "server_name|root |passenger_app_env"
    /etc/nginx/sites-enabled/ /etc/nginx/conf.d/ 2>/dev/null
  ls -la /home/deploy/ && for d in /home/deploy/*/current; do
    echo "== $d"; cat "$d/REVISION" 2>/dev/null; done
REVISION gives the deployed code version, comparable against GitHub
to list every change a deploy would bring. Email sent to the lead
developer 2026-09-08. No reply as of 2026-09-14. He is in Pakistan
and takes days; batch anything else he is needed for.

PHONE APP: moved to thread A. Handoff at ~/PhoneApp_private/A1-handoff.txt.

NEXT BUILD (Tony's stated want)
Phone alert whenever something happens that is NOT background
machine traffic, with a link to the activity page. The collector
already holds every number every five minutes, so it can compare
against the last run and send when a non-strange signal moves.
Two delivery routes, undecided, ASK BEFORE CHOOSING:
  - Through Google to the existing Needpedia app. Needs the key
    file and the phone's registered address.
  - Through ntfy, a free open service with its own app. About
    twenty minutes, no Google. Not the Needpedia app.

WORK HANDED OVER BY NP-1 (2026-09-14 brief)
- Publish Capabilities 1.1 and Repo Map 1.0 on the Nexus: a home,
  a tile, entries in the articles index and llms.txt.
- Fix three glossary errors at
  nexus.needpedia.org/articles/glossary.html
    IDEA POST says "one or more problem posts" - it is exactly one.
    OBJECTIVE says followers are notified on completion - no
      completion state exists anywhere, so it cannot fire.
    /IMPACT is written singular - the working path is /impacts.
- Count mismatch: llms.txt claims 13 articles, the articles index
  lists 4. Botskills count of 13 checks out. Index stamped
  2026-07-03, llms.txt says rebuilt 2026-08-08. FIND OUT WHY BEFORE
  CHANGING THE DIGIT - if a script generates these, the mismatch
  means the script is stale or broken and correcting the number
  hides it.
- Build the bug-reporter URL on the Nexus. Report rides in the
  part of the address after the question mark so an AI with no
  email, account or form can file by fetching a link, and the same
  link works when a person clicks it. Rate limit from day one.
- Point the five-minute collector at that URL's hit count once it
  exists.
- NP-1 wants back: how the Nexus file layout works and where a new
  article goes; whether llms.txt and the articles index are written
  by hand or generated; which botskills overlap with capabilities
  (taxonomy navigation, dev onboarding); anything in Tony's "about
  Needpedia" folder describing what people DO with features.

STILL OPEN FROM N40
- AI disclosure text: the site already passes a first-visit flag to
  the assistant, and each assistant's instruction sheet is editable
  at master_admin/ai_prompts (versioned; a new version deactivates
  the old). Tony is writing the wording himself.
- The big "Last Action" line links to the recent posts list, not
  the specific item, because the collector records what happened
  and not which record. Collecting the id would fix it.
- Sparklines - one tiny graph per row beside its numbers - proposed
  as a better fit than one shared graph. Not started.
- Strict overlap-to-white in the graph (rather than the additive
  light effect shipped) is real overlap math, own session.

ADDED 2026-09-21 — FOR THE MISSION: UPDATE NEEDPEDIA'S AI

REFERENCE DOCUMENTS (what the AIs should agree with)
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Capabilities.md
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Repo-Map.md
  https://nexus.needpedia.org/articles/glossary.html
  https://nexus.needpedia.org/articles/core-facts.html
  https://nexus.needpedia.org/botskills/
  https://nexus.needpedia.org/start.html
  https://nexus.needpedia.org/llms.txt
Capabilities wins on what the software does. The glossary wins
on what words mean.

DISAGREEMENTS ALREADY KNOWN — CHECK THESE FIRST
  - Glossary says an idea attaches to "one or more" problems.
    It is exactly one.
  - Glossary says followers are notified when an objective is
    completed. Objectives have no completed state, so this
    cannot happen.
  - Glossary writes /impact. The working address is /impacts.
  - llms.txt says the articles collection holds 13 documents;
    the articles index lists 4. Find out whether a script makes
    these files before changing the number — a stale script is
    a different problem from a typo.
  - The dev onboarding botskill may still say deploys are frozen
    waiting on the lead developer. He has answered and is
    deploying himself; volunteers still never deploy.
    https://nexus.needpedia.org/botskills/dev-onboarding.html
    It and the Repo Map should point at each other rather than
    repeat each other.
  - The site records assistant conversations under the labels
    "Needpedia Assistant", "Needpedia Greeter" and "VC Email
    Assistant", not Florence, Lotte and Adele. Which is which is
    unconfirmed.
  - Project Unstoppable, the server-to-server backup network, is
    NOT in Capabilities. Tony asked the lead developer on
    2026-09-21 whether it was ever built. Until he answers, no
    AI may describe it as existing.
  - Successful logins are not recorded anywhere. Any AI that
    offers to look up someone's login history is wrong.

STARTER QUESTIONS TO PUT TO EACH AI — a starting set, not a
decision. Tony may add or cut.
  - How many kinds of token are there, and what are they?
  - Can an idea be attached to more than one problem?
  - What happens when someone completes an objective?
  - Where do I see someone's impacts?
  - Can I make a task card without a group?
  - How do the time bank and task cards connect?
  - Is there a way to vote on ideas?
  - What is Project Unstoppable?
  - How do I report a bug?
  - Can volunteers deploy code?
Right answers per Capabilities: three tokens (note, question,
debate); exactly one problem; nothing, there is no completed
state; /impacts; no, groups only; they don't, separate systems;
ratings 0-5 plus Lol ARE the voting; not confirmed to exist;
info@needpedia.org; no, never.

OPEN QUESTIONS ABOUT WHERE EACH AI'S KNOWLEDGE LIVES
  - Florence and Lotte: master_admin/ai_prompts on the live
    site. Confirmed.
  - Adele works in the volunteer email app, which is a separate
    project. Whether her instructions also live in that admin
    page, or somewhere in the email app, is not known. Find out
    before editing.
  - The Nexus studios: no shared knowledge exists yet. Designing
    it is part of this mission.

A FIRST-VISIT DISCLOSURE BELONGS IN THIS WORK
The site already tells the assistant when a person has never
talked to it before. Tony wants that first reply to say
conversations are recorded. Tony is writing the wording. Adding
it is one edit per assistant on the admin page.

FROM THE JOHN ONBOARDING THREAD — CODE-PICTURE TOOLS
Free websites that read a public code project and show it as a
picture or a wiki. John tested these in September 2026.
  GitDiagram — works. A clickable box-and-arrow map of the code.
    Helped John; Tony found it useless to a non-programmer. Best
    for developers and for giving an AI context.
    https://gitdiagram.com/Queuevius/Needpedia
  DeepWiki — not set up. Says "Repository Not Indexed", probably
    a one-time switch. Tony: reads like a wiki you'd fact-check
    for a year.
    https://deepwiki.com/Queuevius/Needpedia
  Google Code Wiki — Needpedia not in its catalog. Wait.
    https://codewiki.google
  Gource View — works. Plays the project's whole history as an
    animated growing tree with contributors flying around.
    Fullscreen video mode, title card, music, closing
    leaderboard, phone-shaped video. Looked plainer on John's
    screen than expected, cause unknown.
    https://schlunsen.github.io/gource-view/?repo=Queuevius/Needpedia
  CodeCharta — untested. The project as a 3D city, files as
    buildings. Built for non-coders. Needs one setup step on a
    real computer.
    https://codecharta.com/
Tony's split: code maps are for developers and AI; eye candy is
for pitches, crowdfunding, videos and volunteer morale.

JOHN'S NEXT MILESTONE is being chosen. Likely: finishing the
check of whether Needpedia runs on GitHub's free in-browser
computer, or a read-only look at how posts keep edit history, as
groundwork for letting Adele safely edit and delete task cards.
== ADDED AT N41 CLOSE, 2026-09-21 ==
(N41's handoff was mislabeled from a numbering slip; the session was N41. This file is correctly named for N42.)

N41 DONE — volunteer studio no longer times out on long or research-heavy questions.
- Cause: the web server gave up after ~1 minute waiting for the back-end program (a 504 timeout in its log); the studio then showed a jumbled "not valid JSON" error.
- Fix: answers now arrive word by word as the AI writes them, so the connection never goes quiet long enough to be cut. The studio shows a plain-English message if something fails.
- Also: the back-end program now handles requests side by side instead of one at a time, so one long answer no longer freezes everyone else.
- Backups of the changed files: ~/Nexus_private/*.bak-N41. The two helper scripts that made the changes are also there (patch_server_N41.py, patch_studio_N41.py).

CARRIED:
- Admin chat still has the old ~1-minute limit. Same fix applies; not done yet.
- Studio doors still unlocked (studio pages have no password). Now three sessions old.
- Mission "Update Needpedia's AI" (make Florence, Lotte, Adele and the Nexus volunteer studios say the same true things) was not started at N41. The method and the two open design questions are in the N41 handoff and still stand: ask before fixing; compare against Needpedia Capabilities 1.1 and the glossary; fix at the source; then update each AI's instructions. Design questions: paste the documents in whole vs. a short list of where they live; where that knowledge lives on the Nexus so one edit updates every studio.
- Phone alerts and the bug-report link: designed, waiting on Tony's choices.

WORKING RULES LEARNED AT N41:
- Code edits: never ask Tony to edit by hand. Short changes = one precise terminal command. Long changes = a helper script opened in gedit, saved in ~/Nexus_private/, then run with one short command. Long pasted terminal blocks break his terminal.
- Helper scripts should stop without changing anything if they can't find the exact spot or if the change is already in.
- Backups of any file holding keys go in ~/Nexus_private/, never in the public web folder.
- Claude can reach anything on Tony's computer by giving him commands to run. Ask precise, narrow questions to save tokens.
== SYSTEM CHANGE — 23 September 2026 ==

Prompt accomplices now live at ONE permanent filename per thread.
This thread's accomplice is:
  /home/clearcrow/Nexus_private/PA-NEXUS.txt

The old dated files stay where they are as history. Nothing appends
to them anymore. Do not create a new dated accomplice.
Reference sheets and any document pointing at an accomplice should
point at the permanent filename above, never at a dated one.

Append new rules, decisions and findings to this file AS THEY COME UP
mid-session, not only at the end. If Tony has to say something twice
across sessions, it wasn't captured properly.

== WORKING RULES — added 23 September 2026 ==

- Never give commands that move, rename or delete Tony's existing
  files. Adding new files is fine. Other things already point at
  current locations. If a file's location is needed, give him a
  terminal command to find it rather than assuming.
- Content Tony needs to keep comes as a downloadable file plus the
  command that puts it in place — not as a block of text in chat for
  him to save by hand.
- Put steps in the order he will do them: downloads first, then the
  terminal command that acts on them. Never a command above the thing
  it operates on.
- When a file on his computer is needed, give the terminal command to
  open or copy it so he can paste it back.
- State the exact thing to use every time. Never refer back to an
  earlier value or choice ("the one you picked"). He is following
  steps, not tracking context. When he asks to restart, restart from
  step 1.
- Claude can reach anything on Tony's computer through commands Tony
  runs, including the private folder. Ask precise, narrow questions.

== ADDED 23 September 2026, N41 close ==

ACCOMPLICES ARE PUBLIC. All prompt accomplices live in the public
web folder so any AI can fetch them by address instead of Tony
pasting them. This one is at:
  https://nexus.needpedia.org/PA-NEXUS.txt
Nothing sensitive goes in here. Sensitive items live in the
handoff prompt, in a section marked to stay stable. A thread that
truly needs sensitive material on disk gets its own private
folder, reachable only by Tony running terminal commands.

Two copies of this file currently exist on Tony's computer: the
public one in ~/Needpedia_Nexus/ and the original in
~/Nexus_private/. Until Tony says which is the real one, append
to one and copy it over the other so they stay identical.

SESSION SHAPE. Every session opens with a pasted handoff prompt
and closes with a fresh handoff prompt for the next session. Tony
should be able to open any old session and find the handoff at
the top and the next one at the bottom.

Conversation transcripts are not published. If saved at all, they
are saved privately where only Tony reaches them by running
terminal commands.

FINDINGS FROM N41 — checked against the live site, not assumed:

- The "working with Tony" botskill post does not exist yet. There
  are 13 botskills and none is about how to work with him. No
  thread has written itself in there.
- llms.txt is the file that tells any AI what is on the Nexus and
  where to fetch it. It was last rebuilt 2026-08-08 and lists
  only the front door, articles and botskills. It does not
  mention the accomplices, the devlogs, the context file, or the
  thread system. It is the natural home for the thread index.
- Plain text and .md files are served fine; several were fetched
  directly.
- The Nexus home page cannot be read by an AI, because it is
  assembled by scripts after loading. Give AIs direct file
  addresses, not the home page.
- An AI can only open a web address that has been pasted into the
  conversation or that appeared in something it already fetched.
  It cannot guess an address. So Tony pastes addresses, or they
  get listed in llms.txt.

OPEN QUESTIONS FOR TONY — do not decide these:
  a. Does each thread write its own section into the "working
     with Tony" botskill post, or does one thread write the whole
     post from blocks the others hand to Tony?
  b. Same for llms.txt: one thread owns it, or every thread edits
     its own line?
  c. Which copy of this accomplice is the real one?

CARRIED, NEW: find out where the capture tool and the volunteer
studio save conversations. If either writes into the public web
folder, it contradicts the rule above.

== ADDED AT N42, 24 September 2026 — THE PUBLIC FOLDER ==

WHAT CHANGED
The Nexus now has a public folder for .md files:
  on Tony's computer: ~/Needpedia_Nexus/public/
  on the web:         https://nexus.needpedia.org/public/NAME.md
Any .md file placed directly in that folder can be read by anyone
on the internet, straight away, with no settings change and no
restart. This is the way to publish devlogs, prompt accomplices
and other thread documents from now on.

WHAT STAYS BLOCKED, EVEN INSIDE THE PUBLIC FOLDER
- Any file with "handoff" anywhere in its name (any capitals).
  Handoff prompts carry the sensitive section; a handoff put in
  this folder by mistake still cannot be read.
- Anything in a subfolder of the public folder.
- Every other kind of file: scripts, settings, backups and so on.
Everywhere else on the Nexus, .md files are still blocked unless
named one by one in the settings file (CAPABILITIES.md,
nexus-context.md, needpedia-context.md, DEVLOG.md).

HOW IT WORKS (for the next AI)
The web server's settings file is ~/Needpedia_Nexus/nginx-default.conf.
Rules are checked top to bottom; the first match wins. The public
folder rule sits just above the "# DENYBLOCK" line, so it wins
before the blanket .md block. Old settings saved at
~/Nexus_private/nginx-default.conf.bak-N42. The helper script that
made the change is ~/Nexus_private/patch_nginx_N42.py.
Tested from outside after the restart: a normal .md file in the
folder was served; a file named handoff-test.md was refused (404).

CORRECTION TO AN EARLIER FINDING
N41 wrote "Plain text and .md files are served fine." That was only
true for the four .md files named in the settings file. Every other
.md file on the Nexus was blocked. The public folder fixes this.

AN AI STILL CANNOT FIND THESE FILES ON ITS OWN
An AI can only open an address that was pasted to it or that
appeared in something it already read. Files in the public folder
need to be listed somewhere an AI reads (llms.txt, or a thread's
handoff) to be found. This ties into open question b (who edits
llms.txt).
- N42: DEVLOG-BHS.md now lives in the public folder (https://nexus.needpedia.org/public/DEVLOG-BHS.md). The copies in ~/BHS_private/ and ~/Needpedia_Nexus/ are history. BHS thread told via note.
- N42 check: CAPABILITIES.md, DEVLOG.md and nexus-context.md all serve (200) from outside. setup-b-handoff.md is refused on purpose (handoff name) and stays private unless Tony says otherwise. No other file type is blocked by accident. Claude's web fetch tool showed a stale DEVLOG and a false 404 - verify with curl from Tony's machine before believing it. BHS-1 proposed two additions to working-with-tony.txt (a BROWSER label for the address bar; web addresses on a plain line, never in a copy box). Tony parked them.
- N43: the web fetch tool showed a PA-NEXUS.txt missing the whole N42 section (stale copy again). Read this file with sed or cat on Tony machine instead.
- N43 (26 Sep 2026): working-with-tony.txt replaced with the thread-system version (download dated 26 Sep 19:34). Previous version saved at ~/Nexus_private/working-with-tony.txt.bak-N43.
- N43 rule: messages meant for another thread get their own label too, e.g. FOR THE THREAD-SYSTEM CHAT (not the terminal). An unlabeled message box got pasted into the terminal at N43.
- DECIDED at A2 by Tony: Nexus activity alerts go straight through Google phone-notification service (Firebase Cloud Messaging) using Google project update-needpedia (project number 550163998966), confirmed in an account Tony controls. No new address on needpedia.org, no lead-developer deploy. ntfy route not chosen. Still needed: a sending key (service-account key) from that Google project, and Tony phone registration code from the devices table on the live database. Thread A owns the app side; the Nexus builds the sender.
- FROM NPA NOTE 2026-09-27 (https://nexus.needpedia.org/public/NOTE-TO-NEXUS-2026-09-27.md): the phone app thread is named NPA, not A. No sending key exists yet for Google project update-needpedia; the google-services.json in Downloads is a different project (volunteer-app-db445) and is not a sending key. Phone registration codes are in the devices table of needpedia_production (live and practice sites have separate databases). Four accounts have master_admin. The site phone alerts are counts only, no post name or link. NPA asks the Nexus view on tags plus a map file, and on per-thread cross-reference posts.
- RULE 2026-09-27 CROSSREF: every thread has a public cross-reference post at ~/Needpedia_Nexus/public/CROSSREF-THREADNAME.md (this thread: CROSSREF-NEXUS.md, web address https://nexus.needpedia.org/public/CROSSREF-NEXUS.md). History only: dated entries, written by the thread that did something affecting another thread, never cleared, no action needed. Anything needing a response goes in that thread updates post instead. At each session close, add entries to the cross-reference post of every thread this session affected.
- RULE 2026-09-27 THREAD MESSAGES (Tony chose both): a short message for another thread chat goes in a box labeled for that chat, and every line starts with # so that pasting it into the terminal by mistake does nothing. A long message comes as a downloadable file instead, plus a command that opens it in gedit for copying. Reason: at N43 labeled message boxes got pasted into the terminal twice.

== ADDED AT N44, 28 September 2026, PART 1 ==

LOOSE ENDS ADDED AT N44
- Two watchers wanted for needpedia.org. Why: the project's Docker
  build broke when Debian 11 lost support on 31 Aug 2026, and nobody
  noticed for about a month.
    1. A weekly build test. GitHub's own computers build Needpedia
       from scratch once a week and record pass or fail. Two catches:
       GitHub emails a failure only to whoever last edited the job's
       file (if John sets it up, John gets the email, not Tony), and
       GitHub switches these timed jobs off after 60 days with no
       activity in the project. Something else should check it is
       still running.
    2. A support-date check. Once a month, compare the project's
       pinned versions (Debian 11, Ruby 2.7.8, Node 12, PostgreSQL 13,
       Rails 6.0) against the public list at endoflife.date and warn
       before support ends. This would have warned in June.
  Nexus side (carried from N44, for a later session): the five-minute
  collector reads the weekly build result and notices if the build
  test stopped running. The result shows on the activity page and,
  once the phone sender is built, goes to Tony's phone.
- Admin chat is down (Tony, 28 Sep 2026). Not checked yet. This is
  separate from the old one-minute time limit.
- Tony wants a public AI knowledge base on the Nexus: pages any AI can
  be pointed at so it starts out knowing Needpedia instead of blank.
  The volunteer studios are the first users. Same job as the mission
  "Update Needpedia's AI". Open design question: whole documents, or a
  short list of where they live. Research the John thread cited says
  short, human-written pointers work better for AI tools.

DECISIONS AT N44
- Every thread gets three public posts in ~/Needpedia_Nexus/public/:
  UPDATES-NAME.md (unread news and requests), UPDATES-NAME-ARCHIVE.md
  (already read) and CROSSREF-NAME.md (history, no action needed).
  Names: NEXUS, NP1, PC, JOHN, BHS, JOBS, TS. NPA already had its own.
- One shared script runs these posts for every thread:
  ~/Threads_private/threads.py
  Jobs: setup, show, update, note, clear. Each is one short command.
  NPA's own clearing script (~/PhoneApp_private/archive-updates-NPA.sh)
  stays as it is; both use the same marker line, so either works on
  NPA's posts.
- Job search gets a prompt accomplice. Open for that thread: its list
  of jobs tried may grow very large, so where that list lives is its
  own question.
- The thread posts are referenced from the working-with-tony post, and
  listed anywhere else they are useful.
- New thread TS (test sites) for John's self-hosted test-site package.
  It is standalone: volunteers show their edits there; after Tony
  approves, they submit the code on GitHub for the lead developer's
  review. Nothing goes to the lead developer until the automatic
  copy-per-push part is built and tested.
- Public inbox consent: Tony's lean is "sender says yes" (first email
  held privately, automatic reply asks permission, yes publishes it,
  never asked again). The Public Coms thread builds it.
- For thread TS to weigh: an AI reviewer for submitted code changes
  (CodeRabbit, free for public projects). Name ideas for it or a
  home-made version: Hopper, Porch, Checkpoint, Second Look,
  Waystation, Bridge.

FINDINGS AT N44
- The web fetch tool showed a stale PA-NEXUS.txt for the third time
  (phone sections still present). On disk, both copies had them cut.
  Always check this file on Tony's machine.
- working-with-tony.txt is online, but only three prompt accomplices
  link to it. llms.txt, the botskills list and the home page do not.
- This thread's handoff pointed at the phone app's handoff as
  A1-handoff.txt. The current one is NPA2-handoff.txt.

== ADDED AT N44, 28 September 2026, PART 2 ==

DONE AT N44 (after part 1)
- The updates system is live. Every thread has three public posts in
  ~/Needpedia_Nexus/public/, made and run by
  ~/Threads_private/threads.py (jobs: setup, show, update, note, clear).
  Threads: NEXUS, NP1, NPA, PC, JOHN, TS, PU, BHS, JOBS.
- Updates sent 28 Sep 2026: PC (inbox problems and the consent idea;
  the first real use), then PU, NP1, JOHN, NPA, BHS and JOBS. All
  confirmed on the web.
- working-with-tony.txt reworked twice (N44, N44b), plus a one-line fix
  (N44c) for the TS prompt accomplice. Thread list rechecked against
  Tony's disk; updates section rewritten around the shared tool; four
  new sections at the end: use the other AIs, finish talking first,
  where the Nexus lives and how things go live, ask for the terminal
  output. Backups in ~/Nexus_private/: working-with-tony.txt.bak-N44,
  .bak-N44b, .bak-N44c.
- The post is now listed in the botskills list and in llms.txt.
  regen_index.py has a short EXTRAS list for documents that live
  outside its folders; add a line there to list another one. Old
  script: ~/Nexus_private/regen_index.py.bak-N44. The lists as they
  were before the rebuild: ~/Nexus_private/indexes-bak-N44.tar.gz.
- New thread TS (test sites): prompt accomplice
  ~/Needpedia_Nexus/PA-TS.txt, first handoff ~/TS_private/TS1-handoff.txt.
- New thread PU (Project Unstoppable), started by Tony in its own chat;
  private folder ~/PU_private/. Its prompt accomplice is its own job.

FINDINGS AT N44 (after part 1)
- llms.txt, articles-index.txt and the articles and botskills lists
  are all written by regen_index.py, run by hand. Nothing had run it
  since 8 Aug 2026. rebuild-index.sh only forwards to it.
  watch-articles.sh runs in the background and reruns it only when a
  Word or LibreOffice document is dropped into articles/. Hand edits
  to any of those lists get wiped by the next run: change the script
  instead.
- The old count mismatch (llms.txt said 13 articles, the list showed 4)
  is gone: the page and the folder both had 13 before the rebuild.
- BHS has three copies of its prompt accomplice; public/PA-BHS.md is
  the newest (26 Sep). The BHS thread was told through its updates
  post.

LOOSE ENDS ADDED (after part 1)
- Once TS is running, update anything on the Nexus that tells
  volunteers how to show their work, including the dev onboarding
  botskill.
- Tony's idea, not decided: Google alerts and news-watching drones for
  his city, the world and key topics, feeding his phone notifications.
- The N44 handoff said web addresses go on a plain line, never in a
  copy box. The working-with-tony post says a box labeled BROWSER. The
  post was followed. Tony has not ruled on it.
- Still unanswered: cut the "private, never publish" line at the top of
  this file? Asked once at N44.

== ADDED AT N44, 28 September 2026, PART 3 ==

DECISIONS (Tony, 28 Sep 2026)
- Devlogs are public unless a thread's own prompt accomplice says
  otherwise. Security is the main concern: nothing in a devlog that
  would help someone get in. Settles the conflict with a 23 Sep
  correction that called devlogs private.
- The working-with-tony post keeps one fixed web address; its edition
  name goes on the first line of its header (now EDITION N44d). Every
  change gets a new edition name, a saved old edition, and a
  cross-reference note to every thread naming the new edition. A
  thread that sees an older edition than its handoff or its
  cross-reference post names has a stale copy and reads it from disk.
- Keep old editions of every document: before replacing or rewriting
  one, save the old edition in the thread's private folder, named for
  the session.

FINDING
- The TS thread's web fetch returned an old copy of the post on 28 Sep,
  though Tony's curl got the new one through the same address. So the
  stale copies come from the AI fetch tool keeping its own old copy,
  not from the Nexus or its front door.

DONE
- Post edition N44d in place; old edition at
  ~/Nexus_private/working-with-tony.txt.bak-N44c2 (the one-line TS
  fix, .bak-N44c, came before it).
- N45 handoff and TS1 handoff replaced with version 2; version 1 of
  each kept as .bak-v1 next to it.

== ADDED AT N44, 28 September 2026, PART 4 ==

FINDING
- The PU chat's AI could not use its public posts: its web copy of
  working-with-tony.txt was stale (no edition line), so PU's own post
  addresses never appeared where its AI could open them, and it fell
  back to asking Tony to print them from disk. The files are online:
  Tony's curl got current copies through the same addresses.
- Not yet known: whether the old copies come from Cloudflare or from the
  AI fetch tool itself. Diagnosis and candidate fixes are in the entry
  sent to UPDATES-NEXUS.md on 28 Sep 2026.

DECISION (Tony, 28 Sep 2026)
- N45's objective: make the thread system work from the web, so a thread
  only needs to be told "check for updates", perhaps with one address.
  Every thread has public material; the setup must make it readable.
- After the fix, PU gets told to check its updates.

----- archived 2026-09-29 | from CONTEXT | file nexus-context.md | tags: nexus-context, retired, architecture, n36-to-n41 -----
# NEXUS CONTEXT — AI working file
# Public on purpose: any AI can fetch this at
# https://nexus.needpedia.org/nexus-context.md
# Private details (accounts, keys, exact paths, passwords) are
# NOT here — they ride in Tony's pasted handoff prompt.
# Last updated: N36 close, 2026-09-04

## HOW SESSIONS WORK
Tony pastes a short handoff prompt naming the session type and
objective. That prompt points here for stable context. Sessions
are numbered N##; each one produces an updated handoff, an
updated copy of this file when things change, and a DEVLOG entry.
DEVLOG.md (public) is the running history. CAPABILITIES.md
(public) is the feature index for the Nexus.

## WORKING RULES — follow these
- The session type is declared at the top of the handoff:
  look-only or build. Declared scope outranks momentum. Never
  give action steps in a look-only session.
- Whatever Tony asks for live outranks the handoff's run order.
  Carried items are loose ends, not an agenda.
- In build sessions he runs fast: give paste-ready boxes and
  move. But STOP AND ASK before deciding any real design
  question.
- LABEL EVERY PASTE BOX: terminal or browser console. Prefer
  terminal. If a block is text for a file rather than a command,
  say so above it and give it its own box.
- Long content goes through gedit: one box with the gedit
  command, then the content in its own box. Never terminal
  heredocs for prose. Never download links.
- Max ~3 things per message. Plain English; gloss jargon once.
- Read actual code before describing it. One careful retry after
  a failure, then switch approaches. State only what output
  shows, nothing more.
- When debugging, ask what the screen literally says before
  stacking more commands.
- Speed over hedging: flag only genuinely severe
  vulnerabilities.
- Questions to the lead dev take DAYS. Reserve them for true
  blockers.
- The DEVLOG is public: keep entries vague on account names and
  private paths.

## THE TWO SITES — don't confuse them
NEEDPEDIA.ORG is the production site: a Rails app on AWS EC2,
with a lead dev. Tony owns it and can reach all of it quickly —
server, database, admin pages. What is SLOW is getting ANSWERS
FROM THE LEAD DEV, which takes days. Prefer solutions Tony can
carry out himself; reserve dev questions for true blockers.

THE NEXUS is Tony's own site on his home Linux Mint desktop:
static pages served by nginx in Docker, exposed through a
Cloudflare tunnel, with a small Python backend for admin
endpoints and a browser terminal tile. Its project folder IS the
public web root, so anything placed there is world-readable
unless the nginx denylist blocks it.

## NEXUS ARCHITECTURE NOTES
- Four containers: the tunnel, nginx, the Python backend, and
  the browser-terminal service.
- TWO SEPARATE ADMIN LOCKS, and they can drift apart. One is
  nginx basic auth guarding the terminal tile — a two-field gray
  browser popup wanting a username. The other is an in-page
  password prompt on the gallery that checks against a constant
  in the backend script. A password change must touch BOTH.
  Confusing these cost a whole session once.
- The nginx denylist blocks scripts, configs, dotfiles, and all
  .md files by default. Individual .md docs are allowlisted
  above that rule to stay AI-readable. Config changes need a
  container restart; the password file does not.
- Two separate AI API keys exist by design: one in the backend
  (private) and one embedded in the volunteer studio pages
  (public, spend-capped, for trusted volunteers). Merging them
  would break the security boundary. A revoked studio key shows
  up as "[No response]" on every model because the page
  swallows the error.
- The home tile list is hand-written in the gallery page. A new
  endpoint needs both a backend handler AND a matching nginx
  route.
- Admin chat and the volunteer text studio each offer several
  models through a single AI router account, constrained by an
  account-level allowed-provider list.

## OBJECTIVES — RECENT
- N37 DONE: admin view of real activity on production.
- N38 DONE: volunteer studio conversations saved on the server;
  production activity collector on a 15-minute schedule.
- N39 DONE: web research in the admin chat and volunteer text
  studio. The model decides when to search, writes its own query,
  can read a full page, and knows the date. The volunteer studio
  now routes through the backend, moving its separate spend-capped
  credential off the served page.

## CURRENT OBJECTIVE (N40)
Lock the studio doors. The AI studio pages have no password: the
tile is hidden without a login, but anyone typing the page address
with a volunteer name in it walks in and spends credit. Gate them
against the volunteer password the gallery already checks.
Then: the two visibility questions still open from S38 — logins
reading zero on the activity page, and no record of whether anyone
has used the three production assistants.

## CARRIED LOOSE ENDS — do not start these unless asked
- Rotate two credentials that were publicly readable until the
  N36 denylist patch.
- Email project: back up three near-full mail accounts to a home
  drive, then a count-first cleanup script, then a private mail
  tile. Export links expire about a week after generation.
- CAPABILITIES.md is stale (last updated at Session 17) and
  needs a refresh plus a task-card section.
- A context file for needpedia.org itself does not exist yet;
  CAPABILITIES.md covers only the Nexus.
- Unmerged fix on the mail app for date-range filtering; a
  logging feature whose token may be unset and failing silently.

## UPDATE AT N41 CLOSE, 2026-09-21
- N41 DONE: volunteer text studio answers now arrive word by word, so long research answers no longer time out. The back-end program now handles requests side by side.
- Still open: studio doors (N40 objective) not yet locked. Admin chat still has the ~1-minute limit.
- Code-edit method: short changes = one precise terminal command; long changes = helper script via gedit in the private folder, then one short run command. Never hand edits.
- NEXT (N42): the phone app. Tony names which part at the start.

----- archived 2026-09-29 | from PRIVATE | file reference-to-nginx-default.conf.bak-N45 | tags: nginx, web-server-settings, no-cache, backup -----
Private file, not online: ~/Nexus_private/nginx-default.conf.bak-N45
The web server settings from before the check-back-every-time change
of 29 Sep 2026 (session N45).
Ask Tony to print it with cat if you need it.

----- archived 2026-09-29 | from PRIVATE | file reference-to-patch_nginx_N45.py | tags: nginx, no-cache, helper-script -----
Private file, not online: ~/Nexus_private/patch_nginx_N45.py
The helper script that made that change.
Ask Tony to print it with cat if you need it.

----- archived 2026-09-29 | from PRIVATE | file reference-to-threads.py.bak-N45 | tags: threads-tool, backup, n44 -----
Private file, not online: ~/Threads_private/threads.py.bak-N45
The updates tool as it was before N45 (edition N44).
Ask Tony to print it with cat if you need it.

----- archived 2026-09-29 | from PRIVATE | file reference-to-threads.py.bak-N45b | tags: threads-tool, backup, n45 -----
Private file, not online: ~/Threads_private/threads.py.bak-N45b
The updates tool's first N45 version, before one archive per thread.
Ask Tony to print it with cat if you need it.

----- archived 2026-09-29 | from PRIVATE | file reference-to-N45-handoff.txt | tags: handoff, nexus, n45 -----
Private file, not online: ~/Nexus_private/N45-handoff.txt
The handoff prompt that opened Nexus session N45.
It holds the sensitive section, so it is never published.
Ask Tony to print it with cat if you need it.

----- archived 2026-09-29 | from PRIVATE | file reference-to-N46-handoff.txt | tags: handoff, nexus, n46 -----
Private file, not online: ~/Nexus_private/N46-handoff.txt
The handoff prompt for Nexus session N46, written at the close of N45.
It holds the sensitive section, so it is never published.
Ask Tony to print it with cat if you need it.

----- archived 2026-09-29 | from UPDATES | added 2026-09-28 | tags: untagged -----
UPDATE FOR NEXUS: THE OBJECTIVE FOR N45
From the Nexus thread itself, end of session N44, 28 September 2026.
Tony's live instructions still come first.


WHAT WENT WRONG
Tony sent the PU (Project Unstoppable) chat to its posts. Its AI could not
use anything that is supposed to be public:
- Its web copy of working-with-tony.txt had no edition line at all, so
  it was a stale copy from before edition N44d. The TS chat got a stale
  copy earlier the same day, and this thread got stale copies of
  PA-NEXUS.txt at N42, N43 and N44.
- It fell back to asking Tony to print its updates post and its
  cross-reference post from his disk.

Tony's goal: every thread reads its public material straight from the
Nexus. Tony only has to tell a thread "check for updates", perhaps with
one address.


WHAT IS KNOWN
- The files ARE online. Tony's own curl, through the same public
  addresses, got the new copies at N44: edition N44d, and every UPDATES
  and CROSSREF post answering 200.
- AI web fetch tools can only open an address that has already appeared
  in the conversation or in a page they fetched. PU's stale copy of the
  post had no PU section, so PU's own post addresses never appeared
  anywhere its AI could see them. So a stale post blocks everything
  listed in it.


WHAT IS NOT KNOWN YET
Where the old copy comes from. Two possibilities:
  (a) Cloudflare, the service in front of the Nexus, keeping a saved
      copy at some of its locations.
  (b) The AI fetch tool keeping its own saved copy.

First check, read-only. In the output, cf-cache-status: HIT or EXPIRED
means Cloudflare is serving saved copies; DYNAMIC or MISS means it is
not. Also note any Cache-Control, Last-Modified and ETag lines.
  curl -sI https://nexus.needpedia.org/working-with-tony.txt
  curl -sI https://nexus.needpedia.org/public/UPDATES-PU.md


FIXES TO OFFER TONY (options, not decided)
- Tell every cache to check back each time. The web server sends a
  "do not reuse without checking" instruction (Cache-Control: no-cache)
  with the Nexus's text and markdown files. This fixes (a) outright and
  helps with well-behaved fetchers. It is a web-server settings change,
  so the web-server container needs a restart after it.
- If Cloudflare is caching: a Cloudflare setting that skips caching for
  the Nexus, or clearing its saved copies after each change.
- Put a thread's own addresses into every message sent to it (the chat
  boxes and handoffs), so its AI can open them even when the post it
  fetched is stale.
- A tag on addresses in messages, for example
  working-with-tony.txt?v=N45. The server ignores it; a cache treats it
  as a new address. Tony prefers one fixed address, so this would only
  be a nudge in messages, if used at all.
- Reading from disk with cat stays the fallback. It always works.


HOW TO KNOW IT IS FIXED
A fresh AI chat, told only "check your updates at
https://nexus.needpedia.org/public/UPDATES-PU.md", reads the current
post, sees edition N44d or newer on the post's first header line, and
opens its own cross-reference post without Tony pasting anything.


AFTER IT IS FIXED
Tony will tell PU to check for updates. Its update and two
cross-reference notes are already waiting. Anything new for PU goes
through its updates post.

----- archived 2026-09-29 | from PRIVATE | file handoff-N47-ref.md | tags: handoff, n47, private -----
tags: handoff, n47, private
Handoff prompt for Nexus session N47, written at the close of N46, 29 September 2026.
Saved privately at /home/clearcrow/Nexus_private/handoff-N47.txt
Contents not published: it holds the SENSITIVE section.
To read it, have Tony run: cat ~/Nexus_private/handoff-N47.txt
