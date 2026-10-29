---
name: ar-unemployment-contributions
description: >
  Use this skill whenever asked about Arkansas employer social
  contributions for tax year 2026 — unemployment insurance
  contributions administered by the Division of Workforce Services
  (Arkansas Division of Reemployment), the employer-only nature of
  the UI tax, the $7,000 taxable wage base, the 2026 rate table
  (new-employer 2.0%, experienced range 0.2%-5.1%, stabilization
  0.2%), experience rating, coverage tests, and the absence of state
  disability or paid-leave payroll taxes. Trigger on "Arkansas UI
  rate", "Arkansas SUTA", "Arkansas unemployment wage base",
  "Arkansas employer taxes", "Arkansas workforce services UI".
jurisdiction: US-AR
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: "0.2"
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - ar-income-tax
---

# Arkansas social contributions (unemployment insurance), tax year 2026

> **Source-cited draft.** Built from the Arkansas Division of Workforce Services (Arkansas Division of Reemployment) employer UI pages, read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Arkansas professional.

Arkansas employer social contributions: unemployment insurance (UI) contributions under the Arkansas Unemployment Insurance Law (Title 11 — the DWS employer page cites "Title 11, Chapter 10"), administered by the **Division of Workforce Services (DWS)**; federal FICA/FUTA; and mandatory workers' compensation insurance. Arkansas has **no** state disability insurance, **no** paid family/medical leave contribution, and **no** state-mandated private retirement contribution. The UI tax is computed "on the wages paid to each employee on a calendar quarter basis" ([DWS, Employer UI Contributions](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/employer-ui-contributions/)).

## Who this applies to

- **Employers** covered by the Arkansas Unemployment Insurance Law. If a service is not specifically exempt, it is covered by state unemployment insurance (DWS, Employer UI Contributions).
- **Domestic employment** is exempt unless cash wages meet or exceed $1,000 in any calendar quarter, in which case the employer is liable for the whole calendar year and the following year (DWS, Employer UI Contributions).
- **Agricultural employment** is exempt unless wages of $20,000 or more are paid in a calendar quarter or the employer has 10 or more workers in 20 calendar weeks (DWS, Employer UI Contributions).
- The UI contribution is **employer-only** — "No, deductions are not made from your paycheck" (DWS UI FAQs: Arkansas employees pay no state UI tax).
- Workers' compensation is a separate insurance mandate, not a tax.
- Out-of-state employers with Arkansas employees register with DWS; the wage base applies per employee per state.

## Rates, bands and thresholds

2026 rate table ([DWS, UI for Employers](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/)):

| Item | 2026 | Source |
|---|---|---|
| UI taxable wage base | $7,000 per employee per calendar year | [DWS, UI for Employers](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/); [DWS, Employer UI Contributions](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/employer-ui-contributions/) |
| New employer rate | 2.0% | [DWS, UI for Employers](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/) |
| Experienced employer range | 0.2% – 5.1% | [DWS, UI for Employers](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/) |
| Deficit rates (benefit-cost levels) | 6.1%, 8.1%, 10.1% | [DWS, UI for Employers](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/) |
| Stabilization rate | 0.2% | [DWS, UI for Employers](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/) |
| Statutory rate ceiling without assessments | maximum rate of 5.0% ("tax rates currently range from 0.1% to a maximum rate of 5.0%, plus the stabilization rate") | [DWS, Employer UI Contributions](https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/employer-ui-contributions/) |

Historical rates on the same DWS page, for context and prior-year reconciliations: in 2024 the taxable wage base was $7,000, the experienced-employer range 0.225%–10.125% (including assessments), and the new-employer rate 2.025% (1.9% plus the 0.125% administrative assessment for fiscal 2024); in 2025 the experienced range was 0.200%–10.100% and the new-employer rate 2.0% (1.9% plus the 0.1% administrative assessment for fiscal 2025); a 2023 new employer was assigned 3.1% and stays there until three full years of benefit-risk are established (DWS, Employer UI Contributions). Act 1191: after two consecutive years of a 4.0% additional-contribution assessment, the assessment increases to 6.0% (basic rate 12.0%), and after two more consecutive years at 6.0% it increases to 8.0% (basic rate 14.0%) (DWS, Employer UI Contributions).

## The taxable base

