---
name: nc-income-tax
description: Use this skill whenever asked about North Carolina individual income tax for self-employed / sole proprietors. Trigger on phrases like "North Carolina income tax", "NC income tax", "Form D-400", "NCDOR income tax", "NC self-employment tax".
version: "0.2"
jurisdiction: US-NC
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NC Income Tax

## North Carolina Individual Income Tax Skill — Self-Employed / Sole Proprietor

> **Scope.** This skill covers North Carolina Form D-400 (Individual Income Tax Return) for full-year NC residents who are sole proprietors or single-member LLC owners. Tax year 2025 (returns filed in 2026). North Carolina uses a flat income tax rate.
>
> **Quality tier.** Q3 — AI-drafted, not independently verified. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

## Section 1: Metadata

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax |
| Jurisdiction | North Carolina (US-NC) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form D-400 |
| Supporting schedules | D-400 Schedule S (Additions/Deductions), D-400TC (Tax Credits), D-400 Schedule A (NC Itemized Deductions) |
| Tax structure | Flat rate |
| Tax rate | 4.25% (TY 2025) — NCDOR 2025 D-401 Instructions (archived) |
| Filing deadline | April 15, 2026 |
| Extension deadline | October 15, 2026 |
| Tax authority | North Carolina Department of Revenue (NCDOR) |
| Website | https://www.ncdor.gov |
| Statute | N.C.G.S. Chapter 105 (archived chapter text: https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/ByChapter/Chapter_105.html); individual income tax provisions §§ 105-153 to 105-153.11 (sections archived: 105-153.2, 105-153.4, 105-153.5, 105-153.6, 105-153.7, 105-153.8) |

**Sources:**
- NCDOR, Tax Rate Schedules: https://www.ncdor.gov/taxes-forms/individual-income-tax/tax-rate-schedules
- NCDOR, 2025 D-401 Individual Income Tax Instructions: https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open
- Session Law 2023-134 (rate schedule for future years)

## Rates, bands and thresholds

## Section 2: Quick reference — rates and thresholds

### Tax rate

**Tax rate schedule**  _(Session Law 2023-134; NCDOR Tax Rate Schedules)_

| Tax year | Rate | Source |
| --- | --- | --- |
| 2025 | 4.25% | Session Law 2023-134; NCDOR Tax Rate Schedules |
| 2026 | 3.99% | Session Law 2023-134; NCDOR Tax Rate Schedules |

North Carolina applies a single flat rate to all taxable income regardless of filing status or income level.

### Standard deduction (TY 2025)

**Standard deduction table**

| Filing status | Standard deduction |
| --- | --- |
| Single | $12,750 |
| Married filing jointly | $25,500 |
| Married filing separately | $12,750 |
| Head of household | $19,125 |

### Child deduction (TY 2025)

**Child deduction table**

Thresholds are federal AGI-based, per the archived 2025 D-401 Child Deduction Table:

| Filing status | AGI up to | $3,000 | then $2,500 | then $2,000 | then $1,500 | then $1,000 | then $500 | $0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MFJ/QSS | tiers | ≤$40,000 | $40,001–60,000 | $60,001–80,000 | $80,001–100,000 | $100,001–120,000 | $120,001–140,000 | >$140,000 |
| Head of household | tiers | ≤$30,000 | $30,001–45,000 | $45,001–60,000 | $60,001–75,000 | $75,001–90,000 | $90,001–105,000 | >$105,000 |
| Single / MFS | tiers | ≤$20,000 | $20,001–30,000 | $30,001–40,000 | $40,001–50,000 | $50,001–60,000 | $60,001–70,000 | >$70,000 |

_(NCDOR 2025 D-401 Instructions, Child Deduction Table, archived: "Married Filing Jointly/Qualifying Widow(er)/Surviving Spouse ... Up to $40,000 → $3,000 ... Over $140,000 → $0; Head of Household ... Up to $30,000 → $3,000 ... Over $105,000 → $0; Single/Married Filing Separately ... Up to $20,000 → $3,000 ... Over $70,000 → $0")_

NC does not have personal exemptions — the child deduction is the only per-dependent benefit.

### Local income tax

- **Local income tax permitted** — North Carolina does not permit local income taxes.

## The taxable base

## Section 3: How this skill works with the federal return

North Carolina taxable income starts with **federal adjusted gross income (AGI)** from federal Form 1040, Line 11.

1. **Start with federal AGI** → D-400, Line 6
2. **Add NC additions** (Schedule S, Part A) — items NC adds back that were excluded or deducted federally
3. **Subtract NC deductions** (Schedule S, Part B) — items NC excludes that were included federally
4. **Result = NC adjusted gross income**
5. **Subtract** the NC standard deduction (or NC itemized deductions) and child deduction
6. **Result = NC taxable income** → multiply by 4.25%
7. **Subtract credits** (D-400TC) → final tax due or refund

