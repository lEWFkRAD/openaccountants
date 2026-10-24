---
name: co-transfer-pricing
description: >
  Use this skill whenever asked about Colombian transfer pricing (precios de transferencia, DIAN, formulario 120, vinculados del exterior, paraísos fiscales, zonas francas, estudio local, declaración informativa). Trigger on phrases like "precios de transferencia Colombia", "DIAN formulario 120", "vinculado exterior", "paraíso fiscal Colombia operaciones", "arm's length Colombia", "transfer pricing Colombia", "estudio local DIAN". Covers who is obligated, the ET arts. 260-1 to 260-10 framework, methods, the annual informative return on Form 120, documentation, penalties, and the decree list published by DIAN. Tax year 2026 draft.
jurisdiction: CO
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Colombia transfer pricing

## 1. Who applies

Per DIAN's own FAQ, the regime binds income-tax taxpayers that (a) have linked parties abroad (vinculados del exterior), in free-trade zones, or counterparties in tax havens, and (b) carried out operations with them during the tax year. Foreign-resident groups act through branches/permanent establishments in Colombia. The statutory framework is Estatuto Tributario arts. 260-1 to 260-10, as amended by Ley 1607 de 2012 and later reforms.

## 2. Rates and thresholds

- No "rate": the regime re-prices related-party transactions to arm's length; the ordinary corporate rate (35%, surcharges, 15% METR floor) applies to the adjusted base — see `co-corporate-income-tax`.
- The UVT gross-income threshold that triggers the *informative return* obligation sits in the annual regulations; the current-year figure is **needs-sources** (verify against the DIAN TP normatividad page before relying on a number).
- Regime decrees published on DIAN's [TP normatividad page](https://www.dian.gov.co/Transaccional/Paginas/Normatividad_PT.aspx) (read 2026-10-24): Decretos 1791/2007, 2193/2013, 2972/2013, 3026/2013, 3027/2013, 3028/2013, 3030/2013, 1966/2014, 2095/2014, 2120/2017, 0627/2014.

## 3. Base

- Transactions with: foreign linked parties; Colombian free-zone linked parties; any counterparty located/resident in a tax haven (regardless of linkage).
- Methods (ET art. 260-3): CUP, resale price, cost-plus, TNMM, profit split, plus the market-realisation method for intangibles/going-concern transfers.
- Adjustments flow into the ordinary income-tax return; the TP informative return is a separate virtual filing on **Form 120** signed with electronic signature (DIAN FAQ, read 2026-10-24).

## 4. Deadlines

- Form 120 informative return: annual, due in July of the following year per the DIAN calendar (staggered by NIT) — confirm the exact 2026 date on the [DIAN calendar page](https://www.dian.gov.co/Paginas/CalendarioTributario.aspx).
- Supporting local/master documentation must exist at filing; DIAN can request it in audit.

## 5. Penalties and interest

- Non-filing or error in the TP informative return: 5% of the amount of the operations omitted/understated, capped at 100 UVT minimum tiers per ET art. 651-1; corrections without a DIAN requirement get reduced penalties.
- Re-pricing adjustments: plus tax, plus interest at the ET art. 635 rate.

## 6. Cross-border

- Treaty MAP available with Colombia's treaty partners — see `co-cross-border` and DIAN's [treaty page](https://www.dian.gov.co/normatividad/convenios/paginas/conveniostributariosinternacionales.aspx) (37 instruments listed, read 2026-10-24).
- Payments to tax-haven counterparties face the regime even without linkage; also check the thin-cap and exchange-control declarations.

## 7. Worked examples

**Example 1 — TNMM margin adjustment.**

```oa-check
name: Distributor sales 800,000,000 COP, costs 600,000,000, arm's-length operating margin 5% of sales
inputs:
  sales: 800000000
  costs: 600000000
  al_margin_pct: 5
steps:
  - actual_op: sales - costs
  - al_op: sales * 0.05
  - adjustment: al_op - actual_op
expected:
  actual_op: 200000000
  al_op: 40000000
  adjustment: -160000000
```

(The negative adjustment means the declared margin exceeds the arm's-length margin; DIAN re-prices the cost of goods upward by 160,000,000 COP.)

**Example 2 — cost-plus manufacture.**

```oa-check
name: Contract manufacturer cost base 300,000,000 COP, arm's-length mark-up 8%
inputs:
  cost_base: 300000000
  markup_pct: 8
steps:
  - markup: cost_base * 0.08
  - price: cost_base + markup
expected:
  markup: 24000000
  price: 324000000
```

## 8. Ask the client

1. Which linked parties abroad / free-zone / tax-haven counterparties, and what transaction types?
2. Total annual related-party volume (drives return obligation and penalty exposure)?
3. Existing local/master file and benchmarking study?
4. Any APA or prior DIAN TP audit?
5. Advance rulings (concepto DIAN) relied on?

## 9. Sources

- [DIAN — Precios de transferencia normatividad](https://www.dian.gov.co/Transaccional/Paginas/Normatividad_PT.aspx) — read 2026-10-24 (decree list verified).
- [DIAN — Manuales de presentación de precios de transferencia](https://www.dian.gov.co/Transaccional/Paginas/Manuales-presentacion-precios-de-transferencia.aspx) — read 2026-10-24.
- [DIAN — Preguntas frecuentes declaración de precios de transferencia (PDF)](https://www.dian.gov.co/transaccional/guaservicioslinea/preguntas_frecuentes_declaracion_pt.pdf) — read 2026-10-24 (Form 120, obligation conditions, signature rules verified from the PDF text).
- [DIAN — Calendario Tributario](https://www.dian.gov.co/Paginas/CalendarioTributario.aspx) — read 2026-10-24.
- ET arts. 260-1 to 260-10, 651-1 — gazette text **needs-sources** (pgn.gov.co unresolved 2026-10-24).

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
