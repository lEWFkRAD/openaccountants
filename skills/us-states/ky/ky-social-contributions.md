---
name: ky-social-contributions
description: >
  Use this skill whenever asked about Kentucky employer social contributions for tax year 2026 -- unemployment insurance contributions under KRS chapter 341 (Office of Unemployment Insurance), the employer-only nature of the UI tax, the experience-rating schedules in KRS 341.270, the new-employer 2.7% rate, the 0.075% rate reduction under KRS 341.243, and the absence of state disability or paid-leave payroll taxes. Trigger on "Kentucky UI rate", "Kentucky SUTA", "Kentucky unemployment wage base", "Kentucky employer taxes", "Kentucky workers compensation requirement". ALWAYS load us-tax-workflow-base first.
version: 0.3
jurisdiction: US-KY
category: payroll
tax_year: 2026
last_updated: 2026-10-28
tier: 2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - ky-payroll
---

# Kentucky social contributions (UI + workers' comp), tax year 2026

> **Source-cited draft.** Built from KRS 341.270, 341.272, 341.030, 341.243, 341.614, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

Employers covered under KRS chapter 341 (the Office of Unemployment Insurance administers the program). The UI contribution is **employer-only** -- Kentucky employees pay no state UI tax. Workers' compensation insurance is required for most Kentucky employers under KRS chapter 342 (premiums are carrier-rated by class code; the statute text was not archived this run -- see Not yet confirmed). Kentucky has no state disability insurance and no state paid family/medical leave payroll tax.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Default employer rate | "each employer's contribution rate shall be three percent (3%). Effective for employers who become subject to this chapter on or after January 1, 1999 ... each employer's contribution rate shall be two and seven-tenths percent (2.7%)" | KRS 341.270(1) |
| Experience rating | Rates read from "Table A" schedules (Trust Fund Adequacy Rates; Schedules A–E) by the employer's reserve ratio; the applicable schedule is set each year from the trust fund balance on September 30. In Schedule A the table runs from 0.30% (reserve ratio 8.0% and over) to 9.00% (reserve ratio less than −8.0%) | KRS 341.270(3)–(4) |
| New-employer rate | 2.7% generally; "no subject employer's contribution rate shall be less than two and seven-tenths percent (2.7%)" until the employer has been subject for 12 consecutive calendar quarters | KRS 341.270(1)–(2) |
| Construction-industry new employers | Pay "the maximum rate of contributions payable under the rate schedule in effect for any given calendar year" until 12 consecutive quarters of employment | KRS 341.272(1) |
| Rate reduction in effect | "From October 1, 2018, to December 31, 2026, all rates otherwise established under KRS 341.270 and 341.272 shall be adjusted by subtracting seventy-five thousandths percent (0.075%) from each rate," but only if the trust fund balance exceeds its 12/31/2017 balance. From January 1, 2027 the subtraction is 0.0115% (secretary adjusts annually, not to exceed 0.025%) | KRS 341.243(4)–(5) |
| Interest-payment surcharge | When funds are insufficient: a surcharge of "twenty-two hundredths of one percent (0.22%) of the first nine thousand six hundred dollars ($9,600) in wages paid to each worker" (adjusted annually with the wage base) | KRS 341.614(2)(a) |
| Taxable wage base | Set under KRS 341.030: increases $300 each January 1 while the trust fund triggers are met, until the base reaches $12,000; the base does not increase in years the September 30 trust fund balance is at least $200,000,000 | KRS 341.030 |

## The taxable base

Covered wages paid to each worker up to the annual taxable wage base per employee (KRS 341.030 defines "wages" and the wage-base mechanics). The contribution is employer-only. The surcharge and the rate reduction are computed on the same taxable wages.

## Deadlines and filing

- Contribution and wage reports are filed quarterly with the Office of Unemployment Insurance; unpaid surcharge "shall be subject to interest at the rate of one and one-half percent (1.5%) per month or fraction thereof, not to exceed ninety percent (90%)" (KRS 341.614(4)). Verify the current quarterly due dates and the electronic filing mandate on the Office of Unemployment Insurance employer portal before relying on a specific date (see Not yet confirmed).
- Rate notices: the "computation date" for new rates is July 31 of each year (KRS 341.270(5)).

