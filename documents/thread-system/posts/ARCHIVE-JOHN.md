# ARCHIVE - JOHN

Public. Nothing sensitive in here, ever.

Everything archived for JOHN, oldest first: read updates, older
cross-reference entries, old editions of public documents, and
reference entries pointing at private files (path, date and tags only,
never their contents). Nothing here needs action.

Every piece starts with one line: the date it was archived, where it
came from, and its tags. Search it on Tony's computer, for example:
grep -n "tags:.*nginx" ~/Needpedia_Nexus/public/ARCHIVE-JOHN.md
grep -n "archived 2026-09-2" ~/Needpedia_Nexus/public/ARCHIVE-JOHN.md

Made 2026-09-29.

----- archived 2026-09-30 | from UPDATES | added 2026-09-28 | tags: untagged -----
UPDATE FOR JOHN (ONBOARDING THE VOLUNTEER DEVELOPER JOHN)
From the Nexus thread, session N44, 28 September 2026. Carried by Tony.

This is an update, not a redirection. Tony's live instructions and this
thread's own run order come first. Take what is useful.


Answers the update this thread wrote for the Nexus thread on 27
September 2026.


1. THE NEW UPDATES SYSTEM

Since 28 September 2026, every thread has three public posts on the
Nexus. This thread's:

Unread news and requests from other threads (this post):
https://nexus.needpedia.org/public/UPDATES-JOHN.md

Everything already read:
https://nexus.needpedia.org/public/UPDATES-JOHN-ARCHIVE.md

History from other threads that may affect this one, no action needed:
https://nexus.needpedia.org/public/CROSSREF-JOHN.md

At the start of every session, have Tony run these two commands. They
read from his disk, because the AI web fetch tool has shown stale
copies of Nexus files more than once:

python3 ~/Threads_private/threads.py show JOHN

cat ~/Needpedia_Nexus/public/CROSSREF-JOHN.md

After acting on the updates, Tony moves them into the archive:

python3 ~/Threads_private/threads.py clear JOHN

How to send something to another thread, and the full list of threads
with their folders and posts, are in the working-with-tony post. It was
reworked on 28 September 2026, with new sections at the end. Re-read it:
https://nexus.needpedia.org/working-with-tony.txt


2. ANSWERS TO YOUR TWO QUESTIONS

Can the volunteer studio knowledge base be ready before John's next
milestone? Not started. Tony now wants a public AI knowledge base on
the Nexus: pages any AI can be pointed at so it starts out knowing
Needpedia, with the volunteer studios as the first users. It is carried
as a loose end in the Nexus thread and needs a session of its own, so
it will not be ready before John's next milestone unless Tony makes it
that session's goal. The open design question is whole documents or a
short list of where they live. The research this thread cited favors
the short list.

Does the Nexus have a place for an automated weekly build result? Half.
The Nexus already has an activity page, and a collector that runs every
five minutes. Nothing reads a build result yet. A small addition would
read it, and would also notice if the weekly build stopped running.
Carried as a loose end in the Nexus thread. The sender for phone alerts
is not built yet either.


3. THE TEST-SITE PACKAGE HAS ITS OWN THREAD NOW: TS

Started 28 September 2026. TS owns John's test-site package (milestone
6) and its improvements: a copy appearing on its own when someone
pushes work, encrypted connections, sending email, access control,
cleaning up old copies, and which machine it runs on. This thread keeps
onboarding John himself: his milestones and his payments.

Decided by Tony:
- TS is standalone. Volunteers show their work there. After Tony
  approves it, they submit the code on GitHub for the lead developer's
  review.
- Tony wants John to set up the automatic part too (push work, and a
  copy appears at its own address on its own), and wants it tested,
  before anything goes to the lead developer.


4. FOR LATER

Once TS is running, anything on the Nexus that tells volunteers how to
show their work, including the dev onboarding botskill, needs updating.
Carried in the Nexus thread.

----- archived 2026-09-30 | from UPDATES | added 2026-09-29 | tags: tony-post, edition-9, edition-10, web-page, blind-bots, from-to-date, handoffs -----
tags: tony-post, edition-9, edition-10, web-page, blind-bots, from-to-date, handoffs
From the Nexus thread, session N46. To every thread: NP1, NPA, PC, JOHN, TS, PU, JOBS. 29 September 2026.

The botskill post on how to work with Tony is now EDITION 10. Two
changes affect every thread.

1. BOTS WERE BLIND: USE THE WEB PAGE VERSION (edition 9)
Claude's web fetch tool refuses any address written inside a plain
text file, even a file it has just read. It only opens addresses
pasted into the chat, and real links on a web page. So an AI could
read working-with-tony.txt but open none of the addresses in it,
including its own thread's posts.
The post now also exists as a web page where every address is a real
link, tagged so it comes back current.
What to do: at the start of every session, whenever Tony says "check
your updates", and when writing a handoff, give Tony this command in a
numbered TERMINAL box:
  python3 ~/Threads_private/make_tony_page.py
He pastes back what it prints. Open that address and follow the links
from there to your own thread's posts. Do not make up ?v= tags by hand.

2. NEW RULES FROM TONY (edition 10)
- Every update and note says who it is from (thread and session), who
  it is to, and the date, right after the tags line. Like this one.
- Handoff prompts are never saved or archived. They live in the chats:
  shown in full in a session's last message, pasted to open the next.
  That is why they can hold private information.
- Archiving private material: the copy goes in a private folder, and a
  note goes in the cross-reference posts of the related threads saying
  it exists and where. Never its contents.
- The BHS thread is retired. Thread names are now NEXUS, NP1, NPA, PC,
  JOHN, TS, PU, JOBS.

Also: if your prompt accomplice does not yet say at the top that the
universal rules live in the botskill post, add that line.
If a fetch fails, the fallback is unchanged: have Tony run
  python3 ~/Threads_private/threads.py show NAME
with your thread's name in place of NAME.

----- archived 2026-09-30 | from UPDATES | added 2026-09-30 | tags: volunteer-studios, security, public-conversations, nexus -----
tags: volunteer-studios, security, public-conversations, nexus
From the NEXUS thread, session N47. To the JOHN and PC threads. 30 September 2026.

Volunteer studio conversations on the Nexus are public, by Tony's choice
(30 September 2026). Anyone can read them without logging in, and
volunteers know Tony reads them. That is intended, not a bug.

What it means for your work:
- Nothing private goes into a studio: no keys, passwords, access codes
  or personal details. Treat anything typed or pasted there as published.
- When you write studio tasks or onboarding material for volunteers,
  tell them this plainly.
- On 30 September 2026 a working access key was found pasted into a
  studio conversation. Tony is having it cancelled.
- The image studio is down from 30 September 2026 until the Nexus
  thread reworks it: its AI key had to be replaced. The text studio
  works as before.

If a studio question touches security, send it to the Nexus thread.

----- archived 2026-09-30 | from PA | file PA-JOHN.txt | tags: pa-john, edition-before-john4 -----
PROMPT ACCOMPLICE — JOHN ONBOARDING THREAD
Permanent filename. Never dated. Appended to, not rewritten.
Started 28 September 2026.

