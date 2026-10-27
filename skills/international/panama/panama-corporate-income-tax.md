---
name: NAME
description: >
  DESC
jurisdiction: PA
category: CAT
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Panama corporate income tax

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: DGI's ISR rate
schedule (Art. 710 Código Fiscal), filing-deadline table, and Form 07
dividend pages were read directly. The Fiscal Code (Ley 8 de 1972)
consolidated text could not be fetched (404 on the expected Asamblea
path), so article numbers are cited as DGI publishes them; the CAIR and
complementary-tax mechanics are carried from the existing
panama-income-tax skill and need primary-text confirmation.

## 2. Who applies

Every "persona jurídica" with Panamanian-source income — Panamanian
companies on their Panamanian-source income, and foreign companies to
the extent of Panamanian-source income (permanent establishment or
Panamanian-source flows). Panama's system is territorial: foreign-source
income is reported on its own line and not taxed, and related costs are
not deductible (DGI general rules, read via panama-income-tax).

## 3. Rates

| Item | Rate | Source |
|---|---|---|
| Corporate ISR on net taxable income (fiscal years from 2011) | 25% | DGI rate schedule, Art. 710 (read 2026-10-27) |
| Dividend / profit-sharing withholding, Panamanian-source profits | 10% | DGI Form 07 page (read) |
| Dividend withholding where profits came from exempt ISR income (govt/bank interest, savings deposits) | 5% | DGI Form 07 page (read) |
| Complementary tax where distributions fall below 40% of after-tax net profits | 10% of the shortfall | panama-income-tax (needs primary confirmation) |
| CAIR (regimen de ingresos afectables) for companies above B/.1,500,000 taxable income | special base rules | panama-income-tax (needs confirmation) |
| Securities capital-gains advance withheld by the buyer | 5% | DGI Form 107/108 pages (read) |

## 4. Base and timing

Net taxable income = gross Panamanian-source income less deductions
connected to taxable income, with the Fiscal Code's non-deductible list
(art. 712 — text needs-sources). Accounting must follow Panamanian tax
rules; foreign-source income and its costs sit outside the base (DGI
general rules). The fiscal year is the calendar year unless DGI
authorises a special period (DGI deadlines page, read).

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Annual corporate return (Form 1V) | before 31 March for the prior fiscal year | DGI deadlines table (read) |
| Dividend withholding return (Form 07) | within 10 days of distribution | DGI deadlines table (read) |
| Remesas withholding return (Form 05) | within 10 days of payment or credit | DGI deadlines table (read) |
| Securities capital-gain advance (Form 108) | remit within 10 days of the payment obligation | DGI deadlines table (read) |
| ITBMS (if also VAT-registered) | monthly, 15th of following month | panama-itbms |

## 6. Penalties and interest

Late filing draws a fine (DGI sanctions page read; amounts per taxpayer
classification — needs-sources for the current schedule); late payment
adds a 10% surcharge plus interest (panama-itbms cites Fiscal Code
art. 752 area — needs confirmation). Interest on deferred payment:
needs-sources.

## 7. Cross-border interactions

Payments or credits of Panamanian-source income to non-residents
(services, interest, commissions, rents, royalties) are taxed by
withholding on Form 05 within 10 days; treaty relief goes on Form 433
(DGI Form 05 page, read) — see panama-cross-border. Transfer pricing
studies and the Informe 930 apply to related-party flows
(panama-transfer-pricing). Bearer-share shareholders face a 20%
withholding on company loans (panama-income-tax, needs confirmation).

## 8. Worked examples

A Panamanian company earns B/. 200,000 of net taxable Panamanian-source
income (25%):

```oa-check
name: corporate ISR on 200000 net taxable income
inputs:
  renta: 200000
  tasa: 0.25
steps:
  - impuesto: renta * tasa
expected:
  impuesto: 50000.00
```

It distributes B/. 80,000 of dividends from those taxed profits (10%
withholding, Form 07 within 10 days):

```oa-check
name: dividend withholding 10 percent on 80000
inputs:
  dividendo: 80000
  tasa: 0.1
steps:
  - retencion: dividendo * tasa
expected:
  retencion: 8000.00
```

If it retained B/. 30,000 of the after-tax profit below the 40%
distribution test, the complementary tax on that shortfall (10%) is:

```oa-check
name: complementary tax on 30000 undistributed shortfall
inputs:
  faltante: 30000
  tasa: 0.1
steps:
  - impuesto_complementario: faltante * tasa
expected:
  impuesto_complementario: 3000.00
```

## 9. Ask the client / sources

Ask: Is every income line classified Panamanian-source vs foreign-source
before the return? Are distributions being tracked against the 40% test
before year-end? Are Form 05/07 filings inside the 10-day windows? Any
bearer shares (20% loan withholding)? Above B/.1.5M — CAIR modelling
done?

Sources: DGI Tarifa, Tab-Decla, Formulario07, Formulario05 pages (read
2026-10-27); panama-income-tax (existing skill). Needs-sources: Fiscal
Code consolidated text (arts. 705, 710-712, 752), CAIR decree text,
complementary-tax article, sanctions schedule.

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
