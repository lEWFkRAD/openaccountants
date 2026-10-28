---
name: bt-income-tax
description: "Source-cited draft: personal income tax for Bhutan (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BT
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bhutan Personal Income Tax

## Personal Income Tax bands and rates (income year 2025)

- **Income up to Nu 300,000** — 0% (tax-free) percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/personal-income-tax-pit/))_
- **Income Nu 300,001 to 500,000** — 5% percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/personal-income-tax-pit/))_
- **Income Nu 500,001 to 750,000** — 10% percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/personal-income-tax-pit/))_
- **Income Nu 750,001 to 1,200,000** — 15% percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/personal-income-tax-pit/))_
- **Income Nu 1,200,001 to 2,000,000** — 20% percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/personal-income-tax-pit/))_
- **Income Nu 2,000,001 to 3,500,000** — 25% percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/personal-income-tax-pit/))_
- **Income above Nu 3,500,000** — 30% percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/personal-income-tax-pit/))_
- **Surcharge on high income (2025)** — 10% of net tax payable where gross annual income is Nu 1,000,000 or more percent  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://thebhutanese.bt/major-changes-in-bhutans-income-tax-from-2026-explained/))_
- **PIT taxable income sources** — Salary, rental income, dividends, interest, income from cash crops, and other personal income aggregated per the Act ((approx — confirm))  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **Deduction — Provident Fund / GIS (2025 regime)** — Employee Provident Fund and Group Insurance Scheme contributions deductible from employment income (replaced by a 15% standard deduction (capped Nu 150,000) under the Income Tax Act 2025 from 2026)  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **Deduction — education allowance** — Children's education expenses deductible up to the per-child cap set in the Act ((approx — confirm cap amount))  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **Deduction — housing loan interest** — Interest on a housing loan deductible against rental income per the Act ((approx — confirm))  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **Tax residence / liability** — Taxation is primarily source-based; Bhutanese-source personal income is taxable regardless of citizenship ((approx — confirm residence definition))  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **PIT filing and payment deadline** — By 31 March following the income year (income year 2025 filed by 31 March 2026) ((approx — confirm exact date in DRC notification))  _(Income Tax Act of the Kingdom of Bhutan 2001 (https://www.drc.gov.bt/notification-tax-filing-for-income-year-2025/))_

## Worked examples

```oa-check
name: BT PIT bands on Nu 1,000,000 annual income (2025 bands)
inputs:
  income: 1000000
steps:
  - b2: (min(income, 500000) - 300000) * 0.05
  - b3: (min(income, 750000) - 500000) * 0.10
  - b4: (min(income, 1200000) - 750000) * 0.15
  - tax: b2 + b3 + b4
expected:
  b2: 10000.00
  b3: 25000.00
  b4: 37500.00
  tax: 72500.00
```

```oa-check
name: BT 2025 surcharge 10% of net tax where gross income >= Nu 1,000,000
inputs:
  gross_income: 1000000
  net_tax: 72500
steps:
  - surcharge_applies: (gross_income - 1000000) / (1000000)
  - surcharge: net_tax * 0.10
  - total: net_tax + surcharge
expected:
  surcharge_applies: 0.00
  surcharge: 7250.00
  total: 79750.00
```

## Sources

| Source | URL | as_of |
|---|---|---|
| Income Tax Act of the Kingdom of Bhutan 2001 — DRC PIT page (cited inline) | https://www.drc.gov.bt/personal-income-tax-pit/ | 2026-10-28 |
| Income Tax Act changes 2025 (cited inline) | https://thebhutanese.bt/major-changes-in-bhutans-income-tax-act-2025/ | 2026-10-28 |

Sources are the statutes/agencies already cited inline in this guide, listed as_of 2026-10-28 and **unverified against archived evidence**.

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
