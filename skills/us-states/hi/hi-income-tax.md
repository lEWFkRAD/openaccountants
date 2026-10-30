---
name: hi-income-tax
description: "Use this skill whenever asked about Hawaii individual income tax. Trigger on phrases like \"Hawaii income tax\", \"HI income tax\", \"Form N-11\", \"DOTAX income tax\", \"HRS 235-51\". Hawaii individual income tax for tax year 2025 runs twelve graduated brackets from 1.4% to 11% (HRS §235-51 and the DOTAX 2025 tax-rate schedules); returns are due April 20, 2026. ALWAYS load us-sales-tax first for GET questions."
version: "0.4"
jurisdiction: US-HI
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# HI Income Tax v0.4

> **Source-cited draft.** Built from HRS §§235-51 and 235-97, the DOTAX "Tax Rate Schedules For Taxable Years Beginning After December 31, 2025" page, and the DOTAX tax-year-2025 information page, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

> **General reference only.** This skill covers Hawaii individual income tax for self-employed individuals and sole proprietors filing Form N-11. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Hawaii Individual Income Tax Skill -- Self-Employed / Sole Proprietor.** Hawaii has one of the most progressive rate structures in the U.S. with 12 brackets ranging from 1.4% to 11%.

| Field | Value |
| --- | --- |
| Jurisdiction | US-HI (Hawaii) |
| Tax authority | Hawaii Department of Taxation (DOTAX) |
| Filing portal | [Hawaii Tax Online](https://hitax.hawaii.gov/) |
| Legislation citation | Hawaii Revised Statutes (HRS) Chapter 235 (Income Tax Law) |
| Primary form | Form N-11 (Individual Income Tax Return -- Resident) |
| Filing deadline | April 20, 2026 (for tax year 2025) |
| Extension | Automatic 6-month extension if estimated tax is paid by April 20, 2026 |

See also: `hi-sales-tax` (GET), `hi-payroll-withholding`, `hi-cross-border` (Form N-15), `hi-corporate-income-tax`.

## Who this applies to

Hawaii resident individuals filing Form N-11, with this skill focused on sole proprietors and single-member LLCs (Schedule C income flowing through federal AGI). Nonresidents and part-year residents use Form N-15 (see `hi-cross-border`). Anyone "doing business" in Hawaii must file regardless of income level.

### Refusal catalogue

| Refusal ID | Topic | Reason |
| --- | --- | --- |
| R-HI-01 | Corporate income tax (Form N-30) | Not individual income tax |
| R-HI-02 | Transient accommodations tax (TAT) | Separate regime for lodging |
| R-HI-03 | Part-year / nonresident returns (Form N-15) | Different form and allocation rules; see `hi-cross-border` |
| R-HI-04 | GET computation details | See `hi-sales-tax` |
| R-HI-05 | County surcharge details | Varies by county; requires local analysis |
| R-HI-06 | Conveyance tax | Real property transaction tax |
| R-HI-07 | Estate tax | Separate regime |

## Rates, bands and thresholds

### Tax year 2025 brackets -- Single / Married filing separately  _(HRS §235-51; DOTAX Tax Rate Schedule I, verified verbatim against the archived DOTAX schedule page)_

| Taxable income (DOTAX Schedule I wording) | Rate | Tax per the schedule |
| --- | --- | --- |
| Not over $9,600 | 1.40% | 1.40% of taxable income |
| Over $9,600 but not over $14,400 | 3.20% | $134 plus 3.20% over $9,600 |
| Over $14,400 but not over $19,200 | 5.50% | $288 plus 5.50% over $14,400 |
| Over $19,200 but not over $24,000 | 6.40% | $552 plus 6.40% over $19,200 |
| Over $24,000 but not over $36,000 | 6.80% | $859 plus 6.80% over $24,000 |
| Over $36,000 but not over $48,000 | 7.20% | $1,675 plus 7.20% over $36,000 |
| Over $48,000 but not over $125,000 | 7.60% | $2,539 plus 7.60% over $48,000 |
| Over $125,000 but not over $175,000 | 7.90% | $8,391 plus 7.90% over $125,000 |
| Over $175,000 but not over $225,000 | 8.25% | $12,341 plus 8.25% over $175,000 |
| Over $225,000 but not over $275,000 | 9.00% | $16,466 plus 9.00% over $225,000 |
| Over $275,000 but not over $325,000 | 10.00% | $20,966 plus 10.00% over $275,000 |
| Over $325,000 | 11.00% | $25,966 plus 11.00% over $325,000 |

### Tax year 2025 brackets -- Married filing jointly / Qualifying surviving spouse  _(HRS §235-51; DOTAX Tax Rate Schedule II)_

| Taxable income (DOTAX Schedule II wording) | Rate | Tax per the schedule |
| --- | --- | --- |
| Not over $19,200 | 1.40% | 1.40% of taxable income |
| Over $19,200 but not over $28,800 | 3.20% | $269 plus 3.20% over $19,200 |
| Over $28,800 but not over $38,400 | 5.50% | $576 plus 5.50% over $28,800 |
| Over $38,400 but not over $48,000 | 6.40% | $1,104 plus 6.40% over $38,400 |
| Over $48,000 but not over $72,000 | 6.80% | $1,718 plus 6.80% over $48,000 |
| Over $72,000 but not over $96,000 | 7.20% | $3,350 plus 7.20% over $72,000 |
| Over $96,000 but not over $250,000 | 7.60% | $5,078 plus 7.60% over $96,000 |
| Over $250,000 but not over $350,000 | 7.90% | $16,782 plus 7.90% over $250,000 |
| Over $350,000 but not over $450,000 | 8.25% | $24,682 plus 8.25% over $350,000 |
| Over $450,000 but not over $550,000 | 9.00% | $32,932 plus 9.00% over $450,000 |
| Over $550,000 but not over $650,000 | 10.00% | $41,932 plus 10.00% over $550,000 |
| Over $650,000 | 11.00% | $51,932 plus 11.00% over $650,000 |

The DOTAX schedule page notes that if taxable income is less than $100,000 the taxpayer must use the Tax Table; at or above $100,000, the rate schedule.

### Standard deduction (tax year 2025)  _(DOTAX tax-year-2025 information page: "the standard deduction amounts are the same as in tax year 2024")_

| Filing status | Standard deduction |
| --- | --- |
| Single | $4,400 |
| Married filing jointly | $8,800 |
| Married filing separately | $4,400 |
| Head of household | $6,424 |

### Personal exemptions (tax year 2025)

See Not yet confirmed below -- the exemption amounts were not extractable from the archived primary sources this run.

### Filing thresholds (tax year 2025)

See Not yet confirmed below -- the gross-income filing thresholds were not extractable from the archived primary sources this run.

## The taxable base

### Starting point

- **Starting point** -- Hawaii begins with federal adjusted gross income (AGI) from federal Form 1040, Line 11.

### Key additions to Hawaii income

- Interest on state/local obligations of other states
- Amounts deducted federally but not allowed by Hawaii

### Key subtractions from Hawaii income

- Social Security benefits (Hawaii does not tax Social Security -- see Not yet confirmed below for the statutory citation)
- Interest on U.S. government obligations (Treasury bonds, savings bonds)
- Military reserve/National Guard pay (limited exclusion)
- Certain pension income adjustments

### Resulting computation

- **Hawaii taxable income calculation** -- Federal AGI ± Hawaii modifications = Hawaii AGI → minus standard or itemized deductions → minus personal exemptions = Hawaii taxable income → apply rate schedule.

### Self-employed specific rules

- **QBI conformity** -- Hawaii starts from federal AGI. The federal QBI deduction (§199A) is below AGI and does NOT flow into Hawaii's computation.
- **SE health insurance deduction** -- Already reflected in federal AGI. Flows through to Hawaii automatically.
- **Retirement contributions (SEP, SIMPLE, solo 401(k))** -- Already reflected in federal AGI. No Hawaii add-back required.
- **Home office deduction** -- Already reflected in Schedule C → federal AGI. Flows through automatically.

### Tier 1 rules -- deterministic

| Rule ID | Rule |
| --- | --- |
| HI-IT-1.01 | Hawaii taxable income = Hawaii AGI − deduction − personal exemptions |
| HI-IT-1.02 | If taxable income is less than $100,000, use the tax table; at or above $100,000, use the rate schedule (DOTAX schedule page) |
| HI-IT-1.03 | Personal exemption: see Not yet confirmed below |
| HI-IT-1.04 | Social Security benefits are excluded from Hawaii income (statutory citation pending; see Not yet confirmed below) |
| HI-IT-1.05 | Filing deadline is April 20, 2026 (tax year 2025) -- DOTAX: "Taxpayers must file their income tax returns by April 20, 2026" |
| HI-IT-1.06 | Automatic 6-month extension if the properly estimated tax amount owed is paid by April 20, 2026 (DOTAX tax-year page) |
| HI-IT-1.07 | Hawaii does not conform to federal §168(k) bonus depreciation (see Not yet confirmed below) |
| HI-IT-1.08 | Hawaii allows credit for taxes paid to other states (see Not yet confirmed below) |

### Tier 2 rules -- requires judgment

| Rule ID | Rule | Judgment needed |
| --- | --- | --- |
| HI-IT-2.01 | Standard vs. itemized deduction election | Hawaii allows itemization independently of federal choice |
| HI-IT-2.02 | Depreciation conformity analysis | Determine add-back for federal bonus depreciation vs. Hawaii depreciation (see Not yet confirmed below) |
| HI-IT-2.03 | Part-year resident allocation | Prorate income for period of Hawaii residency |
| HI-IT-2.04 | GET vs. income tax interaction | Ensure GET is properly deducted on Schedule C, not double-counted |
| HI-IT-2.05 | Food/excise tax credit | Available to lower-income residents; verify eligibility |
| HI-IT-2.06 | Refundable food/excise tax credit | See Not yet confirmed below |

### Supplier pattern library

| Pattern on bank statement | Likely meaning |
| --- | --- |
| STATE OF HI TAX | Hawaii income tax payment |
| HAWAII DOTAX | Hawaii Department of Taxation payment |
| HI TAX REFUND | Hawaii income tax refund |
| HITAX PMT | Hawaii estimated tax payment |

## Deadlines and filing

- **Filing deadline** -- Taxpayers must file their tax year 2025 income tax returns by **April 20, 2026** (DOTAX tax-year-2025 information page: "Taxpayers must file their income tax returns by April 20, 2026. Although the law requires taxpayers to file by April 20, taxpayers are granted an automatic 6-month extension (no form is required to request the extension)"). The 6-month extension is granted if the taxpayer is due a refund, or pays the properly estimated tax amount owed by April 20, 2026.
- **Quarterly estimated payment requirement** -- Self-employed individuals must make quarterly estimated payments if they expect to owe $500 or more: HRS §235-97 provides that "In the case of a taxpayer whose tax liability is less than $500, the filing of an estimate and the payment of estimated tax shall not be required."
- **Voucher due dates** -- HRS §235-97 (archived text): the calendar-year first payment voucher "shall be filed, in the case of taxpayers on the calendar year basis, on or before April 20"; "Thereafter, on the twentieth day of June and September, the taxpayer shall transmit with the payment voucher, payment of one-quarter of the estimated tax"; and "The fourth quarter payment of the estimated tax shall be transmitted with the payment voucher by January 20 of the year following the taxable year for which the estimate was made."
- **GET interaction** -- Hawaii self-employed individuals are also subject to GET on gross business income (see `hi-sales-tax` for the confirmed GET rates). GET is NOT the same as income tax. GET paid is a deductible business expense on federal Schedule C, reducing federal AGI and therefore Hawaii taxable income.

### Form mapping

| Hawaii Form | Federal equivalent / Input |
| --- | --- |
| Form N-11, Line 10 | Federal Form 1040, Line 11 (AGI) |
| Form N-11, Lines 11–17 | Hawaii modifications (additions/subtractions) |
| Form N-11, Line 22 | Hawaii AGI |
| Form N-11, Line 24 | Standard or itemized deductions |
| Form N-11, Line 25 | Personal exemptions |
| Form N-11, Line 26 | Hawaii taxable income |
| Form N-11, Line 27 | Tax from table or schedule (the archived DOTAX schedule page keys Schedule I to "Form N-11, Line 26") |
| Form N-1 | Quarterly estimated payments |
| Form N-210 | Underpayment of estimated tax penalty |

### IRC conformity notes

- Hawaii generally conforms to the Internal Revenue Code as of a specific date; Hawaii has its own depreciation rules and may not conform to all federal provisions (see Not yet confirmed below for the conformity date and the §168(k) treatment).

## Penalties and interest

Penalties and interest for income tax follow HRS §231-39 (see `hi-corporate-income-tax` for the confirmed §231-39 amounts: failure-to-file 5%/month capped at 25%; negligence up to 25%; fraud up to 50%; late payment after timely filing up to 20%; interest at two-thirds of one per cent a month), applied through the ch. 235 assessment machinery.

## Cross-border points

- Part-year and nonresident individuals file Form N-15 instead of the N-11; the archived DOTAX rate schedules are stated for both "Form N-11, Line 26 or Form N-15, line 43".
- Residents are taxed on entire income regardless of source; nonresidents only on Hawaii-source income (HRS §235-4; see `hi-cross-border` for the confirmed residency-scope rules).

## Worked examples

### Example 1: single filer, Hawaii taxable income $50,000 (hypothetical client facts)

```oa-check
name: HI single filer 50k TY2025
inputs:
  income: 50000
steps:
  - b1: min(income, 9600) * 0.014
  - b2: (min(income, 14400) - 9600) * 0.032
  - b3: (min(income, 19200) - 14400) * 0.055
  - b4: (min(income, 24000) - 19200) * 0.064
  - b5: (min(income, 36000) - 24000) * 0.068
  - b6: (income - 36000) * 0.072
  - tax: b1 + b2 + b3 + b4 + b5 + b6
expected:
  b1: 134.40
  b2: 153.60
  b3: 264.00
  b4: 307.20
  b5: 816.00
  b6: 1008.00
  tax: 2683.20
```

(Brackets and rates are the confirmed Schedule I table above; the income is hypothetical.)

### Example 2: married filing jointly, Hawaii taxable income $300,000 (hypothetical client facts)

```oa-check
name: HI MFJ 300k TY2025
inputs:
  income: 300000
steps:
  - base: 16782.00
  - excess: income - 250000
  - tax: base + excess * 0.079
expected:
  excess: 50000.00
  tax: 20732.00
```

(Uses the confirmed Schedule II line "Over $250,000 but not over $350,000 $ 16,782 plus 7.90% over $250,000" from the archived DOTAX schedule page; the $300,000 income is hypothetical.)

## Ask the client first

1. Filing status and which rate schedule applies (Schedule I vs Schedule II)?
2. Any Hawaii modifications -- out-of-state municipal bond interest, U.S. government interest, Social Security, pension exclusions?
3. GET paid on gross business receipts -- is it deducted once on Schedule C and not double-counted?
4. Estimated payments and withholding so far -- is the $500 estimated-tax test met?
5. Part-year or nonresident status during the year -- should this be Form N-15 instead of N-11?

## Sources

| Source | URL | Read on |
|---|---|---|
| HRS §235-51 (tax imposed on individuals; rates) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0051.htm | 2026-10-28 |
| HRS §235-97 (estimated tax; $500 threshold; installment dates) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0097.htm | 2026-10-28 |
| DOTAX Tax Rate Schedules for taxable years beginning after Dec 31, 2025 (Schedules I & II; $100,000 tax-table rule) | https://tax.hawaii.gov/forms/d_25table-on/d_25table-on_p13/ | 2026-10-28 |
| DOTAX Tax Year 2025 Information (April 20, 2026 deadline; 6-month extension; standard deductions) | https://tax.hawaii.gov/tax-year-information/ | 2026-10-28 |
| HRS §231-39 (penalties; ⅔%/month interest) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm | 2026-10-28 |
| HRS §235-4 (residents/nonresidents scope) | https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0004.htm | 2026-10-28 |

Not yet confirmed: the personal-exemption and dependent-exemption amounts for tax year 2025 (v0.2 listed $1,144 each -- not extractable from the archived DOTAX pages this run); the gross-income filing thresholds by filing status (v0.2 listed $5,544/$6,688/$11,088/$12,232/$7,568); the refundable food/excise tax credit amount per exemption and its AGI cap (v0.2 listed $110 per exemption at federal AGI ≤ $50,000); the statutory citation for the Social Security exclusion; the IRC conformity date and the treatment of federal §168(k) bonus depreciation; the credit for taxes paid to other states; the current Hawaii minimum-wage figure used elsewhere in the pack; and the exact N-11 due-date and extension wording for tax years after 2025. None of these figures is asserted in the body because none could be tied to an archived primary source this run.

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
