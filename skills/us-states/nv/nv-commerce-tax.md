---
name: nv-commerce-tax
description: Use this skill whenever asked about the Nevada Commerce Tax. Trigger on phrases like "Nevada Commerce Tax", "NV Commerce Tax", "NRS 363C", "Nevada gross receipts tax", "NV business tax", "Nevada $4 million threshold". This tax applies to business entities with Nevada gross revenue exceeding $4 million per taxable year.
version: "0.1"
jurisdiction: US-NV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NV Commerce Tax

## Who this applies to

> **Scope.** This skill covers the Nevada Commerce Tax (NRS Chapter 363C), a gross
> receipts tax imposed on business entities with Nevada gross revenue exceeding
> $4,000,000 in a taxable year. Rates range from 0.051% to 0.331% depending on
> the business category (NAICS code). The taxable year runs July 1 – June 30.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be
> reviewed by a qualified tax professional before filing.

## Rates, bands and thresholds

### Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Gross receipts tax (Commerce Tax) |
| Jurisdiction | Nevada (US-NV) |
| Taxable year | July 1 – June 30 (fiscal year) |
| Primary form | Commerce Tax Return |
| Tax structure | Industry-specific flat rates applied to gross revenue above $4M threshold |
| Rate range | 0.051% – 0.331% (26 business categories) |
| Filing deadline | August 14 (45 days after fiscal year-end) |
| Revenue threshold | $4,000,000 NV gross revenue |
| Tax authority | Nevada Department of Taxation |
| Website | https://tax.nv.gov |
| Statute | NRS Chapter 363C |

**Sources:**
- NRS 363C.100–363C.560 (Commerce Tax statutory provisions)
- Nevada Department of Taxation, Commerce Tax Return Instructions: https://tax.nv.gov
- Tax Foundation, "Nevada Approves Commerce Tax" (2015 analysis)
- AB 594 (2025 session — updated to 2022 NAICS edition)

### Rates by business category

### Complete NAICS category rate table

**Complete NAICS category rate table**

| Business category | NAICS code(s) | Tax rate |
| --- | --- | --- |
| Agriculture, forestry, fishing, hunting | 11 | 0.063% | (not yet confirmed)
| Mining, quarrying, oil and gas extraction | 21 | 0.051% | (not yet confirmed)
| Utilities and telecommunications | 22, 517 | 0.136% | (not yet confirmed)
| Construction | 23 | 0.083% | (not yet confirmed)
| Manufacturing | 31, 32, 33 | 0.091% | (not yet confirmed)
| Wholesale trade | 42 | 0.101% | (not yet confirmed)
| Retail trade | 44, 45 | 0.111% | (not yet confirmed)
| Air transportation | 481 | 0.058% | (not yet confirmed)
| Rail transportation | 482 | 0.331% | (not yet confirmed)
| Truck transportation | 484 | 0.202% | (not yet confirmed)
| Other transportation | 483, 485, 486, 487, 488, 491, 492 | 0.129% | (not yet confirmed)
| Warehousing and storage | 493 | 0.128% | (not yet confirmed)
| Publishing, software and data processing | 512, 513, 516, 518 | 0.253% | (not yet confirmed)
| Finance and insurance | 52 | 0.111% | (not yet confirmed)
| Real estate and rental and leasing | 53 | 0.250% | (not yet confirmed)
| Professional, scientific and technical services | 54 | 0.181% | (not yet confirmed)
| Management of companies and enterprises | 55 | 0.137% | (not yet confirmed)
| Administrative and support services | 561 | 0.154% | (not yet confirmed)
| Waste management and remediation services | 562 | 0.261% | (not yet confirmed)
| Educational services | 61 | 0.281% | (not yet confirmed)
| Health care and social assistance | 62 | 0.190% | (not yet confirmed)
| Arts, entertainment and recreation | 71 | 0.240% | (not yet confirmed)
| Accommodation | 721 | 0.200% | (not yet confirmed)
| Food services and drinking places | 722 | 0.194% | (not yet confirmed)
| Other services | 81 | 0.142% | (not yet confirmed)
| Unclassified | 519, 92 | 0.128% | (not yet confirmed)

### Key thresholds

**Key thresholds**

