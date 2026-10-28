---
pack: US-LA
jurisdiction: US-LA
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

# Louisiana (US-LA) — pack map

Louisiana taxes individuals at a **flat 3%** (effective 2025, Act 11 of 2024 3rd ExSess — per the pre-existing `la-income-tax.md` and LDR RIB 25-012), corporations at a **flat 5.5%** for tax periods beginning on or after January 1, 2025 (graduated brackets repealed — LDR Corporation Income Tax page, verified 2026-10-28), and sales at 4.45% state plus heavy local parishes. The **corporation franchise tax is repealed** for franchise tax periods beginning on or after January 1, 2026 (LDR page, verified). Individual and corporate returns are due **May 15** (15th day of the 5th month — verified on the LDR corporate page). Employer social cost is UI-only (Workforce Commission, lwc.org — 403 to plain HTTP this run, figures needs-sources).

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing) | `la-income-tax.md` | flat 3%, IT-540, May 15 deadline |
| IT-CORP corporate income | drafted 2026-10-28 | `la-corporate-income-tax.md` | CIFT-620, flat 5.5% verified, franchise repeal verified |
| VAT sales/use | drafted (pre-existing) | `la-sales-tax.md` | 4.45% state + parish/local |
| SC social contributions | drafted 2026-10-28 | `la-social-contributions.md` | UI-only via LWC; wage base/rates needs-sources (lwc.org 403) |
| PR payroll withholding | drafted 2026-10-28 | `la-payroll.md` | L-1 quarterly + L-3 annual verified from LDR page incl. payment-frequency bands |
| TP transfer pricing | drafted 2026-10-28 | `la-transfer-pricing.md` | no standalone TP docs regime; unitary/combined + addback exposure needs-sources |
| XB cross-border | drafted 2026-10-28 | `la-cross-border.md` | IT-540B nonresident routing; no reciprocity, no exit tax; credit mechanics needs-sources |

All seven domains apply to Louisiana — no not_applicable entries (franchise repeal is noted inside the corporate skill).

## Key sources (read 2026-10-28)

- LDR Corporation Income Tax page: https://revenue.louisiana.gov/businesses/widely-used-tax-types/corporate-income-franchise-tax/ — **flat 5.5% for periods beginning on/after 2025-01-01; franchise tax repealed for periods beginning on/after 2026-01-01; due 15th day of 5th month (May 15 calendar filers); $1,000 estimated-tax threshold; CIFT-620 + CIFT-620EXT-V; automatic 6-month extension if federal extension timely** (page updated July 07, 2026)
- LDR Withholding page: https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/ — **L-1 quarterly (zero returns required), L-3 annual reconciliation due Jan 31 (or 30 days after final wages), e-file mandatory via LaTAP/LaWage, frequency bands: <$500 quarterly, $500–<$5,000 monthly, ≥$5,000 semi-monthly; residents working in another state may still be LA-withheld if that state doesn't withhold**
- LDR withholding tables: https://revenue.louisiana.gov/tax-professionals/general-resources/louisiana-withholding-tax-tables/ — page resolves; table content JS-rendered, figures needs-sources
- LDR RIB 25-012 (income tax reform, flat 3%): https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf — verified PDF 2026-10-28
- La. R.S. 47 (statutes): https://legis.la.gov/legis/Laws_Toc.aspx?folder=90&title=47 — resolves (269KB HTML) but article-level text requires session state; specific cites needs-sources
- LWC (UI): https://www.lwc.org/ — 403 Forbidden to plain HTTP this run — UI figures needs-sources

## Open items for reviewer

- 2026 UI taxable wage base and experience-rate schedule (lwc.org blocked).
- Withholding table figures (JS-rendered page).
- Combined-report/unitary requirement and form (LA unitary-combination under R.S. 47:287.83 expected — verify).
- Nonresident credit statute citation and IT-540B routing detail.
- Partnership tax (LI-005) interaction with TP/XB skills.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Louisiana questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
