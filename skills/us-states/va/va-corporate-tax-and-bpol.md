---
name: va-corporate-tax-and-bpol
description: "Source-cited tax guide for US-VA: va corporate tax and bpol. Unverified draft, pending local-accountant review."
jurisdiction: US-VA
tax_year: 2026
last_updated: 2026-11-02
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# VA Corporate Tax And Bpol

## Virginia Corporate Income Tax and BPOL Local Tax

Virginia imposes a 6% flat corporate income tax under Va. Code §58.1-400, unchanged since 1972. For tax year 2025 the general apportionment formula is property plus payroll plus double-weighted sales over a denominator of four (Va. Code §58.1-408(A)); manufacturers, retailers, and certain other specified classes use a single sales factor (Va. Code §58.1-422, §58.1-422.1). A Pass-Through Entity (PTE) election at 5.75% under Va. Code §58.1-390.3 has been available since tax year 2021. Localities (counties, cities, towns) impose BPOL gross-receipts taxes ranging from $0.05 to $0.58 per $100 by classification, with annual licenses generally due by March 1. Tax year 2025.

- **Virginia flat corporate income tax rate** - 6%  _(Va. Code §58.1-400)_
- **PTE election rate** - 5.75%  _(Va. Code §58.1-390.3)_

## Who this applies to

This skill covers Virginia state-level corporate income tax under Va. Code §58.1, Chapter 3 (the archived chapter table of contents runs through Article 22; the provisions used here sit in Article 9 (partnerships), Articles 10 and 14 (corporate accounting and returns), Article 16.1 (pass-through entity withholding), and Article 20 (corporate estimated taxes)), the elective Pass-Through Entity tax under Va. Code §58.1-390.3, and the local Business, Professional, Occupational License (BPOL) tax under Va. Code §58.1-3700 et seq. It is intended for use by Virginia-based or Virginia-doing-business C-corporations, S-corporations, partnerships, and single-member LLCs with Virginia nexus, as well as out-of-state contractors performing work in Virginia jurisdictions.

### 1.1 In scope

- **In-scope items** - C-corporation income tax (Form 500, Schedule 500A, Schedule 500AB); Apportionment (Schedule 500A; general double-weighted sales formula, single sales factor for manufacturers/retailers); Elective consolidated returns (Form 500CR election; binding); PTE election under Va. Code §58.1-390.3 (Form 502PTET, refundable credit Form PTE); S-corporation and partnership informational filing (Form 502); Quarterly estimated tax (Form 500ES); Seven-month automatic extension to file for C corporations (six months for other entities; no extension to pay); BPOL gross-receipts tax imposed by counties, independent cities, and towns; Out-of-state contractor BPOL exposure (90-day rule); NOL conformity (no separate Virginia NOL; the federal NOL carried into federal taxable income flows through; 80% limit for post-2017 losses)  _(Va. Code §58.1)_

### 1.2 Out of scope (refer out)

- **Out-of-scope items and refer-outs** - Virginia individual income tax (PIT) - see va-individual-income-tax; Virginia sales and use tax (5.3% statewide plus a 0.70% additional state sales tax in Northern Virginia (Planning District 15) and the Hampton Roads region under Va. Code §58.1-603.1, plus local option taxes) - see va-sales-use-tax; Real estate tax (locally assessed); Machinery and Tools (M&T) tax under Va. Code §58.1-3507 (locally assessed; separate from BPOL); Personal property tax on business equipment; Bank franchise tax (Va. Code §58.1-1200 et seq.); Insurance premiums license tax; Utility license tax (gross receipts of public service corporations); Litter tax (Va. Code §58.1-1707; nominal but separate annual filing); Recordation tax; Federal Schedule C, Schedule SE, federal corporate (Form 1120, 1120S) - see federal skills  _(Va. Code §58.1-3507; Va. Code §58.1-1200; Va. Code §58.1-1707)_

### 1.3 Caller assumptions

This skill assumes: The reviewer holds a Virginia CPA license or equivalent professional credential; Federal taxable income is already computed (we start from federal Line 28 / Line 21 / Line 22); The entity has determined its federal classification before invoking this skill; BPOL gross receipts are gross of cost of goods sold and gross of refunds in most localities (some classifications allow deductions - see §11); All references are to tax year 2025 unless otherwise noted

## Rates, bands and thresholds

### 2.1 Rate

- **Flat corporate income tax rate structure** - Virginia imposes a flat 6% corporate income tax under Va. Code §58.1-400. The rate has been unchanged since the 1972 reorganization of Title 58 (subsequently recodified as Title 58.1 in 1984). There are no brackets, no surtaxes, no AMT, and no minimum tax. There is no franchise tax based on capital, net worth, or shares outstanding. Virginia is one of the few states without any net-worth-style component on top of the income tax.  _(Va. Code §58.1-400)_

### 2.2 Tax base - Virginia Taxable Income (VTI)

