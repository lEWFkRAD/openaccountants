---
jurisdiction: US-DC
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  IT-IND: dc-income-tax
  IT-CORP: dc-franchise-tax
  SC: dc-unemployment-contributions
  PR: dc-payroll-withholding
  TP: dc-transfer-pricing
  XB: dc-cross-border
---

# District of Columbia (US-DC) pack

Jurisdiction: District of Columbia, United States. Tax year 2026. Pack drafted 2026-10-27, conformed and tied out 2026-10-28 (source-cited drafts, tier 2).

The District taxes business activity through the **franchise tax** — 8.25% on DC-computed net income for both corporate and unincorporated businesses, on a **mandatory combined-reporting basis** for unitary groups (D.C. Code §§ 47-1807.02 and 47-1808.03: "For taxable years beginning after December 31, 2017, a tax at the rate of 8.25% upon the taxable income of every corporation"; OTR Business Franchise Tax Rates and Combined Reporting pages, read 2026-10-28). Minimum taxes: $250 (DC gross receipts ≤ $1M) / $1,000 (> $1M) (same statutes and OTR rates page). Apportionment is by the **single sales factor** (D.C. Code § 47-1810.02(d-2)). Estimated tax is required when liability exceeds $1,000, paid quarterly (15 April, 15 June, 15 September, 15 December) with a 110%-of-prior-year safe harbor (OTR Estimated Tax page, read 2026-10-28: "Estimated tax payments are due: Calendar Year Filers: April 15; and June 15; and September 15; and December 15"). Withholding runs on FR-900Q (quarterly, e-file mandatory since TY2023 — OTR Withholding Tax Forms page: "Beginning TY2023, FR-900Q must be filed electronically on MyTax.DC.gov"), FR-900A (annual, due 31 January), FR-900NP (1099/W-2G), with the D-4 employee certificate (OTR page, read 2026-10-28). Unemployment insurance is employer-only on the first $9,000 of wages, with a 2.7%-floor new-employer rate and a 0.2% administrative assessment (DOES UI Handbook for Employers, read 2026-10-28), and Universal Paid Leave adds a 0.62% employer-paid contribution with no wage cap (D.C. Code § 32-541.03(Perm)). DC has **no temporary disability insurance program**; OTR's "Notice of Delinquency (TDI)" is a delinquent-return notice program (OTR page, read 2026-10-28). Non-resident individuals pay no DC income tax (D.C. Code § 1-206.02); withheld tax is recovered on Form D-40B. Individuals pay a graduated income tax at 4%–10.75% (see `dc-income-tax`).

## applicable

- `IT-IND` — individual income tax — present: `dc-income-tax.md`
- `IT-CORP` — corporate franchise tax (8.25%, combined reporting) — drafted: `dc-franchise-tax.md`
- `VAT` — sales & use tax — present: `dc-sales-tax.md`
- `SC` — social contributions (UI via DOES; Paid Family Leave) — drafted: `dc-unemployment-contributions.md`
- `PR` — payroll withholding (FR-900 family) — drafted: `dc-payroll-withholding.md`
- `TP` — transfer pricing / combined reporting — drafted: `dc-transfer-pricing.md`
- `XB` — cross-border / non-resident entities — drafted: `dc-cross-border.md`

## not_applicable

- none — the District has income, franchise, sales, payroll, and social-contribution regimes;
  all pilot domains apply.

## Source status

