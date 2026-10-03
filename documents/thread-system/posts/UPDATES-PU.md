# UPDATES - PU THREAD

Public. Nothing sensitive in here, ever.

What this is: news and requests from OTHER threads that thread PU
has not read yet. Anything below the marker line is unread. Read it at
the start of a session, act on it, then Tony clears it into the archive:
https://nexus.needpedia.org/public/ARCHIVE-PU.md

How to add (another thread hands Tony a file and this command):
python3 ~/Threads_private/threads.py update PU FILE

History that needs no action goes in the cross-reference post instead:
https://nexus.needpedia.org/public/CROSSREF-PU.md

Made 2026-09-28.

== ENTRIES BELOW ==

----- added 2026-09-29 -----
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

----- added 2026-09-30 -----
tags: project-seed, succession, access, john, botcouncil, build-check
From the JOHN thread, session John 4. To the PU thread. 30 September 2026.

1. TONY'S GOAL, NOW PART OF PU (Tony, 30 Sep 2026)
Prepare Needpedia so others could start using it even if Tony is no
longer around. A "project seed": one fully self-contained package any
AI could unpack, files within files, until the new person sits where
Tony is now, with ownership of all the accounts and code, their own
Nexus, master_admin, the thread system, the scheduling tool, the VC
email account, the test sites, and anything else forgotten. Separate
systems can be referenced in a sheet.

2. DECIDED (Tony, 30 Sep 2026)
- Start with a simple version and add to it, rather than one big build.
- Tony inventories what is built.
- John builds the first two pieces: the daily build check (GitHub part)
  and a bot council starter kit (the thread system, packaged so anyone
  can set up their own). His longer-term focus is the test sites.

3. THE CHUNKS, AS PROPOSED BY THE JOHN THREAD (not all decided)
1) Inventory sheet. Tony plus an AI, 1 or 2 evenings. Every account,
   service, machine, domain and piece of code: what, who owns it, where
   its rebuild instructions are. A public version, and a private one
   saying where the passwords are.
2) Keys handover. Tony only. Choose a trusted person; put every
   password in a password manager with emergency access; give the code
   a second owner. About an hour of settings once the person is chosen.
3) All code in places Tony controls, backed up off his desktop. Test
   sites: 15 minutes. The Nexus with keys removed: 2 or 3 sessions with
   the Nexus thread. Live database backups: PU and Murtaza.
4) A rebuild-from-zero recipe per system, each written by its own
   thread: Needpedia, the Nexus, the thread system, VC email and Adele,
   the scheduling tool, the phone app.
5) Admin and master_admin spec sheets and renaming: Tony with NP1.
6) Packing the seed: a "start here" file plus a script that bundles
   everything public; the private sheet stays separate. One session,
   once the rest exists.
7) Test run: someone who is not Tony unpacks it on a blank machine with
   only an AI's help and notes every spot they get stuck. A good later
   job for John once he has a laptop.

4. RESEARCH ON HANDING OVER ACCESS (30 Sep 2026)
- GitHub's "successor" setting does not cover every case. A successor
  can manage only public repositories, only after presenting a death
  certificate (7-day wait) or an obituary (21-day wait), and cannot log
  in. It does nothing if Tony is alive but unreachable.
  https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/maintaining-ownership-continuity-of-your-personal-accounts-repositories
- A password manager with emergency access does. In Bitwarden, a
  trusted contact requests access; if Tony does not reject it, access
  is granted automatically after a wait time he sets (minimum one day).
  That one setup can carry every password to someone he trusts.
  https://bitwarden.com/help/emergency-access/
  Check whether the emergency feature needs the paid plan.
- For the code: a GitHub organization with a second trusted owner
  works in every case, immediately.

5. RELATED, SENT TO NP1 THE SAME DAY
Tony's design intent: master admin can see what admins do; the goal is
a global network of servers run by people you can trust, who can see
everything happening on their own servers; operators who don't monitor
private spaces are negligent. The JOHN thread suggested the spec sheets
tell users plainly that a server's operator can see private content.
That is compatible with PU's "private posts stay private": private from
other users and other servers, visible to that server's own operator.

