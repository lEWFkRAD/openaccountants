---
name: ia-income-tax
description: "Iowa Individual Income Tax Return (Form IA 1040) for sole proprietors and single-member LLCs. Covers the flat 3.8% rate, Iowa net income computation from federal AGI, the retirement-income and Social Security exclusions, filing thresholds, the QBI deduction line, and estimated tax. Trigger: taxpayer is an Iowa resident or has Iowa-source income."
version: "0.3"
jurisdiction: US-IA
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iowa individual income tax, tax year 2025

> **Source-cited draft.** Built from Iowa Code §§422.5 and 422.7 (Iowa Legislature, Iowa Code 2026) and the Iowa Department of Revenue's 2025 IA 1040 Expanded Instructions, read on 2026-10-28. No accountant has reviewed it. Do not file, pay, amend, or take a tax position from it without review by a qualified Iowa professional.

Authority: Iowa Department of Revenue (IDR). Currency: US dollars. Covers Form IA 1040 for self-employed individuals and sole proprietors. Iowa's individual income tax is a flat 3.8% — SF 2442 (2024) completed the transition to the flat rate for tax years beginning on or after January 1, 2025.

See also: `ia-cross-border`, `ia-payroll-withholding`, `ia-sales-tax`.

## Who this applies to

- Every Iowa resident and nonresident individual: "A tax is imposed upon every resident and nonresident of the state which tax shall be levied, collected, and paid annually upon and with respect to the entire taxable income ... at a rate of three and eight-tenths percent" (§422.5(1)(a)).
- Sole proprietors and single-member LLC owners file Form IA 1040 on their business results flowing through federal AGI.
- Nonresidents: tax computed by "multiplying this resulting amount by a fraction of which the nonresident's net income allocated to Iowa ... is the numerator and the nonresident's total net income computed under section 422.7 is the denominator" (§422.5(1)(b)(1)).

## Rates, bands and thresholds

| Item | Value (tax year 2025) | Source |
|---|---|---|
| Rate | 3.8% flat on all Iowa taxable income | §422.5(1)(a) |
| Exempt filing threshold, single / married filing separately | Iowa taxable income $9,000 or less ($24,000 if 65 or older) | 2025 IA 1040 instructions |
| Exempt filing threshold, married filing jointly / head of household / surviving spouse | $13,500 or less ($32,000 if 65 or older) | 2025 IA 1040 instructions |
| Personal exemption credit | $40 per exemption (nonrefundable) | 2025 IA 1040 instructions; §422.12 |

- Low-income exemption: a single filer is "exempt from Iowa tax" if "Iowa taxable income from all sources, IA 1040, line 4, is $9,000 or less"; the combined figure for joint filers is "$13,500 or less"; the 65-or-older figures are $24,000 and $32,000 (2025 IA 1040 instructions).
- Personal exemption credit: "Add the number of personal credits and multiply by $40" (2025 IA 1040 instructions).

## The taxable base

- **Starting point:** Iowa net income is computed from federal AGI with Iowa adjustments under §422.7, then reduced by the Iowa standard or itemized deduction (IA 1040, line 1d) and the qualified business income deduction (IA 1040, line 1e): "Line 1e: Qualified business income deduction. Enter the qualified business income deduction as reported on federal 1040, line 13a." (2025 IA 1040 instructions).
- **Social Security:** "Subtract, to the extent included, the amount of social security benefits taxable under section 86 of the Internal Revenue Code" (§422.7(8)).
- **Retirement income:** "Subtract, to the extent included, the total amount received from a governmental or other pension or retirement plan, including defined benefit or defined contribution plans, annuities, individual retirement accounts, ..." received by a person who is "(1) Disabled. (2) Fifty-five years of age or older. (3) The surviving spouse of an individual ... who would have qualified" (§422.7(19)(a)) — the exclusion is not capped at $6,000 under the archived 2026 statute text. (not yet confirmed)
- **Iowa capital gain deduction:** §422.7(21) excludes qualifying capital gains for a taxpayer "fifty-five years of age or older and who no longer materially participates in a farming business" and related qualifying property dispositions (§422.7(21)); the detailed eligibility conditions are listed under Not yet confirmed.
- **QBI:** Iowa adds back federal below-the-line deductions in computing net income and allows the federal QBI deduction as a separate Iowa line (§422.7(2); IA 1040 line 1e per the instructions).

