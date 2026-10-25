---
name: ga-cross-border-tax
description: >-
  Use when a nonresident works or invests in Georgia, a Georgia business has
  nonresident owners, or an out-of-state company has Georgia activity, and the
  2026 sourcing, de minimis, composite-return and P.L. 86-272 position is
  needed. Trigger on Georgia nonresident return, Schedule 3, Form IT-CR
  composite, 600S-CA Georgia, Public Law 86-272 Georgia, five percent rule.
  Covers the nonresident filing exception (lesser of 5% of income or $5,000),
  Schedule 3 apportionment, S-corp nonresident withholding and composite
  returns, and the P.L. 86-272 solicitation exemption. Source-cited draft.
jurisdiction: US-GA
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Georgia cross-border tax

## 1. Who this applies to

- Nonresident and part-year individual filers with Georgia-source income (Form 500 with Schedule 3) ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download), read 2026-10-24).
- Georgia pass-throughs with nonresident members/shareholders (withholding, Form 600S-CA consent, composite Form IT-CR) ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), read 2026-10-24).
- Out-of-state corporations with Georgia solicitation or sales activity (P.L. 86-272 analysis) (2025 IT-611 booklet, read 2026-10-24).
- Out of scope: residency-determination disputes (refer — O.C.G.A. § 48-7-1 tests); the addback regime (`ga-transfer-pricing-addbacks`).

## 2. Core rules and rates

- **Flat rate for 2026:** 4.99% for taxable years beginning on or after 1 January 2026 (HB 463, read 2026-10-24); 5.19% for 2025.
- **Nonresident employee de minimis exception:** a legal resident of another state whose only Georgia activity is working as an employee need not file a Georgia return if that pay does not exceed **the lesser of five percent of their total pay or $5,000** ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download), read 2026-10-24).
- Part-year residents and nonresidents compute Georgia tax via **Schedule 3** (Georgia net income ratio); they skip Form 500 Lines 9–14 ([2025 IT-511 booklet](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download), read 2026-10-24).
- **S corporation nonresident shareholders:** Georgia recognises the S election only if every nonresident shareholder signs Form 600S-CA; otherwise the entity files Form 600 as a C corporation. Without consent, withholding on nonresident members applies unless a composite return (Form IT-CR) is filed, the members' aggregate annual Georgia-sourced share is under $1,000, or the shareholder properly executed Form 600S-CA and reports and pays the tax (ga-corporate-and-ptet, corroborated by 2025 IT-611 booklet, read 2026-10-24).
- **PTET election binds nonresidents:** an electing entity pays at the entity level at the flat rate; nonresident owners are not separately taxed on that income and no composite return is filed (ga-corporate-and-ptet, read 2026-10-24).
- **P.L. 86-272:** solicitation of orders for tangible personal property, sent outside Georgia for approval and shipment, is exempt from Georgia net-income tax — but **not** from the net worth tax; Forms 600/600S must still be filed with a zero on Schedule 1 line 8 and a statement claiming the exemption ([2025 IT-611 booklet](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download), read 2026-10-24).

## 3. Base and sourcing

- Georgia-source income for nonresidents: wages for work performed in Georgia, Georgia rents, Georgia lottery winnings, flow-through income allocated to Georgia; deferred compensation to nonresidents follows the regulation sourcing rules (Reg. 560-7-4, cited in 2025 IT-611 booklet, read 2026-10-24).
- Schedule 3 apportions federal AGI by the Georgia-net-income-over-total-net-income ratio, then applies the flat rate.

## 4. Deadlines

- Form 500 (with Schedule 3): 15 April for calendar-year individuals; Form 600/600S/700: 15th day of the fourth month after year end; Form IT-CR composite: with the entity return ([2025 IT-511](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download) / [2025 IT-611](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download) booklets, read 2026-10-24).

## 5. Penalties and interest

- Late filing/payment: $25 plus 5% of tax due per month, capped at $25 plus 25%; interest at Federal Reserve prime + 3% compounded per O.C.G.A. § 48-2-40 / § 48-7-126 (2026 Employer's Withholding Tax Guide penalty section, published from <https://dor.georgia.gov/withholding>, read 2026-10-24).

## 6. Treaties and federal overlay

- No state treaty power: US income-tax treaties can limit tax on some nonresident employment/business income; coordinate with the federal skills before claiming relief on a Georgia return.
- Nonresident military: special residency rules for personnel stationed in Georgia under the Servicemembers Civil Relief Act (2025 IT-511 booklet, read 2026-10-24).

## 7. Worked examples

**Example 1 — nonresident employee de minimis test.** A Tennessee resident works in Georgia and earns USD 3,000 of Georgia wages out of USD 90,000 total pay. Threshold: min(90,000 × 5%, 5,000) = 4,500. Georgia pay 3,000 ≤ 4,500 → no Georgia filing required (headroom 4,500 − 3,000 = 1,500). If Georgia pay were 6,000: 6,000 > 4,500 → Form 500-NR with Schedule 3 required.

```oa-check
name: ga nonresident employee de minimis
inputs:
  total_pay: 90000
  ga_pay: 3000
steps:
  - five_pct: total_pay * 0.05
  - threshold: min(five_pct, 5000)
  - headroom: clamp(threshold - ga_pay, 0, 100000)
expected:
  threshold: 4500.00
  headroom: 1500.00
```

**Example 2 — nonresident share via Schedule 3 ratio.** A nonresident's only income is a 25% share of a Georgia LLC's profit: Georgia-source USD 25,000 of USD 100,000 total. Ratio: 25,000 / 100,000 = 0.25. Georgia tax at the 2026 flat rate: 100,000 × 4.99% × 0.25 = USD 1,247.50.

```oa-check
name: ga nonresident schedule 3 apportionment
inputs:
  total_income: 100000
  ga_income: 25000
  rate: 0.0499
steps:
  - ratio: ga_income / total_income
  - ga_tax: total_income * rate * ratio
expected:
  ratio: 0.25
  ga_tax: 1247.50
```

## 8. Ask the client first

1. Where is the individual's legal residence, and what is the Georgia income as a share of total income?
2. Is the employee exception available (Georgia pay ≤ lesser of 5% or $5,000)?
3. For pass-throughs: did every nonresident S shareholder sign Form 600S-CA, or is a composite (IT-CR) or PTET election in place?
4. For out-of-state companies: is activity mere solicitation of tangible-personal-property orders (P.L. 86-272) — and is the net worth tax still being filed?
5. Any treaty position being claimed by a foreign nonresident?

## 9. Sources

- [2025 IT-511 individual income tax booklet (PDF)](https://dor.georgia.gov/document/document/2025-it-511-individual-income-tax-booklet/download) — read 2026-10-24 (de minimis rule, Schedule 3, military nonresidents).
- [2025 IT-611 corporate instruction booklet (PDF)](https://dor.georgia.gov/document/document/2025-it611-corporate-income-tax-instruction-booklet/download) — read 2026-10-24 (P.L. 86-272, 600S-CA, deferred compensation sourcing).
- [HB 463 (2026) enrolled text (PDF)](https://gov.georgia.gov/document/2026-signed-legislation/hb-463/download) — read 2026-10-24 (4.99% flat rate from 1 January 2026).
- [DOR withholding hub](https://dor.georgia.gov/withholding) — read 2026-10-24 (penalty/interest framework via the 2026 Employer's Withholding Tax Guide).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
