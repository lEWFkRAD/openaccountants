---
name: aw-payroll-withholding
description: >-
  Use for Aruba payroll withholding (loonbelasting): the employer's role
  as withholding agent for wage tax plus employee social-insurance
  premiums (AOV/AWW 5%, AZV 1.6% on the Afl. 85,000 base), the
  annualize-deduct-table-prorate withholding computation with the 3%
  cost deduction capped at Afl. 1,500, the 2026 table and Afl. 30,000
  tax-free amount, part-year pro-ration, and the VZL/VOD annual
  statements. Trigger on Aruba loonbelasting, Aruba payroll withholding,
  Aruba employer wage tax. Source-cited draft; DIMP verified 2026-10-27;
  monthly payment deadline needs-sources.
jurisdiction: AW
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Aruba payroll withholding (loonbelasting en premies)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status (2026-10-27):** DIMP pages verified HTTP 200 with real content: <https://www.impuesto.aw/loonbelasting-en-premies> (employer withholds loonbelasting + premies volksverzekeringen and remits to DIMP; VZL/VOD statements; statute PDFs) and <https://www.impuesto.aw/hoeveel-loonbelasting-houdt-u-in-en-draagt-u-af> — the worked withholding mechanics page (its example uses 2019 figures; the 2026 table and tax-free amount come from the existing `aw-individual-income-tax` skill, DIMP 2026 table verified 22 Oct 2026). **needs-sources:** the monthly loonbelasting filing/payment deadline (the BBO 15th-of-following-month rule is verified for turnover taxes only), and current tables of withholding surcharges.

## 1. Who this applies to

- **Every Aruba employer (inhoudingsplichtige):** withholding runs on gross wages for employees, including seconded and part-time staff in an Aruba service relationship.
- **Self-employed without staff** pay through the inkomstenbelasting route instead (DIMP loonbelasting-en-premies, verified 2026-10-27).
- **Foreign employers with Aruba staff** — an Aruba payroll presence creates the withholding obligation; a posted-worker analysis belongs with `aw-cross-border-tax`.

## 2. Rates and key rules

| Item | Value | Source |
|---|---|---|
| Wage tax | Table of inkomstenbelasting/loonbelasting applied to table income (2026: 21%/42%/52% bands) | DIMP 2026 table, carried from `aw-individual-income-tax` |
| Tax-free amount (max) | Afl. 30,000 annually; **pro-rated time-wise for part-year withholding** | DIMP 2026 (existing skill); pro-ration rule from DIMP withholding page |
| Employee cost deduction in withholding | 3% of gross, **capped at Afl. 1,500** | DIMP withholding mechanics page, verified 2026-10-27 |
| Employee AOV/AWW premium withheld | 5% on base capped at Afl. 85,000 | DIMP withholding page + SVB 2026 (existing skill) |
| Employee AZV premium withheld | 1.6% on base capped at Afl. 85,000 | same |
| Employer premiums (AOV/AWW 10.5%, AZV 8.9%, ZV/OV, Cessantia) | See `aw-social-contributions` | SVB 2026 schedule |
| Annual statements | Verzamelloonstaat (VZL) and Verzamelstaat opgaaf derden (VOD) | DIMP loonbelasting-en-premies, verified 2026-10-27 |

## 3. Base and mechanics

DIMP's withholding computation (verified 2026-10-27; example figures on the page are 2019 — 2026 parameters substituted):

1. **Annualize** the gross wage (voljaarsloon).
2. **Deduct:** 3% costs (max Afl. 1,500), employee AOV/AWW (5% × capped base), employee AZV (1.6% × capped base) → zuiver voljaarsloon.
3. **Table income** = zuiver voljaarsloon − tax-free amount (max Afl. 30,000; pro-rated if the employee is not subject for the full year).
4. **Apply the 2026 table** (see `aw-individual-income-tax`); round the annual amount down to whole florins.
5. **Divide by the number of pay periods** and withhold each period.

## 4. Deadlines and filings

- Monthly remittance of withheld loonbelasting and premiums: deadline **needs-sources** (not verified this run; do not assume the BBO 15th rule).
- VZL/VOD annual statements: filing window **needs-sources**.
- Assessment payment terms once assessed: usually 2 months; holiday shift to next working day (DIMP wanneer-moet-u-betalen, verified 2026-10-27).

## 5. Penalties and interest