### Key addition modifications (Schedule S, Part A)

**Addition modifications table**

| Addition | Description |
| --- | --- |
| Interest from other states' bonds | Interest income from bonds of states other than NC |
| Bonus depreciation add-back | NC did not adopt IRC §168(k)/§168(n) bonus depreciation for TY 2025 — add 85% of the federal bonus depreciation on Schedule S Line 3; 20%/year deduction of the add-back over the first five taxable years beginning TY 2026 _(NCDOR 2025 D-401 Instructions, Schedule S Line 3, archived)_ |
| Section 179 excess | NC limits §179 to $25,000 expense / $200,000 investment limitation; add 85% of the difference between the federal and NC-allowed deduction on Schedule S Line 4 (same 20%/year reversal) _(NCDOR 2025 D-401 Instructions, Schedule S Line 4, archived)_ |

### Key subtraction modifications (Schedule S, Part B)

**Subtraction modifications table**

| Subtraction | Description |
| --- | --- |
| US government bond interest | Interest from US Treasury obligations |
| Retirement benefits (Bailey Settlement) | Certain state/local government retirees exempt per court settlement |
| Social Security | NC does not tax Social Security benefits |

## Section 4: Self-employed specific rules

### Self-employment income flow

- **SE income treatment** — Schedule C net profit flows into federal AGI, which flows into NC AGI. NC has no separate self-employment tax — the 4.25% rate applies to all taxable income including self-employment income.

### Estimated tax

- **Estimated tax payment threshold** — $1,000 or more expected liability after withholding and credits

**Estimated tax installment due dates**

| Installment | Due date |
| --- | --- |
| 1st quarter | April 15 |
| 2nd quarter | June 15 |
| 3rd quarter | September 15 |
| 4th quarter | January 15 (following year) |

Form NC-40 is used for estimated tax payments.

### Depreciation decoupling

- **Bonus depreciation decoupling** — NC did not adopt the bonus depreciation provisions of IRC §168(k) or §168(n) for property placed in service for TY 2025. Enter 85% of the federal bonus depreciation as an addition on Schedule S Line 3; if required to add back in TY 2025, you may deduct 20% of the add-back in each of the first five taxable years beginning with TY 2026. _(NCDOR 2025 D-401 Instructions, archived: "North Carolina did not adopt the bonus depreciation provisions in IRC sections 168(k) or 168(n) for property placed in service for tax year 2025. You must add 85% of the amount of bonus depreciation deducted on your federal return to your state return.")_ This is critical for self-employed taxpayers with significant equipment or vehicle purchases.

### Section 179

- **NC Section 179 limits** — $25,000 expense limitation and $200,000 investment limitation
- **Section 179 excess add-back** — NC did not conform to the increased federal expense deduction or investment limitations for TY 2025. Enter 85% of the difference between the §179 deduction using federal limitations and the deduction using NC limitations on Schedule S Line 4; 20%/year deduction of the add-back over the first five taxable years beginning TY 2026. _(NCDOR 2025 D-401 Instructions, archived: "NC dollar and investment limitations are $25,000 and $200,000, respectively. You must add 85% of the difference between the IRC section 179 expense deduction using federal limitations and the deduction using NC limitations.")_

## Deadlines and filing

## Penalties and interest

## Cross-border points

## Worked examples

## Ask the client first

## Section 5: Tier 1 rules — deterministic

**Tier 1 rules table**

| Rule ID | Rule | Source |
| --- | --- | --- |
| NC-T1-01 | NC taxable income = federal AGI ± NC modifications − standard/itemized deduction − child deduction | N.C.G.S. § 105-153.5 (standard deduction), § 105-153.6 (child deduction; see 2025 D-401 instructions, Line 10 Child Deduction Worksheet, archived) |
| NC-T1-02 | Tax = NC taxable income × 4.25% (TY 2025) | N.C.G.S. §105-153.7; Session Law 2023-134 |
| NC-T1-03 | Standard deduction: $12,750 (S), $25,500 (MFJ), $12,750 (MFS), $19,125 (HOH) | N.C.G.S. §105-153.5(a)(1) |
| NC-T1-04 | NC §179 limits = $25,000 expense / $200,000 investment; add 85% of federal-vs-NC difference | N.C.G.S. §105-153.6; NCDOR 2025 D-401 Instructions (archived) |
| NC-T1-05 | NC did not adopt IRC §168(k)/(n) bonus depreciation for TY 2025 — 85% add-back, 20%/yr reversal from TY 2026 | N.C.G.S. §105-130.5B; NCDOR 2025 D-401 Instructions (archived) |
| NC-T1-06 | Estimated tax required if tax due after withholding and credits ≥ $1,000 | N.C.G.S. §105-163.15; NCDOR NC-40 Instructions (archived: "You should make estimated income tax payments if the tax due on your individual tax return, reduced by the amount of tax withheld and tax credits, will be $1,000 or more.") |
| NC-T1-07 | NC does not tax Social Security benefits | N.C.G.S. §105-153.5(b)(8) |

