---
name: ar-unemployment-contributions
description: >
  Use this skill whenever asked about Arkansas employer social
  contributions for tax year 2026 — unemployment insurance
  contributions administered by the Division of Workforce Services,
  the employer-only nature of the UI tax, the Arkansas taxable wage
  base, experience rating and solvency surtaxes, and the absence of
  state disability or paid-leave payroll taxes. Trigger on "Arkansas
  UI rate", "Arkansas SUTA", "Arkansas unemployment wage base",
  "Arkansas employer taxes", "Arkansas workforce services UI".
  Source-cited draft; workservices.arkansas.gov did not resolve from
  this host this run — all UI figures flagged needs-sources.
jurisdiction: US-AR
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ar-income-tax
---

# Arkansas social contributions (UI) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Arkansas employer social contributions: unemployment insurance contributions under Ark. Code Ann. title 11 administered by the **Division of Workforce Services (DWS)**, federal FICA/FUTA, and mandatory workers' compensation insurance above the statutory employee count. Arkansas has **no** state disability insurance, **no** paid family/medical leave contribution, and **no** state-mandated private retirement contribution. **Source status:** workservices.arkansas.gov did not resolve by DNS from this drafting host this run, and arkleg.state.ar.us served empty/500 responses — every UI figure below is **needs-sources**. Pull the DWS 2026 rate notice before publishing amounts.

## 2. Who applies

- Employers covered under Ark. Code Ann. §11-15-301 et seq. (coverage tests — statutory text **needs-sources**). Out-of-state employers with Arkansas employees are covered on the same basis.
- The UI contribution is **employer-only** — Arkansas employees pay no state UI tax.
- Workers' compensation: mandatory for employers with three or more employees (threshold — confirm, **needs-sources**); an insurance mandate, not a tax.

## 3. Rates and base (2026 — all figures needs-sources)

| Item | 2026 amount | Source |
|---|---|---|
| UI taxable wage base | **needs-sources** (DWS 2026 notice) | Ark. Code §11-15-504 — not fetched |
| Experience rate range (min/max) | **needs-sources** | Ark. Code §11-15-505 — not fetched |
| New-employer assigned rate | **needs-sources** | Ark. Code §11-15-506 — not fetched |
| Solvency surtax | **needs-sources** (check DWS annual notice) | DWS notices |
| FUTA credit reduction | none typical — verify current-year DOL list | US DOL |

## 4. Deadlines

- **Quarterly contribution return (Form B-8):** due the last day of the month following each quarter (pattern — confirm, **needs-sources**).
- **Annual reconciliation (Form B-9):** due January 31 (pattern — **needs-sources**).
- **Wage detail (B-81/W-3):** quarterly with the B-8 (**needs-sources**).

## 5. Penalties and interest

Late returns/contributions draw penalties and interest under title 11 (percentages **needs-sources**). Common failure modes: (1) accruing UI at gross payroll instead of the per-employee wage base; (2) missing the solvency surtax in surtax years; (3) misclassifying workers — Arkansas DWS audits contractor arrangements aggressively (program detail **needs-sources**).

## 6. Cross-border interactions

- Multi-state employers register with DWS when Arkansas employees exist; wage base applies per employee per state.
- Staffing/PEO arrangements file under DWS leasing rules (**needs-sources**).

## 7. Worked examples

An employer with 6 Arkansas employees each paid $28,000 in 2026, at an assumed 2.3% rate on a $14,000 wage base (illustrative inputs — both **needs-sources**):

```oa-check
name: AR UI contribution illustrative
inputs:
  employees: 6
  wage_base: 14000
  rate: 0.023
steps:
  - taxable: employees * wage_base
  - contribution: taxable * rate
expected:
  taxable: 84000.00
  contribution: 1932.00
```

## 8. Ask the client

- Has the DWS 2026 rate notice been received; is the experience rate reconciled to the reserve account?
- Are contributions accrued on the wage base, not gross payroll?
- Contractor-heavy workforce: has DWS classification risk been reviewed?
- Workers' comp coverage current for 3+ employee thresholds?

## Sources

1. Division of Workforce Services: https://workservices.arkansas.gov/ (DNS did not resolve from this host 2026-10-27 — **needs-sources**)
2. Ark. Code Ann. title 11 ch. 15: https://www.arkleg.state.ar.us/Code (empty/500 from this host — **needs-sources**)
3. DFA (administers some UI-related payments via ATAP): https://www.dfa.arkansas.gov/office/taxes/ (read 2026-10-27)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Arkansas payroll and UI questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
