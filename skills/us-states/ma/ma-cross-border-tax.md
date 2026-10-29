---
name: ma-cross-border-tax
description: >-
  Use when a nonresident works or invests in Massachusetts, a Massachusetts
  pass-through has nonresident members, or an out-of-state company has
  Massachusetts activity, and the 2026 sourcing, Form 1-NR/PY, composite and
  pass-through-entity (PTE) position is needed. Trigger on Massachusetts
  nonresident return, Form 1-NR/PY, nonresident member withholding,
  PTE election Massachusetts, chapter 63D. Source-cited draft with
  needs-sources caveat on statute pages (404 site-wide 2026-10-25).
jurisdiction: US-MA
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# Massachusetts cross-border tax

## 1. Who this applies to

- Nonresident and part-year individuals with Massachusetts-source income: Form 1-NR/PY ([form page](https://www.mass.gov/forms/massachusetts-nonresident-or-part-year-resident-income-tax-return-form-1-nrpy) — **needs-sources**, 404 site-wide on 2026-10-25; the form and its mechanics are corroborated by the existing `ma-income-tax` skill, which references Form 1-NR).
- Massachusetts pass-throughs with nonresident members (withholding and the PTE election route) (DOR PTE election page — needs-sources).
- Out-of-state corporations with Massachusetts nexus (combined reporting analysis in `ma-transfer-pricing-combined-reporting`).
- Out of scope: residency-domicile disputes (refer); the excise combination mechanics (TP skill).

## 2. Core rules and rates

- **Rates:** flat 5%, plus the 4% surtax on Massachusetts-basis income over the surtax threshold (~$1M) (ma-income-tax, read 2026-10-25).
- **Nonresidents** are taxed on Massachusetts-source income: wages for services performed in Massachusetts, rents from Massachusetts property, and business income apportioned to Massachusetts via the sales factor (Form 1-NR/PY instructions — needs-sources).
- **No de minimis exception** comparable to some states: any Massachusetts-source wage income generally triggers a filing obligation (Form 1-NR/PY — needs-sources; treat the threshold question as unverified until the instructions are re-checked).
- **Pass-through entity (PTE) election** (M.G.L. c.63D — needs-sources): an electing partnership/S-corp pays at the entity level at the corporate rate; qualifying members receive a credit and nonresident members are taxed only at the entity level on that income — the practical composite alternative in Massachusetts (DOR PTE page — needs-sources).
- **Composite returns:** Massachusetts does not operate a general nonresident-composite regime like some states; the PTE election is the standard tool to collapse nonresident-member exposure (needs-sources).

## 3. Base and sourcing

- Wages: sourced to where services are performed; remote workers physically working in Massachusetts have Massachusetts-source wages regardless of employer location (Form 1-NR/PY instructions — needs-sources).
- Business income: apportioned by the single sales factor through the entity return (Form 3 / Form 355 lane).
- Part-year residents: prorate by residency period plus source rules (Form 1-NR/PY — needs-sources).

## 4. Deadlines

- Form 1-NR/PY: 15 April for calendar-year individuals; entity returns (Form 3, Form 355, Form 11-S): 15th day of the 4th month (ma-income-tax / ma-corporate-excise, read 2026-10-25).
- PTE election is made on the entity's timely-filed (including extensions) return for the year (DOR PTE page — needs-sources).

## 5. Penalties and interest

- Late individual filing/payment: penalties plus interest at the federal underpayment rate plus add-on under M.G.L. c.65C — **needs-sources** (404 on 2026-10-25); treat the exact schedule as unverified.

## 6. Treaties and federal overlay

- No state treaty power; US treaties can limit federal tax on some nonresident employment but not the Massachusetts wage sourcing.
- Military personnel stationed in Massachusetts under the SCRA keep domicile elsewhere; Massachusetts-source rules still apply to non-stationed income (needs-sources).
- Credit for taxes paid: Massachusetts residents taxed elsewhere claim the credit for taxes paid to other jurisdictions on Form 1 line 43 mechanics (ma-income-tax, read 2026-10-25).

## 7. Worked examples

**Example 1 — nonresident employee with Massachusetts workdays.** A New York resident earns USD 120,000 total wages, working 20 of 240 annual workdays in Massachusetts. Massachusetts-source wages: 120,000 × 20/240 = 10,000. Massachusetts tax at 5%: 10,000 × 0.05 = 500 (no surtax — below threshold).

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

**Example 2 — PTE election for a nonresident member.** A Massachusetts LLC (taxed as a partnership) allocates USD 80,000 of Massachusetts income to a nonresident member. Without the election the member files Form 1-NR/PY and pays 80,000 × 5% = 4,000. With a valid PTE election the entity pays at the 8.25% corporate rate on the members' distributive share: 80,000 × 0.0825 = 6,600, and the nonresident member owes no individual Massachusetts tax on that income (entity-level cost is higher but removes the individual filing; rate figures from ma-corporate-excise / ma-income-tax, read 2026-10-25; election mechanics needs-sources).

```oa-check
name: ma pte election tradeoff
inputs:
  share: 80000
  ind_rate: 0.05
  entity_rate: 0.0825
steps:
  - individual_tax: share * ind_rate
  - entity_tax: share * entity_rate
  - extra_cost: entity_tax - individual_tax
expected:
  individual_tax: 4000.00
  entity_tax: 6600.00
  extra_cost: 2600.00
```

## 8. Ask the client first

- Where services were physically performed (workday log for remote/hybrid workers).
- Whether the pass-through has already made a PTE election and whether nonresident members consented.
- Whether the client's home state gives a credit that interacts with the Massachusetts liability.

## 9. Sources

- Form 1-NR/PY: <https://www.mass.gov/forms/massachusetts-nonresident-or-part-year-resident-income-tax-return-form-1-nrpy> — **needs-sources** (404 site-wide on 2026-10-25).
- DOR PTE election: <https://www.mass.gov/info-details/passthrough-entity-tax-election> — **needs-sources** (404 on 2026-10-25).
- M.G.L. c.63D (PTE): <https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter63D/Section1> — **needs-sources** (404 on 2026-10-25).
- `ma-income-tax` and `ma-corporate-excise` skills (rates, Form 1-NR reference) — internal corroboration, read 2026-10-25.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
