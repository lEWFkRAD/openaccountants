---
name: mn-cross-border-tax
description: >-
  Use when a nonresident works or invests in Minnesota, a Minnesota
  partnership has nonresident partners, or an out-of-state company has
  Minnesota activity, and the 2026 Schedule M1NR, composite-return,
  nonresident-withholding and P.L. 86-272 position is needed. Trigger on
  Minnesota nonresident return, Schedule M1NR, composite return 289A.08,
  nonresident partner withholding 290.92, 1000 dollar exception.
  Source-cited draft; 289A.08 subd. 7 and 290.92 text verified 2026-10-25.
jurisdiction: US-MN
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.2
---

# Minnesota cross-border tax

## Who this applies to


- Nonresident and part-year individuals with Minnesota-source income: Form M1 with **Schedule M1NR** (mn-income-tax corroborates the form lane, read 2026-10-25).
- Partnerships with nonresident partners: composite returns under M.S. 289A.08 subd. 7 (<https://www.revisor.mn.gov/statutes/cite/289A.08>, 200 with statute text on 2026-10-25) and nonresident-partner withholding under M.S. 290.92 (<https://www.revisor.mn.gov/statutes/cite/290.92>, 200 with statute text on 2026-10-25).
- Out-of-state corporations with Minnesota nexus (combined-reporting analysis in `mn-transfer-pricing-combined-reporting`).
- Out of scope: residency-domicile disputes (refer).

## Rates, bands and thresholds


- **IIT rates:** graduated 5.35% / 6.75% / 7.85% / 9.85% (mn-income-tax, read 2026-10-25).
- **Composite returns** (M.S. 289A.08 subd. 7(a), statute text read 2026-10-25): the commissioner **may allow** a partnership with nonresident partners to file a composite return and pay tax on behalf of nonresident partners **who have no other Minnesota source income**; the composite return must list each electing partner's name, address, SSN, income allocation and tax liability.
- **Nonresident-partner withholding** (M.S. 290.92, statute text read 2026-10-25): a partnership must withhold on allocations to nonresident partners **unless** (1) the partner elects coverage under the partnership's composite return (289A.08 subd. 7); (2) the partner's Minnesota assignable federal AGI from the partnership is **under $1,000**; or (3) the partnership is liquidated/terminated and the income came from the termination transaction with no cash or other property distributed (statute text read 2026-10-25).
- **Nonresident employees:** employers withhold Minnesota tax for nonresidents performing services in Minnesota (M.S. 290.92 subd. 1 scope, read 2026-10-25).
- **P.L. 86-272:** solicitation-only activity for tangible personal property is exempt from the Minnesota income tax (DOR statement not yet confirmed).

## The taxable base


- Wages: sourced to where services are performed in Minnesota (M.S. 290.92 scope, read 2026-10-25).
- Schedule M1NR apportions by Minnesota assignable federal AGI over total federal AGI (mn-income-tax, read 2026-10-25).
- Part-year residents: M1PR lane (mn-income-tax, read 2026-10-25).

## Deadlines and filing


- Form M1 + Schedule M1NR: 15 April for calendar-year individuals; entity returns: 15th day of the 4th month (mn-income-tax / mn-corporate-and-pte, read 2026-10-25).
- Composite return: filed with the partnership return for the year (289A.08 subd. 7, read 2026-10-25).
- Nonresident withholding deposits: payroll-lane schedule (mn-payroll, read 2026-10-25).

## Penalties and interest


- Withholding failures under 290.92 attract the general penalty/interest regime (M.S. 289A.21 — not yet confirmed: not machine-verified 2026-10-25; mn-payroll corroborates the framework).

## Cross-border points


- No state treaty power; US treaties can limit federal tax on some nonresident income but not Minnesota wage sourcing.
- Military: nonresident servicemembers stationed in Minnesota are not taxed on military pay (SCRA overlay — not yet confirmed).
- Minnesota residents taxed elsewhere claim the credit for taxes paid to other jurisdictions (mn-income-tax, read 2026-10-25).

## Worked examples


**Example 1 — $1,000 withholding exception.** A Wisconsin partner's Minnesota assignable FAGI from a partnership is USD 850. Exception test: 850 < 1,000 → no partnership withholding; the partner still files M1 + M1NR and pays 850 × 0.0535 (bottom bracket) = 45.48.

```oa-check
name: mn nonresident partner 1000 exception
inputs:
  mn_agi: 850
  threshold: 1000
  bottom_rate: 0.0535
steps:
  - under_threshold: min(threshold - mn_agi, 100000)
  - tax: mn_agi * bottom_rate
expected:
  under_threshold: 150.00
  tax: 45.48
```

**Example 2 — composite election replaces withholding.** A partnership allocates USD 40,000 of Minnesota income to a nonresident partner with no other Minnesota income. Without the composite: the partnership withholds (and the partner files individually). With a commissioner-approved composite: the partnership reports the partner on the composite with name, address, SSN, allocation and liability; individual tax at the bottom bracket: 40,000 × 0.0535 = 2,140 paid by the partnership on the partner's behalf.

```oa-check
name: mn composite replaces withholding
inputs:
  alloc: 40000
  rate: 0.0535
steps:
  - composite_tax: alloc * rate
  - individual_filing: 0
expected:
  composite_tax: 2140.00
  individual_filing: 0.00
```

## Ask the client first


- Whether nonresident partners have other Minnesota-source income (the composite eligibility gate).
- Each partner's Minnesota assignable FAGI (the $1,000 withholding exception).
- Workday logs for hybrid employees near the state line.

## Sources

| Source | Read on |
| --- | --- |
| M.S. 289A.08 subd. 7 (composite returns): <https://www.revisor.mn.gov/statutes/cite/289A.08> — statute text archived | 2026-10-28 |
| M.S. 290.92 (nonresident withholding, $1,000 exception) — cited in the skill; not yet archived | 2026-10-25 |
| `mn-income-tax`, `mn-corporate-and-pte`, `mn-payroll` skills — internal corroboration | 2026-10-25 |

Not yet confirmed: M.S. 290.92 nonresident-withholding text (archive pending); M.S. 289A.21 penalty schedule; the DOR P.L. 86-272 solicitation statement; the SCRA military-pay position.
## Talk to a verified accountant


This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
