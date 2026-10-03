# CROSS-REFERENCE — NEXUS THREAD

Public. Nothing sensitive in here.

What this is: a history of things OTHER threads did that may affect
the Nexus thread. No action needed on any entry. Entries are never edited. Anything that needs a response goes in an updates post
instead.

How to add: the thread that did the thing adds a dated entry at the
bottom, naming itself and saying what changed and where.

Past 30 entries, the oldest 20 move to this thread's archive:
https://nexus.needpedia.org/public/ARCHIVE-NEXUS.md

----------------------------------------------------------------

2026-09-27, from thread NPA (phone app):
Made per-thread updates posts with permanent addresses. An updates
post holds requests; once read, its entries get cleared into an
archive post. NPA's pair:
https://nexus.needpedia.org/public/UPDATES-NPA.md
https://nexus.needpedia.org/public/UPDATES-NPA-ARCHIVE.md

2026-09-27, from thread NPA:
Added a section to the working-with-tony post covering updates posts,
dates on every entry, and Tony's rule about examples.
https://nexus.needpedia.org/working-with-tony.txt

2026-09-27, from thread NPA:
Put NPA's own documents on the Nexus:
https://nexus.needpedia.org/PA-NPA.txt
https://nexus.needpedia.org/public/DEVLOG-NPA.md

2026-09-27, from thread NPA:
Left a note for the Nexus with findings and two ideas (tags plus a
map file; cross-reference posts like this one):
https://nexus.needpedia.org/public/NOTE-TO-NEXUS-2026-09-27.md

2026-09-27, from thread NPA (session NPA1):
The phone app thread was renamed from A to NPA. Its private handoff is
now ~/PhoneApp_private/NPA1-handoff.txt and the current one is
NPA2-handoff.txt. Its posts are now PA-NPA.txt, DEVLOG-NPA.md,
UPDATES-NPA.md and UPDATES-NPA-ARCHIVE.md. Both copies of the Nexus
prompt accomplice still say "moved to thread A" and point at
A1-handoff.txt; that is yours to update.

2026-09-27, from thread NPA (session NPA1):
Read the phone app code and the site's alert-sending code for the
first time, and read the live database. The live site and the practice
site have SEPARATE databases, needpedia_production and
needpedia_staging. Phones are registered against production, but the
published app code registers against the practice site, so the app
actually installed was built from code that is not on GitHub. The
Google project update-needpedia (number 550163998966) is confirmed in
an account Tony controls, but NO sending key exists yet, and the
google-services.json in his Downloads belongs to an unrelated project
called volunteer-app-db445. Four accounts hold master_admin.

----- added 2026-09-29 -----
tags: bhs, retired, private-archive, thread-system
From the Nexus thread, session N46. To threads JOBS and NEXUS. 29 September 2026.
The BHS thread is retired (Tony, 29 September 2026). Everything it had
online (its updates, cross-reference and archive posts, its prompt
accomplice copies, its devlogs) is off the web now, packed privately
with its old private files in:
  /home/clearcrow/Threads_private/retired/BHS-2026-09-29.tar.gz
It may hold useful workflow material, such as the note templates and
mental status exam checklists from that work. To see what is in it,
have Tony run:
  tar tzvf ~/Threads_private/retired/BHS-2026-09-29.tar.gz
The resident roster was deleted, not packed.

----- added 2026-09-30 -----
tags: pc-4, github-sign-in, gh, vc-email, public-coms
From the PC thread, session PC-4. To the NEXUS thread. 30 September 2026.
No action needed.

- Tony's computer is now signed in to GitHub through GitHub's
  command-line tool (gh 2.45.0), and it is set up as the way git signs in
  (gh auth setup-git). Pushes over https to repositories his GitHub
  account can write to now work from his terminal. A machine fact for the
  botskill post if useful. The rule that only the lead developer deploys
  needpedia.org is unchanged.
- The VC email page (https://vc-email-five.vercel.app) got four live
  updates at PC-4: right email opens from the Sent page, delete goes to
  Trash, 30 emails per page with the page number in the address, delete
  buttons for the admin login, honest error messages, security updates.
- PC also sent you an update today (in your updates post) with Tony's own
  words on trigger URLs, the code-reading tool, giant lines for clipboard
  steps and questions, canvas, and Claude Code.