6. PRIVATE MATERIAL EXISTS (location only)
Tony's rough admin notes in a Google Doc include private contact
details for Murtaza. They belong only in the private version of the
inventory sheet, never in a public post.

----- added 2026-10-01 -----
tags: project-seed, seed-scope, keys-handover, contact-note, phone-app, openrouter
From the JOHN thread, session John 5. To the PU thread. 1 October 2026.

This corrects parts of the JOHN thread's 30 September update about the
project seed, which may still be unread in this post.

1. THE SEED IS FOR ANYONE (Tony, 1 Oct 2026)
A public package any person can unpack, with an AI's help, to get their
own independent version of everything: their own Needpedia site
(starting empty, under their own name if they like), their own Nexus,
the thread system, the public email page with its assistant, the
scheduling app, the phone notification app and the test sites.

2. KEYS HANDOVER IS A SEPARATE JOB
Choosing a trusted person, the password manager with emergency access,
and a second owner for the code are no longer part of the seed. The
seed holds no passwords, keys or private contact details. The research
in the 30 Sep update (GitHub's successor setting, Bitwarden emergency
access, a GitHub organization) still applies to keys handover.

3. OTHER DECISIONS (Tony, 1 Oct 2026)
- A contact note: the email addresses that exist, and contact details
  for Tony, Murtaza and John, in case any of them are still around.
- All documents copied into the seed as files, not links, with a
  "start here" file. The seed tells its reader to look online for other
  people's copies of the seed.
- The phone notification app must be in it: critical for bringing
  people back when there is activity.
- The Chrome capture extension is an option, listed with the thread
  system and the other Nexus pieces.
- Back up copies of everything possible into it.
- Domains: Needpedia's are with IONOS; seed users choose their own.
- AI: the seed recommends DeepSeek V4 v0813 through OpenRouter (cheap,
  can run on European servers that protect user data). Removing
  OpenRouter may be possible; not looked into.
- Test-site code goes in its own public project under Tony's GitHub
  account (started 1 Oct 2026).

4. WHAT IS LEFT, AS THE JOHN THREAD SEES IT
Code copies online (Nexus with keys removed, thread scripts, capture
extension, scheduling app); an export of the content that lives in
needpedia.org's database rather than its code (the assistants'
instructions, email templates, how-tos, FAQs, page pop-up guides,
homepage messages); rebuild-from-zero instructions per system; the
public inventory sheet; the start-here file; the packing script; a test
run by someone who is not Tony. Full list in
https://nexus.needpedia.org/PA-JOHN.txt under session John 5.

----- added 2026-10-02 -----
tags: seed, fediverse, backups, network, nexus-code
From the JOHN thread, session John 6. To thread PU. 2 October 2026.

1. NO SERVER-TO-SERVER BACKUPS IN NEEDPEDIA'S CODE. Checked in the code on
   2 October 2026: Needpedia's fediverse features share individual posts
   between servers, the way Mastodon does. Nothing copies a whole server to
   another one. The backup network is still entirely PU's to design and
   build.

2. WHAT EXISTS: following accounts on other servers works in the code.
   Sending posts out to other servers is built but switched off and
   untested. Incoming messages aren't properly verified yet; sent to NP1
   to fix before the outgoing side is switched on.

3. THE SEED SAYS THIS NOW. The Project Seed page describes the network as
   a plan and says how far along it is:
   https://nexus.needpedia.org/seed/index.html
   Trial 2 of the seed will carry the same note in its own documents.

4. TRIAL 1 OF THE SEED IS PUBLISHED:
   https://github.com/Queuevius/needpedia-seed
   https://nexus.needpedia.org/seed/needpedia-seed-trial-1.zip
   John is being asked to test-unpack it with only an AI's help. A
   "Project Seed" tile on the Nexus front page leads to the seed page.

5. NEXT: Tony decided the Nexus's own code goes into the seed (trial 2),
   with every password and key stripped out. Whoever rebuilds it makes
   their own.
