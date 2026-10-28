---
name: ks-cross-border
description: >
  Use this skill whenever asked about Kansas cross-border taxation for tax
  year 2026 — part-year and nonresident Kansas filing (Form K-40 with
  Schedule S allocation), the resident-worldwide-plus-credit structure,
  no reciprocity with neighboring states, no exit tax, and the
  resident-employee withholding rule that follows Kansas residents out of
  state. Trigger on "Kansas nonresident", "Kansas part-year", "Schedule S
  Kansas", "K-40PN", "Kansas reciprocity", "moving to Kansas".
  Source-cited draft; KDOR withholding-residence rule verified 2026-10-28;
  form IDs and credit mechanics needs-sources (statute JS-only).
jurisdiction: US-KS
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ks-income-tax
---

# Kansas cross-border taxation v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 2026-10-28. Covers Kansas exposure for nonresidents, part-year residents, and Kansans working out of state. **Source status:** the KDOR Withholding page (residence-based withholding rule) was verified 2026-10-28; **K.S.A. 79-32-150 (nonresident returns) and the credit statutes sit behind a JS-only legislature site**, so form IDs (K-40PN vs K-40 + Schedule S Part B), allocation detail, and credit mechanics are **needs-sources**. The pre-existing `ks-income-tax.md` skill already flags Schedule S Part B as the nonresident path — this skill routes to it.

## 2. Who applies

- **Kansas residents**: taxed on worldwide income regardless of where services are performed; the KDOR Withholding page confirms employers must withhold Kansas tax for Kansas residents "performing services inside or outside of Kansas" (verified 2026-10-28).
- **Nonresidents**: taxed on Kansas-source income; withholding required by Kansas employers (same verified page).
- **Part-year residents**: split-year treatment via allocation on Schedule S (form detail **needs-sources**).
- **Entities**: corporations with Kansas-source income file K-120 (see `ks-corporate-income-tax`).

## 3. Structure and rates

| Item | Rule | Source status |
|---|---|---|
| Resident base | worldwide income, Kansas rates (5.20%–5.58% per `ks-income-tax`, needs-sources for 2026) | structure verified via withholding rule; rates needs-sources |
| Nonresident base | Kansas-source income, allocated via Schedule S Part B | **needs-sources** (statute JS-only) |
| Credit for taxes paid to other states | resident credit for tax lawfully paid to the work state; prevents double taxation | **needs-sources** for citation and ordering |
| Reciprocity | **none** — Kansas has no reciprocity agreement with MO, NE, OK, CO, or any neighbor | structural; needs-sources for citation |
| Exit tax | **none** — Kansas imposes no departure/exit tax on moving out | structural, low risk |
| Source rules for remote work | income sourced where services performed; Kansas resident remote workers still Kansas-withheld | verified via KDOR withholding page |

## 4. Deadlines

- K-40 (with or without Schedule S): April 15 for calendar-year filers; federal extension honored (KDOR pages verified for corporate analog; individual citation **needs-sources**).
- Nonresident employers' withholding remittances follow the payroll calendar (see `ks-payroll`).

## 5. Penalties and interest

- Standard K.S.A. 79-32 late-filing/late-payment regime — tiers **needs-sources**.
- Dual-residency disputes (two states claiming residence) require negotiated credits or litigation; Kansas has no special penalty for the dispute itself.

## 6. Cross-border interactions

- **KS resident working in Missouri** (classic KC metro pattern): no reciprocity → MO withholds nonresident tax; Kansas taxes worldwide and credits the MO tax lawfully paid. Net Kansas cost = Kansas tax − credit (capped at Kansas tax on the same income).
- **Nonresident working in Kansas**: Kansas withholds and taxes; home state credits Kansas tax (most states do; verify home-state credit).
- **Military**: MMRA resident-retention rules apply federally; Kansas follows — detail **needs-sources**.
- **No Kansas worldwide-unitary extension for individuals** — state layer is source/credit based.

## 7. Worked examples

**Example 1 — Kansas resident commuting to Missouri (no reciprocity):** Kansas tax on worldwide income $4,200; Missouri nonresident tax $3,800. Kansas credits the MO tax.

```oa-check
name: KS resident MO commuter credit
inputs:
  ks_tax: 4200
  mo_tax: 3800
steps:
  - credit: min(mo_tax, ks_tax)
  - ks_net: ks_tax - credit
  - combined: mo_tax + ks_net
expected:
  credit: 3800
  ks_net: 400
  combined: 4200
```

The household pays the higher of the two states' tax on the same wages — here Kansas's $4,200 total, split $3,800 MO + $400 Kansas.

**Example 2 — nonresident working in Kansas:** Missouri resident earns in Kansas; Kansas tax $2,600; home-state tax on the same income $3,100 with a full credit for Kansas tax.

```oa-check
name: Nonresident KS work home-state credit
inputs:
  ks_tax: 2600
  home_tax: 3100
steps:
  - credit: min(ks_tax, home_tax)
  - home_net: home_tax - credit
  - combined: ks_tax + home_net
expected:
  credit: 2600
  home_net: 500
  combined: 3100
```

## 8. Ask the client

- Where were services physically performed each day? (drives source)
- Kansas residence status for the whole year or part of it? (drives K-40 vs Schedule S split)
- Employer withholding: was Kansas withheld for a resident working out of state (required) or for a nonresident working in Kansas (required)?
- Home/work state credit rules — no reciprocity means credits, not exemptions, do the double-tax relief.

## 9. Sources

- KDOR Withholding (residence-based withholding, nonresident rule): https://www.ksrevenue.gov/bustaxtypeswh.html — read 2026-10-28, text verified.
- K.S.A. 79-32-150 (nonresident returns): https://www.kslegislature.org/li/b2025_26/statutes/2025_79-32-150/ — HTTP 200, JS shell; **needs-sources**.
- Pre-existing `ks-income-tax.md` (Schedule S Part B routing, rate structure): repo file, read 2026-10-28.

**Needs-sources:** K-40PN vs K-40+Schedule S form routing, resident-credit statute citation and ordering, part-year allocation detail, military provisions, 2026 rate confirmation.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Kansas cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
