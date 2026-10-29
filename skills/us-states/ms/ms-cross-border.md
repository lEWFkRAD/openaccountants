---
name: ms-cross-border
description: >
  Use this skill whenever asked about Mississippi cross-border individual
  taxation for 2026 — nonresident taxation of Mississippi-source income,
  the 2026 4% rate environment for border workers, credit for taxes paid
  to other states for Mississippi residents working elsewhere, and the
  absence of local income tax. Trigger on "Mississippi nonresident",
  "80-205", "Mississippi credit for taxes paid", "Mississippi remote
  worker". Source-cited draft; the 2025–2027 rate phase-down verified on
  the DOR rates page 2026-10-28; nonresident return mechanics, credit
  statute and reciprocity needs-sources.
jurisdiction: US-MS
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ms-income-tax
  - ms-payroll
---

# Mississippi cross-border taxation v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

How Mississippi reaches nonresidents and how residents recover other-state tax. **Source status:** the DOR individual rates page (fetched, verified 2026-10-28) confirms the **rate phase-down: 2025 — 0% on the first $10,000 and 4.4% above; 2026 — 4%; 2027 — 3.75%**. **Nonresident return form (80-205 is the conventional number — confirm), the credit-for-taxes-paid statute, reciprocity, and the no-exit-tax statement — needs-sources**.

## 2. Who applies

- **Nonresidents with Mississippi-source income** (wages for work performed in Mississippi, Mississippi business income, rents/gains) — resident-form + nonresident schedule mechanics **needs-sources**.
- **Part-year residents** — split-period filing, mechanics **needs-sources**.
- **Mississippi residents paying tax to another state** — credit expected under conformity practice — **needs-sources**.

## 3. Rates

2026: **4%** flat above the $10,000 zero-rate band (verified). Nonresidents effectively pay the Mississippi-sourced share at that rate.

## 4. Base and mechanics

- Mississippi-source wages: days physically worked in Mississippi (verify any convenience-of-the-employer rule — none located, **needs-sources**).
- **No Mississippi local income tax** on individuals (standing structure — verify, **needs-sources**).
- Withholding applies to Mississippi wages regardless of employee residence (see `ms-payroll.md`).

## 5. Deadlines, penalties, interest

Individual return due April 15 expected (federal conformity) — **needs-sources**. Penalties/interest: **needs-sources**.

## 6. Cross-border notes

- Louisiana/Mississippi border workers: Louisiana nonresident filing may also apply for work in Louisiana (see `la-income-tax` family) — coordinate to avoid double taxation; credit mechanics **needs-sources**.
- No reciprocity agreements located — **needs-sources**.

## 7. Worked examples

**Example 1 — 2026 resident-style computation.** Mississippi taxable income $50,000 in 2026: $10,000 at 0% + $40,000 at 4%:

```oa-check
name: MS 2026 rate 50k
inputs:
  income: 50000
  zero_band: 10000
  rate: 0.04
steps:
  - taxable_above: max(income - zero_band, 0)
  - tax: taxable_above * rate
expected:
  tax: 1600.00
```

**Example 2 — nonresident ratio (illustrative).** Nonresident, total income $300,000, Mississippi-source $60,000; hypothetical full-return tax $12,000:

```oa-check
name: MS nonresident ratio
inputs:
  total_income: 300000
  ms_source: 60000
  tax_on_total: 12000
steps:
  - ratio: ms_source / total_income
  - ms_tax: tax_on_total * ratio
expected:
  ms_tax: 2400.00
```

## 8. Ask the client

- How many workdays physically in Mississippi vs home state?
- Home state — will it credit the Mississippi tax paid (avoid double tax)?
- Moving to/from Mississippi mid-year? (part-year split)

## 9. Sources

1. DOR individual rates: https://www.dor.ms.gov/taxes/individual-income-tax — fetched and verified 2026-10-28 (2025–2027 phase-down).
2. DOR withholding: https://www.dor.ms.gov/taxes/withholding — fetched 2026-10-28.

**Needs-sources:** nonresident form/schedule, credit statute, reciprocity, local-income-tax confirmation, due dates, exit-tax confirmation.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi nonresident/cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
