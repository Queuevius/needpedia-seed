NEEDPEDIA CAPABILITIES 2.0

Version 2.0 — 2 October 2026
Changes from 1.1: new section 17, every admin and master admin page described
section by section by Tony, with notes checked against the code. Section 12
points to it. Section 7.4 updated: the AI conversation reader is now in the
live master admin menu. Section 16 retitled.
Maintained by: Tony Brasher, Needpedia
Canonical copies: nexus.needpedia.org and github.com/Queuevius/Needpedia/wiki


================================================================
WHAT THIS DOCUMENT IS
================================================================

A list of every feature Needpedia actually has, what each one does, what has to
exist before you can use it, where to find it, and whether it currently works.

It exists because AI assistants helping Needpedia volunteers were inventing
features that don't exist and recommending features that are broken. This
document is the correction. If it is not in here, assume it does not exist.

It is deliberately not a list of things people could accomplish with Needpedia.
That list is much longer and gets built on top of this one.

READ THESE FIRST

  Needpedia Glossary — definitions of every Needpedia term, canonical
    https://nexus.needpedia.org/articles/glossary.html

  Needpedia Core Facts — mission, nonprofit status, who runs it
    https://nexus.needpedia.org/articles/core-facts.html

  Nexus front door — everything else Needpedia publishes
    https://nexus.needpedia.org/start.html

  Nexus botskills — behaviour guides for the AI assistants, 13 documents
    https://nexus.needpedia.org/botskills/

  Nexus llms.txt — full machine-readable listing of the above
    https://nexus.needpedia.org/llms.txt

  API documentation
    https://needpedia.org/apipie

  Developer wiki — code architecture. Written January 2023 and badly out of date.
    https://github.com/Queuevius/Needpedia/wiki

Where this document and the glossary disagree, the glossary wins on definitions
and this document wins on what the software does. Known conflicts are listed in
section 15.


================================================================
HOW TO READ AN ENTRY
================================================================

Every entry has some of these. Missing fields mean "nothing notable."

  What it is — plain description, no jargon.
  Prereqs   — what must already exist first. Some are enforced by the database
              and cannot be worked around.
  Who       — who is allowed to do it.
  Where     — direct URL, and the click path for when you only know the name.
  AKA       — other names this has been called.
  Status    — see below.
  Known uses— what people actually do with it.
  Limits    — what it can't do.

STATUS FLAGS

  WORKING   — deployed and confirmed.
  UNTESTED  — built and deployed, nobody has confirmed it works recently.
  BROKEN    — confirmed to misbehave. Details in the entry.
  OFF       — the code exists but is switched off.
  PLANNED   — does not exist. Listed only because people ask.

SITE-WIDE CONTEXT

Needpedia is currently dormant. Traffic and activity are near zero. A feature
marked WORKING means the software works, not that anyone is using it. Do not
tell someone "lots of people are discussing this" — check first.

THE LIVE SITE IS BEHIND THE CODE. This document was written by reading the
repository. The live site has not been deployed in some time, so a feature can
be finished, correct, and completely absent from needpedia.org. Anything marked
"on staging" below is in that state, and there are probably others nobody has
noticed yet. When it matters, check the live site rather than trusting a
WORKING flag.

DO NOT DEPLOY TO FIX THIS. The deploy configuration currently points at the
staging folder with the production line commented out, and the staging and
production settings name the same server. A deploy could overwrite staging
while appearing to update production. The lead developer was asked on
2026-09-08 which folder is live and what the exact deploy command is. Wait for
his answer. (The recent database changes are additive only — new tables,
columns and indexes, nothing dropped or renamed — which is the safe kind.)


================================================================
1. THE SHAPE OF THE SITE
================================================================

Everything content-related hangs off one three-link chain:

        SUBJECT  ──▶  PROBLEM  ──▶  IDEA

A Subject is any topic at all — a place, a movement, an artwork, a field, a
language. A Problem is something wrong within that Subject. An Idea is a
proposed solution to that Problem.

The chain is exactly three links, on purpose. People often want to list problems
WITH an idea, which would make the chain infinite and turn the site into a
labyrinth that no amount of tagging could rescue. Instead: if an idea is good
enough that people want to work on its problems, someone starts a NEW SUBJECT
POST about that idea. Then problems with it get listed under that new Subject,
while the people implementing the original stay on the original Idea post. Both
groups are working on the same idea — one refining, one building.

Because the chain is three links and always starts at a Subject, anyone who
knows the Subject can navigate to everything else.

WHY SEEING ALL THE IDEAS FOR ONE PROBLEM MATTERS

