---
name: nh-interest-dividends-note
description: "Note on the repeal of the New Hampshire Interest & Dividends Tax effective for tax periods beginning on or after January 1, 2025, the phase-down schedule, and prior-year filing obligations."
jurisdiction: US-NH
tax_year: 2025
last_updated: 2026-11-04
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# NH Interest Dividends Note

New Hampshire's Interest & Dividends (I&D) Tax is repealed for tax periods beginning on or after January 1, 2025. Residents no longer pay state tax on interest and dividend income. Prior-year returns remain due, and the business taxes (BPT and BET) are unaffected by the repeal.

## Who this applies to

- New Hampshire residents who received interest and dividend income in tax years through 2024 and still have filing, payment, or refund obligations.
- Business owners who assumed "NH has no income tax" means no state business tax: the Business Profits Tax (BPT) and Business Enterprise Tax (BET) still apply. See `nh-bpt-bet.md`.

## Rates, bands and thresholds

I&D Tax phase-down schedule, per the NH DRA repeal announcement (January 23, 2025):

| Taxable periods ending | I&D rate |
| --- | --- |
| Prior to December 31, 2023 | 5% |
| On or after December 31, 2023 | 4% |
| On or after December 31, 2024 | 3% |
| Tax periods beginning on or after January 1, 2025 | 0% -- repealed |

Under prior law the tax was imposed at 3% on New Hampshire residents receiving more than $2,400 of interest and dividend income filing as an individual, or more than $4,800 filing a joint return. Exemptions were available for residents 65 or older, blind, disabled, or unable to work and under 65.  _(NH DRA news release, January 23, 2025)_

Related business taxes (unchanged by the repeal, detailed in `nh-bpt-bet.md`): Business Profits Tax 7.5% for taxable periods ending on or after December 31, 2023  _(RSA 77-A:2)_ and Business Enterprise Tax 0.55% for taxable periods ending on or after December 31, 2022  _(RSA 77-E:2)_.

## The taxable base

The I&D tax base was New Hampshire source interest and dividend income received by residents, above the exemption thresholds cited above.  _(NH DRA news release, January 23, 2025; RSA Chapter 77)_

## Deadlines and filing

- Taxpayers required to file a 2024 I&D return (or an earlier-year return), on a fiscal or calendar year basis, must still file by the statutory due date with any tax, interest, and penalty due.  _(NH DRA news release, January 23, 2025)_
- Estimated I&D payments for tax year 2025 should not be filed; payments made in error are refundable on written request.  _(NH DRA news release, January 23, 2025)_
- 2025 I&D forms will not be available because no 2025 return is required.  _(NH DRA news release, January 23, 2025)_

## Penalties and interest

Prior-year obligations are unchanged: taxable periods beginning on or before December 31, 2024 remain subject to audit and collection, and the repeal provides no amnesty for earlier tax years.  _(NH DRA news release, January 23, 2025)_

## Cross-border points

- All tax year 2024 I&D overpayments will be refunded unless applied to prior balances; overpayments for years before 2024 are refunded on request within the statute of limitations.  _(NH DRA news release, January 23, 2025)_
- The repeal does not reduce BPT or BET liability. A client who says "NH repealed the income tax, so I owe nothing" may still owe BPT and/or BET.

## Worked examples

### Worked example 1: 2024 return still due

A NH resident with $10,000 of interest and dividends for calendar 2024 files a 2024 I&D return by the statutory due date at the 3% rate for periods ending on or after December 31, 2024, above the $2,400 exemption.

```oa-check
name: 2024 I&D tax
inputs:
  income: 10000
  exemption: 2400
  rate: 0.03
steps:
  taxable: income - exemption
  tax: round(taxable * rate, 2)
```

Tax due: $228.00 on the $7,600 above the exemption.

### Worked example 2: 2025 needs no return

The same resident's 2025 interest and dividends: no I&D return, no estimated payments, and no 2025 I&D form exists.

```oa-check
name: 2025 I&D
inputs:
  income: 10000
  rate_2025: 0
steps:
  tax: round(income * rate_2025, 2)
```

Tax due: $0.00.

## Ask the client first

- Which tax years through 2024 still have unfiled I&D returns or unpaid balances?
- Were any 2025 estimated I&D payments made in error (refundable in writing)?
- Does the client owe BPT or BET notwithstanding the I&D repeal?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| NH DRA news release: Repeal of NH Interest and Dividends Tax Now in Effect (Jan 23, 2025) | https://www.revenue.nh.gov/news-and-media/repeal-nh-interest-and-dividends-tax-now-effect | 2026-10-31 |
| RSA 77-A:2 (BPT rate) | https://gc.nh.gov/rsa/html/V/77-A/77-A-2.htm | 2026-10-28 |
| RSA 77-E:2 (BET rate) | https://gc.nh.gov/rsa/html/V/77-E/77-E-2.htm | 2026-10-31 |

Not yet confirmed: the 1923 enactment date of the I&D Tax; the DP-10 form name and the April 15, 2025 due date for the final 2024 return; the exemption amounts for residents 65 or older under prior law beyond the categories named in the DRA release.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
the OpenAccountants network.

- Use it in your AI: 
- Meet the accountants: 

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
