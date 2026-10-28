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

## 1. Scope and sources

Nebraska has **no standalone TP documentation regime** located; policing runs through Chapter 77 income allocation and (expected) **related-party addback provisions** for interest/intangibles paid to affiliates. **Source status:** Chapter 77 structure and the PTE-tax page verified 2026-10-28; **addback statute cites, apportionment factor mix, and the separate-company-vs-combined posture — needs-sources** (rule/statute text not fetched this run).

## 2. Who applies

- Corporations with intercompany interest, royalties, rents, or management fees paid to affiliates.
- Pass-throughs weighing the PTE election (entity-level tax changes member-level exposure — see `ne-corporate-income-tax.md`).

## 3. Rates / thresholds

No TP-specific rate; exposure rides the corporate table (5.5% default above $100,000 — needs-sources).

## 4. Base and mechanics

- Expected addback of related-party interest/intangible payments unless economic-substance exceptions met — **needs-sources**.
- Federal §482 adjustments flow through conformity (verify linkage — **needs-sources**).

## 5. Deadlines, penalties, interest

Rides the corporate calendar; percentages **needs-sources**.

## 6. Cross-border notes

Foreign affiliates: no water's-edge statute located (separate-company posture makes it moot pending confirmation) — **needs-sources**. State tax not treaty-protected (standing US principle).

## 7. Worked examples

**Example 1 — interest addback sketch.** $250,000 intercompany interest paid to a low-tax affiliate; if added back with a 30% Nebraska sales factor, incremental Nebraska base $75,000 at 5.5% (posture needs-sources):

```oa-check
name: NE interest addback sketch
inputs:
  interest: 250000
  factor: 0.30
  rate: 0.055
steps:
  - added_base: interest * factor
  - tax_at_stake: added_base * rate
expected:
  added_base: 75000.00
  tax_at_stake: 4125.00
```

**Example 2 — arm's-length fee defense.** A management fee currently $400,000 reduced to a supported $320,000 after benchmarking; the $80,000 stays in the Nebraska group at 5.5% with a 30% factor:

```oa-check
name: NE fee benchmark delta
inputs:
  delta: 80000
  factor: 0.30
  rate: 0.055
steps:
  - extra_base: delta * factor
  - extra_tax: extra_base * rate
expected:
  extra_base: 24000.00
  extra_tax: 1320.00
```

## 8. Ask the client

- What intercompany interest/royalty/fee flows exist, and are they benchmarked?
- Would the PTE election change the family's combined Nebraska exposure?
- Any affiliate in a no-income-tax state receiving Nebraska-entity payments?

## 9. Sources

1. Revenue Act Ch. 77 index: https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=77 — fetched 2026-10-28.
2. DOR PTE tax: https://revenue.nebraska.gov/tax-credits/nebraska-pass-through-entity-tax-ptet — verified 2026-10-28.

**Needs-sources:** addback cites, substance exceptions, apportionment mix, filing posture, penalty percentages.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Nebraska TP questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
