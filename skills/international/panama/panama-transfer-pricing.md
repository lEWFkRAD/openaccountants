---
name: panama-transfer-pricing
description: >
  Panama transfer pricing reference for 2026. Thin source-cited draft: DGI maintains a dedicated transfer-pricing section with the Informe 930 (Ventas y Prestacion de Servicios) and a required study (estudio de precios de transferencia) plus group documentation (DGI pages read 2026-10-27); the statute (Ley 52-2016 and amendments) and the 20 percent / 12.5 percent related-party interest withholding split are needs-sources. Trigger on Panama transfer pricing, precios de transferencia Panama, informe 930, partes relacionadas Panama. Source-cited draft, needs-sources.
jurisdiction: PA
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Panama transfer pricing

## 1. Scope and sources

Source-cited draft with a real gap: DGI's transfer-pricing section
(Precios de Transferencia: Concepto, Informe 930, study contents,
group documentation, normative list) was read on 2026-10-27, but the
underlying statute — Ley 52 de 2016 and its amendments (Ley 163-2022
area) — could not be fetched, so article-level rules and thresholds are
needs-sources. Do not quote Panama TP penalties or thresholds from this
skill without confirming the statute.

## 2. Who applies

Related-party transactions between a Panamanian taxpayer and a related
person abroad (Panama's system is territorial, so the TP net is drawn
around Panamanian-source flows and their allocation). DGI's section
defines the concept and requires the "Informe de Ventas y Prestación de
Servicios" (Formulario 930) plus a transfer-pricing study ("Estudio de
Precios de Transferencia") with group-level documentation (DGI section
navigation, read).

## 3. Rates and standards

| Item | Amount | Source |
|---|---|---|
| Arm's-length standard and methods | OECD-aligned methods per DGI concept page | statute text needs-sources |
| Related-party interest withholding (Panama-source) | 20% (vs 12.5% portfolio) | needs-sources (not on the pages read) |
| Informe 930 filing | annual informative return | DGI section (read); deadline needs-sources |
| Study and master-file documentation | required content per DGI pages | DGI section (read); thresholds needs-sources |

## 4. Base and timing

The TP base is the pricing of goods, services, intangibles and
financing between related parties where one side is Panamanian-source.
The Informe 930 accompanies the annual cycle; the study must exist when
DGI requests it (DGI concept page, read). Exact filing deadline:
needs-sources (the deadlines table read does not list 930).

## 5. Deadlines

Annual corporate return context: 31 March (DGI deadlines table, read).
Informe 930 and study deadlines: needs-sources. Treaty-relief and
remesa returns (Forms 433/05) run within 10 days of payment (read).

## 6. Penalties and interest

TP-specific penalties are in the statute (needs-sources). General late
filing fines and the 10% late-payment surcharge plus interest apply to
the underlying tax (panama-corporate-income-tax).

## 7. Cross-border interactions

Panama's territorial rule makes TP the main anti-avoidance lever for
outbound pricing: shifting Panamanian-source margin to a foreign
related party shrinks the 25% base. Related-party interest is the
classic flash point (20% vs 12.5% withholding split — needs-sources).
Free-zone and license companies still face TP on related-party trade
with the mainland (needs-sources on the free-zone interaction).

## 8. Worked examples

A Panamanian distributor buys from its foreign parent at an inflated
price and reports B/. 40,000 of Panamanian-source profit where the
comparable margin is B/. 90,000; on the B/. 50,000 reallocation the
25% corporate tax at stake is:

```oa-check
name: 25 percent tax on 50000 reallocated margin
inputs:
  realocado: 50000
  tasa: 0.25
steps:
  - impuesto: realocado * tasa
expected:
  impuesto: 12500.00
```

A foreign related lender receives B/. 100,000 of Panamanian-source
interest; if reclassified as related-party at 20% (rate needs-sources)
versus 12.5% portfolio, the withholding difference is:

```oa-check
name: withholding difference 20 versus 12.5 percent on 100000
inputs:
  interes: 100000
  rel: 0.2
  port: 0.125
steps:
  - retencion_relacionada: interes * rel
  - retencion_portafolio: interes * port
  - diferencia: (interes * rel) - (interes * port)
expected:
  retencion_relacionada: 20000.00
  retencion_portafolio: 12500.00
  diferencia: 7500.00
```

## 9. Ask the client / sources

Ask: Is an Informe 930 filed and a current study on hand? Which
related-party flows touch Panamanian-source income (trade, services,
intangibles, financing)? Is intercompany interest screened against the
related-party withholding rate? Free-zone/mainland pricing documented?

Sources: DGI Precios de Transferencia section and Convenios Tributarios
(read 2026-10-27). Needs-sources: Ley 52-2016 text and amendments,
930 deadline and thresholds, related-party interest withholding rates,
free-zone interaction.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who
put their name behind the tax answers AI gives people. The live,
always-current version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