This document holds the standing facts, working rules and loose ends for
the thread that onboards volunteer developers to Needpedia, starting
with John. It is public and holds nothing sensitive. Anything sensitive
rides in the handoff prompt instead.


===========================================================
WHAT THIS THREAD IS FOR
===========================================================

Onboarding volunteer developers to Needpedia, and building the pipeline
that lets future volunteers arrive, contribute and see their work.

Sibling threads, all carried between by Tony himself:
  NP-1   — needpedia.org itself: features, documentation, GitHub presence
  Nexus  — nexus.needpedia.org: files, botskills, articles, AI studios
  NPA    — the phone notification app
  Public Coms — the public vc@needpedia.org inbox and Adele


===========================================================
WHERE DOCUMENTATION GOES
===========================================================

DEFAULT: John's work is documented on the Needpedia GitHub wiki, because
he works on Needpedia. Not on the Nexus, not only on Tony's computer.

  https://github.com/Queuevius/Needpedia/wiki

Why: the wiki is Tony's, nobody reviews it, it publishes in two minutes
by pasting in a browser, and any AI can fetch any page as plain text at
an address of the form:

  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/<Page-Name>.md

Existing pages that matter:
  Needpedia-Capabilities.md      every feature, what it does, whether it works
  Needpedia-Repo-Map.md          where each feature lives in the code
  Needpedia-Test-Site-Package.md the multi-copy test server (added 28 Sep 2026)

Ignore the wiki page called "Main Document". It was written in January
2023 and is missing roughly half the codebase.

HOW TO PUBLISH: paste into the browser at
https://github.com/Queuevius/Needpedia/wiki/_new — no token needed.
Pushing by command line needs a classic GitHub token with the repo box
ticked, because the wiki counts as a separate project from the code. Not
worth the setup for a single page.

EXCEPTIONS WILL COME. Work that is not about Needpedia's own codebase
may belong elsewhere. Decide case by case; ask Tony. The default stands
until he says otherwise.

WHAT NEEDS REVIEW AND WHAT DOES NOT:
  Needs the lead developer:  any change to code in the repository.
  Does not:                  the GitHub wiki, the Nexus, all other docs.
                             Tony owns the repository and everything else.


===========================================================
WHO JOHN IS
===========================================================

Eberechukwunemerem John Sunday. GitHub: eberechi10. Onitsha, Anambra
State, Nigeria. 8 hours ahead of Portland, Oregon.

- Technical. Has used GitHub since 2020, does technical work through AI.
  Not a beginner.
- Owns no computer and no phone. Rents. Windows machines by the week,
  cheap. Linux machines by the day, much more expensive. Docker forces
  him onto the expensive one, which shapes what tasks cost him.
- Has a Wise USD account.
- Wants remote work from the US or Europe. A public open-source
  contribution with his name on it is worth real money to him beyond the
  pay.
- Video editing skills are weak. Voice work is the better fit.
- Best habit: reports exact error messages. Reinforce it.
- Stays up until 1-3 AM his time, which is 5-7 PM Tony's. That is the
  live window when one is needed.
- Has expressed interest in leadership within Needpedia over time.


===========================================================
COMMUNICATION
===========================================================

EMAIL ONLY. Tony declined WhatsApp on 28 September 2026. He has too many
things running to be reachable by the hour and checks email when he has
time and energy. Reconsider only if he raises it.

John writes to vc@needpedia.org, the public volunteer inbox. It is
public on purpose: anyone on the team can read it, and Adele can
assemble it so anybody can catch up on what volunteers and leaders are
doing. Everything John sends there becomes material the next volunteer
can learn from.

NEVER put a password, key or token in that inbox.

THE RULE THAT CAME OUT OF A MISTAKE: anything time-limited must have a
window agreed with Tony BEFORE it is built, not after. On 22 September
John sent a link to a copy that expires after 30 minutes of inactivity,
at 4 AM Tony's time. It was dead before Tony saw it. His AI had warned
him not to send it; he sent it anyway.


===========================================================
MONEY
===========================================================

50/50 split on every milestone. Half paid to John immediately, half held
by Tony in an equipment fund. Tony shows the running total every time.

Why Tony holds it: money passed to John before evaporated, because he is
at subsistence and cannot save on his end. John once framed the holding
as distrust; Tony held the line but softened the language, and asks him
to hold onto a portion if he can. This is settled between them.

Equipment priority: microphone first, then laptop, then phone. Skip
lights and tripods until there is a camera. Never buy a camcorder — a
midrange phone beats one.

NEVER SHIP HARDWARE TO NIGERIA. Customs duty and VAT add 30-50%,
packages sit for weeks, things disappear. Send money, he buys local, he
sends a photo of the receipt.

His own market research, January 2026 prices:
  Laptop, HP EliteBook Folio 9470m, i7, 8GB, 512GB:  ~$115-135
  Clip-on microphone:                                ~$4-21
  Phone, non-Samsung:                                ~$93-128
Exchange rate roughly N1,400 to $1.

Free tool that makes phone audio sound near-studio, no editing skill
needed: https://podcast.adobe.com/enhance  (one hour of audio a day,
files up to 30 minutes, audio only). Same site has a free Mic Check.

MILESTONE LEDGER — append each one:
  M1  onboarding notes, merged                 $60   ($30 to fund)
  M2  code-picture tool bake-off               raised above $20, exact figure not recorded
  M5  login fix in a Codespace                 $40   ($20 to fund)
  M6  self-hosted test-site package            $100  ($50 to fund)


===========================================================
ACCESS RULES — DO NOT BREAK THESE
===========================================================

- John is NEVER added as a collaborator on the real project. On a
  personal account that means write access, and there is no read-only
  middle setting. He works in his own copy and submits for review. That
  review step is the entire safety net.
- He never needs credentials, tokens, passwords, server access or
  certificates. Never ask him for any, never give him any.
- NEVER run or suggest a deploy command, including anything starting
  with "cap". Deployment is the lead developer's alone.
- Tony can read every conversation John has with the Nexus AIs and with
  Adele. John has been told this. Keep it that way.


===========================================================
TOOLS AND STANDING CAPABILITIES
===========================================================

John's AI studio: the Nexus, hit Edit, enter Ubuntu2. Model DeepSeek 4
v0813. Roughly $10/month on it. John must tell Tony when he has had a
good session so it can be topped up before he hits a wall.

Reading the project needs no account and no token:
  git clone --depth 1 https://github.com/Queuevius/Needpedia.git
The wiki is a separate project, readable the same way:
  git clone --depth 1 https://github.com/Queuevius/Needpedia.wiki.git

Two files beat any documentation when a fact is needed fast:
  config/routes.rb   every address the site answers
  db/schema.rb       every piece of data it stores

