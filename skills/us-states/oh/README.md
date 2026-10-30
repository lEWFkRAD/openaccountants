---
jurisdiction: US-OH
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
---

# Ohio -- OpenAccountants Tax Skills

| Field | Value |
|---|---|
| State | Ohio |
| Code | US-OH |
| Income tax | Yes (graduated; top rate phasing down under HB 96) |
| Sales tax | Yes (5.75% state rate + local) | (not yet confirmed)
| Franchise / gross receipts tax | Yes -- Commercial Activity Tax (CAT), ORC Ch. 5751 |
| Corporate income tax | No -- Ohio repealed its corporate income/franchise tax in 2013; the CAT is the entity-level business tax |
| Tax authority | [Ohio Department of Taxation](https://tax.ohio.gov) |
| Quality tier | Q3 -- AI-drafted, not independently verified |

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | oh-income-tax | source-cited draft |
| IT-CORP, corporate income tax | oh-corporate-income-tax (CAT as corporate-tax substitute) | source-cited draft |
| VAT / GST / sales tax | oh-sales-tax, ohio-sales-tax | source-cited draft |
| SC, social contributions | oh-social-contributions (UI, BWC workers' comp) | source-cited draft |
| PR, payroll withholding | oh-payroll | source-cited draft |
| TP, transfer pricing | oh-transfer-pricing (CAT consolidated/affiliated-group rules) | source-cited draft |
| XB, cross-border | oh-cross-border (nonresident allocation, municipal 20-day rule, CAT nexus) | source-cited draft |

Ohio has **no corporate income tax**: the entity-level tax on business activity is the Commercial Activity Tax (CAT), a gross-receipts tax under ORC Chapter 5751, so the IT-CORP domain is covered by `oh-corporate-income-tax` (which routes to the CAT skills). Ohio also layers 600+ municipal net profit taxes and 200+ school district income taxes on top of the state income tax -- see `oh-payroll` and `oh-cross-border`.

## Files in this folder

| File | What it covers |
|---|---|
| `oh-income-tax.md` | Individual income tax for self-employed / sole proprietors (Form IT 1040) |
| `oh-sales-tax.md` / `ohio-sales-tax.md` | State and local sales & use tax compliance |
| `oh-cat.md` / `oh-cat-tax.md` | Commercial Activity Tax (CAT) -- gross receipts tax on business activity |
| `oh-corporate-income-tax.md` | Corporate income tax domain: no CIT -- CAT substitute, PTE election, financial institutions tax |
| `oh-social-contributions.md` | Social contributions: unemployment insurance (ORC 4141), BWC state-fund workers' compensation (ORC 4123) |
| `oh-payroll.md` | Employer withholding, municipal income tax collection (RITA/CCA), BWC |
| `oh-transfer-pricing.md` | Transfer pricing / CAT affiliated-group and consolidated-election overlay |
| `oh-cross-border.md` | Cross-border: nonresident Ohio-source allocation (ORC 5747.20), credit for other-state tax, municipal 20-day threshold, CAT nexus |

## What's NOT covered
- Property tax (administered at county level)
- Estate / inheritance tax (Ohio repealed its estate tax effective 2013)
- Financial institutions tax detail (Ch. 4591) -- flagged in `oh-corporate-income-tax`

## Official sources
- [ORC 5751.02 CAT levy](https://codes.ohio.gov/ohio-revised-code/section-5751.02) -- read 2026-10-27 (text effective 2026-06-15, SB 450)
- [ORC 5751.01 CAT definitions / nexus](https://codes.ohio.gov/ohio-revised-code/section-5751.01) -- read 2026-10-27
- [ORC 5747.05 / 5747.20 individual tax, nonresident allocation](https://codes.ohio.gov/ohio-revised-code/section-5747.20) -- read 2026-10-27
- [ORC 4123.26 BWC payroll report](https://codes.ohio.gov/ohio-revised-code/section-4123.26) -- read 2026-10-27
- [Department of Taxation CAT page](https://tax.ohio.gov/portal/divisions/enterprise_services/commercial_activity_tax_cat) -- HTTP 200 2026-10-27 (JS-rendered; figures carried from `oh-cat` verified 2026-10-16)

## How to use
Upload all `.md` files in this folder PLUS the federal skills from `skills/foundation/` and `skills/federal/` to your LLM. See the main README for details.