- The UI tax is computed on wages paid to each employee on a calendar-quarter basis, up to the $7,000 taxable wage base per employee per calendar year (DWS, Employer UI Contributions).
- "Wages" is all remuneration for personal services — salaries (including corporation officers' salaries), commissions, bonuses, fees, fringe benefits, sick pay, deferred compensation and tips reported to the employer (DWS, Employer UI Contributions).
- The employer's experience rate follows the reserve account: when an entire ongoing business is acquired, the previous owner's tax rate is assigned to the new owner; a rate may transfer when a business location is acquired (DWS, Employer UI Contributions).
- The federal FUTA credit reduction status changes year by year — check the current US DOL list before accruing FUTA.

## Deadlines and filing

- UI contributions are computed and paid by calendar quarter through the DWS Tax21 employer system; wage detail is reported quarterly (DWS, UI for Employers).
- The DWS employer handbook has the filing calendar and report forms (DWS, UI for Employers). The exact statutory due date for each quarterly contribution report is on the DWS report forms — see Not yet confirmed.

## Penalties and interest

- Late returns and late contributions draw penalties and interest under the Arkansas Unemployment Insurance Law (title 11); the specific percentages are on the DWS report forms — see Not yet confirmed.
- Common failure modes: (1) accruing UI on gross payroll instead of the per-employee $7,000 wage base; (2) missing the deficit-rate and stabilization components in a surtax year; (3) worker misclassification — DWS audits contractor arrangements.

## Cross-border points

- **Multi-state employers** register with DWS when Arkansas employees exist; the $7,000 wage base applies per employee per state, so the same employee's wages can be taxable in two states up to each state's base.
- **Staffing/PEO arrangements** file under the DWS leasing rules — the rate-transfer rules for acquired businesses apply (DWS, Employer UI Contributions).
- UI contributions are not withheld from employees; the individual income tax side of wages is in `ar-income-tax` and `ar-payroll-withholding`.

## Worked examples

**Example 1: quarterly UI contribution (hypothetical facts, 2026 confirmed figures).** An employer with 6 Arkansas employees each paid $28,000 in 2026 at the 2026 new-employer rate of 2.0%: each employee is taxed on the first $7,000 of wages, so taxable wages are 6 × $7,000 = $42,000 and the contribution is $840.00.

```oa-check
name: AR UI contribution, 6 employees at 2.0% new-employer rate (2026)
inputs:
  employees: 6
  wage_base: 7000
  rate: 0.02
steps:
  - taxable: employees * wage_base
  - contribution: taxable * rate
expected:
  taxable: 42000.00
  contribution: 840.00
```

**Example 2: employee over the wage base (hypothetical facts).** One employee paid $28,000 in 2026 at an experienced-employer rate of 3.0%: UI applies only to the first $7,000, so the contribution is $210.00, not $840.00.

```oa-check
name: AR UI wage-base cap, one employee (2026)
inputs:
  wages: 28000
  wage_base: 7000
  rate: 0.03
steps:
  - taxable: min(wages, wage_base)
  - contribution: taxable * rate
expected:
  taxable: 7000
  contribution: 210.00
```

## Ask the client first

- Has the DWS 2026 rate notice been received, and is the experience rate reconciled to the reserve account (including any stabilization or deficit component)?
- Are contributions accrued on the $7,000 per-employee wage base, not gross payroll?
- Contractor-heavy workforce: has worker-classification risk been reviewed?
- Any business acquisition — was the predecessor's UI rate transferred?
- Domestic or agricultural employment — do the $1,000 (domestic, per quarter) or $20,000 / 10-workers-in-20-weeks (agricultural) coverage tests apply?

## Sources

| Source | URL | Read on |
|---|---|---|
| Arkansas Division of Workforce Services, Unemployment Insurance for Employers (2026 tax rates) | https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/ | 2026-10-28 |
| Arkansas Division of Workforce Services, Employer UI Contributions (wage base, rates, coverage, transfers) | https://dws.arkansas.gov/workforce-services/unemployment/employer-ui-information/employer-ui-contributions/ | 2026-10-28 |

Not yet confirmed: the exact statutory due date for the quarterly UI contribution report and wage detail (the DWS pages confirm quarterly computation but state no day; the employer handbook PDF was not read); the late-filing and late-payment penalty and interest percentages under title 11; the DWS report form numbers for 2026 (the prior draft's Form B-8/B-9 references were not confirmed against a DWS page and are not restated); whether Arkansas is on the current-year federal FUTA credit-reduction list (US DOL list not read); workers' compensation employee-count threshold (insurance mandate, not confirmed on a DWS/DFA page here).

<!-- openaccountants-cta-block -->

---

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