| Item | Value |
| --- | --- |
| Revenue threshold | $4,000,000 NV gross revenue |
| Filing threshold | Same — no filing required if NV gross revenue ≤ $4M |
| Minimum rate | 0.051% (mining) | (not yet confirmed)
| Maximum rate | 0.331% (rail transportation) | (not yet confirmed)
| Unclassified rate | 0.128% | (not yet confirmed)

## The taxable base

### How the Commerce Tax works

### Who must pay

Any **business entity** engaging in business in Nevada whose Nevada gross revenue exceeds $4,000,000 in a taxable year (July 1 – June 30). This includes:

- Corporations (C-corps and S-corps)
- LLCs (including single-member LLCs)
- Partnerships
- Sole proprietors
- Business trusts

### Computation

- **Commerce Tax formula** — Commerce Tax = (NV Gross Revenue − $4,000,000) × Industry Tax Rate

**Example:** A professional services firm (NAICS 54) with $6,000,000 in NV gross revenue:
- Taxable amount: $6,000,000 − $4,000,000 = $2,000,000
- Tax rate: 0.181%
- Commerce Tax: $2,000,000 × 0.00181 = **$3,620**

### Taxable year

- **Fiscal year and due date** — The Commerce Tax uses a fiscal year running July 1 through June 30 — not the calendar year. The return is due by August 14 (45 days after the June 30 year-end).

### Nevada gross revenue

- **Nevada gross revenue definition** — Nevada gross revenue means the total amount realized by a business entity from engaging in business in Nevada. It includes: - Gross receipts from sales of goods or services in NV - Rents and royalties from NV property - Other income attributable to NV business activity
- **Exclusions from NV gross revenue** — Exclusions from NV gross revenue: - Revenue already subject to gaming tax, insurance premium tax, or mining tax - Distributions from pass-through entities (to avoid double-counting) - Stock proceeds - Bad debts expensed on the federal return - Net income from a passive entity to the extent generated by another entity

### Business category determination

- **Business category determination** — If a business operates in multiple NAICS categories, it is classified in the category that generates the highest percentage of its Nevada gross revenue. You cannot split revenue across multiple categories — one rate applies to the entire taxable amount. To change your NAICS code category from a prior year, you must obtain permission from the Department using the NAICS Code Category Change form.

### Self-employed / sole proprietor specific rules

### When does the Commerce Tax affect sole proprietors?

Most sole proprietors will not owe Commerce Tax because their Nevada gross revenue is below $4,000,000. However, sole proprietors with high-revenue businesses (e.g., large consulting practices, real estate operations, wholesale/retail operations) may be subject to it.

### Interaction with federal taxes

- **Interaction with federal taxes** — - Commerce Tax paid is deductible as a business expense on federal Schedule C. - The Commerce Tax is not creditable against any other Nevada tax (except a partial credit against the Modified Business Tax / payroll tax, which only applies to employers with employees). - Nevada has no state income tax, so there is no state income tax return to file.

### Modified Business Tax (MBT) credit

