---
name: ks-social-contributions
description: >
  Use this skill whenever asked about Kansas employer social contributions
  for tax year 2026 — unemployment insurance (UI) contributions under
  K.S.A. 79-27 administered by the Kansas Department of Revenue Labor
  Services, the UI-only nature of Kansas employer social cost (no state
  disability, no paid-family-leave, no state health mandate), and the
  interaction with federal FUTA. Trigger on "Kansas unemployment
  insurance", "Kansas UI rate", "Kansas employer contributions",
  "K.S.A. 79-27", "KW-3 UI". Source-cited draft; wage base and rate
  ranges needs-sources (dol.ks.gov 403 to plain HTTP this run).
jurisdiction: US-KS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ks-income-tax
---

# Kansas social contributions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-28. Kansas has **no state-run social insurance beyond unemployment insurance**: no state disability insurance, no paid family and medical leave program, no individual health-coverage mandate. Employer social cost above federal FICA/FUTA is **UI contributions only** (K.S.A. 79-27), administered by the **Labor Services division of the Kansas Department of Revenue** — UI sits inside KDOR, not a separate labor department, which is why UI forms and e-filing share the KDOR portal. **Source status:** KDOR pages verified 2026-10-28; **dol.ks.gov returned 403 Forbidden to plain HTTP** and the K.S.A. 79-27-105 statute page serves a JS shell, so the **taxable wage base and contribution-rate ranges are needs-sources**.

## 2. Who applies

- **Covered employers**: any employer paying Kansas wages above the statutory threshold must register and pay Kansas UI contributions — registration and quarterly wage reporting run through the KDOR UI system (KDOR business pages, read 2026-10-28).
- **Successors and common-owner groups** are aggregated for experience rating — detail **needs-sources**.
- **Employee side**: Kansas imposes **no employee UI premium** (unlike Alaska/New Jersey/Washington models) — employer-only; **needs-sources** for the current statutory confirmation.
- **Federal layer**: FUTA applies with the standard 6.0% gross / 5.4% net-credit mechanics; Kansas is a credit-reduction state only in years of federal borrowing — status for 2026 **needs-sources**.

## 3. Rates and base

| Item | Rule | Source status |
|---|---|---|
| UI taxable wage base | per-employee annual base (recent years in the $15,000 range) | **needs-sources** — K.S.A. 79-27-105 JS-only; dol.ks.gov 403 |
| Employer contribution rate | experience-rated schedule; new-employer rate applies to first years | **needs-sources** |
| New-employer rate | fixed statutory rate for first coverage years | **needs-sources** |
| Employee share | none | needs-sources (structural, low risk) |
| Suspense/financing surcharges | years of federal loan balance historically added surcharges | **needs-sources** |

## 4. Deadlines

- Quarterly UI wage-and-contribution reports: last day of the month following each calendar quarter (standard KDOR UI calendar) — **needs-sources** for the 2026 calendar page.
- Annual rate notices issue each year for the rate year beginning January 1 — protest windows **needs-sources**.
- Annual report of wages for experience rating accompanies the Q4 filing — **needs-sources**.

## 5. Penalties and interest

- Late quarterly reports/contributions: penalty plus interest under K.S.A. 79-27 — percentages **needs-sources**.
- Misclassification of employees as independent contractors triggers back contributions — KDOR publishes a Misclassification Statistics page (verified in KDOR navigation, read 2026-10-28); penalty tiers **needs-sources**.

## 6. Cross-border interactions

- Multi-state employers: Kansas base/rate apply to Kansas wages; other states' bases differ — file per state.
- Remote workers: UI coverage follows the localization-of-work tests (4-part federal UI compact tests) — **needs-sources** for Kansas adoption citation.
- No Kansas portability issues for Social Security/Medicare — federal only.

## 7. Worked examples

**Example 1 — single-employee UI cost (illustrative base/rate, needs-sources):** one employee, $180,000 annual Kansas wages, illustrative base $15,000, experience rate 2.1%.

```oa-check
name: KS UI employer contribution (illustrative)
inputs:
  wages: 180000
  base: 15000
  rate: 0.021
steps:
  - taxable: min(wages, base)
  - ui: taxable * rate
expected:
  taxable: 15000
  ui: 315
```

**Example 2 — two-employee small employer:** same facts, two employees.

```oa-check
name: KS UI two employees
inputs:
  per_employee_ui: 315
  employees: 2
steps:
  - total: per_employee_ui * employees
expected:
  total: 630
```

## 8. Ask the client

- Kansas payroll footprint and headcount; which states' bases apply.
- Experience-rating history / successor-ownership changes (drives rate).
- Worker classification posture (W-2 vs 1099) — KDOR misclassification exposure.
- Whether FUTA credit-reduction status affects 2026 federal cost.

## 9. Sources

- KDOR business navigation (Labor Services / UI under KDOR; Misclassification Statistics page): https://www.ksrevenue.gov/business.html — read 2026-10-28, verified.
- K.S.A. 79-27-105 (UI rates/base): https://www.kslegislature.org/li/b2025_26/statutes/2025_79-27-105/ — HTTP 200 but JS shell; **needs-sources**.
- dol.ks.gov (UI program pages): 403 Forbidden to plain HTTP on 2026-10-28 — **needs-sources**.

**Needs-sources:** 2026 UI taxable wage base, contribution-rate schedule and new-employer rate, quarterly due-date calendar, penalty/interest percentages, FUTA credit-reduction status for 2026.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kansas payroll/social questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
