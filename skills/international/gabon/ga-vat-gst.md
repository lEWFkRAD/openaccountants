---
name: ga-vat-gst
description: "Source-cited draft: vat / gst for Gabon (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: GA
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gabon VAT / GST

## Value-added tax (TVA)

- **Standard VAT rate** — 18 %  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **Reduced VAT rate** — 10 % (on certain specified products)  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **Lower reduced VAT rate** — 5 % (on certain specified products)  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **Zero-rated supplies** — 0 % (on exports, international transport, and aircraft/ship operations in international traffic)  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **VAT registration threshold** — 60,000,000 XAF (Annual turnover (excl. tax) reaching XAF 60,000,000)  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **VAT on construction / property sales** — 18 % (on construction and property sales by VAT-registered persons)  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **VAT filing frequency** — Monthly returns, generally due by the 20th of the following month ((approx — confirm exact due day))  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **Reverse charge on imported services** — VAT on services supplied by non-established providers is self-accounted by the Gabonese recipient (reverse charge) ((approx — confirm mechanics))  _(Code Général des Impôts (Gabon) — TVA — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **Special Solidarity Contribution (CSS)** — 1 % (on businesses with annual turnover of XAF 30,000,000 or more)  _(Code Général des Impôts (Gabon) — Contribution Spéciale de Solidarité — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_
- **Excise duties** — 5%–40% % (on luxury goods (alcohol, tobacco, cosmetics))  _(Code Général des Impôts (Gabon) — droits d'accise — https://taxsummaries.pwc.com/gabon/corporate/other-taxes)_

Gabon operates a CEMAC-aligned VAT (Taxe sur la Valeur Ajoutée) with a standard 18% rate and reduced/zero categories. Rates, threshold and filing notes below are a 2025 draft pending accountant verification.

## Recomputing examples

```oa-check
name: GA VAT 18% vs reduced 10% vs 5% on 10,000,000 XAF
inputs:
  supply: 10000000
steps:
  - std: supply * 0.18
  - mid: supply * 0.10
  - low: supply * 0.05
expected:
  std: 1800000.00
  mid: 1000000.00
  low: 500000.00
```
```oa-check
name: GA CSS 1% on 100,000,000 XAF turnover (threshold XAF 30,000,000)
inputs:
  turnover: 100000000
steps:
  - css: turnover * 0.01
expected:
  css: 1000000.00
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

- Code Général des Impôts (Gabon), TVA
- Code Général des Impôts (Gabon), Contribution Spéciale de Solidarité
- Code Général des Impôts (Gabon), droits d'accise

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
