---
name: ny-social-contributions
description: >-
  Use when an employer or self-employed person needs the 2026 New York
  answer on state-level social contributions: Paid Family Leave employee
  payroll contribution (2025: 0.388% of gross wages, annual cap $354.53,
  NYSAWW $1,757.19 — verified on paidfamilyleave.ny.gov; 2026 figures
  pending publication), mandatory statutory disability insurance (SDI,
  employee 0.5% of wages up to $300/week, max $1.50/week, employer
  may pay — needs-sources this run), employer-only unemployment
  insurance, and the MCTMT payroll tax in the MCTD (cross-reference
  ny-mctmt). Trigger on NY PFL contribution, NY SDI, 0.388 percent,
  354.53, NYS-45, New York disability insurance.
  Source-cited draft; PFL figures verified 2026-10-25, SDI figures need
  official confirmation.
jurisdiction: US-NY
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# New York social contributions (PFL, SDI, UI, MCTMT overlay)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

Every NY employer (and out-of-state employers with NY employees) for **Paid Family Leave (PFL)** and **Statutory Disability Insurance (SDI)**; employers meeting the UI coverage tests for unemployment insurance; and employers/self-employed persons doing business in the Metropolitan Commuter Transportation District for **MCTMT** (covered in depth by the existing `ny-mctmt` skill — this skill only maps it as a social-contribution-adjacent payroll levy). New York is unusual: it has **both** an employee-side PFL contribution and a mandatory employee SDI contribution, plus employer-only UI and MCTMT.

## 2. Core rules and rates

