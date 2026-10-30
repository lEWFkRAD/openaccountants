---
name: az-corporate-income-tax
description: >
  Use this skill whenever asked about Arizona corporate income tax for
  tax year 2026 -- Form 120/120A filing, the 4.9% flat rate and fifty-dollar
  minimum under A.R.S. §43-1111, combined and consolidated group filing,
  S-corporation treatment under §43-1126, LLCs taxed as corporations,
  estimated-payment thresholds, the 15th-day-of-4th-month deadline, and
  e-file mandates. Trigger on "Arizona corporate income tax", "Arizona
  Form 120", "Form 120A", "AZ corporation tax rate", "4.9 percent
  Arizona", "Arizona combined return", "AZDOR corporate". Source-cited
  draft; statute text read 2026-10-28.
jurisdiction: US-AZ
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - az-income-tax
---

# Arizona corporate income tax v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft; sources read 27–28 October 2026: AZDOR's Corporate Income Tax page (forms, due dates, estimates, e-file, LLC treatment), AZDOR's interest-rate page, the 2026 Booklet 120/165ES and the 2024 Form 120, and the azleg.gov texts of A.R.S. §§43-941, 43-942, 43-947, 43-1111, 43-1126, 43-1131, 43-1132, 43-1133, 43-1134, 43-1141, 43-1143, 43-1145, 43-1146, 43-1151, 43-1201, 43-1231. Items not tied to a primary source this run are on the Not yet confirmed line in Sources.

Every corporation subject to the Arizona Income Tax Act of 1978 must file an Arizona corporate income tax return (AZDOR corporate page, read 2026-10-28). An LLC that makes a valid federal election to be taxed as a corporation files the same return; a single-member disregarded LLC is treated as a branch or division of its owner and is included in the owner's return (AZDOR, citing ruling CTR 97-2, read 2026-10-28). An S corporation that has made a federal subchapter S election is not subject to the corporate chapter to the extent it is not subject to federal income tax, but must still file an annual return showing each shareholder's pro rata share by the fifteenth day of the third month after year-end (§43-1126, read 2026-10-28). Exempt organizations under §43-1201 are outside the tax, but their unrelated business taxable income (IRC §512 definition) is taxed under §43-1111 (§43-1231, read 2026-10-28).

## Rates, bands and thresholds

| Item | Rate / amount | Source |
|---|---|---|
| Corporate income tax on entire Arizona taxable income (taxable years beginning after 31 Dec 2016) | **4.9%** | A.R.S. §43-1111 (read 2026-10-28): "For taxable years beginning from and after December 31, 2016, 4.9 per cent of net income"; the 2026 Booklet 120/165ES computes estimated tax "by 4.9%" and the 2024 Form 120 states "Tax is 4.9 percent of line 15 or fifty dollars ($50), whichever is greater" |
| Minimum tax | **$50** (tax is the greater of fifty dollars or 4.9%) | A.R.S. §43-1111: "taxes in an amount of the greater of fifty dollars or:"; 2024 Form 120: "fifty dollars ($50), whichever is greater" |
| S corporation | no entity-level tax to the extent not federally taxable; informational return still due | §43-1126 (read 2026-10-28) |
| Exempt-org UBIT | same 4.9%/$50 structure | §43-1231 (read 2026-10-28); 2026 Booklet 120/165ES: exempt organizations with UBTI multiply by "the corporate tax rate, 4.9%" |

Arizona has no graduated corporate rate and no separate franchise or gross-receipts income tax; the Transaction Privilege Tax is a separate privilege tax on sellers (see `az-sales-tax` / `az-transaction-privilege-tax`).

## The taxable base

Arizona taxable income starts from federal taxable income with Title 43 adjustments; for a multistate corporation the base is the apportioned share. Apportionment follows the UDITA-style article: property factor at original cost, rented property at eight times the net annual rental rate (§43-1141, read); payroll factor = compensation paid in Arizona over compensation paid everywhere (§43-1143, read); sales factor = Arizona sales over total sales, with tangible-property sales sited where delivered or shipped to the purchaser (§43-1145/§43-1146, read). Nonbusiness income (rents, royalties, capital gains, interest, dividends) is allocated, not apportioned (§43-1134, read). A taxpayer is "taxable in another state" for denominator purposes if that state subjects it to a net-income/franchise tax or has jurisdiction to do so (§43-1133, read). The fiscal year is the taxable year; calendar-year corporations file for 2026 in 2027.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Annual corporate return (Form 120 or 120A) | 15th day of the 4th month after the close of the taxable year (April 15 for calendar-year filers) | AZDOR corporate page (read 2026-10-28): "Returns are due by the 15th day of the fourth month following the close of the taxable year" |
| Estimated tax payments | 15th day of the 4th, 6th, 9th and 12th months of the taxable year | AZDOR corporate page (read 2026-10-28) |
| S-corporation return | 15th day of the 3rd month after year-end | §43-1126(B) (read 2026-10-28) |
| Amended return (Form 120X) after a federal final determination | within 90 days of the IRS final determination | AZDOR corporate page (read 2026-10-28): "must file an Arizona amended return on Form 120X within 90 days of final determination of the federal amended return by the IRS" |
| E-filing | mandatory for corporations and partnerships | AZDOR corporate page (read 2026-10-28) |

Estimated-tax and EFT dollar thresholds from the AZDOR page quote 2020/2021 text: "Corporations expecting an Arizona income tax liability for the 2020 taxable year of $1,000 or more must make Arizona estimated income tax payments" and corporations expecting a 2021 liability "of $500 or more must make Arizona estimated income tax payments using EFT" (AZDOR corporate page, read 2026-10-28). The current-year dollar thresholds are on the Not yet confirmed line -- confirm with AZDOR before setting a payment calendar.

