---
name: la-sales-tax
description: Use this skill whenever asked about Louisiana sales and use tax. Trigger on phrases like "Louisiana sales tax", "LA sales tax", "R.S. 47:301", "parish sales tax", "Sales Tax Commission". State general rate is 5% from 2025-01-01 (was 4.45% through 2024-12-31) plus parish/city taxes. ALWAYS load us-sales-tax first.
version: 2.1
jurisdiction: US-LA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# LA Sales Tax

## Who this applies to

- **Dealers**: any seller or lessor who leases, rents or sells tangible personal property or digital products in Louisiana, furnishes taxable services, holds property for resale, maintains a business location, operates through full-time nonresident salesmen or agents, keeps in-state inventory for lease/rental/delivery, or otherwise meets the dealer definition at R.S. 47:301(4) — must register, collect, and file with LDR (LDR General Sales & Use Tax page, verified 2026-10-29).
- **Remote/out-of-state sellers**: collect Louisiana tax when in-state activity triggers the dealer definition; the Louisiana Sales Tax Commission is the central compliance portal (portal role unverified this run).
- **Consumers**: owe consumer use tax on untaxed out-of-state purchases (R.S. 47:302(K)).

## Rates, bands and thresholds

| Field | Value |
| --- | --- |
| State general rate | **5%** for sales on or after January 1, 2025 (was 4.45% through December 31, 2024) — LDR General Sales & Use Tax page and Sales Tax Reform FAQ, verified 2026-10-29 |
| Telecommunications | 5% (intrastate and interstate; was 3.45%/2.45% pre-2025); cable/satellite/video carry an additional 5% state rate (verified, same pages) |
| Business utilities | 2% (boiler fuel 5%) (verified, LDR FAQ) |
| Direct marketers | 9% from 2025 (was 8.45%) (verified, Sales Tax Reform FAQ) |
| Consumer use tax | 8.45% in lieu of actual local rate (verified, LDR Consumer Use Tax page) |
| Local (parish/city) rates | in addition to state; Louisiana remains among the highest combined-rate states — exact range and maximum unverified this run |
| SST member | No |

## The taxable base

- The state general sales tax is due on the **sales price** [R.S. 47:301(13)] and use tax on the **cost price** [R.S. 47:301(3)]; the base includes the total amount for which TPP or digital products are sold, including services rendered by the seller in connection with the sale, and the gross amount charged for lease/rental (verified quote, LDR page 2026-10-29).
- Taxable categories per the LDR page: tangible personal property; telecommunication services; **prewritten computer software access services**; information services; cable/DTH satellite/video programming/satellite radio (verified). The pre-existing "SaaS not taxable" line is superseded for access services — see Not yet confirmed.

## Deadlines and filing

- Sales tax returns and payments are due **on or before the 20th of the month following the close of the calendar month or calendar quarter** of the reporting period (verified quote, LDR page 2026-10-29).
- Parish self-administration: local compliance can be separate from state filing (structural; parish list unverified this run).

## Penalties and interest

- Standard R.S. 47:305 late-filing/late-payment regime — percentages unverified this run.

## Cross-border points

- Destination-based sourcing (pre-existing; unverified this run).
- Economic nexus threshold ($100,000 sales or 200 transactions) — unverified this run; the LDR page frames remote collection through the dealer definition.

## Worked examples

**Example 1 — state rate change across the 2025 boundary:** a construction contract priced on the pre-2025 4.45% state rate; a $10,000 sale on January 1, 2025 carries the 5% state rate instead.

```oa-check
name: LA state rate 2024 vs 2025
inputs:
  price: 10000
  rate_2024: 0.0445
  rate_2025: 0.05
steps:
  - tax_2024: price * rate_2024
  - tax_2025: price * rate_2025
  - delta: tax_2025 - tax_2024
expected:
  tax_2024: 445
  tax_2025: 500
  delta: 55
```

Rates verified on the LDR Sales Tax Reform FAQ (4.45% through 2024-12-31; 5% from 2025-01-01).

**Example 2 — consumer use tax in lieu of local:** an untaxed out-of-state purchase of $2,000 owes the flat 8.45% consumer use tax regardless of the actual local combined rate (verified rate, LDR Consumer Use Tax page).

```oa-check
name: LA consumer use tax
inputs:
  price: 2000
  use_rate: 0.0845
steps:
  - use_tax: price * use_rate
expected:
  use_tax: 169
```

## Ask the client first

1. **Sale date vs contract date** — the 4.45%→5% switch on 2025-01-01 changes quotes and construction contracts.
2. **Which parishes/municipalities** the business operates in — local rates and self-administration vary.
3. **Whether the product is TPP, a digital product, an access service, or a service** — the taxable-category list on the LDR page drives collection.
4. **Remote-seller footprint** — dealer-definition activity, not just sales volume, drives the collection duty.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| LDR General Sales & Use Tax (rate 5%, who must file, base, 20th-of-month due date) | https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax/ | 2026-10-29 |
| LDR FAQ — What is the sales tax rate in Louisiana? (5.00% from 2025; local taxes in addition) | https://revenue.louisiana.gov/tax-education-and-faqs/faqs/sales-tax/what-is-the-sales-tax-rate-in-louisiana | 2026-10-29 |
| LDR FAQ — What is the state sales tax rate? (4.45% through 2024-12-31 vs 5% from 2025-01-01; telecom/direct-marketer rates) | https://revenue.louisiana.gov/tax-education-and-faqs/faqs/sales-tax-reform/what-is-the-state-sales-tax-rate/ | 2026-10-29 |
| LDR Consumer Use Tax (8.45% in lieu of local) | https://revenue.louisiana.gov/individuals/general-resources/consumer-use-tax/ | 2026-10-28 |

Not yet confirmed: the parish/city rate range and maximum combined rate (the pre-existing ~11.45% figure was not re-verified); destination-based sourcing; the economic-nexus threshold ($100,000/200 transactions); the clothing, grocery-food, prepared-food, professional-services, manufacturing-equipment, prescription-drug and resale exemption lines; whether SaaS is taxable beyond "prewritten computer software access services"; the Louisiana Sales Tax Commission portal role; penalty/interest percentages under R.S. 47:305.

The LDR Sales Tax page (https://revenue.louisiana.gov/businesses/widely-used-tax-types/sales-tax/) should be fetched and text-verified in the next run before these figures are relied on for filing.

## Section 10 -- Prohibitions

- **Parish self-administration** — NEVER ignore parish-level self-administration -- local compliance is separate from state.
- **Highest combined rates** — NEVER forget Louisiana has among the highest combined rates in the US.
- **SaaS taxability** — NEVER treat SaaS as clearly taxable in Louisiana.
- **No computation** — NEVER compute any number.

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
