---
name: ms-cross-border
description: >
  Use this skill whenever asked about Mississippi cross-border individual
  taxation for 2026 -- nonresident taxation of Mississippi-source income,
  the 2026 4% rate environment for border workers, credit for taxes paid
  to other states for Mississippi residents working elsewhere, and the
  absence of local income tax. Trigger on "Mississippi nonresident",
  "80-205", "Mississippi credit for taxes paid", "Mississippi remote
  worker". Corrected 2026-10-29 against archived MSDOR Form 80-100
  2025 individual income tax instructions (Form 80-205 mechanics,
  credit-for-other-state-tax via Form 80-160, due dates, penalties) and
  the DOR tax-rates page (2025-2027 phase-down).
jurisdiction: US-MS
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.2
depends_on:
  - ms-income-tax
  - ms-payroll
---

# Mississippi cross-border taxation, tax year 2026

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## Who this applies to

- **Nonresidents and part-year residents with Mississippi-taxed income** file the Non-Resident/Part-Year Resident Return, Form 80-205: "You are considered a part-year resident and must file the NonResident/Part-Year Resident Return, Form 80-205. You will be taxed only on income earned while a resident of Mississippi and you will prorate your deductions and exemptions." (2025 Form 80-100 instructions)
- **Mississippi residents paying income tax to another state** take a credit (see Rates below).
- **Border workers** (e.g. Louisiana/Mississippi): coordinate both states' filings to avoid double taxation.

## Rates, bands and thresholds

DOR tax-rates page: "Tax Year 2025 Excess of $10,000 of Taxable Income is taxed @ 4.4% Tax Year 2026 Excess of $10,000 of Taxable Income is taxed @ 4% Tax Year 2027 Excess of $10,000 of Taxable Income is taxed @ 3.75%" -- with 0% on the first $10,000. Nonresidents file Form 80-205 and are taxed on the Mississippi-taxed share at that rate.

**Credit for taxes paid to another state:** "If you are a resident of Mississippi who earns income in another state and are required to pay an income tax to that other state, you are allowed to take a credit against your Mississippi income tax due in the same year for the total income tax due to the other state (subject to certain limitations)" -- claimed on line 18 with Form 80-160 and a copy of the other state return(s) attached (2025 Form 80-100 instructions). The credit is "not applicable on the Non-Resident Return".

## The taxable base

Part-year residents are "taxed only on income earned while a resident of Mississippi" with prorated deductions and exemptions (2025 Form 80-100 instructions). Residents working outside Mississippi "must file a Mississippi return" (2025 Form 80-100 instructions). Withholding applies to Mississippi wages regardless of employee residence (see `ms-payroll.md`).

## Deadlines and filing

"Calendar year returns must be filed no later than April 15th annually. Fiscal year returns must be filed no later than the 15th day of the 4th month following the end of the fiscal year" (2025 Form 80-100 instructions). If you will owe tax, Mississippi "will allow you the same time to file your return as allowed by federal. However, if you owe additional taxes, you must remit the tax due with Form 80-106, on or before the due date of the return" (2025 Form 80-100 instructions).

## Penalties and interest

"The penalty imposed for failure to pay the tax when due is 1/2% per month not to exceed 25% in the aggregate"; interest "is at the rate of 1/2% per month from the due date until paid" (2025 Form 80-100 instructions). Late filing: "The penalty imposed for failure to file a return is 5% per month not to exceed 25% in the aggregate... Such failure to file a return penalty shall not be less than $100.00" (2025 Form 80-100 instructions).

## Cross-border points

- Louisiana/Mississippi border workers: Louisiana nonresident filing may also apply for work in Louisiana (see the `la-income-tax` family) -- coordinate both states' filings to avoid double taxation.
- The other-state credit is claimed on the resident return only (Form 80-160); nonresidents file Form 80-205 and take no such credit.

## Worked examples

- How many workdays physically in Mississippi vs home state?
- Home state -- will it credit the Mississippi tax paid (avoid double tax)?
- Moving to/from Mississippi mid-year? (part-year split)

## Ask the client first

- How many workdays physically in Mississippi vs home state?
- Home state -- will it credit the Mississippi tax paid (avoid double tax)?
- Moving to/from Mississippi mid-year? (part-year split on Form 80-205)

## Sources

| Source | URL | Read on |
|---|---|---|
| MSDOR 2025 Individual Income Tax Instructions (Form 80-100, rev. 12/25) -- Form 80-205 part-year mechanics, other-state credit via Form 80-160, April 15 due date, Form 80-106 extension payment, penalties/interest | https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf | 2026-10-29 |
| DOR Tax Rates -- 2025/2026/2027 phase-down (4.4% / 4% / 3.75% above the $10,000 zero-rate band) | https://www.dor.ms.gov/general-information | 2026-10-28 |

Not yet confirmed: reciprocity agreements (none located in the archived sources); any convenience-of-the-employer rule for remote border workers; whether Mississippi levies any local income tax on individuals; exit-tax posture.

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
