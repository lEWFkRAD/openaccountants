---
name: ms-payroll
description: >
  Use this skill whenever asked about Mississippi payroll withholding for
  2026 — mandatory electronic filing through the Taxpayer Access Point
  (TAP), the MCA § 27-3-83(4) penalty of $25 per return capped at $500
  for paper filing, the 10-or-more electronic mandate for W-2/1099
  filings, and withholding mechanics against the 2026 4% rate. Trigger on
  "Mississippi withholding", "TAP", "Mississippi W-2", "82-111",
  "Mississippi employer withholding". Source-cited draft; TAP mandate,
  § 27-3-83(4) penalty and the 10-return electronic threshold verified on
  DOR pages 2026-10-28, and the 3% casino gambling-winnings withholding
  from the archived MSDOR Form 80-100 2025 individual instructions.
jurisdiction: US-MS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.2
depends_on:
  - ms-income-tax
---

# Mississippi payroll withholding, tax year 2026

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## Who this applies to

Every employer paying Mississippi wages (residents and nonresidents working in Mississippi). Mississippi casinos withhold on gambling winnings (see Rates below). DOR withholding page: employers file and pay withholding through the Taxpayer Access Point (TAP); "Employers that issue 10 or more W-2s are required to electronically submit those to the DOR."

## Rates, bands and thresholds

- Withholding tracks the individual schedule — 2026: 4% on taxable income above the $10,000 zero-rate band (DOR Tax Rates page; see `ms-income-tax.md`).
- Gambling winnings: "Gambling winnings reported on a W-2G, 1099, or other informational return from Mississippi casinos are subject to a three percent (3%) non-refundable income tax. The casinos withhold the tax at the time of payment" (2025 Form 80-100 instructions).
- Paper-filing penalty: Miss. Code Ann. § 27-3-83(4) — $25 per return capped at $500 when paper is filed despite the electronic mandate (DOR withholding page, verified 2026-10-28).

## The taxable base

Wages, pensions, and Mississippi casino gambling winnings (3% withheld at source; "Gaming withholding cannot be claimed as a deduction on your tax return" — 2025 Form 80-100 instructions). DOR publishes withholding tax tables by pay period: "Daily Weekly Bi-Weekly Semi-Monthly Monthly" (DOR withholding page).

## Deadlines and filing

- Withholding returns and payments are filed and paid through TAP (DOR withholding page); bulk filers may use the FSET Fed/State program instead.
- W-2/1099 information returns: electronic submission required at 10 or more returns (DOR withholding page).
- Deposit-frequency thresholds (which employers deposit monthly vs more often): see Not yet confirmed.

## Penalties and interest

- **Electronic filing via TAP mandatory; paper penalty $25/return up to $500 (§ 27-3-83(4))** (DOR withholding page, verified 2026-10-28).
- "The taxpayer may be subject to penalties if they issue more than 10 W-2s and do not file as required" (DOR withholding page).
- Late-deposit penalty/interest percentages for withholding specifically: see Not yet confirmed.

## Cross-border points

Nonresident workers: Mississippi taxes wages for work performed in-state and withholding applies regardless of employee residence; nonresidents file Form 80-205 (see `ms-cross-border.md`). No reciprocity agreements located in the archived sources (see Not yet confirmed).

## Worked examples

**Example 1 — paper-filing penalty cap.** Employer files 30 W-2s on paper despite the mandate:

```oa-check
name: MS 27-3-83 penalty cap
inputs:
  returns: 30
  per_return: 25
  cap: 500
steps:
  - raw: returns * per_return
  - penalty: min(raw, cap)
expected:
  penalty: 500.00
```

**Example 2 — quarterly withholding at the 2026 rate.** Mississippi wages $200,000 in a quarter, flat 4% approximation (ignoring the zero-rate band):

```oa-check
name: MS quarterly withholding 4 percent
inputs:
  wages: 200000
  rate: 0.04
steps:
  - withheld: wages * rate
expected:
  withheld: 8000.00
```

## Ask the client first

- Is the payroll provider wired to TAP for withholding returns and W-2s?
- Count of information returns — over 10? electronic mandate applies (verified).
- Nonresident remote workers performing days in Mississippi?

## Sources

| Source | URL | Read on |
|---|---|---|
| DOR Withholding Tax — TAP filing/payment, 10-or-more W-2 electronic mandate, § 27-3-83(4) paper penalty, pay-period tax tables, FSET bulk filing | https://www.dor.ms.gov/business/withholding-tax | 2026-10-28 |
| MSDOR 2025 Individual Income Tax Instructions (Form 80-100, rev. 12/25) — 3% casino gambling withholding, gaming withholding not deductible | https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf | 2026-10-29 |
| DOR Tax Rates — 2026: 4% above the $10,000 zero-rate band | https://www.dor.ms.gov/general-information | 2026-10-28 |

Not yet confirmed: the withholding return form ID (82-111 is conventional but not verified on a fetched page); deposit-frequency thresholds; late-deposit penalty/interest percentages specific to withholding; reciprocity agreements.

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

