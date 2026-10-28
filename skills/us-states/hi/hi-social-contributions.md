---
name: hi-social-contributions
description: >
  Use this skill whenever asked about Hawaii employer/employee social
  contributions for tax year 2026 — unemployment insurance (HRS ch. 383,
  experience-rated employer contributions), temporary disability insurance
  (HRS ch. 392, employee contribution capped at 0.5% of weekly wages), and
  the Prepaid Health Care Act mandate (HRS ch. 393). Trigger on "Hawaii
  unemployment tax", "Hawaii TDI", "Hawaii PREA", "Hawaii employer
  contributions", "HRS 383", "HRS 392", "HRS 393". Source-cited draft;
  statute text read from capitol.hawaii.gov 2026-10-27; UI rate tables
  needs-sources.
jurisdiction: US-HI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - hi-corporate-income-tax
---

# Hawaii social contributions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Hawaii has no state payroll tax beyond income-tax withholding (see `hi-payroll-withholding`); its "social contributions" layer is three separate regimes administered by the Department of Labor and Industrial Relations (DLIR): **unemployment insurance (HRS ch. 383)**, **temporary disability insurance (HRS ch. 392)**, and the **Prepaid Health Care Act (HRS ch. 393)** employer health-coverage mandate. Statute text read from the HRS mirror at capitol.hawaii.gov 2026-10-27. **Source status:** ch. 383 section map, §392-43 contribution rule, and §393-11 coverage trigger are verified from statute; the current UI taxable wage base, contribution-rate schedules, and solvency surcharges live on labor.hawaii.gov, which returned HTTP 429 all run — **needs-sources** for every UI dollar figure.

## 2. Who applies

- **UI (ch. 383):** employers as defined in §383-2; contributions are **employer-only** (employee wage-replacement contributions were not part of the ch. 383 section map read — the TOC shows Part III "Contributions and Coverage" with employer contribution sections §§383-61 to 383-73; Hawaii's TDI/PREA cover the employee-side benefits).
- **TDI (ch. 392):** every employer must provide temporary disability benefits (state plan or private plan approved by the director). Employees may be required to pay **up to one-half the cost, capped at 0.5% of weekly wages** (§392-43(a), text read 2026-10-27); the employer pays the balance.
- **PREA (ch. 393):** every employer paying a regular employee **monthly wages of at least 86.67 × the state minimum hourly wage** must provide qualifying prepaid group health coverage (§393-11, text read 2026-10-27). Premiums may be shared with employees but the employee share is capped by statute (§393-13 — section text not extracted this run, **needs-sources** for the cap percentage).

## 3. Mechanics and rates

| Regime | Who pays | Rate / base | Source status |
|---|---|---|---|
| UI contributions | Employer only | Experience-rated on a taxable wage base; rate schedules in §§383-66/383-68 (fund-solvency schedule + experience rating) | sections confirmed from TOC; **current wage base and rate ranges needs-sources** |
| UI special assessments | Employer | §§383-61.5 (fed-loan interest), 383-129 (employment & training assessment), 383-131 (UI technology assessment) | section titles read from TOC; **rates needs-sources** |
| TDI | Employee ≤ 0.5% of weekly wages; employer pays balance | wage base = (average annual wage ÷ 52) × 1.21, published annually by the director (§392-43(b)(2), text read 2026-10-27); **current dollar base needs-sources** | verified rule; figure needs-sources |
| TDI eligibility screen | — | employee must have earned ≥ $400 and worked ≥14 weeks (20+ hrs each) in the prior 52 weeks to be covered (§392-43(b)(1), text read 2026-10-27) | verified |
| PREA | Employer (may share premium with employee) | coverage trigger: monthly wages ≥ 86.67 × minimum wage (§393-11, text read 2026-10-27); Hawaii minimum wage — **needs-sources** | verified trigger; figure needs-sources |

## 4. Deadlines

- **UI:** quarterly contribution & wage reports and payments — §§383-70 (contributions; levy; returns; assessments) and 383-94 (records and reports) confirm the reporting architecture; the customary quarterly due dates (last day of the month following each calendar quarter) — **needs-sources** for the current published calendar.
- **TDI:** contributions withheld each pay period ("withholding period shall be equal to the pay period", §392-43(a), text read 2026-10-27); private-plan filings annual with DLIR — **needs-sources**.
- **PREA:** continuous coverage obligation; no periodic filing unless seeking an exemption (§393-17/393-18 in TOC).

## 5. Penalties and interest

- UI: §383-73 (penalty for delinquency; remission) and §383-143 (general penalty) exist per the ch. 383 TOC read 2026-10-27; **percentages needs-sources**.
- TDI: §392-42.5 and §392-47 (failure to maintain claims service / failure to give security — penalty and injunction) per TOC; amounts **needs-sources**.
- PREA: §§393-33/393-34 penalties; §393-24 makes a noncomplying employer liable for the employee's health-care costs (TOC titles read 2026-10-27; amounts **needs-sources**).

## 6. Cross-border interactions

- Remote workers physically working in Hawaii trigger PREA/TDI/UI obligations even for an out-of-State employer — Hawaii's definitions key off employment performed in the State (place-of-performance rules, §392-4 in TOC; text not extracted, **needs-sources**).
- Multi-State employers: UI is experience-rated per State; a Hawaii workforce with frequent claims raises the ch. 383 rate schedule outcome (§383-66/68).

## 7. Worked examples

An employer with one employee earning $1,200/week, TDI employee contribution at the statutory cap:

```oa-check
name: HI TDI max weekly employee contribution
inputs:
  weekly_wage: 1200
  cap_rate: 0.005
steps:
  - weekly_contribution: weekly_wage * cap_rate
  - annual_contribution: weekly_contribution * 52
expected:
  weekly_contribution: 6.00
  annual_contribution: 312.00
```

PREA coverage trigger at a $14.00 minimum wage (illustrative — current minimum **needs-sources**):

```oa-check
name: HI PREA monthly wage trigger
inputs:
  minimum_wage: 14.00
  multiplier: 86.67
steps:
  - monthly_trigger: minimum_wage * multiplier
expected:
  monthly_trigger: 1213.38
```

## 8. Ask the client

- Are UI quarterly contribution/wage reports filed for every Hawaii payroll, including remote employees working in Hawaii?
- Is TDI coverage via the state plan or an approved private plan — and is the employee contribution at or under 0.5% of weekly wages?
- Does every regular employee at ≥86.67× minimum wage have qualifying PREA coverage?
- Any exemption applications on file (ch. 393-17) and still valid?

## Sources

1. HRS ch. 383 (Unemployment Insurance) TOC: https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0383/HRS_0383-.htm (200, section map read 2026-10-27)
2. HRS §392-43 (TDI contribution cap 0.5%, wage-base formula, eligibility screen): https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0392/HRS_0392-0043.htm (200, text read 2026-10-27)
3. HRS §393-11 (PREA coverage trigger 86.67× minimum wage): https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0393/HRS_0393-0011.htm (200, text read 2026-10-27)
4. HRS ch. 392 TOC (TDI structure): https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0392/HRS_0392-.htm (200, read 2026-10-27)
5. HRS ch. 393 TOC (PREA structure, penalty sections): https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0393/HRS_0393-.htm (200, read 2026-10-27)
6. DLIR Unemployment Insurance Division: https://labor.hawaii.gov/ui/ (HTTP 429 all attempts 2026-10-27 — UI wage base/rates **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Hawaii payroll/benefits-mandate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