- **MBT credit rule** — Businesses that pay Commerce Tax may claim a credit against the Modified Business Tax (NV's payroll tax) equal to the Commerce Tax paid, up to the amount of MBT owed. This prevents double taxation for businesses subject to both. For sole proprietors with no employees, MBT does not apply and this credit is irrelevant.

## Deadlines and filing

Commerce Tax returns are due the last day of the month following the end of the taxable year; the exact date is not yet confirmed against an archived source.

## Penalties and interest

Late-filing and late-payment penalties apply; current rates are not yet confirmed against an archived source.

## Cross-border points

**Tier 2 rules table**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| NV-T2-01 | **Multi-category business:** Business operates across multiple NAICS codes | Must classify under the single category generating the highest % of NV gross revenue. Cannot split. |
| NV-T2-02 | **Pass-through entity distributions** | Distributions from other entities should be excluded from NV gross revenue to avoid double taxation. Verify the exclusion applies to each distribution type. |
| NV-T2-03 | **Revenue sourcing** | Only revenue attributable to Nevada business activity is included. Multi-state businesses must determine NV-sourced revenue. |
| NV-T2-04 | **MBT credit optimization** | Businesses paying both Commerce Tax and MBT should optimize the credit to minimize total NV tax burden. |
| NV-T2-05 | **Fiscal year timing** | The July 1 – June 30 fiscal year does not align with most businesses' calendar year. Revenue tracking must be aligned to the Commerce Tax fiscal year. |
| NV-T2-06 | **Approaching threshold** | Businesses approaching $4M in NV gross revenue should monitor carefully — once the threshold is crossed, the tax applies to all revenue above $4M. |

## Worked examples

No worked examples yet — category rates pending source confirmation.

## Ask the client first

- Whether Nevada gross revenue exceeds the $4M threshold (not yet confirmed).
- Business category classification for the applicable rate.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Nevada Department of Taxation — homepage | https://tax.nv.gov/ | 2026-10-28 |

Not yet confirmed: $4,000,000 threshold; category rate table (0.051%–0.331%); filing deadline; penalty/interest rates.

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.

- Use it in your AI: 
- Meet the accountants: 

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

### Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| NV-T1-01 | Commerce Tax applies to business entities with NV gross revenue > $4,000,000 | NRS 363C.200 |
| NV-T1-02 | Tax = (NV gross revenue − $4,000,000) × NAICS category rate | NRS 363C.300 |
| NV-T1-03 | Taxable year is July 1 – June 30 | NRS 363C.050 |
| NV-T1-04 | Return due August 14 (45 days after year-end) | NRS 363C.200 |
| NV-T1-05 | Business category = the NAICS category generating the highest % of NV revenue | NRS 363C.097 |
| NV-T1-06 | No filing required if NV gross revenue ≤ $4,000,000 | NRS 363C.200 |
| NV-T1-07 | Commerce Tax paid may be credited against Modified Business Tax (payroll tax) | NRS 363C.300 |
| NV-T1-08 | Revenue from gaming, insurance premiums, and mining already taxed under other chapters is excluded | NRS 363C.300 |
| NV-T1-09 | Rates range from 0.051% (mining) to 0.331% (rail transportation) | NRS 363C.310–363C.560 |
| NV-T1-10 | Unclassified businesses taxed at 0.128% | NRS 363C.560 |

### Supplier pattern library

**Supplier pattern library table**

| Input needed | Where to find it |
| --- | --- |
| NV gross revenue | Business financial records (revenue attributable to NV activity, July 1 – June 30) |
| NAICS code | Business registration / prior Commerce Tax returns / census.gov NAICS lookup |
| Exclusions (pass-through distributions, stock proceeds, etc.) | Financial records, K-1s from partnerships |
| Modified Business Tax payments | NV MBT returns (for credit computation) |
| Prior year NAICS category | Prior year Commerce Tax return |

### Form mapping

**Form mapping table**

| Commerce Tax Return Line | Description | Source |
| --- | --- | --- |
| Line 1 | Business entity NAICS code category | NAICS classification |
| Line 2 | Total Nevada gross revenue | Business financial records |
| Lines 3–26 | Subtractions (pass-throughs, exclusions) | Financial records |
| Line 27 | Taxable Nevada gross revenue above $4M threshold | Computed |
| Line 28 | Tax rate per NAICS code category | Rate table |
| Line 29 | Commerce Tax due | Line 27 × Line 28 |
| Line 30 | Penalty (if applicable) | 10% of tax due if late |
| Line 31 | Interest (if applicable) | Computed |
| Line 32 | Total amount due | Line 29 + Line 30 + Line 31 |

### Refusal catalogue

**Refusal catalogue table**

| Refusal ID | Trigger | Response |
| --- | --- | --- |
| R-NV-01 | Income tax question | "Nevada does not have a state income tax. The Commerce Tax is a gross receipts tax, not an income tax." |
| R-NV-02 | Modified Business Tax computation | "The MBT (payroll tax) is a separate tax. This skill covers only the Commerce Tax." |
| R-NV-03 | Gaming tax | "Nevada gaming taxes (NRS Chapter 463) are not covered by this skill." |
| R-NV-04 | Mining tax | "Nevada mining taxes (Net Proceeds of Minerals) are not covered by this skill." |
| R-NV-05 | Business license fee | "The annual $500 NV business license fee (NRS 76) is separate from the Commerce Tax and not covered here." |
| R-NV-06 | Sales tax computation | "Nevada sales tax is covered in nv-sales-tax.md, not this skill." |
