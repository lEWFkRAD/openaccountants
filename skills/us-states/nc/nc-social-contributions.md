---
name: nc-social-contributions
description: >-
  Use when an employer or worker needs the 2026 North Carolina
  social-contribution picture: NC has no state employee social contribution —
  the only state-level payroll contribution is employer-only unemployment
  insurance (SUI) under N.C.G.S. Chapter 96, administered by the Division of
  Employment Security (DES), with a 2025 wage base of $32,600 and experience
  rates 0.06%–5.76%, plus the workforce investment surcharge mechanics.
  Trigger on North Carolina unemployment rate, DES, NCUI 104, SUI wage base,
  32600, workforce investment act surcharge, NC employer payroll taxes.
  Source-cited draft; DES 2026 rates needs-sources.
jurisdiction: US-NC
category: social
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---

# North Carolina social contributions (employer-only UI)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

Every NC employer (and every out-of-state employer with NC employees) that pays wages subject to NC unemployment insurance. Employees owe **nothing** at the state level: North Carolina levies no state employee social contribution, no state disability insurance, no state paid-family-leave premium, and no state paid-sick-leave mandate. The only state-level social contribution is the **employer** unemployment insurance (SUI) contribution under N.C.G.S. Chapter 96, administered by the Division of Employment Security (DES), a division of the NC Department of Commerce. Workers' compensation (Industrial Commission) and FICA/FUTA are separate and federal or non-tax; see the federal payroll skills and `nc-payroll`.

## 2. Core rules and rates

| Item | 2025 value | 2026 value | Source |
|---|---|---|---|
| SUI taxable wage base | $32,600 per employee | **needs-sources** (announced each November by DES) | N.C.G.S. Ch. 96; DES rate notices |
| Experience contribution rate range | 0.06% – 5.76% of taxable wages | **needs-sources** | DES NCUI 104 rate notices |
| New-employer rate | assigned by DES formula (non-taxed employers higher) | same mechanism | DES |
| Employee share | 0% — employee contributions are prohibited | 0% | N.C.G.S. Ch. 96 |
| Workforce investment surcharge | 20% of SUI contributions reallocated internally to DOE; not a separate line on the employer's return | same | DES guidance; `nc-payroll` |

- **No employee-side deduction.** NC law forbids charging employees UI contributions; payroll software that adds a "NC UI" employee line is wrong.
- **Experience rating.** Rates are set annually per employer from the reserve-ratio formula on the NCUI 104 notice; a new employer with no NC payroll history gets an assigned rate for a limited period.
- **Surcharge mechanics.** The federal Workforce Innovation and Opportunity Act surcharge is collected by reallocation inside DES — the employer pays one SUI contribution at the NCUI 104 rate.

## 3. Base

- **Base:** gross wages per employee up to the taxable wage base ($32,600 for 2025), including most remuneration for services; Chapter 96 exclusions (e.g., certain agricultural, domestic, and state/local/501(c)(3) coverage rules) apply.
- **Credit for FUTA:** NC is a credit-reduction state cycle participant — late or underpaid SUI contributions reduce the 940 credit; see federal payroll skills.

## 4. Deadlines

- Quarterly wage-and-contribution reports (NCUI 101) due the last day of the month following each calendar quarter (Apr 30, Jul 31, Oct 31, Jan 31); e-filing mandatory for employers with 10+ employees in any quarter.
- Annual contribution rate notices (NCUI 104) issued each November/December; effective Jan 1. Trust Fund Solvency Surcharge (N.C.G.S. § 96-9.7) was 0% for 2025 (trust fund above the statutory threshold).
- Registration with DES before the first NC payroll.

## 5. Penalties and interest

- Late quarterly reports: penalty up to 5% of contributions due, escalating with continued lateness (DES enforcement under Ch. 96).
- Late/underpaid contributions: interest and penalty accrue; sustained delinquency triggers **FUTA credit reduction** on federal Form 940 — often the larger dollar consequence.
- Underreported wages: reassessment plus penalty; misclassification of employees as contractors is the most common audit finding.

## 6. Cross-border and federal overlay

- Remote workers: SUI situs follows where services are performed (and multi-state coverage rules under Ch. 96 reciprocity); an employee working from NC for an out-of-state employer generally creates NC SUI exposure.
- No state social credit exists against federal FICA; nothing to coordinate beyond FUTA credit integrity.
- No NC PFL/SDI means no interaction with the federal FMLA at the premium level.

## 7. Worked examples

**Example 1 — employer SUI cost, 2025 wage base.** An NC employer with 3 employees each paid $45,000, experience rate 1.2%.

```oa-check
name: nc sui employer cost 2025
inputs:
  employees: 3
  wage_base: 32600
  rate: 0.012
steps:
  - taxable_wages: employees * wage_base
  - contribution: taxable_wages * rate
expected:
  taxable_wages: 97800
  contribution: 1173.60
```

Employee share: $0. Wages above $32,600 per employee are outside the base.

**Example 2 — FUTA credit-reduction exposure.** Same employer owes $1,173.60 SUI; if it had paid nothing, the Form 940 credit would be reduced, adding up to 0.6% × $7,000 × 3 = $126 federal tax plus state penalties.

```oa-check
name: nc futa credit reduction exposure
inputs:
  employees: 3
  futa_wage_base: 7000
  credit_reduction_rate: 0.006
steps:
  - extra_futa: employees * futa_wage_base * credit_reduction_rate
expected:
  extra_futa: 126.00
```

## 8. Ask the client first

1. Are you registered with DES, and what rate is on your current NCUI 104?
2. Any workers performing services from NC for out-of-state entities (or vice versa)?
3. Contractor classifications — do any "1099" workers meet the NC common-law employee test?
4. Wage base awareness: is payroll software capping SUI at the correct current-year base?

## 9. Sources

- N.C.G.S. Chapter 96 (Employment Security Law) — chapter index verified HTTP 200 with text, 2026-10-25: <https://www.ncleg.gov/Laws/GeneralStatuteSections/Chapter96>
- DES employers hub: <https://des.nc.gov/employers> — 200, 2026-10-25. **2026 wage base and rate range: needs-sources** (DES publishes each November; 2025 figures corroborated by the existing `nc-payroll` skill, read 2026-10-25).
- `nc-payroll` skill (SUI wage base $32,600, rates 0.06–5.76%, surcharge mechanics) — internal corroboration, read 2026-10-25.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
