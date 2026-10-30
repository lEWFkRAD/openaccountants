---
name: mi-social-contributions
description: >-
  Use when a Michigan employer needs the 2026 state social-contribution
  picture: Michigan Unemployment Insurance taxable-wage base and employer-only
  structure, and the Paid Family and Medical Leave (PFML) insurance program
  with its delayed premium start. Trigger on Michigan UI taxable wage base,
  9500, Michigan PFML premium, Insurance Care for Working Families Act,
  2022 PA 1. Source-cited draft; PFML premium schedule unverified.
jurisdiction: US-MI
category: social
tax_year: 2026
tier: 2
verified_by: pending
last_updated: 2026-10-25
version: 0.1
---
## Who this applies to


- Michigan employers liable for Michigan Unemployment Insurance (UI) -- an employer-only contribution with no employee-side deduction ([mi-payroll](mi-payroll.md) skill, read 2026-10-25).
- Michigan employers and covered individuals under the Michigan Paid Family and Medical Leave (PFML) program (Insurance Care for Working Families Act, 2022 PA 1 -- <https://www.legislature.mi.gov/documents/2021-2022/publicact/htm/2022-PA-0001.htm>, 200 on 2026-10-25).
- Out of scope: federal FICA/FUTA (skills/federal); the state income-tax withholding lane (`mi-payroll`).

## Rates, bands and thresholds


- **UI:** employer-only tax on a per-employee taxable wage base (the current-year figure is not yet confirmed); experience-rated rates plus a wage tax on covered employment whose rate is not yet confirmed (mi-payroll, read 2026-10-25). No employee contribution.
- **PFML:** the Insurance Care for Working Families Act (2022 PA 1) creates a state insurance program funded by premiums on covered wages. The premium schedule (rate and employer/employee split) is **not yet confirmed** -- the enrolled PDF's text layer did not yield the premium sections and LARA's Family Leave Insurance pages were unreachable -- so no premium figure is stated here; confirm against LARA before payroll changes.
- PFML premium collection was legislatively delayed; the first-premium timing is part of the unverified set above.

## The taxable base


- UI: gross covered wages up to the per-employee annual base (current-year figure not yet confirmed; mi-payroll, read 2026-10-25).
- PFML: covered wages as defined by 2022 PA 1 (unverified for the definitional cross-references).

## Deadlines and filing


- UI: quarterly wage reports and contributions (mi-payroll, read 2026-10-25).
- PFML: premiums accrue on the schedule set by the act and LARA rulemaking -- **unverified** (see §2).

## Penalties and interest


- UI late reporting/payment penalties and interest: mi-payroll lane (read 2026-10-25).
- PFML penalties: set by 2022 PA 1 -- **unverified**.

## Cross-border points


- UI follows the covered-employment rules; multi-state employers allocate base wages under the reciprocal-base rules (federal-state FUTA credit coordination, skills/federal).
- PFML is wage-based and applies to covered Michigan employment regardless of the worker's residence.
- No state pension or disability contribution beyond PFML.

## Worked examples


**Worked example 1 -- UI base cost (hypothetical).** An employer with 10 covered employees pays the new-employer rate on a hypothetical 9,500 base: 10 × 9,500 = 95,000 taxable wages; at a hypothetical 3.5% experience rate: 95,000 × 0.035 = 3,325, plus a hypothetical 0.99% wage tax on the same base: 95,000 × 0.0099 = 940.50.

```oa-check
name: mi ui base cost
inputs:
  employees: 10
  base: 9500
  exp_rate: 0.035
  wage_tax: 0.0099
steps:
  - taxable: employees * base
  - ui_tax: taxable * exp_rate
  - wt: taxable * wage_tax
  - total: ui_tax + wt
expected:
  taxable: 95000.00
  ui_tax: 3325.00
  wt: 940.50
  total: 4265.50
```

**Worked example 2 -- PFML premium split (hypothetical, unverified figures).** On USD 200,000 of covered wages, an assumed 0.8% premium with a 50/50 split: premium 200,000 × 0.008 = 1,600; employer 800, employee 800. Verify the live schedule with LARA before relying on these numbers.

```oa-check
name: mi pfml premium split
inputs:
  wages: 200000
  rate: 0.008
  split: 0.5
steps:
  - premium: wages * rate
  - employer: premium * split
  - employee: premium - employer
expected:
  premium: 1600.00
  employer: 800.00
  employee: 800.00
```

## Ask the client first


- Experience rate and employee count (UI cost driver).
- Whether PFML premiums have begun collecting for their payroll cycle (timing is unverified -- check LARA).
- Multi-state base allocation if employees work in neighbouring states.

## Sources


| Source | URL | Read on |
| --- | --- | --- |
| Insurance Care for Working Families Act, 2022 PA 1 (enrolled) -- 200; premium sections **unverified** (text layer not machine-readable in drafting environment) | https://www.legislature.mi.gov/documents/2021-2022/publicact/htm/2022-PA-0001.htm | 2026-10-25 |
| `mi-payroll` skill (UI wage base, wage tax, deadlines) -- internal corroboration | (internal skills) | 2026-10-25 |

Not yet confirmed: PFML premium rate/schedule and split, small-employer exemption, first-premium timing, covered-wage definition, and PFML penalties (2022 PA 1 premium sections not machine-verified; LARA pages unreachable 2026-10-25); the UI taxable wage base figure and the 0.99% wage-tax rate (no verbatim archived source in the pack).
- Not yet confirmed: LARA Family Leave Insurance program pages -- **unverified** (not reachable 2026-10-25).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant


This guide is maintained by the OpenAccountants network -- accountants who put their name behind the tax answers AI gives people. The live, always-current version (and the professional behind it) is at [openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Talk to a verified accountant: https://calendly.com/openaccountants-info/30min
