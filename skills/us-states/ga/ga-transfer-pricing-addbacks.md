---
name: ga-transfer-pricing-addbacks
description: >-
  Use when a Georgia C corporation, S corporation, or electing pass-through
  pays intangibles, interest, or REIT expenses to a related member and needs
  the 2026 addback, Form IT-Addback / IT-REIT exception, and Schedule 4/5
  mechanics. Trigger on Georgia addback, related member Georgia, IT-Addback,
  captive REIT Georgia, 48-7-37. Georgia has no OECD-style method regime; it
  polices connected-party flows through statutory addbacks. Source-cited draft
  with needs-sources caveat on the statute text.
jurisdiction: US-GA
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Georgia transfer pricing -- related-member addbacks

## Who this applies to
- Georgia Form 600 filers (C corporations), Form 600S filers (S corporations), Form 700 filers (partnerships), and PTET-electing entities that pay **intangible expenses, related interest expense, or captive REIT expenses directly or indirectly to a related member** -- domestic or foreign ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), read 2026-10-24).
- Out of scope: unrelated-party pricing; the federal §482 analysis (federal skills); net worth tax (ga-net-worth-tax).

## Rates, bands and thresholds
- **No Georgia method regime.** Georgia does not run an OECD transfer-pricing method or documentation regime of its own. It polices connected-party flows through **addback statutes**: the taxpayer must add back to federal taxable income (a) all intangible expense and related interest expense directly or indirectly paid to a related member, and (b) all captive REIT expenses directly or indirectly paid to a related member ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), read 2026-10-24).
- **AUDIT FLASH POINT** -- the addition is mandatory on the return **even if the taxpayer qualifies for an exception**; the exception is then taken as a subtraction on Schedule 5, supported by Form IT-Addback (intangible/interest) or Form IT-REIT (captive REIT). Skipping the addition because "the exception applies" is the classic error ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), read 2026-10-24).
- Statutory citation: the addback provisions sit in O.C.G.A. § 48-7-37 et seq. The consolidated statute text could not be archived on 2026-10-24 (legis.ga.gov API returned 500), so the exact subsection wording is listed under Not yet confirmed below; the mechanics here come from the archived DOR booklet.
- Georgia does **not** require unitary combined reporting; the addback, not combination, is the lever (2025 IT-611 booklet, read 2026-10-24).

## The taxable base
- The full intangible/interest/captive-REIT expense paid to the related member is added to federal taxable income on the Georgia return (Schedule 4 additions).
- If a statutory exception applies (for example the related member's income is itself subject to Georgia tax, or a water's-edge style exception), Form IT-Addback / IT-REIT supports a **subtraction on Schedule 5** for all or part of the addition ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), read 2026-10-24).
- Rate applied to the net addition: the flat corporate rate for the taxable year -- 5.19% for years beginning in 2025, **4.99% for years beginning on or after 1 January 2026** (HB 463, read 2026-10-24).

## Deadlines and filing
- The addback rides the entity's annual return: Form 600/600S/700 due by the 15th day of the fourth month after year end (15 April for calendar years); Form IT-Addback / IT-REIT is filed with that return ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), read 2026-10-24).

## Penalties and interest
- Understatements from a disallowed subtraction carry the general Georgia corporate late-filing/late-payment penalties and interest (see ga-corporate-and-ptet; DOR withholding guide penalty framework, read 2026-10-24). Exact corporate penalty schedule: confirm against the current IT-611 booklet.

## Cross-border points
- The addback reaches payments to **foreign** related members -- a royalty to a foreign affiliate is added back whether or not the payment is arm's length; the exception analysis, not the price, is where the taxpayer argues.
- Federal §482 adjustments flow into federal taxable income and therefore into the Georgia base; coordinate both lanes before amending.

## Worked examples
**Example 1 -- royalty and interest to a foreign affiliate, 2026.** A Georgia C corporation pays its Cayman related member USD 400,000 of royalties and USD 100,000 of interest, and claims no exception. Additions: 400,000 + 100,000 = 500,000. Georgia tax on the addition: 500,000 × 4.99% = USD 24,950.

```oa-check
name: ga related-member addback 2026
inputs:
  royalties: 400000
  interest: 100000
  rate: 0.0499
steps:
  - addition: royalties + interest
  - extra_tax: addition * rate
expected:
  extra_tax: 24950.00
```

**Example 2 -- exception fully granted.** Same facts, but the related member's income from the arrangement is subject to Georgia tax and Form IT-Addback supports a full exception. The 500,000 addition is still reported; the Schedule 5 subtraction of 500,000 nets it to zero: 500,000 − 500,000 = 0, tax effect 0 × 4.99% = 0.

```oa-check
name: ga addback with full exception
inputs:
  addition: 500000
  subtraction: 500000
  rate: 0.0499
steps:
  - net: addition - subtraction
  - tax_effect: net * rate
expected:
  net: 0.00
  tax_effect: 0.00
```

## Ask the client first
1. What is paid to related members -- royalties, licence fees, management interest, REIT expenses -- and to whom (state or country)?
2. Was the full addition reported on Schedule 4 even where an exception applies?
3. Is Form IT-Addback / IT-REIT filed and does it support the Schedule 5 subtraction claimed?
4. Is the related member itself subject to Georgia tax on the corresponding income?
5. Any federal §482 or Schedule L positions that change the Georgia starting point?

## Sources

| Source | URL | Read on |
|---|---|---|
| 2025 IT-611 corporate income tax instruction booklet (addback mechanics, captive REIT, IT-Addback/IT-REIT, due dates) | https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download | 2026-10-28 |
| HB 463 (2026) enrolled text (4.99% rate for taxable years beginning on or after 1 January 2026) | https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download | 2026-10-28 |

Not yet confirmed: the exact subsection wording of the related-member addback statutes, O.C.G.A. § 48-7-37 et seq. (legis.ga.gov returned a server error on 2026-10-24 and the consolidated statute text has not been archived; the mechanics above rest on the archived DOR booklet); the exact corporate penalty schedule for a disallowed Schedule 5 subtraction (see the penalties section of ga-corporate-and-ptet before assessing one).


## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
