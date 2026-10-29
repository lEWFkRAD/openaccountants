---
name: ms-income-tax
description: Use this skill whenever asked about Mississippi individual income tax for self-employed persons, sole proprietors, or single-member LLCs — Form 80-105, the 0%/4.4% (TY2025) and 0%/4% (TY2026) rate structure, standard deductions, exemptions, and estimated-tax rules. Trigger on "Mississippi income tax", "MS income tax", "Form 80-105", "Mississippi DOR", "Miss. Code Ann. § 27-7".
version: "0.3"
jurisdiction: US-MS
tax_year: 2026
last_updated: 2026-10-29
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mississippi individual income tax, tax year 2026

## Who this applies to

> **Scope.** This skill covers Mississippi Form 80-105 for full-year Mississippi residents who are sole proprietors or single-member LLC owners. Mississippi uses a near-flat tax: 0% on the first $10,000 of taxable income, 4.4% on income above $10,000 (TY 2025). The rate drops to 4.0% for TY 2026, with further reductions planned through 2030+.
>
> **Source-cited draft.** Rates, deductions, exemptions and thresholds verified verbatim against the archived MSDOR General Information / Tax Rates page and the archived 2025 Form 80-100 instructions (read 2026-10-28/29). No accountant has reviewed it.

Primary form: Form 80-105 (Resident Individual Income Tax Return); authority: Mississippi Department of Revenue; statute: Miss. Code Ann. § 27-7-5 et seq. Part-year residents and nonresidents file Form 80-205 (see `ms-cross-border.md`).

## Rates, bands and thresholds

### Tax rates (all filing statuses)

**Tax rates table**

| Tax year | First $10,000 | Over $10,000 |
| --- | --- | --- |
| 2025 | 0% | 4.4% ("Tax Year 2025 Excess of $10,000 of Taxable Income is taxed @ 4.4%") |
| 2026 | 0% | 4.0% ("Tax Year 2026 … @ 4%") |
| 2027 | 0% | 3.75% ("Tax Year 2027 … @ 3.75%") |

Mississippi applies the same rate structure to all filing statuses (single, MFJ, MFS, HoH). Rates and the worked example ($23,000 taxable → $572) verified verbatim vs the archived MSDOR General Information / Tax Rates page (archived 2026-10-28): "0% on the first $10,000 of taxable income. 4.4% on the remaining taxable income in excess of $10,000. The 4% rate is eliminated for tax year 2024 and forward." Filing thresholds on the same page: single gross income over $8,300 + $1,500/dependent; married over $16,600 + $1,500/dependent. Standard deduction $2,300 single / $4,600 MFJ and personal exemption $6,000 single / $12,000 MFJ also appear verbatim on that page.

### Standard deduction — 2025

**Standard deduction table**

| Filing status | Amount |
| --- | --- |
| Single | $2,300 |
| MFJ / Combined | $4,600 |
| MFS | $2,300 (each) |
| Head of Family | $3,400 |

### Personal exemptions — 2025

**Personal exemptions table**

| Filing status | Amount |
| --- | --- |
| Single | $6,000 |
| MFJ | $12,000 |
| MFS | $6,000 (each) |
| Head of Family | $8,000 |
| Each dependent | $1,500 |
| Blind taxpayer/spouse | $1,500 additional |

### Key thresholds

**Key thresholds table**

| Item | Value | Source |
| --- | --- | --- |
| Filing deadline | April 15, 2026 (for TY 2025) | Miss. Code Ann. § 27-7-41 |
| Extension | Automatic 6-month with federal extension | MSDOR policy |
| Estimated tax threshold | $200 expected liability after withholding and credits | Miss. Code Ann. § 27-7-320 |

## The taxable base

- **Separate computation process** — Mississippi taxable income is computed independently from the federal return — Mississippi does NOT start from federal AGI. Instead: 1. **Report all income** — Wages, self-employment income, interest, dividends, capital gains, rental income, etc. are reported directly on Form 80-105 and supporting schedules. 2. **Adjustments** — Mississippi allows its own adjustments (e.g., deduction for 50% of self-employment tax, contributions to MS retirement plans). 3. **Deductions** — Apply the Mississippi standard deduction OR Mississippi itemized deductions. 4. **Personal exemptions** — Subtract personal exemptions ($6,000 single, $12,000 MFJ, etc.). 5. **Mississippi taxable income** — Gross income − adjustments − deductions − exemptions. 6. **Tax** — 0% on first $10,000; 4.4% on excess (TY 2025). 7. **Credits** — Apply applicable credits. **Key difference:** Mississippi is a "separate computation" state. It does NOT piggyback on federal AGI or federal taxable income. The taxpayer must independently compute Mississippi income.  _(unsure)_