A good idea posted to social media gets buried in a day. On Needpedia it sits in
a ranked list of every proposed solution to a specific problem. Someone can see
that it is the highest-rated idea for homelessness in their city, see the
objectives and task cards attached to it, and in some cases simply start
helping. Resources can funnel to where they do the most good.

THE DATABASE ENFORCES THIS

  - A Problem CANNOT be created without a Subject.
  - An Idea CANNOT be created without a Problem.
  - An Idea attaches to EXACTLY ONE Problem. Not several.

This is why creating a post by hand is more work than people expect, and why
Lotte creating posts on a user's behalf matters so much — see section 7.


================================================================
2. POSTS
================================================================

2.1 SUBJECT POST
  What it is: the top of the chain. Any topic.
  Prereqs: none. A Subject can be created from nothing.
  Who: any registered user.
  AKA: "Area" — the old name, still used in the January 2023 wiki and in some
       database fields. Called "subject" in the code and in URLs.
  Status: WORKING

2.2 PROBLEM POST
  What it is: a problem within a Subject.
  Prereqs: an existing Subject post.
  Who: any registered user.
  Where: all problems, highest-rated first. Use this link verbatim — it carries
  the post type and the sort order, and an AI will not reconstruct it correctly
  from scratch:
    https://needpedia.org/posts/search_result?active_tab=posts&q%5Btitle_cont%5D=&sorted_by=Highest-Rated&post_type=problem&access_type=Public&skill_tags=&location_tags=&lat=&long=&location_mode=text&q%5Buser_first_name_cont%5D=&tree_url=&resource_tags=&commit=Search
  Status: WORKING

2.3 IDEA POST
  What it is: a proposed solution to a Problem. The richest post type.
  Prereqs: an existing Problem post, which needs an existing Subject post.
  Who: any registered user.
  Contains beyond a normal post: an image carousel, resource tags, objectives,
  interested users, related content, and its own comments section.
  Status: WORKING

2.4 QUICK SHARE POST
  What it is: an Idea-style post that needs no parent.
  Prereqs: none.
  Limits: cannot be private, cannot be curated, cannot carry a map location.
  Known uses: ideas whose Problem and Subject aren't obvious yet.
  Status: WORKING — but it is UNTESTED whether Lotte can create these.

2.5 HAVE / WANT POSTS
  What it is: lists of goods and services you have or want, on your profile.
  Supports barter and mutual aid.
  Prereqs: two-factor authentication enabled on the account.
  Why the 2FA wall: trivially easy to abuse otherwise.
  Where: https://needpedia.org/posts/have
         https://needpedia.org/posts/want
         Also in the profile sidebar.
  Status: WORKING

2.6 GEOMAXXING POSTS
  What it is: a post pinned to a location on a map. Ideas tied to physical
  places.
  Where: in the top nav bar, or https://needpedia.org/posts/geo_maxing_posts
  Status: WORKING

2.7 LAYERS
  What it is: a discussion space attached to a post. A layer is itself a post.
  Any post can have any number of layers.
  Prereqs: a post to attach to, which is not private or curated.
  Who: anyone, on any post that isn't private or curated.
  Where: the "Layer" button at a post's upper right.
  Known uses: expert layers, where specialists evaluate an idea.
  Lived-experience and identity layers, where people who've experienced
  homelessness, or women, or disabled people discuss an idea amongst themselves
  and then bring input back to the public layer. NVC layers — see section 9.
  Limits: LAYER TYPES ARE LABELS ONLY. The software does not know an expert
  layer from any other kind and does not restrict who can post in one. All of it
  is naming convention today.
  Status: WORKING

2.8 SOCIAL MEDIA POST TYPE
  What it is: a post type that exists with no parent.
  Status: WORKING

2.9 POST PROTECTION
  Four independent switches on a post:
    Private          — only named people can see it.
    Curated          — anyone can see it, only named people can edit it.
    Editing disabled — nobody can edit it.
    Layering disabled— nobody can add layers to it.
  Status: WORKING

2.10 VERSION HISTORY
  What it is: every edit is kept. You can restore an old version, report a
  version, or request a version be deleted.
  Status: WORKING

2.11 DELETION AND RESTORE
  What it is: deleting a post doesn't destroy it. Admins can list deleted posts
  and restore them.
  Status: WORKING

2.12 TRACKING A POST
  What it is: get notified about activity on a post you care about.
  Triggers — three, individually switchable: someone edits the post; someone
  adds an expert layer; someone adds a related wiki post.
  Note: "expert layer" exists here as a named notification trigger even though
  layers are otherwise unlabelled (see 2.7). Half a feature.
  Status: WORKING

2.13 TAGS
  What it is: two separate tag systems — ordinary tags and resource tags.
  Where: https://needpedia.org/tags/YOURTAG
  Status: WORKING

