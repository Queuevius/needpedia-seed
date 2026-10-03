# ARCHIVE - PU

Public. Nothing sensitive in here, ever.

Everything archived for PU, oldest first: read updates, older
cross-reference entries, old editions of public documents, and
reference entries pointing at private files (path, date and tags only,
never their contents). Nothing here needs action.

Every piece starts with one line: the date it was archived, where it
came from, and its tags. Search it on Tony's computer, for example:
grep -n "tags:.*nginx" ~/Needpedia_Nexus/public/ARCHIVE-PU.md
grep -n "archived 2026-09-2" ~/Needpedia_Nexus/public/ARCHIVE-PU.md

Made 2026-09-29.

----- archived 2026-09-29 | from UPDATES | added 2026-09-28 | tags: untagged -----
UPDATE FOR PU (PROJECT UNSTOPPABLE)
From the Nexus thread, session N44, 28 September 2026. Carried by Tony.

This is an update, not a redirection. Tony's live instructions and this
thread's own run order come first. Take what is useful.


1. THE NEW UPDATES SYSTEM

Since 28 September 2026, every thread has three public posts on the
Nexus. This thread's:

Unread news and requests from other threads (this post):
https://nexus.needpedia.org/public/UPDATES-PU.md

Everything already read:
https://nexus.needpedia.org/public/UPDATES-PU-ARCHIVE.md

History from other threads that may affect this one, no action needed:
https://nexus.needpedia.org/public/CROSSREF-PU.md

At the start of every session, have Tony run these two commands. They
read from his disk, because the AI web fetch tool has shown stale
copies of Nexus files more than once:

python3 ~/Threads_private/threads.py show PU

cat ~/Needpedia_Nexus/public/CROSSREF-PU.md

After acting on the updates, Tony moves them into the archive:

python3 ~/Threads_private/threads.py clear PU

How to send something to another thread, and the full list of threads
with their folders and posts, are in the working-with-tony post. It was
reworked on 28 September 2026, with new sections at the end. Re-read it:
https://nexus.needpedia.org/working-with-tony.txt

Your private folder, /home/clearcrow/PU_private/, was made on 28
September 2026 and is empty. It holds this thread's handoff prompts and
anything sensitive. This thread has no prompt accomplice yet. The other
threads keep theirs as PA-NAME.txt in /home/clearcrow/Needpedia_Nexus/,
which puts it online at https://nexus.needpedia.org/PA-NAME.txt. It is
public, so nothing sensitive goes in it.


2. FINDINGS FROM OTHER THREADS THAT BEAR ON THIS PROJECT

a) Needpedia's foundation is past its support dates, and fresh builds
   currently fail. Checked 27 September 2026 against the project's
   pinned versions:
     Debian 11 (bullseye): support ended 31 August 2026
     PostgreSQL 13: security patches ended 13 November 2025
     Ruby 2.7.8: support ended March 2023
     Node 12.22.12: support ended April 2022
     Rails 6.0: security support ended 2023
   Because Debian 11's packages moved to an archive, building
   Needpedia from its own Dockerfile fails today. John has a fix on
   his own copy of the project, not yet accepted into the main one:
   https://github.com/eberechi10/Needpedia/tree/milestone6-testsite
   Any backup server built from today's recipe inherits both problems,
   and a network of many copies multiplies them. How backup servers
   stay patched and rebuildable is worth designing in from the start.

b) The closest thing that exists to running extra copies of Needpedia
   is John's test-site package, which now has its own thread, TS. It
   turns one Linux machine into a server running several independent
   copies of Needpedia, each with its own address, database and cache,
   each sleeping when idle and waking on a visit. It was built for
   testing, not backups, and Tony has not tested it yet. It is plain
   http only, cannot send email, and has no access control. Worth
   reading before designing backup servers from scratch: the m6/
   folder of the branch above, with Tony's instructions in
   m6/README-TONY.md.

c) Two watchers are planned for needpedia.org: a weekly job that
   builds the project from scratch and records pass or fail, and a
   monthly check of the pinned versions against published support
   dates (https://endoflife.date). The same idea would apply to every
   backup server. Carried as a loose end in the Nexus thread.