## Penalties and interest

KRS 341.614 imposes 1.5% monthly interest on an unpaid interest-payment surcharge, capped at 90% of the surcharge, plus a lien on the property of a delinquent employer (KRS 341.614(5)). Contribution-penalty percentages for late quarterly reports are set by the Office of Unemployment Insurance -- confirm from the current agency notice before quoting them (see Not yet confirmed). Common failure modes: (1) out-of-state employers missing Kentucky coverage for Kentucky-based staff; (2) misclassifying workers as independent contractors, shifting UI wages; (3) letting a dormant account lapse while still paying Kentucky wages.

## Cross-border points

- Multi-state employees: localization-of-service rules decide which state gets the wages -- confirm current Kentucky guidance before assigning wages (see Not yet confirmed).
- FUTA credit against Kentucky UI follows the standard federal pattern; Kentucky's current-year credit-reduction status must be checked on the IRS credit-reduction list each year (not archived this run).
- KRS 341.272 covers construction-trade new employers including "any foreign corporation authorized to do business in this state."

## Worked examples

### Example 1: contribution at the new-employer rate (hypothetical facts)

A new non-construction Kentucky employer at the 2.7% rate with $10,000 of covered wages for one employee in the quarter: contribution $10,000 × 2.7% = $270.

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

### Example 2: rate reduction under KRS 341.243 (hypothetical facts)

An experience-rated employer with a Table A rate of 3.0% has the rate reduced by 0.075% while the trust-fund condition holds: effective rate 3.0% − 0.075% = 2.925%. On $10,000 of wages: $292.50.

```oa-check
name: KY UI rate reduction 0.075 percent
inputs:
  table_rate: 0.03
  reduction: 0.00075
  wages: 10000
steps:
  - eff_rate: table_rate - reduction
  - tax: wages * eff_rate
expected:
  eff_rate: 0.02925
  tax: 292.50
```

## Ask the client first

- Pull the employer's current rate notice from the Office of Unemployment Insurance before quoting a rate or the wage base.
- Do you have Kentucky-based employees (including remote hires into Kentucky)?
- Is the employer in its first 12 quarters (new-employer rate) or later (experience-rated)?
- Is workers' compensation coverage in force, with correct class codes?
- Are workers correctly classified for UI wages?

## Sources

| Source | URL | Read on |
|---|---|---|
| KRS 341.270 (employer contribution rates; 3%/2.7%; Table A schedules; reserve ratio; computation date) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS341.270 | 2026-10-28 |
| KRS 341.272 (construction-trade new-employer maximum rate) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS341.272 | 2026-10-28 |
| KRS 341.030 ("wages" defined; taxable wage base mechanics; $200M trust fund trigger) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS341.030 | 2026-10-28 |
| KRS 341.243 (service capacity upgrade fund; 0.075% rate reduction to 12/31/2026; 0.0115% from 1/1/2027) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS341.243 | 2026-10-28 |
| KRS 341.614 (interest-payment surcharge 0.22% of first $9,600; 1.5% monthly interest) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS341.614 | 2026-10-28 |

Not yet confirmed: the 2026 (and 2025) taxable wage base dollar amount (the archived KRS 341.030 gives the $300-per-year escalation mechanics toward $12,000, but the current-year dollar figure is set by the Office of Unemployment Insurance's annual determination, whose page was JS-rendered and could not be archived this run -- v0.1's "$11,400" figure is not tied to an archived primary source and must not be used until the rate notice is pulled); which Table A schedule (Trust Fund Adequacy Rates, A, B, C, D or E) is in effect for calendar 2026 (depends on the September 30, 2025 trust fund balance published by the agency); the quarterly report due dates and electronic filing mandate (agency pages JS-rendered); workers' compensation requirements under KRS chapter 342 (statute not archived); FUTA credit-reduction status for 2026 (IRS list not archived); v0.1's "0.075% service capacity surcharge" was corrected this run -- KRS 341.243 provides a 0.075% rate **reduction**, not a surcharge.

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
