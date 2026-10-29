---
name: oh-cross-border
description: >
  Use this skill whenever asked about Ohio cross-border personal tax for tax
  year 2026 — the five-state reciprocity waiver (IN, KY, MI, PA, WV full-year
  nonresidents with wages only need no Ohio return), the IT 1040 nonresident
  credit (IT NRC) and resident credit (IT RC) both run through the Schedule
  of Credits, the 212-contact-period nonresident presumption with the Ohio
  Nonresident Statement box (IT NRS retired for 2025), nonbusiness-income
  allocation under ORC 5747.20, the no-credit-if-federally-deducted rule in
  ORC 5747.05, and the municipal 20-day work-in-municipality threshold
  (SB 22) that drives cross-border commuter withholding. Ohio has no exit
  tax. Trigger on "Ohio nonresident", "Ohio reciprocity", "IT NRC", "IT RC",
  "Ohio resident credit", "Ohio Nonresident Statement", "contact periods
  Ohio", "Ohio 20-day rule", "Ohio municipal withholding nonresident",
  "Ohio exit tax".
  Source-cited draft; ORC 5747.05 and 5747.20 statute text read 2026-10-27;
  mechanics carried from the tier-2 oh-income-tax and oh-payroll skills
  (2025 IT 1040 instructions read 2026-09-25, R.C. 718.011 read 2026-07-13).
jurisdiction: US-OH
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - oh-income-tax
  - oh-payroll
  - oh-cat
---

# Ohio cross-border (nonresidents, reciprocity, credits) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Ohio professional.

## Who this applies to

How Ohio taxes people and payrolls that cross its borders: the **five-state reciprocity waiver**, the **IT NRC** nonresident credit and **IT RC** resident credit, the **Ohio Nonresident Statement** presumption (212-contact-period limit), nonbusiness-income allocation, and the **municipal 20-day rule** for commuters. Entity cross-border (CAT nexus, P.L. 86-272) sits in `oh-corporate-income-tax` and `oh-transfer-pricing`. Ohio has **no exit tax**.

