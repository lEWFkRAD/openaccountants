---
name: az-transfer-pricing
description: >
  Use this skill whenever asked about Arizona transfer pricing and
  related-party rules for tax year 2026 -- the department's §43-941 and
  §43-942 power to distribute, apportion or allocate income among
  commonly-owned or controlled taxpayers, combined-report authority,
  affiliated-group consolidated returns under §43-947, unitary-group
  combined filing on Form 120, and the property/payroll/sales factor
  mechanics (§§43-1141 to 43-1146) that drive intercompany pricing
  outcomes. Trigger on "Arizona transfer pricing", "Arizona combined
  report", "Arizona consolidated return 43-947", "Arizona unitary",
  "Arizona apportionment factors". Source-cited draft; statute texts
  read 2026-10-28.
jurisdiction: US-AZ
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - az-corporate-income-tax
---

# Arizona transfer pricing (related-party allocation, combined/consolidated filing) v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, sources read 28 October 2026 (azleg.gov texts of A.R.S. §§43-941, 43-942, 43-947, 43-1131, 43-1132, 43-1141, 43-1142, 43-1143, 43-1144, 43-1145, 43-1146, plus the AZDOR Corporate Income Tax page and the 2026 Booklet 120/165ES). Arizona has **no dedicated transfer-pricing documentation statute** (no state analogue of federal §482 documentation requirements or a state TP study mandate) -- the enforcement tool is the broad allocation authority in §§43-941/43-942 plus combined-report power.

- **§43-941 (affiliated taxpayers):** two or more "persons, organizations, trades or businesses, whether or not organized in the United States and whether or not affiliated, owned or controlled directly or indirectly by the same interests" -- the department may distribute, apportion or allocate gross income, deductions, credits or allowances where necessary to prevent tax evasion or clearly reflect income (read 2026-10-28: "the department may distribute, apportion or allocate gross income, deductions, credits or allowances between or among such taxpayers, if it determines that such distribution, apportionment or allocation is necessary in order to prevent evasion of taxes or clearly to reflect the income of any such taxpayers"). This reaches foreign-parented groups and non-corporate structures.
- **§43-942 (controlled corporations):** same power for two or more corporations under common ownership/control (read 2026-10-28).
- **§43-947 (consolidation):** the common parent of an "Arizona affiliated group" may elect to consolidate taxable income on or before the original-return due date (with extensions), with written member consents; the election binds succeeding years unless ADOR consents to a change; ADOR may **require** consolidation to prevent tax avoidance (read 2026-10-28).
- **Unitary groups** file combined on Form 120 (AZDOR corporate page, read 2026-10-28).

## Rates, bands and thresholds

There is no separate TP rate; the exposure is the 4.9% corporate rate (§43-1111, read 2026-10-28 -- "For taxable years beginning from and after December 31, 2016, 4.9 per cent of net income"; the 2026 Booklet 120/165ES computes corporate estimated tax "by 4.9%") applied to a re-allocated or apportioned base. The factors that intercompany pricing moves:

| Factor | Statutory mechanic | Source |
|---|---|---|
| Property | original cost; rented property at eight times the net annual rental rate; average value = start/end average | §§43-1141/43-1142 (read 2026-10-28) |
| Payroll | compensation paid in Arizona: service entirely in AZ; incidental out-of-state service; base-of-operations / direction-and-control / residence tie-breakers | §§43-1143/43-1144 (read 2026-10-28) |
| Sales | Arizona sales over total sales; tangible goods sited at delivery/shipment to purchaser regardless of F.O.B. | §§43-1145/43-1146 (read 2026-10-28) |
| Nonbusiness income | rents, royalties, capital gains, interest, dividends allocated under §§43-1134–43-1138 rather than apportioned | §43-1134 (read 2026-10-28) |

## The taxable base

For a unitary or affiliated group, the group's combined/consolidated Arizona taxable income is computed first, then apportioned with group-level factors; intercompany royalties, management fees, and interest generally disappear inside a combined or consolidated return, which is the single biggest planning fact in Arizona TP. Expenses attributable to a foreign corporation that is not itself Arizona-taxable cannot be pushed into the Arizona base (§43-1132(B), read). In audit, ADOR may examine books covering income and expenses both within and without the United States (§43-1132(C), read). Timing: TP adjustments follow the return year; the consolidated election is due with the original return (§43-947(A), read).

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| Consolidated-return election (§43-947) | on or before the original return due date including extensions | §43-947(A) (read 2026-10-28) |
| Combined report when ADOR requires it | as set in the ADOR demand | §43-941(B)/§43-942(B) (read 2026-10-28) |
| Form 120 (combined/consolidated/multistate) | 15th day of the 4th month after year-end | AZDOR corporate page (read 2026-10-28) |

