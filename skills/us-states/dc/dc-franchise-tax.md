---
name: dc-franchise-tax
description: >
  Use this skill whenever asked about District of Columbia franchise
  tax for tax year 2026 — the 8.25% corporate and unincorporated
  business franchise tax, mandatory combined reporting for unitary
  groups, the $250/$1,000 minimum taxes, the 30% owner salary
  allowance and $5,000 exemption for unincorporated businesses, the
  personal-services exemption, estimated tax (D-20ES/D-30ES, 110%
  safe harbor), and D-20/D-30 return mechanics. Trigger on "DC
  franchise tax", "District of Columbia corporate tax", "DC 8.25
  percent", "DC combined reporting", "DC D-20", "DC D-30", "DC
  minimum franchise tax".
jurisdiction: US-DC
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - dc-income-tax
---

# District of Columbia franchise tax, tax year 2026

> **Source-cited draft.** Built from D.C. Code §§ 47-1807.02, 47-1808.01, 47-1808.03, 47-1810.02, 47-4201 and 47-4213 and the OTR Business Franchise Tax Rates, Combined Reporting and Estimated Tax pages, read on 2026-10-28. No accountant has reviewed it. Do not run a filing from it without review by a qualified professional.

The District's business income tax is the **franchise tax**: **8.25%** of DC-computed net income for corporations and for unincorporated businesses, computed on a **combined-reporting basis** for unitary groups. DC administers it through the **Office of Tax and Revenue (OTR)**. See also `dc-transfer-pricing` (combined-reporting mechanics), `dc-cross-border`, `dc-income-tax` (the D-30 trigger for sole proprietors).

## Who this applies to

