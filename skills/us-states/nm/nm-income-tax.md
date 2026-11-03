---
name: nm-income-tax
description: Use this skill whenever asked about New Mexico individual income tax for self-employed / sole proprietors. Trigger on phrases like "New Mexico income tax", "NM income tax", "Form PIT-1", "NM Taxation and Revenue", "NM self-employment tax".
version: "0.2"
jurisdiction: US-NM
tax_year: 2025
last_updated: 2026-11-03
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NM Income Tax

## Who this applies to

> **Scope.** This skill covers New Mexico Form PIT-1 (Personal Income Tax Return) for full-year NM residents who are sole proprietors or single-member LLC owners. Tax year 2025 (returns filed in 2026). New Mexico uses a six-bracket graduated rate structure restructured under HB 252 effective 2025.

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax (Personal Income Tax) |
| Jurisdiction | New Mexico (US-NM) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form PIT-1 |
| Supporting schedules | Schedule PIT-B (Nonresident/Part-year), Schedule PIT-CR (Credits), Schedule PIT-ADJ (Adjustments) |
| Tax structure | Graduated (6 brackets) |
| Tax authority | New Mexico Taxation and Revenue Department |
| Statute | N.M. Stat. Ann. §7-2-7 (Income Tax Act) |

## Rates, bands and thresholds

### Tax brackets -- Single / Estates and trusts (TY 2025)

Verified against the 2025 Tax Expenditure Report bracket table and the 2025 Tax Rate Table (2025trt).

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $5,500 | 1.5% | $0 |
| $5,500 | $16,500 | 3.2% | $82.50 |
| $16,500 | $33,500 | 4.3% | $434.50 |
| $33,500 | $66,500 | 4.7% | $1,165.50 |
| $66,500 | $210,000 | 4.9% | $2,716.50 |
| $210,000 | -- | 5.9% | $9,748 |

### Tax brackets -- Married filing jointly / Head of household / Qualifying surviving spouse (TY 2025)

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $8,000 | 1.5% | $0 |
| $8,000 | $25,000 | 3.2% | $120 |
| $25,000 | $50,000 | 4.3% | $664 |
| $50,000 | $100,000 | 4.7% | $1,739 |
| $100,000 | $315,000 | 4.9% | $4,089 |
| $315,000 | -- | 5.9% | $14,624 |

### Tax brackets -- Married filing separately (TY 2025)

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $4,000 | 1.5% | $0 |
| $4,000 | $12,500 | 3.2% | $60 |
| $12,500 | $25,000 | 4.3% | $332 |
| $25,000 | $50,000 | 4.7% | $869.50 |
| $50,000 | $157,500 | 4.9% | $2,044.50 |
| $157,500 | -- | 5.9% | $7,312 |

### Standard deduction

New Mexico allows the federal standard deduction or federal itemized deduction amount (Form PIT-1, Line 12: enter the allowable federal amount from federal Form 1040/1040-SR, line 12). Mark PIT-1 box 12a only if you itemized on the federal return. The specific TY2025 federal dollar amounts are listed under Not yet confirmed (they are federal figures, not stated in the NM source).

### Low-and-middle-income exemption

- **Low-and-middle-income exemption (N.M. Stat. Ann. §7-2-5.8)** -- New Mexico offers a low-and-middle-income exemption of up to $2,500 per qualified exemption, based on adjusted gross income. All taxpayers (residents, part-year residents, first-year residents, nonresidents) may claim this exemption in full. Income limits verified verbatim vs the archived NM Taxation and Revenue Department PIT overview (archived 2026-10-28): "$36,667 (if single)", "$27,500 (if married filing separately)", "$55,000 (if married filing jointly, qualified widow(er), or head of household)". The statutory basis 7-2-5.8 NMSA 1978 is confirmed in the 2025 Tax Expenditure Report.

### Age 65 or older / blind exemption (Schedule PIT-ADJ)

- Up to $8,000 each for the taxpayer and spouse age 65 or older (or blind). Per the 2025 PIT-ADJ instructions Table 1, the full $8,000 applies only at AGI up to $30,000 (MFJ/HOH/qualifying surviving spouse), $18,000 (single) or $15,000 (MFS); the exemption phases down in steps and reaches $0 above AGI $51,000 / $28,500 / $25,500 respectively. Example in the instructions: AGI $28,000 with two qualifying persons gives $16,000 ($8,000 x 2).
- Also on the archived NM overview page: $3,000 medical-expense exemption for 65+ with expenses over $28,000; refundable medical care credit $2,800 for unreimbursed expenses of $28,000+.

### Local income tax

