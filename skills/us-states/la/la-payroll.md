---
name: la-payroll
description: >
  Use this skill whenever asked about Louisiana payroll withholding for
  tax year 2026 — Form L-1 quarterly withholding returns (zero returns
  required), Form L-3 annual reconciliation due January 31, mandatory
  e-filing through LaTAP/LaWage, and the verified payment-frequency bands
  (quarterly under $500, monthly $500-$5,000, semi-monthly $5,000+).
  Trigger on "Louisiana withholding", "L-1", "L-3", "LaTAP withholding",
  "LaWage", "LDR withholding". Source-cited draft; duty, forms, bands, and
  deadlines verified from the LDR Withholding page 2026-10-28; withholding
  table figures not confirmed.
jurisdiction: US-LA
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - la-income-tax
---

# Louisiana payroll withholding v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-28. Covers Louisiana income-tax withholding by employers. **Source status:** the LDR Withholding page (https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/) was fetched and its text verified 2026-10-28 — the **withholding duty, L-1/L-3 form designations, zero-return rule, payment-frequency bands, and the January 31 reconciliation deadline are verified quotes**. The **withholding table figures** (https://revenue.louisiana.gov/tax-professionals/general-resources/louisiana-withholding-tax-tables/) render via JS and are **not confirmed**.

## Rates, bands and thresholds

- **Every employer with resident or nonresident employees performing services in Louisiana** must withhold, unless specifically exempt, based on the employee's withholding certificate (verified).
- **Louisiana residents performing services in another state** may still be Louisiana-withheld **if those wages are not subject to income-tax withholding in the other state** (verified — this is Louisiana's answer to no-reciprocity, e.g. Texas employers don't withhold, so Louisiana residents working in TX get LA withholding from the TX employer).
- **Every employer who withholds or must withhold** files a **quarterly L-1 for every assigned period — even zero returns** (no employees, no LA wages, no tax due: still file; verified).

## The taxable base

| Item | Rule | Source status |
|---|---|---|
| Quarterly return | **Form L-1**, electronic filing mandatory (LaTAP or approved software) | verified |
| Zero returns | required every assigned period | verified |
| Payment frequency | average monthly withholding **<$500 → quarterly; $500–<$5,000 → monthly; ≥$5,000 → semi-monthly** | **verified table** |
| Annual reconciliation | **Form L-3**, due **January 31**, or 30 days after final wages if the business closes mid-year; file via LaWage | verified |
| Withholding computation | LDR withholding tables (percentage/flat methods) | **not confirmed** (JS page) |
| Amended returns | per affected quarter only; corrections can't cross quarters | verified |
| Account closure | must file final quarterly return + reconciliation and request closure; stopping filings doesn't close the account | verified |

## Deadlines and filing

- L-1 quarterly: assigned periods, electronic file + pay (calendar detail **not confirmed** — standard last-day-of-month-after-quarter).
- L-3 annual reconciliation: **January 31** following the calendar year close (verified).
- Notify LDR of name/address/responsible-party/ownership changes (verified duty).

## Penalties and interest

- Common-mistake list published by LDR: filing after due date, missing zero returns, missing e-payment deadlines (verified page; penalty percentages under R.S. 47:1607 **not confirmed**).
- Failure to withhold: employer liable for amounts that should have been withheld plus penalties — tiers **not confirmed**.

## Cross-border points

- **No reciprocity agreements** — the resident-in-another-state withholding rule (verified) is the mechanism: LA residents working in states that don't withhold (TX, WA, FL...) get LA withholding instead.
- Nonresidents working in Louisiana: withholding required like residents (verified duty).
- W-2 state-box reporting via LaWage e-file (verified channel).

## Worked examples

**Example 1 — payment-frequency band:** employer averages $4,800/month of Louisiana withholding. The bands (average monthly withholding <$500 → quarterly; $500–<$5,000 → monthly; ≥$5,000 → semi-monthly) are verified quotes from the LDR Withholding page (2026-10-28); the $4,800 figure is a hypothetical client fact.

```oa-check
name: LA withholding frequency band
inputs:
  avg_monthly: 4800
  band_q: 500
  band_m: 5000
steps:
  - over_quarterly_band: max(avg_monthly - band_q, 0)
  - under_monthly_band: max(band_m - avg_monthly, 0)
expected:
  over_quarterly_band: 4300
  under_monthly_band: 200
```

$4,800 is above the $500 quarterly ceiling and $200 below the $5,000 semi-monthly floor → **monthly** remitters (verified bands).

**Example 2 — annual remittance count by band:** a monthly-band employer files how many L-1 remittances per year vs a quarterly-band employer?

```oa-check
name: LA remittance counts
inputs:
  monthly_periods: 12
  quarterly_periods: 4
steps:
  - delta: monthly_periods - quarterly_periods
expected:
  delta: 8
```

Monthly band = 12 remittances, quarterly band = 4, plus one L-3 reconciliation each January 31 (verified).

## Ask the client first

- Average monthly withholding — which frequency band applies (bands reassign as payroll grows).
- LA-resident employees working in no-income-tax states — LA withholding required (verified rule).
- Zero-return discipline: dormant accounts still owe quarterly L-1s until formally closed (verified).
- LaTAP/LaWage e-file enrollment status — paper is not an option.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| LDR Withholding (duty, L-1, zero returns, payment-frequency bands, L-3, Jan 31, closure rule) | https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/ | 2026-10-28 |

Not yet confirmed: withholding table figures (the LDR withholding-tables page renders via JS and could not be archived); the exact quarterly due-date calendar; employer penalty/interest percentages under R.S. 47:1607 (the 12% annual underpayment-of-estimated-tax penalty under R.S. 47:118 is verified for individuals, not employers); the W-4-equivalent certificate form ID (LW-4).

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