2.14 POST LENGTH
  Posts have a 2,000-character cap defined in the code.
  Status: WORKING


================================================================
3. TOKENS
================================================================

3.1 WHAT A TOKEN IS
  An icon dropped into the body text of a post at the exact spot it concerns,
  added via the Edit button. Clicking it opens the discussion attached to that
  spot.

  THERE ARE EXACTLY THREE TYPES: NOTE, QUESTION, DEBATE.

  There is no fourth type. A "myth token" appeared in earlier Needpedia
  documents and never existed — it was invented by an AI and spread through the
  files before being removed. If you see a fourth token type anywhere, that
  document is wrong.

3.2 NOTE TOKEN
  Context, a source, or a correction, attached to a specific statement.
  Status: WORKING

3.3 QUESTION TOKEN
  Asks for clarification on a specific word or statement. Other users answer.
  Status: WORKING

3.4 DEBATE TOKEN
  A structured argument. Replies come in three kinds — FOR, AGAINST, and
  NEUTRAL — and each reply can be voted up or down.

  Why this matters more than it looks: because arguments are rated individually
  on all three sides, you can see exactly which concerns carry the most weight,
  rather than just who won. That makes it possible to write a new idea post that
  addresses the real objections — a hybrid that more people can live with. The
  goal on Needpedia is not to defeat the other side. It is to find ideas
  everyone can work with, so the problem gets solved for good.
  Status: WORKING

3.5 WHERE TOKENS WORK
  In posts, and in group discussion topics. Not everywhere.
  Status: WORKING

3.6 YOUR OWN TOKEN ACTIVITY
  https://needpedia.org/note_tokens
  https://needpedia.org/question_tokens
  https://needpedia.org/debate_tokens
  Status: WORKING


================================================================
4. WORKING ON AN IDEA TOGETHER
================================================================

4.1 OBJECTIVES
  What it is: a concrete, completable step listed inside an idea post. Up to 350
  characters. Objectives nest — you can reply to one — though most replies are
  ordinary discussion rather than sub-objectives.
  Prereqs: a post to attach to.
  Limits: THERE IS NO "COMPLETED" STATE ON AN OBJECTIVE. No checkbox, no done
  flag, nothing in the database. The glossary says followers are notified when
  an objective is completed; that cannot currently happen.
  Status: WORKING as a list. The completion half is PLANNED.

4.2 INTERESTED USERS
  What it is: raise your hand to say you want to be part of a project.
  Status: WORKING

4.3 RELATED CONTENT
  What it is: a section on an idea post where people add links and material.
  Status: WORKING

4.4 COMMENTS
  What it is: threaded comments with replies, on posts and task cards.
  Editable. Deleting hides rather than destroys. Flaggable.
  Status: WORKING

4.5 RATINGS AND THE LOL VOTE
  What it is: the rating scale is 0 to 5, PLUS LOL. Lol is for ideas that are
  funny rather than good — someone can give a joke proposal a Lol and a 0, which
  keeps humour from inflating serious rankings.
  THIS IS THE POLLING SYSTEM. There is no separate voting feature. Rankings of
  ideas under a problem come from these ratings.
  BROKEN: ratings and Lol are currently mutually exclusive. Giving something a
  number clears your Lol, and giving it a Lol clears your number. You should be
  able to do both.
  Status: BROKEN — usable, but behaves wrong.

4.6 LIKES AND SHARES
  Separate from ratings.
  Status: WORKING


================================================================
5. GROUPS AND TASK CARDS
================================================================

5.1 GROUP ACCOUNTS
  What it is: an account run by an organization or team rather than a person.
  Has a logo, members, and an owner.
  Four ways in: open join, request to join, invitation, or being added. Requests
  and invitations can be accepted or rejected; members can leave.
  Where: https://needpedia.org/groups
  Limits: the group interface needs a full redesign. Known and acknowledged.
  Status: WORKING

5.2 GROUP DISCUSSION TOPICS
  What it is: threaded discussions inside a group. Tokens work in them.
  Status: WORKING

5.3 GROUP LAYERS AND SUB-GROUPS
  What it is: groups can have layers and child groups, the same way posts can.
  Status: WORKING

5.4 TASK CARDS
  What it is: a card describing a piece of work a group needs done.
  Fields: title, description, required skills, location (city, region, country,
  postal code, and map coordinates), hours, priority, status, assignee,
  check-back date, images, comments.
  Priority: Casual, Pressing, Urgent.
  Status values: Available Tasks, Under Progress, Completed Tasks.
  Prereqs: A GROUP. Task cards can only exist inside a group today.
  Where: https://needpedia.org/tasks
         Also searchable from the main search as their own result type.
  Known uses: this is the intended centre of volunteer recruiting — a person
  arrives, finds a task matching their skills and city, and starts.
  Planned: task cards on all wiki post types and on individual accounts, so a
  person can ask for help without running a group. Also a dedicated visual
  treatment — the cards are meant to look like playing cards.
  Status: WORKING


