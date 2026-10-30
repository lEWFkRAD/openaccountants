---
name: ia-social-contributions
description: >
  Use this skill whenever asked about Iowa employer social contributions
  for tax year 2026 -- unemployment insurance under Iowa Code ch. 96:
  the any-quarter coverage test, employer-only contributions (§96.15 bars
  wage deductions to fund them), 1%/month late-payment interest, the
  0.1%-0.5% delinquent-report penalty ladder with a $35 minimum, the 50%
  willful-fraud contribution penalty, and the July 1 rate computation date.
  Trigger on "Iowa unemployment tax", "Iowa UI", "Iowa workforce
  development", "Iowa employer contributions", "96.14", "96.15". Corrected
  2026-10-28 against archived Iowa Code 2026 statute text.
jurisdiction: US-IA
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ia-payroll-withholding
---

# Iowa social contributions, tax year 2026

> **Source-cited draft.** Built from Iowa Code §§96.1A, 96.8, 96.9, 96.14, 96.15 and 96.16 (Iowa Legislature, Iowa Code 2026), read on 2026-10-28. No accountant has reviewed it. Do not file, pay, amend, or take a tax position from it without review by a qualified Iowa professional.

Tax year: calendar-year contributions. Authority: Iowa Workforce Development. Currency: US dollars. Covers Iowa unemployment-insurance employer contributions.

See also: `ia-payroll-withholding`.

## Who this applies to

- **Covered employers (§96.1A(14)(a)):** for any calendar year after December 31, 2018, "'Employer' means ... any employing unit which in any calendar quarter in either the current or preceding calendar year paid wages for service in employment" -- Iowa has no dollar/employee-count threshold for ordinary employers. **Agricultural** employers: covered when wages for agricultural labor reach "$20,000 or more" in a quarter, or with "ten or more individuals" employed on 20 different days in different weeks (§96.1A(14)(b)). **Domestic-service** employers: covered on "$1,000 or more" cash in a quarter (§96.1A(14)(d) area).
- "Employing unit" includes "any individual or organization ... which has or subsequent to January 1, 1936, had in its employ one or more individuals performing services for it within this state"; multi-establishment employers are treated as a single unit (§96.1A(15)).
- Once covered, the unit is subject for the whole calendar year: voluntary termination requires filing "prior to the fifteenth day of February of that year" when the prior year's liability tests were not met (§96.8(2)).
- **Employee contribution: none.** "Any agreement by any individual in the employ of any person or concern to pay all or any portion of an employer's contributions ... shall be void. No employer shall directly or indirectly make or require or accept any deduction from wages to finance the employer's contributions"; violation "shall, for each offense, be guilty of a serious misdemeanor" (§96.15(1)).

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Coverage | any-quarter wages test (post-2018); ag $20,000/quarter or 10 workers × 20 days; domestic $1,000/quarter | §96.1A(14) |
| Rate computation date | "The computation date for contribution rates shall be July 1 of that calendar year preceding the calendar year with respect to which such rates are to be effective." | §96.1A(7) |
| Wage base / 2026 rate ranges | set administratively by Iowa Workforce Development | Not yet confirmed |

## The taxable base

- Contributions run on wages paid for insured employment; rates are experience-rated from the July 1 computation date (§96.1A(7)).
- The unemployment compensation fund "shall consist of: a. All contributions collected under this chapter, b. Interest earned upon any moneys in the fund" (§96.9(1)).

## Deadlines and filing

- Quarterly contribution and wage reports: due "in the manner and within the time required by this chapter and the rules of the department" (§96.14(2)); the department's published report calendar is listed under Not yet confirmed.
- Rate notices: computed as of the July 1 computation date for rates effective the following calendar year (§96.1A(7)).
- Coverage termination election: filed prior to February 15 (§96.8(2)).

## Penalties and interest

