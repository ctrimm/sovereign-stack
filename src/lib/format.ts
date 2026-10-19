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
