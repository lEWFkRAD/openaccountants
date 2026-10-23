---
name: gp-value-added-tax
description: >
  Guadeloupe VAT reference for 2026. Guadeloupe is a DOM with its own VAT
  rates: 8.5% standard, reduced rates on listed essentials, and territorial
  rules that treat DOM-to-metropole movements as imports/exports for VAT and
  octroi de mer purposes. Covers rates, registration thresholds, filing
  periods, the octroi de mer interface, penalties. Source-cited draft built
  on the France pack's DOM rate table and douane.gouv.fr pages read
  2026-10-22.
jurisdiction: GP
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Guadeloupe value added tax

## 1. Scope and sources

VAT in Guadeloupe follows CGI Art. 251 ff with DOM-specific rates. The rate table is carried from the France pack (`france-vat-return.md`, official impots.gouv.fr DOM-rates page read 19 Sep–19 Oct 2026) and cross-checked against douane.gouv.fr pages read 2026-10-22. impots.gouv.fr itself was in maintenance on 2026-10-22.

## 2. Rates

| Rate | Applies to | Source |
|---:|---|---|
| 8.5% | standard rate in Guadeloupe (and Martinique, Réunion) | [France pack DOM rate table](https://www.impots.gouv.fr/professionnel/questions/quels-sont-les-differents-taux-de-tva-applicables-dans-les-dom), read 19 Oct 2026 |
| Reduced rates (2.1%, 5.5% bands) | listed essentials (food, certain goods) — item-level classification needed | same page; verify each item |
| 0% / exempt | exports; DOM-to-metropole shipments are treated as exports for the DOM seller | territoriality rules, CGI Art. 256 A–259 |

## 3. Who is liable and registration

Same registration regime as metropolitan France: franchise en base threshold (the France pack's €38,500 services / goods thresholds apply with DOM monitoring), mandatory VAT above it. See `france-vat-return.md` Section 1 for the threshold table.

## 4. Territoriality and the octroi interface

- Goods moving **into Guadeloupe from the metropole or third countries** are imports: import VAT at the DOM rate plus **octroi de mer** (see `gp-producer-octroi-compliance`).
- Goods moving **out of Guadeloupe** are exports for the DOM seller (0% VAT) and imports for the metropole buyer.
- Services follow the general place-of-supply rules (Art. 256 bis).

## 5. Deadlines

- CA3 monthly/quarterly returns per the DGFiP regime; the DI (déclaration d'échange) for DOM-to-metropole goods movements is filed with the customs administration (DELTA/OM systems).
- CA12 annual return for franchise-regime entities above the franchise ceiling.

## 6. Penalties and interest

Late filing: 10% increase (Art. 1728 CGI) plus interest in arrears; omitted DOM-rate application is corrected with the same ladder. Octroi de mer late filing has its own customs fines (see the July 2025 circular).

## 7. Worked examples

**Example 1 — Guadeloupe retailer, €50,000 ex-tax sales in the month.**
Output VAT = 50,000 × 8.5% = 4,250.00.

```oa-check
name: Guadeloupe retail sales EUR 50,000 ex-tax
inputs:
  sales: 50000
steps:
  - vat: sales * 0.085
expected:
  vat: 4250.00
```

**Example 2 — import from the metropole, CIF €20,000, illustrative octroi de mer 13%.**
Octroi = 20,000 × 13% = 2,600. Import VAT base = CIF + octroi = 22,600; VAT = 22,600 × 8.5% = 1,921.00. Total landed tax = 4,521.00. (Octroi rate is product-specific — verify against the regional deliberation.)

```oa-check
name: Import CIF EUR 20,000 with octroi 13 percent illustrative
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

1. Which DOM rate applies to each product line (essentials list)?
2. Are DOM↔metropole movements being declared (DI + octroi)?
3. Franchise-threshold position across all activities.
4. Whether the customer is a tourist buying hors-taxe (octroi/VAT refund scheme).

## 9. Sources

- France pack `france-vat-return.md` DOM rate table — official page read 19 Oct 2026.
- [douane.gouv.fr — octroi de mer declaration](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne) — read 2026-10-22.
- [douane.gouv.fr — hors-taxe guide (Guadeloupe/Martinique)](https://www.douane.gouv.fr/fiche/acheter-des-produits-hors-taxe-doctroi-de-mer-en-guadeloupe-et-martinique-touristes) — read 2026-10-22.
