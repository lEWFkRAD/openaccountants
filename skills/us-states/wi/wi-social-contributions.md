---
name: wi-social-contributions
description: >
  Use this skill whenever asked about Wisconsin social contributions for tax
  year 2026 — unemployment insurance under Wis. Stat. ch. 108 (coverage
  thresholds, $14,000 per-employee wage base, experience-rated schedules,
  new-employer rates 3.05% non-construction / 2.90% construction, quarterly
  UCT-101 filings due Apr 30 / Jul 31 / Oct 31 / Jan 31, $50 minimum late
  penalty and 0.75%/month compounded interest), the strict nine-factor UI
  worker-classification test with up to $25,000 misclassification penalty,
  and workers' compensation under ch. 102. Wisconsin has no state disability
  or paid-family-leave program. Trigger on "Wisconsin unemployment", "WI UI
  rates", "UCT-101", "Wisconsin wage base", "Wisconsin new employer UI rate",
  "Wisconsin worker classification", "Wisconsin workers compensation".
  Source-cited draft; mechanics carried from tier-2 wi-payroll (Wis. Stat.
  §§ 108.02, 108.18, 108.22, 108.221, 102.07 read 2026-07-13); ch. 108
  statute text re-read 2026-10-27.
jurisdiction: US-WI
category: state-tax
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - wi-payroll
---

# Wisconsin social contributions (UI, workers' comp) v0.1

> **General reference only.** General tax/accounting reference for AI-assisted workflows. Not reviewed for any specific person's facts, documents, elections, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified Wisconsin professional.

## Who this applies to

Employer-side social contributions in Wisconsin: **unemployment insurance (UI)** under Wis. Stat. ch. 108 (DWD), and **workers' compensation** under ch. 102. Wisconsin has **no state disability insurance and no paid family leave program**. Payroll withholding mechanics sit in `wi-payroll`.

