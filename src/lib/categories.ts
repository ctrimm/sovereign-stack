import { countryName } from "./format";

/** Accent dot color per category (Tailwind class). */
export const CATEGORY_DOT: Record<string, string> = {
  "cloud-hosting": "bg-sky",
  email: "bg-coral",
  "file-storage": "bg-lime",
  "networking-vpn": "bg-violet",
  "office-productivity": "bg-amber",
  "web-analytics": "bg-pink",
};

export function categoryDot(id: string): string {
  return CATEGORY_DOT[id] ?? "bg-ink-faint";
}

/** Sticker flag label for a listing card. Sponsored always wins. */
export function cardFlag(data: {
  sponsored: boolean;
  openSource: boolean;
  selfHost: boolean;
  company: { domicile: string };
}): string {
  if (data.sponsored) return "Sponsored";
  if (data.openSource) return "Open source";
  if (data.selfHost) return "Self-hostable";
  return `${countryName(data.company.domicile)}-hosted`;
}
