---
name: ms-transfer-pricing
description: >
  Use this skill whenever asked about Mississippi transfer pricing and
  combined reporting for 2026 — the Form 83-310 combined report as the
  main related-party policing tool, the 90% estimate rule for combined
  groups, and the absence of a standalone state TP documentation regime.
  Trigger on "Mississippi transfer pricing", "Mississippi combined
  report", "83-310", "Mississippi unitary". Source-cited draft; combined
  report, affiliated-group election and 90% estimate rule verified on
  the DOR Combined Income Filing page 2026-10-28, with the corporate
  rate table from the archived 2025 Form 83-100 instructions.
jurisdiction: US-MS
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.2
depends_on:
  - ms-corporate-income-tax
---

# Mississippi transfer pricing / combined reporting, tax year 2026

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## Who this applies to

- An "affiliated group" of corporations that "may elect to file on a combined basis for purposes of the income tax provided the requirements of Title 35, Part III, Subpart 08, Chapter 07 are met" (DOR Combined Income Filing page).
- Any filer with intercompany management fees, royalties, interest, or rents moving income out of Mississippi.

Mississippi polices related-party income shifting chiefly through combined reporting (Form 83-310) rather than a standalone arm's-length documentation code.

## Rates, bands and thresholds

No standalone TP rate; exposure rides the corporate table — 0% on the first $5,000 of taxable income, 4% on the next $5,000, 5% above $10,000 (2025 Form 83-100 instructions; see `ms-corporate-income-tax.md`).

## The taxable base

"The term combined is used to indicate an election where the separately computed net income/loss of a group of affiliated corporations is summed in order to determine the net income subject to tax" (DOR Combined Income Filing page). The reporting corporation "will file form 83-310, Summary of Net Income of Corporations, as a part of its combination return filing... The combined net income/loss computed on form 83-310 will be entered on Line 4 of form 83-105." Apportionment factor mix: see Not yet confirmed. Federal §482 adjustments flow through conformity (linkage: see Not yet confirmed).

## Deadlines and filing

Combined report rides the corporate calendar: the combination return is due "on or before the 15th day of the 4th month following the close of the accounting year" (2025 Form 83-100 instructions). "In general, a corporation is required to make four quarterly estimated tax payments of at least 90% of its income tax liability... Estimated payments should be remitted by use of the corporate estimate voucher, form 83-300" (DOR Combined Income Filing page). "Estimated payments are not required for franchise tax" (DOR Combined Income Filing page).

## Penalties and interest

"Failure to do so will generally result in underestimate interest and penalties accruing. For further information concerning underestimate calculations, please see Title 35, Part III, Subpart 11, Chapter 21" (DOR Combined Income Filing page). Late-payment penalty 1/2%/month capped at 25%, late-filing penalty 5%/month capped at 25% with a $100 minimum (2025 Form 83-100 instructions; see `ms-corporate-income-tax.md`).

## Cross-border points

Foreign affiliates in an affiliated group: water's-edge treatment is not stated on the fetched DOR page (see Not yet confirmed). State income tax is not treaty-protected (standing US principle).

## Worked examples

**Example 1 — combined income to Mississippi (hypothetical client facts; the 5% top rate is from the skill's own confirmed table above).** Group combined income $1,500,000, hypothetical Mississippi apportionment factor 20%:

```oa-check
name: MS combined apportionment
inputs:
  combined: 1500000
  factor: 0.20
  rate: 0.05
steps:
  - ms_base: combined * factor
  - tax: ms_base * rate
expected:
  ms_base: 300000.00
  tax: 15000.00
```

**Example 2 — royalty shift exposure (hypothetical client facts; 5% rate from the skill's own confirmed table above).** $200,000 intercompany royalty out of the Mississippi member; hypothetical 20% factor:

```oa-check
name: MS royalty shift
inputs:
  royalty: 200000
  factor: 0.20
  rate: 0.05
steps:
  - ms_base_shift: royalty * factor
  - tax_at_stake: ms_base_shift * rate
expected:
  ms_base_shift: 40000.00
  tax_at_stake: 2000.00
```

## Ask the client first

- Is the group commonly owned at combined-report levels? → 83-310 and the 90% estimate rule.
- What intercompany charges run out of Mississippi entities, and are they supported?
- Any foreign affiliates in the chain?

## 9. Sources

1. DOR Combined Filing: https://www.dor.ms.gov/taxes/combined-filing — fetched and verified 2026-10-28.
2. Pre-existing `ms-corporate-income-tax.md` (this pack) for rates.

**Needs-sources:** membership tests, factor mix, addbacks, water's-edge, documentation requirements, penalty percentages.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi combined/TP questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
