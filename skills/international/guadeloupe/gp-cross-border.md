---
name: gp-cross-border
description: >
  Guadeloupe cross-border tax reference for 2026. Guadeloupe is part of the
  French fiscal territory but an EU outermost region: customs and excise
  apply between it and the metropole, the exit tax (CGI Art. 167 bis) and
  non-resident rules apply like elsewhere in France, and CARICOM/EU EPA
  trade context matters for regional operations. Covers residence, source,
  the ORA customs/VAT interface, treaties, and exit. Built on the France
  pack's verified figures plus douane.gouv.fr pages read 2026-10-22.
jurisdiction: GP
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Guadeloupe cross-border tax

## 1. Scope and sources

Guadeloupe = France for tax residence and treaties, but an EU **outermost region**: outside the EU VAT area and customs union in part, with fiscal barriers (octroi de mer, import VAT) between it and the metropole. Figures from the France pack (official pages read 19 Sep–19 Oct 2026) and douane.gouv.fr (read 2026-10-22).

## 2. Residence and source

- CGI Art. 4 B residence tests apply identically in Guadeloupe.
- A Guadeloupe-resident company is French-resident for treaty purposes (France's ~120 treaties cover it).
- Income arising in Guadeloupe is French-source: real property, PE activity, employment exercised there.

## 3. The ORA customs/VAT interface

- Metropole→Guadeloupe goods: export for the metropole seller (0% French VAT), import into Guadeloupe (DOM VAT + octroi de mer — see `gp-value-added-tax`).
- Guadeloupe→third countries (CARICOM region): EU export formalities; the EU–CARIFORUM EPA governs origin/duties on the buyer side.
- Services: general EU place-of-supply rules apply.

## 4. Exit tax and departures

The French exit tax (CGI Art. 167 bis) applies to Guadeloupe residents leaving the French fiscal territory on unrealised share gains above the thresholds; deferral and erasure rules per the France pack (`leaving-france-exit-tax.md`, read 19 Sep–19 Oct 2026). No separate Guadeloupe exit regime.

## 5. Treaties and the DOM question

Most French treaties apply to Guadeloupe; some older treaties exclude or reserve the DOM/territories — check the treaty's territorial-application article before relying on it (needs-sources per treaty).

## 6. Worked examples

**Example 1 — landed cost of a metropole import.** CIF €20,000, illustrative octroi 13%: octroi 2,600; import VAT (20,000+2,600) × 8.5% = 1,921.00; total landed 24,521.00.

```oa-check
name: Landed cost CIF EUR 20,000 illustrative octroi 13 percent
inputs:
  cif: 20000
steps:
  - octroi: cif * 0.13
  - vat: (cif + octroi) * 0.085
  - landed: cif + octroi + vat
expected:
  landed: 24521.00
```

**Example 2 — exit tax base.** A Guadeloupe-resident shareholder leaves France holding shares with unrealised gain €100,000 above the threshold: the 12.8% flat rate (or progressive election) plus 17.2% social charges would apply on the taxable event under Art. 167 bis (deferral available outside the EU/EEA per the France pack). Illustrative flat-rate tax: 100,000 × (12.8% + 17.2%) = 30,000.00.

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
2. Are goods flows declared on both the customs (octroi/DI) and tax sides?
3. Departure plans: Art. 167 bis thresholds and deferral eligibility.
4. CARICOM/EPA origin status for regional sales.

## 8. Sources

- France pack `leaving-france-exit-tax.md`, `france-vat-return.md` (official pages read 19 Sep–19 Oct 2026).
- [douane.gouv.fr — octroi de mer regime](https://www.douane.gouv.fr/demarche/declarer-votre-octroi-de-mer-interne) — read 2026-10-22.
- CGI Art. 4 B, 167 bis — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22).
