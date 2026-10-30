---
name: fl-social-contributions
description: >
  Use this skill whenever asked about Florida employer social contributions
  for tax year 2026 -- Florida reemployment (unemployment) tax under Ch. 443
  Fla. Stat. administered by the Department of Revenue, the $7,000 taxable
  wage base, the 2.7% initial new-employer rate, the employer-only nature
  of the tax, quarterly RT-6 filing due the last day of the month after each
  quarter, and mandatory workers' compensation insurance under Ch. 440
  (construction industry from one employee, other industries from four).
  Trigger on "Florida reemployment tax", "Florida SUTA", "Florida UI rate",
  "RT-6", "Florida workers compensation requirement".
  ALWAYS load us-tax-workflow-base first.
version: 0.2
jurisdiction: US-FL
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - fl-corporate-income-tax
---

# Florida social contributions (reemployment tax + workers' comp overlay), tax year 2026

> **Source-cited draft.** Built from the Florida Department of Revenue reemployment tax page, Form RT-6, the Florida Division of Workers' Compensation coverage-requirements page, and s. 440.04 Fla. Stat. (2026), read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

**Reemployment tax.** Florida reemployment (unemployment) tax is administered by the Florida Department of Revenue. An employer is liable if it meets any of the coverage tests on the DOR page: at least one quarterly payroll of $1,500 or more in a calendar year, or one or more employees for a day (or part of a day) in each of 20 weeks in a calendar year (FDOR reemployment tax page). Out-of-state employers with Florida employees are pulled in on the same basis.

