---
name: nm-income-tax
description: Use this skill whenever asked about New Mexico individual income tax for self-employed / sole proprietors. Trigger on phrases like "New Mexico income tax", "NM income tax", "Form PIT-1", "NM Taxation and Revenue", "NM self-employment tax".
version: "0.2"
jurisdiction: US-NM
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NM Income Tax

## Who this applies to

> **Scope.** This skill covers New Mexico Form PIT-1 (Personal Income Tax Return) for full-year NM residents who are sole proprietors or single-member LLC owners. Tax year 2025 (returns filed in 2026). New Mexico uses a six-bracket graduated rate structure restructured under HB 252 effective 2025.

**Metadata table**

| Field | Value |
| --- | --- |
| Tax type | Individual income tax (Personal Income Tax) |
| Jurisdiction | New Mexico (US-NM) |
| Tax year | 2025 (filed 2026) |
| Primary form | Form PIT-1 |
| Supporting schedules | Schedule PIT-B (Nonresident/Part-year), Schedule PIT-CR (Credits), Schedule PIT-ADJ (Adjustments) |
| Tax structure | Graduated (6 brackets) |
| Tax authority | New Mexico Taxation and Revenue Department |
| Statute | N.M. Stat. Ann. §7-2-7 (Income Tax Act) |

## Rates, bands and thresholds


### Quick reference -- rates and thresholds

### Tax brackets -- Single / Estates and trusts (TY 2025)

