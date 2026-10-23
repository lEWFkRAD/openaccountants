---
name: kn-income-tax-individuals
description: >
  Saint Kitts and Nevis individual income tax reference for 2026. Covers the
  progressive chargeable-income schedule to 55%, personal allowances and
  deductions, the non-domiciliary local-source regime, quarterly instalments,
  filing deadlines, penalties and interest. Uses the official Law Commission
  consolidation of the Income Tax Act (Cap. 18.22) plus the 2021 amendment.
  Use after residence, domicile and the income year have been established.
  Post-2017 Finance Act reconciliation and accountant review remain open;
  this is a source-cited draft.
jurisdiction: KN
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Saint Kitts and Nevis individual income tax

## 1. Scope and sources

Source-cited draft checked 22 October 2026. The operative text is the Income Tax Act, Cap. 18.22 of the Revised Laws of Saint Christopher and Nevis, official consolidation with revision date 31 December 2017, read in full from the Law Commission site, plus the Income Tax (Amendment) Act 2021 (Act 14 of 2021), also read. All amounts are East Caribbean dollars (XCD, pegged USD 2.70). **Caveat: the consolidation is not a complete post-2017 amendment audit; re-check the schedule against the current Finance Act before filing.**

## 2. Who is charged

- A **resident** is charged on income wherever arising (residence follows the Income Tax Act's residence rules, including the physical-presence tests).
- A **non-resident** is charged on income arising in Saint Christopher and Nevis.
- A person **domiciled outside** the Federation who is otherwise chargeable may elect the section 32 regime: chargeable income is limited to (a) income arising in Saint Christopher and Nevis, (b) income received in or remitted to the Federation, and (c) income treated as arising there. Foreign-salary income of a non-domiciliary employed wholly outside the Federation is excluded. This is the key rule for citizenship-by-investment clients.

## 3. Rates

Schedule to the Income Tax Act (individuals), as consolidated:

| Source | All bands below | [Income Tax Act, Cap. 18.22, Schedule](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_22-Income-Tax-Act.pdf) |
|---|---|---|
| First EC$500 | 0% | |
| EC$501 – 1,000 | 5% | |
| EC$1,001 – 1,500 | 7.5% | |
| EC$1,501 – 2,000 | 10% | |
| EC$2,001 – 2,500 | 12.5% | |
| EC$2,501 – 3,000 | 15% | |
| EC$3,001 – 4,000 | 20% | |
| EC$4,001 – 5,500 | 25% | |
| EC$5,501 – 7,000 | 32.5% | |
| EC$7,001 – 9,000 | 40% | |
| EC$9,001 – 11,000 | 47.5% | |
| Above EC$11,000 | 55% | |

The 2021 amendment (Act 14 of 2021) raised the top band to 55% above EC$11,000; the consolidated text above already reflects it.

## 4. Allowances and deductions

From the consolidated Act (as amended to 2017; verify current amounts against the Finance Act):

| Item | Amount | Basis |
|---|---:|---|
| Deduction for employed persons (10% of employment income) | max EC$750 | s.28 |
| Personal allowance | EC$1,200 | s.29 |
| Age allowance (60+) | EC$750 | s.29 |
| Child education allowance | EC$400 per child, max 2 | s.29 |
| Mortgage interest relief | 50% of interest, max EC$1,000 | s.29 |
| Annuity/pension income abatement | 20%, max EC$1,000 | s.29 |

Chargeable income = total income less allowable deductions and allowances.

## 5. Deadlines

- Annual return for a year of income: file by **30 April** following the year of income (s.33; verify against current practice).
- **Instalments** (s.67): four quarterly payments on 15 March, 15 June, 15 September and 15 December, each one quarter of estimated tax at the s.32 rates.
- Tax assessed by notice is due within one month of the notice (s.66).

## 6. Penalties and interest

Tax Administration and Procedures Act, Cap. 20.52:

- Late filing: 5% of tax owing plus EC$100 per month (or part) of continuing failure; EC$1,000 per month for exempt-entity filers (s.37, as amended by Acts 7 of 2014 and 5 of 2016).
- Underpayment from fraud or negligence: 25% of the underpayment (s.38).
- Interest on unpaid tax: 12% per annum from due date to payment (s.22).

## 7. Cross-border points

- No comprehensive treaty network; unilateral relief only under the Double Taxation (Relief) Act, Cap. 18.26, for designated territories.
- Non-domiciliary local-source regime: see section 2 and the `kn-cross-border` skill.
- Employment withholding (PAYE) generally discharges the liability for employees with a single employer — see `kn-payroll-withholding`.

## 8. Worked examples

**Example 1 — resident employee, EC$30,000 employment income, two school-age children.**
Deduction for employed persons: min(10% × 30,000, 750) = 750. Allowances: 1,200 personal + 750 age (assume 60+) + 2 × 400 child education = 2,750; total deductions 3,500. Chargeable income 26,500. Schedule tax on the first 11,000 = 3,062.50; top band (26,500 − 11,000) × 55% = 8,525.00. Total 11,587.50.

```oa-check
name: Resident employee EC$30,000, age 60+, two children
inputs:
  income: 30000
steps:
  - emp_deduction: min(0.10 * income, 750)
  - allowances: emp_deduction + 1200 + 750 + 2 * 400
  - chargeable: income - allowances
  - first_11000: 500*0.05 + 500*0.075 + 500*0.10 + 500*0.125 + 500*0.15 + 1000*0.20 + 1500*0.25 + 1500*0.325 + 2000*0.40 + 2000*0.475
  - top_band: (chargeable - 11000) * 0.55
  - tax: first_11000 + top_band
expected:
  tax: 11587.50
```

**Example 2 — non-domiciliary with EC$8,000 local-source rent, no local employment.**
Under s.32 only the local income is chargeable. Deduction for employed persons does not apply (no employment). Personal allowance 1,200. Chargeable 6,800. Schedule tax: bands to 5,500 = 825.00; (6,800 − 5,500) × 32.5% = 422.50. Total 1,247.50.

```oa-check
name: Non-domiciliary, EC$8,000 local rent
inputs:
  income: 8000
steps:
  - allowances: 1200
  - chargeable: income - allowances
  - to_5500: 500*0.05 + 500*0.075 + 500*0.10 + 500*0.125 + 500*0.15 + 1000*0.20 + 1500*0.25
  - top_band: (chargeable - 5500) * 0.325
  - tax: to_5500 + top_band
expected:
  tax: 1247.50
```

## 9. Ask the client first

1. Residence and domicile status — and whether the s.32 non-domiciliary election applies.
2. All income streams: local employment, local rents, foreign income received or remitted locally.
3. Age, dependants and mortgage interest — they change the allowances.
4. Whether PAYE already discharged the tax on employment income.

## 10. Sources

- [Income Tax Act, Cap. 18.22 (consolidation, revision date 31 Dec 2017)](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_22-Income-Tax-Act.pdf) — read 2026-10-22.
- Income Tax (Amendment) Act 2021 — verified via Law Commission publications.
- [Tax Administration and Procedures Act, Cap. 20.52](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf) — read 2026-10-22.
