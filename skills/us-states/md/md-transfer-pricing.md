---
name: md-transfer-pricing
description: >
  Use this skill whenever asked about Maryland transfer pricing and
  related-party rules for tax year 2026 — Maryland has no standalone state
  transfer-pricing documentation regime; related-party economics enter the
  Form 500 base through the unitary-business/separate-return requirement for
  federal consolidated groups, single receipts-factor apportionment, the
  Special and Alternative Apportionment Formula routes, and separate
  accounting only with Revenue Administration Division approval. Trigger on
  "Maryland transfer pricing", "Maryland related party", "Maryland
  apportionment adjustment", "Maryland alternative apportionment",
  "Maryland separate accounting", "Maryland consolidated group separate
  return".
  Source-cited draft; Comptroller 2024 Corporation Tax Booklet read 2026-10-27.
jurisdiction: US-MD
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - md-corporate-income-tax
---

# Maryland transfer pricing / related-party overlay v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to


Maryland has **no standalone transfer-pricing documentation regime** — no state analogue of IRC §482 with its own penalty or contemporaneous-documentation requirement. Related-party pricing affects Maryland outcomes through four verified levers in the Corporation Tax Booklet: (1) the **separate-return requirement** for members of federal consolidated groups; (2) the **unitary-business** concept that defines what gets apportioned; (3) the **Special Apportionment Formula** (rental/leasing, financial institutions, transportation, worldwide-unitary-headquartered groups) and the **Alternative Apportionment Formula** the Comptroller may accept; and (4) **separate accounting**, allowed only with prior approval of the Revenue Administration Division for nonunitary in-state activity.

**Source status:** all four levers quoted from the Comptroller's 2024 Corporation Tax Booklet (HTTP 200, full text read 2026-10-27). The statutory citations behind them (Tax-General §7-401 et seq. apportionment, §7-404 alternative apportionment) did **not** resolve from the drafting environment — flagged.

## Rates, bands and thresholds


- Any corporation filing Form 500 with related-party transactions that move income or receipts factors across state lines.
- Members of federal consolidated groups: each files a **separate Maryland return** on a separate-company basis "without regard to the consolidation" — intercompany prices therefore survive into each member's Maryland base and factors. (Booklet, read 2026-10-27.)
- Groups using the Special Apportionment Formula: the formula itself is entity-type driven, but intercompany leases, management fees and royalties move the property/payroll/receipts inputs.
- Taxpayers seeking relief from formula distortion: only via an approved Alternative Apportionment Formula or approved separate accounting — not unilaterally.

## The taxable base


There is no separate transfer-pricing rate. The operative amounts:

| Item | Amount / rule | Source |
|---|---|---|
| Corporate rate the adjustments land in | 8.25% flat | Booklet, read 2026-10-27 (see `md-corporate-income-tax`) |
| Apportionment default | single receipts factor (TY beginning after 2021) | Booklet, read 2026-10-27 |
| Special Apportionment Formula | mandatory for rental/leasing, financial institutions, transportation, worldwide-HQ companies | Booklet, read 2026-10-27 |
| Alternative Apportionment Formula | requires Comptroller acceptance | Booklet, read 2026-10-27 |
| Separate accounting | requires prior Revenue Administration Division approval; only for nonunitary activity | Booklet, read 2026-10-27 |
| State-income-tax or intangible addback | none found in the booklet | booklet read 2026-10-27; absence noted — confirm before relying |

## Deadlines and filing


- Alternative-apportionment or separate-accounting requests should be filed **before** the return is filed (the booklet conditions separate accounting on *prior* approval). No fixed statutory clock verified —.
- Form 500 due date and extension mechanics: see `md-corporate-income-tax` (15th day of the 4th month; Form 500E up to 7 months). (not yet confirmed)
- No Maryland TP documentation deadline exists.

## Penalties and interest


- No TP-specific penalty. Adjustments flow into the ordinary regime: interest **11.4825%** annually after 2024, late-filing/payment penalties (percentage, Tax-General §13-701). (Booklet, read 2026-10-27.) (not yet confirmed)
- An unapproved separate-accounting or self-computed apportionment method invites reassessment at the statutory factor plus the interest above.

## Cross-border points


- Maryland follows the federal **unitary business** principle for what income is apportionable; nonunitary activity is allocated by separate accounting only with approval.
- No water's-edge/combined-report election exists in Maryland (separate returns only) — cross-border group structuring questions are federal (IRC §482, GILTI/subpart F) plus each state's own apportionment rules.
- P.L. 86-272 protects solicitation of orders for tangible goods; it does not shelter intercompany service or royalty income.

## Worked examples


**Example 1 — royalty strip moves the receipts factor.** A consolidated member pays a $900,000 royalty to a related IP entity in another state; the payer's Maryland receipts are $6,000,000 of $20,000,000 total. If the royalty is deducted pre-apportionment, Maryland taxable income falls by the Maryland share. (not yet confirmed)

```oa-check
name: MD royalty deduction apportioned effect
inputs:
 royalty: 900000
 receipts_md: 6000000
 receipts_total: 20000000
 rate: 0.0825
steps:
 - factor: receipts_md / receipts_total
 - md_deduction: royalty * factor
 - tax_saved: md_deduction * rate
expected:
 factor: 0.3000
 md_deduction: 270000.00
 tax_saved: 22275.00
```

If the Comptroller re-prices or re-sources the royalty, the exposure is the mirror image: **$22,275** plus 11.4825% interest. (not yet confirmed)

**Example 2 — separate-return vs consolidation arithmetic check.** Two consolidated members, A (Maryland receipts 100% of $2,000,000 income) and B (no Maryland nexus, $1,000,000 income). Federal consolidation nets them; Maryland does not.

```oa-check
name: MD separate return ignores consolidation
inputs:
 a_income: 2000000
 b_income: 1000000
 rate: 0.0825
steps:
 - md_tax: a_income * rate
 - fed_consolidated_would_be: (a_income - b_income) * rate
 - delta: md_tax - fed_consolidated_would_be
expected:
 md_tax: 165000.00
 fed_consolidated_would_be: 82500.00
 delta: 82500.00
```

The $1,000,000 member-B loss shelters nothing in Maryland — a planning point reviewers must price.

## Ask the client first


1. Which members of the federal consolidated group file Maryland returns, and on what separate-company data?
2. What intercompany charges (royalties, management fees, interest, leases) cross into or out of Maryland, and at what arm's-length support?
3. Is the group in a Special Apportionment Formula category, and has anyone sought an Alternative formula?
4. Any separate-accounting approval on file — and is the activity actually nonunitary?
5. Do intercompany services exceed P.L. 86-272 protection?

## Sources


| Source | What it covers | Read on |
|---|---|---|
| COMAR 03.04.08 (financial-institution apportionment) — cited inside the booklet; regulation text not independently fetched,. | internal skill reference | 2026-10-28 |
| Md. Code Tax-General §7-401 et seq., §7-404: — statute pages did not resolve 2026-10-27. | internal skill reference | 2026-10-28 |

Not yet confirmed: the COMAR 03.04.08 regulation text (cited inside the booklet, not independently fetched), the Tax-General §7-401 et seq. and §7-404 statute text, the deadline for alternative-apportionment or separate-accounting requests, and the §13-701 penalty percentage.

## Talk to a verified accountant

No Maryland-specific rule was found in the sources read for this topic.

<!-- openaccountants-cta-block -->

### Talk to a verified accountant

**Talk to a verified accountant** — for Maryland questions on live client facts, book time with an OA Partner.