================================================================
6. TIME BANK
================================================================

  What it is: exchanging help using time credits instead of money.
  How it works: a gig has a title, an area tag, a description, an hours amount,
  and images. Gigs move through pending, active, in progress, awarded, and
  disabled. Every user starts with 1 credit hour; credits move when gigs are
  offered and awarded.
  Where: https://needpedia.org/time_bank — also in the top nav bar.
  Limits: THE TIME BANK AND TASK CARDS ARE NOT CONNECTED. Task card hours do
  nothing to anyone's credit balance. These are two separate systems that look
  like one.
  Planned: rebuild so the time bank works like a pool of task cards, and connect
  it to Have/Want.
  Status: WORKING — built, essentially unused.


================================================================
7. AI ASSISTANTS
================================================================

Three assistants, all named after librarians who resisted fascism.

NAMING WARNING: the conversation records do NOT use these names. They are
labelled "Needpedia Assistant", "Needpedia Greeter" and "VC Email Assistant."
Which label belongs to which assistant is unconfirmed — the lead developer was
asked on 2026-09-08. Anything reporting usage per assistant is unreliable until
that is settled.

7.1 FLORENCE
  Greets visitors who aren't logged in. Answers questions, helps people decide
  whether to join.
  Status: WORKING

7.2 LOTTE
  The main assistant for logged-in users. Can find, create, and edit wiki posts
  through the API on a user's behalf. Works in many languages.
  Why she matters most: the Subject-Problem-Idea chain is mandatory and tedious
  to build by hand. The goal is that a person tells Lotte their idea, she checks
  whether something like it is already posted, and if not she creates the whole
  chain for them.
  Where: https://needpedia.org/ai
  Newly on staging: Lotte can translate whole pages for a user, and can
  re-explain a page in different modes, including a child-safety mode, an
  analysis mode, and a silly mode. Anything the assistant can accommodate.
  Status: WORKING. The automatic full-chain creation is UNTESTED — unconfirmed
  whether it currently does this.

7.3 ADELE
  Volunteer coordination, working in the public email system alongside the human
  Volunteer Coordinator.
  Where: https://vc-email-five.vercel.app/inbox
  Note: this inbox is public on purpose. Anyone, including Adele and every
  volunteer, can read it, so people can see what's going on and see task cards
  immediately. For private or anonymous matters, use Needpedia@gmail.com.
  Status: WORKING

7.4 HOW ASSISTANT INSTRUCTIONS ARE MANAGED
  Instructions are versioned in the admin panel. You activate a version, and you
  can roll back to an earlier one.
  Conversations are saved — every AI conversation since November 2025 is stored
  on the live database, one record per conversation and one per message,
  including the full question text, which assistant answered, and whether the
  person was signed in. As of 2026-09-08 that amounts to 11 questions ever, 2 of
  them in the preceding week, most recent 2026-09-03. So the assistants HAVE
  been used, barely, and all of it is readable.
  An admin page for reading those conversations — with search by text or email,
  filters by assistant and date, and full transcripts — is linked in the master
  admin menu on needpedia.org as of 2 October 2026 (AI Conversations). See
  section 17.
  The assistant is told when it is someone's first ever conversation, so a
  one-time notice (for example, telling people their conversations are recorded)
  needs wording written, not software built.
  People who aren't logged in can use the assistant.
  There is a usage budget — a set number of AI messages for logged-in users and
  a different number for guests.
  Assistants can be given reference documents, PDF ONLY.
  Eco mode / full mode: Florence and Lotte can run on a more powerful model or a
  much lower-energy one.
  Status: WORKING


================================================================
8. GETTING INFORMATION IN AND OUT
================================================================

8.1 PUBLIC API
  List posts, get one post, create a post, update a post.
  Docs: https://needpedia.org/apipie
  Status: WORKING

8.2 INCOMING WEBHOOK
  A URL that creates a post when something posts to it.
  Status: WORKING

8.3 OUTGOING WEBHOOKS
  Register a URL in the admin panel and it gets notified whenever a post is
  created. Each one has a shared secret and an expiry date.
  Status: WORKING

8.4 MOBILE APP API
  A separate interface for the phone app: login, device registration, FAQs,
  how-tos, posts, AI chat.
  Status: WORKING as an interface. See 10.2 for the app itself.

8.5 SEARCH
  Covers posts and users, filterable by post type, with task cards as their own
  result type.
  BROKEN: the results page opens whichever tab has more results rather than
  defaulting to posts. Search a common word that matches many usernames and you
  land on People.
  Status: BROKEN — usable, opens on the wrong tab.