**Tax brackets -- Single / Estates and trusts (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $5,500 | 1.5% | $0 | (not yet confirmed)
| $5,500 | $16,500 | 3.2% | $82.50 | (not yet confirmed)
| $16,500 | $33,500 | 4.3% | $434.50 | (not yet confirmed)
| $33,500 | $66,500 | 4.7% | $1,165.50 | (not yet confirmed)
| $66,500 | $210,000 | 4.9% | $2,716.50 | (not yet confirmed)
| $210,000 | -- | 5.9% | $9,748 | (not yet confirmed)

### Tax brackets -- Married filing jointly / Head of household / Qualifying surviving spouse (TY 2025)

**Tax brackets -- MFJ / HOH / QSS (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $8,000 | 1.5% | $0 | (not yet confirmed)
| $8,000 | $25,000 | 3.2% | $120 | (not yet confirmed)
| $25,000 | $50,000 | 4.3% | $664 | (not yet confirmed)
| $50,000 | $100,000 | 4.7% | $1,739 | (not yet confirmed)
| $100,000 | $315,000 | 4.9% | $4,089 | (not yet confirmed)
| $315,000 | -- | 5.9% | $14,624 | (not yet confirmed)

### Tax brackets -- Married filing separately (TY 2025)

**Tax brackets -- Married filing separately (TY 2025)**

| Taxable income over | But not over | Rate | Tax on lower amount |
| --- | --- | --- | --- |
| $0 | $4,000 | 1.5% | $0 | (not yet confirmed)
| $4,000 | $12,500 | 3.2% | $60 | (not yet confirmed)
| $12,500 | $25,000 | 4.3% | $332 | (not yet confirmed)
| $25,000 | $50,000 | 4.7% | $869.50 | (not yet confirmed)
| $50,000 | $157,500 | 4.9% | $2,044.50 | (not yet confirmed)
| $157,500 | -- | 5.9% | $7,312 | (not yet confirmed)

### Standard deduction

New Mexico follows the **federal standard deduction** amounts (NM conforms to federal for this purpose).

**Standard deduction (TY 2025)**

| Filing status | Standard deduction (TY 2025) |
| --- | --- |
| Single | $15,000 (federal amount -- not yet confirmed) |
| Married filing jointly | $30,000 (federal amount -- not yet confirmed) |
| Head of household | $22,500 (federal amount -- not yet confirmed) |

### Low-and-middle-income exemption

- **Low-and-middle-income exemption** -- New Mexico offers a low-and-middle-income exemption of up to $2,500 per qualified exemption, based on adjusted gross income. All taxpayers (residents, part-year residents, first-year residents, nonresidents) may claim this exemption in full. Income limits verified verbatim vs the archived NM Taxation and Revenue Department PIT overview (archived 2026-10-28): "$36,667 (if single)", "$27,500 (if married filing separately)", "$55,000 (if married filing jointly, qualified widow(er), or head of household)". Also on that page: age-65+ exemption up to $8,000 each; $3,000 medical-expense exemption for 65+ with expenses over $28,000; refundable medical care credit $2,800 for unreimbursed expenses of $28,000+.

### Local income tax

- **Local income tax** -- New Mexico does not permit local income taxes.

### Standard deduction and exemptions

(covered under the quick-reference tables above)

## The taxable base

### How this skill works with the federal return

New Mexico taxable income starts with **federal adjusted gross income (FAGI)** from federal Form 1040, Line 11.

1. **Start with federal AGI** → PIT-1
2. **Add NM additions** -- items NM adds back
3. **Subtract NM subtractions** -- items NM excludes
4. **Subtract NM exemptions** (low-and-middle-income exemption, blind/aged exemptions)
5. **Subtract standard or itemized deductions** (NM follows federal amounts)
6. **Result = NM taxable income**
7. **Apply the graduated rate schedule** → NM tax
8. **Apply credits and rebates** (Schedule PIT-CR) → final tax due or refund

### Key addition modifications

**Key addition modifications**

| Addition | Description |
| --- | --- |
| Lump-sum distributions | Certain lump-sum distributions not included in federal AGI |
| NM income not in federal AGI | Income taxable by NM but excluded from federal return |

### Key subtraction modifications

**Key subtraction modifications**

| Subtraction | Description |
| --- | --- |
| US government bond interest | Interest from US Treasury obligations |
| Social Security | NM does not tax Social Security benefits |
| Military retirement pay | Exempt for certain qualifying individuals |
| Age 65+ income exemption | Up to $8,000 for 65+ with AGI under $51,000 (single) or $36,667 (MFJ per spouse) |

### Self-employed specific rules

### Self-employment income flow

- **Self-employment income flow** -- Schedule C net profit flows into federal AGI, which is the starting point for NM. NM follows the federal self-employment tax deduction (deductible half of SE tax) through federal AGI.

### Estimated tax

- **Estimated tax threshold** -- NM requires estimated tax payments if you expect to owe $1,000 or more after subtracting withholding and credits (not yet confirmed).

**Estimated tax installment due dates**

| Installment | Due date |
| --- | --- |
| 1st quarter | April 15 | (not yet confirmed)
| 2nd quarter | June 15 | (not yet confirmed)
| 3rd quarter | September 15 | (not yet confirmed)
| 4th quarter | January 15 (following year) | (not yet confirmed)

Form PIT-ES is used for estimated tax payments.

### Gross Receipts Tax (GRT) interaction

- **GRT interaction** -- Self-employed taxpayers in NM are also subject to the Gross Receipts Tax (GRT), which is NM's equivalent of a sales/use tax but is imposed on the seller's gross receipts. Unlike a traditional sales tax, the GRT is imposed on the business (not the buyer), though it is commonly passed through to customers. - GRT applies to most services as well as goods (unlike most state sales taxes). - Rates vary by location (combined state + local: approximately 5.0% to 9.4375% (not yet confirmed). - Self-employed service providers must register for and collect/remit GRT. - GRT paid is deductible as a business expense on the federal Schedule C.

### Working Families Tax Credit (NM EIC)

- **NM Working Families Tax Credit** -- NM offers a refundable earned income credit equal to 25% of the federal Earned Income Credit (EIC) -- the archived NM overview states 25% for tax year 2023; the TY 2025 percentage is not yet confirmed. This is particularly valuable for lower-income self-employed taxpayers.

## Deadlines and filing

Estimated-tax installment dates appear under Self-employed specific rules above; statutory filing/extension dates are listed under Not yet confirmed.

## Penalties and interest

NM imposes penalties and interest on late filing and late payment; the current rates are not yet confirmed against an archived source.

## Cross-border points

- **NM-T2-01** -- Multi-state income: Taxpayer has income from another state  _(NM taxes worldwide income of residents. Credit for taxes paid to other states available on Schedule PIT-CR.)_
- **NM-T2-02** -- GRT vs. income tax interaction  _(GRT is a separate tax on gross receipts, not a credit against income tax. GRT paid is deductible as a business expense on federal Schedule C, which flows through to NM.)_
- **NM-T2-03** -- Technology jobs tax credit  _(NM offers credits for qualifying technology businesses. Requires certification.)_
- **NM-T2-04** -- Angel investment credit  _(NM allows credits for qualified investments in NM small businesses. Requires approval from NM Economic Development Department.)_
- **NM-T2-05** -- Federal IRC conformity  _(NM's conformity with the IRC should be verified for recent federal changes. NM generally has rolling conformity but may decouple from specific provisions.)_
- **NM-T2-06** -- Community property  _(New Mexico IS a community property state. MFS returns require community property income allocation.)_

## Worked examples

No worked examples yet -- bracket figures are pending source confirmation.

## Ask the client first

- Residency status (full-year, part-year, nonresident) -- part-year/nonresident use Schedule PIT-B.
- Community-property allocation if married filing separately.
- Whether GRT registration applies to the client's services.

### Tier 1 rules -- deterministic

- **NM-T1-01** -- NM taxable income = federal AGI ± NM modifications − exemptions − deductions  _(N.M. Stat. Ann. §7-2-2)_
- **NM-T1-02** -- Tax computed using a 6-bracket graduated schedule (TY 2025 rates not yet confirmed)  _(N.M. Stat. Ann. §7-2-7; HB 252)_
- **NM-T1-03** -- Starting point is federal AGI (Form 1040, Line 11)  _(N.M. Stat. Ann. §7-2-2)_
- **NM-T1-04** -- Social Security benefits fully exempt  _(N.M. Stat. Ann. §7-2-2(S))_
- **NM-T1-05** -- Low-and-middle-income exemption: up to $2,500 per qualified exemption  _(N.M. Stat. Ann. §7-2-5.6)_
- **NM-T1-06** -- NM Working Families Tax Credit is a refundable % of federal EIC (25% stated for TY 2023 in the archived source; TY 2025 rate not yet confirmed)  _(N.M. Stat. Ann. §7-2-18.16)_
- **NM-T1-07** -- Estimated tax required if expected liability ≥ $1,000  _(N.M. Stat. Ann. §7-2-12.2)_
- **NM-T1-08** -- NM follows federal standard deduction amounts  _(N.M. Stat. Ann. §7-2-2)_

### Tier 2 rules -- requires judgment

- **NM-T2-01** -- Multi-state income: Taxpayer has income from another state  _(NM taxes worldwide income of residents. Credit for taxes paid to other states available on Schedule PIT-CR.)_
- **NM-T2-02** -- GRT vs. income tax interaction  _(GRT is a separate tax on gross receipts, not a credit against income tax. GRT paid is deductible as a business expense on federal Schedule C, which flows through to NM.)_
- **NM-T2-03** -- Technology jobs tax credit  _(NM offers credits for qualifying technology businesses. Requires certification.)_
- **NM-T2-04** -- Angel investment credit  _(NM allows credits for qualified investments in NM small businesses. Requires approval from NM Economic Development Department.)_
- **NM-T2-05** -- Federal IRC conformity  _(NM's conformity with the IRC should be verified for recent federal changes. NM generally has rolling conformity but may decouple from specific provisions.)_
- **NM-T2-06** -- Community property  _(New Mexico IS a community property state. MFS returns require community property income allocation.)_

### Supplier pattern library

**Supplier pattern library**

| Input needed | Where to find it |
| --- | --- |
| Federal AGI | Federal Form 1040, Line 11 |
| NM additions | PIT-1 / Schedule PIT-ADJ |
| NM subtractions | PIT-1 / Schedule PIT-ADJ |
| Standard/itemized deduction | Federal amounts (NM conforms) |
| Low-and-middle-income exemption | Based on AGI and number of exemptions |
| Tax credits and rebates | Schedule PIT-CR |
| Estimated tax payments | PIT-ES records |
| NM withholding | W-2 Box 17 / 1099 NM withholding amounts |
| Federal EIC amount | Federal Schedule EIC / Form 1040 (for NM WFTC calculation) |

### Form mapping

**Form PIT-1 line mapping**

| Form PIT-1 Line | Description | Source |
| --- | --- | --- |
| Line 7 | Federal adjusted gross income | Federal 1040, Line 11 |
| Line 8 | NM additions | Schedule PIT-ADJ |
| Line 10 | NM subtractions | Schedule PIT-ADJ |
| Line 13 | NM exemptions (low-and-middle-income, blind, aged) | Computed |
| Line 15 | Standard or itemized deduction | Federal amount |
| Line 17 | NM taxable income | Computed |
| Line 18 | NM income tax | From rate schedule |
| Line 21 | Credits and rebates | Schedule PIT-CR |
| Line 25 | NM withholding | W-2s / 1099s |
| Line 26 | Estimated tax payments | PIT-ES payments |
| Line 31 | Amount owed or refund | Computed |

### Refusal catalogue

- **R-NM-01** -- Part-year or nonresident  _("NM part-year and nonresident returns require Schedule PIT-B. This is outside the scope of this skill.")_
- **R-NM-02** -- Corporate return  _("This skill covers personal income tax only (Form PIT-1). Corporate income tax (CIT) is not covered.")_
- **R-NM-03** -- Fiduciary return  _("NM fiduciary returns (Form FID-1) are not covered by this skill.")_
- **R-NM-04** -- Amended return  _("NM amended returns (amended PIT-1) are not covered.")_
- **R-NM-05** -- GRT computation  _("NM Gross Receipts Tax is a separate tax. See nm-sales-tax.md for GRT details.")_
- **R-NM-06** -- Oil and gas taxation  _("NM oil, gas, and mineral taxation (severance taxes, conservation taxes) requires specialist review.")_

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.


> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| NM Taxation and Revenue -- Personal Income Tax overview | https://www.tax.newmexico.gov/individuals/personal-income-tax-information-overview/ | 2026-10-28 |
| NM Taxation and Revenue -- index | https://www.tax.newmexico.gov/ | 2026-10-28 |

Not yet confirmed: 2025 bracket boundaries and rates; filing/extension deadlines; standard deduction amounts; TY2025 WFTC percentage; estimated-tax $1,000 threshold; GRT combined rate range; age-65 AGI limits ($51,000/$36,667 pairing).

## Talk to a verified accountant


This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.


> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
