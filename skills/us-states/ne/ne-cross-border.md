---
name: ne-cross-border
description: >
  Use this skill whenever asked about Nebraska cross-border individual
  taxation for 2026 — nonresident and part-year taxation of
  Nebraska-source income, the pass-through entity (PTE) tax election as a
  collection and SALT-posture rail for nonresident members, credit for
  taxes paid to other states, and inheritance tax administration.
  Trigger on "Nebraska nonresident", "Nebraska part-year", "Nebraska PTE
  election", "Nebraska credit for taxes paid", "Nebraska inheritance
  tax". Source-cited draft; PTE-tax page and withholding rails verified
  2026-10-28; nonresident schedule mechanics, credit statute and
  inheritance-tax figures needs-sources.
jurisdiction: US-NE
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ne-income-tax
  - ne-payroll
---

# Nebraska cross-border taxation v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## Scope and sources

How Nebraska reaches nonresidents and how residents recover other-state tax. **Source status:** verified 2026-10-28 — the DOR individual income-tax page resolves, the **PTE tax page** is official, and withholding rails (§ 77-3513, Circular EN) are verified. **Nonresident return/schedule mechanics, the credit-for-taxes-paid statute, reciprocity, and inheritance-tax rates/thresholds — needs-sources** (inheritance tax is county-administered per pre-existing `ne-income-tax.md` notes; not re-verified this run).

## Who this applies to

- **Nonresidents with Nebraska-source income** — wages for Nebraska workdays, Nebraska business income, rents/gains; nonresident/part-year return mechanics are listed under Not yet confirmed.
- **Part-year residents** — split-period filing (mechanics listed under Not yet confirmed).
- **Nebraska residents paying other-state tax** — a credit for taxes paid to other states is expected; the statute is listed under Not yet confirmed.
- **Nonresident members of NE pass-throughs** — PTE tax election moves the liability to entity level (page verified).

## Rates, bands and thresholds

Graduated individual schedule: the TY2026 top rate is **4.55%** (brackets 2.46%/3.51%/4.55%, § 77-2715.03, archived `SRC-US-NE-77-2715.03`; see `ne-income-tax.md`). The PTE tax is levied **at the highest individual rate — 4.55% for TY2026** (§ 77-2727(6), archived `SRC-US-NE-77-2727`; DOR PTET page `SRC-US-NE-DOR-ptet`).

## The taxable base

- Workday sourcing for wages (convenience-of-the-employer rule status is listed under Not yet confirmed).
- PTE election: entity-level tax at the highest individual rate; partners are excluded from Nebraska income tax on that income for the year (§ 77-2727(6), archived `SRC-US-NE-77-2727`).
- No Nebraska exit tax is asserted; confirmation is listed under Not yet confirmed.

## Deadlines and filing

Individual returns are due on the federal due date (April 15, 2026 for TY2025), per the same Chapter 77 due-date rail confirmed in `ne-corporate-income-tax.md` (§ 77-2768, archived `SRC-US-NE-77-2768`; DOR tax calendar `SRC-US-NE-DOR-tax-calendar`). PTE election deadlines are listed under Not yet confirmed.

## Cross-border points

- Colorado/Nebraska and Iowa/Nebraska border workers: check the other state's nonresident filing and credits (see those packs).
- Inheritance tax (county-administered) affects nonresident decedents with Nebraska property; rates and exemptions are listed under Not yet confirmed.

## Worked examples

**Example 1 — nonresident ratio (hypothetical client facts).** Nonresident, total income $220,000, Nebraska-source $55,000; hypothetical full-return tax $11,000:

```oa-check
name: NE nonresident ratio
inputs:
  total_income: 220000
  ne_source: 55000
  tax_on_total: 11000
steps:
  - ratio: ne_source / total_income
  - ne_tax: tax_on_total * ratio
expected:
  ne_tax: 2750.00
```

**Example 2 — PTE election at entity level (hypothetical client facts).** Nebraska pass-through income $300,000, PTE rate 4.55% (TY2026 highest individual rate, § 77-2727(6) / § 77-2715.03):

```oa-check
name: NE PTE election tax
inputs:
  income: 300000
  pte_rate: 0.0455
steps:
  - pte_tax: income * pte_rate
expected:
  pte_tax: 13650.00
```

## Ask the client first

- Workdays physically in Nebraska vs home state — and does the home state credit Nebraska tax?
- Is the pass-through considering the PTE election for SALT-cap posture? Election deadline missed?
- Out-of-state decedent owning Nebraska real property — inheritance tax exposure?

## Sources

| Source | URL | Read on |
|---|---|---|
| DOR PTE tax page (election mechanics, entity-level tax) | https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet | 2026-10-28 |
| DOR individual income tax page | https://revenue.nebraska.gov/individuals/individual-income-tax | 2026-10-28 |
| Neb. Rev. Stat. § 77-2715.03 (individual rate schedule; TY2026 top 4.55%) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2715.03 | 2026-10-28 |
| Neb. Rev. Stat. § 77-2727 (PTE election at highest individual rate; partner exclusion) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2727 | 2026-10-28 |
| Neb. Rev. Stat. § 77-2768 (due date = federal due date) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2768 | 2026-10-28 |
| DOR Tax Calendar (April 15, 2026 entries) | https://revenue.nebraska.gov/about/tax-calendar | 2026-10-28 |

Not yet confirmed: the nonresident/part-year return and Schedule III mechanics; the credit-for-taxes-paid statute; reciprocity; the convenience-of-the-employer rule; the PTE election deadline window and member-credit interplay in § 77-2730; inheritance-tax rates, thresholds and exemptions; exit-tax confirmation.

<!-- openaccountants-cta-block -->
---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network
