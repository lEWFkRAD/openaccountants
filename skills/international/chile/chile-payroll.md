---
name: chile-payroll
description: >
  Chile payroll withholding reference for 2026. Covers second-
  category (employment) tax withholding on wages, the AFP 10%
  pension and 7% health (Fonasa/Isapre) employee deductions with
  the pensionable-income cap, the boleta de honorarios withholding
  at 15.25% for 2026 (stepping to 17% by 2028), PPM provisional
  monthly payments and their credit into the April Operacion Renta,
  employer pension/accident insurance duties, SII Form 29/61
  remittance deadlines and penalties. Trigger on Chile payroll,
  retencion, boleta de honorarios, AFP, PPM, Operacion Renta
  withholding. Source-cited draft.
jurisdiction: CL
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Chile payroll withholding

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: the SII boleta de
honorarios pages (sii.cl — 2026 withholding 15.25% confirmed on the
SII's own page) and the PwC Chile personal-income chapter (IGC and
employment-tax bands, USD/UTM basis with a 28 June 2017 base-date
caveat). Currency: peso (CLP); brackets are expressed in UTM. The
existing reviewed skills `cl-income-tax` and `cl-social-contributions`
cover the independent-worker side; this skill is the **payroll /
withholding agent** view.

## 2. Who the rules apply to

- **Employers (pagadores de rentas de segunda categoria)**: withhold
  monthly second-category tax from wages using the SII monthly table,
  plus the employee's AFP 10% and health 7% deductions, and remit via
  Form 29 / Declaracion de Retenciones (Form 61/102).
- **Anyone paying independent fees (honorarios)**: the payer withholds
  the boleta de honorarios retention — **15.25% for 2026** (SII, read
  2026-10-24; 14.5% in 2025, rising to 17% by 2028 under Ley 21.133's
  phase-in). Since 2023 the retention is computed automatically inside
  the electronic boleta.
- **Non-resident service providers without Chilean residence**: taxed
  at source — 35% additional on services (15% flat for qualifying
  technical/engineering services rendered from abroad through a
  report/advice/plan — PwC Chile personal income, read 2026-10-24).

## 3. Rates table

| Withholding / deduction | Rate | Base | Source |
|---|---|---|---|
| Boleta de honorarios retention (2026) | 15.25% | Gross fee on the electronic boleta | SII boletas_honorarios page, read 2026-10-24 (14.5% 2025; 16% 2027; 17% 2028) |
| Second-category (employment) monthly tax | progressive monthly UTM bands (annual equivalent 0–35.5%) | Renta imponible after AFP/health deductions | PwC Chile personal income (employment-tax bands, 2017 USD basis) — 2026 UTM table **needs-sources** |
| AFP pension (employee) | 10% + AFP commission | Pensionable wage, capped at ~66.5 UF (2026 cap **needs-sources**) | cl-social-contributions (reviewed); DL 3.500 |
| Health (Fonasa/Isapre, employee) | 7% | Renta imponible | cl-social-contributions (reviewed) |
| Employer pension/accident duties | AFP top-up rules vary; Ley 16.744 accident insurance | Payroll | cl-social-contributions — employer rates **needs-sources** |
| Non-resident services (no residence) | 35% additional (15% flat for qualifying technical services from abroad) | Gross fee | PwC Chile personal income, read 2026-10-24 |

The retention on boletas is a **provisional credit** (PPM-like) against
the worker's annual IGC in the April Operacion Renta — it is not a
final tax.

## 4. Tax base and computation

- Employee wage withholding base = gross remuneration minus AFP 10%
  and health 7% (the "renta imponible"); the monthly SII table applies
  to that base. The AFP deduction is capped at the pensionable-income
  ceiling (~66.5 UF — confirm the 2026 UF value, **needs-sources**).
- Honorarios base for IGC purposes: 2026 independent workers compute
  taxable income on gross fees less the law's presumed/actual expense
  and pension-credit rules (see cl-income-tax; the 2025+ reform
  schedule is **needs-sources** for 2026 exact percentages).
- PPMs (Form 29 provisional payments for businesses) and boleta
  retentions accumulate as credits in Form 22 (Operacion Renta).

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Form 29 (VAT + withholdings) | Monthly, ~12th–15th per SII calendar (day varies by terminal digit) | SII vencimientos — exact 2026 day **needs-sources** |
| Boleta retention remittance | With the payer's monthly Form 29/retention declaration | SII, read 2026-10-24 |
| Operacion Renta (Form 22) | Before 30 April (electronic; extensions possible) | PwC Chile tax administration, read 2026-10-24 |
| Cotizaciones previsionales (AFP/health) | By the 10th of the following month | Superintendencia de Pensiones — **needs-sources** confirm |

## 6. Penalties and interest

Late withholding remittance: interest at the banking average rate
(promedio) plus penalties under Art. 97 CT (percent of the unpaid
amount; graduated by self-correction timing — exact 2026 percentages
**needs-sources**). Failure to withhold makes the payer jointly liable.
Statute of limitations: 3 years, 6 if no return filed or maliciously
false return (PwC Chile tax administration, read 2026-10-24).

## 7. Worked examples

**Example 1 — boleta de honorarios, 2026 retention.** A professional
issues a CLP 1,000,000 electronic boleta in 2026: the payer withholds
15.25% automatically.

```oa-check
name: boleta retention 2026 15.25
inputs:
  fee: 1000000
  retention: 15.25
steps:
  - withheld: fee * pct(1, retention)
  - net: fee - withheld
expected:
  withheld: 152500.00
  net: 847500.00
```

**Example 2 — employee monthly deductions.** A CLP 2,000,000 gross
wage (below the pensionable cap): AFP 10% and health 7% come off
before the second-category table applies.

```oa-check
name: employee deductions 2m
inputs:
  gross: 2000000
  afp: 10
  salud: 7
steps:
  - afp_ded: gross * pct(1, afp)
  - salud_ded: gross * pct(1, salud)
  - imponible: gross - afp_ded - salud_ded
expected:
  afp_ded: 200000.00
  salud_ded: 140000.00
  imponible: 1660000.00
```

## 8. Ask the client first

1. Are boletas de honorarios being issued electronically with the
   2026 15.25% retention (the SII computes it automatically — manual
   13%/14.5% boletas are a red flag)?
2. Are Form 29 retention lines reconciled to payroll and boletas each
   month?
3. Is the worker's pensionable base capped correctly (UF ceiling)?
4. For foreign service providers: does the payment qualify for the
   15% technical-services flat rate or the 35% additional?

## 9. Sources

- [SII — Boleta de Honorarios 2026 (15.25%)](https://www.sii.cl/destacados/boletas_honorarios/index.html) — read 2026-10-24.
- [SII — Boletas de honorarios electronicas](https://www.sii.cl/servicios_online/1040-1287.html) — read 2026-10-24.
- [PwC — Chile taxes on personal income](https://taxsummaries.pwc.com/chile/individual/taxes-on-personal-income) — read 2026-10-24 (IGC/employment bands, non-resident 15% flat).
- [PwC — Chile tax administration](https://taxsummaries.pwc.com/chile/corporate/tax-administration) — read 2026-10-24 (30 April, limitation).
- Existing reviewed skills `cl-income-tax`, `cl-social-contributions` — independent-worker side with their citations.
- 2026 UTM/UF tables and Art. 97 CT penalty percentages — **needs-sources**.

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
