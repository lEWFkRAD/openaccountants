---
name: ia-sales-tax
description: "Use this skill whenever asked about Iowa sales and use tax. Trigger on phrases like \"Iowa sales tax\", \"IA sales tax\", \"IDR\", \"Iowa Code chapter 423\", \"Iowa LOST\", \"Iowa remote seller\". ALWAYS load us-sales-tax first."
jurisdiction: US-IA
tax_year: 2026
last_updated: 2026-10-28
version: 0.3
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Iowa sales and use tax, tax year 2026

> **Source-cited draft.** Built from Iowa Code §§423.2, 423.14A and 423.14 and Iowa Administrative Code rule 701-107.2 (Iowa Legislature), read on 2026-10-28. No accountant has reviewed it. Do not file, pay, amend, or take a tax position from it without review by a qualified Iowa professional.

Authority: Iowa Department of Revenue. Currency: US dollars. Covers the state sales and use tax, the local option sales and service tax (LOST), and remote-seller nexus. ALWAYS load `us-sales-tax` first.

## Who this applies to

- Retailers selling tangible personal property, specified digital products, or enumerated services at retail in Iowa (§423.2).
- Out-of-state remote sellers and marketplace facilitators: "A retailer that has gross revenue from Iowa sales equal to or exceeding one hundred thousand dollars for an immediately preceding calendar year or a current calendar year" is subject to Iowa collection duties (§423.14A(3)(a)).
- Use tax: persons using tangible personal property or specified digital products in Iowa on which Iowa sales tax was not paid (§423.14(2)).

## Rates, bands and thresholds

| Item | Value | Source |
|---|---|---|
| State rate | 6% | §423.2(1) |
| Local option sales and service tax (LOST) | not more than 1% where adopted by county voters | IAC 701-107.2; ch. 422B |
| Economic nexus threshold | $100,000 gross revenue from Iowa sales (current or immediately preceding calendar year) | §423.14A(3)(a) |

- §423.2(1)(a): a tax of "six percent upon the sales price of all sales of tangible personal property, sold at retail in the state to consumers or users except as otherwise provided in this subchapter."
- LOST: "The local sales and service tax may be imposed at any rate of not more than 1 percent" (IAC 701-107.2); the maximum combined rate is therefore 7% (6% + 1%).

## The taxable base

- The base is the "sales price" of taxable retail sales (§423.2); enumerated services (utilities, admissions, etc.) are also taxed at 6% (§423.2(1)).
- Transaction-pattern taxability (general TPP taxable; groceries, prescriptions, manufacturing equipment and resale per statutory exemptions in ch. 423) -- verify each item against the current exemption list in §423.28 and department guidance.

## Deadlines and filing

- Sellers collect the tax and add it to the sales price "as far as practicable" (§423.14(1)(a)); tax computations are carried to the third decimal place with rounding rules (§423.14(1)(b)).
- Return and deposit frequencies are set by department rule for each permit holder -- see Not yet confirmed.

## Penalties and interest

- Failure-to-file/failure-to-pay penalties and interest for sales tax run under general ch. 421/422 provisions -- see Not yet confirmed.

## Cross-border points

- Destination-based sourcing under the Streamlined Sales and Use Tax Agreement is reflected in §423.14A (sourcing of sales to Iowa); registration under the agreement "shall not be used as factors in determining whether the seller has nexus with Iowa for any tax" (ch. 423 interstate agreement provisions).
- Remote sellers meeting the $100,000 threshold must collect Iowa sales tax and applicable local option tax; the statute sets the collection start timing on first exceeding the threshold (§423.14A).

## Worked examples

Iowa's check-examples convention for this pack is not to compute tax in this skill; use `us-sales-tax` and the confirmed rates above. For a hypothetical $1,000 taxable sale in a jurisdiction with the maximum local option tax, the combined rate is 7% (6% state, §423.2(1)(a), plus up to 1% LOST, IAC 701-107.2).

## Ask the client first

- Are sales into Iowa at or above the $100,000 gross-revenue threshold (§423.14A(3)(a))?
- Is the delivery jurisdiction one of the local-option jurisdictions, and is LOST being charged where adopted?
- Are SaaS/digital-product sales sourced to Iowa and taxed as specified digital products (ch. 423)?

## Sources

| Source | URL | Read on |
|---|---|---|
| Iowa Code §423.2 (state sales tax rate) | https://www.legis.iowa.gov/docs/code/423.2.pdf | 2026-10-28 |
| Iowa Code §423.14A (remote sellers and marketplace facilitators; nexus threshold) | https://www.legis.iowa.gov/docs/code/423.14A.pdf | 2026-10-28 |
| Iowa Code §423.14 (collection; rounding) | https://www.legis.iowa.gov/docs/code/423.14.pdf | 2026-10-28 |
| IAC rule 701-107.2 (local option sales and service tax -- rate not more than 1 percent) | https://www.legis.iowa.gov/docs/iac/rule/05-24-2006.701.107.2.pdf | 2026-10-28 |

Not yet confirmed: the item-by-item exemption list in §423.28 (grocery food, prescription drugs, manufacturing equipment, resale) and SaaS/digital-product taxability -- not archived this run; the current department return/deposit frequency tiers; Iowa's Streamlined Sales Tax member status; sales-tax penalty and interest percentages; the current local option rates by jurisdiction.

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
