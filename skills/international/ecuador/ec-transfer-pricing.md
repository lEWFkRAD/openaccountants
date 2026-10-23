---
name: ec-transfer-pricing
description: >
  Ecuador transfer pricing reference for 2026. Covers the arm's-length
  obligation for transactions with related parties under the Ley de
  Régimen Tributario Interno (LRTI) and its Reglamento, the SRI's
  cooperative-compliance forum guidance, documentation expectations,
  the 25% corporate base the adjustments hit, ISD interaction, and
  penalties. Trigger on Ecuador transfer pricing, precios de
  transferencia, partes relacionadas, SRI ajuste. Source-cited draft.
jurisdiction: EC
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Ecuador transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the SRI transfer-pricing
forum page (sri.gob.ec/foro-precios-de-transferencia, HTTP 200 — states
directly that taxpayers who transact with related parties must determine
income, costs and deductible expenses using the prices independent parties
would have used in comparable operations), the SRI portal (sri.gob.ec,
HTTP 200), the Asamblea Nacional LRTI page (archivo.asambleanacional.gob.ec,
HTTP 200) and the LRTI reform PDF (asambleanacional.gob.ec, HTTP 200), and
the pack's tier-2 skills (`ec-corporate-income-tax`, `ec-tax-overview`).
Currency US dollar (Ecuador is dollarized). SRI (Servicio de Rentas
Internas) administers.

## 2. Who the rules apply to

- **Related-party transactions.** Taxpayers celebrating operations or
  transactions with related parties must determine deductible income,
  costs and expenses at arm's length (SRI forum page, read 2026-10-23;
  statutory anchor in the LRTI — article numbers **needs-sources** pending
  the consolidated text).
- **Relatedness** follows the LRTI/Reglamento family, control and
  economic-linkage tests (thresholds **needs-sources**).
- **Tax-haven layer:** the corporate rate rises where tax-haven
  shareholders are involved (carried from `ec-corporate-income-tax`) —
  related-party structures through haven vehicles sit in that flash point.

## 3. Rates and thresholds

| Item | Rate / threshold | Source (as_of 2026-10-23) |
|---|---|---|
| Corporate income tax base the adjustment hits | 25% general | LRTI, carried from `ec-corporate-income-tax` (PWC-cited) |
| Higher rate with tax-haven shareholders | applies; rate unconfirmed | carried from `ec-corporate-income-tax` — needs-sources |
| Master/local file thresholds | not published at resolved path | **needs-sources** |
| Andean Community (CAN Decision 578) | residence tie-break for Andean residents | carried from `ec-corporate-income-tax` |

## 4. Filings and deadlines

- Transfer-pricing analysis supports the annual income tax return
  (declaración de renta, due in March–April by last-two-digits schedule —
  carried from `ec-corporate-income-tax`, approx — confirm).
- The SRI runs a cooperative-compliance programme (Programa Cooperativo
  para el Cumplimiento Fiscal) with a dedicated transfer-pricing forum —
  documentation is expected on request (SRI forum page, 2026-10-23).

## 5. Penalties and interest

Understatement of related-party pricing draws the general tax-administration
penalties of the Código Tributario plus interest; specific percentages
**needs-sources** — confirm against the Código before quoting.

## 6. Worked examples

**Example 1 — related-party export underpricing.** An Ecuadorian exporter
sells bananas to its US affiliate for USD 1,000,000 when the arm's-length
price is USD 1,300,000. The SRI restates income up by 300,000; additional
income tax = 300,000 × 25% = 75,000.00.

```oa-check
name: Export underpricing restatement USD 300,000
inputs:
  arm_length: 1300000
  charged: 1000000
steps:
  - uplift: arm_length - charged
  - tax: uplift * 0.25
expected:
  tax: 75000.00
```

**Example 2 — management fee overcharge.** A Quito company pays its
foreign parent a management fee of USD 400,000; only USD 250,000 is
supportable. Disallowed 150,000 × 25% = 37,500.00 additional tax, plus
the 25% royalty/services withholding exposure on the payment itself
(see `ec-cross-border`).

```oa-check
name: Management fee disallowance USD 150,000
inputs:
  paid: 400000
  supportable: 250000
steps:
  - disallowed: paid - supportable
  - tax: disallowed * 0.25
expected:
  tax: 37500.00
```

## 7. Ask the client first

1. Which transactions run through related parties — imports, exports,
   services, financing?
2. Is any counterparty in a tax haven (rate step-up risk)?
3. Does transfer documentation exist — comparables, contracts?
4. Are Andean Community residents involved (Decision 578 tie-break)?
5. Which last-two-digits filing window governs the return year?

## 8. Sources

- [SRI — Foro Precios de Transferencia](https://www.sri.gob.ec/foro-precios-de-transferencia) — read 2026-10-23 (HTTP 200; arm's-length obligation text).
- [SRI portal](https://www.sri.gob.ec/) — read 2026-10-23.
- [Asamblea Nacional — LRTI / Código Tributario](https://archivo.asambleanacional.gob.ec/index.php/ley-de-regimen-tributario-interno-codigo-tributario) — read 2026-10-23 (HTTP 200).
- [LRTI reform law (PDF)](https://www.asambleanacional.gob.ec/es/system/files/ley_reformatoria_a_la_ley_de_regimen_tributario_interno_y_a_la_ley_reformatoria_para_la_equidad_tributaria_del_ecuador.pdf) — read 2026-10-23 (HTTP 200).
- Pack skills carried: `ec-corporate-income-tax`, `ec-tax-overview` (tier 2).

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
