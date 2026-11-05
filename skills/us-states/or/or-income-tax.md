---
name: or-income-tax
description: Triggers when the taxpayer is an Oregon resident sole proprietor or single-member LLC needing to file Oregon Form OR-40. Covers Oregon's four-bracket graduated income tax (4.75%–9.9% for tax year 2026), standard and itemized deductions, personal exemption credit, federal tax subtraction, and Oregon's unique no-sales-tax environment. Must be loaded alongside us-tax-workflow-base and us-federal-return-assembly.
version: "0.2"
jurisdiction: US-OR
tax_year: 2026
last_updated: 2026-10-31
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# OR Income Tax

## Oregon Individual Income Tax Skill -- Self-Employed / Sole Proprietor

> **Scope.** Oregon Form OR-40 (Full-Year Resident) for tax year 2026 for full-year Oregon resident sole proprietors and disregarded single-member LLCs. Covers Oregon's four-bracket graduated income tax, standard and itemized deductions, Oregon-specific modifications to federal income, and credits.
> **Quality tier.** Q3 -- AI-drafted, not independently verified. All rates and thresholds have been researched from primary sources but must be confirmed by a qualified professional before use in return preparation.

## Section 1: Metadata

- **Tax year covered** -- 2026 (returns due April 15, 2027)
- **Primary form** -- Oregon Form OR-40 (Full-Year Resident)
- **Tax authority** -- [Oregon Department of Revenue](https://www.oregon.gov/dor)
- **Tax type** -- Graduated income tax
- **Currency date** -- May 2026

**Section 1 metadata table**

| Field | Value |
| --- | --- |
| Tax year covered | 2026 (returns due April 15, 2027) |
| Primary form | Oregon Form OR-40 (Full-Year Resident) |
| Tax authority | [Oregon Department of Revenue](https://www.oregon.gov/dor) |
| Tax type | Graduated income tax |
| Currency date | May 2026 |

**Primary sources**

| Source | URL |
| --- | --- |
| Oregon Revised Statutes Chapter 316 (personal income tax) | https://www.oregonlegislature.gov/bills_laws/ors/ors316.html |
| 2026 Publication OR-ESTIMATE (rate charts, standard deduction, exemption credit) | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf |
| Oregon Tax Rate Charts (2026) | https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx |

## Section 2: Quick reference -- rates and thresholds

### Statutory base table (ORS 316.048(1)(a), archived 2026-10-28)

The unindexed statutory table is: not over $2,000 -- 4.75%; over $2,000 but not over $5,000 -- $95 + 6.75% of excess; over $5,000 but not over $125,000 -- $298 + 8.75% of excess; over $125,000 -- "$10,798 plus 9.9% of the excess over $125,000". Under ORS 316.048(1)(b) DOR "shall adopt a table" applying cost-of-living adjustments each calendar year -- the indexed 2026 tables below come from that DOR table, as published in the 2026 rate charts in Publication OR-ESTIMATE (archived 2026-10-31).

### Tax brackets -- Single and Married Filing Separately (tax year 2026)

**Tax brackets -- Single and Married Filing Separately (tax year 2026)**

| Oregon taxable income | Tax |
| --- | --- |
| $0 – $4,550 | 4.75% of taxable income |
| $4,551 – $11,400 | $216 + 6.75% of excess over $4,550 |
| $11,401 – $125,000 | $678 + 8.75% of excess over $11,400 |
| Over $125,000 | $10,618 + 9.9% of excess over $125,000 |

### Tax brackets -- MFJ, HOH, and Qualifying Surviving Spouse (tax year 2026)

**Tax brackets -- MFJ, HOH, and Qualifying Surviving Spouse (tax year 2026)**

| Oregon taxable income | Tax |
| --- | --- |
| $0 – $9,100 | 4.75% of taxable income |
| $9,101 – $22,800 | $432 + 6.75% of excess over $9,100 |
| $22,801 – $250,000 | $1,357 + 8.75% of excess over $22,800 |
| Over $250,000 | $21,237 + 9.9% of excess over $250,000 |

### Standard deduction (tax year 2026)

**Standard deduction (tax year 2026)**

| Filing status | Standard deduction |
| --- | --- |
| Single | $2,900 |
| MFJ | $5,800 |
| HOH | $4,650 |
| MFS | $2,900 |

### Personal exemption credit (tax year 2026)

**Personal exemption credit (tax year 2026)**

| Item | Value |
| --- | --- |
| Credit per exemption | $260 |
| Income phase-out begins | $100,000 (single) / $200,000 (MFJ) | (US-OR-dr-dor-vendor-2026.pdf: exemption credit not allowed if federal AGI exceeds $200,000 MFJ/HOH/QSS or $100,000 single/MFS) |

### Other key figures

**Other key figures**

| Item | Value |
| --- | --- |
| Oregon EITC | 12% of federal EITC (refundable) for those with qualifying children under 3; 9% otherwise | (US-OR-dr-lro-basic-facts-2026.pdf: 'Current EIC is 9% & 12% (dependents < 3) of federal EIC') |
| Oregon kicker credit | Varies by year -- taxpayers receive a credit when state revenues exceed projections by >2%. Check for 2025. | (US-OR-dr-dor-kicker.txt: claimed on odd-year returns when actual revenue exceeds the forecast by more than 2 percent) |
| No sales tax | Oregon has no state or local sales tax |
| Estimated tax interest rate | 9% for 2025, 8% for 2026 |

## Section 3: How this skill works with the federal return

Oregon starts from **federal taxable income** (federal Form 1040, Line 15), NOT federal AGI. This is a critical difference from most states. Oregon then applies Oregon-specific additions and subtractions on Schedule OR-ASC to arrive at Oregon taxable income.

**Key flow:**

1. Federal taxable income → Oregon additions → Oregon subtractions → Oregon taxable income
2. Apply graduated tax rates → Oregon tax before credits
3. Apply credits (personal exemption credits, EITC, kicker, etc.) → Oregon income tax liability

### Critical: Oregon starts from federal taxable income

- **Oregon starts from federal taxable income; standard deduction stacks on top** -- Because Oregon starts from federal taxable income (which already includes the federal standard or itemized deduction), Oregon allows its own standard deduction on top. The Oregon standard deduction is relatively small ($2,900 single) because the federal deduction has already been taken. **However,** Oregon requires modifications for items where Oregon does not conform to the IRC: - Oregon additions (income Oregon taxes but federal does not, or deductions federal allows but Oregon does not) - Oregon subtractions (income federal taxes but Oregon does not, or deductions Oregon allows but federal does not) (US-OR-dr-lro-basic-facts-2026.pdf: Oregon's rolling connection to federal taxable income; 'Oregon standard deduction amounts differ from those used at the federal level'; US-OR-publication-or-estimate-2026.pdf: standard deduction single $2,900)

## Section 4: Self-employed specific rules

### No sales tax advantage

- **No sales tax advantage** -- Oregon's lack of a sales tax means sole proprietors selling goods to Oregon customers do not need to collect Oregon sales tax. However, they may still need to collect sales tax for sales to customers in other states with economic nexus.

### Oregon EITC

- **Oregon EITC** -- Oregon provides a refundable earned income tax credit: - 12% of federal EITC for taxpayers with a qualifying child under age 3 - 9% of federal EITC for all other qualifying taxpayers (US-OR-dr-lro-basic-facts-2026.pdf: 'Current EIC is 9% & 12% (dependents < 3) of federal EIC') - ITIN filers are eligible for the Oregon EITC (US-OR-dr-or40-inst-2026.pdf: Schedule OR-EIC-ITIN, 'Oregon's earned income credit for ITIN filers') - Self-employment income qualifies (see the Not yet confirmed: list in Sources)

### Oregon-specific local taxes (warning)

- **Local taxes warning** -- Self-employed individuals in certain parts of Oregon face additional local taxes that are NOT part of the state income tax but may be filed alongside it: - **TriMet self-employment tax** (Portland metro area): rate varies, approximately 0.8237% (verify 2025) - **Lane Transit District (LTD) tax** (Eugene/Springfield area): approximately 0.80% (verify 2025) - **Metro Supportive Housing Services (SHS) tax**: 1% on taxable income above $125,000 (single) / $200,000 (MFJ) for residents of Clackamas, Multnomah, and Washington counties - **Multnomah County Preschool for All (PFA) tax**: 1.5% on taxable income above $125,000 (single) / $200,000 (MFJ); additional 1.5% above $250,000 (single) / $400,000 (MFJ) - **Statewide Transit Tax (STT)**: 0.1% of wages (self-employed individuals are subject via Form OR-STT) These are separate filings and are NOT covered by this skill.

### Oregon additions (common for self-employed)

- **Oregon additions list** -- - Federal income taxes (if deducted on federal Schedule A -- not applicable if taxpayer took the federal standard deduction) - Interest/dividends from other states' bonds (Oregon taxes these; federal may not) - Bonus depreciation add-back (if Oregon does not conform to federal §168(k) -- verify conformity) - OBBBA-specific deductions not conformed to by Oregon (verify)

### Oregon subtractions (common for self-employed)

- **Oregon subtractions list** -- - Oregon income tax refund (if included in federal income) - Federal tax paid on a fiscal-year basis (if applicable) - Interest on U.S. government obligations (Oregon cannot tax federal bond interest) - Social Security benefits (Oregon fully exempts Social Security -- subtract if included in federal taxable income) - Oregon 529 plan contributions (subtraction up to $300 per student for single, $600 for MFJ)

## Section 5: Tier 1 rules -- deterministic

- **R-OR-1. Federal taxable income is the starting point.** -- Form OR-40 Line 7 = federal Form 1040, Line 15 (federal taxable income). This includes the federal standard or itemized deduction already.
- **R-OR-2. Oregon standard deduction is in addition to federal.** -- The Oregon standard deduction ($2,900 single / $5,800 MFJ for 2026, per 2026 Publication OR-ESTIMATE) is subtracted from Oregon adjusted income to arrive at Oregon taxable income.
- **R-OR-3. Social Security is fully exempt.** -- Subtract any Social Security benefits that were included in federal taxable income.
- **R-OR-4. Oregon income tax refund subtraction.** -- If the taxpayer received an Oregon income tax refund in the prior tax year and included it in federal income (Schedule 1 Line 1), subtract it on the Oregon return -- Oregon does not tax its own refund.
- **R-OR-5. U.S. government bond interest is exempt.** -- Subtract interest from U.S. Treasury obligations, I-bonds, and other federal securities included in federal income.
- **R-OR-6. Personal exemption credit is $260 per exemption (2026).** -- Apply after computing tax, subject to income phase-out. (US-OR-publication-or-estimate-2026.pdf: 'Personal exemption credit: $260'; phase-out per US-OR-dr-dor-vendor-2026.pdf)
- **R-OR-7. Oregon EITC is refundable.** -- Compute at 9% (or 12% with qualifying child under 3) of federal EITC. (US-OR-dr-lro-basic-facts-2026.pdf: 'Current EIC is 9% & 12% (dependents < 3) of federal EIC'; refundable per US-OR-dr-or40-inst-2026.pdf, 'Refundable credits')

## Section 6: Tier 2 rules -- requires judgment

- **J-OR-1. Oregon conformity with OBBBA.** -- Oregon's IRC conformity date must be verified. If Oregon does not conform to specific OBBBA provisions (§168(k) bonus depreciation, §179, §174A R&E), additions on Schedule OR-ASC may be required.
- **J-OR-2. Standard vs. itemized deduction choice.** -- Oregon allows a separate standard deduction even though federal taxable income already reflects the federal deduction. The small Oregon standard deduction ($2,900 single, US-OR-publication-or-estimate-2026.pdf) means most taxpayers should take it unless specific Oregon itemized deductions are advantageous.
- **J-OR-3. TriMet / LTD / Metro SHS / PFA applicability.** -- Self-employed individuals in the Portland metro or Eugene/Springfield areas must determine whether they are subject to local transit and housing services taxes. Geographic location of the taxpayer's residence determines applicability.
- **J-OR-4. Oregon kicker credit availability.** -- The kicker is a unique Oregon mechanism that returns excess state revenue to taxpayers. Whether a kicker is available for tax year 2026 depends on state revenue performance. Verify availability and amount.

## Section 7: Supplier pattern library

**Supplier pattern library**

| Pattern | Description |
| --- | --- |
| Portland-area freelancer | Subject to TriMet SE tax (0.8237%, US-OR-dr-trimet-taxinfo.txt) + Metro SHS tax (1% over threshold, US-OR-dr-portland-shs-personal.txt) + potentially Multnomah PFA tax (1.5%/3%, US-OR-dr-multco-pfa.txt) in addition to state income tax (9.9% top bracket, US-OR-publication-or-estimate-2026.pdf). Combined marginal rate can exceed 14%. Flag all local obligations. |
| Federal taxable income reconciliation | Oregon starts from federal taxable income, not AGI. Ensure correct line reference (1040 Line 15, not Line 11). |
| Social Security recipient | Full subtraction of Social Security from Oregon taxable income. |
| No sales tax seller | No Oregon sales tax collection needed, but may have nexus in other states. |
| High-income earner (>$125K single) | Top bracket at 9.9% plus potential Metro SHS (1%) and PFA (1.5%+) taxes if in Portland metro. |

## Section 8: Form mapping

**Form OR-40 line mapping**

| Form OR-40 line | Description | Source |
| --- | --- | --- |
| Line 7 | Federal taxable income | Federal Form 1040, Line 15 |
| Lines 8–13 | Oregon additions | Schedule OR-ASC (Section A) |
| Lines 14–18 | Oregon subtractions | Schedule OR-ASC (Section B) |
| Line 19 | Oregon taxable income | After additions, subtractions, and Oregon standard deduction |
| Line 20 | Oregon tax | Tax tables (if <$50,000) or rate chart (if ≥$50,000) |
| Line 22 | Oregon tax after standard/special credits | After exemption credits and other nonrefundable credits |
| Line 32 | Oregon EITC | 9% or 12% of federal EITC (US-OR-dr-lro-basic-facts-2026.pdf); line number see the Not yet confirmed: list in Sources |
| Line 34 | Kicker credit | If applicable for the tax year |
| Line 44 | Total tax after all credits | Final Oregon tax liability |

## Section 9: Refusal catalogue

- **REFUSE-OR-1** -- REFUSE to prepare an Oregon return for a part-year resident or nonresident without Form OR-40-P or OR-40-N. This skill covers full-year residents only.
- **REFUSE-OR-2** -- REFUSE to compute TriMet, LTD, Metro SHS, or Multnomah PFA taxes. These are separate local taxes with their own rules, forms, and filing requirements.
- **REFUSE-OR-3** -- REFUSE to compute Oregon Corporate Activity Tax (CAT). The CAT is a business-level tax ($250 + 0.57% on taxable commercial activity over $1M) that applies to larger businesses and is outside the scope of this individual income tax skill.
- **REFUSE-OR-4** -- REFUSE to determine the Oregon kicker credit amount without verifying the kicker status for the specific tax year. The kicker is not available every year.
- **REFUSE-OR-5** -- REFUSE to apply Oregon tax rates to a return without verifying Oregon's current IRC conformity date and any OBBBA decoupling provisions.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at the OpenAccountants network. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.

- Use it in your AI: 
- Meet the accountants: 

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.

## Who this applies to

Unconfirmed against archived sources.

## Rates, bands and thresholds

Unconfirmed against archived sources.

## The taxable base

Unconfirmed against archived sources.

## Deadlines and filing

Unconfirmed against archived sources.

## Penalties and interest

Unconfirmed against archived sources.

## Cross-border points

Unconfirmed against archived sources.

## Worked examples

Unconfirmed against archived sources.

## Ask the client first

Unconfirmed against archived sources.

## Sources

Not yet confirmed: self-employment-income eligibility for the Oregon EITC,
the Form OR-40 line-number mapping (line 32 EITC, line 34 kicker, line 44
total tax), the 529 subtraction amounts ($300/$600), and the 2026 estimated
tax interest rate (8%) are not tied to an archived capture; the archived
captures now also cover the Oregon EITC percentages (12%/9%), kicker credit
mechanics (surplus over forecast by more than 2 percent, odd-year returns),
personal exemption phase-out thresholds ($100,000/$200,000), TriMet/LTD/Metro
SHS/PFA local tax rates, the 2025 interest rate (9 percent Tier One), and the
2026 OR-ESTIMATE figures (bracket thresholds, standard deduction $2,900,
personal exemption credit $260).

| Source | URL | Read on |
| --- | --- | --- |
| Oregon Department of Revenue (home) | https://www.oregon.gov/dor | 2026-10-28 |
| Oregon Department of Revenue -- Personal Income Tax | https://www.oregon.gov/dor/programs/individuals/Pages/PIT.aspx | 2026-10-28 |
| Oregon Legislative Assembly -- ORS Chapter 316 | https://www.oregonlegislature.gov/bills_laws/ors/ors316.html | 2026-10-28 |
| Oregon DOR -- 2026 Publication OR-ESTIMATE (2026 rate charts: single/MFS 4.75% to $4,550, 6.75% to $11,400, 8.75% to $125,000, 9.9% above; MFJ/HOH/QSS $9,100/$22,800/$250,000; standard deduction $2,900/$4,650/$5,800; personal exemption credit $260) | https://www.oregon.gov/dor/forms/FormsPubs/publication-or-estimate_101-026_2026.pdf | 2026-10-31 |
| Oregon DOR -- 2026 proposed tax tables/vendor draft (standard deduction $2,910/$5,820/$4,685; exemption amount $263; exemption phase-out $100,000/$200,000) | https://secure.dor.state.or.us/Services/draftforms/api/document/7763/download | 2026-11-04 |
| Oregon LRO Basic Facts 2026 (EIC 9% & 12% of federal EIC; kicker; standard deduction discussion) | https://www.oregonlegislature.gov/lro/Documents/Basic%20Facts%202026.pdf | 2026-11-04 |
| Oregon DOR -- Kicker page (surplus over forecast by more than 2 percent; odd-year returns) | https://www.oregon.gov/dor/programs/individuals/Pages/Kicker.aspx | 2026-11-04 |
| Form OR-40 2026 instructions (refundable credits, EITC, Schedule OR-EIC-ITIN for ITIN filers) | https://secure.dor.state.or.us/Services/draftforms/api/document/7872/download | 2026-11-04 |
| TriMet tax information page (0.8237% transit tax on wages and self-employment earnings) | https://trimet.org/taxinfo/ | 2026-11-04 |
| City of Portland personal tax page (Metro SHS 1% over threshold; Multnomah PFA rates) | https://www.portland.gov/revenue/personal-tax | 2026-11-04 |
| Multnomah County PFA personal income tax page (1.5%/3% tiers; +0.8% from 2027) | https://multco.us/info/multnomah-county-preschool-all-personal-income-tax | 2026-11-04 |
| Oregon Revenue Bulletin 2025 interest rates (9 percent Tier One for 2025) | https://www.oregon.gov/dor/forms/FormsPubs/Annual%20Interest%20Rate%20Update%20for%202025.pdf | 2026-11-04 |

Unconfirmed against archived sources.

## Talk to a verified accountant

Unconfirmed against archived sources.
