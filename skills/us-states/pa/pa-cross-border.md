---
name: pa-cross-border
description: >
  Use this skill whenever asked about Pennsylvania cross-border personal tax
  for tax year 2026 -- the six reciprocal states (NJ, OH, IN, MD, VA, WV:
  full-year residents with only PA wages pay no PA tax, but PA nonresidents
  from those states still file PA-40 and PA local EIT still applies), the
  Schedule G-L resident credit for taxes paid to other states (with the
  Ohio-wage exception), nonresident and part-year PA-40 filing, PA-source
  compensation rules, and the local earned income tax (Act 32) layer that
  reciprocity does NOT waive. Pennsylvania has no exit tax. Trigger on
  "Pennsylvania nonresident", "PA reciprocity", "Schedule G-L", "PA-40
  nonresident", "Pennsylvania resident credit", "PA local services tax
  nonresident", "Pennsylvania exit tax", "work in PA live in New Jersey".
  Source-cited draft; 2025 PA-40 instructions read 2026-10-27 (reciprocity
  carve-outs, Schedule G-L, nonresident/part-year rules quoted); local EIT
  mechanics carried from tier-2 pa-payroll (read 2026-07-13).
jurisdiction: US-PA
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - pa-income-tax
  - pa-payroll
  - pa-local-eit
---

# Pennsylvania cross-border (nonresidents, reciprocity, credits) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Pennsylvania professional.

## Who this applies to

How Pennsylvania taxes people who cross its borders: the **six reciprocal states**, the **Schedule G-L** resident credit, **nonresident/part-year PA-40** filing, and the **local earned income tax / Local Services Tax** layer that reciprocity does not touch. Entity cross-border (CNIT nexus, P.L. 86-272) sits in `pa-corporate-income-tax` and `pa-transfer-pricing`. Pennsylvania has **no exit tax**.

**Source status (as_of 2026-10-27):** [2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf) fetched HTTP 200 (PDF, 48 pages) and read -- reciprocity carve-outs, Schedule G-L rules, and nonresident/part-year filing quoted below. Local EIT/LST mechanics carried from tier-2 `pa-payroll`/`pa-local-eit` (Act 32, read 2026-07-13). 2026 PA-40 instructions not yet published at read time -- figures are 2025 unless flagged.

### 2. Who applies

- **Full-year residents of NJ, OH, IN, MD, VA or WV working in PA:** under the **reciprocal tax agreements** they owe **no PA state income tax on wages** -- but the PA-40 instructions carve out that they **still file a PA-40** if they have other PA-source income, and PA **local EIT and Local Services Tax still apply** to work in PA municipalities (`pa-payroll`, `pa-local-eit`).
- **PA residents working in another state:** full PA-40 + **Schedule G-L** credit for tax properly paid to the other state (or DC/territory per the instructions).
- **Nonresidents and part-year residents with PA-source income:** file PA-40; nonresidents report PA-source income only (Line 10 allocation); part-year residents report income for the PA-residency period.
- **The Ohio-wage wrinkle:** PA residents who worked in Ohio -- the PA-40 instructions state no G-L credit is allowed for Ohio taxes on wages (Ohio's CAT-era system doesn't tax nonresident wages the same way); check the current instructions line-by-line.
- **Municipal layer:** EIT is owed to the **work** municipality by nonresidents and the **residence** municipality by residents, with a credit so the same earnings aren't double-taxed (`pa-local-eit`).

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| PIT rate | **3.07%** flat | `pa-income-tax` (2026 REV-413 read 2026-09-25) | (not yet confirmed)
| Reciprocal states | **NJ, OH, IN, MD, VA, WV** -- wages exempt for full-year residents of those states | 2025 PA-40 instructions, read 2026-10-27 |
| Reciprocity limits | Does NOT waive PA local EIT/LST; other PA-source income still taxable | 2025 PA-40 instructions + `pa-local-eit` |
| Schedule G-L credit | Credit for income tax properly paid to another state on income also taxed by PA; cannot exceed PA tax on that income | 2025 PA-40 instructions, read 2026-10-27 |
| Ohio-wage exception | No G-L credit for Ohio tax on wages (per 2025 instructions) | 2025 PA-40 instructions, read 2026-10-27 |
| Local EIT | Act 32 rates ~1%–3.9% by municipality; LST $10/yr cap | `pa-payroll` (2026-07-13) |
| Exit tax | **None** | no PA statute imposes one |

