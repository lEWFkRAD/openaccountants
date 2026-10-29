---
name: la-corporate-income-tax
description: >
  Use this skill whenever asked about Louisiana corporate income tax for
  tax year 2026 — the flat 5.5% corporation income tax for tax periods
  beginning on or after January 1, 2025 (graduated brackets repealed), Form
  CIFT-620, the May 15 (15th day of 5th month) due date, the $1,000
  estimated-tax threshold, and the corporation franchise tax repeal for
  periods beginning on or after January 1, 2026. Trigger on "Louisiana
  corporate income tax", "CIFT-620", "LA corporation income tax",
  "Louisiana franchise tax repeal", "LDR corporate". Source-cited draft;
  rate, due date, threshold, and franchise repeal verified from the LDR
  Corporation Income Tax page 2026-10-28; apportionment detail
  not confirmed.
jurisdiction: US-LA
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - la-income-tax
---

# Louisiana corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-28. Covers Louisiana corporation income tax (Form CIFT-620), the flat-rate reform, the franchise-tax repeal, and filing mechanics. **Source status:** the LDR Corporation Income Tax page (https://revenue.louisiana.gov/businesses/widely-used-tax-types/corporate-income-franchise-tax/, page "Updated July 07, 2026") was fetched and its text verified 2026-10-28 — the **5.5% flat rate, the May 15 due date, the $1,000 estimated threshold, the CIFT-620/CIFT-620EXT-V form IDs, and the franchise repeal are verified quotes**. **Apportionment/unitary detail sits in La. R.S. 47 behind a session-state legislature site**, so the apportionment formula and combined-report mechanics are not confirmed.

## Rates, bands and thresholds

A Louisiana Corporation Income Tax return is generally required for (LDR page, verified 2026-10-28):

- **Corporations earning income from Louisiana sources**;
- **Entities taxed as corporations for federal purposes**;
- **S corporations required to file as corporations for Louisiana income tax purposes** (Louisiana does not fully conform to federal S pass-through — verify scope);
- **LLCs taxed as corporations federally**;
- **Foreign corporations doing business in or deriving income from Louisiana sources**.
- **Exempt entities**: an IRS exemption ruling must be provided to LDR to request Louisiana exemption (verified).
- **Franchise tax: repealed** for franchise tax periods beginning on or after January 1, 2026; prior-period franchise obligations may remain (verified).

## The taxable base

| Item | Rule | Source status |
|---|---|---|
| Rate | **flat 5.5%** for tax periods beginning on or after Jan 1, 2025; prior graduated brackets repealed | **verified** (LDR page) |
| Base | federal taxable income with Louisiana modifications; Louisiana-source income for multistate filers | duty verified; modification detail not confirmed |
| Apportionment | multistate apportionment formula and any unitary-combination requirement: statute numbering not confirmed (legis.la.gov serves only a JS shell to plain fetchers) | not confirmed |
| Franchise tax | repealed for periods beginning on/after 2026-01-01 | **verified** |
| Exemption | IRS ruling must be furnished to LDR | verified |

## Deadlines and filing

- CIFT-620: due **on or before the 15th day of the 5th month** after the accounting period closes — **May 15** for calendar-year filers (verified quote; note this is a month later than the federal April 15).
- **Extension:** automatic six-month extension to file if a federal extension was timely requested; **extension to file is not an extension to pay** — tax due must be paid by the original due date to avoid interest and penalties (verified). Extension voucher: CIFT-620EXT-V (verified form ID).
- **Estimated payments:** required if liability after credits can reasonably be expected to be **$1,000 or more** for the year (verified); pay via LaTAP.

## Penalties and interest

- Late payment/underpayment: interest and penalties accrue from the original due date (extension-to-file rule, verified); the percentage tiers are not confirmed.
- Federal-adjustment reporting: if a federal adjustment changes Louisiana liability, the taxpayer must report to LDR within the required period (verified duty; the deadline is not confirmed).

## Cross-border points

- Foreign (out-of-state) corporations doing business in Louisiana file CIFT-620 and apportion (see `la-cross-border`).
- S corporations may be taxed at the entity level for Louisiana even when pass-through federally — flag for any S-corp client with Louisiana source (verified category; scope not confirmed).
- No franchise tax layer for 2026+ filers (verified repeal).

## Worked examples

**Example 1 — flat 5.5% on apportioned Louisiana income:** C corporation, $300,000 unitary income, 60% Louisiana apportionment factor.

```oa-check
name: LA corporate flat 5.5%
inputs:
  income: 300000
  factor: 0.60
  rate: 0.055
steps:
  - la_income: income * factor
  - tax: la_income * rate
expected:
  la_income: 180000
  tax: 9900
```

**Example 2 — estimated-payment installments:** projected Louisiana liability after credits is $1,200 — above the $1,000 threshold (verified), so estimates are required. Quarterly installment:

```oa-check
name: LA estimated installments
inputs:
  liability: 1200
  quarters: 4
steps:
  - required: max(liability - 1000, 0)
  - quarterly: liability / quarters
expected:
  required: 200
  quarterly: 300
```

The `required` step shows the liability exceeds the $1,000 threshold by $200, so estimated payments apply; each quarterly installment is $300.

## Ask the client first

- Federal entity classification (C, S, LLC-taxed-as-corp) — Louisiana may tax S corps at the entity level.
- Louisiana nexus: source income, physical presence, remote sellers/service providers.
- Whether the entity still has a prior-period franchise tax obligation (pre-2026 periods).
- Projected liability vs the $1,000 estimated threshold; May 15 (not April 15) due date.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| LDR Corporation Income Tax (rate, due date, threshold, forms, franchise repeal, extension rule) | https://revenue.louisiana.gov/businesses/widely-used-tax-types/corporate-income-franchise-tax/ | 2026-10-28 |
| La. R.S. 47 (Title 47 table of contents; article text behind session state) | https://legis.la.gov/legis/Laws_Toc.aspx?folder=90&title=47 | 2026-10-29 |

Not yet confirmed: the apportionment formula and unitary-combination requirement (the R.S. 47:287.83 numbering was not verified — legis.la.gov serves only a JS shell to plain fetchers); S-corporation entity-level scope; penalty/interest percentage tiers; the federal-adjustment reporting deadline.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Louisiana corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
