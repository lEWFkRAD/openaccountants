---
name: in-transfer-pricing
description: >
  Use this skill whenever asked about Indiana related-party pricing and
  combined reporting for tax year 2026 -- Indiana's affiliated-group
  combined report (Schedule 8-D), the intangible expense and directly
  related interest addback disclosure (Schedule IT-20PIC), foreign-source
  dividend deduction (Schedule IT-20FSD), single-sales-factor apportionment
  (Schedule E), and the PTET election's interaction with entity-level
  planning. Trigger on "Indiana transfer pricing", "Indiana combined
  report", "Indiana affiliated group", "IT-20PIC", "Schedule 8-D",
  "Indiana addback", "Indiana Schedule E". Source-cited draft; DOR form
  inventory verified from in.gov 2026-10-27, statute text pending confirmation.
jurisdiction: US-IN
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - in-corporate-income-tax
---

# Indiana transfer pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 2026-10-27. Indiana's related-party toolkit is **elective consolidated returns and petition-only unitary combined returns** plus the **intangible-expense addback disclosure** -- both visible in the DOR current-year corporate form inventory (read 2026-10-27): Schedule 8-D "Schedule of Indiana Affiliated Group Members", Schedule IT-20PIC "Disclosure of Intangible Expense and Directly Related Interest Expense", Schedule IT-20FSD "Foreign Source Dividend Deduction", Schedule E "Apportionment of Income for Indiana", Schedule F "Allocation of Non-Business Income and Indiana Non-Unitary Partnership Income". **Source status:** form names/IDs verified from in.gov; iga.in.gov is a SPA with no server-side statute text this run. The consolidated and combined filing rules below are from the DOR IT-20 booklet 2025; the addback mechanics are listed under Not yet confirmed below.

### Who applies

- Corporations in an **affiliated group** may elect a consolidated Indiana return if the parent owns at least 80% of each subsidiary's voting stock and at least 80% of total stock value; members are listed on Schedule 8-D (IT-20 booklet 2025, Consolidated Reporting). A **unitary combined** return is filed only with DOR permission, on a petition filed no later than 30 days after the end of the tax year (IT-20 booklet, Unitary (Combined) Filing Status).
- Any IT-20 filer with **intangible expenses paid to related parties** -- IT-20PIC disclosure (form verified via US-IN-dor-corp-forms.html; statutory trigger listed under Not yet confirmed).
- Non-unitary partnership income is carved out and allocated on Schedule F (form title verified 2026-10-27) -- Indiana's unitary-combination boundary is real and matters for holding structures.

## Rates, bands and thresholds

- **Consolidated or combined returns:** business income is apportioned on Schedule E by the single-factor receipts formula (IC 6-3-2-2; IT-20 booklet). In a combined return, members with a sales factor numerator greater than zero are taxable members, each assigned business income by its relative share of the group's Indiana sales factors (IT-20 booklet).
- **IT-20PIC:** discloses intangible expense (royalties, licensing) **and directly related interest expense** paid across state lines; Indiana's answer to royalty-shifting structures (scope listed under Not yet confirmed).
- **IT-20FSD:** foreign-source dividend deduction (form verified via US-IN-dor-corp-forms.html; eligibility listed under Not yet confirmed).
- **PTET (IN-PTET):** SEA 2 (2023) elective entity-level tax with refundable owner credit and a credit for other states' PTETs (DOR PTET page, read 2026-10-27) -- shifts the related-party analysis to the entity level for pass-throughs.

## The taxable base

The taxable base follows the mechanics described under Rates, bands and thresholds above.

## Deadlines and filing

- Consolidated and combined returns follow the IT-20 calendar: due the 15th day of the 5th month after the tax year ends (IT-20 booklet). A consolidated election is made on a timely filed return; a unitary combined petition is due no later than 30 days after the end of the tax year (IT-20 booklet).
- PTET election is annual with the entity return (per the DOR PTET page; exact dates listed under Not yet confirmed).

## Penalties and interest

- Underpayment: Schedule IT-2220 (form verified).
- IC 6-8.1 penalty/interest (percentages listed under Not yet confirmed).

## Cross-border points

- Royalty/interest flows from Indiana operating companies to out-of-State IP affiliates: IT-20PIC disclosure, potential addback (scope listed under Not yet confirmed).
- A consolidated return includes only affiliates with income or loss attributable to Indiana; combined reporting is limited to the water's edge of the United States unless DOR approves otherwise (IT-20 booklet).
- Other-state PTETs: Indiana grants a credit for PTET paid to another state (DOR PTET page, read 2026-10-27).

## Worked examples

Indiana opco pays $1,200,000 royalties + $300,000 directly related interest to a low-tax IP affiliate; tax if the full amount is added back on IT-20PIC, at the 4.9% corporate AGI tax rate (IT-20 booklet):

```oa-check
name: IN IT-20PIC exposure
inputs:
  royalties: 1200000
  interest: 300000
  rate: 0.049
steps:
  - disclosed: royalties + interest
  - tax_if_full_addback: disclosed * rate
expected:
  disclosed: 1500000.00
  tax_if_full_addback: 73500.00
```

Affiliated group with two Indiana members and one out-of-State member; combined Indiana-sourced income $3,400,000 vs standalone $3,000,000:

```oa-check
name: IN combined vs standalone delta
inputs:
  combined_income: 3400000
  standalone_income: 3000000
  rate: 0.049
steps:
  - delta_income: combined_income - standalone_income
  - delta_tax: delta_income * rate
expected:
  delta_income: 400000.00
  delta_tax: 19600.00
```

## Ask the client first

- Has the group elected consolidated filing (80% vote and value test), and are all members with Indiana income on Schedule 8-D? Has a unitary combined petition been filed within 30 days after year end?
- Royalty/licensing/management-fee flows to affiliates: IT-20PIC analyzed, transfer docs current?
- Non-unitary partnership interests: Schedule F treatment reviewed?
- PTET elected at the entity level -- other-state PTET credits captured?

---

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

## Sources

| Source | URL | Read on |
|---|---|---|
| Indiana DOR current corporate/partnership forms (Schedules 8-D, IT-20PIC, IT-20FSD, E, F) | https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/ | 2026-10-28 |
| Indiana DOR, IT-20 Corporate Income Tax Booklet 2025 (SP 259) | https://forms.in.gov/Download.aspx?id=16945 | 2026-11-01 |
| Indiana DOR PTET page (SEA 2, 2023; IN-PTET form; other-state credit) | https://www.in.gov/dor/tax-forms/other-forms/ptet/ | 2026-10-29 |
| Indiana Code IC 6-3 (combined report, addback; iga.in.gov SPA -- no server-side text captured) | https://iga.in.gov/laws/2025/ic/titles/6 | 2026-10-28 |

Not yet confirmed: the IT-20PIC statutory trigger and addback exceptions; IT-20FSD eligibility; the PTET election dates; IC 6-8.1 penalty and interest percentages.

<!-- openaccountants-cta-block -->

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