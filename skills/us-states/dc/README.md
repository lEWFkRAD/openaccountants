---
jurisdiction: US-DC
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
covered_by:
  IT-CORP: dc-franchise-tax
  SC: dc-unemployment-contributions
  PR: dc-payroll-withholding
---

# District of Columbia (US-DC) pack

Jurisdiction: District of Columbia, United States. Tax year 2026. Pack drafted 2026-10-27 (source-cited drafts, tier 2).

The District taxes business activity through the **franchise tax** — 8.25% on DC-computed net income for both corporate and unincorporated businesses, on a **mandatory combined-reporting basis** for unitary groups (DC Code Title 47 ch. 18; rates and the combined-reporting rule read from the OTR Business Franchise Tax Rates and Combined Reporting pages, 2026-10-27). Minimum taxes: $250 (DC gross receipts ≤ $1M) / $1,000 (> $1M). Estimated tax is required when liability exceeds $1,000, paid quarterly (4/15, 6/15, 9/15, 12/15) with a 110%-of-prior-year safe harbor (OTR Estimated Tax page, read 2026-10-27). Withholding runs on FR-900Q (quarterly, e-file mandatory since TY2023), FR-900A (annual), FR-900NP (1099/W-2G), with the D-4 employee certificate (OTR Withholding page, read 2026-10-27). Unemployment is administered by the Department of Employment Services (does.dc.gov — page resolves but is JS-rendered; UI figures **needs-sources**). Individuals pay a graduated income tax (see `dc-income-tax`).

## applicable

- `IT-IND` — individual income tax — present: `dc-income-tax.md`
- `IT-CORP` — corporate franchise tax (8.25%, combined reporting) — drafted: `dc-franchise-tax.md`
- `VAT` — sales & use tax — present: `dc-sales-tax.md`
- `SC` — social contributions (UI via DOES) — drafted: `dc-unemployment-contributions.md`
- `PR` — payroll withholding (FR-900 family) — drafted: `dc-payroll-withholding.md`
- `TP` — transfer pricing / combined reporting — drafted: `dc-transfer-pricing.md`
- `XB` — cross-border / non-resident entities — drafted: `dc-cross-border.md`

## not_applicable

- none — the District has income, franchise, sales, payroll, and social-contribution regimes;
  all pilot domains apply.

## Source status

- OTR Business Franchise Tax Rates page: verified 2026-10-27 (otr.cfo.dc.gov, 200, text read — 8.25% rate table 2018–2025 for corporate and unincorporated; $250/$1,000 minimums; 30% salary allowance + $5,000 exemption for unincorporated; personal-services exemption; DC Code Title 47 ch. 18 citation).
- OTR Combined Reporting page: verified 2026-10-27 (200, text read — mandatory combination for unitary businesses for TYB ≥ 2011-01-01).
- OTR Estimated Tax Requirement page: verified 2026-10-27 (200, text read — >$1,000 trigger, 4/15·6/15·9/15·12/15, fiscal-year pattern, 110% safe harbor, D-20ES/D-30ES/D-2210/D-2220 forms).
- OTR Withholding Tax Forms page: verified 2026-10-27 (200, text read — FR-900Q quarterly e-file mandate, deposit/filing dates, FR-900A annual Jan 31, FR-900NP, FR-900P, WT transmittal, D-4 under review, household-employee FR-900Q rule since 2019).
- DOES unemployment page (does.dc.gov/page/unemployment-compensation): resolves 200 but JS-rendered — UI wage base/rates **needs-sources**.
- DC Code mirror (code.dccouncil.gov Title 47 ch. 18): resolves 200 — section-level text not extracted this run; deep statutory cites **needs-sources**.

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | dc-income-tax | existing (pre-pilot) |
| IT-CORP, corporate income tax | dc-franchise-tax | source-cited draft |
| VAT / GST / sales tax | dc-sales-tax | existing (pre-pilot) |
| SC, social contributions | dc-unemployment-contributions | source-cited draft (figures needs-sources) |
| PR, payroll withholding | dc-payroll-withholding | source-cited draft |
| TP, transfer pricing | dc-transfer-pricing | source-cited draft |
| XB, cross-border | dc-cross-border | source-cited draft |

## Official sources

- OTR Business Franchise Tax Rates: https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates (read 2026-10-27)
- OTR Combined Reporting: https://otr.cfo.dc.gov/page/combined-reporting-business-entities (read 2026-10-27)
- OTR Estimated Tax Requirement: https://otr.cfo.dc.gov/page/underpayment-estimated-tax-interest (read 2026-10-27)
- OTR Withholding Tax Forms: https://otr.cfo.dc.gov/page/withholding-tax-forms (read 2026-10-27)
- DOES Unemployment Compensation: https://does.dc.gov/page/unemployment-compensation (read 2026-10-27, JS-rendered)
- DC Code Title 47 ch. 18: https://code.dccouncil.gov/us/dc/council/code/titles/47/chapters/18/ (200, section text not extracted)
