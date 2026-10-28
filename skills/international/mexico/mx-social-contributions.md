---
name: mx-social-contributions
description: >
  Mexico social contributions (IMSS) reference for 2026. Covers employer and worker quotas under the Ley del Seguro Social (Arts. 28, 38, 39, 73, 147, 168, 211), the five occupational-risk classes, the SBC base and its 25x minimum-wage ceiling, INFONAVIT 5%, the retirement branch, state payroll taxes, monthly cedula payment by the 17th, and PTU. Trigger on Mexico IMSS, cuotas obrero patronales, salario base de cotizacion, INFONAVIT, PTU, prima de riesgo. Source-cited draft.
jurisdiction: MX
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
---

# Mexico social contributions (IMSS, INFONAVIT, PTU)

> **Source-cited draft.** Built from the Cámara de Diputados consolidated texts of the Ley del Seguro Social (LSS) and the Ley del Instituto del Fondo Nacional de la Vivienda para los Trabajadores (LIFNVT), and the INFONAVIT employer help pages, read on 2026-10-28. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Mexican professional.

Tax year: the calendar year. Currency: Mexican peso (MXN). The Instituto Mexicano del Seguro Social (IMSS) collects social security quotas; INFONAVIT receives the housing contribution.

See also: `mx-payroll-withholding` (ISR on wages), `mx-corporate-income-tax` (PTU deduction).

## Who this applies to

Every employer (patrón) with workers in Mexico registers with IMSS, withholds the worker quotas from wages (LSS Art. 38) and pays the combined obrero-patronal quotas. Cooperatives pay the employer quota and their members pay as workers (Art. 19). Independent workers can affiliate voluntarily.

## Rates, bands and thresholds

Quotas are on the salario base de cotización (SBC). The ceiling is 25 times the general minimum wage and the floor is the general minimum wage of the area (LSS Art. 28).

