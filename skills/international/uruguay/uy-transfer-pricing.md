---
name: uy-transfer-pricing
description: >
  Uruguay transfer pricing reference for 2026. Covers the IRAE
  arm's-length rules for related-party transactions, the 25%
  low-and-no-tax-jurisdiction (LNTJ) withholding premium on
  cross-border associate payments (dividends, interest, royalties),
  the 15% domestic minimum top-up tax (IMC, Ley 20.341, Pillar Two),
  and the DGI treaty/MAP route for double-tax relief. Trigger on
  Uruguay transfer pricing, arm's length, related party, LNTJ,
  precio de transferencia, DGI revaluation. Source-cited draft.
jurisdiction: UY
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Uruguay transfer pricing

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the DGI pages on
gub.uy (institution, tributación internacional, CDI status, MAP
guidelines), the DGI's IRNR Texto Ordenado 2023 PDF (served, text not
parsed this pass), and the existing UY pack skills (figures carried
forward with their citations). Currency: Uruguayan peso (UYU).

**Source status caveat:** the legacy DGI portal (dgi.gub.uy/wdgi) was
unreachable this pass and the Texto Ordenado section numbers for the
arm's-length rule, the transfer-pricing decree and any statutory
documentation deadline are **needs-sources** — confirm against the
Texto Ordenado 1996 (Título 4 for IRAE, Título 8 for IRNR) and its
reglamento before tier-1 promotion.

## 2. Who the rules apply to

- **Resident companies and Uruguayan PE's of non-residents** filing
  IRAE (25%): related-party transactions (goods, services, financing,
  intangibles) must reflect arm's-length conditions; the DGI may
  revalue non-arm's-length terms that shift Uruguayan-source profit
  abroad. Section numbers: **needs-sources.**
- **Payments to entities in low-or-no-tax jurisdictions (LNTJ)** face
  the 25% IRNR rate instead of the standard 12% on interest and
  royalties (see the rate table) unless the recipient proves an
  effective level of taxation / transparency — the LNTJ list and the
  rebuttal route are set by decree and DGI resolution
  (**needs-sources** for the current list).
- **In-scope multinational groups** (consolidated revenue ≥ EUR 750m,
  approx — confirm) face the 15% qualified domestic minimum top-up
  tax (IMC) under Ley 20.341 implementing the OECD Pillar Two GloBE
  rules.

## 3. The rules (revaluation and overlay table)

| Rule | Content | Source |
|---|---|---|
| Arm's-length revaluation | DGI may recompute Uruguay-source income where related-party terms depart from arm's length | Texto Ordenado 1996 Título 4 (IRAE) — sections needs-sources |
| IRAE rate | 25% of Uruguayan-source net business income | TO1996 Título 4 — uy-corporate-income-tax |
| Dividend WHT to non-residents | 7% out of IRAE-taxed profits; treaty relief may reduce | TO1996 Título 8 (IRNR) — uy-corporate-income-tax |
| Interest WHT to non-residents | 12% general (0%–12% by instrument); **25% if recipient in LNTJ** | TO1996 Título 8 — uy-corporate-income-tax |
| Royalty WHT to non-residents | 12%; **25% if recipient in LNTJ** | TO1996 Título 8 — uy-corporate-income-tax |
| LNTJ premium rate | 25% IRNR on income of entities resident/located in low-or-no-tax jurisdictions | TO1996 Título 8 — uy-corporate-income-tax |
| Pillar Two domestic top-up (IMC) | 15% for in-scope MNE groups | Ley 20.341 — uy-corporate-income-tax |
| Documentation | No confirmed statutory TP-file/CbCR triplet for all taxpayers; DGI requests records on audit | needs-sources |

## 4. Tax base and computation

A revaluation raises the IRAE base (25% of the uplift). Separately,
the WHT overlay keys on the **gross** payment: an associate royalty
or interest stream can therefore be hit twice — once by IRAE
revaluation of the Uruguayan payer/recipient base and once by IRNR
withholding at 12% or the 25% LNTJ premium on the gross amount.
Compute both charges on any adjustment, and check whether the
counterparty's jurisdiction is on the LNTJ list before applying 12%.

