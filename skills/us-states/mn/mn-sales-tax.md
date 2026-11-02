---
name: mn-sales-tax
description: Use this skill whenever asked about Minnesota sales and use tax. Trigger on phrases like "Minnesota sales tax", "MN sales tax", "M.S. 297A", "Minnesota DOR". NOTE -- Minnesota EXEMPTS clothing. ALWAYS load us-sales-tax first.
version: 2.2
jurisdiction: US-MN
tax_year: 2025
last_updated: 2026-11-02
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MN Sales Tax

## Who this applies to

Sellers with Minnesota nexus -- a physical presence or economic nexus ($100,000 in sales or 200 separate transactions) -- charging Minnesota sales and use tax.

## Rates, bands and thresholds


**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Minnesota |
| State rate | 6.875% |
| Local rate range | 0% -- stacked local taxes reach their highest level in St. Paul: 1.00% city + 1.50% county + 0.50% transit (DOR Local Sales and Use Tax Rate Guide, effective 2025-10-01 to 2025-12-31, read 2026-11-01) |
| Maximum combined rate | 9.875% (St. Paul; DOR Local Sales and Use Tax Rate Guide, effective 2025-10-01 to 2025-12-31, read 2026-11-01) |
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions |
| Tax authority | Minnesota Department of Revenue (MNDOR) |
| SST member | Yes (full member) |
| Clothing exemption | Yes -- ALL clothing exempt |
| Skill version | 2.0 |

## The taxable base


**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 6.875% + local |  |
| Clothing and footwear | EXEMPT | Minnesota exempts ALL clothing |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE |  |
| Canned software (download) | TAXABLE |  |
| Digital goods | TAXABLE | Specified digital products |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT | Capital equipment refund program |
| Prescription drugs | EXEMPT |  |
| OTC drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Deadlines and filing

Periodic sales and use tax returns are filed through the Minnesota Revenue e-Services portal on the assigned monthly, quarterly, or annual filing frequency.

## Penalties and interest

Late-file, late-pay and accuracy penalties plus statutory interest apply to underpaid sales and use tax (M.S. 289A.60 civil penalties, statute text archived 2026-11-02; interest under M.S. 289A.55 per the chapter 289A table of contents archived 2026-10-31).

## Cross-border points

Minnesota is a full Streamlined Sales Tax (SST) member and sources sales by destination; remote and interstate sellers follow the SST simplifications.

## Worked examples

No worked examples yet -- this skill's standing rule is to state rates and taxability, never to compute.

## Ask the client first


- **Clothing taxability prohibition** -- NEVER treat clothing as taxable in Minnesota -- ALL clothing is exempt.
- **SaaS taxability prohibition** -- NEVER treat SaaS as taxable.
- **No computation prohibition** -- NEVER compute any number.

## Sources

| Source | Read on |
| --- | --- |
| M.S. 297A.02 (tax base, rates, clothing exemption): <https://www.revisor.mn.gov/statutes/cite/297A.02> -- statute text archived | 2026-10-28 |
| M.S. 297A.03 (use tax): <https://www.revisor.mn.gov/statutes/cite/297A.03> -- statute text archived | 2026-10-28 |
| M.S. 289A.60 (civil penalties): <https://www.revisor.mn.gov/statutes/cite/289A.60> -- statute text archived | 2026-11-02 |
| DOR Local Sales and Use Tax Rate Guide (Q4 2025): <https://www.revenue.state.mn.us/sites/default/files/2025-09/local-sales-and-use-tax-rate-guide-2025-q4.pdf> | 2026-11-01 |
| DOR Local Sales and Use Taxes page: <https://www.revenue.state.mn.us/book/export/html/18421> | 2026-11-01 |

Not yet confirmed: the $100,000 / 200-transaction economic-nexus thresholds (DOR remote-sellers page not yet archived).
## Disclaimer


Informational only. Review by qualified professional required before filing.

## Disclaimer


This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

## Talk to a verified accountant


This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at


> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