| Branch | Employer | Worker | Tax year | Source |
|---|---|---|---|---|
| Disability and life (invalidez y vida) | 1.75% | 0.625% | 2026 | [LSS Art. 147](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Retirement (retiro, SAR) | 2% | — | 2026 | [LSS Art. 168 fr. I](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Daycare and social benefits (guarderías y prestaciones sociales) | 1% | — | 2026 | [LSS Art. 211](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |
| Housing (INFONAVIT) | 5% of wages | — | 2026 | [LIFNVT Art. 29 fr. II](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIFNVT.pdf); [INFONAVIT employer FAQ](https://portalmx.infonavit.org.mx/wps/portal/infonavitmx/mx2/patrones/centro_ayuda/preguntas_frecuentes/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zizTxdDAwtnA2MLA0NDAzM_J193ZxMTQ09w0z1C7IdFQHkqnMl/) |
| Occupational risk, average premium on first registration or change of activity | 0.54355% (class I) to 7.58875% (class V) | — | 2026 | [LSS Art. 73](https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf) |

## The taxable base

**SBC** is built from fixed pay plus, where pay has variable elements, the average of variable pay over the prior two months (LSS Art. 30). Cash plus in-kind payments and the proportional aguinaldo and seniority premium form part of it.

**Accrual.** Quotas accrue by months in arrears (Art. 39).

**PTU.** PTU paid is deductible for ISR (LISR Art. 9 fr. I). The PTU computation itself is on the "Not yet confirmed" line under Sources.

## Deadlines and filing

| Obligation | Deadline | Source |
|---|---|---|
| IMSS cédula de determinación plus payment | By the 17th of the following month | LSS Art. 39 |
| Worker quota withholding by employer | Each payroll; if not withheld on time, the employer may recover at most four accumulated weekly quotas from the worker | LSS Art. 38 |

## Penalties and interest

Quotas or capitales constitutivos not paid on time bear inflation updating and surcharges (recargos) under the Código Fiscal de la Federación from the date they became due, without prejudice to fines (LSS Art. 40 A). Article 304 A lists the employer acts and omissions that are infractions. IMSS can assess capitales constitutivos for individual claims; they are definitive on notification (Art. 39).

## Cross-border points

- **Foreign employers.** A foreign employer with Mexican staff must register through a PE or a Mexican representative.
- Totalisation agreements and the coverage of seconded staff are on the "Not yet confirmed" line under Sources.

## Worked examples

### Example 1: employer IMSS on a MXN 30,000 SBC, class I

Office work, class I risk premium 0.54355% (Art. 73). The block applies the branch rates earlier drafts used: 20.6% illness and maternity, 1.75% disability and life, 2.375% retirement, 5% housing, 1.75% daycare, plus the risk premium, for a total employer cost of MXN 9,605.57. Only the 1.75% disability-and-life rate, the 5% housing rate and the risk premium are confirmed; the other inputs are not yet confirmed (see Sources).

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

### Example 2: CDMX state payroll tax

A Mexico City employer with MXN 100,000 monthly payroll. At the 3% rate earlier drafts used, the state payroll tax is MXN 3,000. The rate is not yet confirmed against the CDMX Fiscal Code (see Sources).

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

## Ask the client first

1. **Which risk class is registered, and does it match the actual activities** (Art. 73)?
2. **Is the SBC complete** (aguinaldo, premiums, allowances, variable pay)?
3. **Any foreign nationals or seconded staff** who may need a coverage certificate?
4. **PTU exposure:** what is the modified fiscal result, and which cap applies?
5. **In which states does the employer have staff?** State payroll tax follows the state.

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley del Seguro Social, consolidated (Cámara de Diputados), Arts. 19, 28, 30, 38, 39, 40 A, 73, 147, 168, 211, 304 A | https://www.diputados.gob.mx/LeyesBiblio/pdf/LSS.pdf | 2026-10-28 |
| Ley del Instituto del Fondo Nacional de la Vivienda para los Trabajadores, consolidated (Cámara de Diputados), Art. 29 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIFNVT.pdf | 2026-10-28 |
| INFONAVIT, employer help centre: frequently asked questions | https://portalmx.infonavit.org.mx/wps/portal/infonavitmx/mx2/patrones/centro_ayuda/preguntas_frecuentes/!ut/p/z0/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zizTxdDAwtnA2MLA0NDAzM_J193ZxMTQ09w0z1C7IdFQHkqnMl/ | 2026-10-28 |
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Art. 9 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-28 |

Not yet confirmed: the illness-and-maternity rates of 20.6% employer and 3.0% worker (earlier drafts cited LSS Arts. 95, 97; in the text read, Art. 106 finances that branch's benefits in kind); a "retirement, disability, survivors" employer rate of 2.375% (earlier drafts cited Art. 134; the text read puts the employer cesantía y vejez quota in Art. 168 fr. II); a daycare/INSH upper rate of 1.75% (earlier drafts cited Art. 201; Art. 211 sets 1%); the resulting employer total of roughly 20.6% plus a fixed 11.125% plus risk premium, about 31.5% at the top class; the 2026 minimum wage and SBC ceiling in pesos (DOF annual decree); INFONAVIT payment timing (earlier drafts said monthly with the IMSS cédula) and earlier drafts' citation of "INFONAVIT Art. 45"; state payroll tax (impuesto sobre nómina) of about 3% in most states and 3% in CDMX (state codes not archived); a 10% surcharge on unpaid quotas under "LSS Art. 14-A"; PTU of 10% of the modified fiscal result, half split equally and half by wages, capped per worker at the lower of 20 times the local minimum wage or three times the average wage, with directors and non-resident workers excluded (LFT Arts. 123-127), and payment within 60 days of the annual ISR return (no archived copy of the LFT); the list of totalisation agreements and the coverage of seconded staff under the Mexico-US agreement; IMSS circulars (imss.gob.mx refused scripted access).

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
