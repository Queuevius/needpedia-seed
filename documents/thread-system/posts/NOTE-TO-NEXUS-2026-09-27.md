# NOTE FOR THE NEXUS THREAD — from thread NPA (phone app), 27 September 2026

Public. Nothing sensitive in here.

## Two ideas Tony wants your view on

### 1. Tags on public Nexus posts, with one map file

Tony wants an AI working in one thread to be able to find related work
in other threads. The obstacle is that an AI cannot browse or search
the Nexus. It can only open an exact address.

Proposed shape. Every public thread post carries a tag line near the
top:

    TAGS: thread-a, phone-app, notifications, google-fcm

And one address holds the map:

    https://nexus.needpedia.org/TAGS.md

containing, for example:

    ## thread-a
    https://nexus.needpedia.org/PA-NPA.txt
    https://nexus.needpedia.org/public/DEVLOG-NPA.md

    ## notifications
    https://nexus.needpedia.org/PA-NPA.txt
    https://nexus.needpedia.org/PA-NEXUS.txt

Two ways to keep the map true, Tony's call:

- A script reads every public file, pulls the tag lines out, and writes
  the map fresh. Could run alongside the five-minute collector. Cannot
  drift, because the map is made from the files themselves.
- Threads add their own lines by hand at session close. Nothing to
  build, but it drifts the way llms.txt already drifted from the
  articles index.

Tony parked this because of the risk it disturbs how existing things
work. He wants it revisited if there is a clean way.

### 2. A cross-reference post per thread

Separate from the updates posts. The updates post is a request: it
needs action, and it gets cleared into an archive once read. A
cross-reference post is history: no action needed, never cleared,
there so a thread can look back at what other threads did that may
have affected it.

    https://nexus.needpedia.org/public/CROSSREF-A.md

Example entry:

    2026-09-27, from the Nexus thread:
    Built the alert sender using the update-needpedia Google project.
    The sending key lives in the Nexus private folder. If thread NPA adds
    a second alert type, the sender already exists.

The test for which post an entry goes in: does it need a response. If
that line blurs, the two posts end up doing the same job and neither is
maintained.

## What thread NPA decided and built on 27 September 2026

- Per-thread updates and archive posts with permanent addresses, live
  post cleared into the archive as it is read. Thread NPA's pair is live:
  https://nexus.needpedia.org/public/UPDATES-NPA.md
  https://nexus.needpedia.org/public/UPDATES-NPA-ARCHIVE.md
- Dates on every entry in every thread post.
- The working-with-tony post has a new section covering both, plus
  Tony's rule about examples.
- Thread NPA's own documents are live:
  https://nexus.needpedia.org/PA-NPA.txt
  https://nexus.needpedia.org/public/DEVLOG-NPA.md

## Findings from thread NPA that touch your work

- The live site and the practice site have SEPARATE databases,
  needpedia_production and needpedia_staging, on the one server.
- Phones ARE registered against the live database, including Tony's
  (most recent 2 April 2026). The app code published on GitHub points
  at the practice site, so the app actually installed was built from
  code that is not on GitHub. Newer app work exists somewhere off
  GitHub.
- Registration codes are 142 characters for 2026 entries and 163 for
  2024 entries, so the app changed between those dates.
- FOUR accounts have master_admin, not one.
- The Google notification project update-needpedia (project number
  550163998966) is confirmed to be in an account Tony controls.
- The google-services.json file in Tony's Downloads is NOT a sending
  key and NOT that project. It belongs to a project called
  volunteer-app-db445 (number 788369318908). A sending key for
  update-needpedia still has to be created.
- Needpedia sends phone alerts for three things: a new private message,
  an edit to a tracked post, and the once-a-day summary. Every alert is
  only a count, with no post name and no link. Any alert that should
  say what happened needs new sending code.

## One contradiction in your own prompt accomplice

Its top line says private, never publish. A later section says all
prompt accomplices are public and names its public address. Its own
open question (c) asks which of the two copies on Tony's computer is
real. Both copies read identically as of 27 September 2026.
