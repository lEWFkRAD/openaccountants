---
pack: US-MS
jurisdiction: US-MS
applicable:
  - IT-IND
  - IT-CORP
  - VAT
  - SC
  - PR
  - TP
  - XB
not_applicable: {}
as_of: 2026-10-29
---

# Mississippi (US-MS) — pack map

Mississippi phases its individual income tax down on schedule (docketed rate changes verified on the DOR Tax Rates page 2026-10-28: **2025 — 0% on the first $10,000 then 4.4%; 2026 — 4%; 2027 — 3.75%**), taxes corporations under Title 27 Chapter 7 Article 1 at **0% on the first $5,000, 4% on the next $5,000, 5% above $10,000 (verified in the archived 2025 Form 83-100 instructions)** with a **combined-report regime (Form 83-310 filed with the reporting corporation's Form 83-105; 90%-of-current-year estimate rule)** (verified), and charges sales tax at state + local rates (pre-existing `ms-sales-tax.md`). Employer withholding is **mandatory-electronic through TAP** with a **$25-per-return paper penalty capped at $500 (MCA § 27-3-83(4))**, and **10+ W-2s must be filed electronically** (verified). Unemployment is administered by MDES (new-employer rates 1.00%/1.10%/1.20%, quarterly due dates, and interest/penalty rules verified on mdes.ms.gov 2026-10-29).

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | corrected 2026-10-29 | `ms-income-tax.md` | 80-100 instructions + DOR rates page: rates, deductions, exemptions, deadlines, penalties verified |
| IT-CORP corporate income | corrected 2026-10-29 | `ms-corporate-income-tax.md` | 2025 Form 83-100 instructions: 0%/4%/5% rate table, due dates, penalties, franchise rate verified |
| VAT sales/use | drafted (pre-existing) | `ms-sales-tax.md` | state + local |
| SC social contributions | corrected 2026-10-29 | `ms-social-contributions.md` | MDES rates/due dates/penalties verified; wage base open |
| PR payroll withholding | corrected 2026-10-29 | `ms-payroll.md` | TAP mandate + § 27-3-83(4) penalties + 3% gambling withholding verified; form ID open |
| TP transfer pricing | corrected 2026-10-29 | `ms-transfer-pricing.md` | combined report 83-310/83-105, 90% estimates verified; addbacks open |
| XB cross-border | corrected 2026-10-29 | `ms-cross-border.md` | 80-205 mechanics, 80-160 other-state credit, deadlines/penalties verified |

All seven domains apply — no not_applicable entries. Mississippi franchise tax (Title 27 Ch. 13) is noted inside the corporate skill, not a separate domain.

## Key sources (read 2026-10-28/29)

- DOR Tax Rates (General Information): https://www.dor.ms.gov/general-information — **2025: 0% first $10,000 / 4.4% excess; 2026: 4%; 2027: 3.75%**; filing thresholds, standard deductions, exemptions (fetched, verified)
- MSDOR 2025 Individual Income Tax Instructions (Form 80-100): https://www.dor.ms.gov/sites/default/files/tax-forms/individual/80100251%202.pdf — **April 15 due date, estimated-tax $200 threshold, penalties/interest, 80-205 part-year mechanics, 80-160 other-state credit, 3% gambling withholding** (fetched, verified)
- MSDOR 2025 Corporate Income & Franchise Tax Instructions (Form 83-100): https://www.dor.ms.gov/sites/default/files/tax-forms/business/2025%20CIT%20INSTRUCTIONS%2083-100%20-%20Final%20%2001.14.2026.pdf — **corporate 0%/4%/5% rate table, combination-return due date, penalties/interest, franchise $0.75 per $1,000 over $100,000 (min $25)** (fetched, verified)
- DOR Combined Income Filing: https://www.dor.ms.gov/business/corporate-income-franchise-tax/combined-income-filing — **affiliated-group election, Form 83-310 into Form 83-105 line 4, 90% estimates via Form 83-300** (verified)
- DOR Withholding Tax: https://www.dor.ms.gov/business/withholding-tax — **TAP filing/payment; § 27-3-83(4) $25/return up to $500 paper penalty; 10+ W-2 electronic mandate** (verified)
- MDES Unemployment Tax Rates / Quarterly Due Dates / Interest and Penalties: https://www.mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/ — **new-employer 1.00%/1.10%/1.20%; 0.0%–5.4% modified range; Apr 30/Jul 31/Oct 31/Jan 31 due dates; 1%/month interest, 10% late-filing/late-payment penalties** (verified)

## Open items for reviewer

- UI taxable wage base and per-employer experience-rate schedule table.
- Withholding form ID (82-111?) and deposit frequency thresholds.
- Combined-group membership tests (Title 35, Pt III, Sub 08, Ch 07) and water's-edge posture.
- Reciprocity agreements and any convenience-of-the-employer rule.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
