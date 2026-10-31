---
name: fl-sales-tax
description: >
  Florida Sales and Use Tax (Form DR-15) for registered dealers who are
  sole proprietors or single-member LLCs, tax year 2025-26 returns: the 6%
  state sales and use tax rate, the county discretionary sales surtax
  capped at the first $5,000 per item, the collection allowance of 2.5% of
  the first $1,200 of tax due (maximum $30, electronic filers only),
  filing-frequency limits from $100 or less (annual) to more than $1,000
  (monthly), returns due the 1st and late after the 20th of the following
  month, the $5,000 prior-fiscal-year electronic filing threshold, and the
  repeal of sales tax on commercial rentals effective October 1, 2025.
  Primary sources: Florida Statutes Chapter 212 and Florida Department of
  Revenue forms DR-15, DR-15N and DR-15DSS. ALWAYS load us-tax-workflow-base
  first.
version: 0.2
jurisdiction: US-FL
category: state
tax_year: 2025
tier: 2
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - us-tax-workflow-base
---

# Florida Sales and Use Tax (DR-15), tax year 2025-26 returns

> **Source-cited draft.** Built from ss. 212.05, 212.06, 212.054, 212.07, 212.08, 212.12, 212.18, 213.235 and 213.755 Fla. Stat. (2026) and the Florida Department of Revenue's DR-15 return, DR-15N instructions, DR-15DSS surtax rates and sales tax page, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

Any person who makes or intends to make taxable sales or charges admission in Florida must register as a dealer with the Florida Department of Revenue (FDOR); registration is administered under s. 212.18, Fla. Stat. This skill covers the preparation of Form DR-15 (Sales and Use Tax Return) and Form DR-15EZ for Florida-registered dealers who are sole proprietors or single-member LLCs.

In scope: Form DR-15 and DR-15EZ; taxable sales of tangible personal property; the specifically enumerated taxable services; use tax on purchases where sales tax was not collected; the county discretionary sales surtax; the collection allowance; filing-frequency determination.

Out of scope (refused): Form DR-1 registration; the communications services tax; solid waste, lead-acid battery and tire fees; transient rental taxes (see `fl-transient-rental-tax`); marketplace provider obligations; multi-state nexus analysis (see `fl-cross-border`).

