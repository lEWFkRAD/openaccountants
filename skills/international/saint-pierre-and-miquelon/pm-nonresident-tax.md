---
name: pm-nonresident-tax
description: >
  Use this skill when a person or entity outside Saint-Pierre-et-Miquelon receives archipelago-source income, owns a local business establishment, or needs a non-resident income-tax workpaper for 2026. It covers the local-source minimum tax, progressive-rate comparison, small-assessment threshold, investment-income withholding, foreign-income disclosure, permanent establishments, and appointment of a local representative. Trigger on Saint-Pierre-et-Miquelon non-resident, treaty, foreign income, withholding, permanent establishment, tax residence, local representative, cross-border dividend, or departure questions. It requires convention and residence evidence before a filing position is taken.
jurisdiction: PM
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-22
version: 0.1
---

# Saint-Pierre-et-Miquelon Non-Resident Tax v0.1

> **General reference only.** This source-cited draft requires review of the taxpayer's residence, permanent-establishment facts, and any applicable convention before filing or payment.

## 1. Who this applies to

Article 96 applies to persons who do not have their tax domicile in Saint-Pierre-et-Miquelon but receive Saint-Pierre or Miquelon-source income. Articles 114 and 116 address persons or companies with an establishment or property in the archipelago and permit the fiscal service to request appointment of a local representative. Residents must also identify foreign-source income and any convention credit.

## 2. Rates, bands and thresholds

The progressive table below is the article 95 schedule stated for tax calculated in 2026 on 2025 income. Apply it per quotient share before the non-resident minimum comparison.

| Taxable income per share | Rate | Tax year | Official source |
|---:|---:|---:|---|
| Up to EUR 10,140 | 0% | 2026 calculation | [Code local des impôts, art. 95](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| EUR 10,141–11,140 | 5% | 2026 calculation | Same |
| EUR 11,141–12,110 | 10% | 2026 calculation | Same |
| EUR 12,111–13,660 | 15% | 2026 calculation | Same |
| EUR 13,661–16,960 | 20% | 2026 calculation | Same |
| EUR 16,961–20,100 | 25% | 2026 calculation | Same |
| EUR 20,101–23,400 | 30% | 2026 calculation | Same |
| EUR 23,401–27,500 | 35% | 2026 calculation | Same |
| EUR 27,501–40,500 | 40% | 2026 calculation | Same |
| EUR 40,501–54,600 | 45% | 2026 calculation | Same |
| EUR 54,601–68,300 | 50% | 2026 calculation | Same |
| Above EUR 68,300 | 55% | 2026 calculation | Same |
| Non-resident minimum | 10% of net taxable local-source income | 2026 calculation | [Art. 96](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| No assessment under the article 96 minimum | Where corresponding tax does not exceed EUR 550 | 2026 calculation | Same |
| Covered dividends to non-resident | 15% of gross | 2026 work | [Art. 72 bis](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |
| Non-resident interest | 10% | 2026 work | [Art. 74 bis](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf) |

## 3. The base

Classify income as archipelago-source or foreign-source, determine allowable category deductions, and compute net taxable local-source income. For a non-resident, compare article 95 tax with the 10% article 96 minimum. A taxpayer may support a lower effective rate by showing that the local rate on worldwide Saint-Pierre, Miquelon, and foreign income would be below the minimum. Do not apply family quotient benefits to a non-resident without checking article 97 bis and any reciprocal treaty.

For businesses, article 114 taxes persons with a stable establishment in the archipelago. Foreign-source dividends and credits require gross reporting and convention review under the movable-income rules.

## 4. Deadlines and filing

Use the return deadline and forms published for the relevant income year by the Direction des Services Fiscaux. Article 246 provides income-tax instalments on 15 March and 15 June when the prior-year roll meets the statutory threshold, followed by collection of the balance. A non-local company may be asked under article 116 to name an archipelago representative within 90 days after receiving the request.

## 5. Penalties and interest

Article 246 applies a 10% addition where estimated instalments are reduced too far and the final-tax miscalculation exceeds 10%; unpaid monthly instalments also carry a 10% addition. Other late-filing, late-payment, or under-declaration consequences depend on the procedural article and notice. Do not infer a generic rate from these specific provisions.

## 6. Cross-border points

- Obtain a residence certificate and identify the applicable convention before applying source taxation or a credit.
- Separate salary, business profit, immovable-property income, dividends, and interest; source and withholding rules differ.
- Test for a stable establishment under article 114.
- Preserve gross foreign income and convention-credit evidence where a resident reports foreign income.
- Confirm whether the fiscal service has requested a local representative under article 116.

## 7. Worked examples

### Example 1 — Progressive tax exceeds the non-resident minimum

A non-resident has EUR 30,000 net taxable local-source income and one quotient share. Article 95 tax is EUR 5,249.50, while the 10% minimum is EUR 3,000. Before credits or a convention, the larger amount is EUR 5,249.50.

```oa-check
name: PM nonresident progressive tax comparison
inputs:
  income: 30000
steps:
  band_5: min(max(income - 10140, 0), 1000) * 0.05
  band_10: min(max(income - 11140, 0), 970) * 0.10
  band_15: min(max(income - 12110, 0), 1550) * 0.15
  band_20: min(max(income - 13660, 0), 3300) * 0.20
  band_25: min(max(income - 16960, 0), 3140) * 0.25
  band_30: min(max(income - 20100, 0), 3300) * 0.30
  band_35: min(max(income - 23400, 0), 4100) * 0.35
  band_40: max(income - 27500, 0) * 0.40
  progressive_tax: band_5 + band_10 + band_15 + band_20 + band_25 + band_30 + band_35 + band_40
  minimum_tax: income * 0.10
  tax_before_credits: max(progressive_tax, minimum_tax)
expected:
  progressive_tax: 5249.50
  minimum_tax: 3000.00
  tax_before_credits: 5249.50
```

### Example 2 — Small minimum-tax assessment threshold

A non-resident has EUR 4,000 net taxable local-source income. Progressive tax is zero and the 10% minimum is EUR 400. Because that corresponding tax does not exceed the EUR 550 article 96 threshold, no assessment is established under that minimum. The check recomputes the comparison margin; the legal no-assessment conclusion is not an arithmetic subtraction.

```oa-check
name: PM nonresident small-assessment threshold
inputs:
  income: 4000
  no_assessment_threshold: 550
steps:
  progressive_tax: max(income - 10140, 0) * 0.05
  minimum_tax: income * 0.10
  threshold_margin: no_assessment_threshold - minimum_tax
expected:
  progressive_tax: 0.00
  minimum_tax: 400.00
  threshold_margin: 150.00
```

## 8. Ask the client first

- Where was the taxpayer resident during each relevant period?
- What local-source and foreign-source income categories were received?
- Is there a stable establishment, office, agent, or local property?
- Which convention and residence certificate apply?
- What tax was withheld and what foreign tax or convention credit is documented?
- Has the fiscal service requested appointment of a local representative?

## 9. Sources

- [Code local des impôts, 2026 consolidation](https://www.services-fiscaux975.fr/files/file/Documentation/2026/CLI_2026-CLI_AU%2004-05-2026.pdf), articles 72 bis, 74 bis, 95–97 bis, 114, 116, and 246 — `as_of: 2026-10-22`.
- [Direction des Services Fiscaux de Saint-Pierre-et-Miquelon](https://www.services-fiscaux975.fr/) — `as_of: 2026-10-22`.

<!-- openaccountants-cta-block -->
## Talk to a verified accountant

This guide is a source-cited draft. [Book a review with a verified accountant](https://calendly.com/openaccountants) before filing or paying.
