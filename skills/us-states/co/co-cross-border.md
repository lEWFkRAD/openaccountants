---
name: co-cross-border
description: >
  Use this skill whenever asked about Colorado cross-border taxation
  for tax year 2026 — when an out-of-state or foreign corporation or
  owner becomes a Colorado taxpayer (substantial-nexus thresholds of
  $50,000 of payroll or property and $500,000 of sales, or 25% of total
  factors), Public Law 86-272 solicitation protection (15 U.S.C. §381),
  receipts-factor sourcing of multistate sales under C.R.S. §39-22-303.6,
  the resident credit for tax paid to another state (C.R.S. §39-22-108),
  and nonresident partner obligations under the composite and SALT Parity
  regimes. Trigger on "Colorado nexus", "Colorado doing business",
  "PL 86-272 Colorado", "Colorado cross-border", "out-of-state corporation
  Colorado tax", "Colorado credit for taxes paid". DR 0106 instructions
  and the Corporate Income Tax Guide read 2026-10-28.
jurisdiction: US-CO
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
review_status: pending_review
depends_on:
  - co-corporate-income-tax
---

# Colorado cross-border taxation, tax year 2026

> **Source-cited draft.** Revised 2026-10-28 against the 2025 DR 0106 instructions, the Corporate Income Tax Guide (March 2026), 15 U.S.C. §381 and the Colorado Revised Statutes 2026. v0.1 carried a "$100,000 economic nexus" figure that belongs to Colorado sales-and-use tax, not income tax; the income-tax nexus thresholds below are the Corporate Income Tax Guide's. No accountant has reviewed this draft.

## Who this applies to

- An out-of-state (foreign) C corporation is subject to Colorado income tax when it is doing business in Colorado: whenever the minimum standards of Public Law 86-272 are exceeded and the corporation has substantial nexus with Colorado ([Corporate Income Tax Guide, Part 1](https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf); Department Rule 39-22-301(1)).
- **Substantial nexus** exists if Colorado property or payroll exceeds $50,000, or Colorado sales exceed $500,000, or 25% or more of the corporation's total property, payroll or sales are in Colorado (Corporate Income Tax Guide, Part 1).
- Nonresident partners and shareholders of Colorado pass-through entities are taxed through the composite return or the SALT Parity credit mechanics (DR 0106 instructions — see `co-s-corporation-tax`).
- Nonresident individuals with Colorado-source income and part-year residents compute tax on DR 0104PN (C.R.S. §§39-22-109, 39-22-110; see `co-income-tax`).
- Colorado residents taxed on the same income by another state may claim a credit for tax paid to that state (C.R.S. §39-22-108; the Department publishes "Income Tax Topics: Credit for Tax Paid to Another State").

## Rates, bands and thresholds

| Item | Amount | Source |
|---|---|---|
| Corporate / individual rate | 4.4% flat | DR 0106 instructions: "Multiply line 19 by 4.4% (0.044)"; Corporate Income Tax Guide, Part 3 |
| Nexus: Colorado property or payroll | Over $50,000 | Corporate Income Tax Guide, Part 1 |
| Nexus: Colorado sales | Over $500,000 | Corporate Income Tax Guide, Part 1 |
| Nexus: share of total factors | 25% or more of total property, payroll or sales in Colorado | Corporate Income Tax Guide, Part 1 |
| Apportionment | Receipts factor | C.R.S. §39-22-303.6, as referenced on the DR 0106 instructions |

## The taxable base

- Colorado-source income for a nonresident includes property located in Colorado, business carried on in Colorado, and intangibles employed in a Colorado business; the DR 0106 instructions reference the Rule 39-22-109 sourcing framework and C.R.S. §39-22-303.6 receipts-factor apportionment.
- An entity with no activity outside Colorado sources 100% of its income to Colorado (DR 0106 instructions).
- First-year filers register with the Department of Revenue; filing obligations begin with the first year of nexus.
- Dividends between C corporations includible in the same combined report are excluded from taxable income (Corporate Income Tax Guide, Part 3).

## Deadlines and filing