- OTR Business Franchise Tax Rates page: archived 2026-10-28 (`US-DC-otr-franchise-rates.html`) — 8.25% rate table (2018–2025), $250/$1,000 minimums, $12,000 unincorporated trigger, 30% salary allowance + $5,000 exemption, personal-services exemption.
- OTR Combined Reporting page: archived 2026-10-28 (`US-DC-otr-combined-reporting.html`) — mandatory combination for unitary businesses for taxable years beginning on or after 2011-01-01.
- OTR Estimated Tax Requirement page: archived 2026-10-28 (`US-DC-otr-estimated-tax.html`) — more-than-$1,000 trigger, quarterly dates, 110% safe harbor, D-20ES/D-30ES/D-2210/D-2220.
- OTR Withholding Tax Forms page: archived 2026-10-28 (`US-DC-otr-withholding-forms.html`) — FR-900Q quarterly e-file mandate since TY2023, FR-900A annual 31 January, FR-900NP, FR-900P, WT transmittals, D-4, household-employer FR-900Q rule since 2019.
- DOES UI Handbook for Employers, Employer Tax Information and Tax Rate Questions pages: archived 2026-10-28 — $9,000 wage base, 2.7% new-employer floor, six experience-rate tables, 0.2% administrative assessment, UC-30 quarterly due dates.
- DOES Paid Family Leave Employer Toolkit and D.C. Code § 32-541.03(Perm): archived 2026-10-28 — 0.62% employer-paid contribution, no wage cap, quarterly filings.
- DC Code sections archived 2026-10-28: §§ 1-206.02, 47-1801.04, 47-1803.03, 47-1806.03, 47-1806.04, 47-1806.06, 47-1806.15, 47-1807.02, 47-1808.01, 47-1808.03, 47-1810.02, 47-4201, 47-4213, 32-541.03(Perm), plus D.C. Law 26-89, the 2025 D-40 booklet, the 2026 D-40ES booklet, Forms D-2210/FR-127/D-40B, the AG opinion of 24 February 2026, the CFO February 2026 revenue estimate, and the FY 2027 BSA fiscal impact statement.
- Not yet confirmed (see each skill's Not yet confirmed line): the 2026 standard deduction for the D-40, the 2026 EITC percentage, a 2026 child tax credit, DC withholding rate tables and deposit tiering, the 2026 UI experience-rate table, water's-edge mechanics, and P.L. 86-272 administration.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | dc-income-tax | conformed to exemplar, figures tied out |
| IT-CORP, corporate income tax | dc-franchise-tax | conformed to exemplar, figures tied out |
| VAT / GST / sales tax | dc-sales-tax | existing (pre-pilot) |
| SC, social contributions | dc-unemployment-contributions | conformed to exemplar, figures tied out |
| PR, payroll withholding | dc-payroll-withholding | conformed to exemplar, figures tied out |
| TP, transfer pricing | dc-transfer-pricing | conformed to exemplar, figures tied out |
| XB, cross-border | dc-cross-border | conformed to exemplar, figures tied out |

## Official sources

All cited URLs are archived under `~/oa-correction-evidence/sources/` with sidecar JSON (`US-DC-*`). Key sources:

- OTR Business Franchise Tax Rates: https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates (read 2026-10-28)
- OTR Combined Reporting: https://otr.cfo.dc.gov/page/combined-reporting-business-entities (read 2026-10-28)
- OTR Estimated Tax Requirement: https://otr.cfo.dc.gov/page/underpayment-estimated-tax-interest (read 2026-10-28)
- OTR Withholding Tax Forms: https://otr.cfo.dc.gov/page/withholding-tax-forms (read 2026-10-28)
- DOES UI Handbook for Employers: https://does.dc.gov/sites/default/files/dc/sites/does/publication/attachments/UI%20Employer%20Handbook%20-MASTER2-FINAL.pdf (read 2026-10-28)
- DOES Paid Family Leave Employer Toolkit: https://does.dc.gov/sites/default/files/dc/sites/does/page_content/attachments/DOES_PFL_EmployerToolkit.pdf (read 2026-10-28)
- DC Code (code.dccouncil.gov): §§ 1-206.02, 47-1801.04, 47-1803.03, 47-1806.03/.04/.06/.15, 47-1807.02, 47-1808.01/.03, 47-1810.02, 47-4201, 47-4213, 32-541.03(Perm) (read 2026-10-28)
- D.C. Law 26-89: https://code.dccouncil.gov/us/dc/council/laws/26-89 (read 2026-10-28)