### 4. Deadlines

| Filing | Due |
|---|---|
| PA-40 (residents, nonresidents, part-year) | April 15; extension to October 15 | (not yet confirmed)
| Schedule G-L | Attached to the PA-40 |
| Local EIT (Act 32) returns | Per PSD calendar (annual reconciliation Jan 31; quarterly for larger employers) -- see `pa-local-eit` | (not yet confirmed)
| LST | With municipal returns |

### 5. Penalties and interest

- PA-40 late filing: 5% penalty + 0.5%/month (max 25%) + monthly interest -- carried from `pa-income-tax`; exact 2026 interest rate not yet confirmed.
- Non-filers with PA-source wages above the filing threshold get matching notices from the Department's federal-data crossmatch.
- Municipal side: PSDs audit nonresident EIT under-collection -- a common finding where reciprocity confused payroll (`pa-local-eit` AUDIT FLASH POINT).

### 6. Cross-border

- **Compensation is PA-source where earned** (work performed in PA); telework from a reciprocal state can shift source -- confirm day-by-day work location.
- **Reciprocity ≠ exemption from filing:** reciprocal-state residents with PA interest, rents, or business income still file PA-40 for those items.
- **G-L is lesser-of:** credit capped at PA tax on the doubly-taxed income; foreign taxes claimed federally don't generate a G-L credit for states.
- **Entities:** CNIT nexus and P.L. 86-272 in `pa-corporate-income-tax`; combined-group foreign affiliates in `pa-transfer-pricing`.
- **No exit tax:** moving out ends PA resident tax at the move date (part-year return).

### 7. Worked examples

**Example A -- NJ resident commuting to Philadelphia (state layer).**

```oa-check
name: Reciprocity zeroes PA state tax on wages only
inputs:
  pa_wages: 90000
  pa_rate: 0.0307
  nj_tax_on_same_wages: 4900
  pa_state_tax_if_not_reciprocal: 2763.00
steps:
  - pa_state_tax_due: 0
  - nj_tax_due: nj_tax_on_same_wages
expected:
  pa_state_tax_if_not_reciprocal: 2763.00
  pa_state_tax_due: 0
  nj_tax_due: 4900
```

Reciprocity waives the 2,763 PA state tax -- but the Philadelphia wage tax and $10 LST on the work side still apply (local layer, `pa-local-eit`), and NJ taxes the full wages.

**Example B -- PA resident working in Maryland; G-L lesser-of.**

```oa-check
name: G-L credit capped at PA tax on doubly-taxed wages
inputs:
  wages: 120000
  pa_tax_on_wages: 3684
  md_tax_on_wages: 5400
steps:
  - gl_credit: min(pa_tax_on_wages, md_tax_on_wages)
  - pa_remaining: pa_tax_on_wages - gl_credit
expected:
  gl_credit: 3684
  pa_remaining: 0
```

Maryland's higher tax means the credit is capped at the PA figure (120,000 × 3.07% = 3,684); PA residual is zero.

### 8. Ask the client

- Where were they a full-year resident? Any day-count or domicile change mid-year (part-year)?
- Any PA-source income beyond wages despite reciprocity (rents, business, gains)? That forces a PA-40.
- Did payroll apply the **local EIT work-municipality** rate correctly for reciprocal commuters?
- For PA residents working in Ohio: was the G-L Ohio-wage exception applied?
- Telework split: how many days worked from home out-of-state vs in PA?

### 9. Sources

- [2025 PA-40 instructions (PDF)](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf) -- read 2026-10-27 (reciprocity list and carve-outs, Schedule G-L, nonresident/part-year rules)
- `pa-income-tax` (tier 2, 2026 REV-413 read 2026-09-25) -- 3.07% rate, penalties (not yet confirmed)
- `pa-payroll` / `pa-local-eit` (tier 2, read 2026-07-13) -- Act 32 EIT, LST, reciprocity withholding mechanics
- **not yet confirmed:** 2026 PA-40 instructions (not published at read time); per-PSD rate tables; PA interest rate for 2026.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Pennsylvania nonresident, reciprocity and commuter questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
| (see Not yet confirmed) | -- | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