## Deadlines and filing

- **Self-employment income reporting** — Report net business income on Form 80-105 directly. Mississippi recognizes the same business income and expenses as the federal return in most cases, but the starting point is gross income, not federal AGI.  _(unsure)_
- **Self-employment tax deduction** — Mississippi allows a deduction for 50% of self-employment tax paid, mirroring the federal deduction.  _(unsure)_
- **Estimated taxes** — Self-employed taxpayers must make quarterly estimated payments if expected liability exceeds $200. Due dates: April 15, June 15, September 15, January 15.  _(unsure)_
- **Business equipment depreciation** — Mississippi generally follows federal depreciation rules, including IRC § 179 expensing. Check conformity for bonus depreciation (IRC § 168(k)).  _(unsure)_
- **Health insurance deduction** — Self-employed health insurance premiums are deductible for Mississippi purposes, consistent with the federal deduction.  _(unsure)_
- **No local income tax** — Mississippi does not permit local income taxes.  _(unsure)_

## Penalties and interest

**Tier 1 rules table**  _(see rows)_

| Rule ID | Rule | Source |
| --- | --- | --- |
| MS-T1-01 | Compute Mississippi gross income independently (do not start from federal AGI) | Miss. Code Ann. § 27-7-15 |
| MS-T1-02 | Apply 50% self-employment tax deduction | Miss. Code Ann. § 27-7-17 |
| MS-T1-03 | Apply standard deduction: $2,300 (single), $4,600 (MFJ), $3,400 (HoF) | Miss. Code Ann. § 27-7-17 |
| MS-T1-04 | Apply personal exemptions: $6,000 (single), $12,000 (MFJ), $8,000 (HoF) | Miss. Code Ann. § 27-7-21 |
| MS-T1-05 | Apply dependent exemptions: $1,500 per qualifying dependent | Miss. Code Ann. § 27-7-21 |
| MS-T1-06 | First $10,000 of taxable income: 0% | Miss. Code Ann. § 27-7-5 |
| MS-T1-07 | Taxable income over $10,000: 4.4% (TY 2025) / 4.0% (TY 2026) | Miss. Code Ann. § 27-7-5 |
| MS-T1-08 | Interest on U.S. government bonds: exempt from Mississippi tax | Miss. Code Ann. § 27-7-15 |
| MS-T1-09 | Social Security benefits: fully exempt from Mississippi tax | MSDOR guidance |
| MS-T1-10 | Mississippi does not tax retirement income from MS public retirement systems | Miss. Code Ann. § 27-7-15 |

## Cross-border points

**Tier 2 rules table**  _(see rows)_

| Rule ID | Rule | Guidance |
| --- | --- | --- |
| MS-T2-01 | **Residency determination** — Mississippi uses a domicile test. A person domiciled in Mississippi or spending 183+ days in the state is a resident. | If taxpayer has homes in multiple states, flag for professional review. |
| MS-T2-02 | **Separate computation** — Mississippi does not start from federal AGI. Verify that all income items are independently reported on Form 80-105. | Cross-check against federal return to ensure nothing is missed. |
| MS-T2-03 | **Itemized deductions** — Mississippi allows itemized deductions similar to federal Schedule A but with Mississippi-specific limits. | Compare MS itemized vs. standard deduction to choose the better option. |
| MS-T2-04 | **Credit for taxes paid to other states** — Available to prevent double taxation on income earned in other states. | Requires the other state's return. |
| MS-T2-05 | **Income tax phase-out** — Rate drops annually (4.4% → 4.0% → 3.75% → ...) with potential full elimination. Confirm the applicable rate for the tax year. | Check MSDOR for the current-year rate before filing. |
| MS-T2-06 | **Bonus depreciation conformity** — Mississippi's conformity to IRC § 168(k) should be verified for the tax year. | Compare MS conformity date to asset placed-in-service date. |

