---
name: va-social-contributions
description: >-
  Use when an employer or worker in Virginia needs the 2026 answer on
  state-level social contributions: Virginia has NO state employee social
  contribution -- the only state payroll levies are employer-only
  unemployment insurance (Va. Code Title 60.2; wage base $8,000, one of
  the lowest in the US; experience rates 0.10%-6.20% per the 2025
  schedule) and mandatory workers' compensation insurance (Title 65.2,
  3+ employees). The Virginia Paid Family Leave premium (program live
  1 July 2026, reported 0.5% of wages split 50/50) is UNVERIFIED this
  run -- tdi.virginia.gov failed DNS 2026-10-27. Trigger on Virginia SUI,
  VEC FC-20, Virginia unemployment wage base, Virginia paid family leave
  premium, Virginia workers compensation requirement.
  Source-cited draft; PFL figures need-sources.
jurisdiction: US-VA
category: payroll
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-27
version: 0.1
---

# Virginia social contributions (unemployment insurance, workers' comp, paid family leave)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## 1. Who this applies to

Every Virginia employer with employees covered by Va. Code Title 60.2 (unemployment insurance) -- substantially all employers -- plus employers at the workers' compensation threshold (3 or more employees, or one or more in construction). Also relevant to out-of-state employers with Virginia employees, and to anyone modelling the fully loaded Virginia payroll cost. **Employees pay no Virginia state social contribution at all**: there is no state disability, family-leave, or paid-leave employee levy that is verified as of this draft (see §7 caveats on Paid Family Leave). Federal FICA/FUTA are covered by the federal payroll skills and are not repeated here.

## 2. Rates and key figures

| Item | Figure | Source / status |
|---|---|---|
| Employee state social contribution | **None** | No state-level employee levy in Title 60.2; Title 60.2 Ch. 1 verified 2026-10-27 |
| SUI taxable wage base | $8,000 per employee per calendar year (2025; unchanged since 2009) | `va-payroll` skill; 2026 base **not yet confirmed** |
| SUI experience rate range | 0.10% – 6.20% (2025 schedule incl. 0.10% pool charge; 0.20% Fund Building where applicable) | `va-payroll` skill; 2026 schedule **not yet confirmed** |
| New-employer SUI rate | 2.50% standard (first three computation periods, Va. Code § 60.2-516); construction new employers commonly 6.20% | `va-payroll` skill [VERIFY 2026 schedule] | (not yet confirmed)
| Max SUI cost per employee | $8,000 × 6.20% = $496/yr | computed from the two rows above |
| Workers' compensation | Mandatory at 3+ employees (1+ in construction); premium is private-market, class-rated | Title 65.2 (not re-verified this run) -- carried from `va-payroll` |
| Paid Family Leave premium | Reported 0.5% of wages, 50/50 employer/employee, program live 1 July 2026 | **not yet confirmed** -- tdi.virginia.gov / paidfamilyleave.virginia.gov DNS failure 2026-10-27 |

## 3. Contribution base

- SUI base: gross wages up to the $8,000 annual taxable wage base per employee per calendar year; the base has not been raised since 2009, so SUI exposure per employee is capped at roughly $496/yr even at the maximum experience rate.
- Workers' comp base: payroll by class code per the policy -- not a tax and not administered by VEC.
- There is no state-level employee contribution base because there is no state-level employee contribution (PFL pending verification).

### 4. Deadlines and filings

- **VEC FC-20 (quarterly tax report) + FC-21 (quarterly payroll report)** filed together: Q1 due April 30, Q2 July 31, Q3 October 31, Q4 January 31 of the following year, via the VEC Business iFile portal. _(carried from `va-payroll`; VEC root verified 200 2026-10-27 -- page-level schedule re-verify.)_ (not yet confirmed)
- Annual contribution return / wage reconciliation is folded into the Q4 FC-20/FC-21 cycle for most employers.
- Workers' comp: policy renewal dates, not tax deadlines.

### 5. Penalties and interest

