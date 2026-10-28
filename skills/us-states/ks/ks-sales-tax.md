---
name: ks-sales-tax
description: Use this skill whenever asked about Kansas sales and use tax. Trigger on phrases like "Kansas sales tax", "KS sales tax", "KDOR", "K.S.A. §79-3603", "Kansas grocery tax". ALWAYS load us-sales-tax first.
version: 2.1
jurisdiction: US-KS
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# KS Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Kansas |
| State rate | 6.50% |
| Grocery food state rate | 0.00% (K.S.A. 79-3603d: 4% in 2023, 2% in 2024, 0% from Jan 1, 2025 onward) |
| Maximum combined rate | ~11.50% (state 6.5% + local/state credit; verify per Kansas Department of Revenue rate-change page) |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 in gross receipts |
| Filing | Form ST-1 (combined state/local); ST-10 (exempt purchases); e-file via Kansas Revenue Portal |
| Late penalty | 1%/month up to 24% (K.S.A. 79-3615); interest at IRC §6621 underpayment rate (K.S.A. 79-2968) |
| Tax authority | Kansas Department of Revenue (KDOR) |
| Portal | https://www.ksrevenue.gov |
| SST member | Yes -- Full Member |
| Skill version | 2.1 |

**Sources (archived, hashed):** K.S.A. 79-3603 (6.5% state rate), 79-3603d (food rate phase-down to 0%), 79-3615 (penalties), 79-2968 (interest = IRC §6621), KDOR sales-tax pages and ST-1/ST-10 forms.

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6.50% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | 0% state (K.S.A. 79-3603d, 0% from Jan 1, 2025) | Local rates still apply; phase-down was 6.5% → 4% (2023) → 2% (2024) → 0% (2025) |
| Prepared food | TAXABLE 6.50% | Restaurants, catered events, heated food (K.S.A. 79-3603(d)) |
| SaaS | NOT TAXABLE | Kansas has not clearly taxed SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Prohibition - grocery food state tax** — NEVER apply state tax to grocery food as of 2025 -- state rate is 0%. Local still applies.  _(Section 10 -- Prohibitions)_
- **Prohibition - phase-down history** — NEVER forget the phase-down history of grocery food taxation.  _(Section 10 -- Prohibitions)_
- **Prohibition - computation** — NEVER compute any number.  _(Section 10 -- Prohibitions)_

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Sources

| Source | URL | Read on |
|---|---|---|
| K.S.A. 79-3603 (state rate 6.5%) | https://ksrevisor.gov/statutes/chapters/ch79/079_036_0003.html | 2026-10-28 |
| K.S.A. 79-3603d (food and food ingredients: 4% from 2023, 2% from 2024, 0% from Jan 1, 2025; prepared food carve-out) | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_036_0000_article/079_036_0003d_section/079_036_0003d_k/ | 2026-10-28 |
| K.S.A. 79-3606 (exemptions, incl. prescription drugs and integrated-production machinery and equipment) | https://ksrevisor.gov/statutes/chapters/ch79/079_036_0006.html | 2026-10-28 |
| K.S.A. 79-3615 (1% a month, up to 24%, plus interest) | https://ksrevisor.gov/statutes/chapters/ch79/079_036_0015.html | 2026-10-28 |
| K.S.A. 79-2968 (interest by reference to IRC §6621 underpayment rate) | https://ksrevisor.gov/statutes/chapters/ch79/079_029_0068.html | 2026-10-28 |
| KDOR Sales (Retailers) tax page (6.5% state rate since July 1, 2015, plus local taxes) | https://www.ksrevenue.gov/bustaxtypessales.html | 2026-10-28 |
| KDOR sales tax rate changes | https://www.ksrevenue.gov/salesratechanges.html | 2026-10-28 |

Not yet confirmed: the ~11.50% maximum combined state and local rate; destination-based sourcing and Kansas's status as a full Streamlined Sales Tax member; the $100,000 gross-receipts economic-nexus threshold (statute not archived); the ST-1 and ST-10 form IDs and the Kansas Revenue Portal e-filing route (the KDOR form URLs tried returned 404 pages); the citation "K.S.A. 79-3603(d)" for prepared food (the archived prepared-food rule is K.S.A. 79-3603d(b)); the exact interest computation under K.S.A. 79-2968 (the statute ties it to the IRC §6621 underpayment rate as in effect on 1 September 1996, with adjustments not checked here); the taxability of clothing, SaaS, canned software, professional services and sales for resale as listed in the transaction pattern library.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
