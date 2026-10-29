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
| State rate | 6.00% (flat -- no local sales tax) |
| Local taxes | None |
| Maximum combined rate | 6.00% |
| Sourcing | Destination-based |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Comptroller of Maryland |
| Portal | https://www.marylandtaxes.gov |
| SST member | No |
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
Monthly/quarterly returns per Comptroller assignment (cadence not yet confirmed — see Sources).

## Penalties and interest
10% annual interest on underpayments plus penalties (figures not yet confirmed — see Sources).

## Cross-border points
Remote-sale economic nexus; interstate sourcing under the Marketplace Fairness framework (thresholds not yet confirmed).

## Worked examples
Worked example (all hypothetical): $1,000 sale in Baltimore City at 6% = $60.

## Ask the client first
Where is the buyer located? Is the item exempt? Are you registered for out-of-state nexus?

## Common mistakes

- **Prohibition on local taxes** — NEVER add local taxes -- Maryland has none.  _(unsure)_
- **Prohibition on confusing Digital Advertising Tax with sales tax** — NEVER confuse the Digital Advertising Tax with sales tax -- they are separate.  _(unsure)_
- **Prohibition on computing numbers** — NEVER compute any number.  _(unsure)_

### Disclaimer

Informational only. Review by qualified professional required before filing.

### Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Sources
| Source | URL | Read on |
| --- | --- | --- |
| Comptroller sales tax page | https://tax.maryland.gov/ | 2026-10-28 |


Not yet confirmed: rate tables, nexus thresholds, penalty percentages — no machine-readable archive captured this run.

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
