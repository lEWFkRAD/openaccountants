---
name: mn-cross-border-tax
description: >-
  Use when a nonresident works or invests in Minnesota, a Minnesota
  partnership has nonresident partners, or an out-of-state company has
  Minnesota activity, and the 2026 Schedule M1NR, composite-return,
  nonresident-withholding and P.L. 86-272 position is needed. Trigger on
  Minnesota nonresident return, Schedule M1NR, composite return 289A.08,
  nonresident withholding 290.92.
  Source-cited draft; 289A.08 subd. 7 text verified 2026-10-28 and 290.92
  text archived 2026-11-02.
jurisdiction: US-MN
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-11-02
version: 0.3
---

# Minnesota cross-border tax

## Who this applies to


- Nonresident and part-year individuals with Minnesota-source income: Form M1 with **Schedule M1NR** (mn-income-tax corroborates the form lane, read 2026-10-25).
- Partnerships with nonresident partners: composite returns under M.S. 289A.08 subd. 7 (<https://www.revisor.mn.gov/statutes/cite/289A.08>, statute text archived 2026-10-28) and withholding on nonresident individuals' wages under M.S. 290.92 (<https://www.revisor.mn.gov/statutes/cite/290.92>, statute text archived 2026-11-02).
- Out-of-state corporations with Minnesota nexus (combined-reporting analysis in `mn-transfer-pricing-combined-reporting`).
- Out of scope: residency-domicile disputes (refer).

## Rates, bands and thresholds


- **IIT rates:** graduated 5.35% / 6.75% / 7.85% / 9.85% (mn-income-tax, read 2026-10-25).
- **Composite returns** (M.S. 289A.08 subd. 7(a), statute text read 2026-10-25): the commissioner **may allow** a partnership with nonresident partners to file a composite return and pay tax on behalf of nonresident partners **who have no other Minnesota source income**; the composite return must list each electing partner's name, address, SSN, income allocation and tax liability.
- **Nonresident wage withholding** (M.S. 290.92 subd. 4a, statute text read 2026-11-02): "any person having control, receipt, custody, disposal or payment of compensation taxable under this chapter and earned by a nonresident for personal services, shall be deemed an employer" and that compensation "shall be deemed wages" -- Minnesota employers (and out-of-state payers) withhold on nonresidents' Minnesota services.
- **Nonresident-partner withholding exceptions** (composite election, a $1,000 Minnesota-assignable-income floor, termination distributions): the partnership-level withholding rule and its exceptions are not in 290.92's text and the governing section is not yet identified (see Not yet confirmed below).
- **Nonresident employees:** employers withhold Minnesota tax for nonresidents performing services in Minnesota (M.S. 290.92 subd. 1 scope, read 2026-10-25).
- **P.L. 86-272:** solicitation-only activity for tangible personal property is exempt from the Minnesota income tax (federal statute; see Not yet confirmed below).

## The taxable base


- Wages: sourced to where services are performed in Minnesota (M.S. 290.92 scope, read 2026-10-25).
- Schedule M1NR apportions by Minnesota assignable federal AGI over total federal AGI (mn-income-tax, read 2026-10-25).
- Part-year residents: M1PR lane (mn-income-tax, read 2026-10-25).

## Deadlines and filing


- Form M1 + Schedule M1NR: "Your 2026 Minnesota income tax return should be electronically filed, postmarked, or dropped off by April 15, 2027" (M1 instructions, read 2026-11-02). Entity returns: "must be filed by the due date for filing your federal income tax return" with an automatic seven-month extension (Form M4 instructions, 2025, read 2026-10-31).
- Composite return: filed with the partnership return for the year (289A.08 subd. 7, read 2026-10-25).
- Nonresident withholding deposits: payroll-lane schedule (mn-payroll, read 2026-10-25).

## Penalties and interest


- Withholding failures under 290.92 attract the civil penalty and interest regime of M.S. 289A.60 and 289A.55 -- chapter 289A has no section 289A.21 (chapter table of contents archived 2026-10-31).

## Cross-border points


- No state treaty power; US treaties can limit federal tax on some nonresident income but not Minnesota wage sourcing.
- Military: nonresident servicemembers stationed in Minnesota are not taxed on military pay (SCRA overlay; see Not yet confirmed below).
- Minnesota residents taxed elsewhere claim the credit for taxes paid to other jurisdictions (mn-income-tax, read 2026-10-25).

## Worked examples


### Worked example 1: $1,000 withholding exception (rule pending source)

A Wisconsin partner's Minnesota assignable FAGI from a partnership is USD 850. Exception test: 850 < 1,000 → no partnership withholding; the partner still files M1 + M1NR and pays 850 × 0.0535 (bottom bracket) = 45.48.

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

### Worked example 2: composite election replaces withholding

A partnership allocates USD 40,000 of Minnesota income to a nonresident partner with no other Minnesota income. Without the composite: the partnership withholds (and the partner files individually). With a commissioner-approved composite: the partnership reports the partner on the composite with name, address, SSN, allocation and liability; individual tax at the bottom bracket: 40,000 × 0.0535 = 2,140 paid by the partnership on the partner's behalf.

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
- Each partner's Minnesota assignable FAGI (the $1,000 withholding exception, pending source confirmation).
- Workday logs for hybrid employees near the state line.

## Sources

| Source | Read on |
| --- | --- |
| M.S. 289A.08 subd. 7 (composite returns): <https://www.revisor.mn.gov/statutes/cite/289A.08> -- statute text archived | 2026-10-28 |
| M.S. 290.92 (withholding, incl. subd. 4a nonresident wages): <https://www.revisor.mn.gov/statutes/cite/290.92> -- statute text archived | 2026-11-02 |
| M.S. 289A.60 (civil penalties): <https://www.revisor.mn.gov/statutes/cite/289A.60> -- statute text archived | 2026-11-02 |
| M.S. chapter 289A table of contents: <https://www.revisor.mn.gov/statutes/cite/289A> -- archived; no sections 289A.06 or 289A.21 exist | 2026-10-31 |
| Form M1 instructions (2026): <https://www.revenue.state.mn.us/sites/default/files/2026-10/m1-inst-26.pdf> | 2026-11-02 |
| Form M4 instructions (2025): <https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf> | 2026-10-31 |
| `mn-income-tax`, `mn-corporate-and-pte`, `mn-payroll` skills -- internal corroboration | 2026-10-25 |

Not yet confirmed: the partnership nonresident-member withholding rule and its exceptions (composite election, $1,000 Minnesota-assignable-income floor, termination distributions) -- not in 290.92's text and 289A.06 does not exist; the DOR P.L. 86-272 solicitation statement; the SCRA military-pay position.
## Talk to a verified accountant



