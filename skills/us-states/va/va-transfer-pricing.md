---
name: va-transfer-pricing
description: >-
  Use when a related-company group files or plans Virginia corporate income
  tax: affiliated-group filing options (Va. Code § 58.1-442 separate,
  combined or consolidated returns), the § 58.1-446 price-manipulation rule
  (income adjusted to arm's-length where intercompany prices shift income
  in or out of Virginia), the § 58.1-442.1 addback of related-party
  intangible expense (royalties/management fees to affiliates), and
  apportionment mechanics (§ 58.1-416 sourcing, § 58.1-422 single sales
  factor for manufacturing and shipping companies). Trigger on Virginia
  combined reporting, Virginia addback statute, Virginia unitary group,
  intercompany royalty Virginia, Virginia apportionment sales factor.
  Source-cited draft; addback section number not yet confirmed.
jurisdiction: US-VA
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Virginia transfer pricing and affiliated-group rules

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

C corporations and other entities filing Virginia corporate income tax that are members of an affiliated or unitary group, plus any Virginia filer with intercompany transactions (royalties, management fees, interest, sales of goods or services) with related parties inside or outside the US. Virginia taxes at a flat **6%** of Virginia taxable income (§ 58.1-400, verified 2026-10-27), so every dollar of apportionable income moved by intercompany pricing is worth 6 cents — and the Department of Taxation has explicit statutory authority to reprice transactions that move income out of the state. (not yet confirmed)

## 2. Rates and key rules

