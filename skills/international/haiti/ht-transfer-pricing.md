---
name: Haiti transfer pricing
description: Use when a Haiti entity has related-party or preferential-regime transactions and needs the 2026 arm's-length, documentation, filing, audit, or penalty rules.
jurisdiction: HT
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Haiti transfer pricing

## 1. Who this applies to

Articles 77-80 of Haiti's 2026 Code Général des Impôts apply to indirect profit transfers between related entities in Haiti or abroad and to transfers to an entity in a foreign state or territory with a preferential tax regime. Relatedness includes direct or indirect majority control, de facto decision power, common control and specified economic dependence.

The express documentation population includes taxpayers handled by the large-taxpayer directorate or the directorate for exempt organizations and enterprises, and Haiti entities controlling or controlled by such an entity by more than half of capital or voting rights. DGI can request information from other taxpayers when an audit indicates a possible indirect profit transfer.

## 2. Core rules and thresholds

| Rule | 2026 treatment | Authority |
|---|---|---|
| Pricing standard | Price independent entities would use in similar market conditions | CGI art. 77 |
| Preferential regime | Foreign tax is less than half the Haiti ordinary tax that would apply to a Haiti resident | CGI art. 79 |
| Documentation language | Creole or French | CGI art. 80 |
| Electronic file availability | Within three months after filing the results return | CGI art. 424 |
| Simplified declaration | Filed with financial statements; nature/amount, counterparty identity and pricing method | CGI art. 80(2) |
| Response after audit notice | 30 clear days for missing/incomplete documentation | CGI art. 425 |
| Information request for taxpayer outside mandatory file population | At least 60 days, extendable on reasoned request to no more than 90 days total | CGI art. 426 |

## 3. Base and arm's-length analysis

Article 77 requires taxable profit to be increased for benefits indirectly transferred through inflated or reduced purchase or sale prices or any other means. Examples include excessive or unsupported royalties, interest-free or off-market loans, debt waivers and benefits disproportionate to services.

Prepare a transaction-by-transaction file: legal relationship, contracts, functions, assets, risks, market circumstances, tested party, method, comparables, adjustments and the resulting arm's-length price or margin. A label such as “management fee” does not replace proof of services and benefit.

## 4. Documentation and deadlines

The Article 80 taxpayer must keep an electronic file available no later than three months after the results return is filed. The simplified declaration accompanies the financial statements and identifies the nature and amount of related transactions, each related entity's name and registered office, and the method used.

At the start of an audit or accounting examination, present the file to the auditor. If it is missing or partial, Article 425 provides a 30-clear-day cure notice. Verify the ministerial form for the simplified declaration and the DGI electronic format before submission.

**Source status:** the Code itself is verified. The ministerial form and 2026 DGI electronic schema are `needs-sources` until officially published or located.

## 5. Adjustments, penalties and interest

After an unanswered or incomplete cure notice, Article 425 authorizes a fine up to 1% of the transactions concerned or, when an assessment is made and the amount is higher, a 10% surcharge on the assessed duties. Compulsory assessment can also follow under Article 440. Article 426 provides parallel consequences for a taxpayer outside the mandatory documentation population that fails an audit information request.

Ordinary late-declaration and late-payment additions under Articles 474-476 can apply to the resulting tax. Preserve the notice date and count clear days carefully.

**AUDIT FLASH POINT** — The 2026 Code was newly published on 30 September 2026. Confirm commencement and transition rules for the tested fiscal period rather than assuming every new procedure applies retroactively.

## 6. Cross-border coordination

Article 77 covers related entities both inside and outside Haiti and separately covers preferential-regime entities. Coordinate any pricing adjustment with withholding under Articles 97, 116 and 121 and with foreign relief. A deduction allowed at arm's length can still carry withholding; withholding does not validate the amount as arm's length.

## 7. Worked example — understated related-party sale

A Haiti entity records a sale to a related enterprise at HTG 16,000,000. Comparable evidence supports HTG 20,000,000. The preliminary upward adjustment is HTG 4,000,000.

```oa-check
name: haiti related-party sale uplift
inputs:
  arm_length_price: 20000000
  recorded_price: 16000000
steps:
  - adjustment: arm_length_price - recorded_price
expected:
  adjustment: 4000000.00
```

## 8. Worked example — maximum 1% documentation fine base

If transactions affected by missing documentation total HTG 100,000,000, the Article 425 1% limb has a maximum amount of HTG 1,000,000. Compare that with 10% of assessed duties if an assessment is made; the higher applicable limb governs.

```oa-check
name: haiti transfer-pricing documentation fine limb
inputs:
  affected_transactions: 100000000
  maximum_rate: 0.01
steps:
  - maximum_fine_limb: affected_transactions * maximum_rate
expected:
  maximum_fine_limb: 1000000.00
```

## 9. Ask the client first

1. Which entities share ownership, control, decision makers or economic dependence?
2. Is the taxpayer handled by DGC or DOEE, or controlled by/controlling such an entity?
3. Which transactions involve a preferential-regime jurisdiction under Article 79?
4. Were financial statements and the simplified declaration filed, and when does the three-month documentation period expire?
5. Has DGI issued an audit request or 30-day cure notice?

## 10. Sources

- [DGI — Code Général des Impôts, official PDF](https://dgi.gouv.ht/wp-content/uploads/2026/10/Code-Fiscal.pdf) — arts. 77-80, 424-426, 440 and 474-476; PDF returned official content and was opened 2026-10-24.
- [DGI — decree/code landing page](https://dgi.gouv.ht/dgi_doc/decret-remplacant-le-decret-du-19-decembre-2022-portant-le-code-fiscal/) — official publication context; accessed 2026-10-24.
- [DGI — home](https://dgi.gouv.ht/) — form and implementation check; accessed 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
