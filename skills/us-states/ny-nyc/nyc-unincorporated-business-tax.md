---
name: nyc-unincorporated-business-tax
description: Use this skill whenever asked about the New York City Unincorporated Business Tax (UBT). Trigger on phrases like "NYC UBT", "unincorporated business tax", "NYC-202", "NYC-202S", "IT-219 credit", "NYC Admin Code Title 11 Chapter 5". Covers the 4% rate, the credit and exemption bands, who is subject, and the NYC personal-income-tax credit that limits double taxation.
jurisdiction: US-NY-NYC
tax_year: 2026
last_updated: 2026-11-02
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NYC Unincorporated Business Tax

> **Source-cited draft.** Built from the New York City Administrative Code, Title 11, Chapter 5 (current code text, read 2026-10-31), the 2025 instructions for Forms NYC-202, NYC-202S and NYC-204, the current instructions for Form IT-219, the NYC Department of Finance UBT page, and the NYC Comptroller's report "Recent Trends in the City's Business Income Taxes" (February 18, 2025). No accountant has reviewed it. Do not file from it without review by a qualified New York City professional.

Tax year: the calendar year. Authority: New York City Department of Finance (DOF). Governing law: the New York City Administrative Code, Title 11, Chapter 5 (Unincorporated Business Tax).

See also: `ny-cross-border`, `ny-income-tax`.

## Who this applies to

