# DEVLOG - PU THREAD (PROJECT UNSTOPPABLE)

Public. Nothing in here that would help someone get in. Kept vague on
account names and private paths.
Standing facts, rules and loose ends: https://nexus.needpedia.org/PA-PU.txt

----------------------------------------------------------------

## PU 1 - 28 and 29 September 2026

- Thread started from a "blueprint" for a federated Needpedia written
  by other AIs. Checked it against the real code instead of trusting it.
- Read Needpedia's main code (master, commit 26563af, 11 Sep 2026):
  the push to other servers (webhooks), the receiving door, the
  Fediverse link, the reading door and the Docker packaging. What
  exists and what it lacks is written up in PA-PU.txt. Whether this
  code is what runs on needpedia.org is not confirmed yet.
- Found functional problems: echo loop, a dead backup slowing the main
  site, ID numbers that do not match between servers, a stop-sending
  switch nothing reads, one shared password for every partner.
- Found security problems and wrote a private note for the lead
  developer. Details are not published.
- Tony set his requirements (in PA-PU.txt).
- Researched tools and precedents: Kiwix and zimit (offline copies),
  Kiwix Hotspot (Raspberry Pi wifi box), IPFS (Wikipedia mirrors for
  Turkey and Myanmar), Ibis (federated wiki), Standard Webhooks (signed
  messages), UUIDv7 (worldwide IDs), rack-attack (rate limits), Tor
  onion addresses, Cloudflare switch-over, PostgreSQL filtered copying.
- Proposed a five-step staircase plan, from "readable anywhere" to
  "everyone can post anywhere". Tony has not chosen how far to go.
- Read the Nexus thread's first update to PU (aging foundation, John's
  test-site package, planned build watchers) and archived it on
  29 Sep 2026.
- Caught up with the working-with-tony post, edition 8: tags lines on
  every note, one archive file per thread, # at the start of every
  line in a box meant for a chat.
- Tony, 29 Sep 2026: box labels such as TERMINAL go above the box,
  never inside it. Passed to the Nexus thread for the shared post.
- Made PU's prompt accomplice, this devlog, and the PU 2 handoff.
- Next (PU 2): design a series of milestones John can build with AI
  help toward the optimized plan, consulting John's thread.
