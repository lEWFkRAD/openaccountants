---
name: me-corporate-income-tax
description: >
  Use this skill whenever asked about Maine corporate income tax for tax
  year 2026 — the graduated corporate rate from 3.5% (income up to
  $350,000) to 8.93% (income over $3,500,000), Form 1120ME, unitary
  business and combined reporting under Rule 810, apportionment under
  Rule 801, nexus under Rule 808, and the treatment of S corporations and
  financial institutions. Trigger on "Maine corporate income tax",
  "1120ME", "Maine corporation tax", "Maine combined report", "Maine
  unitary". Source-cited draft; rate range, S-corp scope, franchise-tax
  carve-out and rule numbers verified on the MRS 1120ME page
  2026-10-28; middle bracket, deadlines and estimated-payment detail
  needs-sources.
jurisdiction: US-ME
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.1
verified_by: pending
depends_on:
  - me-income-tax
---

# Maine corporate income tax v0.1

> **General reference only.** General tax reference for AI-assisted workflows; not reviewed for any specific client's facts. Do not file, pay, or take a position on this alone — use a qualified Maine practitioner.

## 1. Scope and sources

Source-cited draft, run of 2026-10-28. Covers Maine corporation income tax (Form 1120ME), rates, unitary/combined reporting, and filing mechanics. **Source status:** the MRS Corporate Income Tax (1120ME) page (https://www.maine.gov/revenue/taxes/income-estate-tax/corporate-income-tax-1120me) was fetched and its text verified 2026-10-28 — the **3.5%–8.93% graduated range with the $350,000 / $3,500,000 endpoints, the S-corporation carve-out, the financial-institution franchise-tax carve-out, and Rules 801/808/810 are verified quotes**. The **middle bracket rate, the return due date, and estimated-payment thresholds sit in the 1120ME instructions, not fetched this run — needs-sources**.

## 2. Who applies

Per the MRS page (verified 2026-10-28):

- **All entities organized as corporations** with Maine-source income;
- **S corporations only if the corporation has federal taxable income at the corporate level** (e.g., built-in gains, passive investment income) — otherwise pass-through treatment;
- **Not** financial institutions subject to Maine's franchise tax (Form 1120B-ME) and **not** insurance companies subject to the premiums tax;
- Combined reports required for members of a **unitary business** group — Rule 810 (Maine Unitary Business Taxable Income, Combined Reports and Tax Returns); nexus per Rule 808; apportionment per Rule 801.

## 3. Rates (tax year 2026 filing year; verify brackets)

| Maine taxable income | Rate | Source status |
|---|---|---|
| Up to $350,000 | 3.5% | verified (MRS page) |
| $350,000 – $3,500,000 | 7.93% expected | **needs-sources** (middle bracket not on the page; page states range "3.5% … to 8.93%") |
| Over $3,500,000 | 8.93% | verified (MRS page) |

## 4. Base and apportionment

Maine taxable income starts from federal taxable income with Maine modifications (statute: 36 M.R.S. Title 36 Part 8 — specific modification cites **needs-sources**). Apportionment under **Rule 801** (verified to exist); the factor mix (single sales factor expected) **needs-sources**. Unitary-group combined reporting under **Rule 810** (verified to exist); scope detail **needs-sources**.

## 5. Deadlines, estimates, penalties

- Form 1120ME due date: expected April 15 (federal conformity) — **needs-sources**.
- Estimated payments: threshold and installments **needs-sources**.
- Late-filing/late-payment penalty and interest rates: **needs-sources** (MRS publishes an interest-rate table page: https://www.maine.gov/revenue/ — rates page not fetched).

## 6. Cross-border notes

- Nexus is Rule 808 (public-law thresholds unverified — **needs-sources**).
- Maine taxes nonresident owners' Maine-source income; pass-through entity withholding via Form 941P-ME and composite filing are the collection rails (verified — see `me-payroll.md` and `me-cross-border.md`).

## 7. Worked examples

**Example 1 — small C corp, fully apportioned to Maine.** Maine taxable income $300,000 (all Maine):

```oa-check
name: ME corporate 3.5% band
inputs:
  income: 300000
  rate_low: 0.035
steps:
  - band_low: min(income, 350000) * rate_low
  - tax: band_low
expected:
  tax: 10500.00
```

**Example 2 — $4,000,000 Maine taxable income** (middle bracket 7.93% flagged needs-sources):

```oa-check
name: ME corporate graduated 4M
inputs:
  income: 4000000
  rate_low: 0.035
  rate_mid: 0.0793
  rate_high: 0.0893
steps:
  - band_low: min(income, 350000) * rate_low
  - band_mid: (min(income, 3500000) - 350000) * rate_mid
  - band_high: max(income - 3500000, 0) * rate_high
  - tax: band_low + band_mid + band_high
expected:
  tax: 306695.00
```

## 8. Ask the client

- Is the entity part of a unitary group (common ownership + integrated operations)? → combined report under Rule 810.
- Any factor presence (property, payroll, sales) in Maine that could create Rule 808 nexus?
- Is the S corp carrying federal corporate-level taxable income (built-in gains, passive income)?
- Intercompany management/royalty fees paid out of Maine (addback exposure — **needs-sources**)?

## 9. Sources

1. MRS Corporate Income Tax (1120ME): https://www.maine.gov/revenue/taxes/income-estate-tax/corporate-income-tax-1120me — fetched and verified 2026-10-28 (rate range, carve-outs, Rules 801/808/810).
2. 36 M.R.S. § 5111 (individual rate statute, context for surcharge): https://legislature.maine.gov/statutes/36/title36sec5111.html — fetched 2026-10-28.
3. MRS Employer Withholding (941ME/ME UC-1): https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding — fetched 2026-10-28.

**Needs-sources:** middle bracket 7.93%, 1120ME due date, estimated-payment thresholds, penalty/interest percentages, Rule 801 factor mix, Rule 810 combined-report scope, franchise-tax (1120B-ME) rates.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Maine corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