**Source status (as_of 2026-10-27):** figures carried from tier-2 `wi-payroll` (statutory cites verified 2026-07-13) and [Wis. Stat. § 108.05 text](https://docs.legis.wisconsin.gov/statutes/statutes/108/05) re-read 2026-10-27. 2026 rate schedules depend on the trust-fund balance band — the 2025 Schedule D is reproduced; **the 2026 band/schedule is not yet confirmed** until DWD publishes rate notices.

### 2. Who applies

- **UI-covered employers** (Wis. Stat. § 108.02(13)) — any one trigger: $1,500+ wages in any calendar quarter (current or prior year); one or more workers for any part of a day in 20+ weeks in a year; acquiring a covered employer; 501(c)(3) with $1,500+ quarterly wages; agricultural employer with $20,000+ quarterly wages or 10+ workers 20+ weeks; domestic-service employer with $1,000+ in a quarter.
- **Reimbursing employers** (governments, certain nonprofits) pay benefits directly plus a fee rather than contributions.
- **Workers' comp:** nearly all employers must carry coverage (ch. 102); uninsured employers face direct benefit liability.
- **Worker classification:** the UI nine-factor test (§ 108.02(12)(bm)) and the separate WC nine-factor test (§ 102.07(8)) must **both** be run — a worker can be an employee under one and a contractor under the other.

## 3. Rates and base

| Item | Amount / rule | Source |
|---|---|---|
| UI taxable wage base | **$14,000 per employee per calendar year** (unchanged since 2013; statutory, not indexed) | Wis. Stat. § 108.18(1)(am) via `wi-payroll` (2026-07-13) |
| Experience rates (2025 Schedule D) | 0.00%–12.00% by reserve ratio; small (≤$500K payroll) vs large (> $500K) columns: e.g. 16%+ reserve → 0.00%/0.05%; deficit below −8% → 12.00% both | `wi-payroll` (2026-07-13); **2026 schedule not yet confirmed** |
| New employer rate | **3.05%** non-construction; **2.90%** construction (first 3 calendar years) | Wis. Stat. § 108.18(2)(c) via `wi-payroll` |
| Solvency tax | 0.00% for 2025 (trust fund above trigger) | `wi-payroll`; 2026 not yet confirmed |
| Employee UI contribution | **None** — Wisconsin UI is employer-funded (unlike PA) | ch. 108 structure |
| FUTA | 6.0% on $7,000; credit state status not yet confirmed | not yet confirmed |
| Workers' comp | Manual rates by class, private carriers; state fund closed to most new business since 1996 | not yet confirmed for rate detail |

**AUDIT FLASH POINT** — **misclassification**: the UI test requires Part A (no control) **plus six of nine** Part B factors; failing one required factor flips the worker to employee status. Fraudulent misclassification carries up to **$25,000 per worker** (2009 Wis. Act 292, § 108.221). A 1099 worker for IRS can still be a UI employee. (not yet confirmed)

### 4. Deadlines

| Filing | Due |
|---|---|
| UCT-101 quarterly contribution & wage report (detail UCT-7823) | **Apr 30 / Jul 31 / Oct 31 / Jan 31** |
| Electronic filing | Mandatory for 25+ workers or anyone e-filing Form 940 (Wis. Admin. Code DWD 110.04) | (not yet confirmed)
| Rate appeal | 15 days from notice (DWD) |
| New employer registration | At first covered quarter trigger — register with DWD |
| WC first report of injury | Employer report within 7 days of accident knowledge if >3-day disability or medical beyond first aid — not yet confirmed re-verify |

### 5. Penalties and interest

- Late UCT-101: **$50 minimum per quarter** (§ 108.22(1)(a)).
- Late payment: **0.75% per month, compounded**. (not yet confirmed)
- Fraudulent misclassification: **up to $25,000 per misclassified worker** (§ 108.221). (not yet confirmed)
- Uninsured WC employer: direct liability for benefits plus DIF assessments.

### 6. Cross-border

- UI state follows the **four-part DOL localization test (26 U.S.C. § 3306(j))** — localizing services to the worksite — **not** income-tax reciprocity. An IL-resident driver localized in a WI office: no WI PIT withholding under reciprocity, but **WI UI still owed**. This split is the most common border-employer error (`wi-payroll` §6.3).
- Workers' comp coverage follows the employment contract/situs rules — carry WI coverage for WI work even for out-of-state residents.
- Remote workers: if localized outside Wisconsin, UI follows the other state.

### 7. Worked examples

**Example A — UI contribution for a new non-construction employer, 6 employees.**

```oa-check
name: New employer UI on six employees at 14,000 base
inputs:
  employees: 6
  wage_base: 14000
  new_employer_rate: 0.0305
steps:
  - taxable_wages: employees * wage_base
  - ui_tax: taxable_wages * new_employer_rate
expected:
  taxable_wages: 84000
  ui_tax: 2562.00
```

**Example B — late-payment interest, one quarter.**

```oa-check
name: Compounded monthly interest on 4,000 UI shortfall, 3 months
inputs:
  shortfall: 4000
  monthly: 0.0075
  months: 3
steps:
  - balance: shortfall * (1 + monthly) * (1 + monthly) * (1 + monthly)
  - interest: balance - shortfall
expected:
  balance: 4090.68
  interest: 90.68
```

### 8. Ask the client

- Which quarter triggers coverage ($1,500 test) — startups get caught retroactively. (not yet confirmed)
- Reserve-ratio report reviewed before the rate notice? Experience appeals are 15 days.
- Every 1099 worker run through **both** nine-factor tests (UI and WC)?
- Border commuters: UI localization vs PIT reciprocity split documented?
- WC policy class codes match actual operations (construction carve-outs)?

### 9. Sources

- [Wis. Stat. ch. 108](https://docs.legis.wisconsin.gov/statutes/statutes/108) — § 108.05 text read 2026-10-27; §§ 108.02(12)(bm), 108.02(13), 108.18, 108.22, 108.221 cited via `wi-payroll` (verified 2026-07-13)
- `wi-payroll` (tier 2, read 2026-07-13) — wage base, Schedule D, new-employer rates, UCT-101 calendar, penalties, classification tests
- [DWD UI tax](https://dwd.wisconsin.gov/uitax) — portal referenced by `wi-payroll`
- **not yet confirmed:** 2026 rate schedule band; 2026 solvency tax; FUTA credit-reduction status; WC reporting-day figures and rate detail.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** — for Wisconsin UI, classification and workers' comp questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
| (see Not yet confirmed) | — | 2026-10-28 |

Not yet confirmed against archived sources.

## Talk to a verified accountant

Not yet confirmed against archived sources.
