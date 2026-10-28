---
name: ms-transfer-pricing
description: >
  Use this skill whenever asked about Mississippi transfer pricing and
  combined reporting for 2026 — the Form 83-310 combined report as the
  main related-party policing tool, the 90% estimate rule for combined
  groups, and the absence of a standalone state TP documentation regime.
  Trigger on "Mississippi transfer pricing", "Mississippi combined
  report", "83-310", "Mississippi unitary". Source-cited draft; combined
  report and 90% rule verified on the DOR combined-filing page
  2026-10-28; membership tests, addbacks and documentation requirements
  needs-sources.
jurisdiction: US-MS
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - ms-corporate-income-tax
---

# Mississippi transfer pricing / combined reporting v0.1

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## 1. Scope and sources

Mississippi polices related-party income shifting chiefly through **combined reporting (Form 83-310)** rather than a standalone arm's-length documentation code. **Source status:** the DOR combined-filing page (fetched, verified 2026-10-28) confirms the combined report, combined-group concept, and the **90%-of-current-year estimate requirement** for combined groups. **Ownership thresholds, water's-edge posture, intercompany addbacks, and any documentation requirement — needs-sources** (operative text not fetched).

## 2. Who applies

- Commonly-owned groups meeting Mississippi's combined-report membership tests (**needs-sources** for the test).
- Any filer with intercompany management fees, royalties, interest, or rents moving income out of Mississippi.

## 3. Rates / thresholds

No standalone TP rate; exposure rides the corporate table (5% default above $50,000 — needs-sources, see `ms-corporate-income-tax.md`).

## 4. Base and mechanics

- Combined report aggregates group income, apportions to Mississippi (factor mix **needs-sources**).
- Federal §482 adjustments flow through conformity (verify linkage — **needs-sources**).

## 5. Deadlines, penalties, interest

Combined report rides the corporate calendar; **90% current-year estimates** verified. Penalty percentages **needs-sources**.

## 6. Cross-border notes

Foreign affiliates in a unitary chain: water's-edge treatment **needs-sources**. State tax not treaty-protected (standing US principle).

## 7. Worked examples

**Example 1 — combined income to Mississippi.** Group combined income $1,500,000, Mississippi factor 20%, 5% rate (needs-sources):

```oa-check
name: MS combined apportionment
inputs:
  combined: 1500000
  factor: 0.20
  rate: 0.05
steps:
  - ms_base: combined * factor
  - tax: ms_base * rate
expected:
  ms_base: 300000.00
  tax: 15000.00
```

**Example 2 — royalty shift exposure.** $200,000 intercompany royalty out of the Mississippi member; 20% factor, 5% rate:

```oa-check
name: MS royalty shift
inputs:
  royalty: 200000
  factor: 0.20
  rate: 0.05
steps:
  - ms_base_shift: royalty * factor
  - tax_at_stake: ms_base_shift * rate
expected:
  ms_base_shift: 40000.00
  tax_at_stake: 2000.00
```

## 8. Ask the client

- Is the group commonly owned at combined-report levels? → 83-310 and the 90% estimate rule.
- What intercompany charges run out of Mississippi entities, and are they supported?
- Any foreign affiliates in the chain?

## 9. Sources

1. DOR Combined Filing: https://www.dor.ms.gov/taxes/combined-filing — fetched and verified 2026-10-28.
2. Pre-existing `ms-corporate-income-tax.md` (this pack) for rates.

**Needs-sources:** membership tests, factor mix, addbacks, water's-edge, documentation requirements, penalty percentages.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi combined/TP questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
