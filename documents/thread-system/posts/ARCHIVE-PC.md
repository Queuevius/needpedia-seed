# ARCHIVE - PC

Public. Nothing sensitive in here, ever.

Everything archived for PC, oldest first: read updates, older
cross-reference entries, old editions of public documents, and
reference entries pointing at private files (path, date and tags only,
never their contents). Nothing here needs action.

Every piece starts with one line: the date it was archived, where it
came from, and its tags. Search it on Tony's computer, for example:
grep -n "tags:.*nginx" ~/Needpedia_Nexus/public/ARCHIVE-PC.md
grep -n "archived 2026-09-2" ~/Needpedia_Nexus/public/ARCHIVE-PC.md

Made 2026-09-29.

----- archived 2026-09-30 | from PA | file PA-PC.txt | tags: pa-pc, pc-3, before-pc-3-edit -----
== PROMPT ACCOMPLICE - PUBLIC COMS SYSTEM ==
Stable companion to the PC handoff prompt. Lives on Tony's computer at
~/PublicComs/prompt_accomplice_PC_2026-09-22_v2.txt
Holds nothing sensitive. Any AI may read it.
Last updated: 2026-09-22 (session PC-2)

REPLACES prompt_accomplice_PC_2026-09-22.txt, which said the mailbox was
Gmail / Google Workspace throughout. That was wrong. Delete the old file.


-- WHAT THIS SYSTEM IS --

A public communications system for Needpedia, an open-source nonprofit
civic collaboration platform. It is a web page that shows the mail for
the address VC@Needpedia.org, which stands for Volunteer Coordination.
Anyone can read the page without signing in. An AI assistant named
Adele sits on the page and answers questions about the mail. An admin
can send mail from it.

Live page: https://vc-email-five.vercel.app
Code: https://github.com/Queuevius/vc-email
Built with Next.js 16 and React 19, hosted on Vercel.
Confirmed live build: main branch, commit e8a9514, deployed 2026-07-27
by AdnanRailsCraft. The code in that repo is the code running.


-- WHERE THE MAILBOX ACTUALLY LIVES --

Zoho Mail. Not Gmail, not Google Workspace. The app signs in to
imappro.zoho.com. Tony's Google admin powers have nothing to do with
this mailbox and no Gmail setting affects it.

Zoho plan: Mail Lite, 10GB, paid and active. One license, one used.
Yearly. Expires 2026-12-09. If it lapses, program access to the
mailbox stops and the public page goes blank again.

Zoho admin console: https://mailadmin.zoho.com
Zoho webmail: https://mail.zoho.com

DNS for needpedia.org is at Cloudflare. Tony owns that account.


-- HOW IT WORKS TODAY, FROM READING THE ACTUAL CODE --

Read at PC-2 from src/services/emailService.ts.

There is no database. Nothing is stored anywhere.

Receiving: every time someone opens the page, the site signs in to the
Zoho mailbox using the standard mail-reading protocol (IMAP) and asks
for mail. The code computes a date 30 days back and asks only for mail
since then. It reads the folder named in a setting, currently INBOX.
Results are held in memory for 60 seconds.

The fetch limit setting is 500, but the 30-day window is hardcoded in
the source, not a setting. Changing it means changing code.

Sending: sends through a standard outgoing mail server, then tries to
copy the sent message back into the mailbox's sent folder so it shows
in the outbox. If that copy fails the code logs a warning and carries
on.

Deleting: an admin delete marks the message deleted and immediately
purges it. That permanently erases it from the real mail account. Not
trash. Gone.

Adele: sends up to 20 recent messages plus a "guidescript" instruction
sheet to an AI model through OpenRouter. The guidescript is stored in
an Upstash store. Her conversations get posted to needpedia.org.

Important about Adele: she does not look anything up. She only sees
what the app hands her. Anything she says about her own access comes
from the guidescript, not from checking. Do not treat her answers as
evidence about system state.

Settings all live as environment variables in the Vercel project.


-- WHAT WAS ACTUALLY WRONG, AND WHAT PC-1 GOT WRONG --

PC-1 concluded the mailbox was hiding mail because of a Gmail message
limit, and that the fix was a rebuild. Both were wrong.

The real cause: needpedia.org had NO mail-delivery records in DNS at
all. No MX records, no TXT records of any kind. Mail sent to
VC@Needpedia.org had nowhere to be delivered and died. Outbound was
unaffected because sending does not consult those records.

Confirmed by measurement, not inference: dig returned status NOERROR
with ANSWER 0 and a Cloudflare SOA, meaning the records genuinely did
not exist. Newest message in the Zoho inbox was 2026-04-22.

Mail sent to the address between 2026-04-22 and 2026-09-22 was never
delivered anywhere. It is not recoverable. There is no backlog waiting
to be pulled in.

The website was never broken. It was faithfully showing an empty
mailbox.

How the records disappeared is STILL UNKNOWN. Nobody deletes MX and
TXT records by accident. Until that is answered it can happen again.


-- WHAT WAS FIXED AT PC-2 --

All done in Cloudflare DNS. All confirmed live with dig.

MX records restored, pointing mail to Zoho:
  mx.zoho.com priority 10
  mx2.zoho.com priority 20
  mx3.zoho.com priority 50

Sender permission list (SPF) on needpedia.org:
  v=spf1 include:mailgun.org include:zohomail.com ip4:18.223.241.10 ~all

Sender permission list on www.needpedia.org:
  v=spf1 include:mailgun.org ~all
  (Mailgun is verified on www, not the root. NP-1 supplied this.)

Message signing (DKIM), selector vcaccount, 2048-bit:
  Name: vcaccount._domainkey
  Verified in Zoho, signing toggled ON.

Monitoring policy (DMARC):
  Name: _dmarc
  Value: v=DMARC1; p=none
  Monitoring only. Cannot cause any mail to be rejected.

End-to-end proof: a reply sent from VC@Needpedia.org to Tony's personal
Gmail on 2026-09-22 showed SPF PASS and DKIM PASS in Gmail's "Show
original" view. Inbound test mail arrived in Zoho and appeared on the
public page.

Note for later: DMARC has no reporting address, deliberately. Those
reports arrive daily as machine-readable attachments and would bury
real mail on a public page. If wanted later, send them elsewhere.


-- THE THREE DESIGN FLAWS, ALL STILL TRUE --

These were never the cause of the outage, but they are real and they
are why the outage went unnoticed for five months.

1. Mail older than 30 days is invisible, so the archive silently
   shrinks every day.
2. When the mailbox cannot be reached, the code catches the error,
   logs it where nobody looks, and returns an empty list. The page
   shows "no messages". Broken is indistinguishable from quiet. This
   is confirmed in the source, not suspected.
3. Nothing is stored anywhere. The page is only ever a window onto
   Zoho. Delete is permanent and immediate.


-- THE REBUILD: STATUS CHANGED AT PC-2 --

PC-1 decided on "Option 1" - the mail host keeps receiving and
sending, a small program copies every message into Needpedia's own
storage, and the page plus Adele read only that copy.

That decision still stands as a direction, but the urgency behind it
was based on a wrong diagnosis. The system is not broken now. The case
for rebuilding is the three design flaws above, not a crisis.

This should be revisited fresh at PC-3 rather than inherited as
momentum. Do not start building without Tony re-confirming.

