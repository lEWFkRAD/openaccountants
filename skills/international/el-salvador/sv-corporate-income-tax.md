---
name: sv-corporate-income-tax
description: >-
  El Salvador corporate income tax (Impuesto sobre la Renta, CIT) reference
  for 2026. Covers the 30% rate on Salvadoran-source taxable income under the
  territorial system, the reduced 25% rate up to USD 150,000, the 1.75%
  monthly advance on gross revenues, accrual accounting, inventory methods,
  capital gains inside the CIT, the 30 April annual return, audit windows and
  penalties, and branch/non-resident exposure. Trigger on El Salvador
  corporate tax, CIT El Salvador, pago a cuenta 1.75%, F-10, renta
  sociedades. Source-cited draft.
jurisdiction: SV
category: international
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# El Salvador corporate income tax (CIT)

## 1. Who this applies to

- Companies **incorporated in El Salvador** — resident entities for tax purposes — on Salvadoran-source income (PwC El Salvador corporate residence, read 2026-10-24).
- **Branches of foreign companies authorised in El Salvador** and entities operating through a permanent establishment (PE) are also resident entities for CIT purposes (PwC, read 2026-10-24).
- Source rule: income is Salvadoran-source from goods located in the country, activities performed in the territory, capital invested in the country, and **services rendered or used in El Salvador** — even if paid or performed abroad; securities/financial instruments are Salvadoran-source if the issuing entity is domiciled in El Salvador (PwC corporate CIT, read 2026-10-24).
- Out of scope: individual renta (`el-salvador-income-tax`), IVA (`el-salvador-iva`), ISSS/AFP (`el-salvador-social-contributions`).

## 2. Rates, bands and thresholds

| Item | Amount | Tax year | Source (as_of 2026-10-24) |
|---|---|---|---|
| CIT general rate | 30% of taxable income | 2026 | PwC El Salvador corporate CIT (last reviewed 27 Sep 2026) |
| Reduced CIT rate | 25% where taxable income ≤ USD 150,000 | 2026 | PwC El Salvador corporate CIT |
| Monthly advance (pago a cuenta) | 1.75% of gross revenues accrued, credited against annual CIT | 2026 | PwC corporate CIT / tax administration |
| Capital gains (inside CIT framework) | 10% of net profit; gains within 12 months of purchase taxed as ordinary income; 12-month rule does not apply to securities | 2026 | PwC El Salvador other taxes |
| Municipal income tax | exists; rate depends on location of operations | 2026 | PwC El Salvador corporate CIT |

**Source status:** the consolidated Income Tax Law text did not resolve from the drafting environment on 2026-10-24 — statutory article citations are **needs-sources**; every figure above is corroborated by the PwC pages cited.

## 3. The base

- Taxable income = gross income (collected or accrued, cash or in kind, from Salvadoran sources) less costs and expenses **necessary to generate and maintain the source of income** and other deductions allowed by law; accrual accounting is mandatory for corporations (PwC corporate CIT, read 2026-10-24).
- **AUDIT FLASH POINT** — DGII's stated audit focus includes **deductions and supporting documentation**: an expense without proper vouchers is disallowed outright (PwC tax administration, read 2026-10-24).
- Inventory methods permitted: purchase/manufacturing cost, last purchase cost, direct average, average cost, FIFO, and specific methods for farm products/cattle; changes need prior DGII authorisation (PwC income determination, read 2026-10-24).
- Goodwill, self-developed trademarks and similar self-made intangibles are **not deductible**; interest is deductible only if the loan funds a source of taxable income; bad debts require business origin plus collection-effort evidence (PwC deductions, read 2026-10-24).
- Capital losses offset only capital gains, with a **five-year carry-forward** of the excess (PwC other taxes, read 2026-10-24).
- Territoriality: amounts received from abroad and movements of capital from foreign sources are **excluded from taxable income** (post-reform articles 3, 14-A, 16, 27 — PwC income determination, read 2026-10-24).

## 4. Deadlines and filing

