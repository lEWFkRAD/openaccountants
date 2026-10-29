---
name: fl-transfer-pricing
description: >
  Use this skill whenever asked about Florida transfer pricing and
  related-party adjustments for tax year 2026 — affiliated-group
  consolidated filing under s. 220.131 Fla. Stat., the absence of a
  standalone state transfer-pricing documentation regime, the
  sales-factor apportionment election for qualified capital expenditures
  under s. 220.153, the state-income-tax addback under s. 220.13(1)(a)1.a.,
  and the 50/25/25 statutory apportionment fraction under s. 220.15.
  Trigger on "Florida transfer pricing", "Florida consolidated return",
  "Florida affiliated group", "220.131", "Florida addback".
  ALWAYS load us-tax-workflow-base first.
version: 0.2
jurisdiction: US-FL
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
depends_on:
  - fl-corporate-income-tax
---

# Florida transfer pricing / affiliated-group overlay, tax year 2026

> **Source-cited draft.** Built from ss. 220.11, 220.13, 220.15, 220.131 and 220.153 Fla. Stat. (2026) and the Florida Department of Revenue corporate income tax page, read on 2026-10-28. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

## Who this applies to

Any "taxpayer" under Ch. 220 — a C-corporation or other entity taxed federally as a corporation conducting business in Florida, earning Florida income, or a Florida resident or citizen shareholder of such an entity (s. 220.11(1)).

**Parent companies of affiliated groups.** Florida permits (does not mandate) a consolidated Florida return for groups that filed a federal consolidated return, with every member consenting (s. 220.131(1)).

**Groups that do not consolidate in Florida** still file separate company returns with factor-based apportionment — intercompany transactions then sit inside each entity's apportionment factors, and related-party pricing affects both the numerator (Florida sales factor) and each entity's taxable income.

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| Corporate income tax rate | 5.5% of net income for taxable years beginning on or after 1/1/2022 | s. 220.11(2)(a): "an amount equal to 5 1/2 percent of the taxpayer's net income for the taxable year"; FDOR corporate income tax page: "On or After 1/1/2022 ... 5.5%" |
| Alternative rate for taxpayers computing income under s. 220.13(2)(k) | 3.3% of net income | s. 220.11(3): "an amount equal to 3.3 percent of the taxpayer's net income for the taxable year" |
| Apportionment fraction | Sales factor 50%, property factor 25%, payroll factor 25% | s. 220.15(1) |
| State income tax addback | State/local income taxes deducted federally are added to taxable income in computing adjusted federal income | s. 220.13(1)(a)1.a. |
| Florida consolidated return | Elective by the parent of an affiliated group; every member must consent; the group must have filed a federal consolidated return for the same year with identical members | s. 220.131(1)(a)-(c): "Each member of the group consents to such filing by specific written authorization at the time the consolidated return is filed"; "The affiliated group so filing under this code has filed a consolidated return for federal income tax purposes for the same taxable year"; "composed of the identical component members" |
| Sales-factor apportionment election (qualified capital expenditures) | A taxpayer (other than a financial organization or bank) making qualified capital expenditures in Florida within a 2-year period may apply for apportionment by sales factor | s. 220.153(2): "doing business within and without this state, who applies and demonstrates to the Department of Commerce that, within a 2-year period beginning on or after July 1, 2011, it has made qualified capital expen[ditures]" |

## The taxable base

The base is adjusted federal income (s. 220.13) apportioned by the 50/25/25 fraction (s. 220.15). Florida has **no standalone transfer-pricing documentation regime** — no state version of IRC s. 482 with its own penalty or contemporaneous-documentation requirement. Related-party economics enter the Florida base through the statutory levers: the elective consolidated return (s. 220.131), the state-income-tax addback (s. 220.13(1)(a)1.a.), the factors themselves, and the sales-factor election for qualified capital expenditures (s. 220.153).

Note on s. 220.153: it is titled "Apportionment by sales factor" and is an election for taxpayers making qualified capital expenditures in Florida (acquisition of real property, additions, replacements, major repairs, renovations materially extending useful life, and furniture/equipment for a new or improved facility; expenditures to acquire an existing business or land/buildings in excess of $125 million do not qualify). It is not a general "special apportionment on distortion" provision.

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Florida consolidated-return election | Not later than the due date for filing the return for the taxable year, including extensions (filed with the F-1120) | s. 220.131(1): "may elect, not later than the due date for filing its return for the taxable year, including any extensions thereof, to consolidate its taxable income" |
| Florida Form F-1120 | Generally the later of the 1st day of the 5th month after the tax year end (May 1 for calendar year), or the 15th day following the federal return due date without extension | FDOR corporate income tax page due-date rule |
| Electronic filing | Required where the federal return must be e-filed | s. 220.21(2) |