- Late FC-20 filing: $100 minimum, or $30 plus 10% of tax due, whichever is greater. _(carried from `va-payroll` [VERIFY].)_
- Late FC-20 payment: interest accrues monthly plus stacked penalties. _(carried [VERIFY].)_
- Failure to file FC-21: independent $25/quarter penalty and it corrupts the experience-rating computation. _(carried [VERIFY].)_ (not yet confirmed)
- Misclassification audit exposure: back contributions + interest + 25% penalty, plus civil penalties up to $5,000 per misclassified worker under the Construction Industry Misclassification Act. _(carried [VERIFY].)_

### 6. Cross-border notes

- Virginia has **reciprocity agreements with DC, Kentucky, Maryland, Pennsylvania and West Virginia**: nonresident employees from those states are exempt from Virginia PIT withholding (Form VA-4 exemption), but the employer's SUI obligations follow the usual interstate UI coverage rules (the state where the work is performed is generally the liable state unless a reciprocity certificate under the federal UI compact system shifts coverage).
- Multi-state employers: Virginia's $8,000 base is the lowest in the region -- a group with Virginia and Maryland/D.C. staff will see most UI taxable wages land outside Virginia. Model per state, not blended.

### 7. Worked examples

**Example 1 -- small Virginia employer, 3 employees, mid-tier experience rate.** Three employees, each over the full $8,000 base, experience rate 4.30% (2025-schedule figure used as illustration).

```oa-check
name: va sui 3 employees 4.30 percent
inputs:
  base: 8000
  n: 3
  rate: 0.043
steps:
  - per_emp: base * rate
  - total: n * per_emp
expected:
  per_emp: 344.00
  total: 1032.00
```

**Example 2 -- maximum SUI exposure per employee.** Even at the top 2025 rate of 6.20%, one employee's full-year SUI cost is capped by the wage base.

```oa-check
name: va sui max per employee
inputs:
  base: 8000
  rate: 0.062
steps:
  - max_cost: base * rate
expected:
  max_cost: 496.00
```

### 8. Ask the client first

1. Are you registered with VEC, and what is your current experience rate and taxable-wage history?
2. Any construction work -- does the 1-employee workers' comp rule and the higher new-employer SUI rate apply?
3. Do you employ nonresidents from DC/KY/MD/PA/WV -- are VA-4 reciprocity exemptions on file?
4. Have you checked the current-year (2026) wage base and rate schedule on vec.virginia.gov -- this draft carries 2025 figures?
5. For 2026 payroll cost modelling: has the Paid Family Leave premium actually started collecting, and at what rate -- verify before quoting.

### 9. Sources

- Code of Virginia Title 60.2 Ch. 1 (unemployment compensation, general provisions): <https://law.lis.virginia.gov/vacode/title60.2/chapter1/> -- 200 with text, 2026-10-27.
- Virginia Employment Commission: <https://vec.virginia.gov/> -- 200 with text, 2026-10-27.
- Existing `va-payroll` skill (wage base, rate schedule, FC-20/FC-21 mechanics, penalty schedule -- carried with its [VERIFY] flags): read 2026-10-27.
- Virginia Paid Family Leave premium rate/start date: **not yet confirmed** -- tdi.virginia.gov and paidfamilyleave.virginia.gov DNS failure (getaddrinfo) 2026-10-27. Re-verify before publication.
- 2026 SUI wage base and rate schedule: **not yet confirmed** (2025 figures carried).

<!-- openaccountants-cta-block -->

---

### Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at the OpenAccountants network.

- Use it in your AI: 
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min

## Who this applies to

Not yet confirmed against archived sources.

## Rates, bands and thresholds

Not yet confirmed against archived sources.

## The taxable base

Not yet confirmed against archived sources.

## Deadlines and filing

Not yet confirmed against archived sources.

## Penalties and interest

Not yet confirmed against archived sources.

## Cross-border points

Not yet confirmed against archived sources.

## Worked examples

Not yet confirmed against archived sources.

## Ask the client first

Not yet confirmed against archived sources.

## Sources

Not yet confirmed: figures in this skill lack archived line-citations.


| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed) | -- | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