- Fiscal year: 1 January–31 December (PwC tax administration, read 2026-10-24).
- Annual CIT return: filed **no later than 30 April** after year end; tax is paid with the return through the local banking system (PwC, read 2026-10-24).
- Monthly advance: 1.75% of gross revenues, return + payment due **within ten working days following the calendar month**; farm and cattle concerns are excepted from the advance (PwC, read 2026-10-24).

## 5. Penalties and interest

- Audit window: **3 years** for timely-filed returns, **5 years** for late-filed or unfiled returns; payment-obligation limitation **10 years** (PwC tax administration, read 2026-10-24).
- Audit process: auditor-designation resolution → information requirement → complementary documentation → audit report (PwC, read 2026-10-24).
- Interest and surcharges on late payment apply per the fiscal code; exact current rates **needs-sources**.

## 6. Cross-border points

- Branch profits: branches pay the same CIT as domestic companies; profits/dividends paid or credited to the non-domiciled head office, affiliates, branches, subsidiaries or agencies bear **5% withholding (25% if paid to a tax haven)** (PwC branch income, read 2026-10-24).
- PE triggers: fixed place of business; a non-independent agent habitually concluding contracts in the foreign entity's name; construction/installation or supervision projects **exceeding six months** (PwC corporate residence, read 2026-10-24).
- Withholding on outbound payments: see `sv-cross-border-tax`.

## 7. Worked examples

**Example 1 — standard CIT with advance credit.** A Salvadoran S.A. de C.V. has 2026 gross revenues of USD 2,000,000 and taxable income of USD 300,000. Annual CIT: 300,000 × 30% = USD 90,000. Advances paid during 2026: 2,000,000 × 1.75% = USD 35,000. Balance due with the 30 April 2027 return: 90,000 − 35,000 = USD 55,000.

```oa-check
name: sv cit with advance credit
inputs:
  gross_revenues: 2000000
  taxable_income: 300000
steps:
  - cit: taxable_income * 0.30
  - advances: gross_revenues * 0.0175
  - balance: cit - advances
expected:
  cit: 90000.00
  advances: 35000.00
  balance: 55000.00
```

**Example 2 — reduced-rate edge case.** A small Salvadoran company's 2026 taxable income is USD 150,000 — exactly at the reduced-rate ceiling. CIT: 150,000 × 25% = USD 37,500. One dollar more of taxable income moves the whole base to 30%: 150,001 × 30% = USD 45,000.30 — a cliff, not a marginal band.

```oa-check
name: sv reduced rate cliff
inputs:
  ti_at_ceiling: 150000
  ti_one_more: 150001
steps:
  - tax_at_ceiling: ti_at_ceiling * 0.25
  - tax_one_more: ti_one_more * 0.30
expected:
  tax_at_ceiling: 37500.00
  tax_one_more: 45000.30
```

## 8. Ask the client first

1. Are all revenues Salvadoran-source — any services performed abroad but used in El Salvador?
2. Is taxable income near the USD 150,000 reduced-rate cliff?
3. Were the 1.75% monthly advances filed and paid within ten working days each month?
4. Do all deduction vouchers meet DGII documentation standards?
5. Any foreign parent payments (management fees, royalties, interest) that also trigger withholding — see `sv-cross-border-tax`?

## 9. Sources

- [PwC Worldwide Tax Summaries — El Salvador Corporate: Taxes on corporate income](https://taxsummaries.pwc.com/el-salvador/corporate/taxes-on-corporate-income) — read 2026-10-24 (PwC last reviewed 27 Sep 2026).
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Income determination](https://taxsummaries.pwc.com/el-salvador/corporate/income-determination) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Deductions](https://taxsummaries.pwc.com/el-salvador/corporate/deductions) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Corporate residence](https://taxsummaries.pwc.com/el-salvador/corporate/corporate-residence) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Branch income](https://taxsummaries.pwc.com/el-salvador/corporate/branch-income) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Other taxes](https://taxsummaries.pwc.com/el-salvador/corporate/other-taxes) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Tax administration](https://taxsummaries.pwc.com/el-salvador/corporate/tax-administration) — read 2026-10-24.
- Ley de Impuesto sobre la Renta consolidated text — **needs-sources** (unreachable 2026-10-24).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
