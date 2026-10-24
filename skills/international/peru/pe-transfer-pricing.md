---
name: pe-transfer-pricing
description: >
  Peru transfer pricing reference for 2026. Income Tax Law Art. 32-A
  requires market value for transactions with linked parties (partes
  vinculadas) and lists six accepted methods — CUP, resale price, cost
  plus, profit split, residual profit split, transactional net margin
  — with the Estudio Técnico documentation duty, informative returns,
  and Spanish-translation/retention rules from the TUO (D.S. 139-2014-EF
  consolidated text on SUNAT). Covers the linked-party definition,
  30% interest rate for related-party loans, SUNAT Tax Code fines and
  interest. Trigger on Peru transfer pricing, partes vinculadas,
  estudio técnico, métodos de precios de transferencia, SUNAT TP.
  Source-cited draft.
jurisdiction: PE
category: transfer-pricing
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-23
version: 0.1
---

# Peru transfer pricing

## 1. Who this applies to

- Domiciled companies (second-category income, 29.5% general rate — see pe-corporate-income-tax) transacting with non-domiciled or linked parties.
- Art. 32-A applies to operations with **partes vinculadas** under the linkage tests in the same article (control, direct or indirect participation of 30% or more, management links, and the deemed-linkage cases including low-tax jurisdictions).
- Non-domiciled parties with Peruvian-source income are pulled into the market-value rule through Art. 32 (general market-value definition) and the source rules (Art. 9–10).

## 2. Rates and thresholds

| Item | Amount | Source |
|---|---|---|
| Corporate rate the adjustment lands on | 29.5% general | Income Tax Law (see pe-corporate-income-tax; TUO D.S. 139-2014-EF) |
| Interest from non-domiciled lender, linked or via tax haven | 30% WHT | Income Tax Law Art. 54(c) (Cap. VII, SUNAT TUO PDF, read 2026-10-23) |
| Documentation retention | 5 years or prescription period, whichever is longer; Spanish translation required | Art. 32-A (Cap. V TUO PDF, read 2026-10-23) |

**needs-sources:** the UIT-denominated filing thresholds for the Estudio Técnico / informative returns (local file, master file, CbCR) did not resolve from the chapter PDFs this pass — the amounts are set by the Reglamento (R.M. 122-2018/SUNAT); confirm current UIT values with a Peruvian CPA before quoting.

## 3. The base: market value and the six methods

Art. 32-A (read from the SUNAT TUO chapter PDF, 2026-10-23) requires market value for linked-party transactions and lists the methods, to be applied choosing the most appropriate to the economic reality:

1. **Precio comparable no controlado** (CUP)
2. **Precio de reventa** (resale price — resale price to an independent multiplied by one minus the gross-margin normally earned in comparable transactions)
3. **Costo plus** (cost plus — cost multiplied by one plus the cost-plus margin normally earned in comparable transactions; margin = gross profit / cost of sales)
4. **Partición de utilidades** (profit split — global profit split in the proportion independent parties would have used, weighing sales, costs, risks, assets, functions)
5. **Residual de partición de utilidades** (residual profit split — minimum return via methods 1–4/6, residual allocated by significant intangibles)
6. **Margen neto transaccional** (transactional net margin — profitability on assets, sales, costs, cash flow)

- Using a method outside the list requires filing the supporting documentation plus the economic, financial and technical reasons (Art. 32-A, read 2026-10-23).
- Documentation: per-transaction supporting documentation and a **Estudio Técnico** backing the TP calculation, kept for the prescription period, translated into Spanish if needed; informative returns (declaraciones juradas informativas) per the Reglamento.
- SUNAT may exempt specific cases from the DJI/Estudio Técnico duties; for goods sales the market value may not be below the computed cost.

## 4. Deadlines and mechanics

- TP analysis and Estudio Técnico must exist by the annual return deadline (March–April per SUNAT's annual calendar; **needs-sources:** exact 2026 dates are calendar resolutions, not in the chapter PDFs).
- Informative returns (local/master/CbCR) per the Reglamento deadlines.
- SUNAT can assess TP adjustments under the Tax Code assessment powers; Art. 32-A adjustments recompute second-category income at 29.5%.

## 5. Penalties and interest

- **Interest:** underpaid tax accrues the ITMC (interés moratorio) daily-compounded from the due date (Tax Code Art. 176, read 2026-10-23).
- **Fines:** Tax Code Art. 210 (read 2026-10-23): failure to keep/support documentation and failure to file informative returns are fined as formal-infractions; the base fine for non-filing where the taxpayer is not otherwise obligated is **40% of the UIT**; graduated percentages of net income/UIT apply for other infractions.
- Coercive collection (cobranza coactiva) on exigible debt (Tax Code Art. 115).

## 6. Cross-border notes

- Interest paid to a non-domiciled lender is withheld at **30%** when the parties are linked or the payment comes from/via non-cooperative or low-tax jurisdictions (Art. 54(c)); the non-linked rate is lower — confirm per case.
- Technical assistance is Peruvian-source when used economically in Peru (Art. 9(j)) — TP and WHT interact on the same fee.
- Treaty network: SUNAT publishes the DTT list on a campaign page that did not resolve this pass — **needs-sources**; treaty relief on interest/royalties must be confirmed per counterparty.

## 7. Worked examples

**Example 1 — related-party goods import re-priced.** A Lima importer (29.5%) buys from its non-domiciled parent at S/ 800,000; SUNAT prices the goods at S/ 640,000 arm's length, disallowing S/ 160,000 of cost.

```oa-check
name: PE TP uplift to taxable income
inputs:
  paid: 800000
  arm_length: 640000
  rate: 0.295
steps:
  - uplift: paid - arm_length
  - extra_tax: uplift * rate
expected:
  uplift: 160000
  extra_tax: 47200
```

**Example 2 — related-party loan interest WHT.** A domiciled company pays S/ 500,000 interest to its non-domiciled 40% shareholder. Linked-party rate 30%.

```oa-check
name: PE linked-party interest WHT
inputs:
  interest: 500000
  rate: 0.30
steps:
  - wht: interest * rate
  - net: interest - wht
expected:
  wht: 150000
  net: 350000
```

## 8. Ask the client

- Linkage map: ownership percentages (30% test), common directors, related low-tax entities.
- Whether an Estudio Técnico exists for each transaction class, and whether it is translated and retained.
- Function/asset/risk profiles per entity — the method choice depends on them.
- Loan documentation: purpose, rates, lender residence (30% vs lower rate).

## 9. Sources

- [SUNAT — Ley del Impuesto a la Renta, Cap. V (Art. 32, 32-A TUO text)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf) — read 2026-10-23 (methods, documentation, retention).
- [SUNAT — Ley del Impuesto a la Renta, Cap. VII (Arts. 53–54)](https://www.sunat.gob.pe/legislacion/renta/ley/capvii.pdf) — read 2026-10-23 (non-domiciled rates).
- [SUNAT — Código Tributario, Libro segundo (Arts. 115, 176)](https://www.sunat.gob.pe/legislacion/codigo/libro2/libro.pdf) and [Libro cuarto (Art. 210)](https://www.sunat.gob.pe/legislacion/codigo/libro4/libro.pdf) — read 2026-10-23 (interest, fines, coactiva).
- [SUNAT — legislación del Impuesto a la Renta index](https://www.sunat.gob.pe/legislacion/renta/index.html) — read 2026-10-23.

**Source status:** methods, documentation duties, 30% linked-interest rate, interest/fine mechanics are official (TUO chapter PDFs). UIT thresholds and the treaty list are needs-sources — flagged, not invented.

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
