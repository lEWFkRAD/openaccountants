---
name: ky-payroll
description: Use this skill whenever asked about Kentucky employer payroll withholding for tax year 2026 -- the 4% (2025) / 3.5% (2026) flat individual income tax withholding, Form K-1 filing frequencies and due dates under 103 KAR 18:150, Form K-3 annual reconciliation, and pointers to unemployment insurance (KRS 341) and the local occupational license tax system. Trigger on "Kentucky withholding", "Kentucky payroll", "Form K-1", "Form K-3", "Kentucky K-4". ALWAYS load us-tax-workflow-base first.
version: 3.0
jurisdiction: US-KY
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kentucky payroll withholding, tax year 2026

> **Source-cited draft.** Built from KRS 141.020, 103 KAR 18:150, the DOR Employer Payroll Withholding page, and DOR news releases, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

| Field | Value |
| --- | --- |
| Jurisdiction | Kentucky (US-KY) |
| Tax authority | [Kentucky Department of Revenue (DOR)](https://revenue.ky.gov/) |
| Withholding rate | 4% for tax year 2025; 3.5% for tax year 2026 |
| Employer returns | Form K-1 (periodic), Form K-3 (annual reconciliation) |
| Regulation | 103 KAR 18:150 (employer's withholding reporting requirements) |

## Who this applies to

Every Kentucky employer (or employer with Kentucky-source wages). The DOR Employer Payroll Withholding page states: "Kentucky Revised Statute Chapter 141 requires employers to withhold income tax for both residents and nonresidents employees (unless exempted by law). Employers must withhold the income tax of the employees receiving 'wages' as defined in Section 3401(a) of the Internal Revenue Code." All employer filing frequencies are required to electronically file and pay the income tax withheld per 103 KAR 18:150 (DOR page).

## Rates, bands and thresholds

- **Individual income tax withholding rates (KRS 141.020(2)):** "For taxable years beginning on or after January 1, 2024, but before January 1, 2026, the tax shall be four percent (4%) of net income. For taxable years beginning on or after January 1, 2026, the tax shall be three and one-half percent (3.5%) of net income." The DOR withholding page states: "The Kentucky Withholding Tax rate will be 3.5% for tax year 2026."
- **Withholding computation:** the annual standard deduction ($3,270 for 2025 per the Form 740 instructions; $3,360 for 2026 per the DOR news release) is reflected in the DOR withholding tables/calculator, and the withholding rate is applied to wages after that allowance. For 2026 payrolls use the 3.5% rate and the 2026 tables; for 2025 payrolls, 4% and the 2025 tables.

### Form K-1 filing frequency (lookback-period thresholds, 103 KAR 18:150)

| Lookback-period withholding | Frequency | Return and due date |
| --- | --- | --- |
| Less than $400 | Annual | Form K-3 "filed and paid on or before the last day of the month following the close of the calendar year in which the tax was withheld (January 31)" |
| $400 or more, but less than $2,000 | Quarterly | Form K-1 "filed and paid on or before the last day of the month following the close of each of the first three (3) quarters of the calendar year (April 30, July 31, and October 31)", with K-3 for the fourth quarter by January 31 |
| $2,000 or more, but less than $50,000 | Monthly | Form K-1 for each month "filed and paid on or before the 15th day of the following month for each of the first eleven (11) months of the calendar year", with K-3 for December by January 31 |
| $50,000 or more | Twice monthly | Form K-1 for wages of the 1st through the 15th "reported and paid on or before the 25th day of that month"; the second-half remittance follows the regulation's schedule for the remainder of the month; K-3 closes the year by January 31 |
| $50,000 or more AND average monthly withholding more than $25,000 | Electronic funds transfer | "Any employer who withheld income tax during the lookback period of $50,000 or more and whose average monthly income tax withheld during the lookback period is more than $25,000 shall pay the tax withheld by electronic funds transfer" |

### Unemployment insurance (payroll side)

Kentucky UI contributions are employer-only, experience-rated under KRS 341.270 (new-employer rate 2.7%; construction new employers at the schedule maximum per KRS 341.272; a 0.075% rate reduction applies through 12/31/2026 under KRS 341.243 when the trust-fund condition holds). See `ky-social-contributions` for the full schedule and the wage-base mechanics under KRS 341.030.

## The taxable base

Wages as defined in IRC §3401(a) paid to employees for Kentucky-source work (resident employees: all wages; nonresident employees: Kentucky-source wages). Local occupational license taxes are separate local taxes, not state withholding; the 740 instructions warn "Local government occupational, license or income tax must not be included on line 31(a)" of the individual return.

## Deadlines and filing

- Filing frequency is set by the lookback-period thresholds above (103 KAR 18:150). Re-determine annually.
- Form K-3 (annual reconciliation) is due January 31 following the calendar year, reconciling total Kentucky wages and withholding to Forms W-2.
- Quarterly deposits and returns: per the frequency table above.
- Electronic filing and payment are required for all frequencies (DOR page: "All employer filing frequencies are required to electronically file and pay the income tax withheld per 103 KAR 18:150").

## Penalties and interest

- Late payment and failure to withhold/collect: "Two (2) percent of the total tax due for each 30 days or fraction thereof that a payment is late. The maximum penalty is 20 percent of the tax not timely withheld, collected or paid. The minimum penalty is $10" (DOR Penalties, Interest and Fees page).
- Late filing: 2% per 30 days or fraction, capped at 20%, minimum $10 ($100 after a jeopardy assessment) (same page).
- Interest on unpaid tax: 10% for calendar year 2025, 9% for calendar year 2026, under KRS 131.183(2)(a)2 (DOR interest notices).
- The two late-filing and late-payment penalties can both apply to the same period; the underpayment-of-estimated-tax penalty is computed separately per installment.

## Cross-border points

- Nonresident employees: employers withhold on Kentucky-source wages; nonresidents file Form 740-NP. Nonresident partners/members of Kentucky pass-through entities are covered by the entity withholding rules on Form 740NP-WH (see `ky-cross-border`).
- Reciprocal agreements with neighboring states and the certificate of non-residence (Form 42A809) are asserted in prior drafts but were not tied to an archived primary source this run -- verify with the DOR before honoring an exemption (see Not yet confirmed).
- Kentucky residents working in other states claim the KRS 141.070 credit for tax paid to the other state on Form 740.

## Worked examples

### Example 1: 2026 monthly withholding (hypothetical facts)

An employee's Kentucky wages are $5,000 per month. Withholding at the 2026 flat rate: $5,000 × 3.5% = $175. (The DOR withholding tables also reflect the standard-deduction allowance; this is the flat-rate illustration.)

```oa-check
name: KY 2026 monthly withholding at 3.5 percent
inputs:
  wages: 5000
  rate: 0.035
steps:
  - withheld: wages * rate
expected:
  withheld: 175.00
```

### Example 2: same wages on a 2025 payroll (hypothetical facts)

$5,000 × 4% = $200 per month under the 2025 rate.

```oa-check
name: KY 2025 monthly withholding at 4 percent
inputs:
  wages: 5000
  rate: 0.04
steps:
  - withheld: wages * rate
expected:
  withheld: 200.00
```

### Example 3: filing-frequency determination (hypothetical facts)

An employer withheld $1,200 of Kentucky income tax during the lookback period. That is $400 or more but less than $2,000, so the employer files quarterly Form K-1 returns (April 30, July 31, October 31) with the K-3 closing the year by January 31.

```oa-check
name: KY K-1 frequency for 1200 lookback
inputs:
  lookback: 1200
steps:
  - over400: max(lookback - 400, 0)
  - over2000: max(lookback - 2000, 0)
  - over50000: max(lookback - 50000, 0)
expected:
  over400: 800.00
  over2000: 0.00
  over50000: 0.00
```

### Example 4: UI contribution on new-employer rate (hypothetical facts)

A new non-construction employer at 2.7% with $10,000 of covered wages in the quarter owes $10,000 × 2.7% = $270 (see `ky-social-contributions` for the full rate schedule).

```oa-check
name: KY UI contribution at 2.7 percent
inputs:
  wages: 10000
  rate: 0.027
steps:
  - tax: wages * rate
expected:
  tax: 270.00
```

## Ask the client first

- Which tax year(s) do the pay dates fall in? 4% applies through the last 2025 payroll; 3.5% from the first 2026 payroll.
- Is the employer registered with DOR for withholding and with the Office of Unemployment Insurance?
- What was last year's (lookback-period) total Kentucky withholding -- it sets the filing frequency?
- Are any employees nonresidents working in Kentucky, or Kentucky residents working in reciprocal states?
- Are local occupational license taxes in force at each work site (checked with the locality, not from memory)?

## Sources

| Source | URL | Read on |
|---|---|---|
| KRS 141.020 (individual income tax rates; 4% 2024-2025, 3.5% 2026) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.020 | 2026-10-28 |
| 103 KAR 18:150 employer's withholding reporting requirements (frequency thresholds and due dates; EFT rule) | https://revenue.ky.gov/DOR%20Training%20Materials/103%20KAR%2018.150.%20Employer%27s%20withholding%20reporting%20requirements.pdf | 2026-10-28 |
| DOR Employer Payroll Withholding page ("The Kentucky Withholding Tax rate will be 3.5% for tax year 2026"; electronic filing requirement) | https://revenue.ky.gov/Business/Pages/Employer-Payroll-Withholding.aspx | 2026-10-28 |
| KRS 141.081 (standard deduction; inflation adjustment) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.081 | 2026-10-28 |
| DOR news release: 2026 standard deduction $3,360 | https://revenue.ky.gov/News/Pages/Kentucky-DOR-Announces-2026-Standard-Deduction.aspx | 2026-10-28 |
| DOR 2025 Form 740 instruction packet (2025 standard deduction $3,270; local occupational tax not on line 31(a)) | https://revenue.ky.gov/Forms/740%20Packet%20Instructions.pdf | 2026-10-28 |
| DOR Penalties, Interest and Fees page (2%/20%/$10 penalties) | https://revenue.ky.gov/Collections/Pages/Penalties-Interest-and-Fees.aspx | 2026-10-28 |
| DOR news release: interest rate update for 01-01-25 (10%) | https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-25.aspx | 2026-10-28 |
| DOR news release: interest rate update for 01-01-26 (9%) | https://revenue.ky.gov/News/Pages/Tax-Interest-Rate-Update-for-01-01-26.aspx | 2026-10-28 |
| KRS 341.270 (UI contribution rates; 2.7% new-employer rate) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS341.270 | 2026-10-28 |
| KRS 341.243 (0.075% UI rate reduction through 12/31/2026) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS341.243 | 2026-10-28 |
| KRS 141.070 (credit for tax paid to other states) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.070 | 2026-10-28 |

Not yet confirmed: the local occupational license tax system -- v0.2 listed rates for Louisville Metro (1.45%/0.75% school), Lexington-Fayette (2.25%, $148,000 cap), Covington, Newport, Florence, Bowling Green, Owensboro and several counties, plus Form OL-3 mechanics; none of these local rates, caps or forms were tied to archived primary sources (local ordinances are not archived), so no local rate may be quoted -- check each locality's current published ordinance; the reciprocal-agreement list (Ohio, Indiana, Illinois, Michigan, Virginia, West Virginia) and Form 42A809 mechanics (agreements and form instructions not archived -- verify with DOR before honoring an exemption); the Form K-4 employee withholding certificate mechanics (form instructions not archived); the v0.2 "construction-industry employee presumption under KRS 341.123" -- no KRS 341.123 exists in the archived chapter 341 listing, so that presumption is removed (the construction new-employer UI rate in KRS 341.272 is the confirmed construction-industry rule); final-pay timing under KRS 337.055 and liquidated damages under KRS 337.385 (statutes not archived this run); the mandatory-EFT threshold of $1,000 average monthly withholding asserted in v0.2 -- the archived 103 KAR 18:150 states the EFT rule as lookback $50,000 or more and average monthly over $25,000, which supersedes it; the 2025 interest rate on deficiencies asserted as 8% in v0.2 -- the DOR's 2025 notice sets the base "tax interest rate" at 8% but the rate charged on unpaid tax at 10%, which supersedes it.

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
