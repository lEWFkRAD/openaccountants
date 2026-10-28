---
name: pa-social-contributions
description: >
  Use this skill whenever asked about Pennsylvania social contributions for
  tax year 2026 — unemployment compensation (UC) employer contributions on a
  $10,000 per-employee wage base with experience rating, the 9.2% solvency
  surcharge and 0.60% Additional Contributions in effect for 2026, the 3%
  delinquency increase, the 0.07% uncapped employee UC withholding, UC
  quarterly UC-2/UC-1 reports due the last day of the month after each
  quarter, workers' compensation insurance under the PA Workers' Comp Act,
  and the PA Paid Family Leave program (PFML) flagged needs-sources. Trigger
  on "Pennsylvania unemployment", "PA UC rates", "PA UC surcharge", "PA
  contribution rate", "UC-2", "Pennsylvania paid family leave", "PA PFML
  contributions", "Pennsylvania workers compensation employer".
  Source-cited draft; DLI UC yearly tax highlights read 2026-10-27. PFML
  official pages unreachable 2026-10-27 — PFML figures needs-sources.
jurisdiction: US-PA
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - pa-payroll
---

# Pennsylvania social contributions (UC, workers' comp, PFML) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Pennsylvania professional.

## 1. Scope and sources

Employer-side social contributions in Pennsylvania: **unemployment compensation (UC)** under the Unemployment Compensation Law (Act of Dec. 17, 1936, P.L. 1972 — also an uncodified session law), **workers' compensation insurance**, and the **PA Paid Family Leave (PFML)** insurance program. Payroll mechanics (withholding, UC-2 filing) sit in `pa-payroll`.

**Source status (as_of 2026-10-27):** [DLI UC yearly tax highlights](https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/yearly-tax-highlights) fetched HTTP 200 and read — 2026 and 2027 solvency measures, wage base, surcharge, employee contribution all quoted below. PFML official pages (pfml.pa.gov, ucpfi.pa.gov) did not resolve from this host on 2026-10-27 — **PFML contribution figures are needs-sources**. Workers' comp premium rules are general; the DLI workers' comp pages are navigation shells — **needs-sources for rate detail**.

## 2. Who applies