**Source status (as_of 2026-10-27):** [ORC 5747.05](https://codes.ohio.gov/ohio-revised-code/section-5747.05) (tax credits; resident credit for tax paid to another state or D.C. on income subjected to tax there; credit capped at Ohio tax; no credit where the other-state tax was deducted federally) and [ORC 5747.20](https://codes.ohio.gov/ohio-revised-code/section-5747.20) (nonbusiness income allocation: residents allocate all items to Ohio; nonresidents allocate Ohio-performed personal-services compensation to Ohio) fetched HTTP 200 and read. Reciprocity list, IT NRC/IT RC mechanics, contact-period counts and the 20-day rule are carried from the tier-2 `oh-income-tax` (2025 IT 1040 instructions, read 2026-09-25) and `oh-payroll` (R.C. 718.011 as rewritten by SB 22, read 2026-07-13).

### 2. Who applies

- **Full-year nonresidents in IN, KY, MI, PA or WV:** no Ohio IT 1040 if their **only** Ohio-source income is wages (reciprocity). Any other Ohio income — rental from Ohio property, Ohio business income, Ohio gaming winnings — breaks the waiver and forces a return.
- **Other nonresidents with Ohio income:** file IT 1040 and claim the **IT NRC** credit for income not earned or received in Ohio.
- **Part-year residents:** IT NRC for income earned while a resident of another state; **IT RC** for non-Ohio income taxed by another state while an Ohio resident.
- **Ohio residents working elsewhere:** full Ohio return + **IT RC** credit (US states and D.C. only — not city, foreign, or territory taxes; not wages in the five reciprocity states, which were never taxed there either).
- **Nonresident presumption claimants:** check the **Ohio Nonresident Statement** box on the IT 10/1040 (IT NRS form retired for 2025). All five criteria: ≤212 contact periods; outside-Ohio abode with no depreciation claimed; no Ohio driver's license/ID (surrendered before the year began); no Ohio homestead exemption; no Ohio in-state tuition. Contact period = abode outside Ohio, away overnight, any part of **two consecutive days** in Ohio. <213 contact periods: nonresidency shown "more likely than not"; ≥213: "clear and convincing". Statement deadline: **October 15**; part-year residents cannot use it. (not yet confirmed)

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| Reciprocity states | IN, KY, MI, PA, WV — wages-only waiver for full-year nonresidents | `oh-income-tax` (2025 IT 1040 instructions, 2026-09-25) |
| IT NRC | Credit for income **not** earned or received in Ohio; runs through Schedule of Credits | `oh-income-tax` |
| IT RC | Credit for tax paid to another **US state or D.C.** on income also in Ohio AGI; capped at Ohio tax; no credit if the other-state tax was deducted in federal AGI | [ORC 5747.05](https://codes.ohio.gov/ohio-revised-code/section-5747.05), read 2026-10-27 |
| Business income rate | Flat 3% (2025; HB 96 phasing down) — business income of nonresidents is apportioned to Ohio | `oh-income-tax` | (not yet confirmed)
| Nonbusiness allocation | Residents: all to Ohio. Nonresidents: personal-services compensation for work performed in Ohio, Ohio property income, etc. | [ORC 5747.20](https://codes.ohio.gov/ohio-revised-code/section-5747.20), read 2026-10-27 |
| BID ordering | The other-state-tax deduction (5747.01(A)(28)) first reduces business income apportioned to Ohio when computing the resident credit | ORC 5747.05, read 2026-10-27 |
| Municipal 20-day rule | No non-resident municipal withholding until day 21 of work in a non-principal municipality; then **retroactive to day 1**; employers with prior-year revenue <$500,000 exempt | R.C. 718.011 (SB 22) via `oh-payroll` (2026-07-13) |
| Municipal rates | 1.00%–3.00%; inter-municipal credits vary 0–100% | `oh-payroll` | (not yet confirmed)
| Exit tax | **None** | no Ohio statute imposes one |

## The taxable base

Not yet confirmed against archived sources.
## Deadlines and filing
 (not yet confirmed)
| Filing | Due | (not yet confirmed)
|---|---|
| IT 1040 (residents, nonresidents, part-year) | April 15 (calendar year); extension to October 15 | (not yet confirmed)
| Ohio Nonresident Statement box | Claimed on the return; presumption deadline 15th day of 10th month after year-end (October 15) | (not yet confirmed)
| IT NRC / IT RC | Attached to the IT 1040 via Schedule of Credits |
| Municipal employer returns | Per municipality/RITA/CCA calendar (Form 27 RITA year-end etc.) — see `oh-payroll` |

## Penalties and interest

- IT/SD 2210 underpayment interest on line 11 of the IT 1040; late-payment interest on line 21 — Ohio charges **interest, not a late-filing penalty percentage** on the individual return (per `oh-income-tax` 2025 instructions).
- Delinquency billings can fire when federal AGI > $28,450 and no Ohio return was filed — the Department recommends filing even at zero tax (`oh-income-tax`). (not yet confirmed)
- Municipal side: missed 20-day catch-up withholding is the most common Ohio municipal payroll audit finding (`oh-payroll` AUDIT FLASH POINT).

## Cross-border points

- **Wages sourced where work is performed** (ORC 5747.20(B)(1)); telework days are sourced to the employee's actual physical location from 2022 (SB 22 rolled back the pandemic H.B. 197 fiction) — `oh-payroll`.
- **Reciprocity covers wages only.** A KY resident with Ohio wages only: no Ohio return. Add an Ohio Airbnb: full IT 1040 with IT NRC for the non-Ohio income.
- **IT RC is lesser-of in substance:** credit cannot exceed Ohio tax on the creditable income, and is zero if the taxpayer took the SALT deduction route federally for that other-state income (ORC 5747.05(B)(5)(a)).
- **Entities:** CAT nexus bright-lines and the P.L. 86-272 exclusion are in `oh-corporate-income-tax`; foreign-affiliate group choice in `oh-transfer-pricing`.
- **No exit tax:** moving out of Ohio ends Ohio resident taxation at the move date (part-year rules above).

## Worked examples

**Example A — Ohio resident working in Indiana; IT RC lesser-of.**

```oa-check
name: IT RC capped at lower Indiana tax
inputs:
  ohio_tax_before_credits: 4200
  indiana_tax_on_same_income: 3800
steps:
  - credit: min(ohio_tax_before_credits, indiana_tax_on_same_income)
  - ohio_due: ohio_tax_before_credits - credit
expected:
  credit: 3800
  ohio_due: 400
```

The credit is the other-state tax actually paid on the same income, never more than the Ohio tax (ORC 5747.05(B)). If the client deducted the Indiana tax federally, the credit is zero instead.

**Example B — commuter crosses the municipal 20-day line.**

```oa-check
name: Retroactive municipal withholding after day 21
inputs:
  days_worked_in_city: 25
  daily_wage: 400
  nonresident_rate: 0.025
steps:
  - taxable_days_1_to_25: days_worked_in_city * daily_wage
  - catchup_withholding: taxable_days_1_to_25 * nonresident_rate
expected:
  taxable_days_1_to_25: 10000
  catchup_withholding: 250.00
```

On day 21 the employer must withhold for **all 25 days**, including the first 20 — a catch-up remittance, per R.C. 718.011 via `oh-payroll`.

## Ask the client first

- Which state claims them: domicile, abode, driver's license, homestead exemption, in-state tuition — the five presumption criteria.
- How many contact periods in Ohio (two-consecutive-day counting) — under or over 213?
- Any Ohio income beyond wages if they live in IN/KY/MI/PA/WV? That breaks the reciprocity waiver.
- Did they deduct other-state income taxes on the federal return? That kills IT RC for that income.
- Per-employee, per-municipality day logs for the 20-day rule — does a day-21 trigger report exist?
- Prior-year revenue under $500,000? The small-employer 20-day exemption may apply.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.

| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |

- [ORC 5747.05 — tax credits, resident credit, no-federal-deduction rule](https://codes.ohio.gov/ohio-revised-code/section-5747.05) — read 2026-10-27 (text effective 2025-09-30, HB 96)
- [ORC 5747.20 — allocating nonbusiness income or deduction](https://codes.ohio.gov/ohio-revised-code/section-5747.20) — read 2026-10-27
- `oh-income-tax` (tier 2, 2025 IT 1040 instructions read 2026-09-25) — reciprocity list, IT NRC/IT RC, contact periods, Nonresident Statement criteria
- `oh-payroll` (tier 2, read 2026-07-13) — R.C. 718.011 20-day rule, municipal rates, RITA/CCA/direct-file
- **not yet confirmed:** 2026 IT 1040 instructions (not yet published at read time 2026-09-25 per `oh-income-tax`); municipal credit percentages per city

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Ohio nonresident, reciprocity and commuter questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
## Talk to a verified accountant

Not yet confirmed against archived sources.

### Sources

| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | — | 2026-10-28 |


- [ORC 5747.05 — tax credits, resident credit, no-federal-deduction rule](https://codes.ohio.gov/ohio-revised-code/section-5747.05) — read 2026-10-27 (text effective 2025-09-30, HB 96)
- [ORC 5747.20 — allocating nonbusiness income or deduction](https://codes.ohio.gov/ohio-revised-code/section-5747.20) — read 2026-10-27
- `oh-income-tax` (tier 2, 2025 IT 1040 instructions read 2026-09-25) — reciprocity list, IT NRC/IT RC, contact periods, Nonresident Statement criteria
- `oh-payroll` (tier 2, read 2026-07-13) — R.C. 718.011 20-day rule, municipal rates, RITA/CCA/direct-file
- **not yet confirmed:** 2026 IT 1040 instructions (not yet published at read time 2026-09-25 per `oh-income-tax`); municipal credit percentages per city

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Ohio nonresident, reciprocity and commuter questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

### Talk to a verified accountant


Not yet confirmed against archived sources.
