---
name: bz-vat-gst
description: "Source-cited draft: vat / gst for Belize (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BZ
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belize VAT / GST

## General Sales Tax (GST)

- **Standard GST rate** — 12.5 percent  _(General Sales Tax Act (https://bts.gov.bz/gst-faq/))_
- **Zero-rated supplies** — Exports, certain basic foods, medicines and other prescribed items are zero-rated (approx — confirm zero-rated schedule)  _(General Sales Tax Act)_
- **Exempt supplies** — Certain financial, educational and other prescribed services are exempt (no input credit) (approx — confirm exempt schedule)  _(General Sales Tax Act)_
- **Registration threshold** — 75,000 BZD  _(General Sales Tax Act (https://beltraide.bz/belize-invest/doing-business-in-belize/general-sales-tax-registration/))_
- **Registration threshold — new business proxy** — Averaging BZD 6,250 per month in taxable supplies (business under 12 months old) BZD (approx — confirm)  _(General Sales Tax Act)_
- **Filing frequency** — Monthly GST returns (Form BTS210)  _(General Sales Tax Act (https://bts.gov.bz/file-gst-return/))_
- **Return / payment deadline** — By the 15th of the month following the tax period  _(General Sales Tax Act (https://bts.gov.bz/file-gst-return/))_
- **Input tax credit** — Registered businesses credit GST paid on inputs against GST charged on outputs (net remittance)  _(General Sales Tax Act)_
- **Reverse charge / imported services** — GST applies to imports; place-of-supply and reverse-charge style rules apply to certain imported services (approx — confirm imported-services treatment)  _(General Sales Tax Act)_
- **E-invoicing developments** — Belize is progressing toward a B2B e-invoicing mandate (approx — confirm status/timeline)  _(General Sales Tax Act)_

## Worked examples

```oa-check
name: BZ GST registration threshold test at BZD 90,000 turnover
inputs:
  turnover: 90000
  threshold: 75000
steps:
  - over_threshold: turnover - threshold
  - must_register: (turnover - threshold) / (threshold) * 0 + 1
expected:
  over_threshold: 15000.00
  must_register: 1.00
```

```oa-check
name: BZ GST net remittance, output 12.5% on 40,000 less input on 15,000
inputs:
  sales: 40000
  inputs: 15000
steps:
  - output: sales * 0.125
  - input_credit: inputs * 0.125
  - payable: output - input_credit
expected:
  output: 5000.00
  input_credit: 1875.00
  payable: 3125.00
```

## Sources

| Source | URL | as_of |
|---|---|---|
| General Sales Tax Act — BTS GST FAQ (cited inline) | https://bts.gov.bz/gst-faq/ | 2026-10-28 |
| GST registration — BELTRAIDE (cited inline) | https://beltraide.bz/belize-invest/doing-business-in-belize/general-sales-tax-registration/ | 2026-10-28 |
| Form BTS210 monthly GST return — BTS (cited inline) | https://bts.gov.bz/file-gst-return/ | 2026-10-28 |

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