There is no separate Florida transfer-pricing documentation deadline.

## Penalties and interest

A late corporate return draws a penalty of 10% of any unpaid tax due with the return for each month or fraction of a month late, up to a total of 50% of the unpaid tax, plus a floating rate of interest on underpayments (FDOR corporate income tax page). There is no Florida-specific transfer-pricing penalty; exposure for related-party distortion runs through the factors and the addback.

Common failure modes: (1) assuming Florida mandates combined reporting (it does not — consolidation is elective); (2) forgetting the state-tax addback when a group deducts other states' income taxes federally; (3) letting intercompany service fees shift the sales factor without documentation.

## Cross-border points

- **Foreign-parent groups:** Florida taxes the US member's apportioned income; the affiliated-group definition tracks the federal consolidated group (s. 220.131(1)(c) — identical component members), so there is no Florida unitary water's-edge regime.
- **The state-income-tax addback** in s. 220.13(1)(a)1.a. interacts with any credit for taxes paid to other states in the same sub-subparagraph.
- **Sales-factor election:** s. 220.153's apportionment-by-sales-factor election excludes financial organizations and banks (s. 220.153(2)).

## Worked examples

All client facts in the examples are hypothetical.

A Georgia parent sells to Florida customers through a Florida subsidiary; the group does not elect Florida consolidation. Florida-apportioned income of the Florida sub is $2,000,000. Florida tax at the confirmed 5.5% rate:

```oa-check
name: FL standalone tax on apportioned income
inputs:
  apportioned: 2000000
  rate: 0.055
steps:
  - tax: apportioned * rate
expected:
  tax: 110000.00
```

The same group deducts $300,000 of Georgia income tax federally; Florida adds it back under s. 220.13(1)(a)1.a. before apportioning at a hypothetical 40% Florida fraction. The added Florida income is $120,000, and the tax on it at 5.5% is $6,600:

```oa-check
name: addback effect at 40 percent apportionment
inputs:
  addback: 300000
  app: 0.40
  rate: 0.055
steps:
  - fl_added: addback * app
  - tax_up: fl_added * rate
expected:
  fl_added: 120000.00
  tax_up: 6600.00
```

## Ask the client first

- Does the group file a federal consolidated return, and has it considered the elective Florida consolidated return (s. 220.131), with every member's written consent ready at filing time?
- Are intercompany sales, royalties, or service fees moving income or apportionment factors across the Florida line?
- Is the state-income-tax addback tracked when other states' taxes are deducted federally?
- Has the taxpayer made qualified capital expenditures in Florida that could support the s. 220.153 sales-factor election?

## Sources

| Source | URL | Read on |
|---|---|---|
| s. 220.11 Fla. Stat. (2026) — tax imposed; 5.5% and 3.3% rates | https://www.flsenate.gov/Laws/Statutes/2026/220.11 | 2026-10-28 |
| s. 220.13 Fla. Stat. (2026) — adjusted federal income; state income tax addback | https://www.flsenate.gov/Laws/Statutes/2026/220.13 | 2026-10-28 |
| s. 220.15 Fla. Stat. (2026) — apportionment fraction (sales 50%, property 25%, payroll 25%) | https://www.flsenate.gov/Laws/Statutes/2026/220.15 | 2026-10-28 |
| s. 220.131 Fla. Stat. (2026) — affiliated-group consolidated returns (elective; member consent; federal-consolidation requirement) | https://www.flsenate.gov/Laws/Statutes/2026/220.131 | 2026-10-28 |
| s. 220.153 Fla. Stat. (2026) — apportionment by sales factor (qualified capital expenditures) | https://www.flsenate.gov/Laws/Statutes/2026/220.153 | 2026-10-28 |
| s. 220.21 Fla. Stat. (2026) — returns; electronic filing requirement | https://www.flsenate.gov/Laws/Statutes/2026/220.21 | 2026-10-28 |
| Florida Department of Revenue — Corporate Income Tax page (rate table, F-1120 due date, penalties, interest) | https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx | 2026-10-28 |

Not yet confirmed: whether Ch. 220 contains any other special-apportionment provisions beyond ss. 220.15, 220.151, 220.152 and 220.153 (the full chapter was not read end to end this run); the department's authority to disregard distortions in the factors (cited in the prior draft but not located in the statute text archived this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