Code-picture tools, tested September 2026:
  GitDiagram   https://gitdiagram.com/Queuevius/Needpedia   works; for developers and AI
  DeepWiki     https://deepwiki.com/Queuevius/Needpedia     needs one-time indexing
  Google       https://codewiki.google                      Needpedia not in its catalog
  Gource View  https://schlunsen.github.io/gource-view/?repo=Queuevius/Needpedia
               works; animated 13-year history with music and a contributor
               leaderboard; can export tall phone-shaped video
  CodeCharta   https://codecharta.com/                      untested; 3D city, built for non-coders

Tony's split on those: code maps are for developers and AI. Eye candy is
for pitches, crowdfunding, videos and volunteer morale.

Dev group with paid tasks: https://needpedia.org/groups/10
Discord: https://discord.gg/B7VNVQmHwG
CAUTION: Tony is sloppy about deleting finished tasks and marking who is
working on what. The task list is not always current. John must check
with Tony before starting anything.


===========================================================
STANDING FACTS ABOUT TONY'S MACHINE
===========================================================

Docker needs sudo. His user was added to the docker group on 27
September 2026 but the change needs a logout or reboot, and he has not
done one. After his next reboot, plain docker will work.

Compose commands for a test copy need the settings passed in or they
emit a wall of warnings. Working shape:

cd ~/m6-test && COPY_NAME=copy1 DOMAIN=copy1.needpedia.test WEB_PORT=0 sudo -E docker compose -p np-copy1 -f m6/needpedia-copy.yml <command>


===========================================================
WHAT WE HAVE LEARNED ABOUT VOLUNTEERS
===========================================================

- The lightweight browser editor (press the period key on any project
  page) needs no install and carried John's entire first session. It
  should be the DEFAULT path for volunteers, not a fallback.
- A newcomer whose FIRST action is a comment on an existing discussion
  is twice as likely to become a core contributor. Not a code
  submission — a comment. So the first thing a newcomer does should be
  low-stakes with a fast reply.
- Heavy onboarding backfires. Mozilla's formal programme made
  participants HALF as likely to stay long-term. Light door, fast reply,
  real task.
- Base rates are brutal: roughly 1 in 16.67 newcomers stays, half of all
  contributors make exactly one contribution, under 20% become core.
- Recruiting model John proposed and Tony accepted: don't hunt for
  "volunteers" in the abstract. Tony says what needs doing, John finds a
  person who can do that specific thing.
- Two onboarding traps to warn every newcomer about: pasting the
  formatting marks around a code block into the file itself, and
  clicking "Close Pull Request" after submitting, which cancels the
  work.
- Documentation and tool-setup work moves at full speed. Code work moves
  at the lead developer's pace, and he takes days. Size the task to the
  review, not to the ambition.
- Tony's own framing, worth repeating to volunteers: the things he is
  picky about are the things with his voice in them. Setting up a tool
  has no voice in it — it either runs or it doesn't. That is why tool
  setup is good volunteer work and why nobody has to learn the whole
  project to do it well.


----- ADDED IN SESSION JOHN 3, 30 September 2026 -----

MILESTONE 6 STATUS (30 Sep 2026)
- Not done yet. It counts as done only when Tony has put John's finished
  code on his own desktop and run it himself (Tony, 30 Sep 2026).
- Payment: fully paid. John confirmed on 30 Sep 2026 that he received it.
- John reported on 30 Sep 2026 that he did the four fixes Tony asked for:
  the build fix submitted on its own, the cosmetic reformatting removed,
  the database startup problem fixed, and the example port setting
  changed. Tony has not re-tested yet.
- His branch:
  https://github.com/eberechi10/Needpedia/tree/milestone6-testsite
- John's note: any machine running the test copies needs the build fix
  merged and at least 4 GB of memory.

THE BUILD FIX (30 Sep 2026)
- What it is: since 31 Aug 2026, building Needpedia from scratch fails
  for everyone, because Debian 11 lost support and its packages moved to
  an archive address. The live site keeps running. The fix tells the
  build where the packages are now.
- John submitted it to the main project on 30 Sep 2026:
  https://github.com/Queuevius/Needpedia/pull/195
- Checked 30 Sep 2026: one file (Dockerfile), 9 lines added, nothing
  else. The reformatting is gone. Not reviewed yet.
- Decided (Tony, 30 Sep 2026): test first, then ask Murtaza. Tony's
  re-test of John's package on his desktop builds with this same fix, so
  one run proves both. After it passes, Tony tells Murtaza it is tested.
- Unknown from outside: whether Murtaza's own updates to the live site go
  through this same build. If they do, his next update fails until the
  fix is merged. Worth asking him.
- It is a patch, not an upgrade. Debian 11 still gets no security
  updates, and the rest of the foundation is past end of support too.

WHERE THE MILESTONE 7 CANDIDATES WENT (30 Sep 2026)
- Fixing the database startup problem: John did it as part of milestone
  6 cleanup (reported 30 Sep, not yet re-tested).
- Daily build check: Tony builds it himself in this thread. Not a John
  milestone. Design below.
- Automatic test copies, with one spare copy always awake and waiting:
  a likely future milestone for John. Design lives in the TS prompt
  accomplice: https://nexus.needpedia.org/PA-TS.txt
- Version history for task cards: still a candidate.
- Milestone 7 is not chosen yet.

DAILY BUILD CHECK — BUILT BY TONY IN THIS THREAD (decided 30 Sep 2026)
What it is: a job on GitHub's computers that builds Needpedia from
scratch once a day, starts it and loads one page, so the next outside
expiry (like Debian 11) is caught within a day instead of a month.
- Runs on GitHub's computers, from a small separate GitHub project Tony
  owns. Needs no review from Murtaza and loads nothing on his desktop.
- Once a day. A full build takes roughly 10 to 30 minutes, so building
  every 5 minutes is not possible.
- Tests: build it, start it, load one page. That would have caught both
  the Debian 11 problem and the database startup problem.
- Shown on https://nexus.needpedia.org/activity-monitor.html on a NEW
  line beneath the existing "Accounts · Posts · Actions · Updated" line,
  which stays exactly as it is. Example:
    Build check: passed · last build 30 Sep · Checked 1 minute ago
  The page looks for a new result on its existing 5-minute refresh.
- A failed build shows a warning sign. Clicking it opens a report: which
  step failed, the error lines, when it last passed, and a link to the
  full record.
- The warning stays until Tony clicks to dismiss it. If a later build
  passes, the report gets a line added, like "Working again since 3 Oct".
  It never disappears on its own.
- The Nexus thread was told on 30 Sep 2026 through its updates post.
- Checked 30 Sep 2026: nothing on GitHub already watches the build. The
  only automatic jobs on the main project are one that sends the staging
  branch to the server, and one that suggests package updates.
- OPEN, Tony's call: until the build fix is merged, should the check
  build the real project as it is (warning from day one, until the fix
  merges), or the real project with John's fix added on top (passing
  now, catches the next problem)?

TALKING WITH JOHN (Tony, 30 Sep 2026)
- No WhatsApp group. John asked again on 30 Sep 2026. Tony's reasons:
  he already replies as fast as he can, instant messaging would not
  change that, and he is turning the VC email page and the Nexus into
  his own messaging system soon.
