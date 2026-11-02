---
name: md-sales-tax
description: Use this skill whenever asked about Maryland sales and use tax. Trigger on phrases like "Maryland sales tax", "MD sales tax", "Maryland Comptroller", "digital advertising tax". ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-MD
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MD Sales Tax

## Who this applies to
Maryland retail sales and use tax on tangible personal property and certain digital goods sold to Maryland consumers.

## Rates, bands and thresholds

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Maryland |
| State rate | 6.00% (Comptroller KB: "Maryland's 6 percent sales and use tax"; 9% applies to alcoholic beverages and temporary event licenses) |
| Local taxes | See Not yet confirmed below |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Comptroller of Maryland |
| Skill version | 2.0 |

## The taxable base

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6% |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | TAXABLE | Maryland taxes SaaS and digital products |
| Canned software | TAXABLE |  |
| Digital goods | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| OTC drugs | EXEMPT |  |
| Resale | EXEMPT |  |
| Digital advertising (separate tax) | TAXABLE | Maryland Digital Advertising Gross Revenues Tax -- separate from sales tax |

## Deadlines and filing
Out-of-state vendors that hit the economic nexus criteria file on a monthly schedule by default; the Comptroller's office may adjust the filing schedule depending on the amount of taxable sales (Comptroller Tax Alert on Wayfair nexus).

## Penalties and interest
Interest on unpaid Maryland tax is set by calendar year: 10% for CY2021, 9.5% for CY2022, 9% for CY2023, 10.0075% for CY2024, and 11.4825% for CY2025, running from the date the return was originally due. Late-payment penalties can be up to 25 percent of the tax owed (Comptroller compliance FAQs).

## Cross-border points
Remote-sale economic nexus: an out-of-state vendor with no physical presence must register and collect when gross revenue from sales delivered into Maryland exceeds $100,000, or sales into Maryland reach 200 or more separate transactions, in the current or previous calendar year (Comptroller Tax Alert, COMAR 03.06.01.33).

## Worked examples

### Worked example 1: Baltimore retail sale
$1,000 sale in Baltimore City at the 6% state rate: 1000 * 0.06 = $60.00 tax.

## Ask the client first
Where is the buyer located? Is the item exempt? Are you registered for out-of-state nexus?

## Common mistakes

- **Prohibition on local taxes** -- NEVER add local taxes -- Maryland has none.  _(unsure)_
- **Prohibition on confusing Digital Advertising Tax with sales tax** -- NEVER confuse the Digital Advertising Tax with sales tax -- they are separate.  _(unsure)_
- **Prohibition on computing numbers** -- NEVER compute any number.  _(unsure)_

### Disclaimer

Informational only. Review by qualified professional required before filing.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Sources
| Source | URL | Read on |
| --- | --- | --- |
| Comptroller Knowledge Base - Sales and Use Tax guidance (6 percent rate; 9 percent alcohol/temporary events) | https://services.marylandcomptroller.gov/taxes/en/sales-and-use-tax?id=kb_article_view&sysparm_article=KB0010107 | 2026-11-01 |
| Comptroller Knowledge Base - Compliance FAQs (interest by calendar year, penalties up to 25%) | https://services.marylandcomptroller.gov/taxes/en/compliance-faqs?id=kb_article_view&sysparm_article=KB0010052 | 2026-11-01 |
| Comptroller Tax Alert - Wayfair nexus for out-of-state vendors ($100,000 / 200 transactions, monthly filing default) | https://www.marylandcomptroller.gov/legal-library/sut-ta-sep-01-2018.html | 2026-10-31 |

Not yet confirmed: whether Maryland bars local sales taxes outright (the "no local sales tax" and combined-rate claims), Streamlined Sales Tax membership, filing cadence for Maryland-based sellers, and SaaS/digital-goods taxability -- no archived source states these figures.

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at


> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
