/**
 * Sponsorship slot inventory. Caps are deliberate: scarcity is the product.
 * When a slot type is full, new sponsors wait until a contract ends.
 */
export const SLOT_CAPS = {
  /** Homepage "Sponsored spotlight" cards */
  homepageSpotlight: 3,
  /** Homepage "Powering the stack" logo strip */
  sponsorStrip: 8,
  /** Category page banner — exclusive, one per category */
  categoryBannerPerCategory: 1,
  /** Listing page sidebar slot — max per listing page */
  listingSidebarPerPage: 2,
} as const;

export interface SlotInventory {
  spotlight: { cap: number; claimed: number; remaining: number };
  strip: { cap: number; claimed: number; remaining: number };
  banners: { cap: number; claimed: number; remaining: number; perCategory: number };
}

interface SponsorLike {
  data: { sponsored?: boolean; categories: string[] };
}

/** Derive claimed slots from the live listing collection. */
export function slotInventory(
  listings: SponsorLike[],
  categoryCount: number
): SlotInventory {
  const sponsored = listings.filter((l) => l.data.sponsored);
  const categoriesWithSponsor = new Set<string>();
  for (const l of sponsored) {
    for (const c of l.data.categories) categoriesWithSponsor.add(c);
  }
  const remaining = (cap: number, claimed: number) => Math.max(0, cap - claimed);
  return {
    spotlight: {
      cap: SLOT_CAPS.homepageSpotlight,
      claimed: sponsored.length,
      remaining: remaining(SLOT_CAPS.homepageSpotlight, sponsored.length),
    },
    strip: {
      cap: SLOT_CAPS.sponsorStrip,
      claimed: sponsored.length,
      remaining: remaining(SLOT_CAPS.sponsorStrip, sponsored.length),
    },
    banners: {
      cap: categoryCount * SLOT_CAPS.categoryBannerPerCategory,
      claimed: categoriesWithSponsor.size,
      remaining: remaining(categoryCount, categoriesWithSponsor.size),
      perCategory: SLOT_CAPS.categoryBannerPerCategory,
    },
  };
}
