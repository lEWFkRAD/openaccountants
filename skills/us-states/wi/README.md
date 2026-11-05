---
jurisdiction: US-WI
applicable: [IT-IND, IT-CORP, VAT, SC, PR, TP, XB]
---

# Wisconsin -- OpenAccountants Tax Skills

| Field | Value |
|---|---|
| State | Wisconsin |
| Code | US-WI |
| Income tax | Yes (graduated 3.5%–7.65%) (US-WI-dr-wis-stat-ch71.txt: "On all taxable income from $0 to $14,680, 3.50 percent ... On all taxable income exceeding $323,290, 7.65 percent") |
| Sales tax | Yes (5% state + 0.5% county) |
| Corporate tax | Yes -- franchise tax 7.9% (income tax 7.9% for certain foreign corps), Form 4; economic development surcharge 3% |
| Franchise / gross receipts tax | Franchise tax measured by income (Form 4); no gross-receipts tax |
| Tax authority | [Wisconsin Department of Revenue](https://www.revenue.wi.gov) |
| Quality tier | Q3 -- AI-drafted, not independently verified |

## Domains

| Domain | Skill | Status |
|---|---|---|
| IT-IND, individual income tax | wi-income-tax | source-cited draft |
| IT-CORP, corporate income tax | wi-corporate-income-tax (Form 4 franchise/income, ED surcharge) | source-cited draft |
| VAT / GST / sales tax | wi-sales-tax, wisconsin-sales-tax | source-cited draft |
| SC, social contributions | wi-social-contributions (UI ch. 108, workers' comp) | source-cited draft |
| PR, payroll withholding | wi-payroll | source-cited draft |
| TP, transfer pricing | wi-transfer-pricing (combined Form 6, unitary tests, water's edge) | source-cited draft |
| XB, cross-border | wi-cross-border (1NPR, IL/IN/KY/MI reciprocity, MN reciprocity per statute) | source-cited draft |

Wisconsin's entity-level tax is a **franchise tax measured by income** (Wis. Stat. ch. 71 subch. III, Form 4) at a flat **7.9%**, plus a **3% economic development surcharge** (min $25 / max $9,800). Combined (unitary) groups file **Form 6** through a designated agent -- see `wi-transfer-pricing`. Wisconsin has **no local earned income tax** and **no estate tax**.

## Files in this folder

| File | What it covers |
|---|---|
| `wi-income-tax.md` | Individual income tax for self-employed / sole proprietors (Form 1) |
| `wi-sales-tax.md` / `wisconsin-sales-tax.md` | State and county sales & use tax compliance |
| `wi-payroll.md` | Employer withholding (WT-6/WT-7), UI (ch. 108), workers' comp, Milwaukee sick leave |
| `wi-corporate-income-tax.md` | Form 4 franchise/income tax, ED surcharge, nexus/doing-business, P.L. 86-272, single sales factor |
| `wi-social-contributions.md` | UI coverage/wage base/rates (ch. 108), UI penalties, workers' comp |
| `wi-transfer-pricing.md` | Combined reporting: three tests, designated agent Form 6, water's edge, excluded entities |
| `wi-cross-border.md` | 1NPR nonresident/part-year, IL/IN/KY/MI reciprocity, MN reciprocity per statute, credit for tax paid to another state |

## What's NOT covered
- Property tax (administered at county/municipal level)
- Estate/inheritance tax (Wisconsin has none)
- Insurance premiums tax, utilities taxes (flagged in `wi-corporate-income-tax`)
- Farmland preservation credit detail

## Official sources
- [2025 Form 4 instructions (IC-100)](https://www.revenue.wi.gov/TaxForms2025/2025-Form4-inst.pdf) -- PDF read 2026-10-27 (7.9% rate, ED surcharge 3%/$25/$9,800, combined tests, P.L. 86-272, 18% interest, single sales factor)
- [2025 Form 1NPR instructions](https://www.revenue.wi.gov/TaxForms2025/2025-Form1NPR-inst.pdf) -- PDF read 2026-10-27 (WI-source rules, IL/IN/KY/MI exceptions, credit for tax paid to another state)
- [Wis. Stat. ch. 71 §§ 71.21/71.26](https://docs.legis.wisconsin.gov/statutes/statutes/71/21) -- read 2026-10-27 (US-WI-dr-wis-stat-ch71.txt: ch. 71 table of contents lists "71.21 Computation." and "71.26 Income computation.")
- `wi-payroll` (tier 2, read 2026-07-13) -- UI UCT-101 calendar, penalties, MN reciprocity per statute (see Not yet confirmed in Sources)

## Sources

Not yet confirmed: the `wi-payroll` tier-2 figures carried into this README -- UI taxable wage base $14,000 and the UCT-101 quarterly calendar -- lack an archived source (the archived US-WI-108.html is only the ch. 108 table of contents).

## How to use
Upload all `.md` files in this folder PLUS the federal skills from `skills/foundation/` and `skills/federal/` to your LLM. See the main README for details.
