---
name: az-social-contributions
description: >
  Use this skill whenever asked about Arizona employer social
  contributions for tax year 2026 -- Arizona unemployment insurance
  (UI) wage base and experience rates, the employer-only nature of AZ
  UI, workers' compensation insurance obligations, and how Arizona
  differs from states with state disability or paid-family-leave
  payroll taxes. Trigger on "Arizona unemployment insurance", "AZ UI
  rate", "Arizona SUTA", "Arizona employer taxes", "Arizona workers
  compensation requirement", "A-4 UI". Source-cited draft; wage base
  tied to A.R.S. §23-622, rate mechanics to §23-730; DES pages
  unreachable from this workstation this run.
jurisdiction: US-AZ
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - az-payroll
---

# Arizona social contributions (UI, workers' comp overlay) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 28 October 2026. Arizona's state-level social contributions are narrow: employer-only unemployment insurance administered by the Department of Economic Security (DES), plus mandatory workers' compensation insurance (Title 23). Arizona has **no** state disability insurance, **no** paid family leave contribution, and **no** state retirement mandate for private employers -- the employee side of payroll taxes is federal FICA plus the flat 2.5% income tax withholding (see `az-payroll`). **Source status:** des.az.gov was unreachable from this workstation this run (403/SSL failures, 2026-10-28), so the UI wage base is tied to the statute text (A.R.S. §23-622) and the rate structure to A.R.S. §23-730; DES rate notices and the current rate range are on the Not yet confirmed line.

- **UI:** Arizona employers meeting the Employment Security coverage tests pay Arizona UI on covered wages (see `az-payroll` for the coverage tests; current test text on the Not yet confirmed line). Out-of-state employers with Arizona employees are pulled in on the same basis as for withholding (see `az-payroll`).
- **Workers' compensation:** Arizona employers must carry workers' compensation insurance for employees (Title 23; the statutory citation text was not fetched this run -- see the Not yet confirmed line); uninsured exposure includes the employee's election to sue without the usual defenses.
- **No employee-side state social contribution:** unlike NY (PFL/SDI) or WA (PFML), Arizona employees fund no state payroll social insurance.

## Rates, bands and thresholds

| Item | Rate / base | Source |
|---|---|---|
| AZ UI taxable wage base | $8,000 per employee per calendar year | A.R.S. §23-622(B)(1)(b) (read 2026-10-28): wages do not include the part of remuneration in excess of "$8,000 paid in the 2023 calendar year or in a calendar year thereafter to an individual by an employer or the employer's predecessor with respect to employment during the calendar year" |
| AZ UI employer experience rate | assigned by DES from the statutory reserve-ratio schedule | A.R.S. §23-730 (read 2026-10-28): contribution rates are determined from the employer's positive or negative reserve ratio per the statutory tables, with a required income rate adjustment from the fund-ratio schedule |
| Zero-reserve rate | two and seven-tenths per cent | A.R.S. §23-730 (read 2026-10-28): "If an employer's reserve equals zero, the employer's contribution rate for the ensuing calendar year shall be two and seven-tenths per cent, subject to the adjustments provided by this section" |
| New-employer UI rate | assigned by DES | on the Not yet confirmed line |
| UI surcharges/assessments | DES statutory adjustments | on the Not yet confirmed line |
| Workers' comp premium | carrier-rated by class code; no state rate table | Title 23 |
| Employee-side state social contribution | none | absence confirmed against `az-payroll` scope; no DES contribution page fetched |

UI base: covered wages up to the annual wage base per employee; the rate is employer-specific (experience-rated). Workers' comp base: payroll by class code per the policy.

## The taxable base

UI taxable wages are the first $8,000 of gross wages paid to each employee in a calendar year (A.R.S. §23-622, read 2026-10-28), with wages in excess of that base excluded for UI contribution purposes. The experience rating compares reserve surplus or deficit (contributions paid vs. benefits charged) to average annual taxable payroll (A.R.S. §23-730, read 2026-10-28). Workers' compensation premiums are computed by carriers on classification-code payroll, outside this tax base.

## Deadlines and filing

- UI quarterly contribution and wage reports -- due per the DES reporting schedule (mechanics carried from `az-payroll`; current DES due-date text on the Not yet confirmed line).
- UI annual rate notices issue each year with an appeal window (confirm dates on the DES rate-notice page -- Not yet confirmed).
- Workers' comp: continuous coverage obligation; certificate of insurance on request (DES/ICC).

## Penalties and interest

Late/unpaid UI contributions draw DES penalties and interest (current schedule on the Not yet confirmed line -- DES unreachable 2026-10-28). Common failure modes: (1) out-of-state employers assuming no AZ UI duty for remote Arizona employees; (2) treating workers' comp as optional for a single employee -- it is not; (3) misclassifying workers, which shifts both UI wages and comp premium (7-factor test in `az-payroll`).

## Cross-border points

Multi-state employers allocate Arizona UI wages to Arizona employment (localization-of-service rules carried from `az-payroll`; current DES guidance on the Not yet confirmed line). Reciprocal coverage agreements allow one-state UI coverage for employees working in several states (confirm AZ participation -- Not yet confirmed). Federal FUTA credit against Arizona UI follows the standard federal pattern where the state is not a credit-reduction year (2026 status on the Not yet confirmed line).

## Worked examples

An employer with one Arizona employee at the confirmed $8,000 wage base and a 2.0% experience rate (rate hypothetical -- the actual rate is on the DES rate notice):

```oa-check
name: AZ UI on one employee at wage base
inputs:
  base: 8000
  rate: 0.02
steps:
  - ui: base * rate
expected:
  ui: 160.00
```

Same employer with 5 employees at the base (hypothetical facts):

```oa-check
name: AZ UI five employees
inputs:
  base: 8000
  n: 5
  rate: 0.02
steps:
  - wages: base * n
  - ui: wages * rate
expected:
  wages: 40000.00
  ui: 800.00
```

## Ask the client first

- Do you have Arizona employees (including remote workers hired into Arizona)?
- Are you experience-rated or a new employer? Pull the current DES rate notice for the 2026 rate.
- Is workers' comp coverage in force for every employee, including family members on payroll?
- Any multi-state staffing that needs a UI localization or reciprocal-coverage election?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| A.R.S. §23-622 -- Wages (UI taxable wage base) | https://www.azleg.gov/ars/23/00622.htm | 2026-10-28 |
| A.R.S. §23-730 -- Variation and adjustment of contribution rates | https://www.azleg.gov/ars/23/00730.htm | 2026-10-28 |
| A.R.S. §23-750 -- Special provisions for nonprofits and governments | https://www.azleg.gov/ars/23/00750.htm | 2026-10-28 |
| `az-payroll` skill (this pack) -- coverage tests, A-4 mechanics (carried; re-verify for 2026) | (pack skill) | 2026-10-28 |

Not yet confirmed: the current-year UI experience-rate range and the new-employer rate (the earlier draft's carried range was not tied to a primary source); UI surcharges and assessments; the current coverage-test text; quarterly report due dates and DES penalties/interest schedule; reciprocal-coverage-agreement participation; 2026 FUTA credit-reduction status; the Title 23 workers'-comp coverage citation; the DES rate-notice appeal window.

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
