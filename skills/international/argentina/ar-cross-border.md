---
name: ar-cross-border
description: >
  Argentina cross-border tax reference for 2026. Covers Ganancias
  on foreign-source income of residents (worldwide for individuals,
  with repatriation rules), the non-resident withholding grid (7%
  dividends, 35% deemed-margin on interest and royalties, ~15.05%
  effective interest), the 20+ CDI treaty network, personal assets
  tax (Bienes Personales) on worldwide assets, and the absence of a
  general exit tax. Trigger on Argentina cross-border, non-resident,
  beneficiarios del exterior, treaty, CDI, expatriate, Bienes
  Personales. Source-cited draft.
jurisdiction: AR
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Argentina cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the ARCA portal
(argentina.gob.ar — empleadores and institutional pages), the
InfoLeg statute portal (Ley 27.430 landing served; consolidated text
not machine-readable this pass), and the existing AR pack skills
(figures carried forward with their citations). Currency: Argentine
peso (ARS).

**Source status caveat:** residence-test wording, the current treaty
list with article-level rates, the 2026 Bienes Personales scale and
the repatriation-rule status (Ley 27.541 / 2023 changes) are
**needs-sources**; the WHT grid below is carried from the existing
pack with its citations.

## 2. Who the rules apply to

- **Individuals resident in Argentina** pay Ganancias on worldwide
  income (with the repatriation regime for foreign-source income —
  current status needs-sources) and Bienes Personales on worldwide
  assets (progressive, minimum threshold indexed — needs-sources).
- **Non-residents** pay Ganancias only on Argentine-source income,
  almost always collected by withholding (the grid in section 3).
- **Companies.** Argentine companies pay the tiered 25/30/35% on
  worldwide income (foreign-tax-credit rules); non-resident companies
  are taxed on Argentine-source income via the withholding grid or a
  PE.
- **Departure.** No general exit tax confirmed — **needs-sources.**

## 3. Rates and reliefs table

| Item | Content | Source |
|---|---|---|
| Dividend WHT to non-residents | 7% on distributions and branch remittances (post-2018 profits; equalisation tax may apply to pre-2018 earnings) | Ley 20.628 — ar-corporate-income-tax |
| Interest WHT to non-residents | 35% on a deemed margin (commonly 43%) → ~15.05% effective; treaty-reducible | Ley 20.628 — ar-corporate-income-tax |
| Royalty WHT to non-residents | 35% on deemed margin; ~31.5% software, ~28% trademark/technical assistance; treaty-reducible | Ley 20.628 — ar-corporate-income-tax |
| Corporate rate (resident company / PE) | Tiered 25% / 30% / 35% (top tier above ARS ~1.017bn, indexed) | Ley 20.628 art. 73 — ar-corporate-income-tax |
| IRPF 4ª categoría (resident employment) | Progressive scale, employer-withheld | ar-income-tax — 2026 scale needs-sources |
| Bienes Personales | Annual tax on worldwide assets of individuals; scale/threshold indexed | Ley 23.966 — needs-sources for 2026 values |
| Exit tax | None general | needs-sources |
| Treaty network | 20+ CDIs (e.g. USA, Spain, Italy, Chile, Brazil, Germany, France, UK) reduce WHT | ar-corporate-income-tax — list needs-sources |

## 4. Tax base and computation

For non-residents the base is the **Argentine-source gross amount**,
often reduced by a statutory **deemed margin** before the 35% rate
(interest: 43% of gross → 15.05% effective; royalties: margin varies
by type). For residents the base is worldwide income, with foreign
taxes creditable within limits; foreign-source income of individuals
has been subject to repatriation conditions (status needs-sources).
Source rules matter: services are Argentine-source where performed
in Argentina (services rendered abroad by non-residents are generally
off-net unless used in Argentina — needs-sources for the current
"uso en el país" state).

## 5. Deadlines

- **Ganancias annual return (F.1585):** mid-year following the
  fiscal year (exact 2026 date: needs-sources).
- **WHT remittance (SIRCREB):** monthly per ARCA calendar.
- **Bienes Personales (F.1814):** annual, mid-year (needs-sources
  for the 2026 date).
- **Personal assets abroad / CUIT filings:** per ARCA resolutions.

## 6. Penalties and interest

Underpaid Ganancias/WHT runs through the Ley 27.430 libro II penal
regime (fines plus ARCA active interest); amounts **needs-sources**.

## 7. Worked examples

**Example 1 — dividend to a treaty parent.** An Argentine company
distributes ARS 10,000,000 of post-2018 profits to a non-resident
parent; domestic WHT 7% (treaty may reduce — confirm the CDI).

```oa-check
name: dividend 10m domestic 7 percent
inputs:
  dividend: 10000000
  rate: 7
steps:
  - wht: dividend * pct(1, rate)
expected:
  wht: 700000.00
```

**Example 2 — interest to a non-resident lender.** ARS 4,000,000 of
interest to a foreign bank: 35% applies to the deemed 43% margin →
effective 15.05%.

```oa-check
name: interest 4m deemed margin 43 percent at 35 percent
inputs:
  interest: 4000000
  margin: 43
  rate: 35
steps:
  - deemed_profit: interest * pct(1, margin)
  - wht: deemed_profit * pct(1, rate)
expected:
  deemed_profit: 1720000.00
  wht: 602000.00
```

## 8. Ask the client first

1. Where do the individuals actually live and centre their life —
   and are they still Argentine-source-taxed on local employment or
   rentals?
2. Which treaty (if any) covers the payer–recipient pair, with a
   current residence certificate on file?
3. Are Bienes Personales filings current for worldwide assets,
   including the reduced-rate foreign-securities treatment?
4. Do the cross-border contracts shift Argentine WHT (gross-up), and
   is SIRCREB being filed monthly?

## 9. Sources

- [ARCA — Agencia de Recaudación y Control Aduanero (argentina.gob.ar)](https://www.argentina.gob.ar/arca) — read 2026-10-24.
- [ARCA — Empleadores](https://www.argentina.gob.ar/arca/empleadores) — read 2026-10-24.
- [InfoLeg — Ley 27.430 landing](https://www.infoleg.gob.ar/infolegInternet/anexos/250000-254999/253891/norma.htm) — served 2026-10-24 (consolidated text not machine-readable this pass).
- Existing pack skills `ar-corporate-income-tax`, `ar-income-tax`, `ar-tax-overview` — WHT grid, tiers and treaty figures carried forward with their citations.

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
