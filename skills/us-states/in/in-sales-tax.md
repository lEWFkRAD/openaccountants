---
name: in-sales-tax
description: Use this skill whenever asked about Indiana sales and use tax. Trigger on phrases like "Indiana sales tax", "IN sales tax", "IC 6-2.5", "Indiana DOR". Indiana has one of the SIMPLEST structures -- a flat statewide rate with no local sales taxes (the rate figure is not yet confirmed). ALWAYS load us-sales-tax first.
version: 2.1
jurisdiction: US-IN
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IN Sales Tax

## Who this applies to

**Quick reference**

| Field | Value |
| --- | --- |
| Jurisdiction | Indiana |
| State rate | 7.00% (flat -- no local sales tax) | (not yet confirmed)
| Local taxes | None |
| Maximum combined rate | 7.00% | (not yet confirmed)
| Sourcing | Destination-based (SST) |
| Economic nexus | $100,000 OR 200 transactions | (not yet confirmed)
| Tax authority | Indiana Department of Revenue |
| Portal | https://intime.dor.in.gov |
| SST member | Yes (full member) |
| Skill version | 2.0 |

**One of the simplest sales tax states -- a flat statewide rate (not yet confirmed), no local add-ons.**

## Rates, bands and thresholds

**Transaction pattern library**

| Pattern | Taxable? | Notes |
| --- | --- | --- |
| General TPP | TAXABLE (rate not yet confirmed) | Uniform statewide |
| Clothing | TAXABLE | No exemption |
| Grocery food | EXEMPT |  |
| Prepared food | TAXABLE |  |
| SaaS | NOT TAXABLE | Indiana does not tax SaaS |
| Canned software (download) | TAXABLE |  |
| Professional services | NOT TAXABLE |  |
| Manufacturing equipment | EXEMPT | IC 6-2.5-5-3 |
| Prescription drugs | EXEMPT |  |
| OTC drugs | EXEMPT |  |
| Resale | EXEMPT |  |

## The taxable base

Indiana sales tax applies to retail transactions of tangible personal property and specified services; the transaction pattern library above lists what is taxable, exempt, or not taxed.

## Deadlines and filing

Returns are filed through the INTIME portal (intime.dor.in.gov); filing frequencies and due dates follow the taxpayer's assigned filer status.

## Penalties and interest

Late filing and late payment penalties and interest are assessed by the Indiana Department of Revenue under IC 6-8.1.

## Cross-border points

Indiana is a full Streamlined Sales Tax (SST) member and sources sales by destination; economic nexus thresholds are listed in the quick reference above.

## Worked examples

No worked examples are included in this quick-reference skill; the 7.00% flat statewide rate applies uniformly. (not yet confirmed)

## Ask the client first

- **Never add local tax** — NEVER add local tax -- Indiana has no local sales taxes.
- **Never treat SaaS as taxable** — NEVER treat SaaS as taxable in Indiana.
- **Never compute any number** — NEVER compute any number.

## Sources

| Source | URL | Read on |
|---|---|---|
| Indiana Code IC 6-2.5 (sales and use tax; iga.in.gov SPA — no server-side text captured) | https://iga.in.gov/laws/2025/ic/titles/6#6-25 | 2026-10-28 |

Not yet confirmed: the 7.00% flat rate, the SST member-state status, the $100,000 / 200-transaction economic-nexus threshold, and the transaction-pattern exemptions (IC 6-2.5) — no archived copy of the IC 6-2.5 text or the DOR sales-tax pages was captured this run.

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

## Disclaimer

Informational only. Review by qualified professional required before filing.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained by the OpenAccountants network; log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---
