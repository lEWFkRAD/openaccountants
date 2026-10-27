---
name: pr-payroll-withholding
description: >
  Puerto Rico payroll and information withholding reference for 2026. Covers wage withholding under Code 1-2011 section 1062.01, 10 percent withholding on settlements (1062.02) and service payments (1062.03), 30 percent withholding on special-partnership and S-corporation allocations (1062.04-1062.05), the 2 percent per 30-day failure-to-deposit penalty (6041.01), and the 15 April return framework (1061.16-1061.17). Trigger on Puerto Rico withholding, retencion en el origen, 499R, planilla PR payroll. Source-cited draft.
jurisdiction: PR
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Puerto Rico payroll withholding (Subtítulo A B)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: the OGP consolidated
PDF of the Código de Rentas Internas de Puerto Rico de 2011 (rev. 28 May
2026) was read directly; §§1062.01-1062.05, 1061.16-1061.17, 6041.01 are
quoted from that text. The current withholding tables (tablas de retención
that Hacienda publishes) are needs-sources.

## 2. Who applies

Every "patrono" withholding on wages (§1062.01, read), every payer of
judicial or settlement payments constituting taxable income (10% —
§1062.02, read), and every business paying for services performed in PR
(10% — §1062.03, read, including health-care providers) must withhold and
deposit. Special partnerships and corporations of individuals must
withhold 30% on resident partners' and shareholders' distributable
shares (§§1062.04-1062.05, read).

## 3. Rates

| Payment | Rate | Source |
|---|---|---|
| Wages | per Hacienda withholding tables | §1062.01 (tables needs-sources) |
| Settlement / indemnity payments that are taxable income | 10% (payments after 31 Dec 2018) | §1062.02 (read) |
| Payments for services | 10% (payments after 31 Dec 2018) | §1062.03 (read) |
| Special-partnership distributable share (resident individual / non-resident US-citizen partner) | 30% of estimated share, less other withholding | §1062.04 (read) |
| S-corporation (corporación de individuos) shareholder share | 30% plus applicable rate on corporate-level items | §1062.05 (read) |
| Non-resident individuals / foreign corporations PR-source income | 29% / 10% dividends etc. | §§1091.01, 1092.01 — see pr-cross-border |

## 4. Base and timing

Wages include compensation in any medium for employee services
(§1062.01(a)(1), read); agricultural exclusions ended for payments after
31 December 2018 (read). Service-payment withholding applies to payments
made in the exercise of a trade or business in PR (§1062.03(a), read).
Deposits of withheld amounts follow the Subtítulo A B deposit terms; the
failure-to-deposit penalty runs per 30-day period, so deposit timing is
the compliance risk (§6041.01, read).

## 5. Deadlines

| Obligation | Deadline | Source |
|---|---|---|
| Income-tax return (calendar-year individuals and corporations) | 15 April | §1061.16(a)(1) (read) |
| Automatic extension | 3 months, per Secretary's rules | §1061.16(a)(2) (read) |
| Payment of tax due | 15 April (calendar-year) | §1061.17(a) (read) |
| Withholding deposits | per Subtítulo A B schedule (needs-sources for current cadence) | §6041.01 (penalty read) |
| Annual wage statements (499R series) | 31 January (needs-sources) | administrative |

## 6. Penalties and interest

Failure to deposit withheld tax: 2% of the shortfall for up to 30 days,
plus 2% per additional 30-day period, capped at 24% (§6041.01(a), read).
Failure to file: 5% within 30 days plus 10% per additional 30-day period
(§6030.11, read). Interest on deficiencies and unpaid amounts: 10%
annually (§§6030.01-6030.02, read).

## 7. Cross-border interactions

Payments to non-resident individuals and foreign corporations for
PR-source items are taxed under Chapter 10 (29%/10%/33%) — see
pr-cross-border; the service-payment withholding of §1062.03 can overlap
with the Chapter 10 charge, and the payer must classify the payee first.
US-mainland businesses with PR service providers are PR-source payers
and must withhold 10% unless exempted by the Secretary's rules.

## 8. Worked examples

A PR company pays a local consultant USD 50,000 for services performed
in Puerto Rico (§1062.03, 10%):

```oa-check
name: 10 percent withholding on a 50000 service payment
inputs:
  pago: 50000
  tasa: 0.1
steps:
  - retencion: pago * tasa
  - neto_al_proveedor: pago - retencion
expected:
  retencion: 5000.00
  neto_al_proveedor: 45000.00
```

A special partnership allocates income to a resident individual partner:
the administrator withholds the greater of the computed amounts, 30% of
the estimated distributable share less other withholding (§1062.04, read)
— mechanics shown in the statute; the partner's own estimated-tax
obligation runs in parallel.

## 9. Ask the client / sources

Ask: Are the current Hacienda withholding tables loaded in payroll? Are
service vendors being screened for 10% withholding and TIN reporting?
Are settlement payments being reviewed for the 10% rule? Are partnership
allocations going through §1062.04 withholding? Deposit cadence
documented against the 2%-per-30-day penalty?

Sources: OGP consolidated Code PDF (read 2026-10-27). Needs-sources:
current withholding tables, deposit cadence, 499R filing dates.

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
