---
name: Jamaica cross-border tax and nonresident withholding
description: Use when a Jamaica payer, investor, lender, licensor, service provider, branch, or adviser needs the 2026 nonresident withholding, treaty, permanent-establishment, or outbound-payment rules.
jurisdiction: JM
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Jamaica cross-border tax and nonresident withholding

## 1. Who this applies to

Use this guide for Jamaica-source payments to nonresidents, foreign companies operating in Jamaica, Jamaica companies paying dividends, interest, royalties, management or technical fees abroad, and payers claiming treaty relief. Identify the beneficial recipient and payment character before applying a rate.

## 2. Headline domestic withholding rates

For a corporate payer, the standard domestic rates reflected in the Income Tax Act and TAJ nonresident guidance are:

| Payment to nonresident | Headline rate before treaty relief |
|---|---:|
| Dividend | 15% |
| Interest | 25% |
| Royalty | 25% |
| Management or technical service fee | 25% |

Different rules can apply to individuals, specific exempt recipients, securities, approved arrangements or permanent establishments. A treaty can reduce a rate only when the recipient, beneficial ownership and procedural conditions are satisfied.

## 3. Source, base and permanent establishment

Withholding generally applies to the gross covered payment. Characterize bundled technology and service contracts from the rights and work actually supplied. Determine whether a foreign enterprise has a Jamaica permanent establishment under the Act and any applicable treaty; if so, attributable business profits may be taxed on a net basis in addition to payment-level compliance.

## 4. Withholding, returns and deadlines

Deduct at the statutory payment/credit trigger, remit through the TAJ-prescribed process and provide evidence to the recipient. Use the current TAJ calendar and form for the payment month. The official income-tax landing page links TAJ's nonresident guidance, but live return identifiers and portal steps can change.

**Source status:** headline rates and statutory categories are verified. The exact 2026 form identifier and electronic remittance workflow are `needs-sources` until checked in the live TAJ system.

## 5. Penalties and interest

Failure to deduct or remit can leave the payer liable for the tax, interest and penalties. Keep the contract, invoice, characterization, beneficial-owner and residence evidence, treaty analysis, calculation, return and payment receipt.

**AUDIT FLASH POINT** — Treaty relief is not automatic. A foreign address or certificate of incorporation does not by itself establish treaty residence or beneficial ownership.

## 6. Treaty and transfer-pricing coordination

Read the treaty article for dividends, interest, royalties, business profits and permanent establishment separately. Apply limitation and procedural requirements, retain a current residence certificate, and document beneficial ownership.

Connected-party amounts must also satisfy Jamaica's transfer-pricing rules. Withholding on the gross payment does not protect an excessive deduction, and a transfer-pricing adjustment does not automatically refund withholding.

## 7. Worked example — interest

A Jamaica company credits JMD 2,000,000 interest to a nonresident company. Before treaty relief, 25% withholding is JMD 500,000.

```oa-check
name: jamaica nonresident interest withholding
inputs:
  interest: 2000000
  rate: 0.25
steps:
  - withholding: interest * rate
expected:
  withholding: 500000.00
```

## 8. Worked example — royalty

A Jamaica payer owes JMD 750,000 for foreign IP rights. Before treaty relief, 25% withholding is JMD 187,500.

```oa-check
name: jamaica nonresident royalty withholding
inputs:
  royalty: 750000
  rate: 0.25
steps:
  - withholding: royalty * rate
expected:
  withholding: 187500.00
```

## 9. Ask the client first

1. Who is the legal and beneficial recipient, and where is it treaty-resident?
2. What does the contract provide: debt, IP, services, equipment, data access or several elements?
3. Is the recipient connected to the payer?
4. Does the recipient have people, premises, agents or a project in Jamaica?
5. What treaty article and documentation support any reduced rate?
6. Which TAJ return and due date apply for the payment month?

## 10. Sources

- [TAJ — income tax](https://www.jamaicatax.gov.jm/income-tax) — official nonresident and income-tax guidance access point; accessed 2026-10-24.
- [Laws of Jamaica — Income Tax Act](https://lipj.gov.jm/record/92036) — primary charging, withholding, permanent-establishment and treaty provisions; accessed 2026-10-24.
- [Laws of Jamaica information portal](https://lipj.gov.jm/) — official consolidated Acts and amendments; accessed 2026-10-24.
- [TAJ — transfer pricing](https://www.jamaicatax.gov.jm/transfer-pricing) — connected-party coordination; accessed 2026-10-24.
- [TAJ — tax bulletins](https://www.jamaicatax.gov.jm/tax-bulletins) — current administrative bulletins; accessed 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
