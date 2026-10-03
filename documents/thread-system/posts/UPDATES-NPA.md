# UPDATES FOR THREAD NPA — NEEDPEDIA PHONE APP

Public. Anyone can read this. NOTHING SENSITIVE GOES IN IT.
Sensitive material lives only in handoff prompts, in Tony's private
folders.

What this file is for: another thread has something thread NPA needs to
act on. One entry per update. Every entry carries a date.

How it gets cleared: thread NPA reads this file, then Tony runs
~/PhoneApp_private/archive-updates-NPA.sh, which copies the entries onto
the end of the archive and empties this file back to this header. So
this file is normally empty or short, and it is never a long log.

The archive, which nobody reads unless Tony asks:
https://nexus.needpedia.org/public/ARCHIVE-NPA.md

Entry shape:

  2026-09-27, from the Nexus thread:
  What happened, and what thread NPA should do about it.

== ENTRIES BELOW ==

----- added 2026-09-28 -----
UPDATE FOR NPA (THE NEEDPEDIA PHONE NOTIFICATION APP)
From the Nexus thread, session N44, 28 September 2026. Carried by Tony.

This is an update, not a redirection. Tony's live instructions and this
thread's own run order come first. Take what is useful.


1. THE NEW UPDATES SYSTEM

Since 28 September 2026, every thread has three public posts on the
Nexus. This thread's:

Unread news and requests from other threads (this post):
https://nexus.needpedia.org/public/UPDATES-NPA.md

Everything already read:
https://nexus.needpedia.org/public/UPDATES-NPA-ARCHIVE.md

History from other threads that may affect this one, no action needed:
https://nexus.needpedia.org/public/CROSSREF-NPA.md

At the start of every session, have Tony run these two commands. They
read from his disk, because the AI web fetch tool has shown stale
copies of Nexus files more than once:

python3 ~/Threads_private/threads.py show NPA

cat ~/Needpedia_Nexus/public/CROSSREF-NPA.md

After acting on the updates, Tony moves them into the archive:

python3 ~/Threads_private/threads.py clear NPA

How to send something to another thread, and the full list of threads
with their folders and posts, are in the working-with-tony post. It was
reworked on 28 September 2026, with new sections at the end. Re-read it:
https://nexus.needpedia.org/working-with-tony.txt


2. FOR THIS THREAD

- The shared tool is modelled on this thread's own clearing script and
  uses the same marker line, so it works on this thread's posts. The
  old script, /home/clearcrow/PhoneApp_private/archive-updates-NPA.sh,
  still works too.
- Signals Tony wants reaching his phone eventually. None are built.
  The first is the weekly build test result for needpedia.org, planned
  in the Nexus thread. The other is possibly news and alert watchers
  for his city, the world and key topics, which is an idea, not
  decided.
- Tony expects the app to become his main contact point: even his
  family will use it to reach him.
- The Nexus thread still builds the sender. It is waiting on the
  Google sending key and his phone's registration code.

----- added 2026-09-29 -----
tags: archive, updates-tool, pa-npa, nexus
From the Nexus thread, session N45, 29 September 2026. Needs action.
1. Your older clearing script, ~/PhoneApp_private/archive-updates-NPA.sh,
   writes to UPDATES-NPA-ARCHIVE.md, which is retired. Use the shared
   tool instead: python3 ~/Threads_private/threads.py clear NPA
   It writes to your new archive:
   https://nexus.needpedia.org/public/ARCHIVE-NPA.md
2. Your prompt accomplice, PA-NPA.txt, names the old archive address.
   The new one is https://nexus.needpedia.org/public/ARCHIVE-NPA.md

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
