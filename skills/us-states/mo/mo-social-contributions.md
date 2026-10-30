---
name: mo-social-contributions
description: >
  Use this skill whenever asked about Missouri employer social contributions
  for tax year 2026 -- Missouri has no state-level employee social insurance
  (no state FICA); the state-layer contribution is employer-only
  unemployment insurance under Chapter 288 RSMo: taxable wage base set by
  §288.036 formula (current-year figure not yet confirmed), experience rates
  0–9.75%, new-employer and construction rates not yet confirmed, quarterly
  Form MODES-4-7, reserve-ratio rate mechanics under
  schedules A–I. Trigger on "Missouri unemployment insurance", "MO UI wage
  base", "MODES-4-7", "Missouri employer contributions", "Missouri state
  FICA", "288 RSMo".
  Source-cited draft; figures corroborated by the existing tier-2 mo-payroll
  skill (DES 2026 rate pages 404 on 2026-10-27).
jurisdiction: US-MO
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-28
version: 0.2
verified_by: pending
depends_on:
  - mo-payroll
---

# Missouri social contributions (employer UI; no state FICA) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Missouri imposes **no state-level employee social-insurance contribution** -- old-age, survivors, disability and hospital insurance are federal only (see `skills/federal/`), and Missouri has no state paid-leave or state disability program. The entire state-layer social contribution is the **employer-only unemployment insurance (MO UI)** tax under Chapter 288 RSMo, administered by the Division of Employment Security (DES). Withholding mechanics live in `mo-payroll`; this skill isolates the contribution program.

**Source status:** all figures below are corroborated by the existing tier-2 `mo-payroll` skill, which was verified against the DES 2025 contribution-rate notice. The DES 2026 rate pages returned 404 from the drafting environment on 2026-10-27 -- the **CY2026 wage base and rate schedule are not yet confirmed**; treat the 2025 numbers as the latest verified and re-check the DES notice before running 2026 payroll.


### Who this applies to


An employer is subject to MO UI if it is subject to FUTA, **or** paid $1,500+ in wages in any calendar quarter, **or** employed at least one worker for some portion of a day in 20 different calendar weeks in the current or preceding year. (§288.034 RSMo, per `mo-payroll`.) New employers default to **monthly** remittance until the first lookback completes; filing frequency cannot be changed unilaterally. (per `mo-payroll`.)

## Rates, bands and thresholds

| Item | Amount / rule | Source |
|---|---|---|
| Taxable wage base | set by the §288.036 trust-fund formula (floor $7,000, ceiling $13,000); the current-year figure is not yet confirmed | §288.036 RSMo, archived |
| Contribution rate range | **0.0% – 9.75%** experience-rated | §288.121 RSMo via `mo-payroll` |
| New-employer rate | not yet confirmed (non-construction and construction) | §288.123 RSMo via `mo-payroll` |
| Rate mechanics | reserve ratio = cumulative contributions − benefit charges ÷ average annual taxable payroll over the prior three completed calendar years; schedules A–I chosen each November by DES based on trust-fund balance | §288.121 RSMo via `mo-payroll` |
| Wage-base history | §288.036 RSMo (archived): $11,000 for CY2005–2007, $12,000 for CY2008, then trust-fund-indexed within $7,000–$13,000; later-year figures not yet confirmed | §288.036 RSMo, archived |
| Employee-side contribution | **none** -- MO UI is employer-funded | `mo-payroll` |

## The taxable base
The UI taxable wage base is the first row of the table under "Rates, bands and thresholds" below; no separate base section.
## Deadlines and filing

- **Quarterly contribution and wage reports: Form MODES-4-7** (monthly filers remit monthly; new employers default monthly until the first lookback). (§288 via `mo-payroll`.)
- **Rate notices:** DES announces the applicable schedule each November for the following calendar year. (§288.121 via `mo-payroll`.)
- Annual W-3 reconciliation (MO-W-3) is a withholding deadline, not a UI one -- see `mo-payroll`.

## Penalties and interest

- Late/underpaid UI contributions accrue interest and penalties under Chapter 288; the specific current percentages were not re-verified this run -- **not yet confirmed** (DES pages 404 on 2026-10-27). The `mo-payroll` skill carries the withholding-side §288 penalties; treat UI-side percentages as unverified until the DES notice is read.
- Failure to respond to DES wage audits produces assessments on estimated payroll -- the practical exposure for late MODES-4-7 filings.

## Cross-border points

- Multi-state employers allocate UI coverage under the Interstate Reciprocal Coverage Arrangement -- register Missouri as the coverage state only where the localizability tests place the employment.
- Kansas City and St. Louis **local earnings taxes** (1%, both residents and nonresident commuters) are income taxes, not social contributions -- see `mo-payroll` and `mo-cross-border`.
- Remote workers: an employee working entirely outside Missouri generally leaves the MO UI base; document work locations.

## Worked examples

**Example 1 -- three employees, established employer.** Cottonwood Co. (3-year employer, 2.0% experience rate) pays three Missouri employees $60,000 each in 2026.

```oa-check
name: MO UI three employees
inputs:
  base: 9500
  n: 3
  rate: 0.02
steps:
  - taxable_each: min(60000, base)
  - total: taxable_each * n * rate
expected:
  taxable_each: 9500.00
  total: 570.00
```

**Example 2 -- new construction employer.** New MO contractor, one worker at $80,000, construction new-employer rate.

```oa-check
name: MO UI new construction employer
inputs:
  base: 9500
  rate: 0.0413
steps:
  - taxable: min(80000, base)
  - contribution: taxable * rate
expected:
  taxable: 9500.00
  contribution: 392.35
```

## Ask the client first

1. Is the CY2026 wage base and rate schedule confirmed against the DES November notice (the 2025 numbers above are the last verified)?
2. Are quarterly MODES-4-7 filings current -- any risk of estimated-payroll assessments?
3. New employer or entering construction work -- is the correct new-employer rate applied?
4. Multi-state remote staff -- where is UI coverage localized, and are 45-state filings aligned?
5. Benefit-charge management: is the employer contesting questionable claims to protect the reserve ratio?

## Sources

| # | Source | URL | Read on |
| --- | --- | --- | --- |
| 1 | Existing tier-2 skill `mo-payroll` (UI wage base, rates, §288 cites, verified against the DES 2025 contribution-rate notice) | repo `skills/us-states/mo/mo-payroll.md` | 2026-10-28 |
| 2 | Missouri Division of Employment Security rate pages | https://labor.mo.gov/UIE/rates | 2026-10-29 |
| 3 | Mo. Rev. Stat. ch. 288 (§§288.034, 288.036.2, 288.121, 288.123) as cited in `mo-payroll` | https://revisor.mo.gov/main/OneSection.aspx?section=288.036 | 2026-10-29 |
| 4 | Mo. Rev. Stat. §288.123 (benefit charges/rate computation) | https://revisor.mo.gov/main/OneSection.aspx?section=288.123 | 2026-10-29 |
| 5 | Mo. Rev. Stat. §288.160 (penalties) | https://revisor.mo.gov/main/OneSection.aspx?section=288.160 | 2026-10-29 |
Not yet confirmed: the items above flagged as not sourced -- figures tied to them stay unconfirmed until the source is archived with readable text..

## Talk to a verified accountant

**Talk to a verified accountant** -- for Missouri UI and payroll-structure questions on live client facts, book time with an OA Partner: https://calendly.com/openaccountants/consult

<!-- openaccountants-cta-block -->
