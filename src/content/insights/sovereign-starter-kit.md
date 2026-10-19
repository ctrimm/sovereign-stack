---
title: "The 2026 sovereign starter kit: a complete stack for a 10-person team"
description: "A concrete, fullstack setup — hardware to apps — for a small team that wants to own its infrastructure. All from the directory."
date: 2026-10-19
image: /insights/sovereign-starter-kit.jpg
tags: ["guide", "fullstack", "starter-kit"]
---

Theory is cheap. Here's a complete, working stack for a 10-person company that wants meaningful sovereignty without hiring an infrastructure team. Every pick is cataloged in this directory; total effort is roughly a long weekend.

## Hardware: Framework laptops

Start where your people type. **Framework** laptops (US, upgradeable, repairable) running Linux, or **TUXEDO** (Germany) if you want Linux pre-installed and tuned. The point isn't the brand — it's escaping the closed hardware-software bundle where the OS vendor is also your identity provider, app store, and backup service.

## Cloud: Hetzner

One **Hetzner** (Germany) account. A handful of VPS instances in Nuremberg or Falkenstein run everything below for tens of euros a month. German domicile, German datacenters, no hyperscaler contract. If you outgrow VPS, their dedicated servers are the next step before you ever need AWS.

## Identity and access: ZITADEL or Keycloak

Before any app, set up identity. **ZITADEL** (Switzerland, open source) gives you SSO, MFA, and passkeys you control. This is the single highest-leverage move on this list: one identity system means one place to offboard people and one audit trail.

## Communication: Element + Jitsi

**Element** (UK) on the Matrix protocol for chat — federated, self-hostable, with managed hosting if you don't want the ops burden. **Jitsi** (open source) for video calls on your own Hetzner box. You now own both your chat history and your meeting metadata.

## Email: Tuta or mailbox.org

**Tuta** (Germany, open source clients, encrypted) or **mailbox.org** (Germany, full groupware). Either way: German domicile, no ad-tech business model, your domain on their infrastructure or bridged to your own.

## Files and office: Nextcloud + Collabora

**Nextcloud** (Germany) on your Hetzner server for files, calendar, and contacts. Add **Collabora Online** (UK) for document editing in the browser. This combination replaces Google Workspace's core for most teams, and the data never leaves your server.

## Analytics: Plausible

**Plausible** (Estonia) — cookie-free, EU-hosted analytics. Ten minutes to install, no consent banner required, and you stop feeding your visitor data to an ad-tech company as a side effect of counting pageviews.

## Passwords: Bitwarden

**Bitwarden** (open source) with the vault on your own server or their EU hosting. Every team member gets a password manager on day one; shared collections replace the spreadsheet of credentials.

## VPN: NetBird or Mullvad

**NetBird** (Germany, open source, self-hostable) for zero-trust access to your servers, or **Mullvad** (Sweden) for general browsing privacy. Different tools, different jobs — run both.

## What this costs

Roughly: €100–200/month in Hetzner bills, plus per-seat SaaS fees where you chose managed over self-hosted. Compare that against Google Workspace + Slack + 1Password + the rest, and the sovereign stack is usually *cheaper* — the price was never the barrier. The barrier was knowing the options exist in one place.

That's what the directory is for. Start with identity, then communication, then the rest. Own your layers.