- **Local income tax** -- New Mexico does not permit local income taxes.

## The taxable base

### How this skill works with the federal return

New Mexico taxable income starts with **federal adjusted gross income (FAGI)** from federal Form 1040, Line 11.

1. **Start with federal AGI** → PIT-1
2. **Add NM additions** -- items NM adds back
3. **Subtract NM subtractions** -- items NM excludes
4. **Subtract NM exemptions** (low-and-middle-income exemption, blind/aged exemptions)
5. **Subtract standard or itemized deductions** (NM follows federal amounts)
6. **Result = NM taxable income**
7. **Apply the graduated rate schedule** → NM tax
8. **Apply credits and rebates** (Schedule PIT-CR) → final tax due or refund

### Key addition modifications

| Addition | Description |
| --- | --- |
| Lump-sum distributions | Certain lump-sum distributions not included in federal AGI |
| NM income not in federal AGI | Income taxable by NM but excluded from federal return |

### Key subtraction modifications

| Subtraction | Description |
| --- | --- |
| US government bond interest | Interest from US Treasury obligations |
| Social Security | NM does not tax Social Security benefits |
| Military retirement pay | Exempt for certain qualifying individuals |
| Age 65+ income exemption | Up to $8,000 each; full $8,000 only at AGI up to $30,000 (MFJ/HOH/QSS), $18,000 (single) or $15,000 (MFS), phasing to $0 above $51,000 / $28,500 / $25,500 (2025 PIT-ADJ Table 1) |

### Self-employed specific rules

- **Self-employment income flow** -- Schedule C net profit flows into federal AGI, which is the starting point for NM. NM follows the federal self-employment tax deduction (deductible half of SE tax) through federal AGI.

### Estimated tax

- **Estimated tax threshold** -- every individual liable for state income tax must pay estimated tax if the tax shown on the return for the year exceeds the amount withheld by $1,000 or more (FYI-320; N.M. Stat. Ann. §7-2-12.2). First-year NM residents are NOT subject to estimated payment requirements in their first year of residency.

**Estimated tax installment due dates (calendar-year taxpayers, FYI-320)**

| Installment | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Form PIT-ES is used for estimated tax payments.

### Gross Receipts Tax (GRT) interaction

- **GRT interaction** -- Self-employed taxpayers in NM are also subject to the Gross Receipts Tax (GRT), which is NM's equivalent of a sales/use tax but is imposed on the seller's gross receipts. Unlike a traditional sales tax, the GRT is imposed on the business (not the buyer), though it is commonly passed through to customers. GRT applies to most services as well as goods (unlike most state sales taxes). Rates vary by location: combined state + local rates run from 4.875% to 10.8125% (FYI-105, schedule for July 1, 2025 - June 30, 2026; state portion 4.875%). Self-employed service providers must register for and collect/remit GRT. GRT paid is deductible as a business expense on the federal Schedule C.

### Working Families Tax Credit (NM EIC)

- **NM Working Families Tax Credit (N.M. Stat. Ann. §7-2-18.15)** -- NM offers a refundable credit equal to 25% of the federal Earned Income Credit, confirmed for TY2025 by the 2025 Form PIT-1 instructions ("The credit is 25% of the Earned Income Credit (EIC)... for which you are eligible the same tax year"). This is particularly valuable for lower-income self-employed taxpayers.

## Deadlines and filing

- **Filing due date (TY2025):** April 15, 2026 for both electronic and paper returns.
- **Extension:** New Mexico recognizes the IRS automatic six-month extension. If federal Form 4868 was filed for TY2025, October 15, 2026 is the extended due date. An extension to file does NOT extend the time to pay; interest continues to accrue.
- Estimated-tax installment dates appear under Self-employed specific rules above.

## Penalties and interest

- **Negligence penalty for late filing or late payment:** 2% of the tax due for each month or part of a month, up to a maximum of 20% (2025 PIT-1 instructions, "Interest and Penalties").
- **Civil penalty for willful evasion:** 50% of the tax due, minimum $25.
- **Interest:** computed on a daily basis at the rate established for individual income tax purposes by the Internal Revenue Code (changes quarterly, announced by the IRS); interest cannot be waived by law.
- **Underpayment of estimated tax:** penalty (in the form of interest) accrues from the due date of the installment; see FYI-320 and Form RPD-41272 (alternative method).

## Cross-border points

