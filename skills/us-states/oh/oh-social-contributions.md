---
name: oh-social-contributions
description: >
  Use this skill whenever asked about Ohio social contributions and
  employer-side payroll taxes for tax year 2026 — Ohio has no state
  disability/paid-leave program and no state-level retirement mandate: the
  social-contribution stack is (1) unemployment insurance under ORC Ch. 4141
  ($9,000 taxable wage base, experience rates 0.30%-9.80%, new-employer
  2.70% non-construction / 5.60% construction, mutualized add-on zeroed),
  (2) mandatory state-fund workers' compensation under ORC Ch. 4123 (BWC
  premium per $100 of payroll by class code, annual payroll report due
  August 15, self-assessing employers only by exception), and (3) federal
  FICA/FUTA on top. Covers the employer contribution base, the annual
  reporting calendar, and penalties for late payroll reports.
  Trigger on "Ohio social contributions", "Ohio unemployment insurance",
  "Ohio SUI", "Ohio UI rate", "Ohio wage base", "Ohio workers compensation",
  "BWC premium", "Ohio payroll report", "Ohio mutualized account".
  Source-cited draft; ORC 4123.26 statute text read 2026-10-27; UI figures
  carried from the tier-2 oh-payroll skill (2025 schedule, read 2026-07-13).
jurisdiction: US-OH
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - oh-payroll
---

# Ohio social contributions (UI + workers' compensation) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Ohio professional.

## 1. Scope and sources

Ohio imposes **no state payroll tax for disability, paid family leave, or state retirement contributions**. The employer social-contribution stack is:

1. **Unemployment insurance (UI)** — ORC Chapter 4141, administered by the Department of Job and Family Services (ODJFS).
2. **Workers' compensation** — ORC Chapter 4123, **state fund only**: Ohio has no private workers' comp insurance option; every employer either pays BWC premiums or is an approved self-assessing employer.
3. Federal FICA / FUTA sit on top and are covered by the federal skills.

