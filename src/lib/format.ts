const COUNTRIES: Record<string, string> = {
  AT: "Austria",
  AU: "Australia",
  BE: "Belgium",
  BR: "Brazil",
  CA: "Canada",
  CH: "Switzerland",
  DE: "Germany",
  EE: "Estonia",
  FI: "Finland",
  FR: "France",
  GB: "United Kingdom",
  IN: "India",
  NL: "Netherlands",
  NZ: "New Zealand",
  PL: "Poland",
  SE: "Sweden",
  SG: "Singapore",
  US: "United States",
};

export function countryName(code: string): string {
  return COUNTRIES[code.toUpperCase()] ?? code.toUpperCase();
}

export function slugify(s: string): string {
  return s
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/(^-|-$)/g, "");
}

/** EU member states (ISO alpha-2), for jurisdiction FAQs. */
export const EU_COUNTRIES = new Set([
  "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "GR",
  "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK",
  "SI", "ES", "SE",
]);

interface ResidencyInput {
  dataResidency: string[];
  selfHost: boolean;
  managed: boolean;
  categories: string[];
}

/** Human label for where a product's data lives. */
export function residencyLabel(d: ResidencyInput): string {
  if (d.dataResidency.length > 0) return d.dataResidency.map(countryName).join(", ");
  if (d.selfHost && !d.managed) return "Self-hosted";
  if (d.managed) return "Global";
  if (d.categories.includes("hardware")) return "Physical product";
  return "App";
}
