---
name: er-corporate-income-tax
description: "Source-cited draft: corporate income tax for Eritrea (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: ER
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eritrea Corporate Income Tax

## Corporate income tax and withholding

Companies operating in Eritrea are taxed on business profits under the Income Tax Proclamation No. 24/2011. The headline rate is reported inconsistently across country guides (30% vs 33%), so the figure should be confirmed against the Proclamation. The mining/petroleum sector is taxed under separate legislation at higher rates.

- **Standard corporate income tax rate** — 30% percent (approx — confirm; some sources cite 33%)  _([Income Tax Proclamation No. 24/2011](https://taxratesbycountry.com/tax-rates-in-eritrea/))_
- **Alternative headline rate cited by some guides** — 33% percent (approx — confirm which rate is current)  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea))_
- **Mining / petroleum sector corporate rate** — Higher rate (commonly cited around 38%) under sector-specific mining law percent (approx — confirm rate and statute)  _(Mining Proclamation / Mining Income Tax Proclamation)_
- **Tax base** — Net business profit (taxable income after allowable deductions)  _(Income Tax Proclamation No. 24/2011)_
- **Withholding tax on dividends (to non-residents)** — 5% percent (approx — confirm)  _([Income Tax Proclamation No. 24/2011](https://rivermate.com/guides/eritrea/taxes))_
- **Withholding tax on interest (to non-residents)** — 10% percent (approx — confirm)  _([Income Tax Proclamation No. 24/2011](https://rivermate.com/guides/eritrea/taxes))_
- **Withholding tax on royalties (to non-residents)** — 10% percent (approx — confirm)  _([Income Tax Proclamation No. 24/2011](https://rivermate.com/guides/eritrea/taxes))_
- **Corporate return filing / payment** — Annual return filed after the close of the tax year, with tax payable on assessment (approx — confirm exact deadline)  _(Income Tax Proclamation No. 24/2011)_
- **Capital gains** — Gains generally taxed as business income; no separate general CGT regime widely documented (approx — confirm)  _(Income Tax Proclamation No. 24/2011)_

## Recomputing examples

```oa-check
name: ER CIT 30% vs 33% reported rates on 1,000,000 ERN profit
inputs:
  profit: 1000000
steps:
  - low: profit * 0.30
  - high: profit * 0.33
  - diff: high - low
expected:
  low: 300000.00
  high: 330000.00
  diff: 30000.00
```
```oa-check
name: ER WHT on 100,000 ERN: dividends 5%, interest/royalties 10%
inputs:
  payment: 100000
steps:
  - div: payment * 0.05
  - interest: payment * 0.10
expected:
  div: 5000.00
  interest: 10000.00
```

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

## Sources

- Income Tax Proclamation No. 24/2011 (Eritrea)
- Mining Proclamation / Mining Income Tax Proclamation (Eritrea)

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
