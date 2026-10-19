import type { APIRoute } from "astro";
import { getCollection } from "astro:content";

export const GET: APIRoute = async () => {
  const listings = await getCollection("listings");
  const payload = listings.map((l) => ({
    slug: l.id,
    url: `https://sovereignstack.co/listings/${l.id}/`,
    ...l.data,
  }));
  return new Response(JSON.stringify(payload, null, 2), {
    headers: { "Content-Type": "application/json; charset=utf-8" },
  });
};
