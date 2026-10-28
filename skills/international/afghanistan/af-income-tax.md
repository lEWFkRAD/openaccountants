---
name: af-income-tax
description: "Source-cited draft: personal income tax for Afghanistan (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AF
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Afghanistan Personal Income Tax

## Personal income tax — monthly salary brackets

- **Monthly salary 0 – 5,000 AFN** — 0% percent  _(Income Tax Law 2009)_
- **Monthly salary 5,001 – 12,500 AFN** — 2% of the amount over 5,000 AFN percent  _(Income Tax Law 2009)_
- **Monthly salary 12,501 – 100,000 AFN** — 10% of the amount over 12,500 AFN, plus 150 AFN percent  _(Income Tax Law 2009)_
- **Monthly salary over 100,000 AFN** — 20% of the amount over 100,000 AFN, plus 8,900 AFN percent  _(Income Tax Law 2009)_
- **Effective monthly tax-free threshold** — 5,000 AFN per month (≈ 60,000 AFN per year) AFN  _(Income Tax Law 2009)_
- **Residence test** — Individual domiciled in Afghanistan, OR present in Afghanistan for 183 days or more in the tax year, OR a government employee posted abroad  _(Income Tax Law 2009)_
- **Resident income scope** — Worldwide income (with foreign tax credit relief where applicable)  _(Income Tax Law 2009)_
- **Non-resident income scope** — Afghan-source income only  _(Income Tax Law 2009)_
- **Individual business / sole-proprietor income tax** — Taxed under the general income tax at progressive natural-person rates up to 20%, plus applicable BRT on turnover ((approx — confirm interaction of fixed/small-business tax regimes))  _(Income Tax Law 2009)_
- **Annual return filing deadline** — Within 3 months after the tax year-end ((approx — confirm))  _(Income Tax Law 2009)_
- **Collection of salary tax** — Withheld at source monthly by the employer and remitted to ARD (PAYE-equivalent)  _(Income Tax Law 2009)_

Salary income tax is computed monthly under the Income Tax Law 2009 using a low-banded progressive schedule that effectively exempts low earners. The same schedule applies to residents; non-residents are taxed only on Afghan-source income.

## Recomputing examples

```oa-check
name: AF monthly salary tax on 50,000 AFN
inputs:
  salary: 50000
steps:
  - band2: (min(salary, 12500) - 5000) * 0.02
  - band3: (min(salary, 100000) - 12500) * 0.10
  - fixed: 150
  - tax: band2 + fixed + band3
expected:
  band2: 150.00
  band3: 3750.00
  tax: 4050.00
```
```oa-check
name: AF monthly salary tax on 150,000 AFN (top band)
inputs:
  salary: 150000
steps:
  - top: (salary - 100000) * 0.20
  - tax: top + 8900
expected:
  top: 10000.00
  tax: 18900.00
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

- Income Tax Law 2009 (Afghanistan), salary tax brackets — https://ard.gov.af/

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
