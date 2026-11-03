---
name: nm-sales-tax
description: Use this skill whenever asked about New Mexico Gross Receipts Tax (GRT). Trigger on phrases like "New Mexico GRT", "Gross Receipts Tax", "NM sales tax", "NMSA §7-9". NM has a GRT, not a traditional sales tax. ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-NM
tax_year: 2025
last_updated: 2026-11-03
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NM Sales Tax (Gross Receipts Tax)

## Who this applies to

Sellers with New Mexico gross receipts -- NM taxes the SELLER via Gross Receipts Tax (GRT), not a traditional sales tax.

**CRITICAL: NM GRT taxes virtually ALL services and most transactions. One of the broadest tax bases in the US (similar to Hawaii GET). Tax is on the seller, not the buyer.**

## Rates, bands and thresholds

| Field | Value |
| --- | --- |
| Jurisdiction | New Mexico |
| Tax type | Gross Receipts Tax (GRT) -- NOT a traditional sales tax; tax on the SELLER |
| State GRT rate | 4.875% (cut from 5.125% to 5% on July 1, 2022, then to 4.875% on July 1, 2023) |
| Local add-on range | 0% to 5.9375% (derived: combined rates of 4.875% to 10.8125% minus the 4.875% state portion) |
| Maximum combined rate | 10.8125% (FYI-105 rate schedule for July 1, 2025 - June 30, 2026) |
| Sourcing | Destination-based |
| Economic nexus | $100,000 or more of taxable gross receipts in the previous calendar year (marketplace providers and remote sellers without physical presence) |
| Tax authority | New Mexico Taxation and Revenue Department (TRD) |
| Portal | https://tap.state.nm.us |
| SST member | No |
| Skill version | 2.0 |

**CRITICAL: NM GRT taxes virtually ALL services and most transactions. One of the broadest tax bases in the US (similar to Hawaii GET). Tax is on the seller, not the buyer.**

## The taxable base

### Transaction pattern library

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT | Deductible from gross receipts |
| Prepared food | TAXABLE |  |
| ALL services (including professional) | TAXABLE | NM taxes virtually all services |
| SaaS | TAXABLE |  |
| Digital goods | TAXABLE |  |
| Healthcare services | DEDUCTIBLE | Specific healthcare deductions available |
| Manufacturing equipment | DEDUCTIBLE | Deduction from gross receipts |
| Prescription drugs | EXEMPT |  |
| Resale | DEDUCTIBLE |  |

## Deadlines and filing

- A monthly filing period is assigned at registration. If combined total tax due averages $500 a month or less, you may apply (Form ACD-31015) to file quarterly or semi-annually; if liability exceeds the $500-a-month average for any 12-month period you must convert back to monthly.
- Electronic filing is required if combined tax liability (GRT, compensating, withholding and related taxes) averaged $1,000 or more per month for the previous calendar year (Regulation 3.1.4.18 NMAC). File at https://tap.state.nm.us/Tap.
- If combined liability averaged $25,000 or more per month for the previous calendar year, payment in usable funds is required by the tax-due date (see FYI-401, Special Payment Methods).
- The exact return due dates are listed under Not yet confirmed.

## Penalties and interest

- Late filing or late payment: penalty of 2% per month (or partial month) of tax due, up to a maximum of 20%, minimum $5. A late-filed return with zero liability still draws the $5 minimum penalty.
- Interest accrues on a daily basis at a quarterly rate set by reference to the Internal Revenue Code (7% annual rate shown for Q2 2023 in FYI-105; the rate changes quarterly). No interest is due if accrued interest is under $1.00. Unlike penalty, interest has no 20% cap and accrues until payment.

## Cross-border points

- GRT is destination-based; out-of-state sellers and marketplace providers without physical presence must register if they have at least $100,000 of taxable gross receipts from New Mexico sales in the previous calendar year.
- Out-of-state sellers without local registration remit the state-only rate of 4.875% using location code 88-888.
- NM is not an SST member.

## Worked examples

### Worked example 1: state-only portion for an out-of-state seller

An out-of-state seller with no NM registration makes $10,000 of taxable receipts sourced to New Mexico and uses location code 88-888 (state portion only).

- Tax due: 10000 * 0.04875 = $487.50

### Worked example 2: maximum combined rate

A seller in the highest-rate jurisdiction makes $10,000 of taxable receipts at the maximum combined rate of 10.8125%.

- Tax due: 10000 * 0.108125 = $1,081.25

## Ask the client first

- Whether the client's receipts are services (taxable) or deductible categories (groceries, resale, healthcare).
- Registration status with the TRD TAP portal.
- Which jurisdiction(s) receipts are sourced to, since combined rates run from 4.875% to 10.8125%.
- **Prohibition -- terminology**: NEVER call NM's tax a "sales tax" without noting it is a GRT on the seller.
- **Prohibition -- services exemption assumption**: NEVER assume services are exempt -- NM taxes virtually ALL services.
- **Prohibition -- deduction vs exemption**: NEVER confuse "deduction" with "exemption" -- NM uses deductions from gross receipts.
- **Prohibition -- computing numbers**: NEVER compute any number.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| FYI-105 Gross Receipts Tax and Compensating Tax Overview (rates July 1, 2025 - June 30, 2026) | https://realfile.tax.newmexico.gov/FYI-105.pdf | 2026-10-31 |
| NM Taxation and Revenue -- Gross Receipts Tax overview | https://www.tax.newmexico.gov/businesses/gross-receipts-overview/ | 2026-10-31 |
| NM Taxation and Revenue -- Gross Receipts Tax rates page | https://www.tax.newmexico.gov/businesses/gross-receipts-tax-rates/ | 2026-10-31 |
| 2025 Tax Expenditure Report (NM Legislature, RSTP 12/15/25) | https://www.nmlegis.gov/handouts/RSTP%20121525%20Item%202%20B%20Tax%20Expenditure%20Report.pdf | 2026-10-31 |
| NM Taxation and Revenue -- index | https://www.tax.newmexico.gov/ | 2026-10-28 |

Not yet confirmed: GRT return due dates; per-jurisdiction local rate tables; penalty/interest rates for periods after Q2 2023 (IRC-linked quarterly rate).

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