- **PFL employee contribution (verified).** "For 2025, employees contribute 0.388% of their gross wages per pay period, with a maximum annual contribution of $354.53. Employees earning less than the current NYSAWW of $1,757.19 will contribute less than the annual cap." Commissions and bonuses are wages; contributions are employee-paid unless the employer elects to pay them; reported in W-2 Box 14 ("State disability insurance taxes withheld" convention). _(paidfamilyleave.ny.gov/cost, 200 with text, 2026-10-25. The page hosts 2026 and 2027 calculators but the 2026 rate/SAWW text: **needs-sources** — re-check the cost page when 2026 figures post.)_
- **PFL is not optional** for eligible employees; waiver only for employees regularly scheduled <20 hours/week who will not work 175 days in a year, or similarly limited part-timers. _(same source, verified 2026-10-25)_
- **SDI (statutory disability insurance).** Mandatory private/DBL coverage; the standard employee contribution is **0.5% of wages up to $300/week (max $1.50/week)** where the employer takes the employee share — the employer may instead pay the full premium. _(Wage Replacement Income Law / Workers' Compensation Law Art. 9; the official page could not be located on tax.ny.gov/dol.ny.gov/dfs.ny.gov on 2026-10-25 (multiple 404s, wftc.ny.gov DNS failure): **needs-sources** — confirm against the carrier policy and NYS-45 instructions before relying.)_
- **UI.** Employer-only; NY SUTA wage base and rates per the NYS-45 annual rate notice (2026 schedule: **needs-sources** this run).
- **MCTMT.** Employer payroll tax in the MCTD, quarterly brackets 0.11%–0.60% (Zone 1) / 0.34% (Zone 2) over the $312,500 quarterly floor — full treatment in `ny-mctmt` (rates carried there with statutory citations to Tax Law Art. 23 / Part Q Ch. 59 Laws of 2023).

## 3. Base and adjustments

- PFL base: gross wages per pay period (commissions/bonuses included), annual contribution capped at the published dollar cap; after-tax collection is the default (contributions may be taken from after-tax wages).
- SDI base: wages up to $300/week; the 0.5% is weekly, capped at $1.50/week.
- UI base: per-employee NY taxable wages up to the annual published base.
- MCTMT base: quarterly MCTD-allocated payroll above the zone floor (see `ny-mctmt`).
- PFL and SDI contributions are employee wage deductions — they reduce neither federal wages nor NY wages for income-tax purposes when taken pre-tax under the employer's plan design (confirm plan mechanics).

## 4. Deadlines

- PFL/SDI/UI: combined annual reconciliation and quarterly wage/contribution reporting on **Form NYS-45** (quarterly returns due the last day of the month following each quarter; annual return due January 31). _(NYS-45 mechanics carried from NY withholding practice; the NYS-45 instructions PDF returned 404 on 2026-10-25: **needs-sources** for the current-year due-date text.)_
- PFL contributions begin with the first pay period of the calendar year at the published rate; mid-year rate changes do not occur (annual rate set effective January 1).
- MCTMT quarterly (NYS-45) and self-employed MTA-6 estimates: see `ny-mctmt`.

## 5. Penalties and interest

- Late/unpaid PFL premiums expose the employer to a **penalty of up to $100 per employee** plus interest under the PFL scheme (carrier-administered; exact current penalty text: **needs-sources**).
- NYS-45 late filing/failure to pay: standard Tax Law Ch. 7 penalties and interest (exact 2026 percentages: **needs-sources**).
- Common failure mode: out-of-state employers with NY remote employees assuming no PFL duty — PFL follows the employment relationship (NY employment or employer's choice of NY coverage).

## 6. Cross-border and federal overlay

- PFL/SDI apply to NY employment regardless of the employee's residence; a NJ resident working for a NY employer is in PFL/SDI scope.
- PFL benefits are taxable-free at state level but the interaction with FMLA (unpaid) and workers' comp (occupational) must be sequenced — see paidfamilyleave.ny.gov "PFL and Other Benefits" (nav verified 2026-10-25).
- FICA/FUTA are federal (federal skills). PFL/SDI employee contributions are not deductible on the NY return as a separate credit line.
- MCTMT vs other states' payroll taxes: no reciprocity — MCTD is strictly the 12-county district (see `ny-mctmt`).

## 7. Worked examples

**Example 1 — PFL contribution cap.** Employee earning $120,000 in 2025: 0.388% uncapped would exceed the annual cap.

```oa-check
name: ny pfl cap 2025
inputs:
  wages: 120000
  rate: 0.00388
steps:
  - uncapped: wages * rate
  - cap: 354.53
  - contrib: min(uncapped, cap)
expected:
  uncapped: 465.60
  contrib: 354.53
```

**Example 2 — MCTMT Zone 1 quarterly bracket tax, $500,000 payroll.** Zone 1 brackets over the $312,500 floor (0.11% / 0.23% / 0.60% — carried from `ny-mctmt`).

```oa-check
name: ny mctmt zone1 500k quarter
inputs:
  payroll: 500000
steps:
  - t1: (min(payroll, 375000) - 312500) * 0.0011
  - t2: (min(payroll, 437500) - 375000) * 0.0023
  - t3: (payroll - 437500) * 0.006
  - mctmt: t1 + t2 + t3
expected:
  mctmt: 587.50
```

## 8. Ask the client first

1. Is the employment NY-covered for PFL/SDI (NY work location or NY employer election)?
2. Does the employer pay PFL/SDI premiums or deduct them from wages — is the plan documented?
3. Are W-2 Box 14 disclosures being made for PFL/SDI withheld amounts?
4. MCTD: where do employees actually perform services (zone determination)?
5. Are the 2026 PFL rate/cap and UI schedule picked up from the January notices before the first payroll?

## 9. Sources

- NY Paid Family Leave — Cost (2025 contribution 0.388%, cap $354.53, NYSAWW $1,757.19, waiver rules, W-2 Box 14): <https://paidfamilyleave.ny.gov/cost> — 200 with text, 2026-10-25.
- NY Paid Family Leave — root and "PFL and Other Benefits" nav: <https://paidfamilyleave.ny.gov/> — 200, 2026-10-25.
- Existing `ny-mctmt` skill (MCTMT brackets, zones, NYS-45/MTA-6, Ch. 59 Laws of 2023 citations) — read 2026-10-25.
- SDI contribution figures (0.5%, $300/week, $1.50/week): **needs-sources** — official DFS/DOL/WFTC pages 404 or DNS-failed on 2026-10-25.
- 2026 PFL rate/cap, 2026 UI schedule, NYS-45 instructions, PFL penalty text: **needs-sources**.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
