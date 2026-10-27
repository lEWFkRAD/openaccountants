---
name: vc-paye-withholding
description: >
  Saint Vincent and the Grenadines PAYE payroll withholding reference for 2026.
  Covers the employer's duty to deduct monthly PAYE under Income Tax Act Cap. 435
  Third Schedule, the current Code 245 tax tables with the EC$25,000 standard
  deduction and the 10/20/28% bands, monthly remittance by the 15th, the annual
  31 January return, employee certificates, and Tax Administration Act 2019
  penalties and 1.5% monthly interest. Use for SVG payroll working papers and
  employer compliance checks. Does not cover NIS contributions, final-pay
  procedures or treaty reductions. Independent accountant review pending.
jurisdiction: VC
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Saint Vincent and the Grenadines PAYE withholding v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows; not reviewed for any specific person's facts. Do not file, pay, or take a position on it without review by a qualified SVG professional.

## 1. Scope and sources

PAYE ("Pay As You Earn") is the monthly deduction of income tax by employers from employees' remuneration, under the Income Tax Act Cap. 435, Third Schedule (deduction at the rates in the Fifth Schedule, as currently tabled). Sources: [IRD taxes page](https://ird.gov.vc/index.php/taxes) and [PAYE tax tables PDF (Code 245, effective 1 Jan 2024)](https://ird.gov.vc/images/pdf/tax-tables-2024.pdf), both read 2026-10-27; [IRD standard-deduction page](https://ird.gov.vc/index.php/rates/standard-deduction) read 2026-10-27. This skill covers employer deduction, remittance, annual return, certificates, and penalties. It does not cover NIS (see `vc-national-insurance`) or withholding on payments to non-residents (see `vc-cross-border`).

## 2. Who applies