| Item | Figure / rule | Source / status |
|---|---|---|
| Corporate rate | 6% flat on Virginia taxable income | § 58.1-400 — verified 2026-10-27 | (not yet confirmed)
| Group filing options | Separate, combined, or consolidated returns for affiliated groups; election mechanics in § 58.1-442 | § 58.1-442 — verified 2026-10-27 |
| Price manipulation | Where related-party prices "shift, shift away, convey, transport or otherwise manipulate income… receipts or deductions," the Department adjusts to produce the arm's-length result | § 58.1-446 — verified 2026-10-27 |
| Intangible/management-fee addback | Related-party intangible expense and management-fee addback applies to separate- and combined-filing groups (intangible expense added back unless the affiliate's related income is Virginia-taxed; management-fee addback with a 2% de minimis) | § 58.1-442.1 — **not yet confirmed** (section body not retrieved this run; rule carried from practice) [VERIFY] |
| Apportionment | Default three-factor formula (property, payroll, sales) with double-weighted sales factor; **single sales factor** for manufacturing and shipping companies | § 58.1-422 — verified 2026-10-27 |
| Sales sourcing | Market-based sourcing: sales are assigned to the market where the benefit of the service is received / customer's location for tangible goods | § 58.1-416 — verified 2026-10-27 |
| Federal overlay | Virginia starts from federal taxable income; IRC § 482 adjustments flow through automatically; no separate state TP documentation standard | § 58.1-400 start point; [VERIFY documentation practice] |

## 3. Base and mechanics

- **Virginia taxable income** = federal taxable income with state modifications, multiplied by the apportionment percentage. TP exposure therefore arises in two places: (a) the federal § 482 layer, which Virginia picks up automatically, and (b) the state apportionment layer, where intercompany charges move the sales/payroll/property factors.
- **Combined reporting** (where elected or required for the group structure) collapses intercompany transactions — they are eliminated on consolidation, which neutralises most intra-group pricing questions but exposes the group to the unitary-combination questions (water's-edge, includible members).
- **Separate filing** keeps intercompany charges visible: the § 58.1-446 price-manipulation rule and the § 58.1-442.1 addback are the Department's tools here.
- **Addback logic (verify before relying):** royalties/intangible expense paid to a related member are added back to the payer's Virginia income unless the recipient includes the corresponding income in Virginia taxable income; management fees are added back dollar-for-dollar above a 2% de minimis of the apportioned costs. (not yet confirmed)

### 4. Deadlines and filings

- Virginia corporate return (Form 500) follows the federal due date (April 15 for calendar-year C corps; extensions per the Department's rules). _(tax.virginia.gov/corporation-income-tax verified 200 2026-10-27; exact date page [VERIFY].)_ (not yet confirmed)
- Combined/consolidated elections and any required group schedules attach to Form 500; changes in filing method generally need Department consent — confirm before switching methods.
- No standalone Virginia TP documentation filing; documentation is audit-defence only.

### 5. Penalties and interest

- Late payment: penalty of **6% of the tax due per month, capped at 30%**, plus interest at the federal IRC § 6621 underpayment rate **plus 2%** — § 58.1-455 and § 58.1-15, both verified 2026-10-27.
- Underpayment attributable to a § 58.1-446 repricing adjustment accrues the same penalty/interest stack from the original due date.
- Failure to withhold/pay over (relevant where the repricing recharacterises payments) carries the § 58.1-468 employer liability — verified 2026-10-27.

### 6. Cross-border notes

- Virginia has no separate outbound withholding regime for cross-border royalties beyond the federal layer; the state exposure is the addback and repricing rules, not WHT.
- Foreign affiliates: with water's-edge combined filing (where applicable), intangible expense to a related foreign member is a classic addback target — model the addback before choosing a holding-company location.
- Interstate groups: market-based sourcing (§ 58.1-416) means a service fee billed to a Virginia customer is Virginia-sourced regardless of where the performing affiliate sits — invoicing geography does not move the sales factor.

### 7. Worked examples

**Example 1 — apportionment with double-weighted sales.** A manufacturer (not single-sales-factor eligible) has $1,000,000 of apportionable income; its apportionment percentage computes to 35% (property 20%, payroll 40%, sales 40% × 2, weighted average 35%).

```oa-check
name: va apportionment three factor double weighted sales
inputs:
  income: 1000000
  prop: 0.20
  pay: 0.40
  sales: 0.40
steps:
  - ap: (prop + pay + 2 * sales) / 4
  - va_income: income * ap
  - tax: va_income * 0.06
expected:
  ap: 0.35
  va_income: 350000.00
  tax: 21000.00
```

**Example 2 — single sales factor for a manufacturer.** A Virginia-shipping manufacturer earns $500,000 of apportionable income; total sales $8,000,000, of which $2,000,000 are Virginia-market.

```oa-check
name: va manufacturing single sales factor
inputs:
  income: 500000
  va_sales: 2000000
  total_sales: 8000000
steps:
  - ap: va_sales / total_sales
  - va_income: income * ap
  - tax: va_income * 0.06
expected:
  ap: 0.25
  va_income: 125000.00
  tax: 7500.00
```

### 8. Ask the client first

1. Filing method: separate, combined, or consolidated — and when was the election last reviewed?
2. Which intercompany intangible/management-fee flows exist, and does the recipient affiliate file Virginia returns (the addback exception turns on this)?
3. Is the entity a manufacturing or shipping company — does the single sales factor apply?
4. Where are service customers located (market-based sourcing), not where invoices are raised?
5. Any federal § 482 adjustments or APAs — they flow into Virginia starting income automatically.

### 9. Sources

- Code of Virginia § 58.1-400 (6% rate): <https://law.lis.virginia.gov/vacode/title58.1/chapter13/section58.1-400/> — 200 with text, 2026-10-27. (not yet confirmed)
- Code of Virginia § 58.1-442 (separate/combined/consolidated returns): <https://law.lis.virginia.gov/vacode/title58.1/chapter13/section58.1-442/> — 200 with text, 2026-10-27.
- Code of Virginia § 58.1-446 (intercompany price manipulation): <https://law.lis.virginia.gov/vacode/title58.1/chapter13/section58.1-446/> — 200 with text, 2026-10-27.
- Code of Virginia § 58.1-416 (sourcing) and § 58.1-422 (apportionment formula; single sales factor for manufacturing/shipping): chapter13 section pages — 200 with text, 2026-10-27.
- Code of Virginia § 58.1-455 (penalty 6%/month to 30%) and § 58.1-15 (interest = IRC § 6621 + 2%): 200 with text, 2026-10-27.
- Virginia Tax corporation income tax portal: <https://www.tax.virginia.gov/corporation-income-tax> — 200 with text, 2026-10-27.
- § 58.1-442.1 (intangible/management-fee addback): **not yet confirmed** — section body not retrieved 2026-10-27; rule carried from practice, verify text before publication.

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at the OpenAccountants network.

- Use it in your AI: 
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Who this applies to

Not yet confirmed against archived sources.

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
