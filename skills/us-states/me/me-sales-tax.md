---
name: me-sales-tax
description: Use this skill whenever asked about Maine sales and use tax. Trigger on phrases like "Maine sales tax", "ME sales tax", "MRS", "36 M.R.S. §1811". ALWAYS load us-sales-tax first.
version: "2.1"
jurisdiction: US-ME
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# ME Sales Tax

## Who this applies to

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Maine |
| State rate | 5.50% (general); 8.00% (prepared food; also liquor in licensed establishments); 9.00% (lodging); 10.00% (short-term auto rental); 10% cannabis retail before 2026, 14% from Jan 1 2026 — all per [36 M.R.S. §1811, archived 2026-10-28](https://legislature.maine.gov/statutes/36/title36sec1811.html): "the rate of tax is 5.5% … except the rate of tax is: (1) Eight percent on the value of prepared food; … (3) Nine percent on the value of rental of living quarters …; (4) Ten percent on the value of rental for a period of less than one year of: (a) An automobile …; (5) Before January 1, 2026, 10% on the value of adult use cannabis … For sales occurring on or after January 1, 2026, the applicable rate of tax under this subparagraph is 14%" |
| Local taxes | None |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions (not yet confirmed — the archived § 5211 text covers apportionment factors; the threshold wording was not line-cited) |
| Tax authority | Maine Revenue Services (MRS) |
| Portal | https://www.maine.gov/revenue |
| SST member | No |
| Skill version | 2.0 |

## Rates, bands and thresholds

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 5.50% |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE 8.00% | Higher rate |
| Lodging | TAXABLE 9.00% | Higher rate |
| Short-term auto rental | TAXABLE 10.00% |  |
| SaaS | NOT TAXABLE | Maine does not tax SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## The taxable base

Retail sales of tangible personal property and enumerated services in Maine, plus use tax on out-of-state purchases used in Maine at the same rates. Taxable sales include prepared food and lodging at their elevated rates; exemptions (e.g., most clothing) follow 36 M.R.S. § 1811 and related exemption provisions.

## Deadlines and filing

Registered sellers file periodic Maine sales/use returns; the MRS rates-and-due-dates page (read 2026-10-29) publishes the due-date table — "Monthly/Seasonal Returns Due … Quarterly Returns Due … Semi-Annual Returns Due … Annual Returns Due" keyed to the month activity occurred, with returns generally due "no later than the 15th of the month" following.

## Penalties and interest

Late-filing and late-payment penalties and interest apply under Maine law; specific percentages not yet confirmed line-by-line.

## Cross-border points

- Out-of-state sellers meeting the economic-nexus threshold must register and collect Maine sales tax (threshold wording not yet confirmed line-by-line — see Rates section).
- Maine is not a member of the Streamlined Sales Tax Agreement; SST-simplified sourcing for remote sellers follows the destination-based framework in the archived statute (not yet confirmed line-by-line).
- Use tax applies at the same rates to taxable purchases brought into Maine from out of state.

## Worked examples

**Worked example 1 — prepared food sale (hypothetical).** A $40 prepared-food sale in Maine:

```oa-check
name: ME prepared food tax
inputs:
  price: 40
  rate: 0.08
steps:
  - tax: price * rate
expected:
  tax: 3.20
```

**Worked example 2 — lodging night (hypothetical).** A $150 lodging night (2026 rate):

```oa-check
name: ME lodging tax 2026
inputs:
  price: 150
  rate: 0.09
steps:
  - tax: price * rate
expected:
  tax: 13.50
```

## Ask the client first

- **Prohibition on using 5.50% for prepared food or lodging** — NEVER use the 5.50% rate for prepared food or lodging -- they have higher rates (8% prepared food, 9% lodging).  _(Prohibitions)_
- **Prohibition on forgetting short-term auto rental rate** — NEVER forget the 10% short-term auto rental rate.  _(Prohibitions)_
- **Prohibition on computing numbers** — NEVER compute any number.  _(Prohibitions)_

<!-- openaccountants-cta-block -->

---

## Sources

| Source | URL | Read on |
|---|---|---|
| 36 M.R.S. § 1811 (sales and use tax rates) | https://legislature.maine.gov/statutes/36/title36sec1811.html | 2026-10-28 |
| 36 M.R.S. § 5211 (economic nexus thresholds) | https://legislature.maine.gov/statutes/36/title36sec5211.html | 2026-10-28 |
| MRS Sales Tax Rates page | https://www.maine.gov/revenue/taxes/sales-use-service-provider-tax/rates-due-dates | 2026-10-29 |

Not yet confirmed: whether the Quick-reference SST-membership and sourcing rows match a current MRS page verbatim (they follow the archived statute framework); cannabis market-facility fee interactions with the 14% rate; late-filing/late-payment penalty percentages.

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
