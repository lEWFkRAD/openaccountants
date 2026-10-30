---
name: nj-cross-border
description: >
  Use this skill whenever asked about New Jersey cross-border personal tax
  for tax year 2026 — nonresident Form NJ-1040NR two-column allocation
  (income percentage to four decimals), the no-part-year-return rule (both
  forms, prorated exemptions by months), the Schedule NJ-COJ credit for
  taxes paid to other jurisdictions (lesser-of formula, seven decimals, NY
  "New York State Amount" column, PA reciprocity on wages), the New York
  convenience-of-the-employer referral point for workdays at home in NJ,
  and the PA/NY/NJ commuter patterns. Trigger on "New Jersey nonresident",
  "NJ-1040NR", "part-year New Jersey", "NJ-COJ credit", "credit for taxes
  paid other jurisdictions New Jersey", "NY convenience of the employer New
  Jersey".
  Source-cited draft; corroborated by the existing tier-2 nj-income-tax
  skill (2025 NJ-1040/NJ-1040NR instructions, GIT-3W, GIT-6 read 2026-10-16).
jurisdiction: US-NJ
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - nj-income-tax
---

# New Jersey cross-border (nonresidents, part-year, NJ-COJ) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

How New Jersey taxes people who cross its borders: resident NJ-1040 vs nonresident **NJ-1040NR** (two-column method), the **no part-year return** rule, prorated exemptions for part-year residents, the **Schedule NJ-COJ** credit for taxes paid to other jurisdictions, and the commuter flash points (NY convenience-of-the-employer, PA reciprocity). Corporate cross-border sits in `nj-corporate-income-tax` / `nj-transfer-pricing`.

**Source status:** figures and mechanics corroborated by the existing tier-2 `nj-income-tax` skill (verified against the 2025 NJ-1040 and NJ-1040NR instructions, GIT-3W and GIT-6 on 2026-10-16). The 2026 instruction PDFs were not re-fetched this run — bracket figures carry the 2025-year label where used.

### 2. Who applies

- **Nonresidents with NJ-source income:** NJ-1040NR — report everything in column A, NJ-source in column B, tax computed on column A then multiplied by the income percentage (line 29 B ÷ line 29 A, **four decimal places**). (`nj-income-tax`.)
- **Part-year residents:** **no part-year return exists** — file NJ-1040 for the resident period plus NJ-1040NR if NJ-source income arose while a nonresident; prorate exemptions (line 13) and the property tax deduction/credit by months (15+ days = a month); medical/alimony deductions only while resident; pension exclusion prorated by months only if whole-year income ≤ $100,000 (and only if whole-year income ≤ $150,000). (`nj-income-tax`, GIT-6.)
- **NJ residents working in NY/PA/elsewhere:** full resident return + **NJ-COJ** credit (see §3).
- **Domicile changers:** NJ statutory residency (183+ days) plus domicile facts drive the whole analysis — the 183-day test is in `nj-income-tax`.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Top GIT rate | 10.75% over $1,000,000 (2025 table; 8.97% $500,000–$1M band) | `nj-income-tax` skill |
| NJ-1040NR method | tax(column A) × (col B ÷ col A, 4 decimals) | 2025 NJ-1040NR instructions via `nj-income-tax` |
| NJ-COJ credit | lesser of (a) NJ tax × (dual-taxed income ÷ NJ gross income, 7 decimals) and (b) tax actually paid there; **not** dollar-for-dollar; US/PR/foreign-country taxes get no credit | GIT-3W via `nj-income-tax` |
| "Properly taxed" test | services performed there, business there, property there, gambling there; portfolio income generally not creditable | GIT-3W via `nj-income-tax` |
| NY pattern | use the **"New York State Amount"** column of IT-203, not the federal column | 2025 NJ-1040 instructions via `nj-income-tax` |
| PA pattern | **reciprocal agreement**: PA does not tax NJ residents' wages → no NJ-COJ for PA wage tax; SE income, property gains, and **Philadelphia wage tax** (outside the agreement) can qualify | GIT-3W via `nj-income-tax` |
| NY convenience rule | NJ publications reviewed do not address NJ-home workdays NY taxes under convenience-of-the-employer — **referral point**, expect double exposure | `nj-income-tax` note |

### 4. Deadlines