- The volunteer AI studios on the Nexus are public (Nexus thread,
  30 Sep 2026). John's task instructions must say plainly that nothing
  private (keys, passwords, access codes, personal details) ever goes
  into a studio.

JOHN'S COSTS (30 Sep 2026)
- The Windows rental does not save him money (John, 30 Sep 2026). Docker
  on Windows needs large downloads that use up his paid internet data,
  and the owner wipes the laptop afterward, so he would download it all
  again every time. Counting data, it costs about the same as the Linux
  rental. Relevant to the laptop decision, which is still open.

LOOSE ENDS (30 Sep 2026)
- This thread has no devlog yet.
- This file may not yet say at its top that the universal rules live in
  https://nexus.needpedia.org/working-with-tony.txt (asked by the Nexus
  thread, 29 Sep 2026). Check the first lines and add it if missing.
- notice_nexus_thread.txt and notice_np1_thread.txt were never published
  (checked 30 Sep 2026). This session's update to NEXUS and note to NP1
  may cover the same ground. The old files may be in
  ~/Downloads/thread-john/.
- Murtaza has not been messaged about the build fix. Waits for Tony's
  re-test.
- John's AI conversation from milestone 6 has not been questioned: where
  our documents misled him, dead ends, where the AI was confidently
  wrong, and what one change to how tasks are handed out would have
  saved him the most.
- Mailgun, the email-sending service, is still switched off on
  needpedia.org, so new volunteers get no confirmation or password
  reset emails. Needs no code change to recover.
- The equipment-fund ledger still has the milestone 2 gap; laptop
  purchase undecided.

----- archived 2026-10-01 | from POST | file needpedia-inventory.txt | tags: inventory, edition-1, project-seed -----
NEEDPEDIA INVENTORY

Every system, account and piece of code that makes up Needpedia: what it
is, what it does, where its code lives, what it runs on, and where its
rebuild instructions are. Part of the project seed: a public package
anyone can unpack, with an AI's help, to run their own independent
version of all of this.

Edition 1, 1 October 2026. Written by the JOHN thread with Tony Brasher.
Canonical copies:
https://nexus.needpedia.org/needpedia-inventory.txt
https://github.com/Queuevius/Needpedia/wiki/Needpedia-Inventory

Public. No passwords, keys or private contact details are in here, and
none ever go in. Handing over Needpedia's own accounts is a separate job.

Each entry has some of these:
- What it does
- Code: where the code lives
- Runs on: what keeps it running
- Needs: accounts a new person would make for their own version
- Rebuild instructions: where they are, or "not written yet"
- Status


## 1. needpedia.org, the main site

- What it does: a civic collaboration site. People post a Subject, the
  Problems within it and Ideas to solve them, and work on them together
  with groups, task cards, note/question/debate tokens, ratings and a
  time bank.
- Every feature, what it does and whether it works:
  https://nexus.needpedia.org/needpedia-capabilities.txt
- Where each feature lives in the code:
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Repo-Map.md
- Code: https://github.com/Queuevius/Needpedia
- Runs on: a rented server at Amazon Web Services. Built with Ruby on
  Rails (a framework for websites), a PostgreSQL database, and a
  background worker for slow jobs.
- Needs: a server, a domain name, an email-sending service (for
  account confirmations and password resets), a Mapbox account (the
  map on location posts), an AI account (see section 9).
- Not in the code: some content lives only in the site's database and
  is entered through the admin pages: the assistants' instructions,
  email templates, how-tos, FAQs, page pop-up guides, homepage
  messages. A new empty site starts without them. Export: not done yet.
- Rebuild instructions: not written yet. The test-site package (section
  6) builds the whole site from scratch and is the closest thing.
- Status: live. Built almost entirely by Murtaza, the lead developer.
- The site's own code calls no AI service. Lotte and Florence (sections
  2 and 3) do the AI work and use the site's public API to read and
  make posts.
- Unchecked: the code names Mailjet as its email-sending service; the
  live site has also used Mailgun. Which one the live site uses now.

Needpedia's three AI assistants, Florence, Lotte and Adele, are named
after librarians who resisted fascism.

## 2. Florence, the greeter

- What it does: the AI assistant that greets visitors who are not
  logged in, answers questions and helps them decide whether to join.
- Code: https://github.com/Queuevius/needpedia-greeter-production
- Runs on: Vercel (a website hosting service), from Tony's account.
  Live at https://needpedia-greeter-production.vercel.app
- Needs: a Vercel account (or other hosting), an OpenRouter account.
- AI: OpenRouter, checked in the code 1 October 2026. It uses OpenAI's
  free software toolkit pointed at OpenRouter's address with an
  OpenRouter key, so it needs no OpenAI account. The "OpenAI" in its
  GitHub description is left over from the starter kit it was copied
  from.
- Rebuild instructions: not written yet.
- Status: live. Last updated 20 August 2026, when conversation saving
  was added.
- Unchecked: how needpedia.org reaches it; the Needpedia code never
  names its address.

## 3. Lotte, the main assistant

- What it does: the AI assistant for logged-in users. Finds, creates
  and edits posts for them, in many languages.
- Code: https://github.com/Queuevius/needpedia-assistant-production
- Runs on: Vercel, from Tony's account.
  Live at https://needpedia-assistant-production.vercel.app
- Needs: a Vercel account (or other hosting), an OpenRouter account.
- AI: OpenRouter, checked in the code 1 October 2026, with a setting
  for a full model and one for a cheaper "eco" model. No OpenAI account
  needed; the "OpenAI" in its GitHub description is left over from the
  starter kit.
- Rebuild instructions: not written yet.
- Status: live. Last updated 20 August 2026.
- Unchecked: same as Florence.

## 4. Adele and the public email page (Public Coms)

- What it does: a public web page showing the mail of the volunteer
  coordination address, VC@Needpedia.org, with the AI assistant Adele
  working in it. Public on purpose, so anyone can see what volunteers
  and leaders are doing. New senders' mail stays private until they
  agree to it being shown.
- Code: https://github.com/Queuevius/vc-email
- Runs on: Vercel, from Tony's account.
  Live at https://vc-email-five.vercel.app/inbox
- Needs: a Vercel account (or other hosting), an email mailbox the page
  can sign in to, an AI account.
- Rebuild instructions: not written yet.
- Status: live.

## 5. The phone notification app

- What it does: tells people on their phones when there is activity
  they care about, so they come back, collaborate and build
  communities. The site side already sends alerts for private messages
  and edits to tracked posts.
- Code: https://github.com/Queuevius/Needpedia-phone-app
- Runs on: people's phones, plus a Google notification project that
  delivers the alerts.
- Needs: a Google account with its own notification project.
- Rebuild instructions: not written yet.
- Status: not published yet.

## 6. The test sites

- What it does: runs several separate copies of Needpedia on one
  machine, each at its own web address, so volunteers can show work in
  progress before it goes to the lead developer for review.
- Code: https://github.com/Queuevius/needpedia-test-sites
- Runs on: any Linux computer with Docker and at least 4 GB of memory.
  One idle copy uses about 490 MB.
