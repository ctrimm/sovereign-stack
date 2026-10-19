# Decision Log

## 2026-10-19 — Project kickoff
- **Decision:** Build a digital-sovereignty directory/marketplace in the style of openalternative.co.
- **Evidence:** OpenAlternative does $4–8K/mo (Stripe-verified on TrustMRR) on sponsored ad slots; directories monetize high-intent comparison traffic.
- **Date:** 2026-10-19

## 2026-10-19 — Stack: Astro 7.4 + SST v3 + Node 24
- **Decision:** Astro 7.4 (latest; verified 2026-10-19), SST v3 (`sst.aws.Astro`) to AWS, Node >= 22.12 (using 24 LTS).
- **Evidence:** Astro 7.4 is the current release line (7.4 announced ~Oct 2026); SST v3 is the current major with a first-class Astro component deploying to S3 + CloudFront.
- **Date:** 2026-10-19

## 2026-10-19 — Global vendor scope, jurisdiction-first
- **Decision:** V1 catalogs EU, US, and rest-of-world vendors. Jurisdiction (company domicile, data residency) is a first-class filter, not a tag.
- **Evidence:** Sovereignty is relative to the buyer (EU buyer vs Brazilian buyer want different things); jurisdiction-filtered comparisons are uncontested long-tail SEO.
- **Date:** 2026-10-19

## 2026-10-19 — Newsletter deferred, email capture from day one
- **Decision:** No newsletter at launch. A lightweight email capture ships on day one (`PUBLIC_NEWSLETTER_ENDPOINT`), collecting addresses for a later launch.
- **Evidence:** Newsletter is a monetization amplifier, not a launch dependency; ranked comparison pages must come first. Capturing from day one avoids a cold start later.
- **Date:** 2026-10-19

## 2026-10-19 — Church-state ad policy
- **Decision:** Listings are editorial and free; inclusion is not for sale. Revenue from clearly labeled sponsorships only. Published on /about/.
- **Evidence:** Trust is the product for a directory; undisclosed paid ranking destroys it.
- **Date:** 2026-10-19

## 2026-10-19 — Design direction: Sticker Book
- **Decision:** Rebuilt the site in the "Sticker Book" direction Cory picked from three mocks (Control Room, Sticker Book, Aurora): cream paper, ink borders, hard offset shadows, sticker badges, "DITCH X → TRY Y" ticker.
- **Evidence:** Cory: v1 "looks so freaking stale... make the design look better. More fun, perhaps."
- **Date:** 2026-10-19

## 2026-10-19 — Sponsored inventory replicates the OpenAlternative playbook
- **Decision:** First-class sponsored slots modeled on openalternative.co/advertise (verified 2026-10-19): Silver $147 / Gold $297 / Platinum $597 via Revinel — inline sponsored feed cards, category placements, homepage spots. Ours: draft launch pricing Silver $149 / Gold $299 / Platinum $599 (Cory to confirm); placements = sponsored feed cards (amber sticker, rel="sponsored"), category spotlight banner pinned above comparison tables, homepage sponsored spotlight, sponsor logo strip, listing-page sidebar slot, /advertise media kit. Extras: Sovereignty Verified badge, sponsored migration guides, newsletter slot (later).
- **Evidence:** OpenAlternative's advertise page + Revinel-served inline ad units observed on their homepage; Threads post: "$4–8K/mo, software companies pay for ad slots."
- **Date:** 2026-10-19

## 2026-10-19 — AI-friendly as a first-class requirement
- **Decision:** Semantic HTML + JSON-LD on every page, `llms.txt`, and a JSON feed at `/api/listings.json`.
- **Evidence:** AI search is shifting discovery to zero-click; structured, citable pages keep the directory discoverable by assistants and agents.
- **Date:** 2026-10-19
