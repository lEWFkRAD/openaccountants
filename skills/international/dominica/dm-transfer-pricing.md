---
name: dm-transfer-pricing
description: >
  Use this skill whenever asked about Dominica transfer pricing, associated-persons rules, arm's-length pricing between related companies, or how the Inland Revenue Division re-prices related-party transactions. Trigger on phrases like "transfer pricing Dominica", "associated persons Dominica", "arm's length Dominica", "related party Dominica", "IRD re-pricing", "intercompany pricing OECS". Tax year 2026 draft marked needs-sources: the Income Tax Act Ch. 67:01 PDF is scanned (no text layer) so statutory article text could not be verified; the skill states the framework without quoting figures.
jurisdiction: DM
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Dominica transfer pricing

> **Needs-sources.** The Income Tax Act, Chapter 67:01 PDF on
> dominica.gov.dm is a scanned image with no extractable text (checked
> 2026-10-24), and the IRD site publishes no dedicated transfer-pricing
> guidance page. This skill describes the framework a practitioner should
> verify against the Act's associated-persons provisions and IRD practice
> before relying on it. **No statutory figures are quoted.**

## 1. Who applies

- Companies and trusts filing Dominica income-tax returns that transact with **associated persons** (the Act's related-party concept — control/capital/family links) or with non-residents whose Dominica-source income is computed under the Act.
- The IRD assesses on the statutory basis of "gains or profits forming assessable income" (IRD corporate guidance, read 2026-10-24); where related-party pricing understates Dominica profits, the assessment risk is re-pricing under the Act's associated-persons and source rules.

## 2. Rates and thresholds

- No separate transfer-pricing "rate": adjustments flow into the ordinary rates (companies 25% — see `dm-corporate-income-tax`).
- No published documentation threshold verified — **needs-sources**.

## 3. Base and methods

- Dominica has no published OECD-methods statute text extractable from the official PDF; in practice the CARICOM/OECD-aligned approach (CUP, cost-plus, TNMM) is what an examiner would expect. Treat method choice as professional judgment pending the Act text — **needs-sources**.
- Withholding on cross-border related-party payments (15% on royalties, management charges, commissions, interest, rent — verified on the IRD withholding page) operates independently of any re-pricing.

## 4. Deadlines

- Follows the ordinary return cycle: individuals 31 March; companies within 3 months after financial year-end (IRD corporate guidance, read 2026-10-24). No standalone TP return verified.

## 5. Penalties and interest

- Understatement feeds the Act's civil penalty regime: up to 10% of tax chargeable for incorrect returns, plus 1%/month interest on unpaid tax (IRD withholding page, verified 2026-10-24, citing ss. 98, 117–126).

## 6. Cross-border

- CARICOM Double Taxation Agreement Order 2008 is the main treaty instrument referenced by the IRD corporate page (read 2026-10-24); MAP page exists under IRD international-tax section but body text did not render — **needs-sources**.
- Country-by-Country Reporting: the IRD maintains a CbCR page under international tax (existence verified 2026-10-24; content **needs-sources**).

## 7. Worked examples

Illustrative only — no statutory mark-up is asserted.

**Example 1 — cost-plus intercompany supply.**

```oa-check
name: Related-party supply, cost base EC$25,000, illustrative 5% mark-up
inputs:
  cost_base: 25000
  markup_pct: 5
steps:
  - markup: cost_base * 0.05
  - price: cost_base + markup
expected:
  markup: 1250
  price: 26250
```

**Example 2 — management charge subject to withholding.**

```oa-check
name: Management charge EC$36,000 to a non-resident affiliate, 15% WHT
inputs:
  charge: 36000
steps:
  - wht: charge * 0.15
expected:
  wht: 5400
```

## 8. Ask the client

1. Which associated persons (ownership, control, family) sit on either side of the transaction?
2. What are the intercompany flows — goods, services, management charges, royalties, interest?
3. Are the 15% withholdings on those flows being deducted and remitted within 15 days of month-end?
4. Any IRD audit queries on related-party pricing?
5. Group size — does CARICOM/CRS CbCR or exchange-of-information reporting apply?

## 9. Sources

- [IRD — Withholding Tax](https://ird.gov.dm/tax-laws/withholding-tax) — read 2026-10-24 (15% WHT categories, s. 98 interest, penalties verified).
- [IRD — Corporate Income Tax](https://ird.gov.dm/tax-laws/corporate-income-tax) — read 2026-10-24 (assessable-income base, filing cycle, CARICOM DTA reference).
- [IRD — International Tax](https://ird.gov.dm/international-tax) — read 2026-10-24 (CbCR/MAP pages exist; text not rendered).
- [Income Tax Act Ch. 67:01 (PDF)](http://www.dominica.gov.dm/laws/chapters/chap67-01.pdf) — scanned, no text layer 2026-10-24; **needs-sources**.

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
