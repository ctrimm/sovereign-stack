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

## 2026-10-19 — Sponsored media kit (gallery + video)
- **Decision:** Built the sponsored media kit Cory asked for: `MediaGallery.astro` (main stage + right-hand thumbnail rail, prev/next arrows, keyboard nav, aria carousel semantics, lazy click-to-play video) rendered on sponsored listing pages via new frontmatter (`gallery[]`, `videoUrl`, `videoTitle`). Video allowlist: YouTube (incl. youtu.be/shorts/embed) + Vimeo, converted to privacy embeds; non-matching URLs fail closed. Tier mapping: Silver up to 3 images / Gold up to 6 / Platinum up to 8 + video embed as hero. Marketed on /advertise: media-kit bullets on all tier cards + dedicated "The sponsored media kit" section with live labeled demo gallery (3 generated example images in public/sponsors/example/) + specs/ground-rules box. Verified live via temp-sponsored Plausible listing (video hero slide, thumbnail rail, arrow nav, active-thumb highlight), reverted before push — no real sponsors exist.
- **Evidence:** Cory: "I think if you do a certain tier you should maybe be able to embed a video as well... what are your thoughts on that for a differentiator" → agreed to build; "be sure to call it out in all the advertising text, marketing language."
- **Date:** 2026-10-19

## 2026-10-19 — Two essays + artwork for all Insights
- **Decision:** Added the two queued essays: "Europe's AI sovereignty playbook" (chips→clouds→models→apps, incl. Aleph Alpha/Cohere cautionary tale) and "Your phone is the weakest layer" (mobile sovereignty stack: /e/OS, CalyxOS, Sailfish, 4 hardware theories). Generated 9 sticker-book-style hero images (one per essay, 16:9, no text) via media pipeline; reviewed firsthand before shipping. Wired into Insights: `image` frontmatter field, hero figure on essay pages, thumbnails on index cards, og:image + twitter:image (summary_large_image) via new Base `image` prop.
- **Evidence:** Cory: "let's add those two essays. also, we need images for each, so, make those and include them."
- **Date:** 2026-10-19

## 2026-10-19 — Data essay + living /stats dashboard
- **Decision:** New Insights essay "The state of the sovereign stack: what 359 listings taught us" (Article JSON-LD) built on real computed corpus stats: US 68 vs DE 67 dead heat, 55% EU-domiciled, AWS most-replaced (39), AI tools 2nd-largest category (58), 38% open source / 34% self-hostable, US listings 53% open source (highest share), freemium dominant (141). New **/stats** page: build-time-computed dashboard (domicile bars, open-source share by domicile, category grid, pricing mix, most-replaced incumbents) with Dataset JSON-LD; linked from essay, footer, llms.txt. Caught and corrected stale jurisdiction count (36 → 41). 623 pages.
- **Evidence:** Cory picked "Write the data piece + stats page" from the options widget.
- **Date:** 2026-10-19

