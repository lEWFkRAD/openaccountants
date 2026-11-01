---
name: sd-sales-tax
description: "South Dakota sales and use tax for 2026: the 4.2% state rate (4.5% again from July 1, 2027 under SDCL 10-45-2), municipal sales and use tax of 1% to 2%, the 1% municipal gross receipts tax, the $100,000 remote-seller threshold under SDCL 10-64-2, return and payment due dates, late-filing penalty and interest under SDCL 10-59-6, and the separate 2% contractor's excise tax and 4.2% ag excise tax. Trigger on 'South Dakota sales tax', 'SD sales tax', 'SDCL 10-45', 'South Dakota DOR', 'Wayfair', 'South Dakota use tax', 'municipal gross receipts tax', 'South Dakota remote seller'. Load us-sales-tax first for federal context."
version: 0.3
jurisdiction: US-SD
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# South Dakota sales and use tax, 2026

> **Source-cited draft.** Built from South Dakota Codified Laws (SDCL) 10-45-2, 10-45-27.3, 10-52-2, 10-52A-2, 10-59-6 and 10-64-2 and the Department of Revenue Sales and Use Tax Guide and Municipal Tax Guide (both July 2026), read on 2026-11-01. No accountant has reviewed it. Do not file from it without review by a qualified professional.

South Dakota has no corporate, unitary or personal income tax (DOR Sales and Use Tax Guide, Tax Basics). The Department of Revenue (DOR, dor.sd.gov) administers the state sales and use tax and collects municipal sales, use and gross receipts taxes on the same return.

## Who this applies to

- **Retailers with a physical presence in South Dakota.** Any business with a physical presence must hold a sales tax license and collect; the remote-seller threshold does not apply to them (DOR sales and use tax page).
- **Remote sellers.** A seller with no physical presence must collect and remit if its gross revenue from tangible personal property, products transferred electronically, or services delivered into South Dakota exceeds $100,000 in the previous or current calendar year (SDCL 10-64-2). There is no transaction-count test: the old 200-transaction test is not in the current statute. A remote seller must register by the first day of the month that starts at least thirty days after the threshold is met (DOR guide, Remote Sellers).
- **Marketplace providers.** Since March 1, 2019, marketplace providers that meet the thresholds must license and remit tax on the sales they facilitate (DOR guide, Marketplace Providers).
- **Buyers owing use tax.** Use tax applies when state and municipal sales tax has not been paid on products and services used in South Dakota (DOR sales and use tax page).

## Rates, bands and thresholds

| Tax | Rate | Authority |
|---|---|---|
| State sales and use tax | 4.2% through June 30, 2027; 4.5% from July 1, 2027 | SDCL 10-45-2 (current text "four and two-tenths percent"; version effective July 1, 2027 "four and one-half percent"); DOR guide |
| Municipal sales and use tax | 1% to 2%, set by each municipality | DOR guide; SDCL 10-52-2 caps the rate at two percent |
| Municipal gross receipts tax (MGRT) | 1%, in addition to municipal sales tax | DOR guide; SDCL 10-52A-2 |
| Contractor's excise tax (prime contractors, construction and realty improvement) | 2% of gross receipts | DOR guide |
| Ag excise tax (farm machinery, attachment units, irrigation equipment used exclusively in agriculture) | 4.2%, state only, no municipal tax | DOR guide |
| Tourism tax (certain lodging, amusement services, certain vehicle rentals) | 1.5% | DOR guide |
| Remote-seller threshold | more than $100,000 gross revenue into South Dakota, previous or current calendar year | SDCL 10-64-2 |

Municipal rates used in the worked examples, from the DOR Municipal Tax Guide (July 2026): Sioux Falls 2.00% sales tax and 1.00% MGRT; Rapid City 2.00% and 1.00%; Pierre 2.00% and 1.00%. Look up any other location with the DOR rate lookup before computing.

The MGRT applies to alcoholic beverages, eating establishments, lodging accommodations, admissions to places of amusement, and athletic and cultural events (DOR guide).

## The taxable base

