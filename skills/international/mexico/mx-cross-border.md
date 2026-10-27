---
name: mx-cross-border
description: >
  Mexico cross-border income reference for 2026. Covers LISR Title V taxation of non-residents with Mexican-source income: source-of-wealth rules (Arts. 153-165), flat 25% on real-property rent and gains and on independent services (Arts. 156, 158, 160, read), the permanent-establishment concept, the gross-up duty of the Mexican payer, and treaty interaction. Trigger on Mexico non-resident, residente en el extranjero, fuente de riqueza, establecimiento permanente, retencion 25%, Title V. Source-cited draft.
jurisdiction: MX
category: cross-border
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Mexico cross-border (non-resident income, Title V LISR)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: the LISR consolidated
PDF was read directly — Arts. 153, 156, 158, 160, 161, 163, 165 are
quoted from that text. Treaty rates are needs-sources (DOF/SAT treaty
list).

## 2. Who applies

Foreign residents (individuals or corporations) earning Mexican-source
income without a Mexican permanent establishment (PE) are taxed under
Title V (Art. 153, read). With a PE, they pay the ordinary regimes on
income attributable to it. Art. 153 also imposes arm's-length pricing on
related-party operations even for Title V taxpayers (paragraph added DOF
12-11-2021, read). Payments that merely benefit a foreign resident,
including avoided expenses, are swept into the same net (Art. 153,
read).

## 3. Rates

| Income type | Rate on gross | Source |
|---|---|---|
| Independent services performed in Mexico | 25% | LISR Art. 156 (read) |
| Mexican real-property rent / land-use rights | 25% | LISR Art. 158 (read) |
| Sale of Mexican real property | 25% on gross proceeds | LISR Art. 160 (read) |
| Shares in Mexican companies (50%+ real-estate value test) | 25% | LISR Art. 161 (read) |
| Derivatives on Mexican shares | 25% on gain | LISR Art. 163 (read) |
| Interest | 4.9% / 10% / 25% by payer type | LISR Arts. 166-168 (needs-sources current text) |
| Royalties | 35% | LISR Art. 174 (needs-sources current text) |
| Dividends | corporate-level 30% via Art. 10 gross-up | LISR Art. 165 route (read) |

The Mexican payer is the withholding agent; if the payer is also
non-resident, the foreign recipient self-pays by declaration within 15
days of receiving the income (Arts. 158, 160, read).

## 4. Base and timing

Title V flat categories are on gross with no deductions (read Arts. 156,
158, 160: "sin deduccion alguna"). Source rules are location-based for
real property (Arts. 158, 160, read) and place-of-performance for
services, with a presumption that services are wholly performed in
Mexico once part is performed there, rebuttable by proving the foreign
portion (Art. 156, read). A related-party payment presumption also
applies (Art. 156, read).

## 5. Deadlines

Withholding is remitted with the monthly determinacion by the 17th of
the following month. Self-assessment by the non-resident: declaration
within 15 days of the income (Arts. 158, 160, read). Informative
returns for cross-border related-party flows: Art. 76-A master/local
with the annual return (read).

## 6. Penalties and interest

CFF Arts. 64/65 penalties plus updating and interest (CFF Art. 20).
Failure to withhold makes the Mexican payer jointly liable for the tax.

## 7. Cross-border interactions

PE: domestic definition in Art. 8 plus treaty definitions; a
construction site, a dependent agent, or business performed through a
Mexican resident related party can create one (Arts. 8-8A — verify
current). Treaty relief requires a residence certificate; the Art. 156
presumption survives unless treaty residence and a PE analysis are
documented. Holding structures: Art. 161's 50% real-estate look-through
(read) defeats share structures for Mexican property. Pension funds
enjoy a targeted exemption on Mexican real-property gains under
conditions (Art. 155 area, read).

## 8. Worked examples

A US company leases MXN 50,000/month of Mexico City warehouse space to a
Mexican tenant and wants to receive 50,000 net. Art. 158 taxes 25% of
gross and the tenant withholds — gross-up:

```oa-check
name: gross-up of non-resident rent 25 percent rate
inputs:
  renta_neta: 50000
  tasa: 0.25
steps:
  - renta_bruta: renta_neta / (1 - tasa)
  - retencion: renta_bruta * tasa
expected:
  renta_bruta: 66666.67
  retencion: 16666.67
```

A German consultant invoices a Mexican group company MXN 80,000 net for
services delivered in Mexico City (Art. 156, 25% on gross, grossed up):

```oa-check
name: gross-up of non-resident services 25 percent rate
inputs:
  fee_neta: 80000
  tasa: 0.25
steps:
  - fee_bruta: fee_neta / (1 - tasa)
  - retencion: fee_bruta * tasa
expected:
  fee_bruta: 106666.67
  retencion: 26666.67
```

## 9. Ask the client / sources

Ask: Does the foreign party have a PE (site, agent, dependent
contractor)? Is the payer grossing up flat-rate income, or did the
contract quote net? Is the 50% real-estate share test (Art. 161) hit in
any share sale? Treaty residence certificates on file before payment?
Related-party cross-border flows mapped to the Art. 76-A informative
returns?

Sources: LISR consolidated PDF (read 2026-10-27). Needs-sources:
treaty-by-treaty rates and PE thresholds (DOF/SAT), current Arts. 166-174
interest and royalty text, SAT residence-certificate procedure.

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
