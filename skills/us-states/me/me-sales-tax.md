---
name: me-sales-tax
description: Use this skill whenever asked about Maine sales and use tax. Trigger on phrases like "Maine sales tax", "ME sales tax", "MRS", "36 M.R.S. §1811". ALWAYS load us-sales-tax first.
version: "2.1"
jurisdiction: US-ME
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ME Sales Tax

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Maine |
| State rate | 5.50% (general); 8.00% (prepared food; also liquor in licensed establishments); 9.00% (lodging); 10.00% (short-term auto rental); 10% cannabis retail before 2026, 14% from Jan 1 2026 — all per [36 M.R.S. §1811, archived 2026-10-28](https://legislature.maine.gov/statutes/36/title36sec1811.html): "the rate of tax is 5.5% … except the rate of tax is: (1) Eight percent on the value of prepared food; … (3) Nine percent on the value of rental of living quarters …; (4) Ten percent on the value of rental for a period of less than one year of: (a) An automobile …; (5) Before January 1, 2026, 10% on the value of adult use cannabis … For sales occurring on or after January 1, 2026, the applicable rate of tax under this subparagraph is 14%" |
| Local taxes | None |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Maine Revenue Services (MRS) |
| Portal | https://www.maine.gov/revenue |
| SST member | No |
| Skill version | 2.0 |

## Section 3 -- Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 5.50% |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE 8.00% | Higher rate |
| Lodging | TAXABLE 9.00% | Higher rate |
| Short-term auto rental | TAXABLE 10.00% |  |
| SaaS | NOT TAXABLE | Maine does not tax SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Section 10 -- Prohibitions

- **Prohibition on using 5.50% for prepared food or lodging** — NEVER use the 5.50% rate for prepared food or lodging -- they have higher rates (9%).  _(Section 10 -- Prohibitions)_
- **Prohibition on forgetting short-term auto rental rate** — NEVER forget the 8% short-term auto rental rate.  _(Section 10 -- Prohibitions)_
- **Prohibition on computing numbers** — NEVER compute any number.  _(Section 10 -- Prohibitions)_

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
