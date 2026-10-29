---
name: id-sales-tax
description: Use this skill whenever asked about Idaho sales and use tax. Trigger on phrases like "Idaho sales tax", "ID sales tax", "Idaho Code §63-3619", "Idaho SST". The Idaho sales and use tax rate is 6% (Idaho Code §63-3619); remote sellers with more than $100,000 of gross receipts from sales delivered into Idaho must register and collect (Idaho Code §63-3611(h)); resort cities may adopt local-option sales taxes by a 60% voter majority (Idaho Code §§50-1044, 50-1046). ALWAYS load us-sales-tax first.
version: "2.2"
jurisdiction: US-ID
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Idaho sales and use tax, tax year 2025

> **Source-cited draft.** Built from Idaho Code §§ 63-3603, 63-3606, 63-3611 and 63-3619 and Idaho Code Title 50, Chapter 10 (§§ 50-1044, 50-1046), plus the Idaho State Tax Commission's City Sales Taxes page, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Idaho Sales and Use Tax Skill.** The Idaho State Tax Commission administers sales and use tax under Idaho Code Title 63, Chapter 36. This skill covers the state rate, remote-seller nexus, and resort-city local-option taxes for sellers of tangible personal property into Idaho. It does NOT cover travel and convention taxes, auditorium district taxes, or industry-specific excise taxes.

## Who this applies to

Every retailer making sales at retail in Idaho, and any retailer without a physical presence in Idaho that has, in the previous calendar year or the current calendar year, cumulative gross receipts from sales delivered into Idaho in excess of one hundred thousand dollars ($100,000) — that retailer is a "retailer engaged in business in this state" and must collect and remit Idaho sales tax (Idaho Code §63-3611(h)). A retailer meeting only the §63-3611(h) economic threshold "shall not collect or remit any local sales tax or any other tax or assessment that is not imposed by" chapter 36 (§63-3611(h) proviso).

