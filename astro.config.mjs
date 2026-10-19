// @ts-check
import { defineConfig } from "astro/config";
import sitemap from "@astrojs/sitemap";
import tailwindcss from "@tailwindcss/vite";

// Update `site` once the domain is chosen.
export default defineConfig({
  site: "https://sovereignstack.co",
  integrations: [sitemap()],
  vite: {
    plugins: [tailwindcss()],
  },
});
