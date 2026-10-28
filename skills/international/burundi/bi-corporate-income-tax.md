---
name: bi-corporate-income-tax
description: "Source-cited draft: corporate income tax for Burundi (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BI
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Corporate Income Tax

## Corporate income tax (Impôt sur les sociétés)

Companies resident in Burundi are taxed on profits at a flat rate, with a minimum tax based on turnover for loss-making years. Withholding taxes apply to passive income and to payments to non-residents. Confirm rates and deadlines with the current General Tax Code.

- **Standard corporate income tax rate** — 30% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Minimum tax for loss-making years** — 1% of annual turnover %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Tax base** — Net accounting profit adjusted for non-deductible expenses and exempt income, per the General Tax Code  _(Law No. 1/02 of 24 January 2013 (income tax law))_
- **Capital gains on commercial immovable property** — 15% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Withholding tax on dividends** — 15% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Withholding tax on interest** — 15% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Withholding tax on royalties** — 15% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Withholding tax on management/service fees** — 15% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Branch profit remittance tax** — 15% % ((approx — confirm))  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Annual corporate tax return filing deadline** — Generally by 31 March following the close of the calendar tax year ((approx — confirm))  _(Law No. 1/02 of 24 January 2013 (income tax law))_
- **Advance corporate tax payments** — Provisional/advance instalments are payable during the year, with final balance on filing ((approx — confirm))  _(Law No. 1/02 of 24 January 2013 (income tax law))_

## Worked examples

```oa-check
name: BI CIT 30% on BIF 10,000,000 profit; 1% minimum tax on turnover
inputs:
  profit: 10000000
  turnover: 50000000
steps:
  - normal_tax: profit * 0.30
  - minimum_tax: turnover * 0.01
  - payable: max(normal_tax, minimum_tax)
expected:
  normal_tax: 3000000.00
  minimum_tax: 500000.00
  payable: 3000000.00
```

```oa-check
name: BI dividend withholding 15% on BIF 2,000,000 dividend
inputs:
  dividend: 2000000
steps:
  - wht: dividend * 0.15
  - net: dividend - wht
expected:
  wht: 300000.00
  net: 1700000.00
```

## Sources

| Source | URL | as_of |
|---|---|---|
| Law No. 1/02 of 24 January 2013 (income tax law) (cited inline) | https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/ | 2026-10-28 |

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
