---
name: wi-corporate-income-tax
description: >
  Use this skill whenever asked about Wisconsin corporate income tax for tax
  year 2026 -- the Form 4 franchise tax at a flat 7.9% on Wisconsin-apportioned
  income (income tax at 7.9% for certain foreign corporations in exclusively
  interstate/foreign commerce), the "doing business in Wisconsin" filing
  triggers and P.L. 86-272 limits, the economic development surcharge (3% of
  tax, minimum $25, maximum $9,800), single sales factor apportionment, S
  corporations on Form 5S, exempt entities, and the 18% per year interest on
  delinquent taxes. Trigger on "Wisconsin corporate tax", "Wisconsin Form 4",
  "Wisconsin franchise tax", "7.9%", "economic development surcharge",
  "Wisconsin doing business", "Wisconsin corporation nexus", "Form 5S",
  "Wisconsin single sales factor".
  Source-cited draft; 2025 Form 4 instructions (IC-100, R. 10-25) PDF read
  2026-10-27; Wis. Stat. ch. 71 subch. III.
jurisdiction: US-WI
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - wi-income-tax
  - wi-transfer-pricing
---

# Wisconsin corporate income / franchise tax (Form 4) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Wisconsin professional.

## Who this applies to

Wisconsin taxes corporations under **Wis. Stat. ch. 71, subch. III** on **Form 4** (non-combined) or **Form 6** (combined -- see `wi-transfer-pricing`). Most corporations owe the **franchise tax**; a narrow class of foreign corporations owes the **income tax**. Both run at **7.9%**. S corporations file **Form 5S** (entity-level tax on built-in gains and certain items; owners taxed at the individual rates).

