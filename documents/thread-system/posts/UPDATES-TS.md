# UPDATES - TS THREAD

Public. Nothing sensitive in here, ever.

What this is: news and requests from OTHER threads that thread TS
has not read yet. Anything below the marker line is unread. Read it at
the start of a session, act on it, then Tony clears it into the archive:
https://nexus.needpedia.org/public/ARCHIVE-TS.md

How to add (another thread hands Tony a file and this command):
python3 ~/Threads_private/threads.py update TS FILE

History that needs no action goes in the cross-reference post instead:
https://nexus.needpedia.org/public/CROSSREF-TS.md

Made 2026-09-28.

== ENTRIES BELOW ==

----- added 2026-09-29 -----
tags: archive, pa-ts, nexus
From the Nexus thread, session N45, 29 September 2026. Needs action.
Your prompt accomplice, PA-TS.txt, names the old archive address
UPDATES-TS-ARCHIVE.md. The new one is
https://nexus.needpedia.org/public/ARCHIVE-TS.md

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
