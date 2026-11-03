---
name: nv-commerce-and-mbt
description: Tier 2 Nevada content skill for tax year 2026 covering the Commerce Tax (NRS 363C, 0.051%-0.331% on Nevada gross revenue over $4M) and the Modified Business Tax (1.17% general, 1.554% financial institutions and mining, effective July 1, 2023), including the 50% Commerce Tax credit against MBT.
jurisdiction: US-NV
tax_year: 2026
last_updated: 2026-11-03
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NV Commerce Tax and Modified Business Tax

Nevada imposes no personal income tax: Article 10, Section 1 of the Nevada Constitution bars any tax on wages or personal income of natural persons. State-level business taxation instead runs through two parallel regimes. The Commerce Tax (NRS Chapter 363C) is a gross-receipts tax on business entities whose Nevada gross revenue exceeds $4,000,000 in a July 1 to June 30 taxable year, at rates from 0.051% to 0.331% across 26 statutory business categories (NRS 363C.310 to 363C.560). The Modified Business Tax (MBT) is a quarterly payroll tax on Nevada wages: 1.17% of taxable wages above $50,000 per quarter for general businesses (NRS 363B.110, as reduced under NRS 360.203) and 1.554% with no threshold for financial institutions and mineral-producers-taxpayers (NRS 363A.130, as reduced under NRS 360.203). Both rates took effect July 1, 2023. A credit of 50% of the Commerce Tax paid offsets MBT in the four calendar quarters immediately following the Commerce Tax year (NRS 363B.110(4), NRS 363A.130(4)).

## Who this applies to

- **Commerce Tax**: every "business entity" engaged in a business in Nevada whose Nevada gross revenue exceeds $4,000,000 for the July 1 to June 30 taxable year (NRS 363C.200(1)). "Business entity" is defined broadly (corporations, LLCs, partnerships, trusts and similar arrangements) but excludes, among others: a natural person unless required to file IRS Schedule C, E or F; governmental entities; nonprofit organizations described in IRC 501(c); credit unions; grantor trusts; estates of natural persons; REITs and REMICs; qualified plans; passive entities; persons whose Nevada activity is confined to owning intangible investments; exhibition participants; and persons engaged in extracting gold and silver ores (NRS 363C.020). "Engaging in a business" is defined at NRS 363C.035.
- **MBT (general, NRS 363B)**: every "employer" required to pay contributions under NRS 612.535 (Nevada unemployment insurance), other than financial institutions, taxpayers subject to the net proceeds of minerals tax, and certain governmental, tribal and nonprofit employers (NRS 363B.030).
- **MBT (financial institutions and mining, NRS 363A)**: financial institutions as defined at NRS 363A.050 that are conducting a business activity in Nevada, plus any person subject to the net proceeds of minerals tax under NRS 362.100 to 362.240, who is an "employer" for Chapter 363A purposes (NRS 363A.030(1)(b)).
- **Not covered here**: sales and use tax, live entertainment tax, gaming taxes, insurance premium tax, modified business tax abatement claims, and local licensing. See the cross-references below.

## Rates, bands and thresholds

### Modified Business Tax

| Item | General business (NRS 363B) | Financial institutions and mining (NRS 363A) |
|---|---|---|
| Effective rate from July 1, 2023 | 1.17% | 1.554% |
| Statutory rate before the NRS 360.203 reduction | 1.475% (NRS 363B.110(1)) | 2% (NRS 363A.130(1)) |
| Quarterly wage threshold | $50,000 of taxable wages (NRS 363B.110(1)) | none |
| Health benefit deduction | 100% of amounts paid by the employer (NRS 363B.115) | 100% of amounts paid by the employer (NRS 363A.135) |
| Return | TAX-F003 | TAX-F002 (financial institutions); separate MBT-Mining return for mineral-producers-taxpayers |

Rate history per the Department of Taxation MBT FAQs: the general rate was 0.63% before July 1, 2009, 1.475% before July 1, 2015, and 1.378% before July 1, 2019; the financial-institution rate was 2% from October 1, 2003 to July 1, 2015 and 1.853% from July 1, 2015 to June 30, 2023. Effective July 1, 2023 the rates dropped to 1.17% and 1.554% under the NRS 360.203 reduction mechanism, which stops further reductions once the general rate reaches 1.17% (NRS 360.203(4)). The 1.378% and 1.853% rates expired June 30, 2023 and should not be used for any quarter beginning on or after July 1, 2023. The wage-comparison trigger that drives the NRS 360.203 reductions was suspended for 2015 to 2019 and resumes with the comparison period beginning January 1, 2026 (MBT FAQs).

