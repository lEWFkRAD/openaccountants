---
name: ga-corporate-income-tax
description: "Source-cited draft: corporate income tax for Gabon (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: GA
version: "0.2"
tax_year: 2025
last_updated: 2026-10-28
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Gabon Corporate Income Tax

## Corporate income tax (Impôt sur les Sociétés)

- **Overview** — Companies operating in Gabon are subject to the Impôt sur les Sociétés (IS) on Gabon-source profits, with minimum-tax floors and instalment payments. Rates and deadlines below are a 2025 draft for accountant review.
- **Standard CIT rate** — 30% %  _(Code Général des Impôts (Gabon) — Impôt sur les Sociétés (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **CIT rate — oil and mining sectors** — 35% %  _(Code Général des Impôts (Gabon) — Impôt sur les Sociétés (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **Tax base** — Taxable profit = revenues less deductible expenses and charges, including capital gains on fixed assets  _(Code Général des Impôts (Gabon) — Impôt sur les Sociétés (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **Corporate residence / territoriality** — Companies operating or conducting operations in Gabon are subject to IS on Gabon-source profits  _(Code Général des Impôts (Gabon) — Impôt sur les Sociétés (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **Impôt Minimum Forfaitaire (IMF)** — 1% of annual global turnover of the fiscal year %  _(Code Général des Impôts (Gabon) — IMF (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **Minimum de Perception (CIT floor)** — XAF 500,000 — CIT cannot fall below this, even with no profit XAF ((approx — confirm; some sources cite XAF 1,000,000)) XAF  _(Code Général des Impôts (Gabon) — Minimum de Perception (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **Minimum-tax relief — new/SME companies** — New companies and CIT-exempt entities relieved from minimum taxes; SMEs receive a three-year exemption  _(Code Général des Impôts (Gabon) (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **Withholding tax on dividends (non-treaty)** — 20% %  _(Code Général des Impôts (Gabon) — IRCM/WHT (https://taxsummaries.pwc.com/gabon/corporate/withholding-taxes))_
- **Withholding tax on interest (non-treaty)** — 20% %  _(Code Général des Impôts (Gabon) — WHT (https://taxsummaries.pwc.com/gabon/corporate/withholding-taxes))_
- **Withholding tax on royalties / service fees (non-treaty)** — 25% %  _(Code Général des Impôts (Gabon) — WHT (https://taxsummaries.pwc.com/gabon/corporate/withholding-taxes))_
- **Withholding on non-resident companies without a PE** — 25% withholding in lieu of CIT %  _(Code Général des Impôts (Gabon) (https://taxsummaries.pwc.com/gabon/corporate/taxes-on-corporate-income))_
- **Annual CIT return filing deadline** — Before 30 April of the following year  _(Code Général des Impôts (Gabon) (https://taxsummaries.pwc.com/gabon/corporate/tax-administration))_
- **First CIT instalment** — 25% of prior year's tax, due 30 November  _(Code Général des Impôts (Gabon) (https://taxsummaries.pwc.com/gabon/corporate/tax-administration))_
- **Second CIT instalment** — 33% of prior year's tax, due 30 January  _(Code Général des Impôts (Gabon) (https://taxsummaries.pwc.com/gabon/corporate/tax-administration))_
- **Final CIT balance** — Balance due with the return by 30 April  _(Code Général des Impôts (Gabon) (https://taxsummaries.pwc.com/gabon/corporate/tax-administration))_

## Recomputing examples

```oa-check
name: GA CIT 30% standard vs 35% oil/mining on 100,000,000 XAF profit
inputs:
  profit: 100000000
steps:
  - standard: profit * 0.30
  - oil: profit * 0.35
  - diff: oil - standard
expected:
  standard: 30000000.00
  oil: 35000000.00
  diff: 5000000.00
```
```oa-check
name: GA WHT on 1,000,000 XAF: dividends/interest 20%, royalties 25%
inputs:
  payment: 1000000
steps:
  - div: payment * 0.20
  - roy: payment * 0.25
expected:
  div: 200000.00
  roy: 250000.00
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

- Code Général des Impôts (Gabon), Impôt sur les Sociétés
- Code Général des Impôts (Gabon), IRCM/WHT
- Code Général des Impôts (Gabon), Minimum de Perception

_Sources listed from citations already present in the guide; as_of: 2026-10-28; unverified against archived evidence._
