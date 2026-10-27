---
name: mx-social-contributions
description: >
  Mexico social contributions (IMSS) reference for 2026. Covers employer and worker quotas under the Ley del Seguro Social (Arts. 28, 38, 39, 73), the five occupational-risk decreto-prima classes, the SBC base and its 25x minimum-wage ceiling, INFONAVIT 5%, SAR, state payroll taxes, monthly cedula payment by the 17th, and PTU under LFT Art. 123. Trigger on Mexico IMSS, cuotas obrero patronales, salario base de cotizacion, INFONAVIT, PTU, decreto-prima. Source-cited draft.
jurisdiction: MX
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Mexico social contributions (IMSS, INFONAVIT, PTU)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: the Camara de Diputados
consolidated PDF of the Ley del Seguro Social (LSS) was read directly —
Arts. 28 (SBC ceiling), 30 (SBC construction), 38 (employer as retentor),
39 (monthly payment by the 17th) and 73 (decreto-prima table) are quoted
from that text. The 2026 minimum wage and the resulting 2026 SBC ceiling
are needs-sources (DOF annual decree).

## 2. Who applies

Every employer (patron) with workers in Mexico registers with IMSS,
withholds the worker quotas from wages (LSS Art. 38, read) and pays the
combined obrero-patronal quotas. Cooperative members cotizan as workers
(Art. 19, read). Independent workers can affiliate voluntarily.

## 3. Rates

Quotas are on the salario base de cotizacion (SBC), which includes cash
plus in-kind payments and the proportional aguinaldo and seniority
premium; the ceiling is 25x the general minimum wage (Art. 28, read; the
2026 peso value is needs-sources).

| Branch | Employer | Worker | Source |
|---|---|---|---|
| Illness and maternity | 20.6% | 3.0% | LSS Arts. 95, 97 (schedules — verify current) |
| Disability and life | 1.75% | 0.625% | LSS Art. 119 |
| Retirement, disability, survivors | 2.375% | — | LSS Art. 134 |
| Old-age savings (SAR) | 2% | — | LSS Art. 37 |
| Housing (INFONAVIT) | 5% | — | INFONAVIT Art. 45 |
| Occupational risk (decreto-prima) | 0.54355%-7.58875% by class I-V | — | LSS Art. 73 (table read 2026-10-27) |
| INSH (daycare and cash expenses) | 1%-1.75% | — | LSS Art. 201 (verify current) |

Employer total therefore runs roughly 20.6% + fixed 11.125% + risk
premium = about 31.5% at the top risk class. State payroll tax
(impuesto sobre nomina): about 3% in most states (CDMX 3%) — state codes
needs-sources.

## 4. Base and timing

SBC is built from fixed pay plus the average of variable pay over the
prior two months (Art. 30, read). Quotas accrue monthly in arrears
(Art. 39, read). PTU (employee profit sharing) is 10% of the company's
modified fiscal result under LFT Art. 123, half distributed equally and
half pro-rata to wages, capped at 20x the local minimum wage per worker
or three times the average wage — whichever pays less; directors and
non-resident workers are excluded from the base (LFT Arts. 123-127). PTU
paid is deductible for ISR (LISR Art. 9 fraction I, read).

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| IMSS cedula de determinacion plus payment | by the 17th of the following month (Art. 39, read) | LSS Art. 39 |
| Worker quota withholding by employer | each payroll (Art. 38, read); late recovery limited to 4 accumulated weekly quotas | LSS Art. 38 |
| INFONAVIT | monthly, alongside the IMSS cedula | INFONAVIT rules |
| PTU payment | within 60 days of the annual ISR return date | LFT Art. 123 |

## 6. Penalties and interest

Unpaid quotas: 10% surcharge plus inflation updating and interest under
LSS Art. 14-A; misreporting salaries or primes carries higher fines (LSS
Art. 304a). IMSS can assess capitales constitutivos for individual
claims — definitive on notification and payable in the terms of the law
(Art. 39 paragraph, read).

## 7. Cross-border interactions

Foreign workers in Mexico are subject to IMSS unless a totalisation
agreement applies (list needs-sources). Seconded employees: the Mexico-US
agreement coordinates coverage. A foreign employer with Mexican staff
must register through a PE or a Mexican representative.

## 8. Worked examples

Employer monthly IMSS on a worker with SBC MXN 30,000, office work
(Class I, prima 0.54355% per the Art. 73 table read 2026-10-27):

```oa-check
name: employer IMSS on 30000 SBC Class I premium
inputs:
  sbc: 30000
  c_goce: 0.206
  c_incapacidad: 0.0175
  c_retiro: 0.02375
  c_vivienda: 0.05
  c_insh: 0.0175
  prima: 0.0054355
steps:
  - goce: sbc * c_goce
  - incapacidad: sbc * c_incapacidad
  - retiro: sbc * c_retiro
  - vivienda: sbc * c_vivienda
  - insh: sbc * c_insh
  - riesgo: sbc * prima
  - total_patron: goce + incapacidad + retiro + vivienda + insh + riesgo
expected:
  total_patron: 9605.57
```

CDMX employer with MXN 100,000 monthly payroll, 3% state payroll tax
(rate needs confirmation against the 2026 CDMX Fiscal Code):

```oa-check
name: CDMX payroll tax on 100000 monthly payroll
inputs:
  nomina: 100000
  tasa_cdmx: 0.03
steps:
  - impuesto_nomina: nomina * tasa_cdmx
expected:
  impuesto_nomina: 3000.00
```

## 9. Ask the client / sources

Ask: Which decreto-prima class is registered — does it match the actual
activities (Art. 73)? Is the SBC complete (aguinaldo, prima,
allowances)? Any foreign nationals needing totalisation certificates?
PTU exposure: modified fiscal result and the two-cap comparison?

Sources: LSS consolidated PDF (diputados.gob.mx, read 2026-10-27); LFT
consolidated PDF (fetched 2026-10-27); IMSS site (browser-reachable;
urllib 403 on 2026-10-27). Needs-sources: 2026 minimum wage and SBC
ceiling, current Art. 95/201 schedules, state payroll tax codes,
totalisation agreement list.

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
