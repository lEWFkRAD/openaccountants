---
name: Haiti cross-border tax and withholding
description: Use when a Haiti payer, nonresident service provider, shareholder, lender, branch, or adviser needs the 2026 source, withholding, distribution, or cross-border compliance rules.
jurisdiction: HT
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Haiti cross-border tax and withholding

## 1. Who this applies to

Use this guide for Haiti-source payments to a person fiscally resident outside Haiti, distributions and interest, a nonresident company operating through a Haiti permanent establishment, and a Haiti payer responsible for withholding. Classify the payment and recipient before using a rate.

## 2. Verified statutory rates

| Payment | Headline rate | Payment timing | 2026 CGI |
|---|---:|---|---|
| Services paid by a Haiti resident to a beneficiary fiscally resident outside Haiti | 20%, final withholding | Between the 1st and 15th of the month after payment | Art. 97 |
| Distributed income under Article 114 | 20%, final withholding | Between the 1st and 15th of the following month | Art. 116 |
| Interest and arrears on covered claims, deposits and cash guarantees | 20%, final withholding | Triggered by payment or account debit/credit | Arts. 121-123 |
| Capital gain on sale or repurchase of shares/quotas | 20%, final withholding | Between the 1st and 15th of the month after the transaction | Art. 117 |
| Hidden remuneration or benefits | 45%, final tax | Follow distribution procedure | Art. 116 |

Profits of a Haiti permanent establishment of a nonresident company are deemed distributed each fiscal year and are subject to Article 116 withholding. Article 120's parent-subsidiary exemption requires both entities to be in Haiti and therefore should not be assumed for an outbound dividend.

## 3. Base and characterization

The service-withholding base is the consideration paid for services within the Code's definition. Interest withholding uses the gross interest or arrears. Distribution withholding applies to the covered distributed income.

Separate mixed contracts into defensible components only when the contract, invoice and actual conduct support that split. The official provisions reviewed do not establish a single catch-all royalty rate in the extracted 2026 Code text; royalty classification and rate are therefore `needs-sources` before filing.

## 4. Filing and remittance deadlines

For nonresident services and covered distributions, remit from the 1st through the 15th of the month following payment or allocation. Share-transfer withholding follows the same following-month window. Interest becomes due on payment or when posted to debit or credit; confirm the DGI return and operational remittance date.

**Source status:** statutory windows are verified in the Code. Current DGI form numbers, electronic schemas and any implementing notices are `needs-sources`.

## 5. Penalties and interest

Article 474 imposes 10% for a missing or late declaration, rising to 40% after 30 days following formal notice and 80% for an occult activity. Article 475 adds monthly fixed fines by taxpayer class. Article 476 applies a 10% late-payment addition where the amount should have been withheld at source. Apply the Code's anti-stacking rule in Article 476(4) when declaration and payment penalties overlap.

**AUDIT FLASH POINT** — Do not treat the 20% service withholding as proof that the expense is deductible. Article 71 also requires justification and direct business purpose, and related-party payments face Articles 77-80.

## 6. Treaty, permanent-establishment and transfer-pricing coordination

Before reducing a statutory withholding amount, establish the legal basis, residence and beneficial-owner facts and complete the DGI procedure. For a permanent establishment, coordinate ordinary profit tax with the deemed-distribution rule in Article 119. For a related party, apply the arm's-length standard independently of withholding.

## 7. Worked example — nonresident service fee

A Haiti resident pays HTG 5,000,000 for services to a beneficiary fiscally resident outside Haiti. Article 97 withholding is HTG 1,000,000 before any valid relief.

```oa-check
name: haiti nonresident service withholding
inputs:
  service_fee: 5000000
  rate: 0.20
steps:
  - withholding: service_fee * rate
expected:
  withholding: 1000000.00
```

## 8. Worked example — outbound distribution

A Haiti company distributes HTG 3,000,000 to a foreign shareholder. The Article 116 headline withholding is HTG 600,000.

```oa-check
name: haiti outbound distribution withholding
inputs:
  distribution: 3000000
  rate: 0.20
steps:
  - withholding: distribution * rate
expected:
  withholding: 600000.00
```

## 9. Ask the client first

1. What is the payment's legal and economic character, and is the contract mixed?
2. Where is the beneficial recipient fiscally resident?
3. Does the recipient have a Haiti permanent establishment?
4. Is the counterparty related or in a preferential regime?
5. Which DGI form and implementation notice applies on the payment date?
6. Is any relief claimed, and what evidence supports it?

## 10. Sources

- [DGI — Code Général des Impôts, official PDF](https://dgi.gouv.ht/wp-content/uploads/2026/10/Code-Fiscal.pdf) — arts. 71, 77-80, 95-97, 113-123 and 474-476; opened 2026-10-24.
- [DGI — decree/code landing page](https://dgi.gouv.ht/dgi_doc/decret-remplacant-le-decret-du-19-decembre-2022-portant-le-code-fiscal/) — official publication context; accessed 2026-10-24.
- [DGI — fiscal calendar](https://dgi.gouv.ht/calendrier-fiscale/) — operational calendar check; accessed 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