Buyers storing, using, or otherwise consuming tangible personal property in Idaho owe use tax on the same 6% base when no sales tax was charged.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| State sales tax rate | 6% of the sales price of all retail sales subject to taxation under chapter 36 | current (2025) | [Idaho Code §63-3619](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3619/) |
| Use tax rate | Also 6% (same chapter 36 base) | current (2025) | [Idaho Code §63-3619](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3619/) |
| Remote-seller economic nexus threshold | Gross receipts from sales delivered into Idaho over $100,000 in the previous or current calendar year (effective June 1, 2019) | current (2025) | [Idaho Code §63-3611(h)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3611/) |
| Local sales tax | None at county level; some resort cities adopt local-option sales taxes by 60% voter majority | current (2025) | [Idaho Code §§50-1044, 50-1046](https://legislature.idaho.gov/statutesrules/idstat/Title50/T50CH10/SECT50-1044/); [Idaho Code §50-1046](https://legislature.idaho.gov/statutesrules/idstat/Title50/T50CH10/SECT50-1046/) |
| City eligibility | Resort cities with population not in excess of 10,000 | current (2025) | [Idaho Code §50-1044](https://legislature.idaho.gov/statutesrules/idstat/Title50/T50CH10/SECT50-1044/) |
| Voter approval for a local-option tax | Sixty percent (60%) majority of voters | current (2025) | [Idaho Code §50-1046](https://legislature.idaho.gov/statutesrules/idstat/Title50/T50CH10/SECT50-1046/) |

The rate statute reads: "An excise tax is hereby imposed upon each sale at retail at the rate of six percent (6%) of the sales price of all retail sales subject to taxation under this chapter" (Idaho Code §63-3619). The tax is collected by the retailer from the consumer and computed monthly (§63-3619(b)–(c)).

## The taxable base

The base is the sales price of each retail sale of tangible personal property and taxable services subject to chapter 36 (Idaho Code §63-3619). Chapter 36 definitions control scope: for example, "farm" and "farming" mean the business of operating for gain or profit a ranch or farm, including stock, dairy, poultry, fish, fur, fruit and truck farms, ranches, ranges and orchards, and custom farming (Idaho Code §63-3603); a "new manufactured home" sold for the first time at retail is in the base, with the sale to a licensed retailer holding a valid resale certificate exempt (Idaho Code §63-3606).

Remote sellers over the $100,000 threshold collect the 6% state tax but no local sales tax (Idaho Code §63-3611(h) proviso).

## Deadlines and filing

Sales tax is computed monthly on all retail sales within the preceding month (Idaho Code §63-3619). Registration and filing frequencies are administered by the Idaho State Tax Commission; see Not yet confirmed for return due dates and prepayment thresholds.

## Penalties and interest

Penalty and interest amounts for late sales tax returns and payments are listed under Not yet confirmed — no archived primary source for them is in the evidence set yet, so this skill asserts none.

## Cross-border points

- **Remote sellers:** the $100,000 economic-nexus threshold of §63-3611(h) applies without physical presence; such sellers do not collect local resort-city taxes (§63-3611(h) proviso).
- **Resort-city local taxes** are separate voter-approved taxes under Idaho Code Title 50, Chapter 10; some resort cities limit them to lodging, liquor by the drink, and restaurant food (State Tax Commission, City Sales Taxes page). Cities with local sales taxes include Sun Valley and McCall among others (State Tax Commission, City Sales Taxes page).

## Worked examples

### Example 1: hypothetical remote-seller nexus check

A hypothetical online retailer has $85,000 of gross receipts from sales delivered into Idaho in 2025 and expects $40,000 in 2026. Cumulative receipts in any single calendar year have not exceeded $100,000, so the retailer is not yet a "retailer engaged in business in this state" under Idaho Code §63-3611(h). If 2026 receipts reach $100,001, the threshold is met for that year. Client facts are hypothetical; only the $100,000 threshold and the 6% rate are confirmed figures from the rates table above.

```oa-check
name: Remote seller, $85,000 Idaho receipts in 2025 (2025)
inputs:
  gross_receipts_2025: 85000
  nexus_threshold: 100000
steps:
  - nexus_met: gross_receipts_2025 > nexus_threshold
expected:
  nexus_met: false
```

### Example 2: hypothetical in-state sale

A hypothetical Idaho retailer makes a $1,000 taxable retail sale. Idaho sales tax at the 6% rate is $1,000 × 6% = $60, collected from the consumer (Idaho Code §63-3619(b)). Client facts are hypothetical; only the 6% rate is a confirmed figure from the rates table above.

```oa-check
name: In-state retailer, $1,000 taxable sale (2025)
inputs:
  sale_price: 1000
  rate: 0.06
steps:
  - sales_tax: sale_price * rate
expected:
  sales_tax: 60
```

## Ask the client first

1. **Cumulative Idaho-delivered gross receipts** for the previous and current calendar year — over $100,000 triggers registration (Idaho Code §63-3611(h)).
2. **Physical presence in Idaho** — any physical presence makes the retailer engaged in business regardless of receipts.
3. **Location of the buyer** — resort-city local-option taxes (e.g., Sun Valley, McCall) apply only to in-city sales by sellers that are not remote-only (Idaho Code §63-3611(h) proviso; State Tax Commission, City Sales Taxes page).
4. **Nature of the goods sold** — chapter 36 definitions and exemptions decide whether the sale is a taxable retail sale (e.g., §63-3603 farming; §63-3606 new manufactured homes).

## Sources

| Source | URL | Read on |
|---|---|---|
| Idaho Code §63-3603, Farming (definition) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3603/ | 2026-10-28 |
| Idaho Code §63-3606, New manufactured home (definition and resale exemption) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3606/ | 2026-10-28 |
| Idaho Code §63-3611, Retailer engaged in business in this state (§63-3611(h) $100,000 economic nexus; no local tax for remote sellers) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3611/ | 2026-10-28 |
| Idaho Code §63-3619, Imposition and rate of the sales tax (6% rate; monthly computation; retailer collection) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH36/SECT63-3619/ | 2026-10-28 |
| Idaho Code §50-1044, Authority for resort city nonproperty taxes (resort city defined; 10,000 population cap) | https://legislature.idaho.gov/statutesrules/idstat/Title50/T50CH10/SECT50-1044/ | 2026-10-28 |
| Idaho Code §50-1046, City local-option nonproperty taxes permitted by sixty per cent majority vote (60% approval; lodging, liquor by the drink, and sales subject to chapter 36) | https://legislature.idaho.gov/statutesrules/idstat/Title50/T50CH10/SECT50-1046/ | 2026-10-28 |
| Idaho State Tax Commission, City Sales Taxes (resort cities with local sales taxes; Sun Valley, McCall and others; some limit to lodging, alcohol, restaurant food) | https://tax.idaho.gov/taxes/sales-use/sales-tax/local-sales-tax/city-sales-tax/ | 2026-10-28 |

Not yet confirmed: the maximum resort-city local sales tax rate (earlier drafts said "up to 3%" — no archived primary source states a rate cap, so the cap amount is not asserted); the maximum combined state-plus-local rate (earlier drafts said "~9.00%"); whether Idaho's sourcing rules are destination-based for all transaction types (sourcing rules not yet archived); whether SaaS and canned downloaded software are taxable (earlier drafts asserted SaaS is not taxable and downloaded software is taxable — not tied to an archived source); the taxability rows for clothing, grocery food, prepared food, prescription drugs, professional services, manufacturing production equipment, and resale transactions from earlier drafts (each requires its own archived exemption or definition source before being asserted); sales tax return due dates, filing frequencies, and prepayment thresholds; penalty and interest amounts for late sales tax returns; Idaho's Streamlined Sales Tax (SST) membership status as a full member.

> Contributed by Michael Cutajar.

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
