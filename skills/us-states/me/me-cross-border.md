---
name: me-cross-border
description: >
  Use this skill whenever asked about Maine cross-border individual
  taxation for 2026 — nonresident and part-year taxation of Maine-source
  income (Schedule NR routing on Form 1040ME), the pass-through entity
  withholding (941P-ME) and composite-return rails for nonresident
  owners, credit for taxes paid to other states, and the absence of a
  Maine exit tax. Trigger on "Maine nonresident", "Schedule NR", "1040ME
  nonresident", "Maine composite return", "Maine credit for taxes paid",
  "Maine exit tax". Source-cited draft; 941P-ME/composite rails and the
  § 5111 rate structure verified 2026-10-28; Schedule NR mechanics, credit
  statute cite and reciprocity statements needs-sources.
jurisdiction: US-ME
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - me-income-tax
  - me-payroll
---

# Maine cross-border taxation v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

Covers how Maine reaches nonresidents and how Maine residents get credit for other-state tax. **Source status:** verified 2026-10-28 from MRS pages — **pass-through entities with Maine-source income and nonresident members must withhold (941P-ME), obtain an exemption, or file a composite return combining nonresidents' Maine-source income**; 36 M.R.S. § 5111 sets the graduated rates that apply to Maine taxable income. **Schedule NR mechanics, the credit-for-taxes-paid statute cite, and the no-exit-tax statement — needs-sources** (not fetched this run; the 1040ME page resolves but its nonresident section text was not extracted).

## 2. Who applies

- **Nonresidents with Maine-source income** — file 1040ME with the nonresident schedule (Schedule NR expected — **needs-sources** for the exact routing).
- **Part-year residents** — same mechanics on the residency-split period.
- **Maine residents working/studying in another state** — credit for taxes paid to that other state (statute cite **needs-sources**).
- **Nonresident owners of ME pass-throughs** — entity-level 941P-ME withholding or composite filing (verified).

## 3. Rates

Maine taxable income is taxed on the same graduated schedule as residents (top 7.95% plus 2% surcharge bands — § 5111, verified). Nonresidents are effectively taxed on their Maine-source share (ratio method — mechanics **needs-sources**).

## 4. Base and mechanics

- Maine-source income for nonresidents: wages for work performed in Maine, Maine business income apportioned per Rule 801, Maine rents/gains (detail **needs-sources**).
- **Composite return:** one Maine return covering all nonresident members' Maine-source income, elected by the PTE (verified).
- **Real estate withholding (REW)** on nonresident property sales (nav verified; thresholds **needs-sources**).
- **No Maine exit tax** on departure — assertion, **needs-sources**.

## 5. Deadlines, penalties, interest

1040ME due date expected April 15 with federal-conformity extension behavior — **needs-sources**. Penalties/interest: **needs-sources**.

## 6. Cross-border notes

- No reciprocity agreements located for Maine — **needs-sources** (verify before advising border workers, e.g., NH/Maine commuters).
- Remote workers: days physically worked in Maine create sourcing even for out-of-state employers (verify any convenience-of-the-biometric rule — Maine not known to have one; **needs-sources**).

## 7. Worked examples

**Example 1 — nonresident ratio method (illustrative).** Nonresident with $250,000 total income, $40,000 Maine-source; hypothetical tax on a full $250,000 return $20,000:

```oa-check
name: ME nonresident ratio
inputs:
  total_income: 250000
  me_source: 40000
  tax_on_total: 20000
steps:
  - ratio: me_source / total_income
  - me_tax: tax_on_total * ratio
expected:
  me_tax: 3200.00
```

**Example 2 — 941P over-withholding refund.** PTE withheld $3,975 for the nonresident member (see `me-payroll.md` example); final Maine liability after credits $3,200:

```oa-check
name: ME composite refund
inputs:
  withheld: 3975
  liability: 3200
steps:
  - refund: withheld - liability
expected:
  refund: 775.00
```

## 8. Ask the client

- Where were workdays physically performed? (sourcing driver)
- Is the pass-through already withholding 941P or filing composite — and did the nonresident claim credit at home against that Maine tax?
- Moving out of Maine mid-year? (part-year split; no exit tax asserted — **needs-sources**)

## 9. Sources

1. MRS Pass-through Entity Withholding (941P-ME, composite): https://www.maine.gov/revenue/taxes/income-estate-tax/pass-through-entity-withholding-941p-me-returns — fetched and verified 2026-10-28.
2. 36 M.R.S. § 5111: https://legislature.maine.gov/statutes/36/title36sec5111.html — fetched 2026-10-28.
3. MRS 1040ME page: https://www.maine.gov/revenue/taxes/income-estate-tax/individual-income-tax-1040me — resolves 2026-10-28.

**Needs-sources:** Schedule NR routing, credit statute cite, reciprocity, REW thresholds, due dates, exit-tax confirmation.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Maine nonresident/cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
