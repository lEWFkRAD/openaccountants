---
name: ne-transfer-pricing
description: >
  Use this skill whenever asked about Nebraska transfer pricing for 2026 —
  how related-party dealings are policed under Revenue Act Chapter 77
  (separate-company filing with related-party addback provisions expected,
  no combined reporting located), and the PTE tax election's effect on
  member-level economics. Trigger on "Nebraska transfer pricing",
  "Nebraska addback", "Nebraska unitary", "Nebraska combined reporting".
  Source-cited draft; Chapter 77 structure and the PTE-tax page verified
  2026-10-28; addback statutes, apportionment mix and filing posture
  needs-sources.
jurisdiction: US-NE
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ne-corporate-income-tax
---

# Nebraska transfer pricing v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## Scope and sources

Nebraska has **no standalone TP documentation regime** located; policing runs through Chapter 77 income allocation and (expected) **related-party addback provisions** for interest/intangibles paid to affiliates. **Source status:** Chapter 77 structure and the PTE-tax page verified 2026-10-28; **addback statute cites, apportionment factor mix, and the separate-company-vs-combined posture — needs-sources** (rule/statute text not fetched this run).

## Who this applies to

- Corporations with intercompany interest, royalties, rents, or management fees paid to affiliates.
- Pass-throughs weighing the PTE election (entity-level tax changes member-level exposure — see `ne-corporate-income-tax.md`).

## Rates, bands and thresholds

No TP-specific rate; exposure rides the corporate rate — a flat **4.55%** for TY2026 (3.99% TY2027+), § 77-2734.02, archived `SRC-US-NE-77-2734.02`; see `ne-corporate-income-tax.md`.

## The taxable base

- Addback of related-party interest/intangible payments (if any) and any economic-substance exceptions are listed under Not yet confirmed.
- Federal §482 adjustments flow through conformity; the NE linkage specifics are listed under Not yet confirmed.

## Deadlines and filing

Rides the corporate calendar (April 15 due date rail, § 77-2768, archived `SRC-US-NE-77-2768`).

## Penalties and interest

The corporate late-filing penalty (5%/month up to 25%) and § 45-104.02 interest are confirmed in `ne-corporate-income-tax.md`; TP-specific additions are listed under Not yet confirmed.

## Cross-border points

Foreign affiliates: no water's-edge statute is asserted; confirmation is listed under Not yet confirmed. State tax is not treaty-protected (standing US principle).

## Worked examples

**Example 1 — interest addback sketch (hypothetical client facts).** $250,000 intercompany interest paid to a low-tax affiliate; if added back with a 30% Nebraska sales factor, incremental Nebraska base $75,000 at the TY2026 flat 4.55% rate (addback posture pending confirmation):

```oa-check
name: NE interest addback sketch
inputs:
  interest: 250000
  factor: 0.30
  rate: 0.0455
steps:
  - added_base: interest * factor
  - tax_at_stake: added_base * rate
expected:
  added_base: 75000.00
  tax_at_stake: 3412.50
```

**Example 2 — arm's-length fee defense (hypothetical client facts).** A management fee currently $400,000 reduced to a supported $320,000 after benchmarking; the $80,000 stays in the Nebraska group at the TY2026 flat 4.55% rate with a 30% factor:

```oa-check
name: NE fee benchmark delta
inputs:
  delta: 80000
  factor: 0.30
  rate: 0.0455
steps:
  - extra_base: delta * factor
  - extra_tax: extra_base * rate
expected:
  extra_base: 24000.00
  extra_tax: 1092.00
```

## Ask the client first

- What intercompany interest/royalty/fee flows exist, and are they benchmarked?
- Would the PTE election change the family's combined Nebraska exposure?
- Any affiliate in a no-income-tax state receiving Nebraska-entity payments?

## Sources

| Source | URL | Read on |
|---|---|---|
| Revenue Act Ch. 77 index | https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=77 | 2026-10-28 |
| DOR PTE tax page | https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet | 2026-10-28 |
| Neb. Rev. Stat. § 77-2734.02 (corporate rate: flat 4.55% TY2026, 3.99% TY2027+) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2734.02 | 2026-10-28 |
| Neb. Rev. Stat. § 77-2768 (due date = federal due date) | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2768 | 2026-10-28 |
| DOR regs Ch. 24 (combined-return rails, interest § 45-104.02) | https://revenue.nebraska.gov/about/legal-information/regulations/chapter-24-corporate-income-tax | 2026-10-28 |

Not yet confirmed: related-party addback statute cites and substance exceptions; apportionment factor mix; the separate-company-vs-combined filing posture (unitary combined filing is confirmed in `ne-corporate-income-tax.md`); TP-specific penalty percentages; water's-edge confirmation; the Ch. 77 index page is cited but not archived this run.

<!-- openaccountants-cta-block -->
---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network