- **NM-T2-01** -- Multi-state income: Taxpayer has income from another state  _(NM taxes worldwide income of residents. Credit for taxes paid to other states available on Schedule PIT-CR.)_
- **NM-T2-02** -- GRT vs. income tax interaction  _(GRT is a separate tax on gross receipts, not a credit against income tax. GRT paid is deductible as a business expense on federal Schedule C, which flows through to NM.)_
- **NM-T2-03** -- Technology jobs tax credit  _(NM offers credits for qualifying technology businesses. Requires certification.)_
- **NM-T2-04** -- Angel investment credit  _(NM allows credits for qualified investments in NM small businesses. Requires approval from NM Economic Development Department.)_
- **NM-T2-05** -- Federal IRC conformity  _(NM's conformity with the IRC should be verified for recent federal changes. NM generally has rolling conformity but may decouple from specific provisions.)_
- **NM-T2-06** -- Community property  _(New Mexico IS a community property state. MFS returns require community property income allocation.)_

## Worked examples

### Worked example 1: single filer, NM taxable income $65,000 (TY2025)

```oa-check
name: single filer NM taxable income 65000 TY2025
inputs:
  ti: 65000
steps:
  - b1: 5500 * 0.015
  - b2: (16500 - 5500) * 0.032
  - b3: (33500 - 16500) * 0.043
  - b4_tax: (ti - 33500) * 0.047
  - total: b1 + b2 + b3 + b4_tax
expected:
  b1: 82.5
  b2: 352
  b3: 731
  b4_tax: 1480.5
  total: 2646
```


Apply the single bracket table (marginal buildup, matching the 2025 Tax Expenditure Report's own example):

- First bracket: 5500 * 0.015 = $82.50
- Second bracket: (16500 - 5500) * 0.032 = $352.00
- Third bracket: (33500 - 16500) * 0.043 = $731.00
- Fourth bracket: (65000 - 33500) * 0.047 = $1,480.50
- Total NM income tax: 82.50 + 352.00 + 731.00 + 1480.50 = $2,646.00

### Worked example 2: married filing jointly, NM taxable income $120,000 (TY2025)

```oa-check
name: mfj NM taxable income 120000 TY2025
inputs:
  ti: 120000
steps:
  - b1: 8000 * 0.015
  - b2: (25000 - 8000) * 0.032
  - b3: (50000 - 25000) * 0.043
  - b4: (100000 - 50000) * 0.047
  - b5: (ti - 100000) * 0.049
  - total: b1 + b2 + b3 + b4 + b5
expected:
  b1: 120
  b2: 544
  b3: 1075
  b4: 2350
  b5: 980
  total: 5069
```


- First bracket: 8000 * 0.015 = $120.00
- Second bracket: (25000 - 8000) * 0.032 = $544.00
- Third bracket: (50000 - 25000) * 0.043 = $1,075.00
- Fourth bracket: (100000 - 50000) * 0.047 = $2,350.00
- Fifth bracket: (120000 - 100000) * 0.049 = $980.00
- Total NM income tax: 120 + 544 + 1075 + 2350 + 980 = $5,069.00

### Worked example 3: Working Families Tax Credit

```oa-check
name: NM WFTC 25 percent of federal EIC 2000
inputs:
  eic: 2000
steps:
  - wftc: eic * 0.25
expected:
  wftc: 500
```


A taxpayer eligible for a federal EIC of $2,000 claims the NM WFTC at 25%:

- NM WFTC: 2000 * 0.25 = $500.00 (refundable, Schedule PIT-CR)

## Ask the client first

- Residency status (full-year, part-year, nonresident) -- part-year/nonresident use Schedule PIT-B.
- Community-property allocation if married filing separately.
- Whether GRT registration applies to the client's services.
- Whether the taxpayer or spouse is 65+ or blind (PIT-ADJ exemption phases out by AGI -- see table above).

### Tier 1 rules -- deterministic

- **NM-T1-01** -- NM taxable income = federal AGI ± NM modifications − exemptions − deductions  _(N.M. Stat. Ann. §7-2-2)_
- **NM-T1-02** -- Tax computed using a 6-bracket graduated schedule, TY 2025 rates confirmed vs the 2025 Tax Expenditure Report and 2025 Tax Rate Table  _(N.M. Stat. Ann. §7-2-7; HB 252)_
- **NM-T1-03** -- Starting point is federal AGI (Form 1040, Line 11)  _(N.M. Stat. Ann. §7-2-2)_
- **NM-T1-04** -- Social Security benefits fully exempt  _(N.M. Stat. Ann. §7-2-2(S))_
- **NM-T1-05** -- Low-and-middle-income exemption: up to $2,500 per qualified exemption  _(N.M. Stat. Ann. §7-2-5.8)_
- **NM-T1-06** -- NM Working Families Tax Credit is a refundable 25% of federal EIC (TY2025, 2025 PIT-1 instructions)  _(N.M. Stat. Ann. §7-2-18.15)_
- **NM-T1-07** -- Estimated tax required if tax shown exceeds withholding by $1,000 or more  _(N.M. Stat. Ann. §7-2-12.2)_
- **NM-T1-08** -- NM follows federal standard or itemized deduction amounts (PIT-1 line 12)  _(N.M. Stat. Ann. §7-2-2)_

### Supplier pattern library

| Input needed | Where to find it |
| --- | --- |
| Federal AGI | Federal Form 1040, Line 11 |
| NM additions | PIT-1 / Schedule PIT-ADJ |
| NM subtractions | PIT-1 / Schedule PIT-ADJ |
| Standard/itemized deduction | Federal amounts (NM conforms) |
| Low-and-middle-income exemption | Based on AGI and number of exemptions |
| Tax credits and rebates | Schedule PIT-CR |
| Estimated tax payments | PIT-ES records |
| NM withholding | W-2 Box 17 / 1099 NM withholding amounts |
| Federal EIC amount | Federal Schedule EIC / Form 1040 (for NM WFTC calculation) |

### Form mapping

| Form PIT-1 Line | Description | Source |
| --- | --- | --- |
| Line 7 | Federal adjusted gross income | Federal 1040, Line 11 |
| Line 8 | NM additions | Schedule PIT-ADJ |
| Line 10 | NM subtractions | Schedule PIT-ADJ |
| Line 13 | NM exemptions (low-and-middle-income, blind, aged) | Computed |
| Line 15 | Standard or itemized deduction | Federal amount |
| Line 17 | NM taxable income | Computed |
| Line 18 | NM income tax | From rate schedule |
| Line 21 | Credits and rebates | Schedule PIT-CR |
| Line 25 | NM withholding | W-2s / 1099s |
| Line 26 | Estimated tax payments | PIT-ES payments |
| Line 31 | Amount owed or refund | Computed |

### Refusal catalogue

- **R-NM-01** -- Part-year or nonresident  _("NM part-year and nonresident returns require Schedule PIT-B. This is outside the scope of this skill.")_
- **R-NM-02** -- Corporate return  _("This skill covers personal income tax only (Form PIT-1). Corporate income tax (CIT) is not covered.")_
- **R-NM-03** -- Fiduciary return  _("NM fiduciary returns (Form FID-1) are not covered by this skill.")_
- **R-NM-04** -- Amended return  _("NM amended returns (amended PIT-1) are not covered.")_
- **R-NM-05** -- GRT computation  _("NM Gross Receipts Tax is a separate tax. See nm-sales-tax.md for GRT details.")_
- **R-NM-06** -- Oil and gas taxation  _("NM oil, gas, and mineral taxation (severance taxes, conservation taxes) requires specialist review.")_

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 Form PIT-1 instructions | https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf | 2026-10-31 |
| 2025 Schedule PIT-ADJ instructions | https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf | 2026-10-31 |
| 2025 Tax Rate Table (2025trt) | https://realfile.tax.newmexico.gov/2025trt.pdf | 2026-10-31 |
| FYI-320 Estimated Payments | https://realfile.tax.newmexico.gov/FYI-320.pdf | 2026-10-31 |
| FYI-105 Gross Receipts Tax and Compensating Tax Overview | https://realfile.tax.newmexico.gov/FYI-105.pdf | 2026-10-31 |
| 2025 Tax Expenditure Report (NM Legislature, RSTP 12/15/25) | https://www.nmlegis.gov/handouts/RSTP%20121525%20Item%202%20B%20Tax%20Expenditure%20Report.pdf | 2026-10-31 |
| HB0252 (2024 Regular Session) | https://www.nmlegis.gov/Sessions/24%20Regular/bills/house/HB0252.PDF | 2026-10-31 |
| NM Taxation and Revenue -- Personal Income Tax overview | https://www.tax.newmexico.gov/individuals/personal-income-tax-information-overview | 2026-10-28 |
| NM Taxation and Revenue -- Estimated payments page | https://www.tax.newmexico.gov/individuals/estimated-payments/ | 2026-10-31 |
| NM Taxation and Revenue -- index | https://www.tax.newmexico.gov/ | 2026-10-28 |

Not yet confirmed: TY2025 federal standard deduction dollar amounts ($15,000 single / $30,000 MFJ / $22,500 HOH -- federal figures not stated in the NM source); current-quarter interest rate percentage (IRC-linked, changes quarterly); community-property MFS allocation mechanics; NM IRC conformity date.

<!-- openaccountants-cta-block -->

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
