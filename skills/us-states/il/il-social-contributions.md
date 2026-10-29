---
name: il-social-contributions
description: >
  Use this skill whenever asked about Illinois employer social
  contributions for tax year 2026 — IDES unemployment contribution
  rates and the 2026 $14,250 wage base, the Fund Builder surcharge,
  the 5.4% small-employer rate, minimum penalty, employer workers'
  compensation insurance under the Illinois Workers' Compensation
  Act, and the absence of state disability/paid-leave payroll taxes.
  Trigger on "Illinois UI rate", "Illinois SUTA", "IDES contribution",
  "Illinois unemployment wage base 2026", "Illinois Fund Builder",
  "Illinois employer taxes". Source-cited draft; sources/US-IL-ides-ui-rates-2026.pdf
  PDF read 2026-10-27.
jurisdiction: US-IL
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - il-payroll
---

# Illinois social contributions (IDES unemployment + workers' comp) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Source-cited draft, run of 27 October 2026. Illinois employer social contributions are: IDES unemployment insurance (contribution) tax under the Unemployment Insurance Act (820 ILCS 405), mandatory workers' compensation insurance, and federal FICA — Illinois has **no** state disability insurance, **no** paid family/medical leave contribution, and **no** state retirement mandate for private employers. **Source status:** the IDES historical rate chart PDF (`UI_tax_rates_2026.pdf`) was downloaded and text-read 2026-10-27 from ides.illinois.gov — the 2026 wage base, rate floors/ceilings, standard rate, small-employer rate, and minimum penalty below are read directly from that PDF. The statute page (820 ILCS 405) renders via JavaScript — section-level cites .

### Who this applies to

- Employers covered under 820 ILCS 405 (general tests: payroll above statutory thresholds in 20 or more weeks, or one or more employees in each of 20 weeks — exact current test text: ). Out-of-state employers with Illinois employees are covered on the same basis.
- The contribution is **employer-only** — Illinois employees pay no state UI tax.
- Workers' compensation: most Illinois employers must carry coverage from the first employee (broad employer definition under 820 ILCS 305 — confirm current text: ).

## Rates, bands and thresholds

| Item | 2026 amount | Source |
|---|---|---|
| Taxable wage base | **$14,250** per employee | sources/US-IL-ides-ui-rates-2026.pdf (archived: sources/US-IL-ides-ui-rates-2026.pdf, WAGE BASE row: 14,250), read 2026-10-27 |
| Minimum contribution rate | **0.750%** (includes Fund Builder) | archived sources/US-IL-ides-ui-rates-2026.pdf: MINIMUM RATES row |
| Maximum contribution rate | **7.050%** (includes Fund Builder) | archived sources/US-IL-ides-ui-rates-2026.pdf: MAXIMUM RATES row |
| Standard (ineligible) rate | **3.350%** | archived sources/US-IL-ides-ui-rates-2026.pdf, STANDARD (Ineligible) RATE row: 3.350% |
| Fund Builder component | **0.550%** (embedded in all rates above) | archived sources/US-IL-ides-ui-rates-2026.pdf, FUND BUILDING row: 0.550% |
| Small-employer rate (gross wages < $50,000) | **5.4%** flat | archived sources/US-IL-ides-ui-rates-2026.pdf (Wages less than $50,000 column) |
| Minimum penalty | **$50** | archived sources/US-IL-ides-ui-rates-2026.pdf, MINIMUM PENALTY row |
| Employee share of UI | none — employer-only | 820 ILCS 405 structure; section text  |
| State disability / paid family leave | none | absence confirmed; no such IL program |

Rates are experience-rated (benefit-conversion factor 138.4% and state experience factor 102% for 2026 — both appear in the archived sources/US-IL-ides-ui-rates-2026.pdf). Base: covered wages up to $14,250 per employee per year.

## The taxable base

The base follows the federal starting point with Illinois modifications; see Rates, bands and thresholds above and the archived IL-1040/IL-1120 instructions in Sources.

## Deadlines and filing

- Quarterly contribution and wage reports (Form UI-3/40) due the last day of the month following each quarter (1/31, 4/30, 7/31, 10/31) — confirm current dates on the IDES filing page: .
- Annual rate notices issue in December/January with an appeal window (confirm: ).
- Workers' compensation: continuous coverage obligation; proof of insurance required for many state contracts and permits.

## Penalties and interest

The IDES chart fixes a **$50 minimum penalty** for 2026 (PDF, read 2026-10-27); the percentage late-filing/late-payment penalty and interest rates sit in 820 ILCS 405 —  for current percentages. Common failure modes: (1) out-of-state employers missing Illinois coverage for Illinois-based staff; (2) assuming the small-employer 5.4% rate is favorable — it can exceed an experience rate; (3) treating workers' comp as optional — Illinois requires it broadly from employee one.

## Cross-border points

- Localization-of-service rules decide which state gets the wages for multi-state employees (confirm IDES guidance: ); reciprocal coverage agreements allow single-state UI for multi-state work (confirm FL participation: ).
- FUTA credit against Illinois contribution follows the standard pattern; 2026 credit-reduction status for Illinois: .
- Common-ownership wage treatment rules exist on the IDES site (page identified 2026-10-27) for related-entity employers.

## Worked examples

An experience-rated Illinois employer at the 2026 minimum rate on one employee:

```oa-check
name: IL UI at minimum rate one employee
inputs:
  base: 14250
  rate: 0.0075
steps:
  - tax: base * rate
expected:
  tax: 106.88
```

Same employer with 10 employees at the 2026 maximum rate:

```oa-check
name: IL UI at maximum rate ten employees
inputs:
  base: 14250
  n: 10
  rate: 0.0705
steps:
  - wages: base * n
  - tax: wages * rate
expected:
  wages: 142500.00
  tax: 10046.25
```

## Ask the client first

- What is your current IDES experience rate, and does the small-employer 5.4% flat rate beat it (gross wages under $50,000)?
- Are multi-state employees' wages correctly localized to Illinois?
- Is workers' compensation coverage in force for every Illinois employee?
- Pull the December 2025 rate notice to confirm the 2026 rate and appeal window.

## Sources

| Source | URL | Read on |
|---|---|---|
| sources/US-IL-ides-ui-rates-2026.pdf | https://ides.illinois.gov/content/dam/soi/en/web/ides/ides_forms_and_publications/UI_tax_rates_2026.pdf | 2026-10-27 |
| IDES employer taxes/reporting | https://ides.illinois.gov/employer-resources/taxes-reporting.html | 2026-10-27 |
| IDES annual rate page | https://ides.illinois.gov/employer-resources/taxes-reporting/rates.html | 2026-10-27 |

Not yet confirmed: 820 ILCS 405 section text (JS-rendered), penalty percentages beyond the PDF minimum
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