8.6 MACHINE-READABLE SITE FILES
  No sitemap. No meaningful robots.txt. No llms.txt on needpedia.org.
  The Nexus does have one: https://nexus.needpedia.org/llms.txt
  Status: PLANNED for the main site.


================================================================
9. NVC
================================================================

Nonviolent Communication — observations without judgment, feelings, needs,
requests. Needpedia uses it to keep hard conversations productive.

THERE IS NO NVC FEATURE IN THE SOFTWARE. NVC on Needpedia today is a layer that
people agree to use in NVC form, supported by the conversational NVC botskill
that guides the AI assistants:
  https://nexus.needpedia.org/botskills/conversational-nvc.html

Planned: NVC layers that reject entries which break NVC form. This is structure
for how positions get expressed, not censorship of positions.

Status: convention today. Enforcement PLANNED.


================================================================
10. CONNECTING TO THE WIDER WORLD
================================================================

10.1 FEDIVERSE
  Needpedia accounts can be followed from Mastodon and similar. Users can follow
  remote accounts. There's a fediverse feed and a federated inbox.
  OFF: automatic publishing of new posts outward is switched off in the code —
  the line that would do it is commented out. Unconfirmed against production.
  Status: UNTESTED inbound. OFF outbound.

10.2 PHONE APP
  Status: the app is NOT PUBLISHED. There is no page telling users where to get
  it, and installing it currently triggers security warnings on phones.
  Why it matters: the app is how people come back. Somebody shares an idea and
  then needs to hear what happened to it — replies, messages, activity on posts
  they're tracking.
  Related: the notification settings interface needs a full redesign before this
  is worth pushing.

  PUSH NOTIFICATIONS — the plumbing is complete and unused. The site can store
  registered phones, accept registrations, and send messages using Google's
  current method (not the one retired in 2024). Today it only fires on two
  events: a private message, and an edit to a post you're tracking. And only for
  accounts set to instant notifications rather than daily.
  Two things stand between this and working: the phone app registers devices
  against STAGING rather than the live site, and sending from the live site
  needs a Google key file and a setting present on the server, neither of which
  has been confirmed.

10.3 SIGN IN WITH AN OUTSIDE ACCOUNT
  Status: BROKEN / incomplete. The intent was Facebook and Google. The code
  contains Twitter.


================================================================
11. PEOPLE
================================================================

  Profiles — pictures, about, details. WORKING
  Wall, feed, activity stream — https://needpedia.org/wall and /feed. WORKING
  Friends and connection requests — includes block and unblock. WORKING
  Direct messages — real-time. WORKING
  Notifications — on-site notifications work; the interface needs a redesign.
    Push notifications to phones are wired but only fire on private messages and
    tracked-post edits. See 10.2. WORKING
  Two-factor authentication — QR code plus backup codes. Required for
    Have/Want. WORKING
  Impacts — https://needpedia.org/impacts — showcases what people have
    contributed, the way GitHub credits code. Builds visible track records and
    networks of trust. Some people are rockstars and everyone should know it.
    Assigned from the admin panel. WORKING

  Note: the glossary writes this last one as /impact. The working path is
  /impacts, plural.


================================================================
12. RUNNING THE SITE
================================================================

  Every admin and master admin page, section by section: see section 17.

  Admin and master admin — two permission tiers. WORKING
  Freeze accounts — stops all sign-ins and sign-ups. WORKING
  Freeze posting — stops all post creation and editing. WORKING
  Nuclear note — one switch replaces the entire site with a message, for if
    something forces Needpedia offline. WORKING
  Banned terms — a term list content is checked against. The list needs
    updating. WORKING
  Blocked IPs and users — WORKING
  Failed login tracking — records FAILED login attempts only, and blocks an
    address after more than ten. Useful as an intrusion signal. WORKING
  Successful login tracking — DOES NOT EXIST. The routine that writes login
    records exits before writing if the password is correct, and the flag it
    stores is hardcoded to "failed". The single login timestamp on an account is
    written only the very first time that account ever logs in. No query can
    count logins, on any dashboard, ever. Any document implying otherwise is
    wrong.
  Flags — on posts, comments, versions, and groups, with admin review. WORKING
  Deletion requests — a formal queue. WORKING
  Announcements — tagged new, fix, or update. WORKING
  Tutorials — pop-ups tied to specific pages, marked as seen. Intended to be
    usable by the AI assistants; not yet. WORKING
  How-tos and FAQs — managed from admin, shown on the homepage. WORKING
  Email templates — WORKING
  Homepage video and image buttons — managed from admin. WORKING

