---
name: bm-payroll-social
description: "Source-cited draft: payroll & social contributions for Bermuda (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BM
tax_year: 2025
last_updated: 2026-10-28
version: "0.2"
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bermuda Payroll & Social Contributions

## Payroll tax

- **Payroll tax overview** — Payroll tax is Bermuda's principal tax on employment income, levied under the Payroll Tax Act 1995 and the Payroll Tax Rates Act 1995. It has an employer portion and an employee portion (which the employer may deduct from pay but remains liable to remit). Remuneration is capped at BMD 1,000,000 per person per year. Rates are set annually in the Budget; the values below should be confirmed against the gov.bm tables for the 1 April 2025 to 31 March 2026 year.
- **Governing legislation** — Payroll Tax Act 1995 and Payroll Tax Rates Act 1995  _(Payroll Tax Act 1995; Payroll Tax Rates Act 1995 (https://www.gov.bm/payroll-tax))_
- **Taxable remuneration cap** — BMD 1,000,000 per person per annum BMD  _(Payroll Tax Act 1995 (https://taxsummaries.pwc.com/bermuda/corporate/other-taxes))_
- **Tax structure** — Two portions — employer portion (on gross taxable remuneration) and employee portion (progressive across remuneration bands); employer is liable to remit the full amount  _(Payroll Tax Act 1995 (https://www.gov.bm/calculating-payroll-tax-2025))_
- **Employer portion rate (standard, large employers)** — Tiered by total annual remuneration of the employer; top standard band around 10.25% (approx — confirm 2025-26 employer band table) percent (approx — confirm 2025-26 employer band table)  _(Payroll Tax Rates Act 1995 (https://www.gov.bm/calculating-payroll-tax-2025))_
- **Employer portion rate (small employers)** — Reduced employer rates apply to smaller payrolls and exempt undertakings; lowest bands around 1.50%-5.25% (approx — confirm 2025-26 employer band table) percent (approx — confirm 2025-26 employer band table)  _(Payroll Tax Rates Act 1995 (https://www.gov.bm/calculating-payroll-tax-2025))_
- **Employee portion — Band 1 (first BMD 48,000)** — 0.50% on the first BMD 48,000 of annual remuneration (confirm 2025-26 band thresholds) percent (confirm 2025-26 band thresholds)  _(Payroll Tax Rates Act 1995 (https://www.gov.bm/calculating-payroll-tax-2025))_
- **Employee portion — Band 2** — 9.25% on remuneration above BMD 48,000 up to the next band threshold (approx — confirm 2025-26 band table and upper threshold) percent (approx — confirm 2025-26 band table and upper threshold)  _(Payroll Tax Rates Act 1995 (https://www.gov.bm/calculating-payroll-tax-2025))_
- **Employee portion — band structure** — Progressive (marginal) across 5 bands, with higher marginal rates on higher remuneration up to the BMD 1,000,000 cap (confirm 5-band rates for 2025-26) (confirm 5-band rates for 2025-26)  _(Payroll Tax Rates Act 1995 (https://www.gov.bm/calculating-payroll-tax-2025))_
- **Payroll tax filing & payment frequency** — Quarterly returns and payment to the Office of the Tax Commissioner; due within 15 days after each quarter end (confirm current due date) (confirm current due date)  _(Payroll Tax Act 1995 (https://www.gov.bm/payroll-tax))_
- **Social insurance (contributory pension) total contribution** — BMD 75.30 per week (combined employer + employee) BMD/week  _(Contributory Pensions Act 1970 (https://www.gov.bm/department/social-insurance))_
- **Social insurance split** — Employer pays 50% (BMD 37.65/week) and employee pays 50% (BMD 37.65/week) for workers aged 16-64 BMD/week  _(Contributory Pensions Act 1970 (https://www.gov.bm/department/social-insurance))_
- **Social insurance — employees aged 65+** — Only the employer portion is due; no employee contribution  _(Contributory Pensions Act 1970 (https://www.gov.bm/department/social-insurance))_
- **Social insurance remittance deadline** — Employer billed monthly; payment due by the last Friday of that month  _(Contributory Pensions Act 1970 (https://www.gov.bm/department/social-insurance))_
- **Occupational (private) pension contribution** — Mandatory for Bermudians/spouses under the National Pension Scheme; typically 5% employer + 5% employee of pensionable earnings (approx — confirm current rate) percent (approx — confirm current rate)  _(National Pension Scheme (Occupational Pensions) Act 1998 (https://www.gov.bm/bermuda-pension))_


## Recomputing examples

```oa-check
name: Employee payroll tax on BMD 100,000 remuneration (0.50% first 48,000 + 9.25% excess)
inputs:
  remuneration: 100000
steps:
  - band1: min(remuneration, 48000) * 0.005
  - band2: max(remuneration - 48000, 0) * 0.0925
  - employee_tax: band1 + band2
expected:
  band1: 240.00
  band2: 4810.00
  employee_tax: 5050.00
```
```oa-check
name: Weekly social insurance contribution split (BMD 75.30 total)
inputs:
  total_week: 75.30
steps:
  - employer: total_week / 2
  - employee: total_week / 2
expected:
  employer: 37.65
  employee: 37.65
```

## Sources

| Source | URL | Read on |
|---|---|---|
| Government of Bermuda — Bermuda Corporate Income Tax (CIT effective 1 Jan 2025; payroll tax unchanged) | https://www.gov.bm/CIT | 2026-10-28 |


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