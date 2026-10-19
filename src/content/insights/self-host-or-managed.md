---
title: "Self-host or managed? A decision framework"
description: "The most common question in sovereign tech, answered with a flowchart instead of ideology."
date: 2026-10-19
tags: ["guide", "self-hosting"]
---

Every sovereign tech conversation eventually reaches the same fork: run it yourself, or pay someone in your jurisdiction to run it for you? The self-hosting community treats this as a moral question. It isn't. It's an engineering tradeoff with a correct answer that depends on three variables.

## Variable 1: What's the blast radius?

If the service goes down or gets breached, what happens? Email and identity have enormous blast radii — losing them halts the company. A personal notes app does not. **The bigger the blast radius, the more you should bias toward managed** — unless you genuinely have the operational capacity, because a badly-run self-hosted service is less sovereign than a well-run managed one. Sovereignty that doesn't survive contact with a 3 AM outage is theater.

## Variable 2: Can the vendor read your data?

This is the variable that collapses the whole debate. If the service is end-to-end encrypted (**Tuta**, **Bitwarden**, **CryptPad**) or the sensitive data never leaves your devices, the vendor's infrastructure matters far less — they have nothing to hand over and nothing to leak. Managed is nearly free sovereignty.

If the vendor *can* read your data — analytics, CRM, most groupware — then you're trusting their operations, their employees, and their jurisdiction. That's where self-hosting (**Nextcloud**, **Matomo**, **Mastodon**) or a managed provider in your own jurisdiction (**Hetzner**, **Infomaniak**) earns its keep.

## Variable 3: Do you have a pulse on the machine?

Self-hosting is a commitment to patching, monitoring, backups, and incident response — forever. Be brutally honest: will this still be patched in 18 months? If the answer is "probably not," choose managed from a vendor in your jurisdiction. An unpatched Nextcloud is a liability, not a sovereignty statement.

## The framework

1. **Can the vendor read the data?** No → managed is fine, pick by jurisdiction and price. Yes → continue.
2. **Is the blast radius large?** Yes → managed in your jurisdiction, or self-hosted only with real operational commitment.
3. **Will you actually maintain it?** No → managed in your jurisdiction. Yes → self-host and enjoy the control.

## The hybrid answer

Most mature setups land hybrid: self-host the crown jewels you can operate well (files, git, chat), buy managed for the blast-radius services (email, identity, DNS), and demand end-to-end encryption everywhere else. The directory marks every listing with self-host and managed options precisely so you can build that mix deliberately.

Ideology says self-host everything. Engineering says self-host what you can operate, buy the rest from vendors whose jurisdiction you've chosen. The second one survives contact with reality.