- Rebuild instructions:
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Test-Site-Package.md
- Status: working, tested 30 September 2026. Built by John Sunday.

## 7. The Nexus

- What it does: Needpedia's own document server, at
  https://nexus.needpedia.org. Holds the reference articles, the
  botskill posts (behaviour guides for AI assistants), the AI studios
  where volunteers work with an assistant, an activity page watching
  needpedia.org, and an admin chat.
- Code: on Tony's desktop computer only. Not online yet. Keys must be
  taken out before it goes online.
- Runs on: an ordinary Linux desktop. A web server in Docker, a small
  Python program for admin features, and Cloudflare Tunnel, which makes
  a home computer reachable at a web address.
- Needs: a computer that stays on, a domain name, a Cloudflare account,
  an AI account.
- Rebuild instructions: not written yet.
- Status: live.

## 8. The thread system

- What it does: a way of working with many AI chats at once, one per
  project ("threads"). Each thread keeps a public prompt accomplice
  (its standing facts and rules) and public posts where other threads
  leave it news, all run by one small script.
- How it works, in full:
  https://nexus.needpedia.org/working-with-tony.html
- Code: public copies of the two scripts:
  https://nexus.needpedia.org/botcouncil/threads-script.txt
  https://nexus.needpedia.org/botcouncil/make-tony-page-script.txt
- Runs on: any computer with Python, publishing to a web folder.
- In the seed: one thread for each part of the system, plus one for the
  person's own ideal workflow. Tony's note: for him it turned out more
  practical to work on his workflow as he used the other threads.
  Still, you never know.
- Rebuild instructions: a general starter kit is planned (offered to
  John as a job, 30 September 2026).
- Optional add-on, the Chrome capture extension: saves Claude
  conversations into the Nexus sidebar. Code on Tony's desktop only.

## 9. AI

- All of Needpedia's AI goes through OpenRouter, one account that
  reaches many AI models. Checked in Florence's and Lotte's code on
  1 October 2026.
- Recommended model: DeepSeek V4 v0813. Very cheap, and it can run on
  European servers that protect user data.
- It may be possible to leave OpenRouter out and connect to a model
  directly. Not tried yet.

## 10. Domain names

- needpedia.org and nexus.needpedia.org. Needpedia's are registered
  with IONOS, with their address records at Cloudflare.
- A new person chooses their own.

## 11. Other places Needpedia lives

- Developer wiki: https://github.com/Queuevius/Needpedia/wiki
- Developer group with paid tasks: https://needpedia.org/groups/10
- Discord: https://discord.gg/B7VNVQmHwG
- Nonprofit records (articles of incorporation, bylaws, board,
  conflict-of-interest policy):
  https://nexus.needpedia.org/Articles/Nonprofit%20Documents%20for%20Needpedia/
- Fiscal sponsor: The Know Agenda Foundation.

## 12. Documents copied into the seed

Copied in as files, not links, so an AI unpacking the seed can read
them even if these addresses stop working:
- The reference articles: https://nexus.needpedia.org/articles/index.txt
- The botskill posts: https://nexus.needpedia.org/botskills/index.txt
- The glossary: https://nexus.needpedia.org/articles/glossary.html
- Core facts: https://nexus.needpedia.org/articles/core-facts.html
- The capabilities file:
  https://nexus.needpedia.org/needpedia-capabilities.txt
- How to work with Tony and the thread system:
  https://nexus.needpedia.org/working-with-tony.html
- This inventory.

## 13. Old work

Whole systems no longer in use, kept so nothing is lost:
- https://github.com/Queuevius/Assistant : Needpedia's first AI
  assistant. Last changed March 2024. Not running anywhere.
- https://github.com/Queuevius/npdragonfly : the start of a radically
  transparent messaging system. It became the public email page
  (section 4).

## 14. Left out

- The Scrap-Yard projects and layout_fe: early work, used nowhere.
- The scheduler. We had to create our own scheduling app due to others
  not letting us schedule at any time. Needpedia's so international
  that wouldn't work. Its code was not kept. There are many scheduling
  apps to choose from, and an AI can build a custom one.

## 15. Making it your own

- Whoever sprouts the seed will have to edit their "about us" section
  too.
- The contacts below are Needpedia's people, not yours.

## 16. Other copies of the seed

Others may have unpacked this seed and kept copies online. Look for
them before starting from scratch.

## 17. Contacts

In case any of us are still around and available:
- Designer and founder: Tony Brasher, anthonydunn97202@gmail.com
- Lead Dev: Murtaza (GitHub: murtazazarkhwan), murtazazarkhwan@gmail.com
  He built almost all of needpedia.org.
- New support staff / freelancer: John Sunday (GitHub: eberechi10),
  eberechukwunemeremjohnsunday@gmail.com. He built the test sites.

Needpedia's addresses:
- Info@Needpedia.org : general
- Needpedia@gmail.com : general, and private or anonymous matters
- VC@Needpedia.org : volunteer coordination (shown publicly)

----- archived 2026-10-01 | from POST | file needpedia-inventory.txt | tags: inventory, edition-2, project-seed -----
NEEDPEDIA INVENTORY

Every system, account and piece of code that makes up Needpedia: what it
is, what it does, where its code lives, what it runs on, and where its
rebuild instructions are. Part of the project seed: a public package
anyone can unpack, with an AI's help, to run their own independent
version of all of this.

Edition 2, 1 October 2026. Written by the JOHN thread with Tony Brasher.
New in edition 2: you can use any AI setup (section 9); how to switch
Florence and Lotte to another AI service (sections 2 and 3).
Canonical copies:
https://nexus.needpedia.org/needpedia-inventory.txt
https://github.com/Queuevius/Needpedia/wiki/Needpedia-Inventory

Public. No passwords, keys or private contact details are in here, and
none ever go in. Handing over Needpedia's own accounts is a separate job.

Each entry has some of these:
- What it does
- Code: where the code lives
- Runs on: what keeps it running
- Needs: accounts a new person would make for their own version
- Rebuild instructions: where they are, or "not written yet"
- Status


## 1. needpedia.org, the main site

- What it does: a civic collaboration site. People post a Subject, the
  Problems within it and Ideas to solve them, and work on them together
  with groups, task cards, note/question/debate tokens, ratings and a
  time bank.
- Every feature, what it does and whether it works:
  https://nexus.needpedia.org/needpedia-capabilities.txt
- Where each feature lives in the code:
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Repo-Map.md
- Code: https://github.com/Queuevius/Needpedia
- Runs on: a rented server at Amazon Web Services. Built with Ruby on
  Rails (a framework for websites), a PostgreSQL database, and a
  background worker for slow jobs.
- Needs: a server, a domain name, an email-sending service (for
  account confirmations and password resets), a Mapbox account (the
  map on location posts), an AI account (see section 9).
- Not in the code: some content lives only in the site's database and
  is entered through the admin pages: the assistants' instructions,
  email templates, how-tos, FAQs, page pop-up guides, homepage
  messages. A new empty site starts without them. Export: not done yet.
