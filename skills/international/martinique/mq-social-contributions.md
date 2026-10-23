---
name: mq-social-contributions
description: >
  Martinique social contributions reference for 2026. Employers and workers
  in Martinique pay French social charges on the DOM URSSAF scales: the
  overseas general reduction of employer contributions on low wages, the
  fixed 3.10% family-allowance rate used in the overseas departments, and
  the progressive overseas health-insurance scale with its 24-month start-up
  exemption. Covers who pays, verified DOM rates, bases, DSN filing with
  the CGSS Martinique, penalties. Source-cited draft built on the France
  pack's verified outre-mer figures.
jurisdiction: MQ
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Martinique social contributions

## 1. Scope and sources

French social-security legislation applies in Martinique with overseas scales. Figures carried from the France pack (`fr-social-contributions.md`, official URSSAF/legal pages read 19 Sep–19 Oct 2026), which flags the overseas branch: fixed rather than progressive health scales, a 24-month start-up exemption, abatement from year 3 (T2-8). legifrance 403 on 2026-10-22; full current rate tables needs-sources.

## 2. Who pays

- **Employers**: CGSS Martinique collections; the overseas general reduction applies on low wages with DOM-specific SMIC-multiple thresholds.
- **Self-employed**: independent-worker regime with the overseas health scale and start-up exemption.
- **Employees**: standard employee-side contributions; CSG/CRDS at national rates.

## 3. Verified DOM rates

| Contribution | Rate | Source |
|---|---:|---|
| Allocations familiales (employer, fixed, overseas) | 3.10% of activity income | France pack, official page read 19 Oct 2026 |
| Health insurance (self-employed, overseas) | fixed overseas scale; 24-month start-up exemption; abatement from year 3 | France pack T2-8; exact bands needs-sources |

## 4. Bases

Gross remuneration as in the metropole; the overseas general reduction phases out between DOM-specific SMIC multiples — confirm current multiples on the URSSAF overseas rate page before payroll modelling (needs-sources).

## 5. Deadlines

DSN monthly (quarterly for large filers) to CGSS by the standard calendar (5th–15th of the following month by company size).

## 6. Penalties and interest

Late/incorrect DSN: URSSAF administrative surcharges; late-payment interest at the statutory rate. Same regime as the metropole.

## 7. Worked examples

**Example 1 — employer family allowance on €40,000 payroll.**
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

**Example 2 — AF-only illustration pending the DOM reduction table.**
At SMIC level the overseas general reduction can bring remaining employer contributions close to zero; model with current URSSAF overseas thresholds (needs-sources).

```oa-check
name: Payroll 40000 AF-only DOM illustration
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

1. Wage levels vs the DOM SMIC (drives the overseas reduction).
2. Start-up year for self-employed clients (24-month exemption).
3. Sector agreements extended in Martinique.
4. Staff working across DROM boundaries.

## 9. Sources

- France pack `fr-social-contributions.md` (overseas branch, official pages read 19 Sep–19 Oct 2026).
- URSSAF/CGSS overseas rate pages — needs re-read (legifrance 403 on 2026-10-22).
