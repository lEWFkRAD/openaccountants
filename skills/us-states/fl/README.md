---
jurisdiction: US-FL
applicable: [IT-CORP, VAT, SC, TP, XB]
not_applicable:
  IT-IND: Florida imposes no individual income tax; individuals owe only federal tax plus sales and reemployment taxes
  PR: no state individual income tax means no state payroll withholding; employer reemployment contributions are covered under SC (fl-social-contributions)
---

# Florida -- OpenAccountants Tax Skills

| Field | Value |
|---|---|
| State | Florida |
| Code | US-FL |
| Income tax | No (individual); [5.5% corporate income tax under Ch. 220](https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx) |
| Sales tax | Yes (6% state + county discretionary surtax) |
| Franchise / gross receipts tax | No (for sole proprietors) |
| Tax authority | [Florida Department of Revenue (DOR)](https://floridarevenue.com) |
| Quality tier | Q3 -- AI-drafted, not independently verified |

Florida has no individual income tax and therefore no payroll withholding. The state taxes C-corporations at 5.5% on apportioned net income (s. 220.11, F.S.), levies a 6% sales/use tax with county surtaxes, and charges employers reemployment (unemployment) tax under Ch. 443 plus mandatory workers' compensation under Ch. 440.

## Files in this folder

| File | What it covers |
|---|---|
| `fl-corporate-income-tax.md` | Corporate income tax, Ch. 220 (Form F-1120) -- reviewed |
| `fl-sales-tax.md` | State and county sales & use tax compliance |
| `fl-sales-use-tax.md` | Sales & use tax registration and filing |
| `fl-sales-use-tax-surtax.md` | County discretionary surtax |
| `fl-transient-rental-tax.md` | Tourist development (transient rental) tax |
| `fl-annual-report.md` | Annual report filing for LLCs and corporations |
| `fl-moving-to-florida-domicile.md` | Domicile change to Florida |
| `fl-social-contributions.md` | Reemployment tax (Ch. 443) + workers' comp (Ch. 440) overlay |
| `fl-transfer-pricing.md` | Affiliated-group consolidation (s. 220.131), special apportionment (s. 220.153) |
| `fl-cross-border.md` | Nexus, PL 86-272, out-of-state tax addback, non-resident position |

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | none -- no individual income tax; corporate skill carries the token | n/a in substance |
| IT-CORP, corporate income tax | fl-corporate-income-tax | source-cited draft |
| VAT / sales tax | fl-sales-tax | source-cited draft |
| SC, social contributions | fl-social-contributions | source-cited draft |
| PR, payroll withholding | not applicable, see above | |
| TP, transfer pricing | fl-transfer-pricing | source-cited draft |
| XB, cross-border | fl-cross-border | source-cited draft |

## What's NOT covered
- Property tax (administered at county level)
- Documentary stamp tax
- Communications services tax
- Insurance premium tax
- Estate / inheritance tax (Florida has none)

## Official sources

- Florida Statutes Ch. 220 (corporate income tax): https://www.flsenate.gov/Laws/Statutes/2025/220.11 and sibling sections (200, statute text read 2026-10-27)
- FL DOR corporate tax page incl. rate table: https://floridarevenue.com/taxes/taxesfees/Pages/corporate.aspx (200, read 2026-10-27)
- Forms F-1120 / F-1120ES / F-1120N / F-2220: https://floridarevenue.com/Forms_library/current/f1120.pdf et al. (200 PDF, 2026-10-27)
- Florida Statutes Ch. 440 (workers' comp): https://www.flsenate.gov/Laws/Statutes/2025/440.04 (200, read 2026-10-27)
- Florida Statutes Ch. 443 (reemployment tax): administered by DOR; coverage tests, $7,000 wage base, 2.7% initial rate and RT-6 due dates read from https://floridarevenue.com/taxes/taxesfees/Pages/reemployment.aspx (200, read 2026-10-28); the 2026 statutory rate-schedule sections were not located this run (see Not yet confirmed in fl-social-contributions)

## How to use
Upload all `.md` files in this folder PLUS the federal skills from `skills/foundation/` and `skills/federal/` to your LLM. See the main README for details.
