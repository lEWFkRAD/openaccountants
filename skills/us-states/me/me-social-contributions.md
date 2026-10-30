---
name: me-social-contributions
description: >
  Use this skill whenever asked about Maine employer social contributions
  for 2026 -- unemployment insurance (ME UC-1 quarterly contributions
  report processed by Maine Revenue Services for the Department of Labor),
  the interaction with federal FUTA/SUTA, and what Maine adds on top of
  federal payroll taxes. Trigger on "Maine unemployment insurance",
  "ME UC-1", "Maine employer contributions", "Maine SUTA". Source-cited
  draft; ME UC-1 role and DOL administration verified on the MRS
  employer-withholding page 2026-10-28; wage base and rate schedules
  UI figures not yet confirmed (DOL UI page unreachable this run).
jurisdiction: US-ME
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - me-income-tax
---

# Maine social contributions (employer side) v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

Covers employer social-cost obligations for Maine employment: state unemployment insurance (SUTA) and the state-side rails around FUTA. **Source status:** the MRS Employer Withholding page (https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding, fetched and verified 2026-10-28) confirms **Maine Revenue Services processes the Unemployment Contributions Report (Form ME UC-1) quarterly and the Maine Department of Labor administers the Unemployment Insurance Contributions once the quarterly report is filed**. The **2026 taxable wage base, new-employer rate, and experience-rate schedule sit on the DOL UI site, which was not reachable this run -- not yet confirmed**.

## Who this applies to

Every Maine employer (and out-of-state employers with Maine employees) that pays wages subject to Maine UI. Maine has **no state disability, paid-family-leave, or state retirement mandate** for private employers beyond federal FICA/FUTA -- no state pension surcharge (verify any sector-specific programs; not yet confirmed).

## Rates, bands and thresholds

| Item | 2026 figure | Source status |
|---|---|---|
| ME UI taxable wage base | not fetched | Not yet confirmed |
| Employer experience rates | schedule not fetched | Not yet confirmed |
| New-employer rate | not fetched | Not yet confirmed |
| FUTA (federal, for context) | 6.0% on first $7,000, credit up to 5.4% for timely SUTA | not yet confirmed (federal standing rule; no archived source in this pack) |

## The taxable base

- Quarterly **ME UC-1** gross-wage and contribution report, processed through MRS / Maine Tax Portal (verified); DOL then administers the account (verified).
- W-3ME annual reconciliation of income tax withheld is **discontinued for tax years after 2023** (verified -- MRS page); UI reporting continues via UC-1.

## Deadlines and filing

- UC-1 quarterly due dates: standard last-day-of-month-after-quarter convention expected -- not yet confirmed.
- Penalty/interest schedule for late UI reports: not yet confirmed.

## Penalties and interest

Late filing and late payment attract Maine Revenue Services penalties and interest; the published interest rate is "1/1/26 - 12/31/26 9%" (MRS Interest Rates page, read 2026-10-29). Specific penalty percentages: not yet confirmed.

## Cross-border points

Multi-state employers register with Maine DOL for UI and withhold Maine income tax per `me-payroll.md`; reciprocal-state rules: Maine has **no income-tax reciprocity agreements** (verify -- not yet confirmed).

## Worked examples

**Worked example 1 -- FUTA net cost per employee (federal context; all facts hypothetical).**

```oa-check
name: FUTA net 0.6 percent
inputs:
  wage_base: 7000
  net_rate: 0.006
steps:
  - futa: wage_base * net_rate
expected:
  futa: 42.00
```

**Worked example 2 -- hypothetical ME UI cost (all facts hypothetical, not yet confirmed).** Wage base $37,000 and experience rate 2.1% are assumed pending the DOL schedule:

```oa-check
name: ME UI hypothetical
inputs:
  wage_base: 37000
  rate: 0.021
steps:
  - ui: wage_base * rate
expected:
  ui: 777.00
```

## Ask the client first

- Are UC-1 filings current -- experience rating depends on them?
- Multi-state workforce: is Maine the localizing state under the four-part localization test (verify -- not yet confirmed)?
- Seasonal/agricultural/coverage-exception status (Maine UI coverage exceptions -- not yet confirmed)?

## Sources

| Source | URL | Read on |
|---|---|---|
| MRS Employer Withholding (941ME and ME UC-1) | https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding | 2026-10-29 |
| Maine Department of Labor (UI administration) | https://www.maine.gov/labor/ | 2026-10-29 |

Not yet confirmed: 2026 UI taxable wage base, employer rate schedule, new-employer rate, UC-1 due dates, penalty/interest, localization and reciprocity statements (the DOL UI rate page was not reachable; archived labor page confirms administration only).

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Maine payroll/social-cost questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
