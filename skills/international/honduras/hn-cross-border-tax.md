---
name: Honduras cross-border tax and nonresident withholding
description: Use when a Honduras payer, investor, branch, or adviser needs 2026 source, withholding, treaty, permanent-establishment, or outbound-payment treatment.
jurisdiction: HN
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Honduras cross-border tax and nonresident withholding

## 1. Who this applies to

Use this guide for Honduras-source income paid or credited to a nonresident or non-domiciled person, a foreign business operating through a Honduras branch or other local presence, and a Honduras person claiming foreign-tax or treaty relief. The Honduras payer is generally responsible for withholding and remitting tax on Article 5 income.

## 2. Statutory rates

Income Tax Law Article 5 taxes gross Honduras-source income of nonresidents and non-domiciliaries at the following headline rates:

| Payment or income | Rate |
|---|---:|
| Rent from movable or immovable property, except listed natural-resource and IP items | 25% |
| Natural-resource royalties | 25% |
| Salary, commissions or other service compensation | 25% |
| Profit of foreign enterprises through branches, subsidiaries, affiliates, agencies or representatives | 10% |
| Dividends and other profit distributions | 10% |
| Patent, design, secret-process, trademark and copyright royalties | 25% |
| Commercial interest, bonds, securities and other obligations | 10% |
| Aircraft, vessel and land-transport operations | 10% |
| Communications, software, IT and telematics operations | 10% |
| Insurance and surety premiums | 10% |
| Public entertainment | 25% |
| Films, videotapes and cable-television rights | 25% |
| Other operating income not listed | 10% |

Article 5 states that the payer is responsible for withholding and paying over the tax. Related-party interest is treated as dividends where the statutory relatedness condition applies.

## 3. Base and sourcing

The nonresident tax base is gross Honduras-source income unless another rule or valid treaty changes the result. Classify the legal and economic character of the payment before selecting the rate: a mixed software contract, for example, may include licensing, communications, support and services with different factual attributes.

For a branch or other local operation, first test whether ordinary net-basis corporate income tax applies and then whether an Article 5 branch-profit item also arises. Do not apply a gross withholding table mechanically to locally assessed net business profit.

## 4. Withholding and filing deadlines

Withhold when the governing Income Tax Law and current SAR procedure require it, issue the recipient evidence, and remit through the SAR-prescribed return and payment channel. The consolidated statute establishes payer responsibility, but the official sources reviewed for this draft did not provide one stable 2026 page listing every form code and remittance deadline. Confirm the live SAR calendar and form before payment.

**Source status:** operational form numbers, due dates and payment mechanics are `needs-sources` until matched to a current SAR resolution or calendar.

## 5. Penalties and interest

A payer that fails to withhold or remit can remain liable for the tax and can incur Tax Code interest and penalties. Keep the invoice, contract, characterization memo, residence evidence, beneficial-owner support, withholding computation, exchange-rate evidence and SAR receipt together.

**AUDIT FLASH POINT** — Fees described as “reimbursements,” “software,” or “shared costs” should be tested from the underlying rights and services, not their invoice label.

## 6. Treaty and transfer-pricing coordination

Do not reduce an Article 5 rate merely because the recipient is foreign. Establish that an applicable treaty or other instrument is in force, that the recipient is resident and beneficially entitled, and that procedural requirements were met. Retain the residence certificate and relief computation.

Related-party payments must also meet the arm's-length standard in Law 232-2011 and Agreement 027-2015. Withholding on the recorded payment does not protect an excessive deduction from adjustment.

## 7. Worked example — dividend

A Honduras company declares HNL 1,000,000 to a nonresident shareholder. Before treaty relief, Article 5's 10% rate produces HNL 100,000 withholding.

```oa-check
name: honduras nonresident dividend withholding
inputs:
  dividend: 1000000
  rate: 0.10
steps:
  - withholding: dividend * rate
expected:
  withholding: 100000.00
```

## 8. Worked example — IP royalty

A Honduras payer owes HNL 800,000 for foreign patent rights. Before treaty relief, Article 5's 25% rate produces HNL 200,000 withholding.

```oa-check
name: honduras patent royalty withholding
inputs:
  royalty: 800000
  rate: 0.25
steps:
  - withholding: royalty * rate
expected:
  withholding: 200000.00
```

## 9. Ask the client first

1. Who is the legal and beneficial recipient, and where is it resident?
2. What does the contract actually provide: services, IP rights, financing, insurance, transport or several elements?
3. Is the recipient related to the payer, in a special regime, or operating through a Honduras presence?
4. Is treaty relief claimed, and is a current residence certificate available?
5. Which SAR form and deadline apply on the payment date?

## 10. Sources

- [SAR — Income Tax Law and amendments](https://www.sar.gob.hn/download/consolidado-ley-impuesto-sobre-la-renta-25-junio-2018/) — Article 5 rate table and payer responsibility; accessed 2026-10-24.
- [SAR — legal library](https://www.sar.gob.hn/download-category/otras-leyes/) — current-law access point; accessed 2026-10-24.
- [Agreement 027-2015, transfer-pricing regulation (SAR)](https://www.sar.gob.hn/download/acuerdo-027-2015/) — related-party coordination; accessed 2026-10-24.
- [SAR — home](https://www.sar.gob.hn/) — verify forms and calendar at filing; accessed 2026-10-24.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
