---
name: uy-cross-border
description: >
  Uruguay cross-border tax reference for 2026. Covers the
  territorial-source system for non-residents (IRNR), the 7%
  dividend / 12% interest / 12% royalty withholding on
  Uruguay-source income, the 25% low-and-no-tax-jurisdiction
  premium, the 25-treaty CDI network listed by the DGI with
  effective dates and MLI status, DGI MAP guidelines, and the
  absence of a confirmed exit tax. Trigger on Uruguay
  cross-border, non-resident, treaty, CDI, expat, exit tax,
  IRNR. Source-cited draft.
jurisdiction: UY
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Uruguay cross-border tax

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the DGI pages on
gub.uy (institution, tributación internacional, the CDI status table,
MAP guidelines, AII page) and the existing UY pack skills (figures
carried forward with their citations). Currency: Uruguayan peso
(UYU).

**Source status caveat:** dgi.gub.uy (legacy wdgi portal) was
unreachable this pass; residence-test wording, treaty article-level
rates and the exit-tax position are **needs-sources**. The treaty
table below is copied from the DGI's own CDI status page (read
2026-10-24).

## 2. Who the rules apply to

- **Individuals.** Residents pay IRPF on labour income (progressive to
  36%) and on most capital income; because the system is
  **territorial**, most foreign-source income is outside the Uruguayan
  net (limited exceptions for certain foreign capital income of
  residents — see uruguay-income-tax). Non-residents pay **IRNR** on
  Uruguay-source income only.
- **Companies.** Resident entities and non-resident PE's pay IRAE
  (25%) on Uruguay-source business income; foreign-source income is
  generally outside IRAE (anti-deferral/passive rules excepted — see
  uy-corporate-income-tax).
- **Departure.** No confirmed exit-charge regime for individuals or
  companies — **needs-sources.**

## 3. Rates and reliefs table

| Item | Content | Source |
|---|---|---|
| IRNR — dividends to non-residents | 7% out of IRAE-taxed profits; treaty relief may reduce | TO1996 Título 8 — uy-corporate-income-tax |
| IRNR — interest to non-residents | 0%–12% depending on instrument/term/currency; 25% if recipient in LNTJ | TO1996 Título 8 — uy-corporate-income-tax |
| IRNR — royalties to non-residents | 12%; 25% if recipient in LNTJ | TO1996 Título 8 — uy-corporate-income-tax |
| IRAE (PE / resident company) | 25% Uruguay-source business income | TO1996 Título 4 — uy-corporate-income-tax |
| IRPF (resident labour income) | Progressive 0%–36%, employer-withheld | TO1996 Título 7 — uruguay-payroll |
| Net wealth tax (Impuesto al Patrimonio) | Annual; 1.5% companies (3% LNTJ entities); progressive for individuals | TO1996 Título 14 — uy-tax-overview |
| Exit tax | No confirmed departure charge | needs-sources |

## 4. Treaty network (DGI CDI table, read 2026-10-24)

The DGI publishes the status of every CDI with the approving law, the
entry-into-force date, the first year of application, and whether the
OECD MLI modifies it. In force (approval law / applicable from):
Germany (Ley 18.844 / 2012), Argentina (Ley 19.032 / 2013), Belgium
(Ley 19.403 / 2018), Brazil (Ley 20.009 / 2024), Chile (Ley 19.548 /
2019), South Korea (Ley 19.033 / 2014), Ecuador (Ley 18.932 / 2013),
United Arab Emirates (Ley 19.393 / 2017), Spain (Ley 18.730 / 2012),
Finland (Ley 19.035 / 2014), Hungary (Ley 16.366 / 1994), India (Ley
18.972 / 2014), Italy (Ley 19.819 / 2021), Japan (Ley 19.938 / 2022),
Liechtenstein (Ley 18.933 / 2013), Luxembourg (Ley 19.354 / 2018),
Malta (Ley 19.010 / 2013), Mexico (Ley 18.645 / 2011), Paraguay (Ley
19.697 / 2020), Portugal (Ley 18.934 / 2012), United Kingdom (Ley
19.443 / 2017), Romania (Ley 19.257 / 2015), Singapore (Ley 19.457 /
2018), Switzerland (Ley 18.867 / 2012), Vietnam (Ley 19.404 / 2017).
Signed but not yet in force: Colombia (signed 19/11/2021). Most
CDIs are MLI-modified — check the DGI's MLI columns per treaty.
Article-level rates remain **needs-sources** (confirm each
instrument). The DGI publishes Procedimiento Amistoso (MAP)
guidelines and separate information on Tax Information Exchange
Agreements (AII).

