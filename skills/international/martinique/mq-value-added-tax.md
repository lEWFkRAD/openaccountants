---
name: mq-value-added-tax
description: >
  Martinique VAT reference for 2026. Martinique is a DOM with its own VAT
  rates: 8.5% standard, reduced bands on listed essentials, and territorial
  rules treating DOM-to-metropole movements as imports/exports. Covers
  rates, registration, filing periods, the octroi de mer interface and the
  Guadeloupe single-territory point. Source-cited draft built on the France
  pack DOM rate table and douane.gouv.fr pages read 2026-10-22.
jurisdiction: MQ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Martinique value added tax

## 1. Scope and sources

VAT in Martinique follows CGI Art. 251 ff with DOM rates. Rate table carried from the France pack (`france-vat-return.md`, official impots.gouv.fr DOM-rates page read 19 Sep–19 Oct 2026); douane.gouv.fr pages read 2026-10-22. impots.gouv.fr in maintenance on 2026-10-22.

## 2. Rates

| Rate | Applies to | Source |
|---:|---|---|
| 8.5% | standard rate in Martinique (also Guadeloupe, Réunion) | [France pack DOM rate table](https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom), read 19 Oct 2026 |
| Reduced bands (2.1%, 5.5%) | listed essentials — item-level classification required | same |
| 0% / exempt | exports; Martinique→metropole shipments are exports for the DOM seller | CGI Art. 256 A–259 territoriality |

## 3. Registration

Same regime as the metropole: franchise en base thresholds (France pack table), mandatory VAT above.

## 4. Territoriality and the octroi interface

- Metropole/third-country → Martinique: import VAT at the DOM rate **plus octroi de mer**.
- Martinique → metropole: export for the DOM seller; the Antilles single-territory rule means Guadeloupe↔Martinique movements need no new clearance but do need the monthly dispatch declaration — see `mq-antilles-goods-movements`.
- Services: general place-of-supply rules (Art. 256 bis).

## 5. Deadlines

CA3 monthly/quarterly per regime; DI (goods-exchange declaration) filed with the customs administration; CA12 annual for franchise entities above ceiling.

## 6. Penalties and interest

10% late-filing increase (Art. 1728) plus interest in arrears; octroi de mer has separate customs fines (July 2025 circular).

## 7. Worked examples

**Example 1 — Martinique retailer, €50,000 ex-tax monthly sales.**
Output VAT = 50,000 × 8.5% = 4,250.00.

```oa-check
name: Martinique retail sales EUR 50,000 ex-tax
inputs:
  sales: 50000
steps:
  - vat: sales * 0.085
expected:
  vat: 4250.00
```

**Example 2 — metropole import CIF €20,000, illustrative octroi 13%.**
Octroi 2,600; import VAT (20,000 + 2,600) × 8.5% = 1,921.00; total landed tax 4,521.00. Octroi rate is product-specific — verify against the Martinique regional deliberation.

```oa-check
name: Import CIF EUR 20,000 octroi 13 percent illustrative
inputs:
  cif: 20000
steps:
  - octroi: cif * 0.13
  - vat: (cif + octroi) * 0.085
  - total_tax: octroi + vat
expected:
  total_tax: 4521.00
```

## 8. Ask the client first

1. Product-line rate classification (essentials list).
2. DI and octroi declarations for DOM↔metropole and inter-island flows.
3. Franchise-threshold position.
4. Tourist hors-taxe purchases (octroi refund scheme — douane guide).

## 9. Sources

- France pack `france-vat-return.md` DOM rate table — read 19 Oct 2026.
- [douane.gouv.fr — octroi de mer declaration](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne) — read 2026-10-22.
- [douane.gouv.fr — hors-taxe guide (Guadeloupe/Martinique)](https://www.douane.gouv.fr/fiche/acheter-des-produits-hors-taxe-doctroi-de-mer-en-guadeloupe-et-martinique-touristes) — read 2026-10-22.
