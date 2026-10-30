---
name: id-income-tax
description: "Idaho Individual Income Tax Return (Form 40) for sole proprietors and single-member LLCs. Covers the flat 5.3% rate (tax year 2025), Idaho taxable income computation from federal taxable income, the 2025 exemption amounts ($4,811 single / $9,622 joint, head of household, qualifying surviving spouse), the 2025 standard deduction, and the inflation-adjusted tax threshold ($2,500 single / $5,000 joint statutory base). Trigger: taxpayer is an Idaho resident or has Idaho-source gross income exceeding $2,500."
version: "0.3"
jurisdiction: US-ID
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Idaho individual income tax (Form 40), tax year 2025

> **Source-cited draft.** Built from Idaho Code §§ 63-3002, 63-3024, 63-3025, 63-3030 and 63-3032 (Idaho Legislature statutes pages) and the Idaho State Tax Commission's 2025 Form 40 return and instructions, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Scope.** Idaho Form 40 (Individual Income Tax Return) for sole proprietors and single-member LLCs whose business income flows through federal taxable income. The Idaho State Tax Commission (tax.idaho.gov) administers the tax. Idaho taxable income starts from federal taxable income, subject only to the modifications contained in Idaho law (Idaho Code §63-3002: it is the intent of the legislature "to make the provisions of the Idaho act identical to the provisions of the Federal Internal Revenue Code relating to the measurement of taxable income ... subject only to modifications contained in the Idaho law").

This skill does NOT cover corporate returns (Form 41), partnership/S-corp pass-throughs, or detailed multi-state apportionment. See the corporate rate context in the rates table for §63-3025.

## Who this applies to

- **Resident individuals** required to file a federal return under IRC §6012(a)(1) must file an Idaho return (Idaho Code §63-3030(a)(1)).
- **Nonresident individuals** with gross income from Idaho sources in excess of $2,500 for the taxable year must file (Idaho Code §63-3030(a)(2): "Any nonresident individual having for the current taxable year a gross income from Idaho sources in excess of two thousand five hundred dollars ($2,500)"). Part-year residents with combined Idaho-source and Idaho-period gross income over the same $2,500 threshold must file.
- **Estates and trusts:** every Idaho-resident estate with gross income of $600 or more, nonresident estates with Idaho-source gross income over $600, and Idaho-resident trusts with gross income of $100 or more (Idaho Code §63-3030(a)(5)–(7)).
- **Sole proprietors and single-member LLCs:** business profit is reported on the federal return (Schedule C) and flows into federal taxable income, which is the starting point for the Idaho return (Idaho Code §63-3002).

## Rates, bands and thresholds

**Individual income tax rates (Idaho Code §63-3024)**

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Individual rate | Flat 5.3% of taxable income over $2,500 (single, all filers other than joint) | current (2025) | [Idaho Code §63-3024(2)(a)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3024/) |
| Joint-return rate | Flat 5.3% of taxable income over $5,000 (joint returns; surviving-spouse and head-of-household returns are treated as joint) | current (2025) | [Idaho Code §63-3024(2)(b)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3024/) |
| Threshold indexation | State Tax Commission prescribes an annual CPI-U factor (CPI of the preceding calendar year ÷ CPI for 1998) applied to the $2,500/$5,000 thresholds so inflation does not raise tax | 2000 and thereafter | [Idaho Code §63-3024(3)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3024/) |
| 2025 exemption (Form 40 worksheet) | $4,811 single or married filing separately; $9,622 married filing jointly, head of household, or qualifying surviving spouse; subtracted before applying the 5.3% rate | 2025 | [Form 40 return and instructions 2025](https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf) |
| 2025 standard deduction | $15,750 single or married filing separately; $23,625 head of household; $31,500 married filing jointly or qualifying surviving spouse | 2025 | [Form 40 return and instructions 2025](https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf) |
| Nonresident/part-year filing trigger | Gross income from Idaho sources over $2,500 | current (2025) | [Idaho Code §63-3030(a)(2)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3030/) |
| Estate/trust filing triggers | Idaho-resident estate gross income $600 or more; nonresident estate Idaho-source income over $600; Idaho-resident trust gross income $100 or more | current (2025) | [Idaho Code §63-3030(a)(5)–(7)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3030/) |
| Corporate rate (context) | 5.3% for tax years commencing on and after January 1, 2025; ladder: 7.6% (2001), 7.4% (2012), 6.925% (2018), 6.5% (2021), 6% (2022), 5.8% (2023), 5.695% (2024), 5.3% (2025); minimum tax $20 | current (2025) | [Idaho Code §63-3025](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3025/) |