## 2026-10-19 — Filters + batch F
- **Decision:** Built the missing filtering: new `FilterBar` component (domicile select, pricing select, open-source-only, self-hostable-only, reset, live result count, empty state) on all category pages and all alternatives pages; filters both comparison tables and card grids client-side, full content still statically rendered for SEO. Content: +32 listings (359 total, 21 categories incl. new **OS & firmware**): sovereign email depth (Fastmail AU, Hushmail CA, WEB.DE/freenet/mail.de DE, Laposte.net/Mailo FR, Soverin NL verified, Zoho IN, Seznam CZ, Ukr.net UA, 1984 IS, Cyon CH), EU AI Act tooling (LatticeFlow CH, Saidot FI, 2021.AI DK, Modulos CH, Holistic AI GB verified, Credo AI US), OS/firmware (/e/OS FR, CalyxOS US, Sailfish FI, Ubuntu GB, NixOS NL verified, Qubes OS PL, Dasharo PL, 9elements DE verified, Pop!_OS US, Zorin OS IE verified, elementary OS US, KDE DE, GNOME US). 621 pages.
- **Evidence:** Cory asked whether specific filtering existed (it didn't — only homepage search) and commissioned the three content veins.
- **Date:** 2026-10-19

## 2026-10-19 — Batch E: sovereign clouds + /submit flow
- **Decision:** +41 listings (327 total; 578 pages). Batch E focused on commercial cloud providers with sovereignty posture: SecNumCloud-qualified 3DS Outscale (FR), Open Telekom Cloud + STACKIT (DE), Aruba Cloud (IT), Safespring (SE, verified 100% Swedish), Nubo (BE cooperative, verified), Aiven (FI), Hostinger + Cherry Servers (LT), CloudFerro/Oktawave (PL), Elastx/Cleura/Binero/Glesys (SE), Fuga/Leafcloud/Greenhost/TransIP (NL, Leafcloud verified), CloudSigma/Hostpoint/KeyCDN (CH), Naver Cloud (KR, verified), Sakura (JP), Sify (IN), Alibaba Cloud (CN), Core42 (AE/G42, verified). New **/submit** page: backend-free listing submission — form builds a pre-filled GitHub issue (labeled `new-listing`) + copy-as-markdown fallback; required-field validation; linked from nav, footer, and a homepage CTA band. Editorial review note: inclusion free, never for sale.
- **Evidence:** Cory: "keep adding more - look at commercial cloud service providers... Also, please add a way for people to submit net-new items."
- **Date:** 2026-10-19

## 2026-10-19 — Batch D: researched AI sovereign listings
- **Decision:** +71 listings (286 total; 519 pages: 163 alternatives, 36 jurisdictions). Researched via Firecrawl (awesome-european-ai list, Reuters, Wikipedia): EU AI labs (Poolside, Black Forest Labs, Domyn, H, Kyutai, Almawave, Tilde, NXAI, Noxtua, Legora, Photoroom), EU AI clouds (Nscale, Nebius, Northern Data, Berget AI, Regolo, Verda, VSHN), EU AI chips (SiPearl, Axelera AI, Innatera, SEMRON, SpiNNcloud, Fractile, VSORA, Kalray, GreenWaves), open-source AI tooling (Qdrant DE, Weaviate NL BSD-3 verified, Jina AI, Mixedbread, deepset, Rasa, Langfuse, Giskard, LangWatch, ZenML, Flower, Meilisearch, Argilla, Docling), plus KR chips (FuriosaAI, Rebellions), IL (Hailo, D-ID), CN models (DeepSeek, Qwen), IN (Khoj). **Correction:** Aleph Alpha listing updated — signed definitive merger agreement with Cohere Sept 2026 (Reuters), combined co. operates as Cohere, dual HQ Toronto/Berlin; added Cohere listing (CA).
- **Evidence:** Cory: "keep going and use firecrawl if need be or your internal browser to find more AI sovereign offerings."
- **Date:** 2026-10-19

## 2026-10-19 — Batch C + Insights editorial section
- **Decision:** +92 listings (215 total, 20 categories incl. new AI tools: Ollama, Mistral AI, Aleph Alpha...). New **Insights** section: 6 long-form thought pieces on fullstack sovereign tech (the sovereign stack thesis, jurisdiction buyer's guide, 10-person starter kit, why we list US vendors, self-host vs managed framework, true cost of free) with Article JSON-LD, index page, nav link, and llms.txt section. Programmatic engine now yields 110 alternatives + 33 jurisdiction pages; 392 pages total.
- **Evidence:** Cory: "add some more and then some broader thought pieces on fullstack sovereign tech."
- **Date:** 2026-10-19

## 2026-10-19 — Big content batch: 123 listings, 19 categories
- **Decision:** Added 85 listings via reproducible generator scripts (scripts/gen-batch-a.py, gen-batch-b.py) + 10 new categories (password managers, photo management, social, maps, developer tools, identity/auth, business apps, design, monitoring, publishing). Hardware grew 6 → 13. Fixed Element miscategorized under office-productivity → communication. Added residencyLabel() helper so tables render "Physical product" / "App" / "Global" instead of wrong "Self-hosted" fallbacks.
- **Evidence:** Cory: "add a shit ton more sovereign tech, include hardware." 244 pages build clean.
- **Date:** 2026-10-19

## 2026-10-19 — Programmatic SEO/AEO engine + slot scarcity
- **Decision:** Replicate OpenAlternative's playbook (verified: every SaaS product gets an "alternatives to X" page generated from listing data; long tail of generated pages; 1,700-line llms.txt; year-stamped comparison blog; freshness via GitHub API). Built: /alternatives/[product] (26 pages, e.g. "Sovereign alternatives to Gmail") and /jurisdictions/[country] (12 pages, our differentiator) with comparison tables, cards, FAQPage + ItemList JSON-LD on every page; llms.txt now lists alternatives + jurisdictions; 28 new listings (38 total, 9 categories incl. hardware/search/chat). Scarcity: slot caps in src/data/slots.ts (3 homepage spotlight, 1 banner/category, 8 strip) with live "X of Y left" inventory on /advertise and "your product here" placeholders on empty category pages.
- **Evidence:** Piotr Kulpiński's programmatic-SEO guide (dirstarter.com); OA llms.txt/robots.txt read directly. Pages are data-driven (unique domicile/license/residency data per page) to stay clear of scaled-content-abuse policy.
- **Date:** 2026-10-19

## 2026-10-19 — Doubled ad rates + commitment discounts
- **Decision:** Monthly rates doubled vs the OpenAlternative-anchored draft: Silver $298 / Gold $598 / Platinum $1,198. Commitment ladder: 5% off quarterly, 15% off semi-annual, 35% off annual (annual effective $194/$389/$779 — near standard directory rates; monthly is the flexibility premium).
- **Evidence:** Cory's call ("double them"). Unit economics (see MEMORY.md): ~11 sponsors ≈ OpenAlternative's $6.5K/mo at half the logo count; ~1.5 gross adds/month sustains 12 sponsors at 8% churn.
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
