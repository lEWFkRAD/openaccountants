---
name: ms-social-contributions
description: >
  Use this skill whenever asked about Mississippi employer social
  contributions for 2026 -- unemployment insurance administered by the
  Mississippi Department of Employment Security (MDES), employer quarterly
  wage and contribution reporting, and the interaction with federal
  FUTA/SUTA credits. Trigger on "Mississippi unemployment", "MDES",
  "Mississippi SUTA", "Mississippi employer contributions". Source-cited
  draft; MDES administration, new-employer rates, quarterly due dates
  and interest/penalty rules verified on mdes.ms.gov 2026-10-28/29.
jurisdiction: US-MS
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-29
version: 0.2
depends_on:
  - ms-income-tax
---

# Mississippi social contributions (employer side), tax year 2026

> **General reference only.** General reference for AI-assisted workflows; not client-specific advice.

## Who this applies to

Mississippi employers (including out-of-state employers with Mississippi employees). MDES administers Mississippi UI; employers file quarterly wage and contribution reports -- MDES references bulk filing for the "Form UI-2 Tax Report". Mississippi has no state disability, family-leave, or state-mandated retirement contribution for private employers beyond federal FICA/FUTA (see Not yet confirmed for scope caveats).

## Rates, bands and thresholds

| Item | Figure | Source |
|---|---|---|
| New-employer (start-up) UI rate | "1.00% the first year of liability, 1.10% the second year of liability and 1.20% the third and subsequent years of liability until the employer is eligible for a modified rate" | [MDES Unemployment Tax Rates](https://www.mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/unemployment-tax-rates/) |
| Experience (modified) rates | "Your tax rate will vary between 0.0% and 5.4%" | MDES Unemployment Tax Rates |

MDES: published rates "do not include the Workforce Investment and Training contribution rate that might be applicable for the rate year."

## The taxable base

Quarterly gross wages up to the state UI taxable wage base (base figure: see Not yet confirmed), reported to MDES with contributions; modified rate = "the ratio of benefits charged to an employers' account to taxable wages paid by the employer... plus the general experience ratio of the whole state unemployment program" (MDES Unemployment Tax Rates). Timely SUTA payment preserves the 5.4% FUTA credit (federal rule).

## Deadlines and filing

MDES quarterly due dates: "1st Quarter Due April 30th 2nd Quarter Due July 31st 3rd Quarter Due October 31st 4th Quarter Due January 31st... If the any of the above dates fall on a weekend, the due date will be on the next business day" (MDES Quarterly Report and Tax Due Dates). Quarterly tax and wage reports can be filed and paid online.

## Penalties and interest

MDES: "Interest is calculated at 1 percent per month on any portion of a month in which the payment is past due"; late-filing penalty "beginning 30 days after the due date of the report... an additional 10 percent of tax due"; late-payment penalty "60 days after due date or when a warrant for collection is issued... 10 percent of tax due" (MDES Interest and Penalties).

## Cross-border points

Multi-state employers: localize employees under the interstate reciprocal coverage agreement tests (see Not yet confirmed); Mississippi income-tax withholding is separate (see `ms-payroll.md`).

## Worked examples

**Example 1 -- FUTA net per employee (federal context):**

```oa-check
name: FUTA net 0.6 percent
inputs:
  wage_base: 7000
  net_rate: 0.006
steps:
  - futa: wage_base * net_rate
expected:
  futa: 42.00
```

**Example 2 -- new-employer UI on a hypothetical $9,500 taxable-wage base (rate from the skill's own confirmed table above):**

```oa-check
name: MS UI new employer
inputs:
  wage_base: 9500
  rate: 0.01
steps:
  - ui: wage_base * rate
expected:
  ui: 95.00
```

## Ask the client first

- Are MDES quarterly filings current (experience rating depends on them)?
- Multi-state workforce -- is Mississippi the localization state?
- Successor-employer or rate-transfer events on account purchases?

## Sources

| Source | URL | Read on |
|---|---|---|
| MDES Unemployment Tax Rates -- new-employer 1.00%/1.10%/1.20% schedule, 0.0%–5.4% modified-rate range, WIT contribution note | https://www.mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/unemployment-tax-rates/ | 2026-10-29 |
| MDES Quarterly Report and Tax Due Dates -- April 30 / July 31 / Oct 31 / Jan 31 due dates | https://www.mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/quarterly-report-and-tax-due-dates/ | 2026-10-29 |
| MDES Interest and Penalties -- 1%/month interest, 10% late-filing and late-payment penalties | https://www.mdes.ms.gov/employers/unemployment-tax/reporting-and-filing/interest-and-penalties/ | 2026-10-29 |

Not yet confirmed: the current Mississippi UI taxable wage base; the per-employer experience-rate schedule table; UI-2 form ID beyond MDES's bulk-filing reference; interstate localization (reciprocal coverage agreement) tests; whether any state-mandated retirement contribution applies to specific employer classes.

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

