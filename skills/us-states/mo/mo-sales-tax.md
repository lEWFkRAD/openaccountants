---
name: mo-sales-tax
description: Use this skill whenever asked about Missouri sales and use tax. Trigger on phrases like "Missouri sales tax", "MO sales tax", "RSMo 144", "MyTax Missouri". NOTE -- Missouri was the LAST state to enact economic nexus (Jan 1, 2023). ALWAYS load us-sales-tax first.
version: 2.1
jurisdiction: US-MO
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MO Sales Tax

## Who this applies to

**Section 1 -- Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Missouri |
| State rate | 4.225% |
| Local rate range | 0% -- ~6.5% (county + city + special district) |
| Maximum combined rate | Not yet confirmed |
| Sourcing | Origin-based (intrastate); destination for remote sellers |
| Economic nexus | $100,000 in taxable sales (last state to enact -- Jan 1, 2023) |
| Tax authority | Missouri Department of Revenue (MODOR) |
| Portal | https://mytax.mo.gov |
| SST member | No |
| Skill version | 2.0 |

## Rates, bands and thresholds
Rate figures are in the quick-reference table under "Who this applies to" above; no separate rates section.
## The taxable base

**Section 3 -- Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE 4.225% + local |  |
| Clothing | TAXABLE | No exemption |
| Grocery food | TAXABLE at a reduced state rate (not yet confirmed) | Plus local |
| Prepared food | TAXABLE at full rate |  |
| SaaS | NOT TAXABLE | Missouri does not tax SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT |  |
| Prescription drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## Deadlines and filing
Filing cadence and due dates are not yet confirmed — see the Not-yet-confirmed line under Sources.
## Penalties and interest
Penalty and interest rules are not yet confirmed — see the Not-yet-confirmed line under Sources.
## Cross-border points
No Missouri-specific cross-border sales-tax points are confirmed in this skill yet.
## Worked examples
No worked examples — this skill states figures only and never computes.
## Ask the client first

- **Grocery food exemption prohibition** — NEVER say grocery food is exempt -- Missouri taxes it at a reduced state rate plus full local.  _(Section 10 -- Prohibitions)_
- **SaaS taxability prohibition** — NEVER treat SaaS as taxable in Missouri.  _(Section 10 -- Prohibitions)_
- **Economic nexus history prohibition** — NEVER forget Missouri was the last state to enact economic nexus (2023).  _(Section 10 -- Prohibitions)_
- **No computation prohibition** — NEVER compute any number.  _(Section 10 -- Prohibitions)_

## Sources

| # | Source | URL | Read on |
| --- | --- | --- | --- |
| 1 | Missouri DOR taxation index | https://dor.mo.gov/taxation/ | 2026-10-28 |
| 2 | RSMo §144.010 (imposition of sales tax) | https://revisor.mo.gov/main/OneSection.aspx?section=144.010 | 2026-10-29 |
| 3 | RSMo §144.020 (definitions) | https://revisor.mo.gov/main/OneSection.aspx?section=144.020 | 2026-10-29 |
| 4 | RSMo §144.030 (sales tax rate) | https://revisor.mo.gov/main/OneSection.aspx?section=144.030 | 2026-10-29 |
| 5 | RSMo §144.034 (grocery food reduced rate) | https://revisor.mo.gov/main/OneSection.aspx?section=144.034 | 2026-10-29 |
| 6 | MyTax Missouri portal | https://mytax.mo.gov | 2026-10-28 |
Not yet confirmed: the figures above (state rate, local range, maximum combined rate, grocery rate, nexus threshold) — the sources were archived on the dates shown, but the archive fetches did not return usable text, so the figures stay unconfirmed until readable primary text is archived.


### Disclaimer


Informational only. Review by qualified professional required before filing.


### Disclaimer


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