- **Interest:** "Any employer who fails to pay any contribution ... shall pay to the department in addition to the contribution, interest on the contribution at the rate of one percent per month and one-thirtieth of one percent for each day or fraction thereof computed from the date upon which the contribution should have been paid" (§96.14(1)).
- **Delinquent/insufficient report penalty (§96.14(2)(c)-(d)):** the penalty "shall be computed based on total wages in the period for which the report was due" -- 0.1% for days 1–60, 0.2% for 61–120, 0.3% for 121–180, 0.4% for 181–240, 0.5% for 241 or over; "A penalty shall not be less than thirty-five dollars for each delinquent or insufficient report." The insufficient-report penalty is "in addition to any penalty incurred for a delinquent report where the delinquent report is also insufficient" (§96.14(2)(b)).
- **Willful fraud:** an employer that "willfully failed to pay any contribution ... with intent to defraud the department ... shall in addition ... pay a contribution equal to fifty percent of the amount of such contribution" (§96.14(2)(e)); a dishonored payment also draws a $30 fee (§96.14(2)(f)).
- **Benefit fraud by individuals:** a person making a false statement to obtain benefits "is guilty of a fraudulent practice as defined in sections 714.8 through 714.14" (§96.16(1)).

## Cross-border points

- Out-of-state employers with workers performing services in Iowa are "employing units" under §96.1A(15); the fund may administer reciprocal arrangements with other states (§96.9, ch. 96 collection comity provisions).
- Multi-state employers: Iowa experience rating follows Iowa payroll history; the agricultural coverage tests are quarter-based and can flip mid-year (§96.1A(14)(b)).
- Iowa's remote-work UI coverage follows the same one-or-more-individuals-performing-services-in-state test (§96.1A(15)).

## Worked examples

Hypothetical employer owes $8,000 of Q1 contributions, paid 3 months late:

```oa-check
name: IA UI late interest
inputs:
  contribution: 8000
  months_late: 3
  monthly_rate: 0.01
steps:
  - interest: contribution * monthly_rate * months_late
expected:
  interest: 240.00
```

(The monthly component only; the confirmed §96.14(1) rate is 1% per month plus one-thirtieth of 1% per day, which adds a small further amount on the stated hypothetical facts.)

Hypothetical wage report of $60,000 total wages filed 75 days late:

```oa-check
name: IA UI delinquent report penalty
inputs:
  total_wages: 60000
  rate_61_120: 0.002
  minimum: 35
steps:
  - computed: total_wages * rate_61_120
  - penalty: max(computed, minimum)
expected:
  computed: 120.00
  penalty: 120.00
```

(75 days falls in the confirmed 61–120-day 0.2% bracket; the $35 minimum applies per report (§96.14(2)(d)).)

## Ask the client first

- Are quarterly wage reports filed on time even with zero wages -- the $35 minimum penalty applies per report (§96.14(2)(d))?
- Any remote or seasonal workers whose Iowa weeks create UI coverage mid-year (§96.1A(14))?
- Is anyone deducting UI costs from wages -- void and a serious misdemeanor under §96.15(1)?
- Has the July 1 rate recomputation been checked for protestable benefit charging (§96.1A(7))?

## Sources

| Source | URL | Read on |
|---|---|---|
| Iowa Code §96.1A (definitions; coverage tests; computation date) | https://www.legis.iowa.gov/docs/code/96.1A.pdf | 2026-10-28 |
| Iowa Code §96.8 (coverage period; voluntary termination) | https://www.legis.iowa.gov/docs/code/96.8.pdf | 2026-10-28 |
| Iowa Code §96.9 (unemployment compensation fund) | https://www.legis.iowa.gov/docs/code/96.9.pdf | 2026-10-28 |
| Iowa Code §96.14 (interest; penalty ladder; fraud penalty) | https://www.legis.iowa.gov/docs/code/96.14.pdf | 2026-10-28 |
| Iowa Code §96.15 (employer-only contributions; wage deductions void) | https://www.legis.iowa.gov/docs/code/96.15.pdf | 2026-10-28 |
| Iowa Code §96.16 (fraudulent benefit claims) | https://www.legis.iowa.gov/docs/code/96.16.pdf | 2026-10-28 |

Not yet confirmed: the 2026 UI taxable wage base and contribution-rate ranges (set administratively; the Iowa Workforce Development unemployment-insurance pages returned 403 when archived); the department's published quarterly report due dates; whether Iowa imposes any state disability insurance or employer health-coverage mandate (no separate statute chapter was located this run, but absence is not confirmed from archived text); the §96.21 federal-credit termination clause cited in v0.2 (§96.21 not archived).

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
