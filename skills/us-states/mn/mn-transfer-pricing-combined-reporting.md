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
last_updated: 2026-11-02
version: 0.3
---

# Minnesota transfer pricing (combined reporting)

## Who this applies to


- C corporations whose trade or business is **part of a unitary business** involving another legal entity subject to Minnesota allocation: combined reporting under M.S. 290.17 (<https://www.revisor.mn.gov/statutes/cite/290.17>, statute text archived 2026-10-31).
- Partnerships/corporations not otherwise subject to the allocation rules but conducting business that is part of a unitary business involving an entity that is: they are pulled into the allocation rules (M.S. 290.17 subd. 1(a), read 2026-10-31: "If a partnership or corporation would not otherwise be subject to the allocation rules, but conducts a trade or business that is part of a unitary business involving another legal entity that is subject to the allocation rules, the partnership or corporation is subject to the allocation rules").
- Out of scope: stand-alone filers with no unitary affiliates; the individual lane.

## Rates, bands and thresholds


- **Corporate rate:** flat 9.8% of taxable income (M.S. 290.06 subd. 1, statute text archived 2026-10-28 and re-read 2026-11-02: "The franchise tax imposed upon corporations shall be computed by applying to their taxable income the rate of 9.8 percent"). There is no graduated corporate bracket schedule.
- **Unitary business principle** (M.S. 290.17 subd. 4(a), statute text read 2026-10-31): "If a trade or business conducted wholly within this state or partly within and partly without this state is part of a unitary business, the entire income of the unitary business is subject to apportionment pursuant to section 290.191."
- **Combined filing** is required for unitary groups (M.S. 290.17 subd. 4(h): each entity that is part of a unitary business "must file combined reports as the commissioner determines"); the group's combined net income is taxed at the flat 9.8% corporate rate (M.S. 290.06 subd. 1).
- **Intercompany elimination:** M.S. 290.17 subd. 4(h) (read 2026-10-31): on the combined reports "all intercompany transactions between entities included pursuant to paragraph (g) must be eliminated" -- Minnesota neutralises connected-party shifting through combination.
- **Deduction allocation** follows the unitary income (M.S. 290.17 subd. 1(b), read 2026-10-31): "Expenses, losses, and other deductions ... must be allocated along with the item or class of gross income to which they are definitely related."

## The taxable base


- Combined apportionable income of the unitary group, apportioned by the statutory sales factor (M.S. 290.191, cross-referenced throughout 290.17 subd. 4, read 2026-10-31).
- The unitary principle reaches income of non-Minnesota affiliates that are part of the unitary business (M.S. 290.17 subd. 4(a), read 2026-10-31).

## Deadlines and filing


- Form M4 combined: "Returns, including short-year returns, must be filed by the due date for filing your federal income tax return" and Minnesota grants an automatic seven-month extension (Form M4 instructions, 2025, read 2026-10-31).

## Penalties and interest


- Failure to file combined when required: the combined tax plus the civil penalty and interest regime of M.S. 289A.60 (civil penalties) and 289A.55 (interest) -- chapter 289A has no section 289A.21 (chapter table of contents read 2026-11-02).

## Cross-border points


- P.L. 86-272 solicitation protection applies to the Minnesota income tax but does not dissolve unitary-group status for the rest of the group.
- Federal §482 adjustments do not automatically flow into the Minnesota combination.
- No state treaty power.

## Worked examples


### Worked example 1: combined apportionment at the flat 9.8% rate

A unitary group's combined apportionable income is USD 3,000,000; Minnesota sales factor 30%. Minnesota base: 3,000,000 × 0.30 = 900,000; the flat corporate rate applies: 900,000 × 0.098 = 88,200 (M.S. 290.06 subd. 1).

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

### Worked example 2: intercompany royalty neutralised

A Minnesota manufacturer pays USD 500,000 in royalties to its unitary affiliate in another state. Stand-alone the Minnesota base drops by 500,000; combined, the royalty and the affiliate's matching royalty income eliminate under M.S. 290.17 subd. 4(h), so combined apportionable income stays 3,000,000 and the Minnesota base stays 900,000 -- the royalty moves no Minnesota tax.

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
| M.S. 290.17 (combined reporting), https://www.revisor.mn.gov/statutes/cite/290.17 | statute text archived 2026-10-31 |
| M.S. 290.191 (apportionment): cited within 290.17 text | 2026-10-25 |
| M.S. 290.06 (corporate franchise tax rate), https://www.revisor.mn.gov/statutes/cite/290.06 | statute text archived 2026-10-28, re-read 2026-11-02 |
| M.S. 289A.60 (civil penalties), https://www.revisor.mn.gov/statutes/cite/289A.60 | statute text archived 2026-11-02 |
| M.S. chapter 289A table of contents, https://www.revisor.mn.gov/statutes/cite/289A | archived 2026-10-31; no section 289A.21 exists |
| Form M4 instructions (2025), https://www.revenue.state.mn.us/sites/default/files/2026-07/m4-inst-25.pdf | read 2026-10-31 |
| `mn-corporate-and-pte` skill (combined M4 framework) -- internal corroboration | 2026-10-25 |

Not yet confirmed: the DOR P.L. 86-272 statement; federal §482 interaction.
## Talk to a verified accountant



