---
name: kn-income-tax-companies
description: >
  Saint Kitts and Nevis corporate income tax reference for 2026. Covers the
  33% company rate (38% banks and insurance), the short-term capital-gain
  rule, quarterly instalments, filing deadlines, penalties and interest, and
  the associated-persons adjustment power. Uses the official Law Commission
  consolidation of the Income Tax Act (Cap. 18.22). Post-2017 Finance Act
  reconciliation and accountant review remain open; source-cited draft.
jurisdiction: KN
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Saint Kitts and Nevis corporate income tax

## 1. Scope and sources

Source-cited draft checked 22 October 2026 from the Income Tax Act, Cap. 18.22 (official consolidation, revision date 31 December 2017) and the Tax Administration and Procedures Act, Cap. 20.52, both read in full from the Law Commission site. Amounts are East Caribbean dollars. **Caveat: not a complete post-2017 amendment audit — re-check rates against the current Finance Act before filing.**

## 2. Who is charged

Every company (and unincorporated body) is charged on its gains and profits, wherever arising where resident/controlled in the Federation, and on Federation-source profits where not. A company's year of income follows its accounting year.

## 3. Rates

| Source | All rates below | [Income Tax Act, Cap. 18.22](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_22-Income-Tax-Act.pdf) |
|---|---:|---|
| Companies (general) | 33% | |
| Banks and insurance companies | 38% | |
| Short-term capital gains (asset disposed of within one year of acquisition, s.4(2)) | half the applicable rate, capped at 20% | |

## 4. Base

Taxable profits are computed under the Act's schedules: trade/profession gains, employment, rents, investment income. Losses carry forward within the same trade (s.13). Hotel and pioneer-industry incentives (tax holidays) exist in Part III — verify current status per project before applying.

## 5. Deadlines

- Annual return: file within the period the Act sets for the year of income (by 30 April where the year of income ends 31 December; verify per fiscal year).
- **Instalments** (s.67): four quarterly payments on 15 March, 15 June, 15 September and 15 December, each one quarter of the estimated tax.
- Assessed tax is due within one month of the notice of assessment (s.66).

## 6. Penalties and interest

Tax Administration and Procedures Act, Cap. 20.52:

- Late filing: 5% of tax owing plus EC$100 per month (or part) of continuing failure (s.37).
- Underpayment from fraud or negligence: 25% of the underpayment (s.38).
- Interest on unpaid tax: 12% per annum from due date to payment (s.22).
- Directors are personally liable for unpaid company tax and withheld amounts (s.39).

## 7. Cross-border points

- Branch profits of non-resident companies are taxed at the company rate; there is no separate branch-profits tax.
- Associated-persons adjustments: see `kn-transfer-pricing`.
- Unilateral double-taxation relief only (Double Taxation (Relief) Act, Cap. 18.26, and the DTA Orders scheduled to the Income Tax Act — Canada, Denmark, New Zealand, Norway, Sweden, UK, Switzerland, USA, Monaco, San Marino; verify which Orders are actually in force before claiming).

## 8. Worked examples

**Example 1 — resident trading company, EC$250,000 taxable profit.**
Tax at 33% = 82,500. Each quarterly instalment is one quarter of the estimate: 20,625.00.

```oa-check
name: Company profit EC$250,000
inputs:
  profit: 250000
steps:
  - tax: profit * 0.33
  - instalment: tax / 4
expected:
  tax: 82500.00
  instalment: 20625.00
```

**Example 2 — company sells a warehouse EC$180,000 profit, bought 8 months earlier.**
The gain falls in s.4(2): half the company rate = 16.5%, below the 20% cap. Tax = 180,000 × 16.5% = 29,700.00.

```oa-check
name: Short-term gain EC$180,000
inputs:
  gain: 180000
steps:
  - rate: 0.33 / 2
  - capped_rate: min(rate, 0.20)
  - tax: gain * capped_rate
expected:
  tax: 29700.00
```

## 9. Ask the client first

1. Is the entity a bank or insurance company (38%)?
2. Accounting year-end and whether instalments were estimated correctly.
3. Any hotel/pioneer-incentive grant in force.
4. Any asset bought and resold within twelve months.

## 10. Sources

- [Income Tax Act, Cap. 18.22](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-18_22-Income-Tax-Act.pdf) — read 2026-10-22.
- [Tax Administration and Procedures Act, Cap. 20.52](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-20_52-Tax-Administration-and-Procedures-Act.pdf) — read 2026-10-22.