- **UC employers:** covered under the UC Law — most employers paying wages; also reimbursing (government/nonprofit) employers. New employers get an assigned rate for the first two calendar years (rate figure needs-sources).
- **Employees:** every employee pays the 0.07% UC contribution, **including employees of reimbursable employers**, withheld by the employer.
- **Workers' comp:** nearly all employers must carry insurance or be self-insured (DLI Bureau of Workers' Compensation; SWIF for the state fund).
- **PFML:** employers and employees contribute to the state-administered paid family leave insurance fund — **contribution rates and start date needs-sources** (official pages unreachable 2026-10-27).

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| UC taxable wage base | **$10,000 per employee per calendar year** | DLI highlights, read 2026-10-27 |
| UC employer rate | Experience-rated; published range **0.014190 to 0.103734** for 2025, 2026 and 2027 alike (VERIFIED vs archived DLI yearly tax highlights, which repeat the same figures under each year's heading) | DLI highlights, archived 2026-10-28 |
| Newly liable employer rate | **3.8220%** non-construction / **10.5924%** construction (includes 9.2% surcharge only; 0.60% Additional Contributions does not apply to newly liable employers) — VERIFIED vs archived DLI highlights | DLI highlights, archived 2026-10-28 |
| UC solvency surcharge | **9.2% surcharge in effect for 2026 and 2027**, applied as: (Basic Contribution Rate + 3% delinquency increase if applicable) × 9.2% = Surcharge Adjustment; applies to all employers, not appealable | DLI highlights, read 2026-10-27 |
| Additional Contributions | **0.60% of taxable wages** — applies to all employers, not appealable | DLI highlights, read 2026-10-27 |
| Delinquency increase | **+3 percentage points** to the basic rate for UC delinquency | DLI highlights, read 2026-10-27 |
| Employee UC contribution | **0.07% of gross wages (70¢ per $1,000), no wage cap**, not appealable | DLI highlights, read 2026-10-27 |
| FUTA credit | FUTA 6.0% on $7,000; PA credit-reduction status needs-sources | needs-sources |
| Workers' comp | Private carriers or SWIF; manual rates by class — needs-sources | DLI WC pages (nav shells) 2026-10-27 |
| PFML | State insurance program; rates needs-sources | official pages unreachable 2026-10-27 |

**AUDIT FLASH POINT** — the **3% delinquency increase** and the 9.2% surcharge math: employers who under-report or pay UC late get the delinquency increase folded into the surcharge base, compounding the rate for the next year. DLI applies it automatically; it is not appealable.

## 4. Deadlines

| Filing | Due |
|---|---|
| UC-2/UC-1 quarterly contribution & wage reports | **Last day of the month after each quarter ends** (Apr 30, Jul 31, Oct 31, Jan 31) |
| UC-14 rate appeal | 15 days from the rate notice date |
| New employer registration | Within 15 days of first becoming a covered employer (form figure needs-sources) |
| Workers' comp | Policy continuous; first report of injury within 21 days (needs-sources re-verify) |
| PFML | Program calendar needs-sources |

Quarterly due dates are the standard UC-2 calendar; the DLI highlights page confirms the quarterly cycle — re-verify exact dates against the current notices.

## 5. Penalties and interest

- Late/unpaid UC triggers the **3% delinquency increase** to the experience rate (see flash point) plus interest on contributions due — **1.0% per month (12% yearly) for 2018 onward**, computed per month or fraction of a month on unpaid employer AND employee contributions — VERIFIED vs archived [DLI Calculating Contributions, Penalties and Interest](https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/uc-tax-rates/calculating-contributions--penalties-and-interest).
- **Late quarterly report penalty:** 15% of total contributions payable for the quarter, minimum **$125**, maximum **$450** — filing on time avoids the penalty even if payment is late (interest still accrues). VERIFIED vs archived DLI page.
- **Dishonored remittance penalty:** 10% of the payment, minimum **$25** per occurrence, maximum **$1,000**. VERIFIED vs archived DLI page.
- Failure to withhold the 0.07% employee contribution is an employer liability.
- Workers' comp: uninsured-employer penalties under the WC Act — figures needs-sources.

## 6. Cross-border

- Multi-state employers register per state; PA UC covers work performed in PA (`pa-cross-border`).
- Reciprocal-state commuters (NJ/OH/IN/MD/VA/WV) still owe **PA UC** on PA-worked wages — reciprocity covers income tax only.
- PFML vs other states' paid-leave programs: no known reciprocity — needs-sources.

## 7. Worked examples

**Example A — 2026 employer UC per covered employee (no delinquency).**

```oa-check
name: UC employer contribution with 9.2% surcharge and 0.60% additional
inputs:
  wage_base: 10000
  basic_rate: 0.015
  surcharge: 0.092
  additional: 0.006
steps:
  - surcharge_adj: basic_rate * surcharge
  - total_rate: basic_rate + surcharge_adj + additional
  - employer_uc: wage_base * total_rate
expected:
  surcharge_adj: 0.00138
  total_rate: 0.02238
  employer_uc: 223.80
```

**Example B — employee UC withholding (uncapped).**

```oa-check
name: Employee UC contribution on 85,000 of gross wages
inputs:
  gross_wages: 85000
  employee_rate: 0.0007
steps:
  - employee_uc: gross_wages * employee_rate
expected:
  employee_uc: 59.50
```

## 8. Ask the client

- Are UC quarterly reports current? Delinquency adds 3 points to next year's rate — compounding with the 9.2% surcharge.
- Experience vs assigned rate: new employers (first two calendar years) get the assigned rate.
- Are employees being charged the 0.07% with **no cap** — including reimbursable-employer staff?
- Workers' comp classification codes and SWIF vs private carrier.
- PFML registration and contribution setup — confirm current rates from the program before quoting.

## 9. Sources

- [DLI UC yearly tax highlights](https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/yearly-tax-highlights) — read 2026-10-27 (wage base, 9.2% surcharge formula, 0.60% additional, 0.07% employee, 2027 rate range)
- [DLI workers' compensation](https://www.pa.gov/agencies/dli/businesses/workers-compensation) — HTTP 200 2026-10-27 (navigation shell)
- `pa-payroll` (tier 2, read 2026-09-25) — UC withholding mechanics, $10,000 base cross-check
- **needs-sources:** PFML contribution rates and program calendar (pfml.pa.gov / ucpfi.pa.gov unreachable 2026-10-27); FUTA credit-reduction status; WC penalty figures. Resolved 2026-10-28 from archived DLI pages: 2026 published rate range (same 0.014190–0.103734 as 2025/2027), new-employer assigned rates (3.8220% / 10.5924%), UC interest (1%/month), late-report and dishonored-payment penalties.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Pennsylvania UC, workers' comp and PFML questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