## Deadlines and filing

- Filing/payment: for calendar-year 2025, pay and file by April 30, 2026; the instructions state "A federal extension does not apply for Iowa purposes. If at least 90% of your total tax liability is paid by April 30, 2026, you will automatically have until October 31, 2026, to file your return timely." (2025 IA 1040 instructions).
- Estimated tax (tax year 2025): required at the $200 threshold; "Starting with tax year 2026, the tax threshold for when an individual is required to make estimated tax payments has been raised from $200 to $1000." (2025 IA 1040 instructions). Calendar-year filers "are generally required to pay the tax in four installments with the first installment due by April 30" (2025 IA 1040 instructions).
- The statutory estimated-tax rule for all taxpayers is the $1,000 threshold with installments on the last day of the fourth, sixth, ninth, and first months (§422.16(12)); see Not yet confirmed for the reconciliation of the individual $200/$1,000 voucher rule with §422.16(12).

## Penalties and interest

- Underpayment of estimated tax and late-filing/late-payment penalties run under ch. 421/422 general provisions — the current percentages are listed under Not yet confirmed (the instructions reference the IA 2210 penalty computation).

## Cross-border points

- Part-year and nonresident allocation mechanics (the §422.8 allocation and the IA 1040NR) — see `ia-cross-border` and its Not yet confirmed items.
- Iowa wages of residents are subject to employer withholding under §422.16 (see `ia-payroll-withholding`).

## Worked examples

Hypothetical sole proprietor with $50,000 of Iowa taxable income after all adjustments and deductions:

```oa-check
name: IA flat tax 3.8 percent
inputs:
  taxable_income: 50000
  rate: 0.038
steps:
  - tax: taxable_income * rate
expected:
  tax: 1900.00
```

(Client facts are hypothetical; the 3.8% flat rate is the confirmed §422.5(1)(a) figure.)

Same filer claims two personal exemption credits:

```oa-check
name: IA personal exemption credits
inputs:
  credits: 2
  per_credit: 40
steps:
  - total_credit: credits * per_credit
expected:
  total_credit: 80.00
```

(The $40 personal exemption credit is the confirmed instructions figure.)

## Ask the client first

- Is all pension/retirement income excluded under §422.7(19) (taxpayer disabled, 55+, or a qualifying survivor)?
- Were estimated installments sized against the $200 (2025) / $1,000 (2026) individual threshold, and paid from April 30?
- Is at least 90% of the liability paid by April 30 to keep the automatic October 31 filing date?
- Sole proprietor: has the federal QBI deduction been entered on IA 1040 line 1e?

## Sources

| Source | URL | Read on |
|---|---|---|
| Iowa Code §422.5 (flat 3.8% tax imposed; nonresident proration) | https://www.legis.iowa.gov/docs/code/422.5.pdf | 2026-10-28 |
| Iowa Code §422.7 (net income adjustments; Social Security and retirement exclusions; capital gain deduction) | https://www.legis.iowa.gov/docs/code/422.7.pdf | 2026-10-28 |
| Iowa Code §422.12 (personal exemption credit) | https://www.legis.iowa.gov/docs/code/422.12.pdf | 2026-10-28 |
| Iowa Code §422.16 (estimated tax; due dates) | https://www.legis.iowa.gov/docs/code/422.16.pdf | 2026-10-28 |
| IDR 2025 IA 1040 Expanded Instructions (filing thresholds, $40 credit, extension, estimated tax) | https://revenue.iowa.gov/media/4435/download?inline= | 2026-10-28 |

Not yet confirmed: the Iowa standard deduction and itemized-deduction amounts for 2025 (the figures formerly stated here were not found in the archived sources' text layer); the safe-harbor percentages for avoiding underpayment penalties (90%/100%/110% of prior-year liability figures were not located in archived text); the historical 2024 bracket rates (4.4%-5.7%); the Iowa NOL computation rules (separate from federal); the reconciliation of the individual $200 (2025) estimated-tax voucher threshold with the §422.16(12) $1,000 rule; Schedule IA 126 and IA 1040C line mechanics; whether Iowa inheritance tax is repealed for deaths on or after January 1, 2025; the absence of local/city income taxes in Iowa; military retirement pay exclusion (beyond the general §422.7(19) retirement exclusion); the capital gain deduction's detailed holding-period and material-participation conditions.

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
