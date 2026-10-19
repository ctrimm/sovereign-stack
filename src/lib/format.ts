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
