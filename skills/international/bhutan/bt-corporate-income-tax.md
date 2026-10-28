---
name: bt-corporate-income-tax
description: "Source-cited draft: corporate income tax for Bhutan (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BT
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bhutan Corporate Income Tax

## Bhutan Corporate Income Tax

## Corporate and Business Income Tax (income year 2025)

- **CIT/BIT overview** — Bhutan taxes incorporated companies under Corporate Income Tax (CIT) and unincorporated businesses under Business Income Tax (BIT), both governed by the Income Tax Act 2001. For income year 2025 the standard CIT rate is 30%; from 1 January 2026 the Income Tax Act 2025 cuts CIT to a flat 22%.  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **Corporate Income Tax standard rate (2025)** — 30% percent  _([Income Tax Act of the Kingdom of Bhutan 2001](https://thebhutanese.bt/how-pit-bit-and-cit-reductions-in-the-income-tax-bill-impact-you/))_
- **Corporate Income Tax rate from 2026** — 22% (flat, all companies) percent (effective 1 January 2026 under the Income Tax Act of Bhutan 2025)  _([Income Tax Act of Bhutan 2025](https://thebhutanese.bt/major-changes-in-bhutans-income-tax-from-2026-explained/))_
- **Business Income Tax rate (unincorporated, 2025)** — 30% percent ((approx — confirm))  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **Tax base** — Net profit (gross income less allowable business expenses, depreciation and deductions) per the Act  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **TDS / withholding on dividends** — 10% on dividends from a Bhutan-registered company (bonus shares excluded) percent  _([Income Tax Act of the Kingdom of Bhutan 2001 (TDS provisions)](https://www.drc.gov.bt/what-is-tds/))_
- **TDS / withholding on interest** — 5% on interest from fixed deposits with financial institutions in Bhutan percent  _([Income Tax Act of the Kingdom of Bhutan 2001 (TDS provisions)](https://www.drc.gov.bt/what-is-tds/))_
- **TDS on contract income (Bhutanese firms)** — 2% of gross contract payment percent  _([Income Tax Act of the Kingdom of Bhutan 2001 (TDS provisions)](https://www.drc.gov.bt/what-is-tds/))_
- **TDS on contract income (non-Bhutanese firms)** — 3% of gross contract payment percent  _([Income Tax Act of the Kingdom of Bhutan 2001 (TDS provisions)](https://www.drc.gov.bt/what-is-tds/))_
- **Withholding on royalties / payments to non-residents** — Withheld at source per the Act; treaty rates may apply (Bhutan–India) ((approx — confirm rate))  _(Income Tax Act of the Kingdom of Bhutan 2001 (TDS provisions))_
- **Loss carry-forward** — Tax losses carried forward (extended to indefinite carry-forward under the Income Tax Act 2025) ((approx — confirm 2025 carry-forward period))  _(Income Tax Act of the Kingdom of Bhutan 2001)_
- **Presumptive / small business regime** — Simplified presumptive tax for businesses with turnover under Nu 5 million (introduced under the Income Tax Act 2025; professionals excluded)  _([Income Tax Act of Bhutan 2025](https://thebhutanese.bt/major-changes-in-bhutans-income-tax-from-2026-explained/))_
- **CIT / BIT filing and payment deadline** — By 31 March following the close of the income year ((approx — confirm exact date))  _([Income Tax Act of the Kingdom of Bhutan 2001](https://www.drc.gov.bt/notification-tax-filing-for-income-year-2025/))_

## Worked examples

```oa-check
name: BT CIT 30% (2025) vs 22% (from 2026) on Nu 1,000,000 profit
inputs:
  profit: 1000000
steps:
  - tax_2025: profit * 0.30
  - tax_2026: profit * 0.22
  - saving: tax_2025 - tax_2026
expected:
  tax_2025: 300000.00
  tax_2026: 220000.00
  saving: 80000.00
```

```oa-check
name: BT TDS on dividends 10% and contract payments 2%/3%
inputs:
  dividend: 500000
  contract_bhutanese: 200000
  contract_foreign: 200000
steps:
  - div_tds: dividend * 0.10
  - contract_tds_local: contract_bhutanese * 0.02
  - contract_tds_foreign: contract_foreign * 0.03
expected:
  div_tds: 50000.00
  contract_tds_local: 4000.00
  contract_tds_foreign: 6000.00
```

## Sources

| Source | URL | as_of |
|---|---|---|
| Income Tax Act of the Kingdom of Bhutan 2001 (cited inline) | https://thebhutanese.bt/how-pit-bit-and-cit-reductions-in-the-income-tax-bill-impact-you/ | 2026-10-28 |
| Income Tax Act of Bhutan 2025 (cited inline) | https://thebhutanese.bt/major-changes-in-bhutans-income-tax-act-2025/ | 2026-10-28 |
| DRC TDS provisions (cited inline) | https://www.drc.gov.bt/what-is-tds/ | 2026-10-28 |

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
