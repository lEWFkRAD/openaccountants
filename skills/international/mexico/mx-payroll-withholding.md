---
name: mx-payroll-withholding
description: >
  Mexico payroll withholding reference for 2026. Covers employer ISR withholding on wages under LISR Arts. 94-106 and the SAT monthly tariff tables, the February annual adjustment, monthly declarations by the 17th, aguinaldo and PTU treatment on the payroll, and gross-up duties for payments to non-residents. Trigger on Mexico payroll, retencion ISR salarios, tabuladores SAT, aguinaldo, determinacion mensual. Source-cited draft.
jurisdiction: MX
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Mexico payroll withholding (ISR retenciones)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: the LISR consolidated
PDF was read directly (Arts. 94-106 withholding framework); the tariff
tables themselves are published by SAT and are needs-sources. The 2025
tariff values used in the example come from the SAT tabuladores vigente
2025 — confirm the 2026 version against the SAT tariff publication
before filing.

## 2. Who applies

Any employer withholds ISR from wages each calendar month (LISR Art. 96)
by applying the SAT monthly tariff (cuota fija plus the marginal rate on
the excess over the bracket floor). The withholding is a provisional
credit against the worker's annual ISR (Art. 153). Employees with a
single employer and wages below MXN 400,000 with no other taxable income
generally need no annual return (Art. 150) — thresholds needs-sources
for 2026.

## 3. Rates

Wage withholding follows the SAT tabuladores: progressive, top marginal
35% (2026 tables needs-sources; the example uses the 2025 monthly
table). Aguinaldo (15 days minimum wage, LFT Art. 87) is withheld at the
applicable rate; the portion within 30 days of the minimum wage is
exempt (LISR Art. 91 — verify current text). PTU is taxed separately at
the annual tariff, not through the payroll tables (LISR Art. 98).

## 4. Base and timing

Taxable payroll includes wages, seniority premiums, aguinaldo, bonuses
and cash allowances (Art. 94). Exempt items include PTU up to 15x the
minimum wage and savings-fund contributions within limits (Art. 93).
Withholding is computed per calendar month (Art. 96); multi-month or
irregular payments follow proration rules (Arts. 96, 106).

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Determinacion mensual de retenciones plus payment | by the 17th of the following month | LISR Art. 106 |
| Annual adjustment (determinacion anual) for employees | February of the following year | LISR Art. 106 II |
| Employee annual return (when obliged) | 1 April - 30 April | LISR Art. 150 |

## 6. Penalties and interest

Late or undeclared retenciones: CFF Arts. 64-65 penalties (45%-85% /
50%-150%) plus updating and interest (CFF Art. 20). The employer is
jointly liable for ISR withheld but not remitted.

## 7. Cross-border interactions

Payments to non-resident individuals for personal services performed in
Mexico: 25% flat on gross, withheld by the Mexican payer; services are
presumed wholly performed in Mexico once part is performed there, and
payments by a Mexican resident to a foreign related party are presumed
Mexican-source (LISR Art. 156, read) — gross-up applies (see examples).
Seconded employees become Mexican tax residents after 183 days (Art. 9).

## 8. Worked examples

Monthly ISR withholding on a MXN 25,000 salary using the 2025 monthly
tariff bracket floor 22,956.29 (cuota fija 3,189.53, marginal 35% on
the excess) — 2026 table needs-sources:

```oa-check
name: monthly ISR withholding 25000 salary 2025 tariff
inputs:
  salario: 25000
  limite_inferior: 22956.29
  cuota_fixed: 3189.53
  tasaMarginal: 0.35
steps:
  - excedente: salario - limite_inferior
  - impuesto_mensual: cuota_fixed + excedente * tasaMarginal
expected:
  excedente: 2043.71
  impuesto_mensual: 3904.83
```

Employer pays a non-resident instructor MXN 80,000 net for a Mexico City
course (Art. 156, 25% on gross; the payer grosses up):

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

Ask: Are the SAT tabuladores vigente loaded in payroll for the current
year? Are exempt items (PTU up to 15x minimum wage, fund contributions)
coded correctly? Any foreign instructors or contractors paid net — is
the 25% Title V withholding being grossed up? Is the February annual
adjustment calendared?

Sources: LISR consolidated PDF (read 2026-10-27); SAT portal (read
2026-10-27). Needs-sources: 2026 SAT tabuladores, 2026 exemption
thresholds (Art. 93), Art. 91 aguinaldo exemption current text.

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
