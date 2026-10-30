---
name: hi-social-contributions
description: >
  Use this skill whenever asked about Hawaii employer/employee social
  contributions for tax year 2026 -- unemployment insurance (HRS ch. 383,
  experience-rated employer contributions), temporary disability insurance
  (HRS ch. 392, employee contribution capped at 0.5% of weekly wages), and
  the Prepaid Health Care Act mandate (HRS ch. 393, coverage trigger at 86.67
  times the minimum hourly wage). Trigger on "Hawaii unemployment tax",
  "Hawaii TDI", "Hawaii PREA", "Hawaii employer contributions", "HRS 383",
  "HRS 392", "HRS 393". Source-cited draft; statute text read from
  capitol.hawaii.gov 2026-10-27 and 2026-10-28.
jurisdiction: US-HI
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - hi-corporate-income-tax
---

# Hawaii social contributions v0.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

> **Source-cited draft.** Built from the HRS ch. 383, 392 and 393 statutes (including §§392-43 and 393-11), HRS §387-2, and the DLIR unemployment-insurance pages, read 2026-10-27 and 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

Hawaii has no state payroll tax beyond income-tax withholding (see `hi-payroll-withholding`); its "social contributions" layer is three separate regimes administered by the Department of Labor and Industrial Relations (DLIR): **unemployment insurance (HRS ch. 383)**, **temporary disability insurance (HRS ch. 392)**, and the **Prepaid Health Care Act (HRS ch. 393)** employer health-coverage mandate.

## Who this applies to

