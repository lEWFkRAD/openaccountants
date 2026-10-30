---
jurisdiction: US-PA
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
---

# Pennsylvania — OpenAccountants Tax Skills

| Field | Value |
|---|---|
| State | Pennsylvania |
| Code | US-PA |
| Income tax | Yes (flat 3.07%) | (not yet confirmed)
| Sales tax | Yes (6% state + up to 2% local) |
| Corporate income tax | Yes — Corporate Net Income Tax (CNIT), 9.99% phasing down under Act 53 (2022) | (not yet confirmed)
| Franchise / gross receipts tax | Capital stock/franchise tax repealed effective 2017; margins tax expired 2016 |
| Tax authority | [Pennsylvania Department of Revenue](https://www.pa.gov/agencies/revenue/) |
| Quality tier | Q3 — AI-drafted, not independently verified |

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | pa-income-tax | source-cited draft |
| IT-CORP, corporate income tax | pa-corporate-income-tax (CNIT, RCT-1) | source-cited draft — rate schedule needs-sources |
| VAT / GST / sales tax | pa-sales-tax, pennsylvania-sales-tax | source-cited draft |
| SC, social contributions | pa-social-contributions (UC, workers' comp, PFML) | source-cited draft — PFML needs-sources |
| PR, payroll withholding | pa-payroll | source-cited draft |
| TP, transfer pricing | pa-transfer-pricing (combined/unitary reporting, 7337 addbacks) | source-cited draft — statute text needs-sources |
| XB, cross-border | pa-cross-border (reciprocity, Schedule G-L, nonresident PA-40) | source-cited draft |

Pennsylvania's entity-level tax is the **Corporate Net Income Tax** (CNIT, Act of Mar. 4, 1971 — an uncodified session law, which is why statute searches on legis.state.pa.us USC pages do not find it). The capital stock/franchise tax was repealed effective 2017. PA layers **local earned income taxes (Act 32 PSDs)** and the **Local Services Tax** on top of the state income tax — see `pa-payroll` and `pa-cross-border`. (not yet confirmed)

## Files in this folder

| File | What it covers |
|---|---|
| `pa-income-tax.md` | Individual income tax for self-employed / sole proprietors (Form PA-40) |
| `pa-sales-tax.md` / `pennsylvania-sales-tax.md` | State and local sales & use tax compliance |
| `pa-payroll.md` | Employer withholding, local EIT (Act 32), LST, UC withholding, reciprocal states |
| `pa-local-eit.md` | Local earned income tax jurisdictions |
| `pa-corporate-income-tax.md` | CNIT: rate phase-down, combined vs non-combined RCT-1, nexus, P.L. 86-272 |
| `pa-social-contributions.md` | UC (DLI yearly highlights, 2026/2027 solvency measures), workers' comp, PFML |
| `pa-transfer-pricing.md` | Combined/unitary reporting, intercompany transaction addbacks (72 P.S. § 7337), apportionment |
| `pa-cross-border.md` | Reciprocity (NJ/OH/IN/MD/VA/WV), Schedule G-L resident credit, nonresident/part-year PA-40 |

## What's NOT covered
- Property tax (administered at county/local level)
- Inheritance tax (PA has an inheritance tax, not an estate tax)
- Philadelphia wage tax / net profits tax detail (flagged in `pa-payroll`)
- Pass-through entity (PTE) election status for 2026 — needs-sources

## Official sources
- [DLI UC yearly tax highlights](https://www.pa.gov/agencies/dli/resources/for-employers-and-educators/how-to-file/uc-tax/yearly-tax-highlights) — read 2026-10-27 (2027 wage base $10,000; 9.2% surcharge; 0.60% additional contributions; min .014190 / max .103734; employee 0.07%)
- [2025 PA-40 instructions](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/formsandpublications/formsforindividuals/pit/documents/2025/2025_pa-40in.pdf) — read 2026-10-27 (reciprocity carve-outs, Schedule G-L, nonresident/part-year rules)
- [Revenue CNIT page](https://www.revenue.pa.gov/Businesses/Taxes/CorporateNetIncomeTax.aspx) — HTTP 200 2026-10-27 but JS-rendered shell; RCT-1 instructions PDF 404 on every probed path — **CNIT rate schedule needs-sources**
- `pa-income-tax`, `pa-payroll` (tier 2, read 2026-07-13 / 2026-09-25) — 3.07% PIT, UC $10,000 base, reciprocity list, Act 32 EIT

## How to use
Upload all `.md` files in this folder PLUS the federal skills from `skills/foundation/` and `skills/federal/` to your LLM. See the main README for details.
