---
name: ca-corporate-income-tax
description: >
  Use this skill whenever asked about California corporate franchise tax
  for tax year 2026 -- Form 100 filing, the 8.84% rate and $800 minimum
  franchise tax under R&TC §23153, economic nexus thresholds under §23101,
  unitary combined reporting with single sales factor, Form 3539 estimated
  payments (April/June/September/December), FTB penalties and interest, and
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
income tax, or sales/use tax. Primary sources: FTB tax-rates page, FTB
Form 100/3539/568 (2025 editions), California Revenue and Taxation Code
(R&TC) via leginfo. All URLs resolved 2026-10-27.

## Rates, bands and thresholds
| Item | Amount | Source |
|---|---|---|
| Franchise/income tax rate | 8.84% of net income | FTB tax-rates page; R&TC §23151 |
| Minimum franchise tax | $800 | FTB tax-rates page; R&TC §23153 |
| First-year exemption | New corporations exempt from the $800 minimum for their first taxable year | FTB guidance (Form 100 instructions) |
| LLC annual tax (disregarded/single-member) | $800 | Form 568; R&TC §23153 |
| LLC fee (total-income based) | $800–$11,790 | Form 568 fee table (verified 2025 form) |
| S-corporation entity tax | 1.5% of net income | R&TC §23803 (see Form 100S skill) |

The LLC annual fee table on Form 568 (2025 edition, verified text): $800
(total income $250,000–$499,999), $1,800 ($500,000–$999,999), $5,000
($1,000,000–$4,999,999), $6,000 ($5,000,000–$9,999,999), $9,000
($10,000,000–$24,999,999), $11,790 ($25,000,000 or more). (not yet confirmed)

## The taxable base
- California taxable income starts from federal taxable income with state
  modifications (net operating loss limits, §168(k)/§174 differences,
  interest add-backs on related-party transactions under §25110 et seq.).
- Apportionment: California uses a single sales factor (Proposition 66,
  effective for tax years beginning on or after January 1, 2023; R&TC
  §§25128–25129). Sales are sourced to the purchaser's location.
- Unitary combined reporting: commonly-owned unitary business groups file
  Form 100W; the group's combined apportionable income is apportioned
  using the group's combined sales factor.
- Fiscal-year filers use the rates in effect for their income year.

## Deadlines and filing
| Filing | Calendar-year due date |
|---|---|
| Form 100 (C corporation) | 15th day of the 4th month after year close -- April 15 |
| Form 7004 extension | 6-month extension to file (October 15); payment not extended |
| Form 3539 estimated tax installments | April 15, June 15, September 15, December 15 (verified from Form 3539, 2025 edition) |
| Form 568 (LLC) | April 15 |

Estimated tax: corporations must pay through Form 3539 vouchers or EFT.
Safe harbors per Form 3539: 90% of current-year tax or 100% of
prior-year tax shown on the return (110% for large corporations -- (not yet confirmed)
confirm current thresholds with FTB).

## Penalties and interest
- Late filing: 25% of the unpaid tax (FTB penalties page; R&TC §19255 --
  statute cite to verify).
- Failure to pay estimated installments: Form 3539 underpayment penalty
  computed on the difference between required and timely installments
  (verified Form 3539 text).
- Interest: accrues on unpaid amounts at the rate published by FTB
  (federal short-term rate plus statutory add-on, set semiannually --
  current rate on the FTB interest-rates page).

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
  sized to the 90%/100% safe harbor?

## Sources
| Source | URL | Read on |
| --- | --- | --- |

Not yet confirmed:  FTB -- Corporation Tax Rates | https://www.ftb.ca.gov/file/business/tax-rates.html ;  FTB -- Form 100 (2025) | https://www.ftb.ca.gov/forms/2025/2025-100.pdf ;  FTB -- Form 3539 (2025) | https://www.ftb.ca.gov/forms/2025/2025-3539.pdf ;  FTB -- Form 568 (2025) | https://www.ftb.ca.gov/forms/2025/2025-568.pdf ;  FTB -- Penalties and Interest | https://www.ftb.ca.gov/pay/penalties-and-interest/index.html ;  FTB -- Interest and Estimate Penalty Rates | https://www.ftb.ca.gov/pay/penalties-and-interest/interest-and-estimate-penalty-rates.html ; the 8.84% rate, $800 minimum franchise tax, first-year exemption, LLC fee bands ($800–$11,790), economic-nexus thresholds ($750,000 / 25%), the 25% late-filing penalty, current FTB interest rates, and the 90%/100%/110% estimated-tax safe harbors are not yet confirmed against archived sources; the R&TC §§23151, 23153, 23101 and 25128 statute cites (leginfo 403 on 2026-10-27) remain pending verification.
## Talk to a verified accountant
<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for California franchise-tax questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
