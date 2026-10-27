---
name: sx-social-insurance-premiums
description: >
  Sint Maarten social-insurance premiums AOV, AWW and AVBZ: split employer and
  employee rates (14% plus 2%), the official GRC premium caps and maximum
  premium figures, monthly remittance through the wage-tax return cycle, and
  the penalty exposure for late or incorrect filings. Flags that the published
  caps are 2020 figures and 2026 caps need confirmation. Explains the
  interaction with the wage-tax base (employee premium is deductible from the
  wage-tax ground). Applies to Dutch Sint Maarten.
jurisdiction: SX
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
---

# Sint Maarten: social-insurance premiums (AOV / AWW / AVBZ)

## Who applies

Every employer paying wages in Sint Maarten withholds and remits employee premiums and pays employer premiums alongside the monthly wage-tax return. AOV is old-age insurance, AWW widows' and orphans' insurance, AVBZ the basic health-insurance scheme. The employee premium for AOV/AWW is set by articles 26(1)-(2) of the AOV ordinance and 29(1)-(2) of the AWW ordinance, cited in the GRC's 2026 wage-tax tables.

## Rates (official GRC guide; employee AOV/AWW rate reconfirmed in the 2026 tables)

| Scheme | Employer | Employee | Total |
|---|---|---|---|
| AOV + AWW | 7.5% | 6.5% | 14% |
| AVBZ | 0.5% | 1.5% | 2% |

The GRC's 2026 wage-tax worked example computes the employee AOV/AWW deduction "a 6.5%" "onder voorbehoud dat in 2026 het werknemersdeel AOV/AWW 6,5% bedraagt" — i.e. 6.5% is the operative 2026 employee rate subject to the annual premium regulation.

## Caps — needs-sources for 2026

The official GRC guide publishes **2020** figures: AOV/AWW premium base capped at **NAf 105,382.77** per year (maximum total premium NAf 14,753.59), AVBZ base capped at **NAf 417,357** (maximum total premium NAf 8,347.14). No 2026 cap was retrievable from official sources on 2026-10-27 — confirm the current-year maximum income before running payroll.

## Base and mechanics

- Premium base is the wage paid; the employee AOV/AWW premium is deducted **before** the wage-tax ground: the GRC's 2026 example takes brutoloon Cg 2,473.16, minus verwervingskosten Cg 41.67, minus employee AOV/AWW Cg 158.05 (6.5%), giving a wage-tax ground of Cg 2,273.44.
- Premiums over the annual cap are not due on the excess ("no premium has to be calculated over the excess income").
- Monthly filing and payment for wage tax + AOV/AWW + AVBZ run on the GRC monthly schedule (filing and payment no later than the mid-month date for the preceding month).

## Penalties

Late, missing or unsigned monthly returns, or late payment, produce an assessment increased with a penalty; incorrect/incomplete employer information carries up to NAf 1,000. Two-month motivated written appeal window (see sx-corporate-income-tax).

## Cross-border

Seconded employees: no official totalisation text was retrievable; the Kingdom framework and any bilateral social-security arrangements must be checked per client — do not assume EU coordination applies (Sint Maarten is an OCT).

## Worked examples

**Example 1 — monthly premium split on a Cg 3,000 wage (below caps).**

```oa-check
name: monthly AOV/AWW and AVBZ split
inputs:
  wage: 3000
  emp_aovaww: 0.075
  ee_aovaww: 0.065
  emp_avbz: 0.005
  ee_avbz: 0.015
steps:
  - employer_total: wage * emp_aovaww + wage * emp_avbz
  - employee_total: wage * ee_aovaww + wage * ee_avbz
  - combined: employer_total + employee_total
expected:
  employer_total: 240
  employee_total: 240
  combined: 480
```

**Example 2 — annual AOV/AWW premium capped at the published maximum base.** Annual wage NAf 120,000; cap base NAf 105,382.77 (2020 figure — confirm current-year cap).

```oa-check
name: capped annual AOV/AWW premium
inputs:
  annual_wage: 120000
  cap_base: 105382.77
  total_rate: 0.14
steps:
  - base: min(annual_wage, cap_base)
  - premium: base * total_rate
expected:
  base: 105382.77
  premium: 14753.59
```

## Ask the client

- Current payroll register: does any employee exceed the annual premium base cap? (Refund/true-up exposure.)
- Are monthly returns filed and paid by the GRC mid-month dates?
- Is the wage statement (loonstaat) column 13 ground computed after the employee premium, as the tables assume?
- Any health-insurance (AVBZ) registration gaps for part-time staff?

## Sources

- [GRC 2020 tax-filing guide: AOV/AWW 7.5%/6.5%, AVBZ 0.5%/1.5%, caps NAf 105,382.77 / NAf 417,357, penalties (PDF)](https://www.tax.sx/documents/businesses) — read 2026-10-27
- [AB 2026 no. 11 Annex II wage-tax tables 2026: worked payroll example with 6.5% employee AOV/AWW, AOV art. 26 / AWW art. 29 citations (PDF)](https://www.sintmaartengov.org/Documents/Income%20Tax%20Forms/AB%202026%2C%20no.%2011%20Bijlage%20II%20TABEL%20LOONBELASTING%202026.pdf) — read 2026-10-27
- 2026 premium caps: **needs-sources** (only 2020 caps published in retrievable official documents).

<!-- openaccountants-cta-block -->

**Talk to a verified accountant.** This is a source-cited draft, not reviewed advice. [Book time with an OpenAccountants Partner](https://calendly.com/openaccountants/consultation).
