---
name: ky-transfer-pricing
description: >
  Use this skill whenever asked about Kentucky transfer pricing and combined filing for tax year 2026 -- the mandatory unitary combined group filing from tax years beginning 2019, the 48-month same-as-federal consolidated group election, the combined-group definition (50% voting stock, waters-edge), and how related-party pricing is policed through the combined computation rather than a standalone addback regime. Trigger on "Kentucky combined reporting", "Kentucky unitary", "Kentucky consolidated election", "Kentucky transfer pricing", "Kentucky 48 month election". ALWAYS load us-tax-workflow-base first.
version: 0.3
jurisdiction: US-KY
category: transfer-pricing
tax_year: 2026
last_updated: 2026-10-28
tier: 2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - ky-corporate-income-tax
---

# Kentucky transfer pricing / combined filing, tax year 2026

> **Source-cited draft.** Built from KRS 141.202, 141.120, 141.040 and the DOR Corporation Income & LLET page, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

Every member of a unitary business group of corporations: for tax years beginning on or after 1 January 2019, "Unitary Combined Group filing required," unless the group elects "a 48 month same-as-federal consolidated group filing" (DOR page). KRS 141.202 defines a combined group as "only corporations, the voting stock of which is more than fifty percent (50%) owned, directly or indirectly, by a common owner or owners," and a unitary business as "a single economic enterprise that is made up either of separate parts of a single corporation or of a commonly controlled group of corporations that are sufficiently interdependent, integrated, and interrelated."

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Rate | Flat 5% on combined Kentucky taxable income (TYB on/after 2018) | KRS 141.040(2) |
| Consolidated election | Same-as-federal, 48-month lock-in | DOR page |
| Combined report | Waters-edge: "The combined report shall be filed on a waters-edge basis under subsection (8) of this section" | KRS 141.202(4)(a) |
| Apportionment | Receipts-only fraction (KRS 141.120(9)) | KRS 141.120 |
| Documentation regime | Kentucky polices related-party pricing through combined computation rather than a standalone addback statute; no separate Kentucky transfer-pricing documentation statute found in the archived KRS 141 sections this run | absence noted; see Not yet confirmed |

## The taxable base

The combined report consolidates the income and apportionment factors of the combined group: each member's share is "the taxpayer member's apportionment fraction, determined under KRS 141.120, including in the sales factor numerator the taxpayer's sales associated with the combined group's unitary business in this state" (KRS 141.202). Intercompany dealings between members of the combined group are eliminated inside the combined computation because the group's income and factors are taken into account together; dealings with non-members sit inside the apportionment analysis. The group designates one taxpayer member "to file a single return in lieu of filing their own respective returns," and that member "shall consent to act as surety with respect to the tax liability of all other taxpayers properly included in the combined report" (KRS 141.202).

## Deadlines and filing

- The combined return rides the Form 720 calendar (April 15 for calendar-year filers).
- Estimated installments: "Four installments at 25% of the estimated tax due on April 15, June 15, September 15, and December 15" (DOR page), computed at the combined level.
- Federal audit final determinations: amended Kentucky return within 180 days (DOR page).
- The 48-month consolidated election has no annual deadline -- but track the expiry year.

## Penalties and interest

The declaration penalty was replaced by an "Addition to Tax" penalty for underpaid estimated tax (DOR page; TAM-19-02). Late payment runs 2% per 30 days capped at 20% with a $10 minimum (DOR Penalties, Interest and Fees page). Interest on unpaid tax: 9% for 2026, 10% for 2025, under KRS 131.183(2)(a)2 (DOR interest notices); KRS 141.985 applies the tax interest rate to unpaid chapter-141 tax.

Common failure modes: (1) filing separate-entity when the group is unitary; (2) making the consolidated election without modeling the 48-month lock; (3) assuming foreign affiliates are automatically in or out -- the waters-edge rule and the 50% voting-stock test drive membership, member by member; (4) missing the 180-day federal-audit amendment window, which is where most transfer-pricing adjustments surface.

## Cross-border points

