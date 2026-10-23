---
name: cu-transfer-pricing
description: >
  Cuba transfer pricing reference for 2026. Covers the arm's-length and
  related-party rules of Law No. 113 of 2012 (Ley del Sistema Tributario),
  the ONAT assessment powers over transactions between linked parties, the
  absence of a published master/local documentation regime, the 2024
  private-economy expansion (Decree-Law 46/2021 MIPYMEs and TCPs) that made
  cross-border related-party flows material, and Pillar Two status. Trigger
  on Cuba transfer pricing, partes vinculadas, precios de transferencia,
  ONAT adjustment, Ley 113. Source-cited draft.
jurisdiction: CU
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Cuba transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 23 October 2026: the Gaceta Oficial de la
República de Cuba portal (gacetaoficial.gob.cu, HTTP 200), the Ministerio de
Economía y Planificación (mep.gob.cu, HTTP 200), and the MINJUS commercial
registry page (minjus.gob.cu, HTTP 200). The core statute is Law No. 113 of
2012 (Ley del Sistema Tributario), amended by the Tax Codes (Decree-Law 34
of 2021, Gaceta Oficial Extraordinaria No. 81 of 2021) and annually by the
State Budget Law. Currency Cuban peso (CUP). ONAT (Oficina Nacional de
Administración Tributaria) administers.

**Source status caveat:** the consolidated Spanish text of Ley 113 and the
2021 Tax Codes did not resolve from this workstation during the drafting
pass (gacetaoficial article paths 404; onat.gob.cu connection-refused).
Every figure and rule below is carried from the pack's existing
source-cited skills (`cu-corporate-income-tax`, `cu-income-tax`,
`cu-tax-overview`, tier 2) or marked **needs-sources**. No figure in this
skill is invented; unverified items are flagged and must be confirmed
against the Gaceta Oficial text before tier-1 promotion.

## 2. Who the rules apply to

Cuba has no standalone transfer-pricing code. The arm's-length principle
operates through the general income-determination rules of Ley 113:

- **Linked-party transactions.** Taxable profit for entities subject to the
  Impuesto sobre Utilidades (35% general rate — see `cu-corporate-income-tax`)
  is computed on real income less deductible expenses. ONAT may restate
  amounts where recorded consideration does not reflect the transaction's
  reality; the specific related-party article numbers of Ley 113 are
  **needs-sources** (statute text not retrievable this pass).
- **State enterprises and joint ventures.** Foreign-investment entities
  (Ley No. 118 de la Inversión Extranjera) routinely transact with foreign
  partners; pricing of inputs, management fees and financing between the
  Cuban entity and its foreign partner sits directly in the 35% (or 15%
  joint-venture) base.
- **Private sector (MIPYME / TCP).** Since Decree-Law 46/2021 and the 2021
  Tax Codes, private MIPYMEs file sworn declarations (Declaración Jurada)
  and are exposed to the same ONAT restatement powers; imports priced by a
  related foreign supplier are the common flash point.

## 3. Rates and thresholds

| Item | Rate / threshold | Source (as_of 2026-10-23) |
|---|---|---|
| Impuesto sobre Utilidades (base the TP adjustment hits) | 35% general | Ley 113, carried from `cu-corporate-income-tax` (tier 2) |
| Foreign-investment joint-venture rate | 15% | Ley 118, carried from `cu-corporate-income-tax` (approx — confirm) |
| Natural-resource exploitation rate | up to 50% | Ley 113, carried from `cu-corporate-income-tax` (approx — confirm) |
| Master/local file documentation requirement | none published | **needs-sources** |
| CbCR / Pillar Two | no published regime | **needs-sources** |

## 4. Filings and deadlines

- No separate transfer-pricing return is published; related-party terms are
  exposed through the annual Declaración Jurada (corporate sworn declaration
  commonly cited as due 31 March — carried from `cu-corporate-income-tax`,
  approx — confirm) and quarterly advance payments.
- ONAT audits follow the general assessment procedure of Ley 113; specific
  TP audit windows are **needs-sources**.

## 5. Penalties and interest

General Ley 113 infractions apply (late filing, under-declaration); the
specific percentage figures are **needs-sources** — the pack's existing
Cuba skills do not carry the penalty division, and the statute text did not
resolve this pass. Do not quote a Cuba TP penalty figure without confirming
against the Gaceta Oficial text.

## 6. Worked examples

**Example 1 — related-party import overpricing.** A Cuban MIPYME buys
inventory from its own foreign shareholder for CUP 1,000,000 when the
arm's-length price is CUP 700,000. ONAT restates the deduction down by
300,000, raising taxable profit; at the 35% rate the additional tax is
105,000.00 (before penalties/interest).

```oa-check
name: MIPYME import restatement CUP 300,000
inputs:
  price: 1000000
  arm_length: 700000
steps:
  - uplift: price - arm_length
  - tax: uplift * 0.35
expected:
  tax: 105000.00
```

**Example 2 — management fee stripped from a joint venture.** A foreign
partner charges a Cuban joint venture (15% regime) a management fee of
CUP 200,000 that ONAT finds unsupported; the fee is non-deductible, so
additional tax = 200,000 × 15% = 30,000.00.

```oa-check
name: JV management fee disallowance CUP 200,000
inputs:
  fee: 200000
steps:
  - tax: fee * 0.15
expected:
  tax: 30000.00
```

## 7. Ask the client first

1. Is the counterparty a related party (shareholder, affiliate, family)?
2. What is the entity's regime — state enterprise, Ley 118 joint venture
   (15%), MIPYME, or TCP?
3. Are imports/exports priced by a related foreign supplier or trader?
4. Is there transfer documentation at all (invoices, comparables)?
5. Which Budget Law year governs the rates in force for the filing year?

## 8. Sources

- [Gaceta Oficial de la República de Cuba (portal)](http://www.gacetaoficial.gob.cu/) — read 2026-10-23 (HTTP 200; article-level PDF paths for Ley 113 / DL 34-2021 did not resolve — needs-sources).
- [Ministerio de Economía y Planificación](https://www.mep.gob.cu/) — read 2026-10-23.
- [MINJUS — Registro Mercantil](https://www.minjus.gob.cu/es/servicios/registro-mercantil) — read 2026-10-23.
- Pack skills carried: `cu-corporate-income-tax`, `cu-income-tax`, `cu-tax-overview` (tier 2, read 2026-07-13).

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
