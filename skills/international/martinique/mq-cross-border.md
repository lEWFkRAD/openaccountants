---
name: mq-cross-border
description: >
  Martinique cross-border tax reference for 2026. Martinique is part of the
  French fiscal territory but an EU outermost region: customs/excise
  barriers apply to metropole movements, the French exit tax and
  non-resident rules apply as elsewhere in France, and CARICOM/EU EPA
  proximity shapes regional trade. Covers residence, source, the ORA
  customs/VAT interface, treaty territorial clauses, and exit. Built on the
  France pack's verified figures plus douane.gouv.fr pages read 2026-10-22.
jurisdiction: MQ
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Martinique cross-border tax

## 1. Scope and sources

Martinique = France for residence and treaties, but an EU **outermost region** with fiscal barriers (octroi de mer, import VAT) against the metropole, and immediate proximity to CARICOM states (Saint Lucia, Dominica, Barbados). Figures from the France pack (official pages read 19 Sep–19 Oct 2026) and douane.gouv.fr (read 2026-10-22).

## 2. Residence and source

- CGI Art. 4 B tests apply identically in Martinique.
- A Martinique-resident company is French-resident for treaty purposes.
- Martinique-source income: real property, PE activity, employment exercised there.

## 3. The ORA customs/VAT interface

- Metropole→Martinique goods: export for the seller (0% French VAT), import into Martinique (DOM VAT + octroi de mer — `mq-value-added-tax`).
- Martinique→CARICOM third countries: EU export formalities; EU–CARIFORUM EPA governs origin/duties on the buyer side.
- Guadeloupe↔Martinique: single Antilles octroi territory — no new clearance, but monthly dispatch declarations (`mq-antilles-goods-movements`).

## 4. Exit tax and departures

The French exit tax (CGI Art. 167 bis) applies to Martinique residents leaving the French fiscal territory on unrealised share gains above the thresholds; deferral/erasure per the France pack (`leaving-france-exit-tax.md`, read 19 Sep–19 Oct 2026). No separate Martinique exit regime.

## 5. Treaties and the DOM question

Most French treaties extend to Martinique; some older treaties exclude or reserve the DOM — check the treaty's territorial-application article before relying on it (needs-sources per treaty).

## 6. Worked examples

**Example 1 — landed cost, metropole import CIF €20,000, illustrative octroi 13%.**
Octroi 2,600; import VAT (22,600) × 8.5% = 1,921.00; landed 24,521.00.

```oa-check
name: Landed cost CIF EUR 20,000 octroi 13 percent illustrative
inputs:
  cif: 20000
steps:
  - octroi: cif * 0.13
  - vat: (cif + octroi) * 0.085
  - landed: cif + octroi + vat
expected:
  landed: 24521.00
```

**Example 2 — exit tax illustration, latent gain €100,000.**
Flat rate 12.8% + social charges 17.2% = 30,000.00 (deferral available outside EU/EEA per the France pack).

```oa-check
name: Exit tax illustration EUR 100,000 latent gain
inputs:
  gain: 100000
steps:
  - income_side: gain * 0.128
  - social: gain * 0.172
  - total: income_side + social
expected:
  total: 30000.00
```

## 7. Ask the client first

1. Does the applicable treaty extend to the DOM (territorial clause)?
2. Are goods flows declared on both customs (octroi/DI/dispatch) and tax sides?
3. Departure plans: Art. 167 bis thresholds and deferral.
4. CARICOM/EPA origin status for regional sales.

## 8. Sources

- France pack `leaving-france-exit-tax.md`, `france-vat-return.md` (official pages read 19 Sep–19 Oct 2026).
- [douane.gouv.fr — octroi de mer regime](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne) — read 2026-10-22.
- CGI Art. 4 B, 167 bis — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22).
