---
name: la-income-tax
description: Use this skill whenever asked about Louisiana individual income tax. Trigger on phrases like "Louisiana income tax", "LA income tax", "IT-540", "LDR", "R.S. 47:21", "Louisiana flat tax". Louisiana reformed to a flat 3% rate effective 2025 (Act 11 of 2024 3rd Extraordinary Session). ALWAYS load us-tax-workflow-base first.
version: "0.3"
jurisdiction: US-LA
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# LA Income Tax

## Louisiana Individual Income Tax Skill -- Self-Employed / Sole Proprietor

> **Scope.** This skill covers Louisiana Form IT-540 (Resident Individual Income Tax Return) for sole proprietors and single-member LLCs. It addresses the flat 3% income tax rate (effective 2025), the significantly increased standard deduction, and Louisiana-specific modifications to federal AGI. It does NOT cover nonresident returns (Form IT-540B), corporate returns (CIFT-620), or partnership/S-corp pass-throughs.

> **Quality tier.** Q3 -- AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

**Metadata table**

| Field | Value |
| --- | --- |
| Jurisdiction | Louisiana (US-LA) |
| Tax authority | [Louisiana Department of Revenue (LDR)](https://revenue.louisiana.gov/) |
| Filing portal | [Louisiana File Online](https://revenue.louisiana.gov/EServices) |
| Legislation | La. R.S. 47:21 et seq.; Act 11 of the 2024 Third Extraordinary Session |
| Primary form | Form IT-540 (Louisiana Resident Individual Income Tax Return) |
| Filing deadline | May 15 for calendar-year filers (not April 15); automatic six-month extension to file under La. R.S. 47:103 -- extension to file is not an extension to pay |
| Version | 0.3 |
| Date | 2026-10-28 |
| Validation status | AI-drafted -- Q3 |

### Sources consulted

1. Louisiana Department of Revenue -- Revenue Information Bulletin 25-012 (Income Tax Reform): <https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf>
2. LDR -- Individual Income Tax page: <https://revenue.louisiana.gov/individuals/general-resources/individual-income-tax/> -- fetched and text-verified 2026-10-28
3. LDR -- Declaration of Estimated Income Taxes page: <https://revenue.louisiana.gov/individuals/general-resources/declaration-of-estimated-income-taxes/> -- fetched and text-verified 2026-10-28
4. La. R.S. 47:32 -- Tax rate
5. Act 11 (H.B. 10) of the 2024 Third Extraordinary Session

## Rates, bands and thresholds

### State income tax rate

**State income tax rate table**

| Tax year | Rate | Source |
| --- | --- | --- |
| 2024 and prior | Graduated: 1.85% / 3.50% / 4.25% | La. R.S. 47:32 (prior law); [RIB 25-012 (archived PDF)](https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf) rate tables |
| 2025 and after | **Flat 3.00%** ("Act 11 repeals the graduated rates and brackets for individuals in favor of a flat 3% tax rate applicable to all taxable income") | Act 11 (H.B. 10, 2024 3rd Extraordinary Session); [RIB 25-012, archived 2026-10-28](https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf) |

- **Flat rate effective date** -- Effective January 1, 2025, Louisiana replaced its three-bracket graduated system with a flat 3% rate on all taxable income, for all filing statuses.  _(Act 11 (H.B. 10, 2024 3rd Extraordinary Session))_

### Standard deduction (2025 tax year)

**Standard deduction table**

| Filing status | Amount |
| --- | --- |
| Single | $12,500 |
| Married Filing Separately | $12,500 |
| Married Filing Jointly | $25,000 |
| Head of Household | $25,000 |
| Qualifying Surviving Spouse | $25,000 |

- **Standard deduction note** -- These amounts were significantly increased by Act 11 ("increasing it from $4,500 to $12,500 for taxpayers with a filing status of single or married filing separately"; MFJ/QSS/HoH "increasing from $9,000 to $25,000" -- RIB 25-012, archived). Beginning January 1, 2026, the standard deduction is adjusted annually for CPI inflation.  _(Act 11)_

### Personal exemptions

- **Personal exemptions repealed** -- Act 11 repealed the prior personal exemptions ($1,000 for age 65+, blind, and dependents). These are no longer available for TY2025+.  _(Act 11)_

### Retirement income exemption

- **Retirement income exemption** -- $12,000 USD (RIB 25-012: "increases the exemption for annual retirement income received by individuals aged 65 or older, raising it from $6,000 to $12,000 per person"; adjusted annually for CPI beginning in 2026 -- verified against the archived RIB 25-012 PDF, 2026-10-28)

## The taxable base

### Starting point

- **Starting point** -- Louisiana starts from federal adjusted gross income (AGI) -- Form 1040, Line 11.

### Additions to income

**Additions to income table**

| Item | Description | Source |
| --- | --- | --- |
| Out-of-state bond interest | Interest on bonds of other states must be added | La. R.S. 47:293(4) |
| Federal income tax deducted | The LDR Individual Income Tax page (verified 2026-10-28) still lists "Income taxes paid to other states" as a subtraction from federal AGI; whether a deduction for federal income taxes themselves survives Act 11 is unconfirmed | La. R.S. 47:293 |
| IRC conformity items | Act 11 authorizes a **state bonus depreciation/bonus amortization deduction** (full expensing for qualified property/QIP and R&E under IRC §174 as in effect January 1, 2024); neither may duplicate the federal deduction for the same year (RIB 25-012, verified PDF 2026-10-28) | La. R.S. 47; Act 11 |

### Subtractions from income

**Subtractions from income table**

| Item | Description | Source |
| --- | --- | --- |
| U.S. government interest | Interest on U.S. obligations | La. R.S. 47:293(6) |
| Social Security benefits | Louisiana exempts Social Security | La. R.S. 47:44.2 (citation not confirmed) |
| Taxes paid to other states | The LDR page (verified 2026-10-28) lists "Income taxes paid to other states" as a subtraction | La. R.S. 47:293(3) |
| Retirement income | Up to $12,000 for taxpayers age 65+ (RIB 25-012, verified PDF) | La. R.S. 47:44.1 (citation not confirmed) |
| Military pay | Active-duty military compensation exclusion -- for taxable years beginning before January 1, 2023, LA-domiciled military personnel filed a part-year return (LDR page, verified); current-year military treatment not confirmed | La. R.S. 47:293 |

### Resulting computation

- **Louisiana taxable income and tax formula** -- Federal AGI + additions − subtractions − standard deduction = Louisiana taxable income → times 3% = Louisiana income tax.

**Important:** The LDR Individual Income Tax page (verified 2026-10-28) confirms the subtraction for "Income taxes paid to other states" and the Schedule C credit for net tax liability paid to another state on income included on the Louisiana return. Whether a deduction for federal income taxes themselves survives Act 11 is unconfirmed -- see J-1.

## Deadlines and filing

### Estimated tax payments

- **Estimated payment requirement** -- Taxpayers must file a declaration of estimated income tax (Form IT-540ES) and pay estimated tax if their estimated Louisiana income tax after credits and withholding is expected to exceed **$1,000** (single filers) or **$2,000** (joint filers), per La. R.S. 47:116 (LDR Declaration of Estimated Income Taxes page, verified 2026-10-28).

**Estimated tax payment due dates**

| Voucher | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

- **Estimated-payment exceptions (verified, LDR page 2026-10-28)** -- R.S. 47:116(F): no estimated payments required if the return is filed and paid in full by **March 1** of the succeeding year; the 4th-quarter voucher may be filed any time on or before January 15 without penalty; the required installment is 25% of the required annual payment (the required annual payment is 90% of tax due, or 66.66% for qualified farmers and fishermen).

- **Estimated payment form** -- Use Form IT-540ES for estimated payments.

### Self-employment health insurance

- **Self-employment health insurance treatment** -- Louisiana follows federal treatment -- the deduction reduces federal AGI and flows through.

### Retirement contributions (SEP, SIMPLE, Solo 401(k))

- **Retirement contributions treatment** -- Louisiana follows federal treatment -- these deductions reduce federal AGI and flow through.

### Home office deduction

- **Home office deduction treatment** -- Louisiana follows the federal home office deduction as part of Schedule C, included in federal AGI.

### QBI deduction (Section 199A)

- **QBI deduction treatment** -- Louisiana does not allow the federal QBI deduction because Louisiana starts from federal AGI (before the QBI deduction). The QBI deduction does not affect Louisiana taxable income.

### Filing deadline

- **Filing deadline** -- Louisiana's individual income tax return (IT-540) deadline is May 15 (not April 15) -- one month later than most states. R.S. 47:103 (for taxable years beginning on or after January 1, 2022) grants an **automatic six-month extension to file** with no form or payment; the extension covers filing only -- tax due must be paid by the original due date or interest and late-payment penalty apply (LDR Individual Income Tax page, verified 2026-10-28).

## Penalties and interest

- **Underpayment of estimated tax** -- 12% annually of the underpayment amount for the underpayment period, under La. R.S. 47:118 (LDR Individual Income Tax page, verified 2026-10-28). The underpayment is the excess of the required installment (25% of the required annual payment, 90% of tax due -- 66.66% for qualified farmers and fishermen) over what was actually paid.
- **Late payment** -- payments received after the return due date are charged interest and late-payment penalty (LDR page, verified 2026-10-28); the percentage tiers under R.S. 47:1607 are not confirmed.
- **Extension ≠ payment** -- the automatic six-month extension under R.S. 47:103 extends filing only; tax due must be paid by the original due date.

**Tier 1 rules table**

| Rule | Description |
| --- | --- |
| R-1 | Apply the flat 3% rate to Louisiana taxable income. No brackets for TY2025+. |
| R-2 | Start from federal AGI and apply Louisiana modifications. |
| R-3 | Subtract the standard deduction ($12,500 single/MFS; $25,000 MFJ/HoH/QSS for TY2025). |
| R-4 | Social Security benefits are fully exempt. |
| R-5 | U.S. government bond interest is exempt. |
| R-6 | Retirement income exemption: up to $12,000 for age 65+. |
| R-7 | The filing deadline is May 15, NOT April 15; the six-month extension under R.S. 47:103 is automatic and extends filing only, never payment. |
| R-8 | Prior personal exemptions ($1,000 for age 65+, blind, dependents) were repealed by Act 11 for TY2025+. |
| R-9 | Standard deduction is adjusted annually for CPI beginning in TY2026. |
| R-10 | Estimated tax required when estimated LA tax after credits/withholding exceeds $1,000 (single) / $2,000 (joint) -- R.S. 47:116 (verified). |
| R-11 | Underpayment-of-estimated-tax penalty is 12% annually of the underpayment for the underpayment period -- R.S. 47:118 (verified). |

## Cross-border points

**Tier 2 rules table**

| Rule | Description |
| --- | --- |
| J-1 | Determine the current-year treatment of the federal income tax deduction under the reformed law. |
| J-2 | Evaluate whether itemized deductions exceed the increased standard deduction (less likely under the new $12,500/$25,000 amounts). |
| J-3 | Assess IRC conformity for any areas where Louisiana decouples from recent federal changes. |
| J-4 | Determine the CPI-adjusted standard deduction and retirement exemption amounts for TY2026+. |
| J-5 | Evaluate the Schedule C credit for net tax liability lawfully paid to another state on income included on the LA return (LDR page, verified); statute citation and ordering need confirmation. |

## Worked examples

**Example 1 -- flat 3% after standard deduction:** single filer, Louisiana taxable income before deduction $60,000.

```oa-check
name: LA flat 3% single
inputs:
  income: 60000
  std_deduction: 12500
  rate: 0.03
steps:
  - taxable: income - std_deduction
  - tax: taxable * rate
expected:
  taxable: 47500
  tax: 1425
```

Rates and deduction verified against the archived RIB 25-012 PDF (2026-10-28).

**Example 2 -- estimated-tax threshold:** estimated Louisiana tax after credits and withholding is $1,150 for a single filer -- above the $1,000 threshold, so an IT-540ES declaration is required; quarterly installment at 25% of the required annual payment:

```oa-check
name: LA estimated installment
inputs:
  est_tax: 1150
  threshold_single: 1000
steps:
  - required: est_tax - threshold_single
  - installment: est_tax * 0.25
expected:
  required: 150
  installment: 287.5
```

Threshold and 25% installment verified on the LDR Declaration of Estimated Income Taxes page (2026-10-28).

**Supplier pattern library table**

| Pattern | Louisiana treatment |
| --- | --- |
| Freelance income (Schedule C) | Flows through federal AGI → LA taxable income. Subject to flat 3% state tax. |
| Rental income (Schedule E) | Flows through federal AGI → LA taxable income. Subject to flat 3%. |
| Capital gains | Fully taxable at the flat 3% rate. |
| Interest / dividends | Taxable except U.S. government obligations (exempt). |
| Social Security | Fully exempt. |
| Retirement distributions | Up to $12,000 exempt for age 65+; remainder taxable at 3%. |

## Ask the client first

1. **Residency** -- full-year Louisiana resident (IT-540) or nonresident/part-year (IT-540B, out of this skill's scope)?
2. **Age 65+ and retirement income** -- the $12,000 retirement exemption applies per person at 65+.
3. **Income from other states** -- drives the Schedule C credit and the "income taxes paid to other states" subtraction.
4. **Estimated payments** -- does estimated LA tax after credits/withholding exceed $1,000 (single) / $2,000 (joint)?
5. **Out-of-state bond interest** -- must be added back.

**Form mapping table**

| Form IT-540 line | Description | Source |
| --- | --- | --- |
| Line 7 | Federal AGI (Form 1040, Line 11) | Federal return |
| Line 8 | Louisiana standard deduction ($12,500 or $25,000) | La. R.S. 47:293; Act 11 |
| Line 9 | Adjustments and modifications | La. R.S. 47:293 |
| Line 10 | Louisiana taxable income | Computed |
| Line 11 | Louisiana income tax (Line 10 × 3%) | La. R.S. 47:32 (as amended) |
| Lines 12–19 | Credits (nonrefundable and refundable) | Various |
| Lines 20–25 | Payments, withholding, estimated payments | Various |
| Line 30 | Balance due or refund | Computed |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Code | Situation | Action |
| --- | --- | --- |
| REF-LA-01 | Taxpayer is a nonresident or part-year resident | Refuse; requires Form IT-540B. |
| REF-LA-02 | Taxpayer has complex federal income tax deduction computations | Flag for reviewer -- interaction between federal and state deductions requires specialist analysis. |
| REF-LA-03 | Taxpayer has partnership or S-corp K-1 with Louisiana-specific adjustments | Flag for reviewer. |
| REF-LA-04 | Taxpayer claims complex credits (e.g., LA Historic Rehabilitation, Motion Picture, Enterprise Zone) | Flag for reviewer -- separate forms required. |
| REF-LA-05 | Taxpayer needs CPI-adjusted amounts for TY2026+ | Flag for reviewer -- confirm published inflation-adjusted figures. |

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| LDR Revenue Information Bulletin 25-012 (income tax reform; archived PDF) | https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf | 2026-10-28 |
| LDR Individual Income Tax page (residency, IT-540, Schedule C credit, subtractions, extension, underpayment penalty) | https://revenue.louisiana.gov/individuals/general-resources/individual-income-tax/ | 2026-10-28 |
| LDR Declaration of Estimated Income Taxes page (thresholds, dates, R.S. 47:116 exceptions) | https://revenue.louisiana.gov/individuals/general-resources/declaration-of-estimated-income-taxes/ | 2026-10-28 |

Not yet confirmed: the statute citations for the Social Security exemption (47:44.2) and retirement exemption (47:44.1); whether a deduction for federal income taxes themselves survives Act 11; the current-year military compensation exclusion scope; itemized-deduction detail; the CPI-adjusted TY2026 amounts; the resident-credit statute and ordering behind Schedule C; the late-payment penalty percentage under R.S. 47:1607.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
