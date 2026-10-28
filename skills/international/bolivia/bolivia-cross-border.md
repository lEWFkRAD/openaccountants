---
name: bolivia-cross-border
description: >
  Bolivia cross-border tax reference for 2026. Covers the
  territorial source principle for non-residents, the 12.5%
  withholding on dividends, branch profit remittances, interest,
  royalties and services to non-residents, the 2.5% rate for
  partially-performed activities, the 16% rate for non-domiciled
  individuals, the treaty network (Andean Community, Argentina,
  France, Germany, Spain, Sweden, UK) with Spain 10% and Sweden 0%
  dividend caps, and Bolivia's no-confirmed-exit-tax position.
  Trigger on Bolivia cross-border, non-resident, treaty, expat,
  dividend withholding. Source-cited draft.
jurisdiction: BO
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
---

# Bolivia cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the SIN portal
(impuestos.gob.bo, SIAT) and the PwC Worldwide Tax Summaries Bolivia
corporate chapter (reviewed 21 July 2026). Currency: boliviano (BOB).
Treaty article details are **needs-sources** — confirm each DTT text
before applying a reduced rate.

## 2. Who the rules apply to

- **Non-resident companies** deriving Bolivian-source income: taxed
  through the source principle — a non-resident with Bolivian-source
  income is in scope whether or not it has a registered branch; the
  Bolivian payer generally withholds.
- **Non-resident individuals** working in Bolivia: 16% withholding on
  fees for activities performed in Bolivian territory (this rate
  covers the 3% transaction tax + 13% RC-IVA components — PwC Bolivia,
  read 2026-10-24).
- **Bolivian residents receiving foreign-source income**: Bolivia does
  not tax foreign-source income of residents (territorial system);
  there is no confirmed exit tax on emigration (**needs-sources**).

## 3. Withholding and treaty table

| Payment to non-resident | Rate | Notes / source |
|---|---|---|
| Dividends / branch profit remittance | 12.5% | PwC Bolivia withholding, read 2026-10-24 |
| Interest | 12.5% | PwC Bolivia, read 2026-10-24 |
| Royalties | 12.5% | PwC Bolivia, read 2026-10-24 |
| Services (fully performed in Bolivia) | 12.5% | PwC Bolivia, read 2026-10-24 |
| Partially-performed activities (telecom, insurance, transport, film) | 2.5% | PwC Bolivia, read 2026-10-24 |
| Non-domiciled individuals working in Bolivia | 16% | = 3% IT + 13% RC-IVA; PwC Bolivia, read 2026-10-24 |
| Dividends to Spanish holding (>25%, beneficial owner) | 10% | Spain DTT via PwC Bolivia, read 2026-10-24 |
| Dividends to Swedish holding (>25%, beneficial owner) | 0% | Sweden DTT via PwC Bolivia, read 2026-10-24 |

Treaty network in force (PwC Bolivia, read 2026-10-24): Andean
Community (Colombia, Ecuador, Peru), Argentina, France, Germany,
Spain, Sweden, United Kingdom. Dividends paid to **Bolivian residents**
are not taxable.

## 4. Tax base and computation

Withholding applies to the **gross** payment. There is no general
expense-deduction route for a non-resident without a registered
Bolivian presence — a non-resident providing services into Bolivia is
usually caught at 12.5% gross (or 2.5% for the partially-performed
list). Registering a branch switches the analysis to IUE 25% on the
branch's Bolivian-source profit plus 12.5% on the remittance.

## 5. Deadlines

- WHT remittance: monthly per the SIN vencimientos calendar (exact day
  per taxpayer group: confirm in SIAT — **needs-sources**).
- No exit-tax filing confirmed (**needs-sources**).
- Treaty relief: apply at source with beneficial-ownership
  documentation; refund route through SIN if over-withheld (procedure
  details **needs-sources**).

## 6. Penalties and interest

Failure to withhold makes the Bolivian payer jointly liable for the
tax plus Codigo Tributario interest/penalties (article-level amounts
**needs-sources**; audit mechanics in bolivia-corporate-income-tax).

## 7. Worked examples

**Example 1 — royalty to a foreign licensor.** A Bolivian company
pays BOB 200,000 of royalties to a non-resident licensor in a
non-treaty state: 12.5% withholding on the gross.

```oa-check
name: royalty WHT 12.5 percent
inputs:
  royalty: 200000
  wht: 12.5
steps:
  - wht_due: royalty * pct(1, wht)
  - net: royalty - wht_due
expected:
  wht_due: 25000.00
  net: 175000.00
```

**Example 2 — dividend to a Spanish parent.** A Bolivian company
distributes BOB 500,000 to a Spanish parent holding >25% and proving
beneficial ownership: treaty caps dividend WHT at 10% instead of 12.5%.

```oa-check
name: dividend Spain treaty 10 vs domestic 12.5
inputs:
  dividend: 500000
  domestic: 12.5
  treaty: 10
steps:
  - domestic_wht: dividend * pct(1, domestic)
  - treaty_wht: dividend * pct(1, treaty)
  - saving: domestic_wht - treaty_wht
expected:
  domestic_wht: 62500.00
  treaty_wht: 50000.00
  saving: 12500.00
```

## 8. Ask the client first

1. Is the counterparty jurisdiction on Bolivia's treaty list, and can
   beneficial ownership (>25% for the Spain/Sweden dividend caps) be
   documented?
2. Are imported services on the 2.5% partially-performed list or the
   12.5% general list — and was the right rate withheld?
3. Are visiting non-domiciled individuals being paid gross (16% WHT
   obligation sits on the Bolivian payer)?
4. Is a Bolivian branch/PE being carried without registration —
   remittance exposure at 12.5% on the head-office profit?

## 9. Sources

- [SIN — Servicio de Impuestos Nacionales](https://www.impuestos.gob.bo/) — read 2026-10-24.
- [SIN — SIAT](https://siat.impuestos.gob.bo/) — read 2026-10-24.
- [PwC — Bolivia withholding taxes](https://taxsummaries.pwc.com/bolivia/corporate/withholding-taxes) — read 2026-10-24 (WHT rates, treaty network, Spain/Sweden caps).
- [PwC — Bolivia corporate overview](https://taxsummaries.pwc.com/bolivia/corporate) — read 2026-10-24.
- Treaty texts (DTT Spain, Sweden, UK, Germany, France, Argentina; Andean Community decisions) — **needs-sources**.

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
