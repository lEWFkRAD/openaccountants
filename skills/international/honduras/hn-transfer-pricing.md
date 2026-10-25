---
name: Honduras transfer pricing
description: Use when a Honduras taxpayer has related-party or special-regime transactions and needs the 2026 arm's-length, documentation, filing, adjustment, or penalty rules.
jurisdiction: HN
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Honduras transfer pricing

## 1. Who this applies to

Honduras applies the arm's-length principle to commercial and financial operations between related persons, whether domestic or foreign, and to operations with persons benefiting from special customs or tax regimes. Agreement 027-2015 also reaches restructurings that move functions, assets or risks when the recorded values are not market values.

Related-party analysis is not limited to share ownership. Review direct and indirect management, control, capital, common control, contractual dependence and transactions with special-regime beneficiaries.

## 2. Core rules and rates

| Rule | 2026 treatment | Primary authority |
|---|---|---|
| Pricing standard | Price or margin that independent parties would have agreed in comparable conditions | Law 232-2011; Agreement 027-2015 arts. 10, 18-23 |
| Annual informative return | Calendar-year taxpayers: 1 January through 30 April (or next business day); special fiscal years: within three months after close | Agreement 027-2015 art. 31 |
| Missing/false/incomplete requested information | USD 10,000 equivalent in lempiras | Agreement 027-2015 arts. 35-36 |
| Understated base from non-arm's-length pricing | 15% of the tax-authority adjustment | Agreement 027-2015 art. 36 |
| Adjustment plus information failure | 30% of adjustment or USD 20,000 equivalent, whichever is greater | Agreement 027-2015 art. 36 |
| Other breach | USD 5,000 equivalent in lempiras | Agreement 027-2015 art. 36 |

The informative-return population includes medium and large taxpayers with related-party dealings, taxpayers dealing with special-regime beneficiaries, taxpayers dealing with related parties in tax havens, and other taxpayers whose annual related-party amount exceeds a threshold fixed by general agreement. Confirm the currently operative SAR threshold and taxpayer classification before filing.

## 3. Tax base, methods and comparability

Test each controlled transaction by reference to functions, assets, risks, contractual terms, economic circumstances and business strategies. The regulation implements the methods in Article 8 of Law 232-2011, including comparable uncontrolled price, resale price, cost plus, profit split and transactional net margin methods. Select and document the method that gives the most reliable arm's-length result; do not choose a method solely because it gives the lowest adjustment.

The study must quantify controlled transactions, identify counterparties and comparables, state sources, explain comparability adjustments, show the arm's-length range and reconcile any tax adjustment.

## 4. Documentation and filing deadlines

Maintain the analysis and underlying evidence when the transaction is booked. Article 29 requires sufficient information and an accompanying transfer-pricing study, with all supporting material available to SAR. Supply the study when requested within the period then applicable under the Tax Code.

For calendar-year taxpayers, file the annual informative return between 1 January and 30 April of the following year (next business day if required). A special-year taxpayer files within three months after its close. Confirm the live SAR form, schema and submission channel before filing.

## 5. Adjustments, penalties and interest

SAR may make a primary adjustment if the taxpayer cannot substantiate normal market prices, values or profitability. The specific transfer-pricing penalties in Article 36 apply in addition to ordinary assessment, collection and interest rules under the Tax Code. Preserve proof of the exchange rate used when a USD-denominated fine is paid in lempiras.

**AUDIT FLASH POINT** — Special-regime transactions are expressly within scope even when both parties are in Honduras. A domestic label does not remove the documentation duty.

## 6. Cross-border coordination

Reconcile the transfer-pricing result with nonresident withholding under Income Tax Law Article 5. A payment can be arm's length and still carry withholding; conversely, withholding does not prove that the deductible amount is arm's length. For outbound financing, also document beneficial ownership, use of funds, currency, guarantees, maturity and comparable credit terms.

Before claiming treaty relief or a foreign corresponding adjustment, verify the specific instrument, residence certificate, beneficial-owner facts and procedure in force for the year.

## 7. Worked example — understated sale price

A Honduras company sells goods to an affiliate for HNL 1,400,000. The documented arm's-length amount is HNL 2,000,000. The preliminary upward adjustment is HNL 600,000 before tax-rate and penalty effects.

```oa-check
name: honduras related-party sale uplift
inputs:
  arm_length_price: 2000000
  recorded_price: 1400000
steps:
  - adjustment: arm_length_price - recorded_price
expected:
  adjustment: 600000.00
```

## 8. Worked example — excess related-party interest

A HNL 5,000,000 affiliate loan bears 12%, while the supported arm's-length rate is 8%. The excess annual interest is HNL 200,000, subject to final factual and legal review.

```oa-check
name: honduras excess related-party interest
inputs:
  principal: 5000000
  charged_rate: 0.12
  arm_length_rate: 0.08
steps:
  - charged_interest: principal * charged_rate
  - arm_length_interest: principal * arm_length_rate
  - excess_interest: charged_interest - arm_length_interest
expected:
  excess_interest: 200000.00
```

## 9. Ask the client first

1. Which domestic, foreign, tax-haven or special-regime counterparties were related during the year?
2. What goods, services, royalties, loans, guarantees or restructurings occurred, and at what values?
3. Is the taxpayer classified by SAR as medium or large, and does a current general agreement impose a filing threshold?
4. Is the study contemporaneous, and do invoices, contracts, ledgers and withholding receipts reconcile to it?
5. Did any payment also trigger Article 5 nonresident withholding or a treaty claim?

## 10. Sources

- [Agreement 027-2015, Regulation of the Transfer Pricing Law (SAR-hosted official-gazette file)](https://www.sar.gob.hn/download/acuerdo-027-2015/) — arts. 2, 10-11, 18-23 and 29-40; accessed 2026-10-24.
- [SAR — legal library](https://www.sar.gob.hn/download-category/otras-leyes/) — official tax-law access point; accessed 2026-10-24.
- [SAR — Income Tax Law and amendments](https://www.sar.gob.hn/download/consolidado-ley-impuesto-sobre-la-renta-25-junio-2018/) — cross-border coordination; accessed 2026-10-24.
- [SAR — home](https://www.sar.gob.hn/) — filing-channel check; accessed 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
