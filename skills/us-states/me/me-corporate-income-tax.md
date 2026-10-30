---
name: me-corporate-income-tax
description: >
  Use this skill whenever asked about Maine corporate income tax for tax
  year 2026 -- the graduated corporate rate from 3.5% (income up to
  $350,000) to 8.93% (income over $3,500,000), Form 1120ME, unitary
  business and combined reporting under Rule 810, apportionment under
  Rule 801, nexus under Rule 808, and the treatment of S corporations and
  financial institutions. Trigger on "Maine corporate income tax",
  "1120ME", "Maine corporation tax", "Maine combined report", "Maine
  unitary". Source-cited draft; rate range, S-corp scope, franchise-tax
  carve-out and rule numbers verified on the MRS 1120ME page
  2026-10-28; middle bracket, deadlines and estimated-payment detail
  addback statute not yet confirmed.
jurisdiction: US-ME
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - me-income-tax
---

# Maine corporate income tax v0.1

> **General reference only.** General tax reference for AI-assisted workflows; not reviewed for any specific client's facts. Do not file, pay, or take a position on this alone -- use a qualified Maine practitioner.

Source-cited draft, run of 2026-10-28. Covers Maine corporation income tax (Form 1120ME), rates, unitary/combined reporting, and filing mechanics. **Source status:** the MRS Corporate Income Tax (1120ME) page (https://www.maine.gov/revenue/taxes/income-estate-tax/corporate-income-tax-1120me) was fetched and its text verified 2026-10-28 -- the **3.5%–8.93% graduated range with the $350,000 / $3,500,000 endpoints, the S-corporation carve-out, the financial-institution franchise-tax carve-out, and Rules 801/808/810 are verified quotes**. The **middle bracket rates, the return due date, and estimated-payment thresholds are verified from the archived 2025 Form 1120ME instructions (read 2026-10-29)**.

## Who this applies to

Per the MRS page (verified 2026-10-28):

- **All entities organized as corporations** with Maine-source income;
- **S corporations only if the corporation has federal taxable income at the corporate level** (e.g., built-in gains, passive investment income) -- otherwise pass-through treatment;
- **Not** financial institutions subject to Maine's franchise tax (Form 1120B-ME) and **not** insurance companies subject to the premiums tax;
- Combined reports required for members of a **unitary business** group -- Rule 810 (Maine Unitary Business Taxable Income, Combined Reports and Tax Returns); nexus per Rule 808; apportionment per Rule 801.

## Rates, bands and thresholds

| Maine taxable income | Rate | Source status |
|---|---|---|
| Up to $350,000 | 3.5% | verified (MRS page) |
| $350,000 – $1,050,000 | $12,250 plus 7.93% of the excess over $350,000 | 2025 Form 1120ME instructions (archived, read 2026-10-29): "$12,250 plus 7.93% of the excess over $350,000" |
| $1,050,000 – $3,500,000 | $67,760 plus 8.33% of the excess over $1,050,000 | 2025 Form 1120ME instructions (archived): "$67,760 plus 8.33% of the excess over $1,050,000" |
| $3,500,000 or more | $271,845 plus 8.93% of the excess over $3,500,000 | 2025 Form 1120ME instructions (archived): "$271,845 plus 8.93% of the excess over $3,500,000" |
| Over $3,500,000 | 8.93% | verified (MRS page) |

## The taxable base

Maine taxable income starts from federal taxable income (2025 Form 1120ME instructions: "federal taxable income … modified by Maine law and apportionable to Maine"; statute: 36 M.R.S. Title 36 Part 8). Apportionment under **Rule 801**; the 1120ME instructions state "Maine utilizes a single sales factor apportionment formula." Unitary-group combined reporting under **Rule 810** ("standards for determining Maine income tax for unitary businesses and for filing combined reports under 36 M.R.S."); the instructions define a unitary business as "characterized by unity of ownership, functional integration, centralization of management, and economic integration."

## Deadlines and filing

- Form 1120ME due date: "Form 1120ME due date: April 15, 2026" (2025 Form 1120ME instructions, archived); MRS due-dates page: "1120ME, 1120EXT-ME April 15 for calendar year filers, September 15 for filers with a year end of June 30, 15th day of the 4th month following the end of the fiscal year".
- Estimated payments: required unless the liability net of credits is under $1,000 (1120ME instructions: "less than $1,000"); quarterly installments required; safe-harbor sum of payments at least the lesser of prior-year Maine liability or 90% of current-year liability (1120ME instructions).
- Underpayment of estimated tax penalty: 10% compounded monthly for calendar 2025, 9% for calendar 2026 (1120ME instructions: "For calendar year 2025, the penalty is 10%, compounded monthly. The penalty rate for calendar year 2026 is 9%, compounded monthly"). Interest: MRS publishes the table -- "1/1/26 - 12/31/26 9% 0.024658%" (MRS Interest Rates page, read 2026-10-29).

## Penalties and interest

Late filing and late payment attract Maine Revenue Services penalties and interest; the published interest rate is "1/1/26 - 12/31/26 9%" (MRS Interest Rates page, read 2026-10-29). Specific penalty percentages: not yet confirmed.

## Cross-border points

- Nexus is Rule 808 ("describes the circumstances under which a corporation is subject to the income tax jurisdiction of Maine under 36 M.R.S., Part 8", incl. the "Exception for certain solicitation activities (P.L. 86-272)").
- Maine taxes nonresident owners' Maine-source income; pass-through entity withholding via Form 941P-ME and composite filing are the collection rails (verified -- see `me-payroll.md` and `me-cross-border.md`).

## Worked examples

**Worked example 1 -- small C corp, fully apportioned to Maine (hypothetical).** Maine taxable income $300,000 (all Maine):

```oa-check
name: ME corporate 3.5% band
inputs:
  income: 300000
  rate_low: 0.035
steps:
  - band_low: min(income, 350000) * rate_low
  - tax: band_low
expected:
  tax: 10500.00
```

**Worked example 2 -- $4,000,000 Maine taxable income (hypothetical)**:

```oa-check
name: ME corporate graduated 4M
inputs:
  income: 4000000
  rate_low: 0.035
  rate_mid: 0.0793
  rate_high: 0.0893
steps:
  - band_low: min(income, 350000) * rate_low
  - band_mid: (min(income, 3500000) - 350000) * rate_mid
  - band_high: max(income - 3500000, 0) * rate_high
  - tax: band_low + band_mid + band_high
expected:
  tax: 306695.00
```

## Ask the client first

- Is the entity part of a unitary group (common ownership + integrated operations)? → combined report under Rule 810.
- Any factor presence (property, payroll, sales) in Maine that could create Rule 808 nexus?
- Is the S corp carrying federal corporate-level taxable income (built-in gains, passive income)?
- Intercompany management/royalty fees paid out of Maine (addback exposure -- not yet confirmed)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Maine Corporate Income Tax (Form 1120ME) instructions, 2025 (rate brackets, due date) | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/25_1120me_gen_instr_w_cover_pg.pdf | 2026-10-29 |
| MRS List of Forms and Due Dates | https://www.maine.gov/revenue/tax-return-forms/due-dates | 2026-10-29 |
| MRS Interest Rates, 1992 to Present | https://www.maine.gov/revenue/tax-return-forms/interest-rates | 2026-10-29 |
| 36 M.R.S. § 5111 (individual rate statute, surcharge context) | https://legislature.maine.gov/statutes/36/title36sec5111.html | 2026-10-28 |

Not yet confirmed: the Rule 801 factor mix and Rule 810 combined-report operative text (rule PDFs archived but not line-cited here); franchise-tax (1120B-ME) rates; estimated-payment thresholds and penalty percentages for corporations.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Maine corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
