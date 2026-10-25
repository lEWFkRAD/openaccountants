---
name: sv-transfer-pricing
description: >-
  Use when an El Salvador taxpayer transacts with related parties or needs the
  2026 arm's-length, documentation, and withholding position on connected-party
  flows. Trigger on El Salvador transfer pricing, precios de transferencia,
  related-party interest El Salvador, DGII connected-party audit. DGII lists
  transfer-pricing compliance as a standing audit focus; the statutory regime
  (methods, thresholds, study requirements) is needs-sources pending the
  Income Tax Law text. Source-cited draft.
jurisdiction: SV
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# El Salvador transfer pricing

## 1. Who this applies to

- Salvadoran CIT taxpayers (companies, branches, PEs) transacting with related parties — parent, subsidiaries, affiliates, directors-related entities — domestic or cross-border.
- Salvadoran payers on connected-party financing: **financial services between related parties carry 20% withholding** versus 10% on ordinary interest to non-residents (PwC El Salvador income determination, read 2026-10-24) — the withholding lane already prices relatedness.
- Out of scope: unrelated-party pricing; IVA (`el-salvador-iva`).

## 2. Core rules and threshold

- DGII's stated audit focus expressly includes **"Compliance of transfer pricing obligations"** and **"Compliance of the obligations held with non-domiciled subjects, especially those domiciled in tax havens"** (PwC El Salvador tax administration, read 2026-10-24).
- **AUDIT FLASH POINT** — related-party service fees, royalties, and financing charged by foreign affiliates are the classic recharacterisation targets: DGII can disallow the expense (CIT 30%) and reprice the flow, and the tax-haven WHT uplift (20%→25%) applies where the counterparty sits in a listed preferential regime (guideline 700-DGII-GA-2026-002, cited via PwC withholding taxes, read 2026-10-24).
- Statutory TP mechanics — methods, study thresholds, filing deadlines under the Income Tax Law: **needs-sources** (consolidated law text not reachable from the drafting environment 2026-10-24). Do not assert a study deadline without the statute.

## 3. Practical standard

- Price connected-party goods, services, intangibles and financing at arm's length; keep contemporaneous support (contracts, invoices, benchmarking or cost build-ups) — DGII audits **deductions and supporting documentation** as a named focus (PwC tax administration, read 2026-10-24).
- Interest deductibility already requires the loan to fund a source of taxable income (PwC deductions, read 2026-10-24); thin related-party debt fails that test before any TP adjustment is needed.

## 4. Adjustments and double tax

- A DGII upward adjustment increases Salvadoran taxable income at 30% (25% only if the adjusted total stays ≤ USD 150,000).
- El Salvador's treaty network is limited; corresponding-adjustment relief is **needs-sources**.

## 5. Penalties and interest

- Underpayment carries fiscal-code interest and surcharges (exact rates **needs-sources**); audit window 3 years (timely returns), 5 years (late/unfiled) (PwC tax administration, read 2026-10-24).

## 6. Cross-border points

- Related-party interest and financial services to non-residents: 20% WHT at payment (PwC income determination, read 2026-10-24); see `sv-cross-border-tax` for the full WHT grid.
- Payments to entities in DGII-listed preferential/low-or-no-tax regimes: 25% WHT and heightened scrutiny.

## 7. Worked examples

**Example 1 — related-party interest withholding.** A Salvadoran company pays USD 200,000 of interest to its foreign parent. Financial services between related parties: 200,000 × 20% = USD 40,000 WHT (an unrelated third-party loan would carry 10% = USD 20,000).

```oa-check
name: sv related-party interest wht
inputs:
  interest: 200000
steps:
  - wht_related: interest * 0.20
  - wht_unrelated: interest * 0.10
expected:
  wht_related: 40000.00
  wht_unrelated: 20000.00
```

**Example 2 — understated export price.** A Salvadoran manufacturer sells goods to its foreign affiliate at USD 400,000 when the supported arm's-length price is USD 500,000. DGII uplifts the base by USD 100,000; CIT effect: 100,000 × 30% = USD 30,000, before interest.

```oa-check
name: sv understated related-party sale uplift
inputs:
  arm_length_price: 500000
  recorded_price: 400000
steps:
  - uplift: arm_length_price - recorded_price
  - extra_cit: uplift * 0.30
expected:
  extra_cit: 30000.00
```

## 8. Ask the client first

1. Which connected-party flows exist (goods, services, royalties, interest, financing) and at what prices?
2. Is there contemporaneous arm's-length support for each?
3. Is the counterparty in a DGII-listed preferential/low-or-no-tax regime?
4. Was the correct WHT rate applied on the payment leg (10% vs 20% vs 25%)?
5. Any DGII requerimiento already received — which years?

## 9. Sources

- [PwC Worldwide Tax Summaries — El Salvador Corporate: Tax administration](https://taxsummaries.pwc.com/el-salvador/corporate/tax-administration) — read 2026-10-24 (PwC last reviewed 27 Sep 2026).
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Income determination](https://taxsummaries.pwc.com/el-salvador/corporate/income-determination) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Deductions](https://taxsummaries.pwc.com/el-salvador/corporate/deductions) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Withholding taxes](https://taxsummaries.pwc.com/el-salvador/corporate/withholding-taxes) — read 2026-10-24.
- Ley de Impuesto sobre la Renta, transfer-pricing articles — **needs-sources** (unreachable 2026-10-24).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