Build plan as drafted at PC-1, kept for reference. Note that the
watcher section was written for Gmail and needs rewriting for Zoho:
  Storage: a hosted Postgres database for message text and details,
  plus Cloudflare R2 file storage for the untouched original message
  and attachments. Keeping big files out of the database keeps it
  small enough to stay free.
  Rules: write the untouched original to file storage FIRST, before
  parsing. Ignore repeats by matching each message's unique ID. Two
  grades of delete - reversible hiding from the public page, and a
  real erase for genuine privacy requests.
  Watcher: must read both received and sent folders. Must ask "what
  changed since last time" rather than re-reading everything, and must
  fall back to a full sweep automatically if the checkpoint is too old.
  Where it runs is unresolved: Nexus (free, stops when that machine is
  down, catches up after), GitHub's free scheduler (every few minutes),
  or paid Vercel at about $20/month.
  Sending: keep sending through Zoho and write our own copy of each
  sent message into the archive.


-- DECISIONS MADE, DO NOT REOPEN WITHOUT TONY --

PC-1: Option 1 over repair-only and over full independence.

PC-2: Every message shows on the public page as soon as it arrives.
No approval step. Paired with a one-click, reversible hide button for
spam and for personal information people send without realizing the
page is public.

PC-2: The website is the only place VC@Needpedia.org gets read. Nobody
opens the mailbox directly in an ordinary mail program. The mail host
is just the engine.


-- OPEN ITEMS --

How the DNS records disappeared. Unanswered. Can recur.

AdnanRailsCraft, the previous developer, deployed the July build and
may still have access to the Vercel project settings. Not yet removed.

Zoho plan expires 2026-12-09. Nothing breaks before then.

Whether any volunteer can write glue code, which decides how much of
any rebuild lands on Tony.

Mailgun has the Needpedia app's account switched off after a credential
was found exposed on GitHub. That is NP-1's work, not this thread's,
but it means the site's account-confirmation emails are still dead.
It did NOT cause the VC mailbox outage. Two separate failures that
overlapped in time.


-- THINGS ALREADY CHECKED, DO NOT REDO --

The vc-email repo was scanned at PC-2 for committed credentials. Clean.
Only placeholder values in .env.example. The exposed key Mailgun found
is in the Needpedia repo, not this one.

IMAP_USER in Vercel is VC@Needpedia.org, confirmed by reveal. The page
is not reading anyone's personal mailbox.

Signing in to the Zoho mailbox with the Vercel password works, tested
directly with curl. Returned 23 messages. Credentials are valid.


-- WORKING RULES FOR THIS THREAD --

Plain language is the top priority. Say what a thing IS and DOES in
everyday words before naming it, every time, even for things covered
in earlier sessions.

State the exact thing to use. Never say "use yours" or "the one you
picked" and expect Tony to recall it. He is following steps, not
tracking context. When he asks to start over, restart from step 1.

Declare session type at the top: look-only or build. Declared scope
outranks momentum. Never give action steps in a look-only session.

Design questions: surface options with their real-world effects. Don't
make executive decisions for Tony.

Read the actual code before describing it. Never infer from file or
branch names. State only what command output actually shows. After a
failed approach, one careful retry, then switch.

Never ask Tony to edit code by hand. Short change, one precise
terminal command. Long change, a helper script opened in gedit.

Label every paste box: TERMINAL, BROWSER, BROWSER CONSOLE, or GEDIT.
Prefer terminal versions. Long content goes via gedit, not terminal
heredocs.

When a file on Tony's computer is needed, give him a terminal command
to open or copy it. Do not leave him to work out how to retrieve it.
To open: gedit ~/path/to/file
To copy straight to clipboard: xclip -selection clipboard < ~/path/to/file

Explain what a destructive command removes, and what it doesn't,
before giving it.

Security: max speed, minimal hedging. No warnings about pasting keys
into chat. Flag only genuinely severe problems.

Documents get delivered as plain text files, never Word files. One
item per copy box. Bare URLs, no link formatting, no tables. Link
preview cards do not render as clickable for Tony.

Claude cannot put files on Tony's computer. Files land in his
Downloads and he moves them.

Tone: measured. No drama. "That changes a few things" beats "this
changes everything."


-- PEOPLE --

Tony Brasher, founder and president of Needpedia, owns every account
involved here. Legal name Anthony Brasher.
AdnanRailsCraft, previous developer, deployed the July build. May
still have access to the Vercel settings.
Murtaza, Needpedia's lead developer. Reachable but takes days.
Needpedia's own site AI can also be asked questions.


-- GLOSSARY, FOR ANY AI WRITING FOR TONY --

Don't use these names without first saying what the thing does.
  IMAP: the old way a program signs in to a mailbox and reads it.
  SMTP: the standard way mail gets sent out.
  MX record: the public note on a domain saying which server accepts
    its mail. Missing this means mail is never delivered.
  SPF: a public list of who is allowed to send mail using your domain
    name. Receiving servers read it to judge whether mail is forged.
  DKIM: a cryptographic signature on each outgoing message, checked
    against a key published on your domain.
  DMARC: instructions telling receiving servers what to do when a
    message fails the SPF and DKIM checks.
  Postgres: a database, meaning organized storage the website reads.
  R2: cheap file storage for whole files and attachments.
  Webhook: one program poking another the moment something happens.
  dig: a terminal command that looks up public DNS records.

----- archived 2026-09-30 | from UPDATES | added 2026-09-28 | tags: untagged -----
UPDATE FOR PC (PUBLIC COMS: THE VC@NEEDPEDIA.ORG INBOX PAGE)
From the Nexus thread, session N44, 28 September 2026. Carried by Tony.

This is the first real entry sent through the new updates system, so
it doubles as the system's test. Tony's live instructions and this
thread's own run order come first. Take what is useful.


1. THE NEW UPDATES SYSTEM (WHY YOU ARE READING THIS HERE)

Every thread now has three public posts on the Nexus. This thread's:

Unread news and requests from other threads (this post):
https://nexus.needpedia.org/public/UPDATES-PC.md

Everything already read:
https://nexus.needpedia.org/public/UPDATES-PC-ARCHIVE.md

History from other threads that may affect this one, no action needed:
https://nexus.needpedia.org/public/CROSSREF-PC.md

One shared script on Tony's computer runs these posts for every thread.
Each job is one short terminal command for Tony.

Read this thread's unread updates. Use this rather than a web fetch:
the AI web fetch tool has shown stale copies of Nexus files more than
once.
  python3 ~/Threads_private/threads.py show PC

After acting on the entries, Tony moves them into the archive:
  python3 ~/Threads_private/threads.py clear PC

To tell another thread something that needs action, hand Tony a file
plus this command, putting the thread's name in place of NAME:
  python3 ~/Threads_private/threads.py update NAME FILE

For history that needs no action, use its cross-reference post instead:
  python3 ~/Threads_private/threads.py note NAME FILE

Thread names: NEXUS, NP1, PC, JOHN, BHS, JOBS, TS, NPA.
Nothing sensitive ever goes in any of these posts. They are public.

Full working rules for every thread:
https://nexus.needpedia.org/working-with-tony.txt
(The Nexus thread is adding this system to it at session N44.)


2. PROBLEMS TONY FOUND IN THE INBOX PAGE (28 SEPTEMBER 2026)

- Looking at sent emails shows the wrong thing: random old emails
  from the inbox and outbox instead of what was sent.
