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

Louisiana taxes individuals at a **flat 3%** (effective 2025, Act 11 of 2024 3rd ExSess — per the pre-existing `la-income-tax.md` and LDR RIB 25-012), corporations at a **flat 5.5%** for tax periods beginning on or after January 1, 2025 (graduated brackets repealed — LDR Corporation Income Tax page, verified 2026-10-28), and sales at **5% state** from 2025-01-01 (4.45% through 2024-12-31 — LDR General Sales & Use Tax page, verified 2026-10-29) plus heavy local parishes. The **corporation franchise tax is repealed** for franchise tax periods beginning on or after January 1, 2026 (LDR page, verified). Individual and corporate returns are due **May 15** (15th day of the 5th month — verified on the LDR corporate page). Employer social cost is UI-only (Workforce Commission, lwc.org — 403 to plain HTTP this run, figures not confirmed).

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing) | `la-income-tax.md` | flat 3%, IT-540, May 15 deadline |
| IT-CORP corporate income | drafted 2026-10-28 | `la-corporate-income-tax.md` | CIFT-620, flat 5.5% verified, franchise repeal verified |
| VAT sales/use | rewritten 2026-10-29 | `la-sales-tax.md` | 5% state from 2025 (4.45% pre-2025) + parish/local; verified LDR pages |
| SC social contributions | drafted 2026-10-28 | `la-social-contributions.md` | UI-only via LWC; wage base/rates not confirmed (lwc.org 403) |
| PR payroll withholding | drafted 2026-10-28 | `la-payroll.md` | L-1 quarterly + L-3 annual verified from LDR page incl. payment-frequency bands |
| TP transfer pricing | drafted 2026-10-28 | `la-transfer-pricing.md` | no standalone TP docs regime; unitary/combined + addback exposure not confirmed |
| XB cross-border | drafted 2026-10-28 | `la-cross-border.md` | IT-540B nonresident routing; no reciprocity, no exit tax; credit mechanics not confirmed |

All seven domains apply to Louisiana — no not_applicable entries (franchise repeal is noted inside the corporate skill).

## Key sources (read 2026-10-28)

- LDR Corporation Income Tax page: https://revenue.louisiana.gov/businesses/widely-used-tax-types/corporate-income-franchise-tax/ — **flat 5.5% for periods beginning on/after 2025-01-01; franchise tax repealed for periods beginning on/after 2026-01-01; due 15th day of 5th month (May 15 calendar filers); $1,000 estimated-tax threshold; CIFT-620 + CIFT-620EXT-V; automatic 6-month extension if federal extension timely** (page updated July 07, 2026)
- LDR Withholding page: https://revenue.louisiana.gov/businesses/widely-used-tax-types/withholding/ — **L-1 quarterly (zero returns required), L-3 annual reconciliation due Jan 31 (or 30 days after final wages), e-file mandatory via LaTAP/LaWage, frequency bands: <$500 quarterly, $500–<$5,000 monthly, ≥$5,000 semi-monthly; residents working in another state may still be LA-withheld if that state doesn't withhold**
- LDR withholding tables: https://revenue.louisiana.gov/tax-professionals/general-resources/louisiana-withholding-tax-tables/ — page resolves; table content JS-rendered, figures not confirmed
- LDR RIB 25-012 (income tax reform, flat 3%): https://dam.ldr.la.gov/lawspolicies/RIB-25-012-Louisiana-Individual-Income-Tax-Reform-1.pdf — verified PDF 2026-10-28
- La. R.S. 47 (statutes): https://legis.la.gov/legis/Laws_Toc.aspx?folder=90&title=47 — resolves (269KB HTML) but article-level text requires session state; specific cites not confirmed
- LWC (UI): https://www.lwc.org/ — 403 Forbidden to plain HTTP this run — UI figures not confirmed
- LDR General Sales & Use Tax: https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax/ — **state rate 5%; returns/payments due 20th of month after month/quarter; dealer definition R.S. 47:301(4); base = sales price R.S. 47:301(13)** (read 2026-10-29)
- LDR FAQ sales rate table: https://revenue.louisiana.gov/tax-education-and-faqs/faqs/sales-tax-reform/what-is-the-state-sales-tax-rate/ — **4.45% through 2024-12-31 vs 5% from 2025-01-01; telecom 5%; direct marketers 9%** (read 2026-10-29)
- LDR Consumer Use Tax: https://revenue.louisiana.gov/individuals/general-resources/consumer-use-tax/ — **8.45% use tax in lieu of local** (read 2026-10-28)
- LDR Individual Income Tax: https://revenue.louisiana.gov/individuals/general-resources/individual-income-tax/ — **residency, IT-540, Schedule C credit, subtractions, R.S. 47:103 automatic 6-month extension, R.S. 47:118 12% underpayment penalty** (read 2026-10-28)
- LDR Declaration of Estimated Income Taxes: https://revenue.louisiana.gov/individuals/general-resources/declaration-of-estimated-income-taxes/ — **$1,000/$2,000 thresholds, Apr 15/Jun 15/Sep 15/Jan 15 vouchers, R.S. 47:116(F) March 1 exception** (read 2026-10-28)

## Open items for reviewer

- 2026 UI taxable wage base and experience-rate schedule (lwc.org blocked).
- Withholding table figures (JS-rendered page).
- Combined-report/unitary requirement and form (statute numbering never verified — legis.la.gov serves only a JS shell).
- Nonresident credit statute citation and IT-540B routing detail.
- Partnership tax (LI-005) interaction with TP/XB skills.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Louisiana questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
