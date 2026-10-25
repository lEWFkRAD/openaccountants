---
name: ma-social-contributions
description: >-
  Use when a Massachusetts employer or covered individual needs the 2026
  state social-contribution picture: PFML paid family and medical leave
  contribution rates, the employer/employee split, small-employer relief, and
  how FICA/FUTA/UI sit alongside. Trigger on PFML contribution, 0.88%,
  family leave Massachusetts, medical leave split, DFML employer.
  Source-cited draft; rate page verified 2026-10-25.
jurisdiction: US-MA
category: social
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# Massachusetts social contributions (PFML)

## 1. Who this applies to

- Massachusetts employers with 25 or more covered individuals: mandatory PFML contributions ([DFML contribution rates page](https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers), read 2026-10-25).
- Employers with fewer than 25 covered individuals: contributions are optional; if they do not contribute, covered individuals may still self-contribute (DFML page, read 2026-10-25).
- Covered individuals (W-2 employees and, for some programs, 1099-MISC contractors) whose wages are eligible wages under DFML rules.
- Out of scope: federal FICA/FUTA (skills/federal); Massachusetts Unemployment Insurance, an employer-only tax covered by the withholding/payroll lane (see §6).

## 2. Core rules and rates

2026 rates for employers with 25+ covered individuals ([DFML page](https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers), read 2026-10-25):

| Piece | Rate on eligible wages | Employee-withholdable | Employer share |
|---|---|---|---|
| Total PFML contribution | 0.88% | — | — |
| Family leave | 0.18% | up to 100% (0.18%) | 0% |
| Medical leave | 0.70% | up to 40% (0.28%) | 60% (0.42%) |

- The employer may allocate the family-leave piece entirely to covered individuals' wage withholdings; the medical piece may be shifted to employees only up to 40% of that piece.
- Rates are set by the DFML for each year; confirm the current-year table on the DFML page before payroll changes (read 2026-10-25).

## 3. Base

- "Eligible wages" = W-2 gross wages (plus certain 1099-MISC contractor amounts for the family-leave program) up to the Social Security wage base; the DFML page defines the current base (read 2026-10-25).
- Contributions are computed per pay period on eligible wages, remitted with the quarterly DFML filing.

## 4. Deadlines

- Contributions are withheld/remit each pay period; employers file and pay quarterly to DFML (DFML employer guidance, read 2026-10-25).
- Annual rate changes take effect 1 January; DFML publishes the next year's rates in advance (DFML page, read 2026-10-25).

## 5. Penalties and interest

- Late/underpaid PFML contributions attract DFML penalties and interest; the schedule is published in DFML employer guidance — **needs-sources** (mass.gov guidance pages 404 from the drafting environment on 2026-10-25). Treat the exact penalty table as unverified until re-checked.

## 6. Cross-border and interaction

- PFML is a state social-insurance contribution, not income tax: it is withheld on wages for covered employment irrespective of the employee's residency, so nonresident Massachusetts workers see PFML withholdings too (DFML page, read 2026-10-25).
- Massachusetts Unemployment Insurance is employer-only (no employee contribution) — a social cost of employment but not an employee-side contribution; see the payroll lane.
- No state pension or disability contribution beyond PFML; FICA/FUTA are federal.

## 7. Worked examples

**Example 1 — 2026 PFML split on a mid-size employer.** An employer with 30 covered individuals pays USD 500,000 of eligible wages in the quarter-year base. Total contribution: 500,000 × 0.88% = 4,400. Family piece: 500,000 × 0.18% = 900 (fully withholdable). Medical piece: 500,000 × 0.70% = 3,500; employee-withholdable 40% = 1,400; employer 60% = 2,100. Employer minimum cash cost = 2,100.

```oa-check
name: ma pfml 2026 split
inputs:
  wages: 500000
steps:
  - family: wages * 0.0018
  - medical: wages * 0.007
  - med_employee: medical * 0.4
  - med_employer: medical * 0.6
  - total: family + medical
expected:
  family: 900.00
  medical: 3500.00
  med_employee: 1400.00
  med_employer: 2100.00
  total: 4400.00
```

**Example 2 — small-employer relief.** An employer with 20 covered individuals elects not to contribute: employer PFML cost = 0; covered individuals may self-contribute the full 0.88% (900 + 3,500 = 4,400 on the same 500,000 wage base if they opt in).

```oa-check
name: ma pfml small employer opt-in
inputs:
  wages: 500000
  employer_share: 0
steps:
  - full_rate: wages * 0.0088
  - employer_cost: full_rate * employer_share
expected:
  full_rate: 4400.00
  employer_cost: 0.00
```

## 8. Ask the client first

- Headcount of covered individuals (the 25 threshold flips the obligation).
- Whether any 1099-MISC contractors are in the family-leave base.
- Whether the employer already withholds the maximum family-leave piece (payroll config question, not a legal one).

## 9. Sources

- DFML PFML contribution rates for employers: <https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers> — 200 with content, read 2026-10-25 (as_of 2026 rates).
- DFML employer guidance / penalty schedule — **needs-sources** (mass.gov 404 site-wide on 2026-10-25).
- Federal FICA/FUTA overlay: skills/federal.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
