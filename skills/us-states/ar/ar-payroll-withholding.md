---
name: ar-payroll-withholding
description: >
  Use this skill whenever asked about Arkansas payroll withholding
  for tax year 2026 — the DFA Withholding Tax Branch, the 2026
  formula-method withholding tables and the employee certificate
  (AR W4EC), corporate (Sub-S) withholding, the pass-through entity
  (PET) withholding regime, composite filing for non-resident
  members, the AR3MAR annual reconciliation, W-2/1099 transmittals
  and ATAP e-filing. Trigger on "Arkansas withholding", "Arkansas
  withholding formula", "Arkansas Sub-S withholding", "Arkansas
  pass-through entity tax withholding", "Arkansas composite
  filing", "Arkansas AR3MAR", "Arkansas ATAP".
jurisdiction: US-AR
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.2"
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - ar-income-tax
---

# Arkansas payroll withholding, tax year 2026

> **Source-cited draft.** Built from the DFA Withholding Tax Branch page, the DFA 2026 Withholding Tax Formula and the DFA Corporation Income Tax page, read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Arkansas professional.

Arkansas withholding is run by the DFA **Withholding Tax Branch**. The branch covers individual wage withholding (the AR W-4 employee certificate and the withholding tables/formula), **Corporate (Sub-S) Withholding**, **Pass-Through Tax Withholding** and the **Pass-Through Entity Tax** program, and **Composite Filing** for non-resident members; filing and payment run through **ATAP** (Arkansas Taxpayer Access Point) ([DFA Withholding Tax Branch page](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/)).

## Who this applies to

- **Employers** paying Arkansas-source wages withhold individual income tax. Employees give a withholding certificate (Form AR W4EC) to set allowances. Employers with electronic systems may compute withholding with DFA's formula method rather than the tables ([2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf)).
- **S corporations** withhold on distributions to non-resident members under the Corporate (Sub-S) Withholding program (program listed on the DFA Corporation Income Tax and Withholding Tax Branch pages).
- **Partnerships/LLCs** participate in the Pass-Through Entity Tax (PET) or withhold on non-electing/non-resident members' distributions under Pass-Through Tax Withholding, and may cover non-resident members with a **composite return** instead of individual returns (programs listed on the DFA pages; see `ar-corporate-income-tax`).
- Every employer that pays wages subject to Arkansas withholding is a withholding agent for the individual income tax; the mechanics of the individual return are in `ar-income-tax`.

## Rates, bands and thresholds

The formula method, effective 01/01/2026 ([2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf)):

1. Multiply the period gross pay by the number of pay periods per year (12 monthly, 24 semi-monthly, 26 bi-weekly, 52 weekly, 260 daily).
2. Subtract the standard deduction of $2,470 to arrive at net taxable income.
3. Compute the annual gross tax from the bracket (the 2026 individual rates; the same brackets as `ar-income-tax`):

| From | Less than or equal to | Percentage | Minus adjustment |
|---|---|---|---|
| $0 | $5,599 | 0.00% | — |
| $5,600 | $11,199 | 2.00% | $111.98 |
| $11,200 | $15,999 | 3.00% | $223.97 |
| $16,000 | $26,399 | 3.40% | $287.97 |
| $26,400 | $94,700 | 3.70% | $367.16 |

From $94,701 the formula applies the bracket adjustment amounts ($369.90 at $94,701–$94,800, falling by $10 per $100 band), ending at a flat 3.7% minus $79.90 for income of $97,601 and over — the same shape as the Act 2 of 2026 rate tables in `ar-income-tax`. Employers using the printed withholding tables must read the tax from the table, not the formula.

