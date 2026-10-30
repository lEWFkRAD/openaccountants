---
name: nj-social-contributions
description: >
  Use this skill whenever asked about New Jersey social contributions for
  tax year 2026 -- the state's worker-plus-employer contribution stack:
  Unemployment Insurance (UI), Temporary Disability Insurance (TDI, shown as
  DI), Family Leave Insurance (FLI), and the Workforce Development /
  Supplemental Workforce Funds (WF/SWF). Covers the calendar-2026 rates
  (worker UI 0.3825%, DI 0.19%, WF/SWF 0.0425%, FLI 0.23%; employer DI
  0.19%, WF/SWF 0.0425%, FLI 0.23%, UI experience-rated), the two wage bases
  ($44,800 UI/WF/SWF and employer TDI; $171,100 worker TDI/FLI), new-employer
  UI rate 2.6825%, benefit caps, private-plan rules, and NJ-927/WR-30
  remittance. Trigger on "New Jersey UI rate", "NJ TDI", "FLI rate",
  "workforce development fund", "NJ-927", "New Jersey wage base 2026",
  "new employer UI rate".
  Source-cited draft; NJDOL rate-information page read 2026-10-27.
jurisdiction: US-NJ
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - nj-payroll
---

# New Jersey social contributions (UI, TDI, FLI, WF/SWF) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

New Jersey's social-insurance contributions, all remitted on the quarterly **Form NJ-927** with the **WR-30** wage detail: **Unemployment Insurance (UI)**, **Temporary Disability Insurance (TDI -- "DI" on NJDOL tables)**, **Family Leave Insurance (FLI)**, and the **Workforce Development Partnership / Supplemental Workforce Funds (WF/SWF)**. Worker contributions are wage-based with two different bases; employer UI is experience-rated. Out of scope: income-tax withholding tables (in `nj-payroll`), workers' compensation insurance (private market), federal FICA/FUTA.

**Source status:** the NJDOL employer rate-information page (20,924 chars) verified HTTP 200 and read **2026-10-27** -- CY2026 and CY2025 rates and bases, new-employer rates through FY June 2027, and 2027 bases are quoted from it. Figures corroborated by the existing tier-2 `nj-payroll` skill. (not yet confirmed)

### 2. Who applies

- Every NJ-covered employer: employer DI, WF/SWF, FLI and experience-rated UI contributions plus worker deductions for UI, WF/SWF, and (State Plan only) TDI and FLI.
- Workers: UI/WF/SWF up to $44,800; TDI/FLI up to $171,100 (worker share only for TDI/FLI).
- **New employers:** keep the new-employer UI rate until three consecutive full or partial years of contribution experience.
- Employers with approved **private TDI/FLI plans**: worker cost cannot exceed the State Plan cost.

## 3. Rates and base

**Calendar-year worker and employer rates** (NJDOL rate-information page, read 2026-10-27):

| Program | Worker CY2026 | Employer CY2026 | Worker CY2025 | Employer CY2025 |
|---|---|---|---|---|
| UI | 0.3825% | 0.0825% (new-employer; experience-rated otherwise) | 0.3825% | 0.0825% (new-employer) |
| TDI (DI) | 0.19% | 0.19% | 0.23% | 0.23% |
| WF/SWF | 0.0425% | 0.0425% | 0.0425% | 0.0425% |
| FLI | 0.23% | 0.23% | 0.33% | 0.33% |

**Wage bases** (same page):

| Base | CY2025 | CY2026 | CY2027 (published) |
|---|---|---|---|
| UI + WF/SWF (worker and employer) and employer TDI | $43,300 | **$44,800** | $46,400 |
| Worker TDI + FLI | $165,400 | **$171,100** | $177,100 |

