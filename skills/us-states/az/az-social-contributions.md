---
name: az-social-contributions
description: >
  Use this skill whenever asked about Arizona employer social
  contributions for tax year 2026 — Arizona unemployment insurance
  (UI) wage base and experience rates, the employer-only nature of AZ
  UI, workers' compensation insurance obligations, and how Arizona
  differs from states with state disability or paid-family-leave
  payroll taxes. Trigger on "Arizona unemployment insurance", "AZ UI
  rate", "Arizona SUTA", "Arizona employer taxes", "Arizona workers
  compensation requirement", "A-4 UI". Source-cited draft; DES pages
  unreachable this run, figures carried from az-payroll with
  needs-sources flags.
jurisdiction: US-AZ
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - az-payroll
---

# Arizona social contributions (UI, workers' comp overlay) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Arizona's state-level social contributions are narrow: employer-only unemployment insurance administered by the Department of Economic Security (DES), plus mandatory workers' compensation insurance (Title 23). Arizona has **no** state disability insurance, **no** paid family leave contribution, and **no** state retirement mandate for private employers — the employee side of payroll taxes is federal FICA plus the flat 2.5% income tax withholding (see `az-payroll`). **Source status:** des.az.gov and azdes.gov were unreachable from this workstation this run (repeated SSL handshake timeouts, 2026-10-27), so UI wage-base/rate figures are carried from the existing `az-payroll` skill (2025 schedule: wage base $8,000, rates 0.07%–15.6%) and flagged **needs-sources** for 2026; the Title 23 workers'-comp coverage statute text was not fetched and is **needs-sources**.

## 2. Who applies

- **UI:** employers meeting Arizona coverage tests (generally payroll in 20 or more weeks in a calendar year, or wages above the statutory threshold — exact current test: needs-sources) pay Arizona UI on covered wages. Out-of-state employers with Arizona employees are pulled in on the same basis as for withholding (see `az-payroll`).
- **Workers' compensation:** Arizona employers must carry workers' compensation insurance for employees (Title 23; statutory citation needs-sources this run); uninsured exposure includes the employee's election to sue without the usual defenses.
- **No employee-side state social contribution:** unlike NY (PFL/SDI) or WA (PFML), Arizona employees fund no state payroll social insurance.

## 3. Rates and base

| Item | Rate / base | Source |
|---|---|---|
| AZ UI taxable wage base (2025 carried) | $8,000 per employee per year | `az-payroll` (2025 schedule; 2026: **needs-sources** — DES unreachable 2026-10-27) |
| AZ UI employer experience rate (2025 carried) | 0.07% – 15.6% | `az-payroll` (2026 schedule: **needs-sources**) |
| New-employer UI rate | assigned rate (confirm current value) | **needs-sources** |
| UI surcharges/assessments | small employer assessments fund DES and job-training programs | **needs-sources** |
| Workers' comp premium | carrier-rated by class code; no state rate table | Title 23 (text needs-sources) |
| Employee-side state social contribution | none | absence confirmed against `az-payroll` scope; no DES contribution page fetched |

UI base: covered wages up to the annual wage base per employee; the rate is employer-specific (experience-rated). Workers' comp base: payroll by class code per the policy.

## 4. Deadlines

- UI quarterly contribution and wage reports (Form A-4 quarterly wage filing via DES eServices) — due the last day of the month following each quarter (mechanics carried from `az-payroll`; current DES due-date text: **needs-sources**).
- UI annual rate notices issue each year with an appeal window (confirm dates on the DES rate-notice page: **needs-sources**).
- Workers' comp: continuous coverage obligation; certificate of insurance on request (DES/ICC).

## 5. Penalties and interest

Late/unpaid UI contributions draw DES penalties and interest (current schedule: **needs-sources** — DES unreachable 2026-10-27). Common failure modes: (1) out-of-state employers assuming no AZ UI duty for remote Arizona employees; (2) treating workers' comp as optional for a single employee — it is not; (3) misclassifying workers, which shifts both UI wages and comp premium (7-factor test in `az-payroll`).

## 6. Cross-border interactions

Multi-state employers allocate Arizona UI wages to Arizona employment (localization-of-service rules; confirm current DES guidance: needs-sources). Reciprocal coverage agreements allow one-state UI coverage for employees working in several states (confirm AZ participation: needs-sources). Federal FUTA credit against Arizona UI is the standard $42/$5,600 pattern where the state is not a credit-reduction year (2026 status: **needs-sources**).

## 7. Worked examples

An employer with one Arizona employee at the carried $8,000 wage base and a 2.0% experience rate:

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

Same employer with 5 employees at the base:

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

## 8. Ask the client

- Do you have Arizona employees (including remote workers hired into Arizona)?
- Are you experience-rated or a new employer? Pull the current DES rate notice for the 2026 base and rate.
- Is workers' comp coverage in force for every employee, including family members on payroll?
- Any multi-state staffing that needs a UI localization or reciprocal-coverage election?

## Sources

1. `az-payroll` skill (this pack) — 2025 UI wage base $8,000, rates 0.07–15.6%, A-4 mechanics (carried; re-verify for 2026).
2. AZ DES — Unemployment Insurance hub: https://des.az.gov/services/employment/unemployment-insurance — **unreachable (SSL timeout) 2026-10-27**; re-read before relying on 2026 figures.
3. A.R.S. Title 23 (workers' compensation) — statute text not fetched this run: needs-sources.
