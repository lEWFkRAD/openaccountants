---
name: af-corporate-income-tax
description: "Source-cited draft: corporate income tax for Afghanistan (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AF
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Afghanistan Corporate Income Tax

## Corporate income tax

Afghan companies and other legal persons pay a flat 20% corporate income tax on taxable profit under the Income Tax Law 2009, in addition to the Business Receipts Tax levied on gross turnover. Withholding obligations apply to dividends, interest, royalties, rent and contractor payments.

- **Corporate income tax rate** — 20% percent (flat)  _(Income Tax Law 2009)_
- **Rate applies to** — All corporations and limited-liability companies regardless of size or sector  _(Income Tax Law 2009)_
- **Tax base** — Net taxable income (gross income less allowable business deductions)  _(Income Tax Law 2009)_
- **Business Receipts Tax (separate from CIT)** — Levied on gross receipts before deductions; 4% general, 2% / 5% for certain sectors percent  _(Income Tax Law 2009)_
- **Withholding tax on dividends** — 20% percent ((approx — confirm current rate))  _(Income Tax Law 2009)_
- **Withholding tax on interest** — 20% percent ((approx — confirm current rate))  _(Income Tax Law 2009)_
- **Withholding tax on royalties** — 20% percent ((approx — confirm current rate))  _(Income Tax Law 2009)_
- **Withholding on contractor payments (licensed firm)** — 2% of the gross contract payment percent  _(Income Tax Law 2009)_
- **Withholding on contractor payments (no business licence)** — 7% of the gross contract payment percent  _(Income Tax Law 2009)_
- **Withholding tax on rent** — 20% where monthly rent exceeds 15,000 AFN (10% for lower amounts) percent ((approx — confirm tiers))  _(Income Tax Law 2009)_
- **Loss carry-forward** — Trading losses may be carried forward (commonly up to 3 years) ((approx — confirm carry-forward period))  _(Income Tax Law 2009)_
- **Corporate return filing deadline** — Within 3 months after the end of the tax year ((approx — confirm))  _(Income Tax Law 2009)_
- **Corporate tax payment** — Balance due with the annual return; BRT paid quarterly  _(Income Tax Law 2009)_

## Recomputing examples

```oa-check
name: AF CIT on 1,000,000 AFN taxable profit at flat 20%
inputs:
  profit: 1000000
steps:
  - tax: profit * 0.20
expected:
  tax: 200000.00
```
```oa-check
name: AF contractor withholding: 500,000 AFN licensed (2%) vs unlicensed (7%)
inputs:
  contract: 500000
steps:
  - licensed: contract * 0.02
  - unlicensed: contract * 0.07
expected:
  licensed: 10000.00
  unlicensed: 35000.00
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

- Income Tax Law 2009 (Afghanistan), corporate income tax and withholding — https://ard.gov.af/

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