## 5. Tax base and computation

Uruguay taxes by **source**, not residence: the non-resident charge
(IRNR) attaches to Uruguay-source income — Uruguayan employment and
services, immovable property, Uruguayan business activity (PE), and
Uruguayan-source passive income. Withholding is often the collection
mechanism and may be final for non-residents. For residents, the
territorial principle keeps most foreign-source income out of IRPF/
IRAE, which makes source analysis the central computation question.

## 6. Deadlines

- **IRPF annual return (Form 1102/1103):** generally mid-year
  following the tax year; most single-employer employees do not file
  (employer/BPS ajuste anual instead) — see uruguay-payroll.
- **IRAE return:** annual, commonly within ~4 months of fiscal
  year-end; monthly advances during the year (see
  uy-corporate-income-tax).
- **IRNR withholding remittances:** monthly per the DGI vencimientos
  calendar (exact day: needs-sources).

## 7. Penalties and interest

Late or understated IRNR/IRAE runs through the Texto Ordenado
penalty-and-interest regime (section-level amounts **needs-sources**);
treaty disputes follow the DGI's MAP guidelines.

## 8. Worked examples

**Example 1 — interest to a non-resident bank.** A Uruguayan company
pays UYU 5,000,000 of Uruguay-source interest to a non-resident
lender. Standard IRNR is 12%; if the lender is in an LNTJ the rate
jumps to 25%.

```oa-check
name: interest UYU 5m standard vs LNTJ
inputs:
  interest: 5000000
  standard: 12
  lntj: 25
steps:
  - wht_standard: interest * pct(1, standard)
  - wht_lntj: interest * pct(1, lntj)
  - delta: wht_lntj - wht_standard
expected:
  wht_standard: 600000.00
  wht_lntj: 1250000.00
  delta: 650000.00
```

**Example 2 — dividend to a UK parent.** A Uruguayan company
distributes UYU 2,000,000 of IRAE-taxed profit to its UK parent
(CDI in force from 2017, Ley 19.443). Domestic rate 7%; confirm the
treaty article rate before applying relief.

```oa-check
name: dividend UYU 2m domestic 7 percent
inputs:
  dividend: 2000000
  rate: 7
steps:
  - wht: dividend * pct(1, rate)
expected:
  wht: 140000.00
```

## 9. Ask the client first

1. Where is the income sourced under Uruguayan rules — services
   performed where, property where, payer resident where?
2. Is the counterparty in an LNTJ (25% premium) or a CDI state
   (possible relief, MLI check)?
3. Does the client hold Uruguayan immovable property or a PE that
   keeps them in the IRNR net even while living abroad?
4. Is the Impuesto al Patrimonio (annual wealth tax) being filed for
   Uruguayan assets?

## 10. Sources

- [DGI — Dirección General Impositiva (gub.uy)](https://www.gub.uy/direccion-general-impositiva) — read 2026-10-24.
- [DGI — Tributación internacional](https://www.gub.uy/direccion-general-impositiva/tributacion-internacional) — read 2026-10-24.
- [DGI — Estado de los CDI](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/convenios-para-evitar-doble-imposicion) — read 2026-10-24 (full treaty table with laws and dates).
- [DGI — Procedimiento amistoso (MAP)](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/procedimiento-amistoso) — read 2026-10-24.
- [DGI — Acuerdos de Intercambio de Información (AII)](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/acuerdos-intercambio-informacion-aii) — read 2026-10-24.
- Existing pack skills `uy-corporate-income-tax`, `uruguay-payroll`, `uy-tax-overview` — IRNR/IRAE/IRPF figures carried forward with their citations.

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
