---
name: nm-sales-tax
description: Use this skill whenever asked about New Mexico Gross Receipts Tax (GRT). Trigger on phrases like "New Mexico GRT", "Gross Receipts Tax", "NM sales tax", "NMSA §7-9". NM has a GRT, not a traditional sales tax. ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-NM
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NM Sales Tax (Gross Receipts Tax)

## Who this applies to

Sellers with New Mexico gross receipts — NM taxes the SELLER via Gross Receipts Tax (GRT), not a traditional sales tax.

**CRITICAL: NM GRT taxes virtually ALL services and most transactions. One of the broadest tax bases in the US (similar to Hawaii GET). Tax is on the seller, not the buyer.**

## Rates, bands and thresholds

| Field | Value |
| --- | --- |
| Jurisdiction | New Mexico |
| Tax type | Gross Receipts Tax (GRT) -- NOT a traditional sales tax; tax on the SELLER |
| State GRT rate | 5.125% |
| Local add-on range | 0% -- ~4.1875% | (not yet confirmed)
| Maximum combined rate | ~9.3125% | (not yet confirmed)
| Sourcing | Destination-based |
| Economic nexus | $100,000 in taxable gross receipts |
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

GRT returns are filed monthly or quarterly depending on receipts volume; the exact cadence thresholds are not yet confirmed.


## Penalties and interest

GRT late filing/payment penalties and interest apply; current rates are not yet confirmed against an archived source.

## Cross-border points

- GRT is destination-based; out-of-state sellers meeting the economic nexus threshold must register.
- NM is not an SST member.

## Worked examples

No worked examples yet — rate figures pending source confirmation.

## Ask the client first

- Whether the client's receipts are services (taxable) or deductible categories (groceries, resale, healthcare).
- Registration status with the TRD TAP portal.

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| NM Taxation and Revenue — index | https://www.tax.newmexico.gov/ | 2026-10-28 |

Not yet confirmed: state GRT rate 5.125%; local add-on range; maximum combined rate; economic nexus $100,000 threshold; penalty/interest rates.
- **Prohibition -- terminology** — NEVER call NM's tax a "sales tax" without noting it is a GRT on the seller.
- **Prohibition -- services exemption assumption** — NEVER assume services are exempt -- NM taxes virtually ALL services.
- **Prohibition -- deduction vs exemption** — NEVER confuse "deduction" with "exemption" -- NM uses deductions from gross receipts.
- **Prohibition -- computation** — NEVER compute any number.
