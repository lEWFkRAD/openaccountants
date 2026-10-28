---
name: bd-corporate-income-tax
description: "Source-cited draft: corporate income tax for Bangladesh (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: BD
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bangladesh Corporate Income Tax

## Corporate income tax rates

- **Non-publicly traded company** — 27.5% (25% if all receipts/payments above thresholds go through banking channels) percent  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025 — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **Publicly traded company (IPO float > 10% of paid-up capital)** — 20% (22.5% if banking-channel conditions not met) percent  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025 — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **Publicly traded company (IPO float <= 10% of paid-up capital)** — 22.5% (25% if banking-channel conditions not met) percent  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025 — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **Banks, insurance and financial institutions (non-listed)** — 40% (37.5% if publicly traded) percent ((listed rate approx — confirm))  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025 — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **Mobile phone operators** — 45% percent  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025 — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **Tobacco / cigarette manufacturers** — 45% plus 2.5% surcharge percent  _(Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025 — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_
- **Tax base** — Resident company taxed on worldwide income; non-resident company taxed on Bangladesh-source income  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/taxes-on-corporate-income)_

## Withholding taxes and filing

- **Dividend WHT — resident company recipient** — 20% percent ((approx — taxed at company rate; confirm))  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/withholding-taxes)_
- **Dividend WHT — resident individual** — 10% with e-TIN, 15% without e-TIN percent  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/withholding-taxes)_
- **Dividend WHT — non-resident** — 20% (company/fund/trust); 30% (other persons) percent (subject to reduction under an applicable tax treaty)  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/withholding-taxes)_
- **Interest WHT — resident** — 10% (20% on company/trust/AoP savings and fixed deposits) percent  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/withholding-taxes)_
- **Interest WHT — non-resident** — 20% percent (subject to reduction under an applicable tax treaty)  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/withholding-taxes)_
- **Royalty WHT — resident** — 10% percent  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/withholding-taxes)_
- **Royalty / technical service fee WHT — non-resident** — 20% percent (subject to reduction under an applicable tax treaty)  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/withholding-taxes)_
- **Company return filing deadline** — 15th day of the 7th month after income-year end, or 15 September (whichever is later) ((approx — described as around mid-September for July-June filers; confirm exact rule))  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/tax-administration)_
- **Advance tax installments** — Four quarterly installments: 15 Sep, 15 Dec, 15 Mar, 15 Jun (required where latest assessed income exceeds the prescribed limit)  _(Income Tax Act 2023 (Bangladesh) — https://taxsummaries.pwc.com/bangladesh/corporate/tax-administration)_

## Recomputing examples

```oa-check
name: BD non-listed company 1,000,000 BDT profit at 27.5% vs 25% banking-channel rate
inputs:
  profit: 1000000
steps:
  - standard: profit * 0.275
  - banking: profit * 0.25
  - saving: standard - banking
expected:
  standard: 275000.00
  banking: 250000.00
  saving: 25000.00
```
```oa-check
name: BD listed company 1,000,000 BDT profit at 20% vs 22.5%
inputs:
  profit: 1000000
steps:
  - low: profit * 0.20
  - high: profit * 0.225
expected:
  low: 200000.00
  high: 225000.00
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

- Income Tax Act 2023 (Bangladesh), as amended by Finance Ordinance 2025

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