- Attachments do not work, in or out.
- No rich formatting (bold, links, and so on), in or out.
- The chat button is redundant. The button labeled "Adele" already
  does the job and works fine.
- Tony needs to be able to delete emails once logged in.


3. A CONSENT STEP BEFORE MESSAGES GO PUBLIC

Tony's concern: the inbox is meant for volunteers, and everything in it
is public. Someone who did not read the volunteer post properly could
send something private, and Tony would hate for a person's resume to
end up online.

Tony's lean is "sender says yes," which he sees as the easiest to set
up and the most reliable:
  - The first email from an address nobody has seen before is held
    privately, not shown.
  - The inbox sends an automatic reply saying this inbox is public and
    asking permission, with a yes button.
  - If they click yes, that first email is published, and they are
    never asked again. Later emails from them show as normal.

He is open to other approaches, for example:
  - Tony approves the first email from each new person before it shows.
  - Held until either the sender says yes or Tony approves, whichever
    comes first.

Worth knowing:
  - This changes a decision made at PC-2 (every message shows as soon
    as it arrives, with a hide button that can be undone). Confirm with
    Tony before building.
  - Attachments do not work yet, so an attached resume would not
    appear today. A resume pasted into the email body would. When
    attachments are added, they need to pass the same consent step.
  - Questions for Tony, not decided: what the automatic reply says;
    what happens to a held email if the sender never answers; and
    whether Tony can see the held emails.

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

----- archived 2026-09-30 | from PA | file PA-PC.txt | tags: pa-pc, pc-3, before-rules-cut -----
== PROMPT ACCOMPLICE - PUBLIC COMS SYSTEM ==
The universal rules for working with Tony live in the botskill post,
https://nexus.needpedia.org/working-with-tony.txt (open its web page
version). This file holds only what is true of the PC thread.
Stable companion to the PC handoff prompt. Lives on Tony's computer at
/home/clearcrow/PublicComs/PA-PC.txt, with an identical web copy at
/home/clearcrow/Needpedia_Nexus/PA-PC.txt. Change both.
Holds nothing sensitive. Any AI may read it.
Last updated: 2026-09-30 (session PC-3)

REPLACES prompt_accomplice_PC_2026-09-22.txt, which said the mailbox was
Gmail / Google Workspace throughout. That was wrong. Delete the old file.


-- WHAT THIS SYSTEM IS --

A public communications system for Needpedia, an open-source nonprofit
civic collaboration platform. It is a web page that shows the mail for
the address VC@Needpedia.org, which stands for Volunteer Coordination.
Anyone can read the page without signing in. An AI assistant named
Adele sits on the page and answers questions about the mail. An admin
can send mail from it.

Live page: https://vc-email-five.vercel.app
Code: https://github.com/Queuevius/vc-email
Built with Next.js 16 and React 19, hosted on Vercel.
Confirmed live build: main branch, commit e8a9514, deployed 2026-07-27
by AdnanRailsCraft. The code in that repo is the code running.


-- WHERE THE MAILBOX ACTUALLY LIVES --

Zoho Mail. Not Gmail, not Google Workspace. The app signs in to
imappro.zoho.com. Tony's Google admin powers have nothing to do with
this mailbox and no Gmail setting affects it.

Zoho plan: Mail Lite, 10GB, paid and active. One license, one used.
Yearly. Expires 2026-12-09. If it lapses, program access to the
mailbox stops and the public page goes blank again.

Zoho admin console: https://mailadmin.zoho.com
Zoho webmail: https://mail.zoho.com

DNS for needpedia.org is at Cloudflare. Tony owns that account.


-- HOW IT WORKS TODAY, FROM READING THE ACTUAL CODE --

Read at PC-2 from src/services/emailService.ts.

There is no database. Nothing is stored anywhere.

Receiving: every time someone opens the page, the site signs in to the
Zoho mailbox using the standard mail-reading protocol (IMAP) and asks
for mail. The code computes a date 30 days back and asks only for mail
since then. It reads the folder named in a setting, currently INBOX.
Results are held in memory for 60 seconds.

The fetch limit setting is 500, but the 30-day window is hardcoded in
the source, not a setting. Changing it means changing code.

Sending: sends through a standard outgoing mail server, then tries to
copy the sent message back into the mailbox's sent folder so it shows
in the outbox. If that copy fails the code logs a warning and carries
on.

Deleting: an admin delete marks the message deleted and immediately
purges it. That permanently erases it from the real mail account. Not
trash. Gone.

Adele: sends up to 20 recent messages plus a "guidescript" instruction
sheet to an AI model through OpenRouter. The guidescript is stored in
an Upstash store. Her conversations get posted to needpedia.org.

Important about Adele: she does not look anything up. She only sees
what the app hands her. Anything she says about her own access comes
from the guidescript, not from checking. Do not treat her answers as
evidence about system state.

Settings all live as environment variables in the Vercel project.


-- WHAT WAS ACTUALLY WRONG, AND WHAT PC-1 GOT WRONG --

PC-1 concluded the mailbox was hiding mail because of a Gmail message
limit, and that the fix was a rebuild. Both were wrong.

The real cause: needpedia.org had NO mail-delivery records in DNS at
all. No MX records, no TXT records of any kind. Mail sent to
VC@Needpedia.org had nowhere to be delivered and died. Outbound was
unaffected because sending does not consult those records.

Confirmed by measurement, not inference: dig returned status NOERROR
with ANSWER 0 and a Cloudflare SOA, meaning the records genuinely did
not exist. Newest message in the Zoho inbox was 2026-04-22.

Mail sent to the address between 2026-04-22 and 2026-09-22 was never
delivered anywhere. It is not recoverable. There is no backlog waiting
to be pulled in.

The website was never broken. It was faithfully showing an empty
mailbox.

How the records disappeared is STILL UNKNOWN. Nobody deletes MX and
TXT records by accident. Until that is answered it can happen again.


-- WHAT WAS FIXED AT PC-2 --

All done in Cloudflare DNS. All confirmed live with dig.

MX records restored, pointing mail to Zoho:
  mx.zoho.com priority 10
  mx2.zoho.com priority 20
  mx3.zoho.com priority 50

Sender permission list (SPF) on needpedia.org:
  v=spf1 include:mailgun.org include:zohomail.com ip4:18.223.241.10 ~all

Sender permission list on www.needpedia.org:
  v=spf1 include:mailgun.org ~all
  (Mailgun is verified on www, not the root. NP-1 supplied this.)

Message signing (DKIM), selector vcaccount, 2048-bit:
  Name: vcaccount._domainkey
  Verified in Zoho, signing toggled ON.

Monitoring policy (DMARC):
  Name: _dmarc
  Value: v=DMARC1; p=none
  Monitoring only. Cannot cause any mail to be rejected.

End-to-end proof: a reply sent from VC@Needpedia.org to Tony's personal
Gmail on 2026-09-22 showed SPF PASS and DKIM PASS in Gmail's "Show
original" view. Inbound test mail arrived in Zoho and appeared on the
public page.

Note for later: DMARC has no reporting address, deliberately. Those
reports arrive daily as machine-readable attachments and would bury
real mail on a public page. If wanted later, send them elsewhere.


-- THE THREE DESIGN FLAWS, ALL STILL TRUE --

These were never the cause of the outage, but they are real and they
are why the outage went unnoticed for five months.

1. Mail older than 30 days is invisible, so the archive silently
   shrinks every day.