**Workers' compensation.** Employers in the construction industry must carry workers' compensation coverage from one or more employees (including the owner where the owner is a corporate officer or LLC member); employers in other industries must carry coverage from four or more employees (Florida Division of Workers' Compensation, coverage requirements). An exempted corporate officer does not count as an employee for the non-construction test.

**No employee-side state social contribution.** Unlike New York or Washington, Florida employees fund no state payroll social insurance; the employee side of a Florida payroll is federal FICA only, and Florida has no state individual income tax withholding.

## Rates, bands and thresholds

| Item | Rate / amount | Source |
|---|---|---|
| Reemployment taxable wage base | First $7,000 of wages paid to each employee per calendar year | FDOR reemployment tax page: "Only the first $7,000 of wages paid to each employee by their employer in a calendar year is taxable." |
| Initial (new-employer) rate | 2.7% | FDOR reemployment tax page: "The initial tax rate for new employers is .0270 (2.7%), which is applied to the first $7,000 in wages paid to each employee during a calendar year." |
| Experienced-employer rates | Experience-rated; employers with stable employment records receive reduced rates after a qualifying period | FDOR reemployment tax page: "Employers with stable employment records receive reduced tax rates after a qualifying period." |
| Employee contribution to reemployment tax | None -- the tax is an employer obligation | FDOR reemployment tax page: "An employer is liable to pay reemployment tax if it meets any of the following conditions..." |
| Workers' compensation premium | Carrier-rated by job classification code; no state rate table | s. 440.04 Fla. Stat. governs waiver of exemption; coverage requirements per the Division of Workers' Compensation |
| State disability / paid family leave | No Florida program exists | The state's payroll contributions are limited to reemployment tax (Ch. 443) and workers' compensation (Ch. 440); no disability or PFML statute is administered on payroll |

Wages over $7,000 per employee for the year are "excess wages" and not subject to tax (FDOR reemployment tax page). S-corporation salaries paid to corporate officers are wages, and part of officer distributions for active officers performing services can be considered wages (FDOR reemployment tax page).

## The taxable base

The reemployment base is covered wages up to $7,000 per employee per calendar year at the employer's assigned rate. The workers' compensation premium base is payroll by classification code under the carrier's policy. Florida has no state disability-insurance, paid-family-leave, or state-retirement contribution on private payroll.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Employer's Quarterly Report (Form RT-6) and wage report | By the end of the month following each quarter: 1st (Jan-Mar) due April 30; 2nd (Apr-Jun) due July 31; 3rd (Jul-Sep) due October 31; 4th (Oct-Dec) due January 31 | FDOR reemployment tax page due-date table |
| Zero-activity quarters | Reports are due even if the employer had no employees or wages for the quarter | FDOR reemployment tax page: "Reports are due even if you had no employees or wages to report for that quarter." |
| Annual rate notices | Issued each year; an employer who protests a rate notice must file with the department within 20 days of the "mailed on or before" date on the notice | FDOR reemployment tax page: "you must file a protest with the Florida Department of Revenue within 20 days of the 'mailed on or before' date stated on the Notice." |
| Workers' compensation coverage | Continuous while the employer meets the coverage tests; certificates of insurance on request; construction-industry compliance verified through the Division of Workers' Compensation | Division of Workers' Compensation, coverage requirements |

## Penalties and interest

Late or unpaid reemployment contributions draw penalties and interest under Ch. 443 (the Form RT-6 shows a penalty and interest computation after the due date). Common failure modes: (1) out-of-state employers assuming no Florida reemployment duty for remote Florida employees; (2) treating workers' compensation as optional for a small crew -- construction requires it from the first employee; (3) misclassifying employees as contractors, which shifts both reemployment wages and compensation premium.

## Cross-border points

- Multi-state employers allocate reemployment wages to Florida employment under the standard localization-of-services rules; reciprocal coverage agreements permit one-state coverage for employees working in several states.
- Federal FUTA credit reduction depends on each year's federal determination for Florida; check the current year's FUTA status before computing federal unemployment tax.
- Florida has no state individual income tax, so there is no state withholding to remit for Florida employees (see the pack README).

## Worked examples

All client facts in the examples are hypothetical; the $7,000 wage base and 2.7% initial rate are the confirmed figures from the rates table above.

An employer with one Florida employee paid above the $7,000 base all year, at the 2.7% initial rate:

```oa-check
name: FL reemployment tax on one employee
inputs:
  base: 7000
  rate: 0.027
steps:
  - tax: base * rate
expected:
  tax: 189.00
```

The same employer with four Florida employees at the same base and rate:

```oa-check
name: FL reemployment tax four employees
inputs:
  base: 7000
  n: 4
  rate: 0.027
steps:
  - wages: base * n
  - tax: wages * rate
expected:
  wages: 28000.00
  tax: 756.00
```

## Ask the client first

- Do you have Florida employees, including remote workers hired into Florida?
- Are you experience-rated or a new employer? Pull the current rate notice (and check the 20-day protest window if the rate is unexpected).
- Is workers' compensation coverage in place for every crew -- construction work from the first employee, other industries from four?
- Are workers correctly classified -- employee vs contractor -- for both reemployment wages and compensation premium?
- Are officer salaries and active-officer distributions reported as wages?

## Sources

| Source | URL | Read on |
|---|---|---|
| Florida Department of Revenue -- Reemployment Tax page (coverage tests, $7,000 wage base, 2.7% initial rate, RT-6 due dates, 20-day rate protest) | https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx | 2026-10-28 |
| Form RT-6, Employer's Quarterly Report (PDF) | https://floridarevenue.com/Forms_library/current/rt6.pdf | 2026-10-28 |
| Florida Division of Workers' Compensation -- Coverage Requirements (construction one or more; non-construction four or more) | https://www.myfloridacfo.com/division/wc/employer/coverage-requirements | 2026-10-28 |
| s. 440.04 Fla. Stat. (2026) -- workers' compensation; waiver of exemption | https://www.flsenate.gov/Laws/Statutes/2026/440.04 | 2026-10-28 |

Not yet confirmed: the statutory minimum and maximum experience rates and the full rate-schedule mechanics in Ch. 443 (the current rate tables were not located in the 2026 statute chapter sections archived this run); the current-year federal FUTA credit-reduction status for Florida; the reciprocal-coverage-agreement participation details for multi-state employers; the specific penalty percentages and interest rate for late reemployment contributions (the Ch. 443 penalty provisions were not archived this run).

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