- Rebuild instructions: not written yet. The test-site package (section
  6) builds the whole site from scratch and is the closest thing.
- Status: live. Built almost entirely by Murtaza, the lead developer.
- The site's own code calls no AI service. Lotte and Florence (sections
  2 and 3) do the AI work and use the site's public API to read and
  make posts.
- Unchecked: the code names Mailjet as its email-sending service; the
  live site has also used Mailgun. Which one the live site uses now.

Needpedia's three AI assistants, Florence, Lotte and Adele, are named
after librarians who resisted fascism.

## 2. Florence, the greeter

- What it does: the AI assistant that greets visitors who are not
  logged in, answers questions and helps them decide whether to join.
- Code: https://github.com/Queuevius/needpedia-greeter-production
- Runs on: Vercel (a website hosting service), from Tony's account.
  Live at https://needpedia-greeter-production.vercel.app
- Needs: a Vercel account (or other hosting), an OpenRouter account.
- AI: OpenRouter, checked in the code 1 October 2026. It uses OpenAI's
  free software toolkit pointed at OpenRouter's address with an
  OpenRouter key, so it needs no OpenAI account.
- To switch her to another AI service: change three settings, the
  service's address (OPENROUTER_BASE_URL), its key (OPENROUTER_API_KEY)
  and the model (OPENROUTER_MODEL). No code change.
- Her project's front page (README) lists every setting she reads and
  what it does. Rewritten 1 October 2026 to match the code.
- Rebuild instructions: not written yet.
- Status: live. Last updated 20 August 2026, when conversation saving
  was added.
- Unchecked: how needpedia.org reaches it; the Needpedia code never
  names its address.

## 3. Lotte, the main assistant

- What it does: the AI assistant for logged-in users. Finds, creates
  and edits posts for them, in many languages.
- Code: https://github.com/Queuevius/needpedia-assistant-production
- Runs on: Vercel, from Tony's account.
  Live at https://needpedia-assistant-production.vercel.app
- Needs: a Vercel account (or other hosting), an OpenRouter account.
- AI: OpenRouter, checked in the code 1 October 2026, with a setting
  for a full model and one for a cheaper "eco" model. No OpenAI account
  needed.
- To switch her to another AI service: her service's address is written
  into her code, in app/api/chat/route.ts
  (baseURL: 'https://openrouter.ai/api/v1'). Change that one line, then
  her key (OPENROUTER_API_KEY) and model settings.
- Rebuild instructions: not written yet.
- Status: live. Last updated 20 August 2026.
- Unchecked: same as Florence.

## 4. Adele and the public email page (Public Coms)

- What it does: a public web page showing the mail of the volunteer
  coordination address, VC@Needpedia.org, with the AI assistant Adele
  working in it. Public on purpose, so anyone can see what volunteers
  and leaders are doing. New senders' mail stays private until they
  agree to it being shown.
- Code: https://github.com/Queuevius/vc-email
- Runs on: Vercel, from Tony's account.
  Live at https://vc-email-five.vercel.app/inbox
- Needs: a Vercel account (or other hosting), an email mailbox the page
  can sign in to, an AI account.
- Rebuild instructions: not written yet.
- Status: live.

## 5. The phone notification app

- What it does: tells people on their phones when there is activity
  they care about, so they come back, collaborate and build
  communities. The site side already sends alerts for private messages
  and edits to tracked posts.
- Code: https://github.com/Queuevius/Needpedia-phone-app
- Runs on: people's phones, plus a Google notification project that
  delivers the alerts.
- Needs: a Google account with its own notification project.
- Rebuild instructions: not written yet.
- Status: not published yet.

## 6. The test sites

- What it does: runs several separate copies of Needpedia on one
  machine, each at its own web address, so volunteers can show work in
  progress before it goes to the lead developer for review.
- Code: https://github.com/Queuevius/needpedia-test-sites
- Runs on: any Linux computer with Docker and at least 4 GB of memory.
  One idle copy uses about 490 MB.
- Rebuild instructions:
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Test-Site-Package.md
- Status: working, tested 30 September 2026. Built by John Sunday.

## 7. The Nexus

- What it does: Needpedia's own document server, at
  https://nexus.needpedia.org. Holds the reference articles, the
  botskill posts (behaviour guides for AI assistants), the AI studios
  where volunteers work with an assistant, an activity page watching
  needpedia.org, and an admin chat.
- Code: on Tony's desktop computer only. Not online yet. Keys must be
  taken out before it goes online.
- Runs on: an ordinary Linux desktop. A web server in Docker, a small
  Python program for admin features, and Cloudflare Tunnel, which makes
  a home computer reachable at a web address.
- Needs: a computer that stays on, a domain name, a Cloudflare account,
  an AI account.
- Rebuild instructions: not written yet.
- Status: live.

## 8. The thread system

- What it does: a way of working with many AI chats at once, one per
  project ("threads"). Each thread keeps a public prompt accomplice
  (its standing facts and rules) and public posts where other threads
  leave it news, all run by one small script.
- How it works, in full:
  https://nexus.needpedia.org/working-with-tony.html
- Code: public copies of the two scripts:
  https://nexus.needpedia.org/botcouncil/threads-script.txt
  https://nexus.needpedia.org/botcouncil/make-tony-page-script.txt
- Runs on: any computer with Python, publishing to a web folder.
- In the seed: one thread for each part of the system, plus one for the
  person's own ideal workflow. Tony's note: for him it turned out more
  practical to work on his workflow as he used the other threads.
  Still, you never know.
- Rebuild instructions: a general starter kit is planned (offered to
  John as a job, 30 September 2026).
- Optional add-on, the Chrome capture extension: saves Claude
  conversations into the Nexus sidebar. Code on Tony's desktop only.

## 9. AI

- All of Needpedia's AI goes through OpenRouter, one account that
  reaches many AI models. Checked in Florence's and Lotte's code on
  1 October 2026.
- Recommended model: DeepSeek V4 v0813. Very cheap, and it can run on
  European servers that protect user data.
- You can use a different AI setup. Any AI service that accepts the
  same kind of messages works: another provider, a model's own maker,
  or a model running on your own computer. Florence switches by
  changing settings; Lotte by changing one line of code (sections 2
  and 3). Leaving OpenRouter out this way has not been tried yet.

## 10. Domain names

- needpedia.org and nexus.needpedia.org. Needpedia's are registered
  with IONOS, with their address records at Cloudflare.
- A new person chooses their own.

## 11. Other places Needpedia lives

- Developer wiki: https://github.com/Queuevius/Needpedia/wiki
- Developer group with paid tasks: https://needpedia.org/groups/10
- Discord: https://discord.gg/B7VNVQmHwG
- Nonprofit records (articles of incorporation, bylaws, board,
  conflict-of-interest policy):
  https://nexus.needpedia.org/Articles/Nonprofit%20Documents%20for%20Needpedia/
- Fiscal sponsor: The Know Agenda Foundation.

## 12. Documents copied into the seed