2. When the mailbox cannot be reached, the code catches the error,
   logs it where nobody looks, and returns an empty list. The page
   shows "no messages". Broken is indistinguishable from quiet. This
   is confirmed in the source, not suspected.
3. Nothing is stored anywhere. The page is only ever a window onto
   Zoho. Delete is permanent and immediate.


-- THE REBUILD: STATUS CHANGED AT PC-2 --

PC-1 decided on "Option 1" - the mail host keeps receiving and
sending, a small program copies every message into Needpedia's own
storage, and the page plus Adele read only that copy.

That decision still stands as a direction, but the urgency behind it
was based on a wrong diagnosis. The system is not broken now. The case
for rebuilding is the three design flaws above, not a crisis.

This should be revisited fresh at PC-3 rather than inherited as
momentum. Do not start building without Tony re-confirming.

Build plan as drafted at PC-1, kept for reference. Note that the
watcher section was written for Gmail and needs rewriting for Zoho:
  Storage: a hosted Postgres database for message text and details,
  plus Cloudflare R2 file storage for the untouched original message
  and attachments. Keeping big files out of the database keeps it
  small enough to stay free.
  Rules: write the untouched original to file storage FIRST, before
  parsing. Ignore repeats by matching each message's unique ID. Two
  grades of delete - reversible hiding from the public page, and a
  real erase for genuine privacy requests.
  Watcher: must read both received and sent folders. Must ask "what
  changed since last time" rather than re-reading everything, and must
  fall back to a full sweep automatically if the checkpoint is too old.
  Where it runs is unresolved: Nexus (free, stops when that machine is
  down, catches up after), GitHub's free scheduler (every few minutes),
  or paid Vercel at about $20/month.
  Sending: keep sending through Zoho and write our own copy of each
  sent message into the archive.


-- DECISIONS MADE, DO NOT REOPEN WITHOUT TONY --

PC-1: Option 1 over repair-only and over full independence.

PC-2: Every message shows on the public page as soon as it arrives.
No approval step. Paired with a one-click, reversible hide button for
spam and for personal information people send without realizing the
page is public.

PC-2: The website is the only place VC@Needpedia.org gets read. Nobody
opens the mailbox directly in an ordinary mail program. The mail host
is just the engine.


-- OPEN ITEMS --

How the DNS records disappeared. Unanswered. Can recur.

AdnanRailsCraft, the previous developer, deployed the July build and
may still have access to the Vercel project settings. Not yet removed.

Zoho plan expires 2026-12-09. Nothing breaks before then.

Whether any volunteer can write glue code, which decides how much of
any rebuild lands on Tony.

Mailgun has the Needpedia app's account switched off after a credential
was found exposed on GitHub. That is NP-1's work, not this thread's,
but it means the site's account-confirmation emails are still dead.
It did NOT cause the VC mailbox outage. Two separate failures that
overlapped in time.


-- THINGS ALREADY CHECKED, DO NOT REDO --

The vc-email repo was scanned at PC-2 for committed credentials. Clean.
Only placeholder values in .env.example. The exposed key Mailgun found
is in the Needpedia repo, not this one.

IMAP_USER in Vercel is VC@Needpedia.org, confirmed by reveal. The page
is not reading anyone's personal mailbox.

Signing in to the Zoho mailbox with the Vercel password works, tested
directly with curl. Returned 23 messages. Credentials are valid.


-- WORKING RULES FOR THIS THREAD --

Plain language is the top priority. Say what a thing IS and DOES in
everyday words before naming it, every time, even for things covered
in earlier sessions.

State the exact thing to use. Never say "use yours" or "the one you
picked" and expect Tony to recall it. He is following steps, not
tracking context. When he asks to start over, restart from step 1.

Declare session type at the top: look-only or build. Declared scope
outranks momentum. Never give action steps in a look-only session.

Design questions: surface options with their real-world effects. Don't
make executive decisions for Tony.

Read the actual code before describing it. Never infer from file or
branch names. State only what command output actually shows. After a
failed approach, one careful retry, then switch.

Never ask Tony to edit code by hand. Short change, one precise
terminal command. Long change, a helper script opened in gedit.

Label every paste box: TERMINAL, BROWSER, BROWSER CONSOLE, or GEDIT.
Prefer terminal versions. Long content goes via gedit, not terminal
heredocs.

When a file on Tony's computer is needed, give him a terminal command
to open or copy it. Do not leave him to work out how to retrieve it.
To open: gedit ~/path/to/file
To copy straight to clipboard: xclip -selection clipboard < ~/path/to/file

Explain what a destructive command removes, and what it doesn't,
before giving it.

Security: max speed, minimal hedging. No warnings about pasting keys
into chat. Flag only genuinely severe problems.

Documents get delivered as plain text files, never Word files. One
item per copy box. Bare URLs, no link formatting, no tables. Link
preview cards do not render as clickable for Tony.

Claude cannot put files on Tony's computer. Files land in his
Downloads and he moves them.

Tone: measured. No drama. "That changes a few things" beats "this
changes everything."


-- PEOPLE --

Tony Brasher, founder and president of Needpedia, owns every account
involved here. Legal name Anthony Brasher.
AdnanRailsCraft, previous developer, deployed the July build. May
still have access to the Vercel settings.
Murtaza, Needpedia's lead developer. Reachable but takes days.
Needpedia's own site AI can also be asked questions.


-- GLOSSARY, FOR ANY AI WRITING FOR TONY --

Don't use these names without first saying what the thing does.
  IMAP: the old way a program signs in to a mailbox and reads it.
  SMTP: the standard way mail gets sent out.
  MX record: the public note on a domain saying which server accepts
    its mail. Missing this means mail is never delivered.
  SPF: a public list of who is allowed to send mail using your domain
    name. Receiving servers read it to judge whether mail is forged.
  DKIM: a cryptographic signature on each outgoing message, checked
    against a key published on your domain.
  DMARC: instructions telling receiving servers what to do when a
    message fails the SPF and DKIM checks.
  Postgres: a database, meaning organized storage the website reads.
  R2: cheap file storage for whole files and attachments.
  Webhook: one program poking another the moment something happens.
  dig: a terminal command that looks up public DNS records.

== ADDED 30 SEPTEMBER 2026, SESSION PC-3 ==

FOUND THIS SESSION (30 September 2026)
- Zoho's folder for sent mail is named Sent. Read from Zoho's folder
  list with curl. All folders: INBOX, Drafts, Templates, Snoozed, Sent,
  Spam, Trash, Notification, Newsletter, Archive.
- Zoho keeps every email. The 30-day window is only how far back the
  page asks Zoho, not how long mail is kept. Nothing is lost by it.
  Mail is really lost only two ways today: the page's admin delete
  erases it from Zoho for good, and the Zoho plan lapsing on 2026-12-09.
- The vc-email repo on GitHub shows one open pull request (a proposed
  code change waiting for approval). Not looked at yet.
- The AI web fetch tool was refused when opening folders of the
  vc-email repo on GitHub. Until that is solved, code is read through
  Tony's terminal.

TONY'S PROBLEM LIST FOR THE PAGE
From the Nexus thread's update of 28 September 2026:
- Looking at sent emails shows the wrong thing: random old emails from
  the inbox and outbox instead of what was sent.
- Attachments do not work, in or out.
- No rich formatting (bold, links and so on), in or out.
- The chat button is redundant. The button labeled "Adele" already
  does the job.
