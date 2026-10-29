---
name: dc-transfer-pricing
description: >
  Use this skill whenever asked about District of Columbia transfer
  pricing for tax year 2026 — mandatory combined reporting for
  unitary businesses for taxable years beginning on or after
  2011-01-01, the unitary-group concept, the DC single-sales-factor
  apportionment, and how combined reporting changes related-party
  planning. Trigger on "DC combined reporting", "District of
  Columbia unitary group", "DC transfer pricing", "DC water's
  edge", "DC apportionment factor", "DC D-20 combined".
jurisdiction: US-DC
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - dc-franchise-tax
---

# District of Columbia transfer pricing (combined reporting), tax year 2026

> **Source-cited draft.** Built from D.C. Code §§ 47-1807.02, 47-1808.03 and 47-1810.02 and the OTR Combined Reporting and Business Franchise Tax Rates pages, read on 2026-10-28. No accountant has reviewed it. Do not take a position from it without review by a qualified professional.

DC is a **mandatory combined-reporting state**: the OTR Combined Reporting page states that businesses that are part of a **unitary business** must file a combined franchise-tax return, and that the requirement applies to taxable years beginning on or after **January 1, 2011**. Combined reporting means related-party intragroup transactions are eliminated at the group level and the group's DC share is driven by the apportionment factor, not by intercompany pricing alone.

## Who this applies to

- Every member of a **unitary business** with DC nexus files one combined return — corporate and unincorporated members alike ([OTR Combined Reporting page](https://otr.cfo.dc.gov/page/combined-reporting-business-entities), read 2026-10-28).
- Because combination is mandatory, classic transfer-pricing levers (royalties, management fees, intercompany debt) mostly wash out inside the combined group; the live issues become **where the group's sales sit** (the single sales factor) and **which entities are in the group**.
- International groups: the water's-edge treatment of foreign affiliates is not confirmed in the archived sources (see the Not yet confirmed line).

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Combination | Mandatory for unitary groups, taxable years beginning on or after 1 January 2011 | [OTR Combined Reporting page](https://otr.cfo.dc.gov/page/combined-reporting-business-entities): "For tax years beginning on or after January 1, 2011, a corporation or unincorporated business entity subject to tax and engaged in a unitary business with one or more corporations or unincorporated business entities" |
| Franchise tax rate on combined income | 8.25% of DC-apportioned taxable income; $250/$1,000 minimum tax | [D.C. Code § 47-1807.02](https://code.dccouncil.gov/us/dc/council/code/sections/47-1807.02); [§ 47-1808.03](https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.03) |
| Apportionment factor | **Single sales factor** | [D.C. Code § 47-1810.02(d-2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02): "All business income shall be apportioned to the District by multiplying the income by the sales factor" |
| Intragroup transactions | Eliminated in combination | Inherent in combined reporting (OTR page) |

## The taxable base

- The group's **combined net income**, with intragroup transactions eliminated, apportioned to DC by the **sales factor alone** ([§ 47-1810.02(d-2)](https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02)). Earlier years used a property-payroll-sales formula (double-weighted sales for 2011–2014); the sales-only factor applies to taxable years beginning after 31 December 2014.
- The unitary test is the standard unity-of-business doctrine (operational or functional integration); the statutory definition of the unitary group was not extracted from the archived sources this run — see the Not yet confirmed line.

## Deadlines and filing

- Combined returns ride the franchise-tax calendar (D-20/D-30): estimated payments 15 April, 15 June, 15 September and 15 December, with the 110%-of-prior-year safe harbor (see `dc-franchise-tax`).
- OTR audit adjustments to combination scope follow DC's assessment windows (not confirmed in the archived sources).

## Penalties and interest

- **Failure-to-file / failure-to-pay additions:** 5% a month up to 25% each, with the failure-to-file addition reduced by the failure-to-pay addition for the same months ([D.C. Code § 47-4213](https://code.dccouncil.gov/us/dc/council/code/sections/47-4213), archived 2026-10-28).
- **Interest** on unpaid tax and on underpayments of estimated tax runs at 10% a year, compounded daily ([D.C. Code § 47-4201](https://code.dccouncil.gov/us/dc/council/code/sections/47-4201), archived 2026-10-28); businesses compute underpayment interest on Form D-2220.
- Common failure modes: (1) filing separate D-20s for a unitary group — combination has been mandatory since 2011; (2) excluding a foreign subsidiary without confirming water's-edge status; (3) building royalty/fee structures that wash out in combination and surprise planners when DC tax doesn't move; (4) sales-by-destination data not maintained at group level for the single sales factor.

## Cross-border points

- Worldwide combination is the default posture of a mandatory combined-reporting regime; a water's-edge election's availability and mechanics are not confirmed in the archived sources (see `dc-cross-border` and the Not yet confirmed line).
- Federal § 245A/BEAT/GILTI interactions with DC combined income: DC starts from federal taxable income; the decoupling detail for those provisions was not read from an archived source this run.

## Worked examples

Client facts below are hypothetical; all rates and the single-sales-factor formula are the confirmed rules from the tables above.

**A unitary group with $10,000,000 combined net income and a DC sales-factor share of 0.12:**

```oa-check
name: DC combined group DC-share
inputs:
  combined_income: 10000000
  factor: 0.12
  rate: 0.0825
steps:
  - dc_base: combined_income * factor
  - tax: dc_base * rate
expected:
  dc_base: 1200000.00
  tax: 99000.00
```

**A $2,000,000 intercompany royalty inside the same group** — eliminated on combination, so the DC tax effect at the group level is zero before factor effects:

```oa-check
name: DC intragroup royalty wash
inputs:
  royalty: 2000000
  eliminated: 2000000
steps:
  - net_effect: royalty - eliminated
expected:
  net_effect: 0.00
```

## Ask the client first

- Is every unitary member on the combined return — including LLCs and foreign subsidiaries (water's-edge status confirmed)?
- Are intercompany fee/royalty plans modeled at the combined level, not entity level?
- Is apportionment data (sales by destination) maintained group-wide for the single sales factor?
- Any restructuring that changes unity or affiliation percentages?

## Sources

| Source | URL | Read on |
|---|---|---|
| OTR: Combined Reporting of Business Entities | https://otr.cfo.dc.gov/page/combined-reporting-business-entities | 2026-10-28 |
| D.C. Code § 47-1810.02 (apportionment; single sales factor) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1810.02 | 2026-10-28 |
| D.C. Code § 47-1807.02 (corporate rate and minimum tax) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1807.02 | 2026-10-28 |
| D.C. Code § 47-1808.03 (unincorporated business rate and minimum tax) | https://code.dccouncil.gov/us/dc/council/code/sections/47-1808.03 | 2026-10-28 |
| D.C. Code § 47-4213 (failure-to-file/pay additions) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4213 | 2026-10-28 |
| D.C. Code § 47-4201 (interest, 10% compounded daily) | https://code.dccouncil.gov/us/dc/council/code/sections/47-4201 | 2026-10-28 |
| OTR: DC Business Franchise Tax Rates | https://otr.cfo.dc.gov/page/dc-business-franchise-tax-rates | 2026-10-28 |

Not yet confirmed: the statutory unitary-group definition and affiliation/ownership threshold (D.C. Code Title 47 ch. 18 section text beyond § 47-1810.02 was not extracted this run); the availability and mechanics of a water's-edge election for foreign affiliates; DC's assessment windows for combination-scope adjustments; and DC's decoupling (if any) from federal § 245A/BEAT/GILTI in the combined-income starting point.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