- NJ-1040 / NJ-1040NR: **15 April** for calendar-year filers (2025 returns: 15 April 2026; 15 October 2026 extended).
- Part-year filers file both forms with the same deadline.
- NJ-COJ claimed on the resident return; a later other-state amendment must be reported — the credit adjusts.
- Estimated-tax underpayment interest on Form NJ-2210 (safe-harbor rules in `nj-income-tax`).

### 5. Penalties and interest

- Late-filing 5% a month up to 25% of balance due; late-payment 5%; interest at the statutory rate (NJ interest compounds; the GIT penalty page was not re-fetched — quote percentages from the NJ-1040 instructions, **not yet confirmed** for the 2026 printed rate).
- The classic audit population: nonresidents with NJ rental/SE income who filed nothing, and part-year filers who prorated exemptions wrongly.

### 6. Cross-border patterns

- **NY↔NJ commuter:** NY taxes nonresident wages for workdays in NY (and remote workdays under convenience-of-the-employer when the employer is NY-based); NJ grants NJ-COJ only for income **properly** taxed by NY — home-workday wages NY grabs under the convenience rule are the unresolved double-tax wedge (referral point).
- **PA↔NJ commuter:** reciprocity means no PA wage tax for NJ residents and no credit — but Philadelphia's wage tax sits outside the agreement and is creditable.
- **NJ rental to a nonresident:** NJ-source (column B) regardless of owner residence; the income-percentage method pulls the rate bracket up via column A.
- **No part-year return** is unusual among high-tax states — never model an NJ part-year as a single blended return.

### 7. Worked examples

**Example 1 — nonresident NJ rental (2025 brackets, method current).** PA resident, total income everywhere $200,000, NJ rental $50,000.

```oa-check
name: NJ-1040NR rental method
inputs:
  world_income: 200000
  nj_income: 50000
  exemption: 1000
  rate: 0.0637
  fixed: 2126.25
steps:
  - pct: nj_income / world_income
  - taxable_a: world_income - exemption
  - tax_a: taxable_a * rate - fixed
  - nj_tax: tax_a * pct
expected:
  pct: 0.25
  taxable_a: 199000.00
  tax_a: 10550.05
  nj_tax: 2637.51
```

Matches the skill's Case 8. PA then credits the NJ tax within PA's limits.

**Example 2 — NJ-COJ lesser-of cap.** NJ resident, NJ gross income $300,000; $120,000 also properly taxed by NY; NJ tax before credit $25,000; NY tax on that income $11,000.

```oa-check
name: NJ-COJ lesser of
inputs:
  nj_tax: 25000
  dual: 120000
  nj_gross: 300000
  other_tax: 11000
steps:
  - share: dual / nj_gross
  - cap: nj_tax * share
  - credit: min(cap, other_tax)
expected:
  share: 0.40
  cap: 10000.00
  credit: 10000.00
```

The credit is capped at $10,000 — $1,000 of the NY tax is stranded, the standard NJ-COJ wedge.

### 8. Ask the client

1. Domicile and day counts — 183+ days anywhere? Statutory residency analysis documented?
2. Moved mid-year — are BOTH forms filed and exemptions prorated by months (15-day rule)?
3. NY employer — how many workdays at an NJ home office? Is the convenience-of-the-employer double exposure modeled (referral point)?
4. Philadelphia or other PA municipal taxes — creditable and claimed on NJ-COJ?
5. NJ rental/SE income owned by a nonresident — NJ-1040NR filed, income percentage computed to four decimals?

### 9. Sources

1. Existing tier-2 skill `nj-income-tax` (NJ-1040/NJ-1040NR method, NJ-COJ rules, PA reciprocity, NY column rule, part-year proration; verified 2026-10-16): repo `skills/us-states/nj/nj-income-tax.md`.
2. NJ Division of Taxation, GIT-3W (credit for taxes paid to other jurisdictions) and GIT-6 (part-year/nonresident): <https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git3w.pdf>, <https://www.nj.gov/treasury/taxation/pdf/pubs/tgi-ee/git6.pdf> — cited via `nj-income-tax`; not re-fetched this run.
3. 2025 NJ-1040NR instructions: <https://www.nj.gov/treasury/taxation/pdf/current/1040nri.pdf> — cited via `nj-income-tax`; 2026 edition **not yet confirmed**.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for New Jersey nonresident and dual-residency questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
