---
name: cr-transfer-pricing
description: >
  Use this skill whenever asked about Costa Rica transfer pricing (precios de transferencia, relaciones especiales, LIR artículos 1018 a 1028, Ley 9635, estudio local, DICEX/DGT). Trigger on phrases like "precios de transferencia Costa Rica", "relaciones especiales Costa Rica", "arm's length Costa Rica", "artículo 1018 LIR", "transfer pricing Costa Rica", "operaciones partes relacionadas Costa Rica". Covers the Costa Rican TP regime introduced by Ley 9635 in the LIR (arts. 1018-1028): who applies, special-relationship tests, methods, documentation, penalties. Tax year 2026 draft; article text needs-sources at consolidated level, regime existence verified via Ley 9635.
jurisdiction: CR
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Costa Rica transfer pricing

> **Source status.** The TP rules live in LIR arts. 1018–1028, inserted by
> Ley 9635 (2018). The consolidated article text could not be fetched from
> an official server-rendered page in this environment (SCIJ JS shell;
> hacienda.go.cr unreachable 2026-10-24), so article-level quotes are
> **needs-sources**; the regime itself and its OECD alignment are confirmed
> by secondary sources (PwC, read 2026-10-24).

## 1. Who applies

Income-tax taxpayers (corporate and individual) carrying out transactions
with **related parties abroad** within a "special relationship" (relaciones
especiales) as defined in LIR art. 1019 — control, management, or ≥25%
capital links (direct or indirect), spouse/relative links, and other
statutory ties. The regime follows the OECD Guidelines.

## 2. Rates and thresholds

- No rate: transactions must be priced at arm's length (valores de mercado); DGT may re-price and assess the difference at the ordinary corporate rate (30%) — see `cr-corporate-income-tax`.
- No published small-transaction exemption threshold verified — **needs-sources**; treat all material cross-border related-party flows as in scope.

## 3. Base and methods

- Methods (LIR art. 1020, OECD-aligned): CUP, resale price, cost-plus, TNMM, profit split, and other methods adapted to the transaction.
- Documentation: local file (estudio de precios de transferencia) supporting the analysis; DGT can request it during audit. Costa Rica does not operate a full BEPS Action 13 master-file/CbCR package for all groups — verify current DGT resolutions.

## 4. Deadlines

- TP analysis must exist to support the annual income-tax return (D-102 band); no separate standalone TP return verified — **needs-sources**.
- Advance pricing agreements (acuerdos anticipados) available under the Código (Ley 4755 arts. 4 bis and procedure) — verify current practice.

## 5. Penalties and interest

- Re-pricing adjustments: additional tax plus interest under Ley 4755; understatement fines 10%–100% depending on intent.
- Failure to maintain supporting documentation feeds the understatement presumption.

## 6. Cross-border

- MAP available only with treaty partners (narrow network — see `cr-cross-border`).
- TP interacts with the territorial principle: re-characterising income can create or destroy CR-source income.

## 7. Worked examples

**Example 1 — cost-plus import price.**

```oa-check
name: Import from related manufacturer, cost base CRC 500,000,000, arm's-length mark-up 10%
inputs:
  cost_base: 500000000
  markup_pct: 10
steps:
  - markup: cost_base * 0.10
  - price: cost_base + markup
expected:
  markup: 50000000
  price: 550000000
```

**Example 2 — TNMM margin on a distribution fee.**

```oa-check
name: Distributor sales CRC 200,000,000, arm's-length operating margin 5%
inputs:
  sales: 200000000
  margin_pct: 5
steps:
  - target_margin: sales * 0.05
expected:
  target_margin: 10000000
```

## 8. Ask the client

1. Which related parties abroad, and ownership/management links (special-relationship test)?
2. Transaction types and volumes per year?
3. Existing TP study and benchmarking?
4. Any DGT audit or requerimiento open?
5. Treaty position if a MAP is contemplated?

## 9. Sources

- [Ley 9635 — PGR text](https://www.pgrweb.go.cr/DOCS/NORMAS/1/NOVIGEN/L/2010-2019/2015-2019/2018/156A8/127E2C.HTML) — read 2026-10-24 (the fetched page carries the IVA title; the TP articles sit in the same law's income-tax title).
- [PwC Tax Summaries — Costa Rica](https://taxsummaries.pwc.com/costa-rica/corporate/taxes-on-corporate-income) — read 2026-10-24 (regime confirmation).
- LIR arts. 1018–1028 consolidated text — **needs-sources** (SCIJ JS-rendered 2026-10-24).

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