## 5. Deadlines

- **IRAE return and balance:** annual, commonly within about four
  months after fiscal year-end; monthly IRAE advances during the year;
  DGI publishes exact dates each year by taxpayer group (see
  uy-corporate-income-tax).
- **IRNR withholding on associate payments:** monthly remittance per
  the DGI vencimientos calendar (exact day: needs-sources).
- **TP documentation:** no statutory preparation deadline confirmed —
  **needs-sources.**

## 6. Penalties and interest

Late or understated IRAE/IRNR runs through the Texto Ordenado
penalty-and-interest regime (section-level amounts **needs-sources**).
Treaty disputes on revaluations go to the DGI's published Procedimiento
Amistoso (MAP) guidelines.

## 7. Worked examples

**Example 1 — royalty to an LNTJ affiliate.** A Uruguayan company
pays UYU 2,000,000 of royalties to an affiliate in a low-tax
jurisdiction. The DGI revalues the royalty 25% higher for IRAE, and
the gross payment suffers IRNR at the 25% LNTJ rate rather than 12%.

```oa-check
name: royalty UYU 2m LNTJ uplift and WHT
inputs:
  royalty: 2000000
  uplift_pct: 25
  cit_rate: 25
  wht_standard: 12
  wht_lntj: 25
steps:
  - uplift: royalty * pct(1, uplift_pct)
  - extra_cit: uplift * pct(1, cit_rate)
  - wht_standard: royalty * pct(1, wht_standard)
  - wht_lntj: royalty * pct(1, wht_lntj)
  - wht_delta: wht_lntj - wht_standard
expected:
  uplift: 500000.00
  extra_cit: 125000.00
  wht_standard: 240000.00
  wht_lntj: 500000.00
  wht_delta: 260000.00
```

**Example 2 — dividend to a treaty parent.** A Uruguayan company
distributes UYU 1,000,000 of IRAE-taxed profit to a parent in a
treaty state; the treaty caps dividend WHT at 5% (illustrative —
confirm each CDI article).

```oa-check
name: dividend UYU 1m domestic 7 percent vs treaty 5 percent
inputs:
  dividend: 1000000
  domestic: 7
  treaty: 5
steps:
  - domestic_wht: dividend * pct(1, domestic)
  - treaty_wht: dividend * pct(1, treaty)
  - saving: domestic_wht - treaty_wht
expected:
  domestic_wht: 70000.00
  treaty_wht: 50000.00
  saving: 20000.00
```

## 8. Ask the client first

1. Which cross-border related-party transactions ran in the year —
   goods, services, royalties, management fees, loans — and at what
   prices on each side?
2. Is every counterparty jurisdiction on the current LNTJ list, and
   has any 12% withholding actually been 25%?
3. Are treaty rates being applied with beneficial-owner documentation,
   and has the MLI been checked for the relevant CDI?
4. Is the group in scope of Ley 20.341 (IMC 15%), and has the top-up
   computation been done?

## 9. Sources

- [DGI — Dirección General Impositiva (gub.uy)](https://www.gub.uy/direccion-general-impositiva) — read 2026-10-24.
- [DGI — Tributación internacional](https://www.gub.uy/direccion-general-impositiva/tributacion-internacional) — read 2026-10-24.
- [DGI — Estado de los CDI](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/convenios-para-evitar-doble-imposicion) — read 2026-10-24.
- [DGI — Procedimiento amistoso (MAP)](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/procedimiento-amistoso) — read 2026-10-24.
- [DGI — IRNR Texto Ordenado 2023 (PDF)](https://www.gub.uy/direccion-general-impositiva/sites/direccion-general-impositiva/files/2024-05/Secci%C3%B3n%20I%20-%20T%C3%ADtulo%202%20-%20TO%202023%20IMPO.pdf) — served 2026-10-24, text not parsed this pass.
- Existing pack skill `uy-corporate-income-tax` — IRAE/IRNR/LNTJ/Pillar Two figures carried forward with their citations.

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
