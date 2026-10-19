# Sovereign Stack

A curated directory of sovereign technology: open-source, self-hostable, and
independently-domiciled products from the EU, US, and rest of world — organized
by jurisdiction, so buyers can choose whose laws govern their data.

## Stack

- [Astro 7](https://astro.build) — static-first, zero-JS pages by default
- [Tailwind CSS v4](https://tailwindcss.com) — styling
- [SST v3](https://sst.dev) (`sst.aws.Astro`) — deploy to AWS (S3 + CloudFront)
- Content Collections — listings and categories as Markdown with a typed schema

## Commands

```sh
npm install
npm run dev      # local dev server
npm run build    # production build to dist/
npm run preview  # preview the build
npx sst deploy   # deploy to AWS (stage defaults to personal stage)
npx sst remove   # tear down
```

Requires Node >= 22.12.

## Content model

- `src/content/categories/*.md` — category title + description
- `src/content/listings/*.md` — product frontmatter (see `src/content.config.ts`
  for the schema) plus an editorial body

Jurisdiction fields are first-class: `company.domicile` (ISO-3166 alpha-2),
`dataResidency[]`, `license`, `selfHost`, `managed`, `replaces[]`.

## AI-friendly by design

- Semantic HTML, skip link, labeled landmarks, focus-visible styles
- JSON-LD (`WebSite`, `ItemList`, `SoftwareApplication`) on every page
- `llms.txt` at `/llms.txt` and a JSON feed at `/api/listings.json`
- `robots.txt` + sitemap

## Email capture

`src/components/EmailCapture.astro` renders a signup form when
`PUBLIC_NEWSLETTER_ENDPOINT` is set, and a "coming soon" note otherwise. The
newsletter itself launches later — day one just collects addresses.
