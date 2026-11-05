---
name: oh-social-contributions
description: >
  Use this skill whenever asked about Ohio social contributions and
  employer-side payroll taxes for tax year 2026 -- Ohio has no state
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

## Who this applies to

Ohio imposes **no state payroll tax for disability, paid family leave, or state retirement contributions**. The employer social-contribution stack is:

1. **Unemployment insurance (UI)** -- ORC Chapter 4141, administered by the Department of Job and Family Services (ODJFS).
2. **Workers' compensation** -- ORC Chapter 4123, **state fund only**: Ohio has no private workers' comp insurance option; every employer either pays BWC premiums or is an approved self-assessing employer.
3. Federal FICA / FUTA sit on top and are covered by the federal skills.

**Source status (as_of 2026-10-28):** [ORC 4123.26](https://codes.ohio.gov/ohio-revised-code/section-4123.26) (employer payroll report; August 15 filing date for policy years from 2015; PEO monthly reports; penalties by rule) fetched HTTP 200, archived, and read in full. **UI wage base and rate ranges are carried from the tier-2 `oh-payroll` skill** (2025 schedule read 2026-07-13); the 2026 ODJFS rate schedule is archived (US-OH-dr-odjfs-2026-rates.txt: "Taxable Wage Base $9,000"; rate classes 1-40 with experience rates 0.3%-10.1% and mutual rate 0.0%).

## 2. Who applies

- **UI:** coverage thresholds (see Not yet confirmed: in Sources); also covers most nonprofit and public employers via reimbursable agreements.
- **Workers' comp:** every private employer with **one or more employees** regularly in the same business must be covered (ORC 4123.26(B)); sole proprietors and partners may elect coverage. Coverage is through the BWC state insurance fund -- private policies are not permitted.
- **No PIT-linked social contribution:** Ohio municipal income taxes and school district income taxes are *income* taxes, not contributions -- see `oh-payroll` and `oh-cross-border`.

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| UI taxable wage base | **$9,000** per employee per year (2025 and 2026) | US-OH-dr-odjfs-2025-rates.txt ("Taxable Wage Base $9,000"); US-OH-dr-odjfs-2026-rates.txt ("Base $9,000") |
| UI experience rate range | **0.30% – 10.10%** experience/MSL rate (rate classes 1-40, 2025 and 2026; surcharges and fees add on top) | US-OH-dr-odjfs-2025-rates.txt and US-OH-dr-odjfs-2026-rates.txt (rate-class tables) |
| New-employer UI rate | **2.70%** non-construction; **5.60%** construction (2025; 5.70% construction in the 2026 schedule) | US-OH-dr-odjfs-2025-rates.txt ("NB Rate 2.7%"; "NB Construction Rate 5.6%"); US-OH-dr-nfib-uc-handbook-2025.txt ("New Employer Rate (except Construction Industry): 2.7%"; "Construction Industry Rate: 5.6%") |
| Mutualized account add-on | **0.0%** for 2025 and 2026 | US-OH-dr-odjfs-2025-rates.txt and US-OH-dr-odjfs-2026-rates.txt (Mutual Rate column 0.0% for all rate classes) |
| UI surcharges | 2025: surcharge 0.1% of taxable wages; 2026: Technology & Customer Service Fee 0.15% | US-OH-dr-odjfs-2025-rates.txt and US-OH-dr-odjfs-2026-rates.txt (surcharge/fee columns) |
| Workers' comp premium | Rate per **$100 of payroll** by BWC classification code; payroll for BWC = nearly all remuneration, capped per worker per year | (see Not yet confirmed: in Sources) |
| BWC annual payroll report | Due **on or before August 15** each year for the policy year beginning January 1 | [ORC 4123.26(B)](https://codes.ohio.gov/ohio-revised-code/section-4123.26), read 2026-10-27 |
| Self-assessing employers | Exception status granted by the administrator; forfeiture on failure | (see Not yet confirmed: in Sources; archived ORC 4123.27 covers use and access to payroll-report information, not self-assessing status) |

## The taxable base

## Deadlines and filing

| Filing | Due |
|---|---|
| UI quarterly return + contributions (MITA / e-file) | Last day of the month following each calendar quarter (Apr 30, Jul 31, Oct 31, Jan 31) (US-OH-dr-orc-4141-20.txt: "the quarterly report shall be filed not later than the last day of the first month following the close of the calendar quarter") |
| UI annual reconciliation | With the Q4 return |
| BWC annual payroll report | **August 15** (ORC 4123.26(B)) |
| BWC premium installments | (see Not yet confirmed: in Sources) |
| UI rate notices | Mailed by ODJFS in December for the following calendar year |

Quarter dates follow ORC 4141.20 (US-OH-dr-orc-4141-20.txt); BWC installment cadence (see Not yet confirmed: in Sources).
## Penalties and interest
- **UI:** late quarterly returns accrue a statutory forfeiture -- US-OH-dr-orc-4141-20.txt: the director "shall assess a forfeiture amounting to twenty-five one-hundredths of one per cent of the total remuneration reported by the employer, provided such forfeiture shall not be less than fifty nor more than one thousand dollars"; failure to report wages triggers assessment on estimated wages. Late-contribution interest percentages (see Not yet confirmed: in Sources).
- **Workers' comp:** every private employer must submit the BWC annual payroll report **on or before August 15** for policy years commencing on or after July 1, 2015 -- VERIFIED against archived [ORC 4123.26(B)](https://codes.ohio.gov/ohio-revised-code/section-4123.26): "For a policy year commencing on or after July 1, 2015, the employer shall submit the payroll report on or before August fifteenth of each year". PEOs/AEOs file **monthly** (4123.26(C)). Failure penalties are set by administrator rule, "including but not limited to exclusion from alternative rating plans and discount programs" (4123.26(F)) -- the earlier "$1,000 first-offense forfeiture" figure is NOT in the archived statute text (see Not yet confirmed: in Sources). Operating without coverage exposes the employer to the full compensation liability plus a BWC order.
- Intentional misclassification of workers as independent contractors carries separate penalties (see Not yet confirmed: in Sources).

## Cross-border points

- UI wages are taxable to Ohio for **all employees working in Ohio**, including nonresident commuters; remote workers for Ohio employers are generally assigned to the office they report to under multistate UI coordination rules.
- BWC payroll includes wages paid to nonresident employees **for work performed in Ohio**.
- Ohio has no total-disability or paid-leave program to coordinate with other states' programs (unlike NJ/NY/CA/MA/CO/WA/MD/CT/DE/OR/MA stacks).

## Worked examples

**Example A -- three employees, standard experience rate.**

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

**Example B -- BWC premium at a class rate of $1.85 per $100.**

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

The $1.85 class rate is hypothetical (see Not yet confirmed: in Sources) -- pull the client's actual BWC class rate from their premium worksheet.
## Ask the client first

- Are all employees reported to ODJFS each quarter, including the first $9,000 of each worker's wages (US-OH-dr-odjfs-2026-rates.txt: "Base $9,000")?
- Experience rate letter for 2026 -- has the client appealed an adverse rate (2026 rate schedule archived: US-OH-dr-odjfs-2026-rates.txt)?
- Is the client a **self-assessing** BWC employer, and is the certificate current?
- Worker classification: any 1099 contractors in Ohio? Misclassification reaches both UI and BWC.
- BWC payroll report filed by August 15 (ORC 4123.26(B), archived US-OH-section-4123.26.html)? Forfeiture is automatic.
- Any reimbursable-agreement status (nonprofits/government) instead of contributory coverage?

## Sources
Not yet confirmed: figures in this skill lack archived line-citations.

| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed: paragraph above) | -- | 2026-10-28 |

- [ORC 4123.26 -- annual statement by employer, forfeiture](https://codes.ohio.gov/ohio-revised-code/section-4123.26) -- read 2026-10-27 (text effective 2021-03-24, SB 201)
- [ORC 4141.04 -- free employment services (UI administration)](https://codes.ohio.gov/ohio-revised-code/section-4141.04) -- read 2026-10-27
- `oh-payroll` (tier 2, read 2026-07-13) -- UI wage base $9,000, rates 0.30–9.80%, new-employer 2.70%/5.60%, mutualized 0.0%
- **Not yet confirmed:** BWC 2026 class rates and per-worker payroll cap; BWC premium installment cadence and first-installment timing; BWC payroll-report forfeiture amounts (4123.26 sets penalties by rule, not statute); ORC 4123.01(C)(2) misclassification penalty; UI late-contribution interest percentages; UI coverage thresholds ($1,500 in wages in any calendar quarter or one employee in each of 20 different weeks); self-assessing-employer exception status and forfeiture (archived ORC 4123.27 covers payroll-report information access, not self-assessing status); the $1.85 BWC class rate in the worked example is hypothetical. Note: ORC 4141.19 does not exist (archived fetch returns "Number Not Found"); the UI late-filing forfeiture is in ORC 4141.20.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Ohio UI and workers'-comp questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult
## Talk to a verified accountant

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| (see Not yet confirmed: paragraph above) | -- | 2026-10-28 |


- [ORC 4123.26 -- annual statement by employer, forfeiture](https://codes.ohio.gov/ohio-revised-code/section-4123.26) -- read 2026-10-27 (text effective 2021-03-24, SB 201)
- [ORC 4141.04 -- free employment services (UI administration)](https://codes.ohio.gov/ohio-revised-code/section-4141.04) -- read 2026-10-27
- `oh-payroll` (tier 2, read 2026-07-13) -- UI wage base $9,000, rates 0.30–9.80%, new-employer 2.70%/5.60%, mutualized 0.0%
- **Not yet confirmed:** BWC 2026 class rates and per-worker payroll cap; BWC premium installment cadence and first-installment timing; BWC payroll-report forfeiture amounts (4123.26 sets penalties by rule, not statute); ORC 4123.01(C)(2) misclassification penalty; UI late-contribution interest percentages; UI coverage thresholds ($1,500 in wages in any calendar quarter or one employee in each of 20 different weeks); self-assessing-employer exception status and forfeiture (archived ORC 4123.27 covers payroll-report information access, not self-assessing status); the $1.85 BWC class rate in the worked example is hypothetical. Note: ORC 4141.19 does not exist (archived fetch returns "Number Not Found"); the UI late-filing forfeiture is in ORC 4141.20.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for Ohio UI and workers'-comp questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

## Talk to a verified accountant

