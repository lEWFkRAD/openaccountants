---
name: gp-payroll-withholding
description: >
  Guadeloupe payroll withholding (prélèvement à la source) reference for
  2026. The French PAS applies in Guadeloupe with its own default withholding
  grid (Guadeloupe/Réunion/Martinique grid, distinct from the metropolitan
  and Guyane/Mayotte grids). Covers the employer's withholding duty, the
  DOM grid, remittance via DSN, the non-resident supplementary tax, and
  penalties. Source-cited draft built on the France pack's verified payroll
  figures.
jurisdiction: GP
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Guadeloupe payroll withholding

## 1. Scope and sources

PAS (prélèvement à la source) under CGI Art. 204 A ff applies unchanged in Guadeloupe; only the **default (neutral) withholding grids** differ: "Guadeloupe, La Reunion and Martinique have their own grid, and Guyane and Mayotte a third grid" — France pack `france-payroll.md`, official page read 19 Sep–19 Oct 2026. legifrance 403 on 2026-10-22.

## 2. Who withholds

Every Guadeloupe employer withholds monthly at the rate transmitted by the DGFiP through the DSN (individual rate, or the DOM default grid where the employee has opted for non-disclosure or no rate is available). The withholding is the employee's income tax; the employer is a collecting agent.

## 3. Mechanics

| Item | Rule | Source |
|---|---|---|
| Rate source | DGFiP individual rate via DSN; otherwise the Guadeloupe default grid | France pack `france-payroll.md` |
| Remittance | monthly (or quarterly ≥11 monthly payslips) with the DSN payment (BRS/virement SEPA) | same |
| DOM grid difference | the DOM grids reflect the Art. 197 B reduction — do not apply the metropolitan grid | same |
| Non-resident employees | the 20% (min €3,000) supplementary tax of Art. 1657 A applies to French-source income where net income exceeds the thresholds | France pack |

## 4. Deadlines

DSN and payment: by the 5th of the following month (companies ≥ 11 employees) or the 15th (smaller), per the standard URSSAF/DGFiP calendar.

## 5. Penalties

Failure to withhold or remit: the employer owes the tax plus the Art. 1726/1732 increases (5% default, 10% for repeated failure) and interest in arrears.

## 6. Cross-border points

Mainland-group secondments into Guadeloupe: withholding follows the place of employment (Guadeloupe employer or PE); the DOM grid applies to the taxable DOM remuneration. See `gp-cross-border`.

## 7. Worked examples

**Example 1 — annualisation check.** Employee net taxable €40,000; barème tax €5,103.99 (see `gp-income-tax-individuals`). Before the Art. 197 B reduction the implied average rate is 5,103.99 / 40,000 = 12.76%; monthly withholding ≈ 425.33. With the 40% Art. 197 B reduction (rate needs-sources) the net tax is 3,062.39 → ≈ 7.66% / €255.20 monthly.

```oa-check
name: PAS annualisation EUR 40,000 gross barème
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

**Example 2 — employer failed to remit one month (€425.33).**
Tax owed 425.33 + 5% default (Art. 1726) = 21.27 → total 446.60 (interest excluded).

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

1. Is the employer using the DOM grid or the individual DGFiP rate?
2. Are seconded mainland employees' grids correct?
3. DSN filing frequency and BRS calendar.
4. Any Art. 1657 A non-resident exposure.

## 9. Sources

- France pack `france-payroll.md` (DOM grids, official page read 19 Sep–19 Oct 2026).
- CGI Art. 204 A ff, 1726, 1732 — [Legifrance](https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069044/) (403 on 2026-10-22).
