# DEVLOG — THREAD NPA — NEEDPEDIA PHONE APP

Public running history. Vague on account names and private paths.

Standing facts live in the prompt accomplice:
https://nexus.needpedia.org/PA-NPA.txt

## NPA1 — 26 September 2026 — look-only

First session of the phone app thread.

Read the app's actual code for the first time. Five small files,
newest change 23 October 2024. All three branches point at the same
last change, so there is no hidden notification work and nothing by
the outside developer exists in the project.

Confirmed the app signs phones up with the practice copy of the site
rather than the live one, for both login and phone registration.

Confirmed the bug where nothing appears if an alert arrives while
the app is open. Found two more: the app tries to open the browser
the moment an alert arrives while closed, and logging out leaves the
phone registered.

Read the site's own alert-sending code. Three things trigger a phone
alert, not two: a new private message, an edit to a tracked post,
and the once-a-day summary. Every alert is only a count, with no
post name and no link.

Found that a master_admin rank is a plain yes/no switch on the
account record and is very likely already included in what login
sends back to the app, so showing an admin-only button is a small
change on the app side.

Established that the app runs on the phone, the site runs on
Amazon's servers, and Google's notification service carries alerts
between them. The Google project is named update-needpedia. Who
owns it is unconfirmed.

Set up this thread's prompt accomplice and devlog.

Nothing decided about the design. Nothing changed in any code.

## NPA1, continued — 27 September 2026 — build, documents only

Read the live database from Tony's desktop. The live site and the
practice site turn out to have separate databases. Phones are
registered against the live one, Tony's most recently in April 2026.
Since the published app code registers against the practice site, the
app actually installed was built from code that is not on GitHub.
Newer app work exists somewhere off GitHub.

Found four accounts with master_admin, not one. Any admin-only page
would be visible to all four.

Confirmed the Google notification project update-needpedia is in an
account Tony controls. Confirmed the file in his Downloads is not a
sending key and belongs to an unrelated project, so a sending key
still has to be made.

Tony decided VC email alerts will send straight through Google using
that project, with no change to needpedia.org and no deploy. He also
decided the master_admin page will be a web page the app displays
rather than screens built into the app. Where that page is hosted is
still open.

Designed and built the way threads pass updates to each other: one
live updates post and one archive post per thread, at permanent
addresses, cleared into the archive as they are read, with dates on
every entry. Thread NPA's pair is live, along with a clearing tool that
copies before it empties and stops without changing anything if
anything fails.

Added a section to the working-with-tony post covering dates on every
entry, Tony's rule about showing examples with the technical and human
sides next to each other, and the updates system.

Parked, and passed to the Nexus thread as proposals: tagging public
Nexus posts with one map file, and a per-thread cross-reference post
for history that needs no action.

Two mistakes worth recording. Files were described as delivered twice
when they had not been created, which cost a round of failed commands
each time. And a web address in a copy box was pasted into the
terminal, the same thing that happened in another thread. Addresses go
on plain lines, never in a box.
