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
  chapter 208 text read 2026-10-27.
jurisdiction: US-CT
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ct-corporate-income-tax
---

# Connecticut cross-border taxation v0.1

## 1. Scope and sources

Covers when out-of-state and foreign companies/owners become Connecticut
taxpayers, federal statutory protection, and multistate relief.
Primary verified source: Conn. Gen. Stat. chapter 208 full text
(cga.ct.gov, read 2026-10-27). Chapter 229 individual credit sections
referenced but not re-audited this run.

## 2. Who applies

- **Economic nexus:** any company deriving income from Connecticut
  sources with a "substantial economic presence" in the state —
  purposeful direction of business toward Connecticut judged by the
  frequency, quantity and systematic nature of economic contacts,
  **without regard to physical presence** — to the extent permitted
  by the U.S. Constitution (§12-216a(a) — verified).
- **Foreign corporations:** §12-216a does not reach a foreign
  corporation with no income effectively connected with a U.S. trade
  or business; where ECI exists, gross income is limited to the ECI
  and only ECI-related property/payroll/receipts enter the
  apportionment factors (§12-216a(b) — verified).
- Partnerships/S corps and their members: entity-level PTE election
  or direct member filing (see `ct-s-corporation-tax`).
- Nonresident individuals with CT-source income: CT-104NR regime
  (chapter 229 — needs-sources this run).

## 3. Rates and thresholds

| Item | Amount | Source |
|---|---|---|
| Corporation business tax | 7.5% | §12-214(a)(1) (verified) |
| Surcharge | 10% for 2018–2025 income years; none in current text for 2026 | §12-214(b)(4) (verified) |
| Economic nexus | qualitative standard (no bright-line $ threshold in statute text) | §12-216a(a) (verified) |
| PTE tax (entity alternative) | 6.99% | §12-699(c) (verified) |

## 4. Base and timing

- Apportionment factors for foreign corporations are ECI-only
  (§12-216a(b)(2) — verified).
- Combined group net income aggregates unitary-business income of
  taxable and nontaxable members, world-wide by default (§12-218e,
  §12-218f — verified).
- Returns due the 15th day of the month after the federal due date
  (§12-222(b) — verified).

## 5. Deadlines

| Filing | Calendar-year due date |
|---|---|
| CT-1120 / combined return | April 15 for calendar-year C corps (§12-222(b) — verified) |
| Estimated installments | Months 3/6/9/15th-day pattern, 30/40/10/20 split (§12-242d — verified) |
| Nonresident individual | April 15 pattern (chapter 229 — needs-sources) |

## 6. Penalties and interest

- 10%/$50 failure-to-pay penalty; 1%/month interest; 3-year
  assessment window (§§12-229, 12-233, 12-235 — verified).

## 7. Cross-border interactions

- **PL 86-272:** federal bar on net-income taxes where in-state
  activity is limited to solicitation of orders for tangible personal
  property, sent outside for acceptance/rejection (15 U.S.C. §381 —
  verified via Cornell LII). No protection for services, digital, or
  in-state fulfillment.
- **Treaties:** U.S. income-tax treaties do not limit Connecticut
  state tax; the ECI limitation in §12-216a(b) is statutory, not
  treaty-based (verified text).
- **Credit for taxes paid:** CT residents (individuals) credit taxes
  paid to other states on doubly-taxed income (§12-704 — referenced
  in §12-699(f)(2), verified reference; mechanics needs-sources).
  Corporate credit mechanics not re-audited — needs-sources.
- **PTE as multistate tool:** electing PTE in Connecticut (6.99%) and
  similar regimes elsewhere lets resident members claim the
  §12-699(f)(2) credit for other states' similar entity taxes
  (verified).
- **Composite repeal:** Connecticut's old entity composite election
  (§12-699b) repealed effective 1/1/2024 (verified) — nonresident
  members file individually unless the entity elects PTE.

## 8. Worked examples

A New York corporation (no CT property or payroll) has CT-apportioned
entire net income of $1,500,000 for 2026 under the economic-nexus
statute:

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

The same company's only CT activity is soliciting goods orders
shipped from New York (PL 86-272 protected):

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

## 9. Ask the client

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

1. Conn. Gen. Stat. ch. 208 §§12-214, 12-216a, 12-218e, 12-218f, 12-222, 12-229, 12-233, 12-235: https://www.cga.ct.gov/current/pub/chap_208.htm (200 HTML, read 2026-10-27)
2. Conn. Gen. Stat. ch. 228z §12-699 (PTE): https://www.cga.ct.gov/current/pub/chap_228z.htm (200 HTML, read 2026-10-27)
3. 15 U.S.C. §381 (Public Law 86-272): https://www.law.cornell.edu/uscode/text/15/381 (200 with text, 2026-10-27)
4. Conn. Gen. Stat. ch. 229 (income tax, credits): https://www.cga.ct.gov/current/pub/chap_229.htm (not re-audited this run — cites needs-sources)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Connecticut nexus and cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