12.1 QUESTIONNAIRES — "SAFE MODE"
  What it is: a gate for weeding out bots and making sure you know everyone
  joining. A person submits an answer and waits for approval.
  Status: UNTESTED — hasn't been exercised in years. Unconfirmed whether
  approval actually works.

12.2 THE FEEDBACK FORM
  Where: https://needpedia.org/users/edit — a "Provide Feedback" button below
  Save Changes. Also at the bottom of the post, comment, objective, related
  content, interested users, and topic forms.
  What it actually is: a SURVEY, not a feedback box. It shows a fixed set of
  admin-written questions with multiple-choice answers. There is no way to type
  a free-form report. If no questions have been entered in the admin panel, the
  page renders completely empty.
  Requires being logged in.
  DO NOT SEND BUG REPORTS HERE. See section 14.
  Status: WORKING

12.3 THE CATCH-ALL SUBJECT AND PROBLEM
  Two pages have create buttons that file a new post under a pre-configured
  catch-all parent rather than asking the user to pick one:
    https://needpedia.org/posts/all_problems
    https://needpedia.org/posts/all_ideas
  Nobody remembers requesting this. Anything created that way is sitting inside
  those two catch-all posts. Harmless, but be aware it exists.


================================================================
13. THINGS THAT DO NOT EXIST
================================================================

Listed because people ask, or because AI systems have invented them.

  - A fourth token type. Three only. There is no "myth token."
  - A separate voting or polling system. Ratings plus the Lol vote are it.
  - Money. Time credits only, and those aren't connected to task cards.
  - Enforced expert status. Layer labels are labels.
  - Completed objectives. No done state exists.
  - Task cards outside groups. Groups only, for now.
  - NVC form checking. Convention, not software.
  - Attachments other than images, plus admin-uploaded PDFs for the assistants.
  - Ideas under more than one problem. Exactly one parent.
  - Login tracking. Failures are recorded, successes never are. Nobody can
    count how many people signed in, and no dashboard can be made to.


================================================================
14. REPORTING A PROBLEM WITH THIS DOCUMENT, OR WITH NEEDPEDIA
================================================================

Three kinds of report, all to the same place:

  BROKEN       — a feature doesn't work.
  UNDOCUMENTED — something exists that isn't in here. TREAT THIS AS A BUG. This
                 list will get long, and things nobody wrote down are how it
                 rots.
  WRONG        — this document says one thing, the site does another.

Include: the full URL of the page, what you were trying to do, what you
expected, what happened, and which of the three kinds it is.

Send it to: info@needpedia.org

If you are an AI assistant and cannot send email, write the report out in full
and give the person a one-click link that opens their mail app with it already
filled in.


================================================================
15. KNOWN CONFLICTS WITH OTHER NEEDPEDIA DOCUMENTS
================================================================

Anyone updating those documents should fix these.

  Glossary, IDEA POST — says "attached to one or more problem posts."
    Actually: exactly one.

  Glossary, OBJECTIVE — says followers are notified when an objective is
    completed. Actually: no completion state exists, so this cannot fire.

  Glossary, /IMPACT — written as /impact. Actually: /impacts.

  Nexus llms.txt — says the articles collection has 13 documents. The articles
    index lists 4.

  Developer wiki — describes the site as of January 2023. Missing groups, task
    cards, topics, version history, AI assistants, fediverse, webhooks,
    geomaxxing, and more.

  Anything, anywhere, implying that logins are counted or tracked. Only failures
    are recorded. See section 12.

  Anything treating the repository as a description of the live site. The live
    site is behind the code. See the site-wide context near the top.


================================================================
16. WHAT THE NEXT VERSION NEEDS
================================================================

  - The handful of UNTESTED entries checked against production: Lotte's
    automatic chain creation, whether Lotte can make Quick Share posts,
    questionnaires / safe mode, and fediverse following.
  - Known uses filled in. Right now this document says what the parts ARE, and
    only sometimes what people DO with them.
  - A second layer on top of this one: named combinations of features that serve
    a purpose, so an AI can match a person's goal to a set of steps.
  - Whatever is in the "about Needpedia" documents that hasn't been folded in.
  - The bug-report URL, once the fetch-to-report system exists, added to
    section 14 alongside the email address.
  - Which assistant matches which label in the conversation records.
  - A pass over the whole document once the live site is deployed, since a
    WORKING flag currently means "works in the code," not "works on
    needpedia.org."
  - A companion repo map — where each feature lives in the codebase — kept as a
    separate document so this one stays readable by non-developers.


