---
name: ec-cross-border
description: >
  Ecuador cross-border tax reference for 2026. Covers residence and
  worldwide taxation for residents versus source taxation for
  non-residents, withholding on dividends (25% on 40% of the dividend),
  interest and royalties to non-residents, the Andean Community Decision
  578 tie-break, the treaty network, ISD on outbound payments, and exit
  position for individuals. Trigger on Ecuador treaty, non-resident
  withholding, salida de divisas, ISD, retención en la fuente.
  Source-cited draft.
jurisdiction: EC
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Ecuador cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the SRI portal
(sri.gob.ec, HTTP 200), the Asamblea Nacional LRTI/Código Tributario page
(archivo.asambleanacional.gob.ec, HTTP 200) and the LRTI reform PDF
(HTTP 200), and the pack's tier-2 skills (`ec-corporate-income-tax`,
`ec-tax-overview`) whose withholding figures trace to the LRTI via the
PwC tax-summaries mirror. Currency US dollar (dollarized). SRI administers.

## 2. Charging scope

- **Residents** (individuals and companies) are taxed on worldwide income;
  **non-residents** on Ecuador-source income (carried from `ec-tax-overview`).
- A company is Ecuador-resident if incorporated or with effective
  administration in Ecuador (LRTI pattern; article **needs-sources**).
- **No general individual exit tax** is carried in the pack sources;
  capital-gains crystallisation on departure is **needs-sources**.

## 3. Withholding on outbound flows

| Item | Rate / rule | Source (as_of 2026-10-23) |
|---|---|---|
| Dividends to non-residents | 25% applied to 40% of the dividend (effective ~10%) | LRTI, carried from `ec-corporate-income-tax` |
| Interest to non-residents | 25% (0% on registered foreign loans within authorized limits) | LRTI, carried from `ec-corporate-income-tax` |
| Royalties / technical services to non-residents | 25% | LRTI, carried from `ec-corporate-income-tax` |
| Domestic withholding on local payments | ~1%–10% by payment type | Reglamento + SRI resolutions (approx — confirm by type) |
| Andean Community residents | CAN Decision 578 residence tie-break | carried from `ec-corporate-income-tax` |
| Treaty network | DTTs in force with a growing partner list; relief only treaty-by-treaty | **needs-sources** (in-force list not verified this pass) |
| ISD (salida de divisas) | percentage tax on certain outbound payments/currency outflow; rate varies by era | carried from pack (`ecuador-tax-optimization`) — **needs-sources** current rate |

## 4. Filings and deadlines

- Withholding is remitted by the Ecuadoran payer on the periodic SRI
  returns (monthly/semi-monthly by taxpayer category — confirm schedule).
- Non-residents with Ecuador-source income generally have no annual return
  when fully withheld at source; a return is needed for refunds or
  unwithheld income (confirm — needs-sources).

## 5. Penalties and interest

General Código Tributario penalties for late or wrong withholding;
percentages **needs-sources**.

## 6. Worked examples

**Example 1 — dividend to a foreign parent.** A Quito company distributes
USD 500,000 to its non-resident parent. Withholding = 25% × (40% ×
500,000) = 50,000.00 (effective 10%).

```oa-check
name: Dividend WHT to non-resident USD 500,000
inputs:
  dividend: 500000
steps:
  - base: dividend * 0.40
  - wht: base * 0.25
expected:
  wht: 50000.00
```

**Example 2 — royalty to a non-resident licensor.** A Guayaquil licensee
pays a USD 200,000 royalty to a non-resident licensor with no treaty
relief: withholding = 200,000 × 25% = 50,000.00. A treaty or CAN-relief
review may reduce this — confirm the partner country first.

```oa-check
name: Royalty WHT USD 200,000
inputs:
  royalty: 200000
steps:
  - wht: royalty * 0.25
expected:
  wht: 50000.00
```

## 7. Ask the client first

1. Is the recipient country a treaty partner or Andean Community member?
2. Is the loan registered with SRI (0% interest WHT window)?
3. Does ISD apply to the outbound flow at the current rate — confirm the
   rate in force for the payment date.
4. Is the payer inside the domestic withholding grid for the payment type?
5. Is the individual becoming non-resident — what crystallises on exit?

## 8. Sources

- [SRI portal](https://www.sri.gob.ec/) — read 2026-10-23.
- [Asamblea Nacional — LRTI / Código Tributario](https://archivo.asambleanacional.gob.ec/index.php/ley-de-regimen-tributario-interno-codigo-tributario) — read 2026-10-23 (HTTP 200).
- [LRTI reform law (PDF)](https://www.asambleanacional.gob.ec/es/system/files/ley_reformatoria_a_la_ley_de_regimen_tributario_interno_y_a_la_ley_reformatoria_para_la_equidad_tributaria_del_ecuador.pdf) — read 2026-10-23 (HTTP 200).
- Pack skills carried: `ec-corporate-income-tax`, `ec-tax-overview`, `ecuador-tax-optimization` (tier 2).

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
