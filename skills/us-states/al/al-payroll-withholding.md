---
name: al-payroll-withholding
description: >
  Use this skill whenever asked about Alabama payroll withholding for
  tax year 2026 — Form A-1 (withholding return) and A-2 (annual
  reconciliation), A-3 (non-resident real-estate withholding), A-6
  (withholding on non-payroll compensation), bulk-filer registration
  (Form BF-1), the A-1/A-6 file-layout change effective 2024-01-27
  for overtime-exemption reporting, and Alabama withholding on
  non-resident members of pass-through entities. Trigger on "Alabama
  withholding", "Alabama A-1", "Alabama A-6", "Alabama bulk filing",
  "Alabama composite return", "Alabama overtime exemption W-2".
  Source-cited draft; ALDOR withholding page read 2026-10-27.
jurisdiction: US-AL
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - al-income-tax
---

# Alabama payroll withholding v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Alabama individual income tax withholding runs through the Alabama Department of Revenue (ALDOR) on Forms **A-1** (return of income tax withheld), **A-2** (annual reconciliation), **A-3** (withholding on non-resident real-estate / mineral proceeds), and **A-6** (withholding on non-payroll compensation — the composite/pass-through withholding vehicle). **Source status:** the ALDOR Withholding page was fetched 2026-10-27 (200, text read): bulk-filer registration via **Form BF-1**, file types **A-1/A-6** and **A-3**, comma-delimited .csv/.txt layouts, and the notice that the **A-1/A-6 bulk layout changed for files uploaded after 2024-01-27** to add the overtime-exemption fields ("Number of Employees with Exempt Overtime Wages", "Total Amount of Exempt Overtime Wages Paid", "No Exempt Overtime Wages Paid to Report" flag). Deposit frequency, rate tables, and penalty percentages are **needs-sources** (form PDFs not retrievable this run).

## 2. Who applies

- Every employer paying Alabama-source wages withholds on the ALDOR tables (with Form A-4 employee certificate) — table mechanics **needs-sources**.
- **Bulk filers** (agents filing for multiple employers) must register with ALDOR via Form BF-1 and use their bulk registration on every submission (ALDOR page, read 2026-10-27).
- Payers of non-payroll compensation (pass-through distributions, certain non-resident payments) withhold under A-6 rules (statutory trigger — Ala. Code §40-18-411 et seq. — text **needs-sources**).
- Buyers of Alabama real estate from non-residents withhold under A-3 (percentage **needs-sources**).

## 3. Mechanics and rates

| Item | Value | Source |
|---|---|---|
| A-1 withholding tables | graduated per ALDOR tables — **needs-sources** | Form A-1 not retrievable this run |
| Deposit frequency | monthly/semi-monthly by liability tier — **needs-sources** | ALDOR page (no schedule in page text) |
| A-3 non-resident real-estate withholding | percentage **needs-sources** | Ala. Code §40-18-413 — not fetched |
| Overtime-exemption W-2 reporting | fields required in A-1/A-6 bulk files after 2024-01-27 | ALDOR page, read 2026-10-27 |

The overtime-exemption reporting ties to Alabama's 2024 overtime-pay-preemption statute: W-2s must flag exempt-overtime wages (fields read from the ALDOR page 2026-10-27; underlying statute text **needs-sources**).

## 4. Deadlines

- **A-1 returns + deposits:** monthly (pattern — exact frequency tiers **needs-sources**).
- **A-2 annual reconciliation + W-2/1099 copies:** due January 31 (pattern; confirm — **needs-sources**).
- **Bulk uploads:** same due dates; layout must match the post-2024-01-27 A-1/A-6 spec (ALDOR page, read 2026-10-27).

## 5. Penalties and interest

Failure-to-file/failure-to-deposit penalties and interest under Ala. Code §40-2A-1 et seq. — percentages **needs-sources**. Common failure modes: (1) bulk filers uploading pre-2024 layouts after the cutover (zeros + the "no exempt overtime wages" flag are required, not blank fields); (2) treating A-6 as optional for pass-through distributions; (3) A-3 missed on non-resident property sales.

## 6. Cross-border interactions

- Non-resident members of Alabama-sourcing partnerships/LLCs are covered by composite withholding (A-6) — see `al-cross-border`.
- Reciprocity: Alabama has **no** withholding reciprocity with neighboring states (verify — **needs-sources**); remote workers trigger Alabama withholding once Alabama wages exist.

## 7. Worked examples

An employer withholds $12,400 of Alabama income tax in a month and deposits in full by the due date; a late deposit draws a 5% FTD penalty (illustrative rate — **needs-sources**):

```oa-check
name: AL FTD penalty illustrative
inputs:
  deposit: 12400
  penalty_rate: 0.05
steps:
  - penalty: deposit * penalty_rate
expected:
  penalty: 620.00
```

Bulk filer submitting 3 employers × 12 monthly A-1s in one year:

```oa-check
name: AL bulk filing volume
inputs:
  employers: 3
  months: 12
steps:
  - filings: employers * months
expected:
  filings: 36.00
```

## 8. Ask the client

- Are bulk uploads on the post-January-2024 A-1/A-6 layout with the overtime-exemption fields populated (zeros + flag when none)?
- Is A-6 withholding being run for non-resident pass-through members?
- Are A-3 withholdings captured on non-resident real-estate closings?
- Is the deposit frequency tier current after a growth year?

## Sources

1. ALDOR Withholding page: https://revenue.alabama.gov/taxes-fees/withholding/ (200, text read 2026-10-27 — bulk-filer registration BF-1, A-1/A-6 and A-3 layouts, 2024-01-27 layout change and overtime-exemption fields)
2. Form BF-1: linked from the ALDOR withholding page (updated 2016-05-02 per page)
3. Ala. Code Title 40 ch. 18 art. 11 (withholding): https://law.justia.com/codes/alabama/title-40/ (not fetched — **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Alabama withholding questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