Form selection (AZDOR page, read): Form 120 for multistate corporations, partners in multistate partnerships, unitary-group combined filers, and affiliated groups electing consolidation; Form 120A only for a separate-entity filer taxable entirely within Arizona.

## Penalties and interest

Interest on under- and overpayments is the federal §6621 rate (federal short-term plus three percentage points), compounded annually, with outstanding interest added to principal each January 1 (AZDOR interest page, read 2026-10-28: "that rate of interest for both overpayments and underpayments for all taxpayers is the federal short-term rate, determined by the IRC, plus three percentage points"; 2026 quarterly table rows: first quarter 7%, second quarter 6%, third and fourth quarters 7%). Late-filing/failure-to-pay penalty percentages are not tied out this run -- see the Not yet confirmed line. Common failure mode: a corporation with consignment inventory in Arizona can be pulled into nexus -- §43-1132(E) (read) relieves apportionment only where strict conditions are met (contract requirement, customer's premises, and others).

## Cross-border points

A foreign (out-of-state or out-of-country) corporation not itself subject to Arizona tax has its income and related expenses excluded from Arizona allocation/apportionment (§43-1132(A)-(B), read) -- unless it is a member of an Arizona affiliated group under §43-947 (§43-1132(D), read). On dissolution, surrender, or term reduction, a tax-clearance certificate from the department is required before the court or corporation commission acts; the department responds within thirty days (§43-1151, read). Shareholder-level cross-border treatment of S income and nonresident partners: see `az-cross-border`.

## Worked examples

A calendar-year C corporation has $400,000 of income apportioned to Arizona for 2026 (hypothetical facts). Tax:

```oa-check
name: corporate tax on 400000 apportioned income
inputs:
  income: 400000
  rate: 0.049
steps:
  - tax: income * rate
  - due: max(50, tax)
expected:
  tax: 19600.00
  due: 19600.00
```

A unitary group files combined (hypothetical facts): group-wide sales $10,000,000, of which $3,000,000 delivered to Arizona purchasers; combined Arizona-apportionable income $2,000,000 (single sales factor assumed for the example):

```oa-check
name: sales factor and combined tax
inputs:
  az_sales: 3000000
  total_sales: 10000000
  income: 2000000
  rate: 0.049
steps:
  - factor: az_sales / total_sales
  - apportioned: income * factor
  - tax: apportioned * rate
expected:
  factor: 0.30
  apportioned: 600000.00
  tax: 29400.00
```

## Ask the client first

- Is the entity taxed as a corporation federally (including an LLC that elected it)? Disregarded single-member LLCs ride the owner's return.
- Is the group unitary (combined Form 120) or an affiliated group electing consolidation (§43-947 -- confirm current mechanics with ADOR)?
- Any consignment inventory, remote employees, or marketplace sales creating Arizona nexus?
- Expected liability at or above the estimate threshold? Confirm the current estimate/EFT dollar thresholds with AZDOR before setting the payment calendar.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| AZDOR -- Corporate Income Tax | https://azdor.gov/business/corporate-income-tax | 2026-10-28 |
| AZDOR -- Corporate Tax Forms | https://azdor.gov/forms/corporate-tax-forms | 2026-10-28 |
| AZDOR -- Interest Rates | https://azdor.gov/business/interest-rates | 2026-10-28 |
| AZDOR -- 2026 Booklet 120/165ES (Form 120/PTE-W) | https://azdor.gov/sites/default/files/document/FORMS_CORPORATE_2026_120_165ESBooklet.pdf | 2026-10-28 |
| Arizona Form 120 (2024) -- Corporation Income Tax Return | https://azdor.gov/sites/default/files/document/FORMS_CORPORATE_2024_120_f.pdf | 2026-10-28 |
| A.R.S. §43-941 -- Allocation; affiliated taxpayers | https://www.azleg.gov/ars/43/00941.htm | 2026-10-28 |
| A.R.S. §43-942 -- Allocation; controlled corporations | https://www.azleg.gov/ars/43/00942.htm | 2026-10-28 |
| A.R.S. §43-947 -- Consolidated returns; affiliated group | https://www.azleg.gov/ars/43/00947.htm | 2026-10-28 |
| A.R.S. §43-1111 -- Tax rates for corporations | https://www.azleg.gov/ars/43/01111.htm | 2026-10-28 |
| A.R.S. §43-1126 -- Small business corporation; election; return | https://www.azleg.gov/ars/43/01126.htm | 2026-10-28 |
| A.R.S. §43-1131/1132/1133/1134 -- Liability, allocation, taxability | https://www.azleg.gov/ars/43/01131.htm | 2026-10-28 |
| A.R.S. §43-1141/1143/1145/1146 -- Apportionment factors and situs | https://www.azleg.gov/ars/43/01141.htm | 2026-10-28 |
| A.R.S. §43-1151 -- Tax clearance | https://www.azleg.gov/ars/43/01151.htm | 2026-10-28 |
| A.R.S. §43-1201 -- Exempt organizations | https://www.azleg.gov/ars/43/01201.htm | 2026-10-28 |
| A.R.S. §43-1231 -- Unrelated business income | https://www.azleg.gov/ars/43/01231.htm | 2026-10-28 |

Not yet confirmed: the current-year corporate estimated-tax and EFT dollar thresholds (the AZDOR page quotes 2020/2021 amounts); the §43-323 e-file mandate text; late-filing and failure-to-pay penalty percentages; 2027 interest-rate quarters beyond the AZDOR 2026 table.

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
