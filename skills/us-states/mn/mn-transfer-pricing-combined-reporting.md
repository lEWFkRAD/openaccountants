---
name: mn-transfer-pricing-combined-reporting
description: >-
  Use when a Minnesota corporate group has related-party flows and needs the
  2026 answer: combined reporting under M.S. 290.17, the unitary-business
  principle pulling the whole group's income into apportionment, and how
  intercompany transactions disappear in the combination. Trigger on Minnesota
  combined return, M.S. 290.17, unitary business Minnesota, M4 combined,
  water's-edge Minnesota. Minnesota polices connected-party income by forcing
  combination, not an addback schedule. Source-cited draft; 290.17 text
  verified 2026-10-25.
jurisdiction: US-MN
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.2
---

# Minnesota transfer pricing (combined reporting)

## Who this applies to


- C corporations whose trade or business is **part of a unitary business** involving another legal entity subject to Minnesota allocation: combined reporting under M.S. 290.17 (<https://www.revisor.mn.gov/statutes/cite/290.17>, 200 with statute text on 2026-10-25).
- Partnerships/corporations not otherwise subject to the allocation rules but conducting business that is part of a unitary business involving an entity that is: they are pulled into the allocation rules (M.S. 290.17 subd. 3(a), read 2026-10-25).
- Out of scope: stand-alone filers with no unitary affiliates; the individual lane.

## Rates, bands and thresholds


- **Corporate rates:** graduated 4.8% / 9.8% (mn-corporate-and-pte, read 2026-10-25; the 290A.03 rate text renders via JavaScript — the statutory citation of the brackets is not yet confirmed, corroborated internally).
- **Unitary business principle** (M.S. 290.17 subd. 4(a), statute text read 2026-10-25): if a business conducted wholly or partly in Minnesota is part of a unitary business, **the entire income of the unitary business is subject to apportionment** under M.S. 290.191.
- **Combined filing** is required for unitary groups (Form M4 combined schedules); the group's combined apportionable income is taxed at the corporate brackets (mn-corporate-and-pte corroborates the combined-return framework, read 2026-10-25).
- **Intercompany elimination:** in the combination, intercompany dividends, interest, rents and royalties between unitary members eliminate — Minnesota neutralises connected-party shifting through combination (mn-corporate-and-pte, read 2026-10-25).
- **Deduction allocation** follows the unitary income (M.S. 290.17 subd. 3(b), read 2026-10-25): expenses, losses and other deductions allocate along with the item or activity to which they relate.

## The taxable base


- Combined apportionable income of the unitary group, apportioned by the statutory sales factor (M.S. 290.191; mn-corporate-and-pte, read 2026-10-25).
- The unitary principle reaches income of non-Minnesota affiliates that are part of the unitary business (M.S. 290.17 subd. 4(a), read 2026-10-25).

## Deadlines and filing


- Form M4 (combined): 15th day of the 4th month after year end (calendar year: 15 April); 7-month extension available with payment by the original due date (mn-corporate-and-pte, read 2026-10-25).

## Penalties and interest


- Failure to file combined when required: combined tax plus late-file/late-pay penalties and interest (M.S. 289A.21 — not yet confirmed: not machine-verified 2026-10-25; mn-corporate-and-pte corroborates the general framework).

## Cross-border points


- P.L. 86-272 solicitation protection applies to the Minnesota income tax but does not dissolve unitary-group status for the rest of the group (the specific DOR statement is not yet confirmed).
- Federal §482 adjustments do not automatically flow into the Minnesota combination (not yet confirmed).
- No state treaty power.

## Worked examples


**Example 1 — combined apportionment at 9.8%.** A unitary group's combined apportionable income is USD 3,000,000; Minnesota sales factor 30%. Minnesota base: 3,000,000 × 0.30 = 900,000 — above the bracket threshold, so 9.8% applies to the top bracket; simplified single-rate illustration: 900,000 × 0.098 = 88,200 (graduated brackets apply in the real computation — see mn-corporate-and-pte).

```oa-check
name: mn combined apportionment illustration
inputs:
  combined_income: 3000000
  mn_factor: 0.30
  top_rate: 0.098
steps:
  - mn_base: combined_income * mn_factor
  - tax_upper_bound: mn_base * top_rate
expected:
  mn_base: 900000.00
  tax_upper_bound: 88200.00
```

**Example 2 — intercompany royalty neutralised.** A Minnesota manufacturer pays USD 500,000 in royalties to its unitary affiliate in another state. Stand-alone the Minnesota base drops by 500,000; combined, the royalty and the affiliate's matching royalty income eliminate, so combined apportionable income stays 3,000,000 and the Minnesota base stays 900,000 — the royalty moves no Minnesota tax.

```oa-check
name: mn intercompany royalty elimination
inputs:
  royalty: 500000
  combined_income: 3000000
  mn_factor: 0.30
steps:
  - net_effect: royalty - royalty
  - combined_after: combined_income + net_effect
  - mn_base: combined_after * mn_factor
expected:
  net_effect: 0.00
  combined_after: 3000000.00
  mn_base: 900000.00
```

## Ask the client first


- Ownership and control links between affiliates (the unitary-group composition question).
- Whether operations are integrated/interdependent (functional unity) or separate enterprises.
- Whether foreign affiliates are inside the water's-edge boundary.

## Sources

| Source | Read on |
| --- | --- |
| M.S. 290.191 (apportionment): cited within 290.17 text | 2026-10-25 |
| `mn-corporate-and-pte` skill (4.8%/9.8% brackets, combined M4, deadlines) — internal corroboration | 2026-10-25 |

Not yet confirmed: M.S. 290.17 archive (pending); M.S. 290A.03 rate text (JS-rendered); M.S. 289A.21 penalty schedule; the DOR P.L. 86-272 statement; federal §482 interaction.
## Talk to a verified accountant



