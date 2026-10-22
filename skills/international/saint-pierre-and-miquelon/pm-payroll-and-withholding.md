---
name: pm-payroll-and-withholding
description: >
  Use this skill for Saint-Pierre-et-Miquelon employer reporting, DADS preparation, and local withholding on investment income in 2026 work. It distinguishes the annual employee-remuneration return from source deductions on payments to non-residents, including dividends and fixed-income interest, and provides mechanically checkable workpaper examples. Trigger on Saint-Pierre-et-Miquelon payroll, employer declaration, DADS, form 2470, salary reporting, non-resident dividend withholding, bank-interest withholding, remittance, or payer compliance. It does not supply unverified CPS contribution rates or convert annual income tax into wage withholding.
jurisdiction: PM
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-22
version: 0.1
---

# Saint-Pierre-et-Miquelon Payroll and Withholding v0.1

> **General reference only.** This source-cited draft requires local professional review before any return, remittance, or payment.

## 1. Who this applies to

The employer-reporting rules apply to any individual, administration, company, or association that pays employees, apprentices, workers, or auxiliaries. Separate payer rules apply to entities paying local movable-capital income, particularly dividends and fixed-income interest to persons whose tax domicile or registered office is outside Saint-Pierre-et-Miquelon.

This skill does not treat the progressive annual personal income tax as payroll withholding. Confirm whether a payment is salary, a taxable benefit, a dividend, interest, or another fee before selecting the rule.

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Official source |
|---|---:|---:|---|
| Withholding on covered dividends and distributed income paid to a non-resident | 15% of gross payment | 2026 work | [Code local des impôts, art. 72 bis](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| Interest paid to a non-resident | 10% of interest | 2026 work | [Code local des impôts, art. 74 bis](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| Anonymous cash-certificate interest | 55% final levy | 2026 work | [Code local des impôts, art. 74 bis](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| Late remittance addition stated for article 74 bis payer | 10% | 2026 work | [Code local des impôts, art. 74 bis](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |

## 3. The base

For DADS reporting, collect each recipient's gross cash remuneration, benefits in kind, commissions or fees, and covered period. Do not net employee contributions or expenses out of the gross remuneration fields unless the official form instructions expressly require it.

Article 72 bis applies its 15% withholding to the gross covered income put into payment. Article 74 bis applies 10% to non-resident interest. Determine beneficial ownership and tax domicile before applying the non-resident rate, and preserve any treaty or exemption analysis.

## 4. Deadlines and filing

The DADS and a form 2470 for each recipient are due to the territorial fiscal services before 31 January following the payment year under article 57. Article 74 bis requires the payer to remit the 55% anonymous-instrument levy by the 15th of the month after payment or account credit and to submit a semiannual summary. For other source deductions, confirm the current remittance form and operational deadline with the Direction des Services Fiscaux before paying.

## 5. Penalties and interest

Article 74 bis states a 10% addition where the payer does not remit its covered levy on time. Do not extend that specific addition to a different withholding category without checking the governing article. Preserve notices and payment dates so a reviewer can determine interest or other additions under the current local procedure.

## 6. Cross-border points

Residence drives the 15% article 72 bis and 10% article 74 bis rules. Obtain the recipient's tax-residence evidence and check any applicable convention before finalizing. A foreign company with local employees may still have annual employer-reporting duties even if it has no local registered office; permanent-establishment and corporate-income-tax questions belong in the corporate skill.

## 7. Worked examples

### Example 1 — Amount reported for an employee

An employer paid EUR 22,000 cash salary and provided EUR 1,500 of taxable benefits. The remuneration workpaper total for the DADS is EUR 23,500 before mapping each item to the current form.

```oa-check
name: PM annual employee remuneration total
inputs:
  cash_salary: 22000
  taxable_benefits: 1500
steps:
  reportable_remuneration: cash_salary + taxable_benefits
expected:
  reportable_remuneration: 23500.00
```

### Example 2 — Non-resident dividend and interest

A non-resident receives EUR 12,000 of covered dividends and EUR 3,000 of local bank interest. Before any convention analysis, article 72 bis produces EUR 1,800 of dividend withholding and article 74 bis produces EUR 300 of interest withholding, for EUR 2,100 total.

```oa-check
name: PM nonresident investment-income withholding
inputs:
  gross_dividend: 12000
  gross_interest: 3000
steps:
  dividend_withholding: gross_dividend * 0.15
  interest_withholding: gross_interest * 0.10
  total_withholding: dividend_withholding + interest_withholding
expected:
  dividend_withholding: 1800.00
  interest_withholding: 300.00
  total_withholding: 2100.00
```

## 8. Ask the client first

- What was each payment's legal character: salary, benefit, fee, dividend, or interest?
- Where was each recipient tax-resident on the payment date?
- Is a tax convention, exemption, or residence certificate available?
- Were amounts paid in cash, credited to an account, or provided in kind?
- Were all employees and forms 2470 included in the annual DADS?
- What remittance receipts and payer summaries exist?

## 9. Sources

- [Code local des impôts, 2026 consolidation](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf), articles 57, 72 bis, 74 bis, and 74 ter — `as_of: 2026-10-22`.
- [Direction des Services Fiscaux de Saint-Pierre-et-Miquelon](https://www.services-fiscaux975.fr/) — `as_of: 2026-10-22`.

<!-- openaccountants-cta-block -->
## Talk to a verified accountant

This guide is a source-cited draft. [Book a review with a verified accountant](https://calendly.com/openaccountants) before filing or paying.
