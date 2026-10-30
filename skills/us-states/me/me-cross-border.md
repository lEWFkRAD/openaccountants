---
name: me-cross-border
description: >
  Use this skill whenever asked about Maine cross-border individual
  taxation for 2026 -- nonresident and part-year taxation of Maine-source
  income (Schedule NR routing on Form 1040ME), the pass-through entity
  withholding (941P-ME) and composite-return rails for nonresident
  owners, credit for taxes paid to other states, and the absence of a
  Maine exit tax. Trigger on "Maine nonresident", "Schedule NR", "1040ME
  nonresident", "Maine composite return", "Maine credit for taxes paid",
  "Maine exit tax". Source-cited draft; 941P-ME/composite rails and the
  § 5111 rate structure verified 2026-10-28; Schedule NR mechanics, credit
  statute cite and reciprocity statements not yet confirmed.
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

Covers how Maine reaches nonresidents and how Maine residents get credit for other-state tax. **Source status:** verified 2026-10-28 from MRS pages -- **pass-through entities with Maine-source income and nonresident members must withhold (941P-ME), obtain an exemption, or file a composite return combining nonresidents' Maine-source income**; 36 M.R.S. § 5111 sets the graduated rates that apply to Maine taxable income. **Schedule NR mechanics, the credit-for-taxes-paid statute cite, and the no-exit-tax statement -- not yet confirmed** (Schedule NR form archived; its mechanics text and the credit statute not line-cited this run).

## Who this applies to

- **Nonresidents with Maine-source income** -- file 1040ME with Schedule NR (2025 Schedule NR archived, read 2026-10-29; 1040ME instructions: "Nonresidents - see Schedule NR instructions for minimum taxability thresholds").
- **Part-year residents** -- same mechanics on the residency-split period.
- **Maine residents working/studying in another state** -- credit for taxes paid to that other state (statute cite not yet confirmed).
- **Nonresident owners of ME pass-throughs** -- entity-level 941P-ME withholding or composite filing (verified).

## Rates, bands and thresholds

Maine taxable income is taxed on the same graduated schedule as residents (top 7.95% plus 2% surcharge bands -- § 5111, verified). Nonresidents are effectively taxed on their Maine-source share (Schedule NR ratio method -- mechanics not yet confirmed line-by-line).

## The taxable base

- Maine-source income for nonresidents: wages for work performed in Maine, Maine business income apportioned per Rule 801 ("This rule explains apportionment for corporations, pass-through entities, sole proprietorships, and other business types that have income from business" -- Rule 801 summary, archived), Maine rents/gains (detail not yet confirmed).
- **Composite return:** one Maine return covering all nonresident members' Maine-source income, elected by the PTE (verified).
- **Real estate withholding (REW)** on nonresident property sales: "The amount to be withheld is equal to 2.5% of the sale price", filed on form REW-1 (MRS Real Estate Withholding page, read 2026-10-29).
- **No Maine exit tax** on departure -- assertion, not yet confirmed.

## Deadlines and filing

1040ME due date: "Form 1040ME due date: Wednesday, April 15, 2026" (2025 Form 1040ME instructions, archived). Penalties/interest: MRS interest table 9% for 2026 (see `me-corporate-income-tax.md`); individual penalty percentages not yet confirmed.

## Penalties and interest

Late filing and late payment attract Maine Revenue Services penalties and interest; the published interest rate is "1/1/26 - 12/31/26 9%" (MRS Interest Rates page, read 2026-10-29). Specific penalty percentages: not yet confirmed.

## Cross-border points

- No reciprocity agreements located for Maine -- not yet confirmed (verify before advising border workers, e.g., NH/Maine commuters).
- Remote workers: days physically worked in Maine create sourcing even for out-of-state employers (verify any convenience-of-the-employer rule -- Maine not known to have one; not yet confirmed).

## Worked examples

**Worked example 1 -- nonresident ratio method (all facts hypothetical).** Nonresident with $250,000 total income, $40,000 Maine-source; hypothetical tax on a full $250,000 return $20,000:

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

**Worked example 2 -- 941P over-withholding refund (hypothetical).** PTE withheld $3,975 for the nonresident member (see `me-payroll.md` example); final Maine liability after credits $3,200:

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

## Ask the client first

- Where were workdays physically performed? (sourcing driver)
- Is the pass-through already withholding 941P or filing composite -- and did the nonresident claim credit at home against that Maine tax?
- Moving out of Maine mid-year? (part-year split; no exit tax asserted -- not yet confirmed)

## Sources

| Source | URL | Read on |
|---|---|---|
| MRS Pass-through Entity Withholding (941P-ME) and Returns | https://www.maine.gov/revenue/taxes/income-estate-tax/pass-through-entity-withholding-941p-me-returns | 2026-10-29 |
| 2025 Schedule NR (nonresident/part-year form) | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/25_1040me_sch_nr_fillable.pdf | 2026-10-29 |
| 36 M.R.S. § 5111 | https://legislature.maine.gov/statutes/36/title36sec5111.html | 2026-10-28 |
| MRS Individual Income Tax (1040ME) | https://www.maine.gov/revenue/taxes/income-estate-tax/individual-income-tax-1040me | 2026-10-29 |

Not yet confirmed: credit statute cite for taxes paid to other states, interstate reciprocity details, real-estate withholding thresholds, and Maine exit-tax confirmation.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Maine nonresident/cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
