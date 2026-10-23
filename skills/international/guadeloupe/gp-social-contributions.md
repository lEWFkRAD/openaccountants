---
name: gp-social-contributions
description: >
  Guadeloupe social contributions reference for 2026. Employers and workers
  in Guadeloupe pay French social charges on the DOM URSSAF scales: reduced
  employer contribution scales (the overseas general reduction), the fixed
  3.10% family-allowance rate used in the overseas departments, and the
  progressive overseas health-insurance scale with its start-up exemption.
  Covers who pays, the verified DOM rates, bases, filing with URSSAF
  Guadeloupe, penalties. Source-cited draft built on the France pack's
  verified outre-mer figures.
jurisdiction: GP
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Guadeloupe social contributions

## 1. Scope and sources

French social-security legislation applies in Guadeloupe with overseas scales. The figures below are carried from the France pack (`fr-social-contributions.md`, official URSSAF/legal pages read 19 Sep–19 Oct 2026), which flags the overseas branch explicitly: "the overseas scales are fixed rather than progressive for health, there is a 24 month start-up exemption and then an abatement in the third and later years" (T2-8). legifrance.gouv.fr 403 on 2026-10-22; full current rate tables need re-verification (needs-sources).

## 2. Who pays

- **Employers** in Guadeloupe: URSSAF Guadeloupe (CGSS) collections; the overseas general reduction of employer contributions applies on low wages (the L.241-13-type overseas variant with its own thresholds).
- **Self-employed**: the independent-worker regime with the overseas health scale and its start-up exemption.
- **Employees**: standard employee-side contributions; CSG/CRDS at the national rates.

## 3. Verified DOM rates

| Contribution | Rate | Source |
|---|---:|---|
| Allocations familiales (employer, fixed, overseas) | 3.10% of activity income | France pack, official page read 19 Oct 2026 ("Allocations familiales en Outre-mer … 3,10 %") |
| Health insurance (self-employed, overseas) | fixed overseas scale, 24-month start-up exemption, abatement from year 3 | France pack T2-8; exact bands needs-sources |
| Mayotte-specific ceilings | not applicable to Guadeloupe | context |

## 4. Bases

Gross remuneration like the metropole; the overseas general reduction phases out between SMIC multiples specific to the DOM — confirm the current threshold multiples on the URSSAF overseas rate page before payroll modelling (needs-sources).

## 5. Deadlines

DSN (déclaration sociale nominative) monthly (or quarterly for large filers) to URSSAF/CGSS by the standard DSN calendar (5–15th of the following month per company size).

## 6. Penalties and interest

Late/incorrect DSN: URSSAF administrative surcharges (percentage-of-contributions scales); late payment interest at the statutory rate. Same regime as the metropole.

## 7. Worked examples

**Example 1 — employer family allowance on €40,000 of payroll.**
3.10% × 40,000 = 1,240.00.

```oa-check
name: Family allowance overseas fixed rate on EUR 40,000
inputs:
  payroll: 40000
steps:
  - af: payroll * 0.031
expected:
  af: 1240.00
```

**Example 2 — the same employer's other contributions are scale-dependent.**
At the SMIC level the overseas general reduction can bring the employer's remaining contributions close to zero; model with the current URSSAF overseas threshold multiples (needs-sources) rather than the mainland scale.

```oa-check
name: Payroll 40000, AF-only illustration of DOM fixed rate
inputs:
  payroll: 40000
steps:
  - af: payroll * 0.031
  - other_contributions: 0
  - total_modelled: af + other_contributions
expected:
  total_modelled: 1240.00
```

## 8. Ask the client first

1. Wage level relative to the DOM SMIC (drives the overseas general reduction).
2. Start-up year for a self-employed client (24-month health exemption).
3. Sector-specific agreements (Guadeloupe extensions differ).
4. Whether staff work across DROM boundaries (aggregation rules).

## 9. Sources

- France pack `fr-social-contributions.md` (overseas branch, official pages read 19 Sep–19 Oct 2026).
- URSSAF overseas rate pages — needs re-read (legifrance 403 on 2026-10-22).