- UI and WF/SWF together = 0.425% of wages up to the UI base (worker side).
- **New-employer UI rate (fiscal rate years, July–June):** 2.6825% for July 2025–June 2026 and July 2026–June 2027.
- 2026 benefit caps: max UI weekly benefit **$905**; max TDI weekly **$1,119**; alternative earnings test $15,500; base week $310.
- No state disability beyond TDI; no state paid-family-leave employer surcharge beyond the FLI split above. Federal FICA/FUTA unchanged.

### 4. Deadlines

- **NJ-927 + WR-30:** quarterly, electronic, due the last day of the month following each quarter (Q4 2026 due 31 January 2027); due even for zero-tax quarters.
- Worker deductions taken each pay period; stop each program at its own base.
- UI rate notices (NJDOL) arrive each year for the July–June rate year; protests have their own appeal window.

### 5. Penalties and interest

- Late NJ-927/WR-30 filings and late contributions accrue additions to tax and interest under NJ labor and taxation provisions; current percentages **not yet confirmed** (NJDOL penalty page not fetched this run).
- Under-deducting worker contributions: employer remains liable for the worker share.
- Misclassifying employees as independent contractors exposes the group to UI/TDI/FLI back-contributions (ABC test under NJ Wage and Hour Law -- see `nj-payroll`).

### 6. Cross-border

- Multi-state workers: UI coverage follows the four-fold test (localization of services, place of direction, residence, place of hiring) -- NJ is the covering state only when the test points there; coordinate with the other state's UI to avoid double coverage.
- Remote workers living outside NJ but performing services in NJ are in the NJ UI/TDI/FLI base; document work location.
- FLI/TDI benefits are portable to workers who later work in other states; no interstate credit for contributions.

### 7. Worked examples

**Example 1 -- worker contributions, $120,000 wage, CY2026.**

```oa-check
name: NJ worker contributions 2026
inputs:
  wage: 120000
  ui_base: 44800
  tdi_fli_base: 171100
  ui: 0.003825
  wf: 0.000425
  di: 0.0019
  fli: 0.0023
steps:
  - ui_wf: (ui + wf) * min(wage, ui_base)
  - di_fli: (di + fli) * min(wage, tdi_fli_base)
  - total: ui_wf + di_fli
expected:
  ui_wf: 190.40
  di_fli: 504.00
  total: 694.40
```

**Example 2 -- new employer, one employee at the UI base, FY Jul 2026–Jun 2027.**

```oa-check
name: NJ new employer UI
inputs:
  wage: 44800
  new_ui: 0.026825
  di: 0.0019
  wf: 0.000425
  fli: 0.0023
steps:
  - employer_ui: wage * new_ui
  - employer_other: wage * (di + wf + fli)
  - employer_total: employer_ui + employer_other
expected:
  employer_ui: 1201.76
  employer_other: 207.20
  employer_total: 1408.96
```

### 8. Ask the client

1. State Plan or approved private TDI/FLI plan -- is the worker cost capped at State Plan levels?
2. New employer? Which rate year applies, and when does experience kick in?
3. Multi-state workers -- which state's UI covers them (four-fold test documented)?
4. Are worker deductions stopping at the correct, different bases?
5. Contractor classifications -- ABC test exposure to back UI/TDI/FLI?

### 9. Sources

1. NJ Department of Labor, employer rate information (CY2026/CY2025 rates, bases, new-employer rates, benefit caps): <https://www.nj.gov/labor/ea/employer-services/rate-info/> -- 200, read 2026-10-27.
2. Existing tier-2 skill `nj-payroll` (NJ-927 mechanics, 2026 bases, withholding): repo `skills/us-states/nj/nj-payroll.md`.
3. NJ Employer Handbook (TDI/FLI private plans, taxes and wages): <https://www.nj.gov/labor/ea/help/employer_handbook/tdi-fli.shtml> -- cited in `nj-payroll`, not re-fetched this run.

<!-- openaccountants-cta-block -->
**Talk to a verified accountant** -- for New Jersey UI/TDI/FLI questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

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
