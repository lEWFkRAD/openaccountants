---
name: mn-social-contributions
description: >-
  Use when a Minnesota employer needs the 2026 state social-contribution
  picture: PFML family and medical leave premiums under M.S. 268B.14 (0.7%
  both-programs employer rate, 50% employee deduction floor, small-employer
  relief), plus UI and the MinnesotaCare provider tax context. Trigger on
  Minnesota paid leave premium, 268B.14, 0.7 percent, small employer 25
  percent, MinnesotaCare 0.7. Source-cited draft; statute verified 2026-10-25.
jurisdiction: US-MN
category: social
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.2
---

# Minnesota social contributions (PFML + MinnesotaCare)

## Who this applies to


- Minnesota employers in covered employment under the family and medical leave insurance program (M.S. 268B.14 — <https://www.revisor.mn.gov/statutes/cite/268B.14>, 200 with statute text on 2026-10-25).
- Covered employees, through the wage-deduction share of premiums (M.S. 268B.14 subd. 4, read 2026-10-25).
- Health-care providers for the MinnesotaCare provider tax (M.S. 290A.03/290A.06 — gross-revenue provider tax; the 0.7% provider rate is corroborated by the `mn-payroll` skill; the 290A.03 rate text renders via JavaScript and is not yet confirmed).
- Out of scope: federal FICA/FUTA (skills/federal); UI mechanics in the payroll lane.

## Rates, bands and thresholds


Family and medical leave premiums (M.S. 268B.14, read 2026-10-25):

| Item | Rule (statute text verified 2026-10-25) |
|---|---|
| Employer premium rate from 1 Jan 2026, both programs | **0.7%** of taxable wages (subd. 6(1)) |
| Medical-only with approved private family plan | 0.4% (subd. 6(2)) | (not yet confirmed)
| Family-only with approved private medical plan | 0.3% (subd. 6(3)) | (not yet confirmed)
| Employer minimum share | at least **50%** of annual premiums; employees pay the remainder via wage deduction (subd. 4) |
| Small employers (≤30 employees, avg wage ≤150% of state average) | premium rate = **75% of the standard rate**; employer pays at least **25%**, employees the rest (subd. 5a) |
| Premium timing | quarterly, computed from the wage detail report; due by the last day of the month after quarter end (subd. 1(a)) |
| Rate adjustments | commissioner adjusts annually by 31 July for the following year (subd. 7) |

- **MinnesotaCare provider tax:** 0.7% of gross revenue for qualifying health-care providers (mn-payroll corroboration; statute rate text not yet confirmed — 290A.03 JS-rendered 2026-10-25).

## The taxable base


- PFML: "taxable wages" as defined in chapter 268B (UI-covered wages) (M.S. 268B.14 subd. 1(a), read 2026-10-25).
- MinnesotaCare: gross revenue from patient care of qualifying providers (mn-payroll, read 2026-10-25).

## Deadlines and filing


- PFML premiums: quarterly, received by the department on or before the last day of the month following the calendar quarter (M.S. 268B.14 subd. 1(a), read 2026-10-25).
- Wage detail report drives the premium computation (subd. 1(a), read 2026-10-25).

## Penalties and interest


- PFML late premiums: chapter 268B penalty/interest overlay — exact schedule not yet confirmed (not machine-verified 2026-10-25).
- UI penalties: payroll lane (mn-payroll, read 2026-10-25).

## Cross-border points


- PFML applies to covered employment for Minnesota work regardless of employee residence.
- Employers with approved private plans can substitute for one program (0.4%/0.3% rates above) (M.S. 268B.14 subd. 6, read 2026-10-25). (not yet confirmed)
- No state pension contribution; FICA/FUTA federal.

## Worked examples


**Example 1 — standard employer, both programs.** An employer with 50 employees pays USD 1,200,000 of taxable wages in a year. Premium: 1,200,000 × 0.007 = 8,400. Employer must pay at least 50%: 4,200; employees may bear up to 4,200 via wage deductions.

```oa-check
name: mn pfml standard employer
inputs:
  wages: 1200000
  rate: 0.007
  employer_floor: 0.5
steps:
  - premium: wages * rate
  - employer_min: premium * employer_floor
  - employee_max: premium - employer_min
expected:
  premium: 8400.00
  employer_min: 4200.00
  employee_max: 4200.00
```

**Example 2 — small-employer relief.** A qualifying small employer (28 employees) on the same 1,200,000 wage base: reduced rate = 0.7% × 75% = 0.525%; premium = 1,200,000 × 0.00525 = 6,300. Employer pays at least 25%: 1,575; employees up to 4,725.

```oa-check
name: mn pfml small employer
inputs:
  wages: 1200000
  std_rate: 0.007
  relief: 0.75
  employer_floor: 0.25
steps:
  - small_rate: std_rate * relief
  - premium: wages * small_rate
  - employer_min: premium * employer_floor
  - employee_max: premium - employer_min
expected:
  small_rate: 0.00525
  premium: 6300.00
  employer_min: 1575.00
  employee_max: 4725.00
```

## Ask the client first


- Employee count and average wage (small-employer eligibility: ≤30 employees and avg wage ≤150% of state average). (not yet confirmed)
- Whether they hold an approved private plan for either program (0.4%/0.3% rates). (not yet confirmed)
- Whether they are a qualifying health-care provider (MinnesotaCare overlay).

## Sources

| Source | Read on |
| --- | --- |
| M.S. 290A.03 (MinnesotaCare): <https://www.revisor.mn.gov/statutes/cite/290A.03> — page archived; rate text JS-rendered, figures not readable from archive | 2026-10-28 |
| `mn-payroll` skill (UI, MinnesotaCare) — internal corroboration | 2026-10-25 |

Not yet confirmed: the 0.7% MinnesotaCare provider-tax rate text (290A.03 archive is JS-rendered); the chapter 268B penalty/interest schedule.
## Talk to a verified accountant



