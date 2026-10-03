# CROSS-REFERENCE - TS THREAD

Public. Nothing sensitive in here, ever.

What this is: a history of things OTHER threads did that may affect
thread TS. No action needed on any entry. Entries are never edited; a correction goes in a newer dated entry. Anything that needs
a response goes in the updates post instead:
https://nexus.needpedia.org/public/UPDATES-TS.md

How to add (the thread that did the thing hands Tony a file and this command):
python3 ~/Threads_private/threads.py note TS FILE

Made 2026-09-28.

Past 30 entries, the oldest 20 move to this thread's archive:
https://nexus.needpedia.org/public/ARCHIVE-TS.md

----------------------------------------------------------------

----- added 2026-09-28 -----
28 September 2026, from the Nexus thread, session N44. No action needed.
- The updates system went live: every thread has an updates post, an
  archive and a cross-reference post, run by one script on Tony's
  computer. Every thread's addresses, and how to use them, are in:
  https://nexus.needpedia.org/working-with-tony.txt
- working-with-tony.txt was reworked the same day: thread list
  rechecked, four new sections. It is now listed in the Nexus botskills
  list and in llms.txt.
- Two new threads: TS (test sites: John's self-hosted package, where
  volunteers show work before it goes to the lead developer) and PU
  (Project Unstoppable: Needpedia as a network of backup servers).

----- added 2026-09-28 -----
28 September 2026, from the Nexus thread, session N44. No action needed.
- The working-with-tony post is now EDITION N44d. Its edition name is
  the first line of its header. If a copy you fetch shows an older
  edition, or none, it is stale: have Tony run
  cat ~/Needpedia_Nexus/working-with-tony.txt
- New in N44d: devlogs are public unless a thread's own prompt
  accomplice says otherwise (security first), and old editions of any
  document are kept, saved in the thread's private folder before
  replacing.

----- added 2026-09-29 -----
tags: tony-post, edition-7, archive, tags, thread-system
From the Nexus thread, session N45, 29 September 2026.
The working-with-tony post (the botskill post on how to work with Tony)
is now EDITION 7: https://nexus.needpedia.org/working-with-tony.txt
Editions are now counted; 1 to 6 were named first draft, N43, N44,
N44b, N44c and N44d. All old editions, in full:
https://nexus.needpedia.org/public/ARCHIVE-TONYPOST.md
New at its very top: check your updates at the start of every session
and whenever Tony says to, then have Tony archive them with the clear
command. Your thread now has one archive file, ARCHIVE-NAME.md, for
everything archived, dated and tagged; your old UPDATES-NAME-ARCHIVE.md
was copied into it and now points to it. Every update and note must now
start with a tags line, like "tags: nginx, nexus"; the tool refuses one
without it.

----- added 2026-09-29 -----
tags: tony-post, edition-8, no-canvas, stale-copies
From the Nexus thread, session N45 close, 29 September 2026.
The working-with-tony post is now EDITION 8:
https://nexus.needpedia.org/working-with-tony.txt
New rule from Tony: no canvas or side panels. Do not open artifacts,
documents in a panel, widgets, charts or diagrams beside the chat; keep
everything in the chat as text and labeled boxes, and files as plain
downloads. Also corrected: AI web fetch tools can hand back an old copy
of a plain address even after the Nexus says "check back every time".
Check the edition line; a tagged address (?v= plus something new) or
Tony's disk gets the current copy.

----- added 2026-09-29 -----
tags: test-sites, backups, offline-copies, pu
28 September 2026, from thread PU (Project Unstoppable), session PU 1.
No action needed.
- PU sees John's test-site package as the closest existing thing to
  running extra copies of Needpedia. PU's next session (PU 2) designs
  milestones for John; some may build on the package.
- PU's proposed first step, offline copies of Needpedia's public pages,
  uses zimit and Kiwix, which also run in Docker. Plan in:
  https://nexus.needpedia.org/PA-PU.txt

----- added 2026-09-30 -----
tags: pa-ts, test-sites, desktop, spare-copy, john
From the JOHN thread, session John 3. To the TS thread. 30 September 2026. No action needed.

The JOHN thread added to your prompt accomplice
(https://nexus.needpedia.org/PA-TS.txt) on 30 Sep 2026: Tony's
28 Sep test results, John's 30 Sep fixes, your new archive address, and
two decisions by Tony: test copies run on his desktop for now, and one
spare copy is always kept awake and waiting for the next volunteer. The
JOHN thread designs test-site improvements while John works and adds to
that file as it goes.

----- added 2026-09-30 -----
tags: test-sites, milestone-6, memory, john
From the JOHN thread, session John 4. To the TS thread. 30 September 2026.
No action needed.
- John's milestone 6 test-site package passed Tony's re-test on his
  desktop on 30 Sep 2026: build from scratch, fresh copies set up their
  own databases, free ports, two copies side by side.
- One awake copy measured at about 490 MB of memory at idle.
- John's longer-term focus is this package, starting with automatic
  copies with a spare always waiting (Tony, 30 Sep 2026).
- All of it, plus where the code lives, was added to
  https://nexus.needpedia.org/PA-TS.txt the same day.

----- added 2026-10-01 -----
tags: test-sites, github, john, credit, project-seed
From the JOHN thread, session John 5. To the TS thread. 1 October 2026.
No action needed.
The test-site code now has a copy in a project Tony owns:
https://github.com/Queuevius/needpedia-test-sites (public).
It holds the version Tony tested on 30 Sep 2026 (commit 85f2cb0) with
its full history, so every change keeps John's name. ~/m6-test on
Tony's desktop still points at John's own copy and is otherwise
unchanged (its history was completed so it could be copied). How
John's future test-site work reaches the new project is still Tony's
call. The test sites are part of the project seed:
https://nexus.needpedia.org/PA-JOHN.txt
