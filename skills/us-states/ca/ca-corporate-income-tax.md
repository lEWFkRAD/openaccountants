---
name: ca-corporate-income-tax
description: >
  Use this skill whenever asked about California corporate franchise tax
  for tax year 2026 -- Form 100 filing, the 8.84% rate and $800 minimum
  franchise tax under R&TC §23153, economic nexus thresholds under §23101,
  unitary combined reporting with single sales factor, Form 100-ES estimated
  installments (April/June/September/December), the automatic 7-month filing
  extension paid with FTB 3539, FTB penalties and interest, and
  LLC annual tax/fee interaction. Trigger on "California corporate income
  tax", "California franchise tax", "FTB Form 100", "8.84 percent",
  "minimum franchise tax California", "California combined report",
  "California estimated tax corporation", "Form 3539". Source-cited draft;
  FTB pages and forms read 2026-10-27.
jurisdiction: US-CA
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - ca-smllc-form-568
---

# California corporate franchise tax v0.1

## Who this applies to
Covers the California franchise/income tax on corporations (Form 100), the
minimum franchise tax, combined reporting, and corporate estimated tax.
Does not cover the S-corporation entity tax (Form 100S -- separate skill),
the LLC annual tax/fee (Form 568 -- see `ca-smllc-form-568`), personal
income tax, or sales/use tax. Primary sources: FTB tax-rates, LLC,
doing-business, extension, penalties and interest-rates pages; FTB 2025
Corporation Tax Booklet; FTB 2026 Form 100-ES instructions; California
Revenue and Taxation Code (R&TC) via leginfo. All URLs archived
2026-10-31/2026-11-01.

## Rates, bands and thresholds
| Item | Amount | Source |
|---|---|---|
| Franchise/income tax rate | 8.84% of net income | FTB tax-rates page; R&TC §23151 |
| Minimum franchise tax | $800 | FTB tax-rates page; R&TC §23153 |
| First-year exemption | New corporations exempt from the $800 minimum for their first taxable year | FTB guidance (Form 100 instructions) |
| LLC annual tax (disregarded/single-member) | $800 | Form 568; R&TC §23153 |
| LLC fee (total-income based) | $900–$11,790 | FTB LLC filing requirements page (fee table effective for tax years beginning on/after 1/1/2021) |
| S-corporation entity tax | 1.5% (11/2 percent) of net income | R&TC §23802(b)(1) (see Form 100S skill) |

The LLC fee table (FTB LLC filing requirements page): $900 (total
California income $250,000–$499,999), $2,500 ($500,000–$999,999), $6,000
($1,000,000–$4,999,999), $11,790 ($5,000,000 or more). The $800 figure is
the LLC annual tax, not a fee tier; the old $1,800/$5,000/$9,000 tiers no
longer exist. LLCs must estimate and pay the fee by the 15th day of the
6th month of the tax year using FTB 3536.

## The taxable base
- California taxable income starts from federal taxable income with state
  modifications (net operating loss limits, §168(k)/§174 differences,
  interest add-backs on related-party transactions under §25110 et seq.).
- Apportionment: California uses a single sales factor for all business
  income other than financial corporations, for taxable years beginning
  on or after January 1, 2013 (Proposition 39; R&TC §25128.7). Financial
  corporations under §25128(b) use a different formula (Proposition 66
  changed that formula effective 1/1/2023). Sales are sourced to the
  purchaser's location.
- Unitary combined reporting: commonly-owned unitary business groups file
  Form 100W; the group's combined apportionable income is apportioned
  using the group's combined sales factor.
- Fiscal-year filers use the rates in effect for their income year.

## Deadlines and filing
| Filing | Calendar-year due date |
|---|---|
| Form 100 (C corporation) | 15th day of the 4th month after year close -- April 15 |
| Automatic filing extension | FTB automatically allows a 7-month extension for corporations filing Form 100 (to the 15th day of the 11th month after year close -- November 15 for calendar-year filers, moved to the next business day if it falls on a weekend or holiday). No application required; it extends filing only, not payment. Pay the balance due with FTB 3539 (Corporations and Exempt Organizations). Form 7004 is the federal extension form, not a California one. |
| Form 100-ES estimated tax installments | 15th day of the 4th, 6th, 9th, and 12th months of the taxable year -- April 15, June 15, September 15, December 15 for calendar-year filers (FTB 2026 Form 100-ES instructions) |
| Form 568 (LLC) | April 15 |