The statute reads: "The tax imposed upon individuals, trusts, and estates shall be computed at the rate of five and three-tenths percent (5.3%) of taxable income over two thousand five hundred dollars ($2,500)" (§63-3024(2)(a)), with joint returns at 5.3% over $5,000 (§63-3024(2)(b)).

## The taxable base

Idaho taxable income is derived from the federal return. The legislature's declared intent is that taxable income reported to the IRS "shall be the identical sum reported to this state, subject only to modifications contained in the Idaho law" (Idaho Code §63-3002). In practice on Form 40: start from federal adjusted gross income (federal Form 1040 line 11), apply Idaho additions and subtractions, deduct the Idaho standard deduction (or itemized deductions), and subtract the exemption amount. The Form 40 tax worksheet for 2025 is: taxable income, minus the exemption ($4,811 or $9,622 per the filing-status amounts above), with the result multiplied by 5.3% (Form 40 instructions, line 20 worksheet).

For trusts that are electing small business trusts under IRC §1361, the individual rate in §63-3024(2)(a) applies (Idaho Code §63-3024(4)).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Calendar-year individual return (Form 40) | On or before the fifteenth day of April following the close of the calendar year | [Idaho Code §63-3032(1)(a)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3032/) |
| Fiscal-year individual return | On or before the fifteenth day of the fourth month following the close of the fiscal year | [Idaho Code §63-3032(1)(a)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3032/) |
| Short-period return | By the later of the date required by §63-3032 or the date required for the period by the Internal Revenue Code | [Idaho Code §63-3032(1)(b)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3032/) |
| Farmers' cooperative returns (to the extent taxable under §63-3025B) | September 15 following the close of the calendar year (fifteenth day of the ninth month for fiscal years); §63-3033 extensions do not apply | [Idaho Code §63-3032(2)](https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3032/) |

## Penalties and interest

Penalty and interest amounts for late filing and late payment by individuals are listed under Not yet confirmed -- no archived primary source for them is in the evidence set yet, so this skill computes none and asserts none.

## Cross-border points

- **Nonresidents** file when gross income from Idaho sources exceeds $2,500 for the year (Idaho Code §63-3030(a)(2)).
- **Part-year residents** file when gross income from all sources while an Idaho resident, plus Idaho-source income while a nonresident, exceeds $2,500 in total (Idaho Code §63-3030(a)(2)).
- **S corporations** transacting or authorized to transact business in Idaho must file and identify as S corporations for the same periods their federal election is effective (Idaho Code §63-3030(a)(4)).
- **Residents are taxed on Idaho taxable income wherever derived; nonresidents only on income from activity within or derived from sources within Idaho** (Idaho Code §63-3002).

## Worked examples

### Worked example 1: hypothetical single sole proprietor, 2025

Maria is a hypothetical single sole proprietor with 2025 Idaho taxable income of $60,000 after her standard deduction. She has no dependents.

Per the 2025 Form 40 tax worksheet: subtract the $4,811 single exemption from $60,000, leaving $55,189, and multiply by the 5.3% rate: $55,189 × 5.3% = $2,925.02 of Idaho tax. Client facts are hypothetical; only the 5.3% rate and the $4,811 exemption are confirmed figures from the rates table above.