**Source status (as_of 2026-10-28):** [ORC 4123.26](https://codes.ohio.gov/ohio-revised-code/section-4123.26) (employer payroll report; August 15 filing date for policy years from 2015; PEO monthly reports; penalties by rule) fetched HTTP 200, archived, and read in full. **UI wage base and rate ranges are carried from the tier-2 `oh-payroll` skill** (2025 schedule read 2026-07-13); ODJFS UI pages did not resolve from this drafting environment on 2026-10-27 (`odjfs.ohio.gov` DNS failed, `jfs.ohio.gov` 404) — the 2026 schedule is **needs-sources**.

## 2. Who applies

- **UI:** every employer that pays $1,500+ in wages in any calendar quarter, or employs at least one employee in each of 20 different weeks (federal test adopted); also covers most nonprofit and public employers via reimbursable agreements.
- **Workers' comp:** every private employer with **one or more employees** regularly in the same business must be covered (ORC 4123.26(B)); sole proprietors and partners may elect coverage. Coverage is through the BWC state insurance fund — private policies are not permitted.
- **No PIT-linked social contribution:** Ohio municipal income taxes and school district income taxes are *income* taxes, not contributions — see `oh-payroll` and `oh-cross-border`.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| UI taxable wage base | **$9,000** per employee per year (2025; unchanged since 2013) | `oh-payroll` (ODJFS, read 2026-07-13) — **needs-sources 2026** |
| UI experience rate range | **0.30% – 9.80%** (2025; top rate includes any mutualized component) | `oh-payroll` — needs-sources 2026 |
| New-employer UI rate | **2.70%** non-construction; **5.60%** construction (OAC 4141-9-04) | `oh-payroll` |
| Mutualized account add-on | **0.0%** for 2025 (trust fund solvent; zeroed late 2024) | `oh-payroll` — needs-sources 2026 |
| UI surcharges | Reemployment Tax / interest assessments billed separately by ODJFS | needs-sources |
| Workers' comp premium | Rate per **$100 of payroll** by BWC classification code; payroll for BWC = nearly all remuneration, capped per worker per year | needs-sources (class rates not read this run) |
| BWC annual payroll report | Due **on or before August 15** each year for the policy year beginning January 1 | [ORC 4123.26(B)](https://codes.ohio.gov/ohio-revised-code/section-4123.26), read 2026-10-27 |
| Self-assessing employers | Exception status granted by the administrator; forfeiture on failure | ORC 4123.26 / 4123.27 — 4123.27 not read, needs-sources |

## 4. Deadlines

| Filing | Due |
|---|---|
| UI quarterly return + contributions (MITA / e-file) | Last day of the month following each calendar quarter (Apr 30, Jul 31, Oct 31, Jan 31) |
| UI annual reconciliation | With the Q4 return |
| BWC annual payroll report | **August 15** (ORC 4123.26(B)) |
| BWC premium installments | Monthly or quarterly per BWC billing schedule; first installment at policy inception (Jan 1 policy year) |
| UI rate notices | Mailed by ODJFS in December for the following calendar year |

Quarter dates follow the ODJFS pattern in `oh-payroll`; BWC installment cadence **needs-sources**.

## 5. Penalties and interest

- **UI:** late quarterly returns and late contributions accrue penalty plus interest; failure to report wages triggers assessment on estimated wages. Exact 2026 percentages: **needs-sources** (ORC 4141.19/4141.20 not read this run).
- **Workers' comp:** every private employer must submit the BWC annual payroll report **on or before August 15** for policy years commencing on or after July 1, 2015 — VERIFIED against archived [ORC 4123.26(B)](https://codes.ohio.gov/ohio-revised-code/section-4123.26): "For a policy year commencing on or after July 1, 2015, the employer shall submit the payroll report on or before August fifteenth of each year". PEOs/AEOs file **monthly** (4123.26(C)). Failure penalties are set by administrator rule, "including but not limited to exclusion from alternative rating plans and discount programs" (4123.26(F)) — the earlier "$1,000 first-offense forfeiture" figure is NOT in the archived statute text and is **needs-sources**. Operating without coverage exposes the employer to the full compensation liability plus a BWC order.
- Intentional misclassification of workers as independent contractors carries separate penalties (ORC 4123.01(C)(2) — needs-sources).

## 6. Cross-border

- UI wages are taxable to Ohio for **all employees working in Ohio**, including nonresident commuters; remote workers for Ohio employers are generally assigned to the office they report to under multistate UI coordination rules.
- BWC payroll includes wages paid to nonresident employees **for work performed in Ohio**.
- Ohio has no total-disability or paid-leave program to coordinate with other states' programs (unlike NJ/NY/CA/MA/CO/WA/MD/CT/DE/OR/MA stacks).

## 7. Worked examples

**Example A — three employees, standard experience rate.**

```oa-check
name: Ohio UI contributions, 3 employees at 2.1%
inputs:
  base: 9000
  employees: 3
  rate: 0.021
steps:
  - taxable: base * employees
  - ui: taxable * rate
expected:
  taxable: 27000
  ui: 567.00
```

**Example B — BWC premium at a class rate of $1.85 per $100.**

```oa-check
name: BWC premium on 1,250,000 covered payroll
inputs:
  payroll: 1250000
  rate_per_100: 1.85
steps:
  - hundreds: payroll / 100
  - premium: hundreds * rate_per_100
expected:
  hundreds: 12500
  premium: 23125.00
```

The $1.85 class rate is illustrative — pull the client's actual BWC class rate from their premium worksheet (needs-sources).

## 8. Ask the client

- Are all employees reported to ODJFS each quarter, including the first $9,000 of each worker's wages?
- Experience rate letter for 2026 — has the client appealed an adverse rate?
- Is the client a **self-assessing** BWC employer, and is the certificate current?
- Worker classification: any 1099 contractors in Ohio? Misclassification reaches both UI and BWC.
- BWC payroll report filed by August 15? Forfeiture is automatic.
- Any reimbursable-agreement status (nonprofits/government) instead of contributory coverage?

## 9. Sources

- [ORC 4123.26 — annual statement by employer, forfeiture](https://codes.ohio.gov/ohio-revised-code/section-4123.26) — read 2026-10-27 (text effective 2021-03-24, SB 201)
- [ORC 4141.04 — free employment services (UI administration)](https://codes.ohio.gov/ohio-revised-code/section-4141.04) — read 2026-10-27
- `oh-payroll` (tier 2, read 2026-07-13) — UI wage base $9,000, rates 0.30–9.80%, new-employer 2.70%/5.60%, mutualized 0.0%
- **needs-sources:** 2026 ODJFS UI wage base/rate schedule (odjfs.ohio.gov DNS failed 2026-10-27; archived ORC 4141.04 is only the employment-offices section, no rate numbers); BWC 2026 class rates and per-worker payroll cap; ORC 4141.19/4141.20 UI penalty and interest percentages; BWC payroll-report forfeiture amounts (4123.26 sets penalties by rule, not statute); ORC 4123.01(C)(2) misclassification penalty

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Ohio UI and workers'-comp questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
