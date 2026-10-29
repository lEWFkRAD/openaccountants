---
name: ca-cross-border
description: >
  Use this skill whenever asked about California cross-border taxation
  for tax year 2026 — what counts as "doing business" in California for
  a foreign or out-of-state corporation (18 CCR §23101), Public Law
  86-272 solicitation protection (15 U.S.C. §381), economic nexus
  thresholds, interstate apportionment with the single sales factor,
  and how state tax sits outside U.S. income-tax treaties. Trigger on
  "California doing business", "California nexus out-of-state",
  "PL 86-272 California", "California cross-border corporation",
  "California economic nexus", "18 CCR 23101". Source-cited draft;
  18 CCR §23101, §25128 and 15 U.S.C. §381 read 2026-10-27.
jurisdiction: US-CA
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ca-corporate-income-tax
  - ca-transfer-pricing
---

# California cross-border taxation v0.1

## 1. Scope and sources

Covers when an out-of-state or foreign corporation becomes subject to
California franchise tax, what federal statutory protection applies,
and how interstate/cross-border income is apportioned. Primary
verified sources this run: 18 CCR §23101 ("Doing Business"-Defined,
via Cornell LII, 200, 2026-10-27), 15 U.S.C. §381 (PL 86-272, 200,
2026-10-27), 18 CCR §25128 (apportionment factors, 200, 2026-10-27).
R&TC §§23101/25128 leginfo pages returned 403 to this agent —
statute cites pending verification.

## 2. Who applies

- Every corporation "doing business" in California is subject to the
  franchise tax; "doing business" means "actively engaging in any
  transaction for the purpose of financial or pecuniary gain or
  profit" (18 CCR §23101 — verified text).
- A corporation incorporated in California is subject to the tax
  regardless of activity (R&TC §23151 — pending verification).
- Economic-nexus thresholds (sales > $750,000 or > 25% of total
  revenue) codify the constitutional standard (R&TC §23101 — pending
  verification; confirm current amounts with FTB).
- Corporations protected by PL 86-272 are not subject to a net-income
  tax measured by income from protected activity (see §7).

## 3. Rates and thresholds

| Item | Amount | Source |
|---|---|---|
| Franchise tax | 8.84%, $800 minimum | FTB tax-rates page (verified 2026-10-27) |
| Economic nexus — sales | > $750,000 (verify current) | R&TC §23101 (pending) |
| Economic nexus — revenue share | > 25% of total (verify current) | R&TC §23101 (pending) |
| Apportionment | Single sales factor (2023+) | 18 CCR §25128 (verified); R&TC §25128 (pending) |

## 4. Base and timing

- A foreign corporation first doing business in California files Form
  100 for that year; the $800 minimum applies from the first year of
  doing business (first-year exemption applies to newly *incorporated*
  entities — verify interaction with FTB Form 100 instructions).
- Sales of tangible personal property are sourced to the purchaser's
  location; sales of services and intangibles use cost of performance
  (R&TC §25134 — pending verification; see `ca-transfer-pricing`).
- Nonbusiness income (rents, royalties, gains) is allocated rather
  than apportioned (R&TC §25123 et seq. — pending verification).

## 5. Deadlines

- Form 100: 15th day of the 4th month after year close (April 15
  calendar year); Form 7004 extends filing only.
- A first-year filer should register with FTB before the due date;
  failure to register does not stop the filing clock.

## 6. Penalties and interest

- FTB 25% late-filing penalty and published interest rates apply to
  foreign/out-of-state corporations identically (FTB
  penalties-and-interest pages, verified 2026-10-27).
- FTB may assess for years before registration; the assessment
  lookback follows the general FTB statute of limitations (verify
  current SOL rules in FTB guidance).

## 7. Cross-border interactions

- **PL 86-272:** shields a corporation whose only California activity
  is "solicitation of orders ... for sales of tangible personal
  property, which orders are sent outside the State for approval or
  rejection" (15 U.S.C. §381 — verified text). California regs note
  such corporations "would not be subject to either a tax measured by
  income ... or the income tax" (18 CCR §23101 — verified text). The
  protection does not extend to services, intangibles, or in-state
  order fulfillment.
- **Treaties:** U.S. income-tax treaties do not apply to California
  state taxes; a foreign parent's treaty status does not shelter the
  California franchise tax.
- **Unitary/worldwide:** water's-edge election controls which foreign
  affiliates enter the combined report (18 CCR §25110 — verified; see
  `ca-transfer-pricing`).
- **Credit for taxes paid:** California residents taxed by other
  states claim a credit under R&TC §17059 (pending verification);
  corporations use the §24011 credit mechanics (pending verification).

## 8. Worked examples

An Ohio corporation with no California property or payroll has
California sales of $900,000 and total sales of $3,000,000; total
revenue $3,000,000. Nexus and tax on $1,000,000 of unitary income:

```oa-check
name: economic nexus and single-factor tax
inputs:
  ca_sales: 900000
  total_sales: 3000000
  income: 1000000
  rate: 0.0884
steps:
  - factor: ca_sales / total_sales
  - apportioned: income * factor
  - tax: apportioned * rate
expected:
  factor: 0.30
  apportioned: 300000.00
  tax: 26520.00
```

The same corporation's only California activity is a salesperson
soliciting orders for goods shipped from Ohio:

```oa-check
name: PL 86-272 protected sales
inputs:
  ca_sales: 900000
  total_sales: 3000000
  income: 1000000
  factor: 0.30
  rate: 0.0884
  protected: 1
steps:
  - apportioned: income * factor
  - tax: apportioned * rate * (1 - protected)
expected:
  apportioned: 300000.00
  tax: 0.00
```

(PL 86-272 removes the net-income tax on protected activity; the
$800 minimum franchise tax question for protected corporations should
be confirmed against current FTB guidance before advising.)

## 9. Ask the client

- What California contacts exist — employees, inventory, agents,
  marketplace sales, remote workers?
- Is the activity pure solicitation of tangible-goods orders shipped
  out of state (PL 86-272), or does it include services, digital
  goods, or in-state fulfillment?
- Where are customers located (destination sourcing) and where are
  services performed (cost of performance)?
- Is the entity incorporated in California (automatic filing)?
- Has FTB registration been completed, and are prior open years a
  concern?

## Sources

1. 18 CCR §23101 "Doing Business"-Defined: https://www.law.cornell.edu/regulations/california/18-CCR-23101 (200 with text, 2026-10-27)
2. 15 U.S.C. §381 (Public Law 86-272): https://www.law.cornell.edu/uscode/text/15/381 (200 with text, 2026-10-27)
3. 18 CCR §25128 (apportionment factors): https://www.law.cornell.edu/regulations/california/18-CCR-25128 (200 with text, 2026-10-27)
4. FTB — Corporation Tax Rates: https://www.ftb.ca.gov/file/business/tax-rates.html (200 with text, 2026-10-27)
5. FTB — Penalties and Interest: https://www.ftb.ca.gov/pay/penalties-and-interest/index.html (200 with text, 2026-10-27)
6. R&TC §23101 (doing business / economic nexus): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23101 (403 to this agent 2026-10-27 — cite pending verification)
7. R&TC §25134 (cost of performance): https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25134 (403 to this agent 2026-10-27 — cite pending verification)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for California nexus and cross-border questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