- The sales tax applies to the gross receipts of all retail sales, including the sale, lease or rental of personal property or any product transferred electronically, and the sale of services (DOR guide, Sales Tax). Services are taxable unless specifically exempt, so professional services such as legal and consulting work and software delivered electronically fall in the base.
- **Services the DOR guide lists as exempt:** health services, educational services, social services, agricultural services, forestry services, services of certain membership organizations, financial services of institutions under the bank franchise tax, insurance agent commissions, stock and commodity broker services, trucking, travel agent services, and construction services (taxed instead under the contractor's excise tax).
- **Food.** The DOR guide's exemption list has no general food exemption; food stamp (SNAP) purchases are not subject to sales tax.
- **Farm machinery** used exclusively in agriculture is not sales-taxed but bears the 4.2% ag excise tax, with no municipal tax (DOR guide).
- **Use tax** is at the same rate as sales tax, on the purchase price including freight and handling, due in the filing period in which the product or service is received, at the rate for the location where it is used (DOR guide, Use Tax). Credit is given for another state's tax legally paid.

## Deadlines and filing

- Returns and tax are due on or before the 20th day of the month following each monthly period (SDCL 10-45-27.3).
- Electronic filers file by the 20th and remit by the 25th of the month following the period (SDCL 10-45-27.3; DOR guide: "All electronic payments are due the 25th of the month").
- The secretary may assign a basis other than monthly; that return is still due the 20th of the month after the reporting period unless the secretary sets another date (SDCL 10-45-27.3).
- A return is required for every reporting period even with no business (DOR guide). If a due date falls on a weekend or legal holiday, the next business day is the due date.
- The secretary may grant an extension of not more than five days (SDCL 10-45-27.3).

## Penalties and interest

- **Late filing:** a return not filed within thirty days following the month it is due draws a penalty of 10% of the tax or $10, whichever is greater; the secretary may reduce or remove it for reasonable cause (SDCL 10-59-6). The DOR guide adds that the $10 minimum applies even if no tax is due.
- **Interest:** 1% or $5, whichever is greater, for the first month, and 1% per month thereafter; 1.5% (or $5) per month where the failure was intended to avoid or delay payment (SDCL 10-59-6).

## Cross-border points

- Sales tax applies where the customer receives the product or service (DOR guide). For products transferred electronically with no delivery or customer address on file, sales tax applies where the product is first available for transmission by the seller.
- Additional municipal use tax may be due if a product is used in a different city with a higher rate than was paid (DOR guide).
- Remote sellers can obtain licensing in several states through the Streamlined Sales Tax system (DOR guide).

## Worked examples

### Worked example 1: office supplies sold in Sioux Falls

A Sioux Falls retailer sells $500 of office supplies in October 2026. State 4.2% plus Sioux Falls municipal 2.00% = 6.2%. Tax is $500 × 6.2% = $31.00, total $531.00. The MGRT does not apply: office supplies are not on the MGRT list.

```oa-check
name: Sioux Falls retail sale, $500 (2026)
inputs:
  price: 500
  state_rate: 0.042
  city_rate: 0.02
steps:
  - combined_rate: state_rate + city_rate
  - tax: price * combined_rate
  - total: price + tax
expected:
  combined_rate: 0.062
  tax: 31.00
  total: 531.00
```

### Worked example 2: tractor bought for exclusive farm use

A farmer buys an $80,000 tractor for exclusive agricultural use. It is not sales-taxed, but the 4.2% ag excise tax applies, with no municipal tax: $80,000 × 4.2% = $3,360, total $83,360. If the dealer does not charge it, the farmer owes it.

```oa-check
name: Farm tractor, ag excise tax, $80,000 (2026)
inputs:
  price: 80000
  ag_excise_rate: 0.042
steps:
  - tax: price * ag_excise_rate
  - total: price + tax
expected:
  tax: 3360
  total: 83360
```

## Ask the client first

1. **Do you have a physical presence in South Dakota?** If not, did gross revenue into the state exceed $100,000 this year or last?
2. **Which municipalities do you deliver into?** Each sets its own 1% to 2% rate and may impose the 1% MGRT.
3. **Do you sell meals, alcohol, lodging, admissions or amusements?** Those carry the MGRT and possibly the tourism tax.
4. **Is any of the work construction or realty improvement?** That is under the 2% contractor's excise tax, not sales tax.
5. **Do you sell farm machinery or irrigation equipment?** The 4.2% ag excise tax applies instead of sales tax.
6. **Do you file electronically?** Payment is due the 25th, not the 20th.
7. **Will the sale or delivery happen on or after July 1, 2027?** The state rate returns to 4.5%.

## Sources

| Source | URL | Read on |
|---|---|---|
| SDCL 10-45-2, tax on sale of tangible property (current text and version effective July 1, 2027) | https://sdlegislature.gov/api/Statutes/10-45-2.html | 2026-11-01 |
| SDCL 10-45-27.3, filing return and remitting tax | https://sdlegislature.gov/Statutes/10-45-27.3 | 2026-11-01 |
| SDCL 10-52-2, municipal tax, conformance and rate | https://sdlegislature.gov/Statutes/10-52-2 | 2026-11-01 |
| SDCL 10-52A-2, municipal gross receipts tax | https://sdlegislature.gov/Statutes/10-52A-2 | 2026-11-01 |
| SDCL 10-59-6, penalty and interest | https://sdlegislature.gov/Statutes/10-59-6 | 2026-11-01 |
| SDCL 10-64-2, remote sellers | https://sdlegislature.gov/Statutes/10-64-2 | 2026-11-01 |
| SD DOR, Sales and Use Tax Guide (July 2026) | https://dor.sd.gov/media/avyep2sr/2026-7_sales-use-tax-guide.pdf | 2026-11-01 |
| SD DOR, Municipal Tax Guide (July 2026) | https://dor.sd.gov/media/54mb5a2w/2026-07_municipal-tax-guide.pdf | 2026-11-01 |
| SD DOR, Remote Seller Bulletin | https://dor.sd.gov/media/yh0n3oc2/remote-seller-bulletin.pdf | 2026-11-01 |
| SD DOR, sales and use tax page | https://dor.sd.gov/businesses/taxes/sales-use-tax/ | 2026-11-01 |

Not yet confirmed: which filing frequency (monthly, bi-monthly, semi-annual) DOR assigns at which liability level, since neither SDCL 10-45-27.3 nor the DOR guide gives dollar cut-offs; any civil fraud penalty percentage (SDCL 10-59-6 sets the 1.5% intentional-avoidance interest; a fixed fraud penalty was not found); the specific exemptions for prescription drugs, durable medical equipment and prosthetics (the DOR guide points to a separate Health Services, Drugs and Medical Devices tax fact not read today); the exemptions for feed, seed, fertilizer, livestock and agricultural chemicals (the DOR guide points to separate agriculture tax facts not read today); whether a vendor collection allowance exists; how the MGRT is shown to customers.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put their name behind the tax answers AI gives people.

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
