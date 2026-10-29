---
name: ne-corporate-income-tax
description: >
  Use this skill whenever asked about Nebraska corporate income tax for
  tax year 2026 — the Revenue Act Chapter 77 corporation tax, Form
  1120N, the pass-through entity (PTE) tax election, and filing
  mechanics. Trigger on "Nebraska corporate income tax", "1120N",
  "4-1120C",
  "Nebraska corporation tax", "Nebraska PTE tax". Source-cited draft;
  Chapter 77 structure, the withholding statute rail (§ 77-3513) and the
  official PTE-tax page verified 2026-10-28; rate (flat 4.55% TY2026 per § 77-2734.02),
  Form 1120N identity, deadlines, estimate thresholds, penalties and PTE mechanics
  corrected against archived official sources 2026-10-28.
jurisdiction: US-NE
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - ne-income-tax
---

# Nebraska corporate income tax v0.2

> **General reference only.** General tax reference for AI-assisted workflows; not reviewed for any specific client's facts. Do not file, pay, or take a position on this alone — use a qualified Nebraska practitioner.

## Scope and sources

Nebraska corporation income tax under the Revenue Act, Chapter 77. **Source status:** all operative claims below are checked against archived official sources (statutes from nebraskalegislature.gov, DOR pages/PDFs) retrieved 2026-10-28 — see Sources. The corporate return is **Form 1120N** (not "4-1120C" — that legacy form number no longer appears on the DOR forms index, `SRC-US-NE-DOR-corp-forms`).

## Who this applies to

- Corporations (and entities taxed as corporations) with Nebraska-source income — Chapter 77 (structure verified).
- **Pass-through entities may elect the Nebraska PTE tax** at the entity level — election is annual and irrevocable for the year, made on the return (box 5) or Form PTET-E; entity pays at the **highest individual rate** (§ 77-2715.03 — 4.55% for TY2026) on Nebraska-apportioned income; partners are then excluded from Nebraska income tax on that income for the year (§§ 77-2727(6), 77-2730, 77-2734.01; DOR PTET page `SRC-US-NE-DOR-ptet`, statute `SRC-US-NE-77-2727`).
- Related-affiliate addback specifics and an explicit "no franchise tax" statement are listed under Not yet confirmed.

## Rates, bands and thresholds

**Nebraska's corporate rate is a flat rate that steps down by taxable year — there are no income bands.** For taxable years beginning on or after January 1, 2026 and before January 1, 2027, the rate is **4.55% on all taxable income** (Neb. Rev. Stat. § 77-2734.02(1)(g), archived: `SRC-US-NE-77-2734.02`). For taxable years beginning on or after January 1, 2027 the rate drops to **3.99%** (§ 77-2734.02(1)(h)).

The commonly cited "5% up to $100,000 / 5.5% above" two-band table is **obsolete** — it dates to LB 86 (2021–2023 biennium) and no longer states current law. Do not use 5.5% for 2026 planning.

## The taxable base

Federal taxable income with Nebraska modifications. **Unitary groups must file a single combined return** (DOR Business Income Tax FAQs, `SRC-US-NE-DOR-biz-faqs`; Form 1120N Schedules III–IV carry combined-group and conversion schedules, `SRC-US-NE-DOR-corp-forms`; combined-return rails in DOR regs Ch. 24, `SRC-US-NE-DOR-chapter24`). Related-affiliate addback specifics are listed under Not yet confirmed.

## Deadlines and filing

- **Return due date:** Nebraska returns are due "on or before the dates prescribed by the laws of the United States for filing federal income tax returns" (Neb. Rev. Stat. § 77-2768, archived: `SRC-US-NE-77-2768`) — for calendar-year 2025 returns the DOR tax calendar shows the **04/15/2026** Form 1040N entry; the DOR 2026 tax calendar confirms the 04/15/2026 Form 1040N entry (`SRC-US-NE-DOR-tax-calendar`). Corporate extension: Form 7004N (DOR regs Ch. 24, `SRC-US-NE-DOR-chapter24`).
- **Estimated payments:** required when the tax reasonably expected to be shown on the return (net of withholding) is **$400 or more** for corporations ($500 or more for individuals) — Neb. Rev. Stat. § 77-2769(2), archived: `SRC-US-NE-77-2769`. The statute sets the $400/$500 thresholds; installment due dates follow the federal schedule per the DOR tax calendar (Form 1120N-ES first installment April 15, 2026).
## Penalties and interest

