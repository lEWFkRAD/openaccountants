---
name: er-payroll-social
description: "Source-cited draft: payroll & social contributions for Eritrea (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: ER
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eritrea Payroll & Social Contributions

## Payroll withholding and social contributions

Employers withhold personal income tax at source on salaries under the Income Tax Proclamation No. 24/2011. Eritrea does not operate a broad, well-documented mandatory national social-security contribution scheme comparable to neighbouring countries; arrangements should be confirmed locally as several figures here are uncertain.

- **Payroll income tax withholding (PAYE-equivalent)** — 2%–30% percent (Employer withholds progressive income tax from monthly salary)  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Payroll tax remittance deadline** — Withheld tax remitted to the Inland Revenue Department monthly (approx — confirm exact day of month)  _(Income Tax Proclamation No. 24/2011)_
- **National social security / pension scheme** — No widely documented mandatory general social-security contribution regime for private-sector employees (approx — confirm; may apply to civil servants/military)  _(Eritrean labour and social welfare legislation)_
- **Employer social-security contribution rate** — Not clearly established for private sector (approx — confirm)  _(Eritrean labour and social welfare legislation)_
- **Employee social-security contribution rate** — Not clearly established for private sector (approx — confirm)  _(Eritrean labour and social welfare legislation)_
- **Contribution wage base / cap** — Not documented (no clear contributory scheme) (approx — confirm)  _(Eritrean labour and social welfare legislation)_
- **National service salary deductions** — National-service obligations may affect remuneration arrangements in practice (approx — non-tax; confirm applicability)  _(National Service Proclamation No. 82/1995)_
- **Diaspora 2% tax interaction** — 2% percent (Eritrean nationals abroad remain liable to the 2% rehabilitation tax outside payroll)  _([Proclamation on the 2% Rehabilitation and Recovery Tax (diaspora tax)](https://rivermate.com/guides/eritrea/taxes))_

## Recomputing examples

```oa-check
name: ER PAYE on ERN 3,000 monthly salary (bands to 20%)
inputs:
  salary: 3000
steps:
  - b1: (min(salary, 1000) - 800) * 0.05
  - b2: (min(salary, 1500) - 1000) * 0.10
  - b3: (min(salary, 2000) - 1500) * 0.15
  - b4: (min(salary, 3000) - 2000) * 0.20
  - withhold: b1 + b2 + b3 + b4
expected:
  withhold: 335.00
```
```oa-check
name: ER diaspora 2% on 100,000 ERN worldwide income
inputs:
  income: 100000
steps:
  - diaspora: income * 0.02
expected:
  diaspora: 2000.00
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
- Proclamation on the 2% Rehabilitation and Recovery Tax (Eritrea)

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