- Tony needs to be able to delete emails once logged in.
Tony, 30 September 2026, in his words: "ordinary email functions like
receiving and sending attachments, bold italic and underline text, text
color, and other basic things. It would be cool if there was a way for
me to insert a logo and update/change it when I'm logged in. Just to
help people know it's a Needpedia space."

TONY'S DIRECTION (30 September 2026, his words)
- "For now let's get the email system working right."
- "I really do need to know the emails will always show up though,
  even if we have to save them to my computer or something"
- "If we could set it to save everything, then archive stuff older
  than 6 months that works too. Especially if the old ones can still
  be brought up, (just takes longer or something)."
- "let's combine all ideas to make the best Public Coms system."
- A thought, not a decision: put the whole email system on the Nexus,
  so it moves with the Nexus when the Nexus goes to a proper server.
This lines up with the PC-1 rebuild direction (a copier program saving
every email into storage of our own, with the page reading that copy),
plus his feature list and the consent step below.

CONSENT STEP (from the 28 September 2026 update; NOT DECIDED)
Tony's lean, "sender says yes": the first email from a new address is
held privately; an automatic reply says the inbox is public and asks
permission with a yes button; on yes it is published and that sender
is never asked again. Alternatives he is open to: Tony approves each
new sender's first email; or held until either the sender says yes or
Tony approves. This would change the PC-2 decision that every email
shows as soon as it arrives. Attachments must pass the same step.
Open: the automatic reply's wording; what happens if the sender never
answers; whether Tony can see held emails.

OPEN DESIGN QUESTIONS, NOT DECIDED (30 September 2026)
- Where the saved copy lives: Tony's computer (the Nexus), storage
  online, or both.
- Whether the whole page moves onto the Nexus.
- Order of work: fixes the rebuild would replace (showing sent mail,
  the 30-day window) versus only fixes that carry over (attachments,
  formatting, delete, the extra chat button, the logo).

----- archived 2026-09-30 | from PA | file PA-PC.txt | tags: pa-pc, pc-4, before-header-cleanup -----
== PROMPT ACCOMPLICE - PUBLIC COMS SYSTEM ==
The universal rules for working with Tony live in the botskill post,
https://nexus.needpedia.org/working-with-tony.txt (open its web page
version). This file holds only what is true of the PC thread.
Stable companion to the PC handoff prompt. Lives on Tony's computer at
/home/clearcrow/PublicComs/PA-PC.txt, with an identical web copy at
/home/clearcrow/Needpedia_Nexus/PA-PC.txt. Change both.
Holds nothing sensitive. Any AI may read it.
Last updated: 2026-09-30 (session PC-3)

REPLACES prompt_accomplice_PC_2026-09-22.txt, which said the mailbox was
Gmail / Google Workspace throughout. That was wrong. Delete the old file.


-- WHAT THIS SYSTEM IS --

A public communications system for Needpedia, an open-source nonprofit
civic collaboration platform. It is a web page that shows the mail for
the address VC@Needpedia.org, which stands for Volunteer Coordination.
Anyone can read the page without signing in. An AI assistant named
Adele sits on the page and answers questions about the mail. An admin
can send mail from it.

Live page: https://vc-email-five.vercel.app
Code: https://github.com/Queuevius/vc-email
Built with Next.js 16 and React 19, hosted on Vercel.
Confirmed live build: main branch, commit e8a9514, deployed 2026-07-27
by AdnanRailsCraft. The code in that repo is the code running.


-- WHERE THE MAILBOX ACTUALLY LIVES --

Zoho Mail. Not Gmail, not Google Workspace. The app signs in to
imappro.zoho.com. Tony's Google admin powers have nothing to do with
this mailbox and no Gmail setting affects it.

Zoho plan: Mail Lite, 10GB, paid and active. One license, one used.
Yearly. Expires 2026-12-09. If it lapses, program access to the
mailbox stops and the public page goes blank again.

Zoho admin console: https://mailadmin.zoho.com
Zoho webmail: https://mail.zoho.com

DNS for needpedia.org is at Cloudflare. Tony owns that account.


-- HOW IT WORKS TODAY, FROM READING THE ACTUAL CODE --

Read at PC-2 from src/services/emailService.ts.

There is no database. Nothing is stored anywhere.

Receiving: every time someone opens the page, the site signs in to the
Zoho mailbox using the standard mail-reading protocol (IMAP) and asks
for mail. The code computes a date 30 days back and asks only for mail
since then. It reads the folder named in a setting, currently INBOX.
Results are held in memory for 60 seconds.

The fetch limit setting is 500, but the 30-day window is hardcoded in
the source, not a setting. Changing it means changing code.

Sending: sends through a standard outgoing mail server, then tries to
copy the sent message back into the mailbox's sent folder so it shows
in the outbox. If that copy fails the code logs a warning and carries
on.

Deleting: an admin delete marks the message deleted and immediately
purges it. That permanently erases it from the real mail account. Not
trash. Gone.

Adele: sends up to 20 recent messages plus a "guidescript" instruction
sheet to an AI model through OpenRouter. The guidescript is stored in
an Upstash store. Her conversations get posted to needpedia.org.

Important about Adele: she does not look anything up. She only sees
what the app hands her. Anything she says about her own access comes
from the guidescript, not from checking. Do not treat her answers as
evidence about system state.

Settings all live as environment variables in the Vercel project.


-- WHAT WAS ACTUALLY WRONG, AND WHAT PC-1 GOT WRONG --

PC-1 concluded the mailbox was hiding mail because of a Gmail message
limit, and that the fix was a rebuild. Both were wrong.

The real cause: needpedia.org had NO mail-delivery records in DNS at
all. No MX records, no TXT records of any kind. Mail sent to
VC@Needpedia.org had nowhere to be delivered and died. Outbound was
unaffected because sending does not consult those records.

Confirmed by measurement, not inference: dig returned status NOERROR
with ANSWER 0 and a Cloudflare SOA, meaning the records genuinely did
not exist. Newest message in the Zoho inbox was 2026-04-22.

Mail sent to the address between 2026-04-22 and 2026-09-22 was never
delivered anywhere. It is not recoverable. There is no backlog waiting
to be pulled in.

The website was never broken. It was faithfully showing an empty
mailbox.

How the records disappeared is STILL UNKNOWN. Nobody deletes MX and
TXT records by accident. Until that is answered it can happen again.


-- WHAT WAS FIXED AT PC-2 --

All done in Cloudflare DNS. All confirmed live with dig.

MX records restored, pointing mail to Zoho:
  mx.zoho.com priority 10
  mx2.zoho.com priority 20
  mx3.zoho.com priority 50

Sender permission list (SPF) on needpedia.org:
  v=spf1 include:mailgun.org include:zohomail.com ip4:18.223.241.10 ~all

Sender permission list on www.needpedia.org:
  v=spf1 include:mailgun.org ~all
  (Mailgun is verified on www, not the root. NP-1 supplied this.)

Message signing (DKIM), selector vcaccount, 2048-bit:
  Name: vcaccount._domainkey
  Verified in Zoho, signing toggled ON.

Monitoring policy (DMARC):
  Name: _dmarc
  Value: v=DMARC1; p=none
  Monitoring only. Cannot cause any mail to be rejected.

End-to-end proof: a reply sent from VC@Needpedia.org to Tony's personal
Gmail on 2026-09-22 showed SPF PASS and DKIM PASS in Gmail's "Show
original" view. Inbound test mail arrived in Zoho and appeared on the
public page.

