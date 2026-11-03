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

Sellers with Nevada sales -- state and local sales/use tax.

## Rates, bands and thresholds

| Field | Value |
| --- | --- |
| Jurisdiction | Nevada |
| State rate | 6.85%
| Local rate range | Local add-ons on top of the 6.85% state base; county combined rates run 7.10% to 8.375% |
| Maximum combined rate | 8.375% (Clark County, effective January 1, 2020; Washoe County 8.265% effective April 1, 2017) |
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

For returns filed and paid within 30 days of the due date the penalty is calculated on the graduated scale of NAC 360.395, and interest accrues at 0.75% per month (reduced from 1% effective July 1, 2011) (Nevada Department of Taxation sales and use tax page).

## Cross-border points

- Destination sourcing; interstate sales require use-tax analysis on the buyer side.

## Worked examples

No worked examples yet -- rate figures pending source confirmation.

## Ask the client first

- Nexus status (economic threshold) and SST registration.
- Whether receipts are services (not taxable in NV) or TPP/canned software.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Nevada Department of Taxation -- homepage notice | https://tax.nv.gov/ | 2026-10-28 |
| Nevada Department of Taxation, Sales Tax and Use Tax page (6.85% base; Clark 8.375% from 1/1/2020; Washoe 8.265% from 4/1/2017; NAC 360.395 graduated penalty; 0.75%/month interest from 7/1/2011) | https://tax.nv.gov/tax-types/sales-tax-use-tax/ | 2026-10-31 |
| Nevada Department of Taxation, Marketplace Facilitator/Seller FAQs (economic nexus $100,000 or 200 separate transactions) | https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/ | 2026-11-01 |

Not yet confirmed: the full county-by-county rate list beyond the rate sheets quoted by the Department (Carson City and Churchill/Storey and Nye 7.60%; Douglas, Elko, Lander, Lincoln, Lyon and Pershing 7.10%; White Pine 7.725%); special district surcharges (Tourism Improvement Districts, Stadium Entertainment Improvement District); prepared-food taxability detail.

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

### Prohibitions

- **Prohibition on treating SaaS as taxable** -- NEVER treat SaaS as taxable in Nevada.
- **Prohibition on computation** -- NEVER compute any number.
