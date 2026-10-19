---
title: "Your phone is the weakest layer"
description: "You can self-host everything and still lose at the device in your pocket. The mobile sovereignty stack: OS, hardware, and what deGoogling can't fix."
date: 2026-10-19
image: /insights/phone-weakest-layer.jpg
tags: ["mobile", "fullstack", "guide"]
---

You did everything right. Email on a German provider, files on your own Nextcloud, chat on Matrix, VPN always on. Then you checked it all from a phone that reports your location to two American companies before breakfast.

Mobile is the layer where sovereignty goes to die — not because the options don't exist, but because the phone is the most consolidated, most closed, and most intimate computer you own. Here's the stack, bottom to top.

## The duopoly problem

Two operating systems run virtually every phone on earth, and both are controlled by American companies whose business models depend on the data flowing through them. Below the OS sits the baseband processor — the chip that talks to cell towers — running proprietary firmware with direct memory access that no OS, however open, can fully audit. Above the OS sit the app stores: the chokepoint through which every application, update, and payment must pass.

This is why the phone is the weakest layer. Your server can be in Frankfurt under German law; your traffic still transits a device whose lowest levels answer to someone else.

## The OS layer: deGoogling works, up to a point

**/e/OS** (France, from the e Foundation) strips Google services from Android and replaces them with privacy-respecting defaults — the most complete deGoogled experience, preinstalled on **Murena** phones. **CalyxOS** (US, from the Calyx Institute nonprofit) takes a similar path with a security-first hardening approach. **Sailfish OS** (Finland, from Jolla) is the true independent: not Android at all, but its own OS — the only real third option, kept alive for over a decade against impossible odds.

What deGoogling actually removes: Google's services, tracking, and cloud dependencies. What it can't remove: the baseband firmware, proprietary driver blobs, and the app-ecosystem gravity that pulls most people back to the Play Store. An honest accounting.

## The hardware layer: four theories of the phone

The directory now lists four distinct answers to "what should a sovereign phone be":

1. **The repairable phone** — **Fairphone** (Netherlands): open it, fix it, keep it for a decade. Sovereignty as longevity and ownership.
2. **The deGoogled phone** — **Murena** (France), **Volla** (Germany): mainstream hardware, private OS preinstalled. Sovereignty as convenience.
3. **The minimal phone** — **Punkt** (Switzerland), **Light Phone** (US): calls, texts, almost nothing else. Sovereignty as absence — a device that can't leak what it never collects.
4. **The open phone** — **MNT Reform** and its Pocket sibling: open hardware down to the schematics. Sovereignty as auditability.

Each is a real product you can buy today. None is perfect; together they cover every threat model from "I want a normal phone without Google" to "I want to read the schematics."

## The pragmatic stack

Most people won't carry a minimal phone, and that's fine. Sovereignty here is a spectrum, not a purity test:

- **Maximum:** minimal phone (Punkt/Light) + no smartphone at all for the truly committed.
- **Strong:** Fairphone or Murena with /e/OS — a real smartphone minus Google.
- **Good enough:** standard phone, disciplined: audited apps, VPN, no Google/Facebook apps, encrypted messaging.

The residual risks — baseband, blobs, carriers — don't disappear at any level. But "the phone reports everything to everyone" and "the phone reports metadata to the carrier" are very different situations, and the distance between them is purchasable today.

Your stack is only as sovereign as its weakest layer. For most people, that's the rectangle in their pocket. Fix it first — or at least know exactly what you're accepting.