Note for later: DMARC has no reporting address, deliberately. Those
reports arrive daily as machine-readable attachments and would bury
real mail on a public page. If wanted later, send them elsewhere.


-- THE THREE DESIGN FLAWS, ALL STILL TRUE --

These were never the cause of the outage, but they are real and they
are why the outage went unnoticed for five months.

1. Mail older than 30 days is invisible, so the archive silently
   shrinks every day.
2. When the mailbox cannot be reached, the code catches the error,
   logs it where nobody looks, and returns an empty list. The page
   shows "no messages". Broken is indistinguishable from quiet. This
   is confirmed in the source, not suspected.
3. Nothing is stored anywhere. The page is only ever a window onto
   Zoho. Delete is permanent and immediate.


-- THE REBUILD: STATUS CHANGED AT PC-2 --

PC-1 decided on "Option 1" - the mail host keeps receiving and
sending, a small program copies every message into Needpedia's own
storage, and the page plus Adele read only that copy.

That decision still stands as a direction, but the urgency behind it
was based on a wrong diagnosis. The system is not broken now. The case
for rebuilding is the three design flaws above, not a crisis.

This should be revisited fresh at PC-3 rather than inherited as
momentum. Do not start building without Tony re-confirming.

Build plan as drafted at PC-1, kept for reference. Note that the
watcher section was written for Gmail and needs rewriting for Zoho:
  Storage: a hosted Postgres database for message text and details,
  plus Cloudflare R2 file storage for the untouched original message
  and attachments. Keeping big files out of the database keeps it
  small enough to stay free.
  Rules: write the untouched original to file storage FIRST, before
  parsing. Ignore repeats by matching each message's unique ID. Two
  grades of delete - reversible hiding from the public page, and a
  real erase for genuine privacy requests.
  Watcher: must read both received and sent folders. Must ask "what
  changed since last time" rather than re-reading everything, and must
  fall back to a full sweep automatically if the checkpoint is too old.
  Where it runs is unresolved: Nexus (free, stops when that machine is
  down, catches up after), GitHub's free scheduler (every few minutes),
  or paid Vercel at about $20/month.
  Sending: keep sending through Zoho and write our own copy of each
  sent message into the archive.


-- DECISIONS MADE, DO NOT REOPEN WITHOUT TONY --

PC-1: Option 1 over repair-only and over full independence.

PC-2: Every message shows on the public page as soon as it arrives.
No approval step. Paired with a one-click, reversible hide button for
spam and for personal information people send without realizing the
page is public.

PC-2: The website is the only place VC@Needpedia.org gets read. Nobody
opens the mailbox directly in an ordinary mail program. The mail host
is just the engine.


-- OPEN ITEMS --

How the DNS records disappeared. Unanswered. Can recur.

AdnanRailsCraft, the previous developer, deployed the July build and
may still have access to the Vercel project settings. Not yet removed.

Zoho plan expires 2026-12-09. Nothing breaks before then.

Whether any volunteer can write glue code, which decides how much of
any rebuild lands on Tony.

Mailgun has the Needpedia app's account switched off after a credential
was found exposed on GitHub. That is NP-1's work, not this thread's,
but it means the site's account-confirmation emails are still dead.
It did NOT cause the VC mailbox outage. Two separate failures that
overlapped in time.


-- THINGS ALREADY CHECKED, DO NOT REDO --

The vc-email repo was scanned at PC-2 for committed credentials. Clean.
Only placeholder values in .env.example. The exposed key Mailgun found
is in the Needpedia repo, not this one.

IMAP_USER in Vercel is VC@Needpedia.org, confirmed by reveal. The page
is not reading anyone's personal mailbox.

Signing in to the Zoho mailbox with the Vercel password works, tested
directly with curl. Returned 23 messages. Credentials are valid.


-- WORKING RULES FOR THIS THREAD --

Cut 30 September 2026 at Tony's say-so: they repeated the botskill post
(see the top of this file). The full old text is in ARCHIVE-PC.md.

One rule this thread keeps that the botskill post lacks:
Tone: measured. No drama. "That changes a few things" beats "this
changes everything."


-- PEOPLE --

Tony Brasher, founder and president of Needpedia, owns every account
involved here. Legal name Anthony Brasher.
AdnanRailsCraft, previous developer, deployed the July build. May
still have access to the Vercel settings.
Murtaza, Needpedia's lead developer. Reachable but takes days.
Needpedia's own site AI can also be asked questions.


-- GLOSSARY, FOR ANY AI WRITING FOR TONY --

Don't use these names without first saying what the thing does.
  IMAP: the old way a program signs in to a mailbox and reads it.
  SMTP: the standard way mail gets sent out.
  MX record: the public note on a domain saying which server accepts
    its mail. Missing this means mail is never delivered.
  SPF: a public list of who is allowed to send mail using your domain
    name. Receiving servers read it to judge whether mail is forged.
  DKIM: a cryptographic signature on each outgoing message, checked
    against a key published on your domain.
  DMARC: instructions telling receiving servers what to do when a
    message fails the SPF and DKIM checks.
  Postgres: a database, meaning organized storage the website reads.
  R2: cheap file storage for whole files and attachments.
  Webhook: one program poking another the moment something happens.
  dig: a terminal command that looks up public DNS records.

== ADDED 30 SEPTEMBER 2026, SESSION PC-3 ==

FOUND THIS SESSION (30 September 2026)
- Zoho's folder for sent mail is named Sent. Read from Zoho's folder
  list with curl. All folders: INBOX, Drafts, Templates, Snoozed, Sent,
  Spam, Trash, Notification, Newsletter, Archive.
- Zoho keeps every email. The 30-day window is only how far back the
  page asks Zoho, not how long mail is kept. Nothing is lost by it.
  Mail is really lost only two ways today: the page's admin delete
  erases it from Zoho for good, and the Zoho plan lapsing on 2026-12-09.
- The vc-email repo on GitHub shows one open pull request (a proposed
  code change waiting for approval). Not looked at yet.
- The AI web fetch tool was refused when opening folders of the
  vc-email repo on GitHub. Until that is solved, code is read through
  Tony's terminal.

TONY'S PROBLEM LIST FOR THE PAGE
From the Nexus thread's update of 28 September 2026:
- Looking at sent emails shows the wrong thing: random old emails from
  the inbox and outbox instead of what was sent.
- Attachments do not work, in or out.
- No rich formatting (bold, links and so on), in or out.
- The chat button is redundant. The button labeled "Adele" already
  does the job.
- Tony needs to be able to delete emails once logged in.
Tony, 30 September 2026, in his words: "ordinary email functions like
receiving and sending attachments, bold italic and underline text, text
color, and other basic things. It would be cool if there was a way for
me to insert a logo and update/change it when I'm logged in. Just to
help people know it's a Needpedia space."

TONY'S DIRECTION (30 September 2026, his words)
- "For now let's get the email system working right."
- "I really do need to know the emails will always show up though,
  even if we have to save them to my computer or something"
- "If we could set it to save everything, then archive stuff older
  than 6 months that works too. Especially if the old ones can still
  be brought up, (just takes longer or something)."
- "let's combine all ideas to make the best Public Coms system."
- A thought, not a decision: put the whole email system on the Nexus,
  so it moves with the Nexus when the Nexus goes to a proper server.
