---
name: cr-corporate-income-tax
description: >
  Use this skill whenever asked about Costa Rica corporate income tax (impuesto sobre las utilidades, sociedades anónimas, personas jurídicas, declaración de renta D-102, régimen de empresas, exoneraciones MEIC). Trigger on phrases like "impuesto sobre las utilidades Costa Rica", "corporate tax Costa Rica", "D-102", "sociedad anónima impuestos", "tarifa 30% utilidades Costa Rica", "empresas pequeñas régimen tributo Costa Rica". Covers the corporate income-tax branch of Ley 7092 (LIR) as reformed by Ley 9635, the 30% general rate, graduated small-company rates, territorial base, deadlines, penalties, and withholding interaction. Tax year 2026 draft; primary consolidated text needs-sources, figures carry PwC citations.
jurisdiction: CR
category: international
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-28
version: 0.2
---

# Costa Rica corporate income tax

> **Source status.** The consolidated post-2019 text of the LIR corporate
> title could not be fetched from an official page in this environment
> (SCIJ renders via JavaScript; hacienda.go.cr unreachable 2026-10-24).
> Rates below carry PwC Tax Summaries citations (read 2026-10-24) and the
> as-enacted LIR text from official ministry mirrors. A Costa Rican CPA must
> confirm current indexed thresholds before filing.

## 1. Who applies

- Companies (sociedades anónimas, sociedades de responsabilidad limitada, and other personas jurídicas) on their net profits — Título I LIR ("impuesto sobre las utilidades"), as restructured by Ley 9635 arts. 102–111.
- Branches/permanent establishments of foreign companies, on CR-source profits.
- Sole proprietors with profit-generating activity fall under the separate self-employed schedule — see `costa-rica-income-tax`.

## 2. Rates and thresholds

| Category | Rate | Source |
|---|---|---|
| General corporate rate (profits) | 30% | _(PwC Tax Summaries, CIT title of Ley 9635 — read 2026-10-24); archived Ley 7092 consolidated text (`CR-ley-7092-impuesto-renta.pdf`) Art. 15(a): "Personas jurídicas: Treinta por ciento (30%)")_ |
| Small companies (MEIC/MAG-registered, gross income ≤ CRC 119,174,000 band) | 5% / 10% / 15% / 20% graduated on net income bands | _(PwC — thresholds indexed annually; confirm current year)_ |
| Capital gains and passive income of individuals | separate schedule (Ley 9635 Título II) | see `costa-rica-income-tax` |

The pre-2019 LIR taxed sociedades anónimas at 25% and other companies at 30% (as-enacted text on official mirrors); Ley 9635 unified the corporate rate at 30% — **needs-sources** at consolidated-text level.

## 3. Base

- Territorial: Costa Rica-source income only (LIR arts. 1–2, 8; source rules arts. 9–10).
- Net income = gross income minus deductible costs/expenses useful, necessary and pertinent to producing the income (LIR art. 7, verified in as-enacted text).
- Passive income (dividends, interest, royalties, capital gains, real estate) of a resident corporation is taxed inside the same 30% base; substance requirements apply to avoid source re-characterisation _(PwC)_.

## 4. Deadlines

- Annual return D-102 (empresas): through TRIBU-CR, deadline staggered by the last digits of the taxpayer identification number in the months following year-end (calendar-year taxpayers: March–April band) — **needs-sources** for the current DGT resolution.
- Provisional monthly payments (pagos mínimos) on the prior-year base.

## 5. Penalties and interest

- Ley 4755 (Código de Normas y Procedimientos Tributarios): late filing fine (1% of monthly declared income, min 25% of a base salary), understatement fines 10%–100%, interest at the DGT-published rate.
- Ley 9635 art. 85 bis (verified in the PGR text, 2026-10-24): refusing alternative payment methods is fined one base salary.

## 6. Cross-border

- Outbound remittances suffer final withholding (dividends 15%, royalties/technical services 25%, interest 5.5%–15%) — see `cr-cross-border`.
- Transfer pricing for related-party transactions — see `cr-transfer-pricing`.
- Treaty network is narrow (Germany, Canada, Spain, Dominican Republic, Ecuador, Mexico, Chile in force at various dates) — verify status per instrument.

## 7. Worked examples

**Example 1 — general corporate rate.**

```oa-check
name: Net profit CRC 100,000,000, general 30%
inputs:
  profit: 100000000
steps:
  - tax: profit * 0.30
expected:
  tax: 30000000
```

**Example 2 — graduated small-company bands (PwC band values; indexed yearly).**

```oa-check
name: Net profit CRC 50,000,000 in small-company bands 5/10/15/20
inputs:
  profit: 50000000
steps:
  - band1: min(profit, 5621000) * 0.05
  - band2: (min(profit, 8433000) - 5621000) * 0.10
  - band3: (min(profit, 11243000) - 8433000) * 0.15
  - band4: (profit - 11243000) * 0.20
  - total: band1 + band2 + band3 + band4
expected:
  band1: 281050
  band2: 281200
  band3: 421500
  band4: 7751400
  total: 8735150
```

## 8. Ask the client

1. Legal form and registration (MEIC/MAG small-business registry)?
2. Fiscal year end and DGT deadline band (last ID digits)?
3. Any exempt income (exports are outside the territorial base)?
4. Related-party transactions (TP regime)?
5. Pagos mínimos history and provisional-payment reconciliation?

## 9. Sources

- [Ley 7092 LIR as-enacted PDF — COMEX mirror](https://www.comex.go.cr/media/1894/ley_7092.pdf) and [MEP mirror](https://www.mep.go.cr/sites/default/files/2024-12/3LeyImpestoRentaN%C2%B07092.pdf) — verified resolving 2026-10-24; arts. 1, 7, withholding-title rates verified in extracted text.
- [Ley 9635 — PGR text](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) — read 2026-10-24 (VAT title + art. 85 bis verified; the fetched page carries the IVA title only).
- [PwC Tax Summaries — Costa Rica CIT](https://taxsummaries.pwc.com/costa-rica/corporate/taxes-on-corporate-income) — read 2026-10-24 (30% general rate, small-company bands).
- Consolidated LIR text — SCIJ JS-rendered, **needs-sources**.

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
