---
jurisdiction: US
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
---

# United States (federal): tax pack

The United States federal system taxes individuals and corporations
through the Internal Revenue Code, administered by the IRS, on a
calendar-year basis in USD. There is no federal VAT or GST —
consumption tax is a state-and-local sales-tax matter, covered in this
pack by the sales-tax and nexus-matrix skills. Payroll social
contributions (FICA: Social Security and Medicare, plus FUTA
unemployment tax) are the federal SC domain; self-employed persons pay
the equivalent SE tax. Transfer pricing runs through IRC §482 and the
§482 regulations (specified methods plus the best-method rule), with
the §6662(e)/(h) valuation-misstatement penalties and country-by-
country reporting under §6038. The 2026 layer reflects the OBBBA
changes recorded in `packages/us-federal/rates.2026.json` (BEAT 12.5%,
§250 GILTI deduction 37.5%, FDII deduction 21.875%).

**Source status:** IRS and eCFR pages verified 2026-10-24. The SSA
pages that publish the 2026 Social Security wage base returned 403 to
this drafting environment, so the 2026 wage-base figure is
**needs-sources** throughout (the IRS SE-tax page still quotes the
$168,600 pre-2026 base).

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | us-form-1040-individual-income-tax-return | source-cited draft |
| IT-CORP, corporate income tax | us-form-1120-c-corp | source-cited draft |
| VAT / GST (state sales tax) | us-sales-tax | source-cited draft |
| SC, social contributions | us-social-contributions | source-cited draft |
| PR, payroll withholding | us-form-941-940-payroll | source-cited draft |
| TP, transfer pricing | us-transfer-pricing | source-cited draft |
| XB, cross-border | us-citizen-moving-abroad-tax | source-cited draft |

## Official sources

- [IRS — Self-employment tax (Social Security and Medicare taxes)](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) — read 2026-10-24.
- [IRS — Employment taxes](https://www.irs.gov/businesses/small-businesses-self-employed/employment-taxes) — read 2026-10-24.
- [IRS — About Form 941](https://www.irs.gov/forms-pubs/about-form-941) / [About Form 940](https://www.irs.gov/forms-pubs/about-form-940) — read 2026-10-24.
- [IRS — Transfer pricing](https://www.irs.gov/businesses/international-businesses/transfer-pricing) — read 2026-10-24.
- [eCFR 26 CFR 1.482-1](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-1), [1.482-3](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-3), [1.482-4](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-4), [1.482-5](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-D/part-1/section-1.482-5) — read 2026-10-24.
- [eCFR 26 CFR 1.6662-6 (transfer pricing penalties)](https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1/section-1.6662-6) — read 2026-10-24.
- [IRS — About Form 8975 (Country by Country Report)](https://www.irs.gov/forms-pubs/about-form-8975), [About Form 5472](https://www.irs.gov/forms-pubs/about-form-5472), [About Form 8991 (BEAT)](https://www.irs.gov/forms-pubs/about-form-8991) — read 2026-10-24.
- SSA COLA/wage-base pages (ssa.gov) — 403 to this environment 2026-10-24; **2026 wage base needs-sources**.
- `packages/us-federal/rates.2026.json` — hand-authored, CPA-reviewed rates file in this repo.