Estimated tax: corporations pay via Form 100-ES vouchers or EFT.
California does not conform to the federal 90%/100% safe harbors -- the
underpayment penalty is based on current-year tax only (2026 Form 100-ES
instructions, General Information). Exceptions are computed cumulatively.
Exception A (prior year's tax): payments by each installment date equal or
exceed 100% of the prior year's tax prorated to installments; not
available in the first taxable year. A "large corporation" (California net
income of $1 million or more in any of the three preceding taxable years)
may use the prior-year exception only for the first installment and must
pay 30%/70%/70%/100% of the estimated tax in installments 1-4. Standard
installment percentages of estimated tax for all other corporations:
30%/40%/0%/30%.

## Penalties and interest
- Late filing: 5% of the tax per month or fraction, capped at 25%
  (R&TC §19131(a); FTB penalties page). §19255 is the 20-year collection
  statute of limitations, not the penalty provision.
- Failure to pay estimated installments: underpayment penalty computed on
  the difference between required and timely installments, current-year
  basis (Form 100-ES instructions; FTB 5806 figures the penalty).
- Interest: accrues on unpaid amounts at the rate published by FTB
  (federal short-term rate plus statutory add-on, set semiannually --
  7% for 07/01/2025-06/30/2026 and 07/01/2026-12/31/2026 per the FTB
  interest-rates page).

## Cross-border points
- Public Law 86-272 shields certain solicitation-only activities from
  net-income tax; California applies it narrowly (FTB guidance).
- Water's-edge election (R&TC §25109) limits combined reporting to
  US-plus-combined-unitary-group affiliates; election is binding for
  5 years.
- California does not conform to federal international provisions such
  as FDII/GILTI in the same form -- check current conformity status in
  FTB legal notices before relying on federal starting points.
- Related-party interest, rent and royalty payments to affiliated
  members are subject to add-back under §25110 unless an
  arm's-length/business-purpose exception is established (see
  `ca-transfer-pricing`).
- Economic nexus (R&TC §23101(b), FTB doing-business page): for 2025,
  California sales over $757,070 (or 25% of total sales), California
  real/tangible property over $75,707 (or 25%), or California payroll
  over $75,707 (or 25%) means "doing business". Thresholds are indexed
  annually ($735,019 for 2024, $711,538 for 2023).

## Worked examples
A calendar-year C corporation has $500,000 of income apportioned to
California for 2026. Tax:

```oa-check
name: corporate tax on 500000 apportioned income
inputs:
  income: 500000
  rate: 0.0884
  minimum: 800
steps:
  - tax: income * rate
  - due: max(minimum, tax)
expected:
  tax: 44200.00
  due: 44200.00
```

A unitary group has worldwide sales of $10,000,000, of which $4,000,000
are California sales (single sales factor); combined California
apportionable income $2,000,000:

```oa-check
name: single sales factor and combined tax
inputs:
  ca_sales: 4000000
  total_sales: 10000000
  income: 2000000
  rate: 0.0884
steps:
  - factor: ca_sales / total_sales
  - apportioned: income * factor
  - tax: apportioned * rate
expected:
  factor: 0.40
  apportioned: 800000.00
  tax: 70720.00
```

## Ask the client first
- Is the entity incorporated in California or doing business there
  (employees, inventory, marketplace sales, economic nexus thresholds)?
- Is the group unitary? Has a water's-edge election been made, and when
  does it expire?
- Any related-party interest, rent, or royalty payments that trigger
  §25110 add-back?
- Did the corporation qualify for the first-year minimum-tax exemption?
- Are estimated payments on the April/June/September/December schedule
  sized to current-year tax (CA's basis) or to the prior-year-tax
  exception (Form 100-ES)?

## Sources
| Source | URL | Read on |
| --- | --- | --- |
| FTB Corporation Tax Rates page | https://www.ftb.ca.gov/file/business/tax-rates.html | 2026-11-01 |
| FTB 2025 Corporation Tax Booklet (Form 100 instructions) | https://www.ftb.ca.gov/forms/2025/2025-100-booklet.html | 2026-11-01 |
| FTB 2026 Form 100-ES instructions | https://www.ftb.ca.gov/forms/2026/2026-100-es-instructions.html | 2026-11-01 |
| FTB LLC filing requirements page | https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html | 2026-10-31 |
| FTB Doing Business in California page | https://www.ftb.ca.gov/file/business/doing-business-in-california.html | 2026-11-01 |
| FTB Extension to File page | https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html | 2026-11-01 |
| FTB Penalties and Interest page | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html | 2026-11-01 |
| FTB Interest and Estimate Penalty Rates page | https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html | 2026-10-31 |
| R&TC §19131 (late-filing penalty) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=19131 | 2026-11-01 |
| R&TC §23153 (minimum franchise tax) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23153. | 2026-11-01 |
| R&TC §23802 (S-corporation entity tax) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=23802 | 2026-11-01 |
| R&TC §25128.7 (single sales factor) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=25128.7 | 2026-11-01 |

Not yet confirmed: none -- every figure in this file was read in the
archived sources listed above.
## Talk to a verified accountant
<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for California franchise-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