**Source status (as_of 2026-10-27):** [2025 Form 4 instructions, IC-100 (R. 10-25)](https://www.revenue.wi.gov/TaxForms2025/2025-Form4-inst.pdf) fetched as PDF and read -- rate, surcharge, doing-business list, combined tests, penalties, apportionment all quoted from it. 2026 instructions not yet published at read time; figures are 2025 unless flagged.

### 2. Who applies

- **Franchise tax:** all **domestic** (Wisconsin-organized) corporations, and **foreign corporations doing business in Wisconsin** (or buying/selling Wisconsin lottery prizes), unless exempted by statute or barred by federal law.
- **Income tax:** only foreign corporations **not** subject to the franchise tax that own property in Wisconsin or whose Wisconsin business is **exclusively in foreign or interstate commerce** -- the P.L. 86-272 pocket.
- **"Doing business" triggers** (per IC-100): selling lottery prizes; issuing credit/debit cards to Wisconsin customers; regularly selling to Wisconsin customers who receive in Wisconsin; regularly soliciting business in Wisconsin -- **except where P.L. 86-272 protects** solicitation of orders for tangible personal property.
- **Always-file rule:** multistate corporations, Wisconsin-only corporations, domestic insurers, and unlicensed corporations must file even absent "doing business."
- **Exempt entities** (secs. 71.26(1)/71.45(1)): insurers exempt under IRC §501(c)(15), completely inactive corporations that filed Form 4H, certain credit unions that filed Form CU, and others. (not yet confirmed)
- **S corporations:** Form 5S; REITs/RICs/REMICs/FASITs file separately and can never join a combined group.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| Franchise tax rate | **7.9%** flat on Wisconsin-apportioned franchise tax base | IC-100, read 2026-10-27 |
| Income tax rate (foreign, exclusively interstate/foreign commerce) | **7.9%**; US-obligation income excluded under income tax law but included under franchise tax law | IC-100, read 2026-10-27 |
| Base start | Federal taxable income **before NOL deduction and special deductions** (Form 1120 line 28), modified per Schedule M | IC-100, read 2026-10-27 |
| Economic development surcharge | **3% of franchise/income tax before credits; min $25, max $9,800** | IC-100, read 2026-10-27 |
| Apportionment | **Single sales factor** (WI sales / total sales), Schedule A-01 Part I; specialized industries use A-02…A-09 | IC-100, read 2026-10-27 |
| S corp | Form 5S; owners at 3.5%–7.65% individual rates | IC-100 + `wi-income-tax` | (not yet confirmed)
| Urban transit | Special tax under sec. 71.39 | IC-100, read 2026-10-27 | (not yet confirmed)

### 4. Deadlines

| Filing | Due |
|---|---|
| Form 4 / 5S / 6 | On or before the **federal due date**; a Wisconsin extension runs to **30 days after the federal extended date** -- automatic, no WI application |
| Short-year return | Federal short-year due date |
| Final return (dissolution) | Within 3 months of dissolution (2nd/3rd month per IC-100 rule) |
| Estimated tax | Quarterly corporate estimates (Form 4ES) -- amounts per IC-100 |

### 5. Penalties and interest

- **Interest on delinquent taxes: 18% per year** -- one of the highest in the country. **AUDIT FLASH POINT.** (not yet confirmed)
- Civil penalties up to **100% of unreported tax** for negligence/fraud; false-return criminal exposure: fine up to $10,000 and imprisonment.
- Reportable-transaction non-disclosure penalties per IC-100.

### 6. Cross-border

- **P.L. 86-272** protects solicitation-only tangible-goods sellers from the franchise tax but not from the income tax branch (which exists precisely for that federal pocket).
- **Single sales factor** pulls out-of-state sellers with Wisconsin customers into the base -- market-based sourcing for sales; specialized-industry schedules for services/intangibles.
- **Combined groups** (Form 6) apply a **water's edge** rule -- see `wi-transfer-pricing`.
- Wisconsin has no reciprocal corporate relief with other states.

### 7. Worked examples

**Example A -- standalone Form 4 with ED surcharge.**

```oa-check
name: Form 4 tax plus economic development surcharge
inputs:
  apportioned_income: 1000000
  rate: 0.079
  ed_rate: 0.03
  ed_min: 25
  ed_max: 9800
steps:
  - tax: apportioned_income * rate
  - ed_raw: tax * ed_rate
  - ed: min(max(ed_raw, ed_min), ed_max)
  - total: tax + ed
expected:
  tax: 79000.00
  ed_raw: 2370.00
  ed: 2370.00
  total: 81370.00
```

**Example B -- surcharge cap bites on a large liability.**

```oa-check
name: ED surcharge capped at 9,800
inputs:
  tax: 500000
  ed_rate: 0.03
  ed_max: 9800
steps:
  - ed_raw: tax * ed_rate
  - ed: min(ed_raw, ed_max)
  - total: tax + ed
expected:
  ed_raw: 15000.00
  ed: 9800
  total: 509800
```

### 8. Ask the client

- Organized in Wisconsin or doing business there? Card issuers, lottery, e-commerce sellers get caught by the doing-business list.
- Is the activity pure solicitation of tangible-goods orders (P.L. 86-272)?
- In a commonly controlled unitary group? Then Form 6, not Form 4 (`wi-transfer-pricing`).
- Specialized industry (services, intangibles, freight)? Different apportionment schedule.
- NOLs: Wisconsin computes its own; track the Schedule M differences (bonus depreciation, §163(j) conformity list in Schedule I).

### 9. Sources

- [2025 Form 4 instructions IC-100 (R. 10-25)](https://www.revenue.wi.gov/TaxForms2025/2025-Form4-inst.pdf) -- PDF read 2026-10-27 (all quoted figures)
- [Wis. Stat. § 71.21 et seq.](https://docs.legis.wisconsin.gov/statutes/statutes/71/21) -- read 2026-10-27 (not yet confirmed)
- `wi-transfer-pricing` (this pack) -- combined reporting; `wi-income-tax` -- S corp owner rates
- **not yet confirmed:** 2026 Form 4 instructions (not published at read time); Form 4ES estimate thresholds; insurance premiums tax (sec. 71.35) detail.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Wisconsin Form 4 and franchise tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | -- | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
