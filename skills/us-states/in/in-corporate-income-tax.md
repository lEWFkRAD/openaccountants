---
name: in-corporate-income-tax
description: >
  Use this skill whenever asked about Indiana corporate income tax for tax
  year 2026 — the flat corporate adjusted gross income tax (IC 6-3), Form
  IT-20 with Schedule E single-sales-factor apportionment, Schedule 8-D
  affiliated-group disclosure, Schedule IT-20PIC intangible-expense
  addback, Schedule IT-20FSD foreign-source dividend deduction, and the
  corporate estimated-tax/underpayment mechanics (Schedule IT-2220).
  Trigger on "Indiana corporate income tax", "IT-20", "Indiana combined
  report", "Indiana Schedule E", "Indiana corporate estimated tax".
  Source-cited draft; DOR form inventory read from in.gov 2026-10-27,
  statute text not machine-readable this run (iga.in.gov SPA).
jurisdiction: US-IN
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - in-income-tax
---

# Indiana corporate income tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-27. Indiana's corporate tax is a **flat tax on adjusted gross income** (IC 6-3, subchapters on corporate AGI tax). **Source status:** the DOR current-year corporate form inventory (IT-20 booklet, Schedules E, E-7, F, IT-20PIC, IT-20FSD, M, IT-2220, IT-20NOL, 8-D, RECAP, NOL-MOD, IT-20X) was read from in.gov 2026-10-27 — form IDs verified. **iga.in.gov is a JavaScript SPA that returns no server-side statute text to plain HTTP; Justia mirror 403'd** — so the **rate (2.5% flat since the 2022 reduction, IC 6-3-2-1) and the combined-report ownership test are carried as needs-sources** pending a CPA check against IC 6-3-2-1. Never rely on the rate figure without confirming it against the current statute.

## 2. Who applies

- **C corporations** file Form IT-20 (DOR "Choosing the Proper Income Tax Form" page, read 2026-10-27: "Corporation: The corporation must file a Form IT-20").
- **S corporations** file IT-20S (same page) — income taxed once at shareholder level.
- **Partnerships/LLPs/LPs** file IT-65; partners report on IT-40/IT-40PNR (same page).
- **Nonprofits:** exempt status requires IRS recognition **plus** an Indiana application (NP-20A); then IT-20NP/NP-20 (same page, read 2026-10-27).
- **Affiliated groups** file a combined report — Schedule 8-D "Schedule of Indiana Affiliated Group Members" exists in the current form inventory (verified); the ownership test (80%-type) is **needs-sources**.

## Rates, bands and thresholds

| Item | Rule | Source status |
|---|---|---|
| Rate | **flat 2.5%** on Indiana adjusted gross income (post-2022 HEA 1004 reduction from 5%) | **needs-sources** — IC 6-3-2-1 text not machine-readable this run |
| Base | federal taxable income with Indiana modifications; Schedule IT-20 RECAP "Reconciliation of Federal Taxable Income" is the bridge form | form verified 2026-10-27 |
| Apportionment | **Schedule E "Apportionment of Income for Indiana"** — single sales factor per DOR form set; Schedule E-7 for interstate transportation | forms verified 2026-10-27; factor detail needs-sources |
| Non-business income | Schedule F "Allocation of Non-Business Income and Indiana Non-Unitary Partnership Income" | form verified 2026-10-27 |
| Addbacks | Schedule IT-20PIC "Disclosure of Intangible Expense and Directly Related Interest Expense" | form verified 2026-10-27; scope needs-sources |
| Foreign dividends | Schedule IT-20FSD "Foreign Source Dividend Deduction" | form verified 2026-10-27 |
| Alternate calculation | Schedule M "Alternate Adjusted Gross Income Tax Calculation" | form verified 2026-10-27 |

## The taxable base

The taxable base follows the mechanics described under Rates, bands and thresholds above.

## Deadlines and filing

- IT-20: due the **15th day of the 4th month** after the tax year ends (calendar-year filers April 15) — standard corporate calendar; **needs-sources** (DOR deadlines page 404 this run).
- Estimated tax: quarterly vouchers (88-ES series); underpayment penalty computed on **Schedule IT-2220 "Penalty for Underpayment of Corporate Income Tax"** (form verified 2026-10-27).
- Extension: federal extension generally honored — **needs-sources**.

## 5. Penalties and interest

- Underpayment of estimates: Schedule IT-2220 mechanics (form verified).
- Late filing/payment penalties and interest under IC 6-8.1 — percentages **needs-sources**.
- NOL tracking: Schedule IT-20NOL and Schedule NOL-MOD exist in the current inventory (forms verified 2026-10-27).

## Cross-border points

- Out-of-state corporations doing business in Indiana: apportion via Schedule E; Indiana follows public-law-280-type protections — **needs-sources**.
- Combined reporting pulls out-of-State affiliates into the Indiana report (Schedule 8-D) — test **needs-sources**.
- Foreign-source dividends: Schedule IT-20FSD deduction (form verified).
- Intangibles parked in low-tax affiliates: Schedule IT-20PIC addback disclosure (form verified; scope needs-sources).

## Worked examples

C corporation, $2,000,000 Indiana-scheduled AGI:

```oa-check
name: IN corporate flat tax
inputs:
  agi: 2000000
  rate: 0.025
steps:
  - tax: agi * rate
expected:
  tax: 50000.00
```

(Rate carried at 2.5% per the post-2022 statute — **confirm against IC 6-3-2-1 before use**.)

Same corporation shifts $500,000 of intangible expense (royalties) to a related affiliate; the addback schedule restores it:

```oa-check
name: IN IT-20PIC addback effect
inputs:
  intangible_expense: 500000
  rate: 0.025
steps:
  - added_tax: intangible_expense * rate
expected:
  added_tax: 12500.00
```

## Ask the client first

- Is the group an affiliated group requiring a combined report (Schedule 8-D members listed)?
- Royalty/management-fee flows to low-tax affiliates — IT-20PIC addback analyzed?
- Estimated payments sized against IT-2220 exposure?
- Foreign-source dividends — IT-20FSD deduction claimed?

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

## Sources

1. Indiana DOR current corporate/partnership forms (IT-20 + schedules): https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/ (200, read 2026-10-27)
2. Indiana DOR choosing the proper income tax form: https://www.in.gov/dor/i-am-a/business-corp/choosing-the-proper-income-tax-form/ (200, read 2026-10-27)
3. Indiana Code IC 6-3 (corporate AGI tax): https://iga.in.gov/laws/2025/ic/titles/6 (200 but SPA — no server-side text; **needs-sources**)
4. Indiana DOR corporate forms index: https://www.in.gov/dor/tax-forms/corporate/ (200, read 2026-10-27)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Indiana corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
