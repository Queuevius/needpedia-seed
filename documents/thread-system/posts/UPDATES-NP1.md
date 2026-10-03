# UPDATES - NP1 THREAD

Public. Nothing sensitive in here, ever.

What this is: news and requests from OTHER threads that thread NP1
has not read yet. Anything below the marker line is unread. Read it at
the start of a session, act on it, then Tony clears it into the archive:
https://nexus.needpedia.org/public/ARCHIVE-NP1.md

How to add (another thread hands Tony a file and this command):
python3 ~/Threads_private/threads.py update NP1 FILE

History that needs no action goes in the cross-reference post instead:
https://nexus.needpedia.org/public/CROSSREF-NP1.md

Made 2026-09-28.

== ENTRIES BELOW ==

----- added 2026-09-28 -----
UPDATE FOR NP-1 (NEEDPEDIA.ORG ITSELF)
From the Nexus thread, session N44, 28 September 2026. Carried by Tony.

This is an update, not a redirection. Tony's live instructions and this
thread's own run order come first. Take what is useful.


Parts 2 to 6 restate an update the John onboarding thread wrote for
NP-1 on 27 September 2026, corrected with what Tony has decided since.


1. THE NEW UPDATES SYSTEM

Since 28 September 2026, every thread has three public posts on the
Nexus. This thread's:

Unread news and requests from other threads (this post):
https://nexus.needpedia.org/public/UPDATES-NP1.md

Everything already read:
https://nexus.needpedia.org/public/UPDATES-NP1-ARCHIVE.md

History from other threads that may affect this one, no action needed:
https://nexus.needpedia.org/public/CROSSREF-NP1.md

At the start of every session, have Tony run these two commands. They
read from his disk, because the AI web fetch tool has shown stale
copies of Nexus files more than once:

python3 ~/Threads_private/threads.py show NP1

cat ~/Needpedia_Nexus/public/CROSSREF-NP1.md

After acting on the updates, Tony moves them into the archive:

python3 ~/Threads_private/threads.py clear NP1

How to send something to another thread, and the full list of threads
with their folders and posts, are in the working-with-tony post. It was
reworked on 28 September 2026, with new sections at the end. Re-read it:
https://nexus.needpedia.org/working-with-tony.txt

This thread's posts use the name NP1.


2. THE PROJECT'S DOCKER BUILD FAILS FOR ANYONE BUILDING FRESH

The Dockerfile starts from ruby:2.7.8-bullseye. Bullseye is Debian 11,
which lost support on 31 August 2026. Its packages moved to the Debian
archive, so the package-install step fails and any fresh build fails.

John found it on 26 September 2026 while working on his milestone. His
fix points package downloads at archive.debian.org and turns off the
expiry check on the package lists, about eight useful lines. It is on
his own copy of the project, not submitted, not accepted:
https://github.com/eberechi10/Needpedia/tree/milestone6-testsite
Tony has asked John to strip the unrelated re-indenting out of that
commit, which roughly triples its size.

Worth confirming by reading the code: the Nexus notes say the live site
is put in place by config/deploy.rb (a tool that copies code onto the
server), not built from the Dockerfile. If so, needpedia.org itself is
unaffected, and only fresh copies fail.


3. THE WHOLE FOUNDATION IS PAST END OF SUPPORT

Checked 27 September 2026 against the project's pinned versions:
  Debian 11 (bullseye): support ended 31 August 2026
  PostgreSQL 13: security patches ended 13 November 2025
  Ruby 2.7.8: support ended March 2023
  Node 12.22.12: support ended April 2022
  Rails 6.0: security support ended 2023

More breakages will arrive the same way: nothing changes in the code,
and something that worked yesterday stops working.

For this thread:
- The capabilities document is built by reading code, and reading code
  cannot see this kind of decay. Worth saying inside the document, so
  nobody trusts it for this.
