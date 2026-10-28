---
name: ky-social-contributions
description: >
  Use this skill whenever asked about Kentucky employer social
  contributions for tax year 2026 — unemployment insurance
  contributions administered by the Education & Workforce Development
  Cabinet (KRS ch. 341), employer-only nature of the UI tax, workers'
  compensation insurance under KRS ch. 342, and the absence of state
  disability or paid-leave payroll taxes. Trigger on "Kentucky UI
  rate", "Kentucky SUTA", "Kentucky unemployment wage base", "Kentucky
  employer taxes", "Kentucky workers compensation requirement".
  Source-cited draft; labor.ky.gov pages JS-rendered this run — UI
  figures flagged needs-sources.
jurisdiction: US-KY
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - ky-payroll
---

# Kentucky social contributions (UI + workers' comp) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Kentucky employer social contributions: unemployment insurance contributions under KRS ch. 341 administered by the Education & Workforce Development Cabinet (EWD), mandatory workers' compensation insurance under KRS ch. 342, and federal FICA. Kentucky has **no** state disability insurance, **no** paid family/medical leave contribution, and **no** state retirement mandate for private employers. **Source status:** the EWD employer and rate pages (labor.ky.gov) returned 200 but render their content via JavaScript — no wage-base or rate text was extractable this run, so every 2026 UI figure below is flagged **needs-sources**; do not publish numbers until the current rate notice is pulled.

## 2. Who applies

- Employers covered under KRS ch. 341 (general coverage tests — statutory text **needs-sources**). Out-of-state employers with Kentucky employees are covered on the same basis.
- The UI contribution is **employer-only** — Kentucky employees pay no state UI tax.
- Workers' compensation: most Kentucky employers must carry coverage (KRS ch. 342; thresholds and exemptions — **needs-sources**).

## 3. Rates and base (2026 — all figures needs-sources)

| Item | 2026 amount | Source |
|---|---|---|
| UI taxable wage base | **needs-sources** (pull the EWD 2026 rate notice) | KRS 341.370 — JS shell |
| Experience rate range (min/max) | **needs-sources** | KRS 341.365 — JS shell |
| New-employer assigned rate | **needs-sources** | KRS 341.367 — JS shell |
| Employee share of UI | none — employer-only | KRS ch. 341 structure |
| Workers' comp premium | carrier-rated by class code | KRS ch. 342 — **needs-sources** |
| State disability / paid family leave | none | absence confirmed; no such KY program |

Base: covered wages up to the annual wage base per employee; rates are experience-rated with reserve-ratio components.

## 4. Deadlines

- Quarterly contribution and wage reports (Form UC-2/UC-6) due the last day of the month following each quarter (1/31, 4/30, 7/31, 10/31 pattern — confirm on the EWD filing page: **needs-sources**).
- Annual rate notices issue late in the year with an appeal window (confirm: **needs-sources**).
- Workers' compensation: continuous coverage obligation; certificate of insurance required for many contracts and permits.

## 5. Penalties and interest

Late/unpaid UI contributions draw penalties and interest under KRS ch. 341 (current schedule: **needs-sources**). Common failure modes: (1) out-of-state employers missing Kentucky coverage for Kentucky-based staff; (2) misclassifying workers as independent contractors, shifting both UI wages and comp premium; (3) letting a dormant account lapse while still paying Kentucky wages.

## 6. Cross-border interactions

- Multi-state employees: localization-of-service rules decide which state gets the wages (confirm EWD guidance: **needs-sources**).
- FUTA credit against Kentucky UI follows the standard pattern; 2026 credit-reduction status for Kentucky: **needs-sources**.
- Reciprocal coverage agreements for multi-state workers (confirm KY participation: **needs-sources**).

## 7. Worked examples

Illustrative only — substitute the real 2026 wage base and rate from the EWD notice before use. Employer at an assumed $11,000 base and 2.0% rate on one employee:

```oa-check
name: KY UI illustrative one employee
inputs:
  base: 11000
  rate: 0.02
steps:
  - tax: base * rate
expected:
  tax: 220.00
```

Same employer, 6 employees at the assumed base and rate:

```oa-check
name: KY UI illustrative six employees
inputs:
  base: 11000
  n: 6
  rate: 0.02
steps:
  - wages: base * n
  - tax: wages * rate
expected:
  wages: 66000.00
  tax: 1320.00
```

## 8. Ask the client

- Pull the current EWD rate notice for the 2026 wage base and experience rate before quoting anything.
- Do you have Kentucky-based employees (including remote hires into Kentucky)?
- Is workers' compensation coverage in force, with correct class codes?
- Are workers correctly classified for both UI wages and comp premium?

## Sources

1. EWD employer UI page: https://labor.ky.gov/unemployment-insurance/employers/ (200, JS-rendered — content **needs-sources**, 2026-10-27)
2. EWD UI rates page: https://labor.ky.gov/unemployment-insurance/employers/rates/ (200, JS-rendered — **needs-sources**, 2026-10-27)
3. KRS ch. 341 (UI): https://apps.legislature.ky.gov/law/krs/341/341.365.asp (JS shell — **needs-sources**)
4. KRS ch. 342 (workers' comp): section text not fetched — **needs-sources**

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kentucky payroll and UI questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