Copied in as files, not links, so an AI unpacking the seed can read
them even if these addresses stop working:
- The reference articles: https://nexus.needpedia.org/articles/index.txt
- The botskill posts: https://nexus.needpedia.org/botskills/index.txt
- The glossary: https://nexus.needpedia.org/articles/glossary.html
- Core facts: https://nexus.needpedia.org/articles/core-facts.html
- The capabilities file:
  https://nexus.needpedia.org/needpedia-capabilities.txt
- How to work with Tony and the thread system:
  https://nexus.needpedia.org/working-with-tony.html
- This inventory.

## 13. Old work

Whole systems no longer in use, kept so nothing is lost:
- https://github.com/Queuevius/Assistant : Needpedia's first AI
  assistant. Last changed March 2024. Not running anywhere.
- https://github.com/Queuevius/npdragonfly : the start of a radically
  transparent messaging system. It became the public email page
  (section 4).

## 14. Left out

- The Scrap-Yard projects and layout_fe: early work, used nowhere.
- The scheduler. We had to create our own scheduling app due to others
  not letting us schedule at any time. Needpedia's so international
  that wouldn't work. Its code was not kept. There are many scheduling
  apps to choose from, and an AI can build a custom one.

## 15. Making it your own

- Whoever sprouts the seed will have to edit their "about us" section
  too.
- The contacts below are Needpedia's people, not yours.

## 16. Other copies of the seed

Others may have unpacked this seed and kept copies online. Look for
them before starting from scratch.

## 17. Contacts

In case any of us are still around and available:
- Designer and founder: Tony Brasher, anthonydunn97202@gmail.com
- Lead Dev: Murtaza (GitHub: murtazazarkhwan), murtazazarkhwan@gmail.com
  He built almost all of needpedia.org.
- New support staff / freelancer: John Sunday (GitHub: eberechi10),
  eberechukwunemeremjohnsunday@gmail.com. He built the test sites.

Needpedia's addresses:
- Info@Needpedia.org : general
- Needpedia@gmail.com : general, and private or anonymous matters
- VC@Needpedia.org : volunteer coordination (shown publicly)

----- archived 2026-10-01 | from POST | file needpedia-inventory.txt | tags: inventory, edition-3, project-seed -----
NEEDPEDIA INVENTORY

Every system, account and piece of code that makes up Needpedia: what it
is, what it does, where its code lives, what it runs on, and where its
rebuild instructions are. Part of the project seed: a public package
anyone can unpack, with an AI's help, to run their own independent
version of all of this.

Edition 3, 1 October 2026. Written by the JOHN thread with Tony Brasher.
New in edition 3: the assistants' knowledge bases (section 9); a note
in the contacts (section 17).
Canonical copies:
https://nexus.needpedia.org/needpedia-inventory.txt
https://github.com/Queuevius/Needpedia/wiki/Needpedia-Inventory

Public. No passwords, keys or private contact details are in here, and
none ever go in. Handing over Needpedia's own accounts is a separate job.

Each entry has some of these:
- What it does
- Code: where the code lives
- Runs on: what keeps it running
- Needs: accounts a new person would make for their own version
- Rebuild instructions: where they are, or "not written yet"
- Status


## 1. needpedia.org, the main site

- What it does: a civic collaboration site. People post a Subject, the
  Problems within it and Ideas to solve them, and work on them together
  with groups, task cards, note/question/debate tokens, ratings and a
  time bank.
- Every feature, what it does and whether it works:
  https://nexus.needpedia.org/needpedia-capabilities.txt
- Where each feature lives in the code:
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Repo-Map.md
- Code: https://github.com/Queuevius/Needpedia
- Runs on: a rented server at Amazon Web Services. Built with Ruby on
  Rails (a framework for websites), a PostgreSQL database, and a
  background worker for slow jobs.
- Needs: a server, a domain name, an email-sending service (for
  account confirmations and password resets), a Mapbox account (the
  map on location posts), an AI account (see section 9).
- Not in the code: some content lives only in the site's database and
  is entered through the admin pages: the assistants' instructions,
  email templates, how-tos, FAQs, page pop-up guides, homepage
  messages. A new empty site starts without them. Export: not done yet.
- Rebuild instructions: not written yet. The test-site package (section
  6) builds the whole site from scratch and is the closest thing.
- Status: live. Built almost entirely by Murtaza, the lead developer.
- The site's own code calls no AI service. Lotte and Florence (sections
  2 and 3) do the AI work and use the site's public API to read and
  make posts.
- Unchecked: the code names Mailjet as its email-sending service; the
  live site has also used Mailgun. Which one the live site uses now.

Needpedia's three AI assistants, Florence, Lotte and Adele, are named
after librarians who resisted fascism.

## 2. Florence, the greeter

- What it does: the AI assistant that greets visitors who are not
  logged in, answers questions and helps them decide whether to join.
- Code: https://github.com/Queuevius/needpedia-greeter-production
- Runs on: Vercel (a website hosting service), from Tony's account.
  Live at https://needpedia-greeter-production.vercel.app
- Needs: a Vercel account (or other hosting), an OpenRouter account.
- AI: OpenRouter, checked in the code 1 October 2026. It uses OpenAI's
  free software toolkit pointed at OpenRouter's address with an
  OpenRouter key, so it needs no OpenAI account.
- To switch her to another AI service: change three settings, the
  service's address (OPENROUTER_BASE_URL), its key (OPENROUTER_API_KEY)
  and the model (OPENROUTER_MODEL). No code change.
- Her project's front page (README) lists every setting she reads and
  what it does. Rewritten 1 October 2026 to match the code.
- Rebuild instructions: not written yet.
- Status: live. Last updated 20 August 2026, when conversation saving
  was added.
- Unchecked: how needpedia.org reaches it; the Needpedia code never
  names its address.

## 3. Lotte, the main assistant

- What it does: the AI assistant for logged-in users. Finds, creates
  and edits posts for them, in many languages.
- Code: https://github.com/Queuevius/needpedia-assistant-production
- Runs on: Vercel, from Tony's account.
  Live at https://needpedia-assistant-production.vercel.app
- Needs: a Vercel account (or other hosting), an OpenRouter account.
- AI: OpenRouter, checked in the code 1 October 2026, with a setting
  for a full model and one for a cheaper "eco" model. No OpenAI account
  needed.
- To switch her to another AI service: her service's address is written
  into her code, in app/api/chat/route.ts
  (baseURL: 'https://openrouter.ai/api/v1'). Change that one line, then
  her key (OPENROUTER_API_KEY) and model settings.
- Rebuild instructions: not written yet.
- Status: live. Last updated 20 August 2026.
- Unchecked: same as Florence.

## 4. Adele and the public email page (Public Coms)

- What it does: a public web page showing the mail of the volunteer
  coordination address, VC@Needpedia.org, with the AI assistant Adele
  working in it. Public on purpose, so anyone can see what volunteers
  and leaders are doing. New senders' mail stays private until they
  agree to it being shown.
- Code: https://github.com/Queuevius/vc-email
- Runs on: Vercel, from Tony's account.
  Live at https://vc-email-five.vercel.app/inbox
