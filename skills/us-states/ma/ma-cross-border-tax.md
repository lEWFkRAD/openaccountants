---
name: ma-cross-border-tax
description: >-
  Use when a nonresident works or invests in Massachusetts, a Massachusetts
  pass-through has nonresident members, or an out-of-state company has
  Massachusetts activity, and the 2026 sourcing, Form 1-NR/PY, composite and
  pass-through-entity (PTE) position is needed. Trigger on Massachusetts
  nonresident return, Form 1-NR/PY, nonresident member withholding,
  PTE election Massachusetts, chapter 63D.
jurisdiction: US-MA
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-29
version: 0.2
---

# Massachusetts cross-border tax

## Who this applies to

- Nonresident and part-year individuals with Massachusetts-source income: Form 1-NR/PY (the existing `ma-income-tax` skill references Form 1-NR; the current DOR form page was unreachable from this environment -- see Not yet confirmed below).
- Massachusetts pass-throughs with nonresident members (withholding and the PTE election route) (DOR Elective Pass-through Entity Excise page, archived 2026-10-28).
- Out-of-state corporations with Massachusetts nexus (combined reporting analysis in `ma-transfer-pricing-combined-reporting`).
- Out of scope: residency-domicile disputes (refer); the excise combination mechanics (TP skill).

## Rates, bands and thresholds

- **Individual rates:** flat 5% Part B income tax; the 4% surtax applies to Massachusetts-basis income above the inflation-adjusted threshold (approximately $1.083M for 2025) -- see the `ma-income-tax` skill (Article 44 Amendments to the Massachusetts Constitution; threshold figure listed under Not yet confirmed below).
- **PTE excise rate (ch.63D):** "an excise equal to 5% of a PTE's income that is attributable to qualified members and subject to tax under chapter 62" (DOR Elective Pass-through Entity Excise page, archived 2026-10-28).
- **PTE member credit:** "Qualified members of an electing PTE are eligible for a credit equal to 90% of the member's distributive share of the chapter 63D excise paid by the PTE" (DOR PTE page, archived 2026-10-28).
- **Nonresident filing relief under the PTE election:** "Where the PTE pays the chapter 63D PTE excise, a nonresident member is not required to file a personal income tax return on their own account if (i) they participate in the filing of a nonresident composite return or returns that report all of the nonresident's Massachusetts source income and (ii) they are not subject to the surtax" (DOR PTE page, archived 2026-10-28).
- **Election mechanics:** the election is made annually on the PTE's timely filed Form 3, Form 355S (Schedule S), or Form 2 (Form 63-FI Schedule S for financial-institution S-corps), confirmed by filing Form 63-ELT; it may not be made on an amended return and is irrevocable for the year (DOR PTE page, archived 2026-10-28).
- **Composite returns:** Massachusetts operates a Nonresident Composite Return (Form NRCR) that PTEs may file for participating nonresident members, and a PTE filing Form NRCR may claim the sum of PTE credits for participating members (DOR PTE page, archived 2026-10-28).

## The taxable base

- Wages: sourced to where services are performed; remote workers physically working in Massachusetts have Massachusetts-source wages regardless of employer location (see Not yet confirmed for the instructions citation).
- Business income: apportioned by the single sales factor through the entity return (Form 3 / Form 355 lane; G.L. c.63 §38(c)-(d), archived 2026-10-28).
- Part-year residents: prorate by residency period plus source rules (see Not yet confirmed).

## Deadlines and filing

- Form 1-NR/PY: 15 April for calendar-year individuals; entity returns (Form 3, Form 355, Form 11-S/355S): 15th day of the 4th month (see `ma-income-tax` / `ma-corporate-excise` skills).
- PTE election: made on the entity's timely-filed (including extensions) return for the year; Form 63-ELT must be filed on or before the due date of the PTE's tax return, taking into account valid extensions (DOR PTE page, archived 2026-10-28).

## Penalties and interest

- Late individual filing/payment attracts penalties plus interest; the exact schedule is listed under Not yet confirmed below.

## Cross-border points

- No state treaty power; US treaties can limit federal tax on some nonresident employment but not the Massachusetts wage sourcing.
- Military personnel stationed in Massachusetts under the SCRA keep domicile elsewhere; Massachusetts-source rules still apply to non-stationed income (see Not yet confirmed).
- Credit for taxes paid: Massachusetts residents taxed elsewhere claim the credit for taxes paid to other jurisdictions (see the `ma-income-tax` skill).

## Worked examples

Client facts (wages, workdays, distributive share) are hypothetical; rates are the confirmed 5% individual and 5% ch.63D PTE figures above.

**Example 1 -- nonresident employee with Massachusetts workdays.** A New York resident earns USD 120,000 total wages, working 20 of 240 annual workdays in Massachusetts. Massachusetts-source wages: 120,000 × 20/240 = 10,000. Massachusetts tax at 5%: 10,000 × 0.05 = 500 (no surtax -- below threshold).

```oa-check
name: ma nonresident workday sourcing
inputs:
  total_wages: 120000
  ma_days: 20
  total_days: 240
  rate: 0.05
steps:
  - ma_wages: total_wages * ma_days / total_days
  - ma_tax: ma_wages * rate
expected:
  ma_wages: 10000.00
  ma_tax: 500.00
```

**Example 2 -- PTE election for a nonresident member.** A Massachusetts LLC (taxed as a partnership) allocates USD 80,000 of Massachusetts income to a nonresident member. Without the election the member files Form 1-NR/PY and pays 80,000 × 5% = 4,000. With a valid ch.63D election the entity pays 5% at the entity level on qualified income: 80,000 × 0.05 = 4,000; the member gets a credit equal to 90% of their share of the excise paid (DOR PTE page, archived 2026-10-28). The election's value is administrative (the nonresident may avoid a personal filing when a composite return covers them and they are not subject to the surtax), not a rate cut.

```oa-check
name: ma pte election tradeoff
inputs:
  share: 80000
  ind_rate: 0.05
  entity_rate: 0.05
  credit_pct: 0.9
steps:
  - individual_tax: share * ind_rate
  - entity_tax: share * entity_rate
  - member_credit: entity_tax * credit_pct
expected:
  individual_tax: 4000.00
  entity_tax: 4000.00
  member_credit: 3600.00
```

## Ask the client first

- Where services were physically performed (workday log for remote/hybrid workers).
- Whether the pass-through has already made a PTE election and whether nonresident members consented.
- Whether the client's home state gives a credit that interacts with the Massachusetts liability.

## Sources

| Source | URL | Read on |
|---|---|---|
| DOR -- Elective Pass-through Entity Excise (ch.63D 5% excise, 90% member credit, election mechanics, NRCR interaction) | <https://www.mass.gov/info-details/elective-pass-through-entity-excise> | 2026-10-28 |
| M.G.L. c.63 §38 -- sales-factor apportionment of business income | <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter63/Section38> | 2026-10-28 |

Not yet confirmed: the Form 1-NR/PY form page and its instructions (mass.gov returned 403/404 site-wide from this environment on 2026-10-25 through 2026-10-29) -- including wage-sourcing detail for remote workers, part-year proration, and any de minimis filing threshold; the exact 2026 surtax threshold dollar figure (the `ma-income-tax` skill carries $1,083,150 for TY2025, inflation-adjusted annually); the individual penalty and interest schedule (M.G.L. c.62C pages unreachable); SCRA military-personnel treatment; the full text of M.G.L. c.63D (malegislature.gov chapter page 404 from this environment -- the DOR page above is the archived authority for ch.63D mechanics).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
