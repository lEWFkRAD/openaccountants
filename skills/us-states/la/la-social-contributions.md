---
name: la-social-contributions
description: >
  Use this skill whenever asked about Louisiana employer social
  contributions for tax year 2026 -- unemployment insurance (UI)
  contributions administered by the Louisiana Workforce Commission (LWC)
  under La. R.S. 23:1601 et seq., the UI-only nature of Louisiana employer
  social cost (no state disability, no paid-family-leave, no state health
  mandate), and interaction with federal FUTA. Trigger on "Louisiana
  unemployment insurance", "LA UI rate", "LWC employer contributions",
  "R.S. 23:1601", "LaWage UI". Source-cited draft; wage base and rate
  ranges not confirmed (lwc.org 403 to plain HTTP this run).
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

# Louisiana social contributions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-28. Louisiana has **no state social insurance beyond unemployment insurance**: no state disability insurance, no paid family and medical leave program, no individual health-coverage mandate. Employer social cost above federal FICA/FUTA is **UI contributions only**, administered by the **Louisiana Workforce Commission (LWC)** -- a separate agency from LDR (unlike Kansas, where UI sits inside the revenue department). **Source status:** lwc.org returned **403 Forbidden to plain HTTP** on 2026-10-28 (bot-blocked), and La. R.S. 23 sits behind the session-state legislature site, so the **taxable wage base, contribution-rate ranges, and quarterly calendar are not confirmed**.

## Rates, bands and thresholds

- **Covered employers**: employers paying Louisiana wages meeting the statutory coverage tests must register with LWC, report quarterly wages, and pay contributions (structural; registration runs through the LaCOSA24/7 portal -- portal name **not confirmed**).
- **Successor and affiliated-group aggregation** for experience rating -- **not confirmed**.
- **Employee side**: no employee UI premium in Louisiana -- employer-only (structural, low risk).
- **Federal layer**: FUTA is a federal tax outside this pack -- see the federal skill for rates and credit mechanics; Louisiana's credit-reduction status for 2026 is not confirmed.

## The taxable base

| Item | Rule | Source status |
|---|---|---|
| UI taxable wage base | per-employee annual base | **not confirmed** -- lwc.org 403 |
| Employer contribution rate | experience-rated schedule with min/max bounds | **not confirmed** |
| New-employer rate | fixed statutory rate for first years | **not confirmed** |
| Employee share | none | structural, low risk |
| Solvency surcharge | years of federal loan balance historically added surcharges | **not confirmed** |

## Deadlines and filing

- Quarterly UI wage-and-contribution reports: last day of the month following each calendar quarter (standard UI calendar) -- **not confirmed** for the 2026 LWC calendar.
- Annual contribution-rate notices issue each year for the following rate year -- protest windows and the rate-year start date **not confirmed**.
- Quarterly wage reports also feed the LaCOSA24/7 system -- portal mechanics **not confirmed**.

## Penalties and interest

- Late reports/contributions: penalty plus interest under R.S. 23:1631 et seq. -- percentages **not confirmed**.
- Worker-misclassification exposure: LWC audits employer classifications; back-contributions plus penalties -- tiers **not confirmed**.

## Cross-border points

- Multi-state employers: Louisiana base/rate apply to Louisiana wages; bases differ by state.
- Remote workers: localization-of-work tests determine which state's UI covers the wages -- Louisiana adoption citation **not confirmed**.
- No state-level portability issues for Social Security/Medicare -- federal only.

## Worked examples

**Example 1 -- single-employee UI cost (hypothetical base/rate -- not confirmed against LWC):** one employee, $120,000 annual Louisiana wages, assumed base $9,000, assumed experience rate 2.7%.

```oa-check
name: LA UI employer contribution (hypothetical base/rate)
inputs:
  wages: 120000
  base: 9000
  rate: 0.027
steps:
  - taxable: min(wages, base)
  - ui: taxable * rate
expected:
  taxable: 9000
  ui: 243
```

**Example 2 -- three-employee small employer:** same hypothetical parameters, three employees.

```oa-check
name: LA UI three employees
inputs:
  per_employee_ui: 243
  employees: 3
steps:
  - total: per_employee_ui * employees
expected:
  total: 729
```

## Ask the client first

- Louisiana payroll footprint and headcount; which states' bases apply.
- Experience-rating history, successor ownership, rate-notice protests.
- Worker classification posture (W-2 vs 1099) -- LWC audit exposure.
- FUTA credit-reduction status affecting 2026 federal cost.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| LDR Withholding page (confirms income-tax withholding sits with LDR, separate from LWC UI) | https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/ | 2026-10-28 |

Not yet confirmed: the 2026 UI taxable wage base, contribution-rate schedule and new-employer rate, quarterly due dates, the January 1 rate-year start and protest windows for annual contribution-rate notices, penalty/interest percentages, FUTA credit-reduction status, and LaCOSA24/7 portal mechanics -- lwc.org returned 403 Forbidden to plain HTTP on 2026-10-28 and La. R.S. 23 sits behind the session-state legislature site, so no primary UI source could be archived this run.

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
