#!/usr/bin/env python3
"""Generate listing markdown files for batch F:
sovereign email depth, EU AI Act tooling, new os-firmware category.
Researched 2026-10-19 via Firecrawl (Saidot, 2021.AI, Modulos, Holistic AI,
NixOS Foundation, Zorin, 9elements, Soverin verified).
Usage: python3 gen-batch-f.py  (run from ~/workspace/sovereign-stack)
Idempotent: overwrites the files it owns.
"""
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "content", "listings")

def q(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'

def arr(items):
    return "[" + ", ".join(q(i) for i in items) + "]"

# slug, title, tagline, website, categories, replaces, license, openSource,
# pricing, co_name, co_dom, co_founded, residency, selfHost, managed, gdpr, maturity, body
LISTINGS = [
    # ---- sovereign email depth ----
    ("fastmail", "Fastmail", "Independent email from Australia.", "https://www.fastmail.com",
     ["email"], ["Gmail", "Outlook"], "Proprietary", False, "Paid",
     "Fastmail Pty Ltd", "AU", 1999, ["AU"], False, True,
     "Australian domicile.", "Established",
     "Fastmail is an Australian independent email provider with a loyal following and no ads."),
    ("hushmail", "Hushmail", "Encrypted email from Canada.", "https://www.hushmail.com",
     ["email"], ["Proton Mail"], "Proprietary", False, "Paid",
     "Hush Communications Ltd", "CA", 1999, ["CA"], False, True,
     "Canadian domicile.", "Established",
     "Hushmail is a Canadian encrypted email service operating since 1999."),
    ("web-de", "WEB.DE", "Germany's freemail giant.", "https://web.de",
     ["email"], ["Gmail"], "Proprietary", False, "Freemium",
     "1&1 Mail & Media GmbH", "DE", 1999, ["DE"], False, True,
     "German domicile.", "Established",
     "WEB.DE (with GMX) is Germany's largest email provider — freemail under German law."),
    ("freenet-mail", "freenet", "Email and hosting from Germany.", "https://www.freenet.de",
     ["email"], ["Gmail"], "Proprietary", False, "Freemium",
     "freenet AG", "DE", 1999, ["DE"], False, True,
     "German domicile.", "Established",
     "freenet is a German digital lifestyle provider with email and cloud services."),
    ("mail-de", "mail.de", "Secure email from Germany.", "https://mail.de",
     ["email"], ["Gmail"], "Proprietary", False, "Freemium",
     "mail.de GmbH", "DE", 2009, ["DE"], False, True,
     "German domicile.", "Established",
     "mail.de is a German secure email provider with encrypted storage."),
    ("laposte-net", "Laposte.net", "Email from La Poste.", "https://www.laposte.net",
     ["email"], ["Gmail"], "Proprietary", False, "Free",
     "La Poste", "FR", 1999, ["FR"], False, True,
     "French domicile; state-owned.", "Established",
     "Laposte.net is the free email service of La Poste, the French postal service."),
    ("mailo", "Mailo", "French ethical email.", "https://www.mailo.com",
     ["email"], ["Gmail"], "Proprietary", False, "Freemium",
     "Mailo", "FR", 1998, ["FR"], False, True,
     "French domicile.", "Established",
     "Mailo (formerly Net-C) is a French independent email service with an ethical, ad-free stance."),
    ("soverin", "Soverin", "Private email from the Netherlands.", "https://soverin.net",
     ["email"], ["Gmail"], "Proprietary", False, "Paid",
     "Soverin", "NL", 2015, ["NL"], False, True,
     "Dutch domicile.", "Established",
     "Soverin is a Dutch private email provider — your domain, no tracking, for a few euros a month."),
    ("zoho-mail", "Zoho Mail", "Business email from India.", "https://www.zoho.com/mail",
     ["email"], ["Gmail", "Outlook"], "Proprietary", False, "Freemium",
     "Zoho Corporation", "IN", 1996, ["IN"], False, True,
     "Indian domicile.", "Established",
     "Zoho Mail is part of India's Zoho suite — business email from an independent Indian software company."),
    ("seznam-mail", "Seznam Email", "Czech email from Seznam.", "https://email.seznam.cz",
     ["email"], ["Gmail"], "Proprietary", False, "Free",
     "Seznam.cz a.s.", "CZ", 1996, ["CZ"], False, True,
     "Czech domicile.", "Established",
     "Seznam is the Czech internet portal with its own email service used across the country."),
    ("ukr-net", "Ukr.net", "Ukrainian email and portal.", "https://www.ukr.net",
     ["email"], ["Gmail"], "Proprietary", False, "Free",
     "Ukr.net", "UA", 1998, ["UA"], False, True,
     "Ukrainian domicile.", "Established",
     "Ukr.net is Ukraine's major internet portal with free email for millions of users."),
    ("1984-mail", "1984", "Icelandic hosting and email.", "https://1984.is",
     ["email"], ["Proton Mail"], "Proprietary", False, "Paid",
     "1984 ehf", "IS", 2006, ["IS"], False, True,
     "Icelandic domicile; strong privacy laws.", "Established",
     "1984 is an Icelandic hosting and email provider operating under Iceland's strong privacy protections."),
    ("cyon", "Cyon", "Swiss hosting with email.", "https://www.cyon.ch",
     ["email", "cloud-hosting"], ["Infomaniak"], "Proprietary", False, "Paid",
     "Cyon GmbH", "CH", 2001, ["CH"], False, True,
     "Swiss domicile.", "Established",
     "Cyon is a Swiss hoster with email and web hosting in Swiss datacenters."),
    # ---- EU AI Act compliance tooling ----
    ("latticeflow", "LatticeFlow AI", "AI governance from Switzerland.", "https://latticeflow.ai",
     ["ai-tools"], ["Credo AI"], "Proprietary", False, "Paid",
     "LatticeFlow AI", "CH", 2021, ["CH"], False, True,
     "Swiss domicile; EU AI Act evaluation.", "Beta",
     "LatticeFlow AI is a Swiss AI governance platform for EU AI Act evaluation, from the creators of COMPL-AI."),
    ("saidot", "Saidot", "AI governance from Finland.", "https://www.saidot.ai",
     ["ai-tools"], ["Credo AI"], "Proprietary", False, "Paid",
     "Saidot", "FI", 2018, ["FI"], False, True,
     "Finnish domicile.", "Beta",
     "Saidot is a Finnish AI governance platform for managing AI systems, models, and agents."),
    ("2021-ai", "2021.AI", "AI governance from Denmark.", "https://2021.ai",
     ["ai-tools"], ["Credo AI"], "Proprietary", False, "Paid",
     "2021.AI", "DK", 2016, ["DK"], False, True,
     "Danish domicile; GRACE platform.", "Established",
     "2021.AI is a Danish AI company whose GRACE platform governs enterprise AI deployments."),
    ("modulos", "Modulos", "AI governance from Switzerland.", "https://www.modulos.ai",
     ["ai-tools"], ["Credo AI"], "Proprietary", False, "Paid",
     "Modulos AG", "CH", 2018, ["CH"], False, True,
     "Swiss domicile; ISO 42001-certified.", "Beta",
     "Modulos is a Swiss AI governance platform — ISO 42001-certified, covering the EU AI Act."),
    ("holistic-ai", "Holistic AI", "AI auditing from London.", "https://www.holisticai.com",
     ["ai-tools"], ["Credo AI"], "Proprietary", False, "Paid",
     "Holistic AI", "GB", 2020, ["GB"], False, True,
     "UK domicile.", "Beta",
     "Holistic AI is a London AI auditing company assessing AI systems against regulations including the EU AI Act."),
    ("credo-ai", "Credo AI", "AI governance from San Francisco.", "https://www.credo.ai",
     ["ai-tools"], ["Holistic AI"], "Proprietary", False, "Paid",
     "Credo AI Inc", "US", 2020, ["US"], False, True,
     "US domicile.", "Established",
     "Credo AI is a US AI governance platform for compliance and risk management."),
    # ---- os & firmware ----
    ("e-os", "/e/OS", "DeGoogled Android from France.", "https://e.foundation",
     ["os-firmware"], ["Android"], "Apache-2.0", True, "Free",
     "e Foundation", "FR", 2018, [], True, False,
     "French nonprofit.", "Beta",
     "/e/OS is a French deGoogled Android operating system from the e Foundation — privacy by default on your phone."),
    ("calyxos", "CalyxOS", "Private Android from the US.", "https://calyxos.org",
     ["os-firmware"], ["Android"], "Apache-2.0", True, "Free",
     "The Calyx Institute", "US", 2020, [], True, False,
     "US nonprofit.", "Beta",
     "CalyxOS is a US nonprofit Android distribution focused on privacy and security."),
    ("sailfish", "Sailfish OS", "Independent mobile OS from Finland.", "https://sailfishos.org",
     ["os-firmware"], ["Android", "iOS"], "Proprietary", False, "Paid",
     "Jolla Oy", "FI", 2011, [], False, False,
     "Finnish domicile.", "Established",
     "Sailfish OS is a Finnish independent mobile operating system from Jolla — the alternative to the Android/iOS duopoly."),
    ("ubuntu", "Ubuntu", "Linux from the UK.", "https://ubuntu.com",
     ["os-firmware"], ["Windows", "macOS"], "GPL-3.0", True, "Free",
     "Canonical Ltd", "GB", 2004, [], True, True,
     "UK domicile.", "Established",
     "Ubuntu is the UK's Canonical-built Linux distribution — the world's most popular desktop Linux."),
    ("nixos", "NixOS", "Reproducible Linux from the Netherlands.", "https://nixos.org",
     ["os-firmware"], ["Ubuntu"], "MIT", True, "Free",
     "NixOS Foundation", "NL", 2003, [], True, False,
     "Dutch foundation (stichting).", "Beta",
     "NixOS is a Linux distribution built on the purely functional Nix package manager, stewarded by the Dutch NixOS Foundation."),
    ("qubes-os", "Qubes OS", "Security by compartmentalization.", "https://www.qubes-os.org",
     ["os-firmware"], ["Windows"], "GPL-2.0", True, "Free",
     "Invisible Things Lab", "PL", 2012, [], True, False,
     "Polish company.", "Beta",
     "Qubes OS is a security-focused operating system from Poland's Invisible Things Lab — every app in its own isolated qube."),
    ("dasharo", "Dasharo", "Open-source firmware from Poland.", "https://dasharo.com",
     ["os-firmware"], [], "GPL-3.0", True, "Paid",
     "3mdeb", "PL", 2016, [], False, False,
     "Polish domicile.", "Beta",
     "Dasharo is open-source coreboot-based firmware from Poland's 3mdeb — auditable boot for modern PCs."),
    ("9elements", "9elements", "Open-source firmware from Germany.", "https://9elements.com",
     ["os-firmware"], [], "GPL-3.0", True, "Paid",
     "9elements GmbH", "DE", 2011, [], False, True,
     "German domicile.", "Established",
     "9elements is a German firmware company building production-ready open-source firmware for servers and devices."),
    ("pop-os", "Pop!_OS", "Linux from System76.", "https://pop.system76.com",
     ["os-firmware"], ["Ubuntu", "Windows"], "GPL-3.0", True, "Free",
     "System76", "US", 2017, [], True, False,
     "US domicile.", "Established",
     "Pop!_OS is System76's Ubuntu-based Linux distribution, tuned for developers and makers."),
    ("zorin-os", "Zorin OS", "Linux from Ireland.", "https://zorinos.com",
     ["os-firmware"], ["Windows", "macOS"], "GPL-3.0", True, "Freemium",
     "Zorin Group", "IE", 2008, [], True, False,
     "Irish domicile.", "Established",
     "Zorin OS is an Irish Linux distribution designed to ease Windows users into open source."),
    ("elementary-os", "elementary OS", "Design-first Linux from the US.", "https://elementary.io",
     ["os-firmware"], ["macOS"], "GPL-3.0", True, "Freemium",
     "elementary Inc", "US", 2011, [], True, False,
     "US domicile.", "Established",
     "elementary OS is a US design-focused Linux distribution with a pay-what-you-want model."),
    ("kde", "KDE", "The desktop from Germany.", "https://kde.org",
     ["os-firmware"], ["Windows", "macOS"], "GPL-2.0", True, "Free",
     "KDE e.V.", "DE", 1996, [], True, False,
     "German nonprofit.", "Established",
     "KDE is the German nonprofit community behind the Plasma desktop — one of Linux's two great desktop environments."),
    ("gnome", "GNOME", "The desktop from the US.", "https://www.gnome.org",
     ["os-firmware"], ["Windows", "macOS"], "GPL-2.0", True, "Free",
     "GNOME Foundation", "US", 2000, [], True, False,
     "US nonprofit.", "Established",
     "GNOME is the US nonprofit foundation behind the GNOME desktop — the default face of many Linux distributions."),
]


def render(entry):
    (slug, title, tagline, website, categories, replaces, license, openSource,
     pricing, co_name, co_dom, co_founded, residency, selfHost, managed,
     gdpr, maturity, body) = entry
    lines = [
        "---",
        f"title: {q(title)}",
        f"tagline: {q(tagline)}",
        f"website: {q(website)}",
        f"categories: {arr(categories)}",
        f"replaces: {arr(replaces)}",
        f"license: {q(license)}",
        f"openSource: {'true' if openSource else 'false'}",
        f"pricing: {q(pricing)}",
        "company:",
        f"  name: {q(co_name)}",
        f"  domicile: {q(co_dom)}",
    ]
    if co_founded:
        lines.append(f"  founded: {co_founded}")
    lines += [
        f"dataResidency: {arr(residency)}",
        f"selfHost: {'true' if selfHost else 'false'}",
        f"managed: {'true' if managed else 'false'}",
        f"gdpr: {q(gdpr)}",
        f"maturity: {q(maturity)}",
        "---",
        "",
        body,
        "",
    ]
    return "\n".join(lines)


def main():
    os.makedirs(OUT, exist_ok=True)
    for entry in LISTINGS:
        path = os.path.join(OUT, entry[0] + ".md")
        with open(path, "w") as f:
            f.write(render(entry))
    print(f"wrote {len(LISTINGS)} listings to {OUT}")


if __name__ == "__main__":
    main()