- DR 0106 (partnerships and S corporations): the fifteenth day of the fourth month after the close of the tax year, which is April 15 for calendar-year filers; an automatic six-month extension to October 15, with **no extension of payment** (DR 0106 instructions).
- DR 0112 (C corporations): the fifteenth day of the fifth month — May 15 for calendar-year filers — with an automatic six-month extension to November 15 and no extension of payment ([DR 0112 (2025) instructions](https://tax.colorado.gov/sites/default/files/documents/DR0112_2025.pdf)).

## Penalties and interest

- The delinquent-payment penalty is the greater of $5 or 5% of the additional tax due for the first month of delinquency, plus 0.5% for each additional month, up to 12% in total; it is avoided if 90% of the tax is paid by the original due date (DR 0106 instructions).
- Estimated-tax penalties are computed on form DR 0233 (pass-throughs) or DR 0205 (C corporations) (DR 0106 instructions; Corporate Income Tax Guide, Part 9).
- Interest runs at the rate fixed under C.R.S. §39-21-110.5 (Colorado Revised Statutes 2026; v0.1 cited §39-21-118, which in the 2026 statutes is "Criminal penalties").

## Cross-border points

- **Public Law 86-272** (15 U.S.C. §381): no state may impose a net-income tax on a person whose only business activity within the state is solicitation of orders for tangible personal property, where the orders are sent outside the state for approval or rejection and filled from outside the state ([Cornell LII, 15 U.S.C. §381](https://www.law.cornell.edu/uscode/text/15/381)). There is no protection where the activity includes services, intangibles, or in-state fulfillment; the Corporate Income Tax Guide applies the "doing business" test only when these federal minimum standards are exceeded.
- **Treaties:** U.S. income-tax treaties generally do not limit a state's power to tax; do not assume treaty relief applies to Colorado tax.
- **Credit for taxes paid:** a Colorado resident may credit income tax paid to another state on income subject to tax in both states (C.R.S. §39-22-108).
- **SALT Parity vs other states:** Colorado's entity-level election interacts with other states' pass-through-entity tax regimes for multistate groups — coordinate elections state by state.
- **Real-estate withholding:** nonresidents selling Colorado real estate face DR 1079 withholding, credited by submitting the DR 1079 with the return (DR 0106 instructions).

## Worked examples

A Texas corporation with no Colorado property or payroll has Colorado receipts of $1,200,000 and total receipts of $6,000,000; unitary income $2,000,000 (hypothetical facts; receipts factor per C.R.S. §39-22-303.6):

```oa-check
name: receipts factor cross-border tax
inputs:
  co_receipts: 1200000
  total_receipts: 6000000
  income: 2000000
  rate: 0.044
steps:
  - factor: co_receipts / total_receipts
  - apportioned: income * factor
  - tax: apportioned * rate
expected:
  factor: 0.20
  apportioned: 400000.00
  tax: 17600.00
```

The same corporation's only Colorado activity is solicitation of orders for tangible personal property shipped from Texas, so the income is protected by Public Law 86-272 (hypothetical facts):

```oa-check
name: PL 86-272 protected
inputs:
  co_receipts: 1200000
  total_receipts: 6000000
  income: 2000000
  factor: 0.20
  rate: 0.044
  protected: 1
steps:
  - apportioned: income * factor
  - tax: apportioned * rate * (1 - protected)
expected:
  apportioned: 400000.00
  tax: 0.00
```

## Ask the client first

- What Colorado contacts exist — employees, agents, inventory, marketplace sales, remote workers? Do Colorado property or payroll exceed $50,000, or Colorado sales exceed $500,000?
- Is the activity pure solicitation of tangible-goods orders (PL 86-272), or does it include services, intangibles or in-state fulfillment?
- Are nonresident owners aware of composite / SALT Parity mechanics and their own DR 0104 credits?
- Is the client a Colorado resident who paid income tax to another state — is credit documentation being kept?

## Sources

| Source | URL | Read on |
|---|---|---|
| Colorado DOR — Colorado Corporate Income Tax Guide (March 2026) | https://tax.colorado.gov/sites/default/files/documents/Corporate_Income_Tax_Guide_Mar_2026_.pdf | 2026-10-28 |
| Colorado DOR — Form DR 0106 instructions (2025) | https://tax.colorado.gov/sites/tax/files/documents/DR0106_2025.pdf | 2026-10-28 |
| Colorado DOR — Form DR 0112 (2025) C Corporation Income Tax Return and instructions | https://tax.colorado.gov/sites/default/files/documents/DR0112_2025.pdf | 2026-10-28 |
| Colorado OLLS — Colorado Revised Statutes 2026, Title 39 (Taxation) | https://olls.info/crs/crs2026-title-39.pdf | 2026-10-28 |
| Cornell Law LII — 15 U.S.C. §381 (Public Law 86-272) | https://www.law.cornell.edu/uscode/text/15/381 | 2026-10-28 |
| Colorado DOR — Colorado Taxes & Fees Due Date Guide | https://tax.colorado.gov/due-date-guide | 2026-10-28 |

Not yet confirmed: the statutory text and mechanics of the C.R.S. §39-22-108 credit for tax paid to another state (the section number is confirmed from the Title 39 table of contents, but the DOR topic page "Income Tax Topics: Credit for Tax Paid to Another State" was not successfully archived this run — confirm the computation order and limits before advising); whether a nonresident's retirement income protection (4 U.S.C. §114) is applied by Colorado exactly as stated in v0.1 (the claim was carried from the Part-Year Residents & Nonresidents topic, which was archived — re-read the credit paragraphs before relying on them for a filing position).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

**Talk to a verified accountant** — for Colorado nexus and cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
