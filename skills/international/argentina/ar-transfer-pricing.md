---
name: ar-transfer-pricing
description: >
  Argentina transfer pricing reference for 2026. Covers the
  fair-value (valor razonable) rule for related-party transactions
  under the Income Tax Law as amended by Ley 27.430, the
  comparable-uncontrolled-price / resale-price / cost-plus /
  profit-split / residual methods, the import/export reference-price
  overlay for related-party goods, the withholding overlay (35%
  deemed-margin on interest and royalties, 31.5% software), and the
  20+ treaty network. Trigger on Argentina transfer pricing, precio
  de transferencia, valor razonable, ART, beneficiarios del exterior.
  Source-cited draft.
jurisdiction: AR
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Argentina transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the ARCA portal
(argentina.gob.ar), the InfoLeg statute portal (infoleg.gob.ar —
Ley 27.430 landing page served; consolidated text not machine-
readable this pass), and the existing AR pack skills (figures carried
forward with their citations). Currency: Argentine peso (ARS).

**Source status caveat:** the article-level fair-value text (Ley
20.628 t.o. arts. 15–17 as amended by Ley 27.430), the current
documentation requirements (master/local file, CbCR thresholds and
deadlines under RG AFIP 4717/4850) and the current reference-price
regime for related-party imports (resolutions of the former MPYD,
RG 4582/4819) could not be machine-read this pass — **needs-sources**.
Method names and rates below are carried from the existing pack.

## 2. Who the rules apply to

- **Argentine taxpayers** (Ganancias taxpayers, including PE's) whose
  transactions with **related parties** — foreign affiliates,
  entities in low/none-tax jurisdictions, permanent establishments —
  depart from **fair value** (valor razonable): ARCA may revalue to
  the arm's-length amount under the methods in art. 15 (Ley 20.628
  t.o., as amended by Ley 27.430 — sections needs-sources).
- **Related-party importers** additionally face reference-price
  (precios de referencia) rules for certain goods from related
  parties (regime status after 2023 changes: **needs-sources**).
- **Cross-border payments** (interest, royalties, services) to
  non-residents carry the withholding overlay in section 3.

## 3. The rules (methods and overlay table)

| Rule | Content | Source |
|---|---|---|
| Methods (in order of the law) | Comparable uncontrolled price; resale price; cost plus; profit split; residual profit split | Ley 20.628 t.o. art. 15 (Ley 27.430) — needs-sources |
| Corporate rates | Tiered 25% / 30% / 35% (top tier above ARS ~1.017bn, indexed) | ar-corporate-income-tax |
| Interest WHT to non-residents | 35% on a deemed profit margin (commonly 43%) → effective ~15.05%; treaty-reducible | ar-corporate-income-tax |
| Royalty WHT to non-residents | 35% on deemed margin; effective ~31.5% software, ~28% trademark/technical assistance | ar-corporate-income-tax |
| Dividend WHT | 7% on distributions and branch remittances (post-2018 profits) | ar-corporate-income-tax |
| Documentation | Master/local file + CbCR thresholds per RG AFIP 4717/4850 — needs-sources | needs-sources |
| Treaty network | 20+ CDIs may reduce WHT | ar-corporate-income-tax |

## 4. Tax base and computation

A revaluation adjusts the Ganancias base at the applicable tier
(25/30/35%). Separately, WHT on cross-border services/royalties/
interest is computed on a **deemed margin** of the gross payment
(e.g. 43% of gross interest × 35% = 15.05% effective), so an
arm's-length adjustment and the withholding overlay can both bite on
the same flow. Compute the revaluation charge at the top marginal
tier when the group is in tier 3, and gross-up the WHT where the
contract shifts it.

## 5. Deadlines

- **Ganancias return (F.1585):** annual, mid-year following the
  fiscal year (exact date by year — needs-sources).
- **TP documentation (RG 4717/4850):** local file / master file
  information regimes tied to the return period — **needs-sources**
  for the 2026 thresholds and dates.
- **WHT (SIRCREB/SICORE):** monthly remittance per ARCA calendars.

## 6. Penalties and interest

Understatement runs through the Ley 27.430 libro II penal regime
(fines plus ARCA active interest); documentation gaps carry specific
fines (RG 4717/4850 — amounts needs-sources).

## 7. Worked examples

**Example 1 — related-party import revaluation.** An Argentine
company imports goods from its parent at ARS 1,000,000; the
arm's-length price is ARS 1,200,000. ARCA revalues the deduction
down, adding ARS 200,000 to the Ganancias base, taxed at the 25% or
35% tier.

```oa-check
name: import uplift 200k at 25 and 35 percent
inputs:
  arm: 1200000
  invoiced: 1000000
  tier1: 25
  tier3: 35
steps:
  - disallowed: arm - invoiced
  - tax_25: disallowed * pct(1, tier1)
  - tax_35: disallowed * pct(1, tier3)
expected:
  disallowed: 200000.00
  tax_25: 50000.00
  tax_35: 70000.00
```

**Example 2 — software royalty to the foreign parent.** The Argentine
licensee pays ARS 800,000 of software royalties to a related
non-resident; the effective WHT on software royalties is ~31.5%
(35% on the deemed margin) absent treaty relief.

```oa-check
name: software royalty 800k effective 31.5 percent
inputs:
  royalty: 800000
  eff_rate: 31.5
steps:
  - wht: royalty * pct(1, eff_rate)
expected:
  wht: 252000.00
```

## 8. Ask the client first

1. Which related-party flows ran in the year (goods, services,
   royalties, loans), and at what prices on each side of the border?
2. Is there a local file / master file / CbCR package, and does it
   use one of the statutory methods in the law's order?
3. Are any counterparty entities in low/none-tax jurisdictions
   (stricter scrutiny, non-deductibility risk on certain payments)?
4. Are treaty rates being applied on WHT with residence
   certificates, and are SIRCREB filings current?

## 9. Sources

- [ARCA — Agencia de Recaudación y Control Aduanero (argentina.gob.ar)](https://www.argentina.gob.ar/arca) — read 2026-10-24.
- [InfoLeg — Ley 27.430 (reforma tributaria) landing](https://www.infoleg.gob.ar/infolegInternet/anexos/250000-254999/253891/norma.htm) — served 2026-10-24 (consolidated text not machine-readable this pass).
- Existing pack skill `ar-corporate-income-tax` — rates, deemed-margin WHT and treaty figures carried forward with their citations.

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
