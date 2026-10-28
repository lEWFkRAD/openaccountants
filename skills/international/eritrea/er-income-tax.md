---
name: er-income-tax
description: "Source-cited draft: personal income tax for Eritrea (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: ER
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Eritrea Personal Income Tax

## Personal income tax bands (employment income)

Personal income tax is progressive and applied at source on employment income. The monthly bands below are widely reported by country tax guides; the precise schedule should be confirmed against the Income Tax Proclamation No. 24/2011.

- **Tax-free threshold (monthly employment income)** — Up to ERN 800 per month is exempt ERN/month (approx — confirm)  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Band: ERN 801–1,000 per month** — 5 percent  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Band: ERN 1,001–1,500 per month** — 10 percent  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Band: ERN 1,501–2,000 per month** — 15 percent  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Band: ERN 2,001–3,000 per month** — 20 percent  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Band: above ERN 3,000 per month** — 30 percent  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Overall progressive rate range** — 2% to 30% percent (approx — lowest band reported as 2% by some sources)  _([Income Tax Proclamation No. 24/2011](https://taxatlas.io/country/eritrea/income-tax))_
- **Collection method for employment income** — Tax withheld at source by the employer (PAYE-equivalent)  _(Income Tax Proclamation No. 24/2011)_
- **Residence test** — Generally based on physical presence / domicile in Eritrea during the tax year (approx — confirm day-count test)  _(Income Tax Proclamation No. 24/2011)_
- **Non-resident employment income** — Taxed on Eritrean-source income; final withholding may apply (approx — confirm)  _(Income Tax Proclamation No. 24/2011)_
- **Diaspora income tax** — 2 percent (rehabilitation and recovery tax on worldwide income of Eritrean nationals abroad)  _([Proclamation on the 2% Rehabilitation and Recovery Tax (diaspora tax)](https://rivermate.com/guides/eritrea/taxes))_
- **Filing / payment of withheld tax** — Employer remits monthly; annual reconciliation after year-end (approx — confirm exact dates)  _(Income Tax Proclamation No. 24/2011)_

## Recomputing examples

```oa-check
name: ER monthly salary tax on ERN 3,000 (bands 5/10/15/20%)
inputs:
  salary: 3000
steps:
  - b1: (min(salary, 1000) - 800) * 0.05
  - b2: (min(salary, 1500) - 1000) * 0.10
  - b3: (min(salary, 2000) - 1500) * 0.15
  - b4: (min(salary, 3000) - 2000) * 0.20
  - tax: b1 + b2 + b3 + b4
expected:
  b1: 10.00
  b2: 50.00
  b3: 75.00
  b4: 200.00
  tax: 335.00
```
```oa-check
name: ER top band 30% on ERN 5,000 salary above ERN 3,000 plus band tax
inputs:
  salary: 5000
steps:
  - top: (salary - 3000) * 0.30
  - tax: 335 + top
expected:
  top: 600.00
  tax: 935.00
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
- Proclamation on the 2% Rehabilitation and Recovery Tax (Eritrea, diaspora tax)

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