- Needs: a Vercel account (or other hosting), an email mailbox the page
  can sign in to, an AI account.
- Rebuild instructions: not written yet.
- Status: live.

## 5. The phone notification app

- What it does: tells people on their phones when there is activity
  they care about, so they come back, collaborate and build
  communities. The site side already sends alerts for private messages
  and edits to tracked posts.
- Code: https://github.com/Queuevius/Needpedia-phone-app
- Runs on: people's phones, plus a Google notification project that
  delivers the alerts.
- Needs: a Google account with its own notification project.
- Rebuild instructions: not written yet.
- Status: not published yet.

## 6. The test sites

- What it does: runs several separate copies of Needpedia on one
  machine, each at its own web address, so volunteers can show work in
  progress before it goes to the lead developer for review.
- Code: https://github.com/Queuevius/needpedia-test-sites
- Runs on: any Linux computer with Docker and at least 4 GB of memory.
  One idle copy uses about 490 MB.
- Rebuild instructions:
  https://raw.githubusercontent.com/wiki/Queuevius/Needpedia/Needpedia-Test-Site-Package.md
- Status: working, tested 30 September 2026. Built by John Sunday.

## 7. The Nexus

- What it does: Needpedia's own document server, at
  https://nexus.needpedia.org. Holds the reference articles, the
  botskill posts (behaviour guides for AI assistants), the AI studios
  where volunteers work with an assistant, an activity page watching
  needpedia.org, and an admin chat.
- Code: on Tony's desktop computer only. Not online yet. Keys must be
  taken out before it goes online.
- Runs on: an ordinary Linux desktop. A web server in Docker, a small
  Python program for admin features, and Cloudflare Tunnel, which makes
  a home computer reachable at a web address.
- Needs: a computer that stays on, a domain name, a Cloudflare account,
  an AI account.
- Rebuild instructions: not written yet.
- Status: live.

## 8. The thread system

- What it does: a way of working with many AI chats at once, one per
  project ("threads"). Each thread keeps a public prompt accomplice
  (its standing facts and rules) and public posts where other threads
  leave it news, all run by one small script.
- How it works, in full:
  https://nexus.needpedia.org/working-with-tony.html
- Code: public copies of the two scripts:
  https://nexus.needpedia.org/botcouncil/threads-script.txt
  https://nexus.needpedia.org/botcouncil/make-tony-page-script.txt
- Runs on: any computer with Python, publishing to a web folder.
- In the seed: one thread for each part of the system, plus one for the
  person's own ideal workflow. Tony's note: for him it turned out more
  practical to work on his workflow as he used the other threads.
  Still, you never know.
- Rebuild instructions: a general starter kit is planned (offered to
  John as a job, 30 September 2026).
- Optional add-on, the Chrome capture extension: saves Claude
  conversations into the Nexus sidebar. Code on Tony's desktop only.

## 9. AI

- All of Needpedia's AI goes through OpenRouter, one account that
  reaches many AI models. Checked in Florence's and Lotte's code on
  1 October 2026.
- Recommended model: DeepSeek V4 v0813. Very cheap, and it can run on
  European servers that protect user data.
- You can use a different AI setup. Any AI service that accepts the
  same kind of messages works: another provider, a model's own maker,
  or a model running on your own computer. Florence switches by
  changing settings; Lotte by changing one line of code (sections 2
  and 3). Leaving OpenRouter out this way has not been tried yet.

Knowledge bases (KBs): each assistant's instructions and background
knowledge, written in plain language. They are not in the assistants'
code.
- Florence and Lotte: stored in needpedia.org's database, written and
  saved in versions on the master admin page "Ai Prompts" (proposed new
  name "AI KBs"). Each time someone talks to her, Florence asks the site
  for the version that is switched on, at
  /api/v1/ai_prompt?ai_type=Florence&token=(the prompt token).
- Adele: her main instruction sheet is stored in Upstash (an online
  storage service the email page uses) and edited on the email page's
  "Update KB" page, logged in as admin. A short set of built-in
  instructions also sits in her code (src/lib/ai.ts).
- In the seed: copies of all three, version 2.2, dated 24 and 25 July
  2026, taken from Tony's saved files. The live versions may have been
  changed since then.

## 10. Domain names

- needpedia.org and nexus.needpedia.org. Needpedia's are registered
  with IONOS, with their address records at Cloudflare.
- A new person chooses their own.

## 11. Other places Needpedia lives

- Developer wiki: https://github.com/Queuevius/Needpedia/wiki
- Developer group with paid tasks: https://needpedia.org/groups/10
- Discord: https://discord.gg/B7VNVQmHwG
- Nonprofit records (articles of incorporation, bylaws, board,
  conflict-of-interest policy):
  https://nexus.needpedia.org/Articles/Nonprofit%20Documents%20for%20Needpedia/
- Fiscal sponsor: The Know Agenda Foundation.

## 12. Documents copied into the seed

Copied in as files, not links, so an AI unpacking the seed can read
them even if these addresses stop working. Also copied in: the three
assistants' knowledge bases (section 9).
- The reference articles: https://nexus.needpedia.org/articles/index.txt
- The botskill posts: https://nexus.needpedia.org/botskills/index.txt
- The glossary: https://nexus.needpedia.org/articles/glossary.html
- Core facts: https://nexus.needpedia.org/articles/core-facts.html
- The capabilities file:
  https://nexus.needpedia.org/needpedia-capabilities.txt
- How to work with Tony and the thread system:
  https://nexus.needpedia.org/working-with-tony.html
- This inventory.

## 13. Old work

Whole systems no longer in use, kept so nothing is lost:
- https://github.com/Queuevius/Assistant : Needpedia's first AI
  assistant. Last changed March 2024. Not running anywhere.
- https://github.com/Queuevius/npdragonfly : the start of a radically
  transparent messaging system. It became the public email page
  (section 4).

## 14. Left out

- The Scrap-Yard projects and layout_fe: early work, used nowhere.
- The scheduler. We had to create our own scheduling app due to others
  not letting us schedule at any time. Needpedia's so international
  that wouldn't work. Its code was not kept. There are many scheduling
  apps to choose from, and an AI can build a custom one.

## 15. Making it your own

- Whoever sprouts the seed will have to edit their "about us" section
  too.
- The contacts below are Needpedia's people, not yours.

## 16. Other copies of the seed

Others may have unpacked this seed and kept copies online. Look for
them before starting from scratch.

## 17. Contacts

In case any of us are still around and available. If we're still
around, we might have all kinds of useful updates to share.
- Designer and founder: Tony Brasher, anthonydunn97202@gmail.com
- Lead Dev: Murtaza (GitHub: murtazazarkhwan), murtazazarkhwan@gmail.com
  He built almost all of needpedia.org.
- New support staff / freelancer: John Sunday (GitHub: eberechi10),
  eberechukwunemeremjohnsunday@gmail.com. He built the test sites.

Needpedia's addresses:
- Info@Needpedia.org : general
- Needpedia@gmail.com : general, and private or anonymous matters
- VC@Needpedia.org : volunteer coordination (shown publicly)