## Worked examples

**Example 1 — DOR's own worked example (verbatim from the DOR Tax Rates page).** Single taxpayer, taxable income $23,000, tax year 2025: "$10,000 X 0% = $0 $13,000 X 4.4% = $572 Total Tax Liability = $572"

```oa-check
name: MS 2025 single 23k
inputs:
  income: 23000
  zero_band: 10000
  rate: 0.044
steps:
  - above: income - zero_band
  - tax: above * rate
expected:
  tax: 572.00
```

**Example 2 — 2026 rate on the same facts (hypothetical client facts; the 4% rate is from the skill's own confirmed table above).** Single taxpayer, taxable income $23,000, tax year 2026: $10,000 at 0% + $13,000 at 4%:

```oa-check
name: MS 2026 single 23k
inputs:
  income: 23000
  zero_band: 10000
  rate: 0.04
steps:
  - above: income - zero_band
  - tax: above * rate
expected:
  tax: 520.00
```

**Supplier pattern library table**  _(see rows)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| W-2 wages from Mississippi employer | MS withholding applies; report on Form 80-105 | Most common |
| Schedule C net profit (sole prop) | Report directly on Form 80-105 | Independent computation |
| Rental income | Report on Form 80-105 | MS-source if property in MS |
| Interest on U.S. government bonds | Exempt from Mississippi tax | Miss. Code Ann. § 27-7-15 |
| Interest on non-MS muni bonds | Taxable for MS purposes | Report as income |
| Social Security benefits | Fully exempt from Mississippi tax | Do not include |
| Capital gains from asset sale | Report on Form 80-105 | No special MS rate |
| 1099-NEC freelance income | Report directly on Form 80-105 | Estimated payments likely needed |

## Ask the client first

**Form mapping table**  _(see rows)_

| Mississippi form / schedule | What it covers | Federal counterpart |
| --- | --- | --- |
| Form 80-105 | Resident Individual Income Tax Return | Form 1040 |
| Form 80-205 | Non-Resident / Part-Year Resident Return | Form 1040 |
| Form 80-106 | Individual Income Tax Adjustments | Schedule 1 (Form 1040) |
| Form 80-107 | Income Tax Credits Summary | N/A |
| Form 80-108 | Schedule of Deductions (Itemized) | Schedule A (Form 1040) |
| Form 80-320 | Estimated Tax Declaration | Form 1040-ES |

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR General Information / Tax Rates — 2025/2026/2027 rates (0% first $10,000; 4.4%/4%/3.75% above), filing thresholds ($8,300/$16,600 + $1,500 per dependent), standard deduction ($2,300/$4,600/$3,400), exemptions ($6,000/$12,000/$8,000/$1,500), $23,000 worked example | https://www.dor.ms.gov/general-information | 2026-10-28 |
| MSDOR 2025 Individual Income Tax Instructions (Form 80-100, rev. 12/25) — April 15 due date, fiscal-year rule, estimated-tax $200 threshold with April 15/June 15/Sept 15/Jan 15 dates, late-pay 1/2%/month cap 25%, late-file 5%/month cap 25% min $100, 3% gambling withholding, other-state credit via Form 80-160 | https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf | 2026-10-29 |



**Refusal catalogue table**  _(see rows)_

| ID | Situation | Action |
| --- | --- | --- |
| MS-R-01 | Part-year or non-resident return (Form 80-205) | Refuse — out of scope |
| MS-R-02 | Corporate income tax (Form 83-100) | Refuse — out of scope |
| MS-R-03 | Corporate franchise tax | Refuse — out of scope |
| MS-R-04 | Multi-state income apportionment | Refuse — flag for professional review |
| MS-R-05 | Amended returns | Refuse — out of scope |
| MS-R-06 | Tax year other than current | Refuse — rates change annually during phase-out |
| MS-R-07 | Partnership / S-corp pass-through returns | Refuse — out of scope |

---

Not yet confirmed: the 183-day/domicile residency test detail; statute cites for the Social Security and US-government-bond exemptions; statute cites for the 50%-self-employment-tax and self-employed health-insurance deductions; bonus-depreciation (IRC §168(k)) conformity date for 2026; whether 2026 standard deduction/exemption amounts change from the 2025 figures archived here.

---

---

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
