---
name: md-social-contributions
description: >
  Use this skill whenever asked about Maryland employer social contributions
  for tax year 2026 — unemployment insurance (SUI) on the first $8,500 of
  each employee's calendar-year wages, 2026 rates 0.30%–7.50% under Tax
  Table A, new-employer rates 1.0%–2.6%, 1.5% monthly interest on unpaid
  balances, and the FAMLI paid-family-leave program (contributions begin
  April 2027, quarterly wage reports from April 2027, small-employer 50%
  relief). Trigger on "Maryland unemployment insurance", "MD SUI wage base",
  "Maryland FAMLI", "Maryland paid family leave contributions",
  "MW-506 unemployment".
  Source-cited draft; Maryland Department of Labor pages read 2026-10-27.
jurisdiction: US-MD
category: payroll
tax_year: 2026
tier: 2
last_updated: 2026-10-27
version: 0.1
verified_by: pending
depends_on:
  - md-payroll
---

# Maryland social contributions (SUI + FAMLI) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to


Maryland has **no state-level employee social-insurance contribution** — there is no state version of FICA; old-age, survivors, disability and hospital insurance are federal (see `skills/federal/`). The state-layer social contributions are therefore the **employer-only** ones: unemployment insurance (SUI) under Md. Code, Labor & Employment §8-101 et seq., and the incoming **FAMLI** (Family and Medical Leave Insurance) program. Income-tax withholding mechanics live in `md-payroll`; this skill covers the contribution programs themselves.

**Source status:** the Department of Labor SUI tax-rate page verified HTTP 200 with live 2026 content on 2026-10-27; the FAMLI employer page verified HTTP 200 the same day. The FAMLI **contribution-rate page** returned 404 from the drafting environment — the FAMLI rate percentage is; dates and mechanics below come from the verified FAMLI employer page.

## Rates, bands and thresholds


- **SUI:** every "employer" — any person or governmental entity employing at least one person within Maryland. Most businesses are **contributory employers** (pay quarterly unemployment taxes based on benefit charges and taxable wages); government entities and certain non-profits may elect **reimbursable** status (reimburse benefits charged instead of paying contributions). (Labor & Employment §8-101 et seq. via DOL page, read 2026-10-27.)
- **FAMLI:** all Maryland employers and covered employees from the program's 2027 start; employees of small employers pay a reduced share (see §3).

## The taxable base


| Item | Amount / rule | Source |
|---|---|---|
| SUI taxable wage base | **$8,500** per employee per **calendar** year (first $8,500 of wages) | DOL SUI tax-rate page, read 2026-10-27 | (not yet confirmed)
| SUI experience rates 2026 | **0.30% – 7.50%**; Tax Table A in effect for 2026 (same table as 2025; Tables A–F keyed to the UI Trust Fund balance, A = lowest) | DOL page, read 2026-10-27 | (not yet confirmed)
| Standard rate | **7.50%** — assigned when an employer has no taxable wages in a fiscal year because it failed to file quarterly tax and wage reports | DOL page, read 2026-10-27 | (not yet confirmed)
| New-employer rate | **1.0% – 2.6%**; out-of-state construction contractors get the Maryland construction-industry average rate | DOL page, read 2026-10-27 |
| Rate mechanics | benefit ratio = benefit charges ÷ taxable wages over the 3 fiscal years, mapped to the active tax table | DOL page, read 2026-10-27 |
| FAMLI contribution rate | — the published rate page 404'd on 2026-10-27; program contributions begin with the first quarterly remittance **April 2027** | FAMLI employer page, read 2026-10-27 |
| FAMLI small-employer relief | small employers remit only **50% of the total contribution rate** and may withhold that amount from employee pay | FAMLI employer page, read 2026-10-27 |

## Deadlines and filing


- **SUI quarterly reports and contributions:** quarterly (Form MW-506 series with the wage report); the fiscal year for rate purposes runs 1 July – 30 June while taxable wages are tracked on the calendar year. (DOL page, read 2026-10-27.)
- **FAMLI:** employer registration live now; **quarterly wage and hour reports** electronically through paidleave.maryland.gov **starting April 2027**; **contributions remitted quarterly starting April 2027** unless enrolled in an approved private plan. Notice to employees one pay period before payroll deductions begin. (FAMLI employer page, read 2026-10-27.)
- Benefits become payable from **1 January 2028** (up to 12 weeks, paid up to $1,000/week). (FAMLI landing page, read 2026-10-27.)

## Penalties and interest


- **SUI interest: 1.5% per month** on unpaid contribution and reimbursement balances. (DOL page, read 2026-10-27.) (not yet confirmed)
- Failure to file quarterly reports converts the employer to the 7.50% standard rate (see §3) — a rate penalty as much as a cash one. (not yet confirmed)
- FAMLI penalty schedule: (regulations page not fetched).

## Cross-border points


- SUI wage base and rates apply to services performed **in Maryland**; multi-state employers allocate under the interstate reciprocal coverage arrangements (45-state agreement) — register in the state where the localizability rules place the employment.
- FAMLI covers Maryland employment; employees working remotely across state lines should check the other state's paid-leave program to avoid double contribution.
- Reciprocal-income-tax states (PA/VA/WV/DC) affect income-tax withholding only, not SUI — see `md-payroll` and `md-cross-border`.

## Worked examples


**Example 1 — SUI contribution for one employee.** Employer rated 2.40%; one employee paid $60,000 in Maryland during 2026. (not yet confirmed)

```oa-check
name: MD SUI per-employee contribution
inputs:
 wage_base: 8500
 rate: 0.024
steps:
 - taxable: min(60000, wage_base)
 - contribution: taxable * rate
expected:
 taxable: 8500.00
 contribution: 204.00
```

**Example 2 — late SUI payment interest.** A $12,000 quarterly contribution is paid 3 months late. (not yet confirmed)

```oa-check
name: MD SUI late interest
inputs:
 due: 12000
 monthly: 0.015
 months: 3
steps:
 - interest: due * monthly * months
 - total: due + interest
expected:
 interest: 540.00
 total: 12540.00
```

## Ask the client first


1. Which tax table and benefit ratio produced the 2026 rate — and does the employer want to pay down benefit charges to buy a lower rate?
2. Are quarterly MW-506 wage reports complete — any risk of the 7.50% standard rate? (not yet confirmed)
3. Is the employer small-employer eligible for FAMLI, and will it use a private plan instead of the state fund?
4. Multi-state workforce: where is each employee's employment localized for SUI?
5. Any reimbursable (government/non-profit) election in place?

## Sources


| Source | What it covers | Read on |
|---|---|---|

Not yet confirmed: the FAMLI contribution-rate percentage (the published rate page 404'd on 2026-10-27) and the FAMLI penalty schedule (regulations page not fetched).

## Talk to a verified accountant

No Maryland-specific rule was found in the sources read for this topic.

<!-- openaccountants-cta-block -->

### Talk to a verified accountant

**Talk to a verified accountant** — for Maryland questions on live client facts, book time with an OA Partner.
