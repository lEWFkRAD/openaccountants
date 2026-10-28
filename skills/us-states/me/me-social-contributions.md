---
name: me-social-contributions
description: >
  Use this skill whenever asked about Maine employer social contributions
  for 2026 — unemployment insurance (ME UC-1 quarterly contributions
  report processed by Maine Revenue Services for the Department of Labor),
  the interaction with federal FUTA/SUTA, and what Maine adds on top of
  federal payroll taxes. Trigger on "Maine unemployment insurance",
  "ME UC-1", "Maine employer contributions", "Maine SUTA". Source-cited
  draft; ME UC-1 role and DOL administration verified on the MRS
  employer-withholding page 2026-10-28; wage base and rate schedules
  needs-sources (DOL UI page unreachable this run).
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

## 1. Scope and sources

Covers employer social-cost obligations for Maine employment: state unemployment insurance (SUTA) and the state-side rails around FUTA. **Source status:** the MRS Employer Withholding page (https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding, fetched and verified 2026-10-28) confirms **Maine Revenue Services processes the Unemployment Contributions Report (Form ME UC-1) quarterly and the Maine Department of Labor administers the Unemployment Insurance Contributions once the quarterly report is filed**. The **2026 taxable wage base, new-employer rate, and experience-rate schedule sit on the DOL UI site, which was not reachable this run — needs-sources**.

## 2. Who applies

Every Maine employer (and out-of-state employers with Maine employees) that pays wages subject to Maine UI. Maine has **no state disability, paid-family-leave, or state retirement mandate** for private employers beyond federal FICA/FUTA — no state pension surcharge (verify any sector-specific programs; **needs-sources**).

## 3. Rates and wage base

| Item | 2026 figure | Source status |
|---|---|---|
| ME UI taxable wage base | not fetched | **needs-sources** |
| Employer experience rates | schedule not fetched | **needs-sources** |
| New-employer rate | not fetched | **needs-sources** |
| FUTA (federal, for context) | 6.0% on first $7,000, credit up to 5.4% for timely SUTA | federal standing rule |

## 4. Base and mechanics

- Quarterly **ME UC-1** gross-wage and contribution report, processed through MRS / Maine Tax Portal (verified); DOL then administers the account (verified).
- W-3ME annual reconciliation of income tax withheld is **discontinued for tax years after 2023** (verified — MRS page); UI reporting continues via UC-1.

## 5. Deadlines, penalties, interest

- UC-1 quarterly due dates: standard last-day-of-month-after-quarter convention expected — **needs-sources**.
- Penalty/interest schedule for late UI reports: **needs-sources**.

## 6. Cross-border notes

Multi-state employers register with Maine DOL for UI and withhold Maine income tax per `me-payroll.md`; reciprocal-state rules: Maine has **no income-tax reciprocity agreements** (verify — **needs-sources**).

## 7. Worked examples

**Example 1 — FUTA net cost per employee (federal context).**

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

**Example 2 — illustrative ME UI cost (figures assumed, needs-sources).** Wage base $37,000 and experience rate 2.1% are placeholders pending the DOL schedule:

```oa-check
name: ME UI illustrative
inputs:
  wage_base: 37000
  rate: 0.021
steps:
  - ui: wage_base * rate
expected:
  ui: 777.00
```

## 8. Ask the client

- Are UC-1 filings current — experience rating depends on them?
- Multi-state workforce: is Maine the localizing state under the four-part localization test (verify — **needs-sources**)?
- Seasonal/agricultural/coverage-exception status (Maine UI coverage exceptions — **needs-sources**)?

## 9. Sources

1. MRS Employer Withholding (941ME and ME UC-1): https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding — fetched and verified 2026-10-28.
2. Maine DOL portal: https://www.maine.gov/labor/ — resolves; UI employer rate page not reachable this run.

**Needs-sources:** 2026 wage base, rate schedule, new-employer rate, UC-1 due dates, penalty/interest, localization and reciprocity statements.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Maine payroll/social-cost questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