**Tax year coverage.** This skill targets returns for reporting periods in tax year 2025-26 (monthly, quarterly, semiannual or annual, per the dealer's assigned frequency).

## Rates, bands and thresholds

| Item | Rate / amount | Source |
|---|---|---|
| State sales tax | 6% of the sales price of each item of tangible personal property sold at retail | s. 212.05(1)(a)1.a.: "At the rate of 6 percent of the sales price of each item or article of tangible personal property" |
| State use tax | 6% of the cost price at the moment of purchase | s. 212.06(1)(a): "The aforesaid tax at the rate of 6 percent of the retail sales price as of the moment of sale, 6 percent of the cost price as of the moment of purchase" |
| County discretionary sales surtax | Levied by counties under s. 212.055; rates published annually on Form DR-15DSS | s. 212.054(2); FDOR sales tax page: "For a list of discretionary sales surtax rates, visit ... Form DR-15DSS ... updated yearly in November." |
| Surtax cap per item | Only the first $5,000 of the sales amount of any item of tangible personal property is subject to surtax | s. 212.054(4)(b)1.: "The sales amount above $5,000 on any item of tangible personal property shall not be subject to the surtax." |
| Collection allowance | 2.5% of the first $1,200 of the amount due, not to exceed $30; electronic filing and payment only; forfeited on late or incomplete returns | s. 212.12(1): "shall be allowed 2.5 percent of the amount of the tax due ... if the amount of the tax due ... exceeds $1,200, an allowance is not allowed for all amounts in excess of $1,200"; DR-15N instructions: "a collection allowance of 2.5% (.025) of the first $1,200 of the Amount Due (Line 10), not to exceed $30" |
| Electronic filing threshold | Dealers that paid $5,000 or more in state sales and use tax during the prior state fiscal year (July 1 - June 30) must file and pay electronically during the next calendar year | s. 213.755(1): "paid that tax in the prior state fiscal year in an amount greater than or equal to $5,000"; DR-15N: "taxpayers who paid $5,000 or more in sales and use tax during the State of Florida's prior fiscal year ... are required to file returns and pay tax electronically"; FDOR sales tax page |
| Registration | Any person who makes or intends to make taxable sales must register as a dealer | s. 212.18 (administration of law; registration of dealers) |

**Selected county surtax rates (calendar year 2025, Form DR-15DSS R. 11/24).** Surtax applies in the county where the goods are delivered or the service is performed; the dealer must look up the current rate on the current DR-15DSS for each county (rates change every January).

| County | Total surtax rate (CY2025) |
|---|---|
| Alachua | 1.5% |
| Broward | 1% |
| Duval | 1.5% |
| Hillsborough | 1.5% |
| Miami-Dade | 1% |
| Orange | 0.5% |
| Palm Beach | 1% |

## The taxable base

The DR-15 computation runs line by line: gross sales (line 1) less exempt sales (line 2) gives the taxable amount (line 3); state tax at 6% (line 4); discretionary surtax (line 15) computed county by county, applying the surtax only to the first $5,000 of the sales amount of each individual item delivered in that county; use tax (line 3B) on out-of-state or internet purchases where no Florida tax was collected, at 6% plus the applicable surtax; lawful deductions (line 6); minus the collection allowance (line 11, electronic filers only); plus penalty and interest if late (lines 12-13).

Items that assemble into one working unit count as a single item for the $5,000 surtax cap when documented. Charges for prepaid calling arrangements remain subject to surtax above $5,000 (s. 212.054(4)(b)1.).

**Common exemptions** (s. 212.08, Fla. Stat.): food products for human consumption are exempt -- "Food products for human consumption are exempt from the tax imposed by this chapter" (s. 212.08(1)(a)); also exempt are prescription eyeglasses, dentures, hearing aids, crutches, prosthetic and orthopedic appliances, and funeral purchases (s. 212.08(2)). Sales for resale must be in strict compliance with s. 212.18 and the rules adopted under it; a dealer who makes a sale for resale that is not in strict compliance is liable for the tax (s. 212.07(1)(b)), and the department provides each newly registered dealer an annual resale certificate (s. 212.18(2)(e)).

**Taxable services.** Most Florida services are not taxable; the specifically enumerated taxable services include nonresidential building pest control and nonresidential cleaning services, and detective, burglar protection and other protection services (s. 212.05(1)(d), Fla. Stat.).

**Commercial rentals repealed.** The sales tax on commercial real property rentals was repealed effective October 1, 2025; the DR-15N instructions (R. 10/25) state "Sales Tax on Commercial Rentals -- Repealed Effective October 1, 2025. See TIP 25A01-04."

**Zero returns.** A return must be filed for each reporting period even if no tax is due (DR-15N: "You must file a tax return for each reporting period, even if no tax is due."; FDOR sales tax page).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Return and payment | Due on the 1st and late after the 20th of the month following each reporting period; if the 20th falls on a Saturday, Sunday or state/federal holiday, the due date is the next business day | DR-15N instructions: "Tax returns and payments are due on the 1st and late after the 20th day of the month following each reporting period." |
| Filing frequency limits | More than $1,000 in annual sales tax collections: monthly. $501 - $1,000: quarterly. $101 - $500: semiannual. $100 or less: annual. Most new businesses are set up to file quarterly | FDOR sales tax page filing-frequency limits table |
| Electronic payment initiation | To avoid penalty and interest, electronic payments must be initiated and confirmed no later than 5 p.m. ET on the business day prior to the 20th | DR-15N instructions |
| Estimated tax | Dealers that paid $200,000 or more in state sales and use tax during the prior fiscal year must make monthly estimated payments (60% methods) starting with the December return | DR-15N instructions lines 8-9 |

## Penalties and interest

| Failure | Penalty / interest | Source |
|---|---|---|
| Failure to timely file or pay | 10% of the tax not timely filed or paid, with a minimum of $50 | s. 212.12(2)(a): "a specific penalty shall be added to the tax or fee in the amount of 10 percent of either the tax or fee shown on the return that is not timely filed or any tax or fee not paid timely. The penalty may not be less than $50" |
| Continued nonpayment | An additional 10% of the unpaid tax or fee for each additional 30 days or fraction thereof, up to a total penalty of 50% | s. 212.12(2)(c) |
| Fraudulent return with willful intent to evade | 100% of the unreported tax | s. 212.12(2)(d) |
| Interest | Floating rate on deficiencies; the annual rate is the adjusted prime rate rounded to the nearest full percent plus 4 percentage points, set under Ch. 213 | s. 213.235(1)-(2) |
| Underpayment of estimated tax | Loss of collection allowance and a 10% penalty on the underpayment, plus interest | DR-15N instructions |

The collection allowance is denied on late or incomplete returns (s. 212.12(1)(b); DR-15N).

## Cross-border points

- Out-of-state retailers with no physical presence in Florida must register and collect once taxable remote sales exceed $100,000 in the previous calendar year (FDOR sales tax page, consumer information).
- Use tax on remote purchases is due the first day of the month following the quarter of purchase and late after the 20th (FDOR consumer page quarterly schedule).
- Registered Florida dealers report use tax on their DR-15 returns; out-of-state individuals use Form DR-15MO (FDOR sales tax page).

## Worked examples

```oa-check
name: FL monthly dealer 100000 taxable sales at 6 plus 1.5 surtax with collection allowance
inputs:
  sales: 100000
  state: 0.06
  surtax: 0.015
steps:
  - state_tax: sales * state
  - surtax_tax: sales * surtax
  - gross: state_tax + surtax_tax
  - allowance: min(gross * 0.025, 30)
  - net: gross - allowance
expected:
  state_tax: 6000.00
  surtax_tax: 1500.00
  gross: 7500.00
  allowance: 30.00
  net: 7470.00
```

```oa-check
name: FL single item over the surtax cap
inputs:
  price: 10000
  state: 0.06
  surtax: 0.015
  cap: 5000
steps:
  - state_tax: price * state
  - surtax_tax: min(price, cap) * surtax
  - gross: state_tax + surtax_tax
expected:
  state_tax: 600.00
  surtax_tax: 75.00
  gross: 675.00
```
## Ask the client first

- Is the dealer registered with FDOR (registration is administered under s. 212.18)? Any location or mailing-address changes on the account?
- What is the assigned filing frequency (more than $1,000 annual collections = monthly; $501-$1,000 = quarterly; $101-$500 = semiannual; $100 or less = annual), and does the total tax paid last fiscal year exceed $5,000 (mandatory e-file)?
- Which county surtax rates apply to each delivery location this year (check the current DR-15DSS -- rates change every January)?
- Are all resale certificates (annual resale certificate under s. 212.18(2)(e)) collected and verified as strictly compliant with s. 212.18 before exemption is honored?
- Is use tax being reported on out-of-state and internet purchases where no Florida tax was collected?
- Was the return filed for every reporting period, including zero-tax periods?
- Do not accept an exemption without a properly completed certificate; do not apply surtax above the first $5,000 per item; do not claim the collection allowance on a late return; do not assume commercial rentals are still taxable -- the tax was repealed effective October 1, 2025.

## Sources

| Source | URL | Read on |
|---|---|---|
| s. 212.05 Fla. Stat. (2026) -- sales tax rate; taxable services | https://www.flsenate.gov/Laws/Statutes/2026/212.05 | 2026-10-28 |
| s. 212.06 Fla. Stat. (2026) -- use tax; dealers must collect | https://www.flsenate.gov/Laws/Statutes/2026/212.06 | 2026-10-28 |
| s. 212.054 Fla. Stat. (2026) -- discretionary sales surtax; $5,000 per-item cap | https://www.flsenate.gov/Laws/Statutes/2026/212.054 | 2026-10-28 |
| s. 212.07 Fla. Stat. (2026) -- resale in strict compliance with s. 212.18 | https://www.flsenate.gov/Laws/Statutes/2026/212.07 | 2026-10-28 |
| s. 212.08 Fla. Stat. (2026) -- exemptions (food products; medical; funeral) | https://www.flsenate.gov/Laws/Statutes/2026/212.08 | 2026-10-28 |
| s. 212.12 Fla. Stat. (2026) -- collection allowance; delinquency penalties (10%, $50 minimum, 50% cap, 100% fraud) | https://www.flsenate.gov/Laws/Statutes/2026/212.12 | 2026-10-28 |
| s. 212.18 Fla. Stat. (2026) -- registration of dealers; annual resale certificate | https://www.flsenate.gov/Laws/Statutes/2026/212.18 | 2026-10-28 |
| s. 213.235 Fla. Stat. (2026) -- interest on deficiencies (floating rate) | https://www.flsenate.gov/Laws/Statutes/2026/213.235 | 2026-10-28 |
| s. 213.755 Fla. Stat. (2026) -- electronic filing and payment ($5,000 prior-year threshold) | https://www.flsenate.gov/Laws/Statutes/2026/213.755 | 2026-10-28 |
| Florida Department of Revenue -- Sales and Use Tax page (filing frequencies, due dates, e-file threshold, remote-seller registration) | https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx | 2026-10-28 |
| Form DR-15, Sales and Use Tax Return (PDF, R. 01/25, effective 02/25) | https://floridarevenue.com/Forms_library/current/dr15.pdf | 2026-10-28 |
| Instructions for DR-15 (Form DR-15N, R. 10/25) -- due dates, collection allowance, e-file threshold, estimated tax, commercial rentals repealed effective October 1, 2025 | https://floridarevenue.com/Forms_library/current/dr15n.pdf | 2026-10-28 |
| Form DR-15DSS, Discretionary Sales Surtax Information for Calendar Year 2025 (R. 11/24) | https://floridarevenue.com/Forms_library/current/dr15dss.pdf | 2026-10-28 |

Not yet confirmed: the calendar year 2026 county surtax rates (the archived DR-15DSS covers CY2025; the 2026 form publishes in November); the current bracket chart for tax on partial dollars under s. 212.12(9) (the bracket table itself was not archived this run); the taxability of canned software delivered electronically and digital goods (the prior draft's treatment relied on unarchived DOR guidance; confirm against current DOR publications before relying on it); the current interest rate percentage for late payments (the floating-rate formula is confirmed in s. 213.235 but the current year's published rate was not archived this run).

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
