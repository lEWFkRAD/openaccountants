---
name: ct-cross-border
description: >
  Use this skill whenever asked about Connecticut cross-border
  taxation for tax year 2026 — economic nexus without physical
  presence under Conn. Gen. Stat. §12-216a, effectively-connected-
  income limitation for foreign corporations, Public Law 86-272
  solicitation protection (15 U.S.C. §381), combined-reporting
  perimeter for foreign affiliates (§12-218f), credits for taxes paid
  to other states (§12-704), and nonresident member filing after the
  2024 composite repeal. Trigger on "Connecticut nexus", "out-of-
  state corporation Connecticut tax", "PL 86-272 Connecticut",
  "Connecticut economic nexus", "Connecticut cross-border",
  "Connecticut credit for taxes paid". Source-cited draft; CGA
  chapter 208 text read 2026-10-28.
jurisdiction: US-CT
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
depends_on:
  - ct-corporate-income-tax
---

# Connecticut cross-border taxation v0.2

Covers when out-of-state and foreign companies/owners become Connecticut
taxpayers, federal statutory protection, and multistate relief.
Primary sources: Conn. Gen. Stat. chapter 208 full text (cga.ct.gov,
archived and read 2026-10-28), chapter 229 (income tax, credits, archived
same date), chapter 228z (PTE, archived same date), and 15 U.S.C. §381
(Cornell LII, archived same date).

## Who this applies to

- **Economic nexus:** any company deriving income from Connecticut
  sources with a "substantial economic presence" in the state —
  purposeful direction of business toward Connecticut judged by the
  frequency, quantity and systematic nature of economic contacts,
  **without regard to physical presence** — to the extent permitted
  by the U.S. Constitution (§12-216a(a)).
- **Foreign corporations:** §12-216a does not reach a foreign
  corporation with no income effectively connected with a U.S. trade
  or business; where ECI exists, gross income is limited to the ECI
  and only ECI-related property/payroll/receipts enter the
  apportionment factors (§12-216a(b)).
- Partnerships/S corps and their members: entity-level PTE election
  or direct member filing (see `ct-s-corporation-tax`).
- Nonresident individuals with CT-source income: CT-1040NR/PY regime
  (chapter 229 — see Not yet confirmed).

## Rates, bands and thresholds

| Item | Amount | Source |
|---|---|---|
| Corporation business tax | 7.5% of entire net income | §12-214(a)(1) |
| Surcharge | 10% for 2018–2025 income years; none in the current text for income years commencing on or after January 1, 2026 | §12-214(b)(4) |
| Economic nexus | qualitative standard — no bright-line dollar threshold in the statute text | §12-216a(a) |
| PTE tax (entity alternative) | 6.99% of the tax base | §12-699(c): "six and ninety-nine-hundredths per cent multiplied by the tax base" |

## The taxable base

- Apportionment factors for foreign corporations are ECI-only
  (§12-216a(b)(2)).
- Combined group net income aggregates unitary-business income of
  taxable and nontaxable members, world-wide by default (§12-218e,
  §12-218f).

## Deadlines and filing

| Filing | Due date |
|---|---|
| CT-1120 / combined return | the fifteenth day of the month next succeeding the due date of the corresponding federal income tax return, without regard to any extension (§12-222(b)) |
| Estimated installments | fifteenth-day-of-the-third/sixth/ninth/twelfth-month pattern, 30/40/10/20 split (§12-242d) |
| Nonresident individual | see Not yet confirmed (chapter 229 due-date mechanics were not tied out this run) |

## Penalties and interest

- Ten per cent / fifty-dollar failure-to-pay penalty; one per cent per
  month interest; three-year assessment window (§§12-229, 12-233,
  12-235).

## Cross-border points

- **PL 86-272:** federal bar on net-income taxes where in-state
  activity is limited to solicitation of orders for tangible personal
  property, sent outside for acceptance/rejection (15 U.S.C. §381).
  No protection for services, digital, or in-state fulfillment.
- **Treaties:** U.S. income-tax treaties do not limit Connecticut
  state tax; the ECI limitation in §12-216a(b) is statutory, not
  treaty-based.
- **Credit for taxes paid:** CT residents (individuals) may claim a
  credit against the chapter 229 income tax for income tax paid to a
  qualifying jurisdiction (another U.S. state, its local governments,
  or DC) on income also taxed by Connecticut (§12-704). See
  Not yet confirmed for the mechanics not tied out this run.
- **PTE as multistate tool:** electing PTE in Connecticut (6.99%) and
  similar regimes elsewhere lets resident members claim the §12-699(f)(2)
  credit for other states' substantially similar entity taxes.
- **Composite repeal:** Connecticut's old entity composite election
  (§12-699b) "is repealed, effective January 1, 2024" (chapter 228z) —
  nonresident members file individually unless the entity elects PTE.

## Worked examples

Hypothetical facts. A New York corporation (no CT property or payroll)
has CT-apportioned entire net income of $1,500,000 for 2026 under the
economic-nexus statute:

```oa-check
name: economic nexus tax 2026
inputs:
  apportioned_income: 1500000
  rate: 0.075
steps:
  - tax: apportioned_income * rate
expected:
  tax: 112500.00
```

The same hypothetical company, whose only CT activity is soliciting
goods orders shipped from New York (PL 86-272 protected):

```oa-check
name: PL 86-272 protected
inputs:
  apportioned_income: 1500000
  rate: 0.075
  protected: 1
steps:
  - tax: apportioned_income * rate * (1 - protected)
expected:
  tax: 0.00
```

## Ask the client first

- What CT contacts exist — remote workers, clients, marketplace
  sales, data/property — and do they form a "systematic" economic
  presence?
- Is the activity pure tangible-goods solicitation (PL 86-272) or
  services/digital/fulfillment?
- For foreign parents: is there U.S. ECI, and are factor computations
  ECI-only?
- Are resident members tracking §12-704 credits for taxes paid to
  other states, including other states' PTE taxes?
- Is the group's combined perimeter (world-wide vs water's-edge)
  documented?

## Sources

| Source | URL | Read on |
|---|---|---|
| Conn. Gen. Stat. ch. 208 §§12-214, 12-216a, 12-218e, 12-218f, 12-222, 12-229, 12-233, 12-235, 12-242d | https://www.cga.ct.gov/current/pub/chap_208.htm | 2026-10-28 |
| Conn. Gen. Stat. ch. 228z §12-699 (PTE) | https://www.cga.ct.gov/current/pub/chap_228z.htm | 2026-10-28 |
| Conn. Gen. Stat. ch. 229 §12-704 (resident credit for income tax paid to qualifying jurisdiction) | https://www.cga.ct.gov/current/pub/chap_229.htm | 2026-10-28 |
| 15 U.S.C. §381 (Public Law 86-272) | https://www.law.cornell.edu/uscode/text/15/381 | 2026-10-28 |

Not yet confirmed: nonresident individual filing and due-date mechanics under chapter 229 (Form CT-1040NR/PY) — the chapter 229 text was archived but the specific nonresident return provisions were not tied out this run; corporate credit-for-taxes-paid mechanics beyond the resident individual credit in §12-704.

## Talk to a verified accountant

**Talk to a verified accountant** — for Connecticut nexus and cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

This skill is a source-cited draft; no accountant has reviewed it. Verify
figures against the cited primary sources or with a licensed Connecticut
professional before relying on them.