| Item | Value | Tax year | Source |
|---|---|---|---|
| Standard deduction used in the formula | $2,470 | 2026 | [2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| Top individual rate applied | 3.7% (from $26,400) | 2026 | [2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf) |
| Sub-S withholding rate | see Not yet confirmed | 2026 | — |
| PET withholding rate | see Not yet confirmed | 2026 | — |
| Deposit frequency tiers | see Not yet confirmed | 2026 | — |

## The taxable base

- **Individual wage withholding:** the formula annualizes period gross pay, subtracts the $2,470 standard deduction, applies the bracket, and divides the annual tax back by the pay periods. Below $100,001 of net taxable income the tax is read at the $50-range midpoint; at $100,001 and over the exact dollar figure is used ([2026 withholding formula](https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf)).
- The formula brackets are the individual income tax brackets of Act 2 of the 2026 First Extraordinary Session (0% / 2% / 3% / 3.4% / 3.7% with a top marginal rate of 3.7%) — see `ar-income-tax` for the full rate tables, the personal tax credits ($29 / $58) and the low-income tables.
- **Sub-S withholding and pass-through withholding** operate on distributions to non-resident members; the programs are administered by the Withholding Tax Branch and the Corporation Income Tax Section (DFA pages). Their rates and the deposit schedule are on the program forms — see Not yet confirmed.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| W-2s with Form ARW-3 (transmittal) and 1099 state copies with federal transmittal 1096 | "by January 31st" | [DFA Withholding Tax Branch page](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/) |
| Annual reconciliation, Form AR3MAR | "due by February 28th" | [DFA Withholding Tax Branch page](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/) |
| Withholding deposits (AR 1000-WE family) | per the branch's due-dates schedule (see Not yet confirmed) | [DFA Withholding Tax Branch page](https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/) |

Withholding payments and filings run through ATAP; the branch also publishes bulk W-2/1099 file upload options (DFA Withholding Tax Branch page).

## Penalties and interest

- Withholding failures draw the Arkansas penalty and interest provisions (ACA §26-18-208; the DFA Corporate FAQs confirm "failure to pay penalties at 5% per month" and interest of 10% per annum for corporation income tax, and the same title-26 procedure provisions govern withholding). The specific withholding-penalty percentages are on the AR 1000-WE instructions — see Not yet confirmed.
- Common failure modes: (1) S-corp distributions paid without Sub-S withholding; (2) non-resident members filing nothing because the entity never withheld or filed composite; (3) missing the January 31 W-2/ARW-3 and February 28 AR3MAR deadlines.

## Cross-border points

- **Non-resident members** of an Arkansas entity: the entity withholds (Pass-Through Tax Withholding), elects the PET, or files a composite return — the three programs are alternatives for the same non-resident member income (DFA Corporation Income Tax and Withholding Tax Branch pages).
- **Out-of-state employers** with Arkansas employees register for an Arkansas withholding account and remit through ATAP.
- The individual income tax side of part-year/nonresident wages (proration, AR1000NR) is in `ar-income-tax`.

## Worked examples

**Example 1: monthly wage withholding, 2026 formula (hypothetical facts).** An employee is paid $6,000 a month (annual gross $72,000) with no low-income or status adjustments. Net taxable income = $72,000 − $2,470 = $69,530. The $26,400–$94,700 bracket applies: $69,530 × 3.7% − $367.16 = $2,205.45 for the year, or $183.79 a month.

```oa-check
name: AR 2026 monthly withholding, 6,000 gross (hypothetical facts, confirmed formula)
inputs:
  monthly_gross: 6000
  standard_deduction: 2470
steps:
  - annual_gross: monthly_gross * 12
  - nti: annual_gross - standard_deduction
  - annual_tax: nti * 0.037 - 367.16
  - monthly_withholding: annual_tax / 12
expected:
  nti: 69530
  annual_tax: 2205.45
  monthly_withholding: 183.79
```

**Example 2: employer filing volume (hypothetical facts).** An employer making 12 monthly withholding deposits plus the AR3MAR annual reconciliation and the ARW-3 transmittal:

```oa-check
name: AR withholding filing volume (hypothetical facts)
inputs:
  months: 12
  annual_reconciliations: 1
  transmittals: 1
steps:
  - filings: months + annual_reconciliations + transmittals
expected:
  filings: 14.00
```

## Ask the client first

- Are S-corp distributions to non-resident members running through Sub-S withholding (or the PET election) consistently?
- Which of PET / pass-through withholding / composite filing covers each non-resident member?
- Are the printed withholding tables or the formula method in use, and is the payroll system on the 2026 formula?
- Were last year's W-2s/ARW-3 sent by January 31 and the AR3MAR by February 28?
- Is the employer paying through ATAP, and above the EFT threshold (see `ar-corporate-income-tax`)?

## Sources

| Source | URL | Read on |
|---|---|---|
| DFA, Withholding Tax Branch (programs, ARW-3/AR3MAR deadlines, ATAP, bulk uploads) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/withholding-tax-branch/ | 2026-10-28 |
| DFA, Withholding Tax Formula Method, effective 01/01/2026 | https://www.dfa.arkansas.gov/wp-content/uploads/Withholding-Tax-Formula.pdf | 2026-10-28 |
| DFA, Corporation Income Tax (PET, Sub-S, composite program pages) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/ | 2026-10-28 |
| DFA, Corporate FAQs (penalty and interest provisions, EFT) | https://www.dfa.arkansas.gov/office/taxes/income-tax-administration/corporation-income-tax/corporate-faqs/ | 2026-10-28 |

Not yet confirmed: the Sub-S withholding rate and the PET withholding rate (the DFA pages list the programs but state no rates — pull the program forms before quoting); the withholding deposit frequency tiers and due dates (the branch's Due Dates page was not read); the withholding-specific penalty percentages on the AR 1000-WE instructions; whether Arkansas has withholding reciprocity with any neighboring state; the 2026 printed withholding tables themselves (only the formula method document was read).

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
