---
name: bd-tax-overview
description: "Source-cited draft: tax overview for Bangladesh (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BD
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bangladesh Tax Overview

## Bangladesh tax system at a glance

- **Income year (tax year)** — 1 July to 30 June (banks, insurers and financial institutions use the calendar year; foreign-parent subsidiaries may follow the parent's year)  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/tax-administration)_
- **Currency** — Bangladeshi Taka (BDT / Tk)  _(NBR (National Board of Revenue))_
- **Tax authority** — National Board of Revenue (NBR), under the Internal Resources Division, Ministry of Finance  _(NBR (National Board of Revenue) — https://nbr.gov.bd)_
- **Basis of taxation** — Residents are taxed on worldwide income; non-residents are taxed only on Bangladesh-source income  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **Headline top personal income tax rate** — 30% percent  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Act 2024 — https://taxsummaries.pwc.com/bangladesh/individual/taxes-on-personal-income)_
- **Personal tax-free threshold (general taxpayer)** — BDT 350,000 BDT (AY 2025-26 / income year 2024-25; raised to BDT 375,000 from income year 2025-26)  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Act 2024 — https://taxsummaries.pwc.com/bangladesh/individual/taxes-on-personal-income)_
- **Headline corporate tax rate (non-listed company)** — 27.5% percent (reduced to 25% where prescribed receipts/payments are made through banking channels; listed companies 20-22.5%)  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025 — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **VAT (value added tax)** — Yes — standard rate 15% percent  _(Value Added Tax and Supplementary Duty Act 2012 — https://taxsummaries.pwc.com/bangladesh/corporate/other-taxes)_
- **Individual return filing deadline (Tax Day)** — 30 November following the end of the income year  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/individual/tax-administration)_
- **Company return filing deadline** — 15th day of the 7th month following income-year end, or 15 September (whichever is later) (approx — confirm exact month; sources describe it as around mid-September for July-June filers)  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/tax-administration)_

## Recomputing examples

```oa-check
name: BD VAT 15% on 1,000,000 BDT supply
inputs:
  supply: 1000000
steps:
  - vat: supply * 0.15
expected:
  vat: 150000.00
```
```oa-check
name: BD company 1,000,000 BDT profit at 27.5% headline vs 25% banking rate
inputs:
  profit: 1000000
steps:
  - headline: profit * 0.275
  - banking: profit * 0.25
expected:
  headline: 275000.00
  banking: 250000.00
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

- Income Tax Act 2023 (Bangladesh), as amended by Finance Act 2024 / Finance Ordinance 2025 — https://nbr.gov.bd
- Value Added Tax and Supplementary Duty Act 2012 (Bangladesh)

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