- Employer is the debtor for what it failed to withhold — surcharge/interest percentages **needs-sources**.
- Late payment of assessments: extra costs after the due date (DIMP wanneer-moet-u-betalen, verified 2026-10-27).

## 6. Cross-border notes

- **Part-year employees:** the tax-free amount is reduced time-wise (pro rata dagen) — a mid-year joiner/leaver must not get the full Afl. 30,000 (DIMP withholding page, verified 2026-10-27).
- **Non-resident employees** working in Aruba: withholding still applies on Aruba wages; the employee may also be a buitenlandse belastingplichtige (see `aw-cross-border-tax`).
- **Benefits in kind and cost reimbursements** enter the wage base per the ministerial rules on onbelaste kostenvergoedingen (PDF linked from DIMP loonbelasting page; detail **needs-sources**).

## 7. Worked examples

**Example 1 — full-year employee, 2026.** Gross monthly wage Afl. 8,000, no benefits in kind, no pension scheme.

```oa-check
name: aw pr fullyear 8000
inputs:
  gross_month: 8000
steps:
  - annual: 12 * gross_month
  - kosten: min(0.03 * annual, 1500)
  - aov_emp: 0.05 * 85000
  - azv_emp: 0.016 * 85000
  - zuiver: annual - kosten - aov_emp - azv_emp
  - tabel: zuiver - 30000
  - tax: 0.21 * (tabel - 34930)
  - tax_rounded: floor(tax)
  - per_month: tax_rounded / 12
expected:
  annual: 96000.00
  kosten: 1500.00
  zuiver: 88890.00
  tabel: 58890.00
  tax: 5031.60
  tax_rounded: 5031.00
  per_month: 419.25
```

**Example 2 — part-year employee (6 months).** Gross monthly Afl. 5,000 for 6 months; DIMP annualizes the wage and pro-rates the tax-free amount time-wise (6/12 × 30,000).

```oa-check
name: aw pr partyear 6m
inputs:
  gross_month: 5000
  months: 6
steps:
  - annualized: 12 * gross_month
  - kosten: min(0.03 * annualized, 1500)
  - prem_base: min(85000, annualized)
  - aov_emp: 0.05 * prem_base
  - azv_emp: 0.016 * prem_base
  - zuiver: annualized - kosten - aov_emp - azv_emp
  - vrij: clamp(30000 * months / 12, 0, 30000)
  - tabel: zuiver - vrij
  - tax_annual: 0.21 * (tabel - 34930)
  - tax_rounded: floor(tax_annual)
  - per_month: tax_rounded / months
expected:
  annualized: 60000.00
  kosten: 1500.00
  prem_base: 60000.00
  zuiver: 54540.00
  vrij: 15000.00
  tabel: 39540.00
  tax_annual: 968.10
  tax_rounded: 968.00
  per_month: 161.33
```

*(The pro-rated tax-free amount is DIMP's stated rule; applying the annualized procedure — including the premium base — to a part-year worker is the consistent reading but is flagged **needs-sources**: confirm against a current DIMP toelichting before running payroll, and reconcile via the employee's annual return.)*

## 8. Ask the client first

1. Is there an Aruba employment relationship (dienstbetrekking) — the withholding trigger — or a foreign payroll posting?
2. Full-year or part-year employee — the tax-free amount must be pro-rated.
3. Benefits in kind, cost reimbursements, pension scheme — each changes the wage base.
4. Are the employee-side premiums (AOV/AWW, AZV) actually being withheld on the capped base?
5. Are VZL/VOD annual statements filed — DIMP reconciles withholding against them.

## 9. Sources

- DIMP — Loonbelasting en Premies (employer withholding role, VZL/VOD, statute PDFs): <https://www.impuesto.aw/loonbelasting-en-premies> — verified 200 with text 2026-10-27.
- DIMP — Hoeveel loonbelasting houdt u in en draagt u af? (withholding mechanics, 3%/Afl. 1,500 cost deduction, pro-rated tax-free amount): <https://www.impuesto.aw/hoeveel-loonbelasting-houdt-u-in-en-draagt-u-af> — verified 200 with text 2026-10-27.
- DIMP — 2026 income/wage tax table: carried from `aw-individual-income-tax` (verified 22 Oct 2026).
- SVB 2026 tariff schedule: carried from `aw-social-contributions` (verified 22 Oct 2026).
- Landsverordening loonbelasting (PDF linked from DIMP; article text **needs-sources** this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
