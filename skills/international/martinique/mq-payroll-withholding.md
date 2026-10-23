---
name: mq-payroll-withholding
description: >
  Martinique payroll withholding (prélèvement à la source) reference for
  2026. The French PAS applies in Martinique with the Guadeloupe/Réunion/
  Martinique default grid (distinct from the metropolitan and
  Guyane/Mayotte grids). Covers the employer's withholding duty, the DOM
  grid, DSN remittance, the non-resident supplementary tax, and penalties.
  Source-cited draft built on the France pack's verified payroll figures.
jurisdiction: MQ
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Martinique payroll withholding

## 1. Scope and sources

PAS under CGI Art. 204 A ff applies unchanged in Martinique; only the default (neutral) withholding grids differ — "Guadeloupe, La Reunion and Martinique have their own grid" (France pack `france-payroll.md`, official page read 19 Sep–19 Oct 2026). legifrance 403 on 2026-10-22.

## 2. Who withholds

Every Martinique employer withholds monthly at the DGFiP-transmitted rate via the DSN (individual rate, or the Martinique default grid where the employee opts for non-disclosure). The withholding is the employee's income tax; the employer collects.

## 3. Mechanics

| Item | Rule | Source |
|---|---|---|
| Rate source | DGFiP individual rate via DSN; otherwise the Martinique default grid | France pack `france-payroll.md` |
| Remittance | monthly (quarterly ≥11 monthly payslips) with the DSN payment | same |
| DOM grid difference | DOM grids reflect the Art. 197 B reduction — do not use the metropolitan grid | same |
| Non-resident employees | Art. 1657 A supplementary tax (20%, min €3,000) where thresholds exceeded | France pack |

## 4. Deadlines

DSN + payment by the 5th (≥11 employees) or 15th (smaller) of the following month.

## 5. Penalties

Failure to withhold/remit: employer owes the tax plus Art. 1726/1732 increases (5% default, 10% repeated) and interest.

## 6. Cross-border points

Metropole-group secondments into Martinique: withholding follows the place of employment; the DOM grid applies to taxable DOM remuneration. See `mq-cross-border`.

## 7. Worked examples

**Example 1 — annualisation.** Net taxable €40,000; barème tax €5,103.99 (`mq-income-tax-individuals`). Implied rate 12.76%; monthly ≈ €425.33 before Art. 197 B.

```oa-check
name: PAS annualisation EUR 40,000 barème
inputs:
  tax: 5103.99
  income: 40000
steps:
  - monthly: tax / 12
  - rate_pct: tax / income * 100
expected:
  monthly: 425.33
  rate_pct: 12.76
```

**Example 2 — one unremitted month (€425.33).**
425.33 + 5% (Art. 1726) = 21.27 → 446.60 total (interest excluded).

```oa-check
name: Unremitted PAS month
inputs:
  tax: 425.33
steps:
  - default: tax * 0.05
  - total: tax + default
expected:
  total: 446.60
```

## 8. Ask the client first

1. DOM grid vs individual DGFiP rate in use.
2. Seconded metropole employees' grids.
3. DSN frequency and BRS calendar.
4. Art. 1657 A non-resident exposure.

## 9. Sources

- France pack `france-payroll.md` (DOM grids, official page read 19 Sep–19 Oct 2026).
- CGI Art. 204 A ff, 1726, 1732 — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22).
