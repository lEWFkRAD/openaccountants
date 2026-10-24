---
name: ar-payroll-withholding
description: >
  Argentina payroll withholding reference for 2026. Covers employer
  and employee social contributions (11% employer, 3% employee up to
  the tope, plus 3% work-risk insurance, union and obra social
  levies), Ganancias withholding on salaries via the ARCA scale,
  F931 (F31) monthly remittance, and the UOCRA/construction regime.
  Trigger on Argentina payroll, aportes, contribuciones, retenciones
  cuarta categoría, F931, tope, ART. Source-cited draft.
jurisdiction: AR
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.1
verified_by: pending
---

# Argentina payroll withholding

## 1. Scope and sources

Source-cited draft, sources read 24 October 2026: ARCA (ex-AFIP)
empleadores portal (argentina.gob.ar/arca/empleadores), the
information-law portal infoleg.gob.ar (Ley 19.032 work-risk
insurance, Ley 23.660 social-security contributions, Ley 23.661
health insurance, Ley 27.430 tax reform), and the existing AR pack
skills (figures carried forward with their citations). Currency:
Argentine peso (ARS).

**Source status caveat:** the current-year **tope** (contribution
ceiling) and **minimum wage**, and the 2026 Ganancias scale and
deducciones, are updated by decree/RESOLUCIÓN general each year and
were not machine-readable this pass — all are **needs-sources**; the
percentages below are the standing statutory rates.

## 2. Who the rules apply to

- **Employers** in a dependent-employment relationship must register
  with ARCA, withhold the employee contributions and Ganancias
  (fourth-category) each month, pay the employer contributions, and
  remit everything on the F931 (F31) return; they must also carry
  work-risk insurance (ART, Ley 19.032) and pay union/obra-social
  levies.
- **Employees** owe aportes (3% up to the tope) and, above the
  Ganancias threshold, fourth-category withholding collected by the
  employer.
- **Domestic-work and construction** regimes have their own
  simplified contribution tables (UOCRA regime for construction).

## 3. Rates table

| Item | Rate / amount | Base | Source |
|---|---|---|---|
| Employer contributions (contribuciones) | 11% general (reduced regimes: Ley 25.631 small employers, Zona Franca Tierra del Fuego) | Monthly remuneration up to the tope | Ley 24.004 / Ley 24.013 — ar-social-contributions |
| Employee retirement aporte | 3% (additional 1%–2% for higher earners per Ley 27.430 art. 24 bands) | Remuneration up to the tope | Ley 24.241 — ar-social-contributions |
| Work-risk insurance (ART) | ~3% (rate class-dependent) | Remuneration | Ley 19.032 (infoleg, read 2026-10-24) |
| Employee obra social | 3% (employer 6%) | Remuneration up to the tope | Ley 23.661 — ar-social-contributions |
| Union contribution (obra social sindical / aportes solidarios) | ~3% employee + ~3% employer (activity-dependent) | Remuneration | collective bargaining — needs-sources |
| Ganancias 4ª categoría WHT | Progressive scale on net salary after deductions | Monthly salary | Ley 20.628 t.o. — needs-sources for the 2026 scale |
| Tope (contribution ceiling) | 15 × average monthly taxable remuneration (SIP), updated monthly by ANSES | — | Ley 24.241 art. 9 — needs-sources for the current value |
| Minimum wage (SMVM) | Updated by decree | — | needs-sources |

## 4. Tax base and computation

The contribution base is **monthly remuneration in money** (and
in-kind per art. 10 LCT), capped at the tope (15 × the SIP average).
Non-remunerative concepts (gratificaciones extraordinarias per art.
131 bis LCT, utilities, certain reimbursements) are excluded.
Ganancias withholding applies to net salary after the conceptual
deduction (deducción especial) and other deductions, using the
monthly scale published by ARCA; the 14th-salary (aguinaldo) is
taxed on the same basis. Employer computes F931 per employee per
month; the tope applies per month, not annualized.

## 5. Deadlines

- **F931 (F31) return and payment:** monthly, mid-month following the
  period, by ARCA general resolution (exact day by CUIT ending —
  needs-sources).
- **Ganancias withholding remittance:** with the F931 period cycle
  (needs-sources for the 2026 calendar).
- **SIRADIG / SICORE:** employer registration and withholding
  regimes run continuously through ARCA.
- **ART premium:** monthly with contributions.

## 6. Penalties and interest

Underpayment of contributions and withholdings runs through Ley
27.430 libro II penal regime (fines plus interest at the ARCA active
rate); failure to withhold makes the employer jointly liable for the
employee's tax. Section-level amounts: **needs-sources**.

## 7. Worked examples

**Example 1 — monthly employer and employee contributions.** A
salaried employee earns ARS 1,000,000 (below the tope). Employer
contributions 11%, employee retirement 3%, employee obra social 3%,
employer obra social 6%.

```oa-check
name: payroll 1m contributions
inputs:
  gross: 1000000
  emp_contrib: 11
  emp_retiro: 3
  emp_obra: 3
  employer_obra: 6
steps:
  - employer_contrib: gross * pct(1, emp_contrib)
  - employee_retiro: gross * pct(1, emp_retiro)
  - employee_obra: gross * pct(1, emp_obra)
  - employer_obra: gross * pct(1, employer_obra)
expected:
  employer_contrib: 110000.00
  employee_retiro: 30000.00
  employee_obra: 30000.00
  employer_obra: 60000.00
```

**Example 2 — tope caps the contribution base.** The tope is 15 ×
the SIP average; with an illustrative average of ARS 700,000 the tope
is ARS 10,500,000, so a ARS 2,000,000 monthly salary is fully
contributable (confirm the live tope before use).

```oa-check
name: tope 15x average 700k vs salary 2m
inputs:
  avg: 700000
  salary: 2000000
  rate: 11
steps:
  - tope: avg * 15
  - base: min(salary, tope)
  - employer_contrib: base * pct(1, rate)
expected:
  tope: 10500000.00
  base: 2000000.00
  employer_contrib: 220000.00
```

## 8. Ask the client first

1. What is each employee's monthly remuneration and which concepts
   are non-remunerative under the LCT?
2. Is the employer in a reduced-contribution regime (Ley 25.631,
   Tierra del Fuego, domestic work)?
3. Are Ganancias withholdings being run on the current ARCA scale
   with the correct deducción especial, and is SIRADIG/SICORE
   registered?
4. Is the ART policy current and at the correct risk class, and are
   union levies being paid per the applicable convenio colectivo?

## 9. Sources

- [ARCA — Empleadores (argentina.gob.ar)](https://www.argentina.gob.ar/arca/empleadores) — read 2026-10-24.
- [InfoLeg — Ley 19.032 (riesgos del trabajo)](https://www.infoleg.gob.ar/infolegInternet/anexos/0-4999/611/norma.htm) — read 2026-10-24.
- [InfoLeg — Ley 23.660 (aportes y contribuciones SS)](https://www.infoleg.gob.ar/infolegInternet/anexos/35000-39999/37141/norma.htm) — read 2026-10-24.
- [InfoLeg — Ley 23.661 (obras sociales)](https://www.infoleg.gob.ar/infolegInternet/anexos/35000-39999/37142/norma.htm) — read 2026-10-24.
- Existing pack skill `ar-social-contributions` — rate figures carried forward with their citations.

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
