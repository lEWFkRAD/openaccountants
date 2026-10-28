---
name: ia-social-contributions
description: >
  Use this skill whenever asked about Iowa employer social contributions
  for tax year 2026 — unemployment insurance under Iowa Code ch. 96:
  coverage tests, employer-only contributions (§96.15 bars wage deductions
  to fund them), 1%/month late-payment interest, the 0.1%–0.5% delinquent-
  report penalty ladder with $35 minimum, and the July 1 rate computation
  date. Iowa has no state disability insurance and no employer health-
  coverage mandate. Trigger on "Iowa unemployment tax", "Iowa UI",
  "Iowa workforce development", "Iowa employer contributions", "96.14",
  "96.15". Source-cited draft; Iowa Code 2026 text read from
  legis.iowa.gov 2026-10-27.
jurisdiction: US-IA
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ia-payroll-withholding
---

# Iowa social contributions v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-27. Iowa's employer social-contribution layer is a single regime: **unemployment insurance** under Iowa Code ch. 96, administered by the workforce development department. Iowa has **no state temporary-disability program and no state employer health-coverage mandate** (ACA rules only). Statute text read directly from Iowa Code 2026 PDFs at legis.iowa.gov 2026-10-27. **Source status:** coverage tests (§96.1A), employer-only contribution rule (§96.15), interest and penalty ladder (§96.14), fund structure (§96.9), and the July 1 computation date (§96.1A(7)) verified from statute text; the **UI taxable wage base and 2026 contribution-rate ranges** are set administratively and live on workforce.iowa.gov — **needs-sources**.

## 2. Who applies

- **Covered employers (§96.1A(14)(a), text read 2026-10-27):** for calendar years after December 31, 2018, **any employing unit that paid wages for service in employment in any calendar quarter in the current or preceding calendar year** — Iowa has no dollar/employee-count threshold for ordinary employers (the old $1,500/20-week federal-style test was removed). **Agricultural** employers: **$20,000+ wages in a quarter** or 10+ workers on 20 different weeks; **domestic-service** employers: **$1,000+ cash in a quarter** (§96.1A(14)-(15), text read 2026-10-27).
- "Employing unit" = any individual or organization with **one or more** individuals performing services within Iowa; multi-establishment employers are treated as a single unit; statutory contractor/subcontractor deeming applies (§96.1A(15), text read 2026-10-27).
- Subject for the **whole calendar year** once covered within it; voluntary termination requires filing before **February 15** if the prior year's liability tests were not met (§96.8, text read 2026-10-27).
- **Employee contribution: none.** Any agreement to have an employee pay any portion of the employer's UI contribution is **void**, and deducting it from wages is a serious misdemeanor (§96.15(1), text read 2026-10-27).

## 3. Mechanics and rates

| Item | Rule | Source |
|---|---|---|
| Contribution base | taxable wages per employee per year — 2026 wage base set administratively | **needs-sources** (workforce.iowa.gov) |
| Contribution rate | experience-rated; **computation date July 1** of the preceding year (§96.1A(7), text read 2026-10-27); "average annual taxable payroll" = 5-quarter average (§96.1A(2), text read 2026-10-27) | verified mechanics; rate ranges **needs-sources** |
| Fund | unemployment compensation fund; contributions + federal credits (§96.9, text read 2026-10-27) | verified |
| Federal credit | ch. 96 operates for FUTA credit; §96.21 termination clause if federal credit dies (text read 2026-10-27) | verified |
| TDI / health mandate | none in Iowa | absence confirmed from ch. 96 scope; no separate chapter located — flag |

## 4. Deadlines

- Quarterly contribution and wage reports: due last day of the month following each calendar quarter (standard UI calendar; the §96.14 penalty runs from "the time required by this chapter and the rules of the department" — exact published dates **needs-sources**).
- Rate notices: computed as of July 1 computation date, effective January 1 (§96.1A(7), text read 2026-10-27).
- Coverage termination election: before February 15 (§96.8(2), text read 2026-10-27).

## 5. Penalties and interest

- **Interest:** unpaid contributions accrue **1% per month plus 1/30 of 1% per day** from the due date (§96.14(1), text read 2026-10-27).
- **Delinquent/insufficient report penalty ladder (§96.14(2)(c), text read 2026-10-27):** on total wages for the period — days 1–60: 0.1%; 61–120: 0.2%; 121–180: 0.3%; 181–240: 0.4%; 241+: 0.5%. **Minimum $35 per report**; delinquent and insufficient penalties stack (§96.14(2)(b)).
- Willful failure to pay with intent to defraud: additional penalty under §96.14(2)(e) (text truncated at extraction — amount **needs-sources**).
- Fraudulent benefit claims by individuals: fraudulent practice under §§714.8–714.14 (§96.16(1), text read 2026-10-27).

## 6. Cross-border interactions

- Remote workers physically working in Iowa make the out-of-State employer an "employing unit" for Iowa UI; reciprocal benefit arrangements with other states are authorized (§96.20, text read 2026-10-27).
- Multi-State employers: Iowa experience rating follows Iowa payroll history; agricultural coverage tests are quarter-based and can flip mid-year (§96.1A(14), text read 2026-10-27).

## 7. Worked examples

Employer owes $8,000 of Q1 contributions, paid 90 days late:

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

(The daily 1/30% component adds a small amount on top; shown monthly for the bracket.)

Wage report of $60,000 total wages filed 75 days late:

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

## 8. Ask the client

- Are quarterly wage reports filed on time even with zero wages — the $35 minimum penalty applies per report?
- Any remote or seasonal workers whose Iowa weeks create UI coverage mid-year?
- Is anyone deducting UI costs from wages — void and a misdemeanor under §96.15?
- Has the July 1 rate recomputation been checked for protestable claims charging?

## Sources

1. Iowa Code §96.1A (definitions; coverage tests; computation date): https://www.legis.iowa.gov/docs/code/96.1A.pdf (200, text read 2026-10-27)
2. Iowa Code §96.8 (coverage period; termination): https://www.legis.iowa.gov/docs/code/96.8.pdf (200, text read 2026-10-27)
3. Iowa Code §96.9 (unemployment compensation fund): https://www.legis.iowa.gov/docs/code/96.9.pdf (200, text read 2026-10-27)
4. Iowa Code §96.14 (interest 1%/month; penalty ladder): https://www.legis.iowa.gov/docs/code/96.14.pdf (200, text read 2026-10-27)
5. Iowa Code §96.15 (employer-only contributions; wage deductions void): https://www.legis.iowa.gov/docs/code/96.15.pdf (200, text read 2026-10-27)
6. Iowa Code §96.16 (fraud offenses): https://www.legis.iowa.gov/docs/code/96.16.pdf (200, text read 2026-10-27)
7. Iowa Workforce Development UI: https://www.iowaworkforcedevelopment.gov/unemployment-insurance (403 this run — wage base and 2026 rate ranges **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Iowa UI questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
