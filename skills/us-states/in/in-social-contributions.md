---
name: in-social-contributions
description: >
  Use this skill whenever asked about Indiana employer social contributions
  for tax year 2026 -- unemployment insurance (SUTA) under IC 22-4 with the
  Department of Workforce Development: taxable wage base, experience-rated
  employer rates, new-employer rate, quarterly contribution and wage
  reports, and the fact that Indiana has no state disability insurance and
  no employer health-coverage mandate. Trigger on "Indiana unemployment
  tax", "Indiana SUTA", "Indiana UI", "Indiana employer contributions",
  "IC 22-4", "Indiana DWD". Source-cited draft; DWD pages are a
  JavaScript SPA -- rate tables pending confirmation.
jurisdiction: US-IN
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - in-payroll
---

# Indiana social contributions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-27. Indiana's employer social-contribution layer is **unemployment insurance only** (IC 22-4, administered by the Department of Workforce Development). Indiana has **no state temporary-disability program and no state employer health-coverage mandate** (ACA only). **Source status:** in.gov/dwd pages are a JavaScript SPA returning no server-side text to plain HTTP (root 200, guessed sub-paths 404 this run) -- the wage base and rate ranges below are carried from the existing `in-payroll` skill (tier 2, drafted 2026-07-13) and are listed under Not yet confirmed below.

### Who applies

- Employers paying wages to individuals performing employment in Indiana (IC 22-4 coverage; the statutory tests are not yet confirmed -- statute text not machine-readable this run).
- **Employee contribution: none** -- UI is employer-funded (standard FUTA-credit structure; the IC 22-4 text is not yet confirmed).
- Worker classification: DWD applies Indiana's ABC test for UI purposes (cross-ref `in-payroll`, drafted 2026-10-27 from earlier sources).

## Rates, bands and thresholds

| Item | Value (from `in-payroll`, 2025 figures) | Source status |
|---|---|---|
| Taxable wage base | **$9,500** per employee per year  | confirm the 2026 base on the DWD notice -- see Not yet confirmed below |
| Experience rates | **0.50% – 7.40%**  | not yet confirmed |
| New-employer rate | **2.5%**  | not yet confirmed |
| Fund structure | employer contributions + federal credits  | not yet confirmed |

## The taxable base

The taxable base follows the mechanics described under Rates, bands and thresholds above.

## Deadlines and filing

- Quarterly contribution/wage reports (Form WH-34 series): due the last day of the month following each calendar quarter -- the published DWD calendar is not yet confirmed.
- Rate notices issue annually before the calendar year; protest windows follow the DWD notice -- not yet confirmed.

## Penalties and interest

- Late/unpaid contributions: interest and penalty under IC 22-4 -- percentages not yet confirmed.
- Successor liability and transfer provisions exist in IC 22-4 -- scope not yet confirmed.

## Cross-border points

- Remote workers physically working in Indiana create Indiana UI exposure for out-of-State employers; reciprocal coverage arrangements under the interstate UI agreement -- not yet confirmed.
- Reciprocal **income-tax** agreements (OH, KY, MI, PA, WI -- per `in-payroll`) do **not** extend to UI.

## Worked examples

Employer with 10 employees, all at the $9,500 base, experience rate 2.1%:

```oa-check
name: IN UI annual contribution
inputs:
  employees: 10
  wage_base: 9500
  rate: 0.021
steps:
  - taxable_payroll: employees * wage_base
  - contribution: taxable_payroll * rate
expected:
  taxable_payroll: 95000.00
  contribution: 1995.00
```

New employer, 4 hires, first-year rate 2.5%:

```oa-check
name: IN UI new employer first year
inputs:
  employees: 4
  wage_base: 9500
  new_rate: 0.025
steps:
  - contribution: employees * wage_base * new_rate
expected:
  contribution: 950.00
```

## Ask the client first

- Is the 2026 wage base/rate notice checked against payroll settings -- the base is small, so caps hit early in the year?
- Remote workers in Indiana: UI account registered?
- Acquisition of an Indiana business: successor UI account and experience-transfer election reviewed?
- ABC-test contractors: reclassification exposure on UI contributions?

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

## Sources

| Source | URL | Read on |
|---|---|---|
| Indiana Code IC 6 (title index incl. IC 22-4; iga.in.gov SPA -- no server-side text captured) | https://iga.in.gov/laws/2025/ic/titles/6 | 2026-10-28 |

Internal cross-reference: `in-payroll.md` (tier 2, 2026-07-13) -- UI figures originate there and require re-verification.

Not yet confirmed: the 2026 UI taxable wage base ($9,500 carried from `in-payroll`); the 0.50%–7.40% experience-rate range; the 2.5% new-employer rate; the IC 22-4 statutory coverage tests; the quarterly contribution/wage-report calendar and protest windows; IC 22-4 penalty and interest percentages; successor-liability scope; interstate UI agreement coverage.

<!-- openaccountants-cta-block -->

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