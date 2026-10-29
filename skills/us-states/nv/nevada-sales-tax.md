---
name: nevada-sales-tax
description: Use this skill whenever asked about Nevada sales and use tax. Trigger on phrases like "Nevada sales tax", "NV sales tax", "NRS 372". ALWAYS load us-sales-tax first.
jurisdiction: US-NV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Nevada Sales Tax

## Who this applies to

Sellers with Nevada sales — state and local sales/use tax.

## Rates, bands and thresholds

| Field | Value |
| --- | --- |
| Jurisdiction | Nevada |
| State rate | 6.85%
| Local rate range | 0% -- ~1.525%
| Maximum combined rate | ~8.375%
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions
| Tax authority | Nevada Department of Taxation |
| Portal | https://tax.nv.gov |
| SST member | Yes -- Full Member |
| No state income tax | Correct |
| Skill version | 2.0 |

## The taxable base

### Transaction pattern library

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6.85% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE | Nevada has not enacted SaaS taxation |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Deadlines and filing

See the quick-reference due-date row above.

## Penalties and interest

Late filing/payment penalties and interest apply; current rates are not yet confirmed against an archived source.

## Cross-border points

- Destination sourcing; interstate sales require use-tax analysis on the buyer side.

## Worked examples

No worked examples yet — rate figures pending source confirmation.

## Ask the client first

- Nexus status (economic threshold) and SST registration.
- Whether receipts are services (not taxable in NV) or TPP/canned software.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Nevada Department of Taxation — homepage notice | https://tax.nv.gov/ | 2026-10-28 |

Not yet confirmed: state rate 6.85%; local range; max combined ~8.375%; economic nexus $100,000/200 transactions; penalty/interest rates.

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

### Prohibitions

- **Prohibition on treating SaaS as taxable** — NEVER treat SaaS as taxable in Nevada.
- **Prohibition on computation** — NEVER compute any number.
