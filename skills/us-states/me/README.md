---
pack: US-ME
jurisdiction: US-ME
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

# Maine (US-ME) — pack map

Maine taxes individuals on a graduated schedule (top marginal 7.95% plus a 2% surcharge on high income — 36 M.R.S. § 5111, statute page verified 2026-10-28), corporations on a **graduated scale from 3.5% (income up to $350,000) to 8.93% (income in excess of $3,500,000)** (Maine Revenue Services 1120ME page, verified 2026-10-28), and sales at 5.5% general state rate (prepared food 8%, lodging 9% from 2026 — MRS rates page, archived 2026-10-29; see `me-sales-tax.md`). Employer withholding runs on **Form 941ME (quarterly)** with the **ME UC-1** unemployment contributions report processed by MRS for the Department of Labor (verified). Pass-through entities with nonresident members must withhold via **Form 941P-ME** or file a composite return (verified).

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing) | `me-income-tax.md` | 1040ME, graduated rates, 2026 rate schedules |
| IT-CORP corporate income | drafted 2026-10-28 | `me-corporate-income-tax.md` | 1120ME brackets 3.5%/7.93%/8.33%/8.93% verified from 1120ME instructions; deadlines verified |
| VAT sales/use | drafted (pre-existing) | `me-sales-tax.md` | 5.5% general state rate; 8% prepared food, 9% lodging, 10% short-term auto rental (MRS rates page archived) |
| SC social contributions | drafted 2026-10-28 | `me-social-contributions.md` | ME UC-1 UI report verified; wage base/rates not yet confirmed (DOL page not reachable this run) |
| PR payroll withholding | drafted 2026-10-28 | `me-payroll.md` | 941ME quarterly + 941P-ME PTE verified; W-3ME discontinued after 2023 verified; table method detail not line-cited |
| TP transfer pricing | drafted 2026-10-28 | `me-transfer-pricing.md` | unitary/combined Rule 810 + apportionment Rule 801 verified to exist; mechanics verified from rule PDFs |
| XB cross-border | drafted 2026-10-28 | `me-cross-border.md` | 941P-ME/composite verified; Schedule NR routing + credit mechanics not yet confirmed |

All seven domains apply to Maine — no not_applicable entries. Maine's "franchise tax" (1120B-ME) applies only to financial institutions and is noted inside the corporate skill, not as a separate domain.

## Key sources (read 2026-10-28)

- MRS Corporate Income Tax (1120ME): https://www.maine.gov/revenue/taxes/income-estate-tax/corporate-income-tax-1120me — **graduated 3.5% (up to $350,000) to 8.93% (over $3,500,000); S corps generally out unless federal taxable income at corporate level; financial institutions → franchise tax, insurers → premiums tax; Rules 801 (apportionment), 808 (nexus), 810 (unitary business, combined reports)** (page fetched, text verified)
- MRS Employer Withholding: https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding — **Form 941ME quarterly return; ME UC-1 unemployment contributions report (DOL administers once filed); W-3ME annual reconciliation discontinued for tax years after 2023; Rule 803** (verified)
- MRS Pass-through Entity Withholding: https://www.maine.gov/revenue/taxes/income-estate-tax/pass-through-entity-withholding-941p-me-returns — **Form 941P required for partnerships/S corps with Maine-source income and any nonresident members; withholding or exemption certificate or composite election; composite return combines nonresidents' Maine-source income** (verified)
- 36 M.R.S. § 5111 (rate statute): https://legislature.maine.gov/statutes/36/title36sec5111.html — **graduated individual schedules; 2% income tax surcharge above filing-status thresholds** (statute page fetched 2026-10-28)
- MRS 1040ME page: https://www.maine.gov/revenue/taxes/income-estate-tax/individual-income-tax-1040me — resolves (200); nonresident Schedule NR detail not yet confirmed
- Maine DOL (UI): https://www.maine.gov/labor/cwri/ resolves but is the labor-statistics portal; the UI employer rate/wage-base page was not reachable this run — **UI figures not yet confirmed**

## Open items for reviewer

- Corporate middle brackets (7.93%/8.33% verified from 1120ME instructions) and the 1120ME due date / estimated-payment thresholds (verified).
- 2026 UI taxable wage base and experience-rate schedule (DOL page unreachable).
- Withholding table figures (Rule 803 methods and quarterly dates verified; table figures not line-cited).
- Combined-report scope under Rule 810 (unitary test verified via 1120ME instructions) and single sales factor under Rule 801 (verified).
- Nonresident Schedule NR mechanics and the credit-for-tax-paid-to-other-states statute cite.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Maine questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
