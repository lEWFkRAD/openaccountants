---
name: al-unemployment-contributions
description: >
  Use this skill whenever asked about Alabama employer social
  contributions for tax year 2026 -- unemployment insurance
  contributions administered by the Alabama Department of Labor
  (adol.alabama.gov), the employer-only nature of the UI tax, and the
  absence of state disability or paid-leave payroll taxes. Trigger on
  "Alabama UI rate", "Alabama SUTA", "Alabama unemployment wage base",
  "Alabama employer taxes".
jurisdiction: US-AL
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.3
verified_by: pending
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - al-income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Alabama social contributions (UI)

> **Source-cited draft.** Built from the Alabama Department of Labor Unemployment Compensation Division page, read 2026-10-28. The UI taxable wage base, experience-rate range and new-employer rate were not extractable from archived primary sources this run -- every figure is on the Not yet confirmed line. No accountant has reviewed it.

## Who this applies to

- Employers covered under Alabama's unemployment-compensation law (Ala. Code Title 25), administered by the Alabama Department of Labor (ADOL): "The Unemployment Compensation (UC) division is built around one central idea: a worker who loses his job, through no fault of his own, deserves financial help" (ADOL UC Division page). The statutory coverage tests are not yet confirmed.
- The UI contribution is employer-only -- Alabama employees pay no state UI tax (not yet confirmed against statute -- see Not yet confirmed).
- Workers' compensation insurance is mandatory for employers with the statutory number of employees (threshold not yet confirmed); it is an insurance mandate, not a tax.
- Alabama has no state disability insurance, no paid family/medical leave contribution, and no state-mandated retirement contribution for private employers (a negative not provable from the archived pages -- see Not yet confirmed).

## Rates, bands and thresholds

| Item | 2026 amount | Source |
|---|---|---|
| UI taxable wage base | Not yet confirmed | see Not yet confirmed |
| Experience rate range | Not yet confirmed | see Not yet confirmed |
| New-employer assigned rate | Not yet confirmed | see Not yet confirmed |
| Solvency/add-on surtaxes | Not yet confirmed | see Not yet confirmed |
| FUTA credit reduction | Not yet confirmed | see Not yet confirmed |

No 2026 UI figures should be used from this guide until ADOL's current rate notice is archived and tied out.

## The taxable base

- The UI wage base is per-employee per-year, not gross payroll (the amount is not yet confirmed).
- Multi-state employers register in Alabama when they have Alabama employees; the wage base applies per employee per state.
- Leasing companies / PEOs file under ADOL's leasing-company rules (not yet confirmed).

## Deadlines and filing

- Quarterly contribution returns (previously carried as Form A-4, due the last day of the month following each quarter) and the annual reconciliation (previously carried as Form A-5, due January 31): both dates are not yet confirmed -- see Not yet confirmed.
- 2026 rate notices are issued to employers through the ADOL employer portal (date not yet confirmed).
- ADOL publishes quarterly wage reporting upload-file specifications and a due-date calendar on its UC pages (see Sources).

## Penalties and interest

- Late contribution returns and payments draw penalties and interest under Title 25 (percentages not yet confirmed).
- Common failure modes: (1) reporting wages above the wage base; (2) missing a solvency surtax line in years it applies; (3) new employers assuming the assigned rate is negotiable -- it is assigned, with appeal rights (appeal mechanics not yet confirmed).

## Cross-border points

- Multi-state employers: register in Alabama when they have Alabama employees or localizable work; the wage base applies per employee per state.
- No Alabama counterpart to EU-style social-security totalization; interstate only.

## Worked examples

No worked example is carried in this skill: the UI rate and wage base are not confirmed against an archived primary source, and worked examples may only use rates from the skill's own confirmed table. The prior draft's example (10 employees × $30,000 at 2.7% on an $8,000 base) used unconfirmed figures and has been removed; the figures are on the Not yet confirmed line.

## Ask the client first

- Has the 2026 ADOL rate notice been received and the experience rate verified against the reserve account?
- Are wages reported capped at the wage base per employee, with multi-state employees allocated correctly?
- Is any solvency surtax included in accruals?
- Construction/trades: is workers' compensation coverage current and classified correctly?

## Sources

| Source | URL | Read on |
|---|---|---|
| ADOL Unemployment Compensation Division page (UC division, employer services, quarterly wage reporting upload-file specifications, UC partials) | https://adol.alabama.gov/divisions/unemployment-compensation/ | 2026-10-28 |

Not yet confirmed: the UI taxable wage base (previously carried as $8,000 -- pull ADOL's current rate notice); the 2026 experience-rate range; the new-employer assigned rate (previously carried as 2.7%); solvency/add-on surtaxes; the FUTA credit-reduction status; the employer-only nature of the contribution (confirm against Title 25); the coverage tests; the workers'-compensation employee threshold; the quarterly return form ID (previously carried as Form A-4) and its due dates (previously carried as the last day of the month following each quarter); the annual reconciliation form (previously carried as Form A-5, due January 31); the 2026 rate-notice issue date; the leasing-company/PEO filing rules; the Title 25 penalty percentages; Ala. Code Title 25 text (the legislative mirror was not retrievable this run).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at openaccountants.com.

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
