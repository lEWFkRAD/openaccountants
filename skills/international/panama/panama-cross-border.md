---
name: panama-cross-border
description: >
  Panama cross-border income reference for 2026. Covers withholding on remesas al exterior (payments or credits of Panamanian-source income to non-residents, Form 05 within 10 days, DGI page read 2026-10-27), dividend withholding 10 percent / 5 percent (Form 07, read), the 5 percent securities capital-gain advance (Forms 107/108, read), treaty relief via Form 433 and the DGI treaty list, and Panama territorial-source rules. Trigger on Panama non-resident withholding, remesa al exterior, Formulario 05 Panama, fuente panamena. Source-cited draft.
jurisdiction: PA
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Panama cross-border (non-residents and remesas)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: DGI's Form 05 (remesas
al exterior), Form 07 (dividends), Form 107/108 (securities gains) and
the filing-deadlines table were read directly. The Fiscal Code source
rules (art. 705) and treaty texts are needs-sources; the treaty list is
on DGI's Convenios Tributarios page (read).

## 2. Who applies

Any Panamanian person or company that pays or credits Panamanian-source
income to a beneficiary located abroad ("beneficiado radicado en el
extranjero") must withhold and file Form 05 within 10 days of payment
or credit, whichever comes first (DGI Form 05 page, read). The rule
covers personal work remuneration, interest, commissions, rents,
royalties and other Panamanian-source flows (read). A non-resident may
register with DGI and self-declare instead (read).

## 3. Rates

| Flow | Rate | Source |
|---|---|---|
| Panamanian-source payments/credits to non-resident companies | 25% (corporate rate applied to the Panamanian-source amount) | panama-income-tax (DGI-cited; needs primary confirmation) |
| Panamanian-source payments/credits to non-resident individuals | graduated 0/15/25% schedule | DGI Tarifa (read) via panama-income-tax |
| Dividends, Panamanian-source profits | 10% | DGI Form 07 (read) |
| Dividends from ISR-exempt profits (govt/bank interest, savings deposits) | 5% | DGI Form 07 (read) |
| Securities capital gains (buyer advance) | 5% | DGI Form 107/108 (read) |
| Treaty-reduced amounts | per treaty, Form 433 | DGI Form 05/433 pages (read) |

## 4. Base and timing

Panamanian-source income is defined by Fiscal Code art. 705 (text
needs-sources); DGI's plain rule: income "generated as a product of any
service or act, documented or not, that benefits a person in Panama" is
Panamanian-source — money sent abroad for services benefiting Panama is
a remesa (DGI Form 05 page, read). Withholding attaches at payment or
credit ("pague o acredite en cuenta"), whichever first (read).

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Form 05 (remesas withholding) | within 10 days of payment/credit | DGI deadlines table (read) |
| Form 07 (dividend withholding) | within 10 days of distribution | DGI deadlines table (read) |
| Form 108 (5% securities advance) | within 10 days of the payment obligation | DGI deadlines table (read) |
| Form 433 (treaty relief) | filed with the withholding cycle | DGI Form 05 page (read) |
| Non-resident annual return (if registered) | 31 March companies / 15 March individuals | DGI deadlines table (read) |

## 6. Penalties and interest

Late Form 05/07 filings draw DGI fines (sanctions page read; amounts
needs-sources) and late payment adds the 10% surcharge plus interest
(panama-itbms cites art. 752 area — needs confirmation).

## 7. Cross-border interactions

Panama has no worldwide taxation for non-residents: only
Panamanian-source flows are caught, and the remesa rule is the
collection mechanism. Treaty network (DGI list, read) reduces rates for
treaty residents via Form 433; the US has no income-tax treaty with
Panama (needs-sources confirmation), so US payers rely on the domestic
rules. Panama's territorial rule means a non-resident's foreign-source
income never enters the Panamanian base.

## 8. Worked examples

A Panamanian company pays its foreign parent B/. 40,000 for services
benefiting Panama (corporate 25% withholding, Form 05 within 10 days):

```oa-check
name: remesa withholding 25 percent on 40000 service fee
inputs:
  pago: 40000
  tasa: 0.25
steps:
  - retencion: pago * tasa
  - neto: pago - retencion
expected:
  retencion: 10000.00
  neto: 30000.00
```

A buyer acquires shares from a non-resident with a B/. 100,000 gain and
withholds the 5% advance (Form 108 within 10 days):

```oa-check
name: 5 percent advance on 100000 share sale gain
inputs:
  ganancia: 100000
  tasa: 0.05
steps:
  - adelanto: ganancia * tasa
expected:
  adelanto: 5000.00
```

## 9. Ask the client / sources

Ask: Which outbound payments are Panamanian-source under the DGI
benefit rule? Are Form 05 filings inside the 10-day window and Form 433
used where a treaty applies? Are share purchases from non-residents
collecting the 5% advance? Is any non-resident registered with DGI to
self-declare?

Sources: DGI Formulario05, Formulario07, Tab-Decla, Convenios
Tributarios, IIFiscal pages (read 2026-10-27). Needs-sources: Fiscal
Code art. 705 text, treaty list status incl. US position, sanctions
amounts, art. 752 interest mechanics.

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