Misclassification between the two MBT regimes costs 0.384 percentage points: on $1,000,000 of annual Nevada wages that is $3,840 per year.

### Commerce Tax (NRS 363C.300 to 363C.560)

Tax equals (Nevada gross revenue minus $4,000,000) times the rate of the business category in which the entity is primarily engaged (NRS 363C.200, 363C.300). The category is the one producing the highest percentage of the entity's Nevada gross revenue (NRS 363C.097).

| Business category | NAICS | Rate | Section |
|---|---|---|---|
| Agriculture, forestry, fishing and hunting | 11 | 0.063% | NRS 363C.310 |
| Mining, quarrying and oil and gas extraction | 21 | 0.051% | NRS 363C.320 |
| Utilities and telecommunications | 22, 517 | 0.136% | NRS 363C.330 |
| Construction | 23 | 0.083% | NRS 363C.340 |
| Manufacturing | 31, 32, 33 | 0.091% | NRS 363C.350 |
| Wholesale trade | 42 | 0.101% | NRS 363C.360 |
| Retail trade | 44, 45 | 0.111% | NRS 363C.370 |
| Air transportation | 481 | 0.058% | NRS 363C.380 |
| Rail transportation | 482 | 0.331% | NRS 363C.390 |
| Other transportation | 483, 485-488, 491, 492 | 0.129% | NRS 363C.400 |
| Truck transportation | 484 | 0.202% | NRS 363C.410 |
| Warehousing and storage | 493 | 0.128% | NRS 363C.420 |
| Publishing, software and data processing | 512, 513, 516, 518 | 0.253% | NRS 363C.430 |
| Finance and insurance | 52 | 0.111% | NRS 363C.440 |
| Real estate and rental and leasing | 53 | 0.25% | NRS 363C.450 |
| Professional, scientific and technical services | 54 | 0.181% | NRS 363C.460 |
| Management of companies and enterprises | 55 | 0.137% | NRS 363C.470 |
| Administrative and support services | 561 | 0.154% | NRS 363C.480 |
| Waste management and remediation services | 562 | 0.261% | NRS 363C.490 |
| Educational services | 61 | 0.281% | NRS 363C.500 |
| Health care and social assistance | 62 | 0.190% | NRS 363C.510 |
| Arts, entertainment and recreation | 71 | 0.24% | NRS 363C.520 |
| Accommodation | 721 | 0.2% | NRS 363C.530 |
| Food services and drinking places | 722 | 0.194% | NRS 363C.540 |
| Other services | 81 | 0.142% | NRS 363C.550 |
| Unclassified business entities | - | 0.128% | NRS 363C.560 |

The category election matters: on $1,000,000 of Nevada gross revenue above the threshold, the difference between publishing and software at 0.253% and professional services at 0.181% is $720 of additional tax. The initial return must designate the category, and the designation cannot be changed unless the taxpayer applies to the Department and the Department determines the business is no longer primarily engaged in the designated category (NRS 363C.200(3)).

### Taxes outside this skill (for scoping only)

- Sales and use tax: statewide base 6.85%, composed of 2.00% (NRS 372) plus 2.60% local school support (NRS 374) plus 0.50% and 1.75% city relief components (NRS 377). Clark County combined 8.375% (effective January 1, 2020); Washoe County combined 8.265% (effective April 1, 2017). See the Nevada sales tax skill.
- Live entertainment tax: 9% (NRS 368A).
- Gaming: 3.5% to 6.75% on gaming revenue (NRS 463.370).
- Insurance premium tax: 3.5% (NRS 680B.027).
- Unemployment insurance taxable wage base: $41,800 for 2025 (DETR contributions newsletter, June 2025).

## The taxable base

### Commerce Tax

