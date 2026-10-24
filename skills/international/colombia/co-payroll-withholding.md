---
name: co-payroll-withholding
description: >
  Use this skill whenever asked about Colombian payroll and source withholding (retención en la fuente, agentes de retención, Formulario 350, UGPP, seguridad social nómina, ARL, parafiscales). Trigger on phrases like "retención en la fuente Colombia", "agente de retención DIAN", "formulario 350", "seguridad social empleado", "parafiscales SENA ICBF", "UGPP", "ARL empleador", "pila empleador", "withholding Colombia payroll". Covers employer social-security and parafiscal rates, employee pension/health/solidarity contributions, ARL risk classes, withholding-agent obligations and monthly Form 350 filing, penalties and interest. Tax year 2026 draft; current-year resolution figures flagged needs-sources.
jurisdiction: CO
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-24
version: 0.1
---

# Colombia payroll withholding and employer contributions

## 1. Who applies

- **Withholding agents (agentes de retención)** — persons/entities designated by DIAN that must withhold income tax and VAT on payments to Colombian suppliers and on payments to non-residents. Designation follows DIAN's annual resolution criteria (gross income/patrimonio thresholds); the current 2026 resolution text is **needs-sources** (pgn.gov.co did not resolve 2026-10-24).
- **Every employer** — must pay social security and parafiscales on each employee's Ingreso Base de Cotización (IBC) monthly via the PILA planilla; enforcement by UGPP.
- **Payers to independents** — service fees attract withholding per the same DIAN resolution (see `co-social-contributions` for the independent's own contributions).

## 2. Rates and thresholds

Employee-side and employer-side social security on the IBC (statutory rates stable for years; confirm against current UGPP/DIAN resolution before filing):

| Component | Employee | Employer | Notes |
|---|---|---|---|
| Pension | 4.0% | 12.0% | IBC floor 1 SMMLV, cap 25 SMMLV |
| Health (salud) | 4.0% | 12.5% | EPS |
| Occupational risk (ARL) | — | 0.522%–6.960% | by risk class I–V |
| Labor solidarity fund | 1.0% (IBC > 4 SMMLV) | — | Ley 21/1982 |
| SENA | — | 2.0% | parafiscal |
| ICBF | — | 3.0% | parafiscal |
| Cajas de compensación | — | 4.0% | parafiscal |

Income-tax withholding on employment (retención en la fuente por rentas de trabajo) runs on a monthly table expressed in UVT; the 2026 table comes from the annual DIAN resolution — **needs-sources** for the current table values.

Withholding on payments to non-residents (statutory maxima, ET arts. 398, 408; treaty rates override):

| Payment type | Rate |
|---|---|
| Technical services, royalties, software | 20% |
| Interest | 15%–20% |
| Dividends from taxed profits | 20% (ET art. 245) |

## 3. Base

- Social security: IBC = ordinary monthly salary (plus contractual regular allowances); floor 1 SMMLV, ceiling 25 SMMLV.
- Income-tax withholding on wages: monthly base after the statutory rentas exentas/deducciones allowances, annualised through the cédula general table (see `co-income-tax`).
- Non-resident withholding: gross payment, no deductions, unless a treaty applies.

## 4. Deadlines

- PILA social-security planilla: last business day of the month the salaries relate to (UGPP calendar).
- Form 350 (retenciones en la fuente): monthly, DIAN calendar staggered by NIT last digits — see [DIAN Calendario Tributario](https://www.dian.gov.co/Paginas/CalendarioTributario.aspx).
- Information returns (220, 221, exógena): annual, DIAN calendar.

## 5. Penalties and interest

- Late/under-declared withholding: 5%–100% of the withheld amount not reported (ET art. 667); 10% where no return filed (art. 651).
- Interest: bank current-liability rate + 20% annual (ET art. 635) on unpaid amounts.
- Social-security shortfall: UGPP charges moratory interest plus fines; the employer is directly liable for employee-side amounts it failed to deduct.

## 6. Cross-border

- Payments to non-residents for services/royalties: withhold at the rates in §2; treaty relief requires a certificate of tax residence and DIAN's Form 1042 procedure.
- Foreign employees: Colombia-source employment income is taxable where services are rendered in Colombia, regardless of payer location.

## 7. Worked examples

**Example 1 — withholding on a service invoice to a Colombian company (2026).**

```oa-check
name: Service payment 100,000,000 COP, 20% general withholding
inputs:
  gross: 100000000
steps:
  - wht: gross * 0.20
  - net: gross - wht
expected:
  wht: 20000000
  net: 80000000
```

**Example 2 — professional fees at the reduced professional rate.**

```oa-check
name: Honorarios 50,000,000 COP at 11%
inputs:
  gross: 50000000
steps:
  - wht: gross * 0.11
expected:
  wht: 5500000
```

(The 11% professional-fee rate and the 3.5% other-payments rate come from the annual DIAN resolution; verify the current resolution before applying — **needs-sources**.)

## 8. Ask the client

1. Is the payer a designated withholding agent (resolución DIAN)?
2. What is the payment type — honorarios, servicios, comisiones, arrendamiento?
3. Employee vs independent contract (contrato de prestación de servicios)?
4. Risk class (ARL) for the activity?
5. Any treaty claim with a certificate of residence?

## 9. Sources

- [DIAN — main site](https://www.dian.gov.co/) — read 2026-10-24.
- [DIAN — Calendario Tributario](https://www.dian.gov.co/Paginas/CalendarioTributario.aspx) — read 2026-10-24.
- Estatuto Tributario arts. 398, 408, 245, 651, 667, 635 — cited via earlier pack skills; gazette text **needs-sources** (pgn.gov.co DNS unresolved 2026-10-24).
- Existing pack skill `co-social-contributions` — IBC/PILA mechanics carried forward with its citations.

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
