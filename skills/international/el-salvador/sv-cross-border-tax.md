---
name: sv-cross-border-tax
description: >-
  Use when a non-resident receives Salvadoran-source income or a
  Salvadoran-connected payer needs the 2026 withholding grid, tax-haven uplift,
  PE/branch rules, or treaty position. Trigger on El Salvador withholding,
  retención El Salvador, payments to foreign suppliers El Salvador, tax haven
  25% El Salvador, branch profits El Salvador. Covers 20% WHT on
  Salvadoran-source payments to non-residents, 25% preferential-regime uplift,
  5% dividends, 10% interest, services-used-in-country source rule, PE triggers,
  and the limited treaty network. Source-cited draft with needs-sources
  caveats.
jurisdiction: SV
category: cross-border
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# El Salvador cross-border tax

## 1. Who this applies to

- Non-resident individuals and entities earning **Salvadoran-source** income — taxpayers of the withholding regime administered by DGII (PwC El Salvador withholding taxes, read 2026-10-24).
- Salvadoran payers acting as withholding agents on outbound payments, and foreign companies operating through branches or PEs.
- Out of scope: resident-only flows (`sv-corporate-income-tax`, `el-salvador-income-tax`); connected-party pricing (`sv-transfer-pricing`).

## 2. Rates and source rules

| Payment / income | Rate | Notes | Source (as_of 2026-10-24) |
|---|---|---|---|
| Payments/credits to non-residents from Salvadoran-source income | 20% WHT | source includes services **used in** El Salvador even if performed/paid abroad | PwC withholding taxes |
| Same, counterparty in a tax haven / preferential regime | 25% WHT | list per DGII guideline 700-DGII-GA-2026-002 (Sept 2024 update cited by PwC) | PwC withholding taxes |
| Dividends / profits remitted or credited to shareholders | 5% WHT | 25% if paid to a tax haven | PwC income determination |
| Interest paid by Salvadoran residents (capital invested in country) | 10% WHT | 20% if financial services between related parties | PwC income determination |
| International transport services to non-residents | 5% WHT | reduced category | PwC withholding taxes |
| Insurance, reinsurance, bondings to non-residents | 5% WHT | reduced category | PwC withholding taxes |
| Film/music/cable/satellite intangible rights | 5% WHT | reduced category | PwC withholding taxes |
| Services by resident individuals (non-labour) | 10% WHT | domestic rule, listed for completeness | PwC withholding taxes |
| Intangible acquisitions between resident entities | 5% WHT | domestic rule | PwC withholding taxes |

- **Source rule**: income from assets located in the country, activities performed or capital invested in the territory, and services rendered **or used** in national territory is Salvadoran-source regardless of where paid or performed (PwC withholding taxes, read 2026-10-24).
- **Preferential-regime test** (guideline 700-DGII-GA-2026-002): any jurisdiction not specifically named that exempts income tax or taxes it at more than 80% below the Salvadoran liability is treated as preferential/low-or-no-tax; holding companies, SEM headquarters, international trusts and similar vehicles are named categories (PwC withholding taxes, read 2026-10-24).

## 3. Base and computation

- WHT applies to the gross payment or credit unless a specific base rule applies; dividends: 5% of cash profits remitted or credited (PwC income determination, read 2026-10-24).
- Territoriality cuts the other way for inbound flows: amounts received from abroad from foreign sources are excluded from taxable income (PwC income determination, read 2026-10-24).

## 4. Deadlines and filing

- WHT is settled with the payer's monthly tax filings through the banking system; the CIT annual return is due by 30 April (PwC tax administration, read 2026-10-24).
- Branch/PE: foreign companies with authorised branches file and pay like domestic companies (PwC branch income, read 2026-10-24).

## 5. Penalties and interest

- Failure to withhold: fiscal-code interest and surcharges (exact rates **needs-sources**); audit window 3 years (timely) / 5 years (late or unfiled); payment limitation 10 years (PwC tax administration, read 2026-10-24).

## 6. Treaties and PE

- El Salvador's double-tax-treaty network is **limited**; treaty entitlement for a specific counterparty is **needs-sources** — verify before reducing any WHT.
- PE triggers: fixed place of business; non-independent agent habitually concluding contracts in the foreign entity's name; construction/installation or supervision **exceeding six months** (PwC corporate residence, read 2026-10-24).
- Branch profits repatriation: 5% WHT (25% haven) on profits paid/credited to the non-domiciled head office or affiliates (PwC branch income, read 2026-10-24).

## 7. Worked examples

**Example 1 — service fee used in El Salvador.** A Salvadoran company pays a non-resident consultant USD 100,000 for advisory used in El Salvador. WHT: 100,000 × 20% = USD 20,000, filed with the payer's monthly return. If the consultant sits in a DGII-listed preferential regime: 100,000 × 25% = USD 25,000.

```oa-check
name: sv services-used-in-country wht
inputs:
  fee: 100000
steps:
  - wht_standard: fee * 0.20
  - wht_haven: fee * 0.25
expected:
  wht_standard: 20000.00
  wht_haven: 25000.00
```

**Example 2 — dividend repatriation.** A Salvadoran subsidiary distributes USD 300,000 of cash profits to its foreign parent. Dividend WHT: 300,000 × 5% = USD 15,000. If the parent is a DGII-listed holding in a preferential regime: 300,000 × 25% = USD 75,000.

```oa-check
name: sv dividend repatriation wht
inputs:
  dividend: 300000
steps:
  - wht_standard: dividend * 0.05
  - wht_haven: dividend * 0.25
expected:
  wht_standard: 15000.00
  wht_haven: 75000.00
```

## 8. Ask the client first

1. Where is the counterparty resident, and does DGII's guideline list treat it as preferential?
2. Is the service **used in** El Salvador — that alone creates source?
3. Which WHT rate fits the flow (20/25/10/5%) — and was it applied on gross?
4. Is there a PE risk (six-month construction rule, contract-concluding agent)?
5. Any treaty claimed — does El Salvador actually have one with that state?

## 9. Sources

- [PwC Worldwide Tax Summaries — El Salvador Corporate: Withholding taxes](https://taxsummaries.pwc.com/el-salvador/corporate/withholding-taxes) — read 2026-10-24 (PwC last reviewed 27 Sep 2026).
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Income determination](https://taxsummaries.pwc.com/el-salvador/corporate/income-determination) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Corporate residence](https://taxsummaries.pwc.com/el-salvador/corporate/corporate-residence) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Branch income](https://taxsummaries.pwc.com/el-salvador/corporate/branch-income) — read 2026-10-24.
- [PwC Worldwide Tax Summaries — El Salvador Corporate: Tax administration](https://taxsummaries.pwc.com/el-salvador/corporate/tax-administration) — read 2026-10-24.
- DGII guideline 700-DGII-GA-2026-002 — cited via PwC; primary text **needs-sources** (unreachable 2026-10-24).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