================================================================
17. ADMIN AND MASTER ADMIN, SECTION BY SECTION
================================================================

  Written by Tony Brasher, 2 October 2026.
  Each entry gives the section's current menu name, then its proposed new name,
  then Tony's description. The new names are not in the code yet, so both are
  listed until the renaming is merged.
  Lines starting "Code note:" were added from reading the code (commit 26563af,
  11 September 2026). They are not Tony's words.
  Master admin: https://needpedia.org/master_admin
  Admin: https://needpedia.org/admin


MASTER ADMIN

AI Conversations → AI Chat Transcripts. Search by words, email, or name, and filter by assistant and date. Clicking a person or guest opens all their AI conversations on one page.

Ai Prompts → AI KBs. Saved in versions, with a button to switch a version on.
  Code note: switching a version on switches the previous one off.

Admin Histories → Admin Activity Log. Who did what, to which item, from which internet address. It only covers actions taken in /admin; nothing done in /master_admin is logged.
  Code note: it also records every time an admin opens a person's profile from /admin.

Preformatted Messages → New Post Starter Text. Text that fills the editor automatically when someone starts a post. It's tied to a post type, but the code only uses the one for ideas.

How Tos → How-To Entries. Question and answer pairs that display in the how-to section on Needpedia's homepage.

Impacts → Contributor Badges. A badge and description given to a person. It shows on their profile and on /impacts. This section has not been developed yet.

Questions → Edit Signup Questionnaire. This lets you edit questions inside the signup questionnaire. This feature was used to screen applicants but may be out of order.

Questionnaires → Signup Approval Gate. Only the first questionnaire is ever used. Its "active" checkbox decides whether newcomers wait for approval. Unticking it makes confirmation emails go out automatically again. The bot check still runs either way, (we were seeing a ton of bots), but the nonsense-answer filter would stop, (the bots gave us gibberish answers which made this feature very effective at weeding them out).
  Code note: "first" means the questionnaire that was created first. Making a new questionnaire changes nothing while the first one still exists.

Faqs → FAQs. Question and answer pairs users can see in /faq section.

Home Videos → Homepage Video Updater. This lets you choose what video shows up on Needpedia's homepage.

Admin Notifications → Homepage Messages. Messages on the homepage aimed at one of three audiences: everyone, newcomers, or logged-out visitors.

Admin Notices → Editable Site Text. Named blocks of text you can edit without code. Only one is in use: the message shown next to two-factor setup. I have no idea why we set this up or what how it currently works. It's possible some of this code came from a previous project and is purely vestigial.
  Code note: the block in use is the one named OTP_message.

Announcements → Site Announcements. Each has a title, description, type (new, fix, or update), and publish date.

Answers → Newcomer Answers & Approval. Lets you see what each newcomer wrote. The approve button marks the person approved and sends their confirmation email. There's also delete-selected and delete-everything. This feature lets you screen who gets to create an account.

Comments: Lets you see all comments. Not currently functional.

Connections: Lets you see which users are friends. This will help with analystics and detecting bot activity.

Deletions → Post Deletion Request Log. Written automatically every time a post is deleted: who deleted it and what went with it, such as child posts and layers. It's a record, and possibly a request queue. It's unclear if it deletes child posts. The idea is we want it to be hard for someone to destroy someone else's posts.
  Code note: it is only a record, written at the moment of deletion. Deleting hides a post rather than erasing it, and it can be restored from /admin Posts → Deleted Posts. Child posts are hidden too: deleting a Subject hides its Problems, their Ideas, and all their layers; deleting a Problem hides its Ideas and their layers; deleting an Idea hides its layers. Not yet checked: who is allowed to delete someone else's post.

Feedbacks → Feedback Survey Submissions. Who filled in the survey. Unsure if still functional as AI concluded: "I found no admin page anywhere for writing the survey's questions."
  Code note: if no survey questions exist, the survey page shows up empty.

Flags → Flagged Content. Shows you stuff that's been flagged

Gigs → Time Bank Gigs. Needpedia has a time bank that should help people help each other, and to ask for help.

Guests → Logged-Out Visitor Count. One record per internet address of anyone using the site without logging in, mainly for counting their AI messages. It also includes one built-in "guest" that stands for Adele's public inbox.

Notifications → All User Notifications.

Posts → All Posts. Its private-posts link actually sends you to the Admin version.

Post Tokens → Note, Question, & Debate Tokens. Let's you see what tokens people have posted so far.