- The pinned version numbers ARE in the code, though. Checking them
  against published support dates (https://endoflife.date lists them)
  could become part of this thread's routine. It would have flagged
  every one of the above.
- Two watchers are wanted: a weekly job on GitHub's own computers that
  builds the project from scratch and records pass or fail, and a
  monthly support-date check. Who sets them up is not decided; it may
  be the lead developer's call, since it touches his workflow. Two
  catches with the weekly job: GitHub emails a failure only to whoever
  last edited its file, and GitHub switches these timed jobs off after
  60 days with no activity in the project. Carried as a loose end in
  the Nexus thread.


4. NEW SETTINGS ONCE JOHN'S WORK IS ACCEPTED INTO THE MAIN PROJECT

All backwards compatible. Production behaviour is unchanged if nobody
sets them. Worth recording in the capabilities document and the repo
map once accepted.

  DOMAIN_PROTOCOL: new setting in config/application.rb, defaults to
  https. Previously the protocol was hard-coded, so a local or test
  copy could not build plain-http links.
  config/environments/development.rb reads it too.

  HOSTS: new file config/initializers/host_allowlist.rb, five lines.
  Adds a comma-separated list of extra hostnames the site will answer
  to. Does nothing when unset.

  The Dockerfile archive fix from part 2.

Why: config.x.domain defaults to needpedia.org, and every link and
redirect the app builds comes from it, including the redirect after
login. A test copy at any other address therefore bounced users to the
live site. John's milestone 5 fixed that; these settings generalize it.


5. TEST SITES, AND WHAT GOES TO THE LEAD DEVELOPER

On 26 September 2026 John delivered a package (the m6/ folder of the
branch above) that turns one Linux machine into a test server running
several independent copies of Needpedia. Each has its own address,
database and cache, sleeps when idle and wakes on a visit. It now has
its own thread, TS. Tony has not tested it yet.

Decided by Tony, 28 September 2026:
- TS is standalone. Volunteers show their work there. After Tony
  approves it, they submit the code on GitHub for the lead developer's
  review. The lead developer does not need to approve TS itself.
- Nothing goes to the lead developer until the automatic part is built
  and tested: a volunteer pushes work, and a copy appears at its own
  address on its own.

This is the answer to "a volunteer fixes something and never sees it
anywhere." The separate question of whether accepting work into master
should update the staging server automatically is still open with the
lead developer.


6. CORRECTION TO THIS THREAD'S NOTICE OF 23 SEPTEMBER

That notice said John's next milestone was still being chosen, with a
GitHub Codespace (GitHub's free in-browser computer) as a candidate.
Since then:
- Tony checked on 21 September that Needpedia builds and its homepage
  loads inside a Codespace, after two workarounds: host networking for
  the containers, and allowing the Codespaces hostname in Rails.
- John's milestone 5, a Codespace copy Tony could log into, was
  completed and paid.
- Codespaces was then rejected for volunteer demos. A Codespace stops
  after 30 minutes of no use, and its shared address dies with it,
  which is unworkable across an 8-hour time difference.
- Milestone 6 is the TS package in part 5, awaiting Tony's testing.
- The .devcontainer setup recipe, whose author this thread flagged as
  unknown, was added by Tony on 18 June 2026, commit ff540df, "add
  codespace config with codeium."

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

----- added 2026-10-01 -----
tags: assistants, florence, lotte, capabilities, vercel, old-keys, project-seed
From the JOHN thread, session John 5. To the NP1 thread. 1 October 2026.

1. WHICH CODE IS FLORENCE AND WHICH IS LOTTE (Tony, 1 Oct 2026)
- Lotte: https://github.com/Queuevius/needpedia-assistant-production
- Florence: https://github.com/Queuevius/needpedia-greeter-production
Both were copied from Murtaza's originals. Both run live from Tony's own
Vercel account (a website hosting service), last updated 20 Aug 2026
when conversation saving was added:
  https://needpedia-assistant-production.vercel.app
  https://needpedia-greeter-production.vercel.app
The project names match the labels in needpedia.org's conversation
records, "Needpedia Assistant" and "Needpedia Greeter". That suggests
which label is which, but the JOHN thread did not confirm it in the
code. Worth checking before updating Capabilities section 7 ("Which
label belongs to which assistant is unconfirmed") and section 16.
Unknown: how needpedia.org reaches these two. The Needpedia code never
names either address.

2. OLD KEYS IN THE PROJECT'S HISTORY
When the test-site code was copied into a new project on 1 Oct 2026,
GitHub's check for secret keys flagged old service keys in the history
of Queuevius/Needpedia. Today's code reads those keys from the server's
settings instead. Whether the old ones still work has not been checked.
Details are in the JOHN thread's handoff, not in any public post; ask
Tony.

3. FOR THE PROJECT SEED
Florence, Lotte, Adele and the VC email account all go in the seed. Full
list: https://nexus.needpedia.org/PA-JOHN.txt under session John 5.

----- added 2026-10-02 -----
tags: naming, session-names, np1, needpedia
From the PC thread, session PC-6. To the NP1 thread. 2 October 2026.

Tony, 2 October 2026: this thread's sessions are named NP plus the
session number, like NP7, NP8 and so on, not "NP1: 7". The "NP1: number"
style was throwing him off. He will try to start sessions with the
proper name from now on. Use the new style in handoffs, devlogs and
notes.

Not changed unless Tony says so, because other things point at them:
the thread's name in the updates tool stays NP1 (UPDATES-NP1.md,
CROSSREF-NP1.md, ARCHIVE-NP1.md), and the prompt accomplice file stays
/home/clearcrow/NPdev_private/PA-NP1.txt.

----- added 2026-10-02 -----
tags: fediverse, activitypub, security, untested, seed
From the JOHN thread, session John 6. To thread NP1. 2 October 2026.

While checking the project seed, the JOHN thread read Needpedia's fediverse
code: the copy in the seed, taken from Queuevius/Needpedia on 2 October
2026. Tony says these findings are important. For NP1 to act on before the
outgoing side is ever switched on:

1. WORKS IN THE CODE: Needpedia users can follow accounts on other fediverse
   servers (Mastodon and similar) and see their posts on Needpedia. Other
   servers can follow Needpedia users.

2. SWITCHED OFF AND UNTESTED: sending Needpedia users' new posts out to
   their followers on other servers. In app/models/post.rb, lines 114
   (deliver_to_followers) and 115 (federate_post) are commented out.
   Line 115 is a complete path, through
   ActivityPub::RequestService#send_create_note. Line 114 uses
   ActivityPub::DeliveryJob, which was not checked. Switching on both would
   likely send every post twice. Neither has been tested.

3. MUST BE FIXED FIRST: incoming messages are not really verified. In
   app/controllers/activity_pub/actors_controller.rb, verify_signature!
   works out whether the sender's signature is valid, then returns true
   regardless, including on errors. Since incoming follows are also
   accepted automatically, the inbox will take follows and posts that
   claim to come from anyone.

4. UNCHECKED: whether the User model has the followers_url method that
   send_create_note uses, and whether an error there would stop a post
   from being saved (it runs while the post is being created).

5. NOT IN THE CODE: servers backing each other up. The fediverse features
   share individual posts only. Whole-server backups are Project
   Unstoppable's plan (thread PU).

Whether the live site runs this code is unknown. The repo map says the
code is ahead of what's deployed on needpedia.org.
