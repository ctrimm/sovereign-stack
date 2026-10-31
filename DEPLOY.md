# Deploying Sovereign Stack (Cloudflare Pages)

The site is a fully static Astro build, so the cheapest production setup is:

| Piece | Service | Cost |
|---|---|---|
| Domain | sovereignstack.co (Cloudflare Registrar or Porkbun) | ~$16–30/yr |
| Hosting | Cloudflare Pages (free plan) | $0 |
| Email catchall | Cloudflare Email Routing | $0 |
| SSL | Cloudflare (automatic) | $0 |

Total running cost: the domain renewal. Pages free plan covers this site
easily: unlimited bandwidth/requests, 500 builds/month, 20,000 files/site,
100 custom domains. Our build is ~625 pages in ~15 seconds.

## One-time setup (in the Cloudflare dashboard)

1. **Register the domain** — `sovereignstack.co`
   - Cloudflare Registrar: $30/yr flat (register = renew, no markup games).
   - Or Porkbun: ~$16 first year, ~$31/yr renewals. Registrar choice doesn't
     matter for hosting; DNS is what Pages needs.
2. **Add the site to Cloudflare** (if registered elsewhere): Add site →
   enter the domain → Free plan → move nameservers to Cloudflare at your
   registrar.
3. **Create the Pages project**: Workers & Pages → Create → Pages →
   Connect to Git → pick `ctrimm/sovereign-stack`. Build settings:
   - Framework preset: **Astro**
   - Build command: `npm run build`
   - Build output directory: `dist`
   - Environment variable: `NODE_VERSION` = `22`
   
   Every push to `main` then deploys automatically. Preview URLs are
   generated for other branches.
4. **Attach the custom domain**: Pages project → Custom domains →
   `sovereignstack.co` (and `www.sovereignstack.co`). DNS records and the
   TLS certificate are created automatically when the domain is on
   Cloudflare.
5. **Email catchall**: Email → Email Routing → enable, add a catch-all rule
   forwarding `*@sovereignstack.co` to your inbox. This makes
   `admin@sovereignstack.co` (the /submit destination) real.

## Notes

- The site URL is already `https://sovereignstack.co` in `astro.config.mjs`,
  JSON-LD, `llms.txt`, and the submit flow — no code changes needed.
- `sst.config.ts` (AWS) is retained but unused on this path; Pages is the
  production target unless we outgrow the free plan.
- Sponsor video embeds and galleries are plain static assets; nothing in
  the paid feature set needs a backend.
