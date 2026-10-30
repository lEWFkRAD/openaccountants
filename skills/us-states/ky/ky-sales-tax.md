---
name: ky-sales-tax
description: Use this skill whenever asked about Kentucky sales and use tax. Trigger on phrases like "Kentucky sales tax", "KY sales tax", "KRS 139", "Kentucky use tax". Kentucky imposes a uniform statewide 6% with no local sales taxes. ALWAYS load us-sales-tax first.
version: 3.0
jurisdiction: US-KY
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kentucky sales and use tax, tax year 2026

> **Source-cited draft.** Built from KRS 139.200, 139.105, 139.485, 139.330 and the DOR Sales and Use Tax page, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

| Field | Value |
| --- | --- |
| Jurisdiction | Kentucky (US-KY) |
| State rate | 6% of gross receipts or purchase price, uniform statewide |
| Local sales taxes | None |
| Tax authority | [Kentucky Department of Revenue (DOR)](https://revenue.ky.gov/) |
| Legislation | KRS Chapter 139; 103 KAR Title 18 |
| SST member | Yes -- Kentucky participates in the Streamlined Sales Tax Agreement (DOR page: "The Streamlined Sales Tax Agreement is a compact of state joining together to give common definitions and rules") |

## Who this applies to

Any retailer making retail sales of tangible personal property, digital property, or the taxable services listed in KRS 139.200 into or within Kentucky, and any purchaser storing or using taxable property in Kentucky on which Kentucky tax was not paid (use tax, KRS 139.330). Remote retailers must register and collect once the economic-nexus thresholds are met (see Rates, bands and thresholds).

## Rates, bands and thresholds

- **Rate.** KRS 139.200: "A tax is hereby imposed upon all retailers at the rate of six percent (6%) of the gross receipts derived from: (1) Retail sales of: (a) Tangible personal property, regardless of the method of delivery, made within this Commonwealth; and (b) Digital property." The DOR page states: "Kentucky Sales and Use Tax is imposed at the rate of 6 percent of gross receipts or purchase price. There are no local sales and use taxes in Kentucky."
- **Economic nexus.** The DOR page states: "Remote Retailers HB 487, effective July 1, 2018, requires remote retailers with 200 or more sales into the state or $100,000 or more in gross receipts from sales into the state to register and collect Kentucky sales and use tax. The transaction and gross receipts thresholds are based on the previous or current calendar year."
- **Sourcing.** KRS 139.105 sources retail sales; receipts from the sale of a service are in this state "if and to the extent the service is delivered to a location in this state" (KRS 141.120 has the parallel market-based rule for income tax; KRS 139.105 governs sales tax sourcing).

### Taxable pattern library (per KRS 139.200(2))

| Pattern | Taxable? | Authority |
| --- | --- | --- |
| General tangible personal property | Taxable, 6% | KRS 139.200(1)(a) |
| Digital property (regardless of right of permanence or continued payment) | Taxable | KRS 139.200(1)(b) |
| Prewritten computer software access services (SaaS) | Taxable | KRS 139.200(2)(ax) |
| Data brokering services | Taxable | KRS 139.200(2)(ay) |
| Hotel/motel/lodging accommodations | Taxable | KRS 139.200(2)(a) |
| Sewer services | Taxable | KRS 139.200(2)(b) |
| Landscaping services (lawn care, tree trimming, snow plowing) | Taxable | KRS 139.200(2)(g) |
| Janitorial services (residential/commercial cleaning, carpet/upholstery/window) | Taxable | KRS 139.200(2)(h) |
| Small animal veterinary services (excluding equine/cattle/poultry etc.) | Taxable | KRS 139.200(2)(i) |
| Pet care services (grooming, boarding, sitting, obedience) | Taxable | KRS 139.200(2)(j) |
| Personal fitness training services | Taxable | KRS 139.200(2)(am) |
| Massage services (except when medically necessary) | Taxable | KRS 139.200(2)(an) |
| Cosmetic surgery services | Taxable | KRS 139.200(2)(ao) |
| Body modification services | Taxable | KRS 139.200(2)(ap) |
| Grocery food (food items and food ingredients) | Exempt | KRS 139.485 |
| Professional services (legal, accounting, medical) not listed in KRS 139.200(2) | Not taxable -- not among the enumerated services | KRS 139.200 (list is specific) |

## The taxable base

The base is gross receipts from retail sales of tangible personal property, digital property, and the enumerated services (KRS 139.200). Use tax applies to the purchase price of property stored, used or consumed in Kentucky when Kentucky tax was not collected (KRS 139.330: the purchaser's liability for the tax imposed by KRS 139.310). Retailers may collect the tax from the purchaser (KRS 139.210: separate display of tax; KRS 139.380).

## Deadlines and filing

- Returns and payments are filed with the DOR on its prescribed schedule (monthly/quarterly per account type). Verify the account's filing frequency on the DOR business portal before relying on a specific due date.
- Streamlined Sales Tax participants may register through the SST system (DOR page: "Kentucky State Specifications for Streamlined Sales Tax Participants").

## Penalties and interest

Per the DOR Penalties, Interest and Fees page: late payment and failure to collect/pay are "Two (2) percent of the total tax due for each 30 days or fraction thereof that a payment is late. The maximum penalty is 20 percent of the tax not timely withheld, collected or paid. The minimum penalty is $10." Interest on unpaid tax accrues at 9% for calendar year 2026 and 10% for 2025 (DOR interest notices under KRS 131.183(2)(a)2).

## Cross-border points

- Remote retailers: register and collect at 200 transactions or $100,000 gross receipts (see above).
- Interstate purchases: credit for sales tax legally due and paid to another state; the 740 packet's use-tax discussion notes only the additional tax above 6% is due to Kentucky when another state's rate is lower.
- Out-of-state deliveries of tangible personal property are sourced by delivery location (KRS 139.105/139.210).

## Worked examples

### Example 1: in-state retail sale (hypothetical facts)

A Kentucky retailer sells $1,000 of furniture. Kentucky tax: $1,000 × 6% = $60. No local sales tax applies.

```oa-check
name: KY sales tax 6 percent on 1000
inputs:
  sale: 1000
  rate: 0.06
steps:
  - tax: sale * rate
expected:
  tax: 60.00
```

### Example 2: remote retailer nexus test (hypothetical facts)

A remote retailer had 150 sales totaling $120,000 of Kentucky gross receipts last calendar year. The $100,000 gross-receipts threshold is met, so registration and collection are required regardless of the transaction count.

```oa-check
name: KY remote retailer nexus threshold
inputs:
  ky_receipts: 120000
  threshold: 100000
steps:
  - over: ky_receipts - threshold
  - excess: max(over, 0)
expected:
  over: 20000.00
  excess: 20000.00
```

## Ask the client first

- Does the business sell tangible personal property, digital property, or any of the services enumerated in KRS 139.200(2)?
- Are Kentucky gross receipts at or above $100,000, or Kentucky sales at or above 200, in the previous or current calendar year?
- Are purchases of taxable property made out of state and brought into Kentucky (use-tax exposure)?
- Is the business an SST participant using a certified service provider?
- Does the client sell food items (KRS 139.485 exemption) or other exempt categories?

## Sources

| Source | URL | Read on |
|---|---|---|
| KRS 139.200 (imposition of sales tax; 6%; taxable services list) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS139.200 | 2026-10-28 |
| KRS 139.330 (purchaser's liability for use tax) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS139.330 | 2026-10-28 |
| KRS 139.105 (sourcing of retail sales) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS139.105 | 2026-10-28 |
| KRS 139.485 (exemption of food items) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS139.485 | 2026-10-28 |
| DOR Sales and Use Tax page (6% rate; no local sales taxes; remote retailer thresholds; SST membership) | https://revenue.ky.gov/Business/Sales-Use-Tax/Pages/default.aspx | 2026-10-28 |
| DOR Penalties, Interest and Fees page (late payment penalties; interest rates) | https://revenue.ky.gov/Collections/Pages/Penalties-Interest-and-Fees.aspx | 2026-10-28 |
| DOR news release: interest rate update for 01-01-26 (9% on unpaid tax) | https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-26.aspx | 2026-10-28 |
| DOR news release: interest rate update for 01-01-25 (10% on unpaid tax) | https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-25.aspx | 2026-10-28 |

Not yet confirmed: the exact monthly/quarterly return due dates for a specific sales-tax account (check the DOR business portal); the current exemption certificate forms and renewal cycles (DOR guidance pages not archived this run); whether any specific prepared-food or catering categories fall outside KRS 139.485's "food items and food ingredients" definition (the statute text is archived; category-by-category rulings are not).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