- **UI (ch. 383):** employers as defined in §383-2; contributions are employer-only (the ch. 383 TOC shows Part III "Contributions and Coverage" with employer contribution sections §§383-61 to 383-73; Hawaii's TDI/PREA cover the employee-side benefits).
- **TDI (ch. 392):** every employer must provide temporary disability benefits (state plan or a private plan approved by the director). §392-43(a) (archived text): "an employer may deduct and withhold contributions, from each employee of one-half the cost but not more than .5 per cent of the weekly wages earned by the employee in employment and the employer shall provide for the balance of the cost."
- **PREA (ch. 393):** §393-11 (archived text): "Every employer who pays to a regular employee monthly wages in an amount of at least 86.67 times the minimum hourly wage, specified in chapter 387 ... shall provide coverage of such employee by a prepaid group health care plan."

## Rates, bands and thresholds

| Regime | Who pays | Rate / base | Source status |
|---|---|---|---|
| UI contributions | Employer only | Experience-rated on a taxable wage base; rate schedules in §§383-66/383-68 (fund-solvency schedule + experience rating) | sections confirmed from the archived ch. 383 TOC; current wage base and rate ranges -- see Not yet confirmed below |
| UI special assessments | Employer | §§383-61.5 (fed-loan interest), 383-129 (employment & training assessment), 383-131 (UI technology assessment) | section titles read from the archived TOC; rates -- see Not yet confirmed below |
| TDI | Employee ≤ 0.5% of weekly wages; employer pays the balance | wage base = average annual wage ÷ 52, "multiplied by the factor 1.21, which amount the director shall cause to be published annually" (§392-43(b)(2), archived text); current dollar base -- see Not yet confirmed below | verified rule |
| TDI eligibility screen | -- | §392-43 (archived text): "the employee has earned wages of at least $400 and has been in employment for at least fourteen weeks during each of which the employee has received remuneration in any form for twenty or more hours" | verified |
| PREA | Employer (premiums may be shared; the employee-share cap in §393-13 -- see Not yet confirmed below) | coverage trigger: monthly wages ≥ 86.67 × the minimum hourly wage (§393-11, archived text); minimum wage per HRS §387-2: "$16.00 per hour beginning January 1, 2026" | verified trigger and current minimum wage |

## The taxable base

- UI: wages up to the taxable wage base (current base -- see Not yet confirmed below); experience-rated per employer.
- TDI: weekly wages, employee contribution capped at 0.5% of weekly wages (§392-43).
- PREA: qualifying prepaid group health coverage for regular employees at or above the 86.67× minimum-wage trigger.

## Deadlines and filing

- **UI:** quarterly contribution & wage reports and payments -- §§383-70 (contributions; levy; returns; assessments) and 383-94 (records and reports) confirm the reporting architecture per the archived ch. 383 TOC; the current published quarterly due-date calendar -- see Not yet confirmed below.
- **TDI:** "withholding period shall be equal to the pay period" (§392-43, archived text); private-plan filings with DLIR -- see Not yet confirmed below.
- **PREA:** continuous coverage obligation; no periodic filing unless seeking an exemption (§§393-17/393-18 in the archived ch. 393 TOC).

## Penalties and interest

- UI: §383-73 (penalty for delinquency; remission) and §383-143 (general penalty) exist per the archived ch. 383 TOC; percentages -- see Not yet confirmed below.
- TDI: §392-42.5 and §392-47 (failure to maintain claims service / failure to give security) per the archived ch. 392 TOC; amounts -- see Not yet confirmed below.
- PREA: §§393-33/393-34 penalties; §393-24 noncomplying-employer liability per the archived ch. 393 TOC; amounts -- see Not yet confirmed below.

## Cross-border points

- Remote workers physically working in Hawaii trigger PREA/TDI/UI obligations even for an out-of-State employer -- Hawaii's definitions key off employment performed in the State (place-of-performance rules; see Not yet confirmed below for the §392-4 text).
- Multi-State employers: UI is experience-rated per State; a Hawaii workforce with frequent claims raises the ch. 383 rate-schedule outcome (§§383-66/68).

## Worked examples

### Example 1: employer with one employee earning $1,200/week (hypothetical client facts), TDI employee contribution at the statutory cap

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

(The 0.5% cap is the confirmed §392-43 sentence; the wage is hypothetical.)

### Example 2: PREA coverage trigger at the confirmed 2026 minimum wage ($16.00 per hour per HRS §387-2)

```oa-check
name: HI PREA monthly wage trigger
inputs:
  minimum_wage: 16.00
  multiplier: 86.67
steps:
  - monthly_trigger: minimum_wage * multiplier
expected:
  monthly_trigger: 1386.72
```

(Both inputs are confirmed figures: 86.67 from §393-11 and $16.00 from §387-2.)

## Ask the client first

1. Are UI quarterly contribution/wage reports filed for every Hawaii payroll, including remote employees working in Hawaii?
2. Is TDI coverage via the state plan or an approved private plan -- and is the employee contribution at or under 0.5% of weekly wages?
3. Does every regular employee at or above 86.67 × the minimum wage have qualifying PREA coverage? (At the §387-2 minimum wage of $16.00 per hour beginning January 1, 2026, the Example 2 oa-check computes the monthly trigger at $1,386.72.)
4. Any exemption applications on file (ch. 393-17) and still valid?
5. What is the employer's current experience rating and the current taxable wage base (not published in the archived sources -- see Not yet confirmed below)?

## Sources

| Source | URL | Read on |
|---|---|---|
| HRS ch. 383 table of contents (unemployment insurance section map) | https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0383/HRS_0383-.htm | 2026-10-28 |
| HRS §392-43 (TDI contribution cap 0.5%, wage-base formula, eligibility screen) | https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0392/HRS_0392-0043.htm | 2026-10-28 |
| HRS §393-11 (PREA coverage trigger: 86.67 × minimum hourly wage) | https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0393/HRS_0393-0011.htm | 2026-10-28 |
| HRS ch. 392 table of contents (TDI structure) | https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0392/HRS_0392-.htm | 2026-10-28 |
| HRS ch. 393 table of contents (PREA structure, penalty sections) | https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0393/HRS_0393-.htm | 2026-10-28 |
| HRS §387-2 (minimum wage: $16.00 per hour beginning January 1, 2026) | https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0387/HRS_0387-0002.htm | 2026-10-28 |
| DLIR Unemployment Insurance Division (division contact/claims structure) | https://labor.hawaii.gov/ui/ | 2026-10-28 |

Not yet confirmed: the current UI taxable wage base and contribution-rate ranges (the archived DLIR page carries claims-office information, not the rate schedules); rates for the UI special assessments (§§383-61.5, 383-129, 383-131); the current TDI dollar wage base published annually by the director under §392-43(b)(2); the §393-13 employee premium-share cap; UI/TDI/PREA penalty percentages (§§383-73, 383-143, 392-42.5, 392-47, 393-33/393-34, 393-24); the current UI reporting calendar; and the §392-4 place-of-performance text. Each was flagged in v0.2 and has not been tied to an archived primary source, so no figure for them is asserted here.

<!-- openaccountants-cta-block -->

---

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