- **Virginia Taxable Income (VTI) starting point** - The starting point is federal taxable income before the federal NOL deduction and before the federal dividends-received deduction (Form 1120, Line 28). This is then adjusted on Schedule 500ADJ.  _(Va. Code §58.1-402)_
- **Additions** - Interest on state and local obligations of states other than Virginia; Income taxes imposed by any state and deducted federally (Va. Code §58.1-402(B)(4)); The federal §199A QBI deduction is not added back for C-corps (C-corps don't claim §199A); Bonus depreciation in excess of Virginia conformity (Virginia conforms to federal bonus depreciation as of the fixed-date conformity statute - see §2.5); §168(k) bonus depreciation excess for years where Virginia decoupled (historic); Business interest expense disallowed under §163(j): Virginia's subtraction for the federally disallowed amount is reduced from 50% to 20% effective for Taxable Year 2025 returns (2025 Form 500 instructions, What's New)  _(Va. Code §58.1-402(B))_
- **Subtractions** - Interest on U.S. obligations; Federal income tax refunds previously included; Foreign-source income to the extent included federally and not subject to Virginia tax under apportionment; Subpart F income and GILTI (IRC §951A) - Virginia subtracts the full amount included in federal taxable income for taxable years beginning on and after January 1, 2018 (Va. Code §58.1-402(C)); Dividends from subsidiaries eligible for the federal DRD  _(Va. Code §58.1-402(C))_

### 2.3 Apportionment to Virginia

- **Apportionment basis** - After computing VTI on a 100% basis, apportionment to Virginia is via the general formula (property factor plus payroll factor plus twice the sales factor, divided by four), or the single sales factor if the corporation is a manufacturer, retailer, or other class covered by §§58.1-422 to 58.1-422.3 (see §3).  _(Va. Code §58.1-408)_

### 2.4 NOL

- **NOL conformity features** - There is no Virginia net operating loss available for carryback or carryover (2025 Form 500 instructions, Net Operating Loss Deductions). Because the Virginia starting point is federal taxable income, net operating loss deductions are taken into account on the Virginia return to the extent the losses are included in federal taxable income. For losses arising in tax years 2018+, the federal indefinite carryforward applies with the IRC §172(a)(2) 80%-of-taxable-income limitation, which Virginia enforces (Virginia does not conform to the 100% NOL usage allowed federally for tax years 2018, 2019, and 2020). Where federal and Virginia NOL carrybacks/carryforwards differ, separate accounting is required; carryback refunds use Form 500NOLD, not Form 500.  _(2025 Form 500 instructions; IRC §172(a)(2))_

### 2.5 Federal conformity - fixed date

- **Fixed-date conformity** - Virginia is a fixed-date conformity state. During the 2026 General Assembly session, the 2026 Amendments to the 2025 Appropriation Act replaced Virginia's suspended rolling conformity with a fixed conformity date of December 31, 2025 (2025 Form 500 instructions, What's New). This allows Virginia to conform to most provisions of the 2025 federal Budget Reconciliation Act (H.R. 1, P.L. 119-21) and reduces Virginia's subtraction for business interest disallowed on the federal return from 50% to 20%, effective for Taxable Year 2025 returns. Virginia deconforms from certain business provisions of that act: immediate expensing of qualified production property, immediate expensing of domestic research and experimental expenditures (including retroactive and catchup provisions), and increases to expensing limits for certain depreciable assets (Tax Bulletin 26-1). The legislation also automatically conforms to any federal amendment that extends the expiration date of a provision Virginia already conforms to.  _(Va. Code §58.1-301; 2025 Form 500 instructions)_

## The taxable base

### 3.1 Historical phase-in

- **Formula history** - The archived Va. Code §58.1-408(A) (read 2026-10-28) still states the general formula as property factor plus payroll factor plus twice the sales factor, denominator four. Manufacturers have used a single sales factor with market-based sourcing since 2013-2014 (§58.1-422) and retail companies since 2014 (§58.1-422.1); motor carriers use a single mileage factor (§58.1-417). There is no completed general phase-in to a single sales factor in the archived statute.  _(Va. Code §58.1-408(A); §58.1-422; §58.1-422.1; §58.1-417)_

### 3.2 Current formula - general and single sales factor

- **Apportionment percentage formula** - General formula: Apportionment % = (property factor + payroll factor + 2 x sales factor) / 4 (Va. Code §58.1-408(A)). Single sales factor (Virginia sales / everywhere sales) applies to manufacturers (§58.1-422), retail companies (§58.1-422.1), and the other classes specified in §§58.1-422.2 and 58.1-422.3; the 2025 Schedule 500A instructions label Line 9 as the multi-factor formula with double-weighted sales factor.  _(Va. Code §58.1-408; 2025 Schedule 500A instructions)_
- **Sales included** - Gross receipts from sales of tangible personal property delivered to a Virginia purchaser (ultimate destination); Gross receipts from services (sourced under market-based sourcing - see §3.3); Rents and royalties from Virginia property; Gross receipts from the sale, lease, or rental of real or tangible personal property located in Virginia; Other business income from Virginia sources  _(Va. Code §58.1-408)_
- **Sales excluded** - Returns and allowances (deducted); Sales of investment assets (not part of ordinary business income); Receipts from sales of 'intangible' property except where part of ordinary business operations; Receipts already excluded from federal taxable income  _(Va. Code §58.1-408)_

### 3.3 Market-based sourcing of services and intangibles

- **Market-based sourcing rules** - For sales of services and intangibles, Virginia uses market-based sourcing: Services are sourced to where the service is delivered or where the customer receives the benefit; Intangible licenses are sourced to where the intangible is used by the licensee; Software-as-a-service (SaaS): sourced to the customer's location. Cost-of-performance sourcing (the pre-2013 default for non-manufacturers) is no longer used. For purposes of 'delivered to' a customer: 1. Where the contract designates delivery (if explicit); 2. Where the customer's invoicing address is located; 3. Where the customer's commercial domicile is; 4. Throwback to seller's state if origin in Virginia and no nexus elsewhere (Virginia does NOT have a throwback rule - sales to a state where the seller has no nexus stay 'nowhere' sales and are still in the denominator but not numerator). Virginia is a no-throwback state for sales factor purposes. This is an important multistate planning point: Virginia headquartered service businesses selling into states where they have no nexus can have significant 'nowhere' sales that effectively reduce their Virginia apportionment percentage.

### 3.4 Special industry formulas

- **Special industry apportionment formulas** - Manufacturers (§58.1-422): single sales factor, market-based sourcing - applied since 2014; Retail companies (§58.1-422.1): single sales factor since 2014; Motor carriers (§58.1-417): single mileage factor (vehicle miles); Financial corporations (§58.1-418): special apportionment based on receipts, payroll, and property; Construction contractors (§58.1-419): completed-contract method permitted; sales factor uses receipts attributable to construction performed in Virginia; Railroad and pipeline companies: special formulas under §58.1-420 and §58.1-421  _(Va. Code §58.1-422; §58.1-422.1; §58.1-417; §58.1-418; §58.1-419; §58.1-420; §58.1-421)_

### 3.5 Alternative apportionment (§58.1-421)

- **Alternative apportionment petition** - A taxpayer may petition for alternative apportionment if the statutory formula does not fairly reflect Virginia business activity. The taxpayer bears the burden by clear and cogent evidence. The Tax Commissioner has discretion. Documented requests are filed with the return on Schedule 500ADJ with attached petition.  _(Va. Code §58.1-421)_

## 4. Combined Returns - Elective Consolidated

Virginia does not mandate unitary combined reporting. Instead, Va. Code §58.1-442 permits an elective consolidated or combined return for affiliated groups meeting certain ownership tests.

### 4.1 Three filing methods

- **Filing methods for affiliated group** - A Virginia affiliated group (Va. Code §58.1-302: one corporation owns at least 80 percent of the voting stock of the other or others, or at least 80 percent of the voting stock of each is owned by a third) may file: 1. Separate returns - each Virginia entity files its own Form 500; 2. Combined return - Virginia group files one Form 500 combining only those affiliates with Virginia nexus; intercompany transactions are eliminated; apportionment factors are combined; 3. Consolidated return - Virginia group includes ALL members of the federal consolidated group (regardless of whether they have Virginia nexus); apportionment is on a consolidated basis  _(Va. Code §58.1-442; §58.1-302)_

### 4.2 Election is binding

- **Binding election rule** - The election made on the first return where two or more affiliated members have Virginia nexus is binding for all future years. Changes require the Tax Commissioner's permission and must demonstrate a substantial business reason (Va. Code §58.1-442(B)). This is a critical first-year decision. The skill-user should flag the consolidation election in the workpapers for every first-Virginia-return engagement.  _(Va. Code §58.1-442(B))_

### 4.3 Practical considerations

- **Practical considerations for filing method choice** - Consolidated returns include 'nowhere' income: bringing in non-Virginia affiliates can dilute Virginia apportionment but also brings in losses; Combined returns: only Virginia-nexus members participate; intercompany sales are eliminated from sales factor; NOLs: a consolidated group's NOL is apportioned to Virginia using the consolidated apportionment factor in the loss year

### 4.4 No mandatory unitary

- **No mandatory unitary combined reporting** - Unlike California, Massachusetts, New York, Texas (margin tax), and approximately 28 other states, Virginia does NOT require unitary combined reporting. A 2021 General Assembly study (HB 1800 §3-5.23) examined a mandatory unitary regime, and an informational filing was required for tax year 2021 only. As of tax year 2025, separate, combined, or consolidated remains elective.  _(HB 1800 §3-5.23)_

## 5. Pass-Through Entity (PTE) Election

### 5.1 Background

- **Background of PTE election** - The Tax Cuts and Jobs Act of 2017 imposed a $10,000 cap on the federal individual SALT deduction. In response, Virginia enacted Va. Code §58.1-390.3 (HB 1121, 2022) creating an elective entity-level tax on pass-through entities. The federal IRS blessed this approach in Notice 2020-75 ('SALT cap workaround'). The election is available for tax years 2021 and later (the 2022 Virginia legislation made the election retroactive to 2021).  _(Va. Code §58.1-390.3; HB 1121 (2022); Notice 2020-75)_

### 5.2 Who can elect

- **Eligible electing entities** - S-corporations (including SMLLCs that elected S-corp status); Partnerships (including general partnerships and LLPs); LLCs taxed as partnerships; LLCs taxed as S-corporations. Not eligible: Single-member LLCs treated as disregarded entities for federal tax (because there is no separate entity-level federal return); C-corporations (different regime under §58.1-400); Sole proprietorships; Tiered partnerships where the upper-tier partner is itself a PTE (the election is made at the entity that pays out to natural persons or C-corp partners)  _(Va. Code §58.1-390.3(B))_

### 5.3 Rate and base

- **PTE election rate** - 5.75% flat, matching the top Virginia individual rate  _(Va. Code §58.1-390.3(C))_
- **PTE tax base** - The entity's net income attributable to Virginia from all sources, computed at the entity level as if the entity were a resident individual for those items, then apportioned using the entity's Virginia apportionment factor. For a single-state entity (all Virginia), the base is simply VA-source ordinary income + separately stated VA items. For multistate entities, the apportionment factor is computed at the entity level using the same single sales factor as in §3.  _(Va. Code §58.1-390.3(C))_

### 5.4 Mechanics - Form 502PTET and refundable credit

- **PTE mechanics** - The entity files Form 502PTET (separate from Form 502, which is informational); The entity pays 5.75% of its VTI at the entity level; Each owner receives a Form PTE showing their share of PTE tax paid; The owner claims a refundable credit on their Virginia individual return (Form 760 Line 25) for their proportionate share of PTE tax; For federal purposes, the entity deducts the PTE tax as an ordinary state-tax expense on Form 1120S Line 12 or Form 1065 Line 14 (a state and local tax under §164(a)(3)), thereby reducing federal taxable income flowing to the owners by the amount of PTE tax - this is the SALT-cap workaround benefit  _(§164(a)(3))_

### 5.5 Election mechanics

- **Election timing and payments** - Election is annual and is made on or before the due date for filing the applicable return, including any extensions that have been granted (Va. Code §58.1-390.3(A); 2025 Form 502 instructions). Form 502W is the pass-through entity withholding payment form - the withholding tax payment is due on the due date of the PTE's return regardless of any extension; it is not a quarterly PTE estimated-payment voucher.  _(Va. Code §58.1-390.3(A); 2025 Form 502 instructions)_

### 5.6 Composite returns (Form 765) vs. PTE election

Before §58.1-390.3, nonresident owners of Virginia PTEs typically participated in a composite return on Form 765 (Form 765-COMP), which avoided each nonresident filing a separate Form 763. The composite return remains available, but it does NOT generate a federal SALT deduction at the entity level.

**Composite Return (765) vs. PTE Election (502PTET) comparison**

| Feature | Composite Return (765) | PTE Election (502PTET) |
| --- | --- | --- |
| Federal SALT benefit | None (treated as withholding) | Full (entity-level §164 deduction) |
| Available to | Nonresident PTE owners | All owners (resident and nonresident) |
| Rate | Graduated individual rates (2% to 5.75% top bracket over $17,000) on each nonresident's VA share | 5.75% flat on entity's VA income |
| Owner filing | Owner can opt out and file own | Owners receive refundable credit |
| Tax year | Pre-2021 and continuing | 2021+ |

Most engagements with VA-resident owners and material taxable income will benefit from the PTE election. Run the breakeven: PTE election makes sense whenever the owner's federal marginal rate × VA-tax-paid exceeds the cost of the entity's compliance and any state-credit haircuts at the owner's home state level.

### 5.7 Nonresident owner credit

- **Nonresident owner credit treatment by resident state** - For owners who are residents of states OTHER than Virginia, the PTE election creates a credit at the resident state. Some resident states allow a full credit for the Virginia PTE tax against the resident state's tax (treating it as an income tax paid by the individual indirectly); others do not. Notable issues: Maryland - historically denied the credit before MD enacted its own PTE election in 2020; check current MD guidance; DC - allows credit; North Carolina, Tennessee - allows credit; California - allows credit (treats VA PTE tax as paid by the owner). Always verify the resident state's treatment before recommending an election for multistate ownership groups.

## Deadlines and filing

### 6.1 Form 500 - Corporate income tax

- **Due date** - 15th day of the 4th month after year-end. Calendar-year C-corps: April 15.
- **Extension** - 7-month automatic extension (calendar-year C corporations: to November 15); 6 months for nonprofit corporations and entities other than C corporations. Automatic if at least 90% of the tax is paid by the original due date; if 90% was not paid, an extension penalty of 2% per month (or fraction) applies, capped at 14% (12% for nonprofits/other entities).  _(Va. Code §58.1-453; 2025 Form 500 instructions)_
- **Extension payment** - Form 500CP (extension payment voucher) - payment of estimated tax balance.
- **Failure-to-pay penalty** - 6% per month (or fraction of a month), up to a maximum of 30% of the tax due (Va. Code §58.1-455; 2025 Form 500 instructions).
- **Failure-to-file penalty** - 6% per month (or fraction) up to 30% maximum if the return is not filed by the extended due date; in no case less than a $100 minimum, whether or not tax is due (Va. Code §58.1-455; 2025 Form 500 instructions).
- **Interest** - federal underpayment rate plus 2% (recalculated quarterly).

### 6.2 Form 500ES - Estimated tax

- **Estimated tax requirement threshold** - $1,000 USD (ND net tax liability expected)

**Form 500ES installment due dates**

| Installment | Calendar year due date |
| --- | --- |
| 1st | April 15 |
| 2nd | June 15 |
| 3rd | September 15 |
| 4th | December 15 |

- **Safe harbor** - 100% of prior year tax (if return was for a full 12 months and showed a liability), OR 90% of current year tax  _(Va. Code §58.1-504)_
- **Underpayment penalty** - federal underpayment rate plus 2%, computed on Form 500C.

### 6.3 Form 502 - PTE informational return

- **Filing requirement** - S-corporations, partnerships, and multi-member LLCs taxed as partnerships file Form 502. This is informational at the entity level (no tax due unless PTE elected or composite return filed) but is required. Due date: 15th day of the 4th month after year-end (April 15 calendar). Extension: automatic 6-month.
- **Late-filing penalty** - $200 per month (or fraction of a month) for failure to file, capped at six months ($1,200); if the return is still not filed after six months, the penalty is 6% of the total Virginia taxable income derived by the entity's owners for the taxable year. There is no per-K-1 penalty.  _(Va. Code §58.1-394.1)_

### 6.4 Form 502PTET - PTE election return

- **PTE election filing details** - If the PTE election is made: Filed separately from (or in addition to) Form 502; Same due dates and extension (election due on or before the return due date including extensions). Form 502W is the PTE withholding payment form, not a PTE estimated-payment voucher.  _(Va. Code §58.1-390.3(A); 2025 Form 502 instructions)_

### 6.5 Form 502V - Nonresident withholding

- **Nonresident withholding requirement** - If the PTE does NOT elect the PTE tax AND does NOT file a composite return, the entity must withhold 5% on each nonresident owner's share of Virginia source income; the withholding tax payment is due on the due date of the PTE's return regardless of any extension, remitted using Form 502W (2025 Form 502 instructions).
- **No de minimis threshold** - Va. Code §58.1-486.2 contains no $1,000-per-owner threshold; withholding applies to the whole nonresident share unless a subsection C exception applies (e.g., exempt owners or an undue-hardship waiver).  _(Va. Code §58.1-486.2)_

## Penalties and interest

- **Corporate late filing and late payment** - Form 500 late filing draws a 5% penalty on the balance due plus interest at 0.01% per month on unpaid tax; the extension payment on Form 500CP avoids the late-payment penalty when the balance is paid by the original due date.  _(2025 Form 500 instructions)_
- **Pass-through entity late Form 502** - $10 per member or 10% of the tax shown, whichever is greater.  _(Va. Code §58.1-394.1)_
- **BPOL late penalties vary by locality** - Richmond and Alexandria charge 10% of the tax due or a $10 minimum; Vienna charges 10% plus interest at 0.0083 per month.

## 7. BPOL Tax - Overview

### 7.1 Statutory basis

- **BPOL statutory basis** - The Business, Professional, Occupational License tax is authorized by Va. Code §58.1-3700 through §58.1-3735. It is a local tax imposed by counties, independent cities, and incorporated towns. Each locality enacts its own ordinance and sets rates within the state-imposed maximums. BPOL is NOT a state tax. It is collected by the local Commissioner of the Revenue (in counties) or Department of Finance (in cities), not by Virginia Tax (Department of Taxation).  _(Va. Code §58.1-3700 through §58.1-3735)_

### 7.2 Nature of the tax

- **Gross receipts tax nature** - BPOL is a gross-receipts tax, not an income tax. The base is gross receipts before deductions for cost of goods sold, payroll, rent, or other business expenses. Limited exclusions are statutory (see §11.4). The tax is paid annually upon the issuance or renewal of a business license. Operating without a license is a separate licensing violation (often a misdemeanor under local ordinance).

### 7.3 Geographic scope and nexus

- **Definite place of business nexus** - A business owes BPOL in any locality where it has a definite place of business. Va. Code §58.1-3700.1 defines 'definite place of business' as 'an office or location at which occurs a regular and continuous course of dealing for thirty consecutive days or more.' Out-of-state contractors performing work in a Virginia locality owe BPOL once they exceed the 90-day threshold under §58.1-3715 (see §13).  _(Va. Code §58.1-3700.1; §58.1-3715)_

### 7.4 Rate structure

- **Rate variance factors** - BPOL rates are set per $100 of gross receipts and vary by: 1. Locality (within state-imposed maximums by classification); 2. Business classification (contractor, retailer, professional, financial, repair/personal service, wholesale, etc.). The General Assembly caps the rate per classification under §58.1-3706. Localities can set rates below these statutory maxima - and many do. The maxima are statutory ceilings that prevent localities from imposing unlimited rates.  _(Va. Code §58.1-3706)_

**Maximum BPOL rate per $100 by classification**  _(Va. Code §58.1-3706)_

| Classification | Maximum rate per $100 |
| --- | --- |
| Contractors and persons constructing for their own account for sale | $0.16 |
| Retail sales | $0.20 |
| Financial services | $0.58 |
| Real estate services | $0.58 |
| Professional services (attorneys, CPAs, architects, engineers, consultants) | $0.58 |
| Repair, personal, and business services | $0.36 |
| Wholesale (basis is purchases, not gross receipts) | $0.05 (per $100 of purchases) |

### 7.5 Filing and renewal

- **Annual license renewal and new business rules** - The annual business license is typically renewed by March 1 each year. Some localities (notably Fairfax County) require renewal by March 1; all localities checked for this guide use March 1. The license year is generally the calendar year. A new business must apply for an initial license within 30 days of starting operations in the locality. The first-year base is estimated gross receipts; reconciliation occurs at the next year's renewal.

## 8. BPOL Rates - Major Virginia Localities

The following table summarizes BPOL rates for tax year 2025 across major Northern Virginia, Richmond metro, and Hampton Roads jurisdictions. All rates are per $100 of gross receipts unless otherwise noted. Always verify directly with the locality's Commissioner of the Revenue before filing.

### 8.1 Northern Virginia

| Locality | Contractor | Retail | Professional | Repair/personal/business | Wholesale (per $100 purchases) | Threshold / flat fee |
| --- | --- | --- | --- | --- | --- | --- |
| Fairfax County | $0.11 | $0.17 | $0.31 | $0.19 | $0.04 | $100,000; $30 (10k-50k), $50 (50k-100k) |
| City of Fairfax | $0.16 | $0.20 | $0.40 | $0.27 | $0.05 | $50,000; $30 (10k-50k) |
| Loudoun County | $0.13 | $0.17 | $0.33 | $0.16 | $0.05 | $200,000; $30 (10k-200k) |
| Prince William County | $0.13 | $0.17 | $0.33 | $0.21 | $0.05 | no tax below $500,000 |
| Arlington County | $0.16 | $0.20 | $0.36 | $0.35 | $0.08 | $100,000; $30 (10k-50k), $50 (50k-100k) |
| Alexandria | $0.16 | $0.20 | $0.58 | $0.35 | $0.05 | no tax liability below $10,000; $50 minimum |
| Falls Church | $0.16 | $0.19 | $0.52 | $0.36 | $0.08 | no fee at or below $10,000; $30 (10k-50k) |
| Manassas | $0.13 | $0.17 | $0.33 | $0.22 | $0.05 | rates apply above $150,000 |
| Manassas Park | see note | see note | see note | see note | see note | $50,000 |
| Vienna | $0.12 | $0.17 | $0.52 | $0.22 | $0.10 | $100,000; $30 (0-50k) |
| Herndon | see note | see note | see note | see note | see note | $30 (0-50k), $50 (50k-100k) |
| Leesburg | $0.10 | $0.10 | $0.20 | $0.15 | $0.075 | $20 below $100,000 |

_Sources: county and town rate pages and the City of Falls Church comparison table (see Sources). Leesburg figures are 2024 rates published March 2025; professional column for Leesburg is health professionals/business services at 0.20%._

### 8.2 Richmond metro

| Locality | Contractor | Retail | Professional | Repair/personal/business | Wholesale | Threshold / flat fee |
| --- | --- | --- | --- | --- | --- | --- |
| Richmond | $0.19 | $0.20 | $0.58 | $0.36 | $0.22 | $0 at or below $5,000; $30 for $5,001-$500,000 |
| Henrico County | $0.15 | $0.20 | $0.20 | see note | tiered $0.20 down to $0.0125 after $1,000,000 purchase exclusion | no tax at or below $500,000 (2025 application; current page $1,000,000) |
| Chesterfield County | $0.14 | $0.19 | $0.20 | $0.20 | $0.10 | $550,000 (receipts reduced by $550,000) |
| Hanover County | $0.10 | see note | see note | see note | see note | $100,000 |
| Petersburg | $0.16 | $0.20 | $0.58 | $0.32 | tiered $0.25/$0.15/$0.10 | $50 below $50,000 |

### 8.3 Hampton Roads

| Locality | Contractor | Retail | Professional | Repair/personal/business | Wholesale | Threshold / flat fee |
| --- | --- | --- | --- | --- | --- | --- |
| Virginia Beach | $0.16 | $0.20 | $0.58 | $0.36 | $0.12 | $25 (to 25k), $40 (to 100k), $50 (to 200k) |
| Norfolk | $0.16 | $0.20 | $0.58 | $0.36 | $50 flat + $0.15 | $100,000; $50 minimum |
| Chesapeake | see note | see note | see note | see note | see note | no tax below $100,000 (Va. Code §58.1-3706) |
| Newport News | $0.15 | $0.20 | $0.58 | $0.36 | $50 + $0.20 over $10,000 of purchases | $30 (to 50k), $50 (50k-100k) |
| Hampton | $0.16 | $0.20 | $0.58 | $0.36 | $0.15 (on purchases) | $100,000 |
| Suffolk | $0.16 | $0.20 | $0.58 | $0.36 | $0.09 | see note |
| Portsmouth | see note | see note | see note | see note | see note | see note |

### 8.4 Other localities

Rates for Williamsburg, York County, James City County, Charlottesville, Albemarle County, Roanoke, Lynchburg, Winchester, and Fredericksburg were not confirmed from archived sources; see the Not-yet-confirmed line in Sources.

Reviewer note: rates above were read from locality rate pages and rate sheets captured 2026-10-31 through 2026-11-01 (see Sources). The binding figure is always the current local ordinance. Verify with the locality's Commissioner of the Revenue before filing.

## 9. BPOL Classifications

Va. Code §58.1-3706 and the Virginia BPOL Guidelines (most recently revised effective January 1, 2024) provide the classification rules. Misclassification is the most common BPOL error - and the most common audit adjustment.

### 9.1 Contractor (rate cap $0.16 per $100)

- **Contractor BPOL rate cap** - $0.16 per $100  _(§58.1-3700.1)_
- **Contractor definition** - "Persons accepting orders or contracts for performing any services, including those that require the construction, repair, renovation, demolition, or removal of any building, structure, or other improvement to real property"  _(§58.1-3700.1)_

Includes:
- General contractors
- Subcontractors (electrical, plumbing, HVAC, drywall, roofing, etc.)
- Excavation and grading
- Landscape installation (but landscape maintenance is "repair/personal services")
- Persons selling building materials to be installed by them
- Cable installers
- Roofing contractors
- Solar panel installers
- Persons constructing for their own account for sale (spec builders)

### 9.2 Retail merchant (rate cap $0.20 per $100)

- **Retail merchant BPOL rate cap** - $0.20 per $100

Sale of goods to ultimate consumer, including:
- Brick-and-mortar retail
- E-commerce retailers with VA nexus (online sellers shipping to VA from a VA fulfillment center)
- Restaurants (gross receipts include both food sales and meals; alcohol included)
- Auto dealers (with adjustments for trade-ins)
- Convenience stores, grocers
- Coffee shops

### 9.3 Professional services (rate cap $0.58 per $100)

- **Financial services BPOL rate cap** - $0.58 per $100
- **Professional services definition** - Defined as services rendered by a person engaged in any of the "professions" listed in §58.1-3732 or in any field requiring "high educational and technical attainment"  _(§58.1-3732)_

- Attorneys at law
- CPAs and public accountants
- Architects (registered)
- Professional engineers (licensed)
- Physicians, dentists, veterinarians
- Optometrists, chiropractors, podiatrists
- Real estate appraisers (registered)
- Insurance agents (some localities treat as financial)
- Stockbrokers (some localities financial)
- Management consultants
- IT consultants (in most localities - some treat as repair/business services; this is heavily contested)
- Investment advisors
- Actuaries
- Surveyors

- **Software developers and IT consultants classification** - Classification varies. Fairfax County and Loudoun County generally treat IT consulting as "business and personal services" ($0.19-$0.31), while Richmond and the Hampton Roads cities tend to apply the professional rate ($0.58). When IT consulting is at the level of architecture, system design, or licensed/credentialed work, the professional rate is more likely. When work is implementation, support, or commodity coding, the business-services rate is more likely. This is fact-specific - request a written classification ruling from the locality if material.

### 9.4 Financial services (rate cap $0.58 per $100)

- **Financial services BPOL rate cap** - $0.58 per $100
- **Banks exemption** - Banks pay separate Bank Franchise Tax and are EXEMPT from BPOL  _(§58.1-3703(C)(7))_
- **Credit unions exemption** - Credit unions are exempt as well  _(§58.1-3703(C)(8))_

- Banks (note: banks pay separate Bank Franchise Tax and are EXEMPT from BPOL under §58.1-3703(C)(7))
- Credit unions (exempt as well - §58.1-3703(C)(8))
- Securities dealers
- Mortgage brokers
- Money transmitters
- Pawnbrokers

The "financial services" BPOL classification primarily catches mortgage brokers, securities firms, and similar entities that don't qualify for the bank franchise tax exemption.

### 9.5 Real estate services (rate cap $0.58 per $100)

- **Financial services BPOL rate cap** - $0.58 per $100

- Real estate brokers and agents
- Property managers
- Real estate developers (when selling property)
- Title companies

### 9.6 Repair, personal, business services (rate cap $0.36 per $100)

- **Repair, personal, business services BPOL rate cap** - $0.36 per $100

The catch-all classification for service businesses that don't fit professional, financial, or real estate:

- Auto repair, body shops
- Appliance repair
- Salons, barbers, spas
- Laundry, dry cleaning
- Photographers
- Caterers (not restaurants)
- Janitorial, cleaning, pest control
- Lawn care, landscape maintenance
- Staffing agencies
- Marketing and advertising agencies
- Most IT support and helpdesk businesses
- Pet groomers
- Tutoring (when not at a fixed school)
- Wedding planners, event planners

### 9.7 Wholesale (rate cap $0.05 per $100 of purchases)

- **Wholesale BPOL rate cap** - $0.05 per $100 of purchases
- **Wholesale tax base** - The wholesale tax is based on purchases (i.e., cost of goods sold), not gross receipts. This significantly limits the wholesale BPOL.

Sale of goods for resale, including:
- Manufacturers selling to retailers
- Distributors
- Wholesale food distributors

### 9.8 Multi-classification businesses

- **Multi-classification requirement** - Where a single entity operates in multiple classifications (e.g., a retailer that also performs installation contracts, or a CPA firm that has consulting and audit lines), BPOL must be paid at each applicable rate on the corresponding portion of gross receipts. Books and records must segregate receipts by classification. If receipts are not segregated, the locality may apply the highest applicable rate to the entire gross.

## 10. BPOL Filing and Thresholds

### 10.1 Filing dates

**BPOL renewal due dates by locality**

| Locality | Renewal due date |
| --- | --- |
| Fairfax County | March 1 |
| Loudoun County | March 1 |
| Prince William County | March 1 |
| Arlington County | March 1 |
| Alexandria | March 1 |
| Falls Church | March 1 |
| Richmond | March 1 |
| Henrico | March 1 |
| Chesterfield | March 1 |
| Virginia Beach | March 1 |
| Norfolk | March 1 |
| Newport News | March 1 |
| Chesapeake | March 1 |
| Hampton | March 1 |
| Charlottesville | March 1 |
| Most other localities | March 1 |

- **Late penalty** - Localities set their own BPOL late penalties: Richmond and Alexandria charge 10% of the tax due or a $10 minimum; Vienna charges 10% plus interest at 0.0083 per month.

### 10.2 Gross-receipts threshold by locality

- **Threshold exemption authority** - Va. Code §58.1-3706 bars licensure and taxation where gross receipts are less than $100,000 in localities with population over 50,000, and less than $50,000 in localities with population of 25,000 to 50,000.  _(§58.1-3706)_
- **Verified locality thresholds** - Fairfax County $100,000 (flat fee $30 for $10,000-$50,000, $50 for $50,000-$100,000); Loudoun County $200,000 (flat fee $30 up to $200,000); Prince William County no tax below $500,000; Henrico County no tax at or below $500,000 per the 2025 application (current page says $1,000,000); Chesterfield County $550,000 (gross receipts reduced by $550,000); Hanover County $100,000; City of Fairfax $50,000; Falls Church no fee at or below $10,000 and a $30 fee for $10,001-$50,000; Manassas rates apply above $150,000; Manassas Park $50,000; Virginia Beach flat fees $25 (up to $25,000), $40 (to $100,000), $50 (to $200,000); Norfolk minimum $50 below $100,000; Newport News $30 (to $50,000) and $50 (to $100,000); Petersburg $50 below $50,000; Leesburg $20 below $100,000; Herndon $30 (to $50,000) and $50 (to $100,000); Richmond $0 at or below $5,000 and $30 for $5,001-$500,000; Alexandria no tax liability below $10,000 and a $50 minimum for $100,000-$1,999,000.
- **Application of threshold** - Under most ordinances, if gross receipts exceed the threshold, BPOL is calculated on the FULL gross receipts (the threshold is a true exemption ceiling, not an exclusion). This is sometimes called a "cliff" but in practice most localities apply the rate only to the portion of receipts that exceeds the threshold (verify in the locality ordinance - language varies).

### Worked example: sample BPOL computation

A professional consulting LLC in Fairfax County with $500,000 of gross receipts:

```
Gross receipts                       $500,000
Threshold exemption (Fairfax)      ($   -   )  (none for professional above $100k)
Taxable gross receipts               $500,000
Rate (professional)                  $0.31 per $100
Tax = 500,000 / 100 × 0.31         = $1,550
```

Same LLC in Loudoun County:

```
Gross receipts                       $500,000
Rate (professional, Loudoun)         $0.33 per $100
Tax = 500,000 / 100 × 0.33         = $1,650
```

Same LLC in Arlington:

```
Gross receipts                       $500,000
Rate (professional, Arlington)       $0.36 per $100
Tax = 500,000 / 100 × 0.36         = $1,800
```

Same LLC in Richmond (city):

```
Gross receipts                       $500,000
Rate (professional, Richmond)        $0.58 per $100
Tax = 500,000 / 100 × 0.58         = $2,900
```

The locality choice can nearly double BPOL for the same receipts. For mobile professional businesses, locality selection is a meaningful planning consideration (subject to where the work is actually performed and the "definite place of business" rules).

### 10.4 Deductions and exclusions from gross receipts

- **Excludable items from BPOL base** - Va. Code §58.1-3732 permits the following exclusions from the BPOL base: - Receipts from interstate commerce sourced under U.S. Constitution Commerce Clause (apportionment of gross receipts among states for businesses with multistate activity) - Federal government contract receipts where federal law preempts state taxation (rare - most federal contracting is taxable) - Bad debts (when written off in accordance with federal income tax rules) - Reimbursement of out-of-pocket expenses passed through at cost to clients (where separately stated and supported by records) - Bona fide sales tax collected - Refunds and returns  _(§58.1-3732)_
- **Not deductible items** - Not deductible (gross receipts include): - Salaries paid to employees - Cost of goods sold (for retail/contractor - except wholesale rule) - Rent and operating expenses - Subcontractor payments (some localities allow deduction - see §10.5)

### 10.5 Subcontractor deduction (contractors only)

- **Subcontractor deduction rule** - Va. Code §58.1-3715 allows general contractors to deduct payments to subcontractors from their gross receipts IF the subcontractor is itself licensed and pays BPOL on those same receipts. This avoids pyramiding of the contractor tax on the same dollar of receipts as it flows up the contracting chain.  _(§58.1-3715)_
- **General contractor requirements** - The general contractor must: 1. Obtain the subcontractor's license number 2. Document payments to subcontractors 3. Report deducted subcontractor payments on a Schedule SC (form varies by locality) The locality may verify by cross-checking the subcontractor's BPOL filing.

## Cross-border points

### 11.1 The 90-day rule

- **30-day rule for out-of-state contractors** - Va. Code §58.1-3715 imposes BPOL on out-of-state contractors performing work in a Virginia locality. A contractor with no Virginia office is subject to BPOL in any Virginia locality where it performs construction work for 30 days or more in the license year.  _(§58.1-3715)_
- **Clarification on 30-day vs 90-day threshold** - (The 30-day threshold for "definite place of business" applies; the 90-day reference sometimes seen in older guidance referred to a different statute, and the controlling rule is the §58.1-3700.1 definite-place-of-business test.)  _(§58.1-3700.1)_

### 11.2 Each jurisdiction is separate

- **Separate jurisdiction BPOL liability** - Critical practice point: a Virginia contractor or out-of-state contractor working in multiple Virginia localities owes BPOL in each locality separately, based on the receipts earned from work performed in that locality. There is no "central" Virginia license. A general contractor with a Fairfax County office that performs work in Loudoun County, Arlington County, and the City of Falls Church owes BPOL in all four jurisdictions.
- **Allocation for mobile work** - Allocation: each locality is entitled to BPOL on the gross receipts attributable to construction performed within its boundaries. For mobile work (HVAC servicing multiple sites), the contractor must allocate based on physical work location.

### 11.3 Subcontractor pass-through

- **Subcontractor licensing requirement** - When the general contractor takes the §58.1-3715 subcontractor deduction (see §10.5), the subcontractor must be licensed in the locality of the work. An unlicensed subcontractor disqualifies the general from the deduction.  _(§58.1-3715)_

### Worked example: Maryland HVAC contractor scenario

A Maryland-based HVAC contractor performs $300,000 of work in Fairfax County over 60 days and $100,000 of work in Arlington over 40 days. License year: calendar 2025.

```
Fairfax County:
  Gross receipts attributable to Fairfax       $300,000
  Rate (contractor)                            $0.11 per $100
  BPOL                                         $330

Arlington County:
  Gross receipts attributable to Arlington     $100,000
  Rate (contractor)                            $0.16 per $100
  BPOL                                         $160

Total Virginia BPOL                           $490
```

The contractor must apply for a license in each county. Maryland's tax (if any) on the same receipts is a separate matter under Maryland law.

## Worked examples

### Worked example 1: Small Fairfax consulting LLC - single-member LLC plus owner PIT

**Facts:**
- Sarah is a Virginia resident
- She operates "Sarah Consulting LLC" - a single-member LLC, disregarded for federal income tax
- The LLC has its only office in Fairfax County, VA
- 2025 gross receipts: $350,000
- 2025 federal Schedule C net profit: $225,000 (after $75,000 wages to a contractor, $30,000 rent, $20,000 other expenses)
- Sarah has no other Virginia income
- Sarah is single, no dependents, takes the Virginia standard deduction ($8,500 single, 2025)

- **Step 1: BPOL (Fairfax County, professional consulting)** - Gross receipts                       $350,000 Classification (consulting)          Professional (Fairfax: $0.31/$100) Above $100,000 threshold            Yes (full rate) BPOL = 350,000 / 100 × 0.31       = $1,085 Due date: March 1, 2025 (for 2024 receipts) or March 1, 2026 (for 2025)

- Federal Schedule C net profit: $225,000
- Federal SE tax: 92.35% × $225,000 × 15.3% (capped) ≈ $25,500 (after SS cap effect)
- Deductible half: $12,750
- Federal AGI: $225,000 - $12,750 = $212,250
- (Federal income tax not computed here)

- **Step 3: Virginia individual income tax** - Single-member LLC is disregarded - Sarah reports the Schedule C income directly on her Virginia Form 760. Federal AGI                                   $212,250 Virginia additions (e.g., other-state munis)      $- Virginia subtractions                             $- (BPOL tax - not deductible against VA PIT; deductible on federal Sch C as a tax expense, so already in federal AGI as expense) Virginia AGI                                  $212,250 Less: Virginia standard deduction            ($  8,500) Virginia taxable income                       $203,750 Virginia tax (2025 brackets): First $3,000           × 2.0%       = $    60 Next $2,000  (to $5k)  × 3.0%       = $    60 Next $12,000 (to $17k) × 5.0%       = $   600 Above $17,000          × 5.75%      = $10,738  (on $186,750) -------- Total Virginia tax                  = $11,458
- **Step 4: PTE election available?** - No - single-member LLCs disregarded for federal tax cannot elect PTE under §58.1-390.3. Sarah pays Virginia PIT at the individual level.  _(§58.1-390.3)_

**Step 5: Total Virginia + BPOL burden (Fairfax)**

| Tax | Amount |
| --- | --- |
| BPOL (Fairfax County) | $1,085 |
| Virginia individual income tax | $11,458 |
| **Total state and local** | **$12,543** |

Effective state+local rate on Schedule C net profit: 12,543 / 225,000 = **5.57%**

**If Sarah relocated to Loudoun County comparison**

| Tax | Amount |
| --- | --- |
| BPOL (Loudoun) - $350k × $0.33/$100 | $1,155 |
| Virginia PIT (unchanged - same VA resident) | $11,458 |
| **Total** | **$12,608** |

Loudoun costs $70 more than Fairfax for this LLC (BPOL difference only).

### Worked example 2: Multistate manufacturer using single sales factor

**Facts:**
- "Acme Widgets, Inc." is a Virginia C-corp headquartered in Richmond
- Manufactures widgets at a Richmond plant
- 2025 gross sales: $50,000,000 (everywhere)
- Federal taxable income (before NOL): $5,000,000
- Property in Virginia: $20,000,000 (Richmond plant)
- Property everywhere: $30,000,000 (Richmond + Ohio warehouse)
- Payroll in Virginia: $8,000,000
- Payroll everywhere: $12,000,000
- Sales destinations:
  - Virginia customers: $10,000,000 (20%)
  - Other states with nexus: $25,000,000 (50%)
  - Other states with NO nexus: $15,000,000 (30% - "nowhere sales")

- **Step 1: Apportionment - single sales factor** - Virginia sales numerator             $10,000,000 Everywhere sales denominator         $50,000,000  (includes the $15M nowhere) Single sales factor                  20.00%  _(§58.1-422)_
- **Step 2: Compare to historic 3-factor (comparison)** - Property factor:   20M / 30M    = 66.67% Payroll factor:    8M / 12M     = 66.67% Sales factor:      10M / 50M    = 20.00% Equal-weighted average           = 51.11% Double-weighted sales            = 43.33%

Single sales factor (20.00%) drives a dramatically lower Virginia apportionment than a property/payroll weighted formula would for an in-state manufacturer. This is the policy intent - incentivize Virginia-located property and payroll.

- **Step 3: Virginia Taxable Income** - Federal taxable income (before fed NOL)            $5,000,000 Virginia additions (e.g., state taxes deducted)     $  300,000 Virginia subtractions (US bond interest, etc.)     ($  100,000) Apportionable Virginia base                        $5,200,000 Apportionment %                                    × 20.00% Apportioned Virginia income                        $1,040,000 Virginia tax = 1,040,000 × 6%                    = $62,400
- **Step 4: BPOL applies despite corporate income tax** - Even though Acme is paying corporate income tax, it still owes Richmond city BPOL on its gross receipts. Manufacturing classification: manufacturers selling their own goods are generally classified as "manufacturer/wholesaler" under §58.1-3703(C)(4). Under that classification, wholesale BPOL applies to manufacturer sales at wholesale, on a base of purchases - but a manufacturer selling its own product has no "purchases" of finished goods. Many localities (Richmond included) impose BPOL on manufacturers at a separate, lower rate, often $0.20 per $100 of gross receipts attributable to wholesale sales from the Virginia plant, capped under §58.1-3703. Richmond's 2024 ordinance applies $0.20/$100 to manufacturer-wholesale receipts arising in Richmond. ``` Receipts attributable to Richmond manufacturing operation = $50,000,000 (all manufacturing is in Richmond) BPOL = 50,000,000 / 100 × 0.20             = $100,000 ```  _(§58.1-3703(C)(4))_
- **Reviewer check on manufacturer exemption** - **Reviewer check:** the §58.1-3703(C)(4) exemption is heavily fact-specific. Manufacturers selling at WHOLESALE from a Virginia plant are EXEMPT from BPOL on those wholesale receipts under §58.1-3703(C)(4). Acme should claim the manufacturer exemption if and only if it is selling at wholesale (i.e., to retailers for resale). If Acme sells directly to ultimate consumers, the receipts are retail and BPOL applies at the retail rate. Assuming Acme's $50M is all wholesale (to distributors and retailers), Acme's BPOL = **$0** under the §58.1-3703(C)(4) manufacturer exemption.  _(§58.1-3703(C)(4))_

**Step 5: Total state and local burden**

| Tax | Amount |
| --- | --- |
| Virginia corporate income tax | $62,400 |
| Richmond BPOL (manufacturer exemption) | $0 |
| **Total** | **$62,400** |

Effective state-and-local rate on $5M federal income: 62,400 / 5,000,000 = **1.25%**.

The single sales factor combined with the manufacturer BPOL exemption makes Virginia very competitive for manufacturing.

### Worked example 3: S-corp electing PTE tax

**Facts:**
- "Tidewater Engineering, S-Corp" - a Virginia S-corp with two equal shareholders
- Both shareholders are Virginia residents
- 2025 ordinary income (Form 1120S Line 21): $400,000 (all VA source, single-state operation)
- S-corp paid each shareholder a $100,000 reasonable salary, reported on W-2 (already deducted in arriving at $400,000)
- The PTE election is made for 2025 on Form 502PTET

- **Step 1: PTE tax at entity level** - Virginia source income at S-corp level           $400,000 PTE rate                                         × 5.75% PTE tax (Form 502PTET)                           $ 23,000

The PTE tax is paid with the election return; Form 502W is the pass-through entity withholding payment form (due by the return due date), not a quarterly PTE estimated-payment voucher.

The S-corp deducts $23,000 of PTE tax on Form 1120S as a state tax expense (Line 12, "Taxes and licenses"). This reduces federal ordinary income flowing to the shareholders.

Adjusted federal Schedule K-1 ordinary income (per shareholder): ($400,000 - $23,000) / 2 = $188,500 each (down from $200,000 each absent the election).

Federal SALT cap benefit per shareholder at a 37% top federal bracket:
- Federal tax saved on the entity-level deduction: $23,000 × 37% / 2 shareholders = $4,255 per shareholder, $8,510 total.

This is the SALT-cap workaround benefit. Without the PTE election, each shareholder would have paid the $11,500 of VA PIT individually (which would have been subject to the $10,000 federal SALT cap and largely lost as a federal deduction).

- **Step 3: Virginia individual returns - refundable PTE credit** - Each shareholder receives Form PTE showing $11,500 of PTE tax paid on their behalf. For each shareholder's Virginia Form 760: Virginia AGI from Schedule K-1 ordinary income     $200,000 (Federal-deducted PTE tax is ADDED BACK on Schedule ADJ for VA-PIT purposes to avoid double-benefit - Va. Code §58.1-322.02 add-back) Add: PTE tax deducted federally                  + $ 11,500 (added back so VA PIT base is the pre-PTE income) Virginia taxable income (after standard deduction) $200,000 + 11,500 - 8,500 = $203,000 Plus W-2 wages                                    + $100,000 Total VA taxable income                            $303,000 Virginia tax on $303,000: $3,000 × 2.0%   = $60 $2,000 × 3.0%   = $60 $12,000 × 5.0%  = $600 $286,000 × 5.75% = $16,445 Total VA tax                                       $17,165 Less: refundable PTE credit (from Form PTE)      ($11,500) Net VA tax due (per shareholder)                   $ 5,665  _(§58.1-322.02)_

Without the PTE election, the S-corp would have $400,000 of federal ordinary income flowing through. Each shareholder receives $200,000 + $100,000 W-2 = $300,000 of VA taxable income.

VA tax per shareholder (no election): $16,504 (vs $17,165 with election - slightly higher because the election grossed up VA base by the PTE deduction).

But: without the election, each shareholder must pay the $11,500 of VA tax themselves. Total federal SALT impact: their VA tax becomes a state income tax deduction, subject to the $10,000 cap, mostly lost.

With the election, the S-corp gets the $23,000 federal deduction unconditionally. Federal tax saved: ~$8,510. Net benefit per shareholder: ~$4,000.

**Decision**: elect PTE for 2025. Net federal-tax savings ~$8,500 across both shareholders, at a Virginia-tax cost essentially neutral (slight grossup wash). Time spent on Form 502PTET preparation is incremental on top of Form 502 already required.

- **Step 5: BPOL** - Engineering services are "professional" for BPOL purposes. Assume the S-corp's office is in Norfolk: Gross receipts (assume $1,200,000)                $1,200,000 Norfolk professional rate                         $0.58/$100 BPOL                                              = $6,960 This BPOL is a deductible business expense for federal purposes (reduces the $400,000 ordinary income - assume already reflected above).

## Ask the client first

- Which localities does the business have a definite place of business in, and where is work physically performed? BPOL is owed locality by locality.
- How does each locality classify the business (professional vs business services vs contractor)? Classification drives the rate and is contested for IT and consulting work.
- Did the entity make, or does it want to make, the annual PTE election, and have all owners consented?
- What were prior-year gross receipts by locality? Thresholds and flat-fee bands depend on them.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| US-VA-dr-section58.1-302.html | https://law.lis.virginia.gov/vacode/title58.1/chapter1/section58.1-302/ | 2026-10-31 |
| US-VA-section58.1-302.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-302 | 2026-10-28 |
| US-VA-dr-section58.1-390.3.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-390.3/ | 2026-10-31 |
| US-VA-dr-section58.1-394.1.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-394.1/ | 2026-10-31 |
| US-VA-dr-section58.1-402.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-402/ | 2026-10-31 |
| US-VA-dr-section58.1-408.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-408/ | 2026-10-31 |
| US-VA-dr-section58.1-422.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-422/ | 2026-10-31 |
| US-VA-dr-section58.1-453.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-453/ | 2026-10-31 |
| US-VA-dr-section58.1-455.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-455/ | 2026-10-31 |
| US-VA-dr-section58.1-486.2.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-486.2/ | 2026-10-31 |
| US-VA-dr-section58.1-492.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-492/ | 2026-10-31 |
| US-VA-dr-section58.1-504.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-504/ | 2026-10-31 |
| US-VA-dr-section58.1-603.1.html | https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-603.1/ | 2026-10-31 |
| US-VA-dr-section58.1-633.html | https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-633/ | 2026-10-31 |
| US-VA-dr-section58.1-3700.html | https://law.lis.virginia.gov/vacode/title58.1/chapter2/section58.1-3700/ | 2026-10-31 |
| US-VA-dr-section58.1-3703.1.html | https://law.lis.virginia.gov/vacode/title58.1/chapter2/section58.1-3703.1/ | 2026-10-31 |
| US-VA-dr-section58.1-3703.html | https://law.lis.virginia.gov/vacode/title58.1/chapter2/section58.1-3703/ | 2026-10-31 |
| US-VA-dr-section58.1-3703.1.html | https://law.lis.virginia.gov/vacode/title58.1/chapter2/section58.1-3703.1/ | 2026-10-31 |
| US-VA-dr-section58.1-3706.html | https://law.lis.virginia.gov/vacode/title58.1/chapter2/section58.1-3706/ | 2026-10-31 |
| US-VA-dr-section58.1-3716.html | https://law.lis.virginia.gov/vacode/title58.1/chapter37/section58.1-3716/ | 2026-11-01 |
| US-VA-dr-chapter3.html | https://law.lis.virginia.gov/vacode/title58.1/chapter3/ | 2026-10-31 |
| US-VA-dr-2025-500-instructions.pdf | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500-instructions.pdf | 2026-10-31 |
| US-VA-dr-2025-500a-instructions.pdf | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-500a-instructions.pdf | 2026-10-31 |
| US-VA-dr-2025-502-instructions.pdf | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-502-instructions.pdf | 2026-10-31 |
| US-VA-dr-2025-765-instructions.pdf | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2025-765-instructions.pdf | 2026-10-31 |
| US-VA-dr-alexandria-bpol-2025.html | http://web.archive.org/web/20250516180857id_/https://www.alexandriava.gov/taxes/business-license-tax | 2026-11-01 |
| US-VA-dr-alexandria-bpol-2025.md | http://web.archive.org/web/20250516180857/https://www.alexandriava.gov/taxes/business-license-tax | 2026-11-01 |
| US-VA-dr-arlington-bpol-rates.html | https://www.arlingtonva.us/Government/Programs/Taxes/Business-License-and-Taxes/Business-License-Tax/Business-License-Tax-Rates | 2026-11-01 |
| US-VA-dr-chesapeake-tax-rates.html | https://www.cityofchesapeake.net/237/Local-Tax-Rates | 2026-11-01 |
| US-VA-dr-chesapeake-biz-license.html | https://www.cityofchesapeake.net/212/Business-License-Tax | 2026-11-01 |
| US-VA-dr-chesterfield-bpol.html | https://www.chesterfield.gov/311/Business-Taxes-Rates-and-Appeals | 2026-11-01 |
| US-VA-dr-chesterfield-bpol-2025.html | http://web.archive.org/web/20250608161303id_/https://www.chesterfield.gov/311/Business-Taxes-Rates-and-Appeals | 2026-11-01 |
| US-VA-dr-fairfaxcity-bpol.html | https://www.fairfaxva.gov/Property-Business/Permit-License-Hub/Permit-Applications/Business-Licenses | 2026-11-01 |
| US-VA-dr-fairfaxcity-rates-levies-fy2026.pdf | https://www.fairfaxva.gov/files/assets/city/v/1/public-works/documents/stormwater/fy-2026-adopted-schedule-of-rates-levies.pdf | 2026-11-01 |
| US-VA-dr-fairfaxcounty-bpol-rates-2025.html | http://web.archive.org/web/20250715012113id_/https://www.fairfaxcounty.gov/taxes/business/bpol-license-rates | 2026-11-01 |
| US-VA-dr-fallschurch-bpol-rates.pdf | https://www.fallschurchva.gov/DocumentCenter/View/19410/3a-Business-License | 2026-11-01 |
| US-VA-dr-fallschurch-bl-instr-rates.pdf | https://www.fallschurchva.gov/DocumentCenter/View/757/Business-License-Instructions-and-Rates | 2026-11-01 |
| US-VA-dr-hampton-bpol-rates.html | https://www.hampton.gov/2145/Business-Tax-Rates | 2026-11-01 |
| US-VA-dr-hanover-bpol.html | https://www.hanovercounty.gov/384/Business-Licenses | 2026-11-01 |
| US-VA-dr-henrico-bpol-2025.html | http://web.archive.org/web/20250212143106id_/https://henrico.gov/services/business-license/ | 2026-11-01 |
| US-VA-dr-henrico-bpol-2025.md | http://web.archive.org/web/20250212143106/https://henricova.gov/193/Business-License-Tax | 2026-11-01 |
| US-VA-dr-herndon-bpol.html | https://www.herndon-va.gov/businesses/business-resources/business-licenses | 2026-11-01 |
| US-VA-dr-herndon-bpol-2025.md | http://web.archive.org/web/20251202112148/https://www.herndon-va.gov/businesses/business-resources/business-licenses | 2026-11-01 |
| US-VA-dr-leesburg-bpol.html | https://www.leesburgva.gov/departments/finance/taxes-fees/business-taxes | 2026-11-01 |
| US-VA-dr-leesburg-tax-rates-2025.md | http://web.archive.org/web/20250312/https://www.leesburgva.gov/departments/finance/taxes-fees/tax-rates-and-fees | 2026-11-01 |
| US-VA-dr-loudoun-bpol-rates-2025.html | http://web.archive.org/web/20250302161502id_/https://sheriff.loudoun.gov/1570/Business-Tax-Rates | 2026-11-01 |
| US-VA-dr-manassas-bpol-rates-2025.html | http://web.archive.org/web/20250303125710id_/https://www.manassasva.gov/connect/commissioner_of_the_revenue/business_taxes/business_licenses/bpol_rate_schedule.php | 2026-11-01 |
| US-VA-dr-manassaspark-bpol.html | https://www.manassasparkva.gov/departments/commissioner_of_the_revenue/business_licenses___taxes.php | 2026-11-01 |
| US-VA-dr-nn-tax-rates.html | https://www.nnva.gov/529/Tax-Rate-Schedules | 2026-11-01 |
| US-VA-dr-nn-bpol.html | https://www.nnva.gov/579/Business-License-Tax | 2026-11-01 |
| US-VA-dr-norfolk-biz-license.html | https://www.norfolk.gov/1744/Business-License | 2026-11-01 |
| US-VA-dr-norfolk-bpol.html | https://www.norfolk.gov/743/Business-Tax-Services | 2026-11-01 |
| US-VA-dr-petersburg-rate-sheet-2026.pdf | https://www.petersburgva.gov/DocumentCenter/View/9419/2026-Rate-Sheet- | 2026-11-01 |
| US-VA-dr-petersburg-rate-sheet-2026.txt | https://www.petersburgva.gov/DocumentCenter/View/9419/2026-Rate-Sheet-?bidId= | 2026-11-01 |
| US-VA-dr-portsmouth-bpol-rates.pdf | https://www.portsmouthva.gov/DocumentCenter/View/50/Business-License-Rate-Sheet-PDF | 2026-11-01 |
| US-VA-dr-pwc-tax-rates-2025.pdf | https://www.pwcva.gov/assets/2025-06/Tax%20Rates%20-%202025%20Final.pdf | 2026-11-01 |
| US-VA-dr-richmond-bpol.html | https://www.rva.gov/finance/bpol-tax | 2026-11-01 |
| US-VA-dr-suffolk-bpol-2025.html | http://web.archive.org/web/20250808105202/https://www.suffolkva.us/183/Business-Tax-License | 2026-11-01 |
| US-VA-dr-vb-bpol-rates.html | https://cor.virginiabeach.gov/tax-rates-important-dates-deadlines | 2026-11-01 |
| US-VA-dr-vienna-bpol.html | https://www.viennava.gov/Town-Departments/Finance/Business-Licenses | 2026-11-01 |
| US-VA-dr-vienna-biz-license-2025.md | http://web.archive.org/web/20250715/https://www.viennava.gov/Town-Departments/Finance/Business-Licenses | 2026-11-01 |
| US-VA-dr-vienna-renewal-2026.pdf | https://www.viennava.gov/files/assets/town/v/4/finance/business-licenses/2026_new-business-license-application.pdf | 2026-11-01 |

### 13.1 Statutory citations

- **Va. Code §58.1-400** - Corporate income tax (6% rate)
- **Va. Code §58.1-301 et seq.** - Federal conformity (fixed date)
- **Va. Code §58.1-302** - Definitions
- **Va. Code §58.1-322.02** - Virginia adjustments for individuals (PTE add-back)
- **Va. Code §58.1-390.3** - PTE election (effective tax year 2021, enacted 2022 HB 1121)
- **Va. Code §58.1-394** - Filing of S-corp / partnership return (Form 502)
- **Va. Code §58.1-394.1** - Penalty for late Form 502
- **Va. Code §58.1-402** - Modifications to federal taxable income
- **Va. Code §58.1-408** - Apportionment formula (general: property + payroll + double-weighted sales, denominator four)
- **Va. Code §58.1-417 through 58.1-422** - Special industry apportionment
- **Va. Code §58.1-422** - Manufacturer single sales factor (effective 2014)
- **Va. Code §58.1-422.1** - Retailer single sales factor (effective 2014)
- **Va. Code §58.1-442** - Consolidated/combined return election
- **Va. Code §58.1-453** - Extension of time to file (7 months for C corporations per 2025 Form 500 instructions)
- **Va. Code §58.1-492** - Underpayment of estimated tax (PTE)
- **Va. Code §58.1-504** - Corporate estimated tax safe harbor
- **Va. Code §58.1-3700 through 58.1-3735** - BPOL
- **Va. Code §58.1-3700.1** - BPOL definitions (definite place of business)
- **Va. Code §58.1-3703** - BPOL exemptions (manufacturer, banks, credit unions, etc.)
- **Va. Code §58.1-3706** - BPOL rate caps by classification
- **Va. Code §58.1-3715** - Out-of-state contractors; subcontractor deduction
- **Va. Code §58.1-3732** - Excluded items (deductions from BPOL base)

### 13.2 Regulatory and administrative guidance

- **23 VAC 10-120** - Virginia Administrative Code, corporate income tax regulations
- **Virginia Tax Bulletin** - annual fixed-date conformity bulletin (issued each spring)
- **2024 Guidelines for the Local Business, Professional and Occupational License Tax** - issued by the Virginia Department of Taxation, effective January 1, 2024, providing model guidance to localities under §58.1-3701
- **Department of Taxation Rulings** - searchable on tax.virginia.gov; particularly relevant for service-business BPOL classification disputes
- **Virginia Tax Commissioner letter rulings** - taxpayer-specific guidance with limited precedential value

### 13.3 Major recent legislation

- **2022 HB 1121** - Enacted PTE election effective tax year 2021 (retroactive)
- **2023 HB 1442** - Refined PTE election (cleared issues for tiered PTEs, added refundable credit mechanics)
- **2014 - General Assembly** - Manufacturer single sales factor (§58.1-422)
- **2014 session** - Retailer single sales factor (§58.1-422.1)
- **2026 Amendments to the 2025 Appropriation Act** - Fixed conformity date of December 31, 2025; partial conformity to the 2025 federal Budget Reconciliation Act (2025 Form 500 instructions)
- **2021 HB 1800 §3-5.23** - Unitary combined informational filing for one year (2021 only); did not result in mandatory unitary

### 13.4 Forms

- **Form 500** - Corporation Income Tax Return
- **Form 500ES** - Corporation Estimated Tax
- **Form 500CP** - Extension Payment Voucher
- **Form 500C** - Underpayment of Estimated Tax
- **Form 500CR** - Credit Schedule (includes consolidation election)
- **Form 500ADJ** - Schedule of Adjustments
- **Form 500A** - Apportionment Schedule
- **Form 500AB** - Add-backs schedule
- **Form 502** - Pass-Through Entity Return (informational)
- **Form 502PTET** - PTE election return
- **Form 502W** - PTE withholding payment
- **Form 502V** - PTE return payment voucher
- **Form 760** - Resident Individual Income Tax Return (referenced for owner credit)
- **Form 763** - Nonresident Individual Income Tax Return
- **Form 765** - Composite return
- **Form PTE** - PTE credit information to owners
- **Local BPOL applications/renewals** - vary by locality; common forms include "Business License Application" or "Business License Renewal" with Schedule of Gross Receipts by Classification

### 13.5 Caveats and confidence

The following items in this skill should be flagged for reviewer confirmation:

1. **Conformity vehicle** - the December 31, 2025 conformity date was set by the 2026 Amendments to the 2025 Appropriation Act per the 2025 Form 500 instructions; monitor the 2027 session for further changes (see §2.5).
2. **BPOL rate tables (§8)** - locality rates change frequently. The figures in §8 were read from locality rate pages and rate sheets captured 2026-10-31 through 2026-11-01 (see Sources); rates change annually - always verify with the locality's Commissioner of the Revenue.
3. **IT consulting classification** - the professional-vs-business-services classification varies by locality and is contested (see §9.3). Request a written ruling for any material engagement.
4. **Manufacturer BPOL exemption** - fact-specific under §58.1-3703(C)(4); requires that sales be at wholesale (see §12.2).
5. **PTE election interaction with nonresident state credits** - verify each nonresident owner's home-state treatment (§5.7).

### 13.6 Out of scope - refer to companion skills

- Federal Schedule C, Schedule SE - see `us-sole-prop-bookkeeping` and `us-schedule-c-and-se-computation`
- Federal Form 1120S - see federal S-corp skill (pending)
- Virginia individual income tax computation - see `va-individual-income-tax` (pending)
- Virginia sales and use tax - see `va-sales-use-tax` (pending)
- Virginia M&T and personal property - see `va-local-property-taxes` (pending)

Not yet confirmed: Manassas Park BPOL rates; Portsmouth BPOL rates; Chesapeake BPOL rates; Herndon BPOL rates; Henrico repair-service rate; Suffolk threshold; Hanover rates other than the $0.10 contractor rate; rates for Williamsburg, York County, James City County, Charlottesville, Albemarle County, Roanoke, Lynchburg, Winchester, and Fredericksburg; the claim that the 6% corporate rate dates to 1972; HB 1121 and 2021 HB 1800 legislative references.

## End of skill

*End of skill. Tax year 2026 (worked examples use 2025 figures).*

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network - accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.