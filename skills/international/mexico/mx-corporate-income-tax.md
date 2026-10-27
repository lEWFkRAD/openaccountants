---
name: NAME
description: >
  DESC
jurisdiction: MX
category: CAT
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Mexico corporate income tax (ISR, personas morales)

## 1. Scope and sources

Source-cited draft, sources read 27 October 2026: the Camara de Diputados
consolidated PDF of the Ley del Impuesto Sobre la Renta (LISR, last reform
DOF 01-04-2024) was read directly; article citations below are from that
text. The Codigo Fiscal de la Federacion (CFF) PDF was fetched for the
penalty framework. Administrative 2026 amounts (UMA, minimum wage,
tariffs) are needs-sources.

## 2. Who applies

Resident Mexican corporations (personas morales) are taxed on worldwide
income (LISR Arts. 8-9). A Mexican-source rule and a permanent-establishment
concept bring non-resident corporations in under Title V — see the
mx-cross-border skill. Mexican branches of foreign companies are taxed as
resident corporations; a foreign corporation without a PE pays the
Title V flat rates instead.

## 3. Rates

| Item | Rate | Source |
|---|---|---|
| Corporate ISR on the annual fiscal result | 30% | LISR Art. 9 (read 2026-10-27) |
| Corporate-level tax on distributed dividends | 30% via gross-up factor 1.4286 | LISR Art. 10 |
| Additional tax on distributions out of post-2014 profits | 10% | LISR Art. 10 (second paragraph) |
| Non-resident flat rates (no PE) | 25% / 35% by income type | LISR Title V — see mx-cross-border |

No general reduced corporate rate exists. The 2025-2026 reform debate
about a rate increase had not changed Art. 9 in the consolidated text
read on 2026-10-27 — verify against the DOF before relying on it.

## 4. Tax base and timing

The annual fiscal result (LISR Art. 9, read): accumulate all Title II
income, subtract authorised deductions (Arts. 25-37) and PTU actually
paid in the year (Constitution Art. 123), then subtract updated
prior-year loss carryforwards. Losses carry forward 8 years,
inflation-updated, with same-line-of-business limits on mergers and
control changes (Art. 57; the control-change paragraph was read from the
Art. 58-adjacent text). Accrual basis; inflation adjustment applies to
certain items (Arts. 44-46). Deductions require strict CFDI invoice
compliance (Art. 27 and the CFF).

Dividends: distributions are tax-free in the recipient's hands only if
paid out of the Cuenta de Utilidad Fiscal Neta (CUFIN, profits taxed
before 2014) or CUFIN-NON-RESIDENTE; otherwise the paying company
grosses the dividend up by the factor 1.4286 and pays 30% (Art. 10,
read), plus 10% additional tax on post-2014 profits. Capital reductions
are recharacterised through the CUFIN waterfall (Art. 78, read).

## 5. Deadlines and filings

| Obligation | Deadline | Source |
|---|---|---|
| Monthly provisional ISR payments | by the 17th of the following month, on the prior year's utilidad/ingresos coefficient (Art. 14, read) | LISR Art. 14 |
| Annual ISR return | within 3 months of year end — 30 July for calendar-year taxpayers | LISR Art. 81 |
| PTU payment | within 60 days of the annual return | LFT Art. 123 |
| Determinations and informative returns (incl. related-party, Art. 76-A) | with the annual return | LISR Arts. 76, 76-A |

## 6. Penalties and interest

CFF (consolidated PDF fetched 2026-10-27; article numbers from the CFF
text): 45%-85% penalty for underpaid amounts (CFF Art. 64), 50%-150% for
false returns (Art. 65), inflation updating plus interest (CFF Art. 20;
the 1.41% monthly rate is needs-sources). IMSS contribution penalties
are covered in mx-social-contributions.

## 7. Cross-border interactions

Payments to non-residents without a PE trigger Title V withholding —
rent and real-property gains 25% flat (Arts. 158, 160, read), services
25% flat (Art. 156, read) — usually grossed up because the Mexican payer
owes the tax as retentor. Treaty relief requires the beneficiary to
prove residence; Mexico's network is extensive but rates vary by treaty
(treaty tables needs-sources). Transfer pricing runs through Arts. 76
(XII), 179-182 and the master/local informative returns (Art. 76-A,
read) — see mexico-transfer-pricing.

## 8. Worked examples

A Mexican S.A. de C.V. has MXN 12,000,000 acumulable income, MXN
8,500,000 authorised deductions, pays PTU of MXN 400,000, and has an
updated loss carryforward of MXN 2,000,000 from two years ago.

```oa-check
name: corporate tax with loss carryforward
inputs:
  ingresos: 12000000
  deducciones: 8500000
  ptu_pagada: 400000
  perdida_cf: 2000000
  tasa: 0.3
steps:
  - utilidad_fiscal: ingresos - deducciones - ptu_pagada
  - resultado_fiscal: utilidad_fiscal - perdida_cf
  - impuesto: resultado_fiscal * tasa
expected:
  utilidad_fiscal: 3100000.00
  resultado_fiscal: 1100000.00
  impuesto: 330000.00
```

The same company distributes a MXN 700,000 dividend out of post-2014
profits (so the 10% additional tax applies to the grossed-up amount):

```oa-check
name: dividend gross-up and 10 percent additional tax
inputs:
  dividendo: 700000
  factor: 1.4286
  tasa: 0.3
  adicional: 0.1
steps:
  - impuesto_dividendo: dividendo * factor * tasa
  - bruto_con_impuesto: dividendo + impuesto_dividendo
  - impuesto_adicional: bruto_con_impuesto * adicional
expected:
  impuesto_dividendo: 300006.00
  bruto_con_impuesto: 1000006.00
  impuesto_adicional: 100000.60
```

## 9. Ask the client / sources

Ask: Is the CUFIN (pre-2014) balance sufficient for planned
distributions? Any control change or merger that limits the loss
carryforward (Art. 57)? Are CFDI requirements met for every deduction
(Art. 27)? Was PTU paid in the year, so it is deductible? Any payments
to non-residents that need Title V withholding before the payment date?

Sources: LISR consolidated PDF (diputados.gob.mx, read 2026-10-27); CFF
consolidated PDF (read 2026-10-27); SAT portal (read 2026-10-27).
Needs-sources: 2026 UMA and minimum wage (DOF/INEGI), current SAT
tariff tables, treaty-by-treaty withholding rates, CFF interest rate.

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