- **Corporations** (including financial institutions) with DC-source income, filing on a combined basis for unitary groups ([OTR rates page](https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates); [OTR combined reporting page](https://otr.cfo.dc.gov/page/combined-reporting-business-entities)). Corporations and financial institutions cannot escape the minimum tax even with exempt business income (note read from the OTR rates page).
- **Unincorporated businesses** (partnerships, LLCs, sole proprietorships) with DC gross receipts over **$12,000**: the OTR rates page applies the franchise tax to unincorporated businesses "on a combined reporting basis with gross receipts more than $12,000".
- **Exemption:** an unincorporated business is exempt where more than 80% of gross income is personal services rendered by members and capital is not a material income-producing factor; also entities that by law, customs or ethics cannot incorporate (OTR rates page, read 2026-10-28; [D.C. Code § 47-1808.01](https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.01)) — a critical rule for professional practices.

## Rates, bands and thresholds

| Item | Rate / base | Source |
|---|---|---|
| Corporate franchise tax | **8.25%** of taxable income, for taxable years beginning after 31 December 2017 (so 2018 through 2026) | [D.C. Code § 47-1807.02(a)(8)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1807.02): "For taxable years beginning after December 31, 2017, a tax at the rate of 8.25% upon the taxable income of every corporation, whether domestic or foreign"; OTR rates page table (2018–2025) |
| Unincorporated franchise tax | **8.25%** of taxable income, same period | [D.C. Code § 47-1808.03(a)(8)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.03): "For taxable years beginning after December 31, 2017, a tax at the rate of 8.25% upon the taxable income of every unincorporated business, whether domestic or foreign" |
| Minimum tax | **$250** (DC gross receipts ≤ $1M) / **$1,000** (> $1M) | § 47-1807.02(b) / § 47-1808.03(b): "The minimum tax payable under this section shall be $250. If District gross receipts are greater than $1 million..."; OTR rates page: "$250 minimum tax, if DC gross receipts are $1 million or less" |
| Unincorporated deductions | 30% salary allowance for owners + $5,000 exemption, deducted from net income to reach taxable income | OTR rates page: "A 30% salary allowance for owners and a $5,000 exemption are deductible from net income to arrive at taxable income" |
| Filing trigger (unincorporated) | DC gross receipts > $12,000 | OTR rates page |
| Apportionment | Single sales factor | [D.C. Code § 47-1810.02(d-2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02): "All business income shall be apportioned to the District by multiplying the income by the sales factor" |

## The taxable base

- The base is **DC-computed net income** on a **combined-reporting basis** for unitary groups: for taxable years beginning on or after 1 January 2011, a business "engaged in a unitary business with one or more corporations or unincorporated business entities" must file a combined franchise-tax return ([OTR combined reporting page](https://otr.cfo.dc.gov/page/combined-reporting-business-entities)).
- Unincorporated businesses deduct the 30% owner salary allowance and the $5,000 exemption from net income before applying the 8.25% rate (OTR rates page).
- Business income is apportioned to DC by the **sales factor alone** ([§ 47-1810.02(d-2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02)); intragroup transactions are eliminated in combination (see `dc-transfer-pricing`).

## Deadlines and filing

- **Estimated tax:** required when the year's DC franchise tax liability is more than **$1,000**; calendar-year filers pay **15 April, 15 June, 15 September and 15 December**; fiscal filers on the 15th day of months 4, 6, 9 and 12 of the tax year ([OTR estimated tax page](https://otr.cfo.dc.gov/page/underpayment-estimated-tax-interest): "Estimated tax payments are due: Calendar Year Filers: April 15; and June 15; and September 15; and December 15"). Corporations use the D-20ES vouchers and unincorporated businesses the D-30ES (same page).
- **Safe harbor:** no underpayment interest where the current year's liability is less than $1,000, there was no DC franchise tax liability in the preceding year, estimated payments equal or exceed **110% of the preceding year's liability**, or the remaining balance after credits and estimates is less than 10% of the year's liability (OTR estimated tax page). Annualization uses **Form D-2220** (same page).
- **Returns:** D-20 (corporate) / D-30 (unincorporated). Form-level due dates were not read from an archived OTR return instruction this run — see the Not yet confirmed line and the current D-20/D-30 instructions.

## Penalties and interest

- **Failure-to-file / failure-to-pay additions:** 5% a month up to 25% each, with the failure-to-file addition reduced by the failure-to-pay addition for the same months; neither applies with reasonable cause ([D.C. Code § 47-4213](https://code.dccouncil.gov/us/dc/council/code/sections/47-4213), archived 2026-10-28 as `US-DC-47-4213.html`).
- **Interest** on unpaid tax runs at **10% a year, compounded daily** ([D.C. Code § 47-4201](https://code.dccouncil.gov/us/dc/council/code/sections/47-4201), archived 2026-10-28 as `US-DC-47-4201.html`). Businesses compute estimated-tax underpayment interest on **Form D-2220** (OTR estimated tax page); individuals use the D-2210.
- Common failure modes: (1) professional LLCs assuming the individual return covers everything — the unincorporated franchise tax applies unless the 80% personal-services exemption is documented; (2) forgetting the owner-salary allowance when computing the D-30 base; (3) 100%-of-prior-year accruals when DC's safe harbor is **110%**; (4) minimum tax missed by exempt-income corporations.

## Cross-border points

- Combined reporting pulls out-of-District unitary affiliates into the DC computation (see `dc-transfer-pricing`).
- DC sources and apportions income under D.C. Code Title 47 ch. 18: business income by the **single sales factor** ([§ 47-1810.02(d-2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02)).
- No DC entity exit-tax regime is described in the archived sources; non-resident entity taxation runs through DC-source combined income (see `dc-cross-border`).

## Worked examples

Client facts below are hypothetical; all rates and thresholds are the confirmed figures from the tables above.

**An unincorporated business with $200,000 DC net income** (gross receipts well over $12,000, no personal-services exemption):

```oa-check
name: DC unincorporated franchise tax with salary allowance
inputs:
  net_income: 200000
  salary_pct: 0.30
  exemption: 5000
  rate: 0.0825
steps:
  - salary_allowance: net_income * salary_pct
  - base: net_income - salary_allowance - exemption
  - tax: base * rate
expected:
  salary_allowance: 60000.00
  base: 135000.00
  tax: 11137.50
```

**A corporation with $1,000,000 DC-apportioned combined net income:**

```oa-check
name: DC corporate franchise tax
inputs:
  base: 1000000
  rate: 0.0825
steps:
  - tax: base * rate
  - min_check: max(tax, 1000)
expected:
  tax: 82500.00
  min_check: 82500.00
```

## Ask the client first

- Does the entity qualify for the 80% personal-services exemption — is the capital-not-material test documented?
- Are estimated payments tracking the 110% safe harbor (not 100%)?
- Is the owner-salary allowance being claimed correctly on the D-30?
- Part of a unitary group? The combined report is mandatory — see `dc-transfer-pricing`.
- DC gross receipts relative to $12,000 (unincorporated filing trigger) and $1 million (minimum-tax tier)?

## Sources

| Source | URL | Read on |
|---|---|---|
| D.C. Code § 47-1807.02 (corporate rate and minimum tax) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1807.02 | 2026-10-28 |
| D.C. Code § 47-1808.03 (unincorporated business rate and minimum tax) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.03 | 2026-10-28 |
| D.C. Code § 47-1810.02 (apportionment; single sales factor) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02 | 2026-10-28 |
| D.C. Code § 47-1808.01 (unincorporated business; personal-services exemption) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.01 | 2026-10-28 |
| D.C. Code § 47-4213 (failure-to-file/pay additions) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4213 | 2026-10-28 |
| D.C. Code § 47-4201 (interest, 10% compounded daily) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4201 | 2026-10-28 |
| OTR: DC Business Franchise Tax Rates | https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates | 2026-10-28 |
| OTR: Combined Reporting of Business Entities | https://otr.cfo.dc.gov/page/combined-reporting-business-entities | 2026-10-28 |
| OTR: Estimated Tax Requirement / Underpayment Interest | https://otr.cfo.dc.gov/page/underpayment-estimated-tax-interest | 2026-10-28 |

Not yet confirmed: the D-20 and D-30 return due dates and form-line mechanics (not read from an archived return instruction this run); the water's-edge treatment of foreign affiliates in a DC combined group; and the 2026 row of OTR's rate table (its published table lists 2018 through 2025, while the statutory 8.25% rate in D.C. Code §§ 47-1807.02(a)(8) and 47-1808.03(a)(8) applies to all taxable years beginning after 31 December 2017).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
