---
pack: US-IN
jurisdiction: US-IN
applicable:
  - IT-IND
  - IT-CORP
  - VAT
  - SC
  - PR
  - TP
  - XB
not_applicable: {}
as_of: 2026-10-27
---

# Indiana (US-IN) — pack map

Indiana taxes individuals at a **flat state rate plus a county income tax** in all 92 counties (county rate locked to January 1 residence), corporations at a **flat rate on adjusted gross income** (IC 6-3 — 2.5% post-2022, confirm for 2026: needs-sources), and sales at 7% flat statewide with no local sales taxes. Employer social contributions are UI-only (IC 22-4, DWD). No state disability insurance, no state health-coverage mandate. Inheritance tax repealed. (not yet confirmed)

## Domain map

| Domain | Status | File | Notes |
|---|---|---|---|
| IT-IND individual income | drafted (pre-existing; jurisdiction code fixed 2026-10-27) | `in-income-tax.md` | flat rate + county tax, IT-40, self-employed focus |
| IT-CORP corporate income | drafted 2026-10-27 | `in-corporate-income-tax.md` | IT-20 + schedules verified from DOR inventory; rate + combined-report test needs-sources |
| VAT sales/use | drafted (pre-existing) | `in-sales-tax.md`, `indiana-sales-tax.md` | flat statewide rate (not yet confirmed), no local sales tax |
| SC social contributions | drafted 2026-10-27 | `in-social-contributions.md` | UI-only; DWD SPA so wage base/rates needs-sources |
| PR payroll withholding | drafted (pre-existing, deep) | `in-payroll.md` | WH-1/WH-3/WH-4, county rule, reciprocity, UI figures |
| TP transfer pricing | drafted 2026-10-27 | `in-transfer-pricing.md` | Schedule 8-D + IT-20PIC + PTET verified as forms; statutory scope needs-sources |
| XB cross-border | drafted 2026-10-27 | `in-cross-border.md` | IT-40PNR routing + PTET verified; reciprocity form IDs + 2026 rate needs-sources |

All seven domains apply to Indiana — no not_applicable entries.

## Key sources (read 2026-10-27)

- DOR corporate forms inventory: https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/ (IT-20, Schedules E, E-7, F, IT-20PIC, IT-20FSD, M, IT-2220, IT-20NOL, 8-D, RECAP, NOL-MOD, IT-20X)
- DOR withholding: https://www.in.gov/dor/i-am-a/business-corp/withholding/ (WH-1/WH-1U/WH-3/WH-4; late WH-1 up to 20% min $5; WH-3 $10 per document; Departmental Notice #1 county rates)
- DOR PTET: https://www.in.gov/dor/tax-forms/other-forms/ptet/ (SEA 2, 2023; IN-PTET; other-state PTET credit)
- DOR proper-form routing: https://www.in.gov/dor/i-am-a/business-corp/choosing-the-proper-income-tax-form/ (IT-20/IT-65/IT-20S/IT-40PNR/NP-20A)
- Indiana Code IC 6-3 / 6-8.1 / 22-4: https://iga.in.gov/ (SPA — no server-side text; statute cites are needs-sources)

## Open items for reviewer

- 2026 flat rates: individual (2.95% per in-income-tax vs 3.15% per in-payroll — reconcile; neither rate is yet confirmed against archived sources) and corporate (2.5%, not yet confirmed).
- Combined-report ownership test; IT-20PIC addback scope; Schedule E factor detail.
- UI wage base/rates 2026 (DWD SPA).
- Reciprocity exemption form IDs (OH/KY/MI/PA/WI).

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Indiana questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