- **Every individual or unincorporated entity carrying on a trade, business, or profession wholly or partly in NYC** is subject to UBT: "UBT is imposed on every individual or unincorporated entity carrying on a trade, business, or profession wholly or partly in NYC."
- **Sole proprietors (IRS Schedule C businesses) and unincorporated entities (partnerships and LLCs)** pay UBT; the Business Corporation Tax (BCT) applies to C-corporations and the General Corporation Tax (GCT) to S-corporations.
- **Private equity and hedge funds** organized as LLPs or LLCs "are subject to UBT for their management fees but not for carried interest (the performance fee based on realized profits)."
- **Self-trading is largely outside the base:** "Income derived from trading on one's own account ('self-trading') is, with some exceptions, exempt from UBT."
- **Employees are not carrying on an unincorporated business** for their employment income: "The performance of services by an individual as an employee or as an officer or director of a corporation, society, association, or political entity, or as a fiduciary, shall not be deemed an unincorporated business, unless such services constitute part of a business regularly carried on by such individual" (Admin Code § 11-503(b)).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| UBT income tax rate | **4%** | 2025 and 2026 (DOF: "A 4% tax rate is charged for taxable income allocated to New York City") | [DOF UBT page](https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page); [Comptroller, Table 1 "Summary of main features"](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |
| Unincorporated business exemption | **flat $5,000** for every unincorporated business, proprietor or partnership, "prorated for taxable years of less than twelve months" | current code text | [Admin Code § 11-510(1)](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-9723); [NYC-202 instructions, line 15](https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf) |
| Per-partner exemption | **none** - the additional partner exemption was allowed only "for any taxable year of the unincorporated business beginning" on or before June 30, 1994 | repealed | [Admin Code § 11-510(2)](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-9723) |
| Full credit against the tax | allowed "if the tax computed under subdivision (a) of this section is three thousand four hundred dollars or less" | current code text | [Admin Code § 11-503(b)(3-a)(A)](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-222406); NYC-202 instructions |
| Partial credit band | tax **above $3,400 and below $5,400**: credit = tax x ($5,400 - tax) / $2,000 | current code text | [Admin Code § 11-503(b)(3-a)(B)](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-222406); NYC-202 instructions ("$5,400 minus the amount of the tax on line 17 ... $2,000") |
| No credit | tax of $5,400 or more | current code text | [Admin Code § 11-503(b)(3-a)(C)](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-222406) |
| Zero-liability point | **$90,000** of NYC-allocated net income when no § 11-509(a) owner-allowance is claimed: 4% x ($90,000 - $5,000) = $3,400, fully credited. The $5,000 exemption is flat, so with no allowance the point does not depend on partner count; if the allowance is claimed it rises by the allowance (a proprietor claiming $10,000 reaches zero at $100,000) | derived from the rows above plus § 11-509(a) | §§ 11-503, 11-509, 11-510 |
| Filing threshold | gross income **over $95,000** (before any deduction for cost of goods sold or services performed), all business wherever carried on | taxable years beginning after 2008 | [Admin Code § 11-514(a)(4)](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-9723); NYC-202 and NYC-202S instructions ("has a total gross income from all business regardless of where carried on of more than $95,000") |
| Estimated-tax declaration | required if "its estimated tax can reasonably be expected to exceed three thousand four hundred dollars" | taxable years beginning after 2008 | [Admin Code § 11-511(a)(4)](https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-9723) |
| NYC personal-income-tax credit for UBT paid (Form IT-219) | **100%** of UBT imposed for city taxable income of **$42,000 or less**, decreasing "gradually from 100% to 23%" above $42,000 and below $142,000, **23%** at $142,000 or more; capped so NYC PIT cannot go below zero; "Any unused credit cannot be refunded or carried over" | current | [IT-219 instructions](https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf); [Comptroller report](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |

The Comptroller report's February 2025 table still shows a $15,000 proprietor exemption, a "$5,000 plus $10,000 per partner" partnership exemption, a partial band up to $4,500, and zero liability "up to $100,000." The archived Administrative Code and the 2025 DOF instructions state a flat $5,000 exemption and the $3,400-to-$5,400 band; the statute and instructions govern, and the report's figures are treated as outdated.

## The taxable base

- **Base is net income of the unincorporated business** carried on wholly or partly in NYC, taxed at 4% (DOF UBT page; Comptroller report, Table 1).
- **The $5,000 exemption comes off before the credit** (§ 11-510(1); NYC-202 instructions, line 15).
- **Owner compensation allowance:** § 11-509(a) allows "deductions for reasonable compensation ... for personal services of the proprietor and each partner actively engaged in the unincorporated business" - capped at $5,000 per person for taxable years beginning before January 1, 2007 and **$10,000 per person for taxable years beginning on or after January 1, 2007** - and "the aggregate of such deductions shall not exceed twenty per centum" of the UBT income computed without these deductions or the § 11-510 exemptions. The 2025 NYC-202 instructions implement it on line 13: "The allowable deduction is: 1) 20% of line 12 or 2) $10,000, whichever is lower. If line 12 is a loss, enter '0' on line 13." Worked examples 1-2 and the partnership variant below assume no allowance is claimed; example 3 shows the allowance.
- **Self-trading income is excluded** "with some exceptions" (Comptroller report); carried interest of fund managers is outside the base while management fees are inside it.
- **Multi-jurisdiction businesses are allocated, not fully taxed here:** "business income of entities doing businesses across taxing jurisdictions is allocated based on apportionment and sourcing rules," and UBT uses a **single sales factor** apportionment with **cost-of-performance sourcing for services provided within NYC, except for sales of tangible personal property** (Comptroller report).
- **Investment income under UBT** "is allocated using investment allocation percentages, which are themselves determined using issuer allocation percentages" (Comptroller report).

## Deadlines and filing

- **Forms (2025 returns):** Form NYC-202 for individuals and sole proprietors ("Single-member LLCs must file on Form NYC-202"); Form NYC-204, the "Unincorporated Business Tax Return for Partnerships, including Limited Liability Companies" (Form 204EZ variant); Form NYC-202EIN for estates and trusts; Form NYC-202S, the simplified individual return.
- **Annual due dates (2025 returns, per the archived 2025 instructions):** Form NYC-202 "is due on or before April 15, 2026, or, for fiscal year taxpayers, on or before the 15th day of the fourth month following the close of the taxable year" (NYC-202 instructions). Form NYC-204: "For taxable years beginning on or after January 1, 2025, Form NYC-204 is due on or before March 16, 2026, or, for fiscal year taxpayers, on or before the 15th day of the third month following the close of the taxable year" (NYC-204 instructions). Note: the archived code text of § 11-514(a) reads "the fifteenth day of the third month" for taxable years beginning on or after January 1, 2016 - that matches the NYC-204 instructions but not the NYC-202 instructions' April 15 date; see Not yet confirmed.
- **Extension:** Form NYC-EXT, "Application for Automatic 6-month Extension of Time to File Business Tax Return. File Form NYC-EXT on or before the due date of the return" (NYC-202 instructions).
- **Estimated tax:** a declaration is required when estimated tax can reasonably be expected to exceed $3,400 (§ 11-511(a)(4)); the declaration is due "on or before April fifteenth of the taxable year," with later dates if the threshold is met mid-year (§ 11-511(c)); estimated payments are made with Form NYC-5UBTI (NYC-202 instructions; DOF UBT page lists NYC-5UB / NYC-5UBTI for 2026).
- **Simplified return (NYC-202S):** eligibility is set by 12 listed conditions in the 2025 instructions (no allocation of business income, no investment capital or income, no NOL deduction, filing timely with no late penalties, and similar); the $250,000 gross-income cap previously carried in this guide does not appear in the 2025 instructions - see Not yet confirmed.

## Penalties and interest

- **No archived source in this pack states the UBT late-filing, late-payment or interest rates.** The figures previously carried in this guide are removed and listed under Not yet confirmed.
- The archived DOF page confirms only that NYC can abate "interest and penalty" by legislation in specific circumstances (the One Big Beautiful Bill Act decoupling abatement, entered with Special Condition Code "OB"); that is an abatement rule, not the UBT penalty schedule.
- Do not quote a UBT penalty or interest percentage to a client until the NYC Administrative Code penalty sections are archived and read.

## Cross-border points

- **Apportionment:** UBT uses a **single sales factor** - the City "gradually transitioned to only using the share of sales" between 2009 and 2018 (Comptroller report). A business with workers and real estate in NYC but a low share of NYC sales is taxed on less; the reverse increases the base.
- **Sourcing:** "GCT and UBT use cost of performance for services provided within NYC, except for sales of tangible personal property," while BCT adopted market-based sourcing (Comptroller report). A NYC-based service provider to an out-of-state customer is therefore still NYC-taxed on those receipts under UBT.
- **Multi-jurisdiction exposure is the norm, not the exception:** "Between tax year 2011 and 2020 ... on average 72.2% of the City tax liability came from multi-jurisdiction businesses" (Comptroller report).
- **No combined reporting under UBT** (Comptroller report), so a partner's own entity structure does not fold into one UBT return.
- **IT-219 credit:** New York State residents and part-year residents claim the credit for NYC UBT paid on Form IT-219 against their New York City personal income tax; the credit is 100% of the UBT imposed at city taxable income of $42,000 or less, decreases gradually to 23% between $42,000 and $142,000, and is 23% at $142,000 or more; it cannot reduce NYC tax below zero and unused credit "cannot be refunded or carried over" (IT-219 instructions). A partner claims the credit for the allocated share of UBT paid by the partnership (IT-219 instructions).

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used.

### Worked example 1: proprietor at the zero-liability point

A sole proprietor (hypothetical) has $90,000 of NYC net business income, and no § 11-509(a) owner-allowance is claimed (the examples isolate the exemption and credit bands; example 3 adds the allowance). The flat $5,000 exemption leaves $85,000; 4% of $85,000 is $3,400, which is at the $3,400 full-credit ceiling, so UBT liability is $0. Because the $5,000 exemption is flat, the $90,000 zero-liability point does not depend on partner count when no allowance is claimed; if the proprietor claimed the $10,000 allowance, the zero-liability point would rise to $100,000.

```oa-check
name: NYC UBT proprietor at zero-liability point
inputs:
  net_income: 90000
  exemption: 5000
  rate: 0.04
  full_credit: 3400
steps:
  - taxable: net_income - exemption
  - tax_before_credit: taxable * rate
  - ubt_due: max(0, tax_before_credit - full_credit)
expected:
  taxable: 85000
  tax_before_credit: 3400
  ubt_due: 0
```

### Worked example 2: proprietor in the partial-credit band

A sole proprietor (hypothetical) has $120,000 of NYC net business income, and no § 11-509(a) owner-allowance is claimed. $120,000 - $5,000 = $115,000; 4% is $4,600, which sits in the partial band above $3,400 and below $5,400. The credit is $4,600 x ($5,400 - $4,600) / $2,000 = $1,840, so UBT liability is $4,600 - $1,840 = $2,760.

```oa-check
name: NYC UBT proprietor in partial-credit band
inputs:
  net_income: 120000
  exemption: 5000
  rate: 0.04
  band_top: 5400
  band_denominator: 2000
steps:
  - taxable: net_income - exemption
  - tax_before_credit: taxable * rate
  - partial_credit: tax_before_credit * (band_top - tax_before_credit) / band_denominator
  - ubt_due: tax_before_credit - partial_credit
expected:
  taxable: 115000
  tax_before_credit: 4600
  partial_credit: 1840
  ubt_due: 2760
```

### Worked example 3: proprietor claiming the § 11-509(a) owner-allowance

A sole proprietor (hypothetical) has $120,000 of NYC net business income and claims the § 11-509(a) allowance for personal services. The allowance is the lesser of 20% of net income (20% x $120,000 = $24,000) or the $10,000 per-person cap, so $10,000 (NYC-202 instructions, line 13). $120,000 - $10,000 - $5,000 = $105,000; 4% is $4,200, in the partial band. The credit is $4,200 x ($5,400 - $4,200) / $2,000 = $2,520, so UBT liability is $4,200 - $2,520 = $1,680 - $1,080 less than the same proprietor with no allowance (example 2).

```oa-check
name: NYC UBT proprietor claiming 11-509(a) allowance
inputs:
  net_income: 120000
  per_person_cap: 10000
  pct_cap: 0.20
  exemption: 5000
  rate: 0.04
  band_top: 5400
  band_denominator: 2000
steps:
  - pct_amount: net_income * pct_cap
  - allowance: min(per_person_cap, pct_amount)
  - taxable: net_income - allowance - exemption
  - tax_before_credit: taxable * rate
  - partial_credit: tax_before_credit * (band_top - tax_before_credit) / band_denominator
  - ubt_due: tax_before_credit - partial_credit
expected:
  allowance: 10000
  taxable: 105000
  tax_before_credit: 4200
  partial_credit: 2520
  ubt_due: 1680
```

### Partnership variant (prose only - not a counted worked example)

A two-partner LLC (hypothetical) with $110,000 of NYC net business income is **not** at zero when no § 11-509(a) allowance is claimed: the exemption is the flat $5,000 (the per-partner exemption was repealed for taxable years beginning after June 30, 1994), so the tax is 4% x $105,000 = $4,200; the partial credit is $4,200 x ($5,400 - $4,200) / $2,000 = $2,520; liability is $1,680. If both partners are actively engaged and each claims the $10,000 allowance, the aggregate $20,000 is within the 20% cap (20% x $110,000 = $22,000), the base falls to $110,000 - $20,000 - $5,000 = $85,000, the tax is 4% x $85,000 = $3,400, fully credited, and liability is $0 - so with the allowance claimed, the zero-liability point does depend on partner count.

## Ask the client first

1. **What is the entity form?** Sole proprietorship, partnership or LLC pays UBT (NYC-202 vs NYC-204); a C-corporation pays BCT and an S-corporation GCT instead (Comptroller report; NYC-202/204 instructions).
2. **Is the activity carried on wholly or partly in NYC, and where is the service performed?** UBT sources services by cost of performance for work done in NYC (Comptroller report).
3. **Is the income self-trading or carried interest?** Both sit outside the UBT base, with exceptions (Comptroller report).
4. **What is the client's NYC personal-income-tax position?** The IT-219 credit for UBT paid is 100% up to $42,000 of city taxable income and falls to 23% at $142,000 or more (IT-219 instructions), so the net cost of UBT depends on it.
5. **Does the client qualify for the simplified NYC-202S?** Check the 12 eligibility conditions in the instructions; and confirm the current-year NYC-202 due date with DOF, since the archived code text (third month) and the 2025 NYC-202 instructions (April 15) state different months.

## Sources

| Source | URL | Read on |
|---|---|---|
| NYC Administrative Code, Title 11, Chapter 5, § 11-503 (imposition of tax; credit bands: full at $3,400 or less, partial formula to $5,400, none at $5,400 or more) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-222406 | 2026-10-31 |
| NYC Administrative Code, Title 11, Chapter 5, §§ 11-509 to 11-514 (owner-compensation deduction caps; $5,000 exemption and repealed partner exemption; $3,400 estimated-tax threshold; $95,000 filing threshold; return due date text) | https://codelibrary.amlegal.com/codes/newyorkcity/latest/NYCadmin/0-0-0-9723 | 2026-10-31 |
| Instructions for Form NYC-202, 2025 (due April 15, 2026; NYC-EXT extension; $5,000 exemption line 15; credit formula $5,400; NYC-5UBTI estimated payments; single-member LLCs file NYC-202) | https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202-instr_2025.pdf | 2026-10-31 |
| Instructions for Form NYC-202S, 2025 ($95,000 filing threshold; 12 eligibility conditions, no gross-income cap) | https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-202s-instr_2025.pdf | 2026-10-31 |
| Instructions for Form NYC-204, 2025 ("Unincorporated Business Tax Return for Partnerships, including Limited Liability Companies"; due on or before March 16, 2026, or the 15th day of the third month for fiscal year taxpayers) | https://www.nyc.gov/assets/finance/downloads/pdf/25pdf/business_tax_forms/nyc-204-instr_2025.pdf | 2026-10-31 |
| Instructions for Form IT-219, Credit for New York City Unincorporated Business Tax (current) ($42,000/$142,000 credit bands, 100% to 23%, cap at NYC tax, no carryover) | https://www.tax.ny.gov/pdf/current_forms/it/it219i.pdf | 2026-10-31 |
| NYC Department of Finance, Unincorporated business tax (UBT) page - "A 4% tax rate is charged for taxable income allocated to New York City"; 2026 UBT forms listed as NYC-5UB / NYC-5UBTI | https://www.nyc.gov/site/finance/business/business-unincorporated-business-tax-ubt.page | 2026-10-31 |
| NYC Comptroller, "Recent Trends in the City's Business Income Taxes" (Feb 18, 2025) - UBT scope, 4% rate, $42,000/$142,000 PIT-credit bands, single sales factor, cost-of-performance sourcing, self-trading and carried interest, no combined reporting, 72.2% multi-jurisdiction share (its exemption and credit-band figures are outdated against the code text) | https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/ | 2026-10-28 |
| NYC Department of Finance, business corporation tax page - OBBBA interest-and-penalty abatement, Administrative Code §§ 11-653 and 11-654 citations | https://www.nyc.gov/site/finance/business/business-corporation-tax.page | 2026-10-28 |

Not yet confirmed: the simplified-return gross-income threshold (previously carried as $250,000 on Form NYC-202S; the 2025 instructions list 12 eligibility conditions with no gross-income cap); the quarterly estimated-installment due dates for UBT (the archived § 11-511(c) states declaration dates, not installment dates); the UBT late-filing penalty, late-payment penalty and interest rates (no archived source states them); whether the archived § 11-514(a) "fifteenth day of the third month" text or the 2025 NYC-202 instructions' April 15 date states the current statutory due date for NYC-202 (the 2025 NYC-204 instructions' March 16, 2026 date matches the code text, the NYC-202 instructions do not); whether partnerships compute the § 11-509(a) allowance on the NYC-204 the same way the NYC-202 line 13 instructions describe for proprietors; and any phase-out of the $5,000 exemption (none appears in the archived § 11-510 text).

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
