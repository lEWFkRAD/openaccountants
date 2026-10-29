---
jurisdiction: US-HI
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
not_applicable: []
covered_by:
  IT-CORP: hi-corporate-income-tax
  SC: hi-social-contributions
  PR: hi-payroll-withholding
  TP: hi-transfer-pricing
  XB: hi-cross-border
---

# Hawaii (US-HI) pack

Jurisdiction: State of Hawaii, United States. Tax year 2026. Pack drafted 2026-10-27 (source-cited drafts, tier 2).

Hawaii taxes individuals through a graduated income tax (1.4%–11%, HRS ch. 235) and businesses through **two separate regimes**: a corporate **net-income tax** (4.4%/5.4%/6.4% graduated, HRS §235-71) and the **General Excise Tax** — a seller-side gross-receipts excise (published DOTAX rate 4.5% on Oahu, which includes a 0.5% county surcharge; 0.50% wholesale; 0.15% insurance commissions), not a purchaser sales tax (see `hi-sales-tax`). There is no franchise tax. The social layer is DLIR-administered: unemployment insurance (HRS ch. 383, employer-only experience-rated), temporary disability insurance (HRS ch. 392, employee contribution capped at 0.5% of weekly wages), and the Prepaid Health Care Act employer coverage mandate (HRS ch. 393, trigger at 86.67× minimum wage monthly). Income-tax withholding runs on the §235-61–68 family with $5,000/$40,000 annual deposit tiers and a 7.25% withholding on Hawaii real property sold by nonresidents. Estimated tax is due 4/20, 6/20, 9/20, 1/20 (§235-97). Statute text read from the HRS mirror at capitol.hawaii.gov 2026-10-27.

## applicable

- `IT-IND` — individual income tax — present: `hi-income-tax.md`
- `IT-CORP` — corporate income tax (graduated 4.4–6.4%) — drafted: `hi-corporate-income-tax.md`
- `VAT` — General Excise Tax (seller-side gross receipts) — present: `hi-sales-tax.md`
- `SC` — social contributions (UI ch. 383 / TDI ch. 392 / PREA ch. 393) — drafted: `hi-social-contributions.md`
- `PR` — payroll withholding (§§235-61–68) — drafted: `hi-payroll-withholding.md`
- `TP` — transfer pricing / apportionment (three-factor §235-29, royalty exclusion §235-7.3) — drafted: `hi-transfer-pricing.md`
- `XB` — cross-border / nonresident / part-year — drafted: `hi-cross-border.md`

## not_applicable

- none — Hawaii has income, corporate, excise, payroll, social-contribution, and apportionment regimes; all pilot domains apply.

## Source status

- HRS mirror (capitol.hawaii.gov): verified 2026-10-27/28 — §§235-4, 235-4.2, 235-7.3, 235-24, 235-29, 235-51, 235-61, 235-62, 235-68, 235-71, 235-71.5, 235-72, 235-97, 235-98, 235-104, 231-39, 387-2, 392-43, 393-11 read as text; ch. 383/392/393 section maps read from TOCs. All archived under sources/US-HI-*.
- tax.hawaii.gov: GET rates/nexus page, tax-rate schedules and tax-year-2025 information archived 2026-10-28. Still unresolved (listed in each skill's Not yet confirmed line): UI wage base/rates, HW-1/HW-3/HW-4 form IDs, N-15/N-30 instruction details, federal conformity date, personal exemptions and filing thresholds.
- labor.hawaii.gov: UI division page archived 2026-10-28 (claims-office information; UI rate schedules not extracted).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | hi-income-tax | existing (pre-pilot) |
| IT-CORP, corporate income tax | hi-corporate-income-tax | source-cited draft |
| VAT / GST / sales tax (GET) | hi-sales-tax | existing (pre-pilot) |
| SC, social contributions | hi-social-contributions | source-cited draft (UI figures unconfirmed — see skill's Not yet confirmed) |
| PR, payroll withholding | hi-payroll-withholding | source-cited draft (form IDs unconfirmed — see skill's Not yet confirmed) |
| TP, transfer pricing | hi-transfer-pricing | source-cited draft (addbacks unconfirmed — see skill's Not yet confirmed) |
| XB, cross-border | hi-cross-border | source-cited draft (residency definition unconfirmed — see skill's Not yet confirmed) |

## Official sources

- HRS ch. 235 (Income Tax Law): https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-.htm (read 2026-10-27)
- HRS §235-71 rates: https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0235/HRS_0235-0071.htm (read 2026-10-27)
- HRS §231-39 penalties/interest: https://www.capitol.hawaii.gov/hrscurrent/Vol04_Ch0201-0257/HRS0231/HRS_0231-0039.htm (read 2026-10-27)
- HRS ch. 383 (Unemployment Insurance): https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0383/HRS_0383-.htm (read 2026-10-27)
- HRS ch. 392 (TDI) §392-43: https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0392/HRS_0392-0043.htm (read 2026-10-27)
- HRS ch. 393 (PREA) §393-11: https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0393/HRS_0393-0011.htm (read 2026-10-27)
- Hawaii Department of Taxation: https://tax.hawaii.gov/ (GET page, tax-rate schedules, tax-year information archived 2026-10-28)
- DLIR: https://labor.hawaii.gov/ (UI division page archived 2026-10-28)
