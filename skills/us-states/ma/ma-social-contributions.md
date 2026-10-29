---
name: ma-social-contributions
description: >-
  Use when a Massachusetts employer or covered individual needs the 2026
  state social-contribution picture: PFML paid family and medical leave
  contribution rates, the employer/employee split, small-employer relief, and
  how FICA/FUTA/UI sit alongside. Trigger on PFML contribution, 0.88%,
  family leave Massachusetts, medical leave split, DFML employer.
  Source-cited; DFML rate page archived 2026-10-29.
jurisdiction: US-MA
category: social
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-29
version: 0.2
---

# Massachusetts social contributions (PFML)

## Who this applies to

- Massachusetts employers with 25 or more covered individuals: mandatory PFML contributions ([DFML contribution rates page](https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers), read 2026-10-28).
- Employers with fewer than 25 covered individuals: they must send an effective contribution rate of 0.46% of eligible wages; small employers are not required to pay the employer share of the medical leave contribution but may elect to cover some or all of the covered individuals' share (DFML page, read 2026-10-28).
- Covered individuals (W-2 employees and, for some programs, 1099-MISC contractors) whose wages are eligible wages under DFML rules.
- Out of scope: federal FICA/FUTA (skills/federal); Massachusetts Unemployment Insurance, an employer-only tax covered by the withholding/payroll lane (see Cross-border points).

## Rates, bands and thresholds

2026 rates for employers with 25 or more covered individuals ([DFML page](https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers), read 2026-10-28):

| Piece | Rate on eligible wages | Employee-withholdable | Employer share |
|---|---|---|---|
| Total PFML contribution | 0.88% | — | — |
| Family leave | 0.18% | up to 100% (0.18%) | 0% |
| Medical leave | 0.70% | up to 40% (0.28%) | 60% (0.42%) |

- The employer may allocate the family-leave piece entirely to covered individuals' wage withholdings; the medical piece may be shifted to employees only up to 40% of that piece.
- Employers with fewer than 25 covered individuals must send an effective contribution rate of 0.46% of eligible wages (no employer share of medical leave).
- Contribution rates are set annually for January 1–December 31; the new rate applies to wages earned on or after January 1 of each year.
- New legislation (Chapter 101 of the Acts of 2026) shifts employer contributions from medical leave to family leave effective January 1, 2027: for employers with 25+ covered individuals, up to 40% of the family leave contribution (0.28%) may be withheld with the employer contributing the remaining 60% (0.42%), and up to 100% of the medical leave contribution (0.18%) may be withheld (DFML page, read 2026-10-28).

## The taxable base

- "Eligible wages" is the DFML-defined base; individual contributions are capped by the Social Security taxable maximum (DFML page, read 2026-10-28).
- Contributions are computed per pay period on eligible wages, remitted with the quarterly DFML filing.

## Deadlines and filing

- Contributions are withheld/remit each pay period; employers file and pay quarterly to DFML.
- Annual rate changes take effect 1 January; DFML publishes the next year's rates in advance (DFML page, read 2026-10-28).

## Penalties and interest

- Late/underpaid PFML contributions attract DFML penalties and interest; the exact schedule is listed under Not yet confirmed below.

## Cross-border points

- PFML is a state social-insurance contribution, not income tax: it is withheld on wages for covered employment irrespective of the employee's residency, so nonresident Massachusetts workers see PFML withholdings too (DFML page, read 2026-10-28).
- Massachusetts Unemployment Insurance is employer-only (no employee contribution) — a social cost of employment but not an employee-side contribution; see the payroll lane.
- No state pension or disability contribution beyond PFML; FICA/FUTA are federal.

## Worked examples

Client facts (headcount, wages) are hypothetical; rates are the confirmed 2026 DFML rates above.

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

**Example 2 — small-employer relief.** An employer with 20 covered individuals elects not to contribute: employer PFML cost = 0; the employer still sends the effective 0.46% rate withheld from covered individuals (500,000 × 0.46% = 2,300 on the same hypothetical wage base).

```oa-check
name: ma pfml small employer opt-in
inputs:
  wages: 500000
  employer_share: 0
steps:
  - withheld_rate: wages * 0.0046
  - employer_cost: withheld_rate * employer_share
expected:
  withheld_rate: 2300.00
  employer_cost: 0.00
```

## Ask the client first

- Headcount of covered individuals (the 25 threshold flips the obligation).
- Whether any 1099-MISC contractors are in the family-leave base.
- Whether the employer already withholds the maximum family-leave piece (payroll config question, not a legal one).

## Sources

| Source | URL | Read on |
|---|---|---|
| DFML — PFML employer contribution rates and calculator (2026 and 2027 rate splits) | <https://www.mass.gov/info-details/family-and-medical-leave-contribution-rates-for-employers> | 2026-10-28 |

Not yet confirmed: the DFML penalty and interest schedule for late or underpaid PFML contributions (the mass.gov employer-guidance pages returned 403/404 from this environment on 2026-10-28/29); the exact definition of "eligible wages" beyond the Social Security cap noted on the DFML page; whether 1099-MISC contractor amounts enter the family-leave base (DFML coverage pages unreachable).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
