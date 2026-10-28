---
name: bi-vat-gst
description: "Source-cited draft: vat / gst for Burundi (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BI
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Burundi VAT / GST

## Value Added Tax (Taxe sur la Valeur Ajoutée)

Burundi operates a VAT (TVA) administered by the OBR, with a standard rate of 18% and a reduced rate for essential goods. VAT-registered businesses file periodically and may offset input VAT against output VAT.

- **Standard VAT rate** — 18% %  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law))_
- **Reduced rate on essential goods (basic foodstuffs, medicine, educational items)** — 10% % ((approx — confirm))  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law), https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/)_
- **Exempt supplies** — Healthcare services (and other supplies listed in the VAT Law) are exempt  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law), https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/)_
- **Zero-rated supplies** — Exports of goods are zero-rated ((approx — confirm))  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law))_
- **Compulsory VAT registration threshold** — BIF 100,000,000 BIF (annual taxable turnover (approx — confirm))  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law))_
- **VAT return filing frequency** — Monthly  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law), https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/)_
- **Monthly VAT return and payment deadline** — 15th of the month following the taxable period ((approx — confirm))  _(OBR filing rules under the VAT Law, https://remotepeople.com/countries/burundi/hire-employees/payroll-tax/)_
- **Input VAT recovery** — Registered taxpayers deduct input VAT on business purchases against output VAT collected  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law))_
- **Reverse charge on imported services** — VAT on services supplied by non-residents is self-accounted by the Burundi recipient under the reverse-charge mechanism ((approx — confirm))  _(Loi relative à la Taxe sur la Valeur Ajoutée (VAT Law))_

## Worked examples

```oa-check
name: BI VAT payable, 18% output on BIF 20,000,000 less 18% input on BIF 7,000,000
inputs:
  sales_net: 20000000
  purchases_net: 7000000
steps:
  - output: sales_net * 0.18
  - input: purchases_net * 0.18
  - payable: output - input
expected:
  output: 3600000.00
  input: 1260000.00
  payable: 2340000.00
```

```oa-check
name: BI VAT registration threshold test at BIF 120,000,000 turnover
inputs:
  turnover: 120000000
  threshold: 100000000
steps:
  - over_threshold: turnover - threshold
  - vat_on_excess: over_threshold * 0.18
expected:
  over_threshold: 20000000.00
  vat_on_excess: 3600000.00
```

## Sources

| Source | URL | as_of |
|---|---|---|
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