- Every employer must withhold PAYE from employees whose remuneration exceeds the annual standard deduction ([IRD taxes page](https://ird.gov.vc/index.php/taxes), read 2026-10-27).
- Liability runs to "all employees earning above the annual standard deduction"; the employer is the withholding agent and is personally liable for amounts not deducted (Cap. 435 Third Schedule, para on employer liability — the duty is not extinguished by failure to deduct; if the employer pays the tax itself it is deemed deducted).
- Representative employers (agents, executors, trustees) carry the same duties to the extent of assets held.

## 3. Rates and base

Current tables: **Code 245, standard deduction EC$25,000, effective 1 January 2024** ([tax-tables-2024.pdf](https://ird.gov.vc/images/pdf/tax-tables-2024.pdf), read 2026-10-27; the [standard-deduction page](https://ird.gov.vc/index.php/rates/standard-deduction) confirms EC$25,000 for 2024 and 2025). Annualised bands decoded from the monthly table (verified against table rows, e.g. monthly salary 3,090 → tax 173.53; 5,520 → 853.93):

| Annual income band (EC$) | Rate |
|---|---|
| First 25,000 (standard deduction) | 0% |
| 25,001 – 30,000 | 10% |
| 30,001 – 35,000 | 20% |
| Over 35,000 | 28% |

The consolidated Cap. 435 PDF's Fifth Schedule still prints the older 10/20/30/40% bands (last amendment note: Act No. 2 of 2009); the IRD's published Code 245 tables are the operative PAYE rates. **needs-sources:** the amending Finance Act that moved the individual bands to 10/20/28% was not retrievable on 2026-10-27 (finance.gov.vc returned 503).

Base: remuneration for the pay period, annualised through the table. Use the table for the pay frequency (monthly / fortnightly / weekly); do not convert one frequency's ceiling or band into another.

## 4. Deadlines

- **Monthly remittance:** file and pay on or before the **15th of the month following** the month in which tax was withheld ([IRD taxes page](https://ird.gov.vc/index.php/taxes), read 2026-10-27).
- **Annual PAYE return:** due **31 January** of the year following the calendar year of payment (same source).
- Employee certificates: annual certificate plus per-payment particulars of remuneration and tax deducted (Cap. 435 Third Schedule).

## 5. Penalties and interest

Per the [IRD non-compliance page](https://ird.gov.vc/index.php/non-compliance) (Tax Administration Act 2019), read 2026-10-27:

- **Late filing (s.75):** the GREATER of 5% of tax owing plus 1% per month (or part) of continued failure, AND $500 plus $100 per month in default; capped at $10,000.
- **Late payment (s.76):** 20% of tax due but unpaid.
- **Negligent/fraudulent underpayment (s.77):** 75% of the underpayment where it exceeds $150,000 or 25% of liability; otherwise 25%.
- **Interest:** 1.5% monthly on unpaid amounts (IRD taxes page).
- Employer who fails to deduct remains liable for the tax (Cap. 435 Third Schedule).

## 6. Cross-border

PAYE applies to employment income wherever the employment is exercised in SVG; non-resident employees of SVG employers are withheld on the same tables. Directors not actively engaged in day-to-day management are outside the "member" definition (Cap. 435 s.66 definitions) — their fees follow the non-resident withholding rules in `vc-cross-border`. Treaty residents may claim reduced WHT on services, not on PAYE employment, absent a relief direction from the Comptroller (Cap. 435 s.66(3)).

## 7. Worked examples

**Example 1 — monthly PAYE, EC$3,000 salary.** Annual 36,000; taxable 11,000 above the 25,000 deduction.

```oa-check
name: PAYE monthly, salary 3000 (Code 245)
inputs:
  salary_m: 3000
  sd: 25000
  b1: 5000
  r1: 0.10
  b2: 5000
  r2: 0.20
  r3: 0.28
steps:
  - annual: salary_m * 12
  - taxable: annual - sd
  - band1: min(taxable, b1) * r1
  - band2: min(max(taxable - b1, 0), b2) * r2
  - band3: max(taxable - b1 - b2, 0) * r3
  - annual_tax: band1 + band2 + band3
  - monthly: round(annual_tax / 12, 2)
expected:
  annual_tax: 1780
  monthly: 148.33
```

Cross-check: the published monthly table shows salary 3,000 → tax 148.33 (tax-tables-2024.pdf, read 2026-10-27).

**Example 2 — employer monthly remittance, two employees.** Salaries EC$3,000 and EC$6,000 for July; remit by 15 August.

```oa-check
name: July PAYE remittance, two employees
inputs:
  sd: 25000
  r1: 0.10
  r2: 0.20
  r3: 0.28
steps:
  - e1_annual: 3000 * 12
  - e1_taxable: e1_annual - sd
  - e1_tax: min(e1_taxable, 5000) * r1 + min(max(e1_taxable - 5000, 0), 5000) * r2 + max(e1_taxable - 10000, 0) * r3
  - e1_m: round(e1_tax / 12, 2)
  - e2_annual: 6000 * 12
  - e2_taxable: e2_annual - sd
  - e2_tax: min(e2_taxable, 5000) * r1 + min(max(e2_taxable - 5000, 0), 5000) * r2 + max(e2_taxable - 10000, 0) * r3
  - e2_m: round(e2_tax / 12, 2)
  - remit: round(e1_m + e2_m, 2)
expected:
  e1_m: 148.33
  e2_m: 988.33
  remit: 1136.66
```

## 8. Ask the client

- Pay frequency and gross pay per employee, including arrears, commissions, gratuities and benefits in kind (they enter remuneration).
- Any employee with a second SVG employer (bands apply per employee, not per employer — aggregate).
- Directors' fees vs. management salaries (different withholding tracks).
- Whether PAYE was actually deducted: the employer owes it either way.
- Date the last monthly remittance and last 31 January annual return were filed.

## 9. Sources

- [IRD — Taxes (PAYE section)](https://ird.gov.vc/index.php/taxes) — read 2026-10-27
- [IRD — PAYE Tax Tables, Code 245, effective 1 Jan 2024 (PDF)](https://ird.gov.vc/images/pdf/tax-tables-2024.pdf) — read 2026-10-27
- [IRD — Standard Deduction by year](https://ird.gov.vc/index.php/rates/standard-deduction) — read 2026-10-27
- [IRD — Non-Compliance (TAA 2019 penalties)](https://ird.gov.vc/index.php/non-compliance) — read 2026-10-27
- [Income Tax Act Cap. 435, Third Schedule (PDF)](https://ird.gov.vc/images/pdf/Cap435.pdf) — read 2026-10-27

<!-- openaccountants-cta-block -->

**Talk to a verified accountant** — this skill is a source-cited draft (tier 2). For SVG payroll work under professional review, book time with an OpenAccountants verified accountant: [Calendly](https://www.openaccountants.com).