- **Gross revenue** means the total amount realized from engaging in a business in Nevada without deduction for cost of goods sold or other expenses, including the fair market value of property and services received and debt forgiven as consideration; it excludes, among other items, amounts from licensing trademarks, patents and similar intellectual property, cash discounts taken, complimentary goods or services, certain IRC reorganization and like-kind transactions, and donations to 501(c)(3) organizations (NRS 363C.045).
- **Deductions from gross revenue** (NRS 363C.210(1)) include: revenue the state is barred from taxing under federal law; revenue already taxed under another Nevada regime (mining net proceeds, gaming, insurance premium tax); health care provider payments (fully deductible for most providers, 50% for certain institutions); pass-through revenue; the tax basis of securities and loans sold; interest income other than interest on credit sales; dividends and distributions; receipts from the sale or exchange of IRC 1221 or 1231 assets not held for sale in the ordinary course; hedging receipts; and proceeds from issuing the entity's own debt or equity.
- **Situs of Nevada gross revenue** (NRS 363C.220): real property is sitused where it is located; tangible personal property where it is delivered or shipped to the purchaser (or located if not shipped); transportation revenue only if both the origin and the destination of the shipment are in Nevada; services are sitused to where the benefit is received in Nevada, with the location where the benefit is received paramount; and a residual rule situs other revenue to where the purchaser is located (NRS 363C.220(1)(a) to (g)).
- **Tax**: (Nevada gross revenue minus $4,000,000) times the category rate. Entities at or below $4,000,000 are not required to file (NRS 363C.200(2)).

### Modified Business Tax

- **Wages** take the meaning given in NRS 612.190 (NRS 363B.110(1)). Gross wages are all wages paid during the quarter, including reported tips, with no cap (MBT FAQs).
- **General MBT base**: taxable wages minus the health benefit deduction minus $50,000 per quarter; the rate applies only to the excess (NRS 363B.110(1)). The $50,000 threshold is per quarter and does not carry over to other quarters.
- **Health benefit deduction**: the full amount paid by the employer for health insurance or health benefit plans for employees, including self-insured plan claims plus administration costs, premiums to insurers, and payments to trust funds under Taft-Hartley arrangements; workers' compensation premiums and employee-paid amounts do not qualify (NRS 363B.115(2), NRS 363A.135). Employer contributions to health savings accounts do not qualify (MBT FAQs). Any deduction exceeding the quarter's taxable wages carries forward to the next quarter until fully used (NRS 363B.115(3)).
- **MBT is not deductible from employee wages**: an employer may not withhold or deduct the MBT from an employee's wages (NRS 363B.110(2)(b), NRS 363A.130(2)(b)).
- **First-four-years abatement**: a new employer's MBT is abated 50% for its first four taxable years (NRS 363B.120, administered under NRS 360.750). This is separate from the Commerce Tax credit, which lives at NRS 363B.110(4).

## Deadlines and filing

### Commerce Tax