## Penalties and interest

No TP-specific penalty. Reallocations carry the ordinary assessment plus §6621-tracked interest (federal short-term plus three percentage points, compounded annually -- AZDOR interest page, read 2026-10-28). Common failure modes: (1) keeping an intercompany royalty outside a combined group to strip Arizona income while the royalty payer sits in the factor base; (2) assuming the sales factor follows F.O.B. terms -- §43-1146 sites at delivery; (3) remote-work payroll shifting the payroll factor under §43-1144's direction-and-control test.

## Cross-border points

Foreign affiliates: §43-941 reaches non-U.S.-organized entities under common control (read). A foreign corporation not itself Arizona-taxable cannot contribute losses/expenses to the Arizona base (§43-1132(A)-(B), read) unless it joins an Arizona affiliated group (§43-1132(D), read). Federal §482 adjustments flow through federal taxable income and therefore into the Arizona starting point; coordinate with the federal treaty position -- see `az-cross-border`.

## Worked examples

An affiliated group elects consolidation; combined Arizona taxable income $500,000 (hypothetical facts):

```oa-check
name: consolidated group tax 500000
inputs:
  income: 500000
  rate: 0.049
steps:
  - tax: income * rate
  - due: max(50, tax)
expected:
  tax: 24500.00
  due: 24500.00
```

ADOR reallocates 60% of a $250,000 intercompany management fee (hypothetical facts) from an out-of-state affiliate back to the Arizona taxpayer under §43-941; incremental Arizona tax at 4.9%:

```oa-check
name: reallocation of 60 percent of 250000 fee
inputs:
  fee: 250000
  share: 0.6
  rate: 0.049
steps:
  - moved: fee * share
  - tax: moved * rate
expected:
  moved: 150000.00
  tax: 7350.00
```

## Ask the client first

- Is the group unitary (combined Form 120) or an affiliated group (consolidation election under §43-947)? Was the election made with member consents, and is it still binding?
- What intercompany fees, royalties, or interest remain outside the combined/consolidated base, and do they have economic substance in Arizona?
- Where are employees directed and controlled from -- does remote work move the payroll factor (§43-1144)?
- Do goods ship to Arizona customers from out-of-state warehouses (sales factor lands in Arizona under §43-1146)?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| A.R.S. §43-941 -- Allocation; affiliated taxpayers; combined-report power | https://www.azleg.gov/ars/43/00941.htm | 2026-10-28 |
| A.R.S. §43-942 -- Controlled corporations | https://www.azleg.gov/ars/43/00942.htm | 2026-10-28 |
| A.R.S. §43-947 -- Consolidated returns; affiliated group | https://www.azleg.gov/ars/43/00947.htm | 2026-10-28 |
| A.R.S. §43-1111 -- Tax rates for corporations | https://www.azleg.gov/ars/43/01111.htm | 2026-10-28 |
| A.R.S. §43-1132 -- Liability; foreign-corporation expense bar; audit scope | https://www.azleg.gov/ars/43/01132.htm | 2026-10-28 |
| A.R.S. §§43-1141–43-1146 -- Apportionment factors | https://www.azleg.gov/ars/43/01141.htm | 2026-10-28 |
| AZDOR -- Corporate Income Tax (Form 120 combined/consolidated) | https://azdor.gov/business/corporate-income-tax | 2026-10-28 |
| AZDOR -- 2026 Booklet 120/165ES (Form 120/PTE-W) | https://azdor.gov/sites/default/files/document/FORMS_CORPORATE_2026_120_165ESBooklet.pdf | 2026-10-28 |
| AZDOR -- Interest Rates | https://azdor.gov/business/interest-rates | 2026-10-28 |

Not yet confirmed: ADOR audit guidance on intercompany intangibles; current combined-report form mechanics beyond the Form 120 page.

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
