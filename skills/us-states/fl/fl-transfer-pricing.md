---
name: fl-transfer-pricing
description: >
  Use this skill whenever asked about Florida transfer pricing and
  related-party adjustments for tax year 2026 — affiliated-group
  consolidated filing under s. 220.131 Fla. Stat., the absence of a
  standalone state transfer-pricing documentation regime, special
  apportionment under s. 220.153, the state-income-tax addback under
  s. 220.13(1)(a)1.a., and how Florida conforms to federal
  consolidated returns. Trigger on "Florida transfer pricing",
  "Florida combined reporting", "Florida consolidated return",
  "Florida addback", "220.131", "Florida affiliated group".
  Source-cited draft; Ch. 220 statute text read 2026-10-27.
jurisdiction: US-FL
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - fl-corporate-income-tax
---

# Florida transfer pricing / affiliated-group overlay v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Florida has **no standalone transfer-pricing documentation regime** — no state version of IRC §482 with its own penalty or contemporaneous-documentation requirement. Related-party economics enter the Florida corporate tax base through four verified statutory levers: (1) mandatory federal-consolidation conformity and the optional Florida consolidated return under s. 220.131, Fla. Stat.; (2) the addition back of state income taxes deducted federally under s. 220.13(1)(a)1.a.; (3) special apportionment when intercompany dealings distort the statutory fraction under s. 220.153; and (4) the department's authority to disregard distortions in the factors. **Source status:** ss. 220.13, 220.131, 220.15 statute text read 2026-10-27 from flsenate.gov (200); s. 220.153 special-apportionment text not re-audited this run — flagged **needs-sources**.

## 2. Who applies

- Any "taxpayer" under Ch. 220 — a C-corporation or other entity taxed as a corporation doing business in Florida, earning Florida income, or a Florida resident/citizen shareholder of such an entity (s. 220.11(1) verified 2026-10-27).
- Parent companies of affiliated groups: Florida permits (does not mandate) a consolidated Florida return for groups that file federally consolidated, with member consent (s. 220.131(1), verified 2026-10-27).
- Groups that do **not** consolidate in Florida still file separate company returns with factor-based apportionment — intercompany transactions then sit inside each entity's apportionment factors, where the department can adjust distortions.

## 3. Rates and base

There is no separate transfer-pricing rate. The operative amounts:

| Item | Amount / rule | Source |
|---|---|---|
| Corporate income tax rate | 5.5% of net income (s. 220.11(2)(a): "5 1/2 percent") | flsenate.gov 2025 statute text, read 2026-10-27 |
| Rate for taxpayers using s. 220.13(2)(k) computation | 3.3% (s. 220.11(3)) | same, read 2026-10-27 |
| Apportionment fraction | sales 50% / property 25% / payroll 25% (s. 220.15(1)) | flsenate.gov, read 2026-10-27 |
| State income tax addback | add back state/local income taxes deducted federally, with credit interplay per s. 220.13(1)(a)1.a.-b. | flsenate.gov, read 2026-10-27 |
| Florida consolidated return | elective, requires federal consolidation + member consent (s. 220.131(1)) | flsenate.gov, read 2026-10-27 |
| Special apportionment | s. 220.153 departure from statutory fraction on distortion | **needs-sources** (text not re-audited this run) |

Base: adjusted federal income (s. 220.13) apportioned by the 50/25/25 fraction; related-party pricing affects both the numerator (Florida sales factor) and each entity's taxable income.

## 4. Deadlines

- Florida consolidated-return election is made "not later than the due date for filing its return for the taxable year, including any extensions" (s. 220.131(1), verified 2026-10-27) — i.e., with the F-1120 (or F-1120-N for the $2,500 no-tax/liability return).
- F-1120 due date follows the federal return date (April 15 for calendar-year taxpayers; confirm current e-file mandate under s. 220.21(2), verified 2026-10-27).
- No separate transfer-pricing documentation deadline exists in Florida.

## 5. Penalties and interest

Florida penalty/interest provisions sit in ss. 220.25–220.27; section text did not extract cleanly this run — **needs-sources** for current percentages. Practical exposure for related-party distortion: factor adjustment plus interest; there is no Florida-specific transfer-pricing penalty. Common failure modes: (1) assuming Florida mandates combined reporting (it does not — consolidation is elective); (2) forgetting the state-tax addback when a group deducts other states' income taxes federally; (3) letting intercompany service fees shift the sales factor without documentation.

## 6. Cross-border interactions

- Foreign-parent groups: Florida taxes the US member's apportioned income; there is no Florida unitary water's-edge regime — the affiliated-group definition tracks the federal consolidated group (s. 220.131).
- Payments to related foreign affiliates are not separately restricted by Florida statute (no state interest/royalty addback regime found in Ch. 220 — absence noted, confirm against full chapter text: **needs-sources**).
- The state-income-tax addback interacts with credits for taxes paid to other states under s. 220.13(1)(a)1.b. (read 2026-10-27).

## 7. Worked examples

A Georgia parent sells to Florida customers through a Florida subsidiary; the group does not elect Florida consolidation. Florida-apportioned income of the FL sub is $2,000,000:

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

The same group deducts $300,000 of Georgia income tax federally; Florida adds it back under s. 220.13(1)(a)1.a. before apportionment at 40%:

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

## 8. Ask the client

- Does the group file a federal consolidated return, and has it considered the elective Florida consolidated return (s. 220.131)?
- Are intercompany sales, royalties, or service fees moving income or apportionment factors across the Florida line?
- Is the state-income-tax addback tracked when other states' taxes are deducted federally?
- Would special apportionment (s. 220.153) help where the statutory fraction distorts Florida activity?

## Sources

1. s. 220.11 Fla. Stat. (tax imposed; 5.5% / 3.3% rates): https://www.flsenate.gov/Laws/Statutes/2025/220.11 (200, statute text read 2026-10-27)
2. s. 220.13 Fla. Stat. (adjusted federal income; addback): https://www.flsenate.gov/Laws/Statutes/2025/220.13 (200, statute text read 2026-10-27)
3. s. 220.15 Fla. Stat. (50/25/25 apportionment): https://www.flsenate.gov/Laws/Statutes/2025/220.15 (200, statute text read 2026-10-27)
4. s. 220.131 Fla. Stat. (affiliated-group consolidation): https://www.flsenate.gov/Laws/Statutes/2025/220.131 (200, statute text read 2026-10-27)
5. s. 220.153 Fla. Stat. (special apportionment): **needs-sources** — text not fetched this run
6. ss. 220.25–220.27 (penalties/interest): **needs-sources** — text not extracted this run

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Florida related-party and apportionment questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