- **Late-filing penalty:** **5% per month, up to 25%** (DOR Business Income Tax FAQs, guidance: `SRC-US-NE-DOR-biz-faqs`). Interest accrues at the rate in Neb. Rev. Stat. § 45-104.02 (DOR regs Ch. 24, REG-24-043).

## Cross-border points

Nexus: Chapter 77 income-tax nexus provisions + P.L. 86-272 (detailed nexus tests are listed under Not yet confirmed). Nonresident member taxation and PTE withholding rails: see `ne-payroll.md` / `ne-cross-border.md`.

## Worked examples

**Example 1 — $400,000 Nebraska taxable income at the TY2026 flat 4.55% rate (statute § 77-2734.02(1)(g)):**

```oa-check
name: NE corporate 4.55 percent TY2026
inputs:
  income: 400000
  rate: 0.0455
steps:
  - tax: income * rate
expected:
  tax: 18200.00
```

**Example 2 — PTE election comparison (TY2026).** Under § 77-2727(6)(b) (archived: `SRC-US-NE-77-2727`), an electing entity pays tax **at the highest individual rate in § 77-2715.03 — 4.55% for TY2026** (`SRC-US-NE-77-2715.03`) — on Nebraska-apportioned income, and partners are then excluded from Nebraska filing for that year. Pass-through income $200,000 all Nebraska-source: entity-level PTE tax at 4.55% vs member-level at the same 4.55% top marginal rate (member-level is lower in practice if the member's bracket/effective rate is below the top rate; the PTE benefit is the SALT-cap exclusion, not a rate cut):

```oa-check
name: NE PTE vs member level TY2026
inputs:
  income: 200000
  pte_rate: 0.0455
  member_top: 0.0455
steps:
  - pte_tax: income * pte_rate
  - member_tax: income * member_top
  - delta: pte_tax - member_tax
expected:
  pte_tax: 9100.00
  member_tax: 9100.00
  delta: 0.00
```

## Ask the client first

- Is the entity considering the PTE election (SALT-cap workaround posture)? Compare entity vs member rates.
- Related-party interest/dividend payments that trigger Nebraska addbacks?
- Factor presence (payroll, sales, property) creating Chapter 77 nexus?

## Sources

| Source | URL | Read on |
|---|---|---|
| Neb. Rev. Stat. § 77-2734.02 (corporate rate: 4.55% TY2026, 3.99% TY2027+) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2734.02 | 2026-10-28 |
| Neb. Rev. Stat. § 77-2715.03 (individual brackets; top rate 4.55% TY2026) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2715.03 | 2026-10-28 |
| Neb. Rev. Stat. § 77-2768 (due date = federal due date) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2768 | 2026-10-28 |
| Neb. Rev. Stat. § 77-2769 (estimated-tax thresholds $400 corp / $500 individual) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2769 | 2026-10-28 |
| Neb. Rev. Stat. § 77-2727 (PTE election at highest individual rate) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2727 | 2026-10-28 |
| DOR corporation forms index (Form 1120N, 1120-SN, 1120XN, 7004N, 2220N, 1120N-ES) | https://revenue.nebraska.gov/about/forms/corporation-and-s-corporation-income-tax-forms | 2026-10-28 |
| DOR Business Income Tax FAQs (combined unitary filing, 5%/month penalty to 25%, due dates) | https://revenue.nebraska.gov/about/frequently-asked-questions/business-income-tax-faqs | 2026-10-28 |
| DOR Tax Calendar (April 15, 2026 entries) | https://revenue.nebraska.gov/about/tax-calendar | 2026-10-28 |
| DOR regs Ch. 24 (combined-return rails, interest § 45-104.02) | https://revenue.nebraska.gov/about/legal-information/regulations/chapter-24-corporate-income-tax | 2026-10-28 |
| DOR PTET page (election mechanics, Form PTET-E/box 5) | https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet | 2026-10-28 |
| 2026 Nebraska Tax Table draft PDF (individual 4.55% over $79,860) | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/drafts/2026_tax_tables.pdf | 2026-10-28 |

Not yet confirmed: the related-affiliate addback statute cite; an explicit "no franchise tax" statement; the PTE partner-credit vs exclusion interplay in § 77-2730 (statute archived at § 77-2727 only); detailed Chapter 77 nexus tests and P.L. 86-272 protection scope.

<!-- openaccountants-cta-block -->
---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network