```oa-check
name: Maria, single sole proprietor, $60,000 Idaho taxable income (2025)
inputs:
  taxable_income: 60000
  exemption_single: 4811
  rate: 0.053
steps:
  - tax_base: taxable_income - exemption_single
  - idaho_tax: tax_base * rate
expected:
  tax_base: 55189
  idaho_tax: 2925.02
```

### Worked example 2: hypothetical married-filing-joint SMLLC owner, 2025

Dan and his spouse file jointly (hypothetical facts) with 2025 Idaho taxable income of $100,000 after their standard deduction. The joint exemption is $9,622: ($100,000 − $9,622) × 5.3% = $90,378 × 5.3% = $4,790.03 of Idaho tax. Only the 5.3% rate and the $9,622 joint exemption are confirmed figures from the rates table above.

```oa-check
name: Dan, married filing jointly, $100,000 Idaho taxable income (2025)
inputs:
  taxable_income: 100000
  exemption_joint: 9622
  rate: 0.053
steps:
  - tax_base: taxable_income - exemption_joint
  - idaho_tax: tax_base * rate
expected:
  tax_base: 90378
  idaho_tax: 4790.03
```

## Ask the client first

1. **Residency status for the year** -- resident, part-year, or nonresident? This sets the $2,500 Idaho-source gross-income trigger (Idaho Code §63-3030(a)(2)).
2. **Filing status and dependents** -- this sets the exemption ($4,811 or $9,622) and the standard deduction ($15,750 / $23,625 / $31,500) used in the Form 40 tax worksheet.
3. **Federal taxable income and any Idaho modifications** -- Idaho starts from the federal figures (Idaho Code §63-3002); unresolved federal items flow straight into the Idaho return.
4. **Business form** -- sole proprietor or single-member LLC (this skill), or corporation/S-corp (see the §63-3025 corporate rates for context and route complex pass-throughs out)?
5. **Estimated payments made during the year** -- needed to compute balance due with the return.

## Sources

| Source | URL | Read on |
|---|---|---|
| Idaho Code §63-3002, Declaration of intent (income taxable identical to federal, subject to Idaho modifications) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3002/ | 2026-10-28 |
| Idaho Code §63-3024, Individuals' tax and tax on estates and trusts (5.3% rate; $2,500/$5,000 thresholds; CPI-U indexation factor) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3024/ | 2026-10-28 |
| Idaho Code §63-3025, Tax on corporate income (rate ladder to 5.3% for 2025; $20 minimum) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3025/ | 2026-10-28 |
| Idaho Code §63-3030, Persons required to make returns of income (residents, nonresident $2,500 trigger, estates $600, trusts $100) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3030/ | 2026-10-28 |
| Idaho Code §63-3032, Time for filing income tax returns (fifteenth day of April; fiscal-year rule) | https://legislature.idaho.gov/statutesrules/idstat/Title63/T63CH30/SECT63-3032/ | 2026-10-28 |
| Idaho State Tax Commission, Form 40 Individual Income Tax Return and Instructions 2025 (exemption worksheet $4,811/$9,622 at 5.3%; standard deduction $15,750/$23,625/$31,500) | https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf | 2026-10-28 |

Not yet confirmed: Idaho individual late-filing and late-payment penalty percentages and the interest rate (no archived primary source yet); the exact 2025 inflation-adjusted tax threshold the State Tax Commission prescribed from the §63-3024(3) CPI-U factor (the statutory base $2,500/$5,000 is confirmed; the adjusted 2025 dollar amount is not); itemized-deduction rules and Idaho addition/subtraction items beyond §63-3002's general statement (e.g., the specific modification statutes); the Permanent Building Fund $10 mechanics in detail; estimated-payment requirements and due dates.

> Contributed by Michael Cutajar.

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
