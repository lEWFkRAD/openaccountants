---
name: Jamaica transfer pricing
description: Use when a Jamaica taxpayer has connected-party transactions and needs the 2026 arm's-length, threshold, method, documentation, return, adjustment, or penalty rules.
jurisdiction: JM
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Jamaica transfer pricing

## 1. Who this applies to

Jamaica's transfer-pricing rules apply the arm's-length principle to transactions between connected persons. The rules generally apply where the taxpayer conducting a trade or business has annual gross revenue of JMD 500 million or more; do not net expenses or group entities when testing the entity's gross-revenue threshold. Separate statutory rules can preserve scope for specified transactions or anti-avoidance cases, so document the threshold conclusion rather than treating it as an informal safe harbour.

## 2. Core rules and threshold

| Rule | 2026 treatment | Primary source |
|---|---|---|
| Effective regime | Transfer-pricing rules effective from 1 January 2016 | Income Tax (Amendment) Act 2015; TAJ Transfer Pricing at a Glance |
| General gross-revenue threshold | JMD 500,000,000 | Income Tax (Amendment) (No. 2) Act 2017 |
| Standard | Conditions independent persons would have agreed in comparable circumstances | Income Tax Act Part 1A |
| Methods | Comparable uncontrolled price, resale price, cost plus, transactional net margin, profit split; use the most appropriate method | Income Tax Act/TAJ guidance |
| Documentation response | Maintain contemporaneous support and produce it within the statutory/TAJ request period | Income Tax Act; TAJ Transfer Pricing at a Glance |

Connected-person status can arise through control, ownership and relationships specified by the Act. Map direct and indirect ownership, common management, financing and economically significant contracts before deciding that a counterparty is independent.

## 3. Base, method and comparability

Identify the accurately delineated transaction and compare functions, assets, risks, product/service characteristics, contractual terms, economic conditions and business strategies. Select the most appropriate method based on reliable data and explain rejected methods. Reconcile the arm's-length result to the income tax return and related-party disclosures.

For services, prove receipt, benefit, allocation key and absence of shareholder or duplicate costs. For financing, document principal, currency, maturity, security, credit profile and comparable yield. For intangibles, identify legal ownership and the parties performing development, enhancement, maintenance, protection and exploitation functions.

## 4. Documentation and filing deadlines

Prepare the file by the time the return position is finalized; a report produced only after an audit notice is weak evidence even if delivered within the response period. Retain organization structure, transaction schedules, agreements, tested-party selection, searches, comparables, adjustments and financial reconciliation.

File the prescribed related-party information with the annual income tax return and follow the current TAJ due date for the taxpayer's year end. Confirm the current return/schedule and TAJ request deadline on the filing date.

**Source status:** the legal regime and JMD 500 million threshold are verified. The exact 2026 electronic schedule name and portal mechanics are `needs-sources` until checked in the live TAJ filing system.

## 5. Adjustments, penalties and interest

TAJ can replace the recorded conditions with arm's-length conditions and assess additional income tax, interest and applicable Income Tax Act penalties. General penalties can turn on negligence, gross negligence or fraud; do not quote an amount without checking the current assessment notice and operative provision.

**AUDIT FLASH POINT** — A taxpayer below the revenue threshold should retain the revenue test and connected-party map. Threshold evidence can itself become the first audit issue.

## 6. Cross-border coordination

Transfer pricing and withholding are separate. A 25% withholding on a royalty or management fee does not make the full expense arm's length. Likewise, an arm's-length amount can still require withholding. For treaty relief, confirm residence, beneficial ownership and the relevant article; for permanent establishments, attribute profits consistently with the Act and treaty.

## 7. Worked example — understated goods sale

A Jamaica company records a sale to a connected enterprise at JMD 12,000,000. Reliable comparable evidence supports JMD 15,000,000. The preliminary adjustment is JMD 3,000,000.

```oa-check
name: jamaica related-party goods sale uplift
inputs:
  arm_length_price: 15000000
  recorded_price: 12000000
steps:
  - adjustment: arm_length_price - recorded_price
expected:
  adjustment: 3000000.00
```

## 8. Worked example — excessive royalty

A Jamaica licensee deducts JMD 9,000,000, while the supported arm's-length royalty is JMD 7,000,000. The preliminary disallowance is JMD 2,000,000 before tax, interest and penalty effects.

```oa-check
name: jamaica excess connected-party royalty
inputs:
  royalty_deducted: 9000000
  arm_length_royalty: 7000000
steps:
  - preliminary_disallowance: royalty_deducted - arm_length_royalty
expected:
  preliminary_disallowance: 2000000.00
```

## 9. Ask the client first

1. Did the entity's annual gross revenue reach JMD 500 million, and how was it tested?
2. Which persons are connected under the Act, including indirect and common control?
3. What goods, services, loans, guarantees, intangibles or restructurings occurred?
4. Is a contemporaneous report reconciled to the return and withholding records?
5. Was treaty relief or a permanent-establishment position taken?

## 10. Sources

- [TAJ — transfer pricing](https://www.jamaicatax.gov.jm/transfer-pricing) — official overview and link to Transfer Pricing at a Glance; accessed 2026-10-24.
- [Laws of Jamaica — Income Tax Act](https://lipj.gov.jm/record/92036) — consolidated primary legislation, Part 1A; accessed through the official portal 2026-10-24.
- [Laws of Jamaica — Income Tax (Amendment) Act 2015](https://lipj.gov.jm/record/84689) — introduced the modern regime; accessed 2026-10-24.
- [Laws of Jamaica — Income Tax (Amendment) (No. 2) Act 2017](https://lipj.gov.jm/record/79043) — JMD 500 million gross-revenue threshold; accessed 2026-10-24.
- [TAJ — income tax](https://www.jamaicatax.gov.jm/income-tax) — return and filing guidance; accessed 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
