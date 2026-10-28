---
name: il-corporate-income-tax
description: >
  Use this skill whenever asked about Illinois corporate income tax
  for tax year 2026 — the 7.0% income tax plus 2.5% replacement tax
  on Illinois-apportioned net income (9.5% combined), Form IL-1120
  mechanics, estimated tax via IL-1120-V above the $400 threshold,
  the IL-2220 underpayment penalty, and unitary combined reporting
  through Schedule UB. Trigger on "Illinois corporate tax", "IL-1120",
  "Illinois replacement tax", "Illinois corporation income tax rate",
  "Illinois estimated tax corporation", "Schedule UB". Source-cited
  draft; IL-1120 (R-12/25) form + 24-page instructions PDFs read
  2026-10-27.
jurisdiction: US-IL
category: corporate
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - il-income-tax
---

# Illinois corporate income + replacement tax v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Scope and sources

Source-cited draft, run of 27 October 2026. Illinois taxes corporations under the Income Tax Act (35 ILCS 5) with a two-component levy on the same base: a **7.0% income tax** and a **2.5% replacement tax**, both computed on Illinois net income after apportionment — a combined 9.5% effective rate. **Source status:** Form IL-1120 (R-12/25, for tax years ending on/after 2025-12-31 and before 2026-12-31 — i.e., the 2026 calendar-year return) and its 24-page instructions PDF were downloaded and text-read 2026-10-27 from tax.illinois.gov; the rate lines ("Multiply Line 39 by 7.0%", "Multiply Line 39 by 2.5%", estimated worksheet "9.5 percent") are read directly from those PDFs. The ILCS section pages render via JavaScript and did not yield text this run — statutory cites carry **needs-sources** for section-level text.

## 2. Who applies

- Corporations (including foreign insurers, cooperatives under IRC 1381, settlement funds under IRC 468B, and political organizations filing federal 1120-POL/1120-H per the instructions) that (per the IL-1120 instructions): do business in Illinois, derive income from Illinois sources, **or** are qualified to do business in Illinois and required to file a federal return — regardless of net income or loss.
- Unitary business group members file combined apportionment on Illinois Schedule UB (box "Unitary Filer" on IL-1120 Step 1 Line E).
- S corporations pay the replacement tax component (see `il-income-tax` for the shareholder side).

## 3. Rates and base

| Item | Rate / base | Source |
|---|---|---|
| Corporate income tax | **7.0%** of Illinois net income (IL-1120 Line 45) — re-VERIFIED vs archived IL-1120 PDF (2026-10-28): "Income tax. Multiply Line 39 by 7.0% (.07)"; "Replacement tax. Multiply Line 39 by 2.5% (.025)" | IL-1120 (R-12/25) PDF, archived 2026-10-28 |
| Corporate replacement tax | **2.5%** of Illinois net income (IL-1120 Line 40) | same PDF, read 2026-10-27 |
| Combined effective | 9.5% (IDOR estimated-payment worksheet uses 9.5%) | IL-1120 instructions PDF, read 2026-10-27 |
| Base | "Net income" = adjusted base income after Illinois modifications, net loss deduction, and apportionment (Steps 3–5 of IL-1120) | IL-1120 PDF |
| Apportionment | single sales factor for most corporations; special formulas for sales/insurance/financial/transportation companies (Step 1 Line G); unitary groups use Schedule UB with the **Finnigan** method for tax years ending on/after 2025-12-31 | IL-1120 instructions, read 2026-10-27 |
| Related-party expenses | Schedule 80/20 addback of interest/intangible expenses and service fees to related affiliates (with exemptions) | IL-1120 instructions, read 2026-10-27 |

## 4. Deadlines

- **Return:** IL-1120 due on the same date as the federal return — 15th day of the 4th month after year close (April 15 for calendar-year filers); special rule for June-30 year-ends per instructions.
- **Estimated tax:** required if expected IL income + replacement tax + surcharge exceeds **$400**; quarterly IL-1120-V payments due 4/15, 6/15, 9/15, 12/15 for calendar-year filers (dates read from instructions examples).
- **Extension:** automatic 7-month filing extension, but tentative tax must be paid by the **original** due date to stop penalty/interest (instructions, read 2026-10-27).
- Amended returns: IL-1120-X.

## 5. Penalties and interest

Per the IL-1120 instructions (read 2026-10-27): late-filing penalty (return not processable by extended due date), late-payment penalty (tax unpaid at original due date), estimated-tax underpayment penalty (self-assessed on **Form IL-2220**, Step 4 Line 22; annualization available at Step 6), and bad-check penalty. Current penalty percentages and the 35 ILCS 5/806 interest rate: **needs-sources** (not in the extracted text). Common failure modes: (1) assuming the extension extends payment — it does not; (2) forgetting the replacement tax stacks on the same base; (3) unitary filers checking the "income derived inside Illinois only" box, which the form prohibits for unitary filers.

## 6. Cross-border interactions

- Non-IL corporations with IL nexus file IL-1120 and apportion by the single sales factor; throwback/throwout rules apply per statute (Finnigan method for unitary groups from TYE 2025-12-31 — instructions, read 2026-10-27).
- Schedule 80/20 curbs base-erosion payments (interest, intangibles, service fees) to related parties — Illinois's main related-party lever (see `il-transfer-pricing`).
- PTE: the pass-through entity tax has its expiration date removed per the 2025-26 amendments noted in the instructions; corporations receive K-1-P/K-1-T credits on Lines 61c/61d.
- Credit for IL tax paid by pass-throughs flows via Schedule K-1-P/K-1-T (Lines 61c–61d verified on form).

## 7. Worked examples

A calendar-year C corporation with $1,000,000 Illinois-apportioned net income for 2026:

```oa-check
name: IL corporate combined tax
inputs:
  net_income: 1000000
  income_rate: 0.07
  repl_rate: 0.025
steps:
  - income_tax: net_income * income_rate
  - repl_tax: net_income * repl_rate
  - total: income_tax + repl_tax
expected:
  income_tax: 70000.00
  repl_tax: 25000.00
  total: 95000.00
```

Same corporation, 40% apportionment factor on $2,500,000 base income:

```oa-check
name: IL tax at 40 percent apportionment
inputs:
  base: 2500000
  app: 0.40
  combined: 0.095
steps:
  - il_net: base * app
  - tax: il_net * combined
expected:
  il_net: 1000000.00
  tax: 95000.00
```

## 8. Ask the client

- Is the entity in a unitary business group — does Schedule UB combined reporting apply, and is the Finnigan method now in play for 2026?
- Are there related-party interest, royalty, or service-fee payments requiring Schedule 80/20?
- Are estimated IL-1120-V payments on track against the 9.5% combined rate?
- Any June-30 fiscal year-end special due date, or foreign-insurer/cooperative status?

## Sources

1. Form IL-1120 (R-12/25) PDF: https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/business/corporate/il-1120.pdf (200 PDF, text read 2026-10-27)
2. IL-1120 instructions PDF: https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/business/corporate/il-1120-instr.pdf (200 PDF, text read 2026-10-27)
3. Form IL-1120-V voucher PDF: https://tax.illinois.gov/content/dam/soi/en/web/tax/forms/incometax/documents/currentyear/business/corporate/il-1120-v.pdf (200 PDF, read 2026-10-27)
4. 35 ILCS 5 (Income Tax Act): https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=592&ChapterID=8 (200 frame page; article text JS-rendered — section-level cites **needs-sources**)

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Illinois corporate questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
