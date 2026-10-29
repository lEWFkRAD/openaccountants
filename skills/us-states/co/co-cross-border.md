---
name: co-cross-border
description: >
  Use this skill whenever asked about Colorado cross-border taxation
  for tax year 2026 — when an out-of-state or foreign corporation is
  taxed by Colorado, Public Law 86-272 solicitation protection (15
  U.S.C. §381), receipts-factor sourcing of multistate sales, credits
  for taxes paid to other states, and nonresident partner obligations
  under the composite regime. Trigger on "Colorado nexus", "Colorado
  doing business", "PL 86-272 Colorado", "Colorado cross-border",
  "out-of-state corporation Colorado tax", "Colorado credit for taxes
  paid". Source-cited draft; DR 0106 instructions and 15 U.S.C. §381
  read 2026-10-27.
jurisdiction: US-CO
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - co-corporate-income-tax
---

# Colorado cross-border taxation v0.1

## 1. Scope and sources

Covers when out-of-state and foreign corporations/owners become
Colorado taxpayers, federal statutory protection, and multistate
relief. Verified sources this run: DR 0106 instructions (2025 PDF,
2026-10-27 — sourcing rules, 100%-Colorado rule, composite regime),
15 U.S.C. §381 (PL 86-272, Cornell LII, 200, 2026-10-27). C.R.S.
nexus/credit sections were 403/404 this run — flagged pending.

## 2. Who applies

- Colorado taxes corporations with Colorado-source income; the
  "doing business"/taxable nexus standard
  is C.R.S. §39-22-103 (pending verification; economic nexus commonly
  cited at $100,000 Colorado sales — verify with DOR).
- Nonresident partners/shareholders of Colorado-pass-through income
  are taxed through the composite return or SALT Parity credit
  mechanics (verified DR 0106 text — see `co-s-corporation-tax`).
- Colorado residents with out-of-state income claim a credit for
  taxes paid to other states (C.R.S. §39-22-105 — pending
  verification).

## 3. Rates and thresholds

| Item | Amount | Source |
|---|---|---|
| Corporate / individual rate | 4.4% flat | Verified DR 0106 (0.044) |
| Economic nexus (sales) | commonly cited $100,000 threshold | C.R.S. §39-22-103 (pending) — verify with DOR |
| Apportionment | receipts factor | C.R.S. §39-22-303.6 (verified reference) |

## 4. Base and timing

- Colorado-source income: property located in Colorado, business
  carried on in Colorado, and intangibles employed in a Colorado
  business (Rule 39-22-109(3) — verified reference on DR 0106).
- Entity with no activity outside Colorado sources 100% of income to
  Colorado (verified DR 0106 text).
- First-year filers register with DOR; filing obligations begin with
  the first year of nexus.

## 5. Deadlines

- DR 0107 / DR 0106: 15th day of the 4th month (April 15 calendar
  year); automatic 6-month filing extension, no payment extension
  (verified DR 0106 text).
- Nonresident individual DR 0104: April 15 pattern (verified Book 104
  text).

## 6. Penalties and interest

- Same delinquent-payment penalty (greater of $5 or 5% + 0.5%/month;
  90% shield) and DR 0233 estimated penalty (verified DR 0106 text).
- Interest under C.R.S. §39-21-118 (pending verification).

## 7. Cross-border interactions

- **PL 86-272:** bars a net-income tax where the only in-state activity
  is solicitation of orders for tangible personal property sent
  outside the state for approval/rejection (15 U.S.C. §381 — verified
  text). No protection for services, intangibles, or in-state
  fulfillment.
- **Treaties:** U.S. income-tax treaties do not limit Colorado state
  tax.
- **Credit for taxes paid:** Colorado residents pay Colorado tax on
  worldwide income and credit taxes paid to other states on
  double-taxed income (C.R.S. §39-22-105 — pending verification).
- **SALT Parity vs other states:** Colorado's entity-level election
  interacts with other states' PTE regimes for multistate groups —
  coordinate elections state by state.
- **Real-estate withholding:** nonresidents selling Colorado real
  estate face DR 1079 withholding (verified DR 0106 reference).

## 8. Worked examples

A Texas corporation with no Colorado property or payroll has Colorado
receipts of $1,200,000 and total receipts of $6,000,000; unitary
income $2,000,000:

```oa-check
name: receipts factor cross-border tax
inputs:
  co_receipts: 1200000
  total_receipts: 6000000
  income: 2000000
  rate: 0.044
steps:
  - factor: co_receipts / total_receipts
  - apportioned: income * factor
  - tax: apportioned * rate
expected:
  factor: 0.20
  apportioned: 400000.00
  tax: 17600.00
```

The same corporation's only Colorado activity is solicitation of
goods orders shipped from Texas (PL 86-272 protected):

```oa-check
name: PL 86-272 protected
inputs:
  co_receipts: 1200000
  total_receipts: 6000000
  income: 2000000
  factor: 0.20
  rate: 0.044
  protected: 1
steps:
  - apportioned: income * factor
  - tax: apportioned * rate * (1 - protected)
expected:
  apportioned: 400000.00
  tax: 0.00
```

## 9. Ask the client

- What Colorado contacts exist — employees, agents, inventory,
  marketplace sales, remote workers?
- Is the activity pure solicitation of tangible-goods orders (PL
  86-272) or does it include services/digital/fulfillment?
- Are nonresident owners aware of composite/SALT Parity mechanics and
  their own DR 0104 credits?
- Is the client a Colorado resident with out-of-state tax paid →
  credit tracking?

## Sources

1. Colorado DOR — Form DR 0106 instructions (2025): https://tax.colorado.gov/sites/tax/files/documents/DR0106_2025.pdf (200 PDF, 2026-10-27)
2. Colorado DOR — Book 104 (2025): https://tax.colorado.gov/sites/tax/files/documents/Book104_2025.pdf (200 PDF, 2026-10-27)
3. 15 U.S.C. §381 (Public Law 86-272): https://www.law.cornell.edu/uscode/text/15/381 (200 with text, 2026-10-27)
4. C.R.S. §39-22-103 (taxable income of foreign corporations): https://leg.colorado.gov (403/404 this run — cite pending verification)
5. C.R.S. §39-22-105 (credit for taxes paid to other states): https://leg.colorado.gov (403/404 this run — cite pending verification)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Colorado nexus and cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
