---
name: fl-social-contributions
description: >
  Use this skill whenever asked about Florida employer social
  contributions for tax year 2026 — Florida reemployment (unemployment)
  tax under Ch. 443 Fla. Stat., the employer-only nature of FL
  reemployment tax, mandatory workers' compensation insurance under
  Ch. 440, and how Florida has no state disability, paid-family-leave,
  or retirement contribution on payroll. Trigger on "Florida
  reemployment tax", "Florida SUTA", "FL UI rate", "Florida employer
  taxes", "Florida workers compensation requirement", "RT-6".
  Source-cited draft; Ch. 440 text read 2026-10-27, Ch. 443 rate
  schedule pages unreachable this run (needs-sources flags).
jurisdiction: US-FL
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - fl-corporate-income-tax
---

# Florida social contributions (reemployment tax + workers' comp overlay) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Florida's state-level social contributions are narrow: employer-only reemployment (unemployment) tax administered by the Department of Commerce under Ch. 443, Fla. Stat., plus mandatory workers' compensation insurance under Ch. 440, Fla. Stat. Florida has **no** individual income tax, so there is no state withholding on payroll (see the pack README), **no** state disability insurance, **no** paid family leave contribution, and **no** state retirement mandate for private employers. **Source status:** s. 440.04 Fla. Stat. text read 2026-10-27 (200, flsenate.gov); the Ch. 443 rate-schedule pages on floridajobs.org did not resolve from this workstation this run, so the 2026 wage base, rate ranges, and new-employer rate are flagged **needs-sources**; the F-2220 reemployment return form PDF was verified 2026-10-27.

## 2. Who applies

- **Reemployment tax:** employers meeting Florida coverage tests (generally payroll in each of 20 or more weeks in a calendar year, or covered wages above the statutory threshold — exact current test: **needs-sources**) pay Florida reemployment tax on covered wages. Out-of-state employers with Florida employees are pulled in on the same basis.
- **Workers' compensation:** most Florida employers must carry workers' compensation insurance — the Ch. 440 coverage obligation is continuous; construction employers need coverage for even one employee, other industries generally at four or more employees (current thresholds: confirm against Ch. 440 text; s. 440.04 waiver mechanics verified 2026-10-27).
- **No employee-side state social contribution:** unlike NY (PFL/SDI) or WA (PFML), Florida employees fund no state payroll social insurance; the employee side is federal FICA only.

## 3. Rates and base

| Item | Rate / base | Source |
|---|---|---|
| FL reemployment taxable wage base (2026) | **needs-sources** (floridajobs.org unreachable 2026-10-27; recent-year base has been in the $7,000–$8,700 range — confirm) | Reemployment Tax Act, Ch. 443, F.S. |
| FL reemployment experience rate range | **needs-sources** (confirm current min/max on the 2026 rate notice) | Ch. 443, F.S. |
| New-employer assigned rate | **needs-sources** | Ch. 443, F.S. |
| Employee contribution to FL reemployment tax | none — employer-only | Ch. 443 structure (verified absence; no employee contribution page exists) |
| Workers' comp premium | carrier-rated by class code; no state rate table | Ch. 440, F.S. (s. 440.04 text read 2026-10-27) |
| State disability / paid family leave | none | absence confirmed; no such program in F.S. Ch. 443/440 scope |

Reemployment tax base: covered wages up to the annual wage base per employee; the rate is employer-specific (experience-rated, with reserve-ratio and solvency adjustments). Workers' comp base: payroll by class code per the policy.

## 4. Deadlines

- Quarterly reemployment tax return and wage report (Form RT-6) — due the last day of the month following each quarter (1/31, 4/30, 7/31, 10/31 pattern; confirm current dates on floridajobs.org: **needs-sources**).
- Annual rate notices issue each December/January with an appeal window (confirm: **needs-sources**).
- Workers' compensation: continuous coverage obligation; certificate of insurance on request; construction certificates verified through the DBPR system.

## 5. Penalties and interest

Late/unpaid reemployment contributions draw penalties and interest under Ch. 443 (current schedule: **needs-sources** — rate pages unreachable 2026-10-27). Common failure modes: (1) out-of-state employers assuming no FL reemployment duty for remote Florida employees; (2) treating workers' comp as optional for a small crew — construction requires it from the first employee; (3) misclassifying workers as contractors, which shifts both reemployment wages and comp premium.

## 6. Cross-border interactions

Multi-state employers allocate Florida reemployment wages to Florida employment under the localization-of-service rules (confirm current DEO guidance: **needs-sources**). Reciprocal coverage agreements allow one-state UI coverage for employees working in several states (confirm FL participation: **needs-sources**). Federal FUTA credit against Florida reemployment tax follows the standard $42/$5,600 pattern where the state is not a credit-reduction year (2026 status: **needs-sources**).

## 7. Worked examples

An employer with one Florida employee at an assumed $8,000 wage base and a 2.7% new-employer rate (illustrative — confirm both figures against the 2026 rate notice):

```oa-check
name: FL reemployment tax on one employee (illustrative base)
inputs:
  base: 8000
  rate: 0.027
steps:
  - tax: base * rate
expected:
  tax: 216.00
```

Same employer with 4 employees at the same base and rate:

```oa-check
name: FL reemployment tax four employees (illustrative)
inputs:
  base: 8000
  n: 4
  rate: 0.027
steps:
  - wages: base * n
  - tax: wages * rate
expected:
  wages: 32000.00
  tax: 864.00
```

## 8. Ask the client

- Do you have Florida employees (including remote workers hired into Florida)?
- Are you experience-rated or a new employer? Pull the current 2026 rate notice for the wage base and rate.
- Is workers' compensation coverage in place for every crew, including construction work from the first employee?
- Are workers correctly classified — employee vs contractor — for both reemployment wages and comp premium?

## Sources

1. Ch. 440, Fla. Stat. (workers' compensation), s. 440.04: https://www.flsenate.gov/Laws/Statutes/2025/440.04 (200, statute text read 2026-10-27)
2. Ch. 443, Fla. Stat. (reemployment tax): https://www.flsenate.gov/Laws/Statutes/2025/443.08 (page resolved 2026-10-27 but section text not extracted this run — figures **needs-sources**)
3. FL DOR / Reemployment forms index incl. F-2220: https://floridarevenue.com/Forms_library/current/f2220.pdf (200 PDF, 2026-10-27)
4. floridajobs.org reemployment employer pages: unreachable from this workstation 2026-10-27 (DNS failure) — wage base, rate ranges, RT-6 dates **needs-sources**

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Florida payroll and reemployment tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
