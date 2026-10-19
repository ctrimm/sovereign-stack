import type { APIRoute } from "astro";
import { getCollection } from "astro:content";
import { countryName, slugify } from "../lib/format";

export const GET: APIRoute = async () => {
  const site = "https://sovereignstack.co";
  const categories = await getCollection("categories");
  const listings = await getCollection("listings");
  const insights = await getCollection("insights");

  const replacesMap = new Map<string, string[]>();
  for (const l of listings) {
    for (const r of l.data.replaces) {
      if (!replacesMap.has(r)) replacesMap.set(r, []);
      replacesMap.get(r)!.push(l.data.title);
    }
  }
  const jurisdictions = new Map<string, string[]>();
  for (const l of listings) {
    const code = l.data.company.domicile.toUpperCase();
    if (!jurisdictions.has(code)) jurisdictions.set(code, []);
    jurisdictions.get(code)!.push(l.data.title);
  }

  const lines = [
    "# Sovereign Stack",
    "",
    "> A curated directory of sovereign technology: open-source, self-hostable,",
    "> and independently-domiciled products from the EU, US, and rest of world,",
    "> organized by jurisdiction.",
    "",
    "## Stats",
    "",
    `- Aggregate directory statistics: ${site}/stats/`,
    "",
    "## Insights",
    "",
    ...insights.map((i) => `- [${i.data.title}](${site}/insights/${i.id}/): ${i.data.description}`),
    "",
    "## Categories",
    "",
    ...categories.map((c) => `- [${c.data.title}](${site}/categories/${c.id}/): ${c.data.description}`),
    "",
    "## Sovereign alternatives (by product replaced)",
    "",
    ...[...replacesMap.entries()].map(
      ([r, names]) =>
        `- [Sovereign alternatives to ${r}](${site}/alternatives/${slugify(r)}/): ${names.join(", ")}.`
    ),
    "",
    "## Jurisdictions (by company domicile)",
    "",
    ...[...jurisdictions.entries()].map(
      ([code, names]) =>
        `- [Sovereign tech from ${countryName(code)}](${site}/jurisdictions/${code.toLowerCase()}/): ${names.join(", ")}.`
    ),
    "",
    "## Listings",
    "",
    ...listings.map((l) => {
      const d = l.data;
      const bits = [
        d.tagline,
        `Domicile: ${countryName(d.company.domicile)}`,
        d.openSource ? `License: ${d.license}` : "Proprietary",
        d.selfHost ? "Self-hostable" : "Managed only",
        d.replaces.length > 0 ? `Replaces: ${d.replaces.join(", ")}` : null,
      ]
        .filter(Boolean)
        .join(". ");
      return `- [${d.title}](${site}/listings/${l.id}/): ${bits}.`;
    }),
    "",
    `Machine-readable feed: ${site}/api/listings.json`,
  ];

  return new Response(lines.join("\n"), {
    headers: { "Content-Type": "text/plain; charset=utf-8" },
  });
};
