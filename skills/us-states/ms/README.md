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
as_of: 2026-10-28
---

# Mississippi (US-MS) — pack map

Mississippi phases its individual income tax down on schedule (docketed rate changes verified on the DOR rates page 2026-10-28: **2025 — 0% on the first $10,000 then 4.4%; 2026 — 4%; 2027 — 3.75%**), taxes corporations under Title 27 Chapter 7 Article 1 with a **combined-report regime (Form 83-310; 90%-of-current-year estimate rule tied to Form 83-105)** (verified), and charges sales tax at state + local rates (pre-existing `ms-sales-tax.md`). Employer withholding is **mandatory-electronic through TAP** with a **$25-per-return paper penalty capped at $500 (MCA § 27-3-83(4))**, and **10+ W-2s must be filed electronically** (verified). Unemployment is administered by MDES (reporting/filing page verified; rate tables needs-sources).

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing) | `ms-income-tax.md` | 80-100; 2025–2027 rate phase-down verified |
| IT-CORP corporate income | drafted 2026-10-28 | `ms-corporate-income-tax.md` | statute + combined-report rails verified; 3/4/5% rate table needs-sources |
| VAT sales/use | drafted (pre-existing) | `ms-sales-tax.md` | state + local |
| SC social contributions | drafted 2026-10-28 | `ms-social-contributions.md` | MDES rails verified; wage base/rates needs-sources |
| PR payroll withholding | drafted 2026-10-28 | `ms-payroll.md` | TAP mandate + § 27-3-83(4) penalties verified; form IDs/frequencies needs-sources |
| TP transfer pricing | drafted 2026-10-28 | `ms-transfer-pricing.md` | combined report 83-310 verified; standalone TP needs-sources |
| XB cross-border | drafted 2026-10-28 | `ms-cross-border.md` | rate phase-down verified; nonresident mechanics needs-sources |

All seven domains apply — no not_applicable entries. Mississippi franchise tax (Title 27 Ch. 13) is noted inside the corporate skill, not a separate domain.

## Key sources (read 2026-10-28)

- DOR individual rates: https://www.dor.ms.gov/taxes/individual-income-tax — **2025: 0% first $10,000 / 4.4% excess; 2026: 4%; 2027: 3.75%** (page fetched, verified)
- DOR combined filing: https://www.dor.ms.gov/taxes/combined-filing — **combined report Form 83-310; combined group members; 90% current-year estimate requirement; Form 83-105 corporate estimated tax** (verified)
- DOR withholding / TAP: https://www.dor.ms.gov/taxes/withholding — **electronic filing via TAP required; § 27-3-83(4) penalty $25 per return up to $500 for paper filing; W-2/1099 electronic mandate at 10+ information returns** (verified)
- MDES employer reporting: https://www.mdes.ms.gov/ (reporting-and-filing page) — resolves; UI rate tables needs-sources
- Statute: Miss. Code Ann. Title 27 Ch. 7 Art. 1 (income taxes), Ch. 13 (franchise tax) — chapter structure verified via DOR pages; section-level cites needs-sources

## Open items for reviewer

- Corporate rate table (3%/4%/5% bands) and Form 83-100 identity; franchise tax rates.
- UI taxable wage base and experience-rate schedule (MDES tables not fetched).
- Withholding form ID (82-111?) and deposit frequency thresholds.
- Nonresident return mechanics (80-205?) and credit-for-taxes-paid treatment.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Mississippi questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