- Taxable year: July 1 to June 30 (NRS 363C.080).
- Return (Form EXC-F025) and payment are due on or before the 45th day immediately following the end of the taxable year, i.e. August 14 (NRS 363C.200(2); Form EXC-F025 instructions; the Department's 2025-2026 filing was due August 14, 2026).
- No return is required for a taxable year in which Nevada gross revenue is $4,000,000 or less (NRS 363C.200(2)).
- Extension: on written application made before the payment due date, the Department may extend the time to pay by not more than 30 days for good cause; no penalty accrues during the extension, but interest runs at 0.75% per month from the original due date (NRS 363C.200(4)). The Department offers a combined 30-day extension of time to file and pay.

### Modified Business Tax

- Returns and payment are due by the last day of the calendar month following the end of each calendar quarter (NRS 363B.110(3), NRS 363A.130(3)): April 30, July 31, October 31 and January 31.
- A return must be filed even when no wages were paid and no tax is due (MBT FAQs).
- Forms: TAX-F003 (general business), TAX-F002 (financial institutions), and a separate MBT-Mining return for taxpayers subject to the net proceeds of minerals tax (MBT FAQs).
- **Commerce Tax credit**: an employer that paid the Commerce Tax for a taxable year may claim a credit equal to 50% of the Commerce Tax paid against the MBT computed for each of the 4 calendar quarters immediately following the end of that Commerce Tax taxable year. The credit in any quarter cannot exceed the MBT computed for that quarter; any unused credit after the fourth quarter lapses and is not refundable (NRS 363B.110(4), NRS 363A.130(4)). The credit is claimed on the MBT return (TAX-F003 line 10 / TAX-F002).

## Penalties and interest

- Late MBT filing penalties are graduated by days late under NAC 360.395: 2% of the tax due for 1 to 10 days, 4% for 11 to 15 days, 6% for 16 to 20 days, 8% for 21 to 30 days, and 10% for more than 30 days; 10% is the maximum, not a flat rate (TAX-F003 instructions).
- Interest on underpayments accrues at 0.75% per month under NRS 360.417 (TAX-F003 instructions; the rate was reduced from 1% to 0.75% per month effective July 1, 2011, per the Department's sales and use tax page).
- Commerce Tax extension period interest: 0.75% per month (NRS 363C.200(4)).

## Cross-border points

- The Commerce Tax reaches out-of-state entities: it is imposed on the privilege of engaging in a business in Nevada (NRS 363C.200(1)), and the situs rules in NRS 363C.220 pull in revenue from goods delivered to Nevada purchasers and services whose benefit is received in Nevada, without any physical-presence condition in the statute.
- The MBT follows the Nevada unemployment insurance system: an employer required to pay Nevada UI contributions is inside the MBT net (NRS 363B.030).
- Related entities: for financial-institution status, entities are related if at least 50% of the interest in each, by vote or value, is owned directly or indirectly by the same entity (NRS 363A.050(3)(e)); a related entity is a financial institution even if it does no business in Nevada (NRS 363A.050(1)(r)).
- Insurance salespeople are excluded from financial-institution status if more than 50% of the business's annual commission income comes from selling, soliciting or negotiating insurance (NRS 363A.050(2)(c), 363A.050(3)(d)).
- Mining: taxpayers subject to the net proceeds of minerals tax (NRS 362.100 to 362.240) are "employers" under Chapter 363A and pay the 1.554% MBT rate (NRS 363A.030(1)(b), added by SB 483 (2019); MBT FAQs).
- Nevada's constitutional bar on taxing wages of natural persons (Article 10, Section 1) means the MBT is an employer-level tax, never a personal income tax on the employee.

## Worked examples

### Worked example 1: SaaS company over $4M, publishing and software category, with the MBT credit

Sierra Cloud Inc. is a Delaware corporation doing business in Nevada. For the Commerce Tax year July 1, 2025 to June 30, 2026 its Nevada gross revenue is $5,000,000. It claims $70,000 of deductions under NRS 363C.210 (returns and refunds plus pass-through revenue). Its category is publishing, software and data processing at 0.253% (NRS 363C.430). Commerce Tax: ($5,000,000 minus $70,000 minus $4,000,000) = $930,000 times 0.253% = $2,352.90, paid with Form EXC-F025 on August 14, 2026 (rounded to $2,353 on the return).

Sierra Cloud is a general-business MBT employer. Quarterly Nevada gross wages are $250,000 and the employer pays $40,000 per quarter of health insurance premiums, fully deductible (NRS 363B.115). Taxable wages are $210,000; the base above the $50,000 quarterly threshold is $160,000; MBT is 1.17% times $160,000 = $1,872.00 per quarter. The Commerce Tax credit is 50% of $2,353 = $1,176.50, claimed against the four quarters beginning with the quarter ended September 30, 2026: that quarter's payment drops to $695.50, and the remaining credit is used in the following quarters. Annual MBT after the credit: 4 times $1,872.00 minus $1,176.50 = $6,311.50.

```oa-check
name: Sierra Cloud, SaaS, CT plus general MBT with credit (2026)
inputs:
  nv_gross: 5000000
  ct_deductions: 70000
  ct_threshold: 4000000
  ct_rate: 0.00253
  wages_q: 250000
  health_q: 40000
  mbt_threshold: 50000
  mbt_rate: 0.0117
steps:
  - ct_base: nv_gross - ct_deductions - ct_threshold
  - commerce_tax: ct_base * ct_rate
  - ct_paid: round(commerce_tax)
  - credit_total: ct_paid * 0.5
  - taxable_wages_q: wages_q - health_q
  - mbt_base_q: max(taxable_wages_q - mbt_threshold, 0)
  - mbt_q: mbt_base_q * mbt_rate
  - first_q_payment: max(mbt_q - credit_total, 0)
  - annual_mbt_after_credit: mbt_q * 4 - credit_total
expected:
  commerce_tax: 2352.90
  ct_paid: 2353
  credit_total: 1176.50
  mbt_q: 1872.00
  first_q_payment: 695.50
  annual_mbt_after_credit: 6311.50
```

### Worked example 2: contractor below the Commerce Tax threshold, quarterly MBT threshold

Vegas Custom Builds LLC is a general contractor (construction) with Nevada gross revenue of $2,500,000 for the July 1 to June 30 year: below $4,000,000, so no Commerce Tax return is required (NRS 363C.200(2)). It is a general-business MBT employer. Quarterly Nevada gross wages and employer-paid health premiums:

| Quarter | Gross wages | Health premiums | Taxable wages | Base over $50,000 | MBT at 1.17% |
|---|---|---|---|---|---|
| Q1 | $40,000 | $4,000 | $36,000 | $0 (no tax; $14,000 of threshold unused, no carryover) | $0.00 |
| Q2 | $80,000 | $6,000 | $74,000 | $24,000 | $280.80 |
| Q3 | $90,000 | $6,000 | $84,000 | $34,000 | $397.80 |
| Q4 | $35,000 | $4,000 | $31,000 | $0 | $0.00 |

Annual MBT: $678.60. A return is still due for every quarter, including the zero quarters (MBT FAQs).

```oa-check
name: Vegas Custom Builds, quarterly MBT threshold (2026)
inputs:
  q1_wages: 40000
  q1_health: 4000
  q2_wages: 80000
  q2_health: 6000
  q3_wages: 90000
  q3_health: 6000
  q4_wages: 35000
  q4_health: 4000
  mbt_threshold: 50000
  mbt_rate: 0.0117
steps:
  - q1_taxable: q1_wages - q1_health
  - q1_mbt: max(q1_taxable - mbt_threshold, 0) * mbt_rate
  - q2_taxable: q2_wages - q2_health
  - q2_mbt: max(q2_taxable - mbt_threshold, 0) * mbt_rate
  - q3_taxable: q3_wages - q3_health
  - q3_mbt: max(q3_taxable - mbt_threshold, 0) * mbt_rate
  - q4_taxable: q4_wages - q4_health
  - q4_mbt: max(q4_taxable - mbt_threshold, 0) * mbt_rate
  - annual_mbt: q1_mbt + q2_mbt + q3_mbt + q4_mbt
expected:
  q1_mbt: 0
  q2_mbt: 280.80
  q3_mbt: 397.80
  q4_mbt: 0
  annual_mbt: 678.60
```

### Worked example 3: financial institution, 1.554% with no threshold

Silver State Mortgage Co. LLC is a financial institution under NRS 363A.050. Quarterly Nevada gross wages are $400,000 and the employer pays $60,000 per quarter of health premiums, fully deductible (NRS 363A.135). There is no $50,000 threshold: MBT is 1.554% times ($400,000 minus $60,000) = 1.554% times $340,000 = $5,283.60 per quarter, $21,134.40 per year, filed on TAX-F002.

If in a later year Silver State's Nevada gross revenue exceeds $4,000,000 and it pays, say, $5,000 of Commerce Tax (finance and insurance at 0.111%, NRS 363C.440), it may credit 50% of that, $2,500, against MBT in the four quarters following the Commerce Tax year, reducing that year's MBT from $21,134.40 to $18,634.40.

```oa-check
name: Silver State Mortgage, FI MBT with later CT credit (2026)
inputs:
  wages_q: 400000
  health_q: 60000
  fi_rate: 0.01554
  ct_paid: 5000
steps:
  - taxable_q: wages_q - health_q
  - mbt_q: taxable_q * fi_rate
  - annual_mbt: mbt_q * 4
  - credit_total: ct_paid * 0.5
  - annual_after_credit: annual_mbt - credit_total
expected:
  mbt_q: 5283.60
  annual_mbt: 21134.40
  credit_total: 2500
  annual_after_credit: 18634.40
```

## Ask the client first

- Which NAICS category does the client's Nevada revenue actually fall in, and what is the evidence? The category is fixed on the initial return and hard to change later (NRS 363C.200(3)).
- Is the client a financial institution under NRS 363A.050, including through the related-entity rule at 50% vote or value (NRS 363A.050(3)(e)), or a net-proceeds-of-minerals taxpayer swept into Chapter 363A (NRS 363A.030(1)(b))?
- Who employs the Nevada workers? The MBT follows the entity that pays Nevada wages and UI contributions.
- How is the health plan structured (insured, self-insured, Taft-Hartley trust)? The deduction covers the full amount the employer pays, but HSA contributions and employee-paid amounts do not qualify.
- Did the client pay Commerce Tax for the prior July-June year? If so, the 50% credit must be claimed in the four following quarters or it lapses (NRS 363B.110(4)).
- Is the client a new employer that may qualify for the 50% first-four-years MBT abatement (NRS 363B.120)?

## Sources

| Source | URL | Read on |
|---|---|---|
| NRS Chapter 363C (Commerce Tax), current revision | https://www.leg.state.nv.us/nrs/nrs-363c.html | 2026-10-31 |
| NRS Chapter 363B (MBT, general business), current revision | https://www.leg.state.nv.us/nrs/nrs-363b.html | 2026-10-31 |
| NRS Chapter 363A (MBT, financial institutions), current revision | https://www.leg.state.nv.us/nrs/nrs-363a.html | 2026-10-31 |
| NRS Chapter 360 (tax administration, including 360.203 rate reductions and 360.417 interest), current revision | https://www.leg.state.nv.us/nrs/nrs-360.html | 2026-11-03 |
| Nevada Department of Taxation, Modified Business Tax FAQs | https://tax.nv.gov/tax-types/modified-business-tax/mbt-faqs/ | 2026-10-31 |
| Nevada Department of Taxation, Commerce Tax page (2025-2026 filing due August 14, 2026; extension of time to file and pay) | https://tax.nv.gov/tax-types/commerce-tax/ | 2026-10-31 |
| Form EXC-F025, Commerce Tax Return, with instructions (due August 14; 0.75% monthly extension interest) | https://tax.nv.gov/wp-content/uploads/2025/07/EXC-F025-COM-Tax-Return-2.pdf | 2026-11-03 |
| Form TAX-F003, MBT Return General Business, with instructions (rate .0117; graduated penalties per NAC 360.395; interest per NRS 360.417) | https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf | 2026-11-03 |
| Form TAX-F002, MBT Return Financial Institution (rate .01554) | https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F002-MBT-Return-Financial-Institution.pdf | 2026-11-03 |
| Nevada Department of Taxation, Components of Sales Tax (2.00 + 2.60 + 0.50 + 1.75) | https://tax.nv.gov/wp-content/uploads/2024/01/Components-of-Sales-Tax.pdf | 2026-10-31 |
| Nevada Department of Taxation, Sales Tax and Use Tax (6.85% statewide; Clark 8.375%; Washoe 8.265%; interest 0.75% per month from July 1, 2011) | https://tax.nv.gov/tax-types/sales-tax-use-tax/ | 2026-10-31 |
| NRS Chapter 374 (local school support tax), current revision | https://www.leg.state.nv.us/nrs/nrs-374.html | 2026-10-31 |
| NRS Chapter 368A (live entertainment tax, 9%), current revision | https://www.leg.state.nv.us/nrs/nrs-368a.html | 2026-10-31 |
| NRS Chapter 463 (gaming, 3.5%-6.75% at 463.370), current revision | https://www.leg.state.nv.us/nrs/nrs-463.html | 2026-10-31 |
| NRS Chapter 680B (insurance premium tax, 3.5% at 680B.027), current revision | https://www.leg.state.nv.us/nrs/nrs-680b.html | 2026-10-31 |
| Nevada Constitution, Article 10, Section 1 (no tax on wages or personal income of natural persons) | https://www.leg.state.nv.us/constitution/constitution.html | 2026-10-31 |
| Nevada Constitution (full text copy) | https://www.leg.state.nv.us/const/nvconst.html | 2026-11-03 |
| Nevada DETR, Unemployment Insurance Contributions Newsletter, June 2025 (2025 taxable wage base $41,800) | https://detr.nv.gov/content/media/FINAL_Contributions_Newsletter_June_2025.pdf | 2026-11-03 |

Not yet confirmed: the litigation history behind the 2019-2023 rate changes (the review flagged that the old file inverted the Settelmeyer holding; no archived source in this pack states the holding, so the case is not discussed in the body); whether affiliated Commerce Tax groups may file a combined return and on what form (the Department's Commerce Tax FAQs page references consolidated filing and an MBT credit FAQ for affiliated groups, but those pages are not archived in this pack); whether a zero-dollar Commerce Tax return is ever required for entities at or below $4,000,000 (NRS 363C.200(2) says the Department shall not require one); the current MBT-Mining return form number; and the federal deductibility line references for the MBT and Commerce Tax on income tax returns.

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
