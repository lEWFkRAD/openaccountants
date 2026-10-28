---
name: af-vat-gst
description: "Source-cited draft: vat / gst for Afghanistan (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AF
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Afghanistan VAT / GST

## VAT status and Business Receipts Tax

Afghanistan has enacted a VAT Law but, as of 2025, its commencement has been repeatedly postponed and it is not generally operational. In practice the consumption-type levy in force is the Business Receipts Tax (BRT), a tax on gross turnover with no input-credit mechanism.

- **Operational VAT** — No general VAT is currently operational; the VAT Law's entry into force has been deferred ((approx — confirm current commencement status with ARD))  _(Value Added Tax Law (not yet in force))_
- **Legislated VAT standard rate (when in force)** — 10 percent  _(Value Added Tax Law)_
- **Legislated VAT registration threshold** — 150,000,000 AFN annual turnover ((approx — confirm; applies only when VAT commences))  _(Value Added Tax Law)_
- **Business Receipts Tax — general rate** — 4% of gross receipts percent  _(Income Tax Law 2009)_
- **BRT — small restaurants** — 2% of gross receipts percent ((approx — confirm sector classification))  _(Income Tax Law 2009)_
- **BRT — hotels, large restaurants, club halls** — 5% of gross receipts percent  _(Income Tax Law 2009)_
- **BRT — telecom / airlines** — 5% of gross receipts (incl. telecom services fee components where applicable) percent ((approx — confirm))  _(Income Tax Law 2009)_
- **BRT tax base** — Total gross receipts (sales) before any deduction; no input credit  _(Income Tax Law 2009)_
- **BRT filing / payment frequency** — Quarterly  _([Income Tax Law 2009](https://ard.gov.af/820/quarterly-business-receipts-tax-brt-user-guides))_
- **Reverse charge** — Not applicable while VAT is not operational; BRT has no reverse-charge mechanism  _(Income Tax Law 2009)_

## Recomputing examples

```oa-check
name: AF BRT general 4% on 1,000,000 AFN gross receipts
inputs:
  receipts: 1000000
steps:
  - brt: receipts * 0.04
expected:
  brt: 40000.00
```
```oa-check
name: AF BRT hotels/large restaurants 5% on 2,000,000 AFN vs small restaurant 2%
inputs:
  hotel: 2000000
  restaurant: 2000000
steps:
  - hotel_brt: hotel * 0.05
  - restaurant_brt: restaurant * 0.02
expected:
  hotel_brt: 100000.00
  restaurant_brt: 40000.00
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

- Income Tax Law 2009 (Afghanistan), Business Receipts Tax — https://ard.gov.af/820/quarterly-business-receipts-tax-brt-user-guides
- Value Added Tax Law (Afghanistan, not yet in force)

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