Settings → Emergency Switches. Holds exactly three things: stop all sign-ins and sign-ups, stop all posting, and the nuclear note with its on switch. (replaces the site with a message of your choosing. Shouldn't delete DB or anything like that. This tool is ideal for automated DMCA bot attacks)
  Code note: the nuclear note only shows when its switch is on AND the message isn't empty. It deletes nothing. The admin pages keep working while it's on, so it can be switched back off.

Token Ans Debates → Debate Replies. It is unclear what this section was for.
  Code note: it lists every reply left on debate tokens, each marked for, against, or neutral.

Tutorials → Tutorial Mode. These are basically Page Pop-Up Guides. Each has the page it appears on, the text it shows users, and a show/hide switch.

User Assistant Documents → AI Reference PDFs. Each has a title, description, and change notes. *This section is old, we now use [Ai Prompts → AI KBs] to upload new KBs for AI.

User Gigs → Gig Accepters. Lets you see who took which time gig. (This feature is easy to abuse)

Users → People & Accounts. Every account. It has a "not yet confirmed" view (the Newcomers list), a resend-confirmation button, and bulk delete, (good for bots). A person's page shows the admin log entries about them. *This section lets you see conversations they have while logged in. This can be a powerful tool for supporting people and improving how your community does things but you also need to make sure people know their AI convos are being saved and aren't private. Always design around consent and safety.
  Code note: a person's page also has the "Login As User" button (see the additional notes below) and an "AI Chat History" button. The people list has a "Remaining Tokens" column: how many AI messages each person has left.

Webhook Configurations → (no description yet)
  Code note: the outgoing version. Each entry is a web address that gets a message every time a post is created, with a secret, an on switch, and an expiry date.

Webhooks → Incoming Post Address On/Off. A switch for the address other apps can send to in order to create a post. The goal is to make global networks of Needpedia instances that back each other up so that no one gov or billionaire can shut this movement down. Fortunately you have AI to help you and all this tech is literally built around the creation of a solution engine.


ADMIN

Blocked Ips. Internet addresses that are blocked from signing in. An address gets added automatically after more than ten failed login attempts. Each one has an unblock button.

Button Images → Homepage Button Images. This lets you update the pictures on the two big homepage buttons, "Quick post" and "Archive post."

Email Templates → Site->User Email Templates. The wording of five emails the site sends automatically: confirm your account, reset your password, unlock your account, your email was changed, and your password was changed. I'm unsure if you can still make all 5 types.
  Code note: all five still work. Each is found by the exact name typed into its Name box: confirmation_instructions, reset_password_instructions, unlock_instructions, email_changed, password_change. If no template exists under one of those names, the site sends its built-in plain wording instead. For email_changed, only the subject line can be customized; the body always uses the built-in wording.

Banned Terms. The list of words that posts are checked against.

Posts. *Similar to the feature by a similar name in master admin, but with two extra buttons:
-"Deleted Posts" shows everything that's been deleted, and each one has a Restore button.
-"Upload" takes a spreadsheet (CSV file) and creates many posts at once. It files each row under a Subject and Problem by matching their titles.
Master admin's private-posts link also lands on this page.

Users. *Different from master admin's version in several ways:
Extra: a "User History" button that shows everything the person has done on the site, which you can narrow to a date range.
Extra: a notes box for writing a private admin note about the person.
Missing: the "AI Chat History" button.
Missing: the "Login As User" button. It's switched off here but live in master admin.
Opening someone's profile from here gets written to the activity log.

Deletion Requests. People asking for an old version of a post to be erased. Each request has a Destroy button that erases that version.

Post Versions. Every saved edit of every wiki post. In case anyone decides to try vandalizing posts, users can simply 'revert to previous' to undo any damage. It will also be interesting seeing how pages evolve over time.

Groups. Group accounts: their name, logo, members, and owner. Groups are where task cards are located, which are central to actual workflows for not just users, but the volunteers who will hopefully be helping you too. You can list all your tasks in dedicated groups then have AI assist people in organizing more easily and more effectively.

Code note: sections with the same name in both places that aren't described separately above (Post Tokens, Token Ans Debates, Connections, User Gigs, Flags, Comments, Gigs, Answers, Notifications, Feedbacks, Deletions) work the same in /admin as in master admin, except that everything done in /admin is written to the Admin Activity Log.


ADDITIONAL NOTES BETWEEN THE TWO SECTIONS

Invitations. Invitations sent for people to join groups. *We need to make a URL / linkable version of this to help people invite others to help them more easily.
  Code note: separate from this, the code has an email invitation to join Needpedia itself; a person's admin page shows who invited them. That email's wording isn't in Email Templates.

Users → "Login As User" button. It lets a master admin sign in as that person and see the site exactly as they do, and it isn't logged. *Which needs to change, this is a work in progress. Even the actions of master_admins should be logged. Or should I say *Especially*.

Flags → Flagged Content. On both admin and master_admin this section has an option to delete the reported item itself, not just the report.



Needpedia is an open-source nonprofit civic collaboration platform, fiscally
sponsored by The Know Agenda Foundation. This document may be copied and
republished freely.