## Section 6: Tier 2 rules — requires judgment

**Tier 2 rules table**

| Rule ID | Situation | Guidance |
| --- | --- | --- |
| NC-T2-01 | **Multi-state income:** Taxpayer has income from another state | NC taxes all income of residents; credit for taxes paid to other states available on D-400TC. Allocation requires review. |
| NC-T2-02 | **Business vs. hobby determination** | NC follows federal hobby loss rules. If IRS disallows Schedule C, NC deductions are also disallowed. |
| NC-T2-03 | **IRC conformity date changes** | NC references IRC as of a specific date. If federal law changed after NC's conformity date, add-backs or subtractions may be required. Verify conformity date for the tax year. |
| NC-T2-04 | **Home office deduction** | NC conforms to federal home office deduction rules. Flows through federal AGI. No separate NC adjustment needed. |
| NC-T2-05 | **Net operating losses** | NC conforms to federal NOL rules with modifications. Post-2017 NOLs limited to 80% of taxable income. Carryforward only (no carryback). |

## Section 7: Supplier pattern library

**Supplier pattern library table**

| Input needed | Where to find it |
| --- | --- |
| Federal AGI | Federal Form 1040, Line 11 |
| NC additions | Schedule S, Part A (computed from federal return) |
| NC deductions | Schedule S, Part B (computed from federal return) |
| Standard deduction | Based on filing status |
| Child deduction | Number of qualifying children × per-child amount from the Child Deduction Table, phased down by federal AGI (2025 D-401 instructions, Line 10 worksheet, archived) |
| Tax credits | D-400TC (credit for taxes paid to other states, child tax credit, etc.) |
| Estimated tax payments | NC-40 records |
| NC withholding | W-2 Box 17 / 1099 NC withholding amounts |

## Section 8: Form mapping

**Form D-400 line mapping table**

| Form D-400 Line | Description | Source |
| --- | --- | --- |
| Line 6 | Federal adjusted gross income | Federal 1040, Line 11 |
| Line 7 | Additions from Schedule S | Schedule S, Part A total |
| Line 9 | Deductions from Schedule S | Schedule S, Part B total |
| Line 11 | NC standard deduction or NC itemized deductions | § 105-153.5 amounts (§ 105-153.5 archived) |
| Line 13 | Child deduction | Child Deduction Worksheet (2025 D-401 instructions, Line 10; archived) |
| Line 14 | NC taxable income | Line 6 + Line 7 − Line 9 − Line 11 − Line 13 |
| Line 15 | NC income tax | Line 14 × 0.0425 (§ 105-153.7 rate confirmed) |
| Line 20 | Tax credits | D-400TC total |
| Line 23 | NC tax withheld | W-2s / 1099s |
| Line 25 | Estimated tax payments | NC-40 payments |

## Section 9: Refusal catalogue

**Refusal catalogue table**

| Refusal ID | Trigger | Response |
| --- | --- | --- |
| R-NC-01 | Part-year or nonresident | "NC part-year and nonresident returns require Schedule PN. This is outside the scope of this skill." |
| R-NC-02 | Corporate or S-corp return | "This skill covers individual income tax only (Form D-400). Corporate returns (CD-405) are not covered." |
| R-NC-03 | Estate or trust return | "NC fiduciary returns (Form D-407) are not covered by this skill." |
| R-NC-04 | Amended return | "NC amended returns (Form D-400X Amended) are not covered." |
| R-NC-05 | Pass-through entity tax | "NC PTET elections are not covered by this skill." |

## Sources

| Source | URL | Read on |
|---|---|---|
| N.C.G.S. § 105-153.7 (flat rate; phase-down schedule) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.7.html | 2026-10-29 |
| N.C.G.S. § 105-153.5 (standard deduction) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.5.html | 2026-10-29 |
| N.C.G.S. § 105-153.8 (who must file) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.8.html | 2026-10-29 |
| N.C.G.S. § 105-153.2 (purpose/sourcing) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.2.html | 2026-10-29 |
| N.C.G.S. § 105-153.6 (tax computed; credits) | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-153.6.html | 2026-10-29 |
| NCDOR 2025 D-401 individual income tax instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | 2026-10-29 |
| NCDOR home | https://www.ncdor.gov | 2026-10-29 |

Not yet confirmed: 2026 indexed standard deduction and child deduction amounts (D-400 instructions not archived); whether NC conforms to current federal §179/bonus-depreciation limits for 2026.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

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