- Waters-edge: the combined report is filed on a waters-edge basis (KRS 141.202(4)(a)); the DOR page describes the group as "domestic corporations (with some exceptions) involved in unitary business."
- Receipts-only apportionment means sales into Kentucky -- wherever the seller sits -- create apportioned income for combined-group members (KRS 141.120(9)-(11): receipts are in this state if the market is here, including services "delivered to a location in this state").
- No Kentucky addback statute for related-party payments was found in the archived KRS 141 sections this run; federal §482 adjustments flow through the federal taxable income starting point and the 180-day amendment rule.
- LLET paid by a limited liability pass-through entity credits against members' Kentucky income tax (KRS 141.0401; see `ky-cross-border`).

## Worked examples

### Example 1: combined computation (hypothetical facts)

A unitary group with $8,000,000 combined apportionable income and a 25% Kentucky receipts factor: Kentucky income $2,000,000; tax $2,000,000 × 5% = $100,000.

```oa-check
name: KY combined tax unitary group
inputs:
  combined: 8000000
  app: 0.25
  rate: 0.05
steps:
  - ky_income: combined * app
  - tax: ky_income * rate
expected:
  ky_income: 2000000.00
  tax: 100000.00
```

### Example 2: fee shift to a non-member (hypothetical facts)

The same group pays $600,000 of management fees to a non-member affiliate, reducing combined income before apportionment. New combined income $7,400,000; Kentucky income $1,850,000; tax $92,500 -- a $7,500 Kentucky saving that must survive federal scrutiny of the fee.

```oa-check
name: fee shift effect on combined base
inputs:
  combined: 8000000
  shift: 600000
  app: 0.25
  rate: 0.05
steps:
  - new_combined: combined - shift
  - new_ky: new_combined * app
  - new_tax: new_ky * rate
  - saving: 100000 - new_tax
expected:
  new_combined: 7400000.00
  new_ky: 1850000.00
  new_tax: 92500.00
  saving: 7500.00
```

## Ask the client first

- Is the group unitary under KRS 141.202's definition -- has anyone mapped members against the 50% voting-stock and flow-of-value tests?
- Has the 48-month consolidated election been made, and when does it expire?
- Are intercompany fees moving income outside the combined base -- and are they defensible at the federal level too?
- Any federal audit adjustments -- is the 180-day Kentucky amendment clock tracked?

## Sources

| Source | URL | Read on |
|---|---|---|
| KRS 141.202 (combined report requirement; unitary business and combined-group definitions; waters-edge; TYB 2019+) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.202 | 2026-10-28 |
| KRS 141.120 (apportionment; receipts-only fraction; market-based sourcing) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.120 | 2026-10-28 |
| KRS 141.121 (special apportionment rules; treasury functions; airlines; sourcing of receipts) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.121 | 2026-10-28 |
| KRS 141.040 (flat 5% corporate rate) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.040 | 2026-10-28 |
| KRS 141.985 (interest on unpaid chapter 141 tax) | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=KRS141.985 | 2026-10-28 |
| DOR Corporation Income & LLET page (48-month election; combined-group description; estimated tax; Addition to Tax) | https://revenue.ky.gov/Business/Corporation-Income-and-Limited-Liability-Entity-Tax/Pages/default.aspx | 2026-10-28 |
| Form 720 (Corporation Income Tax and LLET return, PDF) | https://revenue.ky.gov/Forms/720.pdf | 2026-10-28 |
| TAM-19-02 Estimated Tax Payments (PDF) | https://revenue.ky.gov/TaxProfessionals/PublishingImages/Pages/Guidance/Estimated%20Tax%20Payments%20TAM-19-02%20FINAL%204.3.19.pdf | 2026-10-28 |
| DOR Penalties, Interest and Fees page | https://revenue.ky.gov/Collections/Pages/Penalties-Interest-and-Fees.aspx | 2026-10-28 |

Not yet confirmed: whether Kentucky has a related-party interest/intangible addback or documentation statute outside the archived KRS 141 sections (no addback provision appeared in KRS 141.040/141.120/141.202/141.121; a full chapter review is recommended before advising); the detailed intercompany-elimination mechanics within the combined computation (KRS 141.202's surety and designated-member provisions are archived; DOR combined-return form instructions are not); the treatment of foreign members under the waters-edge rule beyond the statutory subsection reference (KRS 141.202(8) not separately archived).

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