This lines up with the PC-1 rebuild direction (a copier program saving
every email into storage of our own, with the page reading that copy),
plus his feature list and the consent step below.

CONSENT STEP (from the 28 September 2026 update; NOT DECIDED)
Tony's lean, "sender says yes": the first email from a new address is
held privately; an automatic reply says the inbox is public and asks
permission with a yes button; on yes it is published and that sender
is never asked again. Alternatives he is open to: Tony approves each
new sender's first email; or held until either the sender says yes or
Tony approves. This would change the PC-2 decision that every email
shows as soon as it arrives. Attachments must pass the same step.
Open: the automatic reply's wording; what happens if the sender never
answers; whether Tony can see held emails.

OPEN DESIGN QUESTIONS, NOT DECIDED (30 September 2026)
- Where the saved copy lives: Tony's computer (the Nexus), storage
  online, or both.
- Whether the whole page moves onto the Nexus.
- Order of work: fixes the rebuild would replace (showing sent mail,
  the 30-day window) versus only fixes that carry over (attachments,
  formatting, delete, the extra chat button, the logo).

== ADDED 30 SEPTEMBER 2026, SESSION PC-3, PART 2 ==

DECIDED BY TONY (30 September 2026)
- Order of work: fix everything on the current page now, including
  showing sent mail and the 30-day window, even though the rebuild
  would later replace those two. Tony's answer: "Yes".
- New item for the list: a way to see the password while typing it at
  login.
- The working rules section above was cut (Tony: "yes").

OPEN (30 September 2026)
- Code pages: a Nexus web page per project linking each code file, so
  an AI can open code without Tony running commands. Big projects get
  one page per folder. Links point at exact saved versions on GitHub.
  Untested: whether the AI fetch tool follows a link from a Nexus page
  to a GitHub file. Not decided: whether PC builds a PC-only page as a
  test first, or the Nexus thread builds it for every thread.

== ADDED 30 SEPTEMBER 2026, SESSION PC-3, PART 3 (CLOSE) ==

CODE READ THIS SESSION (30 September 2026)
Version e8a9514, the same as the live site. Local copy made 30 Sep 2026
at /home/clearcrow/PublicComs/vc-email-code.
Read: src/services/emailService.ts, src/actions/emailActions.ts,
src/app/sent/SentPageContent.tsx, src/app/api/emails/route.ts,
src/app/api/emails/[id]/route.ts.
Not read yet: src/app/inbox/EmailList.tsx, EmailItem.tsx,
EmailDetailPageContent.tsx, src/app/inbox/[id]/page.tsx,
src/app/api/emails/fetch/route.ts, src/lib/permissions.ts,
src/auth/auth.ts. Then the compose, send, login and layout files.

CORRECTION (30 September 2026)
The PC-3 handoff said the page only opens INBOX and never reads the
sent folder. Wrong. fetchEmailsFromIMAP opens whatever folder it is
asked for, and the Sent page asks for "Sent", Zoho's real name for it.

WHY THE SENT PAGE OPENS WRONG EMAILS (30 September 2026)
Each email's id is only Zoho's number for it, and Zoho numbers each
folder separately. Received #12 and sent #12 both get the id "12".
getEmailById returns the first "12" in anything recently loaded, and
when nothing is loaded it searches only the default folder, INBOX.
Fix: make the id include the folder (for example Sent-12) and make
every action use it. Whether the Sent list itself has a second
problem: check EmailList.tsx and api/emails/fetch/route.ts.

DANGER UNTIL FIXED (30 September 2026)
deleteEmail, toggleStar and toggleReadStatus open "INBOX" whichever
folder the email came from. Deleting sent #7 from the Sent page
permanently erases received #7. Do not delete on the Sent page until
fixed. Delete is a permanent erase (marked deleted, then purged), not
Zoho's trash.

OTHER FINDINGS (30 September 2026)
- 30-day window: one line in fetchEmailsFromIMAP sets the start date
  30 days back. Count cap: IMAP_FETCH_LIMIT, 500 in Vercel, 50 if
  missing.
- Delete is limited to the admin login in both email routes and in the
  server action. Why Tony cannot delete when logged in: not known yet;
  check permissions.ts and auth.ts.
- The emails route takes any folder name from the web address, with
  no login, so anyone can read Drafts, Spam or Trash. Matters once the
  consent step exists: held emails must not be reachable this way.
- After sending, the code saves its own copy into Sent. Zoho may also
  save one. Check for doubles before changing anything.
- Errors reaching Zoho still show as an empty list (known flaw 2).

TONY'S DIRECTION, ADDED AT CLOSE (30 September 2026, his words)
"the moment an email comes in, it gets saved to my computer. Then we
don't have to deal with Zoho's bullshit, and I have a file with all the
emails in it I can back up."
Notes: a mail host such as Zoho still has to receive the mail. This is
the PC-1 copier idea with Tony's computer as the storage. If his
computer is off, mail waits in Zoho and is copied when it is back on.
How the public page reads the saved copy is the open design question.

REQUEST TOOL IDEA (Tony, 30 September 2026; sent to the Nexus thread)
A program on the Nexus serving a reference sheet of real links, each
one a request for a specific thing; opening a link gets that thing
back on the same link. Tony's version posted the result at an address
made of date, time and name; an AI cannot open an address it builds
itself, so the reply comes back on the trigger link instead. Tony: "Of
course we'll program the program to not reveal private info." Only a
fixed list of public items; never a file path taken from a link.


== ADDED 30 SEPTEMBER 2026, SESSION PC-4, PART 1 ==

DECIDED BY TONY (30 September 2026, PC-4)
- Delete moves an email to Zoho's Trash folder, so it is "recoverable in
  Zoho if I delete by mistake". Not a permanent erase. The reversible
  hide button decided at PC-2 is a separate thing.
- Older mail, his words: "once the emails are saved to our own stuff we
  can just let them display by however many fit on the page. Maybe 30
  emails listed at a time. With an option to look back further."
- Email chains, his words: "when there's email chains, they need to
  display when I open an email. That's the kinda thing I mean by basic
  email features."
- Changes go straight to the live site, no test copy first. His answer:
  "B, straight to live".
- The handoff, his words: "The handoff prompt, is printed at the end of a
  session, and I use it to start a new one. Period."

FOUND (30 September 2026, PC-4). All of src/ was read at PC-4, version
e8a9514.
- Sent page: the list asks Zoho for the Sent folder correctly. The wrong
  email appeared on clicking, because each email's id was only Zoho's
  number for it, and Zoho numbers each folder separately.
- The email list has no delete button. The code for it exists but was
  never put on screen. The only delete is a small trash can at the top of
  an opened email, shown to the admin login only.
- Received attachments: read, but only file name and size are kept; the
  file itself is thrown away and nothing is shown.
- Compose is a plain text box. The send code accepts plain text only.
- The extra chat button is "Chat with AI" at the bottom right
  (src/components/ai/AIAssistant.tsx). The "Adele" button opens the same
  window.
- Adele's built-in instructions (src/lib/ai.ts) call her an assistant for
  "Needpedia/Venture Capital" handling "deal flow". VC here means
  Volunteer Coordination. To be corrected. Her window is titled
  "VC Assistant".
- Every page visit downloads up to IMAP_FETCH_LIMIT whole emails from the
  last 30 days, attachments included.
- Received formatting shown: bold, italic, underline, links, lists,
  headings. Stripped: colors, tables, fonts, images.
