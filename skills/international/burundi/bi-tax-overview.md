---
name: bi-tax-overview
description: "Source-cited draft: tax overview for Burundi (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BI
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi Tax Overview

## Burundi tax system at a glance

Burundi taxes are administered by the Office Burundais des Recettes (OBR). The framework rests on the General Tax Code / income tax law (Law No. 1/02 of 24 January 2013) and a separate VAT law. The figures below are a source-cited draft pending review by a licensed Burundi accountant.

- **National tax authority** — Office Burundais des Recettes (OBR) — Burundi Revenue Office  _([Loi portant création de l'Office Burundais des Recettes (OBR)](https://www.obr.bi))_
- **Currency** — Burundian Franc (BIF)  _(Banque de la République du Burundi)_
- **Tax year** — Calendar year (1 January to 31 December) ((approx — confirm))  _(Law No. 1/02 of 24 January 2013 (income tax law))_
- **Basis of taxation** — Residents taxed on worldwide income; non-residents taxed only on Burundi-source income  _(Law No. 1/02 of 24 January 2013 (income tax law))_
- **Top personal income tax rate** — 30% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Standard corporate income tax rate** — 30% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Does Burundi levy VAT?** — Yes — VAT (Taxe sur la Valeur Ajoutée, TVA) at a standard rate of 18%  _([Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law)](https://www.eac.int/financial/eac-tax-matrices/value-added-tax))_
- **Standard VAT rate** — 18% %  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law))_
- **Withholding tax on dividends** — 15% %  _([Law No. 1/02 of 24 January 2013 (income tax law)](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_
- **Monthly payroll/VAT remittance deadline** — 15th of the month following the taxable period  _([OBR filing rules under the General Tax Code](https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/))_

## Worked examples

```oa-check
name: BI headline rates check — 30% CIT on BIF 5,000,000 and 18% VAT on BIF 1,000,000
inputs:
  profit: 5000000
  net_sale: 1000000
steps:
  - cit: profit * 0.30
  - vat: net_sale * 0.18
expected:
  cit: 1500000.00
  vat: 180000.00
```

```oa-check
name: BI dividend WHT 15% on BIF 1,000,000
inputs:
  dividend: 1000000
steps:
  - wht: dividend * 0.15
expected:
  wht: 150000.00
```

## Sources

| Source | URL | as_of |
|---|---|---|
| Law No. 1/02 of 24 January 2013 (income tax law) (cited inline) | https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/ | 2026-10-28 |
| Loi relative a la Taxe sur la Valeur Ajoutee (VAT Law) (cited inline) | https://www.eac.int/financial/eac-tax-matrices/value-added-tax | 2026-10-28 |
| Office Burundais des Recettes (OBR) (cited inline) | https://www.obr.bi | 2026-10-28 |

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
