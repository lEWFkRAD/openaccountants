---
name: Jamaica payroll and social contributions
description: Use when a Jamaica employer needs 2026 PAYE, NIS, NHT, Education Tax, HEART/NSTA, payroll-base, remittance, or year-end compliance rules.
jurisdiction: JM
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Jamaica payroll and social contributions

## 1. Who this applies to

Jamaica employers must register, deduct employee amounts, calculate employer contributions, remit payroll taxes and contributions, and report employment income. Review employees, directors, casual workers, expatriates and workers labelled contractors. Classification follows the actual relationship, not just the contract title.

## 2. 2026 rates and limits

| Item | Employee | Employer | 2026 rule/source |
|---|---:|---:|---|
| National Insurance Scheme (NIS) | 3% | 3% | Insurable earnings up to JMD 5,000,000 annually; National Insurance (Contributions) (Amendment) Order 2022 and MLSS NIS guidance |
| National Housing Trust (NHT) | 2% | 3% | NHT Act and contribution regulations; employee amount may have refund consequences under NHT rules |
| Education Tax | 2.25% | 3.5% | Education Tax Act as amended; Provisional Collection of Tax (Education Tax) Order 2013 |
| HEART/NSTA levy | — | 3% | 3% of covered employer emoluments; Human Employment and Resource Training Act |
| PAYE income tax | Withheld by employer | — | Annual tax-free threshold JMD 1,700,088 from 1 April 2025; 25% and 30% bands under current TAJ guidance |

Do not assume every levy uses the same base or ceiling. Map each cash and non-cash pay component to each statute separately.

## 3. Payroll base

Start with gross emoluments: salary, wages, overtime, commissions, bonuses, taxable allowances, benefits and director remuneration. Apply the specific inclusion/exclusion rules for PAYE, NIS, NHT, Education Tax and HEART/NSTA. Track the NIS annual insurable-earnings ceiling employee by employee and across payroll-system changes.

For PAYE, apply allowable statutory deductions and the current threshold and bands in the order required by TAJ. Do not derive PAYE solely by applying 25% to gross pay.

## 4. Registration, returns and deadlines

Register the employer and employees with TAJ, NIS/MLSS and NHT as required. TAJ's payroll guidance states that monthly statutory deductions are generally due by the 14th day of the following month. File the prescribed monthly payroll return, remit PAYE and statutory deductions, and complete annual employee reporting and certificates.

Confirm the current S01/S02 or successor form, portal workflow and weekend/holiday rule in the live TAJ system. Reconcile each submission to payroll, the general ledger and bank proof.

## 5. Penalties, interest and corrections

Late filing or payment can produce statutory interest, penalties and collection action; incorrect employee records can also impair NIS/NHT credit. Correct the payroll record, return and employee statement together. Keep registration evidence, pay records, benefit calculations, filed returns and receipts.

**AUDIT FLASH POINT** — NIS has an annual ceiling while NHT, Education Tax and HEART/NSTA use their own bases. A single capped “statutory deduction” base is not a valid substitute.

## 6. Cross-border and mobile workers

For expatriates, secondees and remote workers, identify the legal and economic employer, work location, residence, treaty position and any certificate or exemption from Jamaica social coverage. PAYE and social-contribution conclusions can differ. Do not stop NIS or other deductions merely because a foreign payroll also withholds tax.

## 7. Worked example — NIS and NHT

An employee earns JMD 300,000 in a month and remains below the annual NIS ceiling. Employee NIS is JMD 9,000, employer NIS is JMD 9,000, employee NHT is JMD 6,000 and employer NHT is JMD 9,000.

```oa-check
name: jamaica monthly nis and nht
inputs:
  monthly_earnings: 300000
  nis_rate: 0.03
  employee_nht_rate: 0.02
  employer_nht_rate: 0.03
steps:
  - employee_nis: monthly_earnings * nis_rate
  - employer_nis: monthly_earnings * nis_rate
  - employee_nht: monthly_earnings * employee_nht_rate
  - employer_nht: monthly_earnings * employer_nht_rate
expected:
  employee_nis: 9000.00
  employer_nis: 9000.00
  employee_nht: 6000.00
  employer_nht: 9000.00
```

## 8. Worked example — Education Tax and HEART/NSTA

On JMD 300,000 of covered monthly emoluments, employee Education Tax is JMD 6,750, employer Education Tax is JMD 10,500 and employer HEART/NSTA is JMD 9,000.

```oa-check
name: jamaica education tax and heart
inputs:
  emoluments: 300000
  employee_education_rate: 0.0225
  employer_education_rate: 0.035
  heart_rate: 0.03
steps:
  - employee_education_tax: emoluments * employee_education_rate
  - employer_education_tax: emoluments * employer_education_rate
  - employer_heart: emoluments * heart_rate
expected:
  employee_education_tax: 6750.00
  employer_education_tax: 10500.00
  employer_heart: 9000.00
```

## 9. Ask the client first

1. Are all employees, directors and contractors correctly classified and registered?
2. Which pay and benefit components are included in each statutory base?
3. Has each employee's year-to-date NIS ceiling usage been carried correctly?
4. Do monthly returns, payroll, general ledger and bank payments reconcile?
5. Are there expatriates, secondees or remote workers with treaty or coverage questions?
6. Which TAJ form and deadline apply in the current portal?

## 10. Sources

- [TAJ — income tax](https://www.jamaicatax.gov.jm/income-tax) — official Payroll Taxes and Contributions guidance and PAYE access point; accessed 2026-10-24.
- [MLSS — National Insurance Scheme](https://mlss.gov.jm/departments/national-insurance-scheme/) — official NIS scope and administration; accessed 2026-10-24.
- [Laws of Jamaica — National Insurance (Contributions) (Amendment) Order 2022](https://lipj.gov.jm/record/91300) — 3% and JMD 5,000,000 annual ceiling; accessed 2026-10-24.
- [Laws of Jamaica — National Housing Trust Act](https://lipj.gov.jm/record/79143) — NHT framework; accessed 2026-10-24.
- [Laws of Jamaica — Education Tax Act](https://lipj.gov.jm/record/74988) and [Provisional Collection of Tax (Education Tax) Order 2013](https://lipj.gov.jm/record/80285) — 2.25% employee and 3.5% employer rates; accessed 2026-10-24.
- [Laws of Jamaica — Human Employment and Resource Training Act](https://lipj.gov.jm/record/92035) — employer levy framework and 3% rate; accessed 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