- Two logins exist: admin (ADMIN_EMAIL, or IMAP_USER if unset, typed
  exactly, plus ADMIN_PASSWORD) and an optional read-only guest.
- Zoho's Sent folder held 29 emails on 30 September 2026. Whether Zoho
  also keeps its own copy of mail sent from the page: being checked.
- Vercel only puts a new version live if it builds without errors; a
  failed build leaves the current live site in place.

PC AI'S PROPOSED ORDER OF WORK (PC-4; not a decision by Tony)
1. Folder mix-up: ids carry the folder (INBOX-12, Sent-12), the page can
   only read Inbox and Sent, delete moves to Trash.
2. Delete buttons in the list plus select-several; 30 at a time with a
   way to look further back.
3. Remove the extra chat button; show-password at login; a logo Tony
   uploads and changes when logged in; Adele's name and what VC means.
4. Formatting and attachments in and out; email chains shown when an
   email is opened.
5. The consent step.


== ADDED 30 SEPTEMBER 2026, SESSION PC-4, PART 2 ==

CONSENT STEP, DECIDED BY TONY (30 September 2026, PC-4)
This replaces the PC-2 decision that every email shows on the public page
as soon as it arrives. Not built yet; planned as chunk 5.
- His design, his words: "We could make the first email sent by someone
  ONLY show for people who've logged in, then automatically add a note to
  the response email / reply I create, which says 'Our community uses a
  radically transparent communication system where all messages are
  publicly visible online and our AI can tell you what everyone's
  currently working on, (it can see task cards on Needpedia too). This
  makes it an excellent resource for seeing what's going on with our
  community, and coordination, but it requires people's consent. To
  provide yours, click 'yes'. To opt out, simply reply to us at
  NeedpediaVC@gmail.com"
- Later emails from the same person before they click yes stay
  logged-in-only. His answer: "yes."
- His own replies, his words: "until the convo is public nothing in it
  should be, my comments included."
- If they never click yes, it stays private. His words: "Yes, consent is
  priority."
- Adele, his words: "We could make it so that Adele can't even SEE emails
  that aren't supposed to be online yet." Plan: held emails are never
  handed to Adele at all.
- Note for whoever builds it: the Adele on this page sees only the emails
  and up to 4 web pages linked in her instructions, not Needpedia task
  cards. The note's task-card line is true here only if her instructions
  link a page that lists them.
- Still open: what the page reached by the yes link says. Attachments
  follow the same rule (from the Nexus thread's update of 28 Sep 2026).

CHUNK 1 IS LIVE (30 September 2026, PC-4)
- Commit bd0e3a1 on main, deployed by Vercel, confirmed live: the live
  page now refuses to show the Trash folder.
- What it changed: every email's id carries its folder (INBOX-12,
  Sent-12), so opening, star, mark-read, delete and Summarize hit the
  right email; the page reads only Inbox and Sent; delete moves the email
  to Zoho's Trash folder; "Back" on a sent email goes to the Sent list.
- The DANGER from PC-3 (deleting sent #7 erased received #7) is fixed by
  this.
- Also changed one line in src/lib/permissions.test.ts ('USER' as any),
  because the code check stopped on an old error in that practice-test
  file. Not a PC-4 error.

HOW CODE GOES LIVE NOW (30 September 2026)
- Tony's computer is signed in to GitHub through GitHub's command-line
  tool (gh), so pushes from ~/PublicComs/vc-email-code work. A push to
  main goes live through Vercel within about 2 minutes. Old versions stay
  in Vercel's Deployments list and can be put back with one click.
- Node 22 and npm 10 are installed; the code copy has its building blocks
  installed, so "npx tsc --noEmit" checks the code for errors before a
  push.

FOUND (30 September 2026, PC-4)
- No double copies in Sent. Zoho saves its own copy of every email sent
  from the page (marked "X-Mailer: VC Email System"). The page's own
  save-a-copy step never worked. To be removed in chunk 2.
- Un-starring probably fails: the code calls removeFlags, but the mail
  library (imap-simple) names that command delFlags. Fix in chunk 2.
- Open pull request #2 (June 2026, "Extend IMAP fetch window so older
  emails aren't hidden from the inbox") is replaced by chunk 2's
  30-at-a-time design. Closing it is Tony's call.
- Security check, 30 Sep 2026: 13 serious known weaknesses in the building
  blocks the live page runs, 3 of them critical: next, next-auth,
  @auth/core. Being looked at.


== ADDED 30 SEPTEMBER 2026, SESSION PC-4, PART 3 ==

LIVE ON THE PAGE (30 September 2026, PC-4)
- Chunk 1b, commit e5a258f: security updates. next 16.1.0 -> 16.3.8,
  next-auth -> 4.24.15, unused @auth/core removed from the package list.
  Vercel: "Deployment has completed".
- Chunk 2, commit 742eb85, plus chunk 2b, commit d4848e1:
  - Inbox and Sent list the newest 30. "Show 30 older" and "Show 30
    newer" buttons change ?page= in the address, so a page number can be
    typed into the address bar. Tony's design: "The UI says "Show 30
    older" button but when I go back, the URL has a page number I can
    edit." No more 30-day cutoff.
  - Logged in as admin: tick box and trash can on every email, "Select
    all on this page", "Delete selected". Deleted mail goes to Zoho's
    Trash. Visitors see none of these and no star button.
  - When Zoho cannot be reached, the page says so with a "Try again"
    button instead of showing an empty list (design flaw 2 from PC-2 is
    fixed).
  - Refresh really fetches fresh mail. Un-starring fixed.
  - The page no longer tries to save its own copy of sent mail.
  - Summarize finds an email even when it is older than the first page.
  - Mail libraries updated: nodemailer (latest 7.x), mailparser (latest
    3.x).
- Checked live after 2b: the page showed 29 of 29 in Inbox and 29 of 29
  in Sent, matching Zoho's own counts. Tony: "The email site is looking
  good, I can see everything now." He also confirmed sent emails open
  correctly.

FOUND (30 September 2026, PC-4)
- Mail library quirk (imap-simple / node-imap): given email numbers as one
  written list ("29,28,27"), it quietly keeps only the first number. Hand
  them over one by one (["UID", ...uids]). This is why chunk 2 first
  showed 1 email per page.
- Vercel reports "Deployment has completed" a few seconds before the live
  address switches over. Wait about 20 seconds before testing the live
  page.
- The login package (next-auth 4.24.15, the newest of version 4) still
  carries @auth/core inside it, marked critical. That weakness is about
  sign-in by emailed link, which this page does not use (it signs in with
  a password). Only version 5, not finished yet, removes it. Left as is.
- Remaining "high" items are in the mail-reading and mail-sending
  libraries. Their risk comes from the mail server sending booby-trapped
  replies, and the only server is Zoho. The mail-reading ones get
  replaced when mail is saved to Tony's computer.

STILL TO BUILD (PC AI's proposed order, 30 September 2026)
- Chunk 3: remove the extra "Chat with AI" button; show-password at login;
  a logo Tony uploads and changes when logged in; Adele's name and what VC
  means in her built-in instructions.
- Chunk 4: formatting and attachments in and out; email chains shown when
  an email is opened.
- Chunk 5: the consent step (see PART 2). Tony asked on 30 September 2026
  whether it was time to test it; open questions put to him: build it
  next or keep the order, what to do about the emails already public, and
  whether the note goes on every email he sends to someone who has not
  said yes.
