import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const categories = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/categories" }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    // Short label used in filters, e.g. "Email".
    shortLabel: z.string().optional(),
  }),
});

const listings = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./src/content/listings" }),
  schema: z.object({
    title: z.string(),
    tagline: z.string(),
    website: z.string().url(),
    // Big-tech / incumbent products this replaces, e.g. ["Gmail", "Outlook"].
    replaces: z.array(z.string()).default([]),
    // Slugs matching files in src/content/categories.
    categories: z.array(z.string()).min(1),
    license: z.string().describe("SPDX id or 'Proprietary'"),
    openSource: z.boolean().default(false),
    pricing: z.enum(["Free", "Freemium", "Paid", "Usage-based"]),
    company: z.object({
      name: z.string(),
      // ISO 3166-1 alpha-2 country code of legal domicile, e.g. "DE".
      domicile: z.string().length(2),
      founded: z.number().int().optional(),
    }),
    // ISO country codes where customer data can reside.
    dataResidency: z.array(z.string().length(2)).default([]),
    selfHost: z.boolean().default(false),
    managed: z.boolean().default(true),
    // One-line GDPR / legal posture, e.g. "GDPR-native, EU-owned".
    gdpr: z.string(),
    featured: z.boolean().default(false),
    // Paid placement. Sponsored listings render with a labeled "Sponsored"
    // sticker, a disclosure, and rel="sponsored" on outbound links.
    // Rankings are editorial; sponsorship buys visibility only.
    sponsored: z.boolean().default(false),
    // Editorial maturity signal.
    maturity: z.enum(["Beta", "Production", "Established"]).default("Production"),
  }),
});

export const collections = { categories, listings };
