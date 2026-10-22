---
name: pm-social-contributions
description: >
  Use this skill when reviewing Saint-Pierre-et-Miquelon employee social contributions, payroll deductions, or the income-tax treatment of compulsory social charges for 2026 work. It explains which payroll amounts reduce taxable salary under the local income-tax code, the employer's annual DADS reporting obligation, and how to build a reviewable salary-base workpaper when the current CPS rate schedule is supplied. Trigger on Saint-Pierre-et-Miquelon payroll, CPS contributions, employee social security, deductible payroll charges, DADS, taxable salary, or social-contribution reconciliation questions.
jurisdiction: PM
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-22
version: 0.1
---

# Saint-Pierre-et-Miquelon Social Contributions v0.1

> **General reference only.** This source-cited draft requires local professional review before filing or payment. It does not calculate an employer or employee contribution unless the current official CPS rate schedule and the worker's coverage facts are supplied.

## 1. Who this applies to

This skill applies to employers and employees whose remuneration is reported in Saint-Pierre-et-Miquelon and to reviewers reconciling payroll deductions to local taxable salary. Article 56 of the local tax code allows employee retirement, social-security, and, where relevant, unemployment contributions to be deducted from gross salary before the standard employment-expense deduction.

The French coordination rules described by CLEISS may matter where a worker remains covered by another French scheme. Confirm the worker's place of work, assignment status, certificate of coverage, and CPS registration before choosing a contribution schedule.

### Source status caveat

The official CPS public site did not resolve during the 2026-10-22 source check. The local tax code and CLEISS coordination page resolved, but neither is a current CPS contribution-rate schedule. This draft therefore does **not** invent contribution percentages, ceilings, employer rates, or payment dates. Obtain the 2026 CPS schedule before calculating liabilities.

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Official source |
|---|---:|---:|---|
| Employee retirement and social-security contributions deductible from gross salary | Actual qualifying amount | 2026 filing work | [Code local des impôts, art. 56(1)](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| Standard employment-expense deduction after those contributions | 10% | 2026 filing work | [Code local des impôts, art. 56(2)](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| Minimum standard employment-expense deduction | EUR 500, capped at gross salary | 2026 filing work | [Code local des impôts, art. 56(4)](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| CPS contribution rates and ceilings | Source pending; do not estimate | 2026 | Current CPS schedule required |

## 3. The base

Start with gross cash remuneration and taxable benefits. Deduct only employee retirement, social-security, and applicable unemployment contributions that are supported by payroll records. Apply the 10% employment-expense deduction to the remainder, subject to the EUR 500 minimum and the gross-salary cap. A worker may instead substantiate actual professional expenses under article 56(5); do not claim both methods.

This is an income-tax-base reconciliation, not a substitute for the CPS contribution base. Preserve gross pay, each employee deduction, employer-only charges, benefits, and corrections as separate workpaper columns.

## 4. Deadlines and filing

Article 57 requires an employer, administration, company, or association paying employees to file the annual *déclaration annuelle de données sociales* (DADS) with the territorial fiscal services before 31 January, accompanied by form 2470 for each recipient. The filing includes identity, employment, remuneration, benefits, and the covered period. Confirm separate CPS periodic declarations and payments from the current CPS schedule because those dates were not available from a resolving primary source.

## 5. Penalties and interest

Do not calculate CPS late-payment additions from this draft. Obtain the current CPS recovery rules and notice. Tax-code penalties can apply to inaccurate or late fiscal reporting, but the contribution-specific rate and interest basis must be verified from the governing CPS source before a provision is booked.

## 6. Cross-border points

CLEISS explains that social-protection coordination can keep some temporarily assigned workers within another French scheme. A foreign employer should not assume that tax residence, payroll reporting, and social-security coverage move together. Obtain any certificate of coverage and determine whether a local employer or representative has reporting duties.

## 7. Worked examples

### Example 1 — Taxable salary after supplied employee contributions

An employee has EUR 30,000 gross salary and payroll records show EUR 2,100 of qualifying employee retirement and social-security contributions. The post-contribution amount is EUR 27,900; the 10% employment-expense deduction is EUR 2,790; taxable salary is EUR 25,110. The EUR 2,100 is an input from payroll records, not a rate computed by this skill.

```oa-check
name: PM taxable salary from supplied contributions
inputs:
  gross_salary: 30000
  employee_contributions: 2100
steps:
  after_contributions: gross_salary - employee_contributions
  employment_expense_deduction: after_contributions * 0.10
  taxable_salary: after_contributions - employment_expense_deduction
expected:
  after_contributions: 27900.00
  employment_expense_deduction: 2790.00
  taxable_salary: 25110.00
```

### Example 2 — Minimum employment-expense deduction

An employee has EUR 4,000 gross salary and EUR 280 of supported employee contributions. Ten percent of the EUR 3,720 remainder is EUR 372, so article 56's EUR 500 minimum applies. Taxable salary is EUR 3,220.

```oa-check
name: PM minimum employment-expense deduction
inputs:
  gross_salary: 4000
  employee_contributions: 280
  minimum_deduction: 500
steps:
  after_contributions: gross_salary - employee_contributions
  percentage_deduction: after_contributions * 0.10
  allowed_deduction: max(percentage_deduction, minimum_deduction)
  taxable_salary: after_contributions - allowed_deduction
expected:
  after_contributions: 3720.00
  percentage_deduction: 372.00
  allowed_deduction: 500.00
  taxable_salary: 3220.00
```

## 8. Ask the client first

- Where did the employee physically work, and for what dates?
- Was the worker registered with CPS or covered under another scheme?
- What current CPS rate schedule, ceilings, and payment notices apply?
- Which payroll deductions were employee amounts versus employer-only charges?
- Were benefits in kind and corrections included in the annual DADS?
- Is an actual-expense claim being considered instead of the standard deduction?

## 9. Sources

- [Code local des impôts, 2026 consolidation](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf), articles 56 and 57 — `as_of: 2026-10-22`.
- [Direction des Services Fiscaux de Saint-Pierre-et-Miquelon](https://www.services-fiscaux975.fr/) — `as_of: 2026-10-22`.
- [CLEISS, Saint-Pierre-et-Miquelon coordination page](https://www.cleiss.fr/docs/ol/stpm.html) — `as_of: 2026-10-22`.

<!-- openaccountants-cta-block -->
## Talk to a verified accountant

This guide is a source-cited draft. [Book a review with a verified accountant](https://calendly.com/openaccountants) before filing or paying.
