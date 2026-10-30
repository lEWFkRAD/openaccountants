---
name: nyc-unincorporated-business-tax
description: Use this skill whenever asked about the New York City Unincorporated Business Tax (UBT). Trigger on phrases like "NYC UBT", "unincorporated business tax", "NYC-202", "NYC-202S", "IT-219 credit", "NYC Admin Code Title 11 Chapter 5". Covers the 4% rate, the credit and exemption bands, who is subject, and the NYC personal-income-tax credit that limits double taxation.
jurisdiction: US-NY-NYC
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NYC Unincorporated Business Tax

> **Source-cited draft.** Built from the NYC Comptroller's report "Recent Trends in the City's Business Income Taxes" (February 18, 2025) and the NYC Department of Finance business-tax page, both read on 2026-10-28. No accountant has reviewed it. Do not file from it without review by a qualified New York City professional.

Tax year: the calendar year. Authority: New York City Department of Finance (DOF). Governing law: the New York City Administrative Code, Title 11, Chapter 5 (Unincorporated Business Tax).

See also: `ny-cross-border`, `ny-income-tax`.

## Who this applies to

- **Every individual or unincorporated entity carrying on a trade, business, or profession wholly or partly in NYC** is subject to UBT: "UBT is imposed on every individual or unincorporated entity carrying on a trade, business, or profession wholly or partly in NYC."
- **Sole proprietors (IRS Schedule C businesses) and unincorporated entities (partnerships and LLCs)** pay UBT; the Business Corporation Tax (BCT) applies to C-corporations and the General Corporation Tax (GCT) to S-corporations.
- **Private equity and hedge funds** organized as LLPs or LLCs "are subject to UBT for their management fees but not for carried interest (the performance fee based on realized profits)."
- **Self-trading is largely outside the base:** "Income derived from trading on one's own account ('self-trading') is, with some exceptions, exempt from UBT."
- **Employees are not carrying on an unincorporated business** for their employment income; the employee point is not yet confirmed against an archived primary source (see Not yet confirmed).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| UBT income tax rate | **4%** | 2025 | [Comptroller, Table 1 "Summary of main features"](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |
| Full credit against the tax | allowed "if the tax is up to $3,400" | 2025 | [Comptroller report](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |
| Partial credit band | "a partial credit is allowed for tax liabilities between $3,400 and $4,500" | 2025 | [Comptroller report](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |
| Proprietor exemption | **$15,000**, "so that UBT liability after the $3,400 credit is zero for net incomes up to $100,000" | 2025 | [Comptroller report](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |
| Partnership exemption | **$5,000 plus $10,000 per partner**, "so that UBT liability is zero for net incomes up to $90,000 plus $10,000 times the number of partners" | 2025 | [Comptroller report](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |
| NYC personal-income-tax credit for UBT paid | **100%** for residents with taxable income up to **$42,000**, declining "gradually to 23% for taxable incomes higher than $142,000" | 2025 | [Comptroller report](https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/) |

The filing threshold, the simplified-return threshold and the estimated-payment threshold previously carried in this guide ($95,000, $250,000 and $3,400) are **not yet confirmed** -- see Not yet confirmed.

## The taxable base

- **Base is net income of the unincorporated business** carried on wholly or partly in NYC, taxed at 4% (Comptroller report, Table 1 and the UBT description).
- **Exemptions come off before the credit:** proprietors get $15,000 and partnerships $5,000 plus $10,000 per partner (Comptroller report).
- **Self-trading income is excluded** "with some exceptions" (Comptroller report); carried interest of fund managers is outside the base while management fees are inside it.
- **Multi-jurisdiction businesses are allocated, not fully taxed here:** "business income of entities doing businesses across taxing jurisdictions is allocated based on apportionment and sourcing rules," and UBT uses a **single sales factor** apportionment with **cost-of-performance sourcing for services provided within NYC, except for sales of tangible personal property** (Comptroller report).
- **Investment income under UBT** "is allocated using investment allocation percentages, which are themselves determined using issuer allocation percentages" (Comptroller report).
- **Owner salary, draws and income-tax deductions:** the previous rule in this guide (no deduction for the owner's salary or for income taxes) is **not yet confirmed** -- see Not yet confirmed.

## Deadlines and filing

- The UBT annual return form IDs (previously carried as NYC-202, NYC-202S and NYC-202EIN) and the UBT annual due date are **not yet confirmed** against an archived primary source -- see Not yet confirmed.
- The archived DOF business-tax page confirms the **corporate** calendar-year pattern and the extension mechanics: "Annual returns and tax payments must be postmarked by April 15 of the following year, if the corporation chooses an accounting period that is based on the calendar year," and "Businesses that are subject to the business corporation tax may get an automatic six-month extension by filing Form NYC-EXT. This extension is given only if the extension form is filed on or before the original due date for the return and the tax was estimated correctly and paid." Do not transfer those corporate rules to UBT without confirming them.
- Quarterly estimated-payment mechanics for UBT are **not yet confirmed** -- see Not yet confirmed.

## Penalties and interest

- **No archived source in this pack states the UBT late-filing, late-payment or interest rates.** The figures previously carried in this guide are removed and listed under Not yet confirmed.
- The archived DOF page confirms only that NYC can abate "interest and penalty" by legislation in specific circumstances (the One Big Beautiful Bill Act decoupling abatement, entered with Special Condition Code "OB"); that is an abatement rule, not the UBT penalty schedule.
- Do not quote a UBT penalty or interest percentage to a client until the NYC Administrative Code penalty sections are archived and read.

## Cross-border points

- **Apportionment:** UBT uses a **single sales factor** -- the City "gradually transitioned to only using the share of sales" between 2009 and 2018 (Comptroller report). A business with workers and real estate in NYC but a low share of NYC sales is taxed on less; the reverse increases the base.
- **Sourcing:** "GCT and UBT use cost of performance for services provided within NYC, except for sales of tangible personal property," while BCT adopted market-based sourcing (Comptroller report). A NYC-based service provider to an out-of-state customer is therefore still NYC-taxed on those receipts under UBT.
- **Multi-jurisdiction exposure is the norm, not the exception:** "Between tax year 2011 and 2020 ... on average 72.2% of the City tax liability came from multi-jurisdiction businesses" (Comptroller report).
- **No combined reporting under UBT** (Comptroller report), so a partner's own entity structure does not fold into one UBT return.
- **The IT-219 credit form and its mechanics** (previously carried as a 100% credit against NYC personal income tax flowing to Form IT-201-ATT) are **not yet confirmed** -- see Not yet confirmed. The archived report confirms the credit's shape (100% up to $42,000 taxable income, declining to 23% above $142,000) but not the form.

## Worked examples

Client facts in these examples are hypothetical. Only rates from the confirmed table above are used.

### Example 1: proprietor below the zero-liability point

A sole proprietor (hypothetical) has $90,000 of NYC net business income. The $15,000 proprietor exemption leaves $75,000; 4% of $75,000 is $3,000, which is under the $3,400 full credit, so UBT liability is $0. The Comptroller report states liability is zero "for net incomes up to $100,000."

```oa-check
name: NYC UBT proprietor below zero-liability point
inputs:
  net_income: 90000
  proprietor_exemption: 15000
  rate: 0.04
  full_credit: 3400
steps:
  - taxable: net_income - proprietor_exemption
  - tax_before_credit: taxable * rate
  - ubt_due: max(0, tax_before_credit - full_credit)
expected:
  taxable: 75000
  tax_before_credit: 3000
  ubt_due: 0
```

### Example 2: proprietor above the zero-liability point

A sole proprietor (hypothetical) has $120,000 of NYC net business income. $120,000 - $15,000 = $105,000; 4% is $4,200, which sits in the partial-credit band between $3,400 and $4,500. The exact partial-credit formula is **not yet confirmed** (see Not yet confirmed), so only the band is asserted here: liability is above $0 and below the full $4,200.

```oa-check
name: NYC UBT proprietor in partial-credit band
inputs:
  net_income: 120000
  proprietor_exemption: 15000
  rate: 0.04
steps:
  - taxable: net_income - proprietor_exemption
  - tax_before_credit: taxable * rate
expected:
  taxable: 105000
  tax_before_credit: 4200
```

### Example 3: partnership exemption

A two-partner LLC (hypothetical) has $110,000 of NYC net business income. The exemption is $5,000 + 2 x $10,000 = $25,000, leaving $85,000; 4% is $3,400, which is at the top of the full-credit band, so UBT liability is $0. The report states liability is zero "for net incomes up to $90,000 plus $10,000 times the number of partners" -- here $110,000.

```oa-check
name: NYC UBT two-partner LLC exemption
inputs:
  net_income: 110000
  base_exemption: 5000
  per_partner: 10000
  partners: 2
  rate: 0.04
  full_credit: 3400
steps:
  - exemption: base_exemption + per_partner * partners
  - taxable: net_income - exemption
  - tax_before_credit: taxable * rate
  - ubt_due: max(0, tax_before_credit - full_credit)
expected:
  exemption: 25000
  taxable: 85000
  tax_before_credit: 3400
  ubt_due: 0
```

## Ask the client first

1. **What is the entity form?** Sole proprietorship, partnership or LLC pays UBT; a C-corporation pays BCT and an S-corporation GCT instead (Comptroller report).
2. **Is the activity carried on wholly or partly in NYC, and where is the service performed?** UBT sources services by cost of performance for work done in NYC (Comptroller report).
3. **Is the income self-trading or carried interest?** Both sit outside the UBT base, with exceptions (Comptroller report).
4. **What is the client's NYC personal-income-tax position?** The credit for UBT paid is 100% up to $42,000 of taxable income and falls to 23% above $142,000 (Comptroller report), so the net cost of UBT depends on it.
5. **Which return and which due date apply?** Confirm the current UBT form IDs and dates with DOF before filing -- they are not yet confirmed in this guide.

## Sources

| Source | URL | Read on |
|---|---|---|
| NYC Comptroller, "Recent Trends in the City's Business Income Taxes" (Feb 18, 2025) -- UBT scope, 4% rate, $3,400/$4,500 credit bands, $15,000 proprietor and $5,000 + $10,000/partner exemptions, $42,000/$142,000 PIT-credit bands, single sales factor, cost-of-performance sourcing, self-trading and carried interest, no combined reporting, 72.2% multi-jurisdiction share | https://comptroller.nyc.gov/reports/recent-trends-in-the-citys-business-income-taxes/ | 2026-10-28 |
| NYC Department of Finance, business corporation tax page -- April 15 calendar-year filing date, Form NYC-EXT automatic six-month extension, OBBBA interest-and-penalty abatement, Administrative Code §§ 11-653 and 11-654 citations | https://www.nyc.gov/site/finance/business/business-corporation-tax.page | 2026-10-28 |

Not yet confirmed: the UBT filing threshold (previously carried as gross income over $95,000 under NYC Admin Code § 11-503(a); no archived copy of that section exists in this pack); the simplified-return threshold and form (previously carried as $250,000 gross income on Form NYC-202S); the estimated-payment threshold and form (previously carried as $3,400 on Form NYC-202EIN); the UBT annual return form IDs (previously carried as NYC-202) and the UBT annual due date and extension rule for UBT specifically (the archived April 15 and NYC-EXT rules are for the business corporation tax); the exact partial-credit formula between $3,400 and $4,500 (the report gives the band, not the arithmetic); the phase-out of the $15,000 proprietor exemption above $100,000 of net income; the UBT late-filing penalty, late-payment penalty and interest rates (no archived source states them; the previous $3,400 estimated-tax figure and the "line 17 tax" phase-out language are removed); the IT-219 credit form and its flow to Form IT-201-ATT (the report confirms the credit's percentages, not the form); the rule that the owner's salary, draws and income taxes are not deductible in the UBT base; the employee exclusion from UBT; and the current NYC Administrative Code Title 11 Chapter 5 section numbers (§§ 11-503, 11-510, 11-514 are cited in the previous draft but were not archived).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
