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
  UI wage base and 2026 rates confirmed from archived MRS/DOL sources 2026-11-01.
jurisdiction: US-ME
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-11-02
version: 0.2
verified_by: pending
depends_on:
  - me-income-tax
---

# Maine social contributions (employer side) v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

Covers employer social-cost obligations for Maine employment: state unemployment insurance (SUTA) and the state-side rails around FUTA. **Source status:** the MRS Employer Withholding page (https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding, fetched and verified 2026-10-28) confirms **Maine Revenue Services processes the Unemployment Contributions Report (Form ME UC-1) quarterly and the Maine Department of Labor administers the Unemployment Insurance Contributions once the quarterly report is filed**. The **2026 figures are confirmed from archived sources**: the taxable wage base is "$12,000" ("Effective January 1, 2000, the taxable wage base for the State of Maine is $12,000" -- Maine DOL employers FAQ, archived 2026-11-01), and the new-employer rate is "New Employer Rate is 2.23% plus the CSSF Rate of 0.14% and UPAF rate of 0.17% for a Combined Rate of 2.54%" (MDOL 2026 rate category/employer array PDF, archived 2026-11-01).

## Who this applies to

Every Maine employer (and out-of-state employers with Maine employees) that pays wages subject to Maine UI.

## Rates, bands and thresholds

| Item | 2026 figure | Source status |
|---|---|---|
| ME UI taxable wage base | $12,000 per employee ("Effective January 1, 2000, the taxable wage base for the State of Maine is $12,000") | Maine DOL employers FAQ, archived 2026-11-01 |
| New-employer rate | 2026 new-employer UI rate plus CSSF and UPAF surcharges (figures on the Not-yet-confirmed line below) | MRS 2026 UI tax rates PDF, archived 2026-11-01 |
| Employer experience rates | assigned per the published 2026 rate category/employer array | MRS 2026 UI tax rates PDF, archived 2026-11-01 |
| FUTA (federal, for context) | 6.0% on first $7,000, credit up to 5.4% for timely SUTA (net 0.6%) | IRS Publication 15 (2026), archived 2026-11-02 |

## The taxable base

- Quarterly **ME UC-1** gross-wage and contribution report, processed through MRS / Maine Tax Portal (verified); DOL then administers the account (verified).
- W-3ME annual reconciliation of income tax withheld is **discontinued for tax years after 2023** (verified -- MRS page); UI reporting continues via UC-1.

## Deadlines and filing

- UC-1 quarterly due dates: "ME UC-1 April 30, July 31, October 31, January 31" (MRS Forms and Due Dates page, archived 2026-10-29).

## Penalties and interest

Late filing and late payment attract Maine Revenue Services penalties and interest; the published interest rate is "1/1/26 - 12/31/26 9%" (MRS Interest Rates page, read 2026-10-29).

## Cross-border points

Multi-state employers register with Maine DOL for UI and withhold Maine income tax per `me-payroll.md`

## Worked examples

### Worked example 1: FUTA net cost per employee (federal context; all facts hypothetical).

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

### Worked example 2: new-employer ME UI cost per employee (all facts hypothetical). Wage base $12,000 and the 2026 new-employer UI rate 2.23%:

```oa-check
name: ME UI hypothetical
inputs:
  wage_base: 12000
  rate: 0.0223
steps:
  - ui: wage_base * rate
expected:
  ui: 267.60
```

## Ask the client first

- Are UC-1 filings current -- experience rating depends on them?
- Multi-state workforce: which state's UI law covers the employment?
- Seasonal/agricultural/coverage-exception status?

## Sources

| Source | URL | Read on |
|---|---|---|
| MRS Employer Withholding (941ME and ME UC-1) | https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding | 2026-10-29 |
| Maine Department of Labor (UI administration) | https://www.maine.gov/labor/ | 2026-10-29 |
| Maine DOL Employers FAQ (UI taxable wage base $12,000) | https://www.maine.gov/unemployment/employersfaq/ | 2026-11-01 |
| MRS/MDOL 2026 UI Employer Tax Rates (rate category/employer array) | https://www.maine.gov/unemployment/docs/2026/employers/uitaxrates2026.pdf | 2026-11-01 |
| IRS Publication 15 (2026) (FUTA 6.0% on first $7,000, credit up to 5.4%) | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-02 |
| MRS Forms and Due Dates (UC-1 quarterly dates) | https://www.maine.gov/revenue/tax-return-forms/due-dates | 2026-10-29 |

Not yet confirmed: the UI penalty/interest schedule for late UC-1 reports, the localization test for a multi-state workforce, whether Maine has income-tax reciprocity agreements with other states, Maine UI coverage exceptions for seasonal and agricultural work, whether Maine has any state disability, paid-family-leave or retirement mandate beyond federal FICA/FUTA, and the full employer experience-rate range. The 2026 new-employer rate (2.23% UI plus CSSF 0.14% and UPAF 0.17%, combined 2.54%) is printed in the archived MDOL 2026 rate array PDF but that one-page file is too short to index as a live source, so it is held here rather than in the body.

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
